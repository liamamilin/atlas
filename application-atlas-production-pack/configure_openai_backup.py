#!/usr/bin/env python3
"""Import the root .env into Atlas settings after a bounded Luna probe.

No shell evaluation, key logging, service restart, or catalog job creation.
The existing default stays selected; --apply replaces the single backup slot.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import urllib.error
import urllib.request
from urllib.parse import urlparse

import atlas_model

DEFAULT_ENV = Path(__file__).resolve().parents[1] / ".env"


def read_env(path: Path) -> dict:
    values = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, separator, value = line.removeprefix("export ").partition("=")
        if not separator:
            raise ValueError(f".env 第 {number} 行缺少等号")
        value = value.strip()
        if value[:1] in {"'", '"'}:
            if len(value) < 2 or value[-1] != value[0]:
                raise ValueError(f".env 第 {number} 行引号不匹配")
            value = value[1:-1]
        values[name.strip()] = value
    return values


def settings_request(api: str, route: str, payload: dict | None = None) -> dict:
    request = urllib.request.Request(
        api + "/api/settings/model" + route,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Content-Type": "application/json"},
        method="POST" if payload is not None else "GET",
    )
    # Local settings must never send a credential through a proxy or redirect.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Do not echo a settings response that could contain submitted secrets.
        raise ValueError(f"Atlas 设置接口返回 HTTP {error.code}；路由未确认") from None
    except urllib.error.URLError:
        raise ValueError("无法连接本地 Atlas 设置接口") from None


def configure(values: dict, *, apply: bool = False) -> dict:
    key = values.get("OPENAI_API_KEY", "").strip()
    base_url = values.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = values.get("OPENAI_MODEL", "gpt-6-luna").strip()
    api = values.get("ATLAS_API_URL", "http://127.0.0.1:5199").rstrip("/")
    if not key or key.lower().startswith(("your-", "replace-", "sk-your")):
        raise ValueError("请先在本机 .env 的 OPENAI_API_KEY= 后填写 OpenAI API key")
    if base_url != "https://api.openai.com/v1" or model != "gpt-6-luna":
        raise ValueError("此导入脚本仅配置官方 OpenAI / gpt-6-luna")
    parsed = urlparse(api)
    if (parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}
            or parsed.username or parsed.password or parsed.query or parsed.fragment
            or parsed.path not in {"", "/"}):
        raise ValueError("ATLAS_API_URL 必须为本机 HTTP 服务地址")
    if not apply:
        return {"ready": True, "applied": False, "provider": "openai", "model": model}

    view = settings_request(api, "")
    default = view.get("default") or {}
    primary = default.get("provider")
    if not primary or primary == "openai":
        raise ValueError("需先配置不同于 OpenAI 的主模型；当前主模型未更改")
    if model not in ((view.get("presets") or {}).get("openai") or {}).get("models", []):
        raise ValueError("运行中的 API 尚未加载 Luna 参数适配；请先安排代码重新加载，脚本不会重启服务")

    # Probe before saving credentials or replacing the existing fallback.
    result = atlas_model._chat_openai(
        {"provider": "openai", "model": model, "api_key": key, "base_url": base_url, "style": "openai"},
        [{"role": "user", "content": "Reply exactly OK."}],
        None, 0, 32, None, 30, False,
    )
    if result["content"].strip() != "OK":
        raise ValueError("Luna 回执未通过，原路由保留")
    current = settings_request(api, "")
    if current.get("default") != default:
        raise ValueError("主模型设置发生变化，请重新运行导入")
    existing = next((item for item in current.get("providers", []) if item.get("id") == "openai"), {})
    models = list(dict.fromkeys([model] + existing.get("models", [])))
    settings_request(api, "/providers", {
        "id": "openai", "preset": "openai", "name": "OpenAI",
        "base_url": base_url, "api_key": key, "models": models,
    })
    settings_request(api, "/fallback", {
        "enabled": True, "from_provider": primary, "provider": "openai", "model": model,
    })
    saved = settings_request(api, "")
    fallback = saved.get("fallback") or {}
    if (saved.get("default") != default or fallback.get("provider") != "openai"
            or fallback.get("model") != model or fallback.get("enabled") is not True):
        raise ValueError("保存后的备用路由未通过核对，请检查设置页")
    return {"ready": True, "applied": True, "provider": "openai", "model": model,
            "default": default, "credential_verified": True, "fallback_active": fallback.get("active")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--apply", action="store_true", help="进行一次短模型验证并替换备用路由")
    args = parser.parse_args()
    try:
        result = configure(read_env(args.env), apply=args.apply)
    except (OSError, ValueError, atlas_model.ModelConfigError) as error:
        # Upstream errors may contain request material. Only print known-safe
        # local validation messages or the provider error code.
        message = (f"OpenAI 验证失败：{error.code}" if isinstance(error, atlas_model.ModelConfigError)
                   else "无法读取 .env 文件" if isinstance(error, OSError) else str(error))
        print(json.dumps({"ok": False, "message": message}, ensure_ascii=False))
        return 1
    print(json.dumps({"ok": True, **result}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
