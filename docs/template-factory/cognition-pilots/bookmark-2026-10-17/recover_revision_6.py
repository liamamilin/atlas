"""Recover one complete real provider file response, then resume the same paid revision."""

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
from template_factory.cli import recover_cognitive_framing  # noqa: E402
from template_factory.cognition import validate_file_plan  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
jid = "job_d502b67ef3874555b9bc49454bca9bb3"
job = s.job(jid)
if job["state"] != "failed" or job["attempt"] != 1 or job["error"] != "multiple cognitive objects":
    raise SystemExit("Only this recorded complete plan envelope failure is eligible.")
stage = pilot / "jobs" / jid / "attempt-1/blueprint-generate-1"
events = [json.loads(line) for line in (stage / "events.jsonl").read_text().splitlines()]
content = "\n".join(v["part"]["text"] for v in events if v.get("type") == "text")
result, recovery = recover_cognitive_framing(content)
assert recovery["method"] == "remove-one-premature-spec-closer"
validate_file_plan(result, allow_reuse=True)
recovery.update({
    "source_job": jid, "source_attempt": 1, "source_stage": "blueprint-generate-1",
    "session_ids": sorted({e.get("sessionID") for e in events if e.get("sessionID")}),
    "scope_note": "One framing brace removed from the complete final model proposal. No values edited, no specification regeneration call. Design preflight still required before file authoring.",
})
s.retry(jid)
j = s.claim("authorized-complete-file-format-recovery", "production")
s.checkpoint(
    jid, "blueprint-plan-1", {"result": result, "digest": digest(result)}, j["token"]
)
(Path(__file__).parent / "revision-6-plan-framing-recovery.json").write_text(
    json.dumps(recovery, ensure_ascii=False, indent=2)
)
(pilot / "revision-6-attempt-2-implementation.json").write_text(
    json.dumps(
        {
            "job_id": jid,
            "attempt": j["attempt"],
            "recovery": recovery,
            "sha256": {
                n: hashlib.sha256(
                    (pack / "template_factory" / n).read_bytes()
                ).hexdigest()
                for n in (
                    "cognition.py",
                    "cli.py",
                    "pipeline.py",
                    "store.py",
                    "blueprints.py",
                )
            },
        },
        ensure_ascii=False,
        indent=2,
    )
)
pipeline = Pipeline(s)
print(
    json.dumps(
        {"event": "revision_resumed_from_complete_plan", "attempt": j["attempt"]}
    ),
    flush=True,
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
            "event": "recovery_run_finished",
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
