"""Read-only preparation and same-job queueing for the fixed R7 evidence review."""
from __future__ import annotations

import hashlib
import json
import sqlite3
import subprocess
import time
import uuid

from .store import FactoryError, canonical, digest, now

SCHEMA = "atlas.evidence-recovery-proposal.v1"
PREPARE_SCHEMA = "atlas.evidence-recovery-prepare.v1"
RECOVER_SCHEMA = "atlas.evidence-recovery.v1"
SAVED_RESUME_SCHEMA = "atlas.evidence-saved-result-resume.v1"
SOURCE_REF = "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/authorization/ATLAS_G1_R7_EVIDENCE_RECOVERY_CODEX_INSTRUCTIONS.txt"
SOURCE_DIGEST = "9194614646b37e52e8dbe026f8e383b65f91337925b674ca93940cd968fd7675"
JOB_ID = "job_3a658ba085e8417ea6faad5cb0cdd493"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"
CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
BATCH_ID = "bat_6b4fc8bf5b4e42d79bc6a9069277e9f0"
PLAN_PARENT_BATCH_ID = "bat_d13dc5920a574140be85da0ea6f5395b"
SNAPSHOT_DIGEST = "c4778af6053066cc90b22c1c1320928f7bed4ea9c818bed19cf62c3e986e9239"
DEADLINE = 1792495312.855422
ACTIVE_AMENDMENT_ID = "bamd_f2054b5d9a9b4e80b6a4e379ed04a42a"
RETRY_SCOPE = "blueprint-spec-review:phase_acceptance"
REQUIRED_CHECKS = ("check", "docker-integration")


def _strict_keys(value, keys, label):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise FactoryError(f"{label} has unknown or missing fields", "evidence_recovery_schema", 400)


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _source_tree(repo_root, evidence_paths=()):
    try:
        head = subprocess.run(["git", "-C", str(repo_root), "rev-parse", "HEAD"], check=True,
                              capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", str(repo_root), "status", "--porcelain", "-z"], check=True,
                               capture_output=True, text=True).stdout
    except (OSError, subprocess.CalledProcessError) as exc:
        raise FactoryError("source checkout identity is unavailable", "evidence_source_gate", 409) from exc
    dirty_paths = [item[3:] for item in dirty.split("\0") if item]
    if any(path not in set(evidence_paths) for path in dirty_paths):
        raise FactoryError("source checkout must be clean before evidence recovery registration", "evidence_source_gate", 409)
    from .v1_batches import _g1_source_digest
    return head, _g1_source_digest(repo_root)


