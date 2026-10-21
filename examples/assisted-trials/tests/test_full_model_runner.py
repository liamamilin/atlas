"""Model routing and bounded-dispatch checks; no provider or production DB calls."""

import json
import hashlib
from pathlib import Path
import plistlib
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import produce_all_leaves as runner
from produce_with_opencode import MODEL, MODELS
from template_factory.full_auxiliary import (
    FullAuxiliaryService,
    MODEL as FULL_MODEL,
    REVISED_MODEL,
    MODEL_SWITCH_AUTHORIZATION,
)
from template_factory.store import FactoryStore, FactoryError, digest


def load_path(path):
    return json.loads(Path(path).read_text())


class FullModelRunnerTests(unittest.TestCase):
    def test_new_model_is_accepted_by_opencode_cli_go(self):
        self.assertIn("open-design/deepseek-v4.1-flash", MODELS)

    def test_existing_checkpoint_uses_bound_historical_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            (pack / "applications").mkdir(parents=True)
            leaf_bytes = b"# Example\n"
            (pack / "applications/example.md").write_bytes(leaf_bytes)
            work = root / "attempt-1"
            stage = work / "calls/blueprint-generate-aux"
            stage.mkdir(parents=True)
            (work / "STAGE_PATHS.json").write_text(json.dumps({"blueprint-generate-aux": "calls/blueprint-generate-aux"}))
            (stage / "BINDING.json").write_text(json.dumps({"model": "opencode-go/minimax-m3.1-flash-free"}))

            class Store:
                def __init__(self):
                    self.pack = pack

            class Service:
                store = Store()
                ledger = "fixture-ledger"

                def effective_model(self, plan_id):
                    return MODEL

                def allowed_models(self, plan_id):
                    return [MODEL, "opencode-go/minimax-m3.1-flash-free"]

            observed = {}

            def fake_checkpoint(*args, **kwargs):
                observed["model"] = kwargs["model"]
                return {"research": "ok"}

            item = {"leaf": "example", "leaf_sha256": __import__("hashlib").sha256(leaf_bytes).hexdigest()}
            with patch.object(runner, "checkpoint", side_effect=fake_checkpoint):
                runner.stage_call(root, Service(), item, work, "blueprint-generate-aux", {}, "prompt", "content")
            self.assertEqual(observed["model"], "opencode-go/minimax-m3.1-flash-free")

    def _amended_service(self, root, leaf_bytes):
        pack = root / "pack"
        (pack / "applications").mkdir(parents=True)
        (pack / "applications/leaf.md").write_bytes(leaf_bytes)
        scope_path = root / "scope.json"
        auth_path = root / "auth.txt"
        scope_path.write_text(json.dumps({"full_plan_id": "plan", "items": [{"leaf": "leaf"}]}))
        auth_path.write_text("original plan authorization\n")
        user_auth = root / MODEL_SWITCH_AUTHORIZATION
        user_auth.parent.mkdir(parents=True)
        user_auth.write_text("operator authorizes the provider switch\n")
        store = FactoryStore(root / "state", pack)
        service = FullAuxiliaryService(store, "fixture", lambda: 1000.0)
        request = {
            "schema": "atlas.full-leaf-auxiliary-authorization.v1",
            "full_plan_id": "plan",
            "campaign_id": "fixture",
            "phase": "auxiliary-full-plan",
            "baseline": 0,
            "max_new_calls": 7200,
            "per_leaf_calls": 6,
            "concurrency": 2,
            "batch_size": 20,
            "window_seconds": 2592000,
            "model": FULL_MODEL,
            "scope": {"path": "scope.json", "sha256": hashlib.sha256(scope_path.read_bytes()).hexdigest()},
            "authorization": {"path": "auth.txt", "sha256": hashlib.sha256(auth_path.read_bytes()).hexdigest()},
        }
        service.register(request)
        service.control("plan", "resume")
        service.update_leaf("plan", "leaf", "running", {})
        service.control("plan", "pause")
        service.resume_selected("plan", ["leaf"])
        old = service.ledger.reserve(
            "plan:leaf", request["phase"], requested_model=FULL_MODEL,
            plan_id="plan", job_id="plan:leaf:attempt-1",
            stage="first/blueprint-generate-aux/attempt-1", kind="production",
        )
        service.ledger.finish(old["id"], "failed", outcome="cli_protocol")
        service.control("plan", "pause")
        amendment = {
            "schema": "atlas.full-leaf-model-revision.v1",
            "full_plan_id": "plan",
            "previous_model": FULL_MODEL,
            "new_model": REVISED_MODEL,
            "authorization_sha256": request["authorization"]["sha256"],
            "authorization": {
                "path": MODEL_SWITCH_AUTHORIZATION,
                "sha256": hashlib.sha256(user_auth.read_bytes()).hexdigest(),
            },
            "reason": "fixture authorized provider replacement",
        }
        service.register_model_revision(amendment)
        service.control("plan", "resume")
        return service, old["id"]

    def test_delivered_old_model_checkpoint_replays_without_cli_and_preserves_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            leaf = b"# Leaf\n"
            service, _old_id = self._amended_service(root, leaf)
            work = root / "items/leaf/attempt-1"
            stage = work / "calls/blueprint-generate-aux"
            stage.mkdir(parents=True)
            (work / "STAGE_PATHS.json").write_text(json.dumps({"blueprint-generate-aux": "calls/blueprint-generate-aux"}))
            (stage / "leaf.md").write_bytes(leaf)
            payload, prompt, result = {"fixture": True}, "fixed prompt", {"value": "old delivered result"}
            (stage / "input.json").write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")))
            binding = {
                "model": FULL_MODEL,
                "input_digest": digest(payload),
                "prompt": prompt,
                "source": {},
                "leaf_sha256": hashlib.sha256(leaf).hexdigest(),
            }
            (stage / "BINDING.json").write_text(json.dumps(binding, sort_keys=True, separators=(",", ":")))
            (stage / "RESULT.json").write_text(json.dumps(result, sort_keys=True, separators=(",", ":")))
            receipt = {"binding_digest": digest(binding), "result_digest": digest(result)}
            (stage / "DELIVERED.json").write_text(json.dumps(receipt, sort_keys=True, separators=(",", ":")))
            raw = {"text": json.dumps(result)}
            raw_bytes = json.dumps(raw, sort_keys=True, separators=(",", ":")).encode()
            (stage / "original-response.json").write_bytes(raw_bytes)
            summary = {
                "requested_model": FULL_MODEL,
                "delivery_status": "delivered",
                "session_id": "historical-session",
                "original_response_sha256": hashlib.sha256(raw_bytes).hexdigest(),
            }
            (stage / "cli-summary.json").write_text(json.dumps(summary, sort_keys=True, separators=(",", ":")))
            names = ("BINDING.json", "RESULT.json", "DELIVERED.json", "cli-summary.json")
            before = {name: (stage / name).read_bytes() for name in names}
            cli_calls = []

            class NeverCLI:
                def run(self, *args, **kwargs):
                    cli_calls.append(args)
                    raise AssertionError("delivered historical call must replay")

            item = {"leaf": "leaf", "leaf_sha256": hashlib.sha256(leaf).hexdigest()}
            with patch.object(runner, "PLAN_ID", "plan"), patch.object(runner, "CoordinatedCLI", return_value=NeverCLI()):
                got = runner.stage_call(root, service, item, work, "blueprint-generate-aux", payload, prompt, "production")
            self.assertEqual(got, result)
            self.assertEqual(cli_calls, [])
            self.assertEqual({name: (stage / name).read_bytes() for name in names}, before)

    def test_failed_old_model_checkpoint_gets_one_new_model_protocol_successor(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            leaf = b"# Leaf\n"
            service, old_id = self._amended_service(root, leaf)
            work = root / "items/leaf/attempt-1"
            stage = work / "calls/blueprint-generate-aux"
            stage.mkdir(parents=True)
            (work / "STAGE_PATHS.json").write_text(json.dumps({"blueprint-generate-aux": "calls/blueprint-generate-aux"}))
            (stage / "leaf.md").write_bytes(leaf)
            payload, prompt = {"fixture": True}, "fixed prompt"
            (stage / "input.json").write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")))
            binding = {
                "model": FULL_MODEL,
                "input_digest": digest(payload),
                "prompt": prompt,
                "source": {},
                "leaf_sha256": hashlib.sha256(leaf).hexdigest(),
            }
            (stage / "BINDING.json").write_text(json.dumps(binding, sort_keys=True, separators=(",", ":")))
            (stage / "LAUNCH_INTENT.json").write_text(json.dumps({"binding_digest": digest(binding)}, sort_keys=True, separators=(",", ":")))
            (stage / "cli-summary.json").write_text(json.dumps({"requested_model": FULL_MODEL, "delivery_status": "failed", "failure_code": "cli_protocol", "output_observed": True}))
            (stage / "original-response.json").write_text(json.dumps({"text": "old malformed response"}))
            cli_seen = []

            class FailingSuccessorCLI:
                def run(self, directory, _prompt, model, _timeout, _cancelled, _progress, **kwargs):
                    budget = kwargs["budget"]
                    reservation = budget["ledger"].reserve(
                        budget["identity"], budget["phase"], budget["kind"],
                        job_id=budget["job_id"], requested_model=model,
                        plan_id=budget["plan_id"], stage=budget["stage"],
                    )
                    budget["ledger"].finish(reservation["id"], "failed", outcome="cli_protocol")
                    cli_seen.append((model, budget["stage"], reservation["id"]))
                    (Path(directory) / "cli-summary.json").write_text(json.dumps({
                        "requested_model": model,
                        "delivery_status": "failed",
                        "failure_code": "cli_protocol",
                        "output_observed": True,
                    }))
                    (Path(directory) / "original-response.json").write_text(json.dumps({"text": "successor malformed response"}))
                    raise FactoryError("mock invalid JSON", "cli_protocol", 409)

            item = {"leaf": "leaf", "leaf_sha256": hashlib.sha256(leaf).hexdigest()}
            with patch.object(runner, "PLAN_ID", "plan"), patch.object(runner, "CoordinatedCLI", return_value=FailingSuccessorCLI()):
                with self.assertRaises(FactoryError) as first:
                    runner.stage_call(root, service, item, work, "blueprint-generate-aux", payload, prompt, "production")
                self.assertEqual(first.exception.code, "cli_protocol")
                count_before_retry = service.status("plan")["new_calls"]
                with self.assertRaisesRegex(ValueError, "do not launch a duplicate"):
                    runner.stage_call(root, service, item, work, "blueprint-generate-aux", payload, prompt, "production")
            self.assertEqual(len(cli_seen), 1)
            self.assertEqual(cli_seen[0][0], REVISED_MODEL)
            self.assertEqual(cli_seen[0][1], "protocol/blueprint-generate-aux/attempt-1")
            self.assertEqual(service.status("plan")["new_calls"], count_before_retry)
            rows = service.status("plan")["calls"]
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["id"], old_id)
            self.assertEqual(rows[0]["requested_model"], FULL_MODEL)
            self.assertEqual(rows[0]["status"], "failed")
            self.assertEqual(rows[1]["requested_model"], REVISED_MODEL)
            self.assertEqual(rows[1]["status"], "failed")
            self.assertEqual(load_path(stage / "BINDING.json")["model"], FULL_MODEL)
            successor = work / "calls/blueprint-generate-aux-protocol-1"
            self.assertEqual(load_path(successor / "BINDING.json")["model"], REVISED_MODEL)

    def test_selected_first_pass_pauses_even_when_repair_is_pending(self):
        rows = [
            {"leaf": "pilot-a", "state": "ready_not_run", "first_pass_done": True},
            {"leaf": "pilot-b", "state": "needs_revision", "first_pass_done": True, "repair_pending": True},
            {"leaf": "outside", "state": "pending"},
        ]
        self.assertTrue(runner.selected_first_pass_complete(rows, {"pilot-a", "pilot-b"}))
        rows[1]["first_pass_done"] = False
        self.assertFalse(runner.selected_first_pass_complete(rows, {"pilot-a", "pilot-b"}))

    def test_runner_inherits_only_the_persisted_three_leaf_dispatch(self):
        leaves = {"e-book-library-application", "markdown-editor", "resource-calendar"}
        self.assertEqual(runner.effective_dispatch_selection([], leaves, leaves), leaves)
        self.assertEqual(runner.effective_dispatch_selection(leaves, leaves, leaves), leaves)
        with self.assertRaisesRegex(ValueError, "differ from the active durable dispatch"):
            runner.effective_dispatch_selection(leaves | {"outside"}, leaves, leaves | {"outside"})
        with self.assertRaisesRegex(ValueError, "selected run must be activated"):
            runner.effective_dispatch_selection(leaves, [], leaves)

    def test_running_start_rejects_a_subset_of_active_dispatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, _calls, fake_run, _events, state, _timeline = self._daemon_fixture(root)
            state["selected"] = ["e-book-library-application", "markdown-editor", "resource-calendar"]
            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fake_run):
                with self.assertRaisesRegex(ValueError, "exactly match the active durable dispatch"):
                    runner.start_daemon(root, "http://fixture", ["e-book-library-application"])

    def _daemon_fixture(self, root, *, active_calls=0, print_output="state = waiting\n", status="running"):
        root.mkdir(exist_ok=True)
        bounded_leaves = ["e-book-library-application", "markdown-editor", "resource-calendar"]
        (root / "FROZEN_SCOPE.json").write_text(json.dumps({"items": [{"leaf": leaf} for leaf in ["pilot", *bounded_leaves]]}))
        state = {"active_calls": active_calls, "status": status, "selected": []}
        events = []
        timeline = []

        class Service:
            def control_state(self, plan_id):
                return state["status"]

            def status(self, plan_id):
                return dict(state)

            def selected_leaves(self, plan_id):
                return list(state["selected"])

            def resume_selected(self, plan_id, leaves):
                events.append(("resume_selected", list(leaves)))
                timeline.append(("service", "resume_selected"))
                state["selected"] = sorted(leaves)
                state["status"] = "running"

            def control(self, plan_id, action, reason=None):
                events.append(("control", action, reason))
                timeline.append(("service", action))
                state["status"] = action
                return dict(state)

        service = Service()
        calls = []

        class Completed:
            def __init__(self, command):
                self.returncode = 1 if command[1] == "print" and not (root / "coordinator.plist").exists() else 0
                self.stdout = print_output if command[1] == "print" else ""
                self.stderr = ""

        def fake_run(command, **kwargs):
            calls.append(command)
            timeline.append(("launchctl", command[1]))
            return Completed(command)

        return service, calls, fake_run, events, state, timeline

    def test_same_label_daemon_reconfigures_only_selected_leaf_arguments(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, calls, fake_run, events, state, timeline = self._daemon_fixture(root)
            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fake_run):
                runner.start_daemon(root, "http://fixture")
                before = (root / "coordinator.plist").read_bytes()
                state["status"] = "paused"
                runner.start_daemon(root, "http://fixture", ["e-book-library-application", "markdown-editor", "resource-calendar"])
                pilot_bytes = (root / "coordinator.plist").read_bytes()
                runner.start_daemon(root, "http://fixture", [])
            current = plistlib.loads((root / "coordinator.plist").read_bytes())
            self.assertNotIn("--leaf", current["ProgramArguments"])
            archives = list(root.glob("coordinator.previous-*.plist"))
            self.assertEqual(len(archives), 2)
            self.assertIn(before, [path.read_bytes() for path in archives])
            self.assertIn(pilot_bytes, [path.read_bytes() for path in archives])
            self.assertNotEqual(before, pilot_bytes)
            operations = [call[1] for call in calls]
            self.assertEqual(operations.count("bootout"), 2)
            for index, operation in enumerate(operations):
                if operation == "bootout":
                    self.assertEqual(operations[index + 1], "bootstrap")
            self.assertEqual(events, [("resume_selected", ["e-book-library-application", "markdown-editor", "resource-calendar"])])
            resume_index = timeline.index(("service", "resume_selected"))
            self.assertGreater(resume_index, timeline.index(("launchctl", "bootout")))
            self.assertEqual(timeline[resume_index + 1], ("launchctl", "bootstrap"))
            self.assertNotIn(("service", "resume"), timeline)

    def test_daemon_refuses_live_or_active_and_unrelated_definition_changes(self):
        for output, active_calls in (("pid = 4321\n", 0), ("state = waiting\n", 1)):
            with self.subTest(output=output, active_calls=active_calls), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp) / "runner"
                service, _, fake_run, _events, state, _timeline = self._daemon_fixture(root, active_calls=0)
                with patch.object(runner, "host", return_value=(None, service)), \
                        patch.object(runner, "verify_plan"), \
                        patch.object(runner.subprocess, "run", side_effect=fake_run):
                    runner.start_daemon(root, "http://fixture")
                    old = (root / "coordinator.plist").read_bytes()
                    state["status"] = "paused"
                    state["active_calls"] = active_calls
                    with patch.object(runner.subprocess, "run", side_effect=lambda command, **kwargs: type("R", (), {"returncode": 0, "stdout": output, "stderr": ""})()):
                        with self.assertRaisesRegex(ValueError, "while (coordinator|model) calls are active|coordinator is live"):
                            runner.start_daemon(root, "http://fixture", ["pilot"])
                    self.assertEqual((root / "coordinator.plist").read_bytes(), old)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, _, fake_run, _events, state, _timeline = self._daemon_fixture(root)
            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fake_run):
                runner.start_daemon(root, "http://fixture")
                plist = root / "coordinator.plist"
                config = plistlib.loads(plist.read_bytes())
                config["ProgramArguments"][0] = "/unexpected/python"
                plist.write_bytes(plistlib.dumps(config))
                state["status"] = "paused"
                with self.assertRaisesRegex(ValueError, "beyond selected leaf arguments"):
                    runner.start_daemon(root, "http://fixture", ["pilot"])

    def test_paused_selected_bootstrap_failure_repauses_and_keeps_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, _calls, fake_run, events, state, timeline = self._daemon_fixture(root, status="paused")

            def fail_bootstrap(command, **kwargs):
                timeline.append(("launchctl", command[1]))
                if command[1] == "bootstrap":
                    raise runner.subprocess.CalledProcessError(5, command)
                return type("Result", (), {"returncode": 1, "stdout": "", "stderr": ""})()

            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fail_bootstrap):
                with self.assertRaises(runner.subprocess.CalledProcessError):
                    runner.start_daemon(root, "http://fixture", ["pilot"])
            self.assertEqual(events[0], ("resume_selected", ["pilot"]))
            self.assertEqual(state["selected"], ["pilot"])
            self.assertEqual(state["status"], "pause")
            self.assertEqual(timeline, [
                ("launchctl", "print"),
                ("service", "resume_selected"),
                ("launchctl", "bootstrap"),
                ("service", "pause"),
            ])

    def test_final_launchd_verification_failure_repauses_and_keeps_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, _calls, _fake_run, events, state, timeline = self._daemon_fixture(root, status="paused")
            print_calls = 0

            def fail_final_print(command, **kwargs):
                nonlocal print_calls
                timeline.append(("launchctl", command[1]))
                if command[1] == "print":
                    print_calls += 1
                    if print_calls == 1:
                        return type("Result", (), {"returncode": 1, "stdout": "", "stderr": ""})()
                    raise runner.subprocess.CalledProcessError(5, command)
                return type("Result", (), {"returncode": 0, "stdout": "", "stderr": ""})()

            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fail_final_print):
                with self.assertRaises(runner.subprocess.CalledProcessError):
                    runner.start_daemon(root, "http://fixture", ["pilot"])
            self.assertEqual(events[0], ("resume_selected", ["pilot"]))
            self.assertEqual(state["selected"], ["pilot"])
            self.assertEqual(state["status"], "pause")
            self.assertEqual(timeline, [
                ("launchctl", "print"),
                ("service", "resume_selected"),
                ("launchctl", "bootstrap"),
                ("launchctl", "print"),
                ("service", "pause"),
            ])

    def test_paused_plan_rejects_unbounded_start(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "runner"
            service, _calls, fake_run, events, _state, _timeline = self._daemon_fixture(root, status="paused")
            with patch.object(runner, "host", return_value=(None, service)), \
                    patch.object(runner, "verify_plan"), \
                    patch.object(runner.subprocess, "run", side_effect=fake_run):
                with self.assertRaisesRegex(ValueError, "only with selected leaves"):
                    runner.start_daemon(root, "http://fixture")
            self.assertEqual(events, [])


if __name__ == "__main__":
    unittest.main()
