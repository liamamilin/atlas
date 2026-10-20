"""R7 program behavior against controlled positive/mutant HTTP fixtures, not G1."""
import ast
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = Path(__file__).resolve().parents[2]
DOC = REPO / 'docs/template-factory/g1-r7-acceptance-alignment-2026-10-20'
SUITE = DOC / 'prepared-programs/acceptance'
OLD = DOC.parent / 'g1-r6-source-alignment-2026-10-20/candidate-attempt-1-not-frozen/acceptance'
APP = Path(__file__).resolve().parent / 'fixtures/r7_bookmark'


def load(name):
    sys.path.insert(0, str(SUITE))
    spec = importlib.util.spec_from_file_location('r7_' + name, SUITE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class R7AcceptancePrograms(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.library = load('p0_library')
        self.common = self.library.common

    def run_case(self, case, mutant='', missing_flags=False, app_root=None):
        with mock.patch.dict(os.environ, {'ATLAS_R7_FIXTURE_MUTANT': mutant}):
            proc = self.common.launch_app(str(APP), self.temp.name + '/base', 0, fresh=True)
            try:
                script = 'p0_find_open.py' if case in ('A07', 'A08') else 'p0_library.py'
                args = [sys.executable, str(SUITE / script), '--case', case, '--base-url', proc.base_url]
                if case in ('A01', 'A11') and not missing_flags:
                    args += ['--app-root', str(app_root or APP), '--data-dir', self.temp.name + '/scratch']
                result = subprocess.run(args, capture_output=True, text=True, timeout=60)
                value = json.loads(result.stdout)
                evidence_dir = os.environ.get('ATLAS_R7_EVIDENCE_DIR')
                if evidence_dir:
                    dest = Path(evidence_dir) / (self._testMethodName + '-' + case)
                    dest.mkdir(parents=True, exist_ok=True)
                    (dest / 'result.json').write_text(result.stdout)
                    (dest / 'stderr.txt').write_text(result.stderr)
                    (dest / 'invocation.json').write_text(json.dumps({
                        'argv': args, 'mutant': mutant, 'exit_code': result.returncode,
                        'evidence_kind': 'controlled fixture only; NOT real P0 or G1',
                    }, indent=2) + '\n')
                self.assertEqual(value['case_id'], case)
                self.assertEqual(value['schema'], 'atlas.acceptance-result.v1')
                return result, value
            finally:
                self.common.stop_app(proc)
                self.assertIsNotNone(proc.poll())

    def assert_outcome(self, case, mutant='', passed=True, **kwargs):
        result, value = self.run_case(case, mutant, **kwargs)
        self.assertEqual(value['status'], 'passed' if passed else 'failed', result.stderr)
        self.assertEqual(result.returncode == 0, passed, result.stderr)
        return value

    def test_a02_positive_and_existing_negatives(self):
        value = self.assert_outcome('A02')
        ids = {a['id'] for a in value['assertions']}
        self.assertIn('a02-json-boundary-readback', ids)
        self.assertIn('a02-relative-count', ids)
        self.assertIn('a02-json-illegal-hostname-code', ids)

    def test_a02_json_reject_single_label_mutant(self):
        self.assert_outcome('A02', 'reject-json-single-label', passed=False)

    def test_a07_correct_three_fields(self):
        self.assert_outcome('A07')

    def test_a07_reject_url_path_search_mutant(self):
        value = self.assert_outcome('A07', 'url-path', passed=False)
        for transport in ('json', 'html'):
            self.assertTrue(any(not a['passed'] and 'url-path' in a['id'] and transport in a['id'] for a in value['assertions']))

    def test_a07_reject_url_query_search_mutant(self):
        value = self.assert_outcome('A07', 'url-query', passed=False)
        for transport in ('json', 'html'):
            self.assertTrue(any(not a['passed'] and 'url-query' in a['id'] and transport in a['id'] for a in value['assertions']))

    def test_a07_reject_category_search_mutant(self):
        value = self.assert_outcome('A07', 'category-name', passed=False)
        for transport in ('json', 'html'):
            self.assertTrue(any(not a['passed'] and 'category-name' in a['id'] and transport in a['id'] for a in value['assertions']))

    def test_a07_reject_always_empty(self):
        self.assert_outcome('A07', 'always-empty', passed=False)

    def test_a11_fresh_empty_and_presets(self):
        value = self.assert_outcome('A11')
        ids = {a['id'] for a in value['assertions']}
        self.assertIn('a11-fresh-process-stopped', ids)
        self.assertIn('a11-fresh-including-trash-empty', ids)
        self.assertTrue(any(i.startswith('a11-base-') for i in ids))

    def test_a11_seeded_record_fails(self):
        self.assert_outcome('A11', 'seeded-record', passed=False)

    def test_a11_missing_preset_fails(self):
        self.assert_outcome('A11', 'missing-preset', passed=False)

    def test_a11_missing_empty_ui_fails(self):
        self.assert_outcome('A11', 'missing-empty-ui', passed=False)

    def test_a11_missing_flags_emits_own_failure(self):
        self.assert_outcome('A11', passed=False, missing_flags=True)

    def test_a11_missing_script_fails(self):
        self.assert_outcome('A11', passed=False, app_root=Path(self.temp.name))

    def test_a11_nonexistent_app_root_emits_own_failure(self):
        self.assert_outcome('A11', passed=False, app_root=Path(self.temp.name) / 'nonexistent')

    def test_a11_start_failure_emits_own_failure(self):
        bad = Path(self.temp.name) / 'bad/app'
        bad.mkdir(parents=True)
        (bad / 'serve.py').write_text('raise RuntimeError("controlled start failure")\n')
        self.assert_outcome('A11', passed=False, app_root=bad.parent)

    def test_a11_cleanup_failure_cannot_pass(self):
        with contextlib.redirect_stderr(io.StringIO()):
            proc = self.common.launch_app(str(APP), self.temp.name + '/cleanup-base', 0, fresh=True)
            try:
                args = self.common.parse_case_args(['--case', 'A11', '--base-url', proc.base_url, '--app-root', str(APP), '--data-dir', self.temp.name + '/cleanup-fresh'])
                stop = self.common.stop_app

                def fail_after_stop(owned):
                    stop(owned)
                    raise RuntimeError('controlled cleanup failure')

                recorder = self.common.Recorder('A11')
                with mock.patch.object(self.common, 'stop_app', side_effect=fail_after_stop):
                    self.library._case_a11(args, recorder)
                self.assertFalse(recorder.passed)
                self.assertTrue(any(a['id'] == 'a11-fresh-cleanup' and not a['passed'] for a in recorder.assertions))
            finally:
                self.common.stop_app(proc)

    def test_a01_a03_a08_preserved_and_behave(self):
        for case in ('A01', 'A03', 'A08'):
            with self.subTest(case=case):
                self.assert_outcome(case)

    def test_unchanged_functions_and_five_original_bytes(self):
        for filename, names in [('p0_library.py', ['_case_a01', '_case_a03']), ('p0_find_open.py', ['_case_a08'])]:
            before = {n.name: ast.dump(n) for n in ast.parse((OLD / filename).read_text()).body if isinstance(n, ast.FunctionDef)}
            after = {n.name: ast.dump(n) for n in ast.parse((SUITE / filename).read_text()).body if isinstance(n, ast.FunctionDef)}
            for name in names:
                self.assertEqual(before[name], after[name])
        for name in ('common.py', 'p0_organize.py', 'p0_recovery.py', 'p1_maturity.py', 'requirements.txt'):
            self.assertEqual((OLD / name).read_bytes(), (SUITE / name).read_bytes())
        before, after = [json.loads((folder / 'runner.json').read_text()) for folder in (OLD, SUITE)]
        self.assertEqual(after['cases']['A11']['args'], ['--case', '{case_id}', '--base-url', '{base_url}', '--app-root', '{app_root}', '--data-dir', '{data_dir}'])
        after['cases']['A11'] = before['cases']['A11']
        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
