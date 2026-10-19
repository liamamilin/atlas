"""Durable JSON storage for plans and receipts (readable, non-overwriting)."""

import json
import os

from atlas_errors import AtlasError


def _require_plain_file(path, what):
    if os.path.islink(path):
        raise AtlasError(f"{what}不能是符号链接: {path}")
    if not os.path.isfile(path):
        raise AtlasError(f"{what}不存在或不是普通文件: {path}")


def read_json(path, kind):
    """Read and validate a JSON object of the expected ``kind``."""
    _require_plain_file(path, "文件")
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        raise AtlasError(f"无法读取 JSON: {path}: {exc}")
    if not isinstance(data, dict) or data.get("kind") != kind:
        raise AtlasError(f"文件类型不符，期望 {kind}: {path}")
    return data


def write_json_exclusive(path, obj):
    """Write JSON atomically-ish and refuse to overwrite an existing file."""
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, mode=0o700, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise AtlasError(f"拒绝覆盖已存在文件: {path}")
    except OSError as exc:
        raise AtlasError(f"无法写入: {path}: {exc}")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
    except OSError as exc:
        try:
            os.unlink(path)
        except OSError:
            pass
        raise AtlasError(f"写入失败: {path}: {exc}")
