#!/usr/bin/env python3
"""生活待购与灵感收藏夹 —— 本地单用户书签收藏夹入口。

用法：
    python3 app.py --port PORT --data-dir DIR

仅绑定 127.0.0.1；全部持久数据写入 DIR（SQLite：DIR/app.sqlite3）。
仅使用 Python 3 标准库，无需安装任何依赖。
"""

import argparse
import os
import sys
from http.server import ThreadingHTTPServer

import server as app_server


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="app.py",
        description="生活待购与灵感收藏夹（本地、仅回环、数据存于 --data-dir）",
    )
    parser.add_argument("--port", type=int, default=8080, help="监听端口（默认 8080）")
    parser.add_argument(
        "--data-dir",
        dest="data_dir",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"),
        help="数据目录（不存在时创建）",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if not (1 <= args.port <= 65535):
        sys.stderr.write("端口不合法：%s\n" % args.port)
        return 2

    store = app_server.configure(args.data_dir)
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), app_server.AppHandler)
    httpd.daemon_threads = True

    sys.stderr.write(
        "已在 http://127.0.0.1:%d/ 启动；数据目录：%s\n" % (args.port, store.data_dir)
    )
    sys.stderr.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stderr.write("\n收到中断，正在停止……\n")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
