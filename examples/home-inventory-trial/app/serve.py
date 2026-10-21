#!/usr/bin/env python3
"""Local, single-user home inventory. Python standard library only."""

import argparse
from http.server import ThreadingHTTPServer
from pathlib import Path
import re
import sqlite3
from urllib.parse import urlencode
from uuid import uuid4

from web_support import Error, Handler, connect, h, options, page

ROOT = Path(__file__).resolve().parents[1]


def text(value, minimum, maximum, code, label):
    if not isinstance(value, str) or not minimum <= len(value.strip()) <= maximum:
        raise Error(code, f"{label}需填写 {minimum}–{maximum} 个字符。")
    return value.strip()


def money(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"[0-9]+(?:\.[0-9]{1,2})?", value
    ):
        raise Error(
            "invalid_value", "估值请填写非负金额，最多两位小数；不接受指数或特殊值。"
        )
    whole, _, fraction = value.partition(".")
    # Bound length before integer conversion, also rejecting excessive leading zeroes.
    if len(whole.lstrip("0")) > 9:
        raise Error("invalid_value", "估值最大为 999999999.99 元。")
    minor = int(whole.lstrip("0") or "0") * 100 + int(fraction.ljust(2, "0") or "0")
    if minor > 99999999999:
        raise Error("invalid_value", "估值最大为 999999999.99 元。")
    return minor


def amount(minor):
    return f"{minor // 100:,}.{minor % 100:02d}"


