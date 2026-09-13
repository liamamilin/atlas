"""Lifecycle for the local OpenCode server used by U17 executions."""
from __future__ import annotations

import atexit
import json
import os
from pathlib import Path
import socket
import subprocess
import threading
import time

from opencode_client import OpenCodeClient


class OpenCodeRuntime:
    """Reuse a configured server or own one child server for this API process."""

    def __init__(self, state_root: str | Path):
        self.state_root = Path(state_root).resolve() / "runtime" / "opencode"
        self._lock = threading.RLock()
        self._process: subprocess.Popen | None = None
        self._base_url: str | None = None
        self._log = None
        atexit.register(self.close)

    def client(self, directory: str | Path) -> OpenCodeClient:
        workdir = Path(directory).resolve()
        if not workdir.is_dir():
            raise ValueError("execution workdir must be an existing directory")
        return OpenCodeClient(self.ensure(), str(workdir))

    def ensure(self) -> str:
        configured = os.environ.get("ATLAS_OPENCODE_URL", "").strip()
        if configured:
            client = OpenCodeClient(configured, str(self.state_root))
            client.health()
            return configured.rstrip("/")
        with self._lock:
            if self._base_url and self._process and self._process.poll() is None:
                try:
                    OpenCodeClient(self._base_url, str(self.state_root)).health()
                    return self._base_url
                except Exception:
                    self.close()
            return self._start()

    def close(self):
        with self._lock:
            process, log = self._process, self._log
            self._process = None
            self._base_url = None
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
        self.state_root.mkdir(parents=True, exist_ok=True)
        config = {
            "$schema": "https://opencode.ai/config.json",
            "permission": {
                "read": "allow", "glob": "allow", "grep": "allow", "list": "allow",
                "edit": "allow", "bash": "ask", "question": "allow",
                "external_directory": "deny", "webfetch": "deny", "websearch": "deny",
                "task": "deny", "skill": "deny",
            },
        }
        config_path = self.state_root / "opencode.json"
        config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n")
        with socket.socket() as probe:
            probe.bind(("127.0.0.1", 0))
            port = probe.getsockname()[1]
        self._base_url = f"http://127.0.0.1:{port}"
        self._log = (self.state_root / "server.log").open("ab")
        environment = {**os.environ, "OPENCODE_CONFIG": str(config_path)}
        self._process = subprocess.Popen(
            ["opencode", "serve", "--pure", "--hostname", "127.0.0.1",
             "--port", str(port), "--print-logs", "--log-level", "WARN"],
            cwd=self.state_root, env=environment, stdout=self._log,
            stderr=subprocess.STDOUT)
        client = OpenCodeClient(self._base_url, str(self.state_root), timeout=2)
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
