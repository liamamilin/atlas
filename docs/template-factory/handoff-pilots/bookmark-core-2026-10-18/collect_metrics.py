"""Reported CLI fields only; never infer unique billed tokens."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    result = {}
    for root in ["production", "development", "repair", "repair-recovery", "evaluation/outcome-review"]:
        for stage in sorted((HERE / root).rglob("events.jsonl")):
            events = [
                json.loads(line)
                for line in stage.read_text().splitlines()
                if line.strip()
            ]
            finishes = [
                event.get("part", {})
                for event in events
                if event.get("type") == "step_finish"
            ]
            tokens = {
                key: 0
                for key in ["input", "output", "reasoning", "cache_read", "cache_write"]
            }
            for part in finishes:
                reported = part.get("tokens", {})
                for key in ["input", "output", "reasoning"]:
                    tokens[key] += reported.get(key, 0) or 0
                for key in ["read", "write"]:
                    tokens["cache_" + key] += (reported.get("cache") or {}).get(
                        key, 0
                    ) or 0
            summary = stage.parent / "cli-summary.json"
            name = stage.parent.relative_to(HERE).as_posix()
            status = "summary_available" if summary.exists() else "summary_missing"
            if name == "repair/scenario-review" and (HERE / "repair-interruption.json").exists():
                status = "interrupted_no_exit_status_captured"
            if name == "evaluation/outcome-review/cognitive-review" and (HERE / "review-protocol-failure.json").exists():
                status = "failed_json_protocol"
            if (stage.parent / "format-input-failure.json").exists():
                status = "stopped_unreadable_long_line_input"
            result[name] = {
                "status": status,
                "cli": json.loads(summary.read_text()) if summary.exists() else None,
                "visible_fields": tokens,
                "tool_calls": sum(
                    e.get("type") in {"tool", "tool_use"} for e in events
                ),
                "search_or_fetch_calls": sum(
                    e.get("type") in {"tool", "tool_use"}
                    and (e.get("part") or {}).get("tool") in {"websearch", "webfetch"}
                    for e in events
                ),
                "error_events": sum(e.get("type") == "error" for e in events),
                "final_stop_usage_event_observed": bool(
                    finishes
                    and finishes[-1].get("reason") in {"stop", "end_turn", "end-turn"}
                ),
            }
    output = {
        "scope": "cognitive production, initial development, interrupted repair, recovery, independent review and format-only repair are separate entries",
        "caveat": "Visible fields may overlap and the final usage event may be missing. Do not add them into unique billed tokens or interpret cost=0 as free. Historical speed/cost changes are confounded by new scope, stack default, model variability and provider state.",
        "calls": result,
    }
    (HERE / "metrics.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    )
    print("collected", len(result), "calls")


if __name__ == "__main__":
    main()
