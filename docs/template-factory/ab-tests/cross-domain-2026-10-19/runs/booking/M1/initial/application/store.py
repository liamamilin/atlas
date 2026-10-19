"""业务数据访问层：设施、可用性、预约与取消。

重叠唯一占用：写入走 BEGIN IMMEDIATE 串行事务，先按半开区间语义
（existing.start < new.end AND existing.end > new.start）SELECT 重叠，
命中返回 409；另有部分唯一索引作为同起点守卫。
"""
import sqlite3
import time


class ApiError(Exception):
    """携带 HTTP 状态码与可读原因的业务错误。"""

    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def _serialize(row):
    return {
        "id": row["id"],
        "resource_id": row["resource_id"],
        "owner_id": row["owner_id"],
        "start": row["start_iso"],
        "end": row["end_iso"],
        "note": row["note"],
        "status": row["status"],
    }


def resource_exists(conn, resource_id):
    return conn.execute(
        "SELECT 1 FROM resources WHERE id = ?", (resource_id,)
    ).fetchone() is not None


def list_resources(conn):
    rows = conn.execute(
        "SELECT id, name FROM resources WHERE active = 1 ORDER BY id"
    ).fetchall()
    return [{"id": row["id"], "name": row["name"]} for row in rows]


def create_resource(conn, name):
    if not isinstance(name, str) or not name.strip():
        raise ApiError(400, "设施名称不能为空")
    name = name.strip()
    if len(name) > 200:
        raise ApiError(400, "设施名称过长（最多 200 字）")
    cursor = conn.execute("INSERT INTO resources (name, active) VALUES (?, 1)", (name,))
    return {"id": cursor.lastrowid, "name": name}


def availability(conn, resource_id):
    """仅返回 active 预约的时段，且只含 start/end，不泄露他人个人细节。"""
    rows = conn.execute(
        "SELECT start_iso, end_iso FROM bookings "
        "WHERE resource_id = ? AND status = 'active' ORDER BY start_epoch",
        (resource_id,),
    ).fetchall()
    return [{"start": row["start_iso"], "end": row["end_iso"]} for row in rows]


def create_booking(conn, resource_id, owner_id, start_epoch, end_epoch,
                   start_iso, end_iso, note):
    if end_epoch <= start_epoch:
        raise ApiError(400, "结束时间必须晚于开始时间")
    try:
        conn.execute("BEGIN IMMEDIATE")
    except sqlite3.OperationalError:
        raise ApiError(409, "系统繁忙，请稍后重试") from None
    try:
        overlap = conn.execute(
            "SELECT id FROM bookings WHERE resource_id = ? AND status = 'active' "
            "AND start_epoch < ? AND end_epoch > ?",
            (resource_id, end_epoch, start_epoch),
        ).fetchone()
        if overlap is not None:
            conn.execute("ROLLBACK")
            raise ApiError(409, "该设施在所选时段已被预约")
        cursor = conn.execute(
            "INSERT INTO bookings "
            "(resource_id, owner_id, start_epoch, end_epoch, start_iso, end_iso, "
            " note, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, 'active', ?)",
            (resource_id, owner_id, start_epoch, end_epoch, start_iso, end_iso,
             note, int(time.time())),
        )
        booking_id = cursor.lastrowid
        conn.execute("COMMIT")
    except ApiError:
        raise
    except sqlite3.IntegrityError:
        conn.execute("ROLLBACK")
        raise ApiError(409, "该设施在所选时段已被预约") from None
    except Exception:
        conn.execute("ROLLBACK")
        raise
    return booking_id


def list_bookings(conn, user):
    if user["role"] == "admin":
        rows = conn.execute("SELECT * FROM bookings ORDER BY id").fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM bookings WHERE owner_id = ? ORDER BY id", (user["id"],)
        ).fetchall()
    return [_serialize(row) for row in rows]


def get_booking(conn, booking_id):
    row = conn.execute("SELECT * FROM bookings WHERE id = ?", (booking_id,)).fetchone()
    return _serialize(row) if row is not None else None


def cancel_booking(conn, booking_id, user):
    """软取消：保留行、status=cancelled，重复取消幂等返回同一记录。"""
    try:
        conn.execute("BEGIN IMMEDIATE")
    except sqlite3.OperationalError:
        raise ApiError(409, "系统繁忙，请稍后重试") from None
    try:
        row = conn.execute("SELECT * FROM bookings WHERE id = ?", (booking_id,)).fetchone()
        if row is None:
            conn.execute("ROLLBACK")
            raise ApiError(404, "预约不存在")
        if user["role"] != "admin" and row["owner_id"] != user["id"]:
            conn.execute("ROLLBACK")
            raise ApiError(403, "不能取消他人的预约")
        if row["status"] != "cancelled":
            conn.execute(
                "UPDATE bookings SET status = 'cancelled', cancelled_at = ? WHERE id = ?",
                (int(time.time()), booking_id),
            )
        conn.execute("COMMIT")
    except ApiError:
        raise
    except Exception:
        conn.execute("ROLLBACK")
        raise
    return get_booking(conn, booking_id)
