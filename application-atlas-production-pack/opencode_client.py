"""Small, version-aware OpenCode HTTP adapter for U17.

Atlas owns project/task state. This client only translates calls to the
OpenCode server and normalizes the V2 response shape to the small internal
contract used by the execution state projector. The legacy V1 endpoints remain
available for projects that intentionally pin the V1 CLI.
"""
from __future__ import annotations

import base64
import json
from typing import BinaryIO, Iterator
from urllib.error import HTTPError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen


class OpenCodeError(RuntimeError):
    def __init__(self, status: int, message: str, body=None):
        super().__init__(message)
        self.status = status
        self.body = body


class OpenCodeClient:
    """Client for the documented OpenCode server APIs used by U17."""

    def __init__(self, base_url: str, directory: str, timeout: int = 300,
                 opener=urlopen, major_version: int | None = None,
                 username: str | None = None, password: str | None = None,
                 permissions: list[dict] | None = None):
        parsed = urlparse(base_url)
        if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("OpenCode base URL must be a local HTTP endpoint")
        if not directory:
            raise ValueError("directory is required")
        self.base_url = base_url.rstrip("/")
        self.directory = directory
        self.timeout = timeout
        self._opener = opener
        # None deliberately means the legacy adapter. Runtime passes the
        # detected major version; tests and V1 callers retain the old contract.
        self.major_version = int(major_version) if major_version is not None else 1
        self.username = username or "opencode"
        self.password = password
        self.permissions = list(permissions) if permissions is not None else None
        self._permission_sessions: dict[str, str] = {}
        self._form_fields: dict[str, list[dict]] = {}
        self._form_session_map: dict[str, str] = {}

    @property
    def v2(self) -> bool:
        return self.major_version >= 2

    def health(self):
        path = "/api/info" if self.v2 else "/global/health"
        return self._unwrap(self._request("GET", path, scoped=False))

    def create_session(self, title: str, parent_id: str | None = None):
        if self.v2:
            # V2 exposes parent sessions through fork/import routes rather
            # than the V1 create-session field; U17 creates root sessions.
            body = {"title": title, "location": {"directory": self.directory}}
            if self.permissions is not None:
                body["permissions"] = self.permissions
            return self._unwrap(self._request("POST", "/api/session", body))
        body = {"title": title}
        if parent_id:
            body["parentID"] = parent_id
        return self._request("POST", "/session", body)

    def get_session(self, session_id: str):
        session_id = _identifier(session_id, "ses")
        if self.v2:
            return self._unwrap(self._request("GET", f"/api/session/{session_id}"))
        return self._request("GET", f"/session/{session_id}")

    def session_statuses(self):
        if self.v2:
            result = self._request("GET", "/api/session/active")
            return result.get("data", {}) if isinstance(result, dict) else {}
        return self._request("GET", "/session/status")

    def messages(self, session_id: str, limit: int | None = None):
        session_id = _identifier(session_id, "ses")
        query = {} if limit is None else {"limit": max(0, int(limit))}
        if self.v2:
            query = {**query, "order": "desc"}
            result = self._request(
                "GET", f"/api/session/{session_id}/message", query=query)
            raw_messages = result.get("data", []) if isinstance(result, dict) else []
            raw_messages = list(raw_messages)
            raw_messages.reverse()
            return _normalize_v2_messages(raw_messages)
        return self._request("GET", f"/session/{session_id}/message", query=query)

    def send_message(self, session_id: str, text: str, provider_id: str,
                     model_id: str, agent: str = "build", tools: dict | None = None,
                     system: str | None = None):
        if self.v2:
            return self._send_v2_message(
                session_id, text, provider_id, model_id, agent, system)
        body = _message_body(text, provider_id, model_id, agent, tools, system)
        return self._request(
            "POST", f"/session/{_identifier(session_id, 'ses')}/message", body)

    def send_message_async(self, session_id: str, text: str, provider_id: str,
                           model_id: str, agent: str = "build", tools: dict | None = None,
                           system: str | None = None):
        """Start work without holding the HTTP request open through approvals.

        V2's prompt endpoint accepts an inbox delivery and returns immediately;
        V1 retains its historical prompt_async endpoint.
        """
        if self.v2:
            return self._send_v2_message(
                session_id, text, provider_id, model_id, agent, system)
        body = _message_body(text, provider_id, model_id, agent, tools, system)
        return self._request(
            "POST", f"/session/{_identifier(session_id, 'ses')}/prompt_async", body)

    def abort(self, session_id: str):
        session_id = _identifier(session_id, "ses")
        if self.v2:
            return self._unwrap(self._request(
                "POST", f"/api/session/{session_id}/interrupt", {}))
        return self._request("POST", f"/session/{session_id}/abort", {})

    def diff(self, session_id: str):
        session_id = _identifier(session_id, "ses")
        if self.v2:
            return self._unwrap(self._request(
                "GET", f"/api/session/{session_id}/diff")) or []
        return self._request("GET", f"/session/{session_id}/diff")

    def _optional_list(self, getter):
        """A session may not expose optional pending-state endpoints yet."""
        try:
            return getter()
        except OpenCodeError as error:
            if error.status == 404:
                return []
            raise

    def _diff_or_empty(self, session_id: str):
        """A running session may not have a diff endpoint yet."""
        return self._optional_list(lambda: self.diff(session_id))

    def delete_session(self, session_id: str):
        session_id = _identifier(session_id, "ses")
        if self.v2:
            return self._request("DELETE", f"/api/session/{session_id}")
        return self._request("DELETE", f"/session/{session_id}")

    def pending_permissions(self, session_id: str | None = None):
        if self.v2:
            if session_id:
                path = f"/api/session/{_identifier(session_id, 'ses')}/permission"
            else:
                path = "/api/permission/request"
            result = self._request("GET", path)
            items = result.get("data", []) if isinstance(result, dict) else []
            normalized = []
            for item in items:
                value = dict(item)
                source = value.get("source") or {}
                if source.get("messageID"):
                    value["tool"] = {"messageID": source["messageID"]}
                if value.get("id") and value.get("sessionID"):
                    self._permission_sessions[value["id"]] = value["sessionID"]
                normalized.append(value)
            return normalized
        return self._request("GET", "/permission")

    def reply_permission(self, request_id: str, reply: str, message: str | None = None,
                         session_id: str | None = None):
        if self.v2:
            request_id = _identifier(request_id, "per")
            session_id = session_id or self._permission_sessions.get(request_id)
            if not session_id:
                raise ValueError("V2 permission reply requires a session id")
            body = {"decision": reply}
            if message:
                body["message"] = message
            return self._request(
                "POST",
                f"/api/session/{_identifier(session_id, 'ses')}/permission/{request_id}/reply",
                body)
        if reply not in {"once", "always", "reject"}:
            raise ValueError("reply must be once, always, or reject")
        body = {"reply": reply}
        if message:
            body["message"] = message
        return self._request("POST", f"/permission/{_identifier(request_id, 'per')}/reply", body)

    def pending_questions(self, session_id: str | None = None):
        if not self.v2:
            return self._request("GET", "/question")
        if not session_id:
            return []
        result = self._request(
            "GET", f"/api/session/{_identifier(session_id, 'ses')}/form")
        items = result.get("data", []) if isinstance(result, dict) else []
        normalized = []
        for item in items:
            value = dict(item)
            form_id = value.get("id")
            if form_id:
                self._form_fields[form_id] = list(value.get("fields") or [])
                if value.get("sessionID"):
                    self._form_session_map[form_id] = value["sessionID"]
            # V2 forms do not carry the V1 messageID field. Session matching is
            # handled by execution_state; retain a stable question-shaped view.
            metadata = value.get("metadata") if isinstance(value.get("metadata"), dict) else {}
            value["messageID"] = metadata.get("messageID")
            normalized.append(value)
        return normalized

    def reply_question(self, request_id: str, answers: list[list[str]],
                       session_id: str | None = None, reject: bool = False):
        if not self.v2:
            if not isinstance(answers, list) or not answers or not all(
                    isinstance(answer, list) and answer and all(
                        isinstance(value, str) and value.strip() for value in answer)
                    for answer in answers):
                raise ValueError("answers must contain one or more non-empty text selections")
            return self._request(
                "POST", f"/question/{_identifier(request_id, 'que')}/reply",
                {"answers": answers})
        request_id = _identifier(request_id, "frm")
        session_id = session_id or next(
            (sid for fid, sid in self._form_sessions().items() if fid == request_id), None)
        if not session_id:
            raise ValueError("V2 form reply requires a session id")
        base = f"/api/session/{_identifier(session_id, 'ses')}/form/{request_id}"
        if reject:
            return self._request("DELETE", base)
        fields = self._form_fields.get(request_id, [])
        answer = {}
        for index, field in enumerate(fields):
            key = field.get("key")
            if not isinstance(key, str) or index >= len(answers):
                continue
            values = answers[index]
            answer[key] = values[0] if len(values) == 1 else list(values)
        if not answer and answers:
            answer = {"value": answers[0][0] if len(answers[0]) == 1 else list(answers[0])}
        return self._request("POST", f"{base}/reply", {"answer": answer})

    def reject_question(self, request_id: str, session_id: str | None = None):
        return self.reply_question(
            request_id, [], session_id=session_id, reject=True)

    def reconcile(self, session_id: str, message_limit: int = 20):
        """Read current engine state after connecting or reconnecting.

        Events are not treated as replayable. The caller must also compare an
        Atlas-owned filesystem baseline because engine diff may be incomplete.
        """
        session_id = _identifier(session_id, "ses")
        if self.v2:
            statuses = self.session_statuses()
            session = self.get_session(session_id)
            messages = self.messages(session_id, message_limit)
            if session.get("outcome") in {"failed", "interrupted"} and not any(
                    (item.get("info") or {}).get("role") == "assistant"
                    for item in messages):
                user_id = next((
                    (item.get("info") or {}).get("id") for item in reversed(messages)
                    if (item.get("info") or {}).get("role") == "user"), None)
                messages.append({
                    "info": {
                        "id": f"msg_{session_id[4:]}_atlas_outcome",
                        "role": "assistant",
                        "parentID": user_id,
                        "time": {},
                        "finish": "error",
                        "error": {
                            "name": "MessageAbortedError" if session.get("outcome") == "interrupted"
                            else "ProviderError",
                        },
                    },
                    "parts": [],
                })
            return {
                "session": session,
                "status": statuses.get(session_id, {"type": "idle"}),
                "messages": messages,
                "engine_diff": self._diff_or_empty(session_id),
                "pending_permissions": self._optional_list(
                    lambda: self.pending_permissions(session_id)),
                "pending_questions": self._optional_list(
                    lambda: self.pending_questions(session_id)),
            }
        statuses = self.session_statuses()
        return {
            "session": self.get_session(session_id),
            "status": statuses.get(session_id, {"type": "idle"}),
            "messages": self.messages(session_id, message_limit),
            "engine_diff": self._diff_or_empty(session_id),
            "pending_permissions": [
                item for item in self._optional_list(self.pending_permissions)
                if item.get("sessionID") == session_id
            ],
            "pending_questions": [
                item for item in self._optional_list(self.pending_questions)
                if item.get("sessionID") == session_id
            ],
        }

    def event_stream(self):
        path = "/api/event" if self.v2 else "/event"
        headers = self._headers(scoped=True)
        headers["Accept"] = "text/event-stream"
        request = Request(self._url(path, scoped=False), headers=headers)
        return self._opener(request, timeout=self.timeout)

    def events(self, stream: BinaryIO, session_id: str | None = None) -> Iterator[dict]:
        """Parse SSE JSON events, optionally keeping only one session."""
        wanted = _identifier(session_id, "ses") if session_id else None
        for event in iter_sse(stream):
            properties = event.get("properties") or {}
            event_session = properties.get("sessionID")
            if wanted and event_session not in {None, wanted}:
                continue
            yield event

    def _send_v2_message(self, session_id: str, text: str, provider_id: str,
                         model_id: str, agent: str, system: str | None):
        session_id = _identifier(session_id, "ses")
        self._request("POST", f"/api/session/{session_id}/agent", {"agent": agent})
        self._request("POST", f"/api/session/{session_id}/model", {
            "model": _v2_model_ref(provider_id, model_id),
        })
        body = {"text": text, "delivery": "steer"}
        if system:
            body["metadata"] = {"system": system}
        return self._unwrap(self._request(
            "POST", f"/api/session/{session_id}/prompt", body))

    def _request(self, method: str, path: str, body=None, query=None, scoped=True):
        data = None
        headers = self._headers(scoped=scoped)
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = Request(
            self._url(path, query, scoped), data=data, headers=headers, method=method)
        try:
            with self._opener(request, timeout=self.timeout) as response:
                raw = response.read()
        except HTTPError as error:
            raw = error.read()
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = raw.decode("utf-8", "replace")
            raise OpenCodeError(
                error.code, f"OpenCode HTTP {error.code}", parsed) from error
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as error:
            raise OpenCodeError(
                502, "OpenCode returned a non-JSON response", raw[:200]) from error

    def _headers(self, scoped: bool) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.v2 and self.password:
            token = base64.b64encode(
                f"{self.username}:{self.password}".encode("utf-8")).decode("ascii")
            headers["Authorization"] = f"Basic {token}"
        if self.v2 and scoped:
            headers["x-opencode-directory"] = quote(self.directory, safe="")
        return headers

    def _url(self, path: str, query=None, scoped=True):
        params = dict(query or {})
        if scoped and not self.v2:
            params["directory"] = self.directory
        suffix = "?" + urlencode(params) if params else ""
        return self.base_url + path + suffix

    def _form_sessions(self) -> dict[str, str]:
        return dict(self._form_session_map)

    @staticmethod
    def _unwrap(value):
        if isinstance(value, dict) and "data" in value and len(value) <= 2:
            return value["data"]
        return value


