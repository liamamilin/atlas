"""Project OpenCode records into stable U17 execution states.

The projection deliberately uses snapshot endpoints as its source of truth.
SSE events may make the UI faster, but they are not required to rebuild state
after a disconnect.
"""
from __future__ import annotations


STATES = {
    "queued",
    "running",
    "waiting_permission",
    "waiting_input",
    "completed",
    "failed",
    "stopped",
    "unknown",
}


def project_execution(reconcile: dict, task_message_id: str | None = None) -> dict:
    """Return an engine-independent status plus the evidence used to derive it.

    ``task_message_id`` is the OpenCode user message created for one Atlas task.
    Passing it prevents messages from older tasks in the same session from
    affecting the result.
    """
    messages = reconcile.get("messages") or []
    pending = reconcile.get("pending_permissions") or []
    status_record = reconcile.get("status") or {"type": "idle"}
    engine_status = status_record.get("type", "idle")
    relevant = _relevant_messages(messages, task_message_id)

    permission = _last_matching_permission(pending, relevant)
    if permission:
        return _result("waiting_permission", engine_status, relevant,
                       permission_id=permission.get("id"))

    question = _pending_question(reconcile.get("pending_questions") or [], relevant)
    if question:
        return _result("waiting_input", engine_status, relevant,
                       question_id=question.get("id"))

    error = _last_error(relevant)
    if error:
        name = error.get("name") or error.get("type") or "UnknownError"
        state = "stopped" if name == "MessageAbortedError" else "failed"
        return _result(state, engine_status, relevant, error=name)

    if engine_status in {"busy", "retry"}:
        return _result("running", engine_status, relevant)

    completed = [item for item in relevant
                 if item.get("info", {}).get("role") == "assistant"
                 and item.get("info", {}).get("time", {}).get("completed")
                 and item.get("info", {}).get("finish") == "stop"]
    if completed:
        return _result("completed", engine_status, relevant,
                       message_id=completed[-1]["info"].get("id"))

    if task_message_id and not relevant:
        return _result("queued", engine_status, relevant)
    return _result("unknown", engine_status, relevant)


def _relevant_messages(messages: list[dict], task_message_id: str | None) -> list[dict]:
    if not task_message_id:
        return messages
    return [item for item in messages if (
        item.get("info", {}).get("id") == task_message_id
        or item.get("info", {}).get("parentID") == task_message_id
    )]


def _related_message_ids(messages: list[dict]) -> set[str]:
    return {item.get("info", {}).get("id") for item in messages
            if item.get("info", {}).get("id")}


def _last_matching_permission(items: list[dict], messages: list[dict]) -> dict | None:
    ids = _related_message_ids(messages)
    matches = [item for item in items
               if not ids or (item.get("tool") or {}).get("messageID") in ids]
    return matches[-1] if matches else None


def _pending_question(items: list[dict], messages: list[dict]) -> dict | None:
    ids = _related_message_ids(messages)
    matches = [item for item in items
               if not ids or item.get("messageID") in ids
               or (item.get("tool") or {}).get("messageID") in ids]
    return matches[-1] if matches else None


def _last_error(messages: list[dict]) -> dict | None:
    errors = [item.get("info", {}).get("error") for item in messages
              if item.get("info", {}).get("error")]
    return errors[-1] if errors else None


def _result(state: str, engine_status: str, messages: list[dict], **evidence) -> dict:
    return {
        "state": state,
        "engine_status": engine_status,
        "evidence": {
            "message_ids": sorted(_related_message_ids(messages)),
            **evidence,
        },
    }
