"""JSON API 路由与业务规则（服务端权限执行的核心）。

错误契约：所有校验失败抛 ApiError(status, message)，由 app.py 统一转为
非 2xx 的 JSON 形如 {"error": "可读原因"}，绝不返回伪成功。
"""

import time

import db
from security import (
    SESSION_COOKIE,
    SESSION_TTL_SECONDS,
    new_session_token,
    verify_password,
)
from timeutil import epoch_to_iso, parse_iso_instant


class ApiError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


class ApiResult:
    def __init__(self, status=200, data=None, set_cookie=None):
        self.status = status
        self.data = data
        self.set_cookie = set_cookie


# ---------------------------------------------------------------------------
# 入口
# ---------------------------------------------------------------------------

def handle_request(db_path, method, path, query, body, token):
    conn = db.connect(db_path)
    try:
        return _dispatch(conn, method, path, query, body, token)
    finally:
        conn.close()


def _dispatch(conn, method, path, query, body, token):
    if path == '/api/login' and method == 'POST':
        return _login(conn, body)
    if path == '/api/logout' and method == 'POST':
        return _logout(conn, token)
    if path == '/api/me' and method == 'GET':
        return ApiResult(200, {'user': _public_user(_require_user(conn, token))})

    if path == '/api/resources':
        if method == 'GET':
            _require_user(conn, token)
            return ApiResult(200, {'resources': _list_resources(conn)})
        if method == 'POST':
            _require_admin(_require_user(conn, token))
            return _create_resource(conn, body)

    if path == '/api/availability' and method == 'GET':
        _require_user(conn, token)
        return _availability(conn, query)

    if path == '/api/bookings':
        if method == 'GET':
            return ApiResult(200, {'bookings': _list_bookings(conn, _require_user(conn, token))})
        if method == 'POST':
            return _create_booking(conn, _require_user(conn, token), body)

    prefix = '/api/bookings/'
    if path.startswith(prefix):
        rest = path[len(prefix):]
        if rest.endswith('/cancel') and method == 'POST':
            booking_id = _parse_int(rest[:-len('/cancel')], '无效的预约编号')
            user = _require_user(conn, token)
            return _cancel_booking(conn, user, booking_id)
        if method == 'GET':
            booking_id = _parse_int(rest, '无效的预约编号')
            user = _require_user(conn, token)
            return _get_booking(conn, user, booking_id)

    raise ApiError(404, '未找到接口：%s %s' % (method, path))


# ---------------------------------------------------------------------------
# 会话与授权
# ---------------------------------------------------------------------------

def _require_user(conn, token):
    user = _session_user(conn, token)
    if user is None:
        raise ApiError(401, '请先登录')
    return user


def _session_user(conn, token):
    if not token:
        return None
    row = conn.execute(
        'SELECT u.id AS id, u.username AS username, u.role AS role '
        'FROM sessions s JOIN users u ON u.id = s.user_id '
        'WHERE s.token = ? AND s.expires_at > ?',
        (token, int(time.time())),
    ).fetchone()
    return dict(row) if row else None


def _require_admin(user):
    if user['role'] != 'admin':
        raise ApiError(403, '只有管理员可以执行该操作')


def _public_user(user):
    return {'id': user['id'], 'username': user['username'], 'role': user['role']}


def _login(conn, body):
    body = _as_object(body)
    username = body.get('username')
    password = body.get('password')
    if not isinstance(username, str) or not username.strip() or not isinstance(password, str) or password == '':
        raise ApiError(400, '用户名和密码不能为空')
    row = conn.execute(
        'SELECT id, username, role, password_hash FROM users WHERE username = ?',
        (username.strip(),),
    ).fetchone()
    if row is None or not verify_password(password, row['password_hash']):
        raise ApiError(401, '用户名或密码错误')
    token = new_session_token()
    now = int(time.time())
    conn.execute(
        'INSERT INTO sessions (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)',
        (token, row['id'], now, now + SESSION_TTL_SECONDS),
    )
    cookie = '%s=%s; Path=/; HttpOnly; SameSite=Lax; Max-Age=%d' % (
        SESSION_COOKIE, token, SESSION_TTL_SECONDS)
    return ApiResult(200, {'user': {'id': row['id'], 'username': row['username'], 'role': row['role']}},
                     set_cookie=cookie)


def _logout(conn, token):
    if token:
        conn.execute('DELETE FROM sessions WHERE token = ?', (token,))
    cookie = '%s=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0' % SESSION_COOKIE
    return ApiResult(200, {'ok': True}, set_cookie=cookie)


# ---------------------------------------------------------------------------
# 设施
# ---------------------------------------------------------------------------

def _list_resources(conn):
    rows = conn.execute('SELECT id, name FROM resources WHERE active = 1 ORDER BY id').fetchall()
    return [{'id': row['id'], 'name': row['name']} for row in rows]


def _create_resource(conn, body):
    body = _as_object(body)
    name = body.get('name')
    if not isinstance(name, str) or not name.strip():
        raise ApiError(400, '设施名称不能为空')
    cur = conn.execute(
        'INSERT INTO resources (name, active, created_at) VALUES (?, 1, ?)',
        (name.strip()[:120], int(time.time())),
    )
    return ApiResult(201, {'id': cur.lastrowid})


