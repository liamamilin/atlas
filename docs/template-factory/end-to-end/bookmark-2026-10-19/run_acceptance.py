"""Submit this pilot's frozen app to the real independent verification queue."""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from atlas_runtime import atomic_json
from template_factory.api import get_store
from template_factory.pipeline import Pipeline
from template_factory.worker import execute


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--delivery", type=Path, required=True)
    parser.add_argument("--label", required=True, choices=["initial", "repair-1", "repair-2"])
    args = parser.parse_args()
    target = HERE / "runtime" / args.label
    target.mkdir(parents=True, exist_ok=True)
    run = json.loads((HERE / "run.json").read_text())
    store = get_store()
    data = (args.delivery / "application.zip").read_bytes()
    archive_hash = hashlib.sha256(data).hexdigest()
    if (target / "submission.json").exists():
        submission = json.loads((target / "submission.json").read_text())
        if submission["archive_sha256"] != archive_hash:
            raise SystemExit("Do not change source behind an acceptance label")
        job_id = submission["job_id"]
    else:
        batch = store.create_acceptance(run["artifact_id"], {
            "method": "blueprint-runtime", "expected_digest": run["artifact_digest"],
            "phase": "P0", "execution_confirmed": True, "timeout": 600,
            "language": "zh", "source_archive_base64": base64.b64encode(data).decode(),
        })
        job_id = batch["jobs"][0]["id"]
        atomic_json(target / "submission.json", {"job_id": job_id, "batch_id": batch["id"],
                                                  "archive_sha256": archive_hash,
                                                  "artifact_digest": run["artifact_digest"], "phase": "P0"})
        run["additional_job_ids"] = list(dict.fromkeys([*run.get("additional_job_ids", []), job_id]))
        atomic_json(HERE / "run.json", run)
    job = store.job(job_id)
    if job["state"] == "queued":
        with store.connect() as con:
            first = con.execute("SELECT id FROM job WHERE state='queued' AND kind IN ('harness-review','runtime-verification','scenario-review','cognitive-review','blueprint-runtime') ORDER BY created_at LIMIT 1").fetchone()
            if not first or first["id"] != job_id:
                raise SystemExit("Refusing to claim an unrelated acceptance task")
        job = store.claim("bookmark-independent-runtime", "verification")
        if not job or job["id"] != job_id:
            raise SystemExit("Unexpected claim; stop")
        execute(store, job, Pipeline(store))
    reports = [r for r in store.acceptances(run["artifact_id"]) if r["job_id"] == job_id]
    state = store.job(job_id)
    atomic_json(target / "job.json", {k: state[k] for k in ("id", "state", "stage", "error", "attempt")})
    if reports:
        atomic_json(target / "report.json", reports[0])
    print(json.dumps({"job_id": job_id, "state": state["state"], "error": state["error"],
                      "outcome": reports[0]["outcome"] if reports else None,
                      "cases": len(reports[0].get("case_results", [])) if reports else 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
