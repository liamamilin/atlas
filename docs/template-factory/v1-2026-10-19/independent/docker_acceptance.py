"""Independent Docker + Chromium acceptance executor for frozen Python web targets."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import re
import shutil
import socket
import subprocess
import tempfile
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PLAYWRIGHT = ROOT / "atlas-web/node_modules/playwright"
IMAGE_DEFAULT = "python:3.12-slim"
sys_path_root = str(ROOT / "application-atlas-production-pack")
if sys_path_root not in os.sys.path:
    os.sys.path.insert(0, sys_path_root)
from template_factory.store import digest as atlas_digest
from template_factory.artifacts import tree_manifest
from template_factory.delivery import prepare_application


class DockerCommandTimeout(subprocess.TimeoutExpired):
    """A bounded Docker CLI call timed out; classify it as an environment block."""


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def source_hashes(root):
    output = {}
    for base, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d != ".git" and d != "__pycache__")
        for name in sorted(files):
            path = Path(base) / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                output[rel] = {"symlink": os.readlink(path)}
            elif path.is_file():
                output[rel] = sha256(path)
    return output


def validate_phase_assertions(assertions, required_ids, phase):
    """Validate one phase without treating a pre-restart seed as restart proof."""
    if not isinstance(assertions, list):
        return ["<assertions-array>"], []
    observed = {}
    for item in assertions:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            observed[item["id"]] = item
    missing = sorted(set(required_ids) - observed.keys())
    failed = sorted(case_id for case_id in required_ids
                    if case_id in observed and observed[case_id].get("passed") is not True)
    if phase == "initial":
        failed.extend(case_id for case_id in observed if "restart" in case_id.lower())
    return sorted(set(missing)), sorted(set(failed))


def validate_combined_assertions(phase_results, required_ids):
    """Require every frozen case to pass; restart proof must come post-restart."""
    passed = set()
    for phase, result in phase_results:
        for item in result.get("assertions", []) if isinstance(result, dict) else []:
            if isinstance(item, dict) and item.get("passed") is True:
                if "restart" not in str(item.get("id", "")).lower() or phase == "after-restart":
                    passed.add(item.get("id"))
    return sorted(set(required_ids) - passed)


def validate_runtime_binding(binding, *, phase, template_digest, suite_digest,
                             case_basis_digest, application_files=None):
    """Bind execution inputs to the generated-application target before Docker."""
    if not isinstance(binding, dict):
        raise ValueError("runtime target binding must be a JSON object")
    if binding.get("target_kind") != "generated_application":
        raise ValueError("runtime target binding target_kind must be generated_application")
    if binding.get("selected_phase") != phase or phase != "P0":
        raise ValueError("runtime target binding selected_phase must equal the selected P0 phase")
    for label, supplied in (("artifact_digest", template_digest),
                            ("suite_digest", suite_digest),
                            ("case_basis_digest", case_basis_digest)):
        value = binding.get(label)
        if value != supplied:
            raise ValueError(f"CLI {label} does not match runtime target binding")
    app_digest = binding.get("application_digest")
    if not isinstance(app_digest, str) or not re.fullmatch(r"[0-9a-f]{64}", app_digest):
        raise ValueError("runtime target binding application_digest must be a lowercase SHA-256 digest")
    if application_files is not None:
        actual_digest = hashlib.sha256(json.dumps(
            application_files, sort_keys=True, separators=(",", ":")
        ).encode()).hexdigest()
        if actual_digest != app_digest:
            raise ValueError("verified application source inventory digest does not match target binding")
        return actual_digest
    return None


def docker(*args, check=True, timeout=30):
    try:
        return subprocess.run(["docker", *map(str, args)], check=check, text=True,
                              capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise DockerCommandTimeout(exc.cmd, exc.timeout, output=exc.output, stderr=exc.stderr) from exc


def atomic_write_json(path, value):
    path = Path(path)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("x", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def atomic_write_text(path, text):
    path = Path(path)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("x", encoding="utf-8") as stream:
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def classify_failure(stage, exc):
    if isinstance(exc, DockerCommandTimeout):
        return "blocked", "environment_docker_cli_timeout"
    if stage == "docker_daemon_preflight":
        return "blocked", "environment_docker_daemon_unavailable"
    if stage == "local_image_preflight":
        return "blocked", "environment_image_missing_or_uninspectable"
    if stage in {"docker_network_setup", "docker_container_create"}:
        return "blocked", "environment_docker_setup_failed"
    if isinstance(exc, (FileNotFoundError, TimeoutError, subprocess.TimeoutExpired, URLError)):
        return "blocked", "environment_or_readiness_timeout"
    return "failed", "product_or_acceptance_failure"


def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _strict_json_bytes(data, label):
    def pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key in {label}: {key}")
            result[key] = value
        return result
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=pairs)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid UTF-8 JSON in {label}") from exc


def _manifest_strict(root):
    root = Path(root)
    manifest = {}
    for base, dirs, files in os.walk(root, followlinks=False):
        base_path = Path(base)
        for name in list(dirs):
            item = base_path / name
            if item.is_symlink():
                raise ValueError(f"symlink in frozen source tree: {item}")
        for name in files:
            item = base_path / name
            if item.is_symlink() or not item.is_file():
                raise ValueError(f"non-regular file in frozen source tree: {item}")
            manifest[item.relative_to(root).as_posix()] = sha256(item)
    return dict(sorted(manifest.items()))


def unpack_verified_bundle(bundle_dir, destination, expected_archive_sha256):
    """Verify a formal V1 runtime submission via prepare_application and tree_manifest."""
    bundle_dir = Path(bundle_dir).resolve()
    receipt_path = bundle_dir / "delivery-receipt.json"
    archive_path = bundle_dir / "application.zip"
    application_copy = bundle_dir / "application"
    if (not receipt_path.is_file() or receipt_path.is_symlink()
            or not archive_path.is_file() or archive_path.is_symlink()
            or not application_copy.is_dir() or application_copy.is_symlink()):
        raise ValueError("bundle must contain application.zip, delivery-receipt.json and application/")
    receipt_bytes = receipt_path.read_bytes()
    receipt = _strict_json_bytes(receipt_bytes, "delivery-receipt.json")
    archive_bytes = archive_path.read_bytes()
    destination = Path(destination)
    if destination.exists():
        raise ValueError("verified extraction destination must not already exist")
    archive_sha256 = hashlib.sha256(archive_bytes).hexdigest()
    if archive_sha256 != expected_archive_sha256:
        raise ValueError("application.zip SHA-256 does not match pinned runtime input")
    extracted_metadata = prepare_application(archive_bytes, destination)
    if receipt != extracted_metadata:
        raise ValueError("delivery-receipt.json differs from official prepare_application metadata")
    root_name = receipt.get("app_root")
    if root_name not in (".", "app"):
        raise ValueError("official delivery receipt has an invalid app_root")
    app_root = destination if root_name == "." else destination / "app"
    copied_app_root = application_copy if root_name == "." else application_copy / "app"
    if tree_manifest(copied_app_root) != receipt["files"]:
        raise ValueError("submission application/ tree differs from official receipt files inventory")
    application_inventory = tree_manifest(app_root)
    if application_inventory != receipt["files"]:
        raise ValueError("verified application root differs from official receipt files inventory")
    return {
        "bundle_dir": str(bundle_dir),
        "receipt_sha256": hashlib.sha256(receipt_bytes).hexdigest(),
        "archive_sha256": archive_sha256,
        "delivery": receipt,
        "app_root": str(app_root),
        "application_inventory": application_inventory,
        "application_digest": hashlib.sha256(json.dumps(application_inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "extracted_root": str(destination),
    }


class Fixture(BaseHTTPRequestHandler):
    def do_GET(self):
        page = urlsplit(self.path).path
        if page not in ("/original", "/second", "/xss"):
            self.send_error(404)
            return
        label = "Local original fixture page" if page == "/original" else "Local secondary fixture page"
        body = f"<!doctype html><title>{label}</title><h1>{label}</h1>".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("fixture: " + fmt % args, flush=True)


RELAY_EXEC_CODE = r'''import base64,http.client,json,sys
req=json.load(sys.stdin)
conn=http.client.HTTPConnection("127.0.0.1",int(req["port"]),timeout=6)
try:
 body=base64.b64decode(req.get("body", ""),validate=True)
 conn.request(req["method"],req["path"],body=body,headers={"Host":"127.0.0.1:%s"%req["port"],**req["headers"]})
 res=conn.getresponse(); data=res.read(4*1024*1024+1)
 if len(data)>4*1024*1024: raise ValueError("upstream response exceeds relay limit")
 headers=[(k,v) for k,v in res.getheaders() if k.lower() in {"content-type","content-length","cache-control","location","set-cookie","allow","www-authenticate","etag","last-modified"}]
 print(json.dumps({"status":res.status,"headers":headers,"body":base64.b64encode(data).decode("ascii")}))
finally: conn.close()
'''


class AppRelay(BaseHTTPRequestHandler):
    container = None
    port = None
    allowed_methods = {"GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"}
    request_headers = {"accept", "content-type", "cookie", "authorization", "if-match", "if-none-match", "origin", "referer", "x-requested-with", "x-csrf-token"}
    app_origin = None
    slots = threading.BoundedSemaphore(8)

    @classmethod
    def wait_drained(cls, timeout=12):
        acquired = []
        deadline = time.monotonic() + timeout
        try:
            while len(acquired) < 8:
                remaining = deadline - time.monotonic()
                if remaining <= 0 or not cls.slots.acquire(timeout=remaining):
                    return False
                acquired.append(True)
            return True
        finally:
            for _ in acquired:
                cls.slots.release()

    def _relay(self):
        if not self.slots.acquire(blocking=False):
            self.send_error(503, "relay concurrency limit reached")
            return
        try:
            self.connection.settimeout(10)
            self._relay_request()
        finally:
            self.slots.release()

    def _relay_request(self):
        if self.command not in self.allowed_methods or not self.path.startswith("/") or self.path.startswith("//") or len(self.path) > 8192:
            self.send_error(400)
            return
        length = self.headers.get("Content-Length", "0")
        if self.headers.get("Transfer-Encoding"):
            self.send_error(411, "chunked request bodies are not accepted by the relay")
            return
        if not length.isdigit() or int(length) > 2 * 1024 * 1024:
            self.send_error(413)
            return
        body = self.rfile.read(int(length)) if int(length) else b""
        headers = {k: v for k, v in self.headers.items() if k.lower() in self.request_headers}
        origin = headers.get("Origin") or headers.get("origin")
        referer = headers.get("Referer") or headers.get("referer")
        if ((origin is not None and origin != self.app_origin)
                or (referer is not None and not referer.startswith(self.app_origin + "/"))):
            self.send_error(403, "relay accepts only the configured app origin")
            return
        request = json.dumps({"port": self.port, "method": self.command, "path": self.path,
                              "headers": headers, "body": base64.b64encode(body).decode("ascii")}).encode()
        try:
            result = subprocess.run(
                ["docker", "exec", "-i", self.container, "python3", "-c", RELAY_EXEC_CODE],
                input=request, capture_output=True, timeout=10, check=True,
            )
            answer = json.loads(result.stdout)
            data = base64.b64decode(answer["body"], validate=True)
            self.send_response(int(answer["status"]))
            for key, value in answer["headers"]:
                if key.lower() != "content-length":
                    self.send_header(key, value)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(data)
        except (subprocess.SubprocessError, OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
            self.send_error(502, "isolated app relay failed")
            print(f"app relay error: {exc!r}", flush=True)

    do_GET = do_HEAD = do_POST = do_PUT = do_PATCH = do_DELETE = do_OPTIONS = _relay

    def log_message(self, fmt, *args):
        print("app-relay: " + fmt % args, flush=True)


def command_value(command, flag):
    for i, arg in enumerate(command):
        if arg == flag:
            if i + 1 >= len(command):
                raise ValueError(f"delivery runtime.start has {flag} without a value")
            return command[i + 1]
        if arg.startswith(flag + "="):
            return arg.split("=", 1)[1]
    return None


def read_delivery(doc, app_root):
    if doc.get("schema") != "atlas.application-delivery.v1":
        raise ValueError(f"unexpected delivery schema: {doc.get('schema')!r}")
    root = doc.get("app_root")
    runtime = doc.get("runtime")
    if root not in {".", "app"} or not isinstance(runtime, dict):
        raise ValueError("official delivery app_root/runtime missing or malformed")
    start = runtime.get("start")
    if not isinstance(start, list) or not start or not all(isinstance(x, str) for x in start):
        raise ValueError("delivery runtime.start must be a nonempty argv list")
    if runtime.get("install", []) or runtime.get("build", []):
        raise ValueError("offline acceptance requires delivery install/build to be empty")
    if runtime.get("profile") != "python-web":
        raise ValueError(f"unsupported delivery runtime profile: {runtime.get('profile')!r}")
    port = runtime.get("port")
    if type(port) is not int or not (1024 <= port <= 65535):
        raise ValueError("delivery runtime.port must be a valid integer")
    if command_value(start, "--host") != "0.0.0.0":
        raise ValueError("container command must explicitly bind --host 0.0.0.0")
    if command_value(start, "--port") != str(port):
        raise ValueError("delivery start argv --port must equal runtime.port")
    data_dir = command_value(start, "--data-dir")
    if not isinstance(data_dir, str) or not (data_dir == "/state" or data_dir.startswith("/state/")) or ".." in PurePosixPath(data_dir).parts:
        raise ValueError("delivery start argv must use a data directory beneath /state")
    app_root = Path(app_root).resolve()
    if not app_root.is_dir():
        raise ValueError(f"delivery application root does not exist: {app_root}")
    return doc, start, port, app_root, data_dir, runtime.get("readiness_path", "/")


def wait_ready(base_url, container, timeout=30):
    last = None
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        state = json.loads(docker("inspect", container, timeout=5).stdout)[0]["State"]
        if not state.get("Running"):
            raise RuntimeError(f"app container exited before readiness: {state}")
        try:
            with urlopen(base_url, timeout=1) as response:
                if response.status == 200:
                    return
                last = f"HTTP {response.status}"
        except (URLError, TimeoutError, OSError) as exc:
            last = repr(exc)
        time.sleep(0.25)
    raise TimeoutError(f"app did not become ready: {last}")


def remove_temp_tree(root):
    root = Path(root)
    if not root.exists():
        return True
    for base, dirs, files in os.walk(root, topdown=False, followlinks=False):
        for name in files:
            path = Path(base) / name
            if not path.is_symlink():
                path.chmod(0o600)
        for name in dirs:
            path = Path(base) / name
            if not path.is_symlink():
                path.chmod(0o700)
        Path(base).chmod(0o700)
    shutil.rmtree(root)
    return not root.exists()


def _docker_says_missing(result):
    if result.returncode == 0:
        return False
    detail = ((result.stdout or "") + "\n" + (result.stderr or "")).lower()
    return "no such" in detail or "not found" in detail or "does not exist" in detail


def cleanup_resources(report, persist, *, container, network, temp_root,
                      container_attempted, network_attempted, fixture, fixture_thread,
                      relay=None, relay_thread=None,
                      docker_call=docker, temp_remover=remove_temp_tree):
    """Bounded, independently recorded cleanup; dependency injection supports no-Docker tests."""
    cleanup = report.setdefault("cleanup", {"events": []})
    evidence_dir = Path(report["evidence_dir"]) if report.get("evidence_dir") else None

    def preserve_interruption(exc, step_name):
        interruption = {
            "stage": f"cleanup:{step_name}",
            "error": repr(exc),
            "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        report.setdefault("cleanup_interruptions", []).append(interruption)
        if evidence_dir is not None:
            try:
                atomic_write_json(evidence_dir / "interruption.json", {
                    "status": "interrupted_during_cleanup",
                    **interruption,
                    "run_json": str(evidence_dir / "run.json"),
                })
            except BaseException as write_exc:
                report["interruption_record_error"] = repr(write_exc)

    def journal(step_name):
        try:
            persist()
            return True
        except BaseException as exc:
            cleanup.setdefault("journal_errors", []).append({"step": step_name, "error": repr(exc)})
            if isinstance(exc, KeyboardInterrupt):
                preserve_interruption(exc, f"journal:{step_name}")
            return False

    def step(name, callback):
        cleanup["events"].append({"step": name, "state": "started", "at": time.time()})
        journal(f"{name}:started")
        try:
            value = callback()
            cleanup[name] = value
            cleanup["events"].append({"step": name, "state": "completed", "at": time.time()})
        except BaseException as exc:  # A cleanup failure must not skip later cleanup or the report write.
            cleanup[name] = {"ok": False, "error": repr(exc)}
            cleanup["events"].append({"step": name, "state": "failed", "error": repr(exc), "at": time.time()})
            if isinstance(exc, KeyboardInterrupt):
                preserve_interruption(exc, name)
        journal(f"{name}:finished")
        return cleanup[name]

    def remove_container():
        if not container_attempted:
            return {"ok": True, "state": "not-created"}
        result = docker_call("rm", "--force", container, check=False, timeout=10)
        return {"ok": result.returncode == 0 or _docker_says_missing(result),
                "returncode": result.returncode, "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}

    def verify_container_absent():
        if not container_attempted:
            return {"ok": True, "state": "not-created"}
        result = docker_call("inspect", container, check=False, timeout=10)
        return {"ok": _docker_says_missing(result), "returncode": result.returncode,
                "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}

    def remove_network():
        if not network_attempted:
            return {"ok": True, "state": "not-created"}
        result = docker_call("network", "rm", network, check=False, timeout=10)
        return {"ok": result.returncode == 0 or _docker_says_missing(result),
                "returncode": result.returncode, "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}

    def verify_network_absent():
        if not network_attempted:
            return {"ok": True, "state": "not-created"}
        result = docker_call("network", "inspect", network, check=False, timeout=10)
        return {"ok": _docker_says_missing(result), "returncode": result.returncode,
                "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}

    container_removal = step("container_remove", remove_container)
    report["owned_resources"]["container"]["state"] = "removed" if container_removal.get("ok") else "cleanup-failed"
    journal("container_remove:resource-state")
    container_absence = step("container_absence_verification", verify_container_absent)
    if container_absence.get("ok"):
        report["owned_resources"]["container"]["state"] = "absent-verified"
    journal("container_absence_verification:resource-state")
    network_removal = step("network_remove", remove_network)
    if network_attempted:
        report["owned_resources"]["network"]["state"] = "removed" if network_removal.get("ok") else "cleanup-failed"
    else:
        report["owned_resources"]["network"]["state"] = "not-created; container uses built-in none network"
    journal("network_remove:resource-state")
    network_absence = step("network_absence_verification", verify_network_absent)
    if network_absence.get("ok") and network_attempted:
        report["owned_resources"]["network"]["state"] = "absent-verified"
    journal("network_absence_verification:resource-state")

    if fixture is None:
        cleanup["fixture_server_stopped"] = {"ok": True, "state": "not-created"}
        report["owned_resources"]["fixture_server"]["state"] = "not-created"
        journal("fixture_server:not-created")
    else:
        def shutdown_fixture():
            if fixture_thread is None or not fixture_thread.is_alive():
                return {"ok": True, "state": "serve-loop-not-running"}
            fixture.shutdown()
            return {"ok": True}
        step("fixture_shutdown", shutdown_fixture)
        step("fixture_server_close", lambda: (fixture.server_close(), {"ok": True})[1])
    if fixture_thread is None:
        cleanup["fixture_thread_stopped"] = {"ok": True, "state": "not-created"}
        report["owned_resources"]["fixture_thread"]["state"] = "not-created"
        journal("fixture_thread:not-created")
    else:
        def join_fixture():
            if not fixture_thread.ident:
                return {"ok": True, "state": "never-started", "alive": False}
            fixture_thread.join(timeout=3)
            return {"ok": not fixture_thread.is_alive(), "alive": fixture_thread.is_alive()}
        step("fixture_thread_stopped", join_fixture)
        cleanup["fixture_server_stopped"] = {
            "ok": all(cleanup.get(key, {}).get("ok", False) for key in (
                "fixture_shutdown", "fixture_server_close", "fixture_thread_stopped"))
        }
        report["owned_resources"]["fixture_server"]["state"] = (
            "stopped" if cleanup["fixture_server_stopped"]["ok"] else "cleanup-failed")
        report["owned_resources"]["fixture_thread"]["state"] = (
            "stopped" if cleanup["fixture_thread_stopped"]["ok"] else "cleanup-failed")
        journal("fixture:resource-state")

    if relay is None:
        cleanup["app_relay_stopped"] = {"ok": True, "state": "not-created"}
        report["owned_resources"]["app_relay"]["state"] = "not-created"
        journal("app_relay:not-created")
    else:
        def shutdown_relay():
            if relay_thread is None or not relay_thread.is_alive():
                return {"ok": True, "state": "serve-loop-not-running"}
            relay.shutdown()
            drained = AppRelay.wait_drained()
            return {"ok": drained, "active_exec_requests_drained": drained}
        step("app_relay_shutdown", shutdown_relay)
        step("app_relay_server_close", lambda: (relay.server_close(), {"ok": True})[1])
        def join_relay():
            if not relay_thread.ident:
                return {"ok": True, "state": "never-started", "alive": False}
            relay_thread.join(timeout=3)
            return {"ok": not relay_thread.is_alive(), "alive": relay_thread.is_alive()}
        step("app_relay_thread_stopped", join_relay)
        cleanup["app_relay_stopped"] = {"ok": all(cleanup.get(key, {}).get("ok", False) for key in (
            "app_relay_shutdown", "app_relay_server_close", "app_relay_thread_stopped"))}
        report["owned_resources"]["app_relay"]["state"] = "stopped" if cleanup["app_relay_stopped"]["ok"] else "cleanup-failed"
        journal("app_relay:resource-state")

    def remove_temp():
        return {"ok": temp_remover(temp_root)}
    step("temporary_state_removed", remove_temp)
    report["owned_resources"]["temporary_root"]["state"] = (
        "removed" if cleanup["temporary_state_removed"].get("ok") else "cleanup-failed")
    journal("temporary_state_removed:resource-state")
    cleanup["container_absent_verified"] = cleanup["container_absence_verification"].get("ok", False)
    cleanup["network_absent_verified"] = cleanup["network_absence_verification"].get("ok", False)
    cleanup["fixture_server_stopped"] = cleanup.get("fixture_server_stopped", {}).get("ok", False)
    cleanup["fixture_thread_stopped"] = cleanup.get("fixture_thread_stopped", {}).get("ok", False)
    cleanup["app_relay_stopped"] = cleanup.get("app_relay_stopped", {}).get("ok", False)
    cleanup["temporary_state_removed"] = cleanup["temporary_state_removed"].get("ok", False)
    cleanup["all_resources_removed"] = all(cleanup.get(key, False) for key in (
        "container_absent_verified", "network_absent_verified", "fixture_server_stopped",
        "fixture_thread_stopped", "app_relay_stopped", "temporary_state_removed"))
    journal("cleanup:summary")
    return cleanup


def finalize_cleanup_outcome(report, persist, evidence_dir, *, max_persist_attempts=2):
    """Reconcile cleanup/journal outcomes before writing the final verdict."""
    evidence_dir = Path(evidence_dir)

    def note_interruption(exc, stage_name):
        event = {
            "stage": stage_name,
            "error": repr(exc),
            "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        report.setdefault("cleanup_interruptions", []).append(event)
        try:
            atomic_write_json(evidence_dir / "interruption.json", {
                "status": "interrupted_during_cleanup", **event,
                "run_json": str(evidence_dir / "run.json"),
            })
        except BaseException as write_exc:
            report["interruption_record_error"] = repr(write_exc)

    def aggregate():
        cleanup = report.setdefault("cleanup", {})
        has_interruption = bool(report.get("cleanup_interruptions"))
        has_journal_error = bool(report.get("cleanup_journal_errors") or cleanup.get("journal_errors"))
        resources_removed = cleanup.get("all_resources_removed", False)
        if not resources_removed or has_journal_error:
            report["cleanup_failure"] = True
        if report.get("status") == "passed" and (not resources_removed or has_interruption or has_journal_error):
            if has_interruption and resources_removed:
                report["status"] = "interrupted"
                report["failure_kind"] = "cleanup_interrupted"
                report["error"] = "cleanup was interrupted after the acceptance workflow passed"
            else:
                report["status"] = "failed"
                report["failure_kind"] = "acceptance_cleanup_or_evidence_failed"
                report["error"] = "cleanup or final evidence persistence did not complete cleanly"
            report.setdefault("primary_failure", {
                "stage": "cleanup", "status": report["status"],
                "failure_kind": report["failure_kind"], "error": report["error"],
            })

    aggregate()
    for attempt in range(max_persist_attempts):
        try:
            persist()
            break
        except BaseException as exc:
            report.setdefault("cleanup_journal_errors", []).append({
                "stage": "cleanup:final_persist", "attempt": attempt + 1, "error": repr(exc),
            })
            if isinstance(exc, KeyboardInterrupt):
                note_interruption(exc, "cleanup:final_persist")
            aggregate()
    return report.get("status")


def container_meta(container, timeout=10):
    item = json.loads(docker("inspect", container, timeout=timeout).stdout)[0]
    return {
        "id": item["Id"],
        "state": {key: item["State"].get(key) for key in ("Status", "Running", "Pid", "StartedAt", "FinishedAt", "ExitCode")},
        "restart_count": item.get("RestartCount"),
        "port_bindings": item["HostConfig"].get("PortBindings"),
        "effective_ports": item["NetworkSettings"].get("Ports"),
        "networks": item["NetworkSettings"].get("Networks", {}),
        "network_mode": item["HostConfig"].get("NetworkMode"),
        "internal_rootfs": item["HostConfig"].get("ReadonlyRootfs"),
        "cap_drop": item["HostConfig"].get("CapDrop"),
        "security_options": item["HostConfig"].get("SecurityOpt"),
        "limits": {key: item["HostConfig"].get(key) for key in ("Memory", "NanoCpus", "PidsLimit")},
        "mounts": [{key: m.get(key) for key in ("Type", "Source", "Destination", "RW")} for m in item["Mounts"]],
        "environment_names": [entry.split("=", 1)[0] for entry in item["Config"].get("Env", [])],
    }


def verify_network_none(meta):
    if meta.get("network_mode") != "none":
        raise RuntimeError(f"container NetworkMode is not none: {meta.get('network_mode')!r}")
    if meta.get("port_bindings") not in (None, {}):
        raise RuntimeError("network=none container unexpectedly has published port bindings")
    networks = meta.get("networks") or {}
    if set(networks) != {"none"}:
        raise RuntimeError(f"network=none container has unexpected network attachments: {sorted(networks)}")
    ports = meta.get("effective_ports") or {}
    if any(binding for bindings in ports.values() for binding in (bindings or [])):
        raise RuntimeError("network=none container unexpectedly exposes an effective host port")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True, type=Path,
                        help="Formal V1 submission directory containing application.zip, delivery-receipt.json and application/")
    parser.add_argument("--evidence-dir", required=True, type=Path,
                        help="Use a fresh directory per run, e.g. evaluation/initial or evaluation/repair-1")
    parser.add_argument("--image", default=IMAGE_DEFAULT, help="Must already exist locally; no image pull is attempted")
    parser.add_argument("--scenario-id", required=True)
    parser.add_argument("--phase", required=True)
    parser.add_argument("--target-binding", required=True, type=Path,
                        help="Host-supplied frozen acceptance target binding JSON")
    parser.add_argument("--acceptance-adapter", required=True, type=Path,
                        help="Independent Playwright adapter implementing the frozen user-journey contract")
    parser.add_argument("--required-assertions", required=True, type=Path,
                        help="JSON list of mandatory assertion IDs fixed before the run")
    parser.add_argument("--template-digest", required=True)
    parser.add_argument("--archive-sha256", required=True,
                        help="Host-pinned SHA-256 of the submitted application.zip")
    parser.add_argument("--suite-digest", required=True)
    parser.add_argument("--case-basis-digest", required=True)
    parser.add_argument("--plan-digest", required=True)
    args = parser.parse_args()
    if not args.scenario_id.startswith("scn_"):
        parser.error("--scenario-id must be a real scn_ identifier")
    for label, path in (("target binding", args.target_binding), ("acceptance adapter", args.acceptance_adapter),
                        ("required assertions", args.required_assertions)):
        if not path.is_file() or path.is_symlink():
            parser.error(f"{label} must be an existing non-symlink file")
    target_binding = json.loads(args.target_binding.read_text(encoding="utf-8"))
    required_assertions = json.loads(args.required_assertions.read_text(encoding="utf-8"))
    if not isinstance(target_binding, dict) or target_binding.get("scenario_id") != args.scenario_id:
        parser.error("target binding does not name the selected scenario")
    if not isinstance(required_assertions, list) or not required_assertions or not all(isinstance(x, str) and x for x in required_assertions):
        parser.error("required assertions must be a non-empty JSON array of assertion IDs")
    if len(set(required_assertions)) != len(required_assertions):
        parser.error("required assertion IDs must be unique")
    for label, value in (("template digest", args.template_digest), ("archive SHA-256", args.archive_sha256), ("suite digest", args.suite_digest),
                         ("case basis digest", args.case_basis_digest), ("plan digest", args.plan_digest)):
        if not re.fullmatch(r"[0-9a-f]{64}", value):
            parser.error(f"--{label.replace(' ', '-')} must be a lowercase SHA-256 digest")
    try:
        validate_runtime_binding(
            target_binding, phase=args.phase, template_digest=args.template_digest,
            suite_digest=args.suite_digest, case_basis_digest=args.case_basis_digest,
        )
    except ValueError as exc:
        parser.error(str(exc))
    frozen_plan_path = HERE / "machineplan.json"
    frozen_plan_hash = sha256(frozen_plan_path)
    recorded_plan_hash = (HERE / "PLAN.sha256").read_text(encoding="utf-8").split()[0]
    if frozen_plan_hash != recorded_plan_hash or args.plan_digest != frozen_plan_hash:
        parser.error("--plan-digest does not match the independently frozen machine plan")
    frozen_plan = json.loads(frozen_plan_path.read_text(encoding="utf-8"))
    selected = next((item for item in frozen_plan["scenarios"] if item["scenario_id"] == args.scenario_id), None)
    if selected is None:
        parser.error("scenario is not one of the three preselected targets in the frozen plan")
    if target_binding.get("scenario_revision") != selected["revision"]:
        parser.error("runtime target binding scenario revision differs from the preselected plan")
    missing_planned = sorted(set(selected["planned_core_cases"]) - set(required_assertions))
    if missing_planned:
        parser.error(f"required assertion manifest omits frozen independent cases: {missing_planned}")
    evidence = args.evidence_dir.resolve()
    if evidence.exists():
        raise SystemExit(f"evidence directory already exists; refusing overwrite: {evidence}")
    evidence.mkdir(parents=True)
    (evidence / "screenshots").mkdir()
    env_evidence = evidence / "run.json"

    run_token = uuid.uuid4().hex
    temp_root = Path(tempfile.gettempdir()) / f"bookmark-product-acceptance-{run_token}"
    data_dir = temp_root / "state"
    network = "none"
    container = "bookmark-product-app-" + run_token[:10]
    host_port = free_port()
    fixture_port = free_port()
    app_url = f"http://127.0.0.1:{host_port}/"
    fixture_base = f"http://127.0.0.1:{fixture_port}"
    fixture = None
    fixture_thread = None
    relay = None
    relay_thread = None
    network_attempted = False
    container_attempted = False
    interrupted = False
    report = {
        "schema": "atlas.independent-ui-acceptance.v1",
        "scenario_id": args.scenario_id,
        "phase": args.phase,
        "target_binding": target_binding,
        "target_digest": hashlib.sha256(json.dumps(target_binding, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "target_binding_file_sha256": sha256(args.target_binding),
        "required_assertions": required_assertions,
        "required_assertions_file_sha256": sha256(args.required_assertions),
        "template_digest": args.template_digest,
        "suite_digest": args.suite_digest,
        "case_basis_digest": args.case_basis_digest,
        "plan_digest": args.plan_digest,
        "plan_file": str(frozen_plan_path),
        "plan_file_sha256": frozen_plan_hash,
        "status": "running",
        "stage": "preflight",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "evidence_dir": str(evidence),
        "runner_command": ["python3", str(Path(__file__).resolve()), *os.sys.argv[1:]],
        "runtime_submission_dir": str(args.bundle.resolve()),
        "delivery_sha256": None,
        "app_root": None,
        "app_source_sha256_before": None,
        "app_source_sha256_after": None,
        "app_image": args.image,
        "app_image_id": None,
        "app_url": app_url,
        "acceptance_adapter": str(args.acceptance_adapter.resolve()),
        "acceptance_adapter_sha256": sha256(args.acceptance_adapter),
        "acceptance_adapter_version": "bookmark-independent-adapter/1.0.0",
        "fixture_base": fixture_base,
        "browser_policy": "Chromium requests permitted only to exact app origin and exact local fixture origin; all other requests aborted",
        "docker_network_mode": "none; no container network interface",
        "network_none": False,
        "container_settings": None,
        "lifecycle": [],
        "stage_events": [],
        "owned_resources": {
            "temporary_root": {"path": str(temp_root), "state": "planned"},
            "fixture_server": {"address": f"127.0.0.1:{fixture_port}", "state": "planned"},
            "fixture_thread": {"name": f"fixture-{run_token[:10]}", "state": "planned"},
            "network": {"name": network, "state": "planned"},
            "container": {"name": container, "state": "planned"},
            "app_relay": {"address": f"127.0.0.1:{host_port}", "state": "planned"},
        },
        "docker_commands": {
            "network_mode": "none",
            "container_cleanup": ["docker", "rm", "--force", container],
            "container_run_plan": {
                "name": container, "image": args.image, "network_mode": "none", "host_publish": None,
                "source_mount": f"{temp_root}/verified-application:/app:readonly",
                "state_mount": f"{data_dir}:/state", "runtime_argv": "<verified delivery-receipt.json runtime.start>",
            },
        },
        "limitations": ["The app container has Docker network mode none; the host relay exposes only loopback and proxies requests to the fixed app container through docker exec."],
        "screenshots_dir": str(evidence / "screenshots"),
    }

    def persist():
        report["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        atomic_write_json(env_evidence, report)

    def stage(name):
        report["stage"] = name
        report["stage_events"].append({"stage": name, "state": "started", "at": time.time()})
        persist()

    def stage_done(name, details=None):
        report["stage_events"].append({"stage": name, "state": "completed", "at": time.time(), "details": details or {}})
        persist()

    # This first durable snapshot precedes creation of local servers or a container.
    persist()
    try:
        stage("temporary_data_setup")
        temp_root.mkdir(mode=0o700)
        data_dir.mkdir()
        data_dir.chmod(0o777)
        report["owned_resources"]["temporary_root"]["state"] = "created"
        stage_done("temporary_data_setup", {"data_dir": str(data_dir)})

        stage("fixture_server_setup")
        fixture = ThreadingHTTPServer(("127.0.0.1", fixture_port), Fixture)
        fixture_thread = threading.Thread(target=fixture.serve_forever, daemon=True)
        fixture_thread.start()
        report["owned_resources"]["fixture_server"]["state"] = "started"
        stage_done("fixture_server_setup", {"fixture_base": fixture_base})

        stage("bundle_verification")
        app_root = temp_root / "verified-application"
        bundle_info = unpack_verified_bundle(args.bundle, app_root, args.archive_sha256)
        verified_application_files = bundle_info["application_inventory"]
        app_digest = validate_runtime_binding(
            target_binding, phase=args.phase, template_digest=args.template_digest,
            suite_digest=args.suite_digest, case_basis_digest=args.case_basis_digest,
            application_files=verified_application_files,
        )
        report["application_digest"] = app_digest
        report["target_binding_verified"] = True
        delivery = bundle_info["delivery"]
        delivery_path = Path(args.bundle).resolve() / "delivery-receipt.json"
        delivery, start_argv, container_port, app_root, data_argument, readiness_path = read_delivery(delivery, bundle_info["app_root"])
        report["bundle_verification"] = bundle_info
        report["delivery_file"] = str(delivery_path)
        report["delivery_sha256"] = bundle_info["receipt_sha256"]
        report["application_archive_sha256"] = bundle_info["archive_sha256"]
        report["delivery_runtime_start_argv"] = start_argv
        report["delivery_runtime_port"] = container_port
        report["delivery_data_dir_argument"] = data_argument
        report["delivery_readiness_path"] = readiness_path
        report["app_root"] = str(app_root)
        report["app_source_sha256_before"] = source_hashes(app_root)
        report["docker_commands"]["container_run_plan"]["runtime_argv"] = start_argv
        report["docker_commands"]["container_run_plan"]["relay_address"] = f"127.0.0.1:{host_port}"
        report["docker_commands"]["container_run_plan"]["relay_target"] = f"{container}:127.0.0.1:{container_port}"
        stage_done("bundle_verification", {
            "archive_sha256": bundle_info["archive_sha256"],
            "delivery_sha256": report["delivery_sha256"],
            "application_digest": app_digest,
        })

        stage("docker_daemon_preflight")
        docker("info", timeout=10)
        stage_done("docker_daemon_preflight")
        stage("local_image_preflight")
        report["app_image_id"] = docker("image", "inspect", "--format", "{{.Id}}", args.image, timeout=10).stdout.strip()
        stage_done("local_image_preflight", {"image_id": report["app_image_id"]})

        stage("docker_container_create")
        container_attempted = True
        report["owned_resources"]["container"]["state"] = "creation-attempted"
        persist()
        run = docker(
            "run", "--detach", "--read-only", "--tmpfs", "/tmp:rw,nosuid,nodev",
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges:true",
            "--memory", "256m", "--cpus", "0.5", "--pids-limit", "64",
            "--user", f"{os.getuid()}:{os.getgid()}", "--workdir", "/app",
            "--mount", f"type=bind,src={app_root},dst=/app,readonly",
            "--mount", f"type=bind,src={data_dir},dst=/state",
            "--network", "none",
            "--env", "PYTHONDONTWRITEBYTECODE=1", "--env", "PYTHONUNBUFFERED=1",
            "--name", container, args.image, *start_argv,
            timeout=30,
        )
        report["container_id"] = run.stdout.strip()
        report["owned_resources"]["container"]["state"] = "created"
        report["container_settings"] = container_meta(container, timeout=10)
        verify_network_none(report["container_settings"])
        report["network_none"] = True
        stage_done("docker_container_create", {"container_id": run.stdout.strip(), "network_mode": "none", "ports_published": False})
        stage("app_relay_setup")
        AppRelay.container, AppRelay.port = container, container_port
        AppRelay.app_origin = app_url.rstrip("/")
        relay = ThreadingHTTPServer(("127.0.0.1", host_port), AppRelay)
        relay.daemon_threads = True
        relay_thread = threading.Thread(target=relay.serve_forever, daemon=True)
        relay_thread.start()
        report["owned_resources"]["app_relay"]["state"] = "started"
        stage_done("app_relay_setup", {"address": f"127.0.0.1:{host_port}", "container": container, "container_port": container_port})
        readiness_url = app_url.rstrip("/") + readiness_path

        stage("application_readiness")
        wait_ready(readiness_url, container, timeout=30)
        report["lifecycle"].append({"event": "initial_start", "container": container_meta(container, timeout=10)})
        stage_done("application_readiness")

        stage("browser_setup")
        home = temp_root / "browser-home"
        home.mkdir()
        # Playwright resolves executablePath from its browser cache. Discover the
        # installed binary with an allowlisted environment using the user's HOME,
        # then launch it with a separate temporary HOME so Chromium cannot see
        # the user's normal profile/configuration.
        discovery_env = {
            "PATH": os.environ["PATH"],
            "HOME": str(Path.home()),
            "TMPDIR": str(temp_root),
        }
        module_result = subprocess.run(
            ["node", "-e", "const {chromium}=require(process.argv[1]);process.stdout.write(chromium.executablePath())", str(PLAYWRIGHT)],
            cwd=ROOT, env=discovery_env, check=True, text=True, capture_output=True, timeout=15,
        )
        isolated_browser_env = {"PATH": os.environ["PATH"], "HOME": str(home), "TMPDIR": str(temp_root)}
        phase_env = {
            **isolated_browser_env,
            "PLAYWRIGHT_MODULE": str(PLAYWRIGHT),
            "PLAYWRIGHT_EXECUTABLE": module_result.stdout,
            "APP_URL": app_url,
            "FIXTURE_BASE": fixture_base,
            "EVIDENCE_DIR": str(evidence),
            "ACCEPTANCE_ADAPTER": str(args.acceptance_adapter.resolve()),
            "SCENARIO_ID": args.scenario_id,
            "REQUIRED_ASSERTIONS_JSON": json.dumps(required_assertions),
        }
        restart_assertions = {case_id for case_id in required_assertions
                              if "restart" in case_id.lower()}
        report["browser"] = {"engine": "Chromium", "executable": module_result.stdout,
                             "executable_discovery": "allowlisted PATH/HOME/TMPDIR; HOME used only to resolve Playwright's installed browser binary",
                             "environment": "Chromium launch uses temporary HOME and allowlisted PATH/HOME/TMPDIR; no inherited credential variables"}
        stage_done("browser_setup", {"executable": module_result.stdout})

        def run_phase(phase, run_id=None):
            stage(f"ui_{phase}")
            phase_env["PHASE"] = phase
            phase_required = (sorted(set(required_assertions) - restart_assertions)
                              if phase == "initial" else required_assertions)
            phase_env["REQUIRED_ASSERTIONS_JSON"] = json.dumps(phase_required)
            if run_id:
                phase_env["RUN_ID"] = run_id
            try:
                proc = subprocess.run(
                    ["node", str(HERE / "independent_ui_acceptance.cjs")], cwd=ROOT,
                    env=phase_env, text=True, capture_output=True, timeout=120,
                )
            except subprocess.TimeoutExpired as exc:
                out = exc.stdout or ""
                err = exc.stderr or ""
                if isinstance(out, bytes):
                    out = out.decode("utf-8", "replace")
                if isinstance(err, bytes):
                    err = err.decode("utf-8", "replace")
                atomic_write_text(evidence / f"{phase}.stdout.json", out)
                atomic_write_text(evidence / f"{phase}.stderr.log", err)
                report["phase_timeout"] = {"phase": phase, "seconds": exc.timeout, "cmd": exc.cmd}
                persist()
                raise
            atomic_write_text(evidence / f"{phase}.stdout.json", proc.stdout)
            atomic_write_text(evidence / f"{phase}.stderr.log", proc.stderr)
            persist()
            if proc.returncode:
                raise RuntimeError(f"Chromium UI phase {phase} failed (exit {proc.returncode}): {proc.stderr[-4000:]}")
            parsed = json.loads(proc.stdout)
            assertions = parsed.get("assertions") if isinstance(parsed, dict) else None
            if not isinstance(assertions, list):
                raise RuntimeError("independent browser adapter must emit an assertions array")
            missing, failed = validate_phase_assertions(assertions, phase_required, phase)
            if missing or failed:
                raise RuntimeError(f"mandatory assertions missing={missing}, failed={failed}")
            report[f"{phase.replace('-', '_')}_phase"] = parsed
            stage_done(f"ui_{phase}")
            return parsed

        run_id = "bm-" + uuid.uuid4().hex[:12]
        initial_result = run_phase("initial", run_id)
        initial_metadata = initial_result.get("adapter_metadata") if isinstance(initial_result, dict) else None
        if not isinstance(initial_metadata, dict):
            raise RuntimeError("initial browser phase omitted adapter metadata required for post-restart identity checks")
        phase_env["INITIAL_METADATA_JSON"] = json.dumps(initial_metadata)
        stage("pre_restart_snapshot")
        before_restart = container_meta(container, timeout=10)
        report["lifecycle"].append({"event": "before_restart", "container": before_restart})
        stage_done("pre_restart_snapshot", {"started_at": before_restart["state"]["StartedAt"]})

        stage("docker_restart")
        restart_output = docker("restart", "--time", "5", container, timeout=30).stdout.strip()
        stage_done("docker_restart", {"stdout": restart_output})
        stage("post_restart_readiness")
        wait_ready(readiness_url, container, timeout=30)
        after_restart = container_meta(container, timeout=10)
        report["lifecycle"].append({"event": "docker_restart", "command": ["docker", "restart", "--time", "5", container], "stdout": restart_output})
        report["lifecycle"].append({"event": "after_restart", "container": after_restart})
        if before_restart.get("id") != after_restart.get("id"):
            raise RuntimeError("Docker restart changed container ID; same-container restart is unproven")
        if (before_restart.get("state", {}).get("Running") is not True
                or after_restart.get("state", {}).get("Running") is not True):
            raise RuntimeError("same Docker container was not running both before and after restart")
        if before_restart["state"]["StartedAt"] == after_restart["state"]["StartedAt"]:
            raise RuntimeError("Docker container StartedAt did not change; real process restart is unproven")
        verify_network_none(after_restart)
        stage_done("post_restart_readiness", {"started_at": after_restart["state"]["StartedAt"]})

        phase_env["RESTART_LIFECYCLE_CONFIRMED"] = "1"
        run_phase("after-restart")
        missing_combined = validate_combined_assertions(
            [("initial", report.get("initial_phase", {})),
             ("after-restart", report.get("after_restart_phase", {}))],
            required_assertions,
        )
        if missing_combined:
            raise RuntimeError(f"frozen cases did not pass across required phases: {missing_combined}")
        stage("post_acceptance_source_integrity")
        report["app_source_sha256_after"] = source_hashes(app_root)
        if report["app_source_sha256_after"] != report["app_source_sha256_before"]:
            raise RuntimeError("application source changed during acceptance")
        stage_done("post_acceptance_source_integrity")
        report["status"] = "passed"
        adapter_after = sha256(args.acceptance_adapter)
        if adapter_after != report["acceptance_adapter_sha256"]:
            raise RuntimeError("independent acceptance adapter changed during execution")
        report["mandatory_assertions_passed"] = required_assertions
        report["phase_assertion_contract"] = {
            "initial_required": sorted(set(required_assertions) - restart_assertions),
            "after_restart_required": required_assertions,
            "restart_assertions_must_pass_after_restart": sorted(restart_assertions),
            "combined_missing": missing_combined,
        }
        persist()
    except KeyboardInterrupt as exc:
        interrupted = True
        report["status"] = "interrupted"
        report["failure_kind"] = "operator_interruption"
        report["error"] = repr(exc)
        report["interrupted_at_stage"] = report.get("stage")
        report["primary_failure"] = {
            "stage": report["interrupted_at_stage"],
            "status": "interrupted",
            "failure_kind": "operator_interruption",
            "error": repr(exc),
        }
        try:
            atomic_write_json(evidence / "interruption.json", {
                "status": "interrupted",
                "stage": report["interrupted_at_stage"],
                "error": repr(exc),
                "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "run_json": str(env_evidence),
            })
        except BaseException as write_exc:
            report["interruption_record_error"] = repr(write_exc)
        persist()
    except Exception as exc:
        report["failure_stage"] = report.get("stage")
        report["status"], report["failure_kind"] = classify_failure(report.get("stage", "unknown"), exc)
        report["error"] = repr(exc)
        report["primary_failure"] = {
            "stage": report["failure_stage"],
            "status": report["status"],
            "failure_kind": report["failure_kind"],
            "error": report["error"],
        }
        if isinstance(exc, subprocess.CalledProcessError):
            report["command"] = exc.cmd
            report["stdout"] = exc.stdout
            report["stderr"] = exc.stderr
            report["primary_failure"].update({"command": exc.cmd, "stdout": exc.stdout, "stderr": exc.stderr})
        if isinstance(exc, subprocess.TimeoutExpired):
            report["command"] = exc.cmd
            report["timeout_seconds"] = exc.timeout
            report["primary_failure"].update({"command": exc.cmd, "timeout_seconds": exc.timeout})
        persist()
        if container_attempted:
            try:
                report["failure_container_logs"] = docker("logs", "--tail", "200", container, check=False, timeout=10).stdout
                persist()
            except BaseException as log_exc:
                report["failure_container_logs_error"] = repr(log_exc)
                persist()
    finally:
        report["stage"] = "cleanup"
        try:
            persist()
        except BaseException as persist_exc:
            report.setdefault("cleanup_journal_errors", []).append({"stage": "cleanup:started", "error": repr(persist_exc)})
            if isinstance(persist_exc, KeyboardInterrupt):
                report.setdefault("cleanup_interruptions", []).append({
                    "stage": "cleanup:journal:started", "error": repr(persist_exc),
                    "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                })
                try:
                    atomic_write_json(evidence / "interruption.json", {
                        "status": "interrupted_during_cleanup",
                        **report["cleanup_interruptions"][-1],
                        "run_json": str(env_evidence),
                    })
                except BaseException as write_exc:
                    report["interruption_record_error"] = repr(write_exc)
        cleanup_resources(
            report, persist, container=container, network=network, temp_root=temp_root,
            container_attempted=container_attempted, network_attempted=network_attempted,
            fixture=fixture, fixture_thread=fixture_thread, relay=relay, relay_thread=relay_thread,
        )
        report["completed_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        finalize_cleanup_outcome(report, persist, evidence)
    if report.get("status") == "passed":
        phase_assertions = []
        for phase in ("initial_phase", "after_restart_phase"):
            phase_result = report.get(phase)
            if not isinstance(phase_result, dict):
                report.update(status="failed", failure_kind="product_or_acceptance_failure",
                              error=f"missing required browser phase result: {phase}")
                break
            phase_assertions.extend({"phase": phase, **item} for item in phase_result.get("assertions", []))
        if report.get("status") == "passed":
            proof = {
                "schema": "atlas.phase-evidence.v1",
                "requirement_id": "independent-core-journey",
                "target_digest": atlas_digest(target_binding),
                "outcome": "passed",
                "executor": {"kind": "independent_executor", "name": "atlas-independent-acceptance-v1", "version": "1.0.0"},
                "scenario_id": args.scenario_id,
                "scenario_revision": target_binding.get("scenario_revision"),
                "phase": args.phase,
                "application_digest": report.get("application_digest"),
                "plan_digest": args.plan_digest,
                "template_digest": args.template_digest,
                "suite_digest": args.suite_digest,
                "case_basis_digest": args.case_basis_digest,
                "actual_assertions": phase_assertions,
                "environment": {
                    "profile": "python-web", "os": os.sys.platform,
                    "docker_image": args.image, "docker_image_id": report.get("app_image_id"),
                    "container_settings": report.get("container_settings"),
                    "browser": report.get("browser"), "app_url_origin": urlsplit(report["app_url"]).netloc,
                    "fixture_origin": urlsplit(report["fixture_base"]).netloc,
                    "docker_restart_observed": len(report.get("lifecycle", [])) >= 3,
                    "network_mode_none": report.get("network_none") is True,
                    "app_relay": report.get("cleanup", {}).get("app_relay_stopped"),
                    "source_unchanged": report.get("app_source_sha256_before") == report.get("app_source_sha256_after"),
                },
                "logs": [
                    {"path": f"{phase}.stdout.json", "sha256": sha256(evidence / f"{phase}.stdout.json")}
                    for phase in ("initial", "after-restart")
                ] + [
                    {"path": f"{phase}.stderr.log", "sha256": sha256(evidence / f"{phase}.stderr.log")}
                    for phase in ("initial", "after-restart")
                ],
            }
            if sha256(args.target_binding) != report["target_binding_file_sha256"]:
                report.update(status="failed", failure_kind="acceptance_contract_changed",
                              error="target binding file changed during independent acceptance")
            elif sha256(args.required_assertions) != report["required_assertions_file_sha256"]:
                report.update(status="failed", failure_kind="acceptance_contract_changed",
                              error="required assertion manifest changed during independent acceptance")
            elif sha256(args.acceptance_adapter) != report["acceptance_adapter_sha256"]:
                report.update(status="failed", failure_kind="acceptance_contract_changed",
                              error="independent adapter changed during independent acceptance")
            elif sha256(frozen_plan_path) != report["plan_file_sha256"]:
                report.update(status="failed", failure_kind="acceptance_contract_changed",
                              error="frozen independent plan changed during acceptance")
            if report.get("status") != "passed":
                persist()
                proof = None
            if proof is None:
                pass
            else:
                atomic_write_json(evidence / "proof.json", proof)
                report["phase_evidence"] = {"path": "proof.json", "sha256": sha256(evidence / "proof.json")}
                persist()
        else:
            persist()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] == "interrupted":
        raise SystemExit(130)
    if report["status"] != "passed":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
