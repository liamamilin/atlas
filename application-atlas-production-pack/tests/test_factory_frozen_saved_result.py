"""Host-only continuation is limited to a fully delivered frozen review."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.pipeline import Pipeline  # noqa: E402
from template_factory.store import FactoryError  # noqa: E402


from test_factory_frozen_link import FrozenReviewFixtureCLI


class FramedFixtureCLI(FrozenReviewFixtureCLI):
    def run(self, directory, *args, **kwargs):
        from atlas_runtime import atomic_json
        from template_factory.cli import recover_cognitive_framing
        result = super().run(directory, *args, **kwargs)
        directory = Path(directory)
        text = json.dumps(result, ensure_ascii=False) + "</｜｜DSML｜｜ parameter>"
        recovered, receipt = recover_cognitive_framing(text)
        assert recovered == result
        atomic_json(directory / "original-response.json", {"text": text})
        atomic_json(directory / "framing-recovery.json", receipt)
        summary = json.loads((directory / "cli-summary.json").read_bytes())
        summary["original_response_sha256"] = hashlib.sha256((directory / "original-response.json").read_bytes()).hexdigest()
        atomic_json(directory / "cli-summary.json", summary)
        return result


class FrozenSavedResultTests(unittest.TestCase):
    def setUp(self):
        from test_factory_frozen_link import FrozenReviewPipelineLinkTests, PRODUCED
        self.fixture = FrozenReviewPipelineLinkTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        artifact = next(row for row in self.fixture.store.artifacts() if row["id"] == "tpl_f7ecff8d8fef4deba828aa2a8ef82918")
        archive = self.fixture.store.root / artifact["archive_path"]
        archive.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PRODUCED / "blueprint.zip", archive)

    def test_host_only_resume_requires_verified_saved_result_and_does_not_call_cli(self):
        from test_factory_frozen_link import FrozenReviewFixtureCLI, JOB_ID
        fixture = self.fixture
        service, request, _prepared, grant, claimed = fixture._prepare_recover_and_claim()
        cli = FramedFixtureCLI(fixture.store)
        complete = fixture.store.complete_acceptance
        calls = 0

        def fail_first_acceptance(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 1:
                raise RuntimeError("fixture interruption after delivered output")
            return complete(*args, **kwargs)

        with patch.object(fixture.store, "complete_acceptance", side_effect=fail_first_acceptance):
            with self.assertRaises(RuntimeError):
                Pipeline(fixture.store, cli=cli).run(claimed)

        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(fixture.store.job(JOB_ID)["state"], "needs_review")
        result_path = cli.calls[0] / "result.json"
        result_sha = hashlib.sha256(result_path.read_bytes()).hexdigest()
        resume_request = {
            "schema": "atlas.frozen-review-saved-result-resume.v1",
            "grant_id": grant["id"],
            "request_key": request["request_key"] + "-host-only",
            "source_gate": request["source_gate"],
            "expected_result_sha256": "0" * 64,
        }
        with self.assertRaises(FactoryError):
            service.resume_saved_result(JOB_ID, resume_request)

        resume_request["expected_result_sha256"] = result_sha
        saved = service.resume_saved_result(JOB_ID, resume_request)
        self.assertFalse(saved["cli_allowed"])
        claimed_again = fixture.store.claim("frozen-review-host-only")
        self.assertEqual(claimed_again["attempt"], 3)
        Pipeline(fixture.store, cli=cli).run(claimed_again)
        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(fixture.store.job(JOB_ID)["state"], "completed")
        with fixture.store.connect() as con:
            receipt = con.execute(
                "SELECT result_sha256,old_attempt,next_attempt FROM tf_evidence_saved_resume WHERE id=?",
                (saved["id"],),
            ).fetchone()
        self.assertEqual((receipt["result_sha256"], receipt["old_attempt"], receipt["next_attempt"]),
                         (result_sha, 2, 3))

    def test_normal_framing_delivery_and_checks_tamper_boundary(self):
        from test_factory_frozen_link import JOB_ID
        fixture = self.fixture
        service, _, _, grant, claimed = fixture._prepare_recover_and_claim()
        cli = FramedFixtureCLI(fixture.store)
        Pipeline(fixture.store, cli=cli).run(claimed)
        self.assertEqual(fixture.store.job(JOB_ID)["state"], "completed")
        self.assertEqual(len(cli.calls), 1)
        # An unrelated or changed framing receipt cannot authenticate the raw text.
        receipt = cli.calls[0] / "framing-recovery.json"
        receipt.write_text('{}')
        with self.assertRaises(FactoryError):
            service.validate_saved_result(claimed, {"grant_id": grant["id"]})

    def test_checks_tamper_with_same_passed_outcome_is_rejected(self):
        from test_factory_frozen_link import JOB_ID
        fixture = self.fixture
        _, _, _, _, claimed = fixture._prepare_recover_and_claim()
        cli = FramedFixtureCLI(fixture.store)
        complete = fixture.store.complete_acceptance
        def tamper(job_id, token, result):
            if result.get("outcome") == "passed":
                result = {**result, "checks": [{**r, "reason": "unrelated replacement"} for r in result["checks"]]}
            return complete(job_id, token, result)
        with patch.object(fixture.store, "complete_acceptance", side_effect=tamper):
            with self.assertRaises(FactoryError):
                Pipeline(fixture.store, cli=cli).run(claimed)
        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(fixture.store.job(JOB_ID)["state"], "needs_review")


if __name__ == "__main__":
    unittest.main()
