"""Small stdlib HTTP/HTML helpers, vendored into each standalone trial app."""

from contextlib import contextmanager
import html
from http.server import BaseHTTPRequestHandler
import json
import sqlite3
from urllib.parse import parse_qs, urlsplit


class Error(ValueError):
    def __init__(self, code, message, status=400):
        super().__init__(message)
        self.code, self.message, self.status = code, message, status


def h(value):
    return html.escape(str(value if value is not None else ""), quote=True)


@contextmanager
def connect(path):
    con = sqlite3.connect(path, timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    try:
        with con:
            yield con
    finally:
        con.close()


def options(items, current=""):
    return "".join(
        f'<option value="{h(value)}"{" selected" if str(value) == str(current) else ""}>{h(label)}</option>'
        for value, label in items
    )


CSS = """
+:root{--ink:#243a35;--muted:#73827b;--accent:#285c4c;--line:#dce4dd;--bg:#f3f6f0;--paper:#fffefa;color-scheme:light}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}header{background:var(--paper);border-bottom:1px solid var(--line)}.top,main{max-width:1260px;margin:auto;padding:20px 28px}.top{display:flex;justify-content:space-between;align-items:center}.brand{font-size:20px;font-weight:750}.badge{font-size:12px;color:var(--muted);border:1px solid var(--line);border-radius:20px;padding:4px 10px}main{padding-top:30px;padding-bottom:70px}h1{font-size:32px;margin:0 0 8px;letter-spacing:-1px}h2{font-size:18px;margin:0 0 15px}h3{font-size:16px}.muted{font-size:13px;color:var(--muted)}.intro{margin-bottom:24px}.panel{background:var(--paper);border:1px solid var(--line);border-radius:15px;padding:22px;margin-bottom:18px}.grid{display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:24px;align-items:start}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:22px}.metric{padding:18px;background:var(--paper);border:1px solid var(--line);border-radius:12px}.metric strong{display:block;font-size:25px;margin:8px 0 2px}.metric small{color:var(--muted)}button,.button{cursor:pointer;border:1px solid var(--line);border-radius:8px;padding:9px 13px;background:#fffefa;color:var(--ink);font:inherit;display:inline-block}button:hover,.button:hover{background:#e8eee5}.primary{background:var(--accent);border-color:var(--accent);color:white}.primary:hover{background:#1b493b}input,textarea,select{width:100%;padding:10px 12px;font:inherit;border:1px solid #cbd6cc;border-radius:8px;background:white;color:var(--ink)}textarea{resize:vertical}input:focus,textarea:focus,select:focus{outline:2px solid #8aa88e;outline-offset:2px}label{display:block;font-size:13px;font-weight:600;margin-bottom:5px}.field{margin-bottom:14px}.inline{display:flex;gap:10px;align-items:end;flex-wrap:wrap}.inline .field{flex:1;margin:0;min-width:100px}.inline input,.inline select{min-width:100px}.row{display:flex;gap:12px;align-items:center;justify-content:space-between}.notice{padding:12px 16px;background:#e2efdf;border-radius:10px;margin:16px 0}.error{background:#fff0e9;color:#923c21}.negative{color:#b04125!important}.positive{color:#2b6650}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:12px 8px;text-align:left;border-bottom:1px solid var(--line);vertical-align:middle}th{font-size:12px;color:var(--muted);font-weight:500}.amount{text-align:right;font-variant-numeric:tabular-nums}.small-input{width:110px;padding:6px 8px}.empty{text-align:center;border:1px dashed #c6d2c3;border-radius:12px;padding:35px 20px;color:var(--muted)}.note-card{display:block;color:var(--ink);border:1px solid var(--line);border-radius:12px;background:var(--paper);padding:18px;margin:12px 0}.note-card:hover{text-decoration:none;border-color:#9bb79d}.note-title{font-size:18px;font-weight:650}.preview{color:var(--muted);font-size:13px;white-space:pre-wrap;overflow-wrap:anywhere}.pill{display:inline-block;padding:3px 9px;border-radius:15px;background:#e6eddf;font-size:11px}.body-text{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;line-height:1.9;margin:20px 0}.sidebar a{display:block;padding:9px 12px;border-radius:8px;margin:4px 0}.sidebar .active{background:#e3ecdd;font-weight:600}.notes-layout{display:grid;grid-template-columns:170px minmax(0,1fr) 300px;gap:24px}.footer{margin-top:24px;color:var(--muted);font-size:12px}.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}@media(max-width:1000px){.grid{grid-template-columns:1fr}.notes-layout{grid-template-columns:150px 1fr}.quick{grid-column:2}.cards{grid-template-columns:repeat(2,1fr)}}@media(max-width:650px){main,.top{padding:18px 14px}.notes-layout{display:block}.sidebar{display:flex;flex-wrap:wrap;gap:2px}.cards{gap:8px}.metric{padding:12px}.metric strong{font-size:20px}.panel{padding:16px}h1{font-size:27px}.table-wrap{overflow:auto}.badge{font-size:10px}}
+""".replace("\n+", "\n")


def page(title, subtitle, content):
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{h(title)}</title><style>{CSS}</style></head><body><header><div class="top"><a class="brand" href="/">{h(title)}</a><span class="badge">本机保存 · 辅助试用版</span></div></header><main><div class="intro"><h1>{h(subtitle)}</h1></div>{content}<p class="footer">源自 Atlas 场景与固定开源案例 · SQLite 本机持久化 · Codex 辅助实现</p></main></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def send(self, status, body, content="text/html; charset=utf-8", headers=None):
        raw = body.encode()
        self.send_response(status)
        for key, value in {
            "Content-Type": content,
            "Content-Length": str(len(raw)),
            "Cache-Control": "no-store",
            "Referrer-Policy": "same-origin",
            "X-Content-Type-Options": "nosniff",
            "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'",
            **(headers or {}),
        }.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(raw)

    def json(self, status, value):
        self.send(
            status,
            json.dumps(value, ensure_ascii=False),
            "application/json; charset=utf-8",
        )

    def redirect(self, path):
        self.send(303, "", headers={"Location": path})

    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def handle_request(self, method):
        self.route = urlsplit(self.path).path
        self.query = {
            k: v[-1]
            for k, v in parse_qs(
                urlsplit(self.path).query, keep_blank_values=True
            ).items()
        }
        self.data = {}
        try:
            host = self.headers.get("Host", "")
            if host not in (
                f"127.0.0.1:{self.server.server_port}",
                f"localhost:{self.server.server_port}",
            ):
                raise Error("bad_request", "请通过本机地址打开应用。", 403)
            origin = self.headers.get("Origin")
            if origin and origin != "http://" + host:
                raise Error("bad_request", "请从本应用页面提交。", 403)
            if method == "POST":
                try:
                    size = int(self.headers.get("Content-Length", "0"))
                    if size < 0 or size > 1024 * 1024:
                        raise ValueError()
                    raw = self.rfile.read(size).decode()
                    if (
                        self.headers.get("Content-Type", "").split(";")[0]
                        == "application/json"
                    ):
                        self.data = json.loads(raw)
                        if not isinstance(self.data, dict):
                            raise ValueError()
                    else:
                        self.data = {
                            k: v[-1]
                            for k, v in parse_qs(raw, keep_blank_values=True).items()
                        }
                except (ValueError, UnicodeError):
                    raise Error(
                        "bad_request", "提交内容无法解析，请检查后重试。"
                    ) from None
            self.dispatch(method)
        except Error as error:
            if self.route.startswith("/api/"):
                self.json(
                    error.status,
                    {"error": {"code": error.code, "message": error.message}},
                )
            else:
                self.send(error.status, self.error_page(error))
        except sqlite3.Error:
            self.log_error("Storage operation failed")
            error = Error(
                "storage_unavailable",
                "暂时无法读写数据，请检查数据目录权限或磁盘空间。",
                503,
            )
            if self.route.startswith("/api/"):
                self.json(
                    503, {"error": {"code": error.code, "message": error.message}}
                )
            else:
                self.send(503, self.error_page(error))
