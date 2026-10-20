"""Positive R7 production-pipeline link with temporary state and a no-provider CLI."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from test_factory_r6_link import FreshReviewFixtureCLI, StopAtAggregateReview
from template_factory.cognition import queue_repair
from template_factory.plan_revision import (
    R7_AUTHORIZATION_REF, R7_APPROVED_REVISION_REF, R7_PATCH_REF,
    R7_PROGRAMS_REF, R7_PROGRAM_PATHS, R7_REPLACE_PATHS, R7_SOURCE_JOB,
    PreparedRevisionService, program_revision_contents,
)
from template_factory.pipeline import Pipeline
from template_factory.store import canonical, digest
from template_factory.v1_batches import BatchService

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parent
R6_DOCS = ROOT / "docs/template-factory/g1-r6-source-alignment-2026-10-20"
R7_DOCS = ROOT / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20"


class R7ReviewFixtureCLI(FreshReviewFixtureCLI):
    def __init__(self, expected_proposal_digest, expected_program_hashes, manifest, authorization):
        super().__init__(expected_proposal_digest, expected_program_hashes)
        self.expected_manifest = manifest
        self.expected_authorization = authorization
        self.aggregate_prompt = None

    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        if Path(directory).name == "aggregate-semantic-review":
            self.aggregate_prompt = prompt
        return super().run(directory, prompt, model, timeout, cancelled, on_progress, **kwargs)

    def assert_aggregate_materials(self, directory, payload):
        diff = payload.get("exact_diff")
        if not isinstance(diff, dict):
            raise AssertionError("aggregate review did not receive exact diff")
        before = diff.get("program_file_hashes_before")
        after = diff.get("program_file_hashes_after")
        if set(before or {}) != set(R7_PROGRAM_PATHS) or set(after or {}) != set(R7_PROGRAM_PATHS):
            raise AssertionError("aggregate program inventory is not the exact nine files")
        incremental = diff.get("r7_incremental_diff")
        if not isinstance(incremental, dict):
            raise AssertionError("aggregate diff omitted R7 incremental proof")
        if (set(incremental.get("replaced_paths", [])) != R7_REPLACE_PATHS
                or len(incremental.get("reused_paths", [])) != 5
                or incremental.get("program_byte_change_count") != 4
                or set(incremental.get("program_file_hashes_after", {})) != set(R7_PROGRAM_PATHS)
                or incremental.get("program_file_hashes_after") != self.expected_program_hashes
                or after != self.expected_program_hashes
                or set(incremental.get("program_diffs", {})) != R7_REPLACE_PATHS):
            raise AssertionError("R7 incremental proof differs from four replacements and five reuses")
        if incremental.get("program_revision_manifest_digest") != digest(self.expected_manifest):
            raise AssertionError("R7 incremental proof is detached from the prepared program manifest")
        authorization_digest = digest({key: value for key, value in self.expected_authorization.items() if key != "files"})
        if (incremental.get("authorization_material_digest") != authorization_digest
                or payload.get("identity", {}).get("r7_authorization_material_digest") != authorization_digest):
            raise AssertionError("R7 authorization materials are not bound into aggregate identity")
        metadata = diff.get("generated_metadata", {}).get("files", {}).get("acceptance/plan.json")
        if (not isinstance(metadata, dict) or metadata.get("role") != "host-generated-acceptance-plan-metadata"
                or not metadata.get("changed") or not metadata.get("unified_diff")):
            raise AssertionError("generated acceptance metadata is not separately disclosed")
        candidate = directory / "source/candidate"
        r6_baseline = directory / "source/r6-baseline"
        if {str(path.relative_to(r6_baseline)) for path in r6_baseline.rglob("*") if path.is_file()
            and str(path.relative_to(r6_baseline)).startswith("acceptance/")} != set(R7_PROGRAM_PATHS):
            raise AssertionError("aggregate source lacks the exact R6 attempt-1 nine-program baseline")
        for path, expected_hash in incremental["program_file_hashes_before"].items():
            if hashlib.sha256((r6_baseline / path).read_bytes()).hexdigest() != expected_hash:
                raise AssertionError("R6 baseline file differs from incremental source digest: " + path)
        for rel, expected in self.expected_authorization["files"].items():
            if (directory / "source" / rel).read_bytes() != expected:
                raise AssertionError("aggregate source omitted or changed R7 authorization evidence: " + rel)
        actual_manifest = json.loads((directory / "source/authorization/PROGRAM_REVISION_MANIFEST.json").read_text())
        if actual_manifest != self.expected_manifest:
            raise AssertionError("aggregate source manifest differs from the prepared program revision")
        saved_incremental = json.loads((candidate / "inputs/r7-incremental-diff.json").read_text())
        if saved_incremental != incremental:
            raise AssertionError("candidate does not carry the exact R7 incremental proof")
        actual = {path: hashlib.sha256((candidate / path).read_bytes()).hexdigest()
                  for path in R7_PROGRAM_PATHS}
        if actual != self.expected_program_hashes:
            raise AssertionError("rendered candidate hashes differ from prepared R7 bytes")
        for side, key in (("baseline", "baseline_sha256"), ("candidate", "candidate_sha256")):
            path = directory / "source" / side / "generated-metadata/acceptance/plan.json"
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != metadata[key]:
                raise AssertionError("generated metadata source is missing or has the wrong hash")


class R7PositivePipelineLinkTests(unittest.TestCase):
    def setUp(self):
        self.base = r5_fixture.R5PreparedLinkTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.tearDown)
        self.store = self.base.store
        self.root = self.base.root
        self._install_r7_source_evidence()

    def _install_r7_source_evidence(self):
        baseline = json.loads((R7_DOCS / "BASELINE.json").read_text())
        job = baseline["job"]
        for rel in (R7_AUTHORIZATION_REF, R7_APPROVED_REVISION_REF, R7_PATCH_REF):
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, target)
        disposition = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/FINDINGS_DISPOSITION.json"
        target = self.root / disposition
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / disposition, target)
        target_programs = self.root / R7_PROGRAMS_REF
        if target_programs.exists():
            shutil.rmtree(target_programs)
        shutil.copytree(ROOT / R7_PROGRAMS_REF, target_programs)

        original = R6_DOCS / "candidate-attempt-1-not-frozen"
        source_attempt = self.store.root / "jobs" / R7_SOURCE_JOB / "attempt-1"
        generated = source_attempt / "context/generated-0"
        generated.mkdir(parents=True, exist_ok=True)
        for path in R7_PROGRAM_PATHS:
            destination = generated / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original / path, destination)
        candidate = source_attempt / "candidate-0/template.json"
        candidate.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original / "template.json", candidate)

        with self.store.connect(True) as con:
            con.execute("UPDATE job SET id=?,state='failed',stage=?,attempt=1,token=NULL,lease=NULL,snapshot=?,error=?,updated_at=? WHERE id=?",
                        (R7_SOURCE_JOB, job["stage"], canonical(job["snapshot"]),
                         canonical(job["error"]) if not isinstance(job["error"], str) else job["error"],
                         job.get("updated_at", job.get("created_at")), r5_fixture.JOB_ID))
            con.execute("DELETE FROM checkpoint WHERE job_id IN (?,?)", (r5_fixture.JOB_ID, R7_SOURCE_JOB))
            for row in baseline["checkpoints"]:
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (R7_SOURCE_JOB, row["name"], row["body"]))

    def test_r7_uses_four_prepared_replacements_five_reuses_six_fresh_reviews_and_reaches_aggregate(self):
        request = json.loads((R7_DOCS / "prepare-request.json").read_text())
        prepared = PreparedRevisionService(self.store).prepare(R7_SOURCE_JOB, request)
        self.assertEqual(prepared["state"], "prepared_not_queued")
        self.assertEqual(len(prepared["incremental_diff"]["spec_changes"]), 16)
        contents = program_revision_contents(self.store, prepared["prepared_program_revision"])
        self.assertEqual(set(contents), set(R7_PROGRAM_PATHS))
        expected_hashes = {path: hashlib.sha256(content.encode("utf-8")).hexdigest()
                           for path, content in contents.items()}
        entries = {row["path"]: row for row in prepared["prepared_program_revision"]["entries"]}
        self.assertEqual({path for path, row in entries.items() if row["mode"] == "replace"}, R7_REPLACE_PATHS)

        artifact = next(row for row in self.store.artifacts() if row["id"] == r5_fixture.ARTIFACT_ID)
        old_snapshot = self.store.job(R7_SOURCE_JOB)["snapshot"]
        repair = {
            "expected_digest": artifact["digest"],
            "note": "Apply the fixed R7 acceptance alignment and consume its prepared four replacements plus five exact R6 bytes.",
            "edit_paths": prepared["cumulative_repair_scope"]["edit_paths"],
            "repair_scope": prepared["cumulative_repair_scope"],
            "reuse_spec": False,
            "spec_edit_paths": None,
            "prepared_revision": request,
            "model": old_snapshot["config"]["model"],
            "language": old_snapshot["config"]["language"],
            "timeout": old_snapshot["config"]["timeout"],
        }

        class NoBudgetWrites:
            def record_repair(self, *args, **kwargs):
                return {"fixture_only": True}

        queued = queue_repair(self.store, artifact, repair, parent_state_override="running", ledger=NoBudgetWrites())
        child_id = queued["jobs"][0]["id"]
        BatchService(self.store).action(old_snapshot["v1"]["plan_id"], "resume")
        child = self.store.claim("r7-positive-fixture")
        self.assertEqual(child["id"], child_id)

        source_authorization = request["source_authorization"]
        authorization = {
            "source_ref": source_authorization["source_ref"],
            "source_sha256": source_authorization["source_digest"],
            "revision_ref": source_authorization["revision_ref"],
            "revision_digest": source_authorization["revision_digest"],
            "patch_ref": "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/patch.json",
            "patch_digest": digest(request["patch"]),
            "program_manifest_digest": digest(prepared["prepared_program_revision"]),
        }
        authorization["files"] = {
            "authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt": (self.root / source_authorization["source_ref"]).read_bytes(),
            "authorization/approved-revision.json": (self.root / source_authorization["revision_ref"]).read_bytes(),
            "authorization/patch.json": (self.root / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/patch.json").read_bytes(),
        }
        cli = R7ReviewFixtureCLI(prepared["effective_plan_digest"], expected_hashes,
                                 prepared["prepared_program_revision"], authorization)
        with self.assertRaises(StopAtAggregateReview):
            Pipeline(self.store, cli=cli).run(child)

        dimensions = [payload["review_dimensions"][0] for payload in cli.review_payloads]
        self.assertEqual(set(dimensions), {
            "scenario_scope", "product_completeness", "architecture_contract",
            "phase_acceptance", "decisions_defaults", "runtime_protocol",
        })
        self.assertEqual(len(dimensions), 6)
        self.assertEqual(len(cli.calls), 7)
        self.assertFalse(any("blueprint-code" in name or "blueprint-research" in name or "case-adaptation" in name for name in cli.calls))
        self.assertTrue(cli.calls[-1].startswith("aggregate-semantic-review"))
        self.assertIn("copy every key from input.identity exactly", cli.aggregate_prompt)
        self.assertIn("r7_authorization_material_digest", cli.aggregate_prompt)
        self.assertIn("source/authorization/", cli.aggregate_prompt)
        self.assertIn("source/r6-baseline/", cli.aggregate_prompt)

        runroot = self.store.root / "jobs" / child["id"] / "attempt-1"
        self.assertTrue((runroot / "context/PREPARED_PROGRAM_REVISION.json").is_file())
        source_report = json.loads((runroot / "context/SOURCE_REFERENCE_REPORT.json").read_text())
        self.assertTrue(source_report["valid"])
        self.assertEqual(source_report["binding"]["case_basis_digest"], old_snapshot["case_basis"]["basis_digest"])
        adaptation = json.loads((runroot / "context/CASE_DESIGN.json").read_text())
        self.assertEqual(adaptation, prepared["case_design"])
        for path in R7_PROGRAM_PATHS:
            self.assertEqual(hashlib.sha256((runroot / "aggregate-semantic-review-source/candidate" / path).read_bytes()).hexdigest(), expected_hashes[path])
        self.assertEqual(self.store.job(R7_SOURCE_JOB)["state"], "failed")


if __name__ == "__main__":
    unittest.main()
