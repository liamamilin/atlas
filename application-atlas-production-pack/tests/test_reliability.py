import concurrent.futures
from contextlib import closing, redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import re
from types import SimpleNamespace
import socket
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import zipfile
from unittest.mock import patch

import numpy as np

CODE = Path(__file__).resolve().parents[1]


def condition_result(requirement, result, note=""):
    return {
        "requirement_id": requirement["id"],
        "revision": requirement["revision"],
        "condition": requirement["acceptance_conditions"][0],
        "result": result,
        **({"note": note} if note else {}),
    }


sys.path.insert(0, str(CODE))
import atlas_runtime as rt
import atlas_cli
import classify as classifier
import draft_new
import drafts_api
import gate_check
import promote_draft as promote
from atlas_sources import SourceError, read_source, source_manifest
from opencode_client import OpenCodeClient, OpenCodeError, iter_sse
from execution_state import project_execution
from execution_workspace import apply_execution_workspace, prepare_execution_workspace
from execution_service import (
    _completion_report, _execution_evidence,
    apply_execution_result,
    continue_execution,
    create_iteration as create_execution_iteration,
    create_task as create_execution_task,
    rebase_iteration,
    reconcile_execution, reply_permission, start_execution, stop_execution,
    record_cli_run_evidence,
    cleanup_execution_workspace,
    start_cli_execution,
    run_cli_verification,
)
from project_store import ProjectStore, ProjectStoreError
from project_export import export_project
from project_generation import (
    apply_generation_item, execute_generation, generation_staleness, prepare_generation,
    read_generation,
)
from project_open_items import list_open_items, resolve_open_item
from project_baseline import (
    capture_project_baseline, check_project_changes, get_project_baseline,
    latest_project_baseline, list_project_baselines,
)
from handoff_bundle import build_handoff, validate_handoff, write_handoff
from sample_package import validate_package
from workspace_snapshot import compare_snapshots, snapshot_workspace
from review_store import fingerprint, corpus_revision, update_review, load_review


class ApiRequestBoundaryTests(unittest.TestCase):
    @staticmethod
    def handler(headers=None):
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        handler.headers = headers or {'Host': 'localhost:5173'}
        handler.path = '/api/health'
        handler._json = lambda value, code=200: (value, code)
        return handler

    def test_local_host_and_origin_allowlist(self):
        self.assertTrue(drafts_api._local_http_authority('localhost:5199'))
        self.assertTrue(drafts_api._local_http_authority('127.0.0.1'))
        self.assertTrue(drafts_api._local_http_origin('http://localhost:5173/'))
        self.assertFalse(drafts_api._local_http_authority('attacker.example'))
        self.assertFalse(drafts_api._local_http_authority('localhost:invalid'))
        self.assertFalse(drafts_api._local_http_origin('https://attacker.example'))
        handler = self.handler({
            'Host': 'localhost:5173',
            'Origin': 'http://localhost:5173',
            'Sec-Fetch-Site': 'same-origin',
        })
        payload, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertTrue(payload['ok'])

    def test_request_guard_rejects_unsafe_requests(self):
        cases = [
            ({'Host': 'attacker.example'}, 'GET', 403),
            ({
                'Host': 'localhost:5173',
                'Origin': 'https://attacker.example',
            }, 'GET', 403),
            ({
                'Host': 'localhost:5173',
                'Sec-Fetch-Site': 'cross-site',
            }, 'GET', 403),
            ({
                'Host': 'localhost:5173',
                'Content-Type': 'text/plain',
                'Content-Length': '2',
            }, 'POST', 415),
            ({
                'Host': 'localhost:5173',
                'Content-Type': 'application/json',
                'Transfer-Encoding': 'chunked',
            }, 'POST', 400),
            ({
                'Host': 'localhost:5173',
                'Content-Type': 'application/json',
                'Content-Length': str(drafts_api.MAX_REQUEST_BODY_BYTES + 1),
            }, 'POST', 413),
            ({
                'Host': 'localhost:5173',
                'Content-Type': 'application/json',
                'Content-Length': 'invalid',
            }, 'POST', 400),
        ]
        for headers, method, expected in cases:
            with self.subTest(headers=headers, method=method):
                handler = self.handler(headers)
                result, code = (handler.do_GET() if method == 'GET' else handler.do_POST())
                self.assertEqual(code, expected)
                self.assertIn('error', result)

    def test_json_body_is_bounded_and_must_be_an_object(self):
        handler = self.handler({
            'Host': 'localhost:5173',
            'Content-Type': 'application/json',
            'Content-Length': '7',
        })
        handler.rfile = io.BytesIO(b'{"x":1}')
        self.assertEqual(handler._body(), {'x': 1})

        handler = self.handler({
            'Host': 'localhost:5173',
            'Content-Type': 'application/json',
            'Content-Length': '1',
        })
        handler.rfile = io.BytesIO(b'[')
        with self.assertRaisesRegex(ValueError, 'valid JSON'):
            handler._body()

        handler.headers['Content-Length'] = '2'
        handler.rfile = io.BytesIO(b'[]')
        with self.assertRaisesRegex(ValueError, 'must be an object'):
            handler._body()


