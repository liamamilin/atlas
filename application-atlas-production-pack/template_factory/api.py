"""Small factory API surface sharing the local server's existing request guards."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from functools import lru_cache
from urllib.parse import parse_qs

from atlas_runtime import PACK
from .artifacts import archive_tree, render_template
from .blueprints import (
    DOCUMENTS,
    decode_archive,
    export_development,
    import_blueprint,
    is_blueprint,
    verify_frozen,
)
from .cli import CLI
from .runtime import DockerVerifier
from .store import FactoryError, FactoryStore, digest
from .worker import ensure_worker


@lru_cache(maxsize=8)
def _initialized_store(root, pack):
    return FactoryStore(root, pack)


def get_store():
    return _initialized_store(
        os.environ.get("ATLAS_FACTORY_ROOT", str(PACK / "atlas/template-factory")), str(PACK)
    )


def artifact(store, artifact_id):
    result = next((a for a in store.artifacts() if a["id"] == artifact_id), None)
    if not result:
        raise FactoryError("template not found", "not_found", 404)
    return result


def controlled_path(store, value):
    if (
        not isinstance(value, str)
        or ".." in Path(value).parts
        or Path(value).is_absolute()
    ):
        raise FactoryError("invalid internal artifact path")
    path = store.root / value
    if any(
        p.is_symlink() for p in (path, *list(path.parents)[: len(Path(value).parts)])
    ):
        raise FactoryError("internal artifact path is a symlink")
    resolved = path.resolve()
    if not resolved.is_relative_to(store.root) or not path.exists():
        raise FactoryError("artifact is unavailable", "not_found", 404)
    return path


def dispatch(method, path, query="", body=None, store=None):
    """Return (JSON object, status) or (Path, download name, content type)."""
    store = store or get_store()
    body = body or {}
    route = path.removeprefix("/api/factory").strip("/")
    if method == "GET" and route == "auxiliary-workflows":
        from .auxiliary_workflow import WorkflowService
        return WorkflowService(store).list_plans(), 200
    workflow_output = re.fullmatch(r"auxiliary-workflows/([A-Za-z0-9._-]+)/leaves/([A-Za-z0-9._-]+)/steps/([A-Za-z0-9._-]+)/([A-Za-z_]+)/outputs/(\d+)", route)
    if method == "GET" and workflow_output:
        from .auxiliary_workflow import WorkflowService
        return WorkflowService(store).output_file(*workflow_output.groups()[:4], int(workflow_output[5]))
    workflow_match = re.fullmatch(r"auxiliary-workflows/([A-Za-z0-9._-]+)", route)
    if method == "GET" and workflow_match:
        from .auxiliary_workflow import WorkflowService
        params = parse_qs(query)
        try:
            offset = int(params.get("offset", ["0"])[0])
            limit = int(params.get("limit", ["20"])[0])
        except ValueError as error:
            raise FactoryError("invalid workflow pagination") from error
        return WorkflowService(store).detail(workflow_match[1], offset, limit, params.get("state", [""])[0], params.get("q", [""])[0]), 200
    if method == "GET" and route == "assisted-templates":
        from .assisted_catalog import catalog
        return catalog(store, {k: v[0] for k, v in parse_qs(query).items()}), 200
    assisted_match = re.fullmatch(r"assisted-templates/(tpl_[a-f0-9]{32})/files/([a-z]+)", route)
    if method == "GET" and assisted_match:
        from .assisted_catalog import download
        return download(store, assisted_match[1], assisted_match[2])
    if route.startswith("v1/"):
        from .v1_api import dispatch_v1
        return dispatch_v1(method, route[3:], query, body, store)
    if method == "GET" and route == "status":
        return {
            "cli": CLI().info(models=True),
            "runtime": DockerVerifier().info(),
            "profiles": ["static-web", "python-web", "node-web", "cli"],
            "renderer": "atlas-declarative-v1",
            "parameter": "project_name",
            "note": "Scenario proposals and verification plans require review; L3 is never automatic.",
        }, 200
    if method == "GET" and route == "catalog":
        leaf = parse_qs(query).get("leaf", [None])[0]
        return store.scenarios(leaf), 200
    if method == "POST" and route == "scenarios":
        return store.save_scenario(body), 201
    match = re.fullmatch(r"scenarios/(scn_[a-f0-9]{32})", route)
    if method == "POST" and match:
        return store.save_scenario(body, match[1]), 200
    if method == "GET" and route == "batches":
        # Opening the factory also recovers queued work after API/worker restart.
        batches = store.batches()
        if any(j["state"] in {"queued", "running"} for b in batches for j in b["jobs"]):
            ensure_worker(store)
        return batches, 200
    if method == "POST" and route == "batches":
        result = store.create_batch(body)
        ensure_worker(store)
        return result, 202
    match = re.fullmatch(r"batches/(bat_[a-f0-9]{32})/(pause|resume|cancel)", route)
    if method == "POST" and match:
        result = store.batch_action(match[1], match[2])
        if match[2] == "resume":
            ensure_worker(store)
        return result, 200
    match = re.fullmatch(r"jobs/(job_[a-f0-9]{32})(/retry)?", route)
    if match:
        if method == "GET" and not match[2]:
            return store.job(match[1]), 200
        if method == "POST" and match[2]:
            result = store.retry(match[1])
            ensure_worker(store)
            return result, 202
    match = re.fullmatch(r"artifacts/(tpl_[a-f0-9]{32})/develop", route)
    if method == "POST" and match:
        from .development_jobs import queue_development
        result = queue_development(store, artifact(store, match[1]), body)
        ensure_worker(store)
        return result, 202
    match = re.fullmatch(r"jobs/(job_[a-f0-9]{32})/(delivery|verify-delivery)", route)
    if match:
        job = store.job(match[1])
        record = store.checkpoint(job["id"], "application-delivery")
        if job["kind"] != "application-development" or job["state"] != "completed" or not record or digest(record["result"]) != record["digest"]:
            raise FactoryError("validated application delivery is unavailable", "delivery_unavailable", 409)
        receipt = record["result"]
        archive = controlled_path(store, receipt["archive_path"])
        if hashlib.sha256(archive.read_bytes()).hexdigest() != receipt["archive_sha256"]:
            raise FactoryError("validated application archive changed", "application_changed", 409)
        if method == "GET" and match[2] == "delivery":
            return archive, "application-" + job["id"] + ".zip", "application/zip"
        if method == "POST" and match[2] == "verify-delivery":
            import base64
            if body.get("expected_archive_sha256") != receipt["archive_sha256"]:
                raise FactoryError("application archive version changed", "revision_conflict", 409)
            result = store.create_acceptance(receipt["artifact_id"], {
                "method": "blueprint-runtime", "expected_digest": receipt["template_digest"],
                "phase": receipt["phase"], "execution_confirmed": body.get("execution_confirmed"),
                "timeout": body.get("timeout", 600),
                "source_archive_base64": base64.b64encode(archive.read_bytes()).decode(),
            })
            ensure_worker(store)
            return result, 202
    if method == "POST" and route in {"blueprints/import", "blueprints/sample"}:
        if route == "blueprints/sample":
            sample = (
                Path(__file__).resolve().parents[2]
                / "docs/template-factory/blueprints/bookmark-personal"
            )
            if not sample.is_dir():
                raise FactoryError(
                    "bundled cognition sample unavailable", "not_found", 404
                )
            # Checked-in source is self-contained in a shallow/clean checkout;
            # do not depend on ignored local ZIPs or historical git objects.
            with tempfile.TemporaryDirectory(dir=store.root) as temporary:
                path = Path(temporary) / "sample.zip"
                archive_tree(sample, path)
                data = path.read_bytes()
        else:
            data = decode_archive(body.get("archive_base64"))
        return import_blueprint(
            store,
            data,
            "bundled-sample" if route.endswith("sample") else "imported-blueprint",
        ), 201
    if method == "GET" and route == "artifacts":
        filters = parse_qs(query)
        values = store.artifacts()
        # Navigation identity comes from the host-owned job snapshot, not a
        # title match. This projection does not rewrite any frozen artifact.
        with store.connect() as con:
            scene_ids = {r["id"]: (json.loads(r["snapshot"]).get("scenario") or {}).get("id")
                         for r in con.execute("SELECT id,snapshot FROM job")}
        values = [{**a, "scenario_id": scene_ids.get(a["job_id"])} for a in values]
        if filters.get("scenario_id"):
            values = [a for a in values if a["scenario_id"] == filters["scenario_id"][0]]
        if filters.get("leaf"):
            values = [a for a in values if a["leaf"] == filters["leaf"][0]]
        if filters.get("type"):
            values = [
                a
                for a in values
                if a.get("artifact_type", "runnable-starter") == filters["type"][0]
            ]
        if filters.get("published", [""])[0] == "1":
            values = [a for a in values if a["state"] == "published" and a.get("catalog_eligible", True)]
        return values, 200
    match = re.fullmatch(
        r"artifacts/(tpl_[a-f0-9]{32})/(review|download|instantiate|preview|accept|repair|blueprint|development-package)",
        route,
    )
    if match:
        value = artifact(store, match[1])
        bundle = controlled_path(store, value["bundle_path"])
        if is_blueprint(value):
            spec = verify_frozen(bundle, value["digest"])
            if method == "POST" and match[2] == "review":
                return store.artifact_action(match[1], body), 200
            if method == "GET" and match[2] == "blueprint":
                from .runtime_jobs import runtime_support

                return {
                    "artifact_id": value["id"],
                    "digest": value["digest"],
                    "spec": spec,
                    "documents": {
                        name: (bundle / "source" / name).read_text()
                        for name in (*DOCUMENTS, "TRIAL_SCOPE.md")
                        if (bundle / "source" / name).is_file()
                    },
                    "evidence_scope": "Package declarations only; imported reports do not become factory acceptance.",
                    "runtime_acceptance": runtime_support(bundle / "source", spec),
                }, 200
            if method == "POST" and match[2] == "development-package":
                if value.get("provenance", {}).get("origin") == "assisted-trial" and value["state"] == "withdrawn":
                    raise FactoryError("withdrawn assisted template requires revision before development", "assisted_review_needs_changes", 409)
                if body.get("expected_digest") != value["digest"]:
                    raise FactoryError(
                        "artifact version changed", "revision_conflict", 409
                    )
                with tempfile.TemporaryDirectory(dir=store.root) as temporary:
                    result = export_development(
                        bundle,
                        value["digest"],
                        Path(temporary) / "development",
                        body.get("project_name"),
                        body.get("phase"),
                    )
                    download_dir = store.root / "downloads"
                    download_dir.mkdir(exist_ok=True)
                    import uuid

                    download_id = uuid.uuid4().hex
                    archive_tree(
                        Path(temporary) / "development",
                        download_dir / (download_id + ".zip"),
                    )
                return {
                    **result,
                    "download_url": "/api/factory/development-downloads/" + download_id,
                    "artifact_type": "product-blueprint",
                    "message": "Development handoff only; no LLM, install or application execution.",
                }, 201
            if method == "POST" and match[2] in {"accept", "repair"}:
                result = (
                    store.create_acceptance(match[1], body)
                    if match[2] == "accept"
                    else store.create_repair(match[1], body)
                )
                ensure_worker(store)
                return result, 202
            if match[2] != "download":
                raise FactoryError(
                    "Use cognitive reading, download, development export, cognitive-review, blueprint-runtime (when a frozen runner adapter exists), or repair. Eligible versions can be published through the digest-bound review endpoint.",
                    "blueprint_operation_unavailable",
                    409,
                )
        elif match[2] in {"blueprint", "development-package"}:
            raise FactoryError(
                "this artifact is a runnable code template", "wrong_artifact_type", 409
            )
        if method == "POST" and match[2] in {"accept", "repair"}:
            result = (
                store.create_acceptance(match[1], body)
                if match[2] == "accept"
                else store.create_repair(match[1], body)
            )
            ensure_worker(store)
            return result, 202
        if method == "GET" and match[2] == "preview":
            if not value.get("preview_path"):
                raise FactoryError(
                    "no browser screenshot for this artifact", "not_found", 404
                )
            return (
                controlled_path(store, value["preview_path"]),
                "application.png",
                "image/png",
            )
        if method == "POST" and match[2] == "review":
            # Recheck frozen contents before a human review changes publication.
            with tempfile.TemporaryDirectory(dir=store.root) as temporary:
                render_template(bundle, Path(temporary) / "check", "review-check")
            return store.artifact_action(match[1], body), 200
        if method == "GET" and match[2] == "download":
            if is_blueprint(value) and value.get("provenance", {}).get("origin") == "assisted-trial":
                # Preserve host provenance/identity on a download→import roundtrip.
                # The immutable source-only archive remains untouched.
                download_dir = store.root / "downloads"
                download_dir.mkdir(exist_ok=True)
                snapshot_archive = download_dir / (value["digest"] + ".zip")
                with tempfile.TemporaryDirectory(dir=store.root) as temporary:
                    generated = Path(temporary) / "snapshot.zip"
                    archive_tree(bundle, generated)
                    os.replace(generated, snapshot_archive)
                return snapshot_archive, value["id"] + ".zip", "application/zip"
            file = controlled_path(store, value["archive_path"])
            if hashlib.sha256(file.read_bytes()).hexdigest() != value["archive_sha256"]:
                raise FactoryError(
                    "archive changed after validation", "artifact_changed", 409
                )
            return file, value["id"] + ".zip", "application/zip"
        if method == "POST" and match[2] == "instantiate":
            # No caller-supplied host path and no automatic install/code execution.
            with tempfile.TemporaryDirectory(dir=store.root) as temporary:
                directory = Path(temporary) / "app"
                render_template(bundle, directory, body.get("project_name"))
                download_dir = store.root / "downloads"
                download_dir.mkdir(exist_ok=True)
                import uuid

                download_id = uuid.uuid4().hex
                archive_tree(directory, download_dir / (download_id + ".zip"))
            return {
                "download_url": "/api/factory/downloads/" + download_id,
                "project_name": body["project_name"],
                "template_digest": value["digest"],
                "message": "Created without an LLM call. Unzip and follow README; nothing was installed on this host.",
            }, 201
    match = re.fullmatch(r"(downloads|development-downloads)/([a-f0-9]{32})", route)
    if method == "GET" and match:
        return (
            controlled_path(store, "downloads/" + match[2] + ".zip"),
            "atlas-development.zip"
            if match[1] == "development-downloads"
            else "atlas-application.zip",
            "application/zip",
        )
    match = re.fullmatch(r"jobs/(job_[a-f0-9]{32})/evidence", route)
    if method == "GET" and match:
        job = store.job(match[1])
        root = controlled_path(store, "jobs/" + job["id"])
        results = []
        for file in sorted(root.rglob("*.json")):
            if file.name not in {
                "report.json",
                "cli-summary.json",
                "plan.json",
                "discovery.json",
                "source.json",
                "baseline.json",
                "acceptance-report.json",
                "blueprint-research.json",
            }:
                if file.name != "result.json" or file.parent.name not in {
                    "scenarios",
                    "scenario-review",
                    "blueprint-research",
                    "cognitive-review",
                }:
                    continue
            file = controlled_path(store, str(file.relative_to(store.root)))
            if file.stat().st_size < 1_000_000:
                from privacy import redact_value

                results.append(
                    {
                        "path": str(file.relative_to(root)),
                        "data": redact_value(json.loads(file.read_text())),
                    }
                )
        return results, 200
    raise FactoryError("factory route not found", "not_found", 404)
