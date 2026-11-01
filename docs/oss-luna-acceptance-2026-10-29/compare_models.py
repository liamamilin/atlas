"""Paired 50-project comparison; reuse identical Luna receipts, request DeepSeek only.

No catalog writes, model-setting changes, collection jobs or full audit runs.
"""
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import threading
import time

import review_sample as core

OUT = core.OUT / "paired-50"
DS_MODEL = "deepseek-v4.1-flash"
PAIR_COUNT = 50
SEED = "atlas-paired50-2026-10-29-v1"


def select_pairs(manifest, calibration_ids):
    by_id = {v["repository_id"]: v for v in manifest["projects"]}
    assert set(calibration_ids) <= set(by_id)
    groups = defaultdict(list)
    for v in by_id.values():
        groups[v["domain"]].append(v)
    for g in groups:
        groups[g].sort(key=lambda v: core.digest(SEED + ":" + str(v["repository_id"])))
    selected = {rid: by_id[rid] for rid in calibration_ids}
    for g in sorted(groups):
        if not any(v["domain"] == g for v in selected.values()):
            v = next(v for v in groups[g] if v["repository_id"] not in selected)
            selected[v["repository_id"]] = v
    while len(selected) < PAIR_COUNT:
        counts = Counter(v["domain"] for v in selected.values())
        eligible = [g for g in groups if any(v["repository_id"] not in selected for v in groups[g])]
        g = min(eligible, key=lambda g: (counts[g] / manifest["strata"][g]["population"], g))
        v = next(v for v in groups[g] if v["repository_id"] not in selected)
        selected[v["repository_id"]] = v
    assert len(selected) == PAIR_COUNT and len({v["domain"] for v in selected.values()}) == len(groups)
    return sorted(selected.values(), key=lambda v: (v["domain"], core.digest(SEED + ":" + str(v["repository_id"]))))


def citation_metrics(result, payload):
    sources = {v["id"]: v["text"] for v in payload["sources"]}
    counts = Counter()
    for issue in result.get("review", {}).get("issues", []):
        sid, quote = issue.get("source_id"), issue.get("quote")
        if isinstance(quote, str) and "[ARCHIVE TEXT OMITTED]" in quote:
            counts["truncation_marker_not_official_evidence"] += 1
        elif not sid and not quote:
            counts["uncited_absence_claims"] += 1
        elif sid not in sources or not isinstance(quote, str) or not quote:
            counts["invalid_reference"] += 1
        elif quote in sources[sid]:
            counts["literal_match"] += 1
        elif " ".join(quote.split()) in " ".join(sources[sid].split()):
            counts["whitespace_only_difference"] += 1
        else:
            counts["not_found_in_source"] += 1
    return dict(counts)


def prepare():
    manifest = json.loads((core.OUT / "MANIFEST.json").read_text())
    assert manifest["prompt_sha256"] == core.digest(core.PROMPT)
    triage = json.loads((core.OUT / "HUMAN_TRIAGE.json").read_text())
    gold = [v["repository_id"] for v in triage["cases"]]
    projects = select_pairs(manifest, gold)
    record = {"prepared_at": core.now(), "job_id": core.JOB, "pair_count": PAIR_COUNT,
              "model_reviews": {"luna": 50, "deepseek": 50}, "new_luna_requests": 0,
              "luna_model": core.MODEL, "deepseek_requested_model": DS_MODEL, "seed": SEED,
              "prompt_sha256": manifest["prompt_sha256"], "domains": len({v["domain"] for v in projects}),
              "calibration_ids": gold, "selection": "Six pre-adjudicated calibration cases plus deterministic domain-covered sampling from the frozen100. Not an unbiased population error-rate estimate.",
              "settings_sha256_before": hashlib.sha256(core.atlas_model.config_path().read_bytes()).hexdigest(),
              "production_job_sha256": manifest["production_job_sha256"], "projects": projects,
              "full_run_started": False, "production_writes": False}
    OUT.mkdir(exist_ok=True)
    target = OUT / "MANIFEST.json"
    if target.exists():
        old = json.loads(target.read_text())
        assert [v["repository_id"] for v in old["projects"]] == [v["repository_id"] for v in projects]
        assert old["prompt_sha256"] == record["prompt_sha256"]
        return old
    for item in projects:
        path = core.OUT / item["input_path"]
        assert core.digest(path.read_text()) == item["input_sha256"]
        luna_path = core.OUT / "results" / (str(item["repository_id"]) + ".json")
        luna = json.loads(luna_path.read_text())
        assert luna["status"] == "reviewed" and luna["input_sha256"] == item["input_sha256"]
        assert luna["requested_model"] == core.MODEL
        item["luna_receipt_sha256"] = hashlib.sha256(luna_path.read_bytes()).hexdigest()
    core.atomic_json(target, record)
    return record


