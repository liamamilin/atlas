import json
from pathlib import Path
import tempfile
import threading
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import BudgetLedger
from template_factory.cli import CLI
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
        for job in ("job-file-1", "job-file-2", "job-file-3"):
            reservation = self.ledger.reserve("product-a", "G1", "production", 30,
                                              stage="blueprint-code-0", job_id=job)
            self.ledger.mark_started(reservation["id"])
            self.ledger.finish(reservation["id"], "completed")
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 3)
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
