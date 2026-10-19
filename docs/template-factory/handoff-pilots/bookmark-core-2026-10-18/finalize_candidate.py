"""Reuse complete authored files; repair metadata/docs; freeze and review core P0."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from atlas_runtime import atomic_json  # noqa: E402
from template_factory.cognition import (  # noqa: E402
    apply_file_response,
    render_candidate,
    REVIEW_PROMPT,
    validate_review,
    validate_file_plan,
)
from template_factory.blueprints import (  # noqa: E402
    freeze_blueprint,
    export_development,
    validate_blueprint,
)
from template_factory.artifacts import archive_tree, tree_manifest  # noqa: E402

module_spec = importlib.util.spec_from_file_location(
    "pilot_produce", HERE / "produce.py"
)
production = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(production)


def main():
    plan = json.loads(
        (HERE / "production/blueprint-generate-correction/result.json").read_text()
    )
    rows = plan["file_plan"]
    files = {}
    for n, row in enumerate(rows, 1):
        options = [
            HERE / f"production/blueprint-code-{n}/result.json",
            HERE / f"production/blueprint-code-{n}-retry-1/result.json",
        ]
        result = json.loads(next(p for p in options if p.exists()).read_text())
        files[row["path"]] = apply_file_response(result, row["path"])["content"]
    helper = (HERE / "diagnostics/helper-fixed.cjs").read_text()
    excerpts = "\n".join(line for line in helper.splitlines() if "rawTarget" in line)
    response = production.call(
        HERE / "production/blueprint-generate-finalize",
        "Finish only the missing metadata and two narrow consistency edits. Read source/ARCHITECTURE.md, source/README.md, source/CONFIG_EXCERPTS.md and source/NETWORK_PROBE.json. "
        'Return {"limits":["verbatim existing limitation bullet, without the bullet marker"],"edits":[{"path":"acceptance/common.cjs","replacements":[{"old":"exact unique old snippet","new":"replacement"}]},{"path":"acceptance/README.md","replacements":[{"old":"exact unique old text","new":"replacement"}]}]}. '
        "limits was accidentally omitted from spec: copy the already declared ## 限制 bullets into an array, do not invent new restrictions or change P0. "
        "Common helper: remove raw TARGET_URL echoes from validation error messages; invalid or userinfo URLs may contain secrets. Explain the problem without echoing the submitted URL. Do not change any validation condition, exported signature or substantive behavior. Source excerpts are exact original lines. "
        "README: align transport instructions with the independently probed repair: local HTTP target only (HTTPS explicitly unsupported), no URL userinfo, optional supported Basic credentials target the exact origin including port, unknown auth modes reject before requests; dedicated deny-default proxy blocks other origins even through redirects and closes with its owned browser. Navigation attempts are blocked/recorded; background attempts are violations. This only had a bounded helper probe, NOT the full suite or app acceptance. Preserve all unrelated commands, module contracts and tests. No execution, network, editing, fixture hardcoding or fake pass.",
        {
            "language": "zh",
            "host_failure": "Missing required authored field limits; all program calls complete and retained",
        },
        {
            "ARCHITECTURE.md": plan["spec"]["architecture_markdown"],
            "README.md": files["acceptance/README.md"],
            "CONFIG_EXCERPTS.md": excerpts,
            "NETWORK_PROBE.json": json.loads(
                (HERE / "diagnostics/network-fixed-result.json").read_text()
            ),
        },
    )
    assert set(response) == {"limits", "edits"}
    assert isinstance(response["limits"], list) and all(
        isinstance(x, str) for x in response["limits"]
    )
    effective = {
        "spec": {**plan["spec"], "limits": response["limits"]},
        "file_plan": rows,
    }
    validate_file_plan(effective)
    assert len(response["edits"]) == 2 and {x["path"] for x in response["edits"]} == {
        "acceptance/common.cjs",
        "acceptance/README.md",
    }
    prior = HERE / "diagnostics/finalization-base"
    (prior / "acceptance").mkdir(parents=True, exist_ok=True)
    (prior / "acceptance/common.cjs").write_text(helper)
    (prior / "acceptance/README.md").write_text(files["acceptance/README.md"])
    for edit in response["edits"]:
        value = apply_file_response(edit, edit["path"], prior)
        files[value["path"]] = value["content"]
    final_helper = HERE / "diagnostics/helper-final.cjs"
    final_helper.write_text(files["acceptance/common.cjs"])
    subprocess.run(
        [
            shutil.which("node"),
            str(HERE / "diagnostics/network-reprobe.cjs"),
            str(final_helper),
            str(HERE / "diagnostics/network-final-result.json"),
        ],
        check=True,
        timeout=60,
        env={
            "PATH": "/usr/bin:/bin",
            "HOME": str(Path.home()),
            "LANG": "en_US.UTF-8",
            "NODE_PATH": str(ROOT / "atlas-web/node_modules"),
        },
    )
    probe = json.loads((HERE / "diagnostics/network-final-result.json").read_text())
    assert (
        probe["passed"]
        and probe["helper_sha256"]
        == hashlib.sha256(files["acceptance/common.cjs"].encode()).hexdigest()
    )
    files["references/helper-network-probe.json"] = (
        json.dumps(probe, ensure_ascii=False, indent=2) + "\n"
    )
    with zipfile.ZipFile(production.OLD) as archive:
        old = json.loads(archive.read("template.json"))
    candidate = HERE / "candidate"
    if not candidate.exists():
        render_candidate(
            {"spec": effective["spec"], "files": files},
            old["research"],
            {
                "scenario": old["scenario"],
                "config": {"language": "zh"},
                "cognitive_repair": {"version": "0.2.0"},
            },
            candidate,
            "bookmark-core-pilot-2026-10-18",
        )
        value = json.loads((candidate / "template.json").read_text())
        value["evidence"] = [
            {
                "kind": "acceptance-helper-network-probe",
                "path": "references/helper-network-probe.json",
                "scope": "Owned local HTTP fixtures and synthetic credentials: helper transport only. Full 17-case suite and downstream app have NOT run.",
            }
        ]
        atomic_json(candidate / "template.json", value)
        validation = candidate / "VALIDATION.md"
        validation.write_text(
            validation.read_text()
            + "\n补充：references/helper-network-probe.json 只验证验收辅助模块的传输边界，使用自有本地测试服务和虚构凭据；不是完整验收套件或下游应用通过。\n"
        )
        inventory = tree_manifest(candidate)
        inventory.pop("integrity.json")
        atomic_json(
            candidate / "integrity.json",
            {"template_version": "0.2.0", "sha256": inventory},
        )
    validate_blueprint(candidate)
    frozen = HERE / "frozen"
    if not frozen.exists():
        meta = freeze_blueprint(
            candidate,
            frozen,
            {
                "origin": "OpenCode core-P0 successor pilot",
                "parent_zip_sha256": hashlib.sha256(
                    production.OLD.read_bytes()
                ).hexdigest(),
                "host_scope": "Render/freeze, exact response application, measured helper evidence. No app edits.",
            },
        )
        production.save(HERE / "freeze.json", meta)
        archive_tree(candidate, HERE / "bookmark-core-cognition-v0.2.0.zip")
    meta = json.loads((HERE / "freeze.json").read_text())
    review = production.call(
        HERE / "production/cognitive-review",
        REVIEW_PROMPT,
        {"language": "zh", "scenario": old["scenario"], "digest": meta["digest"]},
        {
            p.relative_to(candidate).as_posix(): p.read_text()
            for p in candidate.rglob("*")
            if p.is_file()
        },
    )
    assessed = validate_review(review, candidate)
    production.save(HERE / "independent-static-review.json", assessed)
    print(
        json.dumps(
            {
                "version": "0.2.0",
                "outcome": assessed["outcome"],
                "checks": assessed["checks"],
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    if assessed["outcome"] == "blocked" or any(
        row["outcome"] != "passed" and row["dimension"] != "phase_acceptance"
        for row in assessed["checks"]
    ):
        raise RuntimeError(
            "Core design has blocking/unresolved findings; retain candidate"
        )
    # The reviewer found no blocker, and only test-tool reliability is uncertain.
    # This allows an unpublished practical experiment, never a pass/promotion.

    development = HERE / "development-package"
    if not development.exists():
        export_development(
            frozen, meta["digest"], development, "bookmark-core-trial", "P0"
        )
        (development / "KNOWN_VALIDATION_LIMITS.md").write_text(
            "# 已知验收工具局限 / Known test-tool limits\n\n"
            "独立静态审阅：7 项 passed，phase_acceptance uncertain，没有 blocked。"
            "完整 17 用例尚未运行，不能声称通过。核心产品目标不因此删减。\n\n"
            "A08 的空库检查应在实际空库完成，不能要求应用为测试常驻隐藏空态容器。"
            "A13 的 20000 兜底不是产品长度要求；采用并记录合理的明确上限，"
            "验收按已声明上限检查显式拒绝与原有数据安全，不能静默裁剪已接受内容。"
            "A10 的 OPERATOR_CONFIRMED 只是人工声明，不是实际重启证据；"
            "应记录自有进程前后 PID、同一数据目录及 UI 读回，不能以刷新冒充重启。"
            "归类名失败和规范化变体仍需后续测试，现不声称覆盖。\n\n"
            "These are limitations of the authored suite, not reasons to distort the product. "
            "Do not add hidden empty-state placeholders or an arbitrary 20000 limit for a test. "
            "A confirmation flag is not process-restart evidence. Retain negative behaviors, "
            "data integrity and explicit unsupported/unrun states. The separate operator will "
            "test the actual shared workflow, real process restarts, long notes and double saves.\n"
        )
        handoff = development / "HANDOFF.md"
        handoff.write_text(
            handoff.read_text()
            + "\n先读 KNOWN_VALIDATION_LIMITS.md；本包仍为未发布试用候选，阶段验收可靠性待实际验证。\nRead KNOWN_VALIDATION_LIMITS.md before using the authored suite; this is an unpublished trial candidate, not accepted software.\n"
        )
        archive_tree(development, HERE / "bookmark-core-development-p0.zip")
    production.save(
        HERE / "current-candidate.json",
        {
            "version": "0.2.0",
            "candidate_dir": candidate.name,
            "review": "independent-static-review.json",
            "development_package": development.name,
            "digest": meta["digest"],
            "static_review_outcome": assessed["outcome"],
            "trial_allowed": True,
            "trial_basis": "No independent blocking finding; core scope/architecture passed. Test-tool uncertainty is preserved and sent to practical runtime checks, not marked passed.",
            "full_acceptance_execution": "not_run",
            "downstream_application_execution": "not_run",
        },
    )


if __name__ == "__main__":
    main()
