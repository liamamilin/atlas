"""Checkpointed factory-protocol template production for the new domains."""

import argparse
import ast
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import sys
import time

from prepare import HERE, ROOT, MODEL, hashes, save

sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.cli import CLI  # noqa: E402
from template_factory.cognition import (  # noqa: E402
    RESEARCH_PROMPT, GENERATE_PROMPT, CODE_PROMPT, REVIEW_PROMPT,
    validate_research, research_context, validate_file_plan, apply_file_response,
    render_candidate, validate_review,
)
from template_factory.blueprints import (  # noqa: E402
    validate_blueprint, freeze_blueprint, export_development,
)
from template_factory.artifacts import archive_tree  # noqa: E402

GUIDANCE = """This is an unpublished experimental cognitive template, not an application. Preserve the common REQUEST and CONTRACT exactly; do not invent extra P0 obligations. The first and only implemented target phase P0 must complete the whole confirmed journey. Relevant mature-product extensions remain explicit later/not-applicable features with phase=null, acceptance=[], applicability reasons. Do not pretend a full desktop file manager or enterprise billing product is requested. Explain product/engineering choices and genuine human decision triggers, not arbitrary feature-count or latency/cost standards.
Respect the task's Python standard-library runtime, exact common JSON API/CLI contracts and Chinese UI/CLI. These are trial controls, not universal category preferences. All developers are prohibited from execution, installation or shell: AGENT instructions MUST tell them to report not_run and leave actual tests to an independent operator rather than getting stuck demanding execution. Recommend decisions with reasons while honoring already fixed choices. Never include old application source, task-specific fixture outputs, fake passed reports or full application starters.
Plan a compact acceptance program set: exactly acceptance/run.py and acceptance/README.md. run.py is an independently runnable REAL target checker using Python standard library, not the downstream application; map P0 cases to it. The operator supplies a freshly isolated app and explicit target. For web targets use only the supplied exact loopback HTTP origin/port, deny redirects to other origins, do not echo credentials; auth uses only synthetic local demo accounts. For the file CLI test allow only an explicitly supplied app.py plus owned disposable root fixtures, shell=False, no arbitrary commands, no real user Downloads/HOME. Never run these programs during generation. All acceptance states stay not_run. Keep code focused and machine outputs small; no encoded archive or enormous testing framework.
Research is model-reported primary evidence with explicit gaps; source URLs and license claims are facts only to the extent actually observed. No copied third-party code. No forced product winner or claim of universal stack/quality benefits. Read source/COMMON_DEVELOPMENT.md for common output/permission rules.
"""


def call(case, key, basename, prompt, inputs, sources, *, web_leaf=None):
    base = HERE / "cases" / case / "production" / key
    for attempt in (1, 2):
        stage = base / f"attempt-{attempt}" / basename
        if (stage / "result.json").exists():
            return json.loads((stage / "result.json").read_text())
        if (stage / "failure.json").exists():
            continue
        assert not stage.exists(), f"Unfinished owned stage requires audit: {stage}"
        stage.mkdir(parents=True)
        inventory = []
        for name, content in sources.items():
            path = stage / "source" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(content, str):
                path.write_text(content)
            else:
                save(path, content)
            inventory.append("source/" + name)
        if web_leaf is not None:
            (stage / "leaf.md").write_text(web_leaf)
        save(stage / "input.json", {**inputs, "source_inventory": inventory})
        (stage / "prompt.txt").write_text(prompt)
        save(stage / "input-freeze.json", hashes(stage))
        print(f"START {case}/{key}/attempt-{attempt}", flush=True)
        try:
            result = CLI().run(stage, prompt, MODEL, 1200, lambda: False,
                               lambda *args: None, reasoning_effort="high")
            save(stage / "result.json", result)
            print(f"DONE {case}/{key}/attempt-{attempt}", flush=True)
            return result
        except Exception as exc:
            save(stage / "failure.json", {"pipeline_status": "failed", "error": str(exc)})
            print(f"FAILED {case}/{key}/attempt-{attempt}: {str(exc)[-400:]}", flush=True)
    raise RuntimeError(f"Both transport/protocol attempts failed: {case}/{key}")