class Inventory:
    def __init__(self, directory, demo=False):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "inventory.sqlite3"
        with connect(self.path) as db:
            fresh = not db.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name='locations'"
            ).fetchone()
            db.executescript("""CREATE TABLE IF NOT EXISTS locations (id TEXT PRIMARY KEY, name TEXT NOT NULL UNIQUE);
            CREATE TABLE IF NOT EXISTS items (id TEXT PRIMARY KEY, name TEXT NOT NULL,
            location_id TEXT NOT NULL REFERENCES locations(id), value_minor INTEGER NOT NULL CHECK(value_minor>=0),
            notes TEXT NOT NULL DEFAULT '', archived INTEGER NOT NULL DEFAULT 0 CHECK(archived IN (0,1)),
            revision INTEGER NOT NULL DEFAULT 1);""")
            if fresh:
                db.execute(
                    "INSERT INTO locations VALUES (?,?)", ("uncategorized", "未分类")
                )
                if demo:
                    db.executemany(
                        "INSERT INTO locations VALUES (?,?)",
                        [("bedroom", "卧室"), ("kitchen", "厨房"), ("living", "客厅")],
                    )
                    db.executemany(
                        "INSERT INTO items VALUES (?,?,?,?,?,?,?)",
                        [
                            (
                                "demo-desk",
                                "橡木书桌",
                                "bedroom",
                                90000,
                                "搬家时先拆下桌腿；螺丝放在抽屉里。",
                                0,
                                1,
                            ),
                            (
                                "demo-lamp",
                                "阅读台灯",
                                "bedroom",
                                18000,
                                "床头使用，灯泡单独装盒。",
                                0,
                                1,
                            ),
                            (
                                "demo-kettle",
                                "电热水壶",
                                "kitchen",
                                12900,
                                "1.5L，留在最后一天打包。",
                                0,
                                1,
                            ),
                            (
                                "demo-books",
                                "旧版旅行图册",
                                "living",
                                6500,
                                "暂不参与本次搬家盘点。",
                                1,
                                1,
                            ),
                        ],
                    )

    def state(self, query=None):
        query = query or {}
        view = query.get("view", "active")
        if view not in ("active", "archive", "all"):
            raise Error("bad_request", "请选择有效的物品视图。")
        with connect(self.path) as db:
            locations = [
                dict(r) for r in db.execute("SELECT * FROM locations ORDER BY rowid")
            ]
            rows = [
                dict(r) for r in db.execute("SELECT * FROM items ORDER BY rowid DESC")
            ]
        needle = query.get("q", "").casefold()
        location = query.get("location", "")
        rows = [
            r
            for r in rows
            if (view == "all" or bool(r["archived"]) == (view == "archive"))
            and (not location or r["location_id"] == location)
            and (
                not needle
                or needle in r["name"].casefold()
                or needle in r["notes"].casefold()
            )
        ]
        for row in rows:
            row["archived"] = bool(row["archived"])
        return {
            "locations": locations,
            "items": rows,
            "summary": {
                "count": len(rows),
                "total_minor": sum(r["value_minor"] for r in rows),
            },
        }

    def get(self, identity):
        with connect(self.path) as db:
            row = db.execute("SELECT * FROM items WHERE id=?", (identity,)).fetchone()
            if not row:
                raise Error("not_found", "这件物品不存在。", 404)
            return dict(row)

    def mutate(self, route, data):
        with connect(self.path) as db:
            if route == "/api/locations":
                name = text(data.get("name"), 1, 80, "invalid_name", "位置名称")
                identity = uuid4().hex
                try:
                    db.execute("INSERT INTO locations VALUES (?,?)", (identity, name))
                except sqlite3.IntegrityError:
                    raise Error(
                        "already_exists", "这个位置已存在，请使用已有位置。", 409
                    ) from None
                return {"id": identity, "name": name}, 201
            if route not in ("/api/items", "/api/items/update", "/api/items/archive"):
                raise Error("not_found", "页面不存在。", 404)
            identity = data.get("id")
            existing = None
            if route != "/api/items":
                if not isinstance(identity, str):
                    raise Error("bad_request", "缺少物品编号。")
                existing = db.execute(
                    "SELECT * FROM items WHERE id=?", (identity,)
                ).fetchone()
                if not existing:
                    raise Error("not_found", "这件物品不存在。", 404)
                revision = data.get("revision")
                if route.endswith("/update") or revision is not None:
                    if (
                        isinstance(revision, bool)
                        or not isinstance(revision, (str, int))
                        or not str(revision).isdigit()
                        or len(str(revision)) > 12
                    ):
                        raise Error("bad_request", "缺少有效的版本号。")
                    if int(revision) != existing["revision"]:
                        raise Error(
                            "revision_conflict",
                            "这件物品已被另一个页面修改。原稿已保留，请打开最新记录核对后再保存。",
                            409,
                        )
            if route.endswith("/archive"):
                changed = db.execute(
                    "UPDATE items SET archived=1-archived,revision=revision+1 WHERE id=? AND revision=?",
                    (identity, existing["revision"]),
                ).rowcount
                if changed != 1:
                    raise Error(
                        "revision_conflict", "记录刚刚发生变化，请核对最新记录。", 409
                    )
                status = 200
            else:
                name = text(data.get("name"), 1, 120, "invalid_name", "物品名称")
                value = money(data.get("value"))
                notes = data.get("notes", "")
                if not isinstance(notes, str) or len(notes) > 2000:
                    raise Error("bad_request", "备注最多 2000 个字符。")
                location = data.get("location_id")
                if (
                    not isinstance(location, str)
                    or not db.execute(
                        "SELECT 1 FROM locations WHERE id=?", (location,)
                    ).fetchone()
                ):
                    raise Error("invalid_location", "请选择已存在的位置。")
                if existing:
                    # Obtain the write lock before checking revision again, preventing competing tabs from both committing.
                    changed = db.execute(
                        "UPDATE items SET name=?,location_id=?,value_minor=?,notes=?,revision=revision+1 WHERE id=? AND revision=?",
                        (name, location, value, notes, identity, existing["revision"]),
                    ).rowcount
                    if changed != 1:
                        raise Error(
                            "revision_conflict",
                            "记录刚刚发生变化，原稿已保留，请核对最新记录。",
                            409,
                        )
                    status = 200
                else:
                    identity = uuid4().hex
                    db.execute(
                        "INSERT INTO items VALUES (?,?,?,?,?,0,1)",
                        (identity, name, location, value, notes),
                    )
                    status = 201
            result = dict(
                db.execute("SELECT * FROM items WHERE id=?", (identity,)).fetchone()
            )
            result["archived"] = bool(result["archived"])
            return result, status


