"""Transactional contract for the explicitly scoped G1 paused-job recovery."""
from pathlib import Path
import sqlite3
import json
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.budget import (  # noqa: E402
    BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN,
    G1_AMENDMENT_OLD_DEADLINE, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT,
    G1_AUTHORIZATION_SOURCE_DIGEST,
)
from template_factory.product_recovery import ProductRecoveryService  # noqa: E402
from template_factory.store import FactoryError, FactoryStore, canonical, digest  # noqa: E402
from template_factory.v1_batches import BatchService, migrate  # noqa: E402
from template_factory.v1_api import dispatch_v1  # noqa: E402

PINNED_BUNDLE = (Path(__file__).resolve().parents[2]
                 / "docs/template-factory/v1-2026-10-19/g1-real-sample/template-8d9229d3895b")
PINNED_ARTIFACT_ID = "tpl_7f4c17e834c342e7b462e6bb8b6379e4"
PINNED_ARTIFACT_DIGEST = "8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9"
PINNED_OLD_JOB_ID = "job_4f30d0f41ce94a2cbd16ae7996fb27ab"


class ProductRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        (self.pack / "atlas").mkdir(parents=True)
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug TEXT,name TEXT,name_zh TEXT,defining_core TEXT,overview TEXT)")
            con.execute("INSERT INTO leaf VALUES(?,?,?,?,?)", ("bookmark-manager", "Bookmark", "书签", "URLs", "Save links"))
        self.store = FactoryStore(self.root / "state", self.pack)
        self.at = [1_792_418_000.0]
        self.ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.at[0])
        self.amendments = BudgetAmendmentService(self.store, clock=lambda: self.at[0])
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", 1_792_400_000.0, G1_AMENDMENT_OLD_DEADLINE))
            for index in range(2):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"old-{index}", self.at[0]))
            for index in range(42):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"old-reservation-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, "G1", "production", "completed", self.at[0] + index, "production"))
        migrate(self.store)
        self.case_basis = {"basis_digest": "e" * 64, "case_refs": []}
        self.scenario = {"id": "scn_test", "revision": 2}
        self.plan = {"id": G1_AMENDMENT_PLAN, "campaign_id": G1_AMENDMENT_CAMPAIGN, "segment": "G1",
                     "seeds": [{"product_id": G1_AMENDMENT_PRODUCT, "scenario": self.scenario,
                                "case_basis": self.case_basis, "runtime_sample": False}]}
        self.plan["digest"] = digest(self.plan)
        self.old_job = PINNED_OLD_JOB_ID
        self.parent_batch = "bat_" + "1" * 32
        self.artifact = {"id": "tpl_" + "1" * 32, "digest": "d" * 64,
                         "provenance": {"v1": {"campaign_id": G1_AMENDMENT_CAMPAIGN,
                                                "plan_id": G1_AMENDMENT_PLAN,
                                                "product_id": G1_AMENDMENT_PRODUCT},
                                        "scenario": self.scenario, "case_basis": self.case_basis}}
        self.old_snapshot = {"leaf": {"slug": "bookmark-manager"}, "config": {}, "v1": {"campaign_id": G1_AMENDMENT_CAMPAIGN,
                                    "plan_id": G1_AMENDMENT_PLAN,
                                    "product_id": G1_AMENDMENT_PRODUCT, "segment": "G1"},
                             "scenario": self.scenario, "case_basis": self.case_basis}
        self.checkpoint = {"basis": "retained checkpoint"}
        self.checkpoint_digest = digest(self.checkpoint)
        with self.store.connect(True) as con:
            con.execute("INSERT INTO v1_plan VALUES(?,?,?,?)",
                        (self.plan["id"], self.plan["digest"], canonical(self.plan), "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (self.parent_batch, "paused", "{}", "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO v1_execution VALUES(?,?,?,?,?)",
                        (self.plan["id"], self.plan["digest"], "g1-idempotency", self.parent_batch, "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (self.old_job, self.parent_batch, "blueprint-production", "paused_budget", "blueprint-spec-review-0-runtime_protocol-v1", 1,
                         "late-worker-token", 9999999999.0, canonical(self.old_snapshot), "budget exceeded",
                         "2026-10-19T00:00:00Z", "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (self.old_job, "completed-research", canonical(self.checkpoint)))
        self.amendment = self.amendments.register({
            "product_id": G1_AMENDMENT_PRODUCT, "plan_id": G1_AMENDMENT_PLAN,
            "source_ref": "ATLAS_G1_CONVERGENCE_CODEX_INSTRUCTIONS.txt",
            "source_digest": G1_AUTHORIZATION_SOURCE_DIGEST, "summary": "Authorized single G1 continuation",
            "reason": "Supersede the over-narrow paused request with the aggregate repair scope.",
            "idempotency_key": "amendment-test",
        })
        self.request = {"old_job_id": self.old_job, "artifact_id": self.artifact["id"],
                        "expected_digest": self.artifact["digest"], "checkpoint_name": "completed-research",
                        "checkpoint_digest": self.checkpoint_digest, "amendment_id": self.amendment["id"],
                        "idempotency_key": "resume-test", "repair": {"expected_digest": self.artifact["digest"],
                        "note": "Bounded aggregate repair", "edit_paths": ["acceptance/p0_library.py"]}}
        self._prepare_real_frozen_candidate()

    def tearDown(self):
        self.temp.cleanup()

    def _queue(self, store, artifact, request, *, con, parent_state_override, ledger):
        ledger.record_repair(G1_AMENDMENT_PRODUCT, "successor-repair", con=con, plan_id=G1_AMENDMENT_PLAN)
        batch_id, job_id = "bat_" + "2" * 32, "job_" + "2" * 32
        snapshot = {"leaf": {}, "v1": self.old_snapshot["v1"]}
        con.execute("INSERT INTO batch VALUES(?,?,?,?)", (batch_id, parent_state_override, "{}", "2026-10-19T00:00:01Z"))
        con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (job_id, batch_id, "blueprint-production", "queued", "blueprint-generate", 1,
                     None, None, canonical(snapshot), None, "2026-10-19T00:00:01Z", "2026-10-19T00:00:01Z"))
        return {"batch_id": batch_id, "job_id": job_id, "created": True}

    def _artifacts(self):
        return [self.artifact]

    def _prepare_real_frozen_candidate(self):
        bundle_path = self.store.root / "jobs" / self.old_job / "attempt-1" / "bundle"
        bundle_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(PINNED_BUNDLE, bundle_path, dirs_exist_ok=True)
        provenance = json.loads((bundle_path / "provenance.json").read_text())
        scenario = provenance["scenario"]
        self.case_basis = provenance["case_basis"]
        provenance["v1"] = {"campaign_id": G1_AMENDMENT_CAMPAIGN,
                            "plan_id": G1_AMENDMENT_PLAN,
                            "product_id": G1_AMENDMENT_PRODUCT}
        self.artifact = {"id": PINNED_ARTIFACT_ID, "digest": PINNED_ARTIFACT_DIGEST,
                         "artifact_type": "product-blueprint",
                         "job_id": self.old_job, "acceptances": [],
                         "bundle_path": str(bundle_path.relative_to(self.store.root)),
                         "manifest": json.loads((bundle_path / "manifest.json").read_text()),
                         "plan": json.loads((bundle_path / "plan.json").read_text()),
                         "provenance": provenance}
        self.old_snapshot.update({"scenario": scenario, "case_basis": self.case_basis,
                                  "cognitive_repair": {"id": PINNED_ARTIFACT_ID,
                                                        "digest": PINNED_ARTIFACT_DIGEST}})
        self.plan["seeds"][0].update({"scenario": scenario, "case_basis": self.case_basis})
        self.plan["digest"] = digest({key: value for key, value in self.plan.items() if key != "digest"})
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(self.old_snapshot), self.old_job))
            con.execute("UPDATE v1_plan SET digest=?,body=? WHERE id=?",
                        (self.plan["digest"], canonical(self.plan), self.plan["id"]))
            con.execute("UPDATE v1_execution SET plan_digest=? WHERE plan_id=?",
                        (self.plan["digest"], self.plan["id"]))
        edit_paths = ["acceptance/p0_library.py", "acceptance/p0_organize.py",
                      "acceptance/p0_find_open.py", "acceptance/p0_recovery.py", "acceptance/README.md"]
        authorized_scope = json.loads((Path(__file__).resolve().parents[2]
            / "docs/template-factory/g1-convergence-2026-10-19/repair/aggregate-repair-request.json").read_text())["repair_scope"]
        self.request["repair"] = {"expected_digest": self.artifact["digest"], "note": "Bounded aggregate repair",
                                   "edit_paths": edit_paths, "reuse_spec": False,
                                   "repair_scope": authorized_scope}
        self.request.update({"artifact_id": self.artifact["id"], "expected_digest": self.artifact["digest"],
                             "repair": {**self.request["repair"], "model": "fixture/model"}})
        return self.artifact

    def test_supersession_activation_and_queue_resume_commit_as_one_idempotent_operation(self):
        with patch.object(self.store, "artifacts", self._artifacts), patch(
                "template_factory.cognition.queue_repair", side_effect=self._queue):
            result = ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
            replay = ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertFalse(result["replayed"])
        self.assertTrue(replay["replayed"])
        self.assertEqual(result["successor_job_id"], replay["successor_job_id"])
        old = self.store.job(self.old_job)
        successor = self.store.job(result["successor_job_id"])
        self.assertEqual(old["state"], "cancelled")
        with self.store.connect() as con:
            self.assertIsNone(con.execute("SELECT token FROM job WHERE id=?", (self.old_job,)).fetchone()[0])
        self.assertEqual(successor["snapshot"]["formal_resume_checkpoint"], {
            "old_job_id": self.old_job, "name": "completed-research", "digest": self.checkpoint_digest})
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT state FROM batch WHERE id=?", (self.parent_batch,)).fetchone()[0], "running")
            self.assertEqual(con.execute("SELECT successor_job_id FROM tf_job_supersession WHERE old_job_id=?", (self.old_job,)).fetchone()[0], successor["id"])
            supersession = con.execute("SELECT old_state,old_error FROM tf_job_supersession WHERE old_job_id=?", (self.old_job,)).fetchone()
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0], 3)
        self.assertEqual(tuple(supersession), ("paused_budget", "budget exceeded"))
        self.assertIsNotNone(self.amendments.list()[0]["activated_at"])
        with patch("template_factory.v1_api.CaseLibrary"):
            budget_response, status = dispatch_v1("GET", f"jobs/{successor['id']}/effective-budget", "", {}, self.store)
        self.assertEqual(status, 200)
        self.assertEqual(budget_response["schema"], "atlas.g1-effective-budget.v1")
        self.assertEqual(budget_response["binding"], {"campaign_id": G1_AMENDMENT_CAMPAIGN,
            "plan_id": G1_AMENDMENT_PLAN, "product_id": G1_AMENDMENT_PRODUCT,
            "segment": "G1", "job_id": successor["id"]})
        self.assertEqual(budget_response["effective_deadline"], self.amendments.list()[0]["new_deadline"])
        with patch("template_factory.v1_reporting.enrich_report", side_effect=lambda _store, report: report):
            report = BatchService(self.store).report(G1_AMENDMENT_PLAN)
        self.assertEqual(report["counts"]["queue_total"], 1)
        self.assertEqual(report["counts"]["queue_completed"], 0)
        self.assertEqual(report["counts"]["superseded_history_jobs"], 1)
        self.assertEqual(report["batch"]["state"], "running")

    def test_queue_failure_rolls_back_activation_and_preserves_paused_job(self):
        def fail(*_args, **_kwargs):
            raise FactoryError("injected queue failure", "queue_failed", 409)
        with patch.object(self.store, "artifacts", self._artifacts), patch(
                "template_factory.cognition.queue_repair", side_effect=fail):
            with self.assertRaises(FactoryError):
                ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(self.store.job(self.old_job)["state"], "paused_budget")
        self.assertIsNone(self.amendments.list()[0]["activated_at"])
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT state FROM batch WHERE id=?", (self.parent_batch,)).fetchone()[0], "paused")
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_job_supersession").fetchone()[0], 0)

    def test_real_queue_repair_atomically_supersedes_old_job_and_charges_one_repair(self):
        self._prepare_real_frozen_candidate()
        with patch.object(self.store, "artifacts", self._artifacts):
            result = ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(self.store.job(self.old_job)["state"], "cancelled")
        self.assertEqual(self.store.job(self.old_job)["error"], "budget exceeded")
        successor = self.store.job(result["successor_job_id"])
        self.assertEqual(successor["kind"], "blueprint-production")
        self.assertEqual(successor["state"], "queued")
        self.assertEqual(successor["snapshot"]["cognitive_repair"]["digest"], self.artifact["digest"])
        self.assertEqual(successor["snapshot"]["formal_resume_checkpoint"]["digest"], self.checkpoint_digest)
        with self.store.connect() as con:
            counts = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                 (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            old = con.execute("SELECT old_state,old_error,successor_job_id FROM tf_job_supersession WHERE old_job_id=?",
                              (self.old_job,)).fetchone()
            self.assertEqual(con.execute("SELECT state FROM batch WHERE id=?", (self.parent_batch,)).fetchone()[0], "running")
        self.assertEqual(counts, 3)
        self.assertEqual(tuple(old), ("paused_budget", "budget exceeded", successor["id"]))
        self.assertEqual(self.amendments.list()[0]["activated_at"] is not None, True)

    def test_real_recovery_rejects_case_basis_drift_before_activation(self):
        self._prepare_real_frozen_candidate()
        changed = self.store.job(self.old_job)["snapshot"]
        changed["case_basis"] = {"basis_digest": "f" * 64, "case_refs": []}
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(changed), self.old_job))
        with patch.object(self.store, "artifacts", self._artifacts), self.assertRaises(FactoryError) as caught:
            ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(caught.exception.code, "resume_case_basis_mismatch")
        self.assertEqual(self.store.job(self.old_job)["state"], "paused_budget")
        self.assertIsNone(self.amendments.list()[0]["activated_at"])

    def test_recovery_rejects_unbounded_or_stale_repair_scope(self):
        for mutate in (
            lambda repair: repair.update(reuse_spec=True),
            lambda repair: repair.update(repair_scope={**repair["repair_scope"], "version": "old"}),
            lambda repair: repair.pop("repair_scope"),
        ):
            request = json.loads(json.dumps(self.request))
            mutate(request["repair"])
            with patch.object(self.store, "artifacts", self._artifacts), self.assertRaises(FactoryError):
                ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, request)
            self.assertEqual(self.store.job(self.old_job)["state"], "paused_budget")
            self.assertIsNone(self.amendments.list()[0]["activated_at"])

    def test_recovery_rejects_another_paused_job_or_artifact_revision(self):
        changed = json.loads(json.dumps(self.request))
        changed["old_job_id"] = "job_" + "9" * 32
        with self.assertRaises(FactoryError) as caught:
            ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, changed)
        self.assertEqual(caught.exception.code, "resume_baseline_mismatch")
        changed = json.loads(json.dumps(self.request))
        changed["artifact_id"] = "tpl_" + "9" * 32
        with self.assertRaises(FactoryError) as caught:
            ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, changed)
        self.assertEqual(caught.exception.code, "resume_baseline_mismatch")
        snapshot = self.store.job(self.old_job)["snapshot"]
        snapshot["cognitive_repair"]["digest"] = "f" * 64
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(snapshot), self.old_job))
        with patch.object(self.store, "artifacts", self._artifacts), self.assertRaises(FactoryError) as caught:
            ProductRecoveryService(self.store).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(caught.exception.code, "resume_old_job_invalid")
        self.assertIsNone(self.amendments.list()[0]["activated_at"])

    def test_expired_supplemental_window_cannot_supersede_or_charge(self):
        active = self.amendments.activate(self.amendment["id"])
        with self.store.connect() as con:
            before_repairs = con.execute("SELECT count(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                         (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
        self.at[0] = active["new_deadline"] + 1
        with patch.object(self.store, "artifacts", self._artifacts), self.assertRaises(FactoryError) as caught:
            ProductRecoveryService(self.store, clock=lambda: self.at[0]).resume_product(G1_AMENDMENT_PLAN, self.request)
        self.assertEqual(caught.exception.code, "budget_deadline")
        self.assertEqual(self.store.job(self.old_job)["state"], "paused_budget")
        with self.store.connect() as con:
            after_repairs = con.execute("SELECT count(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                                        (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT)).fetchone()[0]
            self.assertEqual(con.execute("SELECT state FROM batch WHERE id=?", (self.parent_batch,)).fetchone()[0], "paused")
            self.assertEqual(con.execute("SELECT count(*) FROM tf_job_supersession").fetchone()[0], 0)
        self.assertEqual(after_repairs, before_repairs)

    def test_t08_budget_reads_use_its_original_base_deadline(self):
        amendment = BudgetAmendmentService(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN).activate(self.amendment["id"])
        ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN)
        with self.store.connect(True) as con:
            plan_row = con.execute("SELECT body FROM v1_plan WHERE id=?", (G1_AMENDMENT_PLAN,)).fetchone()
            plan = json.loads(plan_row[0])
            plan["segment"] = "T08"
            plan["digest"] = digest({key: value for key, value in plan.items() if key != "digest"})
            con.execute("UPDATE v1_plan SET body=? WHERE id=?", (canonical(plan), G1_AMENDMENT_PLAN))
            con.execute("UPDATE v1_plan SET digest=? WHERE id=?", (plan["digest"], G1_AMENDMENT_PLAN))
            con.execute("UPDATE v1_execution SET plan_digest=? WHERE plan_id=?", (plan["digest"], G1_AMENDMENT_PLAN))
            job_row = con.execute("SELECT snapshot FROM job WHERE id=?", (self.old_job,)).fetchone()
            snapshot = json.loads(job_row[0])
            snapshot["v1"]["segment"] = "T08"
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(snapshot), self.old_job))
        t08_deadline = ledger.begin_segment("T08")
        with patch("template_factory.v1_api.CaseLibrary"):
            by_plan, status = dispatch_v1("GET", f"plans/{G1_AMENDMENT_PLAN}/budget", f"product_id={G1_AMENDMENT_PRODUCT}", {}, self.store)
        self.assertEqual(status, 200)
        self.assertEqual(by_plan["effective_deadline"], t08_deadline)
        self.assertEqual(by_plan["deadline_source"], "base")
        self.assertIsNone(by_plan["amendment_id"])
        with patch("template_factory.v1_api.CaseLibrary"):
            by_job, status = dispatch_v1("GET", f"jobs/{self.old_job}/effective-budget", "", {}, self.store)
        self.assertEqual(status, 200)
        self.assertEqual(by_job["effective_deadline"], t08_deadline)
        self.assertEqual(by_job["binding"]["segment"], "T08")
        self.assertNotEqual(by_job["effective_deadline"], amendment["new_deadline"])


if __name__ == "__main__":
    unittest.main()
