"""Read-only protection check; run from the repository root with production data mounted."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path.cwd()
sys.path[:0] = [str(ROOT / 'application-atlas-production-pack'), str(ROOT / 'examples/assisted-trials')]
from produce_all_leaves import host, PLAN_ID
from template_factory.cases import CaseLibrary
from template_factory.reference_pilot import ReferencePilotService

folder = ROOT / 'docs/product-review-2026-10-22'
prior = ROOT / 'docs/template-factory/product-reference-convergence-2026-10-22'
read = lambda path: json.loads(path.read_text())
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
baseline = read(folder / 'BASELINE.json')
bad = [p for p, value in baseline['protected_files'].items() if not (ROOT/p).is_file() or sha(ROOT/p) != value]
store, service = host()
state = service.status(PLAN_ID)
cases = [{key: item[key] for key in ('case_id', 'revision', 'digest')} for item in CaseLibrary(store, initialize=False).list_cases()]
before = read(prior / 'CASES_BEFORE.json')
pilot = ReferencePilotService(store).get('reference-two-shapes-2026-10-22')
result = {
    'protected_file_count': len(baseline['protected_files']), 'protected_mismatches': bad,
    'legacy_catalog_unchanged': sha(ROOT/'examples/assisted-trials/CATALOG.json') == read(prior/'PROTECTED_FILES_BEFORE.json')['catalog_sha256'],
    'case_versions_before': len(before), 'case_versions_after': len(cases), 'cases_identical': before == cases,
    'case_new': len([item for item in cases if item not in before]),
    'full': {key: state[key] for key in ('status', 'reason', 'new_calls', 'active_calls', 'deadline', 'model')},
    'pilot_call_count': len(pilot['calls']), 'model_calls_added': 0, 'production_resumed': False,
}
assert not bad and result['cases_identical'] and result['legacy_catalog_unchanged'], result
assert state['status'] == 'paused' and state['new_calls'] == 186 and state['active_calls'] == 0, result
assert len(pilot['calls']) == 12, result
(folder/'PROTECTION_FINAL.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False))
