#!/usr/bin/env python3
"""Monthly budgeting, local single-user SQLite; no banking connections."""

import argparse
from datetime import date
from decimal import Decimal
from http.server import ThreadingHTTPServer
from pathlib import Path
import re
import uuid
from urllib.parse import urlencode
from web_support import Error, Handler, connect, h, options, page


def money(value, positive=False):
    if not isinstance(value, str) or not re.fullmatch(
        r"[0-9]+(?:\.[0-9]{1,2})?", value
    ):
        raise Error(
            "invalid_amount", "金额请填写非负数，最多两位小数；支出和转移须大于0。"
        )
    amount = int(Decimal(value) * 100)
    if amount > 99999999999 or (positive and amount <= 0):
        raise Error("invalid_amount", "金额超出范围，或支出/转移未大于0。")
    return amount


def month(value):
    if (
        not isinstance(value, str)
        or not re.fullmatch(r"[0-9]{4}-(0[1-9]|1[0-2])", value)
        or int(value[:4]) < 1
    ):
        raise Error("invalid_month", "请选择有效月份（YYYY-MM）。")
    return value


def fmt(value):
    return f"{value // 100}.{value % 100:02}" if value >= 0 else "-" + fmt(-value)


def name(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80:
        raise Error("invalid_name", "用途名称不能为空，且不能超过80个字符。")
    return value.strip()


class Budget:
    def __init__(self, directory, demo=False):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "budget.sqlite3"
        with connect(self.path) as db:
            db.executescript("""CREATE TABLE IF NOT EXISTS meta(version INTEGER);
            CREATE TABLE IF NOT EXISTS months(month TEXT PRIMARY KEY,income_minor INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS categories(id TEXT PRIMARY KEY,month TEXT NOT NULL REFERENCES months(month),name TEXT NOT NULL,planned_minor INTEGER NOT NULL,UNIQUE(month,name));
            CREATE TABLE IF NOT EXISTS expenses(id TEXT PRIMARY KEY,month TEXT NOT NULL REFERENCES months(month),date TEXT NOT NULL,category_id TEXT NOT NULL REFERENCES categories(id),amount_minor INTEGER NOT NULL,note TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS template(name TEXT PRIMARY KEY,planned_minor INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY,value INTEGER NOT NULL);""")
            if not db.execute("SELECT 1 FROM meta").fetchone():
                db.execute("INSERT INTO meta VALUES(1)")
                if demo:
                    m = date.today().strftime("%Y-%m")
                    self.change(db, "/months/start", {"month": m})
                    self.change(db, "/income", {"month": m, "income": "5000"})
                    self.change(
                        db,
                        "/categories",
                        {"month": m, "name": "[演示] 食品", "amount": "1000"},
                    )
                    self.change(
                        db,
                        "/categories",
                        {"month": m, "name": "[演示] 交通", "amount": "200"},
                    )

    @staticmethod
    def require(db, m):
        row = db.execute("SELECT * FROM months WHERE month=?", (m,)).fetchone()
        if row is None:
            raise Error("not_found", "请先创建这个月的计划。", 404)
        return row

    @staticmethod
    def category(db, m, identifier):
        row = db.execute(
            "SELECT * FROM categories WHERE id=? AND month=?", (identifier, m)
        ).fetchone()
        if row is None:
            raise Error("invalid_category", "请选择当前月份的已有用途。")
        return row

    def state(self, db, m):
        m = month(m)
        row = db.execute("SELECT * FROM months WHERE month=?", (m,)).fetchone()
        cats = [
            dict(r)
            for r in db.execute(
                "SELECT c.*,COALESCE(SUM(e.amount_minor),0) AS spent_minor FROM categories c LEFT JOIN expenses e ON e.category_id=c.id AND e.month=c.month WHERE c.month=? GROUP BY c.id ORDER BY c.rowid",
                (m,),
            )
        ]
        for cat in cats:
            cat["remaining_minor"] = cat["planned_minor"] - cat["spent_minor"]
        expenses = [
            dict(r)
            for r in db.execute(
                "SELECT e.*,c.name AS category_name FROM expenses e JOIN categories c ON c.id=e.category_id WHERE e.month=? ORDER BY e.date DESC,e.rowid DESC",
                (m,),
            )
        ]
        planned = sum(c["planned_minor"] for c in cats)
        spent = sum(e["amount_minor"] for e in expenses)
        income = row["income_minor"] if row else 0
        return {
            "initialized": row is not None,
            "month": m,
            "income_minor": income,
            "categories": cats,
            "expenses": expenses,
            "totals": {
                "planned_minor": planned,
                "spent_minor": spent,
                "remaining_minor": planned - spent,
                "unallocated_minor": income - planned,
            },
        }

    def change(self, db, action, data):
        m = month(data.get("month"))
        if action == "/months/start":
            if db.execute("SELECT 1 FROM months WHERE month=?", (m,)).fetchone():
                raise Error("already_exists", "这个月的计划已存在，不会覆盖。", 409)
            income = db.execute(
                "SELECT value FROM settings WHERE key='template_income'"
            ).fetchone()
            db.execute(
                "INSERT INTO months VALUES(?,?)", (m, income[0] if income else 0)
            )
            for row in db.execute("SELECT * FROM template ORDER BY rowid").fetchall():
                db.execute(
                    "INSERT INTO categories VALUES(?,?,?,?)",
                    (uuid.uuid4().hex, m, row["name"], row["planned_minor"]),
                )
            return {"month": m}, 201
        self.require(db, m)
        if action == "/income":
            value = money(data.get("income"))
            db.execute("UPDATE months SET income_minor=? WHERE month=?", (value, m))
            return {"income_minor": value}, 200
        if action == "/categories":
            n = name(data.get("name"))
            amount = money(data.get("amount"))
            if db.execute(
                "SELECT 1 FROM categories WHERE month=? AND name=?", (m, n)
            ).fetchone():
                raise Error(
                    "already_exists", "这个月已有同名用途，请使用行内预算修改。", 409
                )
            identifier = uuid.uuid4().hex
            db.execute(
                "INSERT INTO categories VALUES(?,?,?,?)", (identifier, m, n, amount)
            )
            return {"id": identifier}, 201
        if action == "/categories/update":
            cat = self.category(db, m, data.get("id"))
            amount = money(data.get("amount"))
            db.execute(
                "UPDATE categories SET planned_minor=? WHERE id=?", (amount, cat["id"])
            )
            return {"id": cat["id"]}, 200
        if action in ("/expenses", "/expenses/update"):
            cat = self.category(db, m, data.get("category_id"))
            amount = money(data.get("amount"), True)
            try:
                day = date.fromisoformat(data.get("date", ""))
                if day.isoformat() != data.get("date") or day.strftime("%Y-%m") != m:
                    raise ValueError()
            except (TypeError, ValueError):
                raise Error(
                    "invalid_date", "支出日期必须有效，且属于当前月份。"
                ) from None
            note = data.get("note", "")
            if not isinstance(note, str) or len(note) > 2000:
                raise Error("bad_request", "备注最多2000个字符。")
            if action == "/expenses/update":
                identifier = data.get("id")
                if not db.execute(
                    "SELECT 1 FROM expenses WHERE id=? AND month=?", (identifier, m)
                ).fetchone():
                    raise Error("not_found", "这笔支出不存在于当前月份。", 404)
                db.execute(
                    "UPDATE expenses SET date=?,category_id=?,amount_minor=?,note=? WHERE id=?",
                    (str(day), cat["id"], amount, note, identifier),
                )
            else:
                identifier = uuid.uuid4().hex
                db.execute(
                    "INSERT INTO expenses VALUES(?,?,?,?,?,?)",
                    (identifier, m, str(day), cat["id"], amount, note),
                )
            return {"id": identifier}, 201 if action == "/expenses" else 200
        if action == "/transfer":
            source = self.category(db, m, data.get("source_id"))
            target = self.category(db, m, data.get("target_id"))
            amount = money(data.get("amount"), True)
            if source["id"] == target["id"] or amount > source["planned_minor"]:
                raise Error(
                    "invalid_amount",
                    "请选择两个不同用途，且转移金额不能超过来源用途的计划。",
                )
            db.execute(
                "UPDATE categories SET planned_minor=planned_minor-? WHERE id=?",
                (amount, source["id"]),
            )
            db.execute(
                "UPDATE categories SET planned_minor=planned_minor+? WHERE id=?",
                (amount, target["id"]),
            )
            return {"ok": True}, 200
        if action == "/template":
            db.execute("DELETE FROM template")
            db.executemany(
                "INSERT INTO template VALUES(?,?)",
                [
                    (r["name"], r["planned_minor"])
                    for r in db.execute(
                        "SELECT * FROM categories WHERE month=? ORDER BY rowid", (m,)
                    ).fetchall()
                ],
            )
            db.execute(
                "INSERT OR REPLACE INTO settings VALUES('template_income',?)",
                (self.require(db, m)["income_minor"],),
            )
            return {"ok": True}, 200
        raise Error("not_found", "这个操作不存在。", 404)


def field(label, key, value="", kind="text", extra=""):
    identifier = key + "-" + uuid.uuid5(uuid.NAMESPACE_DNS, label).hex[:8]
    return f'<div class="field"><label for="{identifier}">{h(label)}</label><input id="{identifier}" name="{h(key)}" type="{kind}" value="{h(value)}" {extra}></div>'


def hidden(key, value):
    return f'<input type="hidden" name="{h(key)}" value="{h(value)}">'


class Web(Handler):
    def dispatch(self, method):
        lib = self.server.library
        if self.route == "/api/health" and method == "GET":
            return self.json(200, {"ready": True, "origin": "assisted-trial"})
        m = month(
            self.data.get(
                "month", self.query.get("month", date.today().strftime("%Y-%m"))
            )
        )
        with connect(lib.path) as db:
            if method == "GET":
                if self.route == "/api/state":
                    return self.json(200, lib.state(db, m))
                if self.route == "/":
                    return self.send(200, self.home(db, m))
                if re.fullmatch(r"/expense/[a-f0-9]+/edit", self.route):
                    row = db.execute(
                        "SELECT * FROM expenses WHERE id=?", (self.route.split("/")[2],)
                    ).fetchone()
                    if row is None:
                        raise Error("not_found", "没有找到这笔支出。", 404)
                    return self.send(200, self.edit(db, dict(row)))
            if method == "POST":
                db.execute("BEGIN IMMEDIATE")
                result, status = lib.change(
                    db, self.route.removeprefix("/api"), self.data
                )
                db.commit()
                return (
                    self.json(status, result)
                    if self.route.startswith("/api/")
                    else self.redirect("/?" + urlencode({"month": m, "saved": "1"}))
                )
            raise Error("not_found", "页面不存在。", 404)

    def error_page(self, error):
        m = self.data.get(
            "month", self.query.get("month", date.today().strftime("%Y-%m"))
        )
        try:
            month(m)
        except Error:
            m = date.today().strftime("%Y-%m")
        with connect(self.server.library.path) as db:
            if self.route.endswith("/expenses/update"):
                row = db.execute(
                    "SELECT * FROM expenses WHERE id=?", (self.data.get("id"),)
                ).fetchone()
                if row:
                    return self.edit(db, {**dict(row), **self.data}, error)
            return self.home(db, m, error, self.data)

    def expense_form(self, state, values=None, edit=False):
        values = values or {}
        m = state["month"]
        today = date.today().isoformat()
        day = today if today.startswith(m) else m + "-01"
        catopts = options(
            [(c["id"], c["name"]) for c in state["categories"]],
            values.get("category_id", ""),
        )
        amount = values.get(
            "amount", fmt(values["amount_minor"]) if "amount_minor" in values else ""
        )
        action = "/expenses/update" if edit else "/expenses"
        return f'''<form method="post" action="{action}" data-testid="expense-form" novalidate>{hidden("month", m)}{hidden("id", values.get("id", ""))}{field("日期", "date", values.get("date", day), "date")}
        <div class="field"><label for="category_id">归属用途</label><select id="category_id" name="category_id">{catopts}</select></div>{field("支出金额（元）", "amount", amount, extra='inputmode="decimal" placeholder="例如 35.50"')}{field("备注（可选）", "note", values.get("note", ""))}<button class="primary">{"保存修改" if edit else "记录支出"}</button></form>'''

    def edit(self, db, row, error=None):
        s = self.server.library.state(db, row["month"])
        msg = (
            f'<p class="notice error" role="alert">{h(error.message)}</p>'
            if error
            else ""
        )
        return page(
            "月有度 · 个人预算",
            "修改这笔支出",
            f'<a href="/?month={h(row["month"])}">← 返回当月</a><section class="panel" style="max-width:600px;margin-top:20px">{msg}{self.expense_form(s, row, True)}</section>',
        )

    def home(self, db, m, error=None, values=None):
        s = self.server.library.state(db, m)
        values = values or {}
        urlmonth = hidden("month", m)
        head = f"""<p class="muted">计划先行，消费前看一眼剩余。金额单位：人民币元。</p><form class="inline panel" method="get" data-testid="month-form">{field("查看月份", "month", m, "month")}<button>查看月份</button></form>"""
        if error:
            head += f'<p class="notice error" role="alert">{h(error.message)} ({h(error.code)})</p>'
        elif self.query.get("saved"):
            head += '<p class="notice" role="status">已保存，金额已重新计算。</p>'
        if not s["initialized"]:
            return page(
                "月有度 · 个人预算",
                "每个月，都心中有数。",
                head
                + f'<section class="panel"><h2>这个月还没有计划</h2><p class="muted">创建时只复制已保存模板的用途、计划与预计收入，不复制支出，也不结转剩余；没有模板则从空白开始。</p><form method="post" action="/months/start">{urlmonth}<button class="primary">创建本月计划</button></form></section>',
            )
        t = s["totals"]
        cards = ""
        for label, key in [
            ("计划支出", "planned_minor"),
            ("已花费", "spent_minor"),
            ("计划剩余", "remaining_minor"),
            ("收入未分配", "unallocated_minor"),
        ]:
            cards += f'<div class="metric"><small>{label}</small><strong class="{"negative" if t[key] < 0 else ""}">¥{fmt(t[key])}</strong><small>{"已超支 / 超额分配" if t[key] < 0 else m}</small></div>'
        cats = ""
        for c in s["categories"]:
            cats += f'''<tr data-testid="category-row" data-id="{c["id"]}"><td>{h(c["name"])}</td><td class="amount">{fmt(c["planned_minor"])}</td><td class="amount">{fmt(c["spent_minor"])}</td><td class="amount {"negative" if c["remaining_minor"] < 0 else ""}">{fmt(c["remaining_minor"])}</td><td><form class="inline" action="/categories/update" method="post">{urlmonth}{hidden("id", c["id"])}<input class="small-input" name="amount" aria-label="{h(c["name"])}预算" value="{fmt(c["planned_minor"])}" inputmode="decimal"><button>改预算</button></form></td></tr>'''
        expenses = "".join(
            f'<tr data-testid="expense-row" data-id="{e["id"]}"><td>{h(e["date"])}</td><td>{h(e["category_name"])}</td><td>{h(e["note"])}</td><td class="amount">{fmt(e["amount_minor"])}</td><td><a href="/expense/{e["id"]}/edit">编辑</a></td></tr>'
            for e in s["expenses"]
        )
        allopts = options([(c["id"], c["name"]) for c in s["categories"]])
        content = (
            head
            + f"""<div class="cards" data-testid="totals">{cards}</div><div class="grid"><div><section class="panel"><h2>{m} · 用途预算</h2><form class="inline" action="/income" method="post">{urlmonth}{field("本月预计收入（元）", "income", values.get("income", fmt(s["income_minor"])))}<button>保存收入</button></form><div class="table-wrap"><table><thead><tr><th>用途</th><th class="amount">计划</th><th class="amount">实际</th><th class="amount">剩余</th><th>调整</th></tr></thead><tbody>{cats}</tbody></table></div>{'<p class="empty">还没有用途，先添加一个预算项目。</p>' if not cats else ""}<h3>添加用途</h3><form class="inline" action="/categories" method="post" novalidate>{urlmonth}{field("用途名称", "name", values.get("name", ""), extra='placeholder="如：食品"')}{field("计划金额（元）", "amount", values.get("amount", ""))}<button>添加用途</button></form></section>
        <section class="panel"><h2>本月支出</h2><div class="table-wrap"><table><thead><tr><th>日期</th><th>用途</th><th>备注</th><th class="amount">金额</th><th>操作</th></tr></thead><tbody>{expenses}</tbody></table></div>{'<p class="empty">还没有支出，记下第一笔消费吧。</p>' if not expenses else ""}</section>
        <section class="panel"><h2>在用途之间调整计划</h2><p class="muted">只移动计划金额，不改历史支出，计划总额保持不变。</p><form class="inline" method="post" action="/transfer">{urlmonth}<div class="field"><label for="source_id">从</label><select id="source_id" name="source_id">{allopts}</select></div><div class="field"><label for="target_id">转入</label><select id="target_id" name="target_id">{allopts}</select></div>{field("转移金额", "amount", values.get("amount", ""))}<button>转移计划金额</button></form></section></div>
        <aside><section class="panel"><h2>＋ 记一笔支出</h2>{self.expense_form(s, values) if s["categories"] else '<p class="muted">先添加至少一个用途，再记录支出。</p>'}</section><section class="panel"><h2>为下个月留个模板</h2><p class="muted">保存当前用途预算和预计收入为模板。下个月创建计划时使用；不带入任何支出或剩余。</p><form method="post" action="/template">{urlmonth}<button>保存本月计划为模板</button></form></section></aside></div>"""
        )
        return page("月有度 · 个人预算", "每个月，都心中有数。", content)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--port", type=int, default=5274)
    p.add_argument("--host", default="127.0.0.1", choices=["127.0.0.1", "localhost"])
    p.add_argument(
        "--data-dir", type=Path, default=Path(__file__).resolve().parents[1] / "data"
    )
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    lib = Budget(args.data_dir.resolve(), args.demo)
    with ThreadingHTTPServer((args.host, args.port), Web) as server:
        server.library = lib
        print(f"月有度 http://{args.host}:{args.port}/ · {lib.path}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
