"""SQLite 连接、建表与工具函数。

所有持久数据只落在 --data-dir 指定的目录内（一个 SQLite 文件）。
进程为单进程多线程：读操作各自连接；写操作由 store.py 用
BEGIN IMMEDIATE 串行化，保证同一设施重叠时段最多一笔成功。
"""
import os
import sqlite3

DB_FILENAME = "trial-booking.sqlite3"

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL CHECK (role IN ('admin', 'resident'))
);

CREATE TABLE IF NOT EXISTS sessions (
    token      TEXT PRIMARY KEY,
    user_id    INTEGER NOT NULL REFERENCES users(id),
    expires_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS resources (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT NOT NULL,
    active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS bookings (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    resource_id  INTEGER NOT NULL REFERENCES resources(id),
    owner_id     INTEGER NOT NULL REFERENCES users(id),
    start_epoch  INTEGER NOT NULL,
    end_epoch    INTEGER NOT NULL,
    start_iso    TEXT NOT NULL,
    end_iso      TEXT NOT NULL,
    note         TEXT NOT NULL DEFAULT '',
    status       TEXT NOT NULL DEFAULT 'active'
                 CHECK (status IN ('active', 'cancelled')),
    created_at   INTEGER NOT NULL,
    cancelled_at INTEGER
);

/* 同起点守卫：同一设施同一开始时刻只允许一笔 active 预约。
   使用部分索引，使取消后同一时段可以重新预约。 */
CREATE UNIQUE INDEX IF NOT EXISTS ux_bookings_active_start
    ON bookings (resource_id, start_epoch) WHERE status = 'active';
CREATE INDEX IF NOT EXISTS ix_bookings_resource_status
    ON bookings (resource_id, status);
CREATE INDEX IF NOT EXISTS ix_bookings_owner_status
    ON bookings (owner_id, status);
"""


def db_path(data_dir):
    """返回数据目录内的数据库文件路径。"""
    return os.path.join(data_dir, DB_FILENAME)


def connect(path):
    """打开一个 SQLite 连接（自动提交模式，写入由调用方显式开启事务）。"""
    conn = sqlite3.connect(path, timeout=30.0, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 30000")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize(path):
    """建表建索引（幂等），并启用 WAL 以允许读写并发。"""
    conn = connect(path)
    try:
        conn.execute("PRAGMA journal_mode = WAL")
        conn.executescript(SCHEMA)
    finally:
        conn.close()
