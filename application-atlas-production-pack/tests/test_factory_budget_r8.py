import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import (
    BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN,
    G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT,
)
from template_factory.store import FactoryError, FactoryStore, digest


class FrozenRevisionBudgetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = Path(__file__).resolve().parents[2]
        self.store = FactoryStore(self.root / "state", self.repo / "application-atlas-production-pack")
        self.now = [2_000_000_000.0]
        self.ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN,
                                   clock=lambda: self.now[0])
        self.service = BudgetAmendmentService(self.store, clock=lambda: self.now[0])
        self.resume = {
            "grant_id": "egrant_5168847ee98d4b7f980779bb9199f44f",
            "job_id": "job_b01427592b164863aab5bedf7b3863bb",
            "campaign_id": G1_AMENDMENT_CAMPAIGN,
            "plan_id": G1_AMENDMENT_PLAN,
            "product_id": G1_AMENDMENT_PRODUCT,
            "previous_deadline": 1_792_495_312.855422,
            "paused_at": 1_792_490_680.244128,
            "remaining_seconds": 4632.611294,
            "activated_at": 1_792_496_531.354074,
            "effective_deadline": 1_792_501_163.965368,
            "authorization_digest": "4384d1c263c8c553c73b85b2fe6e11533325b64f95c9343fe63a49f4fd97767e",
            "external_cli_sessions": 1,
        }
        self._seed_history()
        self.resume_patch = patch("template_factory.budget.BudgetLedger._time_resume_locked",
                                  side_effect=self._time_resume)
        self.resume_patch.start()
        self.addCleanup(self.resume_patch.stop)

    def tearDown(self):
        self.temp.cleanup()

    def _time_resume(self, _con, identity, phase="G1", plan_id=None):
        if (self.store and str(identity) == G1_AMENDMENT_PRODUCT and str(phase) == "G1"
                and plan_id == G1_AMENDMENT_PLAN):
            return self.resume
        return None

    def _seed_history(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", 1_792_410_000.0,
                         1_792_495_312.855422))
            con.execute(
                "INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,4,6,7,7,82,?,0,1,1,?)",
                ("bamd_" + "4" * 32, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                 G1_AMENDMENT_PLAN, "prior-auth.txt", "a" * 64, "prior", "prior", "prior-key",
                 1_792_495_312.855422, 1_792_495_312.855422),
            )
            for index in range(7):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"repair-{index}", index + 1))
            for index in range(82):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"reservation-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                             "G1", "review", "completed", index + 1, "production"))

    def _request(self):
        source_ref = "docs/template-factory/g1-r8-contract-convergence-2026-10-20/authorization/ATLAS_G1_R8_CONTRACT_CONVERGENCE_CODEX_INSTRUCTIONS.txt"
        source_digest = hashlib.sha256((self.repo / source_ref).read_bytes()).hexdigest()
        limits = {"cli_sessions": 500, "expected_repairs": 7, "repair_limit": 8,
                  "expected_cli_total": 83}
        supersedes = self.ledger._timing_source_snapshot(self.resume)
        timing = {"window_seconds": 86400, "supersedes": supersedes}
        prepared_revision = {
            "schema": "atlas.frozen-plan-revision.v1",
            "binding": {"job_id": "job_frozen", "campaign_id": G1_AMENDMENT_CAMPAIGN,
                        "plan_id": G1_AMENDMENT_PLAN, "product_id": G1_AMENDMENT_PRODUCT,
                        "scenario_id": "scenario-id", "scenario_revision": 2},
            "source_authorization": {"source_ref": source_ref, "source_digest": source_digest,
                                     "revision_ref": "revision.json", "revision_digest": "b" * 64},
        }
        case_design = {"choices": []}
        program_revision = {"entries": []}
        request = {
            "schema": "atlas.budget-amendment.v3", "campaign_id": G1_AMENDMENT_CAMPAIGN,
            "product_id": G1_AMENDMENT_PRODUCT, "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": source_ref, "source_digest": source_digest,
            "summary": "bounded frozen candidate revision", "reason": "authorized new content",
            "idempotency_key": "r8-budget-test-key", "source_gate": {"source_commit": "c" * 40},
            "limits": limits, "timing": timing, "prepared_revision": prepared_revision,
            "prepared_revision_digest": digest(prepared_revision),
            "effective_plan_digest": "d" * 64, "case_design_digest": digest(case_design),
            "program_revision_digest": digest(program_revision),
        }
        response = {"request_digest": request["prepared_revision_digest"],
                    "effective_plan_digest": request["effective_plan_digest"],
                    "case_design_digest": request["case_design_digest"], "case_design": case_design,
                    "prepared_program_revision": program_revision,
                    "binding": prepared_revision["binding"],
                    "source_authorization": prepared_revision["source_authorization"],
                    "authorization_limits": limits, "authorization_timing": timing}
        return request, response

    def _prepared(self, response):
        return lambda _service, _job_id, _request: response

    def _register(self):
        request, response = self._request()
        prepared_patch = patch("template_factory.plan_revision.PreparedRevisionService.prepare", self._prepared(response))
        gate_patch = patch("template_factory.evidence_recovery.validate_source_gate")
        prepared_patch.start()
        gate_patch.start()
        self.addCleanup(prepared_patch.stop)
        self.addCleanup(gate_patch.stop)
        amendment = self.service.register(request)
        return request, response, amendment

    def test_pending_is_inert_then_activation_supersedes_expired_resume_once(self):
        _, _, amendment = self._register()
        before = self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(before["deadline_source"], "authorized_external_pause_resume")
        self.assertEqual(before["effective_deadline"], self.resume["effective_deadline"])
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_deadline")
        with self.store.connect(True) as con:
            activated = self.service.activate_frozen_locked(
                con, amendment["id"], expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
        self.assertEqual(activated["new_deadline"], self.now[0] + 86400)
        after = self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(after["deadline_source"], "amendment_superseding_timing")
        self.assertEqual(after["supersedes"], self.ledger._timing_source_snapshot(self.resume))
        effective = self.ledger.snapshot()["effective_timings"]
        self.assertEqual(effective[0]["effective_deadline"], after["effective_deadline"])
        self.assertEqual(effective[0]["deadline_source"], after["deadline_source"])
        self.assertEqual(self.ledger.phase_remaining(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN), 86400)
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 83)
        self.assertEqual(self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "eighth", plan_id=G1_AMENDMENT_PLAN)["repairs_used"], 8)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.record_repair(G1_AMENDMENT_PRODUCT, "ninth", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_repair_limit")
        self.now[0] += 60
        self.assertEqual(self.ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), activated["new_deadline"])
        reservation = self.ledger.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN)
        self.assertTrue(reservation["id"])
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 84)

    def test_external_cli_history_remains_separate_and_other_scopes_stay_unchanged(self):
        _, _, amendment = self._register()
        baseline = self.ledger.snapshot()
        self.assertEqual(baseline["factory_cli_sessions_used"], 82)
        self.assertEqual(baseline["external_cli_sessions_used"], 1)
        self.assertEqual(baseline["cli_sessions_used"], 83)
        with self.store.connect(True) as con:
            self.service.activate_frozen_locked(con, amendment["id"],
                expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
        snapshot = self.ledger.snapshot()
        self.assertEqual(snapshot["cli_sessions_used"], 83)
        other = self.ledger.effective_deadline_snapshot("other-product", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(other["deadline_source"], "base")
        t08 = self.ledger.effective_deadline_snapshot(G1_AMENDMENT_PRODUCT, "T08", plan_id="plan_t08")
        self.assertEqual(t08["deadline_source"], "base")
        self.assertIsNone(t08["amendment_id"])

    def test_global_cli_budget_exhaustion_counts_external_session_once(self):
        _, _, amendment = self._register()
        with self.store.connect(True) as con:
            self.service.activate_frozen_locked(con, amendment["id"],
                expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
        with self.store.connect(True) as con:
            for index in range(417):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"extra-{index}", G1_AMENDMENT_CAMPAIGN, "another-product", "G1",
                             "review", "completed", 1000 + index, "production"))
        snapshot = self.ledger.snapshot()
        self.assertEqual(snapshot["factory_cli_sessions_used"], 499)
        self.assertEqual(snapshot["external_cli_sessions_used"], 1)
        self.assertEqual(snapshot["cli_sessions_used"], snapshot["cli_sessions_limit"])
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN)
        self.assertEqual(caught.exception.code, "budget_exhausted")

    def test_baseline_race_and_transaction_failure_do_not_activate_or_double_count(self):
        _, _, amendment = self._register()
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, "unexpected-repair", 99))
        with self.store.connect(True) as con:
            with self.assertRaises(FactoryError):
                self.service.activate_frozen_locked(con, amendment["id"],
                    expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
        self.assertIsNone(self.service.list()[-1]["activated_at"])

    def test_spawn_intent_is_not_missed_by_registration_or_activation_active_checks(self):
        with self.store.connect(True) as con:
            con.execute("UPDATE tf_budget_reservation SET status='spawn_intent' WHERE id='reservation-0'")
        with self.assertRaises(FactoryError) as caught:
            self._register()
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertFalse(any(row["version"] == 5 for row in self.service.list()))

        with self.store.connect(True) as con:
            con.execute("UPDATE tf_budget_reservation SET status='completed' WHERE id='reservation-0'")
        _, _, amendment = self._register()
        with self.store.connect(True) as con:
            con.execute("UPDATE tf_budget_reservation SET status='spawn_intent' WHERE id='reservation-0'")
        with self.store.connect(True) as con:
            with self.assertRaises(FactoryError) as caught:
                self.service.activate_frozen_locked(con, amendment["id"],
                    expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertIsNone(next(row for row in self.service.list() if row["id"] == amendment["id"])["activated_at"])

    def test_queue_failure_rolls_back_activation_deadline(self):
        _, _, amendment = self._register()
        class QueueFailure(Exception):
            pass
        with self.assertRaises(QueueFailure):
            with self.store.connect(True) as con:
                self.service.activate_frozen_locked(con, amendment["id"],
                    expected_prepared_digest=self._request()[0]["prepared_revision_digest"])
                raise QueueFailure("simulated successor queue failure")
        row = next(item for item in self.service.list() if item["id"] == amendment["id"])
        self.assertIsNone(row["activated_at"])
        self.assertIsNone(row["new_deadline"])

    def test_public_activation_cannot_bypass_successor_transaction(self):
        _, _, amendment = self._register()
        with self.assertRaises(FactoryError) as caught:
            self.service.activate(amendment["id"])
        self.assertEqual(caught.exception.code, "budget_amendment_version")
        self.assertIsNone(self.service.list()[-1]["activated_at"])

    def test_prepared_policy_summary_must_match_budget_request(self):
        request, response = self._request()
        response["authorization_limits"] = {**response["authorization_limits"], "repair_limit": 9}
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self._prepared(response)), \
                patch("template_factory.evidence_recovery.validate_source_gate"):
            with self.assertRaises(FactoryError) as caught:
                self.service.register(request)
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertFalse(any(row["version"] == 5 for row in self.service.list()))

    def test_prepared_timing_policy_cannot_rebind_a_different_current_snapshot(self):
        request, response = self._request()
        timing = json.loads(json.dumps(request["timing"]))
        timing["supersedes"]["effective_deadline"] += 1
        request["timing"] = timing
        response["authorization_timing"] = timing
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", self._prepared(response)), \
                patch("template_factory.evidence_recovery.validate_source_gate"):
            with self.assertRaises(FactoryError) as caught:
                self.service.register(request)
        self.assertEqual(caught.exception.code, "budget_amendment_basis")
        self.assertFalse(any(row["version"] == 5 for row in self.service.list()))

