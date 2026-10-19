"""Durable, conservative model-call accounting for factory campaigns."""

from __future__ import annotations

import json
import re
import time
import uuid

from .store import FactoryError


DEFAULT_LIMITS = {
    "cli_sessions": 500,
    "production_concurrency": 2,
    "runtime_concurrency": 1,
    "product_repairs": 2,
    "transient_retries": 2,
    "phase_seconds": 8 * 60 * 60,
}

G1_AMENDMENT_CAMPAIGN = "atlas-v1-first-production-2026-10-19"
G1_AMENDMENT_PRODUCT = "product-c42848f63251507bd9d911a5"
G1_AMENDMENT_PLAN = "plan_87059846caf345d2b2fe690657cf324f"
G1_AMENDMENT_OLD_DEADLINE = 1792418554.633465
G1_AMENDMENT_WINDOW_SECONDS = 8 * 60 * 60
G1_AUTHORIZATION_SOURCE_DIGEST = "cc3df91f60afad1a2bf4e862e534be36cb8fcc1f2b8d07687995b325fa7841ae"


def _legacy_retry_scope(stage):
    """Map historical indexed stage names to today's stable retry scopes."""
    base = str(stage or "").split(":", 1)[0]
    match = re.fullmatch(r"blueprint-spec-review-\d+-(.+?)(?:-v1)?", base)
    if match:
        return "blueprint-spec-review:" + match.group(1)
    if base.startswith("blueprint-code-"):
        return "blueprint-code"
    if base.startswith("blueprint-generate-research-repair-") or base.startswith("blueprint-research"):
        return "blueprint-research"
    if base.startswith("blueprint-generate-"):
        return "blueprint-generate"
    if base.startswith("cognitive-review-reference-repair"):
        return "cognitive-review"
    if base.startswith("p0-delivery"):
        return "p0-delivery"
    return base


