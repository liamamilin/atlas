"""Provider usage evidence is retained per CLI step without inferred totals."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.cli import CLI


class FactoryCLIUsageTests(unittest.TestCase):
    def test_step_usage_is_preserved_and_missing_fields_stay_null(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            executable = root_path / "fake-opencode"
            work = root_path / "stage"
            work.mkdir()
            first_usage = {
                "cost": 0.0125,
                "tokens": {
                    "input": 120,
                    "output": 23,
                    "reasoning": 7,
                    "cache": {"read": 80, "write": 11},
                },
            }
            script = (
                "#!/usr/bin/env python3\nimport json,sys\n"
                "if '--version' in sys.argv: print('v2.1.0'); raise SystemExit(0)\n"
                f"print(json.dumps({json.dumps({'type': 'step_finish', 'id': 'evt_1', 'sessionID': 'ses_1', 'messageID': 'msg_1', 'part': {'id': 'part_1', **first_usage}})}))\n"
                "print(json.dumps({'type':'step_finish','sessionId':'ses_1','messageId':'msg_2','part':{'id':'part_2','reason':'stop'}}))\n"
                "print(json.dumps({'type':'text','part':{'text':'{\"ok\":true}'}}))\n"
            )
            executable.write_text(script)
            executable.chmod(0o700)

            result = CLI(str(executable)).run(
                work,
                "fixture",
                "vendor/model",
                30,
                lambda: False,
                lambda _message: None,
            )

            self.assertEqual(result, {"ok": True})
            summary = json.loads((work / "cli-summary.json").read_text())
            self.assertEqual(summary["usage_event_limit"], 1000)
            self.assertFalse(summary["usage_events_truncated"])
            self.assertEqual(len(summary["usage_events"]), 2)
            first, second = summary["usage_events"]
            self.assertEqual(
                (first["event_type"], first["event_id"], first["session_id"], first["message_id"], first["part_id"]),
                ("step_finish", "evt_1", "ses_1", "msg_1", "part_1"),
            )
            self.assertEqual(first["cost"], 0.0125)
            self.assertIsNone(first["cost_currency"])
            self.assertEqual(first["tokens"], first_usage["tokens"])
            self.assertEqual(first["reported_usage"], first_usage)
            self.assertIsNone(second["cost"])
            self.assertIsNone(second["cost_currency"])
            self.assertEqual(
                second["tokens"],
                {"input": None, "output": None, "reasoning": None, "cache": {"read": None, "write": None}},
            )
            self.assertEqual(second["reported_usage"], {})
            self.assertNotIn("total_tokens", summary)
            self.assertNotIn("total_cost", summary)

    def test_usage_events_are_bounded_and_truncation_is_explicit(self):
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            executable = root_path / "fake-opencode"
            work = root_path / "stage"
            work.mkdir()
            executable.write_text(
                "#!/usr/bin/env python3\nimport json,sys\n"
                "if '--version' in sys.argv: print('v2.1.0'); raise SystemExit(0)\n"
                "for i in range(1001): print(json.dumps({'type':'step_finish','messageID':str(i),'part':{'tokens':{'input':i}}}))\n"
                "print(json.dumps({'type':'text','part':{'text':'{\"ok\":true}'}}))\n"
            )
            executable.chmod(0o700)

            CLI(str(executable)).run(
                work,
                "fixture",
                "vendor/model",
                30,
                lambda: False,
                lambda _message: None,
            )

            summary = json.loads((work / "cli-summary.json").read_text())
            self.assertEqual(len(summary["usage_events"]), 1000)
            self.assertEqual(summary["usage_event_limit"], 1000)
            self.assertTrue(summary["usage_events_truncated"])


if __name__ == "__main__":
    unittest.main()