class Web(Handler):
    def dispatch(self, method):
        if method == "GET":
            if self.route == "/api/health":
                return self.json(200, {"status": "ok"})
            if self.route == "/api/state":
                return self.json(200, self.server.inventory.state(self.query))
            if self.route == "/":
                return self.send(200, self.home())
            if self.route == "/items/edit":
                item = self.server.inventory.get(self.query.get("id", ""))
                return self.send(200, self.editor(item))
            raise Error("not_found", "页面不存在。", 404)
        if self.route.startswith("/api/"):
            result, status = self.server.inventory.mutate(self.route, self.data)
            return self.json(status, result)
        mapping = {
            "/items/create": "/api/items",
            "/items/update": "/api/items/update",
            "/items/archive": "/api/items/archive",
            "/locations/create": "/api/locations",
        }
        if self.route not in mapping:
            raise Error("not_found", "页面不存在。", 404)
        self.server.inventory.mutate(mapping[self.route], self.data)
        return self.redirect(
            "/?"
            + urlencode(
                {
                    "saved": "1",
                    "view": self.data.get("return_view", "active"),
                    "location": self.data.get("return_location", ""),
                    "q": self.data.get("return_q", ""),
                }
            )
        )

    def error_page(self, error):
        notice = f'<div class="notice error" role="alert">{h(error.message)}</div>'
        if self.route == "/items/update":
            return self.editor(self.data, notice)
        if self.route in ("/items/create", "/locations/create", "/items/archive"):
            return self.home(
                notice,
                self.data if self.route == "/items/create" else None,
                self.data.get("name", "") if self.route == "/locations/create" else "",
            )
        return page("家物清单", "暂时无法完成", notice + '<a href="/">返回清单</a>')

    def item_form(self, data=None, editing=False):
        data = data or {}
        locations = self.server.inventory.state()["locations"]
        current = data.get("location_id", locations[0]["id"])
        choices = [(r["id"], r["name"]) for r in locations]
        if current not in [r["id"] for r in locations]:
            choices.append((current, "无效位置，请重新选择"))
        minor = data.get("value_minor", 0)
        minor = minor if isinstance(minor, int) else 0
        value = (
            data["value"]
            if "value" in data
            else (f"{minor // 100}.{minor % 100:02d}" if editing else "")
        )
        identity = (
            f'<input type="hidden" name="id" value="{h(data.get("id", ""))}"><input type="hidden" name="revision" value="{h(data.get("revision", ""))}">'
            if editing
            else ""
        )
        return f'''<form method="post" action="/items/{"update" if editing else "create"}">{identity}
        <div class="field"><label for="item-name">物品名称</label><input id="item-name" name="name" value="{h(data.get("name", ""))}" maxlength="120" required placeholder="例如：床头阅读灯"></div>
        <div class="field"><label for="item-location">所在位置</label><select id="item-location" name="location_id">{options(choices, current)}</select></div>
        <div class="field"><label for="item-value">估值（元）</label><input id="item-value" name="value" value="{h(value)}" inputmode="decimal" required placeholder="0.00"><span class="muted">每行一件 · 人民币 · 最多两位小数</span></div>
        <div class="field"><label for="item-notes">备注</label><textarea id="item-notes" name="notes" rows="4" maxlength="2000" placeholder="打包提醒、购买信息……">{h(data.get("notes", ""))}</textarea></div>
        <button class="primary" type="submit">{"保存修改" if editing else "添加物品"}</button>{' <a class="button" href="/">取消</a>' if editing else ""}
        <p class="muted">点击按钮后保存到本机。</p></form>'''

    def editor(self, data, notice=""):
        latest = (
            f'<a href="/items/edit?{urlencode({"id": data.get("id", "")})}">打开最新记录核对</a>'
            if notice
            else ""
        )
        content = f'<a href="/">← 返回清单</a><section class="panel edit-panel">{notice}<p class="muted">可修改名称、位置和估值，移动位置后清单立即更新。</p>{self.item_form(data, True)}{latest}</section>'
        return page("家物清单", "编辑物品", content)

    def home(self, notice="", draft=None, location_draft=""):
        state = self.server.inventory.state(self.query)
        query = self.query
        location = query.get("location", "")
        view = query.get("view", "active")
        q = query.get("q", "")
        names = {r["id"]: r["name"] for r in state["locations"]}
        filters = f'''<form method="get" class="inline"><div class="field"><label for="search">搜索名称或备注</label><input id="search" name="q" value="{h(q)}" placeholder="找一件物品……"></div><div class="field"><label for="location">位置</label><select id="location" name="location">{options([("", "全部位置")] + list(names.items()), location)}</select></div><div class="field"><label for="view">物品状态</label><select id="view" name="view">{options([("active", "活跃物品"), ("archive", "已归档"), ("all", "全部物品")], view)}</select></div><button type="submit">筛选</button><a class="button" href="/">重置</a></form>'''
        rows = ""
        for item in state["items"]:
            returning = "".join(
                f'<input type="hidden" name="return_{key}" value="{h(value)}">'
                for key, value in [("view", view), ("location", location), ("q", q)]
            )
            rows += f'''<article class="inventory-row"><div class="row"><div><a class="note-title" href="/items/edit?{urlencode({"id": item["id"]})}">{h(item["name"])}</a> <span class="pill">{h(names[item["location_id"]])}</span>{' <span class="pill archive">已归档</span>' if item["archived"] else ""}</div><strong class="item-amount">¥{amount(item["value_minor"])}</strong></div><div class="preview">{h(item["notes"]) if item["notes"] else "暂无备注"}</div><div class="item-actions"><a href="/items/edit?{urlencode({"id": item["id"]})}">编辑 / 调整位置</a><form method="post" action="/items/archive"><input type="hidden" name="id" value="{h(item["id"])}"><input type="hidden" name="revision" value="{item["revision"]}">{returning}<button type="submit">{"恢复到活跃清单" if item["archived"] else "归档"}</button></form></div></article>'''
        if not rows:
            rows = '<div class="empty"><strong>当前筛选下没有物品</strong><p>试试其他位置或搜索词，也可以添加第一件物品。</p></div>'
        links = "".join(
            f'<a class="{"active" if location == identity else ""}" href="/?{urlencode({"location": identity, "q": q, "view": view})}">{h(name)}</a>'
            for identity, name in [("", "全部位置")] + list(names.items())
        )
        success = (
            '<div class="notice" role="status">已保存，清单已更新。</div>'
            if query.get("saved")
            else ""
        )
        content = f'''<style>.inventory-layout{{display:grid;grid-template-columns:170px minmax(0,1fr) 305px;gap:22px;align-items:start}}.inventory-row{{border-top:1px solid var(--line);padding:20px 0}}.inventory-row:first-child{{border-top:0}}.inventory-row .preview{{margin:12px 0;line-height:1.7}}.item-actions{{display:flex;align-items:center;justify-content:space-between;gap:10px;font-size:12px}}.item-actions button{{font-size:12px;padding:5px 10px}}.item-amount{{white-space:nowrap;font-variant-numeric:tabular-nums}}.archive{{background:#eeeae0}}.edit-panel{{max-width:660px;margin:22px auto}}.intro p{{margin:0;color:var(--muted)}}.summary{{display:flex;gap:42px;margin:24px 0 12px}}.summary strong{{font-size:29px;display:block;line-height:1.4}}.summary small{{color:var(--muted)}}.sidebar h2{{font-size:13px;color:var(--muted);padding-left:12px}}@media(max-width:1100px){{.inventory-layout{{grid-template-columns:150px minmax(0,1fr)}}.add-panel{{grid-column:2}}}}@media(max-width:650px){{.inventory-layout{{display:block}}.sidebar{{margin-bottom:16px}}.sidebar h2{{display:none}}.item-actions{{flex-wrap:wrap}}.row{{align-items:start}}.summary{{gap:24px}}}}</style>
        <p class="muted" style="margin-top:-12px;margin-bottom:24px">搬家前，给每一件物品找到位置。</p>{notice}{success}<div class="inventory-layout"><aside class="sidebar"><h2>我的位置 · {len(names)}</h2>{links}<div class="panel" style="padding:12px;margin-top:20px"><form method="post" action="/locations/create"><label for="new-location">添加位置</label><input id="new-location" name="name" maxlength="80" required value="{h(location_draft)}" placeholder="例如：书房"><button style="margin-top:10px;width:100%">创建位置</button></form></div></aside>
        <section class="panel"><h2>物品清单</h2>{filters}<div class="summary"><div><small>当前列表 · 物品数量</small><strong>{state["summary"]["count"]} <span class="muted">件</span></strong></div><div><small>当前列表 · 总估值</small><strong>¥{amount(state["summary"]["total_minor"])}</strong></div></div>{rows}</section><aside class="panel add-panel"><h2>记下一件物品</h2>{self.item_form(draft)}</aside></div>'''
        return page("家物清单", "让搬家，心中有数。", content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=5276)
    parser.add_argument("--data-dir", type=Path, default=ROOT / "data")
    parser.add_argument(
        "--demo", action="store_true", help="Only seed a newly initialized database"
    )
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Web)
    server.inventory = Inventory(args.data_dir, args.demo)
    print(
        f"家物清单 http://127.0.0.1:{args.port} · {args.data_dir.resolve()}", flush=True
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
