#!/usr/bin/env python3
"""Draft-leaf API server (local, stdlib only).

  python3 drafts_api.py [--port 5199]

Endpoints:
  GET    /api/health
  GET    /api/ready
  GET    /api/drafts                     list drafts (frontmatter + lint_ok)
  POST   /api/drafts                     create + start engine in background
                                         body: {name?, name_zh?, desc?, link?, force?}
                                         name 留空 -> 临时 wip-slug，引擎调研后在 identity.json 定名
  GET    /api/drafts/<slug>              {front, body, body_sha256, status, research, lint, collision}
  PUT    /api/drafts/<slug>              save body   {body, expected_body_sha256?}
  DELETE /api/drafts/<slug>              delete draft + research files + review entry
  POST   /api/dedupe                     {slug, body_sha256} -> vector top-5 stored in review.json
  GET    /api/review                     full review.json
  GET    /api/sources/<slug>             canonical source manifest + outlines
  GET    /api/sources/<kind>/<slug>      canonical Markdown, optionally paged
                                        ?section=<outline-id>&offset=0&limit=12000
  GET    /api/projects                   list U17 projects
  POST   /api/projects                   create {name,objective,mode,workspace?}
                                         optional starter_reference pins a type source
  GET    /api/projects/<id>              read one U17 project
  DELETE /api/projects/<id>              delete Atlas records; preserve local workspace
  GET    /api/projects/<id>/references   list saved source excerpts + version state
  POST   /api/projects/<id>/references   save canonical {kind,slug,section?,note?};
                                        kind=application|research|app
  PATCH  /api/projects/<id>/references/<reference-id>
                                        update {note?,read_status?}
  GET    /api/projects/<id>/acceptance-migration  dry-run legacy acceptance report
  POST   /api/projects/<id>/acceptance-migration/backfill
  GET    /api/projects/<id>/workspace    requirements, decisions, documents
  POST   /api/projects/<id>/requirements
  PATCH  /api/projects/<id>/requirements/<requirement-id>
  POST   /api/projects/<id>/requirements/<requirement-id>/confirm
  POST   /api/projects/<id>/decisions
  POST   /api/projects/<id>/documents
  GET    /api/projects/<id>/documents/<document-id>/versions
  POST   /api/projects/<id>/documents/<document-id>/versions
  GET    /api/projects/<id>/documents/<document-id>/diff?from=1&to=2
  POST   /api/projects/<id>/backup       create scoped non-destructive backup
  GET    /api/projects/<id>/backups      list validated project backups
  GET    /api/projects/<id>/backups/<name> download a backup archive
  POST   /api/projects/<id>/backups/<name>/restore-target
  POST   /api/projects/<id>/backups/<name>/restore
  GET    /api/projects/<id>/restore-status/<restore-id>
  POST   /api/projects/<id>/restore-status/<restore-id>/recover
  DELETE /api/projects/<id>/backups/<name> delete one backup after confirmation
  POST   /api/projects/<id>/export       create self-contained Markdown bundle
  GET    /api/projects/<id>/generation-runs
  POST   /api/projects/<id>/generation-runs
                                        {mode,document_kinds?,improvement_goal?,model?,
                                         document_id?,section_heading?,revision_instruction?}
  GET    /api/projects/<id>/generation-runs/<generation-id>
  POST   /api/projects/<id>/generation-runs/<generation-id>/apply
  GET    /api/projects/<id>/workspace-baselines
  POST   /api/projects/<id>/workspace-baselines
  GET    /api/projects/<id>/workspace-baselines/<snapshot-id>
  POST   /api/projects/<id>/iterations
  POST   /api/projects/<id>/iterations/<iteration-id>/status
  POST   /api/projects/<id>/tasks
  POST   /api/projects/<id>/tasks/<task-id>/executions
  GET    /api/projects/<id>/executions/<execution-id>
  POST   /api/projects/<id>/executions/<execution-id>/reconcile|continue|stop|apply|recover-apply|cleanup|permission|question
  POST   /api/projects/<id>/tasks/<task-id>/acceptance
  GET    /api/settings/model                provider list + resolved state (keys masked)
  POST   /api/settings/model/providers      add/update a provider
  DELETE /api/settings/model/providers/<id> remove a provider (explicit confirm)
  POST   /api/settings/model/providers/<id>/test    probe a provider
  GET    /api/settings/model/providers/<id>/models  live model list
  POST   /api/settings/model/default        set the default provider/model
  POST   /api/settings/model/embedding      set the embedding endpoint
  POST   /api/settings/model/import         import credentials from OpenCode
  GET    /api/ask/threads                   list conversations
  POST   /api/ask/threads                   create a conversation
  GET    /api/ask/threads/<id>              one conversation (messages + steps)
  POST   /api/ask/threads/<id>/messages     ask a question (background)
  DELETE /api/ask/threads/<id>              delete a conversation (explicit confirm)

Run alongside `npm run dev` (vite proxies /api -> :5199).
"""
import argparse
import datetime
import hashlib
import http.client
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import socket
import ssl
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urljoin, urlparse, urlsplit

from atlas_runtime import PACK as DATA_PACK, atomic_write, corpus_lock, recover_publication
from review_store import (
    load_review, update_review, remove_review, fingerprint, corpus_revision,
    review_current, valid_slug,
)
from atlas_sources import SourceError, read_source, source_manifest
from project_store import ProjectStore, ProjectStoreError
from project_workflow import (
    add_document_version, confirm_requirement, create_decision,
    create_document as create_project_document,
    create_requirement as create_project_requirement,
    document_diff, document_versions, export_bundle, project_workspace,
    update_requirement as update_project_requirement,
)
from project_generation import (
    ProjectLifecycleBusy, apply_generation_item, execute_generation, generation_staleness,
    list_generations, mark_generation_interrupted, prepare_generation, project_lifecycle_lock,
    read_generation,
)
from project_open_items import list_open_items, resolve_open_item
from project_backup import (
    BACKUP_DELETE_CONFIRMATION, ProjectBackupError, RESTORE_RECOVERY_CONFIRMATION,
    RESTORE_TARGET_CONFIRMATION, backup_archive_path, create_project_backup,
    delete_project_backup, inspect_prepared_project_restore,
    list_project_backups, prepare_project_restore,
    recover_prepared_project_restore, restore_prepared_project_backup,
)
from privacy import redact_text
from runtime_recovery import acquire_project_store_lock, recover_atlas_runtime
from project_baseline import (
    capture_project_baseline, check_project_changes, get_project_baseline,
    list_project_baselines,
)
from opencode_cli_adapter import HarnessCompatibilityError, preflight as opencode_preflight
import atlas_model
import atlas_ask
from template_factory import api as factory_api
from template_factory.store import FactoryError
from execution_service import (
    apply_execution_result,
    cleanup_execution_workspace,
    continue_execution,
    create_iteration as create_project_iteration,
    create_task as create_execution_task,
    rebase_iteration as rebase_project_iteration,
    reconcile_execution, recover_interrupted_apply,
    reply_permission as reply_execution_permission,
    reply_question as reply_execution_question, start_execution, stop_execution,
)
PACK = str(DATA_PACK)
sys.path.insert(0, PACK)
from leaf_lint import lint, parse_front  # noqa: E402
import draft_new as dn  # noqa: E402

DRAFTS = os.path.join(PACK, "drafts")
PROMPT = os.path.join(PACK, "drafts_prompt.md")
WORKDIR = os.path.dirname(PACK)
REVIEW = os.path.join(DRAFTS, "review.json")

GEN_LOCK = threading.Semaphore(2)          # max concurrent engine runs
GEN_THREADS = {}
GEN_THREADS_LOCK = threading.Lock()
TRANSLATION_LOCK = threading.Lock()
TRANSLATION_THREADS = {}
PROMOTE_LOCK = threading.Lock()
PROMOTE_THREADS = set()
PROJECT_STORE = None
PROJECT_STORE_LOCK = threading.Lock()
PROJECT_STORE_PROCESS_LOCK = None
PROJECT_RECOVERY_REPORT = None
_PROJECT_RUNTIME_INITIALIZING = False
PROJECT_GENERATION_LOCK = threading.Semaphore(1)
PROJECT_GENERATION_THREADS = {}


class SourceRevisionConflict(ValueError):
    """The source changed after the reader displayed its fingerprint."""


class DraftRevisionConflict(ValueError):
    """The draft body changed after the reviewer's client loaded it."""


def _body_sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _require_body_revision(slug: str, expected: object) -> str:
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise DraftRevisionConflict("body revision is required")
    path = draft_path(slug)
    _, body = parse_front(Path(path).read_text(encoding="utf-8"))
    current = _body_sha256(body)
    if current != expected:
        raise DraftRevisionConflict("草稿正文已变化，请重新加载后再操作")
    return current


def get_project_store():
    global PROJECT_STORE
    created = False
    if PROJECT_STORE is None:
        with PROJECT_STORE_LOCK:
            if PROJECT_STORE is None:
                PROJECT_STORE = ProjectStore()
                created = True
                redacted = PROJECT_STORE.redact_persisted_evidence()
                if redacted["executions"] or redacted["tasks"]:
                    print(
                        "[api] redacted persisted evidence:",
                        json.dumps(redacted, sort_keys=True))
    if created and PROJECT_STORE_PROCESS_LOCK is None \
            and PROJECT_RECOVERY_REPORT is None and not _PROJECT_RUNTIME_INITIALIZING:
        initialize_project_runtime()
    return PROJECT_STORE


def initialize_project_runtime():
    global PROJECT_STORE_PROCESS_LOCK, PROJECT_RECOVERY_REPORT, _PROJECT_RUNTIME_INITIALIZING
    if PROJECT_STORE_PROCESS_LOCK is not None:
        return PROJECT_RECOVERY_REPORT
    _PROJECT_RUNTIME_INITIALIZING = True
    try:
        configured = os.environ.get("ATLAS_PROJECT_STORE", "").strip()
        store_path = (Path(configured).expanduser() if configured else
                      Path(DATA_PACK) / "projects" / "atlas-projects.sqlite")
        lock = acquire_project_store_lock(store_path)
        try:
            store = get_project_store()
            PROJECT_RECOVERY_REPORT = recover_atlas_runtime(store)
        except BaseException:
            lock.close()
            raise
        PROJECT_STORE_PROCESS_LOCK = lock
    finally:
        _PROJECT_RUNTIME_INITIALIZING = False
    return PROJECT_RECOVERY_REPORT


def start_project_generation(project_id, body, store=None):
    if not isinstance(body, dict):
        raise ValueError("request body must be an object")
    allowed = {
        "mode", "document_kinds", "model", "improvement_goal",
        "document_id", "section_heading", "revision_instruction",
    }
    unknown = set(body) - allowed
    if unknown:
        raise ValueError(f"unknown generation fields: {', '.join(sorted(unknown))}")
    store = store or get_project_store()
    run = prepare_generation(
        store, project_id, body.get("mode"), body.get("document_kinds"),
        body.get("model", os.environ.get("ATLAS_PROJECT_MODEL", "")),
        body.get("improvement_goal", ""), body.get("document_id", ""),
        body.get("section_heading", ""), body.get("revision_instruction", ""))
    thread = threading.Thread(
        target=_run_project_generation, args=(store, project_id, run["id"]), daemon=True)
    PROJECT_GENERATION_THREADS[run["id"]] = thread
    try:
        thread.start()
    except BaseException:
        PROJECT_GENERATION_THREADS.pop(run["id"], None)
        mark_generation_interrupted(store, project_id, run["id"])
        raise
    return run


