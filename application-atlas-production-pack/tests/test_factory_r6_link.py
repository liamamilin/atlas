"""Positive R6 pipeline link against the archived G1 attempt-4 evidence."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from template_factory.cognition import queue_repair
from template_factory.plan_revision import (
    R6_AUTHORIZATION_REF,
    R6_APPROVED_REVISION_REF,
    R6_PROGRAM_PATHS,
    R6_SOURCE_JOB,
    R6_PREPARATION_SCHEMA,
    PreparedRevisionService,
    build_program_reuse_manifest,
)
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, canonical, digest
from template_factory.v1_batches import BatchService

DOCS = Path(__file__).resolve().parents[2] / "docs/template-factory"
R6_DOCS = DOCS / "g1-r6-source-alignment-2026-10-20"
R5_DOCS = DOCS / "g1-protocol-recovery-2026-10-19"


class StopAtAggregateReview(Exception):
    """The fixture has reached real aggregate review inputs; no provider used."""


class FreshReviewFixtureCLI:
    def __init__(self, expected_proposal_digest, expected_program_hashes):
        self.expected_proposal_digest = expected_proposal_digest
        self.expected_program_hashes = expected_program_hashes
        self.review_payloads = []
        self.aggregate_payload = None
        self.calls = []

    def info(self):
        return {"kind": "fixture-only", "provider_called": False}

    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        directory = Path(directory)
        name = directory.name
        payload = json.loads((directory / "input.json").read_text())
        self.calls.append(name)
        if name.startswith("blueprint-spec-review-"):
            self.assert_review_materials(directory, payload)
            dimension = payload["review_dimensions"][0]
            self.review_payloads.append(payload)
            cited = ["DRAFT.md"]
            if dimension == "architecture_contract":
                cited.extend(["SOURCE_MANIFEST.json", "SOURCE_CITATION_MATRIX.json"])
            return {
                "summary": "Fresh temporary review fixture; no model or provider was called.",
                "checks": [{
                    "dimension": dimension,
                    "outcome": "passed",
                    "files": cited,
                    "reason": "Fixture response for this new R6 projection identity.",
                }],
                "suggestions": [],
            }
        if name == "aggregate-semantic-review":
            self.aggregate_payload = payload
            self.assert_aggregate_materials(directory, payload)
            raise StopAtAggregateReview
        raise AssertionError("unexpected model-backed stage before aggregate review: " + name)

    def assert_review_materials(self, directory, payload):
        if payload.get("proposal_digest") != self.expected_proposal_digest:
            raise AssertionError("review is not bound to the prepared R6 proposal")
        source = directory / "source"
        manifest = json.loads((source / "SOURCE_MANIFEST.json").read_text())
        matrix = json.loads((source / "SOURCE_CITATION_MATRIX.json").read_text())
        shared_context = directory.parent / "context"
        if ((shared_context / "SOURCE_MANIFEST.json").read_bytes()
                != (source / "SOURCE_MANIFEST.json").read_bytes()
                or (shared_context / "SOURCE_CITATION_MATRIX.json").read_bytes()
                != (source / "SOURCE_CITATION_MATRIX.json").read_bytes()):
            raise AssertionError("shared context and reviewer projection source bytes differ")
        manifest_rows = manifest.get("sources", manifest if isinstance(manifest, list) else None)
        if not isinstance(manifest_rows, list):
            raise AssertionError("source manifest is missing its source rows")
        ids = [row.get("id") for row in manifest_rows]
        if ids != ["S01", "S02", "S03", "S04", "S06", "S07", "S12", "S13", "S14", "S15", "S16", "S19", "S20", "S21"]:
            raise AssertionError("new projection must include exactly the 14 current sources")
        if any(row.get("facts_view_digest") != manifest.get("facts_view_digest") for row in manifest_rows):
            raise AssertionError("source manifest detached from the accepted facts view")
        if not isinstance(matrix, dict) or not matrix.get("features"):
            raise AssertionError("source citation matrix is missing")
        if not {"SOURCE_MANIFEST.json", "SOURCE_CITATION_MATRIX.json"}.issubset(
                set(payload.get("source_inventory", []))):
            raise AssertionError("source references were not made available to the reviewer")
        draft = (source / "DRAFT.md").read_text()
        if (digest(manifest) not in draft or "source_citation_matrix" not in draft
                or matrix["facts_view_digest"] not in draft):
            raise AssertionError("source manifest and citation matrix are not in the hashed review projection")

    def assert_aggregate_materials(self, directory, payload):
        diff = payload.get("exact_diff")
        if not isinstance(diff, dict):
            raise AssertionError("aggregate review did not receive the exact rendered diff")
        incremental = diff.get("r6_incremental_diff")
        if not isinstance(incremental, dict) or incremental.get("program_byte_changes") != 0:
            raise AssertionError("aggregate diff lacks the zero-change R6 incremental proof")
        if incremental.get("prepared_effective_plan_digest") != self.expected_proposal_digest:
            raise AssertionError("aggregate diff is not bound to the prepared R6 proposal")
        before = incremental.get("program_file_hashes_before")
        after = incremental.get("program_file_hashes_after")
        if before != after or before != self.expected_program_hashes:
            raise AssertionError("incremental diff does not prove all nine archived program bytes")
        candidate = directory / "source/candidate"
        actual = {}
        for path in R6_PROGRAM_PATHS:
            raw = (candidate / path).read_bytes()
            actual[path] = hashlib.sha256(raw).hexdigest()
        if actual != self.expected_program_hashes:
            raise AssertionError("rendered candidate differs from the attempt-4 program bytes")


class R6PositivePipelineLinkTests(unittest.TestCase):
    def setUp(self):
        self.base = r5_fixture.R5PreparedLinkTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.tearDown)
        self.store = self.base.store
        self.root = self.base.root
        self._install_r6_source_evidence()

    def _install_r6_source_evidence(self):
        baseline = json.loads((R6_DOCS / "BASELINE.json").read_text())
        job = baseline["job"]
        snapshot = job["snapshot"]
        self.assertTrue(snapshot["v1"]["campaign_id"])

        # Supply the exact approved authorization and revision bytes in the
        # temporary project root expected by PreparedRevisionService.
        for rel in (R6_AUTHORIZATION_REF,
                    R6_APPROVED_REVISION_REF,
                    "docs/template-factory/g1-r6-source-alignment-2026-10-20/patch.json"):
            target = self.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(Path(__file__).resolve().parents[2] / rel, target)

        # Replace only the temporary source-job row and its checkpoints with
        # the exact archived attempt-4 baseline. The shared case library and
        # frozen original artifact are installed by the existing R5 fixture.
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET id=?,state='failed',stage=?,attempt=4,token=NULL,lease=NULL,snapshot=?,error=?,updated_at=? WHERE id=?",
                        (R6_SOURCE_JOB, job["stage"], canonical(snapshot), canonical(job["error"]), job["updated_at"], r5_fixture.JOB_ID))
            con.execute("DELETE FROM checkpoint WHERE job_id IN (?,?)", (r5_fixture.JOB_ID, R6_SOURCE_JOB))
            for row in baseline["checkpoints"]:
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (R6_SOURCE_JOB, row["name"], row["body"]))

        # Bind the original attempt-4 file bytes and successful author inputs.
        candidate = R5_DOCS / "candidate-attempt-4-not-frozen"
        generated = self.store.root / "jobs" / R6_SOURCE_JOB / "attempt-4/context/generated-0"
        generated.mkdir(parents=True, exist_ok=True)
        for relative in R6_PROGRAM_PATHS:
            target = generated / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(candidate / relative, target)
        archived_inputs = R5_DOCS / "actual-attempt-4"
        attempt_dir = self.store.root / "jobs" / R6_SOURCE_JOB / "attempt-4"
        for index in range(9):
            source_input = archived_inputs / f"blueprint-code-0-{index}/input.json"
            if source_input.is_file():
                target = attempt_dir / f"blueprint-code-0-{index}/input.json"
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source_input, target)

    def _request(self):
        snapshot = self.store.job(R6_SOURCE_JOB)["snapshot"]
        plan = self.store.checkpoint(R6_SOURCE_JOB, "blueprint-plan-0")
        facts = self.store.checkpoint(R6_SOURCE_JOB, "blueprint-accepted-facts-view")
        design_name = "case-adaptation-prepared-aaf080ba52611126"
        design = self.store.checkpoint(R6_SOURCE_JOB, design_name)
        authorization_source = json.loads((R6_DOCS / "authorization-source.json").read_text())
        binding = {
            "job_id": R6_SOURCE_JOB,
            "attempt": 4,
            "snapshot_digest": digest(snapshot),
            "checkpoint_name": "blueprint-plan-0",
            "checkpoint_digest": plan["digest"],
            "plan_id": snapshot["v1"]["plan_id"],
            "plan_digest": snapshot["v1"]["plan_digest"],
            "product_id": snapshot["v1"]["product_id"],
            "scenario_id": snapshot["scenario"]["id"],
            "scenario_revision": snapshot["scenario"]["revision"],
            "case_basis_digest": snapshot["case_basis"]["basis_digest"],
            "facts_view_checkpoint_name": "blueprint-accepted-facts-view",
            "facts_view_checkpoint_digest": facts["digest"],
            "facts_view_digest": facts["result"]["view_digest"],
            "case_design_checkpoint_name": design_name,
            "case_design_checkpoint_digest": design["digest"],
            "original_proposal_digest": plan["digest"],
        }
        authorization = {
            "source_ref": authorization_source["source_ref"],
            "source_digest": authorization_source["source_sha256"],
            "revision_ref": R6_APPROVED_REVISION_REF,
            "revision_digest": digest(json.loads((R6_DOCS / "authorization/approved-revision.json").read_text())),
        }
        return {
            "schema": R6_PREPARATION_SCHEMA,
            "binding": binding,
            "patch": json.loads((R6_DOCS / "patch.json").read_text()),
            "source_authorization": authorization,
            "program_reuse_manifest": build_program_reuse_manifest(self.store, R6_SOURCE_JOB),
        }

    def test_prepared_r6_runs_all_new_design_reviews_reuses_nine_programs_and_renders(self):
        request = self._request()
        prepared = PreparedRevisionService(self.store).prepare(R6_SOURCE_JOB, request)
        self.assertEqual(prepared["state"], "prepared_not_queued")
        self.assertEqual(len(prepared["incremental_diff"]["spec_changes"]), 21)
        expected_hashes = {entry["path"]: entry["sha256"] for entry in prepared["prepared_program_reuse"]["entries"]}

        artifact = next(row for row in self.store.artifacts() if row["id"] == r5_fixture.ARTIFACT_ID)
        old_snapshot = self.store.job(R6_SOURCE_JOB)["snapshot"]
        repair = {
            "expected_digest": artifact["digest"],
            "note": "Apply only the approved R6 source-alignment patch and reuse the nine attempt-4 program files.",
            "edit_paths": old_snapshot["cognitive_repair"]["edit_paths"],
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
        self.assertEqual(len(queued["jobs"]), 1)
        child_id = queued["jobs"][0]["id"]
        BatchService(self.store).action(old_snapshot["v1"]["plan_id"], "resume")
        child = self.store.claim("r6-positive-fixture")
        self.assertEqual(child["id"], child_id)

        cli = FreshReviewFixtureCLI(prepared["effective_plan_digest"], expected_hashes)
        with self.assertRaises(StopAtAggregateReview):
            Pipeline(self.store, cli=cli).run(child)

        dimensions = [payload["review_dimensions"][0] for payload in cli.review_payloads]
        self.assertEqual(set(dimensions), {
            "scenario_scope", "product_completeness", "architecture_contract",
            "phase_acceptance", "decisions_defaults", "runtime_protocol",
        })
        self.assertEqual(len(dimensions), 6)
        self.assertEqual(len(cli.calls), 7)
        self.assertTrue(all(name.startswith("blueprint-spec-review-0-") for name in cli.calls[:6]))
        self.assertTrue(cli.calls[-1].startswith("aggregate-semantic-review"))
        self.assertFalse(any("blueprint-code" in name or "blueprint-research" in name or "case-adaptation" in name for name in cli.calls))
        self.assertEqual(cli.aggregate_payload["exact_diff"]["r6_incremental_diff"]["prepared_effective_plan_digest"],
                         prepared["effective_plan_digest"])

        runroot = self.store.root / "jobs" / child["id"] / "attempt-1"
        self.assertTrue((runroot / "context/PREPARED_PROGRAM_REUSE.json").is_file())
        self.assertTrue((runroot / "aggregate-semantic-review-source/candidate/acceptance/common.py").is_file())
        source_report = json.loads((runroot / "context/SOURCE_REFERENCE_REPORT.json").read_text())
        self.assertEqual(source_report["binding"]["case_basis_digest"],
                         old_snapshot["case_basis"]["basis_digest"])
        self.assertEqual(self.store.job(R6_SOURCE_JOB)["state"], "failed")
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM checkpoint WHERE job_id=?", (R6_SOURCE_JOB,)).fetchone()[0], 20)


if __name__ == "__main__":
    unittest.main()
