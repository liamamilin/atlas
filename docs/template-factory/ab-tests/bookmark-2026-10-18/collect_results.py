"""Collect reported fields without billing assumptions or exposing mapping to reviewers."""

import hashlib
import json
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def collect():
    results = {}
    for label in ["X", "Y"]:
        rounds = {}
        for stage in sorted((HERE / "control" / label).glob("*/scenario-review")):
            events_file = stage / "events.jsonl"
            events = [json.loads(s) for s in events_file.read_text().splitlines()] if events_file.exists() else []
            finishes = [e.get("part", {}) for e in events if e.get("type") == "step_finish"]
            tokens = {"input": 0, "output": 0, "reasoning": 0, "cache_read": 0, "cache_write": 0}
            for part in finishes:
                t = part.get("tokens", {})
                for key in ["input", "output", "reasoning"]:
                    tokens[key] += t.get(key, 0) or 0
                for key in ["read", "write"]:
                    tokens["cache_" + key] += (t.get("cache", {}) or {}).get(key, 0) or 0
            summary_file = stage / "cli-summary.json"
            summary = json.loads(summary_file.read_text()) if summary_file.exists() else None
            rounds[stage.parent.name] = {"cli_summary": summary, "reported_tokens": tokens, "step_finishes": len(finishes), "tool_calls": sum(e.get("type") in ["tool_use", "tool"] for e in events), "error_events": sum(e.get("type") == "error" for e in events), "final_stop_usage_event_observed": bool(finishes and finishes[-1].get('reason') in ['stop','end_turn','end-turn']), "cli_completed_without_error": bool(summary and summary['exit_code'] == 0 and not any(e.get('type')=='error' for e in events)), "visible_search_calls": sum(e.get('type') in ['tool_use','tool'] and e.get('part',{}).get('tool') in ['websearch','webfetch'] for e in events), "caveat": "Reported fields may overlap; no unique billed total inferred; cost=0 does not mean free. Nonzero exits or missing final step_finish can omit final usage; reported values are not a complete bill."}
            source = HERE / "blind" / label / stage.parent.name / "app"
            if source.exists():
                export = HERE / f"application-{label}-{stage.parent.name}.zip"
                with zipfile.ZipFile(export, "w", zipfile.ZIP_DEFLATED) as z:
                    for p in sorted(source.rglob("*")):
                        if p.is_file() and "__pycache__" not in p.parts:
                            z.write(p, p.relative_to(source).as_posix())
                rounds[stage.parent.name]["export"] = {"file": export.name, "sha256": hashlib.sha256(export.read_bytes()).hexdigest()}
        results[label] = rounds
    (HERE / "control" / "metrics.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    collect()
