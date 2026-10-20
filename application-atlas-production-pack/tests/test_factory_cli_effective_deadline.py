"""Fake-process checks for the absolute deadline; no provider is contacted."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_factory_cli_reliability as reliability
from template_factory.cli import CLI
from template_factory.store import FactoryError


class EffectiveDeadlineTests(unittest.TestCase):
    def test_delay_before_setup_or_spawn_never_starts_provider(self):
        for delay_at in ("dispatch", "configuration"):
            with self.subTest(delay_at=delay_at), tempfile.TemporaryDirectory() as root:
                fixture = reliability.FactoryCLIReliabilityTests()
                exe, work = fixture.fake(root, 'print(json.dumps({"ok":True}))\n')
                epoch, events = [100.0], []

                class Ledger:
                    def clock(self):
                        return epoch[0]

                    def reserve(self, *args, **kwargs):
                        return {"id": "fixture", "timeout": 5, "deadline": 105}

                    def release_not_started(self, reservation_id):
                        events.append("released_proven_not_started")

                class DelayedCLI(CLI):
                    def _run(self, *args, **kwargs):
                        if delay_at == "dispatch":
                            epoch[0] = 106
                        return super()._run(*args, **kwargs)

                def configure(*args, **kwargs):
                    epoch[0] = 106
                    return 1

                with patch("template_factory.cli._detect_major", side_effect=configure), \
                     patch("template_factory.cli.initialize_project"), \
                     patch("template_factory.cli.subprocess.Popen") as spawn:
                    with self.assertRaises(FactoryError) as caught:
                        DelayedCLI(str(exe)).run(work, "fixture", "fake/model", 5,
                                                lambda: False, lambda _: None,
                                                budget={"ledger": Ledger(), "identity": "p", "phase": "G1"})
                    spawn.assert_not_called()
                self.assertEqual(caught.exception.code, "budget_deadline")
                self.assertEqual(events, ["released_proven_not_started"])

    def test_running_process_stops_at_effective_deadline(self):
        with tempfile.TemporaryDirectory() as root:
            fixture = reliability.FactoryCLIReliabilityTests()
            exe, work = fixture.fake(root, 'time.sleep(10)\n')
            epoch, events = [100.0], []

            class Ledger:
                def clock(self):
                    return epoch[0]

                def reserve(self, *args, **kwargs):
                    return {"id": "fixture", "timeout": 5, "deadline": 105}

                def mark_started(self, reservation_id):
                    events.append("started")

                def finish(self, reservation_id, status, **kwargs):
                    events.append(status)

            def progress(message):
                if message == "OpenCode CLI started":
                    epoch[0] = 106

            with patch("template_factory.cli._detect_major", return_value=1):
                with self.assertRaises(FactoryError) as caught:
                    CLI(str(exe)).run(work, "fixture", "fake/model", 5,
                                      lambda: False, progress,
                                      budget={"ledger": Ledger(), "identity": "p", "phase": "G1"})
            self.assertEqual(caught.exception.code, "budget_deadline")
            self.assertEqual(events.count("started"), 1)
            self.assertIn("failed", events)
            self.assertNotIn("completed", events)
            self.assertEqual(fixture.summary(work)["failure_code"], "budget_deadline")
