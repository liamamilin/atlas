"""Audit only this pilot's finished OpenCode sessions, never global history."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from atlas_runtime import atomic_json
from privacy import redact_text
from template_factory.api import get_store


def audit(stage, export):
    summary = json.loads((stage / "cli-summary.json").read_text())
    sid = summary.get("session_id")
    events = []
    if (stage / "events.jsonl").is_file():
        for line in (stage / "events.jsonl").read_text().splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    record = {"stage": str(stage.relative_to(ROOT)), "cli": summary,
              "websearch_calls": sum(e.get("type") in {"tool", "tool_use"} and (e.get("part") or {}).get("tool") == "websearch" for e in events),
              "webfetch_calls": sum(e.get("type") in {"tool", "tool_use"} and (e.get("part") or {}).get("tool") == "webfetch" for e in events)}
    receipt = stage / "session-audit.json"
    if export and sid and not receipt.exists():
        env = dict(os.environ)
        for key in ("OPENCODE_CONFIG", "OPENCODE_CONFIG_CONTENT", "OPENCODE_CONFIG_DIR"):
            env.pop(key, None)
        env.update(PWD=str(stage), OPENCODE_CONFIG=str(stage / "opencode.json"))
        result = subprocess.run([shutil.which("opencode"), "session", "export", "--standalone", sid],
                                cwd=stage, env=env, stdin=subprocess.DEVNULL,
                                capture_output=True, timeout=60)
        if result.returncode:
            record["export_error"] = redact_text(result.stderr.decode(errors="replace"))[-800:]
        else:
            value = json.loads(result.stdout)
            users = [m for m in value.get("messages", []) if m.get("type") == "user"]
            user_text = "\n".join(str(m.get("text", "")) for m in users)
            atomic_json(receipt, {
                "session_id": sid, "user_messages": len(users),
                "actual_input_sha256": hashlib.sha256(user_text.encode()).hexdigest(),
                "actual_input_characters": len(user_text),
                "inherited_driver_marker": "run_name='__main__')" in user_text,
                "assistant_usage_records": [{key: m.get(key) for key in ("id", "finish", "rawFinish", "tokens", "model")}
                                            for m in value.get("messages", []) if m.get("type") == "assistant"],
                "limits": "This owned session only. No full transcript, credentials or unrelated session exported. Usage fields may overlap; not an invoice.",
            })
    if receipt.exists():
        record["session_audit"] = json.loads(receipt.read_text())
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--export", action="store_true")
    args = parser.parse_args()
    run = json.loads((HERE / "run.json").read_text())
    store = get_store()
    job_ids = {run["production_job_id"], *run.get("additional_job_ids", [])}
    for artifact in store.artifacts():
        if artifact["job_id"] in job_ids:
            job_ids.update(j["id"] for j in artifact.get("acceptance_jobs", []))
    stages = set(HERE.rglob("cli-summary.json"))
    for job_id in job_ids:
        stages.update((store.root / "jobs" / job_id).rglob("cli-summary.json"))
    records = [audit(p.parent, args.export) for p in sorted(stages) if "source" not in p.relative_to(ROOT).parts]
    totals = dict.fromkeys(["input", "output", "reasoning", "cache_read", "cache_write"], 0)
    missing = 0
    for record in records:
        for message in record.get("session_audit", {}).get("assistant_usage_records", []):
            tokens = message.get("tokens")
            if not isinstance(tokens, dict):
                missing += 1
                continue
            for key in ("input", "output", "reasoning"):
                totals[key] += tokens.get(key, 0) or 0
            for key in ("read", "write"):
                totals["cache_" + key] += (tokens.get("cache") or {}).get(key, 0) or 0
    result = {"scope": "Only this trial's production, repair, author and independent review sessions, including failures.",
              "calls_with_session_id": sum(bool(r["cli"].get("session_id")) for r in records),
              "non_model_replays": sum(r["cli"].get("cli_status") == "replayed_prior_response" for r in records),
              "websearch_calls": sum(r["websearch_calls"] for r in records),
              "webfetch_calls": sum(r["webfetch_calls"] for r in records),
              "session_usage_fields": totals, "assistant_messages_missing_tokens": missing,
              "records": records,
              "limits": "Recorded token/cache/reasoning fields can overlap. No billed monetary total inferred. Missing exports/tokens are unavailable, not evidence of zero usage."}
    atomic_json(HERE / "usage.json", result)
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
