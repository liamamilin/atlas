"""Command implementations: list, preview, apply, undo."""

import os
import uuid
from datetime import datetime, timezone

from atlas_errors import AtlasError
from fsops import file_identity, identity_matches, list_ordinary_files
from naming import compute_replacements, is_bare_name, is_state_token
from paths import ensure_child_dir, ensure_state_dir, normalize_root, resolve_state_path
from planner import read_json, write_json_exclusive

PLAN_KIND = "atlas-rename-plan"
RECEIPT_KIND = "atlas-rename-receipt"


def _now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _casefolded_entries(root):
    try:
        return {name.casefold() for name in os.listdir(root)}
    except OSError as exc:
        raise AtlasError(f"无法读取根目录: {exc}")


def cmd_list(root_arg):
    root = normalize_root(root_arg)
    return {"files": list_ordinary_files(root)}


def cmd_preview(root_arg, find, replace, plan_arg):
    if not find:
        raise AtlasError("--find 不能为空（查找为字面文本，不是正则）")
    if replace is None:
        raise AtlasError("--replace 不能为空字符串参数（可用 --replace \"\" 表示删除）")
    root = normalize_root(root_arg)
    sd = ensure_state_dir(root)
    plan_target = resolve_state_path(plan_arg, sd)
    if os.path.lexists(plan_target):
        raise AtlasError(f"计划文件已存在，拒绝覆盖: {plan_target}")

    names = [item["name"] for item in list_ordinary_files(root)]
    operations = compute_replacements(names, find, replace)

    existing = _casefolded_entries(root)
    seen_new = {}
    plan_operations = []
    for old, new in operations:
        if not is_bare_name(new):
            raise AtlasError(f"替换结果不是合法文件名: {new!r}（来自 {old!r}）")
        key = new.casefold()
        if key in seen_new:
            raise AtlasError(f"替换后文件名冲突: {new!r} 与 {seen_new[key]!r}")
        if key in existing:
            raise AtlasError(f"目标文件已存在，拒绝生成计划: {new!r}")
        seen_new[key] = new
        identity = file_identity(os.path.join(root, old))
        if identity is None:
            raise AtlasError(f"源文件不是普通文件: {old}")
        plan_operations.append(
            {
                "old": old,
                "new": new,
                "size": identity["size"],
                "mtime_ns": identity["mtime_ns"],
                "sha256": identity["sha256"],
            }
        )

    plan = {
        "version": 1,
        "kind": PLAN_KIND,
        "id": uuid.uuid4().hex,
        "created": _now(),
        "root": root,
        "find": find,
        "replace": replace,
        "operations": plan_operations,
    }
    write_json_exclusive(plan_target, plan)
    return {
        "status": "preview",
        "operations": [{"old": op["old"], "new": op["new"]} for op in plan_operations],
        "plan": plan_target,
    }


def _validated_plan_ops(plan):
    operations = plan.get("operations")
    if not isinstance(operations, list):
        raise AtlasError("计划格式错误: operations 必须是数组")
    return operations


