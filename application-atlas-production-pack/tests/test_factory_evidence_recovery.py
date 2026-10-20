"""Focused temporary-store tests for R7 evidence preparation and same-job queueing."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.evidence_recovery import (
    BATCH_ID, CAMPAIGN_ID, DEADLINE, JOB_ID, PLAN_ID, PLAN_PARENT_BATCH_ID, PREPARE_SCHEMA, PRODUCT_ID,
    RECOVER_SCHEMA, SOURCE_DIGEST, SOURCE_REF, EvidenceRecoveryService, validate_source_gate,
)
from template_factory.evidence_grants import EvidenceGrantService
from template_factory.budget import BudgetLedger
from template_factory.store import FactoryError, FactoryStore, canonical, digest, now

PACK = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20"


def _materials():
    phase_payload = {"review_dimensions": ["phase_acceptance"], "proposal_digest": "e7b9e82beb121a4d73852e556eac0eeefd2406af2d4a3f8fc6489eea4944f54"}
    input_digest = digest(phase_payload)
    prompt = "read-only review"
    stage = "blueprint-spec-review-0-ad1379367f3e742a-phase_acceptance"
    return {
        "binding": {"campaign_id": CAMPAIGN_ID, "plan_id": PLAN_ID, "product_id": PRODUCT_ID,
                    "job_id": JOB_ID, "batch_id": BATCH_ID, "attempt": 1,
                    "snapshot_digest": "c4778af6053066cc90b22c1c1320928f7bed4ea9c818bed19cf62c3e986e9239",
                    "deadline": DEADLINE},
        "old_phase": {"checkpoint_name": "blueprint-design-check-0-phase_acceptance",
                      "checkpoint_digest": "dd19d90217dc6cadd7e8346ac4d2af2b1b5a73f4fee2f28aa3ea2f8190ad6d8f",
                      "projection_digest": "39d09af2c64eae5f81b4f83505383eb05902cf1f794e2612786a04892b7b6b4b",
                      "input_sha256": "ef0e7f1ab2963050b046060ac088d43513c871a60b33f1329279a4061a7a3b56",
                      "full_payload_digest": "559c03f2846706675146695d5c30cd4670a51b2039b113e57756dbe9dd9cf6a5",
                      "budget_input_digest": "7742082f7e399a3be58bcebbb66123d4447b7c2cd0f658b83b82ee72977f2a20",
                      "reservation_id": "bud_fbec046b65054a33a1c132ad8ed2fd32"},
        "old_aggregate": {"checkpoint_name": "blueprint-spec-review-0-ad1379367f3e742a-runtime-v1",
                          "checkpoint_digest": "c67396039eda05f809ab13afb7ee6783d614ab826550db612268cf7ae78746df"},
        "new_phase": {"stage_name": stage, "operation": stage + ":" + input_digest[:16],
                      "logical_retry_scope": "blueprint-spec-review:phase_acceptance", "payload": phase_payload,
                      "input_sha256": "a" * 64, "full_payload_digest": digest(phase_payload),
                      "budget_input_digest": input_digest, "prompt": prompt,
                      "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                      "source_tree_digest": "e" * 64, "projection_digest": "e" * 64,
                      "requested_model": "opencode-go/deepseek-v4.1-flash", "cli_config_identity": {"deny_by_default": True}},
        "reuse_checks": {name: {"identical": True, "checkpoint_digest": name} for name in
                         ("architecture_contract", "decisions_defaults", "product_completeness", "runtime_protocol", "scenario_scope")},
    }


class EvidenceRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.workspace = self.root / "workspace"
        self.workspace.mkdir()
        self.pack = self.workspace / "application-atlas-production-pack"
        (self.pack / "template_factory").mkdir(parents=True)
        (self.pack / "tests").mkdir()
        (self.pack / "template_factory/source_marker.py").write_text("# source fixture\n")
        (self.pack / "tests/source_marker.py").write_text("# test fixture\n")
        self.authorization = self.workspace / SOURCE_REF
        self.authorization.parent.mkdir(parents=True)
        shutil.copy(ARCHIVE / "authorization/ATLAS_G1_R7_EVIDENCE_RECOVERY_CODEX_INSTRUCTIONS.txt", self.authorization)
        self.store = FactoryStore(self.root / "state", self.pack)
        self.request = {"schema": PREPARE_SCHEMA, "request_key": "evidence-test-once",
                        "source_authorization": {"source_ref": SOURCE_REF, "source_digest": SOURCE_DIGEST},
                        "source_gate": {"source_commit": "test-commit", "source_tree_digest": "test-tree", "ci_evidence": []}}
        self.service = EvidenceRecoveryService(self.store, clock=lambda: 1792481200.0,
                                               evidence_builder=lambda _store, _job: _materials(),
                                               source_gate_validator=lambda _store, gate: dict(gate))

    def tearDown(self):
        self.tmp.cleanup()

    def _tables(self):
        with self.store.connect() as con:
            return {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}

    def test_prepare_is_pure_and_binds_materials_and_source_authorization(self):
        before = self._tables()
        proposal = self.service.prepare(JOB_ID, self.request)
        self.assertEqual(self._tables(), before)
        self.assertEqual(proposal["source_gate"], self.request["source_gate"])
        self.assertTrue(proposal["source_gate_passed"])
        self.assertEqual(proposal["proposal_digest"], digest({k: v for k, v in proposal.items() if k != "proposal_digest"}))

    def test_unknown_request_fields_and_wrong_authorization_reject(self):
        bad = dict(self.request, extra="not allowed")
        with self.assertRaises(FactoryError):
            self.service.prepare(JOB_ID, bad)
        bad = dict(self.request, source_authorization={"source_ref": SOURCE_REF, "source_digest": "0" * 64})
        with self.assertRaises(FactoryError):
            self.service.prepare(JOB_ID, bad)

    def test_source_gate_checks_exact_head_and_successful_raw_ci(self):
        repo = self.root / "gitrepo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
        pack = repo / "application-atlas-production-pack"
        (pack / "template_factory").mkdir(parents=True)
        (pack / "tests").mkdir()
        (pack / "template_factory/source_marker.py").write_text("# source fixture\n")
        (pack / "tests/source_marker.py").write_text("# test fixture\n")
        evidence = []
        run_ids = (39378796575, 39382442263, 39383180095)
        archives = ("g1-r7-evidence-recovery-2026-10-20", "g1-frozen-review-recovery-2026-10-20",
                    "g1-r8-contract-convergence-2026-10-20")
        for run_id, archive in zip(run_ids, archives):
            data = repo / "docs/template-factory" / archive
            data.mkdir(parents=True)
            path = data / f"ci-{run_id}.json"
            raw = {"runs": [{"run": {"id": run_id, "head_sha": "pending", "status": "completed", "conclusion": "success"},
                             "jobs": {"jobs": [{"name": "check", "status": "completed", "conclusion": "success"},
                                                 {"name": "docker-integration", "status": "completed", "conclusion": "success"}]}}]}
            path.write_text(json.dumps(raw))
            evidence.append({"path": str(path.relative_to(repo)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                             "run_id": run_id, "head_sha": "pending", "required_checks": ["check", "docker-integration"]})
        subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
        subprocess.run(["git", "-C", str(repo), "commit", "-qm", "fixture"], check=True)
        head = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
        from template_factory.v1_batches import _g1_source_digest
        tree = _g1_source_digest(repo)
        for item in evidence:
            item["head_sha"] = head
            path = repo / item["path"]
            document = json.loads(path.read_text())
            document["runs"][0]["run"]["head_sha"] = head
            path.write_text(json.dumps(document))
            item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        gate = {"source_commit": head, "source_tree_digest": tree, "ci_evidence": evidence}
        service = EvidenceRecoveryService(FactoryStore(self.root / "gate-state", pack))
        self.assertEqual(validate_source_gate(service.store, gate)["source_commit"], head)
        for path in ("docs/other/ci.json", "docs/template-factory/../ci.json",
                     "docs/template-factory//ci.json", "docs/template-factory/ci.txt"):
            with self.subTest(path=path), self.assertRaises(FactoryError):
                validate_source_gate(service.store, dict(gate, ci_evidence=[dict(item, path=path) for item in evidence]))
        bad = json.loads((repo / evidence[0]["path"]).read_text())
        bad["runs"][0]["jobs"]["jobs"][0]["conclusion"] = "failure"
        bad_path = repo / evidence[0]["path"]
        bad_path.write_text(json.dumps(bad))
        evidence[0]["sha256"] = hashlib.sha256(bad_path.read_bytes()).hexdigest()
        with self.assertRaises(FactoryError):
            validate_source_gate(service.store, dict(gate, ci_evidence=evidence))

    def test_stale_prepared_proposal_is_rejected_at_registration(self):
        proposal = self.service.prepare(JOB_ID, self.request)
        changed = dict(proposal)
        changed["materials"] = dict(proposal["materials"], tampered=True)
        with self.assertRaises(FactoryError):
            self.service.register(changed, self.request)

    def _install_recovery_fixture(self):
        baseline = json.loads((ARCHIVE / "BASELINE.json").read_text())
        job = baseline["job"]
        subprocess.run(["git", "init", "-q", str(self.workspace)], check=True)
        subprocess.run(["git", "-C", str(self.workspace), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(self.workspace), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(self.workspace), "add", str(self.authorization.relative_to(self.workspace)),
                        "application-atlas-production-pack/template_factory/source_marker.py",
                        "application-atlas-production-pack/tests/source_marker.py"], check=True)
        subprocess.run(["git", "-C", str(self.workspace), "commit", "-qm", "fixture source"], check=True)
        head = subprocess.run(["git", "-C", str(self.workspace), "rev-parse", "HEAD"], check=True,
                              capture_output=True, text=True).stdout.strip()
        from template_factory.v1_batches import _g1_source_digest
        tree = _g1_source_digest(self.workspace)
        rel = "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/ci-fixture.json"
        ci_path = self.workspace / rel
        ci_path.parent.mkdir(parents=True, exist_ok=True)
        ci_path.write_text(json.dumps({"runs": [{"run": {"id": 991, "head_sha": head, "status": "completed", "conclusion": "success"},
                                       "jobs": {"jobs": [{"name": "check", "status": "completed", "conclusion": "success"},
                                                           {"name": "docker-integration", "status": "completed", "conclusion": "success"}]}}]}))
        self.request["source_gate"] = {"source_commit": head, "source_tree_digest": tree,
                                        "ci_evidence": [{"path": rel, "sha256": hashlib.sha256(ci_path.read_bytes()).hexdigest(),
                                                         "run_id": 991, "head_sha": head,
                                                         "required_checks": ["check", "docker-integration"]}]}
        self.service._source_gate_validator = None
        proposal = self.service.prepare(JOB_ID, self.request)
        BudgetLedger(self.store, campaign_id=CAMPAIGN_ID, clock=lambda: 1792481200.0)
        with self.store.connect(True) as con:
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (BATCH_ID, "paused", "{}", now()))
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (PLAN_PARENT_BATCH_ID, "paused", "{}", now()))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (JOB_ID, BATCH_ID, job["kind"], "failed", job["stage"], 1, None, None,
                         canonical(job["snapshot"]), "phase_acceptance blocked", now(), now()))
            for cp in baseline["checkpoints"]:
                con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (JOB_ID, cp["name"], cp["body"]))
            for event in job["events"]:
                con.execute("INSERT INTO event(seq,job_id,attempt,at,stage,message) VALUES(?,?,?,?,?,?)",
                            (event["seq"], JOB_ID, event["attempt"], event["at"], event["stage"], event["message"]))
            def restore_table(table, records):
                columns = {row[1] for row in con.execute(f"PRAGMA table_info({table})")}
                for record in records:
                    values = {key: value for key, value in record.items() if key in columns}
                    names = list(values)
                    con.execute(f"INSERT INTO {table}({','.join(names)}) VALUES({','.join('?' for _ in names)})",
                                [values[name] for name in names])
            restore_table("tf_budget_reservation", baseline["ledger"]["tf_budget_reservation"])
            restore_table("tf_budget_repair", baseline["ledger"]["tf_budget_repair"])
            restore_table("tf_budget_phase", baseline["ledger"]["tf_budget_phase"])
            restore_table("tf_budget_amendment", baseline["ledger"]["tf_budget_amendment"])
            restore_table("tf_protocol_retry_grant", baseline["ledger"]["tf_protocol_retry_grant"])
            restore_table("tf_protocol_retry_grant_use", baseline["ledger"]["tf_protocol_retry_grant_use"])
        grant = EvidenceGrantService(self.store, clock=lambda: 1792481200.0).register(proposal, self.request)
        return proposal, grant["id"], baseline

    def test_recover_queues_same_job_once_and_preserves_prior_checkpoint_history(self):
        proposal, grant_id, baseline = self._install_recovery_fixture()
        request = {"schema": RECOVER_SCHEMA, "grant_id": grant_id, "request_key": self.request["request_key"],
                   "proposal_digest": proposal["proposal_digest"]}
        before = {cp["name"]: cp["body"] for cp in baseline["checkpoints"]}
        recovered = self.service.recover(JOB_ID, request)
        self.assertEqual((recovered["state"], recovered["attempt"], recovered["worker_started"]), ("queued", 2, False))
        replay = self.service.recover(JOB_ID, request)
        self.assertTrue(replay["replayed"])
        with self.store.connect() as con:
            current = con.execute("SELECT state,attempt,snapshot FROM job WHERE id=?", (JOB_ID,)).fetchone()
            after = {row["name"]: row["body"] for row in con.execute("SELECT name,body FROM checkpoint WHERE job_id=?", (JOB_ID,))}
            grant_state = con.execute("SELECT status FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()[0]
        self.assertEqual((current["state"], current["attempt"]), ("queued", 2))
        self.assertEqual(json.loads(current["snapshot"]), baseline["job"]["snapshot"])
        self.assertEqual(after, before)
        self.assertEqual(grant_state, "queued")
        self.assertEqual(self.service.active_for_job(JOB_ID)["attempt"], 2)
        ci_path = self.workspace / self.request["source_gate"]["ci_evidence"][0]["path"]
        ci_path.write_text("archived elsewhere after recovery")
        self.service.clock = lambda: DEADLINE + 1
        registration_replay = self.service.register(proposal, self.request)
        self.assertEqual(registration_replay["id"], grant_id)
        changed = dict(request, request_key="second-key")
        with self.assertRaises(FactoryError):
            self.service.recover(JOB_ID, changed)

    def test_recover_budget_drift_rolls_back_grant_activation_and_job_queue(self):
        proposal, grant_id, _baseline = self._install_recovery_fixture()
        request = {"schema": RECOVER_SCHEMA, "grant_id": grant_id, "request_key": self.request["request_key"],
                   "proposal_digest": proposal["proposal_digest"]}
        with self.store.connect(True) as con:
            con.execute("DELETE FROM tf_budget_repair WHERE operation_key=(SELECT operation_key FROM tf_budget_repair LIMIT 1)")
        with self.assertRaises(FactoryError):
            self.service.recover(JOB_ID, request)
        with self.store.connect() as con:
            job_state = con.execute("SELECT state,attempt FROM job WHERE id=?", (JOB_ID,)).fetchone()
            grant_state = con.execute("SELECT status FROM tf_evidence_recovery_grant WHERE id=?", (grant_id,)).fetchone()[0]
            relation_count = con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='tf_evidence_recovery'").fetchone()[0]
        self.assertEqual(tuple(job_state), ("failed", 1))
        self.assertEqual(grant_state, "registered")
        self.assertEqual(relation_count, 0)

    def test_api_prepare_route_and_cli_prepare_never_start_worker(self):
        from template_factory.v1_api import dispatch_v1
        with patch("template_factory.evidence_recovery.EvidenceRecoveryService.prepare", return_value={"prepared": True}), \
             patch("template_factory.worker.ensure_worker") as ensure:
            result, status = dispatch_v1("POST", f"jobs/{JOB_ID}/prepare-evidence", "", self.request, self.store)
            self.assertEqual((result, status), ({"prepared": True}, 200))
            ensure.assert_not_called()

        from template_factory.batch_cli import main
        request_path = self.root / "request.json"
        request_path.write_text(json.dumps(self.request))
        output = StringIO()
        with patch("template_factory.evidence_recovery.EvidenceRecoveryService.prepare", return_value={"prepared": True}), \
             patch("template_factory.worker.ensure_worker") as ensure, redirect_stdout(output):
            status = main(["--root", str(self.root / "cli-state"), "--pack", str(self.pack),
                           "evidence-prepare", JOB_ID, "--request", str(request_path)])
            self.assertEqual(status, 0)
            ensure.assert_not_called()


if __name__ == "__main__":
    unittest.main()
