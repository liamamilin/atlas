"""Offline triage of the completed frozen audit. No model or catalog write API."""
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
import argparse
import hashlib
import json
import re
import sqlite3

import full_audit as audit
from final_acceptance import readonly, row_hash

OUT = audit.DOC / "triage"
VERSION = "atlas.offline.triage.v1"
VALID_QUOTES = {"literal", "whitespace_equivalent"}
GROUP_LABELS = {
    "source_supported_proposal": "已有归档对照支持的建议",
    "source_checked_dismissed": "归档对照撤销",
    "source_checked_unresolved": "归档对照仍未决",
    "model_dismissed_reference": "模型已撤销，保留原意见",
    "review_failure": "审核结果缺口",
    "integrity_gap": "证据完整性缺口",
    "invalid_target_reference": "疑点引用的场景不在冻结关联中",
    "license_scope": "许可声明与适用范围",
    "taxonomy_policy": "类型分类规范待明确",
    "existing_qualifications": "检查已有适用条件/限定",
    "citation_gap": "引用需要补证据",
    "coverage_limit": "资料覆盖不足",
    "roadmap_tense": "计划/要求与现有能力的时态",
    "claim_alignment": "主张与来源逐项对照",
}


def normalize(value):
    return " ".join(value.split()) if isinstance(value, str) else ""


def locate(text, quote):
    if not isinstance(quote, str) or not quote:
        return {"state": "no_quote"}
    if "[ARCHIVE TEXT OMITTED]" in quote:
        return {"state": "non_source_marker"}
    start = text.find(quote)
    end = start + len(quote)
    state = "literal"
    if start < 0:
        if normalize(quote) not in normalize(text):
            return {"state": "not_found"}
        state = "whitespace_equivalent"
        # Escape all source text; whitespace flexibility is the only relaxation.
        match = re.search(r"\s+".join(re.escape(w) for w in quote.split()), text)
        if not match:
            return {"state": state, "offset": None}
        start, end = match.span()
    context = text[max(0,start-180):min(len(text),end+250)]
    return {"state":state,"offset":start,"line":text.count("\n",0,start)+1,
            "quote_chars":len(quote),"context":context[:1100]}


def target_values(payload, finding):
    field = finding.get("field")
    if field == "scenario_match":
        sid = finding.get("scenario_id")
        matches = [(ix,m) for ix,m in enumerate(payload["scenario_matches"]) if m.get("scenario_id") == sid]
        return [{"path":"/scenario_matches/"+str(ix),"value":m} for ix,m in matches]
    value = payload["card"].get(field)
    if field == "features" and isinstance(value,list):
        exact = [(ix,v) for ix,v in enumerate(value) if normalize(v.get("text")) == normalize(finding.get("claim"))]
        selected = exact or list(enumerate(value))
        return [{"path":"/card/features/"+str(ix)+"/text","value":v.get("text"),"claim_exact_match":bool(exact)} for ix,v in selected]
    if field == "license":
        return [{"path":"/card/license","value":{k:(value or {}).get(k) for k in ("status","spdx","detected_spdx","note")}}]
    return [{"path":"/card/"+str(field),"value":value}]


def signals(payload, finding, targets):
    result = []
    field = finding.get("field")
    if field == "scenario_match":
        if not targets:
            result.append("scenario_id_not_in_frozen_project")
        for target in targets:
            match = target["value"]
            if match.get("applicability") in ("conditional","unverified"):
                result.append("scenario_already_"+match["applicability"])
            if match.get("conditions"):
                result.append("scenario_has_explicit_conditions")
            if re.search("未说明|未明确|需核实|待核|不支持|不具备|部分|但|仅",match.get("reason", "")):
                result.append("scenario_reason_has_qualification")
    if (payload.get("coverage") or {}).get("files_included",0) == 0:
        result.append("metadata_only")
    if (payload.get("coverage") or {}).get("truncated_files",0):
        result.append("source_packet_truncated")
    if finding.get("kind") == "wrong_type" or field == "project_type":
        result.append("type_policy_required_before_relabel")
    if finding.get("kind") == "insufficient_evidence":
        result.append("absence_of_evidence_does_not_prove_absence")
    if field == "license" or finding.get("kind") == "license_overclaim":
        result.append("license_scope_requires_distinct_judgment")
    return sorted(set(result))