def validate_source_gate(store, gate):
    """Verify the exact checked-out commit/tree and raw GitHub run/job evidence."""
    _strict_keys(gate, {"source_commit", "source_tree_digest", "ci_evidence"}, "source gate")
    repo_root = store.pack.parent
    evidence = gate["ci_evidence"]
    if not isinstance(evidence, list) or not evidence:
        raise FactoryError("source gate must bind this source revision's CI runs", "evidence_source_gate", 409)
    allowlisted = [item.get("path") for item in evidence if isinstance(item, dict)]
    head, tree = _source_tree(repo_root, allowlisted)
    if gate["source_commit"] != head or gate["source_tree_digest"] != tree:
        raise FactoryError("source gate does not identify the current clean checkout", "evidence_source_gate", 409)
    observed = set()
    successful_checks = set()
    for item in evidence:
        _strict_keys(item, {"path", "sha256", "run_id", "head_sha", "required_checks"}, "CI evidence")
        run_id = item["run_id"]
        if not isinstance(run_id, int) or run_id in observed:
            raise FactoryError("CI evidence run identity is duplicated or invalid", "evidence_source_gate", 409)
        observed.add(run_id)
        rel = item["path"]
        if (not isinstance(rel, str) or not rel.startswith("docs/template-factory/")
                or not rel.endswith(".json") or any(part in {"", ".", ".."} for part in rel.split("/"))):
            raise FactoryError("CI evidence path is outside the template factory evidence archive", "evidence_source_gate", 409)
        path = repo_root / rel
        if path.is_symlink() or any(parent.is_symlink() for parent in (path.parent, *path.parent.parents) if parent != repo_root.parent):
            raise FactoryError("CI evidence must be a regular file without symlinked parents", "evidence_source_gate", 409)
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise FactoryError("raw CI evidence is unavailable", "evidence_source_gate", 409) from exc
        if _sha256(raw) != item["sha256"]:
            raise FactoryError("raw CI evidence bytes differ from their bound digest", "evidence_source_gate", 409)
        try:
            document = json.loads(raw)
        except (ValueError, UnicodeDecodeError) as exc:
            raise FactoryError("raw CI evidence is not valid JSON", "evidence_source_gate", 409) from exc
        runs = document.get("runs") if isinstance(document, dict) else None
        matches = [entry for entry in runs or [] if isinstance(entry, dict)
                   and isinstance(entry.get("run"), dict) and entry["run"].get("id") == run_id]
        if len(matches) != 1:
            raise FactoryError("raw CI archive does not contain exactly the bound run", "evidence_source_gate", 409)
        record = matches[0]
        run = record["run"]
        if (run.get("head_sha") != item["head_sha"] or run.get("head_sha") != head
                or run.get("status") != "completed" or run.get("conclusion") != "success"
                or item["required_checks"] != list(REQUIRED_CHECKS)):
            raise FactoryError("GitHub run is not successful for the exact source head", "evidence_source_gate", 409)
        jobs = record.get("jobs", {}).get("jobs", [])
        for required in REQUIRED_CHECKS:
            found = [job for job in jobs if job.get("name") == required]
            if found:
                if len(found) != 1 or found[0].get("status") != "completed" or found[0].get("conclusion") != "success":
                    raise FactoryError("required GitHub check or docker-integration job is not successful", "evidence_source_gate", 409)
                successful_checks.add(required)
    if successful_checks != set(REQUIRED_CHECKS):
        raise FactoryError("source gate omits a successful check or docker-integration job", "evidence_source_gate", 409)
    return {"source_commit": head, "source_tree_digest": tree, "ci_evidence": evidence}


