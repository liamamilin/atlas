"""Resume the authorized revision with full companion inputs; same provider may charge."""

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
jid = "job_9aaecca27143477992cb205f2e7c29bb"
if s.job(jid)["state"] != "failed":
    raise SystemExit("No implicit duplicate retry.")
s.retry(jid)
j = s.claim("authorized-revision-with-full-companions", "production")
(
    pilot / ("revision-2-attempt-" + str(j["attempt"]) + "-implementation.json")
).write_text(
    json.dumps(
        {
            "job_id": jid,
            "attempt": j["attempt"],
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
print(
    json.dumps({"event": "revision_retry_started", "attempt": j["attempt"]}), flush=True
)
execute(s, j, pipeline)
print(
    json.dumps(
        {
            "event": "revision_finished",
            "state": s.job(jid)["state"],
            "error": s.job(jid)["error"],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
review = s.claim("authorized-revision-independent-review", "verification")
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
            "event": "revision_retry_finished",
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
