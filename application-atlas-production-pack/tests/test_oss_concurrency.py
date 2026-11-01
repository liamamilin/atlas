"""Bounded model overlap, isolated receipts, serial commits and resumable partial failure."""
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from threading import Barrier, Lock
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_model as model  # noqa: E402
from oss_batch import BatchJobs  # noqa: E402
from oss_catalog import CatalogStore  # noqa: E402
from oss_workflow import discover_open_leaf  # noqa: E402
from test_oss_discovery import SearchSource  # noqa: E402


class ConcurrencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for p in [patch.dict(os.environ, {model.CONFIG_ENV: str(self.root / 'model-config.json')}),
                  patch('oss_batch.ROOT', self.root), patch('oss_workflow.MODEL_WORKERS', 2)]:
            p.start()
            self.addCleanup(p.stop)
        model.upsert_provider({'preset': 'open-design', 'api_key': 'fixture-primary'})
        model.upsert_provider({'preset': 'opencode-go', 'api_key': 'fixture-go'})
        model.set_default('open-design', 'deepseek-v4.1-flash')
        model.set_fallback({'enabled': True, 'from_provider': 'open-design', 'provider': 'opencode-go', 'model': 'deepseek-v4.1-flash'})
        self.store = CatalogStore(self.root / 'test.sqlite', bootstrap=False)
        self.github = SearchSource()
        sample = self.github.items[0]
        self.github.items = [{**copy.deepcopy(sample), 'id': i, 'full_name': f'test/demo-{i}', 'name': f'demo-{i}'} for i in range(100, 108)]
        self.store.record_candidates('feed-reader', self.github.items, 'fixture')
        with self.store.connect() as con:
            self.store._scenarios(con, [{'id': 'fixture', 'name': '订阅阅读', 'description': '阅读订阅文章'}], 'feed-reader')

    @staticmethod
    def reply(body):
        data = json.loads(body['messages'][1]['content'])
        result = {'items': [{'repository_id': m['repository_id'], 'relevant': True,
                             'summary': {'text': '依据官方 README 整理的订阅工具', 'source_id': 'readme'}} for m in data['repositories']]}
        return {'model': 'fixture-served', 'choices': [{'message': {'content': json.dumps(result)}}], 'usage': {'total_tokens': 20}}

    def worker(self, store, leaf, run, **kwargs):
        return discover_open_leaf(store, leaf, run, github=self.github, root=self.root, **kwargs)

    def start(self):
        return BatchJobs(self.store, self.worker, lambda *a, **kw: None).create(['feed-reader'], existing_only=True, auto_recovery=False)

    def test_two_requests_overlap_and_counters_receipts_checkpoints_and_cache_are_preserved(self):
        barrier, lock = Barrier(2), Lock()
        active, peak = 0, 0
        commit_threads = []
        upsert = self.store._upsert
        def commit(*args, **kwargs):
            from threading import get_ident
            commit_threads.append(get_ident())
            return upsert(*args, **kwargs)
        def post(url, body, headers, timeout):
            nonlocal active, peak
            with lock:
                active += 1
                peak = max(active, peak)
            try:
                barrier.wait(timeout=5)
                return self.reply(body)
            finally:
                with lock:
                    active -= 1
        with patch.object(model, '_post_json', side_effect=post) as network, patch.object(self.store, '_upsert', side_effect=commit):
            job = self.start()
        self.assertEqual((job['status'], job['processed']), ('completed', 8))
        self.assertEqual((peak, network.call_count, len(set(commit_threads))), (2, 2, 1))
        run = self.store.run(job['current_run'])
        self.assertEqual((run['model_calls'], len(run['model_receipts'])), (2, 2))
        self.assertEqual(len(run['model_tasks']), 2)
        self.assertTrue(all(t['state'] == 'completed' for t in run['model_tasks'].values()))
        self.assertEqual(sum(r['usage']['total_tokens'] for r in run['model_receipts']), 40)
        self.assertEqual(len(self.store.catalog('feed-reader')['projects']), 8)
        repeat = BatchJobs.new_run('feed-reader')
        with patch.object(model, '_post_json', side_effect=AssertionError('cache must avoid another request')):
            self.worker(self.store, 'feed-reader', repeat, selected_ids=list(range(100, 108)), search=False)
        self.assertEqual((repeat['model_calls'], repeat['model_cache_hits']), (0, 2))
        self.assertEqual(len(self.store.catalog('feed-reader')['projects']), 8)

    def test_one_group_outage_still_saves_successful_sibling_and_resume_only_requests_unfinished_ids(self):
        barrier, seen, lock = Barrier(2), set(), Lock()
        def post(url, body, headers, timeout):
            ids = [m['repository_id'] for m in json.loads(body['messages'][1]['content'])['repositories']]
            with lock:
                first = ids[0] not in seen
                seen.add(ids[0])
            if first:
                barrier.wait(timeout=5)
            if ids[0] == 100:
                raise HTTPError(url, 503, '', {}, io.BytesIO(b'temporary upstream failure'))
            return self.reply(body)
        with patch.object(model, '_post_json', side_effect=post) as network, patch('oss_discovery.time.sleep'):
            job = self.start()
        self.assertEqual((job['status'], job['processed'], network.call_count), ('paused_model', 4, 4))
        self.assertEqual({p['repository_id'] for p in self.store.catalog('feed-reader')['projects']}, set(range(104, 108)))
        run = self.store.run(job['current_run'])
        self.assertEqual((run['model_calls'], len(run['model_errors']), len(run['model_receipts'])), (4, 3, 1))
        requested = []
        def recovered(url, body, headers, timeout):
            requested.extend(m['repository_id'] for m in json.loads(body['messages'][1]['content'])['repositories'])
            return self.reply(body)
        with patch.object(model, '_post_json', side_effect=recovered):
            resumed = BatchJobs(self.store, self.worker, lambda *a, **kw: None).resume(job['id'])
        self.assertEqual((resumed['status'], resumed['processed']), ('completed', 8))
        self.assertEqual(requested, list(range(100, 104)))

    def test_simultaneous_quota_failures_switch_to_go_with_correct_cache_identity(self):
        barrier, lock, seen = Barrier(2), Lock(), []
        def post(url, body, headers, timeout):
            with lock:
                seen.append((url, headers.get('x-opencode-session')))
            if 'open-design' in url:
                barrier.wait(timeout=5)
                raise HTTPError(url, 402, '', {}, io.BytesIO(b'insufficient_balance'))
            return self.reply(body)
        with patch.object(model, '_post_json', side_effect=post):
            job = self.start()
        self.assertEqual((job['status'], job['processed']), ('completed', 8))
        run = self.store.run(job['current_run'])
        self.assertEqual([r['provider'] for r in run['model_receipts']], ['opencode-go', 'opencode-go'])
        self.assertEqual(len(list((self.root / 'model-cache').glob('*.json'))), 2)
        self.assertEqual(len(seen), 4)
        self.assertTrue(all(session == run['id'] for url, session in seen if 'opencode.ai' in url))
        self.assertTrue(model.fallback_view()['active'])

    def test_serial_setting_remains_available(self):
        with patch('oss_workflow.MODEL_WORKERS', 1), patch.object(model, '_post_json', side_effect=lambda url, body, headers, timeout: self.reply(body)) as network:
            job = self.start()
        self.assertEqual((job['status'], job['processed'], network.call_count), ('completed', 8, 2))
        self.assertEqual(self.store.run(job['current_run'])['concurrency']['model_workers'], 1)

    def add_candidates(self):
        sample = self.github.items[0]
        self.github.items.extend({**copy.deepcopy(sample), 'id': i, 'full_name': f'test/demo-{i}', 'name': f'demo-{i}'} for i in range(108, 116))
        self.store.record_candidates('feed-reader', self.github.items, 'fixture')

    def test_larger_chunk_still_has_at_most_two_active_model_requests(self):
        self.add_candidates()
        barrier, lock = Barrier(2), Lock()
        active, peak = 0, 0
        def post(url, body, headers, timeout):
            nonlocal active, peak
            with lock:
                active += 1
                peak = max(active, peak)
            try:
                barrier.wait(timeout=5)
                return self.reply(body)
            finally:
                with lock:
                    active -= 1
        with patch.object(model, '_post_json', side_effect=post) as network:
            job = BatchJobs(self.store, self.worker, lambda *a, **kw: None).create(['feed-reader'], existing_only=True, batch_size=16, auto_recovery=False)
        self.assertEqual((job['status'], job['processed'], peak, network.call_count), ('completed', 16, 2, 4))
        run = self.store.run(job['current_run'])
        self.assertEqual((len(run['model_tasks']), run['model_calls'], len(run['model_receipts'])), (4, 4, 4))

    def test_persistent_outage_does_not_start_queued_groups_after_active_groups_stop(self):
        self.add_candidates()
        barrier, lock, seen = Barrier(2), Lock(), set()
        def post(url, body, headers, timeout):
            first_id = json.loads(body['messages'][1]['content'])['repositories'][0]['repository_id']
            with lock:
                first = first_id not in seen
                seen.add(first_id)
            if first:
                barrier.wait(timeout=5)
            raise HTTPError(url, 503, '', {}, io.BytesIO(b'temporary upstream failure'))
        with patch.object(model, '_post_json', side_effect=post) as network, patch('oss_discovery.time.sleep'):
            job = BatchJobs(self.store, self.worker, lambda *a, **kw: None).create(['feed-reader'], existing_only=True, batch_size=16, auto_recovery=False)
        self.assertEqual((job['status'], job['processed'], network.call_count), ('paused_model', 0, 6))
        self.assertEqual(seen, {100, 104})
        self.assertFalse(self.store.catalog('feed-reader')['projects'])

    def test_four_requests_overlap_and_a_full_transient_outage_recovers_without_manual_resume(self):
        self.add_candidates()
        barrier, lock = Barrier(4), Lock()
        attempts, first_active = {}, 0
        peak = 0
        wall = [1000.0]
        waits = []
        def wait(seconds):
            waits.append(seconds)
            wall[0] += seconds
        def post(url, body, headers, timeout):
            nonlocal first_active, peak
            first_id = json.loads(body['messages'][1]['content'])['repositories'][0]['repository_id']
            with lock:
                attempts[first_id] = attempts.get(first_id, 0) + 1
                attempt = attempts[first_id]
                if attempt == 1:
                    first_active += 1
                    peak = max(peak, first_active)
            if attempt == 1:
                barrier.wait(timeout=5)
            if attempt <= 3:
                raise HTTPError(url, 520, '', {}, io.BytesIO(b'temporary gateway failure'))
            return self.reply(body)
        jobs = BatchJobs(self.store, self.worker, lambda *a, **kw: None, clock=lambda: wall[0], waiter=wait)
        with patch('oss_workflow.MODEL_WORKERS', 4), patch.object(model, '_post_json', side_effect=post) as network, patch('oss_discovery.time.sleep'):
            job = jobs.create(['feed-reader'], existing_only=True, batch_size=16)
        self.assertEqual((job['status'], job['processed'], peak, network.call_count), ('completed', 16, 4, 16))
        self.assertEqual(sum(waits), 60)
        self.assertEqual(job['recovery']['cycles'], 1)
        self.assertEqual(job['recovery']['consecutive_failures'], 0)
        run = self.store.run(job['current_run'])
        self.assertEqual((run['model_calls'], len(run['model_receipts']), run['concurrency']['model_workers']), (4, 4, 4))


if __name__ == '__main__':
    unittest.main()
