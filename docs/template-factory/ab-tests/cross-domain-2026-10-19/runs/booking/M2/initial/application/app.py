#!/usr/bin/env python3
"""社区共享设施预约 —— 回环本地演示应用（CPython 3.10 标准库 + SQLite）。

启动：
    python3 app.py --port PORT --data-dir DIR [--init-demo]

只绑定 127.0.0.1；全部持久数据落在 DIR 内的 booking.sqlite3。
GET / 返回中文 UI，与 JSON API 共享同一真实状态；无外部网络、遥测或安装。
"""

import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

import api
import db

APP_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROUTES = {
    '/': ('index.html', 'text/html; charset=utf-8'),
    '/index.html': ('index.html', 'text/html; charset=utf-8'),
    '/app.js': ('app.js', 'application/javascript; charset=utf-8'),
    '/style.css': ('style.css', 'text/css; charset=utf-8'),
}

DEMO_ACCOUNTS = (
    {'username': 'admin', 'password': 'AtlasDemo-Admin-9!', 'role': 'admin'},
    {'username': 'alice', 'password': 'AtlasDemo-Alice-9!', 'role': 'resident'},
    {'username': 'bob', 'password': 'AtlasDemo-Bob-9!', 'role': 'resident'},
)


class AppHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'TrialBooking/1.0'

    # -- 路由 -------------------------------------------------------------
    def do_GET(self):
        parsed = urlsplit(self.path)
        static = STATIC_ROUTES.get(parsed.path)
        if static is not None:
            self._serve_static(*static)
            return
        self._handle_api('GET', parsed, None)

    def do_POST(self):
        parsed = urlsplit(self.path)
        body = self._read_json_body()
        if body is _INVALID:
            self._send_json(400, {'error': '请求体不是合法 JSON'})
            return
        self._handle_api('POST', parsed, body)

    def do_HEAD(self):
        self.send_error(405, 'Method Not Allowed')

    # -- API 分发 ---------------------------------------------------------
    def _handle_api(self, method, parsed, body):
        token = _session_token(self.headers.get('Cookie'))
        query = parse_qs(parsed.query, keep_blank_values=True)
        try:
            result = api.handle_request(self.server.db_path, method, parsed.path, query, body, token)
        except api.ApiError as exc:
            self._send_json(exc.status, {'error': exc.message})
        except Exception:
            self._send_json(500, {'error': '服务器内部错误'})
        else:
            self._send_json(result.status, result.data, result.set_cookie)

    # -- 传输 -------------------------------------------------------------
    def _read_json_body(self):
        length = self.headers.get('Content-Length')
        try:
            length = int(length) if length else 0
        except ValueError:
            return _INVALID
        if length <= 0:
            return None
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return _INVALID

    def _send_json(self, status, payload, set_cookie=None):
        data = json.dumps(payload if payload is not None else {}, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        if set_cookie:
            self.send_header('Set-Cookie', set_cookie)
        self.end_headers()
        self.wfile.write(data)

    def _serve_static(self, filename, content_type):
        path = os.path.join(APP_DIR, filename)
        try:
            with open(path, 'rb') as handle:
                data = handle.read()
        except OSError:
            self._send_json(500, {'error': '资源不可用'})
            return
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):  # 保持 stdout 干净，不打印访问日志
        return


_INVALID = object()


class AppServer(ThreadingHTTPServer):
    """并发重叠预约需要同时到达的连接，放宽监听队列避免握手被丢弃。"""

    daemon_threads = True
    request_queue_size = 128

    def __init__(self, address, handler, db_path):
        super().__init__(address, handler)
        self.db_path = db_path


def _session_token(cookie_header):
    if not cookie_header:
        return None
    for part in cookie_header.split(';'):
        name, _, value = part.strip().partition('=')
        if name == 'session':
            return value
    return None


def build_parser():
    parser = argparse.ArgumentParser(description='社区共享设施预约（回环本地演示）')
    parser.add_argument('--port', type=int, default=8000, help='监听端口（默认 8000）')
    parser.add_argument('--data-dir', default=os.path.join(APP_DIR, 'data'),
                        help='持久数据目录（默认 ./data）')
    parser.add_argument('--init-demo', action='store_true',
                        help='仅在空库初始化合成演示账号；绝不重置既有数据')
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not (1 <= args.port <= 65535):
        print('端口超出范围', file=sys.stderr)
        return 2

    db_path = db.ensure_data_dir(args.data_dir)
    db.init_db(db_path)
    if args.init_demo:
        created = db.seed_demo_users(db_path, DEMO_ACCOUNTS)
        if created:
            print('已初始化演示账号：admin / alice / bob', file=sys.stderr)

    server = AppServer(('127.0.0.1', args.port), AppHandler, db_path)
    print('预约服务已启动：http://127.0.0.1:%d （数据目录：%s）'
          % (args.port, os.path.dirname(db_path)), file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
