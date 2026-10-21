"""Frozen core HTTP assertions; only use a disposable tester-owned target."""
import argparse,json,urllib.request,urllib.error,tempfile,socket,subprocess,sys,time
from pathlib import Path

def call(base,path,data=None,expected=200):
 req=urllib.request.Request(base+path,None if data is None else json.dumps(data).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=5) as r:status=r.status;result=json.load(r)
 except urllib.error.HTTPError as e:status=e.code;result=json.load(e)
 assert status==expected,(path,status,result)
 return result

def state(base):return call(base,'/api/state?date=2026-11-02')
def journey(base,case):
 p=call(base,'/api/projects',{'name':'项目'+case},201)
 data={'project_id':p['id'],'date':'2026-11-02','start':'09:00','end':'11:00','break_minutes':15,'notes':''}
 a=call(base,'/api/entries',data,201);assert state(base)['summary']['total_minutes']==105
 call(base,'/api/entries',{**data,'start':'13:00','end':'14:00','break_minutes':0},201);assert state(base)['summary']['total_minutes']==165
 call(base,'/api/entries/update',{**data,'id':a['id'],'break_minutes':30});assert state(base)['summary']['total_minutes']==150
 before=state(base);call(base,'/api/entries',{**data,'start':'10:00','end':'12:00'},409);assert before==state(base)
 assert call(base,'/api/state?date=2026-11-03')['summary']['total_minutes']==0
 return state(base)


def owned(root):
 with tempfile.TemporaryDirectory() as data:
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
