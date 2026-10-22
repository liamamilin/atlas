"""Recovery, review and containment checks without any real model call."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from produce_with_opencode import (CHECKS, MODEL, checkpoint, fixed_json, safe_file,
                                  readable_candidate, validate_generation, validate_review, validate_read_coverage,
                                  verify_production, snapshot_audit)
from produce_batch import authored_definition
from template_factory.store import FactoryError, digest
from produce_with_opencode import pin_sources


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
        args = (self.root / "calls/stage", {"fixed": 1}, "prompt", cli, {}, source, b"leaf")
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
        stage, cli = self.root / "calls/stage", FakeCLI()
        checkpoint(stage, {}, "prompt", cli, {})
        (stage / "DELIVERED.json").unlink()
        (stage / "RESULT.json").unlink()
        fixed_json(stage / "cli-summary.json", {"delivery_status": "delivered", "session_id": "real"})
        fixed_json(stage / "original-response.json", {"text": '{"value":42}'})
        self.assertEqual(checkpoint(stage, {}, "prompt", cli, {}), {"value": 42})
        self.assertEqual(cli.calls, 1)

    def test_uncertain_or_failed_attempt_never_blindly_relaunches(self):
        stage, cli = self.root / "calls/stage", FakeCLI()
        checkpoint(stage, {}, "prompt", cli, {})
        (stage / "DELIVERED.json").unlink()
        for status in ("uncertain", "failed"):
            (stage / "cli-summary.json").write_text(json.dumps({"delivery_status": status}))
            with self.assertRaisesRegex(ValueError, "do not launch a duplicate"):
                checkpoint(stage, {}, "prompt", cli, {})
        self.assertEqual(cli.calls, 1)

    def test_changed_delivered_result_rejected(self):
        cli, stage = FakeCLI(), self.root / "calls/stage"
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

    def test_pin_sources_preserves_existing_snapshot_bytes_through_storage_alias_without_fetch(self):
        import hashlib
        store_root = self.root / "state"
        store_root.mkdir()
        external = self.root / "external-sources"
        external.mkdir()
        alias = store_root / "sources"
        alias.symlink_to(external, target_is_directory=True)
        folder = self.root / "items/leaf-0/attempt-1"
        folder.mkdir(parents=True)
        local = external / "p/leaf-0/attempt-1"
        local.mkdir(parents=True)
        for name, content in {"README.md": b"readme\n", "LICENSE": b"MIT\n"}.items():
            (local / name).write_bytes(content)
        proposal = {"repository": "https://github.com/example/repo", "files": ["README.md", "LICENSE"]}
        pin = {"repository": proposal["repository"], "paths": proposal["files"],
               "commit_sha": "a" * 40, "license_spdx": "MIT", "repository_id": 7,
               "collected_at": "2026-10-21T00:00:00+00:00"}
        fixed_json(folder / "SOURCE_PIN.json", pin)
        files = {name: hashlib.sha256((local / name).read_bytes()).hexdigest()
                 for name in proposal["files"]}
        snapshot = {
            "repository": proposal["repository"], "commit_sha": "a" * 40,
            "local_root": str(alias / "p/leaf-0/attempt-1"),
            "strategy_version": "full-leaf-selected-v2-" + digest(proposal["files"])[:16],
            "collected_at": pin["collected_at"], "files": files,
            "license_files": ["LICENSE"],
            "license": {"status": "located", "spdx_id": "MIT",
                        "notice_hashes": {"LICENSE": files["LICENSE"]}},
            "license_uncertainties": ["Design reference only; no source code copied; file-level exceptions not exhaustively audited."],
            "excluded_paths": ["Unselected files; upstream not installed or run"],
        }
        fixed_json(folder / "source-snapshot.json", snapshot)
        original_snapshot = (folder / "source-snapshot.json").read_bytes()
        result = pin_sources(
            proposal, folder, SimpleNamespace(root=store_root), namespace="p",
            fetch=lambda *_args: self.fail("an existing snapshot must not fetch"),
        )
        self.assertEqual(result, snapshot)
        self.assertEqual((folder / "source-snapshot.json").read_bytes(), original_snapshot)

    def test_pin_sources_rejects_tampered_existing_snapshot_metadata_and_path(self):
        import hashlib
        mutations = (
            ("license", lambda value: value["license"].update(spdx_id="Apache-2.0")),
            ("strategy_version", lambda value: value.update(strategy_version="changed")),
            ("collected_at", lambda value: value.update(collected_at="changed")),
            ("license_files", lambda value: value.update(license_files=[])),
            ("notice_hashes", lambda value: value["license"]["notice_hashes"].update(LICENSE="0" * 64)),
            ("local_root", lambda value: value.update(local_root="/missing/fixed-source")),
        )
        for label, mutate in mutations:
            with self.subTest(field=label), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                state, external = root / "state", root / "external"
                state.mkdir()
                external.mkdir()
                (state / "sources").symlink_to(external, target_is_directory=True)
                folder = root / "items/leaf-0/attempt-1"
                folder.mkdir(parents=True)
                local = external / "p/leaf-0/attempt-1"
                local.mkdir(parents=True)
                (local / "README.md").write_bytes(b"readme\n")
                (local / "LICENSE").write_bytes(b"MIT\n")
                proposal = {"repository": "https://github.com/example/repo", "files": ["README.md", "LICENSE"]}
                pin = {"repository": proposal["repository"], "paths": proposal["files"],
                       "commit_sha": "a" * 40, "license_spdx": "MIT", "repository_id": 7,
                       "collected_at": "2026-10-21T00:00:00+00:00"}
                fixed_json(folder / "SOURCE_PIN.json", pin)
                files = {name: hashlib.sha256((local / name).read_bytes()).hexdigest()
                         for name in proposal["files"]}
                snapshot = {
                    "repository": proposal["repository"], "commit_sha": pin["commit_sha"],
                    "strategy_version": "full-leaf-selected-v2-" + digest(proposal["files"])[:16],
                    "collected_at": pin["collected_at"], "local_root": str(state / "sources/p/leaf-0/attempt-1"),
                    "files": files, "license_files": ["LICENSE"],
                    "license": {"status": "located", "spdx_id": "MIT", "notice_hashes": {"LICENSE": files["LICENSE"]}},
                    "license_uncertainties": ["Design reference only; no source code copied; file-level exceptions not exhaustively audited."],
                    "excluded_paths": ["Unselected files; upstream not installed or run"],
                }
                mutate(snapshot)
                fixed_json(folder / "source-snapshot.json", snapshot)
                with self.assertRaises(FactoryError) as caught:
                    pin_sources(proposal, folder, SimpleNamespace(root=state), namespace="p",
                                fetch=lambda *_args: self.fail("snapshot validation must not fetch"))
                self.assertEqual(caught.exception.code, "workflow_integrity")

    def test_pin_sources_refuses_broken_storage_alias_without_local_fallback(self):
        store_root = self.root / "state"
        store_root.mkdir()
        (store_root / "sources").symlink_to(self.root / "missing-external", target_is_directory=True)
        folder = self.root / "items/leaf-0/attempt-1"
        folder.mkdir(parents=True)
        with self.assertRaises(FactoryError) as caught:
            pin_sources(
                {"repository": "https://github.com/example/repo", "files": ["README.md", "LICENSE"]},
                folder, SimpleNamespace(root=store_root), namespace="p",
                fetch=lambda *_args: self.fail("broken storage must stop before network"),
            )
        self.assertEqual(caught.exception.code, "source_storage_unavailable")
        self.assertTrue((store_root / "sources").is_symlink())

    def test_failed_latest_review_cannot_be_bypassed_by_the_legacy_batch_entry(self):
        fixed_json(self.root / "SUPPLEMENTAL_FAILURE.json", {"status": "needs_changes"})
        with self.assertRaisesRegex(ValueError, "do not register/re-export as usable"):
            verify_production(self.root, {}, {}, {})

    def test_audit_snapshot_preserves_evidence_without_embedded_git_or_source(self):
        stage = self.root / "calls/stage"
        (stage / ".git").mkdir(parents=True)
        (stage / ".git/config").write_text("private workspace metadata")
        (stage / "source").mkdir()
        (stage / "source/example").write_text("source bytes separately archived")
        fixed_json(stage / "RESULT.json", {"result": 1})
        snapshot_audit(stage)
        audit = self.root / "audit/stage"
        self.assertEqual((audit / "RESULT.json").read_bytes(), (stage / "RESULT.json").read_bytes())
        self.assertFalse((audit / ".git").exists())
        self.assertFalse((audit / "source").exists())
        self.assertEqual(set(json.loads((audit / "FILES.json").read_text())), {"RESULT.json"})

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
        stage = self.root / "calls/stage"
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
