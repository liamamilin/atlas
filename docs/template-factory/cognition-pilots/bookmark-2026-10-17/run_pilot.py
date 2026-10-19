"""Authorized one-case OpenCode production pilot. Running invokes a paid provider."""

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
if (pilot / "factory.sqlite").exists():
    raise SystemExit(
        "Pilot already exists; inspect evidence before any retry. Do not duplicate calls."
    )
store = FactoryStore(pilot, pack)
scenario = json.loads(
    (
        root / "docs/template-factory/blueprints/bookmark-personal/inputs/scenario.json"
    ).read_text()
)
scene = store.save_scenario(scenario)
batch = store.create_batch(
    {
        "kind": "blueprint-production",
        "name": "书签认知流水线真实试产",
        "model": "open-design/deepseek-v4.1-flash",
        "language": "zh",
        "concurrency": 1,
        "timeout": 1200,
        "repair_attempts": 1,
        "scenario_ids": [scene["id"]],
        "scenario_revisions": {scene["id"]: scene["revision"]},
    }
)
(pilot / "pilot-scope.json").write_text(
    json.dumps(
        {
            "authorized_material": "bookmark leaf, confirmed life-purchase/inspiration scenario, public research, generated cognition and scoped failure/review findings",
            "model": "open-design/deepseek-v4.1-flash",
            "publication": False,
            "batch_id": batch["id"],
            "implementation_sha256": {
                name: hashlib.sha256(
                    (pack / "template_factory" / name).read_bytes()
                ).hexdigest()
                for name in (
                    "cognition.py",
                    "pipeline.py",
                    "store.py",
                    "cli.py",
                    "blueprints.py",
                )
            },
        },
        ensure_ascii=False,
        indent=2,
    )
)
print(json.dumps({"event": "production_started", "batch": batch["id"]}), flush=True)
pipeline = Pipeline(store)
job = store.claim("authorized-bookmark-pilot", "production")
execute(store, job, pipeline)
print(
    json.dumps(
        {
            "event": "production_finished",
            "job": store.job(job["id"])["state"],
            "error": store.job(job["id"])["error"],
        },
        ensure_ascii=False,
    ),
    flush=True,
)
review = store.claim("authorized-bookmark-review", "verification")
if review:
    print(
        json.dumps({"event": "independent_review_started", "job": review["id"]}),
        flush=True,
    )
    execute(store, review, pipeline)
summary = {
    "event": "pilot_finished",
    "artifacts": [
        {
            "id": a["id"],
            "state": a["state"],
            "type": a.get("artifact_type"),
            "acceptances": [
                {
                    "method": v["method"],
                    "outcome": v["outcome"],
                    "summary": v.get("summary"),
                }
                for v in a["acceptances"]
            ],
        }
        for a in store.artifacts()
    ],
}
(pilot / "pilot-result.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2)
)
print(json.dumps(summary, ensure_ascii=False), flush=True)
