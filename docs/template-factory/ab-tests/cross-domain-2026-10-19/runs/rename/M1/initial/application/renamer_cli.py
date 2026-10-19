# -*- coding: utf-8 -*-
"""命令行入口：解析 --root 与子命令，分发到具体实现。

stdout 只输出单个 JSON 对象；帮助/错误/日志走 stderr。
操作失败时非零退出且 stdout 不输出任何 JSON。
"""

import argparse
import json
import sys

from renamer_commands import cmd_apply, cmd_list, cmd_preview, cmd_undo
from renamer_errors import AppError


def build_parser():
    parser = argparse.ArgumentParser(
        prog='app.py',
        description='单目录预览式批量重命名与撤销（Python 标准库 CLI）。',
    )
    parser.add_argument('--root', required=True, help='要整理的根目录；仅操作其立即普通文件')
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('list', help='列出根目录内的立即普通文件')

    preview = sub.add_parser('preview', help='生成旧名到新名的计划，不改动原文件')
    preview.add_argument('--find', required=True, help='非空字面查找文本（非正则）')
    preview.add_argument('--replace', required=True, help='替换文本')
    preview.add_argument('--plan', required=True, help='计划文件路径，须位于 .atlas-renamer/ 内')

    apply_cmd = sub.add_parser('apply', help='确认后按计划执行改名')
    apply_cmd.add_argument('--plan', required=True, help='preview 生成的计划路径')
    apply_cmd.add_argument('--confirm', action='store_true')

    undo = sub.add_parser('undo', help='确认后撤销一次已执行的批次')
    undo.add_argument('--receipt', required=True, help='apply 生成的回执路径')
    undo.add_argument('--confirm', action='store_true')
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == 'list':
            result = cmd_list(args.root)
        elif args.command == 'preview':
            result = cmd_preview(args.root, args.find, args.replace, args.plan)
        elif args.command == 'apply':
            result = cmd_apply(args.root, args.plan, args.confirm)
        elif args.command == 'undo':
            result = cmd_undo(args.root, args.receipt, args.confirm)
        else:
            raise AppError('未知命令: %r' % args.command)
    except AppError as exc:
        sys.stderr.write('错误: %s\n' % exc.message)
        return 1
    except OSError as exc:
        sys.stderr.write('错误: 系统错误 %s\n' % exc)
        return 1
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + '\n')
    sys.stdout.flush()
    return 0
