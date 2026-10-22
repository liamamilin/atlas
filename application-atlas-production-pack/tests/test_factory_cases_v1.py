"""Shared case-library migration and immutable evidence contracts."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.cases import CaseLibrary
from template_factory.migrations import migrate
from template_factory.store import FactoryError, FactoryStore
from drafts_api import _read_app_catalog


PACK_ROOT = Path(__file__).resolve().parents[1]


class CaseLibraryV1Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK_ROOT / "mvp_apps.json", self.pack / "mvp_apps.json")
        shutil.copy(PACK_ROOT / "mvp_apps_classified.json", self.pack / "mvp_apps_classified.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES(?,?,?,?,?)", ("task-management-application", "Task manager", "任务管理", "manage tasks", "Task workflows"))
        (self.pack / "applications").mkdir()
        (self.pack / "applications/task-management-application.md").write_text("# Task manager\n", encoding="utf-8")
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.library = CaseLibrary(self.store)
        self.scenario_a = self.store.save_scenario({"leaf": "task-management-application", "name": "Complete tasks", "audience": "Individual", "objective": "Complete a task", "workflow": ["Create task", "Complete task"], "acceptance": ["Task remains completed"], "status": "ready"})
        self.scenario_b = self.store.save_scenario({"leaf": "task-management-application", "name": "Review tasks", "audience": "Individual", "objective": "Review task state", "workflow": ["Open task", "Review status"], "acceptance": ["Current status is visible"], "status": "ready"})

    def tearDown(self):
        self.tmp.cleanup()

    def _snapshot(self, content="def run():\n    return True\n", name="src/main.py", commit="a" * 40):
        root = self.store.root / "snapshots" / commit[:8]
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        license_path = root / "LICENSE"
        license_path.write_text("MIT License text for the pinned commit.\n", encoding="utf-8")
        files = {name: hashlib.sha256(target.read_bytes()).hexdigest(), "LICENSE": hashlib.sha256(license_path.read_bytes()).hexdigest()}
        return {
            "repository": "https://github.com/example/project",
            "repo_id": "github:1234",
            "commit_sha": commit,
            "collected_at": "2026-10-19T10:00:00Z",
            "strategy_version": "archive-v1",
            "local_root": str(root),
            "files": files,
            "license_files": ["LICENSE"],
            "license": {"spdx_id_supplement": "MIT", "supplement_source": "current GitHub metadata", "supplement_collected_at": "2026-10-19T10:00:00Z", "notice_hashes": {"LICENSE": files["LICENSE"]}},
        }

    def _move_snapshot_to_sources_alias(self, payload):
        snapshot = payload["source_snapshots"][0]
        original = Path(snapshot["local_root"])
        target = self.root / "external-source-cache"
        target.mkdir(parents=True, exist_ok=True)
        moved = target / original.name
        shutil.move(str(original), str(moved))
        alias = self.store.root / "sources"
        alias.symlink_to(target, target_is_directory=True)
        snapshot["local_root"] = str(alias / moved.name)
        return snapshot, alias, target, moved

    def _payload(self, *, case_id="case:demo", scenario=None, snapshot=None, evidence_id="ev-main"):
        snapshot = snapshot or self._snapshot()
        scenario = scenario or self.scenario_a["id"]
        return {
            "app_id": "todoist",
            "case_id": case_id,
            "source_snapshots": [snapshot],
            "research": {
                "summary": "A fixed implementation demonstrates a task workflow.",
                "scope": "Task lifecycle",
                "unknowns": ["Deployment behavior was not run"],
                "input_digest": "research-input-01",
                "task_id": "research-job-01",
            },
            "observations": [{
                "evidence_id": evidence_id,
                "kind": "code_observation",
                "statement": "The entry point returns success after the operation.",
                "location": {"commit_sha": snapshot["commit_sha"], "path": next(iter(snapshot["files"])), "file_digest": next(iter(snapshot["files"].values())), "symbol": "run"},
            }],
            "scenario_links": [{
                "scenario_id": scenario,
                "scenario_revision": 1,
                "reason": "The implementation covers the scenario's central action.",
                "workflow_support": ["complete a task"],
                "adopted_scope": ["task completion"],
                "exclusions": ["multi-user sync"],
                "evidence_ids": [evidence_id],
            }],
        }

    def test_legacy_catalog_imports_33_stable_catalog_only_apps_and_reruns(self):
        first = self.library.list_apps()
        self.assertEqual(len(first), 33)
        todo = self.library.get_app("todoist")
        self.assertEqual(todo["app_id"], "app:todoist")
        self.assertEqual(todo["legacy_slug"], "todoist")
        self.assertEqual(todo["aliases"], ["待办清单", "Doist"])
        self.assertEqual(todo["catalog_status"], "catalog_only")
        original = next(a for a in json.loads((self.pack / "mvp_apps_classified.json").read_text()) if a["slug"] == "todoist")
        self.assertEqual(todo["catalog_classification"], original)
        migrate(self.store)
        self.assertEqual(len(self.library.list_apps()), 33)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM schema_migration WHERE version=1").fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM schema_migration WHERE version=2").fetchone()[0], 1)

    def test_legacy_app_catalog_reference_fingerprint_semantics_are_unchanged(self):
        before = _read_app_catalog("todoist", self.pack)["fingerprint"]
        migrate(self.store)
        after = _read_app_catalog("todoist", self.pack)["fingerprint"]
        self.assertEqual(before, after)

    def test_rejected_observation_cannot_be_borrowed_as_accepted_design_fact(self):
        payload = self._payload()
        payload["observations"].append({**payload["observations"][0], "evidence_id": "ev-rejected", "statement": "Unsubstantiated claim"})
        result = self.library.commit_research(payload, "mixed-review")
        case = result["case"]
        for eid, outcome in [("ev-main", "accepted"), ("ev-rejected", "rejected")]:
            self.library.record_evidence_review(case["case_id"], case["revision"], eid, outcome, "independent-test", "independent_agent")
        basis = self.library.evidence_basis([{"case_id": case["case_id"], "revision": case["revision"]}], self.scenario_a["id"], 1)
        self.library.require_admissible(basis)
        self.assertEqual(self.library.accepted_evidence_ids(basis), {"ev-main"})
        with self.assertRaises(FactoryError):
            self.library.require_design_evidence(basis, [{"disposition": "adopted", "evidence_ids": ["ev-rejected"]}])
        self.library.require_design_evidence(basis, [{"disposition": "not_adopted", "evidence_ids": ["ev-rejected"]}])

    def test_empty_database_migration_rollback_then_retry(self):
        broken_pack = self.root / "broken-pack"
        broken_pack.mkdir()
        (broken_pack / "mvp_apps.json").write_text("[]", encoding="utf-8")
        valid_pack = self.root / "valid-pack"
        valid_pack.mkdir()
        shutil.copy(PACK_ROOT / "mvp_apps.json", valid_pack / "mvp_apps.json")
        broken_store = FactoryStore(self.root / "broken-factory", valid_pack)
        with broken_store.connect(True) as con:
            for table in ("evidence_review", "case_idempotency", "scenario_case_link", "evidence_observation", "case_revision", "source_snapshot", "case_app", "schema_migration"):
                con.execute(f"DROP TABLE {table}")
        broken_store.pack = broken_pack
        with self.assertRaisesRegex(ValueError, "exactly 33"):
            migrate(broken_store)
        with broken_store.connect() as con:
            tables = {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            self.assertNotIn("case_app", tables)
            self.assertNotIn("schema_migration", tables)
        shutil.copy(PACK_ROOT / "mvp_apps.json", broken_pack / "mvp_apps.json")
        migrate(broken_store)
        with broken_store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM case_app").fetchone()[0], 33)

    def test_idempotent_commit_and_many_to_many_fixed_revisions(self):
        first = self.library.commit_research(self._payload(), "request-1")
        replay = self.library.commit_research(self._payload(), "request-1")
        self.assertFalse(first["replayed"])
        self.assertTrue(replay["replayed"])
        self.assertEqual(first["case"]["digest"], replay["case"]["digest"])
        self.assertEqual(len(self.library.list_cases(scenario_id=self.scenario_a["id"])), 1)

        # One case supports a second scenario in a new immutable revision.
        p2 = self._payload(scenario=self.scenario_b["id"])
        p2["research"]["input_digest"] = "research-input-02"
        second_revision = self.library.commit_research(p2, "request-2")["case"]
        self.assertEqual(second_revision["revision"], 2)
        self.assertEqual(len(self.library.list_cases(scenario_id=self.scenario_b["id"])), 1)
        self.assertEqual(self.library.resolve_case_ref("atlas:case:case:demo:r1")["digest"], first["case"]["digest"])

        # A separate case can share the same scenario revision.
        p3 = self._payload(case_id="case:other", scenario=self.scenario_a["id"], snapshot=self._snapshot(commit="b" * 40), evidence_id="ev-other")
        self.library.commit_research(p3, "request-3")
        linked = self.library.list_cases(scenario_id=self.scenario_a["id"])
        self.assertEqual({value["case_id"] for value in linked}, {"case:demo", "case:other"})

    def test_code_location_hash_is_host_verified_and_revision_is_immutable(self):
        payload = self._payload()
        committed = self.library.commit_research(payload, "valid") ["case"]
        reference = self.library.case_ref("case:demo", 1)
        changed = self._payload()
        changed["observations"][0]["location"]["file_digest"] = "0" * 64
        with self.assertRaisesRegex(FactoryError, "verified digest"):
            self.library.commit_research(changed, "wrong-hash")
        p2 = self._payload()
        p2["research"]["input_digest"] = "different-input"
        revision2 = self.library.commit_research(p2, "revision-2")["case"]
        self.assertEqual(revision2["revision"], 2)
        self.assertEqual(self.library.resolve_case_ref(reference["ref"], reference["digest"])["digest"], committed["digest"])
        with self.assertRaises(FactoryError):
            self.library.resolve_case_ref(reference["ref"], "f" * 64)

    def test_rejects_unknown_app_path_escape_root_and_unverified_runtime(self):
        unknown = self._payload()
        unknown["app_id"] = "invented-app"
        with self.assertRaisesRegex(FactoryError, "application not found"):
            self.library.commit_research(unknown, "unknown-app")
        escaping = self._payload()
        escaping["source_snapshots"][0]["local_root"] = str(self.root)
        with self.assertRaisesRegex(FactoryError, "inside the factory store root"):
            self.library.commit_research(escaping, "escape-root")
        traversal = self._payload()
        traversal["observations"][0]["location"]["path"] = "../secret"
        with self.assertRaisesRegex(FactoryError, "escapes"):
            self.library.commit_research(traversal, "path-traversal")
        runtime = self._payload()
        runtime["observations"] = [{"evidence_id": "ev-runtime", "kind": "runtime_verification", "statement": "The case passed.", "verification_run_id": "fake-run", "assertion_id": "assertion-1"}]
        with self.assertRaisesRegex(FactoryError, "persisted run"):
            self.library.commit_research(runtime, "fake-runtime")

    def test_source_snapshot_accepts_host_owned_external_sources_alias(self):
        payload = self._payload()
        snapshot, alias, target, moved = self._move_snapshot_to_sources_alias(payload)
        payload["research"]["input_digest"] = "external-alias"
        case = self.library.commit_research(payload, "external-source-alias")["case"]
        self.assertEqual(Path(snapshot["local_root"]), alias / moved.name)
        self.assertTrue((target / moved.name / "src/main.py").is_file())
        self.assertEqual(case["source_snapshots"][0]["files"]["src/main.py"], snapshot["files"]["src/main.py"])

    def test_source_snapshot_rejects_other_external_roots_and_store_root_injection(self):
        payload = self._payload()
        snapshot = payload["source_snapshots"][0]
        original = Path(snapshot["local_root"])
        rogue = self.root / "rogue-cache" / "repo"
        rogue.parent.mkdir()
        shutil.move(str(original), str(rogue))
        approved = self.root / "approved-cache"
        approved.mkdir()
        (self.store.root / "sources").symlink_to(approved, target_is_directory=True)
        snapshot["local_root"] = str(rogue)
        snapshot["_store_root"] = str(rogue)
        with self.assertRaisesRegex(FactoryError, "inside the factory store root"):
            self.library.commit_research(payload, "other-external-root")

    def test_source_snapshot_alias_rejects_snapshot_and_file_symlinks(self):
        payload = self._payload()
        snapshot, alias, _, moved = self._move_snapshot_to_sources_alias(payload)
        alias_link = alias / "repo-link"
        alias_link.symlink_to(moved, target_is_directory=True)
        snapshot["local_root"] = str(alias_link)
        with self.assertRaisesRegex(FactoryError, "non-symlink directory"):
            self.library.commit_research(payload, "aliased-snapshot-leaf")

        snapshot["local_root"] = str(alias / moved.name)
        target = moved / "src/main.py"
        content = target.read_text(encoding="utf-8")
        target.unlink()
        external_file = self.root / "external-main.py"
        external_file.write_text(content, encoding="utf-8")
        target.symlink_to(external_file)
        with self.assertRaisesRegex(FactoryError, "source path contains a symlink"):
            self.library.commit_research(payload, "aliased-file-symlink")

    def test_source_snapshot_missing_or_broken_sources_alias_does_not_fallback(self):
        for case_id, broken in (("missing-sources-alias", False), ("broken-sources-alias", True)):
            with self.subTest(case_id=case_id):
                payload = self._payload(case_id="case:" + case_id,
                                        snapshot=self._snapshot(commit=("c" if broken else "d") * 40))
                _, alias, target, _ = self._move_snapshot_to_sources_alias(payload)
                alias.unlink()
                if broken:
                    alias.symlink_to(target / "missing", target_is_directory=True)
                with self.assertRaisesRegex(FactoryError, "existing non-symlink directory"):
                    self.library.commit_research(payload, case_id)

    def test_scenario_revision_and_source_location_are_host_validated(self):
        unknown_scenario = self._payload(scenario="unknown-scenario")
        with self.assertRaisesRegex(FactoryError, "scenario revision does not exist"):
            self.library.commit_research(unknown_scenario, "unknown-scenario")
        invalid_symbol = self._payload()
        invalid_symbol["observations"][0]["location"]["symbol"] = "missing_symbol"
        with self.assertRaisesRegex(FactoryError, "symbol is absent"):
            self.library.commit_research(invalid_symbol, "unknown-symbol")
        invalid_lines = self._payload()
        invalid_lines["observations"][0]["location"].update({"line_start": 1, "line_end": 99})
        with self.assertRaisesRegex(FactoryError, "line range is outside"):
            self.library.commit_research(invalid_lines, "line-bounds")

    def test_evidence_ids_cannot_ambiguous_across_case_refs(self):
        first = self.library.commit_research(self._payload(evidence_id="ev-shared"), "shared-evidence-1")["case"]
        second_payload = self._payload(case_id="case:second", snapshot=self._snapshot(commit="b" * 40), evidence_id="ev-shared")
        second = self.library.commit_research(second_payload, "shared-evidence-2")["case"]
        with self.assertRaisesRegex(FactoryError, "ambiguous across selected case revisions"):
            self.library.evidence_basis([{"case_id": first["case_id"], "revision": first["revision"]}, {"case_id": second["case_id"], "revision": second["revision"]}], self.scenario_a["id"], self.scenario_a["revision"])

    def test_snapshot_dedup_ignores_volatile_current_license_metadata(self):
        first_payload = self._payload()
        first = self.library.commit_research(first_payload, "license-snapshot-1")["case"]
        second_payload = self._payload(case_id="case:license", evidence_id="ev-license")
        second_payload["source_snapshots"][0]["collected_at"] = "2026-10-20T10:00:00Z"
        second_payload["source_snapshots"][0]["license"]["spdx_id_supplement"] = "Apache-2.0"
        second_payload["source_snapshots"][0]["license"]["supplement_collected_at"] = "2026-10-20T10:00:00Z"
        second = self.library.commit_research(second_payload, "license-snapshot-2")["case"]
        self.assertEqual(first["snapshot_ids"], second["snapshot_ids"])
        persisted = second["source_snapshots"][0]
        self.assertEqual(persisted["license"]["spdx_id_supplement"], "MIT")
        self.assertEqual(persisted["license_files"], ["LICENSE"])
        self.assertEqual(persisted["files"]["LICENSE"], persisted["license"]["notice_hashes"]["LICENSE"])

    def test_github_repository_identity_is_normalized(self):
        payload = self._payload()
        payload["source_snapshots"][0]["repository"] = "HTTPS://GitHub.COM/Example/Project.git/"
        case = self.library.commit_research(payload, "canonical-repository")["case"]
        self.assertEqual(case["source_snapshots"][0]["repository"], "https://github.com/example/project")

    def test_review_is_separate_from_observation_and_basis_is_digest_bound(self):
        case = self.library.commit_research(self._payload(), "review-test")["case"]
        observation = case["observations"][0]
        self.assertEqual(observation["observation_status"], "source_located")
        self.assertEqual(observation["review"]["status"], "pending")
        with self.assertRaisesRegex(FactoryError, "assigned only"):
            bad = self._payload()
            bad["observations"][0]["review"] = {"status": "independent_reviewed", "reviewer": "self"}
            self.library.commit_research(bad, "self-review")
        basis = self.library.evidence_basis(["atlas:case:case:demo:r1"], self.scenario_a["id"], self.scenario_a["revision"])
        self.assertEqual(self.library.validate_basis(basis), basis)
        with self.assertRaisesRegex(FactoryError, "lacks an independently accepted"):
            self.library.require_admissible(basis)
        reviewed = self.library.record_evidence_review(case["case_id"], case["revision"], observation["evidence_id"], "accepted", "reviewer-1", "independent_agent")
        self.assertEqual(reviewed["evidence_digest"], observation["digest"])
        self.library.require_admissible(basis)
        self.library.record_evidence_review(case["case_id"], case["revision"], observation["evidence_id"], "rejected", "reviewer-2", "independent_agent")
        with self.assertRaisesRegex(FactoryError, "lacks an independently accepted"):
            self.library.require_admissible(basis)
        basis["evidence_ids"] = []
        with self.assertRaisesRegex(FactoryError, "stale or has been altered"):
            self.library.validate_basis(basis)


if __name__ == "__main__":
    unittest.main()