def deepseek_one(item, provider):
    dest = OUT / "deepseek" / (str(item["repository_id"]) + ".json")
    if dest.exists():
        result = json.loads(dest.read_text())
        assert result["input_sha256"] == item["input_sha256"]
        return result
    path = core.OUT / item["input_path"]
    assert core.digest(path.read_text()) == item["input_sha256"]
    payload = json.loads(path.read_text())
    result = {"repository_id": item["repository_id"], "domain": item["domain"], "input_sha256": item["input_sha256"],
              "prompt_sha256": core.digest(core.PROMPT), "provider": provider, "requested_model": DS_MODEL,
              "started_at": core.now(), "status": "requesting", "attempts": []}
    core.atomic_json(dest, result)
    started = time.monotonic()
    try:
        response = core.atlas_model.chat([{"role": "user", "content": core.canonical(payload)}], system=core.PROMPT,
                                        provider=provider, model=DS_MODEL, max_tokens=core.MAX_OUTPUT,
                                        temperature=0, thinking=False, timeout=90, session_id="atlas-quality-paired50-20261029")
        raw = response.get("raw") or {}
        result.update({"returned_model": response.get("model"), "response_id": raw.get("id"), "usage": raw.get("usage") or response.get("usage") or {},
                       "finish_reason": response.get("finish_reason"), "response_text": response["content"]})
        if "deepseek" not in response.get("model", "").lower():
            raise ValueError("unexpected_model_identity")
        content = response["content"].strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        review = json.loads(content)
        invalid = core.validate_review(review, payload)
        result.update({"status": "reviewed" if response.get("finish_reason") != "length" else "truncated_response", "review": review, "invalid_citations": invalid})
    except Exception as error:
        result.update({"status": "failed", "error_code": getattr(error, "code", "parse_or_transport_error"), "error_type": type(error).__name__, "billing_unknown": "usage" not in result})
    result.update({"finished_at": core.now(), "elapsed_seconds": round(time.monotonic() - started, 3)})
    core.atomic_json(dest, result)
    return result


def price_estimate(result, model):
    usage = result.get("usage", {})
    p, o = usage.get("prompt_tokens", 0) or 0, usage.get("completion_tokens", 0) or 0
    if model == "luna":
        return core.token_cost(usage)
    cached = usage.get("prompt_cache_hit_tokens") or (usage.get("prompt_tokens_details") or {}).get("cached_tokens") or 0
    stamp = datetime.fromisoformat(result["started_at"])
    peak = stamp.weekday() < 5 and (1 <= stamp.hour < 4 or 6 <= stamp.hour < 10)
    factor = 2 if peak else 1
    return (max(0, p - cached) * .15 + cached * .003 + o * .6) / 1e6 * factor


