# -*- coding: utf-8 -*-
"""HTTP 层：路由、校验与响应。

仅绑定 127.0.0.1（由 app.py 决定）；JSON API 与浏览器 UI 共用同一真实状态。
所有校验失败都返回非 2xx 且 JSON {"error": "..."}，并且不改变既有数据。
"""

import csv
import datetime
import io
import json
import os
import re
import traceback
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlsplit

from db import DuplicateName, MonthMismatch, NotFound, StoreError
from money import MoneyError, format_cents, parse_positive_amount

MONTH_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

CSS_TYPES = {
    "css": "text/css; charset=utf-8",
    "js": "application/javascript; charset=utf-8",
    "html": "text/html; charset=utf-8",
}


class ValidationError(ValueError):
    """请求输入不合法。"""


def make_handler(store, static_dir):
    """构造绑定了 store 与静态资源目录的请求处理器类。"""

    class Handler(BaseHTTPRequestHandler):
        server_version = "BudgetApp/1.0"
        store = store
        static_dir = static_dir

        # ---- 基础工具 -------------------------------------------------
        def log_message(self, fmt, *args):  # 保持安静，避免污染标准输出
            pass

        def _send_json(self, status, payload):
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _send_error_json(self, status, message):
            self._send_json(status, {"error": message})

        def _send_bytes(self, status, body, content_type, extra_headers=None):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            for key, value in (extra_headers or []):
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(body)

        def _send_file(self, path, content_type):
            try:
                with open(path, "rb") as handle:
                    body = handle.read()
            except OSError:
                self._send_error_json(404, "资源不存在")
                return
            self._send_bytes(200, body, content_type)

        def _read_json(self):
            try:
                length = int(self.headers.get("Content-Length") or 0)
            except (TypeError, ValueError):
                length = 0
            raw = self.rfile.read(length) if length > 0 else b""
            if not raw:
                return {}
            try:
                value = json.loads(raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                raise ValidationError("请求体必须是合法 JSON")
            if not isinstance(value, dict):
                raise ValidationError("请求体必须是 JSON 对象")
            return value

        # ---- 输入校验 -------------------------------------------------
        def _month_param(self, query):
            values = query.get("month")
            month = values[0].strip() if values else ""
            if not MONTH_RE.match(month):
                raise ValidationError("month 必须是 YYYY-MM 形式")
            return month

        def _amount(self, value, label):
            try:
                return parse_positive_amount(value)
            except MoneyError as exc:
                raise ValidationError("%s无效：%s" % (label, exc))

        def _date(self, value):
            if not isinstance(value, str) or not DATE_RE.match(value):
                raise ValidationError("date 必须是 YYYY-MM-DD 形式")
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValidationError("date 不是有效日期")
            return value

        def _category_id(self, value):
            if isinstance(value, bool):
                raise ValidationError("category_id 必须是整数")
            if isinstance(value, int):
                category_id = value
            elif isinstance(value, str) and value.strip().lstrip("-").isdigit():
                category_id = int(value.strip())
            else:
                raise ValidationError("category_id 必须是整数")
            if category_id <= 0:
                raise ValidationError("category_id 必须为正整数")
            return category_id

        def _note(self, value):
            if value is None:
                return ""
            if not isinstance(value, str):
                raise ValidationError("note 必须是字符串")
            return value

        def _match_id(self, path, prefix):
            if not path.startswith(prefix):
                return None
            rest = path[len(prefix):]
            if rest == "" or "/" in rest:
                raise ValidationError("非法 id")
            try:
                value = int(rest)
            except ValueError:
                raise ValidationError("id 必须为整数：%r" % rest)
            if value <= 0:
                raise ValidationError("id 必须为正整数")
            return value

        # ---- 路由 -----------------------------------------------------
        def do_GET(self):
            self._dispatch("GET")

        def do_POST(self):
            self._dispatch("POST")

        def do_PUT(self):
            self._dispatch("PUT")

        def do_DELETE(self):
            self._dispatch("DELETE")

        def _dispatch(self, method):
            parsed = urlsplit(self.path)
            path = parsed.path
            query = parse_qs(parsed.query)
            try:
                if method == "GET":
                    if path == "/":
                        return self._serve_index()
                    if path.startswith("/static/"):
                        return self._serve_static(path)
                    if path == "/api/state":
                        return self._send_json(200, self.store.get_state(self._month_param(query)))
                    if path == "/api/export":
                        return self._serve_export(self._month_param(query))
                elif method == "POST":
                    if path == "/api/categories":
                        return self._create_category()
                    if path == "/api/transactions":
                        return self._create_transaction()
                elif method == "PUT":
                    category_id = self._match_id(path, "/api/categories/")
                    if category_id is not None:
                        return self._update_category(category_id)
                    transaction_id = self._match_id(path, "/api/transactions/")
                    if transaction_id is not None:
                        return self._update_transaction(transaction_id)
                elif method == "DELETE":
                    transaction_id = self._match_id(path, "/api/transactions/")
                    if transaction_id is not None:
                        return self._delete_transaction(transaction_id)
                self._send_error_json(404, "接口不存在")
            except ValidationError as exc:
                self._send_error_json(400, str(exc))
            except DuplicateName as exc:
                self._send_error_json(409, str(exc))
            except NotFound as exc:
                self._send_error_json(404, str(exc))
            except MonthMismatch as exc:
                self._send_error_json(400, str(exc))
            except StoreError as exc:
                self._send_error_json(400, str(exc))
            except Exception:  # noqa: BLE001 - 始终返回 JSON，绝不抛出 HTML 500
                traceback.print_exc()
                self._send_error_json(500, "服务器内部错误")

        # ---- 静态资源 -------------------------------------------------
        def _serve_index(self):
            self._send_file(os.path.join(self.static_dir, "index.html"),
                            "text/html; charset=utf-8")

        def _serve_static(self, path):
            rel = path[len("/static/"):]
            if rel == "" or "/" in rel or rel.startswith("."):
                self._send_error_json(404, "资源不存在")
                return
            safe = os.path.basename(rel)
            extension = safe.rsplit(".", 1)[-1].lower() if "." in safe else ""
            content_type = CSS_TYPES.get(extension, "application/octet-stream")
            self._send_file(os.path.join(self.static_dir, safe), content_type)

        # ---- 业务处理 -------------------------------------------------
        def _create_category(self):
            body = self._read_json()
            month = body.get("month")
            if not isinstance(month, str) or not MONTH_RE.match(month.strip()):
                raise ValidationError("month 必须是 YYYY-MM 形式")
            name = body.get("name")
            if not isinstance(name, str) or not name.strip():
                raise ValidationError("分类名称不能为空")
            cents = self._amount(body.get("budget"), "预算")
            category_id = self.store.create_category(month.strip(), name.strip(), cents)
            self._send_json(201, {"id": category_id})

        def _update_category(self, category_id):
            body = self._read_json()
            cents = self._amount(body.get("budget"), "预算")
            info = self.store.update_category_budget(category_id, cents)
            self._send_json(200, {
                "id": info["id"],
                "month": info["month"],
                "name": info["name"],
                "budget": format_cents(cents),
            })

        def _create_transaction(self):
            body = self._read_json()
            date = self._date(body.get("date"))
            category_id = self._category_id(body.get("category_id"))
            cents = self._amount(body.get("amount"), "金额")
            note = self._note(body.get("note"))
            transaction_id = self.store.create_transaction(date, category_id, cents, note)
            self._send_json(201, {"id": transaction_id})

        def _update_transaction(self, transaction_id):
            body = self._read_json()
            date = self._date(body.get("date"))
            category_id = self._category_id(body.get("category_id"))
            cents = self._amount(body.get("amount"), "金额")
            note = self._note(body.get("note"))
            self.store.update_transaction(
                transaction_id, date, category_id, cents, note)
            self._send_json(200, {"id": transaction_id})

        def _delete_transaction(self, transaction_id):
            self.store.delete_transaction(transaction_id)
            self._send_json(200, {"id": transaction_id, "deleted": True})

        def _serve_export(self, month):
            rows = [["date", "category", "amount", "note"]]
            rows.extend(self.store.export_rows(month))
            buffer = io.StringIO(newline="")
            writer = csv.writer(buffer, lineterminator="\r\n")
            writer.writerows(rows)
            body = buffer.getvalue().encode("utf-8")
            self._send_bytes(
                200, body, "text/csv; charset=utf-8",
                [("Content-Disposition",
                  'attachment; filename="budget-%s.csv"' % month)],
            )

    return Handler
