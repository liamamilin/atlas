"""Synthetic two-origin probe only; never imports or launches application code."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
from threading import Thread

fixture_url = os.environ["FIXTURE_URL"]

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        body = (
            "<!doctype html><title>Synthetic bookmark probe</title>"
            "<h1>Synthetic bookmark probe</h1>"
            f'<a id="original" href="{fixture_url}">Open original fixture</a>'
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/persist":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        payload = self.rfile.read(length)
        Path("/data/probe-marker").write_bytes(payload)
        self.send_response(201)
        self.end_headers()
        self.wfile.write(b"stored")

    def log_message(self, fmt, *args):
        print("app: " + fmt % args, flush=True)

class FixtureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/original":
            self.send_error(404)
            return
        body = b"<!doctype html><title>Local original fixture</title><h1>Local original fixture page</h1>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("fixture: " + fmt % args, flush=True)

fixture_server = ThreadingHTTPServer(("0.0.0.0", 8001), FixtureHandler)
Thread(target=fixture_server.serve_forever, daemon=True).start()
ThreadingHTTPServer(("0.0.0.0", 8000), AppHandler).serve_forever()
