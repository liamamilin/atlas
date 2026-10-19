"""Controlled OpenCode pair. Outputs are materialized, never executed here."""

import argparse
import concurrent.futures
import hashlib
import json
import secrets
import shutil
import sys
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.cli import CLI  # noqa: E402
import development_cli  # noqa: E402

MODEL = "commandcode/deepseek/deepseek-v4.1-flash"
BUNDLE = ROOT / "docs/template-factory/cognition-pilots/bookmark-2026-10-17/tpl_3f303c2a69ea49b7aa1e5d01eba340f5.zip"

PROMPT = """Develop the real, complete local application described in input.json, not a plan or mockup. Read the request and supplied source inventory. Your task is implementation, not evaluation. Explicit task runtime overrides suggested stack defaults. The confirmed workflow must work end to end now: saving, categories, moving, keyword finding, opening and keeping data after restart. Product context, if supplied, may guide decisions, contracts, phases and self-checks; later stages necessary for the confirmed workflow must be implemented. Do not add accounts, cloud services, billing, collaboration, metadata fetching or dependencies. Ordinary reversible choices may be made without asking. Use Python 3 standard library, sqlite3 and a Chinese browser UI. Entry point: python3 app.py --port PORT --data-dir DIR; bind only 127.0.0.1; all durable app data belongs in DIR. Use focused modules and local imports/assets, no installation/build steps, shell/subprocess, arbitrary filesystem access, telemetry or external assets. You cannot execute programs; report checks as not run. Do not hardcode fixtures or invent test success. Do not mention generation condition or source context branding in UI or README. Write complete working application source into app/ using allowed tools, not code in your final response. Include a short README with exact startup, storage location, actual scope and limitations. Allowed application files: .py/.html/.css/.js/.md/.json, at most 12; no third-party code or copied acceptance suite. Final response is only small JSON metadata as instructed. Stop after delivery."""


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def hashes(directory):
    return {
        p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(directory.rglob("*"))
        if p.is_file() and "__pycache__" not in p.parts
    }


def prepare():
    control = HERE / "control"
    if (control / "protocol.json").exists():
        raise SystemExit("already prepared; never overwrite frozen experiment")
    assert hashlib.sha256(BUNDLE.read_bytes()).hexdigest() == "22a2b1e426c6eee0778459540aaf2d7dd34e390140a55e1ccda2bbb51e5b6a4b"
    with zipfile.ZipFile(BUNDLE) as z:
        scenario = json.loads(z.read("inputs/scenario.json"))
        common = {
            "task": "开发可实际使用的中文个人生活待购与灵感收藏夹",
            "scenario": {k: scenario[k] for k in ["name", "audience", "objective", "workflow", "acceptance"]},
            "runtime": "Python 3 standard library + SQLite; python3 app.py --port PORT --data-dir DIR; loopback HTTP only; no dependency installation",
            "scope": "完整实现上述用户流程；自行判断必要的失败反馈、数据保护和日常管理；不要把待实现文档当成完成",
            "source_inventory": [],
        }
        treatment = secrets.choice(["X", "Y"])
        for label in ["X", "Y"]:
            stage = HERE / "control" / label / "initial" / "scenario-review"
            stage.mkdir(parents=True, exist_ok=False)
            data = dict(common)
            if label == treatment:
                source = stage / "source" / "product-context"
                source.mkdir(parents=True)
                for item in z.infolist():
                    name = Path(item.filename)
                    assert not name.is_absolute() and ".." not in name.parts and not item.is_dir()
                    dst = source / name
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(z.read(item))
                data["source_inventory"] = ["source/product-context/" + n for n in z.namelist()]
                data["context_reading"] = "Read AGENT.md, PRODUCT.md, ARCHITECTURE.md, DECISIONS.md, ROADMAP.md first, then relevant category or acceptance material if useful. These are product context, not an already implemented app. The explicit Python runtime overrides Node recommendations."
            save(stage / "input.json", data)
            (stage / "task-prompt.txt").write_text(PROMPT)
    save(control / "mapping.json", {"template": treatment, "without_template": "Y" if treatment == "X" else "X"})
    save(control / "protocol.json", {
        "created": time.time(), "model": MODEL, "reasoning_effort": "high",
        "experiment": "one paired practical trial, not a statistical benchmark",
        "template_version": "0.1.12", "template_sha256": hashlib.sha256(BUNDLE.read_bytes()).hexdigest(),
        "common_prompt_sha256": hashlib.sha256(PROMPT.encode()).hexdigest(),
        "same_controls": ["confirmed scenario", "model and effort", "fresh standalone CLI with app-only writes", "Python standard library + SQLite", "no shell/web/peer/source-repository access", "1800-second infrastructure timeout per call", "single initial implementation and at most one equal feedback repair opportunity", "outcome-based shared evaluation"],
        "interpretation": "Difference is availability of a frozen cognitive template including tests. Different context/token counts are part of treatment, not equalized. Runtime adaptation is shared and differs from template's recommended Node stack. Primary evaluation must not require template-specific routes, error codes or selectors. Template suite is separate diagnostic only. No historical implementation is supplied.",
        "implementation_author": "OpenCode writes application files; orchestrator freezes and tests, no hand repairs",
        "provider_switch": "User requested commandcode. Old open-design attempts are retained in pre-switch-open-design, excluded from primary pair. Both new arms use file-write tools to avoid observed whole-source final-output truncation; rubric and product goals unchanged.",
        "inputs": {label: hashes(control / label / "initial" / "scenario-review") for label in ["X", "Y"]},
    })
    print("prepared frozen pair", flush=True)


