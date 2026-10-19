"""Integrity checks and unblinding only after the final independent comparison."""

import hashlib
import json
from pathlib import Path

from collect_results import collect
from run_experiment import hashes

HERE = Path(__file__).resolve().parent


def main():
    comparison_file = HERE / 'evaluation/independent-comparison.json'
    assert comparison_file.exists(), 'no unblinding before independent evaluation finishes'
    comparison = json.loads(comparison_file.read_text())
    assert comparison['condition_mapping_seen'] is False
    protocol = json.loads((HERE / 'control/protocol.json').read_text())
    assert protocol['model'] == 'commandcode/deepseek/deepseek-v4.1-flash'
    freeze = json.loads((HERE / 'control/rubric-freeze.json').read_text())
    assert all(hashlib.sha256((HERE / 'evaluation' / n).read_bytes()).hexdigest() == h for n,h in freeze['sha256'].items())
    apps = {}
    for label in ['X', 'Y']:
        stage = HERE / 'control' / label / 'initial/scenario-review'
        assert json.loads((stage / 'process.json').read_text())['pid'] is None
        assert hashlib.sha256((stage / 'task-prompt.txt').read_bytes()).hexdigest() == protocol['common_prompt_sha256']
        for name, expected in protocol['inputs'][label].items():
            assert hashlib.sha256((stage / name).read_bytes()).hexdigest() == expected
        target = HERE / 'blind' / label / 'initial'
        source_hashes = hashes(target / 'app')
        assert source_hashes == json.loads((target / 'generation.json').read_text())['files']
        assert source_hashes == hashes(HERE / 'evaluation/pair-final/cognitive-review/source' / label / 'application')
        runtime = json.loads((target / 'evidence/runtime-results.json').read_text())
        assert {r['id'] for r in runtime['checks'] if r['kind'] == 'required'} == {f'R{i:02d}' for i in range(1,10)}
        epochs = json.loads((target / 'evidence/processes.json').read_text())['epochs']
        assert epochs and all('stopped_at' in e for e in epochs)
        supplement = json.loads((target / 'supplement/result.json').read_text())
        apps[label] = {'source_hashes': source_hashes, 'runtime_required': {r['id']:r['status'] for r in runtime['checks'] if r['kind']=='required'}, 'supplement': {k:supplement[k] for k in ['outcome','submitted_full_note_verified','expected_note_code_points','actual_note_code_points']}, 'test_services_stopped':True}
    mapping = json.loads((HERE / 'control/mapping.json').read_text())
    collect()
    result = {'experiment':protocol['experiment'],'model':protocol['model'],'template_version':protocol['template_version'],'mapping':mapping,'integrity_verified':True,'independent_comparison_sha256':hashlib.sha256(comparison_file.read_bytes()).hexdigest(),'apps':apps,'caveats':['one scenario, one pair, no statistical causal conclusion','shared Python runtime overrides recommended Node stack','post-review M02b is exploratory and not a changed required gate','text-only independent evaluator audited actual runtime records; evaluator did not execute code','original template acceptance suite not run; no publication or grade promotion']}
    (HERE / 'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'unblinded':mapping,'integrity_verified':True,'supplement':{l:a['supplement'] for l,a in apps.items()}},ensure_ascii=False))


if __name__ == '__main__':
    main()
