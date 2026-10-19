"""Proof-gated orphan cleanup for durable V1 model-call reservations."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.budget import BudgetLedger
from template_factory.store import FactoryError, FactoryStore
from template_factory import worker


class FactoryRecoveryV1Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        self.store = FactoryStore(self.root / "state", self.pack)
        self.ledger = BudgetLedger(
            self.store,
            campaign_id="campaign-v1",
            limits={"cli_sessions": 10, "production_concurrency": 1},
        )

    def tearDown(self):
        self.temp.cleanup()

    def add_running_job(self, job_id="job_orphan", stage="research"):
        with self.store.connect(True) as con:
            con.execute(
                "INSERT INTO job(id,batch_id,kind,state,stage,attempt,token,lease,snapshot,error,created_at,updated_at) "
                "VALUES(?, 'batch_test', 'case-research', 'running', ?, 1, 'old-worker:token', 9999999999, '{}', NULL, 'created', 'updated')",
                (job_id, stage),
            )
        reservation = self.ledger.reserve(
            "product-v1", "research", "research", 30, job_id=job_id
        )
        self.ledger.mark_started(reservation["id"])
        self.ledger.finish(reservation["id"], "uncertain", outcome="worker_interrupted")
        directory = self.root / "state" / "jobs" / job_id / "attempt-1" / stage
        directory.mkdir(parents=True)
        return directory

    def run_recovery(self, process_rows, kill):
        with (
            patch("template_factory.cli.CLI") as cli,
            patch.object(worker, "_process_table", side_effect=lambda: list(process_rows)),
            patch.object(worker.os, "killpg", side_effect=kill),
            patch.object(worker.shutil, "which", return_value=None),
        ):
            cli.return_value.executable = "/opt/opencode"
            worker.stop_orphans(self.store)

    def test_proven_stop_frees_concurrency_but_keeps_call_charged(self):
        directory = self.add_running_job()
        pid = 41231
        command = f"/opt/opencode run Task workspace: {directory.resolve()}."
        members = [{"pgid": pid, "pid": pid, "state": "S", "command": command}]
        signals = []

        def send(group, sig):
            self.assertEqual(group, pid)
            signals.append(sig)
            members.clear()  # the host probe sees the whole group exit

        (directory / "process.json").write_text(json.dumps({"pid": pid, "started": 1}))
        before = self.ledger.snapshot()
        self.assertEqual(before["active"], 1)
        self.assertEqual(before["cli_sessions_used"], 1)

        self.run_recovery(members, send)

        after = self.ledger.snapshot()
        self.assertEqual(signals, [worker.signal.SIGTERM])
        self.assertEqual(after["active"], 0)
        self.assertEqual(after["cli_sessions_used"], 1)
        with self.store.connect() as con:
            row = con.execute(
                "SELECT status,outcome FROM tf_budget_reservation WHERE job_id='job_orphan'"
            ).fetchone()
        self.assertEqual(row["status"], "failed")
        self.assertEqual(row["outcome"], "recovered_after_owned_processes_stopped")

        replacement = self.ledger.reserve(
            "product-next", "research", "research", 30, job_id="job_next"
        )
        self.assertTrue(replacement["id"].startswith("bud_"))
        self.assertEqual(self.ledger.snapshot()["active"], 1)
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 2)

    def test_mismatched_pid_marker_does_not_kill_or_release_unknown_reservation(self):
        directory = self.add_running_job()
        pid = 42345
        (directory / "process.json").write_text(json.dumps({"pid": pid, "started": 1}))
        unrelated = [
            # The record PID exists, but it is not the new-session group ID.
            {"pgid": pid - 1, "pid": pid, "state": "S",
             "command": f"/opt/opencode run Task workspace: {directory.resolve()} ."},
            # A matching PID/PGID with a different task marker is also not ours.
            {"pgid": pid + 1, "pid": pid + 1, "state": "S",
             "command": "/opt/opencode run Task workspace: /other/task."},
        ]
        signals = []

        self.run_recovery(unrelated, lambda group, sig: signals.append((group, sig)))

        self.assertEqual(signals, [])
        snapshot = self.ledger.snapshot()
        self.assertEqual(snapshot["active"], 1)
        self.assertEqual(snapshot["cli_sessions_used"], 1)
        with self.assertRaises(FactoryError) as caught:
            self.ledger.reserve("product-next", "research", "research", 30, job_id="job_next")
        self.assertEqual(caught.exception.code, "budget_concurrency")

    def test_unproved_termination_keeps_reservation_active(self):
        directory = self.add_running_job()
        pid = 43456
        command = f"/opt/opencode run Task workspace: {directory.resolve()}."
        members = [{"pgid": pid, "pid": pid, "state": "S", "command": command}]
        (directory / "process.json").write_text(json.dumps({"pid": pid, "started": 1}))

        def denied(group, sig):
            raise PermissionError("signal denied")

        self.run_recovery(members, denied)

        snapshot = self.ledger.snapshot()
        self.assertEqual(snapshot["active"], 1)
        self.assertEqual(snapshot["cli_sessions_used"], 1)
        with self.store.connect() as con:
            row = con.execute(
                "SELECT status FROM tf_budget_reservation WHERE job_id='job_orphan'"
            ).fetchone()
        self.assertEqual(row["status"], "uncertain")

    def test_sigkill_escalation_requires_final_empty_process_group_probe(self):
        directory = self.root / "task"
        directory.mkdir()
        pid = 44567
        members = [{
            "pgid": pid,
            "pid": pid,
            "state": "S",
            "command": f"/opt/opencode run Task workspace: {directory.resolve()}.",
        }]
        signals = []
        clock = [0.0]

        def monotonic():
            clock[0] += 0.5
            return clock[0]

        def send(group, sig):
            self.assertEqual(group, pid)
            signals.append(sig)
            if sig == worker.signal.SIGKILL:
                members.clear()

        stopped = worker._stop_owned_process_group(
            pid,
            directory,
            "/opt/opencode",
            process_table=lambda: list(members),
            killpg=send,
            sleep=lambda _seconds: None,
            monotonic=monotonic,
        )

        self.assertTrue(stopped)
        self.assertEqual(signals, [worker.signal.SIGTERM, worker.signal.SIGKILL])


if __name__ == "__main__":
    unittest.main()
