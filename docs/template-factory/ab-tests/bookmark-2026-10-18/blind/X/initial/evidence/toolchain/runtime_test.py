#!/usr/bin/env python3
"""Independent blind UI test process supervisor; Python standard library only.

Never edits application files. Run only after reviewing the anonymous source.
"""
from __future__ import annotations

import argparse
import ast
import json
import hashlib
import os
from pathlib import Path
import signal
import shutil
import socket
import subprocess
import sys
import time
import urllib.request

HERE = Path(__file__).resolve().parent
NODE = Path('/Users/milin/.nvm/versions/node/v22.21.1/bin/node')


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


def minimal_env():
    # Deliberately do not inherit provider tokens, API credentials, or proxies.
    return {
        'PATH': '/usr/bin:/bin:/usr/sbin:/sbin',
        'LANG': 'en_US.UTF-8', 'LC_ALL': 'en_US.UTF-8',
        'PYTHONIOENCODING': 'utf-8', 'PYTHONUNBUFFERED': '1', 'PYTHONDONTWRITEBYTECODE': '1',
        'HOME': str(Path.home()), 'TMPDIR': '/private/tmp',
    }


def free_port():
    with socket.socket() as sock:
        sock.bind(('127.0.0.1', 0))
        return sock.getsockname()[1]


def static_inventory(app):
    findings = []
    imports = set()
    files = []
    for path in sorted(app.rglob('*')):
        if path.is_file() and '__pycache__' not in path.parts:
            files.append(str(path.relative_to(app)))
        if path.suffix != '.py' or '__pycache__' in path.parts:
            continue
        tree = ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(i.name.split('.')[0] for i in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split('.')[0])
            elif isinstance(node, ast.Call):
                name = ast.unparse(node.func)
                if name in {'eval', 'exec', 'compile', '__import__', 'os.system', 'os.popen'} or name.startswith('subprocess.'):
                    findings.append({'file': str(path.relative_to(app)), 'line': node.lineno, 'call': name})
    local_modules = {p.stem for p in app.glob('*.py')}
    non_stdlib = sorted(imports - set(sys.stdlib_module_names) - local_modules)
    return {'application': str(app), 'files': files, 'imports': sorted(imports),
            'non_stdlib_imports': non_stdlib, 'command_execution_flags': findings,
            'policy': 'Inventory is supplemental; an operator must read source before authorizing execution.'}


