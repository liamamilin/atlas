"""Non-production reading and export of product reference drafts and design examples.

No artifact, case, budget, queue, review or runtime status is changed here.
"""
from __future__ import annotations

import hashlib
import io
import json
import zipfile

from .store import FactoryError, digest


def _examples(store):
    root = store.pack.parent / "atlas-reference-examples-2026-10-22"
    if not root.is_dir() or root.is_symlink():
        raise FactoryError("reference examples unavailable", "not_found", 404)
    manifest = json.loads((root / "CONTENTS.json").read_text())
    documents = {item["path"]: item for item in manifest["documents"]}
    return root, manifest, documents


def examples(store, key=None):
    root, manifest, documents = _examples(store)
    items = []
    for item in manifest["templates"]:
        filename = item["directory"] + "/PRODUCT_REFERENCE.md"
        # Only the fixed package manifest's indexed document can be read.
        if filename not in documents or "/" in item["directory"] or ".." in item["directory"]:
            raise FactoryError("invalid reference example index")
        path = root / filename
        if path.is_symlink() or path.parent.is_symlink() or not path.is_file():
            raise FactoryError("reference example unavailable", "not_found", 404)
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != documents[filename]["sha256"]:
            raise FactoryError("reference example changed", "reference_changed", 409)
        if key == item["directory"]:
            return {"key": key, "name": item["name"], "markdown": data.decode(),
                    "sha256": documents[filename]["sha256"], "kind": "design_example",
                    "independent_review": "not_run", "application_runtime": "not_run"}
        items.append({"key": item["directory"], "name": item["name"], "counts": item["counts"],
                      "sha256": documents[filename]["sha256"]})
    if key is not None:
        raise FactoryError("reference example not found", "not_found", 404)
    return {"items": items, "kind": "design_example", "independent_review": "not_run",
            "application_runtime": "not_run"}


def preview(body):
    from .product_reference import render_reference, select_scope, validate_reference

    if not isinstance(body, dict) or not isinstance(body.get("reference"), dict):
        raise FactoryError("reference object is required", "invalid_product_reference")
    source_ids = body.get("source_ids", [])
    if not isinstance(source_ids, list) or any(not isinstance(x, str) or not x for x in source_ids):
        raise FactoryError("source_ids must be a list of strings", "invalid_product_reference")
    # Caller supplied IDs only support a draft's structural inspection. They are
    # never treated as CaseLibrary proof or independent source verification.
    try:
        spec = validate_reference(body["reference"], source_ids=set(source_ids))
        documents = render_reference(spec, source_ids=set(source_ids))
        selection = select_scope(spec, body["scope_id"], source_ids=set(source_ids)) if body.get("scope_id") else None
    except (ValueError, TypeError, KeyError) as error:
        raise FactoryError(str(error), "invalid_product_reference") from error
    return {"artifact_kind": "product-reference-preview", "schema": spec["schema"],
            "reference_digest": digest(spec), "documents": documents,
            "scope_options": [{"id": s["id"], "name": s["name"]} for s in spec["scope_options"]],
            "selection": selection, "status": {"structure": "valid", "source_verification": "not_run",
                "independent_review": "not_run", "application_runtime": "not_run"}}


def export_preview(body):
    result = preview(body)
    buffer = io.BytesIO()
    manifest = {k: v for k, v in result.items() if k != "documents"}
    manifest["files"] = {name: hashlib.sha256(data.encode()).hexdigest() for name, data in result["documents"].items()}
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(result["documents"].items()):
            archive.writestr(name, data)
        archive.writestr("PREVIEW_MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=2))
    import base64
    data = buffer.getvalue()
    return {"filename": "product-reference-preview.zip", "archive_base64": base64.b64encode(data).decode(),
            "sha256": hashlib.sha256(data).hexdigest(), "artifact_kind": result["artifact_kind"],
            "status": result["status"]}
