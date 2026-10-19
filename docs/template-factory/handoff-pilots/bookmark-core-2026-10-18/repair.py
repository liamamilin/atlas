"""Preserve initial delivery; ask the same scoped OpenCode author for a narrow repair."""

import argparse
import json
from pathlib import Path
import shutil
import time

from develop import HERE, MODEL, driver, hashes, save

STAGE = HERE / "repair/scenario-review"
PROMPT = """Repair the supplied app/ using the observed feedback in source/feedback.json. This is a repair round, not an initial successful delivery. Keep the existing Python standard-library/SQLite runtime, Chinese UI and source entrypoint. Implement a genuine user-visible category creation action independent of saving a bookmark, so an existing record can be moved to a new category without an unrelated/dummy save. Preserve the existing inline-create path, original URL, search, duplicate choice, idempotency, error/input preservation and real data-directory persistence. Handle blank and duplicate category names with clear feedback and no data loss. Do not add editing/deletion/accounts/import/export or rewrite the application.
Fix the static request-body truncation risk: explicitly reject oversized requests before parsing or writing instead of treating a clamped prefix as a valid form. Return an honest HTTP 413 and understandable Chinese feedback, leave existing records unchanged, and do not claim to retain an unread oversized form. Invalid lengths/encoding should not be accepted through silent replacement. The oversize risk has NOT yet been runtime reproduced; distinguish it from the observed category workflow failure.
Keep the documented 2000-character note limit for this bounded repair; reject rather than silently truncate, retain submitted fields on ordinary validation failure. The 3420-character follow-up is an observation, not a new minimum-length requirement. Update README only for actual behavior. Read existing source before editing; make focused changes. Do not execute, browse, install or claim tests passed: the external operator will run them. Return the required small files/implemented/limits/self_checks JSON, listing all delivered application files."""


def prepare():
    assert not STAGE.exists(), "Do not overwrite a repair session"
    expected = json.loads((HERE / "generation.json").read_text())["source_sha256"]
    assert hashes(HERE / "application") == expected, "Initial application changed"
    STAGE.mkdir(parents=True)
    shutil.copytree(HERE / "application", STAGE / "app")
    source = STAGE / "source"
    source.mkdir()
    runtime = json.loads((HERE / "evaluation/runtime/runtime-results.json").read_text())
    feedback = {
        "scope": "One follow-up trial, preserve initial outcome; no numeric score or forced winner",
        "observed": [
            {
                "trigger": "Create 学习 independently, then move an existing 酸面包教程 into it",
                "result": "No standalone create or move-and-create UI. R05 could not complete; R08 fixture could not reach its normal restart checks.",
                "evidence": "initial runtime checks R04, R05, R08 and UI-only adapter createCategory/move",
                "harness_caveat": "R04 label says pass but only inline creation while saving a real bookmark was exercised. Do not manufacture extra saved records to satisfy the workflow.",
            },
            {
                "trigger": "Fully submitted 3420 logical-character note",
                "result": "Not saved. Existing app documents a 2000-character limit. This is a usability limit, not proven silent accepted-data loss. Initial supplement did not capture the immediate error before refresh.",
            },
        ],
        "static_risks_not_runtime_proven": [
            "server.py _read_form clamps Content-Length above MAX_BODY_BYTES, then parses and may accept a prefix. Reject oversize before parsing/writing.",
            "Invalid UTF-8 currently decoded with replacement; reject malformed input explicitly.",
        ],
        "core_check_summary": [
            {key: row[key] for key in ("id", "area", "status", "error") if key in row}
            for row in runtime["checks"] if row["id"].startswith("R")
        ],
        "repair_acceptance": [
            "Create two real empty categories through visible UI, save/select one, move an existing bookmark to the other and back to unclassified.",
            "Search/open original query+fragment, real process restart same data dir and independent empty data dir preserve the expected data boundaries.",
            "Blank/duplicate category feedback, physical double click, ordinary invalid/overlong note feedback without accepted-value clipping.",
            "Oversized request is explicitly rejected without partial write; source review and a separate posthoc synthetic diagnostic, not a rewritten frozen rubric.",
        ],
    }
    save(source / "feedback.json", feedback)
    save(STAGE / "input.json", {
        "task": "修复书签应用核心归类流程，显式拒绝截断请求",
        "runtime": "python3 app.py --port PORT --data-dir DIR; standard library + SQLite; loopback only",
        "source_inventory": ["source/feedback.json"],
        "preserved_initial_source_sha256": expected,
        "write_scope": "app/ only; existing initial application and evidence remain immutable",
    })
    (STAGE / "task-prompt.txt").write_text(PROMPT)
    save(HERE / "repair-input-freeze.json", {
        "model": MODEL, "reasoning_effort": "high",
        "inputs_sha256": hashes(STAGE), "observed_at": time.time(),
        "runtime_status": "not_run", "repair_status": "prepared",
    })
    print("Prepared narrow repair; no provider call made", flush=True)


def run():
    assert STAGE.exists() and not (STAGE / "process.json").exists()
    started = time.time()
    try:
        result = driver.run(STAGE, PROMPT, MODEL, 1800)
        save(STAGE / "result.json", result)
        actual = hashes(STAGE / "app")
        assert "app.py" in actual and 1 <= len(actual) <= 12
        assert set(result["files"]) == set(actual)
        for rel in actual:
            path = Path(rel)
            assert not path.is_absolute() and ".." not in path.parts
            assert path.suffix in {".py", ".html", ".css", ".js", ".md", ".json"}
            assert len(path.parts) <= 3 and (STAGE / "app" / path).stat().st_size < 400_000
        target = HERE / "application-repair"
        assert not target.exists()
        shutil.copytree(STAGE / "app", target)
        assert hashes(target) == actual
        save(HERE / "repair-generation.json", {
            "pipeline_status": "completed", "elapsed_seconds": round(time.time() - started, 2),
            "source_sha256": actual, "source_hand_edits": False,
            "implemented_claims": result.get("implemented"), "limits_claims": result.get("limits"),
            "runtime_status": "not_run", "initial_evidence_preserved": True,
        })
        print("DONE narrow repair; runtime verification pending", flush=True)
    except Exception as exc:
        save(HERE / "repair-failure.json", {
            "pipeline_status": "failed", "error": str(exc),
            "elapsed_seconds": round(time.time() - started, 2),
            "source_hand_edits": False, "runtime_status": "not_run",
        })
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "run"])
    args = parser.parse_args()
    (prepare if args.action == "prepare" else run)()
