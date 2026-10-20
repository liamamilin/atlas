import sys,os,json,subprocess,hashlib,sqlite3
from pathlib import Path
from datetime import datetime,timezone
REPO=Path('/Users/milin/2026/软件开发/application-atlas');PACK=REPO/'application-atlas-production-pack';ROOT=PACK/'atlas/template-factory';OUT=Path('/tmp/atlas-additional-recovery-20261020')
sys.path.insert(0,str(PACK))
from template_factory.v1_batches import _g1_source_digest
from template_factory.store import digest
from template_factory import frozen_review_additional as extra
JOB='job_b01427592b164863aab5bedf7b3863bb';PLAN='plan_87059846caf345d2b2fe690657cf324f';HEAD='da15a23a4007fa60158a87ee5a24e3d7b86852a7';TREE='a6f749d0f3785cd982e432362d735c6574ef414aef6688995169aa994ad9e472';CI='docs/template-factory/g1-frozen-review-recovery-2026-10-20/additional-call-authorization/ci-source.json'
def save(name,value):
 p=OUT/name
 raw=json.dumps(value,ensure_ascii=False,indent=2)+'\n'
 if p.exists():
  assert json.loads(p.read_text())==value,'request/record differs: '+str(p)
 else:p.write_text(raw)
 return p

def call(action,name,request=None):
 cmd=['python3','-m','template_factory.batch_cli','--root',str(ROOT),'--pack',str(PACK),action]
 if action in ['frozen-review-prepare','recover-frozen-review']:cmd.append(JOB)
 elif action in ['resume','pause','status','report']:cmd.append(PLAN)
 if request is not None:cmd.extend(['--request',str(request)])
 env=os.environ.copy();env.pop('ATLAS_FACTORY_ROOT',None)
 r=subprocess.run(cmd,cwd=PACK,env=env,capture_output=True,text=True)
 (OUT/(name+'.stdout.json')).write_text(r.stdout);(OUT/(name+'.stderr.log')).write_text(r.stderr)
 save(name+'.receipt.json',{'command':cmd,'returncode':r.returncode,'captured_at':datetime.now(timezone.utc).isoformat()})
 if r.returncode:raise RuntimeError(r.stdout[:1200]+r.stderr[:800])
 return json.loads(r.stdout)

def state(name):
 c=sqlite3.connect((ROOT/'factory.sqlite').as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
 job=dict(c.execute('select * from job where id=?',(JOB,)).fetchone());job['snapshot']=json.loads(job['snapshot'])
 grants=[dict(x) for x in c.execute('select * from tf_evidence_recovery_grant where job_id=? order by created_at',(JOB,))]
 batches=[dict(x) for x in c.execute('select id,state from batch where id in (?,?)',('bat_6b4fc8bf5b4e42d79bc6a9069277e9f0','bat_d13dc5920a574140be85da0ea6f5395b'))]
 try:time_row=[dict(x) for x in c.execute('select * from tf_frozen_review_time_resume')]
 except sqlite3.OperationalError:time_row=[]
 value={'captured_at':datetime.now(timezone.utc).isoformat(),'job':job,'grants':grants,'batches':batches,'time_resumes':time_row,'reservations':[dict(x) for x in c.execute('select * from tf_budget_reservation where campaign_id=? order by created',('atlas-v1-first-production-2026-10-19',))],'business_repairs':c.execute('select count(*) from tf_budget_repair where campaign_id=? and product_id=?',('atlas-v1-first-production-2026-10-19','product-c42848f63251507bd9d911a5')).fetchone()[0]}
 save(name+'.json',value);return value

if __name__=='__main__':
 action=sys.argv[1]
 if action=='prepare':
  assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()==HEAD
  assert _g1_source_digest(REPO)==TREE
  raw=(REPO/CI).read_bytes();archive=json.loads(raw);run=archive['runs'][0]['run'];jobs=archive['runs'][0]['jobs']['jobs']
  assert run['head_sha']==HEAD and run['status']=='completed' and run['conclusion']=='success'
  assert all(any(x['name']==n and x['status']=='completed' and x['conclusion']=='success' for x in jobs) for n in ['check','docker-integration'])
  req={'schema':'atlas.frozen-review-prepare.v1','request_key':extra.REQUEST_KEY,'source_authorization':{'source_ref':extra.AUTH_REF,'source_digest':extra.AUTH_SHA256},'timing_override_authorization':{'source_ref':extra.TIMING_AUTH_REF,'source_digest':extra.TIMING_AUTH_SHA256},'source_gate':{'source_commit':HEAD,'source_tree_digest':TREE,'ci_evidence':[{'path':CI,'sha256':hashlib.sha256(raw).hexdigest(),'run_id':run['id'],'head_sha':HEAD,'required_checks':['check','docker-integration']}]}}
  result=call('frozen-review-prepare','prepare',save('prepare-request.json',req));save('prepared-proposal.json',result);print(json.dumps({'prepared':True,'proposal_digest':result['proposal_digest'],'failed_attempt':result['materials']['binding']['attempt']}))
 elif action=='register':
  req=json.loads((OUT/'prepare-request.json').read_text());proposal=json.loads((OUT/'prepared-proposal.json').read_text());result=call('frozen-review-grant-register','register',save('grant-request.json',{'prepared_proposal':proposal,'request':req}));save('grant-response.json',result);s=state('post-register-state');assert s['job']['attempt']==2 and s['job']['state']=='needs_review' and not s['time_resumes'] and len(s['reservations'])==81 and s['business_repairs']==7;print(json.dumps({'grant_id':result['id'],'status':result['status'],'time_activated':False}))
 elif action=='recover':
  grant=json.loads((OUT/'grant-response.json').read_text());proposal=json.loads((OUT/'prepared-proposal.json').read_text());req={'schema':'atlas.frozen-review-recovery.v1','grant_id':grant['id'],'request_key':extra.REQUEST_KEY,'proposal_digest':proposal['proposal_digest']};result=call('recover-frozen-review','recover',save('recover-request.json',req));s=state('post-recover-state');assert s['job']['attempt']==3 and s['job']['state']=='queued' and len(s['time_resumes'])==1 and len(s['reservations'])==81 and s['business_repairs']==7 and all(x['state']=='paused' for x in s['batches']);assert digest(s['job']['snapshot'])=='db51b4ca834dd031135025d761b46407f02b2850ad993c950f55407a0f95fcf6';old=next(g for g in s['grants'] if g['id']==extra.PREDECESSOR_GRANT);assert old['status']=='consumed' and old['consumed_reservation_id']==extra.PREDECESSOR_RESERVATION;print(json.dumps({'result':result,'time_resume':s['time_resumes'][0]}))
 elif action=='replay':
  a=call('frozen-review-grant-register','register-replay',OUT/'grant-request.json');b=call('recover-frozen-review','recover-replay',OUT/'recover-request.json');s=state('post-replay-state');before=json.loads((OUT/'post-recover-state.json').read_text());assert s['time_resumes']==before['time_resumes'] and s['job']['attempt']==3 and s['job']['state']=='queued' and b['replayed'];print(json.dumps({'grant_id':a['id'],'recovery_replayed':b['replayed'],'same_window':True,'actual_attempt':s['job']['attempt']}))
 elif action=='resume':
  s=state('pre-resume-state');assert s['job']['attempt']==3 and s['job']['state']=='queued';result=call('resume','resume');print(json.dumps({'resumed':True,'batch_state':result['batch']['state']}))
 elif action in ['pause','status','report']:
  result=call(action,action);print(json.dumps({'action':action,'completed':True}))
 else:raise ValueError(action)
