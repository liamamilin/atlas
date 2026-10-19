"""Bounded OpenCode Go checks using synthetic input only, not product validation."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from atlas_runtime import atomic_json
from privacy import redact_text
from template_factory.cli import CLI

MODELS = [
    "opencode-go/longcat-2.5-preview-free",
    "opencode-go/beam-free",
    "opencode-go/deepseek-v4.1-flash",
]
TASK = {
    "schema": "atlas.provider-smoke.v1",
    "records": [{"title": "Alpha", "url": "https://example.invalid/alpha"}],
    "candidate_url": "javascript:alert(1)",
    "request": "Return only JSON: {schema:'atlas.provider-smoke.v1',count:1,reject_candidate:true}. Use double quotes for valid JSON. Do not use search, execute code or edit files.",
}


def probe(model):
    work = HERE / model.split("/", 1)[1] / "cognitive-review"
    work.mkdir(parents=True, exist_ok=True)
    atomic_json(work / "input.json", TASK)
    row = {"requested_model": model, "started_at": datetime.now(timezone.utc).isoformat()}
    try:
        reply = CLI().run(work, TASK["request"], model, 120,
                          lambda: False, lambda *args: None)
        atomic_json(work / "result.json", reply)
        expected = {"schema": "atlas.provider-smoke.v1", "count": 1, "reject_candidate": True}
        row.update(status="passed" if reply == expected else "unexpected_response", response=reply)
    except Exception as error:
        row.update(status="failed", code=getattr(error, "code", type(error).__name__),
                   error=redact_text(str(error))[:1800])
    summary = work / "cli-summary.json"
    if summary.exists():
        row["cli"] = json.loads(summary.read_text())
    row["completed_at"] = datetime.now(timezone.utc).isoformat()
    atomic_json(work.parent / "probe-result.json", row)
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=MODELS)
    args = parser.parse_args()
    cli = CLI()
    info = cli.info(models=True)
    atomic_json(HERE / "catalog.json", info)
    previous = HERE / "results.json"
    results = json.loads(previous.read_text())["results"] if previous.exists() else []
    selected = [args.model] if args.model else MODELS
    results = [row for row in results if row["requested_model"] not in selected]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for future in as_completed([pool.submit(probe, model) for model in selected]):
            row = future.result()
            results.append(row)
            print(json.dumps({"model": row["requested_model"], "status": row["status"],
                              "code": row.get("code")}), flush=True)
    results.sort(key=lambda row: MODELS.index(row["requested_model"]) if row["requested_model"] in MODELS else len(MODELS))
    atomic_json(HERE / "results.json", {
        "scope": "Synthetic JSON smoke checks only. No Atlas leaf, template, application source or credentials sent as task input; not a quality benchmark.",
        "input_sha256": hashlib.sha256(json.dumps(TASK, sort_keys=True).encode()).hexdigest(),
        "requested_models": MODELS,
        "results": results,
    })


if __name__ == "__main__":
    main()
