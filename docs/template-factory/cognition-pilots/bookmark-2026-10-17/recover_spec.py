"""Recover complete model JSON framing, then continue authorized file production."""

import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore, digest  # noqa: E402
from template_factory.pipeline import Pipeline  # noqa: E402
from template_factory.worker import execute  # noqa: E402
from template_factory.cli import parse_result  # noqa: E402
from template_factory.cognition import validate_file_plan  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
jid = "job_2ecd0ef53c074c17802cac662f9e96b9"
j = s.job(jid)
if (
    j["state"] != "failed"
    or j["attempt"] != 2
    or j["snapshot"]["config"]["model"] != "open-design/deepseek-v4.1-flash"
):
    raise SystemExit(
        "This recovery applies only to the recorded attempt-2 framing failure."
    )
events = [
    json.loads(line)
    for line in (pilot / "jobs" / jid / "attempt-2/blueprint-generate-0/events.jsonl")
    .read_text()
    .splitlines()
]
content = [v["part"]["text"] for v in events if v.get("type") == "text"][-1]
plan = parse_result(content, redundant_closing=True)
validate_file_plan(plan)
original, end = json.JSONDecoder().raw_decode(content)
assert original == plan and content[end:] == "}"
s.retry(jid)
j = s.claim("authorized-bookmark-framing-recovery", "production")
record = {
    "attempt": j["attempt"],
    "job_id": jid,
    "recovery": "Complete attempt-2 JSON object reused; only one redundant terminal brace removed. No fields edited and no new model specification call.",
    "original_text_sha256": hashlib.sha256(content.encode()).hexdigest(),
    "normalized_plan_digest": digest(plan),
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
}
(pilot / "attempt-3-implementation.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2)
)
(Path(__file__).parent / "spec-framing-recovery.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2)
)
s.checkpoint(
    jid, "blueprint-plan-0", {"result": plan, "digest": digest(plan)}, j["token"]
)
pipeline = Pipeline(s)
print(
    json.dumps(
        {
            "event": "file_production_started",
            "attempt": j["attempt"],
            "file_count": len(plan["file_plan"]),
        }
    ),
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
review = s.claim("authorized-bookmark-independent-review", "verification")
if review:
    print(
        json.dumps({"event": "independent_review_started", "job_id": review["id"]}),
        flush=True,
    )
    execute(s, review, pipeline)
print(
    json.dumps(
        {
            "event": "recovery_finished",
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
