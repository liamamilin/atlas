"""Scoped specification patch repair contracts using local fixture services."""
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import test_cognition as cognition_fixtures
from test_cognition import FakeCognitionCLI
from template_factory.store import FactoryError, canonical, digest


class SpecPatchCLI(FakeCognitionCLI):
    invalid_patch = None

    def run(self, directory, prompt, model, timeout, cancelled, progress):
        if directory.name.endswith("-spec-patch"):
            supplied = json.loads((directory / "input.json").read_text())
            plan = json.loads((directory / "source/SPECIFICATION.json").read_text())
            self.spec_repair_requests.append({"input": supplied})
            current = plan["spec"]["architecture_markdown"]
            result = {
                "base_proposal_digest": supplied["base_proposal_digest"],
                "spec_changes": [{
                    "path": ["architecture_markdown"],
                    "replacements": [{"old": current.splitlines()[0], "new": current.splitlines()[0] + "\nSpec patch fixture."}],
                }],
            }
            if self.invalid_patch == "field":
                result["spec_changes"][0]["path"] = ["limits"]
            elif self.invalid_patch == "file_plan":
                result["file_plan_changes"] = [{"path": "acceptance/README.md", "reuse": False}]
            return result
        return super().run(directory, prompt, model, timeout, cancelled, progress)


class WeakeningAggregateCLI(FakeCognitionCLI):
    weaken_program = False
    aggregate_semantic_outcome = "blocked"
    program_content = None

    def run(self, directory, prompt, model, timeout, cancelled, progress):
        if self.weaken_program and directory.name.startswith("blueprint-code"):
            supplied = json.loads((directory / "input.json").read_text())
            path = supplied["file"]["path"]
            if path == "acceptance/p0_organize.py":
                content = self.program_content or "# Deliberately weakened: no category assertions remain.\n"
                return {"path": path, "content": content}
        return super().run(directory, prompt, model, timeout, cancelled, progress)


