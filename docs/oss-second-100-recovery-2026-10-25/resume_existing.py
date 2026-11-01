"""Resume the original interrupted targets without stopping the healthy API."""
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys

os.environ["ATLAS_OSS_MODEL_CONCURRENCY"] = "4"
BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, now
from oss_batch import BatchJobs

IDENTIFIER = "batch_9ab8ea47e4ef450cbb4afe5b295594e3"
store = CatalogStore(bootstrap=False)
jobs = BatchJobs(store)
job = jobs.get(IDENTIFIER, detect_interruption=False)
targets = jobs.interrupted_targets(job)
if not targets:
    assert job['status'] == 'interrupted' and job.get('restored_interruptions')
    previously_restored = {(x['leaf'], x['repository_id']) for x in job['restored_interruptions'][-1]['targets']}
    targets = [(leaf, item) for leaf, items in job['targets'].items() for item in items
               if (leaf, item['repository_id']) in previously_restored and item['status'] in {'pending', 'running'}]
assert len(targets) == 16
assert {leaf for leaf, _ in targets} == {"outliner"}
assert len(job["leaves"]) == len(job["prepared"]) == 100
target_keys = {(leaf, item["repository_id"]) for leaf, item in targets}
target_ids = {rid for _, rid in target_keys}

def other_targets(value):
    return hashlib.sha256(canonical([(leaf, item) for leaf, items in value['targets'].items()
        for item in items if (leaf, item['repository_id']) not in target_keys]).encode()).hexdigest()

def invariant():
    result = {}
    with store.connect() as con:
        for key, query in {
            "scenarios": "SELECT * FROM oss_scenario ORDER BY id",
            "other_leaf_matches": "SELECT m.* FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id WHERE s.leaf<>'outliner' ORDER BY m.scenario_id,m.repository_id",
            "other_projects": "SELECT * FROM oss_project ORDER BY repository_id",
            "existing_favorites": "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id",
        }.items():
            checksum = hashlib.sha256()
            for row in con.execute(query):
                if key == 'other_projects' and row[0] in target_ids:
                    continue
                if key == 'existing_favorites' and row[0] not in existing_ids:
                    continue
                checksum.update(canonical(list(row)).encode())
                checksum.update(b'\n')
            result[key] = checksum.hexdigest()
    return result

with store.connect() as con:
    existing_ids = {row[0] for row in con.execute('SELECT repository_id FROM oss_project')}
before = invariant()
before_targets = other_targets(job)
if not (BASE / 'REPLAY_BEFORE.json').exists():
    backup = Path('/private/tmp/atlas-second100-before-target-recovery.sqlite')
    with sqlite3.connect(store.path) as src, sqlite3.connect(backup) as dst:
        src.backup(dst)
    (BASE / 'REPLAY_BEFORE.json').write_text(json.dumps({
        'job_id': IDENTIFIER, 'checked_at': now(), 'status': job['status'], 'processed': job['processed'],
        'total': job['total'], 'interrupted_targets': len(targets), 'backup': str(backup),
        'other_targets_sha256': before_targets, 'invariants': before,
        'healthy_api_restarted': False,
    }, ensure_ascii=False, indent=2) + '\n')
result = jobs.resume(IDENTIFIER)
assert result['id'] == IDENTIFIER and result['leaves'] == job['leaves']
assert result['prepared'] == job['prepared']
assert other_targets(result) == before_targets
assert invariant() == before
new_runs = [rid for rid in result['runs'] if rid not in job['runs']]
run_proofs = []
with store.connect() as con:
    for rid in new_runs:
        run = json.loads(con.execute('SELECT data FROM oss_run WHERE id=?', (rid,)).fetchone()[0])
        run_proofs.append({**{k: run.get(k) for k in ['id','status','processed','total','concurrency','finished_at']},
                           'provider_models': sorted({(r['provider'],r['model']) for r in run.get('model_receipts',[])})})
remaining_failures = sum(t['status'] == 'failed' for items in result['targets'].values() for t in items)
proof = {'job_id': IDENTIFIER, 'checked_at': now(), 'status': result['status'], 'processed': result['processed'],
         'total': result['total'], 'finished_at': result.get('finished_at'), 'remaining_failed_targets': remaining_failures,
         'restored_targets': len(targets), 'other_targets_unchanged': True,
         'other_projects_scenarios_other_leaf_matches_and_favorites_preserved': True,
         'healthy_api_restarted': False, 'new_batch_created': False, 'runs': run_proofs,
         'server_code_reload_pending': True}
(BASE / 'REPLAY_AFTER.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(proof, ensure_ascii=False))
