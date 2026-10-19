"""Recover an interrupted repair without overwriting it or inventing CLI success."""

import argparse
import json
import shutil

import repair
from develop import HERE, MODEL, hashes, save


def prepare():
    stage = repair.STAGE
    assert not stage.exists()
    previous = HERE / "repair/scenario-review"
    stage.mkdir(parents=True)
    shutil.copytree(previous / "app", stage / "app")
    shutil.copytree(previous / "source", stage / "source")
    data = json.loads((previous / "input.json").read_text())
    data["recovery"] = {
        "previous_status": "interrupted; no CLI exit/final response captured",
        "task": "Inspect the partial repair already in app/, complete only necessary fixes and give a reliable final delivery manifest. Do not claim tests ran.",
        "seed_source_sha256": hashes(stage / "app"),
    }
    save(stage / "input.json", data)
    (stage / "task-prompt.txt").write_text(repair.PROMPT)
    save(HERE / "repair-recovery-input-freeze.json", {
        "model": MODEL, "reasoning_effort": "high", "inputs_sha256": hashes(stage),
        "predecessor_status": "interrupted", "runtime_status": "not_run",
    })
    print("Prepared recovery from preserved partial repair; no provider call", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run"])
    args = parser.parse_args()
    repair.STAGE = HERE / "repair-recovery/scenario-review"
    (prepare if args.action == "prepare" else repair.run)()
