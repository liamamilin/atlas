"""Source-grounded, review-before-apply document generation for U17 projects.

Atlas owns the immutable input and result files. OpenCode is only the first
replaceable runner used to produce a proposal from that input.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import threading
import uuid

from atlas_runtime import atomic_json, atomic_write
from project_store import ProjectStoreError
from project_workflow import DOCUMENT_KINDS


RUN_STATES = {"queued", "running", "completed", "failed"}
MODES = {"analysis", "documents"}
SCOPES = {"current", "later", "excluded"}
MAX_INPUT_CHARS = 500_000
MAX_RESULT_BYTES = 2_000_000
_STATE_LOCK = threading.RLock()


def prepare_generation(store, project_id: str, mode: str,
                       document_kinds: list[str] | None = None,
                       model: str = "") -> dict:
    if mode not in MODES:
        raise ValueError("mode must be analysis or documents")
    if not isinstance(model, str):
        raise ValueError("model must be text")
    targets = ["analysis"] if mode == "analysis" else _document_kinds(document_kinds)
    request = build_generation_input(store, project_id, mode, targets)
    run_id = "gen_" + uuid.uuid4().hex
    directory = _run_root(store, project_id) / run_id
    directory.mkdir(parents=True)
    atomic_json(directory / "input.json", request)
    atomic_write(directory / "input.md", render_generation_input(request))
    atomic_write(directory / "prompt.md", render_generation_prompt(request))
    now = _now()
    run = {
        "id": run_id,
        "project_id": project_id,
        "mode": mode,
        "document_kinds": targets,
        "engine": "opencode",
        "model": model.strip(),
        "status": "queued",
        "input_fingerprint": request["input_fingerprint"],
        "result": None,
        "applied": {"requirements": {}, "documents": {}},
        "error": "",
        "engine_session_id": None,
        "created_at": now,
        "updated_at": now,
    }
    atomic_json(directory / "run.json", run)
    return run


def build_generation_input(store, project_id: str, mode: str,
                           document_kinds: list[str]) -> dict:
    project = store.get_project(project_id)
    references = store.list_references(project_id)
    if not references:
        raise ValueError("at least one fixed project reference is required")
    requirements = store.list_requirements(project_id)
    if mode == "documents":
        requirements = [item for item in requirements
                        if item["confirmed_scope"] == "current"]
        if not requirements:
            raise ValueError("document generation requires a confirmed current-scope requirement")
    decisions = store.list_decisions(project_id)
    documents = store.list_documents(project_id)
    payload = {
        "schema": 1,
        "mode": mode,
        "project": {
            "id": project["id"], "name": project["name"],
            "objective": project["objective"], "mode": project["mode"],
        },
        "document_kinds": document_kinds,
        "references": [{
            "id": item["id"], "source_kind": item["source_kind"],
            "source_ref": item["source_ref"], "source_version": item["source_version"],
            "locator": item["locator"], "excerpt": item["excerpt"],
            "project_note": item["note"], "read_status": item["read_status"],
        } for item in references],
        "requirements": [{
            key: item[key] for key in (
                "id", "content", "recommended_scope", "recommendation_reason",
                "confirmed_scope", "confirmation_reason", "acceptance_conditions",
                "reference_ids")
        } for item in requirements],
        "decisions": [{
            key: item[key] for key in ("id", "statement", "rationale", "reference_ids")
        } for item in decisions],
        "documents": [{
            key: item[key] for key in (
                "id", "kind", "title", "current_version", "version_id", "content",
                "content_sha256", "basis", "author", "change_summary")
        } for item in documents],
    }
    canonical = _canonical(payload)
    if len(canonical) > MAX_INPUT_CHARS:
        raise ValueError("fixed project input is too large for one generation run")
    payload["input_fingerprint"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


def render_generation_prompt(request: dict) -> str:
    targets = ", ".join(request["document_kinds"])
    requirements_example = (
        '''[{\n    "key": "short-local-key", "content": "...",\n    "recommended_scope": "current|later|excluded", "recommendation_reason": "...",\n    "acceptance_conditions": ["..."], "reference_ids": ["ref_..."]\n  }]'''
        if request["mode"] == "analysis" else "[]"
    )
    mode_rules = (
        "Analyze the evidence. Return candidate requirements with recommendations, open questions, "
        "evidence-backed conflicts and optional suggestions. Also draft one analysis document."
        if request["mode"] == "analysis" else
        "DOCUMENTS MODE: draft only the requested document kinds from confirmed current-scope "
        "requirements and the fixed evidence. The result `requirements` array MUST be exactly empty "
        "(`[]`). Do not propose, restate, or infer candidate requirements outside document content."
    )
    return f"""# Atlas U17 generation task

