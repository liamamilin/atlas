"""Offline acceptance evidence. Refuse final output until this audit has ended."""
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import sqlite3

import full_audit as audit
from audit_ledger import charges, CAP


def readonly(path, immutable=False):
    con = sqlite3.connect(path.as_uri()+"?mode=ro"+("&immutable=1" if immutable else ""), uri=True)
    con.row_factory = sqlite3.Row
    return con


def row_hash(con, query):
    h = hashlib.sha256()
    for row in con.execute(query):
        h.update(audit.core.canonical(list(row)).encode()); h.update(b"\n")
    return h.hexdigest()


def validate():
    progress = json.loads((audit.DOC/"PROGRESS.json").read_text())
    model = json.loads((audit.DOC/"FINAL_MODEL_REVIEW.json").read_text())
    manifest = json.loads((audit.DOC/"MANIFEST.json").read_text())
    assert progress["status"] == "completed" and model["scope_complete"]
    assert progress["audit_id"] == model["audit_id"] == manifest["audit_id"] == audit.AUDIT_ID
    assert audit.sha(audit.SNAPSHOT) == manifest["snapshot_sha256"]
    assert all(audit.sha(audit.core.OUT/n) == h for n,h in manifest["implementation_sha256"].items())
    assert audit.core.digest(audit.PRIMARY_PROMPT) == manifest["primary"]["prompt_sha256"]
    assert audit.core.digest(audit.SECONDARY_PROMPT) == manifest["secondary"]["prompt_sha256"]
    c = readonly(audit.STATE_DB); c.execute("BEGIN")
    rows = c.execute("SELECT * FROM projects ORDER BY rid").fetchall()
    assert len(rows) == audit.EXPECTED == 55651
    assert not any(r["primary_status"] in ("pending","inflight") or r["secondary_status"] in ("pending","inflight") for r in rows)
    corpus = hashlib.sha256()
    for r in rows: corpus.update(audit.core.canonical([r["rid"],r["data_sha"]]).encode())
    assert corpus.hexdigest() == manifest["corpus_sha256"]
    primary, secondary, outcomes, domains = Counter(), Counter(), Counter(), Counter()
    primary_citations, secondary_citations = Counter(), Counter()
    issue_kinds, issue_severity, issue_fields, dispositions = Counter(), Counter(), Counter(), Counter()
    disposition_kinds, coverage = defaultdict(Counter), Counter()
    versions, failed_projects, payload_mismatches, citation_mismatches = Counter(), [], [], []
    missing_required_secondary = []
    for r in rows:
        primary[r["primary_status"]] += 1; secondary[r["secondary_status"]] += 1
        outcomes[r["outcome"]] += 1; domains[r["domain"]] += 1
        versions["primary:"+str(r["primary_version"])] += 1
        versions["secondary:"+str(r["secondary_version"])] += 1
        path = audit.DATA/"inputs"/(str(r["rid"])+".json")
        if not path.exists() or audit.core.digest(path.read_text()) != r["payload_sha"]:
            payload_mismatches.append(r["rid"]); continue
        payload = json.loads(path.read_text()); cv = json.loads(r["coverage"] or "{}")
        assert payload["card"]["repository_id"] == r["rid"]
        coverage["metadata_only_projects"] += cv.get("files_included",0) == 0
        coverage["projects_with_truncated_sources"] += cv.get("truncated_files",0) > 0
        coverage["projects_with_omitted_files"] += cv.get("omitted_files",0) > 0
        coverage["truncated_source_files"] += cv.get("truncated_files",0)
        coverage["omitted_source_files"] += cv.get("omitted_files",0)
        coverage["scenario_associations_available"] += cv.get("total_campaign_matches",0)
        coverage["scenario_associations_included"] += cv.get("matches_included",0)
        coverage["shared_repository_multiple_associations"] += cv.get("total_campaign_matches",0) > 1
        p = json.loads(r["primary_review"]) if r["primary_review"] else None
        s = json.loads(r["secondary_review"]) if r["secondary_review"] else None
        if p:
            sources = {v["id"]:v["text"] for v in payload["sources"]}
            for i in p.get("issues",[]):
                state = audit.citation_state(i.get("source_id"),i.get("quote"),sources)
                primary_citations[state] += 1; issue_kinds[i.get("kind","unspecified")] += 1
                issue_severity[i.get("severity","unspecified")] += 1; issue_fields[i.get("field","unspecified")] += 1
                coverage["primary_invalid_scenario_references"] += i.get("citation_state") == "invalid_scenario"
            if r["primary_version"] == audit.VERSION and audit.issue_findings(p) and r["secondary_status"] == "none":
                missing_required_secondary.append(r["rid"])
        if s and r["secondary_version"] == audit.VERSION:
            focused_path = audit.DATA/"secondary-inputs"/(str(r["rid"])+".json")
            focused = json.loads(focused_path.read_text())
            sources = {v["id"]:v["text"] for v in focused["sources"]}
            findings = {v["finding_id"]:v for v in focused["primary_findings"]}
            assert {v["finding_id"] for v in s["adjudications"]} == set(findings)
            for ad in s["adjudications"]:
                state = audit.citation_state(ad.get("source_id"),ad.get("quote"),sources)
                secondary_citations[state] += 1; dispositions[ad["disposition"]] += 1
                disposition_kinds[ad["disposition"]][findings[ad["finding_id"]].get("kind","unspecified")] += 1
                if ad["disposition"] == "confirmed" and state not in ("literal","whitespace_equivalent"):
                    citation_mismatches.append(r["rid"])
                coverage["secondary_confirmations_downgraded_for_citation"] += ad.get("model_disposition") == "confirmed"
        if r["primary_status"] == "failed" or r["secondary_status"] == "failed":
            failed_projects.append({"repository_id":r["rid"],"repository":r["full_name"],"primary_status":r["primary_status"],"secondary_status":r["secondary_status"],"error_code":r["error_code"]})
    assert not payload_mismatches and not citation_mismatches and not missing_required_secondary
    assert len(domains) == 29
    providers = defaultdict(lambda:{"states":Counter(),"returned_models":Counter(),"billed_micro":0,"estimated_micro":0,"reserved_micro":0,"reported_cost_usd":Decimal(0),"token_priced_exact_usd":Decimal(0),"usage_receipts":0,"response_ids":set(),"missing_response_id":0,"legacy_requests":0})
    cost_mismatches = []; receipt_identity_errors = []; receipt_rids = defaultdict(set)
    for r in c.execute("SELECT * FROM requests"):
        v = providers[r["provider"]]; v["states"][r["state"]] += 1
        v["billed_micro"] += r["charged"]; v["estimated_micro"] += r["estimated"]
        v["reserved_micro"] += r["reserved"] if r["state"] in ("uncertain","reserved") else 0
        v["legacy_requests"] += bool(r["legacy_path"])
        receipt = json.loads(r["receipt"] or "{}"); usage = receipt.get("usage") or {}
        if usage:
            actual = receipt.get("returned_model"); v["returned_models"][str(actual)] += 1; v["usage_receipts"] += 1
            expected = "gpt-6-luna" if r["provider"] == "openai" else "deepseek-v4.1-flash"
            if actual != expected: receipt_identity_errors.append(r["id"])
            receipt_rids[r["stage"]].add(r["rid"])
            if receipt.get("response_id"): v["response_ids"].add(receipt["response_id"])
            else: v["missing_response_id"] += 1
            if r["state"] == "settled" and charges(usage,r["provider"]) != (r["estimated"],r["charged"]): cost_mismatches.append(r["id"])
            if type(usage.get("cost")) in (int,float): v["reported_cost_usd"] += Decimal(str(usage["cost"]))
            if r["provider"] == "openai":
                pt,ot = usage["prompt_tokens"],usage["completion_tokens"]
                dt = usage.get("prompt_tokens_details") or {}; cached = dt.get("cached_tokens",0); writes = dt.get("cache_write_tokens",0)
                v["token_priced_exact_usd"] += ((Decimal(pt-cached-writes)*Decimal('.1')+Decimal(cached)*Decimal('.01')+Decimal(writes)*Decimal('.125'))*(2 if pt>272000 else 1)+Decimal(ot)*Decimal('.5')*(Decimal('1.5') if pt>272000 else 1))/1000000
    assert not cost_mismatches and not receipt_identity_errors
    assert all(r["rid"] in receipt_rids["primary"] for r in rows if r["primary_status"] == "done")
    assert all(r["rid"] in receipt_rids["secondary"] for r in rows if r["secondary_status"] == "done")
    for v in providers.values():
        v["distinct_response_ids"] = len(v.pop("response_ids")); v["reported_cost_usd"] = str(v["reported_cost_usd"]); v["token_priced_exact_usd"] = str(v["token_priced_exact_usd"])
    budget = audit.Ledger.balance(c); assert budget["available_micro"] >= 0 and budget["cap_micro"] == CAP
    assert not any(v["states"].get("reserved",0) for v in providers.values())
    failed_receipt_validation = Counter()
    for r in c.execute("SELECT rid,stage,receipt FROM requests WHERE rid IN (SELECT rid FROM projects WHERE primary_status='failed' OR secondary_status='failed') AND error_code='invalid_model_response'"):
        receipt = json.loads(r["receipt"] or "{}")
        path = audit.DATA/("inputs" if r["stage"] == "primary" else "secondary-inputs")/(str(r["rid"])+".json")
        try:
            audit.parse_review(receipt,json.loads(path.read_text()),r["stage"])
        except Exception as error:
            failed_receipt_validation[r["stage"]+":"+type(error).__name__+":"+str(error)[:80]] += 1
        else:
            raise AssertionError("failed review has a recoverable valid paid receipt")
    checks = {}
    with audit.core.readonly() as production:
        for name,q in {"project_keys":"SELECT repository_id,full_name FROM oss_project ORDER BY repository_id","memberships":"SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id","matches":"SELECT * FROM oss_match ORDER BY scenario_id,repository_id","favorites":"SELECT repository_id,favorite FROM oss_project ORDER BY repository_id","jobs":"SELECT * FROM oss_batch_job ORDER BY id"}.items():
            actual = row_hash(production,q); checks[name] = {"sha256":actual,"unchanged":actual == manifest["baseline"][name]}
        frozen = {r["rid"]:r["data_sha"] for r in rows}; changed = []
        for r in production.execute("SELECT repository_id,data FROM oss_project"):
            if r["repository_id"] in frozen and audit.core.digest(r["data"]) != frozen[r["repository_id"]]: changed.append(r["repository_id"])
        checks["frozen_project_data"] = {"changed_repository_ids":changed,"unchanged":not changed}
        original_job = production.execute("SELECT data FROM oss_batch_job WHERE id=?",(audit.core.JOB,)).fetchone()
        checks["original_collection_job"] = {"sha256":audit.core.digest(original_job["data"]),"unchanged":audit.core.digest(original_job["data"]) == manifest["original_job_sha256"]}
    checks["model_settings"] = {"sha256":audit.sha(audit.core.atlas_model.config_path()),"unchanged":audit.sha(audit.core.atlas_model.config_path()) == manifest["settings_sha256"]}
    snapshot_stats = {}
    with readonly(audit.SNAPSHOT,True) as snap:
        for field in ("project_type","completeness","license.status"):
            snapshot_stats[field] = dict(snap.execute("SELECT json_extract(data,?),COUNT(*) FROM oss_project WHERE repository_id IN (SELECT repository_id FROM oss_batch_target WHERE job_id=? AND status IN ('accepted','partial')) GROUP BY 1",("$."+field,audit.core.JOB)))
    issues = audit.DOC/"ISSUES.jsonl"; assert audit.sha(issues) == model["issues_sha256"]
    issue_ids = set(); issue_rows = 0
    with issues.open() as src:
        for line in src:
            v = json.loads(line); assert v["repository_id"] not in issue_ids; issue_ids.add(v["repository_id"]); issue_rows += 1
            assert v.get("human_confirmed") is False
    launched = json.loads((audit.DOC/"LAUNCHED.json").read_text())["at"]
    elapsed = (datetime.fromisoformat(model["finished_at"])-datetime.fromisoformat(launched)).total_seconds()
    spot = json.loads((audit.DOC/"SOURCE_SPOT_REVIEW.json").read_text())
    assert len(spot["domains"]) == 29 and spot["human_user_confirmation_count"] == 0
    result = {"audit_id":audit.AUDIT_ID,"validated_at":audit.core.now(),"finished_at":model["finished_at"],"launched_at":launched,"elapsed_hours":elapsed/3600,
              "frozen_projects":55651,"scope_corpus_verified":True,"model_processing_complete":True,"primary":dict(primary),"secondary":dict(secondary),"outcomes":dict(outcomes),"domains":dict(domains),"versions":dict(versions),
              "primary_issue_kinds":dict(issue_kinds),"primary_issue_fields":dict(issue_fields),"primary_issue_severity":dict(issue_severity),"focused_finding_dispositions":dict(dispositions),"focused_dispositions_by_kind":{k:dict(v) for k,v in disposition_kinds.items()},
              "citations":{"primary":dict(primary_citations),"focused_secondary":dict(secondary_citations),"all_model_confirmed_focused_quotes_locatable":True},"coverage":dict(coverage),"providers":dict(providers),"budget":budget,"failed_projects":failed_projects,
              "unreviewed_pending_primary":0,"unreviewed_pending_secondary":0,"failed_receipt_validation_errors":dict(failed_receipt_validation),"production_baseline":checks,"frozen_catalog_stats":snapshot_stats,"issue_export_rows":issue_rows,"issues_sha256":model["issues_sha256"],
              "human_user_confirmed":0,"source_spot_review":{"path":str(audit.DOC/"SOURCE_SPOT_REVIEW.json"),"reviewer":"Codex","cases":len(spot["records"]),"domains":29,"dispositions":spot["counts"],"non_statistical":True},"provider_invoice_downloaded":False,"catalog_unconditional_acceptance":False,"audit_acceptance_complete":True,"acceptance_status":"completed_with_limits_and_open_findings"}
    result["acceptance_tool_sha256"] = {name:audit.sha(audit.core.OUT/name) for name in ("final_acceptance.py","write_final_report.py","reconcile_costs.py")}
    result["source_spot_review_sha256"] = audit.sha(audit.DOC/"SOURCE_SPOT_REVIEW.json")
    audit.core.atomic_json(audit.DOC/"FINAL_ACCEPTANCE.json",result)
    c.close()
    return result


if __name__ == "__main__":
    v = validate()
    print(json.dumps({k:v[k] for k in ("audit_id","primary","secondary","outcomes","focused_finding_dispositions","coverage","budget","issue_export_rows","elapsed_hours")},ensure_ascii=False,indent=1))
