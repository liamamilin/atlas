"""Compare repaired production to its pre-repair SQLite backup, read-only."""
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

BASE = Path(__file__).resolve().parent
PACK = BASE.parent.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import canonical, now

JOB = "batch_4812ef3db57543c3acc1871b8ea5ba6e"
LEAVES = ["log-management", "distributed-control-system-dcs", "it-operations-management-itom", "portfolio-management-system"]


def connect(path):
    immutable = "&immutable=1" if str(path).startswith("/private/tmp/") else ""
    con = sqlite3.connect(f"file:{path}?mode=ro{immutable}", uri=True)
    con.row_factory = sqlite3.Row
    return con


def table_hash(con, query):
    h = hashlib.sha256()
    for row in con.execute(query):
        h.update(canonical(list(row)).encode())
        h.update(b"\n")
    return h.hexdigest()


def main():
    state = json.loads((BASE / "STATE.json").read_text())
    before = json.loads((BASE / "BEFORE.json").read_text())
    assert state["state"] == "completed"
    old, new = connect(before["backup"]), connect(PACK / "atlas/oss-catalog.sqlite")
    failures, checks = [], {}
    def check(name, passed, **details):
        checks[name] = {"passed": bool(passed), **details}
        if not passed:
            failures.append(name)

    old_jobs = {r[0] for r in old.execute("SELECT id FROM oss_batch_job")}
    new_jobs = {r[0] for r in new.execute("SELECT id FROM oss_batch_job")}
    check("no_new_batch", old_jobs == new_jobs, before=len(old_jobs), after=len(new_jobs))
    old_targets = {tuple(r) for r in old.execute("SELECT * FROM oss_batch_target WHERE job_id=?", (JOB,))}
    new_targets = {tuple(r) for r in new.execute("SELECT * FROM oss_batch_target WHERE job_id=?", (JOB,))}
    check("original_targets_exactly_preserved", old_targets <= new_targets, original=len(old_targets), missing=len(old_targets-new_targets))
    extra = new_targets - old_targets
    check("extra_targets_only_two_empty_leaves", all(r[1] in LEAVES[1:3] for r in extra), added=len(extra))
    counts = dict(new.execute("SELECT leaf,COUNT(*) FROM oss_batch_target WHERE job_id=? GROUP BY leaf", (JOB,)))
    check("per_leaf_60_limit", all(v <= 60 for v in counts.values()), maximum=max(counts.values()))
    changed_facts = changed_favorites = missing_projects = 0
    for row in old.execute("SELECT repository_id,data,favorite FROM oss_project"):
        current = new.execute("SELECT data,favorite FROM oss_project WHERE repository_id=?", (row[0],)).fetchone()
        if current is None:
            missing_projects += 1
            continue
        a, b = json.loads(row[1]), json.loads(current[0])
        a.pop("matches", None); b.pop("matches", None)
        changed_facts += a != b
        changed_favorites += row[2] != current[1]
    check("existing_project_facts_and_licenses_preserved", not changed_facts and not missing_projects,
          changed=changed_facts, missing=missing_projects)
    check("existing_favorites_preserved", not changed_favorites, changed=changed_favorites)
    for table, columns in [("oss_leaf_project", "leaf,repository_id"), ("oss_match", "scenario_id,repository_id,data")]:
        previous = {tuple(r) for r in old.execute(f"SELECT {columns} FROM {table}")}
        current = {tuple(r) for r in new.execute(f"SELECT {columns} FROM {table}")}
        check(table+"_original_rows_preserved", previous <= current, before=len(previous), after=len(current), missing=len(previous-current))
    missing_candidates = changed_metadata = changed_old_status = 0
    for row in old.execute("SELECT leaf,repository_id,status,reason,data FROM oss_candidate"):
        current = new.execute("SELECT status,reason,data FROM oss_candidate WHERE leaf=? AND repository_id=?", (row[0],row[1])).fetchone()
        if current is None:
            missing_candidates += 1
            continue
        changed_old_status += tuple(row[2:4]) != tuple(current[:2])
        changed_metadata += json.loads(row[4])["meta"] != json.loads(current[2])["meta"]
    check("all_original_candidates_preserved", not missing_candidates, missing=missing_candidates)
    check("original_candidate_metadata_and_states_preserved", not changed_metadata and not changed_old_status,
          metadata_changes=changed_metadata, state_changes=changed_old_status)
    outside = "leaf NOT IN (" + ",".join("'"+leaf+"'" for leaf in LEAVES) + ")"
    for table, order in [("oss_candidate", "leaf,repository_id"), ("oss_batch_leaf", "job_id,leaf"), ("oss_scenario", "id")]:
        query=f"SELECT * FROM {table} WHERE {outside} ORDER BY {order}"
        check(table+"_outside_four_leaves_unchanged", table_hash(old, query)==table_hash(new, query))
    job=json.loads(new.execute("SELECT data FROM oss_batch_job WHERE id=?", (JOB,)).fetchone()[0])
    check("all_four_errors_resolved_with_history", not job["errors"] and len([
        e for e in job.get("resolved_errors",[]) if e.get("repair_record")==str(BASE/"STATE.json")])==4)
    result={"checked_at":now(),"job_id":JOB,"passed":not failures,"production_database_modified":False,
            "checks":checks,"failures":failures}
    (BASE/"PRESERVATION.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(canonical({"passed":result["passed"],"failures":failures,"new_targets":len(extra)}),flush=True)
    old.close();new.close()
    raise SystemExit(0 if result["passed"] else 1)


if __name__=="__main__":
    main()
