"""Read-only, provenance-bounded enrichment for V1 batch reports."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


MAX_USAGE_EVENTS_PER_STAGE = 1000
MAX_USAGE_EVENTS_PER_REPORT = 5000
MAX_USAGE_RECORDS_PER_REPORT = 5000
MAX_USAGE_SOURCE_BYTES_PER_REPORT = 32 * 1024 * 1024
MAX_SUMMARY_BYTES = 1024 * 1024
MAX_EVENTS_BYTES = 8 * 1024 * 1024


def _ids(values):
    return sorted(set(value for value in values if isinstance(value, str) and value))


def _ratio(numerator_ids, denominator_ids):
    numerator_ids = _ids(numerator_ids)
    denominator_ids = _ids(denominator_ids)
    denominator_set = set(denominator_ids)
    numerator_ids = [item for item in numerator_ids if item in denominator_set]
    denominator = len(denominator_ids)
    numerator = len(numerator_ids)
    return {
        "numerator": numerator,
        "denominator": denominator,
        "ratio": numerator / denominator if denominator else None,
        "numerator_ids": numerator_ids,
        "denominator_ids": denominator_ids,
    }


def _safe_path(root, path, *, max_size=None):
    root = Path(root).resolve()
    path = Path(path)
    try:
        candidate = path if path.is_absolute() else root / path
        lexical = candidate.absolute().relative_to(root)
        current = root
        for part in lexical.parts:
            current = current / part
            if current.is_symlink():
                return None
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root)
        if not resolved.is_file() or (max_size is not None and resolved.stat().st_size > max_size):
            return None
        return resolved
    except (OSError, ValueError):
        return None


def _sha256(path):
    hasher = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def _read_bounded(root, path, tracker, *, per_file_limit):
    """Read and hash only bounded bytes; report prefix hashes when truncated."""
    resolved = _safe_path(root, path)
    if resolved is None:
        tracker["unsafe_files"] += 1
        return None
    try:
        size = resolved.stat().st_size
        allowance = min(per_file_limit, tracker["remaining_bytes"])
        if allowance <= 0:
            tracker["truncated"] = True
            return {"path": resolved, "data": b"", "sha256": None, "read_bytes": 0,
                    "truncated": True, "size": size, "hash_scope": "unavailable"}
        with resolved.open("rb") as stream:
            data = stream.read(allowance + 1)
        truncated = len(data) > allowance or size > allowance
        data = data[:allowance]
        tracker["remaining_bytes"] -= len(data)
        if truncated:
            tracker["truncated"] = True
        return {
            "path": resolved,
            "data": data,
            "sha256": hashlib.sha256(data).hexdigest(),
            "read_bytes": len(data),
            "truncated": truncated,
            "size": size,
            "hash_scope": "read_prefix" if truncated else "full_file",
        }
    except OSError:
        tracker["unsafe_files"] += 1
        return None


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def _identifier(value):
    return value if isinstance(value, str) and 0 < len(value) <= 256 else None


def _safe_usage_event(event):
    if not isinstance(event, dict):
        return None
    raw = event.get("reported_usage")
    if not isinstance(raw, dict):
        raw = {}
        if "cost" in event:
            raw["cost"] = event.get("cost")
        if "tokens" in event:
            raw["tokens"] = event.get("tokens")
    reported = {}
    if "cost" in raw:
        reported["cost"] = _number(raw.get("cost"))
    raw_tokens = raw.get("tokens")
    tokens = raw_tokens if isinstance(raw_tokens, dict) else {}
    clean_tokens = {}
    for key in ("input", "output", "reasoning"):
        if key in tokens:
            clean_tokens[key] = _number(tokens.get(key))
    raw_cache = tokens.get("cache")
    if isinstance(raw_cache, dict):
        clean_tokens["cache"] = {
            key: _number(raw_cache.get(key))
            for key in ("read", "write")
            if key in raw_cache
        }
    if "tokens" in raw:
        reported["tokens"] = clean_tokens
    normalized_cache = clean_tokens.get("cache", {})
    return {
        "event_type": "step_finish",
        "event_id": _identifier(event.get("event_id") or event.get("id")),
        "session_id": _identifier(event.get("session_id") or event.get("sessionID") or event.get("sessionId")),
        "message_id": _identifier(event.get("message_id") or event.get("messageID") or event.get("messageId")),
        "part_id": _identifier(event.get("part_id")),
        "step_id": _identifier(event.get("step_id")),
        "cost": _number(reported.get("cost")),
        "cost_currency": None,
        "tokens": {
            "input": clean_tokens.get("input"),
            "output": clean_tokens.get("output"),
            "reasoning": clean_tokens.get("reasoning"),
            "cache": {
                "read": normalized_cache.get("read"),
                "write": normalized_cache.get("write"),
            },
        },
        "reported_usage": reported,
    }


def _legacy_usage_events(events_path, root, tracker):
    read = _read_bounded(root, events_path, tracker, per_file_limit=MAX_EVENTS_BYTES)
    if read is None:
        return [], None, False, 0, "unavailable"
    if read["sha256"] is None:
        return [], None, True, read["read_bytes"], read["hash_scope"]
    raw = read["data"]
    truncated = read["truncated"]
    events = []
    from .cli import _usage_event

    for line in raw.splitlines():
        if len(events) >= min(MAX_USAGE_EVENTS_PER_STAGE, tracker["remaining_events"]):
            truncated = True
            tracker["truncated"] = True
            break
        try:
            event = json.loads(line)
        except (UnicodeError, ValueError):
            continue
        if isinstance(event, dict) and event.get("type") == "step_finish":
            part = event.get("part")
            event_record = _usage_event(event, part if isinstance(part, dict) else {})
            events.append(event_record)
            tracker["remaining_events"] -= 1
    return events, read["sha256"], truncated, read["read_bytes"], read["hash_scope"]


def _usage_stage(store, job, tracker):
    job_id, attempt = job.get("id"), job.get("attempt")
    if (
        not isinstance(job_id, str)
        or not job_id
        or Path(job_id).name != job_id
        or isinstance(attempt, bool)
        or not isinstance(attempt, int)
        or attempt < 1
    ):
        return []
    output = []
    for attempt_number in range(1, attempt + 1):
        attempt_root = Path(store.root) / "jobs" / job_id / f"attempt-{attempt_number}"
        try:
            if attempt_root.is_symlink() or not attempt_root.is_dir():
                continue
            # CLI creates one host-owned summary directly inside the stage
            # directory; never recurse into source archives or generated trees.
            summary_paths = sorted(attempt_root.glob("*/cli-summary.json"))
        except OSError:
            tracker["unsafe_files"] += 1
            continue
        for summary_candidate in summary_paths:
            if tracker["remaining_events"] <= 0 or tracker["remaining_bytes"] <= 0:
                tracker["truncated"] = True
                return output
            if tracker["remaining_records"] <= 0:
                tracker["truncated"] = True
                return output
            summary_read = _read_bounded(store.root, summary_candidate, tracker, per_file_limit=MAX_SUMMARY_BYTES)
            if summary_read is None:
                continue
            summary_path = summary_read["path"]
            summary_valid = True
            try:
                summary = json.loads(summary_read["data"].decode("utf-8"))
            except (UnicodeError, ValueError):
                summary = {}
                summary_valid = False
            if not isinstance(summary, dict):
                summary = {}
                summary_valid = False
            stage_directory = summary_path.parent
            stage_relative = stage_directory.relative_to(attempt_root).as_posix()
            events_present = isinstance(summary.get("usage_events"), list)
            truncated = summary_read["truncated"] or not summary_valid
            if events_present:
                raw_events = summary["usage_events"]
                event_limit = min(MAX_USAGE_EVENTS_PER_STAGE, tracker["remaining_events"])
                events = [_safe_usage_event(item) for item in raw_events[:event_limit]]
                events = [item for item in events if item is not None]
                tracker["remaining_events"] -= len(events)
                truncated |= bool(summary.get("usage_events_truncated")) or len(raw_events) > event_limit
                usage_source_path = summary_path
                usage_source_hash = summary_read["sha256"]
                usage_hash_scope = summary_read["hash_scope"]
                usage_source_bytes = summary_read["read_bytes"]
                source_kind = "cli-summary"
            else:
                legacy_path = stage_directory / "events.jsonl"
                legacy, legacy_hash, legacy_truncated, event_bytes, hash_scope = _legacy_usage_events(legacy_path, store.root, tracker)
                events = [_safe_usage_event(item) for item in legacy]
                events = [item for item in events if item is not None]
                truncated |= legacy_truncated
                usage_source_path = legacy_path if legacy_hash else summary_path
                usage_source_hash = legacy_hash or summary_read["sha256"]
                usage_hash_scope = hash_scope if legacy_hash else summary_read["hash_scope"]
                usage_source_bytes = event_bytes if legacy_hash else summary_read["read_bytes"]
                source_kind = "events.jsonl" if legacy_hash else "cli-summary-missing-usage"
            tracker["truncated"] |= truncated
            tracker["remaining_records"] -= 1
            output.append({
                "job_id": job_id,
                "job_kind": job.get("kind"),
                "job_state": job.get("state"),
                "attempt": attempt_number,
                "stage": stage_relative,
                "exit_code": summary.get("exit_code") if type(summary.get("exit_code")) is int else None,
                "cli_status": summary.get("cli_status") if isinstance(summary.get("cli_status"), str) and summary["cli_status"] in {"completed", "interrupted", "not_started", "failed"} else None,
                "delivery_status": summary.get("delivery_status") if isinstance(summary.get("delivery_status"), str) and summary["delivery_status"] in {"delivered", "failed", "unverified"} else None,
                "failure_code": _identifier(summary.get("failure_code")),
                "summary_path": summary_path.relative_to(store.root).as_posix(),
                "summary_sha256": summary_read["sha256"],
                "summary_hash_scope": summary_read["hash_scope"],
                "usage_source": source_kind,
                "usage_source_path": usage_source_path.relative_to(store.root).as_posix(),
                "usage_source_sha256": usage_source_hash,
                "usage_hash_scope": usage_hash_scope,
                "usage_source_bytes_read": usage_source_bytes,
                "requested_model": _identifier(summary.get("requested_model") or summary.get("model")),
                "observed_model": _identifier(summary.get("observed_model") or summary.get("actual_model")),
                "requested_reasoning_effort": _identifier(summary.get("requested_effort") or summary.get("reasoning_effort")),
                "observed_reasoning_effort": _identifier(summary.get("observed_effort") or summary.get("actual_reasoning_effort")),
                "usage_events": events,
                "usage_events_truncated": truncated,
                "cost_currency": None,
                "provider_requests": None,
            })
    return output


def _case_record(con, case_id, revision):
    row = con.execute(
        "SELECT c.body,c.digest,c.app_id,c.created_at,a.created_at AS app_created_at "
        "FROM case_revision c JOIN case_app a ON a.app_id=c.app_id "
        "WHERE c.case_id=? AND c.revision=?",
        (case_id, revision),
    ).fetchone()
    if not row:
        return None
    body = json.loads(row["body"])
    observations = [
        json.loads(item[0]) for item in con.execute(
            "SELECT body FROM evidence_observation WHERE case_id=? AND revision=? ORDER BY evidence_id",
            (case_id, revision),
        )
    ]
    links = [
        json.loads(item[0]) for item in con.execute(
            "SELECT body FROM scenario_case_link WHERE case_id=? AND case_revision=? ORDER BY scenario_id,scenario_revision",
            (case_id, revision),
        )
    ]
    snapshot_ids = body.get("snapshot_ids", []) if isinstance(body.get("snapshot_ids"), list) else []
    snapshots = []
    if snapshot_ids:
        placeholders = ",".join("?" for _ in snapshot_ids)
        snapshots = [dict(item) for item in con.execute(
            f"SELECT snapshot_id,repository,commit_sha,digest,created_at,body FROM source_snapshot WHERE snapshot_id IN ({placeholders})",
            snapshot_ids,
        )]
    return {
        "case_id": case_id,
        "revision": revision,
        "digest": row["digest"],
        "app_id": row["app_id"],
        "created_at": row["created_at"],
        "app_created_at": row["app_created_at"],
        "created_task_id": body.get("created_task_id"),
        "snapshot_ids": _ids(snapshot_ids),
        "observations": observations,
        "scenario_links": links,
        "snapshots": snapshots,
    }


def _file_verified(store, relative_path, expected_hash):
    if not isinstance(relative_path, str) or not isinstance(expected_hash, str):
        return False
    candidate = Path(relative_path)
    if candidate.is_absolute():
        return False
    resolved = _safe_path(store.root, Path(store.root) / candidate)
    return bool(resolved and _sha256(resolved) == expected_hash)


def enrich_report(store, report):
    """Return supplemental persisted evidence without mutating report or state."""
    if not isinstance(report, dict) or not isinstance(report.get("plan"), dict):
        return {"schema": "atlas.batch-report-enrichment.v1", "status": "unavailable", "reason": "plan_missing"}
    plan = report["plan"]
    plan_id = plan.get("id")
    if not isinstance(plan_id, str) or not plan_id:
        return {"schema": "atlas.batch-report-enrichment.v1", "status": "unavailable", "reason": "plan_id_missing"}

    with store.connect() as con:
        job_rows = list(con.execute(
            "SELECT * FROM job WHERE json_extract(snapshot,'$.v1.plan_id')=? ORDER BY created_at,rowid",
            (plan_id,),
        ))
        jobs = []
        checkpoints = {}
        for row in job_rows:
            job = store._job(row)
            jobs.append(job)
            checkpoints[job["id"]] = {
                item["name"]: json.loads(item["body"])
                for item in con.execute(
                    "SELECT name,body FROM checkpoint WHERE job_id=?",
                    (job["id"],),
                )
            }

        research_jobs = [job for job in jobs if job.get("kind") == "case-research"]
        research_ids = {job["id"] for job in research_jobs}
        new_case_keys = set()
        if research_ids:
            placeholders = ",".join("?" for _ in research_ids)
            research_rows = con.execute(
                "SELECT case_id,revision,body FROM case_revision "
                f"WHERE json_extract(body,'$.research.task_id') IN ({placeholders})",
                sorted(research_ids),
            )
            plan_scenarios = {
                (seed.get("scenario", {}).get("id"), seed.get("scenario", {}).get("revision"))
                for seed in plan.get("seeds", []) if isinstance(seed, dict)
            }
            for item in research_rows:
                links = [json.loads(link[0]) for link in con.execute(
                    "SELECT body FROM scenario_case_link WHERE case_id=? AND case_revision=?",
                    (item["case_id"], item["revision"]),
                )]
                if any((link.get("scenario_id"), link.get("scenario_revision")) in plan_scenarios for link in links):
                    new_case_keys.add((item["case_id"], item["revision"]))

        reused_case_keys = set()
        for seed in plan.get("seeds", []):
            basis = seed.get("case_basis") if isinstance(seed, dict) else None
            if isinstance(basis, dict):
                for ref in basis.get("case_refs", []):
                    if isinstance(ref, dict) and isinstance(ref.get("case_id"), str) and isinstance(ref.get("revision"), int):
                        reused_case_keys.add((ref["case_id"], ref["revision"]))
        all_case_keys = new_case_keys | reused_case_keys
        case_records = []
        for case_id, revision in sorted(all_case_keys):
            record = _case_record(con, case_id, revision)
            if record:
                record["increment_origin"] = "research_job" if (case_id, revision) in new_case_keys else "plan_case_basis"
                case_records.append(record)

        acceptance_rows = []
        artifact_ids = [artifact.get("id") for artifact in report.get("artifacts", []) if isinstance(artifact, dict) and artifact.get("id")]
        if artifact_ids:
            placeholders = ",".join("?" for _ in artifact_ids)
            acceptance_rows = list(con.execute(
                f"SELECT id,artifact_id,digest,method,job_id,body FROM acceptance WHERE artifact_id IN ({placeholders}) AND method='blueprint-runtime' ORDER BY created_at,rowid",
                artifact_ids,
            ))

    # Each app’s catalog timestamp establishes existence before plan creation;
    # later creation has no creator field and is therefore conservatively unknown.
    app_ids = _ids(record["app_id"] for record in case_records)
    app_created = {}
    if app_ids:
        placeholders = ",".join("?" for _ in app_ids)
        with store.connect() as con:
            app_created = {
                row["app_id"]: row["created_at"]
                for row in con.execute(
                    f"SELECT app_id,created_at FROM case_app WHERE app_id IN ({placeholders})",
                    app_ids,
                )
            }
    plan_created = plan.get("created_at")
    reused_apps = _ids(app_id for app_id in app_ids if isinstance(plan_created, str) and app_created.get(app_id, "") <= plan_created)
    unknown_apps = _ids(app_id for app_id in app_ids if app_id not in set(reused_apps))
    snapshot_records = {}
    for record in case_records:
        for snapshot in record["snapshots"]:
            body = json.loads(snapshot["body"])
            snapshot_records[snapshot["snapshot_id"]] = {
                "snapshot_id": snapshot["snapshot_id"],
                "repository": snapshot["repository"],
                "commit_sha": snapshot["commit_sha"],
                "digest": snapshot["digest"],
                "file_manifest_digest": body.get("file_manifest_digest"),
                "file_count": len(body.get("files", {})) if isinstance(body.get("files"), dict) else None,
                "created_at": snapshot["created_at"],
            }
    reused_snapshots = _ids(
        snapshot_id for snapshot_id, item in snapshot_records.items()
        if isinstance(plan_created, str) and item["created_at"] <= plan_created
    )
    unknown_snapshots = _ids(snapshot_id for snapshot_id in snapshot_records if snapshot_id not in set(reused_snapshots))

    observations = {kind: [] for kind in ("documentation", "code_observation", "inference", "runtime_verification")}
    upstream_runtime = []
    for record in case_records:
        for item in record["observations"]:
            kind = item.get("kind")
            if kind not in observations:
                continue
            safe_item = {"evidence_id": item.get("evidence_id"), "case_id": record["case_id"], "case_revision": record["revision"]}
            observations[kind].append(safe_item)
            if kind == "runtime_verification":
                location = item.get("location") if isinstance(item.get("location"), dict) else {}
                run_id = location.get("verification_run_id")
                assertion_id = location.get("assertion_id")
                if isinstance(run_id, str) and isinstance(assertion_id, str):
                    with store.connect() as con:
                        runtime = con.execute("SELECT body FROM acceptance WHERE id=?", (run_id,)).fetchone()
                    runtime_body = json.loads(runtime[0]) if runtime else {}
                    if runtime_body.get("target_kind") == "upstream_case" and assertion_id in runtime_body.get("assertion_ids", []):
                        upstream_runtime.append({**safe_item, "run_id": run_id, "assertion_id": assertion_id, "target_kind": "upstream_case"})

    downstream_runtime = []
    blocked_external_ids = set(job["id"] for job in jobs if job.get("state") == "blocked_external")
    for row in acceptance_rows:
        runtime = json.loads(row["body"])
        binding = runtime.get("target_binding") if isinstance(runtime.get("target_binding"), dict) else {}
        if binding.get("target_kind") != "generated_application":
            continue
        target = {
            "artifact_id": row["artifact_id"],
            "artifact_digest": row["digest"],
            "run_id": row["id"],
            "job_id": row["job_id"],
            "target_kind": "generated_application",
            "selected_phase": runtime.get("selected_phase"),
            "phase_status": runtime.get("phase_status"),
            "outcome": runtime.get("outcome"),
            "application_digest": binding.get("application_digest"),
        }
        downstream_runtime.append(target)
        if runtime.get("outcome") == "blocked_external" or runtime.get("phase_status") == "blocked_external":
            blocked_external_ids.add(row["job_id"])

    actual_product_ids = _ids(seed.get("product_id") for seed in plan.get("seeds", []) if isinstance(seed, dict))
    products = report.get("products") if isinstance(report.get("products"), dict) else {}
    reviewed_ids = [product_id for product_id in actual_product_ids if products.get(product_id, {}).get("reviewed") is True]
    catalog_ids = [product_id for product_id in actual_product_ids if products.get(product_id, {}).get("published") is True]
    sample_seeds = [seed for seed in plan.get("seeds", []) if isinstance(seed, dict) and seed.get("runtime_sample")]
    sample_ids = _ids(seed.get("scenario", {}).get("id") for seed in sample_seeds if isinstance(seed.get("scenario"), dict))
    sample_passed_ids = _ids(
        seed.get("scenario", {}).get("id") for seed in sample_seeds
        if isinstance(seed.get("scenario"), dict) and products.get(seed.get("product_id"), {}).get("p0_runtime") is True
    )
    completed_job_ids = _ids(job["id"] for job in jobs if job.get("state") == "completed")
    all_job_ids = _ids(job.get("id") for job in jobs)

    repairs = _ids(job["id"] for job in jobs if job.get("kind") == "application-development" and job.get("snapshot", {}).get("repair_of"))
    failure_ids = _ids(job["id"] for job in jobs if job.get("state") in {"failed", "interrupted", "needs_review"})
    paused_budget_ids = _ids(job["id"] for job in jobs if job.get("state") == "paused_budget")

    first_success_ids = []
    for job in jobs:
        snapshot = job.get("snapshot") if isinstance(job.get("snapshot"), dict) else {}
        if job.get("kind") != "application-development" or snapshot.get("repair_of") is not None or job.get("state") != "completed":
            continue
        delivery = checkpoints.get(job["id"], {}).get("application-delivery")
        delivery = delivery.get("result") if isinstance(delivery, dict) and isinstance(delivery.get("result"), dict) else delivery
        if isinstance(delivery, dict) and _file_verified(store, delivery.get("archive_path"), delivery.get("archive_sha256")):
            first_success_ids.append(job["id"])
    first_success_ids = _ids(first_success_ids)

    usage_stages = []
    usage_tracker = {
        "remaining_events": MAX_USAGE_EVENTS_PER_REPORT,
        "remaining_records": MAX_USAGE_RECORDS_PER_REPORT,
        "remaining_bytes": MAX_USAGE_SOURCE_BYTES_PER_REPORT,
        "truncated": False,
        "unsafe_files": 0,
    }
    for job in jobs:
        usage_stages.extend(_usage_stage(store, job, usage_tracker))
        if usage_tracker["remaining_records"] <= 0 or usage_tracker["remaining_bytes"] <= 0:
            usage_tracker["truncated"] = True
            break
    usage_stages.sort(key=lambda item: (item["job_id"], item["attempt"], item["stage"]))

    return {
        "schema": "atlas.batch-report-enrichment.v1",
        "status": "available",
        "source_plan_id": plan_id,
        "source_plan_digest": plan.get("digest"),
        "application_evidence_increment": {
            "product_denominator": {"count": len(actual_product_ids), "product_ids": actual_product_ids},
            "research_job_ids": _ids(job.get("id") for job in research_jobs),
            "research_completed_job_ids": _ids(job["id"] for job in research_jobs if job.get("state") == "completed"),
            "research_unresolved_product_ids": _ids(
                seed.get("product_id") for seed in plan.get("seeds", [])
                if isinstance(seed, dict) and not seed.get("case_basis")
                and not any(record.get("created_task_id") in research_ids and any(link.get("scenario_id") == seed.get("scenario", {}).get("id") and link.get("scenario_revision") == seed.get("scenario", {}).get("revision") for link in record.get("scenario_links", [])) for record in case_records)
            ),
            "new_case_revisions": [
                {"case_id": record["case_id"], "revision": record["revision"], "created_task_id": record["created_task_id"], "app_id": record["app_id"]}
                for record in case_records if record["increment_origin"] == "research_job"
            ],
            "reused_case_revisions": [
                {"case_id": record["case_id"], "revision": record["revision"], "app_id": record["app_id"]}
                for record in case_records if record["increment_origin"] == "plan_case_basis"
            ],
            "apps": {
                "denominator": len(app_ids),
                "app_ids": app_ids,
                "reused_app_ids": reused_apps,
                "new_app_ids": [],
                "classification_unknown_app_ids": unknown_apps,
                "new_classification": "unknown when app creation lacks a persisted creator/baseline record",
            },
            "source_snapshots": {
                "denominator": len(snapshot_records),
                "snapshot_ids": sorted(snapshot_records),
                "records": [snapshot_records[key] for key in sorted(snapshot_records)],
                "reused_before_plan_ids": reused_snapshots,
                "new_or_unattributed_after_plan_ids": unknown_snapshots,
            },
            "scene_links": [
                {"scenario_id": link.get("scenario_id"), "scenario_revision": link.get("scenario_revision"), "case_id": record["case_id"], "case_revision": record["revision"], "evidence_ids": _ids(link.get("evidence_ids", []))}
                for record in case_records for link in record["scenario_links"]
            ],
            "observation_kinds": {
                key: {"count": len(value), "items": value}
                for key, value in observations.items()
            },
            "runtime_evidence": {
                "upstream_case_observations": upstream_runtime,
                "downstream_generated_applications": downstream_runtime,
            },
        },
        "ratios": {
            "queue_completion": _ratio(completed_job_ids, all_job_ids),
            "product_reviewed": _ratio(reviewed_ids, actual_product_ids),
            "product_catalog_eligible": _ratio(catalog_ids, actual_product_ids),
            "runtime_sample_passed": _ratio(sample_passed_ids, sample_ids),
        },
        "job_outcomes": {
            "jobs_total": len(all_job_ids),
            "repair_job_ids": repairs,
            "first_success_job_ids": first_success_ids,
            "failure_job_ids": failure_ids,
            "paused_budget_job_ids": paused_budget_ids,
            "blocked_external_job_ids": _ids(blocked_external_ids),
        },
        "usage": {
            "provider_requests": None,
            "provider_requests_reason": "CLI step events do not establish provider HTTP request counts.",
            "cost_currency": None,
            "cost_currency_reason": "OpenCode step_finish events report cost without a currency field.",
            "token_aggregation": "per-step raw fields only; step totals may overlap and are not summed",
            "truncated": usage_tracker["truncated"],
            "record_limit": MAX_USAGE_RECORDS_PER_REPORT,
            "read_byte_limit": MAX_USAGE_SOURCE_BYTES_PER_REPORT,
            "unsafe_files_skipped": usage_tracker["unsafe_files"],
            "stages": usage_stages,
        },
    }
