"""Run the unmodified formal export's probe against disposable owned processes."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
from urllib.request import urlopen
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKAGE = (
    ROOT.parents[1]
    / "docs/template-factory/assisted-batch-2026-10-21/home-inventory/atlas-development-package.zip"
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "source": str(args.package),
        "scope": "real HTTP and owned process restart; browser evidence separate",
        "cases": [],
    }
    with (
        zipfile.ZipFile(args.package) as package,
        tempfile.TemporaryDirectory(prefix="inventory-frozen-") as workspace,
    ):
        work = Path(workspace)
        probe_bytes = package.read("blueprint/acceptance/probe.py")
        contract = json.loads(package.read("ACCEPTANCE_CONTRACT.json"))
        assert (
            hashlib.sha256(probe_bytes).hexdigest()
            == contract["suite_sha256"]["acceptance/probe.py"]
        )
        probe = work / "probe.py"
        probe.write_bytes(probe_bytes)
        for case in ["A01", "A02", "A03", "A04"]:
            command = [sys.executable, str(probe), "--case", case]
            process = None
            if case == "A04":
                command += ["--app-root", str(ROOT)]
            else:
                with socket.socket() as sock:
                    sock.bind(("127.0.0.1", 0))
                    port = sock.getsockname()[1]
                base = f"http://127.0.0.1:{port}"
                process = subprocess.Popen(
                    [
                        sys.executable,
                        str(ROOT / "app/serve.py"),
                        "--port",
                        str(port),
                        "--data-dir",
                        str(work / case),
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                for _ in range(100):
                    try:
                        with urlopen(base + "/api/health", timeout=1):
                            break
                    except OSError:
                        time.sleep(0.05)
                command += ["--base-url", base]
            try:
                result = subprocess.run(
                    command, capture_output=True, text=True, timeout=45
                )
                entry = {
                    "case": case,
                    "command": command,
                    "exit_code": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "status": "passed" if result.returncode == 0 else "failed",
                }
                report["cases"].append(entry)
                print(result.stdout or result.stderr, end="", flush=True)
            finally:
                if process is not None:
                    process.terminate()
                    process.wait(timeout=10)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return 0 if all(r["status"] == "passed" for r in report["cases"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
