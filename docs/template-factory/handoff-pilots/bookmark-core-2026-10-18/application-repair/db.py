"""SQLite 持久化层：分类、书签、保存幂等令牌。

所有数据都在 --data-dir 指定的目录下（app.sqlite3）。每次请求使用独立连接，
写操作由全局锁串行化，避免同按钮重复提交产生竞态。
"""

import os
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS bookmark (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    url_key TEXT NOT NULL,
    title TEXT,
    note TEXT,
    category_id INTEGER REFERENCES category(id),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS save_nonce (
    token TEXT PRIMARY KEY,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookmark_order ON bookmark(created_at DESC, id DESC);
CREATE INDEX IF NOT EXISTS idx_bookmark_key ON bookmark(url_key);
"""

NONCE_TTL_HOURS = 1


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def _nonce_cutoff():
    return (datetime.now(timezone.utc) - timedelta(hours=NONCE_TTL_HOURS)).isoformat()


def _matches(item, needle):
    for field in (item.get("title"), item.get("url"), item.get("note"), item.get("category_name")):
        if field and needle in str(field).casefold():
            return True
    return False


class Store:
    def __init__(self, data_dir):
        self.data_dir = os.path.abspath(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        self.db_path = os.path.join(self.data_dir, "app.sqlite3")
        self._lock = threading.RLock()
        conn = sqlite3.connect(self.db_path, timeout=20)
        try:
            conn.execute("PRAGMA journal_mode=WAL")
            conn.executescript(SCHEMA)
            conn.commit()
        finally:
            conn.close()

    @contextmanager
    def _cursor(self):
        conn = sqlite3.connect(self.db_path, timeout=20)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA busy_timeout=20000")
        try:
            with conn:
                yield conn
        finally:
            conn.close()

    # ---- 分类 ----
    def list_categories(self):
        with self._cursor() as conn:
            rows = conn.execute(
                "SELECT id, name, created_at FROM category ORDER BY created_at, id"
            ).fetchall()
        return [dict(row) for row in rows]

    def get_category(self, category_id):
        with self._cursor() as conn:
            row = conn.execute(
                "SELECT id, name FROM category WHERE id = ?", (category_id,)
            ).fetchone()
        return dict(row) if row else None

    def get_category_by_name(self, name):
        with self._cursor() as conn:
            row = conn.execute(
                "SELECT id, name FROM category WHERE name = ?", (name,)
            ).fetchone()
        return dict(row) if row else None

    def create_category(self, name):
        """新建分类；名称重复（含并发竞态）时返回 None，由调用方给出反馈。"""
        with self._cursor() as conn:
            try:
                cur = conn.execute(
                    "INSERT INTO category(name, created_at) VALUES(?, ?)", (name, utcnow())
                )
            except sqlite3.IntegrityError:
                return None
            return cur.lastrowid

    # ---- 书签 ----
    def list_bookmarks(self, category_id=None, category_filter="all", q=None):
        with self._cursor() as conn:
            rows = conn.execute(
                "SELECT b.id, b.url, b.url_key, b.title, b.note, b.category_id, "
                "c.name AS category_name, b.created_at "
                "FROM bookmark b LEFT JOIN category c ON c.id = b.category_id "
                "ORDER BY b.created_at DESC, b.id DESC"
            ).fetchall()
        items = [dict(row) for row in rows]
        if category_filter == "unsorted":
            items = [it for it in items if it["category_id"] is None]
        elif category_filter == "id" and category_id is not None:
            items = [it for it in items if it["category_id"] == category_id]
        if q:
            needle = q.casefold()
            items = [it for it in items if _matches(it, needle)]
        return items

    def count_bookmarks(self):
        with self._cursor() as conn:
            return conn.execute("SELECT COUNT(*) AS n FROM bookmark").fetchone()["n"]

    def count_in_category(self, category_id):
        with self._cursor() as conn:
            if category_id is None:
                row = conn.execute(
                    "SELECT COUNT(*) AS n FROM bookmark WHERE category_id IS NULL"
                ).fetchone()
            else:
                row = conn.execute(
                    "SELECT COUNT(*) AS n FROM bookmark WHERE category_id = ?",
                    (category_id,),
                ).fetchone()
        return row["n"]

    def find_by_key(self, key):
        with self._cursor() as conn:
            row = conn.execute(
                "SELECT id, url, title FROM bookmark WHERE url_key = ? ORDER BY id LIMIT 1",
                (key,),
            ).fetchone()
        return dict(row) if row else None

    def insert_bookmark(self, url, key, title, note, category_id):
        now = utcnow()
        with self._cursor() as conn:
            cur = conn.execute(
                "INSERT INTO bookmark(url, url_key, title, note, category_id, created_at, updated_at) "
                "VALUES(?, ?, ?, ?, ?, ?, ?)",
                (url, key, title, note, category_id, now, now),
            )
            return cur.lastrowid

    def move_bookmark(self, bookmark_id, category_id):
        with self._cursor() as conn:
            cur = conn.execute(
                "UPDATE bookmark SET category_id = ?, updated_at = ? WHERE id = ?",
                (category_id, utcnow(), bookmark_id),
            )
            return cur.rowcount

    # ---- 幂等令牌 ----
    def register_nonce(self, token):
        """首次使用返回 True；重复提交返回 False。"""
        if not token:
            return True
        with self._cursor() as conn:
            cur = conn.execute(
                "INSERT OR IGNORE INTO save_nonce(token, created_at) VALUES(?, ?)",
                (token, utcnow()),
            )
            conn.execute("DELETE FROM save_nonce WHERE created_at < ?", (_nonce_cutoff(),))
            return cur.rowcount == 1