def cmd_apply(root_arg, plan_arg, confirm):
    if not confirm:
        raise AtlasError("apply 需要显式 --confirm")
    root = normalize_root(root_arg)
    sd = ensure_state_dir(root)
    plan_target = resolve_state_path(plan_arg, sd)
    plan = read_json(plan_target, PLAN_KIND)
    if plan.get("root") != root:
        raise AtlasError("计划与当前根目录不匹配")
    operations = _validated_plan_ops(plan)

    # Containment guard: the plan ``id`` becomes a receipt file name. An edited
    # or absolute value must never be able to escape the assigned root, so it is
    # validated as a safe single-segment token before any mutation happens.
    plan_id = plan.get("id")
    if not is_state_token(plan_id):
        raise AtlasError("计划 id 非法或缺失，拒绝执行（计划可能被篡改）")
    receipts_dir = ensure_child_dir(sd, "receipts")
    receipt_path = os.path.join(receipts_dir, plan_id + ".json")
    if os.path.exists(receipt_path):
        raise AtlasError("该计划已经执行过，拒绝重复执行")

    current = _casefolded_entries(root)
    seen_old = set()
    for op in operations:
        old = op.get("old")
        new = op.get("new")
        if not is_bare_name(old) or not is_bare_name(new):
            raise AtlasError("计划包含非法文件名")
        old_key = old.casefold()
        if old_key in seen_old:
            raise AtlasError(f"计划重复源文件: {old}")
        seen_old.add(old_key)
        identity = file_identity(os.path.join(root, old))
        if identity is None:
            if identity_matches(root, new, op):
                raise AtlasError("该计划似乎已经执行过")
            raise AtlasError(f"源文件缺失或不是普通文件: {old}")
        if identity["sha256"] != op.get("sha256") or identity["size"] != op.get("size"):
            raise AtlasError(f"计划已过期，源文件内容已改变: {old}")

    seen_new = {}
    for op in operations:
        new = op["new"]
        key = new.casefold()
        if key in seen_new:
            raise AtlasError(f"目标重名: {new}")
        seen_new[key] = new
        if key in current:
            raise AtlasError(f"目标已存在，拒绝整批执行: {new}")

    done = []
    try:
        for op in operations:
            os.rename(os.path.join(root, op["old"]), os.path.join(root, op["new"]))
            done.append(op)
    except OSError as exc:
        _rollback(root, done, back=False)
        raise AtlasError(f"执行失败，已回滚本次改动: {exc}")

    receipt = {
        "version": 1,
        "kind": RECEIPT_KIND,
        "plan_id": plan_id,
        "created": _now(),
        "root": root,
        "plan_path": plan_target,
        "operations": [
            {
                "old": op["old"],
                "new": op["new"],
                "size": op.get("size"),
                "sha256": op.get("sha256"),
            }
            for op in operations
        ],
    }
    try:
        write_json_exclusive(receipt_path, receipt)
    except Exception:
        _rollback(root, done, back=False)
        raise

    return {
        "status": "applied",
        "operations": [{"old": op["old"], "new": op["new"]} for op in operations],
        "receipt": receipt_path,
    }


def cmd_undo(root_arg, receipt_arg, confirm):
    if not confirm:
        raise AtlasError("undo 需要显式 --confirm")
    root = normalize_root(root_arg)
    sd = ensure_state_dir(root)
    receipt_target = resolve_state_path(receipt_arg, sd)
    receipt = read_json(receipt_target, RECEIPT_KIND)
    if receipt.get("root") != root:
        raise AtlasError("回执与当前根目录不匹配")

    operations = receipt.get("operations")
    if not isinstance(operations, list):
        raise AtlasError("回执格式错误: operations 必须是数组")
    if not operations:
        # A plan with no matching files renamed nothing; undoing it is a no-op.
        return {"status": "undone"}

    states = []
    for op in operations:
        old = op.get("old")
        new = op.get("new")
        if not is_bare_name(old) or not is_bare_name(new):
            raise AtlasError("回执包含非法文件名")
        old_exists = os.path.lexists(os.path.join(root, old))
        new_exists = os.path.lexists(os.path.join(root, new))
        new_ok = identity_matches(root, new, op)
        old_ok = identity_matches(root, old, op)
        if new_ok and not old_exists:
            states.append("applied")
        elif old_ok and not new_exists:
            states.append("undone")
        else:
            states.append("conflict")

    if all(state == "undone" for state in states):
        raise AtlasError("该回执已经撤销过")
    if any(state == "undone" for state in states):
        raise AtlasError("回执状态不一致，拒绝操作")
    if any(state == "conflict" for state in states):
        raise AtlasError("撤销目标存在冲突或数据已改变，拒绝覆盖")

    done = []
    try:
        for op in operations:
            os.rename(os.path.join(root, op["new"]), os.path.join(root, op["old"]))
            done.append(op)
    except OSError as exc:
        _rollback(root, done, back=True)
        raise AtlasError(f"撤销失败，已回滚本次改动: {exc}")

    return {"status": "undone"}


def _rollback(root, done, back):
    """Undo already-performed renames: ``back`` False => new->old, True => old->new."""
    for op in reversed(done):
        if back:
            source, target = op["old"], op["new"]
        else:
            source, target = op["new"], op["old"]
        try:
            os.rename(os.path.join(root, source), os.path.join(root, target))
        except OSError:
            pass
