"""HTTP 路由与 JSON 接口。

每个请求被解析成 (method, path, query, body)，返回 (status, headers, body) 三元组。
"""

import json
import re
from urllib.parse import parse_qs

from storage import StorageError

JSON_HEADERS = [("Content-Type", "application/json; charset=utf-8")]
TEXT_HEADERS = [("Content-Type", "text/plain; charset=utf-8")]


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def _json_body(raw):
    if not raw:
        return {}
    try:
        data = json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise ApiError(400, "请求内容不是有效的 JSON")
    if not isinstance(data, dict):
        raise ApiError(400, "请求内容格式不正确")
    return data


def _int_id(segment):
    try:
        value = int(segment)
    except (TypeError, ValueError):
        raise ApiError(404, "找不到对应资源")
    if value <= 0:
        raise ApiError(404, "找不到对应资源")
    return value


def _category_filter(query):
    raw = query.get("category_id", [None])[0]
    if raw in (None, "", "all"):
        return None
    try:
        return int(raw)
    except (TypeError, ValueError):
        raise ApiError(400, "归类编号无效")


BOOKMARK_ITEM = re.compile(r"^/api/bookmarks/(\d+)$")
BOOKMARK_OPEN = re.compile(r"^/api/bookmarks/(\d+)/open$")
CATEGORY_ITEM = re.compile(r"^/api/categories/(\d+)$")


def handle(storage, method, path, raw_query, body):
    query = parse_qs(raw_query or "")

    if path == "/api/state" and method == "GET":
        categories = storage.list_categories()
        return 200, JSON_HEADERS, {
            "categories": categories,
            "default_category_id": storage.default_category_id(),
            "stats": storage.stats(),
        }

    if path == "/api/bookmarks" and method == "GET":
        items = storage.list_bookmarks(
            category_id=_category_filter(query),
            query=query.get("q", [""])[0],
        )
        return 200, JSON_HEADERS, {"bookmarks": items, "count": len(items)}

    if path == "/api/bookmarks" and method == "POST":
        data = _json_body(body)
        record = storage.create_bookmark(
            url=data.get("url"),
            title=data.get("title", ""),
            note=data.get("note", ""),
            category_id=data.get("category_id"),
        )
        return 201, JSON_HEADERS, {"bookmark": record}

    match = BOOKMARK_ITEM.match(path)
    if match:
        bookmark_id = _int_id(match.group(1))
        if method in ("PUT", "PATCH"):
            record = storage.update_bookmark(bookmark_id, _json_body(body))
            return 200, JSON_HEADERS, {"bookmark": record}
        if method == "DELETE":
            return 200, JSON_HEADERS, storage.delete_bookmark(bookmark_id)

    match = BOOKMARK_OPEN.match(path)
    if match and method == "POST":
        url = storage.record_open(_int_id(match.group(1)))
        return 200, JSON_HEADERS, {"url": url}

    if path == "/api/categories" and method == "POST":
        data = _json_body(body)
        return 201, JSON_HEADERS, {"category": storage.create_category(data.get("name"))}

    match = CATEGORY_ITEM.match(path)
    if match:
        category_id = _int_id(match.group(1))
        if method in ("PUT", "PATCH"):
            data = _json_body(body)
            return 200, JSON_HEADERS, {"category": storage.rename_category(category_id, data.get("name"))}
        if method == "DELETE":
            return 200, JSON_HEADERS, storage.delete_category(category_id)

    if path.startswith("/api/"):
        return 404, JSON_HEADERS, {"error": "接口不存在"}
    return 404, TEXT_HEADERS, "未找到该页面"


def dispatch(storage, method, path, raw_query, body):
    """把异常统一转换成结构化响应，保证界面总能收到可读的错误信息。"""
    try:
        return handle(storage, method, path, raw_query, body)
    except ApiError as exc:
        return exc.status, JSON_HEADERS, {"error": exc.message}
    except StorageError as exc:
        return 400, JSON_HEADERS, {"error": str(exc)}
    except Exception:
        return 500, JSON_HEADERS, {"error": "服务器内部错误，请稍后重试"}


def encode(payload):
    if isinstance(payload, (dict, list)):
        return json.dumps(payload, ensure_ascii=False).encode("utf-8")
    return str(payload).encode("utf-8")
