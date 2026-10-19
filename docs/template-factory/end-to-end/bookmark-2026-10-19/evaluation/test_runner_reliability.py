"""Synthetic reliability checks; mocks every Docker call and never starts a container."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import sys
from unittest.mock import patch
from types import SimpleNamespace

RUNNER = Path(__file__).with_name("docker_ui_acceptance.py")
spec = importlib.util.spec_from_file_location("bookmark_acceptance_runner", RUNNER)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
sys.path.insert(0, str(RUNNER.parent))
import posthoc_http_probes as posthoc


class RunnerReliabilityTests(unittest.TestCase):
    def test_docker_timeout_is_bounded_and_classified_as_environment(self):
        with patch.object(runner.subprocess, "run", side_effect=subprocess.TimeoutExpired(["docker", "info"], 10)) as mocked:
            with self.assertRaises(runner.DockerCommandTimeout) as caught:
                runner.docker("info", timeout=10)
        self.assertEqual(mocked.call_args.kwargs["timeout"], 10)
        self.assertEqual(runner.classify_failure("docker_daemon_preflight", caught.exception),
                         ("blocked", "environment_docker_cli_timeout"))

    def test_cleanup_continues_and_persists_when_a_cleanup_step_fails(self):
        with tempfile.TemporaryDirectory(prefix="runner-reliability-synthetic-") as temp:
            evidence = Path(temp) / "run.json"
            report = {"status": "blocked", "stage": "local_image_preflight", "owned_resources": {
                "container": {"state": "creation-attempted"}, "network": {"state": "creation-attempted"},
                "temporary_root": {"state": "created"}, "fixture_server": {"state": "planned"},
                "fixture_thread": {"state": "planned"},
            }}
            calls = []

            def persist():
                runner.atomic_write_json(evidence, report)

            def fake_docker(*args, check=True, timeout=None):
                calls.append((args, timeout))
                if args[:2] == ("rm", "--force"):
                    raise runner.DockerCommandTimeout(args, timeout)
                return SimpleNamespace(returncode=0, stdout="ok", stderr="")

            cleanup = runner.cleanup_resources(
                report, persist,
                container="synthetic-container", network="synthetic-network",
                temp_root=Path(temp) / "nonexistent-temp-root",
                container_attempted=True, network_attempted=True,
                fixture=None, fixture_thread=None, docker_call=fake_docker,
                temp_remover=lambda _root: True,
            )
            saved = json.loads(evidence.read_text())
            self.assertFalse(cleanup["container_remove"]["ok"])
            self.assertFalse(cleanup["all_resources_removed"])
            self.assertEqual([args[0] for args, _ in calls], [
                "rm", "inspect", "network", "network",
            ])
            self.assertTrue(all(timeout == 10 for _, timeout in calls))
            self.assertIn("temporary_state_removed", cleanup)
            self.assertEqual(saved["cleanup"]["events"][-1]["state"], "completed")
            self.assertFalse(saved["cleanup"]["all_resources_removed"])

    def test_initial_journal_precedes_owned_resource_creation(self):
        source = RUNNER.read_text()
        self.assertLess(source.index("persist()\n    try:"), source.index("temp_root.mkdir(mode=0o700)"))
        self.assertLess(source.index("persist()\n    try:"), source.index("ThreadingHTTPServer((\"127.0.0.1\", fixture_port), Fixture)"))

    def test_cleanup_interrupt_is_preserved_and_later_steps_continue(self):
        with tempfile.TemporaryDirectory(prefix="runner-interruption-synthetic-") as temp:
            root = Path(temp)
            evidence = root / "run.json"
            primary = {"stage": "ui_initial", "status": "failed", "failure_kind": "product_or_acceptance_failure",
                       "error": "original acceptance failure"}
            report = {"status": "failed", "failure_kind": primary["failure_kind"],
                      "error": primary["error"], "primary_failure": primary,
                      "evidence_dir": str(root), "owned_resources": {
                "container": {"state": "planned"}, "network": {"state": "planned"},
                "temporary_root": {"state": "created"}, "fixture_server": {"state": "planned"},
                "fixture_thread": {"state": "planned"},
            }}

            def persist():
                runner.atomic_write_json(evidence, report)

            def interrupted_cleanup(*args, **_kwargs):
                if args[:2] == ("rm", "--force"):
                    raise KeyboardInterrupt()
                return SimpleNamespace(returncode=0, stdout="ok", stderr="")

            cleanup = runner.cleanup_resources(
                report, persist,
                container="synthetic-container", network="synthetic-network",
                temp_root=root / "nonexistent-temp-root",
                container_attempted=True, network_attempted=False,
                fixture=None, fixture_thread=None,
                docker_call=interrupted_cleanup, temp_remover=lambda _root: True,
            )
            marker = json.loads((root / "interruption.json").read_text())
            saved = json.loads(evidence.read_text())
            self.assertEqual(marker["stage"], "cleanup:container_remove")
            self.assertEqual(saved["status"], "failed")
            self.assertEqual(saved["error"], "original acceptance failure")
            self.assertEqual(saved["primary_failure"], primary)
            self.assertTrue(saved["cleanup_interruptions"])
            self.assertTrue(cleanup["temporary_state_removed"])
            self.assertEqual(cleanup["events"][-1]["state"], "completed")

    def test_persist_interrupt_does_not_skip_later_cleanup(self):
        with tempfile.TemporaryDirectory(prefix="runner-journal-interruption-synthetic-") as temp:
            root = Path(temp)
            evidence = root / "run.json"
            report = {"status": "blocked", "failure_kind": "environment_docker_cli_timeout",
                      "error": "original environment failure", "evidence_dir": str(root),
                      "owned_resources": {
                "container": {"state": "creation-attempted"}, "network": {"state": "planned"},
                "temporary_root": {"state": "created"}, "fixture_server": {"state": "planned"},
                "fixture_thread": {"state": "planned"},
            }}
            persist_calls = 0

            def persist():
                nonlocal persist_calls
                persist_calls += 1
                if persist_calls == 1:
                    raise KeyboardInterrupt()
                runner.atomic_write_json(evidence, report)

            def fake_docker(*_args, **_kwargs):
                return SimpleNamespace(returncode=1, stdout="[]", stderr="No such object")

            cleanup = runner.cleanup_resources(
                report, persist,
                container="synthetic-container", network="synthetic-network",
                temp_root=root / "nonexistent-temp-root",
                container_attempted=True, network_attempted=False,
                fixture=None, fixture_thread=None, docker_call=fake_docker,
                temp_remover=lambda _root: True,
            )
            saved = json.loads(evidence.read_text())
            marker = json.loads((root / "interruption.json").read_text())
            self.assertEqual(marker["status"], "interrupted_during_cleanup")
            self.assertEqual(saved["status"], "blocked")
            self.assertEqual(saved["error"], "original environment failure")
            self.assertTrue(cleanup["temporary_state_removed"])
            self.assertEqual(cleanup["events"][-1]["state"], "completed")

    def test_posthoc_html_inventory_parser_handles_nested_li_and_controls(self):
        doc = posthoc.BookmarkHTML()
        doc.feed('<ul><li class="collection" data-collection-id="2"><a>Concurrent run 01</a><button>移除</button>'
                 '<ul><li class="bookmark" data-bookmark-id="7"><a href="/go/7">Saved link</a></li></ul></li></ul>')
        self.assertEqual(len(doc.collections), 1)
        self.assertIn("Concurrent run 01", doc.collections[0]["text"])
        self.assertEqual(len(doc.bookmarks), 1)
        self.assertEqual(doc.bookmarks[0]["attrs"]["data-bookmark-id"], "7")

    def test_final_cleanup_error_cannot_leave_passed_verdict(self):
        for exception, expected_status, expected_exit in (
            (OSError("synthetic disk error"), "failed", 1),
            (KeyboardInterrupt(), "interrupted", 130),
        ):
            with self.subTest(exception=type(exception).__name__), tempfile.TemporaryDirectory(
                    prefix="runner-finalize-synthetic-") as temp:
                root = Path(temp)
                report = {"status": "passed", "cleanup": {"all_resources_removed": True}}
                calls = 0

                def persist():
                    nonlocal calls
                    calls += 1
                    if calls == 1:
                        raise exception
                    runner.atomic_write_json(root / "run.json", report)

                final_status = runner.finalize_cleanup_outcome(report, persist, root)
                saved = json.loads((root / "run.json").read_text())
                self.assertEqual(final_status, expected_status)
                self.assertEqual(saved["status"], expected_status)
                self.assertEqual(expected_exit, 130 if saved["status"] == "interrupted" else 1)
                self.assertTrue(saved["cleanup_failure"])
                self.assertTrue(saved["cleanup"]["all_resources_removed"])
                self.assertNotEqual(saved["status"], "passed")
                if expected_status == "interrupted":
                    self.assertEqual(json.loads((root / "interruption.json").read_text())["status"],
                                     "interrupted_during_cleanup")


if __name__ == "__main__":
    unittest.main(verbosity=2)
