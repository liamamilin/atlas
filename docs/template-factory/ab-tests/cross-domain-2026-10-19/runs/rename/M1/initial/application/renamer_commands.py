# -*- coding: utf-8 -*-
"""list / preview / apply / undo 四个命令的高层实现。

失败的语义：任何一步拒绝或失败都抛出 AppError，由 CLI 层转为非零退出 + stderr；
本模块绝不返回部分成功的 JSON。
"""

import os
import stat

from renamer_errors import AppError
from renamer_listing import list_regular_files
from renamer_plans import (
    PLAN_VERSION,
    active_operations,
    build_operations,
    check_conflicts,
    identity_matches,
    make_plan,
    now_stamp,
    public_operations,
    validate_find_replace,
    validate_plan,
    validate_receipt,
)
from renamer_state import (
    canonical_root,
    ensure_state_dir,
    read_json,
    resolve_state_path,
    write_json_atomic,
    write_json_exclusive,
)


def cmd_list(root):
    root_real = canonical_root(root)
    return {'files': list_regular_files(root_real)}


def cmd_preview(root, find, replace, plan_arg):
    root_real = canonical_root(root)
    validate_find_replace(find, replace)
    # 先验证状态路径（含符号链接与穿越），此时还不创建状态目录。
    resolve_state_path(root_real, plan_arg)
    names = [item['name'] for item in list_regular_files(root_real)]
    ops = build_operations(names, find, replace)
    check_conflicts(root_real, ops)
    plan = make_plan(root_real, find, replace, ops)
    ensure_state_dir(root_real)
    plan_path = resolve_state_path(root_real, plan_arg)
    write_json_exclusive(plan_path, plan)
    return {
        'status': 'preview',
        'operations': public_operations(plan['operations']),
        'plan': plan_path,
    }


def _receipt_path(plan_path):
    directory = os.path.dirname(plan_path)
    stem = os.path.splitext(os.path.basename(plan_path))[0]
    return os.path.join(directory, 'receipt-' + stem + '.json')


def _verify_sources(root_real, ops):
    """执行前核对每个源文件的类型与身份证据；全部通过才继续。"""
    for op in active_operations(ops):
        src = os.path.join(root_real, op['old'])
        try:
            st = os.lstat(src)
        except OSError as exc:
            raise AppError('计划已过期，源文件不可用: %s (%s)' % (op['old'], exc))
        if not stat.S_ISREG(st.st_mode):
            raise AppError('计划已过期，源文件类型改变: %s' % op['old'])
        if not identity_matches(op.get('identity'), st):
            raise AppError('计划已过期，源文件已改动: %s' % op['old'])


def _write_receipt(path, root_real, plan_path, status, operations, completed):
    payload = {
        'version': PLAN_VERSION,
        'status': status,
        'updated_at': now_stamp(),
        'root': root_real,
        'plan': plan_path,
        'operations': operations,
        'completed': completed,
    }
    write_json_atomic(path, payload)


def _rollback_apply(root_real, completed):
    for op in reversed(completed):
        src = os.path.join(root_real, op['old'])
        dst = os.path.join(root_real, op['new'])
        try:
            if os.path.lexists(dst) and not os.path.lexists(src):
                os.rename(dst, src)
        except OSError:
            pass


def _remove(path):
    try:
        if os.path.lexists(path):
            os.remove(path)
    except OSError:
        pass


