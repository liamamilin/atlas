import hashlib
import json
from pathlib import Path
import sqlite3
import shutil
import sys
import tempfile
import threading
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import BudgetLedger, G1_AMENDMENT_CAMPAIGN
from template_factory.protocol_grants import (
    CONTEXT_KEYS, DEADLINE, JOB_ID, OPERATION_ID, RETRY_SCOPE,
    SOURCE_FAILURE_RESERVATION_ID, STAGE, ProtocolRetryGrantService,
    protocol_retry_request,
)
from template_factory.store import FactoryError, FactoryStore


class ProtocolGrantTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "application-atlas-production-pack"
        self.pack.mkdir()
        self.repo = Path(__file__).resolve().parents[2]
        source = self.repo / "docs/template-factory/g1-protocol-recovery-2026-10-19/authorization/ATLAS_G1_PROTOCOL_RETRY_CODEX_INSTRUCTIONS.txt"
        target = self.root / "docs/template-factory/g1-protocol-recovery-2026-10-19/authorization/ATLAS_G1_PROTOCOL_RETRY_CODEX_INSTRUCTIONS.txt"
        target.parent.mkdir(parents=True)
        shutil.copyfile(source, target)
        self.now = [DEADLINE - 100]
        self.store = FactoryStore(self.root / "state", self.pack)
        evidence_source = self.repo / "docs/template-factory/g1-protocol-recovery-2026-10-19/original-phase-input"
        evidence_target = self.store.root / "jobs" / JOB_ID / "attempt-1" / STAGE
        shutil.copytree(evidence_source, evidence_target)
        self.ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.now[0])
        self.service = ProtocolRetryGrantService(self.store, clock=lambda: self.now[0])
        self._seed_baseline()

    def tearDown(self):
        self.temp.cleanup()

    def _seed_baseline(self):
        from template_factory.protocol_grants import G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", DEADLINE - 8 * 3600, DEADLINE))
            for index in range(5):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"repair-{index}", 100 + index))
            for index in range(56):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,job_id,requested_model,stage,retry,group_kind,retry_scope,outcome) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (SOURCE_FAILURE_RESERVATION_ID if index == 0 else f"old-{index}", G1_AMENDMENT_CAMPAIGN,
                             G1_AMENDMENT_PRODUCT, "G1", "transient_retry" if index < 3 else "production",
                             "failed" if index < 3 else "completed", 100 + index,
                             JOB_ID if index == 0 else None,
                             "opencode-go/deepseek-v4.1-flash" if index == 0 else None,
                             OPERATION_ID if index == 0 else STAGE if index < 3 else f"old-stage-{index}",
                             None if index == 0 else index if index < 3 else None,
                             "production", RETRY_SCOPE if index < 3 else None,
                             "cli_protocol" if index == 0 else None))
            snapshot = {"v1": {"plan_id": G1_AMENDMENT_PLAN, "product_id": G1_AMENDMENT_PRODUCT,
                               "campaign_id": G1_AMENDMENT_CAMPAIGN}, "scenario": {}}
            con.execute("INSERT INTO job(id,batch_id,kind,state,stage,attempt,token,lease,snapshot,error,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (JOB_ID, "batch", "blueprint-production", "paused_budget", STAGE, 2, None, None,
                         json.dumps(snapshot), "budget_retry_limit: transient retry limit exhausted", "now", "now"))

    def request(self):
        return protocol_retry_request(self.store)

    def context(self):
        request = self.request()
        return {key: request[key] for key in CONTEXT_KEYS}

    def register(self, request):
        return self.service.register(request)

    def test_registration_is_exact_idempotent_and_precedes_baseline_recheck(self):
        request = self.request()
        first = self.register(request)
        self.assertEqual(first["status"], "available")
        self.assertEqual(first["max_extra_calls"], 1)
        with self.store.connect(True) as con:
            con.execute("UPDATE tf_budget_reservation SET status='completed' WHERE id='old-2'")
        self.assertEqual(self.service.register(request)["id"], first["id"])
        with self.assertRaises(FactoryError) as conflict:
            self.register({**request, "requested_model": "different"})
        self.assertEqual(conflict.exception.code, "idempotency_conflict")
        with self.assertRaises(FactoryError):
            self.register({**request, "idempotency_key": "another-key"})
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_protocol_retry_grant").fetchone()[0], 1)

    def test_exact_grant_allows_one_retry_and_records_linkage(self):
        grant = self.register(self.request())
        reservation = self.ledger.reserve(
            "product-c42848f63251507bd9d911a5", "G1", "review", 120,
            job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash", stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
            plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=self.context())
        self.assertEqual(reservation["protocol_grant_id"], grant["id"])
        with self.assertRaises(FactoryError) as exhausted:
            self.ledger.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                                job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash", stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                                plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=self.context())
        self.assertEqual(exhausted.exception.code, "budget_retry_limit")
        with self.store.connect() as con:
            use = con.execute("SELECT * FROM tf_protocol_retry_grant_use WHERE grant_id=?", (grant["id"],)).fetchone()
            self.assertEqual(use["reservation_id"], reservation["id"])
        self.ledger.mark_started(reservation["id"])
        self.assertEqual(self.service.get(grant["id"])["status"], "consumed")
        self.ledger.finish(reservation["id"], "completed")

    def test_mismatch_concurrency_deadline_and_proven_not_started_release(self):
        with self.assertRaises(FactoryError) as missing:
            self.ledger.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                                job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash",
                                stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                                plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=self.context())
        self.assertEqual(missing.exception.code, "budget_retry_limit")
        grant = self.register(self.request())
        for key, value in (("input_digest", "wrong"), ("prompt_sha256", "wrong"),
                           ("projection_digest", "wrong")):
            bad = {**self.context(), key: value}
            with self.subTest(key=key), self.assertRaises(FactoryError):
                self.ledger.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                                    job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash", stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                                    plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=bad)
        outcomes = []
        barrier = threading.Barrier(2)
        def reserve():
            barrier.wait()
            try:
                outcomes.append(self.ledger.reserve(
                    "product-c42848f63251507bd9d911a5", "G1", "review", 120,
                    job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash", stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                    plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=self.context()))
            except FactoryError as exc:
                outcomes.append(exc.code)
        threads = [threading.Thread(target=reserve) for _ in range(2)]
        for thread in threads: thread.start()
        for thread in threads: thread.join()
        self.assertEqual(sum(isinstance(item, dict) for item in outcomes), 1)
        reservation = next(item for item in outcomes if isinstance(item, dict))
        self.ledger.release_not_started(reservation["id"])
        self.assertEqual(self.service.get(grant["id"])["status"], "available")
        self.assertEqual(self.service.get(grant["id"])["consumed_reservation_id"], None)
        with self.store.connect() as con:
            use = con.execute("SELECT status,released_at FROM tf_protocol_retry_grant_use WHERE reservation_id=?",
                              (reservation["id"],)).fetchone()
            self.assertEqual(use["status"], "not_started")
            self.assertIsNotNone(use["released_at"])
        self.now[0] = DEADLINE
        with self.assertRaises(FactoryError) as expired:
            self.ledger.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                                job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash", stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                                plan_id="plan_87059846caf345d2b2fe690657cf324f", protocol_context=self.context())
        self.assertEqual(expired.exception.code, "budget_deadline")

    def test_wrong_campaign_job_operation_model_plan_or_segment_cannot_claim(self):
        grant = self.register(self.request())
        cases = (
            ("job_id", "job-other"),
            ("stage", "different-operation"),
            ("requested_model", "different-model"),
            ("plan_id", "different-plan"),
            ("phase", "T08"),
        )
        base = {"identity": "product-c42848f63251507bd9d911a5", "phase": "G1",
                "kind": "review", "timeout": 120, "job_id": JOB_ID,
                "requested_model": "opencode-go/deepseek-v4.1-flash", "stage": OPERATION_ID,
                "retry": 1, "retry_scope": RETRY_SCOPE,
                "plan_id": "plan_87059846caf345d2b2fe690657cf324f",
                "protocol_context": self.context()}
        for name, value in cases:
            args = {**base, name: value}
            if name == "phase":
                self.ledger.begin_segment("T08")
            with self.subTest(binding=name), self.assertRaises(FactoryError) as caught:
                self.ledger.reserve(**args)
            self.assertEqual(caught.exception.code, "budget_retry_limit")

        other = BudgetLedger(self.store, campaign_id="other-campaign", clock=lambda: self.now[0])
        other.begin_segment("G1")
        with self.store.connect(True) as con:
            for index in range(2):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,stage,retry,group_kind,retry_scope) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                            (f"other-retry-{index}", "other-campaign", base["identity"], "G1", "review",
                             "failed", 1 + index, OPERATION_ID, index + 1, "production", RETRY_SCOPE))
        with self.assertRaises(FactoryError) as wrong_campaign:
            other.reserve(**base)
        self.assertEqual(wrong_campaign.exception.code, "budget_retry_limit")
        self.assertEqual(self.service.get(grant["id"])["status"], "available")
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_protocol_retry_grant_use WHERE grant_id=?",
                                         (grant["id"],)).fetchone()[0], 0)

    def test_stricter_configured_retry_limit_is_not_overridden(self):
        grant = self.register(self.request())
        strict = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN,
                              limits={"transient_retries": 1}, clock=lambda: self.now[0])
        with self.assertRaises(FactoryError) as caught:
            strict.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                           job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash",
                           stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                           plan_id="plan_87059846caf345d2b2fe690657cf324f",
                           protocol_context=self.context())
        self.assertEqual(caught.exception.code, "budget_retry_limit")
        self.assertEqual(self.service.get(grant["id"])["status"], "available")

    def test_fault_after_grant_link_rolls_back_reservation_and_keeps_grant_available(self):
        grant = self.register(self.request())
        with self.store.connect(True) as con:
            con.execute("CREATE TRIGGER inject_protocol_grant_update_failure BEFORE UPDATE ON tf_protocol_retry_grant BEGIN SELECT RAISE(ABORT,'injected grant update fault'); END")
        with self.assertRaises(sqlite3.IntegrityError):
            self.ledger.reserve("product-c42848f63251507bd9d911a5", "G1", "review", 120,
                                job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash",
                                stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                                plan_id="plan_87059846caf345d2b2fe690657cf324f",
                                protocol_context=self.context())
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_budget_reservation WHERE id NOT LIKE 'old-%' AND id!=?",
                                         (SOURCE_FAILURE_RESERVATION_ID,)).fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_protocol_retry_grant_use WHERE grant_id=?",
                                         (grant["id"],)).fetchone()[0], 0)
        self.assertEqual(self.service.get(grant["id"])["status"], "available")

    def _assert_consumption_stays_spent(self, outcome):
        grant = self.register(self.request())
        reservation = self.ledger.reserve(
            "product-c42848f63251507bd9d911a5", "G1", "review", 120,
            job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash",
            stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
            plan_id="plan_87059846caf345d2b2fe690657cf324f",
            protocol_context=self.context())
        self.ledger.mark_started(reservation["id"])
        if outcome == "uncertain":
            self.ledger.finish(reservation["id"], "uncertain")
        with self.assertRaises(FactoryError) as denied:
            self.ledger.release_not_started(reservation["id"])
        self.assertEqual(denied.exception.code, "budget_release_denied")
        self.assertEqual(self.service.get(grant["id"])["status"], outcome)
        with self.assertRaises(FactoryError) as no_reclaim:
            self.ledger.reserve(
                "product-c42848f63251507bd9d911a5", "G1", "review", 120,
                job_id=JOB_ID, requested_model="opencode-go/deepseek-v4.1-flash",
                stage=OPERATION_ID, retry=1, retry_scope=RETRY_SCOPE,
                plan_id="plan_87059846caf345d2b2fe690657cf324f",
                protocol_context=self.context())
        self.assertEqual(no_reclaim.exception.code, "budget_retry_limit")

    def test_started_reservation_cannot_be_released_or_reclaimed(self):
        self._assert_consumption_stays_spent("consumed")

    def test_uncertain_reservation_cannot_be_released_or_reclaimed(self):
        self._assert_consumption_stays_spent("uncertain")


if __name__ == "__main__":
    unittest.main()
