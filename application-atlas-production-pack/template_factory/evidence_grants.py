"""One-use, input-bound authorization for the fixed R7 evidence review."""

from __future__ import annotations

import hashlib
import json
import time
import uuid

from .store import FactoryError, digest

SCHEMA = "atlas.evidence-recovery-proposal.v1"
AUTHORIZATION_SOURCE_REF = "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/authorization/ATLAS_G1_R7_EVIDENCE_RECOVERY_CODEX_INSTRUCTIONS.txt"
AUTHORIZATION_SOURCE_DIGEST = "9194614646b37e52e8dbe026f8e383b65f91337925b674ca93940cd968fd7675"
CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"
JOB_ID = "job_3a658ba085e8417ea6faad5cb0cdd493"
PREDECESSOR_ID = "bamd_100a302fe8424d9493dafe62d6e43db9"
R7_V4_AMENDMENT_ID = "bamd_f2054b5d9a9b4e80b6a4e379ed04a42a"
R7_BATCH_ID = "bat_6b4fc8bf5b4e42d79bc6a9069277e9f0"
R7_PARENT_BATCH_ID = "bat_d13dc5920a574140be85da0ea6f5395b"
FAILED_ATTEMPT = 1
SNAPSHOT_DIGEST = "c4778af6053066cc90b22c1c1320928f7bed4ea9c818bed19cf62c3e986e9239"
OLD_DEADLINE = 1792495312.855422
RETRY_SCOPE = "blueprint-spec-review:phase_acceptance"
STAGE_NAME = "blueprint-spec-review-0-ad1379367f3e742a-phase_acceptance"
REQUESTED_MODEL = "opencode-go/deepseek-v4.1-flash"
MAX_EXTRA_CALLS = 1


