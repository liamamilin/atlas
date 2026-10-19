"""Declarative template protocol, immutable artifacts and deterministic copies."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import zipfile
from urllib.parse import urlsplit

from atlas_runtime import atomic_json
from .store import FactoryError, digest

PROFILES = {"static-web", "python-web", "node-web", "cli"}
# Match the executables supplied by Atlas's images, not the host environment.
PROFILE_EXECUTABLES = {
    profile: (
        {"node", "npm", "npx"}
        if profile == "node-web"
        else {"python", "python3", "pip", "pip3"}
    )
    for profile in PROFILES
}
IGNORED = {
    ".git",
    ".opencode",
    "node_modules",
    ".venv",
    "__pycache__",
    "dist",
    ".pytest_cache",
}
MAX_FILES = 12000
MAX_TOTAL = 128 * 1024 * 1024


def relative(value):
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise FactoryError("invalid artifact path")
    path = PurePosixPath(value)
    if (
        path.is_absolute()
        or any(p in {"..", ".", ""} for p in path.parts)
        or str(path) != value
    ):
        raise FactoryError("artifact paths must stay inside the project")
    if any(p in IGNORED for p in path.parts):
        raise FactoryError("artifact path contains an internal or dependency directory")
    if path.name in {"AGENTS.md", "CLAUDE.md", "opencode.json", "opencode.jsonc"}:
        raise FactoryError("repository agent configuration is not part of a template")
    if (
        path.name.startswith(".env")
        and path.name not in {".env.example", ".env.sample", ".env.template"}
    ) or path.suffix.lower() in {".pem", ".key", ".p12"}:
        raise FactoryError("secret files cannot be packaged")
    if path.name in {".npmrc", ".pypirc", "auth.json"}:
        raise FactoryError("credential configuration cannot be packaged")
    return str(path)


def tree_manifest(root):
    root = Path(root)
    result, total = {}, 0
    for file in sorted(root.rglob("*")):
        rel = file.relative_to(root).as_posix()
        if any(p in IGNORED for p in file.relative_to(root).parts):
            continue
        if file.is_symlink() or not (file.is_file() or file.is_dir()):
            raise FactoryError("artifact contains symlink or special file")
        if file.is_dir():
            continue
        relative(rel)
        total += file.stat().st_size
        if len(result) >= MAX_FILES or total > MAX_TOTAL:
            raise FactoryError("artifact exceeds configured packaging safety limits")
        result[rel] = hashlib.sha256(file.read_bytes()).hexdigest()
    return result


def copy_tree(source, target):
    target = Path(target)
    target.mkdir(parents=True, exist_ok=False)
    for rel in tree_manifest(source):
        src, dst = Path(source) / rel, target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        if src.stat().st_mode & stat.S_IXUSR:
            dst.chmod(0o700)


def command(value):
    if not isinstance(value, list) or not value or len(value) > 80:
        raise FactoryError("command must be a non-empty argv list")
    if any(
        not isinstance(v, str) or not v or len(v) > 4000 or "\x00" in v or "\n" in v
        for v in value
    ):
        raise FactoryError("invalid command arguments")
    # Commands run only in the separately managed container, never a host shell.
    if value[0] not in {"python", "python3", "node", "npm", "npx", "pip", "pip3"}:
        raise FactoryError(
            "command executable is not supported by the first factory runtime"
        )
    return value


def validate_plan(value, scenario):
    if isinstance(value, dict) and value.get("profile") == "review-only":
        from .store import text

        return {
            "profile": "review-only",
            "reason": text(value.get("reason"), "unsupported runtime reason", 2000),
            "install": [],
            "build": [],
            "tests": [],
            "start": None,
            "port": 8080,
            "checks": [],
            "parameter_checks": ["atlas-example", "renamed-example"],
        }
    if not isinstance(value, dict) or value.get("profile") not in PROFILES:
        raise FactoryError("plan must select a supported runtime profile")
    out = {"profile": value["profile"]}
    for key in ("install", "build", "tests"):
        commands = value.get(key, [])
        if not isinstance(commands, list) or len(commands) > 12:
            raise FactoryError("invalid plan commands")
        out[key] = [command(c) for c in commands]
    out["start"] = command(value["start"]) if value.get("start") else None
    out["port"] = value.get("port", 8080)
    if type(out["port"]) is not int or not 1024 <= out["port"] <= 65535:
        raise FactoryError("invalid application port")
    checks = value.get("checks")
    if not isinstance(checks, list) or not checks or len(checks) > 60:
        raise FactoryError("plan needs observable acceptance checks")
    valid_actions = {
        "http",
        "goto",
        "fill",
        "click",
        "open_link",
        "expect_text",
        "reload",
        "restart",
        "command",
    }
    covered = set()
    for check in checks:
        if not isinstance(check, dict) or check.get("action") not in valid_actions:
            raise FactoryError("invalid acceptance action")
        index = check.get("criterion")
        if type(index) is not int or not 0 <= index < len(scenario["acceptance"]):
            raise FactoryError(
                "every check must reference a scenario acceptance criterion"
            )
        if check["action"] in {"http", "expect_text", "command", "open_link"}:
            covered.add(index)
        path = check.get("path", "/")
        if (
            not isinstance(path, str)
            or not path.startswith("/")
            or path.startswith("//")
            or "\\" in path
        ):
            raise FactoryError("checks must target local application paths")
        if check["action"] == "command":
            command(check.get("argv"))
            if not isinstance(check.get("contains"), str) or not check["contains"]:
                raise FactoryError("command checks need an expected output")
        if check["action"] in {"http", "expect_text"} and (
            not isinstance(check.get("contains"), str) or not check["contains"]
        ):
            raise FactoryError("observable checks need expected text")
        if check["action"] in {"fill", "click", "open_link"}:
            if not isinstance(check.get("selector"), str) or not check["selector"]:
                raise FactoryError("browser action needs a selector")
            if check["action"] == "fill" and not isinstance(check.get("value"), str):
                raise FactoryError("fill action needs a value")
        if check["action"] == "open_link":
            url = check.get("url")
            parsed = urlsplit(url) if isinstance(url, str) else None
            if (
                not parsed
                or parsed.scheme not in {"http", "https"}
                or not parsed.hostname
                or parsed.username is not None
                or parsed.password is not None
            ):
                raise FactoryError(
                    "open_link needs an HTTP(S) target without credentials"
                )
    if covered != set(range(len(scenario["acceptance"]))):
        raise FactoryError("fixed checks must cover every acceptance criterion")
    if out["profile"] != "cli" and not out["start"]:
        raise FactoryError("Web runtime requires a start command")
    planned_commands = [*out["install"], *out["build"], *out["tests"]]
    if out["start"]:
        planned_commands.append(out["start"])
    planned_commands.extend(c["argv"] for c in checks if c["action"] == "command")
    for argv in planned_commands:
        if argv[0] not in PROFILE_EXECUTABLES[out["profile"]]:
            raise FactoryError(
                f"{out['profile']} image does not supply {argv[0]}; select a compatible "
                "profile and commands, or use review-only for an unsupported runtime",
                "plan_runtime_mismatch",
                409,
            )
    out["checks"] = checks
    out["parameter_checks"] = ["atlas-example", "renamed-example"]
    out["review_note"] = (
        "AI-proposed plan; independent execution is technical evidence, not human product approval."
    )
    return out


def validate_template(value, source):
    if (
        not isinstance(value, dict)
        or not isinstance(value.get("name"), str)
        or not value["name"].strip()
    ):
        raise FactoryError("template name is required")
    renders = value.get("render_files", [])
    if not isinstance(renders, list) or len(renders) > 100:
        raise FactoryError("invalid render_files")
    for rel in renders:
        path = Path(source) / relative(rel)
        if not path.is_file() or "@@PROJECT_NAME@@" not in path.read_text(
            encoding="utf-8"
        ):
            raise FactoryError("each render file must contain @@PROJECT_NAME@@")
        if Path(rel).name.lower().startswith(("license", "copying", "notice")):
            raise FactoryError("upstream notices cannot be parameterized")
    if not renders:
        raise FactoryError("template must actually use its project_name parameter")
    for rel in tree_manifest(source):
        path = Path(source) / rel
        if (
            path.stat().st_size <= 4_000_000
            and b"@@PROJECT_NAME@@" in path.read_bytes()
            and rel not in renders
        ):
            raise FactoryError("project-name token found outside render_files")
    return {
        "schema": 1,
        "name": value["name"][:160],
        "description": str(value.get("description") or "")[:4000],
        "parameters": {
            "project_name": {
                "type": "string",
                "default": "atlas-example",
                "pattern": "^[a-z][a-z0-9-]{0,62}$",
            }
        },
        "render_files": list(dict.fromkeys(renders)),
    }


def render_template(bundle, destination, project_name):
    if not isinstance(project_name, str) or not re.fullmatch(
        r"[a-z][a-z0-9-]{0,62}", project_name
    ):
        raise FactoryError(
            "project_name must be a lowercase name using letters, digits and hyphens"
        )
    bundle, destination = Path(bundle), Path(destination)
    expected = json.loads((bundle / "inventory.json").read_text())
    current = {
        "source": tree_manifest(bundle / "source"),
        "manifest": json.loads((bundle / "manifest.json").read_text()),
        "plan": json.loads((bundle / "plan.json").read_text()),
        "provenance": json.loads((bundle / "provenance.json").read_text()),
    }
    if digest(current) != expected["digest"]:
        raise FactoryError(
            "template contents changed after freezing", "artifact_changed", 409
        )
    manifest = validate_template(current["manifest"], bundle / "source")
    copy_tree(bundle / "source", destination)
    for rel in manifest["render_files"]:
        path = destination / rel
        path.write_text(path.read_text().replace("@@PROJECT_NAME@@", project_name))
    atomic_json(
        destination / ".atlas-template.json",
        {
            "schema": 1,
            "template_digest": expected["digest"],
            "project_name": project_name,
        },
    )
    return current["plan"]


def freeze(source, target, value, plan, provenance):
    target = Path(target)
    target.mkdir(parents=True, exist_ok=False)
    copy_tree(source, target / "source")
    manifest = validate_template(value, target / "source")
    body = {
        "source": tree_manifest(target / "source"),
        "manifest": manifest,
        "plan": plan,
        "provenance": provenance,
    }
    for name in ("manifest", "plan", "provenance"):
        atomic_json(target / f"{name}.json", body[name])
    fingerprint = digest(body)
    atomic_json(target / "inventory.json", {"digest": fingerprint})
    return {
        "digest": fingerprint,
        "manifest": manifest,
        "plan": plan,
        "provenance": provenance,
    }


def archive_tree(source, output):
    source, output = Path(source), Path(output)
    # Unlike source manifests, package metadata at the bundle root is included.
    paths = sorted(source.rglob("*"))
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            if path.is_symlink():
                raise FactoryError("symlinks cannot be exported")
            if path.is_file():
                info = zipfile.ZipInfo(
                    path.relative_to(source).as_posix(), date_time=(2026, 1, 1, 0, 0, 0)
                )
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
    return output