def group_for(record):
    # Rules route work; they never promote a model judgment into human approval.
    if record.get("integrity_gaps"):
        return "integrity_gap"
    if "scenario_id_not_in_frozen_project" in record["signals"]:
        return "invalid_target_reference"
    spot = record.get("source_check")
    if spot:
        return {"corroborated":"source_supported_proposal","dismissed":"source_checked_dismissed","unresolved":"source_checked_unresolved"}[spot["disposition"]]
    if record["model_disposition"] == "dismissed":
        return "model_dismissed_reference"
    if record["model_disposition"] == "missing_secondary_result":
        return "review_failure"
    flags = record["signals"]
    if "license_scope_requires_distinct_judgment" in flags:
        return "license_scope"
    if "type_policy_required_before_relabel" in flags:
        return "taxonomy_policy"
    if any(v.startswith("scenario_already_") or v == "scenario_reason_has_qualification" for v in flags):
        return "existing_qualifications"
    if not any(e["original"].get("state") in VALID_QUOTES for e in record["evidence"]):
        return "citation_gap"
    if "metadata_only" in flags or record["kind"] == "insufficient_evidence":
        return "coverage_limit"
    if record["kind"] == "roadmap_as_fact":
        return "roadmap_tense"
    return "claim_alignment"


class Evidence:
    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.counts = Counter()
        self.verified_archives = set()
        self.unreadable_files = []

    @lru_cache(maxsize=256)
    def archive(self, relative, expected_sha):
        path = (audit.core.ARCHIVE/relative).resolve()
        assert audit.core.ARCHIVE.resolve() in path.parents
        assert audit.sha(path) == expected_sha, "archive_hash_changed:"+relative
        self.counts["archives_verified"] += 1
        self.verified_archives.add((relative,expected_sha))
        value = json.loads(path.read_text())
        files = [(k,value.get(k)) for k in ("readme","license")]
        files += [("documentation",v.get("file")) for v in value.get("documents",[])]
        files += [("evidence",value.get("file"))]
        texts = {}
        for kind,file in files:
            if not file:
                continue
            try:
                text = audit.core.decode_file(file)
            except Exception as error:
                self.counts["unreadable_archive_files"] += 1
                self.unreadable_files.append({"archive_path":str(path),"kind":kind,"error_type":type(error).__name__,"included_in_reviewed_packet":False})
                continue
            texts[audit.core.digest(text)] = {"text":text,"archive_path":str(path),"archive_sha256":expected_sha,"kind":kind}
        return texts

    def originals(self, rid, payload):
        prov_path = audit.DATA/"provenance"/(str(rid)+".json")
        prov = json.loads(prov_path.read_text())
        texts = {}
        for entry in prov["archives"]:
            texts.update(self.archive(entry["path"],entry["archive_sha256"]))
        originals, gaps = {}, []
        metas = None
        for source in payload["sources"]:
            if source["kind"] == "github_metadata":
                if metas is None:
                    metas = [json.loads(r["data"])["meta"] for r in self.snapshot.execute("SELECT data FROM oss_candidate WHERE repository_id=?",(rid,))]
                match = next((m for m in metas if audit.core.digest(audit.core.canonical(m)) == source["sha256"]),None)
                if match is not None:
                    public = {k:match.get(k) for k in ("id","full_name","description","topics","language","license","archived","html_url")}
                    text = audit.core.canonical(public)+"\n"+(match.get("description") or "")
                    assert text == source["text"], "metadata_packet_changed"
                    originals[source["id"]] = {"text":text,"archive_path":str(audit.SNAPSHOT),"archive_sha256":None,"kind":"github_metadata"}
                    self.counts["metadata_sources_verified"] += 1
                else:
                    gaps.append("metadata_hash_not_found:"+source["id"])
            elif source["sha256"] in texts:
                originals[source["id"]] = texts[source["sha256"]]
                self.counts["text_sources_verified"] += 1
            else:
                gaps.append("original_text_not_found:"+source["id"])
        return originals,gaps

    def check(self, finding, stage, payload, originals, focused=None):
        sid,quote = finding.get("source_id"),finding.get("quote")
        source = next((v for v in payload["sources"] if v["id"] == sid),None)
        packet = focused if stage == "secondary" and focused else payload
        ps = next((v for v in packet["sources"] if v["id"] == sid),None)
        if not source:
            state = "no_quote" if not sid and not quote else "invalid_reference"
            return {"stage":stage,"source_id":sid,"quote":quote or "","packet":{"state":state},"original":{"state":state}}
        raw = originals.get(sid)
        original = locate(raw["text"],quote) if raw else {"state":"original_unavailable"}
        return {"stage":stage,"source_id":sid,"kind":source["kind"],"source_sha256":source["sha256"],"immutable_url":source.get("immutable_url"),"quote":quote or "",
                "packet":locate(ps["text"],quote) if ps else {"state":"invalid_reference"},"original":original,
                "archive_path":raw["archive_path"] if raw else None,"archive_sha256":raw["archive_sha256"] if raw else None,
                "source_is_full_text":bool(raw and source["kind"] != "github_metadata"),"packet_truncated":source.get("truncated",False)}


