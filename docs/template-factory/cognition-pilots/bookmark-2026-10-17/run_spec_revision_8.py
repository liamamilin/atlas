"""Continue a rejected model proposal through exact model-authored specification repair.

The carried review is BLOCKED evidence only. Every corrected proposal must receive
fresh independent design review before any program authoring. No generated code runs.
"""
import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore, digest
from template_factory.pipeline import Pipeline
from template_factory.worker import execute
from template_factory.cli import CLI
from template_factory.cognition import validate_file_plan

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
out = Path(__file__).parent
s = FactoryStore(pilot, pack)
parent_id = "job_14107dcca60746dcb549fc9d2412ea90"
parent = s.job(parent_id)
record_path = out / "revision-8-run.json"
if record_path.exists() or parent["state"] != "failed" or parent["attempt"] != 2:
    raise SystemExit("Inspect existing continuation or finish the previous round first.")
base = pilot / "jobs" / parent_id / "attempt-2"
plan = json.loads((base / "context/SPECIFICATION.json").read_text())
review = json.loads((base / "blueprint-spec-review-1/report.json").read_text())
assert review["outcome"] == "blocked" and review["proposal_digest"] == digest(plan)
validate_file_plan(plan, allow_reuse=True)
original = next(a for a in s.artifacts() if a["id"] == "tpl_231994f1a0a841d6b040d66de3287a6a")
notes = (out / "REPAIR_8_NOTES.md").read_text()
batch = s.create_repair(original["id"], {
    "expected_digest": original["digest"], "model": "open-design/deepseek-v4.1-flash",
    "note": notes, "timeout": 1200, "language": "zh", "reuse_spec": False,
    "edit_paths": ["acceptance/" + name for name in (
        "common.cjs", "run.cjs", "p0-limits.cjs", "p1-categories.cjs",
        "p2-search.cjs", "p0-library.cjs", "ui-p0.cjs", "ui-p1.cjs", "ui-p2.cjs", "README.md",
    )],
})
j = s.claim("authorized-bookmark-exact-spec-continuation", "production")
assert j["batch_id"] == batch["id"]
s.checkpoint(j["id"], "blueprint-plan-0", {"result": plan, "digest": digest(plan)}, j["token"])
carried = {**review, "reused_from": {
    "job_id": parent_id, "attempt": 2, "checkpoint": "blueprint-spec-review-1",
    "scope": "Exact prior model proposal and its blocked design finding retained unchanged as repair input. This is not a new review or acceptance; corrected proposal requires fresh reviews.",
}}
s.checkpoint(j["id"], "blueprint-spec-review-0", {"result": carried, "digest": digest(carried)}, j["token"])
record_path.write_text(json.dumps({
    "job_id": j["id"], "batch_id": batch["id"], "parent_job_id": parent_id,
    "original_artifact_id": original["id"], "original_digest": original["digest"],
    "seeded_model_proposal_digest": digest(plan), "carried_review_outcome": "blocked",
    "note_sha256": hashlib.sha256(notes.encode()).hexdigest(),
    "scope": "New bounded repair round seeded from unchanged prior model proposal plus blocked review only. Model supplies exact normative deltas; all corrected design dimensions reviewed afresh; ten existing programs eligible for revision. No application/program execution or publication.",
    "review_effort": "low", "review_effort_effectiveness": "Not assumed; previous monolithic attempt still exhausted 65536 reasoning tokens.",
    "implementation_sha256": {name: hashlib.sha256((pack / "template_factory" / name).read_bytes()).hexdigest() for name in ("cognition.py", "cli.py", "pipeline.py", "store.py", "blueprints.py")},
}, ensure_ascii=False, indent=2))

class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name.startswith("blueprint-spec-review") or directory.name == "cognitive-review" else None
        return super().run(directory, prompt, model, timeout, cancelled, progress, reasoning_effort=effort)

pipeline = Pipeline(s, cli=PilotCLI())
print(json.dumps({"event": "exact_spec_revision_started", "job_id": j["id"]}), flush=True)
execute(s, j, pipeline)
latest = s.job(j["id"])
print(json.dumps({"event": "exact_spec_revision_finished", "state": latest["state"], "error": latest["error"]}, ensure_ascii=False), flush=True)
review_job = s.claim("authorized-bookmark-revision-independent-review", "verification")
if review_job:
    print(json.dumps({"event": "independent_review_started", "job_id": review_job["id"]}), flush=True)
    execute(s, review_job, pipeline)
artifacts = [
    {"id": a["id"], "version": a["manifest"]["version"], "reviews": [(r["method"], r["outcome"]) for r in a["acceptances"]]}
    for a in s.artifacts() if a["job_id"] == j["id"]
]
print(json.dumps({"event": "revision_run_finished", "artifacts": artifacts}, ensure_ascii=False), flush=True)
