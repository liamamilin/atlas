"""Build a portable task handoff from Atlas-owned state only."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from atlas_runtime import atomic_json, atomic_write
from project_store import ProjectStore


def build_handoff(store: ProjectStore, task_id: str) -> dict:
    context = store.task_context(task_id)
    task = context["task"]
    return {
        "schema": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        **context,
        "recovery": _recovery(task, context["snapshots"], context["executions"]),
    }


def write_handoff(store: ProjectStore, task_id: str, output_dir: str | Path) -> dict:
    bundle = build_handoff(store, task_id)
    output = Path(output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    stem = f"handoff-{task_id}"
    json_path, markdown_path = output / f"{stem}.json", output / f"{stem}.md"
    atomic_json(json_path, bundle)
    atomic_write(markdown_path, render_markdown(bundle))
    return {"bundle": bundle, "json_path": str(json_path),
            "markdown_path": str(markdown_path)}


def render_markdown(bundle: dict) -> str:
    project, task = bundle["project"], bundle["task"]
    iteration = bundle.get("iteration")
    lines = [
        f"# Task handoff: {task['title']}", "",
        "## Project", "",
        f"- Project ID: `{project['id']}`",
        f"- Name: {project['name']}",
        f"- Objective: {project['objective']}",
        f"- Workspace: `{project['workspace']}`",
        "", "## Iteration", "",
        (f"- `{iteration['id']}` · {iteration['title']} · `{iteration['status']}`"
         if iteration else "- No iteration is bound to this task."),
        "", "## Task", "",
        f"- Task ID: `{task['id']}`",
        f"- Objective: {task['objective']}",
        f"- Execution: `{task['execution_status']}`",
        f"- Acceptance: `{task['acceptance_status']}`",
        "", "## Required document versions", "",
    ]
    for document in bundle["documents"]:
        lines.extend([
            f"### {document['title']} · v{document['version']}", "",
            f"Document/version: `{document['document_id']}` / `{document['version_id']}`",
            f"SHA-256: `{document['content_sha256']}`", "", document["content"], "",
        ])
    lines.extend(["## Workspace evidence", ""])
    if bundle["snapshots"]:
        for snapshot in bundle["snapshots"]:
            lines.append(
                f"- `{snapshot['phase']}` snapshot `{snapshot['id']}`: "
                f"`{snapshot['fingerprint']}` at `{snapshot['workspace_root']}`")
    else:
        lines.append("- No Atlas workspace snapshot is recorded.")
    lines.extend(["", "## Execution evidence", ""])
    if bundle["executions"]:
        for execution in bundle["executions"]:
            lines.append(
                f"- `{execution['id']}` via `{execution['engine']}`: "
                f"`{execution['status']}`; raw evidence is in the JSON bundle.")
    else:
        lines.append("- No execution is recorded.")
    lines.extend(["", "## Confirmed requirements", ""])
    if bundle["requirements"]:
        for requirement in bundle["requirements"]:
            lines.append(f"- `{requirement['id']}` [{requirement['confirmed_scope']}]: {requirement['content']}")
    else:
        lines.append("- No requirement is bound to this task.")
    lines.extend(["", "## Project decisions", ""])
    if bundle["decisions"]:
        for decision in bundle["decisions"]:
            lines.append(f"- `{decision['id']}`: {decision['statement']} — {decision['rationale']}")
    else:
        lines.append("- No project decision is recorded.")
    lines.extend(["", "## Recovery instruction", "",
                  bundle["recovery"]["instruction"], ""])
    if bundle["recovery"]["missing"]:
        lines.extend(["Missing evidence:", ""])
        lines.extend(f"- {item}" for item in bundle["recovery"]["missing"])
        lines.append("")
    return "\n".join(lines)


def validate_handoff(bundle: dict) -> dict:
    """Validate a handoff without contacting the old execution engine."""
    errors, warnings = [], []
    if bundle.get("schema") != 1:
        errors.append("unsupported handoff schema")
    project, task = bundle.get("project") or {}, bundle.get("task") or {}
    if not project.get("id") or task.get("project_id") != project.get("id"):
        errors.append("task is not bound to the exported project")
    iteration = bundle.get("iteration")
    if task.get("iteration_id"):
        if not iteration or iteration.get("id") != task.get("iteration_id"):
            errors.append("task iteration is missing or mismatched")
        elif iteration.get("project_id") != project.get("id"):
            errors.append("iteration is not bound to the exported project")
    elif iteration:
        errors.append("handoff includes an iteration not bound to the task")

    expected_versions = task.get("input_document_versions") or []
    documents = bundle.get("documents") or []
    actual_versions = [item.get("version_id") for item in documents]
    if actual_versions != expected_versions:
        errors.append("document versions do not match task inputs")
    for document in documents:
        content = document.get("content")
        if not isinstance(content, str) or hashlib.sha256(content.encode()).hexdigest() != document.get("content_sha256"):
            errors.append(f"document content fingerprint mismatch: {document.get('version_id')}")
    expected_requirements = task.get("requirement_ids") or []
    requirements = bundle.get("requirements") or []
    if [item.get("id") for item in requirements] != expected_requirements:
        errors.append("requirements do not match task inputs")
    for requirement in requirements:
        if requirement.get("confirmed_scope") != "current":
            errors.append(f"task requirement is not confirmed for current scope: {requirement.get('id')}")

    snapshots = bundle.get("snapshots") or []
    snapshot_ids = {item.get("id") for item in snapshots}
    for snapshot in snapshots:
        manifest = snapshot.get("manifest")
        digest = hashlib.sha256(json.dumps(
            manifest, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        if digest != snapshot.get("fingerprint"):
            errors.append(f"workspace snapshot fingerprint mismatch: {snapshot.get('id')}")
        if snapshot.get("workspace_root") != project.get("workspace"):
            warnings.append(f"snapshot workspace differs from project: {snapshot.get('id')}")
    for execution in bundle.get("executions") or []:
        if execution.get("task_id") != task.get("id"):
            errors.append(f"execution belongs to another task: {execution.get('id')}")
        for key in ("before_snapshot_id", "after_snapshot_id"):
            if execution.get(key) and execution[key] not in snapshot_ids:
                errors.append(f"execution references missing snapshot: {execution.get(key)}")
    if (bundle.get("recovery") or {}).get("old_engine_session_required") is not False:
        errors.append("handoff requires the old engine session")
    return {"valid": not errors, "errors": errors, "warnings": warnings}


def _recovery(task: dict, snapshots: list[dict], executions: list[dict]) -> dict:
    missing = []
    phases = {item["phase"] for item in snapshots}
    if "before" not in phases:
        missing.append("execution baseline before changes")
    if task["execution_status"] in {"completed", "failed", "stopped"} and "after" not in phases:
        missing.append("workspace snapshot after execution")
    if task["acceptance_status"] == "pending":
        missing.append("product acceptance evidence")

    if task["execution_status"] == "completed" and task["acceptance_status"] == "pending":
        instruction = "Reconcile the current workspace with the recorded baseline, then run the stated acceptance checks."
    elif task["execution_status"] in {"failed", "stopped", "unknown", "running"}:
        instruction = "Reconcile the current workspace before retrying; do not replay prior operations blindly."
    elif task["execution_status"] == "planned":
        instruction = "Confirm the recorded inputs and baseline, then begin this task in a new execution."
    else:
        instruction = "Review the recorded result and choose the next project task."
    return {"instruction": instruction, "missing": missing,
            "old_engine_session_required": False}
