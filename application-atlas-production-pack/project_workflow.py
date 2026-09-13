"""Validated service functions for the U17 analysis and document workflow."""
from __future__ import annotations

import difflib

from project_export import export_project
from project_store import ProjectStoreError


DOCUMENT_KINDS = {
    "analysis", "product-requirements", "interaction", "technical-plan",
    "development-plan", "acceptance-plan", "current-state",
}
SCOPE_STATES = {"current", "later", "excluded"}


def project_workspace(store, project_id):
    return {
        "project": store.get_project(project_id),
        "references": store.list_references(project_id),
        "requirements": store.list_requirements(project_id),
        "decisions": store.list_decisions(project_id),
        "documents": store.list_documents(project_id),
        "iterations": store.list_iterations(project_id),
        "tasks": store.list_tasks(project_id),
        "executions": store.list_executions(project_id),
    }


def create_requirement(store, project_id, body):
    body = _object(body)
    recommended = body.get("recommended_scope")
    if recommended is not None and recommended not in SCOPE_STATES:
        raise ValueError("recommended_scope must be current, later, excluded, or null")
    return store.create_requirement(
        project_id,
        _text(body, "content"),
        recommended,
        _optional_text(body, "recommendation_reason"),
        _text_list(body.get("acceptance_conditions", []), "acceptance_conditions"),
        _id_list(body.get("reference_ids", []), "reference_ids"),
    )


def update_requirement(store, project_id, requirement_id, body):
    body = _object(body)
    _owned_requirement(store, project_id, requirement_id)
    allowed = {"content", "recommended_scope", "recommendation_reason",
               "acceptance_conditions", "reference_ids"}
    unknown = set(body) - allowed
    if unknown:
        raise ValueError(f"unknown requirement fields: {', '.join(sorted(unknown))}")
    kwargs = {}
    if "content" in body:
        kwargs["content"] = _text(body, "content")
    if "recommended_scope" in body:
        if body["recommended_scope"] not in SCOPE_STATES:
            raise ValueError("recommended_scope must be current, later, or excluded")
        kwargs["recommended_scope"] = body["recommended_scope"]
    if "recommendation_reason" in body:
        kwargs["recommendation_reason"] = _optional_text(body, "recommendation_reason")
    if "acceptance_conditions" in body:
        kwargs["acceptance_conditions"] = _text_list(
            body["acceptance_conditions"], "acceptance_conditions")
    if "reference_ids" in body:
        kwargs["reference_ids"] = _id_list(body["reference_ids"], "reference_ids")
    return store.update_requirement(project_id, requirement_id, **kwargs)


def confirm_requirement(store, project_id, requirement_id, body):
    body = _object(body)
    _owned_requirement(store, project_id, requirement_id)
    scope = body.get("scope")
    if scope not in SCOPE_STATES:
        raise ValueError("scope must be current, later, or excluded")
    return store.confirm_requirement(requirement_id, scope, _text(body, "reason"))


def create_decision(store, project_id, body):
    body = _object(body)
    return store.record_decision(
        project_id, _text(body, "statement"), _text(body, "rationale"),
        _id_list(body.get("reference_ids", []), "reference_ids"))


def create_document(store, project_id, body):
    body = _object(body)
    kind = body.get("kind")
    if kind not in DOCUMENT_KINDS:
        raise ValueError("invalid document kind")
    return store.create_document(
        project_id, kind, _text(body, "title"), _content(body),
        _basis(body.get("basis", [])), body.get("author", "human"),
        _optional_text(body, "change_summary"))


def add_document_version(store, project_id, document_id, body):
    body = _object(body)
    document = store.get_document(document_id)
    if document["project_id"] != project_id:
        raise ProjectStoreError("document not found")
    expected = body.get("expected_current_version")
    if not isinstance(expected, int) or isinstance(expected, bool):
        raise ValueError("expected_current_version is required")
    summary = _text(body, "change_summary")
    return store.add_document_version(
        document_id, _content(body), _basis(body.get("basis", document["basis"])),
        expected, body.get("author", "human"), summary)


def document_versions(store, project_id, document_id):
    return store.list_document_versions(project_id, document_id)


def document_diff(store, project_id, document_id, from_version, to_version):
    versions = store.list_document_versions(project_id, document_id)
    by_number = {item["version"]: item for item in versions}
    if from_version is None or to_version is None:
        if len(versions) < 2:
            raise ValueError("document needs at least two versions")
        to_version = versions[0]["version"] if to_version is None else to_version
        from_version = versions[1]["version"] if from_version is None else from_version
    if from_version not in by_number or to_version not in by_number:
        raise ValueError("document version not found")
    before, after = by_number[from_version], by_number[to_version]
    diff_lines = difflib.unified_diff(
        before["content"].splitlines(), after["content"].splitlines(),
        fromfile=f"v{from_version}", tofile=f"v{to_version}", n=3, lineterm="")
    diff = "\n".join(diff_lines)
    if diff:
        diff += "\n"
    return {
        "document_id": document_id, "from_version": from_version,
        "to_version": to_version, "diff": diff,
        "from_sha256": before["content_sha256"],
        "to_sha256": after["content_sha256"],
    }


def export_bundle(store, project_id):
    return export_project(store, project_id)


def _owned_requirement(store, project_id, requirement_id):
    item = store.get_requirement(requirement_id)
    if item["project_id"] != project_id:
        raise ProjectStoreError("requirement not found")
    return item


def _object(body):
    if not isinstance(body, dict):
        raise ValueError("request body must be an object")
    return body


def _text(body, key):
    value = body.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} is required")
    return value.strip()


def _optional_text(body, key):
    value = body.get(key, "")
    if not isinstance(value, str):
        raise ValueError(f"{key} must be text")
    return value.strip()


def _content(body):
    value = body.get("content")
    if not isinstance(value, str):
        raise ValueError("content must be text")
    return value


def _text_list(value, key):
    if not isinstance(value, list) or not all(
            isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{key} must contain non-empty text")
    return [item.strip() for item in value]


def _id_list(value, key):
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"{key} must be a list of ids")
    if len(value) != len(set(value)):
        raise ValueError(f"{key} contains duplicates")
    return value


def _basis(value):
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        raise ValueError("basis must be a list of objects")
    return value
