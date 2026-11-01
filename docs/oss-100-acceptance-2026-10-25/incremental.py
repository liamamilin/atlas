"""Replay real saved data in an isolated copy, preserving cross-leaf links and favorites."""
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
from unittest.mock import patch

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, digest
from oss_batch import BatchJobs

with tempfile.TemporaryDirectory(prefix="atlas-100-incremental-") as directory:
    copied = Path(directory) / "catalog.sqlite"
    with sqlite3.connect("/private/tmp/atlas-100-acceptance-2026-10-25.sqlite") as src, sqlite3.connect(copied) as dst:
        src.backup(dst)
    store = CatalogStore(copied, bootstrap=False)
    identifier = "batch_cd8f7a777e3c4e6885de1cf3162e004c"
    job = BatchJobs(store).get(identifier, detect_interruption=False)
    selected = []
    with store.connect() as con:
        for leaf in job["leaves"]:
            rows = con.execute("SELECT p.full_name,p.repository_id FROM oss_leaf_project l JOIN oss_project p USING(repository_id) WHERE l.leaf=? ORDER BY p.repository_id LIMIT 2", (leaf,)).fetchall()
            selected.extend((leaf, r["full_name"], r["repository_id"]) for r in rows)
        shared = con.execute("SELECT repository_id FROM oss_leaf_project GROUP BY repository_id HAVING COUNT(*)>1 ORDER BY COUNT(*) DESC LIMIT 10").fetchall()
        for row in shared:
            rows = con.execute("SELECT l.leaf,p.full_name FROM oss_leaf_project l JOIN oss_project p USING(repository_id) WHERE repository_id=?", (row[0],)).fetchall()
            selected.extend((r[0], r[1], row[0]) for r in rows)
    selected = list(dict.fromkeys(selected))
    store.favorite(selected[0][2], True)
    def state():
        with store.connect() as con:
            return {"projects": con.execute("SELECT COUNT(*) FROM oss_project").fetchone()[0],
                    "memberships": con.execute("SELECT COUNT(*) FROM oss_leaf_project").fetchone()[0],
                    "membership_hash": digest(canonical([list(r) for r in con.execute("SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id")])),
                    "matches_hash": digest(canonical([list(r) for r in con.execute("SELECT * FROM oss_match ORDER BY scenario_id,repository_id")])),
                    "favorites_hash": digest(canonical([list(r) for r in con.execute("SELECT repository_id,favorite FROM oss_project ORDER BY repository_id")])),
                    "runs": con.execute("SELECT COUNT(*) FROM oss_run").fetchone()[0]}
    before = state()
    for leaf, repo, rid in selected:
        card = store.previous(repo, leaf)
        with store.connect() as con:
            store._upsert(con, card, leaf)
    replayed = state()
    assert before == replayed
    with patch("oss_batch.ROOT", Path(directory) / "batch-state"), \
            patch("oss_batch.BatchJobs.launch", side_effect=AssertionError("Finished job must not start")):
        result = BatchJobs(store).resume(identifier)
    assert result["status"] == "partial" and state() == before
    retry_leaves = [leaf for leaf in job["leaves"] if any(t["status"] == "failed" for t in job["targets"][leaf])]
    terminal_leaves = [leaf for leaf in job["leaves"] if leaf not in retry_leaves]
    with patch("oss_batch.ROOT", Path(directory) / "batch-state"), \
            patch("oss_discovery.Model.ask", side_effect=AssertionError("Terminal replay must not call model")), \
            patch("oss_workflow.GitHub.get", side_effect=AssertionError("Terminal replay must not fetch sources")):
        repeat = BatchJobs(store).create(terminal_leaves, existing_only=True)
    after = state()
    assert repeat["status"] == "completed" and repeat["total"] == repeat["processed"] == 0
    assert {k:v for k,v in before.items() if k != "runs"} == {k:v for k,v in after.items() if k != "runs"}
    report = {"result": "passed", "production_database_modified": False,
              "sample_memberships_replayed": len(selected), "sample_leaves": len({s[0] for s in selected}),
              "shared_projects_checked": len(shared), "before": before, "after": after,
              "finished_partial_job_resume_started_new_runs": False,
              "existing_only_terminal_leaves": len(terminal_leaves), "existing_only_targets": repeat["total"],
              "existing_only_preparation_records": after["runs"] - before["runs"],
              "known_failed_leaves_excluded_from_zero_work_assertion": retry_leaves,
              "note": "Two original failed candidates remain explicitly retryable; the terminal replay assertion excludes their two leaves."}
    (BASE / "INCREMENTAL.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k not in {"before", "after"}}, ensure_ascii=False))
