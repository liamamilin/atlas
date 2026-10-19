"""Checkpoint, host-provenance and independent-review contracts for T03."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.case_research import _observation_payload, run_research
from template_factory.cases import CaseLibrary
from template_factory.store import FactoryError, FactoryStore, canonical, digest, uid


PACK_ROOT = Path(__file__).resolve().parents[1]
COMMIT = "c" * 40


class FakePipeline:
    def __init__(self, store, fail_first_fetch=False):
        self.store = store
        self.fail_first_fetch = fail_first_fetch
        self.fetch_calls = []

    def fetcher(self, repository, destination, *, commit):
        self.fetch_calls.append((repository, commit))
        if self.fail_first_fetch:
            self.fail_first_fetch = False
            destination.mkdir(parents=True)
            (destination / "partial").write_text("incomplete", encoding="utf-8")
            raise FactoryError("simulated archive interruption", "source_download_failed", 502)
        destination.mkdir(parents=True, exist_ok=False)
        (destination / "main.py").write_text("def complete_task():\n    return True\n", encoding="utf-8")
        (destination / "LICENSE").write_text("MIT License\n", encoding="utf-8")
        return {"repository": "https://github.com/example/tasks", "repository_id": 9876,
                "commit": commit, "license": "MIT",
                "notice_hashes": {"LICENSE": hashlib.sha256((destination / "LICENSE").read_bytes()).hexdigest()},
                "archive_sha256": "f" * 64, "excluded_paths": []}


class CaseResearchV1Tests(unittest.TestCase):
    def test_exact_source_mount_prefix_normalizes_only_existing_files(self):
        from template_factory.case_research import _source_path
        files = {"src/main.py": "a" * 64}
        self.assertEqual(_source_path("source/src/main.py", files), "src/main.py")
        for bad in ("../src/main.py", "source/source/src/main.py", "source/missing.py"):
            with self.assertRaises(FactoryError):
                _source_path(bad, files)

    def test_unlocated_observation_is_quarantined_without_rewriting_kept_claims(self):
        from template_factory.case_research import _located_subset
        valid = {"id": "good", "kind": "code_observation", "path": "main.py", "statement": "Exact original claim"}
        invalid = {"id": "bad", "kind": "code_observation", "path": "source/directory", "statement": "Unsupported claim"}
        dependent = {"id": "dependent", "kind": "inference", "depends_on": ["bad"], "statement": "Dependent claim"}
        raw = {"observations": [valid, invalid, dependent], "workflow_evidence_ids": ["good", "bad"], "unknowns": [], "summary": "Unchanged summary"}
        effective, audit = _located_subset(raw, {"main.py": "a" * 64})
        self.assertEqual(effective["observations"], [valid])
        self.assertEqual(effective["summary"], raw["summary"])
        self.assertEqual(len(raw["observations"]), 3)
        self.assertEqual({row["id"] for row in audit}, {"bad", "dependent"})
        self.assertEqual(effective["workflow_evidence_ids"], ["good"])
        self.assertEqual(len(effective["unknowns"]), 2)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK_ROOT / "mvp_apps.json", self.pack / "mvp_apps.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES(?,?,?,?,?)", ("task-management-application", "Task manager", "任务管理", "manage tasks", "Task workflows"))
        (self.pack / "applications").mkdir()
        (self.pack / "applications/task-management-application.md").write_text("# Task manager\n", encoding="utf-8")
        self.store = FactoryStore(self.root / "factory", self.pack)
        CaseLibrary(self.store)
        self.job_id, self.token = uid("job"), "lease-token-1"
        self.batch_id = uid("bat")
        now = time.time()
        scenario = self.store.save_scenario({"leaf": "task-management-application", "name": "Complete a task", "audience": "Individual", "objective": "Complete tasks", "workflow": ["Create a task", "Mark it complete"], "acceptance": ["The completed task stays completed"], "status": "ready"})
        leaf = self.store.leaf(scenario["leaf"])
        identity = {"campaign_id": "campaign-test", "plan_id": "plan-test", "plan_digest": "b" * 64,
                    "product_id": "product-test", "segment": "G1", "policy_version": "test-policy"}
        snapshot = {"leaf": leaf, "scenario": scenario, "scenario_digest": digest(scenario),
                    "v1": identity, "config": {"model": "fake/model", "timeout": 1},
                    "repository_hints": [{"repository": "https://github.com/example/tasks", "reason": "Implements task completion."}]}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (self.batch_id, "running", "{}", "2026-10-19T00:00:00Z"))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (self.job_id, self.batch_id, "case-research", "running", "case-research", 1,
                         self.token, now + 3600, canonical(snapshot), None, "2026-10-19T00:00:00Z", "2026-10-19T00:00:00Z"))
        self.job = {"id": self.job_id, "batch_id": self.batch_id, "kind": "case-research", "state": "running",
                    "stage": "case-research", "attempt": 1, "token": self.token, "snapshot": snapshot}
        self.pipeline = FakePipeline(self.store)
        self.calls = []

    def tearDown(self):
        self.tmp.cleanup()

    def _agent(self, invalid_path=False, fail_review=False):
        def agent(name, prompt, payload, source=None, **kwargs):
            self.calls.append(name)
            if name.startswith("case-evidence-review-"):
                if fail_review:
                    return {"outcome": "accepted", "summary": "Missing an evidence item.", "observations": []}
                observation = payload["observations"][0]
                return {"outcome": "accepted", "summary": "The cited implementation supports task completion.",
                        "observations": [{"evidence_id": observation["evidence_id"], "outcome": "accepted",
                                          "reason": "The source function returns after the requested task action.",
                                          "citations": [{"path": "main.py", "line_start": 1, "line_end": 2}]}]}
            if name.startswith("case-study-"):
                return {"summary": "The project exposes a task completion operation.", "scope": "Single-user task completion",
                        "unknowns": ["No runtime execution was performed."],
                        "scenario_fit": {"reason": "The core operation corresponds to completing a task.",
                                         "workflow_support": ["mark task complete"], "adopted_scope": ["task completion"],
                                         "exclusions": ["remote sync"]},
                        "observations": [{"id": "completion", "kind": "code_observation",
                                          "statement": "complete_task returns a successful result.",
                                          "path": "../secret" if invalid_path else "main.py", "line_start": 1, "line_end": 2}],
                        "workflow_evidence_ids": ["completion"]}
            raise AssertionError("unexpected model stage " + name)
        return agent

    def _checkpoint(self):
        def checkpoint(name, create):
            saved = self.store.checkpoint(self.job_id, name)
            if saved is not None:
                self.assertEqual(digest(saved["result"]), saved["digest"])
                return saved["result"]
            value = create()
            record = {"result": value, "digest": digest(value)}
            self.store.checkpoint(self.job_id, name, record, self.token)
            return value
        return checkpoint

    def _stage(self, *_):
        pass

    def test_end_to_end_research_pins_hashes_reviews_and_completes_case_basis(self):
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            run_research(self.pipeline, self.job, Path(self.root), self._agent(), self._stage, self._checkpoint())
        library = CaseLibrary(self.store, initialize=False)
        cases = library.list_cases(scenario_id=self.job["snapshot"]["scenario"]["id"])
        self.assertEqual(len(cases), 1)
        case = cases[0]
        self.assertEqual(case["source_snapshots"][0]["commit_sha"], COMMIT)
        self.assertIn("main.py", case["source_snapshots"][0]["files"])
        observation = case["observations"][0]
        self.assertEqual(observation["location"]["file_digest"], case["source_snapshots"][0]["files"]["main.py"])
        self.assertEqual(observation["reviews"][0]["outcome"], "accepted")
        self.assertEqual(case["observations"][0]["kind"], "code_observation")
        with self.store.connect() as con:
            parent = con.execute("SELECT state,stage FROM job WHERE id=?", (self.job_id,)).fetchone()
            queued = con.execute("SELECT kind,snapshot FROM job WHERE batch_id=? AND kind='blueprint-production'", (self.batch_id,)).fetchone()
        self.assertEqual((parent[0], parent[1]), ("completed", "case-committed"))
        self.assertIsNotNone(queued)
        self.assertEqual(json.loads(queued[1])["case_basis"]["case_refs"][0]["case_id"], case["case_id"])
        self.assertIn("case-study-", self.calls[0])
        self.assertTrue(any(name.startswith("case-evidence-review-") for name in self.calls))
        self.assertEqual(self.pipeline.fetch_calls[0][1], COMMIT)

    def test_invalid_delivered_response_can_use_bounded_protocol_correction(self):
        base = self._agent()
        calls = []
        def corrective(name, prompt, payload, source=None, **kwargs):
            result = base(name, prompt, payload, source, **kwargs)
            if name.startswith("case-study-"):
                calls.append((name, kwargs))
                if len(calls) == 1:
                    result["observations"][0]["line_end"] = 999
            return result
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT) as resolve:
            run_research(self.pipeline, self.job, Path(self.root), corrective, self._stage, self._checkpoint())
        self.assertEqual(len(calls), 2)
        self.assertIn("protocol-repair", calls[1][0])
        self.assertIn("budget_stage", calls[1][1])
        self.assertEqual(resolve.call_count, 1)
        self.assertEqual(len(CaseLibrary(self.store).list_cases()), 1)

    def test_discovery_used_only_when_hints_are_empty(self):
        self.job["snapshot"]["repository_hints"] = []
        self.pipeline.store.checkpoint(self.job_id, "case-discovery", {"result": {
            "candidates": [{"repository": "https://github.com/example/tasks", "reason": "Task workflow"}],
            "selected": "https://github.com/example/tasks", "rationale": "Implements workflow."},
            "digest": digest({"candidates": [{"repository": "https://github.com/example/tasks", "reason": "Task workflow"}],
                              "selected": "https://github.com/example/tasks", "rationale": "Implements workflow."})}, self.token)
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            run_research(self.pipeline, self.job, Path(self.root), self._agent(), self._stage, self._checkpoint())
        self.assertNotIn("case-discovery", self.calls)
        self.assertEqual(len(CaseLibrary(self.store, initialize=False).list_cases()), 1)

    def test_commit_sha_is_checkpointed_before_failed_download_and_reused(self):
        self.pipeline = FakePipeline(self.store, fail_first_fetch=True)
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT) as resolve:
            with self.assertRaisesRegex(FactoryError, "simulated archive interruption"):
                run_research(self.pipeline, self.job, Path(self.root), self._agent(), self._stage, self._checkpoint())
            self.assertEqual(self.store.checkpoint(self.job_id, "case-source-pin-" + hashlib.sha256(b"https://github.com/example/tasks").hexdigest()[:12])["result"]["commit_sha"], COMMIT)
            run_research(self.pipeline, self.job, Path(self.root), self._agent(), self._stage, self._checkpoint())
        self.assertEqual(resolve.call_count, 1)
        self.assertEqual([call[1] for call in self.pipeline.fetch_calls], [COMMIT, COMMIT])
        self.assertEqual(len(CaseLibrary(self.store, initialize=False).list_cases()), 1)

    def test_invalid_source_path_is_rejected_before_persisting_case(self):
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            with self.assertRaisesRegex(FactoryError, "unknown source path"):
                run_research(self.pipeline, self.job, Path(self.root), self._agent(invalid_path=True), self._stage, self._checkpoint())
        self.assertEqual(CaseLibrary(self.store, initialize=False).list_cases(), [])

    def test_host_evidence_ids_are_unique_per_logical_case_revision(self):
        source = self.store.root / "ids-source"
        source.mkdir()
        (source / "main.py").write_text("def complete_task():\n    return True\n", encoding="utf-8")
        files = {"main.py": hashlib.sha256((source / "main.py").read_bytes()).hexdigest()}
        study = {"observations": [{"id": "same-model-id", "kind": "code_observation", "statement": "Task completion returns.", "path": "main.py", "line_start": 1, "line_end": 2}], "workflow_evidence_ids": ["same-model-id"]}
        first, _ = _observation_payload(study, "https://github.com/example/tasks", COMMIT, files, source, "case-revision-one")
        second, _ = _observation_payload(study, "https://github.com/example/tasks", COMMIT, files, source, "case-revision-two")
        self.assertNotEqual(first[0][1]["evidence_id"], second[0][1]["evidence_id"])

    def test_malformed_independent_review_keeps_case_but_does_not_queue_template(self):
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            with self.assertRaisesRegex(FactoryError, "cover every observation"):
                run_research(self.pipeline, self.job, Path(self.root), self._agent(fail_review=True), self._stage, self._checkpoint())
        self.assertEqual(len(CaseLibrary(self.store, initialize=False).list_cases()), 1)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM job WHERE kind='blueprint-production'").fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT state FROM job WHERE id=?", (self.job_id,)).fetchone()[0], "running")
        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            run_research(self.pipeline, self.job, Path(self.root), self._agent(), self._stage, self._checkpoint())
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM case_revision").fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM job WHERE kind='blueprint-production'").fetchone()[0], 1)
            self.assertEqual(con.execute("SELECT state FROM job WHERE id=?", (self.job_id,)).fetchone()[0], "completed")

    def test_late_worker_cannot_commit_case_after_ownership_is_cancelled(self):
        real_agent = self._agent()

        def cancel_after_research(name, prompt, payload, source=None):
            result = real_agent(name, prompt, payload, source)
            if name.startswith("case-study-"):
                with self.store.connect(True) as con:
                    con.execute("UPDATE job SET state='cancelled',token=NULL,lease=NULL WHERE id=?", (self.job_id,))
            return result

        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            with self.assertRaisesRegex(FactoryError, "ownership lost"):
                run_research(self.pipeline, self.job, Path(self.root), cancel_after_research, self._stage, self._checkpoint())
        self.assertEqual(CaseLibrary(self.store, initialize=False).list_cases(), [])

    def test_late_worker_cannot_commit_review_after_ownership_is_cancelled(self):
        real_agent = self._agent()

        def cancel_during_review(name, prompt, payload, source=None):
            result = real_agent(name, prompt, payload, source)
            if name.startswith("case-evidence-review-"):
                with self.store.connect(True) as con:
                    con.execute("UPDATE job SET state='cancelled',token=NULL,lease=NULL WHERE id=?", (self.job_id,))
            return result

        with patch("template_factory.sources.resolve_commit", return_value=COMMIT):
            with self.assertRaisesRegex(FactoryError, "ownership lost"):
                run_research(self.pipeline, self.job, Path(self.root), cancel_during_review, self._stage, self._checkpoint())
        cases = CaseLibrary(self.store, initialize=False).list_cases()
        self.assertEqual(len(cases), 1)
        self.assertEqual(cases[0]["observations"][0]["reviews"], [])


if __name__ == "__main__":
    unittest.main()
