"""Open taxonomy, partial intake, durable batches and crash recovery contracts."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oss_catalog import CatalogError, CatalogStore, ModelServiceUnavailable, available_leaves  # noqa: E402
from oss_batch import BatchJobs  # noqa: E402
from oss_workflow import discover_open_leaf, prepare_leaf  # noqa: E402
from test_oss_discovery import SearchSource, Extractor, TEXT  # noqa: E402


class PartialModel(Extractor):
    def ask(self, stage, instruction, data):
        if stage == "scenarios_open":
            return super().ask("scenarios", instruction, data)
        return {"items": [{"repository_id": r["repository_id"], "relevant": True,
                           "summary": {"text": "根据官方说明整理的初步介绍", "source_id": "readme"},
                           "matches": []} for r in data["repositories"]]}


class BatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CatalogStore(self.root / "test.sqlite", bootstrap=False)
        self.github = SearchSource()
        self.model = PartialModel()
        self.patch = patch("oss_batch.ROOT", self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def run_leaf(self, leaf="bookmark-manager"):
        run = BatchJobs.new_run(leaf)
        return discover_open_leaf(self.store, leaf, run, github=self.github, model=self.model, root=self.root)

    def seed(self, leaf="feed-reader", count=19):
        metas = []
        for index in range(count):
            meta = copy.deepcopy(self.github.items[0])
            meta.update(id=1000 + index, full_name=f"test/project-{index}", name=f"project-{index}")
            metas.append(meta)
        self.store.record_candidates(leaf, metas, "fixture")

    def test_any_existing_leaf_and_zero_star_repository_can_be_collected_without_scenario_proof(self):
        self.assertIn("bookmark-manager", available_leaves())
        for meta in self.github.items:
            meta["stargazers_count"] = 0
        result = self.run_leaf()
        self.assertEqual((result["created"], result["failed"]), (2, 0))
        cards = self.store.catalog("bookmark-manager")["projects"]
        self.assertEqual(len(cards), 2)
        self.assertTrue(all(c["completeness"] == "partial" and not c["matches"] for c in cards))
        self.assertFalse(any("stars:" in p for p in self.github.calls))
        self.assertTrue(all(c["license"]["status"] == "pending" for c in cards))

    def test_missing_readme_keeps_a_metadata_card_but_private_identity_does_not(self):
        original = self.github.get
        def get(path):
            if path.endswith("/readme"):
                raise CatalogError("GitHub 资源不存在", 502)
            value = original(path)
            if path == "/repositories/102":
                value["private"] = True
            return value
        self.github.get = get
        result = self.run_leaf()
        cards = self.store.catalog("bookmark-manager")["projects"]
        self.assertEqual([c["repository_id"] for c in cards], [101])
        self.assertEqual(cards[0]["summary"], TEXT)
        self.assertTrue(cards[0]["collection_notes"])
        self.assertEqual(result["failed"], 1)

    def test_missing_readme_archives_read_license_without_caching_the_failed_readme(self):
        from oss_sources import collect_sources
        from test_oss_discovery import file_data
        original = self.github.get
        read_attempts = []
        def get(path):
            if path.endswith("/readme"):
                read_attempts.append(path)
                raise CatalogError("GitHub 资源不存在或不再公开", 502)
            if path.endswith("/license"):
                return file_data("test/demo-101", "LICENSE", "Public license text for provenance")
            return original(path)
        self.github.get = get
        run = {"source_fetches": 0, "source_cache_hits": 0, "document_fetches": 0, "document_cache_hits": 0}
        meta = copy.deepcopy(self.github.items[0])
        first, cached = collect_sources(self.github, meta, self.root, run, allow_partial=True)
        self.assertFalse(cached)
        self.assertIsNone(first["readme"])
        evidence = list((self.root / "evidence").glob("*.json"))
        self.assertEqual(len(evidence), 1)
        self.assertEqual(json.loads(evidence[0].read_text())["file"]["path"], "LICENSE")
        collect_sources(self.github, meta, self.root, run, allow_partial=True)
        self.assertEqual(len(read_attempts), 2)
        self.assertEqual(run["source_fetches"], 2)
        self.assertEqual(len(list((self.root / "evidence").glob("*.json"))), 1)

    def test_fabricated_quote_is_discarded_without_blocking_a_real_repository(self):
        def ask(stage, instruction, data):
            if stage == "scenarios_open":
                return Extractor().ask("scenarios", instruction, data)
            return {"items": [{"repository_id": r["repository_id"], "relevant": True,
                               "summary": {"text": "不应发布的功能", "quote": "an invented quote", "source_id": "readme"}} for r in data["repositories"]]}
        self.model.ask = ask
        self.run_leaf()
        card = self.store.catalog("bookmark-manager")["projects"][0]
        self.assertEqual(card["summary"], TEXT)
        self.assertNotIn("an invented quote", json.dumps(card))

    def test_empty_or_unreadable_license_does_not_block_partial_intake(self):
        original = self.github.get
        def get(path):
            if path.endswith("/license"):
                return {"encoding": "none", "content": "", "path": "LICENSE"}
            return original(path)
        self.github.get = get
        result = self.run_leaf()
        self.assertEqual(result["created"], 2)
        self.assertEqual(result["failed"], 0)
        self.assertTrue(all(p["license"]["status"] == "pending" for p in self.store.catalog("bookmark-manager")["projects"]))

    def test_malformed_optional_fields_fall_back_to_real_metadata(self):
        original = self.model.ask
        def ask(stage, instruction, data):
            if stage == "scenarios_open":
                return original(stage, instruction, data)
            return {"items": [{"repository_id": r["repository_id"], "relevant": True,
                               "matches": [{"scenario_id": data["scenarios"][0]["id"], "reason": "待核实", "conditions": None}]} for r in data["repositories"]]}
        self.model.ask = ask
        result = self.run_leaf()
        self.assertEqual((result["created"], result["failed"]), (2, 0))
        self.assertTrue(all(p["completeness"] == "partial" for p in self.store.catalog("bookmark-manager")["projects"]))

    def test_long_metadata_with_repeated_whitespace_keeps_valid_proofs_and_a_bounded_summary(self):
        self.github.items[0]['description'] = 'Public  description\nwith spacing. ' * 200
        original = self.github.get
        def get(path):
            if path.endswith('/readme'):
                raise CatalogError('README 暂不可读', 502)
            return original(path)
        self.github.get = get
        self.run_leaf()
        card = self.store.previous('test/demo-101')
        self.assertLessEqual(len(card['summary']), 1500)
        self.assertTrue(card['summary_evidence']['source_url'])
        self.assertLessEqual(len(card['summary_evidence']['excerpt']), 500)

    def test_automatic_continuation_failure_skip_and_completed_job_do_not_replay(self):
        self.seed(count=19)
        seen = []
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            seen.extend(selected_ids)
            for identifier in selected_ids:
                state = "failed" if identifier == 1002 else "partial"
                store.candidate_result(leaf, identifier, state, "fixture")
                on_candidate(identifier, state, "fixture")
            run["status"] = "completed"
        jobs = BatchJobs(self.store, worker, lambda *a, **kw: None)
        job = jobs.create(["feed-reader"], existing_only=True, batch_size=8)
        self.assertEqual((job["processed"], job["total"], job["status"]), (19, 19, "partial"))
        self.assertEqual(len(seen), len(set(seen)))
        self.assertEqual(len(job["runs"]), 4)  # preparation plus three continuing chunks
        self.assertEqual(jobs.resume(job["id"])["processed"], 19)
        self.assertEqual(len(seen), 19)

    def test_crash_resume_replays_only_unfinished_candidates_and_keeps_other_leaf_progress(self):
        self.seed(count=5)
        self.seed("diagramming-application", count=3)
        processed = []
        def interrupted(store, leaf, run, selected_ids, search, on_candidate):
            processed.append(selected_ids[0])
            on_candidate(selected_ids[0], "partial", "saved before crash")
            raise KeyboardInterrupt()
        jobs = BatchJobs(self.store, interrupted, lambda *a, **kw: None)
        with self.assertRaises(KeyboardInterrupt):
            jobs.create(["feed-reader", "diagramming-application"], existing_only=True)
        job = jobs.list()[0]
        self.assertEqual(job["status"], "interrupted")
        self.assertEqual(job["processed"], 1)
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                processed.append(identifier)
                on_candidate(identifier, "partial", "resumed")
        job = BatchJobs(CatalogStore(self.store.path, bootstrap=False), finish, lambda *a, **kw: None).resume(job["id"])
        self.assertEqual((job["status"], job["processed"], job["total"]), ("completed", 8, 8))
        self.assertEqual(processed.count(1000), 2)  # once in each leaf, never twice in the first leaf

    def test_unknown_leaf_and_path_traversal_rejected_before_job_creation(self):
        for leaf in ["../outside", "not-a-real-leaf"]:
            with self.assertRaises(CatalogError):
                BatchJobs(self.store).create([leaf])
        self.assertFalse(BatchJobs(self.store).list())

    def test_model_pause_preserves_unfinished_targets_and_resume_does_not_replay_completed(self):
        self.seed(count=5)
        seen = []
        def paused(store, leaf, run, selected_ids, search, on_candidate):
            seen.append(selected_ids[0])
            on_candidate(selected_ids[0], "accepted", "saved")
            raise ModelServiceUnavailable("模型额度已耗尽")
        job = BatchJobs(self.store, paused, lambda *a, **kw: None).create(["feed-reader"], existing_only=True)
        self.assertEqual((job["status"], job["processed"], job["total"]), ("paused_model", 1, 5))
        self.assertEqual(sum(item["status"] == "running" for item in job["targets"]["feed-reader"]), 4)
        self.assertFalse(self.store.catalog("feed-reader")["projects"])
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            seen.extend(selected_ids)
            for identifier in selected_ids:
                on_candidate(identifier, "accepted", "resumed")
        resumed = BatchJobs(CatalogStore(self.store.path, bootstrap=False), finish, lambda *a, **kw: None).resume(job["id"])
        self.assertEqual((resumed["status"], resumed["processed"]), ("completed", 5))
        self.assertEqual(len(seen), len(set(seen)))
        self.assertNotIn("pause_reason", resumed)

    def test_model_outage_during_extraction_preserves_sources_and_creates_no_placeholder_card(self):
        original = self.model.ask
        def ask(stage, instruction, data):
            if stage == "scenarios_open":
                return original(stage, instruction, data)
            raise ModelServiceUnavailable("模型额度已耗尽")
        self.model.ask = ask
        with self.assertRaises(ModelServiceUnavailable):
            self.run_leaf()
        self.assertFalse(self.store.catalog("bookmark-manager")["projects"])
        self.assertTrue(list((self.root / "sources").glob("*.json")))
        self.assertTrue(all(c["status"] == "pending" for c in self.store.candidates("bookmark-manager")))

    def test_search_pagination_retains_zero_star_results(self):
        from urllib.parse import parse_qs, urlparse
        pages = []
        def get(path):
            query = parse_qs(urlparse(path).query)
            page = int(query["page"][0])
            pages.append(page)
            self.assertNotIn("stars:", query["q"][0])
            metas = []
            for identifier in range(1000 if page == 1 else 1100, 1100 if page == 1 else 1101):
                meta = copy.deepcopy(self.github.items[0])
                meta.update(id=identifier, full_name=f"test/{identifier}", stargazers_count=0)
                metas.append(meta)
            return {"total_count": 101, "items": metas}
        self.github.get = get
        with self.store.connect() as con:
            self.store._scenarios(con, [{"id": "only", "name": "任务", "description": "一个实际任务"}], "bookmark-manager")
        prepare_leaf(self.store, "bookmark-manager", BatchJobs.new_run("bookmark-manager"), github=self.github, model=self.model, root=self.root, search_pages=2)
        self.assertEqual(pages, [1, 2])
        self.assertEqual(len(self.store.candidates("bookmark-manager")), 101)

    def test_unknown_model_identity_cannot_create_a_phantom_project(self):
        original = self.model.ask
        def ask(stage, instruction, data):
            if stage == "scenarios_open":
                return original(stage, instruction, data)
            return {"items": [{"repository_id": 999999, "summary": {"text": "虚构项目"}}]}
        self.model.ask = ask
        self.run_leaf()
        cards = self.store.catalog("bookmark-manager")["projects"]
        self.assertEqual({c["repository_id"] for c in cards}, {101, 102})
        self.assertTrue(all(c["completeness"] == "partial" for c in cards))
        self.assertNotIn("虚构项目", json.dumps(cards, ensure_ascii=False))

    def test_previous_dependency_warning_keeps_the_card_but_labels_inferred_capabilities(self):
        from oss_catalog import digest
        path = self.root / "reviews.json"
        path.write_text(json.dumps({"test/demo-101": {"readme_sha256": digest(TEXT), "exclude_unless_documented": True, "reason": "依赖库用途不能证明产品功能"}}))
        extractor = Extractor()
        self.model.ask = lambda stage, instruction, data: extractor.ask("scenarios" if stage == "scenarios_open" else "extract", instruction, data)
        with patch("oss_discovery.PROJECT_REVIEWS", path):
            self.run_leaf()
        card = self.store.previous("test/demo-101")
        self.assertEqual(card["completeness"], "partial")
        self.assertTrue(all(m["applicability"] == "unverified" for m in card["matches"]))
        self.assertTrue(all(f["evidence"]["verification"] == "inferred" for f in card["features"]))

    def test_batch_creation_takes_a_finite_queue_snapshot_before_any_leaf_is_run(self):
        self.seed(count=2)
        def prepare(*args, **kwargs):
            self.seed(count=3)  # Simulate another discovery adding a candidate during preparation.
        attempted = []
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                attempted.append(identifier)
                on_candidate(identifier, "partial", "saved")
        job = BatchJobs(self.store, worker, prepare).create(["feed-reader"], existing_only=True)
        self.assertEqual(job["total"], 2)
        self.assertEqual(set(attempted), {1000, 1001})

    def test_export_roundtrip_keeps_unassociated_cards_and_legacy_scenario_ownership(self):
        from oss_discovery import export_batch
        self.run_leaf()
        with self.store.connect() as con:
            con.execute("insert into oss_scenario values ('legacy','personal-knowledge-management-application',0,?)", (json.dumps({'id': 'legacy', 'name': '旧场景', 'description': '无内嵌叶子字段'}),))
        export_batch(self.store, self.root / 'batch.snapshot.json')
        bundle = json.loads((self.root / 'batch.snapshot.json').read_text())
        self.assertTrue(all(s.get('leaf') for s in bundle['scenarios']))
        restored = CatalogStore(self.root / 'restored.sqlite', bootstrap=False)
        with patch('oss_catalog.DATA', self.root):
            restored.bootstrap_batch()
        self.assertEqual(len(restored.catalog('bookmark-manager')['projects']), 2)
        self.assertEqual(len(restored.catalog('personal-knowledge-management-application')['scenarios']), 1)


if __name__ == "__main__":
    unittest.main()
