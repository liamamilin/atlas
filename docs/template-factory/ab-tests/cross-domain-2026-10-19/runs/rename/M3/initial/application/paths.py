"""Root resolution and state-directory path safety.

Every plan/receipt path must resolve to a direct child of DIR/.atlas-renamer.
The check compares the *realpath of the parent directory* against the canonical
state directory, so absolute escapes, `..` traversal and a state directory that
is itself an external symlink are all refused before any write happens.
"""

import os

from errors import AppError

STATE_DIRNAME = ".atlas-renamer"


def resolve_root(raw_root):
    if not raw_root:
        raise AppError("必须通过 --root 指定一个明确的本地根目录")
    root_abs = os.path.abspath(raw_root)
    if not os.path.isdir(root_abs):
        raise AppError("--root 不是已存在的目录：%s" % raw_root)
    return os.path.realpath(root_abs)


def state_dir_path(root_real):
    return os.path.join(root_real, STATE_DIRNAME)


def ensure_state_dir(root_real):
    """Create the state directory if needed; never follow an external symlink."""
    target = state_dir_path(root_real)
    if os.path.islink(target):
        raise AppError("状态目录不能是指向别处的符号链接：%s" % STATE_DIRNAME)
    if os.path.exists(target):
        if not os.path.isdir(target):
            raise AppError("状态路径已存在且不是目录：%s" % STATE_DIRNAME)
        return target
    os.mkdir(target)
    return target


def resolve_state_file(root_real, raw_path):
    """Return the canonical path of a plan/receipt, or refuse the request.

    The file must sit directly inside DIR/.atlas-renamer. Rejecting here (before
    any mkdir/write) is what keeps a foreign symlink state directory from ever
    being written to.
    """
    if not raw_path:
        raise AppError("缺少状态文件路径")
    path = raw_path
    if not os.path.isabs(path):
        path = os.path.join(root_real, path)
    parent = os.path.dirname(path)
    base = os.path.basename(path)
    if base in ("", ".", ".."):
        raise AppError("状态文件名无效：%r" % raw_path)
    expected = state_dir_path(root_real)
    if os.path.realpath(parent) != expected:
        raise AppError("状态文件必须位于 %s 目录内：%s" % (STATE_DIRNAME, raw_path))
    return os.path.join(expected, base)
