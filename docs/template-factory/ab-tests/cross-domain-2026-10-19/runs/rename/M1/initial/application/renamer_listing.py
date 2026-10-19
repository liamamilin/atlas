# -*- coding: utf-8 -*-
"""列举根目录内的「立即普通文件」。

非递归；排除子目录、符号链接与内部状态目录 .atlas-renamer。
"""

import os
import stat

from renamer_errors import AppError
from renamer_state import STATE_DIR_NAME


def list_regular_files(root_real):
    """返回 [{name, size}]，按文件名排序，size 为真实字节数。"""
    try:
        entries = list(os.scandir(root_real))
    except OSError as exc:
        raise AppError('无法读取根目录: %s' % exc)
    items = []
    for entry in entries:
        if entry.name == STATE_DIR_NAME:
            continue
        try:
            st = entry.stat(follow_symlinks=False)
        except OSError:
            continue
        if stat.S_ISREG(st.st_mode):
            items.append({'name': entry.name, 'size': int(st.st_size)})
    items.sort(key=lambda item: item['name'])
    return items
