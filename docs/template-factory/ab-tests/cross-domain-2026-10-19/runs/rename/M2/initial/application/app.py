"""Entry point for the preview-based batch rename and undo CLI.

Usage: python3 app.py --root DIR COMMAND ...

stdout carries JSON only. Human-facing messages, help and errors go to stderr.
Operational failures exit nonzero and never print success JSON.
"""

import argparse
import json
import sys

from atlas_errors import AtlasError
from commands import cmd_apply, cmd_list, cmd_preview, cmd_undo


class StderrParser(argparse.ArgumentParser):
    """ArgumentParser that keeps help text off stdout."""

    def _print_message(self, message, file=None):
        if message:
            (file or sys.stderr).write(message)

    def print_help(self, file=None):
        super().print_help(sys.stderr if file is None else file)


def build_parser():
    parser = StderrParser(
        prog="app.py",
        description="预览式批量重命名与撤销（单目录，字面文本替换）",
    )
    parser.add_argument("--root", required=True, help="要整理的根目录（只处理该目录的直接普通文件）")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="列出根目录下的普通文件")

    preview = subparsers.add_parser("preview", help="预览字面替换计划，不修改原文件")
    preview.add_argument("--find", required=True, help="查找的非空字面文本")
    preview.add_argument("--replace", required=True, help="替换文本（可为空字符串）")
    preview.add_argument("--plan", required=True, help="计划保存路径，必须位于 DIR/.atlas-renamer/ 内")

    apply_parser = subparsers.add_parser("apply", help="确认后执行计划")
    apply_parser.add_argument("--plan", required=True, help="之前生成的计划路径")
    apply_parser.add_argument("--confirm", action="store_true", help="显式确认执行")

    undo = subparsers.add_parser("undo", help="确认后撤销一次已执行的重命名")
    undo.add_argument("--receipt", required=True, help="apply 返回的回执路径")
    undo.add_argument("--confirm", action="store_true", help="显式确认撤销")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            result = cmd_list(args.root)
        elif args.command == "preview":
            result = cmd_preview(args.root, args.find, args.replace, args.plan)
        elif args.command == "apply":
            result = cmd_apply(args.root, args.plan, args.confirm)
        elif args.command == "undo":
            result = cmd_undo(args.root, args.receipt, args.confirm)
        else:
            parser.error("未知命令")
            return 2
    except AtlasError as exc:
        sys.stderr.write(f"错误: {exc}\n")
        return 1
    except KeyboardInterrupt:
        sys.stderr.write("已中断\n")
        return 130

    sys.stdout.write(json.dumps(result, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