Read `input.md` completely. It is the only factual input for this task. `input.json` is retained for
Atlas validation; do not use its long JSON lines as a substitute for the complete Markdown input.
Do not browse the web,
inspect other directories, call Bash, or use unstated product facts. {mode_rules}

Requested document kinds: {targets}

Write the final result to `result.json` as UTF-8 JSON with this exact top-level shape:

```json
{{
  "input_fingerprint": "copy from input.md",
  "questions": [{{"question": "...", "why": "...", "affects": ["document-kind"]}}],
  "requirements": {requirements_example},
  "conflicts": [{{"summary": "...", "impact": "...", "evidence": [{{"kind": "reference", "id": "ref_..."}}]}}],
  "suggestions": [{{"summary": "...", "reason": "...", "evidence": [{{"kind": "reference", "id": "ref_..."}}]}}],
  "documents": [{{
    "document_id": null, "kind": "one requested kind", "title": "...", "content": "complete Markdown",
    "basis": [{{"kind": "reference|requirement|decision|document_version", "id": "existing input id"}}]
  }}]
}}
```

Rules:

1. Copy `input_fingerprint` from `input.md` exactly. Atlas rejects results for any other input version.
2. Every factual claim and recommendation must stay within the fixed excerpts. Mark uncertainty
   explicitly. A missing detail remains unknown.
3. A reference is background evidence, not the project's product specification. Its `Project note`
   states why it was selected and controls how it may be used. Do not convert features, examples or
   scope from a referenced application type into project requirements unless the project objective,
   a confirmed requirement, a decision, or the project note explicitly connects them. State every
   candidate in terms of this project and its product; do not restate the referenced category.
4. Recommendations are advice only. Never state that the user confirmed them.
5. Requirements are allowed only in analysis mode. Give each a unique local key, at least one fixed
   reference, a concrete reason and observable acceptance conditions. Do not re-propose an existing
   requirement. If a proposal depends on an open question, omit it or recommend `later`, never `current`.
6. Documents must use only requested kinds and cite non-empty basis IDs present in the fixed input.
   If the fixed input already contains a document of that kind, `document_id` MUST select one such
   document as the new-version target; use null only when no document of that kind exists. In
   documents mode, product scope comes only from confirmed current-scope requirements. Citation
   kinds must match ID prefixes: `ref_` = reference, `req_` = requirement, `dec_` = decision and
   `dver_` = document_version. A `doc_` ID is never a basis ID. Do not cite the target document's
   own current version as an upstream basis; Atlas already records its version chain.
7. Preserve useful human-authored content from existing documents unless the fixed input contradicts
   it; explain uncertainty instead of silently deleting it.
8. `conflicts` contains only explicit contradictions with locatable evidence. Put unresolved choices
   in `questions` and optional practices in `suggestions`. Ask only questions that materially affect
   this project's scope or requested document, not missing details of the reference product itself.
9. Write valid JSON, without Markdown fences or text outside `result.json`.
10. Use the language of the project name and objective for recommendations and documents. Preserve
   source identifiers and short quotations in their original language.
11. Prefer a small set of high-confidence outputs: at most 6 questions, 8 candidate requirements,
    4 conflicts and 6 suggestions. Write one concise complete document for each requested kind. After writing
    `result.json`, stop without running a separate validation command; Atlas validates the file.
