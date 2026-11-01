"""Start exactly the authorized frozen first-round campaign, with a 20-leaf gate."""
import json
from pathlib import Path
import sqlite3
from datetime import datetime, timezone
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
manifest = json.loads((BASE / "MANIFEST.json").read_text())
leaves = [leaf["slug"] for leaf in manifest["leaves"]]
assert len(leaves) == len(set(leaves)) == manifest["leaf_count"] == 1598
with sqlite3.connect(PACK / "atlas/oss-catalog.sqlite") as con:
    jobs = [json.loads(r[0]) for r in con.execute("SELECT data FROM oss_batch_job")]
    covered = {r[0] for r in con.execute("SELECT DISTINCT leaf FROM oss_scenario")}
matching = [j for j in jobs if j["leaves"] == leaves and j.get("first_round_limit") == 60]
if matching:
    assert len(matching) == 1
    job, http_status = matching[0], None
else:
    assert not set(leaves) & covered
    assert not any(j["status"] in {"running", "retry_wait", "interrupted", "paused_model", "awaiting_acceptance"} for j in jobs)
    body = {"leaves": leaves, "existing_only": False, "batch_size": 16, "search_pages": 1,
            "first_round_limit": 60, "pilot_size": 20}
    (BASE / "START_INTENT.json").write_text(json.dumps({"created_at": datetime.now(timezone.utc).isoformat(),
        "body": body, "authorization": "20-leaf actual acceptance, then automatically complete this finite 1598-leaf first-round list"}, ensure_ascii=False, indent=2) + "\n")
    request = Request("http://127.0.0.1:5199/api/oss/batches", data=json.dumps(body).encode(),
                      headers={"Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=30) as response:
        http_status = response.status
        job = json.load(response)
assert job["scope"] == "first_round" and job["first_round_limit"] == 60 and job["pilot"]["size"] == 20
assert job["auto_recovery"] and job["leaves"] == leaves
proof = {k: job.get(k) for k in ["id", "status", "created_at", "scope", "storage_version", "first_round_limit", "source_policy", "source_pipeline", "pilot", "batch_size", "auto_recovery", "processed", "total"]}
proof.update(leaf_count=len(leaves), http_status=http_status, checked_at=datetime.now(timezone.utc).isoformat())
(BASE / "START.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(proof, ensure_ascii=False))
