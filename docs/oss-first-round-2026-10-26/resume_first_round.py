"""Run the existing finite job using current code, without restarting the API.

The normal SQLite/flock checkpoint protocol excludes the API supervisor while
this worker owns the job. No server, service, new job or extra scope is created.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from atlas_runtime import atomic_json  # noqa: E402
from oss_batch import BatchJobs  # noqa: E402
from oss_catalog import CatalogError, CatalogStore, now  # noqa: E402

JOB = "batch_4812ef3db57543c3acc1871b8ea5ba6e"
RECEIPT = PACK / "atlas/oss-discovery/first-round-worker.json"


class ExistingJob(BatchJobs):
    def launch(self, job, lock, background):
        assert job["id"] == JOB and not background
        atomic_json(RECEIPT, {"job_id": JOB, "pid": os.getpid(), "state": "owns_job_lock",
                             "started_at": now(), "service_restarted": False,
                             "first_round_limit": 60, "model_concurrency": 4,
                             "priority_sha256": hashlib.sha256((PACK / "oss_priority.py").read_bytes()).hexdigest()})
        return super().launch(job, lock, background)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accept-verified-pilot", type=Path)
    args = parser.parse_args()
    assert os.environ.get("ATLAS_FACTORY_DISABLE_WORKER") == "1"
    assert os.environ.get("ATLAS_OSS_MODEL_CONCURRENCY") == "4"
    store = CatalogStore(PACK / "atlas/oss-catalog.sqlite", bootstrap=False)
    jobs = ExistingJob(store)
    job = jobs.get(JOB, detect_interruption=False, include_targets=False)
    manifest = json.loads((BASE / "MANIFEST.json").read_text())
    assert job["leaves"] == [r["slug"] for r in manifest["leaves"]]
    assert job["scope"] == "first_round" and job["first_round_limit"] == 60 and job["batch_size"] == 16
    report = None
    if args.accept_verified_pilot:
        path = args.accept_verified_pilot.resolve()
        assert path == (PACK / "atlas/oss-discovery/acceptance" / (JOB + ".json")).resolve()
        text = path.read_text()
        evidence = json.loads(text)
        assert evidence["job_id"] == JOB and evidence["structural_passed"] is True and evidence["semantic_review_passed"] is True
        report = {"job_id": JOB, "structural_passed": True, "semantic_review_passed": True,
                  "report_path": str(path), "report_sha256": hashlib.sha256(text.encode()).hexdigest()}
    elif job["status"] in {"completed", "partial", "awaiting_acceptance", "paused_model"}:
        print(json.dumps({"job_id": JOB, "status": job["status"], "action": "none"}))
        return
    deadline = time.monotonic() + 75
    while True:
        try:
            result = jobs.accept_pilot(JOB, report) if report else jobs.resume(JOB, automatic=True)
            break
        except CatalogError as error:
            if error.status != 409 or time.monotonic() >= deadline:
                raise
            time.sleep(0.5)
    proof = {"job_id": JOB, "pid": os.getpid(), "state": "finished", "status": result["status"],
             "finished_at": now(), "processed": result["processed"], "total": result["total"],
             "completed_leaves": len(result.get("completed_leaves", [])), "pilot": result.get("pilot"),
             "service_restarted": False}
    atomic_json(RECEIPT, proof)
    print(json.dumps(proof, ensure_ascii=False))


if __name__ == "__main__":
    main()
