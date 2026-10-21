"""Pinned auxiliary navigation, evidence honesty and file confinement."""
import hashlib
import json
import shutil
import unittest
from unittest.mock import patch

import test_blueprints as fixtures
from template_factory.api import dispatch
from template_factory.artifacts import archive_tree
from template_factory.assisted_catalog import asset_path
from template_factory.blueprints import freeze_blueprint, import_blueprint
from template_factory.store import FactoryError


class AssistedCatalogTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.BlueprintTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.store = self.fixture.store
        self.root = self.fixture.root
        shutil.copyfile(fixtures.SAMPLE.parents[3] / "application-atlas-production-pack/mvp_apps.json", self.fixture.pack / "mvp_apps.json")
        self.case = {"case_id": "case:example", "revision": 1, "digest": "a" * 64,
                     "app_id": "app:example", "source_snapshots": []}
        mock = patch("template_factory.cases.CaseLibrary.get_case", return_value=self.case)
        mock.start()
        self.addCleanup(mock.stop)
        freeze_blueprint(self.fixture.source, self.root / "freeze", {
            "origin": "assisted-trial", "case_ref": {k: self.case[k] for k in ("case_id", "revision", "digest")}})
        archive_tree(self.root / "freeze", self.root / "freeze.zip")
        self.artifact = import_blueprint(self.store, (self.root / "freeze.zip").read_bytes())
        self.file = self.root / "examples/demo.md"
        self.file.parent.mkdir(exist_ok=True)
        self.file.write_text("# Core journey passed, service availability not checked\n")
        self.row = {"key": "demo", "artifact_id": self.artifact["id"], "artifact_digest": self.artifact["digest"],
                    "runtime": {"status": "core_verified", "scope": "Core journeys only"},
                    "files": {k: {"path": "examples/demo.md", "sha256": hashlib.sha256(self.file.read_bytes()).hexdigest()}
                              for k in ("development", "guide", "source", "evidence")}}
        self.registry = self.root / "examples/assisted-trials/CATALOG.json"
        self.registry.parent.mkdir(exist_ok=True)
        self.save()

    def save(self):
        self.registry.write_text(json.dumps({"schema": "atlas.assisted-catalog.v1", "items": [self.row]}))

    def get(self, query=""):
        return dispatch("GET", "/api/factory/assisted-templates", query, store=self.store)[0]

    def test_historical_evidence_never_becomes_online_or_strict_acceptance(self):
        before = self.store.artifacts()
        with patch("subprocess.run", side_effect=AssertionError("read must not execute anything")):
            result = self.get()
        self.assertEqual(result["counts"], {"total": 1, "core_verified": 1, "not_run": 0, "usable": 1, "needs_revision": 0})
        item = result["items"][0]
        self.assertEqual(item["runtime"]["online_status"], "not_checked")
        self.assertFalse(item["runtime"]["strict_acceptance"])
        self.assertEqual(self.store.artifacts(), before)
        self.assertEqual(dispatch("GET", "/api/factory/artifacts", "published=1", store=self.store)[0], [])

    def test_leaf_scenario_case_and_revision_filters(self):
        item = self.get()["items"][0]
        self.assertEqual(self.get("leaf=" + item["leaf"])["counts"]["total"], 1)
        self.assertEqual(self.get("scenario_id=" + item["scenario"]["id"])["counts"]["total"], 1)
        self.assertEqual(self.get("case_id=case:example&case_revision=1")["counts"]["total"], 1)
        for query in ("leaf=other", "scenario_id=other", "case_id=other", "case_id=case:example&case_revision=2"):
            self.assertEqual(self.get(query)["items"], [])

    def test_changed_evidence_is_not_verified_or_downloadable(self):
        self.file.write_text("changed")
        item = self.get()["items"][0]
        self.assertEqual(item["runtime"]["status"], "evidence_unavailable")
        self.assertFalse(item["files"]["source"]["available"])
        with self.assertRaises(FactoryError) as caught:
            dispatch("GET", f"/api/factory/assisted-templates/{self.artifact['id']}/files/source", store=self.store)
        self.assertEqual(caught.exception.code, "assisted_asset_changed")

    def test_version_mismatch_or_non_assisted_artifact_is_not_listed(self):
        self.row["artifact_digest"] = "b" * 64
        self.save()
        self.assertEqual(self.get()["items"], [])
        self.assertEqual(self.get()["unavailable"][0]["reason"], "revision_conflict")

    def test_non_assisted_artifact_cannot_borrow_auxiliary_evidence(self):
        value = {**self.artifact, "provenance": {"origin": "imported-blueprint"}}
        with patch.object(self.store, "artifacts", return_value=[value]):
            self.assertEqual(self.get()["items"], [])

    def test_model_review_is_displayed_separately_from_runtime_and_publication(self):
        production = {"mode": "opencode-cli-go", "model": "opencode-go/deepseek-v4.1-flash",
                      "review_status": "passed", "review_input_digest": "e" * 64}
        value = {**self.artifact, "provenance": {**self.artifact["provenance"],
                 "imported_snapshot": {"provenance": {"model_production": production}}}}
        self.row["runtime"] = {"status": "not_run", "scope": "No application run"}
        self.save()
        with patch.object(self.store, "artifacts", return_value=[value]):
            item = self.get()["items"][0]
        self.assertEqual(item["production"], production)
        self.assertEqual(item["runtime"]["status"], "not_run")
        self.assertFalse(item["runtime"]["strict_acceptance"])
        self.assertEqual(item["strict_status"]["publication"], "draft")

    def test_supplemental_review_needs_matching_hash_and_artifact_binding(self):
        production = {"mode": "opencode-cli-go", "model": "opencode-go/deepseek-v4.1-flash",
                      "review_status": "passed", "review_input_digest": "e" * 64}
        value = {**self.artifact, "provenance": {**self.artifact["provenance"],
                 "imported_snapshot": {"provenance": {"model_production": production}}}}
        receipt = {"schema": "atlas.auxiliary-readable-review.v1", "artifact_id": value["id"],
                   "artifact_digest": value["digest"], "review_input_digest": "e" * 64,
                   "status": "passed", "session_id": "separate-full-review"}
        self.row["production_review"] = {"status": "incomplete_materials"}
        self.save()
        with patch.object(self.store, "artifacts", return_value=[value]):
            self.assertEqual(self.get()["items"][0]["production"]["review_status"], "incomplete_materials")
            self.file.write_text(json.dumps(receipt))
            # Bind the reviewed report independently of any runtime evidence.
            self.row["production_review"] = {"status": "passed", "file": {
                "path": "examples/demo.md", "sha256": hashlib.sha256(self.file.read_bytes()).hexdigest()}}
            self.save()
            self.assertEqual(self.get()["items"][0]["production"]["review_status"], "passed")
            self.file.write_text("changed")
            self.assertEqual(self.get()["items"][0]["production"]["review_status"], "incomplete_materials")
            self.assertFalse(self.get()["items"][0]["files"]["development"]["available"])
            with self.assertRaises(FactoryError) as caught:
                dispatch("GET", f"/api/factory/assisted-templates/{value['id']}/files/development", store=self.store)
            self.assertEqual(caught.exception.code, "assisted_review_needs_changes")

    def test_artifact_scene_identity_is_projected_without_rewriting_frozen_data(self):
        item = self.get()["items"][0]
        before = self.store.artifacts()
        result, _ = dispatch("GET", "/api/factory/artifacts", "scenario_id=" + item["scenario"]["id"], store=self.store)
        self.assertEqual(result[0]["scenario_id"], item["scenario"]["id"])
        self.assertEqual(dispatch("GET", "/api/factory/artifacts", "scenario_id=other", store=self.store)[0], [])
        self.assertEqual(self.store.artifacts(), before)

    def test_path_confinement_and_symlink_rejection(self):
        for path in ("", "../demo.md", "/etc/passwd", "application-atlas-production-pack/atlas/atlas.sqlite"):
            with self.assertRaises(FactoryError):
                asset_path(self.store, {"path": path, "sha256": "a" * 64})
        link = self.file.parent / "link.md"
        link.symlink_to(self.file)
        with self.assertRaises(FactoryError):
            asset_path(self.store, {"path": "examples/link.md", "sha256": hashlib.sha256(self.file.read_bytes()).hexdigest()})

    def test_not_run_has_no_application_links_and_existing_download_unchanged(self):
        self.row["runtime"] = {"status": "not_run", "scope": "No application run"}
        self.row["files"] = {"development": self.row["files"]["development"]}
        self.save()
        result = self.get()
        self.assertEqual(result["counts"]["not_run"], 1)
        self.assertNotIn("source", result["items"][0]["files"])
        with self.assertRaises(FactoryError):
            dispatch("GET", f"/api/factory/assisted-templates/{self.artifact['id']}/files/source", store=self.store)
        path, _, _ = dispatch("GET", f"/api/factory/assisted-templates/{self.artifact['id']}/files/development", store=self.store)
        self.assertEqual(path.read_bytes(), self.file.read_bytes())

    def test_withdrawn_auxiliary_draft_cannot_export_a_new_development_package(self):
        self.store.artifact_action(self.artifact["id"], {"action": "withdraw", "expected_digest": self.artifact["digest"],
                                                       "review": "Complete-material review requires revision"})
        with self.assertRaises(FactoryError) as caught:
            dispatch("POST", f"/api/factory/artifacts/{self.artifact['id']}/development-package", body={
                "expected_digest": self.artifact["digest"], "project_name": "blocked", "phase": "P0"}, store=self.store)
        self.assertEqual(caught.exception.code, "assisted_review_needs_changes")
        details, _ = dispatch("GET", f"/api/factory/artifacts/{self.artifact['id']}/blueprint", store=self.store)
        self.assertEqual(details["artifact_id"], self.artifact["id"])
