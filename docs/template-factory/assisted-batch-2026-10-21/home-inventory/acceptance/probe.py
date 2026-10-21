"""Core real HTTP assertions. Run only against a disposable, tester-owned app."""
import argparse,json,urllib.request,urllib.error,tempfile,socket,subprocess,sys,time
from pathlib import Path

def call(base,path,data=None,expected=200):
 req=urllib.request.Request(base+path,None if data is None else json.dumps(data).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req,timeout=5) as r:status=r.status;result=json.load(r)
 except urllib.error.HTTPError as e:status=e.code;result=json.load(e)
 assert status==expected,(path,status,result)
 return result

def journey(base,case):
 room=call(base,'/api/locations',{'name':'Probe-'+case},201)['id']
 other=call(base,'/api/locations',{'name':'Other-'+case},201)['id']
 a=call(base,'/api/items',{'name':'Desk-'+case,'location_id':room,'value':'100.00','notes':'Maple receipt'},201)
 call(base,'/api/items',{'name':'Lamp-'+case,'location_id':room,'value':'20.00','notes':''},201)
 state=call(base,'/api/state?location='+room);assert state['summary']=={'count':2,'total_minor':12000}
 b=call(base,'/api/items/update',{'id':a['id'],'revision':a['revision'],'name':a['name'],'location_id':room,'value':'90.00','notes':a['notes']})
 assert call(base,'/api/state?location='+room)['summary']['total_minor']==11000
 for value in ('-1','0.001','NaN','1e2'):
  bad=call(base,'/api/items',{'name':'bad','location_id':room,'value':value,'notes':''},400);assert bad['error']['code']=='invalid_value'
 call(base,'/api/items/update',{'id':a['id'],'revision':a['revision'],'name':'stale','location_id':room,'value':'2','notes':''},409)
 b=call(base,'/api/items/update',{'id':b['id'],'revision':b['revision'],'name':b['name'],'location_id':other,'value':'90','notes':b['notes']})
 assert call(base,'/api/state?location='+room)['summary']['count']==1
 assert call(base,'/api/state?q=maple')['items'][0]['id']==b['id']
 call(base,'/api/items/archive',{'id':b['id']})
 assert not call(base,'/api/state?q=maple')['items']
 assert call(base,'/api/state?view=archive&q=maple')['items'][0]['id']==b['id']
 call(base,'/api/items/archive',{'id':b['id']})
 assert call(base,'/api/state?q=maple')['items'][0]['value_minor']==9000
 return call(base,'/api/state?view=all')

def owned_restart(root):
 with tempfile.TemporaryDirectory() as data:
  with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
  base='http://127.0.0.1:'+str(port)
  command=[sys.executable,str(Path(root)/'app/serve.py'),'--port',str(port),'--data-dir',data]
  def start():
   p=subprocess.Popen(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
   for _ in range(100):
    try:call(base,'/api/health');return p
    except OSError:time.sleep(.05)
   p.terminate();p.wait();raise AssertionError('not ready')
  p=start()
  try:before=journey(base,'restart')
  finally:p.terminate();p.wait(timeout=10)
  p=start()
  try:assert before==call(base,'/api/state?view=all')
  finally:p.terminate();p.wait(timeout=10)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url');p.add_argument('--case',choices=['A01','A02','A03','A04'],required=True);p.add_argument('--app-root');a=p.parse_args()
 if a.case=='A04':owned_restart(a.app_root)
 else:journey(a.base_url,a.case)
 print(json.dumps({'case':a.case,'status':'passed','scope':'real HTTP, not browser evidence'}))
