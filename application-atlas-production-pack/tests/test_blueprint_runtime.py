"""Focused tests for pinned cognitive acceptance runner execution."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.blueprint_runtime import BlueprintRuntimeVerifier, _strict_result, validate_runner_manifest
from template_factory.store import FactoryError


class MockDocker(BlueprintRuntimeVerifier):
    def __init__(self, *, start_fails=False, protocol="passed", cancel_at=None, partial_test_create=False):
        super().__init__(timeout=3)
        self.executable = "docker"
        self.commands = []
        self.start_fails = start_fails
        self.protocol = protocol
        self.cancel_at = cancel_at
        self.partial_test_create = partial_test_create

    def info(self):
        return {"available": True}

    def _call(self, argv, cancelled, timeout=None):
        self.commands.append(list(argv))
        if self.cancel_at is not None and len(self.commands) >= self.cancel_at:
            raise FactoryError("verification cancelled", "cancelled", 409)
        if argv[:2] == ["rm", "-f"] and self.partial_test_create and "-test-" in " ".join(argv):
            return {"argv": argv, "exit_code": 1, "output": "Error: No such container", "passed": False}
        elif argv[:2] == ["image", "inspect"] and "--format" in argv:
            output = "sha256:" + format(abs(hash(argv[-1])) % (16 ** 64), "064x")
        elif argv and argv[0] == "exec" and "-d" in argv:
            output = "synthetic start failure" if self.start_fails else ""
            if self.start_fails:
                return {"argv": argv, "exit_code": 1, "output": output, "passed": False}
        elif argv and argv[0] == "run" and "-test-" in " ".join(argv) and self.partial_test_create:
            return {"argv": argv, "exit_code": 1, "output": "synthetic container creation error", "passed": False}
        elif argv and argv[0] == "exec" and len(argv) >= 4 and argv[2] == "cat":
            output = "startup stderr evidence" if argv[-1].endswith("stderr") else "startup stdout evidence"
        elif argv and argv[0] == "exec" and "/suite/" in " ".join(argv):
            case_id = "A01" if "/suite/acceptance/a.py" in " ".join(argv) else "A02"
            if self.protocol == "invalid":
                output = '{"schema":"atlas.acceptance-result.v1","case_id":"A01","status":"passed","assertions":[]}'
            elif self.protocol == "two-object":
                failed = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id":case_id, "status":"failed", "assertions":[{"id":"assert-1", "passed":False, "detail":"first"}]})
                passed = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id":case_id, "status":"passed", "assertions":[{"id":"assert-2", "passed":True, "detail":"second"}]})
                output = failed + (" " * 16000) + passed
                return {"argv": argv, "exit_code": 0, "output": output, "stdout": output,
                        "stderr": "", "stdout_truncated": False, "passed": True}
            elif self.protocol == "truncated":
                output = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id":case_id,
                                     "status":"passed", "assertions":[{"id":"assert-1", "passed":True, "detail":"ok"}]})
                return {"argv": argv, "exit_code": 0, "output": output, "stdout": output,
                        "stderr": "", "stdout_truncated": True, "passed": True}
            elif self.protocol == "false":
                output = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id": case_id,
                                     "status":"passed", "assertions":[{"id":"assert-1", "passed":False, "detail":"no"}]})
            elif self.protocol == "failed-exit":
                output = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id": case_id,
                                     "status":"failed", "assertions":[{"id":"assert-1", "passed":False, "detail":"expected miss"}]})
                return {"argv": argv, "exit_code": 1, "output": output, "passed": False}
            elif self.protocol == "pass-nonzero":
                output = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id": case_id,
                                     "status":"passed", "assertions":[{"id":"assert-1", "passed":True, "detail":"conflicting exit"}]})
                return {"argv": argv, "exit_code": 1, "output": output, "passed": False}
            else:
                output = json.dumps({"schema":"atlas.acceptance-result.v1", "case_id": case_id,
                                     "status":"passed", "assertions":[{"id":"assert-1", "passed":True, "detail":"ok"}]})
        else:
            output = ""
        if argv and argv[0] == "exec" and "/suite/" in " ".join(argv):
            return {"argv": argv, "exit_code": 0, "output": output + "\nruntime diagnostic", "stdout": output,
                    "stderr": "runtime diagnostic", "stdout_truncated": False, "passed": True}
        return {"argv": argv, "exit_code": 0, "output": output, "passed": True}


class BlueprintRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.source = self.root / "source"
        (self.source / "acceptance").mkdir(parents=True)
        (self.source / "acceptance" / "a.py").write_text("print('not run on host')\n")
        (self.source / "acceptance" / "b.js").write_text("console.log('not run on host')\n")
        self.spec = {"phases": [{"id":"P0"}, {"id":"P1"}], "acceptance": [
            {"id":"A01", "phase":"P0", "implementation":"acceptance/a.py"},
            {"id":"A02", "phase":"P1", "implementation":"acceptance/b.js"},
        ]}
        self.write_manifest({"A01":{"args":["--base-url", "{base_url}", "{case_id}"]},
                             "A02":{"args":["literal", "{data_dir}"]}})
        self.app = self.root / "app"
        self.app.mkdir()
        (self.app / "main.py").write_text("print('application')\n")
        self.evidence = self.root / "evidence"
        self.runtime = {"profile":"python-web", "install":[], "build":[], "start":["python3", "main.py"], "port":8080}

    def tearDown(self):
        self.tmp.cleanup()

    def write_manifest(self, cases):
        (self.source / "acceptance" / "runner.json").write_text(json.dumps({
            "schema":"atlas.acceptance-runner.v1", "result_schema":"atlas.acceptance-result.v1", "cases":cases
        }))

    def test_manifest_requires_exact_normative_ids_and_prerequisite_phase(self):
        result = validate_runner_manifest(self.source, self.spec, "P1")
        self.assertEqual(result["selected_case_ids"], ["A01", "A02"])
        self.assertEqual(result["cases"]["A01"]["args"][1], {"placeholder":"base_url"})
        empty_selected = {**self.spec, "acceptance":[{**self.spec["acceptance"][0], "phase":"P9"}]}
        self.write_manifest({"A01":{"args":[]}})
        with self.assertRaises(FactoryError):
            validate_runner_manifest(self.source, empty_selected, "P0")
        self.write_manifest({"A01":{"args":[]}})
        with self.assertRaises(FactoryError):
            validate_runner_manifest(self.source, self.spec)
        self.write_manifest({"A01":{"args":[]}, "A02":{"args":[]}, "A99":{"args":[]}})
        with self.assertRaises(FactoryError):
            validate_runner_manifest(self.source, self.spec)

    def test_missing_legacy_binding_is_unavailable(self):
        (self.source / "acceptance" / "runner.json").unlink()
        with self.assertRaises(FactoryError) as caught:
            validate_runner_manifest(self.source, self.spec)
        self.assertEqual(caught.exception.code, "acceptance_adapter_missing")

    def test_unknown_placeholder_and_unsupported_legacy_program_are_rejected(self):
        for token in ("{shell}", "--base={base_url}", "{base_url", "base_url}"):
            self.write_manifest({"A01":{"args":[token]}, "A02":{"args":[]}})
            with self.subTest(token=token), self.assertRaises(FactoryError):
                validate_runner_manifest(self.source, self.spec)
        bad = {**self.spec, "acceptance":[{**self.spec["acceptance"][0], "implementation":"acceptance/old.sh"}]}
        with self.assertRaises(FactoryError) as caught:
            validate_runner_manifest(self.source, bad)
        self.assertEqual(caught.exception.code, "acceptance_adapter_missing")

    def test_startup_failure_prevents_cases_and_cleanup_runs(self):
        verifier = MockDocker(start_fails=True)
        report = verifier.verify(self.app, self.source, self.spec, None, self.evidence, self.runtime)
        self.assertEqual(report["outcome"], "blocked")
        self.assertEqual(report["case_results"], [])
        self.assertTrue(any(command[0] == "rm" for command in verifier.commands))

    def test_exit_zero_with_invalid_or_false_protocol_never_passes(self):
        for protocol in ("invalid", "false"):
            verifier = MockDocker(protocol=protocol)
            report = verifier.verify(self.app, self.source, self.spec, "P0", self.evidence / protocol, self.runtime)
            self.assertFalse(report["passed"])
            self.assertEqual(report["case_results"][0]["status"], "unverified" if protocol == "invalid" else "failed")
            self.assertEqual(report["case_results"][0]["id"], "A01")
            self.assertTrue(report["case_results"][0]["reason"])

    def test_valid_failure_with_nonzero_exit_is_blocked_but_conflicting_pass_is_unverified(self):
        failed = MockDocker(protocol="failed-exit").verify(self.app, self.source, self.spec, "P0", self.evidence / "failed", self.runtime)
        self.assertEqual(failed["case_results"][0]["status"], "failed")
        self.assertEqual(failed["outcome"], "blocked")
        conflicting = MockDocker(protocol="pass-nonzero").verify(self.app, self.source, self.spec, "P0", self.evidence / "conflict", self.runtime)
        self.assertEqual(conflicting["case_results"][0]["status"], "unverified")
        self.assertEqual(conflicting["outcome"], "unavailable")

    def test_duplicate_json_fields_are_not_accepted(self):
        value = '{"schema":"atlas.acceptance-result.v1","schema":"atlas.acceptance-result.v1","case_id":"A01","status":"passed","assertions":[{"id":"a","passed":true,"detail":"ok"}]}'
        self.assertIsNone(_strict_result(value, "A01"))

    def test_protocol_uses_stdout_while_retaining_stderr_diagnostics(self):
        verifier = MockDocker(protocol="passed")
        report = verifier.verify(self.app, self.source, self.spec, "P0", self.evidence, self.runtime)
        self.assertTrue(report["passed"])
        self.assertEqual(report["case_results"][0]["status"], "passed")
        self.assertEqual(report["case_results"][0]["stderr"], "runtime diagnostic")

    def test_truncated_and_multiple_json_objects_never_pass(self):
        for protocol, expected_reason in (("truncated", "truncated"), ("two-object", "protocol")):
            verifier = MockDocker(protocol=protocol)
            report = verifier.verify(self.app, self.source, self.spec, "P0", self.evidence / protocol, self.runtime)
            row = report["case_results"][0]
            self.assertFalse(row["passed"])
            self.assertEqual(row["status"], "unverified")
            self.assertIn(expected_reason, row["reason"])

        verifier = MockDocker(protocol="passed")
        report = verifier.verify(self.app, self.source, self.spec, "P0", self.evidence / "complete", self.runtime)
        self.assertTrue(report["passed"])

    def test_success_uses_read_only_suite_and_application_mounts_and_separate_images(self):
        original = (self.app / "main.py").read_bytes()
        verifier = MockDocker()
        report = verifier.verify(self.app, self.source, self.spec, "P1", self.evidence, self.runtime)
        self.assertTrue(report["passed"])
        self.assertEqual((self.app / "main.py").read_bytes(), original)
        run_commands = [row for row in verifier.commands if row and row[0] == "run"]
        self.assertTrue(all("--network" in row for row in run_commands))
        app_run = next(row for row in run_commands if "/workspace" in " ".join(row))
        self.assertIn("/state:rw,nosuid,size=128m,mode=1777", app_run)
        test_run = next(row for row in run_commands if "dst=/suite,readonly" in " ".join(row))
        self.assertIn("dst=/application,readonly", " ".join(test_run))
        image_bindings = report["environment"]["images"]
        references = {value["reference"] for value in image_bindings.values()}
        self.assertIn("python:3.12-slim", references)
        self.assertIn("node:22-bookworm-slim", references)
        self.assertTrue(all(key.startswith("sha256:") for key in image_bindings))
        self.assertEqual(report["app_source_unchanged"], True)
        self.assertTrue(report["cleanup"]["workspace_removed"])
        self.assertIn("startup stderr evidence", report["startup"]["captured_output"]["stderr"])
        launch = next(row for row in verifier.commands if row[:2] == ["exec", "-d"])
        self.assertTrue(any("/state/startup.stderr" in arg for arg in launch))

    def test_partial_tester_creation_is_cleaned_without_false_cleanup_failure(self):
        verifier = MockDocker(partial_test_create=True)
        with self.assertRaises(FactoryError):
            verifier.verify(self.app, self.source, self.spec, None, self.evidence, self.runtime)
        report = json.loads((self.evidence / "report.json").read_text())
        self.assertEqual(report["outcome"], "unavailable")
        self.assertTrue(any(row[:2] == ["rm", "-f"] for row in verifier.commands))
        self.assertTrue(report["cleanup"]["success"])

    def test_cancellation_removes_containers_and_preserves_report(self):
        verifier = MockDocker(cancel_at=5)
        with self.assertRaises(FactoryError):
            verifier.verify(self.app, self.source, self.spec, None, self.evidence, self.runtime)
        self.assertTrue(any(row[0] == "rm" for row in verifier.commands))
        self.assertTrue((self.evidence / "report.json").is_file())

    def test_total_deadline_is_applied_before_startup_and_still_cleans_up(self):
        verifier = MockDocker()
        verifier.timeout = 0
        with self.assertRaises(FactoryError) as caught:
            verifier.verify(self.app, self.source, self.spec, None, self.evidence, self.runtime)
        self.assertEqual(caught.exception.code, "verification_timeout")
        self.assertTrue((self.evidence / "report.json").is_file())


if __name__ == "__main__":
    unittest.main()
