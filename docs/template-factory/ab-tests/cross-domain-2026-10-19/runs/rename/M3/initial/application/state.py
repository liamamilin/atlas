"""Durable JSON state: plans (immutable) and receipts (small journal).

Writes use flush+fsync so a receipt reflects each completed rename; the receipt
is updated with an atomic temp-file replace so a reader never sees a torn file.
This is best-effort crash visibility, not a power-failure guarantee
(see DECISIONS.md, D05).
"""

import json
import os
import tempfile

from errors import AppError


def _dump(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def write_new_json(path, obj):
    """Create a brand-new file (never overwrite). Used for immutable plans."""
    text = _dump(obj)
    try:
        with open(path, "x", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        raise AppError("状态文件已存在，拒绝覆盖：%s" % os.path.basename(path))
    except OSError as exc:
        raise AppError("无法写入状态文件 %s：%s" % (os.path.basename(path), exc))
    _fsync_dir(os.path.dirname(path))


def write_json_atomic(path, obj):
    """Replace a file atomically (temp file + os.replace) and fsync."""
    text = _dump(obj)
    directory = os.path.dirname(path)
    try:
        fd, tmp = tempfile.mkstemp(dir=directory, prefix=".tmp-", suffix=".json")
    except OSError as exc:
        raise AppError("无法在状态目录创建临时文件：%s" % exc)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    except OSError as exc:
        _silent_unlink(tmp)
        raise AppError("无法更新状态文件 %s：%s" % (os.path.basename(path), exc))
    _fsync_dir(directory)


def read_json(path):
    if os.path.islink(path):
        raise AppError("拒绝读取符号链接状态文件：%s" % os.path.basename(path))
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        raise AppError("状态文件不存在：%s" % os.path.basename(path))
    except IsADirectoryError:
        raise AppError("状态路径是目录而不是文件：%s" % os.path.basename(path))
    except PermissionError:
        raise AppError("没有权限读取状态文件：%s" % os.path.basename(path))
    except ValueError as exc:
        raise AppError("状态文件不是合法 JSON：%s（%s）" % (os.path.basename(path), exc))
    except OSError as exc:
        raise AppError("无法读取状态文件 %s：%s" % (os.path.basename(path), exc))


def _fsync_dir(directory):
    try:
        dir_fd = os.open(directory, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(dir_fd)
    except OSError:
        pass
    finally:
        os.close(dir_fd)


def _silent_unlink(path):
    try:
        os.unlink(path)
    except OSError:
        pass
