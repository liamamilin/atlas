"""Focused regression for the prepared R8 acceptance programs (fixtures only)."""
from __future__ import annotations

import ast
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[2]
SOURCE_ACCEPTANCE = ROOT / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/actual-frozen-review/job_b01427592b164863aab5bedf7b3863bb/source/acceptance"
PREPARED = ROOT / "docs/template-factory/g1-r8-contract-convergence-2026-10-20/prepared-programs/acceptance"
def load_module(name: str, path: Path):
    # Evidence archives are immutable. Execute the exact bytes in memory rather
    # than letting importlib create __pycache__ inside a frozen source directory.
    module = ModuleType(name)
    module.__file__ = str(path)
    sys.modules[name] = module
    exec(compile(path.read_bytes(), str(path), "exec"), module.__dict__)
    return module


previous_common = sys.modules.get("common")
sys.modules["common"] = load_module("r8_frozen_common", SOURCE_ACCEPTANCE / "common.py")
try:
    p0 = load_module("r8_prepared_p0_library", PREPARED / "p0_library.py")
    p1 = load_module("r8_prepared_p1_maturity", PREPARED / "p1_maturity.py")
finally:
    if previous_common is None:
        sys.modules.pop("common", None)
    else:
        sys.modules["common"] = previous_common


class A13LinkTests(unittest.TestCase):
    url = "https://Example.invalid/path?a=1&b=Two#frag"
    rid = "r-17"

    def test_program_loader_never_writes_into_source_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "evidence.py"
            source.write_text("VALUE = 17\n")
            loaded = load_module("r8_isolation_probe", source)
            self.assertEqual(loaded.VALUE, 17)
            self.assertEqual(list(Path(temp).iterdir()), [source])

    def check(self, row, *, other="", expected=True):
        body = f"<html>{other}<table>{row}</table></html>"
        actual, _ = p1._a13_target_link(body, self.rid, self.url)
        self.assertEqual(actual, expected)

    def row(self, href=None, target="_blank", rel="noopener"):
        href = self.url if href is None else href
        return (f'<tr data-testid="record-row" data-record-id="{self.rid}">'
                f'<td><a data-testid="record-open-link" href="{href}" '
                f'target="{target}" rel="{rel}">open</a></td></tr>')

    def test_original_url_and_decoded_html_entity_pass_without_go(self):
        encoded = self.url.replace("&", "&amp;")
        self.check(self.row(encoded))

    def test_go_elsewhere_does_not_substitute_for_target_link(self):
        self.check(self.row(None).replace(self.url, "/wrong"), other="<!-- /go/r-17 -->", expected=False)
        self.check('<tr data-testid="record-row" data-record-id="other"><a href="' + self.url + '"></a></tr>',
                   other="/go/r-17", expected=False)

    def test_wrong_target_href_and_rel_each_fail(self):
        self.check(self.row("https://example.invalid/path?a=1&b=Two#frag"), expected=False)
        self.check(self.row(target="_self"), expected=False)
        self.check(self.row(rel="noreferrer"), expected=False)

    def test_other_row_url_and_duplicate_or_missing_target_links_fail(self):
        self.check(self.row("/wrong") + self.row().replace(self.rid, "other"), expected=False)
        self.check(self.row() + self.row(), expected=False)
        self.check('<tr data-testid="record-row" data-record-id="other"></tr>', expected=False)

    def test_implicitly_closed_target_row_cannot_adopt_next_rows_anchor(self):
        malformed = (f'<tr data-testid="record-row" data-record-id="{self.rid}"><td>target'
                     f'<tr data-testid="record-row" data-record-id="other"><td>'
                     f'<a data-testid="record-open-link" href="{self.url}" target="_blank" '
                     f'rel="noopener">other row</a></td></tr>')
        self.check(malformed, expected=False)

    def test_target_record_row_inside_nested_layout_table_is_valid(self):
        nested_layout = (f'<table><tr><td>layout wrapper<table>'
                        f'<tr data-testid="record-row" data-record-id="{self.rid}"><td>'
                        f'<a data-testid="record-open-link" href="{self.url}" target="_blank" '
                        f'rel="noopener">target row</a></td></tr></table></td></tr></table>')
        self.check(nested_layout)

    def test_different_nested_record_row_cannot_supply_target_anchor(self):
        nested = (f'<tr data-testid="record-row" data-record-id="{self.rid}"><td>target row'
                  f'<table><tr data-testid="record-row" data-record-id="other"><td>'
                  f'<a data-testid="record-open-link" href="{self.url}" target="_blank" '
                  f'rel="noopener">other row</a></td></tr></table></td></tr>')
        self.check(nested, expected=False)


sys.path.insert(0, str(ROOT / "application-atlas-production-pack/tests/fixtures"))
from factory_contract_convergence_programs import FakeA03Client, FakeProc

