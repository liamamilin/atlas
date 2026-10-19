import hashlib
import json
from pathlib import Path
import tempfile
import threading
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import BudgetAmendmentService, BudgetLedger, G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_OLD_DEADLINE, G1_AMENDMENT_PLAN, G1_AMENDMENT_PRODUCT, G1_AUTHORIZATION_SOURCE_DIGEST
from template_factory.cli import CLI
from template_factory.pipeline import _budget_next_retry, _budget_operation_identity, _budget_prior_calls, _budget_scope_history, _is_forced_transient_retry, _stable_retry_scope
from template_factory.store import FactoryError, FactoryStore


class FactoryBudgetV1Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        self.now = [1000.0]
        self.store = FactoryStore(self.root / "state", self.pack)
        self.ledger = BudgetLedger(self.store, clock=lambda: self.now[0])

    def tearDown(self):
        self.temp.cleanup()

    def reserve(self, identity="product-a", phase="G1", kind="production", **kwargs):
        return self.ledger.reserve(identity, phase, kind, 3600, **kwargs)

    def _amendment_request(self, **overrides):
        return {"product_id": G1_AMENDMENT_PRODUCT, "plan_id": G1_AMENDMENT_PLAN,
                "source_ref": "ATLAS_G1_CONVERGENCE_CODEX_INSTRUCTIONS.txt",
                "source_digest": G1_AUTHORIZATION_SOURCE_DIGEST, "summary": "User-authorized G1 bounded amendment",
                "reason": "Finish the explicitly authorized single G1 continuation.",
                "idempotency_key": "g1-continuation-v1", **overrides}

    def _seed_original_g1_deadline(self):
        with self.store.connect(True) as con:
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", 100.0, G1_AMENDMENT_OLD_DEADLINE))
            for index in range(2):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"old-repair-{index}", 100.0 + index))
            for index in range(42):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind) VALUES(?,?,?,?,?,?,?,?)",
                            (f"old-reservation-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, "G1", "production", "completed", 500.0 + index, "production"))

    def test_g1_amendment_is_scoped_append_only_and_activates_once(self):
        self.now[0] = G1_AMENDMENT_OLD_DEADLINE + 10
        service = BudgetAmendmentService(self.store, clock=lambda: self.now[0])
        ledger = BudgetLedger(self.store, campaign_id=G1_AMENDMENT_CAMPAIGN, clock=lambda: self.now[0])
        with self.assertRaises(FactoryError) as caught:
            service.register(self._amendment_request(product_id="other-product"))
        self.assertEqual(caught.exception.code, "budget_amendment_scope")
        self._seed_original_g1_deadline()
        self.assertEqual(ledger.snapshot()["cli_sessions_used"], 42)
        self.assertEqual(ledger.snapshot()["limits"]["cli_sessions"], 500)
        self.assertEqual(ledger.snapshot()["limits"]["product_repairs"], 2)
        amendment = service.register(self._amendment_request())
        self.assertEqual(amendment["baseline_repair_count"], 2)
        self.assertEqual(amendment["baseline_cli_sessions"], 42)
        self.assertIsNone(amendment["activated_at"])
        replay = service.register(self._amendment_request())
        self.assertEqual(replay["id"], amendment["id"])
        self.assertEqual(len(service.list()), 1)
        with self.assertRaises(FactoryError):
            ledger.record_repair(G1_AMENDMENT_PRODUCT, "before-activation")
        activated = service.activate(amendment["id"])
        self.assertEqual(activated["new_deadline"], self.now[0] + 8 * 60 * 60)
        self.assertEqual(ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id=G1_AMENDMENT_PLAN), activated["new_deadline"])
        self.assertEqual(ledger.effective_deadline(G1_AMENDMENT_PRODUCT), G1_AMENDMENT_OLD_DEADLINE)
        self.assertEqual(ledger.effective_deadline(G1_AMENDMENT_PRODUCT, plan_id="plan_other"), G1_AMENDMENT_OLD_DEADLINE)
        self.assertEqual(ledger.effective_deadline("other-product"), G1_AMENDMENT_OLD_DEADLINE)
        with self.assertRaises(FactoryError):
            ledger.record_repair(G1_AMENDMENT_PRODUCT, "wrong-plan-extra", plan_id="plan_other")
        for index in range(2, 4):
            result = ledger.record_repair(G1_AMENDMENT_PRODUCT, f"authorized-{index}", plan_id=G1_AMENDMENT_PLAN)
            self.assertEqual(result["repair_limit"], 4)
        with self.assertRaises(FactoryError):
            ledger.record_repair(G1_AMENDMENT_PRODUCT, "unauthorized-fifth", plan_id=G1_AMENDMENT_PLAN)
        same = service.activate(amendment["id"])
        self.assertEqual(same["new_deadline"], activated["new_deadline"])
        self.assertEqual(ledger.phase_remaining(G1_AMENDMENT_PRODUCT, "G1", plan_id=G1_AMENDMENT_PLAN), 8 * 60 * 60)
        self.assertEqual(ledger.phase_remaining("other-product", "G1"), 0)
        for index in range(2):
            ledger.record_repair("other-product", f"other-{index}")
        with self.assertRaises(FactoryError):
            ledger.record_repair("other-product", "other-third")

    def test_g1_amendment_rejects_other_campaign_and_mismatched_idempotent_request(self):
        self._seed_original_g1_deadline()
        service = BudgetAmendmentService(self.store, clock=lambda: self.now[0])
        amendment = service.register(self._amendment_request())
        with self.assertRaises(FactoryError) as caught:
            BudgetAmendmentService(self.store, campaign_id="other-campaign").register(self._amendment_request())
        self.assertEqual(caught.exception.code, "budget_amendment_scope")
        with self.assertRaises(FactoryError) as caught:
            service.register(self._amendment_request(summary="Changed replay payload"))
        self.assertEqual(caught.exception.code, "idempotency_conflict")
        self.assertIsNone(amendment["activated_at"])

    def test_first_amendment_registration_migrates_legacy_budget_schema(self):
        legacy_root = self.root / "legacy"
        legacy_root.mkdir()
        legacy_pack = legacy_root / "pack"
        legacy_pack.mkdir()
        legacy_store = FactoryStore(legacy_root / "state", legacy_pack)
        with legacy_store.connect(True) as con:
            con.execute("CREATE TABLE tf_budget_phase (campaign_id TEXT NOT NULL, identity TEXT NOT NULL, phase TEXT NOT NULL, started REAL NOT NULL, deadline REAL NOT NULL, PRIMARY KEY(campaign_id,identity,phase))")
            con.execute("CREATE TABLE tf_budget_reservation (id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,identity TEXT NOT NULL,phase TEXT NOT NULL,kind TEXT NOT NULL,status TEXT NOT NULL,created REAL NOT NULL,started REAL,finished REAL,job_id TEXT,requested_model TEXT,requested_effort TEXT,stage TEXT,retry INTEGER,observed_model TEXT,observed_effort TEXT,outcome TEXT,group_kind TEXT NOT NULL DEFAULT 'production')")
            con.execute("CREATE TABLE tf_budget_repair (campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,operation_key TEXT NOT NULL,created REAL NOT NULL,PRIMARY KEY(campaign_id,product_id,operation_key))")
            con.execute("INSERT INTO tf_budget_phase VALUES(?,?,?,?,?)",
                        (G1_AMENDMENT_CAMPAIGN, "__campaign_segment__", "G1", 100.0, G1_AMENDMENT_OLD_DEADLINE))
            for index in range(2):
                con.execute("INSERT INTO tf_budget_repair VALUES(?,?,?,?)",
                            (G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT, f"legacy-repair-{index}", 200.0 + index))
            for index in range(42):
                con.execute("INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created) VALUES(?,?,?,?,?,?,?)",
                            (f"legacy-call-{index}", G1_AMENDMENT_CAMPAIGN, G1_AMENDMENT_PRODUCT,
                             "G1", "production", "completed", 300.0 + index))
            self.assertIsNone(con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='tf_budget_amendment'").fetchone())
        service = BudgetAmendmentService(legacy_store, clock=lambda: 400.0)
        amendment = service.register(self._amendment_request())
        self.assertIsNone(amendment["activated_at"])
        snapshot = BudgetLedger(legacy_store, campaign_id=G1_AMENDMENT_CAMPAIGN).snapshot()
        self.assertEqual(snapshot["cli_sessions_used"], 42)
        self.assertEqual(snapshot["limits"]["cli_sessions"], 500)
        self.assertEqual(snapshot["limits"]["product_repairs"], 2)
        self.assertEqual(snapshot["repairs"], [{"product_id": G1_AMENDMENT_PRODUCT, "repairs_used": 2}])

    def test_concurrent_reservations_are_atomic_and_reservation_counts_against_limit(self):
        ledger = BudgetLedger(self.store, limits={"production_concurrency": 1}, clock=lambda: self.now[0])
        outcomes = []
        barrier = threading.Barrier(2)

        def reserve(identity):
            barrier.wait()
            try:
                outcomes.append(ledger.reserve(identity, "G1", "production", 60))
            except FactoryError as exc:
                outcomes.append(exc.code)

        threads = [threading.Thread(target=reserve, args=(f"p-{i}",)) for i in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sum(isinstance(item, dict) for item in outcomes), 1)
        self.assertIn("budget_concurrency", outcomes)
        self.assertEqual(ledger.snapshot()["active"], 1)

    def test_concurrent_duplicate_initial_calls_cannot_both_bypass_retry_scope(self):
        outcomes = []
        barrier = threading.Barrier(2)

        def reserve():
            barrier.wait()
            try:
                outcomes.append(self.ledger.reserve(
                    "product-a", "G1", "review", 60, stage="review:fixed-input",
                    retry_scope="cognitive-review", job_id="same-operation",
                ))
            except FactoryError as error:
                outcomes.append(error.code)

        threads = [threading.Thread(target=reserve) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(sum(isinstance(value, dict) for value in outcomes), 1)
        self.assertIn("budget_retry_limit", outcomes)
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 1)

    def test_changed_operation_stays_initial_but_explicit_protocol_repair_uses_scope_retry(self):
        self.assertIsNone(_budget_next_retry(0, 2, scope_retries=2))
        self.assertEqual(_budget_next_retry(0, 2, forced_transient=True, scope_retries=0), 1)
        with self.assertRaises(FactoryError) as caught:
            _budget_next_retry(0, 2, forced_transient=True, scope_retries=2)
        self.assertEqual(caught.exception.code, "budget_retry_limit")
        self.assertTrue(_is_forced_transient_retry("blueprint-code-0-patch-repair-1"))
        self.assertTrue(_is_forced_transient_retry("blueprint-code-2-4-repair-0"))
        self.assertTrue(_is_forced_transient_retry("blueprint-research-protocol-repair-1"))
        self.assertFalse(_is_forced_transient_retry("blueprint-code-2-5"))
        self.assertFalse(_is_forced_transient_retry("blueprint-code-8-3"))
        self.assertFalse(_is_forced_transient_retry("blueprint-generate-1"))
        first = self.ledger.reserve("product-a", "G1", "production", 50,
                                    stage="blueprint-generate-0", retry=1,
                                    retry_scope="blueprint-generate")
        self.ledger.mark_started(first["id"])
        with self.store.connect() as con:
            history = _budget_scope_history(con, "default", "product-a", "blueprint-generate", "job-2")
        self.assertEqual(history, {"retries": 1})

    def test_dependency_manifest_repairs_consume_real_code_scope_retry_allowance(self):
        initial = self.ledger.reserve(
            "product-a", "G1", "production", 50,
            stage="blueprint-code-2-4", retry_scope="blueprint-code", job_id="job-code",
        )
        self.ledger.mark_started(initial["id"])
        self.ledger.finish(initial["id"], "completed")

        for fix in (0, 1):
            repair_name = f"blueprint-code-2-4-repair-{fix}"
            self.assertTrue(_is_forced_transient_retry(repair_name))
            with self.store.connect() as con:
                history = _budget_scope_history(con, "default", "product-a", "blueprint-code", "job-code")
            retry = _budget_next_retry(0, 2, forced_transient=True, scope_retries=history["retries"])
            reservation = self.ledger.reserve(
                "product-a", "G1", "production", 50, stage=repair_name,
                retry=retry, retry_scope="blueprint-code", job_id="job-code",
            )
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
            self.assertEqual(retry, fix + 1)

        with self.store.connect() as con:
            history = _budget_scope_history(con, "default", "product-a", "blueprint-code", "job-code")
        with self.assertRaises(FactoryError) as caught:
            _budget_next_retry(0, 2, forced_transient=True, scope_retries=history["retries"])
        self.assertEqual(caught.exception.code, "budget_retry_limit")

    def test_restart_and_new_job_do_not_reset_segment_deadline_or_call_count(self):
        ledger = BudgetLedger(self.store, limits={"cli_sessions": 2, "phase_seconds": 100}, clock=lambda: self.now[0])
        first = ledger.reserve("product-a", "G1", timeout=90, job_id="job-1")
        ledger.mark_started(first["id"])
        ledger.finish(first["id"], "completed")
        self.now[0] += 30
        restarted = BudgetLedger(self.store, limits={"cli_sessions": 2, "phase_seconds": 100}, clock=lambda: self.now[0])
        second = restarted.reserve("product-b", "G1", timeout=90, job_id="job-2")
        self.assertEqual(second["timeout"], 70)
        restarted.mark_started(second["id"])
        restarted.finish(second["id"], "completed")
        with self.assertRaises(FactoryError) as caught:
            restarted.reserve("product-c", "G1", timeout=1, job_id="job-3")
        self.assertEqual(caught.exception.code, "budget_exhausted")

    def test_pause_or_restart_does_not_reset_expired_deadline(self):
        ledger = BudgetLedger(self.store, limits={"phase_seconds": 10}, clock=lambda: self.now[0])
        first = ledger.reserve("p1", "T08", timeout=100)
        self.assertEqual(first["timeout"], 10)
        ledger.release_not_started(first["id"])
        self.now[0] += 10
        restarted = BudgetLedger(self.store, limits={"phase_seconds": 10}, clock=lambda: self.now[0])
        with self.assertRaises(FactoryError) as caught:
            restarted.reserve("p2", "T08", timeout=100)
        self.assertEqual(caught.exception.code, "budget_deadline")

    def test_uncertain_reservation_survives_restart_and_cannot_be_refunded(self):
        reservation = self.reserve()
        self.ledger.mark_started(reservation["id"])
        self.ledger.finish(reservation["id"], "uncertain")
        restarted = BudgetLedger(self.store, limits={"production_concurrency": 1}, clock=lambda: self.now[0])
        with self.assertRaises(FactoryError) as caught:
            restarted.reserve("another", "G1", timeout=30)
        self.assertEqual(caught.exception.code, "budget_concurrency")
        with self.assertRaises(FactoryError) as caught:
            restarted.release_not_started(reservation["id"])
        self.assertEqual(caught.exception.code, "budget_release_denied")

    def test_retry_budget_is_cumulative_by_product_and_stage_not_job(self):
        for retry, job in ((1, "job-a"), (2, "job-b")):
            reservation = self.ledger.reserve("product-a", "G1", "production", 50,
                                              stage="generate-0", retry=retry, job_id=job)
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-a", "G1", "production", 50,
                                stage="generate-0", retry=1, job_id="new-job")
        self.assertEqual(caught.exception.code, "budget_retry_limit")

    def test_stable_scope_counts_legacy_cognitive_review_retries_across_new_artifacts(self):
        for retry, stage in ((1, "cognitive-review:old-zh-input"), (2, "cognitive-review:old-zh-input")):
            reservation = self.ledger.reserve("product-a", "G1", "review", 50,
                                              stage=stage, retry=retry, job_id=f"legacy-{retry}")
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
        # A repaired artifact is allowed a fresh initial call, but its next retry
        # remains inside the same campaign/product/review allowance.
        initial = self.ledger.reserve("product-a", "G1", "review", 50,
                                      stage="cognitive-review:new-artifact", job_id="repair-review",
                                      retry_scope="cognitive-review")
        self.ledger.mark_started(initial["id"])
        self.ledger.finish(initial["id"], "completed")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-a", "G1", "review", 50,
                                stage="cognitive-review:new-artifact", retry=1,
                                retry_scope="cognitive-review", job_id="repair-review-retry")
        self.assertEqual(caught.exception.code, "budget_retry_limit")

    def test_legacy_p0_digest_retries_count_toward_stable_delivery_scope(self):
        for retry, stage in ((1, "p0-delivery:old-digest"), (2, "p0-delivery:old-digest")):
            reservation = self.ledger.reserve("product-a", "G1", "production", 50,
                                              stage=stage, retry=retry, job_id=f"p0-{retry}")
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-a", "G1", "production", 50,
                                stage="p0-delivery:new-digest", retry=1,
                                retry_scope="p0-delivery", job_id="p0-new-retry")
        self.assertEqual(caught.exception.code, "budget_retry_limit")

    def test_indexed_legacy_cognitive_stages_normalize_without_merging_review_dimensions(self):
        self.assertEqual(_stable_retry_scope("blueprint-generate-3-patch-repair-0"), "blueprint-generate")
        self.assertEqual(_stable_retry_scope("blueprint-spec-review-0-category_evidence"), "blueprint-spec-review:category_evidence")
        self.assertEqual(_stable_retry_scope("blueprint-spec-review-2-phase_acceptance"), "blueprint-spec-review:phase_acceptance")
        self.assertNotEqual(
            _stable_retry_scope("blueprint-spec-review-0-category_evidence"),
            _stable_retry_scope("blueprint-spec-review-2-phase_acceptance"),
        )

    def test_indexed_legacy_review_retries_are_counted_only_for_the_same_dimension(self):
        for retry, stage in ((1, "blueprint-spec-review-0-category_evidence:old-a"),
                             (2, "blueprint-spec-review-1-category_evidence:old-b")):
            reservation = self.ledger.reserve("product-a", "G1", "production", 50,
                                              stage=stage, retry=retry, job_id=f"review-{retry}")
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-a", "G1", "production", 50,
                                stage="blueprint-spec-review-2-category_evidence:new",
                                retry=1, retry_scope="blueprint-spec-review:category_evidence")
        self.assertEqual(caught.exception.code, "budget_retry_limit")
        other_dimension = self.ledger.reserve(
            "product-a", "G1", "production", 50,
            stage="blueprint-spec-review-2-phase_acceptance:new", retry=1,
            retry_scope="blueprint-spec-review:phase_acceptance",
        )
        self.assertIsNotNone(other_dimension["id"])

    def test_fixed_input_identity_ignores_language_but_retains_legacy_hash_aliases(self):
        zh, zh_aliases = _budget_operation_identity("cognitive-review", {"artifact_digest": "same", "language": "zh"})
        en, en_aliases = _budget_operation_identity("cognitive-review", {"artifact_digest": "same", "language": "en"})
        repaired, _ = _budget_operation_identity("cognitive-review", {"artifact_digest": "new", "language": "en"})
        self.assertEqual(zh, en)
        self.assertIn("cognitive-review:" + hashlib.sha256(
            json.dumps({"artifact_digest": "same", "language": "zh"}, ensure_ascii=False,
                       sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16], en_aliases)
        self.assertEqual(set(zh_aliases), set(en_aliases))
        self.assertNotEqual(zh, repaired)

    def test_legacy_initial_and_two_retries_remain_visible_after_language_changes(self):
        original_payload = {"artifact_digest": "fixed-artifact", "language": "zh"}
        legacy_operation = "cognitive-review:" + hashlib.sha256(
            json.dumps(original_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()[:16]
        for retry in (None, 1, 2):
            reservation = self.ledger.reserve(
                "product-a", "G1", "review", 50, stage=legacy_operation,
                retry=retry, job_id=f"legacy-review-{retry}",
            )
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "failed")
        _, aliases = _budget_operation_identity("cognitive-review", {"artifact_digest": "fixed-artifact", "language": "en"})
        with self.store.connect() as con:
            prior_calls = _budget_prior_calls(con, "default", "product-a", aliases)
            self.assertEqual(prior_calls, 3)
        with self.assertRaises(FactoryError) as caught:
            _budget_next_retry(prior_calls, self.ledger.limits["transient_retries"])
        self.assertEqual(caught.exception.code, "budget_retry_limit")
        before = self.ledger.snapshot()["cli_sessions_used"]
        self.assertEqual(before, 3)
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], before)

    def test_segment_deadline_begins_at_official_start_and_pause_does_not_reset_it(self):
        ledger = BudgetLedger(self.store, limits={"phase_seconds": 100}, clock=lambda: self.now[0])
        ledger.begin_segment("G1")
        self.now[0] += 35
        ledger.pause("operator_pause")
        with self.assertRaises(FactoryError) as caught:
            ledger.reserve("p1", "G1", timeout=50)
        self.assertEqual(caught.exception.code, "budget_paused")
        restarted = BudgetLedger(self.store, limits={"phase_seconds": 100}, clock=lambda: self.now[0])
        self.assertTrue(restarted.snapshot()["paused"])
        restarted.resume()
        reservation = restarted.reserve("p1", "G1", timeout=50)
        self.assertEqual(reservation["timeout"], 50)
        self.now[0] += 20
        second = restarted.reserve("p2", "G1", timeout=90)
        self.assertEqual(second["timeout"], 45)

    def test_old_ledger_reloads_lower_limits_and_new_instance_cannot_raise_them(self):
        lower = BudgetLedger(self.store, limits={"cli_sessions": 2, "production_concurrency": 1}, clock=lambda: self.now[0])
        first = self.ledger.reserve("p1", "G1", timeout=30)
        with self.assertRaises(FactoryError) as caught:
            lower.reserve("p2", "G1", timeout=30)
        self.assertEqual(caught.exception.code, "budget_concurrency")
        self.ledger.mark_started(first["id"])
        self.ledger.finish(first["id"], "completed")
        second = self.ledger.reserve("p2", "G1", timeout=30)
        self.ledger.mark_started(second["id"])
        self.ledger.finish(second["id"], "completed")
        raised = BudgetLedger(self.store, limits={"cli_sessions": 500, "production_concurrency": 2}, clock=lambda: self.now[0])
        self.assertEqual(raised.limits["cli_sessions"], 2)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("p3", "G1", timeout=30)
        self.assertEqual(caught.exception.code, "budget_exhausted")

    def test_business_repairs_are_idempotent_and_cumulative_across_new_jobs(self):
        self.assertTrue(self.ledger.record_repair("product-a", "job-repair-1") ["recorded"])
        replay = self.ledger.record_repair("product-a", "job-repair-1")
        self.assertFalse(replay["recorded"])
        self.assertEqual(replay["repairs_used"], 1)
        self.ledger.record_repair("product-a", "job-repair-2")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.record_repair("product-a", "job-repair-3")
        self.assertEqual(caught.exception.code, "budget_repair_limit")
        self.assertEqual(self.ledger.record_repair("product-b", "job-repair-1")["repairs_used"], 1)

    def test_repeating_legitimate_stage_calls_does_not_infer_transient_retries(self):
        # Nine independent authoring file calls are fresh operations, regardless
        # of sharing the blueprint-code retry scope.
        for index in range(9):
            self.assertIsNone(_budget_next_retry(0, 2, scope_retries=min(index, 2)))
            reservation = self.ledger.reserve("product-a", "G1", "production", 30,
                                              stage=f"blueprint-code-0-{index}",
                                              retry_scope="blueprint-code", job_id=f"job-file-{index}")
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "completed")
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 9)
        self.assertEqual(_budget_next_retry(0, 2, forced_transient=True, scope_retries=0), 1)
        self.assertEqual(_budget_next_retry(0, 2, forced_transient=True, scope_retries=1), 2)
        with self.assertRaises(FactoryError) as caught:
            _budget_next_retry(0, 2, forced_transient=True, scope_retries=2)
        self.assertEqual(caught.exception.code, "budget_retry_limit")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-a", "G1", "transient_retry", 30,
                                stage="blueprint-code-0", retry=3, job_id="job-retry-3")
        self.assertEqual(caught.exception.code, "budget_retry_invalid")

    def test_recovery_frees_concurrency_only_after_host_proves_owned_process_stopped(self):
        reservation = self.ledger.reserve("product-a", "G1", timeout=30, job_id="job-uncertain")
        self.ledger.mark_started(reservation["id"])
        self.ledger.finish(reservation["id"], "uncertain")
        with self.assertRaises(FactoryError) as caught:
            self.ledger.mark_recovered_unknowns(["job-uncertain"])
        self.assertEqual(caught.exception.code, "budget_recovery_unproved")
        self.assertEqual(self.ledger.mark_recovered_unknowns(["job-uncertain"], proof_owned_processes_stopped=True), 1)
        snapshot = self.ledger.snapshot()
        self.assertEqual(snapshot["active"], 0)
        self.assertEqual(snapshot["cli_sessions_used"], 1)

    def test_cli_requires_budget_when_marked_v1_and_observed_model_requires_event(self):
        work = self.root / "stage"
        work.mkdir()
        exe = self.root / "fake-opencode"
        exe.write_text(
            "#!/usr/bin/env python3\nimport sys,json\n"
            "if '--version' in sys.argv: print('v1.2.3'); raise SystemExit(0)\n"
            "print(json.dumps({'type':'text','part':{'text':'{\\\"ok\\\":true}'}}))\n"
        )
        exe.chmod(0o700)
        cli = CLI(str(exe))
        with self.assertRaises(FactoryError) as caught:
            cli.run(work, "fake", "vendor/requested", 30, lambda: False, lambda _: None,
                    budget_required=True)
        self.assertEqual(caught.exception.code, "budget_required")
        result = cli.run(work, "fake", "vendor/requested", 30, lambda: False, lambda _: None,
                         budget={"ledger": self.ledger, "identity": "p", "phase": "G1",
                                 "stage": "generate-0", "job_id": "j1", "kind": "production"})
        self.assertEqual(result, {"ok": True})
        summary = json.loads((work / "cli-summary.json").read_text())
        self.assertEqual(summary["requested_model"], "vendor/requested")
        self.assertIsNone(summary["actual_model"])
        self.assertIsNone(summary["actual_reasoning_effort"])

    def test_cli_records_only_model_and_effort_explicitly_observed_in_execution_event(self):
        work = self.root / "stage-event"
        work.mkdir()
        exe = self.root / "fake-event"
        exe.write_text(
            "#!/usr/bin/env python3\nimport sys,json\n"
            "if '--version' in sys.argv: print('v2.0.0'); raise SystemExit(0)\n"
            "print(json.dumps({'type':'step_finish','model':'provider/model-real',"
            "'reasoning_effort':'high','part':{}}))\n"
            "print(json.dumps({'type':'text','part':{'text':'{\\\"ok\\\":true}'}}))\n"
        )
        exe.chmod(0o700)
        CLI(str(exe)).run(work, "fake", "provider/deepseek-model-requested", 30,
                          lambda: False, lambda _: None,
                          reasoning_effort="low",
                          budget={"ledger": self.ledger, "identity": "p2", "phase": "G1",
                                  "stage": "review", "job_id": "j2", "kind": "review"})
        summary = json.loads((work / "cli-summary.json").read_text())
        self.assertEqual(summary["actual_model"], "provider/model-real")
        self.assertEqual(summary["actual_reasoning_effort"], "high")
        with self.store.connect() as con:
            row = con.execute("SELECT observed_model,observed_effort FROM tf_budget_reservation WHERE identity='p2'").fetchone()
        self.assertEqual(tuple(row), ("provider/model-real", "high"))


if __name__ == "__main__":
    unittest.main()
