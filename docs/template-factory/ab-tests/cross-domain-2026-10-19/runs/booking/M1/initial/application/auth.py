"""认证与会话（纯标准库）。

口令使用 PBKDF2-HMAC-SHA256 加盐哈希存储；会话由服务端持有，
角色与 owner 只取自服务端会话，绝不信任客户端提交的 user_id/role。
"""
import hashlib
import hmac
import http.cookies
import secrets
import time

COOKIE_NAME = "session"
SESSION_TTL_SECONDS = 12 * 3600
_PBKDF2_ROUNDS = 120000
_DEMO_USERS = (
    ("admin", "AtlasDemo-Admin-9!", "admin"),
    ("alice", "AtlasDemo-Alice-9!", "resident"),
    ("bob", "AtlasDemo-Bob-9!", "resident"),
)


def hash_password(password):
    salt = secrets.token_bytes(16)
    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _PBKDF2_ROUNDS)
    return "pbkdf2_sha256$%d$%s$%s" % (_PBKDF2_ROUNDS, salt.hex(), derived.hex())


def verify_password(password, stored):
    if not isinstance(stored, str):
        return False
    parts = stored.split("$")
    if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
        return False
    try:
        rounds = int(parts[1])
        salt = bytes.fromhex(parts[2])
    except (ValueError, TypeError):
        return False
    derived = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, rounds)
    return hmac.compare_digest(derived.hex(), parts[3])


def seed_demo_users(conn):
    """本地实验种子账号：仅在缺失时插入，绝不重置既有账户或记录。"""
    for username, password, role in _DEMO_USERS:
        row = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if row is None:
            conn.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, hash_password(password), role),
            )


def create_session(conn, user_id):
    token = secrets.token_urlsafe(32)
    expires_at = int(time.time()) + SESSION_TTL_SECONDS
    conn.execute(
        "INSERT INTO sessions (token, user_id, expires_at) VALUES (?, ?, ?)",
        (token, user_id, expires_at),
    )
    return token


def session_user(conn, token):
    """返回 {'id','username','role'} 或 None。"""
    if not token:
        return None
    row = conn.execute(
        "SELECT s.expires_at AS expires_at, u.id AS uid, u.username AS username, u.role AS role "
        "FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token = ?",
        (token,),
    ).fetchone()
    if row is None:
        return None
    if row["expires_at"] <= int(time.time()):
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))
        return None
    return {"id": row["uid"], "username": row["username"], "role": row["role"]}


def delete_session(conn, token):
    if token:
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))


def session_cookie(token):
    cookie = http.cookies.SimpleCookie()
    cookie[COOKIE_NAME] = token
    cookie[COOKIE_NAME]["path"] = "/"
    cookie[COOKIE_NAME]["httponly"] = True
    cookie[COOKIE_NAME]["samesite"] = "Lax"
    return cookie[COOKIE_NAME].OutputString()


def clear_cookie():
    cookie = http.cookies.SimpleCookie()
    cookie[COOKIE_NAME] = ""
    cookie[COOKIE_NAME]["path"] = "/"
    cookie[COOKIE_NAME]["max-age"] = 0
    cookie[COOKIE_NAME]["expires"] = "Thu, 01 Jan 1970 00:00:00 GMT"
    return cookie[COOKIE_NAME].OutputString()
