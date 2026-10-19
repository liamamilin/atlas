"""Retry same immutable proposal with version-locked addressed field edits."""
import hashlib
import json
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[4]
pack=root/"application-atlas-production-pack"
sys.path.insert(0,str(pack))
from template_factory.store import FactoryStore
from template_factory.pipeline import Pipeline
from template_factory.worker import execute
from template_factory.cli import CLI
pilot=pack/"atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
s=FactoryStore(pilot,pack)
jid="job_1ac8dcd3b5ef458ba09f9194c2081892"
j=s.job(jid)
if j["state"]!="failed" or j["attempt"]!=1 or not j["error"].startswith("spec field value changed"):
    raise SystemExit("Only this exact-guard failure may retry.")
assert s.checkpoint(jid,"blueprint-plan-1") is None
s.retry(jid)
j=s.claim("authorized-version-locked-spec-retry","production")
(Path(__file__).parent/"revision-9-attempt-2-implementation.json").write_text(json.dumps({
    "job_id":jid,"attempt":j["attempt"],"scope":"Same immutable model proposal and blocked review. Model may address an existing field only with the exact whole-proposal digest. Architecture still requires unique literal spans; identity/source/status/inventory guards retained. No fuzzy recovery of the rejected responses; they remain original evidence.",
    "sha256":{name:hashlib.sha256((pack/"template_factory"/name).read_bytes()).hexdigest() for name in ("cognition.py","cli.py","pipeline.py","store.py","blueprints.py")},
},indent=2))
class PilotCLI(CLI):
    def run(self,directory,prompt,model,timeout,cancelled,progress):
        effort="low" if directory.name.startswith("blueprint-spec-review") or directory.name=="cognitive-review" else None
        return super().run(directory,prompt,model,timeout,cancelled,progress,reasoning_effort=effort)
p=Pipeline(s,cli=PilotCLI())
print(json.dumps({"event":"version_locked_spec_retry_started","job_id":jid,"attempt":j["attempt"]}),flush=True)
execute(s,j,p)
latest=s.job(jid)
print(json.dumps({"event":"revision_finished","state":latest["state"],"error":latest["error"]},ensure_ascii=False),flush=True)
r=s.claim("authorized-independent-bookmark-review","verification")
if r:
    print(json.dumps({"event":"independent_review_started","job_id":r["id"]}),flush=True)
    execute(s,r,p)
print(json.dumps({"event":"revision_run_finished"}),flush=True)
