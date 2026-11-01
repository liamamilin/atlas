"""Run from any directory after the batch: verify stored source bindings, not semantic completeness."""
from pathlib import Path
import json
import re
import sys

REPO = Path(__file__).resolve().parents[2]
PACK = REPO / 'application-atlas-production-pack'
sys.path.insert(0, str(PACK))
from oss_catalog import AUTO_LEAVES, CatalogStore, canonical, decode_file, digest, plain_text
from oss_discovery import ROOT

registry = {}
for directory in ('sources', 'documentation'):
    for path in (ROOT / directory).glob('*.json'):
        value = json.loads(path.read_text())
        files = [value.get('readme'), value.get('license')] if directory == 'sources' else [d['file'] for d in value.get('documents', [])]
        for file in files:
            if not file:
                continue
            try:
                raw = decode_file(file)
            except (ValueError, UnicodeError):
                continue
            registry[(file['git_url'], digest(raw))] = plain_text(raw)
store = CatalogStore()
for candidate in store.candidates():
    meta = candidate['data']['meta']
    registry[('', digest(canonical(meta)))] = re.sub(r'\s+', ' ', meta.get('description') or meta['full_name'])
checks, summary = [], []
for leaf in AUTO_LEAVES:
    data = store.catalog(leaf)
    for card in data['projects']:
        assert card['github_url'] == 'https://github.com/' + card['full_name']
        assert card['license']['status'] in {'open_source', 'source_available', 'pending'}
        if card['license']['status'] == 'open_source':
            assert card['license']['source']
        if card['license']['source']:
            source = card['license']['source']
            assert (source['immutable_url'], source['sha256']) in registry
        proofs = [card['summary_evidence'], card['scope_evidence'], *[f['evidence'] for f in card['features']], *[m['evidence'] for m in card['matches']]]
        if card.get('positioning_evidence'):
            proofs.append(card['positioning_evidence'])
        quotes = 0
        for proof in proofs:
            assert proof['source_url'].startswith('https://')
            text = registry[(proof.get('immutable_url', ''), proof['source_sha256'])]
            if proof.get('excerpt'):
                assert proof['excerpt'].casefold() in text.casefold(), (card['full_name'], 'quote mismatch')
                quotes += 1
            else:
                assert proof.get('verification') in {'source_based', 'inferred'}
        for match in card['matches']:
            assert match.get('applicability', 'direct') in {'direct', 'conditional', 'unverified'}
            if match.get('applicability') == 'conditional':
                assert match.get('conditions')
        checks.append({'leaf': leaf, 'repo': card['full_name'], 'repository_id': card['repository_id'], 'proofs': len(proofs), 'quotes_checked': quotes, 'license': card['license']['status'], 'completeness': card.get('completeness', 'legacy'), 'result': 'passed'})
    summary.append({'leaf': leaf, 'scenarios': len(data['scenarios']), 'projects': len(data['projects']), 'unassociated_projects': sum(not p['matches'] for p in data['projects']), 'partial_cards': sum(p.get('completeness') == 'partial' for p in data['projects']), 'associations': sum(len(p['matches']) for p in data['projects']), 'candidate_total': data['discovery']['total'], 'candidate_counts': data['discovery']['counts'], 'licenses': {s: sum(p['license']['status'] == s for p in data['projects']) for s in ['open_source', 'source_available', 'pending']}, 'empty_scenarios': [s['name'] for s in data['scenarios'] if not s['project_count']]})
base = Path(__file__).parent
(base / 'SOURCE_INTEGRITY.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n')
(base / 'DATA_SUMMARY.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
print({'projects_checked': len(checks), 'quotes_checked': sum(c['quotes_checked'] for c in checks), 'summary': summary})
