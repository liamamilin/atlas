"""Formal same-job protocol recovery through a real Pipeline, with a fake CLI."""
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from template_factory.budget import BudgetLedger
from template_factory.pipeline import Pipeline
from template_factory.protocol_grants import (
    CONTEXT_KEYS, JOB_ID, OPERATION_ID, STAGE, ProtocolRetryGrantService,
    protocol_retry_request,
)
from template_factory.protocol_recovery import ProtocolRecoveryService, RECOVERY_KEY
from template_factory.store import FactoryError, digest
from template_factory.v1_batches import BatchService

DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
NOW = 1792425000.0
PLAN = "plan_87059846caf345d2b2fe690657cf324f"
CAMPAIGN = "atlas-v1-first-production-2026-10-19"
PRODUCT = "product-c42848f63251507bd9d911a5"


class ProtocolPipelineLinkTests(unittest.TestCase):
    def setUp(self):
        # Existing fixture installs the real-shaped case library, fixed source,
        # original artifact and failed prepared source in a temporary store.
        self.base = r5_fixture.R5PreparedLinkTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.tearDown)
        self.store = self.base.store
        self.archive = DOCS / "g1-protocol-recovery-2026-10-19"
        source = self.archive / "authorization/ATLAS_G1_PROTOCOL_RETRY_CODEX_INSTRUCTIONS.txt"
        target = self.base.root / source.relative_to(DOCS.parent.parent)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        shutil.copytree(self.archive / "original-phase-input",
                        self.store.root / "jobs" / JOB_ID / "attempt-1" / STAGE)
        baseline = json.loads((self.archive / "baseline-records.json").read_text())
        original_bundle = json.loads(baseline["job"]["snapshot"])["cognitive_repair"]["bundle_path"]
        shutil.copytree(DOCS / "v1-2026-10-19/g1-real-sample/template-8d9229d3895b",
                        self.store.root / original_bundle)
        self.ledger = BudgetLedger(self.store, campaign_id=CAMPAIGN, clock=lambda: NOW)
        with self.store.connect(True) as con:
            for table in ("tf_budget_reservation", "tf_budget_repair", "tf_budget_amendment", "tf_budget_phase"):
                con.execute("DELETE FROM " + table)
                for row in baseline[table]:
                    columns = list(row)
                    con.execute("INSERT INTO " + table + "(" + ",".join(columns) + ") VALUES(" + ",".join("?" for _ in columns) + ")", tuple(row[k] for k in columns))
            job = baseline["job"]
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (job["batch_id"], "paused", json.dumps(json.loads(job["snapshot"])["config"]), job["created_at"]))
            columns = list(job)
            con.execute("INSERT INTO job(" + ",".join(columns) + ") VALUES(" + ",".join("?" for _ in columns) + ")", tuple(job[k] for k in columns))
            for row in baseline["checkpoints"]:
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (row["job_id"], row["name"], row["body"]))
        self.request = protocol_retry_request(self.store)

    def test_formal_register_recover_resume_claim_and_pipeline_only_retries_phase(self):
        grant_service = ProtocolRetryGrantService(self.store, clock=lambda: NOW)
        grant = grant_service.register(self.request)
        before = self.store.job(JOB_ID)
        recovery = ProtocolRecoveryService(self.store, clock=lambda: NOW)
        request = {"grant_id": grant["id"], "idempotency_key": RECOVERY_KEY}
        receipt = recovery.recover(JOB_ID, request)
        self.assertEqual(receipt["attempt"], 3)
        self.assertTrue(recovery.recover(JOB_ID, request)["replayed"])
        self.assertEqual(self.store.job(JOB_ID)["snapshot"], before["snapshot"])
        self.assertIsNone(self.store.claim("temporary-fixture-worker"))
        self.assertFalse(self.store.owned(JOB_ID, "old-late-worker"))
        BatchService(self.store).action(PLAN, "resume")
        claimed = self.store.claim("temporary-fixture-worker")
        self.assertEqual((claimed["id"], claimed["attempt"]), (JOB_ID, 3))
        calls, next_work = [], []
        expected_context = {key: self.request[key] for key in CONTEXT_KEYS}
        test = self

        class OnlyPhaseCLI:
            def info(self):
                return {"provider_called": False}

            def run(self, directory, prompt, model, timeout, cancelled, progress, **kwargs):
                if Path(directory).name != STAGE:
                    next_work.append(Path(directory).name)
                    raise FactoryError("Fixture ends before next normal dimension; no real provider", "fixture_end", 409)
                budget = kwargs["budget"]
                test.assertEqual(budget["stage"], OPERATION_ID)
                test.assertEqual(budget["retry"], 1)
                test.assertEqual(budget["protocol_context"], expected_context)
                ledger = budget["ledger"]
                reservation = ledger.reserve(budget["identity"], budget["phase"], budget["kind"], timeout,
                    job_id=budget["job_id"], requested_model=model, stage=budget["stage"], retry=budget["retry"],
                    retry_scope=budget["retry_scope"], plan_id=budget["plan_id"], protocol_context=budget["protocol_context"])
                test.assertEqual(reservation["protocol_grant_id"], grant["id"])
                ledger.mark_started(reservation["id"])
                ledger.finish(reservation["id"], "completed", outcome="fake CLI fixture; not real review")
                calls.append(reservation)
                return {"summary": "Fixture only, not a real model review.", "checks": [{"dimension": "phase_acceptance", "outcome": "passed", "files": ["DRAFT.md"], "reason": "Fixture protocol response."}], "suggestions": []}

        real_ledger = BudgetLedger
        def fixed_ledger(store, **kwargs):
            return real_ledger(store, **{**kwargs, "clock": lambda: NOW})
        with patch("template_factory.budget.BudgetLedger", side_effect=fixed_ledger):
            with self.assertRaises(FactoryError) as stopped:
                Pipeline(self.store, cli=OnlyPhaseCLI()).run(claimed)
            self.assertEqual(stopped.exception.code, "fixture_end")
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(next_work), 1)
        self.assertIn("decisions_defaults", next_work[0])
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 57)
        self.assertEqual(grant_service.get(grant["id"])["status"], "consumed")
        self.assertEqual(grant_service.register(self.request)["id"], grant["id"])
        self.assertEqual(recovery.recover(JOB_ID, request)["attempt"], 3)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0], 5)
        for row in json.loads((self.archive / "baseline-records.json").read_text())["checkpoints"]:
            self.assertEqual(self.store.checkpoint(JOB_ID, row["name"]), json.loads(row["body"]))
        completed = self.store.checkpoint(JOB_ID, "blueprint-design-check-0-phase_acceptance")
        self.assertEqual(completed["digest"], digest(completed["result"]))
        self.assertEqual(completed["result"]["outcome"], "passed")
        attempt = self.store.root / "jobs" / JOB_ID / "attempt-3"
        self.assertFalse(list(attempt.glob("blueprint-generate*")))
        self.assertFalse(list(attempt.glob("case-*")))


if __name__ == "__main__":
    unittest.main()
