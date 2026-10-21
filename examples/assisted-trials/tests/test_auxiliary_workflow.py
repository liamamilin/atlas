"""Durable workflow fixtures; no provider or production database access."""

import hashlib
import json
import tempfile
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parents[2] / "application-atlas-production-pack"))
from template_factory.auxiliary_workflow import WorkflowService, STEPS  # noqa: E402
from template_factory.store import FactoryError, FactoryStore  # noqa: E402
from template_factory.full_auxiliary import FullAuxiliaryService, MODEL  # noqa: E402


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        self.store = FactoryStore(self.pack / "state", self.pack)
        self.now = [1000.0]
        self.service = FullAuxiliaryService(self.store, "fixture", lambda: self.now[0])
        (self.root / "auth.txt").write_text("fixture authorization")
        scope = {
            "full_plan_id": "p",
            "items": [{"leaf": f"leaf-{n}", "covered": []} for n in range(200)],
        }
        (self.root / "scope.json").write_text(json.dumps(scope))
        self.request = {
            "schema": "atlas.full-leaf-auxiliary-authorization.v1",
            "full_plan_id": "p",
            "campaign_id": "fixture",
            "phase": "auxiliary-full-p",
            "baseline": 0,
            "max_new_calls": 7200,
            "per_leaf_calls": 6,
            "concurrency": 2,
            "batch_size": 20,
            "window_seconds": 2592000,
            "model": MODEL,
            "scope": {
                "path": "scope.json",
                "sha256": hashlib.sha256(
                    (self.root / "scope.json").read_bytes()
                ).hexdigest(),
            },
            "authorization": {
                "path": "auth.txt",
                "sha256": hashlib.sha256(
                    (self.root / "auth.txt").read_bytes()
                ).hexdigest(),
            },
        }
        self.service.register(self.request)
        self.workflow = WorkflowService(self.store, "fixture", lambda: self.now[0])

    def test_durable_steps_digest_outputs_order_retry_and_idempotency(self):
        h = hashlib.sha256(b"input").hexdigest()
        with self.assertRaises(FactoryError):
            self.workflow.begin("p", "leaf-0", "a1", "scenario", h)
        self.assertTrue(self.workflow.begin("p", "leaf-0", "a1", STEPS[0], h))
        artifact = self.root / "result.json"
        artifact.write_text("stable")
        out = [{"path": "result.json", "sha256": hashlib.sha256(b"stable").hexdigest()}]
        self.workflow.complete("p", "leaf-0", "a1", STEPS[0], out)
        self.assertFalse(self.workflow.begin("p", "leaf-0", "a1", STEPS[0], h))
        before = self.store.path.stat().st_size
        self.workflow.complete("p", "leaf-0", "a1", STEPS[0], out)
        self.assertEqual(before, self.store.path.stat().st_size)
        with self.assertRaises(FactoryError):
            self.workflow.begin(
                "p", "leaf-0", "a1", STEPS[0], hashlib.sha256(b"changed").hexdigest()
            )
        artifact.write_text("tampered")
        with self.assertRaises(FactoryError) as cm:
            self.workflow.begin("p", "leaf-0", "a1", STEPS[0], h)
        self.assertEqual(cm.exception.code, "workflow_integrity")
        with self.assertRaises(FactoryError):
            self.workflow.complete("p", "leaf-0", "a1", STEPS[0], [])
        with self.assertRaises(FactoryError):
            self.workflow.complete(
                "p",
                "leaf-0",
                "a1",
                STEPS[0],
                [{"path": "../outside", "sha256": "a" * 64}],
            )

    def test_output_file_is_scoped_and_detail_derives_output_url(self):
        digest = hashlib.sha256(b"artifact").hexdigest()
        self.workflow.begin("p", "leaf-0", "view1", STEPS[0], digest)
        artifact = self.root / "view.json"
        artifact.write_text('{"ok":true}')
        output = {
            "path": artifact.name,
            "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
        }
        self.workflow.complete("p", "leaf-0", "view1", STEPS[0], [output])

        path, filename, content_type = self.workflow.output_file(
            "p", "leaf-0", "view1", STEPS[0], 0
        )
        self.assertEqual(path, artifact.resolve())
        self.assertEqual(filename, "view.json")
        self.assertEqual(content_type, "text/plain;charset=utf-8")
        detail = self.workflow.detail("p", q="leaf-0")
        step = detail["items"][0]["steps"][0]
        self.assertEqual(
            step["outputs"][0]["url"],
            "/api/factory/auxiliary-workflows/p/leaves/leaf-0/steps/view1/existing_template/outputs/0",
        )
        with self.assertRaises(FactoryError) as cm:
            self.workflow.output_file("p", "leaf-0", "view1", STEPS[0], 1)
        self.assertEqual(cm.exception.status, 404)
        with self.assertRaises(FactoryError) as cm:
            self.workflow.output_file("p", "not-frozen", "view1", STEPS[0], 0)
        self.assertEqual(cm.exception.code, "workflow_binding")
        artifact.write_text("changed")
        with self.assertRaises(FactoryError) as cm:
            self.workflow.output_file("p", "leaf-0", "view1", STEPS[0], 0)
        self.assertEqual(cm.exception.code, "workflow_integrity")

    def test_running_replay_does_not_append_events_and_empty_failure_binds_digest(self):
        h = hashlib.sha256(b"late-bound").hexdigest()
        self.workflow.fail("p", "leaf-0", "a2", STEPS[0], "failed", "before begin")
        self.assertTrue(self.workflow.begin("p", "leaf-0", "a2", STEPS[0], h))
        with self.store.connect() as con:
            count = con.execute(
                "SELECT count(*) FROM auxiliary_workflow_event WHERE plan_id='p'"
            ).fetchone()[0]
        self.workflow.begin("p", "leaf-0", "a2", STEPS[0], h)
        with self.store.connect() as con:
            self.assertEqual(
                count,
                con.execute(
                    "SELECT count(*) FROM auxiliary_workflow_event WHERE plan_id='p'"
                ).fetchone()[0],
            )

    def test_failure_retry_and_paginated_read_has_real_steps_and_calls(self):
        h = hashlib.sha256(b"x").hexdigest()
        self.workflow.begin("p", "leaf-0", "try1", STEPS[0], h)
        self.workflow.fail("p", "leaf-0", "try1", STEPS[0], "fixture_error", "broken")
        self.assertTrue(self.workflow.begin("p", "leaf-0", "try1", STEPS[0], h))
        data = self.workflow.detail("p", offset=0, limit=1, state="pending", q="leaf-0")
        self.assertEqual(data["pagination"]["total"], 1)
        self.assertEqual(data["items"][0]["steps"][0]["state"], "running")
        self.assertEqual(data["items"][0]["calls"], [])
        self.assertEqual(data["items"][0]["steps"][0]["attempt"], "try1")
        self.assertEqual(data["items"][0]["steps"][0]["started"], 1000.0)
        self.assertEqual(data["plan"]["gate"], None)

    def test_validation_gate_requires_actual_fresh_ready_download(self):
        self.service.control("p", "pause")
        self.assertEqual(
            self.workflow.set_validation("p", ["leaf-0"])["status"], "ready"
        )
        evidence = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
            "fresh_ready_leaves": ["leaf-0"],
        }
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", evidence)
        self.assertEqual(
            self.workflow.set_validation("p", ["leaf-0"])["status"], "ready"
        )
        with self.assertRaises(FactoryError):
            self.workflow.set_validation("p", ["leaf-1"])

    def _complete_fresh_workflow(
        self, leaf="leaf-0", attempt="fresh1", mark_ready=True
    ):
        outputs = []
        self.now[0] += 1
        for index, step in enumerate(STEPS):
            input_digest = hashlib.sha256(step.encode()).hexdigest()
            self.assertTrue(self.workflow.begin("p", leaf, attempt, step, input_digest))
            path = self.root / f"{leaf}-{index}.json"
            payload = f"{leaf}:{step}".encode()
            path.write_bytes(payload)
            output = {
                "path": path.name,
                "sha256": hashlib.sha256(payload).hexdigest(),
            }
            outputs.append(path)
            self.workflow.complete("p", leaf, attempt, step, [output])
        if mark_ready:
            self.service.update_leaf(
                "p",
                leaf,
                "ready_not_run",
                {"validation_fixture": True, "current_attempt": attempt},
            )
        return outputs

    def test_passed_gate_requires_real_ready_leaf_and_is_immutable_idempotently(self):
        self.service.control("p", "pause")
        gate = self.workflow.set_validation("p", ["leaf-0"])
        self.assertEqual(gate["initial_states"], {"leaf-0": "pending"})
        outputs = self._complete_fresh_workflow()
        evidence = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
            "fresh_ready_leaves": ["leaf-0"],
        }
        passed = self.workflow.set_gate_passed("p", evidence)
        self.assertEqual(passed["status"], "passed")
        self.assertEqual(self.workflow.set_gate_passed("p", evidence), passed)
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", {**evidence, "replay_new_calls": 1})
        outputs[0].unlink()
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", evidence)

    def test_gate_rejects_pending_member_outside_fresh_ready_subset(self):
        self.service.control("p", "pause")
        self.workflow.set_validation("p", ["leaf-0", "leaf-1"])
        self._complete_fresh_workflow("leaf-0", attempt="fresh1")
        evidence = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
            "fresh_ready_leaves": ["leaf-0"],
        }
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", evidence)
        self.assertEqual(self.workflow.gate("p")["status"], "ready")

    def test_gate_rejects_download_attempt_different_from_current_attempt(self):
        self.service.control("p", "pause")
        self.workflow.set_validation("p", ["leaf-0"])
        self._complete_fresh_workflow(
            "leaf-0", attempt="workflow-attempt", mark_ready=False
        )
        self.service.update_leaf(
            "p", "leaf-0", "ready_not_run", {"current_attempt": "leaf-attempt"}
        )
        evidence = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
            "fresh_ready_leaves": ["leaf-0"],
        }
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", evidence)
        self.assertEqual(self.workflow.gate("p")["status"], "ready")

    def test_preexisting_ready_replay_is_not_fresh_validation(self):
        self.service.update_leaf("p", "leaf-0", "ready_not_run", {"old": True})
        self.service.control("p", "pause")
        self.workflow.set_validation("p", ["leaf-0"])
        self._complete_fresh_workflow(mark_ready=False)
        evidence = {
            "kind": "atlas.auxiliary-workflow-validation.v1",
            "static_checks_passed": True,
            "replay_new_calls": 0,
            "resume_verified": True,
            "failed_leaf_isolated": True,
            "fresh_ready_leaves": ["leaf-0"],
        }
        with self.assertRaises(FactoryError):
            self.workflow.set_gate_passed("p", evidence)


if __name__ == "__main__":
    unittest.main()
