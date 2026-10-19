"""Pinned application submissions and independent runtime jobs; no model calls."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import time

from atlas_runtime import atomic_json
from .artifacts import tree_manifest
from .blueprints import decode_archive, verify_frozen
from .delivery import prepare_application
from .store import FactoryError, canonical, digest, integer, now, uid


def runtime_support(source, spec):
    from .blueprint_runtime import validate_runner_manifest

    result = {
        "supported": False,
        "protocol": "atlas.acceptance-runner.v1",
        "result_schema": "atlas.acceptance-result.v1",
        "network": "none",
        "reason": None,
    }
    try:
        validate_runner_manifest(source, spec)
        result["supported"] = True
    except FactoryError as error:
        result["reason"] = error.code
    return result


def queue_runtime(store, artifact, value):
    from .api import controlled_path
    from .blueprint_runtime import phase_required_evidence, validate_runner_manifest

    if artifact.get("artifact_type") != "product-blueprint":
        raise FactoryError("runtime submission requires a cognitive template", "wrong_artifact_type", 409)
    if value.get("expected_digest") != artifact["digest"]:
        raise FactoryError("artifact version changed", "revision_conflict", 409)
    if value.get("execution_confirmed") is not True:
        raise FactoryError("confirm isolated execution of the application and frozen suite", "execution_confirmation_required", 409)
    bundle = controlled_path(store, artifact["bundle_path"])
    spec = verify_frozen(bundle, artifact["digest"])
    phase = value.get("phase")
    if phase not in [p["id"] for p in spec["phases"]]:
        raise FactoryError("choose a phase declared in the blueprint")
    runner = validate_runner_manifest(bundle / "source", spec, phase)
    requirements = phase_required_evidence(spec, phase)
    suite_inventory = tree_manifest(bundle / "source")
    suite_digest = hashlib.sha256(json.dumps(suite_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    config = {
        "kind": "blueprint-runtime", "name": "Independent application acceptance: " + artifact["manifest"]["name"],
        "model": "", "concurrency": 1,
        "timeout": integer(value.get("timeout", 300), "timeout", 30, 7200),
        "language": value.get("language", "zh"),
    }
    v1 = artifact.get("provenance", {}).get("v1")
    if v1:
        from .budget import BudgetLedger
        remaining = BudgetLedger(store, campaign_id=v1["campaign_id"]).phase_remaining(
            v1["product_id"], v1["segment"], plan_id=v1.get("plan_id"))
        if remaining is not None:
            if remaining <= 0:
                raise FactoryError("runtime segment deadline exhausted", "budget_deadline", 409)
            config["timeout"] = min(config["timeout"], remaining)
    if config["language"] not in ("zh", "en"):
        raise FactoryError("language must be zh or en")
    archive = decode_archive(value.get("source_archive_base64"))
    submission = store.root / "submissions" / uid("sub")
    submission.mkdir(parents=True)
    try:
        metadata = prepare_application(archive, submission / "application")
        archive_hash = hashlib.sha256(archive).hexdigest()
        app_root = submission / "application" / metadata["app_root"]
        application_inventory = tree_manifest(app_root)
        application_digest = hashlib.sha256(json.dumps(application_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        scenario = artifact.get("provenance", {}).get("scenario", {})
        case_basis = artifact.get("provenance", {}).get("case_basis")
        if case_basis is None:
            case_basis = store.job(artifact["job_id"])["snapshot"].get("case_basis")
        target_binding = {
            "target_kind": "generated_application",
            "artifact_id": artifact["id"], "artifact_digest": artifact["digest"],
            "application_digest": application_digest, "suite_digest": suite_digest,
            "selected_phase": phase, "selected_case_ids": runner["selected_case_ids"],
            "scenario_id": scenario.get("id") or artifact.get("scenario_id"),
            "scenario_revision": scenario.get("revision") or artifact.get("scenario_revision"),
            "case_basis_digest": (case_basis.get("basis_digest") if isinstance(case_basis, dict)
                                  else None),
        }
        (submission / "application.zip").write_bytes(archive)
        atomic_json(submission / "delivery-receipt.json", metadata)
        pinned = {
            "schema": "atlas.factory-runtime-input.v1",
            "artifact_id": artifact["id"], "artifact_digest": artifact["digest"],
            "bundle_path": artifact["bundle_path"], "selected_phase": phase,
            "submission_path": str((submission / "application").relative_to(store.root)),
            "archive_sha256": archive_hash, "delivery": metadata,
            "suite_digest": suite_digest, "selected_case_ids": runner["selected_case_ids"],
            "phase_requirements": requirements, "target_binding": target_binding,
            "case_basis": case_basis,
        }
        snapshot = {
            **pinned, "input_digest": digest(pinned),
            "leaf": store.job(artifact["job_id"])["snapshot"]["leaf"],
            "scenario": artifact["provenance"]["scenario"], "config": config,
            "execution_confirmed": True,
            **({"v1": v1} if v1 else {}),
        }
        batch_id, job_id, at = uid("bat"), uid("job"), now()
        with store.connect(True) as con:
            parent_state = "running"
            if v1 and v1.get("plan_id"):
                parent = con.execute(
                    "SELECT b.state FROM v1_execution e JOIN batch b ON b.id=e.batch_id WHERE e.plan_id=?",
                    (v1["plan_id"],),
                ).fetchone()
                if parent:
                    if parent[0] == "cancelled":
                        raise FactoryError("parent plan is cancelled", "cancelled", 409)
                    if parent[0] == "paused":
                        parent_state = "paused"
            if con.execute(
                "SELECT 1 FROM job WHERE kind='blueprint-runtime' AND state IN ('queued','running') "
                "AND json_extract(snapshot,'$.artifact_id')=?", (artifact["id"],)
            ).fetchone():
                raise FactoryError("application acceptance already queued or running", "conflict", 409)
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (batch_id, parent_state, canonical(config), at))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                job_id, batch_id, "blueprint-runtime", "queued", "acceptance", 1, None, None,
                canonical(snapshot), None, at, at,
            ))
        return store.batch(batch_id)
    except BaseException:
        shutil.rmtree(submission, ignore_errors=True)
        raise


def register_phase_evidence(store, artifact_id, run_id, payload):
    """Persist independently executed, host-produced evidence for one runtime run.

    This is an internal host service, not an API endpoint. The evidence file
    must be written by the declared independent executor beneath this run's
    host evidence directory; an application's upload metadata cannot satisfy it.
    """
    from .api import controlled_path

    if not isinstance(payload, dict):
        raise FactoryError("phase evidence payload must be an object")
    requirement_id = payload.get("requirement_id")
    target_digest = payload.get("target_digest")
    evidence_path = payload.get("evidence_path")
    expected_sha = payload.get("sha256")
    executor = payload.get("executor")
    if (not isinstance(requirement_id, str) or not isinstance(target_digest, str)
            or not isinstance(evidence_path, str) or not re.fullmatch(r"[0-9a-f]{64}", str(expected_sha))
            or not isinstance(executor, dict)):
        raise FactoryError("invalid phase evidence registration")

    with store.connect(True) as con:
        row = con.execute("SELECT body FROM acceptance WHERE id=? AND artifact_id=?", (run_id, artifact_id)).fetchone()
        if not row:
            raise FactoryError("runtime acceptance run not found", "not_found", 404)
        report = json.loads(row[0])
        if report.get("method") != "blueprint-runtime":
            raise FactoryError("phase evidence requires a blueprint runtime run", "wrong_acceptance_method", 409)
        current = con.execute("SELECT digest FROM artifact WHERE id=?", (artifact_id,)).fetchone()
        if not current or current[0] != report.get("digest"):
            raise FactoryError("phase evidence target artifact changed", "stale_phase_evidence", 409)
        if report.get("suite_status") != "passed" or not isinstance(report.get("target_binding"), dict):
            raise FactoryError("runtime suite has not passed for this bound target", "phase_evidence_unavailable", 409)
        target = report["target_binding"]
        if target.get("artifact_id") != artifact_id or target.get("artifact_digest") != report.get("digest"):
            raise FactoryError("phase evidence artifact binding changed", "stale_phase_evidence", 409)
        if target_digest != digest(target):
            raise FactoryError("phase evidence target binding changed", "stale_phase_evidence", 409)
        runtime_job = con.execute("SELECT snapshot,attempt FROM job WHERE id=?", (report.get("job_id"),)).fetchone()
        if not runtime_job:
            raise FactoryError("runtime job is unavailable", "not_found", 404)
        runtime_input = json.loads(runtime_job["snapshot"])
        if target != runtime_input.get("target_binding"):
            raise FactoryError("phase evidence differs from the pinned runtime input", "stale_phase_evidence", 409)
        bundle = controlled_path(store, runtime_input["bundle_path"])
        from .blueprints import verify_frozen
        from .blueprint_runtime import validate_runner_manifest

        frozen_spec = verify_frozen(bundle, report["digest"])
        suite_inventory = tree_manifest(bundle / "source")
        current_suite = hashlib.sha256(json.dumps(suite_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if current_suite != target.get("suite_digest"):
            raise FactoryError("acceptance suite changed after runtime execution", "stale_phase_evidence", 409)
        current_runner = validate_runner_manifest(bundle / "source", frozen_spec, target.get("selected_phase"))
        if current_runner["selected_case_ids"] != target.get("selected_case_ids"):
            raise FactoryError("selected acceptance cases changed after runtime execution", "stale_phase_evidence", 409)
        scenario = frozen_spec.get("scenario", {})
        if (scenario.get("id") != target.get("scenario_id")
                or scenario.get("revision") != target.get("scenario_revision")):
            raise FactoryError("scenario basis changed after runtime execution", "stale_phase_evidence", 409)
        case_basis = frozen_spec.get("case_basis")
        if (case_basis.get("basis_digest") if isinstance(case_basis, dict) else None) != target.get("case_basis_digest"):
            raise FactoryError("case basis changed after runtime execution", "stale_phase_evidence", 409)
        submission = controlled_path(store, runtime_input["submission_path"])
        receipt = json.loads((submission.parent / "delivery-receipt.json").read_text())
        archive = submission.parent / "application.zip"
        if receipt != runtime_input.get("delivery") or hashlib.sha256(archive.read_bytes()).hexdigest() != runtime_input.get("archive_sha256"):
            raise FactoryError("runtime submission receipt changed after execution", "stale_phase_evidence", 409)
        app = controlled_path(store, str((submission / receipt["app_root"]).relative_to(store.root)))
        app_inventory = tree_manifest(app)
        current_application = hashlib.sha256(json.dumps(app_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if current_application != target.get("application_digest"):
            raise FactoryError("runtime application target changed after execution", "stale_phase_evidence", 409)
        requirement = next((item for item in report.get("required_evidence", [])
                            if item.get("id") == requirement_id), None)
        if not requirement:
            raise FactoryError("phase evidence requirement is not required for this run", "invalid_phase_evidence", 409)
        if executor.get("kind") != "independent_executor" or executor.get("name") != requirement["executor"]:
            raise FactoryError("phase evidence executor does not match the frozen requirement", "invalid_phase_evidence", 409)
        if not isinstance(executor.get("version"), str) or not executor["version"].strip():
            raise FactoryError("independent executor version is required", "invalid_phase_evidence", 409)

        allowed_prefix = f"jobs/{report['job_id']}/attempt-{runtime_job['attempt']}/runtime-evidence/external/"
        if not evidence_path.startswith(allowed_prefix):
            raise FactoryError("phase evidence must be produced in the host-run evidence directory", "invalid_phase_evidence", 409)
        evidence_file = controlled_path(store, evidence_path)
        raw = evidence_file.read_bytes()
        actual_sha = hashlib.sha256(raw).hexdigest()
        if actual_sha != expected_sha:
            raise FactoryError("phase evidence file digest mismatch", "evidence_digest_mismatch", 409)
        try:
            proof = json.loads(raw)
        except (UnicodeError, ValueError) as error:
            raise FactoryError("phase evidence file is not valid JSON", "invalid_phase_evidence", 409) from error
        if (not isinstance(proof, dict) or proof.get("schema") != "atlas.phase-evidence.v1"
                or proof.get("requirement_id") != requirement_id
                or proof.get("target_digest") != target_digest or proof.get("outcome") != "passed"
                or proof.get("executor") != executor):
            raise FactoryError("phase evidence report does not prove the bound requirement", "invalid_phase_evidence", 409)

        registered = report.setdefault("registered_phase_evidence", {})
        prior = registered.get(requirement_id)
        if prior:
            if prior.get("sha256") == actual_sha:
                return report
            raise FactoryError("phase evidence requirement already has a different result", "conflict", 409)
        registered[requirement_id] = {
            "sha256": actual_sha, "evidence_path": evidence_path,
            "target_digest": target_digest, "executor": executor,
        }
        missing = [item["id"] for item in report.get("required_evidence", []) if item["id"] not in registered]
        report["external_evidence"] = [
            {"id": item["id"], "status": "missing" if item["id"] in missing else "registered",
             **({"sha256": registered[item["id"]]["sha256"], "executor": registered[item["id"]]["executor"]}
                if item["id"] in registered else {})}
            for item in report.get("required_evidence", [])
        ]
        report["missing_evidence"] = missing
        report["phase_status"] = "unverified" if missing else "passed"
        report["passed"] = not missing
        report["outcome"] = "unavailable" if missing else "passed"
        if missing:
            report.update(code="phase_evidence_missing", error="required independent phase evidence is missing")
        else:
            report.pop("code", None)
            report.pop("error", None)
        con.execute("UPDATE acceptance SET body=? WHERE id=?", (canonical(report), run_id))
        if not missing:
            con.execute("UPDATE job SET state='completed',error=NULL,updated_at=? WHERE id=? AND state='needs_review'",
                        (now(), report["job_id"]))
            con.execute("INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                        (report["job_id"], runtime_job["attempt"], now(), "phase-evidence", "all required independent evidence registered"))
        return report


def run_runtime(pipeline, job, attempt, stage, cancelled):
    from .api import controlled_path
    from .blueprint_runtime import BlueprintRuntimeVerifier

    store, snapshot = pipeline.store, job["snapshot"]
    timeout = snapshot["config"]["timeout"]
    execution_deadline = None
    v1 = snapshot.get("v1")
    if v1:
        from .budget import BudgetLedger
        ledger = BudgetLedger(store, campaign_id=v1["campaign_id"])
        budget = ledger.snapshot()
        if budget["paused"]:
            raise FactoryError("campaign budget is paused", "budget_paused", 409)
        remaining = ledger.phase_remaining(v1["product_id"], v1["segment"], plan_id=v1.get("plan_id"))
        if remaining is not None:
            if remaining <= 0:
                raise FactoryError("runtime segment deadline exhausted", "budget_deadline", 409)
            timeout = min(timeout, remaining)
            execution_deadline = time.monotonic() + remaining

    def execution_cancelled():
        return cancelled() or (execution_deadline is not None and time.monotonic() >= execution_deadline)
    fields = ("schema", "artifact_id", "artifact_digest", "bundle_path", "selected_phase",
              "submission_path", "archive_sha256", "delivery", "suite_digest",
              "selected_case_ids", "phase_requirements", "target_binding", "case_basis")
    pinned = {key: snapshot[key] for key in fields}
    if digest(pinned) != snapshot["input_digest"]:
        raise FactoryError("runtime input changed", "checkpoint_changed", 409)
    bundle = controlled_path(store, snapshot["bundle_path"])
    spec = verify_frozen(bundle, snapshot["artifact_digest"])
    suite_inventory = tree_manifest(bundle / "source")
    suite_digest = hashlib.sha256(json.dumps(suite_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if suite_digest != snapshot["suite_digest"]:
        raise FactoryError("frozen acceptance suite changed", "checkpoint_changed", 409)
    submission = controlled_path(store, snapshot["submission_path"])
    # The ZIP, receipt, source and binding all remain pinned across retries.
    if hashlib.sha256((submission.parent / "application.zip").read_bytes()).hexdigest() != snapshot["archive_sha256"]:
        raise FactoryError("application archive changed", "application_changed", 409)
    receipt = json.loads((submission.parent / "delivery-receipt.json").read_text())
    if receipt != snapshot["delivery"]:
        raise FactoryError("delivery receipt changed", "application_changed", 409)
    root_name = receipt["app_root"]
    if root_name not in (".", "app"):
        raise FactoryError("invalid pinned application root")
    app = controlled_path(store, str((submission / root_name).relative_to(store.root)))
    if tree_manifest(app) != receipt["files"]:
        raise FactoryError("application source changed", "application_changed", 409)
    application_digest = hashlib.sha256(json.dumps(receipt["files"], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if application_digest != snapshot["target_binding"]["application_digest"]:
        raise FactoryError("runtime target changed", "application_changed", 409)
    atomic_json(attempt / "runtime-input.json", {**pinned, "input_digest": snapshot["input_digest"]})
    verifier = getattr(pipeline, "blueprint_verifier", None) or BlueprintRuntimeVerifier(
        owner=hashlib.sha256(str(store.root).encode()).hexdigest()[:16],
        timeout=timeout,
    )
    stage("startup", "Independent isolated application startup and frozen suite execution")
    try:
        report = verifier.verify(
            app, bundle / "source", spec, snapshot["selected_phase"], attempt / "runtime-evidence",
            receipt["runtime"], execution_cancelled, lambda message: stage("verify", message),
        )
    except FactoryError as error:
        if execution_deadline is not None and time.monotonic() >= execution_deadline:
            raise FactoryError("runtime segment deadline exhausted", "budget_deadline", 409) from error
        if cancelled() or error.code in {"cancelled", "lease_lost"}:
            raise
        # The verifier writes partial startup/case/cleanup evidence even when
        # infrastructure fails. Persist that attempt as unavailable rather than
        # leaving an older successful acceptance as the apparent latest result.
        partial = attempt / "runtime-evidence" / "report.json"
        report = json.loads(partial.read_text()) if partial.is_file() else {
            "startup": {"status": "not_run"}, "case_results": [],
            "cleanup": {"status": "not_run"},
        }
        report.update(outcome="unavailable", passed=False, error=str(error), code=error.code)
    if execution_deadline is not None and time.monotonic() >= execution_deadline:
        raise FactoryError("runtime segment deadline exhausted", "budget_deadline", 409)
    if cancelled():
        raise FactoryError("runtime job ownership lost", "lease_lost", 409)
    if tree_manifest(app) != receipt["files"]:
        raise FactoryError("application source changed during acceptance", "application_changed", 409)
    report = {
        **report, "selected_phase": snapshot["selected_phase"],
        "application_digest": snapshot["target_binding"]["application_digest"],
        "application_files": receipt["files"],
        "input_digest": snapshot["input_digest"], "delivery_normalizations": receipt["normalizations"],
        "target_binding": snapshot["target_binding"],
        "target_kind": "generated_application",
        "required_evidence": snapshot["phase_requirements"],
        "scope": "Independent managed-container startup and frozen phase-suite execution against this pinned application; no model call, publication or generic security certification.",
    }
    report.setdefault("suite_status", "passed" if report.get("outcome") == "passed" else "unverified")
    report["binding"] = {**report.get("binding", {}), "target": snapshot["target_binding"]}
    if report.get("suite_status") == "passed" and snapshot["phase_requirements"]:
        registered = report.get("registered_phase_evidence", {})
        missing = [item["id"] for item in snapshot["phase_requirements"] if item["id"] not in registered]
        report["external_evidence"] = [
            {"id": item["id"], "status": "registered" if item["id"] in registered else "missing",
             **({"sha256": registered[item["id"]]["sha256"], "executor": registered[item["id"]]["executor"]}
                if item["id"] in registered else {})}
            for item in snapshot["phase_requirements"]
        ]
        report["phase_status"] = "unverified" if missing else "passed"
        if missing:
            report.update(passed=False, outcome="unavailable", code="phase_evidence_missing",
                          error="required independent phase evidence is missing", missing_evidence=missing)
    elif report.get("suite_status") == "passed":
        report["phase_status"] = "passed"
    elif report.get("phase_status") not in {"blocked", "unverified"}:
        report["phase_status"] = "blocked" if report.get("outcome") == "blocked" else "unverified"
    evidence_report = attempt / "runtime-evidence" / "report.json"
    if evidence_report.parent.is_dir():
        atomic_json(evidence_report, report)
    atomic_json(attempt / "acceptance-report.json", report)
    store.complete_acceptance(job["id"], job["token"], report)
