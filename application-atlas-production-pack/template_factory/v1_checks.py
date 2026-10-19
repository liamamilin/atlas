"""Execute the complete configured G1 checks; never call a model or grant G1.

The resulting records are consumed by the host-only milestone assessor together
with the separately executed real sample. CI time is not production wall time.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

from atlas_runtime import atomic_json
from privacy import redact_text
from .v1_batches import G1_REQUIRED_CHECKS, _g1_source_digest


def observed_counts(name, output):
    """Read actual runner output, retaining optional skips rather than hiding them."""
    if name in {"backend_tests", "docker_integration"}:
        matches = re.findall(r"Ran (\d+) tests? in", output)
        tests = int(matches[-1]) if matches else None
        skips = re.findall(r"OK \(skipped=(\d+)\)", output)
        skipped = int(skips[-1]) if skips else 0
        if name == "docker_integration":
            for line in reversed(output.splitlines()):
                try:
                    value = json.loads(line)
                except ValueError:
                    continue
                if isinstance(value, dict) and "tests_run" in value:
                    return value.get("tests_run"), value.get("skipped")
        return tests, skipped
    if name == "web_unit":
        tests = re.findall(r"# tests (\d+)", output)
        skips = re.findall(r"# skipped (\d+)", output)
        return (int(tests[-1]) if tests else None, int(skips[-1]) if skips else 0)
    if name in {"default_e2e", "factory_e2e"}:
        passed = re.findall(r"(\d+) passed", output)
        skipped = re.findall(r"(\d+) skipped", output)
        return (int(passed[-1]) if passed else None, int(skipped[-1]) if skipped else 0)
    return None, 0


def run_checks(workspace, output_directory, progress=print):
    workspace, out = Path(workspace).resolve(), Path(output_directory).resolve()
    out.relative_to(workspace)
    out.mkdir(parents=True, exist_ok=True)
    source_before = _g1_source_digest(workspace)
    checks = {}
    for name, requirement in G1_REQUIRED_CHECKS.items():
        progress("G1 check: " + name, flush=True)
        argv = list(requirement["argv"])
        launched = [sys.executable if argv[0] == "python" else argv[0], *argv[1:]]
        env = {**os.environ, **requirement.get("env", {})}
        # Optional Docker tests stay optional in normal discovery; the strict
        # Docker gate is a distinct executed command with zero allowed skips.
        if name == "backend_tests":
            env.pop("ATLAS_RUN_DOCKER_INTEGRATION", None)
        started = time.time()
        try:
            result = subprocess.run(launched, cwd=workspace / requirement["cwd"], env=env,
                                    stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, timeout=900, text=True)
            output, exit_code = result.stdout, result.returncode
        except (OSError, subprocess.TimeoutExpired) as error:
            output = (getattr(error, "stdout", "") or "")
            if isinstance(output, bytes):
                output = output.decode(errors="replace")
            output += "\nCHECK EXECUTION FAILED: " + str(error)
            exit_code = 124 if isinstance(error, subprocess.TimeoutExpired) else 127
        raw = redact_text(output).encode()
        log_path = out / (name + ".txt")
        log_path.write_bytes(raw)
        count, skipped = observed_counts(name, output)
        record = {"status": "passed" if exit_code == 0 else "failed", "exit_code": exit_code,
                  "argv": argv, "cwd": requirement["cwd"], "env": requirement.get("env", {}),
                  "started_epoch": started, "duration_seconds": round(time.time() - started, 3),
                  "tests_run": count, "skipped": skipped,
                  "log_path": str(log_path.relative_to(workspace)),
                  "log_sha256": hashlib.sha256(raw).hexdigest()}
        checks[name] = record
        atomic_json(out / "checks.json", {"schema": "atlas.g1-check-run.v1", "source_tree_sha256": source_before,
                                          "checks": checks, "complete": False})
    source_after = _g1_source_digest(workspace)
    report = {"schema": "atlas.g1-check-run.v1", "source_tree_sha256": source_before,
              "source_tree_after_sha256": source_after, "source_changed_during_checks": source_before != source_after,
              "checks": checks, "complete": True,
              "passed": source_before == source_after and all(x["exit_code"] == 0 for x in checks.values())}
    atomic_json(out / "checks.json", report)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description="Execute required G1 repository checks; no models or milestone override")
    parser.add_argument("--output", type=Path, required=True, help="Evidence directory inside the repository")
    args = parser.parse_args(argv)
    workspace = Path(__file__).resolve().parents[2]
    result = run_checks(workspace, args.output)
    print(json.dumps({"passed": result["passed"], "source_changed_during_checks": result["source_changed_during_checks"]}))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
