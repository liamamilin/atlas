"""Real export/reuse checks; no service, model or application execution."""

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "examples/assisted-trials"))
from export_trial import export_trial  # noqa: E402

FIXTURE = ROOT / "docs/template-factory/assisted-trials-2026-10-21/budget"


class ExportReuseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.inputs = self.root / "inputs"
        self.inputs.mkdir()
        for name in ("definition.json", "case-record.json"):
            shutil.copyfile(FIXTURE / name, self.inputs / name)
        shutil.copytree(
            FIXTURE / "acceptance",
            self.inputs / "acceptance",
            ignore=shutil.ignore_patterns("__pycache__"),
        )
        self.output = self.root / "packages"

    def archives(self):
        return {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in self.output.glob("*.zip")
        }

    def test_same_input_reuses_without_rewriting(self):
        first = export_trial(self.inputs, self.output, "budget-test")
        hashes = self.archives()
        again = export_trial(self.inputs, self.output, "budget-test", reuse=True)
        self.assertTrue(again["reused"])
        self.assertEqual(first["template_digest"], again["template_digest"])
        self.assertEqual(hashes, self.archives())
        self.assertIn("probe.py", first["provenance"]["acceptance_inputs"])

    def test_file_content_change_requires_new_version_and_preserves_archives(self):
        export_trial(self.inputs, self.output, "budget-test")
        before = self.archives()
        p = self.inputs / "acceptance/probe.py"
        p.write_bytes(p.read_bytes() + b"\n# changed acceptance\n")
        with self.assertRaisesRegex(ValueError, "acceptance files changed"):
            export_trial(self.inputs, self.output, "budget-test", reuse=True)
        self.assertEqual(before, self.archives())

    def test_add_remove_and_rename_are_input_changes(self):
        export_trial(self.inputs, self.output, "budget-test")
        path = self.inputs / "acceptance/probe.py"
        original = path.read_bytes()
        for mutation in ("add", "remove", "rename"):
            with self.subTest(mutation=mutation):
                path.write_bytes(original)
                extra = self.inputs / "acceptance/new.py"
                extra.unlink(missing_ok=True)
                if mutation == "add":
                    extra.write_text("# new assertion\n")
                elif mutation == "remove":
                    path.unlink()
                else:
                    path.rename(extra)
                with self.assertRaisesRegex(ValueError, "acceptance files changed"):
                    export_trial(self.inputs, self.output, "budget-test", reuse=True)

    def test_legacy_receipt_uses_original_frozen_acceptance_bytes(self):
        self.output.mkdir()
        for name in (
            "EXPORT_RECEIPT.json",
            "template-snapshot.zip",
            "development-package.zip",
        ):
            shutil.copyfile(FIXTURE / "packages" / name, self.output / name)
        receipt = json.loads((self.output / "EXPORT_RECEIPT.json").read_text())
        self.assertNotIn("acceptance_inputs", receipt["provenance"])
        hashes = self.archives()
        self.assertTrue(
            export_trial(self.inputs, self.output, "budget-trial", reuse=True)["reused"]
        )
        p = self.inputs / "acceptance/probe.py"
        p.write_bytes(p.read_bytes() + b"\n# changed legacy acceptance\n")
        with self.assertRaisesRegex(ValueError, "acceptance files changed"):
            export_trial(self.inputs, self.output, "budget-trial", reuse=True)
        self.assertEqual(hashes, self.archives())

    def test_model_provenance_travels_with_package_without_runtime_certification(self):
        definition = json.loads((self.inputs / "definition.json").read_text())
        production = {"schema": "atlas.auxiliary-model-production.v1", "mode": "opencode-cli-go",
                      "model": "opencode-go/deepseek-v4.1-flash", "review_status": "passed",
                      "controlled_opencode_calls_added": 3, "application_runtime": "not_run",
                      "upstream_runtime": "not_run", "strict_acceptance": False}
        definition["production"] = production
        (self.inputs / "definition.json").write_text(json.dumps(definition))
        receipt = export_trial(self.inputs, self.output, "model-test")
        self.assertEqual(receipt["controlled_opencode_calls_added"], 3)
        self.assertFalse(receipt["provenance"]["official_publication"])
        self.assertEqual(receipt["provenance"]["independent_evidence_review"], "passed_auxiliary_static")
        import zipfile
        with zipfile.ZipFile(self.output / "template-snapshot.zip") as archive:
            self.assertEqual(json.loads(archive.read("source/inputs/model-production.json")), production)
        again = export_trial(self.inputs, self.output, "model-test", reuse=True)
        self.assertTrue(again["reused"])


if __name__ == "__main__":
    unittest.main()
