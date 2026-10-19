"""Audited same-job recovery for the one authorized G1 protocol retry."""
from __future__ import annotations

import hashlib
import json
import time
from .store import FactoryError, canonical, digest, now

JOB_ID = "job_7742b1c124be4c9ab3a0096da5cdd772"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"
FAILED_RESERVATION_ID = "bud_1806199dfa08411d8f71ee84ea06676f"
STAGE = "blueprint-spec-review-0-bbc43771a1bbbe99-phase_acceptance"
OPERATION = "blueprint-spec-review-0-bbc43771a1bbbe99-phase_acceptance:449b8a5093505d77"
PROPOSAL_DIGEST = "f190b65275ab7c7136f523ba92aecde7c9392440d7676b070393e62ff9137b58"
CASE_CHOICES_DIGEST = "aaf080ba5261112683c0151f653251c3e6686d66cd156f2aa4dc3f61c68ba0ea"
PROJECTION_DIGEST = "4cf088a2964bca2a1917f50505e675d7c5f580694b88c103c98e15eee250695c"
INPUT_DIGEST = "449b8a5093505d77cf97ec22db4d9f9a952ff15e324a92da140bc93b3b05bd23"
INPUT_SHA256 = "44e258910a36e18c6bae070dbcc6a003c345a7f9623f6f2b474b5de633ed0c97"
STDOUT_SHA256 = "00227a3ec72d61eb677d39174f042078cdff5969d0df248771fa630d57ad1b20"
MODEL = "opencode-go/deepseek-v4.1-flash"
DEADLINE = 1792437223.754534
REUSED_CHECKPOINTS = (
    "blueprint-design-check-0-scenario_scope",
    "blueprint-design-check-0-product_completeness",
    "blueprint-design-check-0-architecture_contract-bbc43771a1bbbe99",
)
CASE_ADAPTATION_CHECKPOINT = "case-adaptation-prepared-aaf080ba52611126"
PLAN_CHECKPOINT = "blueprint-plan-0"
EXPECTED_CHECKPOINT_DIGESTS = {
    "blueprint-design-check-0-scenario_scope": "59985649ce6f23c4ff9fd6492171e7d15d33a1e690eed5c8068a278ce5d60d1a",
    "blueprint-design-check-0-product_completeness": "745beaa813737cb87d90a75a3741b8e9912668019db576ab131b634b4ad05ccc",
    "blueprint-design-check-0-architecture_contract-bbc43771a1bbbe99": "44da0c680aee059eaed95d91c439f7f00870eb354cd7811aa6eceb241eff5ee3",
    "case-adaptation-prepared-aaf080ba52611126": "b49f90a92a4830354af2946a83ab56dcc4f5539f5c085a3c862902f067d253c2",
    "blueprint-plan-0": PROPOSAL_DIGEST,
}
RECOVERY_KEY = "atlas-g1-phase-protocol-resume-2026-10-19-v1"


