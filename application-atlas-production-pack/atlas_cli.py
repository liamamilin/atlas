#!/usr/bin/env python3
"""Small, read-only-first terminal entry point for the Atlas workbench.

The CLI deliberately calls the same local API as the web workbench.  It does
not invoke OpenCode directly, so preflight, isolation, verification and
evidence remain owned by Atlas and the API service.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ZH = {
    "projects": "项目",
    "project": "项目",
    "workspace": "工作区",
    "preflight": "启动前检查",
    "tasks": "任务",
    "executions": "执行记录",
    "execution": "最新执行",
    "apply": "应用结果",
    "status": "状态",
    "acceptance": "验收",
    "transport": "执行方式",
    "task": "任务",
    "evidence": "证据",
    "cleanup": "清理",
    "none": "暂无",
    "passed": "通过",
    "failed": "失败",
    "not_configured": "未配置",
    "planned": "计划中",
    "running": "运行中",
    "completed": "已完成",
    "stopped": "已停止",
    "pending": "待处理",
    "waived": "已豁免",
    "applied": "已应用",
    "applying": "应用中",
    "not_applicable": "无需应用",
    "conflict": "有冲突",
    "superseded": "已被新执行替代",
    "http": "OpenCode 会话",
    "cli": "OpenCode CLI",
    "read_only": "只读模式；使用 --start 或 --cleanup 才会执行写操作。",
    "no_project": "没有找到匹配的项目。",
    "no_task": "没有找到匹配的任务。",
    "starting": "正在启动任务",
    "started": "执行已创建",
    "cleaned": "执行工作副本已清理",
    "apply_first": "请先应用结果或明确处理后再清理",
    "error": "错误",
    "view": "查看运行详情",
    "stop": "停止执行",
    "new_task": "新建任务",
    "export": "导出证据包",
}
EN = {
    "projects": "Projects",
    "project": "Project",
    "workspace": "Workspace",
    "preflight": "Preflight",
    "tasks": "Tasks",
    "executions": "Executions",
    "execution": "Latest execution",
    "apply": "Apply result",
    "status": "Status",
    "acceptance": "Acceptance",
    "transport": "Transport",
    "task": "Task",
    "evidence": "Evidence",
    "cleanup": "Cleanup",
    "none": "None",
    "passed": "Passed",
    "failed": "Failed",
    "not_configured": "Not configured",
    "planned": "Planned",
    "running": "Running",
    "completed": "Completed",
    "stopped": "Stopped",
    "pending": "Pending",
    "waived": "Waived",
    "applied": "Applied",
    "applying": "Applying",
    "not_applicable": "Not applicable",
    "conflict": "Conflict",
    "superseded": "Superseded",
    "http": "OpenCode session",
    "cli": "OpenCode CLI",
    "read_only": "Read-only mode; use --start or --cleanup for mutations.",
    "no_project": "No matching project was found.",
    "no_task": "No matching task was found.",
    "starting": "Starting task",
    "started": "Execution created",
    "cleaned": "Execution worktree cleaned",
    "apply_first": "Apply or explicitly handle the result before cleanup",
    "error": "Error",
    "view": "View run details",
    "stop": "Stop execution",
    "new_task": "New task",
    "export": "Export evidence bundle",
}


class AtlasCliError(RuntimeError):
    """A user-facing API or argument error."""


@dataclass
class AtlasApi:
    base_url: str = "http://127.0.0.1:5199"
    timeout: float = 30.0

    def request(self, method: str, path: str, body: dict | None = None) -> Any:
        payload = None
        headers = {"Accept": "application/json"}
        if body is not None:
            payload = json.dumps(body, ensure_ascii=False).encode()
            headers["Content-Type"] = "application/json"
        url = self.base_url.rstrip("/") + path
        try:
            with urlopen(Request(url, data=payload, headers=headers, method=method),
                         timeout=self.timeout) as response:
                raw = response.read()
                return json.loads(raw) if raw else {}
        except HTTPError as error:
            try:
                detail = json.loads(error.read() or b"{}")
            except (ValueError, TypeError):
                detail = {}
            raise AtlasCliError(detail.get("error") or f"API {error.code}: {url}") from error
        except (URLError, TimeoutError, OSError) as error:
            raise AtlasCliError(f"Atlas API unavailable: {url} ({error})") from error

    def get(self, path: str) -> Any:
        return self.request("GET", path)

    def post(self, path: str, body: dict | None = None) -> Any:
        return self.request("POST", path, body)


def _label(lang: str, key: str) -> str:
    return (ZH if lang == "zh" else EN).get(key, key)


def _status(value: Any, lang: str) -> str:
    return _label(lang, str(value or "unknown"))


def _project_match(projects: list[dict], selector: str | None) -> dict | None:
    if not selector:
        return projects[0] if len(projects) == 1 else None
    for project in projects:
        if selector in {project.get("id"), project.get("name")}:
            return project
    return None


def _task_match(tasks: list[dict], selector: str | None) -> dict | None:
    if not selector:
        return None
    for task in tasks:
        if selector in {task.get("id"), task.get("title")}:
            return task
    return None


def _execution_summary(execution: dict, lang: str) -> dict:
    evidence = execution.get("raw_state", {}).get("evidence", {}) or {}
    cli_run = evidence.get("cli_run", {}) or {}
    summary = cli_run.get("summary", {}) or {}
    return {
        "id": execution.get("id"),
        "status": _status(execution.get("status"), lang),
        "transport": _label(lang, "cli" if execution.get("engine") == "opencode-cli" else "http"),
        "exitCode": summary.get("exitCode"),
        "timedOut": summary.get("timedOut", False),
        "diagnosticCode": summary.get("diagnosticCode"),
        "diagnosticHint": summary.get("diagnosticHint"),
        "evidenceDirectory": cli_run.get("evidenceDirectory"),
        "applicationStatus": execution.get("application_status"),
    }


def _print_project(project: dict, workspace: dict, preflight: dict,
                   lang: str, *, output: Any = print) -> None:
    output(f"{_label(lang, 'project')}: {project.get('name', project.get('id'))} [{project.get('id')}]" )
    output(f"{_label(lang, 'workspace')}: {project.get('workspace')}")
    output(f"{_label(lang, 'preflight')}: {_status(preflight.get('status'), lang)}")
    tasks = workspace.get("tasks", []) or []
    output(f"{_label(lang, 'tasks')}: {len(tasks)}")
    for task in tasks:
        output(f"  - {task.get('id')}  {task.get('title')}  "
               f"[{_status(task.get('execution_status'), lang)} / "
               f"{_status(task.get('acceptance_status'), lang)}]")
    executions = workspace.get("executions", []) or []
    output(f"{_label(lang, 'executions')}: {len(executions)}")
    for execution in executions[:8]:
        item = _execution_summary(execution, lang)
        output(f"  - {item['id']}  {item['status']}  {item['transport']}"
               f"  exit={item['exitCode'] if item['exitCode'] is not None else '-'}")
        if item.get("diagnosticCode"):
            output(f"    diagnostic={item['diagnosticCode']}: {item.get('diagnosticHint') or '-'}")


def _poll(api: AtlasApi, project_id: str, execution_id: str,
          lang: str, *, interval: float = 0.5, timeout: float = 30.0) -> dict:
    deadline = time.monotonic() + timeout
    last = None
    while time.monotonic() < deadline:
        last = api.get(f"/api/projects/{quote(project_id, safe='')}/executions/{quote(execution_id, safe='')}")
        if last.get("status") in {"completed", "failed", "stopped", "unknown"}:
            return last
        time.sleep(interval)
    return last or {}


def _interactive(api: AtlasApi, args: argparse.Namespace) -> int:
    """Run the keyboard-first terminal slice.

    The first slice intentionally keeps the state machine small: choose a
    project, choose a task, inspect preflight and evidence, then explicitly
    confirm a start or cleanup action.  Applying a diff and live event-stream
    controls remain in the web workbench until their API contracts are fixed.
    """
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise AtlasCliError("--interactive requires a TTY")
    import curses

    lang = args.lang
    projects = api.get("/api/projects")
    if not projects:
        raise AtlasCliError(_label(lang, "no_project"))
    matched_index = next(
        (index for index, item in enumerate(projects)
         if args.project and args.project in {item.get("id"), item.get("name")}), None)
    if args.project and matched_index is None:
        raise AtlasCliError(_label(lang, "no_project"))
    project_index = matched_index if matched_index is not None else 0
    project = projects[project_index]
    workspace = None
    preflight = None
    task_index = 0
    message = _label(lang, "read_only")

    def load_project(item):
        nonlocal workspace, preflight, task_index
        workspace = api.get(f"/api/projects/{quote(item['id'], safe='')}/workspace")
        preflight = api.get(f"/api/projects/{quote(item['id'], safe='')}/harness/preflight")
        task_index = min(task_index, max(0, len(workspace.get("tasks", [])) - 1))

    def draw(stdscr, title, lines, footer):
        stdscr.erase()
        height, width = stdscr.getmaxyx()
        stdscr.addnstr(0, 0, title, max(1, width - 1), curses.A_BOLD)
        for row, line in enumerate(lines[:max(0, height - 3)], 2):
            stdscr.addnstr(row, 0, line, max(1, width - 1))
        stdscr.addnstr(height - 1, 0, footer, max(1, width - 1), curses.A_DIM)
        stdscr.refresh()

    def confirm(stdscr, prompt):
        draw(stdscr, _label(lang, "project"), [prompt, "y = yes / n = no"], "y/n")
        while True:
            key = stdscr.getch()
            if key in (ord("y"), ord("Y")):
                return True
            if key in (ord("n"), ord("N"), 27):
                return False

    def text_prompt(stdscr, prompt):
        """Read a short evidence summary without leaving curses mode."""
        height, width = stdscr.getmaxyx()
        stdscr.erase()
        stdscr.addnstr(0, 0, prompt, max(1, width - 1), curses.A_BOLD)
        stdscr.addnstr(2, 0, "> ", max(1, width - 1))
        curses.echo()
        try:
            value = stdscr.getstr(2, 2, max(1, width - 4)).decode("utf-8", "replace").strip()
        finally:
            curses.noecho()
        return value

    def task_for_current():
        tasks = (workspace or {}).get("tasks", [])
        return tasks[task_index] if tasks else None

    def execute_start(stdscr, task):
        nonlocal message
        prompt = f"{_label(lang, 'starting')}: {task.get('title')}?"
        if not confirm(stdscr, prompt):
            message = _label(lang, "read_only")
            return
        try:
            execution = api.post(
                f"/api/projects/{quote(project['id'], safe='')}/tasks/"
                f"{quote(task['id'], safe='')}/executions", {"transport": args.transport})
            if execution.get("status") not in {"completed", "failed", "stopped"}:
                execution = _poll(api, project["id"], execution["id"], lang, timeout=args.timeout)
            message = f"{_label(lang, 'started')}: {execution.get('id')} / " \
                      f"{_status(execution.get('status'), lang)}"
            load_project(project)
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def execute_cleanup(stdscr, task):
        nonlocal message
        executions = [item for item in (workspace or {}).get("executions", [])
                      if item.get("task_id") == task.get("id")]
        if not executions:
            message = _label(lang, "none")
            return
        execution = executions[0]
        if execution.get("status") == "completed" and execution.get("application_status") not in {
                "applied", "not_applicable", "superseded"}:
            message = _label(lang, "apply_first")
            return
        prompt = f"{_label(lang, 'cleanup')}: {execution.get('id')}?"
        if not confirm(stdscr, prompt):
            return
        try:
            result = api.post(
                f"/api/projects/{quote(project['id'], safe='')}/executions/"
                f"{quote(execution['id'], safe='')}/cleanup")
            message = f"{_label(lang, 'cleaned')}: {result.get('id', execution['id'])}"
            load_project(project)
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def execute_apply(stdscr, task):
        nonlocal message
        executions = [item for item in (workspace or {}).get("executions", [])
                      if item.get("task_id") == task.get("id")]
        if task.get("kind") == "analysis" or not executions:
            message = _label(lang, "none")
            return
        execution = executions[0]
        if execution.get("status") != "completed" or execution.get("application_status") not in {
                "pending", "conflict", "failed"}:
            message = f"{_label(lang, 'status')}: " \
                      f"{_status(execution.get('application_status'), lang)}"
            return
        prompt = f"{_label(lang, 'apply')}: {execution.get('id')}?"
        if not confirm(stdscr, prompt):
            return
        try:
            result = api.post(
                f"/api/projects/{quote(project['id'], safe='')}/executions/"
                f"{quote(execution['id'], safe='')}/apply")
            message = f"{_label(lang, 'apply')}: " \
                      f"{_status(result.get('application_status'), lang)}"
            load_project(project)
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def latest_execution(task):
        executions = [item for item in (workspace or {}).get("executions", [])
                      if item.get("task_id") == task.get("id")]
        return executions[0] if executions else None

    def view_execution(stdscr, task):
        execution = latest_execution(task)
        if not execution:
            return
        evidence = (execution.get("raw_state") or {}).get("evidence") or {}
        summary = evidence.get("run_summary") or {}
        cli_run = evidence.get("cli_run") or {}
        lines = [
            f"{_label(lang, 'view')}: {execution.get('id')}",
            f"{_label(lang, 'status')}: {_status(execution.get('status'), lang)} / "
            f"{_status(execution.get('application_status'), lang)}",
            f"{_label(lang, 'transport')}: "
            f"{_label(lang, 'cli' if execution.get('engine') == 'opencode-cli' else 'http')}",
            f"exitCode: {summary.get('exitCode', (cli_run.get('summary') or {}).get('exitCode', '-'))}",
            f"timedOut: {summary.get('timedOut', (cli_run.get('summary') or {}).get('timedOut', False))}",
            f"{_label(lang, 'evidence')}: {cli_run.get('evidenceDirectory', '-')}",
            "",
        ]
        commands = (evidence.get("tool_calls") or {}).get("commands") or []
        if commands:
            lines.append("Verification:")
            for item in commands:
                lines.append(
                    f"  [{'✓' if item.get('status') == 'completed' and item.get('exit') == 0 else '!'}] "
                    f"{item.get('command')}  exit={item.get('exit', '-')} "
                    f"{item.get('durationMs', '-')}ms")
        else:
            lines.append("No recorded verification commands.")
        draw(stdscr, _label(lang, "view"), lines, "Press any key to return")
        stdscr.getch()

    def execute_stop(stdscr, task):
        nonlocal message
        execution = latest_execution(task)
        if not execution or execution.get("status") not in {"queued", "running", "waiting_permission", "waiting_input"}:
            message = _label(lang, "none")
            return
        if not confirm(stdscr, f"{_label(lang, 'stop')}: {execution.get('id')}?"):
            return
        try:
            result = api.post(
                f"/api/projects/{quote(project['id'], safe='')}/executions/"
                f"{quote(execution['id'], safe='')}/stop")
            message = f"{_label(lang, 'stop')}: {_status(result.get('status'), lang)}"
            load_project(project)
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def execute_acceptance(stdscr, task, status):
        nonlocal message
        if task.get("acceptance_status") in {"passed", "waived"}:
            message = f"{_label(lang, 'acceptance')}: " \
                      f"{_status(task.get('acceptance_status'), lang)}"
            return
        summary = text_prompt(stdscr, f"{_label(lang, 'acceptance')} ({_status(status, lang)})")
        if not summary:
            message = _label(lang, "none")
            return
        if not confirm(stdscr, f"{_label(lang, 'acceptance')}: {summary}?"):
            return
        try:
            result = api.post(
                f"/api/projects/{quote(project['id'], safe='')}/tasks/"
                f"{quote(task['id'], safe='')}/acceptance",
                {"status": status, "evidence": [{"kind": "terminal", "summary": summary}]})
            message = f"{_label(lang, 'acceptance')}: " \
                      f"{_status(result.get('acceptance_status'), lang)}"
            load_project(project)
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def create_task(stdscr):
        nonlocal message, task_index
        iterations = (workspace or {}).get("iterations", [])
        iteration = next((item for item in iterations if item.get("status") == "active"), None)
        if not iteration:
            message = f"{_label(lang, 'error')}: no active iteration"
            return
        title = text_prompt(stdscr, f"{_label(lang, 'new_task')} - title")
        objective = text_prompt(stdscr, "Objective") if title else ""
        kind = (text_prompt(stdscr, "Kind: code / document / analysis") or "code").lower()
        if kind not in {"code", "document", "analysis"}:
            kind = "code"
        writes = text_prompt(stdscr, "Allowed write paths (comma separated)") if kind != "analysis" else ""
        checks = text_prompt(stdscr, "Verification commands (semicolon separated)")
        if not title or not objective:
            message = _label(lang, "none")
            return
        body = {
            "iteration_id": iteration["id"], "kind": kind, "title": title,
            "objective": objective,
            "input_document_versions": iteration.get("input_document_versions", []),
            "requirement_ids": iteration.get("requirement_ids", []),
            "write_paths": [item.strip() for item in writes.split(",") if item.strip()],
            "verification_commands": [item.strip() for item in checks.split(";") if item.strip()],
        }
        if kind == "analysis":
            body["write_paths"] = []
        if not confirm(stdscr, f"{_label(lang, 'new_task')}: {title}?"):
            return
        try:
            api.post(f"/api/projects/{quote(project['id'], safe='')}/tasks", body)
            load_project(project)
            task_index = max(0, len(workspace.get("tasks", [])) - 1)
            message = f"{_label(lang, 'new_task')}: {title}"
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def export_project(stdscr):
        nonlocal message
        if not confirm(stdscr, f"{_label(lang, 'export')}: {project.get('name')}?"):
            return
        try:
            result = api.post(f"/api/projects/{quote(project['id'], safe='')}/export")
            message = f"{_label(lang, 'export')}: {result.get('archive', result.get('directory', '-'))}"
        except AtlasCliError as error:
            message = f"{_label(lang, 'error')}: {error}"

    def app(stdscr):
        nonlocal project, project_index, task_index, message
        try:
            curses.curs_set(0)
        except curses.error:
            # Some standard PTYs do not implement cursor visibility; the TUI
            # remains usable when hiding the cursor is unsupported.
            pass
        stdscr.keypad(True)
        mode = "projects" if not args.project and len(projects) > 1 else "tasks"
        if mode == "tasks":
            load_project(project)
        while True:
            if mode == "projects":
                lines = [f"{index + 1}. {item.get('name')} [{item.get('id')}]"
                         for index, item in enumerate(projects)]
                selected = project_index
                lines = [("> " if index == selected else "  ") + line
                         for index, line in enumerate(lines)]
                draw(stdscr, _label(lang, "projects"), lines,
                     "↑/↓ or j/k  Enter: select  q: quit")
                key = stdscr.getch()
                if key in (ord("q"), 27):
                    return
                if key in (curses.KEY_UP, ord("k")):
                    project_index = max(0, project_index - 1)
                elif key in (curses.KEY_DOWN, ord("j")):
                    project_index = min(len(projects) - 1, project_index + 1)
                elif key in (curses.KEY_ENTER, 10, 13):
                    project = projects[project_index]
                    load_project(project)
                    mode = "tasks"
                continue

            task = task_for_current()
            tasks = (workspace or {}).get("tasks", [])
            lines = [
                f"{_label(lang, 'project')}: {project.get('name')} [{project.get('id')}]",
                f"{_label(lang, 'preflight')}: {_status((preflight or {}).get('status'), lang)}",
                "",
            ]
            for index, item in enumerate(tasks):
                marker = "> " if index == task_index else "  "
                lines.append(marker + f"{item.get('title')} [{_status(item.get('execution_status'), lang)}]")
            if task:
                executions = [item for item in (workspace or {}).get("executions", [])
                              if item.get("task_id") == task.get("id")]
                latest_execution = executions[0] if executions else None
                lines.extend([
                    "",
                    f"{_label(lang, 'task')}: {task.get('title')}",
                    f"{task.get('objective')}",
                    f"{_label(lang, 'transport')}: {_label(lang, args.transport)}",
                    f"{_label(lang, 'status')}: {_status(task.get('execution_status'), lang)}",
                    f"{_label(lang, 'acceptance')}: {_status(task.get('acceptance_status'), lang)}",
                    f"{_label(lang, 'evidence')}: {len(executions)}",
                    f"{_label(lang, 'execution')}: "
                    f"{_status((latest_execution or {}).get('status'), lang)} / "
                    f"{_status((latest_execution or {}).get('application_status'), lang)}",
                    "",
                    message,
                ])
            else:
                lines.extend(["", _label(lang, "none"), "", message])
            draw(stdscr, _label(lang, "tasks"), lines,
                 "↑/↓ or j/k: task  n: new  Enter: start  v: view  a: apply  s: stop  p/f/w: acceptance  x: export  c: cleanup  r: refresh  b: projects  q: quit")
            key = stdscr.getch()
            if key in (ord("q"), 27):
                return
            if key in (ord("b"), ord("B")):
                mode = "projects"
            elif key in (curses.KEY_UP, ord("k")) and tasks:
                task_index = max(0, task_index - 1)
            elif key in (curses.KEY_DOWN, ord("j")) and tasks:
                task_index = min(len(tasks) - 1, task_index + 1)
            elif key in (ord("r"), ord("R")):
                load_project(project)
                message = _label(lang, "read_only")
            elif key in (ord("n"), ord("N")):
                create_task(stdscr)
            elif key in (ord("x"), ord("X")):
                export_project(stdscr)
            elif key in (curses.KEY_ENTER, 10, 13) and task:
                execute_start(stdscr, task)
            elif key in (ord("a"), ord("A")) and task:
                execute_apply(stdscr, task)
            elif key in (ord("v"), ord("V")) and task:
                view_execution(stdscr, task)
            elif key in (ord("s"), ord("S")) and task:
                execute_stop(stdscr, task)
            elif key in (ord("p"), ord("P")) and task:
                execute_acceptance(stdscr, task, "passed")
            elif key in (ord("f"), ord("F")) and task:
                execute_acceptance(stdscr, task, "failed")
            elif key in (ord("w"), ord("W")) and task:
                execute_acceptance(stdscr, task, "waived")
            elif key in (ord("c"), ord("C")) and task:
                execute_cleanup(stdscr, task)

    curses.wrapper(app)
    return 0


def run(args: argparse.Namespace, *, api: AtlasApi | None = None,
        output: Any = print) -> dict:
    lang = args.lang
    api = api or AtlasApi(args.base_url, args.timeout)
    if args.interactive:
        _interactive(api, args)
        return {}
    if args.execution:
        if not args.project:
            raise AtlasCliError("--project is required with --execution")
        execution = api.get(f"/api/projects/{quote(args.project, safe='')}/executions/{quote(args.execution, safe='')}")
        if args.cleanup:
            execution = api.post(
                f"/api/projects/{quote(args.project, safe='')}/executions/{quote(args.execution, safe='')}/cleanup")
            output(f"{_label(lang, 'cleaned')}: {execution.get('id', args.execution)}")
        else:
            output(json.dumps(_execution_summary(execution, lang), ensure_ascii=False, indent=2))
        return execution

    projects = api.get("/api/projects")
    project = _project_match(projects, args.project)
    if not project:
        if not projects:
            raise AtlasCliError(_label(lang, "no_project"))
        output(f"{_label(lang, 'projects')}:")
        for item in projects:
            output(f"  - {item.get('id')}  {item.get('name')}")
        raise AtlasCliError(_label(lang, "no_project"))
    project_id = project["id"]
    workspace = api.get(f"/api/projects/{quote(project_id, safe='')}/workspace")
    preflight = api.get(f"/api/projects/{quote(project_id, safe='')}/harness/preflight")
    task = _task_match(workspace.get("tasks", []) or [], args.task)
    if args.start:
        if not task:
            raise AtlasCliError(_label(lang, "no_task"))
        output(f"{_label(lang, 'starting')}: {task.get('title')} [{task.get('id')}]" )
        execution = api.post(
            f"/api/projects/{quote(project_id, safe='')}/tasks/{quote(task['id'], safe='')}/executions",
            {"transport": args.transport, "model": args.model} if args.model else
            {"transport": args.transport})
        if execution.get("status") not in {"completed", "failed", "stopped"}:
            execution = _poll(api, project_id, execution["id"], lang,
                              timeout=args.timeout)
        output(json.dumps(_execution_summary(execution, lang), ensure_ascii=False, indent=2))
        return execution
    if args.cleanup:
        raise AtlasCliError("--cleanup requires --execution")
    _print_project(project, workspace, preflight, lang, output=output)
    output(_label(lang, "read_only"))
    return {"project": project, "workspace": workspace, "preflight": preflight}


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Atlas project workbench terminal entry point")
    p.add_argument("--base-url", default=os.environ.get("ATLAS_API_URL", "http://127.0.0.1:5199"))
    p.add_argument("--project", help="project id or exact name")
    p.add_argument("--task", help="task id or exact title")
    p.add_argument("--execution", help="execution id for status or cleanup")
    p.add_argument("--start", action="store_true", help="start the selected task")
    p.add_argument("--cleanup", action="store_true", help="clean a terminal execution worktree")
    p.add_argument("--interactive", action="store_true", help="open the keyboard-first terminal UI")
    p.add_argument("--transport", choices=("http", "cli"), default="cli")
    p.add_argument("--model")
    p.add_argument("--lang", choices=("zh", "en"), default="zh")
    p.add_argument("--timeout", type=float, default=30.0)
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        run(args)
    except AtlasCliError as error:
        print(f"Atlas: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
