"""Real subprocess transport checks; no Docker daemon or candidate code."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.blueprint_runtime import _strict_result
from template_factory.runtime import DockerVerifier
from template_factory.store import FactoryError


class RuntimeTransportTests(unittest.TestCase):
    def call(self, code):
        verifier = DockerVerifier(timeout=5)
        verifier.executable = sys.executable
        return verifier._call(["-c", code], lambda: False)

    def test_protocol_stdout_and_diagnostic_stderr_stay_separate(self):
        result = self.call("import sys; print('{}'); print('diagnostic',file=sys.stderr)")
        self.assertEqual(json.loads(result["stdout"]), {})
        self.assertIn("diagnostic", result["stderr"])
        self.assertFalse(result["stdout_truncated"])

    def test_protocol_parser_sees_both_objects_despite_display_tail_cut(self):
        failed = {"schema": "atlas.acceptance-result.v1", "case_id": "A01", "status": "failed", "assertions": [{"id": "x", "passed": False, "detail": "actual failure"}]}
        passed = {**failed, "status": "passed", "assertions": [{"id": "x", "passed": True, "detail": "later claim"}]}
        full = json.dumps(failed) + " " * 16000 + json.dumps(passed)
        result = self.call("import sys; sys.stdout.write(" + repr(full) + ")")
        self.assertIsNone(_strict_result(result["stdout"], "A01"))
        self.assertIn("actual failure", result["stdout"])
        self.assertNotIn("actual failure", result["output"])

    def test_truncated_protocol_output_is_explicit_and_uses_prefix(self):
        result = self.call("import sys; sys.stdout.write('first'+ ' '*70000+'last')")
        self.assertTrue(result["stdout_truncated"])
        self.assertEqual(len(result["stdout"]), 64000)
        self.assertTrue(result["stdout"].startswith("first"))

    def test_fast_oversized_output_is_rejected_after_exit(self):
        with self.assertRaises(FactoryError) as caught:
            self.call("import sys; sys.stdout.write('x'*8000001)")
        self.assertEqual(caught.exception.code, "verification_output_limit")

    def test_runtime_commands_cannot_inherit_parent_stdin(self):
        result = self.call("import sys; print(repr(sys.stdin.read()))")
        self.assertEqual(result["stdout"].strip(), "''")


if __name__ == "__main__":
    unittest.main()
