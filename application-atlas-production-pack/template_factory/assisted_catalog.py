"""Read-only navigation over frozen auxiliary artifacts and pinned delivery evidence.

This projection never publishes artifacts or writes acceptance/budget records.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .blueprints import verify_frozen
from .cases import CaseLibrary
from .store import FactoryError

ASSET_KINDS = {"development", "guide", "source", "evidence"}


def registry(store):
    path = store.pack.parent / "examples/assisted-trials/CATALOG.json"
    if not path.is_file():
        return []
    value = json.loads(path.read_text())
    if value.get("schema") != "atlas.assisted-catalog.v1":
        raise FactoryError("unsupported assisted catalog", "invalid_assisted_catalog", 409)
    return value["items"]


def asset_path(store, value):
    """Only explicitly indexed, hash-bound repository files can be served."""
    root = store.pack.parent.resolve()
    relative = Path(value["path"])
    if not relative.parts or relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in {"docs", "examples"}:
        raise FactoryError("invalid assisted file path", "invalid_assisted_asset", 409)
    path = root / relative
    if any((root / Path(*relative.parts[:i])).is_symlink() for i in range(1, len(relative.parts) + 1)):
        raise FactoryError("assisted file is a symlink", "invalid_assisted_asset", 409)
    if not path.resolve().is_relative_to(root) or not path.is_file():
        raise FactoryError("assisted file is unavailable", "not_found", 404)
    if hashlib.sha256(path.read_bytes()).hexdigest() != value["sha256"]:
        raise FactoryError("assisted file changed", "assisted_asset_changed", 409)
    return path


def _entry(store, row, artifacts):
    from .api import controlled_path

    artifact = artifacts.get(row["artifact_id"])
    if not artifact or artifact.get("provenance", {}).get("origin") != "assisted-trial":
        raise FactoryError("assisted artifact is unavailable", "not_found", 404)
    if artifact["digest"] != row["artifact_digest"]:
        raise FactoryError("assisted artifact version differs", "revision_conflict", 409)
    bundle = controlled_path(store, artifact["bundle_path"])
    spec = verify_frozen(bundle, artifact["digest"])
    scenario = json.loads((bundle / "source/inputs/scenario.json").read_text())
    files = {}
    for kind, file in row["files"].items():
        if kind not in ASSET_KINDS:
            continue
        try:
            asset_path(store, file)
            files[kind] = {"available": True, "sha256": file["sha256"],
                           "url": f"/api/factory/assisted-templates/{artifact['id']}/files/{kind}"}
        except FactoryError as error:
            files[kind] = {"available": False, "reason": error.code}
    runtime = dict(row["runtime"])
    if runtime["status"] == "core_verified" and not all(files.get(k, {}).get("available") for k in ASSET_KINDS):
        runtime["status"] = "evidence_unavailable"
    # Historical verification is not a liveness probe or strict acceptance.
    runtime.update(online_status="not_checked", strict_acceptance=False)
    provenance = artifact.get("provenance", {})
    refs = provenance.get("shared_case_refs") or provenance.get("case_basis", {}).get("case_refs", [])
    cases = []
    for ref in refs:
        case = CaseLibrary(store).get_case(ref["case_id"], ref["revision"])
        if case["digest"] != ref["digest"]:
            raise FactoryError("shared case version differs", "revision_conflict", 409)
        cases.append({"case_id": case["case_id"], "revision": case["revision"], "digest": case["digest"],
                      "app_id": case["app_id"], "sources": [
                          {"repository": s["repository"], "commit_sha": s["commit_sha"],
                           "license_files": s.get("license_files", [])} for s in case["source_snapshots"]]})
    model_production = provenance.get("imported_snapshot", {}).get("provenance", {}).get("model_production")
    production = ({"mode": model_production["mode"], "model": model_production["model"],
                   "review_status": model_production["review_status"],
                   "review_input_digest": model_production["review_input_digest"]} if model_production else None)
    supplement = row.get("production_review")
    if production and supplement:
        production["review_status"] = "incomplete_materials"
        if supplement.get("status") == "passed":
            try:
                receipt = json.loads(asset_path(store, supplement["file"]).read_text())
                if (receipt.get("schema") == "atlas.auxiliary-readable-review.v1"
                        and receipt.get("artifact_id") == artifact["id"]
                        and receipt.get("artifact_digest") == artifact["digest"]
                        and receipt.get("review_input_digest") == production["review_input_digest"]
                        and receipt.get("status") == "passed"):
                    production["review_status"] = "passed"
                    production["review_session_id"] = receipt["session_id"]
            except (FactoryError, OSError, ValueError, KeyError):
                pass  # A missing/changed receipt cannot advertise complete review.
    return {"artifact_id": artifact["id"], "digest": artifact["digest"], "key": row["key"], "production": production,
            "title": artifact["manifest"]["name"], "leaf": artifact["leaf"],
            "scenario": {k: scenario[k] for k in ("id", "revision", "name", "audience", "objective", "workflow")},
            "capabilities": [f["name"] for f in spec["features"] if f.get("phase") == "P0"],
            "limits": spec.get("limits", []), "cases": cases, "runtime": runtime, "files": files,
            "strict_status": {"publication": artifact["state"], "acceptances": artifact.get("acceptances", [])}}


def catalog(store, filters=None):
    filters = filters or {}
    artifacts = {a["id"]: a for a in store.artifacts()}
    items, unavailable = [], []
    for row in registry(store):
        if filters.get("artifact_id") and row["artifact_id"] != filters["artifact_id"]:
            continue
        existing = artifacts.get(row["artifact_id"])
        if existing and filters.get("leaf") and existing["leaf"] != filters["leaf"]:
            continue
        if existing and filters.get("case_id"):
            provenance = existing.get("provenance", {})
            refs = provenance.get("shared_case_refs") or provenance.get("case_basis", {}).get("case_refs", [])
            if not any(ref["case_id"] == filters["case_id"] and
                       (not filters.get("case_revision") or str(ref["revision"]) == filters["case_revision"]) for ref in refs):
                continue
        try:
            item = _entry(store, row, artifacts)
        except (FactoryError, OSError, ValueError, KeyError) as error:
            unavailable.append({"artifact_id": row["artifact_id"], "reason": getattr(error, "code", "unavailable")})
            continue
        if filters.get("leaf") and item["leaf"] != filters["leaf"]:
            continue
        if filters.get("scenario_id") and item["scenario"]["id"] != filters["scenario_id"]:
            continue
        if filters.get("case_id") and not any(c["case_id"] == filters["case_id"] and
                (not filters.get("case_revision") or str(c["revision"]) == filters["case_revision"]) for c in item["cases"]):
            continue
        items.append(item)
    return {"items": items, "unavailable": unavailable, "counts": {
        "total": len(items), "core_verified": sum(i["runtime"]["status"] == "core_verified" for i in items),
        "not_run": sum(i["runtime"]["status"] == "not_run" for i in items)}}


def download(store, artifact_id, kind):
    if kind not in ASSET_KINDS:
        raise FactoryError("unknown assisted file", "not_found", 404)
    row = next((r for r in registry(store) if r["artifact_id"] == artifact_id), None)
    if not row:
        raise FactoryError("assisted template not found", "not_found", 404)
    _entry(store, row, {a["id"]: a for a in store.artifacts()})
    if kind not in row["files"]:
        raise FactoryError("no application delivery for this template", "not_found", 404)
    path = asset_path(store, row["files"][kind])
    content_type = "application/zip" if path.suffix == ".zip" else "application/json" if path.suffix == ".json" else "text/markdown; charset=utf-8"
    return path, row["key"] + "-" + kind + path.suffix, content_type
