"""Focused temporary-store tests for fixed same-job protocol recovery."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.protocol_grants import ProtocolRetryGrantService, protocol_retry_request
from template_factory.protocol_recovery import (
    CASE_ADAPTATION_CHECKPOINT, JOB_ID, PLAN_CHECKPOINT, RECOVERY_KEY, REUSED_CHECKPOINTS, STAGE,
    ProtocolRecoveryService,
)
from template_factory.store import FactoryError, FactoryStore, canonical

PACK = Path(__file__).resolve().parents[1]
ARCHIVE = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-r5-2026-10-19"
ATTEMPT = ARCHIVE / "real-pre-reviews/attempt-1" / STAGE


class ProtocolRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        pack = self.root / "pack"
        pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", pack / "mvp_apps.json")
        shutil.copy(PACK / "mvp_apps_classified.json", pack / "mvp_apps_classified.json")
        (pack / "atlas").mkdir()
        self.store = FactoryStore(self.root / "factory", pack)
        self.service = ProtocolRecoveryService(self.store, clock=lambda: 1792420000.0)
        ProtocolRetryGrantService(self.store, clock=lambda: 1792420000.0)
        self._install_paused_job()
        self._install_grant()

    def tearDown(self):
        self.temp.cleanup()

    def _install_paused_job(self):
        fixture = json.loads((ARCHIVE / "job-latest.json").read_text())
        # Reuse the archived full snapshot, while constructing an isolated paused parent.
        with self.store.connect(True) as con:
            con.execute("""INSERT INTO tf_budget_reservation
                (id,campaign_id,identity,phase,kind,status,created,started,finished,job_id,requested_model,
                 requested_effort,stage,retry,observed_model,observed_effort,outcome,group_kind,retry_scope)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
                "bud_1806199dfa08411d8f71ee84ea06676f", "atlas-v1-first-production-2026-10-19",
                "product-c42848f63251507bd9d911a5", "G1", "review", "failed", 1.0, 1.0, 2.0,
                JOB_ID, "opencode-go/deepseek-v4.1-flash", None,
                STAGE + ":449b8a5093505d77", None, None, None, "cli_protocol", "production", None))
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (fixture["batch_id"], "paused", "{}", "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                JOB_ID, fixture["batch_id"], "blueprint-production", "paused_budget", STAGE, 2,
                "stale-token", 9999999999.0, canonical(fixture["snapshot"]),
                "budget_retry_limit: transient retry limit exhausted", "2026-10-19T00:00:00Z", "2026-10-19T00:01:00Z"))
            archived = ARCHIVE / "real-checkpoints"
            actual_by_name = {
                REUSED_CHECKPOINTS[0]: "blueprint-design-check-0-scenario_scope.json",
                REUSED_CHECKPOINTS[1]: "blueprint-design-check-0-product_completeness.json",
                REUSED_CHECKPOINTS[2]: "blueprint-design-check-0-architecture_contract-bbc43771a1bbbe99.json",
                CASE_ADAPTATION_CHECKPOINT: "case-adaptation-prepared-aaf080ba52611126.json",
                PLAN_CHECKPOINT: "blueprint-plan-0.json",
            }
            for name, source_name in actual_by_name.items():
                body = json.loads((archived / source_name).read_text())
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (JOB_ID, name, canonical(body)))
        target = self.store.root / "jobs" / JOB_ID / "attempt-1" / STAGE
        target.mkdir(parents=True)
        shutil.copy(ATTEMPT / "input.json", target / "input.json")
        shutil.copy(ATTEMPT / "stdout.log", target / "stdout.log")

    def _install_grant(self):
        request = protocol_retry_request(self.store)
        encoded = json.dumps(request, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        with self.store.connect(True) as con:
            con.execute("""INSERT INTO tf_protocol_retry_grant
                (id,campaign_id,plan_id,product_id,job_id,source_ref,source_digest,request_json,
                 request_digest,idempotency_key,status,created_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (
                "pgrant_test", request["campaign_id"], request["plan_id"], request["product_id"],
                JOB_ID, request["source_ref"], request["source_digest"], encoded,
                __import__("hashlib").sha256(encoded.encode()).hexdigest(), request["idempotency_key"],
                "available", 1792420000.0))

    def test_recovery_is_atomic_same_job_and_idempotent(self):
        before = self.store.job(JOB_ID)
        request = {"grant_id": "pgrant_test", "idempotency_key": RECOVERY_KEY}
        recovered = self.service.recover(JOB_ID, request)
        self.assertEqual((recovered["job_id"], recovered["old_attempt"], recovered["attempt"]), (JOB_ID, 2, 3))
        self.assertFalse(recovered["replayed"])
        after = self.store.job(JOB_ID)
        with self.store.connect() as con:
            live = con.execute("SELECT state,attempt,token,lease FROM job WHERE id=?", (JOB_ID,)).fetchone()
        self.assertEqual(tuple(live), ("queued", 3, None, None))
        self.assertEqual(after["snapshot"], before["snapshot"])
        with self.store.connect() as con:
            names = [row[0] for row in con.execute("SELECT name FROM checkpoint WHERE job_id=? ORDER BY name", (JOB_ID,))]
        self.assertEqual(names, sorted((*REUSED_CHECKPOINTS, CASE_ADAPTATION_CHECKPOINT, PLAN_CHECKPOINT)))
        with self.store.connect() as con:
            parent = con.execute("SELECT state FROM batch WHERE id=?", (after["batch_id"],)).fetchone()[0]
            archived = con.execute("SELECT old_error,old_attempt,old_token,old_lease,grant_id FROM tf_protocol_recovery WHERE job_id=?", (JOB_ID,)).fetchone()
        self.assertEqual(parent, "paused")
        self.assertEqual(tuple(archived), (before["error"], 2, "stale-token", 9999999999.0, "pgrant_test"))
        replay = self.service.recover(JOB_ID, request)
        self.assertTrue(replay["replayed"])
        self.assertEqual(self.store.job(JOB_ID)["attempt"], 3)
        with self.assertRaises(FactoryError):
            self.service.recover(JOB_ID, {"grant_id": "pgrant_other", "idempotency_key": RECOVERY_KEY})

    def test_tampered_checkpoint_rejects_without_mutating_job(self):
        with self.store.connect(True) as con:
            con.execute("UPDATE checkpoint SET body=? WHERE job_id=? AND name=?", (
                canonical({"digest": "changed", "result": {"outcome": "passed"}}), JOB_ID, REUSED_CHECKPOINTS[0]))
        with self.assertRaises(FactoryError):
            self.service.recover(JOB_ID, {"grant_id": "pgrant_test", "idempotency_key": RECOVERY_KEY})
        job = self.store.job(JOB_ID)
        self.assertEqual((job["state"], job["attempt"]), ("paused_budget", 2))
        with self.store.connect() as con:
            self.assertIsNone(con.execute("SELECT 1 FROM tf_protocol_recovery WHERE job_id=?", (JOB_ID,)).fetchone())


if __name__ == "__main__":
    unittest.main()