def summarize(manifest, elapsed):
    pairs = []
    for item in manifest["projects"]:
        rid = str(item["repository_id"])
        luna_path = core.OUT / "results" / (rid + ".json")
        assert hashlib.sha256(luna_path.read_bytes()).hexdigest() == item["luna_receipt_sha256"]
        luna = json.loads(luna_path.read_text())
        ds_path = OUT / "deepseek" / (rid + ".json")
        ds = json.loads(ds_path.read_text()) if ds_path.exists() else {"status": "not_requested"}
        payload = json.loads((core.OUT / item["input_path"]).read_text())
        pairs.append({"repository_id": item["repository_id"], "domain": item["domain"], "repository_url": payload["card"]["github_url"],
                      "calibration": item["repository_id"] in manifest["calibration_ids"],
                      "luna": luna, "deepseek": ds,
                      "luna_citations": citation_metrics(luna, payload), "deepseek_citations": citation_metrics(ds, payload)})
    stats = {}
    for model in ("luna", "deepseek"):
        values = [p[model] for p in pairs]
        cite = Counter()
        for pair in pairs:
            cite.update(pair[model + "_citations"])
        stats[model] = {"statuses": dict(Counter(v["status"] for v in values)),
                        "verdicts": dict(Counter(v.get("review", {}).get("verdict", "no_verdict") for v in values)),
                        "projects_with_suggestions": sum(bool(v.get("review", {}).get("issues")) for v in values),
                        "suggestions": sum(len(v.get("review", {}).get("issues", [])) for v in values),
                        "tokens": {k: sum(v.get("usage", {}).get(k, 0) or 0 for v in values) for k in ("prompt_tokens", "completion_tokens", "total_tokens")},
                        "citation_counts": dict(cite), "estimated_token_list_price_usd": sum(price_estimate(v, model) for v in values if "usage" in v),
                        "mean_request_seconds": sum(v.get("elapsed_seconds", 0) for v in values) / len(values),
                        "billing_unknown_requests": sum(v.get("billing_unknown", False) for v in values),
                        "provider_reported_cost_usd": sum(v.get("usage", {}).get("cost", 0) or 0 for v in values),
                        "provider_reported_cost_receipts": sum(isinstance(v.get("usage", {}).get("cost"), (float, int)) for v in values),
                        "billing_sources": dict(Counter((v.get("usage", {}).get("opencode") or {}).get("billing_source", "not_reported") for v in values)),
                        "providers": dict(Counter(v.get("provider", "none") for v in values))}
    unchanged = True
    with core.readonly() as con:
        for item in manifest["projects"]:
            row = con.execute("SELECT data FROM oss_project WHERE repository_id=?", (item["repository_id"],)).fetchone()
            unchanged &= core.digest(row[0]) == item["project_data_sha256"]
        row = con.execute("SELECT data FROM oss_batch_job WHERE id=?", (core.JOB,)).fetchone()
        unchanged &= core.digest(row[0]) == manifest["production_job_sha256"]
    result = {"completed_at": core.now(), "pair_count": PAIR_COUNT, "domains": manifest["domains"], "stats": stats,
              "deepseek_wall_seconds": round(elapsed, 3), "same_input_and_prompt": True,
              "production_sample_and_job_unchanged": unchanged,
              "model_config_unchanged": hashlib.sha256(core.atlas_model.config_path().read_bytes()).hexdigest() == manifest["settings_sha256_before"],
              "luna_new_requests": 0, "full_run_started": False, "production_writes": False,
              "limits": ["Luna receipts reused from previous real run; latency was not measured simultaneously.", "DeepSeek estimates are token list value, not necessarily cash charges on subscription channels.", "Six known calibration cases are purposively included; do not extrapolate an overall error rate.", "Suggestion counts and pass rates alone do not establish quality. Source-based human adjudication follows.", "Strict citation mismatches are separated from whitespace-only differences."], "pairs": pairs}
    core.atomic_json(OUT / "RESULTS.json", result)
    print(core.canonical({k: result[k] for k in ("pair_count", "stats", "deepseek_wall_seconds", "production_sample_and_job_unchanged", "model_config_unchanged")}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    with (OUT / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        manifest = prepare()
        print(core.canonical({"prepared": True, "pairs": PAIR_COUNT, "domains": manifest["domains"], "new_luna_requests": 0}), flush=True)
        if not args.run:
            return
        started = time.monotonic()
        route_path = OUT / "ROUTE.json"
        if route_path.exists():
            route = json.loads(route_path.read_text())
        else:
            route = {"selected_provider": "open-design", "model": DS_MODEL, "selected_at": core.now()}
        first = manifest["projects"][0]
        first_result = deepseek_one(first, route["selected_provider"])
        if first_result.get("error_code") == "quota_exhausted" and route["selected_provider"] == "open-design":
            original = OUT / "deepseek" / (str(first["repository_id"]) + ".json")
            original.rename(original.with_name(original.stem + ".open-design-quota.json"))
            route = {"selected_provider": "opencode-go", "model": DS_MODEL, "reason": "fresh_open_design_quota_exhausted", "selected_at": core.now()}
            core.atomic_json(route_path, route)
            first_result = deepseek_one(first, route["selected_provider"])
        core.atomic_json(route_path, route)
        if first_result.get("error_code") in {"quota_exhausted", "authentication", "authentication_failed", "invalid_api_key", "unauthorized", "no_credential"}:
            core.atomic_json(OUT / "BLOCKED.json", {"at": core.now(), "provider": route["selected_provider"], "error_code": first_result["error_code"]})
            summarize(manifest, time.monotonic() - started)
            return
        done = 1
        stop = threading.Event()

        def bounded(item):
            if stop.is_set():
                return {"status": "not_requested"}
            result = deepseek_one(item, route["selected_provider"])
            if result.get("error_code") in {"quota_exhausted", "authentication", "authentication_failed", "invalid_api_key", "unauthorized", "no_credential"}:
                stop.set()
            return result

        with ThreadPoolExecutor(max_workers=4) as pool:
            for future in as_completed([pool.submit(bounded, item) for item in manifest["projects"][1:]]):
                future.result()
                done += 1
                if done % 10 == 0:
                    core.atomic_json(OUT / "PROGRESS.json", {"at": core.now(), "done": done, "total": PAIR_COUNT, "provider": route["selected_provider"], "stopped_on_provider_failure": stop.is_set()})
                    print(core.canonical({"deepseek_done": done, "total": PAIR_COUNT, "provider": route["selected_provider"]}), flush=True)
        summarize(manifest, time.monotonic() - started)


if __name__ == "__main__":
    main()
