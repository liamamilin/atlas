"""JSON HTTP API 的业务逻辑与路由。

每个处理函数返回 (status, payload, cookies)，cookies 为 (名称, 值或 None) 列表，
值为 None 表示清除该 cookie。校验失败一律抛出 ApiError（非 2xx，带中文原因）。
"""
import re

import auth
import db
import times


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def err(status, message):
    raise ApiError(status, message)


def require_user(user):
    if user is None:
        err(401, "请先登录")


def require_admin(user):
    require_user(user)
    if user.get("role") != "admin":
        err(403, "只有管理员可以执行此操作")


def _first(query, key):
    values = query.get(key)
    if not values:
        return None
    return values[0]


def _booking_dict(row):
    return {
        "id": row["id"],
        "resource_id": row["resource_id"],
        "start": times.to_iso(row["start_ts"]),
        "end": times.to_iso(row["end_ts"]),
        "note": row["note"],
        "status": row["status"],
        "owner_id": row["owner_id"],
    }


# ---------------------------------------------------------------- 账号/会话

def login(body):
    username = body.get("username")
    password = body.get("password")
    if not isinstance(username, str) or not username.strip():
        err(400, "用户名不能为空")
    if not isinstance(password, str) or not password:
        err(400, "密码不能为空")
    conn = db.connect()
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username.strip(),)
        ).fetchone()
    finally:
        conn.close()
    if row is None or not auth.verify_password(password, row["salt"], row["password_hash"]):
        err(401, "用户名或密码错误")
    token = auth.create_session(row["id"])
    user = {"id": row["id"], "username": row["username"], "role": row["role"]}
    return 200, {"user": user}, [("session", token)]


def logout(token):
    auth.delete_session(token)
    return 200, {"ok": True}, [("session", None)]


def me(user):
    if user is None:
        err(401, "未登录")
    return 200, {"user": user}, []


# ---------------------------------------------------------------- 设施

def resources_list():
    conn = db.connect()
    try:
        rows = conn.execute(
            "SELECT id, name FROM resources ORDER BY id"
        ).fetchall()
    finally:
        conn.close()
    return 200, {"resources": [{"id": r["id"], "name": r["name"]} for r in rows]}, []


def resources_create(user, body):
    require_admin(user)
    name = body.get("name")
    if not isinstance(name, str) or not name.strip():
        err(400, "设施名称不能为空")
    name = name.strip()
    conn = db.connect()
    try:
        cur = conn.execute(
            "INSERT INTO resources(name, created_at) VALUES(?,?)",
            (name, times.now_iso()),
        )
        rid = cur.lastrowid
    finally:
        conn.close()
    return 200, {"id": rid}, []


def availability(query):
    raw = _first(query, "resource_id")
    if raw is None:
        err(400, "缺少 resource_id")
    try:
        resource_id = int(raw)
    except (TypeError, ValueError):
        err(400, "resource_id 必须是整数")
    conn = db.connect()
    try:
        if conn.execute(
            "SELECT id FROM resources WHERE id = ?", (resource_id,)
        ).fetchone() is None:
            err(404, "设施不存在")
        rows = conn.execute(
            "SELECT start_ts, end_ts FROM bookings"
            " WHERE resource_id = ? AND status = 'active' ORDER BY start_ts",
            (resource_id,),
        ).fetchall()
    finally:
        conn.close()
    slots = [
        {"start": times.to_iso(r["start_ts"]), "end": times.to_iso(r["end_ts"])}
        for r in rows
    ]
    return 200, {"slots": slots}, []


# ---------------------------------------------------------------- 预约

