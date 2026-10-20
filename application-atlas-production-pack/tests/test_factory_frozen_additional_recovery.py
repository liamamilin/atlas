"""Additional same-job frozen-review grant and fixed timing-resume coverage."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import test_factory_frozen_link as frozen_fixture  # noqa: E402
JOB_ID, CAMPAIGN, PRODUCT = frozen_fixture.JOB_ID, frozen_fixture.CAMPAIGN, frozen_fixture.PRODUCT
FROZEN_DOCS, FrozenReviewFixtureCLI = frozen_fixture.FROZEN_DOCS, frozen_fixture.FrozenReviewFixtureCLI
from template_factory.store import FactoryError, canonical, digest  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
EXTRA = FROZEN_DOCS / "additional-call-authorization"
ACTUAL_ATTEMPT_2 = FROZEN_DOCS / "actual-attempt-2" / JOB_ID
OLD_DEADLINE = 1792495312.855422
ACTIVATION = 1792495320.0
REMAINING = 4632.611294
EXPECTED_DEADLINE = ACTIVATION + REMAINING
PRED_GRANT = "egrant_c06325f363b84bd9bb1c8fa46f93f945"
PRED_RESERVATION = "bud_c06f643f77bb4ce9a7bad57f30f161e1"
PRED_ACCEPTANCE = "acc_c0cbb5e84d6f475dade4875d8af60174"
REQUEST_KEY = "atlas-g1-r7-frozen-review-additional-2026-10-20-attempt3"
AUTH = {
    "source_ref": "docs/template-factory/g1-frozen-review-recovery-2026-10-20/additional-call-authorization/USER_AUTHORIZATION.txt",
    "source_digest": "4384d1c263c8c553c73b85b2fe6e11533325b64f95c9343fe63a49f4fd97767e",
}
TIMING_AUTH = {
    "source_ref": "docs/template-factory/g1-frozen-review-recovery-2026-10-20/additional-call-authorization/TIMING_OVERRIDE_AUTHORIZATION.txt",
    "source_digest": "373c24f9861e8a789ce71053c6f7a6412921f99a244953c857f9a0c87852a7c9",
}


class AdditionalFrozenReviewTests(unittest.TestCase):
    def setUp(self):
        self.fixture = frozen_fixture.FrozenReviewPipelineLinkTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self._install_attempt_2_baseline()
        from template_factory.frozen_review_recovery import FrozenReviewRecoveryService
        self.service = FrozenReviewRecoveryService(
            self.fixture.store, clock=lambda: ACTIVATION,
            source_gate_validator=lambda _store, gate: dict(gate),
        )
        self.request = self._request()

    def _install_attempt_2_baseline(self):
        """Start from the existing isolated R7 fixture and add the archived quota-failure attempt."""
        store = self.fixture.store
        pack_root = store.pack.parent
        for ref in (AUTH["source_ref"], TIMING_AUTH["source_ref"]):
            target = pack_root / ref
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / ref, target)
        diagnostic_ref = "docs/template-factory/provider-connectivity-2026-10-20/diagnostic.json"
        diagnostic_target = pack_root / diagnostic_ref
        diagnostic_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / diagnostic_ref, diagnostic_target)

        # The archived second call is the immutable predecessor input/source used by prepare().
        target_attempt = store.root / "jobs" / JOB_ID / "attempt-2" / "cognitive-review"
        if target_attempt.exists():
            shutil.rmtree(target_attempt)
        shutil.copytree(ACTUAL_ATTEMPT_2, target_attempt, dirs_exist_ok=True)

        additional_ledger = json.loads((EXTRA / "ledger-after.json").read_text())
        old_final = json.loads((FROZEN_DOCS / "operations/final-state.json").read_text())
        with store.connect(True) as con:
            con.execute("DELETE FROM tf_budget_reservation WHERE campaign_id=?", (CAMPAIGN,))
            for row in additional_ledger:
                columns = [item[1] for item in con.execute("PRAGMA table_info(tf_budget_reservation)")]
                names = [name for name in columns if name in row]
                con.execute(f"INSERT INTO tf_budget_reservation({','.join(names)}) VALUES({','.join('?' for _ in names)})",
                            [row[name] for name in names])
            # Preserve the previous recovery receipt and grant/use rows from the original frozen recovery.
            for row in old_final["acceptances"]:
                con.execute("INSERT OR REPLACE INTO acceptance VALUES(?,?,?,?,?,?,?)",
                            tuple(row[k] for k in ("id", "artifact_id", "digest", "method", "job_id", "body", "created_at")))
            predecessor_acceptance = next(row for row in old_final["acceptances"] if row["id"] == PRED_ACCEPTANCE)
            con.execute("UPDATE job SET state='needs_review',attempt=2,error=?,updated_at=? WHERE id=?",
                        (canonical({"code": "cli_failed", "message": "Go usage limit exceeded"}),
                         predecessor_acceptance["created_at"], JOB_ID))
            # Baseline final-state fixtures keep the original recovery in place; the predecessor itself is
            # already present in the same tables as an authorization receipt and consumed grant.
            for table, key, value in (("tf_evidence_recovery_grant", "id", PRED_GRANT),
                                      ("tf_evidence_recovery_grant_use", "grant_id", PRED_GRANT)):
                archived = next(row for row in old_final["ledger"][table] if row[key] == value)
                columns = [item[1] for item in con.execute(f"PRAGMA table_info({table})")]
                names = [name for name in columns if name in archived]
                con.execute(f"INSERT OR REPLACE INTO {table}({','.join(names)}) VALUES({','.join('?' for _ in names)})",
                            [archived[name] for name in names])
            from template_factory.evidence_recovery import EvidenceRecoveryService
            EvidenceRecoveryService._initialize_locked(con)
            recovery = next(row for row in old_final["recovery_receipts"] if row["grant_id"] == PRED_GRANT)
            columns = [item[1] for item in con.execute("PRAGMA table_info(tf_evidence_recovery)")]
            names = [name for name in columns if name in recovery]
            con.execute(f"INSERT OR REPLACE INTO tf_evidence_recovery({','.join(names)}) VALUES({','.join('?' for _ in names)})",
                        [recovery[name] for name in names])
        self.assertEqual(store.job(JOB_ID)["attempt"], 2)
        with store.connect() as con:
            pred = con.execute("SELECT status,call_attempt,consumed_reservation_id FROM tf_evidence_recovery_grant WHERE id=?", (PRED_GRANT,)).fetchone()
            use = con.execute("SELECT status,reservation_id FROM tf_evidence_recovery_grant_use WHERE grant_id=?", (PRED_GRANT,)).fetchall()
            failed = con.execute("SELECT job_id,status,outcome,requested_model FROM tf_budget_reservation WHERE id=?", (PRED_RESERVATION,)).fetchone()
            acceptance = con.execute("SELECT job_id,created_at,body FROM acceptance WHERE id=?", (PRED_ACCEPTANCE,)).fetchone()
        self.assertEqual(tuple(pred), ("consumed", 2, PRED_RESERVATION))
        self.assertEqual([tuple(r) for r in use], [("consumed", PRED_RESERVATION)])
        self.assertEqual(tuple(failed), (JOB_ID, "failed", "cli_failed", "opencode-go/deepseek-v4.1-flash"))
        self.assertEqual(acceptance["created_at"], "2026-10-20T10:04:40.244128+00:00")
        self.assertIn("Go usage limit exceeded", acceptance["body"])

    def _request(self):
        from template_factory.v1_batches import _g1_source_digest
        return {
            "schema": "atlas.frozen-review-prepare.v1",
            "request_key": REQUEST_KEY,
            "source_authorization": AUTH,
            "timing_override_authorization": TIMING_AUTH,
            "source_gate": {
                "source_commit": "b" * 40,
                "source_tree_digest": _g1_source_digest(self.fixture.store.pack.parent),
                "ci_evidence": [{
                    "path": "docs/template-factory/g1-frozen-review-recovery-2026-10-20/fixture-ci.json",
                    "sha256": "d" * 64, "run_id": 4343, "head_sha": "b" * 40,
                    "required_checks": ["check", "docker-integration"],
                }],
            },
        }

    def _prepare_register_recover(self):
        prepared = self.service.prepare(JOB_ID, self.request)
        self.assertEqual(prepared["schema"], "atlas.frozen-review-recovery-proposal.v1")
        self.assertEqual(prepared["request_key"], REQUEST_KEY)
        self.assertEqual(prepared["materials"]["binding"]["attempt"], 2)
        grant = self.service.register(prepared, self.request)
        recovery_request = {
            "schema": "atlas.frozen-review-recovery.v1", "grant_id": grant["id"],
            "request_key": REQUEST_KEY, "proposal_digest": prepared["proposal_digest"],
        }
        recovered = self.service.recover(JOB_ID, recovery_request)
        return prepared, grant, recovery_request, recovered

    def test_additional_grant_activates_one_fixed_resume_and_replay_does_not_roll_it(self):
        prepared, grant, recovery_request, recovered = self._prepare_register_recover()
        self.assertEqual((recovered["attempt"], recovered["worker_started"]), (3, False))
        with self.fixture.store.connect() as con:
            row = con.execute("SELECT * FROM tf_frozen_review_time_resume WHERE grant_id=?", (grant["id"],)).fetchone()
            calls = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            old_acceptance = con.execute("SELECT body FROM acceptance WHERE id=?", (PRED_ACCEPTANCE,)).fetchone()
            old_grant = con.execute("SELECT status,consumed_reservation_id,call_attempt FROM tf_evidence_recovery_grant WHERE id=?", (PRED_GRANT,)).fetchone()
        self.assertEqual((row["previous_deadline"], row["remaining_seconds"], row["activated_at"], row["effective_deadline"]),
                         (OLD_DEADLINE, REMAINING, ACTIVATION, EXPECTED_DEADLINE))
        self.assertEqual((calls, repairs), (81, 7))
        self.assertIn("Go usage limit exceeded", old_acceptance["body"])
        self.assertEqual(tuple(old_grant), ("consumed", PRED_RESERVATION, 2))

        # A request-key replay remains the same grant and cannot restart the fixed window.
        self.service.clock = lambda: ACTIVATION + 300
        replay = self.service.register(prepared, self.request)
        self.assertEqual(replay["id"], grant["id"])
        replayed = self.service.recover(JOB_ID, recovery_request)
        self.assertTrue(replayed["replayed"])
        with self.fixture.store.connect() as con:
            after = con.execute("SELECT activated_at,effective_deadline FROM tf_frozen_review_time_resume WHERE grant_id=?", (grant["id"],)).fetchone()
        self.assertEqual(tuple(after), (ACTIVATION, EXPECTED_DEADLINE))
        with self.fixture.store.connect() as con:
            old_proposal = json.loads(con.execute("SELECT request_json FROM tf_evidence_recovery_grant WHERE id=?", (PRED_GRANT,)).fetchone()[0])
        old_replay = self.service.recover(JOB_ID, {
            "schema": "atlas.frozen-review-recovery.v1", "grant_id": PRED_GRANT,
            "request_key": old_proposal["request_key"], "proposal_digest": old_proposal["proposal_digest"],
        })
        self.assertTrue(old_replay["replayed"])
        self.assertEqual(old_replay["attempt"], 2)
        self.assertEqual(self.fixture.store.job(JOB_ID)["attempt"], 3)

    def test_changed_authorizations_and_third_grant_are_rejected(self):
        bad = dict(self.request)
        bad["timing_override_authorization"] = {**TIMING_AUTH, "source_digest": "0" * 64}
        with self.assertRaises(FactoryError):
            self.service.prepare(JOB_ID, bad)
        bad = dict(self.request)
        bad["source_authorization"] = {**AUTH, "source_digest": "0" * 64}
        with self.assertRaises(FactoryError):
            self.service.prepare(JOB_ID, bad)
        prepared, grant, _, _ = self._prepare_register_recover()
        alternate = json.loads(json.dumps(prepared))
        alternate["materials"]["frozen_review_call"]["requested_model"] = "changed-model"
        alternate["proposal_digest"] = digest({k: v for k, v in alternate.items() if k != "proposal_digest"})
        with self.assertRaises(FactoryError):
            self.service.register(alternate, self.request)
        with self.fixture.store.connect() as con:
            count = con.execute("SELECT COUNT(*) FROM tf_evidence_recovery_grant WHERE job_id=?", (JOB_ID,)).fetchone()[0]
        self.assertEqual(count, 2)

    def test_single_additional_fake_cli_call_works_after_old_deadline_and_binds_attempt_three(self):
        from template_factory.pipeline import Pipeline
        from template_factory.v1_batches import BatchService

        _prepared, grant, _request, recovered = self._prepare_register_recover()
        self.assertEqual(recovered["attempt"], 3)
        BatchService(self.fixture.store).action(self.fixture.store.job(JOB_ID)["snapshot"]["v1"]["plan_id"], "resume")
        claimed = self.fixture.store.claim("additional-frozen-review-fixture")
        self.assertEqual(claimed["attempt"], 3)
        active = self.service.active_for_job(JOB_ID)
        self.assertEqual(active["grant_id"], grant["id"])
        with self.fixture.store.connect() as con:
            self.assertIsNotNone(con.execute("SELECT 1 FROM tf_frozen_review_time_resume WHERE grant_id=?", (active["grant_id"],)).fetchone())
            from template_factory.frozen_review_additional import get_time_resume_locked
            self.assertIsNotNone(get_time_resume_locked(con, campaign_id=CAMPAIGN, product_id=PRODUCT,
                                                         plan_id=self.fixture.store.job(JOB_ID)["snapshot"]["v1"]["plan_id"],
                                                         grant_id=active["grant_id"]))
        with self.fixture.store.connect(True) as con:
            con.execute("UPDATE job SET lease=? WHERE id=?", (max(time.time(), 1792497820.0) + 3600, JOB_ID))
        cli = FrozenReviewFixtureCLI(self.fixture.store, fault="past_old_deadline")
        Pipeline(self.fixture.store, cli=cli).run(claimed)

        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(cli.calls[0].parent.name, "attempt-3")
        self.assertEqual(self.fixture.store.job(JOB_ID)["state"], "completed")
        with self.fixture.store.connect() as con:
            sessions = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            repairs = con.execute("SELECT COUNT(*) FROM tf_budget_repair WHERE campaign_id=? AND product_id=?", (CAMPAIGN, PRODUCT)).fetchone()[0]
            grants = con.execute("SELECT COUNT(*) FROM tf_evidence_recovery_grant WHERE job_id=?", (JOB_ID,)).fetchone()[0]
            use = con.execute("SELECT status,call_attempt FROM tf_evidence_recovery_grant_use WHERE grant_id=?", (grant["id"],)).fetchone()
            accepts = con.execute("SELECT id,body FROM acceptance WHERE job_id=? ORDER BY created_at,id", (JOB_ID,)).fetchall()
            timer = con.execute("SELECT external_cli_sessions,effective_deadline FROM tf_frozen_review_time_resume WHERE grant_id=?", (grant["id"],)).fetchone()
        self.assertEqual((sessions, repairs, grants), (82, 7, 2))
        self.assertEqual(tuple(use), ("consumed", 3))
        self.assertEqual(len(accepts), 3)
        self.assertEqual(accepts[1]["id"], PRED_ACCEPTANCE)
        self.assertEqual(json.loads(accepts[1]["body"])["outcome"], "unavailable")
        self.assertNotEqual(accepts[2]["id"], PRED_ACCEPTANCE)
        self.assertEqual(json.loads(accepts[2]["body"])["outcome"], "passed")
        self.assertEqual(tuple(timer), (1, EXPECTED_DEADLINE))

    def test_expired_fixed_window_and_global_500_session_cap_do_not_authorize_a_call(self):
        from template_factory.pipeline import Pipeline
        from template_factory.v1_batches import BatchService

        _prepared, grant, _request, _recovered = self._prepare_register_recover()
        BatchService(self.fixture.store).action(self.fixture.store.job(JOB_ID)["snapshot"]["v1"]["plan_id"], "resume")
        claimed = self.fixture.store.claim("expired-resume-fixture")
        with self.fixture.store.connect() as con:
            deadline = con.execute("SELECT effective_deadline FROM tf_frozen_review_time_resume WHERE grant_id=?", (grant["id"],)).fetchone()[0]
        with self.fixture.store.connect(True) as con:
            con.execute("UPDATE job SET lease=? WHERE id=?", (deadline + 3600, JOB_ID))
        cli = FrozenReviewFixtureCLI(self.fixture.store, fault="expired_resume")
        with self.assertRaises(FactoryError) as caught:
            Pipeline(self.fixture.store, cli=cli).run(claimed)
        self.assertEqual(caught.exception.code, "budget_deadline")
        self.assertEqual(len(cli.calls), 1)
        self.assertEqual(self.fixture.store.job(JOB_ID)["attempt"], 3)
        with self.fixture.store.connect() as con:
            active = con.execute("SELECT status FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()[0]
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
        self.assertEqual((active, charged), ("queued", 81))


    def test_external_diagnostic_session_counts_toward_the_global_500_cap(self):
        from template_factory.pipeline import Pipeline
        from template_factory.v1_batches import BatchService

        _prepared, grant, _request, _recovered = self._prepare_register_recover()
        with self.fixture.store.connect(True) as con:
            # 81 archived sessions plus 418 synthetic historical sessions makes 499 ledger rows.
            for index in range(418):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created) VALUES(?,?,?,?,?,?,?)",
                            (f"cap-{index}", CAMPAIGN, PRODUCT, "G1", "review", "completed", index))
        BatchService(self.fixture.store).action(self.fixture.store.job(JOB_ID)["snapshot"]["v1"]["plan_id"], "resume")
        claimed = self.fixture.store.claim("cap-resume-fixture")
        with self.fixture.store.connect(True) as con:
            con.execute("UPDATE job SET lease=? WHERE id=?", (1792497820.0 + 3600, JOB_ID))
        cli = FrozenReviewFixtureCLI(self.fixture.store, fault="past_old_deadline")
        with self.assertRaises(FactoryError) as caught:
            Pipeline(self.fixture.store, cli=cli).run(claimed)
        self.assertEqual(caught.exception.code, "budget_exhausted")
        self.assertEqual(len(cli.calls), 1)
        with self.fixture.store.connect() as con:
            charged = con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE campaign_id=? AND status!='not_started'", (CAMPAIGN,)).fetchone()[0]
            state = con.execute("SELECT status FROM tf_evidence_recovery_grant WHERE id=?", (grant["id"],)).fetchone()[0]
        self.assertEqual((charged, state), (499, "queued"))


if __name__ == "__main__":
    unittest.main()
