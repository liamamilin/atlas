"""Read-only post-batch verification; actual localhost downloads, no model/app run."""
import hashlib
import io
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'examples/assisted-trials'))
from produce_with_opencode import verify_production
from produce_batch import ROOT as REPO
from template_factory.store import FactoryStore
from template_factory.budget import BudgetLedger
from template_factory.cases import CaseLibrary

folder = Path(__file__).resolve().parent
req = json.loads((folder / 'BATCH_REQUEST.json').read_text())
base = 'http://127.0.0.1:5199'
def get(path):
    with urllib.request.urlopen(base + path, timeout=90) as response:
        return response.read()

def load(path):
    return json.loads(path.read_text())

pack = REPO / 'application-atlas-production-pack'
store = FactoryStore(pack / 'atlas/template-factory', pack)
ledger = BudgetLedger(store, campaign_id=req['campaign_id'])
before, after = load(folder / 'BUDGET_BEFORE.json'), ledger.snapshot()
assert after['active'] == 0, 'wait for all actual CLI sessions to close'
usage = ledger.segment_usage(req['phase'])
assert usage['cli_sessions_used'] <= 9
assert after['cli_sessions_used'] == before['cli_sessions_used'] + usage['cli_sessions_used']
assert all(row['requested_model'] == req['model'] for row in usage['reservations'])
history = ['repairs', 'amendments', 'protocol_retry_grants', 'protocol_retry_grant_uses',
           'evidence_recovery_grants', 'evidence_recovery_grant_uses', 'time_resumes', 'effective_timings', 'limits']
assert all(before[key] == after[key] for key in history)
original = load(folder / 'CATALOG_BEFORE.json')['items']
catalog = json.loads(get('/api/factory/assisted-templates'))
old_downloads = []
for row in original:
    item = next(x for x in catalog['items'] if x['artifact_id'] == row['artifact_id'])
    assert item['digest'] == row['artifact_digest']
    if row.get('production_review', {}).get('status') != 'needs_changes':
        data = get(item['files']['development']['url'])
        assert hashlib.sha256(data).hexdigest() == row['files']['development']['sha256']
        old_downloads.append({'artifact_id': row['artifact_id'], 'sha256': hashlib.sha256(data).hexdigest()})
    else:
        assert not item['files']['development']['available']
        try:
            get('/api/factory/assisted-templates/' + row['artifact_id'] + '/files/development')
        except urllib.error.HTTPError as error:
            assert error.code == 409
        else:
            raise AssertionError('withdrawn history became usable')
