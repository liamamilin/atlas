"""SQLite 持久化层：连接管理与表结构。

所有持久数据都放在 data-dir 下的 app.db 中，重启不丢、不被重置。
"""
import os
import sqlite3

_db_path = None

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    salt          TEXT NOT NULL,
    role          TEXT NOT NULL,
    created_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions (
    token      TEXT PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users(id),
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS resources (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bookings (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_id  INTEGER NOT NULL REFERENCES resources(id),
    owner_id     INTEGER NOT NULL REFERENCES users(id),
    start_ts     REAL NOT NULL,
    end_ts       REAL NOT NULL,
    note         TEXT NOT NULL DEFAULT '',
    status       TEXT NOT NULL DEFAULT 'active',
    created_at   TEXT NOT NULL,
    cancelled_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_bookings_resource
    ON bookings(resource_id, status);
CREATE INDEX IF NOT EXISTS idx_bookings_owner
    ON bookings(owner_id);
CREATE INDEX IF NOT EXISTS idx_sessions_user
    ON sessions(user_id);
"""


def configure(data_dir):
    """设定数据目录并返回数据库文件路径。"""
    global _db_path
    data_dir = os.path.abspath(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    _db_path = os.path.join(data_dir, "app.db")
    return _db_path


def path():
    if _db_path is None:
        raise RuntimeError("db.configure() 必须先调用")
    return _db_path


def connect():
    """每次请求使用独立连接，可被不同线程安全使用。"""
    conn = sqlite3.connect(path(), timeout=15, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 15000")
    return conn


def init_schema():
    conn = connect()
    try:
        conn.executescript(SCHEMA)
    finally:
        conn.close()
