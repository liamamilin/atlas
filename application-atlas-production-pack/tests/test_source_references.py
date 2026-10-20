"""Shared pure source-reference rules used before cognition and at import."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.source_references import (
    feature_source_reference_report,
    validate_feature_source_references,
)
from template_factory.cognition import _source_projection_material
from template_factory.store import FactoryError


class FeatureSourceReferenceTests(unittest.TestCase):
    def test_accepted_documentation_sources_keep_fixed_location_version_and_digest(self):
        fact_digest = "f" * 64
        cases = [{"observations": [
            {"evidence_id": "doc-url-only", "kind": "documentation", "location": {
                "url": "https://example.org/guide", "material_version": "2026-10",
                "content_digest": "a" * 64,
            }},
            {"evidence_id": "doc-source-path", "kind": "documentation", "location": {
                "url": "https://example.org/readme", "material_version": "v2",
                "content_digest": "b" * 64, "source_path": "README.md",
            }},
        ]}]
        research = {"sources": [
            {"id": "S02", "name": "doc-url-only", "url": "https://example.org/guide",
             "version": "2026-10", "facts": "Pinned documentation fact."},
            {"id": "S03", "name": "doc-source-path", "url": "https://example.org/readme",
             "version": "v2", "facts": "Another pinned documentation fact."},
        ]}
        snapshot = {"case_facts_view": {"view_digest": fact_digest},
                    "scenario": {"id": "scenario-fixture", "revision": 1,
                                 "objective": "Fixed test scenario."}}
        manifest, matrix = _source_projection_material(
            research, cases, snapshot,
            {"features": [{"id": "F01", "sources": ["S02", "S03"]}]},
        )
        by_id = {row["id"]: row for row in manifest["sources"]}
        self.assertEqual(by_id["S02"]["kind"], "documentation")
        self.assertEqual(by_id["S02"]["source_path"], "https://example.org/guide")
        self.assertEqual(by_id["S02"]["version"], "2026-10")
        self.assertEqual(by_id["S02"]["content_digest"], "a" * 64)
        self.assertEqual(by_id["S03"]["source_path"], "README.md")
        self.assertEqual(by_id["S03"]["source_url"], "https://example.org/readme")
        self.assertEqual(by_id["S03"]["kind"], "documentation")
        self.assertEqual(matrix["features"][0]["source_ids"], ["S02", "S03"])

    def test_empty_sources_are_legal_and_report_binds_inventory(self):
        spec = {"features": [{"id": "F01", "sources": []}]}
        report = validate_feature_source_references(
            spec, ["S01", {"id": "S02"}], binding={"facts_view_digest": "a" * 64}
        )
        self.assertTrue(report["valid"])
        self.assertEqual(report["available_source_ids"], ["S01", "S02"])
        self.assertEqual(report["features"][0]["source_ids"], [])
        self.assertTrue(report["binding_digest"])

    def test_report_identifies_all_features_and_missing_and_duplicate_refs(self):
        report = feature_source_reference_report(
            {"features": [
                {"id": "F01", "sources": ["S02", "S17"]},
                {"id": "F02", "sources": ["S08", "S08"]},
            ]},
            ["S01", "S02"],
        )
        self.assertFalse(report["valid"])
        self.assertEqual([row["feature_id"] for row in report["features"]], ["F01", "F02"])
        self.assertEqual(report["features"][0]["missing_source_ids"], ["S17"])
        self.assertIn("source IDs must be unique", report["features"][1]["errors"])
        with self.assertRaisesRegex(FactoryError, "feature sources; report="):
            validate_feature_source_references(
                {"features": [{"id": "F01", "sources": ["S17"]}]}, ["S01"]
            )


if __name__ == "__main__":
    unittest.main()
