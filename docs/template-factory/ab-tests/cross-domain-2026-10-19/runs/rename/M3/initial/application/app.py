#!/usr/bin/env python3
"""Preview-able, undoable single-directory batch renamer (stdlib only).

Usage:
    python3 app.py --root DIR list
    python3 app.py --root DIR preview --find TEXT --replace TEXT --plan PATH [--hash]
    python3 app.py --root DIR apply   --plan PATH --confirm
    python3 app.py --root DIR undo    --receipt PATH --confirm

stdout is exactly one JSON object on success. Refusals and failures exit
nonzero and print a message on stderr; no success JSON is ever emitted on
failure. Only immediate ordinary files inside DIR are touched; DIR and
DIR/.atlas-renamer are defined by the root the operator explicitly passes.
"""

import argparse
import json
import sys

from errors import AppError
from execution import apply_plan
from listing import list_payload
from paths import ensure_state_dir, resolve_root, resolve_state_file
from planning import build_plan
from reversal import undo_receipt
from state import write_new_json


def build_parser():
    parser = argparse.ArgumentParser(
        prog="app.py",
        description="单目录预览式批量重命名与撤销：字面查找替换、显式确认、可撤销。",
    )
    parser.add_argument("--root", required=True, help="明确指定的本地根目录（仅操作其内立即普通文件）")
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    sub.add_parser("list", help="列出根目录下的立即普通文件")

    preview = sub.add_parser("preview", help="生成旧名到新名的计划（不改动原文件）")
    preview.add_argument("--find", required=True, help="非空字面查找文本（非正则）")
    preview.add_argument("--replace", required=True, help="替换文本（不含路径分隔符）")
    preview.add_argument("--plan", required=True, help="计划文件路径（必须位于 .atlas-renamer 内）")
    preview.add_argument("--hash", action="store_true", dest="hash_contents",
                         help="额外记录 sha256 内容证据（默认只记元数据）")

    apply_cmd = sub.add_parser("apply", help="执行计划（必须显式 --confirm）")
    apply_cmd.add_argument("--plan", required=True)
    apply_cmd.add_argument("--confirm", action="store_true")

    undo_cmd = sub.add_parser("undo", help="撤销本批次改名（必须显式 --confirm）")
    undo_cmd.add_argument("--receipt", required=True)
    undo_cmd.add_argument("--confirm", action="store_true")

    return parser


def run(args):
    root_real = resolve_root(args.root)

    if args.command == "list":
        return list_payload(root_real)

    if args.command == "preview":
        plan_path = resolve_state_file(root_real, args.plan)
        plan = build_plan(root_real, args.find, args.replace, args.hash_contents)
        ensure_state_dir(root_real)
        write_new_json(plan_path, plan)
        return {
            "status": "preview",
            "operations": [{"old": op["old"], "new": op["new"]} for op in plan["operations"]],
            "plan": plan_path,
        }

    if args.command == "apply":
        return apply_plan(root_real, args.plan, args.confirm)

    if args.command == "undo":
        return undo_receipt(root_real, args.receipt, args.confirm)

    raise AppError("未知命令：%s" % args.command)


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        payload = run(args)
    except AppError as exc:
        print("错误：%s" % exc, file=sys.stderr)
        return 1
    except OSError as exc:
        print("操作失败：%s" % exc, file=sys.stderr)
        return 1
    except Exception as exc:  # last-resort guard: never fabricate success
        print("未预期错误：%r" % exc, file=sys.stderr)
        return 1
    sys.stdout.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
