"""Frozen real-time timer journey; disposable test-owned target, not run yet.
Natural 1 minute focus + 5 minute break can take >6 minutes. No fake time proof.
"""
import argparse,json,urllib.request,urllib.error,time

def call(base,path,data=None,status=200):
 req=urllib.request.Request(base+path,None if data is None else json.dumps(data).encode(),{'Content-Type':'application/json'})
 try:
  with urllib.request.urlopen(req) as r:code=r.status;value=json.load(r)
 except urllib.error.HTTPError as e:code=e.code;value=json.load(e)
 assert code==status,(code,value)
 return value

def settle_until(base,ident):
 deadline=time.monotonic()+330
 while time.monotonic()<deadline:
  call(base,f'/api/sessions/{ident}/settle',{})
  current=call(base,'/api/state')['current']
  if current['state']=='completed':return
  time.sleep(1)
 raise AssertionError('timer did not complete in bound')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--base-url',required=True);p.add_argument('--case',choices=['A01','A02','A03'],required=True);a=p.parse_args();b=a.base_url
 s=call(b,'/api/sessions',{'goal':'Probe writing','minutes':1},201);ident=s['id']
 call(b,f'/api/sessions/{ident}/pause',{})
 before=call(b,'/api/state');time.sleep(1);after=call(b,'/api/state');assert before['current']['remaining_seconds']==after['current']['remaining_seconds']
 call(b,f'/api/sessions/{ident}/resume',{});settle_until(b,ident)
 final=call(b,'/api/state');assert final['totals']['completed_focus']==1 and final['totals']['focus_seconds']==60
 call(b,f'/api/sessions/{ident}/settle',{});assert call(b,'/api/state')['totals']==final['totals']
 br=call(b,'/api/break',{'minutes':5},201);settle_until(b,br['id']);assert call(b,'/api/state')['totals']==final['totals']
 cancel=call(b,'/api/sessions',{'goal':'Cancel me','minutes':1},201);call(b,f'/api/sessions/{cancel["id"]}/cancel',{});assert call(b,'/api/state')['totals']==final['totals']
 call(b,'/api/sessions',{'goal':'bad','minutes':0},400)
 print(json.dumps({'case':a.case,'status':'http_passed','remaining':'Browser refresh and same-data-dir restart require separate evidence. Not passed until executed.'}))
