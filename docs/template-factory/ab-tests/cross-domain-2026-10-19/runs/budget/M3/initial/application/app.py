#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""个人月度预算与消费前剩余额度 —— 本地单机服务入口。

用法：
    python3 app.py --port PORT --data-dir DIR

仅绑定 127.0.0.1；所有持久化数据只写入 --data-dir。无第三方依赖。
"""

import argparse
import os
import sys
from http.server import ThreadingHTTPServer

from api import make_handler
from db import Store

HOST = "127.0.0.1"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="个人月度预算与消费前剩余额度（本地单机，仅绑定 127.0.0.1）")
    parser.add_argument("--port", type=int, default=8000,
                        help="监听端口，默认 8000（仅 127.0.0.1）")
    parser.add_argument("--data-dir", required=True,
                        help="持久化数据目录；数据库文件只写入此目录")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    data_dir = os.path.abspath(os.path.expanduser(args.data_dir))
    os.makedirs(data_dir, exist_ok=True)
    db_path = os.path.join(data_dir, "budget.sqlite3")
    store = Store(db_path)

    static_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "static")
    handler = make_handler(store, static_dir)

    httpd = ThreadingHTTPServer((HOST, args.port), handler)
    httpd.daemon_threads = True
    print("预算应用已启动：http://%s:%d/ （数据目录：%s）"
          % (HOST, args.port, data_dir), flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
