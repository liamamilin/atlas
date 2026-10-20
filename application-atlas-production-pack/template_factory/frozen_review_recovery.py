"""Strict recovery and delivery binding for the one frozen cognitive review."""
from __future__ import annotations

import hashlib
import json
import time
import uuid
from pathlib import Path

from .store import FactoryError, canonical, digest, now

SCHEMA = "atlas.frozen-review-recovery-proposal.v1"
JOB_ID = "job_b01427592b164863aab5bedf7b3863bb"
CAMPAIGN_ID = "atlas-v1-first-production-2026-10-19"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"
BATCH_ID = "bat_6b4fc8bf5b4e42d79bc6a9069277e9f0"
ARTIFACT_ID = "tpl_f7ecff8d8fef4deba828aa2a8ef82918"
ARTIFACT_DIGEST = "ec3f2fc668c20d24b78c22f15eed40779ed38b835c10b7b452aaba725dbb7105"
OLD_ACCEPTANCE_ID = "acc_74476c79fca949a7a0bd4e4c043d31a6"
SNAPSHOT_DIGEST = "db51b4ca834dd031135025d761b46407f02b2850ad993c950f55407a0f95fcf6"
DEADLINE = 1792495312.855422
AUTH_REF = "docs/template-factory/g1-frozen-review-recovery-2026-10-20/authorization/ATLAS_G1_FROZEN_REVIEW_RECOVERY_CODEX_INSTRUCTIONS.txt"
AUTH_SHA256 = "65976f3c72613dfc7208d86cea7ce4c9ec0688ef04c881efba8abacf7f642101"
RETRY_SCOPE = "cognitive-review"
REQUEST_KEY = "atlas-g1-r7-frozen-review-recovery-2026-10-20-once"
OLD_RAW_SHA = "394209fae774d75bcf1fa06c4eb091f26c727438836476cb86471c3adbc1d242"
OLD_PAYLOAD_DIGEST = "b4061425b435f346cd6b5e19745185ad99bebee3b5a3b983759e28e56ff6b0fa"
OLD_BUDGET_DIGEST = "572da86649b4faced76c4c2e4f4d91102be17ef6b2127ec1572a8d44c4c28d38"
OLD_PROMPT_SHA = "9cdd40b5ee69c3b14675fa60569b9f9fb948949dd7be493fe6ff7436a1c9ce09"
OLD_SUMMARY_SHA = "d5c9b3ae369bd3c0f079de9ceb1c661accdb2d24435c3a54872ce9adccba8f72"
ORIGINAL_RESERVATION = "bud_0be070e3a2624ce3989d7eaec26da107"


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _parse_original_response(directory, original_raw):
    from .cli import parse_result, recover_cognitive_framing
    original_text = json.loads(original_raw).get("text")
    if not isinstance(original_text, str):
        raise ValueError("original response text is missing")
    try:
        return parse_result(original_text, redundant_closing=True)
    except FactoryError:
        result, receipt = recover_cognitive_framing(original_text)
        if json.loads((directory / "framing-recovery.json").read_bytes()) != receipt:
            raise ValueError("original framing recovery receipt differs")
        return result


