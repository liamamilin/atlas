"""Validate a real reviewer output's delimiters; no model call or program execution."""

import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore  # noqa: E402
from template_factory.pipeline import Pipeline  # noqa: E402
from template_factory.worker import execute  # noqa: E402
from template_factory.cli import recover_cognitive_framing  # noqa: E402
from template_factory.cognition import validate_review  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s = FactoryStore(pilot, pack)
source_id = "job_7e5ac324e71440ff8251d5447471ec2a"
a = next(a for a in s.artifacts() if a["id"] == "tpl_9f2aae2b2ee9455da6db67381c81b545")
if any(
    r.get("framing_recovery", {}).get("source_job") == source_id
    for r in a["acceptances"]
):
    raise SystemExit("Recovered report already recorded.")
source_job = s.job(source_id)
assert source_job["snapshot"]["artifact_digest"] == a["digest"]
path = pilot / "jobs" / source_id / "attempt-1/cognitive-review/events.jsonl"
rows = [json.loads(line) for line in path.read_text().splitlines()]
content = "\n".join(v["part"]["text"] for v in rows if v.get("type") == "text")
value, recovery = recover_cognitive_framing(content)
validate_review(value, pilot / a["bundle_path"] / "source")
recovery.update(
    {
        "source_job": source_id,
        "session_ids": sorted({r.get("sessionID") for r in rows if r.get("sessionID")}),
        "note": "Original independent reviewer session reused; no additional model call.",
    }
)


class RecoveredCLI:
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        assert (
            directory.name == "cognitive-review"
            and model == "open-design/deepseek-v4.1-flash"
        )
        (directory / "framing-recovery.json").write_text(
            json.dumps(recovery, ensure_ascii=False, indent=2)
        )
        return value


s.create_acceptance(
    a["id"],
    {
        "method": "cognitive-review",
        "expected_digest": a["digest"],
        "model": "open-design/deepseek-v4.1-flash",
        "language": "zh",
        "timeout": 1200,
    },
)
j = s.claim("validated-review-format-recovery", "verification")
execute(s, j, Pipeline(s, cli=RecoveredCLI()))
print(
    json.dumps(
        {
            "recovery_job": j["id"],
            "state": s.job(j["id"])["state"],
            "outcome": s.acceptances(a["id"])[0]["outcome"],
        },
        ensure_ascii=False,
    )
)
