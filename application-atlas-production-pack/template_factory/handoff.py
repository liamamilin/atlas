"""Deterministic, phase-scoped development views over an immutable blueprint."""

import hashlib
import json
from pathlib import Path

from atlas_runtime import atomic_json
from .artifacts import tree_manifest
from .store import digest


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def _write_json(path, value):
    atomic_json(path, value)


def write_handoff(destination, spec, phase, project_name, template_digest):
    destination = Path(destination)
    index = next(i for i, row in enumerate(spec["phases"]) if row["id"] == phase)
    phases = spec["phases"][: index + 1]
    phase_ids = {row["id"] for row in phases}
    cases = [row for row in spec["acceptance"] if row["phase"] in phase_ids]
    case_ids = {row["id"] for row in cases}
    features = [
        {**row, "acceptance": [key for key in row["acceptance"] if key in case_ids]}
        for row in spec["features"]
        if row.get("phase") in phase_ids
    ]
    # Keep the full scenario and all decision triggers. Defaults are proposals;
    # choices remain explicitly unconfirmed until a human records one.
    decisions = [
        {**row, "choice": None, "confirmed": False}
        for row in spec["decisions"]
    ]
    packet = {
        "schema": "atlas.development-handoff.v2",
        "project_name": project_name,
        "template_digest": template_digest,
        "blueprint": "blueprint/template.json",
        "selected_phase": phase,
        "selected_phase_status": "not_started",
        "selected_goal": phases[-1]["goal"],
        "prerequisite_phases": [row["id"] for row in phases[:-1]],
        "prerequisite_status": "requires_verification",
        "scenario": spec["scenario"],
        "case_basis": spec.get("case_basis"),
        "case_design": spec.get("case_design"),
        "roles": spec["roles"],
        "phases": phases,
        "features": features,
        "acceptance": cases,
        # Keep the legacy consumer shape recognizable; PROJECT_DECISIONS.json
        # carries the explicit human confirmation state and complete triggers.
        "decisions": spec["decisions"],
        "limits": spec.get("limits", []),
        "evidence_status": "not_run_by_export",
    }
    _write_json(destination / "CURRENT_PHASE.json", packet)

    _write_json(destination / "PROJECT_DECISIONS.json", {
        "schema": "atlas.project-decisions.v1",
        "project_name": project_name,
        "phase": phase,
        "template_digest": template_digest,
        "confirmed": False,
        "choices": decisions,
    })

    # Contract names exactly the phase-scoped cases and frozen code hashes. It
    # inventories acceptance members, including support/reference files, while
    # leaving command selection to a project-specific adapter.
    acceptance_root = destination / "blueprint/acceptance"
    suite_inventory = {
        "acceptance/" + path: value
        for path, value in tree_manifest(acceptance_root).items()
    }
    references_root = destination / "blueprint/references"
    if references_root.is_dir():
        suite_inventory.update({
            "references/" + path: value
            for path, value in tree_manifest(references_root).items()
        })
    contract_cases = []
    for row in cases:
        implementation = row["implementation"]
        implementation_bytes = (destination / "blueprint" / implementation).read_bytes()
        contract_cases.append({
            "id": row["id"],
            "phase": row["phase"],
            "type": row["type"],
            "goal": row["goal"],
            "features": row["features"],
            "implementation": implementation,
            "implementation_sha256": _sha256(implementation_bytes),
        })
    contract = {
        "schema": "atlas.acceptance-contract.v1",
        "template_digest": template_digest,
        "selected_phase": phase,
        "required_case_ids": [row["id"] for row in contract_cases],
        "cases": contract_cases,
        "suite_sha256": suite_inventory,
        "suite_digest": digest(tree_manifest(destination / "blueprint")),
        "suite_digest_scope": "all-frozen-blueprint-source; identical to managed runtime binding",
        "program_inventory_digest": digest(suite_inventory),
        "case_basis_digest": spec.get("case_basis", {}).get("basis_digest"),
        "scenario_revision": spec["scenario"]["revision"],
        "phase_required_evidence": spec.get("phase_required_evidence", {}).get(phase, []),
        "status": "not_run",
    }
    _write_json(destination / "ACCEPTANCE_CONTRACT.json", contract)

    (destination / "KNOWLEDGE.md").write_text(
        f"# Planning knowledge / 规划认知 · {project_name}\n\n"
        "This is the index into the immutable confirmed blueprint. Read the complete "
        "scenario in `blueprint/inputs/scenario.json`; then consult `blueprint/` "
        "CATEGORY.md, PRODUCT.md, ROADMAP.md, ARCHITECTURE.md, DECISIONS.md, "
        "acceptance/ and the remaining source documents as needed. This view does "
        "not duplicate those sources.\n\n"
        "这是完整冻结认知库的索引。完整场景位于 `blueprint/inputs/scenario.json`；"
        "按需阅读 blueprint/ 下的分类、产品、路线图、架构、决策、验收及其他源文档。\n",
        encoding="utf-8",
    )
    (destination / "README.md").write_text(
        f"# {project_name}\n\n"
        "Development package views: `KNOWLEDGE.md` is the planning index, `HANDOFF.md` "
        "is the current execution entry, and `ACCEPTANCE_CONTRACT.json` is an independent "
        "case and frozen-suite inventory. Export performs no execution. The complete "
        "source remains under `blueprint/`; `.atlas-blueprint.json` records provenance.\n\n"
        "开发包分为认知规划索引、当前执行入口和独立验收契约。导出不执行程序；完整冻结源保留于 `blueprint/`。\n",
        encoding="utf-8",
    )
    (destination / "HANDOFF.md").write_text(
        f"# Current handoff / 当前开发交接 · {phase}\n\n"
        "Read `KNOWLEDGE.md` for the full planning index and `CURRENT_PHASE.json` for "
        "the selected phase packet. The full confirmed scenario, selected and prerequisite "
        "capabilities, and all case goals are retained. Prerequisite phases require "
        "verification; export makes no completion claim.\n\n"
        "Resolve decision triggers from `PROJECT_DECISIONS.json`; defaults are proposed, "
        "and every choice starts unconfirmed. Compare this phase with the full scenario "
        "and report any scope gap instead of silently changing frozen commitments.\n\n"
        "Load architecture contracts from `blueprint/ARCHITECTURE.md`, product rationale "
        "from `blueprint/PRODUCT.md`, reuse and licensing notes from `blueprint/CATEGORY.md`, "
        "test guidance from `blueprint/acceptance/README.md`, and the strict application "
        "delivery protocol from `APP_DELIVERY.md`.\n\n"
        "Use `ACCEPTANCE_CONTRACT.json` as an independent inventory. Its status is `not_run`; "
        "it declares no commands and export runs no acceptance or application code. Before "
        "reporting completion, include actual application start commands and the executed "
        "test commands with passed, failed and not-run statuses. Exit code zero alone does "
        "not prove user behavior passed. Fix the application when frozen assertions fail; "
        "do not weaken or rewrite frozen tests.\n",
        encoding="utf-8",
    )
    (destination / "AGENT.md").write_text(
        "# Development entry\n\n"
        "Read HANDOFF.md, CURRENT_PHASE.json and PROJECT_DECISIONS.json first. Consult "
        "KNOWLEDGE.md, APP_DELIVERY.md and blueprint/ references as needed. Preserve "
        "existing project data and instructions; verify prerequisites before treating "
        "them as complete. Report exact application start commands and actual test "
        "commands with passed, failed and not-run statuses. Do not treat exit code zero "
        "as proof of user behavior; fix the app rather than weakening frozen acceptance.\n",
        encoding="utf-8",
    )

    (destination / "APP_DELIVERY.md").write_text(
        "# Application delivery protocol / 应用交付协议\n\n"
        "This file defines source submission for the independent offline runtime runner. "
        "It does not execute code or make an old blueprint runtime-capable. The factory "
        "can run frozen acceptance only when the immutable source contains "
        "`blueprint/acceptance/runner.json` with a valid `atlas.acceptance-runner.v1` "
        "binding for the frozen cases. Do not invent runner commands or edit frozen tests.\n\n"
        "本协议只定义离线运行验收的应用源码提交格式。只有冻结源包含有效的 "
        "`blueprint/acceptance/runner.json`（`atlas.acceptance-runner.v1`）时，工厂才支持运行；"
        "不得猜测命令或修改冻结验收程序。旧模板不会因此自动获得运行支持。\n\n"
        "## ZIP layout and inventory\n\n"
        "Submit a source-only ZIP no larger than 1 MiB compressed or 8 MiB expanded. "
        "Place `delivery.json` at ZIP root, beside the application files; do not wrap "
        "everything in another directory. Do not include real credentials, `.env` files, "
        "private keys, dependency caches, `node_modules` or virtual environments. The "
        "runner has no network access. Dependencies must be available in its managed "
        "offline image or included as allowed source assets; a network install is unavailable.\n\n"
        "`schema` must equal `atlas.application-delivery.v1`. `root` is `.` or `app`. "
        "`files` must list every application source file exactly, excluding `delivery.json`; "
        "wildcards and omissions are rejected. A single unambiguous `app/` prefix may be "
        "normalized to match files placed at ZIP root or beneath `app/`; duplicates, "
        "collisions and repeated prefixes are rejected.\n\n"
        "The following is a complete valid static-web example when the ZIP also contains "
        "the listed `index.html` file:\n\n"
        "```json\n"
        "{\n"
        '  "schema": "atlas.application-delivery.v1",\n'
        '  "root": ".",\n'
        '  "files": ["index.html"],\n'
        '  "runtime": {\n'
        '    "profile": "static-web",\n'
        '    "install": [],\n'
        '    "build": [],\n'
        '    "start": ["python3", "-m", "http.server", "8000"],\n'
        '    "port": 8000,\n'
        '    "readiness_path": "/"\n'
        "  }\n"
        "}\n"
        "```\n\n"
        "## Runtime profiles\n\n"
        "Web profiles are `python-web`, `node-web` and `static-web`. Each requires a "
        "project-specific `start` argv and an integer `port` from 1024 to 65535; optional "
        "`readiness_path` defaults to `/`. `install` and `build` are optional lists of argv "
        "commands. Use only the profile's supplied executables: Python commands for "
        "`python-web` and `static-web`, Node/npm commands for `node-web`. `cli` requires "
        "a `smoke` argv instead of web startup fields and accepts Python CLI executables. "
        "These argv values are application delivery metadata, never acceptance commands; "
        "acceptance commands come only from the frozen runner binding.\n\n"
        "CLI example shape (declare the exact files present in the ZIP):\n\n"
        "```json\n"
        "{\n"
        '  "schema": "atlas.application-delivery.v1",\n'
        '  "root": ".",\n'
        '  "files": ["app.py"],\n'
        '  "runtime": {"profile": "cli", "install": [], "build": [], "smoke": ["python3", "app.py"]}\n'
        "}\n"
        "```\n\n"
        "## Evidence and completion report\n\n"
        "Report the exact command used to start the app and the actual command/result for "
        "each test: passed, failed or not run. Preserve case IDs, captured output and "
        "assertion details. Exit code zero by itself does not establish user behavior; "
        "fix application defects rather than weakening frozen acceptance. Never describe "
        "an aborted, not-run or unverified case as passed.\n\n"
        "报告实际启动命令及每项测试的实际命令和结果（通过、失败、未运行），保留用例编号、输出和断言细节。"
        "单独退出码为零不能证明用户行为通过；应修复应用，不得弱化冻结验收。中止、未运行或未核实用例不得写成通过。\n",
        encoding="utf-8",
    )

    # Manifest is deliberately written last and does not hash itself.
    entries = [
        "README.md", "AGENT.md", "HANDOFF.md", "KNOWLEDGE.md",
        "CURRENT_PHASE.json", "PROJECT_DECISIONS.json", "ACCEPTANCE_CONTRACT.json",
        "APP_DELIVERY.md",
    ]
    manifest = {
        "schema": "atlas.development-handoff-manifest.v1",
        "version": 1,
        "template_digest": template_digest,
        "selected_phase": phase,
        "entry_sha256": {name: _sha256((destination / name).read_bytes()) for name in entries},
        "blueprint_sha256": tree_manifest(destination / "blueprint"),
        "views": {
            "knowledge": "KNOWLEDGE.md",
            "execution": "HANDOFF.md",
            "acceptance": "ACCEPTANCE_CONTRACT.json",
        },
    }
    _write_json(destination / "HANDOFF_MANIFEST.json", manifest)
    return packet
