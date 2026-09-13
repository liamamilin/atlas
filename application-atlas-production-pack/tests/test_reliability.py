import concurrent.futures
from contextlib import closing, redirect_stdout
import io
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
import zipfile
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
from opencode_client import OpenCodeClient, OpenCodeError, iter_sse
from execution_state import project_execution
from execution_workspace import prepare_execution_workspace
from execution_service import (
    _completion_report,
    apply_execution_result,
    continue_execution,
    create_iteration as create_execution_iteration,
    create_task as create_execution_task,
    reconcile_execution, start_execution, stop_execution,
)
from project_store import ProjectStore, ProjectStoreError
from project_export import export_project
from project_generation import (
    apply_generation_item, execute_generation, prepare_generation,
    read_generation,
)
from project_baseline import (
    capture_project_baseline, check_project_changes, get_project_baseline,
    latest_project_baseline, list_project_baselines,
)
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
            [{'id': 'que_one', 'sessionID': 'ses_abc'}, {'id': 'que_two', 'sessionID': 'ses_other'}],
        ])
        result = self.client.reconcile('ses_abc')
        self.assertEqual(result['status']['type'], 'busy')
        self.assertEqual([item['id'] for item in result['pending_permissions']], ['per_one'])
        self.assertEqual([item['id'] for item in result['pending_questions']], ['que_one'])
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

    def test_question_reply_uses_current_endpoint_and_answer_shape(self):
        self.responses.append(True)
        self.assertTrue(self.client.reply_question('que_abc', [['Use SQLite'], ['Keep both']]))
        request, _ = self.requests[0]
        self.assertIn('/question/que_abc/reply', request.full_url)
        self.assertEqual(json.loads(request.data), {
            'answers': [['Use SQLite'], ['Keep both']],
        })

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

    def test_user_message_without_assistant_response_stays_queued(self):
        result = project_execution({
            'status': {'type': 'idle'},
            'messages': [{
                'info': {'id': 'msg_user', 'role': 'user'},
                'parts': [{'type': 'text', 'text': 'Start'}],
            }],
        }, 'msg_user')
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

    def test_workspace_baseline_separates_evidence_and_adopts_reviewed_changes(self):
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'assets').mkdir()
        (workspace / 'README.md').write_text(
            '# Pilot\n\n## Claimed behavior\nThe project claims to serve a dashboard.\n')
        (workspace / 'package.json').write_text('{"scripts":{"test":"vitest"}}')
        (workspace / 'src/app.py').write_text('def dashboard():\n    return "v1"\n')
        (workspace / 'assets/logo.bin').write_bytes(b'v1')

        baseline = capture_project_baseline(self.store, self.project['id'], ['src'])
        self.assertEqual(baseline['coverage']['focus_paths'], ['src'])
        self.assertIn('README.md', baseline['coverage']['read_paths'])
        self.assertIn('package.json', baseline['coverage']['read_paths'])
        self.assertIn('src/app.py', baseline['coverage']['read_paths'])
        self.assertTrue(baseline['observations']['document_claims'])
        self.assertTrue(baseline['observations']['code_clues'])
        self.assertEqual(baseline['observations']['runtime_verified'], [])
        self.assertIn('没有执行项目命令', baseline['report_markdown'])
        self.assertEqual(get_project_baseline(
            self.store, self.project['id'], baseline['id'])['id'], baseline['id'])

        (workspace / 'src/app.py').write_text('def dashboard():\n    return "v2"\n')
        (workspace / 'assets/logo.bin').write_bytes(b'v2')
        checked = check_project_changes(self.store, self.project['id'])
        self.assertEqual(checked['changes']['reviewed_scope_changes'], ['src/app.py'])
        self.assertEqual(checked['changes']['outside_review_scope_changes'],
                         ['assets/logo.bin'])
        self.assertTrue(checked['changes']['requires_focused_review'])
        self.assertTrue(checked['changes']['has_unread_changes'])
        self.assertEqual(len(list_project_baselines(self.store, self.project['id'])), 1)

        adopted = capture_project_baseline(
            self.store, self.project['id'], ['src'], baseline['id'],
            checked['current']['content_fingerprint'])
        self.assertEqual(adopted['changes_from_previous']['reviewed_scope_changes'],
                         ['src/app.py'])
        self.assertEqual([item['id'] for item in list_project_baselines(
            self.store, self.project['id'])], [adopted['id'], baseline['id']])
        reviewed_again = check_project_changes(self.store, self.project['id'])
        (workspace / 'README.md').write_text('# Pilot\n\nChanged after review.\n')
        with self.assertRaisesRegex(ProjectStoreError, 'workspace changed after review'):
            capture_project_baseline(
                self.store, self.project['id'], ['src'], adopted['id'],
                reviewed_again['current']['content_fingerprint'])
        with self.assertRaisesRegex(ProjectStoreError, 'baseline changed'):
            capture_project_baseline(
                self.store, self.project['id'], ['src'], baseline['id'])

    def test_outside_scope_change_is_visible_without_forcing_focus_review(self):
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'assets').mkdir()
        (workspace / 'src/app.py').write_text('print("stable")\n')
        (workspace / 'assets/photo.bin').write_bytes(b'before')
        capture_project_baseline(self.store, self.project['id'], ['src'])
        (workspace / 'assets/photo.bin').write_bytes(b'after')

        changes = check_project_changes(self.store, self.project['id'])['changes']
        self.assertEqual(changes['outside_review_scope_changes'], ['assets/photo.bin'])
        self.assertTrue(changes['has_unread_changes'])
        self.assertFalse(changes['requires_focused_review'])

    def test_workspace_focus_paths_must_exist_and_remain_inside_root(self):
        workspace = self.root / 'workspace'
        workspace.mkdir(parents=True)
        (workspace / 'README.md').write_text('# Pilot\n')
        with self.assertRaisesRegex(ValueError, 'inside'):
            capture_project_baseline(self.store, self.project['id'], ['../secret'])
        with self.assertRaisesRegex(ValueError, 'does not exist'):
            capture_project_baseline(self.store, self.project['id'], ['missing'])

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
            self.assertEqual(con.execute('PRAGMA user_version').fetchone()[0], 5)

    def test_version_two_store_adds_document_authorship(self):
        path = self.root / 'version-two.sqlite'
        with sqlite3.connect(path) as con:
            con.executescript('''
                CREATE TABLE project (
                    id TEXT PRIMARY KEY, name TEXT NOT NULL, objective TEXT NOT NULL,
                    workspace TEXT NOT NULL, mode TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE document (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    kind TEXT NOT NULL, title TEXT NOT NULL, current_version INTEGER NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE document_version (
                    id TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES document(id),
                    version INTEGER NOT NULL, content TEXT NOT NULL, content_sha256 TEXT NOT NULL,
                    basis_json TEXT NOT NULL, created_at TEXT NOT NULL,
                    UNIQUE(document_id,version));
                INSERT INTO project VALUES
                    ('prj_v2','V2','Migrate','/tmp/v2','existing','now','now');
                INSERT INTO document VALUES
                    ('doc_v2','prj_v2','analysis','Analysis',1,'now','now');
                INSERT INTO document_version VALUES
                    ('dver_v2','doc_v2',1,'legacy','sha','[]','now');
                PRAGMA user_version=2;
            ''')
        migrated = ProjectStore(path)
        document = migrated.get_document('doc_v2')
        self.assertEqual(document['author'], 'unknown')
        self.assertEqual(document['change_summary'], '')
        with sqlite3.connect(path) as con:
            self.assertEqual(con.execute('PRAGMA user_version').fetchone()[0], 5)

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

    def test_document_basis_tracks_authorship_and_upstream_changes(self):
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep work local', 'current', 'User constraint',
            ['No network is required'])
        analysis = self.store.create_document(
            self.project['id'], 'analysis', 'Analysis', 'Initial analysis',
            [{'kind': 'requirement', 'id': requirement['id']}],
            author='ai', change_summary='Generated from confirmed research')
        self.assertEqual(analysis['author'], 'ai')
        self.assertEqual(analysis['review']['status'], 'current')
        self.assertEqual(analysis['basis'][0]['id'], requirement['id'])
        self.assertIn('fingerprint', analysis['basis'][0])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        self.assertEqual(
            self.store.get_document(analysis['id'])['review']['reasons'][0]['kind'],
            'requirement_changed')
        revised = self.store.add_document_version(
            analysis['id'], 'Human revision',
            [{'kind': 'requirement', 'id': requirement['id']}],
            expected_current_version=1, author='human', change_summary='Kept manual nuance')
        self.assertEqual(revised['review']['status'], 'current')
        downstream = self.store.create_document(
            self.project['id'], 'technical-plan', 'Technical plan', 'Plan v1',
            [{'kind': 'document_version', 'id': revised['version_id']}], author='ai')
        self.store.add_document_version(
            analysis['id'], 'Human revision two',
            [{'kind': 'requirement', 'id': requirement['id']}], author='human')
        self.assertEqual(
            self.store.get_document(downstream['id'])['review']['reasons'][0]['kind'],
            'upstream_document_changed')
        changed = self.store.update_requirement(
            self.project['id'], requirement['id'], content='Keep data and execution local')
        self.assertIsNone(changed['confirmed_scope'])

    def test_project_export_is_self_contained_and_keeps_confirmation_separate(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            locator='core-model', excerpt='## Core Model\nFixed evidence',
            note='Use the record boundary', read_status='reviewed')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the record boundary', 'current', 'Matches the evidence',
            ['The boundary is visible'], [reference['id']])
        self.store.record_decision(
            self.project['id'], 'Use a fixed excerpt', 'Prevents silent source changes',
            [reference['id']])
        self.store.create_document(
            self.project['id'], 'product-requirements', 'Product requirements',
            '# Product requirements\n\nKeep the boundary.',
            [{'kind': 'reference', 'id': reference['id']},
             {'kind': 'requirement', 'id': requirement['id']}],
            author='ai', change_summary='Initial document')
        exported = export_project(self.store, self.project['id'])
        archive = Path(exported['archive'])
        self.assertTrue(archive.is_file())
        self.assertEqual(exported['manifest']['unresolved_requirement_ids'], [requirement['id']])
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
            index = bundle.read('INDEX.md').decode()
            requirements = bundle.read('requirements.md').decode()
            source_name = next(name for name in names if name.startswith('sources/'))
            source = bundle.read(source_name).decode()
        self.assertIn('Product requirements', index)
        self.assertIn('User confirmation: `pending`', requirements)
        self.assertIn('AI recommendation: `current`', requirements)
        self.assertIn('Fixed evidence', source)

    def test_analysis_generation_is_grounded_reviewable_and_applied_once(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed local evidence', note='Use the fixed boundary', read_status='reviewed')
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual(request['references'][0]['excerpt'], 'Fixed local evidence')
        self.assertNotIn('workspace', request['project'])
        prompt = (directory / 'prompt.md').read_text()
        self.assertIn('Do not browse the web', prompt)
        self.assertIn('background evidence, not the project', prompt)
        self.assertIn('Fixed local evidence', (directory / 'input.md').read_text())

        def fake_runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [{
                    'question': 'Who owns review?', 'why': 'The evidence does not say.',
                    'affects': ['analysis'],
                    'evidence': [{'kind': 'reference', 'id': 'ref_non_contract'}],
                }],
                'requirements': [{
                    'key': 'keep-local', 'content': 'Keep the workflow local',
                    'recommended_scope': 'current',
                    'recommendation_reason': 'The fixed evidence supports it',
                    'acceptance_conditions': ['The flow works without a remote account'],
                    'reference_ids': [reference['id']],
                }],
                'conflicts': [],
                'suggestions': [{
                    'summary': 'Show the source version', 'reason': 'It keeps review traceable',
                    'evidence': [{'kind': 'reference', 'id': reference['id']}],
                }],
                'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis\n\nFixed evidence and an open ownership question.',
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_fake'})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=fake_runner)
        self.assertEqual(completed['status'], 'completed')
        self.assertEqual(completed['engine_session_id'], 'ses_fake')
        self.assertNotIn('evidence', completed['result']['questions'][0])
        applied_requirement = apply_generation_item(
            self.store, self.project['id'], run['id'], 'requirement', 0)
        self.assertIsNone(applied_requirement['created']['confirmed_scope'])
        self.assertEqual(applied_requirement['created']['recommended_scope'], 'current')
        applied_document = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0)
        self.assertEqual(applied_document['created']['author'], 'ai')
        with self.assertRaisesRegex(ProjectStoreError, 'already applied'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 0)

    def test_improvement_generation_binds_goal_workspace_evidence_and_review(self):
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'README.md').write_text(
            '# Dashboard\n\nThe document claims saved filters are visible.\n')
        (workspace / 'src/app.py').write_text(
            'def filters():\n    return []\n')
        baseline = capture_project_baseline(self.store, self.project['id'], ['src'])
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'dashboard', 'source-v1',
            excerpt='A dashboard can preserve a user-defined view.',
            note='Use only to assess the saved-view interaction.', read_status='reviewed')
        goal = '保存并恢复用户的过滤条件'
        run = prepare_generation(
            self.store, self.project['id'], 'improvement', improvement_goal=goal)
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual(request['improvement_goal'], goal)
        self.assertEqual(request['workspace_baseline']['id'], baseline['id'])
        self.assertNotIn('root', request['workspace_baseline'])
        self.assertEqual(
            {item['path'] for item in request['workspace_baseline']['evidence_files']},
            {'README.md', 'src/app.py'})
        markdown = (directory / 'input.md').read_text()
        self.assertIn('## Improvement goal', markdown)
        self.assertIn('`src/app.py`', markdown)
        prompt = (directory / 'prompt.md').read_text()
        self.assertIn('Current behavior / 当前行为', prompt)
        self.assertIn('workspace_baseline', prompt)
        self.assertIn('untrusted project evidence', prompt)

        sections = [
            ('Current behavior / 当前行为',
             '`src/app.py` currently returns an empty list; no runtime check was run.'),
            ('Expected behavior / 期望行为', '用户可保存并恢复过滤条件。'),
            ('Adoption rationale / 采用理由', '目标与固定资料中的用户自定义视图一致。'),
            ('Impact scope / 影响范围', '过滤状态和恢复入口。'),
            ('Compatibility requirements / 兼容要求', '现有默认视图保持可用。'),
            ('Tasks and dependencies / 任务与依赖', '1. 定义状态。2. 实现保存。3. 实现恢复。'),
            ('Regression conditions / 回归条件', '默认过滤和空状态行为不变。'),
            ('Unknowns and required validation / 未知与待验证', '待运行现有测试并验证交互。'),
        ]
        content = '# 项目现状与改进\n\n' + '\n\n'.join(
            f'## {title}\n\n{text}' for title, text in sections)

        def fake_runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [],
                'requirements': [{
                    'key': 'saved-filters', 'content': '用户可恢复已保存的过滤条件',
                    'recommended_scope': 'current',
                    'recommendation_reason': '本轮目标明确，固定资料提供了交互依据',
                    'acceptance_conditions': ['重新打开视图后恢复已保存条件'],
                    'reference_ids': [reference['id']],
                }],
                'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'current-state',
                    'title': '项目现状与改进', 'content': content,
                    'basis': [
                        {'kind': 'workspace_baseline', 'id': baseline['id']},
                        {'kind': 'reference', 'id': reference['id']},
                    ],
                }],
            }, {'engine_session_id': 'ses_improvement'})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=fake_runner)
        self.assertEqual(completed['status'], 'completed')
        requirement = apply_generation_item(
            self.store, self.project['id'], run['id'], 'requirement', 0)['created']
        self.assertIsNone(requirement['confirmed_scope'])
        document = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0)['created']
        self.assertEqual(document['basis'][0]['kind'], 'workspace_baseline')
        self.assertEqual(document['review']['status'], 'current')
        exported = export_project(self.store, self.project['id'])
        self.assertEqual(exported['manifest']['workspace_baseline_id'], baseline['id'])
        with zipfile.ZipFile(exported['archive']) as bundle:
            self.assertIn('workspace-baseline.md', bundle.namelist())
            exported_baseline = json.loads(bundle.read('workspace-baseline.json'))
        self.assertEqual(exported_baseline['id'], baseline['id'])
        self.assertIn('src/app.py', exported_baseline['manifest']['evidence_files'])

        (workspace / 'src/app.py').write_text(
            'def filters():\n    return ["external-change"]\n')
        changed = check_project_changes(self.store, self.project['id'])
        new_baseline = capture_project_baseline(
            self.store, self.project['id'], ['src'], baseline['id'],
            changed['current']['content_fingerprint'])
        reviewed = self.store.get_document(document['id'])['review']
        self.assertEqual(reviewed['status'], 'needs_review')
        self.assertEqual(reviewed['reasons'][0]['kind'], 'workspace_baseline_changed')
        self.assertEqual(reviewed['reasons'][0]['current_baseline_id'], new_baseline['id'])

    def test_improvement_generation_rejects_workspace_change_after_preparation(self):
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'src/app.py').write_text('print("before")\n')
        capture_project_baseline(self.store, self.project['id'], ['src'])
        self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt='Evidence')
        run = prepare_generation(
            self.store, self.project['id'], 'improvement',
            improvement_goal='Improve the current behavior')
        (workspace / 'src/app.py').write_text('print("after")\n')
        called = []

        def should_not_run(_directory, _run):
            called.append(True)
            return ({}, {})

        with self.assertRaisesRegex(ProjectStoreError, 'workspace changed'):
            execute_generation(
                self.store, self.project['id'], run['id'], runner=should_not_run)
        self.assertEqual(called, [])
        self.assertEqual(
            read_generation(self.store, self.project['id'], run['id'])['status'], 'failed')

    def test_improvement_result_requires_baseline_basis_and_complete_plan(self):
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'src/app.py').write_text('print("observed")\n')
        baseline = capture_project_baseline(self.store, self.project['id'], ['src'])
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt='Evidence')

        def result_for(request, basis, content):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'current-state', 'title': 'Plan',
                    'content': content, 'basis': basis,
                }],
            }, {})

        complete = '# Plan\n\n' + '\n\n'.join(
            f'## {title}\n\n`src/app.py` evidence.' for title in (
                'Current behavior / 当前行为', 'Expected behavior / 期望行为',
                'Adoption rationale / 采用理由', 'Impact scope / 影响范围',
                'Compatibility requirements / 兼容要求',
                'Tasks and dependencies / 任务与依赖',
                'Regression conditions / 回归条件',
                'Unknowns and required validation / 未知与待验证'))
        run = prepare_generation(
            self.store, self.project['id'], 'improvement', improvement_goal='Improve it')
        request = json.loads((self.store.path.parent / 'generation-runs' /
                              self.project['id'] / run['id'] / 'input.json').read_text())
        with self.assertRaisesRegex(ValueError, 'workspace baseline'):
            execute_generation(
                self.store, self.project['id'], run['id'],
                runner=lambda *_: result_for(
                    request, [{'kind': 'reference', 'id': reference['id']}], complete))

        second = prepare_generation(
            self.store, self.project['id'], 'improvement', improvement_goal='Improve it')
        request = json.loads((self.store.path.parent / 'generation-runs' /
                              self.project['id'] / second['id'] / 'input.json').read_text())
        with self.assertRaisesRegex(ValueError, 'missing section'):
            execute_generation(
                self.store, self.project['id'], second['id'],
                runner=lambda *_: result_for(request, [
                    {'kind': 'workspace_baseline', 'id': baseline['id']},
                    {'kind': 'reference', 'id': reference['id']},
                ], '# Plan\n\n## Current behavior / 当前行为\n\n`src/app.py`'))

    def test_generation_rejects_wrong_input_fingerprint_and_unknown_evidence(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt='Evidence')
        run = prepare_generation(self.store, self.project['id'], 'analysis')

        def wrong_fingerprint(_directory, _run):
            return ({
                'input_fingerprint': 'wrong', 'questions': [], 'requirements': [],
                'conflicts': [], 'suggestions': [], 'documents': [],
            }, {})

        with self.assertRaisesRegex(ValueError, 'fingerprint'):
            execute_generation(
                self.store, self.project['id'], run['id'], runner=wrong_fingerprint)
        self.assertEqual(
            read_generation(self.store, self.project['id'], run['id'])['status'], 'failed')

        second = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / second['id'])
        request = json.loads((directory / 'input.json').read_text())

        def unknown_evidence(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [],
                'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis',
                    'basis': [{'kind': 'reference', 'id': 'ref_unknown'}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'unknown input'):
            execute_generation(
                self.store, self.project['id'], second['id'], runner=unknown_evidence)

        third = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / third['id'])
        tampered = json.loads((directory / 'input.json').read_text())
        tampered['references'][0]['excerpt'] = 'Changed after fingerprinting'
        (directory / 'input.json').write_text(json.dumps(tampered))
        with self.assertRaisesRegex(ValueError, 'fixed content'):
            execute_generation(
                self.store, self.project['id'], third['id'], runner=unknown_evidence)

        fourth = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / fourth['id'])
        (directory / 'input.md').write_text('Changed after fingerprinting')
        with self.assertRaisesRegex(ValueError, 'Markdown input'):
            execute_generation(
                self.store, self.project['id'], fourth['id'], runner=unknown_evidence)

    def test_generation_markdown_keeps_long_fixed_evidence_readable(self):
        evidence = 'A' * 2505
        self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt=evidence)
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        markdown = (directory / 'input.md').read_text()
        self.assertIn(evidence, markdown.replace('\n', ''))
        self.assertLessEqual(max(map(len, markdown.splitlines())), 1200)

    def test_document_generation_uses_confirmed_scope_and_will_not_overwrite_newer_edit(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt='Evidence')
        pending = self.store.create_requirement(
            self.project['id'], 'Pending idea', 'current', 'Model advice',
            ['Pending acceptance'], [reference['id']])
        confirmed = self.store.create_requirement(
            self.project['id'], 'Confirmed requirement', 'current', 'Source support',
            ['Observable result'], [reference['id']])
        self.store.confirm_requirement(confirmed['id'], 'current', 'User approved')
        document = self.store.create_document(
            self.project['id'], 'product-requirements', 'PRD', '# PRD\n\nHuman text',
            [{'kind': 'requirement', 'id': confirmed['id']}], author='human')

        duplicate = prepare_generation(
            self.store, self.project['id'], 'documents', ['product-requirements'])
        duplicate_directory = (self.store.path.parent / 'generation-runs' /
                               self.project['id'] / duplicate['id'])
        duplicate_request = json.loads((duplicate_directory / 'input.json').read_text())

        def duplicate_runner(_directory, _run):
            return ({
                'input_fingerprint': duplicate_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'product-requirements',
                    'title': 'Parallel PRD', 'content': '# Parallel PRD',
                    'basis': [{'kind': 'requirement', 'id': confirmed['id']}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'target an existing document'):
            execute_generation(
                self.store, self.project['id'], duplicate['id'], runner=duplicate_runner)

        run = prepare_generation(
            self.store, self.project['id'], 'documents', ['product-requirements'])
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual([item['id'] for item in request['requirements']], [confirmed['id']])
        self.assertNotIn(pending['id'], json.dumps(request))
        prompt = (directory / 'prompt.md').read_text()
        self.assertIn('requirements` array MUST be exactly empty', prompt)
        self.assertIn('"requirements": []', prompt)
        markdown_input = (directory / 'input.md').read_text()
        self.assertIn(f"requirement:{confirmed['id']}", markdown_input)
        self.assertIn('Human text', markdown_input)

        def fake_runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [],
                'suggestions': [{
                    'summary': 'Keep scope fixed', 'reason': 'Use the confirmed input only',
                    'evidence': [{'kind': 'reference', 'id': confirmed['id']}],
                }],
                'documents': [{
                    'document_id': document['id'], 'kind': 'product-requirements',
                    'title': 'PRD', 'content': '# PRD\n\nHuman text retained.\n\nGenerated detail.',
                    'basis': [
                        {'kind': 'reference', 'id': reference['id']},
                        {'kind': 'requirement', 'id': confirmed['id']},
                        {'kind': 'document_version', 'id': document['version_id']},
                    ],
                }],
            }, {})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=fake_runner)
        self.assertEqual(
            completed['result']['suggestions'][0]['evidence'][0]['kind'], 'requirement')
        self.assertNotIn(
            document['version_id'],
            [item['id'] for item in completed['result']['documents'][0]['basis']])
        self.store.add_document_version(
            document['id'], '# PRD\n\nNewer human edit', document['basis'],
            expected_current_version=1, author='human', change_summary='Edited while AI ran')
        with self.assertRaisesRegex(ProjectStoreError, 'version conflict'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 0)
        self.assertEqual(self.store.get_document(document['id'])['content'],
                         '# PRD\n\nNewer human edit')

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

    def test_workspace_allows_only_one_active_execution(self):
        first = self.store.create_task(self.project['id'], 'First', 'First change')
        second = self.store.create_task(self.project['id'], 'Second', 'Second change')
        source = str((self.root / 'workspace').resolve())
        active = self.store.create_execution(
            first['id'], 'opencode', 'ses_first',
            workdir=str((self.root / 'run-one').resolve()), source_workdir=source)
        with self.assertRaisesRegex(ProjectStoreError, 'active execution'):
            self.store.create_execution(
                second['id'], 'opencode', 'ses_second',
                workdir=str((self.root / 'run-two').resolve()), source_workdir=source)
        self.store.update_execution(active['id'], {
            'state': 'stopped', 'engine_status': 'idle', 'evidence': {},
        })
        created = self.store.create_execution(
            second['id'], 'opencode', 'ses_second',
            workdir=str((self.root / 'run-two').resolve()), source_workdir=source)
        self.assertEqual(created['status'], 'queued')

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

    def test_workspace_baseline_http_capture_check_list_and_conflict(self):
        import drafts_api
        workspace = self.root / 'workspace'
        (workspace / 'src').mkdir(parents=True)
        (workspace / 'notes').mkdir()
        (workspace / 'README.md').write_text('# Existing project\n')
        (workspace / 'src/app.py').write_text('print("v1")\n')
        (workspace / 'notes/private.txt').write_text('v1\n')
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)
        handler.path = f"/api/projects/{self.project['id']}/workspace-baselines"
        handler._body = lambda: {'action': 'capture', 'focus_paths': ['src']}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            baseline, code = handler.do_POST()
        self.assertEqual(code, 201)

        handler._body = lambda: {'action': 'check'}
        (workspace / 'notes/private.txt').write_text('v2\n')
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            checked, code = handler.do_POST()
        self.assertEqual(code, 200)
        self.assertEqual(checked['changes']['outside_review_scope_changes'],
                         ['notes/private.txt'])
        self.assertFalse(checked['changes']['requires_focused_review'])

        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            listed, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual([item['id'] for item in listed], [baseline['id']])

        handler._body = lambda: {
            'action': 'capture', 'focus_paths': ['src'],
            'expected_baseline_id': baseline['id'],
            'expected_content_fingerprint': checked['current']['content_fingerprint'],
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            adopted, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertEqual(adopted['changes_from_previous']['outside_review_scope_changes'],
                         ['notes/private.txt'])

        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            conflict, code = handler.do_POST()
        self.assertEqual(code, 409)
        self.assertIn('baseline changed', conflict['error'])

        self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1', excerpt='Evidence')
        (workspace / 'src/app.py').write_text('print("v2")\n')
        handler.path = f"/api/projects/{self.project['id']}/generation-runs"
        handler._body = lambda: {
            'mode': 'improvement', 'improvement_goal': 'Improve the current behavior'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            stale, code = handler.do_POST()
        self.assertEqual(code, 409)
        self.assertIn('workspace differs', stale['error'])

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

    def test_project_workflow_http_keeps_recommendation_confirmation_and_versions_distinct(self):
        import drafts_api
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1',
            excerpt='Fixed evidence', read_status='reviewed')
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)

        handler.path = f"/api/projects/{self.project['id']}/requirements"
        handler._body = lambda: {
            'content': 'Keep the core record visible',
            'recommended_scope': 'current',
            'recommendation_reason': 'Supported by the source',
            'acceptance_conditions': ['The record remains visible'],
            'reference_ids': [reference['id']],
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            requirement, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertEqual(requirement['recommended_scope'], 'current')
        self.assertIsNone(requirement['confirmed_scope'])

        handler.path += '/' + requirement['id'] + '/confirm'
        handler._body = lambda: {'scope': 'current', 'reason': 'Approved for the pilot'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            confirmed, code = handler.do_POST()
        self.assertEqual(code, 200)
        self.assertEqual(confirmed['confirmed_scope'], 'current')

        handler.path = f"/api/projects/{self.project['id']}/documents"
        handler._body = lambda: {
            'kind': 'product-requirements', 'title': 'Product requirements',
            'content': '# Product requirements\n\nInitial human-reviewed scope.',
            'basis': [{'kind': 'requirement', 'id': requirement['id']},
                      {'kind': 'reference', 'id': reference['id']}],
            'author': 'ai', 'change_summary': 'Initial linked draft',
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            document, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertEqual(document['review']['status'], 'current')

        handler.path = (f"/api/projects/{self.project['id']}/documents/"
                        f"{document['id']}/versions")
        handler._body = lambda: {
            'content': '# Product requirements\n\nPreserve the manual constraint.',
            'basis': document['basis'], 'expected_current_version': 1,
            'author': 'human', 'change_summary': 'Clarified the accepted wording',
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            revised, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertEqual(revised['current_version'], 2)
        self.assertEqual(revised['author'], 'human')

        handler.path = (f"/api/projects/{self.project['id']}/documents/"
                        f"{document['id']}/diff?from=1&to=2")
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            diff, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertIn('+Preserve the manual constraint.', diff['diff'])
        self.assertIn(
            '-Initial human-reviewed scope.\n+Preserve the manual constraint.',
            diff['diff'])

        handler.path = (f"/api/projects/{self.project['id']}/requirements/"
                        f"{requirement['id']}")
        handler._body = lambda: {'content': 'Keep the core record and its source visible'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            changed, code = handler.do_PATCH()
        self.assertEqual(code, 200)
        self.assertIsNone(changed['confirmed_scope'])

        handler.path = f"/api/projects/{self.project['id']}/workspace"
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            workspace, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual(workspace['documents'][0]['review']['status'], 'needs_review')

        handler.path = f"/api/projects/{self.project['id']}/export"
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            exported, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertTrue(Path(exported['archive']).is_file())
        self.assertEqual(exported['manifest']['documents_needing_review'], [document['id']])


class ExecutionServiceTests(unittest.TestCase):
    class Client:
        def __init__(self):
            self.prompt = ''
            self.prompts = []
            self.session_ids = []
            self.user_messages = []
            self.mode = 'running'
            self.permission_replies = []
            self.created = 0

        def create_session(self, title):
            self.created += 1
            return {'id': 'ses_execution'}

        def send_message_async(self, session_id, text, provider_id, model_id, **kwargs):
            self.prompt = text
            self.prompts.append(text)
            self.session_ids.append(session_id)
            self.user_messages.append({
                'info': {'id': f'msg_user_{len(self.user_messages) + 1}',
                         'role': 'user'},
                'parts': [{'type': 'text', 'text': text}],
            })
            self.tools = kwargs['tools']

        def messages(self, session_id):
            return list(self.user_messages)

        def reconcile(self, session_id):
            user = self.user_messages[-1]
            user_id = user['info']['id']
            assistant = {'info': {'id': 'msg_answer', 'parentID': user_id,
                                  'role': 'assistant'},
                         'parts': [{'type': 'text', 'text': 'Implemented and checked.'}]}
            permissions = []
            status = {'type': 'busy'}
            if self.mode == 'completed':
                status = {'type': 'idle'}
                assistant['info'].update({'finish': 'stop', 'time': {'completed': 123}})
                requirement_ids = re.findall(r"### `(req_[A-Za-z0-9]+)`", self.prompt)
                report = {
                    'schema': 1,
                    'requirements': [
                        {'id': requirement_id, 'status': 'satisfied',
                         'evidence': ['Value changed and fixed verification passed']}
                        for requirement_id in requirement_ids
                    ],
                    'unfinished': [], 'deviations': [],
                }
                assistant['parts'][0]['text'] = (
                    'Implemented and checked.\nATLAS_RESULT: ' + json.dumps(report))
                assistant['parts'].append({
                    'type': 'tool', 'tool': 'bash',
                    'state': {
                        'status': 'completed',
                        'input': {'command': 'python3 -m unittest'},
                        'output': 'Ran 1 test\nOK\n',
                        'metadata': {'exit': 0, 'truncated': False},
                    },
                })
            elif self.mode == 'permission':
                permissions = [{
                    'id': 'per_execution', 'sessionID': session_id,
                    'tool': {'messageID': 'msg_answer'},
                    'permission': 'bash', 'patterns': ['python3 -m unittest'],
                }]
            return {'session': {'id': session_id}, 'status': status,
                    'messages': [user, assistant], 'engine_diff': [],
                    'pending_permissions': permissions, 'pending_questions': []}

        def reply_permission(self, request_id, reply, message=None):
            self.permission_replies.append((request_id, reply, message))
            self.mode = 'running'
            return True

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / 'workspace'
        (self.workspace / 'src').mkdir(parents=True)
        (self.workspace / 'node_modules/example').mkdir(parents=True)
        (self.workspace / 'README.md').write_text('# Pilot\n')
        (self.workspace / 'src/app.py').write_text('VALUE = 1\n')
        (self.workspace / 'node_modules/example/index.js').write_text('module.exports = 1\n')
        self.store = ProjectStore(self.root / 'state/projects.sqlite')
        self.project = self.store.create_project(
            'Execution pilot', 'Ship one bounded change', self.workspace, 'existing')
        self.baseline = capture_project_baseline(
            self.store, self.project['id'], ['src'])
        self.requirement = self.store.create_requirement(
            self.project['id'], 'Value becomes two', 'current', 'Pilot scope',
            ['The value is two'])
        self.store.confirm_requirement(self.requirement['id'], 'current', 'Approved')
        self.document = self.store.create_document(
            self.project['id'], 'current-state', 'Change plan', 'Update `src/app.py`.',
            [{'kind': 'workspace_baseline', 'id': self.baseline['id']}])
        self.iteration = create_execution_iteration(self.store, self.project['id'], {
            'title': 'Iteration one', 'objective': 'Update the value',
            'input_document_versions': [self.document['version_id']],
            'requirement_ids': [self.requirement['id']],
        })
        self.task = create_execution_task(self.store, self.project['id'], {
            'iteration_id': self.iteration['id'], 'kind': 'code',
            'title': 'Update value', 'objective': 'Set VALUE to 2.',
            'input_document_versions': [self.document['version_id']],
            'requirement_ids': [self.requirement['id']],
            'write_paths': ['src'],
            'verification_commands': ['python3 -m unittest'],
        })
        self.client = self.Client()

    def test_execution_freezes_inputs_and_reconciles_real_file_changes(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.assertEqual(execution['status'], 'running')
        self.assertEqual(execution['input_state']['workspace_baseline']['id'],
                         self.baseline['id'])
        self.assertEqual(execution['input_state']['document_version_ids'],
                         [self.document['version_id']])
        self.assertNotEqual(execution['workdir'], str(self.workspace.resolve()))
        self.assertEqual(execution['source_workdir'], str(self.workspace.resolve()))
        self.assertEqual(execution['application_status'], 'pending')
        self.assertEqual(execution['input_state']['workspace_strategy'], 'isolated_copy')
        self.assertTrue(self.client.tools['bash'])
        self.assertIn('Allowed write paths: `src`', self.client.prompt)
        execution_workspace = Path(execution['workdir'])
        self.assertFalse((execution_workspace / 'node_modules').exists())
        (execution_workspace / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        completed = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        self.assertEqual(completed['status'], 'completed')
        self.assertIsNotNone(completed['after_snapshot_id'])
        self.assertEqual(completed['raw_state']['evidence']['filesystem']['modified'],
                         ['src/app.py'])
        self.assertTrue(completed['raw_state']['evidence']['filesystem']['scope_compliant'])
        self.assertTrue(completed['raw_state']['evidence']['verification']['all_planned_passed'])
        completion = completed['raw_state']['evidence']['completion_report']
        self.assertTrue(completion['valid'])
        self.assertEqual(completion['requirements'][0]['status'], 'satisfied')
        self.assertEqual(completed['raw_state']['evidence']['tool_calls']['commands'][0]['exit'], 0)
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 1\n')
        with self.assertRaisesRegex(ProjectStoreError, 'isolated execution result'):
            self.store.record_acceptance(
                self.task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        applied = apply_execution_result(
            self.store, self.project['id'], execution['id'])
        self.assertEqual(applied['application_status'], 'applied')
        self.assertIsNotNone(applied['applied_snapshot_id'])
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 2\n')
        accepted_baseline = latest_project_baseline(self.store, self.project['id'])
        self.assertNotEqual(accepted_baseline['id'], self.baseline['id'])
        self.assertEqual(applied['application_state']['accepted_baseline_id'],
                         accepted_baseline['id'])
        with self.assertRaisesRegex(ProjectStoreError, 'review document dependencies'):
            create_execution_iteration(self.store, self.project['id'], {
                'title': 'Stale follow-up', 'objective': 'Must review the old plan',
                'input_document_versions': [self.document['version_id']],
                'requirement_ids': [self.requirement['id']],
            })
        self.assertEqual(self.store.get_task(self.task['id'])['acceptance_status'], 'pending')
        exported = export_project(self.store, self.project['id'])
        self.assertEqual(exported['manifest']['schema'], 5)
        self.assertEqual(exported['manifest']['unapplied_execution_ids'], [])
        self.assertEqual(
            exported['manifest']['invalid_completion_report_execution_ids'], [])
        self.assertEqual(exported['manifest']['workspace_baseline_id'],
                         accepted_baseline['id'])
        self.assertEqual(exported['manifest']['counts']['executions'], 1)
        with zipfile.ZipFile(exported['archive']) as bundle:
            self.assertIn('iterations.md', bundle.namelist())
            records = json.loads(bundle.read('execution-records.json'))
            self.assertTrue(records['executions'][0]['raw_state']['evidence']
                            ['verification']['all_planned_passed'])
            self.assertIn(f"handoffs/{self.task['id']}.md", bundle.namelist())

    def test_reconcile_keeps_permission_as_first_class_interaction(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'permission'
        waiting = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        self.assertEqual(waiting['status'], 'waiting_permission')
        self.assertEqual(waiting['raw_state']['interaction']['request']['id'],
                         'per_execution')

    def test_follow_up_reuses_session_and_creates_a_new_snapshot_boundary(self):
        first = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        workdir = Path(first['workdir'])
        (workdir / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        first = reconcile_execution(
            self.store, self.project['id'], first['id'], self.client)

        second = continue_execution(
            self.store, self.project['id'], first['id'],
            {'instruction': 'Change VALUE to 3 and rerun the fixed check.'},
            self.client)

        self.assertEqual(self.client.created, 1)
        self.assertEqual(second['engine_session_id'], first['engine_session_id'])
        self.assertEqual(second['workdir'], first['workdir'])
        self.assertEqual(second['input_state']['continuation_of'], first['id'])
        self.assertEqual(second['status'], 'running')
        self.assertEqual(self.store.get_execution(first['id'])['application_status'],
                         'superseded')
        self.assertIn(f"Atlas execution ID: `{second['id']}`", self.client.prompt)
        self.assertIn('Change VALUE to 3', self.client.prompt)
        self.assertEqual(self.client.session_ids,
                         [first['engine_session_id'], first['engine_session_id']])
        second_before = self.store.get_snapshot(
            self.project['id'], second['before_snapshot_id'])
        first_after = self.store.get_snapshot(
            self.project['id'], first['after_snapshot_id'])
        self.assertEqual(second_before['manifest']['files'],
                         first_after['manifest']['files'])
        with self.assertRaisesRegex(ProjectStoreError, 'superseded'):
            apply_execution_result(self.store, self.project['id'], first['id'])

        (workdir / 'src/app.py').write_text('VALUE = 3\n')
        second = reconcile_execution(
            self.store, self.project['id'], second['id'], self.client)
        self.assertEqual(second['status'], 'completed')
        self.assertEqual(second['raw_state']['evidence']['filesystem']['modified'],
                         ['src/app.py'])
        applied = apply_execution_result(
            self.store, self.project['id'], second['id'])
        self.assertEqual(applied['application_status'], 'applied')
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 3\n')

    def test_follow_up_rejects_an_unrecorded_change_in_the_isolated_copy(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'completed'
        execution = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 9\n')
        with self.assertRaisesRegex(ProjectStoreError, 'changed after'):
            continue_execution(
                self.store, self.project['id'], execution['id'],
                {'instruction': 'Continue.'}, self.client)
        self.assertEqual(self.client.created, 1)

    def test_new_retry_supersedes_the_previous_unapplied_result(self):
        first = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'completed'
        first = reconcile_execution(
            self.store, self.project['id'], first['id'], self.client)
        retry = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.assertEqual(retry['status'], 'running')
        replaced = self.store.get_execution(first['id'])
        self.assertEqual(replaced['application_status'], 'superseded')
        self.assertEqual(
            replaced['application_state']['superseded_by_execution_id'], retry['id'])
        self.assertEqual(replaced['application_state']['reason'],
                         'replaced_by_new_execution')

    def test_missing_session_can_be_closed_as_a_stopped_execution(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)

        class MissingClient:
            def reconcile(self, _session_id):
                raise OpenCodeError(404, 'session unavailable')
            def abort(self, _session_id):
                raise OpenCodeError(404, 'session unavailable')

        unknown = reconcile_execution(
            self.store, self.project['id'], execution['id'], MissingClient())
        self.assertEqual(unknown['status'], 'unknown')
        stopped = stop_execution(
            self.store, self.project['id'], execution['id'], MissingClient())
        self.assertEqual(stopped['status'], 'stopped')
        self.assertEqual(stopped['raw_state']['engine_status'],
                         'session_unavailable_confirmed')
        self.assertIsNotNone(stopped['after_snapshot_id'])

    def test_http_continue_route_uses_the_existing_execution(self):
        import drafts_api
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'completed'
        execution = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        handler = object.__new__(drafts_api.Handler)
        handler.path = (f"/api/projects/{self.project['id']}/executions/"
                        f"{execution['id']}/continue")
        handler._body = lambda: {'instruction': 'Check the implementation again.'}
        handler._json = lambda value, code=200: (value, code)
        real_continue = drafts_api.continue_execution
        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
                patch.object(drafts_api, 'continue_execution',
                             side_effect=lambda store, project_id, execution_id, body:
                             real_continue(store, project_id, execution_id, body,
                                           self.client)):
            continued, code = handler.do_POST()
        self.assertEqual(code, 202)
        self.assertEqual(continued['input_state']['continuation_of'], execution['id'])

    def test_missing_engine_session_does_not_rewrite_terminal_execution(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'completed'
        completed = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        projection = dict(completed['raw_state'])
        projection['evidence'] = dict(projection['evidence'])
        projection['evidence'].pop('verification')
        with sqlite3.connect(self.store.path) as con:
            con.execute(
                'UPDATE execution SET raw_state_json=? WHERE id=?',
                (json.dumps(projection), completed['id']))

        class MissingClient:
            def reconcile(self, _session_id):
                raise OpenCodeError(404, 'session unavailable')

        recovered = reconcile_execution(
            self.store, self.project['id'], execution['id'], MissingClient())
        self.assertEqual(recovered['status'], 'completed')
        self.assertEqual(recovered['after_snapshot_id'], completed['after_snapshot_id'])

    def test_out_of_scope_change_is_preserved_and_flagged(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        execution_workspace = Path(execution['workdir'])
        (execution_workspace / 'README.md').write_text('# Changed outside scope\n')
        self.client.mode = 'completed'
        completed = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        filesystem = completed['raw_state']['evidence']['filesystem']
        self.assertFalse(filesystem['scope_compliant'])
        self.assertEqual(filesystem['out_of_scope_changes'], ['README.md'])
        self.assertEqual((self.workspace / 'README.md').read_text(), '# Pilot\n')
        with self.assertRaisesRegex(ProjectStoreError, 'out-of-scope'):
            apply_execution_result(
                self.store, self.project['id'], execution['id'])

    def test_result_application_detects_source_workspace_conflict(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        (self.workspace / 'src/app.py').write_text('VALUE = 9\n')
        with self.assertRaisesRegex(ProjectStoreError, 'changed since execution'):
            apply_execution_result(
                self.store, self.project['id'], execution['id'])
        recorded = self.store.get_execution(execution['id'])
        self.assertEqual(recorded['application_status'], 'conflict')
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 9\n')

    def test_http_apply_route_uses_the_recorded_isolated_result(self):
        import drafts_api
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        handler = object.__new__(drafts_api.Handler)
        handler.path = (f"/api/projects/{self.project['id']}/executions/"
                        f"{execution['id']}/apply")
        handler._body = lambda: {}
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            applied, code = handler.do_POST()
        self.assertEqual(code, 200)
        self.assertEqual(applied['application_status'], 'applied')
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 2\n')

    def test_result_application_rolls_back_a_partial_filesystem_failure(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        import execution_workspace
        replace = execution_workspace.os.replace
        calls = 0

        def fail_second(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('simulated write failure')
            return replace(source, target)

        with patch.object(execution_workspace.os, 'replace', side_effect=fail_second):
            with self.assertRaisesRegex(OSError, 'simulated write failure'):
                apply_execution_result(
                    self.store, self.project['id'], execution['id'])
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 1\n')
        self.assertEqual(
            self.store.get_execution(execution['id'])['application_status'], 'failed')

    def test_applied_result_recovers_an_interrupted_baseline_adoption(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        with patch('execution_service.capture_project_baseline',
                   side_effect=ProjectStoreError('simulated baseline interruption')):
            applied = apply_execution_result(
                self.store, self.project['id'], execution['id'])
        self.assertEqual(applied['application_status'], 'applied')
        self.assertIsNone(applied['application_state']['accepted_baseline_id'])
        self.assertIn('baseline_adoption_error', applied['application_state'])
        self.assertEqual(
            latest_project_baseline(self.store, self.project['id'])['id'],
            self.baseline['id'])

        recovered = apply_execution_result(
            self.store, self.project['id'], execution['id'])
        self.assertNotEqual(
            recovered['application_state']['accepted_baseline_id'], self.baseline['id'])
        self.assertEqual(
            latest_project_baseline(self.store, self.project['id'])['id'],
            recovered['application_state']['accepted_baseline_id'])

    def test_workspace_change_blocks_execution_before_engine_session(self):
        (self.workspace / 'src/app.py').write_text('VALUE = 9\n')
        with self.assertRaisesRegex(ProjectStoreError, 'accepted baseline'):
            start_execution(
                self.store, self.project['id'], self.task['id'], {}, self.client)
        self.assertEqual(self.client.created, 0)

    def test_task_boundaries_reject_analysis_writes_and_parent_paths(self):
        with self.assertRaisesRegex(ValueError, 'analysis tasks'):
            self.store.create_task(
                self.project['id'], 'Inspect', 'Read only', kind='analysis',
                write_paths=['src'])
        with self.assertRaisesRegex(ValueError, 'inside'):
            self.store.create_task(
                self.project['id'], 'Escape', 'Invalid', write_paths=['../other'])

    def test_isolated_copy_rejects_symlinks_outside_the_project(self):
        source = self.root / 'linked-workspace'
        source.mkdir()
        secret = self.root / 'outside.txt'
        secret.write_text('outside\n')
        (source / 'outside-link').symlink_to(secret)
        manifest = snapshot_workspace(source)
        with self.assertRaisesRegex(ProjectStoreError, 'symlink'):
            prepare_execution_workspace(
                self.root / 'isolated-state', self.project['id'], source, manifest)

    def test_completion_report_rejects_missing_or_mismatched_requirements(self):
        self.assertEqual(
            _completion_report('ordinary final text', [self.requirement['id']])['error'],
            'missing')
        report = {
            'schema': 1,
            'requirements': [{'id': 'req_other', 'status': 'satisfied',
                              'evidence': ['claimed']}],
            'unfinished': [], 'deviations': [],
        }
        parsed = _completion_report(
            'ATLAS_RESULT: ' + json.dumps(report), [self.requirement['id']])
        self.assertTrue(parsed['reported'])
        self.assertFalse(parsed['valid'])
        self.assertEqual(parsed['error'], 'requirement_ids_mismatch')

    def test_execution_rejects_a_project_database_inside_the_source(self):
        store = ProjectStore(self.workspace / 'atlas-project-state.sqlite')
        project = store.create_project(
            'Nested state', 'Reject self-changing state', self.workspace, 'existing')
        iteration = store.create_iteration(
            project['id'], 'Iteration', 'Keep state outside', [], [])
        task = store.create_task(
            project['id'], 'Change', 'Change one file', iteration_id=iteration['id'],
            write_paths=['src'])
        with self.assertRaisesRegex(ProjectStoreError, 'state database is inside'):
            start_execution(store, project['id'], task['id'], {}, self.client)


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
