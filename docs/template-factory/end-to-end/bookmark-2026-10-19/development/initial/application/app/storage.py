"""SQLite storage layer for the P0 bookmark manager.

``Storage`` owns the whole on-disk library and all data access. It never
imports the HTTP layer, so the frozen routes in ``app/server.py`` can be
replaced without touching persistence. A single SQLite file lives at
``<data_dir>/library.sqlite3``::

    storage = Storage("/state/data")   # managed container delivery
    storage = Storage("./state")       # local run

Construction creates the data directory when absent, opens the database,
applies the frozen P0 schema and seeds the undeletable default inbox
(``未整理``, ``is_default = 1``) on first start. Every write runs inside a
transaction and is committed, so data survives a process restart. The schema
is exactly the two frozen P0 tables; no extra table is introduced.

Frozen P0 schema::

    collections(id INTEGER PK, name TEXT NOT NULL UNIQUE,
                is_default INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)
    bookmarks(id INTEGER PK, url TEXT NOT NULL, title TEXT NOT NULL DEFAULT '',
              note TEXT NOT NULL DEFAULT '', collection_id INTEGER NOT NULL
              REFERENCES collections(id), created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL)

All access methods return plain ``dict`` rows (never ``sqlite3.Row``) so
``app/views.py`` can render them without knowing about the database. The
expected caller is ``app/server.py``: it validates the URL before calling
``create_bookmark``, resolves the ``inbox`` alias with
``get_default_collection``, and turns the documented ``ValueError`` and
``None`` outcomes below into the frozen 400/404 responses.

Timestamps are stored as UTC ISO-8601 text.
"""

import datetime
import os
import sqlite3

__all__ = ["Storage", "SCHEMA_VERSION"]

#: Schema revision recorded in ``PRAGMA user_version``.
SCHEMA_VERSION = 1

#: Name of the SQLite file created directly beneath the data directory.
DB_FILENAME = "library.sqlite3"

#: Name of the built-in inbox created on first start; it cannot be deleted.
DEFAULT_COLLECTION_NAME = "未整理"

#: SQLite uses a backslash as the LIKE escape character; the literal is kept
#: out of the source so the ESCAPE clauses below stay unambiguous.
_LIKE_ESCAPE = chr(92)

_COLLECTIONS_SQL = """
CREATE TABLE IF NOT EXISTS collections (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    is_default INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
)
"""

_BOOKMARKS_SQL = """
CREATE TABLE IF NOT EXISTS bookmarks (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    note TEXT NOT NULL DEFAULT '',
    collection_id INTEGER NOT NULL REFERENCES collections(id),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
)
"""

_COLLECTION_COLUMNS = "id, name, is_default, created_at"

_BOOKMARK_COLUMNS = "id, url, title, note, collection_id, created_at, updated_at"

_SEARCH_CLAUSE = (
    "(title LIKE ? ESCAPE '"
    + _LIKE_ESCAPE
    + "' OR url LIKE ? ESCAPE '"
    + _LIKE_ESCAPE
    + "' OR note LIKE ? ESCAPE '"
    + _LIKE_ESCAPE
    + "')"
)


