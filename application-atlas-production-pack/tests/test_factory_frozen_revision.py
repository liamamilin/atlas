"""End-to-end isolation checks for authorized frozen revision preparation."""
from __future__ import annotations

import copy
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PACK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACK))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from frozen_revision_fixture import FrozenRevisionFixture, R7, R8  # noqa: E402
from template_factory.frozen_revision import PROGRAM_PATHS, REPLACE_PATHS, program_contents  # noqa: E402
from template_factory.plan_revision import PreparedRevisionService  # noqa: E402
from template_factory.store import FactoryError, digest  # noqa: E402
from template_factory.budget import BudgetAmendmentService  # noqa: E402
from template_factory.product_recovery import ProductRecoveryService  # noqa: E402


class FrozenRevisionPreparationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = FrozenRevisionFixture()
        self.fixture.setUp()
        self.store = self.fixture.store
        self.request = self.fixture.request

    def tearDown(self):
        self.fixture.base.doCleanups()

    def test_dispatch_prepares_exact_four_replacements_and_five_reuses_read_only(self):
        before = self.store.job(self.request["binding"]["job_id"])
        with self.store.connect() as con:
            ledger = tuple(con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=?", (self.request["binding"]["campaign_id"],)).fetchone())
            repairs = tuple(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=?", (self.request["binding"]["campaign_id"],)).fetchone())
        prepared = PreparedRevisionService(self.store).prepare(before["id"], self.request)
        self.assertEqual(prepared["state"], "prepared_not_queued")
        entries = prepared["prepared_program_revision"]["entries"]
        self.assertEqual(len(entries), 9)
        self.assertEqual({r["path"] for r in entries if r["mode"] == "replace"}, REPLACE_PATHS)
        self.assertEqual({r["path"] for r in entries if r["mode"] == "reuse"}, set(PROGRAM_PATHS) - REPLACE_PATHS)
        self.assertEqual(self.store.job(before["id"]), before)
        with self.store.connect() as con:
            self.assertEqual(tuple(con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=?", (self.request["binding"]["campaign_id"],)).fetchone()), ledger)
            self.assertEqual(tuple(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=?", (self.request["binding"]["campaign_id"],)).fetchone()), repairs)

    def test_dispatch_rejects_mutated_authority_identity_and_old_schemas(self):
        service = PreparedRevisionService(self.store)
        for mutate in (
            lambda r: r["source_authorization"].update(source_digest="0" * 64),
            lambda r: r["patch"]["program_changes"].pop(),
            lambda r: r["binding"].update(case_basis_digest="0" * 64),
        ):
            changed = copy.deepcopy(self.request)
            mutate(changed)
            with self.subTest(mutate=mutate), self.assertRaises(FactoryError):
                service.prepare(changed["binding"]["job_id"], changed)
        for schema in ("atlas.plan-revision.v1", "atlas.prepared-revision.v1", "atlas.frozen-program-revision.v1"):
            changed = copy.deepcopy(self.request)
            changed["schema"] = schema
            with self.subTest(schema=schema), self.assertRaises(FactoryError):
                service.prepare(self.request["binding"]["job_id"], changed)

    def test_review_evidence_has_source_and_prepared_bytes_for_all_nine_paths(self):
        from template_factory.frozen_revision import prepare, review_evidence
        prepared = prepare(self.store, self.request["binding"]["job_id"], self.request)
        contents = program_contents(self.store, prepared["prepared_program_revision"])
        evidence = review_evidence(self.store, prepared, self.request, contents)
        expected = {"program-evidence/source/" + p for p in PROGRAM_PATHS} | {"program-evidence/prepared/" + p for p in PROGRAM_PATHS}
        self.assertTrue(expected.issubset(evidence["files"]))
        for path in PROGRAM_PATHS:
            entry = next(e for e in prepared["prepared_program_revision"]["entries"] if e["path"] == path)
            self.assertEqual(hashlib.sha256(evidence["files"]["program-evidence/source/" + path]).hexdigest(), entry["before_sha256"])
            self.assertEqual(hashlib.sha256(evidence["files"]["program-evidence/prepared/" + path]).hexdigest(), entry["after_sha256"])
        self.assertEqual(contents["acceptance/p0_library.py"].encode(),
                         (R8 / "prepared-programs/acceptance/p0_library.py").read_bytes())

    def _budget_request(self, prepared):
        approved = json.loads((R8 / "authorization/approved-revision.json").read_text())
        source = self.request["source_authorization"]
        return {
            "schema": "atlas.budget-amendment.v3",
            "campaign_id": self.request["binding"]["campaign_id"],
            "product_id": self.request["binding"]["product_id"],
            "plan_id": self.request["binding"]["plan_id"],
            "source_ref": source["source_ref"], "source_digest": source["source_digest"],
            "summary": "Authorized R8 frozen contract convergence window",
            "reason": "Resume exactly one frozen candidate revision",
            "idempotency_key": "test-r8-register-once",
            "source_gate": {"fixture": "source-gate validator mocked at its external CI evidence boundary"},
            "limits": approved["limits"], "timing": approved["timing"],
            "prepared_revision": self.request,
            "prepared_revision_digest": prepared["request_digest"],
            "effective_plan_digest": prepared["effective_plan_digest"],
            "case_design_digest": prepared["case_design_digest"],
            "program_revision_digest": digest(prepared["prepared_program_revision"]),
        }

    def _resume_request(self, prepared, amendment_id):
        scope = prepared["cumulative_repair_scope"]
        return {
            "schema": "atlas.product-resume.v4",
            "old_job_id": self.request["binding"]["job_id"],
            "artifact_id": self.request["binding"]["artifact_id"],
            "expected_digest": self.request["binding"]["artifact_digest"],
            "amendment_id": amendment_id,
            "idempotency_key": "test-r8-resume-once",
            "repair": {"expected_digest": self.request["binding"]["artifact_digest"],
                       "note": "test frozen revision queue", "edit_paths": scope["edit_paths"],
                       "repair_scope": scope, "reuse_spec": False,
                       "prepared_revision": self.request,
                       **self.request["review_config"]},
        }

    def test_real_register_resume_replay_and_queue_failure_rollback(self):
        prepared = PreparedRevisionService(self.store).prepare(self.request["binding"]["job_id"], self.request)
        budget = BudgetAmendmentService(self.store, campaign_id=self.request["binding"]["campaign_id"],
                                        clock=lambda: 1792497000.0)
        gate_patch = patch("template_factory.evidence_recovery.validate_source_gate", return_value={"fixture": True})
        gate_patch.start()
        self.addCleanup(gate_patch.stop)
        amendment = budget.register_frozen_revision(self._budget_request(prepared))
        amendment_replay = budget.register_frozen_revision(self._budget_request(prepared))
        self.assertEqual(amendment["id"], amendment_replay["id"])
        resume = self._resume_request(prepared, amendment["id"])
        old_before = self.store.job(resume["old_job_id"])
        acceptance_before = json.loads((R7 / "actual-attempt-3/acceptance.json").read_text())
        with self.store.connect() as con:
            calls_before = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (self.request["binding"]["campaign_id"],)).fetchone()[0]
            repairs_before = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (self.request["binding"]["campaign_id"], self.request["binding"]["product_id"])).fetchone()[0]
        self.assertEqual(calls_before + 1, 83)
        self.assertEqual(repairs_before, 7)

        from template_factory import cognition
        original_queue = cognition.queue_repair
        def queue_then_fail(*args, **kwargs):
            original_queue(*args, **kwargs)
            raise RuntimeError("injected failure after real queue insertion")
        with patch("template_factory.cognition.queue_repair", side_effect=queue_then_fail), \
             self.assertRaises(RuntimeError):
            ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
                self.request["binding"]["plan_id"], resume)
        with self.store.connect() as con:
            state = con.execute("SELECT activated_at,new_deadline FROM tf_budget_amendment WHERE id=?", (amendment["id"],)).fetchone()
            self.assertIsNone(state["activated_at"])
            self.assertIsNone(state["new_deadline"])
            self.assertIsNone(con.execute("SELECT 1 FROM tf_product_resume WHERE old_job_id=?", (resume["old_job_id"],)).fetchone())
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (self.request["binding"]["campaign_id"], self.request["binding"]["product_id"])).fetchone()[0], 7)
        self.assertEqual(self.store.job(resume["old_job_id"]), old_before)

        result = ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
            self.request["binding"]["plan_id"], resume)
        self.assertEqual(result["schema"], "atlas.product-resume-result.v4")
        self.assertTrue(result["parent_remains_paused"])
        self.assertTrue(result["old_review_preserved"])
        self.assertEqual(result["effective_deadline"] - result["activated_at"], 86400)
        successor = self.store.job(result["successor_job_id"])
        self.assertEqual(successor["snapshot"]["config"]["model"], "opencode-go/deepseek-v4.1-flash")
        self.assertEqual(successor["snapshot"]["config"]["timeout"], 1800)
        self.assertEqual(successor["snapshot"]["config"]["repair_attempts"], 0)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume WHERE plan_id=?", (self.request["binding"]["plan_id"],)).fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (self.request["binding"]["campaign_id"], self.request["binding"]["product_id"])).fetchone()[0], 8)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (self.request["binding"]["campaign_id"],)).fetchone()[0], calls_before)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM job WHERE batch_id=(SELECT successor_batch_id FROM tf_product_resume WHERE old_job_id=?)", (resume["old_job_id"],)).fetchone()[0], 1)
            stored_acceptance = con.execute("SELECT body FROM acceptance WHERE id=?", (acceptance_before["id"],)).fetchone()
            self.assertEqual(json.loads(stored_acceptance["body"]), acceptance_before)
        replay = ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
            self.request["binding"]["plan_id"], resume)
        self.assertTrue(replay["replayed"])
        self.assertEqual(replay["successor_job_id"], result["successor_job_id"])
        def concurrent_replay(_):
            return ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
                self.request["binding"]["plan_id"], copy.deepcopy(resume))
        with ThreadPoolExecutor(max_workers=2) as executor:
            raced = list(executor.map(concurrent_replay, range(2)))
        self.assertTrue(all(row["replayed"] for row in raced))
        self.assertEqual({row["successor_job_id"] for row in raced}, {result["successor_job_id"]})
        conflict = copy.deepcopy(resume)
        conflict["repair"]["note"] = "different approved payload"
        with self.assertRaises(FactoryError):
            ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
                self.request["binding"]["plan_id"], conflict)
        conflict = copy.deepcopy(resume)
        conflict["idempotency_key"] = "another-key-for-same-candidate"
        with self.assertRaises(FactoryError):
            ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
                self.request["binding"]["plan_id"], conflict)

    def test_registered_revision_rechecks_baseline_before_activation(self):
        prepared = PreparedRevisionService(self.store).prepare(self.request["binding"]["job_id"], self.request)
        budget = BudgetAmendmentService(self.store, campaign_id=self.request["binding"]["campaign_id"], clock=lambda: 1792497000.0)
        gate_patch = patch("template_factory.evidence_recovery.validate_source_gate", return_value={"fixture": True})
        gate_patch.start()
        self.addCleanup(gate_patch.stop)
        amendment = budget.register_frozen_revision(self._budget_request(prepared))
        resume = self._resume_request(prepared, amendment["id"])
        # The baseline is an immutable source input to prepare; a one-byte drift
        # must be rejected before activation/queue state is written.
        entry = next(row for row in self.request["prepared_program_revision"]["entries"] if row["mode"] == "replace")
        target = self.fixture.root / entry["prepared_ref"]
        target.write_bytes(target.read_bytes() + b"\n")
        with self.assertRaises(FactoryError):
            ProductRecoveryService(self.store, clock=lambda: 1792497000.0).resume_frozen_revision(
                self.request["binding"]["plan_id"], resume)
        with self.store.connect() as con:
            row = con.execute("SELECT activated_at,new_deadline FROM tf_budget_amendment WHERE id=?", (amendment["id"],)).fetchone()
            self.assertIsNone(row["activated_at"])
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_product_resume WHERE plan_id=?", (self.request["binding"]["plan_id"],)).fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (self.request["binding"]["campaign_id"], self.request["binding"]["product_id"])).fetchone()[0], 7)

    def test_six_projections_and_candidate_render_keep_exact_program_bytes(self):
        from template_factory.cognition import DESIGN_DIMENSIONS, _design_review_payload, _write_design_projection, render_candidate
        from template_factory.frozen_revision import prepare, review_evidence
        prepared = prepare(self.store, self.request["binding"]["job_id"], self.request)
        contents = program_contents(self.store, prepared["prepared_program_revision"])
        evidence = review_evidence(self.store, prepared, self.request, contents)
        producer = self.fixture.producer["job"]
        snapshot = copy.deepcopy(producer["snapshot"])
        snapshot["case_design"] = prepared["case_design"]
        facts = self.fixture.producer["checkpoints"]["blueprint-accepted-facts-view"]["result"]
        snapshot["case_facts_view"] = facts
        research = self.fixture.producer["checkpoints"]["blueprint-research"]["result"]
        dimensions = (*DESIGN_DIMENSIONS, "runtime_protocol")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            context = root / "context"
            context.mkdir()
            (context / "GUIDANCE.md").write_text("R8 isolated projection fixture")
            projections = {}
            for dim in dimensions:
                view = root / dim
                view.mkdir()
                projection_digest = _write_design_projection(view, dim, snapshot, prepared["effective_plan"], research,
                                                              context, None, None, None, evidence)
                payload = _design_review_payload(snapshot, prepared["effective_plan"], dim, view, evidence)
                self.assertEqual(payload["projection_digest"], projection_digest)
                projections[dim] = projection_digest
                self.assertTrue((view / "DRAFT.md").is_file())
                if dim in {"phase_acceptance", "architecture_contract", "runtime_protocol"}:
                    manifest = json.loads((view / "program-evidence/PROGRAM_EVIDENCE.json").read_text())
                    self.assertEqual(set(manifest["files"]), set(evidence["manifest"]["files"]))
                    self.assertEqual((view / "program-evidence/prepared/acceptance/p0_library.py").read_bytes(),
                                     (R8 / "prepared-programs/acceptance/p0_library.py").read_bytes())
                if dim == "runtime_protocol":
                    self.assertTrue((view / "RUNTIME_CONTRACT.md").is_file())
            self.assertEqual(len(projections), 6)
            candidate = root / "candidate"
            render_candidate({"spec": prepared["effective_plan"]["spec"], "files": contents}, research,
                             snapshot, candidate, "r8-test")
            architecture = (candidate / "ARCHITECTURE.md").read_text()
            self.assertEqual(architecture.count("# 架构与契约"), 1)
            for entry in prepared["prepared_program_revision"]["entries"]:
                raw = (candidate / entry["path"]).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["after_sha256"])

