"""HTTP 层：路由、表单处理与静态资源，仅回环监听。

路由：
- GET  /                首页（支持 ?category= 与 ?q=）
- POST /save            保存链接（含校验、重复提示、幂等）
- POST /move            移动记录到其他分类
- POST /category        独立新建分类（无需保存书签即可创建空分类）
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

# 单次请求体的硬上限：超过即整体拒绝，绝不截断后当作有效表单解析。
MAX_BODY_BYTES = 1_000_000
# 拒绝超大请求时，最多尝试排空这么多字节，避免对端因写超时而看不到 413 响应。
DRAIN_CAP_BYTES = 4_000_000
DRAIN_TIMEOUT_SECONDS = 15


class RequestError(Exception):
    """请求层错误：携带 HTTP 状态码与面向用户的中文说明。"""

    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


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
    def _drain_body(self, length):
        """尽量读完被拒绝请求的正文，让客户端能收到响应；绝不解析。"""
        remaining = min(length, DRAIN_CAP_BYTES)
        try:
            self.connection.settimeout(DRAIN_TIMEOUT_SECONDS)
            while remaining > 0:
                chunk = self.rfile.read(min(65536, remaining))
                if not chunk:
                    break
                remaining -= len(chunk)
        except (OSError, ValueError):
            pass
        finally:
            try:
                self.connection.settimeout(self.timeout)
            except (OSError, ValueError):
                pass

    def _read_form(self):
        """严格解析表单：任何长度/编码异常都显式拒绝，绝不静默截断或替换。"""
        header = self.headers.get("Content-Length")
        if header is None:
            # 无正文声明：视为空表单，交由各动作给出正常的校验反馈。
            return {}
        header = header.strip()
        if not header.isdigit():
            raise RequestError(
                400,
                "请求格式无效：Content-Length 缺失或不是合法的非负整数，"
                "已整体拒绝且未保存任何内容，现有记录保持不变。请通过网页表单重新提交。",
            )
        length = int(header)
        if length > MAX_BODY_BYTES:
            self._drain_body(length)
            raise RequestError(
                413,
                "提交内容过大：单次请求上限为 %d 字节，本次声明 %d 字节。"
                "整份请求已被拒绝，未解析、未保存任何内容，现有记录保持不变；"
                "被拒绝的正文不会保留，请缩小后重新填写并提交。"
                % (MAX_BODY_BYTES, length),
            )
        raw = self.rfile.read(length) if length else b""
        if len(raw) != length:
            raise RequestError(
                400,
                "请求体不完整或长度与声明不一致，已整体拒绝且未保存任何内容，"
                "现有记录保持不变。请重新提交。",
            )
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            raise RequestError(
                400,
                "提交内容编码无效（不是合法的 UTF-8），已整体拒绝且未保存任何内容，"
                "现有记录保持不变。请使用浏览器正常提交。",
            )
        try:
            # errors="strict"：字段内非法的百分号编码（例如 %FF）会直接失败，
            # 绝不会被静默替换成 U+FFFD 后再当成有效表单解析。
            parsed = urllib.parse.parse_qs(
                text, keep_blank_values=True, encoding="utf-8", errors="strict"
            )
        except ValueError:
            raise RequestError(
                400,
                "提交内容编码无效（字段中存在无法解码的百分号编码），已整体拒绝且未"
                "保存任何内容，现有记录保持不变。请使用浏览器正常提交。",
            )
        return {key: values[-1] for key, values in parsed.items()}

    def _view_params(self):
        parsed = urllib.parse.urlsplit(self.path)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
        q = (params.get("q", [""])[0] or "").strip()
        category = (params.get("category", [""])[0] or "").strip()
        return q, category

    # ---- 渲染 ----
    def _index_context(self, form=None, error=None, duplicate=None, active_category=None):
        q, category = self._view_params()
        if active_category is not None:
            category = active_category
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

    def _render_index(self, status=200, form=None, error=None, duplicate=None, active_category=None):
        ctx = self._index_context(
            form=form, error=error, duplicate=duplicate, active_category=active_category
        )
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
        try:
            if parsed.path == "/save":
                return self._handle_save()
            if parsed.path == "/move":
                return self._handle_move()
            if parsed.path == "/category":
                return self._handle_create_category()
        except RequestError as exc:
            return self._render_index(status=exc.status, error=exc.message)
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
            new_category_raw = fields.get("new_category") or ""
            new_category = new_category_raw.strip()
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
            if new_category_raw and not new_category:
                # 用户确实在新建分类框里输入了内容，但只有空白：显式提示而不是静默忽略。
                message = "新建分类名称不能为空，请填写有效名称，或清空该输入框。"
                return self._render_index(form=form, error=message)
            if new_category:
                existing = STORE.get_category_by_name(new_category)
                if existing:
                    message = (
                        "分类「%s」已存在，请直接在“分类”下拉中选择它，或换一个名称。"
                        % new_category
                    )
                    return self._render_index(form=form, error=message)
                category_id = STORE.create_category(new_category)
                if category_id is None:
                    message = (
                        "分类「%s」已存在，请直接在“分类”下拉中选择它，或换一个名称。"
                        % new_category
                    )
                    return self._render_index(form=form, error=message)
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

    # ---- 独立新建分类 ----
    def _handle_create_category(self):
        """独立于保存书签的分类创建：空库也能先建好分类，供已有记录移动进去。"""
        with SAVE_LOCK:
            fields = self._read_form()
            raw_name = ""
            for key in ("name", "new_category", "category_name", "category"):
                value = fields.get(key)
                if value:
                    raw_name = value
                    break
            name = raw_name.strip()
            # 记住提交时所在的浏览视图，创建后仍停留在同一视图，避免记录列表被
            # 切走导致无法立即把已有记录移动到刚新建的分类。
            return_raw = (fields.get("return_category") or "").strip()
            if return_raw != "unsorted" and not return_raw.isdigit():
                return_raw = ""
            form = {"new_category_name": name, "new_category_return": return_raw}
            if not name:
                return self._render_index(
                    form=form, error="分类名称不能为空，请填写有效名称后再创建。"
                )
            existing = STORE.get_category_by_name(name)
            if existing:
                return self._render_index(
                    form=form,
                    error="分类「%s」已存在，请直接选择它或换一个名称。" % name,
                )
            new_id = STORE.create_category(name)
            if new_id is None:
                return self._render_index(
                    form=form,
                    error="分类「%s」已存在，请直接选择它或换一个名称。" % name,
                )
            # 创建成功后新分类立即出现在左侧分类列表；保持当前浏览视图不变，
            # 便于用记录下方的“移动到分类”把已有记录移入。
            return self._render_index(active_category=return_raw)
