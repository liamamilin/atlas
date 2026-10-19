"""Posthoc synthetic oversized-form diagnostic, separate from frozen core checks."""

import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess

from runtime_test import HERE, NODE, Supervisor, minimal_env, static_inventory, write_json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--source-reviewed", action="store_true")
    args = parser.parse_args()
    assert args.source_reviewed
    app, evidence = args.app.resolve(), args.evidence.resolve()
    inventory = static_inventory(app)
    assert not inventory["command_execution_flags"] and not inventory["non_stdlib_imports"]
    evidence.mkdir(parents=True, exist_ok=False)
    write_json(evidence / "static-inventory.json", inventory)
    write_json(evidence / "scope.json", {
        "posthoc_exploration": True,
        "trigger": "Source inspection found request body clamped to 1000000 bytes before parsing. Verify explicit rejection and no partial accepted write with synthetic local-only data.",
        "not_a_new_core_requirement": True,
        "source_sha256": {p.relative_to(app).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in app.rglob("*") if p.is_file() and "__pycache__" not in p.parts},
    })
    for source in [Path(__file__), HERE / "body-probe.mjs"]:
        shutil.copyfile(source, evidence / source.name)
    supervisor = Supervisor(app, evidence)
    try:
        supervisor.start()
        with (evidence / "browser-run.log").open("wb") as log:
            code = subprocess.run([
                str(NODE), str(HERE / "body-probe.mjs"), "--base-url", supervisor.base_url,
                "--evidence", str(evidence),
            ], env=minimal_env(), stdout=log, stderr=subprocess.STDOUT, timeout=120).returncode
        assert code == 0, "Diagnostic failed; inspect browser-run.log"
    finally:
        supervisor.stop()
        write_json(evidence / "processes.json", {"epochs": supervisor.epochs})


if __name__ == "__main__":
    main()
