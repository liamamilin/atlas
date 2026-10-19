"""Read-only comparison of production history against the pre-work capture."""
import hashlib
import json
from pathlib import Path
import sqlite3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2] / "application-atlas-production-pack/atlas/template-factory"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def capture():
    with sqlite3.connect("file:" + str(ROOT / "factory.sqlite") + "?mode=ro", uri=True) as con:
        con.row_factory = sqlite3.Row
        names = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        tables = {}
        for name in names:
            rows = [list(r) for r in con.execute('SELECT * FROM "' + name + '" ORDER BY rowid')]
            tables[name] = {"count": len(rows), "digest": digest(rows)}
        job = dict(con.execute("SELECT id,state,stage,attempt,snapshot,error FROM job WHERE id=?", ("job_a53c47f3694047489c4f82cfc2e346be",)).fetchone())
        job["snapshot_digest"] = digest(json.loads(job.pop("snapshot")))
        budget = {n: [dict(r) for r in con.execute("SELECT * FROM " + n)] for n in ("tf_budget_phase", "tf_budget_repair", "tf_budget_amendment")}
    files = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
             for top in ("jobs", "artifacts") for p in (ROOT / top).rglob("*") if p.is_file()}
    groups = {}
    for name, value in files.items():
        groups.setdefault("/".join(name.split("/")[:2]), {})[name] = value
    # File manifests contain ASCII paths/hashes; same canonical encoding as the
    # initial capture. Database values retain UTF-8 in the logical-table hash.
    file_digest = lambda value: hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"job": job, "logical_tables": tables, "budget": budget,
            "historical_files": {"count": len(files), "digest": file_digest(files),
                                 "groups": {name: {"count": len(rows), "digest": file_digest(rows)} for name, rows in groups.items()}}}


if __name__ == "__main__":
    before = json.loads((HERE / "production-before.json").read_text())
    after = capture()
    changed = [key for key in after if before[key] != after[key]]
    (HERE / "production-after.json").write_text(json.dumps(after, ensure_ascii=False, indent=2) + "\n")
    proof = {"unchanged": not changed, "changed_sections": changed,
             "cli_reservations": after["logical_tables"]["tf_budget_reservation"]["count"],
             "business_repairs": after["logical_tables"]["tf_budget_repair"]["count"],
             "historical_file_count": after["historical_files"]["count"],
             "historical_file_manifest_digest": after["historical_files"]["digest"],
             "job_state": after["job"]["state"], "evidence_scope": "Read-only SQL and history file hashes; not G1 assessment."}
    (HERE / "production-unchanged-proof.json").write_text(json.dumps(proof, indent=2) + "\n")
    print(json.dumps(proof))
    raise SystemExit(bool(changed))
