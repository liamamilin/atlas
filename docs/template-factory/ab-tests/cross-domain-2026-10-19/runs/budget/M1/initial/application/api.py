"""HTTP JSON API and CSV export for the budget app.

This module contains no transport code: callers hand it a method, path, parsed
query and raw body, and receive (status, content_type, body_bytes, headers).
Every failure is raised as ApiError so the server can return non-2xx JSON.
"""

import csv
import io
import json
import re
import sqlite3
from contextlib import closing

import storage
from storage import ValidationError

MAX_BODY = 1 << 20

CATEGORY_RE = re.compile(r"^/api/categories/(\d+)$")
TRANSACTION_RE = re.compile(r"^/api/transactions/(\d+)$")


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def json_response(status, payload):
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    return status, "application/json; charset=utf-8", body, {}


def _parse_body(raw):
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ApiError(400, "请求体必须是有效的 JSON")
    if not isinstance(data, dict):
        raise ApiError(400, "请求体必须是 JSON 对象")
    return data


def _require_int(value, field):
    if isinstance(value, bool):
        raise ApiError(400, "%s 必须是整数" % field)
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.strip().isdecimal():
        return int(value.strip())
    raise ApiError(400, "%s 必须是整数" % field)


def _require_month(query):
    values = query.get("month") or []
    if not values or not values[0]:
        raise ApiError(400, "缺少 month 参数")
    return storage.validate_month(values[0])


# --- endpoints -------------------------------------------------------------

def _state(db_path, query):
    month = _require_month(query)
    with closing(storage.connect(db_path)) as conn:
        return json_response(200, storage.get_state(conn, month))


def _create_category(db_path, raw):
    data = _parse_body(raw)
    month = storage.validate_month(data.get("month"))
    name = storage.clean_name(data.get("name"))
    budget = storage.parse_money(data.get("budget"), allow_zero=True)
    with closing(storage.connect(db_path)) as conn:
        try:
            category_id = storage.create_category(conn, month, name, budget)
            conn.commit()
        except sqlite3.IntegrityError:
            raise ApiError(409, "该月份已存在同名分类：%s" % name)
    return json_response(201, {"id": category_id})


def _update_category(db_path, category_id, raw):
    data = _parse_body(raw)
    if "budget" not in data:
        raise ApiError(400, "缺少 budget 字段")
    budget = storage.parse_money(data.get("budget"), allow_zero=True)
    with closing(storage.connect(db_path)) as conn:
        if storage.get_category(conn, category_id) is None:
            raise ApiError(404, "分类不存在")
        storage.update_category_budget(conn, category_id, budget)
        conn.commit()
        row = storage.get_category(conn, category_id)
        entry = storage.category_entry(conn, row)
    return json_response(200, entry)


def _create_transaction(db_path, raw):
    data = _parse_body(raw)
    txn_date = storage.validate_date(data.get("date"))
    category_id = _require_int(data.get("category_id"), "category_id")
    amount = storage.parse_money(data.get("amount"), allow_zero=False)
    note = storage.clean_note(data.get("note"))
    with closing(storage.connect(db_path)) as conn:
        row = storage.get_category(conn, category_id)
        if row is None:
            raise ApiError(400, "分类不存在")
        if row["month"] != txn_date[:7]:
            raise ApiError(400, "支出日期必须属于分类所在月份 %s" % row["month"])
        transaction_id = storage.create_transaction(conn, txn_date, category_id, amount, note)
        conn.commit()
    return json_response(201, {"id": transaction_id})


def _update_transaction(db_path, transaction_id, raw):
    data = _parse_body(raw)
    txn_date = storage.validate_date(data.get("date"))
    category_id = _require_int(data.get("category_id"), "category_id")
    amount = storage.parse_money(data.get("amount"), allow_zero=False)
    note = storage.clean_note(data.get("note"))
    with closing(storage.connect(db_path)) as conn:
        if storage.get_transaction(conn, transaction_id) is None:
            raise ApiError(404, "支出记录不存在")
        row = storage.get_category(conn, category_id)
        if row is None:
            raise ApiError(400, "分类不存在")
        if row["month"] != txn_date[:7]:
            raise ApiError(400, "支出日期必须属于分类所在月份 %s" % row["month"])
        storage.update_transaction(conn, transaction_id, txn_date, category_id, amount, note)
        conn.commit()
        updated = storage.transaction_entry(conn, storage.get_transaction(conn, transaction_id))
    return json_response(200, updated)


def _delete_transaction(db_path, transaction_id):
    with closing(storage.connect(db_path)) as conn:
        if storage.get_transaction(conn, transaction_id) is None:
            raise ApiError(404, "支出记录不存在")
        storage.delete_transaction(conn, transaction_id)
        conn.commit()
    return json_response(200, {"id": transaction_id})


def _export(db_path, query):
    month = _require_month(query)
    with closing(storage.connect(db_path)) as conn:
        rows = storage.export_rows(conn, month)
    buf = io.StringIO(newline="")
    writer = csv.writer(buf)
    writer.writerow(["date", "category", "amount", "note"])
    for row in rows:
        writer.writerow([
            row["date"],
            row["category"],
            storage.format_money(row["amount_cents"]),
            row["note"],
        ])
    body = buf.getvalue().encode("utf-8")
    headers = {"Content-Disposition": 'attachment; filename="budget-%s.csv"' % month}
    return 200, "text/csv; charset=utf-8", body, headers


# --- dispatcher ------------------------------------------------------------

def dispatch(db_path, method, path, query, raw_body):
    try:
        return _dispatch(db_path, method, path, query, raw_body)
    except ValidationError as exc:
        raise ApiError(400, str(exc))


def _dispatch(db_path, method, path, query, raw_body):
    if method == "GET" and path == "/api/state":
        return _state(db_path, query)
    if method == "GET" and path == "/api/export":
        return _export(db_path, query)
    if method == "POST" and path == "/api/categories":
        return _create_category(db_path, raw_body)

    match = CATEGORY_RE.match(path)
    if match and method == "PUT":
        return _update_category(db_path, int(match.group(1)), raw_body)

    if method == "POST" and path == "/api/transactions":
        return _create_transaction(db_path, raw_body)

    match = TRANSACTION_RE.match(path)
    if match and method == "PUT":
        return _update_transaction(db_path, int(match.group(1)), raw_body)
    if match and method == "DELETE":
        return _delete_transaction(db_path, int(match.group(1)))

    raise ApiError(404, "未找到该接口")