class SpecPatchTests(unittest.TestCase):
    setUp = cognition_fixtures.CognitionTests.setUp
    tearDown = cognition_fixtures.CognitionTests.tearDown
    batch = cognition_fixtures.CognitionTests.batch
    pipeline = cognition_fixtures.CognitionTests.pipeline
    produce = cognition_fixtures.CognitionTests.produce
    scenario = cognition_fixtures.CognitionTests.scenario
    def test_spec_patch_queue_and_produce_reuses_all_programs_and_keeps_review_gate(self):
        _, _, original = self.produce()
        original_source = self.store.root / original["bundle_path"] / "source"
        before = {p.relative_to(original_source).as_posix(): p.read_bytes() for p in original_source.rglob("*") if p.is_file()}
        request = {
            "expected_digest": original["digest"],
            "note": "Clarify invalid URL and malformed JSON behavior in the architecture.",
            "model": "fake/flash",
            "spec_edit_paths": [["architecture_markdown"]],
        }
        batch = self.store.create_repair(original["id"], request)
        self.assertEqual(self.store.create_repair(original["id"], request)["id"], batch["id"])
        self.cli = SpecPatchCLI(self.source)
        self.cli.design_outcome = "uncertain"
        from template_factory.pipeline import Pipeline
        pipeline = Pipeline(self.store, cli=self.cli)
        pipeline.run(self.store.claim("spec patch fixture", "production"))
        revision = next(a for a in self.store.artifacts() if a["id"] != original["id"])
        self.assertEqual(revision["provenance"]["spec_edit_paths"], [["architecture_markdown"]])
        self.assertEqual(revision["provenance"]["spec_review"]["outcome"], "uncertain")
        revised_source = self.store.root / revision["bundle_path"] / "source"
        after = {p.relative_to(revised_source).as_posix(): p.read_bytes() for p in revised_source.rglob("*") if p.is_file()}
        self.assertEqual({k: v for k, v in before.items() if k.startswith(("acceptance/", "references/")) and k != "acceptance/plan.json"},
                         {k: v for k, v in after.items() if k.startswith(("acceptance/", "references/")) and k != "acceptance/plan.json"})
        self.assertEqual(before, {p.relative_to(original_source).as_posix(): p.read_bytes() for p in original_source.rglob("*") if p.is_file()})
        checkpoints = self.store.root / "jobs" / revision["job_id"] / "attempt-1/context/SPEC_REVISION_0.json"
        record = json.loads(checkpoints.read_text())
        self.assertEqual(record["scope"], [["architecture_markdown"]])
        self.assertTrue(record["model_response_digest"])

    def test_rendered_aggregate_with_weakened_allowed_program_stops_before_freeze(self):
        # Use the pinned real G1 source inventory so this exercises the same
        # renderer and scope gate that the formal aggregate request will use.
        g1_source = Path(__file__).resolve().parents[2] / "docs/template-factory/v1-2026-10-19/g1-real-sample/template-8d9229d3895b/source"
        shutil.rmtree(self.source)
        shutil.copytree(g1_source, self.source)
        _, _, original = self.produce()
        original_source = self.store.root / original["bundle_path"] / "source"
        spec = json.loads((original_source / "template.json").read_text())
        self.assertTrue((original_source / "acceptance/p0_organize.py").is_file())
        from template_factory.contract_scope import REPAIR_SCOPE_VERSION
        scope = {
            "version": REPAIR_SCOPE_VERSION,
            "known_blockers": [{
                "feature_id": "F03", "acceptance_id": "A04", "decision_id": "D03",
                "basis": "Category management must be proven through actual UI forms.",
            }],
            "authorized_assertion_changes": [{
                "acceptance_id": "A02",
                "change": "single_label_hostname_negative_to_positive",
                "rationale": "A valid single-label HTTP(S) hostname does not require DNS or a dot.",
            }],
            "authored_field_paths": [["architecture_markdown"]],
            "edit_paths": ["acceptance/p0_organize.py"],
        }
        self.assertEqual(spec["acceptance"][3]["id"], "A04")
        request = {
            "expected_digest": original["digest"],
            "note": "Exercise the aggregate freeze guard with a deliberately weakened in-scope acceptance program.",
            "model": "fake/flash",
            "edit_paths": scope["edit_paths"],
            "reuse_spec": False,
            "repair_scope": scope,
        }
        batch = self.store.create_repair(original["id"], request)
        job_id = batch["jobs"][0]["id"]
        self.cli = WeakeningAggregateCLI(self.source)
        self.cli.weaken_program = True
        from template_factory.pipeline import Pipeline
        pipeline = Pipeline(self.store, cli=self.cli)
        with self.assertRaisesRegex(FactoryError, "did not pass"):
            pipeline.run(self.store.claim("aggregate scope fixture", "production"))
        self.assertEqual(self.cli.calls.count("aggregate-semantic-review"), 1)
        self.store.retry(job_id)
        with self.assertRaisesRegex(FactoryError, "did not pass"):
            pipeline.run(self.store.claim("aggregate scope fixture retry", "production"))
        self.assertEqual(self.cli.calls.count("aggregate-semantic-review"), 1)

        # render_candidate produced a real candidate and the host diff gate
        # allowed the in-scope path. The semantic review then rejected the
        # weakened program, and freeze_blueprint was never reached.
        self.assertEqual(len(self.store.artifacts()), 1)
        attempt = self.store.root / "jobs" / job_id / "attempt-2"
        candidate = attempt / "candidate-0"
        self.assertTrue((candidate / "template.json").is_file())
        self.assertEqual((candidate / "acceptance/p0_organize.py").read_text(), "# Deliberately weakened: no category assertions remain.\n")
        self.assertTrue((attempt / "aggregate-semantic-review/report.json").is_file())
        self.assertFalse((attempt / "bundle/source/template.json").exists())
        report = json.loads((attempt / "aggregate-semantic-review/report.json").read_text())
        self.assertEqual(report["outcome"], "blocked")
        failure = self.store.job(job_id).get("error")
        failure = failure.get("message", "") if isinstance(failure, dict) else str(failure)
        self.assertIn("aggregate repair semantic review", failure)

    def test_rendered_aggregate_scope_review_passes_and_freezes_exact_candidate(self):
        g1_source = Path(__file__).resolve().parents[2] / "docs/template-factory/v1-2026-10-19/g1-real-sample/template-8d9229d3895b/source"
        shutil.rmtree(self.source)
        shutil.copytree(g1_source, self.source)
        _, _, original = self.produce()
        original_source = self.store.root / original["bundle_path"] / "source"
        program = (original_source / "acceptance/p0_organize.py").read_text()
        scope = {
            "version": "atlas.aggregate-repair-scope.v1",
            "known_blockers": [{"feature_id": "F03", "acceptance_id": "A04", "decision_id": "D03", "basis": "Add real category UI journeys."}],
            "authorized_assertion_changes": [{"acceptance_id": "A02", "change": "single_label_hostname_negative_to_positive", "rationale": "A valid hostname can be single-label."}],
            "authored_field_paths": [["architecture_markdown"]],
            "edit_paths": ["acceptance/p0_organize.py"],
        }
        batch = self.store.create_repair(original["id"], {
            "expected_digest": original["digest"], "note": "Make an additive scoped documentation comment and semantically review it.",
            "model": "fake/flash", "reuse_spec": False, "edit_paths": scope["edit_paths"], "repair_scope": scope,
        })
        job_id = batch["jobs"][0]["id"]
        self.cli = WeakeningAggregateCLI(self.source)
        self.cli.weaken_program = True
        self.cli.aggregate_semantic_outcome = "passed"
        self.cli.program_content = program + "\n# Additive repair note; existing assertions are retained.\n"
        from template_factory.pipeline import Pipeline
        pipeline = Pipeline(self.store, cli=self.cli)
        with patch("template_factory.cognition.freeze_blueprint", side_effect=FactoryError("synthetic stop after semantic checkpoint")):
            with self.assertRaisesRegex(FactoryError, "synthetic stop"):
                pipeline.run(self.store.claim("aggregate passing fixture", "production"))
        semantic_calls = self.cli.calls.count("aggregate-semantic-review")
        self.assertEqual(semantic_calls, 1)
        self.store.retry(job_id)
        pipeline.run(self.store.claim("aggregate passing fixture retry", "production"))
        self.assertEqual(self.cli.calls.count("aggregate-semantic-review"), semantic_calls)
        revised = next(item for item in self.store.artifacts() if item["id"] != original["id"])
        revised_source = self.store.root / revised["bundle_path"] / "source"
        self.assertEqual(revised["provenance"]["aggregate_semantic_review"]["outcome"], "passed")
        self.assertEqual(revised["provenance"]["aggregate_semantic_review"]["identity"]["baseline_digest"], original["digest"])
        self.assertEqual(revised["provenance"]["aggregate_semantic_review"]["identity"]["diff_digest"], revised["provenance"]["aggregate_repair_diff"]["diff_digest"])
        self.assertEqual(revised_source.joinpath("acceptance/p0_organize.py").read_text(), self.cli.program_content)
        self.assertTrue(revised_source.joinpath("inputs/aggregate-repair-diff.json").is_file())
        self.assertTrue(revised_source.joinpath("inputs/repair-scope.json").is_file())
        frozen_diff = json.loads(
            revised_source.joinpath("inputs/aggregate-repair-diff.json").read_text()
        )
        provenance_diff = revised["provenance"]["aggregate_repair_diff"]
        semantic_identity_digest = revised["provenance"]["aggregate_semantic_review"]["identity"]["diff_digest"]
        self.assertIsInstance(frozen_diff.get("diff_digest"), str)
        self.assertTrue(frozen_diff["diff_digest"])
        self.assertEqual(frozen_diff["diff_digest"], provenance_diff["diff_digest"])
        self.assertEqual(frozen_diff["diff_digest"], semantic_identity_digest)
        # Rendered/host-owned documents are allowed to differ while program
        # edits remain restricted to the explicitly authorized path.
        self.assertNotEqual((original_source / "template.json").read_bytes(), (revised_source / "template.json").read_bytes())
        diff = revised["provenance"]["aggregate_repair_diff"]
        self.assertEqual(set(diff["program_diffs"]), {"acceptance/p0_organize.py"})
        self.assertEqual(self.store.job(job_id)["state"], "completed")

    def test_spec_patch_queue_rejects_unauthorized_fields_and_mixed_modes(self):
        _, _, artifact = self.produce()
        base = {"expected_digest": artifact["digest"], "note": "Repair the architecture.", "model": "fake/flash"}
        for extra in (
            {"spec_edit_paths": [["acceptance", "A01", "goal"]]},
            {"spec_edit_paths": [["decisions", "missing", "impact"]]},
            {"spec_edit_paths": [["architecture_markdown"]], "edit_paths": ["acceptance/README.md"]},
            {"spec_edit_paths": [["architecture_markdown"]], "reuse_spec": True, "edit_paths": ["acceptance/README.md"]},
        ):
            with self.subTest(extra=extra), self.assertRaises(FactoryError):
                self.store.create_repair(artifact["id"], {**base, **extra})

    def test_legacy_repair_digest_replay_reuses_existing_job(self):
        _, _, artifact = self.produce()
        request = {
            "expected_digest": artifact["digest"],
            "note": "Keep the same repair request identity.",
            "model": "fake/flash",
            "edit_paths": ["acceptance/README.md"],
            "reuse_spec": True,
        }
        first_batch = self.store.create_repair(artifact["id"], request)
        legacy_digest = digest({
            "artifact_id": artifact["id"],
            "artifact_digest": artifact["digest"],
            "note": request["note"],
            "scope": request["edit_paths"],
            "reuse": True,
            "config": self.store.job(self.store.batch(first_batch["id"])["jobs"][0]["id"])["snapshot"]["config"],
        })
        with self.store.connect(True) as con:
            row = con.execute(
                "SELECT id,snapshot FROM job WHERE json_extract(snapshot,'$.repair_request_digest')=?",
                (self.store.job(self.store.batch(first_batch["id"])["jobs"][0]["id"])["snapshot"]["repair_request_digest"],),
            ).fetchone()
            snapshot = json.loads(row["snapshot"])
            snapshot["repair_request_digest"] = legacy_digest
            con.execute("UPDATE job SET snapshot=? WHERE id=?", (canonical(snapshot), row["id"]))
            before = con.execute("SELECT COUNT(*) FROM job WHERE kind='blueprint-production'").fetchone()[0]
        replayed = self.store.create_repair(artifact["id"], request)
        with self.store.connect() as con:
            after = con.execute("SELECT COUNT(*) FROM job WHERE kind='blueprint-production'").fetchone()[0]
        self.assertEqual(replayed["id"], first_batch["id"])
        self.assertEqual(after, before)

    def test_queue_repair_can_join_outer_transaction_and_returns_ids(self):
        from template_factory.cognition import queue_repair

        _, _, artifact = self.produce()
        request = {
            "expected_digest": artifact["digest"],
            "note": "Use a caller-owned transaction for recovery orchestration.",
            "model": "fake/flash",
            "edit_paths": ["acceptance/README.md"],
            "reuse_spec": True,
        }
        with self.store.connect(True) as con:
            queued = queue_repair(self.store, artifact, request, con=con, parent_state_override="running")
            self.assertEqual(set(queued), {"batch_id", "job_id", "created"})
            self.assertTrue(queued["created"])
            row = con.execute("SELECT batch_id FROM job WHERE id=?", (queued["job_id"],)).fetchone()
            self.assertEqual(row[0], queued["batch_id"])
        self.assertEqual(self.store.batch(queued["batch_id"])["id"], queued["batch_id"])

    def test_spec_patch_host_rejects_model_scope_and_file_plan_overreach(self):
        for mode in ("field", "file_plan"):
            with self.subTest(mode=mode):
                self.tearDown()
                self.setUp()
                _, _, original = self.produce()
                self.store.create_repair(original["id"], {
                    "expected_digest": original["digest"],
                    "note": "Patch the architecture only.",
                    "model": "fake/flash",
                    "spec_edit_paths": [["architecture_markdown"]],
                })
                cli = SpecPatchCLI(self.source)
                cli.invalid_patch = mode
                from template_factory.pipeline import Pipeline
                pipeline = Pipeline(self.store, cli=cli)
                with self.assertRaises(FactoryError):
                    pipeline.run(self.store.claim("overreach fixture", "production"))
                self.assertEqual(len(self.store.artifacts()), 1)


if __name__ == "__main__":
    unittest.main()
