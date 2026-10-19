"""领域逻辑与数据访问：书签、归类、回收站、检索。"""

import datetime
import threading

import urlutil
from urlutil import UrlError, js_trim, nfkc_lower

SEARCH_SEPARATOR = "\u0001"
MAX_TITLE = 500
MAX_NOTE = 10000
MAX_NAME = 80
DEFAULT_CATEGORY_NAME = "未分类"
SORTS = ("created_desc", "created_asc")


class AppError(Exception):
    def __init__(self, code, status=400, message=None, details=None, reason=None):
        self.code = code
        self.status = status
        self.details = dict(details) if details else {}
        if reason is not None:
            self.details["reason"] = reason
        if message is None:
            message = _DEFAULT_MESSAGES.get(code, "请求无法完成")
        self.message = message
        super().__init__(message)


_DEFAULT_MESSAGES = {
    "invalid_json": "请求体不是合法 JSON",
    "invalid_field": "字段类型或取值不合法",
    "empty_patch": "没有可更新的字段",
    "invalid_url": "URL 不合法",
    "unsupported_protocol": "只支持 http 与 https 地址",
    "invalid_title": "标题不合法",
    "invalid_note": "备注不合法",
    "invalid_name": "归类名称不合法",
    "invalid_category": "归类不存在或不可用",
    "invalid_limit": "limit 必须是 1–100 的整数",
    "invalid_offset": "offset 必须是非负整数",
    "invalid_sort": "排序参数不合法",
    "invalid_mode": "删除模式不合法",
    "invalid_confirm": "确认参数不合法",
    "invalid_query": "查询词不合法",
    "category_delete_mode_required": "必须显式指定删除模式",
    "invalid_host": "Host 不合法",
    "forbidden_origin": "请求来源不被允许",
    "not_found": "资源不存在",
    "duplicate_url": "该地址已存在",
    "category_name_conflict": "归类名称已存在",
    "confirmation_required": "需要显式确认",
    "default_category_protected": "默认归类不可改名或删除",
    "not_trashed": "记录不在回收站",
    "payload_too_large": "请求体过大",
    "internal": "服务器内部错误",
}


def now_iso():
    """毫秒精度的 UTC ISO-8601 时间戳（可被 JavaScript Date.parse 解析）。"""
    moment = datetime.datetime.now(datetime.timezone.utc)
    return moment.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def _code_points(value):
    return len(value)


