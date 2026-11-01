"""Coverage-first discovery over existing Atlas leaves, with honest partial cards."""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
import os
from pathlib import Path
import re
from threading import Event, Lock
from urllib.parse import urlencode

from atlas_runtime import atomic_json
from oss_catalog import (CatalogError, GitHub, ModelServiceUnavailable, ServiceUnavailable, WorkflowInterrupted, available_leaves, canonical, digest, now,
                         repository_metadata, validate_leaf)
from oss_discovery import (BATCH_SIZE, LicenseMatcher, Model, PLAN_PROMPT, ROOT,
                           QualityRejection, response_items, review_card, validate_plan)
from oss_sources import collect_sources, documents

VERSION = "atlas.discovery.v4"
SOURCE_ROOT = Path(__file__).resolve().parent
try:
    MODEL_WORKERS = max(1, min(4, int(os.environ.get("ATLAS_OSS_MODEL_CONCURRENCY", "4"))))
except ValueError:
    MODEL_WORKERS = 4
EXTRACT = """整理真实仓库，优先完成收录，缺资料不淘汰。可以收录应用、库、资源集合，标明 project_type。
只依据输入的官方资料，不凭记忆补功能。只在明确与领域无关时 relevant:false 并写 rejection_reason；资料不足 relevant:true。
教程、API资料索引、硬件设计实例标为resource，保留收录；不能把它们介绍成可部署的通用软件。
区分已实现、路线图、未完成后端、合成数据演示与真实运行。介绍要说明这些边界；依赖外部SaaS/商业SDK许可、宿主或人工流程时，在对应场景列条件。
定位、介绍、适用范围、功能有多少写多少，未知返回空。每项可给 source_id 和原文 quote，但不强求完整引文；不能编造引文。
场景可以直接适用、条件适用或合理推断待核实；分别用 direct/conditional/unverified。条件适用列出真实前提，推断不能伪装事实。
只关联输入的场景 ID；没有可靠关联可 matches:[]，项目仍收录。许可证由独立流程判断。
简短中文输出，不解释过程。每个项目给少量关键功能和场景关联即可，优先提供 source_id，quote可省略。不计算字数。
JSON: {"items":[{"repository_id":123,"relevant":true,"project_type":"application/library/collection/resource/unknown",
"positioning":{"text":"定位","source_id":"readme","quote":"可选原文"},"summary":{"text":"介绍","source_id":"readme"},
"scope":{"text":"适用范围","source_id":"readme"},"features":[{"text":"功能","source_id":"readme"}],
"matches":[{"scenario_id":"输入ID","reason":"理由","applicability":"unverified","conditions":[],"source_id":"readme"}]}]}"""


def context_for(leaf):
    validate_leaf(leaf)
    text = (SOURCE_ROOT / "applications" / (leaf + ".md")).read_text()
    return re.split(r"(?im)^## (?:Representative Products|Sources|Related Application Types)", text)[0][:14000]


