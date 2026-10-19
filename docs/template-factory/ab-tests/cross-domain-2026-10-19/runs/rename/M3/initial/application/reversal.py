"""undo: restore this batch only, refusing any new conflict or changed data.

Whole-batch precheck first: every old name must currently be free, every new
name must still exist with the recorded identity. Only then are the renames
performed (in reverse is unnecessary; the batch is conflict-free by contract),
with rollback on unexpected failure. Nothing is ever overwritten or deleted.
"""

import os
import stat as stat_mod
from datetime import datetime, timezone

from errors import AppError
from identity import identity_matches
from paths import resolve_state_file
from planning import check_simple_name
from state import read_json, write_json_atomic


def _rollback(done):
    for old_path, new_path in reversed(done):
        try:
            if os.path.lexists(old_path) and not os.path.lexists(new_path):
                os.rename(old_path, new_path)
        except OSError:
            pass


def _precheck(root_real, operations):
    prepared = []
    for op in operations:
        if not isinstance(op, dict):
            raise AppError("回执操作项无效")
        old = op.get("old")
        new = op.get("new")
        ident = op.get("identity")
        if not isinstance(old, str) or not isinstance(new, str):
            raise AppError("回执操作缺少 old/new")
        check_simple_name(old, "旧文件名")
        check_simple_name(new, "已改名文件名")
        old_path = os.path.join(root_real, old)
        new_path = os.path.join(root_real, new)
        if os.path.lexists(old_path):
            raise AppError("撤销冲突：旧名已被占用，拒绝覆盖 %s" % old)
        if not os.path.lexists(new_path):
            raise AppError("撤销失败：找不到已改名的文件 %s" % new)
        try:
            st = os.lstat(new_path)
        except OSError as exc:
            raise AppError("无法读取 %s：%s" % (new, exc))
        if not stat_mod.S_ISREG(st.st_mode):
            raise AppError("撤销冲突：%s 已不再是普通文件" % new)
        if not isinstance(ident, dict) or not ident:
            raise AppError("回执缺少身份证据，拒绝撤销：%s" % new)
        if not identity_matches(new_path, ident):
            raise AppError("撤销冲突：%s 数据已被改动，拒绝覆盖" % new)
        prepared.append((old_path, new_path))
    return prepared


def undo_receipt(root_real, raw_receipt, confirm):
    receipt_path = resolve_state_file(root_real, raw_receipt)

    if not confirm:
        raise AppError("undo 需要显式 --confirm 才会撤销")

    receipt = read_json(receipt_path)
    if not isinstance(receipt, dict) or receipt.get("kind") != "atlas-renamer-receipt":
        raise AppError("不是有效的执行回执")
    if not receipt.get("applied"):
        if receipt.get("undone"):
            raise AppError("本批次已经撤销过，拒绝重复撤销")
        raise AppError("该回执没有记录一次成功执行，无法撤销")

    operations = receipt.get("operations")
    if not isinstance(operations, list) or not operations:
        raise AppError("回执缺少可撤销的操作")

    prepared = _precheck(root_real, operations)

    done = []
    try:
        for old_path, new_path in prepared:
            if os.path.lexists(old_path):
                raise AppError("撤销冲突：旧名在撤销瞬间被占用 %s" % os.path.basename(old_path))
            os.rename(new_path, old_path)
            done.append((old_path, new_path))
    except AppError:
        _rollback(done)
        raise
    except OSError as exc:
        _rollback(done)
        raise AppError("撤销改名失败：%s" % exc)

    receipt["applied"] = False
    receipt["undone"] = True
    receipt["undone_at"] = datetime.now(timezone.utc).isoformat()
    write_json_atomic(receipt_path, receipt)
    return {"status": "undone"}
