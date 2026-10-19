"""Validate and prepare an uploaded application ZIP for the isolated runner."""

from __future__ import annotations

import json
from pathlib import Path

from .artifacts import PROFILE_EXECUTABLES, command, relative, tree_manifest
from .blueprints import unpack_archive
from .store import FactoryError

SCHEMA = "atlas.application-delivery.v1"
MAX_FILES = 300
MAX_FILE_SIZE = 8 * 1024 * 1024
WEB_PROFILES = {"python-web", "node-web", "static-web"}


def _strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise FactoryError("delivery metadata has duplicate keys")
        result[key] = value
    return result


def _runtime(value):
    if not isinstance(value, dict) or not isinstance(value.get("profile"), str) or value.get("profile") not in {
        "python-web", "node-web", "cli", "static-web"
    }:
        raise FactoryError("invalid delivery runtime profile")
    profile = value["profile"]
    allowed = {"profile", "install", "build", "start", "smoke", "port", "readiness_path"}
    if set(value) - allowed:
        raise FactoryError("unknown delivery runtime field")
    result = {"profile": profile}
    for field in ("install", "build"):
        commands = value.get(field, [])
        if not isinstance(commands, list) or len(commands) > 12:
            raise FactoryError("invalid delivery command list")
        result[field] = []
        for argv in commands:
            checked = command(argv)
            if checked[0] not in PROFILE_EXECUTABLES[profile]:
                raise FactoryError("command executable does not match runtime profile")
            result[field].append(list(checked))

    if profile in WEB_PROFILES:
        if "start" not in value or "smoke" in value:
            raise FactoryError("web runtime requires start and forbids smoke")
        start = command(value["start"])
        if start[0] not in PROFILE_EXECUTABLES[profile]:
            raise FactoryError("start executable does not match runtime profile")
        result["start"] = list(start)
        port = value.get("port")
        if type(port) is not int or not 1024 <= port <= 65535:
            raise FactoryError("invalid application port")
        result["port"] = port
        path = value.get("readiness_path", "/")
        if (not isinstance(path, str) or not path.startswith("/") or path.startswith("//")
                or "\\" in path or "?" in path or "#" in path or "\x00" in path
                or any(part in {".", ".."} for part in path.split("/"))):
            raise FactoryError("invalid readiness path")
        result["readiness_path"] = path
    else:
        if "smoke" not in value or "start" in value or "port" in value or "readiness_path" in value:
            raise FactoryError("CLI runtime requires smoke and forbids web fields")
        smoke = command(value["smoke"])
        if smoke[0] not in PROFILE_EXECUTABLES[profile]:
            raise FactoryError("smoke executable does not match runtime profile")
        result["smoke"] = list(smoke)
    return result


def _normalize_declared(declared, known):
    if not isinstance(declared, str):
        raise FactoryError("delivery file paths must be strings")
    # Validate exactly as supplied before considering the sole supported alias.
    path = relative(declared)
    candidates = {path}
    if path.startswith("app/"):
        if path.startswith("app/app/") and path[4:] in known and path not in known:
            raise FactoryError("repeated app/ prefix is not a supported alias")
        candidates.add(path[4:])
    else:
        candidates.add("app/" + path)
    matches = candidates & known
    if len(matches) != 1:
        raise FactoryError("declared delivery path is missing or ambiguous")
    normalized = next(iter(matches))
    return normalized


def prepare_application(data: bytes, destination: Path) -> dict:
    """Safely unpack an app archive and validate its exact declared inventory.

    This routine only inspects and writes bytes. It does not execute app code.
    """
    destination = Path(destination)
    if destination.exists() and any(destination.iterdir()):
        raise FactoryError("application destination must be empty")
    destination.mkdir(parents=True, exist_ok=True)
    unpack_archive(data, destination)

    metadata_path = destination / "delivery.json"
    if not metadata_path.is_file() or metadata_path.is_symlink():
        raise FactoryError("application ZIP needs root delivery.json")
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"), object_pairs_hook=_strict_object)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise FactoryError("invalid delivery.json") from error
    if (not isinstance(metadata, dict) or set(metadata) - {"schema", "root", "files", "runtime"}
            or not {"schema", "files", "runtime"}.issubset(metadata)
            or metadata.get("schema") != SCHEMA):
        raise FactoryError("unsupported delivery metadata schema")
    root = metadata.get("root", ".")
    if not isinstance(root, str) or root not in {".", "app"}:
        raise FactoryError("delivery root must be '.' or 'app'")

    # The existing archive unpacker has already rejected traversal, duplicate,
    # symlink, special, secret and internal paths. tree_manifest repeats the
    # source policy while yielding content hashes.
    archive_files = tree_manifest(destination)
    if "delivery.json" not in archive_files:
        raise FactoryError("invalid delivery metadata file")
    if root == ".":
        # Metadata is control input, never a delivered application file.
        metadata_path.unlink()
    all_sources = set(archive_files) - {"delivery.json"}
    if root == "app":
        if not all_sources or any(not name.startswith("app/") for name in all_sources):
            raise FactoryError("root='app' archives may contain only app/ source files")
        source_map = {name[4:]: archive_files[name] for name in all_sources}
        app_root = "app"
    else:
        source_map = {name: value for name, value in archive_files.items() if name != "delivery.json"}
        app_root = "."
    if not source_map or len(source_map) > MAX_FILES:
        raise FactoryError("application source inventory is empty or too large")
    for name in source_map:
        path = destination / ("app/" + name if root == "app" else name)
        if path.stat().st_size > MAX_FILE_SIZE:
            raise FactoryError("application source file is too large")

    declared = metadata.get("files")
    if not isinstance(declared, list) or not declared or len(declared) > MAX_FILES:
        raise FactoryError("delivery files must declare 1 to 300 source files")
    normalized, aliases = [], []
    physical_by_relative = {
        (name[4:] if root == "app" else name): name
        for name in all_sources
    }
    for entry in declared:
        actual = _normalize_declared(entry, set(source_map))
        if (root == "app" and entry == actual and entry.startswith("app/")
                and physical_by_relative.get(actual) == "app/" + entry):
            raise FactoryError("repeated app/ prefix at application root is not supported")
        if actual in normalized:
            raise FactoryError("duplicate or colliding delivery file aliases")
        normalized.append(actual)
        if entry != actual:
            aliases.append({"declared": entry, "path": actual})
    if set(normalized) != set(source_map):
        raise FactoryError("delivery inventory must exactly match application source files")

    runtime = _runtime(metadata.get("runtime"))
    # Keep only app bytes under app/ for root='app'. The metadata file stays at
    # destination root and never enters the delivered application tree.
    files = {name: source_map[name] for name in sorted(source_map)}
    return {
        "schema": SCHEMA,
        "app_root": app_root,
        "files": files,
        "normalizations": aliases,
        "runtime": runtime,
    }
