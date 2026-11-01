"""Persistent cooldowns and server-owned recovery, independent of page reads."""
from datetime import datetime
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oss_batch import BatchJobs, BatchRecoveryService  # noqa: E402
from oss_catalog import CatalogStore, ModelServiceUnavailable, GitHubServiceUnavailable, plain_text  # noqa: E402
from oss_workflow import discover_open_leaf, prepare_leaf  # noqa: E402
import oss_workflow  # noqa: E402
from test_oss_batch import PartialModel  # noqa: E402
from test_oss_discovery import SearchSource, file_data  # noqa: E402


class InlineJobs(BatchJobs):
    def resume(self, identifier, background=False, automatic=False):
        return super().resume(identifier, background=False, automatic=automatic)


class RecoveryServiceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CatalogStore(self.root / 'test.sqlite', bootstrap=False)
        self.store.record_candidates('feed-reader', SearchSource().items, 'fixture')
        p = patch('oss_batch.ROOT', self.root)
        p.start()
        self.addCleanup(p.stop)
        self.wall = 1000.0
        self.waited = []
        self.wait_states = []

    def advance(self, seconds):
        self.waited.append(seconds)
        self.wall += seconds
        with self.store.connect() as con:
            job = json.loads(con.execute('SELECT data FROM oss_batch_job ORDER BY rowid DESC LIMIT 1').fetchone()[0])
        self.wait_states.append(job)

    def jobs(self, worker, preparer=None, cls=BatchJobs, waiter=None):
        return cls(self.store, worker, preparer or (lambda *a, **kw: None),
                   clock=lambda: self.wall, waiter=waiter or self.advance)

    @staticmethod
    def outage(retry_after=None):
        return ModelServiceUnavailable('temporary gateway failure', retryable=True,
                                       retry_after=retry_after, code='provider_error', upstream_status=520)

    def test_repeated_outage_cools_down_and_finishes_without_replaying_completed_targets(self):
        calls, saved = [], []
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            calls.append(selected_ids)
            if len(calls) == 1:
                saved.append(selected_ids[0])
                on_candidate(selected_ids[0], 'accepted', 'saved before outage')
            if len(calls) <= 2:
                raise self.outage()
            for identifier in selected_ids:
                saved.append(identifier)
                on_candidate(identifier, 'accepted', 'saved after recovery')
        job = self.jobs(worker).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['processed']), ('completed', 2))
        self.assertEqual(calls, [[101, 102], [102], [102]])
        self.assertEqual(saved, [101, 102])
        self.assertEqual(sum(self.waited), 180)
        self.assertTrue(all(j['status'] == 'retry_wait' and j['processed'] == 1 for j in self.wait_states))
        self.assertEqual([r['delay_seconds'] for r in job['recovery']['history']], [60, 120])
        self.assertEqual(job['recovery']['consecutive_failures'], 0)
        self.assertFalse(job['errors'])

    def test_unexpected_coordinator_abort_retries_without_failing_untouched_candidates(self):
        attempts = []
        extract = oss_workflow.extract_groups
        def interrupted_once(*args, **kwargs):
            attempts.append(1)
            if len(attempts) == 1:
                raise RuntimeError('private upstream detail must not enter public job errors')
            return extract(*args, **kwargs)
        def worker(store, leaf, run, **kwargs):
            return discover_open_leaf(store, leaf, run, github=SearchSource(), model=PartialModel(), root=self.root, **kwargs)
        with patch('oss_workflow.extract_groups', side_effect=interrupted_once):
            job = self.jobs(worker).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['processed']), ('completed', 2))
        self.assertEqual(len(attempts), 2)
        self.assertEqual(sum(self.waited), 60)
        self.assertEqual(job['recovery']['component'], 'workflow')
        self.assertEqual(job['recovery']['code'], 'workflow_interrupted')
        self.assertIn('RuntimeError', job['recovery']['history'][0]['error'])
        self.assertNotIn('private upstream detail', json.dumps(job))
        self.assertTrue(all(t['status'] != 'failed' for t in job['targets']['feed-reader']))
        self.assertEqual(len(self.store.catalog('feed-reader')['projects']), 2)

    def test_markdown_regex_is_not_mistaken_for_an_html_declaration_or_lost(self):
        source = '<b>Username</b> expression: /(?<![_.])$/ &amp; more text'
        self.assertEqual(plain_text(source), 'Username expression: /(?<![_.])$/ & more text')
        github = SearchSource()
        original = github.get
        def get(path):
            if path == '/repos/test/demo-101/readme':
                return file_data('test/demo-101', 'README.md', source)
            return original(path)
        github.get = get
        def worker(store, leaf, run, **kwargs):
            return discover_open_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, **kwargs)
        job = self.jobs(worker).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['processed']), ('completed', 2))
        self.assertNotIn('recovery', job)
        self.assertEqual(len(self.store.catalog('feed-reader')['projects']), 2)
        card = self.store.previous('test/demo-101', 'feed-reader')
        self.assertTrue(card['summary_evidence']['source_sha256'])
        self.assertIn('git/blobs/', card['summary_evidence']['immutable_url'])

    def test_supervisor_repairs_legacy_abort_only_and_preserves_saved_siblings_and_history(self):
        def legacy_worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                reason = 'already saved' if identifier == 101 else '本批中断，进度已保存'
                state = 'partial' if identifier == 101 else 'failed'
                store.candidate_result(leaf, identifier, state, reason)
                on_candidate(identifier, state, reason)
            run['errors'].append({'error': '本批中断，进度已保存'})
        original = self.jobs(legacy_worker).create(['feed-reader'], existing_only=True)
        self.assertEqual(original['status'], 'partial')
        requested = []
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            requested.extend(selected_ids)
            for identifier in selected_ids:
                store.candidate_result(leaf, identifier, 'partial', 'recovered')
                on_candidate(identifier, 'partial', 'recovered')
        service = BatchRecoveryService(self.store, self.jobs(finish, cls=InlineJobs))
        service.tick()
        result = service.jobs.get(original['id'])
        self.assertEqual((result['id'], result['status'], result['processed']), (original['id'], 'completed', 2))
        self.assertEqual(requested, [102])
        self.assertFalse(result['errors'])
        self.assertEqual(result['resolved_errors'][0]['error'], '本批中断，进度已保存')
        self.assertEqual(result['restored_interruptions'][0]['targets'], [{'leaf': 'feed-reader', 'repository_id': 102}])
        self.assertEqual(result['targets']['feed-reader'][0], original['targets']['feed-reader'][0])
        with patch.object(service.jobs, 'launch', side_effect=AssertionError('do not replay a repaired job')):
            self.assertFalse(service.tick()['started'])

    def test_supervisor_does_not_reopen_ordinary_failed_candidates_or_partial_cards(self):
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                on_candidate(identifier, 'failed' if identifier == 102 else 'partial', 'single unavailable resource')
        jobs = self.jobs(worker, cls=InlineJobs)
        job = jobs.create(['feed-reader'], existing_only=True)
        service = BatchRecoveryService(self.store, jobs)
        with patch.object(jobs, 'launch', side_effect=AssertionError('ordinary failures remain terminal')):
            self.assertFalse(service.tick()['started'])
            self.assertEqual(jobs.resume(job['id'])['status'], 'partial')

    def test_exponential_wait_caps_at_15_minutes_but_honors_longer_retry_after(self):
        jobs = self.jobs(lambda *a, **kw: None)
        job = {'id': 'fixture', 'status': 'running'}
        for _ in range(7):
            jobs.schedule_recovery(job, self.outage())
        self.assertEqual([h['delay_seconds'] for h in job['recovery']['history']], [60, 120, 240, 480, 900, 900, 900])
        jobs.schedule_recovery(job, self.outage(3600))
        self.assertEqual(job['recovery']['delay_seconds'], 3600)
        self.assertEqual(datetime.fromisoformat(job['recovery']['next_retry_at']).timestamp(), self.wall + 3600)

    def test_permanent_credentials_or_quota_require_attention_without_cooldown(self):
        for code in ['unauthorized', 'no_credential', 'bad_endpoint', 'quota_exhausted', 'model_unavailable']:
            with self.subTest(code=code):
                def worker(*a, **kw):
                    raise ModelServiceUnavailable('requires configuration or funds', code=code)
                job = self.jobs(worker).create(['feed-reader'], existing_only=True)
                self.assertEqual(job['status'], 'paused_model')
                self.assertNotIn('recovery', job)
                self.assertFalse(self.waited)
                supervisor = BatchRecoveryService(self.store, self.jobs(worker, cls=InlineJobs))
                self.assertFalse(supervisor.tick()['started'])

    def test_scene_preparation_recovers_without_skipping_or_duplicating_leaf(self):
        calls = []
        def prepare(*a, **kw):
            calls.append(1)
            if len(calls) < 3:
                raise self.outage()
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                on_candidate(identifier, 'accepted', 'done')
        job = self.jobs(worker, prepare).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['prepared'], job['processed']), ('completed', ['feed-reader'], 2))
        self.assertEqual(len(calls), 3)
        self.assertEqual(job['leaf_errors'], {})

    def test_temporary_github_failure_preserves_successful_sibling_and_unfinished_candidate(self):
        github = SearchSource()
        original = github.get
        checked = []
        def get(path):
            if path == '/repositories/101':
                checked.append(path)
                if len(checked) == 1:
                    raise GitHubServiceUnavailable('GitHub temporarily rate limited', retryable=True,
                                                   retry_after=120, code='github_rate_limited')
            return original(path)
        github.get = get
        def worker(store, leaf, run, **kwargs):
            return discover_open_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, **kwargs)
        job = self.jobs(worker).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['processed']), ('completed', 2))
        self.assertEqual(job['recovery']['component'], 'github')
        self.assertEqual(sum(self.waited), 120)
        self.assertTrue(all(j['processed'] == 1 for j in self.wait_states))
        self.assertEqual(len(self.store.catalog('feed-reader')['projects']), 2)
        self.assertFalse(any(i['status'] == 'failed' for i in job['targets']['feed-reader']))

    def test_github_search_outage_waits_without_marking_the_leaf_prepared_or_skipped(self):
        github = SearchSource()
        original = github.get
        attempts = []
        def get(path):
            if path.startswith('/search/'):
                attempts.append(path)
                if len(attempts) == 1:
                    raise GitHubServiceUnavailable('temporary search limit', retryable=True,
                                                   retry_after=90, code='github_rate_limited')
            return original(path)
        github.get = get
        def prepare(store, leaf, run, **kwargs):
            return prepare_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, search=True)
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                on_candidate(identifier, 'accepted', 'done')
        job = self.jobs(worker, prepare).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['prepared']), ('completed', ['feed-reader']))
        self.assertEqual(sum(self.waited), 90)
        self.assertTrue(all(not j['prepared'] for j in self.wait_states))
        self.assertFalse(job['leaf_errors'])

    def test_github_auth_failure_does_not_discard_candidates_or_make_placeholder_cards(self):
        github = SearchSource()
        github.get = lambda path: (_ for _ in ()).throw(GitHubServiceUnavailable('GitHub Token invalid', code='github_unauthorized'))
        def worker(store, leaf, run, **kwargs):
            return discover_open_leaf(store, leaf, run, github=github, model=PartialModel(), root=self.root, **kwargs)
        job = self.jobs(worker).create(['feed-reader'], existing_only=True)
        self.assertEqual((job['status'], job['processed']), ('paused_model', 0))
        self.assertFalse(self.store.catalog('feed-reader')['projects'])
        self.assertTrue(all(c['status'] == 'pending' for c in self.store.candidates('feed-reader')))

    def test_restart_in_cooldown_is_resumed_by_supervisor_without_a_browser_request(self):
        saved = []
        def failed(store, leaf, run, selected_ids, search, on_candidate):
            saved.append(selected_ids[0])
            on_candidate(selected_ids[0], 'accepted', 'saved')
            raise self.outage(120)
        def crash(seconds):
            self.wall += seconds
            raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):
            self.jobs(failed, waiter=crash).create(['feed-reader'], existing_only=True)
        with self.store.connect() as con:
            before = json.loads(con.execute('SELECT data FROM oss_batch_job').fetchone()[0])
        self.assertEqual((before['status'], before['processed']), ('interrupted', 1))
        requested = []
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            requested.extend(selected_ids)
            for identifier in selected_ids:
                saved.append(identifier)
                on_candidate(identifier, 'accepted', 'recovered')
        service = BatchRecoveryService(self.store, self.jobs(finish, cls=InlineJobs))
        service.tick()
        after = service.jobs.get(before['id'])
        self.assertEqual((after['status'], after['processed']), ('completed', 2))
        self.assertEqual(requested, [102])
        self.assertEqual(saved, [101, 102])
        self.assertEqual(sum(self.waited), 105)  # Remaining deadline survived the restart.

    def test_supervisor_does_not_launch_a_duplicate_worker_under_the_refresh_lock(self):
        jobs = self.jobs(lambda *a, **kw: None)
        with patch.object(jobs, 'launch', side_effect=lambda job, lock, background: (lock.close(), job)[1]):
            job = jobs.create(['feed-reader'], existing_only=True)
        called = []
        def finish(store, leaf, run, selected_ids, search, on_candidate):
            called.append(1)
            for identifier in selected_ids:
                on_candidate(identifier, 'accepted', 'done')
        service = BatchRecoveryService(self.store, self.jobs(finish, cls=InlineJobs))
        lock = self.store._lock()
        try:
            service.tick()
            self.assertFalse(called)
        finally:
            lock.close()
        service.tick()
        self.assertEqual(len(called), 1)
        self.assertEqual(service.jobs.get(job['id'])['status'], 'completed')

    def test_supervisor_rechecks_permanent_pause_after_a_stale_status_read(self):
        jobs = self.jobs(lambda *a, **kw: None)
        with patch.object(jobs, 'launch', side_effect=lambda job, lock, background: (lock.close(), job)[1]):
            job = jobs.create(['feed-reader'], existing_only=True)
        job['status'] = 'paused_model'
        jobs.save(job)
        with patch.object(jobs, 'launch', side_effect=AssertionError('must not resume an auth pause')):
            result = jobs.resume(job['id'], automatic=True)
        self.assertEqual(result['status'], 'paused_model')

    def test_supervisor_survives_an_unexpected_tick_failure(self):
        service = BatchRecoveryService(self.store)
        def finish():
            service.stop.set()
        attempts = []
        def tick():
            attempts.append(1)
            if len(attempts) == 1:
                raise RuntimeError('temporary store error')
            finish()
        with patch.object(service, 'tick', side_effect=tick), patch.object(service.stop, 'wait', return_value=False):
            service.run()
        self.assertTrue(service.stop.is_set())
        self.assertIn('temporary store error', service.health_path.read_text())

    def test_manual_retry_wakes_the_existing_waiter_instead_of_creating_a_second_worker(self):
        waiting, done, finished = threading.Event(), threading.Event(), threading.Event()
        calls = []
        jobs = None
        def wait(seconds):
            waiting.set()
            return jobs.wake.wait(seconds)
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            calls.append(selected_ids)
            if len(calls) == 1:
                raise self.outage()
            for identifier in selected_ids:
                on_candidate(identifier, 'accepted', 'done')
            done.set()
        jobs = self.jobs(worker, waiter=wait)
        execute = jobs.execute
        def observed(job, lock):
            try:
                return execute(job, lock)
            finally:
                finished.set()
        with patch.object(jobs, 'execute', side_effect=observed):
            job = jobs.create(['feed-reader'], existing_only=True, background=True)
            self.assertTrue(waiting.wait(3))
            BatchJobs(self.store).resume(job['id'], background=True)
            self.assertTrue(done.wait(3))
            self.assertTrue(finished.wait(3))
        self.assertEqual(len(calls), 2)
        self.assertEqual(jobs.get(job['id'])['status'], 'completed')
