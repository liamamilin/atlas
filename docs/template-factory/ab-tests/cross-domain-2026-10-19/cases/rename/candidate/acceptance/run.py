#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''独立 REAL 目标验收检查器（本实验为认知模板/验收程序，非下游应用；生成阶段不执行）。

本文件是本次实验唯一的验收程序，只依赖 Python 3 标准库，不导入、不实现被测应用代码，
也不读取被测应用源码。它按固定适配契约以 shell=False 子进程调用被测应用：

    python3 <app.py> --root <fixture_root> COMMAND ...

并在一次性临时目录内自建自清理夹具（普通文件、子目录、符号链接、预置冲突目标、
根外诱饵文件/目录），绝不使用真实 Downloads/HOME 或应用源码目录。夹具内容在运行期
随机生成，不硬编码文件名或结果。判定只依据各命令 stdout 的单一 JSON 对象与退出码，
以及可观察到的文件改名/内容变化，绝不把文件或标题存在性当作行为证据。

用法：
    python3 acceptance/run.py --app /path/to/app.py [--root /disposable/root]

--app 必填，指向操作者提供的新隔离应用入口；缺失时按基础设施不完整显式失败并非零退出，
绝不回退到任何真实目录。--root 可选，给出时只在该目录下新建一个唯一子目录作为夹具父目录
并在结束时删除，不触碰该目录内其它内容；缺省时在系统临时目录创建并自清理。任何不支持的
环境或参数模式都以非零退出显式失败，绝不静默跳过或记为通过。