def prepare_leaf(store, leaf, run, github=None, model=None, root=None, search=True, search_pages=1):
    validate_leaf(leaf)
    root = Path(root or ROOT)
    github = github or GitHub()
    model = model or Model(root, run, store._save_run, max_tokens=6500, fast=True)
    context = context_for(leaf)
    scenarios = store.scenarios(leaf)
    if not scenarios:
        run["phase"] = "scenarios"
        store._save_run(run)
        try:
            plan = model.ask("scenarios_open", PLAN_PROMPT, {"leaf": leaf, "definition": context})
            scenarios = validate_plan(plan, leaf)
        except ModelServiceUnavailable:
            raise
        except CatalogError as error:
            # An unusable scenario response may fall back to a preliminary taxonomy scene.
            run["errors"].append({"error": str(error)})
            scenarios = [{"id": "auto-" + leaf + "-overview", "name": available_leaves()[leaf] + "的实际使用",
                          "description": "初步场景，后续可补充具体任务。", "leaf": leaf,
                          "leaf_name": available_leaves()[leaf], "generation_method": "taxonomy_fallback"}]
        with store.connect() as con:
            store._scenarios(con, scenarios, leaf, prune=False)
    searches = []
    if search:
        run["phase"] = "search"
        store._save_run(run)
        category = context.splitlines()[0].removeprefix("# ")
        queries = list(dict.fromkeys([category, *(q for s in scenarios for q in s.get("search_queries", [])[:1])]))
        for keywords in queries:
            # No popularity threshold and no model-supplied repository targeting.
            keywords = re.sub(r"(?:repo|org|user):\S+|https?://\S+", "", keywords, flags=re.I).strip()
            if not keywords:
                continue
            for page in range(1, search_pages + 1):
                query = keywords + " in:name,description,topics archived:false fork:false"
                search_options = {"q": query, "per_page": 100, "page": page}
                if run.get("source_policy") != "essential":
                    search_options["sort"] = "stars"
                try:
                    response = github.get("/search/repositories?" + urlencode(search_options))
                except ServiceUnavailable:
                    raise
                except CatalogError as error:
                    run["errors"].append({"error": str(error), "query": keywords})
                    break
                run["search_requests"] = run.get("search_requests", 0) + response.get("search_request_count", 1)
                items = [repository_metadata(m) for m in response.get("items", []) if not m.get("private") and not m.get("disabled")]
                scenario_id = next((s["id"] for s in scenarios if keywords in s.get("search_queries", [])), None)
                store.record_candidates(leaf, items, VERSION, discovery={"query": keywords, "page": page,
                                                                         "scenario_id": scenario_id,
                                                                         **({"split_pages": response["split_pages"]} if response.get("split_pages") else {}),
                                                                         "order": "best_match" if run.get("source_policy") == "essential" else "stars"})
                searches.append({"query": query, "page": page, "total_count": response.get("total_count", 0),
                                 "repository_ids": [m["id"] for m in items], "incomplete_results": response.get("incomplete_results", False),
                                 **({"split_pages": response["split_pages"]} if response.get("split_pages") else {})})
                if len(items) < 100 or page * 100 >= min(response.get("total_count", 0), 1000):
                    break
    return scenarios, context, searches


def relaxed_card(item, meta, resources, scenarios, matcher):
    docs = documents(resources, meta["full_name"])
    meta_source = {"kind": "repository", "url": meta["url"], "sha256": digest(canonical(meta)),
                   "retrieved_at": resources.get("identity_verified_at") or now()}
    by_id = {d["source_id"]: d for d in docs}
    by_id["repository"] = {"source_id": "repository", "text": re.sub(r"\s+", " ", meta.get("description") or meta["full_name"]), "source": meta_source}
    missing, notes = [], list(resources.get("warnings", []))

    def evidence(value):
        doc = by_id.get(value.get("source_id", "readme"))
        if not doc:
            return None
        source = doc["source"]
        quote = re.sub(r"\s+", " ", str(value.get("quote") or "")).strip()
        if quote and quote.casefold() not in doc["text"].casefold():
            return None  # Fabricated quotes are never stored or displayed.
        return {"source_url": source["url"], "immutable_url": source.get("immutable_url", ""),
                "source_sha256": source["sha256"], "excerpt": quote, "source_kind": source["kind"],
                "verification": "quote_matched" if quote else "source_based"}

    def fact(key, fallback):
        value = item.get(key) or {}
        if isinstance(value, str):
            value = {"text": value}
        proof = evidence(value) if isinstance(value, dict) else None
        text = value.get("text") if isinstance(value, dict) else None
        if not isinstance(text, str) or not text.strip() or not proof:
            missing.append(key)
            proof = evidence({"source_id": "repository", "quote": by_id["repository"]["text"][:500]})
            return fallback[:1500], proof
        return text.strip()[:1500], proof

    positioning, pe = fact("positioning", "候选项目 · 定位待补充")
    summary, se = fact("summary", meta.get("description") or "仓库已确认公开存在，项目介绍待补充。")
    scope, sce = fact("scope", "适用范围待补充；请查看官方项目资料。")
    features = []
    for feature in (item.get("features") or [])[:5]:
        if isinstance(feature, dict) and isinstance(feature.get("text"), str) and (proof := evidence(feature)):
            features.append({"text": feature["text"][:500], "evidence": proof})
    if not features:
        missing.append("features")
    matches = []
    allowed = {s["id"] for s in scenarios}
    for match in item.get("matches") or []:
        if not isinstance(match, dict) or match.get("scenario_id") not in allowed or not isinstance(match.get("reason"), str):
            continue
        if any(m["scenario_id"] == match["scenario_id"] for m in matches):
            continue
        proof = evidence(match)
        kind = match.get("applicability", "unverified")
        conditions = [str(c)[:300] for c in match.get("conditions", []) if isinstance(c, str)][:4]
        if not proof or kind not in {"direct", "conditional", "unverified"} or kind == "conditional" and not conditions:
            kind = "unverified"
        if kind == "direct" and conditions:
            kind = "conditional"
        proof = proof or {**se, "excerpt": "", "verification": "inferred"}
        matches.append({"scenario_id": match["scenario_id"], "reason": match["reason"][:900],
                        "applicability": kind, "conditions": conditions, "evidence": proof})
    if not matches:
        missing.append("scenario_associations")
    license_result = matcher.classify(meta, resources.get("license"), resources.get("readme"))
    if license_result["status"] == "pending":
        missing.append("license_verification")
    if license_result["status"] != "open_source":
        positioning, summary, scope = [re.sub(r"开源|\bopen[ -]source\b", "", value, flags=re.I).strip() for value in (positioning, summary, scope)]
    card = {"repository_id": meta["id"], "name": meta["name"], "full_name": meta["full_name"], "github_url": meta["html_url"],
            "positioning": positioning, "positioning_evidence": pe, "summary": summary, "summary_evidence": se,
            "scope": scope, "scope_evidence": sce, "features": features, "matches": matches,
            "languages": [meta["language"]] if meta.get("language") else [], "language_method": "repository_primary_language",
            "license": license_result, "sources": [d["source"] for d in docs] + [meta_source],
            "pushed_at": meta.get("pushed_at"), "default_branch": meta.get("default_branch"), "archived": meta.get("archived", False),
            "checked_at": now(), "project_type": item.get("project_type", "unknown"),
            "editorial_method": "依据公开仓库资料整理；逐字引文、资料概述和待核实推断分别标注，缺项先收录。",
            "generation_method": "live_search_coverage_first", "generator_version": VERSION}
    try:
        card = review_card(card)
    except QualityRejection as error:
        notes.append(str(error))
        # Keep the project, but a previous evidence warning must not turn into
        # a confirmed capability merely because publication is now permissive.
        for match in card["matches"]:
            match["applicability"] = "unverified"
            match["evidence"] = {**match["evidence"], "verification": "inferred", "excerpt": ""}
        for feature in card["features"]:
            feature["evidence"] = {**feature["evidence"], "verification": "inferred", "excerpt": ""}
        card["project_type"] = "unknown"
    card.update(completeness="partial" if missing or notes or any(m["applicability"] == "unverified" for m in card["matches"]) else "complete",
                missing_fields=missing, collection_notes=notes)
    return card


