"""Launch exactly the authorized following 100 leaves after recorded acceptance."""
import json
from pathlib import Path
import sqlite3
from datetime import datetime, timezone
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
DB = PACK / "atlas/oss-catalog.sqlite"
manifest = json.loads((BASE / "NEXT_100_LEAVES.json").read_text())
totals = json.loads((BASE / "TOTALS.json").read_text())
assert totals["leaf_count"] == 100 and totals["processed"] == totals["targets"]
assert json.loads((BASE / "AUDIT_FAILURES.json").read_text()) == []
assert json.loads((BASE / "INCREMENTAL.json").read_text())["result"] == "passed"
assert json.loads((BASE / "LIVE_BROWSER.json").read_text())["result"] == "passed"
assert json.loads((BASE / "MANUAL_REVIEW.json").read_text())["result"] == "passed_after_one_narrowing_correction"
leaves = [leaf["slug"] for leaf in manifest["leaves"]]
assert len(leaves) == len(set(leaves)) == 100
with sqlite3.connect(DB) as con:
    jobs = [json.loads(row[0]) for row in con.execute("SELECT data FROM oss_batch_job")]
    covered = {row[0] for row in con.execute("SELECT DISTINCT leaf FROM oss_scenario")}
matching = [job for job in jobs if job["leaves"] == leaves]
if matching:
    assert len(matching) == 1
    job = matching[0]
    http_status = None
    reused = True
else:
    assert not any(job["status"] not in {"completed", "partial"} for job in jobs)
    assert not (set(leaves) & covered)
    body = {"leaves": leaves, "existing_only": False, "batch_size": 16, "search_pages": 1}
    intent = {"created_at": datetime.now(timezone.utc).isoformat(), "body": body,
              "parent_accepted_job": manifest["parent_accepted_job"], "acceptance_result": "passed_with_labeled_gaps"}
    (BASE / "NEXT_100_INTENT.json").write_text(json.dumps(intent, ensure_ascii=False, indent=2) + "\n")
    request = Request("http://127.0.0.1:5199/api/oss/batches", data=json.dumps(body).encode(),
                      headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=30) as response:
        http_status = response.status
        job = json.load(response)
    reused = False
assert job["leaves"] == leaves and job["batch_size"] == 16 and job["auto_recovery"] is True
manifest.update(launch_gate="PASSED", accepted_at=datetime.now(timezone.utc).isoformat())
(BASE / "NEXT_100_LEAVES.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
proof = {k: job.get(k) for k in ["id", "status", "created_at", "leaves", "batch_size", "search_pages", "auto_recovery", "processed", "total", "current_leaf", "prepared"]}
proof.update(http_status=http_status, reused_existing_identical_job=reused,
             checked_at=datetime.now(timezone.utc).isoformat(), leaf_count=100,
             root_count=len(manifest["root_distribution"]), model_concurrency=4,
             model_concurrency_proof="Prior production runs; first following-batch run will be checked separately.")
(BASE / "NEXT_100_START.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k:v for k,v in proof.items() if k not in {"leaves", "prepared"}}, ensure_ascii=False))
