"""Filesystem inspection: ordinary-file listing and content identity."""

import hashlib
import os
import stat

from naming import is_bare_name
from paths import STATE_DIR_NAME

_CHUNK = 65536


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(_CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def list_ordinary_files(root):
    """List immediate ordinary files, excluding the state dir, dirs, symlinks."""
    entries = []
    with os.scandir(root) as iterator:
        for entry in iterator:
            if entry.name == STATE_DIR_NAME:
                continue
            try:
                if entry.is_symlink():
                    continue
                if not entry.is_file(follow_symlinks=False):
                    continue
                info = entry.stat(follow_symlinks=False)
            except OSError:
                continue
            entries.append({"name": entry.name, "size": info.st_size})
    entries.sort(key=lambda item: item["name"])
    return entries


def file_identity(path):
    """Return size/mtime/content evidence, or None when not a regular file."""
    try:
        info = os.lstat(path)
    except OSError:
        return None
    if not stat.S_ISREG(info.st_mode):
        return None
    try:
        digest = sha256_file(path)
    except OSError:
        return None
    return {
        "size": info.st_size,
        "mtime_ns": info.st_mtime_ns,
        "sha256": digest,
    }


def identity_matches(root, name, recorded):
    """True when ``root/name`` is a regular file whose content matches recorded."""
    if not recorded or not is_bare_name(name):
        return False
    path = os.path.join(root, name)
    if os.path.islink(path) or not os.path.isfile(path):
        return False
    current = file_identity(path)
    if current is None:
        return False
    return (
        current["size"] == recorded.get("size")
        and current["sha256"] == recorded.get("sha256")
    )
