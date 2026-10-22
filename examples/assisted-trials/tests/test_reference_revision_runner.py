"""Revision preparation does not overwrite or change the original sample inputs."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
sys.path.insert(0, str(ROOT / "examples/assisted-trials"))
import produce_reference_revision as runner  # noqa: E402


class RevisionRunnerTests(unittest.TestCase):
    def test_same_run_replays_registration_and_recovers_import(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old, new = root / "old", root / "new"
            sample = old / "bookmark-manager"
            sample.mkdir(parents=True)
            folder = new / "bookmark-manager/r2"
            folder.mkdir(parents=True)
            (sample / "INPUTS.json").write_text("{}")
            (sample / "SNAPSHOT.json").write_text("{}")
            (sample / "leaf.md").write_text("fixed leaf")
            (folder / "REQUEST.json").write_text(json.dumps({"parents": {"author": {"path": "old/bookmark-manager/generation/author/RESULT.json", "sha256": "a" * 64}}}))
            (old / "REGISTER_REQUEST.json").write_text(json.dumps({"leaves": [{"leaf": "bookmark-manager", "input_path": "old/bookmark-manager/INPUTS.json", "snapshot_path": "old/bookmark-manager/SNAPSHOT.json"}]}))
            package = folder / "reference.zip"
            package.write_bytes(b"fixture-only archive")
            state = {"phase": "fixed-phase", "status": "paused", "active_calls": 0}
            full = SimpleNamespace(status=lambda _: state, ledger=object())
            from unittest.mock import Mock
            pilot = Mock()
            stable = {"pilot_id": runner.PILOT, "revision_digest": "b" * 64, "status": "registered"}
            pilot.begin_revision.side_effect = [{**stable, "idempotent": False, "receipt_only": False},
                                                 {**stable, "idempotent": True, "receipt_only": True}]
            catalog = Mock()
            catalog.import_reference.side_effect = [ValueError("fixture interrupted import"), {"id": "ref_fixture"}]
            generated = {"status": "static_review_passed", "reference": {}, "reference_zip": str(package)}
            with patch.object(runner, "ROOT", root), patch.object(runner, "PARENT", old), patch.object(runner, "DIRECTORY", new), \
                    patch.object(runner, "host", return_value=(object(), full)), \
                    patch.object(runner, "ReferencePilotService", return_value=pilot), \
                    patch.object(runner.profile, "OfficialCheckpointAdapter"), \
                    patch.object(runner.profile, "revise", return_value=generated), \
                    patch("template_factory.reference_catalog.ReferenceCatalog", return_value=catalog):
                with self.assertRaisesRegex(ValueError, "interrupted import"):
                    runner.run_one("bookmark-manager")
                first = json.loads((folder / "OUTCOME.json").read_text())
                self.assertEqual(runner.run_one("bookmark-manager"), first)
            self.assertEqual(json.loads((folder / "REGISTER_RECEIPT.json").read_text()), stable)
            self.assertEqual(catalog.import_reference.call_count, 2)
            self.assertEqual(len(list(folder.glob("IMPORT_FAILURE.*.json"))), 1)
            self.assertEqual(json.loads((folder / "IMPORT_RECEIPT.json").read_text())["id"], "ref_fixture")

    def test_prepare_binds_prior_deliveries_and_is_idempotent_without_starting(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old, new = root / "old", root / "new"
            old.mkdir()
            new.mkdir()
            (old / "REGISTER_RECEIPT.json").write_text(json.dumps({"request_digest": "a" * 64}))
            original = {"leaves": [{"leaf": "bookmark-manager", "input_sha256": "b" * 64,
                                    "snapshot_sha256": "c" * 64}]}
            (old / "REGISTER_REQUEST.json").write_text(json.dumps(original))
            (new / "USER_REQUEST.txt").write_text("Continue both samples, full plan stays paused")
            (new / "HOST_REVISION.json").write_text(json.dumps({"code_sha": "d" * 40}))
            profile_source = root / "examples/assisted-trials/product_reference_profile.py"
            profile_source.parent.mkdir(parents=True)
            profile_source.write_text("fixed profile")
            parent = old / "bookmark-manager"
            for stage in ("research", "author"):
                folder = parent / "generation" / stage
                folder.mkdir(parents=True)
                (folder / "RESULT.json").write_text(json.dumps({"stage": stage}))
                (folder / "DELIVERED.json").write_text(json.dumps({"session_id": "previous-" + stage}))
            (parent / "OUTCOME.json").write_text(json.dumps({"status": "failed"}))
            before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in old.rglob("*") if p.is_file()}
            with patch.object(runner, "ROOT", root), patch.object(runner, "PARENT", old), patch.object(runner, "DIRECTORY", new):
                first = runner.prepare("bookmark-manager")
                self.assertEqual(first, runner.prepare("bookmark-manager"))
                self.assertEqual(first["parents"]["author"]["path"], "old/bookmark-manager/generation/author/RESULT.json")
                (new / "USER_REQUEST.txt").write_text("different request")
                with self.assertRaises(ValueError):
                    runner.prepare("bookmark-manager")
                with self.assertRaises(ValueError):
                    runner.prepare("unregistered-leaf")
            self.assertEqual(before, {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in old.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
