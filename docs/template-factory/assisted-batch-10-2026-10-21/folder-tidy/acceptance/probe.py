"""Frozen core HTTP assertions; only use a disposable tester-owned target."""
import argparse,json,urllib.request,urllib.error,tempfile,socket,subprocess,sys,time
from pathlib import Path
from urllib.parse import quote

def call(base,path,data=None,expected=200):
 req=urllib.request.Request(base+quote(path,safe="/?=&"),None if data is None else json.dumps(data).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=5) as r:status=r.status;result=json.load(r)
 except urllib.error.HTTPError as e:status=e.code;result=json.load(e)
 assert status==expected,(path,status,result)
 return result

ROOT=None
def state(base):return {'root':call(base,'/api/state'),'archive':call(base,'/api/state?path=归档')}
def journey(base,case):
 assert ROOT is not None,'requires owned --app-root disposable sandbox'
 sandbox=Path(ROOT)/'sandbox';sandbox.mkdir(exist_ok=True);(sandbox/'note.txt').write_text('keep bytes')
 call(base,'/api/folders',{'path':'归档'},201)
 p=call(base,'/api/preview',{'source':'note.txt','target':'归档/notes.txt'},201)
 assert (sandbox/'note.txt').read_text()=='keep bytes' and not (sandbox/'归档/notes.txt').exists()
 r=call(base,'/api/confirm',{'token':p['token']});assert r['sha256']==p['source_sha256']
 assert not (sandbox/'note.txt').exists() and (sandbox/'归档/notes.txt').read_text()=='keep bytes'
 assert call(base,'/api/confirm',{'token':p['token']})==r
 call(base,'/api/preview',{'source':'../bad','target':'x'},400)
 (sandbox/'another.txt').write_text('second')
 call(base,'/api/preview',{'source':'another.txt','target':'归档/notes.txt'},409)
 p2=call(base,'/api/preview',{'source':'another.txt','target':'归档/second.txt'},201)
 (sandbox/'another.txt').write_text('changed after preview')
 call(base,'/api/confirm',{'token':p2['token']},409)
 assert (sandbox/'another.txt').read_text()=='changed after preview'
 assert (sandbox/'归档/notes.txt').read_text()=='keep bytes'
 (sandbox/'link').symlink_to(sandbox/'归档/notes.txt')
 call(base,'/api/preview',{'source':'link','target':'x'},400)
 return state(base)


def owned(root):
 with tempfile.TemporaryDirectory() as data:
  global ROOT
  ROOT=data
  with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
  base='http://127.0.0.1:'+str(port)
  command=[sys.executable,str(Path(root)/'app/serve.py'),'--port',str(port),'--data-dir',data]
  def start():
   proc=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
   for _ in range(100):
    try:call(base,'/api/health');return proc
    except OSError:time.sleep(.05)
   proc.terminate();raise AssertionError(proc.communicate(timeout=5)[1].decode())
  proc=start()
  try:before=journey(base,'owned')
  finally:proc.terminate();proc.wait(timeout=10)
  proc=start()
  try:assert before==state(base)
  finally:proc.terminate();proc.wait(timeout=10)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url');p.add_argument('--app-root');p.add_argument('--case',choices=['A01','A02','A03','A04'],required=True);a=p.parse_args()
 # Owned mode gives each case a fresh DB and verifies real stop/restart.
 if a.app_root:owned(a.app_root)
 else:journey(a.base_url,a.case)
 print(json.dumps({'case':a.case,'status':'passed','scope':'real HTTP and owned-process restart, not browser evidence'}))
