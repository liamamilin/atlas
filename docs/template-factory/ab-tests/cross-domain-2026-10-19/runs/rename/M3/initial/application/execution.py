"""apply: whole-batch stale/conflict precheck, then atomic same-directory renames.

Ordering matters for failure safety:
1. Validate the plan path is inside the state directory and the plan is real.
2. Require --confirm. Refuse a plan already applied (no second rename round).
3. Precheck *every* operation (source identity intact, no duplicate target, no
   target on a source name, target must not exist) before touching anything.
4. Rename one by one; update the receipt (flush+fsync) after each step. On any
   failure, roll the completed renames back so no partial batch survives.
"""

import json
import os
import stat as stat_mod
from datetime import datetime, timezone

from errors import AppError
from identity import identity_matches
from paths import resolve_state_file, state_dir_path
from planning import check_simple_name
from state import read_json, write_json_atomic, write_new_json


def _load_plan(root_real, raw_plan):
    plan_path = resolve_state_file(root_real, raw_plan)
    plan = read_json(plan_path)
    if not isinstance(plan, dict) or plan.get("kind") != "atlas-renamer-plan":
        raise AppError("不是有效的重命名计划文件")
    operations = plan.get("operations")
    if not isinstance(operations, list):
        raise AppError("计划缺少 operations 列表")
    plan_id = plan.get("plan_id")
    if not isinstance(plan_id, str) or not plan_id:
        raise AppError("计划缺少 plan_id")
    return plan, operations, plan_id, plan_path


def _receipt_path(root_real, plan_id):
    return os.path.join(state_dir_path(root_real), "receipt-%s.json" % plan_id)


def _read_existing_receipt(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError):
        return None
    return data if isinstance(data, dict) else None


def _precheck(root_real, operations):
    """Validate the whole batch; raise before any mutation on any problem."""
    old_names = set()
    for op in operations:
        if not isinstance(op, dict):
            raise AppError("计划操作项无效")
        old = op.get("old")
        new = op.get("new")
        if not isinstance(old, str) or not isinstance(new, str):
            raise AppError("计划操作缺少 old/new")
        if not isinstance(op.get("identity"), dict) or not op["identity"]:
            raise AppError("计划操作缺少 identity 证据")
        check_simple_name(old, "源文件名")
        check_simple_name(new, "目标文件名")
        old_names.add(old)

    prepared = []
    seen_targets = set()
    for op in operations:
        old, new = op["old"], op["new"]
        old_path = os.path.join(root_real, old)
        new_path = os.path.join(root_real, new)
        if not os.path.lexists(old_path):
            raise AppError("源文件不存在，计划已过期：%s" % old)
        try:
            st = os.lstat(old_path)
        except OSError as exc:
            raise AppError("无法读取源文件 %s：%s" % (old, exc))
        if not stat_mod.S_ISREG(st.st_mode):
            raise AppError("源文件已不再是普通文件，计划已过期：%s" % old)
        if not identity_matches(old_path, op["identity"]):
            raise AppError("源文件已改动，计划已过期：%s" % old)
        if new in seen_targets:
            raise AppError("多个源文件指向同一新名，拒绝执行：%s" % new)
        seen_targets.add(new)
        if new in old_names:
            raise AppError("新名落在本批次源文件名内，拒绝内部覆盖：%s" % new)
        if os.path.lexists(new_path):
            raise AppError("目标已存在，拒绝覆盖：%s" % new)
        prepared.append((old_path, new_path, op))
    return prepared


def _receipt_operations(operations):
    return [
        {"old": op["old"], "new": op["new"], "identity": dict(op.get("identity") or {})}
        for op in operations
    ]


def _rename_no_overwrite(old_path, new_path):
    # Re-check immediately before the call to shrink the TOCTOU window; a tiny
    # race remains (documented limit) because stdlib exposes no RENAME_NOREPLACE.
    if os.path.lexists(new_path):
        raise AppError("目标在改名瞬间出现，拒绝覆盖：%s" % os.path.basename(new_path))
    os.rename(old_path, new_path)


def _rollback(done):
    for old_path, new_path in reversed(done):
        try:
            if os.path.lexists(new_path) and not os.path.lexists(old_path):
                os.rename(new_path, old_path)
        except OSError:
            pass


def apply_plan(root_real, raw_plan, confirm):
    _plan, operations, plan_id, plan_path = _load_plan(root_real, raw_plan)

    if not confirm:
        raise AppError("apply 需要显式 --confirm 才会执行改名")

    receipt_path = _receipt_path(root_real, plan_id)
    existing = _read_existing_receipt(receipt_path)
    if existing and existing.get("applied") and not existing.get("undone"):
        raise AppError("该计划已执行过（already-applied），拒绝重复改名")

    prepared = _precheck(root_real, operations)

    receipt = {
        "version": 1,
        "kind": "atlas-renamer-receipt",
        "plan_id": plan_id,
        "plan": plan_path,
        "root": root_real,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "applied": False,
        "undone": False,
        "completed": 0,
        "operations": _receipt_operations(operations),
    }
    if os.path.lexists(receipt_path):
        write_json_atomic(receipt_path, receipt)
    else:
        write_new_json(receipt_path, receipt)

    done = []
    try:
        for index, (old_path, new_path, _op) in enumerate(prepared, start=1):
            _rename_no_overwrite(old_path, new_path)
            done.append((old_path, new_path))
            receipt["completed"] = index
            write_json_atomic(receipt_path, receipt)
    except AppError:
        _rollback(done)
        receipt["applied"] = False
        receipt["failed"] = True
        try:
            write_json_atomic(receipt_path, receipt)
        except AppError:
            pass
        raise
    except OSError as exc:
        _rollback(done)
        raise AppError("执行改名失败：%s" % exc)

    receipt["applied"] = True
    receipt["completed"] = len(prepared)
    receipt["applied_at"] = datetime.now(timezone.utc).isoformat()
    write_json_atomic(receipt_path, receipt)

    return {
        "status": "applied",
        "operations": [{"old": op["old"], "new": op["new"]} for op in operations],
        "receipt": receipt_path,
    }