def _v2_model_ref(provider_id: str, model_id: str) -> dict:
    base, separator, variant = model_id.partition("#")
    result = {"providerID": provider_id, "id": base}
    if separator and variant:
        result["variant"] = variant
    return result


def _message_body(text: str, provider_id: str, model_id: str, agent: str,
                  tools: dict | None, system: str | None) -> dict:
    body = {
        "model": {"providerID": provider_id, "modelID": model_id},
        "agent": agent,
        "parts": [{"type": "text", "text": text}],
    }
    if tools is not None:
        body["tools"] = tools
    if system:
        body["system"] = system
    return body


def _identifier(value: str | None, prefix: str) -> str:
    if not value or not value.startswith(prefix + "_") or not value.replace("_", "").isalnum():
        raise ValueError(f"invalid {prefix} identifier")
    return quote(value, safe="")


def iter_sse(stream: BinaryIO) -> Iterator[dict]:
    """Yield JSON data records from a server-sent event byte stream."""
    data_lines: list[str] = []
    for raw in stream:
        line = raw.decode("utf-8", "replace").rstrip("\r\n")
        if not line:
            if data_lines:
                yield json.loads("\n".join(data_lines))
                data_lines.clear()
            continue
        if line.startswith("data:"):
            data_lines.append(line[5:].lstrip())
    if data_lines:
        yield json.loads("\n".join(data_lines))


