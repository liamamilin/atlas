"""Read-only compact progress proof; no provider configuration or full cards."""
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
DB = PACK / "atlas/oss-catalog.sqlite"
JOB = "batch_4812ef3db57543c3acc1871b8ea5ba6e"
with sqlite3.connect("file:" + str(DB) + "?mode=ro", uri=True) as con:
    con.row_factory = sqlite3.Row
    job = json.loads(con.execute("SELECT data FROM oss_batch_job WHERE id=?", (JOB,)).fetchone()[0])
    leaves = [dict(r) for r in con.execute(
        "SELECT leaf,position,selected_count,candidate_total,deferred_count,state FROM oss_batch_leaf WHERE job_id=? ORDER BY position", (JOB,))]
    counts = dict(con.execute("SELECT status,COUNT(*) FROM oss_batch_target WHERE job_id=? GROUP BY status", (JOB,)))
    run_ids = set(job["runs"])
    runs = [json.loads(r["data"]) for r in con.execute("SELECT id,data FROM oss_run") if r["id"] in run_ids]
    candidates = [json.loads(r[0]) for r in con.execute(
        "SELECT c.data FROM oss_candidate c JOIN oss_batch_target t ON c.leaf=t.leaf AND c.repository_id=t.repository_id WHERE t.job_id=?", (JOB,))]
windows = [(t["started_at"], t["finished_at"]) for r in runs for t in r.get("model_tasks", {}).values()
           if t.get("started_at") and t.get("finished_at")]
overlap = sum(any(max(s["started_at"], a) < min(s["finished_at"], b) for a, b in windows)
              for r in runs if (s := r.get("source_timing")))
proof = {
    "checked_at": datetime.now(timezone.utc).isoformat(), "id": JOB, "status": job["status"],
    "manifest_leaves": len(job["leaves"]), "completed_leaves": sum(l["state"] in {"first_round_done", "failed"} for l in leaves),
    "current_leaf": job.get("current_leaf"), "current_run": job.get("current_run"),
    "processed": sum(n for status, n in counts.items() if status not in {"pending", "running"}),
    "selected": sum(counts.values()), "target_statuses": counts, "leaves": leaves,
    "deferred_total": sum(l["deferred_count"] for l in leaves), "pilot": job.get("pilot"),
    "recovery": job.get("recovery"),
    "peak_configured_model_workers": max((r.get("concurrency", {}).get("model_workers", 0) for r in runs), default=0),
    "measured_overlapping_source_groups": overlap,
    "source_fetches": sum(r.get("source_fetches", 0) for r in runs),
    "model_calls": sum(r.get("model_calls", 0) for r in runs),
    "models": dict(Counter((m.get("provider", ""), m.get("model", ""))
                           for r in runs for m in r.get("model_receipts", []))),
    "selected_zero_star_candidates": sum(not c["meta"].get("stargazers_count") for c in candidates),
    "supervisor": json.loads(DB.with_suffix(".recovery.json").read_text()),
}
# JSON object keys must be strings; provider/model are non-secret receipt labels.
proof["models"] = {" / ".join(k): v for k, v in proof["models"].items()}
(BASE / "PROGRESS.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in proof.items() if k not in {"leaves", "supervisor"}}, ensure_ascii=False))
