"""Host-bounded preparation tests for the fixed failed G1 blueprint plan."""

from copy import deepcopy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.api import dispatch
from template_factory.cognition import validate_file_plan
from template_factory.contract_scope import validate_contract_coverage
from template_factory.store import FactoryError, FactoryStore, canonical, digest, now

PACK = Path(__file__).resolve().parents[1]
DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
PREP = DOCS / "g1-preparation-2026-10-19"
REPAIR = DOCS / "g1-convergence-2026-10-19/repair-4"
JOB_ID = "job_a53c47f3694047489c4f82cfc2e346be"


class PlanPreparationTests(unittest.TestCase):
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
        self.job_fixture = json.loads((DOCS / "g1-convergence-2026-10-19/job-stop.json").read_text())
        self.plan_checkpoint = json.loads((REPAIR / "blueprint-plan-1.json").read_text())
        self.adaptation_checkpoint = json.loads((REPAIR / "case-adaptation-aggregate-v1.json").read_text())
        self.fixed_plan = json.loads((DOCS / "g1-convergence-2026-10-19/report-after-stop.json").read_text())["plan"]
        self.request = json.loads((PREP / "prepare-revision-request.json").read_text())
        self.expected_response = json.loads((PREP / "prepare-revision-response.json").read_text())
        self._insert_pinned_state()

    def tearDown(self):
        self.temp.cleanup()

    def _insert_pinned_state(self):
        snapshot = self.job_fixture["snapshot"]
        with self.store.connect(True) as con:
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (
                self.job_fixture["batch_id"], "failed", canonical(snapshot["config"]), now()))
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (JOB_ID, self.job_fixture["batch_id"], "blueprint-production", "failed",
                 self.job_fixture["stage"], self.job_fixture["attempt"], None, None,
                 canonical(snapshot), canonical(self.job_fixture["error"]), now(), now()),
            )
            con.execute("INSERT INTO v1_plan VALUES(?,?,?,?)", (
                self.fixed_plan["id"], self.fixed_plan["digest"], canonical(self.fixed_plan), now()))
            for name, record in (("blueprint-plan-1", self.plan_checkpoint),
                                 ("case-adaptation-aggregate-v1", self.adaptation_checkpoint)):
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (JOB_ID, name, canonical(record)))

    def _counts(self):
        with self.store.connect() as con:
            names = [row[0] for row in con.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE 'tf_budget_%' OR name IN ('job','batch','checkpoint','event','artifact')) ORDER BY name")]
            return {name: con.execute(f'SELECT count(*) FROM "{name}"').fetchone()[0] for name in names}

    def _prepare(self, request=None):
        return dispatch("POST", "/api/factory/v1/jobs/" + JOB_ID + "/prepare-revision",
                        body=deepcopy(self.request if request is None else request), store=self.store)

    def test_exact_checked_in_request_prepares_without_queue_budget_or_worker_changes(self):
        before = self._counts()
        with patch("template_factory.worker.ensure_worker") as ensure_worker:
            result, status = self._prepare()
        self.assertEqual(status, 200)
        ensure_worker.assert_not_called()
        self.assertEqual(self._counts(), before)
        self.assertEqual(result, self.expected_response)
        self.assertEqual(result["state"], "prepared_not_queued")
        self.assertEqual(result["base_proposal_digest"], self.request["binding"]["checkpoint_digest"])

        base = self.plan_checkpoint["result"]
        effective = result["effective_plan"]
        changed = set()
        for field in base["spec"]:
            if base["spec"][field] != effective["spec"][field]:
                if field == "acceptance":
                    old_rows = {row["id"]: row for row in base["spec"][field]}
                    new_rows = {row["id"]: row for row in effective["spec"][field]}
                    for identity in old_rows:
                        for key in old_rows[identity]:
                            if old_rows[identity][key] != new_rows[identity][key]:
                                changed.add((field, identity, key))
                elif field == "contract_coverage":
                    changed.add((field, "error_contract"))
                    for key in set(base["spec"][field]) | set(effective["spec"][field]):
                        if key != "features" and base["spec"][field].get(key) != effective["spec"][field].get(key):
                            changed.add((field, key))
                    old_rows = {row["feature_id"]: row for row in base["spec"][field]["features"]}
                    new_rows = {row["feature_id"]: row for row in effective["spec"][field]["features"]}
                    for fid in old_rows:
                        if old_rows[fid] != new_rows[fid]:
                            self.assertEqual({k: v for k, v in old_rows[fid].items() if k != "error_branch_ids"},
                                             {k: v for k, v in new_rows[fid].items() if k != "error_branch_ids"})
                            changed.add((field, "features", fid, "error_branch_ids"))
                else:
                    changed.add((field,))
        self.assertEqual(changed, {
            ("acceptance", "A04", "goal"), ("acceptance", "A12", "goal"),
            ("architecture_markdown",), ("contract_coverage", "error_contract"),
            *(('contract_coverage', 'features', fid, 'error_branch_ids')
              for fid in ("F03", "F04", "F10")),
        })
        self.assertEqual(effective["spec"]["roles"], base["spec"]["roles"])
        self.assertEqual(effective["spec"]["phases"], base["spec"]["phases"])
        self.assertEqual(effective["spec"]["limits"], base["spec"]["limits"])
        self.assertEqual([row["id"] for row in effective["spec"]["features"]],
                         [row["id"] for row in base["spec"]["features"]])
        self.assertEqual([row["id"] for row in effective["spec"]["acceptance"]],
                         [row["id"] for row in base["spec"]["acceptance"]])

    def test_any_out_of_scope_patch_and_checkpoint_or_binding_drift_is_rejected(self):
        bad = deepcopy(self.request)
        bad["patch"]["spec_changes"][0]["path"] = ["acceptance", "A01", "goal"]
        with self.assertRaises(FactoryError):
            self._prepare(bad)
        bad = deepcopy(self.request)
        bad["patch"]["spec_changes"][0]["new"] += " extra"
        with self.assertRaises(FactoryError):
            self._prepare(bad)
        bad = deepcopy(self.request)
        bad["binding"]["checkpoint_digest"] = "0" * 64
        with self.assertRaises(FactoryError):
            self._prepare(bad)
        bad = deepcopy(self.request)
        bad["binding"]["case_design_checkpoint_digest"] = "0" * 64
        with self.assertRaises(FactoryError):
            self._prepare(bad)

        with self.store.connect(True) as con:
            altered = deepcopy(self.plan_checkpoint)
            altered["result"]["spec"]["title"] += " tampered"
            con.execute("UPDATE checkpoint SET body=? WHERE job_id=? AND name='blueprint-plan-1'",
                        (canonical(altered), JOB_ID))
        with self.assertRaises(FactoryError):
            self._prepare()

    def test_required_error_branches_and_all_references_are_host_validated(self):
        from template_factory.plan_revision import apply_bounded_patch
        result, design = apply_bounded_patch(self.plan_checkpoint["result"],
                                             self.adaptation_checkpoint["result"]["choices"],
                                             self.request["patch"])
        self.assertTrue(design)
        valid = result["spec"]
        self.assertIsNotNone(validate_contract_coverage(valid, required=True))
        self.assertTrue(validate_file_plan(result, allow_reuse=True, require_runtime=True))

        missing = deepcopy(result)
        missing["spec"]["contract_coverage"]["error_contract"]["branches"].pop()
        with self.assertRaises(FactoryError):
            validate_contract_coverage(missing["spec"], required=True)
        for mutation in (
            lambda branch: branch.update(code="invalid_name" if branch["code"] == "invalid_category" else "invalid_category"),
            lambda branch: branch.update(acceptance_ids=["A999"]),
            lambda branch: branch.update(feature_ids=["F999"]),
        ):
            bad = deepcopy(result)
            mutation(bad["spec"]["contract_coverage"]["error_contract"]["branches"][0])
            with self.assertRaises(FactoryError):
                validate_contract_coverage(bad["spec"], required=True)
        bad = deepcopy(result)
        organize = next(row for row in bad["file_plan"] if row["path"] == "acceptance/p0_organize.py")
        organize["error_branch_ids"].pop()
        with self.assertRaises(FactoryError):
            validate_file_plan(bad, allow_reuse=True, require_runtime=True)

    def test_prepared_queue_budget_refusal_rolls_back_all_temporary_state(self):
        """The real frozen baseline and exact prepared request still hit the ledger."""
        from template_factory.budget import BudgetLedger
        from template_factory.cognition import queue_repair
        from template_factory.v1_batches import migrate

        bundle_source = DOCS / "v1-2026-10-19/g1-real-sample/template-8d9229d3895b"
        bundle = self.store.root / "jobs" / JOB_ID / "attempt-1" / "bundle"
        bundle.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(bundle_source, bundle)
        manifest = json.loads((bundle / "manifest.json").read_text())
        plan = json.loads((bundle / "plan.json").read_text())
        provenance = json.loads((bundle / "provenance.json").read_text())
        artifact = {
            "id": self.job_fixture["snapshot"]["cognitive_repair"]["id"],
            "digest": self.request["expected_digest"] if "expected_digest" in self.request else "8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9",
            "artifact_type": "product-blueprint", "job_id": JOB_ID,
            "acceptances": self.job_fixture["snapshot"]["cognitive_repair"]["acceptances"],
            "bundle_path": str(bundle.relative_to(self.store.root)),
            "manifest": manifest, "plan": plan, "provenance": provenance,
        }
        request = json.loads((PREP / "formal-repair-request-NOT-EXECUTED.json").read_text())
        migrate(self.store)
        ledger = BudgetLedger(self.store, campaign_id="atlas-v1-first-production-2026-10-19")
        with self.store.connect(True) as con:
            con.executemany("INSERT INTO tf_budget_repair VALUES(?,?,?,?)", [
                ("atlas-v1-first-production-2026-10-19", "product-c42848f63251507bd9d911a5", "prior-" + str(i), now())
                for i in range(4)
            ])
            # Seed the already activated historical 2->4 amendment into this
            # isolated fixture. Do not register/activate any production budget.
            amendment = json.loads((PREP / "production-before.json").read_text())["budget"]["tf_budget_amendment"][0]
            con.execute("INSERT INTO tf_budget_amendment (" + ",".join(amendment) + ") VALUES (" + ",".join("?" for _ in amendment) + ")", tuple(amendment.values()))
        before = self._counts()
        with self.assertRaises(FactoryError) as caught:
            queue_repair(self.store, artifact, request, ledger=ledger)
        self.assertEqual(caught.exception.code, "budget_repair_limit", str(caught.exception))
        self.assertEqual(self._counts(), before)

    def test_prepared_producer_uses_effective_plan_without_generation_call(self):
        from template_factory.cognition import produce

        prepared, status = self._prepare()
        self.assertEqual(status, 200)
        bundle_source = DOCS / "v1-2026-10-19/g1-real-sample/template-8d9229d3895b"
        bundle = self.store.root / "jobs" / JOB_ID / "attempt-1" / "bundle"
        bundle.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(bundle_source, bundle)
        provenance = json.loads((bundle / "provenance.json").read_text())
        artifact_digest = "8d9229d3895be0cd1672ad28a2926549a2e5e6920b186ceeaef09c38c37803d9"
        previous_repair = {
            "id": "tpl_7f4c17e834c342e7b462e6bb8b6379e4",
            "digest": artifact_digest,
            "bundle_path": str(bundle.relative_to(self.store.root)),
            "note": "fixture only",
            "acceptances": [],
            "research": {"sources": [{"id": "S02", "name": "fixture", "url": "https://example.com", "version": "fixed", "facts": "fixture evidence", "license": "fixture", "reuse": "test only"}], "summary": "temporary test evidence", "gaps": []},
            "prepared_revision": prepared,
        }
        job = {
            "id": "job_prepared_consumer", "attempt": 2,
            "snapshot": {
                "config": {"language": "en", "model": "fake/provider", "repair_attempts": 0},
                "scenario": self.job_fixture["snapshot"]["scenario"],
                "leaf": self.job_fixture["snapshot"]["leaf"],
                "cognitive_repair": previous_repair,
            },
        }
        attempts = self.root / "consumer-attempt"
        attempts.mkdir()

        class PipelineStub:
            def __init__(self, store):
                self.store = store

        generation_stages = []
        review_seen_prepared_plan = []

        class StopAtDesignReview(Exception):
            pass

        def agent(stage, prompt, payload, context, **kwargs):
            if stage.startswith("blueprint-generate"):
                generation_stages.append(stage)
            if stage.startswith("blueprint-spec-review"):
                draft = (context / "DRAFT.md").read_text()
                review_seen_prepared_plan.append(prepared["effective_plan"]["spec"]["title"] in draft)
                raise StopAtDesignReview
            raise AssertionError(f"unexpected model call before independent review: {stage}")

        def checkpoint(_name, fn):
            return fn()

        with self.assertRaises(StopAtDesignReview):
            produce(PipelineStub(self.store), job, attempts, agent, lambda *_args: None, checkpoint)
        self.assertEqual(generation_stages, [])
        self.assertEqual(review_seen_prepared_plan, [True])
        for mutation in ("mixed_code", "missing_branch", "missing_file_reference"):
            corrupt_job = deepcopy(job)
            corrupt = corrupt_job["snapshot"]["cognitive_repair"]["prepared_revision"]
            plan = corrupt["effective_plan"]
            branches = plan["spec"]["contract_coverage"]["error_contract"]["branches"]
            if mutation == "mixed_code":
                branches[0]["code"] = "invalid_category"
            elif mutation == "missing_branch":
                branches.pop()
            else:
                next(r for r in plan["file_plan"] if r["path"] == "acceptance/p0_organize.py")["error_branch_ids"].pop()
            corrupt["effective_plan_digest"] = digest(plan)
            directory = self.root / mutation
            directory.mkdir()
            forbidden_agent = unittest.mock.Mock(side_effect=AssertionError("must stop before model pre-review"))
            with self.assertRaises(FactoryError) as caught:
                produce(PipelineStub(self.store), corrupt_job, directory, forbidden_agent, lambda *_args: None, checkpoint)
            self.assertEqual(caught.exception.code, "error_contract_invalid")
            forbidden_agent.assert_not_called()


if __name__ == "__main__":
    unittest.main()
