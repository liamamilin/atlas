"""Recovery, review and containment checks without any real model call."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from produce_with_opencode import (CHECKS, MODEL, checkpoint, fixed_json, safe_file,
                                  readable_candidate, validate_generation, validate_review, validate_read_coverage,
                                  verify_production)
from produce_batch import authored_definition


class FakeCLI:
    def __init__(self):
        self.calls = 0

    def run(self, *args, **kwargs):
        self.calls += 1
        return {"value": 42}


class ProducerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_reentry_uses_delivered_result_and_binds_prompt_source_and_leaf(self):
        source = self.root / "source"
        source.mkdir()
        (source / "upstream.txt").write_text("fixed code")
        cli = FakeCLI()
        args = (self.root / "stage", {"fixed": 1}, "prompt", cli, {}, source, b"leaf")
        self.assertEqual(checkpoint(*args), {"value": 42})
        self.assertEqual(checkpoint(*args), {"value": 42})
        self.assertEqual(cli.calls, 1)
        with self.assertRaisesRegex(ValueError, "fixed input changed"):
            checkpoint(args[0], args[1], "different", cli, {}, source, b"leaf")
        (source / "upstream.txt").write_text("changed code")
        with self.assertRaisesRegex(ValueError, "read-source changed"):
            checkpoint(*args)
        self.assertEqual(cli.calls, 1)

    def test_crash_after_delivery_recovers_raw_response_without_call(self):
        stage, cli = self.root / "stage", FakeCLI()
        checkpoint(stage, {}, "prompt", cli, {})
        (stage / "DELIVERED.json").unlink()
        (stage / "RESULT.json").unlink()
        fixed_json(stage / "cli-summary.json", {"delivery_status": "delivered", "session_id": "real"})
        fixed_json(stage / "original-response.json", {"text": '{"value":42}'})
        self.assertEqual(checkpoint(stage, {}, "prompt", cli, {}), {"value": 42})
        self.assertEqual(cli.calls, 1)

    def test_uncertain_or_failed_attempt_never_blindly_relaunches(self):
        stage, cli = self.root / "stage", FakeCLI()
        checkpoint(stage, {}, "prompt", cli, {})
        (stage / "DELIVERED.json").unlink()
        for status in ("uncertain", "failed"):
            (stage / "cli-summary.json").write_text(json.dumps({"delivery_status": status}))
            with self.assertRaisesRegex(ValueError, "do not launch a duplicate"):
                checkpoint(stage, {}, "prompt", cli, {})
        self.assertEqual(cli.calls, 1)

    def test_changed_delivered_result_rejected(self):
        cli, stage = FakeCLI(), self.root / "stage"
        checkpoint(stage, {}, "prompt", cli, {})
        (stage / "RESULT.json").write_text('{"value":99}')
        with self.assertRaisesRegex(ValueError, "checkpoint result differs"):
            checkpoint(stage, {}, "prompt", cli, {})

    def test_incomplete_or_same_session_review_cannot_pass(self):
        review = {"input_digest": "abc", "verdict": "pass", "issues": [],
                  "checks": {key: True for key in CHECKS},
                  "observations": [{"index": 0, "verdict": "accepted", "reason": "code lines checked"}]}
        validate_review(review, "abc", "author", "review", 1)
        for mutate in (lambda r: r.update(input_digest="other"),
                       lambda r: r["checks"].pop("acceptance"),
                       lambda r: r["checks"].update(core_journey=False),
                       lambda r: r.update(issues=["missing branch"]),
                       lambda r: r.update(observations=[])):
            bad = copy.deepcopy(review)
            mutate(bad)
            with self.assertRaises(ValueError):
                validate_review(bad, "abc", "author", "review", 1)
        with self.assertRaisesRegex(ValueError, "distinct actual session"):
            validate_review(review, "abc", "same", "same", 1)

    def test_generated_code_is_parsed_not_executed_and_citations_bounded(self):
        (self.root / "code.py").write_text("first\nsecond\n")
        snapshot = {"repository": "https://github.com/example/repo", "local_root": str(self.root),
                    "files": {"code.py": "unused"}, "license": {"spdx_id": "MIT"}, "license_files": ["LICENSE"]}
        marker = self.root / "MUST_NOT_EXIST"
        value = {"authored": {**{k: "text" for k in ("name", "audience", "objective", "inference", "arch")},
                             **{k: ["one"] for k in ("workflow", "acceptance", "gaps")},
                             "features": ["a", "b", "c"], "goals": ["a", "b", "c"],
                             "observations": [["documentation", "code.py", 1, 1, "a"],
                                              ["code_observation", "code.py", 2, 2, "b"]]},
                 "acceptance_files": {"probe.py": f"open({str(marker)!r}, 'w').write('bad')\n"}}
        validate_generation(value, snapshot)
        self.assertFalse(marker.exists())
        value["authored"]["observations"][1][3] = 3
        with self.assertRaisesRegex(ValueError, "outside source"):
            validate_generation(value, snapshot)

    def test_paths_cannot_escape_workspace(self):
        for name in ("../outside", "/absolute", "a/../b", "a//b", "a\\b", ""):
            with self.assertRaises(ValueError):
                safe_file(name)

    def test_failed_latest_review_cannot_be_bypassed_by_the_legacy_batch_entry(self):
        fixed_json(self.root / "SUPPLEMENTAL_FAILURE.json", {"status": "needs_changes"})
        with self.assertRaisesRegex(ValueError, "do not register/re-export as usable"):
            verify_production(self.root, {}, {}, {})

    def test_previous_ten_authored_definitions_remain_identical(self):
        root = Path(__file__).resolve().parents[3]
        folder = root / "docs/template-factory/assisted-batch-10-2026-10-21"
        manifest = json.loads((folder / "MANIFEST.json").read_text())
        for item in manifest["items"]:
            p = folder / item["key"]
            load = lambda name: json.loads((p / name).read_text())
            with self.subTest(item=item["key"]):
                actual = authored_definition(item, load("AUTHOR_INPUT.json"), load("scenario.json"),
                                             load("case-record.json"), load("source-snapshot.json"))
                self.assertEqual(actual, load("definition.json"))

    def test_long_json_read_view_is_exact_and_original_is_preserved(self):
        long_arch = "# Interface\n" + "\n".join(f"Endpoint {i}: explicit semantics" for i in range(300))
        value = {"arch": long_arch, "name": "Home care", "features": ["a", "b", "c"]}
        original = self.root / "AUTHOR_INPUT.json"
        fixed_json(original, value)
        before = original.read_bytes()
        views = readable_candidate(self.root, value)
        self.assertEqual((self.root / "VIEW_ARCH.md").read_text(), long_arch)
        self.assertEqual(views["VIEW_ARCH.md"]["json_pointer"], "/arch")
        self.assertEqual(original.read_bytes(), before)
        self.assertTrue(all(len(line) < 2000 for line in (self.root / "VIEW_ARCH.md").read_text().splitlines()))
        readable_candidate(self.root, value)
        self.assertEqual(original.read_bytes(), before)

    def test_review_must_actually_receive_all_architecture_lines(self):
        stage = self.root / "stage"
        candidate = stage / "source/candidate"
        candidate.mkdir(parents=True)
        arch = "\n".join("architecture line " + str(i) + " x" * 40 for i in range(30))
        readable_candidate(candidate, {"arch": arch})
        path = str((candidate / "VIEW_ARCH.md").resolve())
        def event(output):
            return {"type": "tool_use", "part": {"tool": "read", "state": {
                "status": "completed", "input": {"path": path}, "output": output}}}
        output = "\n".join(f"{i}: {line}" for i, line in enumerate(arch.splitlines(), 1))
        (stage / "events.jsonl").write_text(json.dumps(event(output)) + "\n")
        validate_read_coverage(stage, {"arch": arch})
        (stage / "events.jsonl").write_text(json.dumps(event(output.rsplit("\n", 1)[0])) + "\n")
        with self.assertRaisesRegex(ValueError, "full long-field view"):
            validate_read_coverage(stage, {"arch": arch})


if __name__ == "__main__":
    unittest.main()
