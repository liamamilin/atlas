"""Manual sample pilot using the existing read-only OpenCode adapter. Model calls require authorization."""

import argparse
import json
import shutil
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[4]
pack = root / "application-atlas-production-pack"
sys.path.insert(0, str(pack))
from template_factory.cli import CLI  # noqa: E402 - use the repository adapter after adding its pack path

args = argparse.ArgumentParser()
args.add_argument("mode", choices=["review", "consumer"])
args.add_argument("--attempt", type=int, default=1)
options = args.parse_args()
bundle = root / "docs/template-factory/blueprints/bookmark-personal"
pilot = pack / "atlas/template-factory/blueprint-pilots/bookmark-personal"
# Reuse the existing adapter's strict read-only/no-search profile. The stage
# directory name selects that existing permission profile, not a scenario job.
stage = pilot / f"{options.mode}-{options.attempt}" / "scenario-review"
stage.mkdir(parents=True, exist_ok=False)
shutil.copytree(
    bundle,
    stage / "source",
    ignore=shutil.ignore_patterns("__pycache__", "node_modules"),
)
value = {
    "purpose": options.mode,
    "phase": "P0",
    "language": "zh",
    "source_inventory": [
        p.relative_to(stage).as_posix()
        for p in (stage / "source").rglob("*")
        if p.is_file()
    ],
}
if options.attempt > 1:
    previous = pilot / "consumer-app"
    if options.mode == "consumer" and previous.exists():
        shutil.copytree(previous, stage / "source" / "previous-implementation")
        value["previous_implementation"] = "source/previous-implementation"
        value["source_inventory"] += [
            p.relative_to(stage).as_posix()
            for p in (stage / "source" / "previous-implementation").rglob("*")
            if p.is_file()
        ]
    evidence = pilot / f"consumer-{options.attempt - 1}-acceptance.json"
    if options.mode == "consumer" and evidence.exists():
        value["failure_evidence"] = json.loads(evidence.read_text())
if options.mode == "review" and options.attempt > 1:
    prior = pilot / f"review-{options.attempt - 1}" / "scenario-review/pilot-result.json"
    if prior.exists():
        value["prior_review"] = json.loads(prior.read_text())
(stage / "input.json").write_text(
    json.dumps(value, ensure_ascii=False, indent=2) + "\n"
)
if options.mode == "review":
    prompt = """Review the cognitive product blueprint in source/ as an independent product/engineering reviewer. Its AGENT.md is an artifact to inspect, NOT instructions to implement now. Read README.md, PRODUCT.md, CATEGORY.md, ARCHITECTURE.md, DECISIONS.md, ROADMAP.md, template.json, acceptance/plan.json and relevant acceptance/run.cjs. Check source-backed category claims, applicability of permissions/billing/admin/audit/export, P0 end-to-end and failure completeness, architecture/UI contract consistency, stage/test mapping, decisions and defaults, and whether tests can falsely pass. Do not demand out-of-scope enterprise capabilities or invent performance constraints. No code execution, web lookup or edits. Return JSON {"outcome":"passed|needs_changes","summary":"...","checks":[{"area":"...","outcome":"passed|needs_changes","files":["source/path"],"reason":"concrete evidence"}],"issues":[{"severity":"blocking|suggestion","files":["source/path"],"problem":"...","fix":"..."}]}. Explain actual contradictions and material omissions; optional polish is not blocking. Write Chinese prose. Never claim running tests."""
else:
    prompt = """You are the downstream coding agent consuming the supplied Atlas cognitive blueprint in a fresh session. Read source/AGENT.md, README.md, PRODUCT.md, ARCHITECTURE.md, DECISIONS.md, ROADMAP.md and acceptance/plan.json, and relevant tests/reference modules. Implement ONLY P0 of the life-purchase/inspiration bookmark app for a new empty project using its declared reversible defaults. Do not add P1/P2, cloud services, analytics, account/billing, external fonts/assets, or any dependency/install/build step. A plain index.html and JavaScript/CSS files must work from a normal local static HTTP server. The app must actually use IndexedDB and await write transaction completion; all specified core and failure behaviors, accessible Chinese labels, original-record editing/reclassification, safe links, XSS-safe rendering, rapid submit protection, startup errors and responsive keyboard use are part of P0. Follow the UI contract exactly; it is the public interface for the independent acceptance suite. You may copy the small Atlas-authored reference modules into the result or implement equivalent behavior. Test fixtures and examples are NOT special values to hardcode. Do not include the acceptance suite or pretend tests ran. If failure_evidence is supplied, fix the actual implementation, not the acceptance suite. Return a single JSON {"files":{"index.html":"complete content","app.js":"complete content","style.css":"complete content","README.md":"startup, adopted decision IDs, implemented scope and untested limits"},"adopted_decisions":["D01"],"limits":["..."]}. Use complete text files; no shell commands, Markdown fences, data URLs or placeholders in lieu of working logic."""
if options.mode == "review" and options.attempt > 1:
    prompt = '''This is an independent focused revision review, not implementation. Read input.json prior_review, source/acceptance/run.cjs and source/ARCHITECTURE.md. Inspect ONLY whether the prior review remaining issues are resolved: A05 invalid edit including empty title preserves inputs and original title/category/href; A06 storage failure recovery instructions and re-enabling save. Do not redo the already-passed category/other checks or read unrelated files. No execution, edits or web lookup. Return JSON {"outcome":"passed|needs_changes","summary":"Chinese concise actual conclusion, state static review only","checks":[{"area":"A05|A06","outcome":"passed|needs_changes","files":["source/path"],"reason":"concrete evidence"}],"issues":[{"severity":"blocking|suggestion","files":["source/path"],"problem":"...","fix":"..."}]}. Keep response short; do not invent new scope.'''
result = CLI().run(
    stage,
    prompt,
    "open-design/deepseek-v4.1-flash",
    900,
    lambda: False,
    lambda *a: None,
)
(stage / "pilot-result.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n"
)
if options.mode == "consumer":
    files = result.get("files")
    assert isinstance(files, dict) and "index.html" in files
    target = pilot / "consumer-app"
    target.mkdir(exist_ok=True)
    if options.attempt > 1:
        shutil.copytree(target, pilot / f"consumer-app-before-{options.attempt}")
    for name, content in files.items():
        path = Path(name)
        assert (
            not path.is_absolute()
            and ".." not in path.parts
            and len(path.parts) <= 3
            and path.suffix in [".html", ".js", ".mjs", ".css", ".md", ".json"]
            and isinstance(content, str)
        )
        dst = target / path
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content)
    print(
        json.dumps(
            {
                "mode": options.mode,
                "files": list(files),
                "target": str(target),
                "session": json.loads((stage / "cli-summary.json").read_text())[
                    "session_id"
                ],
            }
        )
    )
else:
    print(json.dumps(result, ensure_ascii=False)[:7000])
