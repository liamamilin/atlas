"""HTTP 处理器：JSON API 路由、静态页面与统一错误契约。

错误契约：校验失败一律非 2xx 且响应体为 {"error": "可读原因"}
（400 参数非法、401 未登录、403 越权、404 不存在、409 重叠）。
"""
import http.cookies
import json
import os
import re
import urllib.parse
from http.server import BaseHTTPRequestHandler

import auth
import db
import isoutil
import store
from store import ApiError

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

_ASSETS = {
    "/static/app.js": ("app.js", "application/javascript; charset=utf-8"),
    "/static/style.css": ("style.css", "text/css; charset=utf-8"),
}


class AtlasHandler(BaseHTTPRequestHandler):
    server_version = "TrialBooking/1.0"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # 保持 stdout 安静，避免泄露请求细节
        pass

    # -- 入口 --------------------------------------------------------------
    def do_GET(self):
        self._handle("GET")

    def do_POST(self):
        self._handle("POST")

    def _handle(self, method):
        try:
            parsed = urllib.parse.urlsplit(self.path)
            path = parsed.path or "/"
            query = urllib.parse.parse_qs(parsed.query)
            if method == "GET":
                if path == "/":
                    return self._serve_index()
                if path in _ASSETS:
                    return self._serve_asset(path)
                if path.startswith("/api/"):
                    return self._api_get(path, query)
            else:
                if path.startswith("/api/"):
                    return self._api_post(path)
            self._send_json(404, {"error": "未找到该资源"})
        except ApiError as exc:
            self._send_json(exc.status, {"error": exc.message})
        except Exception:
            self._send_json(500, {"error": "服务器内部错误"})

    # -- API：读 -----------------------------------------------------------
    def _api_get(self, path, query):
        conn = db.connect(self.server.db_path)
        try:
            if path == "/api/me":
                user = self._current_user(conn)
                if user is None:
                    raise ApiError(401, "未登录或会话已失效")
                return self._send_json(200, {"user": user})
            if path == "/api/resources":
                self._require_user(conn)
                return self._send_json(200, {"resources": store.list_resources(conn)})
            if path == "/api/availability":
                self._require_user(conn)
                resource_id = self._int_param(query, "resource_id")
                if not store.resource_exists(conn, resource_id):
                    raise ApiError(404, "设施不存在")
                return self._send_json(200, {"slots": store.availability(conn, resource_id)})
            if path == "/api/bookings":
                user = self._require_user(conn)
                return self._send_json(200, {"bookings": store.list_bookings(conn, user)})
            match = re.fullmatch(r"/api/bookings/(\d+)", path)
            if match:
                user = self._require_user(conn)
                booking = store.get_booking(conn, int(match.group(1)))
                if booking is None:
                    raise ApiError(404, "预约不存在")
                if user["role"] != "admin" and booking["owner_id"] != user["id"]:
                    raise ApiError(403, "无权查看他人的预约")
                return self._send_json(200, {"booking": booking})
            raise ApiError(404, "未找到该资源")
        finally:
            conn.close()

    # -- API：写 -----------------------------------------------------------
    def _api_post(self, path):
        raw = self._read_body()
        conn = db.connect(self.server.db_path)
        try:
            if path == "/api/login":
                return self._login(conn, self._parse_json(raw))
            if path == "/api/logout":
                return self._logout(conn)
            if path == "/api/resources":
                user = self._require_user(conn)
                if user["role"] != "admin":
                    raise ApiError(403, "仅管理员可以创建设施")
                data = self._parse_json(raw)
                resource = store.create_resource(conn, data.get("name"))
                return self._send_json(201, {"id": resource["id"], "name": resource["name"]})
            if path == "/api/bookings":
                return self._create_booking(conn, self._parse_json(raw))
            match = re.fullmatch(r"/api/bookings/(\d+)/cancel", path)
            if match:
                user = self._require_user(conn)
                booking = store.cancel_booking(conn, int(match.group(1)), user)
                return self._send_json(200, {"booking": booking})
            raise ApiError(404, "未找到该资源")
        finally:
            conn.close()

    def _login(self, conn, data):
        username = data.get("username")
        password = data.get("password")
        if not isinstance(username, str) or not isinstance(password, str):
            raise ApiError(400, "用户名和密码必须是字符串")
        row = conn.execute(
            "SELECT id, username, role, password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        if row is None or not auth.verify_password(password, row["password_hash"]):
            raise ApiError(401, "用户名或密码错误")
        token = auth.create_session(conn, row["id"])
        user = {"id": row["id"], "username": row["username"], "role": row["role"]}
        return self._send_json(200, {"user": user}, set_cookie=auth.session_cookie(token))

    def _logout(self, conn):
        auth.delete_session(conn, self._cookie(auth.COOKIE_NAME))
        return self._send_json(200, {"ok": True}, set_cookie=auth.clear_cookie())

    def _create_booking(self, conn, data):
        user = self._require_user(conn)
        resource_id = self._as_int(data.get("resource_id"), "resource_id")
        if not store.resource_exists(conn, resource_id):
            raise ApiError(404, "设施不存在")
        start_epoch = self._parse_time(data.get("start"), "开始时间")
        end_epoch = self._parse_time(data.get("end"), "结束时间")
        if end_epoch <= start_epoch:
            raise ApiError(400, "结束时间必须晚于开始时间")
        note = data.get("note") or ""
        if not isinstance(note, str):
            raise ApiError(400, "备注必须是字符串")
        if len(note) > 1000:
            raise ApiError(400, "备注过长（最多 1000 字）")
        booking_id = store.create_booking(
            conn, resource_id, user["id"], start_epoch, end_epoch,
            isoutil.format_instant(start_epoch), isoutil.format_instant(end_epoch), note,
        )
        booking = store.get_booking(conn, booking_id)
        return self._send_json(201, {"id": booking_id, "booking": booking})

    # -- 请求辅助 ----------------------------------------------------------
    def _require_user(self, conn):
        user = self._current_user(conn)
        if user is None:
            raise ApiError(401, "未登录或会话已失效")
        return user

    def _current_user(self, conn):
        return auth.session_user(conn, self._cookie(auth.COOKIE_NAME))

    def _cookie(self, name):
        header = self.headers.get("Cookie")
        if not header:
            return None
        jar = http.cookies.SimpleCookie()
        try:
            jar.load(header)
        except http.cookies.CookieError:
            return None
        morsel = jar.get(name)
        return morsel.value if morsel is not None else None

    def _read_body(self):
        length = self.headers.get("Content-Length")
        try:
            size = int(length) if length else 0
        except (TypeError, ValueError):
            size = 0
        if size <= 0:
            return b""
        return self.rfile.read(size)

    def _parse_json(self, raw):
        if not raw:
            return {}
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            raise ApiError(400, "请求体不是合法的 JSON") from None
        if not isinstance(data, dict):
            raise ApiError(400, "请求体必须是 JSON 对象")
        return data

    def _parse_time(self, value, label):
        try:
            return isoutil.parse_instant(value)
        except ValueError as exc:
            raise ApiError(400, "%s：%s" % (label, exc)) from None

    def _as_int(self, value, field):
        if isinstance(value, bool):
            raise ApiError(400, "%s 必须是整数" % field)
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            text = value.strip()
            if text.lstrip("-").isdigit():
                return int(text)
        raise ApiError(400, "%s 必须是整数" % field)

    def _int_param(self, query, key):
        values = query.get(key)
        if not values:
            raise ApiError(400, "缺少参数 %s" % key)
        return self._as_int(values[0], key)

    # -- 响应与静态资源 ----------------------------------------------------
    def _send_json(self, status, payload, set_cookie=None):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        if set_cookie:
            self.send_header("Set-Cookie", set_cookie)
        self.end_headers()
        self.wfile.write(body)

    def _serve_bytes(self, body, content_type):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _serve_index(self):
        self._serve_bytes(self._read_asset("index.html"), "text/html; charset=utf-8")

    def _serve_asset(self, path):
        filename, content_type = _ASSETS[path]
        self._serve_bytes(self._read_asset(filename), content_type)

    def _read_asset(self, filename):
        with open(os.path.join(STATIC_DIR, filename), "rb") as handle:
            return handle.read()
