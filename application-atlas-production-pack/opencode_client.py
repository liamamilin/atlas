"""Small OpenCode HTTP adapter for U17.

Atlas owns project/task state. This client only translates calls to one
OpenCode server and deliberately exposes the engine's raw records where Atlas
must reconcile state after a disconnect or process restart.
"""
from __future__ import annotations

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
    """Client for the documented OpenCode server API used by U17."""

    def __init__(self, base_url: str, directory: str, timeout: int = 300,
                 opener=urlopen):
        parsed = urlparse(base_url)
        if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("OpenCode base URL must be a local HTTP endpoint")
        if not directory:
            raise ValueError("directory is required")
        self.base_url = base_url.rstrip("/")
        self.directory = directory
        self.timeout = timeout
        self._opener = opener

    def health(self):
        return self._request("GET", "/global/health", scoped=False)

    def create_session(self, title: str, parent_id: str | None = None):
        body = {"title": title}
        if parent_id:
            body["parentID"] = parent_id
        return self._request("POST", "/session", body)

    def get_session(self, session_id: str):
        return self._request("GET", f"/session/{_identifier(session_id, 'ses')}")

    def session_statuses(self):
        return self._request("GET", "/session/status")

    def messages(self, session_id: str, limit: int | None = None):
        query = {} if limit is None else {"limit": max(0, int(limit))}
        return self._request("GET", f"/session/{_identifier(session_id, 'ses')}/message", query=query)

    def send_message(self, session_id: str, text: str, provider_id: str,
                     model_id: str, agent: str = "build", tools: dict | None = None,
                     system: str | None = None):
        body = _message_body(text, provider_id, model_id, agent, tools, system)
        return self._request("POST", f"/session/{_identifier(session_id, 'ses')}/message", body)

    def send_message_async(self, session_id: str, text: str, provider_id: str,
                           model_id: str, agent: str = "build", tools: dict | None = None,
                           system: str | None = None):
        """Start work without holding the HTTP request open through approvals."""
        body = _message_body(text, provider_id, model_id, agent, tools, system)
        return self._request("POST", f"/session/{_identifier(session_id, 'ses')}/prompt_async", body)

    def abort(self, session_id: str):
        return self._request("POST", f"/session/{_identifier(session_id, 'ses')}/abort", {})

    def diff(self, session_id: str):
        """Return engine-reported diff; an empty list is not proof of no file changes."""
        return self._request("GET", f"/session/{_identifier(session_id, 'ses')}/diff")

    def delete_session(self, session_id: str):
        return self._request("DELETE", f"/session/{_identifier(session_id, 'ses')}")

    def pending_permissions(self):
        return self._request("GET", "/permission")

    def reply_permission(self, request_id: str, reply: str, message: str | None = None):
        if reply not in {"once", "always", "reject"}:
            raise ValueError("reply must be once, always, or reject")
        body = {"reply": reply}
        if message:
            body["message"] = message
        return self._request("POST", f"/permission/{_identifier(request_id, 'per')}/reply", body)

    def reconcile(self, session_id: str, message_limit: int = 20):
        """Read current engine state after connecting or reconnecting.

        Events are not treated as replayable. The caller must also compare an
        Atlas-owned filesystem baseline because engine diff may be incomplete.
        """
        session_id = _identifier(session_id, "ses")
        statuses = self.session_statuses()
        return {
            "session": self.get_session(session_id),
            "status": statuses.get(session_id, {"type": "idle"}),
            "messages": self.messages(session_id, message_limit),
            "engine_diff": self.diff(session_id),
            "pending_permissions": [
                item for item in self.pending_permissions()
                if item.get("sessionID") == session_id
            ],
        }

    def event_stream(self):
        request = Request(self._url("/event"), headers={"Accept": "text/event-stream"})
        return self._opener(request, timeout=self.timeout)

    def events(self, stream: BinaryIO, session_id: str | None = None) -> Iterator[dict]:
        """Parse SSE JSON and optionally keep only events for one session.

        Connection and heartbeat events have no session and are retained so the
        caller can track transport health.
        """
        wanted = _identifier(session_id, "ses") if session_id else None
        for event in iter_sse(stream):
            properties = event.get("properties") or {}
            event_session = properties.get("sessionID")
            if wanted and event_session not in {None, wanted}:
                continue
            yield event

    def _request(self, method: str, path: str, body=None, query=None, scoped=True):
        data = None
        headers = {"Accept": "application/json"}
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = Request(self._url(path, query, scoped), data=data, headers=headers, method=method)
        try:
            with self._opener(request, timeout=self.timeout) as response:
                raw = response.read()
        except HTTPError as error:
            raw = error.read()
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = raw.decode("utf-8", "replace")
            raise OpenCodeError(error.code, f"OpenCode HTTP {error.code}", parsed) from error
        return json.loads(raw) if raw else None

    def _url(self, path: str, query=None, scoped=True):
        params = dict(query or {})
        if scoped:
            params["directory"] = self.directory
        suffix = "?" + urlencode(params) if params else ""
        return self.base_url + path + suffix


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


def _identifier(value: str | None, prefix: str) -> str:
    if not value or not value.startswith(prefix + "_") or not value.replace("_", "").isalnum():
        raise ValueError(f"invalid {prefix} identifier")
    return quote(value, safe="")


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
