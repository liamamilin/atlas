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
    parser.add_argument('--label', choices=['X', 'Y'], required=True)
    parser.add_argument('--app', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, required=True)
    args = parser.parse_args()
    app = args.app.resolve()
    evidence = args.evidence.resolve()
    evidence.mkdir(parents=True, exist_ok=False)
    inventory = static_inventory(app)
    assert not inventory['command_execution_flags'] and not inventory['non_stdlib_imports']
    write_json(evidence / 'static-inventory.json', inventory)
    write_json(evidence / 'probe-scope.json', {
        'id': 'M02b', 'posthoc_exploration': True,
        'trigger': 'Independent first review flagged untested risk of accepted long notes being silently truncated. Test same input through both UIs; do not change R01-R09 judgments or create a new acceptance threshold.',
        'source_hashes': {p.relative_to(app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in app.rglob('*') if p.is_file() and '__pycache__' not in p.parts},
    })
    for f in [Path(__file__), HERE / 'supplement.mjs', HERE / ('adapters.' + args.label + '.mjs')]:
        shutil.copyfile(f, evidence / f.name)
    supervisor = Supervisor(app, evidence)
    try:
        supervisor.start()
        cmd = [str(NODE), str(HERE / 'supplement.mjs'), '--label', args.label, '--base-url', supervisor.base_url,
               '--adapter', str(HERE / ('adapters.' + args.label + '.mjs')), '--evidence', str(evidence)]
        with (evidence / 'browser-run.log').open('wb') as log:
            code = subprocess.run(cmd, env=minimal_env(), stdout=log, stderr=subprocess.STDOUT, timeout=120).returncode
        assert code == 0, 'probe tool failed; inspect browser-run.log'
    finally:
        supervisor.stop()
        write_json(evidence / 'processes.json', {'epochs': supervisor.epochs, 'label': args.label})


if __name__ == '__main__':
    main()
