"""One-use authorization for the fixed G1 phase-acceptance protocol retry."""

from __future__ import annotations

import hashlib
import json
import time
import uuid

from .budget import G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT
from .store import FactoryError, digest

SCHEMA = "atlas.protocol-retry-grant.v1"
SOURCE_REF = "docs/template-factory/g1-protocol-recovery-2026-10-19/authorization/ATLAS_G1_PROTOCOL_RETRY_CODEX_INSTRUCTIONS.txt"
SOURCE_DIGEST = "6592fdddfa743947cba4fcd685e3dc36d62e665203cac2c9a20ba029ee3f5829"
IDEMPOTENCY_KEY = "atlas-g1-phase-protocol-once-2026-10-19-v1"
JOB_ID = "job_7742b1c124be4c9ab3a0096da5cdd772"
SOURCE_FAILURE_RESERVATION_ID = "bud_1806199dfa08411d8f71ee84ea06676f"
STAGE = "blueprint-spec-review-0-bbc43771a1bbbe99-phase_acceptance"
OPERATION_ID = STAGE + ":449b8a5093505d77"
RETRY_SCOPE = "blueprint-spec-review:phase_acceptance"
INPUT_DIGEST = "449b8a5093505d77cf97ec22db4d9f9a952ff15e324a92da140bc93b3b05bd23"
INPUT_SHA256 = "44e258910a36e18c6bae070dbcc6a003c345a7f9623f6f2b474b5de633ed0c97"
PROMPT_SHA256 = "c8ae350e5eb1b66a0f4de936a3d39ca862eab6351758069f8f613d72cac84480"
SOURCE_TREE_DIGEST = "4cf088a2964bca2a1917f50505e675d7c5f580694b88c103c98e15eee250695c"
PROJECTION_DIGEST = SOURCE_TREE_DIGEST
PROPOSAL_DIGEST = "f190b65275ab7c7136f523ba92aecde7c9392440d7676b070393e62ff9137b58"
STDOUT_SHA256 = "00227a3ec72d61eb677d39174f042078cdff5969d0df248771fa630d57ad1b20"
REQUESTED_MODEL = "opencode-go/deepseek-v4.1-flash"
DEADLINE = 1792437223.754534
CHECKPOINT_NAMES = ("scenario_scope", "product_completeness", "architecture_contract")
CONTEXT_KEYS = ("input_digest", "input_sha256", "prompt_sha256", "source_tree_digest", "projection_digest")


def protocol_retry_request(store):
    """Return the exact stable registration request for CLI/service use."""
    return {
        "schema": SCHEMA, "campaign_id": G1_AMENDMENT_CAMPAIGN,
        "plan_id": G1_AMENDMENT_PLAN, "product_id": G1_AMENDMENT_PRODUCT,
        "job_id": JOB_ID, "source_failure_reservation_id": SOURCE_FAILURE_RESERVATION_ID,
        "operation_id": OPERATION_ID, "logical_retry_scope": RETRY_SCOPE,
        "source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST,
        "idempotency_key": IDEMPOTENCY_KEY,
        "input_digest": INPUT_DIGEST, "input_sha256": INPUT_SHA256,
        "prompt_sha256": PROMPT_SHA256, "source_tree_digest": SOURCE_TREE_DIGEST,
        "projection_digest": PROJECTION_DIGEST, "proposal_digest": PROPOSAL_DIGEST,
        "requested_model": REQUESTED_MODEL, "stdout_sha256": STDOUT_SHA256,
        "checkpoint_names": list(CHECKPOINT_NAMES), "deadline": DEADLINE,
        "baseline_cli_sessions": 56, "baseline_product_repairs": 5,
        "baseline_scope_retries": 2, "max_extra_calls": 1,
    }


