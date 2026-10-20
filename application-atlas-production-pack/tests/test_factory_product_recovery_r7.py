"""Temporary-store integration for R7's inherited-deadline queue transaction."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_product_recovery_r6 as r6_fixture
from template_factory.budget import (
    BudgetAmendmentService, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN,
    G1_AMENDMENT_PRODUCT, G1_R7_OLD_DEADLINE,
    build_r7_authorization_request,
)
from template_factory.plan_revision import PreparedRevisionService
from template_factory.product_recovery import ProductRecoveryService, build_r7_product_resume_request
from template_factory.store import FactoryError, canonical, digest

DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
R7_DOCS = DOCS / "g1-r7-acceptance-alignment-2026-10-20"
R6_DOCS = DOCS / "g1-r6-source-alignment-2026-10-20"
RESUME_KEY = "atlas-g1-r7-acceptance-alignment-resume-test-v1"


class ProductRecoveryR7IntegrationTests(unittest.TestCase):
    def setUp(self):
        # Reuse the known clean temporary factory plus archived 64/5 ledger;
        # then layer the separately archived R7 71/6 failed-job evidence.
        self.base = r6_fixture.ProductRecoveryR6IntegrationTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.doCleanups)
        self.store, self.root = self.base.store, self.base.root
        self.clock = self.base.clock
        self.clock[0] = G1_R7_OLD_DEADLINE - 3600
        self._install_r7_source_material()
        self._install_r7_job()
        self._advance_budget_baseline()
        self.prepared_request = json.loads((R7_DOCS / "prepare-request.json").read_text())
        self.prepared = PreparedRevisionService(self.store).prepare(
            self.prepared_request["binding"]["job_id"], self.prepared_request)
        archived = json.loads((R7_DOCS / "prepare-response.json").read_text())
        self.assertEqual(self.prepared["request_digest"], archived["request_digest"])
        self.assertEqual(self.prepared["effective_plan_digest"], archived["effective_plan_digest"])
        self.assertEqual(self.prepared["case_design_digest"], archived["case_design_digest"])
        self.assertEqual(self.prepared["prepared_program_revision"], archived["prepared_program_revision"])
        self.amendments = BudgetAmendmentService(self.store, clock=lambda: self.clock[0])
        self.authorization = build_r7_authorization_request(
            self.store, self.prepared_request,
            summary="One bounded R7 acceptance-alignment successor; inherit the existing R6 cutoff.",
            reason="Exact prepared patch and nine-program manifest; preserve prior CLI, repair, retry and grant history.")
        self.amendment = self.amendments.register(self.authorization)
        self.request = self._resume_request()
        self.recovery = ProductRecoveryService(self.store, clock=lambda: self.clock[0])

    def _install_r7_source_material(self):
        for rel in ("authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt",
                    "authorization/approved-revision.json", "patch.json"):
            source = R7_DOCS / rel
            target = self.root / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        source_programs = R7_DOCS / "prepared-programs/acceptance"
        target_programs = self.root / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/prepared-programs/acceptance"
        shutil.copytree(source_programs, target_programs, dirs_exist_ok=True)

    def _install_r7_job(self):
        baseline = json.loads((R7_DOCS / "BASELINE.json").read_text())
        job = baseline["job"]
        previous_r6_job_id = self.base.snapshot["job"]["id"]
        self.older_r6_job = self.store.job(previous_r6_job_id)
        with self.store.connect() as con:
            self.older_r6_checkpoints = [(row["name"], row["body"]) for row in con.execute(
                "SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (previous_r6_job_id,))]
        attempt = self.root / "factory/jobs" / job["id"] / "attempt-1"
        generated = attempt / "context/generated-0"
        generated.mkdir(parents=True, exist_ok=True)
        # The nine original R6 delivered program bytes are the manifest's before-state.
        original_programs = R6_DOCS / "candidate-attempt-1-not-frozen/acceptance"
        for src in original_programs.iterdir():
            if src.is_file():
                target = generated / "acceptance" / src.name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, target)
        candidate = attempt / "candidate-0/template.json"
        candidate.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(R6_DOCS / "candidate-attempt-1-not-frozen/template.json", candidate)
        with self.store.connect(True) as con:
            con.execute("DELETE FROM checkpoint WHERE job_id=?", (job["id"],))
            con.execute("INSERT OR IGNORE INTO batch VALUES(?,?,?,?)",
                        (job["batch_id"], "failed", canonical(job["snapshot"]["config"]), job["created_at"]))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (job["id"], job["batch_id"], job["kind"], job["state"], job["stage"], job["attempt"],
                         None, None, canonical(job["snapshot"]), job["error"], job["created_at"], job["updated_at"]))
            for checkpoint in baseline["checkpoints"]:
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)",
                            (checkpoint["job_id"], checkpoint["name"], checkpoint["body"]))

    def _advance_budget_baseline(self):
        current = json.loads((R7_DOCS / "baseline-state.json").read_text())
        preserved = current["ledger_preservation"]
        added_calls = preserved["tf_budget_reservation"]["new_rows"]
        added_repairs = preserved["tf_budget_repair"]["new_rows"]
        r6_amendment = preserved["tf_budget_amendment"]["new_rows"][0]
        with self.store.connect(True) as con:
            con.execute("DELETE FROM tf_budget_amendment_binding WHERE amendment_id IN (SELECT id FROM tf_budget_amendment WHERE version=3)")
            con.execute("DELETE FROM tf_budget_amendment WHERE version=3")
            columns = list(r6_amendment)
            con.execute("INSERT INTO tf_budget_amendment(" + ",".join(columns) + ") VALUES(" +
                        ",".join("?" for _ in columns) + ")", tuple(r6_amendment[c] for c in columns))
            for table, rows in (("tf_budget_reservation", added_calls), ("tf_budget_repair", added_repairs)):
                for extra in rows:
                    columns = list(extra)
                    con.execute("INSERT INTO " + table + "(" + ",".join(columns) + ") VALUES(" +
                                ",".join("?" for _ in columns) + ")", tuple(extra[c] for c in columns))

    def _resume_request(self):
        return build_r7_product_resume_request(self.store, self.prepared_request,
                                               self.amendment["id"], idempotency_key=RESUME_KEY)

    def _counts(self):
        with self.store.connect() as con:
            return (con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0],
                    con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0],
                    con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')",
                                (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0])

    def test_registration_is_pending_and_first_queue_is_one_inherited_deadline_successor(self):
        old_job_id = self.prepared_request["binding"]["job_id"]
        before_job = self.store.job(old_job_id)
        with self.store.connect() as con:
            before_checkpoints = [(row["name"], row["body"]) for row in con.execute(
                "SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (old_job_id,))]
            before_grants = [tuple(row) for row in con.execute(
                "SELECT id,status,consumed_reservation_id FROM tf_protocol_retry_grant ORDER BY id")]
            before_retries = [tuple(row) for row in con.execute(
                "SELECT id,retry_scope,stage,retry,status FROM tf_budget_reservation WHERE campaign_id=? AND retry IS NOT NULL ORDER BY id",
                (G1_AMENDMENT_CAMPAIGN,))]
        self.assertEqual((self.amendment["version"], self.amendment["old_repair_limit"],
                          self.amendment["new_repair_limit"], self.amendment["window_seconds"]), (4, 6, 7, 0))
        self.assertIsNone(self.amendment["activated_at"])
        self.assertIsNone(self.amendment["new_deadline"])
        self.assertEqual(self._counts(), (71, 6, 0))
        result = self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(result["schema"], "atlas.product-resume-result.v3")
        self.assertFalse(result["replayed"])
        self.assertEqual(result["effective_deadline"], G1_R7_OLD_DEADLINE)
        old_after = self.store.job(old_job_id)
        successor = self.store.job(result["successor_job_id"])
        self.assertEqual((old_after["state"], old_after["attempt"], old_after["error"], old_after["snapshot"]),
                         (before_job["state"], before_job["attempt"], before_job["error"], before_job["snapshot"]))
        self.assertEqual(successor["state"], "queued")
        self.assertEqual(successor["snapshot"]["config"]["repair_attempts"], 0)
        self.assertEqual(successor["snapshot"]["cognitive_repair"]["prepared_revision"]["schema"],
                         "atlas.failed-plan-revision.v3")
        self.assertEqual(self.store.batch(successor["batch_id"])["state"], "paused")
        parent_batch_id = self.base.snapshot["report"]["batch"]["id"]
        self.assertEqual(self.store.batch(parent_batch_id)["state"], "paused")
        with self.store.connect() as con:
            self.assertEqual([(row["name"], row["body"]) for row in con.execute(
                "SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (old_job_id,))], before_checkpoints)
            self.assertEqual([tuple(row) for row in con.execute(
                "SELECT id,status,consumed_reservation_id FROM tf_protocol_retry_grant ORDER BY id")], before_grants)
            self.assertEqual([tuple(row) for row in con.execute(
                "SELECT id,retry_scope,stage,retry,status FROM tf_budget_reservation WHERE campaign_id=? AND retry IS NOT NULL ORDER BY id",
                (G1_AMENDMENT_CAMPAIGN,))], before_retries)
        self.assertEqual(self.store.job(self.older_r6_job["id"]), self.older_r6_job)
        with self.store.connect() as con:
            self.assertEqual([(row["name"], row["body"]) for row in con.execute(
                "SELECT name,body FROM checkpoint WHERE job_id=? ORDER BY name", (self.older_r6_job["id"],))],
                self.older_r6_checkpoints)
        self.assertEqual(self._counts(), (71, 7, 0))
        replay = self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertTrue(replay["replayed"])
        self.assertEqual(replay["successor_job_id"], result["successor_job_id"])
        self.assertEqual(replay["effective_deadline"], G1_R7_OLD_DEADLINE)
        from template_factory.budget import BudgetLedger
        ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.clock[0])
        later = ledger.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN,
                               stage="post-r7-replay-proof")
        ledger.mark_started(later["id"])
        ledger.finish(later["id"], "completed", outcome="temporary integration fixture")
        replay_after_counts_change = self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertTrue(replay_after_counts_change["replayed"])
        self.assertEqual(replay_after_counts_change["successor_job_id"], result["successor_job_id"])
        self.assertEqual(replay_after_counts_change["effective_deadline"], G1_R7_OLD_DEADLINE)
        self.assertEqual(self._counts(), (72, 7, 0))

    def test_expired_window_rejects_without_activation_or_queue(self):
        self.clock[0] = G1_R7_OLD_DEADLINE
        with self.assertRaises(FactoryError):
            self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(self._counts(), (71, 6, 0))
        row = next(x for x in self.amendments.list() if x["id"] == self.amendment["id"])
        self.assertIsNone(row["activated_at"])
        self.assertIsNone(row["new_deadline"])

    def test_unknown_schema_and_different_idempotency_key_are_rejected(self):
        unknown = dict(self.request, schema="atlas.product-resume.v99")
        with self.assertRaises(FactoryError):
            self.recovery.resume_product(G1_AMENDMENT_PLAN, unknown)
        unknown_authorization = dict(self.authorization, schema="atlas.g1-bounded-revision-authorization.v99")
        with self.assertRaises(FactoryError) as caught:
            self.amendments.register(unknown_authorization)
        self.assertEqual(caught.exception.code, "budget_amendment_invalid")
        self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        conflict = dict(self.request, idempotency_key=RESUME_KEY + "-different")
        with self.assertRaises(FactoryError):
            self.recovery.resume_product(G1_AMENDMENT_PLAN, conflict)
        self.assertEqual(self._counts(), (71, 7, 0))

    def test_queue_and_receipt_failures_roll_back_v4_and_successor(self):
        from template_factory.cognition import queue_repair as real_queue

        def inject_queue_failure(*args, **kwargs):
            real_queue(*args, **kwargs)
            raise sqlite3.IntegrityError("injected R7 queue failure")

        with self.store.connect() as con:
            jobs_before = {row[0] for row in con.execute("SELECT id FROM job")}
            batches_before = {row[0] for row in con.execute("SELECT id FROM batch")}
        with patch("template_factory.cognition.queue_repair", side_effect=inject_queue_failure):
            with self.assertRaisesRegex(sqlite3.IntegrityError, "injected R7 queue failure"):
                self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(self._counts(), (71, 6, 0))
        self.assertIsNone(next(row for row in self.amendments.list() if row["id"] == self.amendment["id"])["activated_at"])
        with self.store.connect() as con:
            self.assertEqual({row[0] for row in con.execute("SELECT id FROM job")}, jobs_before)
            self.assertEqual({row[0] for row in con.execute("SELECT id FROM batch")}, batches_before)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume").fetchone()[0], 0)

        with self.store.connect(True) as con:
            con.execute("CREATE TRIGGER reject_r7_receipt BEFORE INSERT ON tf_product_resume BEGIN SELECT RAISE(ABORT,'R7 receipt fault'); END")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "R7 receipt fault"):
            self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        with self.store.connect(True) as con:
            con.execute("DROP TRIGGER reject_r7_receipt")
        self.assertEqual(self._counts(), (71, 6, 0))
        self.assertIsNone(next(row for row in self.amendments.list() if row["id"] == self.amendment["id"])["activated_at"])

    def test_concurrent_identical_resume_creates_one_successor_and_repair(self):
        barrier = threading.Barrier(2)
        outcomes = []

        def worker():
            barrier.wait()
            try:
                outcomes.append(ProductRecoveryService(self.store, clock=lambda: self.clock[0])
                                .resume_product(G1_AMENDMENT_PLAN, deepcopy(self.request)))
            except Exception as error:
                outcomes.append(error)

        threads = [threading.Thread(target=worker) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(30)
        self.assertTrue(all(not thread.is_alive() for thread in threads))
        results = [item for item in outcomes if isinstance(item, dict)]
        self.assertEqual(len(results), 2, outcomes)
        self.assertEqual(len({item["successor_job_id"] for item in results}), 1)
        self.assertEqual(sum(not item["replayed"] for item in results), 1)
        self.assertEqual(self._counts(), (71, 7, 0))
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume").fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_job_supersession WHERE old_job_id=?",
                                         (self.prepared_request["binding"]["job_id"],)).fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
