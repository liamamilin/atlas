"""Deterministic V1 context rebuilding and authenticated delivery recovery."""

import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from template_factory.artifacts import tree_manifest
from template_factory.cases import CaseLibrary
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, FactoryStore
from test_cognition import FakeCognitionCLI

PACK = Path(__file__).resolve().parents[1]
SAMPLE = Path(__file__).resolve().parents[2] / "docs/template-factory/blueprints/bookmark-personal"


class V1ContextRecoveryTests(unittest.TestCase):
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
        self.source = self.root / "sample"
        shutil.copytree(SAMPLE, self.source)
        self.scene = self.store.save_scenario({
            "leaf": "bookmark-manager", "name": "Save and reopen", "audience": "Personal",
            "objective": "Save links and reopen", "workflow": ["save", "read"],
            "acceptance": ["Saved links remain"], "status": "ready",
        })
        self.basis = self._create_canonical_basis()

    def tearDown(self):
        self.temp.cleanup()

    def _create_canonical_basis(self):
        library = CaseLibrary(self.store)
        snapshot_root = self.store.root / "source-snapshots" / "fixture"
        snapshot_root.mkdir(parents=True)
        code = snapshot_root / "src/main.py"
        code.parent.mkdir(parents=True)
        code.write_text("def save_bookmark():\n    return True\n", encoding="utf-8")
        license_path = snapshot_root / "LICENSE"
        license_path.write_text("MIT License fixture\n", encoding="utf-8")
        files = {"src/main.py": hashlib.sha256(code.read_bytes()).hexdigest(),
                 "LICENSE": hashlib.sha256(license_path.read_bytes()).hexdigest()}
        result = library.commit_research({
            "app_id": "todoist", "case_id": "case:context-recovery",
            "source_snapshots": [{
                "repository": "https://github.com/example/bookmarks", "repo_id": "github:context-recovery",
                "commit_sha": "a" * 40, "collected_at": "2026-10-19T10:00:00Z",
                "strategy_version": "archive-v1", "local_root": str(snapshot_root),
                "files": files, "license_files": ["LICENSE"],
                "license": {"spdx_id_supplement": "MIT", "supplement_source": "fixture metadata",
                            "supplement_collected_at": "2026-10-19T10:00:00Z", "notice_hashes": {"LICENSE": files["LICENSE"]}},
            }],
            "research": {"summary": "A pinned source records bookmark storage.", "scope": "save and reopen",
                         "unknowns": ["The fixture source was not run."], "input_digest": "fixture-input"},
            "observations": [{"evidence_id": "ev-context-save", "kind": "code_observation",
                              "statement": "save_bookmark returns success after saving.",
                              "location": {"commit_sha": "a" * 40, "path": "src/main.py",
                                           "file_digest": files["src/main.py"], "symbol": "save_bookmark"}}],
            "scenario_links": [{"scenario_id": self.scene["id"], "scenario_revision": self.scene["revision"],
                                "reason": "The observation supports the fixed workflow.", "workflow_support": ["save"],
                                "adopted_scope": ["save bookmark"], "exclusions": ["cloud sync"],
                                "evidence_ids": ["ev-context-save"]}],
        }, "context-recovery-case")["case"]
        library.record_evidence_review(result["case_id"], result["revision"], "ev-context-save", "accepted",
                                       "fixture-independent-reviewer", "independent_agent")
        return library.evidence_basis([{"case_id": result["case_id"], "revision": result["revision"]}],
                                      self.scene["id"], self.scene["revision"])

    def _queue_v1_job(self):
        batch = self.store.create_batch({
            "kind": "blueprint-production", "name": "V1 context recovery", "model": "fake/flash",
            "language": "en", "scenario_ids": [self.scene["id"]],
            "scenario_revisions": {self.scene["id"]: self.scene["revision"]},
        })
        with self.store.connect(True) as con:
            row = con.execute("SELECT id,snapshot FROM job WHERE batch_id=?", (batch["id"],)).fetchone()
            snapshot = json.loads(row["snapshot"])
            snapshot.update({"v1": {"campaign_id": "fixture-campaign", "product_id": "bookmark-manager",
                                    "segment": "G1", "plan_id": None}, "case_basis": self.basis})
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (json.dumps(snapshot), row["id"]))
        return row["id"]

    def _cli(self):
        fixture_path = self.source / "template.json"
        fixture = json.loads(fixture_path.read_text())
        for feature in fixture["features"]:
            feature["sources"] = ["S02"]
        fixture_path.write_text(json.dumps(fixture, ensure_ascii=False), encoding="utf-8")
        cli = FakeCognitionCLI(self.source)
        cli.record_generation_delivery = True
        def run(directory, prompt, model, timeout, cancelled, progress, **kwargs):
            if directory.name in {"case-adaptation", "case-adaptation-aggregate-v1"}:
                return {"choices": [{"evidence_ids": ["ev-context-save"], "disposition": "adopted",
                                     "capability": "Save a bookmark", "reason": "Supported by the fixed observation."}]}
            return original_run(directory, prompt, model, timeout, cancelled, progress)
        original_run = cli.run
        cli.run = run
        return cli

    def _aggregate_cli(self):
        from test_factory_spec_patch_v1 import WeakeningAggregateCLI
        cli = WeakeningAggregateCLI(self.source)
        cli.record_generation_delivery = True
        cli.weaken_program = True
        cli.aggregate_semantic_outcome = "passed"
        cli.scope_repair_baseline = json.loads((self.source / "template.json").read_text())
        cli.program_content = (self.source / "acceptance/p0_organize.py").read_text(encoding="utf-8") + "\n# Additive aggregate-recovery fixture.\n"
        cli.reuse_files = False
        original_run = cli.run
        def run(directory, prompt, model, timeout, cancelled, progress, **kwargs):
            if directory.name == "case-adaptation-aggregate-v1":
                result = {"choices": [{"evidence_ids": ["ev-context-save"], "disposition": "adjusted",
                                       "capability": "Save with target-specific local persistence",
                                       "reason": "The pinned evidence describes source behavior; target persistence is adapted."}]}
            else:
                result = original_run(directory, prompt, model, timeout, cancelled, progress)
            if directory.name == "blueprint-generate-0":
                stdout = json.dumps({"type": "text", "part": {"text": json.dumps(result, ensure_ascii=False)}},
                                    ensure_ascii=False).encode()
                (directory / "stdout.log").write_bytes(stdout)
                (directory / "result.json").write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
                (directory / "cli-summary.json").write_text(json.dumps({
                    "requested_model": model, "cli_status": "completed", "exit_code": 0,
                    "delivery_status": "delivered", "failure_code": None,
                    "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
                }), encoding="utf-8")
            return result
        cli.run = run
        return cli

    def _stop_after_delivery(self, pipeline, job):
        calls = 0
        from template_factory.cognition import validate_file_plan as original
        def fail_once(value, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise FactoryError("crash after successful generation delivery")
            return original(value, **kwargs)
        with patch("template_factory.cognition.validate_file_plan", side_effect=fail_once):
            with self.assertRaisesRegex(FactoryError, "crash after successful"):
                pipeline.run(job)

    def _stop_after_plan_checkpoint(self, pipeline, job):
        from template_factory.cognition import validate_review as original
        calls = 0
        def fail_once(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise FactoryError("synthetic independent review interruption")
            return original(*args, **kwargs)
        with patch("template_factory.cognition.validate_review", side_effect=fail_once):
            with self.assertRaisesRegex(FactoryError, "independent review interruption"):
                pipeline.run(job)

    def test_checkpoint_reload_rebuilds_context_and_recovers_canonical_and_outer_envelopes(self):
        for outer_coverage in (False, True):
            with self.subTest(outer_coverage=outer_coverage):
                job_id = self._queue_v1_job()
                cli = self._cli()
                cli.outer_coverage_generation = outer_coverage
                pipeline = Pipeline(self.store, cli=cli)
                self._stop_after_delivery(pipeline, self.store.claim("first", "production"))
                job_root = self.store.root / "jobs" / job_id
                first = job_root / "attempt-1/blueprint-generate-0"
                first_source = first / "source"
                original_evidence = {name: (first / name).read_bytes() for name in
                                     ("input.json", "stdout.log", "result.json", "cli-summary.json")}
                raw_before = original_evidence["result.json"]
                source_before = tree_manifest(first_source)
                self.assertEqual(json.loads((first_source / "CASE_DESIGN.json").read_text())[0]["evidence_ids"], ["ev-context-save"])
                for name in ("CASE_BASIS.json", "ACCEPTED_CASE_FACTS.json", "CASE_DESIGN.json"):
                    encoded = (first_source / name).read_bytes()
                    self.assertEqual(encoded, (json.dumps(json.loads(encoded), ensure_ascii=False,
                                                          indent=1, sort_keys=True) + "\n").encode())
                self.store.retry(job_id)
                self._stop_after_plan_checkpoint(pipeline, self.store.claim("recover", "production"))
                second = job_root / "attempt-2/blueprint-generate-0"
                self.assertEqual(cli.calls.count("blueprint-generate-0"), 1)
                self.assertEqual((second / "input.json").read_bytes(), original_evidence["input.json"])
                self.assertEqual(tree_manifest(second / "source"), source_before)
                receipt = json.loads((second / "recovery-receipt.json").read_text())
                self.assertTrue(receipt["no_new_cli_call"])
                self.assertEqual(receipt["prior_attempt"], 1)
                if outer_coverage:
                    self.assertEqual(receipt["normalization"], "move exact top-level contract_coverage into spec.contract_coverage")
                else:
                    self.assertEqual(receipt["normalization"], "canonical spec.contract_coverage envelope")
                for name, contents in original_evidence.items():
                    self.assertEqual((first / name).read_bytes(), contents)
                self.assertEqual(json.loads((second / "result.json").read_text()), json.loads(raw_before))
                plan_checkpoint = self.store.checkpoint(job_id, "blueprint-plan-0")
                self.assertIsNotNone(plan_checkpoint)
                self.assertIn("contract_coverage", plan_checkpoint["result"]["spec"])
                self.store.retry(job_id)
                pipeline.run(self.store.claim("resume-plan", "production"))
                self.assertEqual(cli.calls.count("blueprint-generate-0"), 1)
                self.assertEqual(self.store.job(job_id)["state"], "completed")

    def test_source_tampering_blocks_recovery_and_triggers_new_generation(self):
        job_id = self._queue_v1_job()
        cli = self._cli()
        pipeline = Pipeline(self.store, cli=cli)
        self._stop_after_delivery(pipeline, self.store.claim("first", "production"))
        first = self.store.root / "jobs" / job_id / "attempt-1/blueprint-generate-0"
        (first / "source/CASE_DESIGN.json").write_text("tampered\n", encoding="utf-8")
        self.store.retry(job_id)
        self._stop_after_delivery(pipeline, self.store.claim("retry", "production"))
        self.assertEqual(cli.calls.count("blueprint-generate-0"), 2)
        self.assertFalse((self.store.root / "jobs" / job_id / "attempt-2/blueprint-generate-0/recovery-receipt.json").exists())

    def test_v1_aggregate_repair_rebuilds_case_context_and_recovers_before_plan_checkpoint(self):
        g1_source = Path(__file__).resolve().parents[2] / "docs/template-factory/v1-2026-10-19/g1-real-sample/template-8d9229d3895b/source"
        shutil.rmtree(self.source)
        shutil.copytree(g1_source, self.source)
        original_cli = self._cli()
        original_pipeline = Pipeline(self.store, cli=original_cli)
        self._queue_v1_job()
        original_pipeline.run(self.store.claim("create temporary V1 baseline", "production"))
        original = self.store.artifacts()[0]
        original_spec = json.loads((self.store.root / original["bundle_path"] / "source/template.json").read_text())
        self.assertTrue((self.store.root / original["bundle_path"] / "source/acceptance/p0_organize.py").is_file())

        scope_path = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-convergence-2026-10-19/repair/REPAIR_SCOPE.json"
        scope = json.loads(scope_path.read_text(encoding="utf-8"))
        # Scope identity is intentionally rebound to this isolated test artifact;
        # the authored contract and allowed paths remain the checked-in request.
        scope["baseline"].update({"artifact_id": original["id"], "expected_digest": original["digest"],
                                 "case_basis_digest": self.basis["basis_digest"],
                                 "immutable_case_facts": len(self.basis["evidence_ids"])})
        repair_batch = self.store.create_repair(original["id"], {
            "expected_digest": original["digest"], "note": "Exercise aggregate context recovery with a temporary fixture.",
            "model": "fake/flash", "language": "en", "edit_paths": scope["edit_paths"],
            "reuse_spec": False, "repair_scope": scope,
        })
        repair_job = repair_batch["jobs"][0]["id"]
        cli = self._aggregate_cli()
        pipeline = Pipeline(self.store, cli=cli)
        self._stop_after_delivery(pipeline, self.store.claim("aggregate initial delivery", "production"))
        job_root = self.store.root / "jobs" / repair_job
        first = job_root / "attempt-1/blueprint-generate-0"
        first_source = first / "source"
        first_manifest = tree_manifest(first_source)
        for name in ("CASE_BASIS.json", "ACCEPTED_CASE_FACTS.json", "CASE_DESIGN.json", "REPAIR_SCOPE.json"):
            encoded = (first_source / name).read_bytes()
            self.assertEqual(encoded, (json.dumps(json.loads(encoded), ensure_ascii=False,
                                                  indent=1, sort_keys=True) + "\n").encode())
        evidence = {name: (first / name).read_bytes() for name in
                    ("input.json", "stdout.log", "result.json", "cli-summary.json")}

        self.store.retry(repair_job)
        self._stop_after_plan_checkpoint(pipeline, self.store.claim("aggregate recovered delivery", "production"))
        second = job_root / "attempt-2/blueprint-generate-0"
        self.assertEqual(cli.calls.count("blueprint-generate-0"), 1)
        self.assertEqual(tree_manifest(second / "source"), first_manifest)
        self.assertEqual((second / "input.json").read_bytes(), evidence["input.json"])
        receipt = json.loads((second / "recovery-receipt.json").read_text())
        self.assertTrue(receipt["no_new_cli_call"])
        self.assertEqual(receipt["normalization"], "canonical spec.contract_coverage envelope")
        self.assertIsNotNone(self.store.checkpoint(repair_job, "blueprint-plan-0"))
        for name, contents in evidence.items():
            self.assertEqual((first / name).read_bytes(), contents)
        self.store.retry(repair_job)
        pipeline.run(self.store.claim("aggregate plan resume", "production"))
        self.assertEqual(cli.calls.count("blueprint-generate-0"), 1)
        self.assertEqual(self.store.job(repair_job)["state"], "completed")
        revised = next(item for item in self.store.artifacts() if item["id"] != original["id"])
        self.assertEqual(revised["provenance"]["case_basis"]["basis_digest"], original_spec["case_basis"]["basis_digest"])
        self.assertEqual(len(revised["provenance"]["case_facts_view"]["facts"]), 1)


if __name__ == "__main__":
    unittest.main()