def protected_state(con):
    return {"projects_sha256":row_hash(con,"SELECT * FROM projects ORDER BY rid"),
            "requests_sha256":row_hash(con,"SELECT * FROM requests ORDER BY id"),
            "request_count":con.execute("SELECT COUNT(*) FROM requests").fetchone()[0],
            "budget":audit.Ledger.balance(con),
            "artifacts":{name:audit.sha(audit.DOC/name) for name in ("MANIFEST.json","PROGRESS.json","FINAL_ACCEPTANCE.json","ISSUES.jsonl","SOURCE_SPOT_REVIEW.json")},
            "model_config_sha256":audit.sha(audit.core.atlas_model.config_path())}


def production_state():
    with audit.core.readonly() as con:
        return {name:row_hash(con,query) for name,query in {
            "project_keys":"SELECT repository_id,full_name FROM oss_project ORDER BY repository_id",
            "memberships":"SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id",
            "matches":"SELECT * FROM oss_match ORDER BY scenario_id,repository_id",
            "favorites":"SELECT repository_id,favorite FROM oss_project ORDER BY repository_id",
            "jobs":"SELECT * FROM oss_batch_job ORDER BY id",
            "card_data":"SELECT repository_id,data FROM oss_project ORDER BY repository_id"}.items()}


def failure_records(con, projects):
    result = []
    requests = defaultdict(list)
    for r in con.execute("SELECT rid,stage,id,receipt,error_code,state,charged,reserved FROM requests WHERE rid IN (SELECT rid FROM projects WHERE primary_status='failed' OR secondary_status='failed')"):
        requests[(r["rid"],r["stage"])].append(r)
    for row in projects:
        for stage in ("primary","secondary"):
            if row[stage+"_status"] != "failed":
                continue
            payload_path = audit.DATA/("inputs" if stage == "primary" else "secondary-inputs")/(str(row["rid"])+".json")
            payload = json.loads(payload_path.read_text())
            expected = [x["finding_id"] for x in payload.get("primary_findings",[])]
            attempts = []
            for r in requests[(row["rid"],stage)]:
                receipt = json.loads(r["receipt"] or "{}")
                entry = {k:r[k] for k in ("id","error_code","state","charged","reserved")}
                entry["finish_reason"] = receipt.get("finish_reason")
                text = (receipt.get("text") or "").strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
                try:
                    parsed = json.loads(text)
                    ads = parsed.get("adjudications",[]) if isinstance(parsed,dict) else []
                    received = [x.get("finding_id") for x in ads if isinstance(x,dict)]
                    entry.update(returned_repository_id=parsed.get("repository_id") if isinstance(parsed,dict) else None,
                                 expected_finding_ids=expected,received_finding_ids=received,
                                 missing_finding_ids=sorted(set(expected)-set(received)),
                                 duplicate_finding_ids=[k for k,v in Counter(received).items() if v>1],
                                 extra_finding_ids=sorted(set(received)-set(expected),key=str))
                except Exception:
                    entry["json_parseable"] = False
                attempts.append(entry)
            result.append({"repository_id":row["rid"],"repository":row["full_name"],"stage":stage,"domain":row["domain"],
                           "status":"unresolved_review_failure","attempts":attempts,"paid_receipts_preserved":True,
                           "additional_paid_requests":0,"next_action":"核对已有回执与证据；缺少或重复的疑点ID不得按顺序猜配，也不伪装成有效复核。"})
    return result