class Store(object):
    def __init__(self, conn):
        self.conn = conn
        self.lock = threading.RLock()
        self._ensure_default_category()

    # ------------------------------------------------------------------ 基础
    def _exec(self, sql, params=()):
        return self.conn.execute(sql, params)

    def _begin(self):
        self._exec("BEGIN IMMEDIATE")

    def _commit(self):
        self._exec("COMMIT")

    def _rollback(self):
        try:
            self._exec("ROLLBACK")
        except Exception:
            pass

    def _ensure_default_category(self):
        with self.lock:
            row = self._exec(
                "SELECT id FROM categories WHERE is_default=1 AND deleted_at IS NULL"
            ).fetchone()
            if row is not None:
                return row["id"]
            key = nfkc_lower(DEFAULT_CATEGORY_NAME)
            stamp = now_iso()
            self._begin()
            try:
                existing = self._exec(
                    "SELECT id FROM categories WHERE name_key=? AND deleted_at IS NULL",
                    (key,),
                ).fetchone()
                if existing is not None:
                    self._exec(
                        "UPDATE categories SET is_default=1, updated_at=? WHERE id=?",
                        (stamp, existing["id"]),
                    )
                    new_id = existing["id"]
                else:
                    cur = self._exec(
                        "INSERT INTO categories(name,name_key,is_default,created_at,updated_at)"
                        " VALUES(?,?,1,?,?)",
                        (DEFAULT_CATEGORY_NAME, key, stamp, stamp),
                    )
                    new_id = cur.lastrowid
                self._commit()
                return new_id
            except Exception:
                self._rollback()
                raise

    def default_category_id(self):
        row = self._exec(
            "SELECT id FROM categories WHERE is_default=1 AND deleted_at IS NULL LIMIT 1"
        ).fetchone()
        if row is None:
            return str(self._ensure_default_category())
        return str(row["id"])

    def _category_row(self, category_id):
        return self._exec("SELECT * FROM categories WHERE id=?", (category_id,)).fetchone()

    def _category_name(self, category_id):
        row = self._category_row(category_id)
        return row["name"] if row is not None else ""

    # -------------------------------------------------------------- 序列化
    def _bookmark_dict(self, row):
        return {
            "id": str(row["id"]),
            "url": row["url"],
            "title": row["title"],
            "titleSource": row["title_source"],
            "note": row["note"],
            "categoryId": str(row["category_id"]),
            "categoryName": self._category_name(row["category_id"]),
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
            "trashedAt": row["trashed_at"],
            "openPath": "/b/" + str(row["id"]),
        }

    def _trash_dict(self, row):
        category = self._category_row(row["category_id"])
        from_row = None
        from_name = None
        if row["trashed_from_category_id"] is not None:
            from_row = self._category_row(row["trashed_from_category_id"])
            from_id = str(row["trashed_from_category_id"])
            from_name = from_row["name"] if from_row is not None else ""
        else:
            from_id = None
        return {
            "id": str(row["id"]),
            "url": row["url"],
            "title": row["title"],
            "titleSource": row["title_source"],
            "note": row["note"],
            "categoryId": str(row["category_id"]),
            "categoryName": category["name"] if category is not None else "",
            "categoryDeleted": bool(category is not None and category["deleted_at"] is not None),
            "trashedFromCategoryId": from_id,
            "trashedFromCategoryName": from_name,
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
            "trashedAt": row["trashed_at"],
        }

    def category_dict(self, row):
        count = self._exec(
            "SELECT COUNT(*) AS c FROM bookmarks WHERE category_id=? AND trashed_at IS NULL",
            (row["id"],),
        ).fetchone()["c"]
        return {
            "id": str(row["id"]),
            "name": row["name"],
            "isDefault": bool(row["is_default"]),
            "bookmarkCount": int(count),
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
        }

    # ---------------------------------------------------------------- 检索
    @staticmethod
    def _search_text(title, url, note):
        return (SEARCH_SEPARATOR.join(
            (nfkc_lower(title), nfkc_lower(url), nfkc_lower(note))
        ))

    @staticmethod
    def _query_terms(q):
        if q is None:
            return []
        if not isinstance(q, str):
            raise AppError("invalid_query", 400)
        if SEARCH_SEPARATOR in q:
            raise AppError("invalid_query", 400)
        normalized = nfkc_lower(q)
        return [term for term in normalized.split() if term != ""]

    # ---------------------------------------------------------------- 归类
    def list_categories(self):
        rows = self._exec(
            "SELECT * FROM categories WHERE deleted_at IS NULL"
            " ORDER BY is_default DESC, name_key ASC, id ASC"
        ).fetchall()
        return [self.category_dict(row) for row in rows]

    def get_category(self, category_id):
        row = self._exec(
            "SELECT * FROM categories WHERE id=? AND deleted_at IS NULL", (category_id,)
        ).fetchone()
        return self.category_dict(row) if row is not None else None

    def _validate_name(self, value):
        if not isinstance(value, str):
            raise AppError("invalid_field", 400, details={"field": "name"})
        name = js_trim(value)
        if name == "":
            raise AppError("invalid_name", 400)
        if _code_points(name) > MAX_NAME:
            raise AppError("invalid_name", 400)
        if SEARCH_SEPARATOR in name:
            raise AppError("invalid_name", 400)
        return name

    def create_category(self, name_value):
        name = self._validate_name(name_value)
        key = nfkc_lower(name)
        with self.lock:
            self._begin()
            try:
                clash = self._exec(
                    "SELECT id FROM categories WHERE name_key=? AND deleted_at IS NULL",
                    (key,),
                ).fetchone()
                if clash is not None:
                    raise AppError("category_name_conflict", 409)
                stamp = now_iso()
                cur = self._exec(
                    "INSERT INTO categories(name,name_key,is_default,created_at,updated_at)"
                    " VALUES(?,?,0,?,?)",
                    (name, key, stamp, stamp),
                )
                new_id = cur.lastrowid
                self._commit()
            except Exception:
                self._rollback()
                raise
        return self.get_category(new_id)

    def rename_category(self, category_id, name_value):
        name = self._validate_name(name_value)
        key = nfkc_lower(name)
        with self.lock:
            row = self._exec(
                "SELECT * FROM categories WHERE id=? AND deleted_at IS NULL", (category_id,)
            ).fetchone()
            if row is None:
                raise AppError("not_found", 404)
            if row["is_default"]:
                raise AppError("default_category_protected", 409)
            self._begin()
            try:
                clash = self._exec(
                    "SELECT id FROM categories WHERE name_key=? AND deleted_at IS NULL AND id<>?",
                    (key, category_id),
                ).fetchone()
                if clash is not None:
                    raise AppError("category_name_conflict", 409)
                stamp = now_iso()
                self._exec(
                    "UPDATE categories SET name=?, name_key=?, updated_at=? WHERE id=?",
                    (name, key, stamp, category_id),
                )
                self._commit()
            except Exception:
                self._rollback()
                raise
        return self.get_category(category_id)

    def delete_category(self, category_id, mode, target_value, confirm_value):
        if mode is None:
            raise AppError("category_delete_mode_required", 400)
        if mode not in ("move", "purge"):
            raise AppError("invalid_mode", 400)

        with self.lock:
            row = self._exec(
                "SELECT * FROM categories WHERE id=? AND deleted_at IS NULL", (category_id,)
            ).fetchone()
            if row is None:
                raise AppError("not_found", 404)
            if row["is_default"]:
                raise AppError("default_category_protected", 409)

            if mode == "purge":
                if confirm_value is None or confirm_value == "" or confirm_value == "false":
                    raise AppError("confirmation_required", 409)
                if confirm_value != "true":
                    raise AppError("invalid_confirm", 400)

            target_id = None
            if mode == "move":
                if target_value is None or target_value == "":
                    target_id = self.default_category_id()
                else:
                    target_id = self._resolve_category_shape(target_value, null_ok=False)
                    if str(target_id) == str(category_id):
                        raise AppError("invalid_category", 400, reason="self_target")
                    target_row = self._exec(
                        "SELECT * FROM categories WHERE id=? AND deleted_at IS NULL",
                        (target_id,),
                    ).fetchone()
                    if target_row is None:
                        raise AppError("invalid_category", 400, reason="target_unavailable")
            else:
                if target_value is not None:
                    raise AppError("invalid_category", 400, reason="target_not_allowed")

            stamp = now_iso()
            moved = 0
            trashed = 0
            self._begin()
            try:
                if mode == "move":
                    cur = self._exec(
                        "UPDATE bookmarks SET category_id=?, updated_at=?"
                        " WHERE category_id=? AND trashed_at IS NULL",
                        (target_id, stamp, category_id),
                    )
                    moved = cur.rowcount
                else:
                    cur = self._exec(
                        "UPDATE bookmarks SET trashed_at=?, trashed_from_category_id=?, updated_at=?"
                        " WHERE category_id=? AND trashed_at IS NULL",
                        (stamp, category_id, stamp, category_id),
                    )
                    trashed = cur.rowcount
                self._exec("UPDATE categories SET deleted_at=? WHERE id=?", (stamp, category_id))
                self._commit()
            except Exception:
                self._rollback()
                raise

        return {
            "mode": mode,
            "moved": int(moved),
            "trashed": int(trashed),
            "targetCategoryId": str(target_id) if target_id is not None else None,
            "deletedCategoryId": str(category_id),
        }

    # ---------------------------------------------------------------- URL
    def _validate_url(self, value):
        try:
            stored, parsed = urlutil.validate_url_value(value)
        except UrlError as exc:
            details = {}
            if exc.field:
                details["field"] = exc.field
            raise AppError(exc.code, 400, message=str(exc), details=details, reason=exc.reason)
        return stored, parsed, urlutil.url_key(parsed)

    # ---------------------------------------------------------------- 标题/备注
    def _resolve_title_create(self, value, parsed):
        if value is None:
            return urlutil.derived_title(parsed), "derived"
        if not isinstance(value, str):
            raise AppError("invalid_field", 400, details={"field": "title"})
        if SEARCH_SEPARATOR in value:
            raise AppError("invalid_title", 400)
        if _code_points(value) > MAX_TITLE:
            raise AppError("invalid_title", 400)
        title = js_trim(value)
        if title == "":
            return urlutil.derived_title(parsed), "derived"
        return title, "user"

    def _resolve_note(self, value):
        if value is None:
            return ""
        if not isinstance(value, str):
            raise AppError("invalid_field", 400, details={"field": "note"})
        if SEARCH_SEPARATOR in value:
            raise AppError("invalid_note", 400)
        if _code_points(value) > MAX_NOTE:
            raise AppError("invalid_note", 400)
        return value

    def _resolve_category_shape(self, value, null_ok):
        """把形状合法的 categoryId 规范化为十进制字符串；形状错误抛 invalid_category。"""
        if value is None:
            if null_ok:
                return None
            raise AppError("invalid_category", 400)
        if isinstance(value, bool):
            raise AppError("invalid_category", 400)
        if isinstance(value, int):
            if value <= 0:
                raise AppError("invalid_category", 400)
            return str(value)
        if isinstance(value, float):
            raise AppError("invalid_category", 400)
        if isinstance(value, str):
            if value == "":
                raise AppError("invalid_category", 400)
            if not urlutil.is_decimal_id(value):
                raise AppError("invalid_category", 400)
            return value
        raise AppError("invalid_category", 400)

    def _resolve_category_active(self, value, null_ok, default_when_null):
        if value is None:
            if null_ok:
                return None
            if default_when_null:
                return self.default_category_id()
            raise AppError("invalid_category", 400)
        candidate = self._resolve_category_shape(value, null_ok=False)
        row = self._exec(
            "SELECT id FROM categories WHERE id=? AND deleted_at IS NULL", (candidate,)
        ).fetchone()
        if row is None:
            raise AppError("invalid_category", 400, reason="unknown_or_deleted")
        return str(row["id"])

    # ---------------------------------------------------------------- 书签写
    def create_bookmark(self, body, allow_duplicate):
        url_value = body.get("url") if isinstance(body, dict) else None
        title_value = body.get("title") if isinstance(body, dict) else None
        note_value = body.get("note") if isinstance(body, dict) else None
        category_value = body.get("categoryId") if isinstance(body, dict) else None

        stored_url, parsed, key = self._validate_url(url_value)
        title, title_source = self._resolve_title_create(title_value, parsed)
        note = self._resolve_note(note_value)
        category_id = self._resolve_category_active(
            category_value, null_ok=False, default_when_null=True
        )

        with self.lock:
            self._begin()
            try:
                duplicate = self._exec(
                    "SELECT id FROM bookmarks WHERE url_key=? AND trashed_at IS NULL"
                    " ORDER BY id ASC LIMIT 1",
                    (key,),
                ).fetchone()
                if duplicate is not None and not allow_duplicate:
                    raise AppError(
                        "duplicate_url", 409,
                        details={"existingId": str(duplicate["id"])},
                    )
                stamp = now_iso()
                search_text = self._search_text(title, stored_url, note)
                cur = self._exec(
                    "INSERT INTO bookmarks(url,url_key,title,title_source,note,category_id,"
                    "search_text,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?)",
                    (stored_url, key, title, title_source, note, category_id,
                     search_text, stamp, stamp),
                )
                new_id = cur.lastrowid
                self._commit()
            except Exception:
                self._rollback()
                raise
        return self.get_active_bookmark(new_id)

    def get_active_bookmark(self, bookmark_id):
        row = self._exec(
            "SELECT * FROM bookmarks WHERE id=? AND trashed_at IS NULL", (bookmark_id,)
        ).fetchone()
        return self._bookmark_dict(row) if row is not None else None

    def patch_bookmark(self, bookmark_id, body):
        if not isinstance(body, dict):
            raise AppError("invalid_field", 400)
        if "url" in body:
            raise AppError("invalid_field", 400, details={"field": "url"})
        provided = [k for k in ("title", "note", "categoryId") if k in body]
        if not provided:
            raise AppError("empty_patch", 400)

        new_title = None
        new_source = None
        rederive = False
        if "title" in body:
            value = body["title"]
            if value is None:
                rederive = True
            elif not isinstance(value, str):
                raise AppError("invalid_field", 400, details={"field": "title"})
            else:
                if SEARCH_SEPARATOR in value:
                    raise AppError("invalid_title", 400)
                if _code_points(value) > MAX_TITLE:
                    raise AppError("invalid_title", 400)
                title = js_trim(value)
                if title == "":
                    raise AppError("invalid_title", 400)
                new_title = title
                new_source = "user"

        new_note = None
        if "note" in body:
            value = body["note"]
            if not isinstance(value, str):
                raise AppError("invalid_field", 400, details={"field": "note"})
            if SEARCH_SEPARATOR in value:
                raise AppError("invalid_note", 400)
            if _code_points(value) > MAX_NOTE:
                raise AppError("invalid_note", 400)
            new_note = value

        category_present = "categoryId" in body
        category_candidate = None
        if category_present:
            category_candidate = self._resolve_category_shape(body["categoryId"], null_ok=False)

        with self.lock:
            row = self._exec("SELECT * FROM bookmarks WHERE id=?", (bookmark_id,)).fetchone()
            if row is None or row["trashed_at"] is not None:
                raise AppError("not_found", 404)

            if category_present:
                target = self._exec(
                    "SELECT id FROM categories WHERE id=? AND deleted_at IS NULL",
                    (category_candidate,),
                ).fetchone()
                if target is None:
                    raise AppError("invalid_category", 400, reason="unknown_or_deleted")
                category_id = str(target["id"])
            else:
                category_id = str(row["category_id"])

            title = row["title"]
            title_source = row["title_source"]
            if rederive:
                try:
                    _, parsed = urlutil.validate_url_value(row["url"])
                except UrlError:
                    raise AppError("internal", 500)
                title = urlutil.derived_title(parsed)
                title_source = "derived"
            elif new_title is not None:
                title = new_title
                title_source = new_source

            note = new_note if new_note is not None else row["note"]

            stamp = now_iso()
            search_text = self._search_text(title, row["url"], note)
            self._begin()
            try:
                self._exec(
                    "UPDATE bookmarks SET title=?, title_source=?, note=?, category_id=?,"
                    " search_text=?, updated_at=? WHERE id=?",
                    (title, title_source, note, category_id, search_text, stamp, bookmark_id),
                )
                self._commit()
            except Exception:
                self._rollback()
                raise
        return self.get_active_bookmark(bookmark_id)

    def delete_bookmark(self, bookmark_id):
        with self.lock:
            row = self._exec(
                "SELECT * FROM bookmarks WHERE id=? AND trashed_at IS NULL", (bookmark_id,)
            ).fetchone()
            if row is None:
                raise AppError("not_found", 404)
            stamp = now_iso()
            self._begin()
            try:
                self._exec(
                    "UPDATE bookmarks SET trashed_at=?, trashed_from_category_id=?, updated_at=?"
                    " WHERE id=?",
                    (stamp, row["category_id"], stamp, bookmark_id),
                )
                self._commit()
            except Exception:
                self._rollback()
                raise
            trashed = self._exec("SELECT * FROM bookmarks WHERE id=?", (bookmark_id,)).fetchone()
        return self._bookmark_dict(trashed)

    def restore_bookmark(self, bookmark_id, body):
        explicit = (isinstance(body, dict) and ("categoryId" in body)
                    and body.get("categoryId") is not None)

        with self.lock:
            row = self._exec("SELECT * FROM bookmarks WHERE id=?", (bookmark_id,)).fetchone()
            if row is None:
                raise AppError("not_found", 404)
            if row["trashed_at"] is None:
                raise AppError("not_trashed", 409)

            fallback_used = False
            if explicit:
                candidate = self._resolve_category_shape(body["categoryId"], null_ok=False)
                target = self._exec(
                    "SELECT id FROM categories WHERE id=? AND deleted_at IS NULL",
                    (candidate,),
                ).fetchone()
                if target is None:
                    raise AppError("invalid_category", 400, reason="unknown_or_deleted")
                target_id = str(target["id"])
            else:
                source_id = row["trashed_from_category_id"]
                if source_id is None:
                    source_id = row["category_id"]
                source = self._exec(
                    "SELECT id FROM categories WHERE id=? AND deleted_at IS NULL", (source_id,)
                ).fetchone()
                if source is not None:
                    target_id = str(source["id"])
                else:
                    target_id = self.default_category_id()
                    fallback_used = True

            stamp = now_iso()
            self._begin()
            try:
                self._exec(
                    "UPDATE bookmarks SET trashed_at=NULL, trashed_from_category_id=NULL,"
                    " category_id=?, updated_at=? WHERE id=?",
                    (target_id, stamp, bookmark_id),
                )
                self._commit()
            except Exception:
                self._rollback()
                raise
        return {
            "bookmark": self.get_active_bookmark(bookmark_id),
            "restoredToCategoryId": str(target_id),
            "fallbackUsed": bool(fallback_used),
        }

    # ---------------------------------------------------------------- 列表
    def list_bookmarks(self, q, category_value, sort, limit, offset):
        terms = self._query_terms(q)
        if sort not in SORTS:
            raise AppError("invalid_sort", 400)

        where = ["trashed_at IS NULL"]
        params = []
        if category_value is not None and category_value != "":
            candidate = None
            if isinstance(category_value, str) and urlutil.is_decimal_id(category_value):
                candidate = category_value
            if candidate is not None:
                active = self._exec(
                    "SELECT id FROM categories WHERE id=? AND deleted_at IS NULL",
                    (candidate,),
                ).fetchone()
                if active is None:
                    return {"items": [], "total": 0, "limit": limit, "offset": offset}
                where.append("category_id=?")
                params.append(str(active["id"]))
            else:
                return {"items": [], "total": 0, "limit": limit, "offset": offset}

        for term in terms:
            where.append("instr(search_text, ?) > 0")
            params.append(term)

        clause = " AND ".join(where)
        total = self._exec(
            "SELECT COUNT(*) AS c FROM bookmarks WHERE " + clause, params
        ).fetchone()["c"]

        if sort == "created_desc":
            order = " ORDER BY created_at DESC, id DESC"
        else:
            order = " ORDER BY created_at ASC, id ASC"
        rows = self._exec(
            "SELECT * FROM bookmarks WHERE " + clause + order + " LIMIT ? OFFSET ?",
            params + [limit, offset],
        ).fetchall()
        return {
            "items": [self._bookmark_dict(row) for row in rows],
            "total": int(total),
            "limit": limit,
            "offset": offset,
        }

    def list_trash(self, limit, offset):
        total = self._exec(
            "SELECT COUNT(*) AS c FROM bookmarks WHERE trashed_at IS NOT NULL"
        ).fetchone()["c"]
        rows = self._exec(
            "SELECT * FROM bookmarks WHERE trashed_at IS NOT NULL"
            " ORDER BY trashed_at DESC, id DESC LIMIT ? OFFSET ?",
            (limit, offset),
        ).fetchall()
        return {
            "items": [self._trash_dict(row) for row in rows],
            "total": int(total),
            "limit": limit,
            "offset": offset,
        }

    def list_category_bookmarks(self, category_id):
        rows = self._exec(
            "SELECT * FROM bookmarks WHERE category_id=? AND trashed_at IS NULL"
            " ORDER BY created_at DESC, id DESC",
            (category_id,),
        ).fetchall()
        return [self._bookmark_dict(row) for row in rows]

    def truncate_state(self):
        active = self._exec(
            "SELECT COUNT(*) AS c FROM bookmarks WHERE trashed_at IS NULL"
        ).fetchone()["c"]
        trashed = self._exec(
            "SELECT COUNT(*) AS c FROM bookmarks WHERE trashed_at IS NOT NULL"
        ).fetchone()["c"]
        return {"active": int(active), "trashed": int(trashed), "total": int(active) + int(trashed)}

    # ---------------------------------------------------------------- 回收站写
    def purge_trash_item(self, bookmark_id):
        with self.lock:
            row = self._exec(
                "SELECT id FROM bookmarks WHERE id=? AND trashed_at IS NOT NULL",
                (bookmark_id,),
            ).fetchone()
            if row is None:
                raise AppError("not_found", 404)
            self._begin()
            try:
                self._exec("DELETE FROM bookmarks WHERE id=?", (bookmark_id,))
                self._commit()
            except Exception:
                self._rollback()
                raise
        return {"purged": 1}

    def purge_trash_all(self):
        with self.lock:
            total = self._exec(
                "SELECT COUNT(*) AS c FROM bookmarks WHERE trashed_at IS NOT NULL"
            ).fetchone()["c"]
            self._begin()
            try:
                self._exec("DELETE FROM bookmarks WHERE trashed_at IS NOT NULL")
                self._commit()
            except Exception:
                self._rollback()
                raise
        return {"purged": int(total)}