def _normalize_v2_messages(messages: list[dict]) -> list[dict]:
    normalized = []
    latest_user = None
    for message in messages if isinstance(messages, list) else []:
        if not isinstance(message, dict):
            continue
        message_type = message.get("type")
        message_id = message.get("id")
        if message_type == "user":
            latest_user = message_id
            normalized.append({
                "info": {"id": message_id, "role": "user", "parentID": None},
                "parts": [{"type": "text", "text": message.get("text", "")}],
            })
            continue
        if message_type != "assistant" or not message_id:
            continue
        info = {
            "id": message_id,
            "role": "assistant",
            "parentID": latest_user,
            "time": message.get("time") or {},
            "finish": message.get("finish"),
            "cost": message.get("cost", 0),
            "tokens": message.get("tokens") or {},
        }
        if message.get("error"):
            info["error"] = message["error"]
        parts = []
        for content in message.get("content") or []:
            if not isinstance(content, dict):
                continue
            if content.get("type") == "text":
                parts.append({"type": "text", "text": content.get("text", "")})
            elif content.get("type") == "tool":
                parts.append(_normalize_v2_tool(content))
        normalized.append({"info": info, "parts": parts})
    return normalized


def _normalize_v2_tool(content: dict) -> dict:
    state = dict(content.get("state") or {})
    status = state.get("status", "unknown")
    if status == "completed":
        output = "\n".join(
            item.get("text", "") for item in state.get("content") or []
            if isinstance(item, dict) and item.get("type") == "text")
        state["output"] = output
    if isinstance(state.get("input"), str):
        try:
            state["input"] = json.loads(state["input"])
        except json.JSONDecodeError:
            state["input"] = {"command": state["input"]}
    state.setdefault("status", status)
    name = content.get("name") or "unknown"
    return {
        "type": "tool",
        "id": content.get("id"),
        "tool": "bash" if name in {"shell", "bash"} else name,
        "state": state,
    }
