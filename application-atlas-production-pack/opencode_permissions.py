"""Version-aware, recoverable OpenCode permission policies.

OpenCode V1 and V2 use different permission shapes and discover configuration
from different project locations. Atlas therefore writes a short-lived policy
into the isolated execution copy, keeps the original bytes in a private
sidecar, and restores the project before Atlas creates its after snapshot.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import threading


_POLICY_LOCK = threading.RLock()
_STATE_DIRECTORY = ".atlas-permission-state"


class OpenCodePermissionError(RuntimeError):
    """Raised when an Atlas-owned permission policy cannot be safely applied."""


def detect_opencode_major_version(executable: str = "opencode") -> int:
    """Return the installed OpenCode major version, defaulting to the V1 shape."""
    try:
        result = subprocess.run(
            [executable, "--version"], text=True, capture_output=True,
            timeout=10, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return 1
    match = re.search(r"v?(\d+)(?:\.\d+)+", result.stdout or result.stderr or "")
    return int(match.group(1)) if match else 1


def execution_permission_config(
        major_version: int, allow_edit: bool = True) -> dict:
    """Build the minimum tool policy needed by an isolated U17 execution."""
    if major_version >= 2:
        permissions = [
            # Deny plugin, MCP, and future tool actions unless explicitly opened.
            {"action": "*", "resource": "*", "effect": "deny"},
            {"action": "read", "resource": "*", "effect": "allow"},
            {"action": "glob", "resource": "*", "effect": "allow"},
            {"action": "grep", "resource": "*", "effect": "allow"},
        ]
        if allow_edit:
            permissions.append(
                {"action": "edit", "resource": "*", "effect": "allow"})
        permissions.extend([
            {"action": "question", "resource": "*", "effect": "allow"},
            # The policy is an Atlas-owned file inside the project copy. Deny
            # edits to it so the agent cannot self-upgrade its permissions.
            {"action": "edit", "resource": ".opencode/**", "effect": "deny"},
            {"action": "edit", "resource": ".opencode/opencode.json", "effect": "deny"},
            {"action": "shell", "resource": "*", "effect": "deny"},
            {"action": "webfetch", "resource": "*", "effect": "deny"},
            {"action": "websearch", "resource": "*", "effect": "deny"},
            {"action": "external_directory", "resource": "*", "effect": "deny"},
            {"action": "subagent", "resource": "*", "effect": "deny"},
            {"action": "skill", "resource": "*", "effect": "deny"},
            {"action": "execute", "resource": "*", "effect": "deny"},
        ])
        return {
            "$schema": "https://opencode.ai/config.json",
            "permissions": permissions,
            "agents": {"build": {"permissions": permissions}},
        }

    permission = {
        "read": "allow", "glob": "allow", "grep": "allow", "list": "allow",
        "code_mode": "deny", "skill": "deny", "execute": "deny",
        "edit": {
            "*": "allow" if allow_edit else "deny",
            "opencode.json": "deny",
            ".opencode/opencode.json": "deny",
        },
        "bash": "deny",
        "question": "allow", "external_directory": "deny",
        "webfetch": "deny", "websearch": "deny",
        "mcp": "deny", "application_atlas_*": "deny",
        "task": "deny",
    }
    return {
        "$schema": "https://opencode.ai/config.json",
        "permission": permission,
        "agent": {"build": {"permission": permission}},
        "tools": {
            "bash": False, "webfetch": False, "websearch": False, "task": False,
            "code_mode": False, "skill": False, "execute": False,
            "mcp": False,
        },
    }


def install_workdir_permission_policy(
        workdir: str | Path, major_version: int,
        allow_edit: bool = True) -> dict:
    """Install an Atlas-owned policy in an OpenCode-discovered project path.

    The operation is idempotent for the same workdir. A private sidecar beside
    (never inside) the workdir preserves the original config across an API
    restart, allowing ``_finish`` to restore it before snapshotting.
    """
    raw_root = Path(workdir)
    root = raw_root.resolve()
    if raw_root.is_symlink() or not root.is_dir():
        raise OpenCodePermissionError("permission workdir must be a real directory")
    with _POLICY_LOCK:
        state_path = _state_path(root)
        if state_path.exists():
            state = _read_state(state_path, root)
            _write_policy(state, major_version, allow_edit)
            return state

        target = (root / ".opencode" / "opencode.json" if major_version >= 2
                  else root / "opencode.json")
        _validate_target(root, target)
        existed = target.exists()
        original = target.read_bytes() if existed else None
        mode = target.stat().st_mode & 0o777 if existed else 0o600
        state = {
            "schema": 1,
            "root": str(root),
            "target": str(target),
            "existed": existed,
            "original_base64": (
                base64.b64encode(original).decode("ascii") if original is not None
                else None),
            "mode": mode,
            "major_version": int(major_version),
            "allow_edit": bool(allow_edit),
        }
        state_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(state_path.parent, 0o700)
        _atomic_write_json(state_path, state)
        _write_policy(state, major_version, allow_edit)
        return state


def remove_workdir_permission_policy(workdir: str | Path) -> bool:
    """Restore the pre-Atlas project config and remove its private sidecar."""
    root = Path(workdir).resolve()
    state_path = _state_path(root)
    with _POLICY_LOCK:
        if not state_path.exists():
            return False
        if not root.exists():
            # The isolated copy is disposable; do not recreate a removed
            # workspace merely to restore its temporary project config.
            state_path.unlink()
            try:
                state_path.parent.rmdir()
            except OSError:
                pass
            return True
        state = _read_state(state_path, root)
        target = Path(state["target"])
        _validate_target(root, target)
        if state.get("existed"):
            original = base64.b64decode(state.get("original_base64") or "", validate=True)
            if target.exists() and (target.is_symlink() or not target.is_file()):
                raise OpenCodePermissionError(
                    "agent replaced the temporary permission policy with a non-file")
            target.parent.mkdir(parents=True, exist_ok=True)
            _atomic_write_bytes(target, original)
            os.chmod(target, int(state.get("mode", 0o600)) & 0o777)
        else:
            if target.exists() and target.is_dir() and not target.is_symlink():
                raise OpenCodePermissionError(
                    "agent replaced the temporary permission policy with a directory")
            target.unlink(missing_ok=True)
        try:
            if target.parent.name == ".opencode":
                target.parent.rmdir()
        except OSError:
            pass
        state_path.unlink()
        try:
            state_path.parent.rmdir()
        except OSError:
            pass
        return True


def _write_policy(state: dict, major_version: int, allow_edit: bool) -> None:
    root = Path(state["root"])
    expected_target = (root / ".opencode" / "opencode.json" if major_version >= 2
                       else root / "opencode.json")
    if Path(state["target"]) != expected_target:
        raise OpenCodePermissionError("OpenCode major version changed during one execution")
    target = expected_target
    _validate_target(root, target)
    config = execution_permission_config(major_version, allow_edit=allow_edit)
    _atomic_write_json(target, config, mode=0o400)
    state["major_version"] = int(major_version)
    state["allow_edit"] = bool(allow_edit)
    _atomic_write_json(_state_path(root), state)


def _read_state(path: Path, root: Path) -> dict:
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise OpenCodePermissionError("permission policy sidecar is unreadable") from error
    if not isinstance(state, dict) or state.get("schema") != 1 or \
            state.get("root") != str(root):
        raise OpenCodePermissionError("permission policy sidecar is invalid")
    _validate_target(root, Path(str(state.get("target") or "")))
    return state


def _validate_target(root: Path, target: Path) -> None:
    try:
        target.resolve().relative_to(root)
        target.parent.resolve().relative_to(root)
    except (OSError, ValueError) as error:
        raise OpenCodePermissionError(
            "permission policy target escapes the isolated workdir") from error
    if target.is_symlink():
        raise OpenCodePermissionError("refusing to replace a symlinked OpenCode config")
    if target.exists() and not target.is_file():
        raise OpenCodePermissionError("OpenCode config target is not a regular file")


def _state_path(root: Path) -> Path:
    digest = hashlib.sha256(str(root).encode("utf-8")).hexdigest()
    return root.parent / _STATE_DIRECTORY / f"{digest}.json"


def _atomic_write_json(path: Path, value: dict, mode: int = 0o600) -> None:
    payload = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    _atomic_write_bytes(path, payload, mode=mode)


def _atomic_write_bytes(path: Path, payload: bytes, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        os.fchmod(descriptor, mode)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        os.chmod(path, mode)
    finally:
        temporary.unlink(missing_ok=True)
