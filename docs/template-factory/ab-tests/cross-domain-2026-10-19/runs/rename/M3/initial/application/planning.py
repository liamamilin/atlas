"""Literal find/replace preview: validation, operations and whole-batch conflicts.

Rules baked in here:
- `find` is a non-empty literal string (never a regex).
- The replacement is applied to *every* literal occurrence in the name (D06).
- Every resulting name must be a single ordinary filename: no path separator,
  no `.`/`..`, no embedded directory traversal.
- Any conflict (target already exists, two sources share a target, or a new name
  lands on one of the batch's own source names / a rename ring) refuses the
  whole batch at preview time (D04).
"""

import os
import uuid
from datetime import datetime, timezone

from errors import AppError
from identity import capture_identity
from listing import immediate_regular_files


def check_simple_name(name, what):
    if name in ("", ".", ".."):
        raise AppError("%s不是单个有效文件名：%r" % (what, name))
    if "\x00" in name:
        raise AppError("%s包含非法字符：%r" % (what, name))
    if os.sep in name or (os.altsep and os.altsep in name):
        raise AppError("%s不能包含路径分隔符：%r" % (what, name))
    if os.path.basename(name) != name:
        raise AppError("%s解析后不是单个文件名：%r" % (what, name))


def check_replace_text(replace):
    if os.sep in replace or (os.altsep and os.altsep in replace):
        raise AppError("替换文本不能包含路径分隔符")
    if replace in (".", ".."):
        raise AppError("替换结果不能是 . 或 ..")


def build_operations(root_real, find, replace):
    operations = []
    for name, _size in immediate_regular_files(root_real):
        if find not in name:
            continue
        new_name = name.replace(find, replace)
        if new_name == name:
            continue
        check_simple_name(new_name, "新的文件名")
        operations.append({"old": name, "new": new_name})
    operations.sort(key=lambda op: op["old"])
    return operations


def find_conflicts(root_real, operations):
    problems = []
    old_names = {op["old"] for op in operations}
    seen_targets = {}
    for op in operations:
        new_name = op["new"]
        if new_name in seen_targets:
            problems.append("多个源文件指向同一新名 %s" % new_name)
        seen_targets[new_name] = op["old"]
        if new_name in old_names:
            problems.append("新名 %s 与本批次源文件名冲突（内部覆盖或换名环）" % new_name)
        if os.path.lexists(os.path.join(root_real, new_name)):
            problems.append("目标已存在，拒绝覆盖 %s" % new_name)
    return problems


def build_plan(root_real, find, replace, hash_contents=False):
    if find == "":
        raise AppError("查找文本不能为空")
    check_replace_text(replace)
    operations = build_operations(root_real, find, replace)
    problems = find_conflicts(root_real, operations)
    if problems:
        unique = list(dict.fromkeys(problems))
        raise AppError("整批冲突，已整体拒绝：" + "；".join(unique))
    for op in operations:
        op["identity"] = capture_identity(
            os.path.join(root_real, op["old"]), hash_contents=hash_contents
        )
    return {
        "version": 1,
        "kind": "atlas-renamer-plan",
        "plan_id": uuid.uuid4().hex,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "root": root_real,
        "find": find,
        "replace": replace,
        "operations": operations,
    }
