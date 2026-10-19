"""Atomic, idempotent activation and queueing for the one authorized G1 R5."""
from __future__ import annotations

import json
import time

from .budget import BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT
from .store import FactoryError, canonical, digest, now

FAILED_JOB = "job_a53c47f3694047489c4f82cfc2e346be"
ARTIFACT = "tpl_7f4c17e834c342e7b462e6bb8b6379e4"
FORMAL_REPAIR_DIGEST = "72991407589cc5cfe950178a7f7ea1dbd0011dad4cd93ca05d77a1956d9a6089"
SOURCE_DIGEST = "4d642929aeccdea2a5b0afb5d92157bc54f7e47871f2a3425b05a35268cc9b73"
QUEUE_KEY = "atlas-g1-r5-prepared-2026-10-19-v1"
INHERITED_DEADLINE = 1792437223.754534


class R5ExecutionService:
    def __init__(self, store, *, clock=time.time):
        self.store, self.clock = store, clock
        # Schema setup precedes the caller-owned business transaction.
        self.amendments = BudgetAmendmentService(store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=clock)
        self.ledger = BudgetLedger(store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=clock)
        with store.connect(True) as con:
            con.execute("CREATE TABLE IF NOT EXISTS tf_g1_r5_execution (plan_id TEXT NOT NULL, old_job_id TEXT NOT NULL, amendment_id TEXT NOT NULL UNIQUE, idempotency_key TEXT NOT NULL UNIQUE, request_digest TEXT NOT NULL, batch_id TEXT NOT NULL, job_id TEXT NOT NULL UNIQUE, created_at TEXT NOT NULL, PRIMARY KEY(plan_id,old_job_id))")
            con.execute("CREATE TABLE IF NOT EXISTS tf_job_supersession(old_job_id TEXT PRIMARY KEY, successor_job_id TEXT NOT NULL UNIQUE, plan_id TEXT NOT NULL, reason TEXT NOT NULL, old_state TEXT NOT NULL, old_error TEXT, old_stage TEXT NOT NULL, old_attempt INTEGER NOT NULL, old_updated_at TEXT NOT NULL, created_at TEXT NOT NULL)")

    def queue(self, plan_id, request):
        from .cognition import queue_repair
        from .v1_batches import BatchService

        if (plan_id != G1_AMENDMENT_PLAN or not isinstance(request, dict)
                or set(request) != {"amendment_id", "idempotency_key", "artifact_id", "repair"}
                or request.get("artifact_id") != ARTIFACT or request.get("idempotency_key") != QUEUE_KEY
                or not isinstance(request.get("amendment_id"), str)
                or digest(request.get("repair")) != FORMAL_REPAIR_DIGEST):
            raise FactoryError("R5 requires its exact authorized plan, artifact, key and prepared repair request", "r5_scope_invalid", 409)
        request_digest = digest(request)
        plan = BatchService(self.store).plan(plan_id)
        artifact = next((a for a in self.store.artifacts() if a["id"] == ARTIFACT), None)
        if not artifact:
            raise FactoryError("R5 frozen baseline artifact is missing", "not_found", 404)
        origin = artifact.get("provenance", {}).get("v1", {})
        if (origin.get("campaign_id") != G1_AMENDMENT_CAMPAIGN or origin.get("plan_id") != plan_id
                or origin.get("product_id") != G1_AMENDMENT_PRODUCT):
            raise FactoryError("R5 artifact is not bound to the authorized original product", "r5_scope_invalid", 409)
        at = now()
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM tf_g1_r5_execution WHERE plan_id=? AND old_job_id=?", (plan_id, FAILED_JOB)).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["idempotency_key"] != request["idempotency_key"]:
                    raise FactoryError("R5 was already queued with a different request", "idempotency_conflict", 409)
                return self._result(prior, True)
            amendment = con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (request["amendment_id"],)).fetchone()
            if (not amendment or amendment["version"] != 2 or amendment["campaign_id"] != G1_AMENDMENT_CAMPAIGN
                    or amendment["product_id"] != G1_AMENDMENT_PRODUCT or amendment["plan_id"] != plan_id
                    or amendment["source_digest"] != SOURCE_DIGEST
                    or amendment["old_repair_limit"] != 4 or amendment["new_repair_limit"] != 5
                    or plan.get("campaign_id") != G1_AMENDMENT_CAMPAIGN or plan.get("segment") != "G1"):
                raise FactoryError("R5 authorization does not match the registered fixed product", "r5_authorization_invalid", 409)
            old = con.execute("SELECT * FROM job WHERE id=?", (FAILED_JOB,)).fetchone()
            if not old or old["state"] != "failed":
                raise FactoryError("R5 source must remain the original failed job", "r5_source_changed", 409)
            if con.execute("SELECT 1 FROM tf_job_supersession WHERE old_job_id=?", (FAILED_JOB,)).fetchone():
                raise FactoryError("R5 failed source already has a different successor", "r5_source_changed", 409)
            execution = con.execute("SELECT batch_id FROM v1_execution WHERE plan_id=?", (plan_id,)).fetchone()
            parent = con.execute("SELECT state FROM batch WHERE id=?", (execution[0],)).fetchone() if execution else None
            if not parent or parent[0] == "cancelled":
                raise FactoryError("G1 parent plan is missing or cancelled", "r5_parent_invalid", 409)
            self.ledger._refresh_limits_locked(con)
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            if charged >= self.ledger.limits["cli_sessions"]:
                raise FactoryError("campaign CLI limit exhausted before R5 queue", "budget_cli_limit", 409)
            active = self.amendments.activate_locked(con, amendment["id"])
            if active["new_deadline"] != INHERITED_DEADLINE or float(self.clock()) >= INHERITED_DEADLINE:
                raise FactoryError("the inherited G1 deadline has expired or changed", "budget_deadline", 409)
            queued = queue_repair(self.store, artifact, request["repair"], con=con, ledger=self.ledger)
            batch_id, job_id = queued["batch_id"], queued["job_id"]
            # queue_repair inherits a paused authoritative parent. Never resume
            # as a side effect of granting a repair; the operator verifies the
            # successor then uses the normal plan resume service.
            row = con.execute("SELECT snapshot FROM job WHERE id=?", (job_id,)).fetchone()
            snapshot = json.loads(row[0])
            snapshot["r5_authorization"] = {"amendment_id": amendment["id"], "source_digest": SOURCE_DIGEST,
                                            "failed_job_id": FAILED_JOB, "queue_request_digest": request_digest,
                                            "effective_deadline": INHERITED_DEADLINE}
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(snapshot), job_id))
            reason = "R5 prepared successor; original failed state/error/checkpoints preserved"
            con.execute("INSERT INTO tf_job_supersession VALUES(?,?,?,?,?,?,?,?,?,?)", (FAILED_JOB, job_id, plan_id, reason, old["state"], old["error"], old["stage"], old["attempt"], old["updated_at"], at))
            con.execute("INSERT INTO tf_g1_r5_execution VALUES(?,?,?,?,?,?,?,?)", (plan_id, FAILED_JOB, amendment["id"], request["idempotency_key"], request_digest, batch_id, job_id, at))
            record = con.execute("SELECT * FROM tf_g1_r5_execution WHERE plan_id=? AND old_job_id=?", (plan_id, FAILED_JOB)).fetchone()
            return self._result(record, False)

    @staticmethod
    def _result(row, replay):
        return {"plan_id": row["plan_id"], "old_job_id": row["old_job_id"], "amendment_id": row["amendment_id"],
                "batch_id": row["batch_id"], "job_id": row["job_id"], "replayed": replay}
