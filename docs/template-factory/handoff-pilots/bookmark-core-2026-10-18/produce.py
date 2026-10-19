"""Single-scenario core-P0 pilot; existing factory authoring/freeze/export code."""

import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.cli import CLI  # noqa: E402
from template_factory.cognition import (  # noqa: E402
    GENERATE_PROMPT,
    CODE_PROMPT,
    REVIEW_PROMPT,
    research_context,
    validate_file_plan,
    apply_file_response,
    render_candidate,
    validate_review,
)
from template_factory.blueprints import (  # noqa: E402
    freeze_blueprint,
    export_development,
    validate_blueprint,
)
from template_factory.artifacts import archive_tree, tree_manifest  # noqa: E402

MODEL = "commandcode/deepseek/deepseek-v4.1-flash"
OLD = (
    ROOT
    / "docs/template-factory/cognition-pilots/bookmark-2026-10-17/tpl_3f303c2a69ea49b7aa1e5d01eba340f5.zip"
)
AB = ROOT / "docs/template-factory/ab-tests/bookmark-2026-10-18"

GUIDANCE = """Create a NEW compact core-P0 successor to the historical bookmark cognitive template, NOT an in-place patch. Preserve the exact confirmed scenario; prior source and runtime lessons are evidence. No new external research or claims. P0 MUST complete the whole confirmed journey: URL-only save, optional title and note, default unclassified, create/select categories, move records, category browse, keyword finding, open original URL with query/fragment, persistence across real process restart. Keep meaningful failures, recovery and data integrity. Preserve the two concretely useful prior lessons: no silently clipped accepted notes; a same-button double-submit does not accidentally produce two saves and duplicate-URL policy is explicit and conservative. Separate empty-library from no-search-match feedback. Do not hardcode known test fixture values.
Do not require editing, deletion/recycle bins, renaming/deleting categories, pagination, audit, accounts, billing, import/export or bulk operations in P0; retain relevant mature-category considerations with applicability=\"later\" or \"not applicable\", phase=null, acceptance=[] and reasons. A single complete P0 phase is appropriate; no need to add phases just to fill a roadmap. Decisions remain recommendations with actual human-choice triggers. Use a small coherent acceptance program set with shared setup, precise target/adapter contracts and true behavior assertions. Do not prescribe app DOM, API routes or error codes solely for testing; expose an equivalent UI adapter contract. Tests must not need APIs or capabilities outside P0. Record actual restart as operator-controlled before/after steps when no safe restart controller is supplied; never equate refresh with process restart or mark a skipped action passed. Do not embed an application, mocks or old runtime reports in acceptance.
The trial's explicit runtime is Python3 stdlib + SQLite and Chinese browser UI, python3 app.py --port PORT --data-dir DIR, loopback only, all durable data under DIR, no app dependency install. This deliberately aligns the default with the common trial environment and differs from the old Node recommendation; record it as a trial choice, not a category constraint or an improvement to the old A/B. Browser acceptance may have its own documented Playwright dependency. Keep the developer entry and architecture actionable and concise rather than restating every maturity possibility. No arbitrary token/latency/cost/feature-count thresholds. Stop when current product behavior and necessary failure paths are specified. All evidence states begin not_run."""


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def call(stage, prompt, inputs, sources):
    # A retry is a new owned call; the failed attempt and its logs stay intact.
    if (stage / "failure.json").exists() and not (stage / "result.json").exists():
        stage = stage.with_name(stage.name + "-retry-1")
        if (stage / "failure.json").exists():
            raise RuntimeError(
                "Retry also failed; inspect evidence before another attempt"
            )
    stage.mkdir(parents=True, exist_ok=True)
    result_file = stage / "result.json"
    if result_file.exists():
        return json.loads(result_file.read_text())
    source = stage / "source"
    source.mkdir(exist_ok=True)
    for name, content in sources.items():
        dest = source / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            content
            if isinstance(content, str)
            else json.dumps(content, ensure_ascii=False, indent=2) + "\n"
        )
    save(
        stage / "input.json",
        {**inputs, "source_inventory": ["source/" + n for n in sources]},
    )
    (stage / "prompt.txt").write_text(prompt)
    print("START " + stage.name, flush=True)
    try:
        result = CLI().run(
            stage,
            prompt,
            MODEL,
            1200,
            lambda: False,
            lambda *a: None,
            reasoning_effort="high",
        )
        save(result_file, result)
        print("DONE " + stage.name, flush=True)
        return result
    except Exception as exc:
        save(stage / "failure.json", {"error": str(exc), "pipeline_status": "failed"})
        print("FAILED " + stage.name + ": " + str(exc)[-500:], flush=True)
        raise


