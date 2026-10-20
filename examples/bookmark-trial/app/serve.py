#!/usr/bin/env python3
"""Local, single-user bookmark library. Python standard library only."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import ipaddress
import json
from pathlib import Path
import re
import sqlite3
import time
from urllib.parse import parse_qs, urlencode, urlsplit
import uuid


class InputError(Exception):
    def __init__(self, code, message, field="", status=400):
        self.code, self.message, self.field, self.status = code, message, field, status


def escape(value):
    return html.escape(str(value if value is not None else ""), quote=True)


def valid_name(value, field="name"):
    if not isinstance(value, str) or not value.strip() or len(value) > 120:
        code = "invalid_name" if field == "name" else "invalid_category"
        raise InputError(code, "分类名称不能为空，且不能超过120个字符。", field)
    return value.strip()


def hostname(value):
    try:
        if not isinstance(value, str) or not value or re.search(r"[\s\x00-\x1f\x7f\\]", value):
            raise ValueError()
        parts = urlsplit(value)
        host = parts.hostname
        if parts.scheme.lower() not in ("http", "https") or not host:
            raise ValueError()
        _ = parts.port  # Reject malformed ports, without rewriting the submitted URL.
        try:
            ipaddress.ip_address(host)
        except ValueError:
            ascii_host = host.encode("idna").decode()
            if len(ascii_host) > 253 or not all(
                re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?", label)
                for label in ascii_host.rstrip(".").split(".")
            ):
                raise ValueError()
        return host.lower()
    except (ValueError, UnicodeError):
        raise InputError("invalid_url", "请输入完整的 http:// 或 https:// 网页链接（域名不能包含空格）。", "url") from None


class Library:
    def __init__(self, directory, demo=False):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "bookmarks.sqlite3"
        with self.connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS schema_meta(version INTEGER);
                CREATE TABLE IF NOT EXISTS categories(
                    id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE COLLATE NOCASE,
                    is_default INTEGER NOT NULL DEFAULT 0, position INTEGER NOT NULL,
                    created_at INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS bookmarks(
                    id TEXT PRIMARY KEY, url TEXT NOT NULL, hostname TEXT NOT NULL,
                    title TEXT, description TEXT, category_id TEXT NOT NULL REFERENCES categories(id),
                    favicon_url TEXT, created_at INTEGER NOT NULL, updated_at INTEGER NOT NULL,
                    trashed_at INTEGER);
                CREATE INDEX IF NOT EXISTS by_category ON bookmarks(category_id);
                CREATE INDEX IF NOT EXISTS by_created ON bookmarks(created_at);
                CREATE INDEX IF NOT EXISTS by_host ON bookmarks(hostname);
            """)
            fresh = db.execute("SELECT version FROM schema_meta").fetchone() is None
            if fresh:
                for i, name in enumerate(("未整理", "待购", "家居改造", "以后看看")):
                    db.execute("INSERT INTO categories VALUES(?,?,?,?,?)", (uuid.uuid4().hex, name, int(i == 0), i, time.time_ns()))
                db.execute("INSERT INTO schema_meta VALUES(1)")
                if demo:
                    for url, title, description, category in (
                        ("https://www.python.org/", "[演示] Python 官方网站", "这是一条演示书签，可以移入回收站。", "以后看看"),
                        ("https://example.com/?idea=reading", "[演示] 留给下次的灵感", "试试搜索“灵感”，或移动到自己的分类。", "未整理"),
                    ):
                        self.save(db, {"url": url, "title": title, "description": description, "category": category})

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def categories(db):
        return [dict(row) for row in db.execute("""SELECT c.*, COUNT(b.id) AS count
            FROM categories c LEFT JOIN bookmarks b ON b.category_id=c.id AND b.trashed_at IS NULL
            GROUP BY c.id ORDER BY c.position, c.created_at, c.id""")]

    @staticmethod
    def category(db, value=None, *, required=False):
        if value is None and not required:
            return db.execute("SELECT * FROM categories WHERE is_default=1").fetchone()
        name = valid_name(value, "category")
        row = db.execute("SELECT * FROM categories WHERE name=? COLLATE NOCASE", (name,)).fetchone()
        if row is None:
            identifier = uuid.uuid4().hex
            db.execute("INSERT INTO categories VALUES(?,?,0,100,?)", (identifier, name, time.time_ns()))
            row = db.execute("SELECT * FROM categories WHERE id=?", (identifier,)).fetchone()
        return row

    @staticmethod
    def record(db, identifier):
        row = db.execute("SELECT * FROM bookmarks WHERE id=?", (identifier,)).fetchone()
        if row is None:
            raise InputError("not_found", "这条收藏不存在。", "record_id", 404)
        return dict(row)

    @staticmethod
    def records(db, category="", q="", include=False, trash=False):
        rows = db.execute("""SELECT b.*, c.name AS category FROM bookmarks b
            JOIN categories c ON c.id=b.category_id ORDER BY b.created_at DESC, b.id ASC""")
        return [dict(row) for row in rows
                if (not trash or row["trashed_at"] is not None)
                and (include or row["trashed_at"] is None)
                and (not category or row["category_id"] == category or row["category"].casefold() == category.casefold())
                and (not q or any(q.casefold() in (row[key] or "").casefold() for key in ("title", "hostname", "description")))]

    def save(self, db, data):
        url = data.get("url")
        host = hostname(url)
        title, description = data.get("title"), data.get("description")
        if any(value is not None and not isinstance(value, str) for value in (title, description)):
            raise InputError("bad_request", "标题和描述应为文字。")
        category = self.category(db, data.get("category"))
        identifier, at = uuid.uuid4().hex, time.time_ns()
        db.execute("INSERT INTO bookmarks VALUES(?,?,?,?,?,?,NULL,?,?,NULL)",
                   (identifier, url, host, title, description, category["id"], at, at))
        return self.record(db, identifier)

    def update(self, db, identifier, action, data):
        old = self.record(db, identifier)
        if action == "move":
            category = self.category(db, data.get("category"), required=True)
            db.execute("UPDATE bookmarks SET category_id=?,updated_at=? WHERE id=?", (category["id"], time.time_ns(), identifier))
        elif action in ("delete", "restore"):
            db.execute("UPDATE bookmarks SET trashed_at=?,updated_at=? WHERE id=?",
                       (time.time_ns() if action == "delete" else None, time.time_ns(), identifier))
        elif action == "patch":
            url = data.get("url", old["url"])
            host = hostname(url)
            category = self.category(db, data["category"]) if "category" in data else {"id": old["category_id"]}
            title, description = data.get("title", old["title"]), data.get("description", old["description"])
            if any(value is not None and not isinstance(value, str) for value in (title, description)):
                raise InputError("bad_request", "标题和描述应为文字。")
            db.execute("UPDATE bookmarks SET url=?,hostname=?,title=?,description=?,category_id=?,updated_at=? WHERE id=?",
                       (url, host, title, description, category["id"], time.time_ns(), identifier))
        return self.record(db, identifier)

    def change_category(self, db, action, data, identifier=None):
        if action == "create":
            name = valid_name(data.get("name"))
            if db.execute("SELECT 1 FROM categories WHERE name=? COLLATE NOCASE", (name,)).fetchone():
                raise InputError("duplicate_category", "这个分类名称已存在，请换一个名称。", "name", 409)
            return dict(self.category(db, name))
        row = db.execute("SELECT * FROM categories WHERE id=?", (identifier,)).fetchone()
        if row is None:
            raise InputError("not_found", "这个分类不存在。", "category_id", 404)
        if row["is_default"]:
            raise InputError("protected_category", "“未整理”是默认分类，不能重命名或删除。", "category_id")
        if action == "rename":
            name = valid_name(data.get("name"))
            if db.execute("SELECT 1 FROM categories WHERE name=? COLLATE NOCASE AND id!=?", (name, identifier)).fetchone():
                raise InputError("duplicate_category", "这个分类名称已存在，请换一个名称。", "name", 409)
            db.execute("UPDATE categories SET name=? WHERE id=?", (name, identifier))
        else:
            default = self.category(db)
            db.execute("UPDATE bookmarks SET category_id=? WHERE category_id=?", (default["id"], identifier))
            db.execute("DELETE FROM categories WHERE id=?", (identifier,))
        return {"id": identifier, "ok": True}


