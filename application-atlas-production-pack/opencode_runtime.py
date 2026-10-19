"""Lifecycle for the local OpenCode server used by U17 executions."""
from __future__ import annotations

import atexit
import json
import os
from pathlib import Path
import secrets
import shutil
import socket
import subprocess
import threading
import time

from opencode_client import OpenCodeClient
from opencode_permissions import (
    detect_opencode_major_version, execution_permission_config,
    install_workdir_permission_policy,
)


class OpenCodeRuntime:
    """Reuse a configured server or own one child server for this API process."""

    def __init__(self, state_root: str | Path):
        self.state_root = Path(state_root).resolve() / "runtime" / "opencode"
        self._lock = threading.RLock()
        self._process: subprocess.Popen | None = None
        self._base_url: str | None = None
        self._major_version: int | None = None
        self._username: str | None = None
        self._password: str | None = None
        self._log = None
        atexit.register(self.close)

    def client(self, directory: str | Path, allow_edit: bool = True) -> OpenCodeClient:
        workdir = Path(directory).resolve()
        if not workdir.is_dir():
            raise ValueError("execution workdir must be an existing directory")
        base_url = self.ensure()
        major_version = self.permission_major_version()
        policy = execution_permission_config(
            major_version, allow_edit=allow_edit)
        install_workdir_permission_policy(
            workdir, major_version, allow_edit=allow_edit)
        return OpenCodeClient(
            base_url, str(workdir), major_version=major_version,
            username=self._username, password=self._password,
            permissions=policy.get("permissions") if major_version >= 2 else None)

    def permission_major_version(self) -> int:
        """Return the version used to select the project permission shape."""
        if os.environ.get("ATLAS_OPENCODE_URL", "").strip():
            return self._external_major_version()
        self.ensure()
        with self._lock:
            return self._major_version or 1

    def _external_major_version(self) -> int:
        executable = os.environ.get("ATLAS_OPENCODE_BINARY", "").strip()
        if not executable:
            executable = shutil.which("opencode") or "opencode"
        return detect_opencode_major_version(executable)

    def ensure(self) -> str:
        configured = os.environ.get("ATLAS_OPENCODE_URL", "").strip()
        if configured:
            if os.environ.get("ATLAS_ALLOW_UNMANAGED_OPENCODE") != "1":
                raise RuntimeError(
                    "ATLAS_OPENCODE_URL is disabled by default because Atlas cannot "
                    "verify that server's permission policy; set "
                    "ATLAS_ALLOW_UNMANAGED_OPENCODE=1 for an explicit trusted override")
            major_version = self._external_major_version()
            self._username = os.environ.get("ATLAS_OPENCODE_USERNAME", "opencode")
            self._password = os.environ.get("ATLAS_OPENCODE_PASSWORD")
            client = OpenCodeClient(
                configured, str(self.state_root), major_version=major_version,
                username=os.environ.get("ATLAS_OPENCODE_USERNAME", "opencode"),
                password=os.environ.get("ATLAS_OPENCODE_PASSWORD"))
            client.health()
            return configured.rstrip("/")
        with self._lock:
            if self._base_url and self._process and self._process.poll() is None:
                try:
                    OpenCodeClient(
                        self._base_url, str(self.state_root),
                        major_version=self._major_version,
                        username=self._username, password=self._password).health()
                    return self._base_url
                except Exception:
                    self.close()
            return self._start()

    def close(self):
        with self._lock:
            process, log = self._process, self._log
            self._process = None
            self._base_url = None
            self._major_version = None
            self._username = None
            self._password = None
            self._log = None
            if process and process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
            if log:
                log.close()

    def _start(self) -> str:
        self.state_root.mkdir(parents=True, exist_ok=True, mode=0o700)
        os.chmod(self.state_root, 0o700)
        executable = os.environ.get("ATLAS_OPENCODE_BINARY", "").strip()
        if not executable:
            executable = shutil.which("opencode") or "opencode"
        major_version = detect_opencode_major_version(executable)
        config = execution_permission_config(major_version, allow_edit=False)
        config_path = self.state_root / "opencode.json"
        config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
        os.chmod(config_path, 0o600)
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        self._base_url = f"http://127.0.0.1:{port}"
        self._major_version = major_version
        # V2's server currently fixes the Basic-auth username to `opencode`;
        # keep the generated password private to this Atlas child process.
        self._username = "opencode"
        self._password = secrets.token_urlsafe(32)
        self._log = (self.state_root / "server.log").open("ab")
        os.chmod(self._log.fileno(), 0o600)
        environment = {
            **os.environ,
            "OPENCODE_CONFIG": str(config_path),
            "OPENCODE_SERVER_USERNAME": self._username,
            "OPENCODE_SERVER_PASSWORD": self._password,
        }
        self._process = subprocess.Popen(
            [executable, "serve", "--hostname", "127.0.0.1",
             "--port", str(port), "--print-logs", "--log-level", "warn"],
            cwd=self.state_root, env=environment, stdout=self._log,
            stderr=subprocess.STDOUT)
        client = OpenCodeClient(
            self._base_url, str(self.state_root), timeout=2,
            major_version=major_version, username=self._username,
            password=self._password)
        deadline = time.monotonic() + 12
        last_error: BaseException | None = None
        while time.monotonic() < deadline:
            if self._process.poll() is not None:
                break
            try:
                client.health()
                return self._base_url
            except BaseException as error:
                last_error = error
                time.sleep(.1)
        code = self._process.poll()
        self.close()
        detail = f"OpenCode server exited with status {code}" if code is not None \
            else f"OpenCode server did not become healthy: {last_error}"
        raise RuntimeError(detail)


_RUNTIMES: dict[str, OpenCodeRuntime] = {}
_RUNTIMES_LOCK = threading.Lock()


def get_opencode_runtime(state_root: str | Path) -> OpenCodeRuntime:
    key = str(Path(state_root).resolve())
    with _RUNTIMES_LOCK:
        if key not in _RUNTIMES:
            _RUNTIMES[key] = OpenCodeRuntime(key)
        return _RUNTIMES[key]
