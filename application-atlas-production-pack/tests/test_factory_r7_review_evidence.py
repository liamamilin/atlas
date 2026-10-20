"""Bounded R7 phase-review program evidence; temporary stores only."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r7_link as r7_fixture
from template_factory.cognition import (
    DESIGN_REVIEW_PROMPT,
    _r7_design_program_evidence,
    _r7_phase_acceptance_prompt,
    _validate_design_review_projection_checkpoint,
)
from template_factory.plan_revision import PreparedRevisionService, R7_SOURCE_JOB, program_revision_contents
from template_factory.artifacts import tree_manifest
from template_factory.store import FactoryError, digest


class R7ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.fixture = r7_fixture.R7PositivePipelineLinkTests(methodName="runTest")
        self.fixture.setUp()

    def tearDown(self):
        self.fixture.tearDown()
        self.fixture.doCleanups()

    def prepare(self):
        request = json.loads((r7_fixture.R7_DOCS / "prepare-request.json").read_text())
        prepared = PreparedRevisionService(self.fixture.store).prepare(R7_SOURCE_JOB, request)
        contents = program_revision_contents(self.fixture.store, prepared["prepared_program_revision"])
        return request, prepared, contents

    def test_verified_programs_authorization_and_disposition_are_available_to_r7_phase_review(self):
        request, prepared, contents = self.prepare()
        evidence = _r7_design_program_evidence(self.fixture.store, prepared, request, contents)
        self.assertEqual(evidence["manifest"]["schema"], "atlas.r7-phase-review-program-evidence.v1")
        self.assertEqual(len(evidence["manifest"]["programs"]), 9)
        self.assertEqual(sum(row["mode"] == "reuse" for row in evidence["manifest"]["programs"]), 5)
        self.assertEqual(sum(row["mode"] == "replace" for row in evidence["manifest"]["programs"]), 4)
        organize = "acceptance/p0_organize.py"
        source = evidence["files"]["program-evidence/source/" + organize].decode()
        candidate = evidence["files"]["program-evidence/prepared/" + organize].decode()
        self.assertIn("_a05_across_restart", candidate)
        self.assertIn("a05-restart-category-id", candidate)
        self.assertIn("_a05_across_restart", source)
        self.assertIn("program-evidence/authorization/approved-revision.json", evidence["files"])
        self.assertIn("program-evidence/authorization/patch.json", evidence["files"])
        disposition = json.loads(evidence["files"]["program-evidence/authorization/A05_FINDING_DISPOSITION.json"])
        self.assertEqual(disposition["schema"], "atlas.r7-findings-disposition.v1")
        self.assertTrue(any("A05" in row.get("reason", "") or "A05" in row.get("text", "")
                            for row in disposition["items"]))
        self.assertEqual(evidence["digest"], digest(evidence["manifest"]))
        projection = self.fixture.root / "phase-projection-fixture"
        for relative, raw in evidence["files"].items():
            target = projection / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        original_projection_digest = digest(tree_manifest(projection))
        target = projection / "program-evidence/prepared/acceptance/p0_organize.py"
        target.write_bytes(target.read_bytes() + b"\n# changed evidence\n")
        changed_projection_digest = digest(tree_manifest(projection))
        self.assertNotEqual(original_projection_digest, changed_projection_digest)
        stale_review = {"proposal_digest": digest({}), "projection_digest": original_projection_digest}
        with self.assertRaises(FactoryError) as stale:
            _validate_design_review_projection_checkpoint(stale_review, {}, changed_projection_digest)
        self.assertEqual(stale.exception.code, "checkpoint_changed")
        prompt = _r7_phase_acceptance_prompt(evidence)
        self.assertNotIn("Historical programs are deliberately excluded", prompt)
        self.assertNotIn("Programs do not exist yet", prompt)
        self.assertIn("do not execute them or claim they passed", prompt)
        self.assertEqual(_r7_phase_acceptance_prompt(None), DESIGN_REVIEW_PROMPT)

    def test_bad_manifest_and_old_program_byte_changes_stop_with_checkpoint_changed(self):
        request, prepared, contents = self.prepare()
        bad_manifest = json.loads(json.dumps(prepared))
        bad_manifest["prepared_program_revision"]["entries"][0]["before_sha256"] = "0" * 64
        with self.assertRaises(FactoryError) as invalid:
            _r7_design_program_evidence(self.fixture.store, bad_manifest, request, contents)
        self.assertEqual(invalid.exception.code, "checkpoint_changed")

        source = self.fixture.store.root / "jobs" / R7_SOURCE_JOB / "attempt-1/context/generated-0/acceptance/p0_organize.py"
        source.write_bytes(source.read_bytes() + b"\n# test-only tamper\n")
        with self.assertRaises(FactoryError) as changed:
            _r7_design_program_evidence(self.fixture.store, prepared, request, contents)
        self.assertEqual(changed.exception.code, "checkpoint_changed")

    def test_non_r7_reviews_receive_no_program_evidence(self):
        self.assertIsNone(_r7_design_program_evidence(
            self.fixture.store,
            {"schema": "atlas.failed-plan-revision.v2"},
            {},
            {},
        ))

    def test_r7_missing_prepared_request_is_a_checkpoint_change(self):
        request, prepared, contents = self.prepare()
        with self.assertRaises(FactoryError) as missing:
            _r7_design_program_evidence(self.fixture.store, prepared, None, contents)
        self.assertEqual(missing.exception.code, "checkpoint_changed")


if __name__ == "__main__":
    unittest.main()
