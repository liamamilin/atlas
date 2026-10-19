"""Continue the authorized pilot across gates; stop on any non-passing stage."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from atlas_runtime import atomic_json
from template_factory.api import get_store


def state(stage, **fields):
    value = {"stage": stage, **fields}
    atomic_json(HERE / "flow-state.json", value)
    print(json.dumps(value, ensure_ascii=False), flush=True)


def command(label, argv):
    state(label, state="running")
    with (HERE / (label + ".log")).open("ab") as log:
        result = subprocess.run([sys.executable, *argv], cwd=ROOT,
                                stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT)
    if result.returncode:
        state(label, state="stopped", exit_code=result.returncode, log=label + ".log")
        raise SystemExit(result.returncode)


def main():
    store = get_store()
    run = json.loads((HERE / "run.json").read_text())
    job_id = run["production_job_id"]
    last = None
    while True:
        job = store.job(job_id)
        if job["state"] not in {"queued", "running"}:
            break
        if job["stage"] != last:
            state("template-production", state=job["state"], job_id=job_id, detail=job["stage"])
            last = job["stage"]
        time.sleep(10)
    if job["state"] != "completed":
        state("template-production", state="stopped", job_id=job_id, detail=job["state"], error=job["error"])
        return
    artifact = next(a for a in store.artifacts() if a["job_id"] == job_id)
    reviews = [r for r in artifact["acceptances"] if r["method"] == "cognitive-review"]
    if not reviews:
        command("cognition-review", [str(HERE / "run_flow.py"), "review"])
    artifact = next(a for a in store.artifacts() if a["job_id"] == job_id)
    reviews = [r for r in artifact["acceptances"] if r["method"] == "cognitive-review"]
    if not reviews or reviews[0]["outcome"] != "passed":
        state("cognition-review", state="stopped", artifact_id=artifact["id"],
              outcome=reviews[0]["outcome"] if reviews else None,
              reason="Inspect independent findings before paying to develop an application.")
        return
    command("development-export", [str(HERE / "run_flow.py"), "export"])
    atomic_json(HERE / "driver-source-sha256.json", {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in ("run_flow.py", "develop_app.py", "run_acceptance.py", "continue_flow.py")
    })
    command("application-development", [str(HERE / "develop_app.py"), "--package", str(HERE / "development-package.zip"), "--phase", "P0"])
    command("application-runtime", [str(HERE / "run_acceptance.py"), "--delivery", str(HERE / "development/initial"), "--label", "initial"])
    report = HERE / "runtime/initial/report.json"
    outcome = json.loads(report.read_text()).get("outcome") if report.exists() else None
    state("independent-browser-pending", state="awaiting_independent_agent", runtime_outcome=outcome,
          note="Runtime suite and browser/restart checks are separate evidence. No publication or overall product pass claimed.")


if __name__ == "__main__":
    main()
