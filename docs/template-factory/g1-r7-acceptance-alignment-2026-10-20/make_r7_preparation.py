import json, sqlite3, sys
from pathlib import Path
sys.path.insert(0, 'application-atlas-production-pack')
import template_factory.plan_revision as pr
from template_factory.store import digest
repo=Path('.').resolve()
root=(repo/'application-atlas-production-pack/atlas/template-factory').resolve()
docs=repo/'docs/template-factory/g1-r7-acceptance-alignment-2026-10-20'
con=sqlite3.connect(f'file:{root}/factory.sqlite?mode=ro',uri=True)
con.row_factory=sqlite3.Row
job_row=con.execute('select kind,state,stage,attempt,snapshot,error from job where id=?',(pr.R7_SOURCE_JOB,)).fetchone()
snapshot=json.loads(job_row['snapshot'])
def cp(name):
 r=con.execute('select body from checkpoint where job_id=? and name=?',(pr.R7_SOURCE_JOB,name)).fetchone()
 if not r: raise RuntimeError('missing checkpoint '+name)
 return json.loads(r['body'])
plan_cp=cp('blueprint-plan-0'); facts_cp=cp('blueprint-accepted-facts-view'); design_cp=cp('case-adaptation-prepared-aaf080ba52611126')
fixed_plan=json.loads(con.execute('select body from v1_plan where id=?',(snapshot['v1']['plan_id'],)).fetchone()[0])
patch=json.loads((docs/'patch.json').read_text(encoding='utf-8'))
class SourceStore:
 def __init__(self): self.root=root; self.pack=repo/'application-atlas-production-pack'
 def checkpoint(self,job_id,name): return cp(name) if job_id==pr.R7_SOURCE_JOB else None
store=SourceStore()
manifest=pr.build_program_revision_manifest(store,patch,repo)
binding={
 'job_id':pr.R7_SOURCE_JOB,'attempt':1,'snapshot_digest':digest(snapshot),'stage':'aggregate-semantic-review',
 'job_error_digest':digest(job_row['error']),'plan_checkpoint_name':'blueprint-plan-0','plan_checkpoint_digest':pr.R7_SOURCE_PROPOSAL_DIGEST,
 'proposal_digest':pr.R7_SOURCE_PROPOSAL_DIGEST,'candidate_path':f'jobs/{pr.R7_SOURCE_JOB}/attempt-1/candidate-0/template.json',
 'candidate_sha256':pr.R7_SOURCE_CANDIDATE_SHA256,'aggregate_checkpoint_name':pr.R7_AGGREGATE_CHECKPOINT,'aggregate_checkpoint_digest':pr.R7_AGGREGATE_DIGEST,
 'campaign_id':snapshot['v1']['campaign_id'],'plan_id':snapshot['v1']['plan_id'],'plan_digest':fixed_plan['digest'],
 'product_id':snapshot['v1']['product_id'],'scenario_id':snapshot['scenario']['id'],'scenario_revision':snapshot['scenario']['revision'],
 'case_basis_digest':snapshot['case_basis']['basis_digest'],'facts_view_checkpoint_name':'blueprint-accepted-facts-view',
 'facts_view_checkpoint_digest':facts_cp['digest'],'facts_view_digest':facts_cp['result']['view_digest'],
 'case_design_checkpoint_name':'case-adaptation-prepared-aaf080ba52611126','case_design_checkpoint_digest':design_cp['digest'],
 'cli_total':71,'business_repairs_used':6,'active_jobs':0,'old_grant_id':'pgrant_f3595368c14d4b23b6ab536f6d198007',
 'old_grant_used':1,'previous_amendment_id':'bamd_100a302fe8424d9493dafe62d6e43db9','absolute_deadline':1792495312.855422}
record={
 'schema':'atlas.g1-bounded-revision-authorization.v1','source_ref':pr.R7_AUTHORIZATION_REF,'source_digest':pr.R7_AUTHORIZATION_SHA256,
 'base_proposal_digest':pr.R7_SOURCE_PROPOSAL_DIGEST,'candidate_sha256':pr.R7_SOURCE_CANDIDATE_SHA256,
 'aggregate_checkpoint_digest':pr.R7_AGGREGATE_DIGEST,'patch_ref':pr.R7_PATCH_REF,'patch_digest':digest(patch),
 'program_ref':pr.R7_PROGRAMS_REF,'program_revision_digest':digest(manifest),'binding_digest':digest(binding),
 'allowed_spec_paths':[list(p) for p in sorted(pr.R7_SPEC_PATHS)],'replace_paths':sorted(pr.R7_REPLACE_PATHS),
 'reuse_paths':sorted(set(pr.R7_PROGRAM_PATHS)-pr.R7_REPLACE_PATHS)}
rev_path=docs/pr.R7_APPROVED_REVISION_REF.split('/authorization/')[1] if False else repo/pr.R7_APPROVED_REVISION_REF
rev_path.parent.mkdir(parents=True,exist_ok=True)
rev_path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
request={'schema':pr.R7_PREPARATION_SCHEMA,'binding':binding,'patch':patch,
 'source_authorization':{'source_ref':pr.R7_AUTHORIZATION_REF,'source_digest':pr.R7_AUTHORIZATION_SHA256,
                        'revision_ref':pr.R7_APPROVED_REVISION_REF,'revision_digest':digest(record)},
 'prepared_program_revision':manifest}
(docs/'prepare-request.json').write_text(json.dumps(request,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'binding':binding,'manifest_digest':digest(manifest),'request_digest':digest(request),'revision_digest':digest(record)},ensure_ascii=False,indent=2))
