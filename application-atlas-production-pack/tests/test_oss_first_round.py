"""First-round limits, balanced priority, durable targets, pipelining and pilot gate."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile
from threading import Event
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oss_batch import BatchJobs, BatchRecoveryService, dispatch_batch  # noqa: E402
from oss_catalog import CatalogError, CatalogStore, canonical, digest, now  # noqa: E402
from oss_priority import select_first_round  # noqa: E402
from oss_sources import collect_sources  # noqa: E402
from oss_workflow import discover_open_leaf, prepare_leaf, read_candidate_sources  # noqa: E402
from oss_acceptance import audit_pilot, verify_incremental  # noqa: E402
from test_oss_batch import PartialModel  # noqa: E402
from test_oss_discovery import SearchSource, file_data  # noqa: E402


class FirstRoundTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CatalogStore(self.root / 'catalog.sqlite', bootstrap=False)
        patcher = patch('oss_batch.ROOT', self.root)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.leaves = ['feed-reader', 'diagramming-application', 'password-manager']

    def seed(self, leaf, count=90):
        sample = SearchSource().items[0]
        scenarios = [{'id': f'{leaf}-scenario-{n}', 'name': f'Task {n}', 'description': f'Real workflow {n}',
                      'search_queries': [f'purpose{n}']} for n in range(3)]
        with self.store.connect() as con:
            self.store._scenarios(con, scenarios, leaf)
        for n in range(3):
            items = [{**copy.deepcopy(sample), 'id': 1000 + i, 'full_name': f'test/project-{i}', 'name': f'project-{i}',
                      'description': f'purpose{n} documented tool', 'stargazers_count': 0 if i % 3 == 0 else 100000}
                     for i in range(n * (count // 3), (n + 1) * (count // 3))]
            self.store.record_candidates(leaf, items, 'fixture', discovery={'query': f'purpose{n}', 'page': 1,
                                                                          'scenario_id': scenarios[n]['id']})
        return scenarios

    @staticmethod
    def finish(store, leaf, run, selected_ids, search, on_candidate, **kwargs):
        for identifier in selected_ids:
            store.candidate_result(leaf, identifier, 'partial', 'documented fixture')
            on_candidate(identifier, 'partial', 'documented fixture')
        run['status'] = 'completed'

    def test_each_leaf_cap_is_60_and_every_unselected_candidate_stays_pending(self):
        for leaf in self.leaves:
            self.seed(leaf)
        jobs = BatchJobs(self.store, self.finish, lambda *a, **kw: None)
        job = jobs.create(self.leaves, existing_only=True, first_round_limit=60)
        self.assertEqual((job['status'], job['processed'], job['total']), ('completed', 180, 180))
        saved = jobs.get(job['id'])
        self.assertEqual(len(saved['completed_leaves']), 3)
        self.assertEqual(saved['deferred_total'], 90)
        for leaf in self.leaves:
            self.assertEqual(len(saved['targets'][leaf]), 60)
            states = self.store.candidate_counts(leaf)
            self.assertEqual(states, {'partial': 60, 'pending': 30})
            allocations = [t['priority']['allocated_scenario'] for t in saved['targets'][leaf]]
            self.assertEqual([allocations.count(f'{leaf}-scenario-{i}') for i in range(3)], [20, 20, 20])
            self.assertTrue(any(t['repository_id'] % 3 == 1 for t in saved['targets'][leaf]))  # zero-star candidates
        with self.store.connect() as con:
            header = json.loads(con.execute('SELECT data FROM oss_batch_job WHERE id=?', (job['id'],)).fetchone()[0])
            self.assertEqual(header['targets'], {})
            self.assertEqual(con.execute('SELECT COUNT(*) FROM oss_batch_target').fetchone()[0], 180)
        self.assertEqual(jobs.list()[0]['targets'], {})
        self.assertEqual(jobs.resume(job['id'])['processed'], 180)

    def test_ranking_prefers_relevance_over_popularity_and_is_stable(self):
        scenarios = self.seed('feed-reader')
        candidates = self.store.candidates('feed-reader')
        ranked = select_first_round(candidates, scenarios, 'Feed Reader', 9, datetime(2026, 10, 26, tzinfo=timezone.utc))
        again = select_first_round(list(reversed(candidates)), scenarios, 'Feed Reader', 9, datetime(2026, 10, 26, tzinfo=timezone.utc))
        self.assertEqual([c['repository_id'] for c in ranked], [c['repository_id'] for c in again])
        self.assertEqual(len({c['priority']['allocated_scenario'] for c in ranked}), 3)
        self.assertEqual(len({c['repository_id'] for c in ranked}), 9)

    def test_checkpoint_is_durable_even_if_header_counter_is_stale(self):
        self.seed('feed-reader')
        requested = []
        def crash(store, leaf, run, selected_ids, search, on_candidate):
            requested.append(selected_ids[0])
            store.candidate_result(leaf, selected_ids[0], 'partial', 'saved before crash')
            on_candidate(selected_ids[0], 'partial', 'saved before crash')
            raise KeyboardInterrupt()
        jobs = BatchJobs(self.store, crash, lambda *a, **kw: None)
        with self.assertRaises(KeyboardInterrupt):
            jobs.create(['feed-reader'], existing_only=True, first_round_limit=60)
        with self.store.connect() as con:
            row = con.execute('SELECT id,data FROM oss_batch_job').fetchone()
            header = json.loads(row['data'])
            header['processed'] = 0
            con.execute('UPDATE oss_batch_job SET data=? WHERE id=?', (canonical(header), row['id']))
        self.assertEqual(jobs.get(row['id'])['processed'], 1)
        def finish(store, leaf, run, **kwargs):
            requested.extend(kwargs['selected_ids'])
            self.finish(store, leaf, run, **kwargs)
        result = BatchJobs(self.store, finish, lambda *a, **kw: None).resume(row['id'])
        self.assertEqual((result['status'], result['processed']), ('completed', 60))
        self.assertEqual(len(requested), len(set(requested)))
        self.assertEqual(self.store.candidate_counts('feed-reader')['pending'], 30)

    def test_nullable_or_invalid_push_time_is_unknown_activity_not_a_batch_failure(self):
        scenarios = self.seed('feed-reader')
        candidates = self.store.candidates('feed-reader')
        for i, value in enumerate([None, '', 'invalid', '2026-10-26T00:00:00', 123]):
            candidates[i]['data']['meta']['pushed_at'] = value
        candidates[5]['data']['meta'].pop('pushed_at', None)
        ranked = select_first_round(candidates[:6], scenarios, 'Feed Reader', 60,
                                    datetime(2026, 10, 26, tzinfo=timezone.utc))
        self.assertEqual(len(ranked), 6)
        self.assertTrue(all(c['priority']['signals']['activity'] == 0 for c in ranked))
        self.assertEqual({c['repository_id'] for c in ranked}, {c['repository_id'] for c in candidates[:6]})

    def test_pilot_stops_after_20_then_continues_only_after_a_real_bound_record(self):
        from oss_catalog import available_leaves
        leaves = list(available_leaves())[:21]
        for leaf in leaves:
            self.seed(leaf, 3)
        jobs = BatchJobs(self.store, self.finish, lambda *a, **kw: None)
        job = jobs.create(leaves, existing_only=True, first_round_limit=1, pilot_size=20)
        self.assertEqual((job['status'], job['processed'], len(job['completed_leaves'])), ('awaiting_acceptance', 20, 20))
        self.assertNotIn(leaves[20], job['prepared'])
        with self.assertRaises(CatalogError):
            jobs.resume(job['id'])
        self.assertFalse(BatchRecoveryService(self.store, jobs).tick()['started'])
        artifact = {'job_id': job['id'], 'structural_passed': True, 'semantic_review_passed': True, 'pilot_leaves': leaves[:20]}
        path = self.root / 'acceptance' / (job['id'] + '.json')
        path.parent.mkdir()
        text = canonical(artifact)
        report = {k: artifact[k] for k in ['job_id', 'structural_passed', 'semantic_review_passed']}
        report.update(report_path=str(path), report_sha256=digest(text))
        with self.assertRaises(CatalogError):
            jobs.accept_pilot(job['id'], report)
        path.write_text(text)
        resumed = jobs.accept_pilot(job['id'], report)
        self.assertEqual((resumed['status'], resumed['processed'], len(resumed['completed_leaves'])), ('completed', 21, 21))
        self.assertEqual(resumed['pilot']['status'], 'passed')
        self.assertEqual(jobs.resume(job['id'])['processed'], 21)

    def test_source_prefetch_overlaps_model_work_and_does_not_touch_deferred_candidates(self):
        self.seed('feed-reader')
        extracting, next_reading = Event(), Event()
        fetched, committed = [], []
        def read(store, leaf, ids, source_policy):
            fetched.extend(ids)
            if len(fetched) > 16:
                next_reading.set()
                self.assertTrue(extracting.wait(3))
            return {'selected_ids': ids}
        def worker(store, leaf, run, selected_ids, search, on_candidate, prepared_sources):
            self.assertEqual(prepared_sources['selected_ids'], selected_ids)
            if not committed:
                extracting.set()
                self.assertTrue(next_reading.wait(3))
            committed.extend(selected_ids)
            self.finish(store, leaf, run, selected_ids, search, on_candidate)
        jobs = BatchJobs(self.store, worker, lambda *a, **kw: None, prefetcher=read)
        result = jobs.create(['feed-reader'], existing_only=True, first_round_limit=32)
        self.assertEqual((result['status'], result['processed']), ('completed', 32))
        self.assertEqual(fetched, committed)
        self.assertEqual(len(set(fetched)), 32)
        self.assertEqual(self.store.candidate_counts('feed-reader')['pending'], 58)

    def test_prefetch_coordinator_abort_recovers_without_failing_or_losing_quota(self):
        self.seed('feed-reader')
        attempts, waited = [], []
        wall = [1000.0]
        def advance(seconds):
            waited.append(seconds)
            wall[0] += seconds
        def read(store, leaf, ids, source_policy):
            attempts.append(list(ids))
            if len(attempts) == 1:
                raise RuntimeError('private details')
            return {'selected_ids': ids}
        jobs = BatchJobs(self.store, self.finish, lambda *a, **kw: None, prefetcher=read,
                         clock=lambda: wall[0], waiter=advance)
        result = jobs.create(['feed-reader'], existing_only=True, first_round_limit=32)
        self.assertEqual((result['status'], result['processed']), ('completed', 32))
        self.assertEqual(sum(waited), 60)
        self.assertEqual(result['recovery']['component'], 'workflow')
        self.assertEqual(attempts[0], attempts[1])
        self.assertFalse(any(t['status'] == 'failed' for t in result['targets']['feed-reader']))
        self.assertEqual(self.store.candidate_counts('feed-reader')['pending'], 58)

    def test_fast_policy_reads_license_and_reuses_only_previously_public_cached_files(self):
        github = SearchSource()
        original = github.get
        text = 'Official feature description with useful details. ' * 20
        def get(path):
            if path.endswith('/readme'):
                return file_data('test/demo-101', 'README.md', text)
            return original(path)
        github.get = get
        meta = copy.deepcopy(github.items[0])
        counts = {'source_cache_hits': 0, 'source_fetches': 0, 'document_cache_hits': 0, 'document_fetches': 0}
        resources, cached = collect_sources(github, meta, self.root, counts, allow_partial=True,
                                             include_documents=False, search_verified_at=now())
        self.assertFalse(cached)
        self.assertTrue(resources['supplemental_documents_deferred'])
        self.assertTrue(any(p.endswith('/license') for p in github.calls))
        self.assertIn('/repositories/101', github.calls)  # fresh files always recheck public visibility
        self.assertFalse(any('/git/trees/' in p for p in github.calls))
        github.calls.clear()
        collect_sources(github, meta, self.root, counts, allow_partial=True, include_documents=False, search_verified_at=now())
        self.assertFalse(github.calls)  # no fresh private file can enter a cache-only reuse
        self.assertFalse(list((self.root / 'documentation').glob('*.json')))

    def test_short_readme_falls_back_to_supplemental_docs_and_visibility_is_still_checked(self):
        github = SearchSource()
        run = {k: 0 for k in ['source_cache_hits', 'source_fetches', 'document_cache_hits', 'document_fetches']}
        collect_sources(github, copy.deepcopy(github.items[0]), self.root, run, allow_partial=True,
                        include_documents=False, search_verified_at=now())
        self.assertTrue(any('/git/trees/' in p for p in github.calls))
        self.assertIn('/repositories/101', github.calls)

    def test_real_worker_uses_lightweight_scenario_and_count_queries(self):
        github = SearchSource()
        self.store.record_candidates('feed-reader', github.items, 'fixture')
        run = BatchJobs.new_run('feed-reader')
        with patch.object(self.store, 'catalog', side_effect=AssertionError('do not deserialize the full catalog')):
            discover_open_leaf(self.store, 'feed-reader', run, github=github, model=PartialModel(), root=self.root, search=False)
        self.assertEqual((run['status'], run['processed']), ('completed', 2))

    def test_real_pilot_sources_license_labels_and_isolated_incremental_are_auditable(self):
        github = SearchSource()
        def prepare(store, leaf, run, **kwargs):
            return prepare_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, **kwargs)
        def read(store, leaf, ids, source_policy):
            return read_candidate_sources(store, leaf, ids, github=github, root=self.root, source_policy=source_policy)
        def worker(store, leaf, run, **kwargs):
            return discover_open_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, **kwargs)
        job = BatchJobs(self.store, worker, prepare, prefetcher=read).create(self.leaves[:2], first_round_limit=2, pilot_size=1)
        self.assertEqual(job['status'], 'awaiting_acceptance')
        audit = audit_pilot(self.store, job['id'], root=self.root)
        self.assertTrue(audit['structural_passed'], audit['failures'])
        self.assertFalse(audit['semantic_review_passed'])
        self.assertEqual(audit['totals']['published_distinct_projects'], 2)
        self.assertEqual(audit['totals']['licenses'], {'pending': 2})
        replay = verify_incremental(self.store, job['id'])
        self.assertTrue(replay['passed'])
        self.assertFalse(replay['production_database_modified'])

    def test_invalid_limits_and_acceptance_route_cannot_create_or_release_a_task(self):
        for limit in [0, 101, True, '60']:
            with self.assertRaises(CatalogError):
                BatchJobs(self.store).create(['feed-reader'], first_round_limit=limit)
        with self.assertRaises(CatalogError):
            BatchJobs(self.store).create(['feed-reader'], first_round_limit=60, pilot_size=20)
        with self.assertRaises(CatalogError):
            dispatch_batch(self.store, 'POST', '/api/oss/batches/batch_' + 'a' * 32 + '/accept-pilot', {})


if __name__ == '__main__':
    unittest.main()