class ProtocolRetryGrantService:
    """Append-only grant service; the ledger claims the grant with its reservation."""

    def __init__(self, store, *, clock=time.time, initialize=True):
        self.store, self.clock = store, clock
        if initialize:
            # Ensures grant tables exist before callers use this service directly.
            from .budget import BudgetLedger
            self.ledger = BudgetLedger(store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=clock)

    def validate_context(self, context):
        if not isinstance(context, dict) or set(context) != set(CONTEXT_KEYS):
            raise FactoryError("protocol retry context must contain the five fixed digests", "protocol_grant_binding", 409)
        expected = {"input_digest": INPUT_DIGEST, "input_sha256": INPUT_SHA256,
                    "prompt_sha256": PROMPT_SHA256, "source_tree_digest": SOURCE_TREE_DIGEST,
                    "projection_digest": PROJECTION_DIGEST}
        if context != expected:
            raise FactoryError("protocol retry input, prompt, projection or source differs from the grant", "protocol_grant_binding", 409)
        return True

    def _verify_source(self, request):
        source_path = self.store.pack.parent / SOURCE_REF
        try:
            actual = hashlib.sha256(source_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise FactoryError("protocol authorization source is unavailable", "protocol_grant_source", 409) from exc
        if actual != SOURCE_DIGEST or request["source_digest"] != actual:
            raise FactoryError("protocol authorization source bytes changed", "protocol_grant_source", 409)

    def _verify_fixed_evidence(self):
        from .artifacts import tree_manifest
        from .cognition import DESIGN_REVIEW_PROMPT
        evidence = (self.store.root / "jobs" / JOB_ID / "attempt-1" / STAGE)
        try:
            raw_input = (evidence / "input.json").read_bytes()
            raw_stdout = (evidence / "stdout.log").read_bytes()
            summary = json.loads((evidence / "cli-summary.json").read_text(encoding="utf-8"))
            payload = json.loads(raw_input)
            source_digest = digest(tree_manifest(evidence / "source"))
            prompt_digest = hashlib.sha256(DESIGN_REVIEW_PROMPT.encode("utf-8")).hexdigest()
        except (OSError, ValueError, TypeError) as exc:
            raise FactoryError("fixed failed-operation evidence is unavailable", "protocol_grant_basis", 409) from exc
        input_without_language = dict(payload)
        input_without_language.pop("language", None)
        if (hashlib.sha256(raw_input).hexdigest() != INPUT_SHA256
                or digest(input_without_language) != INPUT_DIGEST
                or payload.get("projection_digest") != PROJECTION_DIGEST
                or source_digest != SOURCE_TREE_DIGEST or prompt_digest != PROMPT_SHA256
                or hashlib.sha256(raw_stdout).hexdigest() != STDOUT_SHA256
                or summary.get("requested_model") != REQUESTED_MODEL
                or summary.get("stdout_sha256") != STDOUT_SHA256
                or summary.get("delivery_status") != "failed"
                or summary.get("failure_code") != "cli_protocol"):
            raise FactoryError("fixed failed-operation input, prompt, source or stdout bytes changed", "protocol_grant_basis", 409)

    def _validate_request(self, request):
        fixed = protocol_retry_request(self.store)
        if not isinstance(request, dict) or request != fixed:
            raise FactoryError("protocol retry request differs from the fixed G1 authorization", "protocol_grant_binding", 403)
        self._verify_source(request)
        self._verify_fixed_evidence()
        self.validate_context({key: request[key] for key in CONTEXT_KEYS})

    def register(self, request):
        encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        request_digest = digest(request)
        with self.store.connect(True) as con:
            prior = con.execute("SELECT * FROM tf_protocol_retry_grant WHERE campaign_id=? AND idempotency_key=?",
                                (G1_AMENDMENT_CAMPAIGN, IDEMPOTENCY_KEY)).fetchone()
            if prior:
                if prior["request_digest"] != request_digest or prior["request_json"] != encoded:
                    raise FactoryError("protocol grant idempotency key is bound to another request", "idempotency_conflict", 409)
                return self._public(prior)
            self._validate_request(request)
            if con.execute("SELECT 1 FROM tf_protocol_retry_grant WHERE campaign_id=? AND product_id=? AND job_id=?",
                           (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, JOB_ID)).fetchone():
                raise FactoryError("the fixed protocol retry opportunity is already registered", "protocol_grant_exhausted", 409)
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                  (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                   (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')",
                                 (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0]
            retry_rows = con.execute("SELECT retry_scope,stage FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND retry IS NOT NULL AND status!='not_started'",
                                     (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchall()
            from .budget import _legacy_retry_scope
            scope_count = sum(1 for row in retry_rows if (row[0] == RETRY_SCOPE if row[0] is not None else _legacy_retry_scope(row[1]) == RETRY_SCOPE))
            original = con.execute("SELECT * FROM tf_budget_reservation WHERE id=? AND campaign_id=?",
                                   (SOURCE_FAILURE_RESERVATION_ID, G1_AMENDMENT_CAMPAIGN)).fetchone()
            job = con.execute("SELECT id,state,stage,attempt,error,snapshot FROM job WHERE id=?", (JOB_ID,)).fetchone()
            deadline_row = con.execute("SELECT deadline FROM tf_budget_phase WHERE campaign_id=? AND identity='__campaign_segment__' AND phase='G1'",
                                       (G1_AMENDMENT_CAMPAIGN,)).fetchone()
            predecessor = con.execute("SELECT new_deadline FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? AND version=2 AND activated_at IS NOT NULL",
                                      (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()
            effective_deadline = predecessor[0] if predecessor else (deadline_row[0] if deadline_row else None)
            if (sessions != 56 or repairs != 5 or active != 0 or scope_count != 2
                    or effective_deadline != DEADLINE or float(self.clock()) >= DEADLINE
                    or not original or original["job_id"] != JOB_ID or original["identity"] != G1_AMENDMENT_PRODUCT
                    or original["phase"] != "G1" or original["stage"] != OPERATION_ID
                    or original["status"] != "failed" or original["retry"] is not None
                    or original["outcome"] != "cli_protocol" or original["requested_model"] != REQUESTED_MODEL
                    or not job or job["state"] != "paused_budget" or job["attempt"] != 2
                    or job["stage"] != STAGE or "budget_retry_limit" not in (job["error"] or "")):
                raise FactoryError("current G1 failure or CLI/repair/retry/deadline baseline does not match authorization",
                                   "protocol_grant_basis", 409)
            snapshot = json.loads(job["snapshot"])
            plan = snapshot.get("v1", {})
            if (plan.get("plan_id") != G1_AMENDMENT_PLAN or plan.get("product_id") != G1_AMENDMENT_PRODUCT
                    or plan.get("campaign_id") != G1_AMENDMENT_CAMPAIGN):
                raise FactoryError("paused job snapshot differs from fixed campaign, plan or product", "protocol_grant_basis", 409)
            grant_id = "pgrant_" + uuid.uuid4().hex
            con.execute("INSERT INTO tf_protocol_retry_grant(id,campaign_id,plan_id,product_id,job_id,source_ref,source_digest,request_json,request_digest,idempotency_key,status,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (grant_id, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT,
                         JOB_ID, SOURCE_REF, SOURCE_DIGEST, encoded, request_digest, IDEMPOTENCY_KEY,
                         "available", float(self.clock())))
            return self._public(con.execute("SELECT * FROM tf_protocol_retry_grant WHERE id=?", (grant_id,)).fetchone())

    def _public(self, row):
        out = dict(row)
        request = json.loads(out.pop("request_json"))
        out.update(request)
        return out

    def get(self, grant_id):
        with self.store.connect() as con:
            row = con.execute("SELECT * FROM tf_protocol_retry_grant WHERE id=?", (str(grant_id),)).fetchone()
        if not row:
            raise FactoryError("protocol retry grant not found", "not_found", 404)
        return self._public(row)

    def validate_binding_locked(self, con, grant_row, context):
        self.validate_context(context)
        if (not grant_row or grant_row["campaign_id"] != G1_AMENDMENT_CAMPAIGN
                or grant_row["plan_id"] != G1_AMENDMENT_PLAN
                or grant_row["product_id"] != G1_AMENDMENT_PRODUCT
                or grant_row["job_id"] != JOB_ID or grant_row["status"] != "available"
                or float(self.clock()) >= DEADLINE):
            raise FactoryError("protocol retry grant is unavailable, expired or outside its fixed binding", "protocol_grant_exhausted", 409)
        stored = json.loads(grant_row["request_json"])
        if stored != protocol_retry_request(self.store) or digest(stored) != grant_row["request_digest"]:
            raise FactoryError("persisted protocol grant binding is corrupt or changed", "protocol_grant_binding", 409)
        self.validate_context({key: stored[key] for key in CONTEXT_KEYS})
        return True

    def find_for_reservation_locked(self, con, *, identity, phase, plan_id, job_id, stage,
                                    requested_model, retry, retry_scope, context, kind, campaign_id):
        if (identity != G1_AMENDMENT_PRODUCT or phase != "G1" or plan_id != G1_AMENDMENT_PLAN
                or job_id != JOB_ID or stage != OPERATION_ID or requested_model != REQUESTED_MODEL
                or retry != 1 or retry_scope != RETRY_SCOPE or kind != "review"
                or campaign_id != G1_AMENDMENT_CAMPAIGN):
            return None
        rows = con.execute("SELECT * FROM tf_protocol_retry_grant WHERE campaign_id=? AND product_id=? AND job_id=?",
                           (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, JOB_ID)).fetchall()
        if len(rows) != 1:
            return None
        try:
            self.validate_binding_locked(con, rows[0], context)
        except FactoryError as exc:
            if exc.code == "protocol_grant_binding":
                raise
            return None
        row = rows[0]
        return {"id": row["id"]}

