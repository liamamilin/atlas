"""Resume the same pinned proposal with specification-only design review inputs."""

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
from template_factory.cli import CLI  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
jid = "job_d502b67ef3874555b9bc49454bca9bb3"
job = s.job(jid)
if job["state"] != "failed" or job["attempt"] != 3 or not job["error"].startswith("Cognition response reached the model output limit"):
    raise SystemExit("Only this recorded no-result reasoning-limit failure may resume.")
recovery = {"scope": "The same cached model plan is reused without changes. Design review now receives only current draft, architecture, research and revision requirements. Prior interrupted session is not a review result. No program execution."}
s.retry(jid)
j = s.claim("authorized-complete-file-format-recovery", "production")
(pilot / "revision-6-attempt-4-implementation.json").write_text(
    json.dumps(
        {
            "job_id": jid,
            "attempt": j["attempt"],
            "recovery": recovery,
            "review_effort": "low",
            "review_effort_scope": "Only blueprint-spec-review and cognitive-review; same provider/model, no global settings change. Actual request variant and reported token fields retained.",
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
class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name.startswith("blueprint-spec-review") or directory.name == "cognitive-review" else None
        return super().run(directory, prompt, model, timeout, cancelled, progress, reasoning_effort=effort)

pipeline = Pipeline(s, cli=PilotCLI())
print(
    json.dumps(
        {"event": "revision_resumed_with_explicit_review_effort", "attempt": j["attempt"]}
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