def _utcnow():
    """Return the current instant as UTC ISO-8601 text."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _as_int(value):
    """Return ``value`` as an ``int`` id, or ``None`` when it is not one."""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def _like_pattern(text):
    """Wrap ``text`` in ``%`` wildcards, escaping LIKE metacharacters.

    A backslash, ``%`` or ``_`` typed by the user is escaped so it matches
    literally instead of acting as a wildcard.
    """
    escaped = str(text)
    escaped = escaped.replace(_LIKE_ESCAPE, _LIKE_ESCAPE + _LIKE_ESCAPE)
    escaped = escaped.replace("%", _LIKE_ESCAPE + "%")
    escaped = escaped.replace("_", _LIKE_ESCAPE + "_")
    return "%" + escaped + "%"


class Storage:
    """Own the SQLite library file and expose the P0 data access methods."""

    def __init__(self, data_dir):
        """Open (creating if needed) ``<data_dir>/library.sqlite3``.

        ``data_dir`` is used exactly as given -- the managed container passes
        the literal ``/state/data`` while a local run passes ``./state`` -- and
        is created when it does not already exist.
        """
        if data_dir is None or not str(data_dir).strip():
            raise ValueError("data_dir is required")
        self.data_dir = str(data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        self.db_path = os.path.join(self.data_dir, DB_FILENAME)
        # The server is threaded (ThreadingHTTPServer) and shares this one
        # connection across request threads, so cross-thread use is allowed.
        # A single-process local library needs no further concurrency control.
        self._connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute("PRAGMA foreign_keys = ON")
        self._create_schema()
        self._seed_default_collection()

    # -- schema and seeding ----------------------------------------------

    def _create_schema(self):
        """Create the two frozen P0 tables and record the schema revision."""
        with self._connection:
            self._connection.execute(_COLLECTIONS_SQL)
            self._connection.execute(_BOOKMARKS_SQL)
            self._connection.execute(
                "PRAGMA user_version = %d" % SCHEMA_VERSION
            )

    def _seed_default_collection(self):
        """Ensure the undeletable default inbox exists and return it."""
        default = self.get_default_collection()
        if default is not None:
            return default
        existing = self.find_collection_by_name(DEFAULT_COLLECTION_NAME)
        with self._connection:
            if existing is not None:
                # Promote a same-named collection rather than break UNIQUE.
                self._connection.execute(
                    "UPDATE collections SET is_default = 1 WHERE id = ?",
                    (existing["id"],),
                )
                collection_id = existing["id"]
            else:
                cursor = self._connection.execute(
                    "INSERT INTO collections (name, is_default, created_at) "
                    "VALUES (?, 1, ?)",
                    (DEFAULT_COLLECTION_NAME, _utcnow()),
                )
                collection_id = cursor.lastrowid
        return self.get_collection(collection_id)

    # -- collections ------------------------------------------------------

    def list_collections(self):
        """Return every collection as a dict, the default inbox first."""
        cursor = self._connection.execute(
            "SELECT "
            + _COLLECTION_COLUMNS
            + " FROM collections ORDER BY is_default DESC, name ASC, id ASC"
        )
        return [dict(row) for row in cursor.fetchall()]

    def get_collection(self, collection_id):
        """Return the collection dict with ``collection_id``, or ``None``."""
        key = _as_int(collection_id)
        if key is None:
            return None
        cursor = self._connection.execute(
            "SELECT " + _COLLECTION_COLUMNS + " FROM collections WHERE id = ?",
            (key,),
        )
        row = cursor.fetchone()
        return dict(row) if row is not None else None

    def get_default_collection(self):
        """Return the default inbox (``is_default = 1``), or ``None``."""
        cursor = self._connection.execute(
            "SELECT "
            + _COLLECTION_COLUMNS
            + " FROM collections WHERE is_default = 1 ORDER BY id ASC LIMIT 1"
        )
        row = cursor.fetchone()
        return dict(row) if row is not None else None

    def find_collection_by_name(self, name):
        """Return the collection named ``name`` (trimmed), or ``None``."""
        if name is None:
            return None
        cleaned = str(name).strip()
        if not cleaned:
            return None
        cursor = self._connection.execute(
            "SELECT "
            + _COLLECTION_COLUMNS
            + " FROM collections WHERE name = ? LIMIT 1",
            (cleaned,),
        )
        row = cursor.fetchone()
        return dict(row) if row is not None else None

    def create_collection(self, name):
        """Create a non-default collection and return its dict row.

        Raises ``ValueError`` for an empty or already-used name so the caller
        can render the frozen 400 error page.
        """
        if name is None:
            raise ValueError("collection name is required")
        cleaned = str(name).strip()
        if not cleaned:
            raise ValueError("collection name is required")
        if self.find_collection_by_name(cleaned) is not None:
            raise ValueError("collection %r already exists" % cleaned)
        try:
            with self._connection:
                cursor = self._connection.execute(
                    "INSERT INTO collections (name, is_default, created_at) "
                    "VALUES (?, 0, ?)",
                    (cleaned, _utcnow()),
                )
        except sqlite3.IntegrityError as error:
            # Lost a race against a concurrent insert; preserve the unique-name
            # contract the server relies on for its 400 response.
            raise ValueError("collection %r already exists" % cleaned) from error
        return self.get_collection(cursor.lastrowid)

    # -- bookmarks --------------------------------------------------------

    def list_bookmarks(self, collection_id=None, query=None):
        """Return bookmark dict rows, newest first.

        ``collection_id`` scopes the result to a single collection (``None``
        or empty lists the whole library; the ``inbox``/``default`` alias
        resolves to the default inbox). ``query``, when non-empty, is matched
        case-insensitively with ``LIKE`` over ``title``, ``url`` and ``note``.
        An unknown collection id yields an empty list.
        """
        clauses = []
        parameters = []
        if collection_id is not None and str(collection_id).strip() != "":
            resolved = self._resolve_collection_id(collection_id)
            if resolved is None:
                return []
            clauses.append("collection_id = ?")
            parameters.append(resolved)
        text = "" if query is None else str(query).strip()
        if text:
            pattern = _like_pattern(text)
            clauses.append(_SEARCH_CLAUSE)
            parameters.extend([pattern, pattern, pattern])
        sql = "SELECT " + _BOOKMARK_COLUMNS + " FROM bookmarks"
        if clauses:
            sql = sql + " WHERE " + " AND ".join(clauses)
        sql = sql + " ORDER BY created_at DESC, id DESC"
        cursor = self._connection.execute(sql, parameters)
        return [dict(row) for row in cursor.fetchall()]

    def create_bookmark(self, url, title="", note="", collection_id=None):
        """Insert a bookmark and return its dict row.

        ``url`` is required (the caller validates that it is an absolute
        ``http(s)`` URL first). When ``collection_id`` is missing the record
        goes to the default inbox; an unknown supplied collection raises
        ``ValueError``.
        """
        if url is None or not str(url).strip():
            raise ValueError("url is required")
        cleaned_url = str(url).strip()
        cleaned_title = "" if title is None else str(title).strip()
        cleaned_note = "" if note is None else str(note)
        if collection_id is None or str(collection_id).strip() == "":
            default = self.get_default_collection()
            if default is None:
                raise ValueError("default collection is unavailable")
            target_id = default["id"]
        else:
            target_id = self._resolve_collection_id(collection_id)
            if target_id is None or self.get_collection(target_id) is None:
                raise ValueError("unknown collection id: %r" % (collection_id,))
        now = _utcnow()
        with self._connection:
            cursor = self._connection.execute(
                "INSERT INTO bookmarks "
                "(url, title, note, collection_id, created_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (cleaned_url, cleaned_title, cleaned_note, target_id, now, now),
            )
        return self.get_bookmark(cursor.lastrowid)

    def get_bookmark(self, bookmark_id):
        """Return the bookmark dict with ``bookmark_id``, or ``None``."""
        key = _as_int(bookmark_id)
        if key is None:
            return None
        cursor = self._connection.execute(
            "SELECT " + _BOOKMARK_COLUMNS + " FROM bookmarks WHERE id = ?",
            (key,),
        )
        row = cursor.fetchone()
        return dict(row) if row is not None else None

    def move_bookmark(self, bookmark_id, collection_id):
        """Move a bookmark to another collection and return its dict row.

        Returns ``None`` when the bookmark or the target collection does not
        exist, so the caller can render the frozen 404 page.
        """
        bookmark = self.get_bookmark(bookmark_id)
        if bookmark is None:
            return None
        target_id = self._resolve_collection_id(collection_id)
        if target_id is None or self.get_collection(target_id) is None:
            return None
        with self._connection:
            self._connection.execute(
                "UPDATE bookmarks SET collection_id = ?, updated_at = ? "
                "WHERE id = ?",
                (target_id, _utcnow(), bookmark["id"]),
            )
        return self.get_bookmark(bookmark["id"])

    # -- helpers ----------------------------------------------------------

    def _resolve_collection_id(self, collection_id):
        """Map a collection id or the ``inbox``/``default`` alias to an id."""
        if collection_id is None:
            return None
        if isinstance(collection_id, str):
            token = collection_id.strip()
            if token.lower() in ("inbox", "default"):
                default = self.get_default_collection()
                return default["id"] if default is not None else None
        return _as_int(collection_id)

    def close(self):
        """Close the underlying SQLite connection."""
        self._connection.close()
