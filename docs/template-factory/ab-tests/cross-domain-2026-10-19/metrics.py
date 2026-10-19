"""Visible usage and content access, without pretending they are unique billing."""

import json
from pathlib import Path

from prepare import HERE, save


def collect(stage):
    raw = (stage / "events.jsonl").read_bytes()
    lines = raw.split(b"\n")
    incomplete_tail = len(lines.pop())
    events, malformed = [], []
    for index, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except (ValueError, UnicodeDecodeError):
            malformed.append(index)
    usage = {key: 0 for key in ["input", "output", "reasoning", "cache_read", "cache_write"]}
    finishes = []
    reads = []
    for event in events:
        part = event.get("part") or {}
        if event.get("type") == "step_finish":
            finishes.append(part)
            tokens = part.get("tokens") or {}
            for key in ["input", "output", "reasoning"]:
                usage[key] += tokens.get(key, 0) or 0
            for key in ["read", "write"]:
                usage["cache_" + key] += (tokens.get("cache") or {}).get(key, 0) or 0
        if event.get("type") not in {"tool", "tool_use"} or part.get("tool") != "read":
            continue
        state = part.get("state") or {}
        args = state.get("input") or {}
        name = str(args.get("path") or args.get("filePath") or "")
        file = Path(name)
        if not file.is_absolute():
            file = stage / file
        try:
            name = file.resolve().relative_to(stage.resolve()).as_posix()
        except ValueError:
            name = "outside-owned-stage (do not infer permitted content)"
        output = state.get("output")
        text = output if isinstance(output, str) else ""
        reads.append({"file": name, "status": state.get("status"),
            "offset": args.get("offset"), "limit": args.get("limit"),
            "returned_characters_including_tool_framing": len(text) if output is not None else None,
            "line_truncation_observed": "line truncated" in text,
            "template_material": name.startswith("source/product-context/") or name == "source/FULL_TEMPLATE.md"})
    summary = stage / "cli-summary.json"
    freeze = stage / "input-freeze.json"
    input_receipt = stage / "actual-user-input.json"
    session_usage = None
    if input_receipt.exists():
        records = json.loads(input_receipt.read_text()).get("assistant_usage_records", [])
        if records:
            fields = dict.fromkeys(usage, 0)
            for record in records:
                tokens = record.get("tokens") or {}
                for key in ["input", "output", "reasoning"]:
                    fields[key] += tokens.get(key, 0) or 0
                for key in ["read", "write"]:
                    fields["cache_" + key] += (tokens.get("cache") or {}).get(key, 0) or 0
            session_usage = {"fields": fields,
                "terminal_finish": records[-1].get("finish"),
                "assistant_messages": len(records),
                "messages_missing_tokens": sum(not isinstance(r.get("tokens"), dict) for r in records),
                "limits": "Overlaps event usage; includes stored terminal message when available. Not a billing invoice or unique input/cache total."}
    return {"incomplete_live_tail_bytes": incomplete_tail,
        "malformed_complete_event_line_numbers": malformed,
        "cli": json.loads(summary.read_text()) if summary.exists() else None,
        "failure": json.loads((stage / "failure.json").read_text()) if (stage / "failure.json").exists() else None,
        "visible_usage_fields": usage,
        "session_export_usage": session_usage,
        "final_usage_event_observed": bool(finishes and finishes[-1].get("reason") in {"stop", "end_turn", "end-turn"}),
        "web_tool_calls": sum(e.get("type") in {"tool", "tool_use"} and (e.get("part") or {}).get("tool") in {"websearch", "webfetch"} for e in events),
        "read_events": reads,
        "template_read_events": sum(r["template_material"] for r in reads),
        "template_completed_read_events": sum(r["template_material"] and r["status"] == "completed" for r in reads),
        "distinct_template_files_read": sorted({r["file"] for r in reads if r["template_material"] and r["status"] == "completed"}),
        "read_truncations": sum(r["line_truncation_observed"] for r in reads),
        "initial_input": json.loads(freeze.read_text()) if freeze.exists() and "/runs/" in str(stage) else None}


def main():
    result = {}
    for events in sorted(HERE.rglob("events.jsonl")):
        stage = events.parent
        if "source" in stage.relative_to(HERE).parts:
            continue
        result[stage.relative_to(HERE).as_posix()] = collect(stage)
    save(HERE / "metrics.json", {
        "scope": "Per call: research/template production, application initial/retry/repair, independent review. Failed calls retained.",
        "limits": ["Visible input/output/reasoning/cache fields may overlap; final usage event can be absent. Not unique billed tokens or money.",
                   "Read-event character counts include tool framing/redaction and repeat reads; no equality with LLM tokens. Truncations are reported, not assumed full coverage.",
                   "Native file-attachment byte/hash receipt proves what was supplied, not that every byte became provider context; inspect actual events/usage before claiming smaller effective context.",
                   "One initial generation per cell; provider load/caching and concurrency affect elapsed time. Do not pool case difficulty into a universal winner."],
        "calls": result,
    })
    print("Collected", len(result), "owned model calls")


if __name__ == "__main__":
    main()
