#!/usr/bin/env python3
"""社区共享设施的预约与取消 —— 回环本地实验应用入口。

启动：
    python3 app.py --port PORT --data-dir DIR [--init-demo]

仅绑定 127.0.0.1；全部持久数据（SQLite 文件）位于 --data-dir 内。
--init-demo 仅在缺少演示账号时补建，绝不重置既有账户或记录。
"""
import argparse
import os
import sys
from http.server import ThreadingHTTPServer

import auth
import db
from api import AtlasHandler


class AtlasServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, handler, db_path):
        self.db_path = db_path
        super().__init__(address, handler)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="app.py",
        description="社区共享设施预约与取消（回环本地实验）",
    )
    parser.add_argument("--port", type=int, required=True, help="回环监听端口")
    parser.add_argument("--data-dir", required=True, help="持久数据目录（SQLite 所在）")
    parser.add_argument("--init-demo", action="store_true",
                        help="在空库中补建本地演示账号 admin/alice/bob")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not (1 <= args.port <= 65535):
        print("端口必须在 1..65535 之间", file=sys.stderr)
        return 2

    data_dir = os.path.abspath(args.data_dir)
    os.makedirs(data_dir, exist_ok=True)
    path = db.db_path(data_dir)
    db.initialize(path)

    if args.init_demo:
        conn = db.connect(path)
        try:
            auth.seed_demo_users(conn)
        finally:
            conn.close()

    server = AtlasServer(("127.0.0.1", args.port), AtlasHandler, path)
    print("trial-booking 已启动：http://127.0.0.1:%d （数据目录：%s）"
          % (args.port, data_dir), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
