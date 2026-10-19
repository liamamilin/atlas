"""Pinned P0 application development submissions and delivery validation."""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import tempfile
import time
import zipfile
from pathlib import Path

from atlas_runtime import atomic_json

from .artifacts import relative, tree_manifest
from .blueprints import unpack_archive
from .delivery import prepare_application
from .store import FactoryError, canonical, digest, integer, now, text, uid


MAX_OUTPUT_BYTES = 8 * 1024 * 1024
MAX_DELIVERY_ARCHIVE_BYTES = 1024 * 1024
MAX_OUTPUT_FILES = 300
MAX_PROTOCOL_REPAIRS = 2

DEVELOPMENT_PROMPT = """Implement the selected P0 application from the immutable development handoff in source/.
Read source/AGENT.md, source/HANDOFF.md, source/CURRENT_PHASE.json, source/ACCEPTANCE_CONTRACT.json and the referenced blueprint files before coding. Preserve the frozen acceptance contract and all source/blueprint files. Create only application source files in your response; do not return an archive, diff, test result, review status or claim of execution.
Return exactly {\"files\": {\"relative/path\": \"complete UTF-8 file content\", \"delivery.json\": \"JSON text\"}}. delivery.json must follow source/APP_DELIVERY.md, use the standard atlas.application-delivery.v1 schema, declare every application file exactly, and select a valid runtime profile. No code execution or network is available in this task. Do not fabricate runtime evidence or alter any frozen test, contract or template file."""


REPAIR_PROMPT = """Repair only the application delivery protocol using source/PRIOR_DELIVERY.json and source/VALIDATION_ERROR.json. Preserve all frozen files and acceptance commitments. Return exactly {\"files\": {\"relative/path\": \"complete UTF-8 file content\", \"delivery.json\": \"JSON text\"}}. Do not return a test result or claim acceptance. Do not execute code, install dependencies or access the network."""

APPLICATION_REPAIR_PROMPT = """Repair the P0 application against the actual pinned failure report. Read source/blueprint and the immutable source/FAILURE_REPORT.json and source/previous-application/ files. Keep every frozen template, scenario, case basis and acceptance file unchanged. Correct the application behavior addressed by the reported failed P0 check; preserve unrelated working behavior. Return complete UTF-8 source files in exactly {\"files\": {\"relative/path\": \"complete text\", \"delivery.json\": \"JSON text\"}}. Do not return or claim a test result, review status, runtime pass or acceptance. Do not execute code, install dependencies or access the network."""


def _project_name(artifact, value):
    raw = value.get("project_name")
    if raw is None:
        scenario = artifact.get("provenance", {}).get("scenario", {})
        raw = scenario.get(
            "name", artifact.get("manifest", {}).get("name", "atlas-app")
        )
        raw = re.sub(r"[^a-z0-9]+", "-", str(raw).lower()).strip("-")[:63]
        raw = raw or "atlas-app"
    if not isinstance(raw, str) or not re.fullmatch(r"[a-z][a-z0-9-]{0,62}", raw):
        raise FactoryError(
            "project_name must be a lowercase name using letters, digits and hyphens"
        )
    return raw


def _case_basis(store, artifact):
    from .cases import CaseLibrary

    basis = artifact.get("provenance", {}).get("case_basis")
    if basis is None:
        origin = store.job(artifact["job_id"])
        basis = origin["snapshot"].get("case_basis")
    if not isinstance(basis, dict):
        raise FactoryError(
            "V1 development requires fixed case evidence", "case_evidence_required", 409
        )
    library = CaseLibrary(store, initialize=False)
    library.validate_basis(basis)
    library.require_admissible(basis)
    return basis


