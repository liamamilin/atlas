"""Factory behavior tests. Fake CLI/runtime are explicitly not real production evidence."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import sys
import tarfile
import tempfile
import unittest
import threading
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.api import dispatch
from template_factory.artifacts import (
    archive_tree,
    freeze,
    render_template,
    validate_plan,
)
from template_factory.cli import parse_result
from template_factory.pipeline import Pipeline
from template_factory.sources import fetch_source, github_repo
from template_factory.store import FactoryError, FactoryStore


class FactoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        (self.pack / "atlas").mkdir(parents=True)
        con = sqlite3.connect(self.pack / "atlas/atlas.sqlite")
        con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
        con.execute(
            "INSERT INTO leaf VALUES (?,?,?,?,?)",
            (
                "task-management-application",
                "Task manager",
                "任务管理",
                "tasks",
                "overview",
            ),
        )
        con.commit()
        con.close()
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.spec = {
            "leaf": "task-management-application",
            "name": "每日待办",
            "audience": "个人",
            "objective": "管理任务",
            "workflow": ["添加任务", "完成任务"],
            "acceptance": ["可添加并完成任务"],
            "status": "ready",
        }

    def tearDown(self):
        self.tmp.cleanup()

    def scenario(self):
        return self.store.save_scenario(self.spec)

    def test_safe_generation_rejects_existing_archived_and_completed_zero(self):
        request = {
            "kind": "scenarios",
            "name": "safe",
            "leaves": [self.spec["leaf"]],
            "model": "fake/flash",
            "skip_generated": True,
        }
        item = self.store.save_scenario({**self.spec, "status": "archived"})
        with self.assertRaises(FactoryError) as error:
            self.store.create_batch(request)
        self.assertEqual(error.exception.code, "scenario_already_generated")
        self.assertEqual(self.store.batches(), [])
        batch = self.store.create_batch({**request, "skip_generated": False})
        self.assertEqual(len(batch["jobs"]), 1)
        self.assertEqual(self.store.scenario(item["id"])["status"], "archived")
        self.store.batch_action(batch["id"], "cancel")
        with self.store.connect(True) as con:
            con.execute("DELETE FROM scenario WHERE id=?", (item["id"],))
        self.store.create_batch(request)
        job = self.store.claim("producer")
        pipeline = self.fake_pipeline()
        pipeline.cli.run = lambda *args: {
            "scenarios": [],
            "reason": "No useful additions.",
        }
        pipeline.run(job)
        before = len(self.store.batches())
        with self.assertRaises(FactoryError) as error:
            self.store.create_batch(request)
        self.assertEqual(error.exception.code, "scenario_already_generated")
        self.assertEqual(len(self.store.batches()), before)
        self.assertEqual(
            len(self.store.create_batch({**request, "skip_generated": False})["jobs"]),
            1,
        )

    def test_generation_queue_blocks_concurrent_duplicate_leaf(self):
        request = {
            "kind": "scenarios",
            "name": "parallel",
            "leaves": [self.spec["leaf"]],
            "model": "fake/flash",
            "skip_generated": True,
        }

        def queue():
            try:
                return self.store.create_batch(request)["id"]
            except FactoryError as error:
                return error.code

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: queue(), range(2)))
        self.assertEqual(results.count("scenario_generation_active"), 1)
        self.assertEqual(len(self.store.batches()), 1)
        batch = self.store.batches()[0]
        self.assertEqual(len(batch["jobs"]), 1)
        self.store.batch_action(batch["id"], "pause")
        with self.assertRaises(FactoryError) as error:
            self.store.create_batch({**request, "skip_generated": False})
        self.assertEqual(error.exception.code, "scenario_generation_active")
        self.store.batch_action(batch["id"], "cancel")
        self.assertEqual(len(self.store.create_batch(request)["jobs"]), 1)

    def test_skip_generated_requires_boolean(self):
        with self.assertRaises(FactoryError):
            self.store.create_batch({"kind": "scenarios", "skip_generated": "false"})
        self.assertEqual(self.store.batches(), [])

    def test_generation_pins_existing_scenarios_and_output_language(self):
        item = self.scenario()
        self.store.save_scenario(
            {**self.spec, "name": "archived", "status": "archived"}
        )
        batch = self.store.create_batch(
            {
                "kind": "scenarios",
                "name": "discover",
                "leaves": [item["leaf"]],
                "model": "fake/flash",
                "language": "en",
            }
        )
        self.store.save_scenario(
            {**item, "objective": "edited after queueing", "expected_revision": 1},
            item["id"],
        )
        self.store.save_scenario({**self.spec, "name": "created after queueing"})
        job = self.store.claim("producer")
        expected = job["snapshot"]["existing_scenarios"]
        self.assertEqual(len(expected), 1)
        self.assertEqual(expected[0]["id"], item["id"])
        self.assertEqual(expected[0]["revision"], 1)
        self.assertEqual(expected[0]["objective"], item["objective"])
        self.assertEqual(batch["config"]["language"], "en")
        pipeline = self.fake_pipeline()

        def inspect(directory, *args):
            value = json.loads((directory / "input.json").read_text())
            self.assertEqual(value["existing_scenarios"], expected)
            self.assertEqual(value["language"], "en")
            return {
                "scenarios": [],
                "reason": "The existing scene already covers the useful workflow.",
            }

        pipeline.cli.run = inspect
        pipeline.run(job)
        self.assertEqual(self.store.job(job["id"])["generation_result"]["count"], 0)

    def test_zero_scenarios_complete_without_extra_reviews_or_catalog_changes(self):
        item = self.scenario()
        batch = self.store.create_batch(
            {
                "kind": "scenarios",
                "name": "covered",
                "leaves": [item["leaf"]],
                "model": "fake/flash",
            }
        )
        job = self.store.claim("producer")
        pipeline = self.fake_pipeline()
        pipeline.cli.run = lambda *args: {
            "scenarios": [],
            "reason": "已有场景覆盖了本次用户流程。",
        }
        pipeline.run(job)
        current = self.store.job(job["id"])
        self.assertEqual(current["state"], "completed")
        self.assertEqual(
            current["generation_result"],
            {"count": 0, "reason": "已有场景覆盖了本次用户流程。", "scenario_ids": []},
        )
        finished = self.store.batch(batch["id"])
        self.assertEqual(finished["state"], "completed")
        self.assertEqual(len(finished["jobs"]), 1)
        self.assertEqual(
            finished["jobs"][0]["generation_result"], current["generation_result"]
        )
        self.assertEqual(self.store.scenario(item["id"]), item)
        self.assertEqual(len(self.store.scenarios()), 1)
        evidence, _ = dispatch(
            "GET", f"/api/factory/jobs/{job['id']}/evidence", store=self.store
        )
        self.assertTrue(
            any(e["path"].endswith("scenarios/result.json") for e in evidence)
        )

    def test_empty_proposal_without_explanation_fails_and_saves_nothing(self):
        for reason in (None, "", "   "):
            with self.subTest(reason=reason):
                batch = self.store.create_batch(
                    {
                        "kind": "scenarios",
                        "name": "invalid",
                        "leaves": [self.spec["leaf"]],
                        "model": "fake/flash",
                    }
                )
                job = self.store.claim("producer")
                pipeline = self.fake_pipeline()
                pipeline.cli.run = lambda *args: {"scenarios": [], "reason": reason}
                with self.assertRaises(FactoryError):
                    pipeline.run(job)
                self.assertEqual(self.store.job(job["id"])["state"], "failed")
                self.assertEqual(len(self.store.batch(batch["id"])["jobs"]), 1)
        self.assertEqual(self.store.scenarios(), [])

    def test_invalid_generation_language_creates_no_batch(self):
        for language in ("", "zh-CN", None, ["zh"]):
            with self.subTest(language=language), self.assertRaises(FactoryError):
                self.store.create_batch(
                    {
                        "kind": "scenarios",
                        "name": "invalid locale",
                        "leaves": [self.spec["leaf"]],
                        "model": "fake/flash",
                        "language": language,
                    }
                )
        self.assertEqual(self.store.batches(), [])

    @staticmethod
    def scenario_report(outcome="passed"):
        from template_factory.scenario_review import DIMENSIONS

        return {
            "summary": "Synthetic review; no provider or runtime execution.",
            "checks": [
                {
                    "dimension": dimension,
                    "outcome": outcome,
                    "reason": "Synthetic task workflow and observable acceptance checked.",
                }
                for dimension in DIMENSIONS
            ],
            "leaf_quotes": ["tasks"],
            "related_scenario_ids": [],
            "suggestions": []
            if outcome == "passed"
            else ["补齐添加与完成任务的可观察验收条件"],
        }

    def review_batch(self, items, **overrides):
        return self.store.create_batch(
            {
                "kind": "scenario-review",
                "name": "review",
                "model": "fake/flash",
                "scenario_ids": [s["id"] for s in items],
                "scenario_revisions": {s["id"]: s["revision"] for s in items},
                **overrides,
            }
        )

    def test_scenario_review_pins_inputs_and_never_confirms(self):
        item = self.store.save_scenario({**self.spec, "status": "draft"})
        peer = self.scenario()
        self.review_batch([item])
        self.assertIsNone(self.store.claim("producer", "production"))
        job = self.store.claim("reviewer", "verification")
        self.assertEqual(job["snapshot"]["peer_scenarios"][0]["id"], peer["id"])
        self.assertTrue(job["snapshot"]["leaf"]["content"])
        self.fake_pipeline().run(job)
        stored = next(s for s in self.store.scenarios() if s["id"] == item["id"])
        self.assertEqual(stored["status"], "draft")
        self.assertEqual(stored["revision"], 1)
        report = stored["reviews"][0]
        self.assertTrue(report["current"])
        self.assertEqual(report["outcome"], "passed")
        self.assertEqual(report["input_digest"], job["snapshot"]["input_digest"])
        self.assertEqual(report["model"], "fake/flash")
        self.assertEqual(self.store.artifacts(), [])

    def test_agent_receives_an_exact_markdown_leaf_alongside_json(self):
        (self.pack / "applications").mkdir()
        content = "# tasks\n" + "完整正文，保留换行供读取工具分页。\n" * 300
        (self.pack / "applications/task-management-application.md").write_text(content)
        item = self.scenario()
        self.review_batch([item])
        job = self.store.claim("reviewer")
        pipeline = self.fake_pipeline()
        original_run = pipeline.cli.run

        def inspect(directory, *args):
            payload = json.loads((directory / "input.json").read_text())
            self.assertEqual(payload["leaf"]["content"], content)
            self.assertEqual(payload["leaf"]["content_file"], "leaf.md")
            document = (directory / "leaf.md").read_bytes()
            self.assertEqual(document, content.encode())
            self.assertEqual(
                hashlib.sha256(document).hexdigest(),
                job["snapshot"]["leaf"]["fingerprint"],
            )
            return original_run(directory, *args)

        pipeline.cli.run = inspect
        pipeline.run(job)
        self.assertEqual(self.store.scenarios()[0]["reviews"][0]["outcome"], "passed")

    def test_scenario_review_schema_rejects_unsupported_claims(self):
        from template_factory.scenario_review import validate_review

        item = self.scenario()
        self.review_batch([item])
        job = self.store.claim("reviewer")
        snapshot = job["snapshot"]
        bad_reports = []
        report = self.scenario_report()
        bad_reports.append({**report, "checks": report["checks"][:-1]})
        bad_reports.append({**report, "checks": [report["checks"][0]] * 5})
        bad_reports.append({**report, "leaf_quotes": ["fabricated definition"]})
        bad_reports.append({**report, "related_scenario_ids": ["scn_unknown"]})
        bad_reports.append({**self.scenario_report("needs_changes"), "suggestions": []})
        for report in bad_reports:
            with self.subTest(report=report), self.assertRaises(FactoryError):
                validate_review(report, snapshot)
        # An agent cannot override a problematic dimension by saying passed overall.
        report = self.scenario_report("needs_changes")
        report["outcome"] = "passed"
        self.assertEqual(validate_review(report, snapshot)["outcome"], "needs_changes")
        # Comparison does not itself mean material duplication.
        compared = {**snapshot, "peer_scenarios": [{"id": "compared-peer"}]}
        contradictory = {
            **self.scenario_report(),
            "related_scenario_ids": ["compared-peer"],
        }
        with self.assertRaises(FactoryError):
            validate_review(contradictory, compared)
        consistent = {
            **self.scenario_report("needs_changes"),
            "related_scenario_ids": ["compared-peer"],
        }
        self.assertEqual(
            validate_review(consistent, compared)["outcome"], "needs_changes"
        )

    def test_review_line_references_extract_exact_markdown_and_reject_invalid_ranges(
        self,
    ):
        from template_factory.scenario_review import validate_review

        content = "# tasks\n\n**Exact original** with punctuation.\nNext paragraph.\n"
        snapshot = {"leaf": {"content": content}, "peer_scenarios": []}
        value = {
            **self.scenario_report(),
            "leaf_evidence": [{"start_line": 3, "end_line": 4}],
        }
        report = validate_review(value, snapshot)
        self.assertEqual(
            report["leaf_quotes"],
            ["**Exact original** with punctuation.\nNext paragraph."],
        )
        self.assertEqual(report["leaf_evidence"], value["leaf_evidence"])
        for refs in (
            [],
            [{"start_line": 0, "end_line": 2}],
            [{"start_line": 3, "end_line": 5}],
            [{"start_line": True, "end_line": 2}],
            [{"start_line": "3", "end_line": 4}],
            [{"start_line": 4, "end_line": 3}],
            [{"start_line": 2, "end_line": 2}],
        ):
            with self.subTest(refs=refs), self.assertRaises(FactoryError):
                validate_review({**value, "leaf_evidence": refs}, snapshot)

    def test_scenario_review_invalid_result_fails_without_a_pass(self):
        item = self.scenario()
        self.review_batch([item])
        job = self.store.claim("reviewer")
        pipeline = self.fake_pipeline()
        pipeline.cli.run = lambda *args: {"outcome": "passed"}
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        scene = self.store.scenarios()[0]
        self.assertEqual(scene["reviews"], [])
        self.assertEqual(scene["review_jobs"][0]["state"], "failed")
        self.assertEqual(self.store.scenario(item["id"])["revision"], 1)

    def test_scenario_review_context_changes_expire_reports(self):
        item = self.scenario()
        self.review_batch([item])
        self.fake_pipeline().run(self.store.claim("reviewer"))
        self.assertTrue(self.store.scenarios()[0]["reviews"][0]["current"])
        peer = self.store.save_scenario({**self.spec, "name": "new peer"})
        stored = next(s for s in self.store.scenarios() if s["id"] == item["id"])
        self.assertFalse(stored["reviews"][0]["current"])
        # An archived peer was never part of the compared active context.
        self.store.save_scenario(
            {**peer, "status": "archived", "expected_revision": 1}, peer["id"]
        )
        self.assertTrue(
            next(s for s in self.store.scenarios() if s["id"] == item["id"])["reviews"][
                0
            ]["current"]
        )
        self.store.save_scenario(
            {**item, "objective": "changed", "expected_revision": 1}, item["id"]
        )
        self.assertFalse(
            next(s for s in self.store.scenarios() if s["id"] == item["id"])["reviews"][
                0
            ]["current"]
        )

    def test_scenario_review_leaf_changes_and_late_completion_are_historical(self):
        item = self.scenario()
        self.review_batch([item])
        job = self.store.claim("reviewer")
        (self.pack / "applications").mkdir()
        (self.pack / "applications/task-management-application.md").write_text(
            "a revised task definition"
        )
        self.fake_pipeline().run(job)
        scene = self.store.scenarios()[0]
        self.assertFalse(scene["reviews"][0]["current"])
        self.assertFalse(scene["review_jobs"][0]["current"])

    def test_scenario_review_queue_cas_duplicates_and_cancel_are_atomic(self):
        item = self.scenario()
        with self.assertRaises(FactoryError):
            self.review_batch([item], scenario_revisions={item["id"]: 0})
        self.assertEqual(self.store.batches(), [])
        batch = self.review_batch([item])
        with self.assertRaises(FactoryError):
            self.review_batch([item])
        self.assertEqual(len(self.store.batches()), 1)
        job = self.store.claim("reviewer")
        self.store.batch_action(batch["id"], "cancel")
        with self.assertRaises(FactoryError):
            self.store.complete_scenario_review(
                job["id"], job["token"], self.scenario_report()
            )
        self.assertEqual(self.store.scenarios()[0]["reviews"], [])

    def test_scenario_generation_queues_independent_review_and_preserves_draft_on_failure(
        self,
    ):
        batch = self.store.create_batch(
            {
                "kind": "scenarios",
                "name": "generate",
                "model": "fake/flash",
                "leaves": ["task-management-application"],
            }
        )
        job = self.store.claim("producer", "production")
        self.fake_pipeline().run(job)
        jobs = self.store.batch(batch["id"])["jobs"]
        self.assertEqual(
            sorted(j["kind"] for j in jobs), ["scenario-review", "scenarios"]
        )
        self.assertEqual(self.store.job(job["id"])["state"], "completed")
        review = self.store.claim("reviewer", "verification")
        broken = self.fake_pipeline()
        broken.cli.run = lambda *args: (_ for _ in ()).throw(
            FactoryError("provider unavailable")
        )
        with self.assertRaises(FactoryError):
            broken.run(review)
        self.assertEqual(len(self.store.scenarios()), 1)
        self.assertEqual(self.store.scenarios()[0]["status"], "draft")
        self.store.retry(review["id"])
        self.fake_pipeline().run(self.store.claim("retry", "verification"))
        self.assertEqual(self.store.scenarios()[0]["reviews"][0]["outcome"], "passed")
        self.assertEqual(len(self.store.scenarios()), 1)

    def test_generated_siblings_review_each_other_in_an_independent_lane(self):
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute(
                "INSERT INTO leaf VALUES(?,?,?,?,?)",
                ("another-task-type", "Other task", "另一任务", "tasks", "overview"),
            )
        batch = self.store.create_batch(
            {
                "kind": "scenarios",
                "name": "two leaves",
                "model": "fake/flash",
                "concurrency": 1,
                "leaves": ["task-management-application", "another-task-type"],
            }
        )
        generated = self.store.claim("producer", "production")
        drafts = [
            {**self.spec, "leaf": generated["snapshot"]["leaf"]["slug"], "name": name}
            for name in ("one", "two")
        ]
        self.store.complete_scenario_proposals(
            generated["id"], generated["token"], drafts
        )
        producing = self.store.claim("producer", "production")
        reviewing = self.store.claim("reviewer", "verification")
        self.assertIsNotNone(producing)
        self.assertEqual(len(reviewing["snapshot"]["peer_scenarios"]), 1)
        self.assertNotEqual(
            reviewing["snapshot"]["scenario"]["id"],
            reviewing["snapshot"]["peer_scenarios"][0]["id"],
        )
        self.assertEqual(len(self.store.batch(batch["id"])["jobs"]), 4)

    def batch(self, ids=None, **kwargs):
        return self.store.create_batch(
            {
                "name": "batch",
                "model": "fake/flash",
                "scenario_ids": ids or [self.scenario()["id"]],
                **kwargs,
            }
        )

    def test_plan_commands_must_exist_in_selected_image(self):
        scenario = self.scenario()
        for phase in ("install", "build", "tests"):
            with self.subTest(phase=phase), self.assertRaises(FactoryError) as error:
                validate_plan({**self.plan(), phase: [["npm", "install"]]}, scenario)
            self.assertEqual(error.exception.code, "plan_runtime_mismatch")

        node_plan = {
            **self.plan(),
            "profile": "node-web",
            "install": [["npm", "install"]],
            "build": [["npm", "run", "build"]],
            "start": ["npm", "run", "serve", "--", "--host", "0.0.0.0"],
        }
        self.assertEqual(validate_plan(node_plan, scenario)["profile"], "node-web")
        for plan in (
            {**node_plan, "start": ["python3", "-m", "http.server", "8080"]},
            {
                **self.plan(),
                "checks": [
                    {
                        "action": "command",
                        "argv": ["node", "--version"],
                        "contains": "v22",
                        "criterion": 0,
                    }
                ],
            },
        ):
            with self.assertRaises(FactoryError) as error:
                validate_plan(plan, scenario)
            self.assertEqual(error.exception.code, "plan_runtime_mismatch")

    def test_link_acceptance_requires_a_specific_http_target(self):
        check = {
            "action": "open_link",
            "selector": "article a",
            "url": "https://example.com/bookmark",
            "criterion": 0,
        }
        plan = {
            **self.plan(),
            "checks": [{"action": "goto", "path": "/", "criterion": 0}, check],
        }
        self.assertEqual(validate_plan(plan, self.scenario())["checks"][-1], check)
        for url in (
            None,
            "file:///etc/passwd",
            "javascript:alert(1)",
            "https://user:secret@example.com",
            "https:///missing-host",
        ):
            with self.subTest(url=url), self.assertRaises(FactoryError):
                validate_plan(
                    {**plan, "checks": [{**check, "url": url}]}, self.scenario()
                )

    def test_scenarios_have_revision_compare_and_swap(self):
        item = self.scenario()
        new = self.store.save_scenario(
            {**item, "name": "changed", "expected_revision": 1}, item["id"]
        )
        self.assertEqual(new["revision"], 2)
        with self.assertRaises(FactoryError):
            self.store.save_scenario({**item, "expected_revision": 1}, item["id"])
        with self.store.connect() as con:
            self.assertEqual(
                con.execute("SELECT count(*) FROM scenario_history").fetchone()[0], 2
            )

    def test_corpus_truth_and_confirmation_gate(self):
        with self.assertRaises(FactoryError):
            self.store.save_scenario({**self.spec, "leaf": "made-up"})
        item = self.store.save_scenario({**self.spec, "status": "draft"})
        with self.assertRaises(FactoryError):
            self.batch([item["id"]])

    def test_batch_pins_scenario_and_leaf(self):
        item = self.scenario()
        batch = self.batch([item["id"]])
        self.store.save_scenario(
            {**item, "name": "changed", "expected_revision": 1}, item["id"]
        )
        job = self.store.job(batch["jobs"][0]["id"])
        self.assertEqual(job["snapshot"]["scenario"]["name"], "每日待办")
        self.assertEqual(job["snapshot"]["scenario"]["revision"], 1)
        self.assertTrue(job["snapshot"]["leaf"]["fingerprint"])

    def test_atomic_claim_respects_concurrency(self):
        ids = [self.scenario()["id"] for _ in range(4)]
        self.batch(ids, concurrency=2)
        with ThreadPoolExecutor(max_workers=8) as pool:
            jobs = list(pool.map(lambda i: self.store.claim(str(i)), range(8)))
        self.assertEqual(len([j for j in jobs if j]), 2)
        self.assertEqual(len(set(j["id"] for j in jobs if j)), 2)

    def test_pause_resume_and_cancel_fence_late_worker(self):
        batch = self.batch()
        self.store.batch_action(batch["id"], "pause")
        self.assertIsNone(self.store.claim("a"))
        self.store.batch_action(batch["id"], "resume")
        job = self.store.claim("a")
        self.store.batch_action(batch["id"], "cancel")
        self.assertFalse(self.store.owned(job["id"], job["token"]))
        self.assertFalse(self.store.heartbeat(job["id"], job["token"]))
        with self.assertRaises(FactoryError):
            self.store.add_artifact(job["id"], job["token"], {"digest": "x"})
        with self.assertRaises(FactoryError):
            self.store.batch_action(batch["id"], "resume")

    def test_expired_lease_cannot_publish_or_renew(self):
        self.batch()
        job = self.store.claim("a")
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET lease=0 WHERE id=?", (job["id"],))
        self.assertFalse(self.store.heartbeat(job["id"], job["token"]))
        with self.assertRaises(FactoryError):
            self.store.update(job["id"], job["token"], "done", "late")

    def test_restart_marks_interrupted_and_explicit_retry_new_owner(self):
        self.batch()
        job = self.store.claim("old")
        self.assertEqual(self.store.recover(), 1)
        self.assertEqual(self.store.job(job["id"])["state"], "interrupted")
        retried = self.store.retry(job["id"])
        self.assertEqual(retried["attempt"], 2)
        newer = self.store.claim("new")
        self.assertNotEqual(newer["token"], job["token"])
        with self.assertRaises(FactoryError):
            self.store.update(job["id"], job["token"], "completed", "old")

    def test_nonterminal_job_cannot_retry(self):
        batch = self.batch()
        with self.assertRaises(FactoryError):
            self.store.retry(batch["jobs"][0]["id"])

    @staticmethod
    def plan():
        return {
            "profile": "static-web",
            "install": [],
            "build": [],
            "tests": [],
            "start": ["python3", "-m", "http.server", "8080", "--bind", "0.0.0.0"],
            "port": 8080,
            "checks": [
                {"action": "http", "path": "/", "contains": "todo", "criterion": 0}
            ],
        }

    def test_plan_requires_observable_coverage(self):
        scenario = self.scenario()
        plan = self.plan()
        self.assertEqual(
            validate_plan(plan, scenario)["parameter_checks"],
            ["atlas-example", "renamed-example"],
        )
        for checks in [
            [],
            [{"action": "click", "selector": "button", "criterion": 0}],
            [{"action": "http", "path": "//host/", "contains": "x", "criterion": 0}],
        ]:
            with self.subTest(checks=checks), self.assertRaises(FactoryError):
                validate_plan({**plan, "checks": checks}, scenario)

    def bundle(self):
        source = self.root / "source"
        source.mkdir()
        (source / "index.html").write_text("<h1>@@PROJECT_NAME@@ todo</h1>")
        (source / "LICENSE").write_text("MIT notice")
        bundle = self.root / "bundle"
        value = {"name": "Todo", "description": "todo", "render_files": ["index.html"]}
        freeze(
            source,
            bundle,
            value,
            validate_plan(self.plan(), self.scenario()),
            {"repository": "https://github.com/a/b"},
        )
        return bundle

    def test_deterministic_instantiation_and_parameter_validation(self):
        bundle = self.bundle()
        render_template(bundle, self.root / "one", "alpha")
        render_template(bundle, self.root / "two", "beta")
        self.assertIn("alpha", (self.root / "one/index.html").read_text())
        self.assertIn("beta", (self.root / "two/index.html").read_text())
        self.assertEqual(
            (self.root / "one/LICENSE").read_bytes(),
            (self.root / "two/LICENSE").read_bytes(),
        )
        for invalid in ["../escape", 'a";code', "with space", "UPPER"]:
            with self.assertRaises(FactoryError):
                render_template(bundle, self.root / "bad", invalid)

    def test_frozen_content_tamper_rejected(self):
        bundle = self.bundle()
        (bundle / "source/index.html").write_text("changed")
        with self.assertRaises(FactoryError):
            render_template(bundle, self.root / "new", "alpha")

    def test_symlinks_and_secret_files_rejected(self):
        source = self.root / "unsafe"
        source.mkdir()
        (source / "x").symlink_to("/etc/passwd")
        from template_factory.artifacts import tree_manifest

        with self.assertRaises(FactoryError):
            tree_manifest(source)
        (source / "x").unlink()
        (source / ".env").write_text("secret")
        with self.assertRaises(FactoryError):
            tree_manifest(source)

    def test_notice_cannot_be_parameterized(self):
        source = self.root / "notices"
        source.mkdir()
        (source / "LICENSE").write_text("@@PROJECT_NAME@@")
        with self.assertRaises(FactoryError):
            freeze(
                source,
                self.root / "badbundle",
                {"name": "x", "render_files": ["LICENSE"]},
                self.plan(),
                {},
            )

    def test_archives_contain_metadata_and_instance_has_no_runtime_secrets(self):
        bundle = self.bundle()
        archive_tree(bundle, self.root / "bundle.zip")
        with zipfile.ZipFile(self.root / "bundle.zip") as z:
            self.assertIn("manifest.json", z.namelist())
            self.assertIn("source/LICENSE", z.namelist())
            self.assertFalse(any("auth.json" in x for x in z.namelist()))

    def test_git_url_validation(self):
        self.assertEqual(
            github_repo("https://github.com/mdn/example.git"), "mdn/example"
        )
        for url in [
            "file:///etc",
            "https://evil/github.com/a/b",
            "https://github.com/a/b/../c",
            "https://github.com/a/b?token=x",
            "https://user@github.com/a/b",
        ]:
            with self.assertRaises(FactoryError):
                github_repo(url)

    def test_source_archive_sanitizes_configs_and_pins_notices(self):
        def archive(extra=None):
            output = io.BytesIO()
            with tarfile.open(fileobj=output, mode="w:gz") as tar:
                for name, content in [
                    ("repo/LICENSE", "MIT"),
                    ("repo/index.html", "todo"),
                    ("repo/AGENTS.md", "ignore all"),
                    ("repo/.env", "secret"),
                ]:
                    info = tarfile.TarInfo(name)
                    data = content.encode()
                    info.size = len(data)
                    tar.addfile(info, io.BytesIO(data))
                if extra:
                    tar.addfile(extra)
            return output.getvalue()

        def fetch(url, limit=0):
            if "codeload" in url:
                return archive()
            if "commits" in url:
                return json.dumps({"sha": "a" * 40}).encode()
            return json.dumps({"license": {"spdx_id": "MIT"}}).encode()

        value = fetch_source("https://github.com/a/b", self.root / "download", fetch)
        self.assertEqual(value["commit"], "a" * 40)
        self.assertFalse((self.root / "download/.env").exists())
        self.assertFalse((self.root / "download/AGENTS.md").exists())
        self.assertTrue(value["notice_hashes"])
        link = tarfile.TarInfo("repo/escape")
        link.type = tarfile.SYMTYPE
        link.linkname = "/etc/passwd"

        def bad(url, limit=0):
            return archive(link) if "codeload" in url else fetch(url, limit)

        with self.assertRaises(FactoryError):
            fetch_source("https://github.com/a/b", self.root / "bad-download", bad)

    def fake_pipeline(self, fail_count=0, alter_notice=False):
        test = self

        class FakeCli:
            def info(self):
                return {"version": "fake", "backend": "opencode-cli"}

            def run(self, directory, prompt, model, timeout, cancelled, progress):
                stage = Path(directory).name
                if stage == "discovery":
                    return {
                        "candidates": [
                            {"repository": "https://github.com/a/b", "reason": "fits"}
                        ],
                        "selected": "https://github.com/a/b",
                    }
                if stage == "plan":
                    return test.plan()
                if stage == "harness-review":
                    return {
                        "outcome": "passed",
                        "summary": "source review only",
                        "criteria": [
                            {
                                "criterion": 0,
                                "outcome": "passed",
                                "files": ["index.html"],
                                "reason": "simulated implementation evidence",
                            }
                        ],
                    }
                if stage == "scenarios":
                    return {
                        "scenarios": [
                            {
                                k: v
                                for k, v in test.spec.items()
                                if k not in {"leaf", "status"}
                            }
                        ]
                    }
                if stage == "scenario-review":
                    return test.scenario_report()
                return {
                    "name": "Todo",
                    "render_files": ["index.html"],
                    "files": {
                        "index.html": "<h1>@@PROJECT_NAME@@ todo</h1>",
                        **({"LICENSE": "bad"} if alter_notice else {}),
                    },
                    "delete_files": [],
                }

        class FakeVerifier:
            def __init__(self):
                self.failures = fail_count

            def verify(self, app, plan, evidence, *args, baseline=False):
                if not baseline and self.failures:
                    self.failures -= 1
                    return {
                        "passed": False,
                        "steps": [{"passed": False, "output": "failed"}],
                    }
                return {
                    "passed": True,
                    "steps": [{"passed": True}],
                    "environment": {"platform": "simulated", "image": "fake"},
                }

        def fetcher(repo, dest):
            Path(dest).mkdir()
            (Path(dest) / "index.html").write_text("todo")
            (Path(dest) / "LICENSE").write_text("MIT")
            return {
                "repository": repo,
                "commit": "a" * 40,
                "license": "MIT",
                "notice_hashes": {"LICENSE": hashlib.sha256(b"MIT").hexdigest()},
            }

        return Pipeline(self.store, FakeCli(), FakeVerifier(), fetcher)

    def test_literal_repair_changes_only_a_unique_match(self):
        self.batch()
        pipeline = self.fake_pipeline()
        original_run = pipeline.cli.run

        def replacement_result(directory, *args):
            result = original_run(directory, *args)
            if Path(directory).name.startswith("generate"):
                result["files"] = {}
                result["replacements"] = [
                    {
                        "path": "index.html",
                        "old": "todo",
                        "new": "<h1>@@PROJECT_NAME@@ todo</h1>",
                    }
                ]
            return result

        pipeline.cli.run = replacement_result
        pipeline.run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        bundle = self.store.root / artifact["bundle_path"]
        self.assertEqual(
            (bundle / "source/index.html").read_text(), "<h1>@@PROJECT_NAME@@ todo</h1>"
        )
        self.assertEqual((bundle / "source/LICENSE").read_text(), "MIT")

        for changes, files in (
            ([{"path": "index.html", "old": "not-present", "new": "x"}], {}),
            (
                [
                    {"path": "index.html", "old": "o", "new": "x"},
                ],
                {},
            ),
            ([{"path": "LICENSE", "old": "MIT", "new": "bad"}], {}),
            (
                [{"path": "index.html", "old": "todo", "new": "x"}],
                {"index.html": "todo"},
            ),
        ):
            with self.subTest(changes=changes):
                self.batch()
                p = self.fake_pipeline()
                run = p.cli.run

                def conflict_result(directory, *args):
                    result = run(directory, *args)
                    if Path(directory).name.startswith("generate"):
                        result.update(files=files, replacements=changes)
                    return result

                p.cli.run = conflict_result
                with self.assertRaises(FactoryError):
                    p.run(self.store.claim("test"))
                self.assertEqual(len(self.store.artifacts()), 1)

    def test_full_pipeline_and_explicit_publication(self):
        self.batch()
        job = self.store.claim("test")
        self.fake_pipeline().run(job)
        self.assertEqual(self.store.job(job["id"])["state"], "completed")
        artifact = self.store.artifacts()[0]
        self.assertEqual((artifact["level"], artifact["state"]), ("L0", "draft"))
        with self.assertRaises(FactoryError):
            self.store.artifact_action(
                artifact["id"],
                {
                    "action": "publish",
                    "review": "reviewed",
                    "expected_digest": artifact["digest"],
                },
            )
        self.accept_artifact(artifact, "harness-review")
        artifact = self.store.artifacts()[0]
        self.assertEqual(artifact["level"], "L1")
        published = self.store.artifact_action(
            artifact["id"],
            {
                "action": "publish",
                "review": "reviewed",
                "expected_digest": artifact["digest"],
            },
        )
        self.assertEqual(published["state"], "published")
        with self.assertRaises(FactoryError):
            self.store.artifact_action(
                artifact["id"],
                {
                    "action": "publish",
                    "review": "reviewed",
                    "level": "L3",
                    "expected_digest": artifact["digest"],
                },
            )

    def accept_artifact(self, artifact, method, pipeline=None):
        self.store.create_acceptance(
            artifact["id"], {"method": method, "expected_digest": artifact["digest"]}
        )
        job = self.store.claim("test", "verification")
        (pipeline or self.fake_pipeline()).run(job)
        return job

    def test_production_does_not_call_docker(self):
        self.batch()
        job = self.store.claim("test")
        pipeline = self.fake_pipeline()
        pipeline.verifier.verify = lambda *_args, **_kwargs: (_ for _ in ()).throw(
            AssertionError("production must not execute candidate code")
        )
        pipeline.run(job)
        self.assertEqual(self.store.job(job["id"])["state"], "completed")
        self.assertEqual(self.store.artifacts()[0]["reports"], [])
        self.assertEqual(len(self.store.artifacts()[0]["formal_checks"]), 2)

    def test_failed_acceptance_keeps_produced_candidate_and_does_not_block_production(
        self,
    ):
        self.batch()
        produced = self.store.claim("test")
        self.fake_pipeline().run(produced)
        artifact = self.store.artifacts()[0]
        acceptance = self.accept_artifact(
            artifact, "runtime-verification", self.fake_pipeline(fail_count=1)
        )
        self.assertEqual(self.store.job(acceptance["id"])["state"], "needs_review")
        self.assertEqual(self.store.job(produced["id"])["state"], "completed")
        self.assertEqual(self.store.artifacts()[0]["level"], "L0")
        self.batch()
        self.assertIsNotNone(self.store.claim("next", "production"))

    def test_explicit_repair_creates_new_immutable_artifact(self):
        self.batch()
        produced = self.store.claim("test")
        self.fake_pipeline().run(produced)
        artifact = self.store.artifacts()[0]
        self.accept_artifact(
            artifact, "runtime-verification", self.fake_pipeline(fail_count=1)
        )
        self.store.create_repair(
            artifact["id"],
            {"expected_digest": artifact["digest"], "note": "fix observed behavior"},
        )
        job = self.store.claim("test", "production")
        pipeline = self.fake_pipeline()
        pipeline.fetcher = lambda *_: (_ for _ in ()).throw(
            AssertionError("repair must use frozen source")
        )
        original_run = pipeline.cli.run

        def reject_replanning(directory, *args):
            self.assertNotEqual(Path(directory).name, "plan")
            return original_run(directory, *args)

        pipeline.cli.run = reject_replanning
        pipeline.run(job)
        artifacts = self.store.artifacts()
        self.assertEqual(len(artifacts), 2)
        self.assertEqual(artifacts[0]["supersedes"], artifact["id"])
        self.assertEqual(artifacts[1]["digest"], artifact["digest"])
        self.assertEqual(artifacts[0]["plan"], artifact["plan"])

    def test_repair_plan_changes_require_an_explicit_option(self):
        self.batch()
        self.fake_pipeline().run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        request = {"expected_digest": artifact["digest"], "note": "fix runtime plan"}
        with self.assertRaises(FactoryError):
            self.store.create_repair(artifact["id"], {**request, "replan": "false"})
        self.store.create_repair(artifact["id"], {**request, "replan": True})
        job = self.store.claim("test", "production")
        self.assertEqual(job["snapshot"]["repair_artifact"]["plan"], artifact["plan"])
        pipeline = self.fake_pipeline()
        original_run = pipeline.cli.run

        def changed_plan(directory, *args):
            if Path(directory).name == "plan":
                return {**self.plan(), "port": 8090}
            return original_run(directory, *args)

        pipeline.cli.run = changed_plan
        pipeline.run(job)
        self.assertEqual(self.store.artifacts()[0]["plan"]["port"], 8090)
        self.assertEqual(self.store.artifacts()[1]["plan"], artifact["plan"])

    def test_verification_lane_and_production_lane_are_independent(self):
        self.batch()
        produced = self.store.claim("test", "production")
        self.fake_pipeline().run(produced)
        artifact = self.store.artifacts()[0]
        self.store.create_acceptance(
            artifact["id"],
            {"method": "harness-review", "expected_digest": artifact["digest"]},
        )
        self.batch()
        review = self.store.claim("review", "verification")
        production = self.store.claim("produce", "production")
        self.assertEqual(review["kind"], "harness-review")
        self.assertEqual(production["kind"], "production")
        with self.assertRaises(FactoryError):
            self.store.create_acceptance(
                artifact["id"],
                {"method": "harness-review", "expected_digest": artifact["digest"]},
            )

    def test_runtime_unavailable_is_recorded_and_harness_acceptance_can_pass(self):
        self.batch()
        self.fake_pipeline().run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        pipeline = self.fake_pipeline()

        def unavailable(*args, **kwargs):
            raise FactoryError("Docker unavailable", "runtime_unavailable", 503)

        pipeline.verifier.verify = unavailable
        self.accept_artifact(artifact, "runtime-verification", pipeline)
        self.accept_artifact(artifact, "harness-review")
        updated = self.store.artifacts()[0]
        self.assertEqual(
            {r["outcome"] for r in updated["acceptances"]}, {"passed", "unavailable"}
        )
        self.assertEqual(updated["level"], "L1")
        self.assertTrue(
            all(r["digest"] == artifact["digest"] for r in updated["acceptances"])
        )

    def test_scheduler_runs_acceptance_while_production_waits(self):
        from template_factory.worker import run

        self.batch()
        self.fake_pipeline().run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        self.batch()
        self.store.create_acceptance(
            artifact["id"],
            {"method": "harness-review", "expected_digest": artifact["digest"]},
        )
        started = threading.Event()
        reviewed = threading.Event()
        release = threading.Event()
        stop = threading.Event()

        class WaitingPipeline:
            def run(_, job):
                if job["kind"] == "production":
                    started.set()
                    release.wait(10)
                else:
                    started.wait(5)
                    reviewed.set()

        thread = threading.Thread(
            target=run, args=(self.store, stop, WaitingPipeline())
        )
        with patch("template_factory.worker.stop_orphans"):
            thread.start()
            try:
                self.assertTrue(started.wait(5))
                self.assertTrue(
                    reviewed.wait(5),
                    "acceptance must run while production remains active",
                )
            finally:
                stop.set()
                release.set()
                thread.join(10)
        self.assertFalse(thread.is_alive())

    def test_review_only_plan_can_be_produced_without_runtime(self):
        plan = validate_plan(
            {
                "profile": "review-only",
                "reason": "Native GUI requires a desktop runtime",
            },
            self.scenario(),
        )
        self.assertEqual(plan["checks"], [])
        from template_factory.runtime import DockerVerifier

        with self.assertRaises(FactoryError) as raised:
            DockerVerifier().verify(self.root, plan, self.root / "evidence")
        self.assertEqual(raised.exception.code, "runtime_unavailable")

    def test_provider_review_failure_is_visible_without_failing_production(self):
        self.batch()
        produced = self.store.claim("test")
        self.fake_pipeline().run(produced)
        artifact = self.store.artifacts()[0]
        pipeline = self.fake_pipeline()

        def disconnected(*args, **kwargs):
            raise FactoryError("provider connection reset", "cli_failed", 409)

        pipeline.cli.run = disconnected
        with self.assertRaises(FactoryError):
            self.accept_artifact(artifact, "harness-review", pipeline)
        value = self.store.artifacts()[0]
        self.assertEqual(value["acceptances"][0]["outcome"], "unavailable")
        self.assertEqual(self.store.job(produced["id"])["state"], "completed")
        self.assertEqual(value["level"], "L0")

    def test_cancelled_acceptance_cannot_publish_late_evidence(self):
        self.batch()
        self.fake_pipeline().run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        b = self.store.create_acceptance(
            artifact["id"],
            {"method": "harness-review", "expected_digest": artifact["digest"]},
        )
        job = self.store.claim("test", "verification")
        self.store.batch_action(b["id"], "cancel")
        with self.assertRaises(FactoryError):
            self.store.complete_acceptance(
                job["id"], job["token"], {"outcome": "passed"}
            )
        self.assertEqual(self.store.artifacts()[0]["acceptances"], [])

    def test_leaf_only_lists_its_published_templates(self):
        self.batch()
        self.fake_pipeline().run(self.store.claim("test"))
        artifact = self.store.artifacts()[0]
        values, status = dispatch(
            "GET",
            "/api/factory/artifacts",
            query="leaf=task-management-application&published=1",
            store=self.store,
        )
        self.assertEqual(values, [])
        self.accept_artifact(artifact, "harness-review")
        self.store.artifact_action(
            artifact["id"],
            {
                "action": "publish",
                "expected_digest": artifact["digest"],
                "review": "reviewed",
                "level": "L2",
            },
        )
        values, status = dispatch(
            "GET",
            "/api/factory/artifacts",
            query="leaf=task-management-application&published=1",
            store=self.store,
        )
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0]["level"], "L2")
        values, status = dispatch(
            "GET",
            "/api/factory/artifacts",
            query="leaf=another-type&published=1",
            store=self.store,
        )
        self.assertEqual(values, [])

    def test_retry_reuses_source_checkpoint_after_failed_generation(self):
        self.batch()
        job = self.store.claim("test")
        with self.assertRaises(FactoryError):
            self.fake_pipeline(alter_notice=True).run(job)
        self.store.retry(job["id"])
        pipeline = self.fake_pipeline()
        pipeline.fetcher = lambda *_: (_ for _ in ()).throw(
            AssertionError("source should be reused")
        )
        pipeline.run(self.store.claim("retry"))
        self.assertEqual(self.store.job(job["id"])["state"], "completed")

    def test_agent_cannot_remove_licenses(self):
        self.batch()
        job = self.store.claim("test")
        with self.assertRaises(FactoryError):
            self.fake_pipeline(alter_notice=True).run(job)
        self.assertEqual(self.store.artifacts(), [])

    def test_cli_final_json_can_follow_assistant_preamble(self):
        self.assertEqual(
            parse_result('I will inspect the source.\n{"files": {"app.js":"code"}}'),
            {"files": {"app.js": "code"}},
        )

    def test_cli_protocol_not_zero_exit_success(self):
        for content in [
            "not json",
            "[]",
            '{"type":"text","part":{"text":"hello"}}\n{"type":"end"}',
        ]:
            with self.assertRaises(FactoryError):
                parse_result(content)
        self.assertEqual(parse_result('```json\n{"files":{}}\n```'), {"files": {}})

    def test_factory_api_instantiates_without_model_call_and_no_host_path(self):
        self.batch()
        job = self.store.claim("test")
        self.fake_pipeline().run(job)
        artifact = self.store.artifacts()[0]
        result, status = dispatch(
            "POST",
            f"/api/factory/artifacts/{artifact['id']}/instantiate",
            body={"project_name": "new-app"},
            store=self.store,
        )
        self.assertEqual(status, 201)
        file, _, _ = dispatch("GET", result["download_url"], store=self.store)
        with zipfile.ZipFile(file) as z:
            self.assertIn("new-app", z.read("index.html").decode())
        with self.assertRaises(FactoryError):
            dispatch(
                "POST",
                f"/api/factory/artifacts/{artifact['id']}/instantiate",
                body={"project_name": "../../outside"},
                store=self.store,
            )

    def test_scenario_discovery_creates_drafts_not_production_jobs(self):
        self.store.create_batch(
            {
                "kind": "scenarios",
                "name": "discover",
                "leaves": ["task-management-application"],
                "model": "fake/flash",
            }
        )
        job = self.store.claim("test")
        self.fake_pipeline().run(job)
        self.assertEqual(self.store.scenarios()[0]["status"], "draft")
        self.assertEqual(self.store.artifacts(), [])


class CliProcessTests(unittest.TestCase):
    def test_explicit_deepseek_effort_is_scoped_to_one_cli_v2_invocation(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
            cli = CLI(str(executable))
            cli.run(
                work,
                "review",
                "test/deepseek-flash",
                10,
                lambda: False,
                lambda _: None,
                reasoning_effort="low",
            )
            config = json.loads((work / "opencode.json").read_text())
            variant = config["providers"]["test"]["models"]["deepseek-flash"][
                "variants"
            ][0]
            self.assertEqual(variant["body"], {"reasoning_effort": "low"})
            summary = json.loads((work / "cli-summary.json").read_text())
            self.assertEqual(summary["model"], "test/deepseek-flash#atlas-effort-low")
            self.assertEqual(summary["requested_model"], "test/deepseek-flash")
            self.assertEqual(summary["reasoning_effort"], "low")
            # A subsequent ordinary call keeps provider defaults.
            cli.run(
                work,
                "ordinary",
                "test/deepseek-flash",
                10,
                lambda: False,
                lambda _: None,
            )
            config = json.loads((work / "opencode.json").read_text())
            self.assertNotIn("providers", config)
            for model, effort in (
                ("test/other", "low"),
                ("test/deepseek-flash#high", "low"),
                ("test/deepseek-flash", "none"),
            ):
                with self.assertRaises(FactoryError):
                    cli.run(
                        work,
                        "review",
                        model,
                        10,
                        lambda: False,
                        lambda _: None,
                        reasoning_effort=effort,
                    )

    def test_scenario_reviewer_cannot_search_or_fetch_external_content(self):
        from template_factory.cli import CLI

        for major in (1, 2):
            with self.subTest(major=major), tempfile.TemporaryDirectory() as root:
                executable, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
                target = work.with_name("scenario-review")
                work.rename(target)
                with patch(
                    "template_factory.cli.detect_opencode_major_version",
                    return_value=major,
                ):
                    CLI(str(executable)).run(
                        target,
                        "review",
                        "fake/flash",
                        30,
                        lambda: False,
                        lambda _: None,
                    )
                config = json.loads((target / "opencode.json").read_text())
                if major == 2:
                    for resource in ("leaf.md", str(target.resolve() / "leaf.md")):
                        self.assertIn(
                            {"action": "read", "resource": resource, "effect": "allow"},
                            config["permissions"],
                        )
                    self.assertFalse(
                        any(
                            rule["action"] in {"websearch", "webfetch"}
                            and rule["effect"] == "allow"
                            for rule in config["permissions"]
                        )
                    )
                else:
                    self.assertEqual(config["permission"]["read"]["leaf.md"], "allow")
                    self.assertEqual(config["permission"]["websearch"], "deny")
                    self.assertEqual(config["permission"]["webfetch"], {"*": "deny"})

    def test_cognition_stages_cannot_search_or_fetch_external_content(self):
        from template_factory.cli import CLI

        for major, stage in (
            (1, "cognitive-review"),
            (2, "cognitive-review"),
            (1, "cognitive-review-reference-repair"),
            (2, "cognitive-review-reference-repair"),
            (1, "blueprint-generate-0"),
            (2, "blueprint-generate-0"),
            (1, "blueprint-code-0-0"),
            (2, "blueprint-code-0-0"),
            (1, "blueprint-spec-review-0"),
            (2, "blueprint-spec-review-0"),
        ):
            with (
                self.subTest(major=major, stage=stage),
                tempfile.TemporaryDirectory() as root,
            ):
                executable, work = self.fake(root, 'print(json.dumps({"ok": True}))\n')
                target = work.with_name(stage)
                work.rename(target)
                with patch(
                    "template_factory.cli.detect_opencode_major_version",
                    return_value=major,
                ):
                    CLI(str(executable)).run(
                        target,
                        "review",
                        "fake/flash",
                        30,
                        lambda: False,
                        lambda _: None,
                    )
                config = json.loads((target / "opencode.json").read_text())
                if major == 2:
                    for resource in (
                        "leaf.md",
                        str(target.resolve() / "leaf.md"),
                        "source/**",
                        str(target.resolve() / "source/**"),
                    ):
                        self.assertIn(
                            {"action": "read", "resource": resource, "effect": "allow"},
                            config["permissions"],
                        )
                    self.assertFalse(
                        any(
                            rule["action"] in {"websearch", "webfetch"}
                            and rule["effect"] == "allow"
                            for rule in config["permissions"]
                        )
                    )
                else:
                    self.assertEqual(config["permission"]["read"]["leaf.md"], "allow")
                    self.assertEqual(config["permission"]["read"]["source/**"], "allow")
                    self.assertEqual(config["permission"]["websearch"], "deny")
                    self.assertEqual(config["permission"]["webfetch"], {"*": "deny"})

    def test_cognition_output_length_stops_before_continuation(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(
                root,
                'print(json.dumps({"type":"step_finish","part":{"reason":"length"}}),flush=True)\ntime.sleep(10)\n',
            )
            target = work.with_name("blueprint-code-0-0")
            work.rename(target)
            with self.assertRaises(FactoryError) as found:
                CLI(str(executable)).run(
                    target,
                    "write one file",
                    "fake/flash",
                    2,
                    lambda: False,
                    lambda _: None,
                )
            self.assertEqual(found.exception.code, "cli_output_truncated")
            self.assertTrue((target / "events.jsonl").exists())

    def test_cognition_framing_accepts_only_complete_objects_with_extra_closing(self):
        from template_factory.cli import parse_result

        self.assertEqual(
            parse_result(
                'Prose\n{"spec":{"a":1},"file_plan":[]}}', redundant_closing=True
            ),
            {"spec": {"a": 1}, "file_plan": []},
        )
        for invalid in (
            '{"spec":{"a":1}',
            '{"a":1} unrelated',
            '{"a":1}{"b":2} trailing',
        ):
            with self.assertRaises(FactoryError):
                parse_result(invalid, redundant_closing=True)

    def test_cognitive_framing_recovery_never_fills_missing_data_or_changes_strings(
        self,
    ):
        from template_factory.cli import recover_cognitive_framing

        result, evidence = recover_cognitive_framing(
            '{"summary":"keep ]} verbatim","checks":[],"suggestions":["x"]]}'
        )
        self.assertEqual(
            result, {"summary": "keep ]} verbatim", "checks": [], "suggestions": ["x"]}
        )
        self.assertEqual(len(evidence["removed_positions"]), 1)
        for invalid in (
            '{"a":[1}}',
            '{"a":"unfinished}',
            '{"a":1]]} trailing',
            '{"a":1}{"b":2]}',
        ):
            with self.assertRaises(FactoryError):
                recover_cognitive_framing(invalid)

    def test_cognitive_framing_tolerates_only_known_provider_closing_markers(self):
        from template_factory.cli import recover_cognitive_framing

        content = '{"path":"acceptance/x.cjs","content":"const literal = \'</｜｜DSML｜｜ calls>\';"}'
        value, evidence = recover_cognitive_framing(
            content
            + "</｜｜DSML｜｜ parameter>\n</｜｜DSML｜｜ invoke>\n</｜｜DSML｜｜ calls>"
        )
        self.assertEqual(value, json.loads(content))
        self.assertEqual(evidence["method"], "remove-known-dsml-closing-markers-only")
        with self.assertRaises(FactoryError):
            recover_cognitive_framing(content + "</unknown>")

    def test_cognitive_plan_recovers_premature_spec_closer_without_value_changes(self):
        from template_factory.cli import recover_cognitive_framing

        spec = {
            "title": '保留原值 } ,"limits": [ Unicode',
            "roles": [],
            "features": [],
            "decisions": [],
            "phases": [],
            "acceptance": [],
            "architecture_markdown": '引号 " 与换行\n原样保留',
        }
        limits = ["not run", {"nested": ["}]"]}]
        files = [{"path": "acceptance/a.cjs", "purpose": "unchanged order"}]
        broken = json.dumps({"spec": spec, "limits": limits}, ensure_ascii=False)
        continuation = ', "file_plan": ' + json.dumps(files) + "}"
        result, evidence = recover_cognitive_framing(broken + continuation)
        self.assertEqual(
            result,
            {
                "spec": {**spec, "limits": limits},
                "file_plan": files,
            },
        )
        self.assertEqual(evidence["method"], "remove-one-premature-spec-closer")
        self.assertEqual(len(evidence["removed_positions"]), 1)

        # Ambiguity, incomplete values and extra objects remain errors rather
        # than guesses about what the author intended.
        for invalid in (
            broken + continuation + '{"another": true}',
            broken + continuation[:-2],
            broken + ', "files": []}',
            broken + ', "file_plan": {}}',
            json.dumps({"spec": {**spec, "limits": []}, "limits": limits})
            + continuation,
            json.dumps({"spec": {"title": "missing fields"}, "limits": []})
            + continuation,
        ):
            with self.subTest(invalid=invalid):
                with self.assertRaises(FactoryError):
                    recover_cognitive_framing(invalid)

    def fake(self, root, body):
        executable = Path(root) / "opencode-test"
        executable.write_text(
            '#!/usr/bin/env python3\nimport sys,json,time\nif "--version" in sys.argv:\n print("2.0.26");sys.exit(0)\n'
            + body
        )
        executable.chmod(0o700)
        work = Path(root) / "work"
        work.mkdir()
        (work / "input.json").write_text('{"test":true}')
        return executable, work

    def test_reads_real_jsonl_stream_and_final_line_without_newline(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(
                root,
                'print(json.dumps({"type":"text","part":{"text":"{\\"ok\\":true}"}}),end="")\n',
            )
            value = CLI(str(executable)).run(
                work, "probe", "fake/flash", 10, lambda: False, lambda _: None
            )
            self.assertEqual(value, {"ok": True})
            self.assertTrue((work / "cli-summary.json").is_file())
            policy = json.loads((work / "opencode.json").read_text())
            self.assertEqual(
                policy["permissions"][0],
                {"action": "*", "resource": "*", "effect": "deny"},
            )

    def test_zero_exit_error_event_is_failure(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(
                root,
                'print(json.dumps({"type":"error","error":"provider unavailable"}))\n',
            )
            with self.assertRaises(FactoryError):
                CLI(str(executable)).run(
                    work, "probe", "fake/flash", 10, lambda: False, lambda _: None
                )

    def test_error_without_final_newline_overrides_prior_valid_text(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(
                root,
                'print(json.dumps({"type":"text","part":{"text":"{\\"ok\\":true}"}}))\nprint(json.dumps({"type":"error","error":"provider reset"}),end="")\n',
            )
            with self.assertRaises(FactoryError) as raised:
                CLI(str(executable)).run(
                    work, "probe", "fake/flash", 10, lambda: False, lambda _: None
                )
            self.assertEqual(raised.exception.code, "cli_failed")
            self.assertIn("provider reset", str(raised.exception))

    def test_cancel_terminates_owned_process_group(self):
        from template_factory.cli import CLI

        with tempfile.TemporaryDirectory() as root:
            executable, work = self.fake(root, "time.sleep(90)\n")
            with self.assertRaises(FactoryError):
                CLI(str(executable)).run(
                    work, "probe", "fake/flash", 10, lambda: True, lambda _: None
                )
            self.assertIsNone(json.loads((work / "process.json").read_text())["pid"])


if __name__ == "__main__":
    unittest.main()
