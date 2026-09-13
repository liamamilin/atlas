"""Atlas-owned filesystem baselines for U17 execution reconciliation."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


DEFAULT_IGNORES = frozenset({
    ".git", ".hg", ".svn", ".venv", "__pycache__", "node_modules", "dist",
})


def snapshot_workspace(root: str | Path, ignore_names=DEFAULT_IGNORES) -> dict:
    """Fingerprint regular files without following symlinks.

    The result is owned by Atlas and can be compared independently of an
    execution engine's diff endpoint.
    """
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError("workspace root must be an existing directory")
    ignored = set(ignore_names)
    files: dict[str, dict] = {}
    errors: list[dict] = []
    for current, directories, names in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        kept = []
        for name in sorted(directories):
            path = current_path / name
            if name in ignored:
                continue
            if path.is_symlink():
                _record_link(root, path, files, errors)
            else:
                kept.append(name)
        directories[:] = kept
        for name in sorted(names):
            if name in ignored:
                continue
            path = current_path / name
            if path.is_symlink():
                _record_link(root, path, files, errors)
                continue
            try:
                stat = path.stat()
                if not path.is_file():
                    continue
                digest = hashlib.sha256()
                with path.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                files[path.relative_to(root).as_posix()] = {
                    "kind": "file", "size": stat.st_size, "sha256": digest.hexdigest(),
                }
            except OSError as error:
                errors.append({"path": path.relative_to(root).as_posix(), "error": str(error)})
    return {"schema": 1, "root": str(root), "files": dict(sorted(files.items())), "errors": errors}


def compare_snapshots(before: dict, after: dict) -> dict:
    """Return deterministic added, removed, and content-modified paths."""
    if before.get("schema") != 1 or after.get("schema") != 1:
        raise ValueError("unsupported workspace snapshot schema")
    if before.get("root") != after.get("root"):
        raise ValueError("workspace snapshot roots differ")
    old = before.get("files") or {}
    new = after.get("files") or {}
    old_paths, new_paths = set(old), set(new)
    modified = sorted(path for path in old_paths & new_paths if old[path] != new[path])
    return {
        "root": before["root"],
        "added": sorted(new_paths - old_paths),
        "removed": sorted(old_paths - new_paths),
        "modified": modified,
        "changed": bool((old_paths ^ new_paths) or modified),
        "before_errors": before.get("errors") or [],
        "after_errors": after.get("errors") or [],
    }


def _record_link(root: Path, path: Path, files: dict, errors: list):
    try:
        target = os.readlink(path)
        files[path.relative_to(root).as_posix()] = {
            "kind": "symlink",
            "target": target,
            "sha256": hashlib.sha256(target.encode("utf-8")).hexdigest(),
        }
    except OSError as error:
        errors.append({"path": path.relative_to(root).as_posix(), "error": str(error)})
