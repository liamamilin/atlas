"""Focused temporary-store tests for the single R7 evidence-review allowance."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import (
    BudgetLedger, G1_AMENDMENT_CAMPAIGN, G1_R6_PROTOCOL_GRANT_ID,
    G1_R6_PROTOCOL_RESERVATION_ID,
)
from template_factory.evidence_grants import (
    AUTHORIZATION_SOURCE_DIGEST, AUTHORIZATION_SOURCE_REF, CAMPAIGN_ID,
    JOB_ID, OLD_DEADLINE, PLAN_ID, PRODUCT_ID, R7_BATCH_ID, R7_PARENT_BATCH_ID, RETRY_SCOPE,
    SNAPSHOT_DIGEST, STAGE_NAME, EvidenceGrantService,
)
from template_factory.store import FactoryError, FactoryStore, digest

REPO = Path(__file__).resolve().parents[2]


class EvidenceGrantTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.pack = self.root / "application-atlas-production-pack"
        self.pack.mkdir()
        auth_path = self.root / AUTHORIZATION_SOURCE_REF
        auth_path.parent.mkdir(parents=True)
        shutil.copyfile(REPO / AUTHORIZATION_SOURCE_REF, auth_path)
        self.now = [OLD_DEADLINE - 120]
        self.store = FactoryStore(self.root / "state", self.pack)
        self.service = EvidenceGrantService(self.store, clock=lambda: self.now[0])
        self.ledger = BudgetLedger(self.store, campaign_id=CAMPAIGN_ID, clock=lambda: self.now[0])
        self.proposal = self.make_proposal()
        self.request = {"request_key": self.proposal["request_key"]}
        self._seed_job_and_deadline()

    def tearDown(self):
        self.tmp.cleanup()

    def make_proposal(self):
        payload = {"proposal": "fixed evidence review", "projection_digest": "tree", "language": "zh"}
        prompt = "review exact supplemental evidence"
        budget_digest = digest({k: v for k, v in payload.items() if k != "language"})
        phase = {
            "stage_name": STAGE_NAME, "payload": payload,
            "input_sha256": "a" * 64, "full_payload_digest": digest(payload),
            "budget_input_digest": budget_digest, "prompt": prompt,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "source_tree_digest": "tree", "projection_digest": "tree",
            "operation": STAGE_NAME + ":" + budget_digest[:16],
            "logical_retry_scope": RETRY_SCOPE,
            "requested_model": "opencode-go/deepseek-v4.1-flash",
            "cli_config_identity": {"schema": "test"},
        }
        materials = {
            "binding": {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                        "job_id": JOB_ID, "batch_id": R7_BATCH_ID, "attempt": 1,
                        "snapshot_digest": SNAPSHOT_DIGEST, "deadline": OLD_DEADLINE},
            "new_phase": phase,
            "old_phase": {"checkpoint_name": "blueprint-design-check-0-phase_acceptance",
                          "checkpoint_digest": "dd19d90217dc6cadd7e8346ac4d2af2b1b5a73f4fee2f28aa3ea2f8190ad6d8f",
                          "projection_digest": "39d09af2c64eae5f81b4f83505383eb05902cf1f794e2612786a04892b7b6b4b",
                          "input_sha256": "ef0e7f1ab2963050b046060ac088d43513c871a60b33f1329279a4061a7a3b56",
                          "full_payload_digest": "559c03f2846706675146695d5c30cd4670a51b2039b113e57756dbe9dd9cf6a5",
                          "budget_input_digest": "7742082f7e399a3be58bcebbb66123d4447b7c2cd0f658b83b82ee72977f2a20",
                          "reservation_id": "bud_fbec046b65054a33a1c132ad8ed2fd32"},
            "old_aggregate": {"checkpoint_name": "blueprint-spec-review-0-runtime-v1", "checkpoint_digest": "f" * 64},
            "reuse_checks": {name: {"identical": True} for name in
                             ("architecture_contract", "decisions_defaults", "product_completeness", "runtime_protocol", "scenario_scope")},
        }
        proposal = {"schema": "atlas.evidence-recovery-proposal.v1", "request_key": "r7-evidence-once",
                    "source_authorization": {"source_ref": AUTHORIZATION_SOURCE_REF,
                                             "source_digest": AUTHORIZATION_SOURCE_DIGEST},
                    "source_gate": {"source_commit": "c" * 40, "source_tree_digest": "tree",
                                    "ci_evidence": [{"path": "ci.json", "sha256": "a" * 64,
                                                     "run_id": 1, "head_sha": "c" * 40,
                                                     "required_checks": ["check", "docker-integration"]}]},
                    "source_gate_passed": True, "materials": materials}
        proposal["proposal_digest"] = digest(proposal)
        return proposal

    def _seed_job_and_deadline(self):
        snapshot = {"v1": {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID,
                            "product_id": PRODUCT_ID}, "test_snapshot": "R7"}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (CAMPAIGN_ID, "__campaign_segment__", "G1", self.now[0] - 100, OLD_DEADLINE))
            con.execute("INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        ("bamd_f2054b5d9a9b4e80b6a4e379ed04a42a", CAMPAIGN_ID, PRODUCT_ID, PLAN_ID,
                         "fixture", "a" * 64, "R7 v4", "fixed", "r7-v4", 4, 6, 7, 6, 77,
                         OLD_DEADLINE, 0, 1.0, 1.0, OLD_DEADLINE))
            con.execute("INSERT INTO batch(id,state,config,created_at) VALUES(?,?,?,?)",
                        (R7_BATCH_ID, "paused", "{}", "now"))
            con.execute("INSERT INTO batch(id,state,config,created_at) VALUES(?,?,?,?)",
                        (R7_PARENT_BATCH_ID, "paused", "{}", "now"))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (JOB_ID, R7_BATCH_ID, "blueprint-production", "running", STAGE_NAME, 2,
                         "token-1", self.now[0] + 1000, json.dumps(snapshot), None, "now", "now"))
            for index in range(77):
                reservation_id = G1_R6_PROTOCOL_RESERVATION_ID if index == 0 else f"prior-{index}"
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,stage,retry,group_kind,retry_scope,outcome) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                            (reservation_id, CAMPAIGN_ID, PRODUCT_ID, "G1", "review", "completed", index + 1,
                             "blueprint-spec-review-prior" if index < 3 else None,
                             index + 1 if index < 3 else None, "production",
                             RETRY_SCOPE if index < 3 else None, "completed"))
            for index in range(7):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (CAMPAIGN_ID, PRODUCT_ID, f"repair-{index}", index + 1))
            grant_request = {"schema": "atlas.protocol-retry-grant.v1"}
            con.execute("INSERT INTO tf_protocol_retry_grant VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (G1_R6_PROTOCOL_GRANT_ID, CAMPAIGN_ID, PLAN_ID, PRODUCT_ID,
                         "job_7742b1c124be4c9ab3a0096da5cdd772", "ref", "a" * 64,
                         json.dumps(grant_request), digest(grant_request), "old-r6-key", "consumed",
                         G1_R6_PROTOCOL_RESERVATION_ID, 1))
            con.execute("INSERT INTO tf_protocol_retry_grant_use VALUES(?,?,?,?,?)",
                        (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID, "consumed", 1, None))
        self.job_snapshot = snapshot

    def register(self):
        with patch.object(self.store, "job", return_value={"state": "failed", "attempt": 1,
                                                            "batch_id": R7_BATCH_ID,
                                                            "snapshot": {"digest_stub": SNAPSHOT_DIGEST}}):
            # The fixture deliberately stubs the fixed production snapshot digest;
            # the proposal itself is still fully checked and hashed.
            with patch("template_factory.evidence_grants.digest", side_effect=lambda value: SNAPSHOT_DIGEST if value == {"digest_stub": SNAPSHOT_DIGEST} else digest(value)):
                with patch.object(self.service, "_verify_source_gate"):
                    return self.service.register(self.proposal, self.request)

    def queue(self, grant):
        with self.store.connect(True) as con:
            EvidenceGrantService.queue_locked(con, grant["id"], self.proposal,
                                              self.proposal["request_key"], JOB_ID)

    def context(self):
        return {
            "input_digest": self.proposal["materials"]["new_phase"]["budget_input_digest"],
            "input_sha256": self.proposal["materials"]["new_phase"]["input_sha256"],
            "full_payload_digest": self.proposal["materials"]["new_phase"]["full_payload_digest"],
            "budget_input_digest": self.proposal["materials"]["new_phase"]["budget_input_digest"],
            "prompt_sha256": self.proposal["materials"]["new_phase"]["prompt_sha256"],
            "source_tree_digest": "tree", "projection_digest": "tree",
            "stage_name": STAGE_NAME, "logical_retry_scope": RETRY_SCOPE,
            "operation": self.proposal["materials"]["new_phase"]["operation"],
        }

    def reserve(self, grant):
        return self.ledger.reserve(PRODUCT_ID, "G1", "review", 90, job_id=JOB_ID,
                                   job_token="token-1", requested_model="opencode-go/deepseek-v4.1-flash",
                                   stage=self.proposal["materials"]["new_phase"]["operation"], retry=1,
                                   retry_scope=RETRY_SCOPE, plan_id=PLAN_ID,
                                   protocol_context=self.context(), evidence_recovery_id=grant["id"])

    def test_idempotence_conflict_and_single_grant_per_job(self):
        first = self.register()
        self.assertEqual(first["status"], "registered")
        self.assertEqual(self.register()["id"], first["id"])
        other = dict(self.proposal, request_key="another-key")
        other["proposal_digest"] = digest({k: v for k, v in other.items() if k != "proposal_digest"})
        with patch.object(self.store, "job", return_value={"state": "failed", "attempt": 1,
                                                            "batch_id": R7_BATCH_ID, "snapshot": {"digest_stub": SNAPSHOT_DIGEST}}):
            with patch("template_factory.evidence_grants.digest", side_effect=lambda value: SNAPSHOT_DIGEST if value == {"digest_stub": SNAPSHOT_DIGEST} else digest(value)):
                with patch.object(self.service, "_verify_source_gate"):
                    with self.assertRaises(FactoryError):
                        self.service.register(other, {"request_key": "another-key"})
        self.assertEqual(self.service.get(first["id"])["proposal"], self.proposal)

    def test_exact_registration_replay_survives_recovery_and_expiry(self):
        first = self.register()
        # The dynamic baseline deliberately no longer passes after recovery;
        # exact idempotent replay must still return the original receipt.
        self.now[0] = OLD_DEADLINE + 1
        with patch.object(self.store, "job", return_value={"state": "running", "attempt": 2,
                                                            "batch_id": R7_BATCH_ID,
                                                            "snapshot": {"changed": True}}):
            replay = self.service.register(self.proposal, self.request)
        self.assertEqual(replay["id"], first["id"])
        changed = json.loads(json.dumps(self.proposal))
        changed["materials"]["new_phase"]["payload"]["proposal"] = "altered"
        changed["proposal_digest"] = digest({k: v for k, v in changed.items() if k != "proposal_digest"})
        with self.assertRaises(FactoryError) as caught:
            self.service.register(changed, self.request)
        self.assertEqual(caught.exception.code, "evidence_grant_conflict")

    def test_reservation_is_atomic_and_mismatch_does_not_consume(self):
        grant = self.register()
        self.queue(grant)
        bad = self.context()
        bad["prompt_sha256"] = "0" * 64
        with self.assertRaises(FactoryError):
            self.ledger.reserve(PRODUCT_ID, "G1", "review", 90, job_id=JOB_ID, job_token="token-1",
                                requested_model="opencode-go/deepseek-v4.1-flash",
                                stage=self.proposal["materials"]["new_phase"]["operation"], retry=1,
                                retry_scope=RETRY_SCOPE, plan_id=PLAN_ID,
                                protocol_context=bad, evidence_recovery_id=grant["id"])
        self.assertEqual(self.service.get(grant["id"])["status"], "queued")
        reservation = self.reserve(grant)
        with self.assertRaises(FactoryError):
            self.reserve(grant)
        with self.store.connect() as con:
            use = con.execute("SELECT status FROM tf_evidence_recovery_grant_use WHERE reservation_id=?", (reservation["id"],)).fetchone()
            self.assertEqual(use[0], "reserved")

    def test_binding_mismatch_lower_limit_and_transaction_fault_do_not_spend_grant(self):
        grant = self.register()
        self.queue(grant)
        base = {"identity": PRODUCT_ID, "phase": "G1", "kind": "review", "timeout": 90,
                "job_id": JOB_ID, "job_token": "token-1",
                "requested_model": "opencode-go/deepseek-v4.1-flash",
                "stage": self.proposal["materials"]["new_phase"]["operation"], "retry": 1,
                "retry_scope": RETRY_SCOPE, "plan_id": PLAN_ID,
                "protocol_context": self.context(), "evidence_recovery_id": grant["id"]}
        for change in ({"identity": "other-product"}, {"job_id": "other-job"},
                       {"requested_model": "other/model"}, {"stage": "other-operation"},
                       {"plan_id": "other-plan"}, {"retry_scope": "other-scope"}, {"retry": 2}):
            with self.subTest(change=change), self.assertRaises(FactoryError):
                self.ledger.reserve(**{**base, **change})
            self.assertEqual(self.service.get(grant["id"])["status"], "queued")
        from template_factory.evidence_grants import EvidenceGrantService as GrantService
        original = GrantService.occupy_locked
        def fail_after_link(*args, **kwargs):
            original(*args, **kwargs)
            raise RuntimeError("injected fault after grant link")
        with self.store.connect() as con:
            before = con.execute("SELECT COUNT(*) FROM tf_budget_reservation").fetchone()[0]
        with patch.object(GrantService, "occupy_locked", side_effect=fail_after_link):
            with self.assertRaises(RuntimeError):
                self.ledger.reserve(**base)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_reservation").fetchone()[0], before)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_evidence_recovery_grant_use WHERE grant_id=?", (grant["id"],)).fetchone()[0], 0)
        self.assertEqual(self.service.get(grant["id"])["status"], "queued")
        strict = BudgetLedger(self.store, campaign_id=CAMPAIGN_ID,
                              limits={"transient_retries": 1}, clock=lambda: self.now[0])
        with self.assertRaises(FactoryError):
            strict.reserve(**base)
        self.assertEqual(self.service.get(grant["id"])["status"], "queued")

    def test_only_proven_pre_spawn_release_reopens_same_grant(self):
        grant = self.register()
        self.queue(grant)
        reservation = self.reserve(grant)
        workspace = self.root / "cli"
        workspace.mkdir()
        (workspace / "opencode.json").write_text("{}", encoding="utf-8")
        with patch("template_factory.evidence_views.readonly_cli_config_identity",
                   return_value=self.proposal["materials"]["new_phase"]["cli_config_identity"]):
            self.ledger.mark_spawn_intent(reservation["id"], directory=workspace)
        self.ledger.release_not_started(reservation["id"])
        self.assertEqual(self.service.get(grant["id"])["status"], "queued")
        second = self.reserve(grant)
        self.ledger.mark_started(second["id"])
        self.ledger.finish(second["id"], "uncertain", outcome="host_lost")
        self.assertEqual(self.service.get(grant["id"])["status"], "uncertain")
        with self.assertRaises(FactoryError):
            self.reserve(grant)
        with self.store.connect() as con:
            rows = con.execute("SELECT status FROM tf_evidence_recovery_grant_use WHERE grant_id=? ORDER BY created_at,reservation_id", (grant["id"],)).fetchall()
            self.assertEqual(sorted(row[0] for row in rows), ["not_started", "uncertain"])

    def test_r7_phase_cannot_be_recast_as_retry_none_or_new_stage(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,job_id,stage,retry,group_kind) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                        ("original-phase", CAMPAIGN_ID, PRODUCT_ID, "G1", "review", "completed", 90,
                         JOB_ID, STAGE_NAME + ":original", None, "production"))
        for stage, scope in ((STAGE_NAME + ":changed-input", None),
                             (STAGE_NAME + "-renamed", "another-scope"),
                             ("renamed-review-stage", RETRY_SCOPE)):
            with self.subTest(stage=stage), self.assertRaises(FactoryError) as denied:
                self.ledger.reserve(PRODUCT_ID, "G1", "review", 90, job_id=JOB_ID,
                                    job_token="token-1", requested_model="opencode-go/deepseek-v4.1-flash",
                                    stage=stage, retry_scope=scope, plan_id=PLAN_ID)
            self.assertEqual(denied.exception.code, "budget_retry_limit")
        # Later, distinct review stages on the same job retain their normal
        # first-call behavior; the guard is scoped to phase_acceptance only.
        later = self.ledger.reserve(PRODUCT_ID, "G1", "review", 90, job_id=JOB_ID,
                                   job_token="token-1", requested_model="opencode-go/deepseek-v4.1-flash",
                                   stage="aggregate-semantic-review", plan_id=PLAN_ID)
        self.assertIsNotNone(later["id"])


if __name__ == "__main__":
    unittest.main()
