"""Strict runner for the required, opt-in Docker integration suite.

The regular unittest discovery keeps Docker tests optional. CI calls this
runner so missing infrastructure, a missing image, or a skipped test fails the
required gate with a useful external-block reason.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def blocked(reason: str) -> int:
    print(json.dumps({"status": "blocked_external", "reason": reason}))
    return 2


def main() -> int:
    if os.environ.get("ATLAS_RUN_DOCKER_INTEGRATION") != "1":
        return blocked("ATLAS_RUN_DOCKER_INTEGRATION must be set to 1")

    docker = shutil.which("docker")
    if not docker:
        return blocked("Docker CLI is unavailable")
    daemon = subprocess.run(
        [docker, "info", "--format", "{{.ServerVersion}}"],
        capture_output=True, text=True, timeout=15,
    )
    if daemon.returncode:
        return blocked("Docker daemon unavailable: " + daemon.stderr.strip()[-500:])

    from template_factory.runtime import IMAGES

    for image in sorted(set(IMAGES.values())):
        inspected = subprocess.run(
            [docker, "image", "inspect", image],
            capture_output=True, text=True, timeout=15,
        )
        if inspected.returncode:
            return blocked("required local image missing: " + image)

    sys.path.insert(0, str(ROOT / "tests"))
    import test_blueprint_runtime_docker
    import test_blueprint_runtime_jobs

    suite = unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromModule(test_blueprint_runtime_docker),
        unittest.defaultTestLoader.loadTestsFromModule(test_blueprint_runtime_jobs),
    ])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    summary = {
        "status": "passed" if result.wasSuccessful() and not result.skipped else "failed",
        "tests_run": result.testsRun,
        "skipped": len(result.skipped),
        "failures": len(result.failures),
        "errors": len(result.errors),
        "daemon_version": daemon.stdout.strip(),
        "images": sorted(set(IMAGES.values())),
    }
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
