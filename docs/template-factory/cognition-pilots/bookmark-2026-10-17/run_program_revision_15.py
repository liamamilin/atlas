"""Verify server-side HTML confirmation safety in the authorized fixed-design pilot."""
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
record = out / "revision-15-run.json"
if record.exists():
    raise SystemExit("Inspect/resume this exact repair rather than duplicate it.")
with s.connect() as con:
    assert not con.execute("select 1 from job where kind='blueprint-production' and state in ('queued','running')").fetchone()
original = next(a for a in s.artifacts() if a["id"] == "tpl_161c545d749e4a57b8e9f2f423c1c918")
notes = (out / "REPAIR_15_NOTES.md").read_text()
batch = s.create_repair(original["id"], {
    "expected_digest": original["digest"], "model": "open-design/deepseek-v4.1-flash",
    "note": notes, "edit_paths": ["acceptance/p1-trash.cjs", "acceptance/README.md"], "reuse_spec": True,
    "timeout": 1200, "language": "zh",
})
j = s.claim("authorized-bookmark-server-confirmation-repair", "production")
assert j["batch_id"] == batch["id"]
record.write_text(json.dumps({
    "job_id": j["id"], "batch_id": batch["id"], "original_artifact_id": original["id"],
    "original_digest": original["digest"], "note_sha256": hashlib.sha256(notes.encode()).hexdigest(),
    "scope": "Confirmed missing direct HTTP HTML confirmation negatives; add only unconfirmed requests and zero-write/readback assertions, plus manual global-clear positive instructions. Fixed normative design/research, two files only. Prior redundant review cancelled without a verdict. No generated program execution/publication.",
    "implementation_sha256": {n: hashlib.sha256((pack / "template_factory" / n).read_bytes()).hexdigest() for n in ("cognition.py", "cli.py", "pipeline.py", "store.py", "blueprints.py")},
}, ensure_ascii=False, indent=2))

class PilotCLI(CLI):
    def run(self, directory, prompt, model, timeout, cancelled, progress):
        effort = "low" if directory.name == "cognitive-review" else None
        return super().run(directory, prompt, model, timeout, cancelled, progress, reasoning_effort=effort)

p = Pipeline(s, cli=PilotCLI())
print(json.dumps({"event": "server_confirmation_repair_started", "job_id": j["id"]}), flush=True)
execute(s, j, p)
latest = s.job(j["id"])
print(json.dumps({"event": "production_finished", "state": latest["state"], "error": latest["error"]}, ensure_ascii=False), flush=True)
r = s.claim("authorized-bookmark-independent-full-review", "verification")
if r:
    print(json.dumps({"event": "independent_review_started", "job_id": r["id"]}), flush=True)
    execute(s, r, p)
print(json.dumps({"event": "round_finished"}), flush=True)
