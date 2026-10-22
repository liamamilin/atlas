"""Draft reading/export never confers production, source, or runtime approval."""
import base64
import hashlib
import io
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
import zipfile

from template_factory.api import dispatch
from template_factory.store import FactoryError
from test_product_reference import make_reference


class ReferencePreviewTests(unittest.TestCase):
    def setUp(self):
        self.store = SimpleNamespace(pack=Path(__file__).resolve().parents[1])

    def test_real_design_examples_integrity_and_honest_state(self):
        result, code = dispatch("GET", "/api/factory/product-reference-examples", store=self.store)
        self.assertEqual(code, 200)
        self.assertEqual(len(result["items"]), 3)
        for item in result["items"]:
            detail, _ = dispatch("GET", "/api/factory/product-reference-examples", "key=" + item["key"], store=self.store)
            self.assertEqual(hashlib.sha256(detail["markdown"].encode()).hexdigest(), item["sha256"])
            self.assertEqual(detail["independent_review"], "not_run")
            self.assertEqual(detail["application_runtime"], "not_run")
        with self.assertRaises(FactoryError):
            dispatch("GET", "/api/factory/product-reference-examples", "key=../../secrets", store=self.store)

    def test_preview_and_download_are_distinct_from_development_package(self):
        body = {"reference": make_reference(), "scope_id": "p0"}
        result, _ = dispatch("POST", "/api/factory/product-references/preview", body=body, store=self.store)
        self.assertEqual(result["artifact_kind"], "product-reference-preview")
        self.assertEqual(result["status"]["source_verification"], "not_run")
        self.assertEqual(result["selection"]["action_ids"], ["save"])
        self.assertIn("bulk-archive", result["selection"]["deferred_action_ids"])
        downloaded, _ = dispatch("POST", "/api/factory/product-references/export-preview", body=body, store=self.store)
        data = base64.b64decode(downloaded["archive_base64"])
        self.assertEqual(hashlib.sha256(data).hexdigest(), downloaded["sha256"])
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            names = set(archive.namelist())
            self.assertNotIn("probe.py", names)
            self.assertNotIn("HANDOFF.md", names)
            self.assertNotIn(".atlas-blueprint.json", names)
            manifest = json.loads(archive.read("PREVIEW_MANIFEST.json"))
            for name, expected in manifest["files"].items():
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), expected)
            self.assertEqual(manifest["status"]["independent_review"], "not_run")
            self.assertEqual(manifest["selection"]["action_ids"], ["save"])

    def test_invalid_draft_cannot_export(self):
        spec = make_reference()
        spec["journeys"][0]["steps"][0]["action_id"] = "missing"
        with self.assertRaises(FactoryError) as error:
            dispatch("POST", "/api/factory/product-references/export-preview", body={"reference": spec}, store=self.store)
        self.assertEqual(error.exception.code, "invalid_product_reference")

    def test_status_cannot_be_injected_in_content(self):
        spec = make_reference()
        spec["runtime_status"] = "passed"
        with self.assertRaises(FactoryError):
            dispatch("POST", "/api/factory/product-references/preview", body={"reference": spec}, store=self.store)


if __name__ == "__main__":
    unittest.main()