def proposal(record, payload):
    rid = record["repository_id"]
    # Only the twelve individually checked findings are eligible for this list.
    specs = {
        1127048:("/card/features/0/text","README 的界面设计目标：不设“新建/保存”按钮，支持点击任意处编辑及方向键导航。"),
        131455697:("/card/features/0/text","README 中的作业要求：顾客下单后检查库存，库存不足时拒绝订单，否则更新库存。"),
        54466417:("/card/features/0/text","README 建模题要求：按经纬度与勾股定理计算最近可用出租车。"),
        125183707:("/card/features/0/text","抓取昨日及可选的前一日用电与发电数据；README 将周/月/季节数据列为尚未完成的扩展。"),
    }
    license_notes = {
        569823356:"README 声明 MIT-0，归档 LICENSE 为 Apache-2.0；两份文件的适用范围需进一步核实。",
        127054182:"归档 license.txt 的版权行指向 CodePen 表单设计；该文本对仓库其他内容的授权适用范围尚未核清。",
        125462659:"README 声明模块为 CC BY 4.0，归档 LICENSE 为 GPL v3；两份文件的适用范围需进一步核实。",
        99834648:"README 同时出现 MIT 与 CC BY-SA 4.0 声明，归档 LICENSE 为 MIT；各声明的适用范围尚需核实。",
    }
    summary_replacements = {
        8854010:("采用 Apache 2.0 许可","README 声明采用 Apache 2.0，独立许可证全文核验仍待完成"),
        3955881:("采用 AGPL 3 许可","归档文档声明采用 AGPL 3，独立许可证全文核验仍待完成"),
        35279603:("采用 GPL 许可证","README 声明按 GPL v3 或更高版本发布，独立许可证全文核验仍待完成"),
    }
    item = {"id":record["id"],"repository_id":rid,"repository":record["repository"],"reason":record["source_check"]["reason"],
            "source_check":record["source_check"],
            "evidence":record["evidence"],"input_path":record["input_path"],"input_sha256":record["input_sha256"],
            "repository_data_sha256":record["repository_data_sha256"],"status":"draft_for_review","approved":False,"auto_apply":False,
            "human_user_confirmed":False,"changes":[],"blockers":[]}
    if rid == 2056773:
        item["blockers"] = ["来源表明是命令行图像工具；先明确CLI工具在现有粗分类中的规则，再决定library是否改为application。"]
        item["proposed_direction"] = "明确为stdin/stdout命令行工具，类型标签暂不改。"
        return item
    if rid in specs:
        path,after = specs[rid]
        index = int(path.split('/')[3]); before = payload["card"]["features"][index]["text"]
        assert normalize(before) == normalize(record["claim"])
    elif rid in summary_replacements:
        path = "/card/summary";before = payload["card"]["summary"];old,new = summary_replacements[rid]
        assert before.count(old) == 1
        after = before.replace(old,new)
    elif rid in license_notes:
        path = "/card/license/note";before = payload["card"]["license"].get("note","")
        after = before.rstrip("。")+"。"+license_notes[rid]
        item["blockers"] = ["仅增加来源声明/适用范围说明；授权状态、SPDX及全文匹配结论另行判断。"]
    else:
        raise AssertionError("unexpected individually supported finding")
    item["changes"] = [{"path":path,"before":before,"after":after,"precondition_value_sha256":audit.core.digest(audit.core.canonical(before))}]
    item["patch_on_frozen_packet"] = [{"op":"test","path":path,"value":before},{"op":"replace","path":path,"value":after}]
    return item


