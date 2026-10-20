"""Temporary-store integration for R6's real preparation and queue transaction."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from template_factory.budget import (
    BudgetAmendmentService, BudgetLedger, build_r6_authorization_request,
    G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT,
    G1_R6_FAILED_JOB, G1_R6_OLD_DEADLINE, G1_R6_PROTOCOL_RESERVATION_ID,
    G1_R6_WINDOW_SECONDS,
)
from template_factory.plan_revision import (
    R6_AUTHORIZATION_REF, R6_PROGRAM_PATHS, PreparedRevisionService,
    build_program_reuse_manifest,
)
from template_factory.product_recovery import ProductRecoveryService
from template_factory.store import FactoryError, canonical, digest

DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
ARCHIVE = DOCS / "g1-protocol-recovery-2026-10-19"
R6_DOCS = DOCS / "g1-r6-source-alignment-2026-10-20"
NOW = G1_R6_OLD_DEADLINE + 30
RESUME_KEY = "atlas-g1-r6-source-alignment-resume-test-v1"


class ProductRecoveryR6IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.base = r5_fixture.R5PreparedLinkTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.tearDown)
        self.store = self.base.store
        self.root = self.base.root
        self.clock = [NOW]
        self.snapshot = json.loads((ARCHIVE / "actual-structural-stop.json").read_text())
        self.ledger_history = json.loads((ARCHIVE / "actual-final-ledger-history.json").read_text())
        self._install_authorization_and_job()
        self._install_attempt4_checkpoints_and_files()
        self._install_real_budget_baseline()
        self.prepared_request = self._prepared_request()
        self.assertEqual(self.prepared_request, json.loads((R6_DOCS / "prepare-request.json").read_text()))
        self.prepared = PreparedRevisionService(self.store).prepare(G1_R6_FAILED_JOB, self.prepared_request)
        archived_prepared = json.loads((R6_DOCS / "prepare-response.json").read_text())
        self.assertEqual(self.prepared["request_digest"], archived_prepared["request_digest"])
        self.assertEqual(self.prepared["effective_plan_digest"], archived_prepared["effective_plan_digest"])
        self.amendment_request = build_r6_authorization_request(
            self.store, self.prepared_request,
            summary="One bounded source-alignment repair and one replacement G1 window.",
            reason="Exact prepared source-alignment revision and retained program manifest.")
        self.amendments = BudgetAmendmentService(self.store, clock=lambda: self.clock[0])
        self.amendment = self.amendments.register(self.amendment_request)
        self.request = self._resume_request()
        self.recovery = ProductRecoveryService(self.store, clock=lambda: self.clock[0])

    def _install_authorization_and_job(self):
        source = self.root / R6_AUTHORIZATION_REF
        source.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(R6_DOCS / "authorization/ATLAS_G1_R6_SOURCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt", source)
        shutil.copyfile(R6_DOCS / "authorization/approved-revision.json",
                        source.parent / "approved-revision.json")
        shutil.copyfile(R6_DOCS / "patch.json", source.parent.parent / "patch.json")
        job = self.snapshot["job"]
        parent = self.snapshot["report"]["batch"]
        at = "2026-10-20T00:00:00+00:00"
        with self.store.connect(True) as con:
            con.execute("INSERT OR IGNORE INTO batch VALUES(?,?,?,?)",
                        (job["batch_id"], "failed", canonical(job["snapshot"]["config"]), at))
            # The plan's currently paused batch is the R6 parent and is the
            # execution referenced by the fixed plan.
            con.execute("UPDATE batch SET state='paused' WHERE id=?", (parent["id"],))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (job["id"], job["batch_id"], job["kind"], job["state"], job["stage"],
                         job["attempt"], None, None, canonical(job["snapshot"]),
                         job["error"], at, at))

    def _install_attempt4_checkpoints_and_files(self):
        attempt_root = self.store.root / "jobs" / G1_R6_FAILED_JOB / "attempt-4"
        generated = attempt_root / "context/generated-0"
        raw = ARCHIVE / "actual-attempt-4"
        generated.mkdir(parents=True, exist_ok=True)
        with self.store.connect(True) as con:
            for item in self.snapshot["checkpoints"]:
                body = item["body"]
                body_text = body if isinstance(body, str) else canonical(body)
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)",
                            (item["job_id"], item["name"], body_text))
                if not item["name"].startswith("blueprint-code-0-"):
                    continue
                result = json.loads(body_text)["result"]
                target = generated / result["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(result["content"].encode("utf-8"))
                raw_input = raw / item["name"] / "input.json"
                if raw_input.is_file():
                    input_target = attempt_root / item["name"] / "input.json"
                    input_target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(raw_input, input_target)

    def _install_real_budget_baseline(self):
        with self.store.connect(True) as con:
            for table in ("tf_budget_reservation", "tf_budget_repair", "tf_budget_amendment",
                          "tf_budget_phase", "tf_protocol_retry_grant", "tf_protocol_retry_grant_use"):
                con.execute("DELETE FROM " + table)
            for table in ("tf_budget_reservation", "tf_budget_repair", "tf_budget_amendment",
                          "tf_budget_phase", "tf_protocol_retry_grant", "tf_protocol_retry_grant_use"):
                rows = self.ledger_history[table]
                for row in rows:
                    columns = list(row)
                    con.execute("INSERT INTO " + table + "(" + ",".join(columns) + ") VALUES(" +
                                ",".join("?" for _ in columns) + ")", tuple(row[key] for key in columns))
        BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.clock[0])

    def _prepared_request(self):
        checkpoints = {item["name"]: json.loads(item["body"]) for item in self.snapshot["checkpoints"]}
        job = self.snapshot["job"]
        snapshot = job["snapshot"]
        plan = checkpoints["blueprint-plan-0"]
        facts = checkpoints["blueprint-accepted-facts-view"]
        design = checkpoints[next(name for name in checkpoints if name.startswith("case-adaptation-prepared-"))]
        manifest = build_program_reuse_manifest(self.store)
        binding = {
            "job_id": G1_R6_FAILED_JOB, "attempt": 4, "snapshot_digest": digest(snapshot),
            "checkpoint_name": "blueprint-plan-0", "checkpoint_digest": plan["digest"],
            "plan_id": snapshot["v1"]["plan_id"], "plan_digest": snapshot["v1"]["plan_digest"],
            "product_id": snapshot["v1"]["product_id"], "scenario_id": snapshot["scenario"]["id"],
            "scenario_revision": snapshot["scenario"]["revision"],
            "case_basis_digest": snapshot["case_basis"]["basis_digest"],
            "facts_view_checkpoint_name": "blueprint-accepted-facts-view",
            "facts_view_checkpoint_digest": facts["digest"], "facts_view_digest": facts["result"]["view_digest"],
            "case_design_checkpoint_name": next(name for name in checkpoints if name.startswith("case-adaptation-prepared-")),
            "case_design_checkpoint_digest": design["digest"],
            "original_proposal_digest": plan["digest"],
        }
        return {
            "schema": "atlas.failed-plan-revision.v2", "binding": binding,
            "patch": json.loads((R6_DOCS / "patch.json").read_text()),
            "source_authorization": {"source_ref": R6_AUTHORIZATION_REF,
                                     "source_digest": "7c36e8048393bf7b3fd7eecc78c3af76e3189d462310d88955ce283dd4ce0168",
                                     "revision_ref": "docs/template-factory/g1-r6-source-alignment-2026-10-20/authorization/approved-revision.json",
                                     "revision_digest": digest(json.loads((R6_DOCS / "authorization/approved-revision.json").read_text()))},
            "program_reuse_manifest": manifest,
        }

    def _resume_request(self):
        old = self.store.job(G1_R6_FAILED_JOB)
        old_repair = old["snapshot"]["cognitive_repair"]
        artifact = next(item for item in self.store.artifacts() if item["id"] == r5_fixture.ARTIFACT_ID)
        repair = {
            "expected_digest": artifact["digest"],
            "note": "Apply the exact authorized source-alignment revision and reuse the verified attempt-4 program bytes.",
            "edit_paths": old_repair["edit_paths"], "repair_scope": self.prepared["cumulative_repair_scope"],
            "reuse_spec": False, "prepared_revision": self.prepared_request,
            "model": old["snapshot"]["config"]["model"],
            "language": old["snapshot"]["config"]["language"],
            "timeout": old["snapshot"]["config"]["timeout"],
        }
        return {"schema": "atlas.product-resume.v2", "old_job_id": G1_R6_FAILED_JOB,
                "artifact_id": artifact["id"], "expected_digest": artifact["digest"],
                "amendment_id": self.amendment["id"], "idempotency_key": RESUME_KEY,
                "repair": repair}

    def _ledger_counts(self):
        with self.store.connect() as con:
            return {
                "repairs": con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                        (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0],
                "calls": con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'",
                                     (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0],
                "active": con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')",
                                      (G1_AMENDMENT_CAMPAIGN,)).fetchone()[0],
            }

    def test_real_preparation_and_queue_commit_preserves_failed_attempt_and_replays(self):
        before_job = self.store.job(G1_R6_FAILED_JOB)
        before_checkpoints = {item["name"]: self.store.checkpoint(G1_R6_FAILED_JOB, item["name"])
                              for item in self.snapshot["checkpoints"]}
        self.assertEqual(self._ledger_counts(), {"repairs": 5, "calls": 64, "active": 0})
        self.assertIsNone(self.amendment["activated_at"])
        result = self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertFalse(result["replayed"])
        self.assertEqual(result["schema"], "atlas.product-resume-result.v2")
        self.assertEqual(result["effective_deadline"], result["activated_at"] + G1_R6_WINDOW_SECONDS)
        self.assertEqual(self._ledger_counts(), {"repairs": 6, "calls": 64, "active": 0})
        with self.store.connect() as con:
            grant = con.execute("SELECT status,consumed_reservation_id FROM tf_protocol_retry_grant WHERE id=?",
                                ("pgrant_f3595368c14d4b23b6ab536f6d198007",)).fetchone()
            self.assertEqual((grant["status"], grant["consumed_reservation_id"]),
                             ("consumed", G1_R6_PROTOCOL_RESERVATION_ID))
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_protocol_retry_grant").fetchone()[0], 1)
        old = self.store.job(G1_R6_FAILED_JOB)
        successor = self.store.job(result["successor_job_id"])
        self.assertEqual((old["state"], old["attempt"], old["error"], old["snapshot"]),
                         (before_job["state"], before_job["attempt"], before_job["error"], before_job["snapshot"]))
        self.assertEqual(successor["state"], "queued")
        self.assertEqual(successor["snapshot"]["config"]["repair_attempts"], 0)
        self.assertEqual(successor["snapshot"]["config"]["model"], before_job["snapshot"]["config"]["model"])
        successor_prepared = successor["snapshot"]["cognitive_repair"]["prepared_revision"]
        self.assertEqual(successor_prepared["request_digest"], self.prepared["request_digest"])
        self.assertEqual(successor_prepared["effective_plan_digest"], self.prepared["effective_plan_digest"])
        self.assertEqual(successor_prepared["prepared_program_reuse"], self.prepared["prepared_program_reuse"])
        self.assertEqual(self.store.batch(successor["batch_id"])["state"], "paused")
        self.assertEqual(self.store.batch(self.snapshot["report"]["batch"]["id"])["state"], "paused")
        self.assertEqual({name: self.store.checkpoint(G1_R6_FAILED_JOB, name) for name in before_checkpoints},
                         before_checkpoints)
        # A later ordinary completed session changes the baseline after first
        # commit; receipt replay must still resolve before the old baseline gate.
        later_ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN,
                                    clock=lambda: self.clock[0])
        later = later_ledger.reserve(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN,
                                     stage="post-r6-replay-proof")
        later_ledger.mark_started(later["id"])
        later_ledger.finish(later["id"], "completed", outcome="temporary integration fixture")
        replay = self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertTrue(replay["replayed"])
        self.assertEqual(replay["successor_job_id"], result["successor_job_id"])
        self.assertEqual(replay["effective_deadline"], result["effective_deadline"])
        self.assertEqual(self._ledger_counts(), {"repairs": 6, "calls": 65, "active": 0})

    def test_queue_failure_and_receipt_failure_rollback_window_repair_and_successor(self):
        def run_failure(fail_receipt=False):
            if fail_receipt:
                with self.store.connect(True) as con:
                    con.execute("CREATE TRIGGER reject_r6_receipt BEFORE INSERT ON tf_product_resume BEGIN SELECT RAISE(ABORT,'receipt fault'); END")
            self.assertEqual(self._ledger_counts(), {"repairs": 5, "calls": 64, "active": 0})
            with self.store.connect() as con:
                jobs_before = {row[0] for row in con.execute("SELECT id FROM job")}
                batches_before = {row[0] for row in con.execute("SELECT id FROM batch")}
            if fail_receipt:
                with self.assertRaisesRegex(sqlite3.IntegrityError, "receipt fault"):
                    self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
            else:
                from template_factory.cognition import queue_repair as real_queue
                def queue_then_fail(*args, **kwargs):
                    real_queue(*args, **kwargs)
                    raise sqlite3.IntegrityError("injected outbox/queue failure")
                with patch("template_factory.cognition.queue_repair", side_effect=queue_then_fail):
                    with self.assertRaisesRegex(sqlite3.IntegrityError, "injected outbox/queue failure"):
                        self.recovery.resume_product(G1_AMENDMENT_PLAN, self.request)
            self.assertEqual(self._ledger_counts(), {"repairs": 5, "calls": 64, "active": 0})
            self.assertEqual(self.store.job(G1_R6_FAILED_JOB)["state"], "failed")
            self.assertIsNone(self.amendments.list()[-1]["activated_at"])
            with self.store.connect() as con:
                self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume").fetchone()[0], 0)
                self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_job_supersession WHERE old_job_id=?",
                                             (G1_R6_FAILED_JOB,)).fetchone()[0], 0)
                self.assertEqual({row[0] for row in con.execute("SELECT id FROM job")}, jobs_before)
                self.assertEqual({row[0] for row in con.execute("SELECT id FROM batch")}, batches_before)
                if fail_receipt:
                    con.execute("DROP TRIGGER reject_r6_receipt")

        run_failure(False)
        run_failure(True)
        # The same prepared authorization is still available after both rollbacks.
        self.assertEqual(self._ledger_counts(), {"repairs": 5, "calls": 64, "active": 0})

    def test_concurrent_identical_resume_creates_one_successor_and_one_repair(self):
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
        self.assertEqual(self._ledger_counts(), {"repairs": 6, "calls": 64, "active": 0})
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume").fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_job_supersession WHERE old_job_id=?",
                                         (G1_R6_FAILED_JOB,)).fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