def bookings_create(user, body):
    require_user(user)
    raw_rid = body.get("resource_id")
    try:
        resource_id = int(raw_rid)
    except (TypeError, ValueError):
        err(400, "resource_id 必须是整数")

    try:
        start_ts = times.parse_instant(body.get("start"))
        end_ts = times.parse_instant(body.get("end"))
    except times.TimeError as exc:
        err(400, str(exc))
    if end_ts <= start_ts:
        err(400, "结束时间必须晚于开始时间")

    note = body.get("note", "")
    if note is None:
        note = ""
    if not isinstance(note, str):
        err(400, "备注必须是字符串")

    conn = db.connect()
    try:
        conn.execute("BEGIN IMMEDIATE")
        if conn.execute(
            "SELECT id FROM resources WHERE id = ?", (resource_id,)
        ).fetchone() is None:
            conn.execute("ROLLBACK")
            err(404, "设施不存在")
        clash = conn.execute(
            "SELECT id FROM bookings"
            " WHERE resource_id = ? AND status = 'active'"
            "   AND start_ts < ? AND ? < end_ts",
            (resource_id, end_ts, start_ts),
        ).fetchone()
        if clash is not None:
            conn.execute("ROLLBACK")
            err(409, "该时段与已有预约重叠，请另选时间")
        cur = conn.execute(
            "INSERT INTO bookings(resource_id, owner_id, start_ts, end_ts, note,"
            " status, created_at) VALUES(?,?,?,?,?,'active',?)",
            (resource_id, user["id"], start_ts, end_ts, note, times.now_iso()),
        )
        booking_id = cur.lastrowid
        conn.execute("COMMIT")
    except ApiError:
        raise
    except Exception:
        try:
            conn.execute("ROLLBACK")
        except Exception:
            pass
        raise
    finally:
        conn.close()
    return 200, {"id": booking_id}, []


def bookings_list(user):
    require_user(user)
    conn = db.connect()
    try:
        if user["role"] == "admin":
            rows = conn.execute(
                "SELECT * FROM bookings ORDER BY start_ts, id"
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM bookings WHERE owner_id = ? ORDER BY start_ts, id",
                (user["id"],),
            ).fetchall()
    finally:
        conn.close()
    return 200, {"bookings": [_booking_dict(r) for r in rows]}, []


def bookings_get(user, booking_id):
    require_user(user)
    conn = db.connect()
    try:
        row = conn.execute(
            "SELECT * FROM bookings WHERE id = ?", (booking_id,)
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        err(404, "预约不存在")
    if user["role"] != "admin" and row["owner_id"] != user["id"]:
        err(403, "无权查看他人的预约")
    return 200, _booking_dict(row), []


def bookings_cancel(user, booking_id):
    require_user(user)
    conn = db.connect()
    try:
        conn.execute("BEGIN IMMEDIATE")
        row = conn.execute(
            "SELECT * FROM bookings WHERE id = ?", (booking_id,)
        ).fetchone()
        if row is None:
            conn.execute("ROLLBACK")
            err(404, "预约不存在")
        if user["role"] != "admin" and row["owner_id"] != user["id"]:
            conn.execute("ROLLBACK")
            err(403, "无权取消他人的预约")
        if row["status"] != "cancelled":
            conn.execute(
                "UPDATE bookings SET status = 'cancelled', cancelled_at = ?"
                " WHERE id = ?",
                (times.now_iso(), booking_id),
            )
        updated = conn.execute(
            "SELECT * FROM bookings WHERE id = ?", (booking_id,)
        ).fetchone()
        conn.execute("COMMIT")
    except ApiError:
        raise
    except Exception:
        try:
            conn.execute("ROLLBACK")
        except Exception:
            pass
        raise
    finally:
        conn.close()
    return 200, _booking_dict(updated), []


# ---------------------------------------------------------------- 路由

_CANCEL_RE = re.compile(r"^/api/bookings/(\d+)/cancel$")
_BOOKING_RE = re.compile(r"^/api/bookings/(\d+)$")


def dispatch(method, path, query, body, user, token):
    if method == "POST" and path == "/api/login":
        return login(body)
    if method == "POST" and path == "/api/logout":
        return logout(token)
    if method == "GET" and path == "/api/me":
        return me(user)
    if path == "/api/resources":
        if method == "GET":
            return resources_list()
        if method == "POST":
            return resources_create(user, body)
    if method == "GET" and path == "/api/availability":
        return availability(query)
    if path == "/api/bookings":
        if method == "GET":
            return bookings_list(user)
        if method == "POST":
            return bookings_create(user, body)
    match = _CANCEL_RE.match(path)
    if match and method == "POST":
        return bookings_cancel(user, int(match.group(1)))
    match = _BOOKING_RE.match(path)
    if match:
        if method == "GET":
            return bookings_get(user, int(match.group(1)))
    err(404, "接口不存在")
