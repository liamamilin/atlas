"""Best-effort redaction for locally persisted execution and export evidence."""
from __future__ import annotations

import re
from typing import Any

REDACTED = "[REDACTED]"
_SENSITIVE_KEYS = {
    "apikey", "accesstoken", "refreshtoken", "idtoken", "authorization",
    "clientsecret", "credential", "credentials", "cookie", "password",
    "privatekey", "secret", "token",
}
_TEXT_RULES = (
    (
        re.compile(r"(?i)\b(authorization\s*[:=]\s*)(?:bearer\s+)?[^\s,;]+"),
        rf"\1{REDACTED}",
    ),
    (re.compile(r"(?i)\b(bearer)\s+[A-Za-z0-9._~+/=-]{8,}"), rf"\1 {REDACTED}"),
    (
        re.compile(
            r"(?i)\b((?:api[_-]?key|access[_-]?token|refresh[_-]?token|secret|password)"
            r"\s*[:=]\s*[\"']?)[^\s,\"';]+"),
        rf"\1{REDACTED}",
    ),
    (re.compile(r"(?i)\b(sk-[A-Za-z0-9_-]{8,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16})\b"), REDACTED),
    (re.compile(r"(?i)\b(eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,})\b"), REDACTED),
    (re.compile(r"(?i)(://[^/\s:@]+:)[^/\s:@]+(@)"), rf"\1{REDACTED}\2"),
)


def _sensitive_key(key: Any) -> bool:
    if not isinstance(key, str):
        return False
    normalized = re.sub(r"[^a-z0-9]", "", key.lower())
    return normalized in _SENSITIVE_KEYS or normalized.endswith((
        "apikey", "accesstoken", "refreshtoken", "clientsecret", "password"))


def redact_text(value: str) -> str:
    redacted = value
    for pattern, replacement in _TEXT_RULES:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def redact_value(value: Any, *, key: Any = None) -> Any:
    if _sensitive_key(key) and value not in (None, "", [], {}):
        return REDACTED
    if isinstance(value, dict):
        return {item_key: redact_value(item, key=item_key) for item_key, item in value.items()}
    if isinstance(value, list):
        return [redact_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_value(item) for item in value)
    if isinstance(value, str):
        return redact_text(value)
    return value
