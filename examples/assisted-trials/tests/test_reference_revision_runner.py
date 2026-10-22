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
    def test_read_proof_recovery_is_zero_call_and_preserves_original_failure(self):
        from unittest.mock import Mock
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            old, new = root / "old", root / "new"
            sample, folder = old / "bookmark-manager", new / "bookmark-manager/r4"
            sample.mkdir(parents=True)
            folder.mkdir(parents=True)
            for filename in ("INPUTS.json", "SNAPSHOT.json"):
                (sample / filename).write_text("{}")
            binding = {"leaf": "bookmark-manager", "input_path": "old/bookmark-manager/INPUTS.json",
                       "snapshot_path": "old/bookmark-manager/SNAPSHOT.json",
                       "input_sha256": runner.sha(sample / "INPUTS.json"),
                       "snapshot_sha256": runner.sha(sample / "SNAPSHOT.json")}
            (old / "REGISTER_REQUEST.json").write_text(json.dumps({"leaves": [binding]}))
            request = {"parents": {"author": {"path": "new/bookmark-manager/r3/generation/author/RESULT.json",
                                               "sha256": "a" * 64}}}
            (folder / "REQUEST.json").write_text(json.dumps(request))
            failure = {"status": "failed", "error_type": "ValueError",
                       "reason": "review lacks actual completed full-content read coverage for readable/REVIEW_STRUCTURE.json"}
            (folder / "OUTCOME.json").write_text(json.dumps(failure))
            original_failure = (folder / "OUTCOME.json").read_bytes()
            for stage in ("research", "author", "review"):
                stage_dir = folder / "generation" / stage
                stage_dir.mkdir(parents=True)
                for filename in ("BINDING.json", "DELIVERED.json", "RESULT.json"):
                    (stage_dir / filename).write_text(json.dumps({"verdict": "pass"}))
            package = folder / "generation/reference.zip"
            package.write_bytes(b"fixture archive")
            (folder / "generation/READ_COVERAGE_PROOF.json").write_text("{}")
            state = {"status": "paused", "active_calls": 0, "new_calls": 182}
            full = SimpleNamespace(status=lambda _: state,
                                   host_revision=lambda _: {"new_host_sha256": {"old/bookmark-manager/INPUTS.json": binding["input_sha256"]}})
            pilot = Mock()
            pilot.get_revision.return_value = {"request": request}
            pilot.get.return_value = {"calls": [{"id": "fixed-call", "status": "completed"}]}
            catalog = Mock()
            catalog.import_reference.return_value = {"id": "ref_fixture"}

            def replay(*args):
                with self.assertRaisesRegex(RuntimeError, "cannot launch"):
                    args[-1]("review", {}, "", {})
                return {"status": "static_review_passed", "reference_zip": str(package)}

            with patch.object(runner, "ROOT", root), patch.object(runner, "PARENT", old), patch.object(runner, "DIRECTORY", new), \
                    patch.object(runner, "host", return_value=(object(), full)), \
                    patch.object(runner, "ReferencePilotService", return_value=pilot), \
                    patch.object(runner.profile, "revise", side_effect=replay) as revise, \
                    patch("template_factory.reference_catalog.ReferenceCatalog", return_value=catalog):
                first = runner.recover_read_proof("bookmark-manager", "r4")
                self.assertEqual(first, runner.recover_read_proof("bookmark-manager", "r4"))
                self.assertEqual(first["model_calls_added"], 0)
                self.assertEqual(first["ledger_before"], first["ledger_after"])
                self.assertEqual((folder / "OUTCOME.json").read_bytes(), original_failure)
                recovery_path = folder / "RECOVERY_OUTCOME.json"
                original_recovery_bytes = recovery_path.read_bytes()
                self.assertEqual(first["ledger_before"]["new_calls"], 182)
                self.assertEqual(list(folder.glob("RECOVERY_REPLAY.*.json")), [])
                # Same ledger snapshot remains a replay of the original receipt.
                self.assertEqual(runner.recover_read_proof("bookmark-manager", "r4"), first)
                self.assertEqual(recovery_path.read_bytes(), original_recovery_bytes)
                self.assertEqual(list(folder.glob("RECOVERY_REPLAY.*.json")), [])
                # A legitimate call for another leaf advances the shared ledger.
                # It must not rewrite the earlier replay's evidence or make its
                # idempotent retry compare against a stale global ledger snapshot.
                state["new_calls"] += 2
                pilot.get.return_value = {"calls": [
                    {"id": "fixed-call", "status": "completed"},
                    {"id": "other-leaf-call", "status": "completed"}]}
                replayed = runner.recover_read_proof("bookmark-manager", "r4")
                self.assertEqual(recovery_path.read_bytes(), original_recovery_bytes)
                replay_files = list(folder.glob("RECOVERY_REPLAY.*.json"))
                self.assertEqual(len(replay_files), 1)
                replay_evidence_path = replay_files[0]
                replay_evidence = json.loads(replay_evidence_path.read_text())
                self.assertEqual(replayed, replay_evidence)
                self.assertEqual(replay_evidence["ledger_before"], replay_evidence["ledger_after"])
                self.assertEqual(replay_evidence["ledger_before"]["new_calls"], 184)
                self.assertEqual(json.loads(original_recovery_bytes)["ledger_before"]["new_calls"], 182)
                self.assertEqual(replay_evidence["replay_of"], {
                    "path": str(recovery_path.relative_to(root)),
                    "sha256": runner.sha(recovery_path)})
                (folder / "generation/review/RESULT.json").write_text('{"verdict":"needs_changes"}')
                with self.assertRaisesRegex(ValueError, "content rejection"):
                    runner.recover_read_proof("bookmark-manager", "r4")
                self.assertEqual(revise.call_count, 4)
                (folder / "generation/review/DELIVERED.json").unlink()
                with self.assertRaisesRegex(ValueError, "all three durable"):
                    runner.recover_read_proof("bookmark-manager", "r4")
                self.assertEqual(catalog.import_reference.call_count, 4)

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
                prior = new / "bookmark-manager/r2"
                for stage in ("research", "author", "review"):
                    stage_dir = prior / "generation" / stage
                    stage_dir.mkdir(parents=True)
                    (stage_dir / "RESULT.json").write_text(json.dumps({"verdict": "needs_changes"}))
                    (stage_dir / "DELIVERED.json").write_text(json.dumps({"session_id": stage}))
                failure = {"status": "failed", "error_type": "ValueError",
                           "reason": "review lacks actual completed full-content read coverage for readable/source/upstream/docs.md",
                           "completed_stages": ["research", "author", "review"]}
                failure_bytes = json.dumps(failure).encode()
                (prior / "OUTCOME.json").write_bytes(failure_bytes)
                continuation = runner.prepare("bookmark-manager", "r3", "r2")
                self.assertEqual(continuation["parents"]["review"]["sha256"],
                                 runner.sha(prior / "generation/review/RESULT.json"))
                self.assertIn("review_receipt", continuation["parents"])
                self.assertEqual((prior / "OUTCOME.json").read_bytes(), failure_bytes)
                (new / "USER_REQUEST.txt").write_text("different request")
                with self.assertRaises(ValueError):
                    runner.prepare("bookmark-manager")
                with self.assertRaises(ValueError):
                    runner.prepare("unregistered-leaf")
            self.assertEqual(before, {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in old.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
