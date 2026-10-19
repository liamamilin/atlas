"""Persistence and money handling for the local monthly budget app.

All durable data lives in a single SQLite file inside the configured data
directory. Money is stored as integer minor units (fen / cents) so summaries
never lose precision; the JSON layer converts to two-decimal strings.
"""

import os
import re
import sqlite3
from contextlib import closing
from datetime import date as _date

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
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    amount_cents INTEGER NOT NULL,
    note TEXT NOT NULL DEFAULT ''
);

CREATE INDEX IF NOT EXISTS idx_transactions_category ON transactions(category_id);
"""

_MONEY_RE = re.compile(r"^\d+(?:\.\d{1,2})?$")
_MONTH_RE = re.compile(r"^\d{4}-(?:0[1-9]|1[0-2])$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(ValueError):
    """Raised for user-supplied values that fail validation."""


def default_db_path(data_dir):
    return os.path.join(data_dir, "budget.sqlite3")


def connect(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path):
    with closing(connect(db_path)) as conn:
        conn.executescript(SCHEMA)
        conn.commit()


# --- money -----------------------------------------------------------------

def format_money(cents):
    sign = "-" if cents < 0 else ""
    cents = abs(int(cents))
    return "%s%d.%02d" % (sign, cents // 100, cents % 100)


def parse_money(value, allow_zero=True):
    """Return integer cents. Rejects malformed or over-precise input."""
    if isinstance(value, bool):
        raise ValidationError("金额无效")
    if isinstance(value, int):
        text = str(value)
    elif isinstance(value, str):
        text = value.strip()
    else:
        raise ValidationError("金额必须是数字字符串，例如 12.50")
    if not _MONEY_RE.match(text):
        raise ValidationError("金额必须是最多两位小数的非负数字，例如 12.50")
    whole, _, frac = text.partition(".")
    cents = int(whole) * 100 + int((frac + "00")[:2])
    if cents == 0 and not allow_zero:
        raise ValidationError("支出金额必须大于 0")
    return cents


# --- value validation ------------------------------------------------------

def validate_month(month):
    if not isinstance(month, str) or not _MONTH_RE.match(month):
        raise ValidationError("月份格式必须为 YYYY-MM")
    return month


def validate_date(value):
    if not isinstance(value, str) or not _DATE_RE.match(value):
        raise ValidationError("日期格式必须为 YYYY-MM-DD")
    try:
        _date.fromisoformat(value)
    except ValueError:
        raise ValidationError("日期不是有效日期")
    return value


def clean_name(value):
    if not isinstance(value, str):
        raise ValidationError("分类名称必须是文本")
    name = value.strip()
    if not name:
        raise ValidationError("分类名称不能为空")
    if len(name) > 100:
        raise ValidationError("分类名称过长")
    return name


def clean_note(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValidationError("备注必须是文本")
    return value


# --- categories ------------------------------------------------------------

def get_category(conn, category_id):
    return conn.execute(
        "SELECT id, month, name, budget_cents FROM categories WHERE id = ?",
        (category_id,),
    ).fetchone()


def category_spent(conn, category_id):
    row = conn.execute(
        "SELECT COALESCE(SUM(amount_cents), 0) AS s FROM transactions WHERE category_id = ?",
        (category_id,),
    ).fetchone()
    return int(row["s"])


def category_entry(conn, row):
    budget = int(row["budget_cents"])
    spent = category_spent(conn, row["id"])
    return {
        "id": row["id"],
        "name": row["name"],
        "budget": format_money(budget),
        "spent": format_money(spent),
        "remaining": format_money(budget - spent),
    }


def create_category(conn, month, name, budget_cents):
    cur = conn.execute(
        "INSERT INTO categories (month, name, budget_cents) VALUES (?, ?, ?)",
        (month, name, budget_cents),
    )
    return cur.lastrowid


def update_category_budget(conn, category_id, budget_cents):
    conn.execute(
        "UPDATE categories SET budget_cents = ? WHERE id = ?",
        (budget_cents, category_id),
    )


# --- transactions ----------------------------------------------------------

def get_transaction(conn, transaction_id):
    return conn.execute(
        "SELECT id, date, category_id, amount_cents, note FROM transactions WHERE id = ?",
        (transaction_id,),
    ).fetchone()


def create_transaction(conn, txn_date, category_id, amount_cents, note):
    cur = conn.execute(
        "INSERT INTO transactions (date, category_id, amount_cents, note) VALUES (?, ?, ?, ?)",
        (txn_date, category_id, amount_cents, note),
    )
    return cur.lastrowid


def update_transaction(conn, transaction_id, txn_date, category_id, amount_cents, note):
    conn.execute(
        "UPDATE transactions SET date = ?, category_id = ?, amount_cents = ?, note = ? WHERE id = ?",
        (txn_date, category_id, amount_cents, note, transaction_id),
    )


def delete_transaction(conn, transaction_id):
    conn.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))


def transaction_entry(conn, row):
    return {
        "id": row["id"],
        "date": row["date"],
        "category_id": row["category_id"],
        "amount": format_money(row["amount_cents"]),
        "note": row["note"],
    }


# --- state & export --------------------------------------------------------

def get_state(conn, month):
    rows = conn.execute(
        "SELECT id, name, budget_cents FROM categories WHERE month = ? ORDER BY id",
        (month,),
    ).fetchall()

    spent_rows = conn.execute(
        "SELECT category_id, COALESCE(SUM(amount_cents), 0) AS s "
        "FROM transactions WHERE category_id IN "
        "(SELECT id FROM categories WHERE month = ?) GROUP BY category_id",
        (month,),
    ).fetchall()
    spent = {r["category_id"]: int(r["s"]) for r in spent_rows}

    categories = []
    for row in rows:
        budget = int(row["budget_cents"])
        used = spent.get(row["id"], 0)
        categories.append({
            "id": row["id"],
            "name": row["name"],
            "budget": format_money(budget),
            "spent": format_money(used),
            "remaining": format_money(budget - used),
        })

    txn_rows = conn.execute(
        "SELECT t.id, t.date, t.category_id, t.amount_cents, t.note "
        "FROM transactions t JOIN categories c ON c.id = t.category_id "
        "WHERE c.month = ? ORDER BY t.date, t.id",
        (month,),
    ).fetchall()
    transactions = [
        {
            "id": r["id"],
            "date": r["date"],
            "category_id": r["category_id"],
            "amount": format_money(r["amount_cents"]),
            "note": r["note"],
        }
        for r in txn_rows
    ]

    total_budget = sum(c["budget_cents"] for c in rows) if rows else 0
    total_spent = sum(spent.values()) if spent else 0
    return {
        "month": month,
        "categories": categories,
        "transactions": transactions,
        "totals": {
            "budget": format_money(total_budget),
            "spent": format_money(total_spent),
            "remaining": format_money(total_budget - total_spent),
        },
    }


def export_rows(conn, month):
    return conn.execute(
        "SELECT t.date AS date, c.name AS category, t.amount_cents AS amount_cents, t.note AS note "
        "FROM transactions t JOIN categories c ON c.id = t.category_id "
        "WHERE c.month = ? ORDER BY t.date, t.id",
        (month,),
    ).fetchall()
