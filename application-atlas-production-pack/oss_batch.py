"""Persistent, resumable batch jobs. Each frozen candidate is attempted once per job."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import os
import re
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from contextlib import nullcontext

from atlas_runtime import atomic_json
from oss_catalog import AUTO_LEAVES, CatalogError, CatalogStore, ServiceUnavailable, WorkflowInterrupted, canonical, digest, now, validate_leaf
from oss_discovery import ROOT
from oss_workflow import context_for, discover_open_leaf, prepare_leaf, read_candidate_sources
from oss_priority import VERSION as PRIORITY_VERSION, select_first_round

RECOVERY_BASE_SECONDS = 60
RECOVERY_MAX_SECONDS = 900
_WAKEUPS = {}
_WAKEUPS_LOCK = threading.Lock()
LEGACY_INTERRUPTION_REASON = "本批中断，进度已保存"


class BatchJobs:
    def __init__(self, store, worker=None, preparer=None, *, clock=None, waiter=None, prefetcher=None):
        self.store = store
        self.worker = worker or discover_open_leaf
        self.preparer = preparer or prepare_leaf
        self.clock = clock or time.time
        self.wake = threading.Event()
        self.waiter = waiter or self.wake.wait
        self.prefetcher = prefetcher or (read_candidate_sources if worker is None else None)

    def save(self, job):
        job["updated_at"] = now()
        job["heartbeat_at"] = job["updated_at"]
        payload = {**job, "targets": {}} if job.get("storage_version") == 2 else job
        with self.store.connect() as con:
            con.execute("INSERT INTO oss_batch_job VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET status=excluded.status,data=excluded.data",
                        (job["id"], job["status"], canonical(payload)))
        atomic_json(ROOT / "batches" / (job["id"] + ".json"), payload)

    def get(self, identifier, detect_interruption=True, include_targets=True):
        with self.store.connect() as con:
            row = con.execute("SELECT data FROM oss_batch_job WHERE id=?", (identifier,)).fetchone()
        if not row:
            raise CatalogError("批量任务不存在", 404)
        job = json.loads(row[0])
        if job.get("storage_version") == 2:
            self.load_ledger(job, include_targets)
        if detect_interruption and job["status"] in {"running", "retry_wait"}:
            try:
                lock = self.store._lock()
            except CatalogError:
                return job if include_targets else {**job, "targets": {}}
            try:
                job["status"] = "interrupted"
                self.save(job)
            finally:
                lock.close()
        return job if include_targets else {**job, "targets": {}}

    def list(self):
        with self.store.connect() as con:
            ids = [r[0] for r in con.execute("SELECT id FROM oss_batch_job ORDER BY rowid DESC LIMIT 30")]
        return [self.get(identifier, include_targets=False) for identifier in ids]

    def create(self, leaves, existing_only=False, batch_size=16, search_pages=1, background=False, auto_recovery=True,
               first_round_limit=None, pilot_size=0):
        if not isinstance(leaves, list) or not leaves:
            raise CatalogError("请指定至少一个现有叶子")
        leaves = list(dict.fromkeys(validate_leaf(leaf) for leaf in leaves))
        if type(auto_recovery) is not bool or type(existing_only) is not bool or type(batch_size) is not int or not 1 <= batch_size <= 100 or type(search_pages) is not int or not 1 <= search_pages <= 10:
            raise CatalogError("批量参数无效；batch_size 为 1–100，search_pages 为 1–10")
        if first_round_limit is not None and (type(first_round_limit) is not int or not 1 <= first_round_limit <= 100):
            raise CatalogError("首轮每叶候选数应为 1–100")
        if type(pilot_size) is not int or pilot_size < 0 or pilot_size > len(leaves) or pilot_size and first_round_limit is None:
            raise CatalogError("试跑叶子数无效，试跑仅用于首轮覆盖任务")
        lock = self.store._lock()
        with self.store.connect() as con:
            awaiting = con.execute("SELECT id FROM oss_batch_job WHERE status='awaiting_acceptance' LIMIT 1").fetchone()
        if awaiting:
            lock.close()
            raise CatalogError("已有首轮试跑等待实际验收，请先完成原任务验收", 409)
        job = {"id": "batch_" + uuid.uuid4().hex, "status": "running", "created_at": now(),
               "leaves": leaves, "existing_only": existing_only, "auto_recovery": auto_recovery, "batch_size": batch_size, "search_pages": search_pages,
               "targets": {}, "prepared": [], "leaf_errors": {}, "runs": [], "errors": [], "processed": 0, "total": 0}
        if first_round_limit is not None:
            job.update(storage_version=2, scope="first_round", first_round_limit=first_round_limit,
                       source_policy="essential", source_pipeline=True, priority_version=PRIORITY_VERSION,
                       completed_leaves=[], deferred_counts={}, candidate_totals={}, checkpoints=[],
                       pilot={"size": pilot_size, "status": "pending" if pilot_size else "not_required"})
        if existing_only and first_round_limit is None:
            for leaf in leaves:
                job["targets"][leaf] = [{"repository_id": c["repository_id"], "full_name": c["data"]["meta"]["full_name"], "status": "pending"}
                                        for c in self.store.candidates(leaf) if c["status"] in {"pending", "needs_evidence", "failed"}]
            job["total"] = sum(len(items) for items in job["targets"].values())
        try:
            self.save(job)
            return self.launch(job, lock, background)
        except BaseException:
            lock.close()
            raise

    def load_ledger(self, job, include_targets=True):
        with self.store.connect() as con:
            leaves = con.execute("SELECT * FROM oss_batch_leaf WHERE job_id=? ORDER BY position", (job["id"],)).fetchall()
            counts = dict(con.execute("SELECT status,COUNT(*) FROM oss_batch_target WHERE job_id=? GROUP BY status", (job["id"],)))
            if include_targets:
                job["targets"] = {}
                for row in con.execute("SELECT * FROM oss_batch_target WHERE job_id=? ORDER BY leaf,rowid", (job["id"],)):
                    item = {k: row[k] for k in ("repository_id", "full_name", "status", "reason", "finished_at")}
                    item["priority"] = json.loads(row["priority"])
                    job["targets"].setdefault(row["leaf"], []).append(item)
        job["prepared"] = [r["leaf"] for r in leaves]
        job["completed_leaves"] = [r["leaf"] for r in leaves if r["state"] in {"first_round_done", "failed"}]
        job["candidate_totals"] = {r["leaf"]: r["candidate_total"] for r in leaves}
        job["deferred_counts"] = {r["leaf"]: r["deferred_count"] for r in leaves}
        for row in leaves:
            if include_targets:
                job["targets"].setdefault(row["leaf"], [])
        job["total"] = sum(counts.values())
        job["processed"] = sum(n for state, n in counts.items() if state not in {"pending", "running"})
        job["target_counts"] = counts
        job["deferred_total"] = sum(job["deferred_counts"].values())

    def freeze_first_round(self, job, leaf, candidates):
        selected = select_first_round(candidates, self.store.scenarios(leaf), context_for(leaf).splitlines()[0], job["first_round_limit"])
        with self.store.connect() as con:
            existing = con.execute("SELECT 1 FROM oss_batch_leaf WHERE job_id=? AND leaf=?", (job["id"], leaf)).fetchone()
            if not existing:
                con.execute("INSERT INTO oss_batch_leaf VALUES (?,?,?,?,?,?,?,?)", (
                    job["id"], leaf, job["leaves"].index(leaf), len(selected), len(candidates), len(candidates) - len(selected),
                    "prepared", canonical({"priority_version": PRIORITY_VERSION, "selected_at": now()})))
                for item in selected:
                    con.execute("INSERT INTO oss_batch_target VALUES (?,?,?,?,?,?,?,?)", (
                        job["id"], leaf, item["repository_id"], item["data"]["meta"]["full_name"], "pending", None,
                        canonical(item["priority"]), None))
        self.load_ledger(job, include_targets=False)
        with self.store.connect() as con:
            rows = con.execute("SELECT * FROM oss_batch_target WHERE job_id=? AND leaf=? ORDER BY rowid", (job["id"], leaf)).fetchall()
        job["targets"][leaf] = [{**{k: r[k] for k in ("repository_id", "full_name", "status", "reason", "finished_at")},
                                  "priority": json.loads(r["priority"])} for r in rows]

    def resume(self, identifier, background=False, automatic=False):
        if not automatic:
            with _WAKEUPS_LOCK:
                wake = _WAKEUPS.get(identifier)
                if wake and self.get(identifier, detect_interruption=False)["status"] == "retry_wait":
                    wake.set()
                    return self.get(identifier, detect_interruption=False)
        lock = self.store._lock()
        try:
            job = self.get(identifier, detect_interruption=False)
            if job["status"] == "awaiting_acceptance":
                raise CatalogError("试跑已结束，实际验收通过后自动续跑", 409)
            if not automatic or job.get("auto_recovery"):
                self.restore_interrupted_targets(job)
            if job["status"] in {"completed", "partial"}:
                lock.close()
                return job
            if automatic and (not job.get("auto_recovery") or job["status"] not in {"running", "retry_wait", "interrupted"}):
                lock.close()
                return job
            job["status"] = "retry_wait" if automatic and job.get("recovery", {}).get("next_retry_at") else "running"
            if not automatic:
                job.get("recovery", {}).pop("next_retry_at", None)
            job.pop("finished_at", None)
            job["resumed_at"] = now()
            job.pop("pause_reason", None)
            self.save(job)
            return self.launch(job, lock, background)
        except BaseException:
            lock.close()
            raise

    @staticmethod
    def interrupted_targets(job):
        # Only the old coordinator-abort marker qualifies. Ordinary per-project
        # failures and completed partial cards remain terminal for this job.
        if job["status"] != "partial":
            return []
        return [(leaf, item) for leaf, items in job.get("targets", {}).items() for item in items
                if item["status"] == "failed" and item.get("reason") == LEGACY_INTERRUPTION_REASON]

    def restore_interrupted_targets(self, job):
        targets = self.interrupted_targets(job)
        if not targets:
            return
        restored_at = now()
        job.setdefault("restored_interruptions", []).append({
            "restored_at": restored_at, "previous_finished_at": job.get("finished_at"),
            "reason": LEGACY_INTERRUPTION_REASON,
            "targets": [{"leaf": leaf, "repository_id": item["repository_id"]} for leaf, item in targets]})
        for _, item in targets:
            item.update(status="pending", reason="恢复上次批处理中断，等待重新处理")
            item.pop("finished_at", None)
        if job.get("storage_version") == 2:
            with self.store.connect() as con:
                con.executemany("UPDATE oss_batch_target SET status='pending',reason=?,finished_at=NULL WHERE job_id=? AND leaf=? AND repository_id=?", (
                    ("恢复上次批处理中断，等待重新处理", job["id"], leaf, item["repository_id"]) for leaf, item in targets))
        resolved = [e for e in job["errors"] if e.get("error") == LEGACY_INTERRUPTION_REASON]
        job.setdefault("resolved_errors", []).extend({**e, "resolved_at": restored_at} for e in resolved)
        job["errors"] = [e for e in job["errors"] if e.get("error") != LEGACY_INTERRUPTION_REASON]
        job["processed"] = sum(i["status"] not in {"pending", "running"} for items in job["targets"].values() for i in items)
        job["status"] = "interrupted"

    def launch(self, job, lock, background):
        if background:
            threading.Thread(target=self.execute, args=(job, lock), name=job["id"], daemon=True).start()
            return dict(job)
        return self.execute(job, lock)

    def recovery_succeeded(self, job):
        recovery = job.get("recovery")
        if recovery and recovery.get("consecutive_failures"):
            recovery.update(consecutive_failures=0, last_recovered_at=now())
            recovery.pop("next_retry_at", None)
            job.pop("pause_reason", None)

    def schedule_recovery(self, job, error):
        recovery = job.setdefault("recovery", {})
        failures = recovery.get("consecutive_failures", 0) + 1
        delay = max(min(RECOVERY_MAX_SECONDS, RECOVERY_BASE_SECONDS * 2 ** min(failures - 1, 10)), error.retry_after or 0)
        next_retry = datetime.fromtimestamp(self.clock() + delay, timezone.utc).isoformat()
        recovery.update(consecutive_failures=failures, cycles=recovery.get("cycles", 0) + 1,
                        next_retry_at=next_retry, delay_seconds=delay, last_error=str(error),
                        code=error.code, upstream_status=error.upstream_status)
        recovery["component"] = error.component
        recovery.setdefault("history", []).append({"at": now(), "next_retry_at": next_retry,
                                                   "delay_seconds": delay, "code": error.code,
                                                   "upstream_status": error.upstream_status, "error": str(error)})
        recovery["history"] = recovery["history"][-100:]
        job.update(status="retry_wait", pause_reason=str(error))
        self.save(job)

    def wait_for_recovery(self, job):
        deadline = datetime.fromisoformat(job["recovery"]["next_retry_at"]).timestamp()
        while not self.wake.is_set():
            remaining = deadline - self.clock()
            if remaining <= 0:
                break
            self.waiter(min(15, remaining))
            self.save(job)
        self.wake.clear()
        job["recovery"].pop("next_retry_at", None)
        job.update(status="running", resumed_at=now())
        job.pop("pause_reason", None)
        self.save(job)

    def execute(self, job, lock):
        with _WAKEUPS_LOCK:
            _WAKEUPS[job["id"]] = self.wake
        try:
            with self.store.connect() as con:
                for row in con.execute("SELECT data FROM oss_run WHERE status='running'").fetchall():
                    run = json.loads(row[0])
                    run.update(status="interrupted", finished_at=now())
                    con.execute("UPDATE oss_run SET status=?,data=? WHERE id=?", (run["status"], canonical(run), run["id"]))
            while True:
                if job.get("recovery", {}).get("next_retry_at"):
                    self.wait_for_recovery(job)
                try:
                    self.execute_pass(job)
                    break
                except ServiceUnavailable as error:
                    if job.get("auto_recovery", False) and error.retryable:
                        self.schedule_recovery(job, error)
                        continue
                    job.update(status="paused_model", pause_reason=str(error))
                    break
        except BaseException:
            job["status"] = "interrupted"
            raise
        finally:
            with _WAKEUPS_LOCK:
                if _WAKEUPS.get(job["id"]) is self.wake:
                    _WAKEUPS.pop(job["id"], None)
            try:
                self.save(job)
            finally:
                lock.close()
        return job

    def execute_pass(self, job):
        if self.pilot_waits(job):
            return
        for leaf in job["leaves"]:
            if job.get("storage_version") == 2 and leaf in job.get("completed_leaves", []):
                continue
            job["current_leaf"] = leaf
            if leaf not in job["prepared"]:
                prep = self.new_run(leaf)
                prep["source_policy"] = job.get("source_policy", "full")
                self.store._save_run(prep)
                try:
                    self.preparer(self.store, leaf, prep, search=not job["existing_only"], search_pages=job["search_pages"])
                except ServiceUnavailable as error:
                    prep.update(status="paused_model", finished_at=now())
                    prep["errors"].append({"error": str(error)})
                    self.store._save_run(prep)
                    job["runs"].append(prep["id"])
                    raise
                except Exception as error:
                    reason = str(error) if isinstance(error, CatalogError) else "叶子准备失败，已跳过并保留记录"
                    job["leaf_errors"][leaf] = reason
                    job["errors"].append({"leaf": leaf, "error": reason})
                job["errors"].extend({"leaf": leaf, **error} for error in prep.get("errors", []))
                prep.update(status="failed" if leaf in job["leaf_errors"] else "partial" if prep["errors"] else "completed", finished_at=now())
                self.store._save_run(prep)
                job["runs"].append(prep["id"])
                if leaf not in job["targets"]:
                    targets = [c for c in self.store.candidates(leaf) if c["status"] in {"pending", "needs_evidence", "failed"}]
                    if job.get("storage_version") == 2:
                        self.freeze_first_round(job, leaf, targets)
                    else:
                        job["targets"][leaf] = [{"repository_id": c["repository_id"], "full_name": c["data"]["meta"]["full_name"], "status": "pending"} for c in targets]
                self.recovery_succeeded(job)
                if leaf not in job["prepared"]:
                    job["prepared"].append(leaf)
                if job.get("storage_version") != 2:
                    job["total"] = sum(len(items) for items in job["targets"].values())
                self.save(job)
            items = job["targets"][leaf]
            remaining = [item for item in items if item["status"] in {"pending", "running"}]
            self.execute_groups(job, leaf, remaining)
            if job.get("storage_version") == 2:
                with self.store.connect() as con:
                    con.execute("UPDATE oss_batch_leaf SET state=? WHERE job_id=? AND leaf=?", (
                        "failed" if leaf in job["leaf_errors"] else "first_round_done", job["id"], leaf))
                self.load_ledger(job, include_targets=False)
                count = len(job["completed_leaves"])
                if (count % 100 == 0 or count == job.get("pilot", {}).get("size")) and not any(c["completed_leaves"] == count for c in job["checkpoints"]):
                    job["checkpoints"].append({"completed_leaves": count, "processed": job["processed"],
                                               "deferred_total": job["deferred_total"], "at": now()})
                self.save(job)
                if self.pilot_waits(job):
                    return
        job["status"] = "partial" if job["errors"] or job["leaf_errors"] or any(i["status"] == "failed" for entries in job["targets"].values() for i in entries) else "completed"
        job["finished_at"] = now()

    def pilot_waits(self, job):
        pilot = job.get("pilot", {})
        if pilot.get("size") and pilot.get("status") != "passed" and len(job.get("completed_leaves", [])) >= pilot["size"]:
            job["status"] = "awaiting_acceptance"
            pilot.update(status="awaiting_acceptance", finished_at=now())
            self.save(job)
            return True
        return False

    def accept_pilot(self, identifier, report, background=False):
        if not isinstance(report, dict) or set(report) != {"job_id", "structural_passed", "semantic_review_passed", "report_path", "report_sha256"}:
            raise CatalogError("验收记录字段无效")
        if (report["job_id"] != identifier or report["structural_passed"] is not True or report["semantic_review_passed"] is not True
                or not isinstance(report["report_path"], str) or not 1 <= len(report["report_path"]) <= 1000
                or not re.fullmatch(r"[a-f0-9]{64}", str(report["report_sha256"]))):
            raise CatalogError("需完成来源、许可证、增量及实际内容验收后才能续跑")
        lock = self.store._lock()
        try:
            job = self.get(identifier, detect_interruption=False)
            if job.get("pilot", {}).get("status") == "passed":
                lock.close()
                return job
            if job["status"] != "awaiting_acceptance":
                raise CatalogError("任务尚未到达试跑验收点", 409)
            expected = ROOT / "acceptance" / (identifier + ".json")
            if Path(report["report_path"]).resolve() != expected.resolve() or not expected.is_file():
                raise CatalogError("未找到本任务的实际验收记录")
            text = expected.read_text()
            evidence = json.loads(text)
            if (digest(text) != report["report_sha256"] or evidence.get("job_id") != identifier
                    or evidence.get("structural_passed") is not True or evidence.get("semantic_review_passed") is not True
                    or evidence.get("pilot_leaves") != job["leaves"][:job["pilot"]["size"]]):
                raise CatalogError("验收记录与本次试跑不一致")
            job["pilot"].update(status="passed", accepted_at=now(), report=report)
            job["status"] = "running"
            self.save(job)
            return self.launch(job, lock, background)
        except BaseException:
            lock.close()
            raise

    def execute_groups(self, job, leaf, remaining):
        groups = [remaining[offset:offset + job["batch_size"]] for offset in range(0, len(remaining), job["batch_size"])]
        pipeline = bool(groups and job.get("source_pipeline") and self.prefetcher)
        context = ThreadPoolExecutor(max_workers=1, thread_name_prefix="atlas-prefetch") if pipeline else nullcontext(None)
        with context as reader:
            future = reader.submit(self.prefetcher, self.store, leaf, [i["repository_id"] for i in groups[0]],
                                   source_policy=job["source_policy"]) if reader else None
            for index, group in enumerate(groups):
                for item in group:
                    item["status"] = "running"
                if job.get("storage_version") == 2:
                    with self.store.connect() as con:
                        con.executemany("UPDATE oss_batch_target SET status='running' WHERE job_id=? AND leaf=? AND repository_id=?", (
                            (job["id"], leaf, item["repository_id"]) for item in group))
                run = self.new_run(leaf)
                run["source_policy"] = job.get("source_policy", "full")
                run["phase"] = "read_sources"
                job["current_run"] = run["id"]
                job["runs"].append(run["id"])
                self.save(job)
                self.store._save_run(run)

                def checkpoint(identifier, state, reason):
                    item = next(i for i in group if i["repository_id"] == identifier)
                    was_pending = item["status"] in {"pending", "running"}
                    item.update(status=state, reason=reason, finished_at=now())
                    if job.get("storage_version") == 2:
                        with self.store.connect() as con:
                            con.execute("UPDATE oss_batch_target SET status=?,reason=?,finished_at=? WHERE job_id=? AND leaf=? AND repository_id=?", (
                                state, reason, item["finished_at"], job["id"], leaf, identifier))
                        job["processed"] += int(was_pending and state not in {"pending", "running"})
                    else:
                        job["processed"] = sum(i["status"] not in {"pending", "running"} for entries in job["targets"].values() for i in entries)
                        self.save(job)

                try:
                    options = {}
                    if reader:
                        options["prepared_sources"] = future.result()
                        # At most one following source group is in flight. Its
                        # immutable cache survives errors; it publishes nothing.
                        if index + 1 < len(groups):
                            future = reader.submit(self.prefetcher, self.store, leaf,
                                                   [i["repository_id"] for i in groups[index + 1]], source_policy=job["source_policy"])
                    self.worker(self.store, leaf, run, selected_ids=[i["repository_id"] for i in group], search=False,
                                on_candidate=checkpoint, **options)
                except ServiceUnavailable as error:
                    if future:
                        future.cancel()
                    run.update(status="interrupted" if error.component == "workflow" else "paused_model", finished_at=now())
                    self.store._save_run(run)
                    raise
                except Exception as error:
                    if job.get("storage_version") == 2 and not isinstance(error, CatalogError):
                        interruption = WorkflowInterrupted(type(error).__name__, run.get("phase"))
                        run.update(status="interrupted", finished_at=now(), interruption={"exception_type": type(error).__name__, "phase": run.get("phase")})
                        run["errors"].append({"error": str(interruption), "code": interruption.code})
                        self.store._save_run(run)
                        if future:
                            future.cancel()
                        raise interruption from error
                    run.update(status="failed", finished_at=now())
                    run["errors"].append({"error": str(error) if isinstance(error, CatalogError) else "本批执行失败，继续后续批次"})
                    self.store._save_run(run)
                self.recovery_succeeded(job)
                for item in group:
                    if item["status"] == "running":
                        reason = (run.get("errors") or [{"error": "本批未返回结果，已跳过"}])[-1]["error"]
                        self.store.candidate_result(leaf, item["repository_id"], "failed", reason)
                        checkpoint(item["repository_id"], "failed", reason)
                job["errors"].extend({"leaf": leaf, **error} for error in run.get("errors", []))
                self.save(job)

    @staticmethod
    def new_run(leaf):
        return {"id": "oss_" + uuid.uuid4().hex, "leaf": leaf, "status": "running", "started_at": now(),
                "created": 0, "updated": 0, "unchanged": 0, "failed": 0, "processed": 0, "errors": []}


class BatchRecoveryService:
    """Server-owned supervision; never depends on a browser poll or a chat turn."""

    def __init__(self, store=None, jobs=None):
        self.store = store or CatalogStore()
        self.jobs = jobs or BatchJobs(self.store)
        self.stop = threading.Event()
        self.thread = None
        self.health_path = self.store.path.with_suffix(".recovery.json")
        self.last_started = None

    def tick(self):
        health = {"checked_at": now(), "pid": os.getpid(), "started": [], "errors": []}
        with self.store.connect() as con:
            rows = con.execute("SELECT data FROM oss_batch_job WHERE status IN ('running','retry_wait','interrupted','partial') ORDER BY rowid").fetchall()
        for row in rows:
            job = json.loads(row[0])
            if job.get("auto_recovery") is not True:
                continue
            if job["status"] == "partial" and job.get("storage_version") == 2:
                with self.store.connect() as con:
                    eligible = con.execute("SELECT 1 FROM oss_batch_target WHERE job_id=? AND status='failed' AND reason=? LIMIT 1", (
                        job["id"], LEGACY_INTERRUPTION_REASON)).fetchone()
                if not eligible:
                    continue
                job = self.jobs.get(job["id"], detect_interruption=False)
            if job["status"] == "partial" and not self.jobs.interrupted_targets(job):
                continue
            try:
                resumed = self.jobs.resume(job["id"], background=True, automatic=True)
                if resumed["status"] in {"running", "retry_wait"}:
                    health["started"].append(job["id"])
                    self.last_started = {"job_id": job["id"], "at": now()}
            except CatalogError as error:
                if error.status != 409:
                    health["errors"].append(str(error))
        health["last_started"] = self.last_started
        atomic_json(self.health_path, health)
        return health

    def run(self):
        while not self.stop.is_set():
            try:
                self.tick()
            except Exception as error:
                # A supervisor failure must not silently kill supervision.
                from privacy import redact_text
                try:
                    atomic_json(self.health_path, {"checked_at": now(), "pid": os.getpid(),
                                                   "errors": [redact_text(str(error))]})
                except OSError:
                    print("OSS recovery supervisor could not save its health record", flush=True)
            self.stop.wait(15)

    def start(self):
        if not self.thread or not self.thread.is_alive():
            self.thread = threading.Thread(target=self.run, name="oss-batch-recovery", daemon=True)
            self.thread.start()
        return self


def dispatch_batch(store, method, path, body):
    jobs = BatchJobs(store)
    if method == "GET" and path == "/api/oss/batches":
        return {"jobs": jobs.list()}, 200
    match = re.fullmatch(r"/api/oss/batches/(batch_[0-9a-f]{32})(/resume|/accept-pilot)?", path)
    if match and method == "GET" and not match[2]:
        return jobs.get(match[1], include_targets=False), 200
    if method == "POST":
        if not isinstance(body, dict):
            raise CatalogError("请求必须是 JSON 对象")
        if path == "/api/oss/batches" and not set(body) - {"leaves", "existing_only", "batch_size", "search_pages", "first_round_limit", "pilot_size"}:
            return jobs.create(body.get("leaves"), body.get("existing_only", False), body.get("batch_size", 16), body.get("search_pages", 1),
                               background=True, first_round_limit=body.get("first_round_limit"), pilot_size=body.get("pilot_size", 0)), 202
        if match and match[2] == "/resume" and not body:
            return jobs.resume(match[1], background=True), 202
        if match and match[2] == "/accept-pilot":
            return jobs.accept_pilot(match[1], body, background=True), 202
    raise CatalogError("批量接口或参数无效", 400)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["start", "resume", "status"])
    parser.add_argument("--leaves", nargs="+", default=list(AUTO_LEAVES))
    parser.add_argument("--job")
    parser.add_argument("--db")
    parser.add_argument("--existing-only", action="store_true", help="固定现有待处理队列，不在本次任务中扩大搜索")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--search-pages", type=int, default=1)
    parser.add_argument("--first-round-limit", type=int)
    parser.add_argument("--pilot-size", type=int, default=0)
    parser.add_argument("--output")
    args = parser.parse_args()
    jobs = BatchJobs(CatalogStore(args.db))
    if args.action == "start":
        result = jobs.create(args.leaves, args.existing_only, args.batch_size, args.search_pages,
                             first_round_limit=args.first_round_limit, pilot_size=args.pilot_size)
    elif not args.job:
        parser.error("resume/status 需要 --job")
    elif args.action == "resume":
        result = jobs.resume(args.job)
    else:
        result = jobs.get(args.job)
    if args.output:
        atomic_json(Path(args.output), result)
    print(canonical(result), flush=True)


if __name__ == "__main__":
    main()
