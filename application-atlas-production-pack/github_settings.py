"""Local, write-only GitHub credential settings. Never included in model inputs."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import tempfile
import threading

from atlas_runtime import PACK

_LOCK = threading.Lock()


def config_path():
    return Path(os.environ.get("ATLAS_GITHUB_CONFIG", PACK / "atlas/github-credentials.json"))


def _saved_token():
    path = config_path()
    if not path.exists():
        return ""
    try:
        return json.loads(path.read_text()).get("token", "")
    except (ValueError, OSError):
        raise ValueError("GitHub 凭据文件不可读，请重新保存") from None


def token():
    return _saved_token() or os.environ.get("ATLAS_GITHUB_TOKEN", "").strip()


def public_view():
    saved = bool(_saved_token())
    return {"configured": saved or bool(os.environ.get("ATLAS_GITHUB_TOKEN", "").strip()),
            "source": "local" if saved else "environment" if os.environ.get("ATLAS_GITHUB_TOKEN", "").strip() else "none"}


def save(body):
    if not isinstance(body, dict) or set(body) - {"token", "remove"}:
        raise ValueError("GitHub 设置请求无效")
    if "remove" in body and (body["remove"] is not True or "token" in body):
        raise ValueError("清除请求无效")
    value = body.get("token", "")
    if not isinstance(value, str) or (value and not re.fullmatch(r"[A-Za-z0-9_.-]{10,512}", value)):
        raise ValueError("Token 格式无效；请勿输入空格或换行")
    with _LOCK:
        path = config_path()
        if body.get("remove"):
            path.unlink(missing_ok=True)
        elif value:
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
                    temporary = Path(stream.name)
                    os.fchmod(stream.fileno(), 0o600)
                    json.dump({"token": value}, stream)
                os.replace(temporary, path)
            finally:
                if temporary and temporary.exists():
                    temporary.unlink()
    return public_view()


def test_connection():
    from oss_catalog import GitHub
    result = GitHub().get("/rate_limit")
    return {"ok": True, **public_view(),
            "limits": {name: {key: result.get("resources", {}).get(name, {}).get(key)
                              for key in ("limit", "remaining", "reset")}
                       for name in ("core", "search")}}
