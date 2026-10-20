"""Temporary-store end-to-end link for one frozen review retry; no provider calls."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_factory_r5_link as r5_fixture
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, canonical, digest
from template_factory.v1_batches import BatchService

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parent
DOCS = ROOT / "docs/template-factory"
FROZEN_DOCS = DOCS / "g1-frozen-review-recovery-2026-10-20"
R7_DOCS = DOCS / "g1-r7-evidence-recovery-2026-10-20"
JOB_ID = "job_b01427592b164863aab5bedf7b3863bb"
ARTIFACT_ID = "tpl_f7ecff8d8fef4deba828aa2a8ef82918"
CAMPAIGN = "atlas-v1-first-production-2026-10-19"
PRODUCT = "product-c42848f63251507bd9d911a5"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
BASELINE_PATH = FROZEN_DOCS / "BASELINE.json"
ACTUAL = R7_DOCS / "actual-frozen-review" / JOB_ID
PRODUCED = R7_DOCS / "produced" / ARTIFACT_ID
OPS = R7_DOCS / "operations/final-state.json"


class StopAfterAcceptance(Exception):
    pass


class FrozenReviewFixtureCLI:
    """A no-provider CLI that performs the real budget/grant lifecycle."""
    def __init__(self, store, *, outcome="passed", fault=None):
        self.store = store
        self.outcome = outcome
        self.fault = fault
        self.calls = []
        self.result = None
        self.reservation_id = None

    def info(self):
        return {"kind": "frozen-review-fixture", "provider_called": False}

    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        from atlas_runtime import atomic_json
        from template_factory.evidence_grants import EvidenceGrantService, get_call_binding
        from template_factory.frozen_review_materials import extend_readonly_config

        directory = Path(directory)
        self.calls.append(directory)
        budget = kwargs["budget"]
        ledger = budget["ledger"]
        context = dict(budget["protocol_context"])
        reserve = {
            "identity": budget["identity"], "phase": budget["phase"],
            "kind": budget["kind"], "timeout": timeout,
            "job_id": budget["job_id"], "requested_model": model,
            "stage": budget["stage"], "retry": budget["retry"],
            "retry_scope": budget["retry_scope"], "plan_id": budget["plan_id"],
            "protocol_context": context,
            "evidence_recovery_id": budget["evidence_recovery_id"],
            "job_token": budget["job_token"],
        }
        if self.fault == "timeout_3600":
            reserve["timeout"] = 3600
        elif self.fault == "deadline_2699":
            # Exercise the real reserve deadline check under a controllable clock.
            from template_factory.budget import BudgetLedger
            ledger = BudgetLedger(self.store, clock=lambda: 1792492613.855422)
        elif self.fault in {"language", "prompt", "source", "projection", "payload", "material", "model", "stage", "scope", "retry", "artifact", "job", "auth"}:
            if self.fault == "language":
                context["input_sha256"] = "f" * 64
            elif self.fault == "prompt":
                context["prompt_sha256"] = "f" * 64
            elif self.fault == "source":
                context["source_tree_digest"] = "f" * 64
            elif self.fault == "projection":
                context["projection_digest"] = "f" * 64
            elif self.fault == "payload":
                context["full_payload_digest"] = "f" * 64
            elif self.fault == "material":
                context["materials_manifest_digest"] = "f" * 64
            elif self.fault == "model":
                reserve["requested_model"] = "unapproved-model"
            elif self.fault == "stage":
                reserve["stage"] = "another-stage"
            elif self.fault == "scope":
                reserve["retry_scope"] = "another-scope"
            elif self.fault == "retry":
                reserve["retry"] = None
            elif self.fault == "artifact":
                context["source_tree_digest"] = "e" * 64
            elif self.fault == "job":
                reserve["job_id"] = "another-job"
            elif self.fault == "auth":
                reserve["evidence_recovery_id"] = "another-grant"
        reserved = ledger.reserve(
            reserve.pop("identity"), reserve.pop("phase"), reserve.pop("kind"), reserve.pop("timeout"),
            **reserve,
        )
        self.reservation_id = reserved["id"]
        grant = EvidenceGrantService(self.store).get(budget["evidence_recovery_id"])
        call = get_call_binding(grant["proposal"])
        manifest = json.loads((directory / "review-materials/manifest.json").read_bytes())
        archived_config = json.loads((ACTUAL / "opencode.json").read_bytes())
        reads = [rule["resource"] for rule in archived_config["permissions"] if rule.get("action") == "read"]
        original_input = next(path for path in reads if path.startswith("/") and path.endswith("/input.json"))
        original_attempt = Path(original_input).parent
        config, identity = extend_readonly_config(archived_config, original_attempt, directory, manifest)
        if identity != call["cli_config_identity"]:
            raise AssertionError("fixture ACL identity differs from the immutable call proposal")
        atomic_json(directory / "opencode.json", config)
        (directory / "prompt.txt").write_bytes(prompt.encode("utf-8"))
        ledger.mark_spawn_intent(reserved["id"], directory=directory)
        ledger.mark_started(reserved["id"])

        if self.fault == "timeout":
            ledger.finish(reserved["id"], "failed", observed_model=model, outcome="cli_timeout")
            raise FactoryError("fixture timeout after model-call start", "cli_timeout", 409)

        from template_factory.cognition import DIMENSIONS
        checks = [{"dimension": dimension, "outcome": self.outcome,
                   "files": ["README.md"],
                   "reason": "Fixture exercises binding and delivery only; no product claim is made."}
                  for dimension in DIMENSIONS]
        if self.fault == "missing_dimension":
            checks.pop()
        if self.fault == "invalid_reference":
            checks[0]["files"] = ["missing/never-authored.txt"]
        self.result = {
            "summary": "Temporary static frozen-candidate review fixture; no model/provider was called.",
            "checks": checks,
            "suggestions": [],
        }
        atomic_json(directory / "original-response.json", {"text": json.dumps(self.result, ensure_ascii=False)})
        result_bytes = (json.dumps(self.result, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
        atomic_json(directory / "cli-summary.json", {
            "delivery_status": "delivered", "failure_code": None,
            "reservation_id": reserved["id"], "result_sha256": hashlib.sha256(result_bytes).hexdigest(),
            "original_response_sha256": hashlib.sha256((directory / "original-response.json").read_bytes()).hexdigest(),
            "requested_model": model, "cli_status": "completed", "exit_code": 0,
            "effective_timeout_seconds": timeout,
        })
        ledger.finish(reserved["id"], "completed", observed_model=model, outcome="fixture-delivered")
        return self.result


class FrozenReviewPipelineLinkTests(unittest.TestCase):
    def setUp(self):
        self.base = r5_fixture.R5PreparedLinkTests(methodName="runTest")
        self.base.setUp()
        self.addCleanup(self.base.tearDown)
        self.store, self.root = self.base.store, self.base.root
        self.baseline = json.loads(BASELINE_PATH.read_text())
        self.final_state = json.loads(OPS.read_text())
        self._install_original_frozen_state()

    def _prepare_recover_and_claim(self):
        from template_factory.frozen_review_recovery import (
            AUTH_REF, AUTH_SHA256, JOB_ID as FROZEN_JOB, REQUEST_KEY,
            FrozenReviewRecoveryService,
        )
        from template_factory.v1_batches import _g1_source_digest
        gate = {
            "source_commit": "a" * 40,
            "source_tree_digest": _g1_source_digest(self.store.pack.parent),
            "ci_evidence": [{
                "path": "docs/template-factory/g1-frozen-review-recovery-2026-10-20/fixture-ci.json",
                "sha256": "c" * 64, "run_id": 4242, "head_sha": "a" * 40,
                "required_checks": ["check", "docker-integration"],
            }],
        }
        request = {"schema": "atlas.frozen-review-prepare.v1", "request_key": REQUEST_KEY,
                   "source_authorization": {"source_ref": AUTH_REF, "source_digest": AUTH_SHA256},
                   "source_gate": gate}
        service = FrozenReviewRecoveryService(self.store, clock=lambda: 1792489000,
                                              source_gate_validator=lambda _store, value: value)
        prepared = service.prepare(FROZEN_JOB, request)
        self.assertEqual(prepared["schema"], "atlas.frozen-review-recovery-proposal.v1")
        grant = service.register(prepared, request)
        recovered = service.recover(FROZEN_JOB, {
            "schema": "atlas.frozen-review-recovery.v1", "grant_id": grant["id"],
            "request_key": request["request_key"], "proposal_digest": prepared["proposal_digest"],
        })
        self.assertEqual((recovered["attempt"], recovered["worker_started"]), (2, False))
        BatchService(self.store).action(PLAN_ID, "resume")
        claimed = self.store.claim("frozen-review-fixture")
        self.assertEqual((claimed["id"], claimed["attempt"]), (FROZEN_JOB, 2))
        return service, request, prepared, grant, claimed

    def _install_original_frozen_state(self):
        from template_factory.frozen_review_recovery import AUTH_REF

        # Copy only the fixed authorization source into the temporary pack.
        target = self.root / AUTH_REF
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(FROZEN_DOCS / "authorization/ATLAS_G1_FROZEN_REVIEW_RECOVERY_CODEX_INSTRUCTIONS.txt", target)
        archive_copy = (self.root / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/produced"
                        / ARTIFACT_ID / "blueprint.zip")
        archive_copy.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PRODUCED / "blueprint.zip", archive_copy)

        # Recreate the immutable frozen bundle at the exact path bound by snapshot.
        snapshot = self.baseline["job"]["snapshot"]
        bundle = self.store.root / snapshot["bundle_path"]
        bundle.parent.mkdir(parents=True, exist_ok=True)
        archive_artifact = json.loads((PRODUCED / "ARTIFACT-AT-FREEZE.json").read_text())
        actual_archive = self.store.root / archive_artifact["archive_path"]
        actual_archive.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PRODUCED / "blueprint.zip", actual_archive)
        with zipfile.ZipFile(PRODUCED / "blueprint.zip") as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                rel = Path(info.filename)
                if rel.is_absolute() or ".." in rel.parts:
                    raise AssertionError("frozen fixture zip contains an unsafe path")
                destination = bundle / "source" / rel
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(archive.read(info))
        from atlas_runtime import atomic_json
        for name in ("manifest", "plan", "provenance"):
            atomic_json(bundle / (name + ".json"), archive_artifact[name])
        atomic_json(bundle / "inventory.json", {"digest": archive_artifact["digest"]})

        original_review = self.store.root / "jobs" / JOB_ID / "attempt-1" / "cognitive-review"
        original_review.mkdir(parents=True, exist_ok=True)
        for name in ("input.json", "leaf.md", "cli-summary.json", "opencode.json"):
            shutil.copyfile(ACTUAL / name, original_review / name)
        shutil.copytree(ACTUAL / "source", original_review / "source")
        from atlas_runtime import atomic_json
        from template_factory.frozen_review_materials import _base_config
        atomic_json(original_review / "opencode.json", _base_config(original_review))

        # Install the captured 80/7 ledger and protocol/evidence history.
        with self.store.connect(True) as con:
            for table, rows in self.final_state["ledger"].items():
                columns = [row[1] for row in con.execute(f"PRAGMA table_info({table})")]
                if not columns:
                    continue
                con.execute(f"DELETE FROM {table}")
                for row in rows:
                    keys = [name for name in columns if name in row]
                    con.execute(f"INSERT INTO {table} ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                                tuple(row[name] for name in keys))
            for table, rows in self.final_state.get("recovery_tables", {}).items():
                columns = [row[1] for row in con.execute(f"PRAGMA table_info({table})")]
                if not columns:
                    continue
                con.execute(f"DELETE FROM {table}")
                for row in rows:
                    keys = [name for name in columns if name in row]
                    con.execute(f"INSERT INTO {table} ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                                tuple(row[name] for name in keys))

            frozen_job = self.baseline["job"]
            # Replace the R5 fixture's colliding plan batch with the captured paused batch.
            batch = self.baseline["batch"]
            con.execute("DELETE FROM batch WHERE id=?", (batch["id"],))
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (batch["id"], batch["state"], canonical(batch["config"]), batch["created_at"]))
            for prior_batch in self.final_state["batches"]:
                con.execute("INSERT OR REPLACE INTO batch VALUES(?,?,?,?)", (prior_batch["id"], prior_batch["state"], prior_batch["config"], prior_batch["created_at"]))
            con.execute("DELETE FROM job WHERE id=?", (JOB_ID,))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                frozen_job["id"], frozen_job["batch_id"], frozen_job["kind"], frozen_job["state"],
                frozen_job["stage"], frozen_job["attempt"], None, None,
                canonical(frozen_job["snapshot"]), canonical(frozen_job["error"]),
                frozen_job["created_at"], frozen_job["updated_at"]))
            for event in self.baseline["events"]:
                con.execute("INSERT INTO event(seq,job_id,attempt,at,stage,message) VALUES(?,?,?,?,?,?)",
                            (event["seq"], JOB_ID, event["attempt"], event["at"], event["stage"], event["message"]))
            for acceptance in self.baseline["acceptances"]:
                con.execute("INSERT OR REPLACE INTO acceptance VALUES(?,?,?,?,?,?,?)",
                            tuple(acceptance[k] for k in ("id", "artifact_id", "digest", "method", "job_id", "body", "created_at")))

            existing = con.execute("SELECT id FROM artifact WHERE id=?", (ARTIFACT_ID,)).fetchone()
            if existing:
                con.execute("DELETE FROM artifact WHERE id=?", (ARTIFACT_ID,))
            con.execute("INSERT INTO artifact VALUES(?,?,?,?,?,?,?)", (
                ARTIFACT_ID, archive_artifact["job_id"], archive_artifact["digest"],
                archive_artifact["level"], archive_artifact["state"], canonical(archive_artifact),
                archive_artifact["created_at"]))

        self.assertEqual(digest(self.store.job(JOB_ID)["snapshot"]), self.baseline["snapshot_digest"])
        with self.store.connect() as con:
            calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            unavailable = con.execute("SELECT id,body FROM acceptance WHERE job_id=?", (JOB_ID,)).fetchall()
        self.assertEqual(calls, 80)
        self.assertEqual(repairs, 7)
        self.assertEqual([(row["id"], json.loads(row["body"])["outcome"]) for row in unavailable],
                         [(self.baseline["acceptances"][0]["id"], "unavailable")])

    def test_prepare_register_recover_and_real_pipeline_use_exactly_one_model_call(self):
        service, request, prepared, grant, claimed = self._prepare_recover_and_claim()
        FROZEN_JOB = claimed["id"]
        old_snapshot = self.store.job(FROZEN_JOB)["snapshot"]
        cli = FrozenReviewFixtureCLI(self.store)
        Pipeline(self.store, cli=cli).run(claimed)

        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(cli.calls[0].name, "cognitive-review")
        self.assertEqual(cli.calls[0].parent.name, "attempt-2")
        self.assertEqual(cli.result["checks"][0]["dimension"], "category_evidence")
        self.assertEqual(self.store.job(FROZEN_JOB)["attempt"], 2)
        self.assertEqual(self.store.job(FROZEN_JOB)["snapshot"], old_snapshot)
        self.assertEqual(self.store.job(FROZEN_JOB)["state"], "completed")
        with self.store.connect() as con:
            reservations = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN,)).fetchone()[0]
            acceptances = con.execute("SELECT id,body FROM acceptance WHERE job_id=? ORDER BY created_at,id", (FROZEN_JOB,)).fetchall()
            grant_row = con.execute("SELECT status,consumed_reservation_id,call_attempt FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()
        self.assertEqual((reservations, repairs, active), (81, 7, 0))
        self.assertEqual(len(acceptances), 2)
        self.assertEqual(acceptances[0]["id"], self.baseline["acceptances"][0]["id"])
        self.assertEqual(json.loads(acceptances[0]["body"])["outcome"], "unavailable")
        self.assertNotEqual(acceptances[1]["id"], acceptances[0]["id"])
        self.assertEqual(json.loads(acceptances[1]["body"])["outcome"], "passed")
        self.assertEqual((grant_row["status"], grant_row["consumed_reservation_id"], grant_row["call_attempt"]),
                         ("consumed", cli.reservation_id, 2))
        artifact = next(row for row in self.store.artifacts() if row["id"] == ARTIFACT_ID)
        self.assertNotEqual(artifact.get("publication_status"), "published")
        self.assertFalse(artifact.get("catalog_eligible"))

    def test_blocked_uncertain_invalid_and_timeout_results_never_trigger_a_second_call(self):
        cases = (("blocked", None, False), ("uncertain", None, False),
                 ("passed", "missing_dimension", True), ("passed", "invalid_reference", True),
                 ("passed", "timeout", True))
        for outcome, fault, should_raise in cases:
            with self.subTest(outcome=outcome, fault=fault):
                fixture = type(self)(methodName="runTest")
                fixture.setUp()
                try:
                    _, _, _, grant, claimed = fixture._prepare_recover_and_claim()
                    cli = FrozenReviewFixtureCLI(fixture.store, outcome=outcome, fault=fault)
                    if should_raise:
                        with self.assertRaises(FactoryError):
                            Pipeline(fixture.store, cli=cli).run(claimed)
                    else:
                        Pipeline(fixture.store, cli=cli).run(claimed)
                    self.assertEqual(len(cli.calls), 1)
                    self.assertEqual(cli.calls[0].name, "cognitive-review")
                    self.assertFalse((cli.calls[0].parent / "cognitive-review-reference-repair").exists())
                    with fixture.store.connect() as con:
                        count = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
                        repair_count = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
                        grant_row = con.execute("SELECT status,call_attempt FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()
                    self.assertEqual((count, repair_count), (81, 7))
                    self.assertEqual((grant_row["status"], grant_row["call_attempt"]), ("consumed", 2))
                finally:
                    fixture.doCleanups()

    def test_register_and_recover_are_idempotent_but_proposal_conflicts(self):
        service, request, prepared, grant, _claimed = self._prepare_recover_and_claim()
        replay = service.register(prepared, request)
        self.assertEqual(replay["id"], grant["id"])
        recovery_request = {
            "schema": "atlas.frozen-review-recovery.v1", "grant_id": grant["id"],
            "request_key": request["request_key"], "proposal_digest": prepared["proposal_digest"],
        }
        replayed = service.recover(JOB_ID, recovery_request)
        self.assertTrue(replayed["replayed"])
        self.assertFalse(replayed["worker_started"])
        changed = json.loads(json.dumps(prepared))
        changed["materials"]["frozen_review_call"]["requested_model"] = "different-model"
        changed["proposal_digest"] = digest({k: v for k, v in changed.items() if k != "proposal_digest"})
        with self.assertRaises(FactoryError):
            service.register(changed, request)
        changed_request = dict(recovery_request, proposal_digest="0" * 64)
        with self.assertRaises(FactoryError):
            service.recover(JOB_ID, changed_request)

    def test_mutated_call_binding_is_rejected_before_reservation_or_spawn(self):
        faults = ("timeout_3600", "deadline_2699", "language", "prompt", "source", "projection",
                  "payload", "material", "model", "stage", "scope", "retry", "artifact", "job", "auth")
        for fault in faults:
            with self.subTest(fault=fault):
                fixture = type(self)(methodName="runTest")
                fixture.setUp()
                try:
                    _, _, _, grant, claimed = fixture._prepare_recover_and_claim()
                    cli = FrozenReviewFixtureCLI(fixture.store, fault=fault)
                    with self.assertRaises(FactoryError):
                        Pipeline(fixture.store, cli=cli).run(claimed)
                    self.assertEqual(len(cli.calls), 1)
                    with fixture.store.connect() as con:
                        charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
                        active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN,)).fetchone()[0]
                        grant_row = con.execute("SELECT status FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()
                    # Invalid immutable identity is rejected before a new budget row is charged.
                    self.assertEqual(charged, 80)
                    self.assertEqual(active, 0)
                    self.assertIn(grant_row["status"], {"queued", "registered"})
                finally:
                    fixture.doCleanups()

    def test_expired_worker_lease_cannot_reserve_or_spawn(self):
        _service, _request, _prepared, _grant, claimed = self._prepare_recover_and_claim()
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET lease=? WHERE id=?", (1792488999.0, JOB_ID))
        cli = FrozenReviewFixtureCLI(self.store)
        with self.assertRaises(FactoryError):
            Pipeline(self.store, cli=cli).run(claimed)
        self.assertEqual(len(cli.calls), 0)
        with self.store.connect() as con:
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN,)).fetchone()[0]
        self.assertEqual((charged, active), (80, 0))

    def test_ordinary_ungranted_retry_cannot_use_the_frozen_job_budget(self):
        from template_factory.budget import BudgetLedger

        ledger = BudgetLedger(self.store, campaign_id=CAMPAIGN, clock=lambda: 1792489000)
        model = self.store.job(JOB_ID)["snapshot"]["config"]["model"]
        for retry, retry_scope, stage in ((None, "cognitive-review", "cognitive-review:572da86649b4face"),
                                          (1, "another-scope", "another-stage")):
            with self.subTest(retry=retry, retry_scope=retry_scope, stage=stage):
                with self.assertRaises(FactoryError):
                    ledger.reserve(PRODUCT, "G1", "review", 1800, job_id=JOB_ID,
                                   requested_model=model, stage=stage,
                                   retry=retry, retry_scope=retry_scope, plan_id=PLAN_ID)
        with self.store.connect() as con:
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
        self.assertEqual(charged, 80)

    def test_runtime_rejects_changed_host_source_but_docs_do_not_change_source_gate(self):
        from template_factory.v1_batches import _g1_source_digest

        before = _g1_source_digest(self.store.pack.parent)
        docs_note = self.root / "docs/template-factory/g1-frozen-review-recovery-2026-10-20/runtime-note.md"
        docs_note.parent.mkdir(parents=True, exist_ok=True)
        docs_note.write_text("documentation-only evidence change\n")
        self.assertEqual(_g1_source_digest(self.store.pack.parent), before)
        docs_note.unlink()

        _service, _request, _prepared, _grant, claimed = self._prepare_recover_and_claim()
        source_marker = self.root / "application-atlas-production-pack" / "template_factory" / "frozen_source_marker.py"
        source_marker.parent.mkdir(parents=True, exist_ok=True)
        source_marker.write_text("# source changed after grant registration\n")
        cli = FrozenReviewFixtureCLI(self.store)
        with self.assertRaises(FactoryError):
            Pipeline(self.store, cli=cli).run(claimed)
        self.assertEqual(len(cli.calls), 0)
        with self.store.connect() as con:
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            active = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status IN ('reserved','started','uncertain')", (CAMPAIGN,)).fetchone()[0]
        self.assertEqual((charged, active), (80, 0))


if __name__ == "__main__":
    unittest.main()