class Supervisor:
    def __init__(self, app, evidence):
        self.app, self.evidence = app, evidence
        self.port = free_port()
        self.base_url = f'http://127.0.0.1:{self.port}'
        self.proc = None
        self.log_file = None
        self.epochs = []
        self.data = evidence / 'data-core'
        self.core_data = self.data
        self.sequence = 0

    def start(self):
        self.data.mkdir(parents=True, exist_ok=True)
        self.sequence += 1
        log = self.evidence / f'service-{self.sequence:02d}.log'
        self.log_file = log.open('wb')
        command = [sys.executable, 'app.py', '--port', str(self.port), '--data-dir', str(self.data)]
        self.proc = subprocess.Popen(command, cwd=self.app, env=minimal_env(), stdout=self.log_file,
                                     stderr=subprocess.STDOUT, start_new_session=True)
        epoch = {'number': self.sequence, 'command': command, 'cwd': str(self.app),
                 'data_dir': str(self.data), 'port': self.port, 'pid': self.proc.pid,
                 'log': str(log), 'started_at': time.time()}
        self.epochs.append(epoch)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if self.proc.poll() is not None:
                raise RuntimeError(f'Application exited during startup: {self.proc.returncode}; see {log}')
            try:
                with urllib.request.urlopen(self.base_url, timeout=.5) as response:
                    epoch['http_status'] = response.status
                    epoch['ready_at'] = time.time()
                    return epoch
            except OSError:
                time.sleep(.1)
        raise RuntimeError(f'No loopback response; see {log}')

    def stop(self, sudden=False):
        if self.proc is None:
            return
        if self.proc.poll() is None:
            self.proc.send_signal(signal.SIGKILL if sudden else signal.SIGTERM)
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=5)
        self.epochs[-1].update(stopped_at=time.time(), returncode=self.proc.returncode,
                               stop='SIGKILL' if sudden else 'SIGTERM')
        if self.log_file:
            self.log_file.close()
        self.proc = None

    def probe_failures(self):
        results = []
        bad_data = self.evidence / 'unusable-data-path'
        bad_data.write_text('A regular file, deliberately not a data directory.', encoding='utf-8')
        cases = [('occupied-port', self.port, self.evidence / 'data-occupied-port'),
                 ('unusable-data-dir', free_port(), bad_data)]
        for name, port, data in cases:
            log = self.evidence / f'probe-{name}.log'
            cmd = [sys.executable, 'app.py', '--port', str(port), '--data-dir', str(data)]
            with log.open('wb') as stream:
                proc = subprocess.Popen(cmd, cwd=self.app, env=minimal_env(), stdout=stream,
                                        stderr=subprocess.STDOUT, start_new_session=True)
                try:
                    code = proc.wait(timeout=3)
                    outcome = 'exited'
                except subprocess.TimeoutExpired:
                    proc.terminate()
                    try:
                        code = proc.wait(timeout=3)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                        code = proc.wait(timeout=3)
                    outcome = 'still_running_after_3_seconds_then_stopped'
            results.append({'probe': name, 'command': cmd, 'log': str(log),
                            'outcome': outcome, 'returncode': code,
                            'text': log.read_text(encoding='utf-8', errors='replace')})
        return results

    def handle(self, request):
        action = request['action']
        if action == 'probe_start_failures':
            return {'probes': self.probe_failures()}
        if action in {'restart', 'crash_restart', 'isolate', 'restore', 'explore'}:
            self.stop(sudden=action == 'crash_restart')
            if action == 'isolate':
                self.data = self.evidence / 'data-isolation'
            elif action == 'restore':
                self.data = self.core_data
            elif action == 'explore':
                self.data = self.evidence / 'data-exploration'
            return {'epoch': self.start(), 'base_url': self.base_url}
        raise ValueError(f'Unknown control action {action}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label', required=True, choices=['X', 'Y'])
    parser.add_argument('--app', required=True, type=Path)
    parser.add_argument('--adapter', required=True, type=Path)
    parser.add_argument('--source-reviewed', action='store_true')
    parser.add_argument('--evidence', type=Path)
    args = parser.parse_args()
    app = args.app.resolve()
    evidence = (args.evidence or HERE / 'runtime-evidence' / args.label).resolve()
    evidence.mkdir(parents=True, exist_ok=True)
    tools = evidence / 'toolchain'
    tools.mkdir(exist_ok=True)
    for source in [Path(__file__).resolve(), HERE / 'runtime_test.mjs', args.adapter.resolve()]:
        shutil.copyfile(source, tools / source.name)
    write_json(tools / 'hashes.json', {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in tools.iterdir() if p.is_file()})
    inventory = static_inventory(app)
    write_json(evidence / 'static-inventory.json', inventory)
    if not args.source_reviewed:
        raise SystemExit('Refusing execution: read source and then pass --source-reviewed.')
    if inventory['command_execution_flags'] or inventory['non_stdlib_imports']:
        raise SystemExit('Static inventory found command execution or non-stdlib imports; review before execution.')
    control = evidence / 'control'
    control.mkdir(exist_ok=True)
    supervisor = Supervisor(app, evidence)
    browser_proc = None
    try:
        supervisor.start()
        cmd = [str(NODE), str(HERE / 'runtime_test.mjs'), '--label', args.label,
               '--base-url', supervisor.base_url, '--adapter', str(args.adapter.resolve()),
               '--evidence', str(evidence), '--control', str(control)]
        with (evidence / 'browser-run.log').open('wb') as stream:
            browser_proc = subprocess.Popen(cmd, env=minimal_env(), cwd=HERE,
                                            stdout=stream, stderr=subprocess.STDOUT)
            while browser_proc.poll() is None:
                for request_file in sorted(control.glob('request-*.json')):
                    response_file = control / request_file.name.replace('request-', 'response-')
                    if response_file.exists():
                        continue
                    request = json.loads(request_file.read_text(encoding='utf-8'))
                    try:
                        response = {'ok': True, **supervisor.handle(request)}
                    except Exception as exc:
                        response = {'ok': False, 'error': repr(exc)}
                    write_json(response_file, response)
                time.sleep(.05)
        if browser_proc.returncode:
            raise RuntimeError(f'Browser harness exited {browser_proc.returncode}; see browser-run.log')
    finally:
        if browser_proc is not None and browser_proc.poll() is None:
            browser_proc.terminate()
            browser_proc.wait(timeout=5)
        supervisor.stop()
        write_json(evidence / 'processes.json', {'label': args.label, 'epochs': supervisor.epochs,
                                               'environment_keys': sorted(minimal_env())})


if __name__ == '__main__':
    main()
