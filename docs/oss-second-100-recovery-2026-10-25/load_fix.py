"""Load the tested fix while no discovery is active, preserving the catalog."""
import hashlib
import json
import os
from pathlib import Path
import shlex
import signal
import sqlite3
import subprocess
import sys
import time
from urllib.request import urlopen

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, now
from oss_batch import BatchJobs

IDENTIFIER = "batch_9ab8ea47e4ef450cbb4afe5b295594e3"
if os.environ.get("ATLAS_APPROVED_IDLE_API_RELOAD") != "1":
    raise RuntimeError("Requires explicit user approval to reload a healthy API; no service operation performed")
EXPECTED_PID = 63353
PYTHON = "/Users/milin/.pyenv/versions/3.10.13/bin/python3"
SCRIPT = str(PACK / "drafts_api.py")
store = CatalogStore(bootstrap=False)
lock = store._lock()

def invariants():
    result = {}
    with store.connect() as con:
        for table, order in [("oss_project", "repository_id"), ("oss_scenario", "id"),
                             ("oss_match", "scenario_id,repository_id"),
                             ("oss_leaf_project", "leaf,repository_id"), ("oss_candidate", "leaf,repository_id")]:
            checksum = hashlib.sha256()
            count = 0
            for row in con.execute(f"SELECT * FROM {table} ORDER BY {order}"):
                checksum.update(canonical(list(row)).encode())
                checksum.update(b"\n")
                count += 1
            result[table] = {"rows": count, "sha256": checksum.hexdigest()}
    return result

def settings_digests():
    return {name: hashlib.sha256((PACK / "atlas" / name).read_bytes()).hexdigest()
            for name in ("model-config.json", "github-credentials.json")
            if (PACK / "atlas" / name).exists()}

try:
    with store.connect() as con:
        assert not con.execute("SELECT 1 FROM oss_batch_job WHERE status IN ('running','retry_wait','interrupted')").fetchone()
    job = BatchJobs(store).get(IDENTIFIER, detect_interruption=False)
    legacy_targets = len(BatchJobs.interrupted_targets(job))
    assert (job["status"] == "partial" and legacy_targets == 16) or (job["status"] == "completed" and legacy_targets == 0)
    command = subprocess.check_output(["ps", "-p", str(EXPECTED_PID), "-o", "command="], text=True).strip()
    assert shlex.split(command) == [PYTHON, "-u", SCRIPT, "--port", "5199"], command
    listeners = subprocess.check_output(["lsof", "-t", "-iTCP:5199", "-sTCP:LISTEN"], text=True).split()
    assert listeners == [str(EXPECTED_PID)], listeners
    with urlopen("http://127.0.0.1:5199/api/health", timeout=10) as response:
        health = json.load(response)
        assert health["ok"] and not health["generating"] and not health["promoting"]
    before = invariants()
    settings_before = settings_digests()
    backup = Path("/private/tmp/atlas-second100-before-recovery.sqlite")
    with sqlite3.connect(store.path) as src, sqlite3.connect(backup) as dst:
        src.backup(dst)
    (BASE / "BEFORE.json").write_text(json.dumps({
        "id": IDENTIFIER, "checked_at": now(), "status": job["status"], "processed": job["processed"],
        "total": job["total"], "failed_targets": legacy_targets,
        "backup": str(backup), "invariants": before,
    }, ensure_ascii=False, indent=2) + "\n")
    os.kill(EXPECTED_PID, signal.SIGTERM)
    for _ in range(50):
        if subprocess.run(["lsof", "-t", "-iTCP:5199", "-sTCP:LISTEN"], capture_output=True).returncode != 0:
            break
        time.sleep(0.2)
    else:
        raise RuntimeError("Old API did not release port; no replacement started")
    environment = dict(os.environ, ATLAS_FACTORY_DISABLE_WORKER="1", ATLAS_OSS_MODEL_CONCURRENCY="4")
    with (PACK / "atlas/oss-api.log").open("ab") as output:
        process = subprocess.Popen([PYTHON, "-u", SCRIPT, "--port", "5199"], cwd=PACK,
                                   env=environment, stdin=subprocess.DEVNULL,
                                   stdout=output, stderr=output, start_new_session=True)
    Path("/private/tmp/atlas-v3-api-pid").write_text(str(process.pid) + "\n")
    healthy = False
    for _ in range(40):
        assert process.poll() is None, "Replacement API exited; inspect local log"
        try:
            with urlopen("http://127.0.0.1:5199/api/health", timeout=2) as response:
                healthy = response.status == 200 and json.load(response)["ok"]
            if healthy:
                break
        except OSError:
            pass
        time.sleep(0.25)
    assert healthy
    after = invariants()
    assert before == after
    assert settings_digests() == settings_before
    proof = {"checked_at": now(), "job_id": IDENTIFIER, "previous_pid": EXPECTED_PID,
             "pid": process.pid, "api_healthy": healthy, "active_jobs_before_maintenance": 0,
             "factory_worker_disabled": True, "model_concurrency": 4,
             "catalog_invariants_preserved": before == after, "invariants": after,
             "model_and_github_settings_preserved": True, "settings_sha256": settings_before,
             "manual_resume_requests": 0,
             "note": "Release the update lock; server supervisor will restore only legacy coordinator-abort targets."}
    (BASE / "SERVICE.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k:v for k,v in proof.items() if k != "invariants"}, ensure_ascii=False))
finally:
    lock.close()
