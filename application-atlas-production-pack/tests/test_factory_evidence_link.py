"""Cross-component evidence recovery link; all state and CLI calls are temporary/fake."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from evidence_recovery_fixture import ARCHIVE, JOB_ID, install_r7_evidence
from test_factory_r7_link import R7PositivePipelineLinkTests
from test_factory_r6_link import StopAtAggregateReview
from template_factory.budget import BudgetLedger
from template_factory.evidence_recovery import (
    EvidenceRecoveryService, PREPARE_SCHEMA, RECOVER_SCHEMA, SAVED_RESUME_SCHEMA, SOURCE_DIGEST, SOURCE_REF,
)
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, canonical, digest
from template_factory.v1_batches import BatchService

PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
GATE = {
    "source_commit": "a" * 40, "source_tree_digest": "b" * 64,
    "ci_evidence": [{"path": "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/fixture-ci.json",
                     "sha256": "c" * 64, "run_id": 9001, "head_sha": "a" * 40,
                     "required_checks": ["check", "docker-integration"]}],
}


class EvidencePipelineFixture:
    def __init__(self, outcome="passed", malformed=False):
        self.calls = []; self.phase_payload = None
        self.outcome, self.malformed = outcome, malformed
    def info(self): return {"kind": "fixture-only", "provider_called": False}
    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        from pathlib import Path
        directory = Path(directory)
        name = directory.name
        payload = json.loads((directory / "input.json").read_text())
        if name == "aggregate-semantic-review":
            self.calls.append(name)
            selection = payload.get("effective_review_selection") or payload.get("identity", {}).get("effective_review_selection")
            # The aggregate is a host-side checkpoint composition. Stop here after observing it.
            raise StopAtAggregateReview
        self.calls.append(name)
        if payload.get("review_dimensions") != ["phase_acceptance"]:
            raise AssertionError("only the authorized appended phase may reach the fake CLI")
        self.phase_payload = payload
        budget = kwargs["budget"]
        ledger = budget["ledger"]
        # The archived authorization has a fixed date; this fixture must use
        # the same in-window clock as its recovery service, not today's date.
        ledger.clock = lambda: 1792490000
        reserved = ledger.reserve(
            budget["identity"], budget["phase"], budget["kind"], timeout,
            job_id=budget["job_id"], requested_model=model, stage=budget["stage"],
            retry=budget["retry"], retry_scope=budget["retry_scope"], plan_id=budget["plan_id"],
            protocol_context=budget["protocol_context"],
            evidence_recovery_id=budget["evidence_recovery_id"], job_token=budget["job_token"],
        )
        config = self._config(directory)
        (directory / "opencode.json").write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n")
        ledger.mark_spawn_intent(reserved["id"], directory=directory)
        ledger.mark_started(reserved["id"])
        ledger.finish(reserved["id"], "completed", observed_model=model, outcome="fixture-completed")
        if self.malformed:
            return {"not": "a valid review report"}
        return {"summary": "Fixture evidence review; no provider was called.",
                "checks": [{"dimension": "phase_acceptance", "outcome": self.outcome,
                            "files": ["program-evidence/prepared/acceptance/p0_organize.py"],
                            "reason": "The prepared P0 evidence is structurally consistent."}],
                "suggestions": []}

    @staticmethod
    def _config(directory):
        reads = ["input.json", "leaf.md", "source", "source/**"]
        reads += [str(directory.resolve() / name) for name in reads[:]]
        rules = [{"action": "*", "resource": "*", "effect": "deny"}]
        rules += [{"action": "read", "resource": name, "effect": "allow"} for name in reads]
        agent = "atlas-factory-" + hashlib.sha256(str(directory.resolve()).encode()).hexdigest()[:12]
        policies = [{"action": action, "resource": resource, "effect": "deny"} for action, resource in
                    [("tool.use", "shell:*"), ("tool.use", "execute:*"), ("plugin.use", "*"),
                     ("mcp.use", "*"), ("skill.use", "*")]]
        return {"$schema": "https://opencode.ai/config.json", "permissions": rules,
                "agents": {agent: {"mode": "primary", "description": "Atlas read-only factory proposal agent", "permissions": rules}},
                "policies": policies}


class PrestartFailureFixtureCLI(EvidencePipelineFixture):
    """Reserve then prove no spawn; the provider boundary is never reached."""
    def __init__(self):
        super().__init__(); self.provider_calls = 0
    def run(self, directory, prompt, model, timeout, cancelled, on_progress, **kwargs):
        budget = kwargs["budget"]
        ledger = budget["ledger"]
        ledger.clock = lambda: 1792490000
        reservation = ledger.reserve(
            budget["identity"], budget["phase"], budget["kind"], timeout,
            job_id=budget["job_id"], requested_model=model, stage=budget["stage"],
            retry=budget["retry"], retry_scope=budget["retry_scope"], plan_id=budget["plan_id"],
            protocol_context=budget["protocol_context"],
            evidence_recovery_id=budget["evidence_recovery_id"], job_token=budget["job_token"],
        )
        ledger.release_not_started(reservation["id"])
        raise FactoryError("fixture proves subprocess was never started", "fixture_prestart", 409)


class EvidenceRecoveryPipelineLinkTests(unittest.TestCase):
    def setUp(self):
        self.fixture = R7PositivePipelineLinkTests(methodName="runTest")
        self.fixture.setUp()
        self.base = self.fixture.base
        self.addCleanup(self.base.tearDown)
        self.store = self.base.store
        self.baseline = install_r7_evidence(self.base)
        auth_path = self.base.root / SOURCE_REF
        self.assertEqual(hashlib.sha256(auth_path.read_bytes()).hexdigest(), SOURCE_DIGEST)
        self.service = EvidenceRecoveryService(self.store, clock=lambda: 1792490000,
                                              source_gate_validator=lambda _store, gate: gate)

    def test_prepare_register_recover_claim_and_append_one_phase_before_aggregate(self):
        from template_factory.v1_batches import _g1_source_digest
        gate = dict(GATE, source_tree_digest=_g1_source_digest(self.store.pack.parent))
        request = {"schema": PREPARE_SCHEMA, "request_key": "evidence-link-fixture",
                   "source_authorization": {"source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST},
                   "source_gate": gate}
        prepared = self.service.prepare(JOB_ID, request)
        self.expected_evidence_digest = prepared["materials"]["evidence_digest"]
        self.assertEqual(set(prepared["materials"]["reuse_checks"]), {
            "scenario_scope", "product_completeness", "architecture_contract", "decisions_defaults", "runtime_protocol"})
        before = {name: self.store.checkpoint(JOB_ID, name) for name in (
            prepared["materials"]["old_phase"]["checkpoint_name"], prepared["materials"]["old_aggregate"]["checkpoint_name"])}
        grant = self.service.register(prepared, request)
        recovered = self.service.recover(JOB_ID, {"schema": RECOVER_SCHEMA, "grant_id": grant["id"],
            "request_key": request["request_key"], "proposal_digest": prepared["proposal_digest"]})
        self.assertEqual(recovered["attempt"], 2)
        BatchService(self.store).action(PLAN_ID, "resume")
        claimed = self.store.claim("evidence-link-fixture")
        self.assertEqual((claimed["id"], claimed["attempt"]), (JOB_ID, 2))
        cli = EvidencePipelineFixture()
        with self.assertRaises(StopAtAggregateReview):
            Pipeline(self.store, cli=cli).run(claimed)
        self.assertEqual(len([name for name in cli.calls if "phase_acceptance" in name]), 1)
        self.assertEqual(cli.phase_payload["review_dimensions"], ["phase_acceptance"])
        self.assertEqual(cli.phase_payload["prepared_program_evidence_digest"], self.expected_evidence_digest)
        for name, record in before.items():
            self.assertEqual(self.store.checkpoint(JOB_ID, name), record)
        recovery = self.service.active_for_job(JOB_ID)
        self.assertEqual(recovery["attempt"], 2)
        new_phase_name = prepared["materials"]["old_phase"]["checkpoint_name"] + "-evidence-" + grant["id"]
        new_outer_name = prepared["materials"]["old_aggregate"]["checkpoint_name"] + "-evidence-" + grant["id"]
        new_phase = self.store.checkpoint(JOB_ID, new_phase_name)
        new_outer = self.store.checkpoint(JOB_ID, new_outer_name)
        self.assertIsNotNone(new_phase)
        self.assertIsNotNone(new_outer)
        self.assertEqual(new_phase["result"]["evidence_grant_id"], grant["id"])
        self.assertEqual(new_phase["result"]["checks"][0]["dimension"], "phase_acceptance")
        self.assertEqual(new_outer["result"]["effective_review_selection"]["grant_id"], grant["id"])
        with self.store.connect() as con:
            row = con.execute("SELECT retry,retry_scope,status FROM tf_budget_reservation WHERE job_id=? AND retry_scope LIKE '%phase_acceptance%' ORDER BY created DESC LIMIT 1", (JOB_ID,)).fetchone()
        self.assertEqual(row["retry"], 1)
        self.assertEqual(row["status"], "completed")
        self.assertTrue(row["retry_scope"].endswith("phase_acceptance"))

    def test_invalid_prepared_evidence_reference_is_rejected_without_second_call(self):
        # The supported validator independently rejects an invented evidence file.
        from template_factory.cognition import validate_review
        from pathlib import Path
        stage = self.store.root / "jobs" / JOB_ID / "attempt-2" / "fixture-review"
        stage.mkdir(parents=True)
        with self.assertRaises(FactoryError):
            validate_review({"summary": "bad", "checks": [{"dimension": "phase_acceptance",
                "outcome": "passed", "files": ["program-evidence/prepared/acceptance/not-a-real-file.py"],
                "reason": "bad reference"}], "suggestions": []}, stage, ("phase_acceptance",))

    def test_saved_phase_result_resumes_host_only_without_another_phase_call(self):
        from template_factory.v1_batches import _g1_source_digest
        gate = dict(GATE, source_tree_digest=_g1_source_digest(self.store.pack.parent))
        request = {"schema": PREPARE_SCHEMA, "request_key": "saved-result-fixture",
                   "source_authorization": {"source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST},
                   "source_gate": gate}
        prepared = self.service.prepare(JOB_ID, request)
        grant = self.service.register(prepared, request)
        self.service.recover(JOB_ID, {"schema": RECOVER_SCHEMA, "grant_id": grant["id"],
            "request_key": request["request_key"], "proposal_digest": prepared["proposal_digest"]})
        BatchService(self.store).action(PLAN_ID, "resume")
        claimed = self.store.claim("saved-result-prestart")
        prestart_cli = PrestartFailureFixtureCLI()
        with self.assertRaises(FactoryError):
            Pipeline(self.store, cli=prestart_cli).run(claimed)
        self.assertEqual(prestart_cli.provider_calls, 0)
        with self.store.connect() as con:
            row = con.execute("SELECT call_attempt,status FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()
            released = con.execute("SELECT status FROM tf_budget_reservation WHERE job_id=? AND retry_scope LIKE '%phase_acceptance%' ORDER BY created DESC LIMIT 1", (JOB_ID,)).fetchone()
        self.assertIsNone(row["call_attempt"])
        self.assertEqual(row["status"], "queued")
        self.assertEqual(released["status"], "not_started")
        # Model the operator's new claim after a proven pre-spawn failure.
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET state='queued',attempt=3,token=NULL,lease=NULL WHERE id=?", (JOB_ID,))
        BatchService(self.store).action(PLAN_ID, "resume")
        claimed = self.store.claim("saved-result-actual-call")
        self.assertEqual(claimed["attempt"], 3)
        first_cli = EvidencePipelineFixture()
        with self.assertRaises(StopAtAggregateReview):
            Pipeline(self.store, cli=first_cli).run(claimed)
        self.assertIn("aggregate-semantic-review", first_cli.calls)
        self.assertEqual(len([name for name in first_cli.calls if "phase_acceptance" in name]), 1)
        from template_factory.evidence_grants import EvidenceGrantService
        consumed = EvidenceGrantService(self.store).get(grant["id"])
        self.assertEqual(consumed["call_attempt"], 3)
        self.assertEqual(consumed["status"], "consumed")
        # The host-only continuation is explicitly bound to a new source tree and exact saved result bytes.
        BatchService(self.store).action(PLAN_ID, "pause")
        source_fixture = self.store.pack.parent / "application-atlas-production-pack" / "template_factory" / "host_only_fixture.py"
        source_fixture.parent.mkdir(parents=True, exist_ok=True)
        source_fixture.write_text("synthetic host-side correction\n")
        updated_gate = dict(gate, source_commit="d" * 40,
                            source_tree_digest=_g1_source_digest(self.store.pack.parent))
        self.assertNotEqual(updated_gate["source_tree_digest"], gate["source_tree_digest"])
        phase = prepared["materials"]["new_phase"]
        result_path = self.store.root / "jobs" / JOB_ID / "attempt-3" / phase["stage_name"] / "result.json"
        actual_input = result_path.parent / "input.json"
        from template_factory.artifacts import tree_manifest
        saved_materials = EvidenceGrantService(self.store).get(grant["id"])["proposal"]["materials"]
        saved_phase = saved_materials["new_phase"]
        self.assertFalse(actual_input.read_bytes() == (json.dumps(saved_phase["payload"], ensure_ascii=False, indent=1) + "\n").encode())
        self.assertEqual(actual_input.read_bytes(), (json.dumps(phase["payload"], ensure_ascii=False, indent=1) + "\n").encode())
        self.assertEqual(digest(tree_manifest(result_path.parent / "source")), saved_phase["source_tree_digest"])
        self.assertEqual(actual_input.read_bytes(), (json.dumps(phase["payload"], ensure_ascii=False, indent=1) + "\n").encode())
        import hashlib
        resumed = self.service.resume_saved_result(JOB_ID, {
            "schema": SAVED_RESUME_SCHEMA, "grant_id": grant["id"], "request_key": "host-resume-fixture",
            "source_gate": updated_gate, "expected_saved_result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        })
        self.assertEqual(resumed["attempt"], 4)
        BatchService(self.store).action(PLAN_ID, "resume")
        claimed_again = self.store.claim("saved-result-host-only")
        self.assertEqual(claimed_again["attempt"], 4)
        second_cli = EvidencePipelineFixture()
        with self.assertRaises(StopAtAggregateReview):
            Pipeline(self.store, cli=second_cli).run(claimed_again)
        self.assertEqual(second_cli.calls, ["aggregate-semantic-review"])
        self.assertEqual(self.service.active_for_job(JOB_ID)["source_gate"], updated_gate)

    def test_blocked_uncertain_and_malformed_phase_outputs_cannot_advance_or_get_a_second_call(self):
        # Each subcase gets a separate isolated baseline and one-use grant.
        for label, outcome, malformed in (("blocked", "blocked", False),
                                          ("uncertain", "uncertain", False),
                                          ("malformed", "passed", True)):
            with self.subTest(result=label):
                self.base.tearDown()
                self.fixture = R7PositivePipelineLinkTests(methodName="runTest")
                self.fixture.setUp()
                self.base = self.fixture.base
                self.addCleanup(self.base.tearDown)
                self.store = self.base.store
                install_r7_evidence(self.base)
                self.service = EvidenceRecoveryService(self.store, clock=lambda: 1792490000,
                                                      source_gate_validator=lambda _store, gate: gate)
                from template_factory.v1_batches import _g1_source_digest
                gate = dict(GATE, source_tree_digest=_g1_source_digest(self.store.pack.parent))
                request = {"schema": PREPARE_SCHEMA, "request_key": "failure-" + label,
                           "source_authorization": {"source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST},
                           "source_gate": gate}
                prepared = self.service.prepare(JOB_ID, request)
                grant = self.service.register(prepared, request)
                self.service.recover(JOB_ID, {"schema": RECOVER_SCHEMA, "grant_id": grant["id"],
                    "request_key": request["request_key"], "proposal_digest": prepared["proposal_digest"]})
                BatchService(self.store).action(PLAN_ID, "resume")
                claimed = self.store.claim("failure-fixture")
                cli = EvidencePipelineFixture(outcome=outcome, malformed=malformed)
                with self.assertRaises((FactoryError, ValueError)):
                    Pipeline(self.store, cli=cli).run(claimed)
                self.assertEqual(len(cli.calls), 1)
                with self.store.connect() as con:
                    row = con.execute("SELECT status,call_attempt FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()
                self.assertIn(row["status"], {"consumed", "started"})
                self.assertEqual(row["call_attempt"], 2)


if __name__ == "__main__": unittest.main()
