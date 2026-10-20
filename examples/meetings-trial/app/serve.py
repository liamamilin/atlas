#!/usr/bin/env python3
"""Local project meeting notes; preserve plaintext, search and reversible lifecycle."""

import argparse
from http.server import ThreadingHTTPServer
from pathlib import Path
import re
import time
from urllib.parse import urlencode
import uuid
from web_support import Error, Handler, connect, h, options, page


def name(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80:
        raise Error("invalid_name", "项目名称不能为空，且不能超过80个字符。")
    return value.strip()


def content(data):
    body = data.get("body")
    title = data.get("title", "")
    if not isinstance(body, str) or not body.strip() or len(body) > 100000:
        raise Error(
            "invalid_body", "正文不能为空，最多100000个字符。请保留原文后再修正。"
        )
    if not isinstance(title, str) or len(title) > 120:
        raise Error("invalid_title", "标题最多120个字符。")
    return title.strip() or body.strip().splitlines()[0][:80], body


def hidden(key, value):
    return f'<input type="hidden" name="{h(key)}" value="{h(value)}">'


class Notebook:
    def __init__(self, directory, demo=False):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "meetings.sqlite3"
        with connect(self.path) as db:
            db.executescript("""CREATE TABLE IF NOT EXISTS meta(version INTEGER);
            CREATE TABLE IF NOT EXISTS projects(id TEXT PRIMARY KEY,name TEXT NOT NULL UNIQUE COLLATE NOCASE,created_at INTEGER NOT NULL,is_default INTEGER NOT NULL DEFAULT 0);
            CREATE TABLE IF NOT EXISTS notes(id TEXT PRIMARY KEY,title TEXT NOT NULL,body TEXT NOT NULL,project_id TEXT NOT NULL REFERENCES projects(id),pinned INTEGER NOT NULL DEFAULT 0,archived INTEGER NOT NULL DEFAULT 0,trashed_at INTEGER,revision INTEGER NOT NULL,created_at INTEGER NOT NULL,updated_at INTEGER NOT NULL);
            CREATE INDEX IF NOT EXISTS notes_project ON notes(project_id);""")
            if not db.execute("SELECT 1 FROM meta").fetchone():
                db.execute(
                    "INSERT INTO projects VALUES(?,?,?,1)",
                    (uuid.uuid4().hex, "收件箱", time.time_ns()),
                )
                db.execute("INSERT INTO meta VALUES(1)")
                if demo:
                    project, _ = self.change(db, "/projects", {"name": "[演示] 新产品"})
                    self.change(
                        db,
                        "/notes",
                        {
                            "title": "[演示] 先记下来，之后再整理",
                            "body": "结论：用一个地方留存每次会议的决定。\n行动：会后补充负责人和截止日期。\n\n这是一条演示笔记，可以移入回收站并恢复。",
                            "project_id": project["id"],
                        },
                    )

    @staticmethod
    def project(db, identifier=None):
        row = (
            db.execute("SELECT * FROM projects WHERE is_default=1").fetchone()
            if identifier is None
            else db.execute(
                "SELECT * FROM projects WHERE id=?", (identifier,)
            ).fetchone()
        )
        if row is None:
            raise Error("invalid_project", "请选择一个已有项目。")
        return row

    @staticmethod
    def note(db, identifier):
        row = db.execute(
            "SELECT n.*,p.name AS project_name FROM notes n JOIN projects p ON n.project_id=p.id WHERE n.id=?",
            (identifier,),
        ).fetchone()
        if row is None:
            raise Error("not_found", "这条笔记不存在。", 404)
        return dict(row)

    @staticmethod
    def projects(db):
        return [
            dict(row)
            for row in db.execute(
                "SELECT p.*,COUNT(n.id) AS count FROM projects p LEFT JOIN notes n ON n.project_id=p.id AND n.archived=0 AND n.trashed_at IS NULL GROUP BY p.id ORDER BY p.is_default DESC,p.created_at,p.id"
            )
        ]

    def state(self, db, query):
        project = query.get("project", "")
        q = query.get("q", "")
        view = query.get("view", "active")
        sort = query.get("sort", "updated")
        if view not in ("active", "archive", "trash") or sort not in (
            "updated",
            "title",
        ):
            raise Error("bad_request", "请选择已有的视图或排序。")
        rows = [
            dict(row)
            for row in db.execute(
                "SELECT n.*,p.name AS project_name FROM notes n JOIN projects p ON p.id=n.project_id"
            )
        ]
        notes = [
            n
            for n in rows
            if (not project or n["project_id"] == project)
            and (
                (n["trashed_at"] is not None)
                if view == "trash"
                else (n["trashed_at"] is None)
            )
            and (view != "archive" or n["archived"])
            and (view != "active" or bool(q) or not n["archived"])
            and (
                not q
                or q.casefold() in n["title"].casefold()
                or q.casefold() in n["body"].casefold()
            )
        ]
        notes.sort(
            key=lambda n: (
                -n["pinned"],
                n["title"].casefold() if sort == "title" else -n["updated_at"],
                n["id"],
            )
        )
        return {
            "projects": self.projects(db),
            "notes": notes,
            "project": project,
            "q": q,
            "view": view,
            "sort": sort,
        }

    def change(self, db, action, data):
        if action == "/projects":
            n = name(data.get("name"))
            if db.execute(
                "SELECT 1 FROM projects WHERE name=? COLLATE NOCASE", (n,)
            ).fetchone():
                raise Error("already_exists", "已有这个项目，请换一个名称。", 409)
            identifier = uuid.uuid4().hex
            db.execute(
                "INSERT INTO projects VALUES(?,?,?,0)", (identifier, n, time.time_ns())
            )
            return {"id": identifier, "name": n}, 201
        if action == "/notes":
            title, body = content(data)
            project = self.project(db, data.get("project_id"))
            identifier = uuid.uuid4().hex
            at = time.time_ns()
            db.execute(
                "INSERT INTO notes VALUES(?,?,?,?,0,0,NULL,1,?,?)",
                (identifier, title, body, project["id"], at, at),
            )
            return self.note(db, identifier), 201
        row = self.note(db, data.get("id"))
        if action not in (
            "/notes/update",
            "/notes/move",
            "/notes/pin",
            "/notes/archive",
            "/notes/trash",
            "/notes/restore",
        ):
            raise Error("not_found", "操作不存在。", 404)
        if row["trashed_at"] is not None and action != "/notes/restore":
            raise Error("bad_request", "笔记在回收站中，请先恢复再修改。")
        if action == "/notes/update":
            title, body = content(data)
            project = self.project(db, data.get("project_id"))
            try:
                revision = int(data.get("revision"))
                if str(revision) != str(data.get("revision")):
                    raise ValueError()
            except (TypeError, ValueError):
                raise Error(
                    "bad_request", "缺少有效笔记版本，请重新打开编辑页。"
                ) from None
            if revision != row["revision"]:
                raise Error(
                    "revision_conflict",
                    "笔记已有更新。你的草稿已保留，页面已载入最新版本号；请先核对，再次保存会替换当前内容。",
                    409,
                )
            db.execute(
                "UPDATE notes SET title=?,body=?,project_id=? WHERE id=?",
                (title, body, project["id"], row["id"]),
            )
        elif action == "/notes/move":
            project = self.project(db, data.get("project_id"))
            db.execute(
                "UPDATE notes SET project_id=? WHERE id=?", (project["id"], row["id"])
            )
        elif action in ("/notes/pin", "/notes/archive"):
            column = "pinned" if action == "/notes/pin" else "archived"
            db.execute(
                f"UPDATE notes SET {column}=? WHERE id=?", (1 - row[column], row["id"])
            )
        elif action == "/notes/trash":
            db.execute(
                "UPDATE notes SET trashed_at=? WHERE id=?", (time.time_ns(), row["id"])
            )
        elif action == "/notes/restore":
            db.execute("UPDATE notes SET trashed_at=NULL WHERE id=?", (row["id"],))
        db.execute(
            "UPDATE notes SET revision=revision+1,updated_at=? WHERE id=?",
            (time.time_ns(), row["id"]),
        )
        return self.note(db, row["id"]), 200


class Web(Handler):
    def dispatch(self, method):
        lib = self.server.library
        with connect(lib.path) as db:
            if method == "GET":
                if self.route == "/api/health":
                    return self.json(200, {"ready": True, "origin": "assisted-trial"})
                if self.route == "/api/state":
                    return self.json(200, lib.state(db, self.query))
                if re.fullmatch(r"/api/notes/[a-f0-9]+", self.route):
                    return self.json(200, lib.note(db, self.route.split("/")[-1]))
                if self.route == "/":
                    return self.send(200, self.home(db))
                match = re.fullmatch(r"/note/([a-f0-9]+)(/edit)?", self.route)
                if match:
                    row = lib.note(db, match[1])
                    return self.send(
                        200, self.editor(db, row) if match[2] else self.detail(db, row)
                    )
            if method == "POST":
                db.execute("BEGIN IMMEDIATE")
                result, status = lib.change(
                    db, self.route.removeprefix("/api"), self.data
                )
                db.commit()
                if self.route.startswith("/api/"):
                    return self.json(status, result)
                if self.route == "/projects":
                    return self.redirect(
                        "/?" + urlencode({"project": result["id"], "saved": "1"})
                    )
                if self.route == "/notes/trash":
                    return self.redirect("/?view=trash&saved=1")
                return self.redirect("/note/" + result["id"] + "?saved=1")
            raise Error("not_found", "页面不存在。", 404)

    def error_page(self, error):
        with connect(self.server.library.path) as db:
            if self.route == "/notes/update":
                try:
                    return self.editor(
                        db,
                        self.server.library.note(db, self.data.get("id")),
                        error,
                        self.data,
                    )
                except Error:
                    pass
            return self.home(db, error, self.data)

    @staticmethod
    def message(error=None, saved=False):
        if error:
            return f'<p class="notice error" role="alert">{h(error.message)} ({h(error.code)})</p>'
        return '<p class="notice" role="status">已保存到本机。</p>' if saved else ""

    def form(self, projects, row=None, values=None):
        row = row or {}
        values = values or {}
        pid = values.get("project_id", row.get("project_id", projects[0]["id"]))
        identifier = row.get("id", "")
        title = values.get("title", row.get("title", ""))
        body = values.get("body", row.get("body", ""))
        editing = bool(identifier)
        prefix = "edit" if editing else "capture"
        return f'''<form action="{"/notes/update" if editing else "/notes"}" method="post" data-testid="{"note-edit-form" if editing else "note-create-form"}" novalidate>{hidden("id", identifier)}{hidden("revision", row.get("revision", ""))}<div class="field"><label for="{prefix}-title">标题（可选）</label><input id="{prefix}-title" name="title" value="{h(title)}" placeholder="例如：发布评审结论"></div><div class="field"><label for="{prefix}-body">正文 *</label><textarea id="{prefix}-body" name="body" rows="{"16" if editing else "8"}" placeholder="结论、行动项、负责人…">{h(body)}</textarea></div><div class="field"><label for="{prefix}-project">存入项目</label><select id="{prefix}-project" name="project_id">{options([(p["id"], p["name"]) for p in projects], pid)}</select></div><p class="muted">点击保存才写入本机；支持多行文字和 Markdown 表格原文。</p><button class="primary">{"保存修改" if editing else "保存笔记"}</button></form>'''

    def editor(self, db, row, error=None, values=None):
        if row["trashed_at"] is not None:
            return self.detail(db, row)
        return page(
            "会后 · 项目笔记",
            "把会议结论补充完整。",
            f'<a href="/note/{row["id"]}">← 返回笔记</a>{self.message(error)}<section class="panel" style="max-width:850px;margin-top:18px">{self.form(self.server.library.projects(db), row, values)}</section>',
        )

    def detail(self, db, row):
        controls = ""
        projects = self.server.library.projects(db)
        if row["trashed_at"] is not None:
            controls = f'<form action="/notes/restore" method="post">{hidden("id", row["id"])}<button class="primary">恢复笔记</button></form><p class="muted">保留原项目、正文和归档/置顶状态，不自动过期。</p>'
        else:
            controls = (
                f'<a class="button primary" href="/note/{row["id"]}/edit">编辑正文</a>'
            )
            for action, label in [
                ("pin", "取消置顶" if row["pinned"] else "置顶笔记"),
                ("archive", "取消归档" if row["archived"] else "归档笔记"),
                ("trash", "移入回收站"),
            ]:
                controls += f'<form action="/notes/{action}" method="post">{hidden("id", row["id"])}<button>{label}</button></form>'
            controls += f'<form class="inline" action="/notes/move" method="post">{hidden("id", row["id"])}<div class="field"><label for="move-project">移动到项目</label><select id="move-project" name="project_id">{options([(p["id"], p["name"]) for p in projects], row["project_id"])}</select></div><button>移动笔记</button></form>'
        status = (
            "回收站"
            if row["trashed_at"] is not None
            else "已归档"
            if row["archived"]
            else "活跃笔记"
        )
        return page(
            "会后 · 项目笔记",
            row["title"],
            f"""<a href="/">← 返回笔记库</a>{self.message(saved=bool(self.query.get("saved")))}<section class="panel" style="margin-top:18px"><div class="row"><span>{h(row["project_name"])} · <span class="pill">{status}</span>{'<span class="pill">置顶</span>' if row["pinned"] else ""}</span><span class="muted">版本 {row["revision"]}</span></div><div class="body-text" data-testid="note-body">{h(row["body"])}</div><div class="inline">{controls}</div></section>""",
        )

    def home(self, db, error=None, values=None):
        values = values or {}
        lib = self.server.library
        try:
            s = lib.state(db, self.query)
        except Error:
            s = lib.state(db, {})
        projects = s["projects"]
        side = '<a href="/">全部活跃笔记</a>'
        for p in projects:
            side += f'<a class="{"active" if s["project"] == p["id"] else ""}" href="/?{h(urlencode({"project": p["id"]}))}">{h(p["name"])} <small>({p["count"]})</small></a>'
        side += '<hr style="border:0;border-top:1px solid var(--line);margin:18px 0"><a href="/?view=archive">已归档</a><a href="/?view=trash">回收站</a>'
        cards = ""
        for n in s["notes"]:
            tags = ('<span class="pill">置顶</span> ' if n["pinned"] else "") + (
                '<span class="pill">已归档</span>' if n["archived"] else ""
            )
            cards += f'<a class="note-card" data-testid="note-row" data-id="{n["id"]}" href="/note/{n["id"]}"><span class="muted">{h(n["project_name"])} · {tags}</span><div class="note-title">{h(n["title"])}</div><p class="preview">{h(n["body"][:160])}</p></a>'
        filters = options(
            [("", "全部项目")] + [(p["id"], p["name"]) for p in projects], s["project"]
        )
        content = f'''<p class="muted">先记下，再按项目整理；需要时，连归档一起找回来。</p>{self.message(error, bool(self.query.get("saved")))}<div class="notes-layout"><nav class="sidebar" aria-label="项目笔记本">{side}</nav><section><form method="get" action="/" data-testid="search-form"><div class="field"><label for="q">搜索标题与正文（包含归档）</label><input id="q" name="q" value="{h(s["q"])}" placeholder="输入一个决定、行动项或关键词"></div><div class="inline"><div class="field"><label for="filter-project">项目范围</label><select id="filter-project" name="project">{filters}</select></div><div class="field"><label for="view">视图</label><select id="view" name="view">{options([("active", "活跃 / 搜索"), ("archive", "已归档"), ("trash", "回收站")], s["view"])}</select></div><div class="field"><label for="sort">排序（置顶始终在前）</label><select id="sort" name="sort">{options([("updated", "最近更新"), ("title", "标题")], s["sort"])}</select></div><button>搜索 / 筛选</button></div></form><p class="muted">{len(s["notes"])} 条笔记 · {"全库关键词含归档" if s["q"] and s["view"] == "active" else {"active": "活跃视图", "archive": "归档视图", "trash": "可恢复的回收站"}[s["view"]]}</p>{cards or '<p class="empty" data-testid="empty-state">没有匹配的笔记。试试其他关键词、项目范围，或新建一条会议记录。</p>'}</section>
        <aside class="quick"><section class="panel"><h2>＋ 快速记录</h2>{self.form(projects, values=values)}</section><section class="panel"><h2>新建项目笔记本</h2><form method="post" action="/projects"><div class="field"><label for="project-name">项目名称</label><input id="project-name" name="name" value="{h(values.get("name", ""))}" placeholder="例如：产品发布"></div><button>创建项目</button></form></section></aside></div>'''
        return page("会后 · 项目笔记", "决定有归处，回查有线索。", content)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--port", type=int, default=5275)
    p.add_argument("--host", default="127.0.0.1", choices=["127.0.0.1", "localhost"])
    p.add_argument(
        "--data-dir", type=Path, default=Path(__file__).resolve().parents[1] / "data"
    )
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    lib = Notebook(args.data_dir.resolve(), args.demo)
    with ThreadingHTTPServer((args.host, args.port), Web) as server:
        server.library = lib
        print(f"会后 http://{args.host}:{args.port}/ · {lib.path}", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