class WebFetchSafetyTests(unittest.TestCase):
    class Response:
        def __init__(self, status, headers=None, body=b''):
            self.status = status
            self.headers = headers or {}
            self.body = body

        def getheader(self, name, default=None):
            for key, value in self.headers.items():
                if key.lower() == name.lower():
                    return value
            return default

        def read(self, amount=None):
            return self.body if amount is None else self.body[:amount]

    class Connection:
        def __init__(self, response):
            self.response = response
            self.request_args = None
            self.closed = False

        def request(self, method, target, headers=None):
            self.request_args = (method, target, headers or {})

        def getresponse(self):
            return self.response

        def close(self):
            self.closed = True

    def test_web_fetch_extracts_text_through_validated_pinned_connection(self):
        connection = self.Connection(self.Response(
            200, {'Content-Type': 'text/html; charset=utf-8'},
            b'<html><style>hidden</style><script>bad()</script>'
            b'<h1>Public research</h1><p>Useful evidence.</p></html>'))
        with patch.object(drafts_api, '_resolve_public_addresses',
                          return_value=['93.184.216.34']), \
             patch.object(drafts_api, '_pinned_web_connection', return_value=connection):
            result = drafts_api._fetch_text('https://example.com/research')
        self.assertEqual(result, 'Public research Useful evidence.')
        self.assertEqual(connection.request_args[0], 'GET')
        self.assertEqual(connection.request_args[1], '/research')
        self.assertEqual(connection.request_args[2]['Host'], 'example.com')
        self.assertTrue(connection.closed)

    def test_web_fetch_rejects_non_http_credentials_and_local_targets(self):
        unsafe = [
            'file:///etc/passwd',
            'ftp://example.com/research',
            'https://user:secret@example.com/research',
            'http://127.0.0.1/internal',
            'http://10.0.0.1/internal',
            'http://169.254.169.254/latest/meta-data/',
            'http://[::1]/internal',
        ]
        for url in unsafe:
            with self.subTest(url=url), self.assertRaises(ValueError):
                drafts_api._fetch_text(url)

    def test_web_fetch_revalidates_redirect_targets(self):
        redirect = self.Connection(self.Response(
            302, {'Location': 'http://127.0.0.1/private'}))
        with patch.object(drafts_api, '_resolve_public_addresses',
                          return_value=['93.184.216.34']), \
             patch.object(drafts_api, '_pinned_web_connection', return_value=redirect) as connection:
            with self.assertRaisesRegex(ValueError, 'private, local, or reserved'):
                drafts_api._fetch_text('https://example.com/start')
        self.assertTrue(redirect.closed)
        self.assertEqual(connection.call_count, 1)

    def test_web_fetch_rejects_mixed_dns_binary_and_oversized_responses(self):
        mixed_dns = [
            (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', ('93.184.216.34', 443)),
            (socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, '', ('127.0.0.1', 443)),
        ]
        with patch.object(drafts_api.socket, 'getaddrinfo', return_value=mixed_dns):
            with self.assertRaisesRegex(ValueError, 'private, local, or reserved'):
                drafts_api._resolve_public_addresses('mixed.example', 443)

        binary = self.Connection(self.Response(
            200, {'Content-Type': 'application/octet-stream'}, b'binary'))
        with patch.object(drafts_api, '_resolve_public_addresses',
                          return_value=['93.184.216.34']), \
             patch.object(drafts_api, '_pinned_web_connection', return_value=binary):
            with self.assertRaisesRegex(ValueError, 'supported text format'):
                drafts_api._fetch_text('https://example.com/file')

        oversized = self.Connection(self.Response(
            200, {
                'Content-Type': 'text/plain',
                'Content-Length': str(drafts_api.WEB_FETCH_MAX_BYTES + 1),
            }, b'x'))
        with patch.object(drafts_api, '_resolve_public_addresses',
                          return_value=['93.184.216.34']), \
             patch.object(drafts_api, '_pinned_web_connection', return_value=oversized):
            with self.assertRaisesRegex(ValueError, 'too large'):
                drafts_api._fetch_text('https://example.com/large')


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

    def test_missing_source_manifest_returns_a_stable_empty_contract(self):
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        handler.headers = {'Host': 'localhost:5173'}
        handler.path = '/api/sources/missing-type'
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PACK', str(self.pack)):
            payload, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual(payload, {'slug': 'missing-type', 'sources': []})

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

    def test_reconcile_treats_missing_diff_as_empty(self):
        self.responses.extend([
            {'ses_abc': {'type': 'busy'}},
            {'id': 'ses_abc'},
            [{'info': {'id': 'msg_one'}, 'parts': []}],
            [],
            [{'id': 'per_one', 'sessionID': 'ses_abc'}],
            [{'id': 'que_one', 'sessionID': 'ses_abc'}],
        ])
        with patch.object(self.client, 'diff', side_effect=OpenCodeError(404, 'not ready')), \
             patch.object(self.client, 'pending_permissions', side_effect=OpenCodeError(404, 'not ready')), \
             patch.object(self.client, 'pending_questions', side_effect=OpenCodeError(404, 'not ready')):
            result = self.client.reconcile('ses_abc')
        self.assertEqual(result['engine_diff'], [])
        self.assertEqual(result['pending_permissions'], [])
        self.assertEqual(result['pending_questions'], [])
        self.assertEqual(result['status']['type'], 'busy')

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

    def test_v2_transport_uses_api_auth_and_normalizes_messages(self):
        client = OpenCodeClient(
            'http://127.0.0.1:4098', '/tmp/project',
            major_version=2, username='opencode', password='v2-secret',
            permissions=[{'action': 'shell', 'resource': '*', 'effect': 'deny'}])
        # Use the same small response adapter as the V1 tests, with an explicit
        # opener so the request sequence remains inspectable.
        def opener(request, timeout):
            self.requests.append((request, timeout))
            return self.Response(self.responses.pop(0))
        client._opener = opener
        self.responses.extend([
            {'version': '2.0.13', 'pid': 1, 'urls': [], 'paths': {'tmp': '/tmp'}},
            {'data': {'id': 'ses_v2', 'title': 'probe'}},
            None, None,
            {'data': {'id': 'msg_v2', 'sessionID': 'ses_v2', 'type': 'user',
                      'payload': {'text': 'hello'}}},
            {'data': {'ses_v2': {'type': 'running'}}},
            {'data': {'id': 'ses_v2'}},
            {'data': [
                {'id': 'msg_a', 'type': 'assistant', 'time': {'completed': 1},
                 'finish': 'stop', 'content': [{'type': 'text', 'text': 'done'}]},
                {'id': 'msg_v2', 'type': 'user', 'text': 'hello'},
            ], 'cursor': {}},
            {'data': []}, {'data': []}, {'data': []},
        ])
        self.assertEqual(client.health()['version'], '2.0.13')
        session = client.create_session('probe')
        self.assertEqual(session['id'], 'ses_v2')
        result = client.send_message_async(
            'ses_v2', 'hello', 'opencode-go', 'space-bunny-free')
        self.assertEqual(result['id'], 'msg_v2')
        current = client.reconcile('ses_v2')
        self.assertEqual(current['status']['type'], 'running')
        self.assertEqual(current['messages'][1]['info']['parentID'], 'msg_v2')
        self.assertEqual(current['messages'][1]['parts'][0]['text'], 'done')
        request_paths = [request.full_url for request, _ in self.requests]
        self.assertTrue(all('/api/' in path for path in request_paths))
        self.assertIn('Authorization', self.requests[0][0].headers)
        self.assertTrue(self.requests[0][0].headers['Authorization'].startswith('Basic '))
        self.assertEqual(
            json.loads(self.requests[1][0].data)['location'],
            {'directory': '/tmp/project'})
        self.assertEqual(
            json.loads(self.requests[1][0].data)['permissions'],
            [{'action': 'shell', 'resource': '*', 'effect': 'deny'}])

    def test_v2_permission_and_form_replies_use_session_scoped_endpoints(self):
        client = OpenCodeClient(
            'http://127.0.0.1:4098', '/tmp/project', major_version=2,
            username='opencode', password='v2-secret')
        requests = []
        def opener(request, timeout):
            requests.append(request)
            if request.method == 'GET':
                return self.Response(
                    {'data': [{'id': 'frm_v2', 'sessionID': 'ses_v2', 'title': 'Choose',
                               'fields': [{'key': 'option', 'type': 'string'}]}]})
            return self.Response(None)
        client._opener = opener
        forms = client.pending_questions('ses_v2')
        self.assertEqual(forms[0]['id'], 'frm_v2')
        client.reply_question('frm_v2', [['yes']], session_id='ses_v2')
        self.assertIn('/api/session/ses_v2/form/frm_v2/reply', requests[1].full_url)
        self.assertEqual(json.loads(requests[1].data), {'answer': {'option': 'yes'}})

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

    def test_snapshot_rejects_broad_roots_and_resource_limits(self):
        with self.assertRaisesRegex(ValueError, 'too broad'):
            snapshot_workspace('/')
        with self.assertRaisesRegex(ValueError, 'too broad'):
            snapshot_workspace(Path.home())
        with patch('workspace_snapshot.MAX_SNAPSHOT_FILES', 1):
            with self.assertRaisesRegex(ValueError, 'file count'):
                snapshot_workspace(self.root)
        with patch('workspace_snapshot.MAX_SNAPSHOT_BYTES', 1):
            with self.assertRaisesRegex(ValueError, 'byte limit'):
                snapshot_workspace(self.root)

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

    def test_partial_assistant_message_without_terminal_outcome_stays_running(self):
        result = project_execution({
            'status': {'type': 'idle'},
            'session': {'outcome': None},
            'messages': [{'info': {
                'id': 'msg_partial', 'parentID': 'msg_user', 'role': 'assistant',
            }}],
        }, 'msg_user')
        self.assertEqual(result['state'], 'running')

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

    def test_project_delete_removes_owned_records_preserves_workspace_and_blocks_active_run(self):
        workspace = Path(self.project['workspace'])
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / 'keep.txt').write_text('source workspace stays\n')
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed evidence', read_status='read')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the evidence', 'current', 'Relevant source',
            ['Evidence remains visible'], [reference['id']])
        self.store.record_decision(
            self.project['id'], 'Use the source', 'It is relevant', [reference['id']])
        document = self.store.create_document(
            self.project['id'], 'analysis', 'Analysis', 'Version one',
            [{'kind': 'reference', 'id': reference['id']}])
        self.store.add_document_version(document['id'], 'Version two')
        self.store.save_snapshot(
            self.project['id'], {'root': str(workspace), 'files': []}, 'observed')
        task = self.store.create_task(
            self.project['id'], 'Read it', 'Inspect the source', kind='analysis')
        execution = self.store.create_execution(task['id'], 'opencode', 'ses_delete')

        with self.assertRaisesRegex(ProjectStoreError, 'active execution'):
            self.store.delete_project(self.project['id'])
        self.store.update_execution(execution['id'], {'state': 'stopped'})
        result = self.store.delete_project(self.project['id'])

        self.assertTrue(result['deleted'])
        self.assertTrue(result['workspace_preserved'])
        self.assertEqual((workspace / 'keep.txt').read_text(), 'source workspace stays\n')
        self.assertEqual(result['deleted_records']['document_versions'], 2)
        with self.assertRaisesRegex(ProjectStoreError, 'project not found'):
            self.store.get_project(self.project['id'])
        with sqlite3.connect(self.store.path) as con:
            for table in ('project', 'reference', 'requirement', 'decision', 'document',
                          'document_version', 'task', 'execution', 'workspace_snapshot'):
                self.assertEqual(con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0], 0)

    def test_project_delete_blocks_an_applying_result(self):
        task = self.store.create_task(
            self.project['id'], 'Apply result', 'Apply a reviewed result', kind='code')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_apply_delete', application_status='pending')
        self.store.update_execution(execution['id'], {'state': 'completed'})
        self.store.record_execution_application(
            execution['id'], 'applying', {'apply_intent': {'after_snapshot_id': 'snap_pending'}})
        with self.assertRaisesRegex(ProjectStoreError, 'unresolved execution result'):
            self.store.delete_project(self.project['id'])
        with self.assertRaisesRegex(ProjectStoreError, 'already being applied'):
            self.store.record_execution_application(
                execution['id'], 'applying', {'retry': True})
        self.store.record_execution_application(execution['id'], 'superseded', {'error': 'test'})
        result = self.store.delete_project(self.project['id'])
        self.assertTrue(result['deleted'])

    def test_project_delete_uses_generation_lifecycle_lock(self):
        import drafts_api
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed evidence', read_status='read')
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        entered = threading.Event()
        release = threading.Event()

        def runner(directory, _run):
            request = json.loads((directory / 'input.json').read_text())
            entered.set()
            release.wait(5)
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis\n\nFixed evidence.',
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_lifecycle'})

        worker = threading.Thread(
            target=execute_generation,
            args=(self.store, self.project['id'], run['id']),
            kwargs={'runner': runner},
        )
        worker.start()
        self.assertTrue(entered.wait(2))
        with self.assertRaisesRegex(ProjectStoreError, 'active generation|lifecycle'):
            drafts_api.delete_project(
                self.project['id'], {'confirm': self.project['id']}, store=self.store)
        self.assertTrue(self.store.get_project(self.project['id']))
        release.set()
        worker.join(5)
        self.assertFalse(worker.is_alive())
        result = drafts_api.delete_project(
            self.project['id'], {'confirm': self.project['id']}, store=self.store)
        self.assertTrue(result['deleted'])

    def test_artifact_cleanup_does_not_follow_symlink_roots(self):
        import drafts_api
        outside = self.root / 'outside'
        outside.mkdir()
        target = outside / self.project['id']
        target.mkdir()
        (target / 'keep.txt').write_text('keep')
        root = self.root / 'exports'
        root.symlink_to(outside, target_is_directory=True)
        removed, error = drafts_api._remove_project_artifact_root(
            root, self.project['id'])
        self.assertFalse(removed)
        self.assertIn('symlink', error)
        self.assertTrue((target / 'keep.txt').exists())

    def test_empty_workspace_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'workspace'):
            self.store.create_project('Invalid', 'No workspace', '  ', 'existing')
        generated = self.store.create_project('Idea', 'Start with an idea', '', 'new')
        self.assertTrue(generated['workspace'].endswith('/workspaces/' + generated['id']))
        self.assertTrue(Path(generated['workspace']).is_dir())
        baseline = capture_project_baseline(self.store, generated['id'])
        self.assertEqual(baseline['inventory']['file_count'], 0)
        explicit = self.store.create_project(
            'Explicit idea', 'Create the requested workspace', self.root / 'new-workspace', 'new')
        self.assertTrue(Path(explicit['workspace']).is_dir())

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

    def test_nested_workspace_git_state_ignores_parent_repository_siblings(self):
        workspace = Path(self.project['workspace'])
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / 'tracked.txt').write_text('stable\n')
        subprocess.run(['git', 'init'], cwd=self.root, check=True,
                       capture_output=True)
        subprocess.run(['git', 'config', 'user.name', 'Atlas Test'],
                       cwd=self.root, check=True)
        subprocess.run(['git', 'config', 'user.email', 'atlas@example.test'],
                       cwd=self.root, check=True)
        subprocess.run(['git', 'add', 'workspace/tracked.txt'], cwd=self.root,
                       check=True)
        subprocess.run(['git', 'commit', '-m', 'baseline'], cwd=self.root,
                       check=True, capture_output=True)

        baseline = capture_project_baseline(self.store, self.project['id'])
        (self.root / 'unrelated-runtime.txt').write_text('outside project\n')
        checked = check_project_changes(self.store, self.project['id'])

        self.assertEqual(checked['current']['content_fingerprint'],
                         baseline['content_fingerprint'])
        self.assertFalse(checked['changes']['git_state_changed'])
        self.assertEqual(checked['current']['git']['changes'], [])

        (workspace / 'local.txt').write_text('inside project\n')
        local_change = check_project_changes(self.store, self.project['id'])
        self.assertNotEqual(local_change['current']['content_fingerprint'],
                            baseline['content_fingerprint'])
        self.assertTrue(local_change['changes']['git_worktree_state_changed'])

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
        workspace.mkdir(parents=True, exist_ok=True)
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
        self.assertIn('acceptance-migration.json', names)
        self.assertEqual(exported['manifest']['legacy_acceptance_migration']['total_bindings'], 0)
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

    def test_open_items_merge_dispositions_and_convert_to_records(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed local evidence', note='Use the fixed boundary', read_status='reviewed')
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())

        def runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [{'question': 'Who owns review?', 'why': 'The evidence is silent.',
                               'affects': ['analysis']}],
                'requirements': [],
                'conflicts': [{'summary': 'Two owners claim review',
                               'impact': 'Ownership is ambiguous',
                               'evidence': [{'kind': 'reference', 'id': reference['id']}]}],
                'suggestions': [{'summary': 'Show the source version',
                                 'reason': 'It keeps review traceable',
                                 'evidence': [{'kind': 'reference', 'id': reference['id']}]}],
                'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis\n\nOne open ownership question.',
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_fake'})

        execute_generation(self.store, self.project['id'], run['id'], runner=runner)
        items = list_open_items(self.store, self.project['id'])
        self.assertEqual(len(items), 3)
        self.assertTrue(all(item['status'] == 'open' for item in items))
        self.assertTrue(all(item['current'] for item in items))
        by_kind = {item['kind']: item for item in items}
        self.assertEqual(by_kind['question']['affects'], ['analysis'])
        self.assertEqual(by_kind['suggestion']['reference_ids'], [reference['id']])

        with self.assertRaisesRegex(ValueError, 'note is required'):
            resolve_open_item(self.store, self.project['id'], {
                'run_id': run['id'], 'item_kind': 'question',
                'item_index': by_kind['question']['index'],
                'item_key': by_kind['question']['key'],
                'status': 'answered', 'note': '',
            })
        answered = resolve_open_item(self.store, self.project['id'], {
            'run_id': run['id'], 'item_kind': 'question',
            'item_index': by_kind['question']['index'],
            'item_key': by_kind['question']['key'],
            'status': 'answered', 'convert': 'decision',
            'note': 'The user owns review.',
        })
        self.assertEqual(answered['item']['status'], 'answered')
        self.assertIsNotNone(answered['decision_id'])
        decision = next(item for item in self.store.list_decisions(self.project['id'])
                        if item['id'] == answered['decision_id'])
        self.assertEqual(decision['statement'], 'The user owns review.')

        accepted = resolve_open_item(self.store, self.project['id'], {
            'run_id': run['id'], 'item_kind': 'suggestion',
            'item_index': by_kind['suggestion']['index'],
            'item_key': by_kind['suggestion']['key'],
            'status': 'accepted', 'convert': 'requirement',
            'note': 'Add it as a candidate requirement.',
        })
        self.assertEqual(accepted['item']['status'], 'accepted')
        requirement = next(item for item in self.store.list_requirements(self.project['id'])
                           if item['id'] == accepted['requirement_id'])
        self.assertIsNone(requirement['confirmed_scope'])
        self.assertEqual(requirement['reference_ids'], [reference['id']])

        dismissed = resolve_open_item(self.store, self.project['id'], {
            'run_id': run['id'], 'item_kind': 'conflict',
            'item_index': by_kind['conflict']['index'],
            'item_key': by_kind['conflict']['key'],
            'status': 'dismissed', 'note': 'Not a conflict after review.',
        })
        self.assertEqual(dismissed['item']['status'], 'dismissed')
        self.assertIsNone(dismissed['decision_id'])

        deferred = resolve_open_item(self.store, self.project['id'], {
            'run_id': run['id'], 'item_kind': 'question',
            'item_index': by_kind['question']['index'],
            'item_key': by_kind['question']['key'],
            'status': 'deferred', 'note': '',
        })
        self.assertEqual(deferred['item']['status'], 'deferred')
        current = list_open_items(self.store, self.project['id'])
        self.assertEqual(len(current), 3)
        self.assertEqual(len([item for item in current
                              if item['kind'] == 'question' and item['run_id'] == run['id']]), 1)
        with self.assertRaisesRegex(ProjectStoreError, 'changed'):
            resolve_open_item(self.store, self.project['id'], {
                'run_id': run['id'], 'item_kind': 'question',
                'item_index': by_kind['question']['index'],
                'item_key': 'question:deadbeefdeadbeef',
                'status': 'deferred', 'note': '',
            })

    def test_generation_apply_is_receipt_backed_and_staleness_aware(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed local evidence', note='Use the fixed boundary', read_status='reviewed')
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())

        def runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'conflicts': [], 'suggestions': [],
                'requirements': [{
                    'key': 'keep-local', 'content': 'Keep the workflow local',
                    'recommended_scope': 'current',
                    'recommendation_reason': 'The fixed evidence supports it',
                    'acceptance_conditions': ['Works without an account'],
                    'reference_ids': [reference['id']],
                }],
                'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis\n\nLocal only.',
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_fake'})

        execute_generation(self.store, self.project['id'], run['id'], runner=runner)
        applied = apply_generation_item(
            self.store, self.project['id'], run['id'], 'requirement', 0)
        current = read_generation(self.store, self.project['id'], run['id'])
        staleness = generation_staleness(self.store, self.project['id'], current)
        self.assertTrue(staleness['known'])
        self.assertFalse(staleness['stale'])

        stored = json.loads((directory / 'run.json').read_text())
        stored['applied']['requirements'] = {}
        (directory / 'run.json').write_text(json.dumps(stored))
        again = apply_generation_item(
            self.store, self.project['id'], run['id'], 'requirement', 0)
        self.assertEqual(again['created']['id'], applied['created']['id'])
        self.assertEqual(len(self.store.list_requirements(self.project['id'])), 1)

        self.store.add_reference(
            self.project['id'], 'atlas:application', 'second', 'source-v1',
            excerpt='More evidence', note='Added later', read_status='read')
        current = read_generation(self.store, self.project['id'], run['id'])
        self.assertTrue(generation_staleness(
            self.store, self.project['id'], current)['stale'])
        with self.assertRaisesRegex(ProjectStoreError, 'stale'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 0)
        confirmed = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0,
            confirm_stale=True)
        self.assertEqual(confirmed['created']['kind'], 'analysis')
        self.assertEqual(len(self.store.list_documents(self.project['id'])), 1)

    def test_generation_without_basis_fingerprint_fails_closed(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed evidence')
        run = prepare_generation(self.store, self.project['id'], 'analysis')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())

        def runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'conflicts': [], 'suggestions': [],
                'requirements': [{
                    'key': 'unknown-basis', 'content': 'Require explicit review',
                    'recommended_scope': 'current', 'recommendation_reason': 'fixed',
                    'acceptance_conditions': ['Reviewed'], 'reference_ids': [reference['id']],
                }], 'documents': [{
                    'document_id': None, 'kind': 'analysis', 'title': 'Analysis',
                    'content': '# Analysis\n\nVerified.', 'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_unknown'})

        execute_generation(self.store, self.project['id'], run['id'], runner=runner)
        stored = json.loads((directory / 'run.json').read_text())
        stored.pop('basis_fingerprint', None)
        (directory / 'run.json').write_text(json.dumps(stored))
        with self.assertRaisesRegex(ProjectStoreError, 'unknown'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'requirement', 0)
        applied = apply_generation_item(
            self.store, self.project['id'], run['id'], 'requirement', 0,
            confirm_stale=True)
        self.assertTrue(applied['created']['id'])

    def test_generation_staleness_tracks_confirmation_and_document_state(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed evidence')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the accepted scope', 'current', 'Supported',
            ['Scope is confirmed'], [reference['id']])
        confirmation_run = prepare_generation(self.store, self.project['id'], 'analysis')
        self.assertFalse(generation_staleness(
            self.store, self.project['id'], confirmation_run)['stale'])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        self.assertTrue(generation_staleness(
            self.store, self.project['id'], confirmation_run)['stale'])

        document = self.store.create_document(
            self.project['id'], 'analysis', 'Analysis', 'Initial analysis',
            [{'kind': 'reference', 'id': reference['id']}])
        approval_run = prepare_generation(self.store, self.project['id'], 'analysis')
        self.assertFalse(generation_staleness(
            self.store, self.project['id'], approval_run)['stale'])
        self.store.review_document(
            self.project['id'], document['id'], 'approved', 'Reviewed')
        self.assertTrue(generation_staleness(
            self.store, self.project['id'], approval_run)['stale'])

        version_run = prepare_generation(self.store, self.project['id'], 'analysis')
        self.store.add_document_version(
            document['id'], 'Newer analysis', document['basis'],
            expected_current_version=1, change_summary='Changed after generation')
        self.assertTrue(generation_staleness(
            self.store, self.project['id'], version_run)['stale'])

    def test_value_analysis_is_advisory_grounded_and_never_changes_scope(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Teams compare alternatives before committing to a workflow.',
            note='Use only as an alternative pattern', read_status='reviewed')
        requirement = self.store.create_requirement(
            self.project['id'], 'Let a user review the proposed workflow', 'later',
            'Unconfirmed idea', ['A review view is visible'], [reference['id']])
        original_requirements = self.store.list_requirements(self.project['id'])
        run = prepare_generation(self.store, self.project['id'], 'value')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual(request['document_kinds'], ['value-analysis'])
        self.assertIsNone(requirement['confirmed_scope'])
        prompt = (directory / 'prompt.md').read_text()
        self.assertIn('advice for the user to weigh', prompt)
        self.assertIn('never changes scope', prompt)

        sections = (
            ('Evidence-backed observations / 有依据的观察',
             f'- [Evidence: {reference["id"]}] The fixed reference describes comparing alternatives.'),
            ('User and problem unknowns / 用户与问题未知',
             '- [Unknown] Target users, demand, price, and frequency remain unknown.'),
            ('Existing alternatives / 现有替代',
             '- [Inference] A manual comparison workflow is a possible alternative.'),
            ('Differentiation hypotheses / 差异化假设',
             '- [Hypothesis] Review traceability may reduce rework.'),
            ('Cost and risk signals / 成本与风险信号',
             '- [Unknown] Integration and maintenance cost are unknown.'),
            ('Small validation experiments / 小型验证实验',
             '- [Validation advice] Interview five target users and test a paper workflow.'),
            ('Advisory summary / 建议摘要',
             '[Advice] Consider testing the problem and workflow before expanding scope.'),
        )
        content = '# Value analysis\n\n' + '\n\n'.join(
            f'## {heading}\n\n{body}' for heading, body in sections)

        def value_runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'value-analysis',
                    'title': 'Value analysis', 'content': content,
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {'engine_session_id': 'ses_value'})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=value_runner)
        self.assertEqual(completed['result']['requirements'], [])
        saved = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0)['created']
        self.assertEqual(saved['kind'], 'value-analysis')
        self.assertEqual(self.store.list_requirements(self.project['id']), original_requirements)

        invalid = prepare_generation(self.store, self.project['id'], 'value')
        invalid_directory = (self.store.path.parent / 'generation-runs' /
                             self.project['id'] / invalid['id'])
        invalid_request = json.loads((invalid_directory / 'input.json').read_text())
        existing = self.store.get_document(saved['id'])

        def verdict_runner(_directory, _run):
            return ({
                'input_fingerprint': invalid_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': existing['id'], 'kind': 'value-analysis',
                    'title': 'Value analysis',
                    'content': content.replace(
                        'Consider testing the problem and workflow before expanding scope.',
                        '评分：92/100。值得开发。'),
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'score or build verdict'):
            execute_generation(
                self.store, self.project['id'], invalid['id'], runner=verdict_runner)

        evidence_run = prepare_generation(self.store, self.project['id'], 'value')
        evidence_directory = (self.store.path.parent / 'generation-runs' /
                              self.project['id'] / evidence_run['id'])
        evidence_request = json.loads((evidence_directory / 'input.json').read_text())

        def evidence_runner(_directory, _run):
            return ({
                'input_fingerprint': evidence_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': existing['id'], 'kind': 'value-analysis',
                    'title': 'Value analysis',
                    'content': content.replace(
                        f'[Evidence: {reference["id"]}]',
                        '[Evidence: ref_unknown]'),
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'unknown evidence marker'):
            execute_generation(
                self.store, self.project['id'], evidence_run['id'], runner=evidence_runner)

        status_run = prepare_generation(self.store, self.project['id'], 'value')
        status_directory = (self.store.path.parent / 'generation-runs' /
                            self.project['id'] / status_run['id'])
        status_request = json.loads((status_directory / 'input.json').read_text())

        def status_runner(_directory, _run):
            return ({
                'input_fingerprint': status_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': existing['id'], 'kind': 'value-analysis',
                    'title': 'Value analysis',
                    'content': content.replace(
                        'Consider testing the problem',
                        'The confirmed requirement suggests testing the problem'),
                    'basis': [{'kind': 'reference', 'id': reference['id']}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'misstates a pending requirement'):
            execute_generation(
                self.store, self.project['id'], status_run['id'], runner=status_runner)

        requirement_run = prepare_generation(self.store, self.project['id'], 'value')
        requirement_directory = (self.store.path.parent / 'generation-runs' /
                                 self.project['id'] / requirement_run['id'])
        requirement_request = json.loads((requirement_directory / 'input.json').read_text())

        def requirement_runner(_directory, _run):
            result, metadata = value_runner(_directory, _run)
            result['input_fingerprint'] = requirement_request['input_fingerprint']
            result['documents'][0]['document_id'] = existing['id']
            result['requirements'] = [{
                'key': 'auto-scope', 'content': 'Build it now',
                'recommended_scope': 'current', 'recommendation_reason': 'Advice',
                'acceptance_conditions': ['It exists'], 'reference_ids': [reference['id']],
            }]
            return result, metadata

        with self.assertRaisesRegex(ValueError, 'only allowed in analysis or improvement'):
            execute_generation(
                self.store, self.project['id'], requirement_run['id'],
                runner=requirement_runner)

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
        failed_run = read_generation(self.store, self.project['id'], run['id'])
        self.assertEqual(failed_run['status'], 'failed')
        self.assertEqual(failed_run['error_code'], 'invalid_result')

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
        with self.assertRaisesRegex(ProjectStoreError, 'stale'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 0)
        self.assertEqual(self.store.get_document(document['id'])['content'],
                         '# PRD\n\nNewer human edit')

    def test_document_bundle_is_complete_ordered_and_applied_by_dependency(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:type', 'sample', 'v1', excerpt='Fixed evidence')
        requirement = self.store.create_requirement(
            self.project['id'], 'Ship the approved workflow', 'current', 'Source support',
            ['The workflow is observable'], [reference['id']])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')

        incomplete = prepare_generation(
            self.store, self.project['id'], 'documents',
            ['acceptance-plan', 'product-requirements'])
        incomplete_directory = (self.store.path.parent / 'generation-runs' /
                                self.project['id'] / incomplete['id'])
        incomplete_request = json.loads((incomplete_directory / 'input.json').read_text())

        def incomplete_runner(_directory, _run):
            return ({
                'input_fingerprint': incomplete_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': None, 'kind': 'product-requirements', 'title': 'PRD',
                    'content': '# PRD',
                    'basis': [{'kind': 'requirement', 'id': requirement['id']}],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'missing: acceptance-plan'):
            execute_generation(
                self.store, self.project['id'], incomplete['id'], runner=incomplete_runner)

        run = prepare_generation(
            self.store, self.project['id'], 'documents',
            ['acceptance-plan', 'technical-plan', 'product-requirements'])
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual(request['document_kinds'], [
            'product-requirements', 'technical-plan', 'acceptance-plan'])
        self.assertEqual(request['document_dependencies']['acceptance-plan'], [
            'product-requirements', 'technical-plan'])

        def bundle_runner(_directory, _run):
            documents = []
            for kind, title in (
                    ('acceptance-plan', 'Acceptance'), ('technical-plan', 'Technical'),
                    ('product-requirements', 'PRD')):
                documents.append({
                    'document_id': None, 'kind': kind, 'title': title,
                    'content': f'# {title}',
                    'basis': [{'kind': 'requirement', 'id': requirement['id']}],
                })
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': documents,
            }, {})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=bundle_runner)
        self.assertEqual([item['kind'] for item in completed['result']['documents']], [
            'product-requirements', 'technical-plan', 'acceptance-plan'])
        self.assertEqual(completed['result']['documents'][1]['depends_on'], [
            'product-requirements'])
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        handler.path = (f"/api/projects/{self.project['id']}/generation-runs/"
                        f"{run['id']}/apply")
        handler._body = lambda: {'item_kind': 'document', 'index': 2}
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            dependency_error, code = handler.do_POST()
        self.assertEqual(code, 409)
        self.assertIn('product-requirements', dependency_error['error'])
        with self.assertRaisesRegex(ProjectStoreError, 'dependency.*product-requirements'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 2)

        product = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0)
        self.assertEqual(product['run']['applied']['documents']['0']['version_id'],
                         product['created']['version_id'])
        with self.assertRaisesRegex(ProjectStoreError, 'dependency.*technical-plan'):
            apply_generation_item(
                self.store, self.project['id'], run['id'], 'document', 2)

        technical = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 1)
        self.assertIn(
            product['created']['version_id'],
            [item['id'] for item in technical['created']['basis']])
        acceptance = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 2)
        self.assertEqual(
            {product['created']['version_id'], technical['created']['version_id']},
            {item['id'] for item in acceptance['created']['basis']
             if item['kind'] == 'document_version'})

    def test_section_revision_preserves_outside_content_and_checks_version(self):
        original = (
            '# Plan\n\nHuman introduction.\n\n## Scope\n\nKeep this manual sentence.\n\n'
            '### Details\n\nOld detail.\n\n## Constraints\n\nHuman constraint.\n')
        document = self.store.create_document(
            self.project['id'], 'development-plan', 'Delivery plan', original,
            [{'source': 'user-import', 'fingerprint': 'sha256:manual'}],
            author='human', change_summary='Manual plan')
        run = prepare_generation(
            self.store, self.project['id'], 'revision', document_id=document['id'],
            section_heading='## Scope',
            revision_instruction='Clarify the detail while retaining the manual sentence.')
        directory = (self.store.path.parent / 'generation-runs' /
                     self.project['id'] / run['id'])
        request = json.loads((directory / 'input.json').read_text())
        self.assertEqual(request['revision']['version_id'], document['version_id'])
        self.assertIn('## Scope', (directory / 'input.md').read_text())

        revised = original.replace('Old detail.', 'New detail with an observable outcome.')

        def revision_runner(_directory, _run):
            return ({
                'input_fingerprint': request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': document['id'], 'kind': 'development-plan',
                    'title': 'Delivery plan', 'content': revised, 'basis': [],
                }],
            }, {})

        completed = execute_generation(
            self.store, self.project['id'], run['id'], runner=revision_runner)
        candidate = completed['result']['documents'][0]
        self.assertIn('-Old detail.', candidate['diff'])
        self.assertIn('+New detail with an observable outcome.', candidate['diff'])
        saved = apply_generation_item(
            self.store, self.project['id'], run['id'], 'document', 0)['created']
        self.assertEqual(saved['content'], revised)
        self.assertEqual(saved['author'], 'ai')
        self.assertEqual(saved['basis'], document['basis'])
        self.assertIn('## Scope', saved['change_summary'])

        outside = prepare_generation(
            self.store, self.project['id'], 'revision', document_id=document['id'],
            section_heading='## Constraints', revision_instruction='Clarify the constraint.')
        outside_directory = (self.store.path.parent / 'generation-runs' /
                             self.project['id'] / outside['id'])
        outside_request = json.loads((outside_directory / 'input.json').read_text())

        def outside_runner(_directory, _run):
            return ({
                'input_fingerprint': outside_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': document['id'], 'kind': 'development-plan',
                    'title': 'Delivery plan',
                    'content': revised.replace('Human introduction.', 'Changed outside.')
                    .replace('Human constraint.', 'Clarified constraint.'),
                    'basis': [],
                }],
            }, {})

        with self.assertRaisesRegex(ValueError, 'outside the selected section'):
            execute_generation(
                self.store, self.project['id'], outside['id'], runner=outside_runner)

        stale = prepare_generation(
            self.store, self.project['id'], 'revision', document_id=document['id'],
            section_heading='## Constraints', revision_instruction='Clarify the constraint.')
        stale_directory = (self.store.path.parent / 'generation-runs' /
                           self.project['id'] / stale['id'])
        stale_request = json.loads((stale_directory / 'input.json').read_text())
        stale_source = self.store.get_document(document['id'])

        def stale_runner(_directory, _run):
            return ({
                'input_fingerprint': stale_request['input_fingerprint'],
                'questions': [], 'requirements': [], 'conflicts': [], 'suggestions': [],
                'documents': [{
                    'document_id': document['id'], 'kind': 'development-plan',
                    'title': 'Delivery plan',
                    'content': stale_source['content'].replace(
                        'Human constraint.', 'Clarified constraint.'),
                    'basis': [],
                }],
            }, {})

        execute_generation(self.store, self.project['id'], stale['id'], runner=stale_runner)
        self.store.add_document_version(
            document['id'], stale_source['content'] + '\nExternal edit.\n', stale_source['basis'],
            expected_current_version=stale_source['current_version'], author='human',
            change_summary='Edited while revision ran')
        with self.assertRaisesRegex(ProjectStoreError, 'stale'):
            apply_generation_item(
                self.store, self.project['id'], stale['id'], 'document', 0)

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

    def test_source_reference_rejects_a_stale_displayed_fingerprint(self):
        import drafts_api
        pack = self.root / 'source-pack'
        (pack / 'applications').mkdir(parents=True)
        (pack / 'research').mkdir()
        (pack / 'applications' / 'sample.md').write_text('# Sample\n\nFixed body\n')
        with self.assertRaisesRegex(drafts_api.SourceRevisionConflict, 'source changed'):
            drafts_api.collect_atlas_reference(self.project['id'], {
                'kind': 'application', 'slug': 'sample',
                'expected_fingerprint': '0' * 64,
            }, self.store, pack)
        saved = drafts_api.collect_atlas_reference(self.project['id'], {
            'kind': 'application', 'slug': 'sample',
            'expected_fingerprint': drafts_api._read_complete_source(
                'sample', 'application', None, pack)['fingerprint'],
        }, self.store, pack)
        self.assertEqual(saved['source_ref'], 'sample')

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

    def test_late_execution_update_does_not_overwrite_latest_task_status(self):
        task = self.store.create_task(
            self.project['id'], 'Concurrent executions', 'Keep latest state',
            kind='analysis')
        first = self.store.create_execution(task['id'], 'opencode', 'ses_first')
        self.store.update_execution(first['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {},
        })
        second = self.store.create_execution(task['id'], 'opencode', 'ses_second')
        self.store.update_execution(first['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {},
        })
        self.assertEqual(self.store.get_task(task['id'])['execution_status'], 'queued')
        self.store.update_execution(second['id'], {
            'state': 'running', 'engine_status': 'busy', 'evidence': {},
        })
        self.assertEqual(self.store.get_task(task['id'])['execution_status'], 'running')
        self.store.update_execution(second['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {},
        })
        self.assertEqual(self.store.get_task(task['id'])['execution_status'], 'completed')

    def test_execution_completion_does_not_imply_acceptance(self):
        task = self.store.create_task(
            self.project['id'], 'Review', 'Inspect the evidence', kind='analysis')
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

    def test_acceptance_records_server_owned_execution_and_input_binding(self):
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'source-v1',
            excerpt='Fixed evidence', read_status='read')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the evidence visible', 'current', 'Relevant',
            ['The evidence remains pinned'], [reference['id']])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        document = self.store.create_document(
            self.project['id'], 'analysis', 'Analysis plan', 'Review the evidence',
            [{'kind': 'reference', 'id': reference['id']}])
        task = self.store.create_task(
            self.project['id'], 'Review evidence', 'Check the fixed record',
            [document['version_id']], [requirement['id']], kind='analysis')
        execution = self.store.create_execution(task['id'], 'opencode', 'ses_binding')
        self.assertEqual(task['requirement_snapshots'][0]['acceptance_conditions'],
                         ['The evidence remains pinned'])
        self.store.update_execution(execution['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {},
        })
        with self.assertRaisesRegex(ProjectStoreError, 'every pinned condition'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Evidence checked'}])
        with self.assertRaisesRegex(ProjectStoreError, 'every pinned condition'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Evidence checked'}],
                [condition_result(requirement, 'failed')])
        accepted = self.store.record_acceptance(
            task['id'], 'passed', [{'kind': 'review', 'summary': 'Evidence checked'}],
            [condition_result(requirement, 'passed')])
        binding = next(item for item in accepted['acceptance_evidence']
                       if item['kind'] == 'acceptance_binding')
        self.assertEqual(binding['execution_id'], execution['id'])
        self.assertEqual(binding['document_version_ids'], [document['version_id']])
        self.assertEqual(binding['requirement_bindings'], [{
            'requirement_id': requirement['id'],
            'revision': requirement['revision'],
            'acceptance_conditions': ['The evidence remains pinned'],
        }])
        self.assertEqual(binding['condition_results'], [condition_result(requirement, 'passed')])
        with self.assertRaisesRegex(ValueError, 'reserved'):
            self.store.record_acceptance(
                task['id'], 'waived', [{
                    'kind': 'acceptance_binding', 'summary': 'forged'
                }])

    def test_acceptance_route_requires_and_persists_condition_results(self):
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the route contract', 'current', 'Required',
            ['The route records each condition'])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        document = self.store.create_document(
            self.project['id'], 'analysis', 'Plan', 'Review the route')
        task = self.store.create_task(
            self.project['id'], 'Review route', 'Check the condition',
            [document['version_id']], [requirement['id']], kind='analysis')
        handler = object.__new__(drafts_api.Handler)
        handler.headers = {
            'Host': 'localhost:5199', 'Content-Type': 'application/json', 'Content-Length': '0',
        }
        handler.path = f'/api/projects/{self.project["id"]}/tasks/{task["id"]}/acceptance'
        handler._body = lambda: {
            'status': 'waived',
            'evidence': [{'kind': 'review', 'summary': 'Explicitly waived'}],
        }
        responses = []
        handler._json = lambda body, code=200: responses.append((body, code)) or (body, code)
        with patch.object(drafts_api, 'get_project_store', return_value=self.store):
            missing, missing_code = handler.do_POST()
        self.assertNotEqual(missing_code, 200)
        self.assertIn('condition', missing['error'])
        handler._body = lambda: {
            'status': 'waived',
            'evidence': [{'kind': 'review', 'summary': 'Explicitly waived'}],
            'condition_results': [condition_result(requirement, 'waived')],
        }
        with patch.object(drafts_api, 'get_project_store', return_value=self.store):
            accepted, accepted_code = handler.do_POST()
        self.assertEqual(accepted_code, 200)
        binding = next(item for item in accepted['acceptance_evidence']
                       if item['kind'] == 'acceptance_binding')
        self.assertEqual(binding['condition_results'], [condition_result(requirement, 'waived')])

    def test_legacy_acceptance_migration_is_dry_run_explicit_and_idempotent(self):
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep the legacy condition', 'current', 'Required',
            ['The legacy condition remains visible'])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        task = self.store.create_task(
            self.project['id'], 'Review legacy', 'Check the old record',
            requirement_ids=[requirement['id']], kind='analysis')
        accepted = self.store.record_acceptance(
            task['id'], 'waived', [{'kind': 'review', 'summary': 'Legacy review'}],
            [condition_result(requirement, 'waived')])
        binding = next(item for item in accepted['acceptance_evidence']
                       if item['kind'] == 'acceptance_binding')
        binding.pop('condition_results')
        with sqlite3.connect(self.store.path) as con:
            con.execute(
                'UPDATE task SET acceptance_evidence_json=? WHERE id=?',
                (json.dumps([{'kind': 'review', 'summary': 'Legacy review'}, binding]),
                 task['id']))
            con.commit()
        report = self.store.legacy_acceptance_migration(self.project['id'])
        self.assertEqual(report['summary']['not_backfilled'], 1)
        record = next(item for item in report['records'] if item['task_id'] == task['id'])
        self.assertEqual(record['missing_conditions'][0]['condition'],
                         'The legacy condition remains visible')
        with self.assertRaisesRegex(ProjectStoreError, 'confirm'):
            self.store.backfill_legacy_acceptance(self.project['id'], 'wrong')
        migrated = self.store.backfill_legacy_acceptance(
            self.project['id'], 'backfill_legacy_acceptance_metadata')
        self.assertEqual(migrated['backfilled_task_ids'], [task['id']])
        migrated_task = self.store.get_task(task['id'])
        migrated_binding = next(item for item in migrated_task['acceptance_evidence']
                                if item['kind'] == 'acceptance_binding')
        self.assertEqual(migrated_binding['condition_results'], [])
        self.assertEqual(migrated_binding['condition_results_status'], 'not_backfilled')
        self.assertEqual(migrated_task['acceptance_status'], 'waived')
        again = self.store.backfill_legacy_acceptance(
            self.project['id'], 'backfill_legacy_acceptance_metadata')
        self.assertEqual(again['backfilled_task_ids'], [])
        self.assertEqual(again['summary']['backfilled'], 1)

    def test_legacy_acceptance_migration_routes_require_confirmation(self):
        import drafts_api
        requirement = self.store.create_requirement(
            self.project['id'], 'Route migration condition', 'current', 'Required',
            ['The old route record remains explicit'])
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        task = self.store.create_task(
            self.project['id'], 'Legacy route task', 'Review old record',
            requirement_ids=[requirement['id']], kind='analysis')
        accepted = self.store.record_acceptance(
            task['id'], 'waived', [{'kind': 'review', 'summary': 'Legacy route review'}],
            [condition_result(requirement, 'waived')])
        evidence = accepted['acceptance_evidence']
        binding = next(item for item in evidence if item['kind'] == 'acceptance_binding')
        binding.pop('condition_results')
        with sqlite3.connect(self.store.path) as con:
            con.execute('UPDATE task SET acceptance_evidence_json=? WHERE id=?',
                        (json.dumps(evidence), task['id']))
            con.commit()
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'get_project_store', return_value=self.store):
            handler.path = f'/api/projects/{self.project["id"]}/acceptance-migration'
            report, code = handler.do_GET()
            self.assertEqual(code, 200)
            self.assertEqual(report['summary']['not_backfilled'], 1)
            handler.path = (
                f'/api/projects/{self.project["id"]}/acceptance-migration/backfill')
            handler._body = lambda: {'confirm': 'wrong'}
            rejected, code = handler.do_POST()
            self.assertEqual(code, 400)
            self.assertIn('confirmation', rejected['error'])
            handler._body = lambda: {'confirm': 'backfill_legacy_acceptance_metadata'}
            migrated, code = handler.do_POST()
            self.assertEqual(code, 200)
            self.assertEqual(migrated['backfilled_task_ids'], [task['id']])

    def test_passed_acceptance_requires_a_completed_and_applied_execution(self):
        task = self.store.create_task(
            self.project['id'], 'Implement', 'Do work', kind='code')
        with self.assertRaisesRegex(ProjectStoreError, 'requires a completed execution'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_apply', application_status='pending')
        self.store.update_execution(execution['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {}})
        with self.assertRaisesRegex(ProjectStoreError, 'apply the isolated execution result'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        self.store.record_execution_application(execution['id'], 'applied', {})
        with self.assertRaisesRegex(ProjectStoreError, 'accepted workspace baseline'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        workspace = Path(self.project['workspace'])
        workspace.mkdir(parents=True, exist_ok=True)
        baseline = capture_project_baseline(self.store, self.project['id'], [])
        newer = capture_project_baseline(
            self.store, self.project['id'], [],
            expected_baseline_id=baseline['id'],
            expected_content_fingerprint=baseline['content_fingerprint'])
        self.store.record_execution_application(execution['id'], 'applied', {
            'accepted_baseline_id': baseline['id'],
        })
        with self.assertRaisesRegex(ProjectStoreError, 'accepted workspace baseline'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        self.store.record_execution_application(execution['id'], 'applied', {
            'accepted_baseline_id': newer['id'],
        })
        (workspace / 'unreviewed.txt').write_text('changed after baseline\n')
        with self.assertRaisesRegex(ProjectStoreError, 'changed after the accepted baseline'):
            self.store.record_acceptance(
                task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        (workspace / 'unreviewed.txt').unlink()
        accepted = self.store.record_acceptance(
            task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}])
        self.assertEqual(accepted['acceptance_status'], 'passed')

    def test_acceptance_focus_paths_do_not_replace_default_snapshot_ignores(self):
        workspace = Path(self.project['workspace'])
        (workspace / 'src').mkdir(parents=True, exist_ok=True)
        (workspace / 'src' / 'app.py').write_text('print("ok")\\n')
        baseline = capture_project_baseline(self.store, self.project['id'], ['src'])
        task = self.store.create_task(
            self.project['id'], 'Focused implementation', 'Use the focused path',
            kind='code')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_focus', application_status='pending')
        self.store.update_execution(execution['id'], {
            'state': 'completed', 'engine_status': 'idle', 'evidence': {},
        })
        self.store.record_execution_application(execution['id'], 'applied', {
            'accepted_baseline_id': baseline['id'],
        })
        accepted = self.store.record_acceptance(
            task['id'], 'passed', [{'kind': 'review', 'summary': 'Focused baseline verified'}])
        self.assertEqual(accepted['acceptance_status'], 'passed')

    def test_document_review_and_requirement_confirmation_use_revision_cas(self):
        document = self.store.create_document(
            self.project['id'], 'analysis', 'Plan', 'v1')
        updated = self.store.add_document_version(document['id'], 'v2')
        with self.assertRaisesRegex(ProjectStoreError, 'version conflict'):
            self.store.review_document(
                self.project['id'], document['id'], 'approved', expected_current_version=1)
        self.store.review_document(
            self.project['id'], document['id'], 'approved',
            expected_current_version=updated['current_version'])

        requirement = self.store.create_requirement(self.project['id'], 'Keep evidence')
        changed = self.store.update_requirement(
            self.project['id'], requirement['id'], content='Keep revised evidence')
        with self.assertRaisesRegex(ProjectStoreError, 'revision conflict'):
            self.store.confirm_requirement(
                requirement['id'], 'current', 'stale', expected_revision=1)
        self.store.confirm_requirement(
            requirement['id'], 'current', 'current',
            expected_revision=changed['revision'])

    def test_execution_evidence_and_export_redact_known_secrets(self):
        task = self.store.create_task(
            self.project['id'], 'Inspect', 'Inspect the evidence', kind='analysis')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_redact',
            input_state={'api_key': 'input-secret'},
            capabilities={'nested': {'token': 'capability-secret'}})
        updated = self.store.update_execution(execution['id'], {
            'state': 'running',
            'engine_status': 'busy',
            'evidence': {
                'assistant_text': (
                    'Authorization: Bearer output-secret\n'
                    'ATLAS_RESULT: {"requirements": []}'),
                'tool_calls': {'commands': [{
                    'command': 'curl https://user:password@example.com/private'}]},
            },
        })
        self.assertEqual(updated['input_state']['api_key'], '[REDACTED]')
        self.assertEqual(
            updated['capabilities']['nested']['token'], '[REDACTED]')
        self.assertIn('ATLAS_RESULT', updated['raw_state']['evidence']['assistant_text'])
        persisted = json.dumps(updated, ensure_ascii=False)
        for secret in ('input-secret', 'capability-secret', 'output-secret', 'password'):
            self.assertNotIn(secret, persisted)

        with sqlite3.connect(self.store.path) as con:
            con.execute(
                'UPDATE execution SET raw_state_json=?,input_state_json=? WHERE id=?',
                (json.dumps({
                    'state': 'running',
                    'evidence': {'assistant_text': 'Bearer legacy-export-secret'},
                }), json.dumps({'token': 'legacy-input-secret'}), execution['id']))
            con.commit()
        exported = export_project(self.store, self.project['id'])
        archive = Path(exported['archive'])
        self.assertEqual(archive.stat().st_mode & 0o777, 0o600)
        self.assertEqual(archive.parent.stat().st_mode & 0o777, 0o700)
        self.assertTrue(exported['manifest']['privacy']['known_secret_redaction'])
        with zipfile.ZipFile(archive) as bundle:
            combined = b'\n'.join(bundle.read(name) for name in bundle.namelist())
            execution_records = bundle.read('execution-records.json')
            handoff = bundle.read(f'handoffs/{task["id"]}.json')
        self.assertNotIn(b'legacy-export-secret', combined)
        self.assertNotIn(b'legacy-input-secret', combined)
        self.assertIn(b'[REDACTED]', execution_records)
        self.assertIn(b'[REDACTED]', handoff)
        self.assertEqual(
            (Path(exported['directory']) / 'manifest.json').stat().st_mode & 0o777, 0o600)

        sanitized = self.store.redact_persisted_evidence()
        self.assertEqual(sanitized['executions'], 1)
        with sqlite3.connect(self.store.path) as con:
            database_text = '\n'.join(
                row[0] for row in con.execute(
                    'SELECT raw_state_json FROM execution UNION ALL '
                    'SELECT input_state_json FROM execution'))
        self.assertNotIn('legacy-export-secret', database_text)
        self.assertNotIn('legacy-input-secret', database_text)

    def test_waived_acceptance_requires_an_explicit_reason(self):
        task = self.store.create_task(self.project['id'], 'Implement', 'Do work')
        with self.assertRaisesRegex(ValueError, 'evidence is required'):
            self.store.record_acceptance(task['id'], 'waived', [])
        waived = self.store.record_acceptance(
            task['id'], 'waived', [{'kind': 'review', 'summary': 'Out of scope for this round'}])
        self.assertEqual(waived['acceptance_status'], 'waived')

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
        self.store.record_acceptance(
            task['id'], 'waived',
            [{'kind': 'review', 'summary': 'Explicitly waived for this unit test'}])
        completed = self.store.update_iteration_status(iteration['id'], 'completed')
        self.assertEqual(completed['status'], 'completed')
        self.assertIsNotNone(completed['completed_at'])

    def test_failed_transaction_does_not_leave_partial_task(self):
        with self.assertRaises(ProjectStoreError):
            self.store.create_task(self.project['id'], 'Implement', 'Do work', ['dver_missing'])
        with sqlite3.connect(self.store.path) as con:
            self.assertEqual(con.execute('SELECT count(*) FROM task').fetchone()[0], 0)

    def test_generation_accepts_result_written_in_persistent_engine_directory(self):
        from project_generation import _run_opencode
        source_root = self.root / 'fallback-source-root'
        source_root.mkdir()
        (source_root / 'existing.txt').write_text('keep')
        directory = self.root / 'generation-fallback'
        directory.mkdir()
        (directory / 'input.json').write_text('{}')
        (directory / 'input.md').write_text('fixed input')
        (directory / 'prompt.md').write_text('write result.json')
        engine = directory / 'engine'
        engine.mkdir()
        (engine / 'engine.log').write_text('')
        original_run = subprocess.run
        observed = {}

        def fake_run(command, **kwargs):
            if command[:2] == ['git', 'init']:
                return original_run(command, **kwargs)
            observed['cwd'] = Path(kwargs['cwd'])
            observed['pws'] = kwargs['env'].get('PWD')
            config_path = observed['cwd'] / '.opencode' / 'opencode.json'
            observed['config'] = json.loads(config_path.read_text())
            observed['git_root'] = (observed['cwd'] / '.git').is_dir()
            (engine / 'result.json').write_text('{"input_fingerprint":"fixed"}')
            return SimpleNamespace(returncode=0)

        with patch('project_generation._generation_source_root', return_value=source_root), \
             patch('project_generation.detect_opencode_major_version', return_value=2), \
             patch('project_generation.subprocess.run', side_effect=fake_run):
            result, metadata = _run_opencode(directory, {'id': 'gen_fallback', 'model': ''})
        self.assertEqual(result['input_fingerprint'], 'fixed')
        self.assertIsNone(metadata['engine_session_id'])
        self.assertTrue(observed['git_root'])
        self.assertEqual(observed['pws'], str(observed['cwd']))
        self.assertIn(
            {'action': 'edit', 'resource': 'result.json', 'effect': 'allow'},
            observed['config']['permissions'])

    def test_generation_keeps_provider_result_in_disposable_runtime(self):
        from project_generation import _run_opencode
        source_root = self.root / 'source-root'
        source_root.mkdir()
        (source_root / 'existing.txt').write_text('keep')
        directory = self.root / 'generation-runtime-result'
        directory.mkdir()
        (directory / 'input.json').write_text('{}')
        (directory / 'input.md').write_text('fixed input')
        (directory / 'prompt.md').write_text('write result.json')
        original_run = subprocess.run

        def fake_run(command, **kwargs):
            if command[:2] == ['git', 'init']:
                return original_run(command, **kwargs)
            (Path(kwargs['cwd']) / 'result.json').write_text(
                '{"input_fingerprint":"fixed"}')
            return SimpleNamespace(returncode=0)

        with patch('project_generation._generation_source_root', return_value=source_root), \
             patch('project_generation.detect_opencode_major_version', return_value=2), \
             patch('project_generation.subprocess.run', side_effect=fake_run):
            result, metadata = _run_opencode(
                directory, {'id': 'gen_runtime_result', 'model': ''})
        self.assertEqual(result['input_fingerprint'], 'fixed')
        self.assertEqual(metadata['artifact_root'], 'runtime')
        self.assertTrue((directory / 'engine' / 'result.json').is_file())
        self.assertFalse((source_root / 'result.json').exists())

    def test_generation_rejects_provider_artifact_outside_runtime(self):
        from project_generation import _run_opencode
        source_root = self.root / 'source-root'
        source_root.mkdir()
        (source_root / 'existing.txt').write_text('keep')
        directory = self.root / 'generation-violation'
        directory.mkdir()
        (directory / 'input.json').write_text('{}')
        (directory / 'input.md').write_text('fixed input')
        (directory / 'prompt.md').write_text('write result.json')
        original_run = subprocess.run

        def fake_run(command, **kwargs):
            if command[:2] == ['git', 'init']:
                return original_run(command, **kwargs)
            (source_root / 'result.json').write_text('{"input_fingerprint":"fixed"}')
            return SimpleNamespace(returncode=0)

        with patch('project_generation._generation_source_root', return_value=source_root), \
             patch('project_generation.detect_opencode_major_version', return_value=2), \
             patch('project_generation.subprocess.run', side_effect=fake_run):
            with self.assertRaisesRegex(RuntimeError, 'outside the controlled'):
                _run_opencode(directory, {'id': 'gen_violation', 'model': ''})
        report = json.loads(
            (directory / 'provider-artifact-violation.json').read_text())
        self.assertIn('result.json', report['added'])
        self.assertTrue((source_root / 'result.json').exists())
        self.assertFalse((directory / 'engine' / 'result.json').exists())

    def test_generation_recovers_only_matching_complete_json_text(self):
        from project_generation import _generation_result_from_log
        result = {
            'input_fingerprint': 'fixed', 'questions': [], 'requirements': [],
            'conflicts': [], 'suggestions': [], 'documents': [],
        }
        event = {'type': 'text', 'part': {'text': 'prefix\n```json\n' + json.dumps(result) + '\n```'}}
        raw = (json.dumps(event) + '\n').encode()
        self.assertEqual(_generation_result_from_log(raw, 'fixed'), result)
        self.assertIsNone(_generation_result_from_log(raw, 'other'))
        self.assertIsNone(_generation_result_from_log(
            (json.dumps({'type': 'text', 'text': '{"input_fingerprint":"fixed"}'}) + '\n').encode(),
            'fixed'))

    def test_generation_engine_log_is_redacted_and_bounded(self):
        from project_generation import _persist_engine_log
        path = self.root / 'engine.log'
        _persist_engine_log(path, (
            b'Authorization: Bearer generation-secret\n' +
            b'x' * 1_100_000))
        value = path.read_text(encoding='utf-8')
        self.assertNotIn('generation-secret', value)
        self.assertIn('[REDACTED]', value)
        self.assertIn('Atlas truncated', value)
        self.assertLessEqual(len(value), 1_000_000)
        self.assertEqual(path.stat().st_mode & 0o777, 0o600)

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
        (self.root / 'existing').mkdir()
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
        self.assertTrue(Path(idea['workspace']).is_dir())

        handler._body = lambda: {
            'name': 'Missing project', 'objective': 'Inspect it', 'mode': 'existing',
            'workspace': str(self.root / 'does-not-exist'),
        }
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            invalid_workspace, code = handler.do_POST()
        self.assertEqual(code, 400)
        self.assertIn('existing directory', invalid_workspace['error'])

    def test_execution_get_is_read_only_and_reconcile_is_explicit_post(self):
        import drafts_api
        task = self.store.create_task(
            self.project['id'], 'Inspect', 'Inspect the evidence', kind='analysis')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_read_only')
        handler = object.__new__(drafts_api.Handler)
        handler.headers = {
            'Host': 'localhost:5173',
            'Origin': 'http://localhost:5173',
            'Content-Type': 'application/json',
            'Content-Length': '2',
        }
        handler._json = lambda value, code=200: (value, code)
        base = (f'/api/projects/{self.project["id"]}/executions/'
                f'{execution["id"]}')
        handler.path = base
        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
             patch.object(drafts_api, 'reconcile_execution') as reconcile:
            payload, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertEqual(payload['id'], execution['id'])
        reconcile.assert_not_called()

        handler.path = base + '/reconcile'
        handler._body = lambda: {}
        expected = {'id': execution['id'], 'status': 'completed'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
             patch.object(drafts_api, 'reconcile_execution', return_value=expected) as reconcile:
            payload, code = handler.do_POST()
        self.assertEqual(code, 200)
        self.assertEqual(payload, expected)
        reconcile.assert_called_once_with(self.store, self.project['id'], execution['id'])

    def test_project_http_starter_reference_and_confirmed_delete(self):
        import drafts_api
        pack = self.root / 'corpus'
        (pack / 'applications').mkdir(parents=True)
        (pack / 'research').mkdir()
        (pack / 'applications/sample.md').write_text(
            '# Sample type\n\n## Core Model\nFixed type evidence.\n')
        created = drafts_api.create_project({
            'name': 'From a type',
            'objective': 'Build from fixed type evidence',
            'mode': 'new',
            'starter_reference': {
                'kind': 'application', 'slug': 'sample',
                'note': 'Started from the type page', 'read_status': 'read',
            },
        }, store=self.store, pack=pack)
        references = self.store.list_references(created['id'])
        self.assertEqual(len(references), 1)
        self.assertEqual(references[0]['source_kind'], 'atlas:application')
        self.assertIn('Fixed type evidence', references[0]['excerpt'])

        with patch.object(drafts_api, 'project_generation_list',
                          return_value=[{'id': 'gen_active', 'status': 'running'}]):
            with self.assertRaisesRegex(ProjectStoreError, 'active generation'):
                drafts_api.delete_project(
                    created['id'], {'confirm': created['id']}, store=self.store)

        handler = object.__new__(drafts_api.Handler)
        handler.path = f"/api/projects/{created['id']}"
        handler._json = lambda value, code=200: (value, code)
        handler._body = lambda: {'confirm': 'wrong'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            error, code = handler.do_DELETE()
        self.assertEqual(code, 400)
        self.assertIn('confirm', error['error'])

        workspace = Path(created['workspace'])
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / 'keep.txt').write_text('keep\n')
        artifact_roots = {}
        for name, relative in {
            'generation-runs': 'gen_finished/run.json',
            'execution-workspaces': 'run_test/workspace.txt',
            'execution-evidence': 'exe_test/stderr.txt',
            'exports': 'bundle/export.zip',
        }.items():
            artifact = self.store.path.parent / name / created['id'] / relative
            artifact.parent.mkdir(parents=True)
            artifact.write_text(
                json.dumps({'id': 'gen_finished', 'project_id': created['id'],
                            'status': 'completed', 'created_at': '2026-09-24T00:00:00Z'})
                if name == 'generation-runs' else 'artifact')
            artifact_roots[name] = artifact
        custom_run = (self.root / 'custom-executions' / created['id'] /
                      'run_test')
        custom_run.mkdir(parents=True)
        (custom_run / 'workspace.txt').write_text('isolated')
        custom_task = self.store.create_task(
            created['id'], 'Cleanup', 'Exercise custom cleanup')
        custom_execution = self.store.create_execution(
            custom_task['id'], 'opencode', 'ses_cleanup', workdir=str(custom_run))
        self.store.update_execution(custom_execution['id'], {
            'state': 'stopped', 'engine_status': 'idle', 'evidence': {}})
        handler._body = lambda: {'confirm': created['id']}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            deleted, code = handler.do_DELETE()
        self.assertEqual(code, 200)
        self.assertTrue(deleted['workspace_preserved'])
        self.assertEqual((workspace / 'keep.txt').read_text(), 'keep\n')
        self.assertTrue(set(artifact_roots).issubset(deleted['artifacts_removed']))
        self.assertIn('execution-workspaces:custom', deleted['artifacts_removed'])
        self.assertEqual(deleted['artifact_cleanup_errors'], {})
        self.assertFalse(custom_run.parent.exists())
        for artifact in artifact_roots.values():
            self.assertFalse(artifact.exists())
        with self.assertRaisesRegex(ProjectStoreError, 'project not found'):
            self.store.get_project(created['id'])

        workspaces_before = set((self.store.path.parent / 'workspaces').iterdir())
        with self.assertRaises(FileNotFoundError):
            drafts_api.create_project({
                'name': 'Missing starter', 'objective': 'Must roll back', 'mode': 'new',
                'starter_reference': {'kind': 'application', 'slug': 'missing'},
            }, store=self.store, pack=pack)
        self.assertNotIn('Missing starter', [item['name'] for item in self.store.list_projects()])
        self.assertEqual(
            set((self.store.path.parent / 'workspaces').iterdir()), workspaces_before)

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
        handler._body = lambda: {
            'scope': 'current', 'reason': 'Approved for the pilot', 'expected_revision': 1,
        }
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

        def reply_permission(self, request_id, reply, message=None, session_id=None):
            self.permission_replies.append((request_id, reply, message))
            self.mode = 'running'
            return True

    def test_fixed_verification_excludes_unplanned_commands(self):
        messages = [{
            'info': {'role': 'assistant', 'parentID': 'msg_task'},
            'parts': [
                {'type': 'tool', 'tool': 'bash', 'state': {
                    'input': {'command': 'python3 -m unittest -v'},
                    'status': 'completed', 'metadata': {'exit': 0}}},
                {'type': 'tool', 'tool': 'bash', 'state': {
                    'input': {'command': 'ls -la'},
                    'status': 'completed', 'metadata': {'exit': 0}}},
                {'type': 'tool', 'tool': 'bash', 'state': {
                    'input': {'command': 'optional-probe'},
                    'status': 'completed', 'metadata': {'exit': 1}}},
            ],
        }]

        evidence = _execution_evidence(
            messages, 'msg_task', ['python3 -m unittest -v'])

        self.assertEqual(evidence['verification']['successful_commands'],
                         ['python3 -m unittest -v'])
        self.assertEqual(evidence['verification']['missing_or_failed_commands'], [])
        self.assertTrue(evidence['verification']['all_planned_passed'])
        self.assertEqual(
            [item['planned'] for item in evidence['tool_calls']['commands']],
            [True, False, False])

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
        self.store.review_document(
            self.project['id'], self.document['id'], 'approved', 'Pilot plan reviewed')
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

    def test_iteration_requires_core_inputs_and_workspace_baseline(self):
        with self.assertRaisesRegex(ProjectStoreError, 'document version'):
            create_execution_iteration(self.store, self.project['id'], {
                'title': 'Missing document', 'objective': 'Must stay blocked',
                'input_document_versions': [],
                'requirement_ids': [self.requirement['id']],
            })
        with self.assertRaisesRegex(ProjectStoreError, 'confirmed current requirement'):
            create_execution_iteration(self.store, self.project['id'], {
                'title': 'Missing requirement', 'objective': 'Must stay blocked',
                'input_document_versions': [self.document['version_id']],
                'requirement_ids': [],
            })

        pending_document = self.store.create_document(
            self.project['id'], 'development-plan', 'Unapproved plan', 'Draft plan')
        with self.assertRaisesRegex(ProjectStoreError, 'approve every fixed document'):
            create_execution_iteration(self.store, self.project['id'], {
                'title': 'Unapproved document', 'objective': 'Must stay blocked',
                'input_document_versions': [pending_document['version_id']],
                'requirement_ids': [self.requirement['id']],
            })
        self.store.review_document(
            self.project['id'], pending_document['id'], 'rejected', 'Needs rework')
        rejected = self.store.get_document(pending_document['id'])
        self.assertEqual(rejected['review']['approval'], 'rejected')
        with self.assertRaisesRegex(ProjectStoreError, 'approve every fixed document'):
            create_execution_iteration(self.store, self.project['id'], {
                'title': 'Rejected document', 'objective': 'Must stay blocked',
                'input_document_versions': [pending_document['version_id']],
                'requirement_ids': [self.requirement['id']],
            })
        self.store.review_document(
            self.project['id'], pending_document['id'], 'approved', 'Rework accepted')
        self.store.add_document_version(
            pending_document['id'], 'Draft plan v2', change_summary='Edited')
        reset = self.store.get_document(pending_document['id'])
        self.assertEqual(reset['review']['approval'], 'pending')

        no_baseline = self.store.create_project(
            'No baseline', 'Require workspace review', self.root / 'no-baseline', 'new')
        requirement = self.store.create_requirement(
            no_baseline['id'], 'Keep scope explicit', 'current', 'Required')
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        document = self.store.create_document(
            no_baseline['id'], 'development-plan', 'Plan', 'Approved plan')
        with self.assertRaisesRegex(ProjectStoreError, 'workspace baseline'):
            create_execution_iteration(self.store, no_baseline['id'], {
                'title': 'Missing baseline', 'objective': 'Must stay blocked',
                'input_document_versions': [document['version_id']],
                'requirement_ids': [requirement['id']],
            })

    def test_api_tasks_require_fixed_document_and_requirement_inputs(self):
        with self.assertRaisesRegex(ProjectStoreError, 'fixed document version'):
            create_execution_task(self.store, self.project['id'], {
                'iteration_id': self.iteration['id'], 'kind': 'analysis',
                'title': 'Missing document', 'objective': 'Must stay blocked',
                'input_document_versions': [],
                'requirement_ids': [self.requirement['id']],
            })
        with self.assertRaisesRegex(ProjectStoreError, 'fixed requirement'):
            create_execution_task(self.store, self.project['id'], {
                'iteration_id': self.iteration['id'], 'kind': 'analysis',
                'title': 'Missing requirement', 'objective': 'Must stay blocked',
                'input_document_versions': [self.document['version_id']],
                'requirement_ids': [],
            })

    def test_failed_product_acceptance_can_start_a_new_execution(self):
        failed = self.store.record_acceptance(
            self.task['id'], 'failed',
            [{'kind': 'review', 'summary': 'The visible behavior is still incorrect'}],
            [condition_result(self.requirement, 'failed')])
        self.assertEqual(failed['acceptance_status'], 'failed')
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.assertEqual(execution['status'], 'running')

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
        self.assertFalse(self.client.tools['bash'])
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
        self.assertEqual(completed['raw_state']['evidence']['verification_source'], 'atlas_fixed')
        self.assertIn('agent_reported_verification', completed['raw_state']['evidence'])
        self.assertEqual(completed['raw_state']['evidence']['run_summary']['status'], 'completed')
        self.assertIsNone(completed['raw_state']['evidence']['run_summary']['exitCode'])
        completion = completed['raw_state']['evidence']['completion_report']
        self.assertTrue(completion['valid'])
        self.assertEqual(completion['requirements'][0]['status'], 'satisfied')
        self.assertEqual(completed['raw_state']['evidence']['tool_calls']['commands'][0]['exit'], 0)
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 1\n')
        with self.assertRaisesRegex(ProjectStoreError, 'isolated execution result'):
            self.store.record_acceptance(
                self.task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}],
                [condition_result(self.requirement, 'passed')])
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

    def test_cli_run_evidence_is_persisted_outside_workspace_and_indexed(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        result = record_cli_run_evidence(self.store, self.project['id'], execution['id'], {
            'argv': ['opencode', 'run', '--format', 'json'],
            'exitCode': 0,
            'timedOut': False,
            'stdout': '{"type":"run.finished"}\n',
            'stderr': '',
        })
        evidence = result['raw_state']['evidence']['cli_run']
        self.assertEqual(evidence['summary']['status'], 'completed')
        self.assertTrue(Path(evidence['directory']).is_dir())
        self.assertTrue((Path(evidence['directory']) / 'run.json').exists())
        self.assertNotIn(str(self.workspace), evidence['directory'])

    def test_cli_failure_and_timeout_evidence_remain_distinguishable(self):
        for exit_code, timed_out, expected in ((2, False, 'failed'), (124, True, 'timed_out')):
            execution = start_execution(
                self.store, self.project['id'], self.task['id'], {}, self.client)
            result = record_cli_run_evidence(self.store, self.project['id'], execution['id'], {
                'argv': ['opencode', 'run', '--format', 'json'],
                'exitCode': exit_code,
                'timedOut': timed_out,
                'stdout': '',
                'stderr': 'provider failure' if not timed_out else 'command timed out',
            })
            result = self.store.update_execution(execution['id'], {
                'state': 'failed',
                'engine_status': 'cli_test',
                'evidence': result['raw_state']['evidence'],
            }, execution.get('engine_message_id'))
            summary = result['raw_state']['evidence']['cli_run']['summary']
            self.assertEqual(summary['status'], expected)
            self.assertNotEqual(summary['status'], 'completed')

    def test_verification_registry_rejects_inline_absolute_and_unknown_commands(self):
        from execution_service import _verification_argv
        root = Path(self.temp.name) / 'verify-root'
        root.mkdir()
        for command, message in (
                ('python3 -c "print(1)"', 'inline interpreter'),
                ('python3 /tmp/read_secret.py', 'absolute paths'),
                ('curl https://example.com', 'not registered'),
                ('/bin/sh -c true', 'not allowed'),
                ('node -e "process.exit(0)"', 'inline Node'),
                ('python3 -m pip install left-pad', 'registered Python')):
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, message):
                _verification_argv(command, root)
        argv = _verification_argv('python3 -m unittest discover -s tests -v', root)
        self.assertTrue(Path(argv[0]).is_absolute())
        self.assertEqual(argv[1:], ['-m', 'unittest', 'discover', '-s', 'tests', '-v'])

        with self.assertRaisesRegex(ValueError, 'inline interpreter'):
            create_execution_task(self.store, self.project['id'], {
                'iteration_id': self.iteration['id'], 'kind': 'analysis',
                'title': 'Rejected verifier', 'objective': 'Do not run inline code',
                'input_document_versions': [self.document['version_id']],
                'requirement_ids': [self.requirement['id']],
                'verification_commands': ['python3 -c "print(1)"'],
            })

    def test_task_timeout_overrides_project_timeout_for_verification(self):
        task = self.store.create_task(
            self.project['id'], 'Bounded check', 'Run a bounded verification',
            iteration_id=self.iteration['id'],
            input_document_versions=[self.document['version_id']],
            requirement_ids=[self.requirement['id']],
            kind='analysis', verification_commands=['sleep 31'], timeout_seconds=30)
        self.assertEqual(task['timeout_seconds'], 30)
        self.assertEqual(task['timeout_seconds'], 30)
        # A short real command keeps the regression test fast while exercising
        # the same timed_out mapping used by the CLI execution path.
        evidence = run_cli_verification(self.workspace, ['sleep 2'], timeout_seconds=1)
        command = evidence['tool_calls']['commands'][0]
        self.assertEqual(command['status'], 'timed_out')
        self.assertTrue(command['timedOut'])
        self.assertFalse(evidence['verification']['all_planned_passed'])

    def test_cleanup_requires_terminal_execution_and_preserves_evidence(self):
        running = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        with self.assertRaisesRegex(ProjectStoreError, 'finished execution'):
            cleanup_execution_workspace(self.store, self.project['id'], running['id'])

        self.client.mode = 'completed'
        completed = reconcile_execution(
            self.store, self.project['id'], running['id'], self.client)
        workdir = Path(completed['workdir'])
        record_cli_run_evidence(self.store, self.project['id'], completed['id'], {
            'argv': ['opencode', 'run'], 'exitCode': 0, 'timedOut': False,
            'stdout': '{"type":"run.finished"}\n', 'stderr': '',
        })
        apply_execution_result(self.store, self.project['id'], completed['id'])
        completed = self.store.get_execution(completed['id'])
        evidence_dir = self.store.path.parent / 'execution-evidence' / self.project['id'] / completed['id']
        self.assertTrue(workdir.exists())
        cleaned = cleanup_execution_workspace(
            self.store, self.project['id'], completed['id'])
        self.assertFalse(workdir.exists())
        self.assertTrue((evidence_dir / 'run.json').exists())
        self.assertEqual(cleaned['raw_state']['evidence']['cleanup']['status'], 'cleaned')
        self.assertTrue(cleaned['raw_state']['evidence']['cleanup']['evidence_preserved'])

    def test_stopped_http_cleanup_materializes_evidence(self):
        class AbortClient(self.Client):
            def abort(self, _session_id):
                return True

        client = AbortClient()
        running = start_execution(
            self.store, self.project['id'], self.task['id'], {}, client)
        stopped = stop_execution(
            self.store, self.project['id'], running['id'], client)
        self.assertEqual(stopped['status'], 'stopped')
        evidence_dir = self.store.path.parent / 'execution-evidence' / self.project['id'] / stopped['id']
        cleaned = cleanup_execution_workspace(
            self.store, self.project['id'], stopped['id'])
        self.assertTrue((evidence_dir / 'atlas.json').exists())
        self.assertEqual(evidence_dir.stat().st_mode & 0o777, 0o700)
        self.assertEqual((evidence_dir / 'atlas.json').stat().st_mode & 0o777, 0o600)
        self.assertTrue(cleaned['raw_state']['evidence']['cleanup']['evidence_preserved'])
        self.assertEqual(
            cleaned['raw_state']['evidence']['run_summary']['status'], 'cancelled')

    def test_cli_transport_runs_in_isolation_and_records_terminal_evidence(self):
        cli_task = create_execution_task(self.store, self.project['id'], {
            'iteration_id': self.iteration['id'], 'kind': 'code',
            'title': 'CLI transport task', 'objective': 'Run the CLI transport path.',
            'input_document_versions': [self.document['version_id']],
            'requirement_ids': [self.requirement['id']], 'write_paths': ['src'],
            'verification_commands': ['python3 -m unittest'],
        })
        config_dir = self.workspace / '.atlas'
        config_dir.mkdir()
        (config_dir / 'harness.json').write_text(json.dumps({
            'backend': {'openCode': {
                'minimumCompatibleVersion': '1.18.31',
                'installSource': {'binaryPath': sys.executable},
            }},
            'provider': {'results': [{'name': 'OpenAI'}]},
        }))
        checked = check_project_changes(self.store, self.project['id'])
        adopted = capture_project_baseline(
            self.store, self.project['id'], ['src'], self.baseline['id'],
            checked['current']['content_fingerprint'])
        self.store.rebase_iteration(
            self.project['id'], self.iteration['id'], adopted['id'], 'CLI transport test')

        from opencode_cli_adapter import CliResult
        def runner(argv, cwd, timeout):
            return CliResult(tuple(argv), 0, '{"type":"run.finished"}\n', '')

        with patch('execution_service.opencode_preflight', return_value={'status': 'passed'}):
            execution = start_cli_execution(
                self.store, self.project['id'], cli_task['id'],
                {'model': 'openai/gpt', 'transport': 'cli'}, runner=runner)
        self.assertEqual(execution['engine'], 'opencode-cli')
        self.assertEqual(execution['status'], 'completed')
        self.assertEqual(execution['raw_state']['evidence']['cli_run']['summary']['status'], 'completed')
        self.assertEqual(execution['raw_state']['evidence']['run_summary']['exitCode'], 0)
        self.assertTrue(execution['raw_state']['evidence']['verification']['all_planned_passed'])
        self.assertEqual(execution['raw_state']['evidence']['tool_calls']['commands'][0]['exit'], 0)
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 1\n')

    def test_cli_verification_maps_steps_and_timeout(self):
        result = run_cli_verification(
            self.workspace,
            ['python3 -m unittest', 'sleep 2'],
            timeout_seconds=1)
        commands = result['tool_calls']['commands']
        self.assertEqual(commands[0]['status'], 'completed')
        self.assertEqual(commands[0]['exit'], 0)
        self.assertEqual(commands[1]['status'], 'timed_out')
        self.assertTrue(commands[1]['timedOut'])
        self.assertFalse(result['verification']['all_planned_passed'])

    def test_fixed_verifier_rejects_modified_protected_tests(self):
        from execution_service import _verification_protection
        tests = self.workspace / 'tests'
        tests.mkdir()
        test_file = tests / 'test_sample.py'
        test_file.write_text('def test_sample():\n    assert True\n')
        before = snapshot_workspace(self.workspace)
        protected = _verification_protection(before, ['python3 -m unittest'])
        test_file.write_text('def test_sample():\n    assert False\n')
        result = run_cli_verification(
            self.workspace, ['python3 -m unittest'], protected_files=protected)
        self.assertFalse(result['verification']['all_planned_passed'])
        self.assertIn('verification inputs changed', result['verification']['error'])
        self.assertEqual(result['tool_calls']['commands'], [])

    def test_verification_rejects_shell_chaining_and_scrubs_environment(self):
        marker = self.workspace / 'shell-injection'
        probe = self.workspace / 'verify_env.py'
        probe.write_text(
            'import os\n'
            'assert not os.environ.get("OPENAI_API_KEY")\n'
            'assert not os.environ.get("ANTHROPIC_API_KEY")\n')
        commands = [
            (f'python3 -c "import pathlib; pathlib.Path(\'shell-injection\').write_text(\'bad\')" '
             f'&& touch {marker.name}'),
            '/bin/sh -c "touch shell-injection"',
            'python3 verify_env.py',
        ]
        with patch.dict(os.environ, {
                'OPENAI_API_KEY': 'must-not-reach-verification',
                'ANTHROPIC_API_KEY': 'must-not-reach-verification',
        }, clear=False):
            result = run_cli_verification(self.workspace, commands, timeout_seconds=5)
        records = result['tool_calls']['commands']
        self.assertEqual(records[0]['status'], 'failed')
        self.assertIn('shell operators', records[0]['output'])
        self.assertEqual(records[1]['status'], 'failed')
        self.assertIn('not allowed', records[1]['output'])
        self.assertEqual(records[2]['status'], 'completed')
        self.assertFalse(marker.exists())
        self.assertFalse(result['verification']['all_planned_passed'])

    def test_reconcile_keeps_permission_as_first_class_interaction(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'permission'
        waiting = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        self.assertEqual(waiting['status'], 'waiting_permission')
        self.assertEqual(waiting['raw_state']['interaction']['request']['id'],
                         'per_execution')

    def test_permission_replies_cannot_create_persistent_grants(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.client.mode = 'permission'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        with self.assertRaisesRegex(ProjectStoreError, 'persistent permission grants'):
            reply_permission(
                self.store, self.project['id'], execution['id'],
                {'request_id': 'per_execution', 'reply': 'always'}, self.client)
        with self.assertRaisesRegex(ProjectStoreError, 'outside the Atlas U17 policy'):
            reply_permission(
                self.store, self.project['id'], execution['id'],
                {'request_id': 'per_execution', 'reply': 'once'}, self.client)
        self.assertEqual(self.client.permission_replies, [])

    def test_permission_reply_rejects_resource_outside_task_write_paths(self):
        class ResourceClient(self.Client):
            def reconcile(self, session_id):
                result = super().reconcile(session_id)
                result['pending_permissions'] = [{
                    'id': 'per_resource', 'permission': 'edit',
                    'resource': 'tests/agent_test.py',
                    'tool': {'messageID': 'msg_answer'},
                }]
                return result

        client = ResourceClient()
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, client)
        client.mode = 'permission'
        execution = reconcile_execution(
            self.store, self.project['id'], execution['id'], client)
        with self.assertRaisesRegex(ProjectStoreError, 'outside the task write_paths'):
            reply_permission(
                self.store, self.project['id'], execution['id'],
                {'request_id': 'per_resource', 'reply': 'once'}, client)
        self.assertEqual(client.permission_replies, [])

    def test_cleanup_does_not_remove_a_workdir_reused_by_follow_up(self):
        first = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(first['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        first = reconcile_execution(
            self.store, self.project['id'], first['id'], self.client)
        second = continue_execution(
            self.store, self.project['id'], first['id'],
            {'instruction': 'Review the change again.'}, self.client)
        with self.assertRaisesRegex(ProjectStoreError, 'still referenced'):
            cleanup_execution_workspace(
                self.store, self.project['id'], first['id'])
        self.assertTrue(Path(second['workdir']).exists())

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

    def test_unknown_execution_workspace_can_be_cleaned_after_explicit_review(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)

        class MissingClient:
            def reconcile(self, _session_id):
                raise OpenCodeError(404, 'session unavailable')

        unknown = reconcile_execution(
            self.store, self.project['id'], execution['id'], MissingClient())
        self.assertEqual(unknown['status'], 'unknown')
        workdir = Path(unknown['workdir'])
        self.assertTrue(workdir.exists())
        cleaned = cleanup_execution_workspace(
            self.store, self.project['id'], execution['id'])
        self.assertFalse(workdir.exists())
        self.assertEqual(cleaned['raw_state']['evidence']['cleanup']['status'], 'cleaned')
        self.assertTrue(cleaned['raw_state']['evidence']['cleanup']['evidence_preserved'])

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

    def test_explicit_apply_recovery_restores_a_journaled_backup(self):
        from execution_workspace import (
            _write_apply_journal, restore_interrupted_apply,
        )
        source = self.root / 'journal-source'
        source.mkdir()
        target = source / 'file.txt'
        old = b'old\n'
        new = b'new\n'
        target.write_bytes(old)
        before = {'files': {'file.txt': {
            'kind': 'file', 'size': len(old),
            'sha256': hashlib.sha256(old).hexdigest(),
        }}}
        after = {'files': {'file.txt': {
            'kind': 'file', 'size': len(new),
            'sha256': hashlib.sha256(new).hexdigest(),
        }}}
        stage = source / '.atlas-apply-test'
        (stage / 'backup').mkdir(parents=True)
        (stage / 'backup' / 'file.txt').write_bytes(old)
        target.unlink()
        _write_apply_journal(stage, {
            'schema': 1,
            'execution_id': 'exe_journal',
            'before_manifest': before,
            'after_manifest': after,
            'difference': {'added': [], 'modified': ['file.txt'], 'removed': []},
            'phase': 'backing_up',
            'backed_up': ['file.txt'],
            'applied': [],
        })
        result = restore_interrupted_apply(source, 'exe_journal')
        self.assertEqual(result['status'], 'restored')
        self.assertEqual(target.read_bytes(), old)
        self.assertFalse(stage.exists())

    def test_process_crash_leaves_a_recoverable_apply_journal(self):
        source = self.root / 'crash-source'
        work = self.root / 'crash-work'
        source.mkdir()
        work.mkdir()
        (work / 'file.txt').write_text('new\n')
        old = b'old\n'
        (source / 'file.txt').write_bytes(old)
        before = {'files': {'file.txt': {
            'kind': 'file', 'size': len(old),
            'sha256': hashlib.sha256(old).hexdigest(),
        }}}
        new = b'new\n'
        after = {'files': {'file.txt': {
            'kind': 'file', 'size': len(new),
            'sha256': hashlib.sha256(new).hexdigest(),
        }}}
        script = """
import json, os, sys
sys.path.insert(0, sys.argv[1])
import execution_workspace
real = execution_workspace.os.replace
crashed = False
def crash_after_backup(source, target):
    global crashed
    real(source, target)
    if not crashed and '/backup/' in str(target):
        crashed = True
        os._exit(77)
execution_workspace.os.replace = crash_after_backup
execution_workspace.apply_execution_workspace(
    sys.argv[2], sys.argv[3], json.loads(sys.argv[4]), json.loads(sys.argv[5]),
    {'added': [], 'modified': ['file.txt'], 'removed': []}, 'exe_crash')
"""
        result = subprocess.run([
            sys.executable, '-c', script, str(CODE), str(source), str(work),
            json.dumps(before), json.dumps(after),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(result.returncode, 77)
        self.assertFalse((source / 'file.txt').exists())
        from execution_workspace import read_apply_journal, restore_interrupted_apply
        self.assertIsNotNone(read_apply_journal(source, 'exe_crash'))
        recovered = restore_interrupted_apply(source, 'exe_crash')
        self.assertEqual(recovered['status'], 'restored')
        self.assertEqual((source / 'file.txt').read_bytes(), old)

    def test_result_application_rechecks_each_target_before_replace(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        import execution_workspace
        original = execution_workspace._assert_apply_target
        changed = False

        def edit_before_check(root, relative, expected):
            nonlocal changed
            if not changed and relative == 'src/app.py':
                changed = True
                (root / relative).write_text('VALUE = 9\n')
            return original(root, relative, expected)

        with patch.object(execution_workspace, '_assert_apply_target',
                          side_effect=edit_before_check):
            with self.assertRaisesRegex(ProjectStoreError, 'changed while applying'):
                apply_execution_result(
                    self.store, self.project['id'], execution['id'])
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 9\n')
        self.assertEqual(
            self.store.get_execution(execution['id'])['application_status'], 'conflict')

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

    def test_http_recover_apply_route_requires_explicit_service_call(self):
        import drafts_api
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        handler = object.__new__(drafts_api.Handler)
        handler.path = (f"/api/projects/{self.project['id']}/executions/"
                        f"{execution['id']}/recover-apply")
        handler._body = lambda: {
            'action': 'restore_before', 'confirm': execution['id']}
        handler._json = lambda value, code=200: (value, code)
        expected = {'id': execution['id'], 'application_status': 'conflict'}
        with patch.object(drafts_api, 'PROJECT_STORE', self.store), \
             patch.object(drafts_api, 'recover_interrupted_apply',
                          return_value=expected) as recover:
            payload, code = handler.do_POST()
        self.assertEqual(code, 200)
        self.assertEqual(payload, expected)
        recover.assert_called_once_with(
            self.store, self.project['id'], execution['id'], handler._body())

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
            if '/backup/' in str(target):
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

    def test_failed_or_stopped_execution_cannot_pass_acceptance(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.store.update_execution(execution['id'], {
            'state': 'failed', 'engine_status': 'idle', 'evidence': {}})
        with self.assertRaisesRegex(ProjectStoreError, 'cannot pass acceptance'):
            self.store.record_acceptance(
                self.task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}],
                [condition_result(self.requirement, 'passed')])
        waived = self.store.record_acceptance(
            self.task['id'], 'waived',
            [{'kind': 'review', 'summary': 'Superseded by an explicit follow-up'}],
            [condition_result(self.requirement, 'waived')])
        self.assertEqual(waived['acceptance_status'], 'waived')

    def test_applied_result_without_adopted_baseline_cannot_pass_acceptance(self):
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
        self.assertIn('baseline_adoption_error', applied['application_state'])
        with self.assertRaisesRegex(ProjectStoreError, 'accepted workspace baseline'):
            self.store.record_acceptance(
                self.task['id'], 'passed', [{'kind': 'review', 'summary': 'Looks good'}],
                [condition_result(self.requirement, 'passed')])

    def test_requirement_revisions_are_frozen_into_iterations_and_tasks(self):
        self.assertEqual(self.iteration['baseline_id'], self.baseline['id'])
        self.assertEqual(self.iteration['requirement_revisions'],
                         [{'requirement_id': self.requirement['id'], 'revision': 1}])
        updated = self.store.update_requirement(
            self.project['id'], self.requirement['id'], content='Value becomes three')
        self.assertEqual(updated['revision'], 2)
        self.assertIsNone(updated['confirmed_scope'])
        revisions = self.store.list_requirement_revisions(
            self.project['id'], self.requirement['id'])
        self.assertEqual([item['revision'] for item in revisions], [2, 1])
        self.assertEqual(revisions[1]['content'], 'Value becomes two')

        task = self.store.get_task(self.task['id'])
        self.assertEqual(task['requirement_revisions'],
                         [{'requirement_id': self.requirement['id'], 'revision': 1}])
        context = self.store.task_context(self.task['id'])
        self.assertEqual(context['requirements'][0]['content'], 'Value becomes two')
        self.assertEqual(context['requirements'][0]['revision'], 1)

        recommendation_only = self.store.update_requirement(
            self.project['id'], self.requirement['id'],
            recommended_scope='later', recommendation_reason='Still later')
        self.assertEqual(recommendation_only['revision'], 2)
        self.assertEqual(recommendation_only['content'], 'Value becomes three')

    def test_iteration_baseline_requires_an_explicit_rebase(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        applied = apply_execution_result(
            self.store, self.project['id'], execution['id'])
        new_baseline = applied['application_state']['accepted_baseline_id']
        self.assertNotEqual(new_baseline, self.baseline['id'])

        with self.assertRaisesRegex(ProjectStoreError, 'rebase the iteration'):
            start_execution(
                self.store, self.project['id'], self.task['id'], {}, self.client)
        rebased = rebase_iteration(
            self.store, self.project['id'], self.iteration['id'], {})
        self.assertEqual(rebased['baseline_id'], new_baseline)
        self.assertEqual(rebased['baseline_history'][0]['baseline_id'], self.baseline['id'])
        created = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        self.assertEqual(created['status'], 'running')
        self.assertEqual(created['input_state']['workspace_baseline']['id'], new_baseline)

    def test_interrupted_apply_recovers_the_intended_result(self):
        execution = start_execution(
            self.store, self.project['id'], self.task['id'], {}, self.client)
        (Path(execution['workdir']) / 'src/app.py').write_text('VALUE = 2\n')
        self.client.mode = 'completed'
        completed = reconcile_execution(
            self.store, self.project['id'], execution['id'], self.client)
        before = self.store.get_snapshot(self.project['id'], execution['before_snapshot_id'])
        after = self.store.get_snapshot(
            self.project['id'], completed['after_snapshot_id'])
        difference = compare_snapshots(before['manifest'], after['manifest'])
        self.store.record_execution_application(execution['id'], 'applying', {
            'baseline_id': self.baseline['id'],
            'execution_workdir': execution['workdir'],
            'apply_intent': {'after_snapshot_id': completed['after_snapshot_id']},
        })
        apply_execution_workspace(
            str(self.workspace), execution['workdir'], before['manifest'],
            after['manifest'], difference, execution['id'])

        recovered = apply_execution_result(
            self.store, self.project['id'], execution['id'])
        self.assertEqual(recovered['application_status'], 'applied')
        self.assertTrue(recovered['application_state']['recovered_from_interrupted_apply'])
        self.assertEqual((self.workspace / 'src/app.py').read_text(), 'VALUE = 2\n')
        self.assertIsNotNone(recovered['application_state']['accepted_baseline_id'])

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


class ClassificationProviderTests(unittest.TestCase):
    class Response:
        def __init__(self, payload):
            self.payload = payload

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def read(self):
            return json.dumps(self.payload).encode("utf-8")

    @staticmethod
    def state():
        return classifier.Snapshot(
            ("task-management-application",), np.array([[1.0]], dtype=np.float32),
            {"task-management-application": ("任务管理", "任务和项目记录")},
            {"task-management-application": "01"}, {}, {},
        )

    def test_classify_uses_explicit_model_and_returns_stable_metadata(self):
        observed = {}

        def fake_chat(messages, **kwargs):
            observed["model"] = kwargs.get("model")
            observed["timeout"] = kwargs.get("timeout")
            observed["role"] = kwargs.get("role")
            return {
                "content": ('[{"slug":"task-management-application","score":9,"brief":"ok"}]\n'
                            '{"choice":"task-management-application"}'),
                "model": "qwen3.8-flash",
            }

        with patch.object(classifier, "snapshot", return_value=self.state()), \
             patch.object(classifier, "candidates", return_value=(
                 ("task-management-application",), {"task-management-application": 0.9})), \
             patch.object(classifier.atlas_model, "chat", side_effect=fake_chat):
            result = classifier.classify("local task history", model="qwen3.8-flash")
        self.assertEqual(result["choice"], "task-management-application")
        self.assertEqual(result["model"], "qwen3.8-flash")
        self.assertEqual(observed["model"], "qwen3.8-flash")
        self.assertEqual(observed["timeout"], 300)
        self.assertEqual(observed["role"], "adjudicator")

    def test_unavailable_model_is_redacted_and_not_retried(self):
        # A provider rejecting the model must surface as a non-retryable
        # configuration failure, and the credential must not leak into it.
        error = classifier.atlas_model.ModelConfigError(
            "the selected model is unavailable on this provider",
            code="model_unavailable", status=400)
        with patch.object(classifier, "snapshot", return_value=self.state()), \
             patch.object(classifier, "candidates", return_value=(
                 ("task-management-application",), {"task-management-application": 0.9})), \
             patch.object(classifier.atlas_model, "chat", side_effect=error) as chat:
            with self.assertRaises(classifier.ClassificationProviderError) as raised:
                classifier.classify("local task history", model="unavailable/model")
        self.assertEqual(raised.exception.code, "model_unavailable")
        self.assertFalse(raised.exception.retryable)
        self.assertEqual(chat.call_count, 1)

    def test_provider_http_failure_is_retryable_without_fallback(self):
        import urllib.error

        error = urllib.error.HTTPError(
            "https://opencode.ai/zen/go/v1/chat/completions", 503, "Unavailable", {},
            io.BytesIO(b"{}"))
        with patch.object(classifier, "snapshot", return_value=self.state()), \
             patch.object(classifier, "candidates", return_value=(
                 ("task-management-application",), {"task-management-application": 0.9})), \
             patch.object(classifier.atlas_model, "_post_json", side_effect=error):
            with self.assertRaises(classifier.ClassificationProviderError) as raised:
                classifier.classify("local task history", model="qwen3.8-flash")
        self.assertEqual(raised.exception.code, "provider_http_error")
        self.assertTrue(raised.exception.retryable)

    def test_provider_credential_is_never_echoed(self):
        # The raw provider body may quote the credential; it must be redacted
        # before it can reach a caller or the persisted detail field.
        import urllib.error

        error = urllib.error.HTTPError(
            "https://opencode.ai/zen/go/v1/chat/completions", 400, "Bad Request", {},
            io.BytesIO(b'{"error":{"message":"bad key. Authorization: Bearer test-secret"}}'))
        with patch.object(classifier, "snapshot", return_value=self.state()), \
             patch.object(classifier, "candidates", return_value=(
                 ("task-management-application",), {"task-management-application": 0.9})), \
             patch.object(classifier.atlas_model, "_post_json", side_effect=error):
            with self.assertRaises(classifier.ClassificationProviderError) as raised:
                classifier.classify("local task history", model="qwen3.8-flash")
        self.assertNotIn("test-secret", str(raised.exception))
        self.assertNotIn("test-secret", raised.exception.detail)


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


class RuntimeRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / 'workspace'
        self.workspace.mkdir()
        self.store = ProjectStore(self.root / 'state' / 'projects.sqlite')
        self.project = self.store.create_project(
            'Recovery', 'Recover interrupted work safely', self.workspace, 'existing')

    def test_startup_recovery_marks_active_work_unknown_without_replay(self):
        from runtime_recovery import recover_atlas_runtime
        running_task = self.store.create_task(
            self.project['id'], 'Running', 'Interrupted running task', kind='analysis')
        running = self.store.create_execution(
            running_task['id'], 'opencode', 'ses_running')
        self.store.update_execution(running['id'], {
            'state': 'running', 'engine_status': 'busy', 'evidence': {},
            'interaction': {'type': 'permission', 'request': {'id': 'per_keep'}}})
        applying_task = self.store.create_task(
            self.project['id'], 'Applying', 'Interrupted applying task')
        applying = self.store.create_execution(
            applying_task['id'], 'opencode', 'ses_applying',
            application_status='pending')
        self.store.record_execution_application(
            applying['id'], 'applying', {'apply_intent': {'after_snapshot_id': 'snap_missing'}})
        reference = self.store.add_reference(
            self.project['id'], 'atlas:application', 'sample', 'v1',
            excerpt='Fixed recovery evidence')
        self.assertTrue(reference['id'].startswith('ref_'))
        generation = prepare_generation(self.store, self.project['id'], 'analysis')
        staging = self.workspace / '.atlas-apply-test'
        staging.mkdir()
        (staging / 'new').mkdir()

        report = recover_atlas_runtime(self.store)
        self.assertFalse(report['automatic_replay'])
        self.assertEqual(len(report['executions_interrupted']), 2)
        self.assertEqual(len(report['generations_interrupted']), 1)
        self.assertEqual(len(report['applications_requiring_review']), 1)
        self.assertEqual(report['staging_directories'][0]['action'], 'reported_only')
        recovered = self.store.get_execution(running['id'])
        self.assertEqual(recovered['status'], 'unknown')
        self.assertEqual(recovered['raw_state']['engine_status'], 'api_restart_interrupted')
        self.assertEqual(recovered['raw_state']['interaction']['request']['id'], 'per_keep')
        self.event = recovered['raw_state']['evidence']['recovery_events'][-1]
        self.assertEqual(self.event['previous_status'], 'running')
        self.assertFalse(self.event['automatic_replay'])
        self.assertEqual(self.store.get_execution(applying['id'])['application_status'], 'applying')
        from project_generation import read_generation
        self.assertEqual(read_generation(
            self.store, self.project['id'], generation['id'])['status'], 'failed')
        self.assertTrue(staging.exists())
        latest = self.root / 'state' / 'runtime' / 'recovery' / 'latest.json'
        self.assertTrue(latest.is_file())
        self.assertEqual(latest.stat().st_mode & 0o777, 0o600)

        second = recover_atlas_runtime(self.store)
        self.assertEqual(second['executions_interrupted'], [])
        self.assertEqual(second['generations_interrupted'], [])
        self.assertEqual(len(second['applications_requiring_review']), 1)

    def test_startup_recovery_reports_a_journaled_apply_stage(self):
        from execution_workspace import _write_apply_journal
        from runtime_recovery import recover_atlas_runtime
        task = self.store.create_task(
            self.project['id'], 'Journaled apply', 'Keep the journal visible')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_journaled', application_status='pending')
        self.store.update_execution(execution['id'], {'state': 'completed'})
        self.store.record_execution_application(
            execution['id'], 'applying', {'apply_intent': {'after_snapshot_id': 'snap_missing'}})
        stage = self.workspace / '.atlas-apply-journaled'
        stage.mkdir()
        _write_apply_journal(stage, {
            'schema': 1,
            'execution_id': execution['id'],
            'before_manifest': {'files': {}},
            'after_manifest': {'files': {}},
            'difference': {'added': [], 'modified': [], 'removed': []},
            'phase': 'installing',
            'backed_up': [],
            'applied': [],
        })
        report = recover_atlas_runtime(self.store)
        entry = next(item for item in report['staging_directories']
                     if item.get('execution_id') == execution['id'])
        self.assertEqual(entry['action'], 'explicit_apply_recovery_required')
        self.assertEqual(entry['phase'], 'installing')
        self.assertTrue(Path(entry['journal']).is_file())

    def test_startup_recovery_reports_malformed_generation_runs(self):
        from runtime_recovery import recover_atlas_runtime
        broken = self.root / 'state' / 'generation-runs' / self.project['id'] / 'gen_broken'
        broken.mkdir(parents=True)
        (broken / 'run.json').write_text('{not valid json', encoding='utf-8')
        report = recover_atlas_runtime(self.store)
        self.assertTrue(any(item.get('scope') == 'generations'
                            for item in report['errors']))

    def test_project_store_process_lock_prevents_two_api_owners(self):
        from runtime_recovery import acquire_project_store_lock
        first = acquire_project_store_lock(self.store.path)
        self.addCleanup(first.close)
        lock_path = self.store.path.parent / 'runtime' / 'api-process.lock'
        self.assertEqual(lock_path.stat().st_mode & 0o777, 0o600)
        with self.assertRaisesRegex(RuntimeError, 'another Atlas API process'):
            acquire_project_store_lock(self.store.path)
        first.close()
        replacement = acquire_project_store_lock(self.store.path)
        replacement.close()


class ProjectBackupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = ProjectStore(self.root / 'state' / 'projects.sqlite')
        self.workspace = self.root / 'workspace'
        self.workspace.mkdir()
        (self.workspace / 'keep.py').write_text('print("source")\n')
        self.project = self.store.create_project(
            'Backup me', 'Preserve accepted intent', self.workspace, 'existing')
        requirement = self.store.create_requirement(
            self.project['id'], 'Keep accepted scope', 'current', 'User approved')
        self.store.confirm_requirement(requirement['id'], 'current', 'Approved')
        self.document = self.store.create_document(
            self.project['id'], 'technical-plan', 'Plan', '# Plan\n\nAccepted content')
        other_workspace = self.root / 'other-workspace'
        other_workspace.mkdir()
        self.other = self.store.create_project(
            'Other project', 'Must not enter scoped backup', other_workspace, 'existing')
        self.store.create_requirement(
            self.other['id'], 'Other requirement', 'later', 'Out of scope')

    def test_backup_is_project_scoped_and_restores_to_a_new_store(self):
        from project_backup import (
            ProjectBackupError, create_project_backup, restore_project_backup,
            validate_project_backup,
        )
        artifacts = {
            'generation-runs': 'gen_test/run.json',
            'execution-evidence': 'exe_test/stderr.txt',
            'exports': 'bundle/manifest.json',
        }
        for name, relative in artifacts.items():
            path = self.store.path.parent / name / self.project['id'] / relative
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'project_id': self.project['id']}))
        other_artifact = (self.store.path.parent / 'exports' / self.other['id'] /
                          'other.txt')
        other_artifact.parent.mkdir(parents=True)
        other_artifact.write_text('other')

        create_project_backup(self.store, self.project['id'])
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        handler.path = f"/api/projects/{self.project['id']}/backup"
        handler._body = lambda: {}
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            api_result, code = handler.do_POST()
        self.assertEqual(code, 201)
        self.assertNotIn('archive', api_result)
        self.assertRegex(api_result['archive_name'], r'^\d{8}T\d{6}Z-[0-9a-f]{8}\.zip$')
        self.assertTrue(api_result['download_url'].endswith(api_result['archive_name']))
        handler.path = api_result['download_url']
        handler._file = lambda path, name: (path, name)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            downloaded = handler.do_GET()
        self.assertEqual(downloaded[1], api_result['archive_name'])

        archive = (self.store.path.parent / "backups" / self.project['id'] /
                   api_result['archive_name'])
        self.assertEqual(archive.stat().st_mode & 0o777, 0o600)
        self.assertEqual(archive.parent.stat().st_mode & 0o777, 0o700)
        manifest = validate_project_backup(archive)
        self.assertEqual(manifest['project_id'], self.project['id'])
        self.assertFalse(manifest['source_workspace_included'])
        with zipfile.ZipFile(archive) as bundle:
            names = bundle.namelist()
        self.assertIn('backup/project.sqlite', names)
        self.assertFalse(any(self.other['id'] in name for name in names))
        self.assertFalse(any('keep.py' in name for name in names))

        target = self.root / 'restored' / 'projects.sqlite'
        restored = restore_project_backup(archive, target)
        self.assertEqual(restored['project_id'], self.project['id'])
        store = ProjectStore(target)
        self.assertEqual([item['id'] for item in store.list_projects()], [self.project['id']])
        self.assertEqual(store.get_document(self.document['id'])['content'],
                         '# Plan\n\nAccepted content')
        self.assertEqual(target.stat().st_mode & 0o777, 0o600)
        for name, relative in artifacts.items():
            restored_artifact = target.parent / name / self.project['id'] / relative
            self.assertTrue(restored_artifact.is_file(), relative)
            self.assertEqual(restored_artifact.stat().st_mode & 0o777, 0o600)
        self.assertEqual((self.workspace / 'keep.py').read_text(), 'print("source")\n')
        with self.assertRaisesRegex(ProjectBackupError, 'already exists'):
            restore_project_backup(archive, target)

    def test_browser_backup_list_and_restore_target_are_controlled(self):
        import drafts_api
        from project_backup import create_project_backup
        created = create_project_backup(self.store, self.project['id'])
        archive_name = Path(created['archive']).name
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            handler.path = f'/api/projects/{self.project["id"]}/backups'
            listed, code = handler.do_GET()
            self.assertEqual(code, 200)
            self.assertEqual(len(listed['backups']), 1)
            self.assertEqual(listed['backups'][0]['name'], archive_name)
            self.assertNotIn('archive', listed['backups'][0])

            handler.path = (
                f'/api/projects/{self.project["id"]}/backups/{archive_name}/restore-target')
            handler._body = lambda: {}
            prepared, code = handler.do_POST()
            self.assertEqual(code, 201)
            self.assertNotIn('target_store', prepared)
            self.assertRegex(prepared['restore_id'], r'^restore_[0-9a-f]{32}$')

            handler.path = (
                f'/api/projects/{self.project["id"]}/backups/{archive_name}/restore')
            handler._body = lambda: {
                'restore_id': prepared['restore_id'],
                'confirm': 'restore_to_new_store',
                'target_store': '/tmp/should-not-be-accepted',
            }
            rejected, code = handler.do_POST()
            self.assertEqual(code, 400)
            self.assertIn('only', rejected['error'])
            self.assertEqual(rejected['code'], 'invalid_request')
            self.assertFalse(rejected['retryable'])

            handler._body = lambda: {
                'restore_id': prepared['restore_id'],
                'confirm': 'restore_to_new_store',
            }
            restored, code = handler.do_POST()
            self.assertEqual(code, 201)
            self.assertEqual(restored['status'], 'completed')
            self.assertNotIn('store', restored)
            self.assertNotIn('target_store', restored)
            self.assertEqual(restored['project_id'], self.project['id'])

            handler.path = (
                f'/api/projects/{self.project["id"]}/restore-status/'
                f'{prepared["restore_id"]}')
            status, code = handler.do_GET()
            self.assertEqual(code, 200)
            self.assertEqual(status['status'], 'completed')
            self.assertNotIn('target_store', status)
        self.assertEqual((self.workspace / 'keep.py').read_text(), 'print("source")\n')

    def test_browser_backup_delete_and_restore_cleanup_are_explicit(self):
        import drafts_api
        import project_backup
        from project_backup import create_project_backup, prepare_project_restore
        created = create_project_backup(self.store, self.project['id'])
        archive_name = Path(created['archive']).name
        handler = object.__new__(drafts_api.Handler)
        handler._json = lambda value, code=200: (value, code)
        with patch.object(drafts_api, 'PROJECT_STORE', self.store):
            handler.path = f'/api/projects/{self.project["id"]}/backups/{archive_name}'
            handler._body = lambda: {}
            rejected, code = handler.do_DELETE()
            self.assertEqual(code, 400)
            self.assertIn('confirmation', rejected['error'])
            handler._body = lambda: {'confirm': 'delete_backup'}
            deleted, code = handler.do_DELETE()
            self.assertEqual(code, 200)
            self.assertTrue(deleted['deleted'])
            self.assertFalse(Path(created['archive']).exists())

            prepared = prepare_project_restore(self.store, self.project['id'])
            target = Path(prepared['target_store'])
            stage = target.parent / '.atlas-restore-test'
            stage.mkdir()
            project_backup._write_restore_journal(
                project_backup._restore_journal_path(target), {
                    'schema': project_backup.RESTORE_JOURNAL_SCHEMA,
                    'project_id': self.project['id'],
                    'target_store': str(target),
                    'artifact_root': str(target.parent),
                    'stage': str(stage),
                    'phase': 'extracting',
                    'installed_artifacts': [],
                    'artifact_fingerprints': {},
                    'database_sha256': '',
                    'database_installed': False,
                })
            handler.path = (
                f'/api/projects/{self.project["id"]}/restore-status/'
                f'{prepared["restore_id"]}/recover')
            handler._body = lambda: {'confirm': 'cleanup_partial_restore'}
            recovered, code = handler.do_POST()
            self.assertEqual(code, 200)
            self.assertEqual(recovered['status'], 'recovered')
            self.assertFalse(stage.exists())
            handler.path = (
                f'/api/projects/{self.project["id"]}/restore-status/'
                f'{prepared["restore_id"]}')
            status, code = handler.do_GET()
            self.assertEqual(code, 200)
            self.assertEqual(status['status'], 'not_started')
        self.assertEqual((self.workspace / 'keep.py').read_text(), 'print("source")\n')

    def test_prepare_restore_target_rejects_workspace_overlap(self):
        from project_backup import ProjectBackupError, prepare_project_restore
        overlap_store = ProjectStore(self.workspace / 'atlas' / 'projects.sqlite')
        overlap_project = overlap_store.create_project(
            'Overlap', 'Must not create restore state in source', self.workspace, 'existing')
        with self.assertRaisesRegex(ProjectBackupError, 'overlaps'):
            prepare_project_restore(overlap_store, overlap_project['id'])

    def test_restore_validates_and_extracts_the_same_archive_handle(self):
        import project_backup
        from project_backup import create_project_backup, restore_project_backup
        result = create_project_backup(self.store, self.project['id'])
        archive = Path(result['archive'])
        replacement = self.root / 'replacement.zip'
        with zipfile.ZipFile(archive) as source, zipfile.ZipFile(
                replacement, 'w', zipfile.ZIP_DEFLATED) as changed:
            changed.writestr('backup/undeclared.txt', b'changed')
            for item in source.infolist():
                changed.writestr(item, source.read(item.filename))
        real_validate = project_backup._validate_open_backup

        def validate_then_replace(bundle):
            manifest = real_validate(bundle)
            os.replace(replacement, archive)
            return manifest

        target = self.root / 'same-handle' / 'projects.sqlite'
        with patch.object(project_backup, '_validate_open_backup',
                          side_effect=validate_then_replace):
            restored = restore_project_backup(archive, target)
        self.assertEqual(restored['project_id'], self.project['id'])
        self.assertEqual(ProjectStore(target).get_project(self.project['id'])['id'],
                         self.project['id'])

    def test_interrupted_restore_keeps_journal_until_explicit_cleanup(self):
        import project_backup
        from project_backup import (
            RESTORE_RECOVERY_CONFIRMATION, create_project_backup,
            inspect_project_restore, recover_interrupted_restore,
        )
        artifact = self.store.path.parent / 'exports' / self.project['id'] / 'bundle'
        artifact.mkdir(parents=True)
        (artifact / 'manifest.json').write_text('{"ok": true}\n', encoding='utf-8')
        result = create_project_backup(self.store, self.project['id'])
        target = self.root / 'interrupted-restore' / 'projects.sqlite'
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import project_backup
real_rename = project_backup.os.rename
def crash_after_rename(source, destination):
    real_rename(source, destination)
    if '/exports/' in str(destination):
        os._exit(78)
project_backup.os.rename = crash_after_rename
project_backup.restore_project_backup(sys.argv[2], sys.argv[3])
"""
        crashed = subprocess.run([
            sys.executable, '-c', script, str(CODE), result['archive'], str(target),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(crashed.returncode, 78)
        status = inspect_project_restore(target)
        self.assertTrue(status['interrupted'])
        self.assertFalse(target.exists())
        with self.assertRaisesRegex(project_backup.ProjectBackupError, 'confirm'):
            recover_interrupted_restore(target)
        recovered = recover_interrupted_restore(target, RESTORE_RECOVERY_CONFIRMATION)
        self.assertEqual(recovered['action'], 'cleanup_partial_restore')
        self.assertFalse(inspect_project_restore(target)['interrupted'])
        self.assertFalse(target.exists())

    def test_restore_database_link_crash_window_is_explicitly_recoverable(self):
        from project_backup import (
            RESTORE_RECOVERY_CONFIRMATION, create_project_backup,
            inspect_project_restore, recover_interrupted_restore,
        )
        result = create_project_backup(self.store, self.project['id'])
        target = self.root / 'db-crash' / 'projects.sqlite'
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import project_backup
real_link = project_backup.os.link
def crash_after_link(source, destination):
    real_link(source, destination)
    os._exit(79)
project_backup.os.link = crash_after_link
project_backup.restore_project_backup(sys.argv[2], sys.argv[3])
"""
        crashed = subprocess.run([
            sys.executable, '-c', script, str(CODE), result['archive'], str(target),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(crashed.returncode, 79)
        status = inspect_project_restore(target)
        self.assertTrue(status['interrupted'])
        self.assertFalse(status['database_installed'])
        self.assertTrue(target.is_file())
        recovered = recover_interrupted_restore(target, RESTORE_RECOVERY_CONFIRMATION)
        self.assertEqual(recovered['action'], 'cleanup_partial_restore')
        self.assertFalse(target.exists())
        self.assertFalse(inspect_project_restore(target)['interrupted'])

    def test_restore_recovery_refuses_replaced_database(self):
        from project_backup import (
            RESTORE_RECOVERY_CONFIRMATION, ProjectBackupError, create_project_backup,
            inspect_project_restore, recover_interrupted_restore,
        )
        result = create_project_backup(self.store, self.project['id'])
        target = self.root / 'replaced-db' / 'projects.sqlite'
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import project_backup
real_link = project_backup.os.link
def crash_after_link(source, destination):
    real_link(source, destination)
    os._exit(82)
project_backup.os.link = crash_after_link
project_backup.restore_project_backup(sys.argv[2], sys.argv[3])
"""
        crashed = subprocess.run([
            sys.executable, '-c', script, str(CODE), result['archive'], str(target),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(crashed.returncode, 82)
        target.write_bytes(b'not the restored database')
        with self.assertRaisesRegex(ProjectBackupError, 'changed after database installation'):
            recover_interrupted_restore(target, RESTORE_RECOVERY_CONFIRMATION)
        self.assertTrue(target.exists())
        self.assertTrue(inspect_project_restore(target)['interrupted'])

    def test_restore_artifact_journal_precedes_atomic_install(self):
        from project_backup import (
            RESTORE_RECOVERY_CONFIRMATION, create_project_backup,
            inspect_project_restore, recover_interrupted_restore,
        )
        artifact = self.store.path.parent / 'exports' / self.project['id'] / 'bundle'
        artifact.mkdir(parents=True)
        (artifact / 'manifest.json').write_text('{"ok": true}\n', encoding='utf-8')
        result = create_project_backup(self.store, self.project['id'])
        target = self.root / 'artifact-journal' / 'projects.sqlite'
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import project_backup
real_rename = project_backup.os.rename
def crash_before_rename(source, destination):
    if '/exports/' in str(destination):
        os._exit(80)
    return real_rename(source, destination)
project_backup.os.rename = crash_before_rename
project_backup.restore_project_backup(sys.argv[2], sys.argv[3])
"""
        crashed = subprocess.run([
            sys.executable, '-c', script, str(CODE), result['archive'], str(target),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(crashed.returncode, 80)
        status = inspect_project_restore(target)
        self.assertTrue(status['interrupted'])
        self.assertFalse(target.exists())
        self.assertTrue(status['installed_artifacts'])
        recovered = recover_interrupted_restore(target, RESTORE_RECOVERY_CONFIRMATION)
        self.assertEqual(recovered['action'], 'cleanup_partial_restore')
        self.assertFalse(inspect_project_restore(target)['interrupted'])

    def test_restore_recovery_refuses_replaced_artifact(self):
        from project_backup import (
            RESTORE_RECOVERY_CONFIRMATION, ProjectBackupError, create_project_backup,
            inspect_project_restore, recover_interrupted_restore,
        )
        artifact = self.store.path.parent / 'exports' / self.project['id'] / 'bundle'
        artifact.mkdir(parents=True)
        (artifact / 'manifest.json').write_text('{"ok": true}\n', encoding='utf-8')
        result = create_project_backup(self.store, self.project['id'])
        target = self.root / 'replaced-artifact' / 'projects.sqlite'
        script = """
import os, sys
sys.path.insert(0, sys.argv[1])
import project_backup
real_rename = project_backup.os.rename
def crash_after_rename(source, destination):
    real_rename(source, destination)
    if '/exports/' in str(destination):
        os._exit(81)
project_backup.os.rename = crash_after_rename
project_backup.restore_project_backup(sys.argv[2], sys.argv[3])
"""
        crashed = subprocess.run([
            sys.executable, '-c', script, str(CODE), result['archive'], str(target),
        ], cwd=str(CODE), capture_output=True)
        self.assertEqual(crashed.returncode, 81)
        installed = target.parent / 'exports' / self.project['id']
        (installed / 'manifest.json').write_text('{"changed": true}\n', encoding='utf-8')
        with self.assertRaisesRegex(ProjectBackupError, 'changed after installation'):
            recover_interrupted_restore(target, RESTORE_RECOVERY_CONFIRMATION)
        self.assertTrue(installed.exists())
        self.assertTrue(inspect_project_restore(target)['interrupted'])

    def test_backup_redacts_legacy_execution_evidence_in_the_copy(self):
        from project_backup import create_project_backup
        task = self.store.create_task(
            self.project['id'], 'Legacy evidence', 'Backup redacts old evidence')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_legacy', application_status='not_applicable')
        self.store.update_execution(execution['id'], {'state': 'stopped'})
        with sqlite3.connect(self.store.path) as con:
            con.execute(
                'UPDATE execution SET raw_state_json=? WHERE id=?',
                (json.dumps({'evidence': {'token': 'legacy-secret-value'}}), execution['id']))
            con.commit()
        result = create_project_backup(self.store, self.project['id'])
        with zipfile.ZipFile(result['archive']) as bundle:
            data = bundle.read('backup/project.sqlite')
        restored = self.root / 'redacted.sqlite'
        restored.write_bytes(data)
        with sqlite3.connect(restored) as con:
            raw = con.execute(
                'SELECT raw_state_json FROM execution WHERE id=?', (execution['id'],)
            ).fetchone()[0]
        self.assertNotIn('legacy-secret-value', raw)
        self.assertIn('[REDACTED]', raw)
        self.assertNotIn(b'legacy-secret-value', data)

    def test_backup_refuses_active_work(self):
        from project_backup import ProjectBackupError, create_project_backup
        task = self.store.create_task(
            self.project['id'], 'Active', 'Must finish before backup')
        self.store.create_execution(task['id'], 'opencode', 'ses_active')
        with self.assertRaisesRegex(ProjectBackupError, 'active generation or execution'):
            create_project_backup(self.store, self.project['id'])

    def test_backup_refuses_unapplied_completed_results(self):
        from project_backup import ProjectBackupError, create_project_backup
        task = self.store.create_task(
            self.project['id'], 'Pending result', 'Cannot restore an isolated result')
        execution = self.store.create_execution(
            task['id'], 'opencode', 'ses_pending_backup', application_status='pending')
        self.store.update_execution(execution['id'], {'state': 'completed'})
        with self.assertRaisesRegex(ProjectBackupError, 'active generation or execution'):
            create_project_backup(self.store, self.project['id'])

    def test_backup_validation_detects_tampering(self):
        from project_backup import ProjectBackupError, create_project_backup, validate_project_backup
        result = create_project_backup(self.store, self.project['id'])
        source = Path(result['archive'])
        tampered = self.root / 'tampered.zip'
        with zipfile.ZipFile(source) as original:
            with zipfile.ZipFile(tampered, 'w', zipfile.ZIP_DEFLATED) as changed:
                for item in original.infolist():
                    data = original.read(item.filename)
                    if item.filename == 'backup/project.sqlite':
                        data += b'tampered'
                    changed.writestr(item, data)
        with self.assertRaisesRegex(ProjectBackupError, 'hash mismatch'):
            validate_project_backup(tampered)


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

    def test_web_data_publish_rolls_back_an_interrupted_directory_swap(self):
        import importlib.util
        script = CODE.parent / 'atlas-web/scripts/gen-data.py'
        spec = importlib.util.spec_from_file_location('atlas_gen_data_test', script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / 'data'
            output.mkdir()
            (output / 'marker.txt').write_text('old')
            stage = root / '.data.staging-test'
            stage.mkdir()
            (stage / 'marker.txt').write_text('new')
            real_replace = os.replace
            def fail_cutover(source, target):
                if Path(source).name.startswith('.data.staging-') and Path(target) == output:
                    raise OSError('simulated cutover failure')
                return real_replace(source, target)
            with patch.object(module.os, 'replace', side_effect=fail_cutover):
                with self.assertRaisesRegex(OSError, 'simulated cutover failure'):
                    module.publish_web_data(stage, output)
            self.assertEqual((output / 'marker.txt').read_text(), 'old')
            self.assertFalse(stage.exists())
            self.assertFalse((root / '.data.publish.json').exists())
            self.assertEqual(list(root.glob('.data.backup-*')), [])

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


    def test_web_data_generation_removes_stale_files_and_matches_leaf_index(self):
        self.fill_aux(self.pack)
        output = self.pack / 'web-data'
        (output / 'leaves').mkdir(parents=True)
        (output / 'sections').mkdir(parents=True)
        (output / 'leaves' / 'stale-tool.json').write_text('{}')
        (output / 'sections' / 'stale-section.json').write_text('{}')
        self.run_script(self.pack, '../atlas-web/scripts/gen-data.py')
        meta = json.loads((output / 'meta.json').read_text())
        leaf_files = {path.stem for path in (output / 'leaves').glob('*.json')}
        self.assertEqual(meta['leafCount'], 1)
        self.assertEqual(leaf_files, {'existing-tool'})
        self.assertFalse((output / 'leaves' / 'stale-tool.json').exists())
        self.assertFalse((output / 'sections' / 'stale-section.json').exists())
        self.assertEqual(json.loads((output / 'leaves/existing-tool.json').read_text())['slug'],
                         'existing-tool')

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

    def test_draft_body_revision_rejects_stale_save_and_promote(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')):
            original = drafts_api.read_draft('wip-new')['body_sha256']
            changed = self.draft.read_text() + '\nLocal edit'
            new_hash = drafts_api.save_body('wip-new', changed, original)
            self.assertNotEqual(new_hash, original)
            with self.assertRaises(drafts_api.DraftRevisionConflict):
                drafts_api.save_body('wip-new', changed + '\nStale write', original)

            handler = object.__new__(drafts_api.Handler)
            handler.path = '/api/promote'
            handler._body = lambda: {
                'slug': 'wip-new', 'action': 'new', 'section': '01.01',
                'body_sha256': original,
            }
            responses = []
            handler._json = lambda body, code=200: responses.append((body, code))
            with patch.object(drafts_api.threading, 'Thread') as thread:
                handler.do_POST()
            self.assertEqual(responses[0][1], 409)
            thread.assert_not_called()

    def test_saving_body_invalidates_old_translation(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')):
            body_hash = drafts_api.read_draft('wip-new')['body_sha256']
            (self.pack / 'drafts/wip-new.zh.json').write_text('{"old": true}')
            (self.pack / 'drafts/wip-new.research.zh.md').write_text('旧译文')
            update_review('wip-new', {
                'translation_state': 'completed', 'translation_body_sha256': body_hash,
            }, self.pack)
            drafts_api.save_body('wip-new', self.draft.read_text() + '\nChanged', body_hash)
            self.assertFalse((self.pack / 'drafts/wip-new.zh.json').exists())
            self.assertFalse((self.pack / 'drafts/wip-new.research.zh.md').exists())
            self.assertEqual(load_review(self.pack)['wip-new']['translation_state'], 'stale')

    def test_published_review_conflict_is_read_only(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')):
            update_review('wip-new', {'promoted': True, 'final_slug': 'new-tool'}, self.pack)
            detail = drafts_api.read_draft('wip-new')
            self.assertTrue(detail['status_conflict'])
            self.assertEqual(detail['status'], 'status_conflict')
            handler = object.__new__(drafts_api.Handler)
            handler.path = '/api/drafts/wip-new'
            handler._body = lambda: {'body': 'must not write'}
            responses = []
            handler._json = lambda body, code=200: responses.append((body, code))
            handler.do_PUT()
            self.assertEqual(responses[0][1], 409)

    def test_create_rejects_empty_slug_without_writing(self):
        import drafts_api
        with patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.dn, 'collision', return_value=[]), \
             patch.object(drafts_api.threading, 'Thread') as thread:
            handler = object.__new__(drafts_api.Handler)
            handler.path = '/api/drafts'
            handler._body = lambda: {'name': '!!!', 'desc': 'an idea'}
            responses = []
            handler._json = lambda body, code=200: responses.append((body, code))
            handler.do_POST()
            self.assertEqual(responses[0][1], 400)
            self.assertFalse((self.pack / 'drafts' / '.md').exists())
            thread.assert_not_called()

    def test_concurrent_create_of_same_slug_has_one_winner(self):
        import drafts_api
        def create(_):
            handler = object.__new__(drafts_api.Handler)
            handler.path = '/api/drafts'
            handler._body = lambda: {'name': 'Same Slug', 'desc': 'same idea'}
            responses = []
            handler._json = lambda body, code=200: responses.append((body, code))
            handler.do_POST()
            return responses[0]
        with patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.dn, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.dn, 'PACK', str(self.pack)), \
             patch.object(drafts_api.dn, 'collision', return_value=[]), \
             patch.object(drafts_api, 'run_engine', lambda _slug: None):
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(create, range(2)))
        self.assertEqual(sorted(code for _, code in results), [201, 409])
        self.assertEqual(len(list((self.pack / 'drafts').glob('same-slug.md'))), 1)

    def test_dedupe_rejects_a_second_writer_while_slug_is_locked(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')):
            body_hash = drafts_api.read_draft('wip-new')['body_sha256']
            with drafts_api.dn.slug_lock('wip-new', str(self.pack / 'drafts')):
                with self.assertRaises(drafts_api.dn.SlugLockBusy):
                    drafts_api.dedupe_draft('wip-new', body_hash)

    def test_delete_removes_review_record_with_draft(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')):
            update_review('wip-new', {'verdict': 'new'}, self.pack)
            result = drafts_api.delete_draft('wip-new')
            self.assertIn('review.json:wip-new', result['removed'])
            self.assertNotIn('wip-new', load_review(self.pack))

    def test_translation_start_is_single_flight_and_durable_state(self):
        import drafts_api
        class FakeThread:
            def __init__(self, *args, **kwargs):
                pass
            def start(self):
                pass
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.threading, 'Thread', FakeThread):
            try:
                body_hash = drafts_api.read_draft('wip-new')['body_sha256']
                self.assertTrue(drafts_api.start_translation('wip-new', body_hash))
                self.assertFalse(drafts_api.start_translation('wip-new', body_hash))
                self.assertEqual(load_review(self.pack)['wip-new']['translation_state'], 'running')
            finally:
                drafts_api.TRANSLATION_THREADS.pop('wip-new', None)

    def test_restart_fails_closed_for_generation_and_translation(self):
        import drafts_api
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.dn, 'DRAFTS', str(self.pack / 'drafts')):
            self.draft.write_text(self.draft.read_text().replace('status: draft', 'status: generating'))
            update_review('wip-new', {'translation_state': 'running'}, self.pack)
            result = drafts_api.recover_interrupted_drafts()
            self.assertEqual(result, {'generating': 1, 'translations': 1})
            self.assertIn('status: failed', self.draft.read_text())
            review = load_review(self.pack)['wip-new']
            self.assertEqual(review['generation_state'], 'interrupted')
            self.assertEqual(review['translation_state'], 'failed')

    def test_failed_generation_can_be_explicitly_restarted(self):
        import drafts_api
        class FakeThread:
            def __init__(self, *args, **kwargs):
                pass
            def start(self):
                pass
        with patch.object(drafts_api, 'PACK', str(self.pack)), \
             patch.object(drafts_api, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.dn, 'DRAFTS', str(self.pack / 'drafts')), \
             patch.object(drafts_api.threading, 'Thread', FakeThread):
            self.draft.write_text(self.draft.read_text().replace('status: draft', 'status: failed'))
            (self.pack / 'drafts/wip-new.body.md').write_text('partial')
            body_hash = drafts_api.read_draft('wip-new')['body_sha256']
            try:
                self.assertTrue(drafts_api.start_regeneration('wip-new', body_hash))
                self.assertIn('status: generating', self.draft.read_text())
                self.assertFalse((self.pack / 'drafts/wip-new.body.md').exists())
            finally:
                drafts_api.GEN_THREADS.pop('wip-new', None)

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


class DraftEngineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workdir = self.root / 'pack'
        self.workdir.mkdir()
        (self.workdir / 'applications').mkdir()
        (self.workdir / 'drafts').mkdir()
        (self.workdir / 'WRITING_GUIDE.md').write_text('Guide')
        (self.workdir / 'applications' / 'one.md').write_text('One')
        (self.workdir / 'applications' / 'two.md').write_text('Two')
        (self.workdir / 'drafts' / 'safe-draft.md').write_text('Draft')

    def test_draft_permissions_deny_shell_web_and_undeclared_edits(self):
        from drafts_engines import draft_permission_config
        exemplars = ('one', 'two')
        v2 = draft_permission_config('safe-draft', exemplars, 2)
        rules = v2['permissions']
        self.assertTrue(any(
            rule == {'action': 'shell', 'resource': '*', 'effect': 'deny'}
            for rule in rules))
        self.assertTrue(any(
            rule == {'action': 'webfetch', 'resource': '*', 'effect': 'deny'}
            for rule in rules))
        self.assertTrue(any(
            rule == {'action': 'edit', 'resource': '*', 'effect': 'deny'}
            for rule in rules))
        for output in (
                'drafts/safe-draft.identity.json', 'drafts/safe-draft.body.md',
                'drafts/safe-draft.research.md'):
            self.assertTrue(any(
                rule == {'action': 'edit', 'resource': output, 'effect': 'allow'}
                for rule in rules))
        self.assertTrue(any(
            rule == {'action': 'edit', 'resource': '.opencode/**', 'effect': 'deny'}
            for rule in rules))
        self.assertFalse(any(
            rule.get('action') == 'edit' and rule.get('resource') == 'drafts/other.md'
            for rule in rules))
        self.assertTrue(any(
            rule.get('action') == 'application_atlas_get_leaf'
            for rule in rules))
        self.assertEqual(
            v2['mcp']['application-atlas']['command'][1:],
            [str(Path(__file__).resolve().parents[1] / 'mcp_atlas.py'),
             '--atlas-read-only']
        )
        self.assertTrue(Path(v2['mcp']['application-atlas']['command'][1]).is_file())

        v1 = draft_permission_config('safe-draft', exemplars, 1)
        permission = v1['permission']
        self.assertEqual(permission['bash'], 'deny')
        self.assertEqual(permission['webfetch'], 'deny')
        self.assertEqual(permission['list'], 'deny')
        self.assertEqual(permission['code_mode'], 'deny')
        self.assertEqual(permission['skill'], 'deny')
        self.assertEqual(permission['edit']['*'], 'deny')
        self.assertEqual(
            permission['edit']['drafts/safe-draft.body.md'], 'allow')
        self.assertEqual(permission['application_atlas_classify_product'], 'deny')
        self.assertEqual(permission['application_atlas_search_atlas'], 'allow')
        self.assertEqual(
            v1['mcp']['application-atlas']['command'][1:],
            [str(Path(__file__).resolve().parents[1] / 'mcp_atlas.py'),
             '--atlas-read-only']
        )

    def test_read_only_mcp_refuses_classification_side_effect(self):
        import runpy
        import sys
        original_argv = sys.argv
        try:
            sys.argv = [str(CODE / 'mcp_atlas.py'), '--atlas-read-only']
            module = runpy.run_path(
                str(CODE / 'mcp_atlas.py'), run_name='atlas_read_only_test')
        finally:
            sys.argv = original_argv
        result = json.loads(module['classify_product']('a local database tool'))
        self.assertIn('disabled', result['error'])

    def test_draft_engine_uses_temporary_exact_config_and_redacts_log(self):
        from drafts_engines import OpencodeEngine, render_prompt
        prompt_path = self.root / 'prompt.md'
        prompt_path.write_text(
            'Link: {{LINK}}\nExcerpt: {{LINK_EXCERPT}}\nSlug: {{SLUG}}')
        rendered = render_prompt(str(prompt_path), {
            'slug': 'safe-draft', 'name': 'Safe', 'name_zh': '安全',
            'desc': 'Test', 'link': 'https://example.com',
            'link_excerpt': 'untrusted public evidence',
        }, ('one', 'two'))
        self.assertIn('untrusted public evidence', rendered)
        log_path = self.workdir / 'drafts' / 'safe-draft.opencode.log'
        observed = {}
        def fake_run(argv, **kwargs):
            config_path = Path(kwargs['cwd']) / '.opencode' / 'opencode.json'
            observed['config'] = json.loads(config_path.read_text())
            observed['config_path'] = config_path
            observed['argv'] = argv
            return SimpleNamespace(
                returncode=0,
                stdout='Authorization: Bearer draft-log-secret\n',
                stderr='')
        with patch('drafts_engines.detect_opencode_major_version', return_value=2), \
             patch('drafts_engines.choose_exemplars', return_value=('one', 'two')), \
             patch('drafts_engines.subprocess.run', side_effect=fake_run):
            self.assertTrue(OpencodeEngine().generate(
                {'slug': 'safe-draft', 'name': 'Safe', 'name_zh': '安全',
                 'desc': 'Test', 'link': 'https://example.com',
                 'link_excerpt': 'untrusted public evidence'},
                str(prompt_path), str(self.workdir), str(log_path)))
        self.assertTrue(any(
            rule == {'action': 'shell', 'resource': '*', 'effect': 'deny'}
            for rule in observed['config']['permissions']))
        self.assertFalse(observed['config_path'].exists())
        self.assertNotIn('draft-log-secret', log_path.read_text())
        self.assertEqual(log_path.stat().st_mode & 0o777, 0o600)


class OpenCodeCliAdapterTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / ".atlas").mkdir()
        (self.root / ".atlas" / "harness.json").write_text(json.dumps({
            "backend": {"openCode": {"minimumCompatibleVersion": "1.18.31",
                                       "installSource": {"binaryPath": "/usr/local/bin/opencode"}}},
            "provider": {"results": [{"name": "OpenAI"}, {"name": "OpenCode Go"}]},
            "policy": {"commandTimeoutSeconds": 10},
        }))

    def test_preflight_returns_safe_evidence_without_command_output(self):
        from opencode_cli_adapter import CliResult, preflight
        def runner(argv, cwd, timeout):
            if argv[-1] == "--version":
                return CliResult(tuple(argv), 0, "opencode 1.18.31\n", "")
            return CliResult(tuple(argv), 0, "OpenAI\nOpenCode Go\nsecret-like-value\n", "")
        with patch("opencode_cli_adapter.resolve_executable", return_value="/usr/local/bin/opencode"):
            result = preflight(self.root, runner)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["version"], "1.18.31")
        self.assertNotIn("secret-like-value", json.dumps(result))
        self.assertEqual(result["providerNames"], ["OpenAI", "OpenCode Go"])

    def test_preflight_rejects_version_below_baseline(self):
        from opencode_cli_adapter import CliResult, HarnessCompatibilityError, preflight
        def runner(argv, cwd, timeout):
            return CliResult(tuple(argv), 0, "1.17.0\n", "")
        with patch("opencode_cli_adapter.resolve_executable", return_value="/usr/local/bin/opencode"):
            with self.assertRaises(HarnessCompatibilityError) as raised:
                preflight(self.root, runner)
        self.assertEqual(raised.exception.code, "version_incompatible")

    def test_preflight_marks_provider_check_failure_without_leaking_output(self):
        from opencode_cli_adapter import CliResult, preflight

        def runner(argv, cwd, timeout):
            if argv[-1] == "--version":
                return CliResult(tuple(argv), 0, "opencode 1.18.31\n", "")
            return CliResult(tuple(argv), 2, "", "provider credentials unavailable: secret-token")

        with patch("opencode_cli_adapter.resolve_executable", return_value="/usr/local/bin/opencode"):
            result = preflight(self.root, runner)
        self.assertEqual(result["status"], "failed")
        self.assertFalse(result["checks"]["providers"]["passed"])
        self.assertNotIn("secret-token", json.dumps(result))

    def test_preflight_marks_timeout_as_failed(self):
        from opencode_cli_adapter import CliResult, preflight

        def runner(argv, cwd, timeout):
            if argv[-1] == "--version":
                return CliResult(tuple(argv), 0, "opencode 1.18.31\n", "")
            return CliResult(tuple(argv), 124, "", "", timed_out=True)

        with patch("opencode_cli_adapter.resolve_executable", return_value="/usr/local/bin/opencode"):
            result = preflight(self.root, runner)
        self.assertEqual(result["status"], "failed")
        self.assertTrue(result["diagnostics"]["timedOut"])

    def test_build_run_argv_is_shell_free_and_scoped(self):
        from opencode_cli_adapter import build_run_argv
        with patch('opencode_cli_adapter.detect_opencode_major_version', return_value=2):
            argv = build_run_argv("opencode", "echo hello; touch outside", self.root, "openai/gpt")
        self.assertEqual(argv[:5], ("opencode", "run", "--format", "json", "--standalone"))
        self.assertNotIn("--dir", argv)
        self.assertNotIn("shell", argv)

    def test_summarize_run_normalizes_json_events_and_transport_state(self):
        from opencode_cli_adapter import summarize_run
        summary = summarize_run({
            "argv": ["opencode", "run", "--format", "json"],
            "exitCode": 0,
            "timedOut": False,
            "stdout": '{"type":"step.started"}\nnot-json\n{"type":"step.finished"}\n',
            "stderr": "warning",
        })
        self.assertEqual(summary["status"], "completed")
        self.assertEqual(summary["jsonEventCount"], 2)
        self.assertEqual(summary["eventTypes"], ["step.finished", "step.started"])
        self.assertEqual(summary["stderrBytes"], len("warning".encode("utf-8")))

    def test_summarize_run_distinguishes_timeout_and_failure(self):
        from opencode_cli_adapter import summarize_run
        self.assertEqual(summarize_run({"exitCode": 124, "timedOut": True})["status"], "timed_out")
        self.assertEqual(summarize_run({"exitCode": 2, "timedOut": False})["status"], "failed")

    def test_summarize_run_classifies_local_log_access_failure(self):
        from opencode_cli_adapter import summarize_run
        summary = summarize_run({
            "exitCode": 1,
            "timedOut": False,
            "stderr": "Error: Unexpected error\\nUnknown: FileSystem.open (/tmp/opencode.log)",
        })
        self.assertEqual(summary["diagnosticCode"], "log_access")
        self.assertIn("local log", summary["diagnosticHint"])

    def test_summarize_run_classifies_provider_failure_without_raw_message(self):
        from opencode_cli_adapter import summarize_run
        summary = summarize_run({
            "exitCode": 1,
            "timedOut": False,
            "stderr": "Unexpected server error. Check server logs for details.",
        })
        self.assertEqual(summary["diagnosticCode"], "provider_error")
        self.assertNotIn("server logs", summary["diagnosticHint"])

    def test_run_prompt_returns_stable_summary_alongside_raw_output(self):
        from opencode_cli_adapter import CliResult, run_prompt

        def runner(argv, cwd, timeout):
            return CliResult(tuple(argv), 0, '{"type":"run.finished"}\n', "")

        with patch("opencode_cli_adapter.resolve_executable", return_value="/usr/local/bin/opencode"):
            result = run_prompt(self.root, "hello", runner=runner)
        self.assertEqual(result["summary"]["status"], "completed")
        self.assertEqual(result["summary"]["eventTypes"], ["run.finished"])
        self.assertEqual(result["stdout"], '{"type":"run.finished"}\n')
        self.assertFalse((self.root / ".atlas" / "opencode-cli.json").exists())

    def test_cli_runner_uses_atlas_owned_v2_permissions(self):
        from opencode_cli_adapter import _run
        project_config = self.root / '.atlas' / 'opencode-cli.json'
        project_config.write_text(json.dumps({
            'permission': {'bash': 'allow', 'webfetch': 'allow'},
        }))
        original_project_config = project_config.read_text()
        observed = {}

        def fake_run(argv, **kwargs):
            config_path = Path(kwargs['cwd']) / '.opencode' / 'opencode.json'
            observed['config'] = json.loads(config_path.read_text())
            observed['path'] = config_path
            return SimpleNamespace(
                returncode=0, stdout='ok', stderr='', check=False)
        with patch('opencode_cli_adapter.detect_opencode_major_version', return_value=2), \
             patch('opencode_cli_adapter.subprocess.run', side_effect=fake_run):
            result = _run(('opencode', 'run'), self.root, 30)
        self.assertEqual(result.exit_code, 0)
        shell_rules = [
            rule for rule in observed['config']['permissions']
            if rule['action'] == 'shell']
        self.assertEqual(shell_rules, [
            {'action': 'shell', 'resource': '*', 'effect': 'deny'}])
        self.assertFalse(observed['path'].exists())
        self.assertEqual(project_config.read_text(), original_project_config)

    def test_write_run_evidence_creates_self_contained_files(self):
        from opencode_cli_adapter import write_run_evidence
        directory = self.root / "records" / "run_1"
        result = write_run_evidence({
            "argv": ["opencode", "run", "--format", "json"],
            "exitCode": 0,
            "timedOut": False,
            "stdout": '{"type":"run.finished"}\n',
            "stderr": "",
        }, directory)
        self.assertEqual(Path(result["directory"]), directory.resolve())
        self.assertTrue((directory / "run.json").exists())
        self.assertEqual((directory / "stdout.txt").read_text(), '{"type":"run.finished"}\n')
        metadata = json.loads((directory / "run.json").read_text())
        self.assertEqual(metadata["schema"], 1)
        self.assertEqual(metadata["summary"]["status"], "completed")

    def test_write_run_evidence_redacts_secrets_and_uses_private_permissions(self):
        from opencode_cli_adapter import MAX_EVIDENCE_TEXT_CHARS, write_run_evidence
        directory = self.root / "records" / "redacted"
        result = write_run_evidence({
            "argv": ["tool", "--api-key=cli-argv-secret"],
            "exitCode": 1,
            "timedOut": False,
            "stdout": "Authorization: Bearer cli-stdout-secret\n",
            "stderr": "api_key=cli-stderr-secret\n" + ("x" * MAX_EVIDENCE_TEXT_CHARS),
        }, directory)
        self.assertEqual(directory.stat().st_mode & 0o777, 0o700)
        for name in ("stdout.txt", "stderr.txt", "run.json"):
            self.assertEqual((directory / name).stat().st_mode & 0o777, 0o600)
        combined = ''.join((directory / name).read_text() for name in (
            "stdout.txt", "stderr.txt", "run.json"))
        for secret in (
                "cli-argv-secret", "cli-stdout-secret", "cli-stderr-secret"):
            self.assertNotIn(secret, combined)
        self.assertIn("[REDACTED]", combined)
        self.assertTrue(result["metadata"]["truncated"]["stderr"])
        self.assertIn("Atlas truncated", (directory / "stderr.txt").read_text())
        self.assertLessEqual(
            len((directory / "stderr.txt").read_text()), MAX_EVIDENCE_TEXT_CHARS)
        self.assertNotIn("cli-stdout-secret", result["metadata"]["argv"])


class OpenCodePermissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'run'
        self.root.mkdir()

    def test_v2_policy_is_restored_after_a_temporary_run(self):
        from opencode_permissions import (
            install_workdir_permission_policy, remove_workdir_permission_policy,
        )
        target = self.root / '.opencode' / 'opencode.json'
        target.parent.mkdir()
        original = {'permissions': [
            {'action': 'shell', 'resource': '*', 'effect': 'allow'}]}
        target.write_text(json.dumps(original), encoding='utf-8')
        state = install_workdir_permission_policy(self.root, 2, allow_edit=True)
        self.assertEqual(state['schema'], 1)
        policy = json.loads(target.read_text(encoding='utf-8'))
        self.assertEqual(policy['permissions'][0], {
            'action': '*', 'resource': '*', 'effect': 'deny'})
        self.assertIn(
            {'action': 'shell', 'resource': '*', 'effect': 'deny'},
            policy['permissions'])
        self.assertIn(
            {'action': 'edit', 'resource': '.opencode/**', 'effect': 'deny'},
            policy['permissions'])
        self.assertEqual(target.stat().st_mode & 0o777, 0o400)
        os.chmod(target, 0o600)
        target.write_text('agent replacement', encoding='utf-8')
        self.assertTrue(remove_workdir_permission_policy(self.root))
        self.assertEqual(json.loads(target.read_text(encoding='utf-8')), original)
        self.assertFalse((self.root.parent / '.atlas-permission-state').exists())

    def test_v1_policy_uses_direct_config_and_denies_shell(self):
        from opencode_permissions import (
            install_workdir_permission_policy, remove_workdir_permission_policy,
        )
        install_workdir_permission_policy(self.root, 1, allow_edit=False)
        target = self.root / 'opencode.json'
        config = json.loads(target.read_text(encoding='utf-8'))
        self.assertEqual(config['permission']['bash'], 'deny')
        self.assertEqual(config['permission']['edit']['*'], 'deny')
        self.assertEqual(config['permission']['code_mode'], 'deny')
        self.assertEqual(config['permission']['skill'], 'deny')
        self.assertEqual(config['permission']['mcp'], 'deny')
        self.assertEqual(config['permission']['application_atlas_*'], 'deny')
        self.assertFalse(config['tools']['mcp'])
        self.assertEqual(config['permission']['edit']['opencode.json'], 'deny')
        self.assertFalse(config['tools']['bash'])
        self.assertTrue(remove_workdir_permission_policy(self.root))
        self.assertFalse(target.exists())

    def test_version_detection_handles_opencode_v_prefix(self):
        from unittest.mock import patch
        from opencode_permissions import detect_opencode_major_version
        with patch('opencode_permissions.subprocess.run', return_value=SimpleNamespace(
                stdout='opencode v2.0.13\n', stderr='')):
            self.assertEqual(detect_opencode_major_version('opencode'), 2)
        with patch('opencode_permissions.subprocess.run', return_value=SimpleNamespace(
                stdout='opencode 1.18.31\n', stderr='')):
            self.assertEqual(detect_opencode_major_version('opencode'), 1)

    def test_permission_policy_rejects_a_symlinked_config(self):
        from opencode_permissions import (
            OpenCodePermissionError, install_workdir_permission_policy,
        )
        target = self.root / '.opencode' / 'opencode.json'
        target.parent.mkdir()
        target.symlink_to(self.root / 'outside.json')
        with self.assertRaises(OpenCodePermissionError):
            install_workdir_permission_policy(self.root, 2)

    def test_unmanaged_opencode_url_requires_explicit_trust_override(self):
        from opencode_runtime import OpenCodeRuntime
        runtime = OpenCodeRuntime(self.root.parent)
        with patch.dict(os.environ, {
                'ATLAS_OPENCODE_URL': 'http://127.0.0.1:65530',
                'ATLAS_ALLOW_UNMANAGED_OPENCODE': '',
        }, clear=False), self.assertRaisesRegex(RuntimeError, 'disabled by default'):
            runtime.ensure()


class AtlasCliTests(unittest.TestCase):
    class FakeApi:
        def __init__(self):
            self.posts = []
            self.project = {"id": "prj_demo", "name": "演示项目", "workspace": "/tmp/demo"}
            self.task = {
                "id": "tsk_demo", "title": "运行验证", "execution_status": "planned",
                "acceptance_status": "pending",
            }
            self.execution = {
                "id": "exe_demo", "engine": "opencode-cli", "status": "completed",
                "application_status": "not_applicable", "raw_state": {"evidence": {
                    "cli_run": {"summary": {"exitCode": 0, "timedOut": False},
                                "evidenceDirectory": "/tmp/evidence"}}},
            }

        def get(self, path):
            if path == "/api/projects":
                return [self.project]
            if path.endswith("/workspace"):
                return {"project": self.project, "tasks": [self.task], "executions": [self.execution]}
            if path.endswith("/harness/preflight"):
                return {"status": "passed"}
            if path.endswith("/executions/exe_demo"):
                return self.execution
            raise AssertionError(path)

        def post(self, path, body=None):
            self.posts.append((path, body))
            if path.endswith("/executions"):
                return self.execution
            if path.endswith("/cleanup"):
                return self.execution
            raise AssertionError(path)

    def test_terminal_entry_defaults_to_read_only_and_renders_chinese(self):
        api = self.FakeApi()
        output = []
        result = atlas_cli.run(
            atlas_cli.parser().parse_args(["--project", "prj_demo"]),
            api=api, output=output.append)
        self.assertEqual(result["project"]["id"], "prj_demo")
        self.assertFalse(api.posts)
        self.assertTrue(any("启动前检查: 通过" in line for line in output))
        self.assertTrue(any("只读模式" in line for line in output))

    def test_terminal_entry_requires_explicit_start_or_cleanup_for_mutations(self):
        api = self.FakeApi()
        output = []
        result = atlas_cli.run(
            atlas_cli.parser().parse_args(["--project", "prj_demo", "--task", "tsk_demo", "--start"]),
            api=api, output=output.append)
        self.assertEqual(result["id"], "exe_demo")
        self.assertEqual(api.posts[0][1], {"transport": "cli"})
        self.assertTrue(any('"exitCode": 0' in line for line in output))
        output.clear()
        atlas_cli.run(
            atlas_cli.parser().parse_args(["--project", "prj_demo", "--execution", "exe_demo", "--cleanup"]),
            api=api, output=output.append)
        self.assertTrue(api.posts[-1][0].endswith("/cleanup"))
        self.assertTrue(any("清理" in line for line in output))

    def test_terminal_entry_exposes_keyboard_slice_without_changing_api_contract(self):
        api = self.FakeApi()
        args = atlas_cli.parser().parse_args(["--interactive", "--project", "prj_demo"])
        with patch("atlas_cli._interactive", return_value=0) as interactive:
            result = atlas_cli.run(args, api=api)
        self.assertEqual(result, {})
        interactive.assert_called_once_with(api, args)

    def test_terminal_execution_summary_keeps_verification_transport_fields(self):
        summary = atlas_cli._execution_summary(self.FakeApi().execution, "zh")
        self.assertEqual(summary["transport"], "OpenCode CLI")
        self.assertEqual(summary["exitCode"], 0)
        self.assertFalse(summary["timedOut"])
        self.assertIsNone(summary["diagnosticCode"])
        self.assertEqual(summary["evidenceDirectory"], "/tmp/evidence")

    def test_terminal_status_labels_cover_acceptance_states(self):
        self.assertEqual(atlas_cli._status("passed", "zh"), "通过")
        self.assertEqual(atlas_cli._status("waived", "en"), "Waived")


class ModelSettingsTests(unittest.TestCase):
    """Provider configuration and credential handling for /api/settings/model."""

    def setUp(self):
        import atlas_model
        self.model = atlas_model
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.config = Path(self._tmp.name) / "model-config.json"
        self._env = patch.dict(os.environ, {
            "ATLAS_MODEL_CONFIG": str(self.config)}, clear=False)
        self._env.start()
        self.addCleanup(self._env.stop)
        self.addCleanup(lambda: os.environ.pop("ATLAS_MODEL_CONFIG", None))

    def saved(self):
        return json.loads(self.config.read_text(encoding="utf-8"))

    def test_credentials_are_write_only(self):
        provider = self.model.upsert_provider({
            "preset": "open-design", "api_key": "sk-secret-value-1234567890"})
        self.assertTrue(provider["has_key"])
        self.assertNotIn("api_key", provider)
        self.assertIn("\u2022\u2022\u2022\u2022", provider["key_masked"])

        blob = json.dumps(self.model.public_view(), ensure_ascii=False)
        self.assertNotIn("sk-secret-value-1234567890", blob)

    def test_saved_file_is_owner_only(self):
        self.model.upsert_provider({"preset": "deepseek", "api_key": "sk-abcdef123456"})
        self.assertEqual(self.config.stat().st_mode & 0o777, 0o600)

    def test_blank_key_keeps_stored_value_and_null_clears_it(self):
        self.model.upsert_provider({"preset": "openai", "api_key": "sk-original-123456"})
        self.model.upsert_provider({"preset": "openai", "base_url": "https://example.com/v1"})
        stored = self.saved()["providers"]["openai"]
        self.assertEqual(stored["api_key"], "sk-original-123456")
        self.assertEqual(stored["base_url"], "https://example.com/v1")

        self.model.upsert_provider({"preset": "openai", "api_key": None})
        self.assertEqual(self.saved()["providers"]["openai"]["api_key"], "")

    def test_base_url_must_be_absolute_http(self):
        for bad in ["not-a-url", "ftp://example.com", "file:///etc/passwd", ""]:
            with self.subTest(base_url=bad):
                with self.assertRaises(self.model.ModelConfigError):
                    self.model.upsert_provider({
                        "id": "custom", "name": "Custom", "api_key": "k",
                        "base_url": bad})

    def test_unknown_provider_is_reported_as_not_configured(self):
        with self.assertRaises(self.model.ModelConfigError) as ctx:
            self.model.resolve(provider="does-not-exist")
        self.assertEqual(ctx.exception.code, "not_configured")

    def test_missing_credential_is_reported(self):
        self.model.upsert_provider({"preset": "groq"})
        with self.assertRaises(self.model.ModelConfigError) as ctx:
            self.model.resolve(provider="groq")
        self.assertEqual(ctx.exception.code, "no_credential")

    def test_delete_requires_explicit_confirmation(self):
        self.model.upsert_provider({"preset": "mistral", "api_key": "k"})
        with self.assertRaises(self.model.ModelConfigError):
            self.model.delete_provider("mistral", "yes")
        self.assertTrue(self.model.load_config()["providers"]["mistral"])
        self.model.delete_provider(
            "mistral", self.model.DELETE_CONFIRMATION)
        self.assertNotIn("mistral", self.model.load_config()["providers"])

    def test_deleting_the_default_clears_the_default(self):
        self.model.upsert_provider({"preset": "xai", "api_key": "k", "models": ["grok-1"]})
        self.model.set_default("xai", "grok-1")
        self.model.delete_provider("xai", self.model.DELETE_CONFIRMATION)
        self.assertEqual(self.model.load_config()["default"],
                         {"provider": None, "model": None})

    def test_provider_error_messages_do_not_leak_the_credential(self):
        import urllib.error
        secret = "sk-super-secret-token-value"
        error = urllib.error.HTTPError(
            "https://api.example.com/v1/models", 401, "Unauthorized", {},
            io.BytesIO(b'{"error":"bad key "}'))
        mapped = self.model._provider_error(error)
        self.assertEqual(mapped.code, "unauthorized")
        self.assertNotIn(secret, str(mapped))

    def test_role_model_falls_back_to_the_default(self):
        self.model.upsert_provider({
            "preset": "open-design", "api_key": "k",
            "models": ["deepseek-v4.1-flash", "glm-5.3-flash"]})
        self.model.set_default("open-design", "deepseek-v4.1-flash")
        # No role configured: every task uses the default model.
        for role in ("adjudicator", "dedupe", "translate", "identity"):
            self.assertEqual(self.model.role_model(role), "")
            self.assertEqual(self.model.resolve(role=role)["model"],
                             "deepseek-v4.1-flash")

    def test_role_model_naming_a_served_model_is_honored(self):
        self.model.upsert_provider({
            "preset": "open-design", "api_key": "k",
            "models": ["deepseek-v4.1-flash", "glm-5.3-flash"]})
        self.model.set_default("open-design", "deepseek-v4.1-flash")
        with patch.dict(os.environ, {"ATLAS_ADJUDICATOR": "glm-5.3-flash"}):
            self.assertEqual(self.model.resolve(role="adjudicator")["model"],
                             "glm-5.3-flash")

    def test_role_model_the_provider_lacks_is_ignored(self):
        # A stale Go-era model name must not be sent to a provider that does
        # not serve it; the default model is used instead.
        self.model.upsert_provider({
            "preset": "open-design", "api_key": "k",
            "models": ["deepseek-v4.1-flash"]})
        self.model.set_default("open-design", "deepseek-v4.1-flash")
        with patch.dict(os.environ, {"ATLAS_ADJUDICATOR": "qwen3.8-flash"}):
            self.assertEqual(self.model.resolve(role="adjudicator")["model"],
                             "deepseek-v4.1-flash")

    def test_complete_text_falls_back_to_reasoning(self):
        # Some reasoning models return the answer in `reasoning` with an empty
        # `content`; the helper must not return an empty string.
        self.model.upsert_provider({
            "id": "r", "name": "R", "api_key": "k",
            "base_url": "https://api.example.com/v1", "models": ["m"]})
        payload = {"model": "m",
                   "choices": [{"message": {"content": "", "reasoning": " 42 "}}]}
        with patch.object(self.model, "_post_json",
                          lambda url, body, headers, timeout: payload):
            self.assertEqual(
                self.model.complete_text([{"role": "user", "content": "x"}],
                                         provider="r"),
                "42")

    def test_import_reads_credentials_from_the_sqlite_store(self):
        # OpenCode keeps recently added providers only in opencode.db, so an
        # importer reading auth.json alone silently misses them.
        root = Path(self._tmp.name)
        store = root / ".local/share/opencode"
        store.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(store / "opencode.db") as connection:
            connection.execute(
                "CREATE TABLE credential (integration_id TEXT, value TEXT)")
            connection.execute(
                "INSERT INTO credential VALUES (?, ?)",
                ("open-design", json.dumps({"key": "sk-from-db", "type": "api"})))
        with patch.object(Path, "home", return_value=root):
            result = self.model.import_from_opencode()
        self.assertIn("open-design", result["imported"])
        stored = self.saved()["providers"]["open-design"]
        self.assertEqual(stored["api_key"], "sk-from-db")
        self.assertEqual(stored["base_url"],
                         "https://amr-link.open-design.ai/v1")

    def test_http_error_mapping(self):
        import urllib.error
        cases = [
            (404, "bad_endpoint"),
            (429, "rate_limited"),
            (500, "provider_error"),
        ]
        for status, expected in cases:
            with self.subTest(status=status):
                error = urllib.error.HTTPError(
                    "https://api.example.com/v1/chat/completions", status, "", {},
                    io.BytesIO(b"upstream failure"))
                self.assertEqual(self.model._provider_error(error).code, expected)

    def test_model_unavailable_is_not_retryable(self):
        import urllib.error
        error = urllib.error.HTTPError(
            "https://api.example.com/v1/chat/completions", 400, "", {},
            io.BytesIO(b'{"error":{"message":"Model is unavailable"}}'))
        mapped = self.model._provider_error(error)
        self.assertEqual(mapped.code, "model_unavailable")

    def test_usage_omits_unknown_numbers_rather_than_guessing(self):
        self.model.upsert_provider({
            "id": "probe", "name": "Probe", "api_key": "k",
            "base_url": "https://api.example.com/v1", "models": ["m"]})
        payload = {
            "model": "m",
            "choices": [{"message": {"content": "hi"}, "finish_reason": "stop"}],
        }
        with patch.object(self.model, "_post_json",
                          lambda url, body, headers, timeout: payload):
            out = self.model.chat([{"role": "user", "content": "x"}], provider="probe")
        self.assertEqual(out["content"], "hi")
        self.assertIsNone(out["usage"]["total_tokens"])
        self.assertIsNone(out["usage"]["cost"])

    def test_tool_calls_are_normalized(self):
        payload = {
            "model": "m",
            "choices": [{
                "message": {
                    "content": "",
                    "tool_calls": [{
                        "id": "call_1", "type": "function",
                        "function": {"name": "search_atlas",
                                     "arguments": '{"query": "kanban"}'}}],
                },
                "finish_reason": "tool_calls",
            }],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        }
        self.model.upsert_provider({
            "id": "tools", "name": "Tools", "api_key": "k",
            "base_url": "https://api.example.com/v1", "models": ["m"]})
        with patch.object(self.model, "_post_json",
                          lambda url, body, headers, timeout: payload):
            out = self.model.chat(
                [{"role": "user", "content": "x"}],
                provider="tools",
                tools=[{"type": "function", "function": {
                    "name": "search_atlas", "parameters": {"type": "object"}}}])
        self.assertEqual(out["finish_reason"], "tool_calls")
        self.assertEqual(out["tool_calls"][0]["function"]["name"], "search_atlas")
        self.assertEqual(out["usage"]["total_tokens"], 15)

    def test_settings_routes_return_masked_views(self):
        handler = object.__new__(drafts_api.Handler)
        handler.headers = {'Host': 'localhost:5199'}
        handler.path = '/api/settings/model'
        captured = {}
        handler._json = lambda value, code=200: captured.update(
            {"value": value, "code": code}) or (value, code)
        body = {
            "preset": "open-design",
            "api_key": "sk-route-secret-abcdef123456",
        }
        handler._body = lambda: body
        handler._settings_model_post('/api/settings/model/providers')
        self.assertEqual(captured["code"], 201)
        self.assertNotIn("api_key", captured["value"])

        captured.clear()
        payload, code = handler.do_GET()
        self.assertEqual(code, 200)
        self.assertIn("providers", payload)
        self.assertIn("presets", payload)
        self.assertNotIn("sk-route-secret-abcdef123456",
                         json.dumps(payload, ensure_ascii=False))

    def test_settings_route_reports_config_errors_with_codes(self):
        handler = object.__new__(drafts_api.Handler)
        handler.headers = {'Host': 'localhost:5199'}
        handler._json = lambda value, code=200: {"value": value, "code": code}
        handler._body = lambda: {"preset": "bad preset id!!", "api_key": "k"}
        result = handler._settings_model_post('/api/settings/model/providers')
        self.assertEqual(result["code"], 400)
        self.assertEqual(result["value"]["code"], "invalid_request")


class AskHarnessTests(unittest.TestCase):
    """The read-only Ask harness: tool surface, bounding, and citation safety."""

    def setUp(self):
        import atlas_ask
        import atlas_tools
        self.ask = atlas_ask
        self.tools = atlas_tools
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self._env = patch.dict(os.environ, {
            "ATLAS_ASK_ROOT": str(Path(self._tmp.name) / "ask")}, clear=False)
        self._env.start()
        self.addCleanup(self._env.stop)
        self.addCleanup(lambda: os.environ.pop("ATLAS_ASK_ROOT", None))
        # Point the module-level root at the temp dir for this test.
        self._root = patch.object(
            self.ask, "ASK_ROOT", Path(self._tmp.name) / "ask")
        self._root.start()
        self.addCleanup(self._root.stop)

    # ---- tool surface ----

    def test_only_read_only_tools_are_exposed(self):
        names = set(self.tools.TOOL_FUNCTIONS)
        self.assertEqual(names, {
            "search_atlas", "get_leaf", "get_neighbors", "get_section_tree",
            "read_atlas_source", "get_atlas_source_manifest"})
        # No tool may write, shell out, or reach the network.
        for forbidden in ("write", "edit", "shell", "bash", "webfetch",
                          "websearch", "subagent", "delete", "promote"):
            self.assertNotIn(forbidden, names)

    def test_schemas_match_the_dispatch_table(self):
        declared = {schema["function"]["name"]
                    for schema in self.tools.TOOL_SCHEMAS}
        self.assertTrue(declared <= set(self.tools.TOOL_FUNCTIONS))
        for schema in self.tools.TOOL_SCHEMAS:
            self.assertIn("description", schema["function"])
            self.assertEqual(schema["function"]["parameters"]["type"], "object")

    def test_unknown_tool_is_refused_not_executed(self):
        result = self.tools.run_tool("os.system", {"cmd": "rm -rf /"})
        self.assertEqual(result["code"], "unknown_tool")

    def test_bad_arguments_are_reported_as_data(self):
        self.assertEqual(
            self.tools.run_tool("get_leaf", {"nope": 1})["code"], "bad_argument")
        self.assertEqual(
            self.tools.run_tool("get_leaf", "not-a-dict")["code"], "bad_argument")

    def test_arguments_are_rejected_when_missing_required_field(self):
        result = self.tools.run_tool("search_atlas", {})
        self.assertEqual(result["code"], "bad_argument")

    def test_limit_is_clamped(self):
        # A model asking for more than the cap gets the cap, never more.
        self.assertEqual(self.tools._limit(9999, 5, self.tools.MAX_SEARCH_K),
                         self.tools.MAX_SEARCH_K)
        self.assertEqual(self.tools._limit(-5, 5, self.tools.MAX_SEARCH_K), 1)
        self.assertEqual(self.tools._limit("abc", 5, self.tools.MAX_SEARCH_K), 5)

    def test_slug_is_bounded(self):
        with self.assertRaises(self.tools.ToolError):
            self.tools._slug("")
        with self.assertRaises(self.tools.ToolError):
            self.tools._slug("x" * 500)

    # ---- conversation lifecycle ----

    def test_thread_round_trip_and_delete_confirmation(self):
        thread = self.ask.create_thread("hello")
        self.assertTrue(thread["id"].startswith("ask_"))
        self.assertEqual(self.ask.read_thread(thread["id"])["messages"], [])
        self.assertEqual(len(self.ask.list_threads()), 1)

        with self.assertRaises(self.ask.AskError):
            self.ask.delete_thread(thread["id"], "yes")
        self.assertTrue(self.ask.read_thread(thread["id"]))

        self.ask.delete_thread(thread["id"], self.ask.DELETE_CONFIRMATION)
        with self.assertRaises(self.ask.AskError) as ctx:
            self.ask.read_thread(thread["id"])
        self.assertEqual(ctx.exception.code, "not_found")

    def test_invalid_thread_id_is_not_found(self):
        for bad in ("", "nope", "../escape", "ask_short"):
            with self.subTest(thread_id=bad):
                with self.assertRaises(self.ask.AskError) as ctx:
                    self.ask.read_thread(bad)
                self.assertEqual(ctx.exception.code, "not_found")

    def test_thread_id_cannot_escape_the_root(self):
        with self.assertRaises(self.ask.AskError):
            self.ask._path("ask_" + "0" * 32 + "/../../etc/passwd")

    def test_empty_question_is_rejected_before_spawning(self):
        thread = self.ask.create_thread()
        for bad in ("", "   ", None, 123):
            with self.subTest(content=bad):
                with self.assertRaises(self.ask.AskError) as ctx:
                    self.ask.start_question(thread["id"], bad)
                self.assertEqual(ctx.exception.code, "invalid_request")
        # Nothing was recorded and no worker is running.
        self.assertEqual(self.ask.read_thread(thread["id"])["messages"], [])
        self.assertFalse(self.ask.read_thread(thread["id"])["running"])

    def test_over_long_question_is_rejected(self):
        thread = self.ask.create_thread()
        with self.assertRaises(self.ask.AskError):
            self.ask.start_question(thread["id"], "x" * (self.ask.MAX_QUESTION_CHARS + 1))

    # ---- citation safety ----

    def test_citations_only_include_slugs_a_tool_surfaced(self):
        available = {"kanban-task-board": {"slug": "kanban-task-board",
                                           "name_zh": "看板任务板"}}
        answer = "看板 [kanban-task-board] 和 [invented-type] 不同。"
        cited = self.ask._citations(answer, available)
        self.assertEqual([item["slug"] for item in cited], ["kanban-task-board"])
        # A fabricated slug must never become a link.
        self.assertNotIn("invented-type", [item["slug"] for item in cited])

    def test_citations_are_deduplicated_and_bounded(self):
        available = {f"type-{i}": {"slug": f"type-{i}", "name_zh": ""}
                     for i in range(100)}
        answer = " ".join(f"[type-{i}]" for i in range(100))
        cited = self.ask._citations(answer, available)
        self.assertEqual(len(cited), 20)
        self.assertEqual(len({item["slug"] for item in cited}), len(cited))

    def test_no_answer_yields_no_citations(self):
        self.assertEqual(self.ask._citations("", {"a": {"slug": "a"}}), [])

    def test_type_collection_records_names_from_search_results(self):
        payload = {"count": 1, "results": [
            {"slug": "kanban-task-board", "name_zh": "看板任务板",
             "related": ["task-management-application"]}]}
        found = self.ask._collect_types(payload, {})
        self.assertEqual(found["kanban-task-board"]["name_zh"], "看板任务板")
        self.assertIn("task-management-application", found)

    # ---- tool output redaction ----

    def test_tool_output_is_redacted_before_storage(self):
        payload = {"note": "Authorization: Bearer sk-secret-value-1234567890"}
        cleaned = self.ask._redact_payload(payload)
        self.assertNotIn("sk-secret-value-1234567890", json.dumps(cleaned))

    def test_tool_result_text_is_fenced_as_data(self):
        fenced = self.ask._fence({"a": 1})
        self.assertTrue(fenced.startswith("<atlas-data>"))
        self.assertTrue(fenced.endswith("</atlas-data>"))
        # Oversized output is truncated rather than pasted whole.
        big = self.ask._fence({"blob": "x" * 60_000})
        self.assertLess(len(big), 30_000)

    def test_summarize_reports_errors_compactly(self):
        self.assertIn("boom", self.ask._summarize("get_leaf", {"error": "boom"}))

    # ---- bounding ----

    def test_run_limits_are_finite_and_sane(self):
        self.assertGreaterEqual(self.ask.MAX_TURNS, 1)
        self.assertLessEqual(self.ask.MAX_TURNS, 20)
        self.assertGreater(self.ask.MAX_SECONDS, 0)
        self.assertGreater(self.ask.MAX_TOKENS, 0)

    def test_worker_records_a_failed_message_instead_of_hanging(self):
        thread = self.ask.create_thread()
        # Simulate a model failure mid-run.
        with patch.object(self.ask.atlas_model, "chat",
                          side_effect=self.ask.atlas_model.ModelConfigError(
                              "no provider", code="not_configured")):
            self.ask.start_question(thread["id"], "hello")
            for _ in range(100):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)
        final = self.ask.read_thread(thread["id"])
        self.assertFalse(final["running"])
        last = final["messages"][-1]
        self.assertEqual(last["role"], "assistant")
        self.assertEqual(last["status"], "provider_error")
        # The failure is visible and did not leave the thread stuck.
        self.assertTrue(last["content"] or last["error"])

    def test_concurrent_question_on_one_thread_is_refused(self):
        thread = self.ask.create_thread()
        started = threading.Event()
        release = threading.Event()

        def slow_chat(*_args, **_kwargs):
            started.set()
            release.wait(timeout=10)
            return {"content": "done", "tool_calls": [], "usage": {}, "raw": {}}

        with patch.object(self.ask.atlas_model, "chat", side_effect=slow_chat):
            self.ask.start_question(thread["id"], "first")
            self.assertTrue(started.wait(timeout=5))
            try:
                with self.assertRaises(self.ask.AskError) as ctx:
                    self.ask.start_question(thread["id"], "second")
                self.assertEqual(ctx.exception.code, "busy")
                self.assertEqual(ctx.exception.status, 409)
            finally:
                release.set()
            for _ in range(100):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)

    def test_turn_limit_stops_a_tool_loop_that_never_answers(self):
        thread = self.ask.create_thread()
        calls = {"n": 0}

        def always_calls_tool(*_args, **_kwargs):
            calls["n"] += 1
            return {
                "content": "",
                "tool_calls": [{
                    "id": f"call_{calls['n']}", "type": "function",
                    "function": {"name": "get_section_tree",
                                 "arguments": '{"depth": 1}'}}],
                "usage": {"total_tokens": 1},
                "model": "m", "provider": "p",
                "raw": {"choices": [{"message": {
                    "content": "",
                    "tool_calls": [{
                        "id": f"call_{calls['n']}", "type": "function",
                        "function": {"name": "get_section_tree",
                                     "arguments": '{"depth": 1}'}}]}}]},
            }

        with patch.object(self.ask.atlas_model, "chat", side_effect=always_calls_tool), \
             patch.object(self.ask.atlas_tools, "run_tool",
                          return_value={"count": 29, "sections": []}):
            self.ask.start_question(thread["id"], "loop forever")
            for _ in range(200):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)

        final = self.ask.read_thread(thread["id"])
        self.assertFalse(final["running"])
        last = final["messages"][-1]
        # It must stop at the turn ceiling rather than looping forever.
        self.assertEqual(last["status"], "turn_limit")
        self.assertEqual(calls["n"], self.ask.MAX_TURNS)

    def test_step_records_carry_a_readable_summary(self):
        thread = self.ask.create_thread()

        def one_tool_then_answer(*_args, **_kwargs):
            if not getattr(one_tool_then_answer, "done", False):
                one_tool_then_answer.done = True
                return {
                    "content": "",
                    "tool_calls": [{"id": "c1", "type": "function",
                                    "function": {"name": "search_atlas",
                                                 "arguments": '{"query": "x"}'}}],
                    "usage": {}, "model": "m", "provider": "p",
                    "raw": {"choices": [{"message": {
                        "content": "", "tool_calls": [{"id": "c1", "type": "function",
                        "function": {"name": "search_atlas",
                                     "arguments": '{"query": "x"}'}}]}}]},
                }
            return {"content": "答案 [kanban-task-board]", "tool_calls": [],
                    "usage": {}, "model": "m", "provider": "p", "raw": {}}

        fake_result = {"count": 1, "results": [
            {"slug": "kanban-task-board", "name_zh": "看板任务板"}]}
        with patch.object(self.ask.atlas_model, "chat", side_effect=one_tool_then_answer), \
             patch.object(self.ask.atlas_tools, "run_tool", return_value=fake_result):
            self.ask.start_question(thread["id"], "q")
            for _ in range(200):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)

        last = self.ask.read_thread(thread["id"])["messages"][-1]
        self.assertEqual(last["status"], "completed")
        self.assertEqual(len(last["steps"]), 1)
        self.assertEqual(last["steps"][0]["tool"], "search_atlas")
        self.assertTrue(last["steps"][0]["summary"])
        self.assertEqual([c["slug"] for c in last["citations"]],
                         ["kanban-task-board"])

    # ---- usage honesty ----

    def test_usage_is_null_when_the_provider_reports_nothing(self):
        thread = self.ask.create_thread()
        with patch.object(self.ask.atlas_model, "chat",
                          return_value={"content": "hi", "tool_calls": [],
                                        "usage": {}, "model": "m",
                                        "provider": "p", "raw": {}}):
            self.ask.start_question(thread["id"], "q")
            for _ in range(100):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)
        usage = self.ask.read_thread(thread["id"])["messages"][-1]["usage"]
        self.assertIsNone(usage["total_tokens"])
        self.assertIsNone(usage["cost"])

    def test_usage_accumulates_across_turns(self):
        thread = self.ask.create_thread()
        turns = {"n": 0}

        def two_turns(*_args, **_kwargs):
            turns["n"] += 1
            if turns["n"] == 1:
                return {"content": "", "tool_calls": [
                    {"id": "c1", "type": "function",
                     "function": {"name": "get_section_tree", "arguments": "{}"}}],
                    "usage": {"total_tokens": 100, "prompt_tokens": 80,
                              "completion_tokens": 20},
                    "model": "m", "provider": "p",
                    "raw": {"choices": [{"message": {
                        "content": "", "tool_calls": [{"id": "c1", "type": "function",
                        "function": {"name": "get_section_tree",
                                     "arguments": "{}"}}]}}]}}
            return {"content": "done", "tool_calls": [],
                    "usage": {"total_tokens": 50, "prompt_tokens": 40,
                              "completion_tokens": 10},
                    "model": "m", "provider": "p", "raw": {}}

        with patch.object(self.ask.atlas_model, "chat", side_effect=two_turns), \
             patch.object(self.ask.atlas_tools, "run_tool",
                          return_value={"count": 1, "sections": []}):
            self.ask.start_question(thread["id"], "q")
            for _ in range(200):
                if not self.ask.read_thread(thread["id"])["running"]:
                    break
                time.sleep(0.05)
        usage = self.ask.read_thread(thread["id"])["messages"][-1]["usage"]
        self.assertEqual(usage["total_tokens"], 150)
        self.assertIsNone(usage["cost"])


if __name__=='__main__':unittest.main()
