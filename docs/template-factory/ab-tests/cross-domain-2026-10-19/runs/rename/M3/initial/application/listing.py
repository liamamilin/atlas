"""Listing of immediate ordinary files in the assigned root.

Scope is deliberately narrow: no recursion, no directories, no symlinks (even
valid ones), and the internal `.atlas-renamer` state directory is excluded so
the ground truth stays predictable.
"""

import os
import stat as stat_mod

from paths import STATE_DIRNAME


def immediate_regular_files(root_real):
    """Return sorted [(name, size_bytes)] for immediate regular files only."""
    found = []
    try:
        entries = list(os.scandir(root_real))
    except OSError as exc:
        raise OSError("无法读取根目录 %s：%s" % (root_real, exc))
    for entry in entries:
        if entry.name == STATE_DIRNAME:
            continue
        try:
            st = entry.stat(follow_symlinks=False)
        except OSError:
            continue
        if stat_mod.S_ISREG(st.st_mode):
            found.append((entry.name, int(st.st_size)))
    found.sort(key=lambda item: item[0])
    return found


def list_payload(root_real):
    return {
        "files": [{"name": name, "size": size} for name, size in immediate_regular_files(root_real)]
    }
