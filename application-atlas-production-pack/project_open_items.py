"""Open analysis items: generated questions, conflicts, and suggestions.

Generation results are immutable files. This module derives the latest
completed run per mode, merges durable user dispositions from the project
store, and applies resolution actions (answer, defer, dismiss, convert).
"""
from __future__ import annotations

import hashlib

from project_generation import list_generations, read_generation
from project_store import ProjectStoreError


INBOX_MODES = ("analysis", "improvement", "value")
CONVERT_BY_KIND = {
    "question": {"decision"},
    "conflict": {"decision"},
    "suggestion": {"decision", "requirement"},
}
NOTE_REQUIRED = {"answered", "resolved", "accepted"}
TITLE_KEYS = {"question": "question", "conflict": "summary", "suggestion": "summary"}
DETAIL_KEYS = {"question": "why", "conflict": "impact", "suggestion": "reason"}


def _stable_key(item_kind: str, title: str) -> str:
    digest = hashlib.sha256(title.strip().encode()).hexdigest()[:16]
    return f"{item_kind}:{digest}"


def _reference_ids(item: dict) -> list[str]:
    evidence = item.get("evidence")
    if not isinstance(evidence, list):
        return []
    return [value.get("id") for value in evidence
            if isinstance(value, dict) and value.get("kind") == "reference"
            and isinstance(value.get("id"), str)]


def _run_items(run: dict) -> list[dict]:
    result = run.get("result") or {}
    items = []
    kinds = (("question", result.get("questions") or []),
             ("conflict", result.get("conflicts") or []),
             ("suggestion", result.get("suggestions") or []))
    for item_kind, source in kinds:
        for index, item in enumerate(source):
            if not isinstance(item, dict):
                continue
            title = item.get(TITLE_KEYS[item_kind])
            if not isinstance(title, str) or not title.strip():
                continue
            detail = item.get(DETAIL_KEYS[item_kind]) or ""
            items.append({
                "id": f"{run['id']}:{item_kind}:{index}",
                "run_id": run["id"],
                "mode": run["mode"],
                "kind": item_kind,
                "index": index,
                "key": _stable_key(item_kind, title),
                "title": title,
                "detail": detail if isinstance(detail, str) else "",
                "affects": [value for value in item.get("affects") or []
                            if isinstance(value, str)],
                "reference_ids": _reference_ids(item),
                "created_at": run.get("created_at", ""),
            })
    return items


def latest_items_by_mode(store, project_id: str) -> dict[str, list[dict]]:
    latest: dict[str, dict] = {}
    for run in list_generations(store, project_id):
        if run.get("status") != "completed" or run.get("mode") not in INBOX_MODES:
            continue
        if run["mode"] in latest:
            continue
        latest[run["mode"]] = run
    return {mode: _run_items(latest[mode]) for mode in INBOX_MODES if mode in latest}


def list_open_items(store, project_id: str) -> list[dict]:
    store.get_project(project_id)
    dispositions = {
        (row["run_id"], row["item_kind"], row["item_index"]): row
        for row in store.list_open_item_dispositions(project_id)
    }
    items = []
    current_modes = {mode for mode in ("analysis", "improvement")}
    for mode, run_items in latest_items_by_mode(store, project_id).items():
        for item in run_items:
            row = dispositions.get((item["run_id"], item["kind"], item["index"]))
            merged = dict(item)
            merged["status"] = row["status"] if row else "open"
            merged["note"] = row["note"] if row else ""
            merged["decision_id"] = row["decision_id"] if row else None
            merged["requirement_id"] = row["requirement_id"] if row else None
            merged["current"] = mode in current_modes
            items.append(merged)
    return items


def _find_item(store, project_id: str, body: dict) -> tuple[dict, list[dict]]:
    run_id = body.get("run_id")
    item_kind = body.get("item_kind")
    item_index = body.get("item_index")
    item_key = body.get("item_key")
    if not isinstance(run_id, str) or not run_id.strip():
        raise ValueError("run_id is required")
    if item_kind not in TITLE_KEYS:
        raise ValueError("item_kind must be question, conflict, or suggestion")
    if not isinstance(item_index, int) or isinstance(item_index, bool) or item_index < 0:
        raise ValueError("item_index must be a non-negative integer")
    run = read_generation(store, project_id, run_id)
    if run.get("status") != "completed" or run.get("mode") not in INBOX_MODES:
        raise ProjectStoreError("open items come from completed analysis, improvement, or value runs")
    items = _run_items(run)
    for item in items:
        if item["kind"] == item_kind and item["index"] == item_index:
            if not isinstance(item_key, str) or item_key != item["key"]:
                raise ProjectStoreError(
                    "this generated item changed; reload the workspace before resolving it")
            return item, items
    raise ProjectStoreError("generated item not found")


def resolve_open_item(store, project_id: str, body: dict) -> dict:
    if not isinstance(body, dict):
        raise ValueError("body must be an object")
    item, _items = _find_item(store, project_id, body)
    status = body.get("status")
    if not isinstance(status, str):
        raise ValueError("status is required")
    note = body.get("note", "")
    if not isinstance(note, str):
        raise ValueError("note must be text")
    note = note.strip()
    if status in NOTE_REQUIRED and not note:
        raise ValueError(f"a note is required to mark an item {status}")
    convert = body.get("convert")
    if convert is not None:
        if convert not in CONVERT_BY_KIND[item["kind"]]:
            raise ValueError(f"{item['kind']} items cannot convert to {convert}")
    decision = requirement = None
    if convert == "decision":
        if not note:
            raise ValueError("a note is required to record a decision")
        decision = {
            "statement": note,
            "rationale": f"针对「{item['title']}」的处理记录。{item['detail']}".strip(),
            "reference_ids": item["reference_ids"],
        }
    elif convert == "requirement":
        requirement = {
            "content": item["title"],
            "recommendation_reason": note or item["detail"],
            "acceptance_conditions": [],
            "reference_ids": item["reference_ids"],
        }
    result = store.resolve_open_item(
        project_id, item["run_id"], item["kind"], item["index"], item["key"],
        status, note, decision, requirement)
    merged = dict(item)
    merged["status"] = result["disposition"]["status"]
    merged["note"] = result["disposition"]["note"]
    merged["decision_id"] = result["disposition"]["decision_id"]
    merged["requirement_id"] = result["disposition"]["requirement_id"]
    merged["current"] = item["mode"] in ("analysis", "improvement")
    return {"item": merged, "decision_id": result["decision_id"],
            "requirement_id": result["requirement_id"]}