def service_failure(current, error):
    if current is None or current.retryable and not error.retryable:
        return error
    if current.retryable and error.retryable:
        current.retry_after = max(current.retry_after or 0, error.retry_after or 0)
    return current


def extract_groups(store, leaf, run, model, pending, context, scenarios, instruction=EXTRACT):
    """Parallel network calls with isolated counters; one coordinator commits cards."""
    groups = [pending[offset:offset + 4] for offset in range(0, len(pending), 4)]
    workers = min(MODEL_WORKERS, len(groups))
    run.update(phase="extract", concurrency={"source_workers": 4, "model_workers": workers,
                                             "configured_model_workers": MODEL_WORKERS})
    store._save_run(run)
    lock, stopped = Lock(), Event()
    stop_errors = []
    counters = {k: run.get(k, 0) for k in ("model_calls", "model_cache_hits")}
    history = {k: list(run.get(k, [])) for k in ("model_receipts", "model_errors")}
    tasks = {}

    def save_task(identifier, state):
        with lock:
            tasks[identifier] = deepcopy(state)
            run["model_tasks"] = deepcopy(tasks)
            for key, base in counters.items():
                run[key] = base + sum(t.get(key, 0) for t in tasks.values())
            for key, base in history.items():
                run[key] = sorted(base + [r for t in tasks.values() for r in t.get(key, [])], key=lambda r: r.get("created_at", ""))
            retries = [{**t["model_retry"], "task_id": key} for key, t in tasks.items() if t.get("model_retry")]
            if retries:
                run["model_retry"] = next((r for r in retries if r["state"] in {"waiting", "requesting"}), retries[-1])
            policy = next((t["model_retry_policy"] for t in tasks.values() if t.get("model_retry_policy")), None)
            if policy:
                run["model_retry_policy"] = policy
            store._save_run(run)

    def extract(entry):
        index, group = entry
        if stopped.is_set():
            return group, None, stop_errors[0]
        extractor = model
        task = {"id": run["id"], "task_id": str(index), "model_calls": 0, "state": "running", "started_at": now()}
        if workers > 1 and isinstance(model, Model):
            extractor = Model(model.root, task, lambda state: save_task(str(index), state),
                              max_tokens=model.max_tokens, fast=model.fast)
        payload = {"leaf": leaf, "definition": context[:5000], "scenarios": [{k: s[k] for k in ("id", "name", "description")} for s in scenarios],
                   "repositories": [{"repository_id": m["id"], "name": m["full_name"], "description": (m.get("description") or "")[:2000],
                                     "documents": [{"source_id": d["source_id"], "text": d["text"][:11000]} for d in documents(r, m["full_name"])]} for m, r in group]}
        try:
            items = response_items(extractor.ask("extract_open", instruction, payload), {m["id"] for m, _ in group})
            task["state"] = "completed"
            return group, items, None
        except ModelServiceUnavailable as error:
            with lock:
                if not stop_errors:
                    stop_errors.append(error)
                stopped.set()
            task["state"] = "paused_model"
            return group, None, error
        except CatalogError as error:
            task["state"] = "partial"
            return group, None, error
        finally:
            if extractor is not model:
                task["finished_at"] = now()
                if task["state"] == "running":
                    task["state"] = "failed"
                save_task(str(index), task)

    if not groups:
        return []
    if workers == 1:
        return [extract(entry) for entry in enumerate(groups)]
    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="atlas-extract") as executor:
        return list(executor.map(extract, enumerate(groups)))