class FrozenReviewRecoveryService:
    def __init__(self, store, *, clock=time.time, materials_builder=None, source_gate_validator=None):
        self.store, self.clock, self.materials_builder = store, clock, materials_builder
        self.source_gate_validator = source_gate_validator

    def _materials(self, input_raw, leaf_raw, source_dir):
        from .frozen_review_materials import build_materials
        return (self.materials_builder or build_materials)(input_raw, leaf_raw, source_dir)

    def _assert_live_source_gate(self, proposal):
        gate = proposal.get("source_gate") if isinstance(proposal, dict) else None
        if not isinstance(gate, dict) or not isinstance(gate.get("source_tree_digest"), str):
            raise FactoryError("frozen-review source gate is missing", "evidence_source_gate", 409)
        from .v1_batches import _g1_source_digest
        if _g1_source_digest(self.store.pack.parent) != gate["source_tree_digest"]:
            raise FactoryError("frozen-review host source changed after source authorization", "evidence_source_gate", 409)

    def _original(self):
        from .agent_inputs import build_agent_input
        from .artifacts import tree_manifest
        from .cognition import REVIEW_PROMPT, frozen_review_payload, verify_frozen
        from .api import controlled_path
        job = self.store.job(JOB_ID)
        snapshot = job["snapshot"]
        if (job["state"] != "needs_review" or job["attempt"] != 1 or job["batch_id"] != BATCH_ID
                or digest(snapshot) != SNAPSHOT_DIGEST or snapshot.get("artifact_id") != ARTIFACT_ID
                or snapshot.get("artifact_digest") != ARTIFACT_DIGEST):
            raise FactoryError("frozen review job no longer matches its original snapshot", "frozen_recovery_baseline", 409)
        bundle = controlled_path(self.store, snapshot["bundle_path"])
        artifact = next((item for item in self.store.artifacts() if item["id"] == ARTIFACT_ID), None)
        if not artifact or artifact.get("id") != ARTIFACT_ID or artifact.get("digest") != ARTIFACT_DIGEST:
            raise FactoryError("frozen artifact record changed", "frozen_recovery_baseline", 409)
        archive_ref = artifact.get("archive_path")
        if not isinstance(archive_ref, str):
            raise FactoryError("frozen artifact archive reference is missing", "frozen_recovery_baseline", 409)
        archive_path = controlled_path(self.store, archive_ref)
        if _sha(archive_path.read_bytes()) != "20d602d7a4eba259a88126366780b571aefae6821b32c123f2d1d9614cc83bee":
            raise FactoryError("frozen artifact archive bytes changed", "frozen_recovery_baseline", 409)
        verify_frozen(bundle, ARTIFACT_DIGEST)
        source = bundle / "source"
        attempt = self.store.root / "jobs" / JOB_ID / "attempt-1" / "cognitive-review"
        source_copy = attempt / "source"
        raw = (attempt / "input.json").read_bytes()
        leaf_raw = (attempt / "leaf.md").read_bytes()
        payload = frozen_review_payload(snapshot, source)
        effective, expected_raw, expected_leaf = build_agent_input(payload)
        if (_sha(raw) != OLD_RAW_SHA or raw != expected_raw or digest(json.loads(raw)) != OLD_PAYLOAD_DIGEST
                or digest({k: v for k, v in json.loads(raw).items() if k != "language"}) != OLD_BUDGET_DIGEST
                or _sha(REVIEW_PROMPT.encode()) != OLD_PROMPT_SHA
                or leaf_raw != expected_leaf):
            raise FactoryError("original frozen review input or prompt changed", "frozen_recovery_baseline", 409)
        if (digest(tree_manifest(source)) != "c56d550a62c929f0429006c6252058f0e588067f2107a1afb0b2d8026dc4c636"
                or tree_manifest(source_copy) != tree_manifest(source)):
            raise FactoryError("frozen source tree differs from the archived artifact", "frozen_recovery_baseline", 409)
        from .cases import CaseLibrary
        library = CaseLibrary(self.store, initialize=False)
        basis = snapshot.get("case_basis")
        library.require_admissible(basis)
        template = json.loads((source / "template.json").read_bytes())
        if template.get("case_basis") != basis:
            raise FactoryError("frozen source case basis differs from job snapshot", "frozen_recovery_baseline", 409)
        library.validate_facts_view(template.get("case_facts_view"), basis)
        library.require_design_evidence(basis, template.get("case_design", []))
        summary_raw = (attempt / "cli-summary.json").read_bytes()
        if _sha(summary_raw) != OLD_SUMMARY_SHA:
            raise FactoryError("original frozen review CLI summary changed", "frozen_recovery_baseline", 409)
        return job, snapshot, bundle, source, attempt, raw, leaf_raw, effective, REVIEW_PROMPT, tree_manifest(source)

    def _verify_baseline_locked(self, con):
        sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN_ID,)).fetchone()[0]
        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN_ID,)).fetchone()[0]
        repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()[0]
        amendment = con.execute("SELECT id,new_deadline,activated_at FROM tf_budget_amendment WHERE campaign_id=? AND product_id=? ORDER BY version DESC LIMIT 1", (CAMPAIGN_ID, PRODUCT_ID)).fetchone()
        old = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id='pgrant_f3595368c14d4b23b6ab536f6d198007'").fetchone()
        prior = con.execute("SELECT status,consumed_reservation_id FROM tf_evidence_recovery_grant WHERE id='egrant_dd03245306034022bbc046e3b9428955'").fetchone()
        batch = con.execute("SELECT state FROM batch WHERE id=?", (BATCH_ID,)).fetchone()
        parent_batch = con.execute("SELECT state FROM batch WHERE id='bat_d13dc5920a574140be85da0ea6f5395b'").fetchone()
        retry_rows = con.execute("SELECT retry_scope,stage,retry FROM tf_budget_reservation WHERE campaign_id=? AND identity=? AND status!='not_started'", (CAMPAIGN_ID, PRODUCT_ID)).fetchall()
        from .budget import _legacy_retry_scope
        prior_scope_retries = sum(1 for r in retry_rows if (r[0] or _legacy_retry_scope(r[1])) == "cognitive-review" and r[2] is not None)
        old_use = con.execute("SELECT status FROM tf_evidence_recovery_grant_use WHERE grant_id='egrant_dd03245306034022bbc046e3b9428955'").fetchall()
        if (sessions != 80 or active != 0 or repairs != 7 or not amendment
                or amendment["id"] != "bamd_f2054b5d9a9b4e80b6a4e379ed04a42a"
                or amendment["activated_at"] is None or float(amendment["new_deadline"]) != DEADLINE
                or float(self.clock()) >= DEADLINE or not old or old["status"] != "consumed"
                or old["consumed_reservation_id"] != "bud_9a81a7a4adc14f49b46239ec68ee2fdb"
                or not prior or prior["status"] != "consumed"
                or len(old_use) != 1 or old_use[0]["status"] != "consumed"
                or not batch or batch["state"] != "paused" or not parent_batch or parent_batch["state"] != "paused"
                or prior_scope_retries != 2):
            raise FactoryError("frozen review budget, old grants or absolute deadline changed", "frozen_recovery_baseline", 409)

    def prepare(self, job_id, request):
        from .cognition import DIMENSIONS
        from .frozen_review_materials import append_review_prompt, extend_readonly_config
        if job_id != JOB_ID or not isinstance(request, dict) or set(request) != {"schema", "request_key", "source_authorization", "source_gate"}:
            raise FactoryError("invalid frozen-review prepare scope", "frozen_recovery_schema", 400)
        if request.get("schema") != "atlas.frozen-review-prepare.v1" or request.get("request_key") != REQUEST_KEY:
            raise FactoryError("unsupported frozen-review prepare request", "frozen_recovery_schema", 400)
        if request.get("source_authorization") != {"source_ref": AUTH_REF, "source_digest": AUTH_SHA256}:
            raise FactoryError("frozen-review source authorization differs", "frozen_recovery_authorization", 403)
        try:
            if _sha((self.store.pack.parent / AUTH_REF).read_bytes()) != AUTH_SHA256:
                raise ValueError("authorization bytes changed")
        except OSError as exc:
            raise FactoryError("frozen-review authorization is unavailable", "frozen_recovery_authorization", 409) from exc
        from .evidence_recovery import validate_source_gate
        gate = (self.source_gate_validator(self.store, request["source_gate"])
                if self.source_gate_validator else validate_source_gate(self.store, request["source_gate"]))
        job, snapshot, bundle, source, old_dir, raw, leaf_raw, payload, original_prompt, source_manifest = self._original()
        source_copy = old_dir / "source"
        materials = self._materials(raw, leaf_raw, source_copy)
        prompt, prompt_identity = append_review_prompt(original_prompt)
        call_payload = json.loads(raw)
        input_raw = raw
        input_hash = _sha(input_raw)
        from .pipeline import _budget_operation_identity
        operation, _ = _budget_operation_identity("cognitive-review", call_payload)
        if operation != "cognitive-review:572da86649b4face":
            raise FactoryError("frozen-review operation identity changed", "frozen_recovery_baseline", 409)
        target_attempt = self.store.root / "jobs" / JOB_ID / "attempt-2" / "cognitive-review"
        old_config = json.loads((old_dir / "opencode.json").read_bytes())
        derived_config, config_identity = extend_readonly_config(old_config, old_dir, target_attempt, materials["manifest"])
        call = {"payload": call_payload, "input_json": raw.decode("utf-8"), "prompt": prompt, "input_sha256": input_hash,
                "full_payload_digest": digest(call_payload),
                "budget_input_digest": digest({k: v for k, v in call_payload.items() if k != "language"}),
                "prompt_sha256": _sha(prompt.encode()), "source_tree_digest": digest(source_manifest),
                "projection_digest": digest(source_manifest), "stage_name": "cognitive-review",
                "operation": operation, "logical_retry_scope": "cognitive-review",
                "requested_model": snapshot["config"]["model"], "cli_config_identity": config_identity,
                "materials_manifest_digest": materials["manifest_digest"], "materials_tree_digest": materials["tree_digest"],
                "leaf_sha256": _sha(leaf_raw), "timeout_seconds": 1800,
                "prompt_append_identity": prompt_identity, "materials_scan": materials["scan"],
                "source_manifest": source_manifest, "cli_config": derived_config}
        with self.store.connect() as con:
            self._verify_baseline_locked(con)
            acceptance = con.execute("SELECT body FROM acceptance WHERE id=?", (OLD_ACCEPTANCE_ID,)).fetchone()
            if not acceptance or json.loads(acceptance["body"]).get("outcome") != "unavailable":
                raise FactoryError("original unavailable acceptance changed", "frozen_recovery_baseline", 409)
            reservation = con.execute("SELECT * FROM tf_budget_reservation WHERE id=?", (ORIGINAL_RESERVATION,)).fetchone()
            if not reservation or reservation["job_id"] != JOB_ID or reservation["status"] != "failed":
                raise FactoryError("original failed reservation changed", "frozen_recovery_baseline", 409)
            events = [dict(row) for row in con.execute("SELECT seq,attempt,at,stage,message FROM event WHERE job_id=? ORDER BY seq", (JOB_ID,))]
            checkpoints = [dict(row) for row in con.execute("SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (JOB_ID,))]
        binding = {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                   "job_id": JOB_ID, "batch_id": BATCH_ID, "attempt": 1, "snapshot_digest": SNAPSHOT_DIGEST,
                   "deadline": DEADLINE, "artifact_id": ARTIFACT_ID, "artifact_digest": ARTIFACT_DIGEST,
                   "old_acceptance_id": OLD_ACCEPTANCE_ID, "old_acceptance_digest": _sha(acceptance["body"].encode()),
                   "original_reservation_id": ORIGINAL_RESERVATION, "original_events_digest": digest(events),
                   "original_checkpoints_digest": digest(checkpoints), "source_manifest_digest": digest(source_manifest)}
        proposal = {"schema": SCHEMA, "request_key": REQUEST_KEY, "source_authorization": request["source_authorization"],
                    "source_gate": gate, "source_gate_passed": True,
                    "materials": {"binding": binding, "old_phase": {"reservation_id": ORIGINAL_RESERVATION,
                    "input_sha256": OLD_RAW_SHA, "full_payload_digest": OLD_PAYLOAD_DIGEST,
                    "budget_input_digest": OLD_BUDGET_DIGEST, "prompt_sha256": OLD_PROMPT_SHA,
                    "summary_sha256": OLD_SUMMARY_SHA, "source_tree_digest": digest(source_manifest)},
                    "frozen_review_call": call, "review_dimensions": list(DIMENSIONS),
                    "material_files": {path: _sha(content) for path, content in materials["files"].items()}}}
        proposal["proposal_digest"] = digest(proposal)
        return proposal

    def register(self, prepared_proposal, request):
        from .evidence_grants import EvidenceGrantService
        request_key = request.get("request_key") if isinstance(request, dict) else None
        # Idempotent replay is resolved before checking the live deadline/source gate.
        try:
            with self.store.connect() as con:
                prior = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE campaign_id=? AND request_key=?",
                                    (CAMPAIGN_ID, request_key)).fetchone()
        except Exception as exc:
            if "no such table" not in str(exc):
                raise
            prior = None
        if prior:
            stored = json.loads(prior["request_json"])
            req_matches = (request == {"schema": "atlas.frozen-review-prepare.v1", "request_key": stored.get("request_key"),
                           "source_authorization": stored.get("source_authorization"), "source_gate": stored.get("source_gate")})
            if (not req_matches or stored != prepared_proposal
                    or prepared_proposal.get("proposal_digest") != digest({k: v for k, v in prepared_proposal.items() if k != "proposal_digest"})):
                raise FactoryError("frozen-review key is already bound to another proposal", "evidence_grant_conflict", 409)
            return EvidenceGrantService._record(prior)
        refreshed = self.prepare(JOB_ID, request)
        if refreshed != prepared_proposal:
            raise FactoryError("frozen-review materials changed after preparation", "checkpoint_changed", 409)
        return EvidenceGrantService(self.store, clock=self.clock, source_gate_validator=self.source_gate_validator).register(prepared_proposal, request)

    def recover(self, job_id, request):
        from .evidence_grants import EvidenceGrantService
        expected_keys = {"schema", "grant_id", "request_key", "proposal_digest"}
        if (job_id != JOB_ID or not isinstance(request, dict) or set(request) != expected_keys
                or request.get("schema") != "atlas.frozen-review-recovery.v1"):
            raise FactoryError("invalid frozen-review recovery request", "frozen_recovery_schema", 400)
        request_digest = digest(request)
        with self.store.connect(True) as con:
            EvidenceRecoveryService = __import__("template_factory.evidence_recovery", fromlist=["EvidenceRecoveryService"]).EvidenceRecoveryService
            EvidenceRecoveryService._initialize_locked(con)
            prior = con.execute("SELECT * FROM tf_evidence_recovery WHERE job_id=?", (job_id,)).fetchone()
            if prior:
                if prior["grant_id"] != request["grant_id"] or prior["request_key"] != request["request_key"] or prior["request_digest"] != request_digest:
                    raise FactoryError("frozen review was already recovered with another request", "idempotency_conflict", 409)
                return {"recovery_id": prior["recovery_id"], "grant_id": prior["grant_id"], "job_id": job_id,
                        "attempt": prior["old_attempt"] + 1, "replayed": True, "worker_started": False}
            job = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            if not job or job["state"] != "needs_review" or job["attempt"] != 1 or digest(json.loads(job["snapshot"])) != SNAPSHOT_DIGEST:
                raise FactoryError("frozen review is not the fixed needs-review attempt 1", "frozen_recovery_state", 409)
            self._verify_baseline_locked(con)
            grant_row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (request["grant_id"],)).fetchone()
            if not grant_row:
                raise FactoryError("frozen review grant not found", "evidence_grant_missing", 404)
            proposal = json.loads(grant_row["request_json"])
            if grant_row["job_id"] != JOB_ID or proposal["schema"] != SCHEMA or proposal["proposal_digest"] != request["proposal_digest"]:
                raise FactoryError("grant does not bind the frozen review", "evidence_grant_binding", 409)
            from .evidence_recovery import validate_source_gate
            gate = (self.source_gate_validator(self.store, proposal["source_gate"])
                    if self.source_gate_validator else validate_source_gate(self.store, proposal["source_gate"]))
            if gate != proposal["source_gate"]:
                raise FactoryError("frozen-review source gate changed", "evidence_source_gate", 409)
            EvidenceGrantService.validate_locked(con, request["grant_id"], proposal, request["request_key"], job_id)
            current = self.prepare(JOB_ID, {"schema": "atlas.frozen-review-prepare.v1", "request_key": REQUEST_KEY,
                      "source_authorization": proposal["source_authorization"], "source_gate": proposal["source_gate"]})
            if current != proposal:
                raise FactoryError("frozen-review evidence changed before recovery", "checkpoint_changed", 409)
            EvidenceGrantService.queue_locked(con, request["grant_id"], proposal, request["request_key"], job_id)
            checkpoints = [dict(x) for x in con.execute("SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (job_id,))]
            events = [dict(x) for x in con.execute("SELECT seq,attempt,at,stage,message FROM event WHERE job_id=? ORDER BY seq", (job_id,))]
            at = now()
            rid = "frec_" + uuid.uuid4().hex
            con.execute("INSERT INTO tf_evidence_recovery VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (rid, job_id, request["grant_id"], request["request_key"], request_digest,
                         proposal["proposal_digest"], job["state"], job["error"], job["stage"], 1,
                         SNAPSHOT_DIGEST, digest(checkpoints), canonical([x["name"] for x in checkpoints]), canonical(events), at))
            changed = con.execute("UPDATE job SET state='queued',attempt=2,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=? AND attempt=1 AND state='needs_review'", (at, job_id)).rowcount
            if changed != 1:
                raise FactoryError("frozen review changed during recovery", "frozen_recovery_race", 409)
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (job_id, 2, at, job["stage"], "Authorized same-job frozen review recovery queued; no provider started"))
            return {"recovery_id": rid, "grant_id": request["grant_id"], "job_id": job_id,
                    "attempt": 2, "replayed": False, "worker_started": False}

    def prepare_call(self, job, directory, prompt, payload, context):
        """Rebuild derived readable material and fail closed on any call drift."""
        from .agent_inputs import build_agent_input
        from .evidence_grants import get_call_binding
        proposal = context.get("proposal") if isinstance(context, dict) else None
        self._assert_live_source_gate(proposal)
        call = get_call_binding(proposal)
        target = Path(directory)
        raw = (target / "input.json").read_bytes()
        bound_payload = json.loads(call.get("input_json", "{}"))
        normalized, expected_raw, leaf = build_agent_input(bound_payload)
        if raw != expected_raw or normalized != payload or prompt != call.get("prompt") or payload != bound_payload:
            raise FactoryError("frozen review input or prompt differs from its registered call", "evidence_grant_binding", 409)
        source = target / "source"
        if not source.is_dir() or source.is_symlink():
            raise FactoryError("frozen review source tree is missing or unsafe", "evidence_grant_binding", 409)
        from .artifacts import tree_manifest
        if digest(tree_manifest(source)) != call.get("source_tree_digest"):
            raise FactoryError("frozen review source tree changed", "evidence_grant_binding", 409)
        leaf_path = target / "leaf.md"
        leaf_bytes = leaf if leaf is not None else (leaf_path.read_bytes() if leaf_path.is_file() else None)
        if leaf_bytes is None or not leaf_path.is_file() or _sha(leaf_bytes) != call.get("leaf_sha256"):
            raise FactoryError("frozen review leaf bytes differ from the registered call", "evidence_grant_binding", 409)
        materials = self._materials(raw, leaf_bytes, source)
        if (_sha(prompt.encode("utf-8")) != call.get("prompt_sha256")
                or _sha(raw) != call.get("input_sha256")
                or digest(payload) != call.get("full_payload_digest")
                or materials["manifest_digest"] != call.get("materials_manifest_digest")
                or materials["tree_digest"] != call.get("materials_tree_digest")):
            raise FactoryError("frozen review material or digest differs from the registered call", "evidence_grant_binding", 409)
        (target / "prompt.txt").write_bytes(prompt.encode("utf-8"))
        root = target / "review-materials"
        root.mkdir(exist_ok=False)
        for rel, content in materials["files"].items():
            out = root / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(content)
        (root / "manifest.json").write_bytes(json.dumps(materials["manifest"], ensure_ascii=False, indent=2).encode("utf-8") + b"\n")
        return call

    def active_for_job(self, job_id):
        if job_id != JOB_ID:
            return None
        with self.store.connect() as con:
            try:
                row = con.execute("SELECT r.*,g.request_json,g.status grant_status,g.call_attempt,g.consumed_reservation_id FROM tf_evidence_recovery r JOIN tf_evidence_recovery_grant g ON g.id=r.grant_id WHERE r.job_id=? AND json_extract(g.request_json,'$.schema')=?", (job_id, SCHEMA)).fetchone()
            except Exception as exc:
                if "no such table" in str(exc):
                    return None
                raise
        if not row:
            return None
        result = {"grant_id": row["grant_id"], "recovery_id": row["recovery_id"],
                "proposal": json.loads(row["request_json"]), "attempt": row["old_attempt"] + 1,
                "request_key": row["request_key"], "proposal_digest": row["proposal_digest"],
                "host_only": False, "cli_allowed": True, "call_attempt": row["call_attempt"],
                "reservation_id": row["consumed_reservation_id"]}
        with self.store.connect() as con:
            try:
                saved = con.execute("SELECT * FROM tf_evidence_saved_resume WHERE job_id=? ORDER BY next_attempt DESC LIMIT 1", (job_id,)).fetchone()
            except Exception as exc:
                if "no such table" not in str(exc):
                    raise
                saved = None
        current = self.store.job(job_id)
        if saved and current["attempt"] == saved["next_attempt"]:
            result.update({"attempt": saved["next_attempt"], "host_only": True, "cli_allowed": False,
                           "saved_resume_id": saved["id"], "saved_result_sha256": saved["result_sha256"],
                           "source_gate": json.loads(saved["source_gate_json"])})
        return result

    @staticmethod
    def get_call_binding(proposal):
        from .evidence_grants import get_call_binding
        return get_call_binding(proposal)

    def validate_saved_result(self, job, recovery):
        """Return only a fully delivered result for this grant's actual call attempt."""
        return self._validated_delivery(job, recovery)

    def resume_saved_result(self, job_id, request):
        required = {"schema", "grant_id", "request_key", "source_gate", "expected_result_sha256"}
        if (job_id != JOB_ID or not isinstance(request, dict) or set(request) != required
                or request.get("schema") != "atlas.frozen-review-saved-result-resume.v1"
                or not isinstance(request.get("request_key"), str) or not request["request_key"]):
            raise FactoryError("invalid frozen-review saved-result request", "frozen_recovery_schema", 400)
        request_digest = digest(request)
        with self.store.connect(True) as init:
            init.execute("""CREATE TABLE IF NOT EXISTS tf_evidence_saved_resume (
                id TEXT PRIMARY KEY,job_id TEXT NOT NULL,grant_id TEXT NOT NULL,request_key TEXT NOT NULL UNIQUE,
                request_digest TEXT NOT NULL,source_gate_json TEXT NOT NULL,result_sha256 TEXT NOT NULL,
                old_attempt INTEGER NOT NULL,next_attempt INTEGER NOT NULL,created_at TEXT NOT NULL)""")
        with self.store.connect() as read:
            prior = read.execute("SELECT * FROM tf_evidence_saved_resume WHERE request_key=?", (request["request_key"],)).fetchone()
            if prior:
                if prior["job_id"] != job_id or prior["request_digest"] != request_digest:
                    raise FactoryError("saved-result key is already bound to another request", "idempotency_conflict", 409)
                return {"id": prior["id"], "job_id": job_id, "grant_id": prior["grant_id"],
                        "attempt": prior["next_attempt"], "replayed": True, "worker_started": False,
                        "cli_allowed": False}
            before_job = read.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            before_recovery = read.execute("SELECT * FROM tf_evidence_recovery WHERE job_id=? AND grant_id=?", (job_id, request["grant_id"])).fetchone()
            before_grant = read.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (request["grant_id"],)).fetchone()
            latest_acceptance = read.execute("SELECT body FROM acceptance WHERE job_id=? ORDER BY created_at DESC,id DESC LIMIT 1", (job_id,)).fetchone()
        state_ok = before_job and before_job["state"] in {"failed", "interrupted", "needs_review"}
        if before_job and before_job["state"] == "needs_review":
            acceptance_body = json.loads(latest_acceptance["body"]) if latest_acceptance else {}
            state_ok = (acceptance_body.get("job_attempt") == before_job["attempt"]
                        and acceptance_body.get("outcome") == "unavailable")
        if (not state_ok or before_job["attempt"] < 2
                or not before_recovery or not before_grant or before_grant["status"] != "consumed"):
            raise FactoryError("frozen-review host-only continuation is not eligible", "evidence_saved_state", 409)
        gate = (self.source_gate_validator(self.store, request["source_gate"])
                if self.source_gate_validator else __import__("template_factory.evidence_recovery", fromlist=["validate_source_gate"]).validate_source_gate(self.store, request["source_gate"]))
        if gate != request["source_gate"]:
            raise FactoryError("saved-result source gate changed", "evidence_source_gate", 409)
        self._assert_live_source_gate({"source_gate": gate})
        self._validated_delivery(self.store.job(job_id), {"grant_id": before_grant["id"], "recovery_id": before_recovery["recovery_id"]})
        call = __import__("template_factory.evidence_grants", fromlist=["get_call_binding"]).get_call_binding(json.loads(before_grant["request_json"]))
        directory = self.store.root / "jobs" / JOB_ID / f"attempt-{before_grant['call_attempt']}" / call["stage_name"]
        result_hash = _sha((directory / "result.json").read_bytes())
        if result_hash != request["expected_result_sha256"]:
            raise FactoryError("saved frozen-review result bytes changed", "checkpoint_changed", 409)
        with self.store.connect(True) as con:
            con.execute("""CREATE TABLE IF NOT EXISTS tf_evidence_saved_resume (
                id TEXT PRIMARY KEY,job_id TEXT NOT NULL,grant_id TEXT NOT NULL,request_key TEXT NOT NULL UNIQUE,
                request_digest TEXT NOT NULL,source_gate_json TEXT NOT NULL,result_sha256 TEXT NOT NULL,
                old_attempt INTEGER NOT NULL,next_attempt INTEGER NOT NULL,created_at TEXT NOT NULL)""")
            prior = con.execute("SELECT * FROM tf_evidence_saved_resume WHERE request_key=?", (request["request_key"],)).fetchone()
            if prior:
                if prior["job_id"] != job_id or prior["request_digest"] != request_digest:
                    raise FactoryError("saved-result key is already bound to another request", "idempotency_conflict", 409)
                return {"id": prior["id"], "job_id": job_id, "grant_id": prior["grant_id"],
                        "attempt": prior["next_attempt"], "replayed": True, "worker_started": False,
                        "cli_allowed": False}
            job_row = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            recovery = con.execute("SELECT * FROM tf_evidence_recovery WHERE job_id=? AND grant_id=?", (job_id, request["grant_id"])).fetchone()
            grant_row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (request["grant_id"],)).fetchone()
            latest = con.execute("SELECT body FROM acceptance WHERE job_id=? ORDER BY created_at DESC,id DESC LIMIT 1", (job_id,)).fetchone()
            can_resume = job_row and job_row["state"] in {"failed", "interrupted"}
            if job_row and job_row["state"] == "needs_review":
                body = json.loads(latest["body"]) if latest else {}
                can_resume = body.get("job_attempt") == job_row["attempt"] and body.get("outcome") == "unavailable"
            if (not can_resume or job_row["attempt"] < 2
                    or not recovery or not grant_row or grant_row["status"] != "consumed"):
                raise FactoryError("frozen-review host-only continuation is not eligible", "evidence_saved_state", 409)
            if grant_row["call_attempt"] != before_grant["call_attempt"] or recovery["recovery_id"] != before_recovery["recovery_id"]:
                raise FactoryError("frozen-review saved result binding changed", "evidence_saved_state", 409)
            if result_hash != request["expected_result_sha256"]:
                raise FactoryError("saved frozen-review result bytes changed", "checkpoint_changed", 409)
            old_attempt = job_row["attempt"]
            next_attempt = old_attempt + 1
            rid = "fsave_" + uuid.uuid4().hex
            at = now()
            con.execute("INSERT INTO tf_evidence_saved_resume VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (rid, job_id, request["grant_id"], request["request_key"], request_digest,
                         canonical(gate), result_hash, old_attempt, next_attempt, at))
            changed = con.execute("UPDATE job SET state='queued',attempt=?,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=? AND attempt=? AND state IN ('failed','interrupted','needs_review')",
                                  (next_attempt, at, job_id, old_attempt)).rowcount
            if changed != 1:
                raise FactoryError("job changed during host-only continuation", "frozen_recovery_race", 409)
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (job_id, next_attempt, at, job_row["stage"], "Verified saved frozen-review result queued for host-only acceptance; no CLI authorized"))
            return {"id": rid, "job_id": job_id, "grant_id": request["grant_id"], "attempt": next_attempt,
                    "replayed": False, "worker_started": False, "cli_allowed": False}

    def _validated_delivery(self, job, recovery):
        from .evidence_grants import EvidenceGrantService, get_call_binding
        grant = EvidenceGrantService(self.store).get(recovery["grant_id"])
        call = get_call_binding(grant["proposal"])
        attempt = grant.get("call_attempt")
        if not isinstance(attempt, int) or attempt < 2:
            raise FactoryError("frozen review has no proved model call attempt", "evidence_result_unproved", 409)
        directory = self.store.root / "jobs" / JOB_ID / f"attempt-{attempt}" / call["stage_name"]
        try:
            raw_input = (directory / "input.json").read_bytes()
            prompt_raw = (directory / "prompt.txt").read_bytes()
            summary = json.loads((directory / "cli-summary.json").read_bytes())
            result_bytes = (directory / "result.json").read_bytes()
            result = json.loads(result_bytes)
            original_raw = (directory / "original-response.json").read_bytes()
            original_result = _parse_original_response(directory, original_raw)
            from .artifacts import tree_manifest
            from .frozen_review_materials import registered_read_resources, validate_readonly_config
            registered = registered_read_resources(directory,
                expected_manifest_digest=call["materials_manifest_digest"],
                expected_tree_digest=call["materials_tree_digest"])
            config = json.loads((directory / "opencode.json").read_bytes())
            validate_readonly_config(config, directory, registered["manifest"], call["cli_config_identity"])
            if (_sha(raw_input) != call["input_sha256"] or _sha(prompt_raw) != call["prompt_sha256"]
                    or digest(tree_manifest(directory / "source")) != call["source_tree_digest"]
                    or _sha(result_bytes) != summary.get("result_sha256")
                    or _sha(original_raw) != summary.get("original_response_sha256")
                    or original_result != result
                    or summary.get("delivery_status") != "delivered" or summary.get("failure_code")
                    or summary.get("reservation_id") != grant.get("consumed_reservation_id")
                    or summary.get("requested_model") != call["requested_model"]):
                raise ValueError("delivered output binding differs")
        except (OSError, ValueError, TypeError) as exc:
            raise FactoryError("frozen review result is not a verified delivered call", "evidence_result_unproved", 409) from exc
        with self.store.connect() as con:
            reservation = con.execute("SELECT status,job_id,stage FROM tf_budget_reservation WHERE id=?", (grant.get("consumed_reservation_id"),)).fetchone()
        if not reservation or reservation["status"] != "completed" or reservation["job_id"] != JOB_ID or reservation["stage"] != call["operation"]:
            raise FactoryError("frozen review reservation did not complete", "evidence_result_unproved", 409)
        from .cognition import validate_review
        validate_review(result, directory / "source")
        return result

    def acceptance_binding(self, job, recovery, result):
        from .evidence_grants import EvidenceGrantService, get_call_binding
        grant = EvidenceGrantService(self.store).get(recovery["grant_id"])
        call = get_call_binding(grant["proposal"])
        if result.get("outcome") != "unavailable":
            delivered = self._validated_delivery(job, recovery)
            if result != delivered:
                raise FactoryError("review result differs from delivered model response", "evidence_result_unproved", 409)
        return {"schema": SCHEMA, "job_id": JOB_ID, "attempt": job.get("attempt"),
                "recovery_id": recovery["recovery_id"], "grant_id": grant["id"],
                "reservation_id": grant.get("consumed_reservation_id"),
                "call_attempt": grant.get("call_attempt"), "artifact_id": ARTIFACT_ID,
                "artifact_digest": ARTIFACT_DIGEST, "input_sha256": call["input_sha256"],
                "prompt_sha256": call["prompt_sha256"], "source_tree_digest": call["source_tree_digest"],
                "materials_manifest_digest": call["materials_manifest_digest"],
                "materials_tree_digest": call["materials_tree_digest"], "timeout_seconds": 1800,
                "result_digest": digest(result)}

    def validate_acceptance_locked(self, con, row, result):
        report = result.get("frozen_review_recovery") if isinstance(result, dict) else None
        if row["id"] != JOB_ID:
            return
        if isinstance(result, dict) and result.get("outcome") == "unavailable":
            # Preserve factual failures (including timeout, invalid references,
            # and pre-spawn errors). The caller already holds the current job
            # token/lease; an unavailable result cannot claim a successful call.
            if report is not None and (not isinstance(report, dict) or report.get("schema") != SCHEMA
                                       or report.get("job_id") != JOB_ID):
                raise FactoryError("unavailable frozen-review lineage is malformed", "evidence_acceptance_binding", 409)
            return
        if not isinstance(report, dict) or report.get("schema") != SCHEMA or report.get("job_id") != JOB_ID:
            raise FactoryError("frozen review acceptance lacks its recovery binding", "evidence_acceptance_binding", 409)
        if (report.get("attempt") != row["attempt"] or report.get("artifact_id") != ARTIFACT_ID
                or report.get("artifact_digest") != ARTIFACT_DIGEST):
            raise FactoryError("frozen review acceptance is attached to another attempt or artifact", "evidence_acceptance_binding", 409)
        recovery = con.execute("SELECT * FROM tf_evidence_recovery WHERE recovery_id=? AND job_id=? AND grant_id=?",
                               (report.get("recovery_id"), JOB_ID, report.get("grant_id"))).fetchone()
        if not recovery or recovery["old_attempt"] != 1 or recovery["snapshot_digest"] != SNAPSHOT_DIGEST:
            raise FactoryError("frozen review recovery receipt differs", "evidence_acceptance_binding", 409)
        grant_row = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (report.get("grant_id"),)).fetchone()
        if not grant_row or grant_row["status"] != "consumed" or grant_row["consumed_reservation_id"] != report.get("reservation_id") or grant_row["call_attempt"] != report.get("call_attempt"):
            raise FactoryError("frozen review acceptance is not bound to its completed grant", "evidence_acceptance_binding", 409)
        proposal = json.loads(grant_row["request_json"])
        from .evidence_grants import get_call_binding
        call = get_call_binding(proposal)
        if any(report.get(field) != call.get(field) for field in ("input_sha256", "prompt_sha256", "source_tree_digest", "materials_manifest_digest", "materials_tree_digest")):
            raise FactoryError("frozen review acceptance call identity changed", "evidence_acceptance_binding", 409)
        reservation = con.execute("SELECT status,job_id,stage FROM tf_budget_reservation WHERE id=?", (grant_row["consumed_reservation_id"],)).fetchone()
        if not reservation or reservation["status"] != "completed" or reservation["job_id"] != JOB_ID or reservation["stage"] != call["operation"]:
            raise FactoryError("frozen review reservation is not a completed delivery", "evidence_acceptance_binding", 409)
        directory = self.store.root / "jobs" / JOB_ID / f"attempt-{grant_row['call_attempt']}" / call["stage_name"]
        try:
            raw_result = (directory / "result.json").read_bytes()
            summary = json.loads((directory / "cli-summary.json").read_bytes())
            raw_input = (directory / "input.json").read_bytes()
            raw_prompt = (directory / "prompt.txt").read_bytes()
            from .artifacts import tree_manifest
            from .frozen_review_materials import registered_read_resources, validate_readonly_config
            registered = registered_read_resources(directory, expected_manifest_digest=call["materials_manifest_digest"],
                                                   expected_tree_digest=call["materials_tree_digest"])
            config = json.loads((directory / "opencode.json").read_bytes())
            validate_readonly_config(config, directory, registered["manifest"], call["cli_config_identity"])
            original_raw = (directory / "original-response.json").read_bytes()
            original_result = _parse_original_response(directory, original_raw)
            delivered_result = json.loads(raw_result)
            if (_sha(raw_result) != summary.get("result_sha256")
                    or digest(json.loads(raw_result)) != report.get("result_digest")
                    or _sha(original_raw) != summary.get("original_response_sha256") or original_result != delivered_result
                    or summary.get("reservation_id") != grant_row["consumed_reservation_id"]
                    or summary.get("delivery_status") != "delivered" or summary.get("failure_code")
                    or _sha(raw_input) != call["input_sha256"] or _sha(raw_prompt) != call["prompt_sha256"]
                    or digest(tree_manifest(directory / "source")) != call["source_tree_digest"]):
                raise ValueError("delivered call identity differs")
        except (OSError, ValueError, TypeError) as exc:
            raise FactoryError("frozen review acceptance lacks verified delivered output", "evidence_result_unproved", 409) from exc
        from .cognition import validate_review
        checked = validate_review(delivered_result, directory / "source")
        for field in ("outcome", "checks", "summary", "suggestions", "scope"):
            if result.get(field) != checked.get(field):
                raise FactoryError("submitted acceptance differs from delivered review content", "evidence_acceptance_binding", 409)
        if result.get("citation_aliases", []) != checked.get("citation_aliases", []):
            raise FactoryError("submitted citation aliases differ from delivered review content", "evidence_acceptance_binding", 409)
