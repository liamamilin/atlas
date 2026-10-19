# -*- coding: utf-8 -*-
"""根目录、状态目录与路径安全，以及 JSON 的读写。

所有计划文件与回执文件都必须位于 <root>/.atlas-renamer/ 的直接子项，
经 `..` 穿越、绝对路径逃逸或外部符号链接指向的状态文件一律拒绝。
"""

import json
import os

from renamer_errors import AppError

STATE_DIR_NAME = '.atlas-renamer'


def canonical_root(root):
    """校验并返回根目录的真实路径。"""
    if not isinstance(root, str) or root == '':
        raise AppError('缺少 --root 根目录')
    real = os.path.realpath(root)
    if not os.path.isdir(real):
        raise AppError('根目录不存在或不是目录: %s' % root)
    return real


def state_dir(root_real):
    return os.path.join(root_real, STATE_DIR_NAME)


def _state_real(root_real):
    return os.path.realpath(state_dir(root_real))


def check_state_dir_safe(root_real):
    """状态目录不得是符号链接，也不得是已存在的非目录。"""
    path = state_dir(root_real)
    if os.path.islink(path):
        raise AppError('状态目录 %s 是符号链接，拒绝在根目录之外写入' % STATE_DIR_NAME)
    if os.path.lexists(path) and not os.path.isdir(path):
        raise AppError('状态路径 %s 已存在但不是目录' % path)


def ensure_state_dir(root_real):
    """安全地创建并返回状态目录。"""
    check_state_dir_safe(root_real)
    path = state_dir(root_real)
    if not os.path.isdir(path):
        try:
            os.mkdir(path, 0o700)
        except FileExistsError:
            pass
        except OSError as exc:
            raise AppError('无法创建状态目录 %s: %s' % (STATE_DIR_NAME, exc))
    if os.path.islink(path) or not os.path.isdir(path):
        raise AppError('无法安全创建状态目录 %s' % STATE_DIR_NAME)
    return path


def resolve_state_path(root_real, user_path):
    """把用户给的计划/回执路径解析为状态目录内的真实直接子项路径。"""
    check_state_dir_safe(root_real)
    if not isinstance(user_path, str) or user_path == '':
        raise AppError('缺少状态文件路径')
    candidate = user_path
    if not os.path.isabs(candidate):
        candidate = os.path.join(root_real, candidate)
    normalized = os.path.realpath(candidate)
    base = os.path.basename(normalized)
    if os.path.dirname(normalized) != _state_real(root_real) or base in ('', '.', '..'):
        raise AppError('状态文件必须位于 %s/ 目录内: %s' % (STATE_DIR_NAME, user_path))
    return normalized


def read_json(path):
    """读取状态目录内的普通 JSON 文件（符号链接或缺失即拒绝）。"""
    if os.path.islink(path):
        raise AppError('文件是符号链接，拒绝读取: %s' % path)
    if not os.path.isfile(path):
        raise AppError('文件不存在或不是普通文件: %s' % path)
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            return json.load(handle)
    except ValueError as exc:
        raise AppError('无法解析 JSON 文件 %s: %s' % (path, exc))
    except OSError as exc:
        raise AppError('无法读取文件 %s: %s' % (path, exc))


def _dump(path, obj):
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    with open(path, 'w', encoding='utf-8') as handle:
        handle.write(text)
        handle.write('\n')
        handle.flush()
        os.fsync(handle.fileno())


def write_json_exclusive(path, obj):
    """以独占方式创建不可变计划文件；已存在则拒绝覆盖。"""
    if os.path.islink(path) or os.path.lexists(path):
        raise AppError('状态文件已存在，拒绝覆盖: %s' % path)
    try:
        with open(path, 'x', encoding='utf-8') as handle:
            handle.write(json.dumps(obj, ensure_ascii=False, indent=2))
            handle.write('\n')
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        raise AppError('状态文件已存在，拒绝覆盖: %s' % path)
    except OSError as exc:
        raise AppError('无法写入状态文件 %s: %s' % (path, exc))


def write_json_atomic(path, obj):
    """原子更新可变的回执文件（先写临时文件再替换）。"""
    if os.path.islink(path):
        raise AppError('状态文件是符号链接，拒绝写入: %s' % path)
    directory = os.path.dirname(path)
    tmp = os.path.join(directory, '.tmp-' + os.path.basename(path))
    try:
        _dump(tmp, obj)
        os.replace(tmp, path)
    except OSError as exc:
        try:
            if os.path.lexists(tmp):
                os.remove(tmp)
        except OSError:
            pass
        raise AppError('无法写入状态文件 %s: %s' % (path, exc))