def produce(case):
    root = HERE / "cases" / case
    if (root / "template-ready.json").exists():
        return json.loads((root / "template-ready.json").read_text())
    scenario = json.loads((root / "request.json").read_text())
    # Factory serialization requires ready. This is an explicitly authorized
    # experiment input, not an update/confirmation of any catalog scenario.
    original_status = scenario["status"]
    scenario = {**scenario, "status": "ready", "authorization_scope": "user-authorized local experiment only; no catalog mutation"}
    save(root / "production/scenario-authorization.json", {
        "original_experiment_status": original_status,
        "derived_status": "ready", "purpose": "factory serialization for this authorized trial only",
        "catalog_modified": False,
    })
    fixed = {"language": "zh", "scenario": scenario, "research_date": "2026-10-19"}
    leaf = (root / "leaf.md").read_text()
    raw_research = call(case, "research", "research", RESEARCH_PROMPT,
        fixed, {"REQUEST.md": (root / "REQUEST.md").read_text()}, web_leaf=leaf)
    try:
        research = validate_research(raw_research)
    except Exception as exc:
        save(root / "research-host-validation.json", {"status": "failed", "error": str(exc)})
        # Atlas supplies S01 from the exact frozen scenario. Some research
        # responses redundantly cite that local input as an external source.
        # Remove ONLY this explicit local duplicate, retaining raw failure and
        # every external fact/ID unchanged; never normalize a real HTTPS source.
        local = [r for r in raw_research.get("sources", []) if r.get("id") == "S01"]
        assert len(local) == 1 and not str(local[0].get("url", "")).startswith(("http:", "https:"))
        normalized = {**raw_research, "sources": [r for r in raw_research["sources"] if r is not local[0]]}
        research = validate_research(normalized)
        save(root / "research-local-source-normalization.json", {
            "status": "validated_after_explicit_normalization", "removed_row": local[0],
            "scope": "Only redundant local S01 row removed; Atlas injects exact scenario as S01. Original invalid model response preserved. No external fact, source ID, summary or gap changed.",
            "external_sources_unchanged": normalized["sources"] == [r for r in raw_research["sources"] if r.get("id") != "S01"],
        })
    save(root / "research.json", research)
    sources = {
        "RESEARCH.md": research_context(research), "GUIDANCE.md": GUIDANCE,
        "REQUEST.md": (root / "REQUEST.md").read_text(),
        "CONTRACT.md": (root / "CONTRACT.md").read_text(),
        "COMMON_DEVELOPMENT.md": (HERE / "COMMON_DEVELOPMENT.md").read_text(),
        "FORMAT.md": "Return exactly spec and file_plan, no reserved fields. spec has exactly title,roles,features,decisions,phases,acceptance,architecture_markdown,limits. Use one complete core P0, mature later features unphased. Source IDs: S01 plus research IDs. File plan exactly acceptance/run.py then acceptance/README.md. These are authored test programs, never app.py. No source/runtime/grade claims. All current capabilities and P0 cases mapped bidirectionally.",
    }
    fixed["guidance_file"] = "source/GUIDANCE.md"
    plan = call(case, "spec", "blueprint-generate", GENERATE_PROMPT, fixed, sources)
    try:
        rows = validate_file_plan(plan)
        assert {r["path"] for r in rows} == {"acceptance/run.py", "acceptance/README.md"}
    except Exception as exc:
        save(root / "spec-host-validation.json", {"status": "failed", "error": str(exc)})
        plan = call(case, "spec-correction", "blueprint-generate", GENERATE_PROMPT,
            fixed, {**sources, "PREVIOUS.json": plan,
                    "FEEDBACK.md": "Repair the preserved proposal: " + str(exc)
                    + ". Read previous and feedback; preserve scenario, correct the complete spec and fixed two-file plan."})
        rows = validate_file_plan(plan)
        assert {r["path"] for r in rows} == {"acceptance/run.py", "acceptance/README.md"}
    content = {}
    for row in rows:
        key = "program" if row["path"].endswith(".py") else "instructions"
        value = call(case, key, "blueprint-code-" + key, CODE_PROMPT,
            {**fixed, "file": row, "revision": 1},
            {**sources, "SPECIFICATION.json": plan,
             "ARCHITECTURE.md": plan["spec"]["architecture_markdown"],
             **{"generated-1/" + name: text for name, text in content.items()}})
        content[row["path"]] = apply_file_response(value, row["path"])["content"]
        if row["path"].endswith(".py"):
            ast.parse(content[row["path"]])
    candidate = root / "candidate"
    if not candidate.exists():
        render_candidate({"spec": plan["spec"], "files": content}, research,
            {"scenario": scenario, "config": {"language": "zh"}}, candidate,
            "cross-domain-" + case + "-2026-10-19")
    validate_blueprint(candidate)
    frozen = root / "frozen"
    if not frozen.exists():
        meta = freeze_blueprint(candidate, frozen,
            {"origin": "OpenCode multi-domain controlled trial; unpublished", "scenario_scope": "experiment, not a catalog state change"})
        save(root / "freeze.json", meta)
        archive_tree(candidate, root / (case + "-cognition.zip"))
    meta = json.loads((root / "freeze.json").read_text())
    review = call(case, "static-review", "cognitive-review", REVIEW_PROMPT,
        {**fixed, "digest": meta["digest"]},
        {p.relative_to(candidate).as_posix(): p.read_text() for p in candidate.rglob("*") if p.is_file()})
    assessed = validate_review(review, candidate)
    save(root / "independent-template-review.json", assessed)
    if assessed["outcome"] == "blocked":
        raise RuntimeError(f"{case}: material template design blocker, preserve review before any trial")
    package = root / "development-package"
    if not package.exists():
        export_development(frozen, meta["digest"], package, "trial-" + case, "P0")
        notice = "Experimental unpublished template. Independent static outcome: " + assessed["outcome"] + ". Programs have NOT run. Common task forbids developer execution; report not_run and implement the user journey. External independent tests remain separate. Source facts are model-reported; no universal stack or license certification.\n"
        (package / "EXPERIMENT_NOTICE.md").write_text(notice)
        (package / "HANDOFF.md").write_text((package / "HANDOFF.md").read_text() + "\nSee EXPERIMENT_NOTICE.md.\n")
        archive_tree(package, root / (case + "-development-p0.zip"))
    ready = {"status": "unpublished_trial_input", "template_digest": meta["digest"],
             "review_outcome": assessed["outcome"], "package_sha256": hashes(package),
             "authored_acceptance": "syntax parsed, not executed", "program_files": list(content),
             "application_implemented": False, "published": False}
    save(root / "template-ready.json", ready)
    return ready


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", nargs="+", default=["budget", "booking", "rename"])
    args = parser.parse_args()
    assert (HERE / "evaluation/freeze.json").exists(), "Freeze independent oracle before template generation"
    started = time.time()
    outcomes = {}
    with ThreadPoolExecutor(max_workers=3) as pool:
        pending = {pool.submit(produce, case): case for case in args.cases}
        for future in as_completed(pending):
            case = pending[future]
            try:
                outcomes[case] = future.result()
            except Exception as exc:
                outcomes[case] = {"status": "failed", "error": str(exc)}
            save(HERE / "production-progress.json", {"cases": outcomes, "elapsed_seconds": round(time.time() - started, 2)})
    if any(row.get("status") == "failed" for row in outcomes.values()):
        raise SystemExit("Template production has preserved failures; resolve before development")


if __name__ == "__main__":
    main()
