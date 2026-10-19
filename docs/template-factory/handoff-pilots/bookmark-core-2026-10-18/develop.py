"""Fresh OpenCode implementation using the phase handoff, never historical code."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
AB = ROOT / "docs/template-factory/ab-tests/bookmark-2026-10-18"
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
module_spec = importlib.util.spec_from_file_location(
    "pilot_development_cli", AB / "development_cli.py"
)
driver = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(driver)
MODEL = "commandcode/deepseek/deepseek-v4.1-flash"


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def hashes(root):
    return {
        p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file() and "__pycache__" not in p.parts
    }


def main():
    current = json.loads((HERE / "current-candidate.json").read_text())
    review = json.loads((HERE / current["review"]).read_text())
    assert current["trial_allowed"] and review["outcome"] != "blocked"
    assert all(
        row["outcome"] == "passed" or row["dimension"] == "phase_acceptance"
        for row in review["checks"]
    )
    stage = HERE / "development/scenario-review"
    assert not stage.exists(), "Do not overwrite an initial development session"
    stage.mkdir(parents=True)
    shutil.copytree(
        HERE / current["development_package"], stage / "source/product-context"
    )
    scenario = json.loads(
        (stage / "source/product-context/CURRENT_PHASE.json").read_text()
    )["scenario"]
    original_prompt = (
        AB / "control/X/initial/scenario-review/task-prompt.txt"
    ).read_text()
    prompt = original_prompt.replace(
        "Product context, if supplied, may guide decisions, contracts, phases and self-checks; later stages necessary for the confirmed workflow must be implemented.",
        "Start with source/product-context/HANDOFF.md, CURRENT_PHASE.json and PROJECT_DECISIONS.json. Implement the complete core P0. Read relevant contracts and acceptance material as directed, without preloading all later-stage or historical material. Existing explicit task runtime takes precedence over stack recommendations.",
    )
    inventory = [
        "source/product-context/" + name
        for name in hashes(stage / "source/product-context")
    ]
    save(
        stage / "input.json",
        {
            "task": "开发可实际使用的中文个人生活待购与灵感收藏夹",
            "scenario": {
                k: scenario[k]
                for k in ["name", "audience", "objective", "workflow", "acceptance"]
            },
            "runtime": "Python 3 standard library + SQLite; python3 app.py --port PORT --data-dir DIR; loopback HTTP only; no dependency installation",
            "scope": "完整实现上述用户流程；按 P0 交接保留必要失败反馈与数据保护，不实现后期成熟度功能",
            "context_reading": "Start with source/product-context/HANDOFF.md and CURRENT_PHASE.json, then related contracts and test programs when needed. No historical application code or runtime results supplied.",
            "source_inventory": inventory,
        },
    )
    (stage / "task-prompt.txt").write_text(prompt)
    save(
        HERE / "development-input-freeze.json",
        {
            "model": MODEL,
            "reasoning_effort": "high",
            "frozen_inputs": hashes(stage),
            "rubric_sha256": hashlib.sha256(
                (HERE / "evaluation/rubric.json").read_bytes()
            ).hexdigest(),
            "runtime_js_sha256": hashlib.sha256(
                (HERE / "evaluation/runtime_test.mjs").read_bytes()
            ).hexdigest(),
            "comparison": "single follow-up, not a randomized repeat; new P0 scope, shorter materials and aligned default stack all change",
        },
    )
    started = time.time()
    print("START core-P0 development", flush=True)
    try:
        result = driver.run(stage, prompt, MODEL, 1800)
        save(stage / "result.json", result)
        actual = hashes(stage / "app")
        assert "app.py" in actual and 1 <= len(actual) <= 12
        assert set(result["files"]) == set(actual), (
            "Declared files differ from delivered source"
        )
        for rel in actual:
            path = Path(rel)
            assert not path.is_absolute() and ".." not in path.parts
            assert path.suffix in {".py", ".html", ".css", ".js", ".md", ".json"}
            assert (
                len(path.parts) <= 3 and (stage / "app" / path).stat().st_size < 400_000
            )
        target = HERE / "application"
        shutil.copytree(stage / "app", target)
        assert hashes(target) == actual
        save(
            HERE / "generation.json",
            {
                "status": "generated",
                "pipeline_status": "completed",
                "elapsed_seconds": round(time.time() - started, 2),
                "source_sha256": actual,
                "implemented_claims": result.get("implemented"),
                "limits_claims": result.get("limits"),
                "execution": "not_run",
                "source_hand_edits": False,
            },
        )
        print("DONE core-P0 development", flush=True)
    except Exception as exc:
        save(
            HERE / "generation-failure.json",
            {
                "pipeline_status": "failed",
                "error": str(exc),
                "elapsed_seconds": round(time.time() - started, 2),
                "source_hand_edits": False,
                "runtime_status": "not_run",
            },
        )
        raise


if __name__ == "__main__":
    main()
