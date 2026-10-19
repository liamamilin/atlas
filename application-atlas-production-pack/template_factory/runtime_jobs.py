"""Pinned application submissions and independent runtime jobs; no model calls."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

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
    from .blueprint_runtime import validate_runner_manifest

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
    validate_runner_manifest(bundle / "source", spec, phase)
    config = {
        "kind": "blueprint-runtime", "name": "Independent application acceptance: " + artifact["manifest"]["name"],
        "model": "", "concurrency": 1,
        "timeout": integer(value.get("timeout", 300), "timeout", 30, 7200),
        "language": value.get("language", "zh"),
    }
    if config["language"] not in ("zh", "en"):
        raise FactoryError("language must be zh or en")
    archive = decode_archive(value.get("source_archive_base64"))
    submission = store.root / "submissions" / uid("sub")
    submission.mkdir(parents=True)
    try:
        metadata = prepare_application(archive, submission / "application")
        archive_hash = hashlib.sha256(archive).hexdigest()
        (submission / "application.zip").write_bytes(archive)
        atomic_json(submission / "delivery-receipt.json", metadata)
        pinned = {
            "schema": "atlas.factory-runtime-input.v1",
            "artifact_id": artifact["id"], "artifact_digest": artifact["digest"],
            "bundle_path": artifact["bundle_path"], "selected_phase": phase,
            "submission_path": str((submission / "application").relative_to(store.root)),
            "archive_sha256": archive_hash, "delivery": metadata,
        }
        snapshot = {
            **pinned, "input_digest": digest(pinned),
            "leaf": store.job(artifact["job_id"])["snapshot"]["leaf"],
            "scenario": artifact["provenance"]["scenario"], "config": config,
            "execution_confirmed": True,
        }
        batch_id, job_id, at = uid("bat"), uid("job"), now()
        with store.connect(True) as con:
            if con.execute(
                "SELECT 1 FROM job WHERE kind='blueprint-runtime' AND state IN ('queued','running') "
                "AND json_extract(snapshot,'$.artifact_id')=?", (artifact["id"],)
            ).fetchone():
                raise FactoryError("application acceptance already queued or running", "conflict", 409)
            con.execute("INSERT INTO batch VALUES(?,?,?,?)", (batch_id, "running", canonical(config), at))
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                job_id, batch_id, "blueprint-runtime", "queued", "acceptance", 1, None, None,
                canonical(snapshot), None, at, at,
            ))
        return store.batch(batch_id)
    except BaseException:
        shutil.rmtree(submission, ignore_errors=True)
        raise


def run_runtime(pipeline, job, attempt, stage, cancelled):
    from .api import controlled_path
    from .blueprint_runtime import BlueprintRuntimeVerifier

    store, snapshot = pipeline.store, job["snapshot"]
    fields = ("schema", "artifact_id", "artifact_digest", "bundle_path", "selected_phase",
              "submission_path", "archive_sha256", "delivery")
    pinned = {key: snapshot[key] for key in fields}
    if digest(pinned) != snapshot["input_digest"]:
        raise FactoryError("runtime input changed", "checkpoint_changed", 409)
    bundle = controlled_path(store, snapshot["bundle_path"])
    spec = verify_frozen(bundle, snapshot["artifact_digest"])
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
    atomic_json(attempt / "runtime-input.json", {**pinned, "input_digest": snapshot["input_digest"]})
    verifier = getattr(pipeline, "blueprint_verifier", None) or BlueprintRuntimeVerifier(
        owner=hashlib.sha256(str(store.root).encode()).hexdigest()[:16],
        timeout=snapshot["config"]["timeout"],
    )
    stage("startup", "Independent isolated application startup and frozen suite execution")
    try:
        report = verifier.verify(
            app, bundle / "source", spec, snapshot["selected_phase"], attempt / "runtime-evidence",
            receipt["runtime"], cancelled, lambda message: stage("verify", message),
        )
    except FactoryError as error:
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
    if cancelled():
        raise FactoryError("runtime job ownership lost", "lease_lost", 409)
    if tree_manifest(app) != receipt["files"]:
        raise FactoryError("application source changed during acceptance", "application_changed", 409)
    report = {
        **report, "selected_phase": snapshot["selected_phase"],
        "application_digest": digest(receipt["files"]), "application_files": receipt["files"],
        "input_digest": snapshot["input_digest"], "delivery_normalizations": receipt["normalizations"],
        "scope": "Independent managed-container startup and frozen phase-suite execution against this pinned application; no model call, publication or generic security certification.",
    }
    atomic_json(attempt / "acceptance-report.json", report)
    store.complete_acceptance(job["id"], job["token"], report)