def run_one(label, round_name):
    stage = HERE / "control" / label / round_name / "scenario-review"
    if (stage / "result.json").exists():
        return {"label": label, "round": round_name, "status": "already_done"}
    if round_name != "initial":
        raise ValueError("repair inputs must be prepared explicitly before running")
    began = time.time()
    print(json.dumps({"label": label, "event": "started", "at": began}), flush=True)
    try:
        result = development_cli.run(stage, PROMPT, MODEL, 1800)
        save(stage / "result.json", result)
        app_source = stage / "app"
        files = [p for p in app_source.rglob("*") if p.is_file()]
        assert (app_source / "app.py").is_file() and 1 <= len(files) <= 12
        validated = []
        for source_path in files:
            p = source_path.relative_to(app_source)
            content = source_path.read_text()
            assert not p.is_absolute() and ".." not in p.parts and all(not x.startswith(".") for x in p.parts)
            assert len(p.parts) <= 3 and p.suffix in [".py", ".html", ".css", ".js", ".md", ".json"]
            assert isinstance(content, str) and len(content.encode()) < 400_000
            validated.append((p, content))
        target = HERE / "blind" / label / round_name / "app"
        target.mkdir(parents=True, exist_ok=False)
        for p, content in validated:
            dst = target / p
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(content)
        evidence = {"label": label, "round": round_name, "status": "generated", "elapsed": round(time.time()-began, 2), "files": hashes(target), "implemented_claims": result.get("implemented"), "limits_claims": result.get("limits"), "execution": "not_yet_run"}
        save(HERE / "blind" / label / round_name / "generation.json", evidence)
        print(json.dumps({"label": label, "event": "generated", "files": len(files), "elapsed": evidence["elapsed"]}), flush=True)
        return evidence
    except Exception as e:
        failure = {"label": label, "round": round_name, "status": "failed", "error": str(e), "elapsed": round(time.time()-began, 2)}
        save(stage / "failure.json", failure)
        print(json.dumps(failure), flush=True)
        return failure


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "generate"])
    opts = parser.parse_args()
    if opts.action == "prepare":
        prepare()
    else:
        assert (HERE / "evaluation" / "rubric.json").exists(), "freeze rubric first"
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda label: run_one(label, "initial"), ["X", "Y"]))
        save(HERE / "control" / "generation-results.json", results)
        print("pair_generation_finished", flush=True)
