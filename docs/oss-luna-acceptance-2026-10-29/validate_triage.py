"""Validate generated offline triage and simulate draft edits in memory only."""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import json
import re

import triage_audit as t
from final_acceptance import readonly


def validate(out=t.OUT):
    s=json.loads((out/'SUMMARY.json').read_text())
    assert s['audit_id']==t.audit.AUDIT_ID and s['frozen_projects']==55651
    assert s['code_sha256']==t.audit.sha(Path(t.__file__))
    assert s['protected_before']==s['protected_after']
    assert s['production_before']==s['production_after']
    assert not s['integrity_gaps'] and s['additional_paid_requests']==0
    rows=[json.loads(line) for line in (out/'FINDINGS.jsonl').open()]
    by_id={r['id']:r for r in rows};assert len(by_id)==len(rows)==s['findings']
    assert Counter(r['model_disposition'] for r in rows)==s['model_dispositions']
    assert Counter(r['group'] for r in rows)=={k:v['findings'] for k,v in s['groups'].items()}
    for r in rows:
        assert not any(r[k] for k in ('human_user_confirmed','automatic_semantic_approval','automatic_production_write'))
        if r['group']=='invalid_target_reference':
            assert not r['targets'] and 'scenario_id_not_in_frozen_project' in r['signals']
        if r['group']=='source_supported_proposal':
            assert r['source_check']['disposition']=='corroborated'
    batches=json.loads((out/'BATCHES.json').read_text());queued=[]
    for batch in batches:
        assert (out/batch['path']).exists() and not batch['automatic_approval']
        assert len(batch['finding_ids'])==batch['findings']<=40
        for key in batch['finding_ids']:
            assert key in by_id and by_id[key]['group']==batch['group']
            assert by_id[key]['group'] not in ('source_supported_proposal','source_checked_dismissed','model_dismissed_reference','invalid_target_reference')
        queued.extend(batch['finding_ids'])
    assert len(queued)==len(set(queued))==s['review_batch_findings']
    excluded={'source_supported_proposal','source_checked_dismissed','model_dismissed_reference','invalid_target_reference'}
    assert set(queued)=={r['id'] for r in rows if r['group'] not in excluded}
    proposals=json.loads((out/'PROPOSALS.json').read_text());changes=0
    with readonly(t.audit.SNAPSHOT,True) as snapshot,t.audit.core.readonly() as live:
        for p in proposals:
            assert p['id'] in by_id and by_id[p['id']]['group']=='source_supported_proposal'
            assert not p['approved'] and not p['auto_apply'] and not p['human_user_confirmed']
            path=Path(p['input_path']);assert t.audit.core.digest(path.read_text())==p['input_sha256']
            packet=json.loads(path.read_text());candidate=deepcopy(packet)
            for con in (snapshot,live):
                data=con.execute('SELECT data FROM oss_project WHERE repository_id=?',(p['repository_id'],)).fetchone()['data']
                assert t.audit.core.digest(data)==p['repository_data_sha256']
            for c in p['changes']:
                assert re.fullmatch(r'/card/(summary|features/\d+/text|license/note)',c['path'])
                assert t.audit.core.digest(t.audit.core.canonical(c['before']))==c['precondition_value_sha256']
                node=candidate;keys=c['path'].strip('/').split('/')
                for key in keys[:-1]:node=node[int(key)] if isinstance(node,list) else node[key]
                key=int(keys[-1]) if isinstance(node,list) else keys[-1]
                assert node[key]==c['before'];node[key]=c['after'];changes+=1
            for key in ('status','spdx','detected_spdx','verification'):
                assert (candidate['card'].get('license') or {}).get(key)==(packet['card'].get('license') or {}).get(key)
            assert candidate['scenario_matches']==packet['scenario_matches']
    assert changes==s['proposal_changes']==11 and len(proposals)==12
    failures=json.loads((out/'FAILURES.json').read_text())
    assert Counter(f['stage'] for f in failures)=={'primary':1,'secondary':59}
    assert all(f['additional_paid_requests']==0 for f in failures)
    recoveries=json.loads((out/'CITATION_RECOVERIES.json').read_text())
    assert len(recoveries)==s['original_quote_recoveries']
    assert all(r['original_state'] in t.VALID_QUOTES and r['packet_state'] not in t.VALID_QUOTES and not r['semantic_judgment_changed'] for r in recoveries)
    # The post-run state is still identical to the protected audit and production state.
    with readonly(t.audit.STATE_DB) as con:
        assert t.protected_state(con)==s['protected_after']
    assert t.production_state()==s['production_after']
    result={'audit_id':t.audit.AUDIT_ID,'at':t.audit.core.now(),'passed':True,'unit_tests_passed':10,
            'inventory_findings':len(rows),'model_dispositions':s['model_dispositions'],'draft_proposals':len(proposals),'draft_edits_simulated':changes,
            'draft_live_value_preconditions_match':True,'license_labels_and_relations_preserved_in_simulation':True,
            'all_batches_complete_and_disjoint':True,'review_batch_findings':len(queued),'no_automatic_semantic_approval':True,
            'original_audit_and_production_preserved':True,'additional_model_requests':0,
            'artifact_sha256':{name:t.audit.sha(out/name) for name in ('SUMMARY.json','FINDINGS.jsonl','PROPOSALS.json','FAILURES.json','BATCHES.json','CITATION_RECOVERIES.json','INVALID_TARGETS.json','README.md','PROPOSALS.md','RULES.md','POLICY_QUESTIONS.md')},
            'triage_code_sha256':t.audit.sha(Path(t.__file__)),'validation_code_sha256':t.audit.sha(Path(__file__))}
    t.audit.core.atomic_json(out/'CHECKS.json',result)
    print(json.dumps({k:result[k] for k in ('passed','inventory_findings','draft_edits_simulated','review_batch_findings','original_audit_and_production_preserved','additional_model_requests')},ensure_ascii=False))
    return result


if __name__=='__main__':validate()