def run(out=OUT):
    out.mkdir(parents=True,exist_ok=True)
    acceptance = json.loads((audit.DOC/"FINAL_ACCEPTANCE.json").read_text())
    manifest = json.loads((audit.DOC/"MANIFEST.json").read_text())
    assert acceptance["audit_acceptance_complete"] and manifest["projects"] == 55651
    assert audit.sha(audit.SNAPSHOT) == manifest["snapshot_sha256"]
    assert audit.sha(audit.DOC/"ISSUES.jsonl") == acceptance["issues_sha256"]
    assert audit.sha(audit.DOC/"SOURCE_SPOT_REVIEW.json") == acceptance["source_spot_review_sha256"]
    spot = json.loads((audit.DOC/"SOURCE_SPOT_REVIEW.json").read_text())
    checked = {(x["repository_id"],x["finding_id"]):x for x in spot["records"]}
    con = readonly(audit.STATE_DB); snap = readonly(audit.SNAPSHOT,True)
    before = protected_state(con); prod_before = production_state()
    rows = con.execute("SELECT * FROM projects ORDER BY rid").fetchall()
    assert len(rows) == 55651
    paid_payloads = defaultdict(set)
    for r in con.execute("SELECT rid,payload_sha FROM requests WHERE stage='secondary' AND legacy_path IS NULL"):
        paid_payloads[r["rid"]].add(r["payload_sha"])
    evidence = Evidence(snap); records = []; proposals = []; processed = set(); integrity_gaps = []
    temp = out/"FINDINGS.tmp"
    with temp.open("w") as dest:
        for row in rows:
            primary = json.loads(row["primary_review"] or "{}"); secondary = json.loads(row["secondary_review"] or "{}")
            findings = audit.issue_findings(primary)
            focused = None
            if row["secondary_version"] == audit.VERSION or row["secondary_status"] == "failed":
                path = audit.DATA/"secondary-inputs"/(str(row["rid"])+".json")
                focused = json.loads(path.read_text())
                assert audit.core.digest(audit.core.canonical(focused)) in paid_payloads[row["rid"]], "focused_packet_not_in_receipts"
                findings = focused["primary_findings"]
            legacy = secondary.get("issues",[]) if row["secondary_version"] == "legacy-independent-v1" else []
            if not findings and not legacy:
                continue
            rid = row["rid"];processed.add(rid);path = audit.DATA/"inputs"/(str(rid)+".json")
            assert audit.core.digest(path.read_text()) == row["payload_sha"]
            payload = json.loads(path.read_text()); originals,gaps = evidence.originals(rid,payload)
            integrity_gaps.extend({"repository_id":rid,"gap":g} for g in gaps)
            ads = {x["finding_id"]:x for x in secondary.get("adjudications",[])}
            pairs = [(f,ads.get(f["finding_id"]),"primary") for f in findings]
            pairs += [({"finding_id":"legacy-secondary-"+str(ix),**f},None,"legacy_secondary") for ix,f in enumerate(legacy)]
            for finding,ad,origin in pairs:
                fid = finding["finding_id"];source_checked = checked.get((rid,fid)); targets = target_values(payload,finding)
                disposition = ad["disposition"] if ad else "independent_opinion" if origin == "legacy_secondary" else "missing_secondary_result"
                ev = [evidence.check(finding,"primary" if origin == "primary" else "legacy_secondary",payload,originals)]
                if ad:ev.append(evidence.check(ad,"secondary",payload,originals,focused))
                record = {"id":str(rid)+":"+fid,"repository_id":rid,"repository":row["full_name"],"repository_url":"https://github.com/"+row["full_name"],"domain":row["domain"],
                          "finding_id":fid,"origin":origin,"project_outcome":row["outcome"],"model_disposition":disposition,"severity":finding.get("severity","minor"),
                          "kind":finding.get("kind","insufficient_evidence"),"field":finding.get("field","overall"),"claim":finding.get("claim",""),
                          "model_reason":finding.get("reason",""),"secondary_reason":(ad or {}).get("reason",""),"model_suggested_correction":(ad or finding).get("suggested_correction",""),
                          "targets":targets,"signals":signals(payload,finding,targets),"evidence":ev,"integrity_gaps":gaps,
                          "input_path":str(path),"input_sha256":row["payload_sha"],"repository_data_sha256":row["data_sha"],"source_check":None,
                          "human_user_confirmed":False,"automatic_semantic_approval":False,"automatic_production_write":False}
                if source_checked:
                    record["source_check"] = {"disposition":source_checked["source_review_disposition"],"reason":source_checked["reason"],"reviewer":"Codex direct archive comparison","record_path":str(audit.DOC/"SOURCE_SPOT_REVIEW.json"),"original_archive_checks":source_checked["original_archive_checks"]}
                record["group"] = group_for(record)
                record["priority"] = 0 if record["group"] in ("integrity_gap","review_failure") else 1 if record["group"] == "license_scope" or record["severity"] == "major" else 2
                if record["group"] == "source_supported_proposal":proposals.append(proposal(record,payload))
                records.append(record);dest.write(audit.core.canonical(record)+"\n")
    temp.replace(out/"FINDINGS.jsonl")
    assert len({r["id"] for r in records}) == len(records)
    assert len(proposals) == 12
    failures = failure_records(con,rows)
    assert Counter(r["stage"] for r in failures) == {"primary":1,"secondary":59}
    # Batches combine the same task, while retaining a check and evidence for every row.
    recoveries = [{"id":r["id"],"repository":r["repository"],"stage":e["stage"],"model_disposition":r["model_disposition"],"source_id":e["source_id"],"packet_state":e["packet"]["state"],
                   "original_state":e["original"]["state"],"original_line":e["original"].get("line"),"archive_path":e.get("archive_path"),"source_sha256":e.get("source_sha256"),"semantic_judgment_changed":False}
                  for r in records for e in r["evidence"] if e["packet"]["state"] not in VALID_QUOTES and e["original"]["state"] in VALID_QUOTES]
    invalid_targets = [{k:r[k] for k in ("id","repository_id","repository","claim","model_reason","signals","input_path")} for r in records if r["group"] == "invalid_target_reference"]
    groups = defaultdict(list)
    for r in records:
        if r["group"] not in ("source_checked_dismissed","model_dismissed_reference","source_supported_proposal","invalid_target_reference"):
            groups[(r["priority"],r["group"],r["kind"])].append(r)
    batches = []
    for (priority,group,kind),rs in sorted(groups.items()):
        for start in range(0,len(rs),40):
            subset = rs[start:start+40]
            batches.append({"id":"batch-"+str(len(batches)+1).zfill(4),"priority":priority,"group":group,"label":GROUP_LABELS[group],"kind":kind,
                            "findings":len(subset),"projects":len({r["repository_id"] for r in subset}),"finding_ids":[r["id"] for r in subset],
                            "status":"awaiting_type_policy" if group == "taxonomy_policy" else "ready_for_evidence_review",
                            "path":"batches/batch-"+str(len(batches)+1).zfill(4)+".md","automatic_approval":False})
    after = protected_state(con); prod_after = production_state()
    assert before == after, "audit_inputs_or_ledger_changed"
    assert prod_before == prod_after, "production_changed_during_triage"
    summary = {"audit_id":audit.AUDIT_ID,"version":VERSION,"at":audit.core.now(),"frozen_projects":55651,"finding_projects":len(processed),"findings":len(records),
               "project_outcomes":dict(Counter(r["outcome"] for r in rows)),"model_dispositions":dict(Counter(r["model_disposition"] for r in records)),
               "groups":{g:{"findings":sum(r["group"]==g for r in records),"projects":len({r["repository_id"] for r in records if r["group"]==g}),"label":GROUP_LABELS[g]} for g in sorted({r["group"] for r in records})},
               "signals":dict(Counter(s for r in records for s in r["signals"])),"evidence_checks":{**dict(evidence.counts),"unique_archives_verified":len(evidence.verified_archives)},
               "unreadable_nonpacket_files":evidence.unreadable_files,"original_quote_recoveries":len(recoveries),"invalid_target_references":len(invalid_targets),
               "citation_states":{stage:dict(Counter(e["original"]["state"] for r in records for e in r["evidence"] if e["stage"]==stage)) for stage in ("primary","secondary","legacy_secondary")},
               "integrity_gaps":integrity_gaps,"source_checked_findings":len(checked),"proposal_records":len(proposals),"proposal_changes":sum(bool(r["changes"]) for r in proposals),
               "review_batches":len(batches),"review_batch_findings":sum(b["findings"] for b in batches),"review_batch_projects":len({r["repository_id"] for rs in groups.values() for r in rs}),
               "review_failures":dict(Counter(r["stage"] for r in failures)),"additional_paid_requests":0,"additional_cost_usd":0,
               "human_user_confirmed":0,"production_writes":False,"audit_db_writes":False,
               "protected_before":before,"protected_after":after,"production_before":prod_before,"production_after":prod_after,
               "code_sha256":audit.sha(Path(__file__)),"limits":["Grouping and exact quote matches are deterministic checks, not semantic approval.","Existing model dismissals remain model judgments; only exact source-reviewed IDs reuse the 37 recorded decisions.","Each proposed production change requires its own frozen-value/data-hash precondition; this tool has no apply command."]}
    for name,value in (("SUMMARY.json",summary),("PROPOSALS.json",proposals),("FAILURES.json",failures),("BATCHES.json",batches),("CITATION_RECOVERIES.json",recoveries),("INVALID_TARGETS.json",invalid_targets)):
        audit.core.atomic_json(out/name,value)
    write_docs(out,summary,proposals,batches)
    write_batches(out,records,batches)
    con.close();snap.close()
    return summary


