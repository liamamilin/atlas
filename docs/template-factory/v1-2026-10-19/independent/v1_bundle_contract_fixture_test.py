"""Synthetic end-to-end preflight for the official V1 runtime bundle shape."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.artifacts import tree_manifest
from template_factory.delivery import prepare_application

SPEC = importlib.util.spec_from_file_location("docker_acceptance_v1_bundle_fixture", HERE / "docker_acceptance.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class OfficialV1BundleFixtures(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.bundle = self.root / "submission"
        self.bundle.mkdir()
        self.archive = self.bundle / "application.zip"
        metadata = {
            "schema": "atlas.application-delivery.v1",
            "root": ".",
            "files": ["app/serve.py", "app/store.py"],
            "runtime": {
                "profile": "python-web", "install": [], "build": [],
                "start": ["python3", "app/serve.py", "--host", "0.0.0.0", "--port", "8000", "--data-dir", "/state/app-data"],
                "port": 8000, "readiness_path": "/api/health",
            },
        }
        self.sources = {
            "app/serve.py": b"# synthetic fixture\n",
            "app/store.py": b"# synthetic store\n",
        }
        with zipfile.ZipFile(self.archive, "w") as zf:
            zf.writestr("delivery.json", json.dumps(metadata))
            for name, data in self.sources.items():
                zf.writestr(name, data)
        self.expected_archive_sha256 = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        normalized = self.root / "official-prepared"
        receipt = prepare_application(self.archive.read_bytes(), normalized)
        (self.bundle / "delivery-receipt.json").write_text(json.dumps(receipt), encoding="utf-8")
        app_copy = self.bundle / "application"
        app_copy.mkdir()
        for name in receipt["files"]:
            target = app_copy / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((normalized / name).read_bytes())
        self.destination = self.root / "verified-extraction"
        self.receipt = receipt
        self.inventory = tree_manifest(normalized)
        self.binding = {
            "target_kind": "generated_application", "artifact_id": "art-fixture",
            "artifact_digest": "1" * 64, "application_digest": runner.atlas_digest(self.inventory),
            "suite_digest": "2" * 64, "selected_phase": "P0",
            "selected_case_ids": ["save-and-open"], "scenario_id": "scn_fixture",
            "scenario_revision": 2, "case_basis_digest": "3" * 64,
        }

    def tearDown(self):
        self.temp.cleanup()

    def test_official_prepare_receipt_copy_and_formal_binding_match(self):
        info = runner.unpack_verified_bundle(self.bundle, self.destination, self.expected_archive_sha256)
        self.assertEqual(info["delivery"], self.receipt)
        self.assertEqual(info["application_inventory"], self.inventory)
        self.assertEqual(info["application_digest"], self.binding["application_digest"])
        self.assertEqual(runner.validate_runtime_binding(
            self.binding, phase="P0", template_digest="1" * 64,
            suite_digest="2" * 64, case_basis_digest="3" * 64,
            application_files=info["application_inventory"]), self.binding["application_digest"])
        parsed = runner.read_delivery(info["delivery"], info["app_root"])
        self.assertEqual(parsed[1], self.receipt["runtime"]["start"])
        self.assertEqual(parsed[2], 8000)

    def test_archive_pin_and_binding_mismatches_fail_preflight(self):
        with self.assertRaisesRegex(ValueError, "pinned runtime input"):
            runner.unpack_verified_bundle(self.bundle, self.root / "bad-pin", "f" * 64)
        for field, value in [("target_kind", "template"), ("selected_phase", "P1"),
                             ("artifact_digest", "f" * 64), ("suite_digest", "e" * 64),
                             ("case_basis_digest", "d" * 64),
                             ("application_digest", "c" * 64)]:
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    runner.validate_runtime_binding(
                        {**self.binding, field: value}, phase="P0", template_digest="1" * 64,
                        suite_digest="2" * 64, case_basis_digest="3" * 64,
                        application_files=self.inventory)

    def test_receipt_must_equal_official_prepare_application_output(self):
        receipt_path = self.bundle / "delivery-receipt.json"
        receipt_path.write_text(json.dumps({**self.receipt, "normalizations": ["forged"]}), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs from official prepare_application"):
            runner.unpack_verified_bundle(self.bundle, self.root / "wrong-receipt", self.expected_archive_sha256)


if __name__ == "__main__":
    unittest.main()
