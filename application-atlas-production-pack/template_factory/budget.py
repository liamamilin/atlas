"""Durable, conservative model-call accounting for factory campaigns."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path
import re
import time
import uuid

from .store import FactoryError, digest


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
G1_R5_AUTHORIZATION_SCHEMA = "atlas.g1-r5-authorization.v1"
G1_R5_AUTHORIZATION_SOURCE_REF = "docs/template-factory/g1-r5-2026-10-19/authorization/ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt"
G1_R5_AUTHORIZATION_SOURCE_DIGEST = "4d642929aeccdea2a5b0afb5d92157bc54f7e47871f2a3425b05a35268cc9b73"
G1_R5_DEADLINE = 1792437223.754534
G1_R5_BASE_STARTED = 1792389754.633465
G1_R5_BASE_DEADLINE = 1792418554.633465
G1_R5_PREDECESSOR_ID = "bamd_9378738d1e274c409f756d92ec9c2ac5"
G1_R5_FAILED_JOB = "job_a53c47f3694047489c4f82cfc2e346be"
G1_R5_CHECKPOINT = "blueprint-plan-1"
G1_R5_CHECKPOINT_DIGEST = "b82eaafd6126d5e21e1ccd734a590b5e8a417f51497465e72a4574ab20873894"
G1_R5_PREPARED_REQUEST_DIGEST = "10c8b1c4ae25a5a4d5346295da426510aea6d0b2c981b8d8c12df50b660a1e43"
G1_R5_EFFECTIVE_PLAN_DIGEST = "f190b65275ab7c7136f523ba92aecde7c9392440d7676b070393e62ff9137b58"
G1_R5_PATCH_DIGEST = "76673a0a9b28bd52aab8d44208ea58a6764aa78d0d9b541af2ff41e4d237241c"
G1_R5_REPAIR_REQUEST_DIGEST = "72991407589cc5cfe950178a7f7ea1dbd0011dad4cd93ca05d77a1956d9a6089"
G1_R6_AUTHORIZATION_SCHEMA = "atlas.g1-source-alignment-authorization.v1"
G1_R6_AUTHORIZATION_SOURCE_REF = "docs/template-factory/g1-r6-source-alignment-2026-10-20/authorization/ATLAS_G1_R6_SOURCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt"
G1_R6_AUTHORIZATION_SOURCE_DIGEST = "7c36e8048393bf7b3fd7eecc78c3af76e3189d462310d88955ce283dd4ce0168"
G1_R6_PREDECESSOR_ID = "bamd_ad804106fd7049b1b67b914b8e494300"
G1_R6_FAILED_JOB = "job_7742b1c124be4c9ab3a0096da5cdd772"
G1_R6_FAILED_ATTEMPT = 4
G1_R6_FAILED_STAGE = "blueprint-code-0-7"
G1_R6_FAILED_ERROR = "cognition generation failed structural checks: invalid blueprint references: feature sources"
G1_R6_PROTOCOL_GRANT_ID = "pgrant_f3595368c14d4b23b6ab536f6d198007"
G1_R6_PROTOCOL_RESERVATION_ID = "bud_9a81a7a4adc14f49b46239ec68ee2fdb"
G1_R6_OLD_DEADLINE = G1_R5_DEADLINE
G1_R6_WINDOW_SECONDS = 8 * 60 * 60
G1_R6_IDEMPOTENCY_KEY = "atlas-g1-r6-source-alignment-2026-10-20-v1"
G1_R7_AUTHORIZATION_SCHEMA = "atlas.g1-bounded-revision-authorization.v1"
G1_R7_AUTHORIZATION_SOURCE_REF = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt"
G1_R7_AUTHORIZATION_SOURCE_DIGEST = "5fb0792b769739f070f68af6ea196473671c791cd895989026ebf9520e282562"
G1_R7_PREDECESSOR_ID = "bamd_100a302fe8424d9493dafe62d6e43db9"
G1_R7_FAILED_JOB = "job_f3e32b56036b4ec7bea0c00d6a2a8dc4"
G1_R7_FAILED_ATTEMPT = 1
G1_R7_FAILED_STAGE = "aggregate-semantic-review"
G1_R7_OLD_DEADLINE = 1792495312.855422
G1_R7_IDEMPOTENCY_KEY = "atlas-g1-r7-acceptance-alignment-2026-10-20-v1"
G1_R7_EVIDENCE_JOB = "job_3a658ba085e8417ea6faad5cb0cdd493"
G1_R7_EVIDENCE_SCOPE = "blueprint-spec-review:phase_acceptance"
G1_R7_EVIDENCE_STAGE_PREFIX = "blueprint-spec-review-0-ad1379367f3e742a-phase_acceptance"
FROZEN_REVIEW_JOB = "job_b01427592b164863aab5bedf7b3863bb"


def build_r7_authorization_request(store, prepared_request, *, summary, reason,
                                  idempotency_key=G1_R7_IDEMPOTENCY_KEY):
    """Build the fixed R7 authorization from current R6 failure and prepared bytes."""
    from .plan_revision import PreparedRevisionService

    prepared = PreparedRevisionService(store).prepare(G1_R7_FAILED_JOB, prepared_request)
    job = store.job(G1_R7_FAILED_JOB)
    source_path = store.pack.parent / G1_R7_AUTHORIZATION_SOURCE_REF
    source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    return {
        "schema": G1_R7_AUTHORIZATION_SCHEMA,
        "campaign_id": G1_AMENDMENT_CAMPAIGN,
        "product_id": G1_AMENDMENT_PRODUCT,
        "plan_id": G1_AMENDMENT_PLAN,
        "source_ref": G1_R7_AUTHORIZATION_SOURCE_REF,
        "source_digest": source_digest,
        "summary": summary,
        "reason": reason,
        "idempotency_key": idempotency_key,
        "predecessor_amendment_id": G1_R7_PREDECESSOR_ID,
        "old_job_id": G1_R7_FAILED_JOB,
        "old_job_attempt": G1_R7_FAILED_ATTEMPT,
        "old_job_snapshot_digest": digest(job["snapshot"]),
        "old_job_error": job["error"],
        "old_job_stage": G1_R7_FAILED_STAGE,
        "prepared_revision": prepared_request,
        "prepared_revision_digest": prepared.get("request_digest"),
        "effective_plan_digest": prepared.get("effective_plan_digest"),
        "case_design_digest": prepared.get("case_design_digest"),
        "program_revision_digest": digest(prepared.get("prepared_program_revision")),
        "baseline_cli_sessions": 71,
        "baseline_repair_count": 6,
        "baseline_scope_retry_rows": 3,
        "baseline_protocol_grant_uses": 1,
        "baseline_active": 0,
        "old_deadline": G1_R7_OLD_DEADLINE,
    }


def build_r6_authorization_request(store, prepared_request, *, summary, reason,
                                  idempotency_key=G1_R6_IDEMPOTENCY_KEY):
    """Build the fixed, evidence-derived R6 authorization payload for operators."""
    from .plan_revision import PreparedRevisionService
    from .store import digest

    prepared = PreparedRevisionService(store).prepare(G1_R6_FAILED_JOB, prepared_request)
    binding = prepared.get("binding", {})
    job = store.job(G1_R6_FAILED_JOB)
    source_path = store.pack.parent / G1_R6_AUTHORIZATION_SOURCE_REF
    source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    return {
        "schema": G1_R6_AUTHORIZATION_SCHEMA,
        "campaign_id": G1_AMENDMENT_CAMPAIGN,
        "product_id": G1_AMENDMENT_PRODUCT,
        "plan_id": G1_AMENDMENT_PLAN,
        "source_ref": G1_R6_AUTHORIZATION_SOURCE_REF,
        "source_digest": source_digest,
        "summary": summary,
        "reason": reason,
        "idempotency_key": idempotency_key,
        "predecessor_amendment_id": G1_R6_PREDECESSOR_ID,
        "old_job_id": G1_R6_FAILED_JOB,
        "old_job_attempt": G1_R6_FAILED_ATTEMPT,
        "old_job_snapshot_digest": digest(job["snapshot"]),
        "old_job_error": job["error"],
        "old_job_stage": G1_R6_FAILED_STAGE,
        "case_basis_digest": binding.get("case_basis_digest"),
        "facts_view_digest": binding.get("facts_view_digest"),
        "case_design_digest": prepared.get("case_design_digest"),
        "prepared_revision": prepared_request,
        "prepared_revision_digest": prepared.get("request_digest"),
        "effective_plan_digest": prepared.get("effective_plan_digest"),
        "program_manifest_digest": digest(prepared.get("prepared_program_reuse")),
        "protocol_grant_id": G1_R6_PROTOCOL_GRANT_ID,
        "protocol_reservation_id": G1_R6_PROTOCOL_RESERVATION_ID,
        "baseline_cli_sessions": 64,
        "baseline_repair_count": 5,
        "baseline_scope_retry_rows": 3,
        "baseline_active": 0,
        "old_deadline": G1_R6_OLD_DEADLINE,
        "window_seconds": G1_R6_WINDOW_SECONDS,
    }


def _legacy_retry_scope(stage):
    """Map historical indexed stage names to today's stable retry scopes."""
    base = str(stage or "").split(":", 1)[0]
    match = re.fullmatch(r"blueprint-spec-review-\d+-(?:[0-9a-f]{16}-)?(.+?)(?:-[0-9a-f]{16})?(?:-v1)?", base)
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
            "CREATE TABLE IF NOT EXISTS tf_budget_auxiliary_segment (campaign_id TEXT NOT NULL, phase TEXT NOT NULL, identity TEXT NOT NULL, request_json TEXT NOT NULL, request_digest TEXT NOT NULL, max_calls INTEGER NOT NULL, window_seconds INTEGER NOT NULL, model TEXT NOT NULL, PRIMARY KEY(campaign_id,phase))",
            "CREATE TABLE IF NOT EXISTS tf_budget_phase (campaign_id TEXT NOT NULL, identity TEXT NOT NULL, phase TEXT NOT NULL, started REAL NOT NULL, deadline REAL NOT NULL, PRIMARY KEY(campaign_id, identity, phase))",
            "CREATE TABLE IF NOT EXISTS tf_budget_reservation (id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, identity TEXT NOT NULL, phase TEXT NOT NULL, kind TEXT NOT NULL, status TEXT NOT NULL, created REAL NOT NULL, started REAL, finished REAL, job_id TEXT, requested_model TEXT, requested_effort TEXT, stage TEXT, retry INTEGER, observed_model TEXT, observed_effort TEXT, outcome TEXT, group_kind TEXT NOT NULL DEFAULT 'production')",
            "CREATE INDEX IF NOT EXISTS tf_budget_campaign_status ON tf_budget_reservation(campaign_id,status)",
            "CREATE INDEX IF NOT EXISTS tf_budget_identity_kind ON tf_budget_reservation(campaign_id,identity,kind,status)",
            "CREATE TABLE IF NOT EXISTS tf_budget_campaign (campaign_id TEXT PRIMARY KEY, limits_json TEXT NOT NULL)",
            "CREATE TABLE IF NOT EXISTS tf_budget_control (campaign_id TEXT PRIMARY KEY, paused INTEGER NOT NULL DEFAULT 0, paused_at REAL, pause_reason TEXT, updated_at REAL NOT NULL)",
            "CREATE TABLE IF NOT EXISTS tf_budget_repair (campaign_id TEXT NOT NULL, product_id TEXT NOT NULL, operation_key TEXT NOT NULL, created REAL NOT NULL, PRIMARY KEY(campaign_id, product_id, operation_key))",
            "CREATE INDEX IF NOT EXISTS tf_budget_repair_product ON tf_budget_repair(campaign_id,product_id)",
            "CREATE TABLE IF NOT EXISTS tf_budget_amendment (id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, product_id TEXT NOT NULL, plan_id TEXT NOT NULL, source_ref TEXT NOT NULL, source_digest TEXT NOT NULL, summary TEXT NOT NULL, reason TEXT NOT NULL, idempotency_key TEXT NOT NULL, version INTEGER NOT NULL, old_repair_limit INTEGER NOT NULL, new_repair_limit INTEGER NOT NULL, baseline_repair_count INTEGER NOT NULL, baseline_cli_sessions INTEGER NOT NULL, old_deadline REAL NOT NULL, window_seconds INTEGER NOT NULL, created_at REAL NOT NULL, activated_at REAL, new_deadline REAL, UNIQUE(campaign_id,product_id,idempotency_key))",
            "CREATE TABLE IF NOT EXISTS tf_budget_amendment_binding (amendment_id TEXT PRIMARY KEY, request_json TEXT NOT NULL, request_digest TEXT NOT NULL)",
            "CREATE UNIQUE INDEX IF NOT EXISTS tf_budget_amendment_version ON tf_budget_amendment(campaign_id,product_id,version)",
            "CREATE TABLE IF NOT EXISTS tf_protocol_retry_grant (id TEXT PRIMARY KEY, campaign_id TEXT NOT NULL, plan_id TEXT NOT NULL, product_id TEXT NOT NULL, job_id TEXT NOT NULL, source_ref TEXT NOT NULL, source_digest TEXT NOT NULL, request_json TEXT NOT NULL, request_digest TEXT NOT NULL, idempotency_key TEXT NOT NULL, status TEXT NOT NULL, consumed_reservation_id TEXT, created_at REAL NOT NULL, UNIQUE(campaign_id,idempotency_key))",
            "CREATE TABLE IF NOT EXISTS tf_protocol_retry_grant_use (grant_id TEXT NOT NULL, reservation_id TEXT NOT NULL UNIQUE, status TEXT NOT NULL, created_at REAL NOT NULL, released_at REAL, PRIMARY KEY(grant_id,reservation_id))",
            "CREATE UNIQUE INDEX IF NOT EXISTS tf_protocol_retry_grant_one_live_use ON tf_protocol_retry_grant_use(grant_id) WHERE status IN ('reserved','started','uncertain','consumed')",
            "CREATE TABLE IF NOT EXISTS tf_evidence_recovery_grant (id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,plan_id TEXT NOT NULL,job_id TEXT NOT NULL,request_key TEXT NOT NULL,proposal_digest TEXT NOT NULL,request_json TEXT NOT NULL,status TEXT NOT NULL,queued_job_id TEXT,consumed_reservation_id TEXT,call_attempt INTEGER,created_at REAL NOT NULL,UNIQUE(campaign_id,request_key),UNIQUE(campaign_id,job_id))",
            "CREATE TABLE IF NOT EXISTS tf_evidence_recovery_grant_use (grant_id TEXT NOT NULL,reservation_id TEXT NOT NULL UNIQUE,status TEXT NOT NULL,created_at REAL NOT NULL,released_at REAL,call_attempt INTEGER,PRIMARY KEY(grant_id,reservation_id))",
            "CREATE UNIQUE INDEX IF NOT EXISTS tf_evidence_recovery_grant_one_live_use ON tf_evidence_recovery_grant_use(grant_id) WHERE status IN ('reserved','spawn_intent','started','uncertain','consumed')",
        )
        with store.connect(True) as con:
            for statement in statements:
                con.execute(statement)
            from .full_auxiliary import ensure_schema
            ensure_schema(con)
            reservation_columns = {row[1] for row in con.execute("PRAGMA table_info(tf_budget_reservation)")}
            if "retry_scope" not in reservation_columns:
                con.execute("ALTER TABLE tf_budget_reservation ADD COLUMN retry_scope TEXT")
            if "worker_token" not in reservation_columns:
                con.execute("ALTER TABLE tf_budget_reservation ADD COLUMN worker_token TEXT")
            grant_columns = {row[1] for row in con.execute("PRAGMA table_info(tf_evidence_recovery_grant)")}
            if "call_attempt" not in grant_columns:
                con.execute("ALTER TABLE tf_evidence_recovery_grant ADD COLUMN call_attempt INTEGER")
            use_columns = {row[1] for row in con.execute("PRAGMA table_info(tf_evidence_recovery_grant_use)")}
            if "call_attempt" not in use_columns:
                con.execute("ALTER TABLE tf_evidence_recovery_grant_use ADD COLUMN call_attempt INTEGER")
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

    def _time_resume_locked(self, con, identity, phase="G1", plan_id=None):
        if str(phase) != "G1":
            return None
        from .frozen_review_additional import get_time_resume_locked
        return get_time_resume_locked(con, campaign_id=self.campaign_id,
                                      product_id=str(identity), plan_id=plan_id)

    def _effective_timing_locked(self, con, identity, phase="G1", plan_id=None):
        """Resolve one authoritative deadline and its provenance.

        A registered amendment is inert until activation.  An activated
        version 5 may supersede the timing source it explicitly bound; older
        pause/resume rows remain available for accounting and audit.
        """
        phase_row = con.execute(
            "SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity=? AND phase=?",
            (self.campaign_id, "__campaign_segment__", str(phase)),
        ).fetchone()
        base_started = phase_row["started"] if phase_row else None
        base_deadline = phase_row["deadline"] if phase_row else None
        amendment = self._amendment_locked(con, identity, phase, plan_id)
        resume = self._time_resume_locked(con, identity, phase, plan_id)

        if amendment and amendment["version"] == 5:
            binding = con.execute(
                "SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                (amendment["id"],),
            ).fetchone()
            if not binding:
                raise FactoryError("version 5 timing authorization binding is missing", "budget_amendment_basis", 409)
            request = json.loads(binding["request_json"])
            expected = request.get("timing", {}).get("supersedes") if isinstance(request, dict) else None
            if (digest(request) != binding["request_digest"] or not isinstance(expected, dict)
                    or not resume or expected != self._timing_source_snapshot(resume)
                    or amendment["activated_at"] is None
                    or amendment["new_deadline"] != amendment["activated_at"] + amendment["window_seconds"]
                    or request.get("timing", {}).get("window_seconds") != amendment["window_seconds"]):
                raise FactoryError("active amendment no longer supersedes its exact timing source", "budget_amendment_basis", 409)
            return {
                "base_started_at": base_started, "base_deadline": base_deadline,
                "deadline": amendment["new_deadline"],
                "deadline_source": "amendment_superseding_timing",
                "time_resume": dict(resume), "amendment": dict(amendment),
                "supersedes": expected,
            }
        if resume:
            return {"base_started_at": base_started, "base_deadline": base_deadline,
                    "deadline": resume["effective_deadline"],
                    "deadline_source": "authorized_external_pause_resume",
                    "time_resume": dict(resume), "amendment": amendment,
                    "supersedes": None}
        return {"base_started_at": base_started, "base_deadline": base_deadline,
                "deadline": amendment["new_deadline"] if amendment else base_deadline,
                "deadline_source": "amendment" if amendment else "base",
                "time_resume": None, "amendment": dict(amendment) if amendment else None,
                "supersedes": None}

    @staticmethod
    def _timing_source_snapshot(resume):
        return {"deadline_source": "authorized_external_pause_resume",
                "source_id": resume["grant_id"], "activated_at": resume["activated_at"],
                "effective_deadline": resume["effective_deadline"],
                "authorization_digest": resume["authorization_digest"]}

    def register_auxiliary_batch(self, phase, identity, request):
        """Bind one three-leaf auxiliary batch to nine calls; no retry allowance."""
        items = request.get("items", [])
        if (request.get("schema") != "atlas.auxiliary-model-batch.v1"
                or not str(phase).startswith("auxiliary-batch-")
                or request.get("campaign_id") != self.campaign_id
                or request.get("phase") != phase or request.get("identity") != identity
                or request.get("model") != "opencode-go/minimax-m3.1-flash-free"
                or request.get("max_cli_calls") != 9 or request.get("window_seconds") != 28800
                or len(items) != 3 or len({item["leaf"] for item in items}) != 3
                or len({item["key"] for item in items}) != 3
                or any(not item.get("leaf_sha256") or not item.get("scenario") for item in items)
                or not request.get("authorization_sha256")):
            raise FactoryError("invalid auxiliary batch request", "auxiliary_revision_binding", 409)
        return self._register_auxiliary_segment(phase, identity, request, 9, 28800)

    def segment_usage(self, phase):
        """Read this stable segment's charge, independent of other campaigns' work."""
        with self.store.connect() as con:
            rows = [dict(row) for row in con.execute(
                "SELECT id,identity,phase,kind,status,job_id,stage,requested_model,created,started,finished,outcome FROM tf_budget_reservation WHERE campaign_id=? AND phase=? ORDER BY created,id",
                (self.campaign_id, str(phase)))]
        return {"phase": phase, "cli_sessions_used": sum(row["status"] != "not_started" for row in rows),
                "reservations": rows}

    def _register_auxiliary_segment(self, phase, identity, request, max_calls, seconds):
        with self.store.connect(True) as con:
            row = con.execute("SELECT request_digest FROM tf_budget_auxiliary_segment WHERE campaign_id=? AND phase=?",
                              (self.campaign_id, phase)).fetchone()
            if row and row[0] != digest(request):
                raise FactoryError("auxiliary request already bound", "auxiliary_revision_binding", 409)
            if not row:
                if con.execute("SELECT 1 FROM tf_budget_phase WHERE campaign_id=? AND phase=?", (self.campaign_id, phase)).fetchone():
                    raise FactoryError("cannot rebind an existing phase", "auxiliary_revision_binding", 409)
                con.execute("INSERT INTO tf_budget_auxiliary_segment VALUES(?,?,?,?,?,?,?,?)",
                            (self.campaign_id, phase, identity, json.dumps(request, sort_keys=True), digest(request), max_calls, seconds, request["model"]))
        return {"phase": phase, "request_digest": digest(request), "max_cli_calls": max_calls, "window_seconds": seconds}

    def register_auxiliary_revision(self, phase, identity, request):
        """Persist a bounded operator request, without activating its clock.

        This local service does not amend/resume G1 or reset campaign counters.
        Reservations atomically enforce the stable phase cap across all jobs.
        """
        if (not str(phase).startswith("auxiliary-revision-") or not identity
                or request.get("schema") != "atlas.auxiliary-revision-request.v1"
                or request.get("campaign_id") != self.campaign_id
                or request.get("phase") != phase or request.get("identity") != identity
                or request.get("max_cli_calls") != 6 or request.get("window_seconds") != 86400
                or request.get("model") != "opencode-go/deepseek-v4.1-flash"
                or not request.get("authorization_sha256") or not request.get("parent")):
            raise FactoryError("invalid auxiliary revision request", "auxiliary_revision_binding", 409)
        return self._register_auxiliary_segment(phase, identity, request, 6, 86400)

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
        auxiliary = con.execute("SELECT window_seconds FROM tf_budget_auxiliary_segment WHERE campaign_id=? AND phase=?",
                                (self.campaign_id, str(phase))).fetchone()
        full = con.execute("SELECT window_seconds,deadline FROM auxiliary_full_plan WHERE campaign_id=? AND phase=?", (self.campaign_id, str(phase))).fetchone()
        if full and full[1] is None:
            raise FactoryError("full window starts only with controlled reservation", "full_plan_binding",409)
        deadline = float(full[1]) if full else now + float(auxiliary[0] if auxiliary else self.limits["phase_seconds"])
        con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                    (self.campaign_id, phase_key, str(phase), now, deadline))
        return deadline

    def reserve(self, identity, phase, kind="production", timeout=None, *, job_id=None,
                requested_model=None, requested_effort=None, stage=None, retry=None,
                retry_scope=None, plan_id=None, protocol_context=None,
                evidence_recovery_id=None, job_token=None):
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
            from .full_auxiliary import full_reservation_locked
            full = full_reservation_locked(con, self.campaign_id, str(identity), str(phase), plan_id,
                                           requested_model, stage, float(self.clock()), kind=kind)
            auxiliary = con.execute("SELECT * FROM tf_budget_auxiliary_segment WHERE campaign_id=? AND phase=?",
                                    (self.campaign_id, str(phase))).fetchone()
            if str(phase).startswith(("auxiliary-revision-", "auxiliary-batch-")) and not auxiliary:
                raise FactoryError("auxiliary revision must be registered first", "auxiliary_revision_binding", 409)
            if auxiliary:
                used = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND status!='not_started'",
                                   (self.campaign_id, str(phase))).fetchone()[0]
                if str(identity) != auxiliary["identity"] or requested_model != auxiliary["model"]:
                    raise FactoryError("auxiliary revision call binding differs", "auxiliary_revision_binding", 409)
                if used >= auxiliary["max_calls"]:
                    raise FactoryError("auxiliary revision CLI limit exhausted", "budget_exhausted", 409)
            self.begin_segment(phase, con=con)
            timing = self._effective_timing_locked(con, identity, phase, plan_id)
            deadline = timing["deadline"]
            time_resume = timing["time_resume"]
            # Sample the clock after obtaining BEGIN IMMEDIATE. A reservation
            # that waited behind another writer must not receive a timeout
            # based on stale time from before the lock.
            now = float(self.clock())
            remaining = deadline - now
            if remaining <= 0:
                raise FactoryError("phase deadline exhausted", "budget_deadline", 409)
            if job_id == FROZEN_REVIEW_JOB and not time_resume and remaining < 2700:
                raise FactoryError("frozen-review call lacks its required deadline reserve", "budget_deadline", 409)
            if evidence_recovery_id:
                owner = con.execute("SELECT state,token,lease FROM job WHERE id=?", (job_id,)).fetchone()
                if (not job_token or owner is None or owner["state"] != "running"
                        or owner["token"] != job_token or owner["lease"] is None or owner["lease"] <= now):
                    raise FactoryError("evidence review job token or lease is not current", "lease_lost", 409)
            charged = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                (self.campaign_id,),
            ).fetchone()[0]
            # External diagnostics are historical campaign consumption. Keep
            # reading that evidence even after a later amendment supersedes
            # its deadline source.
            campaign_time_resume = self._time_resume_locked(con, G1_AMENDMENT_PRODUCT, "G1", G1_AMENDMENT_PLAN)
            external_sessions = campaign_time_resume["external_cli_sessions"] if campaign_time_resume else 0
            # The new allowance is exclusive to this frozen auxiliary plan.
            # Old grants/limits remain unchanged and cannot borrow its quota.
            ceiling = full["baseline"] + full["max_calls"] if full else self.limits["cli_sessions"]
            if charged + external_sessions >= ceiling:
                raise FactoryError("campaign CLI session budget exhausted", "budget_exhausted", 409)
            active_limit = self.limits["runtime_concurrency"] if kind == "runtime" else self.limits["production_concurrency"]
            group = "runtime" if kind == "runtime" else "production"
            same_group = con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND group_kind=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                (self.campaign_id, group),
            ).fetchone()[0]
            if same_group >= active_limit:
                raise FactoryError("global model-call concurrency limit reached", "budget_concurrency", 409)
            r7_evidence_scope = (
                self.campaign_id == G1_AMENDMENT_CAMPAIGN
                and str(identity) == G1_AMENDMENT_PRODUCT
                and plan_id == G1_AMENDMENT_PLAN
                and job_id == G1_R7_EVIDENCE_JOB
                and str(phase) == "G1"
                and (str(retry_scope or "") == G1_R7_EVIDENCE_SCOPE
                     or _legacy_retry_scope(stage) == G1_R7_EVIDENCE_SCOPE
                     or str(stage or "").startswith(G1_R7_EVIDENCE_STAGE_PREFIX))
            )
            frozen_review_scope = (
                self.campaign_id == G1_AMENDMENT_CAMPAIGN
                and str(identity) == G1_AMENDMENT_PRODUCT
                and plan_id == G1_AMENDMENT_PLAN
                and job_id == FROZEN_REVIEW_JOB
                and str(phase) == "G1"
            )
            if frozen_review_scope and not evidence_recovery_id:
                raise FactoryError("frozen-review job reservations require its exact one-use grant", "evidence_grant_binding", 409)
            if frozen_review_scope and (retry != 1 or kind != "review" or not retry_scope or not stage):
                raise FactoryError("frozen-review grant requires its bound review retry", "evidence_grant_binding", 409)
            if frozen_review_scope and timeout != 1800:
                raise FactoryError("frozen-review grant requires its exact 1800 second timeout", "evidence_grant_binding", 409)
            if r7_evidence_scope:
                if evidence_recovery_id and (
                    str(retry_scope or "") != G1_R7_EVIDENCE_SCOPE
                    or not str(stage or "").startswith(G1_R7_EVIDENCE_STAGE_PREFIX + ":")
                    or retry != 1
                ):
                    raise FactoryError("R7 evidence grant requires the exact phase stage and retry scope", "evidence_grant_binding", 409)
                # The original R7 phase call is already durably recorded. A
                # changed payload/stage cannot turn its authorized successor
                # into retry=None or another apparent first call.
                prior_phase = con.execute(
                    "SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND job_id=? AND status!='not_started'",
                    (self.campaign_id, str(identity), job_id),
                ).fetchall()
                has_prior_phase = any(
                    (row[0] == G1_R7_EVIDENCE_SCOPE if row[0] is not None
                     else _legacy_retry_scope(row[1]) == G1_R7_EVIDENCE_SCOPE)
                    for row in prior_phase
                )
                if has_prior_phase and not evidence_recovery_id:
                    raise FactoryError("R7 phase successor requires its exact evidence recovery grant", "budget_retry_limit", 409)
            protocol_grant = None
            evidence_grant = None
            if retry is not None:
                if (isinstance(retry, bool) or not isinstance(retry, int) or retry < 1
                        or (retry > self.limits["transient_retries"] and not evidence_recovery_id)):
                    raise FactoryError("retry must be a positive integer", "budget_retry_invalid", 400)
                scope = G1_R7_EVIDENCE_SCOPE if r7_evidence_scope else str(retry_scope or stage or phase)
                rows = con.execute(
                    "SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                    (self.campaign_id, str(identity)),
                ).fetchall()
                count = sum(
                    1 for row in rows
                    if (row[0] == scope if row[0] is not None else _legacy_retry_scope(row[1]) == scope)
                )
                if evidence_recovery_id:
                    if self.limits["transient_retries"] < 2:
                        raise FactoryError("configured retry limit is stricter than the evidence grant", "budget_retry_limit", 409)
                    from .evidence_grants import EvidenceGrantService
                    evidence_grant = EvidenceGrantService.occupy_locked(
                        con, evidence_recovery_id, protocol_context, reservation_id, now,
                        campaign_id=self.campaign_id, identity=str(identity), plan_id=plan_id,
                        job_id=job_id, phase=str(phase), stage=stage, retry=retry,
                        retry_scope=scope, requested_model=requested_model, kind=kind,
                        deadline=deadline, timeout=timeout,
                    )
                    if evidence_grant:
                        grant_row = con.execute("SELECT request_json FROM tf_evidence_recovery_grant WHERE id=?",
                                                (evidence_grant["id"],)).fetchone()
                        proposal = json.loads(grant_row[0]) if grant_row else {}
                        if proposal.get("schema") == "atlas.frozen-review-recovery-proposal.v1":
                            from .v1_batches import _g1_source_digest
                            approved = proposal.get("source_gate", {}).get("source_tree_digest")
                            if not approved or _g1_source_digest(self.store.pack.parent) != approved:
                                raise FactoryError("frozen-review host source changed after authorization", "evidence_source_gate", 409)
                elif count >= self.limits["transient_retries"]:
                    if self.limits["transient_retries"] >= 2:
                        from .protocol_grants import ProtocolRetryGrantService
                        grant_service = ProtocolRetryGrantService(self.store, clock=self.clock, initialize=False)
                        protocol_grant = grant_service.find_for_reservation_locked(
                            con, identity=str(identity), phase=str(phase), plan_id=plan_id,
                            job_id=job_id, stage=stage, requested_model=requested_model,
                            retry=retry, retry_scope=scope, context=protocol_context,
                            kind=kind, campaign_id=self.campaign_id,
                        )
                    if protocol_grant is None:
                        raise FactoryError("transient retry limit exhausted", "budget_retry_limit", 409)
            if retry is None and retry_scope:
                duplicate = con.execute(
                    "SELECT 1 FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND stage=? AND status!='not_started' LIMIT 1",
                    (self.campaign_id, str(identity), str(stage or phase)),
                ).fetchone()
                if duplicate:
                    raise FactoryError("repeated fixed-input call must consume retry budget", "budget_retry_limit", 409)
            con.execute(
                "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,job_id,requested_model,requested_effort,stage,retry,group_kind,retry_scope,worker_token) VALUES(?,?,?,?,?,'reserved',?,?,?,?,?,?,?,?,?)",
                (reservation_id, self.campaign_id, str(identity), str(phase), kind, now, job_id,
                 requested_model, requested_effort, stage, retry,
                 "runtime" if kind == "runtime" else "production",
                 str(retry_scope) if retry_scope else None, job_token),
            )
            if retry is not None and protocol_grant is not None:
                con.execute("INSERT INTO tf_protocol_retry_grant_use(grant_id,reservation_id,status,created_at) VALUES(?,?,?,?)",
                            (protocol_grant["id"], reservation_id, "reserved", now))
                con.execute("UPDATE tf_protocol_retry_grant SET status='reserved',consumed_reservation_id=? WHERE id=?",
                            (reservation_id, protocol_grant["id"]))
            if evidence_grant is not None:
                con.execute("INSERT INTO tf_evidence_recovery_grant_use(grant_id,reservation_id,status,created_at,call_attempt) VALUES(?,?,?,?,?)",
                            (evidence_grant["id"], reservation_id, "reserved", now, evidence_grant["call_attempt"]))
        cap = min(float(timeout), remaining) if timeout is not None else remaining
        return {"id": reservation_id, "timeout": max(0.0, cap), "deadline": deadline,
                "protocol_grant_id": protocol_grant["id"] if retry is not None and protocol_grant is not None else None,
                "evidence_recovery_id": evidence_grant["id"] if evidence_grant else None}

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
                f"UPDATE tf_budget_reservation SET status='failed',finished=?,outcome='recovered_after_owned_processes_stopped' WHERE campaign_id=? AND job_id IN ({placeholders}) AND status IN ('reserved','spawn_intent','started','uncertain')",
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
            row = con.execute("SELECT status,job_id,worker_token FROM tf_budget_reservation WHERE id=? AND campaign_id=?",
                              (reservation_id, self.campaign_id)).fetchone()
            if not row:
                raise FactoryError("budget reservation not found", "budget_reservation_missing", 404)
            if row[0] == "reserved":
                evidence = con.execute("SELECT u.grant_id,g.call_attempt,j.attempt,j.state,j.token,j.lease FROM tf_evidence_recovery_grant_use u JOIN tf_evidence_recovery_grant g ON g.id=u.grant_id JOIN job j ON j.id=? WHERE u.reservation_id=? AND u.status='spawn_intent'", (row[1], reservation_id)).fetchone()
                if evidence:
                    now = float(self.clock())
                    if (evidence["state"] != "running" or evidence["token"] != row[2]
                            or evidence["lease"] is None or evidence["lease"] <= now
                            or evidence["attempt"] != evidence["call_attempt"]):
                        raise FactoryError("evidence call lost its current token or attempt before start", "lease_lost", 409)
                con.execute("UPDATE tf_budget_reservation SET status='started',started=? WHERE id=?",
                            (float(self.clock()), reservation_id))
                con.execute("UPDATE tf_protocol_retry_grant_use SET status='started' WHERE reservation_id=? AND status='reserved'", (reservation_id,))
                con.execute("UPDATE tf_protocol_retry_grant SET status='consumed' WHERE consumed_reservation_id=? AND status='reserved'", (reservation_id,))
            evidence = con.execute("SELECT grant_id FROM tf_evidence_recovery_grant_use WHERE reservation_id=? AND status IN ('reserved','spawn_intent')", (reservation_id,)).fetchone()
            if evidence:
                con.execute("UPDATE tf_evidence_recovery_grant_use SET status='started' WHERE reservation_id=?", (reservation_id,))
                con.execute("UPDATE tf_evidence_recovery_grant SET status='started' WHERE id=? AND consumed_reservation_id=?", (evidence[0], reservation_id))

    def mark_spawn_intent(self, reservation_id, *, directory=None):
        """Durably record imminent process creation before calling Popen."""
        with self.store.connect(True) as con:
            row = con.execute("SELECT status,job_id,worker_token FROM tf_budget_reservation WHERE id=? AND campaign_id=?", (reservation_id, self.campaign_id)).fetchone()
            if row is None or row[0] != "reserved":
                raise FactoryError("reservation is not ready to spawn", "budget_spawn_state", 409)
            grant = con.execute("SELECT grant_id FROM tf_evidence_recovery_grant_use WHERE reservation_id=? AND status='reserved'", (reservation_id,)).fetchone()
            if grant:
                if directory is None:
                    raise FactoryError("evidence call CLI configuration path is required", "evidence_grant_binding", 409)
                try:
                    config = json.loads((__import__("pathlib").Path(directory) / "opencode.json").read_text(encoding="utf-8"))
                    proposal_row = con.execute("SELECT request_json FROM tf_evidence_recovery_grant WHERE id=?", (grant[0],)).fetchone()
                    from .evidence_grants import FROZEN_REVIEW_SCHEMA, get_call_binding
                    proposal = json.loads(proposal_row[0])
                    binding = get_call_binding(proposal)
                    if proposal.get("schema") == FROZEN_REVIEW_SCHEMA:
                        from .v1_batches import _g1_source_digest
                        approved_source = proposal.get("source_gate", {}).get("source_tree_digest")
                        if not approved_source or _g1_source_digest(self.store.pack.parent) != approved_source:
                            raise ValueError("frozen-review host source changed after authorization")
                        from .frozen_review_materials import registered_read_resources, validate_readonly_config
                        from .artifacts import tree_manifest
                        call = binding
                        attempt_dir = __import__("pathlib").Path(directory)
                        if (hashlib.sha256((attempt_dir / "input.json").read_bytes()).hexdigest() != call["input_sha256"]
                                or hashlib.sha256((attempt_dir / "prompt.txt").read_bytes()).hexdigest() != call["prompt_sha256"]
                                or digest(tree_manifest(attempt_dir / "source")) != call["source_tree_digest"]):
                            raise ValueError("frozen-review call files changed before spawn")
                        registered = registered_read_resources(directory,
                            expected_manifest_digest=binding["materials_manifest_digest"],
                            expected_tree_digest=binding["materials_tree_digest"])
                        actual_identity = validate_readonly_config(config, directory, registered["manifest"], binding["cli_config_identity"])
                    else:
                        from .evidence_views import readonly_cli_config_identity
                        actual_identity = readonly_cli_config_identity(config, directory)
                    expected_identity = binding["cli_config_identity"]
                except (OSError, ValueError, KeyError, ImportError) as exc:
                    raise FactoryError("evidence call CLI configuration cannot be verified", "evidence_grant_binding", 409) from exc
                if actual_identity != expected_identity:
                    raise FactoryError("evidence call CLI permissions or configuration differ", "evidence_grant_binding", 409)
                now = float(self.clock())
                grant_record = json.loads(proposal_row[0])
                fixed_deadline = float(grant_record["materials"]["binding"]["deadline"])
                frozen = grant_record.get("schema") == "atlas.frozen-review-recovery-proposal.v1"
                resumed = self._time_resume_locked(con, G1_AMENDMENT_PRODUCT, "G1", G1_AMENDMENT_PLAN) if frozen else None
                if resumed and resumed["grant_id"] == grant[0]:
                    fixed_deadline = resumed["effective_deadline"]
                else:
                    resumed = None
                minimum_slack = 2700 if frozen and not resumed else 0
                if now >= fixed_deadline or fixed_deadline - now < minimum_slack:
                    raise FactoryError("evidence recovery authorization deadline has passed", "budget_deadline", 409)
                owner = con.execute("SELECT state,token,lease FROM job WHERE id=?", (row[1],)).fetchone()
                if (owner is None or owner["state"] != "running" or owner["token"] != row[2]
                        or owner["lease"] is None or owner["lease"] <= now):
                    raise FactoryError("evidence review job token or lease is no longer current", "lease_lost", 409)
                if frozen:
                    attempt_row = con.execute("SELECT call_attempt FROM tf_evidence_recovery_grant WHERE id=? AND consumed_reservation_id=?", (grant[0], reservation_id)).fetchone()
                    owner_attempt = con.execute("SELECT attempt FROM job WHERE id=?", (row[1],)).fetchone()
                    if not attempt_row or attempt_row["call_attempt"] != owner_attempt["attempt"]:
                        raise FactoryError("frozen-review call attempt changed before spawn", "evidence_grant_binding", 409)
                changed = con.execute("UPDATE tf_evidence_recovery_grant SET status='spawn_intent' WHERE id=? AND consumed_reservation_id=? AND status='reserved'", (grant[0], reservation_id)).rowcount
                if changed != 1:
                    raise FactoryError("evidence grant cannot enter spawn intent", "evidence_grant_used", 409)
                con.execute("UPDATE tf_evidence_recovery_grant_use SET status='spawn_intent' WHERE reservation_id=?", (reservation_id,))

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
            con.execute("UPDATE tf_protocol_retry_grant_use SET status=? WHERE reservation_id=? AND status IN ('reserved','started','uncertain')",
                        ("consumed" if final in {"completed", "failed"} else "uncertain", reservation_id))
            con.execute("UPDATE tf_protocol_retry_grant SET status=? WHERE consumed_reservation_id=? AND status IN ('reserved','consumed')",
                        ("consumed" if final in {"completed", "failed"} else "uncertain", reservation_id))
            con.execute("UPDATE tf_evidence_recovery_grant_use SET status=? WHERE reservation_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                        ("consumed" if final in {"completed", "failed"} else "uncertain", reservation_id))
            con.execute("UPDATE tf_evidence_recovery_grant SET status=? WHERE consumed_reservation_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                        ("consumed" if final in {"completed", "failed"} else "uncertain", reservation_id))

    def release_not_started(self, reservation_id):
        """Release only when caller has direct evidence subprocess creation failed."""
        with self.store.connect(True) as con:
            cur = con.execute("UPDATE tf_budget_reservation SET status='not_started',finished=? WHERE id=? AND campaign_id=? AND status='reserved'",
                              (float(self.clock()), reservation_id, self.campaign_id))
            if cur.rowcount != 1:
                raise FactoryError("reservation start is not provably absent", "budget_release_denied", 409)
            con.execute("UPDATE tf_protocol_retry_grant_use SET status='not_started',released_at=? WHERE reservation_id=? AND status='reserved'",
                        (float(self.clock()), reservation_id))
            con.execute("UPDATE tf_protocol_retry_grant SET status='available',consumed_reservation_id=NULL WHERE consumed_reservation_id=? AND status='reserved'",
                        (reservation_id,))
            evidence = con.execute("SELECT grant_id FROM tf_evidence_recovery_grant_use WHERE reservation_id=? AND status IN ('reserved','spawn_intent')", (reservation_id,)).fetchone()
            if evidence:
                con.execute("UPDATE tf_evidence_recovery_grant_use SET status='not_started',released_at=? WHERE reservation_id=?", (float(self.clock()), reservation_id))
                con.execute("UPDATE tf_evidence_recovery_grant SET status='queued',consumed_reservation_id=NULL,call_attempt=NULL WHERE id=? AND consumed_reservation_id=? AND status IN ('reserved','spawn_intent')", (evidence[0], reservation_id))

    def phase_remaining(self, identity, phase=None, *, plan_id=None):
        # ``identity`` is retained for older callers; segment deadlines are
        # intentionally campaign-wide rather than product-scoped.
        phase = phase or identity
        with self.store.connect() as con:
            deadline = self._effective_timing_locked(con, identity, phase, plan_id)["deadline"]
        return None if deadline is None else max(0.0, deadline - float(self.clock()))

    def effective_deadline(self, identity, phase="G1", *, plan_id=None):
        with self.store.connect() as con:
            return self._effective_timing_locked(con, identity, phase, plan_id)["deadline"]

    def effective_deadline_snapshot(self, identity, phase="G1", *, plan_id=None, job_id=None):
        with self.store.connect() as con:
            timing = self._effective_timing_locked(con, identity, phase, plan_id)
        amendment = timing["amendment"]
        resumed = timing["time_resume"]
        deadline = timing["deadline"]
        source_authorization = None
        if amendment and amendment["version"] == 5:
            with self.store.connect() as con:
                binding = con.execute("SELECT request_json FROM tf_budget_amendment_binding WHERE amendment_id=?",
                                      (amendment["id"],)).fetchone()
            request = json.loads(binding[0]) if binding else {}
            source_authorization = {"source_ref": request.get("source_ref"),
                                    "source_digest": request.get("source_digest")}
        return {"schema": "atlas.g1-effective-budget.v1", "binding": {
                    "campaign_id": self.campaign_id, "plan_id": plan_id,
                    "product_id": str(identity), "segment": str(phase), "job_id": job_id},
                "base_started_at": timing["base_started_at"],
                "base_deadline": timing["base_deadline"], "effective_deadline": deadline,
                "deadline_source": timing["deadline_source"],
                "time_resume": dict(resumed) if resumed else None,
                "amendment_id": amendment["id"] if amendment else None,
                "activated_at": amendment["activated_at"] if amendment and amendment["version"] == 5 else (resumed["activated_at"] if resumed else (amendment["activated_at"] if amendment else None)),
                "new_deadline": amendment["new_deadline"] if amendment and amendment["version"] == 5 else (resumed["effective_deadline"] if resumed else (amendment["new_deadline"] if amendment else None)),
                "supersedes": timing["supersedes"],
                "source_authorization": source_authorization,
                "generated_at": float(self.clock())}

    def snapshot(self):
        with self.store.connect(True) as con:
            self._refresh_limits_locked(con)
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                  (self.campaign_id,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (self.campaign_id,)).fetchone()[0]
            segments = [dict(r) for r in con.execute("SELECT phase,started,deadline FROM tf_budget_phase WHERE campaign_id=?", (self.campaign_id,))]
            control = con.execute("SELECT paused,paused_at,pause_reason FROM tf_budget_control WHERE campaign_id=?", (self.campaign_id,)).fetchone()
            repairs = [dict(r) for r in con.execute("SELECT product_id,COUNT(*) AS repairs_used FROM tf_budget_repair WHERE campaign_id=? GROUP BY product_id", (self.campaign_id,))]
            amendments = [dict(r) for r in con.execute("SELECT * FROM tf_budget_amendment WHERE campaign_id=? ORDER BY version", (self.campaign_id,))]
            protocol_grants = [dict(r) for r in con.execute(
                "SELECT id,job_id,plan_id,product_id,idempotency_key,request_digest,status,consumed_reservation_id,created_at FROM tf_protocol_retry_grant WHERE campaign_id=? ORDER BY created_at,id",
                (self.campaign_id,))]
            protocol_grant_uses = [dict(r) for r in con.execute(
                "SELECT grant_id,reservation_id,status,created_at,released_at FROM tf_protocol_retry_grant_use WHERE grant_id IN (SELECT id FROM tf_protocol_retry_grant WHERE campaign_id=?) ORDER BY created_at,reservation_id",
                (self.campaign_id,))]
            evidence_grants = [dict(r) for r in con.execute(
                "SELECT id,job_id,plan_id,product_id,request_key,proposal_digest,status,queued_job_id,consumed_reservation_id,call_attempt,created_at FROM tf_evidence_recovery_grant WHERE campaign_id=? ORDER BY created_at,id",
                (self.campaign_id,))]
            evidence_grant_uses = [dict(r) for r in con.execute(
                "SELECT grant_id,reservation_id,status,created_at,released_at FROM tf_evidence_recovery_grant_use WHERE grant_id IN (SELECT id FROM tf_evidence_recovery_grant WHERE campaign_id=?) ORDER BY created_at,reservation_id",
                (self.campaign_id,))]
            resumed = self._time_resume_locked(con, G1_AMENDMENT_PRODUCT, "G1", G1_AMENDMENT_PLAN)
            external_sessions = resumed["external_cli_sessions"] if resumed else 0
            effective_timings = []
            seen = set()
            for amendment in amendments:
                identity = (amendment["product_id"], amendment["plan_id"])
                if identity in seen:
                    continue
                seen.add(identity)
                timing = self._effective_timing_locked(con, amendment["product_id"], "G1", amendment["plan_id"])
                effective_timings.append({
                    "plan_id": amendment["plan_id"], "product_id": amendment["product_id"],
                    "segment": "G1", "effective_deadline": timing["deadline"],
                    "deadline_source": timing["deadline_source"],
                    "amendment_id": timing["amendment"]["id"] if timing["amendment"] else None,
                    "activated_at": timing["amendment"]["activated_at"] if timing["amendment"] and timing["amendment"]["version"] == 5 else (timing["time_resume"]["activated_at"] if timing["time_resume"] else (timing["amendment"]["activated_at"] if timing["amendment"] else None)),
                    "supersedes": timing["supersedes"],
                })
        now = float(self.clock())
        for segment in segments:
            segment["remaining_seconds"] = max(0.0, segment["deadline"] - now)
        return {"campaign_id": self.campaign_id, "cli_sessions_used": charged + external_sessions,
                "factory_cli_sessions_used": charged, "external_cli_sessions_used": external_sessions,
                "time_resumes": [dict(resumed)] if resumed else [],
                "effective_timings": effective_timings,
                "cli_sessions_limit": self.limits["cli_sessions"], "active": active,
                "limits": dict(self.limits), "segments": segments,
                "paused": bool(control[0]) if control else False,
                "paused_at": control[1] if control else None,
                "pause_reason": control[2] if control else None,
                "repairs": repairs, "amendments": amendments,
                "protocol_retry_grants": protocol_grants,
                "protocol_retry_grant_uses": protocol_grant_uses,
                "evidence_recovery_grants": evidence_grants,
                "evidence_recovery_grant_uses": evidence_grant_uses,
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
        if isinstance(request, dict) and request.get("schema") == G1_R5_AUTHORIZATION_SCHEMA:
            return self.register_r5(request)
        if isinstance(request, dict) and request.get("schema") == G1_R6_AUTHORIZATION_SCHEMA:
            return self.register_r6(request)
        if isinstance(request, dict) and request.get("schema") == G1_R7_AUTHORIZATION_SCHEMA:
            return self.register_r7(request)
        if isinstance(request, dict) and request.get("schema") == "atlas.budget-amendment.v3":
            return self.register_frozen_revision(request)
        if isinstance(request, dict) and "schema" in request:
            raise FactoryError("unsupported budget amendment schema", "budget_amendment_invalid", 400)
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

    def _validate_r5_request(self, request):
        required = ("schema", "campaign_id", "product_id", "plan_id", "source_ref", "source_digest",
                    "summary", "reason", "idempotency_key", "predecessor_amendment_id", "failed_job_id",
                    "checkpoint_name", "checkpoint_result_digest", "prepared_request_digest",
                    "effective_plan_digest", "patch_digest", "repair_request_digest")
        if any(not isinstance(request.get(key), str) or not request[key].strip() for key in required):
            raise FactoryError("all version 2 authorization bindings are required", "budget_amendment_invalid", 400)
        if request["schema"] != G1_R5_AUTHORIZATION_SCHEMA:
            raise FactoryError("unsupported budget amendment schema", "budget_amendment_invalid", 400)
        fixed = {
            "campaign_id": G1_AMENDMENT_CAMPAIGN, "product_id": G1_AMENDMENT_PRODUCT,
            "plan_id": G1_AMENDMENT_PLAN, "source_ref": G1_R5_AUTHORIZATION_SOURCE_REF,
            "source_digest": G1_R5_AUTHORIZATION_SOURCE_DIGEST,
            "predecessor_amendment_id": G1_R5_PREDECESSOR_ID,
            "failed_job_id": G1_R5_FAILED_JOB, "checkpoint_name": G1_R5_CHECKPOINT,
            "checkpoint_result_digest": G1_R5_CHECKPOINT_DIGEST,
            "prepared_request_digest": G1_R5_PREPARED_REQUEST_DIGEST,
            "effective_plan_digest": G1_R5_EFFECTIVE_PLAN_DIGEST,
            "patch_digest": G1_R5_PATCH_DIGEST,
            "repair_request_digest": G1_R5_REPAIR_REQUEST_DIGEST,
            "idempotency_key": "atlas-g1-r5-user-authorization-2026-10-19-v1",
        }
        if self.campaign_id != G1_AMENDMENT_CAMPAIGN or any(request.get(k) != v for k, v in fixed.items()):
            raise FactoryError("version 2 amendment is outside the exact authorized binding", "budget_amendment_scope", 403)
        if len(request["summary"]) > 2000 or len(request["reason"]) > 1000:
            raise FactoryError("amendment text exceeds limits", "budget_amendment_invalid", 400)
        source_path = self.store.pack.parent / G1_R5_AUTHORIZATION_SOURCE_REF
        try:
            source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("version 2 authorization source is unavailable", "budget_amendment_source", 409) from exc
        if source_digest != G1_R5_AUTHORIZATION_SOURCE_DIGEST:
            raise FactoryError("version 2 authorization source bytes changed", "budget_amendment_source", 409)
        # Recompute from the fixed checked-in preparation materials and run the
        # existing host re-preparation path against the real failed job.
        repo = self.store.pack.parent
        prep_path = repo / "docs/template-factory/g1-preparation-2026-10-19/prepare-revision-request.json"
        repair_path = repo / "docs/template-factory/g1-preparation-2026-10-19/formal-repair-request-NOT-EXECUTED.json"
        try:
            from .store import digest
            prep_request = json.loads(prep_path.read_text(encoding="utf-8"))
            repair_request = json.loads(repair_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise FactoryError("fixed prepared revision materials are unavailable", "budget_amendment_basis", 409) from exc
        if digest(prep_request) != G1_R5_PREPARED_REQUEST_DIGEST or digest(repair_request) != G1_R5_REPAIR_REQUEST_DIGEST:
            raise FactoryError("fixed prepared revision materials changed", "budget_amendment_basis", 409)
        if repair_request.get("expected_digest") != "8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9":
            raise FactoryError("formal repair request binding changed", "budget_amendment_basis", 409)
        try:
            from .plan_revision import PreparedRevisionService
            prepared = PreparedRevisionService(self.store).prepare(G1_R5_FAILED_JOB, prep_request)
        except FactoryError as exc:
            raise FactoryError("fixed prepared revision no longer validates", "budget_amendment_basis", 409) from exc
        if (prepared.get("request_digest") != G1_R5_PREPARED_REQUEST_DIGEST
                or prepared.get("effective_plan_digest") != G1_R5_EFFECTIVE_PLAN_DIGEST
                or digest(prepared.get("effective_plan")) != G1_R5_EFFECTIVE_PLAN_DIGEST):
            raise FactoryError("prepared revision result differs from the authorized exact materials", "budget_amendment_basis", 409)
        return digest(request)

    def register_r5(self, request):
        if (not isinstance(request, dict)
                or not isinstance(request.get("idempotency_key"), str)
                or not request["idempotency_key"].strip()):
            raise FactoryError("version 2 authorization request is required", "budget_amendment_invalid", 400)
        from .store import digest
        request_digest = digest(request)
        # BEGIN IMMEDIATE serializes the prior lookup, v1/baseline verification,
        # and insertion so a changed key cannot race in a second version 2.
        with self.store.connect(True) as con:
            prior = con.execute(
                "SELECT a.*,b.request_json,b.request_digest FROM tf_budget_amendment a "
                "LEFT JOIN tf_budget_amendment_binding b ON b.amendment_id=a.id "
                "WHERE a.campaign_id=? AND a.product_id=? AND a.idempotency_key=?",
                (self.campaign_id, G1_AMENDMENT_PRODUCT, request["idempotency_key"]),
            ).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["request_json"] != json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":")):
                    raise FactoryError("idempotency key was already used for different authorization", "idempotency_conflict", 409)
                return {k: prior[k] for k in prior.keys() if k not in {"request_json", "request_digest"}}
            self._validate_r5_request(request)
            prior_v2 = con.execute(
                "SELECT id FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND version=2",
                (self.campaign_id, G1_AMENDMENT_PRODUCT),
            ).fetchone()
            if prior_v2:
                raise FactoryError("the single authorized version 2 is already recorded", "budget_amendment_exhausted", 409)
            predecessor = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                      (G1_R5_PREDECESSOR_ID, self.campaign_id, G1_AMENDMENT_PRODUCT)).fetchone()
            if (not predecessor or predecessor["version"] != 1 or predecessor["activated_at"] is None
                    or predecessor["new_repair_limit"] != 4 or predecessor["new_deadline"] != G1_R5_DEADLINE):
                raise FactoryError("active version 1 predecessor or inherited deadline changed", "budget_amendment_basis", 409)
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                  (self.campaign_id, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            old_deadline = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                                       (self.campaign_id,)).fetchone()
            cli_sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                       (self.campaign_id,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (self.campaign_id,)).fetchone()[0]
            if (not old_deadline or old_deadline[0] != G1_R5_BASE_STARTED or old_deadline[1] != G1_R5_BASE_DEADLINE
                    or repairs != 4 or cli_sessions != 52 or active != 0):
                raise FactoryError("first version 2 registration requires the fixed phase and 0-active / 4-repair / 52-call baseline",
                                   "budget_amendment_basis", 409)
            amendment_id = "bamd_" + uuid.uuid4().hex
            at = float(self.clock())
            con.execute(
                "INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,2,4,5,?,?,?,0,?,NULL,?)",
                (amendment_id, self.campaign_id, G1_AMENDMENT_PRODUCT, G1_AMENDMENT_PLAN,
                 G1_R5_AUTHORIZATION_SOURCE_REF, G1_R5_AUTHORIZATION_SOURCE_DIGEST,
                 request["summary"], request["reason"], request["idempotency_key"],
                 repairs, cli_sessions, G1_R5_DEADLINE, at, G1_R5_DEADLINE),
            )
            encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            con.execute("INSERT INTO tf_budget_amendment_binding VALUES(?,?,?)",
                        (amendment_id, encoded, request_digest))
            return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def _validate_r6_request(self, request):
        required = {
            "schema", "campaign_id", "product_id", "plan_id", "source_ref", "source_digest",
            "summary", "reason", "idempotency_key", "predecessor_amendment_id",
            "old_job_id", "old_job_attempt", "old_job_snapshot_digest", "old_job_error",
            "old_job_stage", "case_basis_digest", "facts_view_digest", "case_design_digest",
            "prepared_revision", "prepared_revision_digest", "effective_plan_digest",
            "program_manifest_digest", "protocol_grant_id", "protocol_reservation_id",
            "baseline_cli_sessions", "baseline_repair_count", "baseline_scope_retry_rows",
            "baseline_active", "old_deadline", "window_seconds",
        }
        if not isinstance(request, dict) or set(request) != required:
            raise FactoryError("R6 authorization request has missing or unknown fields", "budget_amendment_invalid", 400)
        fixed = {
            "schema": G1_R6_AUTHORIZATION_SCHEMA,
            "campaign_id": G1_AMENDMENT_CAMPAIGN,
            "product_id": G1_AMENDMENT_PRODUCT,
            "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": G1_R6_AUTHORIZATION_SOURCE_REF,
            "source_digest": G1_R6_AUTHORIZATION_SOURCE_DIGEST,
            "idempotency_key": G1_R6_IDEMPOTENCY_KEY,
            "predecessor_amendment_id": G1_R6_PREDECESSOR_ID,
            "old_job_id": G1_R6_FAILED_JOB,
            "old_job_attempt": G1_R6_FAILED_ATTEMPT,
            "old_job_error": G1_R6_FAILED_ERROR,
            "old_job_stage": G1_R6_FAILED_STAGE,
            "protocol_grant_id": G1_R6_PROTOCOL_GRANT_ID,
            "protocol_reservation_id": G1_R6_PROTOCOL_RESERVATION_ID,
            "baseline_cli_sessions": 64,
            "baseline_repair_count": 5,
            "baseline_scope_retry_rows": 3,
            "baseline_active": 0,
            "old_deadline": G1_R6_OLD_DEADLINE,
            "window_seconds": G1_R6_WINDOW_SECONDS,
        }
        if any(request.get(key) != value for key, value in fixed.items()):
            raise FactoryError("R6 authorization is outside the fixed campaign, job, grant or budget binding", "budget_amendment_scope", 403)
        if any(not isinstance(request.get(key), str) or not request[key].strip()
               for key in ("summary", "reason", "old_job_snapshot_digest", "old_job_error",
                           "case_basis_digest", "facts_view_digest", "case_design_digest",
                           "prepared_revision_digest", "effective_plan_digest", "program_manifest_digest")):
            raise FactoryError("R6 source, job and prepared digest bindings are required", "budget_amendment_invalid", 400)
        if (len(request["summary"]) > 2000 or len(request["reason"]) > 1000
                or len(request["idempotency_key"]) > 200):
            raise FactoryError("R6 authorization text exceeds limits", "budget_amendment_invalid", 400)
        source_path = self.store.pack.parent / G1_R6_AUTHORIZATION_SOURCE_REF
        try:
            actual_source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("R6 authorization source is unavailable", "budget_amendment_source", 409) from exc
        if actual_source_digest != G1_R6_AUTHORIZATION_SOURCE_DIGEST:
            raise FactoryError("R6 authorization source bytes changed", "budget_amendment_source", 409)

        from .plan_revision import PreparedRevisionService
        prepared_request = request["prepared_revision"]
        if not isinstance(prepared_request, dict) or digest(prepared_request) != request["prepared_revision_digest"]:
            raise FactoryError("R6 prepared revision request digest changed", "budget_amendment_basis", 409)
        try:
            prepared = PreparedRevisionService(self.store).prepare(G1_R6_FAILED_JOB, prepared_request)
        except FactoryError as exc:
            raise FactoryError("fixed R6 prepared revision no longer validates", "budget_amendment_basis", 409) from exc
        prepared_program_reuse = prepared.get("prepared_program_reuse")
        manifest = prepared_request.get("program_reuse_manifest")
        if (prepared.get("request_digest") != request["prepared_revision_digest"]
                or prepared.get("effective_plan_digest") != request["effective_plan_digest"]
                or digest(prepared.get("case_design")) != request["case_design_digest"]
                or digest(prepared_program_reuse) != request["program_manifest_digest"]
                or not isinstance(manifest, dict)):
            raise FactoryError("R6 prepared plan, case design or program manifest differs from authorization", "budget_amendment_basis", 409)
        binding = prepared.get("binding", {})
        if (binding.get("case_basis_digest") != request["case_basis_digest"]
                or binding.get("facts_view_digest") != request["facts_view_digest"]):
            raise FactoryError("R6 prepared case basis or facts view differs from authorization", "budget_amendment_basis", 409)
        return digest(request)

    def register_r6(self, request):
        if self.campaign_id != G1_AMENDMENT_CAMPAIGN:
            raise FactoryError("R6 authorization is limited to its fixed campaign", "budget_amendment_scope", 403)
        if not isinstance(request, dict) or not isinstance(request.get("idempotency_key"), str):
            raise FactoryError("R6 authorization request is required", "budget_amendment_invalid", 400)
        request_digest = digest(request)
        encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self.store.connect(True) as con:
            prior = con.execute(
                "SELECT a.*,b.request_json,b.request_digest FROM tf_budget_amendment a "
                "LEFT JOIN tf_budget_amendment_binding b ON b.amendment_id=a.id "
                "WHERE a.campaign_id=? AND a.product_id=? AND a.idempotency_key=?",
                (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, request["idempotency_key"]),
            ).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["request_json"] != encoded:
                    raise FactoryError("R6 idempotency key is already bound to another request", "idempotency_conflict", 409)
                return {key: prior[key] for key in prior.keys() if key not in {"request_json", "request_digest"}}
            request_digest = self._validate_r6_request(request)
            prior_v3 = con.execute(
                "SELECT id FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND version=3",
                (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT),
            ).fetchone()
            if prior_v3:
                raise FactoryError("the single R6 source-alignment amendment is already registered", "budget_amendment_exhausted", 409)
            predecessor = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                      (G1_R6_PREDECESSOR_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
            base = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                               (G1_AMENDMENT_CAMPAIGN,)).fetchone()
            calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                  (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            retry_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                                     (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchall()
            from .budget import _legacy_retry_scope
            scope_retries = sum(1 for row in retry_rows if (row[0] == "blueprint-spec-review:phase_acceptance"
                                 if row[0] is not None else _legacy_retry_scope(row[1]) == "blueprint-spec-review:phase_acceptance"))
            grant = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id=? AND campaign_id=?",
                                (G1_R6_PROTOCOL_GRANT_ID, G1_AMENDMENT_CAMPAIGN)).fetchone()
            grant_use = con.execute("SELECT status FROM tf_protocol_retry_grant_use WHERE grant_id=? AND reservation_id=?",
                                    (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID)).fetchone()
            job = con.execute("SELECT state,attempt,stage,error,snapshot FROM job WHERE id=?", (G1_R6_FAILED_JOB,)).fetchone()
            expected_old_deadline = predecessor["new_deadline"] if predecessor else None
            if (not predecessor or predecessor["version"] != 2 or predecessor["activated_at"] is None
                    or predecessor["new_repair_limit"] != 5 or expected_old_deadline != G1_R6_OLD_DEADLINE
                    or not base or base["deadline"] != G1_R5_BASE_DEADLINE
                    or calls != 64 or repairs != 5 or active != 0 or scope_retries != 3
                    or not grant or grant["status"] != "consumed"
                    or grant["consumed_reservation_id"] != G1_R6_PROTOCOL_RESERVATION_ID
                    or not grant_use or grant_use["status"] != "consumed"
                    or not job or job["state"] != "failed" or job["attempt"] != G1_R6_FAILED_ATTEMPT
                    or job["stage"] != G1_R6_FAILED_STAGE or job["error"] != request["old_job_error"]
                    or digest(json.loads(job["snapshot"])) != request["old_job_snapshot_digest"]):
                raise FactoryError("current G1 job, grant or 64/5/0 budget baseline differs from R6 authorization",
                                   "budget_amendment_basis", 409)
            amendment_id = "bamd_" + uuid.uuid4().hex
            at = float(self.clock())
            con.execute(
                "INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,3,5,6,?,?,?,?,?,NULL,NULL)",
                (amendment_id, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, G1_AMENDMENT_PLAN,
                 G1_R6_AUTHORIZATION_SOURCE_REF, G1_R6_AUTHORIZATION_SOURCE_DIGEST,
                 request["summary"], request["reason"], request["idempotency_key"],
                 repairs, calls, G1_R6_OLD_DEADLINE, G1_R6_WINDOW_SECONDS, at),
            )
            con.execute("INSERT INTO tf_budget_amendment_binding VALUES(?,?,?)",
                        (amendment_id, encoded, request_digest))
            return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def _validate_r7_request(self, request):
        required = {
            "schema", "campaign_id", "product_id", "plan_id", "source_ref", "source_digest",
            "summary", "reason", "idempotency_key", "predecessor_amendment_id", "old_job_id",
            "old_job_attempt", "old_job_snapshot_digest", "old_job_error", "old_job_stage",
            "prepared_revision", "prepared_revision_digest", "effective_plan_digest", "case_design_digest",
            "program_revision_digest", "baseline_cli_sessions", "baseline_repair_count",
            "baseline_scope_retry_rows", "baseline_protocol_grant_uses", "baseline_active", "old_deadline",
        }
        if not isinstance(request, dict) or set(request) != required:
            raise FactoryError("R7 authorization request has missing or unknown fields", "budget_amendment_invalid", 400)
        fixed = {
            "schema": G1_R7_AUTHORIZATION_SCHEMA, "campaign_id": G1_AMENDMENT_CAMPAIGN,
            "product_id": G1_AMENDMENT_PRODUCT, "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": G1_R7_AUTHORIZATION_SOURCE_REF, "source_digest": G1_R7_AUTHORIZATION_SOURCE_DIGEST,
            "idempotency_key": G1_R7_IDEMPOTENCY_KEY, "predecessor_amendment_id": G1_R7_PREDECESSOR_ID,
            "old_job_id": G1_R7_FAILED_JOB, "old_job_attempt": G1_R7_FAILED_ATTEMPT,
            "old_job_stage": G1_R7_FAILED_STAGE, "baseline_cli_sessions": 71,
            "baseline_repair_count": 6, "baseline_scope_retry_rows": 3,
            "baseline_protocol_grant_uses": 1, "baseline_active": 0, "old_deadline": G1_R7_OLD_DEADLINE,
        }
        if any(request.get(key) != value for key, value in fixed.items()):
            raise FactoryError("R7 authorization is outside its fixed campaign, job or budget binding", "budget_amendment_scope", 403)
        if any(not isinstance(request.get(k), str) or not request[k].strip() for k in (
                "summary", "reason", "old_job_snapshot_digest", "old_job_error",
                "prepared_revision_digest", "effective_plan_digest", "case_design_digest", "program_revision_digest")):
            raise FactoryError("R7 authorization digests and reason are required", "budget_amendment_invalid", 400)
        if not isinstance(request.get("prepared_revision"), dict) or request["prepared_revision"].get("schema") != "atlas.failed-plan-revision.v3":
            raise FactoryError("R7 authorization requires the v3 prepared revision", "budget_amendment_invalid", 400)
        if len(request["summary"]) > 2000 or len(request["reason"]) > 1000:
            raise FactoryError("R7 authorization text exceeds limits", "budget_amendment_invalid", 400)
        source_path = self.store.pack.parent / G1_R7_AUTHORIZATION_SOURCE_REF
        try:
            actual_source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("R7 authorization source is unavailable", "budget_amendment_source", 409) from exc
        if actual_source_digest != G1_R7_AUTHORIZATION_SOURCE_DIGEST:
            raise FactoryError("R7 authorization source bytes changed", "budget_amendment_source", 409)
        if digest(request["prepared_revision"]) != request["prepared_revision_digest"]:
            raise FactoryError("R7 prepared revision request digest changed", "budget_amendment_basis", 409)
        from .plan_revision import PreparedRevisionService
        try:
            prepared = PreparedRevisionService(self.store).prepare(G1_R7_FAILED_JOB, request["prepared_revision"])
        except FactoryError as exc:
            raise FactoryError("fixed R7 prepared revision no longer validates", "budget_amendment_basis", 409) from exc
        if (prepared.get("request_digest") != request["prepared_revision_digest"]
                or prepared.get("effective_plan_digest") != request["effective_plan_digest"]
                or prepared.get("case_design_digest") != request["case_design_digest"]
                or digest(prepared.get("prepared_program_revision")) != request["program_revision_digest"]):
            raise FactoryError("R7 prepared plan, case design or program manifest differs from authorization", "budget_amendment_basis", 409)
        return digest(request)

    def register_r7(self, request):
        if self.campaign_id != G1_AMENDMENT_CAMPAIGN:
            raise FactoryError("R7 authorization is limited to its fixed campaign", "budget_amendment_scope", 403)
        request_digest = digest(request)
        encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self.store.connect(True) as con:
            prior = con.execute(
                "SELECT a.*,b.request_json,b.request_digest FROM tf_budget_amendment a "
                "LEFT JOIN tf_budget_amendment_binding b ON b.amendment_id=a.id "
                "WHERE a.campaign_id=? AND a.product_id=? AND a.idempotency_key=?",
                (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, request.get("idempotency_key")),
            ).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["request_json"] != encoded:
                    raise FactoryError("R7 idempotency key is already bound to another request", "idempotency_conflict", 409)
                return {key: prior[key] for key in prior.keys() if key not in {"request_json", "request_digest"}}
            self._validate_r7_request(request)
            prior_v4 = con.execute("SELECT id FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND version=4",
                                   (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
            if prior_v4:
                raise FactoryError("the single R7 bounded-revision amendment is already registered", "budget_amendment_exhausted", 409)
            predecessor = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                      (G1_R7_PREDECESSOR_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
            base = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                               (G1_AMENDMENT_CAMPAIGN,)).fetchone()
            calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                  (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            retry_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                                     (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchall()
            retry_count = sum(1 for item in retry_rows if (item["retry_scope"] == "blueprint-spec-review:phase_acceptance"
                                if item["retry_scope"] is not None else
                                _legacy_retry_scope(item["stage"]) == "blueprint-spec-review:phase_acceptance"))
            grant = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id=? AND campaign_id=?",
                                (G1_R6_PROTOCOL_GRANT_ID, G1_AMENDMENT_CAMPAIGN)).fetchone()
            grant_use = con.execute("SELECT status FROM tf_protocol_retry_grant_use WHERE grant_id=? AND reservation_id=?",
                                    (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID)).fetchone()
            job = con.execute("SELECT state,attempt,stage,error,snapshot FROM job WHERE id=?", (G1_R7_FAILED_JOB,)).fetchone()
            execution = con.execute("SELECT batch_id FROM v1_execution WHERE plan_id=?", (G1_AMENDMENT_PLAN,)).fetchone()
            parent = con.execute("SELECT state FROM batch WHERE id=?", (execution[0],)).fetchone() if execution else None
            if (not predecessor or predecessor["version"] != 3 or predecessor["activated_at"] is None
                    or predecessor["new_repair_limit"] != 6 or predecessor["new_deadline"] != G1_R7_OLD_DEADLINE
                    or not base or base["deadline"] != G1_R5_BASE_DEADLINE
                    or calls != 71 or repairs != 6 or active != 0 or retry_count != 3
                    or not grant or grant["status"] != "consumed"
                    or grant["consumed_reservation_id"] != G1_R6_PROTOCOL_RESERVATION_ID
                    or not grant_use or grant_use["status"] != "consumed"
                    or not job or job["state"] != "failed" or job["attempt"] != 1
                    or job["stage"] != G1_R7_FAILED_STAGE or job["error"] != request["old_job_error"]
                    or digest(json.loads(job["snapshot"])) != request["old_job_snapshot_digest"]
                    or not parent or parent["state"] != "paused"):
                raise FactoryError("current R6 job or 71/6/0 budget baseline differs from R7 authorization", "budget_amendment_basis", 409)
            amendment_id = "bamd_" + uuid.uuid4().hex
            at = float(self.clock())
            con.execute("INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,4,6,7,?,?,?,?,?,NULL,NULL)",
                        (amendment_id, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, G1_AMENDMENT_PLAN,
                         G1_R7_AUTHORIZATION_SOURCE_REF, G1_R7_AUTHORIZATION_SOURCE_DIGEST,
                         request["summary"], request["reason"], request["idempotency_key"],
                         repairs, calls, G1_R7_OLD_DEADLINE, 0, at))
            con.execute("INSERT INTO tf_budget_amendment_binding VALUES(?,?,?)", (amendment_id, encoded, request_digest))
            return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate_locked(self, con, amendment_id):
        row = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=?", (amendment_id, self.campaign_id)).fetchone()
        if not row:
            raise FactoryError("budget amendment not found", "not_found", 404)
        if row["version"] not in {1, 2, 3, 4}:
            raise FactoryError("unknown or queue-only budget amendment version", "budget_amendment_version", 409)
        if row["version"] == 4:
            raise FactoryError("R7 amendment can activate only with its atomic successor queue", "budget_amendment_activation_denied", 409)
        if row["version"] == 3:
            raise FactoryError("R6 amendment can activate only with its atomic source-alignment successor queue", "budget_amendment_activation_denied", 409)
        if row["activated_at"] is not None:
            return dict(row)
        at = float(self.clock())
        if row["version"] == 2:
            if row["old_repair_limit"] != 4 or row["new_repair_limit"] != 5 or row["old_deadline"] != G1_R5_DEADLINE:
                raise FactoryError("version 2 amendment basis changed", "budget_amendment_basis", 409)
            base = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                               (self.campaign_id,)).fetchone()
            predecessor = con.execute("SELECT version,activated_at,new_repair_limit,new_deadline FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                      (G1_R5_PREDECESSOR_ID, self.campaign_id, G1_AMENDMENT_PRODUCT)).fetchone()
            if (not base or base["started"] != G1_R5_BASE_STARTED or base["deadline"] != G1_R5_BASE_DEADLINE
                    or not predecessor or predecessor["version"] != 1 or predecessor["activated_at"] is None
                    or predecessor["new_repair_limit"] != 4 or predecessor["new_deadline"] != G1_R5_DEADLINE
                    or row["new_deadline"] != G1_R5_DEADLINE):
                raise FactoryError("version 2 base phase or active predecessor changed", "budget_amendment_basis", 409)
            if row["old_deadline"] <= at:
                raise FactoryError("inherited G1 deadline has expired", "budget_deadline", 409)
            deadline = G1_R5_DEADLINE
        elif row["version"] == 1:
            old = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'", (self.campaign_id,)).fetchone()
            if not old or old[0] != row["old_deadline"]:
                raise FactoryError("original G1 deadline is missing or changed", "budget_amendment_basis", 409)
            deadline = max(float(row["old_deadline"]), at + row["window_seconds"])
        con.execute("UPDATE tf_budget_amendment SET activated_at=?,new_deadline=? WHERE id=? AND activated_at IS NULL", (at, deadline, amendment_id))
        return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate_frozen_locked(self, con, amendment_id, *, expected_prepared_digest):
        """Activate version 5 only in the caller's successor queue transaction."""
        if not getattr(con, "in_transaction", False):
            raise FactoryError("version 5 activation requires the atomic successor transaction",
                               "budget_amendment_activation_denied", 409)
        row = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=?",
                          (amendment_id, self.campaign_id)).fetchone()
        if not row:
            raise FactoryError("budget amendment not found", "not_found", 404)
        if row["version"] != 5:
            raise FactoryError("frozen revision activation requires version 5", "budget_amendment_version", 409)
        if row["activated_at"] is not None or row["new_deadline"] is not None:
            raise FactoryError("version 5 amendment was activated without its atomic queue receipt",
                               "budget_amendment_activation_conflict", 409)
        binding = con.execute("SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                              (amendment_id,)).fetchone()
        if not binding:
            raise FactoryError("version 5 prepared digest does not match its registered binding",
                               "budget_amendment_basis", 409)
        request = json.loads(binding["request_json"])
        self._validate_frozen_revision_request(request)
        if (digest(request) != binding["request_digest"]
                or request.get("prepared_revision_digest") != expected_prepared_digest
                or row["source_ref"] != request["source_ref"]
                or row["source_digest"] != request["source_digest"]
                or row["window_seconds"] != request["timing"].get("window_seconds")
                or row["new_repair_limit"] != request["limits"].get("repair_limit")):
            raise FactoryError("version 5 registered authorization changed", "budget_amendment_basis", 409)
        predecessor = con.execute(
            "SELECT * FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? "
            "AND version<5 AND activated_at IS NOT NULL ORDER BY version DESC LIMIT 1",
            (row["campaign_id"], row["product_id"]),
        ).fetchone()
        timing = self.ledger._effective_timing_locked(con, row["product_id"], "G1", row["plan_id"])
        if (not predecessor or predecessor["activated_at"] is None
                or predecessor["new_repair_limit"] != request["limits"].get("expected_repairs")
                or timing["deadline_source"] != request["timing"].get("supersedes", {}).get("deadline_source")
                or not timing["time_resume"]
                or request["timing"].get("supersedes") != self.ledger._timing_source_snapshot(timing["time_resume"])):
            raise FactoryError("current predecessor or timing source differs from version 5 authorization",
                               "budget_amendment_basis", 409)
        calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                            (row["campaign_id"],)).fetchone()[0]
        external = int(timing["time_resume"].get("external_cli_sessions", 0))
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                              (row["campaign_id"], row["product_id"])).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                             (row["campaign_id"],)).fetchone()[0]
        limits = request["limits"]
        if (calls + external != limits.get("expected_cli_total")
                or repairs != limits.get("expected_repairs") or active != 0):
            raise FactoryError("live budget changed before atomic version 5 activation", "budget_amendment_basis", 409)
        activated_at = float(self.clock())
        deadline = activated_at + int(row["window_seconds"])
        con.execute("UPDATE tf_budget_amendment SET activated_at=?,new_deadline=? WHERE id=? AND version=5 AND activated_at IS NULL",
                    (activated_at, deadline, amendment_id))
        return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def _validate_frozen_revision_request(self, request):
        required = {
            "schema", "campaign_id", "product_id", "plan_id", "source_ref", "source_digest",
            "summary", "reason", "idempotency_key", "source_gate", "limits", "timing",
            "prepared_revision", "prepared_revision_digest", "effective_plan_digest",
            "case_design_digest", "program_revision_digest",
        }
        if not isinstance(request, dict) or set(request) != required:
            raise FactoryError("version 5 authorization has missing or unknown fields", "budget_amendment_invalid", 400)
        for key in ("campaign_id", "product_id", "plan_id", "source_ref", "source_digest",
                    "summary", "reason", "idempotency_key", "prepared_revision_digest",
                    "effective_plan_digest", "case_design_digest", "program_revision_digest"):
            if not isinstance(request.get(key), str) or not request[key].strip():
                raise FactoryError("version 5 authorization fields must be non-empty strings", "budget_amendment_invalid", 400)
        if request["schema"] != "atlas.budget-amendment.v3":
            raise FactoryError("unsupported budget amendment schema", "budget_amendment_invalid", 400)
        if len(request["summary"]) > 2000 or len(request["reason"]) > 1000 or len(request["idempotency_key"]) > 200:
            raise FactoryError("amendment text exceeds limits", "budget_amendment_invalid", 400)
        if (self.campaign_id != request["campaign_id"] or not isinstance(request["limits"], dict)
                or not isinstance(request["timing"], dict) or not isinstance(request["source_gate"], dict)
                or not isinstance(request["prepared_revision"], dict)):
            raise FactoryError("version 5 authorization scope or objects are invalid", "budget_amendment_invalid", 400)
        if (set(request["limits"]) != {"cli_sessions", "expected_repairs", "repair_limit", "expected_cli_total"}
                or any(isinstance(value, bool) or not isinstance(value, int) or value < 0
                       for value in request["limits"].values())
                or request["limits"]["repair_limit"] <= request["limits"]["expected_repairs"]
                or set(request["timing"]) != {"window_seconds", "supersedes"}
                or isinstance(request["timing"].get("window_seconds"), bool)
                or not isinstance(request["timing"].get("window_seconds"), int)
                or request["timing"]["window_seconds"] <= 0
                or not isinstance(request["timing"].get("supersedes"), dict)
                or set(request["timing"]["supersedes"]) != {"deadline_source", "source_id", "activated_at",
                                                                "effective_deadline", "authorization_digest"}):
            raise FactoryError("version 5 limits or superseded timing source are malformed", "budget_amendment_invalid", 400)
        source_root = self.store.pack.resolve().parent
        source_relative = Path(request["source_ref"])
        if source_relative.is_absolute() or ".." in source_relative.parts:
            raise FactoryError("authorization source path is outside the repository", "budget_amendment_source", 400)
        source_path = source_root / source_relative
        cursor = source_root
        unsafe = False
        for part in source_relative.parts:
            cursor = cursor / part
            unsafe = unsafe or cursor.is_symlink()
        if unsafe or not source_path.is_file() or not source_path.resolve().is_relative_to(source_root):
            raise FactoryError("authorization source is unavailable or unsafe", "budget_amendment_source", 409)
        try:
            actual_source_digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("authorization source is unavailable", "budget_amendment_source", 409) from exc
        if actual_source_digest != request["source_digest"]:
            raise FactoryError("authorization source bytes changed", "budget_amendment_source", 409)
        if digest(request["prepared_revision"]) != request["prepared_revision_digest"]:
            raise FactoryError("prepared revision request digest changed", "budget_amendment_basis", 409)
        from .plan_revision import PreparedRevisionService
        prepared_binding = request["prepared_revision"].get("binding", {})
        job_id = prepared_binding.get("job_id")
        if not isinstance(job_id, str) or not job_id:
            raise FactoryError("prepared revision does not identify its source job", "budget_amendment_basis", 409)
        prepared = PreparedRevisionService(self.store).prepare(job_id, request["prepared_revision"])
        if (prepared.get("request_digest") != request["prepared_revision_digest"]
                or prepared.get("effective_plan_digest") != request["effective_plan_digest"]
                or digest(prepared.get("case_design")) != request["case_design_digest"]
                or digest(prepared.get("prepared_program_revision")) != request["program_revision_digest"]):
            raise FactoryError("prepared revision differs from its authorization digests", "budget_amendment_basis", 409)
        binding = prepared.get("binding", {})
        if (binding.get("campaign_id") != request["campaign_id"]
                or binding.get("plan_id") != request["plan_id"]
                or binding.get("product_id") != request["product_id"]):
            raise FactoryError("prepared revision identity is outside the authorized scope", "budget_amendment_scope", 403)
        from .evidence_recovery import validate_source_gate
        validate_source_gate(self.store, request["source_gate"])
        if (prepared.get("authorization_limits") != request["limits"]
                or prepared.get("authorization_timing") != request["timing"]):
            raise FactoryError("prepared authorization policy differs from budget request", "budget_amendment_basis", 409)
        source_auth = prepared.get("source_authorization") or request["prepared_revision"].get("source_authorization")
        if (not isinstance(source_auth, dict)
                or source_auth.get("source_ref") != request["source_ref"]
                or source_auth.get("source_digest") != request["source_digest"]):
            raise FactoryError("prepared revision is bound to a different authorization source", "budget_amendment_source", 409)
        return prepared

    def register_frozen_revision(self, request):
        request_digest = digest(request)
        encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self.store.connect(True) as con:
            prior = con.execute(
                "SELECT a.*,b.request_json,b.request_digest FROM tf_budget_amendment a "
                "LEFT JOIN tf_budget_amendment_binding b ON b.amendment_id=a.id "
                "WHERE a.campaign_id=? AND a.product_id=? AND a.idempotency_key=?",
                (request.get("campaign_id"), request.get("product_id"), request.get("idempotency_key")),
            ).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["request_json"] != encoded:
                    raise FactoryError("idempotency key is already bound to another request", "idempotency_conflict", 409)
                return {key: prior[key] for key in prior.keys() if key not in {"request_json", "request_digest"}}
            self._validate_frozen_revision_request(request)
            prior_v5 = con.execute("SELECT id FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND version=5",
                                   (request["campaign_id"], request["product_id"])).fetchone()
            if prior_v5:
                raise FactoryError("the single version 5 amendment is already registered", "budget_amendment_exhausted", 409)
            predecessor = con.execute(
                "SELECT * FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? "
                "AND version<5 AND activated_at IS NOT NULL ORDER BY version DESC LIMIT 1",
                (request["campaign_id"], request["product_id"]),
            ).fetchone()
            if (not predecessor or predecessor["activated_at"] is None
                    or predecessor["new_repair_limit"] != request["limits"].get("expected_repairs")):
                raise FactoryError("version 5 predecessor or repair baseline differs", "budget_amendment_basis", 409)
            timing = self.ledger._effective_timing_locked(con, request["product_id"], "G1", request["plan_id"])
            if timing["deadline_source"] != request["timing"].get("supersedes", {}).get("deadline_source"):
                raise FactoryError("current effective timing source differs from authorization", "budget_amendment_basis", 409)
            if request["timing"]["supersedes"] != self.ledger._timing_source_snapshot(timing["time_resume"]):
                raise FactoryError("superseded timing snapshot differs from current effective deadline", "budget_amendment_basis", 409)
            calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                (request["campaign_id"],)).fetchone()[0]
            external = int((timing["time_resume"] or {}).get("external_cli_sessions", 0))
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                  (request["campaign_id"], request["product_id"])).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                                 (request["campaign_id"],)).fetchone()[0]
            limits = request["limits"]
            if (calls + external != limits.get("expected_cli_total")
                    or calls != limits.get("expected_cli_total") - external
                    or repairs != limits.get("expected_repairs") or active != 0
                    or limits.get("cli_sessions") != self.ledger.limits["cli_sessions"]):
                raise FactoryError("live budget baseline differs from version 5 authorization", "budget_amendment_basis", 409)
            old_deadline = timing["deadline"]
            at = float(self.clock())
            amendment_id = "bamd_" + uuid.uuid4().hex
            con.execute(
                "INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,5,?,?,?,?,?,?,?,NULL,NULL)",
                (amendment_id, request["campaign_id"], request["product_id"], request["plan_id"],
                 request["source_ref"], request["source_digest"], request["summary"], request["reason"],
                 request["idempotency_key"], limits["expected_repairs"], limits["repair_limit"],
                 repairs, calls, old_deadline, request["timing"]["window_seconds"], at),
            )
            con.execute("INSERT INTO tf_budget_amendment_binding VALUES(?,?,?)",
                        (amendment_id, encoded, request_digest))
            return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate_r6_locked(self, con, amendment_id):
        """Activate v3 only from ProductRecoveryService's successor queue transaction."""
        if not getattr(con, "in_transaction", False):
            raise FactoryError("R6 activation requires the caller's atomic queue transaction", "budget_amendment_activation_denied", 409)
        row = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=?",
                          (amendment_id, self.campaign_id)).fetchone()
        if not row:
            raise FactoryError("R6 amendment not found", "not_found", 404)
        if row["version"] != 3 or self.campaign_id != G1_AMENDMENT_CAMPAIGN:
            raise FactoryError("source-alignment activation requires the exact version 3 amendment", "budget_amendment_version", 409)
        # A receipt is created later in this same transaction. An activated row
        # without one is inconsistent and must not be used to extend the window.
        if row["activated_at"] is not None or row["new_deadline"] is not None:
            raise FactoryError("R6 amendment was activated without its queue receipt", "budget_amendment_activation_conflict", 409)
        predecessor = con.execute("SELECT version,activated_at,new_repair_limit,new_deadline FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                  (G1_R6_PREDECESSOR_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
        base = con.execute("SELECT started,deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                           (G1_AMENDMENT_CAMPAIGN,)).fetchone()
        calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                            (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                              (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                             (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
        if (not predecessor or predecessor["version"] != 2 or predecessor["activated_at"] is None
                or predecessor["new_repair_limit"] != 5 or predecessor["new_deadline"] != G1_R6_OLD_DEADLINE
                or not base or base["deadline"] != G1_R5_BASE_DEADLINE
                or row["old_repair_limit"] != 5 or row["new_repair_limit"] != 6
                or row["old_deadline"] != G1_R6_OLD_DEADLINE or row["window_seconds"] != G1_R6_WINDOW_SECONDS
                or row["baseline_repair_count"] != 5 or row["baseline_cli_sessions"] != 64
                or calls != 64 or repairs != 5 or active != 0):
            raise FactoryError("R6 activation baseline or inherited V1/V2 deadline changed", "budget_amendment_basis", 409)
        binding = con.execute("SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                              (amendment_id,)).fetchone()
        if not binding:
            raise FactoryError("R6 authorization binding is missing", "budget_amendment_basis", 409)
        request = json.loads(binding["request_json"])
        if digest(request) != binding["request_digest"] or request.get("schema") != G1_R6_AUTHORIZATION_SCHEMA:
            raise FactoryError("R6 authorization binding is corrupt", "budget_amendment_basis", 409)
        at = float(self.clock())
        deadline = at + G1_R6_WINDOW_SECONDS
        con.execute("UPDATE tf_budget_amendment SET activated_at=?,new_deadline=? WHERE id=? AND version=3 AND activated_at IS NULL",
                    (at, deadline, amendment_id))
        return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate_r7_locked(self, con, amendment_id):
        """Activate v4 only inside the transaction that queues its one successor."""
        if not getattr(con, "in_transaction", False):
            raise FactoryError("R7 activation requires the atomic successor transaction", "budget_amendment_activation_denied", 409)
        row = con.execute("SELECT * FROM tf_budget_amendment WHERE id=? AND campaign_id=?",
                          (amendment_id, self.campaign_id)).fetchone()
        if not row:
            raise FactoryError("R7 amendment not found", "not_found", 404)
        if row["version"] != 4 or self.campaign_id != G1_AMENDMENT_CAMPAIGN:
            raise FactoryError("bounded-revision activation requires the exact version 4 amendment", "budget_amendment_version", 409)
        if row["activated_at"] is not None or row["new_deadline"] is not None:
            raise FactoryError("R7 amendment was activated without its queue receipt", "budget_amendment_activation_conflict", 409)
        predecessor = con.execute("SELECT version,activated_at,new_repair_limit,new_deadline FROM tf_budget_amendment WHERE id=? AND campaign_id=? AND product_id=?",
                                  (G1_R7_PREDECESSOR_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
        calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                            (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                              (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','spawn_intent','started','uncertain')",
                             (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
        retry_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                                 (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchall()
        retries = sum(1 for item in retry_rows if (item["retry_scope"] == "blueprint-spec-review:phase_acceptance"
                        if item["retry_scope"] is not None else
                        _legacy_retry_scope(item["stage"]) == "blueprint-spec-review:phase_acceptance"))
        grant = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id=? AND campaign_id=?",
                            (G1_R6_PROTOCOL_GRANT_ID, G1_AMENDMENT_CAMPAIGN)).fetchone()
        grant_use = con.execute("SELECT status FROM tf_protocol_retry_grant_use WHERE grant_id=? AND reservation_id=?",
                                (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID)).fetchone()
        if (not predecessor or predecessor["version"] != 3 or predecessor["activated_at"] is None
                or predecessor["new_repair_limit"] != 6 or predecessor["new_deadline"] != G1_R7_OLD_DEADLINE
                or row["old_repair_limit"] != 6 or row["new_repair_limit"] != 7
                or row["baseline_repair_count"] != 6 or row["baseline_cli_sessions"] != 71
                or row["old_deadline"] != G1_R7_OLD_DEADLINE or row["window_seconds"] != 0
                or calls != 71 or repairs != 6 or active != 0 or retries != 3
                or not grant or grant["status"] != "consumed"
                or grant["consumed_reservation_id"] != G1_R6_PROTOCOL_RESERVATION_ID
                or not grant_use or grant_use["status"] != "consumed"):
            raise FactoryError("R7 activation baseline or inherited deadline changed", "budget_amendment_basis", 409)
        binding = con.execute("SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                              (amendment_id,)).fetchone()
        if not binding:
            raise FactoryError("R7 authorization binding is missing", "budget_amendment_basis", 409)
        request = json.loads(binding["request_json"])
        if digest(request) != binding["request_digest"] or request.get("schema") != G1_R7_AUTHORIZATION_SCHEMA:
            raise FactoryError("R7 authorization binding is corrupt", "budget_amendment_basis", 409)
        if self._validate_r7_request(request) != binding["request_digest"]:
            raise FactoryError("R7 authorization no longer validates against its source and prepared material", "budget_amendment_basis", 409)
        at = float(self.clock())
        if at >= G1_R7_OLD_DEADLINE:
            raise FactoryError("inherited R6 deadline has expired", "budget_deadline", 409)
        con.execute("UPDATE tf_budget_amendment SET activated_at=?,new_deadline=? WHERE id=? AND version=4 AND activated_at IS NULL",
                    (at, G1_R7_OLD_DEADLINE, amendment_id))
        return dict(con.execute("SELECT * FROM tf_budget_amendment WHERE id=?", (amendment_id,)).fetchone())

    def activate(self, amendment_id):
        with self.store.connect(True) as con:
            return self.activate_locked(con, amendment_id)

    def list(self):
        with self.store.connect() as con:
            return [dict(row) for row in con.execute("SELECT * FROM tf_budget_amendment WHERE campaign_id=? ORDER BY version", (self.campaign_id,))]
