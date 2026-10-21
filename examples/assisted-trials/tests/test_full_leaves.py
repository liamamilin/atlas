"""Host fixtures only: no providers, application runs, or production DB writes."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import full_leaf_profiles as profiles
import produce_all_leaves as runner
from template_factory.store import FactoryStore, FactoryError
from template_factory.full_auxiliary import FullAuxiliaryService, MODEL


class FullLeafTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        self.store = FactoryStore(self.pack / "state", self.pack)
        self.now = [1000.0]
        self.service = FullAuxiliaryService(self.store, "fixture", lambda: self.now[0])
        (self.root / "auth.txt").write_text("fixture scoped authorization")
        self.scope = {
            "full_plan_id": "p",
            "items": [{"leaf": "leaf-" + str(n), "covered": []} for n in range(200)],
        }
        (self.root / "scope.json").write_text(json.dumps(self.scope))
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
                "sha256": runner.sha(self.root / "scope.json"),
            },
            "authorization": {
                "path": "auth.txt",
                "sha256": runner.sha(self.root / "auth.txt"),
            },
        }

    def register(self):
        self.service.register(self.request)
        self.service.control("p", "resume")

    def reserve(self, slug="leaf-0", stage="first/discovery/attempt-1", **kw):
        self.service.update_leaf("p", slug, "running", {})
        return self.service.ledger.reserve(
            "p:" + slug,
            "auxiliary-full-p",
            requested_model=MODEL,
            stage=stage,
            plan_id="p",
            **kw,
        )

    def test_scoped_grant_crosses_500_without_unlocking_legacy_or_additive_pool(self):
        ledger = self.service.ledger
        for n in range(499):
            r = ledger.reserve("old", "old", stage=str(n))
            ledger.finish(r["id"], "completed")
        self.request["baseline"] = 499
        self.register()
        for n in range(3):
            r = self.reserve(
                stage=[
                    "first/discovery/attempt-1",
                    "first/blueprint-generate-aux/attempt-1",
                    "first/blueprint-spec-review-aux/attempt-1",
                ][n]
            )
            ledger.finish(r["id"], "completed")
        self.assertEqual(ledger.snapshot()["cli_sessions_used"], 502)
        self.assertEqual(ledger.snapshot()["limits"]["cli_sessions"], 500)
        with self.assertRaisesRegex(FactoryError, "campaign CLI"):
            ledger.reserve("strict", "G1")
        with self.assertRaisesRegex(FactoryError, "binding|identity"):
            ledger.reserve(
                "p:leaf-1",
                "auxiliary-full-p",
                requested_model=MODEL,
                plan_id="other",
                stage="first/discovery/attempt-1",
            )

    def test_frozen_request_window_controls_and_leaf_budget_survive_restart(self):
        self.register()
        r = self.reserve()
        self.service.ledger.finish(r["id"], "failed")
        deadline = self.service.status("p")["deadline"]
        self.now[0] += 100
        again = FullAuxiliaryService(self.store, "fixture", lambda: self.now[0])
        again.register(self.request)
        self.assertEqual(again.status("p")["deadline"], deadline)
        self.assertEqual(deadline, 2593000)
        with self.assertRaisesRegex(FactoryError, "reuse its checkpoint"):
            self.reserve()
        for n, stage in enumerate(
            [
                "protocol/discovery/attempt-1",
                "first/blueprint-generate-aux/attempt-1",
                "first/blueprint-spec-review-aux/attempt-1",
                "repair/blueprint-generate-aux/attempt-2",
                "repair/blueprint-spec-review-aux/attempt-2",
            ]
        ):
            r = self.reserve(stage=stage, job_id="new-" + str(n))
            self.service.ledger.finish(r["id"], "failed")
        with self.assertRaisesRegex(FactoryError, "allowance exhausted"):
            self.reserve(stage="repair/blueprint-spec-review-aux/attempt-2")
        self.assertEqual(again.status("p")["new_calls"], 6)
        self.service.control("p", "pause")
        with self.assertRaisesRegex(FactoryError, "cannot dispatch"):
            self.reserve("leaf-1")
        self.service.control("p", "resume")
        self.now[0] = deadline + 1
        with self.assertRaisesRegex(FactoryError, "deadline"):
            self.reserve("leaf-1")

    def test_concurrent_reservation_is_atomic_and_waits_not_product_failure(self):
        self.register()
        for n in range(3):
            self.service.update_leaf("p", "leaf-" + str(n), "running", {})
        barrier = threading.Barrier(3)
        results = []

        def reserve(n):
            barrier.wait()
            try:
                results.append(
                    self.service.ledger.reserve(
                        "p:leaf-" + str(n),
                        "auxiliary-full-p",
                        requested_model=MODEL,
                        plan_id="p",
                        stage="first/discovery/attempt-1",
                    )
                )
            except FactoryError as e:
                results.append(e.code)

        threads = [threading.Thread(target=reserve, args=(n,)) for n in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(sum(isinstance(x, dict) for x in results), 2)
        self.assertIn("budget_concurrency", results)
        self.assertEqual(self.service.status("p")["new_calls"], 2)
        for x in results:
            if isinstance(x, dict):
                self.service.ledger.finish(x["id"], "failed")

    def test_first_pass_reserved_before_repairs_and_global_cap_is_exclusive(self):
        self.register()
        # Fixture-only seed of already charged sessions at a late-plan boundary.
        with self.store.connect(True) as con:
            for n in range(6600):
                con.execute(
                    "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind,stage) VALUES(?,?,?,?,?,'completed',0,'production',?)",
                    (
                        str(n),
                        "fixture",
                        "p:old",
                        "auxiliary-full-p",
                        "production",
                        "first/old",
                    ),
                )
        with self.assertRaisesRegex(FactoryError, "first-pass allowance"):
            self.reserve(stage="repair/blueprint-generate-aux/attempt-2")
        for item in self.scope["items"]:
            self.service.update_leaf("p", item["leaf"], "needs_revision", {})
        r = self.reserve(stage="repair/blueprint-generate-aux/attempt-2")
        self.service.ledger.finish(r["id"], "completed")
        with self.store.connect(True) as con:
            for n in range(6601, 7200):
                con.execute(
                    "INSERT INTO tf_budget_reservation(id,campaign_id,identity,phase,kind,status,created,group_kind,stage) VALUES(?,?,?,?,?,'failed',0,'production',?)",
                    (
                        str(n),
                        "fixture",
                        "p:old",
                        "auxiliary-full-p",
                        "production",
                        "first/old",
                    ),
                )
        with self.assertRaisesRegex(FactoryError, "allowance exhausted"):
            self.reserve("leaf-1")

    def test_author_source_roles_and_non_web_profile_are_explicit(self):
        source = self.root / "source"
        source.mkdir()
        (source / "core.rs").write_text("a\nb\nc\n")
        (source / "LICENSE").write_text("MIT\n")
        snapshot = {
            "repository": "https://github.com/example/reference",
            "commit_sha": "a" * 40,
            "local_root": str(source),
            "files": {n: runner.sha(source / n) for n in ["core.rs", "LICENSE"]},
            "license": {"spdx_id": "MIT"},
            "license_files": ["LICENSE"],
        }
        ids = profiles.source_ids("leafsha", {"objective": "cli task"}, snapshot)
        inputs = {"source_ids": ids, "delivery_profile": "cli"}
        authored = {
            "name": "CLI task",
            "audience": "operator",
            "objective": "transform a stream",
            "workflow": ["input", "transform"],
            "acceptance": ["expected transformed values"],
            "features": ["Transform"],
            "goals": ["actual output equals expected"],
            "arch": "CLI --input --output; invalid input fails without overwriting destination",
            "inference": "target proposal",
            "gaps": ["upstream/target not run"],
            "delivery_profile": "cli",
            "execution_default": "Rust CLI with isolated input/output files",
            "observations": [
                ["code_observation", "core.rs", 1, 2, "a b"],
                ["documentation", "LICENSE", 1, 1, "MIT"],
            ],
            "source_refs": {
                "requirements": list(ids["requirements"]),
                "case_files": list(ids["upstream"]),
                "design_inferences": [
                    {
                        "text": "target uses file pipeline",
                        "depends_on": list(ids["requirements"]),
                    }
                ],
            },
        }
        generated = {
            "authored": authored,
            "acceptance_files": {"probe.py": "assert 1 == 1\n"},
        }
        profiles.validate_author(copy.deepcopy(generated), snapshot, inputs)
        bad = copy.deepcopy(generated)
        bad["authored"]["source_refs"]["case_files"].append("atlas:leafsha")
        with self.assertRaisesRegex(ValueError, "source partition"):
            profiles.validate_author(bad, snapshot, inputs)
        bad = copy.deepcopy(generated)
        bad["authored"]["observations"][0][1] = "leaf.md"
        with self.assertRaisesRegex(ValueError, "pinned source"):
            profiles.validate_author(bad, snapshot, inputs)

    def test_invalid_protocol_preserves_bytes_and_one_paid_successor(self):
        root = self.root / "plan"
        work = root / "items/leaf-0/attempt-1"
        work.mkdir(parents=True)
        (self.pack / "applications").mkdir()
        (self.pack / "applications/leaf-0.md").write_text("leaf")
        raw = b'{"broken": "quote"inside"}'
        item = {"leaf": "leaf-0", "leaf_sha256": hashlib.sha256(b"leaf").hexdigest()}
        launched = []

        def fake_checkpoint(path, *args, **kwargs):
            path.mkdir(parents=True, exist_ok=True)
            launched.append(path.name)
            if not path.name.endswith("-protocol-1"):
                (path / "original-response.json").write_text(
                    json.dumps({"text": raw.decode()})
                )
                (path / "LAUNCH_INTENT.json").write_text("{}")
                (path / "cli-summary.json").write_text(
                    json.dumps({"failure_code": "cli_protocol"})
                )
                raise FactoryError("bad JSON", "cli_protocol", 409)
            return {"valid": True}

        with (
            patch.object(runner, "verify_plan"),
            patch.object(runner, "checkpoint", fake_checkpoint),
        ):
            result = runner.stage_call(
                root,
                self.service,
                item,
                work,
                "blueprint-generate-aux",
                {},
                "prompt",
                "production",
            )
        self.assertEqual(result, {"valid": True})
        self.assertEqual(len(launched), 2)
        self.assertEqual(
            json.loads(
                (
                    work / "calls/blueprint-generate-aux/original-response.json"
                ).read_text()
            )["text"].encode(),
            raw,
        )
        self.assertTrue((work / "PROTOCOL_SUCCESSOR.json").is_file())

    def test_registration_rejects_authorization_or_scope_drift(self):
        self.register()
        changed = copy.deepcopy(self.request)
        changed["baseline"] = 1
        with self.assertRaisesRegex(FactoryError, "already bound"):
            self.service.register(changed)
        (self.root / "scope.json").write_text("{}")
        with self.assertRaisesRegex(FactoryError, "bytes differ"):
            self.service.register(self.request)

    def test_grant_cannot_be_spent_on_legacy_phase_or_runtime(self):
        self.register()
        self.service.update_leaf("p", "leaf-0", "running", {})
        with self.assertRaises(FactoryError):
            self.service.ledger.reserve(
                "p:leaf-0", "G1", plan_id="p", requested_model=MODEL
            )
        with self.assertRaisesRegex(FactoryError, "runtime"):
            self.reserve(kind="runtime")
        self.assertEqual(self.service.status("p")["new_calls"], 0)
        for _ in range(2):
            self.assertIsNotNone(self.service.schedule_provider_recovery("p"))
        self.assertIsNone(
            FullAuxiliaryService(self.store, "fixture").schedule_provider_recovery("p")
        )

    def test_unknown_launch_is_not_retried_and_stopped_plan_cannot_resume(self):
        work = self.root / "items/leaf-0/attempt-1"
        work.mkdir(parents=True)
        (self.pack / "applications").mkdir()
        (self.pack / "applications/leaf-0.md").write_text("leaf")
        item = {"leaf": "leaf-0", "leaf_sha256": hashlib.sha256(b"leaf").hexdigest()}

        def uncertain(path, *args, **kw):
            path.mkdir(parents=True, exist_ok=True)
            (path / "LAUNCH_INTENT.json").write_text("{}")
            raise ValueError("uncertain previous launch")

        with (
            patch.object(runner, "verify_plan"),
            patch.object(runner, "checkpoint", uncertain),
        ):
            with self.assertRaisesRegex(FactoryError, "reconcile"):
                runner.stage_call(
                    self.root,
                    self.service,
                    item,
                    work,
                    "blueprint-generate-aux",
                    {},
                    "prompt",
                    "production",
                )
        self.register()
        self.service.control("p", "stop")
        for action in ["resume", "pause"]:
            with self.assertRaisesRegex(FactoryError, "cannot dispatch"):
                self.service.control("p", action)

    def test_proven_not_started_keeps_original_intent_and_gets_no_free_paid_retry(self):
        work = self.root / "items/leaf-0/attempt-1"
        path = work / "calls/blueprint-generate-aux"
        path.mkdir(parents=True)
        (path / "LAUNCH_INTENT.json").write_text('{"original":true}')
        (path / "cli-summary.json").write_text(
            json.dumps(
                {
                    "cli_status": "not_started",
                    "output_observed": False,
                    "failure_code": "full_plan_paused",
                }
            )
        )
        (self.pack / "applications").mkdir()
        (self.pack / "applications/leaf-0.md").write_text("leaf")
        item = {"leaf": "leaf-0", "leaf_sha256": hashlib.sha256(b"leaf").hexdigest()}
        called = []

        def delivered(p, *args, **kw):
            called.append(p)
            return {"ok": True}

        with (
            patch.object(runner, "verify_plan"),
            patch.object(runner, "checkpoint", delivered),
        ):
            self.assertEqual(
                runner.stage_call(
                    self.root,
                    self.service,
                    item,
                    work,
                    "blueprint-generate-aux",
                    {},
                    "prompt",
                    "production",
                ),
                {"ok": True},
            )
        self.assertIn("not-started-1", called[0].name)
        self.assertEqual((path / "LAUNCH_INTENT.json").read_text(), '{"original":true}')


if __name__ == "__main__":
    unittest.main()
