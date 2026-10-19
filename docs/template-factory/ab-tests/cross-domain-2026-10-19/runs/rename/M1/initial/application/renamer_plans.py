# -*- coding: utf-8 -*-
"""名称替换、整批冲突预检、身份证据以及计划/回执的校验。

设计要点：
- 查找为非空字面文本（非正则）；替换后必须是单个合法文件名。
- 身份证据默认使用 dev + ino + size + mtime_ns（D01），用于拒绝陈旧计划。
- 冲突判定在「动手之前」整批进行，任何冲突都拒绝整批。
"""

import os
import stat as _stat
import time

from renamer_errors import AppError

PLAN_VERSION = 1
IDENTITY_KEYS = ('dev', 'ino', 'size', 'mtime_ns')


def now_stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def is_plain_filename(name):
    """是否为「单个文件名」：非空、非 . / ..、无路径分隔符、非绝对路径。"""
    if not isinstance(name, str) or name in ('', '.', '..'):
        return False
    if os.path.isabs(name):
        return False
    if name != os.path.basename(name):
        return False
    if '/' in name or '\\' in name or os.sep in name:
        return False
    if os.altsep and os.altsep in name:
        return False
    return True


def validate_find_replace(find, replace):
    """查找必须非空；替换文本不得引入路径分隔符（其余由新名校验兜底）。"""
    if not isinstance(find, str) or find == '':
        raise AppError('查找文本不能为空')
    if not isinstance(replace, str):
        raise AppError('替换文本无效')
    if '/' in replace or '\\' in replace or os.sep in replace:
        raise AppError('替换文本不能包含路径分隔符')
    if os.altsep and os.altsep in replace:
        raise AppError('替换文本不能包含路径分隔符')


def identity_of(st):
    data = {'dev': int(st.st_dev), 'ino': int(st.st_ino), 'size': int(st.st_size)}
    mtime_ns = getattr(st, 'st_mtime_ns', None)
    if mtime_ns is None:
        data['mtime'] = int(st.st_mtime)
    else:
        data['mtime_ns'] = int(mtime_ns)
    return data


def has_evidence(ident):
    if not isinstance(ident, dict):
        return False
    if any(key in ident for key in IDENTITY_KEYS):
        return True
    return 'mtime' in ident


def identity_matches(ident, st):
    """当前 lstat 是否与计划/回执记录的身份证据一致。"""
    if not has_evidence(ident):
        return False
    for key in IDENTITY_KEYS:
        if key in ident:
            current = getattr(st, 'st_' + key, None)
            if current is None:
                return False
            try:
                if int(ident[key]) != int(current):
                    return False
            except (TypeError, ValueError):
                return False
    if 'mtime' in ident:
        try:
            if int(ident['mtime']) != int(st.st_mtime):
                return False
        except (TypeError, ValueError):
            return False
    return True


def build_operations(names, find, replace):
    """对匹配 find 的文件名把全部字面出现替换为 replace，并校验新名。"""
    ops = []
    for name in names:
        if find in name:
            new = name.replace(find, replace)
            if not is_plain_filename(new):
                raise AppError('替换结果不是单个合法文件名: %s -> %s' % (name, new))
            ops.append({'old': name, 'new': new})
    ops.sort(key=lambda op: op['old'])
    return ops


def active_operations(ops):
    """排除 old == new 的空操作。"""
    return [op for op in ops if op['old'] != op['new']]


def check_conflicts(root_real, ops):
    """整批冲突预检：重复目标、目标落在源集合内、目标已存在。"""
    sources = set(op['old'] for op in ops)
    targets = {}
    for op in active_operations(ops):
        new = op['new']
        if new in targets:
            raise AppError('多来源指向同一新名，整批拒绝: %s' % new)
        targets[new] = op['old']
        if new in sources:
            raise AppError('新名与批次内源文件冲突，整批拒绝: %s' % new)
        if os.path.lexists(os.path.join(root_real, new)):
            raise AppError('目标已存在，整批拒绝: %s' % new)


def make_plan(root_real, find, replace, ops):
    """生成带身份证据的计划对象。"""
    plan_ops = []
    for op in ops:
        src = os.path.join(root_real, op['old'])
        try:
            st = os.lstat(src)
        except OSError as exc:
            raise AppError('无法读取源文件 %s: %s' % (op['old'], exc))
        if not _stat.S_ISREG(st.st_mode):
            raise AppError('源不是普通文件: %s' % op['old'])
        plan_ops.append({'old': op['old'], 'new': op['new'], 'identity': identity_of(st)})
    return {
        'version': PLAN_VERSION,
        'created_at': now_stamp(),
        'root': root_real,
        'find': find,
        'replace': replace,
        'operations': plan_ops,
    }


def public_operations(ops):
    return [{'old': op['old'], 'new': op['new']} for op in ops]


def _validate_operation_list(items, label):
    seen = set()
    for op in items:
        if not isinstance(op, dict):
            raise AppError('%s operation 不是对象' % label)
        if not is_plain_filename(op.get('old')) or not is_plain_filename(op.get('new')):
            raise AppError('%s 含非法文件名' % label)
        if op['old'] in seen:
            raise AppError('%s 含重复源文件: %s' % (label, op['old']))
        seen.add(op['old'])
        if not has_evidence(op.get('identity')):
            raise AppError('%s 缺少可核对的身份证据: %s' % (label, op['old']))


def validate_plan(plan, root_real):
    if not isinstance(plan, dict):
        raise AppError('计划文件不是 JSON 对象')
    if plan.get('version') != PLAN_VERSION:
        raise AppError('计划版本不受支持')
    plan_root = plan.get('root')
    if not isinstance(plan_root, str) or os.path.realpath(plan_root) != root_real:
        raise AppError('计划根目录与 --root 不一致')
    ops = plan.get('operations')
    if not isinstance(ops, list):
        raise AppError('计划缺少 operations 列表')
    _validate_operation_list(ops, '计划')


def validate_receipt(receipt, root_real):
    if not isinstance(receipt, dict):
        raise AppError('回执文件不是 JSON 对象')
    if receipt.get('version') != PLAN_VERSION:
        raise AppError('回执版本不受支持')
    receipt_root = receipt.get('root')
    if not isinstance(receipt_root, str) or os.path.realpath(receipt_root) != root_real:
        raise AppError('回执根目录与 --root 不一致')
    ops = receipt.get('operations')
    if not isinstance(ops, list) or not ops:
        raise AppError('回执缺少 operations 记录')
    _validate_operation_list(ops, '回执')