def _scenario_binding(store, artifact):
    scenario = artifact.get("provenance", {}).get("scenario")
    if (
        not isinstance(scenario, dict)
        or not scenario.get("id")
        or not isinstance(scenario.get("revision"), int)
    ):
        raise FactoryError(
            "development requires a pinned scenario revision",
            "scenario_basis_required",
            409,
        )
    with store.connect() as con:
        row = con.execute(
            "SELECT body FROM scenario_history WHERE id=? AND revision=?",
            (scenario["id"], scenario["revision"]),
        ).fetchone()
    if not row:
        raise FactoryError(
            "artifact scenario revision is unavailable",
            "scenario_revision_conflict",
            409,
        )
    saved = json.loads(row["body"])
    if (
        scenario.get("name") != saved.get("name")
        or scenario.get("workflow") != saved.get("workflow")
        or scenario.get("acceptance") != saved.get("acceptance")
    ):
        raise FactoryError(
            "artifact scenario binding does not match its saved revision",
            "scenario_revision_conflict",
            409,
        )
    return saved


def _ensure_schema(store):
    with store.connect(True) as con:
        con.execute("""CREATE TABLE IF NOT EXISTS tf_development_request (
            request_key TEXT PRIMARY KEY, request_digest TEXT NOT NULL,
            batch_id TEXT NOT NULL UNIQUE, job_id TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL)""")
        con.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS tf_development_request_digest ON tf_development_request(request_digest)"
        )


def _prior_request(con, request_key, request_digest):
    by_key = con.execute(
        "SELECT request_digest,batch_id FROM tf_development_request WHERE request_key=?",
        (request_key,),
    ).fetchone()
    if by_key:
        if by_key["request_digest"] != request_digest:
            raise FactoryError(
                "request key belongs to a different development request",
                "conflict",
                409,
            )
        return by_key["batch_id"]
    by_request = con.execute(
        "SELECT batch_id FROM tf_development_request WHERE request_digest=?",
        (request_digest,),
    ).fetchone()
    return by_request["batch_id"] if by_request else None


