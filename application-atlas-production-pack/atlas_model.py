#!/usr/bin/env python3
"""Provider-agnostic model access for Atlas.

One place that owns: which model providers Atlas can talk to, where their
credentials live, and how a chat or embedding call is shaped.

Credentials are write-only over the API. ``public_view()`` masks every key and
the raw value never leaves this process. The config file is stored mode 0600.

Resolution order for a call:

1. explicit arguments
2. the saved default in the config file
3. ``ATLAS_MODEL_PROVIDER`` / ``ATLAS_MODEL`` / ``ATLAS_API_KEY``
4. the local OpenCode credential store (``~/.local/share/opencode/auth.json``)

Every provider here is OpenAI-compatible except Anthropic, which gets a small
translation layer. That keeps the surface to one request shape for the common
case while still allowing a native provider later.
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from atlas_runtime import PACK, atomic_write
from privacy import redact_text

CONFIG_ENV = "ATLAS_MODEL_CONFIG"
CONFIG_PATH = Path(PACK) / "atlas" / "model-config.json"
MASK = "\u2022\u2022\u2022\u2022"
DEFAULT_TIMEOUT = 300
PROBE_TIMEOUT = 25

# Common providers. Selecting a preset fills base_url and style; the user only
# supplies a credential. `open-design`, `opencode-go`, `opencode` and
# `commandcode` mirror the providers already configured in this machine's
# OpenCode, so a credential import lands on the same endpoints.
PRESETS: dict[str, dict] = {
    "open-design": {
        "name": "Open Design", "style": "openai",
        "base_url": "https://amr-link.open-design.ai/v1",
        "models": ["deepseek-v4.1-flash", "deepseek-v4-pro", "deepseek-v4-flash",
                   "glm-5.3-flash", "glm-5.3-flashx", "kimi-k2.7-code",
                   "mimo-v2.6-flash", "mimo-v2.6-pro", "gpt-6-luna",
                   "claude-haiku-5.5"],
    },
    "opencode-go": {
        "name": "OpenCode Go", "style": "openai",
        "base_url": "https://opencode.ai/zen/go/v1",
        "models": ["qwen3.8-flash", "mimo-v2.5", "deepseek-v4-flash"],
    },
    "opencode": {
        "name": "OpenCode Zen", "style": "openai",
        "base_url": "https://opencode.ai/zen/v1", "models": [],
    },
    "commandcode": {
        "name": "Command Code (GOAT)", "style": "openai",
        "base_url": "https://api.commandcode.ai/provider/v1", "models": [],
    },
    "openai": {
        "name": "OpenAI", "style": "openai",
        "base_url": "https://api.openai.com/v1",
        "models": ["gpt-5.6-sol", "gpt-5.6-luna"],
    },
    "anthropic": {
        "name": "Anthropic", "style": "anthropic",
        "base_url": "https://api.anthropic.com/v1",
        "models": ["claude-haiku-5.5"],
    },
    "google": {
        "name": "Google Gemini", "style": "openai",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "models": ["gemini-3.8-flash"],
    },
    "deepseek": {
        "name": "DeepSeek", "style": "openai",
        "base_url": "https://api.deepseek.com/v1", "models": [],
    },
    "moonshot": {
        "name": "Moonshot / Kimi", "style": "openai",
        "base_url": "https://api.moonshot.cn/v1", "models": [],
    },
    "zhipu": {
        "name": "Zhipu GLM", "style": "openai",
        "base_url": "https://open.bigmodel.cn/api/paas/v4", "models": [],
    },
    "dashscope": {
        "name": "Alibaba DashScope", "style": "openai",
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "models": ["qwen3.7-max"],
    },
    "siliconflow": {
        "name": "SiliconFlow", "style": "openai",
        "base_url": "https://api.siliconflow.cn/v1", "models": [],
    },
    "openrouter": {
        "name": "OpenRouter", "style": "openai",
        "base_url": "https://openrouter.ai/api/v1", "models": [],
    },
    "groq": {
        "name": "Groq", "style": "openai",
        "base_url": "https://api.groq.com/openai/v1", "models": [],
    },
    "xai": {
        "name": "xAI", "style": "openai",
        "base_url": "https://api.x.ai/v1", "models": [],
    },
    "mistral": {
        "name": "Mistral", "style": "openai",
        "base_url": "https://api.mistral.ai/v1", "models": [],
    },
    "ollama": {
        "name": "Ollama (local)", "style": "openai",
        "base_url": "http://localhost:11434/v1",
        "models": ["qwen3.8:27b-mlx", "qwen3.5:9b-mlx"],
    },
    "lmstudio": {
        "name": "LM Studio (local)", "style": "openai",
        "base_url": "http://localhost:1234/v1", "models": [],
    },
}

# Map an OpenCode auth.json entry to the preset it corresponds to, so the
# import action stores a usable base_url instead of a bare key.
OPENCODE_AUTH_PROVIDERS = {
    "open-design": "open-design",
    "opencode-go": "opencode-go",
    "opencode": "opencode",
    "commandcode": "commandcode",
    "openai": "openai",
    "anthropic": "anthropic",
    "google": "google",
    "deepseek": "deepseek",
    "moonshotai": "moonshot",
    "zhipuai": "zhipu",
    "openrouter": "openrouter",
    "groq": "groq",
    "xai": "xai",
    "mistral": "mistral",
}

DEFAULT_EMBEDDING = {
    "provider": "ollama",
    "base_url": "http://localhost:11434/v1",
    "model": "bge-m3",
}

# Per-task model preference. A role names a model on the default provider so
# that classification, dedupe, translation and identity generation can each be
# tuned without changing the provider. An unset role uses the default model.
ROLE_ENV = {
    "adjudicator": "ATLAS_ADJUDICATOR",
    "dedupe": "ATLAS_DEDUP_MODEL",
    "translate": "ATLAS_TRANSLATE_MODEL",
    "identity": "ATLAS_IDENTITY_MODEL",
}
ROLES = tuple(ROLE_ENV)

PROVIDER_ID = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
DELETE_CONFIRMATION = "delete_model_provider"


class ModelConfigError(RuntimeError):
    """A provider configuration or provider call failed."""

    def __init__(self, message: str, code: str = "invalid_request", status: int = 400):
        super().__init__(message)
        self.code = code
        self.status = status


def _empty_config() -> dict:
    return {
        "version": 1,
        "providers": {},
        "default": {"provider": None, "model": None},
        "roles": {},
        "embedding": dict(DEFAULT_EMBEDDING),
    }


def config_path() -> Path:
    override = os.environ.get(CONFIG_ENV, "").strip()
    return Path(override).expanduser() if override else CONFIG_PATH


def load_config() -> dict:
    """Read the saved config, tolerating a missing or unreadable file."""
    path = config_path()
    if not path.is_file():
        return _empty_config()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return _empty_config()
    if not isinstance(raw, dict):
        return _empty_config()
    config = _empty_config()
    providers = raw.get("providers")
    if isinstance(providers, dict):
        for key, value in providers.items():
            if isinstance(value, dict) and PROVIDER_ID.match(str(key)):
                config["providers"][key] = {
                    "preset": str(value.get("preset") or ""),
                    "name": str(value.get("name") or key),
                    "style": _style(value.get("style")),
                    "base_url": str(value.get("base_url") or ""),
                    "api_key": str(value.get("api_key") or ""),
                    "models": _models(value.get("models")),
                    "updated_at": str(value.get("updated_at") or ""),
                }
    default = raw.get("default")
    if isinstance(default, dict):
        provider = default.get("provider")
        model = default.get("model")
        config["default"] = {
            "provider": str(provider) if provider else None,
            "model": str(model) if model else None,
        }
    embedding = raw.get("embedding")
    if isinstance(embedding, dict):
        config["embedding"] = {
            "provider": str(embedding.get("provider") or DEFAULT_EMBEDDING["provider"]),
            "base_url": str(embedding.get("base_url") or DEFAULT_EMBEDDING["base_url"]),
            "model": str(embedding.get("model") or DEFAULT_EMBEDDING["model"]),
        }
    roles = raw.get("roles")
    if isinstance(roles, dict):
        config["roles"] = {
            role: str(roles[role]).strip()
            for role in ROLES
            if isinstance(roles.get(role), str) and roles[role].strip()
        }
    return config


def save_config(config: dict) -> None:
    path = config_path()
    atomic_write(path, json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def _style(value) -> str:
    return "anthropic" if str(value or "").strip().lower() == "anthropic" else "openai"


def _models(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        value = [part for part in re.split(r"[,\n]", value)]
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        text = str(item).strip()
        if text and text not in out:
            out.append(text)
    return out[:500]


def mask_key(key: str) -> str:
    key = (key or "").strip()
    if not key:
        return ""
    if len(key) <= 10:
        return MASK
    return f"{key[:6]}{MASK}{key[-4:]}"


def _validate_base_url(value: str) -> str:
    value = (value or "").strip().rstrip("/")
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ModelConfigError("base_url must be an absolute http(s) URL")
    return value


def public_provider(provider_id: str, item: dict) -> dict:
    """A provider view safe to return over HTTP: the key is never included."""
    return {
        "id": provider_id,
        "name": item.get("name") or provider_id,
        "preset": item.get("preset") or "",
        "style": item.get("style") or "openai",
        "base_url": item.get("base_url") or "",
        "models": list(item.get("models") or []),
        "has_key": bool((item.get("api_key") or "").strip()),
        "key_masked": mask_key(item.get("api_key") or ""),
        "updated_at": item.get("updated_at") or "",
    }


def public_view() -> dict:
    config = load_config()
    providers = [
        public_provider(provider_id, item)
        for provider_id, item in sorted(config["providers"].items())
    ]
    return {
        "providers": providers,
        "default": dict(config["default"]),
        "embedding": dict(config["embedding"]),
        "presets": {
            key: {
                "name": value["name"],
                "style": value["style"],
                "base_url": value["base_url"],
                "models": list(value.get("models") or []),
            }
            for key, value in PRESETS.items()
        },
        "resolved": resolved_view(),
        "embeddings": [
            {"id": "ollama", "name": "Ollama (local)", "base_url": "http://localhost:11434/v1", "model": "bge-m3"},
        ],
    }


def resolved_view() -> dict:
    """What an unqualified call would use right now, and where it came from."""
    try:
        resolved = resolve()
    except ModelConfigError as error:
        return {"configured": False, "reason": str(error)}
    return {
        "configured": True,
        "provider": resolved["provider"],
        "provider_name": resolved["provider_name"],
        "model": resolved["model"],
        "source": resolved["source"],
        "base_url": resolved["base_url"],
    }


def upsert_provider(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise ModelConfigError("provider payload must be an object")
    config = load_config()
    preset_id = str(payload.get("preset") or "").strip()
    preset = PRESETS.get(preset_id, {})

    provider_id = str(payload.get("id") or preset_id or "").strip().lower()
    if not provider_id:
        derived = payload.get("name") or preset.get("name") or ""
        provider_id = re.sub(r"[^a-z0-9]+", "-", str(derived).lower()).strip("-")
    if not PROVIDER_ID.match(provider_id):
        raise ModelConfigError(
            "provider id must be lowercase letters, digits and dashes")

    existing = config["providers"].get(provider_id) or {}
    base_url = str(payload.get("base_url") or preset.get("base_url")
                   or existing.get("base_url") or "").strip()
    name = str(payload.get("name") or preset.get("name")
               or existing.get("name") or provider_id).strip()
    style = _style(payload.get("style") or preset.get("style")
                   or existing.get("style"))

    # Empty means "keep the stored one, else the preset's" for the id/name
    # fields, but a provider without an endpoint cannot be called at all, so a
    # base URL is always required once preset and stored values are considered.
    if not base_url:
        raise ModelConfigError("base_url is required")

    # A blank api_key means "keep the stored one"; an explicit null clears it.
    if "api_key" in payload and payload["api_key"] is None:
        api_key = ""
    elif str(payload.get("api_key") or "").strip():
        api_key = str(payload["api_key"]).strip()
    else:
        api_key = str(existing.get("api_key") or "").strip()

    models = _models(payload.get("models"))
    if not models:
        models = _models(existing.get("models")) or _models(preset.get("models"))

    config["providers"][provider_id] = {
        "preset": preset_id or str(existing.get("preset") or ""),
        "name": name[:200],
        "style": style,
        "base_url": _validate_base_url(base_url),
        "api_key": api_key,
        "models": models,
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    default = config["default"]
    if not default.get("provider"):
        default["provider"] = provider_id
        default["model"] = models[0] if models else None
    save_config(config)
    return public_provider(provider_id, config["providers"][provider_id])


def delete_provider(provider_id: str, confirm: str) -> dict:
    if confirm != DELETE_CONFIRMATION:
        raise ModelConfigError("explicit provider deletion confirmation is required")
    config = load_config()
    if provider_id not in config["providers"]:
        raise ModelConfigError("provider not found", code="not_found", status=404)
    del config["providers"][provider_id]
    if config["default"].get("provider") == provider_id:
        config["default"] = {"provider": None, "model": None}
    save_config(config)
    return {"id": provider_id, "deleted": True}


def set_default(provider: str, model: str | None) -> dict:
    config = load_config()
    provider = str(provider or "").strip()
    if not provider:
        config["default"] = {"provider": None, "model": None}
        save_config(config)
        return dict(config["default"])
    if provider not in config["providers"]:
        raise ModelConfigError("provider not found", code="not_found", status=404)
    model = str(model or "").strip()
    if model and model not in (config["providers"][provider].get("models") or []):
        # Allow a model the provider knows but we have not listed yet.
        config["providers"][provider]["models"] = _models(
            [model] + list(config["providers"][provider].get("models") or []))
    config["default"] = {"provider": provider, "model": model or None}
    save_config(config)
    return dict(config["default"])


def set_embedding(payload: dict) -> dict:
    config = load_config()
    current = dict(config["embedding"])
    if "base_url" in payload:
        current["base_url"] = _validate_base_url(str(payload.get("base_url") or ""))
    if "model" in payload:
        current["model"] = str(payload.get("model") or DEFAULT_EMBEDDING["model"]).strip()
    if "provider" in payload:
        current["provider"] = str(payload.get("provider") or "").strip()
    config["embedding"] = current
    save_config(config)
    return dict(current)


def _opencode_auth() -> dict:
    """Credentials from OpenCode's JSON store.

    Kept for callers that only need the file. ``_opencode_credentials`` merges
    this with the newer SQLite store, which is where recently added providers
    (for example Open Design) live.
    """
    path = Path.home() / ".local/share/opencode/auth.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return value if isinstance(value, dict) else {}


def _opencode_credentials() -> dict:
    """All OpenCode credentials, merging the JSON file and the SQLite store.

    OpenCode moved provider credentials into ``opencode.db``; a provider added
    through the OpenCode UI appears only there, so reading just ``auth.json``
    silently misses it. Later sources win, but each entry keeps its own key.
    """
    credentials: dict[str, dict] = {}

    file_store = _opencode_auth()
    for provider_id, entry in file_store.items():
        if isinstance(entry, dict):
            credentials[provider_id] = entry

    db_path = Path.home() / ".local/share/opencode/opencode.db"
    if db_path.is_file():
        try:
            # Read-only: never create or migrate the user's OpenCode database.
            uri = f"file:{db_path}?mode=ro"
            with sqlite3.connect(uri, uri=True, timeout=2) as connection:
                rows = connection.execute(
                    "SELECT integration_id, value FROM credential").fetchall()
        except sqlite3.Error:
            rows = []
        for integration_id, value in rows:
            if not isinstance(value, str) or not integration_id:
                continue
            try:
                parsed = json.loads(value)
            except ValueError:
                continue
            if isinstance(parsed, dict):
                credentials.setdefault(str(integration_id), parsed)

    return credentials


def _credential_key(entry: dict) -> str:
    if not isinstance(entry, dict):
        return ""
    for field in ("key", "access", "api_key", "token"):
        value = entry.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def import_from_opencode() -> dict:
    """Store a credential for every OpenCode provider that has a known preset."""
    stored = _opencode_credentials()
    config = load_config()
    imported: list[str] = []
    for auth_id, preset_id in OPENCODE_AUTH_PROVIDERS.items():
        key = _credential_key(stored.get(auth_id) or {})
        if not key:
            continue
        preset = PRESETS[preset_id]
        existing = config["providers"].get(preset_id) or {}
        config["providers"][preset_id] = {
            "preset": preset_id,
            "name": existing.get("name") or preset["name"],
            "style": existing.get("style") or preset["style"],
            "base_url": existing.get("base_url") or preset["base_url"],
            "api_key": key,
            "models": existing.get("models") or _models(preset.get("models")),
            "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        imported.append(preset_id)
    if imported:
        default = config["default"]
        if not default.get("provider"):
            first = imported[0]
            models = config["providers"][first].get("models") or []
            default["provider"] = first
            default["model"] = models[0] if models else None
        save_config(config)
    return {"imported": imported, "count": len(imported)}


# --------------------------------------------------------------------------
# Calls
# --------------------------------------------------------------------------

def role_model(role: str, config: dict | None = None) -> str:
    """The model a named task should use, or "" to fall back to the default.

    Precedence: environment override, then the saved role mapping, then "".
    A role is a hint; an unset role simply uses the default model, so a fresh
    install works without configuring every task separately.
    """
    env = ROLE_ENV.get(role)
    if env:
        value = os.environ.get(env, "").strip()
        if value:
            return value
    config = config or load_config()
    return str((config.get("roles") or {}).get(role) or "").strip()


def resolve(provider: str | None = None, model: str | None = None,
            role: str | None = None) -> dict:
    """Return the provider, model, key and endpoint a call should use."""
    config = load_config()
    providers = config["providers"]
    source = "config"
    provider_id = str(provider or "").strip()
    if not provider_id:
        provider_id = str(config["default"].get("provider") or "").strip()
    if not provider_id:
        provider_id = os.environ.get("ATLAS_MODEL_PROVIDER", "").strip()
        source = "environment"
    auth_item = None
    if not provider_id:
        stored = _opencode_credentials()
        auth_id = next(
            (key for key in OPENCODE_AUTH_PROVIDERS
             if _credential_key(stored.get(key) or {})), "")
        if auth_id:
            provider_id = OPENCODE_AUTH_PROVIDERS[auth_id]
            key = _credential_key(stored.get(auth_id) or {})
            preset = PRESETS.get(provider_id, {})
            auth_item = {
                "preset": provider_id,
                "name": preset.get("name") or provider_id,
                "style": preset.get("style") or "openai",
                "base_url": preset.get("base_url") or "",
                "api_key": key,
                "models": _models(preset.get("models")),
            }
            source = "opencode"
    if not provider_id:
        raise ModelConfigError(
            "no model provider is configured yet",
            code="not_configured", status=400)

    item = providers.get(provider_id)
    if item is None:
        # Fall back to the OpenCode credential store, then to a bare preset so
        # ATLAS_MODEL_PROVIDER=deepseek works with an environment credential.
        env_key = os.environ.get("ATLAS_API_KEY", "").strip()
        if auth_item and auth_item.get("api_key"):
            item = auth_item
        elif env_key:
            preset = PRESETS.get(provider_id)
            if preset:
                item = {"preset": provider_id, "name": preset["name"],
                        "style": preset["style"], "base_url": preset["base_url"],
                        "api_key": env_key, "models": _models(preset.get("models"))}
                source = "environment"
    if item is None:
        raise ModelConfigError(
            f"provider {provider_id!r} is not configured",
            code="not_configured", status=400)

    api_key = (item.get("api_key") or "").strip() or os.environ.get("ATLAS_API_KEY", "").strip()
    if not api_key:
        raise ModelConfigError(
            f"provider {provider_id!r} has no credential",
            code="no_credential", status=400)

    available = _models(item.get("models"))
    role_choice = role_model(role, config) if role else ""

    # Precedence: an explicit model, then the role's model, then the saved
    # default, then ATLAS_MODEL, then the provider's first known model.
    #
    # A role is only a hint: a provider-specific role name cannot be trusted
    # across providers, so a role that names a model the provider does not
    # advertise is ignored rather than sent and rejected. An empty model list
    # means the provider does not advertise any, so the role is honored.
    if role_choice and available and role_choice not in available:
        role_choice = ""

    chosen_model = (str(model or "").strip()
                    or role_choice
                    or str(config["default"].get("model") or "").strip())
    if not chosen_model:
        chosen_model = os.environ.get("ATLAS_MODEL", "").strip()
    if not chosen_model:
        chosen_model = available[0] if available else ""
    if not chosen_model:
        raise ModelConfigError(
            f"provider {provider_id!r} has no model selected",
            code="no_model", status=400)

    return {
        "provider": provider_id,
        "provider_name": item.get("name") or provider_id,
        "model": chosen_model,
        "base_url": (item.get("base_url") or "").rstrip("/"),
        "api_key": api_key,
        "style": item.get("style") or "openai",
        "source": source,
    }


def _headers(resolved: dict) -> dict:
    headers = {"Accept": "application/json", "Content-Type": "application/json",
               "User-Agent": "atlas-model/1.0"}
    if resolved["style"] == "anthropic":
        headers["x-api-key"] = resolved["api_key"]
        headers["anthropic-version"] = "2023-06-01"
    else:
        headers["Authorization"] = f"Bearer {resolved['api_key']}"
    return headers


def _post_json(url: str, payload: dict, headers: dict, timeout: int) -> dict:
    request = urllib.request.Request(
        url, json.dumps(payload).encode("utf-8"), headers, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def _get_json(url: str, headers: dict, timeout: int) -> dict:
    request = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def _provider_error(error: BaseException) -> ModelConfigError:
    """Turn a transport error into a safe, actionable message."""
    if isinstance(error, urllib.error.HTTPError):
        try:
            detail = error.read(4096).decode("utf-8", "replace")[:400]
        except Exception:
            detail = ""
        detail = redact_text(detail)
        lowered = detail.lower()
        if error.code in {401, 403}:
            return ModelConfigError(
                f"provider rejected the credential (HTTP {error.code})",
                code="unauthorized", status=400)
        if error.code == 404:
            return ModelConfigError(
                "provider endpoint not found (HTTP 404); check the base URL",
                code="bad_endpoint", status=400)
        if error.code == 429:
            return ModelConfigError(
                "provider rate limit reached (HTTP 429)", code="rate_limited",
                status=429)
        # A named model that the provider does not serve is a configuration
        # problem, not a transient one, so it must not be retried.
        if "model" in lowered and "unavailable" in lowered:
            return ModelConfigError(
                "the selected model is unavailable on this provider",
                code="model_unavailable", status=400)
        return ModelConfigError(
            f"provider returned HTTP {error.code}: {detail}",
            code="provider_error", status=502)
    if isinstance(error, urllib.error.URLError):
        return ModelConfigError(
            f"could not reach the provider: {redact_text(str(error.reason))}",
            code="unreachable", status=502)
    if isinstance(error, TimeoutError):
        return ModelConfigError("provider timed out", code="timeout", status=504)
    if isinstance(error, (KeyError, IndexError, TypeError, ValueError)):
        return ModelConfigError(
            f"provider response shape is invalid: {redact_text(str(error))}",
            code="invalid_response", status=502)
    return ModelConfigError(redact_text(str(error)), code="provider_error", status=502)


def list_models(provider_id: str) -> list[str]:
    config = load_config()
    item = config["providers"].get(provider_id)
    if item is None:
        preset = PRESETS.get(provider_id)
        if preset is None:
            raise ModelConfigError("provider not found", code="not_found", status=404)
        item = {"base_url": preset["base_url"], "style": preset["style"],
                "api_key": os.environ.get("ATLAS_API_KEY", "").strip(),
                "name": preset["name"], "models": _models(preset.get("models"))}
    api_key = (item.get("api_key") or "").strip()
    base_url = (item.get("base_url") or "").rstrip("/")
    if not base_url:
        raise ModelConfigError("provider has no base URL")
    if not api_key:
        raise ModelConfigError("provider has no credential", code="no_credential")
    resolved = {"api_key": api_key, "style": _style(item.get("style"))}
    try:
        body = _get_json(f"{base_url}/models", _headers(resolved), PROBE_TIMEOUT)
    except BaseException as error:
        raise _provider_error(error) from error
    data = body.get("data") if isinstance(body, dict) else None
    ids: list[str] = []
    for entry in data or []:
        if isinstance(entry, dict) and entry.get("id"):
            ids.append(str(entry["id"]))
    return ids[:500]


def test_provider(provider_id: str) -> dict:
    """Probe a provider without spending a completion: list its models."""
    started = time.monotonic()
    result = {"id": provider_id, "ok": False, "models": [], "model_count": 0,
              "error": None, "code": None, "latency_ms": 0}
    try:
        models = list_models(provider_id)
    except ModelConfigError as error:
        result["error"] = str(error)
        result["code"] = error.code
        result["latency_ms"] = int((time.monotonic() - started) * 1000)
        return result
    except BaseException as error:  # pragma: no cover - defensive
        result["error"] = redact_text(str(error))
        result["code"] = "provider_error"
        result["latency_ms"] = int((time.monotonic() - started) * 1000)
        return result
    result.update({"ok": True, "models": models, "model_count": len(models)})
    result["latency_ms"] = int((time.monotonic() - started) * 1000)
    if models:
        config = load_config()
        item = config["providers"].get(provider_id)
        if item is not None and not item.get("models"):
            item["models"] = models[:200]
            save_config(config)
    return result


def chat(messages: list[dict], *, model: str | None = None,
         provider: str | None = None, role: str | None = None,
         tools: list[dict] | None = None,
         temperature: float | None = None, max_tokens: int | None = None,
         system: str | None = None, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """Send a chat completion and normalize the response.

    Returns ``{"content", "tool_calls", "usage", "raw"}``. ``usage`` values are
    reported as the provider gave them; unknown numbers stay ``None``.

    ``role`` selects a task-specific model ("adjudicator", "dedupe",
    "translate", "identity") when one is configured for the default provider.
    """
    resolved = resolve(provider=provider, model=model, role=role)
    if resolved["style"] == "anthropic":
        return _chat_anthropic(
            resolved, messages, tools, temperature, max_tokens, system, timeout)
    return _chat_openai(
        resolved, messages, tools, temperature, max_tokens, system, timeout)


def _chat_openai(resolved, messages, tools, temperature, max_tokens, system,
                 timeout) -> dict:
    body: dict = {"model": resolved["model"], "messages": list(messages)}
    if system:
        body["messages"] = [{"role": "system", "content": system}] + body["messages"]
    if tools:
        body["tools"] = tools
        body["tool_choice"] = "auto"
    if temperature is not None:
        body["temperature"] = temperature
    if max_tokens is not None:
        body["max_tokens"] = max_tokens
    url = f"{resolved['base_url']}/chat/completions"
    try:
        raw = _post_json(url, body, _headers(resolved), timeout)
    except BaseException as error:
        raise _provider_error(error) from error
    choice = (raw.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    usage = raw.get("usage") or {}
    return {
        "content": message.get("content") or "",
        "tool_calls": message.get("tool_calls") or [],
        "finish_reason": choice.get("finish_reason"),
        "usage": {
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
            "cost": None,
        },
        "model": raw.get("model") or resolved["model"],
        "provider": resolved["provider"],
        "raw": raw,
    }


def _chat_anthropic(resolved, messages, tools, temperature, max_tokens, system,
                    timeout) -> dict:
    body: dict = {"model": resolved["model"],
                  "max_tokens": max_tokens or 4096,
                  "messages": [m for m in messages if m.get("role") != "system"]}
    if system:
        body["system"] = system
    elif any(m.get("role") == "system" for m in messages):
        body["system"] = "\n\n".join(
            str(m.get("content") or "") for m in messages if m.get("role") == "system")
    if tools:
        body["tools"] = [
            {"name": tool["function"]["name"],
             "description": tool["function"].get("description", ""),
             "input_schema": tool["function"].get("parameters") or {"type": "object"}}
            for tool in tools if isinstance(tool, dict) and tool.get("function")
        ]
    if temperature is not None:
        body["temperature"] = temperature
    url = f"{resolved['base_url']}/messages"
    try:
        raw = _post_json(url, body, _headers(resolved), timeout)
    except BaseException as error:
        raise _provider_error(error) from error
    content = ""
    tool_calls = []
    for block in raw.get("content") or []:
        if not isinstance(block, dict):
            continue
        if block.get("type") == "text":
            content += block.get("text") or ""
        elif block.get("type") == "tool_use":
            tool_calls.append({
                "id": block.get("id"),
                "type": "function",
                "function": {"name": block.get("name"),
                             "arguments": json.dumps(block.get("input") or {})},
            })
    usage = raw.get("usage") or {}
    prompt_tokens = usage.get("input_tokens")
    completion_tokens = usage.get("output_tokens")
    total = (prompt_tokens + completion_tokens
             if isinstance(prompt_tokens, int) and isinstance(completion_tokens, int)
             else None)
    return {
        "content": content,
        "tool_calls": tool_calls,
        "finish_reason": raw.get("stop_reason"),
        "usage": {"prompt_tokens": prompt_tokens,
                  "completion_tokens": completion_tokens,
                  "total_tokens": total, "cost": None},
        "model": raw.get("model") or resolved["model"],
        "provider": resolved["provider"],
        "raw": raw,
    }


def complete(messages: list[dict], *, role: str | None = None,
             model: str | None = None, provider: str | None = None,
             temperature: float | None = None,
             max_tokens: int | None = None,
             timeout: int = DEFAULT_TIMEOUT,
             strip_fence: bool = False) -> dict:
    """Chat and return the text body plus the model that actually served it.

    Every Atlas caller previously repeated "use content, else fall back to
    reasoning, and optionally strip a Markdown fence". Some reasoning models
    put the whole answer in ``reasoning`` with an empty ``content``, so the
    fallback is load-bearing rather than cosmetic.
    """
    result = chat(messages, role=role, model=model, provider=provider,
                  temperature=temperature, max_tokens=max_tokens, timeout=timeout)
    text = (result.get("content") or "").strip()
    if not text:
        raw = result.get("raw") or {}
        choice = (raw.get("choices") or [{}])[0]
        message = choice.get("message") or {}
        text = str(message.get("reasoning") or "").strip()
    if strip_fence:
        text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
    return {"text": text, "model": result.get("model") or "",
            "provider": result.get("provider") or "",
            "usage": result.get("usage") or {}}


def complete_text(messages: list[dict], **kwargs) -> str:
    """Chat and return only the text body."""
    return complete(messages, **kwargs)["text"]


def embed(texts: list[str], *, model: str | None = None,
          timeout: int = 300) -> list[list[float]]:
    """Embed texts through the configured embedding endpoint."""
    config = load_config()
    embedding = config["embedding"]
    base_url = (embedding.get("base_url") or DEFAULT_EMBEDDING["base_url"]).rstrip("/")
    name = model or embedding.get("model") or DEFAULT_EMBEDDING["model"]
    provider = embedding.get("provider") or ""
    api_key = ""
    item = config["providers"].get(provider)
    if item:
        api_key = (item.get("api_key") or "").strip()
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    body = {"model": name, "input": list(texts)}
    try:
        raw = _post_json(f"{base_url}/embeddings", body, headers, timeout)
    except BaseException as error:
        raise _provider_error(error) from error
    data = raw.get("data") or []
    data = sorted(data, key=lambda entry: entry.get("index", 0))
    return [list(entry.get("embedding") or []) for entry in data]
