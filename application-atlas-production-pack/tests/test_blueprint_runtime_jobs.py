"""Runtime queue/pinning integration. Fake transport, not application-quality proof."""

import base64
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import test_blueprints as fixtures
from template_factory.api import dispatch
from template_factory.artifacts import tree_manifest
from template_factory.blueprints import import_blueprint
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, digest
from template_factory.runtime_jobs import register_phase_evidence


class RuntimeJobTests(unittest.TestCase):
    tearDown = fixtures.BlueprintTests.tearDown
    data = fixtures.BlueprintTests.data
    rewrite = fixtures.BlueprintTests.rewrite

    def setUp(self):
        fixtures.BlueprintTests.setUp(self)
        self.worker_patch = patch("template_factory.api.ensure_worker")
        self.worker_patch.start()
        self.addCleanup(self.worker_patch.stop)

    def artifact(self, binding=True, required_evidence=None):
        if binding:
            spec = json.loads((self.source / "template.json").read_text())
            if required_evidence:
                phase = spec["phases"][0]["id"]
                spec["phase_required_evidence"] = {phase: required_evidence}
                (self.source / "template.json").write_text(json.dumps(spec, ensure_ascii=False))
            runner = {
                "schema": "atlas.acceptance-runner.v1",
                "result_schema": "atlas.acceptance-result.v1",
                "cases": {a["id"]: {"args": ["--case", "{case_id}", "--base-url", "{base_url}"]} for a in spec["acceptance"]},
            }
            (self.source / "acceptance/runner.json").write_text(json.dumps(runner))
            self.rewrite(lambda _: None)
        return import_blueprint(self.store, self.data())

    def source_zip(self, *, declared=None):
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as archive:
            archive.writestr("app.py", "print('synthetic fixture; not executed by queue tests')\n")
            archive.writestr("delivery.json", json.dumps({
                "schema": "atlas.application-delivery.v1", "root": ".",
                "files": declared or ["app/app.py"],
                "runtime": {"profile": "cli", "smoke": ["python3", "app.py", "--help"]},
            }))
        return base64.b64encode(output.getvalue()).decode()

    def submit(self, artifact, **changes):
        body = {"method": "blueprint-runtime", "expected_digest": artifact["digest"],
                "phase": artifact["manifest"]["phases"][0]["id"], "execution_confirmed": True,
                "source_archive_base64": self.source_zip(), "timeout": 30}
        body.update(changes)
        return dispatch("POST", f"/api/factory/artifacts/{artifact['id']}/accept", body=body, store=self.store)

    def test_legacy_is_readable_but_runtime_is_explicitly_unavailable(self):
        artifact = self.artifact(binding=False)
        details, status = dispatch("GET", f"/api/factory/artifacts/{artifact['id']}/blueprint", store=self.store)
        self.assertEqual(status, 200)
        self.assertFalse(details["runtime_acceptance"]["supported"])
        self.assertEqual(details["runtime_acceptance"]["reason"], "acceptance_adapter_missing")
        with self.assertRaises(FactoryError):
            self.submit(artifact)
        self.assertEqual(len(self.store.batches()), 1)  # import only

    def test_runtime_child_inherits_fixed_plan_pause_and_cancellation(self):
        artifact = self.artifact()
        origin = self.store.job(artifact["job_id"])
        artifact["provenance"]["v1"] = {
            "campaign_id": "runtime-policy", "plan_id": "plan-policy",
            "product_id": "bookmark", "segment": "G1",
        }
        from template_factory.runtime_jobs import queue_runtime
        from template_factory.store import now
        with self.store.connect(True) as con:
            con.execute("INSERT INTO v1_execution VALUES(?,?,?,?,?)", ("plan-policy", "a" * 64, "policy-key", origin["batch_id"], now()))
            con.execute("UPDATE batch SET state='paused' WHERE id=?", (origin["batch_id"],))
        value = {"expected_digest": artifact["digest"], "phase": artifact["manifest"]["phases"][0]["id"],
                 "execution_confirmed": True, "source_archive_base64": self.source_zip(), "timeout": 30}
        paused = queue_runtime(self.store, artifact, value)
        self.assertEqual(paused["state"], "paused")
        self.assertIsNone(self.store.claim("runtime-worker", "verification"))
        with self.store.connect(True) as con:
            con.execute("UPDATE batch SET state='cancelled' WHERE id=?", (origin["batch_id"],))
            con.execute("UPDATE job SET state='cancelled' WHERE batch_id=?", (paused["id"],))
        with self.assertRaises(FactoryError) as caught:
            queue_runtime(self.store, artifact, value)
        self.assertEqual(caught.exception.code, "cancelled")
        self.assertEqual(len(list((self.store.root / "submissions").iterdir())), 1)

    def test_delayed_runtime_rechecks_segment_deadline_before_container_start(self):
        artifact = self.artifact()
        artifact["provenance"]["v1"] = {"campaign_id": "delayed-runtime", "product_id": "bookmark", "segment": "G1"}
        from template_factory.runtime_jobs import queue_runtime
        batch = queue_runtime(self.store, artifact, {"expected_digest": artifact["digest"],
            "phase": artifact["manifest"]["phases"][0]["id"], "execution_confirmed": True,
            "source_archive_base64": self.source_zip(), "timeout": 30})
        job = self.store.claim("runtime-worker", "verification")
        self.assertEqual(job["batch_id"], batch["id"])
        with patch("template_factory.budget.BudgetLedger.phase_remaining", return_value=0), patch("template_factory.blueprint_runtime.BlueprintRuntimeVerifier.verify", side_effect=AssertionError("expired runtime must not start")):
            with self.assertRaises(FactoryError) as caught:
                Pipeline(self.store).run(job)
            self.assertEqual(caught.exception.code, "budget_deadline")
        self.assertEqual(self.store.job(job["id"])["state"], "paused_budget")

    def test_imported_runtime_enabled_revision_retains_frozen_protocol(self):
        artifact = self.artifact()
        revision = self.store.create_repair(artifact["id"], {
            "expected_digest": artifact["digest"], "model": "fake/flash",
            "note": "Preserve the existing frozen invocation contract while revising documentation.",
        })
        self.assertEqual(revision["jobs"][0]["snapshot"]["config"]["acceptance_protocol"], "atlas.acceptance-runner.v1")

    def test_consent_version_phase_and_duplicate_submission_are_enforced(self):
        artifact = self.artifact()
        for changes in [{"execution_confirmed": False}, {"expected_digest": "wrong"}, {"phase": "unknown"}]:
            with self.subTest(changes=changes), self.assertRaises(FactoryError):
                self.submit(artifact, **changes)
        batch, status = self.submit(artifact)
        self.assertEqual(status, 202)
        self.assertEqual(batch["jobs"][0]["kind"], "blueprint-runtime")
        self.assertEqual(batch["config"]["model"], "")
        details, _ = dispatch("GET", "/api/factory/artifacts", store=self.store)
        rows = details.get("artifacts", []) if isinstance(details, dict) else details
        current = next(row for row in rows if row["id"] == artifact["id"])
        self.assertTrue(any(row["kind"] == "blueprint-runtime" and row["state"] == "queued" for row in current["acceptance_jobs"]))
        with self.assertRaises(FactoryError):
            self.submit(artifact)
        self.assertEqual(len(list((self.store.root / "submissions").iterdir())), 1)
        self.assertIsNone(self.store.claim("production-worker", "production"))
        self.assertEqual(self.store.claim("runtime-worker", "verification")["kind"], "blueprint-runtime")

    def test_runtime_job_pins_application_runs_without_model_and_does_not_promote(self):
        artifact = self.artifact()
        self.submit(artifact)
        job = self.store.claim("runtime-worker", "verification")
        source = self.store.root / job["snapshot"]["submission_path"]
        before = tree_manifest(source)
        invocations = []

        class Verifier:
            def verify(self, app, frozen, spec, phase, evidence, runtime, cancelled, progress):
                invocations.append((app, frozen, phase, runtime))
                return {"outcome": "passed", "startup": {"status": "passed"}, "case_results": [], "cleanup": {"status": "passed"}}

        pipeline = Pipeline(self.store)
        pipeline.blueprint_verifier = Verifier()
        with patch.object(pipeline.cli, "run", side_effect=AssertionError("no model during runtime acceptance")):
            pipeline.run(job)
        self.assertEqual(len(invocations), 1)
        self.assertEqual(tree_manifest(source), before)
        result = self.store.acceptances(artifact["id"])[0]
        self.assertEqual(result["method"], "blueprint-runtime")
        self.assertEqual(result["delivery_normalizations"], [{"declared": "app/app.py", "path": "app.py"}])
        self.assertEqual(self.store.artifacts()[0]["level"], "L0")
        self.assertEqual(self.store.artifacts()[0]["state"], "draft")
        self.assertEqual(self.store.job(job["id"])["state"], "completed")

    def test_changed_source_is_rejected_before_any_container_or_model_call(self):
        artifact = self.artifact()
        self.submit(artifact)
        job = self.store.claim("runtime-worker", "verification")
        (self.store.root / job["snapshot"]["submission_path"] / "app.py").write_text("changed")
        pipeline = Pipeline(self.store)
        with patch("template_factory.blueprint_runtime.BlueprintRuntimeVerifier.verify", side_effect=AssertionError("must not execute changed source")):
            with self.assertRaisesRegex(FactoryError, "source changed"):
                pipeline.run(job)
        self.assertEqual(self.store.acceptances(artifact["id"]), [])
        self.assertEqual(self.store.job(job["id"])["state"], "failed")

    def test_changed_frozen_suite_is_rejected_before_runtime_execution(self):
        artifact = self.artifact()
        self.submit(artifact)
        job = self.store.claim("runtime-worker", "verification")
        frozen_case = self.store.root / artifact["bundle_path"] / "source/acceptance/a.py"
        frozen_case.write_text("changed suite")
        pipeline = Pipeline(self.store)
        with patch("template_factory.blueprint_runtime.BlueprintRuntimeVerifier.verify",
                   side_effect=AssertionError("changed suite must not execute")):
            with self.assertRaises(FactoryError):
                pipeline.run(job)
        self.assertEqual(self.store.acceptances(artifact["id"]), [])
        self.assertEqual(self.store.job(job["id"])["state"], "failed")

    def test_missing_phase_evidence_stays_unverified_until_bound_host_record_is_registered(self):
        requirements = [{"id": "restart-check", "kind": "external", "description": "Verify stored data after restart.",
                         "executor": "independent-restart-checker"}]
        artifact = self.artifact(required_evidence=requirements)
        self.submit(artifact)
        job = self.store.claim("runtime-worker", "verification")
        snapshot = job["snapshot"]
        executor = {"kind": "independent_executor", "name": "independent-restart-checker", "version": "1.0"}
        target_digest = digest(snapshot["target_binding"])
        evidence_location = {}

        class Verifier:
            def verify(self, app, frozen, spec, phase, evidence, runtime, cancelled, progress):
                evidence_location["directory"] = Path(evidence) / "external"
                return {"outcome": "passed", "passed": True, "suite_status": "passed",
                        "phase_status": "passed", "case_results": [],
                        "binding": {"suite_digest": snapshot["suite_digest"]},
                        "cleanup": {"success": True, "status": "passed"}}

        pipeline = Pipeline(self.store)
        pipeline.blueprint_verifier = Verifier()
        pipeline.run(job)
        report = self.store.acceptances(artifact["id"])[0]
        self.assertEqual(report["suite_status"], "passed")
        self.assertEqual(report["phase_status"], "unverified")
        self.assertFalse(report["passed"])
        self.assertEqual(report["missing_evidence"], ["restart-check"])
        folder = evidence_location["directory"]
        folder.mkdir(parents=True)
        evidence_file = folder / "restart-check.json"
        proof = {"schema": "atlas.phase-evidence.v1", "requirement_id": "restart-check",
                 "target_digest": target_digest, "outcome": "passed", "executor": executor,
                 "details": "synthetic independent executor record"}
        evidence_file.write_text(json.dumps(proof, sort_keys=True))
        relative = evidence_file.relative_to(self.store.root).as_posix()
        registration = {"requirement_id": "restart-check", "target_digest": target_digest,
                        "evidence_path": relative,
                        "sha256": hashlib.sha256(evidence_file.read_bytes()).hexdigest(),
                        "executor": executor}
        with self.assertRaisesRegex(FactoryError, "target binding changed"):
            register_phase_evidence(self.store, artifact["id"], report["id"],
                                    {**registration, "target_digest": "0" * 64})
        application = self.store.root / snapshot["submission_path"] / "app.py"
        original_application = application.read_text()
        application.write_text(original_application + "# mutated after run\n")
        with self.assertRaisesRegex(FactoryError, "application target changed"):
            register_phase_evidence(self.store, artifact["id"], report["id"], registration)
        application.write_text(original_application)
        passed = register_phase_evidence(self.store, artifact["id"], report["id"], registration)
        self.assertEqual(passed["phase_status"], "passed")
        self.assertTrue(passed["passed"])
        self.assertEqual(self.store.job(job["id"])["state"], "completed")

    def test_runtime_infrastructure_failure_records_unavailable_with_partial_evidence(self):
        artifact = self.artifact()
        self.submit(artifact)
        job = self.store.claim("runtime-worker", "verification")

        class Verifier:
            def verify(self, app, frozen, spec, phase, evidence, runtime, cancelled, progress):
                evidence.mkdir()
                (evidence / "report.json").write_text(json.dumps({
                    "startup": {"status": "passed"}, "case_results": [{"id": "A01", "status": "failed"}],
                    "cleanup": {"status": "passed"}, "outcome": "unavailable",
                }))
                raise FactoryError("synthetic timeout", "verification_timeout", 409)

        pipeline = Pipeline(self.store)
        pipeline.blueprint_verifier = Verifier()
        pipeline.run(job)
        report = self.store.acceptances(artifact["id"])[0]
        self.assertEqual(report["outcome"], "unavailable")
        self.assertEqual(report["code"], "verification_timeout")
        self.assertEqual(report["startup"]["status"], "passed")
        self.assertEqual(report["case_results"][0]["status"], "failed")
        self.assertEqual(self.store.job(job["id"])["state"], "needs_review")

    def test_missing_docker_records_unavailable_but_cancellation_does_not_complete(self):
        artifact = self.artifact()
        pipeline = Pipeline(self.store)
        for code in ("runtime_unavailable", "cancelled"):
            self.submit(artifact)
            job = self.store.claim("runtime-worker", "verification")
            with patch("template_factory.blueprint_runtime.BlueprintRuntimeVerifier.verify", side_effect=FactoryError("synthetic " + code, code, 409)):
                if code == "cancelled":
                    with self.assertRaises(FactoryError):
                        pipeline.run(job)
                else:
                    pipeline.run(job)
            reports = self.store.acceptances(artifact["id"])
            self.assertEqual(len(reports), 1)
            self.assertEqual(reports[0]["outcome"], "unavailable")

    def test_new_production_can_request_binding_without_changing_legacy_default(self):
        scenario = self.store.save_scenario({
            "leaf": "bookmark-manager", "name": "Synthetic runtime-capable scenario",
            "audience": "local fixture", "objective": "store and reopen synthetic bookmarks",
            "workflow": ["save bookmark", "reopen"], "acceptance": ["saved bookmark remains"], "status": "ready",
        })
        request = {"kind": "blueprint-production", "name": "test", "model": "test/model", "scenario_ids": [scenario["id"]], "scenario_revisions": {scenario["id"]: scenario["revision"]}}
        with self.assertRaisesRegex(FactoryError, "protocol"):
            self.store.create_batch({**request, "acceptance_protocol": "unknown"})
        legacy = self.store.create_batch(request)
        self.store.batch_action(legacy["id"], "cancel")
        modern = self.store.create_batch({**request, "acceptance_protocol": "atlas.acceptance-runner.v1"})
        self.assertNotIn("acceptance_protocol", legacy["jobs"][0]["snapshot"]["config"])
        self.assertEqual(modern["jobs"][0]["snapshot"]["config"]["acceptance_protocol"], "atlas.acceptance-runner.v1")

    @unittest.skipUnless(os.environ.get("ATLAS_RUN_DOCKER_INTEGRATION") == "1", "opt-in synthetic Docker queue integration")
    def test_real_docker_through_api_queue_and_pinned_frozen_source(self):
        # Fixture product prose is irrelevant here: replace its test bodies with
        # explicitly synthetic transport probes, not historical product verdicts.
        spec = json.loads((self.source / "template.json").read_text())
        program = """const args=process.argv.slice(2);
const id=args[args.indexOf('--case')+1], base=args[args.indexOf('--base-url')+1];
(async()=>{const r=await fetch(base+'/value.txt'), value=await r.text();
const missing=await fetch(base+'/missing');
const assertions=[{id:'actual-http-value',passed:r.status===200&&value==='queue-integration-value',detail:'HTTP '+r.status+' body '+value},
{id:'actual-http-negative',passed:missing.status===404,detail:'missing resource HTTP '+missing.status}];
const ok=assertions.every(x=>x.passed);
console.log(JSON.stringify({schema:'atlas.acceptance-result.v1',case_id:id,status:ok?'passed':'failed',assertions}));process.exit(ok?0:1);
})().catch(e=>{console.error(e.message);process.exit(2)});
"""
        for name in {row["implementation"] for row in spec["acceptance"]}:
            self.assertTrue(name.endswith((".cjs", ".js", ".mjs")))
            (self.source / name).write_text(program)
        artifact = self.artifact()
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as archive:
            archive.writestr("value.txt", "queue-integration-value")
            archive.writestr("delivery.json", json.dumps({
                "schema": "atlas.application-delivery.v1", "root": ".", "files": ["value.txt"],
                "runtime": {"profile": "static-web", "start": ["python3", "-m", "http.server", "8080"], "port": 8080},
            }))
        self.submit(artifact, source_archive_base64=base64.b64encode(output.getvalue()).decode(), timeout=120)
        job = self.store.claim("real-docker-worker", "verification")
        Pipeline(self.store).run(job)
        report = self.store.acceptances(artifact["id"])[0]
        self.assertEqual(report["outcome"], "passed", report)
        expected = [row["id"] for row in spec["acceptance"] if row["phase"] == spec["phases"][0]["id"]]
        self.assertEqual([row["id"] for row in report["case_results"]], expected)
        self.assertTrue(all(len(row["assertions"]) == 2 for row in report["case_results"]))
        self.assertTrue(report["cleanup"]["success"])
        self.assertEqual(report["input_digest"], job["snapshot"]["input_digest"])
        self.assertEqual(self.store.artifacts()[0]["level"], "L0")


if __name__ == "__main__":
    unittest.main()
