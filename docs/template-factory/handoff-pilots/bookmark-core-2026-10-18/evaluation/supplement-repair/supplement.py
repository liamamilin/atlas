"""Post-review M02b: identical long-note retention probe, no ranking changes."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

from runtime_test import HERE, NODE, Supervisor, minimal_env, static_inventory, write_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', choices=['C'], required=True)
    parser.add_argument('--app', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, required=True)
    parser.add_argument('--adapter', type=Path)
    parser.add_argument('--probe', type=Path)
    args = parser.parse_args()
    adapter = (args.adapter or HERE / ('adapters.' + args.label + '.mjs')).resolve()
    probe = (args.probe or HERE / 'supplement.mjs').resolve()
    app = args.app.resolve()
    evidence = args.evidence.resolve()
    evidence.mkdir(parents=True, exist_ok=False)
    inventory = static_inventory(app)
    assert not inventory['command_execution_flags'] and not inventory['non_stdlib_imports']
    write_json(evidence / 'static-inventory.json', inventory)
    write_json(evidence / 'probe-scope.json', {
        'id': 'M02b', 'posthoc_exploration': False,
        'trigger': 'Prespecified follow-up probe from the prior A/B lesson: same 3420-codepoint logical note; preserve R01-R09 definitions and report the additional observation separately.',
        'source_hashes': {p.relative_to(app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in app.rglob('*') if p.is_file() and '__pycache__' not in p.parts},
    })
    for f in [Path(__file__), probe, adapter]:
        shutil.copyfile(f, evidence / f.name)
    supervisor = Supervisor(app, evidence)
    try:
        supervisor.start()
        cmd = [str(NODE), str(probe), '--label', args.label, '--base-url', supervisor.base_url,
               '--adapter', str(adapter), '--evidence', str(evidence)]
        with (evidence / 'browser-run.log').open('wb') as log:
            code = subprocess.run(cmd, env=minimal_env(), stdout=log, stderr=subprocess.STDOUT, timeout=120).returncode
        assert code == 0, 'probe tool failed; inspect browser-run.log'
    finally:
        supervisor.stop()
        write_json(evidence / 'processes.json', {'epochs': supervisor.epochs, 'label': args.label})


if __name__ == '__main__':
    main()
