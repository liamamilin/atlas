"""Validate U17 linked-document sample packages."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess


REQUIRED_DOCUMENTS = {"research", "product", "technical", "tasks", "acceptance"}


def validate_package(manifest_path: str | Path) -> dict:
    manifest_path = Path(manifest_path).resolve()
    package_dir = manifest_path.parent
    manifest = json.loads(manifest_path.read_text())
    errors, warnings = [], []
    if manifest.get("schema") != 1:
        errors.append("unsupported sample package schema")
    if manifest.get("scenario") not in {"new-idea", "existing-project"}:
        errors.append("scenario must be new-idea or existing-project")

    documents = manifest.get("documents") or {}
    missing_documents = REQUIRED_DOCUMENTS - set(documents)
    if missing_documents:
        errors.append("missing document kinds: " + ", ".join(sorted(missing_documents)))
    document_text = {}
    for kind, relative in documents.items():
        path = _inside(package_dir, relative, package_dir, errors, f"document {kind}")
        if path and path.is_file():
            text = path.read_text()
            document_text[kind] = text
            if not text.strip():
                errors.append(f"document is empty: {kind}")
        elif path:
            errors.append(f"document not found: {kind}")

    repo_root = _inside(package_dir, manifest.get("repository_root", ""),
                        Path(package_dir.anchor), errors, "repository root")
    if repo_root:
        for source in manifest.get("sources") or []:
            path = _inside(repo_root, source.get("path", ""), repo_root, errors,
                           f"source {source.get('id')}")
            if not path or not path.is_file():
                errors.append(f"source not found: {source.get('id')}")
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            version = source.get("version")
            if isinstance(version, str) and version.startswith("git:"):
                revision = version.removeprefix("git:")
                if not re.fullmatch(r"[0-9a-f]{7,40}", revision):
                    errors.append(f"invalid historical source revision: {source.get('id')}")
                    continue
                historical = subprocess.run([
                    "git", "-C", str(repo_root), "show", f"{revision}:{source['path']}"],
                    capture_output=True, check=False)
                if historical.returncode:
                    errors.append(f"historical source unavailable: {source.get('id')}")
                elif hashlib.sha256(historical.stdout).hexdigest() != source.get("fingerprint"):
                    errors.append(f"historical source fingerprint mismatch: {source.get('id')}")
                if digest != source.get("fingerprint"):
                    warnings.append(f"historical source differs from working tree: {source.get('id')}")
            elif digest != source.get("fingerprint"):
                errors.append(f"source fingerprint changed: {source.get('id')}")

    requirements = _unique_by_id(manifest.get("requirements") or [], "requirement", errors)
    tasks = _unique_by_id(manifest.get("tasks") or [], "task", errors)
    acceptance = _unique_by_id(manifest.get("acceptance") or [], "acceptance", errors)
    source_ids = {item.get("id") for item in manifest.get("sources") or []}
    current_requirements = set()
    for item_id, item in requirements.items():
        if item.get("scope") == "current":
            current_requirements.add(item_id)
        for source_id in item.get("source_ids") or []:
            if source_id not in source_ids:
                errors.append(f"requirement references unknown source: {item_id}/{source_id}")
        for acceptance_id in item.get("acceptance_ids") or []:
            if acceptance_id not in acceptance:
                errors.append(f"requirement references unknown acceptance: {item_id}/{acceptance_id}")
        if item_id not in document_text.get("product", ""):
            errors.append(f"requirement missing from product document: {item_id}")

    covered_requirements = set()
    for task_id, task in tasks.items():
        for requirement_id in task.get("requirement_ids") or []:
            if requirement_id not in requirements:
                errors.append(f"task references unknown requirement: {task_id}/{requirement_id}")
            else:
                covered_requirements.add(requirement_id)
        for acceptance_id in task.get("acceptance_ids") or []:
            if acceptance_id not in acceptance:
                errors.append(f"task references unknown acceptance: {task_id}/{acceptance_id}")
        if task_id not in document_text.get("tasks", ""):
            errors.append(f"task missing from tasks document: {task_id}")
    uncovered = current_requirements - covered_requirements
    if uncovered:
        errors.append("current requirements without tasks: " + ", ".join(sorted(uncovered)))

    for acceptance_id in acceptance:
        if acceptance_id not in document_text.get("acceptance", ""):
            errors.append(f"acceptance missing from acceptance document: {acceptance_id}")
    for item in manifest.get("uncertainties") or []:
        if not item.get("id") or not item.get("owner") or not item.get("next_step"):
            errors.append("uncertainty requires id, owner, and next_step")
        if item.get("status") not in {"open", "resolved", "deferred"}:
            errors.append(f"invalid uncertainty status: {item.get('id')}")
        if item.get("id") and not any(item["id"] in text for text in document_text.values()):
            warnings.append(f"uncertainty not mentioned in documents: {item['id']}")

    if manifest.get("scenario") == "new-idea":
        search = manifest.get("search") or {}
        if not search.get("type_hits") or not search.get("application_hits"):
            errors.append("new-idea sample requires type and application search results")
    if manifest.get("scenario") == "existing-project":
        baseline = manifest.get("baseline") or {}
        if not baseline.get("observed") or not baseline.get("unknown"):
            errors.append("existing-project sample requires observed and unknown baseline facts")
    return {"valid": not errors, "errors": errors, "warnings": warnings,
            "counts": {"documents": len(document_text), "requirements": len(requirements),
                       "tasks": len(tasks), "acceptance": len(acceptance)}}


def _unique_by_id(items: list[dict], label: str, errors: list[str]) -> dict[str, dict]:
    result = {}
    for item in items:
        item_id = item.get("id")
        if not item_id:
            errors.append(f"{label} is missing id")
        elif item_id in result:
            errors.append(f"duplicate {label} id: {item_id}")
        else:
            result[item_id] = item
    return result


def _inside(base: Path, relative: str, boundary, errors: list[str], label: str) -> Path | None:
    if not isinstance(relative, str) or not relative:
        errors.append(f"{label} path is required")
        return None
    path = (base / relative).resolve()
    boundary = Path(boundary).resolve()
    try:
        path.relative_to(boundary)
    except ValueError:
        errors.append(f"{label} escapes its root")
        return None
    return path
