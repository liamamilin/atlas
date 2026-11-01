"""Repair only the four audited preparation errors in the existing campaign.

No new batch, service restart, manifest expansion, or per-leaf limit change.
Existing targets are never replayed; portfolio facts and old relations stay.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sqlite3
import sys
from urllib.parse import urlencode

BASE = Path(__file__).resolve().parent
CAMPAIGN = BASE.parent
PACK = CAMPAIGN.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from atlas_runtime import atomic_json
from oss_batch import BatchJobs
from oss_catalog import CatalogError, CatalogStore, GitHub, canonical, digest, now, repository_metadata
from oss_discovery import Model, PLAN_PROMPT, ROOT, validate_plan
from oss_priority import select_first_round
from oss_workflow import context_for, extract_groups, relaxed_card

JOB = "batch_4812ef3db57543c3acc1871b8ea5ba6e"
ERRORS = {
    "log-management": "GitHub 资源超过采集大小限制",
    "distributed-control-system-dcs": "场景搜索必须使用通用任务关键词，不能指定仓库或作者",
    "it-operations-management-itom": "模型返回的 场景名称 长度或类型无效",
    "portfolio-management-system": "模型未返回有效 JSON；本次结果未入库",
}
PLANS = {
    "distributed-control-system-dcs": "d14a1f63900518dfa59dcc3f417324ee2dfbaf5fbb40f2db2df081b1a68fe93a",
    "it-operations-management-itom": "558129bc63596285a88434e86598858d69bb410f85a9a95f1284c7e9db424fbf",
}
MATCH_PROMPT = """只依据输入官方归档资料，为现有项目补充输入场景的关联，不改写项目事实或许可证。
每个项目都返回 repository_id 和 matches；明显不适用的项目返回空 matches，不凑关联。
区分 direct/conditional/unverified，条件适用写真实前提。资源、教程、库或仅供仿真的项目不能描述成可直接运行的完整业务系统。
每条关联给 source_id、理由、applicability、conditions；可给逐字 quote，不得编造引文。
JSON: {"items":[{"repository_id":123,"matches":[{"scenario_id":"输入ID","reason":"中文理由",
"applicability":"unverified","conditions":[],"source_id":"readme","quote":"可选逐字原文"}]}]}"""


class PreservingStore(CatalogStore):
    def record_candidates(self, leaf, metadata, version, discovery=None):
        """Add new search hits, retaining the frozen metadata and prior statuses."""
        assert leaf in ERRORS
        with self.connect() as con:
            for position, value in enumerate(metadata, 1):
                meta = repository_metadata(value)
                row = con.execute("SELECT status,reason,data FROM oss_candidate WHERE leaf=? AND repository_id=?", (leaf, meta["id"])).fetchone()
                data = json.loads(row["data"]) if row else {
                    "meta": meta, "version": version, "discovered_at": now(), "source_changed": False}
                data["last_seen_at"] = now()
                if discovery is not None:
                    hit = {**discovery, "position": (discovery.get("page", 1) - 1) * 100 + position,
                           "searched_at": now(), "search_metadata_sha256": digest(canonical(meta))}
                    hits = [h for h in data.get("search_hits", []) if (h.get("query"), h.get("page")) != (hit.get("query"), hit.get("page"))]
                    data.update(search_hits=(hits + [hit])[-40:], search_verified_at=hit["searched_at"])
                con.execute("INSERT INTO oss_candidate VALUES (?,?,?,?,?) ON CONFLICT(leaf,repository_id) DO UPDATE SET data=excluded.data", (
                    leaf, meta["id"], row["status"] if row else "pending", row["reason"] if row else "修复搜索补入，保留待补", canonical(data)))

    def _upsert(self, con, card, leaf):
        # Shared repositories retain every previously reviewed global fact.
        old = con.execute("SELECT data FROM oss_project WHERE repository_id=?", (card["repository_id"],)).fetchone()
        if old:
            card = {**json.loads(old[0]), "matches": card["matches"]}
        return super()._upsert(con, card, leaf)


def search(store, leaf, scenarios, run, queries):
    github = GitHub()
    evidence = []
    for query in dict.fromkeys(queries):
        # The same validator guards all model-produced queries before here.
        response = github.get("/search/repositories?" + urlencode({
            "q": query + " in:name,description,topics archived:false fork:false", "per_page": 100, "page": 1}))
        items = [repository_metadata(m) for m in response.get("items", []) if not m.get("private") and not m.get("disabled")]
        scenario_id = next((s["id"] for s in scenarios if query in s.get("search_queries", [])), None)
        store.record_candidates(leaf, items, "atlas.discovery.v4", discovery={
            "query": query, "page": 1, "scenario_id": scenario_id, "order": "best_match",
            **({"split_pages": response["split_pages"]} if response.get("split_pages") else {})})
        entry = {"query": query, "total_count": response.get("total_count"), "returned": len(items),
                 "repository_ids": [m["id"] for m in items], "incomplete_results": response.get("incomplete_results", False),
                 "physical_requests": response.get("search_request_count", 1), "split_pages": response.get("split_pages", [])}
        evidence.append(entry)
        atomic_json(BASE / (leaf + "-search.json"), evidence)
        run["search_requests"] = run.get("search_requests", 0) + entry["physical_requests"]
        store._save_run(run)
    return evidence


def restore_plan(store, leaf, run):
    if leaf in PLANS:
        path = ROOT / "model-cache" / (PLANS[leaf] + ".json")
        value = json.loads(path.read_text())
        plan = value["data"]
        origin = {"method": "revalidate_original_archived_response", "path": str(path),
                  "sha256": digest(path.read_text()), "provider": value["provider"], "model": value["model"]}
    elif (BASE / (leaf + "-plan.json")).exists():
        saved = json.loads((BASE / (leaf + "-plan.json")).read_text())
        plan, origin = saved["original_response"], saved["origin"]
        run["reused_repair_plan"] = str(BASE / (leaf + "-plan.json"))
    else:
        plan = Model(ROOT, run, store._save_run, max_tokens=6500, fast=True).ask(
            "scenarios_open", PLAN_PROMPT, {"leaf": leaf, "definition": context_for(leaf)})
        origin = {"method": "fresh_bounded_model_request", "receipts": run.get("model_receipts", [])}
    scenarios = validate_plan(plan, leaf)
    atomic_json(BASE / (leaf + "-plan.json"), {"origin": origin, "original_response": plan, "validated_scenarios": scenarios})
    with store.connect() as con:
        # Old overview scenarios and any existing matches remain addressable.
        store._scenarios(con, scenarios, leaf, prune=False)
    return scenarios


def update_leaf_counts(store, job, leaf):
    with store.connect() as con:
        total = con.execute("SELECT COUNT(*) FROM oss_candidate WHERE leaf=?", (leaf,)).fetchone()[0]
        selected = con.execute("SELECT COUNT(*) FROM oss_batch_target WHERE job_id=? AND leaf=?", (JOB, leaf)).fetchone()[0]
        assert selected <= 60
        con.execute("UPDATE oss_batch_leaf SET selected_count=?,candidate_total=?,deferred_count=? WHERE job_id=? AND leaf=?", (
            selected, total, total - selected, JOB, leaf))


def fill_empty_leaf(store, jobs, job, leaf, scenarios):
    with store.connect() as con:
        count = con.execute("SELECT COUNT(*) FROM oss_batch_target WHERE job_id=? AND leaf=?", (JOB, leaf)).fetchone()[0]
    if not count:
        selected = select_first_round(store.candidates(leaf), scenarios, context_for(leaf).splitlines()[0], 60)
        with store.connect() as con:
            for item in selected:
                con.execute("INSERT INTO oss_batch_target VALUES (?,?,?,?,?,?,?,?)", (
                    JOB, leaf, item["repository_id"], item["data"]["meta"]["full_name"], "pending", None, canonical(item["priority"]), None))
    update_leaf_counts(store, job, leaf)
    jobs.load_ledger(job, include_targets=True)
    remaining = [t for t in job["targets"][leaf] if t["status"] in {"pending", "running"}]
    jobs.execute_groups(job, leaf, remaining)
    jobs.load_ledger(job, include_targets=True)
    targets = job["targets"][leaf]
    if any(t["status"] in {"pending", "running", "failed"} for t in targets):
        raise ValueError("补查目标仍有未完成或失败记录")
    with store.connect() as con:
        con.execute("UPDATE oss_batch_leaf SET state='first_round_done' WHERE job_id=? AND leaf=?", (JOB, leaf))
    return {"selected": len(targets), "processed_now": len(remaining),
            "published": sum(t["status"] in {"accepted", "partial"} for t in targets),
            "rejected": sum(t["status"] == "rejected" for t in targets)}


def repair_portfolio_matches(store, run, scenarios):
    leaf = "portfolio-management-system"
    targets = [c for c in store.candidates(leaf) if c["status"] in {"accepted", "partial"}]
    pending, previous = [], {}
    versions = {}
    with store.connect() as con:
        ids = [c["repository_id"] for c in targets]
        for row in con.execute("SELECT data FROM oss_candidate WHERE repository_id IN (" + ",".join("?" for _ in ids) + ")", ids):
            meta = json.loads(row[0])["meta"]
            versions.setdefault(meta["id"], set()).add(digest(canonical({
                "id": meta["id"], "pushed_at": meta.get("pushed_at"), "branch": meta.get("default_branch")})))
    for candidate in targets:
        meta = candidate["data"]["meta"]
        old = store.previous(meta["full_name"], leaf)
        key = digest(canonical({"id": meta["id"], "pushed_at": meta.get("pushed_at"), "branch": meta.get("default_branch")}))
        card_key = digest(canonical({"id": meta["id"], "pushed_at": old.get("pushed_at"), "branch": old.get("default_branch")}))
        # Shared global cards can refer to an older actual repository version.
        # Missing README is an honest metadata-only input, never invented text.
        resources = {"readme": None, "license": None, "warnings": ["原归档未提供README，仅依据仓库元数据核对场景"]}
        for version in dict.fromkeys([key, card_key, *sorted(versions.get(meta["id"], set()))]):
            path = ROOT / "sources" / (version + ".json")
            if path.is_file():
                resources = json.loads(path.read_text())
                break
        pending.append((meta, resources))
        previous[meta["id"]] = old
    class ExistingLicenses:
        def classify(self, meta, *_):
            return previous[meta["id"]]["license"]
    model = Model(ROOT, run, store._save_run, max_tokens=6500, fast=True)
    added = 0
    for group, items, error in extract_groups(store, leaf, run, model, pending, context_for(leaf), scenarios, instruction=MATCH_PROMPT):
        if error:
            raise error
        for meta, resources in group:
            item = next(i for i in items if i["repository_id"] == meta["id"])
            matches = relaxed_card(item, meta, resources, scenarios, ExistingLicenses())["matches"]
            old = previous[meta["id"]]
            all_matches = {m["scenario_id"]: m for m in old["matches"]}
            before = len(all_matches)
            all_matches.update({m["scenario_id"]: m for m in matches})
            with store.connect() as con:
                store._upsert(con, {**old, "matches": list(all_matches.values())}, leaf)
            added += len(all_matches) - before
            run["processed"] += 1
            store._save_run(run)
    return {"existing_cards_reviewed": len(pending), "new_scenario_matches": added,
            "global_facts_and_licenses_preserved": True, "old_matches_preserved": True}


def main():
    assert os.environ.get("ATLAS_FACTORY_DISABLE_WORKER") == "1"
    assert os.environ.get("ATLAS_OSS_MODEL_CONCURRENCY") == "4"
    store = PreservingStore(PACK / "atlas/oss-catalog.sqlite", bootstrap=False)
    lock = store._lock()
    state_path = BASE / "STATE.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {"job_id": JOB, "started_at": now(), "cases": {}}
    if state.get("state") == "interrupted":
        state.setdefault("recovery_history", []).append({k: state.get(k) for k in ["failed_at", "error_type", "error"]})
        for key in ["failed_at", "error_type", "error"]:
            state.pop(key, None)
    state.update(pid=os.getpid(), state="running")
    atomic_json(state_path, state)
    jobs = BatchJobs(store)
    job = jobs.get(JOB, detect_interruption=False)
    try:
        with store.connect() as con:
            for row in con.execute("SELECT data FROM oss_run WHERE status='running'").fetchall():
                interrupted = json.loads(row[0])
                if interrupted.get("repair_of") in ERRORS.values():
                    interrupted.update(status="interrupted", finished_at=now())
                    con.execute("UPDATE oss_run SET status=?,data=? WHERE id=?", ("interrupted", canonical(interrupted), interrupted["id"]))
        manifest = json.loads((CAMPAIGN / "MANIFEST.json").read_text())
        assert job["leaves"] == [v["slug"] for v in manifest["leaves"]]
        assert (job["first_round_limit"], job["batch_size"], job["scope"]) == (60, 16, "first_round")
        assert all(leaf in job["leaves"] for leaf in ERRORS)
        baseline = BASE / "BEFORE.json"
        if not baseline.exists():
            backup = Path("/private/tmp/atlas-before-four-error-repair-2026-10-29.sqlite")
            with store.connect() as src, sqlite3.connect(backup) as dst:
                src.backup(dst)
            atomic_json(baseline, {"job_id": JOB, "backup": str(backup), "job_status": job["status"],
                                  "errors": job["errors"], "processed": job["processed"], "total": job["total"],
                                  "deferred_total": job["deferred_total"], "batch_job_count": len(jobs.list()),
                                  "manifest_sha256": digest((CAMPAIGN / "MANIFEST.json").read_text())})
        job["four_error_repair"] = {"started_at": state["started_at"], "state": "running", "pid": os.getpid(), "record": str(state_path)}
        jobs.save(job)
        for leaf, error in ERRORS.items():
            if state["cases"].get(leaf, {}).get("resolved"):
                continue
            run = jobs.new_run(leaf)
            run.update(source_policy="essential", repair_of=error)
            store._save_run(run)
            job["runs"].append(run["id"])
            jobs.save(job)
            if leaf == "log-management":
                evidence = search(store, leaf, store.scenarios(leaf), run, ["request id log search"])
                result = {"queries_recovered": len(evidence), "returned": evidence[0]["returned"], "existing_60_targets_retained": True}
            else:
                scenarios = restore_plan(store, leaf, run)
                queries = [q for s in scenarios for q in s["search_queries"][:1]]
                search_path = BASE / (leaf + "-search.json")
                prior = json.loads(search_path.read_text()) if search_path.exists() else []
                evidence = prior if [e["query"] for e in prior] == list(dict.fromkeys(queries)) else search(store, leaf, scenarios, run, queries)
                result = (fill_empty_leaf(store, jobs, job, leaf, scenarios) if leaf in PLANS
                          else repair_portfolio_matches(store, run, scenarios))
                result.update(valid_scenarios=len(scenarios), queries_recovered=len(evidence))
            update_leaf_counts(store, job, leaf)
            run.update(status="completed", finished_at=now())
            store._save_run(run)
            state["cases"][leaf] = {"resolved": True, "original_error": error, "run_id": run["id"],
                                    "finished_at": now(), **result}
            atomic_json(state_path, state)
            jobs.load_ledger(job, include_targets=True)
            jobs.save(job)
            print(canonical({"leaf": leaf, "resolved": True, **result}), flush=True)
        resolved_at = now()
        remaining = []
        for error in job["errors"]:
            if ERRORS.get(error.get("leaf")) == error.get("error") and state["cases"].get(error["leaf"], {}).get("resolved"):
                job.setdefault("resolved_errors", []).append({**error, "resolved_at": resolved_at, "repair_record": str(state_path)})
            else:
                remaining.append(error)
        job["errors"] = remaining
        jobs.load_ledger(job, include_targets=True)
        assert len(job["completed_leaves"]) == 1598
        assert not any(t["status"] in {"pending", "running"} for group in job["targets"].values() for t in group)
        job["status"] = "partial" if remaining or job["leaf_errors"] or any(t["status"] == "failed" for group in job["targets"].values() for t in group) else "completed"
        job["four_error_repair"].update(state="completed", finished_at=resolved_at)
        job["original_first_round_finished_at"] = job.get("original_first_round_finished_at", job["finished_at"])
        job["finished_at"] = resolved_at
        jobs.save(job)
        state.update(state="completed", finished_at=resolved_at, job_status=job["status"], processed=job["processed"],
                     total=job["total"], deferred_pending=job["deferred_total"], unresolved_errors=len(remaining))
        atomic_json(state_path, state)
        print(canonical({k: state[k] for k in ["state", "job_status", "processed", "total", "deferred_pending", "unresolved_errors"]}), flush=True)
    except BaseException as error:
        if "run" in locals():
            run.update(status="interrupted", finished_at=now())
            store._save_run(run)
        state.update(state="interrupted", failed_at=now(), error_type=type(error).__name__,
                     error=str(error) if isinstance(error, (CatalogError, ValueError)) else "修复中断；检查点及原错误保留")
        atomic_json(state_path, state)
        job["four_error_repair"].update(state="interrupted", failed_at=now())
        jobs.save(job)
        raise
    finally:
        lock.close()


if __name__ == "__main__":
    main()