def write_docs(out,s,proposals,batches):
    lines = ["# 离线批量分诊", "", f"审核 `{s['audit_id']}`，仍为原55,651个冻结项目。完成 {s['finding_projects']:,} 个有关项目、{s['findings']:,} 条线索的逐项机检。新增付费请求0、生产写入0，原审核回执、账本、卡片、关系、收藏、任务和模型配置均未变化。", "",
             "本次机检验证输入包、对应付费复核包、原始归档hash、引用位置和实际卡片字段；按已有条件、类型、许可、时态和覆盖限制分组。关键词仅用于分流，不据此批量判错或撤销。", "",
             "|分组|线索数|涉及项目数（组间可重叠）|", "|---|---:|---:|"]
    for group,v in s["groups"].items():lines.append(f"|{v['label']}|{v['findings']:,}|{v['projects']:,}|")
    lines += ["", f"已有37条Codex归档判断按精确项目/疑点ID复用，未外推给同组其他项目。12条来源支持线索形成 **{s['proposal_changes']} 项具体字段改动草案 + 1项类型规则待定建议**，见 [PROPOSALS.md](PROPOSALS.md)。授权状态与SPDX标签均未改写。", "",
              f"其余需看证据的项目已编排为 {s['review_batches']} 批、每批最多40条线索，涉及 {s['review_batch_projects']:,} 个项目、{s['review_batch_findings']:,} 条线索。此数不是已确认错误数，也不表示这些项目全部必须修改。按批审阅可以共同校准规则，但每项仍保留自己的证据。", "",
              f"另外，{s['invalid_target_references']} 条线索引用的场景ID不在该项目冻结关联中，单列 [INVALID_TARGETS.json](INVALID_TARGETS.json)，不据此修改其他场景。{s['original_quote_recoveries']} 处引文在审核片段中未定位、但已在原归档定位，见 [CITATION_RECOVERIES.json](CITATION_RECOVERIES.json)；只补证据定位，不自动恢复模型确认。", "",
              f"发现 {len(s['unreadable_nonpacket_files'])} 个不可解码的非审核包文件，详情单列于SUMMARY；审核包实际使用的来源均已找到并核验原文，无完整性缺口。", "",
              "1条主审失败、59条独立复核失败另见 [FAILURES.json](FAILURES.json)。只列原回执的身份和疑点ID差异，未猜配ID、未重新收费。", "",
              "完整机检：[FINDINGS.jsonl](FINDINGS.jsonl)；分批清单：[BATCHES.json](BATCHES.json)；校验和金额保护：[SUMMARY.json](SUMMARY.json)。用户人工确认数仍为0，原模型意见和失败记录完整保留。", "", "## 首批审阅顺序", ""]
    for b in batches[:10]:lines.append(f"- [{b['id']}]({b['path']})：P{b['priority']}，{b['label']} / {b['kind']}，{b['findings']}条、{b['projects']}个项目。")
    (out/"README.md").write_text("\n".join(lines)+"\n")
    lines = ["# 首批修改建议", "", "以下均为草案，尚未写入生产。每项保留当前值、建议值、输入hash、项目数据hash和证据。只复用已逐项对照的12条线索，不按模型同意数量批准变更。", ""]
    for p in proposals:
        lines += ["## "+p["repository"],"",p["reason"],"",f"疑点：`{p['id']}`；[冻结证据包]({p['input_path']})。"]
        for source in p['source_check'].get('original_archive_checks',[]):
            lines += ['', '已对照来源：'+source['source_id']+' / '+source['kind']+'，[原始归档]('+source['archive_path']+')，文本hash `'+source['text_sha256']+'`。']
        for change in p["changes"]:lines += ["", "字段：`"+change["path"]+"`", "", "当前："+str(change["before"]),"", "建议："+str(change["after"])]
        for blocker in p["blockers"]:lines += ["", "待判断："+blocker]
        lines += ["", "执行条件：当前生产数据与冻结数据摘要、目标字段值完全一致；本清单没有自动执行入口。", ""]
    (out/"PROPOSALS.md").write_text("\n".join(lines))
    (out/"RULES.md").write_text("""# 机检规则与边界

- 原始审核和生产库均以 SQLite mode=ro 打开；只输出本目录文件。
- 每条线索验证冻结输入hash；聚焦复核包的canonical hash必须对应原付费请求。
- 原始归档文件hash与provenance一致；文本hash与来源一致；元数据单独对照冻结snapshot。
- 引用仅允许逐字或空白归一匹配，不忽略大小写、标点、内容；截断标记不算官方证据。
- 条件已存在、缺README、类型粗分类、计划词等仅作为审阅信号；不自动撤销或确认语义判断。
- 仅精确匹配原37条归档审阅的项目ID与finding_id，才复用原Codex决定；用户人工确认仍为0。
- 许可建议只增补归因/文件范围说明，不改变status、spdx、验证方法或授权结论。
- 11项文本草案及1项类型规范建议均未批准；写回前须再次逐项核对当前值和数据hash。
- 回执中缺失、重复、错误的疑点ID不按顺序猜配，失败保持失败；本轮不发起任何模型请求。
""")


