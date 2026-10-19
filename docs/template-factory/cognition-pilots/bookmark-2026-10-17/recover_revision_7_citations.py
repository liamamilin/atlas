"""Recover only exact source-prefix citations in a complete independent review."""
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
from template_factory.cognition import validate_review
from template_factory.artifacts import tree_manifest
pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
out = Path(__file__).parent
s = FactoryStore(pilot, pack)
jid = "job_14107dcca60746dcb549fc9d2412ea90"
j = s.job(jid)
if j["state"] != "failed" or j["attempt"] != 1 or j["error"] != "review cites nonexistent source file":
    raise SystemExit("Only this complete prefix-citation failure can recover.")
source = pilot / "jobs" / jid / "attempt-1/blueprint-spec-review-1-product_completeness"
raw_bytes = (source / "result.json").read_bytes()
raw = json.loads(raw_bytes)
input_data = json.loads((source / "input.json").read_text())
part = validate_review(raw, source / "source", ("product_completeness",))
assert part.get("citation_aliases") == [
    {"reported": "source/DRAFT.md", "canonical": "DRAFT.md"},
    {"reported": "source/ARCHITECTURE.md", "canonical": "ARCHITECTURE.md"},
]
assert input_data["projection_digest"] == digest(tree_manifest(source / "source"))
part.update({
    "scope": "Independent static design review of declared proposal projection only; no program review, execution or publication.",
    "proposal_digest": input_data["proposal_digest"],
    "projection_digest": input_data["projection_digest"],
    "stage": source.name,
    "citation_recovery": {"source_job": jid, "source_attempt": 1, "raw_report_sha256": hashlib.sha256(raw_bytes).hexdigest(), "scope": "Only exact source/ aliases normalized to provided files. Finding, outcome and reasoning unchanged. No additional model call."},
})
s.retry(jid)
j = s.claim("authorized-review-citation-recovery", "production")
s.checkpoint(jid, "blueprint-design-check-1-product_completeness", {"result": part, "digest": digest(part)}, j["token"])
(out / "revision-7-citation-recovery.json").write_text(json.dumps(part,ensure_ascii=False,indent=2))
(out / "revision-7-attempt-2-implementation.json").write_text(json.dumps({"job_id":jid,"attempt":j["attempt"],"sha256":{name:hashlib.sha256((pack/"template_factory"/name).read_bytes()).hexdigest() for name in ("cognition.py","cli.py","pipeline.py","store.py","blueprints.py")}},indent=2))
class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name.startswith("blueprint-spec-review") or directory.name == "cognitive-review" else None
        return super().run(directory,prompt,model,timeout,cancelled,progress,reasoning_effort=effort)
pipeline = Pipeline(s,cli=PilotCLI())
print(json.dumps({"event":"same_review_recovered","job_id":jid,"attempt":j["attempt"]}),flush=True)
execute(s,j,pipeline)
latest=s.job(jid)
print(json.dumps({"event":"revision_finished","state":latest["state"],"error":latest["error"]},ensure_ascii=False),flush=True)
review=s.claim("authorized-bookmark-independent-review","verification")
if review:
    print(json.dumps({"event":"independent_review_started","job_id":review["id"]}),flush=True)
    execute(s,review,pipeline)
print(json.dumps({"event":"recovery_run_finished"}),flush=True)