def _repair_input(store, con, artifact, repair_of):
    """Return source and failure only for a real, host-pinned failed P0 run."""
    from .api import controlled_path

    row = con.execute(
        "SELECT digest,body FROM acceptance WHERE id=? AND artifact_id=?",
        (repair_of, artifact["id"]),
    ).fetchone()
    report = json.loads(row["body"]) if row else {}
    target = report.get("target_binding", {})
    runtime_job = (
        con.execute(
            "SELECT kind,state,snapshot FROM job WHERE id=?", (report.get("job_id"),)
        ).fetchone()
        if row
        else None
    )
    runtime_input = json.loads(runtime_job["snapshot"]) if runtime_job else {}
    case_failure = any(
        isinstance(result, dict) and result.get("status") == "failed"
        for result in report.get("case_results", [])
    )
    startup = report.get("startup") if isinstance(report.get("startup"), dict) else {}
    startup_failure = (
        report.get("outcome") == "blocked"
        and startup.get("status") == "blocked"
        and bool(report.get("failure"))
    )
    excluded = {
        "runtime_unavailable",
        "verification_timeout",
        "cancelled",
        "phase_evidence_missing",
        "application_changed",
        "runtime_job_failed",
    }
    if (
        not row
        or row["digest"] != artifact["digest"]
        or report.get("method") != "blueprint-runtime"
        or report.get("outcome") != "blocked"
        or report.get("code") in excluded
        or not (case_failure or startup_failure)
        or not runtime_job
        or runtime_job["kind"] != "blueprint-runtime"
        or runtime_job["state"] != "needs_review"
        or target.get("target_kind") != "generated_application"
        or target.get("artifact_id") != artifact["id"]
        or target.get("artifact_digest") != artifact["digest"]
        or target.get("selected_phase") != "P0"
        or runtime_input.get("artifact_id") != artifact["id"]
        or runtime_input.get("artifact_digest") != artifact["digest"]
        or runtime_input.get("selected_phase") != "P0"
        or runtime_input.get("target_binding") != target
    ):
        raise FactoryError(
            "repair requires actual failed P0 application feedback for this exact artifact",
            "repair_target_invalid",
            409,
        )
    receipt = runtime_input.get("delivery")
    if not isinstance(receipt, dict):
        raise FactoryError(
            "failed P0 run has no host delivery receipt", "repair_target_invalid", 409
        )
    application_path = controlled_path(store, runtime_input.get("submission_path"))
    app_root = (
        application_path / receipt["app_root"]
        if receipt["app_root"] != "."
        else application_path
    )
    if tree_manifest(app_root) != receipt.get("files"):
        raise FactoryError(
            "failed application source changed after its acceptance run",
            "repair_target_invalid",
            409,
        )
    provenance = artifact.get("provenance", {})
    scenario = provenance.get("scenario", {})
    case_basis = provenance.get("case_basis", {})
    if (
        target.get("application_digest") != hashlib.sha256(json.dumps(receipt["files"], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        or target.get("scenario_id") != scenario.get("id")
        or target.get("scenario_revision") != scenario.get("revision")
        or target.get("case_basis_digest") != case_basis.get("basis_digest")
    ):
        raise FactoryError(
            "failed P0 run is bound to a different application target",
            "repair_target_invalid",
            409,
        )
    archive = controlled_path(
        store,
        str((application_path.parent / "application.zip").relative_to(store.root)),
    )
    raw = archive.read_bytes()
    archive_sha = hashlib.sha256(raw).hexdigest()
    if archive_sha != runtime_input.get("archive_sha256"):
        raise FactoryError(
            "failed application archive changed after its acceptance run",
            "repair_target_invalid",
            409,
        )
    receipt_path = controlled_path(
        store,
        str(
            (application_path.parent / "delivery-receipt.json").relative_to(store.root)
        ),
    )
    if not receipt_path.is_file() or json.loads(receipt_path.read_text()) != receipt:
        raise FactoryError(
            "failed application receipt changed after its acceptance run",
            "repair_target_invalid",
            409,
        )
    from .delivery import prepare_application

    with tempfile.TemporaryDirectory(dir=store.root) as tempdir:
        checked = prepare_application(raw, Path(tempdir) / "checked")
    if checked != receipt:
        raise FactoryError(
            "failed application receipt does not match its source archive",
            "repair_target_invalid",
            409,
        )
    return {
        "archive": raw,
        "archive_sha256": archive_sha,
        "failure_report": report,
        "failure_report_digest": digest(report),
    }


def _host_counted_template_revision(con, artifact, v1):
    """Whether this artifact is a host-recorded revision of an initial template.

    The artifact's model-authored ``supersedes`` field is insufficient on its
    own. The corresponding production job must contain the matching
    ``cognitive_repair`` receipt, inherit the same V1 product identity, and the
    formal revision's business repair must already be in the campaign ledger.
    The predecessor must itself have an initial P0 development job.
    """
    parent_id = artifact.get("supersedes")
    if not isinstance(parent_id, str) or not parent_id:
        return False
    current = con.execute(
        "SELECT job_id,body FROM artifact WHERE id=? AND digest=?",
        (artifact.get("id"), artifact.get("digest")),
    ).fetchone()
    parent = con.execute(
        "SELECT digest,job_id,body FROM artifact WHERE id=?",
        (parent_id,),
    ).fetchone()
    if not current or not parent:
        return False
    body = json.loads(current["body"])
    parent_body = json.loads(parent["body"])
    if body.get("supersedes") != parent_id:
        return False
    revision_job = con.execute(
        "SELECT kind,snapshot FROM job WHERE id=?", (current["job_id"],)
    ).fetchone()
    parent_job = con.execute(
        "SELECT snapshot FROM job WHERE id=?", (parent["job_id"],)
    ).fetchone()
    if (
        not revision_job
        or revision_job["kind"] != "blueprint-production"
        or not parent_job
    ):
        return False
    revision_snapshot = json.loads(revision_job["snapshot"])
    parent_snapshot = json.loads(parent_job["snapshot"])
    repair = revision_snapshot.get("cognitive_repair")
    if (
        not isinstance(repair, dict)
        or repair.get("id") != parent_id
        or repair.get("digest") != parent["digest"]
        or revision_snapshot.get("v1") != v1
        or parent_snapshot.get("v1") != v1
        or body.get("provenance", {}).get("v1") != v1
        or parent_body.get("provenance", {}).get("v1") != v1
    ):
        return False
    prior_initial = con.execute(
        "SELECT 1 FROM job WHERE kind='application-development' "
        "AND json_extract(snapshot,'$.phase')='P0' "
        "AND json_extract(snapshot,'$.repair_of') IS NULL "
        "AND json_extract(snapshot,'$.artifact_id')=? "
        "AND json_extract(snapshot,'$.artifact_digest')=? "
        "AND json_extract(snapshot,'$.v1.campaign_id')=? "
        "AND json_extract(snapshot,'$.v1.product_id')=? LIMIT 1",
        (parent_id, parent["digest"], v1["campaign_id"], v1["product_id"]),
    ).fetchone()
    if not prior_initial:
        return False
    counted = con.execute(
        "SELECT 1 FROM tf_budget_repair WHERE campaign_id=? AND product_id=? "
        "AND operation_key LIKE ? LIMIT 1",
        (
            v1["campaign_id"],
            v1["product_id"],
            "template-revision:" + parent["digest"] + ":%",
        ),
    ).fetchone()
    return counted is not None


def queue_development(store, artifact, value):
    """Queue one immutable P0 development package; repeated keys are idempotent."""
    if not isinstance(value, dict):
        raise FactoryError("development request must be an object")
    _ensure_schema(store)
    if artifact.get("artifact_type") != "product-blueprint":
        raise FactoryError(
            "development requires a cognitive template", "wrong_artifact_type", 409
        )
    if value.get("expected_digest") != artifact.get("digest"):
        raise FactoryError("artifact version changed", "revision_conflict", 409)
    if artifact.get("review_status") != "passed":
        raise FactoryError(
            "latest independent review of this exact digest must pass",
            "cognitive_review_required",
            409,
        )
    if value.get("phase") != "P0":
        raise FactoryError(
            "V1 development currently supports P0 only", "phase_unsupported", 409
        )
    request_key = text(value.get("request_key"), "request_key", 200)
    model = text(
        value.get(
            "model",
            artifact.get("provenance", {}).get(
                "model", "opencode-go/deepseek-v4.1-flash"
            ),
        ),
        "provider/model",
        200,
    )
    if (
        not re.fullmatch(r"[a-zA-Z0-9._:/#-]+", model)
        or "/" not in model
        or model.startswith("-")
    ):
        raise FactoryError("model must use provider/model format")
    timeout = integer(value.get("timeout", 900), "timeout", 30, 900)
    project_name = _project_name(artifact, value)
    case_basis = _case_basis(store, artifact)
    scenario = _scenario_binding(store, artifact)
    origin = store.job(artifact["job_id"])
    v1 = origin["snapshot"].get("v1")
    if not isinstance(v1, dict) or not {"campaign_id", "product_id", "segment"} <= set(
        v1
    ):
        raise FactoryError(
            "artifact is missing its V1 campaign identity", "v1_identity_required", 409
        )
    repair_of = value.get("repair_of")
    request_body = {
        "artifact_id": artifact["id"],
        "artifact_digest": artifact["digest"],
        "phase": "P0",
        "project_name": project_name,
        "model": model,
        "timeout": timeout,
        "repair_of": repair_of,
    }
    request_digest = digest(request_body)
    config = {
        "kind": "application-development",
        "name": "P0 development: " + project_name,
        "model": model,
        "concurrency": 1,
        "timeout": timeout,
        "language": origin["snapshot"].get("config", {}).get("language", "en"),
    }
    from .budget import BudgetLedger

    ledger = BudgetLedger(store, campaign_id=v1["campaign_id"])
    repair_input = None
    with store.connect() as con:
        prior_batch = _prior_request(con, request_key, request_digest)
        if prior_batch:
            return store.batch(prior_batch)
        if repair_of is not None:
            repair_input = _repair_input(store, con, artifact, repair_of)
    # Export by the same public route and exporter used for user downloads.
    # Perform it before BEGIN IMMEDIATE to avoid nested database connections.
    from .api import dispatch

    export, _ = dispatch(
        "POST",
        f"/api/factory/artifacts/{artifact['id']}/development-package",
        body={
            "expected_digest": artifact["digest"],
            "project_name": project_name,
            "phase": "P0",
        },
        store=store,
    )
    archive, _, _ = dispatch("GET", export["download_url"], store=store)
    raw_archive = archive.read_bytes()
    try:
        archive.unlink()
    except OSError:
        pass
    archive_sha = hashlib.sha256(raw_archive).hexdigest()
    submission = (
        store.root
        / "development-submissions"
        / (hashlib.sha256(request_key.encode()).hexdigest() + "-" + uid("sub"))
    )
    submission.parent.mkdir(parents=True, exist_ok=True)
    submission.mkdir(parents=False, exist_ok=False)
    (submission / "handoff.zip").write_bytes(raw_archive)
    if repair_input is not None:
        (submission / "previous-application.zip").write_bytes(repair_input["archive"])
        atomic_json(submission / "failure-report.json", repair_input["failure_report"])
    pinned = {
        "schema": "atlas.development-input.v1",
        "artifact_id": artifact["id"],
        "artifact_digest": artifact["digest"],
        "phase": "P0",
        "project_name": project_name,
        "handoff_archive": str((submission / "handoff.zip").relative_to(store.root)),
        "handoff_sha256": archive_sha,
        "case_basis": case_basis,
        "scenario": scenario,
        "repair_of": repair_of,
        **(
            {
                "previous_application_archive": str(
                    (submission / "previous-application.zip").relative_to(store.root)
                ),
                "previous_application_sha256": repair_input["archive_sha256"],
                "failure_report": repair_input["failure_report"],
                "failure_report_digest": repair_input["failure_report_digest"],
            }
            if repair_input
            else {}
        ),
    }
    snapshot = {
        **pinned,
        "input_digest": digest(pinned),
        "leaf": origin["snapshot"]["leaf"],
        "v1": v1,
        "config": config,
    }
    batch_id, job_id, at = uid("bat"), uid("job"), now()
    prior_batch = None
    try:
        with store.connect(True) as con:
            prior_batch = _prior_request(con, request_key, request_digest)
            if not prior_batch:
                current = con.execute(
                    "SELECT digest FROM artifact WHERE id=?", (artifact["id"],)
                ).fetchone()
                if not current or current["digest"] != artifact["digest"]:
                    raise FactoryError(
                        "artifact version changed", "revision_conflict", 409
                    )
                from .v1_catalog import review_status

                if review_status(con, artifact["id"], artifact["digest"]) != "passed":
                    raise FactoryError(
                        "latest independent review of this exact digest must pass",
                        "cognitive_review_required",
                        409,
                    )
                plan_id = v1.get("plan_id")
                plan_state = "running"
                if plan_id:
                    parent = con.execute(
                        "SELECT b.state,p.body FROM v1_execution e JOIN batch b ON b.id=e.batch_id "
                        "JOIN v1_plan p ON p.id=e.plan_id WHERE e.plan_id=?",
                        (plan_id,),
                    ).fetchone()
                    if not parent:
                        raise FactoryError(
                            "V1 parent plan execution is unavailable",
                            "v1_plan_missing",
                            409,
                        )
                    plan_body = json.loads(parent["body"])
                    if plan_body.get("campaign_id") != v1["campaign_id"]:
                        raise FactoryError(
                            "artifact campaign identity does not match its V1 plan",
                            "v1_identity_conflict",
                            409,
                        )
                    if parent["state"] == "cancelled":
                        raise FactoryError(
                            "V1 parent execution is cancelled",
                            "v1_parent_cancelled",
                            409,
                        )
                    plan_state = "paused" if parent["state"] == "paused" else "running"
                # Allow a new initial only when this is the host-recorded
                # descendant of the artifact whose initial P0 already ran,
                # and its formal template repair is already charged.
                if repair_of is None:
                    exact_initial = con.execute(
                        "SELECT id FROM job WHERE kind='application-development' "
                        "AND json_extract(snapshot,'$.phase')='P0' "
                        "AND json_extract(snapshot,'$.repair_of') IS NULL "
                        "AND json_extract(snapshot,'$.artifact_id')=? "
                        "AND json_extract(snapshot,'$.artifact_digest')=? LIMIT 1",
                        (artifact["id"], artifact["digest"]),
                    ).fetchone()
                    initial = con.execute(
                        "SELECT id FROM job WHERE kind='application-development' "
                        "AND json_extract(snapshot,'$.phase')='P0' "
                        "AND json_extract(snapshot,'$.repair_of') IS NULL "
                        "AND json_extract(snapshot,'$.v1.campaign_id')=? "
                        "AND json_extract(snapshot,'$.v1.product_id')=? LIMIT 1",
                        (v1["campaign_id"], v1["product_id"]),
                    ).fetchone()
                    if exact_initial or (initial and not _host_counted_template_revision(
                        con, artifact, v1
                    )):
                        raise FactoryError(
                            "P0 development already exists for this V1 product; use actual failed application feedback for repair",
                            "development_initial_exists",
                            409,
                        )
                if repair_of is not None:
                    latest_repair_input = _repair_input(store, con, artifact, repair_of)
                    if (
                        latest_repair_input["archive_sha256"]
                        != repair_input["archive_sha256"]
                    ):
                        raise FactoryError(
                            "failed P0 source changed while repair was queued",
                            "repair_target_invalid",
                            409,
                        )
                    ledger.record_repair(
                        v1["product_id"],
                        "application-development:" + request_digest,
                        con=con,
                    )
                con.execute(
                    "INSERT INTO batch VALUES(?,?,?,?)",
                    (batch_id, plan_state, canonical(config), at),
                )
                con.execute(
                    "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        job_id,
                        batch_id,
                        "application-development",
                        "queued",
                        "development-queued",
                        1,
                        None,
                        None,
                        canonical(snapshot),
                        None,
                        at,
                        at,
                    ),
                )
                con.execute(
                    "INSERT INTO tf_development_request VALUES(?,?,?,?,?)",
                    (request_key, request_digest, batch_id, job_id, at),
                )
    except BaseException:
        shutil.rmtree(submission, ignore_errors=True)
        raise
    if prior_batch:
        shutil.rmtree(submission, ignore_errors=True)
        return store.batch(prior_batch)
    return store.batch(batch_id)


def _response_archive(response):
    if not isinstance(response, dict) or not isinstance(response.get("files"), dict):
        raise FactoryError(
            "model response must contain a files object", "delivery_protocol", 409
        )
    files = response["files"]
    if not files or len(files) > MAX_OUTPUT_FILES:
        raise FactoryError(
            "application must contain 1 to 300 source files", "delivery_protocol", 409
        )
    if any(not isinstance(name, str) for name in files):
        raise FactoryError(
            "application file paths must be strings", "delivery_protocol", 409
        )
    total = 0
    out = io.BytesIO()
    seen = set()
    try:
        with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for raw_path, content in sorted(files.items()):
                path = relative(raw_path)
                if path in seen:
                    raise FactoryError(
                        "duplicate application file path", "delivery_protocol", 409
                    )
                seen.add(path)
                if not isinstance(content, str):
                    raise FactoryError(
                        "application files must be UTF-8 text", "delivery_protocol", 409
                    )
                encoded = content.encode("utf-8")
                total += len(encoded)
                if total > MAX_OUTPUT_BYTES:
                    raise FactoryError(
                        "application output exceeds the 8 MiB limit",
                        "delivery_protocol",
                        409,
                    )
                info = zipfile.ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o600 << 16
                archive.writestr(info, encoded)
    except (UnicodeError, OSError) as error:
        raise FactoryError(
            "application files must be valid UTF-8 text", "delivery_protocol", 409
        ) from error
    return out.getvalue()


def _finish(store, job, report):
    from privacy import redact_text

    at = now()
    with store.connect(True) as con:
        row = con.execute(
            "SELECT * FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
            (job["id"], job["token"], time.time()),
        ).fetchone()
        if not row:
            raise FactoryError("development job ownership lost", "lease_lost", 409)
        con.execute(
            "INSERT OR IGNORE INTO checkpoint VALUES(?,?,?)",
            (
                job["id"],
                "application-delivery",
                canonical({"result": report, "digest": digest(report)}),
            ),
        )
        con.execute(
            "UPDATE job SET state='completed',stage='application-delivered',error=NULL,updated_at=? WHERE id=?",
            (at, job["id"]),
        )
        con.execute(
            "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
            (
                job["id"],
                row["attempt"],
                at,
                "application-delivered",
                redact_text(
                    "Validated P0 application delivery; no execution or acceptance claim."
                ),
            ),
        )


def run_development(pipeline, job, attempt, agent, stage, checkpoint):
    """Generate an application from the standard export and validate delivery, without execution."""
    store, snapshot = pipeline.store, job["snapshot"]
    pinned_fields = (
        "schema",
        "artifact_id",
        "artifact_digest",
        "phase",
        "project_name",
        "handoff_archive",
        "handoff_sha256",
        "case_basis",
        "scenario",
        "repair_of",
        "previous_application_archive",
        "previous_application_sha256",
        "failure_report",
        "failure_report_digest",
    )
    pinned = {key: snapshot[key] for key in pinned_fields if key in snapshot}
    if snapshot.get("input_digest") != digest(pinned) or snapshot.get("phase") != "P0":
        raise FactoryError(
            "development input snapshot changed", "checkpoint_changed", 409
        )
    # The persisted archive is authoritative; derive its parent from the checked relative path.
    from .api import controlled_path

    handoff = controlled_path(store, snapshot["handoff_archive"])
    submission = handoff.parent
    root = attempt / "p0-handoff"
    root.mkdir(parents=True, exist_ok=False)
    raw_handoff = handoff.read_bytes()
    if hashlib.sha256(raw_handoff).hexdigest() != snapshot["handoff_sha256"]:
        raise FactoryError(
            "development handoff changed after queueing", "artifact_changed", 409
        )
    unpack_archive(raw_handoff, root)
    artifact = next(
        (item for item in store.artifacts() if item["id"] == snapshot["artifact_id"]),
        None,
    )
    if not artifact or artifact["digest"] != snapshot["artifact_digest"]:
        raise FactoryError(
            "template changed after development was queued", "revision_conflict", 409
        )
    export_result = {
        "handoff_sha256": snapshot["handoff_sha256"],
        "files": sorted(
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file()
        ),
    }
    checkpoint("development-export", lambda: export_result)
    last_error = None
    response = None
    for index in range(MAX_PROTOCOL_REPAIRS + 1):
        business_repair = index == 0 and snapshot.get("repair_of") is not None
        name = (
            "p0-application-repair"
            if business_repair
            else "p0-application"
            if index == 0
            else f"p0-delivery-repair-{index}"
        )
        agent_source = root
        if business_repair:
            repair_source = attempt / "p0-application-repair-source"
            from .artifacts import copy_tree

            copy_tree(root, repair_source)
            prior_archive = controlled_path(
                store, snapshot["previous_application_archive"]
            )
            prior_bytes = prior_archive.read_bytes()
            if (
                hashlib.sha256(prior_bytes).hexdigest()
                != snapshot["previous_application_sha256"]
            ):
                raise FactoryError(
                    "previous application archive changed", "repair_target_invalid", 409
                )
            if digest(snapshot["failure_report"]) != snapshot["failure_report_digest"]:
                raise FactoryError(
                    "pinned failure report changed", "checkpoint_changed", 409
                )
            prepare_application(prior_bytes, repair_source / "previous-application")
            atomic_json(
                repair_source / "FAILURE_REPORT.json", snapshot["failure_report"]
            )
            payload = {
                "artifact_id": snapshot["artifact_id"],
                "template_digest": snapshot["artifact_digest"],
                "phase": "P0",
                "scenario": snapshot["scenario"],
                "case_basis": snapshot["case_basis"],
                "repair_of": snapshot["repair_of"],
                "previous_application_sha256": snapshot["previous_application_sha256"],
                "failure_report_digest": snapshot["failure_report_digest"],
            }
            prompt = APPLICATION_REPAIR_PROMPT
            agent_source = repair_source
        elif index:
            from .artifacts import copy_tree

            repair_source = attempt / f"p0-repair-source-{index}"
            copy_tree(root, repair_source)
            atomic_json(repair_source / "PRIOR_DELIVERY.json", response)
            atomic_json(
                repair_source / "VALIDATION_ERROR.json",
                {
                    "error": str(last_error),
                    "code": getattr(last_error, "code", "delivery_protocol"),
                },
            )
            payload = {
                "artifact_id": snapshot["artifact_id"],
                "template_digest": snapshot["artifact_digest"],
                "phase": "P0",
                "repair_attempt": index,
                "repair_input": "source/PRIOR_DELIVERY.json",
                "validation_error": "source/VALIDATION_ERROR.json",
            }
            prompt = REPAIR_PROMPT
            agent_source = repair_source
        else:
            payload = {
                "artifact_id": snapshot["artifact_id"],
                "template_digest": snapshot["artifact_digest"],
                "phase": "P0",
                "scenario": snapshot["scenario"],
                "case_basis": snapshot["case_basis"],
            }
            prompt = DEVELOPMENT_PROMPT
        response = checkpoint(
            "development-response-" + str(index),
            lambda name=name, prompt=prompt, payload=payload, source=agent_source if (index or business_repair) else root: (
                agent(name, prompt, payload, source,
                      budget_stage="p0-delivery:" + snapshot["input_digest"],
                      budget_scope="p0-delivery")
            ),
        )
        try:
            raw = _response_archive(response)
            if len(raw) > MAX_DELIVERY_ARCHIVE_BYTES:
                raise FactoryError(
                    "compressed application exceeds the 1 MiB delivery limit",
                    "delivery_protocol",
                    409,
                )
            (submission / "application.zip").write_bytes(raw)
            receipt = prepare_application(raw, attempt / f"delivery-validated-{index}")
            if receipt["runtime"]["profile"] != "python-web":
                raise FactoryError(
                    "V1 P0 application delivery requires the python-web profile",
                    "delivery_protocol",
                    409,
                )
            last_error = None
            break
        except FactoryError as error:
            last_error = error
            if index == MAX_PROTOCOL_REPAIRS:
                raise
    if last_error is not None:
        raise last_error
    archive_path = submission / "application.zip"
    archive_sha = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    report = {
        "artifact_id": snapshot["artifact_id"],
        "template_digest": snapshot["artifact_digest"],
        "phase": "P0",
        "handoff_sha256": snapshot["handoff_sha256"],
        "archive_path": str(archive_path.relative_to(store.root)),
        "archive_sha256": archive_sha,
        "delivery_receipt": receipt,
        "application_digest": hashlib.sha256(json.dumps(receipt["files"], sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "case_basis_digest": snapshot["case_basis"]["basis_digest"],
        "scenario": snapshot["scenario"],
        "runtime_status": "not_run",
        "acceptance_status": "not_run",
        "model_response_digest": digest(response),
        "repair_of": snapshot.get("repair_of"),
        "previous_application_sha256": snapshot.get("previous_application_sha256"),
        "failure_report_digest": snapshot.get("failure_report_digest"),
    }
    saved = checkpoint("application-delivery", lambda: report)
    _finish(store, job, saved)
    return saved
