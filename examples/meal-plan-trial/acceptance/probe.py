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

START='2026-11-02';END='2026-11-08'
def state(base):return call(base,'/api/state?start='+START+'&end='+END)
def totals(base):return {(i['name'],i['unit']):i['quantity_minor'] for i in state(base)['shopping']['items']}
def journey(base,case):
 recipe=call(base,'/api/recipes',{'name':'番茄蛋'+case,'base_servings':2,'ingredients':[{'name':'番茄','unit':'g','quantity':'300'},{'name':'鸡蛋','unit':'个','quantity':'2'}]},201)
 a=call(base,'/api/plans',{'date':START,'recipe_id':recipe['id'],'servings':2},201)
 b=call(base,'/api/plans',{'date':'2026-11-03','recipe_id':recipe['id'],'servings':4},201)
 assert totals(base)=={('番茄','g'):90000,('鸡蛋','个'):600}
 call(base,'/api/plans/update',{'id':b['id'],'servings':2})
 assert totals(base)=={('番茄','g'):60000,('鸡蛋','个'):400}
 call(base,'/api/plans/toggle',{'id':a['id']})
 assert totals(base)=={('番茄','g'):30000,('鸡蛋','个'):200}
 before=state(base)
 for path,payload in [('/api/plans/update',{'id':b['id'],'servings':0}),('/api/plans',{'date':'2026-02-30','recipe_id':recipe['id'],'servings':2}),('/api/recipes',{'name':'bad','base_servings':2,'ingredients':[{'name':'x','unit':'g','quantity':'NaN'}]})]:
  call(base,path,payload,400);assert before==state(base)
 call(base,'/api/plans',{'date':START,'recipe_id':recipe['id'],'servings':2},409)
 call(base,'/api/shopping?start='+START+'&end=2026-11-09',expected=400)
 assert call(base,'/api/shopping?start=2026-11-09&end=2026-11-15')['items']==[]
 call(base,'/api/plans/toggle',{'id':a['id']})
 assert totals(base)=={('番茄','g'):60000,('鸡蛋','个'):400}
 other=call(base,'/api/recipes',{'name':'番茄汁'+case,'base_servings':1,'ingredients':[{'name':'番茄','unit':'ml','quantity':'100'}]},201)
 call(base,'/api/plans',{'date':'2026-11-04','recipe_id':other['id'],'servings':1},201)
 assert totals(base)=={('番茄','g'):60000,('鸡蛋','个'):400,('番茄','ml'):10000}
 call(base,'/api/plans/toggle',{'id':b['id']})
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
