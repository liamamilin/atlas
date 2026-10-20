import json,sqlite3,sys
from pathlib import Path
from contextlib import contextmanager
sys.path.insert(0,'application-atlas-production-pack')
from template_factory.plan_revision import PreparedRevisionService,R7_SOURCE_JOB
from template_factory.store import digest
repo=Path('.').resolve(); root=(repo/'application-atlas-production-pack/atlas/template-factory').resolve()
class ReadOnlyStore:
 def __init__(self): self.root=root; self.pack=repo/'application-atlas-production-pack'; self.uri=f'file:{root}/factory.sqlite?mode=ro'
 def checkpoint(self,j,n):
  with sqlite3.connect(self.uri,uri=True) as c:
   row=c.execute('select body from checkpoint where job_id=? and name=?',(j,n)).fetchone()
  return json.loads(row[0]) if row else None
 def job(self,j):
  with sqlite3.connect(self.uri,uri=True) as c:
   row=c.execute('select kind,state,stage,attempt,snapshot,error from job where id=?',(j,)).fetchone()
  return {'kind':row[0],'state':row[1],'stage':row[2],'attempt':row[3],'snapshot':json.loads(row[4]),'error':row[5]}
 @contextmanager
 def connect(self):
  c=sqlite3.connect(self.uri,uri=True); c.row_factory=sqlite3.Row
  try: yield c
  finally: c.close()
store=ReadOnlyStore(); req=json.load(open(repo/'docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/prepare-request.json'))
response=PreparedRevisionService(store).prepare(R7_SOURCE_JOB,req)
out=repo/'docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/prepare-response.json'
out.write_text(json.dumps(response,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('response',response['state'],response['effective_plan_digest'],response['case_design_digest'],response['request_digest'])
print('source refs',response['source_reference_report'].get('valid'))
print('manifest entries',len(response['prepared_program_revision']['entries']))
print('cumulative scope',response['cumulative_repair_scope']['version'],response['cumulative_repair_scope']['edit_paths'])