class EvidenceGrantService:
    """Persist an immutable proposal and one opportunity to spend it.

    Recovery queueing only changes ``registered`` to ``queued``. The actual
    budget reservation atomically changes ``queued`` to ``reserved``. A
    confirmed pre-spawn failure can release the same opportunity back to
    ``queued``; any spawn intent or possible start permanently occupies it.
    """

    def __init__(self, store, *, clock=time.time, initialize=True, source_gate_validator=None):
        self.store, self.clock = store, clock
        self._source_gate_validator = source_gate_validator
        if initialize:
            with store.connect(True) as con:
                self.initialize_locked(con)

    @staticmethod
    def initialize_locked(con):
        con.execute(
            "CREATE TABLE IF NOT EXISTS tf_evidence_recovery_grant ("
            "id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,"
            "plan_id TEXT NOT NULL,job_id TEXT NOT NULL,request_key TEXT NOT NULL,"
            "proposal_digest TEXT NOT NULL,request_json TEXT NOT NULL,status TEXT NOT NULL,"
            "queued_job_id TEXT,consumed_reservation_id TEXT,call_attempt INTEGER,created_at REAL NOT NULL,"
            "UNIQUE(campaign_id,request_key),UNIQUE(campaign_id,job_id))"
        )
        columns = {row[1] for row in con.execute("PRAGMA table_info(tf_evidence_recovery_grant)")}
        if "call_attempt" not in columns:
            con.execute("ALTER TABLE tf_evidence_recovery_grant ADD COLUMN call_attempt INTEGER")

    def _verify_authorization(self, proposal):
        authorization = proposal.get("source_authorization")
        if not isinstance(authorization, dict):
            raise FactoryError("evidence recovery source authorization is missing", "evidence_grant_binding", 403)
        source_ref = authorization.get("source_ref")
        source_digest = authorization.get("source_digest")
        if source_ref != AUTHORIZATION_SOURCE_REF or source_digest != AUTHORIZATION_SOURCE_DIGEST:
            raise FactoryError("evidence recovery source authorization differs", "evidence_grant_binding", 403)
        path = self.store.pack.parent / AUTHORIZATION_SOURCE_REF
        try:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("evidence recovery authorization source is unavailable", "evidence_grant_source", 409) from exc
        if actual != AUTHORIZATION_SOURCE_DIGEST:
            raise FactoryError("evidence recovery authorization bytes changed", "evidence_grant_source", 409)

    def _verify_current_job(self):
        job = self.store.job(JOB_ID)
        if (job["state"] != "failed" or job["attempt"] != FAILED_ATTEMPT
                or job["batch_id"] != R7_BATCH_ID or digest(job["snapshot"]) != SNAPSHOT_DIGEST):
            raise FactoryError("current R7 failed job no longer matches the authorized baseline", "evidence_grant_baseline", 409)

    def _verify_source_gate(self, proposal):
        from .evidence_recovery import validate_source_gate
        gate = proposal.get("source_gate")
        validator = self._source_gate_validator or validate_source_gate
        if validator(self.store, gate) != gate:
            raise FactoryError("source gate changed after evidence preparation", "evidence_grant_source", 409)

    @staticmethod
    def _verify_budget_baseline_locked(con):
        from .budget import G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID
        calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN_ID,)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN_ID,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()[0]
        scope_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                                 (CAMPAIGN_ID, PRODUCT_ID)).fetchall()
        from .budget import _legacy_retry_scope
        scope_count = sum(1 for row in scope_rows if
                          (row[0] == RETRY_SCOPE if row[0] is not None else _legacy_retry_scope(row[1]) == RETRY_SCOPE))
        deadline = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'", (CAMPAIGN_ID,)).fetchone()
        amendment = con.execute("SELECT id,version,new_deadline,activated_at FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? ORDER BY version DESC LIMIT 1",
                                (CAMPAIGN_ID, PRODUCT_ID)).fetchone()
        batch = con.execute("SELECT state FROM batch WHERE id=?", (R7_BATCH_ID,)).fetchone()
        parent_batch = con.execute("SELECT state FROM batch WHERE id=?", (R7_PARENT_BATCH_ID,)).fetchone()
        grant = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id=?", (G1_R6_PROTOCOL_GRANT_ID,)).fetchone()
        uses = con.execute("SELECT status FROM tf_protocol_retry_grant_use WHERE grant_id=? AND reservation_id=?", (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID)).fetchall()
        if (calls != 77 or active != 0 or repairs != 7 or scope_count != 3
                or not deadline or not amendment or amendment["id"] != R7_V4_AMENDMENT_ID
                or amendment["version"] != 4 or amendment["activated_at"] is None
                or float(amendment["new_deadline"]) != OLD_DEADLINE
                or not batch or batch["state"] != "paused"
                or not parent_batch or parent_batch["state"] != "paused"
                or not grant or grant["status"] != "consumed"
                or grant["consumed_reservation_id"] != G1_R6_PROTOCOL_RESERVATION_ID
                or len(uses) != 1 or uses[0]["status"] != "consumed"):
            raise FactoryError("G1 budget, pause, old-grant, repair or deadline baseline changed", "evidence_grant_baseline", 409)

    @staticmethod
    def _proposal_digest(proposal):
        return digest({key: value for key, value in proposal.items() if key != "proposal_digest"})

    def _validate_proposal(self, proposal, request):
        if not isinstance(proposal, dict) or proposal.get("schema") != SCHEMA:
            raise FactoryError("unsupported evidence recovery proposal schema", "evidence_grant_schema", 400)
        if proposal.get("proposal_digest") != self._proposal_digest(proposal):
            raise FactoryError("evidence recovery proposal digest does not match", "evidence_grant_binding", 409)
        request_key = proposal.get("request_key")
        if not isinstance(request_key, str) or not request_key:
            raise FactoryError("evidence recovery request key is required", "evidence_grant_binding", 400)
        supplied_key = request.get("request_key", request.get("idempotency_key")) if isinstance(request, dict) else None
        if supplied_key != request_key:
            raise FactoryError("request key differs from the prepared proposal", "evidence_grant_binding", 403)
        self._verify_authorization(proposal)
        materials = proposal.get("materials")
        binding = materials.get("binding") if isinstance(materials, dict) else None
        phase = materials.get("new_phase") if isinstance(materials, dict) else None
        if not isinstance(binding, dict) or not isinstance(phase, dict):
            raise FactoryError("evidence recovery proposal is missing phase binding", "evidence_grant_binding", 409)
        fixed = {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                 "job_id": JOB_ID, "attempt": FAILED_ATTEMPT, "snapshot_digest": SNAPSHOT_DIGEST,
                 "batch_id": R7_BATCH_ID, "deadline": OLD_DEADLINE}
        if any(binding.get(key) != value for key, value in fixed.items()):
            raise FactoryError("evidence recovery job, snapshot or deadline differs", "evidence_grant_binding", 409)
        if float(self.clock()) >= OLD_DEADLINE:
            raise FactoryError("evidence recovery authorization deadline has passed", "budget_deadline", 409)
        self._verify_current_job()
        old_phase = materials.get("old_phase")
        old_aggregate = materials.get("old_aggregate")
        if (not isinstance(old_phase, dict)
                or old_phase.get("checkpoint_name") != "blueprint-design-check-0-phase_acceptance"
                or old_phase.get("checkpoint_digest") != "dd19d90217dc6cadd7e8346ac4d2af2b1b5a73f4fee2f28aa3ea2f8190ad6d8f"
                or old_phase.get("projection_digest") != "39d09af2c64eae5f81b4f83505383eb05902cf1f794e2612786a04892b7b6b4b"
                or old_phase.get("input_sha256") != "ef0e7f1ab2963050b046060ac088d43513c871a60b33f1329279a4061a7a3b56"
                or old_phase.get("full_payload_digest") != "559c03f2846706675146695d5c30cd4670a51b2039b113e57756dbe9dd9cf6a5"
                or old_phase.get("budget_input_digest") != "7742082f7e399a3be58bcebbb66123d4447b7c2cd0f658b83b82ee72977f2a20"
                or old_phase.get("reservation_id") != "bud_fbec046b65054a33a1c132ad8ed2fd32"
                or not isinstance(old_aggregate, dict) or not old_aggregate.get("checkpoint_name")
                or not old_aggregate.get("checkpoint_digest")):
            raise FactoryError("original phase or aggregate checkpoint binding differs", "evidence_grant_binding", 409)
        required = ("payload", "input_sha256", "full_payload_digest", "budget_input_digest",
                    "prompt", "prompt_sha256", "source_tree_digest", "projection_digest",
                    "stage_name", "logical_retry_scope", "operation", "requested_model",
                    "cli_config_identity")
        if any(key not in phase for key in required):
            raise FactoryError("evidence recovery phase binding is incomplete", "evidence_grant_binding", 409)
        if (phase.get("logical_retry_scope") != RETRY_SCOPE or phase.get("stage_name") != STAGE_NAME
                or phase.get("requested_model") != REQUESTED_MODEL
                or phase.get("operation") != STAGE_NAME + ":" + phase.get("budget_input_digest", "")[:16]
                or digest(phase.get("payload")) != phase.get("full_payload_digest")
                or digest({key: value for key, value in phase["payload"].items() if key != "language"}) != phase.get("budget_input_digest")
                or hashlib.sha256(phase.get("prompt", "").encode("utf-8")).hexdigest() != phase.get("prompt_sha256")
                or phase.get("source_tree_digest") != phase.get("projection_digest")
                or not isinstance(phase.get("cli_config_identity"), dict)):
            raise FactoryError("evidence recovery phase scope differs", "evidence_grant_binding", 409)
        reuse_checks = materials.get("reuse_checks")
        if not isinstance(reuse_checks, dict) or len(reuse_checks) != 5 or any(
            not isinstance(item, dict) or item.get("identical") is not True for item in reuse_checks.values()
        ):
            raise FactoryError("all five reused dimensions must retain their original identity", "evidence_grant_binding", 409)
        source_gate = proposal.get("source_gate")
        if (not isinstance(source_gate, dict) or not source_gate.get("source_commit")
                or not source_gate.get("source_tree_digest")
                or not isinstance(source_gate.get("ci_evidence"), list)
                or not source_gate["ci_evidence"]):
            raise FactoryError("evidence recovery CI source gate is incomplete", "evidence_grant_binding", 409)
        if proposal.get("source_gate_passed") is not True:
            raise FactoryError("evidence recovery source gate is not satisfied", "evidence_grant_binding", 409)
        if any(not isinstance(item, dict) or not all(item.get(key) for key in
               ("path", "sha256", "run_id", "head_sha", "required_checks"))
               for item in source_gate["ci_evidence"]):
            raise FactoryError("evidence recovery CI evidence entry is incomplete", "evidence_grant_binding", 409)
        self._verify_source_gate(proposal)
        return request_key, binding, phase

    @staticmethod
    def _record(row):
        result = dict(row)
        try:
            result["proposal"] = json.loads(result.pop("request_json"))
        except (ValueError, TypeError):
            raise FactoryError("stored evidence grant is corrupt", "evidence_grant_corrupt", 500)
        return result

    def register(self, prepared_proposal, request):
        # Exact retries are a receipt lookup, not a fresh authorization
        # attempt. They must remain replayable after recovery changes the job
        # state or the authorization deadline passes. Validate the immutable
        # proposal bytes/key first, then return an exact stored proposal before
        # consulting any time-sensitive baseline.
        if not isinstance(prepared_proposal, dict) or prepared_proposal.get("schema") != SCHEMA:
            raise FactoryError("unsupported evidence recovery proposal schema", "evidence_grant_schema", 400)
        request_key = prepared_proposal.get("request_key")
        supplied_key = request.get("request_key", request.get("idempotency_key")) if isinstance(request, dict) else None
        if not isinstance(request_key, str) or not request_key or supplied_key != request_key:
            raise FactoryError("request key differs from the prepared proposal", "evidence_grant_binding", 403)
        if prepared_proposal.get("proposal_digest") != self._proposal_digest(prepared_proposal):
            raise FactoryError("evidence recovery proposal digest does not match", "evidence_grant_binding", 409)
        encoded = json.dumps(prepared_proposal, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self.store.connect(True) as con:
            self.initialize_locked(con)
            existing = con.execute(
                "SELECT * FROM tf_evidence_recovery_grant WHERE campaign_id=? AND request_key=?",
                (CAMPAIGN_ID, request_key),
            ).fetchone()
            if existing:
                record = self._record(existing)
                if (record["proposal_digest"] != prepared_proposal["proposal_digest"]
                        or record["proposal"] != prepared_proposal):
                    raise FactoryError("request key was already used for a different proposal", "evidence_grant_conflict", 409)
                return record
        request_key, binding, _ = self._validate_proposal(prepared_proposal, request)
        with self.store.connect(True) as con:
            self.initialize_locked(con)
            # Another registration may have committed while the full fixed
            # baseline and source gate were being rechecked.
            existing = con.execute(
                "SELECT * FROM tf_evidence_recovery_grant WHERE campaign_id=? AND request_key=?",
                (CAMPAIGN_ID, request_key),
            ).fetchone()
            if existing:
                record = self._record(existing)
                if (record["proposal_digest"] != prepared_proposal["proposal_digest"]
                        or record["proposal"] != prepared_proposal):
                    raise FactoryError("request key was already used for a different proposal", "evidence_grant_conflict", 409)
                return record
            prior = con.execute(
                "SELECT 1 FROM tf_evidence_recovery_grant WHERE campaign_id=? AND job_id=?",
                (CAMPAIGN_ID, JOB_ID),
            ).fetchone()
            if prior:
                raise FactoryError("this failed job already has an evidence recovery grant", "evidence_grant_conflict", 409)
            self._verify_budget_baseline_locked(con)
            grant_id = "egrant_" + uuid.uuid4().hex
            now = float(self.clock())
            con.execute(
                "INSERT INTO tf_evidence_recovery_grant(id,campaign_id,product_id,plan_id,job_id,request_key,proposal_digest,request_json,status,created_at) VALUES(?,?,?,?,?,?,?,?,'registered',?)",
                (grant_id, CAMPAIGN_ID, PRODUCT_ID, PLAN_ID, JOB_ID, request_key,
                 prepared_proposal["proposal_digest"], encoded, now),
            )
            return self._record(con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone())

    def get(self, grant_id):
        with self.store.connect() as con:
            row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()
        if row is None:
            raise FactoryError("evidence recovery grant not found", "evidence_grant_missing", 404)
        return self._record(row)

    @classmethod
    def validate_locked(cls, con, grant_id, proposal, request_key, job_id=None):
        row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()
        if row is None:
            raise FactoryError("evidence recovery grant not found", "evidence_grant_missing", 404)
        if row["status"] not in {"registered", "queued"}:
            raise FactoryError("evidence recovery grant has already been occupied", "evidence_grant_used", 409)
        stored = json.loads(row["request_json"])
        if (row["request_key"] != request_key or stored != proposal
                or row["proposal_digest"] != proposal.get("proposal_digest")
                or (job_id is not None and row["job_id"] != job_id)):
            raise FactoryError("evidence recovery grant binding differs", "evidence_grant_binding", 409)
        return cls._record(row)

    @classmethod
    def queue_locked(cls, con, grant_id, proposal, request_key, job_id):
        record = cls.validate_locked(con, grant_id, proposal, request_key, job_id)
        if record["status"] == "queued":
            if record.get("queued_job_id") != job_id:
                raise FactoryError("evidence grant is queued for another job", "evidence_grant_binding", 409)
            return record
        con.execute("UPDATE tf_evidence_recovery_grant SET status='queued',queued_job_id=? WHERE id=? AND status='registered'",
                    (job_id, grant_id))
        return cls._record(con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone())

    @classmethod
    def occupy_locked(cls, con, grant_id, context, reservation_id, now, *, campaign_id, identity, plan_id, job_id, phase, stage, retry, retry_scope, requested_model, kind, deadline):
        row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()
        if row is None:
            raise FactoryError("evidence recovery grant not found", "evidence_grant_missing", 404)
        if row["status"] != "queued" or row["queued_job_id"] != job_id:
            raise FactoryError("evidence recovery grant is not available for this queued job", "evidence_grant_used", 409)
        proposal = json.loads(row["request_json"])
        materials = proposal["materials"]
        binding = materials["binding"]
        expected_phase = materials["new_phase"]
        owner = con.execute("SELECT state,attempt FROM job WHERE id=?", (job_id,)).fetchone()
        if (campaign_id != CAMPAIGN_ID or identity != PRODUCT_ID or plan_id != PLAN_ID
                or job_id != JOB_ID or phase != "G1" or retry != 1
                or retry_scope != RETRY_SCOPE or kind != "review"
                or str(stage) != str(expected_phase["operation"])
                or requested_model != REQUESTED_MODEL
                or owner is None or owner["state"] != "running" or owner["attempt"] < 2
                or binding.get("deadline") != OLD_DEADLINE
                or float(deadline) != OLD_DEADLINE or float(now) >= OLD_DEADLINE):
            raise FactoryError("call identity does not match the evidence grant", "evidence_grant_binding", 409)
        if not isinstance(context, dict):
            raise FactoryError("evidence call context is required", "evidence_grant_binding", 409)
        # Keep independent digest names independent: full payload and raw input
        # file hashes are not interchangeable with the budget-normalized digest.
        context_fields = ("input_digest", "input_sha256", "full_payload_digest", "budget_input_digest",
                          "prompt_sha256", "source_tree_digest", "projection_digest", "stage_name",
                          "logical_retry_scope", "operation")
        for key in context_fields:
            expected = expected_phase.get(key)
            actual = context.get(key)
            if key == "input_digest":
                expected = expected_phase.get("budget_input_digest")
            if actual != expected:
                raise FactoryError("evidence call payload, prompt, source or projection differs", "evidence_grant_binding", 409)
        con.execute("UPDATE tf_evidence_recovery_grant SET status='reserved',consumed_reservation_id=?,call_attempt=? WHERE id=? AND status='queued'",
                    (reservation_id, owner["attempt"], grant_id))
        return {"id": grant_id, "proposal_digest": row["proposal_digest"], "reservation_id": reservation_id,
                "request_key": row["request_key"], "deadline": binding["deadline"],
                "call_attempt": owner["attempt"], "reserved_at": now}

