import json, shutil, sys, tempfile, threading
from pathlib import Path
PACK = Path('/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack')
sys.path.insert(0, str(PACK)); sys.path.insert(0, str(PACK / 'tests'))
from test_factory_evidence_link import EvidenceRecoveryPipelineLinkTests, GATE
from evidence_recovery_fixture import JOB_ID
from template_factory.evidence_recovery import PREPARE_SCHEMA, RECOVER_SCHEMA, SOURCE_REF, SOURCE_DIGEST
from template_factory.evidence_grants import EvidenceGrantService, OLD_DEADLINE, RETRY_SCOPE, STAGE_NAME
from template_factory.budget import BudgetLedger
from template_factory.v1_batches import _g1_source_digest, BatchService
from template_factory.store import FactoryError
from template_factory.plan_revision import _r7_repo_root

def fixture(key):
    x=EvidenceRecoveryPipelineLinkTests(); x.setUp()
    gate=dict(GATE, source_tree_digest=_g1_source_digest(x.store.pack.parent))
    req={'schema':PREPARE_SCHEMA,'request_key':key,'source_authorization':{'source_ref':SOURCE_REF,'source_digest':SOURCE_DIGEST},'source_gate':gate}
    return x,req

def cleanup(x):
    x.doCleanups()

def _mutate_checkpoint(x):
    with x.store.connect(True) as con:
        row=con.execute('SELECT body FROM checkpoint WHERE job_id=? AND name=?',(JOB_ID,'blueprint-design-check-0-scenario_scope')).fetchone()
        body=json.loads(row[0]); body['result']['tampered']=True
        con.execute('UPDATE checkpoint SET body=? WHERE job_id=? AND name=?',(json.dumps(body),JOB_ID,'blueprint-design-check-0-scenario_scope'))

def _mutate_program(x):
    job=x.store.job(JOB_ID)
    manifest=job['snapshot']['cognitive_repair']['prepared_revision']['prepared_program_revision']
    root=_r7_repo_root(x.store)
    path=root/manifest['entries'][0]['prepared_ref']
    path.write_bytes(path.read_bytes()+b'\n# tamper\n')

# Four source mutation gates: each prepare rejects before any fake CLI can run.
checks=[]
for label, mutate in [
  ('nonphase_old_input', lambda x: (x.store.root/'jobs'/JOB_ID/'attempt-1'/'blueprint-spec-review-0-ad1379367f3e742a-scenario_scope'/'input.json').write_text('{"mutated":true}')),
  ('old_checkpoint', lambda x: _mutate_checkpoint(x)),
  ('authorization_bytes', lambda x: (x.store.pack.parent/SOURCE_REF).write_bytes((x.store.pack.parent/SOURCE_REF).read_bytes()+b'!')),
  ('prepared_program_bytes', lambda x: _mutate_program(x)),
]:
    x,req=fixture('mutation-'+label)
    try:
        mutate(x)
        try:
            x.service.prepare(JOB_ID,req)
            checks.append((label,'UNEXPECTED_ACCEPT'))
        except FactoryError:
            checks.append((label,'rejected; fake CLI calls=0'))
    finally: cleanup(x)

