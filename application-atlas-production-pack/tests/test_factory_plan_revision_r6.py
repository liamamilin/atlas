"""Regression coverage for the narrowly bound R6 preparation primitives."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.plan_revision import (
    R6_ARCHITECTURE_NEW, R6_ARCHITECTURE_OLD, R6_AUTHORIZATION_REF,
    R6_AUTHORIZATION_SHA256,
    R6_APPROVED_REVISION_REF, R6_PROGRAM_PATHS, R6_SOURCE_ARRAYS,
    _apply_r6_patch, _validate_approved_r6_patch,
    _checkpoint_result, _validate_pinned_case_design,
    _validate_research_view_binding, build_program_reuse_manifest,
    program_reuse_contents,
)
from template_factory.source_references import feature_source_reference_report
from template_factory.store import FactoryError, digest

DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-protocol-recovery-2026-10-19"


def checkpoint_rows():
    source = json.loads((DOCS / "actual-structural-stop.json").read_text())
    rows = {}
    for row in source["checkpoints"]:
        body = row["body"]
        rows[row["name"]] = json.loads(body) if isinstance(body, str) else body
    return rows


class _Store:
    def __init__(self, root, rows):
        self.root = root
        self.rows = rows

    def checkpoint(self, job_id, name):
        return self.rows.get(name)


class R6PreparationPrimitiveTests(unittest.TestCase):
    def setUp(self):
        self.rows = checkpoint_rows()
        self.plan = self.rows["blueprint-plan-0"]["result"]
        self.facts = self.rows["blueprint-accepted-facts-view"]["result"]
        self.research = self.rows["blueprint-research"]["result"]

    def _patch(self):
        changes = []
        features = {row["id"]: row for row in self.plan["spec"]["features"]}
        for fid, (old, new) in R6_SOURCE_ARRAYS.items():
            changes.append({"path": ["features", fid, "sources"],
                            "old": old, "new": new})
            self.assertEqual(features[fid]["sources"], old)
        old_arch = self.plan["spec"]["architecture_markdown"]
        self.assertEqual(old_arch.count(R6_ARCHITECTURE_OLD), 1)
        changes.append({"path": ["architecture_markdown"],
                        "old": old_arch,
                        "new": old_arch.replace(R6_ARCHITECTURE_OLD, R6_ARCHITECTURE_NEW, 1)})
        return {"spec_changes": changes}

    def _eligible_sources(self):
        eligible = set(self.facts["accepted_evidence_ids"])
        return [row for row in self.research["sources"] if row.get("name") in eligible] + [{"id": "S01"}]

    def test_old_real_plan_is_rejected_and_exact_patch_passes_same_checker(self):
        old_report = feature_source_reference_report(self.plan["spec"], self._eligible_sources())
        self.assertFalse(old_report["valid"])
        self.assertEqual({row["feature_id"] for row in old_report["features"] if row["missing_source_ids"]},
                         {"F01", "F07", "F08", "F10", "F11", "F12", "F24"})

        effective = _apply_r6_patch(self.plan, self._patch())
        new_report = feature_source_reference_report(effective["spec"], self._eligible_sources())
        self.assertTrue(new_report["valid"], new_report["errors"])
        self.assertEqual(effective["file_plan"], self.plan["file_plan"])
        for field in ("phases", "acceptance", "decisions", "roles", "limits", "contract_coverage"):
            self.assertEqual(effective["spec"][field], self.plan["spec"][field])

    def test_r6_patch_rejects_missing_or_out_of_scope_source_changes(self):
        patch = self._patch()
        patch["spec_changes"].pop(0)
        with self.assertRaises(FactoryError):
            _apply_r6_patch(self.plan, patch)
        patch = self._patch()
        patch["spec_changes"][0]["new"] = ["S02", "S04"]
        with self.assertRaises(FactoryError):
            _apply_r6_patch(self.plan, patch)
        patch = self._patch()
        patch["spec_changes"].append({"path": ["features", "F15", "reason"],
                                       "old": "x", "new": "y"})
        with self.assertRaises(FactoryError):
            _apply_r6_patch(self.plan, patch)

    def test_only_the_host_approved_reason_patch_is_accepted(self):
        import shutil
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rels = (
                R6_AUTHORIZATION_REF,
                R6_APPROVED_REVISION_REF,
                "docs/template-factory/g1-r6-source-alignment-2026-10-20/patch.json",
            )
            for rel in rels:
                target = root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                source = Path(__file__).resolve().parents[2] / rel
                shutil.copy(source, target)
            auth = {"source_ref": R6_AUTHORIZATION_REF,
                    "source_digest": R6_AUTHORIZATION_SHA256,
                    "revision_ref": R6_APPROVED_REVISION_REF,
                    "revision_digest": digest(json.loads((root / R6_APPROVED_REVISION_REF).read_text()))}
            approved = json.loads((root / rels[2]).read_text())
            result = _validate_approved_r6_patch(root, auth, approved)
            self.assertEqual(result, approved)
            effective = _apply_r6_patch(self.plan, result)
            report = feature_source_reference_report(effective["spec"], self._eligible_sources())
            self.assertTrue(report["valid"], report["errors"])

            tampered = json.loads(json.dumps(approved))
            tampered["spec_changes"][7]["new"] += " 改写"
            with self.assertRaises(FactoryError):
                _validate_approved_r6_patch(root, auth, tampered)

            revision_path = root / R6_APPROVED_REVISION_REF
            revision_path.write_text(revision_path.read_text().replace("Exact host", "Changed host"))
            with self.assertRaises(FactoryError):
                _validate_approved_r6_patch(root, auth, approved)

    def test_program_reuse_binds_all_nine_checkpoint_bytes_and_detects_tampering(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generated = root / "jobs" / "job_7742b1c124be4c9ab3a0096da5cdd772" / "attempt-4" / "context" / "generated-0"
            generated.mkdir(parents=True)
            inputs = root / "jobs" / "job_7742b1c124be4c9ab3a0096da5cdd772" / "attempt-4"
            for index, path in enumerate(R6_PROGRAM_PATHS):
                result = self.rows[f"blueprint-code-0-{index}"]["result"]
                target = generated / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(result["content"].encode("utf-8"))
                if "reused_sha256" not in result:
                    input_file = inputs / f"blueprint-code-0-{index}" / "input.json"
                    input_file.parent.mkdir(parents=True, exist_ok=True)
                    input_file.write_text("{}", encoding="utf-8")
            store = _Store(root, self.rows)
            manifest = build_program_reuse_manifest(store)
            contents = program_reuse_contents(store, manifest)
            self.assertEqual(set(contents), set(R6_PROGRAM_PATHS))
            self.assertEqual(len(manifest["entries"]), 9)
            self.assertEqual(sum(row["input_digest"] is None for row in manifest["entries"]), 4)
            tampered = generated / R6_PROGRAM_PATHS[0]
            tampered.write_bytes(tampered.read_bytes() + b"\n")
            with self.assertRaises(FactoryError):
                program_reuse_contents(store, manifest)

    def test_checkpoint_result_tampering_is_rejected_without_expected_digest(self):
        rows = {"blueprint-research": json.loads(json.dumps(self.rows["blueprint-research"]))}
        rows["blueprint-research"]["result"]["summary"] += " tampered"
        store = _Store(Path("/tmp"), rows)
        with self.assertRaises(FactoryError):
            _checkpoint_result(store, "job_7742b1c124be4c9ab3a0096da5cdd772", "blueprint-research")

    def test_research_checkpoint_self_rehash_does_not_rebind_facts_view(self):
        research = json.loads(json.dumps(self.rows["blueprint-research"]))
        research["result"]["summary"] += " edited and rehashed"
        research["digest"] = digest(research["result"])
        with self.assertRaises(FactoryError):
            _validate_research_view_binding(self.facts, research)

    def test_case_design_checkpoint_cannot_drift_with_matching_request_digest(self):
        source = json.loads((DOCS / "actual-structural-stop.json").read_text())
        snapshot = source["job"]["snapshot"]
        if isinstance(snapshot, str):
            snapshot = json.loads(snapshot)
        name = "case-adaptation-prepared-aaf080ba52611126"
        record = json.loads(json.dumps(self.rows[name]))
        _validate_pinned_case_design(snapshot, name, record)

        record["result"]["choices"][0]["reason"] += " drift"
        record["digest"] = digest(record["result"])
        with self.assertRaises(FactoryError):
            _validate_pinned_case_design(snapshot, name, record)


if __name__ == "__main__":
    unittest.main()
