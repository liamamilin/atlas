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

def state(base):return call(base,'/api/state')
def journey(base,case):
 shelf=call(base,'/api/shelves',{'name':'周末'+case},201)
 book=call(base,'/api/books',{'shelf_id':shelf['id'],'title':'深读'+case,'author':'林','total_pages':200},201)
 call(base,'/api/books/progress',{'id':book['id'],'pages_read':50})
 row=call(base,'/api/state?q=深读')['books'][0];assert row['progress_percent']==25 and row['status']=='reading'
 call(base,'/api/books/progress',{'id':book['id'],'pages_read':200});assert call(base,'/api/state?status=finished')['books'][0]['id']==book['id']
 call(base,'/api/books/progress',{'id':book['id'],'pages_read':100});before=state(base)
 call(base,'/api/books/progress',{'id':book['id'],'pages_read':201},400);assert before==state(base)
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