def short_quote(text):
    words=text.split()
    return ' '.join(words[:24]) if len(words)>24 else text[:160]


def write_batches(out,records,batches):
    by_id={r['id']:r for r in records};(out/'batches').mkdir(exist_ok=True)
    for batch in batches:
        lines=['# '+batch['id']+' · '+batch['label'],'',
               '本批共'+str(batch['findings'])+'条；仅供逐项证据审阅，未自动确认。类型类先统一规则再判断个案。','']
        for key in batch['finding_ids']:
            r=by_id[key];lines += ['## '+r['repository']+' · '+r['finding_id'],'',
                '模型意见：'+r['model_disposition']+'；级别：'+r['severity']+'；[冻结包]('+r['input_path']+')。','',
                '待核主张：'+r['claim'],'','主审理由：'+r['model_reason'][:500],'',
                '复核理由：'+r['secondary_reason'][:500],'','当前字段：']
            for target in r['targets']:
                value=target['value']
                if r['field']=='scenario_match' and isinstance(value,dict):
                    value={k:value.get(k) for k in ('scenario_id','scenario_name','scenario_description','reason','applicability','conditions')}
                lines += ['', '`'+target['path']+'`：'+json.dumps(value,ensure_ascii=False)]
            if not r['targets']:lines += ['','未找到对应冻结字段/关联。']
            lines += ['','机检信号：'+', '.join(r['signals'])]
            for e in r['evidence']:
                original=e['original'];path=e.get('archive_path');link='[归档]('+path+')' if path else '无对应归档'
                lines += ['',e['stage']+' 引文：'+short_quote(e['quote']),'',
                          '定位：'+original['state']+'；'+link+'；解码原文行 '+str(original.get('line','未知'))+'。']
            lines += ['','审阅结论：待判断。逐项记录支持/撤销/未决及理由；引用存在本身不证明主张成立。','']
        (out/batch['path']).write_text('\n'.join(lines))
    (out/'POLICY_QUESTIONS.md').write_text('''# 优先统一的分类规则

本轮534条线索进入类型分类组（项目可与其他组重叠）。当前冻结数据使用application、library、resource、collection、unknown五种标签。

先以已有案例明确下列边界，再按每条实际来源检查，避免逐张重复讨论同一个定义：

- Moodle/WordPress/Gradle等宿主插件属于应用型组件还是library？不能仅因需宿主就否定其业务能力。
- stdin/stdout命令行工具如何归类？bovine/defish的现有library标签暂不自动改。
- MCP服务器、Rails engine等代码包与可执行服务如何区分？部署依赖与类型分别记录。
- 共享仓库含多个组件时，collection与application如何选择？仍需读取项目定位，不能仅按仓库名含plugins批量改。

建议先把类型规则写成可复用定义，并用37条已有归档对照中的边界案例检验。关键词命中只能分组，不能自动赋新类型；本轮未改变任何类型标签。
''')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",type=Path,default=OUT)
    summary = run(parser.parse_args().out)
    print(json.dumps({k:summary[k] for k in ("audit_id","finding_projects","findings","groups","proposal_records","proposal_changes","review_batches","review_batch_projects","integrity_gaps","additional_paid_requests")},ensure_ascii=False,indent=1))
