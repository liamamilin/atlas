"""Temporary-database integration for the authorized prepared G1 R5 link."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import BudgetAmendmentService, BudgetLedger
from template_factory.pipeline import Pipeline
from template_factory.r5_execution import R5ExecutionService
from template_factory.store import FactoryStore, canonical, digest, now
from template_factory.v1_batches import BatchService, migrate as migrate_batches

PACK = Path(__file__).resolve().parents[1]
DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
PREP = DOCS / "g1-preparation-2026-10-19"
CONVERGENCE = DOCS / "g1-convergence-2026-10-19"
REPAIR = CONVERGENCE / "repair-4"
R5 = DOCS / "g1-r5-2026-10-19"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
CAMPAIGN = "atlas-v1-first-production-2026-10-19"
PRODUCT = "product-c42848f63251507bd9d911a5"
JOB_ID = "job_a53c47f3694047489c4f82cfc2e346be"
ARTIFACT_ID = "tpl_7f4c17e834c342e7b462e6bb8b6379e4"
ARTIFACT_JOB_ID = "job_d0d9d80dc9f64dd9890fc0b728bd9a5d"
FIXED_CLOCK = 1792408424.0


class StopAtArchitectureReview(Exception):
    """The fake CLI stops when the architecture pre-review sees its materials."""


class DesignReviewSpy:
    def __init__(self, expected_proposal_digest):
        self.expected_proposal_digest = expected_proposal_digest
        self.calls = []
        self.materials = None

    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        name = Path(directory).name
        payload = json.loads((Path(directory) / "input.json").read_text())
        self.calls.append((name, payload, prompt))
        if payload["proposal_digest"] != self.expected_proposal_digest:
            raise AssertionError("Pipeline did not send the prepared effective plan to design review")
        dimension = payload["review_dimensions"][0]
        if dimension == "architecture_contract":
            source = Path(directory) / "source"
            self.materials = {
                "case_design": json.loads((source / "CASE_DESIGN.json").read_text()),
                "case_policy": json.loads((source / "CASE_ADAPTATION_POLICY.json").read_text()),
            }
            raise StopAtArchitectureReview
        return {
            "summary": "Temporary static design-review fixture; no model/provider was called.",
            "checks": [{
                "dimension": dimension,
                "outcome": "passed",
                "files": ["DRAFT.md"],
                "reason": "Fixture response lets the real pipeline advance to architecture pre-review.",
            }],
            "suggestions": [],
        }

    def info(self):
        return {"kind": "test-spy", "provider_called": False}


class R5PreparedLinkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        shutil.copy(PACK / "mvp_apps_classified.json", self.pack / "mvp_apps_classified.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES('bookmark-manager','Bookmarks','书签','Save links','Links')")
        self.store = FactoryStore(self.root / "factory", self.pack)
        self._copy_authorization_inputs()
        self.job_fixture = json.loads((CONVERGENCE / "job-stop.json").read_text())
        self.report = json.loads((CONVERGENCE / "report-after-stop.json").read_text())
        self.plan = self.report["plan"]
        self.plan_checkpoint = json.loads((REPAIR / "blueprint-plan-1.json").read_text())
        self.adaptation_checkpoint = json.loads((REPAIR / "case-adaptation-aggregate-v1.json").read_text())
        self.request = json.loads((PREP / "prepare-revision-request.json").read_text())
        self.repair_request = json.loads((PREP / "formal-repair-request-NOT-EXECUTED.json").read_text())
        self.case_record = json.loads((REPAIR / "canonical-case-current.json").read_text())
        self._insert_parent_plan_and_failed_job()
        self._insert_archived_case_records()
        self._insert_frozen_artifact()
        self._insert_budget_baseline()

    def _copy_authorization_inputs(self):
        target_prep = self.root / "docs/template-factory/g1-preparation-2026-10-19"
        target_prep.mkdir(parents=True)
        for name in ("prepare-revision-request.json", "formal-repair-request-NOT-EXECUTED.json"):
            shutil.copy(PREP / name, target_prep / name)
        target_auth = self.root / "docs/template-factory/g1-r5-2026-10-19/authorization"
        target_auth.mkdir(parents=True)
        shutil.copy(R5 / "authorization/ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt",
                    target_auth / "ATLAS_G1_R5_EXECUTION_CODEX_INSTRUCTIONS.txt")

    def tearDown(self):
        self.temp.cleanup()

    def _insert_parent_plan_and_failed_job(self):
        snapshot = self.job_fixture["snapshot"]
        at = now()
        artifact_job = next(job for job in self.report["batch"]["jobs"] if job["id"] == ARTIFACT_JOB_ID)
        with self.store.connect(True) as con:
            # The running plan's parent is the archived paused V1 batch. The
            # superseded failed job belongs to its separate earlier batch.
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (
                self.report["batch"]["id"], "paused", canonical(self.report["batch"]["config"]), at))
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (
                self.job_fixture["batch_id"], "failed", canonical(snapshot["config"]), at))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                ARTIFACT_JOB_ID, artifact_job["batch_id"], artifact_job["kind"], artifact_job["state"],
                artifact_job["stage"], artifact_job["attempt"], None, None,
                canonical(artifact_job["snapshot"]), None, at, at))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                JOB_ID, self.job_fixture["batch_id"], "blueprint-production", "failed",
                self.job_fixture["stage"], self.job_fixture["attempt"], None, None,
                canonical(snapshot), canonical(self.job_fixture["error"]), at, at))
            con.execute("INSERT INTO v1_plan VALUES(?,?,?,?)", (
                self.plan["id"], self.plan["digest"], canonical(self.plan), at))
            con.execute("INSERT INTO v1_execution VALUES(?,?,?,?,?)", (
                PLAN_ID, self.plan["digest"], "atlas-g1-initial-plan-v1",
                self.report["batch"]["id"], at))
            for name, record in (("blueprint-plan-1", self.plan_checkpoint),
                                 ("case-adaptation-aggregate-v1", self.adaptation_checkpoint)):
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (JOB_ID, name, canonical(record)))

    def _insert_archived_case_records(self):
        """Load immutable archived rows into this test DB, without source refetch."""
        record = self.case_record
        with self.store.connect(True) as con:
            for snapshot in record["source_snapshots"]:
                selected = {key: snapshot[key] for key in (
                    "repository", "repo_id", "commit_sha", "strategy_version", "files",
                    "file_manifest_digest", "license_files", "archive_sha256", "excluded_paths") if key in snapshot}
                source_digest = digest(selected)
                con.execute("INSERT INTO source_snapshot VALUES(?,?,?,?,?,?,?,?)", (
                    snapshot["snapshot_id"], snapshot["repository"], snapshot.get("repo_id"),
                    snapshot["commit_sha"], snapshot["strategy_version"], source_digest,
                    canonical(snapshot), snapshot["collected_at"]))
            con.execute("INSERT INTO case_app VALUES(?,?,?,?)", (
                record["app_id"], "bookmark-manager-r5-fixture", canonical({
                    "app_id": record["app_id"], "legacy_slug": "bookmark-manager-r5-fixture",
                    "name": "Archived bookmark manager case fixture", "aliases": [],
                    "catalog_status": "research_discovered", "source_identity": {
                        "kind": "repository", "repository": record["source_snapshots"][0]["repository"]},
                    "created_at": record["created_at"]}), record["created_at"]))
            body = {key: record[key] for key in (
                "case_id", "revision", "app_id", "snapshot_ids", "research",
                "research_input_digest", "evidence_digest", "created_at", "created_task_id", "digest")}
            con.execute("INSERT INTO case_revision VALUES(?,?,?,?,?,?)", (
                record["case_id"], record["revision"], record["app_id"],
                record["digest"], canonical(body), record["created_at"]))
            for item in record["observations"]:
                observation = {key: value for key, value in item.items() if key != "reviews"}
                con.execute("INSERT INTO evidence_observation VALUES(?,?,?,?,?,?)", (
                    item["evidence_id"], record["case_id"], record["revision"], item["kind"],
                    item["digest"], canonical(observation)))
                for review in item.get("reviews", []):
                    con.execute("INSERT INTO evidence_review VALUES(?,?,?,?,?,?,?,?,?)", (
                        review["review_id"], item["evidence_id"], record["case_id"],
                        record["revision"], review["evidence_digest"], review["outcome"],
                        review["reviewer"], review["reviewer_kind"], review["created_at"]))
            for link in record["scenario_links"]:
                con.execute("INSERT INTO scenario_case_link VALUES(?,?,?,?,?)", (
                    link["scenario_id"], link["scenario_revision"], record["case_id"],
                    record["revision"], canonical(link)))
        from template_factory.cases import CaseLibrary
        library = CaseLibrary(self.store, initialize=False)
        self.assertEqual(len(library.list_cases(scenario_id=self.case_record["scenario_links"][0]["scenario_id"])), 1)
        self.assertEqual(len(library.get_case(record["case_id"], record["revision"])["observations"]), 29)
        library.require_admissible(self.job_fixture["snapshot"]["case_basis"])

    def _insert_frozen_artifact(self):
        source = DOCS / "v1-2026-10-19/g1-real-sample/template-8d9229d3895b"
        bundle = self.store.root / "jobs" / JOB_ID / "attempt-1" / "bundle"
        bundle.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, bundle)
        manifest = json.loads((bundle / "manifest.json").read_text())
        plan = json.loads((bundle / "plan.json").read_text())
        provenance = json.loads((bundle / "provenance.json").read_text())
        body = deepcopy(next(item for item in self.report["artifacts"] if item["id"] == ARTIFACT_ID))
        body.update({
            "bundle_path": str(bundle.relative_to(self.store.root)),
            "manifest": manifest, "plan": plan, "provenance": provenance,
        })
        with self.store.connect(True) as con:
            con.execute("INSERT INTO artifact VALUES(?,?,?,?,?,?,?)", (
                ARTIFACT_ID, ARTIFACT_JOB_ID, body["digest"], body["level"], body["state"], canonical(body), now()))

    def _insert_budget_baseline(self):
        BudgetLedger(self.store, campaign_id=CAMPAIGN, clock=lambda: FIXED_CLOCK)
        amendment = json.loads((R5 / "amendments-before.json").read_text())["amendments"][0]
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)", (
                CAMPAIGN, "__campaign_segment__", "G1", 1792389754.633465, 1792418554.633465))
            con.executemany(
                "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created) VALUES(?,?,?,?,?,?,?)",
                [(f"historic-{i}", CAMPAIGN, PRODUCT, "G1", "production", "completed", FIXED_CLOCK)
                 for i in range(52)],
            )
            con.executemany("INSERT INTO tf_budget_repair VALUES(?,?,?,?)", [
                (CAMPAIGN, PRODUCT, f"prior-repair-{i}", FIXED_CLOCK) for i in range(4)])
            con.execute("INSERT INTO tf_budget_amendment VALUES(" + ",".join("?" for _ in amendment) + ")",
                        tuple(amendment.values()))

    def test_formal_authorization_queues_and_consumes_exact_prepared_v1_successor(self):
        from template_factory.cases import CaseLibrary

        prepared = json.loads((PREP / "prepare-revision-response.json").read_text())
        scope = self.repair_request["repair_scope"]
        edit_paths = self.repair_request["edit_paths"]
        library = CaseLibrary(self.store, initialize=False)
        basis = library.evidence_basis(
            self.job_fixture["snapshot"]["case_basis"]["case_refs"],
            self.job_fixture["snapshot"]["scenario"]["id"],
            self.job_fixture["snapshot"]["scenario"]["revision"],
        )
        self.assertEqual(len(basis["evidence_ids"]), 29)
        self.assertEqual(basis["basis_digest"], self.job_fixture["snapshot"]["case_basis"]["basis_digest"])

        authorization = json.loads((R5 / "authorization-request.json").read_text())
        amendment = BudgetAmendmentService(
            self.store, campaign_id=CAMPAIGN, clock=lambda: FIXED_CLOCK
        ).register(authorization)
        request = {
            "amendment_id": amendment["id"],
            "idempotency_key": "atlas-g1-r5-prepared-2026-10-19-v1",
            "artifact_id": ARTIFACT_ID,
            "repair": self.repair_request,
        }
        service = R5ExecutionService(self.store, clock=lambda: FIXED_CLOCK)
        result = service.queue(PLAN_ID, request)
        self.assertFalse(result["replayed"])
        # Model-independent fixture for a later, already charged CLI session:
        # replay must resolve before rechecking the original 52/4 registration basis.
        ledger = BudgetLedger(self.store, campaign_id=CAMPAIGN, clock=lambda: FIXED_CLOCK)
        later_call = ledger.reserve(PRODUCT, "G1", job_id="later-call-fixture",
                                    stage="later-independent-review", plan_id=PLAN_ID)
        ledger.mark_started(later_call["id"])
        ledger.finish(later_call["id"], "completed", outcome="test fixture only")
        replay = service.queue(PLAN_ID, deepcopy(request))
        self.assertTrue(replay["replayed"])
        self.assertEqual((replay["batch_id"], replay["job_id"]), (result["batch_id"], result["job_id"]))

        old = self.store.job(JOB_ID)
        successor = self.store.job(result["job_id"])
        self.assertEqual(old["state"], "failed")
        self.assertEqual(successor["snapshot"]["case_basis"], self.job_fixture["snapshot"]["case_basis"])
        repair = successor["snapshot"]["cognitive_repair"]
        self.assertEqual(repair["repair_scope"], scope)
        self.assertEqual(repair["edit_paths"], edit_paths)
        self.assertEqual(repair["prepared_revision"]["request_digest"], prepared["request_digest"])
        self.assertEqual(repair["prepared_revision"]["effective_plan_digest"], prepared["effective_plan_digest"])
        self.assertEqual(repair["prepared_revision"]["case_design"], prepared["case_design"])
        self.assertEqual(repair["prepared_revision"]["case_adaptation_input"], prepared["case_adaptation_input"])

        with self.store.connect() as con:
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            amendment_rows = con.execute("SELECT activated_at,new_deadline FROM tf_budget_amendment WHERE version=2").fetchone()
        self.assertEqual(repairs, 5)
        self.assertEqual(amendment_rows["new_deadline"], 1792437223.754534)
        self.assertIsNotNone(amendment_rows["activated_at"])
        self.assertEqual(self.store.batch(result["batch_id"])["state"], "paused")
        with self.store.connect() as con:
            relation = con.execute("SELECT * FROM tf_job_supersession WHERE old_job_id=?", (JOB_ID,)).fetchone()
        self.assertEqual(relation["successor_job_id"], result["job_id"])
        self.assertEqual(relation["old_state"], "failed")
        self.assertEqual(relation["old_error"], canonical(self.job_fixture["error"]))
        self.assertIsNone(self.store.claim("r5-link-test", "production"))

        BatchService(self.store).action(PLAN_ID, "resume")
        claimed = self.store.claim("r5-link-test", "production")
        self.assertEqual(claimed["id"], result["job_id"])
        self.assertEqual(claimed["snapshot"]["v1"]["plan_id"], PLAN_ID)
        spy = DesignReviewSpy(prepared["effective_plan_digest"])
        pipeline = Pipeline(self.store, cli=spy)
        with self.assertRaises(StopAtArchitectureReview):
            pipeline.run(claimed)

        self.assertEqual([call[1]["review_dimensions"][0] for call in spy.calls], [
            "scenario_scope", "product_completeness", "architecture_contract"])
        self.assertIn("case_design", spy.materials)
        self.assertIn("case_policy", spy.materials)
        self.assertEqual(spy.materials["case_design"], prepared["case_design"])
        self.assertEqual(spy.materials["case_policy"]["scenario_id"], self.job_fixture["snapshot"]["scenario"]["id"])
        self.assertEqual(spy.materials["case_policy"]["product_id"], PRODUCT)
        self.assertFalse(any(name.startswith(("blueprint-generate", "blueprint-research", "case-adaptation"))
                             for name, _, _ in spy.calls))
        self.assertEqual(len(spy.calls), 3)
        # The fake design-review boundary itself does not consume CLI sessions;
        # exactly one synthetic later completed session was charged above.
        self.assertEqual(BudgetLedger(self.store, campaign_id=CAMPAIGN, clock=lambda: FIXED_CLOCK).snapshot()["cli_sessions_used"], 53)
        self.assertEqual(self.store.job(JOB_ID)["state"], "failed")
        self.assertEqual(self.store.job(ARTIFACT_JOB_ID)["state"], "completed")
        self.assertEqual(self.store.job(result["job_id"])["state"], "failed")
        with self.store.connect() as con:
            final_repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
        self.assertEqual(final_repairs, 5)


    def test_queue_transaction_rolls_back_activation_repair_and_successor_on_failure(self):
        authorization = json.loads((R5 / "authorization-request.json").read_text())
        amendment = BudgetAmendmentService(
            self.store, campaign_id=CAMPAIGN, clock=lambda: FIXED_CLOCK
        ).register(authorization)
        request = {
            "amendment_id": amendment["id"],
            "idempotency_key": "atlas-g1-r5-prepared-2026-10-19-v1",
            "artifact_id": ARTIFACT_ID,
            "repair": self.repair_request,
        }
        service = R5ExecutionService(self.store, clock=lambda: FIXED_CLOCK)
        from template_factory.cognition import queue_repair as real_queue_repair
        from template_factory.store import FactoryError

        def queue_then_abort(*args, **kwargs):
            real_queue_repair(*args, **kwargs)
            raise FactoryError("injected post-queue failure", "test_injected", 409)

        with mock.patch("template_factory.cognition.queue_repair", side_effect=queue_then_abort):
            with self.assertRaisesRegex(FactoryError, "injected post-queue failure"):
                service.queue(PLAN_ID, request)
        with self.store.connect() as con:
            r5 = con.execute("SELECT activated_at,new_deadline FROM tf_budget_amendment WHERE id=?", (amendment["id"],)).fetchone()
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            existing_batches = {self.job_fixture["batch_id"], self.report["batch"]["id"]}
            child_batches = con.execute("SELECT COUNT(*) FROM batch WHERE id NOT IN (?,?)", tuple(sorted(existing_batches))).fetchone()[0]
            jobs = con.execute("SELECT COUNT(*) FROM job").fetchone()[0]
            executions = con.execute("SELECT COUNT(*) FROM tf_g1_r5_execution").fetchone()[0]
            supersessions = con.execute("SELECT COUNT(*) FROM tf_job_supersession").fetchone()[0]
        self.assertIsNone(r5["activated_at"])
        self.assertEqual(r5["new_deadline"], 1792437223.754534)
        self.assertEqual(repairs, 4)
        self.assertEqual(child_batches, 0)
        self.assertEqual(jobs, 2)
        self.assertEqual(executions, 0)
        self.assertEqual(supersessions, 0)


if __name__ == "__main__":
    unittest.main()