STYLE = """
:root{color-scheme:light;--ink:#24392f;--muted:#68786e;--line:#dbe2d8;--paper:#fffefa;--green:#254e3e}
*{box-sizing:border-box}body{margin:0;background:#f3f5ef;color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}
a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}button,input,select,textarea{font:inherit}button,a.button{cursor:pointer;border:1px solid var(--line);border-radius:9px;padding:8px 14px;background:var(--paper);color:var(--ink);display:inline-block}button:hover,a.button:hover{background:#eaf0e4}button.primary{background:var(--green);color:white;border-color:var(--green)}input,select,textarea{border:1px solid #ccd6c9;border-radius:8px;padding:10px 12px;background:#fff;color:var(--ink);width:100%}input:focus,textarea:focus,select:focus{outline:2px solid #88a88a;outline-offset:2px}label{display:block;font-size:13px;font-weight:600;margin-bottom:5px}header{border-bottom:1px solid var(--line);background:var(--paper)}.top{max-width:1280px;margin:auto;padding:18px 32px;display:flex;align-items:center;justify-content:space-between;gap:16px}.brand{font-size:18px;font-weight:700;letter-spacing:1px}.brand span{color:#78925e}.tag{font-size:12px;color:var(--muted);border:1px solid var(--line);padding:3px 10px;border-radius:20px}main{max-width:1280px;margin:auto;padding:36px 32px 60px}.eyebrow{font-size:11px;letter-spacing:2px;color:var(--muted);font-weight:700}h1{font-size:32px;letter-spacing:-1px;margin:6px 0}h2{font-size:19px;margin:0 0 18px}p{margin:7px 0}.muted{color:var(--muted);font-size:13px}.intro{margin-bottom:28px}.layout{display:grid;grid-template-columns:175px minmax(0,1fr) 300px;gap:22px;align-items:start}.panel{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:22px}.side a{display:flex;justify-content:space-between;padding:9px 12px;border-radius:9px;margin:4px 0;font-size:14px}.side a.active{background:#e3ebdb;font-weight:600}.side .section{margin:22px 12px 8px}.count{font-size:12px;color:var(--muted)}.save{position:sticky;top:22px}.field{margin:14px 0}.save button{width:100%;margin-top:8px}.search{display:grid;grid-template-columns:1fr 145px auto;gap:8px;margin-bottom:20px}.search label{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}.summary{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;font-size:13px;color:var(--muted)}table{width:100%;border-collapse:separate;border-spacing:0 12px;table-layout:fixed}td{padding:20px;border:1px solid var(--line);border-radius:14px;background:var(--paper);overflow-wrap:anywhere}.host{font-size:11px;letter-spacing:1px;color:var(--muted);margin-bottom:5px}.record-title{font-size:18px;font-weight:650;display:block;margin-bottom:5px}.record-description{font-size:13px;color:var(--muted);margin-bottom:12px;white-space:pre-wrap}.record-url{font-size:11px;color:#839083;word-break:break-all}.actions{border-top:1px solid #edf0e9;padding-top:12px;margin-top:15px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}.actions form{display:flex;gap:6px;align-items:center}.actions select{width:135px;padding:6px}.actions button,.actions a{font-size:12px;padding:6px 10px}.actions .remove{margin-left:auto}.pill{font-size:11px;border-radius:15px;background:#edf1e8;padding:3px 9px}.empty{text-align:center;padding:55px 20px;border:1px dashed #c6d3bd;border-radius:14px}.empty strong{display:block;font-size:19px;margin-bottom:8px}.notice{padding:12px 16px;border-radius:10px;background:#e5efdf;margin:0 0 22px}.error{background:#fff0e8;color:#943b20;border:1px solid #e9c5b5}.category-grid{max-width:850px}.category-row{margin-top:14px;display:flex;gap:14px;align-items:center;justify-content:space-between}.category-row form{display:flex;gap:8px;align-items:center}.category-row input{width:180px}.back{display:inline-block;margin-bottom:20px;font-size:14px}.create{display:flex;gap:10px;align-items:end}.create .field{flex:1;margin:0}.footer{margin-top:30px;font-size:12px;color:var(--muted)}@media(max-width:1080px){.layout{grid-template-columns:150px minmax(0,1fr)}.save{grid-column:2;position:static;grid-row:1}.library{grid-column:2}.side{grid-row:1/3}.search{grid-template-columns:1fr 120px auto}}@media(max-width:650px){main,.top{padding:22px 16px}.layout{display:flex;flex-direction:column}.layout>*{width:100%}.side{display:flex;flex-wrap:wrap;gap:3px}.side .section{display:none}.side a{gap:8px}.save{order:0}.library{order:1}.search{grid-template-columns:1fr}.category-row{align-items:start;flex-direction:column}.category-row input{width:150px}.tag{font-size:10px}}
"""


