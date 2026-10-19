"""口令哈希与会话令牌（仅标准库）。

- 口令使用 PBKDF2-HMAC-SHA256 加随机盐存储，绝不保存明文。
- 会话令牌由 secrets 生成，服务端在 sessions 表持有；角色与 owner 只取自会话，
  请求体中的 user_id/role 一律忽略。
"""

import hashlib
import hmac
import os
import secrets

PBKDF2_ROUNDS = 120_000
SESSION_TTL_SECONDS = 30 * 24 * 60 * 60  # 30 天
SESSION_COOKIE = 'session'


def hash_password(password, rounds=PBKDF2_ROUNDS):
    salt = os.urandom(16)
    derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, rounds)
    return 'pbkdf2_sha256$%d$%s$%s' % (rounds, salt.hex(), derived.hex())


def verify_password(password, stored):
    if not isinstance(stored, str):
        return False
    parts = stored.split('$')
    if len(parts) != 4 or parts[0] != 'pbkdf2_sha256':
        return False
    try:
        rounds = int(parts[1])
        salt = bytes.fromhex(parts[2])
        expected = bytes.fromhex(parts[3])
    except ValueError:
        return False
    derived = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, rounds)
    return hmac.compare_digest(derived, expected)


def new_session_token():
    return secrets.token_urlsafe(32)
