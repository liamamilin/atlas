# -*- coding: utf-8 -*-
"""SQLite 持久化层。

单库（budget.sqlite3）位于 --data-dir；金额一律以整数“分”存储；
每次写入都在事务中提交，读操作按稳定顺序返回以保证重启后状态一致。
"""

import sqlite3
from contextlib import contextmanager

from money import format_cents

SCHEMA = """
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT NOT NULL,
    name TEXT NOT NULL,
    budget_cents INTEGER NOT NULL,
    UNIQUE (month, name)
);
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    amount_cents INTEGER NOT NULL,
    note TEXT NOT NULL DEFAULT '',
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
"""


class StoreError(Exception):
    """领域错误基类，由 API 层映射为 HTTP 错误。"""


class DuplicateName(StoreError):
    """同一月份已存在同名分类。"""


class NotFound(StoreError):
    """目标记录不存在。"""


class MonthMismatch(StoreError):
    """支出日期与分类所属月份不一致。"""


class Store(object):
    def __init__(self, db_path):
        self.db_path = db_path
        with self._connect() as con:
            con.executescript(SCHEMA)

    @contextmanager
    def _connect(self):
        con = sqlite3.connect(self.db_path, timeout=15)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys = ON")
        try:
            yield con
            con.commit()
        except Exception:
            con.rollback()
            raise
        finally:
            con.close()

    # ---- 读取 ---------------------------------------------------------
    def get_state(self, month):
        with self._connect() as con:
            categories = con.execute(
                "SELECT id, name, budget_cents FROM categories "
                "WHERE month = ? ORDER BY id",
                (month,),
            ).fetchall()
            spent_rows = con.execute(
                "SELECT category_id AS cid, SUM(amount_cents) AS total "
                "FROM transactions WHERE category_id IN "
                "(SELECT id FROM categories WHERE month = ?) "
                "GROUP BY category_id",
                (month,),
            ).fetchall()
            transactions = con.execute(
                "SELECT t.id, t.date, t.category_id, t.amount_cents, t.note "
                "FROM transactions t JOIN categories c ON c.id = t.category_id "
                "WHERE c.month = ? ORDER BY t.date, t.id",
                (month,),
            ).fetchall()

        spent_by_cat = {row["cid"]: (row["total"] or 0) for row in spent_rows}
        cat_list = []
        total_budget = total_spent = total_remaining = 0
        for row in categories:
            budget = int(row["budget_cents"])
            spent = spent_by_cat.get(row["id"], 0)
            remaining = budget - spent
            total_budget += budget
            total_spent += spent
            total_remaining += remaining
            cat_list.append({
                "id": row["id"],
                "name": row["name"],
                "budget": format_cents(budget),
                "spent": format_cents(spent),
                "remaining": format_cents(remaining),
            })
        txn_list = [{
            "id": row["id"],
            "date": row["date"],
            "category_id": row["category_id"],
            "amount": format_cents(row["amount_cents"]),
            "note": row["note"],
        } for row in transactions]

        return {
            "month": month,
            "categories": cat_list,
            "transactions": txn_list,
            "totals": {
                "budget": format_cents(total_budget),
                "spent": format_cents(total_spent),
                "remaining": format_cents(total_remaining),
            },
        }

    def export_rows(self, month):
        """返回当月 CSV 数据行（不含表头），列为 [date, category, amount, note]。"""
        with self._connect() as con:
            rows = con.execute(
                "SELECT t.date AS date, c.name AS category, "
                "t.amount_cents AS amount_cents, t.note AS note "
                "FROM transactions t JOIN categories c ON c.id = t.category_id "
                "WHERE c.month = ? ORDER BY t.date, t.id",
                (month,),
            ).fetchall()
        return [[row["date"], row["category"],
                 format_cents(row["amount_cents"]), row["note"]] for row in rows]

    # ---- 写入 ---------------------------------------------------------
    def create_category(self, month, name, budget_cents):
        with self._connect() as con:
            existing = con.execute(
                "SELECT id FROM categories WHERE month = ? AND name = ?",
                (month, name),
            ).fetchone()
            if existing is not None:
                raise DuplicateName("该月份已存在同名分类")
            cur = con.execute(
                "INSERT INTO categories (month, name, budget_cents) VALUES (?, ?, ?)",
                (month, name, budget_cents),
            )
            return cur.lastrowid

    def update_category_budget(self, category_id, budget_cents):
        with self._connect() as con:
            row = con.execute(
                "SELECT id, month, name FROM categories WHERE id = ?",
                (category_id,),
            ).fetchone()
            if row is None:
                raise NotFound("分类不存在")
            con.execute(
                "UPDATE categories SET budget_cents = ? WHERE id = ?",
                (budget_cents, category_id),
            )
            return {"id": row["id"], "month": row["month"], "name": row["name"]}

    def create_transaction(self, date, category_id, amount_cents, note):
        with self._connect() as con:
            cat = con.execute(
                "SELECT id, month FROM categories WHERE id = ?",
                (category_id,),
            ).fetchone()
            if cat is None:
                raise NotFound("分类不存在")
            if date[:7] != cat["month"]:
                raise MonthMismatch("支出日期必须属于该分类所在月份")
            cur = con.execute(
                "INSERT INTO transactions (date, category_id, amount_cents, note) "
                "VALUES (?, ?, ?, ?)",
                (date, category_id, amount_cents, note),
            )
            return cur.lastrowid

    def update_transaction(self, transaction_id, date, category_id, amount_cents, note):
        with self._connect() as con:
            txn = con.execute(
                "SELECT id FROM transactions WHERE id = ?", (transaction_id,)
            ).fetchone()
            if txn is None:
                raise NotFound("支出不存在")
            cat = con.execute(
                "SELECT id, month FROM categories WHERE id = ?", (category_id,)
            ).fetchone()
            if cat is None:
                raise NotFound("分类不存在")
            if date[:7] != cat["month"]:
                raise MonthMismatch("支出日期必须属于该分类所在月份")
            con.execute(
                "UPDATE transactions SET date = ?, category_id = ?, "
                "amount_cents = ?, note = ? WHERE id = ?",
                (date, category_id, amount_cents, note, transaction_id),
            )
            return transaction_id

    def delete_transaction(self, transaction_id):
        with self._connect() as con:
            cur = con.execute(
                "DELETE FROM transactions WHERE id = ?", (transaction_id,)
            )
            if cur.rowcount == 0:
                raise NotFound("支出不存在")
            return transaction_id
