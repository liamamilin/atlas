"""Focused regressions for the fixed, read-only R7 preparation path."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.plan_revision import (
    R7_AUTHORIZATION_REF, R7_PATCH_REF, R7_PROGRAM_PATHS, R7_PROGRAMS_REF,
    R7_APPROVED_REVISION_REF, R7_REPLACE_PATHS, R7_SOURCE_JOB,
    _apply_r7_patch, _validate_approved_r7,
    build_program_revision_manifest, program_revision_contents,
)
from template_factory.store import FactoryError, digest


ROOT = Path(__file__).resolve().parents[2]
R7_DOCS = ROOT / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20"


def source_checkpoints():
    baseline = json.loads((R7_DOCS / "BASELINE.json").read_text(encoding="utf-8"))
    rows = {}
    for row in baseline["checkpoints"]:
        body = row["body"]
        rows[row["name"]] = json.loads(body) if isinstance(body, str) else body
    return rows


class _FixtureStore:
    def __init__(self, root, pack, checkpoints):
        self.root, self.pack, self._checkpoints = root, pack, checkpoints

    def checkpoint(self, job_id, name):
        if job_id != R7_SOURCE_JOB:
            return None
        return self._checkpoints.get(name)


class R7PreparationTests(unittest.TestCase):
    def setUp(self):
        self.checkpoints = source_checkpoints()
        self.plan = self.checkpoints["blueprint-plan-0"]["result"]
        self.choices = self.checkpoints["case-adaptation-prepared-aaf080ba52611126"]["result"]["choices"]
        self.patch = json.loads((R7_DOCS / "patch.json").read_text(encoding="utf-8"))

    def test_exact_patch_changes_only_allowlisted_spec_file_plan_and_choices(self):
        plan, choices = _apply_r7_patch(self.plan, self.choices, self.patch)
        self.assertEqual(len(plan["file_plan"]), 9)
        self.assertEqual({row["path"] for row in plan["file_plan"] if not row["reuse"]}, R7_REPLACE_PATHS)
        self.assertEqual(sum(row["path"] in R7_REPLACE_PATHS for row in plan["file_plan"]), 4)
        old_features = {row["id"]: row for row in self.plan["spec"]["features"]}
        new_features = {row["id"]: row for row in plan["spec"]["features"]}
        for identity in old_features:
            if identity != "F01":
                self.assertEqual(old_features[identity], new_features[identity])
        self.assertEqual(len(choices), len(self.choices))
        changed = [i for i, (before, after) in enumerate(zip(self.choices, choices)) if before != after]
        self.assertEqual(len(changed), 2)
        for index in range(len(self.choices)):
            if index not in changed:
                self.assertEqual(self.choices[index], choices[index])

    def test_patch_rejects_unapproved_paths_and_stale_old_values(self):
        bad = json.loads(json.dumps(self.patch))
        bad["spec_changes"][0]["path"] = ["features", "F15", "reason"]
        with self.assertRaises(FactoryError):
            _apply_r7_patch(self.plan, self.choices, bad)
        bad = json.loads(json.dumps(self.patch))
        bad["spec_changes"][0]["old"] = ["stale"]
        with self.assertRaises(FactoryError):
            _apply_r7_patch(self.plan, self.choices, bad)
        bad = json.loads(json.dumps(self.patch))
        bad["file_plan_changes"][0]["new"]["reuse"] = True
        with self.assertRaises(FactoryError):
            _apply_r7_patch(self.plan, self.choices, bad)
        bad = json.loads(json.dumps(self.patch))
        bad["program_changes"][0]["path"] = ["acceptance/p0_library.py"]
        with self.assertRaises(FactoryError):
            build_program_revision_manifest(_FixtureStore(Path("."), ROOT / "application-atlas-production-pack", self.checkpoints), bad, ROOT)

    def _fixture(self, directory):
        root = Path(directory)
        job_root = root / "jobs" / R7_SOURCE_JOB / "attempt-1"
        generated = job_root / "context/generated-0"
        generated.mkdir(parents=True)
        (job_root / "candidate-0").mkdir()
        # The source candidate itself is pinned by its production hash; use its
        # archived actual bytes, available in a clean checkout as well.
        archived = R7_DOCS.parent / "g1-r6-source-alignment-2026-10-20/candidate-attempt-1-not-frozen"
        shutil.copy(archived / "template.json",
                    job_root / "candidate-0/template.json")
        for index, path in enumerate(R7_PROGRAM_PATHS):
            result = self.checkpoints[f"blueprint-code-0-{index}"]["result"]
            target = generated / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(result["content"].encode("utf-8"))
        docs = root / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20"
        shutil.copytree(R7_DOCS / "authorization", docs / "authorization")
        shutil.copy(R7_DOCS / "patch.json", docs / "patch.json")
        shutil.copy(ROOT / R7_APPROVED_REVISION_REF, docs / "authorization/approved-revision.json")
        shutil.copytree(R7_DOCS / "prepared-programs", docs / "prepared-programs")
        pack = root / "application-atlas-production-pack"
        pack.mkdir()
        return _FixtureStore(root, pack, self.checkpoints), root

    def test_manifest_applies_four_exact_replacements_and_reuses_five_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            store, root = self._fixture(temp)
            manifest = build_program_revision_manifest(store, self.patch, root)
            self.assertEqual(len(manifest["entries"]), 9)
            self.assertEqual({row["path"] for row in manifest["entries"] if row["mode"] == "replace"}, R7_REPLACE_PATHS)
            self.assertEqual({row["path"] for row in manifest["entries"] if row["mode"] == "reuse"}, set(R7_PROGRAM_PATHS) - R7_REPLACE_PATHS)
            contents = program_revision_contents(store, manifest)
            self.assertEqual(set(contents), set(R7_PROGRAM_PATHS))
            for entry in manifest["entries"]:
                if entry["mode"] == "reuse":
                    self.assertEqual(entry["before_sha256"], entry["after_sha256"])
                    self.assertEqual(entry["patch"], [])
                else:
                    self.assertNotEqual(entry["before_sha256"], entry["after_sha256"])
                    self.assertTrue(entry["patch"])

    def test_tampered_source_or_prepared_program_bytes_fail_revalidation(self):
        with tempfile.TemporaryDirectory() as temp:
            store, root = self._fixture(temp)
            manifest = build_program_revision_manifest(store, self.patch, root)
            source = root / "jobs" / R7_SOURCE_JOB / "attempt-1/context/generated-0/acceptance/common.py"
            source.write_bytes(source.read_bytes() + b"# tamper\n")
            with self.assertRaises(FactoryError):
                build_program_revision_manifest(store, self.patch, root)

        with tempfile.TemporaryDirectory() as temp:
            store, root = self._fixture(temp)
            manifest = build_program_revision_manifest(store, self.patch, root)
            prepared = root / manifest["entries"][0]["prepared_ref"]
            prepared.write_bytes(prepared.read_bytes() + b"# tamper\n")
            with self.assertRaises(FactoryError):
                program_revision_contents(store, manifest)

    def test_manifest_rejects_unknown_path_or_forged_source_binding(self):
        with tempfile.TemporaryDirectory() as temp:
            store, root = self._fixture(temp)
            manifest = build_program_revision_manifest(store, self.patch, root)
            manifest["entries"][0]["source_job_id"] = "other-job"
            with self.assertRaises(FactoryError):
                program_revision_contents(store, manifest)

    def test_host_authorization_binds_exact_patch_manifest_and_request_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            store, root = self._fixture(temp)
            manifest = build_program_revision_manifest(store, self.patch, root)
            request = json.loads((R7_DOCS / "prepare-request.json").read_text(encoding="utf-8"))
            auth = request["source_authorization"]
            binding = request["binding"]
            self.assertTrue(_validate_approved_r7(root, auth, self.patch, manifest, binding))

            altered = json.loads(json.dumps(self.patch))
            altered["spec_changes"][0]["new"].append("A99")
            with self.assertRaises(FactoryError):
                _validate_approved_r7(root, auth, altered, manifest, binding)
            bad_auth = dict(auth, revision_digest="0" * 64)
            with self.assertRaises(FactoryError):
                _validate_approved_r7(root, bad_auth, self.patch, manifest, binding)


if __name__ == "__main__":
    unittest.main()
