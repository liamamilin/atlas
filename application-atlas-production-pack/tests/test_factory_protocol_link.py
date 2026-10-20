"""Formal same-job protocol recovery through a real Pipeline, with a fake CLI."""
import json
from pathlib import Path
import shutil
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from template_factory.budget import BudgetLedger
from template_factory.pipeline import Pipeline
from template_factory.protocol_grants import (
    JOB_ID, STAGE, ProtocolRetryGrantService,
    protocol_retry_request,
)
from template_factory.protocol_recovery import ProtocolRecoveryService, RECOVERY_KEY
from template_factory.store import FactoryError
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

    def test_formal_register_recover_resume_claim_then_old_source_conflict_stops_before_provider(self):
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
        provider_calls = []
        class NoProviderBeforeSourceGate:
            def info(self):
                return {"provider_called": False}

            def run(self, directory, prompt, model, timeout, cancelled, progress, **kwargs):
                provider_calls.append(Path(directory).name)
                raise AssertionError("legacy source conflict must stop before provider invocation")

        with self.assertRaises(FactoryError) as stopped:
            Pipeline(self.store, cli=NoProviderBeforeSourceGate()).run(claimed)
        self.assertEqual(stopped.exception.code, "invalid_feature_sources")
        self.assertIn("S17", str(stopped.exception))
        self.assertEqual(provider_calls, [])
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 56)
        self.assertEqual(grant_service.get(grant["id"])["status"], "available")
        self.assertEqual(grant_service.register(self.request)["id"], grant["id"])
        self.assertEqual(recovery.recover(JOB_ID, request)["attempt"], 3)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0], 5)
        for row in json.loads((self.archive / "baseline-records.json").read_text())["checkpoints"]:
            self.assertEqual(self.store.checkpoint(JOB_ID, row["name"]), json.loads(row["body"]))
        completed = self.store.checkpoint(JOB_ID, "blueprint-design-check-0-phase_acceptance")
        self.assertIsNone(completed)
        attempt = self.store.root / "jobs" / JOB_ID / "attempt-3"
        self.assertFalse(list(attempt.glob("blueprint-generate*")))
        self.assertFalse(list(attempt.glob("case-*")))


if __name__ == "__main__":
    unittest.main()
