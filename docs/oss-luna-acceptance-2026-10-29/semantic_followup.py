"""Checkpoint direct Codex archive judgments. No network, model or apply command."""
from collections import Counter, defaultdict
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import re

import triage_audit as t

ROOT=t.OUT/'semantic-review'


def read_json(path):return json.loads(Path(path).read_text())


def scope():
    batches=read_json(t.OUT/'BATCHES.json')
    ids=[key for b in batches for key in b['finding_ids']]
    assert len(ids)==len(set(ids))==7123
    value={'audit_id':t.audit.AUDIT_ID,'findings':7123,'finding_ids':ids,
           'batches_sha256':t.audit.sha(t.OUT/'BATCHES.json'),'findings_sha256':t.audit.sha(t.OUT/'FINDINGS.jsonl'),
           'new_paid_requests_allowed':False,'production_writes_allowed':False}
    ROOT.mkdir(exist_ok=True)
    path=ROOT/'SCOPE.json'
    if path.exists():assert read_json(path)==value
    else:t.audit.core.atomic_json(path,value)
    return value,batches


def decisions():
    path=ROOT/'DECISIONS.jsonl'
    values=[]
    if path.exists():
        with path.open() as src:values=[json.loads(x) for x in src]
    assert len({v['id'] for v in values})==len(values)
    return values


def records(keys):
    wanted=set(keys)
    found={}
    with (t.OUT/'FINDINGS.jsonl').open() as src:
        for line in src:
            row=json.loads(line)
            if row['id'] in wanted:found[row['id']]=row
    assert set(found)==wanted
    return found


def progress():
    frozen,batches=scope();ds=decisions();done={d['id'] for d in ds}
    assert done<=set(frozen['finding_ids'])
    value={'audit_id':t.audit.AUDIT_ID,'at':t.audit.core.now(),'scope_findings':7123,'reviewed':len(done),'remaining':7123-len(done),
           'dispositions':dict(Counter(d['disposition'] for d in ds)),
           'completed_batches':sum(set(b['finding_ids'])<=done for b in batches),'total_batches':len(batches),
           'next_batch':next((b['id'] for b in batches if not set(b['finding_ids'])<=done),None),
           'status':'review_complete' if len(done)==7123 else 'in_progress','additional_paid_requests':0,
           'human_user_confirmed':0,'production_writes':False}
    t.audit.core.atomic_json(ROOT/'PROGRESS.json',value)
    return value


def show(batch_id,limit=40):
    frozen,batches=scope();done={d['id'] for d in decisions()}
    batch=next(b for b in batches if b['id']==batch_id)
    keys=[k for k in batch['finding_ids'] if k not in done][:limit]
    found=records(keys);result=[]
    for key in keys:
        r=found[key];payload=read_json(r['input_path']);assert t.audit.core.digest(Path(r['input_path']).read_text())==r['input_sha256']
        targets=[]
        for target in r['targets']:
            value=target['value']
            if r['field']=='scenario_match' and isinstance(value,dict):
                value={k:value.get(k) for k in ('scenario_id','scenario_name','scenario_description','reason','applicability','conditions')}
            targets.append({'path':target['path'],'value':value})
        evidence=[]
        for e in r['evidence']:
            evidence.append({'stage':e['stage'],'source_id':e['source_id'],'kind':e.get('kind'),'quote':e['quote'],'original':e['original'],'archive_path':e.get('archive_path'),'source_sha256':e.get('source_sha256')})
        # Headers help interpret TODO/Goals and license context, without treating
        # a model's short quote as the entire source.
        license_finding=r['field']=='license' or r['kind']=='license_overclaim'
        headers=[{'id':s['id'],'kind':s['kind'],'text':s['text'][:700],'truncated':s.get('truncated',False)} for s in payload['sources'] if s['kind']!='github_metadata' and (license_finding or s['kind']!='license')]
        view={'id':key,'repository':r['repository'],'field':r['field'],'kind':r['kind'],'severity':r['severity'],
              'claim':r['claim'],'targets':targets,'primary_reason':r['model_reason'],'secondary_reason':r['secondary_reason'],
              'signals':r['signals'],'source_headers':headers,'evidence':evidence}
        view['card_context']={k:payload['card'].get(k) for k in ('summary','positioning','scope','project_type')}
        view['card_context']['license_status']=(payload['card'].get('license') or {}).get('status')
        view_sha=t.audit.core.digest(t.audit.core.canonical(view))
        view['view_sha256']=view_sha;result.append(view)
        with (ROOT/'READ_LOG.jsonl').open('a') as log:log.write(t.audit.core.canonical({'id':key,'view_sha256':view_sha,'at':t.audit.core.now(),'input_sha256':r['input_sha256']})+'\n')
    return result


