import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import (
    BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN,
    G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT, G1_R5_AUTHORIZATION_SCHEMA,
    G1_R5_BASE_DEADLINE, G1_R5_BASE_STARTED, G1_R5_DEADLINE,
    G1_R5_EFFECTIVE_PLAN_DIGEST, G1_R5_PREPARED_REQUEST_DIGEST,
    G1_R5_REPAIR_REQUEST_DIGEST,
    _legacy_retry_scope,
)
from template_factory.store import FactoryError, FactoryStore


class FactoryBudgetR5Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "application-atlas-production-pack"
        self.pack.mkdir()
        # The authorization/material files are resolved from repository root.
        self.repo = Path(__file__).resolve().parents[2]
        self.now = [G1_R5_DEADLINE - 500]
        self.store = FactoryStore(self.root / "state", self.repo / "application-atlas-production-pack")
        self.ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.now[0])
        self.service = BudgetAmendmentService(self.store, clock=lambda: self.now[0])
        self._seed_basis()

    def tearDown(self):
        self.temp.cleanup()

    def _seed_basis(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", G1_R5_BASE_STARTED, G1_R5_BASE_DEADLINE))
            con.execute("INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,1,2,4,2,42,?,?,?,?,?)",
                        ("bamd_9378738d1e274c409f756d92ec9c2ac5", G1_AMENDMENT_CAMPAIGN,
                         G1_AMENDMENT_PRODUCT, G1_AMENDMENT_PLAN,
                         "docs/template-factory/g1-convergence-2026-10-19/authorization.txt", "prior-digest",
                         "Prior authorized 2 to 4", "Prior record", "prior-idempotency",
                         G1_R5_BASE_DEADLINE, 8 * 60 * 60, G1_R5_BASE_STARTED,
                         1792408423.754534, G1_R5_DEADLINE))
            for index in range(4):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"repair-{index}", 100 + index))
            for index in range(52):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"reservation-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                             "G1", "production", "completed", 100 + index, "production"))

    def request(self):
        source = self.repo / "docs/template-factory/g1-r5-2026-10-19/authorization/ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt"
        from template_factory.store import digest
        prep = json.loads((self.repo / "docs/template-factory/g1-preparation-2026-10-19/prepare-revision-request.json").read_text())
        return {
            "schema": G1_R5_AUTHORIZATION_SCHEMA,
            "campaign_id": G1_AMENDMENT_CAMPAIGN,
            "product_id": G1_AMENDMENT_PRODUCT,
            "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": "docs/template-factory/g1-r5-2026-10-19/authorization/ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt",
            "source_digest": __import__("hashlib").sha256(source.read_bytes()).hexdigest(),
            "summary": "One additional repair for the bound G1 plan.",
            "reason": "The exact prepared revision was authorized.",
            "idempotency_key": "atlas-g1-r5-user-authorization-2026-10-19-v1",
            "predecessor_amendment_id": "bamd_9378738d1e274c409f756d92ec9c2ac5",
            "failed_job_id": "job_a53c47f3694047489c4f82cfc2e346be",
            "checkpoint_name": "blueprint-plan-1",
            "checkpoint_result_digest": "b82eaafd6126d5e21e1ccd734a590b5e8a417f51497465e72a4574ab20873894",
            "prepared_request_digest": G1_R5_PREPARED_REQUEST_DIGEST,
            "effective_plan_digest": G1_R5_EFFECTIVE_PLAN_DIGEST,
            "patch_digest": "76673a0a9b28bd52aab8d44208ea58a6764aa78d0d9b541af2ff41e4d237241c",
            "repair_request_digest": G1_R5_REPAIR_REQUEST_DIGEST,
        }

    def prepared(self, _job_id, _request):
        response = json.loads((self.repo / "docs/template-factory/g1-preparation-2026-10-19/prepare-revision-response.json").read_text())
        return response

    def test_v2_pending_activation_and_inherited_deadline(self):
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", wraps=self.prepared) as prepare:
            amendment = self.service.register(self.request())
            prepare.assert_called_once()
        self.assertEqual((amendment["version"], amendment["old_repair_limit"], amendment["new_repair_limit"]), (2, 4, 5))
        self.assertEqual(amendment["old_deadline"], G1_R5_DEADLINE)
        self.assertEqual(amendment["new_deadline"], G1_R5_DEADLINE)
        self.assertIsNone(amendment["activated_at"])
        # Pending v2 is inert: v1 remains effective while the original base
        # segment fields remain unchanged.
        self.assertEqual(self.ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), G1_R5_DEADLINE)
        self.assertEqual(self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN)["base_deadline"], G1_R5_BASE_DEADLINE)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "fifth-before-activation", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_repair_limit")
        self.now[0] = G1_R5_DEADLINE - 1
        activated = self.service.activate(amendment["id"])
        self.assertEqual(activated["new_deadline"], G1_R5_DEADLINE)
        self.assertEqual(self.ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), G1_R5_DEADLINE)
        self.assertEqual(self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "fifth", plan_id=G1_AMENDMENT_PLAN)["repairs_used"], 5)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "sixth", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_repair_limit")
        self.assertEqual(self.service.activate(amendment["id"])["new_deadline"], G1_R5_DEADLINE)
        self.assertEqual(self.ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), G1_R5_DEADLINE)
        self.assertEqual(self.ledger.phase_remaining(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN), 1)
        self.ledger.pause("test")
        self.ledger.resume()
        restarted = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.now[0])
        self.assertEqual(restarted.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), G1_R5_DEADLINE)
        self.now[0] = G1_R5_DEADLINE
        with self.assertRaises(FactoryError) as caught:
            restarted.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_deadline")

    def test_idempotent_replay_precedes_consumed_baseline_and_preserves_full_binding(self):
        request = self.request()
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            original = self.service.register(request)
        with self.store.connect(True) as con:
            for index in range(2):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"later-{index}", 200 + index))
            for index in range(52):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"later-call-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                             "G1", "production", "completed", 200 + index, "production"))
            binding = con.execute("SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                                  (original["id"],)).fetchone()
        self.assertEqual(json.loads(binding["request_json"]), request)
        from template_factory.store import digest
        self.assertEqual(binding["request_digest"], digest(request))
        self.assertEqual(self.service.register(request)["id"], original["id"])
        with self.assertRaises(FactoryError) as caught:
            self.service.register({**request, "reason": "different request"})
        self.assertEqual(caught.exception.code, "idempotency_conflict")

    def test_rejects_wrong_binding_or_second_key_and_deadline_expiry(self):
        for key, value in (("patch_digest", "wrong"), ("predecessor_amendment_id", "wrong"),
                           ("source_digest", "wrong"), ("plan_id", "other"),
                           ("checkpoint_result_digest", "wrong"), ("effective_plan_digest", "wrong")):
            with self.subTest(key=key), patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
                with self.assertRaises(FactoryError):
                    self.service.register({**self.request(), key: value})
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            amendment = self.service.register(self.request())
            with self.assertRaises(FactoryError):
                self.service.register({**self.request(), "idempotency_key": "different-key"})
        self.now[0] = G1_R5_DEADLINE
        with self.assertRaises(FactoryError) as caught:
            self.service.activate(amendment["id"])
        self.assertEqual(caught.exception.code, "budget_deadline")
        self.assertIsNone(self.service.list()[-1]["activated_at"])

    def test_registration_requires_unmodified_first_baseline_and_failure_rolls_back(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, "unexpected-fifth", 300))
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            with self.assertRaises(FactoryError) as caught:
                self.service.register(self.request())
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertEqual([row["version"] for row in self.service.list()], [1])
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_amendment_binding").fetchone()[0], 0)

    def test_registration_rejects_any_active_reservation_at_fixed_baseline(self):
        with self.store.connect(True) as con:
            con.execute("UPDATE tf_budget_reservation SET status='reserved' WHERE id='reservation-0'")
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            with self.assertRaises(FactoryError) as caught:
                self.service.register(self.request())
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertEqual([row["version"] for row in self.service.list()], [1])

    def test_v2_does_not_change_other_products_or_non_g1_plan_deadlines(self):
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            amendment = self.service.register(self.request())
        self.service.activate(amendment["id"])
        self.ledger.begin_segment("T08")
        t08 = self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, "T08", plan_id="plan_t08")
        self.assertIsNone(t08["amendment_id"])
        self.assertEqual(t08["deadline_source"], "base")
        with self.assertRaises(FactoryError) as excluded:
            self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "t08-no-g1-increment", plan_id="plan_t08")
        self.assertEqual(excluded.exception.code, "budget_repair_limit")
        self.assertEqual(self.ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id="another-plan"), G1_R5_BASE_DEADLINE)
        self.assertEqual(self.ledger.effective_deadline("another-product", plan_id=G1_AMENDMENT_PLAN), G1_R5_BASE_DEADLINE)
        self.assertIsNone(self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, plan_id="another-plan")["amendment_id"])
        self.assertEqual(self.ledger.record_repair("another-product", "other-one")["repair_limit"], 2)
        self.assertEqual(self.ledger.record_repair("another-product", "other-two")["repair_limit"], 2)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.record_repair("another-product", "other-three")
        self.assertEqual(caught.exception.code, "budget_repair_limit")

    def test_concurrent_same_idempotency_key_returns_one_v2(self):
        outcomes = []
        barrier = threading.Barrier(2)
        def register():
            barrier.wait()
            request = self.request()
            try:
                outcomes.append(self.service.register(request))
            except FactoryError as error:
                outcomes.append(error.code)
        threads = [threading.Thread(target=register) for _ in range(2)]
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self.prepared):
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
        self.assertEqual(sum(isinstance(item, dict) for item in outcomes), 2)
        self.assertEqual(outcomes[0]["id"], outcomes[1]["id"])
        self.assertEqual(len([row for row in self.service.list() if row["version"] == 2]), 1)

    def test_design_binding_suffix_does_not_split_legacy_review_dimension(self):
        self.assertEqual(_legacy_retry_scope("blueprint-spec-review-3-category_evidence-0123456789abcdef"),
                         "blueprint-spec-review:category_evidence")
        self.assertEqual(_legacy_retry_scope("blueprint-spec-review-0-0123456789abcdef-scenario_scope"),
                         "blueprint-spec-review:scenario_scope")

    def test_actual_design_binding_stage_shares_explicit_review_retry_scope(self):
        self.ledger.begin_segment("T08")
        with self.store.connect(True) as con:
            con.execute(
                "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,stage,retry,group_kind,retry_scope) VALUES(?,?,?,?,?,?,?,?,?,?,NULL)",
                ("legacy-bound-review", G1_AMENDMENT_CAMPAIGN, "product-x", "T08", "review", "failed", 100,
                 "blueprint-spec-review-0-0123456789abcdef-scenario_scope", 1, "production"),
            )
        second = self.ledger.reserve(
            "product-x", "T08", "review", 60,
            stage="blueprint-spec-review-1-fedcba9876543210-scenario_scope",
            retry=2, retry_scope="blueprint-spec-review:scenario_scope",
        )
        self.assertTrue(second["id"])
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve(
                "product-x", "T08", "review", 60,
                stage="blueprint-spec-review-2-acde0123456789ab-scenario_scope",
                retry=1, retry_scope="blueprint-spec-review:scenario_scope",
            )
        self.assertEqual(caught.exception.code, "budget_retry_limit")


if __name__ == "__main__":
    unittest.main()
