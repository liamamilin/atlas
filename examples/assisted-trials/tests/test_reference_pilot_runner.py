"""Checks for fixed-source reuse and ordinary-item failure isolation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
sys.path.insert(0, str(ROOT / "examples/assisted-trials"))
spec = importlib.util.spec_from_file_location("reference_pilot_runner", ROOT / "examples/assisted-trials/produce_reference_pilot.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
digest = runner.digest


class PilotRunnerTests(unittest.TestCase):
    def test_source_reuse_retains_unknown_license_and_rejects_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "cache"
            source.mkdir()
            (source / "README.md").write_text("fixed source\n")
            value = hashlib.sha256((source / "README.md").read_bytes()).hexdigest()
            original = {"repository": "https://github.com/o/r", "commit_sha": "a" * 40,
                        "files": {"README.md": value}, "license": {"status": "located"},
                        "license_files": ["README.md"]}
            sample = {"cache": "cache", "leaf": "one", "files": ["README.md"]}
            with patch.object(runner, "ROOT", root), patch.object(runner, "source_storage_root", return_value=root / "external"):
                snap = runner.reuse_text_sources(SimpleNamespace(root=root), original, sample)
                self.assertEqual(snap["license"], original["license"])
                self.assertEqual(snap["upstream_status"], "not_run")
                self.assertEqual(runner.reuse_text_sources(SimpleNamespace(root=root), original, sample), snap)
                (source / "README.md").write_text("changed source\n")
                with self.assertRaises(ValueError):
                    runner.reuse_text_sources(SimpleNamespace(root=root), original, sample)

    def test_content_failure_records_item_and_continues_other_sample(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            leaves = []
            for leaf in ("one", "two"):
                folder = root / leaf
                folder.mkdir()
                leaf_sha = hashlib.sha256(leaf.encode()).hexdigest()
                (folder / "INPUTS.json").write_text(json.dumps({"leaf": {"content_sha256": leaf_sha}}))
                (folder / "SNAPSHOT.json").write_text("{}")
                (folder / "leaf.md").write_text(leaf)
                leaves.append({"leaf": leaf, "frozen_leaf_sha256": leaf_sha,
                               "input_path": leaf + "/INPUTS.json", "snapshot_path": leaf + "/SNAPSHOT.json",
                               "input_sha256": runner.sha(folder / "INPUTS.json"),
                               "snapshot_sha256": runner.sha(folder / "SNAPSHOT.json")})
            manifest = {"leaves": leaves, "profile_version": runner.VERSION, "prompt_digest": runner.PROMPT_DIGEST, "model": runner.MODEL}
            (root / "MANIFEST.json").write_text(json.dumps(manifest))
            (root / "REGISTER_REQUEST.json").write_text(json.dumps(manifest))
            full = SimpleNamespace(ledger=object(), status=lambda _: {"phase": "original-phase", "status": "paused", "new_calls": 4, "active_calls": 0, "deadline": 10})
            pilot = unittest.mock.Mock()
            pilot.get.return_value = {"status": "active", "request_digest": digest(manifest)}
            with patch.object(runner, "ROOT", root), patch.object(runner, "DIRECTORY", root), \
                    patch.object(runner, "host", return_value=(object(), full)), \
                    patch.object(runner, "ReferencePilotService", return_value=pilot), \
                    patch.object(runner, "OfficialCheckpointAdapter"), patch.object(runner, "CLI"), \
                    patch.object(runner, "generate", side_effect=[ValueError("bad contract"), {"status": "needs_changes", "reference": {}, "reference_zip": None}]) as generate:
                result = runner.run()
            self.assertEqual(generate.call_count, 2)
            self.assertEqual([x["status"] for x in result["outcomes"]], ["failed", "needs_changes"])
            self.assertEqual(result["full_plan"]["status"], "paused")
            pilot.action.assert_called_once_with(runner.PILOT, "complete", reason="bounded validation reached terminal outcomes")
            (root / "one/leaf.md").write_text("different leaf")
            with patch.object(runner, "ROOT", root), patch.object(runner, "DIRECTORY", root), self.assertRaises(ValueError):
                runner.verify_run_bindings(manifest, manifest, {"request_digest": digest(manifest)})
            altered = {**manifest, "leaves": list(reversed(leaves))}
            with patch.object(runner, "ROOT", root), patch.object(runner, "DIRECTORY", root), self.assertRaises(ValueError):
                runner.verify_run_bindings(altered, manifest, {"request_digest": digest(manifest)})


if __name__ == "__main__":
    unittest.main()
