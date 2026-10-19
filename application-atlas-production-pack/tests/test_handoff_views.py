"""Acceptance checks for deterministic planning, execution and audit views."""

import hashlib
import json
from pathlib import Path
import sqlite3
import shutil
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.api import dispatch
from template_factory.artifacts import archive_tree, tree_manifest
from template_factory.blueprints import import_blueprint
from template_factory.store import FactoryStore

SAMPLE = Path(__file__).resolve().parents[2] / "docs/template-factory/blueprints/bookmark-personal"


class HandoffViewTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "source"
        shutil.copytree(SAMPLE, self.source, ignore=shutil.ignore_patterns("__pycache__", "node_modules"))
        pack = self.root / "pack"
        (pack / "atlas").mkdir(parents=True)
        with sqlite3.connect(pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES (?,?,?,?,?)", (
                "bookmark-manager", "Bookmark manager", "书签管理器", "URLs", "Bookmarks"))
        self.store = FactoryStore(self.root / "factory", pack)
        archive = self.root / "blueprint.zip"
        archive_tree(self.source, archive)
        self.artifact = import_blueprint(self.store, archive.read_bytes())

    def tearDown(self):
        self.tmp.cleanup()

    def export(self, name):
        result, _ = dispatch("POST", f"/api/factory/artifacts/{self.artifact['id']}/development-package",
            body={"expected_digest": self.artifact["digest"], "project_name": name, "phase": "P1"}, store=self.store)
        path, _, _ = dispatch("GET", result["download_url"], store=self.store)
        target = self.root / (name + "-package")
        with zipfile.ZipFile(path) as archive:
            archive.extractall(target)
        return target, result

    def test_frozen_source_phase_contract_and_manifest_are_complete(self):
        package, result = self.export("first")
        self.assertEqual((package / "blueprint/template.json").read_bytes(), (self.source / "template.json").read_bytes())
        spec = json.loads((self.source / "template.json").read_text())
        phase = json.loads((package / "CURRENT_PHASE.json").read_text())
        self.assertEqual(phase["scenario"], spec["scenario"])
        self.assertEqual(phase["prerequisite_phases"], ["P0"])
        self.assertEqual(phase["prerequisite_status"], "requires_verification")
        self.assertEqual(phase["selected_phase_status"], "not_started")
        expected_cases = [c for c in spec["acceptance"] if c["phase"] in {"P0", "P1"}]
        self.assertEqual(phase["acceptance"], expected_cases)
        self.assertEqual({c["id"] for c in phase["acceptance"]}, {c["id"] for c in expected_cases})
        for feature in phase["features"]:
            self.assertTrue(set(feature["acceptance"]) <= {c["id"] for c in expected_cases})
        decisions = json.loads((package / "PROJECT_DECISIONS.json").read_text())
        self.assertFalse(decisions["confirmed"])
        for source_decision, exported in zip(spec["decisions"], decisions["choices"]):
            for key in ("question", "default", "when_to_ask", "impact", "status"):
                self.assertEqual(exported[key], source_decision[key])
            self.assertIsNone(exported["choice"])
            self.assertFalse(exported["confirmed"])
        contract = json.loads((package / "ACCEPTANCE_CONTRACT.json").read_text())
        self.assertEqual(contract["schema"], "atlas.acceptance-contract.v1")
        self.assertEqual(contract["status"], "not_run")
        self.assertEqual(contract["template_digest"], self.artifact["digest"])
        self.assertEqual(contract["required_case_ids"], [c["id"] for c in expected_cases])
        expected_suite = {"acceptance/" + p: h for p, h in tree_manifest(package / "blueprint/acceptance").items()}
        refs = package / "blueprint/references"
        if refs.is_dir():
            expected_suite.update({"references/" + p: h for p, h in tree_manifest(refs).items()})
        self.assertEqual(contract["suite_sha256"], expected_suite)
        for case in contract["cases"]:
            content = (package / "blueprint" / case["implementation"]).read_bytes()
            self.assertEqual(case["implementation_sha256"], hashlib.sha256(content).hexdigest())
        manifest = json.loads((package / "HANDOFF_MANIFEST.json").read_text())
        self.assertEqual(manifest["blueprint_sha256"], tree_manifest(package / "blueprint"))
        self.assertEqual(manifest["views"], {"knowledge": "KNOWLEDGE.md", "execution": "HANDOFF.md", "acceptance": "ACCEPTANCE_CONTRACT.json"})
        for name, sha in manifest["entry_sha256"].items():
            self.assertEqual(sha, hashlib.sha256((package / name).read_bytes()).hexdigest())
        for rel in manifest["entry_sha256"]:
            self.assertTrue((package / rel).is_file())
        self.assertIn("APP_DELIVERY.md", manifest["entry_sha256"])
        delivery = (package / "APP_DELIVERY.md").read_text()
        for required in (
            "atlas.application-delivery.v1", "atlas.acceptance-runner.v1",
            '"profile": "static-web"', '"profile": "cli"',
            '"files": ["index.html"]', '"port": 8000',
            "no network access", "real credentials", "Exit code zero",
        ):
            self.assertIn(required, delivery)
        self.assertIn("APP_DELIVERY.md", (package / "HANDOFF.md").read_text())
        self.assertIn("APP_DELIVERY.md", (package / "AGENT.md").read_text())
        self.assertEqual(result["acceptance_contract_path"], "ACCEPTANCE_CONTRACT.json")
        self.assertFalse((package / "index.html").exists())
        self.assertTrue((package / ".atlas-blueprint.json").is_file())

    def test_views_are_deterministic_across_exports(self):
        first, _ = self.export("same")
        second, _ = self.export("same")
        for name in ("README.md", "AGENT.md", "HANDOFF.md", "KNOWLEDGE.md", "CURRENT_PHASE.json",
                     "PROJECT_DECISIONS.json", "ACCEPTANCE_CONTRACT.json", "HANDOFF_MANIFEST.json"):
            self.assertEqual((first / name).read_bytes(), (second / name).read_bytes(), name)


if __name__ == "__main__":
    unittest.main()
