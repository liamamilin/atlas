"""Synthetic binding and verified-inventory preflight fixtures only."""
import importlib.util
import inspect
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
import sys
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))

SPEC = importlib.util.spec_from_file_location("docker_acceptance_binding_fixture", HERE / "docker_acceptance.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class BindingContractFixtures(unittest.TestCase):
    def setUp(self):
        self.files = {"app/serve.py": "a" * 64, "app/store.py": "b" * 64}
        self.cli = {
            "phase": "P0",
            "template_digest": "1" * 64,
            "suite_digest": "2" * 64,
            "case_basis_digest": "3" * 64,
        }
        self.binding = {
            "target_kind": "generated_application",
            "selected_phase": self.cli["phase"],
            "artifact_digest": self.cli["template_digest"],
            "suite_digest": self.cli["suite_digest"],
            "case_basis_digest": self.cli["case_basis_digest"],
            "application_digest": runner.atlas_digest(self.files),
            "artifact_id": "art_demo",
            "selected_case_ids": ["case-a"],
            "scenario_id": "scn_fixture",
            "scenario_revision": 2,
        }

    def test_matching_generated_target_and_verified_inventory_pass(self):
        self.assertEqual(self.binding["application_digest"], runner.validate_runtime_binding(
            self.binding, **self.cli, application_files=self.files))

    def test_wrong_target_kind_phase_or_cli_digest_fails_before_docker(self):
        for key, value in [("target_kind", "template"), ("selected_phase", "P1"),
                           ("artifact_digest", "f" * 64), ("suite_digest", "e" * 64),
                           ("case_basis_digest", "d" * 64)]:
            with self.subTest(key=key):
                bad = {**self.binding, key: value}
                with self.assertRaises(ValueError):
                    runner.validate_runtime_binding(bad, **self.cli, application_files=self.files)

    def test_wrong_verified_bundle_inventory_fails_before_docker(self):
        wrong_bundle_files = {**self.files, "app/store.py": "c" * 64}
        with self.assertRaisesRegex(ValueError, "inventory digest does not match"):
            runner.validate_runtime_binding(self.binding, **self.cli, application_files=wrong_bundle_files)

    def test_verified_bundle_binding_check_precedes_first_docker_call(self):
        source = inspect.getsource(runner.main)
        verify = source.index("application_files=verified_application_files")
        first_docker = source.index('docker("info", timeout=10)')
        self.assertLess(verify, first_docker)


if __name__ == "__main__":
    unittest.main()