"""


def render_generation_input(request: dict) -> str:
    project = request["project"]
    lines = [
        "# Atlas fixed generation input", "",
        f"Input fingerprint: `{request['input_fingerprint']}`", "",
        "## Project", "", f"- ID: `{project['id']}`", f"- Name: {project['name']}",
        f"- Objective: {project['objective']}", f"- Mode: `{project['mode']}`", "",
        "## Requested document kinds", "",
    ]
    lines.extend(f"- `{kind}`" for kind in request["document_kinds"])
    lines.extend([
        "", "## Citation ID rules", "",
        "- `ref_…` uses kind `reference`.",
        "- `req_…` uses kind `requirement`.",
        "- `dec_…` uses kind `decision`.",
        "- `dver_…` uses kind `document_version`.",
        "- `doc_…` identifies a document target and is never a basis ID.",
        "", "## Fixed references", "",
    ])
    for item in request["references"]:
        lines.extend([
            f"### `{item['id']}` · {item['source_ref']}", "",
            f"- Kind: `{item['source_kind']}`", f"- Version: `{item['source_version']}`",
            f"- Locator: `{item['locator'] or 'full'}`", f"- Read status: `{item['read_status']}`",
            f"- Project note: {item['project_note'] or 'none'}", "", "Fixed excerpt:", "",
            _readable(item["excerpt"]), "",
        ])
    lines.extend(["## Requirements", ""])
    for item in request["requirements"]:
        lines.extend([
            f"### `{item['id']}`", "", item["content"], "",
            f"- AI recommendation: `{item['recommended_scope'] or 'none'}` — {item['recommendation_reason'] or 'none'}",
            f"- User confirmation: `{item['confirmed_scope'] or 'pending'}` — {item['confirmation_reason'] or 'none'}",
            f"- Reference IDs: {', '.join(item['reference_ids']) or 'none'}", "",
            "Acceptance conditions:", "",
        ])
        lines.extend(f"- {value}" for value in item["acceptance_conditions"])
        lines.append("")
    if not request["requirements"]:
        lines.extend(["No requirements recorded.", ""])
    lines.extend(["## Decisions", ""])
    for item in request["decisions"]:
        lines.extend([
            f"### `{item['id']}` · {item['statement']}", "", item["rationale"], "",
            f"Reference IDs: {', '.join(item['reference_ids']) or 'none'}", "",
        ])
    if not request["decisions"]:
        lines.extend(["No decisions recorded.", ""])
    lines.extend(["## Existing document versions", ""])
    for item in request["documents"]:
        basis = ", ".join(
            f"{value.get('kind', 'unknown')}:{value.get('id', 'unknown')}"
            for value in item["basis"])
        lines.extend([
            f"### `{item['id']}` / `{item['version_id']}` · {item['title']}", "",
            f"- Kind: `{item['kind']}`", f"- Version: {item['current_version']}",
            f"- Author: `{item['author']}`", f"- Change summary: {item['change_summary'] or 'none'}",
            f"- SHA-256: `{item['content_sha256']}`",
            f"- Basis: {basis or 'none'}",
            "",
            _readable(item["content"]), "",
        ])
    if not request["documents"]:
        lines.extend(["No documents recorded.", ""])
    return "\n".join(lines).rstrip() + "\n"


def execute_generation(store, project_id: str, run_id: str, runner=None) -> dict:
    directory = _run_directory(store, project_id, run_id)
    run = read_generation(store, project_id, run_id)
    if run["status"] != "queued":
        raise ProjectStoreError("generation run is not queued")
    try:
        request = json.loads((directory / "input.json").read_text())
        _verify_request(request, run["input_fingerprint"])
        expected_markdown = render_generation_input(request)
        if (directory / "input.md").read_text() != expected_markdown:
            raise ValueError("generation Markdown input does not match its fixed JSON content")
    except BaseException as error:
        _update_run(directory, run, status="failed", error=str(error))
        raise
    _update_run(directory, run, status="running", error="")
    try:
        result, metadata = (runner or _run_opencode)(directory, run)
        validated = validate_generation_result(request, result)
        return _update_run(
            directory, run, status="completed", result=validated,
            engine_session_id=metadata.get("engine_session_id"), error="")
    except BaseException as error:
        _update_run(directory, run, status="failed", error=str(error))
        raise


def read_generation(store, project_id: str, run_id: str) -> dict:
    path = _run_directory(store, project_id, run_id) / "run.json"
    with _STATE_LOCK:
        run = json.loads(path.read_text())
    if run.get("project_id") != project_id or run.get("status") not in RUN_STATES:
        raise ProjectStoreError("invalid generation run")
    return run


def list_generations(store, project_id: str) -> list[dict]:
    store.get_project(project_id)
    root = _run_root(store, project_id)
    if not root.exists():
        return []
    runs = []
    for path in root.glob("gen_*/run.json"):
        try:
            run = json.loads(path.read_text())
            if run.get("project_id") == project_id and run.get("status") in RUN_STATES:
                runs.append(run)
        except (OSError, ValueError):
            continue
    return sorted(runs, key=lambda item: (item["created_at"], item["id"]), reverse=True)


def mark_generation_interrupted(store, project_id: str, run_id: str) -> dict:
    directory = _run_directory(store, project_id, run_id)
    run = read_generation(store, project_id, run_id)
    if run["status"] in {"queued", "running"}:
        return _update_run(
            directory, run, status="failed",
            error="The API process stopped before this generation run finished. Start a new run.")
    return run


def apply_generation_item(store, project_id: str, run_id: str,
                          item_kind: str, index: int) -> dict:
    if item_kind not in {"requirement", "document"}:
        raise ValueError("item_kind must be requirement or document")
    if not isinstance(index, int) or isinstance(index, bool) or index < 0:
        raise ValueError("index must be a non-negative integer")
    directory = _run_directory(store, project_id, run_id)
    with _STATE_LOCK:
        run = read_generation(store, project_id, run_id)
        if run["status"] != "completed" or not run.get("result"):
            raise ProjectStoreError("generation run is not completed")
        plural = item_kind + "s"
        items = run["result"].get(plural) or []
        if index >= len(items):
            raise ValueError("generation item index is out of range")
        key = str(index)
        if key in run["applied"][plural]:
            raise ProjectStoreError("generation item already applied")
        item = items[index]
        if item_kind == "requirement":
            created = store.create_requirement(
                project_id, item["content"], item["recommended_scope"],
                item["recommendation_reason"], item["acceptance_conditions"],
                item["reference_ids"])
        else:
            if item["document_id"]:
                request = json.loads((directory / "input.json").read_text())
                _verify_request(request, run["input_fingerprint"])
                source = next(value for value in request["documents"]
                              if value["id"] == item["document_id"])
                created = store.add_document_version(
                    item["document_id"], item["content"], item["basis"],
                    expected_current_version=source["current_version"], author="ai",
                    change_summary=f"Generated by {run_id}")
            else:
                created = store.create_document(
                    project_id, item["kind"], item["title"], item["content"], item["basis"],
                    author="ai", change_summary=f"Generated by {run_id}")
        run["applied"][plural][key] = created["id"]
        run["updated_at"] = _now()
        atomic_json(directory / "run.json", run)
    return {"run": run, "created": created}


def validate_generation_result(request: dict, result: dict) -> dict:
    if not isinstance(result, dict):
        raise ValueError("generation result must be an object")
    expected = {"input_fingerprint", "questions", "requirements", "conflicts",
                "suggestions", "documents"}
    if set(result) != expected:
        raise ValueError("generation result has an invalid top-level shape")
    if result["input_fingerprint"] != request["input_fingerprint"]:
        raise ValueError("generation result input fingerprint does not match")
    references = {item["id"] for item in request["references"]}
    requirements = {item["id"] for item in request["requirements"]}
    decisions = {item["id"] for item in request["decisions"]}
    versions = {item["version_id"] for item in request["documents"]}
    existing_documents = {item["id"]: item for item in request["documents"]}
    targets = set(request["document_kinds"])
    questions = _objects(result["questions"], "questions")
    for item in questions:
        _keys(item, {"question", "why", "affects"}, "question")
        _nonempty(item["question"], "question")
        _nonempty(item["why"], "question why")
        affects = _strings(item["affects"], "question affects", allow_empty=True)
        if not set(affects).issubset(targets):
            raise ValueError("question affects an unrequested document kind")
    generated_requirements = _objects(result["requirements"], "requirements")
    if request["mode"] != "analysis" and generated_requirements:
        raise ValueError("requirements are only allowed in analysis mode")
    seen_keys = set()
    for item in generated_requirements:
        _keys(item, {"key", "content", "recommended_scope", "recommendation_reason",
                     "acceptance_conditions", "reference_ids"}, "requirement")
        key = _nonempty(item["key"], "requirement key")
        if key in seen_keys:
            raise ValueError("requirement keys must be unique")
        seen_keys.add(key)
        _nonempty(item["content"], "requirement content")
        if item["recommended_scope"] not in SCOPES:
            raise ValueError("invalid generated requirement scope")
        _nonempty(item["recommendation_reason"], "recommendation reason")
        _strings(item["acceptance_conditions"], "acceptance conditions")
        ids = _strings(item["reference_ids"], "requirement reference_ids")
        if not set(ids).issubset(references):
            raise ValueError("generated requirement cites an unknown reference")
    for field in ("conflicts", "suggestions"):
        for item in _objects(result[field], field):
            required = {"summary", "evidence", "impact" if field == "conflicts" else "reason"}
            _keys(item, required, field[:-1])
            _nonempty(item["summary"], f"{field} summary")
            _nonempty(item["impact" if field == "conflicts" else "reason"], field)
            _basis(item["evidence"], references, requirements, decisions, versions)
    documents = _objects(result["documents"], "documents")
    seen_kinds = set()
    for item in documents:
        _keys(item, {"document_id", "kind", "title", "content", "basis"}, "document")
        if item["kind"] not in targets or item["kind"] in seen_kinds:
            raise ValueError("generated document kind is unrequested or duplicated")
        seen_kinds.add(item["kind"])
        document_id = item["document_id"]
        same_kind_documents = {
            key for key, value in existing_documents.items() if value["kind"] == item["kind"]
        }
        if document_id is None and same_kind_documents:
            raise ValueError("generated document must target an existing document of this kind")
        if document_id is not None and (
                not isinstance(document_id, str)
                or document_id not in existing_documents
                or existing_documents[document_id]["kind"] != item["kind"]):
            raise ValueError("generated document targets an unknown or mismatched document")
        _nonempty(item["title"], "document title")
        content = _nonempty(item["content"], "document content")
        if len(content) > 200_000:
            raise ValueError("generated document is too large")
        _basis(item["basis"], references, requirements, decisions, versions)
        if document_id:
            own_version = existing_documents[document_id]["version_id"]
            item["basis"] = [
                value for value in item["basis"]
                if not (value["kind"] == "document_version" and value["id"] == own_version)
            ]
            if not item["basis"]:
                raise ValueError("generated document basis cannot contain only its own prior version")
    return result


def _run_opencode(directory: Path, run: dict) -> tuple[dict, dict]:
    config = {
        "$schema": "https://opencode.ai/config.json",
        "permission": {
            "read": "allow", "edit": "allow", "glob": "allow", "grep": "allow",
            "list": "allow", "bash": "deny", "webfetch": "deny", "websearch": "deny",
            "external_directory": "deny", "task": "deny", "question": "deny",
        },
    }
    workspace = directory / "engine"
    workspace.mkdir(exist_ok=True)
    atomic_write(workspace / "input.json", (directory / "input.json").read_text())
    atomic_write(workspace / "input.md", (directory / "input.md").read_text())
    atomic_write(workspace / "prompt.md", (directory / "prompt.md").read_text())
    atomic_json(workspace / "opencode.json", config)
    command = ["opencode", "run", "--pure", "--dir", str(workspace), "--format", "json",
               "--title", f"Atlas U17 {run['id']}"]
    if run["model"]:
        command.extend(["--model", run["model"]])
    command.append((workspace / "prompt.md").read_text())
    environment = dict(os.environ)
    environment["OPENCODE_CONFIG"] = str(workspace / "opencode.json")
    with (directory / "engine.log").open("wb") as log:
        process = subprocess.run(
            command, cwd=workspace, env=environment, stdout=log, stderr=subprocess.STDOUT,
            timeout=1800)
    if process.returncode:
        raise RuntimeError(f"OpenCode exited with status {process.returncode}")
    result_path = workspace / "result.json"
    if not result_path.is_file() or result_path.stat().st_size > MAX_RESULT_BYTES:
        raise RuntimeError("OpenCode did not produce a valid-sized result.json")
    result = json.loads(result_path.read_text())
    return result, {"engine_session_id": _extract_session_id(directory / "engine.log")}


def _extract_session_id(path: Path) -> str | None:
    pattern = re.compile(r'"sessionID"\s*:\s*"(ses_[A-Za-z0-9]+)"')
    for line in path.read_text(errors="replace").splitlines():
        match = pattern.search(line)
        if match:
            return match.group(1)
    return None


def _basis(value, references, requirements, decisions, versions):
    items = _objects(value, "basis")
    if not items:
        raise ValueError("evidence or document basis must not be empty")
    allowed = {
        "reference": references, "requirement": requirements,
        "decision": decisions, "document_version": versions,
    }
    seen = set()
    for item in items:
        _keys(item, {"kind", "id"}, "basis")
        kind, item_id = item["kind"], item["id"]
        if kind not in allowed or item_id not in allowed[kind]:
            matches = [name for name, ids in allowed.items() if item_id in ids]
            if len(matches) != 1:
                raise ValueError("basis cites an unknown input")
            kind = matches[0]
            item["kind"] = kind
        if (kind, item_id) in seen:
            raise ValueError("basis contains duplicates")
        seen.add((kind, item_id))
    return items


def _document_kinds(value):
    if not isinstance(value, list) or not value:
        raise ValueError("document_kinds must be a non-empty list")
    if not all(isinstance(item, str) and item in DOCUMENT_KINDS for item in value):
        raise ValueError("document_kinds contains an invalid kind")
    if len(value) != len(set(value)):
        raise ValueError("document_kinds contains duplicates")
    return value


def _objects(value, label):
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        raise ValueError(f"{label} must be a list of objects")
    return value


def _strings(value, label, allow_empty=False):
    if not isinstance(value, list) or not all(
            isinstance(item, str) and item.strip() for item in value):
        raise ValueError(f"{label} must be a list of non-empty text")
    if not allow_empty and not value:
        raise ValueError(f"{label} must not be empty")
    if len(value) != len(set(value)):
        raise ValueError(f"{label} contains duplicates")
    return value


def _keys(value, expected, label):
    if not expected.issubset(value):
        raise ValueError(f"{label} has an invalid shape")
    for key in set(value) - expected:
        value.pop(key)


def _nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value


def _run_root(store, project_id):
    return store.path.parent / "generation-runs" / project_id


def _run_directory(store, project_id, run_id):
    if not re.fullmatch(r"gen_[A-Za-z0-9]+", run_id):
        raise ValueError("invalid generation run id")
    store.get_project(project_id)
    directory = _run_root(store, project_id) / run_id
    if not (directory / "run.json").is_file():
        raise ProjectStoreError("generation run not found")
    return directory


def _update_run(directory, run, **changes):
    with _STATE_LOCK:
        current = json.loads((directory / "run.json").read_text())
        current.update(changes)
        current["updated_at"] = _now()
        atomic_json(directory / "run.json", current)
        return current


def _canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _readable(value):
    lines = []
    for line in str(value).splitlines() or [""]:
        lines.extend(line[index:index + 1200] for index in range(0, max(len(line), 1), 1200))
    return "\n".join(lines)


def _verify_request(request, expected_fingerprint):
    if not isinstance(request, dict):
        raise ValueError("generation input must be an object")
    payload = dict(request)
    fingerprint = payload.pop("input_fingerprint", None)
    actual = hashlib.sha256(_canonical(payload).encode()).hexdigest()
    if fingerprint != expected_fingerprint or actual != expected_fingerprint:
        raise ValueError("generation input fingerprint does not match its fixed content")


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")
