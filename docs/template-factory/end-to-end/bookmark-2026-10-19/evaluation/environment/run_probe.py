"""Run a synthetic Docker bridge/loopback/Chromium probe with cleanup."""
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import tempfile
import time
import uuid

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
IMAGE = "python:3.12-slim"
NETWORK = "bookmark-probe-net-" + uuid.uuid4().hex[:10]
CONTAINER = "bookmark-probe-app-" + uuid.uuid4().hex[:10]
RESULT = HERE / "result.json"
PLAYWRIGHT = ROOT / "atlas-web/node_modules/playwright"


def docker(*args, check=True):
    return subprocess.run(["docker", *args], check=check, text=True, capture_output=True)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def free_local_port():
    with socket.socket() as port_socket:
        port_socket.bind(("127.0.0.1", 0))
        return port_socket.getsockname()[1]


def main():
    temp_root = Path(tempfile.mkdtemp(prefix="bookmark-acceptance-probe-"))
    data_dir = temp_root / "data"
    data_dir.mkdir()
    data_dir.chmod(0o777)
    app_port, fixture_port = free_local_port(), free_local_port()
    app_url = f"http://127.0.0.1:{app_port}/"
    fixture_url = f"http://127.0.0.1:{fixture_port}/original"
    result = {
        "probe": "synthetic stdlib HTTP server only",
        "application_source_used": False,
        "image": IMAGE,
        "network_mode": "custom user-defined bridge; not host network",
        "docker_network_internal": False,
        "bridge_egress_enforced": False,
        "published_addresses": [f"127.0.0.1:{app_port}", f"127.0.0.1:{fixture_port}"],
        "browser_request_policy": "Chromium context permits only this app origin and local fixture origin; other requests aborted",
        "network_none": False,
        "source_mount_read_only": True,
        "root_filesystem_read_only": True,
        "dedicated_data_directory": str(data_dir),
        "credentials_passed_to_container": False,
        "container_socket_mounted": False,
        "container_limits": {"memory": "256m", "cpus": "0.5", "pids": 64, "capabilities_dropped": "ALL", "no_new_privileges": True},
        "browser": "Playwright Chromium, independent host process with isolated temporary HOME/TMPDIR",
        "cleanup": "container and network removal attempted in finally",
    }
    try:
        result["probe_source_sha256"] = {
            name: sha256(HERE / name) for name in ("http_probe.py", "chromium_probe.cjs", "run_probe.py")
        }
        result["image_id"] = docker("image", "inspect", "--format", "{{.Id}}", IMAGE).stdout.strip()
        docker("network", "create", NETWORK)
        network_meta = json.loads(docker("network", "inspect", NETWORK).stdout)[0]
        result["docker_network_internal_actual"] = network_meta["Internal"]
        docker(
            "run", "--detach", "--read-only", "--tmpfs", "/tmp:rw,nosuid,nodev",
            "--cap-drop", "ALL", "--security-opt", "no-new-privileges:true",
            "--memory", "256m", "--cpus", "0.5", "--pids-limit", "64",
            "--user", f"{os.getuid()}:{os.getgid()}",
            "--mount", f"type=bind,src={HERE / 'http_probe.py'},dst=/probe.py,readonly",
            "--mount", f"type=bind,src={data_dir},dst=/data",
            "--network", NETWORK,
            "--publish", f"127.0.0.1:{app_port}:8000",
            "--publish", f"127.0.0.1:{fixture_port}:8001",
            "--env", f"FIXTURE_URL={fixture_url}",
            "--name", CONTAINER, IMAGE, "python", "/probe.py",
        )
        inspected = json.loads(docker("inspect", CONTAINER).stdout)[0]
        result["container_id"] = inspected["Id"]
        result["container_configuration"] = {
            "image": inspected["Config"]["Image"],
            "command": inspected["Config"]["Cmd"],
            "user": inspected["Config"]["User"],
            "network_mode": inspected["HostConfig"]["NetworkMode"],
            "port_bindings": inspected["HostConfig"]["PortBindings"],
            "effective_published_ports": inspected["NetworkSettings"]["Ports"],
            "container_running": inspected["State"]["Running"],
            "readonly_rootfs": inspected["HostConfig"]["ReadonlyRootfs"],
            "cap_drop": inspected["HostConfig"]["CapDrop"],
            "security_options": inspected["HostConfig"]["SecurityOpt"],
            "memory_bytes": inspected["HostConfig"]["Memory"],
            "nano_cpus": inspected["HostConfig"]["NanoCpus"],
            "pids_limit": inspected["HostConfig"]["PidsLimit"],
            "mounts": [
                {key: mount[key] for key in ("Type", "Source", "Destination", "RW")}
                for mount in inspected["Mounts"]
            ],
            "environment_variable_names": [
                entry.split("=", 1)[0] for entry in inspected["Config"]["Env"]
            ],
        }
        for published in inspected["NetworkSettings"]["Ports"].values():
            if not published:
                raise RuntimeError("Docker did not register an expected published host port")
        module_result = subprocess.run(
            ["node", "-e", "const {chromium}=require(process.argv[1]);process.stdout.write(chromium.executablePath())", str(PLAYWRIGHT)],
            cwd=ROOT, check=True, capture_output=True, text=True,
        )
        executable = module_result.stdout
        browser_env = {
            "PATH": os.environ["PATH"],
            "HOME": str(temp_root / "home"),
            "TMPDIR": str(temp_root),
            "PLAYWRIGHT_MODULE": str(PLAYWRIGHT),
            "PLAYWRIGHT_EXECUTABLE": executable,
            "APP_URL": app_url,
            "FIXTURE_URL": fixture_url,
        }
        Path(browser_env["HOME"]).mkdir()
        result["chromium_executable"] = executable
        browser = subprocess.run(
            ["node", str(HERE / "chromium_probe.cjs")], cwd=ROOT,
            env=browser_env, check=True, text=True, capture_output=True, timeout=30,
        )
        result["chromium_result"] = json.loads(browser.stdout)
        result["chromium_stderr"] = browser.stderr
        result["persisted_marker"] = (data_dir / "probe-marker").read_text()
        result["status"] = "pass"
    except Exception as exc:
        result["error"] = repr(exc)
        result["status"] = "blocked" if "published host port" in str(exc) else "fail"
        if isinstance(exc, subprocess.CalledProcessError):
            result["command"] = exc.cmd
            result["stdout"] = exc.stdout
            result["stderr"] = exc.stderr
    finally:
        docker("rm", "--force", CONTAINER, check=False)
        docker("network", "rm", NETWORK, check=False)
        result["cleanup"] = "owned container and network removal attempted in finally; temporary directory retained"
        result["temporary_root"] = str(temp_root)
        RESULT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] == "fail":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
