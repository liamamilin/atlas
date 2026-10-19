#!/usr/bin/env python3
"""生活待购与灵感收藏夹 —— 本地收藏工具。

启动方式：
    python3 app.py --port 8000 --data-dir ./data

只监听 127.0.0.1，所有数据保存在 --data-dir 指定的目录中。
"""

import argparse
import os
import posixpath
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import api  # noqa: E402
import storage as storage_module  # noqa: E402

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".md": "text/markdown; charset=utf-8",
    ".svg": "image/svg+xml",
}


def resolve_static(url_path):
    """把 URL 路径安全地映射到 static 目录下的文件，阻止目录穿越。"""
    relative = unquote(url_path).lstrip("/")
    if relative in ("", "/"):
        relative = "index.html"
    normalized = posixpath.normpath(relative)
    if normalized.startswith("..") or os.path.isabs(normalized):
        return None
    candidate = os.path.join(STATIC_DIR, *normalized.split("/"))
    full = os.path.abspath(candidate)
    if full != STATIC_DIR and not full.startswith(STATIC_DIR + os.sep):
        return None
    return full


class Handler(BaseHTTPRequestHandler):
    server_version = "LifeBookmarks/1.0"
    storage = None

    def log_message(self, fmt, *args):  # 保持安静，只输出到 stderr 的简洁日志
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    # -------------------------------------------------------------- 工具方法

    def _read_body(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0:
            return b""
        return self.rfile.read(length)

    def _send(self, status, headers, body):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        for key, value in headers:
            self.send_header(key, value)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ----------------------------------------------------------------- 路由

    def _serve_api(self, method, path, query, body):
        status, headers, payload = api.dispatch(self.storage, method, path, query, body)
        self._send(status, headers, api.encode(payload))

    def _serve_open(self, path):
        match = path.rsplit("/", 1)[-1]
        try:
            bookmark_id = int(match)
        except ValueError:
            return self._send(404, [("Content-Type", "text/plain; charset=utf-8")], "记录不存在")
        try:
            url = self.storage.record_open(bookmark_id)
        except storage_module.StorageError as exc:
            return self._send(404, [("Content-Type", "text/plain; charset=utf-8")], str(exc))
        return self._redirect(url)

    def _serve_static(self, path):
        full = resolve_static(path)
        if full is None or not os.path.isfile(full):
            return self._send(404, [("Content-Type", "text/plain; charset=utf-8")], "未找到该页面")
        ext = os.path.splitext(full)[1].lower()
        ctype = CONTENT_TYPES.get(ext, "application/octet-stream")
        with open(full, "rb") as handle:
            data = handle.read()
        self._send(200, [("Content-Type", ctype)], data)

    def _route(self, method):
        parts = urlsplit(self.path)
        path = parts.path
        query = parts.query
        body = self._read_body() if method in ("POST", "PUT", "PATCH") else b""
        if path.startswith("/api/"):
            return self._serve_api(method, path, query, body)
        if path == "/favicon.ico":
            return self._send(204, [], b"")
        if method == "GET" and path.startswith("/open/"):
            return self._serve_open(path)
        if method == "GET":
            return self._serve_static(path)
        return self._send(405, [("Content-Type", "text/plain; charset=utf-8")], "方法不被支持")

    def do_GET(self):
        self._route("GET")

    def do_HEAD(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def do_PUT(self):
        self._route("PUT")

    def do_PATCH(self):
        self._route("PATCH")

    def do_DELETE(self):
        self._route("DELETE")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="生活待购与灵感收藏夹")
    parser.add_argument("--port", type=int, default=8000, help="监听端口（仅本机回环地址）")
    parser.add_argument("--data-dir", default="data", help="数据存储目录")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if not (1 <= args.port <= 65535):
        sys.stderr.write("端口号必须是 1-65535 之间的整数\n")
        return 2
    try:
        store = storage_module.Storage(args.data_dir)
    except (storage_module.StorageError, OSError) as exc:
        sys.stderr.write("无法初始化数据目录：%s\n" % exc)
        return 2

    Handler.storage = store
    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    httpd.daemon_threads = True
    sys.stdout.write(
        "收藏夹已启动：http://127.0.0.1:%d/  （数据目录：%s）\n" % (args.port, store.data_dir)
    )
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.stdout.write("\n已停止。数据已保存在 %s\n" % store.data_dir)
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
