"""Serialize the preserved independent assessment; never silently repair invalid JSON."""

import hashlib
import argparse
import json
import re
import sys

from develop import HERE, MODEL, ROOT, save

sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.cli import CLI  # noqa: E402

PROMPT = """You are a format-only serializer, NOT a new application evaluator. Read source/raw-assessment-segments.json and source/expected-verdicts.json. The segments contain the COMPLETE existing independent agent assessment with unescaped ASCII double-quotes inside prose. Concatenate the text values in numeric index order, WITHOUT adding any newline or space; segment boundaries are not content. This lossless representation avoids the read tool's 2000-character line truncation. Read ALL segments to the end before serializing. Serialize the entire existing assessment into valid JSON. Preserve its summary, all two rounds of nine verdicts/reasons/evidence, all followup entries, issues and limits without adding, removing or changing findings. Do not execute or reinterpret application behavior. Only fix quotation/JSON framing: embedded ASCII quotes must be escaped or represented as Chinese curly quotes. Return exactly one valid JSON object with the same top-level summary/rounds/followup/issues/limits schema, no code fence or commentary. The expected verdicts are externally extracted from intact id/outcome tokens and must match exactly. This is formatting of an existing assessment, not new independent runtime evidence."""


def main(attempt):
    original = HERE / "evaluation/outcome-review/cognitive-review"
    events = [json.loads(s) for s in (original / "events.jsonl").read_text().splitlines()]
    raw = "\n".join(
        (e.get("part") or {}).get("text") or e.get("text") or ""
        for e in events if e.get("type") == "text"
    ).strip()
    assert raw.startswith('{"summary"')
    split = raw.index('"id":"repaired"')
    pattern = r'"id"\s*:\s*"(R0[1-9])"\s*,\s*"outcome"\s*:\s*"(passed|partial|failed|unverified)"'
    expected = {
        "initial": dict(re.findall(pattern, raw[:split])),
        "repaired": dict(re.findall(pattern, raw[split:])),
    }
    assert len(re.findall(pattern, raw)) == 18
    assert all(len(rows) == 9 for rows in expected.values())
    assert attempt in {"format-repair", "format-repair-readable"}
    stage = HERE / "evaluation/outcome-review" / attempt / "cognitive-review"
    assert not stage.exists()
    (stage / "source").mkdir(parents=True)
    (stage / "source/raw-assessment.txt").write_text(raw)
    segments = [{"index": i // 800, "text": raw[i:i + 800]} for i in range(0, len(raw), 800)]
    assert "".join(s["text"] for s in segments) == raw
    save(stage / "source/raw-assessment-segments.json", {"segments": segments})
    save(stage / "source/expected-verdicts.json", expected)
    save(stage / "input.json", {
        "language": "zh", "source_inventory": ["source/raw-assessment-segments.json", "source/expected-verdicts.json"],
        "scope": "format-only; original review protocol failure remains failed",
    })
    (stage / "prompt.txt").write_text(PROMPT)
    save(HERE / "review-protocol-failure.json", {
        "status": "failed", "code": "cli_protocol", "stage": original.relative_to(HERE).as_posix(),
        "reason": "Independent assessment contains unescaped ASCII quotes in prose; strict JSON parsing failed. No automatic syntax heuristic applied.",
        "raw_assessment_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "preserved_verdicts": expected,
    })
    result = CLI().run(stage, PROMPT, MODEL, 600, lambda: False, lambda *a: None,
                       reasoning_effort="high")
    actual = {row["id"]: {r["id"]: r["outcome"] for r in row["required"]}
              for row in result["rounds"]}
    assert actual == expected and len(result["rounds"]) == 2
    assert all(len(r["required"]) == 9 for r in result["rounds"])
    assert set(result) == {"summary", "rounds", "followup", "issues", "limits"}
    save(HERE / "independent-outcome-review.json", result)
    save(HERE / "review-format-recovery.json", {
        "original_pipeline_status": "failed_protocol",
        "format_repair_status": "completed", "model": MODEL,
        "format_stage": stage.relative_to(HERE).as_posix(),
        "raw_assessment_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "all_18_verdicts_unchanged": True,
        "scope": "Model serialization only. Original independent review and raw failures preserved; not a new runtime test or reevaluation.",
    })
    print("Formatted assessment; all 18 original verdicts preserved", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--attempt", choices=["format-repair", "format-repair-readable"], default="format-repair")
    args = parser.parse_args()
    main(args.attempt)
