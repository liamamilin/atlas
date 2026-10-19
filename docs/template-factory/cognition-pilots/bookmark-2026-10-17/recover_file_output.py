"""Recover one complete real provider file response, then resume the same paid revision."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore, digest  # noqa: E402
from template_factory.pipeline import Pipeline  # noqa: E402
from template_factory.worker import execute  # noqa: E402
from template_factory.cli import recover_cognitive_framing  # noqa: E402
from template_factory.cognition import apply_file_response  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
jid = "job_4acc2b952d174c9a8fc06cfa706bf183"
job = s.job(jid)
if job["state"] != "failed" or job["attempt"] != 2:
    raise SystemExit(
        "Only the recorded complete attempt-2 support response is eligible."
    )
stage = pilot / "jobs" / jid / "attempt-2/blueprint-code-0-1"
events = [
    json.loads(line) for line in (stage / "events.jsonl").read_text().splitlines()
]
content = "\n".join(v["part"]["text"] for v in events if v.get("type") == "text")
value, recovery = recover_cognitive_framing(content)
result = apply_file_response(value, "acceptance/support.cjs")
with tempfile.TemporaryDirectory(prefix="atlas-cognition-syntax-") as temp:
    check = Path(temp) / "support.cjs"
    check.write_text(result["content"])
    subprocess.run(["node", "--check", str(check)], check=True)
recovery.update(
    {
        "source_job": jid,
        "source_attempt": 2,
        "source_stage": "blueprint-code-0-1",
        "session_ids": sorted(
            {e.get("sessionID") for e in events if e.get("sessionID")}
        ),
        "content_sha256": hashlib.sha256(result["content"].encode()).hexdigest(),
        "scope_note": "No file contents changed; no model call to regenerate this response. Syntax checked only.",
    }
)
result["framing_recovery"] = recovery
s.retry(jid)
j = s.claim("authorized-complete-file-format-recovery", "production")
s.checkpoint(
    jid, "blueprint-code-0-1", {"result": result, "digest": digest(result)}, j["token"]
)
(Path(__file__).parent / "support-framing-recovery.json").write_text(
    json.dumps(recovery, ensure_ascii=False, indent=2)
)
(pilot / "revision-attempt-3-implementation.json").write_text(
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
        {"event": "revision_resumed_from_complete_file", "attempt": j["attempt"]}
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