def cmd_apply(root, plan_arg, confirm):
    root_real = canonical_root(root)
    if not confirm:
        raise AppError('apply 需要显式 --confirm 才会执行')
    plan_path = resolve_state_path(root_real, plan_arg)
    plan = read_json(plan_path)
    validate_plan(plan, root_real)
    receipt_path = _receipt_path(plan_path)
    if os.path.lexists(receipt_path):
        existing = read_json(receipt_path)
        if existing.get('status') == 'applied':
            return {
                'status': 'already-applied',
                'operations': public_operations(plan['operations']),
                'receipt': receipt_path,
            }
        raise AppError('存在未完成的执行回执，拒绝重复执行: %s' % receipt_path)
    ops = plan['operations']
    check_conflicts(root_real, ops)
    _verify_sources(root_real, ops)
    completed = []
    try:
        for op in active_operations(ops):
            src = os.path.join(root_real, op['old'])
            dst = os.path.join(root_real, op['new'])
            # 每步执行前再次核查：目标出现即拒绝且不替换（D03，极小 TOCTOU 窗口）。
            if os.path.lexists(dst):
                raise AppError('执行时目标已存在: %s' % op['new'])
            st = os.lstat(src)
            if not stat.S_ISREG(st.st_mode) or not identity_matches(op.get('identity'), st):
                raise AppError('执行时源文件已改动: %s' % op['old'])
            os.rename(src, dst)
            completed.append(op)
            _write_receipt(receipt_path, root_real, plan_path, 'applying', ops, completed)
    except AppError:
        _rollback_apply(root_real, completed)
        _remove(receipt_path)
        raise
    except OSError as exc:
        _rollback_apply(root_real, completed)
        _remove(receipt_path)
        raise AppError('改名失败，已回滚本次未完成的部分: %s' % exc)
    _write_receipt(receipt_path, root_real, plan_path, 'applied', ops, completed)
    return {
        'status': 'applied',
        'operations': public_operations(ops),
        'receipt': receipt_path,
    }


def _undo_rollback(root_real, done):
    for op in reversed(done):
        old_p = os.path.join(root_real, op['old'])
        new_p = os.path.join(root_real, op['new'])
        try:
            if os.path.lexists(old_p) and not os.path.lexists(new_p):
                os.rename(old_p, new_p)
        except OSError:
            pass


def cmd_undo(root, receipt_arg, confirm):
    root_real = canonical_root(root)
    if not confirm:
        raise AppError('undo 需要显式 --confirm 才会执行')
    receipt_path = resolve_state_path(root_real, receipt_arg)
    receipt = read_json(receipt_path)
    validate_receipt(receipt, root_real)
    status = receipt.get('status')
    if status == 'undone':
        raise AppError('该回执已撤销，拒绝重复撤销')
    if status != 'applied':
        raise AppError('回执状态为 %r，拒绝撤销' % status)
    ops = receipt['operations']
    to_restore = active_operations(ops)
    # 整批预检：任一旧名被占用或数据被改动即拒绝，不覆盖不删除。
    for op in to_restore:
        old_p = os.path.join(root_real, op['old'])
        new_p = os.path.join(root_real, op['new'])
        if os.path.lexists(old_p):
            raise AppError('撤销冲突，旧名已被占用: %s' % op['old'])
        if not os.path.lexists(new_p):
            raise AppError('撤销失败，已改名文件不存在: %s' % op['new'])
        st = os.lstat(new_p)
        if not stat.S_ISREG(st.st_mode) or not identity_matches(op.get('identity'), st):
            raise AppError('撤销拒绝，文件已被改动: %s' % op['new'])
    done = []
    try:
        for op in to_restore:
            old_p = os.path.join(root_real, op['old'])
            new_p = os.path.join(root_real, op['new'])
            if os.path.lexists(old_p):
                raise AppError('撤销冲突，旧名已被占用: %s' % op['old'])
            st = os.lstat(new_p)
            if not stat.S_ISREG(st.st_mode) or not identity_matches(op.get('identity'), st):
                raise AppError('撤销拒绝，文件已被改动: %s' % op['new'])
            os.rename(new_p, old_p)
            done.append(op)
    except AppError:
        _undo_rollback(root_real, done)
        raise
    except OSError as exc:
        _undo_rollback(root_real, done)
        raise AppError('撤销失败，已回滚本次未完成的部分: %s' % exc)
    receipt['status'] = 'undone'
    receipt['updated_at'] = now_stamp()
    write_json_atomic(receipt_path, receipt)
    return {'status': 'undone'}
