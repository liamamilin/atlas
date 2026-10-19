"""SQLite 存储层：连接、模式与演示账号播种。

设计要点（见 DECISIONS.md）：
- 全部持久数据只落在 --data-dir 内的单个 SQLite 文件。
- 时段时间以 UTC epoch 整数存储与比较；另存规范化 ISO 文本用于渲染。
- 半开区间 [start, end)：重叠判定为 existing.start < new.end AND existing.end > new.start。
- 活跃预约的同起点由部分唯一索引守卫（仅 status='active' 生效），
  因此软取消后允许重新预约同一时段。
"""

import os
import sqlite3

SCHEMA_STATEMENTS = (
    """
    CREATE TABLE IF NOT EXISTS users (
        id            INTEGER PRIMARY KEY AUTOINCREMENT,
        username      TEXT    NOT NULL UNIQUE,
        password_hash TEXT    NOT NULL,
        role          TEXT    NOT NULL CHECK (role IN ('admin', 'resident'))
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS sessions (
        token      TEXT    PRIMARY KEY,
        user_id    INTEGER NOT NULL,
        created_at INTEGER NOT NULL,
        expires_at INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS resources (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        name       TEXT    NOT NULL,
        active     INTEGER NOT NULL DEFAULT 1,
        created_at INTEGER NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS bookings (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_id  INTEGER NOT NULL,
        owner_id     INTEGER NOT NULL,
        start_epoch  INTEGER NOT NULL,
        end_epoch    INTEGER NOT NULL,
        start_iso    TEXT    NOT NULL,
        end_iso      TEXT    NOT NULL,
        note         TEXT    NOT NULL DEFAULT '',
        status       TEXT    NOT NULL DEFAULT 'active'
                             CHECK (status IN ('active', 'cancelled')),
        created_at   INTEGER NOT NULL,
        cancelled_at INTEGER,
        FOREIGN KEY (resource_id) REFERENCES resources(id),
        FOREIGN KEY (owner_id)    REFERENCES users(id)
    )
    """,
    "CREATE INDEX IF NOT EXISTS ix_bookings_resource_status "
    "ON bookings(resource_id, status)",
    "CREATE INDEX IF NOT EXISTS ix_bookings_owner_status "
    "ON bookings(owner_id, status)",
    # 同起点守卫：仅对活跃预约生效，软取消后可重新占用同一时段。
    "CREATE UNIQUE INDEX IF NOT EXISTS ux_bookings_active_start "
    "ON bookings(resource_id, start_epoch) WHERE status = 'active'",
)


def ensure_data_dir(data_dir):
    """确保数据目录存在。返回目录内数据库文件的绝对路径。"""
    data_dir = os.path.abspath(data_dir)
    os.makedirs(data_dir, exist_ok=True)
    return os.path.join(data_dir, 'booking.sqlite3')


def connect(db_path):
    """为当前线程建立一条连接。调用方负责关闭。

    timeout + busy_timeout 让 BEGIN IMMEDIATE 写入在并发下等待锁而不是立刻报错。
    """
    conn = sqlite3.connect(db_path, timeout=30.0, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA busy_timeout = 30000')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn


def init_db(db_path):
    conn = connect(db_path)
    try:
        for statement in SCHEMA_STATEMENTS:
            conn.execute(statement)
    finally:
        conn.close()


def seed_demo_users(db_path, accounts):
    """仅在完全没有用户时创建合成演示账号；绝不重置既有账户或记录。"""
    from security import hash_password  # 局部导入避免无谓的模块耦合

    conn = connect(db_path)
    try:
        existing = conn.execute('SELECT COUNT(*) AS n FROM users').fetchone()['n']
        if existing:
            return 0
        created = 0
        for account in accounts:
            conn.execute(
                'INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)',
                (account['username'], hash_password(account['password']), account['role']),
            )
            created += 1
        return created
    finally:
        conn.close()
