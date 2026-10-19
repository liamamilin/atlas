"""SQLite 持久化层：归类与收藏记录的读写。

所有数据都存放在启动参数 --data-dir 指定的目录内，进程重启后依然保留。
"""

import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit

DEFAULT_CATEGORY_NAME = "未整理"
SEED_CATEGORY_NAMES = ["待购", "家居改造", "以后看看"]
DB_FILENAME = "bookmarks.db"
MAX_TEXT = 2000
MAX_URL = 2000
MAX_NAME = 60


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT NOT NULL UNIQUE,
    is_default INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmarks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    url         TEXT NOT NULL,
    title       TEXT NOT NULL DEFAULT '',
    note        TEXT NOT NULL DEFAULT '',
    category_id INTEGER NOT NULL REFERENCES categories(id),
    created_at  TEXT NOT NULL,
    updated_at  TEXT NOT NULL,
    open_count  INTEGER NOT NULL DEFAULT 0,
    last_opened TEXT
);

CREATE INDEX IF NOT EXISTS idx_bookmarks_category ON bookmarks(category_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_created ON bookmarks(created_at DESC);
"""


class StorageError(Exception):
    """面向用户的存储层错误，消息可直接显示在界面上。"""


def normalize_url(raw):
    """把用户输入整理成可跳转的 http/https 地址。"""
    if raw is None:
        raise StorageError("请填写要保存的链接")
    text = str(raw).strip()
    if not text:
        raise StorageError("请填写要保存的链接")
    if len(text) > MAX_URL:
        raise StorageError("链接过长")
    if any(ch.isspace() for ch in text):
        raise StorageError("链接中不能包含空格或换行")
    if "://" not in text:
        text = "https://" + text
    parts = urlsplit(text)
    if parts.scheme not in ("http", "https"):
        raise StorageError("只支持 http 或 https 链接")
    if not parts.netloc or "." not in parts.netloc:
        raise StorageError("链接看起来不完整，请检查后重试")
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, parts.fragment))


def clean_text(value, limit=MAX_TEXT):
    if value is None:
        return ""
    text = str(value).replace("\x00", "").strip()
    if len(text) > limit:
        text = text[:limit]
    return text


def default_title_from_url(url):
    parts = urlsplit(url)
    tail = parts.path.rstrip("/").rsplit("/", 1)[-1]
    if tail:
        return tail[:MAX_NAME]
    return parts.netloc


class Storage:
    def __init__(self, data_dir):
        if not data_dir:
            raise StorageError("必须指定数据目录")
        self.data_dir = os.path.abspath(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        self.db_path = os.path.join(self.data_dir, DB_FILENAME)
        self._initialize()

    @contextmanager
    def _connect(self):
        conn = sqlite3.connect(self.db_path, timeout=15)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _initialize(self):
        with self._connect() as conn:
            conn.executescript(SCHEMA)
            row = conn.execute(
                "SELECT id FROM categories WHERE is_default = 1 ORDER BY id LIMIT 1"
            ).fetchone()
            count = conn.execute("SELECT COUNT(*) AS c FROM categories").fetchone()["c"]
            if row is None and count == 0:
                stamp = now_iso()
                names = [DEFAULT_CATEGORY_NAME] + SEED_CATEGORY_NAMES
                for index, name in enumerate(names):
                    conn.execute(
                        "INSERT OR IGNORE INTO categories (name, is_default, created_at) VALUES (?, ?, ?)",
                        (name, 1 if index == 0 else 0, stamp),
                    )
            elif row is None:
                stamp = now_iso()
                conn.execute(
                    "INSERT OR IGNORE INTO categories (name, is_default, created_at) VALUES (?, 1, ?)",
                    (DEFAULT_CATEGORY_NAME, stamp),
                )

    # ------------------------------------------------------------------ 归类

    def default_category_id(self, conn=None):
        def query(c):
            row = c.execute(
                "SELECT id FROM categories WHERE is_default = 1 ORDER BY id LIMIT 1"
            ).fetchone()
            if row is None:
                row = c.execute("SELECT id FROM categories ORDER BY id LIMIT 1").fetchone()
            return row["id"] if row else None

        if conn is not None:
            return query(conn)
        with self._connect() as c:
            return query(c)

    def list_categories(self):
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT c.id, c.name, c.is_default, c.created_at,
                       COUNT(b.id) AS count
                FROM categories c
                LEFT JOIN bookmarks b ON b.category_id = c.id
                GROUP BY c.id
                ORDER BY c.is_default DESC, c.id ASC
                """
            ).fetchall()
            return [dict(r) for r in rows]

    def create_category(self, name):
        clean = clean_text(name, MAX_NAME)
        if not clean:
            raise StorageError("请填写归类名称")
        with self._connect() as conn:
            exists = conn.execute(
                "SELECT id FROM categories WHERE name = ?", (clean,)
            ).fetchone()
            if exists:
                raise StorageError("已存在同名归类")
            cur = conn.execute(
                "INSERT INTO categories (name, is_default, created_at) VALUES (?, 0, ?)",
                (clean, now_iso()),
            )
            return {"id": cur.lastrowid, "name": clean, "is_default": 0, "count": 0}

    def rename_category(self, category_id, name):
        clean = clean_text(name, MAX_NAME)
        if not clean:
            raise StorageError("请填写归类名称")
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, is_default FROM categories WHERE id = ?", (category_id,)
            ).fetchone()
            if row is None:
                raise StorageError("归类不存在")
            if row["is_default"]:
                raise StorageError("默认归类不能改名")
            if conn.execute(
                "SELECT id FROM categories WHERE name = ? AND id != ?", (clean, category_id)
            ).fetchone():
                raise StorageError("已存在同名归类")
            conn.execute("UPDATE categories SET name = ? WHERE id = ?", (clean, category_id))
            return {"id": category_id, "name": clean}

    def delete_category(self, category_id):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, is_default FROM categories WHERE id = ?", (category_id,)
            ).fetchone()
            if row is None:
                raise StorageError("归类不存在")
            if row["is_default"]:
                raise StorageError("默认归类不能删除")
            target = self.default_category_id(conn)
            moved = conn.execute(
                "UPDATE bookmarks SET category_id = ?, updated_at = ? WHERE category_id = ?",
                (target, now_iso(), category_id),
            ).rowcount
            conn.execute("DELETE FROM categories WHERE id = ?", (category_id,))
            return {"moved": moved, "target_category_id": target}

    # ------------------------------------------------------------------ 记录

    def list_bookmarks(self, category_id=None, query=None):
        sql = [
            "SELECT b.id, b.url, b.title, b.note, b.category_id, b.created_at,",
            "b.updated_at, b.open_count, b.last_opened, c.name AS category_name",
            "FROM bookmarks b JOIN categories c ON c.id = b.category_id",
        ]
        where = []
        params = []
        if category_id is not None:
            where.append("b.category_id = ?")
            params.append(category_id)
        if query:
            needle = "%" + str(query).strip() + "%"
            where.append(
                "(b.url LIKE ? OR b.title LIKE ? OR b.note LIKE ? OR c.name LIKE ?)"
            )
            params.extend([needle, needle, needle, needle])
        if where:
            sql.append("WHERE " + " AND ".join(where))
        sql.append("ORDER BY b.created_at DESC, b.id DESC")
        with self._connect() as conn:
            rows = conn.execute(" ".join(sql), params).fetchall()
            return [dict(r) for r in rows]

    def get_bookmark(self, bookmark_id):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT * FROM bookmarks WHERE id = ?", (bookmark_id,)
            ).fetchone()
            return dict(row) if row else None

    def create_bookmark(self, url, title, note, category_id):
        normalized = normalize_url(url)
        with self._connect() as conn:
            if category_id is None:
                category_id = self.default_category_id(conn)
            else:
                found = conn.execute(
                    "SELECT id FROM categories WHERE id = ?", (category_id,)
                ).fetchone()
                if found is None:
                    category_id = self.default_category_id(conn)
            clean_title = clean_text(title, MAX_NAME) or default_title_from_url(normalized)
            clean_note = clean_text(note)
            stamp = now_iso()
            cur = conn.execute(
                """
                INSERT INTO bookmarks (url, title, note, category_id, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (normalized, clean_title, clean_note, category_id, stamp, stamp),
            )
            row = conn.execute(
                """
                SELECT b.*, c.name AS category_name FROM bookmarks b
                JOIN categories c ON c.id = b.category_id WHERE b.id = ?
                """,
                (cur.lastrowid,),
            ).fetchone()
            return dict(row)

    def update_bookmark(self, bookmark_id, fields):
        with self._connect() as conn:
            current = conn.execute(
                "SELECT * FROM bookmarks WHERE id = ?", (bookmark_id,)
            ).fetchone()
            if current is None:
                raise StorageError("记录不存在")
            url = current["url"]
            if "url" in fields:
                url = normalize_url(fields["url"])
            title = current["title"]
            if "title" in fields:
                title = clean_text(fields["title"], MAX_NAME) or default_title_from_url(url)
            note = current["note"]
            if "note" in fields:
                note = clean_text(fields["note"])
            category_id = current["category_id"]
            if "category_id" in fields and fields["category_id"] is not None:
                found = conn.execute(
                    "SELECT id FROM categories WHERE id = ?", (fields["category_id"],)
                ).fetchone()
                if found is None:
                    raise StorageError("目标归类不存在")
                category_id = fields["category_id"]
            conn.execute(
                """
                UPDATE bookmarks SET url = ?, title = ?, note = ?, category_id = ?, updated_at = ?
                WHERE id = ?
                """,
                (url, title, note, category_id, now_iso(), bookmark_id),
            )
            row = conn.execute(
                """
                SELECT b.*, c.name AS category_name FROM bookmarks b
                JOIN categories c ON c.id = b.category_id WHERE b.id = ?
                """,
                (bookmark_id,),
            ).fetchone()
            return dict(row)

    def delete_bookmark(self, bookmark_id):
        with self._connect() as conn:
            cur = conn.execute("DELETE FROM bookmarks WHERE id = ?", (bookmark_id,))
            if cur.rowcount == 0:
                raise StorageError("记录不存在")
            return {"deleted": bookmark_id}

    def record_open(self, bookmark_id):
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, url FROM bookmarks WHERE id = ?", (bookmark_id,)
            ).fetchone()
            if row is None:
                raise StorageError("记录不存在")
            conn.execute(
                """
                UPDATE bookmarks SET open_count = open_count + 1, last_opened = ?
                WHERE id = ?
                """,
                (now_iso(), bookmark_id),
            )
            return row["url"]

    def stats(self):
        with self._connect() as conn:
            total = conn.execute("SELECT COUNT(*) AS c FROM bookmarks").fetchone()["c"]
            opened = conn.execute(
                "SELECT COUNT(*) AS c FROM bookmarks WHERE open_count > 0"
            ).fetchone()["c"]
            return {"total": total, "opened": opened}
