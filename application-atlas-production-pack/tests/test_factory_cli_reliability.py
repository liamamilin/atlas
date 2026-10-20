import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.cli import CLI
from template_factory.store import FactoryError


class FactoryCLIReliabilityTests(unittest.TestCase):
    def test_evidence_grant_stays_occupied_when_spawn_or_start_record_is_uncertain(self):
        for failure_mode in ("popen_interrupt", "start_record_failure"):
            with self.subTest(failure_mode=failure_mode), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, 'import time\ntime.sleep(20)\n')
                events, processes = [], []

                class Ledger:
                    def reserve(self, *args, **kwargs):
                        return {"id": "evidence-reservation", "timeout": 3,
                                "evidence_recovery_id": "egrant-fixture"}

                    def mark_spawn_intent(self, reservation_id, *, directory=None):
                        events.append("spawn_intent")

                    def mark_started(self, reservation_id):
                        events.append("mark_started")
                        if failure_mode == "start_record_failure":
                            raise FactoryError("start write failed", "fixture_start_failed", 409)

                    def finish(self, reservation_id, status, **kwargs):
                        events.append(("finish", status))

                    def release_not_started(self, reservation_id):
                        events.append("release")

                original = subprocess.Popen

                def spawn(*args, **kwargs):
                    child = original(*args, **kwargs)
                    # Setup probes may also use Popen. The model process is
                    # the explicit `opencode run` command.
                    argv = args[0] if args else kwargs.get("args", [])
                    if len(argv) > 1 and argv[1] == "run":
                        processes.append(child)
                        if failure_mode == "popen_interrupt":
                            raise KeyboardInterrupt()
                    return child

                with patch("template_factory.cli._detect_major", return_value=2), \
                     patch("template_factory.cli.subprocess.Popen", side_effect=spawn), \
                     patch("template_factory.evidence_views.readonly_cli_config_identity",
                           return_value={"schema": "fixture"}):
                    with self.assertRaises(KeyboardInterrupt if failure_mode == "popen_interrupt" else FactoryError) as caught:
                        self.run_cli(
                            exe, work,
                            budget={"ledger": Ledger(), "identity": "p", "phase": "G1",
                                    "evidence_recovery_id": "egrant-fixture"},
                        )
                self.assertIn("spawn_intent", events)
                self.assertNotIn("release", events)
                self.assertIn(("finish", "uncertain"), events)
                summary = self.summary(work)
                if failure_mode == "popen_interrupt":
                    self.assertEqual(summary["cli_status"], "uncertain")
                    self.assertIsNone(summary["stdout_sha256"])
                    self.assertIsNone(summary["stderr_sha256"])
                    self.assertFalse(summary["output_observed"])
                self.assertTrue(processes)
                for child in processes:
                    if child.poll() is None:
                        child.kill()
                    child.wait(timeout=3)

    def test_budget_rejection_never_announces_or_spawns_cli(self):
        class DeniedLedger:
            def reserve(self, *args, **kwargs):
                raise FactoryError("retry exhausted", "budget_retry_limit", 409)

        with tempfile.TemporaryDirectory() as root:
            exe, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
            events = []
            with patch("template_factory.cli.subprocess.Popen") as spawn:
                with self.assertRaises(FactoryError) as caught:
                    self.run_cli(exe, work, progress=events.append,
                                 budget={"ledger": DeniedLedger(), "identity": "p", "phase": "G1"})
                spawn.assert_not_called()
            self.assertEqual(caught.exception.code, "budget_retry_limit")
            self.assertNotIn("OpenCode CLI started", events)
            self.assertFalse((work / "process.json").exists())

    def test_started_event_follows_spawn_and_ledger_start_and_failure_cleans_process(self):
        for deny_start in (False, True):
            with self.subTest(deny_start=deny_start), tempfile.TemporaryDirectory() as root:
                events, processes = [], []

                class Ledger:
                    def reserve(self, *args, **kwargs):
                        return {"id": "fixture-reservation", "timeout": 3}

                    def mark_started(self, reservation_id):
                        events.append("mark_started")
                        if deny_start:
                            raise FactoryError("start ledger failed", "fixture_start_failed", 409)

                    def finish(self, *args, **kwargs):
                        events.append("finish")

                exe, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
                real_spawn = subprocess.Popen

                def spawn(argv, **kwargs):
                    process = real_spawn(argv, **kwargs)
                    if "run" in argv:
                        processes.append(process)
                        events.append("spawn")
                    return process

                with patch("template_factory.cli.subprocess.Popen", side_effect=spawn):
                    if deny_start:
                        with self.assertRaises(FactoryError) as caught:
                            self.run_cli(exe, work, progress=events.append,
                                         budget={"ledger": Ledger(), "identity": "p", "phase": "G1"})
                        self.assertEqual(caught.exception.code, "fixture_start_failed")
                        self.assertNotIn("OpenCode CLI started", events)
                    else:
                        self.assertEqual(self.run_cli(exe, work, progress=events.append,
                                                     budget={"ledger": Ledger(), "identity": "p", "phase": "G1"}), {"ok": True})
                        self.assertLess(events.index("spawn"), events.index("mark_started"))
                        self.assertLess(events.index("mark_started"), events.index("OpenCode CLI started"))
                self.assertEqual(len(processes), 1)
                self.assertIsNotNone(processes[0].poll())

    def test_archived_inner_incomplete_review_is_not_repaired(self):
        from template_factory.cli import recover_cognitive_framing

        source = Path(__file__).resolve().parents[2] / "docs/template-factory/g1-r5-2026-10-19/phase-acceptance-incomplete-raw.txt"
        with self.assertRaises(FactoryError) as caught:
            recover_cognitive_framing(source.read_text())
        self.assertEqual(caught.exception.code, "cli_protocol")

    def fake(self, root, body):
        executable = Path(root) / "fake-opencode"
        executable.write_text(
            "#!/usr/bin/env python3\nimport sys,time,json\n"
            "if '--version' in sys.argv: print('1.2.3'); raise SystemExit(0)\n"
            + body
        )
        executable.chmod(0o700)
        work = Path(root) / "stage"
        work.mkdir()
        return executable, work

    def run_cli(self, executable, work, **kwargs):
        args = dict(directory=work, prompt="fake", model="fake/model", timeout=3,
                    cancelled=lambda: False, progress=lambda _: None)
        args.update(kwargs)
        return CLI(str(executable)).run(**args)

    def summary(self, work):
        return json.loads((work / "cli-summary.json").read_text())

    def test_cli_processes_do_not_inherit_stdin(self):
        import subprocess

        original = subprocess.Popen
        seen = []
        def recording(*args, **kwargs):
            seen.append(kwargs.get("stdin"))
            return original(*args, **kwargs)
        with tempfile.TemporaryDirectory() as root:
            exe, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
            with patch("template_factory.cli.subprocess.Popen", side_effect=recording), \
                 patch("template_factory.cli.subprocess.run", wraps=subprocess.run) as run:
                self.run_cli(exe, work)
                self.assertTrue(all(c.kwargs.get("stdin") == subprocess.DEVNULL for c in run.call_args_list))
            self.assertGreaterEqual(len(seen), 1)
            self.assertTrue(all(value == subprocess.DEVNULL for value in seen))

    def test_info_probes_are_stdin_isolated_and_summary_redacts_session_ids(self):
        import subprocess

        with tempfile.TemporaryDirectory() as root:
            exe, work = self.fake(
                root,
                'print(json.dumps({"type":"text","sessionID":"sk-abcdefghijk",'
                '"part":{"text":"{\\"ok\\":true}"}}))\n',
            )
            original = subprocess.run
            with patch("template_factory.cli.subprocess.run", wraps=original) as run:
                CLI(str(exe)).info(models=True)
                self.run_cli(exe, work)
            self.assertGreaterEqual(len(run.call_args_list), 3)
            self.assertTrue(all(call.kwargs.get("stdin") == subprocess.DEVNULL for call in run.call_args_list))
            self.assertEqual(self.summary(work)["session_id"], "[REDACTED]")

    def test_nonzero_and_provider_error_write_failure_summary(self):
        for body, code in (
            ('print("broken"); raise SystemExit(7)\n', "cli_failed"),
            ('print(json.dumps({"type":"error","sessionID":"s-1","error":"provider down"}))\n', "cli_failed"),
        ):
            with self.subTest(code=code), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, body)
                with self.assertRaises(FactoryError) as caught:
                    self.run_cli(exe, work)
                self.assertEqual(caught.exception.code, code)
                summary = self.summary(work)
                self.assertEqual(summary["delivery_status"], "failed")
                self.assertEqual(summary["failure_code"], code)
                self.assertEqual(summary["cli_status"], "completed")
                self.assertIsNotNone(summary["exit_code"])
                self.assertEqual(summary["session_id"], "s-1" if "sessionID" in body else None)

    def test_protocol_failure_and_tail_length_event_are_summarized(self):
        for body, expected in (
            ('print("not-json")\n', "cli_protocol"),
            ('print(json.dumps({"type":"step_finish","sessionId":"tail","part":{"reason":"length"}}),end="")\n', "cli_output_truncated"),
        ):
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, body)
                work.rename(Path(root) / "blueprint-code-0-0")
                work = Path(root) / "blueprint-code-0-0"
                with self.assertRaises(FactoryError) as caught:
                    self.run_cli(exe, work)
                self.assertEqual(caught.exception.code, expected)
                self.assertEqual(self.summary(work)["failure_code"], expected)
                if expected.endswith("truncated"):
                    self.assertEqual(self.summary(work)["session_id"], "tail")

    def test_cancel_and_timeout_terminate_process_and_record_null_exit_if_unstarted(self):
        for mode in ("cancel", "timeout"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, "time.sleep(30)\n")
                options = {"cancelled": lambda: mode == "cancel", "timeout": 0.15 if mode == "timeout" else 3}
                with self.assertRaises(FactoryError) as caught:
                    self.run_cli(exe, work, **options)
                self.assertEqual(caught.exception.code, "cancelled" if mode == "cancel" else "cli_timeout")
                summary = self.summary(work)
                self.assertEqual(summary["failure_code"], caught.exception.code)
                self.assertEqual(summary["delivery_status"], "failed")
                self.assertIsNotNone(summary["exit_code"])
                self.assertIsNone(json.loads((work / "process.json").read_text())["pid"])

    def test_prestart_and_postspawn_setup_failures_write_summary_and_clean_process(self):
        with tempfile.TemporaryDirectory() as root:
            exe, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
            cli = CLI(str(exe))
            cli.executable = None
            with self.assertRaises(FactoryError):
                cli.run(work, "fake", "fake/model", 3, lambda: False, lambda _: None)
            summary = self.summary(work)
            self.assertEqual(summary["failure_code"], "cli_unavailable")
            self.assertIsNone(summary["exit_code"])
            self.assertEqual(summary["cli_status"], "not_started")

        for failed_part in ("selector", "process_marker"):
            with self.subTest(failed_part=failed_part), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
                if failed_part == "selector":
                    class BrokenSelector:
                        def register(self, *_args):
                            raise OSError("registration failed")
                        def close(self):
                            pass
                    patcher = patch("template_factory.cli.selectors.DefaultSelector", return_value=BrokenSelector())
                else:
                    from atlas_runtime import atomic_json as real_atomic_json
                    def fail_marker(path, value):
                        if Path(path).name == "process.json" and value.get("pid"):
                            raise OSError("marker write failed")
                        return real_atomic_json(path, value)
                    patcher = patch("template_factory.cli.atomic_json", side_effect=fail_marker)
                with patcher, self.assertRaises(OSError):
                    self.run_cli(exe, work)
                self.assertEqual(self.summary(work)["delivery_status"], "failed")
                self.assertIsNone(json.loads((work / "process.json").read_text())["pid"])

    def test_unsupported_model_option_has_prestart_summary(self):
        with tempfile.TemporaryDirectory() as root:
            exe, work = self.fake(root, 'print("unused")\n')
            with patch("template_factory.cli._detect_major", return_value=2):
                with self.assertRaises(FactoryError) as caught:
                    self.run_cli(exe, work, model="fake/deepseek-chat", reasoning_effort="none")
            self.assertEqual(caught.exception.code, "unsupported_model_option")
            self.assertEqual(self.summary(work)["failure_code"], "unsupported_model_option")

    def test_cleanup_failure_blocks_success_and_does_not_replace_primary_failure(self):
        for body, expected in (
            ('print(json.dumps({"ok": True}))\n', "cli_cleanup_failed"),
            ('print(json.dumps({"type":"error","error":"provider failed"}))\n', "cli_failed"),
        ):
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as root:
                exe, work = self.fake(root, body)
                original = Path.write_text
                def fail_log(path, content, *args, **kwargs):
                    if path.name == "stdout.log":
                        raise OSError("log persistence failed")
                    return original(path, content, *args, **kwargs)
                with patch.object(Path, "write_text", fail_log):
                    with self.assertRaises(FactoryError) as caught:
                        self.run_cli(exe, work)
                self.assertEqual(caught.exception.code, expected)
                self.assertEqual(self.summary(work)["failure_code"], expected)

    def test_timeout_kills_process_group_after_cli_leader_exits(self):
        with tempfile.TemporaryDirectory() as root:
            body = (
                "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'], "
                "stdout=sys.stdout, stderr=sys.stderr)\n"
                "open('child.pid','w').write(str(child.pid))\n"
            )
            exe = Path(root) / "fake-opencode"
            exe.write_text("#!/usr/bin/env python3\nimport sys,time,json,subprocess,os\n"
                           "if '--version' in sys.argv: print('1.2.3'); raise SystemExit(0)\n" + body)
            exe.chmod(0o700)
            work = Path(root) / "stage"
            work.mkdir()
            with self.assertRaises(FactoryError) as caught:
                self.run_cli(exe, work, timeout=0.4)
            self.assertEqual(caught.exception.code, "cli_timeout")
            child_pid = int((work / "child.pid").read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)

    def test_sigterm_ignoring_descendant_is_killed_after_leader_exits(self):
        with tempfile.TemporaryDirectory() as root:
            child_code = "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
            body = (
                "child = subprocess.Popen([sys.executable, '-c', " + repr(child_code) + "], "
                "stdout=sys.stdout, stderr=sys.stderr)\n"
                "open('child.pid','w').write(str(child.pid))\n"
            )
            exe = Path(root) / "fake-opencode"
            exe.write_text("#!/usr/bin/env python3\nimport sys,time,json,subprocess,os\n"
                           "if '--version' in sys.argv: print('1.2.3'); raise SystemExit(0)\n" + body)
            exe.chmod(0o700)
            work = Path(root) / "stage"
            work.mkdir()
            with self.assertRaises(FactoryError) as caught:
                self.run_cli(exe, work, timeout=0.35)
            self.assertEqual(caught.exception.code, "cli_timeout")
            child_pid = int((work / "child.pid").read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)
            self.assertEqual(self.summary(work)["delivery_status"], "failed")

    def test_successful_cli_cannot_leave_pipe_closed_sigterm_ignoring_descendant(self):
        with tempfile.TemporaryDirectory() as root:
            child_code = "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
            body = (
                "child = subprocess.Popen([sys.executable, '-c', " + repr(child_code) + "], "
                "stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)\n"
                "open('child.pid','w').write(str(child.pid))\n"
                "print(json.dumps({'ok': True}), flush=True)\n"
            )
            exe = Path(root) / "fake-opencode"
            exe.write_text("#!/usr/bin/env python3\nimport sys,time,json,subprocess,os\n"
                           "if '--version' in sys.argv: print('1.2.3'); raise SystemExit(0)\n" + body)
            exe.chmod(0o700)
            work = Path(root) / "stage"
            work.mkdir()
            result = self.run_cli(exe, work)
            self.assertEqual(result, {"ok": True})
            child_pid = int((work / "child.pid").read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(child_pid, 0)
            self.assertEqual(self.summary(work)["delivery_status"], "delivered")


if __name__ == "__main__":
    unittest.main()
