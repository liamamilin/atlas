"""Temporary-store checks for the bounded R6 amendment and activation gate."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import (
    BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN,
    G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT, G1_R5_BASE_DEADLINE,
    G1_R5_BASE_STARTED, G1_R5_DEADLINE, G1_R6_AUTHORIZATION_SCHEMA,
    G1_R6_AUTHORIZATION_SOURCE_DIGEST, G1_R6_AUTHORIZATION_SOURCE_REF,
    G1_R6_FAILED_ERROR, G1_R6_FAILED_JOB, G1_R6_FAILED_STAGE,
    G1_R6_IDEMPOTENCY_KEY, G1_R6_OLD_DEADLINE, G1_R6_PREDECESSOR_ID,
    G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID,
    G1_R6_WINDOW_SECONDS,
)
from template_factory.store import FactoryError, FactoryStore, digest


class FactoryBudgetR6Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "application-atlas-production-pack"
        self.pack.mkdir()
        self.repo = Path(__file__).resolve().parents[2]
        self.clock = [G1_R6_OLD_DEADLINE + 10]
        self.store = FactoryStore(self.root / "state", self.repo / "application-atlas-production-pack")
        self.ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN,
                                   clock=lambda: self.clock[0])
        self.service = BudgetAmendmentService(self.store, clock=lambda: self.clock[0])
        self.prepared_request = {"schema": "atlas.failed-plan-revision.v2", "binding": {"case_basis_digest": "basis", "facts_view_digest": "facts"}}
        self.manifest = {"entries": ["manifest"]}
        self.prepared_request["program_reuse_manifest"] = self.manifest
        self.prepared = {"request_digest": digest(self.prepared_request),
                         "binding": {"case_basis_digest": "basis", "facts_view_digest": "facts"},
                         "effective_plan_digest": "effective", "case_design": [{"choice": "x"}],
                         "prepared_program_reuse": self.manifest}
        self._seed()

    def tearDown(self):
        self.temp.cleanup()

    def _seed(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1",
                         G1_R5_BASE_STARTED, G1_R5_BASE_DEADLINE))
            con.execute("INSERT INTO tf_budget_amendment VALUES(?,?,?,?,?,?,?,?,?,2,4,5,5,64,?,?,?, ?,?)",
                        (G1_R6_PREDECESSOR_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                         G1_AMENDMENT_PLAN, "prior", "prior", "R5", "R5", "r5-key",
                         G1_R6_OLD_DEADLINE, 28800, G1_R5_BASE_STARTED,
                         G1_R6_OLD_DEADLINE - 1, G1_R6_OLD_DEADLINE))
            for index in range(5):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"repair-{index}", index))
            # Fifty-eight ordinary calls and the three retained retry-scope rows.
            for index in range(64):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,stage,retry,retry_scope) VALUES(?,?,?,?,?,?,?,?,?,?)",
                            (f"call-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                             "G1", "production", "completed", index,
                             "blueprint-spec-review-0-phase_acceptance", index if index >= 62 or index == 0 else None,
                             "blueprint-spec-review:phase_acceptance" if index >= 62 or index == 0 else None))
            grant_request = {"schema": "atlas.protocol-retry-grant.v1"}
            con.execute("INSERT INTO tf_protocol_retry_grant VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (G1_R6_PROTOCOL_GRANT_ID, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN,
                         G1_AMENDMENT_PRODUCT, G1_R6_FAILED_JOB, "protocol-source", "digest",
                         json.dumps(grant_request), digest(grant_request), "grant-key", "consumed",
                         G1_R6_PROTOCOL_RESERVATION_ID, 1))
            con.execute("INSERT INTO tf_protocol_retry_grant_use VALUES(?,?,?,?,?)",
                        (G1_R6_PROTOCOL_GRANT_ID, G1_R6_PROTOCOL_RESERVATION_ID, "consumed", 1, None))
            # The grant reservation is already included in the 64-call baseline.
            con.execute("UPDATE tf_budget_reservation SET id=? WHERE id='call-0'",
                        (G1_R6_PROTOCOL_RESERVATION_ID,))
            snapshot = {"v1": {"campaign_id": G1_AMENDMENT_CAMPAIGN,
                               "plan_id": G1_AMENDMENT_PLAN,
                               "product_id": G1_AMENDMENT_PRODUCT}}
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (G1_R6_FAILED_JOB, "batch-1", "blueprint-production", "failed",
                         G1_R6_FAILED_STAGE, 4, None, None, json.dumps(snapshot),
                         G1_R6_FAILED_ERROR, "created", "updated"))

    def request(self):
        return {
            "schema": G1_R6_AUTHORIZATION_SCHEMA,
            "campaign_id": G1_AMENDMENT_CAMPAIGN, "product_id": G1_AMENDMENT_PRODUCT,
            "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": G1_R6_AUTHORIZATION_SOURCE_REF,
            "source_digest": G1_R6_AUTHORIZATION_SOURCE_DIGEST,
            "summary": "One source-alignment repair and one new G1 window.",
            "reason": "Exact prepared source-alignment revision.",
            "idempotency_key": G1_R6_IDEMPOTENCY_KEY,
            "predecessor_amendment_id": G1_R6_PREDECESSOR_ID,
            "old_job_id": G1_R6_FAILED_JOB, "old_job_attempt": 4,
            "old_job_snapshot_digest": digest({"v1": {"campaign_id": G1_AMENDMENT_CAMPAIGN,
                                                        "plan_id": G1_AMENDMENT_PLAN,
                                                        "product_id": G1_AMENDMENT_PRODUCT}}),
            "old_job_error": G1_R6_FAILED_ERROR, "old_job_stage": G1_R6_FAILED_STAGE,
            "case_basis_digest": "basis", "facts_view_digest": "facts",
            "case_design_digest": digest(self.prepared["case_design"]),
            "prepared_revision": self.prepared_request,
            "prepared_revision_digest": digest(self.prepared_request),
            "effective_plan_digest": "effective",
            "program_manifest_digest": digest(self.prepared["prepared_program_reuse"]),
            "protocol_grant_id": G1_R6_PROTOCOL_GRANT_ID,
            "protocol_reservation_id": G1_R6_PROTOCOL_RESERVATION_ID,
            "baseline_cli_sessions": 64, "baseline_repair_count": 5,
            "baseline_scope_retry_rows": 3, "baseline_active": 0,
            "old_deadline": G1_R6_OLD_DEADLINE, "window_seconds": G1_R6_WINDOW_SECONDS,
        }

    def test_register_is_pending_and_replay_keeps_full_request(self):
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", return_value=self.prepared):
            amendment = self.service.register(self.request())
            replay = self.service.register(self.request())
        self.assertEqual(amendment["id"], replay["id"])
        self.assertEqual(amendment["version"], 3)
        self.assertEqual(amendment["new_repair_limit"], 6)
        self.assertIsNone(amendment["activated_at"])
        with self.store.connect() as con:
            row = con.execute("SELECT request_json,request_digest FROM tf_budget_amendment_binding WHERE amendment_id=?",
                              (amendment["id"],)).fetchone()
        self.assertEqual(json.loads(row["request_json"]), self.request())
        self.assertEqual(row["request_digest"], digest(self.request()))
        with self.assertRaises(FactoryError):
            self.service.activate(amendment["id"])

    def test_registration_rejects_changed_baseline_and_different_key(self):
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", return_value=self.prepared):
            with self.assertRaises(FactoryError):
                self.service.register({**self.request(), "idempotency_key": "other-key"})
            request = self.request()
            amendment = self.service.register(request)
            with self.assertRaises(FactoryError):
                self.service.register({**request, "reason": "changed"})
        self.assertIsNone(amendment["activated_at"])

    def test_r6_activation_is_atomic_only_and_uses_new_deadline_once(self):
        with patch("template_factory.plan_revision.PreparedRevisionService.prepare", return_value=self.prepared):
            amendment = self.service.register(self.request())
        with self.store.connect(True) as con:
            activated = self.service.activate_r6_locked(con, amendment["id"])
        self.assertEqual(activated["new_deadline"], self.clock[0] + G1_R6_WINDOW_SECONDS)
        with self.assertRaises(FactoryError):
            with self.store.connect(True) as con:
                self.service.activate_r6_locked(con, amendment["id"])
        self.assertEqual(self.service.list()[-1]["new_deadline"], self.clock[0] + G1_R6_WINDOW_SECONDS)


if __name__ == "__main__":
    unittest.main()
