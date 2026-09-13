"""Atlas-owned, review-before-adopt baselines for local U17 workspaces."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess

from project_store import ProjectStoreError
from workspace_snapshot import DEFAULT_IGNORES, compare_snapshots, snapshot_workspace


PURPOSE = "project-baseline"
MAX_FOCUS_PATHS = 20
MAX_READ_FILES = 80
MAX_READ_CHARS = 400_000
MAX_FILE_CHARS = 60_000
MAX_GIT_OUTPUT = 2_000_000
TEXT_SUFFIXES = {
    ".c", ".cc", ".cpp", ".css", ".csv", ".go", ".graphql", ".h", ".hpp",
    ".html", ".ini", ".java", ".js", ".json", ".jsx", ".kt", ".md", ".mjs",
    ".py", ".rb", ".rs", ".rst", ".sh", ".sql", ".svelte", ".swift", ".toml",
    ".ts", ".tsx", ".txt", ".vue", ".xml", ".yaml", ".yml",
}
CODE_SUFFIXES = {
    ".c", ".cc", ".cpp", ".go", ".h", ".hpp", ".java", ".js", ".jsx", ".kt",
    ".mjs", ".py", ".rb", ".rs", ".sh", ".sql", ".svelte", ".swift", ".ts",
    ".tsx", ".vue",
}
MANIFEST_NAMES = {
    "cargo.toml", "composer.json", "deno.json", "deno.jsonc", "gemfile", "go.mod",
    "package.json", "pom.xml", "pyproject.toml", "requirements.txt", "setup.cfg",
}


def capture_project_baseline(store, project_id: str, focus_paths=None,
                             expected_baseline_id: str | None = None,
                             expected_content_fingerprint: str | None = None) -> dict:
    project = store.get_project(project_id)
    previous = latest_project_baseline(store, project_id)
    if previous:
        if expected_baseline_id is None:
            raise ProjectStoreError("expected_baseline_id is required to adopt a new baseline")
        if previous["id"] != expected_baseline_id:
            raise ProjectStoreError("workspace baseline changed; refresh before accepting")
        if not expected_content_fingerprint:
            raise ProjectStoreError(
                "expected_content_fingerprint is required to adopt a reviewed workspace")
    elif expected_baseline_id is not None:
        raise ProjectStoreError("workspace baseline changed; refresh before accepting")
    manifest = inspect_project_workspace(project["workspace"], focus_paths)
    if previous and _content_fingerprint(manifest) != expected_content_fingerprint:
        raise ProjectStoreError("workspace changed after review; check changes again")
    saved = store.save_snapshot(project_id, manifest, "observed")
    result = baseline_summary(saved)
    result["changes_from_previous"] = (
        compare_project_manifests(previous["manifest"], manifest) if previous else None)
    return result


def check_project_changes(store, project_id: str) -> dict:
    project = store.get_project(project_id)
    baseline = latest_project_baseline(store, project_id)
    if not baseline:
        raise ProjectStoreError("project workspace has no accepted baseline")
    focus_paths = baseline["manifest"].get("coverage", {}).get("focus_paths", [])
    current = inspect_project_workspace(project["workspace"], focus_paths)
    return {
        "baseline": baseline_summary(baseline),
        "current": transient_summary(current),
        "changes": compare_project_manifests(baseline["manifest"], current),
    }


def list_project_baselines(store, project_id: str) -> list[dict]:
    return [baseline_summary(item) for item in store.list_snapshots(project_id)
            if item["manifest"].get("purpose") == PURPOSE]


def get_project_baseline(store, project_id: str, snapshot_id: str) -> dict:
    item = store.get_snapshot(project_id, snapshot_id)
    if item["manifest"].get("purpose") != PURPOSE:
        raise ProjectStoreError("workspace baseline not found")
    return item


def latest_project_baseline(store, project_id: str) -> dict | None:
    for item in store.list_snapshots(project_id):
        if item["manifest"].get("purpose") == PURPOSE:
            return item
    return None


def inspect_project_workspace(root: str | Path, focus_paths=None) -> dict:
    snapshot = snapshot_workspace(root)
    normalized_focus = _focus_paths(focus_paths, snapshot["files"])
    inventory = _inventory(snapshot)
    evidence, coverage = _read_evidence(snapshot, normalized_focus, inventory)
    git = _git_state(Path(snapshot["root"]))
    observations = _observations(snapshot, inventory, evidence, coverage)
    manifest = {
        **snapshot,
        "purpose": PURPOSE,
        "git": git,
        "inventory": inventory,
        "coverage": coverage,
        "evidence_files": evidence,
        "observations": observations,
    }
    manifest["report_markdown"] = render_baseline_report(manifest)
    return manifest


def compare_project_manifests(before: dict, after: dict) -> dict:
    difference = compare_snapshots(before, after)
    changed_paths = sorted(set(
        difference["added"] + difference["removed"] + difference["modified"]))
    coverage = before.get("coverage") or {}
    focus = coverage.get("focus_paths") or []
    read_paths = set(coverage.get("read_paths") or [])
    reviewed = [path for path in changed_paths
                if path in read_paths or any(_matches(path, value) for value in focus)]
    outside = [path for path in changed_paths if path not in set(reviewed)]
    git_before, git_after = before.get("git") or {}, after.get("git") or {}
    git_revision_changed = any(git_before.get(key) != git_after.get(key)
                               for key in ("repository", "root", "head", "branch"))
    git_worktree_state_changed = any(git_before.get(key) != git_after.get(key)
                                     for key in ("dirty", "changes", "truncated"))
    git_changed = git_revision_changed or git_worktree_state_changed
    git_errors = bool(
        git_before.get("repository") and git_before.get("error")
        or git_after.get("repository") and git_after.get("error"))
    errors = bool(difference["before_errors"] or difference["after_errors"] or git_errors)
    return {
        **difference,
        "changed_paths": changed_paths,
        "reviewed_scope_changes": reviewed,
        "outside_review_scope_changes": outside,
        "git_state_changed": git_changed,
        "git_revision_changed": git_revision_changed,
        "git_worktree_state_changed": git_worktree_state_changed,
        "requires_focused_review": bool(reviewed or git_revision_changed or errors),
        "has_unread_changes": bool(outside),
        "comparison_limited_by_errors": errors,
    }


def baseline_summary(record: dict) -> dict:
    summary = transient_summary(record["manifest"])
    return {
        "id": record["id"], "project_id": record["project_id"],
        "phase": record["phase"], "workspace_root": record["workspace_root"],
        "fingerprint": record["fingerprint"], "created_at": record["created_at"],
        **summary,
    }


def transient_summary(manifest: dict) -> dict:
    return {
        "root": manifest["root"],
        "git": manifest["git"],
        "inventory": manifest["inventory"],
        "coverage": manifest["coverage"],
        "observations": manifest["observations"],
        "report_markdown": manifest["report_markdown"],
        "snapshot_errors": manifest.get("errors") or [],
        "content_fingerprint": _content_fingerprint(manifest),
    }


def render_baseline_report(manifest: dict) -> str:
    inventory, coverage = manifest["inventory"], manifest["coverage"]
    observations, git = manifest["observations"], manifest["git"]
    lines = [
        "# 项目工作区基线", "",
        f"- 工作区：`{manifest['root']}`",
        f"- 文件指纹：{inventory['file_count']} 个文件，{inventory['total_bytes']} 字节",
        f"- 内容读取：{len(coverage['read_paths'])} 个文件；部分读取 {len(coverage['partial_paths'])} 个",
        f"- 重点范围：{', '.join(f'`{value}`' for value in coverage['focus_paths']) or '未指定，仅读取入口文档和清单'}",
        "", "## Git 状态", "",
    ]
    if git["repository"]:
        lines.extend([
            f"- 仓库根：`{git['root']}`", f"- 分支：`{git['branch'] or 'detached/unknown'}`",
            f"- HEAD：`{git['head'] or 'unborn/unknown'}`",
            f"- 未提交路径：{len(git['changes'])} 个" + ("（列表已截断）" if git["truncated"] else ""),
        ])
        if git["error"]:
            lines.append(f"- Git 状态读取受限：{git['error']}")
    elif git["error"]:
        lines.append(f"- Git 状态不可用：{git['error']}")
    else:
        lines.append("- 未发现可读取的 Git 工作树；文件指纹仍可作为基线。")
    lines.extend(["", "## 文档描述（尚未验证）", ""])
    if observations["document_claims"]:
        for item in observations["document_claims"]:
            lines.append(f"- `{item['path']}`：{item['summary']}")
    else:
        lines.append("- 当前读取范围内没有可解析的说明文档。")
    lines.extend(["", "## 代码线索（不等于运行事实）", ""])
    for item in observations["code_clues"]:
        lines.append(f"- {item['summary']}")
    lines.extend(["", "## 运行验证", ""])
    if observations["runtime_verified"]:
        for item in observations["runtime_verified"]:
            lines.append(f"- {item['summary']}")
    else:
        lines.append("- 本次基线没有执行项目命令、测试或交互验证。")
    lines.extend(["", "## 未知与未检查范围", ""])
    for item in observations["unknown"]:
        lines.append(f"- {item['summary']}")
    lines.extend([
        "", "> 此报告没有提及某项能力，不代表该能力不存在；它只描述本次读取和验证范围。", "",
    ])
    return "\n".join(lines)


def _inventory(snapshot: dict) -> dict:
    paths = list(snapshot["files"])
    file_paths = [path for path in paths if snapshot["files"][path]["kind"] == "file"]
    documents = sorted(path for path in file_paths if _is_document(path))
    manifests = sorted(path for path in file_paths if Path(path).name.lower() in MANIFEST_NAMES)
    tests = sorted(path for path in file_paths if _is_test(path))
    suffixes = Counter(Path(path).suffix.lower() or "[no suffix]" for path in file_paths)
    code_suffixes = Counter(Path(path).suffix.lower() for path in file_paths
                            if Path(path).suffix.lower() in CODE_SUFFIXES)
    return {
        "file_count": len(file_paths),
        "symlink_count": sum(1 for value in snapshot["files"].values()
                             if value["kind"] == "symlink"),
        "total_bytes": sum(value.get("size", 0) for value in snapshot["files"].values()),
        "document_paths": documents[:200],
        "document_paths_truncated": len(documents) > 200,
        "manifest_paths": manifests[:100],
        "test_paths": tests[:200],
        "test_paths_truncated": len(tests) > 200,
        "suffix_counts": dict(suffixes.most_common(30)),
        "code_suffix_counts": dict(code_suffixes.most_common()),
    }


def _read_evidence(snapshot: dict, focus_paths: list[str], inventory: dict):
    files = snapshot["files"]
    automatic = set(inventory["document_paths"] + inventory["manifest_paths"])
    focused = {path for path, value in files.items()
               if value["kind"] == "file"
               and any(_matches(path, focus) for focus in focus_paths)}
    candidates = sorted(focused) + sorted(automatic - focused)
    evidence = {}
    skipped = []
    total = 0
    root = Path(snapshot["root"])
    for path in candidates:
        if len(evidence) >= MAX_READ_FILES:
            skipped.append({"path": path, "reason": "file-count-limit"})
            continue
        suffix = Path(path).suffix.lower()
        if suffix not in TEXT_SUFFIXES and Path(path).name.lower() not in MANIFEST_NAMES \
                and not _is_document(path):
            skipped.append({"path": path, "reason": "non-text-or-unsupported"})
            continue
        remaining = MAX_READ_CHARS - total
        if remaining <= 0:
            skipped.append({"path": path, "reason": "total-content-limit"})
            continue
        limit = min(MAX_FILE_CHARS, remaining)
        try:
            with (root / path).open("rb") as stream:
                payload = stream.read(limit + 1)
        except OSError as error:
            skipped.append({"path": path, "reason": f"read-error: {error}"})
            continue
        if b"\0" in payload:
            skipped.append({"path": path, "reason": "binary-content"})
            continue
        truncated = len(payload) > limit or files[path].get("size", 0) > len(payload)
        text = payload[:limit].decode("utf-8", errors="replace")
        evidence[path] = {
            "sha256": files[path]["sha256"], "size": files[path].get("size", 0),
            "text": text, "complete": not truncated,
        }
        total += len(text)
    read_paths = sorted(evidence)
    coverage = {
        "ignore_names": sorted(DEFAULT_IGNORES), "focus_paths": focus_paths,
        "hashed_paths": len(files), "read_paths": read_paths,
        "partial_paths": sorted(path for path, value in evidence.items() if not value["complete"]),
        "skipped_count": len(skipped), "skipped": skipped[:200],
        "skipped_truncated": len(skipped) > 200,
        "read_chars": total,
        "limits": {"files": MAX_READ_FILES, "total_chars": MAX_READ_CHARS,
                   "per_file_chars": MAX_FILE_CHARS},
    }
    return evidence, coverage


def _observations(snapshot, inventory, evidence, coverage):
    document_claims = []
    for path in inventory["document_paths"]:
        if path not in evidence:
            continue
        headings = [match.group(1).strip() for match in re.finditer(
            r"(?m)^#{1,3}\s+(.+?)\s*$", evidence[path]["text"])]
        summary = ("已读取；章节包括 " + "、".join(headings[:8])) if headings else "已读取文本内容"
        if not evidence[path]["complete"]:
            summary += "；内容仅部分读取"
        document_claims.append({
            "category": "document_claim", "path": path, "summary": summary,
            "evidence": {"path": path, "sha256": evidence[path]["sha256"],
                         "complete": evidence[path]["complete"]},
        })
    code_clues = []
    if inventory["code_suffix_counts"]:
        languages = "、".join(
            f"{suffix} {count}" for suffix, count in inventory["code_suffix_counts"].items())
        code_clues.append({"category": "code_clue", "summary": f"发现代码文件分布：{languages}。"})
    if inventory["manifest_paths"]:
        code_clues.append({
            "category": "code_clue",
            "summary": "发现工程清单：" + "、".join(f"`{path}`" for path in inventory["manifest_paths"][:12]) + "。",
        })
    if inventory["test_paths"]:
        code_clues.append({
            "category": "code_clue",
            "summary": f"发现 {len(inventory['test_paths'])} 个测试命名路径；本次未执行。",
        })
    unread_files = max(inventory["file_count"] - len(coverage["read_paths"]), 0)
    unknown = [
        {"category": "unknown", "summary": "项目命令、测试、构建和交互行为尚未运行验证。"},
        {"category": "unknown", "summary": f"{unread_files} 个文件只记录了元数据与内容指纹，未读取正文。"},
    ]
    if snapshot.get("errors"):
        unknown.append({"category": "unknown",
                        "summary": f"{len(snapshot['errors'])} 个路径读取失败，比较结论受限。"})
    return {
        "document_claims": document_claims,
        "code_clues": code_clues,
        "runtime_verified": [],
        "unknown": unknown,
    }


def _git_state(root: Path) -> dict:
    inside = _git(root, ["rev-parse", "--is-inside-work-tree"])
    if inside["returncode"] or inside["stdout"].strip() != "true":
        error = inside["error"]
        if "not a git repository" in error.lower():
            error = ""
        return {"repository": False, "root": None, "head": None, "branch": None,
                "dirty": None, "changes": [], "truncated": False,
                "error": error}
    top = _git(root, ["rev-parse", "--show-toplevel"])
    head = _git(root, ["rev-parse", "HEAD"])
    branch = _git(root, ["branch", "--show-current"])
    status = _git(root, ["status", "--porcelain=v1", "--untracked-files=all"])
    raw = status["stdout"]
    truncated = len(raw.encode("utf-8")) > MAX_GIT_OUTPUT
    if truncated:
        raw = raw.encode("utf-8")[:MAX_GIT_OUTPUT].decode("utf-8", errors="replace")
    changes = [line for line in raw.splitlines() if line][:500]
    errors = []
    for item in (top, head, branch, status):
        if item["returncode"] and item["error"] and item["error"] not in errors:
            errors.append(item["error"])
    return {
        "repository": True,
        "root": top["stdout"].strip() if not top["returncode"] else None,
        "head": head["stdout"].strip() if not head["returncode"] else None,
        "branch": branch["stdout"].strip() if not branch["returncode"] else None,
        "dirty": bool(changes) if not status["returncode"] else None,
        "changes": changes,
        "truncated": truncated or len(raw.splitlines()) > 500,
        "error": "; ".join(errors),
    }


def _git(root: Path, args: list[str]) -> dict:
    try:
        environment = {
            **os.environ,
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_TERMINAL_PROMPT": "0",
        }
        result = subprocess.run(
            ["git", "-C", str(root), *args], capture_output=True, text=True,
            errors="replace", timeout=10, env=environment)
        return {"returncode": result.returncode, "stdout": result.stdout,
                "error": result.stderr.strip()}
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"returncode": 1, "stdout": "", "error": str(error)}


def _focus_paths(values, files: dict) -> list[str]:
    if values is None:
        return []
    if not isinstance(values, list) or len(values) > MAX_FOCUS_PATHS:
        raise ValueError(f"focus_paths must be a list of at most {MAX_FOCUS_PATHS} paths")
    result = []
    for value in values:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("focus_paths must contain non-empty relative paths")
        raw = value.strip().replace("\\", "/").rstrip("/")
        path = PurePosixPath(raw)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("focus_paths must stay inside the project workspace")
        normalized = "" if raw == "." else path.as_posix()
        if normalized and not any(_matches(candidate, normalized) for candidate in files):
            raise ValueError(f"focus path does not exist in the workspace snapshot: {normalized}")
        if normalized not in result:
            result.append(normalized)
    return result


def _matches(path: str, focus: str) -> bool:
    return not focus or path == focus or path.startswith(focus + "/")


def _is_document(path: str) -> bool:
    value = path.lower()
    name = Path(value).name
    return (name.startswith("readme") or name.startswith("changelog")
            or name in {"contributing.md", "architecture.md", "agents.md"}
            or value.startswith("docs/") and Path(value).suffix in {".md", ".rst", ".txt"})


def _is_test(path: str) -> bool:
    value = path.lower()
    name = Path(value).name
    return (value.startswith("test/") or value.startswith("tests/") or "/tests/" in value
            or name.startswith("test_") or ".test." in name or ".spec." in name)


def _fingerprint(value) -> str:
    return hashlib.sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _content_fingerprint(manifest: dict) -> str:
    return _fingerprint({
        "root": manifest["root"], "files": manifest["files"],
        "errors": manifest.get("errors") or [], "git": manifest["git"],
    })
