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
FROZEN_REVIEW_SCHEMA = "atlas.frozen-review-recovery-proposal.v1"
FROZEN_REVIEW_JOB = "job_b01427592b164863aab5bedf7b3863bb"
FROZEN_REVIEW_DEADLINE = 1792495312.855422
FROZEN_REVIEW_ADDITIONAL_KEY = "atlas-g1-r7-frozen-review-additional-2026-10-20-attempt3"


def get_call_binding(proposal):
    """Return the exact, versioned binding for a supported one-use grant.

    Keeping this dispatch explicit prevents a new recovery type from being
    mistaken for the old phase retry format merely because both carry fields
    named ``operation`` or ``payload``.
    """
    if not isinstance(proposal, dict):
        raise FactoryError("evidence grant proposal must be an object", "evidence_grant_schema", 400)
    schema = proposal.get("schema")
    materials = proposal.get("materials")
    if not isinstance(materials, dict):
        raise FactoryError("evidence grant materials are missing", "evidence_grant_binding", 409)
    if schema == SCHEMA:
        key = "new_phase"
    elif schema == FROZEN_REVIEW_SCHEMA:
        key = "frozen_review_call"
    else:
        raise FactoryError("unsupported evidence grant proposal schema", "evidence_grant_schema", 400)
    binding = materials.get(key)
    if not isinstance(binding, dict):
        raise FactoryError(f"{key} call binding is missing", "evidence_grant_binding", 409)
    return binding


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
        con.execute("CREATE TABLE IF NOT EXISTS tf_frozen_review_schema_migration(version INTEGER PRIMARY KEY,applied_at REAL NOT NULL,migration_digest TEXT NOT NULL)")
        con.execute(
            "CREATE TABLE IF NOT EXISTS tf_evidence_recovery_grant ("
            "id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,"
            "plan_id TEXT NOT NULL,job_id TEXT NOT NULL,request_key TEXT NOT NULL,"
            "proposal_digest TEXT NOT NULL,request_json TEXT NOT NULL,status TEXT NOT NULL,"
            "queued_job_id TEXT,consumed_reservation_id TEXT,call_attempt INTEGER,created_at REAL NOT NULL,"
            "UNIQUE(campaign_id,request_key))"
        )
        columns = {row[1] for row in con.execute("PRAGMA table_info(tf_evidence_recovery_grant)")}
        if "call_attempt" not in columns:
            con.execute("ALTER TABLE tf_evidence_recovery_grant ADD COLUMN call_attempt INTEGER")
        unique_job = False
        for index in con.execute("PRAGMA index_list(tf_evidence_recovery_grant)").fetchall():
            if not index[2]:
                continue
            cols = [col[2] for col in con.execute(f"PRAGMA index_info('{index[1]}')").fetchall()]
            if cols == ["campaign_id", "job_id"]:
                unique_job = True
                break
        if unique_job:
            custom_indexes = [row[0] for row in con.execute("SELECT sql FROM sqlite_master WHERE type='index' AND tbl_name='tf_evidence_recovery_grant' AND sql IS NOT NULL")]
            con.execute("ALTER TABLE tf_evidence_recovery_grant RENAME TO tf_evidence_recovery_grant_legacy")
            con.execute("""CREATE TABLE tf_evidence_recovery_grant (
                id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,
                plan_id TEXT NOT NULL,job_id TEXT NOT NULL,request_key TEXT NOT NULL,
                proposal_digest TEXT NOT NULL,request_json TEXT NOT NULL,status TEXT NOT NULL,
                queued_job_id TEXT,consumed_reservation_id TEXT,call_attempt INTEGER,created_at REAL NOT NULL,
                UNIQUE(campaign_id,request_key))""")
            con.execute("""INSERT INTO tf_evidence_recovery_grant
                (id,campaign_id,product_id,plan_id,job_id,request_key,proposal_digest,request_json,status,
                 queued_job_id,consumed_reservation_id,call_attempt,created_at)
                SELECT id,campaign_id,product_id,plan_id,job_id,request_key,proposal_digest,request_json,status,
                       queued_job_id,consumed_reservation_id,call_attempt,created_at
                FROM tf_evidence_recovery_grant_legacy""")
            con.execute("DROP TABLE tf_evidence_recovery_grant_legacy")
            for statement in custom_indexes:
                con.execute(statement)
        con.execute("INSERT OR IGNORE INTO tf_frozen_review_schema_migration VALUES(1,?,?)",
                    (time.time(), "grant-job-unique-to-sequential-v1"))

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
    def _verify_frozen_additional_baseline_locked(con, store):
        from .frozen_review_additional import (
            PREDECESSOR_GRANT, PREDECESSOR_RESERVATION, PREDECESSOR_ACCEPTANCE,
            PREDECESSOR_ACCEPTED_AT, DIAGNOSTIC_PATH, DIAGNOSTIC_SHA256,
        )
        calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN_ID,)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN_ID,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()[0]
        prior = con.execute("SELECT status,consumed_reservation_id,call_attempt FROM tf_evidence_recovery_grant WHERE id=?", (PREDECESSOR_GRANT,)).fetchone()
        reservation = con.execute("SELECT status,job_id,stage,finished,outcome FROM tf_budget_reservation WHERE id=?", (PREDECESSOR_RESERVATION,)).fetchone()
        acceptance = con.execute("SELECT job_id,body,created_at FROM acceptance WHERE id=?", (PREDECESSOR_ACCEPTANCE,)).fetchone()
        batches = [con.execute("SELECT state FROM batch WHERE id=?", (batch_id,)).fetchone()
                   for batch_id in ("bat_6b4fc8bf5b4e42d79bc6a9069277e9f0", "bat_d13dc5920a574140be85da0ea6f5395b")]
        try:
            import hashlib
            import json
            path = store.pack.parent / DIAGNOSTIC_PATH
            raw = path.read_bytes()
            diagnostic = json.loads(raw)
            diag_ok = (hashlib.sha256(raw).hexdigest() == DIAGNOSTIC_SHA256
                       and diagnostic.get("cli_invocations") == 1 and diagnostic.get("result") == "passed"
                       and diagnostic.get("provider_model") == "opencode-go/deepseek-v4.1-flash"
                       and diagnostic.get("g1_resumed") is False and diagnostic.get("g1_ledger_baseline") == 81
                       and diagnostic.get("exit_code") == 0 and diagnostic.get("tool_events") == 0
                       and diagnostic.get("timeout_seconds") == 60)
        except (OSError, ValueError, TypeError):
            diag_ok = False
        body = json.loads(acceptance["body"]) if acceptance else {}
        if (calls != 81 or active != 0 or repairs != 7 or not prior or prior["status"] != "consumed"
                or prior["consumed_reservation_id"] != PREDECESSOR_RESERVATION or prior["call_attempt"] != 2
                or not reservation or reservation["status"] != "failed" or reservation["job_id"] != FROZEN_REVIEW_JOB
                or reservation["finished"] is None or abs(float(reservation["finished"]) - 1792490680.240822) > 1e-6
                or reservation["outcome"] != "cli_failed" or reservation["stage"] != "cognitive-review:572da86649b4face"
                or not acceptance or acceptance["job_id"] != FROZEN_REVIEW_JOB
                or acceptance["created_at"] != PREDECESSOR_ACCEPTED_AT
                or body.get("job_attempt") != 2 or body.get("outcome") != "unavailable"
                or body.get("code") != "cli_failed" or any(not b or b["state"] != "paused" for b in batches)
                or not diag_ok):
            raise FactoryError("additional frozen-review predecessor, ledger or diagnostic baseline changed", "evidence_grant_baseline", 409)

    @staticmethod
    def _proposal_digest(proposal):
        return digest({key: value for key, value in proposal.items() if key != "proposal_digest"})

    def _validate_proposal(self, proposal, request):
        if isinstance(proposal, dict) and proposal.get("schema") == FROZEN_REVIEW_SCHEMA:
            return self._validate_frozen_proposal(proposal, request)
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

    def _validate_frozen_proposal(self, proposal, request):
        if not isinstance(request, dict):
            raise FactoryError("frozen-review registration request must be an object", "evidence_grant_binding", 400)
        if proposal.get("proposal_digest") != self._proposal_digest(proposal):
            raise FactoryError("frozen-review proposal digest does not match", "evidence_grant_binding", 409)
        request_key = proposal.get("request_key")
        supplied = request.get("request_key") if isinstance(request, dict) else None
        if not isinstance(request_key, str) or supplied != request_key:
            raise FactoryError("frozen-review request key differs", "evidence_grant_binding", 403)
        additional = proposal.get("request_key") == FROZEN_REVIEW_ADDITIONAL_KEY
        request_fields = {"schema", "request_key", "source_authorization", "source_gate", "timing_override_authorization"} if additional else {"schema", "request_key", "source_authorization", "source_gate"}
        if (set(request) != request_fields or request.get("schema") != "atlas.frozen-review-prepare.v1"
                or request.get("source_authorization") != proposal.get("source_authorization")
                or (additional and request.get("timing_override_authorization") != proposal.get("timing_override_authorization"))
                or request.get("source_gate") != proposal.get("source_gate")):
            raise FactoryError("frozen-review registration request differs from proposal", "evidence_grant_binding", 409)
        from .frozen_review_additional import (
            REQUEST_KEY as ADDITIONAL_KEY, AUTH_REF as ADDITIONAL_AUTH_REF,
            AUTH_SHA256 as ADDITIONAL_AUTH_SHA256, TIMING_AUTH_REF,
            TIMING_AUTH_SHA256, PREDECESSOR_AUTH_REF, PREDECESSOR_AUTH_SHA256,
        )
        additional = proposal.get("request_key") == ADDITIONAL_KEY
        authorization = proposal.get("source_authorization")
        if additional:
            if (authorization != {"source_ref": ADDITIONAL_AUTH_REF, "source_digest": ADDITIONAL_AUTH_SHA256}
                    or proposal.get("timing_override_authorization") != {"source_ref": TIMING_AUTH_REF, "source_digest": TIMING_AUTH_SHA256}
                    or proposal.get("predecessor_source_authorization") != {"source_ref": PREDECESSOR_AUTH_REF, "source_digest": PREDECESSOR_AUTH_SHA256}
                or request.get("timing_override_authorization") != proposal["timing_override_authorization"]):
                raise FactoryError("additional frozen-review authorizations differ", "evidence_grant_binding", 403)
            for ref, sha in ((ADDITIONAL_AUTH_REF, ADDITIONAL_AUTH_SHA256),
                             (TIMING_AUTH_REF, TIMING_AUTH_SHA256),
                             (PREDECESSOR_AUTH_REF, PREDECESSOR_AUTH_SHA256)):
                try:
                    actual = hashlib.sha256((self.store.pack.parent / ref).read_bytes()).hexdigest()
                except OSError as exc:
                    raise FactoryError("additional frozen-review authorization is unavailable", "evidence_grant_source", 409) from exc
                if actual != sha:
                    raise FactoryError("additional frozen-review authorization bytes differ", "evidence_grant_source", 409)
        else:
            auth_ref = "docs/template-factory/g1-frozen-review-recovery-2026-10-20/authorization/ATLAS_G1_FROZEN_REVIEW_RECOVERY_CODEX_INSTRUCTIONS.txt"
            auth_digest = "65976f3c72613dfc7208d86cea7ce4c9ec0688ef04c881efba8abacf7f642101"
            if authorization != {"source_ref": auth_ref, "source_digest": auth_digest}:
                raise FactoryError("frozen-review authorization differs", "evidence_grant_binding", 403)
            try:
                actual = hashlib.sha256((self.store.pack.parent / auth_ref).read_bytes()).hexdigest()
            except OSError as exc:
                raise FactoryError("frozen-review authorization source is unavailable", "evidence_grant_source", 409) from exc
            if actual != auth_digest:
                raise FactoryError("frozen-review authorization bytes differ", "evidence_grant_source", 409)
        materials = proposal.get("materials")
        binding = materials.get("binding") if isinstance(materials, dict) else None
        call = materials.get("frozen_review_call") if isinstance(materials, dict) else None
        fixed = {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                 "job_id": "job_b01427592b164863aab5bedf7b3863bb", "attempt": 2 if additional else 1,
                 "snapshot_digest": "db51b4ca834dd031135025d761b46407f02b2850ad993c950f55407a0f95fcf6",
                 "batch_id": "bat_6b4fc8bf5b4e42d79bc6a9069277e9f0", "deadline": 1792495312.855422,
                 "artifact_id": "tpl_f7ecff8d8fef4deba828aa2a8ef82918",
                 "artifact_digest": "ec3f2fc668c20d24b78c22f15eed40779ed38b835c10b7b452aaba725dbb7105"}
        if not isinstance(binding, dict) or any(binding.get(k) != v for k, v in fixed.items()):
            raise FactoryError("frozen-review binding differs from the fixed job", "evidence_grant_binding", 409)
        required = ("payload", "input_json", "prompt", "input_sha256", "full_payload_digest", "budget_input_digest", "prompt_sha256",
                    "source_tree_digest", "projection_digest", "stage_name", "operation", "logical_retry_scope",
                    "requested_model", "cli_config_identity", "materials_manifest_digest", "materials_tree_digest", "leaf_sha256")
        if not isinstance(call, dict) or any(key not in call for key in required):
            raise FactoryError("frozen-review call binding is incomplete", "evidence_grant_binding", 409)
        if (call["stage_name"] != "cognitive-review" or call["logical_retry_scope"] != "cognitive-review"
                or call["operation"] != "cognitive-review:572da86649b4face"
                or call["requested_model"] != "opencode-go/deepseek-v4.1-flash"
                or digest(call["payload"]) != call["full_payload_digest"]
                or digest({k: v for k, v in call["payload"].items() if k != "language"}) != call["budget_input_digest"]
                or call["timeout_seconds"] != 1800):
            raise FactoryError("frozen-review call identity differs", "evidence_grant_binding", 409)
        try:
            from .cognition import REVIEW_PROMPT
            from .frozen_review_materials import append_review_prompt
            derived_prompt, _ = append_review_prompt(REVIEW_PROMPT)
            input_json = call["input_json"]
            if (hashlib.sha256(input_json.encode("utf-8")).hexdigest() != call["input_sha256"]
                    or json.loads(input_json) != call["payload"]
                    or derived_prompt != call["prompt"]
                    or hashlib.sha256(derived_prompt.encode("utf-8")).hexdigest() != call["prompt_sha256"]):
                raise ValueError("call bytes differ")
        except (KeyError, ValueError, TypeError) as exc:
            raise FactoryError("frozen-review raw call binding is invalid", "evidence_grant_binding", 409) from exc
        old = materials.get("old_phase")
        if (not isinstance(old, dict) or old.get("reservation_id") != "bud_0be070e3a2624ce3989d7eaec26da107"
                or old.get("input_sha256") != "394209fae774d75bcf1fa06c4eb091f26c727438836476cb86471c3adbc1d242"
                or old.get("full_payload_digest") != "b4061425b435f346cd6b5e19745185ad99bebee3b5a3b983759e28e56ff6b0fa"
                or old.get("budget_input_digest") != "572da86649b4faced76c4c2e4f4d91102be17ef6b2127ec1572a8d44c4c28d38"
                or old.get("prompt_sha256") != "9cdd40b5ee69c3b14675fa60569b9f9fb948949dd7be493fe6ff7436a1c9ce09"
                or old.get("summary_sha256") != "d5c9b3ae369bd3c0f079de9ceb1c661accdb2d24435c3a54872ce9adccba8f72"):
            raise FactoryError("original frozen review call differs", "evidence_grant_binding", 409)
        if additional:
            from .frozen_review_additional import (
                REMAINING_SECONDS, PREDECESSOR_GRANT, PREDECESSOR_RESERVATION,
                PREDECESSOR_ACCEPTANCE, PREDECESSOR_AUTH_REF, PREDECESSOR_AUTH_SHA256,
                DIAGNOSTIC_PATH, DIAGNOSTIC_SHA256,
            )
            timing = proposal.get("timing_policy")
            if (proposal.get("predecessor_source_authorization") != {"source_ref": PREDECESSOR_AUTH_REF, "source_digest": PREDECESSOR_AUTH_SHA256}
                    or timing != {"remaining_seconds": REMAINING_SECONDS, "external_cli_sessions": 1,
                                  "previous_deadline": 1792495312.855422, "paused_at": 1792490680.244128}
                    or binding.get("predecessor_grant_id") != PREDECESSOR_GRANT
                    or binding.get("predecessor_reservation_id") != PREDECESSOR_RESERVATION
                    or binding.get("predecessor_acceptance_id") != PREDECESSOR_ACCEPTANCE
                    or binding.get("diagnostic_source_ref") != DIAGNOSTIC_PATH
                    or binding.get("diagnostic_source_digest") != DIAGNOSTIC_SHA256
                    or binding.get("attempt") != 2
                    or not isinstance(binding.get("predecessor_summary_sha256"), str)
                    or len(binding["predecessor_summary_sha256"]) != 64
                    or any(ch not in "0123456789abcdef" for ch in binding["predecessor_summary_sha256"])):
                raise FactoryError("additional frozen-review predecessor or restored timing differs", "evidence_grant_binding", 409)
        self._verify_source_gate(proposal)
        if not additional and float(self.clock()) >= 1792495312.855422:
            raise FactoryError("frozen-review deadline has passed", "budget_deadline", 409)
        return request_key, binding, call

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
        if not isinstance(prepared_proposal, dict) or prepared_proposal.get("schema") not in {SCHEMA, FROZEN_REVIEW_SCHEMA}:
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
            existing_for_job = con.execute(
                "SELECT id,status,consumed_reservation_id,request_key FROM tf_evidence_recovery_grant WHERE campaign_id=? AND job_id=?",
                (CAMPAIGN_ID, binding.get("job_id", JOB_ID)),
            ).fetchall()
            additional = request_key == FROZEN_REVIEW_ADDITIONAL_KEY
            if existing_for_job:
                from .frozen_review_additional import PREDECESSOR_GRANT, PREDECESSOR_RESERVATION
                if (not additional or len(existing_for_job) != 1
                        or existing_for_job[0]["id"] != PREDECESSOR_GRANT
                        or existing_for_job[0]["status"] != "consumed"
                        or existing_for_job[0]["consumed_reservation_id"] != PREDECESSOR_RESERVATION):
                    raise FactoryError("this frozen job already has an unrelated recovery grant", "evidence_grant_conflict", 409)
            elif additional:
                raise FactoryError("additional frozen-review recovery requires its consumed predecessor grant", "evidence_grant_conflict", 409)
            if prepared_proposal.get("schema") == SCHEMA:
                self._verify_budget_baseline_locked(con)
            elif additional:
                self._verify_frozen_additional_baseline_locked(con, self.store)
            else:
                from .frozen_review_recovery import FrozenReviewRecoveryService
                FrozenReviewRecoveryService(self.store, clock=self.clock)._verify_baseline_locked(con)
            grant_id = "egrant_" + uuid.uuid4().hex
            now = float(self.clock())
            con.execute(
                "INSERT INTO tf_evidence_recovery_grant(id,campaign_id,product_id,plan_id,job_id,request_key,proposal_digest,request_json,status,created_at) VALUES(?,?,?,?,?,?,?,?,'registered',?)",
                (grant_id, CAMPAIGN_ID, PRODUCT_ID, PLAN_ID, binding.get("job_id", JOB_ID), request_key,
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
    def occupy_locked(cls, con, grant_id, context, reservation_id, now, *, campaign_id, identity, plan_id, job_id, phase, stage, retry, retry_scope, requested_model, kind, deadline, timeout=None):
        row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()
        if row is None:
            raise FactoryError("evidence recovery grant not found", "evidence_grant_missing", 404)
        if row["status"] != "queued" or row["queued_job_id"] != job_id:
            raise FactoryError("evidence recovery grant is not available for this queued job", "evidence_grant_used", 409)
        proposal = json.loads(row["request_json"])
        materials = proposal["materials"]
        binding = materials["binding"]
        expected_phase = get_call_binding(proposal)
        owner = con.execute("SELECT state,attempt FROM job WHERE id=?", (job_id,)).fetchone()
        frozen = proposal.get("schema") == FROZEN_REVIEW_SCHEMA
        additional = proposal.get("request_key") == FROZEN_REVIEW_ADDITIONAL_KEY
        expected_job = FROZEN_REVIEW_JOB if frozen else JOB_ID
        expected_deadline = FROZEN_REVIEW_DEADLINE if frozen else OLD_DEADLINE
        effective_deadline = expected_deadline
        if additional:
            from .frozen_review_additional import get_time_resume_locked
            resume = get_time_resume_locked(con, campaign_id=campaign_id, product_id=identity,
                                            plan_id=plan_id, grant_id=grant_id)
            if resume is None:
                raise FactoryError("additional frozen-review timing window is not activated", "budget_deadline", 409)
            effective_deadline = float(resume["effective_deadline"])
        expected_scope = expected_phase.get("logical_retry_scope")
        expected_model = expected_phase.get("requested_model")
        if (campaign_id != CAMPAIGN_ID or identity != PRODUCT_ID or plan_id != PLAN_ID
                or job_id != expected_job or phase != "G1" or retry != 1
                or retry_scope != expected_scope or kind != "review"
                or str(stage) != str(expected_phase.get("operation"))
                or requested_model != expected_model
                or owner is None or owner["state"] != "running" or owner["attempt"] < 2
                or binding.get("deadline") != expected_deadline
                or float(deadline) != effective_deadline or float(now) >= effective_deadline
                or (frozen and not additional and owner["attempt"] not in {2, 3, 4})
                or (additional and owner["attempt"] != 3)):
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
        if frozen:
            extra_fields = ("materials_manifest_digest", "materials_tree_digest", "cli_config_identity")
            for key in extra_fields:
                if context.get(key) != expected_phase.get(key):
                    raise FactoryError("frozen-review materials or ACL differ from the grant", "evidence_grant_binding", 409)
            if context.get("timeout_seconds") != 1800:
                raise FactoryError("frozen-review timeout differs from the grant", "evidence_grant_binding", 409)
            if timeout != 1800:
                raise FactoryError("frozen-review reservation timeout must be exactly 1800 seconds", "evidence_grant_binding", 409)
        con.execute("UPDATE tf_evidence_recovery_grant SET status='reserved',consumed_reservation_id=?,call_attempt=? WHERE id=? AND status='queued'",
                    (reservation_id, owner["attempt"], grant_id))
        return {"id": grant_id, "proposal_digest": row["proposal_digest"], "reservation_id": reservation_id,
                "request_key": row["request_key"], "deadline": binding["deadline"],
                "call_attempt": owner["attempt"], "reserved_at": now}

