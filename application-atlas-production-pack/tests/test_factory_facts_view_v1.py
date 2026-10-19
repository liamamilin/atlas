"""Accepted case facts cannot be laundered through narrative research summaries."""
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.cases import CaseLibrary
from template_factory.cognition import produce, research_context, research_from_accepted_facts
from template_factory.store import FactoryError, FactoryStore, canonical, digest
from template_factory.v1_catalog import publish
from template_factory.artifacts import tree_manifest
from template_factory.blueprints import validate_blueprint

PACK = Path(__file__).resolve().parents[1]
SAMPLE = Path(__file__).resolve().parents[2] / "docs/template-factory/blueprints/bookmark-personal"


class FactoryAcceptedFactsViewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES(?,?,?,?,?)", ("task-management-application", "Task manager", "任务管理", "manage tasks", "Task workflows"))
        (self.pack / "applications").mkdir()
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.library = CaseLibrary(self.store)
        self.scenario = self.store.save_scenario({
            "leaf": "task-management-application", "name": "Complete tasks", "audience": "Individual",
            "objective": "Complete a task", "workflow": ["Create task", "Complete task"],
            "acceptance": ["Task remains completed"], "status": "ready",
        })
        snapshot_root = self.store.root / "snapshots" / "a1b2c3d4"
        snapshot_root.mkdir(parents=True)
        source = snapshot_root / "src/main.py"
        source.parent.mkdir()
        source.write_text("def complete_task():\n    return True\n", encoding="utf-8")
        license_path = snapshot_root / "LICENSE"
        license_path.write_text("MIT\n", encoding="utf-8")
        files = {name: hashlib.sha256((snapshot_root / name).read_bytes()).hexdigest() for name in ("src/main.py", "LICENSE")}
        self.snapshot = {
            "repository": "https://github.com/example/project", "repo_id": "github:1234",
            "commit_sha": "a" * 40, "collected_at": "2026-10-19T10:00:00Z",
            "strategy_version": "archive-v1", "local_root": str(snapshot_root),
            "files": files, "license_files": ["LICENSE"],
            "license": {"spdx_id_supplement": "MIT", "supplement_source": "test", "supplement_collected_at": "2026-10-19T10:00:00Z", "notice_hashes": {"LICENSE": files["LICENSE"]}},
        }
        result = self.library.commit_research({
            "app_id": "todoist", "case_id": "case:facts-view", "source_snapshots": [self.snapshot],
            "research": {
                "summary": "Rejected B claims the operation silently sends every task to a server.",
                "scope": "Task lifecycle", "unknowns": ["Actual process restart has not been observed."], "input_digest": "fixture", "task_id": "research-fixture",
            },
            "observations": [
                {"evidence_id": "ev-accepted", "kind": "code_observation",
                 "statement": "The pinned function returns success after completing one task.",
                 "location": {"commit_sha": "a" * 40, "path": "src/main.py", "file_digest": files["src/main.py"], "symbol": "complete_task"}},
                {"evidence_id": "ev-rejected", "kind": "documentation",
                 "statement": "Rejected B claims every task is secretly uploaded.",
                 "location": {"url": "https://example.invalid/docs", "material_version": "v1", "content_digest": "b" * 64}},
            ],
            "scenario_links": [{"scenario_id": self.scenario["id"], "scenario_revision": self.scenario["revision"],
                                "reason": "Covers the task workflow", "workflow_support": ["complete"],
                                "adopted_scope": ["task completion"], "exclusions": [],
                                "evidence_ids": ["ev-accepted", "ev-rejected"]}],
        }, "facts-view-fixture")
        self.case = result["case"]
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-accepted", "accepted", "reviewer", "independent_agent")
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "rejected", "reviewer", "independent_agent")
        self.basis = self.library.evidence_basis([{"case_id": self.case["case_id"], "revision": 1}], self.scenario["id"], self.scenario["revision"])

    def tearDown(self):
        self.temp.cleanup()

    def test_rejected_narrative_is_audit_only_and_cannot_enter_generation_context(self):
        raw = {
            "sources": [{"id": "S02", "name": "ev-accepted", "url": "https://github.com/example/project/blob/" + "a" * 40 + "/src/main.py",
                         "version": "a" * 40, "facts": "accepted source fact", "license": "MIT", "reuse": "accepted"},
                        {"id": "S03", "name": "ev-rejected", "url": "https://example.invalid/docs",
                         "version": "v1", "facts": "Rejected B", "license": "unknown", "reuse": "rejected"}],
            "summary": self.case["research"]["summary"], "gaps": ["Rejected B: false upload assertion"],
        }
        view = self.library.accepted_facts_view(self.basis, digest(raw))
        derived = research_from_accepted_facts(raw, view)
        context = research_context(derived)
        self.assertIn("ev-accepted", context)
        self.assertIn("The pinned function returns success", context)
        self.assertNotIn("Rejected B", context)
        self.assertNotIn("secretly uploads", context)
        self.assertNotIn("ev-rejected", context)
        self.assertIn("Unverified case limitation", context)
        self.assertIn("Actual process restart has not been observed.", context)
        self.assertIn("Rejected B", self.case["research"]["summary"])
        self.assertEqual(view["accepted_evidence_ids"], ["ev-accepted"])
        self.assertEqual(view["basis_digest"], self.basis["basis_digest"])
        self.assertEqual(self.library.validate_facts_view(view, self.basis), view)

    def test_legacy_mixed_checkpoints_block_but_all_accepted_are_labeled_legacy(self):
        with self.assertRaises(FactoryError) as rejected:
            self.library.legacy_facts_marker(self.basis)
        self.assertEqual(rejected.exception.code, "case_facts_view_required")
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "accepted", "reviewer-2", "independent_agent")
        marker = self.library.legacy_facts_marker(self.basis)
        self.assertEqual(marker["status"], "legacy_all_accepted")
        self.assertEqual(marker["policy"], "legacy-checkpoint-all-canonical-observations-accepted-v1")
        self.assertEqual(self.library.validate_facts_view(marker, self.basis), marker)

    def test_view_tamper_or_later_review_revocation_invalidates_publication(self):
        # Accept B as well so that revoking it later does not invalidate the required core code observation.
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "accepted", "reviewer-2", "independent_agent")
        view = self.library.accepted_facts_view(self.basis, "c" * 64)
        tampered = json.loads(json.dumps(view))
        tampered["facts"][0]["statement"] = "rewritten fact"
        tampered["view_digest"] = digest({key: value for key, value in tampered.items() if key != "view_digest"})
        with self.assertRaises(FactoryError):
            self.library.validate_facts_view(tampered, self.basis)

        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "rejected", "reviewer-3", "independent_agent")
        spec = {"case_basis": self.basis, "case_facts_view": view, "case_design": [
            {"disposition": "adopted", "evidence_ids": ["ev-accepted"]},
        ]}
        row = {"id": "artifact-fixture", "digest": "artifact-digest"}
        body = {"bundle_path": "unused", "provenance": {"case_basis": self.basis}}
        with self.assertRaises(FactoryError) as blocked:
            with patch("template_factory.api.controlled_path", return_value=self.root), \
                 patch("template_factory.blueprints.verify_frozen", return_value=spec), \
                 patch("template_factory.blueprint_runtime.validate_runner_manifest"):
                publish(self.store, None, row, body, {"expected_digest": "artifact-digest", "action": "publish"}, "test")
        self.assertEqual(blocked.exception.code, "case_facts_view_invalid")

    def test_frozen_package_requires_view_digest_and_exact_input_mirror(self):
        source = self.root / "blueprint"
        shutil.copytree(SAMPLE, source)
        spec_path = source / "template.json"
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        spec["factory_policy"] = "atlas.factory-v1.1"
        spec["scenario"] = self.scenario
        spec["case_basis"] = self.basis
        spec["case_design"] = []
        view = self.library.accepted_facts_view(self.basis, "d" * 64)
        spec["case_facts_view"] = view
        spec_path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
        (source / "inputs/scenario.json").write_text(json.dumps(spec["scenario"]), encoding="utf-8")
        (source / "inputs/case-basis.json").write_text(json.dumps(self.basis), encoding="utf-8")
        (source / "inputs/accepted-case-facts.json").write_text(json.dumps(view), encoding="utf-8")

        def refresh_inventory():
            inventory = tree_manifest(source)
            inventory.pop("integrity.json")
            (source / "integrity.json").write_text(json.dumps({
                "template_version": spec["version"], "sha256": inventory,
            }), encoding="utf-8")

        refresh_inventory()
        validate_blueprint(source)
        tampered = json.loads((source / "inputs/accepted-case-facts.json").read_text(encoding="utf-8"))
        tampered["facts"][0]["statement"] = "different mirror body"
        (source / "inputs/accepted-case-facts.json").write_text(json.dumps(tampered), encoding="utf-8")
        refresh_inventory()
        with self.assertRaises(FactoryError) as caught:
            validate_blueprint(source)
        self.assertEqual(caught.exception.code, "case_facts_view_invalid")

        for malformed in (["not-an-observation"], [{"evidence_id": None}], []):
            with self.subTest(facts=malformed):
                invalid_view = {**view, "facts": malformed}
                invalid_view["view_digest"] = digest({key: value for key, value in invalid_view.items() if key != "view_digest"})
                spec["case_facts_view"] = invalid_view
                spec_path.write_text(json.dumps(spec), encoding="utf-8")
                (source / "inputs/accepted-case-facts.json").write_text(json.dumps(invalid_view), encoding="utf-8")
                refresh_inventory()
                with self.assertRaises(FactoryError) as invalid:
                    validate_blueprint(source)
                self.assertEqual(invalid.exception.code, "case_facts_view_invalid")

    def _producer_fixture(self, *, repair=None):
        job_id = "job-resume-fixture"
        raw_research = {
            "sources": [{"id": "S02", "name": "ev-accepted", "url": "https://example.invalid/source",
                         "version": "a" * 40, "facts": "accepted observation", "license": "unknown", "reuse": "accepted"}],
            "summary": "Old raw summary repeats rejected B's claim about secret uploads.", "gaps": [],
        }
        with self.store.connect(True) as con:
            con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (
                job_id, "blueprint-research", canonical({"result": raw_research, "digest": digest(raw_research)}),
            ))
        if repair:
            previous = self.store.root / "artifacts/previous"
            (previous / "source").mkdir(parents=True)
            repair["bundle_path"] = "artifacts/previous"
        snapshot = {
            "config": {"repair_attempts": 0, "language": "en", "model": "fixture/model"},
            "leaf": {"slug": "task-management-application", "fingerprint": "f" * 64, "content": "Leaf"},
            "scenario": self.scenario,
            "case_basis": self.basis,
            "v1": {"campaign_id": "campaign-fixture", "product_id": "product-fixture", "segment": "T01"},
        }
        if repair:
            snapshot["cognitive_repair"] = repair
        attempt = self.root / ("attempt-" + job_id)
        attempt.mkdir()
        pipeline = SimpleNamespace(store=self.store)
        job = {"id": job_id, "snapshot": snapshot}

        def checkpoint(name, create):
            saved = self.store.checkpoint(job_id, name)
            if saved is not None:
                return saved["result"]
            if name == "blueprint-plan-0":
                raise RuntimeError("stopped at next plan boundary")
            return create()

        return pipeline, job, attempt, checkpoint

    def test_real_produce_resume_blocks_old_adaptation_even_without_plan_checkpoint(self):
        pipeline, job, attempt, checkpoint = self._producer_fixture()
        old_adaptation = {"choices": [{
            "evidence_ids": [], "disposition": "new_design", "capability": "New behavior",
            "reason": "Old checkpoint accepted without a factual reference",
        }]}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (
                job["id"], "case-adaptation", canonical({"result": old_adaptation, "digest": digest(old_adaptation)}),
            ))
        calls = []
        with self.assertRaises(FactoryError) as blocked:
            produce(pipeline, job, attempt, lambda *args, **kwargs: calls.append(args[0]), lambda *args: None, checkpoint)
        self.assertEqual(blocked.exception.code, "case_facts_view_required")
        self.assertEqual(calls, [])
        self.assertIsNone(self.store.checkpoint(job["id"], "blueprint-accepted-facts-view"))
        stored = self.store.checkpoint(job["id"], "case-adaptation")
        self.assertEqual(stored["digest"], digest(old_adaptation))
        with self.store.connect() as con:
            self.assertIsNone(con.execute("SELECT 1 FROM checkpoint WHERE job_id=? AND name LIKE 'blueprint-plan-%'", (job["id"],)).fetchone())

    def test_real_produce_repair_rejects_predecessor_with_newly_rejected_fact(self):
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "accepted", "reviewer-2", "independent_agent")
        prior_view = self.library.accepted_facts_view(self.basis, "e" * 64)
        previous_spec = {"case_basis": self.basis, "case_facts_view": prior_view}
        self.library.record_evidence_review(self.case["case_id"], 1, "ev-rejected", "rejected", "reviewer-3", "independent_agent")
        repair = {"id": "artifact-previous", "digest": "previous-digest", "note": "repair",
                  "acceptances": [], "edit_paths": [], "reuse_spec": True}
        pipeline, job, attempt, checkpoint = self._producer_fixture(repair=repair)
        calls = []

        def agent(name, prompt, payload, source=None, **kwargs):
            calls.append(name)
            return {"choices": [{"evidence_ids": ["ev-accepted"], "disposition": "adopted",
                                 "capability": "Complete tasks", "reason": "Supported by accepted code"}]}

        previous = self.store.root / "artifacts/previous"
        with patch("template_factory.api.controlled_path", return_value=previous), \
             patch("template_factory.cognition.verify_frozen", return_value=previous_spec):
            with self.assertRaises(FactoryError) as blocked:
                produce(pipeline, job, attempt, agent, lambda *args: None, checkpoint)
        self.assertEqual(blocked.exception.code, "case_facts_view_invalid")
        self.assertEqual(calls, ["case-adaptation"])
        self.assertFalse((attempt / "context/previous").exists())


if __name__ == "__main__":
    unittest.main()