def read_candidate_sources(store, leaf, selected_ids, *, root=None, github=None, source_policy="full"):
    """Read one bounded group without publishing cards or touching checkpoints."""
    root = Path(root or ROOT)
    github = github or GitHub()
    selected = [c for c in store.candidates(leaf) if c["repository_id"] in set(selected_ids)]
    started_at = now()

    def read(candidate):
        meta = dict(candidate["data"]["meta"])
        counts = {k: 0 for k in ("source_cache_hits", "source_fetches", "document_cache_hits", "document_fetches")}
        try:
            options = ({"include_documents": False, "search_verified_at": candidate["data"].get("search_verified_at")}
                       if source_policy == "essential" else {})
            resources, cached = collect_sources(github, meta, root, counts, allow_partial=True, **options)
            return meta, resources, counts, None
        except ServiceUnavailable as error:
            return meta, None, counts, error
        except Exception as error:
            return meta, None, counts, str(error) if isinstance(error, CatalogError) else "读取资料失败，候选已保留"

    with ThreadPoolExecutor(max_workers=4, thread_name_prefix="atlas-source") as executor:
        reads = list(executor.map(read, selected))
    return {"selected_ids": list(selected_ids), "reads": reads, "started_at": started_at,
            "finished_at": now(), "source_policy": source_policy}


