"""Local cognitive-package integration; no provider calls or package execution."""

from concurrent.futures import ThreadPoolExecutor
import base64
import hashlib
import io
import json
from pathlib import Path
import shutil
import sqlite3
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.api import dispatch
from template_factory.artifacts import archive_tree, tree_manifest
from template_factory.blueprints import (
    import_blueprint,
    unpack_archive,
    validate_blueprint,
    verify_frozen,
)
from template_factory.store import FactoryError, FactoryStore

SAMPLE = (
    Path(__file__).resolve().parents[2]
    / "docs/template-factory/blueprints/bookmark-personal"
)


class BlueprintTests(unittest.TestCase):
    def test_bundled_sample_is_self_contained_without_history_or_local_zip(self):
        with patch("subprocess.run", side_effect=AssertionError("sample must not execute code or git")):
            sample, status = dispatch("POST", "/api/factory/blueprints/sample", store=self.store)
        self.assertEqual(status, 201)
        self.assertEqual(sample["artifact_type"], "product-blueprint")
        self.assertEqual(sample["evidence_status"], "legacy_unverified")
        self.assertEqual(sample["state"], "draft")

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "sample"
        shutil.copytree(
            SAMPLE,
            self.source,
            ignore=shutil.ignore_patterns("__pycache__", "node_modules"),
        )
        self.pack = self.root / "pack"
        (self.pack / "atlas").mkdir(parents=True)
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute(
                "INSERT INTO leaf VALUES (?,?,?,?,?)",
                (
                    "bookmark-manager",
                    "Bookmark manager",
                    "书签管理器",
                    "URLs",
                    "Bookmarks",
                ),
            )
        self.store = FactoryStore(self.root / "factory", self.pack)

    def tearDown(self):
        self.tmp.cleanup()

    def data(self):
        output = self.root / (
            "input-" + str(len(list(self.root.glob("input-*.zip")))) + ".zip"
        )
        archive_tree(self.source, output)
        return output.read_bytes()

    def rewrite(self, mutate):
        path = self.source / "template.json"
        value = json.loads(path.read_text())
        mutate(value)
        path.write_text(json.dumps(value, ensure_ascii=False))
        inventory = tree_manifest(self.source)
        inventory.pop("integrity.json")
        (self.source / "integrity.json").write_text(
            json.dumps({"template_version": value["version"], "sha256": inventory})
        )

    def test_sample_validates_without_executing_code(self):
        with patch(
            "subprocess.run",
            side_effect=AssertionError("must not execute imported code"),
        ):
            spec, manifest = validate_blueprint(self.source)
            value = import_blueprint(self.store, self.data())
        self.assertEqual(manifest["feature_count"], 18)
        self.assertEqual(len(spec["acceptance"]), 17)
        self.assertEqual(value["artifact_type"], "product-blueprint")
        self.assertEqual(value["level"], "L0")
        self.assertEqual(value["state"], "draft")
        self.assertEqual(value["acceptances"], [])
        self.assertEqual(self.store.scenarios(), [])
        self.assertEqual(self.store.job(value["job_id"])["state"], "completed")

    def save_definition_and_plan(self, value):
        (self.source / "template.json").write_text(
            json.dumps(value, ensure_ascii=False)
        )
        plan_path = self.source / "acceptance/plan.json"
        plan = json.loads(plan_path.read_text())
        plan.update(cases=value["acceptance"], phases=value["phases"])
        plan_path.write_text(json.dumps(plan, ensure_ascii=False))
        inventory = tree_manifest(self.source)
        inventory.pop("integrity.json")
        (self.source / "integrity.json").write_text(
            json.dumps({"template_version": value["version"], "sha256": inventory})
        )

    def test_later_cases_can_regress_earlier_features_but_not_the_reverse(self):
        value = json.loads((self.source / "template.json").read_text())
        first, second = value["phases"][0]["id"], value["phases"][1]["id"]
        early = next(f for f in value["features"] if f["phase"] == first)
        late = next(c for c in value["acceptance"] if c["phase"] == second)
        early["acceptance"].append(late["id"])
        late["features"].append(early["id"])
        self.save_definition_and_plan(value)
        validate_blueprint(self.source)
        future = next(f for f in value["features"] if f["phase"] == second)
        baseline = next(c for c in value["acceptance"] if c["phase"] == first)
        future["acceptance"].append(baseline["id"])
        baseline["features"].append(future["id"])
        self.save_definition_and_plan(value)
        with self.assertRaisesRegex(FactoryError, "future"):
            validate_blueprint(self.source)

    def test_later_regression_does_not_replace_introduction_phase_acceptance(self):
        value = json.loads((self.source / "template.json").read_text())
        early = next(
            f for f in value["features"] if f["phase"] == value["phases"][0]["id"]
        )
        late = next(
            c for c in value["acceptance"] if c["phase"] == value["phases"][1]["id"]
        )
        extra = {**early, "id": "F99", "acceptance": [late["id"]]}
        value["features"].append(extra)
        late["features"].append("F99")
        value["phases"][0]["features"].append("F99")
        self.save_definition_and_plan(value)
        with self.assertRaisesRegex(FactoryError, "introduction"):
            validate_blueprint(self.source)

    def test_dependency_manifest_must_parse_before_accepting_a_package(self):
        package = self.source / "acceptance/package.json"
        for content in (
            '{"name":"broken"\n"private":true}',
            '{"scripts":{"test":false}}',
        ):
            package.write_text(content)
            self.rewrite(lambda _: None)
            with self.assertRaises(FactoryError):
                validate_blueprint(self.source)

    def test_import_is_idempotent_even_when_concurrent(self):
        data = self.data()
        with ThreadPoolExecutor(max_workers=2) as pool:
            values = list(
                pool.map(lambda _: import_blueprint(self.store, data), range(2))
            )
        self.assertEqual(values[0]["id"], values[1]["id"])
        self.assertEqual(len(self.store.artifacts()), 1)
        self.assertEqual(len(self.store.batches()), 1)

    def test_json_api_read_and_development_export_preserve_blueprint(self):
        result, status = dispatch(
            "POST",
            "/api/factory/blueprints/import",
            body={"archive_base64": base64.b64encode(self.data()).decode()},
            store=self.store,
        )
        self.assertEqual(status, 201)
        prefix = "/api/factory/artifacts/" + result["id"]
        details, status = dispatch("GET", prefix + "/blueprint", store=self.store)
        self.assertEqual(status, 200)
        self.assertIn("AGENT.md", details["documents"])
        self.assertEqual(len(details["spec"]["decisions"]), 8)
        frozen_zip, _, _ = dispatch("GET", prefix + "/download", store=self.store)
        with zipfile.ZipFile(frozen_zip) as archive:
            self.assertIn("template.json", archive.namelist())
        self.assertEqual(
            import_blueprint(self.store, frozen_zip.read_bytes())["id"], result["id"]
        )
        payload, status = dispatch(
            "POST",
            prefix + "/development-package",
            body={
                "project_name": "my-bookmarks",
                "phase": "P0",
                "expected_digest": result["digest"],
            },
            store=self.store,
        )
        self.assertEqual(status, 201)
        path, _, _ = dispatch("GET", payload["download_url"], store=self.store)
        with zipfile.ZipFile(path) as archive:
            receipt = json.loads(archive.read("PROJECT_DECISIONS.json"))
            self.assertEqual(receipt["phase"], "P0")
            self.assertEqual(receipt["project_name"], "my-bookmarks")
            self.assertEqual(len(receipt["choices"]), 8)
            self.assertTrue(all(row["choice"] is None for row in receipt["choices"]))
            current = json.loads(archive.read("CURRENT_PHASE.json"))
            self.assertEqual(current["selected_phase"], "P0")
            self.assertEqual(current["template_digest"], result["digest"])
            self.assertEqual(current["prerequisite_phases"], [])
            self.assertEqual(current["evidence_status"], "not_run_by_export")
            spec = details["spec"]
            self.assertEqual(current["scenario"], spec["scenario"])
            self.assertEqual(current["decisions"], spec["decisions"])
            self.assertEqual(current["limits"], spec["limits"])
            self.assertEqual(
                current["acceptance"],
                [case for case in spec["acceptance"] if case["phase"] == "P0"],
            )
            self.assertTrue(all(row["phase"] == "P0" for row in current["features"]))
            self.assertNotIn("architecture_markdown", current)
            self.assertNotIn("evidence", current)
            self.assertIn("HANDOFF.md", archive.read("README.md").decode())
            self.assertIn(
                "blueprint/ARCHITECTURE.md", archive.read("HANDOFF.md").decode()
            )
            self.assertEqual(
                archive.read("blueprint/template.json"),
                (self.source / "template.json").read_bytes(),
            )
            inventory = json.loads(archive.read("blueprint/integrity.json"))["sha256"]
            for rel, expected in inventory.items():
                self.assertEqual(
                    hashlib.sha256(archive.read("blueprint/" + rel)).hexdigest(),
                    expected,
                )
            self.assertNotIn("index.html", archive.namelist())
        self.assertEqual(
            verify_frozen(self.store.root / result["bundle_path"], result["digest"])[
                "version"
            ],
            "0.1.1",
        )
        filtered, _ = dispatch(
            "GET",
            "/api/factory/artifacts",
            query="type=product-blueprint",
            store=self.store,
        )
        self.assertEqual([a["id"] for a in filtered], [result["id"]])

    def test_old_publication_acceptance_and_repair_are_not_reused(self):
        value = import_blueprint(self.store, self.data())
        for operation, body in [
            ("instantiate", {"project_name": "should-not-run"}),
            ("accept", {"method": "harness-review"}),
            ("review", {"action": "publish", "review": "looks good", "level": "L2"}),
        ]:
            with (
                self.subTest(operation=operation),
                self.assertRaises(FactoryError) as error,
            ):
                dispatch(
                    "POST",
                    f"/api/factory/artifacts/{value['id']}/{operation}",
                    body={**body, "expected_digest": value["digest"]},
                    store=self.store,
                )
            self.assertEqual(error.exception.code, "case_evidence_required" if operation == "review" else "blueprint_operation_unavailable")
        for method, args in [
            (self.store.create_acceptance, {"method": "harness-review"}),
            (
                self.store.artifact_action,
                {"action": "publish", "review": "accepted", "level": "L2"},
            ),
        ]:
            with self.assertRaises(FactoryError):
                method(value["id"], {**args, "expected_digest": value["digest"]})
        self.assertEqual(len(self.store.batches()), 1)

    def test_cognitive_revision_request_replays_terminal_job_instead_of_free_new_round(self):
        value = import_blueprint(self.store, self.data())
        request = {"expected_digest": value["digest"], "model": "fake/flash", "note": "Clarify the phase acceptance and limits."}
        first = self.store.create_repair(value["id"], request)
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET state='failed' WHERE batch_id=?", (first["id"],))
        replay = self.store.create_repair(value["id"], request)
        self.assertEqual(first["id"], replay["id"])
        different = self.store.create_repair(value["id"], {**request, "model": "other/flash"})
        self.assertNotEqual(different["id"], first["id"])

    def test_export_rejects_stale_digest_bad_project_and_unknown_phase(self):
        value = import_blueprint(self.store, self.data())
        route = f"/api/factory/artifacts/{value['id']}/development-package"
        for body in [
            {"expected_digest": "stale", "project_name": "app"},
            {"expected_digest": value["digest"], "project_name": "../escape"},
            {"expected_digest": value["digest"], "project_name": "app", "phase": "P99"},
            {"expected_digest": value["digest"], "project_name": "app", "phase": {}},
        ]:
            with self.subTest(body=body), self.assertRaises(FactoryError):
                dispatch("POST", route, body=body, store=self.store)
        self.assertFalse((self.store.root / "downloads").exists())

    def test_later_phase_handoff_preserves_prerequisites_and_regression_cases(self):
        value = import_blueprint(self.store, self.data())
        original = json.loads((self.source / "template.json").read_text())
        route = f"/api/factory/artifacts/{value['id']}/development-package"
        result, _ = dispatch(
            "POST",
            route,
            body={
                "expected_digest": value["digest"],
                "project_name": "later",
                "phase": "P1",
            },
            store=self.store,
        )
        path, _, _ = dispatch("GET", result["download_url"], store=self.store)
        with zipfile.ZipFile(path) as archive:
            current = json.loads(archive.read("CURRENT_PHASE.json"))
            self.assertEqual(current["prerequisite_phases"], ["P0"])
            self.assertEqual(current["phases"], original["phases"][:2])
            self.assertEqual(
                current["acceptance"],
                [a for a in original["acceptance"] if a["phase"] in {"P0", "P1"}],
            )
            cases = {a["id"] for a in current["acceptance"]}
            self.assertEqual(
                {f["id"] for f in current["features"]},
                {f["id"] for f in original["features"] if f["phase"] in {"P0", "P1"}},
            )
            for feature in current["features"]:
                self.assertTrue(set(feature["acceptance"]) <= cases)
            for case in current["acceptance"]:
                self.assertIn("blueprint/" + case["implementation"], archive.namelist())
            self.assertEqual(
                archive.read("blueprint/template.json"),
                (self.source / "template.json").read_bytes(),
            )

    def test_phase_summary_omits_future_regression_links_without_mutating_source(self):
        # A later test may legitimately regress an earlier capability. Keep it in
        # the full blueprint, not in an earlier-phase development requirement.
        path = self.source / "template.json"
        spec = json.loads(path.read_text())
        spec["features"][0]["acceptance"].append("A10")
        case = next(a for a in spec["acceptance"] if a["id"] == "A10")
        case["features"].append(spec["features"][0]["id"])
        (self.source / "acceptance/plan.json").write_text(
            json.dumps(
                {
                    "template_id": spec["id"],
                    "phases": spec["phases"],
                    "cases": spec["acceptance"],
                }
            )
        )
        self.rewrite(lambda value: value.update(spec))
        value = import_blueprint(self.store, self.data())
        result, _ = dispatch(
            "POST",
            f"/api/factory/artifacts/{value['id']}/development-package",
            body={"expected_digest": value["digest"], "project_name": "first"},
            store=self.store,
        )
        path, _, _ = dispatch("GET", result["download_url"], store=self.store)
        with zipfile.ZipFile(path) as archive:
            packet = json.loads(archive.read("CURRENT_PHASE.json"))
            self.assertNotIn("A10", packet["features"][0]["acceptance"])
            full = json.loads(archive.read("blueprint/template.json"))
            self.assertIn("A10", full["features"][0]["acceptance"])

    def test_export_still_accepts_legacy_package_without_optional_limits(self):
        self.rewrite(lambda spec: spec.pop("limits", None))
        value = import_blueprint(self.store, self.data())
        result, _ = dispatch(
            "POST",
            f"/api/factory/artifacts/{value['id']}/development-package",
            body={"expected_digest": value["digest"], "project_name": "legacy"},
            store=self.store,
        )
        path, _, _ = dispatch("GET", result["download_url"], store=self.store)
        with zipfile.ZipFile(path) as archive:
            self.assertEqual(
                json.loads(archive.read("CURRENT_PHASE.json"))["limits"], []
            )

    def test_rejects_source_tamper_even_with_rewritten_inventory(self):
        value = import_blueprint(self.store, self.data())
        bundle = self.store.root / value["bundle_path"]
        target = bundle / "source/AGENT.md"
        target.write_text(target.read_text() + "\nchanged")
        with self.assertRaises(FactoryError):
            verify_frozen(bundle, value["digest"])
        hashes = tree_manifest(bundle / "source")
        hashes.pop("integrity.json")
        (bundle / "source/integrity.json").write_text(
            json.dumps({"template_version": "0.1.1", "sha256": hashes})
        )
        with self.assertRaises(FactoryError) as error:
            verify_frozen(bundle, value["digest"])
        self.assertEqual(error.exception.code, "artifact_changed")
        with self.assertRaises(FactoryError):
            dispatch(
                "GET",
                f"/api/factory/artifacts/{value['id']}/download",
                store=self.store,
            )

    def test_declared_reports_never_assign_factory_acceptance(self):
        self.rewrite(
            lambda v: v.update(
                status="L3 mature",
                evidence=[
                    {
                        "path": "evidence/review-3.json",
                        "outcome": "passed",
                        "level": "L3",
                    }
                ],
            )
        )
        value = import_blueprint(self.store, self.data())
        self.assertEqual(value["level"], "L0")
        self.assertEqual(value["acceptances"], [])

    def test_structural_references_checked_beyond_file_hashes(self):
        original = json.loads((self.source / "template.json").read_text())
        changes = [
            lambda v: v["features"][0].update(sources=["missing"]),
            lambda v: v["features"][0].update(acceptance=[]),
            lambda v: v["features"][0].update(phase={}),
            lambda v: v["acceptance"][0].update(features=[]),
            lambda v: v["acceptance"][0].update(phase=[]),
            lambda v: v["phases"][0].update(acceptance=[]),
            lambda v: v["decisions"].append(v["decisions"][0]),
            lambda v: v["sources"][0].update(url="javascript:alert(1)"),
            lambda v: v["sources"][0].update(url="https://user:password@example.com"),
            lambda v: v["sources"][0].update(url="https://["),
            lambda v: v.update(schema="unknown"),
        ]
        for change in changes:
            (self.source / "template.json").write_text(
                json.dumps(original, ensure_ascii=False)
            )
            self.rewrite(change)
            with self.subTest(change=change), self.assertRaises(FactoryError):
                validate_blueprint(self.source)

    def test_missing_acceptance_program_rejected(self):
        (self.source / "acceptance/run.cjs").unlink()
        self.rewrite(lambda _: None)
        with self.assertRaises(FactoryError):
            validate_blueprint(self.source)

    def test_archive_rejects_traversal_duplicates_secrets_and_symlinks(self):
        for names in [
            ["../escape"],
            ["/tmp/escape"],
            ["a/../../escape"],
            ["AGENTS.md"],
            ["opencode.json"],
            [".env"],
            ["node_modules/file.js"],
            ["x", "x"],
            ["bad-link"],
        ]:
            data = io.BytesIO()
            with zipfile.ZipFile(data, "w") as archive:
                for name in names:
                    info = zipfile.ZipInfo(name)
                    if name == "bad-link":
                        info.external_attr = (stat.S_IFLNK | 0o777) << 16
                    archive.writestr(info, "data")
            with self.subTest(names=names), self.assertRaises(FactoryError):
                unpack_archive(data.getvalue(), self.root / "extracted")
            self.assertFalse((self.root / "escape").exists())

    def test_archive_rejects_bomb_and_bad_base64_without_database_writes(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("too-big", b"x" * (8 * 1024 * 1024 + 1))
        for payload in [
            base64.b64encode(data.getvalue()).decode(),
            "not base64",
            "x" * 1_500_000,
        ]:
            with self.assertRaises(FactoryError):
                dispatch(
                    "POST",
                    "/api/factory/blueprints/import",
                    body={"archive_base64": payload},
                    store=self.store,
                )
        self.assertEqual(self.store.artifacts(), [])
        self.assertEqual(self.store.batches(), [])


if __name__ == "__main__":
    unittest.main()
