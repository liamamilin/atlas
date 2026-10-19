"""Authorized review-driven revision; invokes the same provider, never executes package programs."""

import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore  # noqa: E402
from template_factory.pipeline import Pipeline  # noqa: E402
from template_factory.worker import execute  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
original = next(
    a for a in s.artifacts() if a["id"] == "tpl_231994f1a0a841d6b040d66de3287a6a"
)
if any(a.get("supersedes") == original["id"] for a in s.artifacts()):
    raise SystemExit("Revision exists; inspect it rather than duplicating calls.")
with s.connect() as con:
    if con.execute(
        "select 1 from job where kind='blueprint-production' and json_extract(snapshot,'$.cognitive_repair.id')=? AND state!='cancelled'",
        (original["id"],),
    ).fetchone():
        raise SystemExit(
            "A revision attempt already exists; inspect/retry its checkpoint."
        )
notes = (Path(__file__).parent / "REPAIR_6_NOTES.md").read_text()
batch = s.create_repair(
    original["id"],
    {
        "expected_digest": original["digest"],
        "model": "open-design/deepseek-v4.1-flash",
        "note": notes,
        "edit_paths": [
            "acceptance/common.cjs", "acceptance/run.cjs",
            "acceptance/p0-limits.cjs", "acceptance/p1-categories.cjs",
            "acceptance/p2-search.cjs", "acceptance/ui-p0.cjs",
            "acceptance/ui-p1.cjs", "acceptance/ui-p2.cjs",
            "acceptance/README.md",
        ],
        "reuse_spec": False,
        "timeout": 1200,
        "language": "zh",
    },
)
j = s.claim("authorized-bookmark-review-driven-revision", "production")
(pilot / "revision-6-scoped-implementation.json").write_text(
    json.dumps(
        {
            "job_id": j["id"],
            "batch_id": batch["id"],
            "original": original["id"],
            "notes_sha256": hashlib.sha256(notes.encode()).hexdigest(),
            "sha256": {
                name: hashlib.sha256(
                    (pack / "template_factory" / name).read_bytes()
                ).hexdigest()
                for name in (
                    "cognition.py",
                    "cli.py",
                    "pipeline.py",
                    "store.py",
                    "blueprints.py",
                )
            },
        },
        indent=2,
    )
)
pipeline = Pipeline(s)
print(json.dumps({"event": "revision_started", "job_id": j["id"]}), flush=True)
execute(s, j, pipeline)
print(
    json.dumps(
        {
            "event": "revision_finished",
            "state": s.job(j["id"])["state"],
            "error": s.job(j["id"])["error"],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
review = s.claim("authorized-bookmark-revision-independent-review", "verification")
if review:
    print(
        json.dumps(
            {"event": "independent_revision_review_started", "job_id": review["id"]}
        ),
        flush=True,
    )
    execute(s, review, pipeline)
print(
    json.dumps(
        {
            "event": "revision_run_finished",
            "artifacts": [
                {
                    "id": a["id"],
                    "version": a["manifest"]["version"],
                    "reviews": [(r["method"], r["outcome"]) for r in a["acceptances"]],
                }
                for a in s.artifacts()
            ],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