class BudgetLedger:
    """Campaign-shared ledger stored alongside FactoryStore's SQLite data.

    ``identity`` is a stable business/product identifier, never a job id.
    Reservations are durable before a process is spawned. A reservation whose
    start status is unknown remains charged until explicitly resolved.
    """

    def __init__(self, store, *, campaign_id="default", limits=None, clock=time.time):
        self.store = store
        self.campaign_id = str(campaign_id)
        self.clock = clock
        self.limits = {key: min(value, (limits or {}).get(key, value)) for key, value in DEFAULT_LIMITS.items()}
        for key, value in self.limits.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{key} must be positive")
        statements = (
            "CREATE TABLE IF NOT EXISTS tf_budget_phase (campaign_id TEXT NOT NULL, identity TEXT NOT NULL, phase TEXT NOT NULL, started REAL NOT NULL, deadline REAL NOT NULL, PRIMARY KEY(campaign_id, identity, phase))",
            "CREATE TABLE IF NOT EXISTS tf_budget_reservation (id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, identity TEXT NOT NULL, phase TEXT NOT NULL, kind TEXT NOT NULL, status TEXT NOT NULL, created REAL NOT NULL, started REAL, finished REAL, job_id TEXT, requested_model TEXT, requested_effort TEXT, stage TEXT, retry INTEGER, observed_model TEXT, observed_effort TEXT, outcome TEXT, group_kind TEXT NOT NULL DEFAULT 'production')",
            "CREATE INDEX IF NOT EXISTS tf_budget_campaign_status ON tf_budget_reservation(campaign_id,status)",
            "CREATE INDEX IF NOT EXISTS tf_budget_identity_kind ON tf_budget_reservation(campaign_id,identity,kind,status)",
            "CREATE TABLE IF NOT EXISTS tf_budget_campaign (campaign_id TEXT PRIMARY KEY, limits_json TEXT NOT NULL)",
            "CREATE TABLE IF NOT EXISTS tf_budget_control (campaign_id TEXT PRIMARY KEY, paused INTEGER NOT NULL DEFAULT 0, paused_at REAL, pause_reason TEXT, updated_at REAL NOT NULL)",
            "CREATE TABLE IF NOT EXISTS tf_budget_repair (campaign_id TEXT NOT NULL, product_id TEXT NOT NULL, operation_key TEXT NOT NULL, created REAL NOT NULL, PRIMARY KEY(campaign_id, product_id, operation_key))",
            "CREATE INDEX IF NOT EXISTS tf_budget_repair_product ON tf_budget_repair(campaign_id,product_id)",
            "CREATE TABLE IF NOT EXISTS tf_budget_amendment (id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, product_id TEXT NOT NULL, plan_id TEXT NOT NULL, source_ref TEXT NOT NULL, source_digest TEXT NOT NULL, summary TEXT NOT NULL, reason TEXT NOT NULL, idempotency_key TEXT NOT NULL, version INTEGER NOT NULL, old_repair_limit INTEGER NOT NULL, new_repair_limit INTEGER NOT NULL, baseline_repair_count INTEGER NOT NULL, baseline_cli_sessions INTEGER NOT NULL, old_deadline REAL NOT NULL, window_seconds INTEGER NOT NULL, created_at REAL NOT NULL, activated_at REAL, new_deadline REAL, UNIQUE(campaign_id,product_id,idempotency_key))",
        )
        with store.connect(True) as con:
            for statement in statements:
                con.execute(statement)
            reservation_columns = {row[1] for row in con.execute("PRAGMA table_info(tf_budget_reservation)")}
            if "retry_scope" not in reservation_columns:
                con.execute("ALTER TABLE tf_budget_reservation ADD COLUMN retry_scope TEXT")
            row = con.execute("SELECT limits_json FROM tf_budget_campaign WHERE campaign_id=?", (self.campaign_id,)).fetchone()
            if row:
                recorded = {**DEFAULT_LIMITS, **json.loads(row[0])}
                self.limits = self._minimum_limits(self.limits, recorded)
                con.execute("UPDATE tf_budget_campaign SET limits_json=? WHERE campaign_id=?", (json.dumps(self.limits, sort_keys=True), self.campaign_id))
            else:
                con.execute("INSERT INTO tf_budget_campaign VALUES(?,?)", (self.campaign_id, json.dumps(self.limits, sort_keys=True)))
            con.execute("INSERT OR IGNORE INTO tf_budget_control(campaign_id,paused,updated_at) VALUES(?,0,?)", (self.campaign_id, float(self.clock())))

    @staticmethod
    def _minimum_limits(requested, recorded):
        return {key: min(requested[key], recorded[key]) for key in DEFAULT_LIMITS}

    def _refresh_limits_locked(self, con):
        """Re-read effective campaign limits under the reservation write lock."""
        row = con.execute("SELECT limits_json FROM tf_budget_campaign WHERE campaign_id=?", (self.campaign_id,)).fetchone()
        recorded = {**DEFAULT_LIMITS, **json.loads(row[0])}
        self.limits = self._minimum_limits(self.limits, recorded)
        encoded = json.dumps(self.limits, sort_keys=True)
        if encoded != row[0]:
            con.execute("UPDATE tf_budget_campaign SET limits_json=? WHERE campaign_id=?", (encoded, self.campaign_id))

    def _amendment_locked(self, con, identity, phase="G1", plan_id=None):
        if (self.campaign_id != G1_AMENDMENT_CAMPAIGN or str(phase) != "G1"
                or str(identity) != G1_AMENDMENT_PRODUCT or plan_id != G1_AMENDMENT_PLAN):
            return None
        return con.execute(
            "SELECT * FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND activated_at IS NOT NULL ORDER BY version DESC LIMIT 1",
            (self.campaign_id, str(identity)),
        ).fetchone()

    def begin_segment(self, phase, *, con=None):
        """Start the campaign-wide segment clock once at official queue start."""
        if not phase:
            raise FactoryError("budget segment is required", "budget_identity_required", 400)
        if con is None:
            with self.store.connect(True) as tx:
                return self.begin_segment(phase, con=tx)
        self._refresh_limits_locked(con)
        phase_key = "__campaign_segment__"
        row = con.execute(
            "SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity=? AND phase=?",
            (self.campaign_id, phase_key, str(phase)),
        ).fetchone()
        if row:
            return row[0]
        now = float(self.clock())
        deadline = now + float(self.limits["phase_seconds"])
        con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                    (self.campaign_id, phase_key, str(phase), now, deadline))
        return deadline

    def reserve(self, identity, phase, kind="production", timeout=None, *, job_id=None,
                requested_model=None, requested_effort=None, stage=None, retry=None,
                retry_scope=None, plan_id=None):
        if not identity or not phase:
            raise FactoryError("budget identity and phase are required", "budget_identity_required", 400)
        if kind not in {"production", "runtime", "review", "research", "transient_retry"}:
            raise FactoryError("unknown budget call kind", "budget_kind_invalid", 400)
        if kind == "transient_retry" and retry is None:
            raise FactoryError("transient retries require an explicit retry number", "budget_retry_invalid", 400)
        reservation_id = "bud_" + uuid.uuid4().hex
        with self.store.connect(True) as con:
            self._refresh_limits_locked(con)
            control = con.execute("SELECT paused FROM tf_budget_control WHERE campaign_id=?", (self.campaign_id,)).fetchone()
            if control and control[0]:
                raise FactoryError("campaign budget is paused", "budget_paused", 409)
            deadline = self.begin_segment(phase, con=con)
            amendment = self._amendment_locked(con, identity, phase, plan_id)
            if amendment:
                deadline = amendment["new_deadline"]
            # Sample the clock after obtaining BEGIN IMMEDIATE. A reservation
            # that waited behind another writer must not receive a timeout
            # based on stale time from before the lock.
            now = float(self.clock())
            remaining = deadline - now
            if remaining <= 0:
                raise FactoryError("phase deadline exhausted", "budget_deadline", 409)
            charged = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                (self.campaign_id,),
            ).fetchone()[0]
            if charged >= self.limits["cli_sessions"]:
                raise FactoryError("campaign CLI session budget exhausted", "budget_exhausted", 409)
            active_limit = self.limits["runtime_concurrency"] if kind == "runtime" else self.limits["production_concurrency"]
            group = "runtime" if kind == "runtime" else "production"
            same_group = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND group_kind=? AND status IN ('reserved','started','uncertain')",
                (self.campaign_id, group),
            ).fetchone()[0]
            if same_group >= active_limit:
                raise FactoryError("global model-call concurrency limit reached", "budget_concurrency", 409)
            if retry is not None:
                if (isinstance(retry, bool) or not isinstance(retry, int) or retry < 1
                        or retry > self.limits["transient_retries"]):
                    raise FactoryError("retry must be a positive integer", "budget_retry_invalid", 400)
                scope = str(retry_scope or stage or phase)
                rows = con.execute(
                    "SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                    (self.campaign_id, str(identity)),
                ).fetchall()
                count = sum(
                    1 for row in rows
                    if (row[0] == scope if row[0] is not None else _legacy_retry_scope(row[1]) == scope)
                )
                if count >= self.limits["transient_retries"]:
                    raise FactoryError("transient retry limit exhausted", "budget_retry_limit", 409)
            if retry is None and retry_scope:
                duplicate = con.execute(
                    "SELECT 1 FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND stage=? AND status!='not_started' LIMIT 1",
                    (self.campaign_id, str(identity), str(stage or phase)),
                ).fetchone()
                if duplicate:
                    raise FactoryError("repeated fixed-input call must consume retry budget", "budget_retry_limit", 409)
            con.execute(
                "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,job_id,requested_model,requested_effort,stage,retry,group_kind,retry_scope) VALUES(?,?,?,?,?,'reserved',?,?,?,?,?,?,?,?)",
                (reservation_id, self.campaign_id, str(identity), str(phase), kind, now, job_id,
                 requested_model, requested_effort, stage, retry,
                 "runtime" if kind == "runtime" else "production",
                 str(retry_scope) if retry_scope else None),
            )
        cap = min(float(timeout), remaining) if timeout is not None else remaining
        return {"id": reservation_id, "timeout": max(0.0, cap), "deadline": deadline}

    def record_repair(self, identity, operation_key, *, con=None, plan_id=None):
        """Count a business repair once, independent of job IDs or CLI calls."""
        if not identity or not operation_key:
            raise FactoryError("product identity and repair operation key are required", "budget_repair_identity_required", 400)
        if con is None:
            with self.store.connect(True) as tx:
                return self.record_repair(identity, operation_key, con=tx, plan_id=plan_id)
        self._refresh_limits_locked(con)
        existing = con.execute(
            "SELECT 1 FROM tf_budget_repair WHERE campaign_id=? AND product_id=? AND operation_key=?",
            (self.campaign_id, str(identity), str(operation_key)),
        ).fetchone()
        count = con.execute(
            "SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
            (self.campaign_id, str(identity)),
        ).fetchone()[0]
        if existing:
            amendment = self._amendment_locked(con, identity, plan_id=plan_id)
            repair_limit = amendment["new_repair_limit"] if amendment else self.limits["product_repairs"]
            return {"product_id": str(identity), "repairs_used": count,
                    "repair_limit": repair_limit, "recorded": False}
        amendment = self._amendment_locked(con, identity, plan_id=plan_id)
        repair_limit = amendment["new_repair_limit"] if amendment else self.limits["product_repairs"]
        if count >= repair_limit:
            raise FactoryError("product repair limit exhausted", "budget_repair_limit", 409)
        con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                    (self.campaign_id, str(identity), str(operation_key), float(self.clock())))
        return {"product_id": str(identity), "repairs_used": count + 1,
                "repair_limit": repair_limit, "recorded": True}

    def pause(self, reason="operator_pause"):
        with self.store.connect(True) as con:
            self._refresh_limits_locked(con)
            now = float(self.clock())
            con.execute("UPDATE tf_budget_control SET paused=1,paused_at=?,pause_reason=?,updated_at=? WHERE campaign_id=?",
                        (now, str(reason), now, self.campaign_id))
        return self.snapshot()

    def resume(self):
        with self.store.connect(True) as con:
            self._refresh_limits_locked(con)
            con.execute("UPDATE tf_budget_control SET paused=0,pause_reason=NULL,updated_at=? WHERE campaign_id=?",
                        (float(self.clock()), self.campaign_id))
        return self.snapshot()

    def mark_recovered_unknowns(self, job_ids, *, proof_owned_processes_stopped=False):
        """Free concurrency only with explicit host proof, while retaining charge."""
        if proof_owned_processes_stopped is not True:
            raise FactoryError("host proof that owned processes stopped is required", "budget_recovery_unproved", 409)
        ids = sorted(set(job_ids or []))
        if not ids or any(not isinstance(job_id, str) or not job_id for job_id in ids):
            raise FactoryError("job IDs are required for recovery", "budget_recovery_invalid", 400)
        placeholders = ",".join("?" for _ in ids)
        with self.store.connect(True) as con:
            cur = con.execute(
                f"UPDATE tf_budget_reservation SET status='failed',finished=?,outcome='recovered_after_owned_processes_stopped' WHERE campaign_id=? AND job_id IN ({placeholders}) AND status IN ('reserved','started','uncertain')",
                (float(self.clock()), self.campaign_id, *ids),
            )
        return cur.rowcount

    def _count(self, con, identity, kind):
        return con.execute(
            "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND kind=? AND status!='not_started'",
            (self.campaign_id, str(identity), kind),
        ).fetchone()[0]

    def mark_started(self, reservation_id):
        with self.store.connect(True) as con:
            row = con.execute("SELECT status FROM tf_budget_reservation WHERE id=? AND campaign_id=?",
                              (reservation_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("budget reservation not found", "budget_reservation_missing", 404)
            if row[0] == "reserved":
                con.execute("UPDATE tf_budget_reservation SET status='started',started=? WHERE id=?",
                            (float(self.clock()), reservation_id))

    def finish(self, reservation_id, status="completed", *, observed_model=None,
               observed_effort=None, outcome=None):
        if status not in {"completed", "failed", "uncertain"}:
            raise ValueError("status must be completed, failed, or uncertain")
        with self.store.connect(True) as con:
            row = con.execute("SELECT status FROM tf_budget_reservation WHERE id=? AND campaign_id=?",
                              (reservation_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("budget reservation not found", "budget_reservation_missing", 404)
            # Never erase evidence that a start may have occurred.
            final = "uncertain" if row[0] == "uncertain" else status
            con.execute("UPDATE tf_budget_reservation SET status=?,finished=?,observed_model=?,observed_effort=?,outcome=? WHERE id=?",
                        (final, float(self.clock()), observed_model, observed_effort, outcome, reservation_id))

    def release_not_started(self, reservation_id):
        """Release only when caller has direct evidence subprocess creation failed."""
        with self.store.connect(True) as con:
            cur = con.execute("UPDATE tf_budget_reservation SET status='not_started',finished=? WHERE id=? AND campaign_id=? AND status='reserved'",
                              (float(self.clock()), reservation_id, self.campaign_id))
            if cur.rowcount != 1:
                raise FactoryError("reservation start is not provably absent", "budget_release_denied", 409)

    def phase_remaining(self, identity, phase=None, *, plan_id=None):
        # ``identity`` is retained for older callers; segment deadlines are
        # intentionally campaign-wide rather than product-scoped.
        phase = phase or identity
        with self.store.connect() as con:
            row = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity=? AND phase=?",
                              (self.campaign_id, "__campaign_segment__", str(phase))).fetchone()
            amendment = self._amendment_locked(con, identity, phase, plan_id)
        deadline = amendment["new_deadline"] if amendment else (row[0] if row else None)
        return None if deadline is None else max(0.0, deadline - float(self.clock()))

    def effective_deadline(self, identity, phase="G1", *, plan_id=None):
        with self.store.connect() as con:
            row = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity=? AND phase=?",
                              (self.campaign_id, "__campaign_segment__", str(phase))).fetchone()
            amendment = self._amendment_locked(con, identity, phase, plan_id)
        return amendment["new_deadline"] if amendment else (row[0] if row else None)

    def effective_deadline_snapshot(self, identity, phase="G1", *, plan_id=None, job_id=None):
        with self.store.connect() as con:
            row = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity=? AND phase=?",
                              (self.campaign_id, "__campaign_segment__", str(phase))).fetchone()
            amendment = self._amendment_locked(con, identity, phase, plan_id)
        base_deadline = row["deadline"] if row else None
        deadline = amendment["new_deadline"] if amendment else base_deadline
        return {"schema": "atlas.g1-effective-budget.v1", "binding": {
                    "campaign_id": self.campaign_id, "plan_id": plan_id,
                    "product_id": str(identity), "segment": str(phase), "job_id": job_id},
                "base_started_at": row["started"] if row else None,
                "base_deadline": base_deadline, "effective_deadline": deadline,
                "deadline_source": "amendment" if amendment else "base",
                "amendment_id": amendment["id"] if amendment else None,
                "activated_at": amendment["activated_at"] if amendment else None,
                "new_deadline": amendment["new_deadline"] if amendment else None,
                "generated_at": float(self.clock())}

    def snapshot(self):
        with self.store.connect(True) as con:
            self._refresh_limits_locked(con)
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                  (self.campaign_id,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')",
                                 (self.campaign_id,)).fetchone()[0]
            segments = [dict(r) for r in con.execute("SELECT phase,started,deadline FROM tf_budget_phase WHERE campaign_id=?", (self.campaign_id,))]
            control = con.execute("SELECT paused,paused_at,pause_reason FROM tf_budget_control WHERE campaign_id=?", (self.campaign_id,)).fetchone()
            repairs = [dict(r) for r in con.execute("SELECT product_id,COUNT(*) AS repairs_used FROM tf_budget_repair WHERE campaign_id=? GROUP BY product_id", (self.campaign_id,))]
            amendments = [dict(r) for r in con.execute("SELECT * FROM tf_budget_amendment WHERE campaign_id=? ORDER BY version", (self.campaign_id,))]
        now = float(self.clock())
        for segment in segments:
            segment["remaining_seconds"] = max(0.0, segment["deadline"] - now)
        return {"campaign_id": self.campaign_id, "cli_sessions_used": charged,
                "cli_sessions_limit": self.limits["cli_sessions"], "active": active,
                "limits": dict(self.limits), "segments": segments,
                "paused": bool(control[0]) if control else False,
                "paused_at": control[1] if control else None,
                "pause_reason": control[2] if control else None,
                "repairs": repairs, "amendments": amendments,
                "provider_requests": None, "cost": None}

    status = snapshot


class BudgetAmendmentService:
    """Append-only, narrowly scoped authorization for the booked G1 product."""

    def __init__(self, store, *, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=time.time):
        self.store, self.campaign_id, self.clock = store, str(campaign_id), clock
        # Register/read-only service entry points can be the first code to touch
        # a legacy campaign database. Run the ledger's idempotent schema setup
        # before any amendment-table query; this does not reserve calls or
        # activate an amendment.
        self.ledger = BudgetLedger(store, campaign_id=self.campaign_id, clock=clock)

    def register(self, request):
        required = ("product_id", "plan_id", "source_ref", "source_digest", "summary", "reason", "idempotency_key")
        if not isinstance(request, dict) or any(not isinstance(request.get(k), str) or not request[k].strip() for k in required):
            raise FactoryError("all amendment source, scope and idempotency fields are required", "budget_amendment_invalid", 400)
        if (self.campaign_id != G1_AMENDMENT_CAMPAIGN or request["product_id"] != G1_AMENDMENT_PRODUCT
                or request["plan_id"] != G1_AMENDMENT_PLAN
                or request["source_ref"] != "ATLAS_G1_CONVERGENCE_CODEX_INSTRUCTIONS.txt"
                or request["source_digest"] != G1_AUTHORIZATION_SOURCE_DIGEST):
            raise FactoryError("amendment is outside the authorized campaign, product, plan or source", "budget_amendment_scope", 403)
        if len(request["summary"]) > 2000 or len(request["reason"]) > 1000 or len(request["idempotency_key"]) > 200:
            raise FactoryError("amendment text exceeds limits", "budget_amendment_invalid", 400)
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND idempotency_key=?", (self.campaign_id, request["product_id"], request["idempotency_key"])).fetchone()
            if prior:
                if any(prior[field] != request[field] for field in ("plan_id", "source_ref", "source_digest", "summary", "reason")):
                    raise FactoryError("idempotency key was already used for different authorization", "idempotency_conflict", 409)
                return dict(prior)
            row = con.execute("SELECT COUNT(*) FROM tf_budget_amendment WHERE campaign_id=? AND product_id=?", (self.campaign_id, request["product_id"])).fetchone()
            if row[0]:
                raise FactoryError("the single authorized amendment is already recorded", "budget_amendment_exhausted", 409)
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (self.campaign_id, request["product_id"])).fetchone()[0]
            cli_sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (self.campaign_id,)).fetchone()[0]
            old_deadline = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'", (self.campaign_id,)).fetchone()
            if repairs != 2 or cli_sessions != 42 or not old_deadline or old_deadline[0] != G1_AMENDMENT_OLD_DEADLINE:
                raise FactoryError("existing G1 history does not match amendment basis", "budget_amendment_basis", 409)
            at = float(self.clock())
            amendment_id = "bamd_" + uuid.uuid4().hex
            con.execute("INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,1,2,4,?,?,?,?,?,NULL,NULL)",
                        (amendment_id, self.campaign_id, request["product_id"], request["plan_id"], request["source_ref"], request["source_digest"], request["summary"], request["reason"], request["idempotency_key"], repairs, cli_sessions, G1_AMENDMENT_OLD_DEADLINE, G1_AMENDMENT_WINDOW_SECONDS, at))
            return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate_locked(self, con, amendment_id):
        row = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=?", (amendment_id, self.campaign_id)).fetchone()
        if not row:
            raise FactoryError("budget amendment not found", "not_found", 404)
        if row["activated_at"] is not None:
            return dict(row)
        old = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'", (self.campaign_id,)).fetchone()
        if not old or old[0] != row["old_deadline"]:
            raise FactoryError("original G1 deadline is missing or changed", "budget_amendment_basis", 409)
        at = float(self.clock())
        deadline = max(float(row["old_deadline"]), at + row["window_seconds"])
        con.execute("UPDATE tf_budget_amendment SET activated_at=?,new_deadline=? WHERE id=? AND activated_at IS NULL", (at, deadline, amendment_id))
        return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate(self, amendment_id):
        with self.store.connect(True) as con:
            return self.activate_locked(con, amendment_id)

    def list(self):
        with self.store.connect() as con:
            return [dict(row) for row in con.execute("SELECT * FROM tf_budget_amendment WHERE campaign_id=? ORDER BY version", (self.campaign_id,))]