def _run_project_generation(store, project_id, run_id):
    try:
        with PROJECT_GENERATION_LOCK:
            execute_generation(store, project_id, run_id)
    except BaseException as error:
        print(f"[project-generation] {run_id}: {error}")
    finally:
        PROJECT_GENERATION_THREADS.pop(run_id, None)


def project_generation_status(store, project_id, run_id):
    run = read_generation(store, project_id, run_id)
    if run["status"] in {"queued", "running"} and run_id not in PROJECT_GENERATION_THREADS:
        run = mark_generation_interrupted(store, project_id, run_id)
    staleness = generation_staleness(store, project_id, run)
    return {**run, "stale": staleness["stale"], "stale_known": staleness["known"]}


def project_generation_list(store, project_id):
    return [project_generation_status(store, project_id, run["id"])
            for run in list_generations(store, project_id)]


def create_project(body, store=None, pack=None):
    if not isinstance(body, dict):
        raise ValueError("request body must be an object")
    for field in ("name", "objective", "mode"):
        if not isinstance(body.get(field), str) or not body[field].strip():
            raise ValueError(f"{field} is required")
    if body["mode"] == "existing" and (
            not isinstance(body.get("workspace"), str) or not body["workspace"].strip()):
        raise ValueError("workspace is required for an existing project")
    if body.get("workspace") is not None and not isinstance(body["workspace"], str):
        raise ValueError("workspace must be a path")
    requested_workspace = (body.get("workspace") or "").strip()
    workspace_existed = bool(
        requested_workspace and Path(requested_workspace).expanduser().exists())
    if body["mode"] == "existing" and not (
            requested_workspace and Path(requested_workspace).expanduser().is_dir()):
        raise ValueError("workspace must be an existing directory")
    starter = body.get("starter_reference")
    if starter is not None and not isinstance(starter, dict):
        raise ValueError("starter_reference must be an object")
    project_store = store or get_project_store()
    project = project_store.create_project(
        body["name"], body["objective"], body.get("workspace"), body["mode"])
    if starter is not None:
        try:
            collect_atlas_reference(
                project["id"], starter, store=project_store, pack=pack or PACK)
        except Exception:
            project_store.delete_project(project["id"])
            if body["mode"] == "new" and not workspace_existed:
                shutil.rmtree(project["workspace"], ignore_errors=True)
            raise
    return project


def _has_symlink_component(path: Path) -> bool:
    current = path if path.is_absolute() else path.absolute()
    while True:
        if current.exists() or current.is_symlink():
            if current.is_symlink():
                return True
        if current.parent == current:
            return False
        current = current.parent


def _remove_project_artifact_root(root: Path, project_id: str) -> tuple[bool, str | None]:
    if _has_symlink_component(root):
        return False, "artifact root contains a symlink"
    if root.exists() and not root.is_dir():
        return False, "artifact root is not a directory"
    raw_target = root / project_id
    target = raw_target.resolve()
    if target.parent != root.resolve():
        return False, "artifact path escaped the managed root"
    if not raw_target.exists() and not raw_target.is_symlink():
        return False, None
    try:
        if raw_target.is_symlink() or raw_target.is_file():
            raw_target.unlink()
        else:
            shutil.rmtree(raw_target)
    except OSError as error:
        return False, str(error)
    return True, None


def _remove_custom_execution_workspaces(
        project_id: str, source_workspace: str, executions: list[dict],
        default_root: Path) -> tuple[bool, str | None]:
    targets = set()
    for execution in executions:
        raw_workdir = execution.get("workdir")
        if not raw_workdir:
            continue
        workdir = Path(raw_workdir)
        project_root = workdir.parent
        if (not workdir.name.startswith("run_") or project_root.name != project_id
                or workdir.is_symlink() or project_root.is_symlink()):
            return False, f"execution {execution.get('id')} has an unmanaged workdir"
        resolved_root = project_root.resolve()
        source_root = Path(source_workspace).resolve()
        try:
            resolved_root.relative_to(source_root)
        except ValueError:
            pass
        else:
            return False, "execution workdir is inside the preserved source workspace"
        try:
            source_root.relative_to(resolved_root)
        except ValueError:
            pass
        else:
            return False, "execution workdir contains the preserved source workspace"
        if _has_symlink_component(default_root):
            return False, "execution root contains a symlink"
        if resolved_root != default_root.resolve() / project_id:
            targets.add(resolved_root)
    removed = False
    for target in sorted(targets, key=str):
        try:
            if target.exists():
                shutil.rmtree(target)
                removed = True
        except OSError as error:
            return removed, str(error)
    return removed, None


def delete_project(project_id, body, store=None):
    if not isinstance(body, dict):
        raise ValueError("request body must be an object")
    if body.get("confirm") != project_id:
        raise ValueError("confirm must match the project id")
    project_store = store or get_project_store()
    try:
        with project_lifecycle_lock(project_store, project_id, blocking=False):
            return _delete_project_locked(project_store, project_id)
    except ProjectLifecycleBusy as error:
        raise ProjectStoreError(str(error)) from error


def _delete_project_locked(project_store, project_id):
    active_generations = [
        run for run in project_generation_list(project_store, project_id)
        if run["status"] in {"queued", "running"}
    ]
    if active_generations:
        raise ProjectStoreError("project has an active generation")
    project = project_store.get_project(project_id)
    executions = project_store.list_executions(project_id)
    result = project_store.delete_project(project_id)
    artifact_root = project_store.path.parent
    removed = []
    cleanup_errors = {}
    for name in ("generation-runs", "execution-workspaces", "execution-evidence", "exports"):
        existed, error = _remove_project_artifact_root(artifact_root / name, project_id)
        if existed:
            removed.append(name)
        if error:
            cleanup_errors[name] = error
    custom_removed, custom_error = _remove_custom_execution_workspaces(
        project_id, project["workspace"], executions,
        artifact_root / "execution-workspaces")
    if custom_removed:
        removed.append("execution-workspaces:custom")
    if custom_error:
        cleanup_errors["execution-workspaces:custom"] = custom_error
    result["artifacts_removed"] = removed
    result["artifact_cleanup_errors"] = cleanup_errors
    return result


def _project_error_code(error):
    message = str(error)
    return 404 if "not found" in message or "does not belong" in message else 409


def collect_atlas_reference(project_id, body, store=None, pack=None):
    if not isinstance(body, dict):
        raise ValueError("request body must be an object")
    kind, slug = body.get("kind"), body.get("slug")
    if kind not in {"application", "research", "app", "case"}:
        raise ValueError("kind must be application, research, app, or case")
    if not isinstance(slug, str) or not slug:
        raise ValueError("slug is required")
    section = body.get("section")
    if section is not None and not isinstance(section, str):
        raise ValueError("section must be an outline id")
    note = body.get("note", "")
    if not isinstance(note, str):
        raise ValueError("note must be text")
    expected_fingerprint = body.get("expected_fingerprint")
    if expected_fingerprint is not None and (
            not isinstance(expected_fingerprint, str)
            or not re.fullmatch(r"[0-9a-f]{64}", expected_fingerprint)):
        raise ValueError("expected_fingerprint must be a sha256 value")
    if kind == "case":
        if section:
            raise ValueError("fixed case references do not have sections")
        saved = _read_case_reference(slug, pack or PACK)
    elif kind == "app":
        if section:
            raise ValueError("app catalog references do not have sections")
        saved = _read_app_catalog(slug, pack or PACK)
    else:
        saved = _read_complete_source(slug, kind, section or None, pack or PACK)
    if expected_fingerprint is not None and saved["fingerprint"] != expected_fingerprint:
        raise SourceRevisionConflict(
            "source changed after it was displayed; refresh before saving the reference")
    return (store or get_project_store()).add_reference(
        project_id, f"atlas:{kind}", slug, saved["fingerprint"],
        locator=(saved["section"] or {}).get("id", ""), excerpt=saved["content"],
        note=note, read_status=body.get("read_status", "read"))


def list_project_references(project_id, store=None, pack=None):
    result = []
    for item in (store or get_project_store()).list_references(project_id):
        current_version = None
        available = False
        tracked = item["source_kind"].startswith("atlas:")
        if tracked:
            kind = item["source_kind"].split(":", 1)[1]
            try:
                if kind == "case":
                    current_version = _read_case_reference(item["source_ref"], pack or PACK)["fingerprint"]
                elif kind == "app":
                    current_version = _read_app_catalog(
                        item["source_ref"], pack or PACK)["fingerprint"]
                else:
                    manifest = source_manifest(item["source_ref"], pack or PACK)
                    current = next(source for source in manifest["sources"] if source["kind"] == kind)
                    current_version = current["fingerprint"]
                available = True
            except (FileNotFoundError, StopIteration, ValueError):
                pass
        result.append({**item, "source_available": available,
                       "current_version": current_version,
                       "stale": tracked and current_version != item["source_version"]})
    return result


def _read_complete_source(slug, kind, section, pack):
    offset, chunks, fingerprint, first = 0, [], None, None
    for _ in range(200):
        page = read_source(slug, kind, section=section, offset=offset,
                           limit=50_000, pack=pack)
        if fingerprint is not None and page["fingerprint"] != fingerprint:
            raise SourceError("source changed while reading; retry")
        fingerprint = page["fingerprint"]
        first = first or page
        chunks.append(page["content"])
        if page["complete"]:
            return {**first, "content": "".join(chunks), "complete": True,
                    "returned_chars": sum(len(chunk) for chunk in chunks),
                    "next_offset": None}
        offset = page["next_offset"]
    raise SourceError("source exceeds safe pagination limit")