# Concurrency of exact recovery replay: one durable receipt, same attempt 2.
x,req=fixture('concurrent-recover')
try:
    prepared=x.service.prepare(JOB_ID,req); grant=EvidenceGrantService(x.store,clock=lambda:1792490000,source_gate_validator=lambda _store,gate: gate).register(prepared,req)
    body={'schema':RECOVER_SCHEMA,'grant_id':grant['id'],'request_key':req['request_key'],'proposal_digest':prepared['proposal_digest']}
    barrier=threading.Barrier(2); results=[]
    def recover():
        barrier.wait()
        try: results.append(x.service.recover(JOB_ID,body))
        except Exception as e: results.append(e)
    ts=[threading.Thread(target=recover) for _ in range(2)]
    [t.start() for t in ts]; [t.join() for t in ts]
    successes=[r for r in results if isinstance(r,dict)]
    assert len(successes)==2 and {r['recovery_id'] for r in successes}.__len__()==1 and {r['attempt'] for r in successes}=={2}, results
    checks.append(('concurrent_exact_recover','2 callers returned same recovery receipt, attempt=2'))
    BatchService(x.store).action('plan_87059846caf345d2b2fe690657cf324f','resume')
    claimed=x.store.claim('external-probe'); phase=prepared['materials']['new_phase'];
    with x.store.connect() as con: lease=con.execute('SELECT lease FROM job WHERE id=?',(JOB_ID,)).fetchone()[0]
    ledger=BudgetLedger(x.store,campaign_id='atlas-v1-first-production-2026-10-19',clock=lambda:lease-1)
    kw=dict(identity='product-c42848f63251507bd9d911a5',phase='G1',kind='review',timeout=60,job_id=JOB_ID,
      job_token=claimed['token'],requested_model=phase['requested_model'],stage=phase['operation'],retry=1,retry_scope=RETRY_SCOPE,
      plan_id='plan_87059846caf345d2b2fe690657cf324f',evidence_recovery_id=grant['id'],protocol_context={
      'input_digest':phase['budget_input_digest'],'input_sha256':phase['input_sha256'],'full_payload_digest':phase['full_payload_digest'],
      'budget_input_digest':phase['budget_input_digest'],'prompt_sha256':phase['prompt_sha256'],'source_tree_digest':phase['source_tree_digest'],
      'projection_digest':phase['projection_digest'],'stage_name':phase['stage_name'],'logical_retry_scope':phase['logical_retry_scope'],'operation':phase['operation']})
    barrier=threading.Barrier(2); reservations=[]
    def reserve():
        barrier.wait()
        try: reservations.append(ledger.reserve(**kw))
        except FactoryError as e: reservations.append(e.code)
    ts=[threading.Thread(target=reserve) for _ in range(2)]
    [t.start() for t in ts]; [t.join() for t in ts]
    assert sum(isinstance(r,dict) for r in reservations)==1, reservations
    checks.append(('concurrent_reserve','exactly one reservation won; other denied'))
finally: cleanup(x)

# Fixed deadline is checked inside reserve before grant occupation.
x,req=fixture('deadline-reserve')
try:
    prepared=x.service.prepare(JOB_ID,req); grant=EvidenceGrantService(x.store,clock=lambda:1792490000,source_gate_validator=lambda _store,gate: gate).register(prepared,req)
    x.service.recover(JOB_ID,{'schema':RECOVER_SCHEMA,'grant_id':grant['id'],'request_key':req['request_key'],'proposal_digest':prepared['proposal_digest']})
    BatchService(x.store).action('plan_87059846caf345d2b2fe690657cf324f','resume'); claimed=x.store.claim('deadline-probe')
    phase=prepared['materials']['new_phase']; ledger=BudgetLedger(x.store,campaign_id='atlas-v1-first-production-2026-10-19',clock=lambda:OLD_DEADLINE+1)
    kw=dict(identity='product-c42848f63251507bd9d911a5',phase='G1',kind='review',timeout=60,job_id=JOB_ID,job_token=claimed['token'],
      requested_model=phase['requested_model'],stage=phase['operation'],retry=1,retry_scope=RETRY_SCOPE,plan_id='plan_87059846caf345d2b2fe690657cf324f',
      evidence_recovery_id=grant['id'],protocol_context={'input_digest':phase['budget_input_digest'],'input_sha256':phase['input_sha256'],
      'full_payload_digest':phase['full_payload_digest'],'budget_input_digest':phase['budget_input_digest'],'prompt_sha256':phase['prompt_sha256'],
      'source_tree_digest':phase['source_tree_digest'],'projection_digest':phase['projection_digest'],'stage_name':phase['stage_name'],
      'logical_retry_scope':phase['logical_retry_scope'],'operation':phase['operation']})
    try: ledger.reserve(**kw); checks.append(('expired_deadline_reserve','UNEXPECTED_ACCEPT'))
    except FactoryError as e:
        assert e.code=='budget_deadline',e.code
        assert EvidenceGrantService(x.store).get(grant['id'])['status']=='queued'
        checks.append(('expired_deadline_reserve','budget_deadline; grant remains queued'))
finally: cleanup(x)

for item in checks: print(f'{item[0]}: {item[1]}')
assert all('UNEXPECTED' not in result for _,result in checks), checks
