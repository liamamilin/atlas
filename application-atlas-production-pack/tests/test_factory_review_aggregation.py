"""Cached design-review aggregation retains strict host-file citation checks."""
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_protocol_link as protocol_fixture
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError
from template_factory.v1_batches import BatchService

ARCHIVE = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-protocol-recovery-2026-10-19"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
JOB_ID = "job_7742b1c124be4c9ab3a0096da5cdd772"
PRODUCT_ID = "product-c42848f63251507bd9d911a5"


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

    def test_real_legacy_source_conflict_is_rejected_before_cached_reviews_or_authoring(self):
        subreview_rows = [row for row in self.checkpoint_rows if row["name"].startswith("blueprint-design-check-0-")]
        self.assertEqual(len(subreview_rows), 6)
        original_checkpoint_bytes = {row["name"]: row["body"] for row in subreview_rows}
        cli_calls = []

        class NoProviderBeforeSourceGate:
            def info(self):
                return {"provider_called": False}

            def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
                cli_calls.append(Path(directory).name)
                raise AssertionError("source conflict must be rejected before provider invocation")

        with self.assertRaises(FactoryError) as rejected:
            Pipeline(self.store, cli=NoProviderBeforeSourceGate()).run(self.job)
        self.assertEqual(rejected.exception.code, "invalid_feature_sources")
        report = json.loads(str(rejected.exception).split("report=", 1)[1])
        self.assertFalse(report["valid"])
        self.assertEqual(
            report["available_source_ids"],
            ["S01", "S02", "S03", "S04", "S06", "S07", "S12", "S13", "S14", "S15", "S16", "S19", "S20", "S21"],
        )
        by_feature = {row["feature_id"]: row for row in report["features"]}
        self.assertEqual(by_feature["F01"]["missing_source_ids"], ["S17"])
        self.assertEqual(by_feature["F07"]["missing_source_ids"], ["S08"])
        self.assertEqual(by_feature["F08"]["missing_source_ids"], ["S09", "S11"])
        self.assertEqual(by_feature["F10"]["missing_source_ids"], ["S08"])
        self.assertEqual(by_feature["F11"]["missing_source_ids"], ["S10", "S18"])
        self.assertEqual(by_feature["F12"]["missing_source_ids"], ["S08"])
        self.assertEqual(by_feature["F24"]["missing_source_ids"], ["S17"])
        self.assertEqual(cli_calls, [])
        for name, body in original_checkpoint_bytes.items():
            with self.store.connect() as con:
                row = con.execute("SELECT body FROM checkpoint WHERE job_id=? AND name=?", (JOB_ID, name)).fetchone()
            self.assertEqual(row[0], body)


if __name__ == "__main__":
    unittest.main()
