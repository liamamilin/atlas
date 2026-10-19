"""Scoped specification patch repair contracts using local fixture services."""
import json
from pathlib import Path
import sys
import unittest

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
