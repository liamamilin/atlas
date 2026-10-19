"""HTTP 层：路由、表单处理与静态资源，仅回环监听。

路由：
- GET  /                首页（支持 ?category= 与 ?q=）
- POST /save            保存链接（含校验、重复提示、幂等）
- POST /move            移动记录到其他分类
- GET  /static/app.css  本地样式表
"""

import os
import sys
import threading
import urllib.parse
import uuid
from http.server import BaseHTTPRequestHandler

import render
from db import Store
from urls import url_key, validate_url

SAVE_LOCK = threading.RLock()
STORE = None

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
STATIC_FILES = {"app.css": "text/css; charset=utf-8"}

MAX_BODY_BYTES = 1_000_000


def configure(data_dir):
    global STORE
    STORE = Store(data_dir)
    return STORE


class AppHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    server_version = "BookmarkShelf/1.0"
    timeout = 65
    _head_only = False

    # ---- 基础响应 ----
    def _send_bytes(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True
        if not self._head_only:
            self.wfile.write(body)

    def _send_html(self, status, text):
        self._send_bytes(status, "text/html; charset=utf-8", text.encode("utf-8"))

    def log_message(self, fmt, *args):
        sys.stderr.write("[app] %s %s\n" % (self.address_string(), fmt % args))

    # ---- 请求解析 ----
    def _read_form(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except (TypeError, ValueError):
            length = 0
        if length <= 0:
            return {}
        if length > MAX_BODY_BYTES:
            length = MAX_BODY_BYTES
        raw = self.rfile.read(length)
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("utf-8", "replace")
        parsed = urllib.parse.parse_qs(text, keep_blank_values=True)
        return {key: values[-1] for key, values in parsed.items()}

    def _view_params(self):
        parsed = urllib.parse.urlsplit(self.path)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        q = (params.get("q", [""])[0] or "").strip()
        category = (params.get("category", [""])[0] or "").strip()
        return q, category

    # ---- 渲染 ----
    def _index_context(self, form=None, error=None, duplicate=None):
        q, category = self._view_params()
        category_filter = "all"
        category_id = None
        if category == "unsorted":
            category_filter = "unsorted"
        elif category.isdigit():
            category_filter = "id"
            category_id = int(category)
        bookmarks = STORE.list_bookmarks(
            category_id=category_id, category_filter=category_filter, q=q
        )
        return {
            "categories": STORE.list_categories(),
            "bookmarks": bookmarks,
            "form": form or {},
            "error": error,
            "duplicate": duplicate,
            "q": q,
            "active_category": category,
            "total_count": STORE.count_bookmarks(),
            "nonce": uuid.uuid4().hex,
            "confirm_nonce": uuid.uuid4().hex,
        }

    def _render_index(self, status=200, form=None, error=None, duplicate=None):
        ctx = self._index_context(form=form, error=error, duplicate=duplicate)
        self._send_html(status, render.render_page(ctx))

    # ---- 路由 ----
    def do_GET(self):
        parsed = urllib.parse.urlsplit(self.path)
        path = parsed.path
        if path.startswith("/static/"):
            return self._serve_static(path[len("/static/"):])
        if path in ("/", "/index.html"):
            return self._render_index()
        return self._send_bytes(404, "text/plain; charset=utf-8", b"not found")

    def do_HEAD(self):
        self._head_only = True
        try:
            self.do_GET()
        finally:
            self._head_only = False

    def do_POST(self):
        parsed = urllib.parse.urlsplit(self.path)
        if parsed.path == "/save":
            return self._handle_save()
        if parsed.path == "/move":
            return self._handle_move()
        return self._send_bytes(404, "text/plain; charset=utf-8", b"not found")

    def _serve_static(self, name):
        if name not in STATIC_FILES:
            return self._send_bytes(404, "text/plain; charset=utf-8", b"not found")
        try:
            with open(os.path.join(STATIC_DIR, name), "rb") as handle:
                data = handle.read()
        except OSError:
            return self._send_bytes(404, "text/plain; charset=utf-8", b"not found")
        self._send_bytes(200, STATIC_FILES[name], data)

    # ---- 保存 ----
    def _handle_save(self):
        with SAVE_LOCK:
            fields = self._read_form()
            token = (fields.get("nonce") or "").strip()
            if token and not STORE.register_nonce(token):
                # 同一表单的重复提交：不再新增，直接回到成功视图。
                return self._render_index()

            raw_url = fields.get("url") or ""
            raw_title = fields.get("title") or ""
            raw_note = fields.get("note") or ""
            new_category = (fields.get("new_category") or "").strip()
            category_raw = (fields.get("category_id") or "").strip()
            force = (fields.get("force") or "") == "1"

            form = {
                "url": raw_url,
                "title": raw_title,
                "note": raw_note,
                "new_category": fields.get("new_category") or "",
                "category_id": category_raw,
            }

            url, err = validate_url(raw_url)
            if err:
                return self._render_index(form=form, error=err)

            note = raw_note if raw_note != "" else None
            if note is not None and len(note) > render.NOTE_MAX_LEN:
                message = (
                    "备注过长：最多 %d 字，本次提交 %d 字，未被保存。请缩短后重试。"
                    % (render.NOTE_MAX_LEN, len(note))
                )
                return self._render_index(form=form, error=message)

            title = raw_title.strip() or None

            key = url_key(url)
            if not force:
                duplicate = STORE.find_by_key(key)
                if duplicate:
                    return self._render_index(
                        form=form,
                        duplicate={"url": url, "title": duplicate.get("title") or duplicate["url"]},
                    )

            category_id = None
            if new_category:
                existing = STORE.get_category_by_name(new_category)
                if existing:
                    message = (
                        "分类「%s」已存在，请直接在“分类”下拉中选择它，或换一个名称。"
                        % new_category
                    )
                    return self._render_index(form=form, error=message)
                category_id = STORE.create_category(new_category)
            elif category_raw.isdigit():
                found = STORE.get_category(int(category_raw))
                if found:
                    category_id = found["id"]

            STORE.insert_bookmark(url, key, title, note, category_id)
            return self._render_index()

    # ---- 移动 ----
    def _handle_move(self):
        with SAVE_LOCK:
            fields = self._read_form()
            bookmark_raw = (fields.get("bookmark_id") or "").strip()
            category_raw = (fields.get("category_id") or "").strip()
            if bookmark_raw.isdigit():
                category_id = None
                if category_raw.isdigit():
                    found = STORE.get_category(int(category_raw))
                    if found:
                        category_id = found["id"]
                STORE.move_bookmark(int(bookmark_raw), category_id)
            return self._render_index()
