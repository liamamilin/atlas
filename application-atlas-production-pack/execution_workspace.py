"""Isolated execution workspaces and conflict-safe result application."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import uuid

from project_store import ProjectStoreError
from workspace_snapshot import DEFAULT_IGNORES, snapshot_workspace


def prepare_execution_workspace(store_root: str | Path, project_id: str,
                                source_root: str | Path,
                                expected_manifest: dict) -> tuple[Path, dict]:
    """Copy the accepted file set without VCS or ignored dependency trees."""
    source = Path(source_root).resolve()
    configured = os.environ.get("ATLAS_EXECUTION_ROOT", "").strip()
    parent = (Path(configured).expanduser().resolve() if configured else
              Path(store_root).resolve() / "execution-workspaces")
    try:
        parent.relative_to(source)
    except ValueError:
        pass
    else:
        store_key = hashlib.sha256(
            str(Path(store_root).resolve()).encode()).hexdigest()[:16]
        parent = (Path(tempfile.gettempdir()) /
                  "application-atlas-execution-workspaces" / store_key)
    parent /= project_id
    parent.mkdir(parents=True, exist_ok=True)
    target = parent / f"run_{uuid.uuid4().hex}"
    target.mkdir()
    try:
        _copy_manifest(source, target, expected_manifest.get("files") or {})
        copied = snapshot_workspace(target)
        current = snapshot_workspace(source)
        if current.get("errors") or current["files"] != expected_manifest.get("files", {}):
            raise ProjectStoreError(
                "project workspace changed while the isolated work copy was prepared")
        if copied.get("errors") or copied["files"] != expected_manifest.get("files", {}):
            raise ProjectStoreError("isolated work copy does not match the accepted baseline")
        return target, copied
    except BaseException:
        shutil.rmtree(target, ignore_errors=True)
        raise


def apply_execution_workspace(source_root: str | Path, work_root: str | Path,
                              before_manifest: dict, after_manifest: dict,
                              difference: dict, execution_id: str) -> dict:
    """Apply one reviewed work-copy diff, rolling back filesystem errors."""
    source, work = Path(source_root).resolve(), Path(work_root).resolve()
    current = snapshot_workspace(source)
    if current.get("errors") or current["files"] != before_manifest.get("files", {}):
        raise ProjectStoreError(
            "project workspace changed since execution started; review and rebase the result")
    work_current = snapshot_workspace(work)
    if work_current.get("errors") or work_current["files"] != after_manifest.get("files", {}):
        raise ProjectStoreError(
            "isolated execution result changed after it was recorded; reconcile it first")

    added = list(difference.get("added") or [])
    modified = list(difference.get("modified") or [])
    removed = list(difference.get("removed") or [])
    changed = added + modified + removed
    _reject_path_shape_transitions(added + modified, removed)
    for relative in changed:
        _relative(relative)
        _safe_destination(source, relative)

    stage = Path(tempfile.mkdtemp(
        prefix=f".atlas-apply-{execution_id[-8:]}-", dir=source))
    new_root, backup_root = stage / "new", stage / "backup"
    applied: list[str] = []
    backed_up: list[str] = []
    try:
        for relative in added + modified:
            _stage_result(work, new_root, relative, after_manifest["files"][relative])
        for relative in sorted(modified + removed, key=_depth, reverse=True):
            target, backup = source / relative, backup_root / relative
            backup.parent.mkdir(parents=True, exist_ok=True)
            os.replace(target, backup)
            backed_up.append(relative)
        _remove_empty_changed_directories(source, removed)
        for relative in sorted(added + modified, key=_depth):
            target, staged = source / relative, new_root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(staged, target)
            applied.append(relative)
        result = snapshot_workspace(source, DEFAULT_IGNORES | {stage.name})
        if result.get("errors") or result["files"] != after_manifest.get("files", {}):
            raise ProjectStoreError("applied files do not match the recorded execution result")
        shutil.rmtree(stage)
        return result
    except BaseException:
        for relative in reversed(applied):
            target = source / relative
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target, ignore_errors=True)
            else:
                target.unlink(missing_ok=True)
        for relative in sorted(backed_up, key=_depth):
            backup, target = backup_root / relative, source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if backup.exists() or backup.is_symlink():
                os.replace(backup, target)
        shutil.rmtree(stage, ignore_errors=True)
        raise


def _copy_manifest(source: Path, target: Path, files: dict):
    for relative, metadata in sorted(files.items()):
        _relative(relative)
        source_path, target_path = source / relative, target / relative
        target_path.parent.mkdir(parents=True, exist_ok=True)
        if metadata.get("kind") == "file":
            if source_path.is_symlink() or not source_path.is_file():
                raise ProjectStoreError(f"baseline file is no longer readable: {relative}")
            shutil.copy2(source_path, target_path)
        elif metadata.get("kind") == "symlink":
            link = os.readlink(source_path)
            if link != metadata.get("target"):
                raise ProjectStoreError(f"baseline symlink changed: {relative}")
            _safe_link(source, source_path.parent, link, relative)
            os.symlink(link, target_path)
        else:
            raise ProjectStoreError(f"unsupported baseline entry: {relative}")


def _stage_result(work: Path, new_root: Path, relative: str, metadata: dict):
    source, target = work / relative, new_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if metadata.get("kind") == "file":
        if source.is_symlink() or not source.is_file():
            raise ProjectStoreError(f"execution result file is unavailable: {relative}")
        shutil.copy2(source, target)
    elif metadata.get("kind") == "symlink":
        link = os.readlink(source)
        if link != metadata.get("target"):
            raise ProjectStoreError(f"execution result symlink changed: {relative}")
        _safe_link(work, source.parent, link, relative)
        os.symlink(link, target)
    else:
        raise ProjectStoreError(f"unsupported execution result entry: {relative}")


def _safe_link(root: Path, parent: Path, link: str, relative: str):
    if Path(link).is_absolute():
        raise ProjectStoreError(f"absolute symlinks cannot enter an isolated run: {relative}")
    resolved = (parent / link).resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError:
        raise ProjectStoreError(
            f"symlink points outside the project workspace: {relative}") from None


def _safe_destination(root: Path, relative: str):
    current = root
    for part in PurePosixPath(relative).parts[:-1]:
        current /= part
        if current.is_symlink():
            raise ProjectStoreError(
                f"result path has a symlinked parent in the project workspace: {relative}")
    target = root / relative
    if target.is_dir() and not target.is_symlink():
        raise ProjectStoreError(f"result would replace a directory: {relative}")


def _reject_path_shape_transitions(writes: list[str], removals: list[str]):
    for write in writes:
        for removed in removals:
            if write.startswith(removed.rstrip("/") + "/") or \
                    removed.startswith(write.rstrip("/") + "/"):
                raise ProjectStoreError(
                    "file-to-directory result transitions require a manual handoff")


def _remove_empty_changed_directories(root: Path, removals: list[str]):
    candidates = set()
    for relative in removals:
        parent = (root / relative).parent
        while parent != root:
            candidates.add(parent)
            parent = parent.parent
    for directory in sorted(candidates, key=lambda value: len(value.parts), reverse=True):
        try:
            directory.rmdir()
        except OSError:
            pass


def _relative(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ProjectStoreError("execution result contains an invalid relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or path.as_posix() != value:
        raise ProjectStoreError("execution result contains an invalid relative path")
    return path


def _depth(value: str) -> tuple[int, str]:
    return len(PurePosixPath(value).parts), value
