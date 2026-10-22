"""Host-only integration fixtures for execute_leaf workflow recovery."""

import hashlib
import io
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import produce_all_leaves as runner
from template_factory.auxiliary_workflow import STEPS, WorkflowService
from template_factory.full_auxiliary import FullAuxiliaryService, MODEL
from template_factory.cases import CaseLibrary
from template_factory.store import FactoryStore


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True))


class WorkflowRunnerHostTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        (self.pack / "applications").mkdir()
        self.leaf = "fixture-workflow"
        leaf_file = self.pack / "applications" / (self.leaf + ".md")
        leaf_file.write_text("fixture application source\n")
        self.item = {
            "leaf": self.leaf,
            "leaf_sha256": hashlib.sha256(leaf_file.read_bytes()).hexdigest(),
            "display_name": "Fixture workflow",
            "covered": [],
        }
        self.scope_path = self.root / "scope.json"
        write_json(self.scope_path, {"full_plan_id": "host-fixture", "items": [self.item]})
        auth = self.root / "authorization.txt"
        auth.write_text("fixture only")
        self.request = {
            "schema": "atlas.full-leaf-auxiliary-authorization.v1",
            "full_plan_id": "host-fixture",
            "campaign_id": "workflow-host-fixture",
            "phase": "auxiliary-full-host-fixture",
            "baseline": 0,
            "max_new_calls": 7200,
            "per_leaf_calls": 6,
            "concurrency": 2,
            "batch_size": 20,
            "window_seconds": 2592000,
            "model": MODEL,
            "scope": {"path": "scope.json", "sha256": runner.sha(self.scope_path)},
            "authorization": {
                "path": "authorization.txt",
                "sha256": runner.sha(auth),
            },
        }
        self.store = FactoryStore(self.pack / "state", self.pack)
        self.service = FullAuxiliaryService(self.store, "workflow-host-fixture", lambda: 1000.0)
        self.service.register(self.request)
        self.service.control("host-fixture", "resume")
        self.work = self.root / "items" / self.leaf / "attempt-1"
        self.provider_calls = []

    def _patches(
        self,
        produce_stub,
        verify_stub=None,
        *,
        real_author_stage=False,
        stage_error=None,
        research_result=None,
        compatible_cases=None,
    ):
        real_stage_call = runner.stage_call
        snapshot_root = self.root / "pinned-source"
        source_file = snapshot_root / "README.md"
        source_file.parent.mkdir(parents=True, exist_ok=True)
        source_file.write_text("pinned fixture source\n")
        license_file = snapshot_root / "LICENSE"
        license_file.write_text("fixture license\n")
        snapshot = {
            "repository": "https://github.com/fixture/example",
            "commit_sha": "a" * 40,
            "files": {
                "README.md": runner.sha(source_file),
                "LICENSE": runner.sha(license_file),
            },
            "local_root": str(snapshot_root),
        }
        self.pin_calls = []

        def fake_stage(_root, service, item, work, stage, *_args, lane="first", **_kwargs):
            paths_file = work / "STAGE_PATHS.json"
            paths = json.loads(paths_file.read_text()) if paths_file.exists() else {}
            relative = paths.setdefault(stage, "calls/" + stage)
            write_json(paths_file, paths)
            target = work / relative
            target.mkdir(parents=True, exist_ok=True)
            if stage_error is not None and stage == "blueprint-generate-aux":
                raise stage_error()
            if real_author_stage and stage == "blueprint-generate-aux":
                write_json(work / "PROTOCOL_SUCCESSOR.json", {
                    "parent_path": "calls/blueprint-spec-review-aux",
                    "reason": "one protocol recovery already used",
                })
                return real_stage_call(
                    _root, service, item, work, stage, *_args, lane=lane, **_kwargs
                )
            if (target / "RESULT.json").exists():
                return json.loads((target / "RESULT.json").read_text())
            self.provider_calls.append(stage)
            reservation = service.ledger.reserve(
                "host-fixture:" + item["leaf"],
                "auxiliary-full-host-fixture",
                requested_model=MODEL,
                plan_id="host-fixture",
                job_id="host-fixture:" + item["leaf"] + ":" + work.name,
                stage=lane + "/" + stage + "/" + work.name,
                kind="review" if "review" in stage else ("research" if stage == "discovery" else "production"),
            )
            if stage == "discovery":
                value = research_result or {
                    "repository": snapshot["repository"],
                    "files": ["README.md", "LICENSE"],
                    "rationale": "fixture research",
                    "reuse_case_id": None,
                    "delivery_profile": "web",
                    "scenario": {
                        "name": "Fixture scenario",
                        "audience": "Fixture user",
                        "objective": "Complete the fixture workflow",
                        "workflow": ["Start", "Complete"],
                        "acceptance": ["Completion is visible"],
                    },
                }
            elif stage == "blueprint-generate-aux":
                value = {"fixture": "generated candidate"}
            else:
                value = {
                    "verdict": "passed",
                    "input_digest": "fixture",
                    "checks": {"source_fidelity": True},
                    "observations": [],
                }
            write_json(target / "RESULT.json", value)
            write_json(target / "BINDING.json", {"model": MODEL})
            write_json(target / "cli-summary.json", {
                "session_id": "session-" + stage,
                "requested_model": MODEL,
                "delivery_status": "delivered",
            })
            service.ledger.finish(reservation["id"], "completed")
            return value

        def save_receipt(_service, _item, work, *_args, **_kwargs):
            receipt = work / "ACCEPTED_RESEARCH_RECEIPT.json"
            if not receipt.exists():
                write_json(receipt, {"fixture": "accepted research preserved"})

        def save_snapshot(research, work, _store, **_kwargs):
            self.pin_calls.append(research)
            write_json(work / "source-snapshot.json", snapshot)
            return snapshot

        class FixtureCaseLibrary:
            def __init__(self, _store):
                pass

            @staticmethod
            def list_cases():
                return compatible_cases or []

        stack = [
            patch.object(runner, "ROOT", self.root),
            patch.object(runner, "PLAN_ID", "host-fixture"),
            patch.object(runner, "verify_plan"),
            patch.object(runner, "get_bytes", return_value=b'{"items": []}'),
            patch.object(runner, "stage_call", side_effect=fake_stage),
            patch.object(runner, "pin_sources", side_effect=save_snapshot),
            patch.object(runner.profiles, "validate_research"),
            patch.object(
                runner.profiles,
                "validate_author",
                return_value=(
                    {
                        "name": "Fixture template",
                        "audience": "Fixture user",
                        "objective": "Complete the fixture workflow",
                        "workflow": ["Start", "Complete"],
                        "acceptance": ["Completion is visible"],
                        "observations": [],
                    },
                    {"README.md": "fixture acceptance notes"},
                ),
            ),
            patch.object(runner.profiles, "source_ids", return_value={}),
            patch.object(runner, "readable_candidate", return_value={}),
            patch.object(runner, "validate_read_coverage"),
            patch.object(runner, "validate_review"),
            patch.object(runner, "save_accepted_research", side_effect=save_receipt),
            patch.object(runner, "register_catalog"),
            patch.object(runner, "CaseLibrary", FixtureCaseLibrary),
            patch.object(runner, "produce", side_effect=produce_stub),
        ]
        if verify_stub:
            stack.append(patch.object(runner, "verify_download", side_effect=verify_stub))
        for mocked in stack:
            mocked.start()
            self.addCleanup(mocked.stop)

    def execute(self):
        current = self.service.status("host-fixture")["items"][0]
        return runner.execute_leaf(self.root, self.service, current, "https://fixture.invalid")

    def test_leaf_delivery_failure_isolated_and_reentry_reuses_completed_work(self):
        produced = []

        def produce_stub(*_args):
            produced.append(1)
            if len(produced) == 1:
                raise runner.FactoryError(
                    "item generation delivery was rejected", "leaf_delivery_error", 409
                )
            write_json(self.work / "IMPORT_RECEIPT.json", {
                "artifact_id": "artifact-fixture", "case_id": "case-fixture", "case_revision": 1,
                "case_ref": {"case_id": "case-fixture", "revision": 1, "digest": "d" * 64},
                "digest": "e" * 64,
                "exported_zip_sha256": "f" * 64,
                "export": {"download_url": "/download"},
            })
            for p in (self.work / "packages" / "template-snapshot.zip", self.work / "atlas-development-package.zip"):
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(b"fixture package")
            return {"artifact_id": "artifact-fixture", "case_id": "case-fixture", "case_revision": 1, "url": "/api/factory/artifacts/artifact-fixture"}

        def verify_stub(work, _api):
            write_json(work / "DOWNLOAD_VERIFIED.json", {"application_runtime": "not_run"})
            return {"application_runtime": "not_run"}

        self._patches(produce_stub, verify_stub)
        first = self.execute()
        self.assertEqual(first["state"], "failed")
        state = self.service.status("host-fixture")
        self.assertEqual(state["status"], "running")
        self.assertEqual(state["items"][0]["state"], "failed", json.dumps(state, indent=2))
        self.assertEqual(state["new_calls"], 3, json.dumps(state, indent=2))
        progress = WorkflowService(self.store, "workflow-host-fixture").detail("host-fixture")
        self.assertEqual([x["step"] for x in progress["items"][0]["steps"]], list(STEPS))
        self.assertTrue(all(x["state"] == "completed" for x in progress["items"][0]["steps"][:6]))
        self.assertEqual(progress["items"][0]["steps"][6]["state"], "failed")
        self.assertEqual(progress["items"][0]["steps"][7]["state"], "pending")
        accepted_receipt = (self.work / "ACCEPTED_RESEARCH_RECEIPT.json").read_bytes()

        self.service.control("host-fixture", "resume")
        second = self.execute()
        self.assertEqual(second["state"], "ready_not_run")
        after = self.service.status("host-fixture")
        self.assertEqual(after["items"][0]["state"], "ready_not_run")
        self.assertEqual(after["new_calls"], 3)
        self.assertEqual(self.provider_calls.count("discovery"), 1)
        self.assertEqual(self.provider_calls.count("blueprint-generate-aux"), 1)
        self.assertEqual(self.provider_calls.count("blueprint-spec-review-aux"), 1)
        self.assertTrue((self.work / "ACCEPTED_RESEARCH_RECEIPT.json").exists())
        self.assertEqual((self.work / "ACCEPTED_RESEARCH_RECEIPT.json").read_bytes(), accepted_receipt)
        completed = WorkflowService(self.store, "workflow-host-fixture").detail("host-fixture")
        self.assertEqual([x["step"] for x in completed["items"][0]["steps"]], list(STEPS))
        self.assertTrue(all(x["state"] == "completed" for x in completed["items"][0]["steps"]))

    def test_database_failure_still_pauses_production(self):
        import sqlite3
        def corrupt(*_args):
            raise sqlite3.DatabaseError("fixture database corruption")
        self._patches(corrupt)
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        self.assertEqual(self.service.status("host-fixture")["status"], "paused")

    def test_unknown_generation_host_error_pauses_instead_of_isolating_leaf(self):
        def unknown_host_failure(*_args):
            raise RuntimeError("unexpected host defect")

        self._patches(unknown_host_failure)
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        self.assertEqual(result["code"], "workflow_host_error")
        self.assertEqual(self.service.status("host-fixture")["status"], "paused")

    def test_later_full_plan_paused_error_does_not_replace_primary_pause_reason(self):
        self._patches(lambda *_args: self.fail("secondary worker must not reach production"))
        primary = "full_plan_integrity: frozen source changed"
        self.service.control("host-fixture", "pause", primary)

        def peer_observes_pause(*_args, **_kwargs):
            raise runner.FactoryError("plan already paused", "full_plan_paused", 409)

        with patch.object(runner, "stage_call", side_effect=peer_observes_pause), patch.object(
            self.service, "pause_if_running", wraps=self.service.pause_if_running
        ) as pause_if_running:
            result = self.execute()

        self.assertEqual(result, {"leaf": self.leaf, "state": "paused", "code": "full_plan_paused"})
        self.assertEqual(self.service.status("host-fixture")["reason"], primary)
        pause_if_running.assert_called_once_with(
            "host-fixture", "full_plan_paused: plan already paused"
        )

    def test_exhausted_protocol_retry_is_leaf_failure_and_keeps_plan_running(self):
        self._patches(lambda *_args: self.fail("generation retry must remain exhausted"), real_author_stage=True)

        class FailedProtocolCLI:
            def run(inner, directory, _prompt, model, _timeout, _cancelled, _progress, **kwargs):
                budget = kwargs["budget"]
                reservation = budget["ledger"].reserve(
                    budget["identity"], budget["phase"], budget["kind"],
                    job_id=budget["job_id"], requested_model=model,
                    plan_id=budget["plan_id"], stage=budget["stage"],
                )
                budget["ledger"].finish(reservation["id"], "failed", outcome="cli_protocol")
                write_json(Path(directory) / "cli-summary.json", {
                    "requested_model": model,
                    "delivery_status": "failed",
                    "failure_code": "cli_protocol",
                    "output_observed": True,
                })
                write_json(Path(directory) / "original-response.json", {"text": "not-json"})
                raise runner.FactoryError("mock protocol failure", "cli_protocol", 409)

        with patch.object(runner, "CoordinatedCLI", return_value=FailedProtocolCLI()):
            result = self.execute()

        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "budget_retry_limit")
        status = self.service.status("host-fixture")
        self.assertEqual(status["status"], "running")
        self.assertEqual(status["items"][0]["state"], "failed")
        self.assertEqual(status["new_calls"], 2)
        retry_summary = self.work / "calls/blueprint-generate-aux/cli-summary.json"
        self.assertEqual(json.loads(retry_summary.read_text())["failure_code"], "cli_protocol")

    def test_first_pass_protocol_reserve_deferral_marks_leaf_done_without_pausing_plan(self):
        self._patches(
            lambda *_args: self.fail("budget deferral must precede the provider"),
            stage_error=lambda: runner.FactoryError(
                "preserve pending first-pass allowance", "budget_first_pass_reserve", 409
            ),
        )
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        status = self.service.status("host-fixture")
        self.assertEqual(status["status"], "running")
        self.assertEqual(status["items"][0]["first_pass_done"], True)
        self.assertEqual(
            status["items"][0]["deferred_reason"],
            "preserve pending first-pass allowance",
        )
        self.assertEqual(status["new_calls"], 1)

    def test_repair_budget_reserve_deferral_retains_needs_revision_without_retry(self):
        self._patches(
            lambda *_args: self.fail("budget deferral must precede the provider"),
            stage_error=lambda: runner.FactoryError(
                "preserve pending first-pass allowance", "budget_first_pass_reserve", 409
            ),
        )
        previous = self.root / "items" / self.leaf / "attempt-1"
        previous.mkdir(parents=True)
        scenario = {
            "name": "Fixture scenario",
            "audience": "Fixture user",
            "objective": "Complete the fixture workflow",
            "workflow": ["Start", "Complete"],
            "acceptance": ["Completion is visible"],
        }
        write_json(previous / "SELECTED_SCENARIO.json", scenario)
        write_json(previous / "RESEARCH.json", {
            "repository": "https://github.com/fixture/example",
            "files": ["README.md", "LICENSE"],
            "rationale": "fixed research",
            "reuse_case_id": None,
            "delivery_profile": "web",
            "scenario": scenario,
        })
        source_root = self.root / "pinned-source"
        source_file = source_root / "README.md"
        source_file.parent.mkdir(parents=True, exist_ok=True)
        source_file.write_text("pinned fixture source\n")
        license_file = source_root / "LICENSE"
        license_file.write_text("fixture license\n")
        write_json(previous / "source-snapshot.json", {
            "repository": "https://github.com/fixture/example",
            "commit_sha": "a" * 40,
            "files": {
                "README.md": runner.sha(source_file),
                "LICENSE": runner.sha(license_file),
            },
            "local_root": str(source_root),
        })
        write_json(previous / "LATEST_FAILURE.json", {"error": "prior review"})
        write_json(previous / "STAGE_PATHS.json", {
            "blueprint-spec-review-aux": "calls/blueprint-spec-review-aux",
        })
        self.service.update_leaf("host-fixture", self.leaf, "needs_revision", {
            "first_pass_done": True,
            "repair_pending": True,
            "current_attempt": "attempt-1",
            "workdir": str(previous.relative_to(self.root)),
        })
        current = self.service.status("host-fixture")["items"][0]
        result = runner.execute_leaf(self.root, self.service, current, "https://fixture.invalid", repair=True)

        self.assertEqual(
            result["state"],
            "needs_revision",
            json.dumps({"result": result, "failure": json.loads((self.work.parent / "attempt-2" / "LATEST_FAILURE.json").read_text())}),
        )
        status = self.service.status("host-fixture")
        self.assertEqual(status["status"], "running")
        self.assertEqual(status["items"][0]["state"], "needs_revision")
        self.assertFalse(status["items"][0]["repair_pending"])
        self.assertEqual(status["items"][0]["deferred_reason"], "preserve pending first-pass allowance")
        self.assertTrue(status["items"][0]["first_pass_done"])

    def test_tampered_request_binding_pauses_before_any_provider_call(self):
        self._patches(lambda *_args: self.fail("tampered request must stop before generation"))
        write_json(self.work / "REQUEST.json", {
            "leaf": self.leaf,
            "leaf_sha256": "0" * 64,
            "full_plan_id": "host-fixture",
            "profile": runner.profiles.VERSION,
            "model": MODEL,
        })
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        self.assertEqual(result["code"], "full_plan_integrity")
        self.assertEqual(self.provider_calls, [])
        self.assertEqual(self.service.status("host-fixture")["status"], "paused")

    def test_source_inventory_mismatch_pauses_workflow(self):
        self._patches(lambda *_args: self.fail("source inventory mismatch must stop before generation"))
        original_manifest = runner.manifest_files

        def mismatched_manifest(path):
            if Path(path).name == "upstream":
                return {"unexpected.txt": "0" * 64}
            return original_manifest(path)

        with patch.object(runner, "manifest_files", side_effect=mismatched_manifest):
            result = self.execute()
        self.assertEqual(result["state"], "paused")
        self.assertEqual(result["code"], "workflow_integrity")
        self.assertEqual(self.service.status("host-fixture")["status"], "paused")

    def _reuse_inputs(self, *, repo="https://github.com/TokTok/c-toxcore", files=None,
                     snapshot_repo="https://github.com/toktok/c-toxcore", snapshot_files=None):
        files = files or ["README.md", "LICENSE"]
        snapshot_files = snapshot_files or files
        selected = {
            "repository": repo,
            "files": files,
            "rationale": "reuse fixture",
            "reuse_case_id": "case-reuse",
            "delivery_profile": "web",
            "scenario": {
                "name": "Fixture scenario", "audience": "Fixture user",
                "objective": "Complete the fixture workflow",
                "workflow": ["Start", "Complete"],
                "acceptance": ["Completion is visible"],
            },
        }
        content = {"README.md": b"fixed source\n", "LICENSE": b"MIT license\n"}
        snapshot = {
            "repository": snapshot_repo, "commit_sha": "a" * 40,
            "files": {name: hashlib.sha256(content[name]).hexdigest() for name in snapshot_files},
            "license": {"spdx_id": "MIT"}, "license_files": ["LICENSE"],
        }
        case = {
            "case_id": "case-reuse", "revision": 3, "digest": "b" * 64,
            "research": {"summary": "fixture case"},
            "scenario_links": [{"leaf": self.leaf}], "source_snapshots": [snapshot],
        }
        cache = self.store.root / "sources" / "host-fixture" / self.leaf / "attempt-1"
        cache.mkdir(parents=True, exist_ok=True)
        for name in snapshot_files:
            (cache / name).write_bytes(content[name])
        return selected, case, cache

    def test_reuse_accepts_casefolded_github_host_identity_and_keeps_fixed_commit(self):
        selected, case, cache = self._reuse_inputs()
        self._patches(
            lambda *_args: self.fail("content stage is intentionally stopped"),
            stage_error=lambda: runner.FactoryError("fixture stop", "auxiliary_content", 409),
            research_result=selected, compatible_cases=[case],
        )
        result = self.execute()
        self.assertEqual(result["state"], "needs_revision")
        self.assertEqual(self.pin_calls, [])
        self.assertEqual(json.loads((self.work / "RESEARCH.json").read_text()), selected)
        snapshot = json.loads((self.work / "source-snapshot.json").read_text())
        self.assertEqual(snapshot["repository"], case["source_snapshots"][0]["repository"])
        self.assertEqual(snapshot["commit_sha"], "a" * 40)
        self.assertEqual(snapshot["files"], case["source_snapshots"][0]["files"])
        self.assertTrue((cache / "README.md").exists())

    def test_wrong_reuse_files_fail_locally_without_pin_or_global_pause(self):
        selected, case, _cache = self._reuse_inputs(
            files=["README.md", "COPYING"], snapshot_files=["README.md", "LICENSE"]
        )
        self._patches(
            lambda *_args: self.fail("invalid source selection must stop before authoring"),
            research_result=selected, compatible_cases=[case],
        )
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        status = self.service.status("host-fixture")
        self.assertEqual(status["status"], "running")
        self.assertTrue(status["items"][0]["first_pass_done"])
        self.assertFalse(status["items"][0]["repair_pending"])
        self.assertEqual(self.pin_calls, [])

    def test_missing_reuse_case_fails_locally_without_pin(self):
        selected, case, _cache = self._reuse_inputs()
        selected["reuse_case_id"] = "missing-case"
        self._patches(lambda *_args: self.fail("invalid case must stop before authoring"),
                      research_result=selected, compatible_cases=[case])
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")
        self.assertEqual(self.pin_calls, [])

    def test_wrong_reuse_repository_fails_locally_without_pin(self):
        selected, case, _cache = self._reuse_inputs(
            repo="https://github.com/other/project",
            snapshot_repo="https://github.com/toktok/c-toxcore",
        )
        self._patches(lambda *_args: self.fail("invalid repository must stop before authoring"),
                      research_result=selected, compatible_cases=[case])
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")
        self.assertEqual(self.pin_calls, [])

    def test_malformed_model_source_selection_is_a_local_failure(self):
        selected = {"repository": "https://[broken", "files": ["README.md", "LICENSE"],
                    "rationale": "fixture", "reuse_case_id": None, "delivery_profile": "web",
                    "scenario": {"name": "Fixture", "audience": "Fixture", "objective": "Complete",
                                 "workflow": ["Start"], "acceptance": ["Visible"]}}
        self._patches(lambda *_args: self.fail("invalid source selection must stop before authoring"),
                      research_result=selected)
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")
        self.assertEqual(self.pin_calls, [])

    def test_source_selection_validator_rejects_malformed_inputs_precisely(self):
        for repository, files in [
            (None, ["README.md", "LICENSE"]),
            (17, ["README.md", "LICENSE"]),
            ("https://[broken", ["README.md", "LICENSE"]),
            ("https://github.com/valid/repo", []),
            ("https://github.com/valid/repo", ["README.md", "src/../escape", "LICENSE"]),
            ("https://github.com/valid/repo", ["README.md", "src/main.py"]),
        ]:
            with self.subTest(repository=repository, files=files), self.assertRaises(runner.FactoryError) as caught:
                runner.validate_research_source_selection({"repository": repository, "files": files})
            self.assertEqual(caught.exception.code, "source_selection_invalid")

    def test_corrupted_reused_source_bytes_pause_as_workflow_integrity(self):
        selected, case, cache = self._reuse_inputs()
        (cache / "README.md").write_bytes(b"corrupted\n")
        self._patches(lambda *_args: self.fail("integrity failure must stop before authoring"),
                      research_result=selected, compatible_cases=[case])
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        self.assertEqual(result["code"], "workflow_integrity")
        self.assertEqual(self.service.status("host-fixture")["status"], "paused")

    def test_oversized_new_source_response_is_a_local_selection_failure(self):
        self._patches(lambda *_args: self.fail("oversized source must stop before authoring"))
        runner.pin_sources.side_effect = runner.FactoryError("source response exceeds download limit")
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")

    def test_non_utf8_new_source_is_a_local_selection_failure(self):
        self._patches(lambda *_args: self.fail("binary source must stop before authoring"))
        runner.pin_sources.side_effect = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "source_selection_invalid")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")

    def test_known_item_download_failure_is_isolated(self):
        def produce_stub(*_args):
            write_json(self.work / "IMPORT_RECEIPT.json", {
                "artifact_id": "artifact", "case_id": "case", "case_revision": 1,
                "digest": "d" * 64, "exported_zip_sha256": "e" * 64,
                "export": {"download_url": "/download"},
            })
            for path in (self.work / "packages/template-snapshot.zip", self.work / "atlas-development-package.zip"):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(b"fixture package")
            return {"artifact_id": "artifact", "case_id": "case", "case_revision": 1, "url": "/api/factory/artifacts/artifact"}

        def missing_item_download(_work, _api):
            raise runner.urllib.error.HTTPError(
                "https://fixture.invalid/download", 404, "missing item", {}, None
            )

        self._patches(produce_stub, missing_item_download)
        result = self.execute()
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["code"], "leaf_delivery_error")
        self.assertEqual(self.service.status("host-fixture")["status"], "running")

    def test_completed_reused_step_repairs_leaf_state_without_provider_calls(self):
        self._patches(lambda *_args: self.fail("reused leaf must not import again"))
        development = b"fixture development package"
        existing = {
            "artifact_id": "artifact-reused",
            "files": {"development": {"available": True, "sha256": hashlib.sha256(development).hexdigest()}},
            "production": {"review_status": "passed"},
        }
        write_json(self.work / "REQUEST.json", {
            "leaf": self.leaf,
            "leaf_sha256": self.item["leaf_sha256"],
            "full_plan_id": "host-fixture",
            "profile": runner.profiles.VERSION,
            "model": MODEL,
        })
        write_json(self.work / "EXISTING_TEMPLATE.json", existing)
        workflow = WorkflowService(self.store, "workflow-host-fixture")
        workflow.begin("host-fixture", self.leaf, "attempt-1", STEPS[0], runner.digest(runner.load(self.work / "REQUEST.json")))
        workflow.complete("host-fixture", self.leaf, "attempt-1", STEPS[0], runner.workflow_outputs(self.work / "EXISTING_TEMPLATE.json"), reused=True)
        self.service.update_leaf("host-fixture", self.leaf, "running", {
            "current_attempt": "attempt-1",
            "workdir": str(self.work.relative_to(self.root)),
        })

        def get_existing_bytes(_api, route):
            if route.startswith("/api/factory/assisted-templates?leaf="):
                return json.dumps({"items": [existing]}).encode()
            if route == "/api/factory/assisted-templates/artifact-reused/files/development":
                return development
            self.fail("unexpected download route: " + route)

        with patch.object(runner, "get_bytes", side_effect=get_existing_bytes):
            result = self.execute()
        self.assertEqual(result["state"], "reused")
        self.assertEqual(self.service.status("host-fixture")["items"][0]["state"], "reused")
        self.assertEqual(self.service.status("host-fixture")["new_calls"], 0)
        self.assertEqual(self.provider_calls, [])
        detail = workflow.detail("host-fixture")
        self.assertEqual(detail["items"][0]["steps"][0]["state"], "reused")
        self.assertEqual(detail["items"][0]["steps"][1]["state"], "pending")

    def test_download_failure_cannot_make_leaf_ready(self):
        def produce_stub(*_args):
            write_json(self.work / "IMPORT_RECEIPT.json", {"artifact_id": "artifact", "case_id": "case", "case_revision": 1, "digest": "d" * 64, "exported_zip_sha256": "e" * 64, "export": {"download_url": "/download"}})
            for p in (self.work / "packages" / "template-snapshot.zip", self.work / "atlas-development-package.zip"):
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(b"fixture package")
            return {"artifact_id": "artifact", "case_id": "case", "case_revision": 1, "url": "/api/factory/artifacts/artifact"}

        def broken_download(_work, _api):
            raise runner.FactoryError("download bytes differ", "workflow_integrity", 409)

        self._patches(produce_stub, broken_download)
        result = self.execute()
        self.assertEqual(result["state"], "paused")
        status = self.service.status("host-fixture")
        self.assertNotEqual(status["items"][0]["state"], "ready_not_run")
        detail = WorkflowService(self.store, "workflow-host-fixture").detail("host-fixture")
        self.assertEqual(detail["items"][0]["steps"][-1]["step"], "download")
        self.assertEqual(detail["items"][0]["steps"][-1]["state"], "paused", json.dumps(status, indent=2))


