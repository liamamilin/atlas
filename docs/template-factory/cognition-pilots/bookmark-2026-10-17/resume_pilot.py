"""Explicit authorized retry of the existing pilot; invokes the same paid provider."""

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
jid = "job_2ecd0ef53c074c17802cac662f9e96b9"
j = s.job(jid)
if (
    j["state"] != "failed"
    or j["snapshot"]["config"]["model"] != "open-design/deepseek-v4.1-flash"
):
    raise SystemExit("Inspect the existing job; no implicit duplicate calls.")
s.retry(jid)
j = s.claim("authorized-split-bookmark-production", "production")
(pilot / ("attempt-" + str(j["attempt"]) + "-implementation.json")).write_text(
    json.dumps(
        {
            "job_id": jid,
            "attempt": j["attempt"],
            "reason": "first monolithic response truncated; use pinned research with split specification and file checkpoints",
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
    json.dumps({"event": "production_retry_started", "attempt": j["attempt"]}),
    flush=True,
)
execute(s, j, pipeline)
print(
    json.dumps(
        {
            "event": "production_finished",
            "state": s.job(jid)["state"],
            "error": s.job(jid)["error"],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
review = s.claim("authorized-split-bookmark-review", "verification")
if review:
    print(
        json.dumps({"event": "independent_review_started", "job_id": review["id"]}),
        flush=True,
    )
    execute(s, review, pipeline)
print(
    json.dumps(
        {
            "event": "retry_finished",
            "artifacts": [
                {
                    "id": a["id"],
                    "reviews": [(r["method"], r["outcome"]) for r in a["acceptances"]],
                }
                for a in s.artifacts()
            ],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