def _availability(conn, query):
    raw = query.get('resource_id', [None])[0]
    resource_id = _parse_int(raw, '缺少或非法的 resource_id')
    if _fetch_resource(conn, resource_id) is None:
        raise ApiError(404, '设施不存在')
    rows = conn.execute(
        "SELECT start_iso, end_iso FROM bookings "
        "WHERE resource_id = ? AND status = 'active' ORDER BY start_epoch, id",
        (resource_id,),
    ).fetchall()
    return ApiResult(200, {'slots': [{'start': row['start_iso'], 'end': row['end_iso']} for row in rows]})


# ---------------------------------------------------------------------------
# 预约
# ---------------------------------------------------------------------------

def _booking_public(row):
    return {
        'id': row['id'],
        'resource_id': row['resource_id'],
        'owner_id': row['owner_id'],
        'start': row['start_iso'],
        'end': row['end_iso'],
        'note': row['note'],
        'status': row['status'],
    }


def _list_bookings(conn, user):
    if user['role'] == 'admin':
        rows = conn.execute('SELECT * FROM bookings ORDER BY start_epoch, id').fetchall()
    else:
        rows = conn.execute(
            'SELECT * FROM bookings WHERE owner_id = ? ORDER BY start_epoch, id',
            (user['id'],),
        ).fetchall()
    return [_booking_public(row) for row in rows]


def _get_booking(conn, user, booking_id):
    row = _fetch_booking(conn, booking_id)
    if row is None:
        raise ApiError(404, '预约不存在')
    _authorize_owner_or_admin(user, row)
    return ApiResult(200, {'booking': _booking_public(row)})


def _create_booking(conn, user, body):
    body = _as_object(body)
    resource_id = _parse_int(body.get('resource_id'), '缺少或非法的 resource_id')
    try:
        start_epoch = parse_iso_instant(body.get('start'))
        end_epoch = parse_iso_instant(body.get('end'))
    except ValueError as exc:
        raise ApiError(400, str(exc)) from None
    if end_epoch <= start_epoch:
        raise ApiError(400, '结束时间必须晚于开始时间')

    note = body.get('note', '')
    if note is None:
        note = ''
    if not isinstance(note, str):
        note = str(note)
    note = note.strip()[:500]

    now = int(time.time())
    conn.execute('BEGIN IMMEDIATE')
    try:
        if _fetch_resource(conn, resource_id) is None:
            raise ApiError(404, '设施不存在')
        # 半开区间重叠：existing.start < new.end AND existing.end > new.start
        clash = conn.execute(
            "SELECT 1 FROM bookings WHERE resource_id = ? AND status = 'active' "
            'AND start_epoch < ? AND end_epoch > ? LIMIT 1',
            (resource_id, end_epoch, start_epoch),
        ).fetchone()
        if clash is not None:
            raise ApiError(409, '该设施在所选时段已被预约')
        cur = conn.execute(
            'INSERT INTO bookings (resource_id, owner_id, start_epoch, end_epoch, '
            'start_iso, end_iso, note, status, created_at) '
            "VALUES (?, ?, ?, ?, ?, ?, ?, 'active', ?)",
            (resource_id, user['id'], start_epoch, end_epoch,
             epoch_to_iso(start_epoch), epoch_to_iso(end_epoch), note, now),
        )
        booking_id = cur.lastrowid
        conn.execute('COMMIT')
    except ApiError:
        conn.execute('ROLLBACK')
        raise
    except Exception:
        conn.execute('ROLLBACK')
        raise
    return ApiResult(201, {'id': booking_id})


def _cancel_booking(conn, user, booking_id):
    now = int(time.time())
    conn.execute('BEGIN IMMEDIATE')
    try:
        row = _fetch_booking(conn, booking_id)
        if row is None:
            raise ApiError(404, '预约不存在')
        _authorize_owner_or_admin(user, row)
        if row['status'] == 'active':
            conn.execute(
                "UPDATE bookings SET status = 'cancelled', cancelled_at = ? WHERE id = ?",
                (now, booking_id),
            )
        conn.execute('COMMIT')
    except ApiError:
        conn.execute('ROLLBACK')
        raise
    except Exception:
        conn.execute('ROLLBACK')
        raise
    updated = _fetch_booking(conn, booking_id)
    return ApiResult(200, {'booking': _booking_public(updated)})


def _authorize_owner_or_admin(user, row):
    if user['role'] != 'admin' and row['owner_id'] != user['id']:
        raise ApiError(403, '无权访问他人的预约')


# ---------------------------------------------------------------------------
# 小工具
# ---------------------------------------------------------------------------

def _fetch_resource(conn, resource_id):
    return conn.execute(
        'SELECT id, name FROM resources WHERE id = ? AND active = 1', (resource_id,)
    ).fetchone()


def _fetch_booking(conn, booking_id):
    return conn.execute('SELECT * FROM bookings WHERE id = ?', (booking_id,)).fetchone()


def _as_object(body):
    if not isinstance(body, dict):
        raise ApiError(400, '请求体必须是 JSON 对象')
    return body


def _parse_int(value, message):
    if isinstance(value, bool):
        raise ApiError(400, message)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        text = value.strip()
        if text.lstrip('-').isdigit():
            return int(text)
    raise ApiError(400, message)
