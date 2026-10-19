"""Cross-module V1 plan/publication/recovery contracts; no provider calls."""
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.store import FactoryError, FactoryStore, digest
from template_factory.v1_batches import BatchService
from template_factory.budget import BudgetLedger
from template_factory.api import dispatch
from template_factory.v1_catalog import review_status

PACK = Path(__file__).resolve().parents[1]


class FactoryV1Contracts(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES('bookmark-manager','Bookmarks','书签','Save links','Links')")
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.scene = self.store.save_scenario({"leaf": "bookmark-manager", "name": "Save and reopen", "audience": "Personal", "objective": "Save links and reopen", "workflow": ["save", "read"], "acceptance": ["Saved links remain"], "status": "ready"})
        self.service = BatchService(self.store)

    def tearDown(self):
        self.temp.cleanup()

    def preview(self, **extra):
        return self.service.preview({"scenario_ids": [self.scene["id"]], "model": "fake/model", **extra})

    def run_plan(self, plan, key="request-1"):
        return self.service.run(plan["id"], {"expected_plan_digest": plan["digest"], "idempotency_key": key})

    def test_preview_is_model_free_and_idempotent_execution_pins_inputs(self):
        with patch("template_factory.cli.CLI.run", side_effect=AssertionError("preview called model")):
            plan = self.preview()
            self.assertEqual(plan["seeds"][0]["next_stage"], "case-research")
            self.assertFalse(plan["seeds"][0]["template_input_ready"])
            first = self.run_plan(plan)
            replay = self.run_plan(plan)
        self.assertEqual(first["batch"]["id"], replay["batch"]["id"])
        self.assertEqual(len(replay["batch"]["jobs"]), 1)
        self.assertEqual(BudgetLedger(self.store, campaign_id=plan["campaign_id"]).snapshot()["cli_sessions_used"], 0)

    def test_stale_scenario_rejects_without_queue_or_ledger_call(self):
        plan = self.preview()
        self.store.save_scenario({**self.scene, "expected_revision": 1, "name": "Revised"}, self.scene["id"])
        with self.assertRaises(FactoryError) as caught:
            self.run_plan(plan)
        self.assertEqual(caught.exception.code, "stale_plan")
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM job").fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT count(*) FROM v1_execution").fetchone()[0], 0)

    def test_leaf_fingerprint_change_rejects_old_preview(self):
        plan = self.preview()
        (self.pack / "applications").mkdir()
        (self.pack / "applications/bookmark-manager.md").write_text("new immutable leaf input")
        with self.assertRaises(FactoryError) as caught:
            self.run_plan(plan)
        self.assertEqual(caught.exception.code, "stale_plan")

    def test_t08_requires_gate_and_prespecified_three_samples(self):
        with self.assertRaises(FactoryError) as caught:
            self.preview(segment="T08", runtime_sample_ids=[self.scene["id"]])
        self.assertEqual(caught.exception.code, "sample_scope_insufficient")
        scenes = [self.scene]
        for n in range(2):
            scenes.append(self.store.save_scenario({**self.scene, "name": f"Separate {n}", "status": "ready"}))
        plan = self.service.preview({"scenario_ids": [s["id"] for s in scenes], "runtime_sample_ids": [s["id"] for s in scenes], "model": "fake/model", "segment": "T08"})
        with self.assertRaises(FactoryError) as caught:
            self.run_plan(plan)
        self.assertEqual(caught.exception.code, "g1_required")

    def test_plan_digest_and_idempotency_key_conflicts(self):
        plan = self.preview()
        self.run_plan(plan)
        with self.assertRaises(FactoryError):
            self.run_plan(plan, "different-key")
        with self.assertRaises(FactoryError):
            self.service.run(plan["id"], {"expected_plan_digest": "0" * 64, "idempotency_key": "request-1"})

    def test_atomic_outbox_recovers_before_and_after_successor_queue(self):
        plan = self.preview()
        run = self.run_plan(plan)
        job = self.store.claim("host", "production")
        artifact_id = self.store.add_artifact(job["id"], job["token"], {
            "digest": "a" * 64, "artifact_type": "product-blueprint", "leaf": "bookmark-manager",
            "manifest": {"name": "fixture"}, "bundle_path": "missing-fixture-not-used",
            "provenance": {"scenario": self.scene, "model": "fake/model", "v1": job["snapshot"]["v1"]},
        })
        # Simulated process death immediately after artifact commit: queued intent
        # exists even though no create_acceptance call was made.
        with patch.object(self.store, "create_acceptance", side_effect=RuntimeError("crash before enqueue")):
            with self.assertRaises(RuntimeError):
                self.store.reconcile_outbox()
        self.store.reconcile_outbox()
        first = self.store.acceptance_jobs(artifact_id)
        self.assertEqual(len(first), 1)
        self.assertEqual(self.store.job(first[0]["id"])["batch_id"], run["batch"]["id"])
        # Replaying after queue commit but before ack must not duplicate review.
        with self.store.connect(True) as con:
            con.execute("UPDATE v1_outbox SET state='pending'")
        self.store.reconcile_outbox()
        self.assertEqual(len(self.store.acceptance_jobs(artifact_id)), 1)
        self.assertEqual(self.service.report(plan["id"])["quality_result"], "in_progress")

    def test_latest_review_request_cannot_fall_back_to_old_pass(self):
        plan = self.preview()
        self.run_plan(plan)
        job = self.store.claim("host", "production")
        aid = self.store.add_artifact(job["id"], job["token"], {"digest": "b" * 64, "artifact_type": "product-blueprint", "leaf": "bookmark-manager", "manifest": {"name": "fixture"}, "bundle_path": "unused", "provenance": {"scenario": self.scene, "model": "fake/model", "v1": job["snapshot"]["v1"]}})
        self.store.reconcile_outbox()
        review_job = self.store.claim("review", "verification")
        self.store.complete_acceptance(review_job["id"], review_job["token"], {"outcome": "passed", "scope": "fixture only"})
        with self.store.connect() as con:
            self.assertEqual(review_status(con, aid, "b" * 64), "passed")
        self.store.create_acceptance(aid, {"method": "cognitive-review", "model": "fake/model", "expected_digest": "b" * 64})
        with self.store.connect() as con:
            self.assertEqual(review_status(con, aid, "b" * 64), "unavailable")

    def test_global_production_limit_spans_batches_and_workers(self):
        for n in range(3):
            plan = self.preview(campaign_id=f"fixture-{n}")
            self.run_plan(plan, f"fixture-{n}")
        self.assertIsNotNone(self.store.claim("a", "production"))
        self.assertIsNotNone(self.store.claim("b", "production"))
        self.assertIsNone(self.store.claim("c", "production"))

    def test_api_legacy_catalog_and_v1_report_quality_do_not_claim_pass(self):
        apps, status = dispatch("GET", "/api/factory/v1/applications", store=self.store)
        self.assertEqual((status, len(apps)), (200, 33))
        plan = self.preview()
        report = self.service.report(plan["id"])
        self.assertEqual(report["quality_result"], "not_run")
        self.assertEqual(report["counts"]["published_products"], 0)
        self.assertEqual(report["runtime_sampling_gate"], "not_passed")


if __name__ == "__main__":
    unittest.main()
