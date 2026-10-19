"""Runner records must reflect actual test-runner counts, including skips."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.v1_checks import observed_counts


class CheckRecordTests(unittest.TestCase):
    def test_missing_runner_counts_are_unknown_not_zero_or_success(self):
        self.assertEqual(observed_counts("backend_tests", "Process failed before tests"), (None, 0))
        self.assertEqual(observed_counts("factory_e2e", "No tests found"), (None, 0))

    def test_counts_preserve_optional_skips_and_read_strict_json_summary(self):
        self.assertEqual(observed_counts("backend_tests", "Ran 501 tests in 42.1s\nOK (skipped=8)"), (501, 8))
        self.assertEqual(observed_counts("backend_tests", "Ran 530 tests in 38.415s\nFAILED (errors=7, skipped=8)"), (530, 8))
        self.assertEqual(observed_counts("docker_integration", 'Ran 20 tests in 50.0s\nOK\n{"status":"passed","tests_run":20,"skipped":0}'), (20, 0))
        self.assertEqual(observed_counts("web_unit", "# tests 9\n# pass 9\n# skipped 0"), (9, 0))
        self.assertEqual(observed_counts("factory_e2e", "25 passed (12.3s)"), (25, 0))
