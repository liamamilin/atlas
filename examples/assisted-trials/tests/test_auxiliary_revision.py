import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from revise_with_opencode import merge_revision, review_identity, verify_revision, write_candidate
from produce_with_opencode import MODEL, CHECKS, checkpoint, manifest_files
from template_factory.store import digest
from template_factory.store import FactoryStore, FactoryError
from template_factory.budget import BudgetLedger


class AuxiliaryRevisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.store = FactoryStore(self.root / 'factory', self.root)
        self.now = [1000.0]
        self.ledger = BudgetLedger(self.store, campaign_id='test', clock=lambda: self.now[0])
        self.req = {'schema': 'atlas.auxiliary-revision-request.v1', 'campaign_id': 'test',
                    'phase': 'auxiliary-revision-test', 'identity': 'home-care', 'model': 'opencode-go/deepseek-v4.1-flash',
                    'max_cli_calls': 6, 'window_seconds': 86400, 'authorization_sha256': 'abc', 'parent': {'digest': 'parent'}}

    def test_durable_cap_and_clock_across_new_instances_jobs_and_failures(self):
        ledger = self.ledger
        ledger.register_auxiliary_revision(self.req['phase'], 'home-care', self.req)
        self.assertEqual(ledger.snapshot()['segments'], [])
        ledger.begin_segment('G1')
        original = copy.deepcopy(ledger.snapshot()['segments'])
        for i in range(6):
            row = ledger.reserve('home-care', self.req['phase'], requested_model=self.req['model'], job_id='job-' + str(i))
            ledger.finish(row['id'], 'failed', outcome='fixture failure')
            self.now[0] += 1
            ledger = BudgetLedger(self.store, campaign_id='test', clock=lambda: self.now[0])
            ledger.register_auxiliary_revision(self.req['phase'], 'home-care', self.req)
        with self.assertRaisesRegex(FactoryError, 'limit exhausted'):
            ledger.reserve('home-care', self.req['phase'], requested_model=self.req['model'])
        segments = ledger.snapshot()['segments']
        g1 = next(s for s in segments if s['phase'] == 'G1')
        self.assertEqual((g1['started'], g1['deadline']), (original[0]['started'], original[0]['deadline']))
        auxiliary = next(s for s in segments if s['phase'] == self.req['phase'])
        self.assertEqual(auxiliary['deadline'], 87400)
        self.assertEqual(ledger.snapshot()['cli_sessions_used'], 6)

    def test_request_identity_model_and_window_cannot_drift(self):
        self.ledger.register_auxiliary_revision(self.req['phase'], 'home-care', self.req)
        for key, value in [('parent', {'digest': 'other'}), ('max_cli_calls', 7), ('window_seconds', 86401)]:
            changed = {**self.req, key: value}
            with self.assertRaises(FactoryError):
                self.ledger.register_auxiliary_revision(self.req['phase'], 'home-care', changed)
        with self.assertRaises(FactoryError):
            self.ledger.reserve('other', self.req['phase'], requested_model=self.req['model'])
        with self.assertRaises(FactoryError):
            self.ledger.reserve('home-care', self.req['phase'], requested_model='other')
        self.assertEqual(self.ledger.snapshot()['cli_sessions_used'], 0)

    def test_deadline_does_not_reset(self):
        self.ledger.register_auxiliary_revision(self.req['phase'], 'home-care', self.req)
        self.ledger.begin_segment(self.req['phase'])
        self.now[0] = 87401
        self.ledger.register_auxiliary_revision(self.req['phase'], 'home-care', self.req)
        with self.assertRaisesRegex(FactoryError, 'deadline exhausted'):
            self.ledger.reserve('home-care', self.req['phase'], requested_model=self.req['model'])

    def test_old_pass_does_not_bind_new_content(self):
        base = review_identity({'parent': 'old'}, {'arch': 'old'}, {'probe.py': 'old'}, {}, {})
        self.assertNotEqual(base, review_identity({'parent': 'old'}, {'arch': 'new'}, {'probe.py': 'old'}, {}, {}))
        self.assertNotEqual(base, review_identity({'parent': 'new'}, {'arch': 'old'}, {'probe.py': 'old'}, {}, {}))
        with self.assertRaisesRegex(ValueError, 'outside'):
            merge_revision({}, {'authored_updates': {'observations': []}}, {})


    def make_real_shape_revision(self):
        folder = self.root / 'home-care-r1'
        folder.mkdir()
        upstream = self.root / 'upstream'
        upstream.mkdir()
        (upstream / 'code.py').write_text('fixed source\n')
        (upstream / 'LICENSE').write_text('MIT\n')
        snapshot = {'repository': 'https://github.com/example/fixed', 'files': manifest_files(upstream),
                    'local_root': str(upstream), 'license': {'spdx_id': 'MIT'}, 'license_files': ['LICENSE']}
        parent = {'name': 'Home', 'audience': 'Local', 'objective': 'Old', 'inference': 'Design', 'arch': 'Old design',
                  'workflow': ['Create'], 'acceptance': ['Check'], 'features': ['one', 'two', 'three'],
                  'goals': ['a', 'b', 'c'], 'gaps': ['not_run'], 'repo_name': 'example/fixed', 'license': 'MIT', 'license_path': 'LICENSE',
                  'observations': [['code_observation', 'code.py', 1, 1, 'Fixed code'], ['documentation', 'LICENSE', 1, 1, 'MIT']]}
        files = {'probe.py': 'print("probe")\n', 'README.md': 'not_run'}
        raw = {'authored_updates': {'objective': 'New'}, 'acceptance_files': files}
        authored, files = merge_revision(parent, raw, snapshot)
        req = self.req
        (self.root / 'REQUEST.json').write_text(json.dumps(req))
        materials = folder / 'materials'
        write_candidate(materials / 'candidate', parent, files)
        from shutil import copytree
        copytree(upstream, materials / 'upstream')
        scene = {'id': 'scene', 'revision': 1}
        identity = review_identity(req, authored, files, snapshot, scene)
        review = {'input_digest': identity, 'verdict': 'pass', 'checks': {k: True for k in CHECKS}, 'issues': [],
                  'observations': [{'index': i, 'verdict': 'accepted', 'reason': 'checked source'} for i in range(2)]}
        class Delivered:
            calls = 0
            def run(inner, directory, *args, **kwargs):
                inner.calls += 1
                result = raw if directory.name == 'author' else review
                data = json.dumps({'text': json.dumps(result)}).encode()
                (directory / 'original-response.json').write_bytes(data)
                (directory / 'events.jsonl').write_text('')
                (directory / 'cli-summary.json').write_text(json.dumps({'delivery_status': 'delivered', 'requested_model': MODEL,
                    'session_id': directory.name, 'original_response_sha256': hashlib.sha256(data).hexdigest()}))
                return result
        cli = Delivered()
        checkpoint(folder / 'calls/author', {'request': req}, 'author', cli, {}, materials, b'leaf')
        reviewed = folder / 'review-materials'
        write_candidate(reviewed / 'candidate', authored, files)
        copytree(upstream, reviewed / 'upstream')
        checkpoint(folder / 'calls/review', {'input_digest': identity}, 'review', cli, {}, reviewed, b'leaf')
        write_candidate(folder, authored, files)
        (folder / 'scenario.json').write_text(json.dumps(scene))
        production = {'review_input_digest': identity, 'revision_request_digest': digest(req), 'parent': req['parent'],
                      'source_snapshot_digest': digest(snapshot), 'stages': {'author': 'author', 'review': 'review'},
                      'sessions': {'author': 'author', 'review': 'review'}, 'review_result_digest': digest(review)}
        return folder, production, authored, snapshot, cli

    def test_full_revision_delivery_reload_and_old_pass_rejection(self):
        folder, production, authored, snapshot, cli = self.make_real_shape_revision()
        verify_revision(folder, production, authored, snapshot)
        # Reload all successful checkpoints without generating again.
        for role in ('author', 'review'):
            stage = folder / 'calls' / role
            checkpoint(stage, json.loads((stage / 'input.json').read_text()), role, cli, {},
                       folder / ('materials' if role == 'author' else 'review-materials'), b'leaf')
        self.assertEqual(cli.calls, 2)
        verify_revision(folder, json.loads(json.dumps(production)), json.loads(json.dumps(authored)), snapshot)
        changed = {**production, 'review_input_digest': 'old-pass'}
        with self.assertRaisesRegex(ValueError, 'provenance differs'):
            verify_revision(folder, changed, authored, snapshot)
        (folder / 'acceptance/probe.py').write_text('changed')
        with self.assertRaises(ValueError):
            verify_revision(folder, production, authored, snapshot)

    def test_failed_review_cannot_freeze_export_even_with_valid_receipt_hashes(self):
        folder, production, authored, snapshot, cli = self.make_real_shape_revision()
        stage = folder / 'calls/review'
        result = json.loads((stage / 'RESULT.json').read_text())
        result.update(verdict='needs_changes', issues=['core mismatch'])
        (stage / 'RESULT.json').write_text(json.dumps(result))
        binding = json.loads((stage / 'BINDING.json').read_text())
        (stage / 'DELIVERED.json').write_text(json.dumps({'binding_digest': digest(binding), 'result_digest': digest(result)}))
        production['review_result_digest'] = digest(result)
        (folder / 'source-snapshot.json').write_text(json.dumps(snapshot))
        (folder / 'case-record.json').write_text('{}')
        (folder / 'definition.json').write_text(json.dumps({'production': production}))
        from export_trial import export_trial
        with self.assertRaisesRegex(ValueError, 'did not pass'):
            export_trial(folder, folder / 'packages', 'trial')
        self.assertFalse((folder / 'packages').exists())


if __name__ == '__main__':
    unittest.main()
