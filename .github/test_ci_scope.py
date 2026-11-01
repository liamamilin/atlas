import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch
import subprocess


spec = importlib.util.spec_from_file_location("ci_scope", Path(__file__).with_name("ci_scope.py"))
scope = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scope)


class ScopeTests(unittest.TestCase):
    def test_reference_only_and_reading_evidence_take_targeted_checks(self):
        self.assertEqual(scope.classify([
            "examples/assisted-trials/product_reference_profile.py",
            "application-atlas-production-pack/template_factory/product_reference.py",
            "docs/template-factory/product-reference-pilot-2026-10-22/REPORT.md",
        ]), "reference")

    def test_shared_ledger_executor_web_and_dependencies_keep_full_gate(self):
        for path in [
            "application-atlas-production-pack/template_factory/budget.py",
            "application-atlas-production-pack/template_factory/full_auxiliary.py",
            "application-atlas-production-pack/template_factory/api.py",
            "application-atlas-production-pack/opencode_runtime.py",
            "atlas-web/src/components/product-references.tsx",
            "requirements.txt", "atlas-web/package-lock.json", ".github/workflows/checks.yml",
        ]:
            with self.subTest(path=path):
                self.assertEqual(scope.classify(["examples/assisted-trials/product_reference_profile.py", path]), "full")

    def test_executable_evidence_and_unknown_paths_are_not_document_shortcuts(self):
        for path in [
            "docs/template-factory/product-reference-pilot-2026-10-22/probe.py",
            "docs/template-factory/product-reference-pilot-2026-10-22/source.zip",
            "docs/template-factory/other/contract.json",
            "application-atlas-production-pack/template_factory/new_unknown.py",
        ]:
            self.assertEqual(scope.classify([path]), "full")

    def test_missing_diff_or_initial_push_defaults_to_full(self):
        self.assertEqual(scope.classify([]), "full")
        self.assertEqual(scope.changed_paths("0" * 40, "a" * 40), [])
        self.assertEqual(scope.changed_paths("--anything", "a" * 40), [])

    def test_git_diff_preserves_all_paths_and_disables_rename_collapsing(self):
        old = "application-atlas-production-pack/template_factory/budget.py"
        new = "examples/assisted-trials/product_reference_profile.py"
        with patch.object(scope.subprocess, "run", return_value=subprocess.CompletedProcess(
            args=[], returncode=0, stdout=(old + "\0" + new + "\0").encode(),
        )) as run:
            paths = scope.changed_paths("a" * 40, "b" * 40)
        self.assertEqual(paths, [old, new])
        self.assertIn("--no-renames", run.call_args.args[0])
        self.assertEqual(scope.classify(paths), "full")

    def test_git_failure_cannot_silently_skip_full_checks(self):
        with patch.object(scope.subprocess, "run", side_effect=subprocess.CalledProcessError(128, "git")):
            self.assertEqual(scope.classify(scope.changed_paths("a" * 40, "b" * 40)), "full")


if __name__ == "__main__":
    unittest.main()
