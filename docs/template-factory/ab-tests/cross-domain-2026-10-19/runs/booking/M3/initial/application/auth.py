"""账号、口令哈希与会话管理。

口令只以 PBKDF2-HMAC-SHA256 哈希保存；会话令牌由服务端生成并保存在数据库，
客户端只持有不透明 cookie，角色/身份从不信任请求体。
"""
import hashlib
import hmac
import os
import secrets

import db
import times

_ITERATIONS = 120_000
_DKLEN = 32


def _derive(password, salt_bytes):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt_bytes, _ITERATIONS, dklen=_DKLEN
    ).hex()


def create_user(username, password, role, conn=None):
    """创建用户；username 唯一冲突由调用方按需处理。"""
    salt = os.urandom(16)
    password_hash = _derive(password, salt)
    own = conn is None
    if own:
        conn = db.connect()
    try:
        cur = conn.execute(
            "INSERT INTO users(username, password_hash, salt, role, created_at)"
            " VALUES(?,?,?,?,?)",
            (username, password_hash, salt.hex(), role, times.now_iso()),
        )
        return cur.lastrowid
    finally:
        if own:
            conn.close()


def verify_password(password, salt_hex, expected_hash):
    try:
        salt = bytes.fromhex(salt_hex)
    except (ValueError, TypeError):
        return False
    candidate = _derive(password, salt)
    return hmac.compare_digest(candidate, expected_hash)


def create_session(user_id):
    token = secrets.token_urlsafe(32)
    conn = db.connect()
    try:
        conn.execute(
            "INSERT INTO sessions(token, user_id, created_at) VALUES(?,?,?)",
            (token, user_id, times.now_iso()),
        )
    finally:
        conn.close()
    return token


def delete_session(token):
    if not token:
        return
    conn = db.connect()
    try:
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))
    finally:
        conn.close()


def get_user_by_token(token):
    if not token:
        return None
    conn = db.connect()
    try:
        row = conn.execute(
            "SELECT u.id AS id, u.username AS username, u.role AS role"
            " FROM sessions s JOIN users u ON u.id = s.user_id"
            " WHERE s.token = ?",
            (token,),
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        return None
    return {"id": row["id"], "username": row["username"], "role": row["role"]}


DEMO_USERS = (
    ("admin", "AtlasDemo-Admin-9!", "admin"),
    ("alice", "AtlasDemo-Alice-9!", "resident"),
    ("bob", "AtlasDemo-Bob-9!", "resident"),
)


def ensure_demo_users():
    """幂等地补建演示账号；已存在的账号与记录绝不重置或覆盖。"""
    conn = db.connect()
    try:
        conn.execute("BEGIN IMMEDIATE")
        for username, password, role in DEMO_USERS:
            exists = conn.execute(
                "SELECT id FROM users WHERE username = ?", (username,)
            ).fetchone()
            if exists is None:
                create_user(username, password, role, conn=conn)
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()