每个用例输出一行 ID PASS|FAIL - 说明；任一断言失败则整体退出非零。
'''

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid

STATE_DIR = '.atlas-renamer'
TIMEOUT = 60
PYTHON = sys.executable or 'python3'
SUCCESS_STATUS = ('applied', 'undone', 'preview', 'already-applied')


class InfraError(Exception):
    '''验收环境或参数不完整，必须以非零退出显式失败。'''


def rand_hex(n=8):
    return uuid.uuid4().hex[:n]


def rand_token(prefix):
    return prefix + rand_hex(10)


def rand_name(prefix='f'):
    return prefix + '_' + rand_hex(8)


def rand_bytes(lo=8, hi=64):
    span = hi - lo + 1
    size = lo + (int.from_bytes(os.urandom(2), 'big') % span)
    return os.urandom(size)


def rand_bytes_sized(n):
    return os.urandom(n)


def write_abs(path, data):
    with open(path, 'wb') as fh:
        fh.write(data)


def write_file(root, name, data):
    write_abs(os.path.join(root, name), data)


def mkdir(parent, name):
    path = os.path.join(parent, name)
    os.makedirs(path)
    return path


def make_symlink(target, link_path):
    try:
        os.symlink(target, link_path)
    except (OSError, NotImplementedError) as exc:
        raise InfraError('当前环境无法创建符号链接夹具：%s' % exc)


def fresh_root(base):
    root = os.path.join(base, 'root-' + rand_hex(10))
    os.makedirs(root)
    return root


def plan_path(root, tag='plan'):
    return os.path.join(root, STATE_DIR, tag + '-' + rand_hex(8) + '.json')


def state_dir(root):
    return os.path.join(root, STATE_DIR)


def read_regular(root):
    out = {}
    if not os.path.isdir(root):
        return out
    for entry in os.scandir(root):
        if entry.name == STATE_DIR:
            continue
        try:
            st = entry.stat(follow_symlinks=False)
        except OSError:
            continue
        if stat.S_ISREG(st.st_mode):
            try:
                with open(entry.path, 'rb') as fh:
                    out[entry.name] = fh.read()
            except OSError:
                out[entry.name] = None
    return out


def list_names(root):
    try:
        return set(os.listdir(root))
    except OSError:
        return set()


def is_within(child, parent):
    child = os.path.realpath(child)
    parent = os.path.realpath(parent)
    try:
        return os.path.commonpath([child, parent]) == parent
    except ValueError:
        return False


def resolve_returned(root, value):
    if not isinstance(value, str) or not value:
        return None
    return os.path.realpath(value if os.path.isabs(value) else os.path.join(root, value))


def parse_obj(stdout):
    if not isinstance(stdout, str):
        return None
    text = stdout.strip()
    if not text:
        return None
    try:
        obj = json.loads(text)
    except Exception:
        return None
    return obj if isinstance(obj, dict) else None


def load_json(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return json.load(fh)


def short(text, limit=200):
    if not isinstance(text, str):
        return ''
    return text.strip().replace('\n', ' ')[:limit]


def false_success(stdout):
    obj = parse_obj(stdout)
    if not isinstance(obj, dict):
        return False
    status = obj.get('status')
    return isinstance(status, str) and status in SUCCESS_STATUS


def run_app(app, root, args, env):
    cmd = [PYTHON, app, '--root', root] + list(args)
    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=root,
            env=env,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return None, '', '<超时>'
    except OSError as exc:
        raise InfraError('无法启动被测应用（%s）：%s' % (' '.join(cmd), exc))
    return proc.returncode, proc.stdout.decode('utf-8', 'replace'), proc.stderr.decode('utf-8', 'replace')


def run_preview(app, root, env, find, repl, plan):
    return run_app(app, root, ['preview', '--find', find, '--replace', repl, '--plan', plan], env)


def run_apply(app, root, env, plan, confirm=True):
    args = ['apply', '--plan', plan]
    if confirm:
        args.append('--confirm')
    return run_app(app, root, args, env)


def run_undo(app, root, env, receipt, confirm=True):
    args = ['undo', '--receipt', receipt]
    if confirm:
        args.append('--confirm')
    return run_app(app, root, args, env)


def seed_find_files(root, find, count=3):
    files = {}
    used = set()
    for _ in range(count):
        while True:
            nm = find + '_' + rand_hex(6) + '.dat'
            if nm not in used:
                break
        used.add(nm)
        data = rand_bytes(8, 100)
        write_file(root, nm, data)
        files[nm] = data
    return files


def expected_ops(names, find, repl):
    ops = []
    for nm in sorted(names):
        if find in nm:
            ops.append((nm, nm.replace(find, repl)))
    return ops


def ops_match(obj, expected):
    ops = obj.get('operations')
    if not isinstance(ops, list):
        return False
    got = []
    for item in ops:
        if not isinstance(item, dict):
            return False
        got.append((item.get('old'), item.get('new')))
    return sorted(got) == sorted(expected)


def check_plan_identity(plan_json, root, fails, ctx):
    ops = plan_json.get('operations')
    if not isinstance(ops, list):
        fails.append('[%s] 计划缺少 operations 列表' % ctx)
        return
    have_evidence = False
    for item in ops:
        if not isinstance(item, dict):
            fails.append('[%s] 计划 operation 不是对象' % ctx)
            continue
        old = item.get('old')
        if not isinstance(old, str):
            fails.append('[%s] 计划 operation 缺少 old' % ctx)
            continue
        ident = item.get('identity')
        if not isinstance(ident, dict) or not ident:
            fails.append('[%s] 计划 operation %s 缺少 identity 证据' % (ctx, old))
            continue
        path = os.path.join(root, old)
        try:
            st = os.lstat(path)
        except OSError as exc:
            fails.append('[%s] 无法 lstat 源文件 %s：%s' % (ctx, old, exc))
            continue
        if 'dev' in ident:
            have_evidence = True
            try:
                if int(ident['dev']) != st.st_dev:
                    fails.append('[%s] %s identity.dev 不符' % (ctx, old))
            except (TypeError, ValueError):
                fails.append('[%s] %s identity.dev 非整数' % (ctx, old))
        if 'ino' in ident:
            have_evidence = True
            try:
                if int(ident['ino']) != st.st_ino:
                    fails.append('[%s] %s identity.ino 不符' % (ctx, old))
            except (TypeError, ValueError):
                fails.append('[%s] %s identity.ino 非整数' % (ctx, old))
        if 'size' in ident:
            have_evidence = True
            try:
                if int(ident['size']) != st.st_size:
                    fails.append('[%s] %s identity.size 不符' % (ctx, old))
            except (TypeError, ValueError):
                fails.append('[%s] %s identity.size 非整数' % (ctx, old))
        if 'mtime_ns' in ident:
            have_evidence = True
            mtime_ns = getattr(st, 'st_mtime_ns', None)
            try:
                if mtime_ns is None or int(ident['mtime_ns']) != mtime_ns:
                    fails.append('[%s] %s identity.mtime_ns 不符' % (ctx, old))
            except (TypeError, ValueError):
                fails.append('[%s] %s identity.mtime_ns 非整数' % (ctx, old))
        if 'mtime' in ident:
            have_evidence = True
        if 'sha256' in ident:
            have_evidence = True
            try:
                with open(path, 'rb') as fh:
                    digest = hashlib.sha256(fh.read()).hexdigest()
            except OSError:
                digest = None
            if digest is None or str(ident['sha256']).lower() != digest:
                fails.append('[%s] %s identity.sha256 不符' % (ctx, old))
    if not have_evidence:
        fails.append('[%s] 计划未包含可核对的身份/内容证据' % ctx)


def verify_plan_file(plan_json, plan, root, expected, find, repl, fails, ctx):
    if not isinstance(plan_json, dict):
        fails.append('[%s] 计划文件不是 JSON 对象' % ctx)
        return
    if not is_within(plan, state_dir(root)):
        fails.append('[%s] 计划文件不在状态目录内' % ctx)
    if not ops_match(plan_json, expected):
        fails.append('[%s] 计划 operations 与预期不符' % ctx)
    if 'find' in plan_json and plan_json.get('find') != find:
        fails.append('[%s] 计划 find 字段不符' % ctx)
    if 'replace' in plan_json and plan_json.get('replace') != repl:
        fails.append('[%s] 计划 replace 字段不符' % ctx)
    check_plan_identity(plan_json, root, fails, ctx)


def case_a01(app, base, env):
    fails = []
    root = fresh_root(base)
    files = {}
    for _ in range(4):
        nm = rand_name('file')
        data = rand_bytes(5, 80)
        write_file(root, nm, data)
        files[nm] = data
    sub = rand_name('dir')
    mkdir(root, sub)
    write_file(os.path.join(root, sub), rand_name('inner'), rand_bytes(1, 20))
    link_in = rand_name('link')
    make_symlink(sorted(files)[0], os.path.join(root, link_in))
    outside_file = os.path.join(base, rand_name('decoy'))
    write_abs(outside_file, b'decoy')
    link_out = rand_name('linkout')
    make_symlink(outside_file, os.path.join(root, link_out))
    os.makedirs(os.path.join(root, STATE_DIR), exist_ok=True)
    write_file(os.path.join(root, STATE_DIR), 'state.json', b'{}')
    before_entries = set(list_names(root))

    rc, out, err = run_app(app, root, ['list'], root, env)
    if rc is None:
        fails.append('[A01] list 命令超时')
        return fails
    if rc != 0:
        fails.append('[A01] list 退出码 %r 非 0（stderr=%s）' % (rc, short(err)))
    obj = parse_obj(out)
    if obj is None:
        fails.append('[A01] list stdout 不是单一 JSON 对象')
    else:
        listing = obj.get('files')
        if not isinstance(listing, list):
            fails.append('[A01] list 缺少 files 列表')
        else:
            got = {}
            for item in listing:
                if not isinstance(item, dict) or 'name' not in item or 'size' not in item:
                    fails.append('[A01] list 条目缺少 name/size：%r' % (item,))
                    continue
                got[item['name']] = item['size']
            if set(got) != set(files):
                missing = sorted(set(files) - set(got))
                extra = sorted(set(got) - set(files))
                fails.append('[A01] list 普通文件集合不符：缺失=%s 多余=%s' % (missing, extra))
            for nm, data in files.items():
                if nm not in got:
                    continue
                try:
                    size = int(got[nm])
                except (TypeError, ValueError):
                    fails.append('[A01] 文件 %s 的 size 非整数：%r' % (nm, got[nm]))
                    continue
                if size != len(data):
                    fails.append('[A01] 文件 %s 的 size=%r 与真实 %d 不符' % (nm, got[nm], len(data)))
            if STATE_DIR in got:
                fails.append('[A01] list 不应包含内部状态目录 %s' % STATE_DIR)
            if sub in got:
                fails.append('[A01] list 不应包含子目录 %s' % sub)
            if link_in in got or link_out in got:
                fails.append('[A01] list 不应包含符号链接')
    if read_regular(root) != files:
        fails.append('[A01] list 不应改动任何普通文件')
    if set(list_names(root)) != before_entries:
        fails.append('[A01] list 不应在根目录创建或删除条目')
    return fails


def case_a02(app, base, env):
    fails = []
    root = fresh_root(base)
    find = rand_token('tk')
    repl = rand_token('rn')
    files = {}
    nm1 = find + '_' + rand_hex(6) + '.dat'
    nm2 = find + '-' + rand_hex(4) + '-' + find + '.dat'
    nm3 = rand_name('plain') + '.dat'
    files[nm1] = rand_bytes(10, 120)
    files[nm2] = rand_bytes(10, 120)
    files[nm3] = rand_bytes(10, 120)
    for nm, data in files.items():
        write_file(root, nm, data)
    pre = read_regular(root)
    expected = expected_ops(files.keys(), find, repl)
    plan = plan_path(root)

    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc is None:
        fails.append('[A02] preview 命令超时')
        return fails
    if rc != 0:
        fails.append('[A02] preview 退出码 %r 非 0（stderr=%s）' % (rc, short(err)))
    obj = parse_obj(out)
    if obj is None:
        fails.append('[A02] preview stdout 不是单一 JSON 对象')
    else:
        if obj.get('status') != 'preview':
            fails.append('[A02] preview status 字段不是 preview：%r' % obj.get('status'))
        if not ops_match(obj, expected):
            fails.append('[A02] preview operations 与预期不符')
        if resolve_returned(root, obj.get('plan')) != os.path.realpath(plan):
            fails.append('[A02] preview 返回的 plan 路径与给定路径不一致：%r' % obj.get('plan'))
    if not os.path.isfile(plan):
        fails.append('[A02] 未在状态目录内生成计划文件')
    else:
        if not is_within(plan, state_dir(root)):
            fails.append('[A02] 计划文件位于状态目录之外')
        try:
            pj = load_json(plan)
        except Exception as exc:
            pj = None
            fails.append('[A02] 计划文件不是可读 JSON：%s' % exc)
        if pj is not None:
            verify_plan_file(pj, plan, root, expected, find, repl, fails, 'A02')
    if read_regular(root) != pre:
        fails.append('[A02] 预览改动了原文件字节或文件名')
    extra = set(list_names(root)) - set(pre) - {STATE_DIR}
    if extra:
        fails.append('[A02] 预览在根目录产生非预期条目：%s' % sorted(extra))
    return fails


def _neg_case(fails, app, base, env, desc, names, find, repl):
    root = fresh_root(base)
    pre = {}
    for nm in names:
        data = rand_bytes(6, 40)
        write_file(root, nm, data)
        pre[nm] = data
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc is None:
        fails.append('[%s] 命令超时' % desc)
        return
    if rc == 0:
        fails.append('[%s] 非法输入未被拒绝（退出码 0）' % desc)
    if not err.strip():
        fails.append('[%s] 拒绝时 stderr 无错误说明' % desc)
    if false_success(out):
        fails.append('[%s] 拒绝时 stdout 输出假成功 JSON' % desc)
    if read_regular(root) != pre:
        fails.append('[%s] 拒绝时改动了文件' % desc)
    if os.path.exists(plan):
        fails.append('[%s] 拒绝时仍创建了计划文件' % desc)


def case_a03(app, base, env):
    fails = []
    tok = rand_token('tk')
    repl = rand_token('rn')
    _neg_case(fails, app, base, env, '空查找文本',
              [rand_name('f'), rand_name('g')], '', repl)
    _neg_case(fails, app, base, env, '替换串含路径分隔符',
              [tok + '_' + rand_hex(6) + '.dat', tok + '_' + rand_hex(6) + '.dat'],
              tok, 'a/b' + rand_hex(4))
    _neg_case(fails, app, base, env, '替换串含目录穿越',
              [tok + '_' + rand_hex(6) + '.dat', tok + '_' + rand_hex(6) + '.dat'],
              tok, '../' + rand_hex(4))
    solo = rand_name('solo')
    _neg_case(fails, app, base, env, '新名解析后不是单个文件名',
              [solo, rand_name('other')], solo, '..')
    return fails


def _conflict_case(fails, app, base, env, desc, files, find, repl):
    root = fresh_root(base)
    for nm, data in files.items():
        write_file(root, nm, data)
    pre = read_regular(root)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc is None:
        fails.append('[%s] preview 超时' % desc)
        return
    rejected = False
    if rc != 0:
        rejected = True
    else:
        if not os.path.isfile(plan):
            fails.append('[%s] preview 成功却未写计划文件' % desc)
        else:
            rc2, out2, err2 = run_apply(app, root, env, plan)
            if rc2 is None:
                fails.append('[%s] apply 超时' % desc)
                return
            if rc2 != 0:
                rejected = True
            else:
                fails.append('[%s] 冲突未被拒绝：apply 返回成功（stdout=%s）' % (desc, short(out2)))
    if not rejected:
        fails.append('[%s] 整批冲突未被拒绝' % desc)
    if read_regular(root) != pre:
        fails.append('[%s] 拒绝后仍有文件被改名或内容变化' % desc)


def case_a04(app, base, env):
    fails = []
    tok = rand_token('tk')
    repl = rand_token('rn')
    tail = rand_hex(6)
    tail2 = rand_hex(6)
    while tail2 == tail:
        tail2 = rand_hex(6)
    files_target = {
        tok + '_' + tail: rand_bytes(6, 40),
        repl + '_' + tail: rand_bytes(6, 40),
        tok + '_' + tail2: rand_bytes(6, 40),
    }
    _conflict_case(fails, app, base, env, '目标已存在', files_target, tok, repl)

    common = rand_name('same')
    files_same = {
        common + tok: rand_bytes(6, 40),
        common + tok + tok: rand_bytes(6, 40),
    }
    _conflict_case(fails, app, base, env, '两个源指向同一新名', files_same, tok, '')

    B = rand_token('bk')
    C = rand_token('ck')
    R = B + tok + C
    files_ring = {
        tok: rand_bytes(6, 40),
        R: rand_bytes(6, 40),
    }
    _conflict_case(fails, app, base, env, '新名落在源集合内', files_ring, tok, R)
    return fails


def case_a05(app, base, env):
    fails = []
    find = rand_token('tk')
    repl = rand_token('rn')
    root = fresh_root(base)
    files = seed_find_files(root, find, 3)
    keep = rand_name('keep')
    keep_data = rand_bytes(6, 40)
    write_file(root, keep, keep_data)
    pre = read_regular(root)
    expected = expected_ops(files.keys(), find, repl)
    plan = plan_path(root)

    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc != 0 or rc is None:
        fails.append('[A05] 前置 preview 失败（退出码 %r，stderr=%s）' % (rc, short(err)))
        return fails
    rc2, out2, err2 = run_apply(app, root, env, plan)
    if rc2 is None:
        fails.append('[A05] apply 命令超时')
        return fails
    if rc2 != 0:
        fails.append('[A05] apply 退出码 %r 非 0（stderr=%s）' % (rc2, short(err2)))
    obj2 = parse_obj(out2)
    if obj2 is None:
        fails.append('[A05] apply stdout 不是单一 JSON 对象')
    else:
        if obj2.get('status') != 'applied':
            fails.append('[A05] apply status 字段不是 applied：%r' % obj2.get('status'))
        if not ops_match(obj2, expected):
            fails.append('[A05] apply operations 与预期不符')
        receipt = obj2.get('receipt')
        if not isinstance(receipt, str) or not receipt:
            fails.append('[A05] apply 未返回 receipt 路径')
        else:
            rec_path = resolve_returned(root, receipt)
            if not is_within(rec_path, state_dir(root)):
                fails.append('[A05] 回执文件位于状态目录之外')
            if not os.path.isfile(rec_path):
                fails.append('[A05] 回执文件不存在或不可读')
            else:
                try:
                    rec = load_json(rec_path)
                except Exception as exc:
                    rec = None
                    fails.append('[A05] 回执不是可读 JSON：%s' % exc)
                if rec is not None and isinstance(rec, (dict, list)):
                    text = json.dumps(rec, ensure_ascii=False)
                    for old, new in expected:
                        if old not in text:
                            fails.append('[A05] 回执未记录旧名 %s' % old)
                        if new not in text:
                            fails.append('[A05] 回执未记录新名 %s' % new)
                elif rec is not None:
                    fails.append('[A05] 回执不是 JSON 对象或数组')
    after = read_regular(root)
    expected_map = {new: pre[old] for old, new in expected}
    if keep not in after or after[keep] != keep_data:
        fails.append('[A05] 未选文件被改动或丢失')
    for old, new in expected:
        if old in after:
            fails.append('[A05] 旧名 %s 仍存在' % old)
        if new not in after:
            fails.append('[A05] 新名 %s 不存在' % new)
        elif after[new] != pre[old]:
            fails.append('[A05] 新名 %s 的内容与源文件不一致' % new)
    extra = set(after) - set(expected_map) - {keep}
    if extra:
        fails.append('[A05] 执行后出现非预期文件：%s' % sorted(extra))
    return fails


def case_a06(app, base, env):
    fails = []
    find = rand_token('tk')
    repl = rand_token('rn')
    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc != 0 or rc is None or not os.path.isfile(plan):
        fails.append('[A06] 前置 preview 失败')
        return fails
    rc2, out2, err2 = run_apply(app, root, env, plan, confirm=False)
    if rc2 is None:
        fails.append('[A06] apply 超时')
    elif rc2 == 0:
        fails.append('[A06] 缺 --confirm 未被拒绝（退出码 0）')
    if not err2.strip():
        fails.append('[A06] 拒绝时 stderr 无错误说明')
    if false_success(out2):
        fails.append('[A06] 拒绝时 stdout 输出假成功 JSON')
    if read_regular(root) != pre:
        fails.append('[A06] 缺 --confirm 时仍改动了文件')
    return fails


def make_applied(app, base, env, fails, ctx, count=3):
    find = rand_token('tk')
    repl = rand_token('rn')
    root = fresh_root(base)
    files = seed_find_files(root, find, count)
    keep = rand_name('keep')
    keep_data = rand_bytes(6, 40)
    write_file(root, keep, keep_data)
    pre = read_regular(root)
    expected = expected_ops([n for n in pre if n != keep], find, repl)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc is None:
        fails.append('[%s] 前置 preview 超时' % ctx)
        return None
    if rc != 0:
        fails.append('[%s] 前置 preview 失败（退出码 %r，stderr=%s）' % (ctx, rc, short(err)))
        return None
    obj = parse_obj(out)
    if obj is None or obj.get('status') != 'preview':
        fails.append('[%s] 前置 preview 输出异常' % ctx)
        return None
    if not ops_match(obj, expected):
        fails.append('[%s] 前置 preview operations 与预期不符' % ctx)
        return None
    rc2, out2, err2 = run_apply(app, root, env, plan)
    if rc2 is None:
        fails.append('[%s] 前置 apply 超时' % ctx)
        return None
    if rc2 != 0:
        fails.append('[%s] 前置 apply 失败（退出码 %r，stderr=%s）' % (ctx, rc2, short(err2)))
        return None
    obj2 = parse_obj(out2)
    if obj2 is None:
        fails.append('[%s] 前置 apply 输出不是 JSON' % ctx)
        return None
    receipt = obj2.get('receipt')
    if not isinstance(receipt, str) or not receipt:
        fails.append('[%s] 前置 apply 未返回 receipt' % ctx)
        return None
    after = read_regular(root)
    return {
        'root': root,
        'pre': pre,
        'after': after,
        'expected': expected,
        'receipt': receipt,
        'plan': plan,
        'keep': keep,
    }


def case_a07(app, base, env):
    fails = []
    st = make_applied(app, base, env, fails, 'A07')
    if st is None:
        return fails
    root = st['root']
    after = st['after']
    plan = st['plan']
    rc, out, err = run_apply(app, root, env, plan)
    if rc is None:
        fails.append('[A07] 第二次 apply 超时')
        return fails
    if rc == 0:
        obj = parse_obj(out)
        status = obj.get('status') if isinstance(obj, dict) else None
        if not (isinstance(status, str) and 'already' in status.lower()):
            fails.append('[A07] 第二次 apply 返回 0 但未显式标记 already-applied（status=%r）' % status)
    if read_regular(root) != after:
        fails.append('[A07] 第二次 apply 产生了第二轮改名')
    return fails


def case_a08(app, base, env):
    fails = []
    root = fresh_root(base)
    find = rand_token('tk')
    repl = rand_token('rn')
    files = seed_find_files(root, find, 2)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc != 0 or rc is None or not os.path.isfile(plan):
        fails.append('[A08-内容] 前置 preview 失败')
        return fails
    victim = sorted(files)[0]
    write_abs(os.path.join(root, victim), files[victim] + rand_bytes_sized(16))
    pre_mod = read_regular(root)
    rc2, out2, err2 = run_apply(app, root, env, plan)
    if rc2 is None:
        fails.append('[A08-内容] apply 超时')
    elif rc2 == 0:
        fails.append('[A08-内容] 陈旧计划未被拒绝（退出码 0）')
    if not err2.strip():
        fails.append('[A08-内容] 拒绝时 stderr 无错误说明')
    if false_success(out2):
        fails.append('[A08-内容] 拒绝时 stdout 输出假成功 JSON')
    after = read_regular(root)
    if set(after) != set(pre_mod):
        fails.append('[A08-内容] 陈旧计划被拒时仍发生了改名')
    for nm in pre_mod:
        if after.get(nm) != pre_mod[nm]:
            fails.append('[A08-内容] 拒绝时文件 %s 内容被改动' % nm)

    root = fresh_root(base)
    find = rand_token('tk')
    repl = rand_token('rn')
    files = seed_find_files(root, find, 2)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc != 0 or rc is None or not os.path.isfile(plan):
        fails.append('[A08-身份] 前置 preview 失败')
        return fails
    victim = sorted(files)[0]
    os.remove(os.path.join(root, victim))
    os.makedirs(os.path.join(root, victim))
    others = {n: files[n] for n in files if n != victim}
    rc2, out2, err2 = run_apply(app, root, env, plan)
    if rc2 is None:
        fails.append('[A08-身份] apply 超时')
    elif rc2 == 0:
        fails.append('[A08-身份] 陈旧计划未被拒绝（退出码 0）')
    if not err2.strip():
        fails.append('[A08-身份] 拒绝时 stderr 无错误说明')
    if false_success(out2):
        fails.append('[A08-身份] 拒绝时 stdout 输出假成功 JSON')
    after = read_regular(root)
    if set(after) != set(others):
        fails.append('[A08-身份] 陈旧计划被拒时仍改动了其它文件')
    for nm, data in others.items():
        if after.get(nm) != data:
            fails.append('[A08-身份] 其它文件 %s 内容被改动' % nm)
    return fails


def case_a09(app, base, env):
    fails = []
    st = make_applied(app, base, env, fails, 'A09')
    if st is None:
        return fails
    root = st['root']
    pre = st['pre']
    receipt = st['receipt']
    rc, out, err = run_undo(app, root, env, receipt)
    if rc is None:
        fails.append('[A09] undo 命令超时')
        return fails
    if rc != 0:
        fails.append('[A09] undo 退出码 %r 非 0（stderr=%s）' % (rc, short(err)))
    obj = parse_obj(out)
    if obj is None:
        fails.append('[A09] undo stdout 不是单一 JSON 对象')
    elif obj.get('status') != 'undone':
        fails.append('[A09] undo status 字段不是 undone：%r' % obj.get('status'))
    after = read_regular(root)
    if after != pre:
        missing = sorted(set(pre) - set(after))
        extra = sorted(set(after) - set(pre))
        changed = sorted(nm for nm in (set(pre) & set(after)) if pre[nm] != after[nm])
        fails.append('[A09] 撤销后文件名/内容未完全恢复：缺失=%s 多余=%s 内容变化=%s'
                     % (missing, extra, changed))
    return fails


def case_a10(app, base, env):
    fails = []
    st = make_applied(app, base, env, fails, 'A10-缺确认')
    if st is not None:
        root = st['root']
        after = st['after']
        receipt = st['receipt']
        rc, out, err = run_undo(app, root, env, receipt, confirm=False)
        if rc is None or rc == 0:
            fails.append('[A10-缺确认] 缺 --confirm 未被拒绝（退出码 %r）' % rc)
        if not err.strip():
            fails.append('[A10-缺确认] 拒绝时 stderr 无错误说明')
        if false_success(out):
            fails.append('[A10-缺确认] 拒绝时 stdout 输出假成功 JSON')
        if read_regular(root) != after:
            fails.append('[A10-缺确认] 拒绝时发生了撤销改动')

    st = make_applied(app, base, env, fails, 'A10-冲突')
    if st is not None:
        root = st['root']
        after = st['after']
        receipt = st['receipt']
        old, new = st['expected'][0]
        occ = rand_bytes(4, 20)
        write_file(root, old, occ)
        rc, out, err = run_undo(app, root, env, receipt)
        if rc is None or rc == 0:
            fails.append('[A10-冲突] 撤销遇新冲突未被拒绝（退出码 %r）' % rc)
        if not err.strip():
            fails.append('[A10-冲突] 拒绝时 stderr 无错误说明')
        if false_success(out):
            fails.append('[A10-冲突] 拒绝时 stdout 输出假成功 JSON')
        now = read_regular(root)
        if now.get(old) != occ:
            fails.append('[A10-冲突] 撤销覆盖了占用旧名的新文件')
        if now.get(new) != after[new]:
            fails.append('[A10-冲突] 撤销破坏了已改名文件')

    st = make_applied(app, base, env, fails, 'A10-改动')
    if st is not None:
        root = st['root']
        after = st['after']
        receipt = st['receipt']
        old, new = st['expected'][0]
        modified = after[new] + rand_bytes_sized(16)
        write_abs(os.path.join(root, new), modified)
        rc, out, err = run_undo(app, root, env, receipt)
        if rc is None or rc == 0:
            fails.append('[A10-改动] 数据被改动时撤销未被拒绝（退出码 %r）' % rc)
        if not err.strip():
            fails.append('[A10-改动] 拒绝时 stderr 无错误说明')
        if false_success(out):
            fails.append('[A10-改动] 拒绝时 stdout 输出假成功 JSON')
        now = read_regular(root)
        if now.get(new) != modified:
            fails.append('[A10-改动] 撤销覆盖或删除了被改动数据')
        for o, n in st['expected']:
            if o not in now and n not in now:
                fails.append('[A10-改动] 撤销失败丢失了数据：%s/%s' % (o, n))
    return fails


def case_a11(app, base, env):
    fails = []
    find = rand_token('tk')
    repl = rand_token('rn')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    outside = os.path.join(base, 'out-' + rand_hex(8))
    os.makedirs(outside)
    plan_out = os.path.join(outside, 'plan.json')
    rc, out, err = run_preview(app, root, env, find, repl, plan_out)
    if rc is None:
        fails.append('[A11-越界计划] preview 超时')
    elif rc == 0:
        fails.append('[A11-越界计划] 状态目录之外的计划路径未被拒绝')
    if rc is not None and rc != 0 and not err.strip():
        fails.append('[A11-越界计划] 拒绝时 stderr 无错误说明')
    if false_success(out):
        fails.append('[A11-越界计划] 拒绝时 stdout 输出假成功 JSON')
    if os.path.exists(plan_out):
        fails.append('[A11-越界计划] 仍在状态目录之外写入了计划')
    if list_names(outside):
        fails.append('[A11-越界计划] 根外目录被写入')
    if read_regular(root) != pre:
        fails.append('[A11-越界计划] 拒绝时改动了文件')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    esc_name = 'escape-' + rand_hex(6) + '.json'
    trav = os.path.join(root, STATE_DIR, '..', esc_name)
    escape = os.path.join(root, esc_name)
    rc, out, err = run_preview(app, root, env, find, repl, trav)
    if rc is None:
        fails.append('[A11-穿越] preview 超时')
    elif rc == 0:
        fails.append('[A11-穿越] 经 .. 越出状态目录未被拒绝')
    if rc is not None and rc != 0 and not err.strip():
        fails.append('[A11-穿越] 拒绝时 stderr 无错误说明')
    if false_success(out):
        fails.append('[A11-穿越] 拒绝时 stdout 输出假成功 JSON')
    if os.path.exists(escape):
        fails.append('[A11-穿越] 越界写入了 %s' % esc_name)
    if read_regular(root) != pre:
        fails.append('[A11-穿越] 拒绝时改动了文件')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    ext = os.path.join(base, 'ext-' + rand_hex(8))
    os.makedirs(ext)
    make_symlink(ext, os.path.join(root, STATE_DIR))
    plan_sym = os.path.join(root, STATE_DIR, 'plan-' + rand_hex(6) + '.json')
    rc, out, err = run_preview(app, root, env, find, repl, plan_sym)
    if rc is None:
        fails.append('[A11-符号链接] preview 超时')
    elif rc == 0:
        fails.append('[A11-符号链接] 经外部符号链接的状态目录未被拒绝')
    if rc is not None and rc != 0 and not err.strip():
        fails.append('[A11-符号链接] 拒绝时 stderr 无错误说明')
    if false_success(out):
        fails.append('[A11-符号链接] 拒绝时 stdout 输出假成功 JSON')
    if list_names(ext):
        fails.append('[A11-符号链接] 根外目标目录被写入')
    if read_regular(root) != pre:
        fails.append('[A11-符号链接] 拒绝时改动了文件')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc == 0 and os.path.isfile(plan):
        outside = os.path.join(base, 'out-' + rand_hex(8))
        os.makedirs(outside)
        extra_plan = os.path.join(outside, 'plan.json')
        shutil.copyfile(plan, extra_plan)
        rc2, out2, err2 = run_apply(app, root, env, extra_plan)
        if rc2 is None:
            fails.append('[A11-越界执行] apply 超时')
        elif rc2 == 0:
            fails.append('[A11-越界执行] 状态目录之外的执行计划未被拒绝')
        if rc2 is not None and rc2 != 0 and not err2.strip():
            fails.append('[A11-越界执行] 拒绝时 stderr 无错误说明')
        if false_success(out2):
            fails.append('[A11-越界执行] 拒绝时 stdout 输出假成功 JSON')
        if read_regular(root) != pre:
            fails.append('[A11-越界执行] 拒绝时发生了改名')
    else:
        fails.append('[A11-越界执行] 前置 preview 失败')

    st = make_applied(app, base, env, fails, 'A11-越界撤销')
    if st is not None:
        root = st['root']
        after = st['after']
        outside = os.path.join(base, 'out-' + rand_hex(8))
        os.makedirs(outside)
        extra_rec = os.path.join(outside, 'receipt.json')
        src_rec = resolve_returned(root, st['receipt'])
        if src_rec and os.path.isfile(src_rec):
            shutil.copyfile(src_rec, extra_rec)
            rc2, out2, err2 = run_undo(app, root, env, extra_rec)
            if rc2 is None:
                fails.append('[A11-越界撤销] undo 超时')
            elif rc2 == 0:
                fails.append('[A11-越界撤销] 状态目录之外的撤销回执未被拒绝')
            if rc2 is not None and rc2 != 0 and not err2.strip():
                fails.append('[A11-越界撤销] 拒绝时 stderr 无错误说明')
            if false_success(out2):
                fails.append('[A11-越界撤销] 拒绝时 stdout 输出假成功 JSON')
            if read_regular(root) != after:
                fails.append('[A11-越界撤销] 拒绝时发生了撤销改动')
        else:
            fails.append('[A11-越界撤销] 无法定位前置回执文件')
    return fails


def case_a12(app, base, env):
    fails = []
    find = rand_token('tk')
    repl = rand_token('rn')

    root = fresh_root(base)
    files = seed_find_files(root, find, 2)
    pre = read_regular(root)
    expected = expected_ops(files.keys(), find, repl)
    plan = plan_path(root)
    rc, out, err = run_preview(app, root, env, find, repl, plan)
    if rc != 0 or rc is None or not os.path.isfile(plan):
        fails.append('[A12-执行冲突] 前置 preview 失败')
        return fails
    old0, new0 = expected[0]
    conflict_data = rand_bytes(5, 30)
    write_file(root, new0, conflict_data)
    rc2, out2, err2 = run_apply(app, root, env, plan)
    if rc2 is None:
        fails.append('[A12-执行冲突] apply 超时')
    elif rc2 == 0:
        fails.append('[A12-执行冲突] 冲突时 apply 未失败')
    if not err2.strip():
        fails.append('[A12-执行冲突] 失败时 stderr 无错误说明')
    if false_success(out2):
        fails.append('[A12-执行冲突] 失败时 stdout 输出假成功 JSON')
    now = read_regular(root)
    for nm, data in pre.items():
        if now.get(nm) != data:
            fails.append('[A12-执行冲突] 旧文件 %s 丢失或被改动' % nm)
    if now.get(new0) != conflict_data:
        fails.append('[A12-执行冲突] 冲突目标被覆盖')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    missing = plan_path(root)
    rc3, out3, err3 = run_apply(app, root, env, missing)
    if rc3 is None or rc3 == 0:
        fails.append('[A12-缺计划] 不存在的计划未被拒绝（退出码 %r）' % rc3)
    if not err3.strip():
        fails.append('[A12-缺计划] 失败时 stderr 无错误说明')
    if false_success(out3):
        fails.append('[A12-缺计划] 失败时 stdout 输出假成功 JSON')
    if read_regular(root) != pre:
        fails.append('[A12-缺计划] 失败时改动了文件')

    root = fresh_root(base)
    seed_find_files(root, find, 2)
    pre = read_regular(root)
    missing_rec = os.path.join(root, STATE_DIR, 'missing-' + rand_hex(6) + '.json')
    rc4, out4, err4 = run_undo(app, root, env, missing_rec)
    if rc4 is None or rc4 == 0:
        fails.append('[A12-缺回执] 不存在的回执未被拒绝（退出码 %r）' % rc4)
    if not err4.strip():
        fails.append('[A12-缺回执] 失败时 stderr 无错误说明')
    if false_success(out4):
        fails.append('[A12-缺回执] 失败时 stdout 输出假成功 JSON')
    if read_regular(root) != pre:
        fails.append('[A12-缺回执] 失败时改动了文件')
    return fails


def build_env(home):
    env = dict(os.environ)
    env['HOME'] = home
    env['USERPROFILE'] = home
    env['XDG_CONFIG_HOME'] = os.path.join(home, '.config')
    env['XDG_CACHE_HOME'] = os.path.join(home, '.cache')
    env['XDG_DATA_HOME'] = os.path.join(home, '.local', 'share')
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    return env


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog='acceptance/run.py',
        description='独立的 REAL 目标验收检查器（本实验为认知模板，非下游应用）。',
    )
    parser.add_argument('--app', help='操作者提供的新隔离应用入口 app.py（必填）')
    parser.add_argument('--root', help='可选的一次性夹具根目录（缺省在临时目录创建并自清理）')
    args = parser.parse_args(argv)

    if not args.app:
        print('基础设施不完整：缺少 --app 参数，必须显式提供隔离应用入口 app.py；不得回退到任何真实目录。', file=sys.stderr)
        return 2
    app = os.path.abspath(args.app)
    if not os.path.isfile(app):
        print('基础设施不完整：--app 指向的不是一个文件：%s' % args.app, file=sys.stderr)
        return 2
    if not os.access(app, os.R_OK):
        print('基础设施不完整：--app 无法读取：%s' % args.app, file=sys.stderr)
        return 2

    parent = None
    try:
        if args.root:
            base_root = os.path.abspath(args.root)
            if not os.path.isdir(base_root):
                print('基础设施不完整：--root 指向的不是一个已存在目录：%s' % args.root, file=sys.stderr)
                return 2
            if not os.access(base_root, os.W_OK):
                print('基础设施不完整：--root 不可写：%s' % args.root, file=sys.stderr)
                return 2
            parent = os.path.join(base_root, 'atlas-accept-' + rand_hex(12))
            os.makedirs(parent)
        else:
            parent = tempfile.mkdtemp(prefix='atlas-accept-')
        home = os.path.join(parent, 'home')
        os.makedirs(home)
    except OSError as exc:
        print('基础设施不完整：无法准备一次性夹具目录：%s' % exc, file=sys.stderr)
        if parent and os.path.isdir(parent):
            shutil.rmtree(parent, ignore_errors=True)
        return 2

    env = build_env(home)
    cases = [
        ('A01', 'list 仅返回立即普通文件并排除 .atlas-renamer/目录/符号链接', case_a01),
        ('A02', 'preview 生成状态目录内计划且原文件字节与文件名未改动', case_a02),
        ('A03', '空查找/含分隔符/目录穿越新名被拒且无改动', case_a03),
        ('A04', '目标已存在/两项同新名/新名落在源集合内整体拒绝且零改名', case_a04),
        ('A05', 'apply --confirm 成功并写可读回执且内容/未选文件不变', case_a05),
        ('A06', 'apply 缺 --confirm 拒绝且无改动', case_a06),
        ('A07', '重复 apply 不再改名', case_a07),
        ('A08', '预览后源内容或身份被改动导致陈旧计划被拒且无部分改名', case_a08),
        ('A09', 'undo --confirm 恢复本批旧名与内容且不影响未参与文件', case_a09),
        ('A10', '撤销缺 --confirm 及遇新冲突/数据被改动时拒绝且不覆盖', case_a10),
        ('A11', 'plan/receipt 越出 .atlas-renamer 或经外部符号链接越界被拒', case_a11),
        ('A12', '失败时非零退出、stderr 有错误说明、stdout 无假成功且旧数据不丢', case_a12),
    ]
    failed = []
    try:
        for cid, desc, func in cases:
            try:
                case_failures = func(app, parent, env)
            except InfraError as exc:
                print('基础设施不完整：%s' % exc, file=sys.stderr)
                return 2
            except Exception as exc:
                case_failures = ['检查器内部错误：%r' % exc]
            if case_failures:
                failed.append(cid)
                print('%s FAIL - %s :: %s' % (cid, desc, '; '.join(case_failures)))
            else:
                print('%s PASS - %s' % (cid, desc))
    finally:
        shutil.rmtree(parent, ignore_errors=True)

    if failed:
        print('验收失败：%d/%d 个用例未通过（%s）。' % (len(failed), len(cases), ', '.join(failed)), file=sys.stderr)
        return 1
    print('验收通过：A01-A12 全部通过（%d 个用例）。' % len(cases))
    return 0


if __name__ == '__main__':
    sys.exit(main())
