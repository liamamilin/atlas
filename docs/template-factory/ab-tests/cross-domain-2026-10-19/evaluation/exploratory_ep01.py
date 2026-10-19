#!/usr/bin/env python3
"""EP01: explicitly posthoc plan-id containment probe, separate from core v3."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from run import Rename, dump, env, hashes, require, CheckFailure

HERE=Path(__file__).resolve().parent
SENTINEL=b'Atlas synthetic EP01 protected sentinel\nDo not overwrite.\x00\xff'

def outside_snapshot(directory):
    return {str(p.relative_to(directory)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(directory.rglob('*')) if p.is_file() and not p.is_symlink()}

def probe(app,evidence,kind):
    area=evidence/kind;area.mkdir()
    tool=Rename(app,area)
    root=tool.fixture()
    (root/'old-a.txt').write_bytes(b'original synthetic renamed content\n\x00\xff')
    (root/'keep.txt').write_bytes(b'untouched synthetic file')
    outside=area/'outside';outside.mkdir()
    (outside/'protected-sentinel.bin').write_bytes(SENTINEL)
    target=outside/'receipt-target.json'
    if kind=='existing_target':
        target.write_bytes(SENTINEL)
    before_outside=outside_snapshot(outside)
    before_inside=tool.snapshot(root)
    plan,_=tool.preview(root)
    parsed=json.loads(plan.read_text(encoding='utf-8'))
    if not isinstance(parsed,dict):
        raise RuntimeError('Expected a JSON plan object to set top-level id; unsupported format remains unverified')
    # Absolute identifier resolves only to this probe's explicitly owned sibling path.
    # Never use ../ traversal or any real user directory.
    identifier=str(target.with_suffix(''))
    require(Path(identifier).is_absolute() and Path(identifier).parent==outside.resolve(), 'Owned absolute identifier required')
    old_id=parsed.get('id')
    parsed['id']=identifier
    plan.write_text(json.dumps(parsed,ensure_ascii=False,indent=2),encoding='utf-8')
    command=[sys.executable,'-B','app.py','--root',str(root),'apply','--plan',str(plan),'--confirm']
    started=time.time()
    proc=subprocess.run(command,cwd=app,env=env(area),capture_output=True,timeout=12)
    event={'command':command,'returncode':proc.returncode,'stdout':proc.stdout.decode('utf-8',errors='replace'),
           'stderr':proc.stderr.decode('utf-8',errors='replace'),'started':started,'finished':time.time()}
    dump(area/'apply-event.json',event)
    dump(area/'preparation-events.json',tool.events)
    after_outside=outside_snapshot(outside)
    after_inside=tool.snapshot(root)
    safe_outside=before_outside==after_outside
    if proc.returncode==0:
        try:
            result=json.loads(event['stdout'])
        except ValueError as error:
            raise CheckFailure('Success stdout must remain valid JSON') from error
        expected={('new-a.txt' if k=='old-a.txt' else k):v for k,v in before_inside.items()}
        safe_inside=after_inside==expected and result.get('status')=='applied'
    else:
        safe_inside=after_inside==before_inside and bool(event['stdout'].strip() or event['stderr'].strip())
    value={'id':'EP01','subprobe':kind,'status':'passed' if safe_outside and safe_inside else 'failed',
           'posthoc':True,'application_command_exit':proc.returncode,'original_plan_id':old_id,
           'tampered_id':identifier,'outside_target':str(target),
           'outside_before':before_outside,'outside_after':after_outside,
           'outside_unchanged':safe_outside,'inside_before':before_inside,'inside_after':after_inside,
           'inside_safe':safe_inside,'meaning':'Safe rejection or safe ignored extra id accepted; any new/changed outside file fails'}
    dump(area/'result.json',value)
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app',type=Path,required=True)
    parser.add_argument('--evidence',type=Path,required=True)
    parser.add_argument('--source-reviewed',action='store_true')
    args=parser.parse_args()
    if not args.source_reviewed:
        parser.error('Manually review every application source file before execution')
    app=args.app.resolve();evidence=args.evidence.resolve()
    if evidence.exists():
        parser.error('New evidence directory required; preserve every prior result')
    if not (app/'app.py').is_file():
        parser.error('No complete app.py')
    frozen=json.loads((HERE/'EP01-freeze.json').read_text())
    for name,digest in frozen['source_sha256'].items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=digest:
            parser.error('Exploratory toolchain changed after freeze: '+name)
    evidence.mkdir(parents=True)
    before=hashes(app)
    values=[]
    for kind in ['absent_target','existing_target']:
        try:
            values.append(probe(app,evidence,kind))
        except Exception as error:
            values.append({'id':'EP01','subprobe':kind,'status':'setup_or_tool_error_unverified','error':f'{type(error).__name__}: {error}'})
    after=hashes(app)
    result={'id':'EP01','kind':'posthoc_exploratory_not_core','tests':values,'application_sha256_before':before,
            'application_sha256_after':after,'application_unchanged':before==after,
            'source_reviewed_operator_assertion':True,'freeze_sha256':hashlib.sha256((HERE/'EP01-freeze.json').read_bytes()).hexdigest(),
            'core_scores_changed':False,'all_executed_checks_passed':all(x['status']=='passed' for x in values)}
    dump(evidence/'result.json',result)
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result['all_executed_checks_passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
