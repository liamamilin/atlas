"""Check this sample's traceability and tamper manifest; not a product review."""
import hashlib
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parent
v = json.loads((root / 'template.json').read_text())
def ids(key):
    return {item['id'] for item in v[key]}
assert json.loads((root/'inputs/scenario.json').read_text()) == v['scenario']
for key in ['sources', 'features', 'decisions', 'phases', 'acceptance', 'roles']:
    assert len(ids(key)) == len(v[key]), f'duplicate {key} id'
for f in v['features']:
    assert set(f['sources']) <= ids('sources'), f['id']
    assert set(f['acceptance']) <= ids('acceptance'), f['id']
    if f['phase']:
        assert f['phase'] in ids('phases') and f['acceptance'], f['id']
for a in v['acceptance']:
    assert set(a['features']) <= ids('features') and a['phase'] in ids('phases')
    for f in a['features']:
        assert a['id'] in next(i for i in v['features'] if i['id'] == f)['acceptance']
        assert a['phase'] == next(i for i in v['features'] if i['id'] == f)['phase']
    assert re.search(r'\b'+a['id']+r':async', (root/'acceptance/run.cjs').read_text()), a['id']+' missing executor'
assert json.loads((root/'acceptance/plan.json').read_text())['cases'] == v['acceptance']
for p in v['phases']:
    assert set(p['acceptance']) == {a['id'] for a in v['acceptance'] if a['phase']==p['id']}
    assert set(p['features']) == {f['id'] for f in v['features'] if f['phase']==p['id']}
manifest=json.loads((root/'integrity.json').read_text())['sha256']
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='integrity.json' and '__pycache__' not in p.parts and 'node_modules' not in p.parts}
assert set(manifest)==actual, 'unlisted or missing files'
for rel, expected in manifest.items():
    path = root/rel
    assert path.resolve().is_relative_to(root.resolve()) and not path.is_symlink()
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, rel
print(json.dumps({'scope':'structure and traceability only','features':len(v['features']),'decisions':len(v['decisions']),'acceptance':len(v['acceptance']),'passed':True}))
