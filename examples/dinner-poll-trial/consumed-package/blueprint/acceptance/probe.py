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

def state(base):
 rows=call(base,'/api/polls')['polls']
 return [call(base,'/api/polls/'+p['id']) for p in rows]
def journey(base,case):
 p=call(base,'/api/polls',{'title':'聚餐'+case,'options':['面馆','火锅']},201)
 other=call(base,'/api/polls',{'title':'另一场'+case,'options':['披萨','寿司']},201)
 a,b=[o['id'] for o in p['options']]
 def vote(name,option,expected=200):return call(base,'/api/votes',{'poll_id':p['id'],'participant':name,'option_id':option},expected)
 vote('小林',a);r=vote('小周',b)
 assert [o['count'] for o in r['options']]==[1,1] and r['total_votes']==2
 r=vote(' 小林 ',b);assert [o['count'] for o in r['options']]==[0,2] and r['total_votes']==2
 before=state(base)
 vote(' ',a,400);vote('小李',other['options'][0]['id'],400)
 call(base,'/api/polls',{'title':'bad','options':[' A ','a']},400)
 assert before==state(base)
 call(base,'/api/polls/close',{'id':p['id']});closed=state(base)
 e=vote('小李',a,409);assert e['error']['code']=='poll_closed' and closed==state(base)
 call(base,'/api/polls/close',{'id':p['id']});assert closed==state(base)
 call(base,'/api/polls/reopen',{'id':p['id']});r=vote('小李',a)
 assert [o['count'] for o in r['options']]==[1,2] and r['total_votes']==3
 assert call(base,'/api/polls/'+other['id'])['total_votes']==0
 call(base,'/api/polls/close',{'id':p['id']})
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
