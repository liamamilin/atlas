"""SQLite 连接、schema 与启动迁移。仅使用标准库 sqlite3。"""

import os
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  name_key TEXT NOT NULL,
  is_default INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  deleted_at TEXT NULL
);

CREATE TABLE IF NOT EXISTS bookmarks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  url_key TEXT NOT NULL,
  title TEXT NOT NULL,
  title_source TEXT NOT NULL,
  note TEXT NOT NULL DEFAULT '',
  category_id INTEGER NOT NULL REFERENCES categories(id),
  search_text TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  trashed_at TEXT NULL,
  trashed_from_category_id INTEGER NULL REFERENCES categories(id)
);

CREATE UNIQUE INDEX IF NOT EXISTS ux_categories_active_name
  ON categories(name_key) WHERE deleted_at IS NULL;
CREATE INDEX IF NOT EXISTS ix_bookmarks_active_created
  ON bookmarks(trashed_at, created_at, id);
CREATE INDEX IF NOT EXISTS ix_bookmarks_category
  ON bookmarks(category_id, trashed_at);
CREATE INDEX IF NOT EXISTS ix_bookmarks_url_key
  ON bookmarks(url_key, trashed_at);
"""

SCHEMA_VERSION = 1


def open_database(data_dir):
    """打开（必要时创建）数据目录中的 SQLite 库，返回连接。"""
    os.makedirs(data_dir, exist_ok=True)
    path = os.path.join(data_dir, "bookmarks.sqlite3")
    conn = sqlite3.connect(path, check_same_thread=False, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute("PRAGMA synchronous=NORMAL")
    migrate(conn)
    return conn


def migrate(conn):
    conn.executescript(SCHEMA)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
    )
    row = conn.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()
    if row is None:
        conn.execute(
            "INSERT INTO meta(key, value) VALUES('schema_version', ?)",
            (str(SCHEMA_VERSION),),
        )
    return SCHEMA_VERSION
