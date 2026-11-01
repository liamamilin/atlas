"""The four-error repair must preserve old candidates and first-round limits."""
import copy
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oss_batch import BatchJobs
from oss_workflow import discover_open_leaf
from test_oss_batch import PartialModel
from test_oss_discovery import SearchSource

script = Path(__file__).resolve().parents[2] / "docs/oss-first-round-2026-10-26/repair-2026-10-29/repair_errors.py"
spec = importlib.util.spec_from_file_location("four_error_repair", script)
repair = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repair)


class RepairCampaignTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = repair.PreservingStore(self.root / "catalog.sqlite", bootstrap=False)

    def test_search_replay_keeps_processed_status_frozen_metadata_and_old_facts(self):
        leaf = "portfolio-management-system"
        github = SearchSource()
        run = BatchJobs.new_run(leaf)
        discover_open_leaf(self.store, leaf, run, github=github, model=PartialModel(), root=self.root)
        before = {c["repository_id"]: c for c in self.store.candidates(leaf)}
        meta = copy.deepcopy(github.items[0]); meta.update(pushed_at="2030-01-01T00:00:00Z", description="changed metadata")
        self.store.record_candidates(leaf, [meta], "new-version", discovery={"query": "generic task", "page": 1})
        after = {c["repository_id"]: c for c in self.store.candidates(leaf)}
        self.assertEqual(before[meta["id"]]["status"], after[meta["id"]]["status"])
        self.assertEqual(before[meta["id"]]["data"]["meta"], after[meta["id"]]["data"]["meta"])
        card = self.store.previous(meta["full_name"], leaf)
        self.store.favorite(meta["id"], True)
        with self.store.connect() as con:
            self.store._upsert(con, {**card, "summary": "must never replace reviewed facts", "license": {"status": "wrong"}}, leaf)
        saved = self.store.previous(meta["full_name"], leaf)
        self.assertEqual(saved["summary"], card["summary"])
        self.assertEqual(saved["license"], card["license"])
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT favorite FROM oss_project WHERE repository_id=?", (meta["id"],)).fetchone()[0], 1)

    def test_empty_frozen_leaf_can_be_filled_once_without_new_job_or_exceeding_60(self):
        leaf = "it-operations-management-itom"
        seen = []
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                seen.append(identifier)
                store.candidate_result(leaf, identifier, "partial", "fixture evidence")
                on_candidate(identifier, "partial", "fixture evidence")
            run.update(status="completed")
        with patch("oss_batch.ROOT", self.root):
            jobs = BatchJobs(self.store, worker=finish, preparer=lambda *a, **kw: None)
            job = jobs.create([leaf], existing_only=True, first_round_limit=60)
            sample = SearchSource().items[0]
            items = [{**sample, "id": 1000 + i, "full_name": f"test/project-{i}", "name": f"project-{i}"} for i in range(90)]
            self.store.record_candidates(leaf, items, "fixture", discovery={"query": "generic task", "page": 1})
            scenarios = [{"id": "repair-scenario", "name": "故障处理", "description": "值班人员排查服务故障", "search_queries": ["generic task"]}]
            with self.store.connect() as con:
                self.store._scenarios(con, scenarios, leaf, prune=False)
            with patch.object(repair, "JOB", job["id"]):
                first = repair.fill_empty_leaf(self.store, jobs, job, leaf, scenarios)
                again = repair.fill_empty_leaf(self.store, jobs, job, leaf, scenarios)
        self.assertEqual((first["selected"], first["processed_now"], again["processed_now"]), (60, 60, 0))
        self.assertEqual(len(seen), len(set(seen)))
        self.assertEqual(self.store.candidate_counts(leaf), {"partial": 60, "pending": 30})
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM oss_batch_job").fetchone()[0], 1)


if __name__ == "__main__":
    unittest.main()
