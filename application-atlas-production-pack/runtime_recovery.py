"""Conservative startup recovery for Atlas project and generation state."""
from __future__ import annotations

from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import uuid

from atlas_runtime import atomic_json
from project_generation import list_generations, mark_generation_interrupted
from privacy import redact_text

ACTIVE_EXECUTION_STATES = {"queued", "running", "waiting_permission", "waiting_input"}


def acquire_project_store_lock(store_path: str | Path):
    store_path = Path(store_path).resolve()
    runtime = store_path.parent / "runtime"
    runtime.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(runtime, 0o700)
    path = runtime / "api-process.lock"
    stream = path.open("a+", encoding="utf-8")
    os.chmod(path, 0o600)
    try:
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as error:
        stream.close()
        raise RuntimeError("another Atlas API process is using this project store") from error
    stream.seek(0)
    stream.truncate()
    stream.write(json.dumps({
        "pid": os.getpid(),
        "acquired_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }) + "\n")
    stream.flush()
    os.fsync(stream.fileno())
    return stream


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def _recovery_root(store) -> Path:
    root = store.path.parent / "runtime" / "recovery"
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(root, 0o700)
    return root


def _write_report(store, report: dict) -> Path:
    root = _recovery_root(store)
    name = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + f"-{uuid.uuid4().hex[:8]}.json"
    path = root / name
    atomic_json(path, report)
    os.chmod(path, 0o600)
    latest = root / "latest.json"
    atomic_json(latest, report)
    os.chmod(latest, 0o600)
    return path


def _mark_execution_unknown(store, project_id: str, execution: dict, at: str) -> dict:
    raw = dict(execution.get("raw_state") or {})
    evidence = dict(raw.get("evidence") or {})
    events = list(evidence.get("recovery_events") or [])
    events.append({
        "event": "api_restart",
        "at": at,
        "previous_status": execution["status"],
        "action": "marked_unknown",
        "automatic_replay": False,
    })
    evidence["recovery_events"] = events[-20:]
    # Preserve interaction, assistant text, and other evidence fields while
    # changing only the lifecycle projection.
    raw.update({
        "state": "unknown",
        "engine_status": "api_restart_interrupted",
        "evidence": evidence,
    })
    return store.update_execution(execution["id"], raw, execution.get("engine_message_id"))


def _staging_directories(projects: list[dict]) -> list[dict]:
    found = []
    for project in projects:
        workspace = Path(project["workspace"])
        if not workspace.is_dir() or workspace.is_symlink():
            continue
        try:
            children = sorted(workspace.iterdir(), key=lambda item: item.name)
        except OSError:
            continue
        for child in children:
            if child.name.startswith(".atlas-apply-") and not child.is_symlink():
                entry = {
                    "project_id": project["id"],
                    "path": str(child.resolve()),
                    "action": "reported_only",
                }
                journal_path = child / "journal.json"
                try:
                    journal = json.loads(journal_path.read_text(encoding="utf-8"))
                except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                    journal = None
                if isinstance(journal, dict) and journal.get("execution_id"):
                    entry.update({
                        "action": "explicit_apply_recovery_required",
                        "execution_id": journal.get("execution_id"),
                        "phase": journal.get("phase", "unknown"),
                        "journal": str(journal_path.resolve()),
                        "backed_up": journal.get("backed_up") or [],
                        "applied": journal.get("applied") or [],
                    })
                found.append(entry)
    return found


def recover_atlas_runtime(store) -> dict:
    """Mark interrupted work unknown without replaying commands or file writes."""
    started_at = _now()
    report = {
        "schema": 1,
        "status": "completed",
        "started_at": started_at,
        "completed_at": "",
        "automatic_replay": False,
        "executions_interrupted": [],
        "generations_interrupted": [],
        "applications_requiring_review": [],
        "staging_directories": [],
        "errors": [],
    }
    projects = store.list_projects()
    for project in projects:
        project_id = project["id"]
        try:
            executions = store.list_executions(project_id)
        except Exception as error:
            report["errors"].append({
                "scope": "executions", "project_id": project_id, "error": redact_text(str(error)),
            })
            continue
        for execution in executions:
            try:
                if execution["status"] in ACTIVE_EXECUTION_STATES:
                    _mark_execution_unknown(store, project_id, execution, _now())
                    report["executions_interrupted"].append({
                        "project_id": project_id,
                        "execution_id": execution["id"],
                        "previous_status": execution["status"],
                    })
                if execution.get("application_status") == "applying":
                    report["applications_requiring_review"].append({
                        "project_id": project_id,
                        "execution_id": execution["id"],
                        "action": "explicit_apply_recovery_required",
                    })
            except Exception as error:
                report["errors"].append({
                    "scope": "execution",
                    "project_id": project_id,
                    "execution_id": execution.get("id"),
                    "error": redact_text(str(error)),
                })
        try:
            for run in list_generations(store, project_id):
                if run.get("status") in {"queued", "running"}:
                    mark_generation_interrupted(store, project_id, run["id"])
                    report["generations_interrupted"].append({
                        "project_id": project_id,
                        "generation_id": run["id"],
                        "previous_status": run["status"],
                    })
        except Exception as error:
            report["errors"].append({
                "scope": "generations", "project_id": project_id, "error": redact_text(str(error)),
            })
    report["staging_directories"] = _staging_directories(projects)
    report["completed_at"] = _now()
    report["status"] = "completed_with_errors" if report["errors"] else "completed"
    report_path = _write_report(store, report)
    report["report_path"] = str(report_path)
    return report