class DownloadEvidenceTests(unittest.TestCase):
    def test_verify_download_checks_real_zip_bytes_and_case_binding(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            case = {"case_id": "case-1", "revision": 2, "digest": "a" * 64}
            files = {"blueprint/inputs/shared-case-record.json": json.dumps(case).encode()}
            entry_hashes = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
            manifest = {
                "template_digest": "b" * 64,
                "entry_sha256": entry_hashes,
                "blueprint_sha256": {"inputs/shared-case-record.json": entry_hashes[next(iter(files))]},
            }
            output = io.BytesIO()
            with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
                for name, data in files.items():
                    archive.writestr(name, data)
                archive.writestr("HANDOFF_MANIFEST.json", json.dumps(manifest))
            raw = output.getvalue()
            write_json(work / "IMPORT_RECEIPT.json", {
                "artifact_id": "artifact-1", "digest": "b" * 64,
                "exported_zip_sha256": hashlib.sha256(raw).hexdigest(),
                "case_ref": case, "export": {"download_url": "/fixture.zip"},
            })
            with patch.object(runner, "get_bytes", return_value=raw):
                proof = runner.verify_download(work, "https://fixture.invalid")
            self.assertEqual(proof["case_ref"], case)
            self.assertEqual(proof["application_runtime"], "not_run")

            bad_ref = {**case, "revision": 3}
            write_json(work / "IMPORT_RECEIPT.json", {
                "artifact_id": "artifact-1", "digest": "b" * 64,
                "exported_zip_sha256": hashlib.sha256(raw).hexdigest(),
                "case_ref": bad_ref, "export": {"download_url": "/fixture.zip"},
            })
            with patch.object(runner, "get_bytes", return_value=raw):
                with self.assertRaisesRegex(runner.FactoryError, "download case differs"):
                    runner.verify_download(work, "https://fixture.invalid")

            write_json(work / "IMPORT_RECEIPT.json", {
                "artifact_id": "artifact-1", "digest": "b" * 64,
                "exported_zip_sha256": "0" * 64, "case_ref": case,
                "export": {"download_url": "/fixture.zip"},
            })
            with patch.object(runner, "get_bytes", return_value=raw):
                with self.assertRaisesRegex(runner.FactoryError, "download bytes differ"):
                    runner.verify_download(work, "https://fixture.invalid")


class AcceptedResearchIdempotencyTests(unittest.TestCase):
    def test_real_case_library_replay_preserves_original_acceptance_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            (pack / "atlas").mkdir(parents=True)
            (pack / "applications").mkdir()
            (pack / "mvp_apps.json").write_text(json.dumps([
                {"slug": slug, "name": slug.replace("-", " ").title()}
                for slug in ["fixture-workflow"] + [f"fixture-leaf-{i}" for i in range(32)]
            ]))
            with sqlite3.connect(pack / "atlas" / "atlas.sqlite") as con:
                con.execute("CREATE TABLE leaf(slug TEXT PRIMARY KEY,name TEXT,name_zh TEXT,defining_core TEXT,overview TEXT)")
                con.execute("INSERT INTO leaf VALUES(?,?,?,?,?)", (
                    "fixture-workflow", "Fixture Workflow", "测试工作流", "Pinned workflow fixture", "Local host test"
                ))
            (pack / "applications" / "fixture-workflow.md").write_text("fixture application leaf\n")
            store = FactoryStore(pack / "state", pack)
            CaseLibrary(store)
            snapshot_root = store.root / "pinned-source"
            (snapshot_root / "src").mkdir(parents=True)
            (snapshot_root / "README.md").write_text("Fixture project documentation.\nSecond line.\n")
            (snapshot_root / "LICENSE").write_text("MIT License\nPermission is hereby granted.\n")
            (snapshot_root / "src" / "core.py").write_text("def run():\n    return True\n")
            source_files = ["README.md", "LICENSE", "src/core.py"]
            file_hashes = {name: hashlib.sha256((snapshot_root / name).read_bytes()).hexdigest() for name in source_files}
            snapshot = {
                "repository": "https://github.com/fixture-owner/fixture-repository",
                "commit_sha": "c" * 40,
                "strategy_version": "host-fixture.v1",
                "collected_at": "2026-10-21T00:00:00Z",
                "files": file_hashes,
                "local_root": str(snapshot_root),
                "license_files": ["LICENSE"],
                "license": {"status": "identified", "spdx_id": "MIT", "notice_hashes": {"LICENSE": file_hashes["LICENSE"]}},
            }
            authored = {
                "repo_name": "Fixture Repository",
                "name": "Fixture Workflow Template",
                "audience": "Local user",
                "objective": "Inspect a fixture workflow",
                "workflow": ["Inspect", "Confirm"],
                "acceptance": ["Confirmation is recorded"],
                "observations": [
                    ("code_observation", "src/core.py", 1, 2, "The core function returns a deterministic result."),
                    ("code_observation", "README.md", 1, 1, "The README documents the fixture project."),
                ],
            }
            identity = "d" * 64
            review = {
                "input_digest": identity,
                "checks": {"source_fidelity": True},
                "observations": [
                    {"index": 0, "verdict": "accepted", "reason": "Matches pinned source lines."},
                    {"index": 1, "verdict": "accepted", "reason": "Matches pinned documentation."},
                ],
            }
            item = {"leaf": "fixture-workflow"}
            work = root / "items" / item["leaf"] / "attempt-1"
            work.mkdir(parents=True)
            service = FullAuxiliaryService(store, "case-fixture", lambda: 1000.0)
            with patch.object(runner, "ROOT", root), patch.object(runner, "PLAN_ID", "case-fixture"):
                runner.save_accepted_research(service, item, work, authored, snapshot, review, identity, "author-session", "review-session")
                original_bytes = (work / "ACCEPTED_RESEARCH_RECEIPT.json").read_bytes()
                original = json.loads(original_bytes)
                with store.connect() as con:
                    versions_before = con.execute("SELECT COUNT(*) FROM case_revision").fetchone()[0]
                    reviews_before = con.execute("SELECT COUNT(*) FROM evidence_review").fetchone()[0]

                runner.save_accepted_research(service, item, work, authored, snapshot, review, identity, "author-session", "review-session")
                replay = json.loads((work / "ACCEPTED_RESEARCH_REPLAY_RECEIPT.json").read_text())
                self.assertEqual((work / "ACCEPTED_RESEARCH_RECEIPT.json").read_bytes(), original_bytes)
                self.assertFalse(original["replayed"])
                self.assertTrue(replay["replayed"])
                self.assertEqual({k: v for k, v in replay.items() if k != "replayed"}, {k: v for k, v in original.items() if k != "replayed"})
                with store.connect() as con:
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM case_revision").fetchone()[0], versions_before)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM evidence_review").fetchone()[0], reviews_before)
                    self.assertEqual(versions_before, 1)
                    self.assertEqual(reviews_before, 2)

if __name__ == "__main__":
    unittest.main()