class ProtocolRecoveryService:
    def __init__(self, store, *, clock=time.time):
        self.store, self.clock = store, clock
        with store.connect(True) as con:
            con.execute("""CREATE TABLE IF NOT EXISTS tf_protocol_recovery (
                job_id TEXT NOT NULL UNIQUE, grant_id TEXT NOT NULL UNIQUE,
                idempotency_key TEXT NOT NULL UNIQUE, request_digest TEXT NOT NULL,
                old_state TEXT NOT NULL, old_error TEXT NOT NULL, old_stage TEXT NOT NULL,
                old_attempt INTEGER NOT NULL, old_updated_at TEXT NOT NULL,
                old_token TEXT, old_lease REAL, snapshot_digest TEXT NOT NULL,
                checkpoint_digest TEXT NOT NULL, checkpoint_names TEXT NOT NULL,
                campaign_id TEXT NOT NULL, plan_id TEXT NOT NULL, product_id TEXT NOT NULL,
                operation TEXT NOT NULL, input_digest TEXT NOT NULL,
                input_sha256 TEXT NOT NULL, stdout_sha256 TEXT NOT NULL,
                created_at TEXT NOT NULL, PRIMARY KEY(job_id))""")

    def recover(self, job_id, request):
        from .protocol_grants import ProtocolRetryGrantService

        if (job_id != JOB_ID or not isinstance(request, dict)
                or set(request) != {"grant_id", "idempotency_key"}
                or not isinstance(request.get("grant_id"), str)
                or request.get("idempotency_key") != RECOVERY_KEY):
            raise FactoryError("protocol recovery requires the fixed job, grant and stable idempotency key", "protocol_recovery_scope", 409)
        request_digest = digest(request)
        # BudgetLedger schema migration must finish before taking the recovery write lock.
        grant_service = ProtocolRetryGrantService(self.store, clock=self.clock)
        # Stable idempotency replay must win over current state checks.
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM tf_protocol_recovery WHERE job_id=?", (job_id,)).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["idempotency_key"] != RECOVERY_KEY:
                    raise FactoryError("this job was already recovered with a different grant or request", "idempotency_conflict", 409)
                return self._result(prior, True)

            grant = con.execute("SELECT * FROM tf_protocol_retry_grant WHERE id=?", (request["grant_id"],)).fetchone()
            if not grant:
                raise FactoryError("protocol retry grant not found", "protocol_grant_not_found", 404)
            job = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            if not job:
                raise FactoryError("protocol recovery job not found", "not_found", 404)
            snapshot = json.loads(job["snapshot"])
            checkpoints = con.execute("SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (job_id,)).fetchall()
            checkpoint_map = {row["name"]: json.loads(row["body"]) for row in checkpoints}
            if (job["state"] != "paused_budget" or job["attempt"] != 2 or job["stage"] != STAGE
                    or job["error"] != "budget_retry_limit: transient retry limit exhausted"):
                raise FactoryError("job no longer matches the authorized paused_budget attempt 2", "protocol_recovery_state", 409)
            v1 = snapshot.get("v1", {})
            if (snapshot.get("config", {}).get("model") != MODEL
                    or v1.get("campaign_id") != CAMPAIGN_ID or v1.get("plan_id") != PLAN_ID
                    or v1.get("product_id") != PRODUCT_ID):
                raise FactoryError("job snapshot differs from the fixed G1 protocol retry binding", "protocol_recovery_binding", 409)
            if not all(name in checkpoint_map for name in EXPECTED_CHECKPOINT_DIGESTS):
                raise FactoryError("required completed design and plan checkpoints are missing", "protocol_recovery_checkpoints", 409)
            expected_dimensions = {
                REUSED_CHECKPOINTS[0]: "scenario_scope",
                REUSED_CHECKPOINTS[1]: "product_completeness",
                REUSED_CHECKPOINTS[2]: "architecture_contract",
            }
            for checkpoint_name, dimension in expected_dimensions.items():
                saved = checkpoint_map[checkpoint_name]
                result = saved.get("result", {})
                checks = result.get("checks", [])
                if (saved.get("digest") != EXPECTED_CHECKPOINT_DIGESTS[checkpoint_name]
                        or saved.get("digest") != digest(result)
                        or result.get("outcome") != "passed" or result.get("proposal_digest") != PROPOSAL_DIGEST
                        or len(checks) != 1 or checks[0].get("dimension") != dimension
                        or checks[0].get("outcome") != "passed"):
                    raise FactoryError("saved design checkpoint is incomplete or differs from the accepted proposal", "protocol_recovery_checkpoints", 409)
            adaptation = checkpoint_map[CASE_ADAPTATION_CHECKPOINT]
            if (adaptation.get("digest") != EXPECTED_CHECKPOINT_DIGESTS[CASE_ADAPTATION_CHECKPOINT]
                    or digest(adaptation.get("result")) != adaptation.get("digest")
                    or digest(adaptation.get("result", {}).get("choices")) != CASE_CHOICES_DIGEST):
                raise FactoryError("prepared case adaptation choices changed", "protocol_recovery_checkpoints", 409)
            if (checkpoint_map[PLAN_CHECKPOINT].get("digest") != PROPOSAL_DIGEST
                    or digest(checkpoint_map[PLAN_CHECKPOINT].get("result")) != PROPOSAL_DIGEST):
                raise FactoryError("prepared blueprint plan digest changed", "protocol_recovery_checkpoints", 409)
            checkpoint_digest = digest({name: checkpoint_map[name] for name in EXPECTED_CHECKPOINT_DIGESTS})
            failure = self._original_failure_evidence(job_id)
            if failure["input_sha256"] != INPUT_SHA256 or failure["stdout_sha256"] != STDOUT_SHA256:
                raise FactoryError("archived attempt-1 protocol evidence does not match the fixed source failure", "protocol_recovery_evidence", 409)
            context = {
                "input_digest": INPUT_DIGEST,
                "input_sha256": failure["input_sha256"],
                "prompt_sha256": json.loads(grant["request_json"])["prompt_sha256"],
                "source_tree_digest": json.loads(grant["request_json"])["source_tree_digest"],
                "projection_digest": PROJECTION_DIGEST,
            }
            grant_service.validate_context(context)
            grant_service.validate_binding_locked(con, grant, context)
            grant_fields = {
                "campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                "job_id": JOB_ID, "source_failure_reservation_id": FAILED_RESERVATION_ID,
                "operation_id": OPERATION, "input_digest": INPUT_DIGEST,
                "input_sha256": INPUT_SHA256, "projection_digest": PROJECTION_DIGEST,
                "proposal_digest": PROPOSAL_DIGEST, "requested_model": MODEL,
                "stdout_sha256": STDOUT_SHA256, "deadline": DEADLINE,
                "logical_retry_scope": "blueprint-spec-review:phase_acceptance",
                "checkpoint_names": ["scenario_scope", "product_completeness", "architecture_contract"],
                "max_extra_calls": 1,
            }
            grant_request = json.loads(grant["request_json"])
            if any(grant_request[key] != value for key, value in grant_fields.items()):
                raise FactoryError("grant fields do not match the fixed paused protocol failure", "protocol_recovery_binding", 409)
            source = con.execute("SELECT * FROM tf_budget_reservation WHERE id=?", (FAILED_RESERVATION_ID,)).fetchone()
            if (not source or source["campaign_id"] != CAMPAIGN_ID or source["identity"] != PRODUCT_ID
                    or source["phase"] != "G1" or source["kind"] != "review" or source["status"] != "failed"
                    or source["job_id"] != JOB_ID or source["stage"] != OPERATION or source["retry"] is not None
                    or source["requested_model"] != MODEL or source["outcome"] != "cli_protocol"):
                raise FactoryError("original attempt-1 reservation no longer proves the fixed CLI protocol failure", "protocol_recovery_evidence", 409)
            if float(self.clock()) >= DEADLINE:
                raise FactoryError("the fixed G1 deadline has expired", "budget_deadline", 409)
            parent = con.execute("SELECT state FROM batch WHERE id=?", (job["batch_id"],)).fetchone()
            if not parent or parent[0] != "paused":
                raise FactoryError("parent plan must remain paused until recovery is verified", "protocol_recovery_parent", 409)

            at = now()
            names = [row["name"] for row in checkpoints]
            con.execute("""INSERT INTO tf_protocol_recovery
                (job_id,grant_id,idempotency_key,request_digest,old_state,old_error,old_stage,old_attempt,
                 old_updated_at,old_token,old_lease,snapshot_digest,checkpoint_digest,checkpoint_names,
                 campaign_id,plan_id,product_id,operation,input_digest,input_sha256,stdout_sha256,created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (job_id, grant["id"], RECOVERY_KEY, request_digest, job["state"], job["error"], job["stage"],
                 job["attempt"], job["updated_at"], job["token"], job["lease"], digest(snapshot), checkpoint_digest,
                 canonical(names), CAMPAIGN_ID, PLAN_ID, PRODUCT_ID, OPERATION, INPUT_DIGEST,
                 failure["input_sha256"], failure["stdout_sha256"], at))
            con.execute("UPDATE job SET state='queued',attempt=3,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=? AND state='paused_budget' AND attempt=2",
                        (at, job_id))
            if con.execute("SELECT changes()").fetchone()[0] != 1:
                raise FactoryError("job changed while protocol recovery was being committed", "protocol_recovery_race", 409)
            record = con.execute("SELECT * FROM tf_protocol_recovery WHERE job_id=?", (job_id,)).fetchone()
            return self._result(record, False)

    def _original_failure_evidence(self, job_id):
        base = self.store.root / "jobs" / job_id / "attempt-1" / STAGE
        input_path, stdout_path = base / "input.json", base / "stdout.log"
        if not input_path.is_file() or not stdout_path.is_file():
            raise FactoryError("original attempt-1 input and stdout must be present for protocol recovery", "protocol_recovery_evidence", 409)
        input_bytes, stdout_bytes = input_path.read_bytes(), stdout_path.read_bytes()
        try:
            payload = json.loads(input_bytes)
        except (ValueError, UnicodeDecodeError) as exc:
            raise FactoryError("original protocol input is not valid JSON", "protocol_recovery_evidence", 409) from exc
        if (payload.get("proposal_digest") != PROPOSAL_DIGEST
                or payload.get("projection_digest") != PROJECTION_DIGEST
                or payload.get("review_dimensions") != ["phase_acceptance"]):
            raise FactoryError("original protocol input differs from the authorized phase input", "protocol_recovery_evidence", 409)
        return {"input_sha256": hashlib.sha256(input_bytes).hexdigest(),
                "stdout_sha256": hashlib.sha256(stdout_bytes).hexdigest()}

    @staticmethod
    def _result(row, replay):
        return {"job_id": row["job_id"], "grant_id": row["grant_id"], "state": "queued",
                "stage": row["old_stage"], "old_attempt": row["old_attempt"],
                "attempt": row["old_attempt"] + 1, "snapshot_digest": row["snapshot_digest"],
                "checkpoint_digest": row["checkpoint_digest"], "replayed": replay}