def source(rid,sid,term=None,start=1,lines=35):
    scope();path=t.audit.DATA/'inputs'/(str(rid)+'.json');payload=read_json(path)
    with t.readonly(t.audit.SNAPSHOT,True) as snap:
        checker=t.Evidence(snap);originals,gaps=checker.originals(rid,payload);assert not gaps
    raw=originals[sid];text=raw['text'];rows=text.splitlines()
    if term:
        matches=[(ix+1,line) for ix,line in enumerate(rows) if term.casefold() in line.casefold()]
        ranges=[]
        for line,_ in matches[:8]:ranges.append({'start':max(1,line-3),'text':'\n'.join(rows[max(0,line-4):line+5])})
        return {'rid':rid,'source_id':sid,'archive_path':raw['archive_path'],'source_sha256':t.audit.core.digest(text),'matches':ranges,'total_matches':len(matches)}
    return {'rid':rid,'source_id':sid,'archive_path':raw['archive_path'],'source_sha256':t.audit.core.digest(text),'total_lines':len(rows),'start':start,'text':'\n'.join(rows[start-1:start-1+lines])}


def value_at(packet,path):
    node=packet
    for key in path.strip('/').split('/'):node=node[int(key)] if isinstance(node,list) else node[key]
    return node


def commit(path):
    frozen,_=scope();data=read_json(path)
    assert isinstance(data,list) and data
    with (ROOT/'review.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        prior={d['id'] for d in decisions()};keys=[d['id'] for d in data]
        assert len(keys)==len(set(keys)) and not set(keys)&prior and set(keys)<=set(frozen['finding_ids'])
        found=records(keys);seen=defaultdict(set)
        with (ROOT/'READ_LOG.jsonl').open() as src:
            for line in src:
                v=json.loads(line);seen[v['id']].add(v['view_sha256'])
        for d in data:
            r=found[d['id']];assert d['view_sha256'] in seen[d['id']]
            assert d['disposition'] in ('modify','dismissed','unresolved')
            assert isinstance(d.get('reason'),str) and len(d['reason'])>=20
            assert not re.search('未逐条核实|未阅读|自动归为|本批统一',d['reason'])
            packet=read_json(r['input_path']);assert t.audit.core.digest(Path(r['input_path']).read_text())==r['input_sha256']
            assert isinstance(d.get('evidence_refs'),list) and d['evidence_refs']
            source_ids={s['id'] for s in packet['sources']}
            assert all(e.get('source_id') in source_ids for e in d['evidence_refs'])
            changes=d.get('changes',[])
            assert bool(changes)==(d['disposition']=='modify')
            if changes:assert d.get('change_necessity') in ('required','recommended')
            for c in changes:
                assert re.fullmatch(r'/card/(summary|positioning|scope|features/\d+/text|license/note|project_type)|/scenario_matches/\d+/(reason|applicability|conditions)',c['path'])
                assert value_at(packet,c['path'])==c['before'] and c['before']!=c['after']
                c['before_sha256']=t.audit.core.digest(t.audit.core.canonical(c['before']))
            d.update(audit_id=t.audit.AUDIT_ID,reviewed_at=t.audit.core.now(),reviewer='Codex direct archived-source semantic comparison',
                     input_path=r['input_path'],input_sha256=r['input_sha256'],repository_id=r['repository_id'],repository=r['repository'],
                     repository_data_sha256=r['repository_data_sha256'],original_model_disposition=r['model_disposition'],
                     production_applied=False,human_user_confirmed=False,new_paid_requests=0)
        with (ROOT/'DECISIONS.jsonl').open('a') as dest:
            for d in data:dest.write(t.audit.core.canonical(d)+'\n')
    return progress()


def summarize():
    p=progress();ds=decisions();mods=[d for d in ds if d['disposition']=='modify']
    conflicts=defaultdict(list)
    for d in mods:
        for c in d['changes']:conflicts[(d['repository_id'],c['path'])].append({'id':d['id'],'after':c['after']})
    collisions=[{'repository_id':rid,'path':path,'alternatives':v} for (rid,path),v in conflicts.items() if len({t.audit.core.canonical(x['after']) for x in v})>1]
    t.audit.core.atomic_json(ROOT/'MODIFICATIONS.json',{'audit_id':t.audit.AUDIT_ID,'complete':p['remaining']==0,'finding_decisions':mods,'overlapping_field_conflicts':collisions,'production_applied':False})
    lines=['# 归档语义核实进度','',f"已逐项核实 {p['reviewed']:,}/7,123 条，剩余 {p['remaining']:,} 条；不能把未读取的线索算作已核实。",'',str(p['dispositions']),'',
           '结论由Codex直接对照归档，用户人工确认仍为0。修改建议未写入生产；没有新增付费请求。','',
           '逐项结论：DECISIONS.jsonl；具体变更：MODIFICATIONS.json；不同疑点修改同一字段的冲突须在最终清单中合并。','']
    (ROOT/'REPORT.md').write_text('\n'.join(lines))
    return p


def finalize():
    p=summarize()
    assert p['remaining']==0 and p['reviewed']==7123, 'semantic_review_not_complete'
    frozen,batches=scope();ds=decisions()
    assert {d['id'] for d in ds}==set(frozen['finding_ids'])
    baseline=read_json(t.OUT/'SUMMARY.json')
    with t.readonly(t.audit.STATE_DB) as con:
        audit_after=t.protected_state(con)
    assert audit_after==baseline['protected_after'], 'original_audit_or_billing_changed'
    production=t.production_state()
    proposals=read_json(ROOT/'MODIFICATIONS.json')
    initial=read_json(t.OUT/'PROPOSALS.json')
    proposals['initial_drafts']=[x for x in initial if x['changes']]
    proposals['initial_policy_pending']=[x for x in initial if not x['changes']]
    proposals['complete']=True
    t.audit.core.atomic_json(ROOT/'MODIFICATIONS.json',proposals)
    summary={**p,'finished_at':t.audit.core.now(),'audit_and_billing_preserved':True,
             'production_matches_initial_baseline':production==baseline['production_after'],
             'production_current':production,'audit_current':audit_after,
             'required_change_findings':sum(d['disposition']=='modify' and d.get('change_necessity')=='required' for d in ds),
             'recommended_clarification_findings':sum(d['disposition']=='modify' and d.get('change_necessity')=='recommended' for d in ds),
             'initial_draft_changes':sum(len(x['changes']) for x in initial),
             'overlapping_field_conflicts':len(proposals['overlapping_field_conflicts']),
             'scope_sha256':t.audit.sha(ROOT/'SCOPE.json'),'decisions_sha256':t.audit.sha(ROOT/'DECISIONS.jsonl'),
             'modifications_sha256':t.audit.sha(ROOT/'MODIFICATIONS.json'),'no_production_changes':True,'final_report_ready':True}
    lines=['# 7,123条归档语义核实结果','',
           f"全部7,123条均已有逐项归档判断。结论：{p['dispositions']}。用户人工确认仍为0；没有新增Atlas模型请求、没有生产写入。",'',
           f"需修正线索 {summary['required_change_findings']} 条；建议澄清措辞 {summary['recommended_clarification_findings']} 条。另保留首轮11项草案。",'',
           f"不同疑点修改同一字段的候选冲突 {summary['overlapping_field_conflicts']} 处，未擅自合并或覆盖。完整当前值、建议值、冻结hash和来源位置见 [MODIFICATIONS.json](MODIFICATIONS.json)。",'',
           '## 拟修改条目','', '|仓库|疑点|必要性|字段|原文对照理由|','|---|---|---|---|---|']
    for d in ds:
        if d['disposition']=='modify':
            lines.append('|'+d['repository']+'|'+d['id']+'|'+d['change_necessity']+'|'+', '.join(c['path'] for c in d['changes'])+'|'+d['reason'].replace('|','\\|')+'|')
    lines += ['','撤销和未决的逐项理由均保存在DECISIONS.jsonl；未决没有改算通过或真实错误。生产中用户自己的变更须与冻结值重新核对。','']
    (ROOT/'FINAL_REPORT.md').write_text('\n'.join(lines))
    t.audit.core.atomic_json(ROOT/'FINAL_SUMMARY.json',summary)
    return summary


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='cmd',required=True)
    sub.add_parser('progress');sub.add_parser('summarize');sub.add_parser('finalize')
    view=sub.add_parser('show');view.add_argument('batch');view.add_argument('--limit',type=int,default=40)
    src=sub.add_parser('source');src.add_argument('rid',type=int);src.add_argument('sid');src.add_argument('--term');src.add_argument('--start',type=int,default=1);src.add_argument('--lines',type=int,default=35)
    com=sub.add_parser('commit');com.add_argument('path',type=Path)
    args=parser.parse_args()
    if args.cmd=='progress':result=progress()
    elif args.cmd=='summarize':result=summarize()
    elif args.cmd=='finalize':result=finalize()
    elif args.cmd=='show':result=show(args.batch,args.limit)
    elif args.cmd=='source':result=source(args.rid,args.sid,args.term,args.start,args.lines)
    else:result=commit(args.path)
    print(json.dumps(result,ensure_ascii=False,indent=1))
