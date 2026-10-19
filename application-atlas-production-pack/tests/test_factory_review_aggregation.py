"""Cached design-review aggregation retains strict host-file citation checks."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_protocol_link as protocol_fixture
from template_factory.cognition import _case_adaptation_review_digest
from template_factory.pipeline import Pipeline
from template_factory.scenario_policy import policy_for
from template_factory.store import FactoryError, digest
from template_factory.v1_batches import BatchService

ARCHIVE = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-protocol-recovery-2026-10-19"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
JOB_ID = "job_7742b1c124be4c9ab3a0096da5cdd772"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"


class StopBeforeProvider(FactoryError):
    def __init__(self):
        super().__init__("temporary test stops before any provider call", "fixture_stop", 409)


class ReviewAggregationTests(unittest.TestCase):
    def setUp(self):
        # Import the existing integration fixture as a module to reuse its faithful
        # temporary V1 plan, frozen source, case records, and checkpoint records.
        self.fixture = protocol_fixture.ProtocolPipelineLinkTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.store = self.fixture.store
        self.archive = self.fixture.archive
        self.checkpoint_rows = json.loads((self.archive / "actual-all-six-subreview-checkpoints.json").read_text())
        with self.store.connect(True) as con:
            for row in self.checkpoint_rows:
                con.execute("INSERT OR REPLACE INTO checkpoint VALUES(?,?,?)",
                            (row["job_id"], row["name"], row["body"]))
            con.execute("UPDATE job SET state='queued',attempt=4,token=NULL,lease=NULL,error=NULL WHERE id=?", (JOB_ID,))
        # Resume the fixture's authoritative paused parent so its queued child can be claimed.
        BatchService(self.store).action(PLAN_ID, "resume")
        self.job = self.store.claim("review-aggregation-fixture")
        self.assertEqual((self.job["id"], self.job["attempt"]), (JOB_ID, 4))

    def test_cached_six_subreviews_aggregate_with_strict_policy_citation_and_no_review_call(self):
        subreview_rows = [row for row in self.checkpoint_rows if row["name"].startswith("blueprint-design-check-0-")]
        self.assertEqual(len(subreview_rows), 6)
        original_checkpoint_bytes = {row["name"]: row["body"] for row in subreview_rows}
        cli_calls = []

        class StopAtFirstCodeGeneration:
            def __init__(self, test_case, job):
                self.test_case, self.job = test_case, job

            def info(self):
                return {"provider_called": False}

            def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
                cli_calls.append(Path(directory).name)
                self.assert_code_stage(directory)
                raise StopBeforeProvider()

            def assert_code_stage(self, directory):
                test = self.test_case
                test.assertRegex(Path(directory).name, r"^blueprint-code-0-[0-9]+$")
                source = Path(directory) / "source"
                policy = policy_for(self.job["snapshot"]["scenario"], PRODUCT_ID)
                policy_bytes = (source / "CASE_ADAPTATION_POLICY.json").read_bytes()
                test.assertEqual(json.loads(policy_bytes), policy)
                test.assertEqual(policy_bytes.decode("utf-8"), json.dumps(policy, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
                # CASE_DESIGN remains the existing stable root-context serialization;
                # the architecture subreview's differently indented copy is not used.
                design_bytes = (source / "CASE_DESIGN.json").read_bytes()
                test.assertEqual(json.loads(design_bytes), self.job["snapshot"]["case_design"])
                test.assertEqual(design_bytes.decode("utf-8"), json.dumps(self.job["snapshot"]["case_design"], ensure_ascii=False, indent=1, sort_keys=True) + "\n")

        with self.assertRaises(FactoryError) as stopped:
            Pipeline(self.store, cli=StopAtFirstCodeGeneration(self, self.job)).run(self.job)
        self.assertEqual(stopped.exception.code, "fixture_stop")
        self.assertEqual(len(cli_calls), 1)
        self.assertRegex(cli_calls[0], r"^blueprint-code-0-[0-9]+$")

        adaptation_digest = _case_adaptation_review_digest(
            self.job["snapshot"]["case_design"],
            policy_for(self.job["snapshot"]["scenario"], PRODUCT_ID),
        )
        aggregate_name = "blueprint-spec-review-0-" + adaptation_digest[:16] + "-runtime-v1"
        aggregate = self.store.checkpoint(JOB_ID, aggregate_name)
        self.assertIsNotNone(aggregate)
        self.assertEqual(aggregate["digest"], digest(aggregate["result"]))
        report = aggregate["result"]
        self.assertEqual(report["outcome"], "passed")
        self.assertEqual(len(report["checks"]), 6)
        self.assertTrue(all(check["outcome"] == "passed" for check in report["checks"]))
        self.assertEqual(report["case_adaptation_review_digest"], adaptation_digest)
        for name, body in original_checkpoint_bytes.items():
            with self.store.connect() as con:
                row = con.execute("SELECT body FROM checkpoint WHERE job_id=? AND name=?", (JOB_ID, name)).fetchone()
            self.assertEqual(row[0], body)


if __name__ == "__main__":
    unittest.main()
