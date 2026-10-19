"""Collect safe local pilot evidence; never invokes a model or executes package code."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.store import FactoryStore  # noqa: E402
from template_factory.blueprints import verify_frozen  # noqa: E402
from privacy import redact_value  # noqa: E402

pilot = pack / "atlas/template-factory/cognition-pilots/bookmark-2026-10-17"
out = Path(__file__).resolve().parent
store = FactoryStore(pilot, pack)
summary = {
    "model": "open-design/deepseek-v4.1-flash",
    "calls": [],
    "call_count_definition": "Each entry is a CLI invocation/session, not an underlying provider request; tool loops can contain multiple model turns.",
    "artifacts": [],
    "jobs": [],
    "scope": "Real one-case automatic production and independent static review. No application tests, grade promotion or publication.",
}
summary["syntax_tool_version"] = subprocess.run(
    ["node", "--version"], capture_output=True, text=True, check=True
).stdout.strip()
with store.connect() as con:
    for row in con.execute(
        "select id,kind,state,stage,attempt,error from job order by created_at"
    ):
        summary["jobs"].append(dict(row))
if any(j["state"] in ("queued", "running") for j in summary["jobs"]):
    raise SystemExit(
        "Pilot still active; do not publish a partial result as completion."
    )
if (pilot / "jobs/design-probe/attempt-1/active").exists():
    raise SystemExit("Design probe is still active; do not collect a partial result.")
for path in sorted(pilot.glob("jobs/**/events.jsonl")):
    record_path = path.parent / "cli-summary.json"
    value = (
        json.loads(record_path.read_text())
        if record_path.exists()
        else {
            "model": summary["model"],
            "incomplete_call": True,
        }
    )
    events = [json.loads(s) for s in path.read_text().splitlines()]
    calls = Counter()
    usage = Counter()
    for event in events:
        part = event.get("part", {})
        if event.get("type") == "tool_use":
            calls[(part.get("tool"), part.get("state", {}).get("status"))] += 1
        if event.get("type") == "step_finish":
            tokens = part.get("tokens", {})
            for key in ("input", "output", "reasoning"):
                if isinstance(tokens.get(key), (int, float)):
                    usage[key] += tokens[key]
            for key in ("read", "write"):
                cache_count = tokens.get("cache", {}).get(key)
                if isinstance(cache_count, (int, float)):
                    usage["cache_" + key] += cache_count
    summary["calls"].append(
        {
            **value,
            "session_ids": sorted(
                {e.get("sessionID") for e in events if e.get("sessionID")}
            ),
            "finish_reasons": [
                e.get("part", {}).get("reason")
                for e in events
                if e.get("type") == "step_finish"
            ],
            "stage": path.parent.name,
            "attempt": path.parent.parent.name,
            "job_id": path.parent.parent.parent.name,
            "registered_job": path.parent.parent.parent.name
            in {job["id"] for job in summary["jobs"]},
            "tools": [
                {"tool": k[0], "status": k[1], "count": v}
                for k, v in sorted(calls.items())
            ],
            "reported_token_fields": dict(usage),
        }
    )
observed_fields = {
    key for call in summary["calls"] for key in call["reported_token_fields"]
}
summary["reported_token_fields"] = {
    key: sum(call["reported_token_fields"].get(key, 0) for call in summary["calls"])
    for key in sorted(observed_fields)
}
summary["usage_definition"] = (
    "Sums of OpenCode step_finish token fields across all retained sessions, including failures/retries. Input/cache/reasoning fields may overlap by provider; this is not unique billed tokens or a price estimate. Missing final events can undercount interrupted calls. Reported cost=0 is not treated as free."
)
artifacts = store.artifacts()
artifact_by_id = {artifact["id"]: artifact for artifact in artifacts}
for artifact in artifacts:
    bundle = pilot / artifact["bundle_path"]
    spec = verify_frozen(bundle, artifact["digest"])
    archive = pilot / artifact["archive_path"]
    name = artifact["id"] + ".zip"
    shutil.copy2(archive, out / name)
    record = {
        k: artifact.get(k)
        for k in (
            "id",
            "job_id",
            "artifact_type",
            "digest",
            "level",
            "state",
            "manifest",
            "formal_checks",
            "supersedes",
            "acceptances",
        )
    }
    record.update(
        {
            "archive": name,
            "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
            "research_source_count": len(spec["sources"]) - 1,
            "scenario": spec["scenario"],
            "programs_executed": False,
        }
    )
    provenance = artifact.get("provenance", {})
    record["production_scope"] = {
        key: provenance.get(key)
        for key in ("origin", "model", "edit_paths", "reuse_spec")
    }
    if provenance.get("edit_paths") is not None:
        parent = artifact_by_id[artifact["supersedes"]]
        old_source = pilot / parent["bundle_path"] / "source"
        old_spec = verify_frozen(old_source.parent, parent["digest"])
        preserved = []
        for prior in sorted(old_source.rglob("*")):
            if not prior.is_file():
                continue
            name = prior.relative_to(old_source).as_posix()
            if (
                not name.startswith(("acceptance/", "references/"))
                or name == "acceptance/plan.json"
                or name in provenance["edit_paths"]
            ):
                continue
            if prior.read_bytes() != (bundle / "source" / name).read_bytes():
                raise SystemExit("Unselected program changed: " + name)
            preserved.append(name)
        record["scope_integrity"] = {
            "passed": True,
            "byte_identical_programs": preserved,
        }
        if provenance.get("reuse_spec"):
            for key in (
                "title",
                "roles",
                "features",
                "decisions",
                "phases",
                "acceptance",
                "architecture_markdown",
                "limits",
                "research",
            ):
                if spec[key] != old_spec[key]:
                    raise SystemExit("Pinned specification changed: " + key)
            record["scope_integrity"]["authored_spec_identical"] = True
    record["syntax_checks"] = []
    for program in sorted((bundle / "source/acceptance").rglob("*.cjs")):
        checked = subprocess.run(
            ["node", "--check", str(program)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        record["syntax_checks"].append(
            {
                "file": program.relative_to(bundle / "source").as_posix(),
                "sha256": hashlib.sha256(program.read_bytes()).hexdigest(),
                "passed": checked.returncode == 0,
                "diagnostic": checked.stderr,
                "scope": "node --check syntax only; program was not executed against any application.",
            }
        )
    summary["artifacts"].append(record)
(out / "result.json").write_text(
    json.dumps(redact_value(summary), ensure_ascii=False, indent=2) + "\n"
)
print(
    json.dumps(
        {
            "jobs": [(j["kind"], j["state"]) for j in summary["jobs"]],
            "artifacts": [
                (a["id"], [(r["method"], r["outcome"]) for r in a["acceptances"]])
                for a in summary["artifacts"]
            ],
            "calls": len(summary["calls"]),
        },
        ensure_ascii=False,
    )
)