class A03SeparationTests(unittest.TestCase):
    def run_a03(self, *, missing_fresh=None, missing_html=None, bad_default=False, reject_new=False, start_error=None, source="/app", cleanup_error=None, flags=True):
        base = FakeA03Client(p0, bad_default=bad_default, reject_new=reject_new)
        fresh = FakeA03Client(p0, fresh=True, missing_fresh=missing_fresh, missing_html=missing_html)
        proc = FakeProc(source)
        calls = []
        original_http, original_launch, original_stop = p0.common.HttpClient, p0.common.launch_app, p0.common.stop_app
        def http(url):
            return fresh if str(url).startswith('http://fresh') else base
        def launch(root, data, port, fresh=False):
            calls.append((root, data, fresh))
            if start_error:
                raise RuntimeError(start_error)
            return proc
        def stop(item):
            if cleanup_error:
                raise RuntimeError(cleanup_error)
            item.stopped = True
        p0.common.HttpClient, p0.common.launch_app, p0.common.stop_app = http, launch, stop
        try:
            args = type('Args', (), {'app_root':'/app' if flags else None, 'data_dir':'/scratch' if flags else None,
                                     'base_url':'http://base'})()
            recorder = p0.common.Recorder('A03')
            p0._case_a03(args, recorder)
            return recorder, calls, base, fresh, proc
        finally:
            p0.common.HttpClient, p0.common.launch_app, p0.common.stop_app = original_http, original_launch, original_stop

    def test_existing_instance_may_have_removed_presets_but_fresh_checks_all_four(self):
        recorder, calls, base, fresh, proc = self.run_a03()
        self.assertEqual(calls, [('/app', '/scratch', True)])
        self.assertTrue(base.closed)
        self.assertTrue(fresh.closed)
        self.assertTrue(proc.stopped)
        self.assertFalse([a for a in recorder.assertions if not a['passed']], recorder.assertions)
        self.assertTrue(any(a['id'] == 'a03-fresh-html-preset-4' for a in recorder.assertions))

    def test_fresh_missing_preset_and_start_source_cleanup_errors_fail(self):
        recorder, *_ = self.run_a03(missing_fresh=p0.common.PRESET_CATEGORIES[-1])
        self.assertTrue(any(a['id'] == 'a03-fresh-api-preset-4' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(missing_html=p0.common.PRESET_CATEGORIES[-1])
        self.assertTrue(any(a['id'] == 'a03-fresh-html-preset-4' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(bad_default=True)
        self.assertTrue(any(a['id'] == 'a03-default-category' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(reject_new=True)
        self.assertTrue(any(a['id'] == 'a03-newcat-row' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(start_error='no start')
        self.assertTrue(any(a['id'] == 'a03-fresh-start' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(source='/other')
        self.assertTrue(any(a['id'] == 'a03-fresh-owned-source' and not a['passed'] for a in recorder.assertions))
        recorder, *_ = self.run_a03(cleanup_error='cannot stop')
        self.assertTrue(any(a['id'] == 'a03-fresh-cleanup' and not a['passed'] for a in recorder.assertions))

    def test_missing_arguments_fail_before_any_target_or_fresh_launch(self):
        recorder, calls, *_ = self.run_a03(flags=False)
        self.assertEqual(calls, [])
        self.assertTrue(any(a['id'] == 'a03-fresh-required-flags' and not a['passed'] for a in recorder.assertions))

    def test_a03_cli_without_required_runner_arguments_exits_nonzero(self):
        original = p0.common.launch_app
        calls = []
        p0.common.launch_app = lambda *args, **kwargs: calls.append((args, kwargs))
        try:
            result = p0.main(["--case", "A03", "--base-url", "http://127.0.0.1:8000"])
        finally:
            p0.common.launch_app = original
        self.assertEqual(result, 1)
        self.assertEqual(calls, [])


class R8ScopeTests(unittest.TestCase):
    def test_four_prepared_files_only_and_five_reuse_digests_match_baseline(self):
        self.assertEqual({path.name for path in PREPARED.iterdir() if path.is_file()},
                         {"p0_library.py", "p1_maturity.py", "README.md", "runner.json"})
        reuse = {
            "common.py": "7f0d7d28d8336bdde3da267795e24d13e430f05e53063ee01ed5611236325d37",
            "p0_organize.py": "93ae82c74946811fac3b1dd213cc077cf89acc6ecfb45e64ec2830e3482b7f60",
            "p0_find_open.py": "342e38d2298cf48e22fb97d76e080ce4a67c3c10a942502c5ef205954878d667",
            "p0_recovery.py": "372c75aa2944a10cc5146859dc0bacd0e03111defe7c8aa75ece2d28ec45aff3",
            "requirements.txt": "f1fc18b605a1eea93892d319d09122d91033a48dfd4b913f8f262a4dc8633deb",
        }
        for filename, expected in reuse.items():
            actual = hashlib.sha256((SOURCE_ACCEPTANCE / filename).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, filename)
        before = json.loads((SOURCE_ACCEPTANCE / "runner.json").read_text())
        after = json.loads((PREPARED / "runner.json").read_text())
        for case_id in before["cases"]:
            if case_id == "A03":
                continue
            self.assertEqual(after["cases"][case_id], before["cases"][case_id], case_id)
        self.assertEqual(after["cases"]["A03"]["args"][-4:],
                         ["--app-root", "{app_root}", "--data-dir", "{data_dir}"])

    def test_untouched_case_implementations_match_frozen_source(self):
        for filename, names in {
            "p0_library.py": ("_case_a01", "_case_a02", "_case_a11_base", "_case_a11"),
            "p1_maturity.py": ("_case_a14", "_case_a15"),
        }.items():
            before_text = (SOURCE_ACCEPTANCE / filename).read_text()
            after_text = (PREPARED / filename).read_text()
            before = {node.name: ast.get_source_segment(before_text, node)
                      for node in ast.walk(ast.parse(before_text))
                      if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
            after = {node.name: ast.get_source_segment(after_text, node)
                     for node in ast.walk(ast.parse(after_text))
                     if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}
            for name in names:
                self.assertEqual(after[name], before[name], f"{filename}:{name}")


if __name__ == "__main__":
    unittest.main()
