#!/usr/bin/env python3
"""Entrypoint for the local monthly budget app.

Run:
    python3 app.py --port PORT --data-dir DIR

Binds 127.0.0.1 only and stores all durable state in DATADIR/budget.sqlite3.
"""

import argparse
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import api
import storage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

STATIC_FILES = {
    "/static/index.html": "text/html; charset=utf-8",
    "/static/app.js": "application/javascript; charset=utf-8",
    "/static/style.css": "text/css; charset=utf-8",
}


class BudgetHandler(BaseHTTPRequestHandler):
    server_version = "BudgetApp/1.0"
    protocol_version = "HTTP/1.1"
    db_path = ""

    def log_message(self, fmt, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    # -- helpers ------------------------------------------------------------
    def _write(self, status, content_type, body, extra=None):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if self.command != "HEAD" and body:
            self.wfile.write(body)

    def _read_body(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        if length <= 0:
            return b""
        return self.rfile.read(length)

    def _serve_static(self, path):
        if path in ("/", "/index.html"):
            path = "/static/index.html"
        content_type = STATIC_FILES.get(path)
        if content_type is None:
            self._write(404, "application/json; charset=utf-8", b'{"error":"not found"}')
            return
        filename = os.path.join(STATIC_DIR, os.path.basename(path))
        try:
            with open(filename, "rb") as handle:
                body = handle.read()
        except OSError:
            self._write(404, "application/json; charset=utf-8",
                        b'{"error":"static file missing"}')
            return
        self._write(200, content_type, body)

    def _handle_api(self, method):
        parsed = urlparse(self.path)
        raw_body = self._read_body() if method in ("POST", "PUT") else b""
        query = parse_qs(parsed.query)
        try:
            status, content_type, body, extra = api.dispatch(
                self.db_path, method, parsed.path, query, raw_body
            )
        except api.ApiError as exc:
            status, content_type, body, extra = api.json_response(
                exc.status, {"error": exc.message}
            )
        except Exception as exc:  # pragma: no cover - unexpected safety net
            self.log_message("unhandled error: %r", exc)
            status, content_type, body, extra = api.json_response(
                500, {"error": "服务器内部错误"}
            )
        self._write(status, content_type, body, extra)

    # -- verbs --------------------------------------------------------------
    def do_GET(self):
        path = urlparse(self.path).path
        if path.startswith("/api/"):
            self._handle_api("GET")
        else:
            self._serve_static(path)

    def do_POST(self):
        self._handle_api("POST")

    def do_PUT(self):
        self._handle_api("PUT")

    def do_DELETE(self):
        self._handle_api("DELETE")

    def do_HEAD(self):
        self.do_GET()


def build_server(port, data_dir):
    data_dir = os.path.abspath(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    db_path = storage.default_db_path(data_dir)
    storage.init_db(db_path)
    BudgetHandler.db_path = db_path
    server = ThreadingHTTPServer(("127.0.0.1", port), BudgetHandler)
    return server, db_path


def main(argv=None):
    parser = argparse.ArgumentParser(description="个人月度预算本地应用")
    parser.add_argument("--port", type=int, default=8000, help="监听端口（仅 127.0.0.1）")
    parser.add_argument("--data-dir", default=os.path.join(BASE_DIR, "data"),
                        help="所有持久化数据的目录")
    args = parser.parse_args(argv)

    server, db_path = build_server(args.port, args.data_dir)
    print("预算应用已启动: http://127.0.0.1:%d/" % args.port)
    print("数据目录: %s" % os.path.dirname(db_path))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
