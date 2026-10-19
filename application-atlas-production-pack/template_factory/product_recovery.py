"""Narrow, transactional supersession for the authorized paused G1 product job."""
from __future__ import annotations

import json
import time

from .budget import BudgetAmendmentService, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT
from .budget import BudgetLedger
from .store import FactoryError, canonical, digest, now

G1_AGGREGATE_EDIT_PATHS = (
    "acceptance/p0_library.py", "acceptance/p0_organize.py",
    "acceptance/p0_find_open.py", "acceptance/p0_recovery.py",
    "acceptance/README.md",
)
G1_OLD_JOB_ID = "job_4f30d0f41ce94a2cbd16ae7996fb27ab"
G1_OLD_ARTIFACT_ID = "tpl_7f4c17e834c342e7b462e6bb8b6379e4"
G1_OLD_ARTIFACT_DIGEST = "8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9"
G1_OLD_JOB_STAGE = "blueprint-spec-review-0-runtime_protocol-v1"
G1_AGGREGATE_REPAIR_SCOPE_DIGEST = "fd3746d6580f6e6bc82f88a7590a91ce7017a8e4402e5efe4ef1ec81d8bdf75b"


class ProductRecoveryService:
    def __init__(self, store, *, clock=time.time):
        self.store, self.clock = store, clock
        with store.connect(True) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tf_job_supersession(old_job_id TEXT PRIMARY KEY, successor_job_id TEXT NOT NULL UNIQUE, plan_id TEXT NOT NULL, reason TEXT NOT NULL, old_state TEXT NOT NULL, old_error TEXT, old_stage TEXT NOT NULL, old_attempt INTEGER NOT NULL, old_updated_at TEXT NOT NULL, created_at TEXT NOT NULL)")
            con.execute("CREATE TABLE IF NOT EXISTS tf_product_resume(plan_id TEXT NOT NULL, old_job_id TEXT NOT NULL, idempotency_key TEXT NOT NULL, request_digest TEXT NOT NULL, amendment_id TEXT NOT NULL, successor_batch_id TEXT NOT NULL, successor_job_id TEXT NOT NULL, created_at TEXT NOT NULL, PRIMARY KEY(plan_id,old_job_id), UNIQUE(idempotency_key))")

    def resume_product(self, plan_id, request):
        from .cognition import queue_repair
        from .v1_batches import BatchService

        if not isinstance(request, dict):
            raise FactoryError("resume request must be an object", "resume_request_invalid", 400)
        required = ("old_job_id", "artifact_id", "expected_digest", "checkpoint_name", "checkpoint_digest", "amendment_id", "idempotency_key", "repair")
        if any(not isinstance(request.get(k), str) or not request[k].strip() for k in required[:-1]) or not isinstance(request.get("repair"), dict):
            raise FactoryError("resume request is missing its scoped candidate, checkpoint or repair request", "resume_request_invalid", 400)
        if plan_id != G1_AMENDMENT_PLAN:
            raise FactoryError("product resume is limited to the authorized G1 plan", "resume_scope", 403)
        plan = BatchService(self.store).plan(plan_id)
        product_seeds = [seed for seed in plan.get("seeds", []) if seed.get("product_id") == G1_AMENDMENT_PRODUCT]
        if plan.get("campaign_id") != G1_AMENDMENT_CAMPAIGN or plan.get("segment") != "G1" or len(product_seeds) != 1:
            raise FactoryError("fixed G1 plan does not contain the authorized product", "resume_scope", 409)
        if request["artifact_id"][:4] != "tpl_" or request["expected_digest"] != request["repair"].get("expected_digest"):
            raise FactoryError("repair request must bind the selected frozen candidate", "resume_request_invalid", 400)
        if (request["old_job_id"] != G1_OLD_JOB_ID or request["artifact_id"] != G1_OLD_ARTIFACT_ID
                or request["expected_digest"] != G1_OLD_ARTIFACT_DIGEST):
            raise FactoryError("first G1 continuation must bind the exact paused baseline job and frozen candidate", "resume_baseline_mismatch", 409)
        artifact = next((item for item in self.store.artifacts() if item.get("id") == request["artifact_id"]), None)
        v1 = (artifact or {}).get("provenance", {}).get("v1", {})
        if (not artifact or artifact.get("digest") != request["expected_digest"]
                or v1.get("campaign_id") != G1_AMENDMENT_CAMPAIGN
                or v1.get("plan_id") != plan_id or v1.get("product_id") != G1_AMENDMENT_PRODUCT):
            raise FactoryError("candidate artifact is not the pinned product revision", "resume_candidate_mismatch", 409)
        repair = request["repair"]
        if (repair.get("reuse_spec") is not False or repair.get("spec_edit_paths") is not None
                or repair.get("edit_paths") != list(G1_AGGREGATE_EDIT_PATHS)):
            raise FactoryError("product resume requires the fixed five-file aggregate repair scope", "contract_scope_invalid", 409)
        from .api import controlled_path
        from .blueprints import verify_frozen
        from .contract_scope import REPAIR_SCOPE_VERSION, validate_repair_scope
        if not isinstance(repair.get("repair_scope"), dict) or repair["repair_scope"].get("version") != REPAIR_SCOPE_VERSION:
            raise FactoryError("product resume requires the current versioned aggregate repair scope", "contract_scope_invalid", 409)
        if digest(repair["repair_scope"]) != G1_AGGREGATE_REPAIR_SCOPE_DIGEST:
            raise FactoryError("product resume repair scope differs from the authorized aggregate scope", "contract_scope_invalid", 409)
        spec = verify_frozen(controlled_path(self.store, artifact["bundle_path"]), artifact["digest"])
        validate_repair_scope(repair["repair_scope"], spec, repair["edit_paths"])
        if not request["checkpoint_name"] or len(request["checkpoint_name"]) > 200:
            raise FactoryError("checkpoint name is invalid", "resume_request_invalid", 400)
        request_digest = digest({key: value for key, value in request.items() if key != "idempotency_key"})
        at = now()
        amendment_service = BudgetAmendmentService(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=self.clock)
        ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN)
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM tf_product_resume WHERE plan_id=? AND old_job_id=?", (plan_id, request["old_job_id"])).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["idempotency_key"] != request["idempotency_key"]:
                    raise FactoryError("paused job already has a different successor", "resume_conflict", 409)
                return self._result(prior, replay=True)
            reused_key = con.execute("SELECT request_digest FROM tf_product_resume WHERE idempotency_key=?", (request["idempotency_key"],)).fetchone()
            if reused_key:
                raise FactoryError("idempotency key was already used for a different recovery", "idempotency_conflict", 409)
            row = con.execute("SELECT * FROM job WHERE id=?", (request["old_job_id"],)).fetchone()
            if not row:
                raise FactoryError("paused G1 job not found", "not_found", 404)
            old_snapshot = json.loads(row["snapshot"])
            old_v1 = old_snapshot.get("v1", {})
            old_repair = old_snapshot.get("cognitive_repair", {})
            if (row["state"] != "paused_budget" or old_v1.get("campaign_id") != G1_AMENDMENT_CAMPAIGN
                    or old_v1.get("plan_id") != plan_id or old_v1.get("product_id") != G1_AMENDMENT_PRODUCT
                    or row["stage"] != G1_OLD_JOB_STAGE
                    or old_repair.get("id") != G1_OLD_ARTIFACT_ID
                    or old_repair.get("digest") != G1_OLD_ARTIFACT_DIGEST):
                raise FactoryError("only the matching paused_budget product job can be superseded", "resume_old_job_invalid", 409)
            fixed_scenario = product_seeds[0].get("scenario") or {}
            old_scenario = old_snapshot.get("scenario") or {}
            artifact_scenario = (artifact.get("provenance", {}).get("scenario") or {})
            def scene_key(value):
                return (value.get("id"), value.get("revision"))
            if (scene_key(fixed_scenario) != scene_key(old_scenario)
                    or scene_key(fixed_scenario) != scene_key(artifact_scenario)):
                raise FactoryError("candidate, paused job and fixed plan scenario do not match", "resume_scenario_mismatch", 409)
            old_basis = old_snapshot.get("case_basis")
            artifact_basis = artifact.get("provenance", {}).get("case_basis")
            if (not isinstance(old_basis, dict) or not isinstance(artifact_basis, dict)
                    or old_basis != artifact_basis
                    or (product_seeds[0].get("case_basis") and product_seeds[0]["case_basis"] != artifact_basis)):
                raise FactoryError("candidate, paused job and fixed plan case basis do not match", "resume_case_basis_mismatch", 409)
            checkpoint = con.execute("SELECT body FROM checkpoint WHERE job_id=? AND name=?", (row["id"], request["checkpoint_name"])).fetchone()
            if not checkpoint or digest(json.loads(checkpoint["body"])) != request["checkpoint_digest"]:
                raise FactoryError("requested checkpoint is missing or changed", "checkpoint_changed", 409)
            execution = con.execute("SELECT batch_id FROM v1_execution WHERE plan_id=?", (plan_id,)).fetchone()
            if not execution:
                raise FactoryError("G1 plan has no active execution", "not_started", 409)
            parent = con.execute("SELECT state FROM batch WHERE id=?", (execution[0],)).fetchone()
            if not parent or parent[0] == "cancelled":
                raise FactoryError("cancelled or missing G1 parent cannot resume", "resume_parent_invalid", 409)
            # Visible only after commit; any successor creation or ledger failure
            # rolls this first activation back with the surrounding transaction.
            active_amendment = amendment_service.activate_locked(con, request["amendment_id"])
            if active_amendment["new_deadline"] is None or float(self.clock()) >= active_amendment["new_deadline"]:
                raise FactoryError("authorized G1 supplemental window has expired", "budget_deadline", 409)
            queued = queue_repair(self.store, artifact, request["repair"], con=con,
                                  parent_state_override="running", ledger=ledger)
            successor_batch_id, successor_job_id = queued["batch_id"], queued["job_id"]
            if not successor_job_id or successor_job_id == row["id"]:
                raise FactoryError("successor job was not created", "resume_successor_invalid", 409)
            successor = con.execute("SELECT snapshot FROM job WHERE id=?", (successor_job_id,)).fetchone()
            successor_snapshot = json.loads(successor["snapshot"])
            successor_snapshot["formal_resume_checkpoint"] = {
                "old_job_id": row["id"], "name": request["checkpoint_name"],
                "digest": request["checkpoint_digest"],
            }
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(successor_snapshot), successor_job_id))
            # Revoke the old attempt's token before making the new queue runnable.
            reason = "Superseded by " + successor_job_id + " under authorized G1 product recovery"
            superseded = con.execute("UPDATE job SET state='cancelled',token=NULL,lease=NULL,updated_at=? WHERE id=? AND state='paused_budget'",
                                     (at, row["id"]))
            if superseded.rowcount != 1:
                raise FactoryError("old job changed during recovery", "resume_old_job_invalid", 409)
            con.execute("INSERT INTO tf_job_supersession VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (row["id"], successor_job_id, plan_id, reason, row["state"], row["error"], row["stage"], row["attempt"], row["updated_at"], at))
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (row["id"], row["attempt"], at, "superseded", reason))
            con.execute("INSERT INTO tf_product_resume VALUES(?,?,?,?,?,?,?,?)",
                        (plan_id, row["id"], request["idempotency_key"], request_digest, request["amendment_id"], successor_batch_id, successor_job_id, at))
            batch_ids = {execution[0]}
            batch_ids.update(item[0] for item in con.execute("SELECT DISTINCT batch_id FROM job WHERE json_extract(snapshot,'$.v1.plan_id')=?", (plan_id,)))
            placeholders = ",".join("?" for _ in batch_ids)
            con.execute(f"UPDATE batch SET state='running' WHERE id IN ({placeholders}) AND state='paused'", tuple(sorted(batch_ids)))
            record = con.execute("SELECT * FROM tf_product_resume WHERE plan_id=? AND old_job_id=?", (plan_id, row["id"])).fetchone()
        return self._result(record, replay=False)

    @staticmethod
    def _result(row, *, replay):
        return {"plan_id": row["plan_id"], "old_job_id": row["old_job_id"],
                "successor_batch_id": row["successor_batch_id"], "successor_job_id": row["successor_job_id"],
                "amendment_id": row["amendment_id"], "replayed": replay}
