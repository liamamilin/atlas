"""Fix two source-confirmed CommonJS interfaces in the authorized bookmark pilot."""
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
from template_factory.cli import CLI  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
out = Path(__file__).parent
s = FactoryStore(pilot, pack)
record = out / "revision-14-run.json"
if record.exists():
    raise SystemExit("Inspect/resume this exact repair rather than duplicate it.")
with s.connect() as con:
    assert not con.execute("select 1 from job where kind='blueprint-production' and state in ('queued','running')").fetchone()
original = next(a for a in s.artifacts() if a["id"] == "tpl_50cd6442ec4d41d3b161b54ac17742d0")
notes = (out / "REPAIR_14_NOTES.md").read_text()
batch = s.create_repair(original["id"], {
    "expected_digest": original["digest"], "model": "open-design/deepseek-v4.1-flash",
    "note": notes, "edit_paths": ["acceptance/ui-p1.cjs", "acceptance/browser.cjs"], "reuse_spec": True,
    "timeout": 1200, "language": "zh",
})
j = s.claim("authorized-bookmark-cjs-interface-repair", "production")
assert j["batch_id"] == batch["id"]
record.write_text(json.dumps({
    "job_id": j["id"], "batch_id": batch["id"], "original_artifact_id": original["id"],
    "original_digest": original["digest"], "note_sha256": hashlib.sha256(notes.encode()).hexdigest(),
    "scope": "Two literal CommonJS interface defects confirmed by independent review and host AST inspection: move one existing import, export one already implemented helper. Fixed normative design/research, two program files only. Prior review stays bound to its own immutable artifact. No generated program execution/publication.",
    "implementation_sha256": {n: hashlib.sha256((pack / "template_factory" / n).read_bytes()).hexdigest() for n in ("cognition.py", "cli.py", "pipeline.py", "store.py", "blueprints.py")},
}, ensure_ascii=False, indent=2))

class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name == "cognitive-review" else None
        return super().run(directory, prompt, model, timeout, cancelled, progress, reasoning_effort=effort)

p = Pipeline(s, cli=PilotCLI())
print(json.dumps({"event": "cjs_interface_repair_started", "job_id": j["id"]}), flush=True)
execute(s, j, p)
latest = s.job(j["id"])
print(json.dumps({"event": "production_finished", "state": latest["state"], "error": latest["error"]}, ensure_ascii=False), flush=True)
r = s.claim("authorized-bookmark-independent-full-review", "verification")
if r:
    print(json.dumps({"event": "independent_review_started", "job_id": r["id"]}), flush=True)
    execute(s, r, p)
print(json.dumps({"event": "round_finished"}), flush=True)
