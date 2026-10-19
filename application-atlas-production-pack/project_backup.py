"""Non-destructive project backup and restore for the local Atlas store."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sqlite3
import tempfile
import uuid
import zipfile

from project_generation import ProjectLifecycleBusy, list_generations, project_lifecycle_lock
from project_store import ProjectStore

BACKUP_SCHEMA = 1
BACKUP_NAME_PATTERN = re.compile(r"^\d{8}T\d{6}Z-[0-9a-f]{8}\.zip$")
RESTORE_ID_PATTERN = re.compile(r"^restore_[0-9a-f]{32}$")
RESTORE_TARGET_CONFIRMATION = "restore_to_new_store"
BACKUP_DELETE_CONFIRMATION = "delete_backup"
BACKUP_ARTIFACT_ROOTS = ("generation-runs", "execution-evidence", "exports")
EXCLUDED_ARTIFACTS = (
    "source_workspace",
    "execution_workspaces",
    "opencode_sessions",
    "external_provider_state",
)
MAX_ARCHIVE_FILES = 100_000
MAX_ARCHIVE_UNCOMPRESSED_BYTES = 2 * 1024 * 1024 * 1024
# Schema 2 records content ownership before each filesystem transition so
# recovery never removes a later replacement at the same path.
RESTORE_JOURNAL_SCHEMA = 2
RESTORE_RECOVERY_CONFIRMATION = "cleanup_partial_restore"


class ProjectBackupError(RuntimeError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _active_work(store: ProjectStore, project_id: str) -> list[dict]:
    active = []
    for execution in store.list_executions(project_id):
        if execution["status"] in {"queued", "running", "waiting_permission", "waiting_input"}:
            active.append({"kind": "execution", "id": execution["id"]})
        elif execution.get("application_status") not in {
                "not_applicable", "applied", "superseded"}:
            active.append({
                "kind": "execution_result",
                "id": execution["id"],
                "status": execution["status"],
                "application_status": execution.get("application_status"),
            })
    for run in list_generations(store, project_id):
        if run.get("status") in {"queued", "running"}:
            active.append({"kind": "generation", "id": run["id"]})
    return active


def _remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def _copy_artifacts(source_root: Path, stage_root: Path, project_id: str) -> None:
    for name in BACKUP_ARTIFACT_ROOTS:
        source = source_root / name / project_id
        if not source.exists() and not source.is_symlink():
            continue
        if source.is_symlink():
            raise ProjectBackupError(f"artifact root is a symlink: {name}")
        for directory, names, files in os.walk(source, followlinks=False):
            for entry_name in (*names, *files):
                if (Path(directory) / entry_name).is_symlink():
                    raise ProjectBackupError("artifact contains a symlink")
        target = stage_root / "artifacts" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target, symlinks=False)


def _project_only_store(source_path: Path, target_path: Path, project_id: str) -> None:
    source = sqlite3.connect(source_path)
    target = sqlite3.connect(target_path)
    try:
        source.backup(target)
    finally:
        target.close()
        source.close()
    target_store = ProjectStore(target_path)
    # Redact legacy evidence in the copied database without mutating the live
    # store or including provider credentials in the archive.
    target_store.redact_persisted_evidence()
    for project in target_store.list_projects():
        if project["id"] == project_id:
            continue
        for execution in target_store.list_executions(project["id"]):
            if execution["status"] in {"queued", "running", "waiting_permission", "waiting_input"}:
                raw = execution.get("raw_state") or {}
                evidence = dict(raw.get("evidence") or {})
                evidence["backup_scope_recovery"] = {
                    "previous_status": execution["status"],
                    "reason": "project removed from scoped backup",
                }
                target_store.update_execution(execution["id"], {
                    "state": "unknown",
                    "engine_status": "backup_scope_removed",
                    "evidence": evidence,
                })
        target_store.delete_project(project["id"])
    with sqlite3.connect(target_path) as con:
        if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise ProjectBackupError("backup project store failed SQLite integrity_check")


def _artifact_fingerprint(root: Path, project_id: str) -> dict[str, str]:
    """Fingerprint project-owned artifacts before and after copying."""
    files = {}
    for name in BACKUP_ARTIFACT_ROOTS:
        source = root / name / project_id
        if not source.exists() and not source.is_symlink():
            continue
        if source.is_symlink() or not source.is_dir():
            raise ProjectBackupError(f"artifact root is not a directory: {name}")
        for directory, names, filenames in os.walk(source, followlinks=False):
            for entry_name in (*names, *filenames):
                entry = Path(directory) / entry_name
                if entry.is_symlink():
                    raise ProjectBackupError("artifact contains a symlink")
            for entry_name in filenames:
                entry = Path(directory) / entry_name
                relative = entry.relative_to(root).as_posix()
                files[relative] = _hash_file(entry)
    return files


def _file_manifest(stage: Path) -> dict[str, dict]:
    files = {}
    for path in sorted(stage.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(stage).as_posix()
        files[relative] = {
            "sha256": _hash_file(path),
            "size": path.stat().st_size,
        }
    return files


def _safe_tree_manifest(root: Path) -> dict[str, dict]:
    if root.is_symlink() or not root.is_dir():
        raise ProjectBackupError("restore artifact is not a regular directory")
    for directory, names, filenames in os.walk(root, followlinks=False):
        for entry_name in (*names, *filenames):
            if (Path(directory) / entry_name).is_symlink():
                raise ProjectBackupError("restore artifact contains a symlink")
    return _file_manifest(root)


def create_project_backup(store: ProjectStore, project_id: str,
                          output_dir: str | Path | None = None) -> dict:
    try:
        with project_lifecycle_lock(store, project_id, blocking=False):
            return _create_project_backup_locked(store, project_id, output_dir)
    except ProjectLifecycleBusy as error:
        raise ProjectBackupError("project has active generation or execution work") from error


def _create_project_backup_locked(store: ProjectStore, project_id: str,
                                  output_dir: str | Path | None = None) -> dict:
    project = store.get_project(project_id)
    active = _active_work(store, project_id)
    if active:
        raise ProjectBackupError("project has active generation or execution work")
    root = (Path(output_dir).expanduser().resolve() if output_dir else
            store.path.parent / "backups" / project_id)
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(root, 0o700)
    stage = Path(tempfile.mkdtemp(prefix=".backup-", dir=root))
    archive_temp = root / f".backup-{uuid.uuid4().hex}.tmp"
    archive = root / (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") +
        f"-{uuid.uuid4().hex[:8]}.zip")
    try:
        database = stage / "project.sqlite"
        artifact_fingerprint = _artifact_fingerprint(store.path.parent, project_id)
        _project_only_store(store.path, database, project_id)
        _copy_artifacts(store.path.parent, stage, project_id)
        if _artifact_fingerprint(store.path.parent, project_id) != artifact_fingerprint:
            raise ProjectBackupError("project artifacts changed while backup was being created")
        if store.get_project(project_id)["updated_at"] != project["updated_at"]:
            raise ProjectBackupError("project changed while backup was being created")
        files = _file_manifest(stage)
        manifest = {
            "schema": BACKUP_SCHEMA,
            "created_at": _now(),
            "project_id": project_id,
            "project_name": project["name"],
            "source_workspace": project["workspace"],
            "source_workspace_included": False,
            "store_scope": "selected_project",
            "included_artifact_roots": list(BACKUP_ARTIFACT_ROOTS),
            "artifact_fingerprint": artifact_fingerprint,
            "excluded": list(EXCLUDED_ARTIFACTS),
            "files": files,
        }
        (stage / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.chmod(stage / "manifest.json", 0o600)
        with zipfile.ZipFile(archive_temp, "w", zipfile.ZIP_DEFLATED) as bundle:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    bundle.write(path, Path("backup") / path.relative_to(stage))
        os.chmod(archive_temp, 0o600)
        os.replace(archive_temp, archive)
    except BaseException:
        _remove_path(stage)
        archive_temp.unlink(missing_ok=True)
        archive.unlink(missing_ok=True)
        raise
    _remove_path(stage)
    return {
        "project_id": project_id,
        "archive": str(archive),
        "archive_sha256": _hash_file(archive),
        "manifest": manifest,
    }


def _safe_member(name: str) -> PurePosixPath:
    if "\\" in name:
        raise ProjectBackupError("backup paths must use POSIX separators")
    path = PurePosixPath(name)
    if path.as_posix() != name:
        raise ProjectBackupError(f"non-canonical backup path: {name}")
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise ProjectBackupError(f"unsafe backup path: {name}")
    if path.parts[:1] != ("backup",):
        raise ProjectBackupError(f"unexpected backup path: {name}")
    return path


def _has_symlink_component(path: Path) -> bool:
    current = path if path.is_absolute() else path.absolute()
    while True:
        if current.exists() or current.is_symlink():
            if current.is_symlink():
                return True
        if current.parent == current:
            return False
        current = current.parent


def _restore_journal_path(target: Path) -> Path:
    digest = hashlib.sha256(str(target).encode("utf-8")).hexdigest()[:16]
    return target.parent / f".atlas-restore-{digest}.json"


def _write_restore_journal(path: Path, state: dict) -> None:
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8")
    os.chmod(temporary, 0o600)
    with temporary.open("rb") as stream:
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    os.chmod(path, 0o600)
    directory_fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)


def _read_restore_journal(target: Path) -> tuple[Path, dict] | None:
    path = _restore_journal_path(target)
    if not path.is_file() or path.is_symlink():
        return None
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ProjectBackupError(f"restore journal is unreadable: {error}") from error
    if not isinstance(state, dict) or state.get("schema") != RESTORE_JOURNAL_SCHEMA:
        raise ProjectBackupError("restore journal schema is invalid")
    if state.get("target_store") != str(target):
        raise ProjectBackupError("restore journal target does not match")
    if not re.fullmatch(r"prj_[A-Za-z0-9]+", str(state.get("project_id", ""))):
        raise ProjectBackupError("restore journal project id is invalid")
    if state.get("artifact_root") != str(target.parent):
        raise ProjectBackupError("restore journal artifact root does not match")
    return path, state


def inspect_project_restore(target_store: str | Path) -> dict:
    target = Path(target_store).expanduser().resolve()
    found = _read_restore_journal(target)
    if not found:
        return {"interrupted": False, "target_store": str(target)}
    path, state = found
    return {
        "interrupted": True,
        "target_store": str(target),
        "journal": str(path),
        "project_id": state.get("project_id"),
        "phase": state.get("phase", "unknown"),
        "installed_artifacts": state.get("installed_artifacts") or [],
        "artifact_fingerprints": state.get("artifact_fingerprints") or {},
        "database_sha256": state.get("database_sha256", ""),
        "database_installed": bool(state.get("database_installed")),
    }


def _validate_restore_cleanup_paths(target: Path, state: dict) -> list[Path]:
    project_id = state["project_id"]
    artifact_root = target.parent
    allowed = {
        (artifact_root / name / project_id).resolve()
        for name in BACKUP_ARTIFACT_ROOTS
    }
    paths = []
    path_values = state.get("installed_artifacts") or []
    fingerprints = state.get("artifact_fingerprints")
    if not isinstance(fingerprints, dict):
        raise ProjectBackupError("restore journal artifact fingerprints are missing")
    for value in path_values:
        if not isinstance(value, str):
            raise ProjectBackupError("restore journal artifact path is invalid")
        path = Path(value)
        if _has_symlink_component(path):
            raise ProjectBackupError("restore journal artifact path contains a symlink")
        path = path.resolve()
        if path not in allowed:
            raise ProjectBackupError("restore journal artifact path is outside the project")
        if str(path) not in fingerprints:
            raise ProjectBackupError("restore journal artifact fingerprint is missing")
        paths.append(path)
    if set(fingerprints) != {str(path) for path in paths}:
        raise ProjectBackupError("restore journal artifact fingerprints do not match paths")
    return paths


def _verify_restore_database(target: Path, stage: Path | None, state: dict) -> bool:
    if not target.exists() and not target.is_symlink():
        return False
    if target.is_symlink() or not target.is_file():
        raise ProjectBackupError("restore target is not a regular project database")
    expected = state.get("database_sha256")
    if (not isinstance(expected, str)
            or not re.fullmatch(r"[0-9a-f]{64}", expected)
            or _hash_file(target) != expected):
        raise ProjectBackupError(
            "restore target changed after database installation; refusing cleanup")
    if not state.get("database_installed"):
        staged = stage / "project.sqlite" if stage is not None else None
        if (staged is None or staged.is_symlink() or not staged.is_file()
                or _hash_file(staged) != expected):
            raise ProjectBackupError(
                "restore target exists but its database installation is unverified")
    return True


def recover_interrupted_restore(target_store: str | Path, confirm: str = "") -> dict:
    """Explicitly remove only the partial files recorded by a restore journal."""
    target = Path(target_store).expanduser().resolve()
    found = _read_restore_journal(target)
    if not found:
        raise ProjectBackupError("no interrupted restore journal was found")
    if confirm != RESTORE_RECOVERY_CONFIRMATION:
        raise ProjectBackupError(
            f"confirm must be exactly {RESTORE_RECOVERY_CONFIRMATION!r}")
    journal, state = found
    artifact_paths = _validate_restore_cleanup_paths(target, state)
    fingerprints = state["artifact_fingerprints"]
    stage_value = state.get("stage")
    if isinstance(stage_value, str):
        stage = Path(stage_value)
        if (stage.parent.resolve() != target.parent
                or not stage.name.startswith(".atlas-restore-")
                or _has_symlink_component(stage.parent)):
            raise ProjectBackupError("restore journal stage path is invalid")
    else:
        stage = None
    if stage is not None and stage.is_symlink():
        raise ProjectBackupError("restore journal stage path is a symlink")

    database = target
    database_present = _verify_restore_database(database, stage, state)

    verified_artifacts = []
    for path in artifact_paths:
        if not path.exists() and not path.is_symlink():
            continue
        if _safe_tree_manifest(path) != fingerprints[str(path)]:
            raise ProjectBackupError(
                f"restore artifact changed after installation; refusing cleanup: {path}")
        verified_artifacts.append(path)

    removed = []
    for path in verified_artifacts:
        _remove_path(path)
        removed.append(str(path))
    if database_present:
        database.unlink()
        removed.append(str(database))
    if stage is not None and (stage.exists() or stage.is_symlink()):
        _remove_path(stage)
        removed.append(str(stage))
    journal.unlink()
    return {
        "project_id": state["project_id"],
        "action": "cleanup_partial_restore",
        "target_store": str(target),
        "removed": removed,
    }


def _validate_open_backup(bundle: zipfile.ZipFile) -> dict:
    infos = bundle.infolist()
    if len(infos) > MAX_ARCHIVE_FILES:
        raise ProjectBackupError("backup contains too many files")
    if sum(item.file_size for item in infos) > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
        raise ProjectBackupError("backup expands beyond the allowed size")
    names = [item.filename for item in infos]
    if len(names) != len(set(names)):
        raise ProjectBackupError("backup contains duplicate paths")
    for item in infos:
        _safe_member(item.filename)
        mode = (item.external_attr >> 16) & 0o170000
        if mode == 0o120000:
            raise ProjectBackupError("backup symlinks are not allowed")
    manifest_info = bundle.getinfo("backup/manifest.json")
    if manifest_info.file_size > 10 * 1024 * 1024:
        raise ProjectBackupError("backup manifest is too large")
    manifest = json.loads(bundle.read(manifest_info))
    if manifest.get("schema") != BACKUP_SCHEMA:
        raise ProjectBackupError("unsupported backup schema")
    if not re.fullmatch(r"prj_[A-Za-z0-9]+", str(manifest.get("project_id", ""))):
        raise ProjectBackupError("backup project id is invalid")
    declared = manifest.get("files")
    if not isinstance(declared, dict):
        raise ProjectBackupError("backup manifest files are invalid")
    allowed_files = {f"backup/{relative}" for relative in declared}
    allowed_files.add("backup/manifest.json")
    unexpected = sorted(
        item.filename for item in infos
        if not item.is_dir() and item.filename not in allowed_files)
    if unexpected:
        raise ProjectBackupError("backup contains undeclared files: " + ", ".join(unexpected[:5]))
    for relative, expected in declared.items():
        if not isinstance(relative, str) or not isinstance(expected, dict) \
                or not isinstance(expected.get("sha256"), str) \
                or not isinstance(expected.get("size"), int):
            raise ProjectBackupError("backup manifest file entry is invalid")
        member = f"backup/{relative}"
        if member not in names:
            raise ProjectBackupError(f"backup file is missing: {relative}")
        with bundle.open(member) as stream:
            digest = hashlib.sha256()
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
            if digest.hexdigest() != expected.get("sha256"):
                raise ProjectBackupError(f"backup file hash mismatch: {relative}")
    if "backup/project.sqlite" not in names:
        raise ProjectBackupError("backup project store is missing")
    return manifest


def validate_project_backup(archive: str | Path) -> dict:
    archive = Path(archive).expanduser().resolve()
    if not archive.is_file():
        raise ProjectBackupError("backup archive does not exist")
    try:
        with zipfile.ZipFile(archive) as bundle:
            return _validate_open_backup(bundle)
    except (OSError, KeyError, TypeError, AttributeError,
            json.JSONDecodeError, zipfile.BadZipFile) as error:
        raise ProjectBackupError(f"backup archive is invalid: {error}") from error


def _backup_root(store: ProjectStore, project_id: str) -> Path:
    if not re.fullmatch(r"prj_[A-Za-z0-9]+", project_id):
        raise ProjectBackupError("project id is invalid")
    root = store.path.parent / "backups" / project_id
    if _has_symlink_component(root):
        raise ProjectBackupError("backup root contains a symlink")
    if root.exists() and (root.is_symlink() or not root.is_dir()):
        raise ProjectBackupError("backup root is not a regular directory")
    return root


def backup_archive_path(store: ProjectStore, project_id: str, archive_name: str) -> Path:
    if not BACKUP_NAME_PATTERN.fullmatch(str(archive_name)):
        raise ProjectBackupError("backup archive name is invalid")
    root = _backup_root(store, project_id)
    archive = root / archive_name
    if archive.is_symlink():
        raise ProjectBackupError("backup archive is a symlink")
    return archive


def list_project_backups(store: ProjectStore, project_id: str) -> list[dict]:
    store.get_project(project_id)
    root = _backup_root(store, project_id)
    if not root.exists():
        return []
    records = []
    for archive in sorted(root.iterdir(), key=lambda path: path.name, reverse=True):
        if (not BACKUP_NAME_PATTERN.fullmatch(archive.name)
                or archive.is_symlink() or not archive.is_file()):
            continue
        record = {
            "name": archive.name,
            "size": archive.stat().st_size,
            "valid": False,
        }
        try:
            manifest = validate_project_backup(archive)
            if manifest.get("project_id") != project_id:
                raise ProjectBackupError("backup project id does not match route")
            files = manifest.get("files") or {}
            record.update({
                "created_at": manifest.get("created_at", ""),
                "project_id": project_id,
                "project_name": manifest.get("project_name", ""),
                "sha256": _hash_file(archive),
                "source_workspace_included": False,
                "included_artifact_roots": list(manifest.get("included_artifact_roots") or []),
                "excluded": list(manifest.get("excluded") or []),
                "file_count": len(files),
                "uncompressed_bytes": sum(
                    int(value.get("size", 0)) for value in files.values()
                    if isinstance(value, dict)),
                "valid": True,
            })
        except ProjectBackupError:
            record["error_code"] = "invalid_archive"
        records.append(record)
    return records


def delete_project_backup(store: ProjectStore, project_id: str,
                           archive_name: str, confirmation: str) -> dict:
    if confirmation != BACKUP_DELETE_CONFIRMATION:
        raise ProjectBackupError(
            f"confirm must be exactly {BACKUP_DELETE_CONFIRMATION!r}")
    store.get_project(project_id)
    archive = backup_archive_path(store, project_id, archive_name)
    if not archive.exists() or archive.is_symlink() or not archive.is_file():
        raise ProjectBackupError("backup archive does not exist")
    archive.unlink()
    return {"project_id": project_id, "name": archive_name, "deleted": True}


def _restore_target_root(store: ProjectStore, project_id: str) -> Path:
    if not re.fullmatch(r"prj_[A-Za-z0-9]+", project_id):
        raise ProjectBackupError("project id is invalid")
    root = (store.path.parent / "restore-targets" / project_id).resolve()
    if _has_symlink_component(root):
        raise ProjectBackupError("restore target root contains a symlink")
    if root.exists() and (root.is_symlink() or not root.is_dir()):
        raise ProjectBackupError("restore target root is not a regular directory")
    workspace = Path(store.get_project(project_id)["workspace"]).expanduser().resolve()
    if workspace == root or root.is_relative_to(workspace) or workspace.is_relative_to(root):
        raise ProjectBackupError("restore target overlaps the project workspace")
    return root


def _restore_target_path(store: ProjectStore, project_id: str, restore_id: str) -> Path:
    if not RESTORE_ID_PATTERN.fullmatch(str(restore_id)):
        raise ProjectBackupError("restore id is invalid")
    root = _restore_target_root(store, project_id)
    target_root = root / restore_id
    if target_root.is_symlink() or (target_root.exists() and not target_root.is_dir()):
        raise ProjectBackupError("restore target is not a regular directory")
    if _has_symlink_component(target_root):
        raise ProjectBackupError("restore target contains a symlink")
    return target_root / "projects.sqlite"


def prepare_project_restore(store: ProjectStore, project_id: str) -> dict:
    store.get_project(project_id)
    root = _restore_target_root(store, project_id)
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(root, 0o700)
    restore_id = "restore_" + uuid.uuid4().hex
    target_root = root / restore_id
    target_root.mkdir(mode=0o700)
    os.chmod(target_root, 0o700)
    return {
        "restore_id": restore_id,
        "project_id": project_id,
        "status": "prepared",
        "target_store": str(target_root / "projects.sqlite"),
    }


def inspect_prepared_project_restore(store: ProjectStore, project_id: str,
                                     restore_id: str) -> dict:
    store.get_project(project_id)
    target = _restore_target_path(store, project_id, restore_id)
    status = inspect_project_restore(target)
    if status.get("interrupted"):
        state = "interrupted"
    elif target.is_file() and not target.is_symlink():
        state = "completed"
    else:
        state = "not_started"
    return {
        "restore_id": restore_id,
        "project_id": status.get("project_id") or project_id,
        "status": state,
        "interrupted": bool(status.get("interrupted")),
        "phase": status.get("phase", ""),
        "database_installed": bool(status.get("database_installed")),
        "installed_artifact_count": len(status.get("installed_artifacts") or []),
    }


def restore_prepared_project_backup(store: ProjectStore, project_id: str,
                                     archive_name: str, restore_id: str,
                                     confirmation: str) -> dict:
    if confirmation != RESTORE_TARGET_CONFIRMATION:
        raise ProjectBackupError(
            f"confirm must be exactly {RESTORE_TARGET_CONFIRMATION!r}")
    archive = backup_archive_path(store, project_id, archive_name)
    target = _restore_target_path(store, project_id, restore_id)
    manifest = validate_project_backup(archive)
    if manifest.get("project_id") != project_id:
        raise ProjectBackupError("backup project id does not match route")
    result = restore_project_backup(archive, target)
    return {
        "restore_id": restore_id,
        "backup_name": archive_name,
        "status": "completed",
        "project_id": result["project_id"],
        "project": result["project"],
        "artifacts_restored_count": len(result.get("artifacts_restored") or []),
    }


def recover_prepared_project_restore(store: ProjectStore, project_id: str,
                                      restore_id: str, confirmation: str) -> dict:
    if confirmation != RESTORE_RECOVERY_CONFIRMATION:
        raise ProjectBackupError(
            f"confirm must be exactly {RESTORE_RECOVERY_CONFIRMATION!r}")
    target = _restore_target_path(store, project_id, restore_id)
    status = inspect_project_restore(target)
    if not status.get("interrupted"):
        raise ProjectBackupError("no interrupted restore exists for this target")
    if status.get("project_id") != project_id:
        raise ProjectBackupError("restore journal project id does not match route")
    result = recover_interrupted_restore(target, confirmation)
    return {
        "restore_id": restore_id,
        "project_id": project_id,
        "status": "recovered",
        "removed_count": len(result.get("removed") or []),
    }


def restore_project_backup(archive: str | Path, target_store: str | Path) -> dict:
    archive = Path(archive).expanduser().resolve()
    raw_target = Path(target_store).expanduser()
    # The caller chooses the restore root; resolve system aliases such as
    # /var -> /private/var, then validate the canonical destination below.
    target = raw_target.resolve()
    journal_path = _restore_journal_path(target)
    if journal_path.is_symlink():
        raise ProjectBackupError("restore journal path is a symlink")
    if _read_restore_journal(target) is not None:
        raise ProjectBackupError(
            "an interrupted restore journal exists; inspect and recover it explicitly")
    if target.exists():
        raise ProjectBackupError("restore target project store already exists")
    artifact_root = target.parent
    if _has_symlink_component(artifact_root):
        raise ProjectBackupError("restore artifact root contains a symlink")
    installed_artifacts = []
    installed_database = False
    stage = None
    journal_state = None
    defer_stage_cleanup = False
    try:
        # Validate and extract from the same open archive handle. This prevents
        # a path replacement between inspection and restore from bypassing the
        # manifest/hash checks.
        with zipfile.ZipFile(archive) as bundle:
            manifest = _validate_open_backup(bundle)
            for name in BACKUP_ARTIFACT_ROOTS:
                if _has_symlink_component(artifact_root / name):
                    raise ProjectBackupError("restore artifact root contains a symlink")
            conflicts = [
                name for name in BACKUP_ARTIFACT_ROOTS
                if (artifact_root / name / manifest["project_id"]).exists()
            ]
            if conflicts:
                raise ProjectBackupError(
                    "restore target already has project artifacts: " + ", ".join(conflicts))
            artifact_root.mkdir(parents=True, exist_ok=True, mode=0o700)
            os.chmod(artifact_root, 0o700)
            if _has_symlink_component(artifact_root):
                raise ProjectBackupError("restore artifact root changed during restore")
            stage = Path(tempfile.mkdtemp(prefix=".atlas-restore-", dir=artifact_root))
            journal_state = {
                "schema": RESTORE_JOURNAL_SCHEMA,
                "project_id": manifest["project_id"],
                "target_store": str(target),
                "artifact_root": str(artifact_root),
                "stage": str(stage),
                "phase": "extracting",
                "installed_artifacts": [],
                "artifact_fingerprints": {},
                "database_sha256": "",
                "database_installed": False,
            }
            _write_restore_journal(journal_path, journal_state)
            for item in bundle.infolist():
                relative = _safe_member(item.filename)
                target_path = stage.joinpath(*relative.parts[1:])
                if item.is_dir():
                    target_path.mkdir(parents=True, exist_ok=True)
                    continue
                target_path.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(item) as source, target_path.open("wb") as destination:
                    shutil.copyfileobj(source, destination)
                os.chmod(target_path, 0o600)
        with sqlite3.connect(stage / "project.sqlite") as con:
            if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                raise ProjectBackupError("restored project store failed SQLite integrity_check")
        restored_store = ProjectStore(stage / "project.sqlite")
        if [item["id"] for item in restored_store.list_projects()] != [manifest["project_id"]]:
            raise ProjectBackupError("restored store does not contain exactly the backed-up project")
        restored_project = restored_store.get_project(manifest["project_id"])
        workspace_value = restored_project.get("workspace")
        if not isinstance(workspace_value, str) or not workspace_value:
            raise ProjectBackupError("restored project workspace reference is invalid")
        workspace = Path(workspace_value)
        if (not workspace.is_absolute() or workspace != workspace.resolve()
                or workspace == Path("/") or _has_symlink_component(workspace)
                or manifest.get("source_workspace") != restored_project["workspace"]):
            raise ProjectBackupError("restored project workspace reference is unsafe or inconsistent")
        try:
            workspace.relative_to(artifact_root)
        except ValueError:
            pass
        else:
            raise ProjectBackupError("restored project workspace overlaps restore artifacts")
        try:
            artifact_root.relative_to(workspace)
        except ValueError:
            pass
        else:
            raise ProjectBackupError("restore artifacts overlap the project workspace")
        target.parent.mkdir(parents=True, exist_ok=True)
        journal_state["database_sha256"] = _hash_file(stage / "project.sqlite")
        journal_state["phase"] = "staged"
        _write_restore_journal(journal_path, journal_state)
        journal_state["phase"] = "installing_artifacts"
        _write_restore_journal(journal_path, journal_state)
        # Install artifacts first and the database last. A crash before the
        # final hard link therefore leaves an unambiguous, explicitly
        # recoverable partial target without a database claiming completion.
        for name in BACKUP_ARTIFACT_ROOTS:
            source = stage / "artifacts" / name
            if not source.exists():
                continue
            if source.is_symlink() or not source.is_dir():
                raise ProjectBackupError("staged restore artifact is not a regular directory")
            destination = artifact_root / name / manifest["project_id"]
            if _has_symlink_component(destination.parent):
                raise ProjectBackupError("restore artifact parent contains a symlink")
            destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            if destination.exists() or destination.is_symlink():
                raise ProjectBackupError("restore artifact destination already exists")
            fingerprint = _safe_tree_manifest(source)
            destination_key = str(destination)
            installed_artifacts.append(destination_key)
            journal_state["installed_artifacts"] = list(installed_artifacts)
            journal_state["artifact_fingerprints"][destination_key] = fingerprint
            _write_restore_journal(journal_path, journal_state)
            # The staged directory and destination share a filesystem. Rename
            # is atomic, so recovery sees either no destination or a complete
            # tree, never the partially copied directory produced by copytree.
            os.rename(source, destination)
            directory_fd = os.open(destination.parent, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
            os.chmod(destination, 0o700)
            for path in destination.rglob("*"):
                os.chmod(path, 0o700 if path.is_dir() else 0o600)
        journal_state["phase"] = "installing_database"
        _write_restore_journal(journal_path, journal_state)
        # os.link fails rather than overwriting a file created by a concurrent
        # restore. The staged database is on the same filesystem as target.
        os.link(stage / "project.sqlite", target)
        os.chmod(target, 0o600)
        installed_database = True
        journal_state["database_installed"] = True
        journal_state["phase"] = "verifying"
        _write_restore_journal(journal_path, journal_state)
        restored = ProjectStore(target).get_project(manifest["project_id"])
        result = {
            "project_id": restored["id"],
            "project": restored,
            "store": str(target),
            "artifacts_restored": [str(path) for path in installed_artifacts],
            "manifest": manifest,
        }
        _remove_path(stage)
        stage = None
        journal_path.unlink()
        return result
    except BaseException:
        if journal_state is not None:
            journal_state["phase"] = "rollback_pending"
            journal_state["installed_artifacts"] = list(installed_artifacts)
            journal_state["database_installed"] = installed_database
            try:
                _write_restore_journal(journal_path, journal_state)
            except BaseException:
                pass
            try:
                if stage is not None and stage.is_symlink():
                    raise ProjectBackupError("restore stage became a symlink")
                database_present = _verify_restore_database(target, stage, journal_state)
                if database_present:
                    target.unlink()
                for value in installed_artifacts:
                    path = Path(value)
                    if not path.exists() and not path.is_symlink():
                        continue
                    if _safe_tree_manifest(path) != journal_state["artifact_fingerprints"][value]:
                        raise ProjectBackupError(
                            f"restore artifact changed during rollback; refusing cleanup: {path}")
                    _remove_path(path)
                if stage is not None:
                    _remove_path(stage)
                    stage = None
                journal_path.unlink(missing_ok=True)
            except BaseException:
                defer_stage_cleanup = True
                raise
        raise
    finally:
        if stage is not None and not defer_stage_cleanup:
            _remove_path(stage)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create, inspect, or safely restore Atlas project backups")
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("create")
    create.add_argument("project_id")
    create.add_argument("--store", default=os.environ.get("ATLAS_PROJECT_STORE", ""))
    create.add_argument("--output", default="")
    inspect = commands.add_parser("inspect")
    inspect.add_argument("archive")
    restore = commands.add_parser("restore")
    restore.add_argument("archive")
    restore.add_argument("target_store")
    restore_status = commands.add_parser("restore-status")
    restore_status.add_argument("target_store")
    recover_restore = commands.add_parser("recover-restore")
    recover_restore.add_argument("target_store")
    recover_restore.add_argument("--confirm", default="")
    args = parser.parse_args()
    if args.command == "create":
        result = create_project_backup(
            ProjectStore(args.store or None), args.project_id,
            args.output or None)
    elif args.command == "inspect":
        result = validate_project_backup(args.archive)
    elif args.command == "restore-status":
        result = inspect_project_restore(args.target_store)
    elif args.command == "recover-restore":
        result = recover_interrupted_restore(args.target_store, args.confirm)
    else:
        result = restore_project_backup(args.archive, args.target_store)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
