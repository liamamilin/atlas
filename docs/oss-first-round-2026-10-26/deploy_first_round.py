"""Load the verified first-round implementation during one approved idle reload."""
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
if os.environ.get("ATLAS_FIRST_ROUND_APPROVED_RELOAD") != "1":
    raise RuntimeError("Requires approval for one idle API reload; no service operation performed")
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, now

EXPECTED_PID = 80467
PYTHON = "/Users/milin/.pyenv/versions/3.10.13/bin/python3"
SCRIPT = str(PACK / "drafts_api.py")
store = CatalogStore(bootstrap=False)

def invariants():
    result = {}
    with store.connect() as con:
        for table, order in [("oss_project", "repository_id"), ("oss_scenario", "id"),
                             ("oss_match", "scenario_id,repository_id"), ("oss_leaf_project", "leaf,repository_id"),
                             ("oss_candidate", "leaf,repository_id"), ("oss_run", "id"), ("oss_batch_job", "id")]:
            checksum, count = hashlib.sha256(), 0
            for row in con.execute(f"SELECT * FROM {table} ORDER BY {order}"):
                checksum.update(canonical(list(row)).encode())
                checksum.update(b"\n")
                count += 1
            result[table] = {"rows": count, "sha256": checksum.hexdigest()}
    return result

def settings_digests():
    return {name: hashlib.sha256((PACK / "atlas" / name).read_bytes()).hexdigest()
            for name in ("model-config.json", "github-credentials.json") if (PACK / "atlas" / name).exists()}

def assert_idle():
    with store.connect() as con:
        assert not con.execute("SELECT 1 FROM oss_batch_job WHERE status IN ('running','retry_wait','interrupted','awaiting_acceptance','paused_model')").fetchone()
    with urlopen("http://127.0.0.1:5199/api/health", timeout=10) as response:
        status = json.load(response)
        assert status["ok"] and not status["generating"] and not status["promoting"]

lock = store._lock()
try:
    assert_idle()
    command = subprocess.check_output(["ps", "-p", str(EXPECTED_PID), "-o", "command="], text=True).strip()
    assert shlex.split(command) == [PYTHON, "-u", SCRIPT, "--port", "5199"]
    assert subprocess.check_output(["lsof", "-t", "-iTCP:5199", "-sTCP:LISTEN"], text=True).split() == [str(EXPECTED_PID)]
    before, settings_before = invariants(), settings_digests()
    backup = Path("/private/tmp/atlas-before-first-round-2026-10-26.sqlite")
    with sqlite3.connect(store.path) as src, sqlite3.connect(backup) as dst:
        src.backup(dst)
    (BASE / "DEPLOY_BEFORE.json").write_text(json.dumps({"checked_at": now(), "backup": str(backup),
        "previous_pid": EXPECTED_PID, "invariants": before}, ensure_ascii=False, indent=2) + "\n")
    assert_idle()
    os.kill(EXPECTED_PID, signal.SIGTERM)
    for _ in range(50):
        if subprocess.run(["lsof", "-t", "-iTCP:5199", "-sTCP:LISTEN"], capture_output=True).returncode != 0:
            break
        time.sleep(0.2)
    else:
        raise RuntimeError("Old API did not release the port; no replacement started")
    environment = dict(os.environ, ATLAS_FACTORY_DISABLE_WORKER="1", ATLAS_OSS_MODEL_CONCURRENCY="4")
    with (PACK / "atlas/oss-api.log").open("ab") as output:
        process = subprocess.Popen([PYTHON, "-u", SCRIPT, "--port", "5199"], cwd=PACK, env=environment,
                                   stdin=subprocess.DEVNULL, stdout=output, stderr=output, start_new_session=True)
    Path("/private/tmp/atlas-v3-api-pid").write_text(str(process.pid) + "\n")
    healthy = False
    for _ in range(40):
        assert process.poll() is None
        try:
            with urlopen("http://127.0.0.1:5199/api/health", timeout=2) as response:
                healthy = response.status == 200 and json.load(response)["ok"]
            if healthy:
                break
        except OSError:
            pass
        time.sleep(0.25)
    assert healthy and invariants() == before and settings_digests() == settings_before
    proof = {"checked_at": now(), "previous_pid": EXPECTED_PID, "pid": process.pid, "api_healthy": True,
             "catalog_candidates_matches_favorites_and_history_preserved": True,
             "model_and_github_settings_preserved": True, "factory_worker_disabled": True,
             "model_concurrency": 4, "backup": str(backup),
             "source_sha256": {name: hashlib.sha256((PACK / name).read_bytes()).hexdigest() for name in [
                 "oss_batch.py", "oss_priority.py", "oss_sources.py", "oss_workflow.py", "oss_catalog.py", "oss_acceptance.py"]}}
    (BASE / "DEPLOYED.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(proof, ensure_ascii=False))
finally:
    lock.close()
