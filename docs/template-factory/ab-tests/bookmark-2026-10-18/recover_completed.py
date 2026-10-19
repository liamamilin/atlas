"""Preserve delivered tool-authored source for testing after a CLI stream error.

No model call, edits to generated source, guessing missing code, or fabricated pass.
"""

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / "application-atlas-production-pack"))
from template_factory.cli import parse_result  # noqa: E402
from run_experiment import hashes, save  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('label', choices=['X', 'Y'])
    args = parser.parse_args()
    stage = HERE / 'control' / args.label / 'initial' / 'scenario-review'
    target = HERE / 'blind' / args.label / 'initial'
    assert not (target / 'app').exists(), 'never overwrite a frozen app'
    assert json.loads((stage / 'process.json').read_text())['pid'] is None
    summary = json.loads((stage / 'cli-summary.json').read_text())
    assert summary['exit_code'] in [0, 1]
    events = list(map(json.loads, (stage / 'events.jsonl').read_text().splitlines()))
    finishes = [e['part'] for e in events if e.get('type') == 'step_finish']
    errors = [e for e in events if e.get('type') == 'error']
    assert errors and all(e.get('error', {}).get('type') == 'provider.invalid-output' for e in errors)
    text = '\n'.join((e.get('part', {}).get('text') or e.get('text') or '') for e in events if e.get('type') == 'text')
    result = parse_result(text)
    assert isinstance(result.get('files'), list) and 'app.py' in result['files']
    files = [p for p in (stage / 'app').rglob('*') if p.is_file()]
    actual = {p.relative_to(stage / 'app').as_posix() for p in files}
    assert actual == set(result['files']) and 1 <= len(actual) <= 12
    texts = []
    for p in files:
        name = p.relative_to(stage / 'app')
        assert len(name.parts) <= 3 and all(not q.startswith('.') for q in name.parts)
        assert p.suffix in ['.py', '.html', '.css', '.js', '.md', '.json'] and not p.is_symlink()
        content = p.read_bytes()
        assert len(content) < 400_000
        content.decode('utf-8')
        texts.append((name, content))
    for name, content in texts:
        dst = target / 'app' / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(content)
    save(stage / 'result-recovered.json', result)
    recovery = {'label': args.label, 'method': 'extract complete declared final JSON metadata from actual final text; freeze already-written matching files byte-for-byte for testing ONLY', 'provider_events': errors, 'no_model_call': True, 'no_source_edits': True, 'cli_exit_code': summary['exit_code'], 'last_step_reason': finishes[-1].get('reason') if finishes else None, 'file_hashes': hashes(target / 'app'), 'runtime': 'not_yet_run', 'original_failure_kept': True, 'pipeline_status': 'failed; not converted to successful completion', 'limitation': 'Complete source and metadata do not erase nonzero CLI exit or missing clean stop.'}
    save(stage / 'terminal-recovery.json', recovery)
    save(target / 'generation.json', {'label': args.label, 'round': 'initial', 'status': 'delivered_source_cli_failed', 'elapsed': summary['duration_seconds'], 'files': recovery['file_hashes'], 'implemented_claims': result.get('implemented'), 'limits_claims': result.get('limits'), 'execution': 'not_yet_run', 'recovery': recovery})
    print(json.dumps({'label': args.label, 'status': 'frozen_complete_source', 'files': len(files), 'provider_events': len(errors)}))


if __name__ == '__main__':
    main()