assert len(old_downloads) == 17
results = []
for fixed in req['items']:
    p = folder / fixed['key']
    state = load(folder / (fixed['key'] + '.manifest.json'))['items'][0]
    row = {'key': fixed['key'], 'leaf': fixed['leaf'], 'state': state['state'], 'application_runtime': 'not_run'}
    if (p / 'source-snapshot.json').exists():
        snap = load(p / 'source-snapshot.json')
        row.update(repository=snap['repository'], commit_sha=snap['commit_sha'], source_files=len(snap['files']))
        if not (p / 'upstream-evidence.zip').exists():
            with zipfile.ZipFile(p / 'upstream-evidence.zip', 'w', zipfile.ZIP_DEFLATED) as z:
                for name, expected in snap['files'].items():
                    data = (Path(snap['local_root']) / name).read_bytes()
                    assert hashlib.sha256(data).hexdigest() == expected
                    z.writestr(name, data)
                z.writestr('source-snapshot.json', (p / 'source-snapshot.json').read_bytes())
    review_path = p / 'audit/blueprint-spec-review-aux/RESULT.json'
    if review_path.exists():
        reviewed = load(review_path)
        row.update(review=reviewed['verdict'], issues=reviewed.get('issues', []), checks=reviewed.get('checks'))
    if (p / 'IMPORT_RECEIPT.json').exists():
        receipt = load(p / 'IMPORT_RECEIPT.json')
        authored, production, snap = (load(p / name) for name in ('AUTHOR_INPUT.json', 'MODEL_PRODUCTION.json', 'source-snapshot.json'))
        verify_production(p, production, authored, snap)
        assert production['model'] == req['model']
        item = next(x for x in catalog['items'] if x['artifact_id'] == receipt['artifact_id'])
        assert item['production']['review_status'] == 'passed' and item['runtime']['status'] == 'not_run'
        assert item['strict_status']['publication'] == 'draft'
        data = get(item['files']['development']['url'])
        assert hashlib.sha256(data).hexdigest() == receipt['exported_zip_sha256']
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            start_files = ['HANDOFF.md', 'KNOWLEDGE.md', 'CURRENT_PHASE.json', 'ACCEPTANCE_CONTRACT.json', 'APP_DELIVERY.md', 'PROJECT_DECISIONS.json']
            assert all(name in z.namelist() for name in start_files)
            assert json.loads(z.read('.atlas-blueprint.json'))['template_digest'] == receipt['digest']
            case = load(p / 'case-record.json')
            assert json.loads(z.read('blueprint/inputs/shared-case-record.json')) == case
            assert json.loads(z.read('blueprint/inputs/model-production.json')) == production
            formal = json.loads(get('/api/factory/v1/cases/' + case['case_id'] + '/revisions/' + str(case['revision'])))
            assert formal['digest'] == case['digest']
        row.update(title=authored['name'], artifact_id=receipt['artifact_id'], artifact_digest=receipt['digest'],
                   development_sha256=hashlib.sha256(data).hexdigest(), url=receipt['url'], download=item['files']['development']['url'],
                   case_ref=receipt['case_ref'], review_input_digest=production['review_input_digest'],
                   review_result_digest=production['review_result_digest'], source_observations=len(authored['observations']),
                   start_files=start_files)
    else:
        row['failure'] = load(p / 'FAILURE.json') if (p / 'FAILURE.json').exists() else {'error': state.get('error')}
    if (p / 'review-materials').exists():
        with zipfile.ZipFile(p / 'review-materials.zip', 'w', zipfile.ZIP_DEFLATED) as z:
            for file in sorted((p / 'review-materials').rglob('*')):
                if file.is_file():
                    z.write(file, file.relative_to(p / 'review-materials'))
    results.append(row)
old_cases = {(c['case_id'], c['revision']): c['digest'] for c in load(folder / 'CASES_BEFORE.json')}
new_cases = {(c['case_id'], c['revision']): c['digest'] for c in CaseLibrary(store).list_cases()}
assert all(new_cases[key] == value for key, value in old_cases.items())
protected = load(folder / 'PRESERVATION_BEFORE.json')
changes = [name for name, expected in protected.items() if not Path(name).is_file() or hashlib.sha256(Path(name).read_bytes()).hexdigest() != expected]
assert not changes, changes
passed = sum('artifact_id' in row for row in results)
assert catalog['counts']['usable'] == 17 + passed
assert catalog['counts']['total'] == 18 + passed
report = {'model': req['model'], 'items': results, 'full_static_flow_success': passed, 'sample_count': 3,
          'catalog_counts': catalog['counts'], 'cases_added': len(new_cases) - len(old_cases),
          'applications_run_added': 0, 'upstream_run_added': 0, 'strict_publications_added': 0,
          'calls_before': before['cli_sessions_used'], 'calls_after': after['cli_sessions_used'],
          'segment_usage': usage, 'old_downloads': old_downloads, 'strict_history_unchanged': history,
          'protected_files_unchanged': len(protected), 'original_case_versions_unchanged': len(old_cases),
          'gates': json.loads(get('/api/factory/v1/gates?campaign_id=' + req['campaign_id']))}
(folder / 'REAL_API_RESULTS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ['full_static_flow_success', 'sample_count', 'catalog_counts', 'cases_added', 'calls_after', 'protected_files_unchanged']}, indent=2))