def main():
    assert (
        hashlib.sha256(OLD.read_bytes()).hexdigest()
        == "22a2b1e426c6eee0778459540aaf2d7dd34e390140a55e1ccda2bbb51e5b6a4b"
    )
    with zipfile.ZipFile(OLD) as z:
        old = json.loads(z.read("template.json"))
    research = old["research"]
    scenario = old["scenario"]
    if not (HERE / "protocol.json").exists():
        (HERE / "evaluation").mkdir(exist_ok=True)
        for name in [
            "rubric.json",
            "rubric.md",
            "runtime_test.py",
            "runtime_test.mjs",
            "supplement.mjs",
        ]:
            shutil.copyfile(AB / "evaluation" / name, HERE / "evaluation" / name)
        save(
            HERE / "protocol.json",
            {
                "kind": "one follow-up trial, not a new randomized pair",
                "model": MODEL,
                "reasoning_effort": "high",
                "source_template_version": "0.1.12",
                "source_zip_sha256": hashlib.sha256(OLD.read_bytes()).hexdigest(),
                "rubric_sha256": hashlib.sha256(
                    (HERE / "evaluation/rubric.json").read_bytes()
                ).hexdigest(),
                "core_journey": scenario,
                "prespecified_followup_probes": [
                    "long logical note round trip, same 3420 codepoints as M02b",
                    "same-button double-save",
                    "empty search explanation",
                ],
                "stacks": "Python stdlib+SQLite; old template default Node is changed, so historical times are not a controlled speed comparison",
                "sources": "reuse pinned historical model-reported category research; no new search or license verification",
                "stop": "produce candidate, independent static review, OpenCode initial downstream app, actual common runtime evidence, independent outcome review; preserve failures",
                "prohibitions": [
                    "no historical app code to developer",
                    "no hand edits to generated app",
                    "no old result rewriting",
                    "no publication",
                    "no implicit CLI-failure promotion",
                ],
            },
        )
    fixed = {
        "scenario": scenario,
        "language": "zh",
        "guidance_file": "source/GUIDANCE.md",
    }
    sources = {
        "RESEARCH.md": research_context(research),
        "GUIDANCE.md": GUIDANCE,
        "FORMAT.md": "Use exactly the authored spec fields described in the prompt. Stable IDs and complete bidirectional mappings. Atlas owns identity, source records, statuses and generated main docs. Available source IDs: S01 plus those in RESEARCH.md. Single-phase complete core P0; later capabilities can be unphased. File plan must include acceptance/README.md. Write code later per file, not now.",
    }
    plan = call(HERE / "production/blueprint-generate", GENERATE_PROMPT, fixed, sources)
    try:
        rows = validate_file_plan(plan)
    except Exception as exc:
        save(
            HERE / "production/blueprint-generate/host-validation.json",
            {"status": "failed", "error": str(exc)},
        )
        corrected = call(
            HERE / "production/blueprint-generate-correction",
            GENERATE_PROMPT
            + "\nThis is a fresh successor proposal repair, not a pinned identity-constrained revision. Read source/PREVIOUS.json and source/FEEDBACK.md completely. Return the complete corrected spec and file_plan; preserve unrelated capabilities and source references.",
            fixed,
            {
                **sources,
                "PREVIOUS.json": plan,
                "FEEDBACK.md": "Host rejected package.json at root; all planned files must remain acceptance/ or references/. Use acceptance/package.json, and commands relative to that directory. Fix associated instructions consistently. "
                "Before program authoring also resolve concrete contradictions: network policy must distinguish forbidden background fetch/telemetry from explicitly user-clicked original navigation, while preventing actual external connections in the test environment and target credential escape. "
                "Do not claim filesystem presence or a newly-opened SQLite connection proves real restart; use a new owned process plus persisted data readback. Do not require internal SQLite-connection instrumentation unavailable through the declared app interface. "
                "Use a UI adapter with default suggested selectors only; equivalent accessible UI implementations must not require template-specific testids. "
                "Default to operator-controlled before/after restart unless a dedicated controller safely owns the exact process; no arbitrary APP_CMD shell execution, no killing unrelated processes. "
                "No scope removal or invented pass. Keep complete P0 and meaningful negative behavior.",
            },
        )
        rows = validate_file_plan(corrected)
        plan = corrected
    spec = plan["spec"]
    assert spec["phases"][0]["id"] == "P0"
    content = {}
    for n, row in enumerate(rows):
        result = call(
            HERE / f"production/blueprint-code-{n + 1}",
            CODE_PROMPT,
            {**fixed, "file": row, "revision": 1},
            {
                "SPECIFICATION.json": plan,
                "ARCHITECTURE.md": spec["architecture_markdown"],
                "RESEARCH.md": research_context(research),
                "GUIDANCE.md": GUIDANCE,
                **{"generated-1/" + name: value for name, value in content.items()},
            },
        )
        content[row["path"]] = apply_file_response(result, row["path"])["content"]
    candidate = HERE / "candidate"
    if not candidate.exists():
        render_candidate(
            {"spec": spec, "files": content},
            research,
            {
                "scenario": scenario,
                "config": {"language": "zh"},
                "cognitive_repair": {"version": "0.2.0"},
            },
            candidate,
            "bookmark-core-pilot-2026-10-18",
        )
    validate_blueprint(candidate)
    frozen = HERE / "frozen"
    if not frozen.exists():
        meta = freeze_blueprint(
            candidate,
            frozen,
            {
                "origin": "OpenCode core-P0 successor pilot",
                "parent_zip_sha256": hashlib.sha256(OLD.read_bytes()).hexdigest(),
            },
        )
        save(HERE / "freeze.json", meta)
        archive_tree(candidate, HERE / "bookmark-core-cognition-v0.2.0.zip")
    meta = json.loads((HERE / "freeze.json").read_text())
    review_sources = {
        p.relative_to(candidate).as_posix(): p.read_text()
        for p in candidate.rglob("*")
        if p.is_file()
    }
    review = call(
        HERE / "production/cognitive-review",
        REVIEW_PROMPT,
        {
            "language": "zh",
            "scenario": scenario,
            "digest": meta["digest"],
            "review_dimensions": [
                "category_evidence",
                "scenario_scope",
                "product_completeness",
                "architecture_contract",
                "phase_acceptance",
                "decisions_defaults",
                "agent_handoff",
                "evidence_honesty",
            ],
        },
        review_sources,
    )
    assessed = validate_review(review, candidate)
    save(HERE / "independent-static-review.json", assessed)
    print(json.dumps({"static_review": assessed}, ensure_ascii=False), flush=True)
    if assessed["outcome"] != "passed":
        raise RuntimeError(
            "Candidate retained; review did not pass. Resolve actual findings before app trial."
        )
    if not (HERE / "development-package").exists():
        export_development(
            frozen,
            meta["digest"],
            HERE / "development-package",
            "bookmark-core-trial",
            "P0",
        )
        archive_tree(
            HERE / "development-package", HERE / "bookmark-core-development-p0.zip"
        )
    save(
        HERE / "candidate-state.json",
        {
            "kind": "unpublished cognition candidate",
            "static_review": "passed",
            "application_execution": "not_run",
            "digest": meta["digest"],
            "candidate_hashes": tree_manifest(candidate),
        },
    )


if __name__ == "__main__":
    main()
