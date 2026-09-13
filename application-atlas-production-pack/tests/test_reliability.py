import concurrent.futures
from contextlib import closing, redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np

CODE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CODE))
import atlas_runtime as rt
import classify as classifier
import draft_new
import gate_check
import promote_draft as promote
from atlas_sources import SourceError, read_source, source_manifest
from opencode_client import OpenCodeClient, iter_sse
from execution_state import project_execution
from project_store import ProjectStore, ProjectStoreError
from handoff_bundle import build_handoff, validate_handoff, write_handoff
from sample_package import validate_package
from workspace_snapshot import compare_snapshots, snapshot_workspace
from review_store import fingerprint, corpus_revision, update_review, load_review


class SourceReadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.pack = Path(self.temp.name)
        (self.pack / 'applications').mkdir()
        (self.pack / 'research').mkdir()
        self.application = '# Sample\nIntro\n\n## Core Model\nCore text\n\n### Detail\nNested text\n\n## Rules\nRule text\n'
        self.research = '## Boundary Findings\n\n### vs Other\nBoundary detail\n\n## Uncertainties\nUnknown\n'
        (self.pack / 'applications/sample.md').write_text(self.application)
        (self.pack / 'research/sample.md').write_text(self.research)

    def test_manifest_reports_both_sources_with_stable_outlines(self):
        result = source_manifest('sample', self.pack)
        self.assertEqual([item['kind'] for item in result['sources']], ['application', 'research'])
        research = result['sources'][1]
        self.assertEqual(research['outline'][0]['id'], 'boundary-findings')
        self.assertEqual(research['outline'][1]['id'], 'vs-other')
        self.assertEqual(len(research['fingerprint']), 64)

    def test_heading_read_includes_nested_sections_and_stops_at_peer(self):
        result = read_source('sample', 'application', 'core-model', pack=self.pack)
        self.assertTrue(result['complete'])
        self.assertIn('### Detail', result['content'])
        self.assertNotIn('## Rules', result['content'])
        self.assertEqual(result['line_start'], 4)

    def test_pagination_never_hides_truncation(self):
        first = read_source('sample', 'research', limit=24, pack=self.pack)
        self.assertFalse(first['complete'])
        self.assertEqual(first['next_offset'], first['returned_chars'])
        second = read_source('sample', 'research', offset=first['next_offset'], limit=500, pack=self.pack)
        self.assertTrue(second['complete'])
        self.assertEqual(first['content'] + second['content'], self.research)
        self.assertEqual(first['fingerprint'], second['fingerprint'])

    def test_invalid_paths_and_offsets_fail_closed(self):
        with self.assertRaises(SourceError):
            read_source('../sample', 'application', pack=self.pack)
        with self.assertRaises(SourceError):
            read_source('sample', 'other', pack=self.pack)
        with self.assertRaises(SourceError):
            read_source('sample', 'application', offset=10000, pack=self.pack)


class OpenCodeClientTests(unittest.TestCase):
    class Response:
        def __init__(self, value):
            self.value = value
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def read(self):
            return json.dumps(self.value).encode()

    def setUp(self):
        self.requests = []
        self.responses = []
        def opener(request, timeout):
            self.requests.append((request, timeout))
            return self.Response(self.responses.pop(0))
        self.client = OpenCodeClient('http://127.0.0.1:4098', '/tmp/project', opener=opener)

    def test_client_scopes_session_requests_to_directory(self):
        self.responses.append({'id': 'ses_abc'})
        result = self.client.create_session('Probe')
        request, _ = self.requests[0]
        self.assertEqual(result['id'], 'ses_abc')
        self.assertIn('directory=%2Ftmp%2Fproject', request.full_url)
        self.assertEqual(json.loads(request.data), {'title': 'Probe'})

    def test_reconcile_reads_authoritative_endpoints_and_filters_permissions(self):
        self.responses.extend([
            {'ses_abc': {'type': 'busy'}},
            {'id': 'ses_abc'},
            [{'info': {'id': 'msg_one'}, 'parts': []}],
            [],
            [{'id': 'per_one', 'sessionID': 'ses_abc'}, {'id': 'per_two', 'sessionID': 'ses_other'}],
        ])
        result = self.client.reconcile('ses_abc')
        self.assertEqual(result['status']['type'], 'busy')
        self.assertEqual([item['id'] for item in result['pending_permissions']], ['per_one'])
        self.assertEqual(result['engine_diff'], [])

    def test_permission_reply_uses_current_nondeprecated_endpoint(self):
        self.responses.append(True)
        self.assertTrue(self.client.reply_permission('per_abc', 'once'))
        request, _ = self.requests[0]
        self.assertIn('/permission/per_abc/reply', request.full_url)
        self.assertEqual(json.loads(request.data), {'reply': 'once'})

    def test_async_message_uses_nonblocking_endpoint(self):
        self.responses.append(None)
        self.assertIsNone(self.client.send_message_async(
            'ses_abc', 'Run tests', 'opencode', 'big-pickle', tools={'bash': True}))
        request, _ = self.requests[0]
        self.assertIn('/session/ses_abc/prompt_async', request.full_url)
        self.assertEqual(json.loads(request.data)['tools'], {'bash': True})

    def test_sse_parser_and_session_filter(self):
        raw = io.BytesIO(
            b'data: {"type":"server.connected","properties":{}}\n\n'
            b'data: {"type":"session.status","properties":{"sessionID":"ses_abc"}}\n\n'
            b'data: {"type":"session.status","properties":{"sessionID":"ses_other"}}\n\n')
        events = list(self.client.events(raw, 'ses_abc'))
        self.assertEqual([event['type'] for event in events], ['server.connected', 'session.status'])
        self.assertEqual(len(list(iter_sse(io.BytesIO(b'data: {"ok":true}\n\n')))), 1)

    def test_rejects_remote_servers_and_invalid_ids(self):
        with self.assertRaises(ValueError):
            OpenCodeClient('https://example.com', '/tmp/project')
        with self.assertRaises(ValueError):
            self.client.get_session('../bad')


class WorkspaceSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'keep.txt').write_text('before')
        (self.root / 'remove.txt').write_text('remove')
        (self.root / 'node_modules').mkdir()
        (self.root / 'node_modules/ignored.js').write_text('large dependency')

    def test_detects_added_removed_and_modified_files(self):
        before = snapshot_workspace(self.root)
        (self.root / 'keep.txt').write_text('after')
        (self.root / 'remove.txt').unlink()
        (self.root / 'added.txt').write_text('new')
        after = snapshot_workspace(self.root)
        diff = compare_snapshots(before, after)
        self.assertEqual(diff['added'], ['added.txt'])
        self.assertEqual(diff['removed'], ['remove.txt'])
        self.assertEqual(diff['modified'], ['keep.txt'])
        self.assertTrue(diff['changed'])
        self.assertNotIn('node_modules/ignored.js', before['files'])

    def test_unchanged_content_is_not_modified(self):
        before = snapshot_workspace(self.root)
        os.utime(self.root / 'keep.txt', None)
        after = snapshot_workspace(self.root)
        self.assertFalse(compare_snapshots(before, after)['changed'])

    def test_symlink_target_is_recorded_without_following_it(self):
        try:
            (self.root / 'link').symlink_to('keep.txt')
        except OSError:
            self.skipTest('symlinks unavailable')
        result = snapshot_workspace(self.root)
        self.assertEqual(result['files']['link']['kind'], 'symlink')
        self.assertEqual(result['files']['link']['target'], 'keep.txt')

    def test_different_roots_cannot_be_compared(self):
        before = snapshot_workspace(self.root)
        with tempfile.TemporaryDirectory() as other:
            after = snapshot_workspace(other)
        with self.assertRaises(ValueError):
            compare_snapshots(before, after)


class ExecutionStateTests(unittest.TestCase):
    def test_permission_has_precedence_over_busy(self):
        result = project_execution({
            'status': {'type': 'busy'},
            'messages': [{'info': {'id': 'msg_assistant', 'parentID': 'msg_user', 'role': 'assistant'}}],
            'pending_permissions': [{'id': 'per_one', 'tool': {'messageID': 'msg_assistant'}}],
        }, 'msg_user')
        self.assertEqual(result['state'], 'waiting_permission')
        self.assertEqual(result['evidence']['permission_id'], 'per_one')

    def test_completed_requires_a_completed_stop_message(self):
        result = project_execution({
            'status': {'type': 'idle'},
            'messages': [{'info': {
                'id': 'msg_answer', 'parentID': 'msg_user', 'role': 'assistant',
                'finish': 'stop', 'time': {'completed': 123},
            }}],
        }, 'msg_user')
        self.assertEqual(result['state'], 'completed')
        self.assertEqual(result['evidence']['message_id'], 'msg_answer')

    def test_idle_alone_is_not_completion(self):
        result = project_execution({'status': {'type': 'idle'}, 'messages': []}, 'msg_missing')
        self.assertEqual(result['state'], 'queued')

    def test_abort_and_other_errors_are_distinct(self):
        base = {'status': {'type': 'idle'}, 'messages': [{'info': {
            'id': 'msg_answer', 'parentID': 'msg_user', 'role': 'assistant',
            'error': {'name': 'MessageAbortedError'},
        }}]}
        self.assertEqual(project_execution(base, 'msg_user')['state'], 'stopped')
        base['messages'][0]['info']['error'] = {'name': 'ProviderError'}
        self.assertEqual(project_execution(base, 'msg_user')['state'], 'failed')

    def test_unrelated_permission_does_not_capture_task(self):
        result = project_execution({
            'status': {'type': 'busy'},
            'messages': [{'info': {'id': 'msg_answer', 'parentID': 'msg_user', 'role': 'assistant'}}],
            'pending_permissions': [{'id': 'per_other', 'tool': {'messageID': 'msg_other'}}],
        }, 'msg_user')
        self.assertEqual(result['state'], 'running')


class ProjectStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = ProjectStore(self.root / 'state/projects.sqlite')
        self.project = self.store.create_project(
            'Pilot', 'Build the approved pilot', self.root / 'workspace', 'new')

    def test_project_data_is_separate_and_persistent(self):
        self.assertTrue((self.root / 'state/projects.sqlite').exists())
        reopened = ProjectStore(self.root / 'state/projects.sqlite')
        self.assertEqual(reopened.get_project(self.project['id'])['objective'],
                         'Build the approved pilot')
        self.assertEqual(reopened.list_projects()[0]['id'], self.project['id'])

    def test_empty_workspace_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'workspace'):
            self.store.create_project('Invalid', 'No workspace', '  ', 'existing')
        generated = self.store.create_project('Idea', 'Start with an idea', '', 'new')
        self.assertTrue(generated['workspace'].endswith('/workspaces/' + generated['id']))

    def test_version_one_store_migrates_without_losing_tasks(self):
        path = self.root / 'legacy.sqlite'
        with sqlite3.connect(path) as con:
            con.executescript('''
                CREATE TABLE project (
                    id TEXT PRIMARY KEY, name TEXT NOT NULL, objective TEXT NOT NULL,
                    workspace TEXT NOT NULL, mode TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE task (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    title TEXT NOT NULL, objective TEXT NOT NULL, execution_status TEXT NOT NULL,
                    acceptance_status TEXT NOT NULL, acceptance_evidence_json TEXT NOT NULL,
                    input_versions_json TEXT NOT NULL, requirement_ids_json TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                INSERT INTO project VALUES
                    ('prj_legacy','Legacy','Keep state','/tmp/legacy','existing','now','now');
                INSERT INTO task VALUES
                    ('tsk_legacy','prj_legacy','Task','Do it','planned','pending','[]','[]','[]','now','now');
                PRAGMA user_version=1;
            ''')
        migrated = ProjectStore(path)
        self.assertEqual(migrated.get_task('tsk_legacy')['title'], 'Task')
        self.assertIsNone(migrated.get_task('tsk_legacy')['iteration_id'])
        with sqlite3.connect(path) as con:
            self.assertEqual(con.execute('PRAGMA user_version').fetchone()[0], 2)

    def test_document_versions_are_immutable_and_conflicts_are_explicit(self):
        document = self.store.create_document(
            self.project['id'], 'product-requirements', 'PRD', 'version one',
            [{'source': 'application/sample.md', 'fingerprint': 'abc'}])
        updated = self.store.add_document_version(
            document['id'], 'version two', expected_current_version=1)
        self.assertEqual(updated['current_version'], 2)
        self.assertEqual(updated['content'], 'version two')
        with self.assertRaises(ProjectStoreError):
            self.store.add_document_version(
                document['id'], 'stale update', expected_current_version=1)

    def test_task_inputs_must_belong_to_same_project(self):
        other = self.store.create_project('Other', 'Other goal', self.root / 'other', 'existing')
        document = self.store.create_document(other['id'], 'plan', 'Plan', 'content')
        with self.assertRaises(ProjectStoreError):
            self.store.create_task(self.project['id'], 'Implement', 'Do work',
                                   [document['version_id']])

    def test_ai_scope_recommendation_is_not_user_confirmation(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas', 'applications/sample.md', 'sha256:abc',
            locator='core-model', read_status='reviewed')
        requirement = self.store.create_requirement(
            self.project['id'], 'Export the current project state', 'current',
            'Useful for recovery', ['The bundle validates offline'], [reference['id']])
        self.assertEqual(requirement['recommended_scope'], 'current')
        self.assertIsNone(requirement['confirmed_scope'])
        task = self.store.create_task(
            self.project['id'], 'Export', 'Build export', requirement_ids=[requirement['id']])
        with self.assertRaises(ProjectStoreError):
            self.store.create_execution(task['id'], 'opencode', 'ses_example')
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved for this release')
        self.assertEqual(
            self.store.create_execution(task['id'], 'opencode', 'ses_example')['status'], 'queued')

    def test_decisions_and_references_cannot_cross_projects(self):
        other = self.store.create_project('Other', 'Other goal', self.root / 'other', 'existing')
        reference = self.store.add_reference(
            other['id'], 'user', 'interview-1', 'v1', excerpt='Need local execution')
        with self.assertRaises(ProjectStoreError):
            self.store.record_decision(
                self.project['id'], 'Use local execution', 'User constraint', [reference['id']])

    def test_references_are_unique_editable_and_project_scoped(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'sha256:one',
            locator='core-model', excerpt='Fixed source text', read_status='read')
        self.assertEqual(self.store.list_references(self.project['id'])[0]['id'], reference['id'])
        with self.assertRaisesRegex(ProjectStoreError, 'already saved'):
            self.store.add_reference(
                self.project['id'], 'atlas:application', 'sample', 'sha256:one',
                locator='core-model', excerpt='Client cannot replace it')
        updated = self.store.update_reference(
            self.project['id'], reference['id'], note='Use this boundary', read_status='reviewed')
        self.assertEqual(updated['note'], 'Use this boundary')
        self.assertEqual(updated['read_status'], 'reviewed')
        other = self.store.create_project('Other', 'Other goal', self.root / 'other', 'existing')
        with self.assertRaises(ProjectStoreError):
            self.store.get_reference(other['id'], reference['id'])
        with self.assertRaises(ProjectStoreError):
            self.store.update_reference(other['id'], reference['id'], note='Wrong project')
        import drafts_api
        external = self.store.add_reference(
            self.project['id'], 'user', 'interview-1', 'notes-v1', excerpt='User evidence')
        projected = drafts_api.list_project_references(
            self.project['id'], self.store, self.root / 'missing-pack')
        external_projection = next(item for item in projected if item['id'] == external['id'])
        self.assertFalse(external_projection['stale'])

    def test_atlas_reference_keeps_excerpt_and_reports_source_update(self):
        import drafts_api
        pack = self.root / 'pack'
        (pack / 'applications').mkdir(parents=True)
        (pack / 'research').mkdir()
        application = '# Sample\nIntro\n\n## Core Model\nCore text\n\n### Detail\nNested text\n\n## Rules\nRule text\n'
        (pack / 'applications/sample.md').write_text(application)
        saved = drafts_api.collect_atlas_reference(self.project['id'], {
            'kind': 'application', 'slug': 'sample', 'section': 'core-model',
            'note': 'Initial note',
        }, self.store, pack)
        self.assertIn('### Detail', saved['excerpt'])
        self.assertNotIn('## Rules', saved['excerpt'])
        self.assertEqual(saved['locator'], 'core-model')
        original_excerpt, original_version = saved['excerpt'], saved['source_version']
        current = drafts_api.list_project_references(self.project['id'], self.store, pack)[0]
        self.assertFalse(current['stale'])
        (pack / 'applications/sample.md').write_text(application + '\n## New Evidence\nChanged\n')
        stale = drafts_api.list_project_references(self.project['id'], self.store, pack)[0]
        self.assertTrue(stale['stale'])
        self.assertNotEqual(stale['current_version'], original_version)
        self.assertEqual(stale['excerpt'], original_excerpt)

    def test_app_catalog_reference_declares_depth_and_tracks_its_record(self):
        import drafts_api
        pack = self.root / 'pack'
        pack.mkdir()
        apps = [{
            'slug': 'sample-app', 'name': 'Sample App', 'aliases': ['Sample'],
            'vendor': 'Example', 'tagline': 'Keeps a sample record.',
            'tasks': ['capture', 'review'],
        }]
        classified = [{
            'slug': 'sample-app', 'desc': 'Sample App description',
            'leaf': 'sample-type', 'scores': {'sample-type': 10},
        }]
        (pack / 'mvp_apps.json').write_text(json.dumps(apps))
        (pack / 'mvp_apps_classified.json').write_text(json.dumps(classified))
        saved = drafts_api.collect_atlas_reference(self.project['id'], {
            'kind': 'app', 'slug': 'sample-app', 'note': 'Compare its capture flow',
        }, self.store, pack)
        self.assertEqual(saved['source_kind'], 'atlas:app')
        self.assertIn('Catalog-level evidence only', saved['excerpt'])
        self.assertIn('sample-type', saved['excerpt'])
        projected = drafts_api.list_project_references(
            self.project['id'], self.store, pack)[0]
        self.assertFalse(projected['stale'])
        original_excerpt = projected['excerpt']
        apps[0]['tagline'] = 'Updated catalog description.'
        (pack / 'mvp_apps.json').write_text(json.dumps(apps))
        stale = drafts_api.list_project_references(
            self.project['id'], self.store, pack)[0]
        self.assertTrue(stale['stale'])
        self.assertEqual(stale['excerpt'], original_excerpt)
        with self.assertRaisesRegex(ValueError, 'do not have sections'):
            drafts_api.collect_atlas_reference(self.project['id'], {
                'kind': 'app', 'slug': 'sample-app', 'section': 'details',
            }, self.store, pack)

    def test_execution_updates_task_and_keeps_raw_projection(self):
        document = self.store.create_document(self.project['id'], 'plan', 'Plan', 'content')
        task = self.store.create_task(self.project['id'], 'Implement', 'Do work',
                                      [document['version_id']])
        snapshot = self.store.save_snapshot(self.project['id'], {
            'schema': 1, 'root': str(self.root / 'workspace'), 'files': {}, 'errors': []},
            'before', task['id'])
        execution = self.store.create_execution(task['id'], 'opencode', 'ses_example', snapshot['id'])
        projection = {'state': 'waiting_permission', 'engine_status': 'busy',
                      'evidence': {'permission_id': 'per_example'}}
        updated = self.store.update_execution(execution['id'], projection, 'msg_example')
        self.assertEqual(updated['raw_state'], projection)
        stored_task = self.store.get_task(task['id'])
        self.assertEqual(stored_task['execution_status'], 'waiting_permission')
        self.assertEqual(stored_task['acceptance_status'], 'pending')

    def test_execution_completion_does_not_imply_acceptance(self):
        task = self.store.create_task(self.project['id'], 'Implement', 'Do work')
        execution = self.store.create_execution(task['id'], 'opencode', 'ses_example')
        self.store.update_execution(execution['id'], {
            'state': 'completed', 'engine_status': 'idle',
            'evidence': {'message_id': 'msg_answer'},
        })
        task = self.store.get_task(task['id'])
        self.assertEqual(task['execution_status'], 'completed')
        self.assertEqual(task['acceptance_status'], 'pending')
        accepted = self.store.record_acceptance(
            task['id'], 'passed', [{'kind': 'test', 'summary': '42 tests passed'}])
        self.assertEqual(accepted['acceptance_status'], 'passed')

    def test_iteration_freezes_scope_and_allows_only_one_active_iteration(self):
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep exported state portable', 'current', 'Recovery')
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        document = self.store.create_document(self.project['id'], 'plan', 'Plan', 'version one')
        iteration = self.store.create_iteration(
            self.project['id'], 'Iteration one', 'Ship portable state',
            [document['version_id']], [requirement['id']])
        newer = self.store.add_document_version(document['id'], 'version two')
        with self.assertRaises(ProjectStoreError):
            self.store.create_task(
                self.project['id'], 'Use new plan', 'Out of scope', [newer['version_id']],
                [requirement['id']], iteration['id'])
        task = self.store.create_task(
            self.project['id'], 'Use fixed plan', 'In scope', [document['version_id']],
            [requirement['id']], iteration['id'])
        self.assertEqual(task['iteration_id'], iteration['id'])
        with self.assertRaises(ProjectStoreError):
            self.store.create_iteration(
                self.project['id'], 'Another active iteration', 'Must wait',
                [document['version_id']], [requirement['id']])

    def test_iteration_completion_requires_task_acceptance(self):
        iteration = self.store.create_iteration(
            self.project['id'], 'Iteration one', 'Complete one task', [], [])
        task = self.store.create_task(
            self.project['id'], 'Implement', 'Do work', iteration_id=iteration['id'])
        with self.assertRaises(ProjectStoreError):
            self.store.update_iteration_status(iteration['id'], 'completed')
        self.store.record_acceptance(task['id'], 'passed', [{'kind': 'review', 'summary': 'Accepted'}])
        completed = self.store.update_iteration_status(iteration['id'], 'completed')
        self.assertEqual(completed['status'], 'completed')
        self.assertIsNotNone(completed['completed_at'])

    def test_failed_transaction_does_not_leave_partial_task(self):
        with self.assertRaises(ProjectStoreError):
            self.store.create_task(self.project['id'], 'Implement', 'Do work', ['dver_missing'])
        with sqlite3.connect(self.store.path) as con:
            self.assertEqual(con.execute('SELECT count(*) FROM task').fetchone()[0], 0)

    def test_handoff_uses_fixed_inputs_and_flags_missing_recovery_evidence(self):
        reference = self.store.add_reference(
            self.project['id'], 'user', 'approved-brief', 'v1', excerpt='Keep user edits')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep user edits', 'current', 'Required by the brief',
            ['Existing prose remains'], [reference['id']])
        self.store.confirm_requirement(requirement['id'], 'current', 'User approved')
        self.store.record_decision(
            self.project['id'], 'Use a replaceable execution backend',
            'Preserve Atlas-owned state', [reference['id']])
        document = self.store.create_document(
            self.project['id'], 'product-requirements', 'PRD', 'Must keep user edits')
        iteration = self.store.create_iteration(
            self.project['id'], 'Portable handoff', 'Preserve accepted intent',
            [document['version_id']], [requirement['id']])
        task = self.store.create_task(
            self.project['id'], 'Implement', 'Implement the accepted scope',
            [document['version_id']], [requirement['id']], iteration['id'])
        before = self.store.save_snapshot(self.project['id'], {
            'schema': 1, 'root': str(self.root / 'workspace'), 'files': {}, 'errors': []},
            'before', task['id'])
        execution = self.store.create_execution(task['id'], 'opencode', 'ses_unavailable', before['id'])
        self.store.update_execution(execution['id'], {
            'state': 'stopped', 'engine_status': 'idle',
            'evidence': {'error': 'MessageAbortedError'},
        })
        bundle = build_handoff(self.store, task['id'])
        self.assertFalse(bundle['recovery']['old_engine_session_required'])
        self.assertEqual(bundle['documents'][0]['version_id'], document['version_id'])
        self.assertEqual(bundle['iteration']['id'], iteration['id'])
        self.assertEqual(bundle['requirements'][0]['confirmed_scope'], 'current')
        self.assertEqual(len(bundle['decisions']), 1)
        self.assertIn('workspace snapshot after execution', bundle['recovery']['missing'])
        self.assertTrue(validate_handoff(bundle)['valid'])
        bundle['documents'][0]['content'] = 'tampered'
        self.assertFalse(validate_handoff(bundle)['valid'])
        written = write_handoff(self.store, task['id'], self.root / 'handoff')
        markdown = Path(written['markdown_path']).read_text()
        self.assertIn('Must keep user edits', markdown)
        self.assertIn('do not replay prior operations blindly', markdown)

    def test_project_http_create_list_get_and_validation(self):
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        body = {
            'name': 'Existing code', 'objective': 'Improve it',
            'workspace': str(self.root / 'existing'), 'mode': 'existing',
        }
        handler.path = '/api/projects'
        handler._body = lambda: body
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            created, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertTrue(created['id'].startswith('prj_'))

        handler.path = '/api/projects'
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            projects, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual({item['id'] for item in projects}, {self.project['id'], created['id']})

        handler.path = '/api/projects/' + created['id']
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            opened, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual(opened['mode'], 'existing')

        handler.path = '/api/projects'
        handler._body = lambda: {'name': 'bad'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            invalid, code = handler.do_POST()
        self.assertEqual(code, 400)
        self.assertIn('objective', invalid['error'])

        handler._body = lambda: {
            'name': 'Idea only', 'objective': 'Explore the idea', 'mode': 'new'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            idea, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertTrue(idea['workspace'].endswith('/workspaces/' + idea['id']))

    def test_project_reference_http_create_list_and_update(self):
        import drafts_api
        pack = self.root / 'pack'
        (pack / 'applications').mkdir(parents=True)
        (pack / 'research').mkdir()
        (pack / 'applications/sample.md').write_text(
            '# Sample\n\n## Core Model\nCanonical evidence\n')
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)
        handler.path = f"/api/projects/{self.project['id']}/references"
        handler._body = lambda: {
            'kind': 'application', 'slug': 'sample', 'section': 'core-model',
            'note': 'Read during discovery',
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
                patch.object(drafts_api, 'PACK', str(pack)):
            created, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertEqual(created['excerpt'], '## Core Model\nCanonical evidence\n')

        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
                patch.object(drafts_api, 'PACK', str(pack)):
            rows, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertFalse(rows[0]['stale'])

        handler.path += '/' + created['id']
        handler._body = lambda: {'note': 'Confirmed evidence', 'read_status': 'reviewed'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            updated, code = handler.do_PATCH()
        self.assertEqual(code, 200)
        self.assertEqual(updated['note'], 'Confirmed evidence')
        self.assertEqual(updated['read_status'], 'reviewed')


class SamplePackageTests(unittest.TestCase):
    def test_new_idea_and_existing_project_samples_have_complete_links(self):
        root = CODE.parent / 'docs/u17-samples'
        new_idea = validate_package(root / 'new-idea/package.json')
        existing = validate_package(root / 'existing-project/package.json')
        self.assertEqual(new_idea['errors'], [])
        self.assertEqual(existing['errors'], [])
        self.assertEqual(new_idea['counts'], {
            'documents': 5, 'requirements': 5, 'tasks': 3, 'acceptance': 4})
        self.assertEqual(existing['counts'], {
            'documents': 5, 'requirements': 5, 'tasks': 4, 'acceptance': 4})


class RetrievalTests(unittest.TestCase):
    def test_scores_follow_slug_and_neighbors_are_unique(self):
        slugs = tuple(f"s{i:02}" for i in range(20))
        values = np.linspace(.1, .99, 20)
        state = classifier.Snapshot(slugs, np.column_stack((values, np.zeros(20))), {}, {},
            {s: set(slugs[:10]) for s in slugs[10:]}, {})
        with patch.object(classifier, '_embed', return_value=[np.array([1., 0.])]):
            pool, scores = classifier.candidates('query', state=state)
        self.assertEqual(pool[0], 's19')
        self.assertAlmostEqual(scores['s19'], .99)
        self.assertEqual(len(pool), 16)
        self.assertEqual(len(set(pool)), 16)
        with patch.object(classifier, 'candidates', return_value=(pool, scores)):
            hits = draft_new.collision('query')
        self.assertEqual(hits[0][0], 's19')
        self.assertAlmostEqual(hits[0][1], .99)

    def test_cache_reloads_after_atomic_database_replacement(self):
        def make(path, names):
            with closing(sqlite3.connect(path)) as con:
                con.executescript('''CREATE TABLE leaf(slug,name_zh,l0_zh,overview,section_id);
                    CREATE TABLE embedding(slug,vec);
                    CREATE TABLE relation(from_slug,to_slug,to_name,distinction);''')
                for name in names:
                    con.execute('INSERT INTO leaf VALUES (?,?,?,?,?)', (name,name,'core','overview','01.01'))
                    con.execute('INSERT INTO embedding VALUES (?,?)', (name,np.array([1.,0.],dtype=np.float32).tobytes()))
                con.commit()
        with tempfile.TemporaryDirectory() as temp:
            db, new = Path(temp)/'atlas.sqlite', Path(temp)/'new.sqlite'
            make(db, ['first'])
            with patch.object(classifier, 'DB', str(db)), patch.object(classifier, '_snapshot', None), patch.object(classifier, '_signature', None):
                old = classifier.snapshot()
                make(new, ['first','second'])
                os.replace(new, db)
                with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
                    snapshots = list(pool.map(lambda _: classifier.snapshot(), range(8)))
                self.assertEqual(old.slugs, ('first',))
                self.assertTrue(all(s.slugs == ('first','second') for s in snapshots))


class GateTests(unittest.TestCase):
    def test_accepted_labels_are_explicit_and_partial_results_fail(self):
        items = [{'name':'钉钉','expect':'team-messaging-application'}]
        rows, summary = gate_check.score_rows([{'name':'钉钉','got':'team-workspace-platform'}], items)
        self.assertTrue(summary['passed'])
        self.assertEqual(summary['raw_accuracy'], 0)
        with self.assertRaises(ValueError):
            gate_check.score_rows([], items)

    def test_request_failure_is_recorded_and_cannot_pass(self):
        items = [{'name':'sample','desc':'test','expect':'first'}]
        with redirect_stdout(io.StringIO()):
            rows = gate_check.run_items(items, lambda _: (_ for _ in ()).throw(OSError('offline')), sleep=lambda _:None)
        _, summary = gate_check.score_rows(rows,items)
        self.assertFalse(summary['passed'])
        self.assertEqual(summary['errors'],1)
        self.assertFalse(rows[0]['ret1'])


class PublicationTests(unittest.TestCase):
    def test_failure_rolls_back_all_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root/'atlas').mkdir()
            old = root/'old'; new = root/'new'; absent=root/'absent'
            old.write_text('before');new.write_text('after')
            real = rt.atomic_copy
            def fail_once(source,target):
                if Path(target)==absent.resolve():
                    raise OSError('disk error')
                return real(source,target)
            with patch.object(rt,'atomic_copy',side_effect=fail_once):
                with self.assertRaises(OSError):rt.publish_files([(new,old),(new,absent)],root)
            self.assertEqual(old.read_text(),'before')
            self.assertFalse(absent.exists())
            self.assertFalse((root/'atlas/.publish').exists())

    def test_recover_interrupted_cutover(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);journal=root/'atlas/.publish';journal.mkdir(parents=True)
            target=root/'live';target.write_text('partial');(journal/'0').write_text('original')
            rt.atomic_json(journal/'journal.json',{'committed':False,'files':[{'target':str(target),'backup':'0'}]})
            rt.recover_publication(root)
            self.assertEqual(target.read_text(),'original')

    def test_corpus_lock_prevents_concurrent_updates(self):
        with tempfile.TemporaryDirectory() as temp:
            with rt.corpus_lock(temp):
                with self.assertRaises(RuntimeError):
                    with rt.corpus_lock(temp):pass

    def test_review_updates_do_not_clobber_other_drafts(self):
        with tempfile.TemporaryDirectory() as temp:
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(lambda n:update_review(f'draft-{n}',{'verdict':'new'},temp),range(30)))
            self.assertEqual(len(load_review(temp)),30)


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.pack=Path(self.temp.name)/'pack';self.pack.mkdir()
        for name in ['applications','research','atlas','logs','drafts']:(self.pack/name).mkdir()
        self.body=(CODE/'applications/cli-accounting-tool.md').read_text()
        for slug,title in [('existing-tool','Existing Tool')]:
            (self.pack/'applications'/f'{slug}.md').write_text(self.body.replace('# CLI Accounting Tool',f'# {title}',1))
            (self.pack/'research'/f'{slug}.md').write_text('## Boundary Findings\nTests\n## Uncertainties\nNone')
        (self.pack/'DIRECTORY.md').write_text('# Test\n## 01 Tools\n### 01.01 Tools\n- Existing Tool\n')
        (self.pack/'STATUS.md').write_text('# Status\n')
        for name in ['mvp_apps.json','mvp_apps_classified.json','pilot_synthetic.json']:(self.pack/name).write_text('[]')
        (self.pack/'pilot_clean.json').write_text(json.dumps([{'name':'sample','desc':'tool','expect':'existing-tool'}]))
        (self.pack/'atlas/section-zh.json').write_text('[{"id":"01.01","name_zh":"工具"}]')
        (self.pack/'atlas/translations.jsonl').write_text(json.dumps({'slug':'existing-tool','name_zh':'工具','aliases_zh':[],'l0_zh':'definition'})+'\n')
        self.run_script(self.pack,'export_atlas.py')
        self.fill_aux(self.pack)
        self.web=Path(self.temp.name)/'web';self.web.mkdir();(self.web/'meta.json').write_text('{"old":true}')
        self.draft=self.pack/'drafts/wip-new.md'
        self.draft.write_text('---\nslug: wip-new\nname: New Tool\nname_zh: 新工具\ndesc: new idea\nsource: human\nstatus: draft\ncreated: 2026-09-13\nengine: test\n---\n'+self.body.replace('# CLI Accounting Tool','# New Tool',1))
        (self.pack/'drafts/wip-new.research.md').write_text('## Boundary Findings\nTests\n## Uncertainties\nNone')
        self.review()

    def run_script(self,pack,name):
        result=subprocess.run([sys.executable,str(CODE/name)],env={**os.environ,'ATLAS_PACK':str(pack),'ATLAS_WEB_OUT':str(pack/'web-data')},capture_output=True,text=True)
        if result.returncode:raise AssertionError(result.stdout+'\n'+result.stderr)

    def fill_aux(self,pack):
        with closing(sqlite3.connect(pack/'atlas/atlas.sqlite')) as con:
            con.execute('CREATE TABLE IF NOT EXISTS embedding(slug TEXT PRIMARY KEY,model,dim,vec)')
            for (slug,) in con.execute('SELECT slug FROM leaf').fetchall():
                con.execute('INSERT OR REPLACE INTO embedding VALUES (?,?,?,?)',(slug,'bge-m3',2,np.array([1.,0.],dtype=np.float32).tobytes()))
                con.execute('INSERT OR REPLACE INTO leaf_zh_body VALUES (?,?,?,?,?,?,?)',(slug,'overview','how','rules','variants','products','test'))
                con.execute('UPDATE leaf SET name_zh=?,l0_zh=? WHERE slug=?',('名称','definition',slug))
            con.commit()

    def review(self,verdict='new',best=None):
        update_review('wip-new',{'verdict':verdict,'best':best,'draft_fingerprint':fingerprint('wip-new',self.pack),'corpus_revision':corpus_revision(self.pack)},self.pack)

    def runner(self,stage,command):
        name=Path(command[1]).name
        if name=='export_atlas.py':self.run_script(stage,name)
        elif name=='translate_zh.py':
            with closing(sqlite3.connect(stage/'atlas/atlas.sqlite')) as con:
                rows=con.execute('SELECT slug FROM leaf').fetchall()
            with (stage/'atlas/translations.jsonl').open('w') as f:
                for (slug,) in rows:f.write(json.dumps({'slug':slug,'name_zh':'名称','l0_zh':'definition','aliases_zh':[]})+'\n')
        elif name=='embed_leaves.py':self.fill_aux(stage)
        elif name=='gen-data.py':self.run_script(stage,'../atlas-web/scripts/gen-data.py')
        elif name=='gate_check.py':
            rt.atomic_json(stage/'atlas/gate_regression.json',[{'name':'sample','got':'existing-tool'}])
            rt.atomic_json(stage/'atlas/gate_summary.json',{'accuracy':1.,'passed':True})

    def test_export_failure_leaves_database_intact(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes()
        with (self.pack/'DIRECTORY.md').open('a') as f:f.write('- Missing Tool\n')
        with self.assertRaises(AssertionError):self.run_script(self.pack,'export_atlas.py')
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)

    def test_export_preserves_unchanged_embeddings_and_accepts_aliases(self):
        # Keep translation fields identical to the source record.
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            con.execute("UPDATE leaf SET name_zh='工具'");con.commit()
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:self.assertEqual(con.execute('SELECT count(*) FROM embedding').fetchone()[0],1)
        p=self.pack/'DIRECTORY.md';p.write_text(p.read_text().replace('- Existing Tool','- Existing Tool / Alternate Tool'))
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            self.assertEqual(con.execute('SELECT slug FROM leaf').fetchone()[0],'existing-tool')
            self.assertEqual(con.execute('SELECT count(*) FROM embedding').fetchone()[0],0)

    def test_alias_of_an_existing_acronym_name_keeps_canonical_slug(self):
        (self.pack/'applications/existing-tool.md').rename(self.pack/'applications/existing-tool-et.md')
        (self.pack/'research/existing-tool.md').rename(self.pack/'research/existing-tool-et.md')
        path=self.pack/'DIRECTORY.md'
        path.write_text(path.read_text().replace('- Existing Tool','- Existing Tool / ET / New Alias'))
        self.run_script(self.pack,'export_atlas.py')
        with closing(sqlite3.connect(self.pack/'atlas/atlas.sqlite')) as con:
            self.assertEqual(con.execute('SELECT slug FROM leaf').fetchone()[0],'existing-tool-et')


    def test_missing_stale_or_variant_review_cannot_create_leaf(self):
        (self.pack/'drafts/review.json').write_text('{}')
        with self.assertRaisesRegex(ValueError,'查重'):promote.validate_promotion('wip-new','new','01.01',self.pack)
        self.review('variant','existing-tool')
        with self.assertRaisesRegex(ValueError,'新类型'):promote.validate_promotion('wip-new','new','01.01',self.pack)
        self.review();self.draft.write_text(self.draft.read_text()+'\nEdit')
        with self.assertRaisesRegex(ValueError,'查重'):promote.validate_promotion('wip-new','new','01.01',self.pack)

    def test_low_gate_does_not_modify_live_corpus(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes();directory=(self.pack/'DIRECTORY.md').read_text()
        def fail_gate(stage,command):
            self.runner(stage,command)
            if Path(command[1]).name=='gate_check.py':
                rt.atomic_json(stage/'atlas/gate_regression.json',[{'name':'sample','got':'none'}])
        with redirect_stdout(io.StringIO()),self.assertRaisesRegex(RuntimeError,'回归未达标'):
            promote.promote('wip-new','new','01.01',self.pack,self.web,fail_gate)
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)
        self.assertEqual((self.pack/'DIRECTORY.md').read_text(),directory)
        self.assertFalse((self.pack/'applications/new-tool.md').exists())
        self.assertTrue((self.pack/'drafts/wip-new.research.md').exists())
        self.assertFalse(load_review(self.pack)['wip-new']['promoted'])
        self.assertFalse(load_review(self.pack)['wip-new']['gate_ok'])
        self.assertEqual(json.loads((self.web/'meta.json').read_text()),{'old':True})

    def test_api_rejects_stale_review_before_starting_background_work(self):
        import drafts_api
        self.draft.write_text(self.draft.read_text()+'\nChanged')
        handler=object.__new__(drafts_api.Handler)
        handler.path='/api/promote'
        handler._body=lambda:{'slug':'wip-new','action':'new','section':'01.01'}
        responses=[]
        handler._json=lambda body,code=200:responses.append((body,code))
        validate=promote.validate_promotion
        with patch.object(promote,'validate_promotion',side_effect=lambda slug,action,target:validate(slug,action,target,self.pack)), patch.object(drafts_api.threading,'Thread') as thread:
            handler.do_POST()
        self.assertEqual(responses[0][1],409)
        thread.assert_not_called()

    def test_api_does_not_enqueue_a_draft_already_promoting_in_another_process(self):
        import drafts_api
        self.draft.write_text(self.draft.read_text().replace('status: draft','status: promoting'))
        handler=object.__new__(drafts_api.Handler)
        handler.path='/api/promote'
        handler._body=lambda:{'slug':'wip-new','action':'new','section':'01.01'}
        responses=[]
        handler._json=lambda body,code=200:responses.append((body,code))
        validate=promote.validate_promotion
        with patch.object(promote,'validate_promotion',side_effect=lambda slug,action,target:validate(slug,action,target,self.pack)), patch.object(drafts_api.threading,'Thread') as thread:
            handler.do_POST()
        self.assertEqual(responses[0][1],409)
        thread.assert_not_called()
        self.assertIn('status: promoting',self.draft.read_text())


    def test_pipeline_exception_preserves_draft_research_and_database(self):
        before=(self.pack/'atlas/atlas.sqlite').read_bytes()
        def unavailable(stage,command):raise OSError('provider unavailable')
        with self.assertRaisesRegex(OSError,'provider unavailable'):
            promote.promote('wip-new','new','01.01',self.pack,self.web,unavailable)
        self.assertEqual((self.pack/'atlas/atlas.sqlite').read_bytes(),before)
        self.assertTrue((self.pack/'drafts/wip-new.research.md').exists())
        self.assertIn('status: draft',self.draft.read_text())


    def test_success_publishes_and_keeps_draft_id(self):
        with redirect_stdout(io.StringIO()):result=promote.promote('wip-new','new','01.01',self.pack,self.web,self.runner)
        self.assertTrue(result['promoted']);self.assertEqual(result['final_slug'],'new-tool')
        self.assertTrue(self.draft.exists());self.assertIn('status: promoted',self.draft.read_text())
        self.assertEqual(json.loads((self.web/'meta.json').read_text())['leafCount'],2)
        self.assertTrue((self.pack/'applications/new-tool.md').exists())
        with self.assertRaisesRegex(ValueError,'状态'):promote.validate_promotion('wip-new','new','01.01',self.pack)

    def test_merge_rebuilds_data_without_adding_a_leaf(self):
        self.review('variant','existing-tool')
        with redirect_stdout(io.StringIO()):result=promote.promote('wip-new','merge','existing-tool',self.pack,self.web,self.runner)
        self.assertTrue(result['promoted'])
        self.assertIn('Existing Tool / New Tool',(self.pack/'DIRECTORY.md').read_text())
        self.assertEqual(json.loads((self.web/'meta.json').read_text())['leafCount'],1)


if __name__=='__main__':unittest.main()