class EvidenceRecoveryService:
    def __init__(self, store, *, clock=time.time, evidence_builder=None, source_gate_validator=None):
        self.store, self.clock = store, clock
        self._evidence_builder = evidence_builder
        self._source_gate_validator = source_gate_validator
    @staticmethod
    def _initialize_locked(con):
        con.execute("CREATE TABLE IF NOT EXISTS tf_frozen_review_schema_migration(version INTEGER PRIMARY KEY,applied_at REAL NOT NULL,migration_digest TEXT NOT NULL)")
        con.execute("""CREATE TABLE IF NOT EXISTS tf_evidence_recovery (
                recovery_id TEXT PRIMARY KEY, job_id TEXT NOT NULL, grant_id TEXT NOT NULL UNIQUE,
                request_key TEXT NOT NULL UNIQUE, request_digest TEXT NOT NULL, proposal_digest TEXT NOT NULL,
                old_state TEXT NOT NULL, old_error TEXT, old_stage TEXT NOT NULL, old_attempt INTEGER NOT NULL,
                snapshot_digest TEXT NOT NULL, checkpoint_digest TEXT NOT NULL, checkpoint_names TEXT NOT NULL,
                old_events_json TEXT NOT NULL, created_at TEXT NOT NULL)""")
        # A job may have sequential, separately authorized recoveries. Preserve
        # all historical receipts while removing only the obsolete job UNIQUE.
        unique_job = False
        for index in con.execute("PRAGMA index_list(tf_evidence_recovery)").fetchall():
            if not index[2]:
                continue
            columns = [col[2] for col in con.execute(f"PRAGMA index_info('{index[1]}')").fetchall()]
            if columns == ["job_id"]:
                unique_job = True
                break
        if unique_job:
            custom_indexes = [row[0] for row in con.execute("SELECT sql FROM sqlite_master WHERE type='index' AND tbl_name='tf_evidence_recovery' AND sql IS NOT NULL")]
            con.execute("ALTER TABLE tf_evidence_recovery RENAME TO tf_evidence_recovery_legacy")
            con.execute("""CREATE TABLE tf_evidence_recovery (
                recovery_id TEXT PRIMARY KEY, job_id TEXT NOT NULL, grant_id TEXT NOT NULL UNIQUE,
                request_key TEXT NOT NULL UNIQUE, request_digest TEXT NOT NULL, proposal_digest TEXT NOT NULL,
                old_state TEXT NOT NULL, old_error TEXT, old_stage TEXT NOT NULL, old_attempt INTEGER NOT NULL,
                snapshot_digest TEXT NOT NULL, checkpoint_digest TEXT NOT NULL, checkpoint_names TEXT NOT NULL,
                old_events_json TEXT NOT NULL, created_at TEXT NOT NULL)""")
            con.execute("""INSERT INTO tf_evidence_recovery
                (recovery_id,job_id,grant_id,request_key,request_digest,proposal_digest,old_state,old_error,
                 old_stage,old_attempt,snapshot_digest,checkpoint_digest,checkpoint_names,old_events_json,created_at)
                SELECT recovery_id,job_id,grant_id,request_key,request_digest,proposal_digest,old_state,old_error,
                       old_stage,old_attempt,snapshot_digest,checkpoint_digest,checkpoint_names,old_events_json,created_at
                FROM tf_evidence_recovery_legacy""")
            con.execute("DROP TABLE tf_evidence_recovery_legacy")
            for statement in custom_indexes:
                con.execute(statement)
        con.execute("INSERT OR IGNORE INTO tf_frozen_review_schema_migration VALUES(2,?,?)",
                    (time.time(), "recovery-job-unique-to-sequential-v1"))

    def _materials(self, job_id):
        if self._evidence_builder is not None:
            return self._evidence_builder(self.store, job_id)
        from .evidence_views import build_evidence_review_materials
        return build_evidence_review_materials(self.store, job_id)

    def _validate_gate(self, gate):
        return (self._source_gate_validator(self.store, gate)
                if self._source_gate_validator else validate_source_gate(self.store, gate))

    def prepare(self, job_id, request):
        _strict_keys(request, {"schema", "request_key", "source_authorization", "source_gate"}, "prepare request")
        if request["schema"] != PREPARE_SCHEMA or job_id != JOB_ID:
            raise FactoryError("unsupported evidence prepare schema or job", "evidence_recovery_scope", 409)
        key = request["request_key"]
        if not isinstance(key, str) or not key.strip() or len(key) > 160:
            raise FactoryError("request_key must be a stable non-empty string", "evidence_recovery_schema", 400)
        _strict_keys(request["source_authorization"], {"source_ref", "source_digest"}, "source authorization")
        if request["source_authorization"] != {"source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST}:
            raise FactoryError("source authorization differs from the fixed R7 recovery instruction", "evidence_recovery_authorization", 403)
        auth_path = self.store.pack.parent / SOURCE_REF
        if auth_path.is_symlink():
            raise FactoryError("source authorization must be a regular file", "evidence_recovery_authorization", 409)
        try:
            auth_bytes = auth_path.read_bytes()
        except OSError as exc:
            raise FactoryError("source authorization file is unavailable", "evidence_recovery_authorization", 409) from exc
        if _sha256(auth_bytes) != SOURCE_DIGEST:
            raise FactoryError("source authorization bytes differ from the fixed digest", "evidence_recovery_authorization", 409)
        gate = self._validate_gate(request["source_gate"])
        materials = self._materials(job_id)
        proposal = {"schema": SCHEMA, "request_key": key,
                    "source_authorization": request["source_authorization"],
                    "source_gate": gate, "source_gate_passed": True, "materials": materials}
        proposal["proposal_digest"] = digest(proposal)
        return proposal

    def register(self, prepared_proposal, request):
        from .evidence_grants import EvidenceGrantService
        # The immutable registration replay is resolved before checking today's
        # source tree, CI archive, deadline or failed-job state. A consumed grant
        # remains readable for audit, but never creates another opportunity.
        try:
            request_key = request.get("request_key") if isinstance(request, dict) else None
            with self.store.connect() as con:
                existing = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE campaign_id=? AND request_key=?",
                                       (CAMPAIGN_ID, request_key)).fetchone()
        except sqlite3.OperationalError as exc:
            if "no such table" in str(exc):
                existing = None
            else:
                raise
        if existing is not None:
            stored = json.loads(existing["request_json"])
            request_matches = (isinstance(request, dict)
                               and set(request) == {"schema", "request_key", "source_authorization", "source_gate"}
                               and request.get("schema") == PREPARE_SCHEMA
                               and request.get("request_key") == stored.get("request_key")
                               and request.get("source_authorization") == stored.get("source_authorization")
                               and request.get("source_gate") == stored.get("source_gate"))
            if (not request_matches or prepared_proposal != stored
                    or stored.get("proposal_digest") != digest({k: v for k, v in stored.items() if k != "proposal_digest"})):
                raise FactoryError("request key is already bound to different prepared evidence", "evidence_grant_conflict", 409)
            return EvidenceGrantService._record(existing)
        # Reconstruct the proposal from the request so stale or edited materials
        # cannot be registered under a previously prepared digest.
        proposal = self.prepare(JOB_ID, request)
        if proposal != prepared_proposal:
            raise FactoryError("prepared evidence proposal changed before grant registration", "evidence_recovery_changed", 409)
        return EvidenceGrantService(self.store, clock=self.clock,
                                    source_gate_validator=self._source_gate_validator).register(proposal, request)

    def recover(self, job_id, request):
        _strict_keys(request, {"schema", "grant_id", "request_key", "proposal_digest"}, "recovery request")
        if request["schema"] != RECOVER_SCHEMA or job_id != JOB_ID:
            raise FactoryError("unsupported evidence recovery schema or job", "evidence_recovery_scope", 409)
        request_digest = digest(request)
        with self.store.connect(True) as con:
            self._initialize_locked(con)
            prior = con.execute("SELECT * FROM tf_evidence_recovery WHERE job_id=?", (job_id,)).fetchone()
            if prior:
                if prior["request_key"] != request["request_key"] or prior["request_digest"] != request_digest:
                    raise FactoryError("this job was already recovered under a different request", "idempotency_conflict", 409)
                return self._result(prior, True)
            job = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            if not job:
                raise FactoryError("evidence recovery job not found", "not_found", 404)
            snapshot = json.loads(job["snapshot"])
            if (job["state"] != "failed" or job["attempt"] != 1 or digest(snapshot) != SNAPSHOT_DIGEST
                    or job["batch_id"] != BATCH_ID):
                raise FactoryError("job is not the fixed failed attempt-1 R7 job", "evidence_recovery_state", 409)
            batch = con.execute("SELECT state FROM batch WHERE id=?", (BATCH_ID,)).fetchone()
            parent_batch = con.execute("SELECT state FROM batch WHERE id=?", (PLAN_PARENT_BATCH_ID,)).fetchone()
            if not batch or batch["state"] != "paused" or not parent_batch or parent_batch["state"] != "paused":
                raise FactoryError("parent batch must remain paused during recovery", "evidence_recovery_parent", 409)
            grant_row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (request["grant_id"],)).fetchone()
            if grant_row is None:
                raise FactoryError("evidence grant not found", "evidence_grant_missing", 404)
            proposal = json.loads(grant_row["request_json"])
            if proposal.get("proposal_digest") != request["proposal_digest"]:
                raise FactoryError("request does not bind the registered proposal", "evidence_recovery_binding", 409)
            if self._validate_gate(proposal.get("source_gate")) != proposal.get("source_gate"):
                raise FactoryError("source gate changed after grant registration", "evidence_source_gate", 409)
            from .evidence_grants import EvidenceGrantService
            EvidenceGrantService.validate_locked(con, request["grant_id"], proposal, request["request_key"], job_id)
            # Recompute the complete proposal before acquiring any provider call.
            # Builder/source checks are read-only; transaction rolls back on drift.
            fresh = self._materials(job_id)
            if fresh != proposal.get("materials"):
                raise FactoryError("current source or review materials differ from the registered proposal", "evidence_recovery_changed", 409)
            self._check_budget_locked(con)
            checkpoints = con.execute("SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (job_id,)).fetchall()
            checkpoint_map = {row["name"]: json.loads(row["body"]) for row in checkpoints}
            old_events = [dict(row) for row in con.execute("SELECT seq,attempt,at,stage,message FROM event WHERE job_id=? ORDER BY seq", (job_id,))]
            if not checkpoint_map:
                raise FactoryError("original review checkpoints are missing", "evidence_recovery_checkpoints", 409)
            checkpoint_digest = digest(checkpoint_map)
            from .evidence_grants import EvidenceGrantService
            EvidenceGrantService.queue_locked(con, request["grant_id"], proposal, request["request_key"], job_id)
            at = now()
            recovery_id = "erec_" + uuid.uuid4().hex
            con.execute("""INSERT INTO tf_evidence_recovery
                (recovery_id,job_id,grant_id,request_key,request_digest,proposal_digest,old_state,old_error,
                 old_stage,old_attempt,snapshot_digest,checkpoint_digest,checkpoint_names,old_events_json,created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (recovery_id, job_id, request["grant_id"], request["request_key"], request_digest,
                 proposal["proposal_digest"], job["state"], job["error"], job["stage"], job["attempt"],
                 digest(snapshot), checkpoint_digest, canonical(sorted(checkpoint_map)), canonical(old_events), at))
            updated = con.execute("UPDATE job SET state='queued',attempt=2,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=? AND state='failed' AND attempt=1",
                                  (at, job_id)).rowcount
            if updated != 1:
                raise FactoryError("job changed while evidence recovery was being committed", "evidence_recovery_race", 409)
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (job_id, 2, at, job["stage"], "Authorized same-job evidence recovery queued; no provider started"))
            record = con.execute("SELECT * FROM tf_evidence_recovery WHERE recovery_id=?", (recovery_id,)).fetchone()
            return self._result(record, False)

    def _check_budget_locked(self, con):
        sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN_ID,)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN_ID,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()[0]
        retry_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'", (CAMPAIGN_ID, PRODUCT_ID)).fetchall()
        from .budget import _legacy_retry_scope
        retry_count = sum(1 for row in retry_rows if (row["retry_scope"] or _legacy_retry_scope(row["stage"])) == RETRY_SCOPE)
        amendment = con.execute("SELECT id,version,new_deadline FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND activated_at IS NOT NULL ORDER BY version DESC LIMIT 1", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()
        if (sessions != 77 or active != 0 or repairs != 7 or retry_count != 3 or not amendment
                or amendment["id"] != ACTIVE_AMENDMENT_ID or amendment["version"] != 4
                or float(amendment["new_deadline"]) != DEADLINE or float(self.clock()) >= DEADLINE):
            raise FactoryError("G1 call, repair, active-job or fixed-deadline baseline changed", "evidence_recovery_budget", 409)
        old_grants = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE campaign_id=? AND product_id=? AND job_id=?", (CAMPAIGN_ID, PRODUCT_ID, "job_7742b1c124be4c9ab3a0096da5cdd772")).fetchall()
        old_uses = con.execute("SELECT status FROM tf_protocol_retry_grant_use WHERE grant_id=? AND reservation_id=?", ("pgrant_f3595368c14d4b23b6ab536f6d198007", "bud_9a81a7a4adc14f49b46239ec68ee2fdb")).fetchall()
        if (len(old_grants) != 1 or old_grants[0]["status"] != "consumed"
                or old_grants[0]["consumed_reservation_id"] != "bud_9a81a7a4adc14f49b46239ec68ee2fdb"
                or len(old_uses) != 1 or old_uses[0]["status"] != "consumed"):
            raise FactoryError("old R5/R6 protocol grant must remain consumed exactly once", "evidence_recovery_budget", 409)

    def active_for_job(self, job_id):
        if job_id != JOB_ID:
            return None
        with self.store.connect() as con:
            try:
                row = con.execute("SELECT r.*,g.request_json FROM tf_evidence_recovery r JOIN tf_evidence_recovery_grant g ON g.id=r.grant_id WHERE r.job_id=?", (job_id,)).fetchone()
            except sqlite3.OperationalError as exc:
                if "no such table" in str(exc):
                    return None
                raise
        if row is None:
            return None
        result = {"grant_id": row["grant_id"], "recovery_id": row["recovery_id"],
                "proposal": json.loads(row["request_json"]), "attempt": row["old_attempt"] + 1,
                "request_key": row["request_key"], "proposal_digest": row["proposal_digest"]}
        with self.store.connect() as con:
            try:
                saved = con.execute("SELECT * FROM tf_evidence_saved_resume WHERE job_id=? ORDER BY next_attempt DESC LIMIT 1", (job_id,)).fetchone()
            except sqlite3.OperationalError as exc:
                if "no such table" not in str(exc):
                    raise
                saved = None
        if saved:
            result.update({"host_only": True, "source_gate": json.loads(saved["source_gate_json"]),
                           "saved_result_sha256": saved["result_sha256"],
                           "saved_resume_id": saved["id"]})
        return result

    def resume_saved_result(self, job_id, request):
        """Queue a host-only continuation after a checked source fix, never a CLI retry."""
        _strict_keys(request, {"schema", "grant_id", "request_key", "source_gate", "expected_saved_result_sha256"}, "saved-result resume")
        if request["schema"] != SAVED_RESUME_SCHEMA or job_id != JOB_ID:
            raise FactoryError("unsupported saved-result recovery scope", "evidence_recovery_scope", 409)
        key = request["request_key"]
        if not isinstance(key, str) or not key.strip() or len(key) > 160:
            raise FactoryError("stable saved-result resume key required", "evidence_recovery_schema", 400)
        request_digest = digest(request)
        with self.store.connect(True) as con:
            con.execute("""CREATE TABLE IF NOT EXISTS tf_evidence_saved_resume (
                id TEXT PRIMARY KEY, job_id TEXT NOT NULL, grant_id TEXT NOT NULL,
                request_key TEXT NOT NULL UNIQUE, request_digest TEXT NOT NULL,
                source_gate_json TEXT NOT NULL, result_sha256 TEXT NOT NULL,
                old_attempt INTEGER NOT NULL, next_attempt INTEGER NOT NULL, created_at TEXT NOT NULL)""")
            prior = con.execute("SELECT * FROM tf_evidence_saved_resume WHERE request_key=?", (key,)).fetchone()
            if prior:
                if prior["job_id"] != job_id or prior["request_digest"] != request_digest:
                    raise FactoryError("saved-result resume key conflict", "idempotency_conflict", 409)
                return dict(prior, replayed=True, worker_started=False, cli_allowed=False)
            recovery = con.execute("SELECT * FROM tf_evidence_recovery WHERE job_id=? AND grant_id=?", (job_id, request["grant_id"])).fetchone()
            grant_row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (request["grant_id"],)).fetchone()
            job = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            if (not recovery or not grant_row or not job or job["state"] not in {"failed", "interrupted"}
                    or job["attempt"] < 2 or digest(json.loads(job["snapshot"])) != SNAPSHOT_DIGEST
                    or float(self.clock()) >= DEADLINE):
                raise FactoryError("saved-result continuation is not currently eligible", "evidence_saved_state", 409)
            for batch_id in (BATCH_ID, PLAN_PARENT_BATCH_ID):
                batch = con.execute("SELECT state FROM batch WHERE id=?", (batch_id,)).fetchone()
                if not batch or batch["state"] != "paused":
                    raise FactoryError("saved-result continuation requires paused batches", "evidence_recovery_parent", 409)
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN_ID,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()[0]
            if active or repairs != 7:
                raise FactoryError("saved-result continuation cannot change active budget or repairs", "evidence_recovery_budget", 409)
            gate = self._validate_gate(request["source_gate"])
            from .evidence_grants import EvidenceGrantService
            grant = EvidenceGrantService._record(grant_row)
            proposal = grant["proposal"]
            if self._materials(job_id) != proposal["materials"]:
                raise FactoryError("reviewed inputs changed; host-only resume forbidden", "checkpoint_changed", 409)
            raw, path = saved_phase_result(self.store, grant, proposal["materials"])
            if _sha256(path.read_bytes()) != request["expected_saved_result_sha256"]:
                raise FactoryError("saved-result bytes changed", "checkpoint_changed", 409)
            # A complete semantic pass is necessary. Missing references or a
            # blocked/uncertain review require stopping, never host-only repair.
            from .cognition import validate_review
            report = validate_review(raw, path.parent / "source", ("phase_acceptance",))
            if report["outcome"] != "passed":
                raise FactoryError("saved phase is not a complete pass", "evidence_review_not_passed", 409)
            outer_key = proposal["materials"]["old_aggregate"]["checkpoint_name"] + "-evidence-" + grant["id"]
            outer = con.execute("SELECT body FROM checkpoint WHERE job_id=? AND name=?", (job_id, outer_key)).fetchone()
            if outer and json.loads(outer["body"])["result"]["outcome"] != "passed":
                raise FactoryError("semantic combination failure cannot be bypassed", "evidence_review_not_passed", 409)
            rid, at = "esave_" + uuid.uuid4().hex, now()
            next_attempt = job["attempt"] + 1
            con.execute("INSERT INTO tf_evidence_saved_resume VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (rid, job_id, grant["id"], key, request_digest, canonical(gate), request["expected_saved_result_sha256"], job["attempt"], next_attempt, at))
            con.execute("UPDATE job SET state='queued',attempt=?,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=?", (next_attempt, at, job_id))
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (job_id, next_attempt, at, job["stage"], "Checked host-only saved-result continuation queued; no CLI qualification created"))
            return {"id": rid, "job_id": job_id, "grant_id": grant["id"], "attempt": next_attempt,
                    "replayed": False, "worker_started": False, "cli_allowed": False}

    get_for_job = active_for_job

    @staticmethod
    def _result(row, replay):
        return {"recovery_id": row["recovery_id"], "job_id": row["job_id"],
                "grant_id": row["grant_id"], "request_key": row["request_key"],
                "proposal_digest": row["proposal_digest"], "old_attempt": row["old_attempt"],
                "attempt": row["old_attempt"] + 1, "state": "queued",
                "snapshot_digest": row["snapshot_digest"], "checkpoint_digest": row["checkpoint_digest"],
                "checkpoint_names": json.loads(row["checkpoint_names"]), "replayed": replay,
                "worker_started": False}


def saved_phase_result(store, grant, materials):
    """Read a completed result from the actual charged attempt, with exact input proof."""
    from .artifacts import tree_manifest
    attempt = grant.get("call_attempt")
    if not isinstance(attempt, int) or attempt < 2:
        raise FactoryError("supplementary call attempt is unproved", "evidence_result_unproved", 409)
    new = materials["new_phase"]
    directory = store.root / "jobs" / JOB_ID / ("attempt-" + str(attempt)) / new["stage_name"]
    path = directory / "result.json"
    try:
        input_bytes = (directory / "input.json").read_bytes()
        if (_sha256(input_bytes) != new["input_sha256"]
                or digest(json.loads(input_bytes)) != new["full_payload_digest"]
                or digest(tree_manifest(directory / "source")) != new["source_tree_digest"]):
            raise FactoryError("saved supplementary result input changed", "checkpoint_changed", 409)
        raw = json.loads(path.read_bytes())
    except FactoryError:
        raise
    except (OSError, ValueError) as exc:
        raise FactoryError("supplementary saved result unavailable; no blind retry", "evidence_result_unproved", 409) from exc
    with store.connect() as con:
        reservation = con.execute("SELECT * FROM tf_budget_reservation WHERE id=?", (grant.get("consumed_reservation_id"),)).fetchone()
    if (not reservation or reservation["status"] != "completed" or reservation["stage"] != new["operation"]
            or reservation["job_id"] != JOB_ID or grant.get("status") != "consumed"):
        raise FactoryError("saved result lacks its completed one-use reservation", "evidence_result_unproved", 409)
    return raw, path
