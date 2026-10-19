"""Root and state-directory resolution with strict boundary checks."""

import os

from atlas_errors import AtlasError

STATE_DIR_NAME = ".atlas-renamer"


def _within(child, parent):
    """True if resolved ``child`` is ``parent`` or lives beneath it."""
    child = os.path.realpath(child)
    parent = os.path.realpath(parent)
    if child == parent:
        return True
    return child.startswith(parent + os.sep)


def normalize_root(root_arg):
    """Resolve the explicit root directory to a real absolute path."""
    if not root_arg:
        raise AtlasError("必须提供 --root 目录")
    root = os.path.realpath(os.path.abspath(root_arg))
    if not os.path.isdir(root):
        raise AtlasError(f"根目录不存在或不是目录: {root_arg}")
    return root


def state_dir_path(root):
    return os.path.join(root, STATE_DIR_NAME)


def ensure_state_dir(root):
    """Create and return the real state directory, refusing symlink escapes."""
    sd = state_dir_path(root)
    if os.path.islink(sd):
        raise AtlasError("状态目录不能是符号链接")
    if os.path.exists(sd):
        if not os.path.isdir(sd):
            raise AtlasError("状态目录路径已被非目录占用")
    else:
        os.mkdir(sd, 0o700)
    real_sd = os.path.realpath(sd)
    if not _within(real_sd, root):
        raise AtlasError("状态目录越出指定根目录")
    return real_sd


def resolve_state_path(given, sd_real):
    """Resolve a user-supplied plan/receipt path and require it in the state dir.

    Both a symlinked parent and a symlinked target are rejected when they would
    resolve outside the state directory.
    """
    if not given:
        raise AtlasError("必须提供路径")
    absolute = os.path.abspath(given)
    parent = os.path.dirname(absolute)
    base = os.path.basename(absolute)
    if base in ("", ".", ".."):
        raise AtlasError("非法文件名")
    real_parent = os.path.realpath(parent)
    if not _within(real_parent, sd_real):
        raise AtlasError(f"路径必须位于状态目录内: {sd_real}")
    target = os.path.join(real_parent, base)
    if os.path.lexists(target):
        real_target = os.path.realpath(target)
        if not _within(real_target, sd_real):
            raise AtlasError("目标路径越界或为外部符号链接")
    if not _within(target, sd_real):
        raise AtlasError("目标路径越界")
    return target