def _read_app_catalog(slug, pack):
    valid_slug(slug)
    root = Path(pack)
    apps = json.loads((root / "mvp_apps.json").read_text(encoding="utf-8"))
    classified_path = root / "mvp_apps_classified.json"
    classified = json.loads(classified_path.read_text(encoding="utf-8")) \
        if classified_path.is_file() else []
    app = next((item for item in apps if item.get("slug") == slug), None)
    if app is None:
        raise FileNotFoundError(f"app/{slug}")
    classification = next(
        (item for item in classified if item.get("slug") == slug), {})
    record = {"app": app, "classification": classification}
    canonical = json.dumps(
        record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    fingerprint = hashlib.sha256(
        ("atlas-app-catalog-v1\n" + canonical).encode("utf-8")).hexdigest()
    lines = [
        f"# {app.get('name') or slug}", "", "## Catalog Record", "",
        f"- **Vendor:** {app.get('vendor') or 'Not recorded'}",
    ]
    aliases = app.get("aliases") or []
    if aliases:
        lines.append(f"- **Aliases:** {', '.join(str(value) for value in aliases)}")
    lines.extend(["", app.get("tagline") or "No description recorded.", "",
                  "## Indexed Tasks", ""])
    tasks = app.get("tasks") or []
    lines.extend(f"- {task}" for task in tasks)
    if not tasks:
        lines.append("- No task tags recorded")
    lines.extend(["", "## Atlas Classification", "",
                  f"- **Type:** {classification.get('leaf') or 'Unclassified'}"])
    if classification.get("desc"):
        lines.extend(["", classification["desc"]])
    lines.extend([
        "", "## Coverage", "",
        "Catalog-level evidence only: name, vendor, short description, task tags, and Atlas classification. This record is not a deep product analysis.",
        "",
    ])
    return {"slug": slug, "kind": "app", "fingerprint": fingerprint,
            "section": None, "content": "\n".join(lines), "complete": True}


def _read_case_reference(reference, pack):
    """Read an immutable case revision separately from atlas-app-catalog-v1."""
    from template_factory.store import FactoryStore
    from template_factory.cases import CaseLibrary
    root = os.environ.get("ATLAS_FACTORY_ROOT", str(Path(pack) / "atlas/template-factory"))
    case = CaseLibrary(FactoryStore(root, pack)).resolve_case_ref(reference)
    # Independent review state changes over time; fixed material does not.
    fixed = {key: value for key, value in case.items() if key != "observations"}
    fixed["observations"] = [{key: value for key, value in row.items() if key != "reviews"} for row in case["observations"]]
    content = json.dumps(fixed, ensure_ascii=False, sort_keys=True, indent=2)
    fingerprint = hashlib.sha256(("atlas-case-reference-v1\n" + json.dumps(fixed, ensure_ascii=False, sort_keys=True, separators=(",", ":"))).encode()).hexdigest()
    return {"slug": reference, "kind": "case", "fingerprint": fingerprint,
            "section": None, "content": content, "complete": True}

# ---- 模型生成身份（英文名/中文名/一句话想法，创建时 name/desc 可不填） ----
ID_PROMPT = """你是软件类型语料库的编辑。根据用户提供的信息，为新软件类型起名并概括主张。

用户输入:
- 一句话想法: {desc}
- 调研起点链接: {link}
{extra}

要求:
- name: 英文类型名，2-5 个单词 Title Case（如 CLI Accounting Tool），指类别而非具体产品
- name_zh: 中文名，不超过 12 个汉字
- desc: 一句话中文主张，含「形态+核心机制+边界说明」，风格如「单机命令行复式记账工具（ledger/hledger 一类：纯文本账本、无 GUI）」，不超过 60 字

只输出 JSON: {{"name":"...","name_zh":"...","desc":"..."}}"""


WEB_FETCH_MAX_BYTES = 200_000
WEB_FETCH_MAX_REDIRECTS = 3
WEB_FETCH_TIMEOUT = 20


def _resolve_public_addresses(hostname: str, port: int) -> list[str]:
    try:
        records = socket.getaddrinfo(
            hostname, port, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP)
    except socket.gaierror as exc:
        raise ValueError("link hostname could not be resolved") from exc
    addresses = []
    for record in records:
        address = str(record[4][0]).split("%", 1)[0]
        if address not in addresses:
            addresses.append(address)
    if not addresses:
        raise ValueError("link hostname has no usable address")
    for address in addresses:
        try:
            parsed = ipaddress.ip_address(address)
        except ValueError as exc:
            raise ValueError("link hostname returned an invalid address") from exc
        if not parsed.is_global:
            raise ValueError("link resolves to a private, local, or reserved address")
    return addresses


def _validated_web_url(url: str):
    if not isinstance(url, str) or not url or len(url) > 2048:
        raise ValueError("link must be a non-empty URL no longer than 2048 characters")
    if any(ord(character) < 32 for character in url):
        raise ValueError("link contains unsupported control characters")
    parsed = urlsplit(url)
    scheme = parsed.scheme.lower()
    if scheme not in {"http", "https"}:
        raise ValueError("link must use HTTP or HTTPS")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("link URLs cannot contain credentials")
    if not parsed.hostname:
        raise ValueError("link must include a hostname")
    try:
        hostname = parsed.hostname.encode("idna").decode("ascii").lower()
        port = parsed.port
    except (UnicodeError, ValueError) as exc:
        raise ValueError("link hostname or port is invalid") from exc
    if port is None:
        port = 443 if scheme == "https" else 80
    try:
        literal_address = ipaddress.ip_address(hostname.split("%", 1)[0])
    except ValueError:
        addresses = _resolve_public_addresses(hostname, port)
    else:
        if not literal_address.is_global:
            raise ValueError("link resolves to a private, local, or reserved address")
        addresses = [str(literal_address)]
    return parsed, hostname, port, addresses


class _PinnedHTTPConnection(http.client.HTTPConnection):
    def __init__(self, hostname: str, port: int, addresses: list[str], timeout: int):
        self._pinned_addresses = addresses
        super().__init__(addresses[0], port, timeout=timeout)

    def connect(self):
        self.sock = socket.create_connection(
            [(address, self.port) for address in self._pinned_addresses],
            self.timeout, self.source_address)


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(self, hostname: str, port: int, addresses: list[str], timeout: int):
        self._pinned_addresses = addresses
        self._logical_hostname = hostname
        super().__init__(addresses[0], port, timeout=timeout,
                         context=ssl.create_default_context())

    def connect(self):
        self.sock = socket.create_connection(
            [(address, self.port) for address in self._pinned_addresses],
            self.timeout, self.source_address)
        self.sock = self._context.wrap_socket(
            self.sock, server_hostname=self._logical_hostname)


def _pinned_web_connection(parsed, hostname: str, port: int, addresses: list[str]):
    if parsed.scheme.lower() == "https":
        return _PinnedHTTPSConnection(
            hostname, port, addresses, WEB_FETCH_TIMEOUT)
    return _PinnedHTTPConnection(hostname, port, addresses, WEB_FETCH_TIMEOUT)


def _fetch_text(url, n=3000):
    current_url = url
    for _redirect_count in range(WEB_FETCH_MAX_REDIRECTS + 1):
        parsed, hostname, port, addresses = _validated_web_url(current_url)
        connection = _pinned_web_connection(parsed, hostname, port, addresses)
        default_port = 443 if parsed.scheme.lower() == "https" else 80
        display_host = f"[{hostname}]" if ":" in hostname else hostname
        host_header = display_host if port == default_port else f"{display_host}:{port}"
        target = parsed.path or "/"
        if parsed.query:
            target += f"?{parsed.query}"
        try:
            connection.request("GET", target, headers={
                "Accept": "text/html,text/plain,application/json;q=0.9",
                "Host": host_header,
                "User-Agent": "Mozilla/5.0 atlas-identity/1.0",
            })
            response = connection.getresponse()
            if response.status in {301, 302, 303, 307, 308}:
                location = response.getheader("Location")
                if not location:
                    raise ValueError("link redirect did not include a destination")
                current_url = urljoin(current_url, location)
                continue
            if not 200 <= response.status < 300:
                raise ValueError(f"link fetch returned HTTP {response.status}")
            content_type = response.getheader("Content-Type", "") or ""
            media_type = content_type.split(";", 1)[0].strip().lower()
            allowed_media = {
                "application/json", "application/xhtml+xml", "application/xml",
            }
            if media_type and not (media_type.startswith("text/") or media_type in allowed_media):
                raise ValueError("link response is not a supported text format")
            content_encoding = (response.getheader("Content-Encoding", "") or "").lower().strip()
            if content_encoding and content_encoding not in {"", "identity"}:
                raise ValueError("compressed link responses are not supported")
            content_length = response.getheader("Content-Length")
            if content_length:
                try:
                    declared_length = int(content_length)
                except ValueError as exc:
                    raise ValueError("link response has an invalid Content-Length") from exc
                if declared_length < 0 or declared_length > WEB_FETCH_MAX_BYTES:
                    raise ValueError("link response is too large")
            raw = response.read(WEB_FETCH_MAX_BYTES + 1)
            if len(raw) > WEB_FETCH_MAX_BYTES:
                raise ValueError("link response is too large")
        finally:
            connection.close()

        charset_match = re.search(
            r"charset\s*=\s*[\"']?([A-Za-z0-9._-]+)", content_type, flags=re.I)
        charset = charset_match.group(1) if charset_match else "utf-8"
        try:
            decoded = raw.decode(charset, "replace")
        except LookupError:
            decoded = raw.decode("utf-8", "replace")
        text = re.sub(
            r"<script.*?</script>|<style.*?</style>", " ", decoded,
            flags=re.S | re.I)
        text = re.sub(r"<[^>]+>", " ", text)
        return re.sub(r"\s+", " ", text).strip()[:max(0, int(n))]
    raise ValueError("link redirected too many times")


def gen_identity(desc, link):
    """desc/link 至少一个非空 -> {name,name_zh,desc} 或 {error}"""
    extra = ""
    if link and not desc:
        try:
            extra = "\n链接页面内容摘录:\n" + _fetch_text(link)
        except Exception as e:
            extra = f"\n（链接抓取失败: {e}）"
    try:
        txt = atlas_model.complete_text(
            [{"role": "user", "content": ID_PROMPT.format(
                desc=desc or "（无）", link=link or "（无）", extra=extra)}],
            role="identity", temperature=0.3, max_tokens=3000)
        m = re.search(r"\{.*\}", txt, re.S)
        out = json.loads(m.group(0)) if m else {}
        name = str(out.get("name", "")).strip()
        name_zh = str(out.get("name_zh", "")).strip()
        d = str(out.get("desc", "")).strip()
        if not name or not d:
            return {"error": f"模型未能生成有效身份: {txt[:200]}"}
        return {"name": name, "name_zh": name_zh, "desc": d}
    except Exception as e:
        return {"error": f"身份生成失败: {e}"}


def draft_path(slug):
    return os.path.join(DRAFTS, valid_slug(slug) + ".md")


def list_drafts():
    out = []
    rv_all = load_review(PACK)
    for f in sorted(os.listdir(DRAFTS)):
        if not f.endswith(".md") or f.endswith(".research.md") or \
                f.endswith(".body.md") or f.endswith(".zh.md"):
            continue
        p = os.path.join(DRAFTS, f)
        front, body = parse_front(Path(p).read_text(encoding="utf-8"))
        r = lint(p)
        rv = rv_all.get(front.get("slug", f[:-3]), {})
        status, conflict = _publication_state(front.get("slug", f[:-3]), front, rv)
        out.append({"slug": front.get("slug", f[:-3]), "name": front.get("name", ""),
                    "name_zh": front.get("name_zh", ""), "status": status,
                    "status_conflict": conflict,
                    "created": front.get("created", ""), "engine": front.get("engine", ""),
                    "size": r["size"], "lint_ok": r["ok"], "lint_errors": len(r["errors"]),
                    "dup": _dup_info(rv_all.get(front.get("slug", f[:-3]), {}))})
    return out


def recover_interrupted_drafts():
    """Fail closed after a restart; never replay generation or translation."""
    recovered = {"generating": 0, "translations": 0}
    for name in sorted(os.listdir(DRAFTS)):
        if not name.endswith(".md") or name.endswith((".research.md", ".body.md", ".zh.md")):
            continue
        path = os.path.join(DRAFTS, name)
        try:
            front, _ = parse_front(Path(path).read_text(encoding="utf-8"))
            review = load_review(PACK).get(front.get("slug", name[:-3]), {})
            if front.get("status") == "generating" and not _publication_state(
                    front.get("slug", name[:-3]), front, review)[1]:
                dn.refresh_front(
                    front.get("slug", name[:-3]), "failed",
                    extra="generation_interrupted: 服务重启后未自动重放，请显式重新生成",
                )
                update_review(front.get("slug", name[:-3]), {
                    "generation_state": "interrupted",
                    "generation_error": "服务重启中断，未自动重放",
                }, PACK)
                recovered["generating"] += 1
        except (OSError, ValueError, json.JSONDecodeError):
            continue
    for slug, record in load_review(PACK).items():
        if record.get("translation_state") == "running":
            update_review(slug, {
                "translation_state": "failed",
                "translation_error": "服务重启中断，未自动重放",
            }, PACK)
            recovered["translations"] += 1
    return recovered


def _publication_state(slug, front, review):
    promoted = bool(review.get("promoted"))
    final_slug = review.get("final_slug")
    try:
        valid_slug(final_slug)
    except (TypeError, ValueError):
        final_slug = None
    canonical_exists = bool(
        final_slug and os.path.exists(os.path.join(PACK, "applications", f"{final_slug}.md"))
    )
    conflict = promoted and (
        front.get("status") != "promoted" or not final_slug or not canonical_exists
    )
    return ("status_conflict" if conflict else front.get("status", "?"), conflict)


def _dup_info(rv):
    ident = rv.get("identity") or {}
    if ident.get("verdict") in ("same", "variant"):
        return {"verdict": ident["verdict"], "best": ident.get("best")}
    return None


def draft_progress(slug):
    """Live generation signals from files the engine writes as it works."""
    out = {"body_chars": 0, "research_chars": 0, "last_h2": "", "sections_done": 0,
           "log_tail": [], "updated_at": 0}
    bp = os.path.join(DRAFTS, slug + ".body.md")
    rp = os.path.join(DRAFTS, slug + ".research.md")
    lp = os.path.join(DRAFTS, slug + ".opencode.log")
    if os.path.exists(rp):
        out["research_chars"] = os.path.getsize(rp)
    if os.path.exists(bp):
        out["body_chars"] = os.path.getsize(bp)
        out["updated_at"] = int(os.path.getmtime(bp))
        hs = re.findall(r"^## (.+)$", Path(bp).read_text(encoding="utf-8", errors="ignore"), re.M)
        out["sections_done"] = len(hs)
        if hs:
            out["last_h2"] = hs[-1].strip()
    if os.path.exists(lp):
        raw = re.sub(r"\x1b\[[0-9;]*m", "", Path(lp).read_bytes()[-3000:].decode("utf-8", "ignore"))
        out["log_tail"] = [
            line.strip() for line in raw.splitlines() if line.strip()][-6:]
    return out


def read_draft(slug):
    p = draft_path(slug)
    if not os.path.exists(p):
        return None
    text = Path(p).read_text(encoding="utf-8")
    front, body = parse_front(text)
    rp = os.path.join(DRAFTS, slug + ".research.md")
    research = Path(rp).read_text(encoding="utf-8") if os.path.exists(rp) else None
    rzp = os.path.join(DRAFTS, slug + ".research.zh.md")
    research_zh = Path(rzp).read_text(encoding="utf-8") if os.path.exists(rzp) else None
    zh = None
    zp = os.path.join(DRAFTS, slug + ".zh.json")
    if os.path.exists(zp):
        try:
            zh = json.loads(Path(zp).read_text(encoding="utf-8"))
        except Exception:
            zh = None
    rv = load_review(PACK).get(slug, {})
    status, status_conflict = _publication_state(slug, front, rv)
    ident = rv.get("identity") or {}
    if ident.get("verdict") in ("same", "variant") and not rv.get("verdict"):
        rv = {**rv, "verdict": ident["verdict"], "best": ident.get("best"),
              "reason": ident.get("reason")}
    top = rv.get("top") or rv.get("collision") or []
    return {"slug": slug, "front": front, "status": status,
            "status_conflict": status_conflict, "body": body,
            "body_sha256": _body_sha256(body), "research": research,
            "research_zh": research_zh, "zh": zh,
            "lint": lint(p), "collision": top or [],
            "review": {**rv, "current": review_current(slug, rv, PACK)}, "progress": draft_progress(slug)}


def list_sections():
    import sqlite3
    con = sqlite3.connect(os.path.join(PACK, "atlas", "atlas.sqlite"))
    rows = con.execute(
        "SELECT id, name, name_zh FROM section WHERE parent != '' ORDER BY id").fetchall()
    con.close()
    return [{"id": r[0], "name": r[1], "name_zh": r[2]} for r in rows]


ZH_SRC = [("overview", ("overview",)), ("how", ("how it works",)),
          ("rules", ("important rules", "rules")), ("variants", ("variants",)),
          ("products", ("representative products", "products"))]
ZH_TRUNC = {"overview": 4000, "how": 2500, "rules": 1800, "variants": 2500, "products": 1800}


RESEARCH_PROMPT = """把下面的软件类型「边界发现/不确定性」调研文档翻译成中文。
要求:
- 保留 Markdown 结构（## / ### 标题、列表、粗体、表格）
- 类型名、产品名、leaf slug 保留英文；证据等级标记（A/B/C）原样保留
- 只输出译文正文，不要任何解释

{research}"""


def translate_research(slug, expected_body_sha256=None):
    rp = os.path.join(DRAFTS, slug + ".research.md")
    if not os.path.exists(rp):
        return False
    if expected_body_sha256 is not None:
        _require_body_revision(slug, expected_body_sha256)
    research = open(rp, encoding="utf-8").read()
    txt = atlas_model.complete_text(
        [{"role": "user",
          "content": RESEARCH_PROMPT.format(research=research)}],
        role="translate", temperature=0.1, max_tokens=8000,
        timeout=600, strip_fence=True)
    if not txt:
        raise RuntimeError("empty translation")
    if expected_body_sha256 is not None:
        _require_body_revision(slug, expected_body_sha256)
    if not os.path.exists(draft_path(slug)):
        raise FileNotFoundError(slug)
    atomic_write(os.path.join(DRAFTS, slug + ".research.zh.md"), txt)
    return True


def translate_draft(slug, expected_body_sha256=None):
    """Generate zh preview (5 key fields) via the corpus translation pipeline."""
    front, body = parse_front(open(draft_path(slug), encoding="utf-8").read())
    if expected_body_sha256 is not None and _body_sha256(body) != expected_body_sha256:
        raise DraftRevisionConflict("草稿正文已变化，翻译已取消")
    import re as _re
    parts = _re.split(r"^##\s+(.+)$", body, flags=_re.M)
    sections = {parts[i].strip().lower(): parts[i + 1]
                for i in range(1, len(parts) - 1, 2)}

    def grab(*names):
        for n in names:
            for k, v in sections.items():
                if k.startswith(n):
                    return v
        return ""

    from translate_bodies import call_api, PROMPT, parse_out
    fields = {k: grab(*names).strip() for k, names in ZH_SRC}
    payload = json.dumps({k: fields[k][:ZH_TRUNC[k]] for k in fields}, ensure_ascii=False)
    zh = parse_out(call_api(PROMPT.format(json=payload)))
    zh["slug"] = slug
    zh["engine"] = "api"
    try:
        zh["research_zh"] = bool(translate_research(slug, expected_body_sha256))
    except Exception as e:
        zh["research_zh"] = False
        zh["research_zh_error"] = redact_text(str(e))[:300]
    if expected_body_sha256 is not None:
        _require_body_revision(slug, expected_body_sha256)
    if not os.path.exists(draft_path(slug)):
        raise FileNotFoundError(slug)
    atomic_write(
        os.path.join(DRAFTS, slug + ".zh.json"),
        json.dumps(zh, ensure_ascii=False, indent=1),
    )
    return zh


def _translation_failure(slug, error):
    update_review(slug, {
        "translation_state": "failed",
        "translation_error": redact_text(str(error))[:500],
        "translation_finished_at": datetime.datetime.now().isoformat(),
    }, PACK)


def run_translation(slug, expected_body_sha256):
    try:
        translate_draft(slug, expected_body_sha256)
        update_review(slug, {
            "translation_state": "completed",
            "translation_body_sha256": expected_body_sha256,
            "translation_finished_at": datetime.datetime.now().isoformat(),
            "translation_error": None,
        }, PACK)
    except Exception as error:
        _translation_failure(slug, error)
    finally:
        with TRANSLATION_LOCK:
            TRANSLATION_THREADS.pop(slug, None)


def start_regeneration(slug, expected_body_sha256):
    with dn.slug_lock(slug, DRAFTS):
        _require_body_revision(slug, expected_body_sha256)
        p = draft_path(slug)
        if not os.path.exists(p):
            raise FileNotFoundError(slug)
        front, _ = parse_front(Path(p).read_text(encoding="utf-8"))
        review = load_review(PACK).get(slug, {})
        if _publication_state(slug, front, review)[1]:
            raise ValueError("草稿状态冲突，请先修复状态")
        if front.get("status") != "failed":
            raise ValueError("只有失败草稿可以重新生成")
        with GEN_THREADS_LOCK:
            if slug in GEN_THREADS:
                return False
            for suffix in (".body.md", ".identity.json"):
                sidecar = os.path.join(DRAFTS, slug + suffix)
                if os.path.exists(sidecar):
                    os.remove(sidecar)
            dn.refresh_front(slug, "generating", extra="generation_restarted: user requested")
            thread = threading.Thread(target=run_engine, args=(slug,), daemon=True)
            GEN_THREADS[slug] = thread
        try:
            thread.start()
        except Exception as error:
            with GEN_THREADS_LOCK:
                GEN_THREADS.pop(slug, None)
            dn.refresh_front(slug, "failed", extra="generation_error: could not start")
            update_review(slug, {
                "generation_state": "failed",
                "generation_error": redact_text(str(error))[:500],
            }, PACK)
            raise
        return True


def start_translation(slug, expected_body_sha256):
    with TRANSLATION_LOCK:
        if slug in TRANSLATION_THREADS:
            return False
        thread = threading.Thread(
            target=run_translation, args=(slug, expected_body_sha256), daemon=True)
        TRANSLATION_THREADS[slug] = thread
    try:
        update_review(slug, {
            "translation_state": "running",
            "translation_body_sha256": expected_body_sha256,
            "translation_started_at": datetime.datetime.now().isoformat(),
            "translation_error": None,
        }, PACK)
        thread.start()
    except Exception as error:
        with TRANSLATION_LOCK:
            TRANSLATION_THREADS.pop(slug, None)
        _translation_failure(slug, error)
        raise
    return True


def run_promote(slug, action, kw):
    try:
        import promote_draft as pd
        pd.promote(
            slug, action, kw["section"] if action == "new" else kw["into"],
            expected_body_sha256=kw.get("body_sha256"),
        )
    except Exception as error:
        update_review(slug, {"promote_error": str(error)}, PACK)
        if os.path.exists(draft_path(slug)):
            dn.refresh_front(slug, "draft")
    finally:
        PROMOTE_THREADS.discard(slug)
        PROMOTE_LOCK.release()


def dedupe_draft(slug, expected_body_sha256):
    with dn.slug_lock(slug, DRAFTS):
        _require_body_revision(slug, expected_body_sha256)
        p = draft_path(slug)
        if not os.path.exists(p):
            raise FileNotFoundError(slug)
        front, _ = parse_front(Path(p).read_text(encoding="utf-8"))
        review = load_review(PACK).get(slug, {})
        if _publication_state(slug, front, review)[1]:
            raise ValueError("草稿状态冲突，请先修复状态")
        if not (front.get("desc") or "").strip():
            raise ValueError("主张（desc）为空：等引擎调研定名后再查重")
        if front.get("status") in ("promoting", "generating"):
            raise ValueError("等待当前任务结束后再查重")
        before = fingerprint(slug, PACK)
        revision = corpus_revision(PACK)
        top = dn.collision(front["desc"])
        try:
            from dedupe_judge import judge
            verdict = judge(slug)
        except Exception as error:
            verdict = {"verdict": "error", "reason": str(error)}
        _require_body_revision(slug, expected_body_sha256)
        if before != fingerprint(slug, PACK) or revision != corpus_revision(PACK):
            raise DraftRevisionConflict("查重期间草稿或语料已更新，请重试")
        import datetime
        update_review(slug, {
            "deduped_at": datetime.datetime.now().isoformat(),
            "top": top, **verdict, "draft_fingerprint": before,
            "corpus_revision": revision, "body_sha256": expected_body_sha256,
        }, PACK)
        return {"slug": slug, "top": top, "verdict": verdict,
                "body_sha256": expected_body_sha256}


def _invalidate_translation(slug):
    removed = False
    for suffix in (".zh.json", ".research.zh.md"):
        path = os.path.join(DRAFTS, slug + suffix)
        if os.path.exists(path):
            os.remove(path)
            removed = True
    record = load_review(PACK).get(slug, {})
    if removed or record.get("translation_state") in {"running", "completed", "failed"}:
        update_review(slug, {
            "translation_state": "stale",
            "translation_error": "正文已修改，请重新生成中文对照",
            "translation_body_sha256": None,
        }, PACK)


def save_body(slug, body, expected_body_sha256=None):
    p = draft_path(slug)
    if not os.path.exists(p):
        return False
    with dn.slug_lock(slug, DRAFTS):
        text = Path(p).read_text(encoding="utf-8")
        if expected_body_sha256 is not None:
            _, current_body = parse_front(text)
            if _body_sha256(current_body) != expected_body_sha256:
                raise DraftRevisionConflict("草稿正文已变化，请重新加载后再保存")
        m = re.match(r"\A---\n.*?\n---\n", text, re.S)
        atomic_write(p, (m.group(0) if m else "") + body)
        _invalidate_translation(slug)
        return _body_sha256(body)


def delete_draft(slug):
    with dn.slug_lock(slug, DRAFTS):
        path = draft_path(slug)
        draft_existed = os.path.exists(path)
        if draft_existed:
            front, _ = parse_front(Path(path).read_text(encoding="utf-8"))
            review = load_review(PACK).get(slug, {})
            if _publication_state(slug, front, review)[1]:
                raise ValueError("草稿状态冲突，请先修复状态")
            if front.get("status") in ("promoting", "generating"):
                raise ValueError("任务执行期间不能删除草稿")
        removed = []
        for suffix in (".md", ".research.md", ".zh.json", ".opencode.log",
                       ".identity.json", ".research.zh.md", ".body.md"):
            p = os.path.join(DRAFTS, slug + suffix)
            if os.path.exists(p):
                os.remove(p)
                removed.append(slug + suffix)
        if draft_existed and remove_review(slug, PACK):
            removed.append("review.json:" + slug)
        return {"removed": removed}


def apply_identity(slug):
    """引擎完成后：读 identity.json 定名/裁决。返回非 None 表示查重失败，勿再翻译。"""
    ip = os.path.join(DRAFTS, slug + ".identity.json")
    ident = {}
    if os.path.exists(ip):
        try:
            ident = json.load(open(ip, encoding="utf-8"))
        except Exception:
            ident = {}
    if ident.get("verdict") in ("same", "variant"):
        update_review(slug, {"identity": ident}, PACK)
        dn.refresh_front(slug, "failed",
                         extra=f"dedupe: 引擎调研判定 {ident.get('verdict')} / {ident.get('best')}: "
                               f"{ident.get('reason', '')[:120]}")
        if os.path.exists(ip):
            os.remove(ip)
        return ident
    front, _ = parse_front(open(draft_path(slug), encoding="utf-8").read())
    text = open(draft_path(slug), encoding="utf-8").read()
    desc = str(ident.get("desc") or "").strip() or (front.get("desc") or "").strip()
    if front.get("name_source") == "pending":
        name = str(ident.get("name", "")).strip()
        name_zh = str(ident.get("name_zh", "")).strip()
        if not name:
            gen = gen_identity(desc, front.get("link", ""))
            if "error" not in gen:
                name, name_zh = gen["name"], gen["name_zh"]
                desc = desc or gen["desc"]
        if name and not name_zh:
            gen = gen_identity(desc, front.get("link", ""))
            if "error" not in gen and gen.get("name_zh"):
                name_zh = gen["name_zh"]
        if name:
            text = re.sub(r"^name: .*$", f"name: {name}", text, count=1, flags=re.M)
            text = re.sub(r"^name_zh: .*$", f"name_zh: {name_zh}", text, count=1, flags=re.M)
            text = re.sub(r"^name_source: .*$", "name_source: model", text, count=1, flags=re.M)
    if desc and desc != front.get("desc"):
        text = re.sub(r"^desc: .*$", f"desc: {desc}", text, count=1, flags=re.M)
    m = re.search(r"^name: (.*)$", text, re.M)
    if m and m.group(1).strip():
        text = re.sub(r"^# .*$", f"# {m.group(1).strip()}", text, count=1, flags=re.M)
    open(draft_path(slug), "w", encoding="utf-8").write(text)
    top = dn.collision(desc) if desc else []
    update_review(slug, {"identity": ident or None, "collision": top}, PACK)
    if os.path.exists(ip):
        os.remove(ip)
    return None


def run_engine(slug):
    """Background: engine writes body, lint gates it, status flips."""
    try:
        _run_engine(slug)
    except Exception as error:
        with open(os.path.join(DRAFTS, slug + ".opencode.log"), "ab") as log:
            log.write(f"\n[api] engine fatal: {redact_text(str(error))[:500]}\n".encode())
        if os.path.exists(draft_path(slug)):
            dn.refresh_front(slug, "failed", extra="generation_error: engine failed")
        update_review(slug, {
            "generation_state": "failed",
            "generation_error": redact_text(str(error))[:500],
        }, PACK)
    finally:
        with GEN_THREADS_LOCK:
            GEN_THREADS.pop(slug, None)


def _run_engine(slug):
    front, _ = parse_front(open(draft_path(slug), encoding="utf-8").read())
    idea = {"slug": slug, "name": front.get("name", slug), "name_zh": front.get("name_zh", ""),
            "desc": front.get("desc", ""), "link": front.get("link", "")}
    if idea["link"]:
        try:
            idea["link_excerpt"] = _fetch_text(idea["link"], 6000)
        except (OSError, ValueError):
            idea["link_excerpt"] = ""
    from drafts_engines import get_engine
    cfg = json.load(open(dn.ENGINES_CFG)) if os.path.exists(dn.ENGINES_CFG) else {}
    eng, _ = get_engine(front.get("engine") or cfg.get("engine"))
    model = front.get("model") or cfg.get("model")
    log_path = os.path.join(DRAFTS, slug + ".opencode.log")
    try:
        with GEN_LOCK:
            ok = eng.generate(idea, PROMPT, WORKDIR, log_path, model=model)
    except Exception as e:
        ok = False
        with open(log_path, "ab") as log:
            log.write(f"\n[api] engine exception: {redact_text(str(e))[:500]}\n".encode())
    if ok and dn.assemble(slug):
        if apply_identity(slug):
            return
        r = lint(draft_path(slug))
        extra = f"lint_errors: {len(r['errors'])}\nlint_warnings: {len(r['warnings'])}"
        dn.refresh_front(slug, "draft" if r["ok"] else "failed", extra=extra)
        if r["ok"]:
            try:
                _, generated_body = parse_front(Path(draft_path(slug)).read_text(encoding="utf-8"))
                start_translation(slug, _body_sha256(generated_body))
            except Exception as e:
                with open(os.path.join(DRAFTS, slug + ".opencode.log"), "ab") as log:
                    log.write(f"\n[api] zh translate scheduling failed: {redact_text(str(e))[:500]}\n".encode())
    else:
        if os.path.exists(os.path.join(DRAFTS, slug + ".identity.json")) and apply_identity(slug):
            return
        dn.refresh_front(slug, "failed", extra="lint: engine failed, see .opencode.log")


MAX_REQUEST_BODY_BYTES = 2 * 1024 * 1024
MUTATING_METHODS = {"POST", "PUT", "PATCH", "DELETE"}


class RequestBoundaryError(ValueError):
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code


def _local_http_authority(value: str) -> bool:
    try:
        parsed = urlparse(f"//{value}")
        port = parsed.port
    except (TypeError, ValueError):
        return False
    hostname = (parsed.hostname or "").lower().rstrip(".")
    return (
        parsed.scheme == "" and not parsed.username and parsed.password is None
        and not parsed.path and not parsed.query and not parsed.fragment
        and hostname in {"localhost", "127.0.0.1", "::1"}
        and (port is None or 1 <= port <= 65535)
    )


def _local_http_origin(value: str) -> bool:
    try:
        parsed = urlparse(value)
        parsed.port
    except (TypeError, ValueError):
        return False
    return (
        parsed.scheme in {"http", "https"}
        and parsed.username is None and parsed.password is None
        and parsed.path in {"", "/"} and not parsed.query and not parsed.fragment
        and _local_http_authority(parsed.netloc)
    )


def _api_error(error: BaseException, code: str | None = None,
               retryable: bool | None = None) -> dict:
    message = redact_text(str(error))[:800]
    if code is None:
        lowered = message.lower()
        if isinstance(error, ProjectBackupError):
            if "active" in lowered:
                code = "conflict"
            elif "already exists" in lowered or "invalid" in lowered or "confirm" in lowered:
                code = "invalid_backup"
            elif "not found" in lowered or "does not exist" in lowered:
                code = "not_found"
            else:
                code = "backup_error"
        elif isinstance(error, ProjectStoreError):
            code = "conflict" if "conflict" in lowered or "changed" in lowered else "not_found"
        elif isinstance(error, (TimeoutError, OSError)):
            code = "service_unavailable"
        else:
            code = "invalid_request"
    if retryable is None:
        retryable = code in {"service_unavailable", "provider_unavailable"}
    return {"error": message, "code": code, "retryable": bool(retryable), "details": {}}


def _ask_error(error: BaseException) -> dict:
    if isinstance(error, atlas_ask.AskError):
        return {"error": str(error), "code": error.code,
                "retryable": error.code in {"busy", "provider_error"},
                "details": {}}
    return _api_error(error, "service_unavailable", True)


def _model_error(error: BaseException) -> tuple[dict, int]:
    """Map a model-config failure to a safe payload and status code."""
    if isinstance(error, atlas_model.ModelConfigError):
        body = {"error": str(error), "code": error.code,
                "retryable": error.code in {"rate_limited", "timeout",
                                            "unreachable", "provider_error"},
                "details": {}}
        return body, error.status
    return _api_error(error, "invalid_request"), 400


def _public_backup_result(result: dict, project_id: str) -> dict:
    archive_name = Path(result["archive"]).name
    manifest = dict(result.get("manifest") or {})
    manifest.pop("source_workspace", None)
    return {
        "project_id": project_id,
        "archive_name": archive_name,
        "archive_sha256": result.get("archive_sha256", ""),
        "manifest": manifest,
    }


class Handler(BaseHTTPRequestHandler):
    def _factory(self, method, parsed):
        try:
            result = factory_api.dispatch(method, unquote(parsed.path), parsed.query,
                                          self._body() if method == "POST" else None)
            if len(result) == 3:
                if result[2] == "image/png":
                    content = result[0].read_bytes()
                    self.send_response(200)
                    self.send_header("Content-Type", "image/png")
                    self.send_header("Content-Length", str(len(content)))
                    self.send_header("X-Content-Type-Options", "nosniff")
                    self.send_header("Cache-Control", "no-store")
                    self.end_headers()
                    self.wfile.write(content)
                    return
                return self._file(result[0], result[1])
            return self._json(result[0], result[1])
        except FactoryError as error:
            return self._json({"error": str(error), "code": error.code}, error.status)
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        except (ValueError, OSError) as error:
            return self._json(_api_error(error, "factory_unavailable", True), 503)

    def log_message(self, fmt, *args):
        print("[api]", fmt % args)

    def _json(self, obj, code=200):
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            return

    def _file(self, path: Path, download_name: str):
        path = path.resolve()
        if not path.is_file():
            return self._json({"error": "backup archive not found"}, 404)
        self.send_response(200)
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Length", str(path.stat().st_size))
        self.send_header("Content-Disposition", f'attachment; filename="{download_name}"')
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        with path.open("rb") as stream:
            shutil.copyfileobj(stream, self.wfile)

    def _content_length(self) -> int:
        headers = getattr(self, "headers", None)
        if headers is None:
            return 0
        if headers.get("Transfer-Encoding"):
            raise RequestBoundaryError("transfer encoding is not supported", 400)
        value = headers.get("Content-Length")
        if value in {None, ""}:
            return 0
        try:
            length = int(value)
        except ValueError as exc:
            raise RequestBoundaryError("invalid Content-Length", 400) from exc
        if length < 0:
            raise RequestBoundaryError("invalid Content-Length", 400)
        if length > MAX_REQUEST_BODY_BYTES:
            raise RequestBoundaryError("request body is too large", 413)
        return length

    def _guard_request(self, method: str):
        headers = getattr(self, "headers", None)
        if headers is None:
            return
        if not _local_http_authority(headers.get("Host", "")):
            raise RequestBoundaryError("request host is not local", 403)
        origin = headers.get("Origin")
        if origin and not _local_http_origin(origin):
            raise RequestBoundaryError("request origin is not local", 403)
        fetch_site = headers.get("Sec-Fetch-Site")
        if fetch_site and fetch_site not in {"same-origin", "same-site", "none"}:
            raise RequestBoundaryError("cross-site requests are not allowed", 403)
        if method in MUTATING_METHODS:
            content_type = (headers.get("Content-Type") or "").split(";", 1)[0].strip().lower()
            if content_type != "application/json":
                raise RequestBoundaryError("write requests require application/json", 415)
            self._content_length()

    def _boundary_error(self, error: RequestBoundaryError):
        return self._json({"error": str(error)}, error.status_code)

    def _ask_post(self, path: str):
        """Conversation creation and question submission."""
        try:
            if path == "/api/ask/threads":
                body = self._body()
                return self._json(atlas_ask.create_thread(
                    str(body.get("title") or "")), 201)
            m = re.match(
                r"^/api/ask/threads/(ask_[0-9a-f]{32})/messages$", path)
            if m:
                body = self._body()
                result = atlas_ask.start_question(m.group(1), body.get("content"))
                return self._json(result, 202)
            return self._json({"error": "no route"}, 404)
        except atlas_ask.AskError as error:
            return self._json(_ask_error(error), error.status)
        except (ValueError, json.JSONDecodeError) as error:
            return self._json(_api_error(error, "invalid_request"), 400)
        except Exception as error:
            return self._json(_api_error(error, "service_unavailable", True), 500)

    def _settings_model_post(self, path: str):
        """All model-provider settings writes. Credentials are write-only."""
        try:
            if path == "/api/settings/model/providers":
                return self._json(atlas_model.upsert_provider(self._body()), 201)
            if path == "/api/settings/model/default":
                body = self._body()
                return self._json(atlas_model.set_default(
                    body.get("provider"), body.get("model")))
            if path == "/api/settings/model/embedding":
                return self._json(atlas_model.set_embedding(self._body()))
            if path == "/api/settings/model/import":
                return self._json(atlas_model.import_from_opencode())
            m = re.match(
                r"^/api/settings/model/providers/([a-z0-9-]+)/test$", path)
            if m:
                return self._json(atlas_model.test_provider(m.group(1)))
            return self._json({"error": "no route"}, 404)
        except atlas_model.ModelConfigError as error:
            body, status = _model_error(error)
            return self._json(body, status)
        except (ValueError, json.JSONDecodeError) as error:
            return self._json(_api_error(error, "invalid_request"), 400)
        except Exception as error:
            return self._json(_api_error(error, "service_unavailable", True), 500)

    def _body(self):
        length = self._content_length()
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        if len(raw) != length:
            raise RequestBoundaryError("request body ended unexpectedly", 400)
        try:
            value = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError("request body must be valid JSON") from exc
        if not isinstance(value, dict):
            raise ValueError("request body must be an object")
        return value

    def do_GET(self):
        try:
            self._guard_request("GET")
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        if path.startswith("/api/factory/"):
            return self._factory("GET", parsed)
        if path == "/api/health":
            recovery = PROJECT_RECOVERY_REPORT or {"status": "not_initialized"}
            return self._json({
                "ok": True,
                "generating": sorted(GEN_THREADS),
                "promoting": sorted(PROMOTE_THREADS),
                "recovery": {
                    "status": recovery.get("status"),
                    "executions_interrupted": len(recovery.get("executions_interrupted", [])),
                    "generations_interrupted": len(recovery.get("generations_interrupted", [])),
                    "applications_requiring_review": len(
                        recovery.get("applications_requiring_review", [])),
                    "errors": len(recovery.get("errors", [])),
                },
            })
        if path == "/api/settings/model":
            try:
                return self._json(atlas_model.public_view())
            except Exception as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        if path == "/api/ask/threads":
            try:
                return self._json(atlas_ask.list_threads())
            except Exception as error:
                return self._json(_ask_error(error), 500)
        m = re.match(r"^/api/ask/threads/(ask_[0-9a-f]{32})$", path)
        if m:
            try:
                return self._json(atlas_ask.read_thread(m.group(1)))
            except atlas_ask.AskError as error:
                return self._json({"error": str(error), "code": error.code,
                                   "retryable": False, "details": {}},
                                  error.status)
        m = re.match(r"^/api/settings/model/providers/([a-z0-9-]+)/models$", path)
        if m:
            try:
                return self._json({"id": m.group(1),
                                   "models": atlas_model.list_models(m.group(1))})
            except atlas_model.ModelConfigError as error:
                return self._json({"error": str(error), "code": error.code},
                                  error.status)
            except Exception as error:
                return self._json(_api_error(error, "provider_error", True), 502)
        if path == "/api/ready":
            recovery = PROJECT_RECOVERY_REPORT
            ready = bool(recovery and recovery.get("status") == "completed")
            try:
                projects = len(get_project_store().list_projects())
            except Exception as error:
                return self._json({
                    "ready": False,
                    "error": redact_text(str(error)),
                }, 503)
            return self._json({
                "ready": ready,
                "projects": projects,
                "recovery_status": (recovery or {}).get("status", "not_initialized"),
            }, 200 if ready else 503)
        if path == "/api/drafts":
            return self._json(list_drafts())
        if path == "/api/sections":
            return self._json(list_sections())
        if path == "/api/review":
            return self._json(load_review(PACK))
        if path == "/api/projects":
            return self._json(get_project_store().list_projects())
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/workspace$", path)
        if m:
            try:
                store = get_project_store()
                payload = project_workspace(store, m.group(1))
                payload["open_items"] = list_open_items(store, m.group(1))
                return self._json(payload)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/generation-runs$", path)
        if m:
            try:
                return self._json(project_generation_list(get_project_store(), m.group(1)))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/workspace-baselines$", path)
        if m:
            try:
                return self._json(list_project_baselines(get_project_store(), m.group(1)))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/workspace-baselines/(snap_[A-Za-z0-9]+)$",
            path)
        if m:
            try:
                return self._json(get_project_baseline(
                    get_project_store(), m.group(1), m.group(2)))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/generation-runs/(gen_[A-Za-z0-9]+)$",
            path)
        if m:
            try:
                return self._json(project_generation_status(
                    get_project_store(), m.group(1), m.group(2)))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/executions/(exe_[A-Za-z0-9]+)$",
            path)
        if m:
            try:
                store = get_project_store()
                execution = store.get_execution(m.group(2))
                task = store.get_task(execution["task_id"])
                if task["project_id"] != m.group(1):
                    raise ProjectStoreError("execution does not belong to project")
                return self._json(execution)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/references$", path)
        if m:
            try:
                return self._json(list_project_references(m.group(1)))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/documents/(doc_[A-Za-z0-9]+)/versions$",
            path)
        if m:
            try:
                return self._json(document_versions(
                    get_project_store(), m.group(1), m.group(2)))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/documents/(doc_[A-Za-z0-9]+)/diff$",
            path)
        if m:
            query = parse_qs(parsed.query)
            try:
                before = int(query["from"][0]) if query.get("from") else None
                after = int(query["to"][0]) if query.get("to") else None
                return self._json(document_diff(
                    get_project_store(), m.group(1), m.group(2), before, after))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except ValueError as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/harness/preflight$", path)
        if m:
            try:
                project = get_project_store().get_project(m.group(1))
                config = Path(project["workspace"]) / ".atlas" / "harness.json"
                if not config.exists():
                    return self._json({"status": "not_configured", "configPath": str(config)})
                return self._json(opencode_preflight(project["workspace"]))
            except ProjectStoreError as error:
                return self._json({"status": "failed", "code": "project_unavailable", "message": str(error)}, 404)
            except HarnessCompatibilityError as error:
                return self._json({"status": "failed", "code": error.code, "message": str(error), "details": error.details})
            except (ValueError, OSError) as error:
                return self._json({"status": "failed", "code": "preflight_error", "message": str(error)})
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/backups$", path)
        if m:
            try:
                return self._json({
                    "project_id": m.group(1),
                    "backups": list_project_backups(get_project_store(), m.group(1)),
                })
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/backups/(\d{8}T\d{6}Z-[0-9a-f]{8}\.zip)$",
            path)
        if m:
            try:
                store = get_project_store()
                archive = backup_archive_path(store, m.group(1), m.group(2))
                return self._file(archive, m.group(2))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/restore-status/(restore_[0-9a-f]{32})$",
            path)
        if m:
            try:
                return self._json(inspect_prepared_project_restore(
                    get_project_store(), m.group(1), m.group(2)))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/acceptance-migration$", path)
        if m:
            try:
                return self._json(get_project_store().legacy_acceptance_migration(m.group(1)))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)$", path)
        if m:
            try:
                return self._json(get_project_store().get_project(m.group(1)))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(r"^/api/sources/([\w-]+)$", path)
        if m:
            try:
                return self._json(source_manifest(m.group(1), PACK))
            except SourceError as error:
                return self._json({"error": str(error)}, 400)
            except FileNotFoundError:
                return self._json({"slug": m.group(1), "sources": []})
        m = re.match(r"^/api/sources/(application|research)/([\w-]+)$", path)
        if m:
            query = parse_qs(parsed.query)
            try:
                return self._json(read_source(
                    m.group(2), m.group(1),
                    section=(query.get("section") or [None])[0],
                    offset=int((query.get("offset") or [0])[0]),
                    limit=int((query.get("limit") or [12000])[0]),
                    pack=PACK,
                ))
            except (SourceError, ValueError) as error:
                return self._json({"error": str(error)}, 400)
            except FileNotFoundError:
                return self._json({"error": "not found"}, 404)
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            d = read_draft(m.group(1))
            return self._json(d) if d else self._json({"error": "not found"}, 404)
        self._json({"error": "no route"}, 404)

    def do_POST(self):
        try:
            self._guard_request("POST")
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        path = unquote(urlparse(self.path).path)
        if path.startswith("/api/factory/"):
            return self._factory("POST", urlparse(self.path))
        if path.startswith("/api/settings/model"):
            return self._settings_model_post(path)
        if path.startswith("/api/ask/"):
            return self._ask_post(path)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/acceptance-migration/backfill$", path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or set(body) != {"confirm"} \
                        or body.get("confirm") != "backfill_legacy_acceptance_metadata":
                    raise ValueError("explicit legacy acceptance backfill confirmation is required")
                return self._json(get_project_store().backfill_legacy_acceptance(
                    m.group(1), body["confirm"]))
            except ProjectStoreError as error:
                return self._json(_api_error(error, "conflict"), 409)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/iterations$", path)
        if m:
            try:
                return self._json(create_project_iteration(
                    get_project_store(), m.group(1), self._body()), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/iterations/(itr_[A-Za-z0-9]+)/status$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or set(body) != {"status"}:
                    raise ValueError("status is required")
                iteration = get_project_store().get_iteration(m.group(2))
                if iteration["project_id"] != m.group(1):
                    raise ProjectStoreError("iteration does not belong to project")
                return self._json(get_project_store().update_iteration_status(
                    m.group(2), body["status"]))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/iterations/(itr_[A-Za-z0-9]+)/rebase$",
            path)
        if m:
            try:
                return self._json(rebase_project_iteration(
                    get_project_store(), m.group(1), m.group(2), self._body()))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/tasks$", path)
        if m:
            try:
                return self._json(create_execution_task(
                    get_project_store(), m.group(1), self._body()), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/tasks/(tsk_[A-Za-z0-9]+)/executions$",
            path)
        if m:
            try:
                store = get_project_store()
                project = store.get_project(m.group(1))
                config = Path(project["workspace"]) / ".atlas" / "harness.json"
                if config.exists():
                    try:
                        report = opencode_preflight(project["workspace"])
                    except HarnessCompatibilityError as error:
                        raise ProjectStoreError(f"OpenCode preflight failed ({error.code}): {error}") from error
                    if report.get("status") != "passed":
                        checks = report.get("checks") or {}
                        raise ProjectStoreError(
                            "OpenCode preflight failed: "
                            f"version={checks.get('version', {}).get('exitCode', 'n/a')}, "
                            f"providers={checks.get('providers', {}).get('exitCode', 'n/a')}")
                return self._json(start_execution(
                    store, m.group(1), m.group(2), self._body()), 202)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
            except (RuntimeError, OSError) as error:
                return self._json({"error": str(error)}, 503)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/tasks/(tsk_[A-Za-z0-9]+)/acceptance$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or not {"status", "evidence"}.issubset(body) \
                        or set(body) - {"status", "evidence", "condition_results"}:
                    raise ValueError(
                        "status and evidence are required; condition_results is optional")
                task = get_project_store().get_task(m.group(2))
                if task["project_id"] != m.group(1):
                    raise ProjectStoreError("task does not belong to project")
                return self._json(get_project_store().record_acceptance(
                    m.group(2), body["status"], body["evidence"],
                    body.get("condition_results")))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/executions/(exe_[A-Za-z0-9]+)/"
            r"(reconcile|continue|stop|apply|recover-apply|cleanup|permission|question)$", path)
        if m:
            try:
                action = m.group(3)
                if action == "reconcile":
                    body = self._body()
                    if body:
                        raise ValueError("reconcile does not accept fields")
                    result = reconcile_execution(
                        get_project_store(), m.group(1), m.group(2))
                elif action == "continue":
                    result = continue_execution(
                        get_project_store(), m.group(1), m.group(2), self._body())
                elif action == "stop":
                    body = self._body()
                    if body:
                        raise ValueError("stop does not accept fields")
                    result = stop_execution(
                        get_project_store(), m.group(1), m.group(2))
                elif action == "apply":
                    body = self._body()
                    if body:
                        raise ValueError("apply does not accept fields")
                    result = apply_execution_result(
                        get_project_store(), m.group(1), m.group(2))
                elif action == "recover-apply":
                    result = recover_interrupted_apply(
                        get_project_store(), m.group(1), m.group(2), self._body())
                elif action == "cleanup":
                    body = self._body()
                    if body:
                        raise ValueError("cleanup does not accept fields")
                    result = cleanup_execution_workspace(
                        get_project_store(), m.group(1), m.group(2))
                elif action == "permission":
                    result = reply_execution_permission(
                        get_project_store(), m.group(1), m.group(2), self._body())
                else:
                    result = reply_execution_question(
                        get_project_store(), m.group(1), m.group(2), self._body())
                return self._json(result, 202 if action == "continue" else 200)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
            except (RuntimeError, OSError) as error:
                return self._json({"error": str(error)}, 503)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/workspace-baselines$", path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict):
                    raise ValueError("request body must be an object")
                action = body.get("action")
                if action == "capture":
                    unknown = set(body) - {
                        "action", "focus_paths", "expected_baseline_id",
                        "expected_content_fingerprint",
                    }
                    if unknown:
                        raise ValueError(
                            f"unknown baseline fields: {', '.join(sorted(unknown))}")
                    return self._json(capture_project_baseline(
                        get_project_store(), m.group(1), body.get("focus_paths"),
                        body.get("expected_baseline_id"),
                        body.get("expected_content_fingerprint")), 201)
                if action == "check":
                    if set(body) != {"action"}:
                        raise ValueError("change checks do not accept additional fields")
                    return self._json(check_project_changes(
                        get_project_store(), m.group(1)))
                raise ValueError("action must be capture or check")
            except ProjectStoreError as error:
                message = str(error)
                code = 409 if any(value in message for value in (
                    "baseline changed", "workspace changed", "expected_baseline_id",
                    "expected_content_fingerprint")) else 404
                return self._json({"error": message}, code)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/generation-runs$", path)
        if m:
            try:
                return self._json(start_project_generation(
                    m.group(1), self._body()), 202)
            except ProjectStoreError as error:
                message = str(error)
                code = 409 if "workspace" in message or "baseline" in message else 404
                return self._json(_api_error(error, "conflict" if code == 409 else "not_found"), code)
            except (ValueError, json.JSONDecodeError, FileExistsError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/generation-runs/"
            r"(gen_[A-Za-z0-9]+)/apply$", path)
        if m:
            try:
                body = self._body()
                return self._json(apply_generation_item(
                    get_project_store(), m.group(1), m.group(2),
                    body.get("item_kind"), body.get("index"),
                    confirm_stale=body.get("confirm_stale", False)), 201)
            except ProjectStoreError as error:
                message = str(error)
                code = 409 if message in {
                    "generation item already applied", "document version conflict",
                    "generation run is not completed",
                } or message.startswith("document dependency must be applied first:") else 404
                return self._json(_api_error(error, "conflict" if code == 409 else "not_found"), code)
            except (ValueError, json.JSONDecodeError, AttributeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/requirements$", path)
        if m:
            try:
                return self._json(create_project_requirement(
                    get_project_store(), m.group(1), self._body()), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/requirements/(req_[A-Za-z0-9]+)/confirm$",
            path)
        if m:
            try:
                return self._json(confirm_requirement(
                    get_project_store(), m.group(1), m.group(2), self._body()))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/decisions$", path)
        if m:
            try:
                return self._json(create_decision(
                    get_project_store(), m.group(1), self._body()), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/documents$", path)
        if m:
            try:
                return self._json(create_project_document(
                    get_project_store(), m.group(1), self._body()), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/documents/(doc_[A-Za-z0-9]+)/versions$",
            path)
        if m:
            try:
                return self._json(add_document_version(
                    get_project_store(), m.group(1), m.group(2), self._body()), 201)
            except ProjectStoreError as error:
                code = 409 if str(error) == "document version conflict" else 404
                return self._json({"error": str(error)}, code)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/documents/(doc_[A-Za-z0-9]+)/review$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or not isinstance(body.get("status"), str):
                    raise ValueError("status is required")
                expected_version = body.get("expected_current_version")
                if (not isinstance(expected_version, int)
                        or isinstance(expected_version, bool) or expected_version < 1):
                    raise ValueError("expected_current_version is required")
                return self._json(get_project_store().review_document(
                    m.group(1), m.group(2), body["status"], body.get("note", ""),
                    expected_version))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/open-items/resolve$", path)
        if m:
            try:
                return self._json(resolve_open_item(
                    get_project_store(), m.group(1), self._body()))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/backup$", path)
        if m:
            try:
                body = self._body()
                if body:
                    raise ValueError("backup does not accept fields")
                result = _public_backup_result(
                    create_project_backup(get_project_store(), m.group(1)), m.group(1))
                result["download_url"] = (
                    f"/api/projects/{m.group(1)}/backups/{result['archive_name']}")
                return self._json(result, 201)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
            except OSError as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/backups/(\d{8}T\d{6}Z-[0-9a-f]{8}\.zip)/restore-target$",
            path)
        if m:
            try:
                body = self._body()
                if body:
                    raise ValueError("restore target does not accept fields")
                result = prepare_project_restore(get_project_store(), m.group(1))
                result = {key: value for key, value in result.items()
                          if key != "target_store"}
                return self._json(result, 201)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
            except OSError as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/backups/(\d{8}T\d{6}Z-[0-9a-f]{8}\.zip)/restore$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or set(body) - {"restore_id", "confirm"}:
                    raise ValueError("restore accepts only restore_id and confirm")
                if not isinstance(body.get("restore_id"), str) \
                        or not isinstance(body.get("confirm"), str):
                    raise ValueError("restore_id and confirm are required")
                if body["confirm"] != RESTORE_TARGET_CONFIRMATION:
                    raise ValueError("explicit restore confirmation is required")
                return self._json(restore_prepared_project_backup(
                    get_project_store(), m.group(1), m.group(2),
                    body["restore_id"], body["confirm"]), 201)
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
            except OSError as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/restore-status/(restore_[0-9a-f]{32})/recover$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or set(body) != {"confirm"} \
                        or body.get("confirm") != RESTORE_RECOVERY_CONFIRMATION:
                    raise ValueError("explicit restore cleanup confirmation is required")
                return self._json(recover_prepared_project_restore(
                    get_project_store(), m.group(1), m.group(2), body["confirm"]))
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
            except OSError as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/export$", path)
        if m:
            try:
                return self._json(export_bundle(get_project_store(), m.group(1)), 201)
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)/references$", path)
        if m:
            try:
                return self._json(collect_atlas_reference(m.group(1), self._body()), 201)
            except FileNotFoundError:
                return self._json({"error": "source not found"}, 404)
            except ProjectStoreError as error:
                code = 404 if str(error) == "project not found" else 409
                return self._json({"error": str(error)}, code)
            except SourceRevisionConflict as error:
                return self._json({"error": str(error)}, 409)
            except (ValueError, SourceError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        if path == "/api/projects":
            try:
                return self._json(create_project(self._body()), 201)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        if path == "/api/drafts":
            b = self._body()
            try:
                res, code = self._create(b)
            except dn.SlugLockBusy as error:
                res, code = {"error": str(error)}, 409
            return self._json(res, code)
        m = re.match(r"^/api/drafts/([\w-]+)/regenerate$", path)
        if m:
            slug = m.group(1)
            try:
                started = start_regeneration(slug, self._body().get("body_sha256"))
                return self._json({"slug": slug, "status": "generating",
                                    "started": started, "already_running": not started}, 202)
            except DraftRevisionConflict as error:
                return self._json({"error": str(error)}, 409)
            except dn.SlugLockBusy as error:
                return self._json({"error": str(error)}, 409)
            except FileNotFoundError:
                return self._json({"error": "not found"}, 404)
            except ValueError as error:
                return self._json({"error": str(error)}, 409)
        if path == "/api/dedupe":
            body = self._body()
            slug = body.get("slug", "")
            try:
                valid_slug(slug)
                result = dedupe_draft(slug, body.get("body_sha256"))
            except DraftRevisionConflict as error:
                return self._json({"error": str(error)}, 409)
            except dn.SlugLockBusy as error:
                return self._json({"error": str(error)}, 409)
            except FileNotFoundError:
                return self._json({"error": "not found"}, 404)
            except ValueError as error:
                return self._json({"error": str(error)}, 409)
            return self._json(result)
        m = re.match(r"^/api/drafts/([\w-]+)/translate$", path)
        if m:
            slug = m.group(1)
            body = self._body()
            if not os.path.exists(draft_path(slug)):
                return self._json({"error": "not found"}, 404)
            try:
                expected_body_sha256 = body.get("body_sha256")
                _require_body_revision(slug, expected_body_sha256)
            except DraftRevisionConflict as error:
                return self._json({"error": str(error)}, 409)
            except (ValueError, FileNotFoundError) as error:
                return self._json({"error": str(error)}, 400)
            started = start_translation(slug, expected_body_sha256)
            return self._json({"slug": slug, "translating": True,
                                "started": started, "already_running": not started,
                                "body_sha256": expected_body_sha256}, 202)
        if path == "/api/promote":
            b = self._body()
            slug, action = b.get("slug", ""), b.get("action", "")
            import promote_draft as pd
            try:
                with dn.slug_lock(slug, DRAFTS):
                    expected_body_sha256 = b.get("body_sha256")
                    _require_body_revision(slug, expected_body_sha256)
                    front, _, _ = pd.validate_promotion(slug, action, b.get("section") if action == "new" else b.get("into"))
                    if front.get("status") != "draft":
                        return self._json({"error": "该草稿已有入库任务正在运行"}, 409)
                    if not PROMOTE_LOCK.acquire(blocking=False):
                        return self._json({"error": "已有入库任务正在运行"}, 409)
                    try:
                        dn.refresh_front(slug, "promoting")
                        PROMOTE_THREADS.add(slug)
                    except Exception:
                        PROMOTE_LOCK.release()
                        raise
            except (ValueError, FileNotFoundError, dn.SlugLockBusy) as error:
                return self._json({"error": str(error)}, 409)
            try:
                threading.Thread(target=run_promote, args=(slug, action, b), daemon=True).start()
            except Exception:
                PROMOTE_THREADS.discard(slug)
                PROMOTE_LOCK.release()
                raise
            return self._json({"slug": slug, "status": "promoting"}, 202)
        self._json({"error": "no route"}, 404)

    def do_PATCH(self):
        try:
            self._guard_request("PATCH")
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        path = unquote(urlparse(self.path).path)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/requirements/(req_[A-Za-z0-9]+)$",
            path)
        if m:
            try:
                return self._json(update_project_requirement(
                    get_project_store(), m.group(1), m.group(2), self._body()))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/references/(ref_[A-Za-z0-9]+)$", path)
        if m:
            try:
                body = self._body()
                return self._json(get_project_store().update_reference(
                    m.group(1), m.group(2), note=body.get("note"),
                    read_status=body.get("read_status")))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, 404)
            except (ValueError, json.JSONDecodeError, AttributeError) as error:
                return self._json({"error": str(error)}, 400)
        self._json({"error": "no route"}, 404)

    def _create(self, b):
        name = (b.get("name") or "").strip()
        name_zh = (b.get("name_zh") or "").strip()
        desc = (b.get("desc") or "").strip()
        link = (b.get("link") or "").strip()
        if not desc and not link:
            return {"error": "一句话想法和调研链接至少填一个"}, 400
        top = dn.collision(desc) if desc else []
        if top and top[0][1] >= dn.HIGH_SIM and not b.get("force"):
            return {"error": f"与语料相似度过高 ({top[0][1]:.3f})，如确认请勾选 force",
                    "collision": top}, 409
        if name:
            slug = dn.slugify(b.get("slug") or name)
            if not slug:
                return {"error": "name must produce a non-empty slug"}, 400
            name_source = "user"
            with dn.slug_lock(slug, DRAFTS):
                taken = dn.slug_taken(slug)
                if taken:
                    return {"error": f"slug「{slug}」已存在于{'草稿区' if taken == 'draft' else '正式语料'}"}, 409
                idea = {"slug": slug, "name": name, "name_zh": name_zh,
                        "desc": desc, "link": link, "name_source": name_source}
                dn.write_draft(slug, idea, "opencode", "human")
        else:
            # 方案A：名字留空 -> 临时占位 slug，引擎调研后定名
            base = dn.slugify(desc or urlparse(link).netloc + urlparse(link).path) or "draft"
            base = ("wip-" + base)[:48]
            with dn.slug_lock(base, DRAFTS):
                slug = base
                suffix = 2
                while dn.slug_taken(slug):
                    slug = f"{base}-{suffix}"
                    suffix += 1
                name = "(调研后定名)"
                name_zh = ""
                name_source = "pending"
                idea = {"slug": slug, "name": name, "name_zh": name_zh,
                        "desc": desc, "link": link, "name_source": name_source}
                dn.write_draft(slug, idea, "opencode", "human")
        th = threading.Thread(target=run_engine, args=(slug,), daemon=True)
        GEN_THREADS[slug] = th
        th.start()
        return {"slug": slug, "status": "generating", "collision": top}, 201

    def do_PUT(self):
        try:
            self._guard_request("PUT")
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        path = unquote(urlparse(self.path).path)
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            slug = m.group(1)
            path = draft_path(slug)
            if not os.path.exists(path):
                return self._json({"error": "not found"}, 404)
            front, _ = parse_front(Path(path).read_text(encoding="utf-8"))
            review = load_review(PACK).get(slug, {})
            if _publication_state(slug, front, review)[1]:
                return self._json({"error": "草稿状态冲突，请先修复状态"}, 409)
            if front.get("status") in ("promoting", "generating", "promoted"):
                return self._json({"error": "当前状态不允许编辑"}, 409)
            payload = self._body()
            body = payload.get("body")
            if not isinstance(body, str):
                return self._json({"error": "body must be text"}, 400)
            try:
                body_sha256 = save_body(
                    slug, body, payload.get("expected_body_sha256"))
            except (DraftRevisionConflict, dn.SlugLockBusy) as error:
                return self._json({"error": str(error)}, 409)
            r = lint(path)
            status = "failed" if r["errors"] else "draft"
            dn.refresh_front(slug, status,
                             extra=f"lint_errors: {len(r['errors'])}\nlint_warnings: {len(r['warnings'])}")
            return self._json({"slug": slug, "body_sha256": body_sha256,
                                "lint": r, "status": status})
        self._json({"error": "no route"}, 404)

    def do_DELETE(self):
        try:
            self._guard_request("DELETE")
        except RequestBoundaryError as error:
            return self._boundary_error(error)
        path = unquote(urlparse(self.path).path)
        m = re.match(r"^/api/ask/threads/(ask_[0-9a-f]{32})$", path)
        if m:
            try:
                body = self._body()
                return self._json(atlas_ask.delete_thread(
                    m.group(1), body.get("confirm")))
            except atlas_ask.AskError as error:
                return self._json(_ask_error(error), error.status)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(r"^/api/settings/model/providers/([a-z0-9-]+)$", path)
        if m:
            try:
                body = self._body()
                return self._json(atlas_model.delete_provider(
                    m.group(1), body.get("confirm")))
            except atlas_model.ModelConfigError as error:
                body, status = _model_error(error)
                return self._json(body, status)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
        m = re.match(
            r"^/api/projects/(prj_[A-Za-z0-9]+)/backups/(\d{8}T\d{6}Z-[0-9a-f]{8}\.zip)$",
            path)
        if m:
            try:
                body = self._body()
                if not isinstance(body, dict) or set(body) != {"confirm"} \
                        or body.get("confirm") != BACKUP_DELETE_CONFIRMATION:
                    raise ValueError("explicit backup deletion confirmation is required")
                return self._json(delete_project_backup(
                    get_project_store(), m.group(1), m.group(2), body["confirm"]))
            except ProjectBackupError as error:
                return self._json(_api_error(error), 409)
            except ProjectStoreError as error:
                return self._json(_api_error(error, "not_found"), 404)
            except (ValueError, json.JSONDecodeError) as error:
                return self._json(_api_error(error, "invalid_request"), 400)
            except OSError as error:
                return self._json(_api_error(error, "service_unavailable", True), 500)
        m = re.match(r"^/api/projects/(prj_[A-Za-z0-9]+)$", path)
        if m:
            try:
                return self._json(delete_project(
                    m.group(1), self._body(), get_project_store()))
            except ProjectStoreError as error:
                return self._json({"error": str(error)}, _project_error_code(error))
            except (ValueError, json.JSONDecodeError) as error:
                return self._json({"error": str(error)}, 400)
        m = re.match(r"^/api/drafts/([\w-]+)$", path)
        if m:
            slug = m.group(1)
            try:
                return self._json(delete_draft(slug))
            except dn.SlugLockBusy as error:
                return self._json({"error": str(error)}, 409)
            except ValueError as error:
                return self._json({"error": str(error)}, 409)
        self._json({"error": "no route"}, 404)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=5199)
    args = ap.parse_args()
    with corpus_lock(PACK):
        recover_publication(PACK)
        for item in list_drafts():
            if item["status"] == "promoting":
                dn.refresh_front(item["slug"], "draft")
                update_review(item["slug"], {"promote_error": "上次入库中断，请重新查重后重试"}, PACK)
    draft_recovery = recover_interrupted_drafts()
    recovery = initialize_project_runtime()
    print("draft recovery:", json.dumps(draft_recovery, sort_keys=True))
    print(
        "project recovery:", json.dumps({
            "status": recovery["status"],
            "executions_interrupted": len(recovery["executions_interrupted"]),
            "generations_interrupted": len(recovery["generations_interrupted"]),
            "applications_requiring_review": len(
                recovery["applications_requiring_review"]),
        }, sort_keys=True))
    print(f"drafts API on :{args.port}  (drafts dir: {DRAFTS})")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