def discover_open_leaf(store, leaf, run, github=None, model=None, root=None, selected_ids=None,
                       search=True, search_pages=1, on_candidate=None, prepared_sources=None):
    validate_leaf(leaf)
    root = Path(root or ROOT)
    github = github or GitHub()
    model = model or Model(root, run, store._save_run, max_tokens=6500, fast=True)
    run.update(mode="automatic", phase="prepare", source_cache_hits=0, source_fetches=0,
               document_cache_hits=0, document_fetches=0, search_requests=0, partial=0, rejected=0)
    audit = {"schema": VERSION, "leaf": leaf, "run_id": run["id"], "source_reads": [], "decisions": []}
    audit_path = root / "runs" / (run["id"] + ".json")
    try:
        scenarios, context, searches = prepare_leaf(store, leaf, run, github, model, root, search, search_pages)
        audit["searches"] = searches
        pool = store.candidates(leaf)
        if selected_ids is None:
            selected_ids = [c["repository_id"] for c in pool if c["status"] in {"pending", "needs_evidence", "failed"}][:BATCH_SIZE]
        selected = [c for c in pool if c["repository_id"] in set(selected_ids)]
        run.update(total=len(selected), selected_ids=[c["repository_id"] for c in selected], discovered=len(pool))
        audit["selected_ids"] = run["selected_ids"]
        store._save_run(run)

        def finish(meta, state, reason):
            store.candidate_result(leaf, meta["id"], state, reason, meta)
            run["processed"] += 1
            audit["decisions"].append({"repository_id": meta["id"], "repo": meta["full_name"], "status": state, "reason": reason})
            store._save_run(run)
            atomic_json(audit_path, audit)
            if on_candidate:
                on_candidate(meta["id"], state, reason)

        run["phase"] = "read_sources"
        store._save_run(run)
        bundle = prepared_sources or read_candidate_sources(store, leaf, selected_ids, root=root, github=github,
                                                            source_policy=run.get("source_policy", "full"))
        if set(bundle["selected_ids"]) != set(selected_ids):
            raise CatalogError("预读取资料与本批候选不一致", 422)
        reads = bundle["reads"]
        run["source_timing"] = {"started_at": bundle["started_at"], "finished_at": bundle["finished_at"],
                                "prefetched": prepared_sources is not None}
        pending = []
        service_error = None
        for meta, resources, counts, error in reads:
            for key, value in counts.items():
                run[key] = run.get(key, 0) + value
            if isinstance(error, ServiceUnavailable):
                service_error = service_failure(service_error, error)
                run.setdefault("source_errors", []).append({"repo": meta["full_name"], "error": str(error),
                                                            "code": error.code, "upstream_status": error.upstream_status,
                                                            "retryable": error.retryable, "retry_after": error.retry_after})
            elif error:
                run["failed"] += 1
                run["errors"].append({"repo": meta["full_name"], "error": error})
                finish(meta, "failed", error)
            else:
                audit["source_reads"].append({"repository_id": meta["id"], "repo": meta["full_name"], "documents": [d["source"] for d in documents(resources, meta["full_name"])], "warnings": resources.get("warnings", [])})
                pending.append((meta, resources))
        matcher = LicenseMatcher(root)
        model_error = service_error
        for group, items, error in extract_groups(store, leaf, run, model, pending, context, scenarios):
            if isinstance(error, ModelServiceUnavailable):
                model_error = service_failure(model_error, error)
                continue
            if error:
                items = [{"repository_id": m["id"], "relevant": True} for m, _ in group]
                for _, resources in group:
                    resources.setdefault("warnings", []).append("介绍待补充：" + str(error))
            for meta, resources in group:
                try:
                    item = next(i for i in items if i["repository_id"] == meta["id"])
                    if item.get("relevant") is False and item.get("decision", "exclude") == "exclude":
                        reason = str(item.get("rejection_reason") or "资料表明与当前领域无关")[:1200]
                        run["rejected"] += 1
                        finish(meta, "rejected", reason)
                        continue
                    try:
                        card = relaxed_card(item, meta, resources, scenarios, matcher)
                    except (CatalogError, ValueError, TypeError, KeyError):
                        resources.setdefault("warnings", []).append("整理响应的部分字段不可用，先保存已确认的仓库资料")
                        card = relaxed_card({}, meta, resources, scenarios, matcher)
                    previous = store.previous(meta["full_name"], leaf)
                    # A sparse retry must never replace stronger existing project facts.
                    if previous and card["completeness"] == "partial" and previous.get("completeness", "complete") == "complete":
                        with store.connect() as con:
                            con.execute("INSERT OR IGNORE INTO oss_leaf_project VALUES (?,?)", (leaf, meta["id"]))
                        run["unchanged"] += 1
                    else:
                        with store.connect() as con:
                            outcome = store._upsert(con, card, leaf)
                        run[outcome] += 1
                    state = "partial" if card["completeness"] == "partial" else "accepted"
                    run["partial"] += state == "partial"
                    finish(meta, state, "已收录；资料待补充或关联待核实" if state == "partial" else "已依据官方资料整理并收录")
                except Exception as error:
                    run["failed"] += 1
                    reason = str(error) if isinstance(error, CatalogError) else "整理失败，已跳过并保留候选"
                    run["errors"].append({"repo": meta["full_name"], "error": reason})
                    finish(meta, "failed", reason)
        if model_error:
            raise model_error
        run["status"] = "partial" if run["failed"] else "completed"
        run["candidate_counts"] = store.candidate_counts(leaf)
    except ServiceUnavailable as error:
        run["status"] = "paused_model"
        run["errors"].append({"error": str(error)})
        raise
    except CatalogError as error:
        run["status"] = "failed"
        run["errors"].append({"error": str(error)})
    except Exception as error:
        interruption = WorkflowInterrupted(type(error).__name__, run.get("phase"))
        run["status"] = "interrupted"
        run["interruption"] = {"exception_type": interruption.exception_type, "phase": interruption.phase}
        run["errors"].append({"error": str(interruption), "code": interruption.code})
        raise interruption from error
    finally:
        run.update(finished_at=now(), audit_path=str(audit_path))
        audit["result"] = dict(run)
        atomic_json(audit_path, audit)
        store._save_run(run)
    return run
