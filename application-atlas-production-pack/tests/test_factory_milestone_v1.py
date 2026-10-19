"""Campaign-bound G1 assessment and plan-wide control contracts; no provider calls."""
import json
import base64
import hashlib
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from template_factory.store import FactoryError, FactoryStore, canonical, digest, now
from template_factory.v1_batches import BatchService, DEFAULT_CAMPAIGN_ID, G1_REQUIRED_CHECKS, _g1_source_digest, _npm_audit_report_passes
from template_factory.cases import CaseLibrary

PACK = Path(__file__).resolve().parents[1]


class FactoryMilestoneV1Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        shutil.copy(PACK / "mvp_apps_classified.json", self.pack / "mvp_apps_classified.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES('bookmark-manager','Bookmarks','书签','Save links','Links')")
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.scene = self.store.save_scenario({
            "leaf": "bookmark-manager", "name": "Save and reopen", "audience": "Personal",
            "objective": "Save links and reopen", "workflow": ["save", "read"],
            "acceptance": ["Saved links remain"], "status": "ready",
        })
        self.service = BatchService(self.store)

    def _create_canonical_basis(self):
        library = CaseLibrary(self.store)
        snapshot_root = self.store.root / "source-snapshots" / "fixture"
        snapshot_root.mkdir(parents=True)
        source = snapshot_root / "src" / "main.py"
        source.parent.mkdir()
        source.write_text("def save_bookmark():\n    return True\n", encoding="utf-8")
        license_path = snapshot_root / "LICENSE"
        license_path.write_text("MIT License fixture\n", encoding="utf-8")
        files = {"src/main.py": hashlib.sha256(source.read_bytes()).hexdigest(),
                 "LICENSE": hashlib.sha256(license_path.read_bytes()).hexdigest()}
        payload = {
            "app_id": "todoist", "case_id": "case:g1-positive",
            "source_snapshots": [{
                "repository": "https://github.com/example/bookmarks", "repo_id": "github:atlas-g1-fixture",
                "commit_sha": "a" * 40, "collected_at": "2026-10-19T10:00:00Z",
                "strategy_version": "archive-v1", "local_root": str(snapshot_root),
                "files": files, "license_files": ["LICENSE"],
                "license": {"spdx_id_supplement": "MIT", "supplement_source": "fixture metadata",
                            "supplement_collected_at": "2026-10-19T10:00:00Z", "notice_hashes": {"LICENSE": files["LICENSE"]}},
            }],
            "research": {"summary": "A pinned source records bookmark storage.", "scope": "save and reopen",
                         "unknowns": ["This fixture did not run the source application."], "input_digest": "fixture-input"},
            "observations": [{"evidence_id": "ev-g1-save", "kind": "code_observation",
                              "statement": "save_bookmark returns success after saving.",
                              "location": {"commit_sha": "a" * 40, "path": "src/main.py",
                                           "file_digest": files["src/main.py"], "symbol": "save_bookmark"}}],
            "scenario_links": [{"scenario_id": self.scene["id"], "scenario_revision": self.scene["revision"],
                                "reason": "The observed save operation supports the fixed workflow.",
                                "workflow_support": ["save"], "adopted_scope": ["save bookmark"],
                                "exclusions": ["cloud sync"], "evidence_ids": ["ev-g1-save"]}],
        }
        case = library.commit_research(payload, "g1-positive-case") ["case"]
        library.record_evidence_review(case["case_id"], case["revision"], "ev-g1-save", "accepted",
                                       "fixture-independent-reviewer", "independent_agent")
        basis = library.evidence_basis([{"case_id": case["case_id"], "revision": case["revision"]}],
                                       self.scene["id"], self.scene["revision"])
        library.require_admissible(basis)
        return basis

    def _check_manifest(self, plan, sample_id, development_snapshot):
        checks_dir = self.root / "verification"
        checks_dir.mkdir(exist_ok=True)
        checks = {}
        skip_names = [
            "test_cli_smoke_and_mixed_python_node_acceptance",
            "test_mixed_python_node_cases_pass_against_stdlib_web_app_and_preserve_source",
            "test_negative_acceptance_valid_failed_json_and_nonzero_exit_is_blocked",
            "test_node_web_launcher_serves_real_request_to_python_tester",
            "test_startup_exception_exit_is_blocked_and_traceback_is_preserved",
            "test_startup_exception_traceback_is_captured_from_stderr",
            "test_total_timeout_removes_every_owned_container",
            "test_real_docker_through_api_queue_and_pinned_frozen_source",
        ]
        logs = {
            "python_audit": "No known vulnerabilities found\n",
            "ruff": "All checks passed!\n",
            "backend_tests": "".join(f"{name} (fixture.Case) ... skipped 'set ATLAS_RUN_DOCKER_INTEGRATION=1 to run isolated local Docker tests'\n" for name in skip_names[:7])
                            + f"{skip_names[-1]} (fixture.Case) ... skipped 'opt-in synthetic Docker queue integration'\n"
                            + "Ran 518 tests in 42.0s\n\nOK (skipped=8)\n",
            "atlas_export": "sqlite -> atlas.sqlite\njson   -> atlas.json\n",
            "web_gen": "npm run gen\nGenerated web data\n",
            "web_verify_data": "npm run verify-data\nVerified web data\n",
            "npm_audit": "found 0 vulnerabilities\n",
            "web_typecheck": "> tsc --noEmit\n",
            "web_unit": "# tests 9\n# pass 9\n# fail 0\n# skipped 0\n",
            "web_build": "vite build\n✓ built in 1.2s\n",
            "default_e2e": "25 passed (1.2m)\n",
            "factory_e2e": "25 passed (1.2m)\n",
            "docker_integration": json.dumps({"status": "passed", "tests_run": 6, "skipped": 0}) + "\n",
        }
        for name, requirement in G1_REQUIRED_CHECKS.items():
            raw = logs[name].encode()
            log_path = checks_dir / (name + ".txt")
            log_path.write_bytes(raw)
            argv = list(requirement["argv"])
            checks[name] = {
                "status": "passed", "exit_code": 0, "argv": argv, "cwd": requirement["cwd"],
                "skipped": requirement.get("allowed_skips", 0), "log_path": str(log_path.relative_to(self.root)),
                "log_sha256": hashlib.sha256(raw).hexdigest(),
            }
            if name == "docker_integration":
                checks[name]["env"] = requirement["env"]
            if requirement["tests"]:
                checks[name]["tests_run"] = {"backend_tests": 518, "web_unit": 9,
                                              "default_e2e": 25, "factory_e2e": 25,
                                              "docker_integration": 6}[name]
        path = checks_dir / "checks.json"
        path.write_text(json.dumps({
            "schema": "atlas.g1-verification-manifest.v1", "campaign_id": plan["campaign_id"],
            "plan_id": plan["id"], "plan_digest": plan["digest"], "sample_scenario_id": sample_id,
            "source_tree_sha256": _g1_source_digest(self.root), "support_scope": plan["support"],
            "checks": checks,
            "development_export": {"artifact_id": development_snapshot["artifact_id"],
                                   "artifact_digest": development_snapshot["artifact_digest"],
                                   "selected_phase": "P0", "archive_path": development_snapshot["handoff_archive"],
                                   "archive_sha256": development_snapshot["handoff_sha256"]},
        }), encoding="utf-8")
        return path

    def _build_synthetic_persisted_g1_chain(self):
        """Build the full persisted chain with explicit test doubles, never a real provider/runtime."""
        import test_blueprints as blueprint_fixtures
        from template_factory.artifacts import archive_tree
        from template_factory.blueprints import freeze_blueprint
        from template_factory.development_jobs import _response_archive, queue_development, run_development
        from template_factory.runtime_jobs import queue_runtime

        basis = self._create_canonical_basis()
        plan = self.preview(runtime_sample_ids=[self.scene["id"]], campaign_id="positive-g1-fixture")
        self.assertEqual(plan["seeds"][0]["case_basis"], basis)
        self.run_plan(plan)
        production = self.store.claim("fixture-production", "production")
        self.assertIsNotNone(production)

        source = self.root / "blueprint-source"
        shutil.copytree(blueprint_fixtures.SAMPLE, source)
        spec = json.loads((source / "template.json").read_text(encoding="utf-8"))
        spec["scenario"] = self.scene
        (source / "inputs" / "scenario.json").write_text(json.dumps(self.scene, ensure_ascii=False), encoding="utf-8")
        spec["case_basis"] = basis
        spec["case_design"] = [{"disposition": "adopted", "evidence_ids": ["ev-g1-save"],
                                "rationale": "The pinned save observation grounds this fixture decision."}]
        spec["phase_required_evidence"] = {"P0": [{"id": "restart-check", "kind": "external",
                                                   "description": "Independent persisted-data restart check.",
                                                   "executor": "independent-restart-checker"}]}
        runner = {"schema": "atlas.acceptance-runner.v1", "result_schema": "atlas.acceptance-result.v1",
                  "cases": {case["id"]: {"args": ["--case", "{case_id}", "--base-url", "{base_url}"]}
                            for case in spec["acceptance"]}}
        (source / "acceptance" / "runner.json").write_text(json.dumps(runner), encoding="utf-8")
        blueprint_fixtures.BlueprintTests.rewrite(type("Fixture", (), {"source": source})(), lambda row: row.update(spec))
        # rewrite() owns the normative acceptance-plan and integrity refresh.
        template_path = source / "template.json"
        spec = json.loads(template_path.read_text(encoding="utf-8"))
        spec["scenario"] = self.scene
        (source / "inputs" / "scenario.json").write_text(json.dumps(self.scene, ensure_ascii=False), encoding="utf-8")
        spec["case_basis"] = basis
        spec["case_design"] = [{"disposition": "adopted", "evidence_ids": ["ev-g1-save"],
                                "rationale": "Pinned observation supports the save workflow."}]
        spec["phase_required_evidence"] = {"P0": [{"id": "restart-check", "kind": "external",
                                                   "description": "Independent persisted-data restart check.",
                                                   "executor": "independent-restart-checker"}]}
        template_path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
        integrity = __import__("template_factory.artifacts", fromlist=["tree_manifest"]).tree_manifest(source)
        integrity.pop("integrity.json")
        (source / "integrity.json").write_text(json.dumps({"template_version": spec["version"], "sha256": integrity}), encoding="utf-8")

        v1 = production["snapshot"]["v1"]
        provenance = {"origin": "fixture-only; not a model output", "scenario": self.scene,
                      "case_basis": basis, "case_design": spec["case_design"], "v1": v1,
                      "model": "fixture/model"}
        bundle = self.store.root / "artifacts" / "fixture-blueprint"
        bundle.parent.mkdir(parents=True, exist_ok=True)
        frozen = freeze_blueprint(source, bundle, provenance)
        archive_path = bundle.parent / "fixture-blueprint.zip"
        archive_tree(bundle / "source", archive_path)
        body = {**frozen, "artifact_type": "product-blueprint", "package_digest": digest(integrity),
                "leaf": self.scene["leaf"], "scenario_id": self.scene["id"],
                "scenario_name": self.scene["name"], "scenario_revision": self.scene["revision"],
                "created_at": now(), "bundle_path": bundle.relative_to(self.store.root).as_posix(),
                "archive_path": archive_path.relative_to(self.store.root).as_posix(),
                "archive_sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(),
                "formal_checks": [], "reports": []}
        artifact_id = self.store.add_artifact(production["id"], production["token"], body)
        self.store.reconcile_outbox()
        review = self.store.claim("fixture-review", "verification")
        self.assertEqual(review["kind"], "cognitive-review")
        self.store.complete_acceptance(review["id"], review["token"], {"outcome": "passed", "scope": "synthetic fixture only"})
        artifact = next(a for a in self.store.artifacts() if a["id"] == artifact_id)
        self.store.artifact_action(artifact_id, {"action": "publish", "expected_digest": artifact["digest"],
                                                 "review": "Fixture exercises formal publication bindings."})
        artifact = next(a for a in self.store.artifacts() if a["id"] == artifact_id)
        # Keep older blocked and unreviewed candidates in the history. They
        # must not mask the later eligible revision selected for the sample.
        parent_batch = self.service.execution(plan["id"])["id"]
        with self.store.connect(True) as con:
            for suffix, review_outcome, state in (("failed", "blocked", "published"), ("needs-review", None, "draft")):
                old_id, old_job, old_review = "tpl-g1-" + suffix, "job-g1-" + suffix, "job-review-g1-" + suffix
                old_at = "2000-01-01T00:00:00Z" if suffix == "failed" else "2001-01-01T00:00:00Z"
                snapshot = dict(production["snapshot"])
                snapshot.setdefault("leaf", self.store.leaf(self.scene["leaf"]))
                snapshot.setdefault("config", plan["config"])
                con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                    old_job, parent_batch, "blueprint-production", "completed", "fixture-old-candidate", 1,
                    None, None, canonical(snapshot), None, old_at, old_at))
                old_body = {key: value for key, value in artifact.items() if key not in {"catalog_eligible", "catalog_blockers", "review_status", "state"}}
                old_body.update({"id": old_id, "job_id": old_job, "created_at": old_at})
                con.execute("INSERT INTO artifact VALUES(?,?,?,?,?,?,?)", (
                    old_id, old_job, artifact["digest"], "L0", state, canonical(old_body), old_at))
                if review_outcome:
                    review_snapshot = {"artifact_id": old_id, "artifact_digest": artifact["digest"],
                                       "leaf": self.store.leaf(self.scene["leaf"])}
                    con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        old_review, parent_batch, "cognitive-review", "completed", "fixture-blocked-review", 1,
                        None, None, canonical(review_snapshot), None, old_at, old_at))
                    con.execute("INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)", (
                        "acc-g1-failed", old_id, artifact["digest"], "cognitive-review", old_review,
                        canonical({"outcome": review_outcome}), old_at))

        queue_development(self.store, artifact, {
            "expected_digest": artifact["digest"], "phase": "P0", "request_key": "positive-g1-development",
            "model": "fixture/model", "project_name": "g1-positive-app"})
        development = self.store.claim("fixture-development", "production")
        self.assertEqual(development["kind"], "application-development")
        attempt = self.root / "development-attempt"
        attempt.mkdir()

        def fake_agent(*_args, **_kwargs):
            return {"files": {
                "index.html": "<main>Fixture app, not runtime quality evidence.</main>",
                "delivery.json": json.dumps({"schema": "atlas.application-delivery.v1", "root": ".",
                                             "files": ["index.html"], "runtime": {
                                                 "profile": "python-web", "start": ["python3", "-m", "http.server", "8000"], "port": 8000}}),
            }}

        def checkpoint(name, create):
            existing = self.store.checkpoint(development["id"], name)
            if existing:
                return existing["result"]
            value = create()
            self.store.checkpoint(development["id"], name, {"result": value, "digest": digest(value)}, development["token"])
            return value

        delivery = run_development(type("Pipeline", (), {"store": self.store})(), development, attempt,
                                   fake_agent, lambda *_args: None, checkpoint)
        dev_snapshot = self.store.job(development["id"])["snapshot"]

        application_zip = _response_archive(fake_agent())
        runtime_batch = queue_runtime(self.store, artifact, {
            "expected_digest": artifact["digest"], "phase": "P0", "execution_confirmed": True,
            "source_archive_base64": base64.b64encode(application_zip).decode("ascii"), "timeout": 30})
        runtime_job = next(job for job in runtime_batch["jobs"] if job["kind"] == "blueprint-runtime")
        runtime_snapshot = runtime_job["snapshot"]
        target_digest = digest(runtime_snapshot["target_binding"])
        proof_path = self.store.root / "jobs" / runtime_job["id"] / "attempt-1" / "runtime-evidence" / "external" / "restart-check.json"
        proof_path.parent.mkdir(parents=True)
        executor = {"kind": "independent_executor", "name": "independent-restart-checker", "version": "fixture-1"}
        proof_raw = json.dumps({"schema": "atlas.phase-evidence.v1", "requirement_id": "restart-check",
                               "target_digest": target_digest, "outcome": "passed", "executor": executor,
                               "details": "Synthetic persisted proof record; no app/container was executed."}, sort_keys=True).encode()
        proof_path.write_bytes(proof_raw)
        evidence_record = {"evidence_path": proof_path.relative_to(self.store.root).as_posix(),
                           "sha256": hashlib.sha256(proof_raw).hexdigest(), "executor": executor}
        runtime_report = {"id": "acceptance-g1-fixture", "method": "blueprint-runtime", "digest": artifact["digest"],
                          "selected_phase": "P0", "outcome": "passed", "suite_status": "passed", "phase_status": "passed",
                          "startup": {"status": "passed"}, "cleanup": {"success": True},
                          "target_binding": runtime_snapshot["target_binding"],
                          "case_results": [{"id": case_id, "status": "passed"} for case_id in runtime_snapshot["selected_case_ids"]],
                          "required_evidence": runtime_snapshot["phase_requirements"],
                          "registered_phase_evidence": {"restart-check": evidence_record}}
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET state='completed',stage='fixture-runtime-verified' WHERE id=?", (runtime_job["id"],))
            con.execute("UPDATE batch SET state='completed' WHERE id=?", (runtime_batch["id"],))
            con.execute("INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)", (
                runtime_report["id"], artifact_id, artifact["digest"], "blueprint-runtime", runtime_job["id"],
                canonical(runtime_report), now()))

        return plan, artifact, dev_snapshot, delivery, runtime_snapshot

    def test_complete_persisted_fixture_chain_can_pass_and_mutations_block(self):
        plan, artifact, development_snapshot, delivery, runtime_snapshot = self._build_synthetic_persisted_g1_chain()
        manifest_path = self._check_manifest(plan, self.scene["id"], development_snapshot)
        passed = self.service.assess_g1(plan["id"], manifest_path)
        self.assertTrue(passed["passed"], passed["reasons"])
        self.assertEqual(passed["status"], "passed")
        self.assertEqual(passed["artifact_digest"], artifact["digest"])
        self.assertEqual(passed["development_delivery_archive_sha256"], delivery["archive_sha256"])

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["checks"]["factory_e2e"]["argv"][-1:] = ["e2e/factory-tests/v1.spec.ts"]
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        rejected_command = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_command["passed"])
        self.assertIn("check_command_mismatch:factory_e2e", rejected_command["reasons"])

        manifest_path = self._check_manifest(plan, self.scene["id"], development_snapshot)
        log_path = self.root / "verification" / "factory_e2e.txt"
        log_path.write_text(log_path.read_text() + "tampered after recorded check\n")
        rejected_log = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_log["passed"])
        self.assertIn("check_log_digest_mismatch:factory_e2e", rejected_log["reasons"])

        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["source_tree_sha256"] = "0" * 64
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        rejected_source = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_source["passed"])
        self.assertIn("source_or_test_tree_changed", rejected_source["reasons"])

        with self.store.connect() as con:
            runtime_job = con.execute("SELECT id,snapshot FROM job WHERE kind='blueprint-runtime' ORDER BY created_at DESC,rowid DESC LIMIT 1").fetchone()
        proof = self.store.root / "jobs" / runtime_job["id"] / "attempt-1" / "runtime-evidence" / "external" / "restart-check.json"
        original = proof.read_bytes()
        proof.write_bytes(original + b"tampered")
        rejected_proof = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_proof["passed"])
        self.assertTrue(any(reason.startswith(("P0_external_evidence_digest_mismatch:", "P0_external_evidence_unreadable:")) for reason in rejected_proof["reasons"]), rejected_proof["reasons"])
        proof.write_bytes(original)

        with self.store.connect() as con:
            runtime_snapshot = json.loads(runtime_job["snapshot"])
        app_archive = self.store.root / runtime_snapshot["submission_path"]
        app_archive = app_archive.parent / "application.zip"
        original_archive = app_archive.read_bytes()
        app_archive.write_bytes(original_archive + b"tampered")
        rejected_app = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_app["passed"])
        self.assertTrue(any(reason.startswith("P0_application_delivery") for reason in rejected_app["reasons"]))
        app_archive.write_bytes(original_archive)

        bundle = self.store.root / artifact["bundle_path"] / "source" / "acceptance" / "runner.json"
        original_suite = bundle.read_bytes()
        bundle.write_bytes(original_suite + b"\n")
        rejected_suite = self.service.assess_g1(plan["id"], manifest_path)
        self.assertFalse(rejected_suite["passed"])
        self.assertTrue(any("integrity_failed" in reason or "frozen_template" in reason for reason in rejected_suite["reasons"]))
        bundle.write_bytes(original_suite)

    def test_npm_audit_evidence_obeys_high_threshold_and_requires_summary(self):
        moderate = """# npm audit report
postcss-selector-parser <7.1.6
Severity: moderate
2 moderate severity vulnerabilities
To address all issues, run npm audit fix.
"""
        self.assertTrue(_npm_audit_report_passes(moderate))
        self.assertTrue(_npm_audit_report_passes("found 0 vulnerabilities\n"))
        self.assertTrue(_npm_audit_report_passes("found 1 low severity vulnerability\n"))
        self.assertFalse(_npm_audit_report_passes("1 high severity vulnerability\n"))
        self.assertFalse(_npm_audit_report_passes(
            "Severity: high\nfound 0 vulnerabilities\n"
        ))
        self.assertFalse(_npm_audit_report_passes(""))
        self.assertFalse(_npm_audit_report_passes("npm ERR! audit failed\nfound 0 vulnerabilities\n"))
        self.assertFalse(_npm_audit_report_passes(
            "Severity: unknown\n1 moderate severity vulnerability\n"
        ))
        self.assertFalse(_npm_audit_report_passes("# npm audit report\nSeverity: moderate\n"))
        self.assertFalse(_npm_audit_report_passes("2 moderate vulnerabilities\n"))

    def tearDown(self):
        self.temp.cleanup()

    def preview(self, **extra):
        return self.service.preview({"scenario_ids": [self.scene["id"]], "model": "fixture/model", **extra})

    def run_plan(self, plan):
        return self.service.run(plan["id"], {"expected_plan_digest": plan["digest"], "idempotency_key": "run:" + plan["id"]})

    def test_default_campaign_continues_current_campaign_and_explicit_override_is_preserved(self):
        self.assertEqual(self.preview()["campaign_id"], DEFAULT_CAMPAIGN_ID)
        first = self.preview(campaign_id="first-executed-campaign")
        self.run_plan(first)
        self.assertEqual(self.preview()["campaign_id"], "first-executed-campaign")
        self.assertEqual(self.preview(campaign_id="operator-campaign")["campaign_id"], "operator-campaign")

    def test_legacy_global_or_other_campaign_gate_cannot_unlock_t08(self):
        scenes = [self.scene]
        for index in range(2):
            scenes.append(self.store.save_scenario({**self.scene, "name": f"Scenario {index}", "status": "ready"}))
        plan = self.service.preview({
            "scenario_ids": [scene["id"] for scene in scenes], "runtime_sample_ids": [scene["id"] for scene in scenes],
            "model": "fixture/model", "segment": "T08", "campaign_id": "target-campaign",
        })
        with self.store.connect(True) as con:
            con.execute("INSERT INTO v1_gate VALUES('G1',?,?)", (canonical({"passed": True}), now()))
            con.execute("INSERT INTO v1_campaign_gate VALUES(?,?,?,?)", (
                "other-campaign", "G1", canonical({"passed": True, "campaign_id": "other-campaign"}), now(),
            ))
        with self.assertRaises(FactoryError) as caught:
            self.run_plan(plan)
        self.assertEqual(caught.exception.code, "g1_required")
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM v1_execution").fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT count(*) FROM job").fetchone()[0], 0)

    def test_stale_campaign_gate_source_digest_cannot_unlock_t08(self):
        scenes = [self.scene]
        for index in range(2):
            scenes.append(self.store.save_scenario({**self.scene, "name": f"Stale gate scenario {index}", "status": "ready"}))
        plan = self.service.preview({
            "scenario_ids": [scene["id"] for scene in scenes],
            "runtime_sample_ids": [scene["id"] for scene in scenes],
            "model": "fixture/model", "segment": "T08", "campaign_id": "stale-campaign",
        })
        with self.store.connect(True) as con:
            con.execute("INSERT INTO v1_campaign_gate VALUES(?,?,?,?)", (
                "stale-campaign", "G1", canonical({"passed": True, "campaign_id": "stale-campaign", "source_tree_sha256": "stale"}), now(),
            ))
        with self.assertRaises(FactoryError) as caught:
            self.run_plan(plan)
        self.assertEqual(caught.exception.code, "g1_required")

    def test_missing_or_boolean_only_manifest_records_blocked_assessment_not_a_pass(self):
        plan = self.preview(runtime_sample_ids=[self.scene["id"]])
        missing = self.service.assess_g1(plan["id"], "evidence/does-not-exist.json")
        self.assertFalse(missing["passed"])
        self.assertEqual(missing["status"], "blocked")
        self.assertIn("manifest_missing_or_unreadable", missing["reasons"])
        self.assertFalse(self.service.gate(plan["campaign_id"])["passed"])

        manifest = self.root / "evidence" / "boolean-only.json"
        manifest.parent.mkdir()
        manifest.write_text(json.dumps({
            "schema": "atlas.g1-verification-manifest.v1", "passed": True,
            "campaign_id": plan["campaign_id"], "plan_id": plan["id"],
            "plan_digest": plan["digest"], "sample_scenario_id": self.scene["id"],
        }))
        rejected = self.service.assess_g1(plan["id"], str(manifest))
        self.assertFalse(rejected["passed"])
        self.assertIn("required_check_records_missing", rejected["reasons"])
        self.assertIn("sample_template_missing", rejected["reasons"])

    def test_plan_control_updates_parent_and_existing_runtime_descendant_atomically(self):
        plan = self.preview()
        run = self.run_plan(plan)
        parent_batch = run["batch"]["id"]
        child_batch, child_job = "bat_child", "job_child"
        snapshot = {"v1": {"plan_id": plan["id"], "campaign_id": plan["campaign_id"]}, "config": {}}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (child_batch, "running", canonical({"concurrency": 1}), now()))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                child_job, child_batch, "blueprint-runtime", "running", "acceptance", 1,
                "owned-token", 9999999999, canonical(snapshot), None, now(), now(),
            ))
        self.service.action(plan["id"], "pause")
        with self.store.connect() as con:
            states = {row["id"]: row["state"] for row in con.execute("SELECT id,state FROM batch WHERE id IN (?,?)", (parent_batch, child_batch))}
            self.assertEqual(set(states.values()), {"paused"})
            self.assertEqual(con.execute("SELECT state,token FROM job WHERE id=?", (child_job,)).fetchone()["token"], "owned-token")
        self.service.action(plan["id"], "resume")
        with self.store.connect() as con:
            states = {row["state"] for row in con.execute("SELECT state FROM batch WHERE id IN (?,?)", (parent_batch, child_batch))}
            self.assertEqual(states, {"running"})
        self.service.action(plan["id"], "cancel")
        with self.store.connect() as con:
            states = {row["state"] for row in con.execute("SELECT state FROM batch WHERE id IN (?,?)", (parent_batch, child_batch))}
            self.assertEqual(states, {"cancelled"})
            job = con.execute("SELECT state,token,lease FROM job WHERE id=?", (child_job,)).fetchone()
            self.assertEqual(tuple(job), ("cancelled", None, None))


if __name__ == "__main__":
    unittest.main()
