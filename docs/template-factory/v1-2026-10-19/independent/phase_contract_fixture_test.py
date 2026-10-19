"""Synthetic regression fixtures for the independent phase assertion contract.

These cases exercise only runner bookkeeping. They are not application evidence.
"""
import importlib.util
from pathlib import Path
import unittest


RUNNER = Path(__file__).with_name("docker_acceptance.py")
SPEC = importlib.util.spec_from_file_location("docker_acceptance_fixture", RUNNER)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class PhaseContractFixtures(unittest.TestCase):
    def setUp(self):
        self.cases = [
            "save bookmark with title and URL",
            "assign category then move it to another category",
            "find by category and by keyword",
            "open and verify exact original URL using a controlled local fixture",
            "restart the same app container with the same persistent state and verify records remain",
            "reject malformed/non-http(s) URL without creating a record",
            "run concurrent independent saves and verify every acknowledged write is present exactly once",
        ]

    def test_initial_requires_every_case_except_restart_proof(self):
        initial_required = self.cases[:-3] + self.cases[-2:]
        passed = [{"id": item, "passed": True} for item in initial_required]
        self.assertEqual(([], []), runner.validate_phase_assertions(passed, initial_required, "initial"))
        restart_precheck = passed + [{"id": self.cases[4], "passed": True}]
        missing, failed = runner.validate_phase_assertions(restart_precheck, initial_required, "initial")
        self.assertFalse(missing)
        self.assertEqual([self.cases[4]], failed)

    def test_after_restart_requires_full_replay_and_state_case(self):
        passed = [{"id": item, "passed": True} for item in self.cases[:-1]]
        missing, failed = runner.validate_phase_assertions(passed, self.cases, "after-restart")
        self.assertEqual([self.cases[-1]], missing)
        self.assertFalse(failed)

    def test_combined_evidence_cannot_pass_restart_case_from_initial_phase(self):
        initial = {"assertions": [{"id": item, "passed": True} for item in self.cases]}
        after = {"assertions": [{"id": item, "passed": True} for item in self.cases if item != self.cases[4]]}
        self.assertEqual([self.cases[4]], runner.validate_combined_assertions(
            [("initial", initial), ("after-restart", after)], self.cases))

    def test_combined_evidence_requires_every_frozen_case_pass(self):
        initial = {"assertions": [{"id": item, "passed": True} for item in self.cases if item != self.cases[4]]}
        after = {"assertions": [{"id": item, "passed": True} for item in self.cases]}
        self.assertEqual([], runner.validate_combined_assertions(
            [("initial", initial), ("after-restart", after)], self.cases))


if __name__ == "__main__":
    unittest.main()
