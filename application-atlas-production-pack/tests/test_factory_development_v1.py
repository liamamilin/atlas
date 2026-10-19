"""P0 development handoff and safe application delivery contracts; no model calls."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import test_blueprints as blueprint_fixtures
from template_factory.blueprints import import_blueprint
from template_factory.budget import BudgetLedger
from template_factory.cases import CaseLibrary
from template_factory.development_jobs import (
    _host_counted_template_revision,
    queue_development,
    run_development,
    _response_archive,
)
from template_factory.delivery import prepare_application
from template_factory.store import FactoryError, canonical, digest, now, uid


PACK = Path(__file__).resolve().parents[1]


class DevelopmentV1Tests(unittest.TestCase):
    def setUp(self):
        blueprint_fixtures.BlueprintTests.setUp(self)
        self.scene = self.store.save_scenario(
            {
                "leaf": "bookmark-manager",
                "name": "Save a bookmark",
                "audience": "Personal",
                "objective": "Save and reopen bookmarks",
                "workflow": ["Save", "Reopen"],
                "acceptance": ["Saved bookmarks remain"],
                "status": "ready",
            }
        )
        imported = import_blueprint(self.store, self.data())
        self.artifact = imported
        basis = {
            "schema": "atlas.case-basis.v1",
            "case_refs": [],
            "basis_digest": "f" * 64,
        }
        origin = self.store.job(imported["job_id"])
        origin_snapshot = origin["snapshot"]
        origin_snapshot.update(
            {
                "v1": {
                    "campaign_id": "study",
                    "plan_id": "plan-test",
                    "plan_digest": "a" * 64,
                    "product_id": "product-a",
                    "segment": "G1",
                },
                "leaf": self.store.leaf("bookmark-manager"),
                "config": {"language": "en"},
                "case_basis": basis,
            }
        )
        with self.store.connect(True) as con:
            plan_body = {"id": "plan-test", "campaign_id": "study"}
            con.execute(
                "INSERT INTO v1_plan VALUES(?,?,?,?)",
                ("plan-test", "a" * 64, canonical(plan_body), now()),
            )
            con.execute(
                "INSERT INTO v1_execution VALUES(?,?,?,?,?)",
                ("plan-test", "a" * 64, "plan-request", origin["batch_id"], now()),
            )
            con.execute(
                "UPDATE batch SET state='running' WHERE id=?", (origin["batch_id"],)
            )
            con.execute(
                "UPDATE job SET snapshot=? WHERE id=?",
                (canonical(origin_snapshot), imported["job_id"]),
            )
            row = con.execute(
                "SELECT body FROM artifact WHERE id=?", (imported["id"],)
            ).fetchone()
            body = json.loads(row[0])
            body["provenance"].update(
                {
                    "scenario": self.scene,
                    "case_basis": basis,
                    "v1": origin_snapshot["v1"],
                    "model": "fixture/model",
                }
            )
            con.execute(
                "UPDATE artifact SET body=? WHERE id=?",
                (canonical(body), imported["id"]),
            )
            review_id = uid("job")
            review_snapshot = {
                "artifact_id": imported["id"],
                "artifact_digest": imported["digest"],
            }
            at = now()
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    review_id,
                    origin["batch_id"],
                    "cognitive-review",
                    "completed",
                    "reviewed",
                    1,
                    None,
                    None,
                    canonical(review_snapshot),
                    None,
                    at,
                    at,
                ),
            )
            con.execute(
                "INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)",
                (
                    uid("acc"),
                    imported["id"],
                    imported["digest"],
                    "cognitive-review",
                    review_id,
                    canonical({"outcome": "passed"}),
                    at,
                ),
            )
        self.artifact = next(
            a for a in self.store.artifacts() if a["id"] == imported["id"]
        )

    tearDown = blueprint_fixtures.BlueprintTests.tearDown
    data = blueprint_fixtures.BlueprintTests.data

    def queue(self, key="request-p0", **changes):
        value = {
            "expected_digest": self.artifact["digest"],
            "phase": "P0",
            "request_key": key,
            "model": "fixture/model",
            "project_name": "bookmark-p0",
        }
        value.update(changes)
        with (
            patch.object(CaseLibrary, "validate_basis"),
            patch.object(CaseLibrary, "require_admissible"),
        ):
            return queue_development(self.store, self.artifact, value)

    def test_standard_handoff_is_pinned_idempotently_and_p0_delivered(self):
        first = self.queue()
        replay = self.queue(key="same-body-new-key")
        self.assertEqual(first["id"], replay["id"])
        with self.assertRaisesRegex(FactoryError, "already exists"):
            self.queue(
                key="changed-initial", model="other/model", project_name="other-app"
            )
        self.assertEqual(first["jobs"][0]["kind"], "application-development")
        job = self.store.claim("development-worker")
        snapshot = job["snapshot"]
        self.assertEqual(snapshot["phase"], "P0")
        self.assertEqual(snapshot["scenario"]["id"], self.scene["id"])
        self.assertTrue((self.store.root / snapshot["handoff_archive"]).is_file())
        calls = []

        def agent(name, prompt, payload, source=None, **budget):
            calls.append((name, payload, source))
            self.assertTrue((source / "ACCEPTANCE_CONTRACT.json").is_file())
            return {
                "files": {
                    "index.html": "<main>Saved bookmarks remain available.</main>",
                    "delivery.json": json.dumps(
                        {
                            "schema": "atlas.application-delivery.v1",
                            "root": ".",
                            "files": ["index.html"],
                            "runtime": {
                                "profile": "python-web",
                                "start": ["python3", "-m", "http.server", "8000"],
                                "port": 8000,
                            },
                        }
                    ),
                }
            }

        def checkpoint(name, create):
            existing = self.store.checkpoint(job["id"], name)
            if existing:
                return existing["result"]
            result = create()
            self.store.checkpoint(
                job["id"],
                name,
                {"result": result, "digest": digest(result)},
                job["token"],
            )
            return result

        attempt = self.root / "worker-attempt"
        attempt.mkdir()
        report = run_development(
            type("Pipeline", (), {"store": self.store})(),
            job,
            attempt,
            agent,
            lambda *_: None,
            checkpoint,
        )
        self.assertEqual(report["runtime_status"], "not_run")
        self.assertEqual(report["acceptance_status"], "not_run")
        self.assertEqual(len(calls), 1)
        self.assertEqual(self.store.job(job["id"])["state"], "completed")
        self.assertEqual(
            self.store.checkpoint(job["id"], "application-delivery")["result"][
                "archive_sha256"
            ],
            report["archive_sha256"],
        )

    def test_materializer_rejects_escape_and_invalid_exact_manifest(self):
        with self.assertRaises(FactoryError):
            _response_archive({"files": {"../escape.py": "no"}})
        bad = _response_archive({"files": {"delivery.json": "{}", "app.py": "safe"}})
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(FactoryError):
                prepare_application(bad, Path(temporary) / "bad")
        valid = {
            "files": {
                "delivery.json": json.dumps(
                    {
                        "schema": "atlas.application-delivery.v1",
                        "root": ".",
                        "files": ["index.html"],
                        "runtime": {
                            "profile": "python-web",
                            "start": ["python3", "-m", "http.server", "8000"],
                            "port": 8000,
                        },
                    }
                ),
                "index.html": "safe",
            }
        }
        self.assertTrue(_response_archive(valid).startswith(b"PK"))

    def test_queue_requires_current_review_phase_and_version(self):
        cases = [
            {"expected_digest": "wrong", "phase": "P0", "request_key": "wrong"},
            {
                "expected_digest": self.artifact["digest"],
                "phase": "P1",
                "request_key": "phase",
            },
        ]
        with (
            patch.object(CaseLibrary, "validate_basis"),
            patch.object(CaseLibrary, "require_admissible"),
        ):
            for value in cases:
                with self.subTest(value=value), self.assertRaises(FactoryError):
                    queue_development(
                        self.store, self.artifact, {**value, "model": "fixture/model"}
                    )
        with self.store.connect() as con:
            self.assertEqual(
                con.execute(
                    "SELECT count(*) FROM job WHERE kind='application-development'"
                ).fetchone()[0],
                0,
            )

    def test_repair_requires_failed_bound_acceptance_and_counts_business_feedback(self):
        reports = [self._failed_runtime_input(i) for i in range(1)]
        with (
            patch.object(CaseLibrary, "validate_basis"),
            patch.object(CaseLibrary, "require_admissible"),
        ):
            with self.assertRaises(FactoryError):
                queue_development(
                    self.store,
                    self.artifact,
                    {
                        "expected_digest": self.artifact["digest"],
                        "phase": "P0",
                        "request_key": "invalid-repair",
                        "repair_of": "not-a-real-run",
                    },
                )
            first_value = {
                "expected_digest": self.artifact["digest"],
                "phase": "P0",
                "request_key": "repair-first",
                "project_name": "repair-first",
                "model": "fixture/model",
                "repair_of": reports[0],
            }
            batch = queue_development(self.store, self.artifact, first_value)
            snapshot = batch["jobs"][0]["snapshot"]
            self.assertEqual(
                snapshot["previous_application_sha256"],
                self.store.job(snapshot["failure_report"]["job_id"])["snapshot"][
                    "archive_sha256"
                ],
            )
            self.assertEqual(
                snapshot["failure_report_digest"], digest(snapshot["failure_report"])
            )
            alias = queue_development(
                self.store,
                self.artifact,
                {**first_value, "request_key": "repair-alias"},
            )
            self.assertEqual(alias["id"], batch["id"])

            second_value = {
                **first_value,
                "request_key": "repair-second",
                "project_name": "repair-second",
                "model": "other/model",
            }
            second = queue_development(self.store, self.artifact, second_value)
            self.assertNotEqual(second["id"], batch["id"])
            with self.assertRaisesRegex(FactoryError, "repair limit"):
                queue_development(
                    self.store,
                    self.artifact,
                    {
                        **first_value,
                        "request_key": "repair-third",
                        "project_name": "repair-third",
                    },
                )
        with self.store.connect() as con:
            self.assertEqual(
                con.execute(
                    "SELECT count(*) FROM tf_budget_repair WHERE campaign_id='study' AND product_id='product-a'"
                ).fetchone()[0],
                2,
            )

    def test_parent_batch_pause_and_cancel_are_inherited(self):
        with self.store.connect(True) as con:
            con.execute(
                "UPDATE batch SET state='paused' WHERE id=?",
                (self.store.job(self.artifact["job_id"])["batch_id"],),
            )
        paused = self.queue(key="paused-child")
        self.assertEqual(paused["state"], "paused")
        with self.store.connect(True) as con:
            con.execute(
                "UPDATE batch SET state='cancelled' WHERE id=?",
                (self.store.job(self.artifact["job_id"])["batch_id"],),
            )
        with self.assertRaisesRegex(FactoryError, "cancelled"):
            self.queue(key="cancelled-child", project_name="cancelled-child")

    def test_charged_ancestry_cannot_authorize_second_initial_for_same_artifact(self):
        first = self.queue()
        with patch("template_factory.development_jobs._host_counted_template_revision", return_value=True):
            with self.assertRaises(FactoryError) as caught:
                self.queue(key="second-initial", project_name="another-app", model="another/model")
        self.assertEqual(caught.exception.code, "development_initial_exists")
        self.assertEqual(self.queue(key="alias")["id"], first["id"])

    def test_only_host_counted_cognitive_revision_can_start_new_initial_p0(self):
        self.queue()
        parent_id = self.artifact["id"]
        parent_digest = self.artifact["digest"]
        v1 = self.artifact["provenance"]["v1"]
        fake = {
            **self.artifact,
            "id": "model-claimed-revision",
            "supersedes": parent_id,
        }
        with self.store.connect() as con:
            self.assertFalse(_host_counted_template_revision(con, fake, v1))

        revision_job_id = uid("job")
        revision_id = uid("tpl")
        revision_batch_id = uid("bat")
        at = now()
        revision_snapshot = {
            "v1": v1,
            "cognitive_repair": {"id": parent_id, "digest": parent_digest},
        }
        revision_body = {
            **self.artifact,
            "id": revision_id,
            "job_id": revision_job_id,
            "supersedes": parent_id,
        }
        BudgetLedger(self.store, campaign_id=v1["campaign_id"]).record_repair(
            v1["product_id"], "template-revision:" + parent_digest + ":fixture"
        )
        with self.store.connect(True) as con:
            con.execute(
                "INSERT INTO batch VALUES(?,?,?,?)",
                (revision_batch_id, "completed", "{}", at),
            )
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    revision_job_id,
                    revision_batch_id,
                    "blueprint-production",
                    "completed",
                    "completed",
                    1,
                    None,
                    None,
                    canonical(revision_snapshot),
                    None,
                    at,
                    at,
                ),
            )
            con.execute(
                "INSERT INTO artifact VALUES(?,?,?,?,?,?,?)",
                (
                    revision_id,
                    revision_job_id,
                    parent_digest,
                    "L0",
                    "draft",
                    canonical(revision_body),
                    at,
                ),
            )
            host_revision = {**revision_body, "digest": parent_digest}
            self.assertTrue(_host_counted_template_revision(con, host_revision, v1))

            # The allowance does not transfer to an uncharged revision or a
            # revision whose cognitive-repair parent differs from supersedes.
            con.execute(
                "DELETE FROM tf_budget_repair WHERE campaign_id=? AND product_id=?",
                (v1["campaign_id"], v1["product_id"]),
            )
            self.assertFalse(_host_counted_template_revision(con, host_revision, v1))

    def _failed_runtime_input(self, index):
        raw = _response_archive(
            {
                "files": {
                    "index.html": "<main>Old implementation</main>",
                    "delivery.json": json.dumps(
                        {
                            "schema": "atlas.application-delivery.v1",
                            "root": ".",
                            "files": ["index.html"],
                            "runtime": {
                                "profile": "python-web",
                                "start": ["python3", "-m", "http.server", "8000"],
                                "port": 8000,
                            },
                        }
                    ),
                }
            }
        )
        base = self.store.root / "submissions" / f"failed-{index}"
        base.mkdir(parents=True)
        (base / "application.zip").write_bytes(raw)
        app_path = base / "application"
        receipt = prepare_application(raw, app_path)
        (base / "delivery-receipt.json").write_text(json.dumps(receipt))
        basis = self.artifact["provenance"]["case_basis"]
        target = {
            "target_kind": "generated_application",
            "artifact_id": self.artifact["id"],
            "artifact_digest": self.artifact["digest"],
            "application_digest": digest(receipt["files"]),
            "suite_digest": "e" * 64,
            "selected_phase": "P0",
            "selected_case_ids": ["A01"],
            "scenario_id": self.scene["id"],
            "scenario_revision": self.scene["revision"],
            "case_basis_digest": basis["basis_digest"],
        }
        run_job = uid("job")
        runtime_input = {
            "artifact_id": self.artifact["id"],
            "artifact_digest": self.artifact["digest"],
            "selected_phase": "P0",
            "submission_path": str(app_path.relative_to(self.store.root)),
            "archive_sha256": __import__("hashlib").sha256(raw).hexdigest(),
            "delivery": receipt,
            "target_binding": target,
        }
        report = {
            "method": "blueprint-runtime",
            "job_id": run_job,
            "outcome": "blocked",
            "suite_status": "blocked",
            "case_results": [{"case_id": "A01", "status": "failed"}],
            "target_binding": target,
        }
        at = now()
        with self.store.connect(True) as con:
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    run_job,
                    self.store.job(self.artifact["job_id"])["batch_id"],
                    "blueprint-runtime",
                    "needs_review",
                    "acceptance",
                    1,
                    None,
                    None,
                    canonical(runtime_input),
                    None,
                    at,
                    at,
                ),
            )
            con.execute(
                "INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)",
                (
                    uid("acc"),
                    self.artifact["id"],
                    self.artifact["digest"],
                    "blueprint-runtime",
                    run_job,
                    canonical(report),
                    at,
                ),
            )
            acceptance_id = con.execute(
                "SELECT id FROM acceptance WHERE job_id=?", (run_job,)
            ).fetchone()[0]
        return acceptance_id

    def test_model_repair_receives_previous_app_and_failure_report_as_read_only_context(
        self,
    ):
        run_id = self._failed_runtime_input(99)
        with (
            patch.object(CaseLibrary, "validate_basis"),
            patch.object(CaseLibrary, "require_admissible"),
        ):
            batch = queue_development(
                self.store,
                self.artifact,
                {
                    "expected_digest": self.artifact["digest"],
                    "phase": "P0",
                    "request_key": "actual-repair",
                    "project_name": "actual-repair",
                    "model": "fixture/model",
                    "repair_of": run_id,
                },
            )
        job = self.store.claim("development-worker")
        self.assertEqual(job["id"], batch["jobs"][0]["id"])
        attempt = self.root / "repair-attempt"
        attempt.mkdir()

        def agent(name, prompt, payload, source=None, **budget):
            self.assertEqual(name, "p0-application-repair")
            self.assertEqual(payload["repair_of"], run_id)
            self.assertTrue((source / "previous-application/index.html").is_file())
            report = json.loads((source / "FAILURE_REPORT.json").read_text())
            self.assertEqual(
                report["job_id"],
                self.store.acceptances(self.artifact["id"])[0]["job_id"],
            )
            return {
                "files": {
                    "index.html": "<main>Repaired implementation</main>",
                    "delivery.json": json.dumps(
                        {
                            "schema": "atlas.application-delivery.v1",
                            "root": ".",
                            "files": ["index.html"],
                            "runtime": {
                                "profile": "python-web",
                                "start": ["python3", "-m", "http.server", "8000"],
                                "port": 8000,
                            },
                        }
                    ),
                }
            }

        def checkpoint(name, create):
            found = self.store.checkpoint(job["id"], name)
            if found:
                return found["result"]
            result = create()
            self.store.checkpoint(
                job["id"],
                name,
                {"result": result, "digest": digest(result)},
                job["token"],
            )
            return result

        result = run_development(
            type("Pipeline", (), {"store": self.store})(),
            job,
            attempt,
            agent,
            lambda *_: None,
            checkpoint,
        )
        self.assertEqual(result["repair_of"], run_id)
        self.assertEqual(
            result["failure_report_digest"], job["snapshot"]["failure_report_digest"]
        )

    def test_bad_delivery_is_bounded_and_never_completes_or_claims_pass(self):
        self.queue("bad-delivery")
        job = self.store.claim("development-worker")
        calls = []

        def agent(*_args, **budget):
            if len(calls) and _args[3] is not None:
                self.assertTrue((_args[3] / "PRIOR_DELIVERY.json").is_file())
                self.assertTrue((_args[3] / "VALIDATION_ERROR.json").is_file())
            calls.append(1)
            return {"files": {"delivery.json": "{}", "main.py": "print('no')"}}

        def checkpoint(name, create):
            found = self.store.checkpoint(job["id"], name)
            if found:
                return found["result"]
            result = create()
            self.store.checkpoint(
                job["id"],
                name,
                {"result": result, "digest": digest(result)},
                job["token"],
            )
            return result

        attempt = self.root / "failed-attempt"
        attempt.mkdir()
        with self.assertRaises(FactoryError):
            run_development(
                type("Pipeline", (), {"store": self.store})(),
                job,
                attempt,
                agent,
                lambda *_: None,
                checkpoint,
            )
        self.assertEqual(len(calls), 3)
        self.assertEqual(self.store.job(job["id"])["state"], "running")
        self.assertIsNone(self.store.checkpoint(job["id"], "application-delivery"))


if __name__ == "__main__":
    unittest.main()
