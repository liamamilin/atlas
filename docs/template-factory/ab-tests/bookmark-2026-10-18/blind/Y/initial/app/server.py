"""HTTP 层：路由、Host/Origin 防护、JSON API 与 SSR 表单入口。"""

import json
import os
import sys
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler

import urlutil
import views
from store import AppError, SORTS

MAX_BODY_BYTES = 64 * 1024
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")


def _json_bytes(obj):
    return json.dumps(obj, ensure_ascii=False).encode("utf-8")


def error_envelope(code, message, details=None):
    return {"error": {"code": code, "message": message, "details": details or {}}}


class AppHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "BookmarkLibrary/1.0"

    # ------------------------------------------------------------- 生命周期
    def log_message(self, fmt, *args):
        if self.server.quiet:
            return
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def do_GET(self):
        self._handle("GET")

    def do_POST(self):
        self._handle("POST")

    def do_PATCH(self):
        self._handle("PATCH")

    def do_DELETE(self):
        self._handle("DELETE")

    # ------------------------------------------------------------- 基础工具
    @property
    def config(self):
        return self.server.config

    @property
    def store(self):
        return self.server.config.store

    def _send(self, status, body=b"", content_type=None, headers=None):
        self.send_response(status)
        if content_type:
            self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for name, value in (headers or []):
            self.send_header(name, value)
        self.end_headers()
        if body:
            try:
                self.wfile.write(body)
            except Exception:
                pass

    def _json(self, status, payload, headers=None):
        self._send(status, _json_bytes(payload), "application/json; charset=utf-8", headers)

    def _error(self, status, code, message, details=None):
        self._json(status, error_envelope(code, message, details))

    def _html(self, status, text, headers=None):
        self._send(status, text.encode("utf-8"), "text/html; charset=utf-8", headers)

    def _redirect(self, status, location):
        self._send(status, b"", None, [("Location", location)])

    # ------------------------------------------------------------- 请求解析
    def _read_body(self):
        header = self.headers.get("Content-Length")
        if header is None:
            return b"", False
        try:
            length = int(header)
        except (TypeError, ValueError):
            return b"", False
        if length <= 0:
            return b"", False
        if length > MAX_BODY_BYTES:
            # 排空超大请求体，保持连接可用后再返回 413。
            if length <= 4 * 1024 * 1024:
                remaining = length
                while remaining > 0:
                    chunk = self.rfile.read(min(65536, remaining))
                    if not chunk:
                        break
                    remaining -= len(chunk)
            else:
                self.close_connection = True
            return b"", True
        return self.rfile.read(length), False

    def _parse_body(self, raw, content_type):
        if content_type and "application/json" in content_type:
            if raw.strip() == b"":
                raise AppError("invalid_json", 400)
            try:
                return json.loads(raw.decode("utf-8"))
            except Exception:
                raise AppError("invalid_json", 400)
        if content_type and "x-www-form-urlencoded" in content_type:
            text = raw.decode("utf-8", "replace")
            parsed = urllib.parse.parse_qs(text, keep_blank_values=True)
            return {key: values[0] for key, values in parsed.items()}
        if raw.strip() == b"":
            return {}
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            raise AppError("invalid_json", 400)

    def _host_ok(self):
        incoming = self.headers.get("Host")
        if incoming is None:
            return False
        return incoming.strip().lower() in self.config.authorities

    def _origin_ok(self):
        site = self.headers.get("Sec-Fetch-Site")
        if site is not None and site.strip().lower() == "cross-site":
            return False
        origin = self.headers.get("Origin")
        if origin is None:
            return True
        normalized = origin.strip().rstrip("/")
        if normalized == "" or normalized.lower() == "null":
            return False
        return normalized.lower() in self.config.origins

    def _strip_base(self, path):
        base = self.config.base_path
        if base == "":
            return path
        if path == base:
            return "/"
        if path.startswith(base + "/"):
            return path[len(base):]
        return None

    def _query(self, name):
        parsed = urllib.parse.parse_qs(
            urllib.parse.urlsplit(self.path).query, keep_blank_values=True
        )
        values = parsed.get(name)
        return values[0] if values else None

    def _raw_query(self):
        return urllib.parse.urlsplit(self.path).query

    # ------------------------------------------------------------- 分发
    def _handle(self, method):
        started = time.time()
        try:
            raw, too_large = self._read_body()
            if too_large:
                self._error(413, "payload_too_large", "请求体超过 64 KiB")
                return

            content_type = self.headers.get("Content-Type") or ""
            if method in ("POST", "PATCH"):
                body = self._parse_body(raw, content_type)
            else:
                body = {}

            if not self._host_ok():
                self._error(400, "invalid_host", "Host 与配置的服务地址不一致",
                            {"host": self.headers.get("Host") or ""})
                return

            if method in ("POST", "PATCH", "DELETE") and not self._origin_ok():
                self._error(403, "forbidden_origin", "请求来源不被允许")
                return

            path = urllib.parse.urlsplit(self.path).path
            stripped = self._strip_base(path)
            if stripped is None:
                self._api_or_page_error(method, 404, "not_found", "资源不存在")
                return
            self._dispatch(method, stripped, body)
        except AppError as exc:
            self._api_or_page_error(None, exc.status, exc.code, exc.message, exc.details)
        except Exception:
            if not self.server.quiet:
                import traceback
                traceback.print_exc()
            try:
                self._api_or_page_error(None, 500, "internal", "服务器内部错误")
            except Exception:
                pass
        finally:
            if not self.server.quiet:
                sys.stderr.write("%s %s -> %s (%.1fms)\n" % (
                    method, self.path, getattr(self, "_status", "?"),
                    (time.time() - started) * 1000.0,
                ))

    def _api_or_page_error(self, method, status, code, message, details=None):
        # API 路由返回错误信封；其它路由返回简单错误页。
        path = urllib.parse.urlsplit(self.path).path
        base = self.config.base_path
        api_prefix = base + "/api/"
        if path == base + "/api" or path.startswith(api_prefix):
            self._error(status, code, message, details)
        else:
            self._html(status, views.render_error_page(base, status, message))

    # ------------------------------------------------------------- 路由
    def _dispatch(self, method, path, body):
        segments = [seg for seg in path.split("/") if seg != ""]

        # 静态资源
        if method == "GET" and len(segments) == 2 and segments[0] == "static":
            self._serve_static(segments[1])
            return

        # 页面
        if method == "GET":
            if path == "/":
                self._home()
                return
            if path == "/trash":
                self._trash_page()
                return
            if len(segments) == 2 and segments[0] == "c":
                self._category_page(segments[1])
                return
            if len(segments) == 2 and segments[0] == "b":
                self._open_link(segments[1])
                return

        # 数据 API
        if segments and segments[0] == "api":
            self._dispatch_api(method, segments, body)
            return

        # HTML 表单写入口
        if method == "POST":
            if path == "/bookmarks":
                self._html_create_bookmark(body)
                return
            if len(segments) == 3 and segments[0] == "bookmarks" and segments[2] == "move":
                self._html_move(segments[1], body)
                return
            if len(segments) == 3 and segments[0] == "bookmarks" and segments[2] == "edit":
                self._html_edit(segments[1], body)
                return
            if len(segments) == 3 and segments[0] == "bookmarks" and segments[2] == "delete":
                self._html_delete_bookmark(segments[1])
                return
            if path == "/categories":
                self._html_create_category(body)
                return
            if len(segments) == 3 and segments[0] == "categories" and segments[2] == "rename":
                self._html_rename_category(segments[1], body)
                return
            if len(segments) == 3 and segments[0] == "categories" and segments[2] == "delete":
                self._html_delete_category(segments[1], body)
                return
            if path == "/trash/clear":
                self._html_clear_trash(body)
                return
            if len(segments) == 3 and segments[0] == "trash" and segments[2] == "restore":
                self._html_restore(segments[1], body)
                return
            if len(segments) == 3 and segments[0] == "trash" and segments[2] == "delete":
                self._html_delete_trash(segments[1], body)
                return

        self._api_or_page_error(method, 404, "not_found", "资源不存在")

    def _dispatch_api(self, method, segments, body):
        if method == "GET":
            if segments == ["api", "health"]:
                self._api_health()
                return
            if segments == ["api", "categories"]:
                self._api_list_categories()
                return
            if segments == ["api", "bookmarks"]:
                self._api_list_bookmarks()
                return
            if len(segments) == 3 and segments[1] == "bookmarks":
                self._api_get_bookmark(segments[2])
                return
            if segments == ["api", "trash"]:
                self._api_list_trash()
                return
        elif method == "POST":
            if segments == ["api", "bookmarks"]:
                self._api_create_bookmark(body)
                return
            if segments == ["api", "categories"]:
                self._api_create_category(body)
                return
            if len(segments) == 4 and segments[1] == "bookmarks" and segments[3] == "restore":
                self._api_restore(segments[2], body)
                return
        elif method == "PATCH":
            if len(segments) == 3 and segments[1] == "bookmarks":
                self._api_patch_bookmark(segments[2], body)
                return
            if len(segments) == 3 and segments[1] == "categories":
                self._api_rename_category(segments[2], body)
                return
        elif method == "DELETE":
            if len(segments) == 3 and segments[1] == "bookmarks":
                self._api_delete_bookmark(segments[2])
                return
            if len(segments) == 3 and segments[1] == "categories":
                self._api_delete_category(segments[2])
                return
            if segments == ["api", "trash"]:
                self._api_purge_all()
                return
            if len(segments) == 3 and segments[1] == "trash":
                self._api_purge_item(segments[2])
                return
        self._api_or_page_error(method, 404, "not_found", "资源不存在")

    # ------------------------------------------------------------- 静态资源
    def _serve_static(self, name):
        if name not in ("app.js", "style.css"):
            self._api_or_page_error("GET", 404, "not_found", "资源不存在")
            return
        try:
            with open(os.path.join(STATIC_DIR, name), "rb") as handle:
                data = handle.read()
        except OSError:
            self._api_or_page_error("GET", 404, "not_found", "资源不存在")
            return
        content_type = "application/javascript; charset=utf-8" if name.endswith(".js") else "text/css; charset=utf-8"
        self._send(200, data, content_type)

    # ------------------------------------------------------------- HTML 页面
    def _flash_headers(self):
        flash_value = None
        cookie = self.headers.get("Cookie")
        if cookie:
            for part in cookie.split(";"):
                piece = part.strip()
                if piece.startswith("atlas_flash="):
                    flash_value = urllib.parse.unquote(piece[len("atlas_flash="):])
        headers = [("Set-Cookie", "atlas_flash=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax")]
        return flash_value, headers

    def _set_flash_headers(self, message):
        return [("Set-Cookie",
                 "atlas_flash=%s; Path=/; HttpOnly; SameSite=Lax"
                 % urllib.parse.quote(message, safe=""))]

    def _base_state(self):
        return {
            "base": self.config.base_path,
            "categories": self.store.list_categories(),
            "defaultId": self.store.default_category_id(),
        }

    def _home(self):
        state = self._base_state()
        q = self._query("q") or ""
        category_id = self._query("categoryId") or ""
        sort = self._query("sort")
        if sort not in SORTS:
            sort = "created_desc"
        limit = self._int_param("limit", 50, 1, 100)
        offset = self._int_param("offset", 0, 0, None)
        listing = self.store.list_bookmarks(q, category_id, sort, limit, offset)
        state.update({
            "q": q, "categoryId": category_id, "sort": sort, "limit": limit,
            "offset": offset, "total": listing["total"], "bookmarks": listing["items"],
        })
        flash, headers = self._flash_headers()
        state["flash"] = flash
        self._html(200, views.render_home(state), headers)

    def _category_page(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("GET", 404, "not_found", "归类不存在")
            return
        category = self.store.get_category(raw_id)
        if category is None:
            self._api_or_page_error("GET", 404, "not_found", "归类不存在")
            return
        state = self._base_state()
        state.update({
            "category": category,
            "bookmarks": self.store.list_category_bookmarks(raw_id),
        })
        flash, headers = self._flash_headers()
        state["flash"] = flash
        self._html(200, views.render_category(state), headers)

    def _trash_page(self):
        state = self._base_state()
        listing = self.store.list_trash(100000, 0)
        state["items"] = listing["items"]
        flash, headers = self._flash_headers()
        state["flash"] = flash
        self._html(200, views.render_trash(state), headers)

    def _open_link(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            self._error(404, "not_found", "记录不存在")
            return
        bookmark = self.store.get_active_bookmark(raw_id)
        if bookmark is None:
            self._error(404, "not_found", "记录不存在")
            return
        try:
            _, parsed = urlutil.validate_url_value(bookmark["url"])
        except Exception:
            self._error(500, "internal", "记录中的地址不合法")
            return
        location = urlutil.serialize(parsed)
        if not all(0x20 <= ord(ch) <= 0x7E for ch in location):
            self._error(500, "internal", "记录中的地址不合法")
            return
        self._redirect(302, location)

    def _int_param(self, name, default, minimum, maximum):
        raw = self._query(name)
        if raw is None or raw == "":
            return default
        try:
            value = int(raw)
        except (TypeError, ValueError):
            return default
        if value < minimum:
            return default
        if maximum is not None and value > maximum:
            return default
        return value

    # ------------------------------------------------------------- HTML 写
    def _html_home_error(self, message, save=None, duplicate=None, dialog=None, prefill=None):
        state = self._base_state()
        state.update({
            "formError": message,
            "save": save or {},
            "duplicate": duplicate,
            "dialog": dialog,
            "prefill": prefill or {},
            "q": "", "categoryId": "", "sort": "created_desc", "limit": 50, "offset": 0,
        })
        listing = self.store.list_bookmarks("", "", "created_desc", 50, 0)
        state["total"] = listing["total"]
        state["bookmarks"] = listing["items"]
        self._html(200, views.render_home(state))

    def _html_create_bookmark(self, body):
        allow_raw = body.get("allowDuplicate")
        allow_duplicate = False
        if allow_raw is not None:
            if allow_raw == "true":
                allow_duplicate = True
            else:
                self._html_home_error("重复另存参数不合法", save=self._save_values(body))
                return
        category = body.get("categoryId")
        if category == "":
            category = None
        payload = {
            "url": body.get("url"),
            "title": body.get("title"),
            "note": body.get("note"),
            "categoryId": category,
        }
        try:
            self.store.create_bookmark(payload, allow_duplicate)
        except AppError as exc:
            duplicate = None
            if exc.code == "duplicate_url":
                duplicate = {
                    "existingId": exc.details.get("existingId"),
                    "url": body.get("url") or "",
                    "title": body.get("title") or "",
                    "note": body.get("note") or "",
                    "categoryId": body.get("categoryId") or "",
                }
            self._html_home_error(exc.message, save=self._save_values(body), duplicate=duplicate)
            return
        headers = self._set_flash_headers("已保存到收藏夹")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    @staticmethod
    def _save_values(body):
        return {
            "url": body.get("url") or "",
            "title": body.get("title") or "",
            "note": body.get("note") or "",
            "categoryId": body.get("categoryId") or "",
        }

    def _html_create_category(self, body):
        try:
            self.store.create_category(body.get("name"))
        except AppError as exc:
            self._html_home_error(exc.message)
            return
        headers = self._set_flash_headers("已新建归类")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_move(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "记录不存在")
            return
        try:
            self.store.patch_bookmark(raw_id, {"categoryId": body.get("categoryId")})
        except AppError as exc:
            self._html_home_error(exc.message, prefill={raw_id: {"categoryId": body.get("categoryId")}})
            return
        headers = self._set_flash_headers("已移动记录")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_edit(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "记录不存在")
            return
        payload = {"title": body.get("title"), "note": body.get("note")}
        try:
            self.store.patch_bookmark(raw_id, payload)
        except AppError as exc:
            self._html_home_error(exc.message, prefill={raw_id: {
                "title": body.get("title"), "note": body.get("note")}})
            return
        headers = self._set_flash_headers("已保存修改")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_delete_bookmark(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "记录不存在")
            return
        try:
            self.store.delete_bookmark(raw_id)
        except AppError as exc:
            self._html_home_error(exc.message)
            return
        headers = self._set_flash_headers("已移入回收站")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_rename_category(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "归类不存在")
            return
        try:
            self.store.rename_category(raw_id, body.get("name"))
        except AppError as exc:
            category = self.store.get_category(raw_id)
            if category is None:
                self._api_or_page_error("POST", 404, "not_found", "归类不存在")
                return
            state = self._base_state()
            state.update({
                "category": category,
                "bookmarks": self.store.list_category_bookmarks(raw_id),
                "formError": exc.message,
                "renameValue": body.get("name") or "",
            })
            self._html(200, views.render_category(state))
            return
        headers = self._set_flash_headers("已重命名归类")
        self._send(303, b"", None,
                   [("Location", self.config.base_path + "/c/" + raw_id)] + headers)

    def _html_delete_category(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "归类不存在")
            return
        try:
            self.store.delete_category(
                raw_id, body.get("mode"), body.get("targetCategoryId"), body.get("confirm")
            )
        except AppError as exc:
            if exc.code == "not_found":
                self._api_or_page_error("POST", 404, "not_found", exc.message)
                return
            self._html_home_error("", dialog={
                "categoryId": raw_id,
                "error": exc.message,
                "targetId": body.get("targetCategoryId"),
            })
            return
        headers = self._set_flash_headers("已删除归类")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_restore(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "记录不存在")
            return
        payload = {}
        category = body.get("categoryId")
        if category not in (None, ""):
            payload["categoryId"] = category
        try:
            self.store.restore_bookmark(raw_id, payload)
        except AppError as exc:
            self._html_trash_error(exc.message)
            return
        headers = self._set_flash_headers("已恢复到收藏夹")
        self._send(303, b"", None, [("Location", self.config.base_path + "/")] + headers)

    def _html_delete_trash(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            self._api_or_page_error("POST", 404, "not_found", "记录不存在")
            return
        if body.get("confirm") != "true":
            self._html_trash_error("请先勾选确认，才能永久删除")
            return
        try:
            self.store.purge_trash_item(raw_id)
        except AppError as exc:
            self._html_trash_error(exc.message)
            return
        headers = self._set_flash_headers("已永久删除")
        self._send(303, b"", None, [("Location", self.config.base_path + "/trash")] + headers)

    def _html_clear_trash(self, body):
        if body.get("confirm") != "true":
            self._html_trash_error("请先勾选确认，才能清空回收站")
            return
        try:
            self.store.purge_trash_all()
        except AppError as exc:
            self._html_trash_error(exc.message)
            return
        headers = self._set_flash_headers("已清空回收站")
        self._send(303, b"", None, [("Location", self.config.base_path + "/trash")] + headers)

    def _html_trash_error(self, message):
        state = self._base_state()
        state.update({
            "items": self.store.list_trash(100000, 0)["items"],
            "formError": message,
        })
        self._html(200, views.render_trash(state))

    # ------------------------------------------------------------- 数据 API
    def _api_health(self):
        config = self.config
        self._json(200, {
            "ok": True,
            "stage": config.stage,
            "instanceId": config.instance_id,
            "startedAt": config.started_at,
            "basePath": config.base_path,
        })

    def _api_list_categories(self):
        self._json(200, {"items": self.store.list_categories()})

    def _api_create_category(self, body):
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        category = self.store.create_category(body.get("name"))
        self._json(201, {"category": category})

    def _api_rename_category(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        category = self.store.rename_category(raw_id, body.get("name"))
        self._json(200, {"category": category})

    def _api_delete_category(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        mode = self._query("mode")
        target = self._query("targetCategoryId")
        confirm = self._query("confirm")
        result = self.store.delete_category(raw_id, mode, target, confirm)
        self._json(200, result)

    def _api_list_bookmarks(self):
        q = self._query("q")
        if q is not None and "\u0001" in q:
            raise AppError("invalid_query", 400)
        category = self._query("categoryId")
        sort = self._query("sort")
        if sort is None or sort == "":
            sort = "created_desc"
        if sort not in SORTS:
            raise AppError("invalid_sort", 400)
        limit = self._api_int("limit", 50, 1, 100, "invalid_limit")
        offset = self._api_int("offset", 0, 0, None, "invalid_offset")
        result = self.store.list_bookmarks(q, category, sort, limit, offset)
        self._json(200, result)

    def _api_int(self, name, default, minimum, maximum, code):
        raw = self._query(name)
        if raw is None or raw == "":
            return default
        if not urlutil.is_decimal_id(raw) and not (raw.startswith("-") and raw[1:].isdigit()):
            raise AppError(code, 400)
        try:
            value = int(raw)
        except (TypeError, ValueError):
            raise AppError(code, 400)
        if value < minimum:
            raise AppError(code, 400)
        if maximum is not None and value > maximum:
            raise AppError(code, 400)
        return value

    def _api_get_bookmark(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        bookmark = self.store.get_active_bookmark(raw_id)
        if bookmark is None:
            raise AppError("not_found", 404)
        self._json(200, {"bookmark": bookmark})

    def _api_create_bookmark(self, body):
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        allow = body.get("allowDuplicate", False)
        if isinstance(allow, bool):
            allow_duplicate = allow
        else:
            raise AppError("invalid_field", 400, details={"field": "allowDuplicate"})
        bookmark = self.store.create_bookmark(body, allow_duplicate)
        self._json(201, {"bookmark": bookmark})

    def _api_patch_bookmark(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        bookmark = self.store.patch_bookmark(raw_id, body)
        self._json(200, {"bookmark": bookmark})

    def _api_delete_bookmark(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        bookmark = self.store.delete_bookmark(raw_id)
        self._json(200, {"bookmark": bookmark})

    def _api_restore(self, raw_id, body):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        if body is None:
            body = {}
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        result = self.store.restore_bookmark(raw_id, body)
        self._json(200, result)

    def _api_list_trash(self):
        limit = self._api_int("limit", 50, 1, 100, "invalid_limit")
        offset = self._api_int("offset", 0, 0, None, "invalid_offset")
        self._json(200, self.store.list_trash(limit, offset))

    def _api_purge_item(self, raw_id):
        if not urlutil.is_decimal_id(raw_id):
            raise AppError("not_found", 404)
        self._json(200, self.store.purge_trash_item(raw_id))

    def _api_purge_all(self):
        confirm = self._query("confirm")
        if confirm is None or confirm == "" or confirm == "false":
            raise AppError("confirmation_required", 409)
        if confirm != "true":
            raise AppError("invalid_confirm", 400)
        self._json(200, self.store.purge_trash_all())
