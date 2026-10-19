#!/usr/bin/env python3
"""社区共享设施预约与取消 —— 本地回环演示服务器。

启动：
    python3 app.py --port PORT --data-dir DIR [--init-demo]

只监听 127.0.0.1；所有持久数据写入 DIR。仅使用 Python 标准库。
"""
import argparse
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import api
import auth
import db

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

STATIC_TYPES = {
    "index.html": "text/html; charset=utf-8",
    "app.js": "application/javascript; charset=utf-8",
    "style.css": "text/css; charset=utf-8",
}

MAX_BODY = 1 << 20  # 1 MiB


class Handler(BaseHTTPRequestHandler):
    server_version = "AmenityBooking/1.0"
    protocol_version = "HTTP/1.1"

    # ------------------------------------------------------------ 工具

    def log_message(self, fmt, *args):  # 保持安静，避免刷屏
        pass

    def _cookie(self, name):
        header = self.headers.get("Cookie")
        if not header:
            return None
        for part in header.split(";"):
            if "=" not in part:
                continue
            key, _, value = part.partition("=")
            if key.strip() == name:
                return value.strip()
        return None

    def _content_length(self):
        length = self.headers.get("Content-Length")
        if not length:
            return 0
        try:
            size = int(length)
        except ValueError:
            raise api.ApiError(400, "无效的 Content-Length")
        if size < 0 or size > MAX_BODY:
            raise api.ApiError(400, "请求体过大")
        return size

    def _drain_body(self):
        size = self._content_length()
        if size:
            self.rfile.read(size)

    def _read_json(self):
        size = self._content_length()
        raw = self.rfile.read(size) if size else b""
        if not raw:
            return {}
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise api.ApiError(400, "请求体必须是合法 JSON")
        if not isinstance(data, dict):
            raise api.ApiError(400, "请求体必须是 JSON 对象")
        return data

    def _send_json(self, status, payload, cookies=None):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        for name, value in (cookies or []):
            if value is None:
                self.send_header(
                    "Set-Cookie", "%s=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax" % name
                )
            else:
                self.send_header(
                    "Set-Cookie", "%s=%s; Path=/; HttpOnly; SameSite=Lax" % (name, value)
                )
        self.end_headers()
        self.wfile.write(data)

    def _send_bytes(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _serve_static(self, name):
        if name not in STATIC_TYPES:
            self._send_json(404, {"error": "文件不存在"})
            return
        path = os.path.join(STATIC_DIR, name)
        try:
            with open(path, "rb") as handle:
                body = handle.read()
        except OSError:
            self._send_json(404, {"error": "文件不存在"})
            return
        self._send_bytes(200, STATIC_TYPES[name], body)

    # ------------------------------------------------------------ 路由

    def _current_user(self):
        token = self._cookie("session")
        return auth.get_user_by_token(token), token

    def _handle(self, method):
        parsed = urlparse(self.path)
        path = parsed.path

        if method == "GET" and path == "/":
            self._serve_static("index.html")
            return
        if method == "GET" and path.startswith("/static/"):
            self._serve_static(path[len("/static/"):])
            return
        if method == "GET" and path in ("/favicon.ico",):
            self._send_json(404, {"error": "文件不存在"})
            return

        if path == "/api/" or path.startswith("/api/"):
            try:
                body = self._read_json() if method == "POST" else {}
                user, token = self._current_user()
                status, payload, cookies = api.dispatch(method, path, parse_qs(parsed.query), body, user, token)
            except api.ApiError as exc:
                status, payload, cookies = exc.status, {"error": exc.message}, []
            self._send_json(status, payload, cookies)
            return

        if method == "POST":
            # 非 API 的 POST：读掉请求体，避免 HTTP/1.1 连接错位。
            self._drain_body()
        self._send_json(404, {"error": "页面不存在"})

    def do_GET(self):
        try:
            self._handle("GET")
        except Exception:
            self._fail_safe()

    def do_POST(self):
        try:
            self._handle("POST")
        except Exception:
            self._fail_safe()

    def _fail_safe(self):
        try:
            self._send_json(500, {"error": "服务器内部错误"})
        except Exception:
            pass


class Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def parse_args(argv):
    parser = argparse.ArgumentParser(description="社区共享设施预约与取消（本地演示）")
    parser.add_argument("--port", type=int, default=8000, help="监听端口")
    parser.add_argument("--data-dir", default="./data", help="持久数据目录")
    parser.add_argument(
        "--init-demo",
        action="store_true",
        help="仅在全新数据库上补建演示账号（不会重置已有账号或记录）",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv if argv is not None else sys.argv[1:])
    if not (1 <= args.port <= 65535):
        print("端口无效", file=sys.stderr)
        return 2

    db.configure(args.data_dir)
    db.init_schema()
    if args.init_demo:
        auth.ensure_demo_users()

    server = Server(("127.0.0.1", args.port), Handler)
    print("数据目录: %s" % db.path())
    print("服务地址: http://127.0.0.1:%d/" % args.port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
