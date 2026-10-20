"""Install the archived R7 recovery evidence into an isolated R5 fixture."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil

from template_factory.store import canonical

PACK = Path(__file__).resolve().parents[1]
REPO = PACK.parent
ARCHIVE = REPO / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20"
R7 = REPO / "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20"
JOB_ID = "job_3a658ba085e8417ea6faad5cb0cdd493"


def install_r7_evidence(base):
    """Replace only temporary DB rows/files with the immutable archived R7 evidence."""
    store, root = base.store, base.root
    baseline = json.loads((ARCHIVE / "BASELINE.json").read_text())
    job = baseline["job"]
    auth = ARCHIVE / "authorization/ATLAS_G1_R7_EVIDENCE_RECOVERY_CODEX_INSTRUCTIONS.txt"
    dest_auth = root / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/authorization/ATLAS_G1_R7_EVIDENCE_RECOVERY_CODEX_INSTRUCTIONS.txt"
    dest_auth.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(auth, dest_auth)

    # Install exact original phase inputs, results, reports, and source projections.
    raw_root = R7 / "actual-production-raw"
    projections = R7 / "actual-review-projections"
    attempt = store.root / "jobs" / JOB_ID / "attempt-1"
    for raw_stage in sorted(p for p in raw_root.iterdir() if p.is_dir()):
        stage = raw_stage.name
        target = attempt / stage
        target.mkdir(parents=True, exist_ok=True)
        for name in ("input.json", "result.json", "report.json"):
            shutil.copyfile(raw_stage / name, target / name)
        dim = stage.removeprefix("blueprint-spec-review-0-ad1379367f3e742a-").removesuffix("-v1")
        projection = projections / ("design-context-0-" + dim)
        shutil.copytree(projection, target / "source", dirs_exist_ok=True)
        config_src = ARCHIVE / "historical-cli-configs" / stage / "opencode.json"
        archived = json.loads(config_src.read_text())
        directory = target.resolve()
        reads = ["input.json", "leaf.md", "source", "source/**"]
        reads += [str(directory / name) for name in reads[:]]
        rules = [{"action": "*", "resource": "*", "effect": "deny"}]
        rules += [{"action": "read", "resource": name, "effect": "allow"} for name in reads]
        policies = archived["policies"]
        agent_name = "atlas-factory-" + hashlib.sha256(str(directory).encode()).hexdigest()[:12]
        config = {"$schema": archived["$schema"], "permissions": rules,
                  "agents": {agent_name: {"mode": "primary", "description": "Atlas read-only factory proposal agent", "permissions": rules}},
                  "policies": policies}
        (target / "opencode.json").write_text(json.dumps(config, ensure_ascii=False, indent=1) + "\n")

    # Restore the full archived 77/7/0 budget ledger rather than the smaller R5 fixture ledger.
    with store.connect(True) as con:
        con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (job["id"], job["batch_id"], job["kind"], job["state"], job["stage"], job["attempt"],
                     None, None, canonical(job["snapshot"]), canonical(job["error"]),
                     job["created_at"], job["updated_at"]))
        con.execute("DELETE FROM checkpoint WHERE job_id=?", (JOB_ID,))
        for row in baseline["checkpoints"]:
            con.execute("INSERT INTO checkpoint VALUES(?,?,?)", (JOB_ID, row["name"], row["body"]))
        con.execute("INSERT OR REPLACE INTO batch VALUES(?,?,?,?)",
                    (job["batch_id"], "paused", canonical(job["snapshot"]["config"]), job["created_at"]))
        for table, rows in baseline["ledger"].items():
            try:
                cols = [r[1] for r in con.execute(f"PRAGMA table_info({table})")]
            except Exception:
                continue
            if not cols:
                continue
            con.execute(f"DELETE FROM {table}")
            for row in rows:
                keys = [key for key in cols if key in row]
                con.execute(f"INSERT INTO {table} ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                            tuple(row[key] for key in keys))
    frozen = store.root / "jobs/job_a53c47f3694047489c4f82cfc2e346be/attempt-1/bundle"
    archived_bundle = store.root / "jobs/job_d0d9d80dc9f64dd9890fc0b728bd9a5d/attempt-5/bundle"
    if archived_bundle.exists():
        shutil.rmtree(archived_bundle)
    archived_bundle.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(frozen, archived_bundle)
    return baseline
