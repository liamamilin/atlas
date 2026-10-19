"""Repair the frozen candidate using actual blocked review evidence; never run it."""
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
from template_factory.cognition import scoped_file_plan, validate_file_plan
from template_factory.blueprints import verify_frozen

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
out = Path(__file__).parent
s = FactoryStore(pilot, pack)
record_path = out / "revision-10-run.json"
recovered_job = None
if record_path.exists():
    prior_record = json.loads(record_path.read_text())
    old = s.job(prior_record["job_id"])
    if old["state"] != "failed" or old["error"] != "'summary'" or list((pilot / "jobs" / old["id"]).rglob("events.jsonl")):
        raise SystemExit("This bounded round already exists; inspect it rather than duplicate.")
    recovered_job = old["id"]
    record_path = out / "revision-10-protocol-retry-run.json"
    if record_path.exists():
        raise SystemExit("Inspect the protocol retry; do not duplicate it.")
with s.connect() as con:
    assert not con.execute("select 1 from job where state in ('queued','running')").fetchone()
original = next(a for a in s.artifacts() if a["id"] == "tpl_276b787582b44503868a308519cc14a4")
source = pilot / original["bundle_path"] / "source"
spec = verify_frozen(source.parent, original["digest"])
base = pilot / "jobs" / original["job_id"] / "attempt-2"
plan = json.loads((base / "context/SPECIFICATION.json").read_text())
for key, value in plan["spec"].items():
    assert value == spec[key], key
review = json.loads((pilot / "jobs/job_f9f174ddf366488f998cc549a483dcf4/attempt-1/cognitive-review/result.json").read_text())
assert any(c["outcome"] == "blocked" for c in review["checks"])
selected = ["acceptance/p0-limits.cjs", "acceptance/p1-edit.cjs"]
plan["file_plan"] = scoped_file_plan(plan["file_plan"], source, selected)
validate_file_plan(plan, allow_reuse=True)
notes = (out / "REPAIR_10_NOTES.md").read_text()
batch = s.create_repair(original["id"], {
    "expected_digest": original["digest"], "model": "open-design/deepseek-v4.1-flash",
    "note": notes, "timeout": 1200, "language": "zh", "reuse_spec": False,
    "edit_paths": selected,
})
j = s.claim("authorized-bookmark-candidate-consistency-repair", "production")
assert j["batch_id"] == batch["id"]
s.checkpoint(j["id"], "blueprint-plan-0", {"result": plan, "digest": digest(plan)}, j["token"])
dimensions = {"scenario_scope", "product_completeness", "architecture_contract", "phase_acceptance", "decisions_defaults"}
carried = {
    "summary": review["summary"], "suggestions": review.get("suggestions", []),
    "outcome": "blocked", "checks": [c for c in review["checks"] if c["dimension"] in dimensions],
    "proposal_digest": digest(plan),
    "scope": "Actual frozen-candidate review retained as BLOCKED repair input only; not a fresh design check. Corrected proposal must receive all five new independent reviews.",
    "reused_from": {"job_id": "job_f9f174ddf366488f998cc549a483dcf4", "artifact_id": original["id"], "digest": original["digest"]},
}
s.checkpoint(j["id"], "blueprint-spec-review-0", {"result": carried, "digest": digest(carried)}, j["token"])
record_path.write_text(json.dumps({
    "job_id": j["id"], "batch_id": batch["id"], "original_artifact_id": original["id"],
    "original_digest": original["digest"], "seeded_proposal_digest": digest(plan),
    "carried_review_outcome": "blocked", "edit_paths": selected,
    "previous_no_model_schema_failure": recovered_job,
    "note_sha256": hashlib.sha256(notes.encode()).hexdigest(),
    "scope": "Exact prior frozen normative values; host only applies two-file reuse policy to inventory. Actual blocked full review as repair input. Model authors local normative deltas, then fresh design preflight, two programs, frozen full review. No generated program execution or publication.",
    "implementation_sha256": {name: hashlib.sha256((pack / "template_factory" / name).read_bytes()).hexdigest() for name in ("cognition.py", "cli.py", "pipeline.py", "store.py", "blueprints.py")},
}, ensure_ascii=False, indent=2))

class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name.startswith("blueprint-spec-review") or directory.name == "cognitive-review" else None
        return super().run(directory, prompt, model, timeout, cancelled, progress, reasoning_effort=effort)

p = Pipeline(s, cli=PilotCLI())
print(json.dumps({"event": "consistency_repair_started", "job_id": j["id"]}), flush=True)
execute(s, j, p)
latest = s.job(j["id"])
print(json.dumps({"event": "production_finished", "state": latest["state"], "error": latest["error"]}, ensure_ascii=False), flush=True)
r = s.claim("authorized-bookmark-independent-candidate-review", "verification")
if r:
    print(json.dumps({"event": "independent_review_started", "job_id": r["id"]}), flush=True)
    execute(s, r, p)
print(json.dumps({"event": "round_finished"}), flush=True)