def page(content, title="留存 · 个人收藏夹"):
    return f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><style>{STYLE}</style></head>
    <body><header><div class="top"><a class="brand" href="/">留存<span> / </span>个人收藏夹</a><span class="tag">本机保存 · 辅助试用版</span></div></header><main>{content}<p class="footer">源自 Atlas「生活待购与灵感收藏夹」 · 数据保存在本机 SQLite · 不抓取网页，不同步云端</p></main></body></html>"""


def option(value, label, current):
    return f'<option value="{escape(value)}"{" selected" if value == current else ""}>{escape(label)}</option>'


class Handler(BaseHTTPRequestHandler):
    server_version = "BookmarkTrial/1.0"

    def send(self, status, body, content="text/html; charset=utf-8", headers=None):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        # no-referrer can make browser form POST Origin opaque ("null").
        # same-origin preserves local CSRF validation while withholding external referrers.
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data)

    def json(self, status, body):
        self.send(status, json.dumps(body, ensure_ascii=False), "application/json; charset=utf-8")

    def redirect(self, path, status=303):
        self.send(status, "", headers={"Location": path})

    def form(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 0 or length > 1024 * 1024:
                raise ValueError()
            raw = self.rfile.read(length).decode("utf-8")
            if self.headers.get("Content-Type", "").split(";")[0] == "application/json":
                data = json.loads(raw)
                if not isinstance(data, dict):
                    raise ValueError()
                return data
            return {k: v[-1] for k, v in parse_qs(raw, keep_blank_values=True).items()}
        except (ValueError, UnicodeError):
            raise InputError("bad_request", "提交内容无法解析，请检查后重试。") from None

    def check_origin(self):
        host = self.headers.get("Host", "")
        allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        if host not in allowed:
            raise InputError("bad_request", "请通过本机地址打开应用。", status=403)
        origin = self.headers.get("Origin")
        if origin and origin != "http://" + host:
            raise InputError("bad_request", "请从本应用页面提交表单。", status=403)

    def do_GET(self):
        self.handle_request("GET")

    def do_POST(self):
        self.handle_request("POST")

    def do_PATCH(self):
        self.handle_request("PATCH")

    def do_DELETE(self):
        self.handle_request("DELETE")

    def handle_request(self, method):
        path = urlsplit(self.path).path
        query = {k: v[-1] for k, v in parse_qs(urlsplit(self.path).query, keep_blank_values=True).items()}
        data = {}
        lib = self.server.library
        try:
            self.check_origin()
            if method != "GET":
                data = self.form()
            with lib.connect() as db:
                if method == "GET":
                    if path == "/":
                        return self.send(200, self.home(db, query))
                    if path == "/categories":
                        return self.send(200, self.category_page(db))
                    if path == "/demo-page":
                        return self.send(200, page('<h1>原始链接已打开</h1><p>这是用于验证路径和查询串不被改写的本地目标页。</p><pre>' + escape(self.path) + '</pre><a href="/">返回收藏夹</a>'))
                    if path == "/api/health":
                        return self.json(200, {"ready": True, "schema_version": 1, "origin": "assisted-trial"})
                    if path == "/api/categories":
                        return self.json(200, lib.categories(db))
                    if path == "/api/bookmarks":
                        return self.json(200, lib.records(db, query.get("category", ""), query.get("q", ""), query.get("include_trashed") == "1"))
                    if path.startswith("/api/bookmarks/"):
                        return self.json(200, lib.record(db, path.split("/")[-1]))
                    if path.startswith("/go/"):
                        return self.redirect(lib.record(db, path.split("/")[-1])["url"], 302)
                if method == "POST" and path in ("/bookmarks/new", "/api/bookmarks"):
                    row = lib.save(db, data)
                    db.commit()
                    if path.startswith("/api/"):
                        return self.json(201, row)
                    return self.redirect("/?" + urlencode({"category": self.category_name(db, row["category_id"]), "notice": "saved"}))
                if path.startswith("/api/categories") and method in ("POST", "PATCH", "DELETE"):
                    action = {"POST": "create", "PATCH": "rename", "DELETE": "delete"}[method]
                    row = lib.change_category(db, action, data, path.split("/")[-1])
                    db.commit()
                    return self.json(201 if action == "create" else 200, row)
                if path.startswith("/categories/") and method == "POST":
                    lib.change_category(db, path.split("/")[-1], data, data.get("category_id"))
                    db.commit()
                    return self.redirect("/categories?notice=updated")
                if path.startswith("/bookmarks/") and method == "POST":
                    action = path.split("/")[-1]
                    if action not in ("move", "delete", "restore"):
                        raise InputError("not_found", "这个操作不存在。", status=404)
                    if action == "move":
                        cid = data.get("category_id")
                        cat = db.execute("SELECT name FROM categories WHERE id=?", (cid,)).fetchone()
                        if cat is None:
                            raise InputError("invalid_category", "请选择一个已有分类。", "category_id")
                        data = {**data, "category": cat["name"]}
                    row = lib.update(db, data.get("record_id"), action, data)
                    db.commit()
                    return self.redirect("/?trash=1&notice=deleted" if action == "delete" else "/?" + urlencode({"category": self.category_name(db, row["category_id"]), "notice": "updated"}))
                if path.startswith("/api/bookmarks/"):
                    parts = path.strip("/").split("/")
                    action = (parts[3] if len(parts) == 4 and method == "POST" else {"PATCH": "patch", "DELETE": "delete"}.get(method))
                    if action in ("move", "restore", "patch", "delete"):
                        row = lib.update(db, parts[2], action, data)
                        db.commit()
                        return self.json(200, row)
                raise InputError("not_found", "页面或记录不存在。", status=404)
        except InputError as exc:
            if path.startswith(("/api/", "/go/")):
                return self.json(exc.status, {"error": {"code": exc.code, "message": exc.message, "field": exc.field}})
            with lib.connect() as db:
                content = self.category_page(db, data, exc) if path.startswith("/categories") else self.home(db, query, data, exc)
                return self.send(exc.status, content)
        except sqlite3.Error:
            self.log_error("Database operation failed")
            if path.startswith("/api/"):
                return self.json(503, {"error": {"code": "storage_unavailable", "message": "暂时无法保存，请检查数据目录后重试。", "field": ""}})
            return self.send(503, page('<h1>暂时无法读取或保存</h1><p>请检查数据目录权限和磁盘空间；已有数据不会被清空。</p><a href="/">重试</a>'))

    @staticmethod
    def category_name(db, identifier):
        return db.execute("SELECT name FROM categories WHERE id=?", (identifier,)).fetchone()[0]

    @staticmethod
    def notice(error, query=None):
        if error:
            return f'<div class="notice error" data-testid="form-error" role="alert">{escape(error.message)} <small>({escape(error.code)})</small></div>'
        messages = {"saved": "已保存。下次回来，这条链接还在。", "updated": "整理已保存。", "deleted": "已移入回收站，可随时恢复。"}
        return f'<div class="notice" role="status">{messages[query["notice"]]}</div>' if query and query.get("notice") in messages else ""

    def home(self, db, query, values=None, error=None):
        values = values or {}
        cats = self.server.library.categories(db)
        category, q, trash = query.get("category", ""), query.get("q", ""), query.get("trash") == "1"
        rows = self.server.library.records(db, category, q, trash, trash)
        side = '<a href="/" class="' + ("active" if not category and not trash else "") + '">全部收藏<span class="count">' + str(sum(c["count"] for c in cats)) + '</span></a><p class="section eyebrow">我的分类</p>'
        for cat in cats:
            side += f'<a href="/?{escape(urlencode({"category":cat["name"]}))}" class="{"active" if category in (cat["name"],cat["id"]) else ""}">{escape(cat["name"])} <span data-testid="category-count" data-category-id="{cat["id"]}" class="count">{cat["count"]}</span></a>'
        side += '<p class="section eyebrow">整理</p><a data-testid="category-manager" href="/categories">管理分类 ↗</a><a href="/?trash=1">回收站</a>'
        records = ""
        for row in rows:
            controls = f'<form data-testid="record-restore-form" method="post" action="/bookmarks/restore"><input type="hidden" name="record_id" value="{row["id"]}"><button>恢复收藏</button></form>' if trash else f'''<form data-testid="record-move-form" method="post" action="/bookmarks/move"><input type="hidden" name="record_id" value="{row['id']}"><select name="category_id" aria-label="移动到分类">{''.join(option(c['id'],c['name'],row['category_id']) for c in cats)}</select><button>移动</button></form><form class="remove" data-testid="record-delete-form" method="post" action="/bookmarks/delete"><input type="hidden" name="record_id" value="{row['id']}"><button title="可以从回收站恢复">移入回收站</button></form>'''
            records += f'''<tr data-testid="record-row" data-record-id="{row['id']}"><td><div class="host">{escape(row['hostname'])}</div><a class="record-title" data-testid="record-open-link" href="{escape(row['url'])}" target="_blank" rel="noopener noreferrer">{escape(row['title'] or row['hostname'])} ↗</a><p class="record-description">{escape(row['description'])}</p><p class="record-url">{escape(row['url'])}</p><div class="actions"><span class="pill">{escape(row['category'])}</span>{controls}</div></td></tr>'''
        empty = '<div class="empty" data-testid="empty-state"><strong>' + ("没有匹配的收藏" if q or category else "回收站是空的" if trash else "留住第一个好链接") + '</strong><p class="muted">' + ("试试其他关键词或选择全部分类。" if q or category else "在保存表单粘贴网页链接，就能在这里找回。") + '</p></div>'
        search_options = option("", "全部分类", category) + ''.join(option(c["name"], c["name"], category) for c in cats)
        if category and not any(category == c["name"] for c in cats):
            search_options += option(category, category, category)
        savecat = values.get("category", "未整理")
        content = f'''<section class="intro"><span class="eyebrow">A LITTLE SPACE FOR GOOD FINDS</span><h1>{"回收站" if trash else "把好东西，留给下次。"}</h1><p class="muted">商品、教程、灵感。先存下来，需要时再找到它。</p></section>{self.notice(error,query)}<div class="layout"><nav class="side" aria-label="收藏分类">{side}</nav><section class="library"><form class="search" data-testid="category-search-form" action="/" method="get"><label for="q">搜索收藏</label><input id="q" name="q" value="{escape(q)}" placeholder="搜索标题、域名或描述"><label for="filter">筛选分类</label><select id="filter" name="category">{search_options}</select>{'<input type="hidden" name="trash" value="1">' if trash else ''}<button>搜索</button></form><div class="summary"><span>{escape(category or ("回收站" if trash else "全部收藏"))}{(' · “'+escape(q)+'”') if q else ''}</span><span>{len(rows)} 条收藏</span></div><div data-testid="record-list"><table aria-label="收藏列表"><tbody>{records}</tbody></table>{empty if not rows else ''}</div></section><aside class="panel save"><h2>＋ 保存一个链接</h2><p class="muted">无需整理完美，先留住它。</p><form method="post" action="/bookmarks/new" novalidate><div class="field"><label for="url">网页链接 *</label><input id="url" name="url" value="{escape(values.get('url',''))}" placeholder="https://…" required></div><div class="field"><label for="title">标题（可选）</label><input id="title" name="title" value="{escape(values.get('title',''))}" placeholder="给它起个容易找的名字"></div><div class="field"><label for="description">描述（可选）</label><textarea id="description" name="description" rows="3" placeholder="为什么想留下它？">{escape(values.get('description',''))}</textarea></div><div class="field"><label for="category">保存到分类</label><input id="category" name="category" list="categories" value="{escape(savecat)}"><datalist id="categories">{''.join(option(c['name'],c['name'],'') for c in cats)}</datalist><p class="muted">可选已有分类，也可输入新名称。</p></div><button class="primary">保存收藏</button></form></aside></div>'''
        return page(content)

    def category_page(self, db, values=None, error=None):
        values = values or {}
        rows = ""
        for cat in self.server.library.categories(db):
            controls = '<span class="muted">默认分类 · 保留</span>' if cat["is_default"] else f'''<form method="post" action="/categories/rename" data-testid="category-rename-form"><input type="hidden" name="category_id" value="{cat['id']}"><input aria-label="重命名 {escape(cat['name'])}" name="name" value="{escape(values.get('name',cat['name']) if values.get('category_id') == cat['id'] else cat['name'])}"><button>重命名</button></form><form method="post" action="/categories/delete" data-testid="category-delete-form"><input type="hidden" name="category_id" value="{cat['id']}"><button>删除分类</button></form>'''
            rows += f'<div class="panel category-row"><div><strong>{escape(cat["name"])}</strong> <span class="count" data-testid="category-count" data-category-id="{cat["id"]}">{cat["count"]}</span></div>{controls}</div>'
        return page(f'''<a class="back" href="/">← 返回收藏夹</a><div class="category-grid"><h1>管理分类</h1><p class="muted">删除分类会把收藏移回“未整理”，不会删除收藏；回收站里的记录也会一起迁移。</p>{self.notice(error)}<section class="panel" style="margin-top:24px"><form class="create" method="post" action="/categories/create" data-testid="category-create-form"><div class="field"><label for="new-name">新分类名称</label><input id="new-name" name="name" value="{escape(values.get('name','') if not values.get('category_id') else '')}" placeholder="例如：周末阅读"></div><button class="primary">创建分类</button></form></section>{rows}</div>''', "管理分类 · 留存")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", choices=["127.0.0.1", "localhost"])
    parser.add_argument("--port", type=int, default=5273)
    parser.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    parser.add_argument("--demo", action="store_true", help="Seed clearly marked sample links on first initialization only")
    args = parser.parse_args()
    library = Library(args.data_dir.resolve(), args.demo)
    with ThreadingHTTPServer((args.host, args.port), Handler) as server:
        server.library = library
        print(f"留存 · http://{args.host}:{args.port}/ · 数据：{library.path}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
