#!/usr/bin/env python3
# 本地生活待购与灵感收藏夹：Python 标准库 + SQLite。
import argparse, html, os, sqlite3, sys
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlencode, urlsplit

APP_NAME = '拾光夹'
DB_NAME = 'library.sqlite3'
MAX_BODY = 200000
CSP = '''default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'; '''

SCHEMA = '''
PRAGMA journal_mode = WAL;
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL COLLATE NOCASE UNIQUE,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS bookmarks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT NOT NULL,
  title TEXT NOT NULL,
  note TEXT NOT NULL DEFAULT '',
  category_id INTEGER NOT NULL REFERENCES categories(id),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS settings (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookmarks_category ON bookmarks(category_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_updated ON bookmarks(updated_at);
'''

BASE = '''<!doctype html>
<html lang=zh-CN>
<head>
<meta charset=utf-8>
<meta name=viewport content='width=device-width, initial-scale=1'>
<meta name=color-scheme content=light>
<title>__TITLE__ · 拾光夹</title>
<style>
:root { --paper:#f5f0e6; --card:#fffdf8; --ink:#2e2a24; --muted:#7c7468; --line:#ddd3c2; --accent:#a24e2d; --accent-dark:#7f3a20; }
* { box-sizing:border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif; line-height:1.65; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
h1,h2,h3 { margin:0; font-family:'Songti SC','STSong','Noto Serif SC',serif; line-height:1.3; }
.wrap { width:100%; max-width:1180px; margin:0 auto; padding:0 24px; }
.topbar { border-bottom:1px solid var(--line); background:rgba(255,253,248,.72); }
.bar { min-height:78px; display:flex; align-items:baseline; gap:18px; }
.brand { color:var(--ink); font-family:'Songti SC','STSong',serif; font-size:29px; font-weight:700; letter-spacing:.12em; }
.brand:hover { text-decoration:none; }
.tagline { margin:0; color:var(--muted); font-size:13px; letter-spacing:.06em; }
.layout { display:grid; grid-template-columns:250px minmax(0,1fr); gap:36px; padding-top:30px; padding-bottom:70px; }
.sidebar { align-self:start; position:sticky; top:20px; }
.side-title { display:flex; justify-content:space-between; align-items:baseline; padding-bottom:8px; border-bottom:2px solid var(--ink); font-weight:600; }
.side-total { color:var(--muted); font-size:12px; font-weight:400; }
.cat-nav { display:flex; flex-direction:column; gap:3px; margin:10px 0 22px; }
.cat { display:flex; justify-content:space-between; align-items:center; gap:8px; padding:8px 10px; border-radius:8px; color:var(--ink); }
.cat:hover { background:#ebe3d5; text-decoration:none; }
.cat[data-active] { background:var(--ink); color:#fffdf8; }
.cat b { font-size:12px; font-weight:500; color:var(--muted); }
.cat[data-active] b { color:#d9cfbf; }
.default-tag { margin-left:6px; padding:1px 5px; border:1px solid currentColor; border-radius:4px; font-size:10px; font-style:normal; opacity:.7; }
.new-cat { margin-top:14px; }
.new-cat label { display:block; margin-bottom:6px; font-size:12px; color:var(--muted); }
.inline { display:flex; gap:6px; }
.inline input { min-width:0; }
button, input, select, textarea { font:inherit; }
input, select, textarea { width:100%; border:1px solid var(--line); border-radius:8px; background:#fffefb; color:var(--ink); padding:9px 11px; }
textarea { resize:vertical; }
input:focus, select:focus, textarea:focus { outline:2px solid rgba(161,78,45,.25); border-color:var(--accent); }
button { border:0; border-radius:8px; padding:9px 14px; background:var(--ink); color:#fffdf8; cursor:pointer; }
button:hover { background:#17140f; }
button.primary { background:var(--accent); }
button.primary:hover { background:var(--accent-dark); }
button.small, button.mini { padding:6px 10px; font-size:12px; background:#ece4d6; color:var(--ink); }
button.mini:hover { background:#ddd2bf; }
button.danger { background:transparent; border:1px solid #dbb6ab; color:#9a3321; }
button.danger:hover { background:#f7e9e5; }
.manager { margin-top:18px; padding-top:12px; border-top:1px dashed var(--line); font-size:12px; }
.manager summary { cursor:pointer; color:var(--muted); }
.manager-body { margin-top:10px; display:flex; flex-direction:column; gap:10px; }
.manager-row { padding-bottom:10px; border-bottom:1px solid #eee6d9; }
.manager-name { display:block; margin-bottom:5px; font-weight:600; color:var(--ink); }
.rename-form { display:flex; gap:5px; margin-bottom:5px; }
.rename-form input { padding:5px 7px; font-size:12px; }
.manager-tip, .side-note { color:var(--muted); line-height:1.55; }
.side-note { margin-top:14px; font-size:11px; }
.page-head { display:flex; justify-content:space-between; align-items:flex-end; gap:20px; margin-bottom:18px; }
.eyebrow { margin:0 0 4px; color:var(--accent); font-size:12px; letter-spacing:.12em; }
.page-head h1 { font-size:30px; }
.result-line { margin:4px 0 0; color:var(--muted); font-size:13px; }
.search-form { display:flex; gap:8px; align-items:center; margin-bottom:18px; }
.search-form input[type=search] { flex:1; }
.clear { flex:0 0 auto; font-size:13px; }
.add-panel { margin-bottom:26px; padding:20px; border:1px solid var(--line); border-top:3px solid var(--accent); border-radius:12px; background:var(--card); box-shadow:0 4px 18px rgba(46,42,36,.04); }
.add-panel h2 { font-size:21px; }
.hint { margin:4px 0 14px; color:var(--muted); font-size:13px; }
.add-grid { display:grid; grid-template-columns:minmax(0,1fr) 220px; gap:12px; }
.add-grid .wide { grid-column:1 / -1; }
.add-grid label, .edit-form label { font-size:12px; color:var(--muted); }
.add-grid input, .add-grid select, .add-grid textarea, .edit-form input, .edit-form select, .edit-form textarea { margin-top:4px; }
.add-form > button { margin-top:14px; }
.cards { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; }
.card { display:flex; flex-direction:column; min-width:0; padding:18px; border:1px solid var(--line); border-radius:12px; background:var(--card); }
.card-meta { display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px; }
.chip { display:inline-block; padding:2px 8px; border-radius:999px; background:#efe7d8; color:#69573f; font-size:11px; }
.chip:hover { text-decoration:none; background:#e4d8c4; }
.card-meta time { color:var(--muted); font-size:11px; white-space:nowrap; }
.card-title { font-size:19px; overflow-wrap:anywhere; }
.card-url { margin:6px 0 10px; color:var(--muted); font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11px; overflow-wrap:anywhere; }
.note { margin:0 0 12px; padding:9px 11px; border-left:2px solid #cbbda6; background:#faf6ed; color:#514a40; font-size:13px; white-space:pre-wrap; overflow-wrap:anywhere; }
.card-actions { display:flex; flex-wrap:wrap; align-items:center; gap:8px; margin-top:auto; }
.open-btn { display:inline-block; padding:8px 12px; border-radius:8px; background:var(--accent); color:#fffdf8; font-size:13px; }
.open-btn:hover { background:var(--accent-dark); text-decoration:none; }
.move-form { display:flex; flex:1 1 160px; gap:5px; min-width:0; }
.move-form select { padding:6px 8px; font-size:12px; }
.move-btn { flex:0 0 auto; }
.edit-box { margin-top:10px; padding-top:9px; border-top:1px dashed var(--line); }
.edit-box summary { cursor:pointer; color:var(--muted); font-size:12px; }
.edit-form { display:flex; flex-direction:column; gap:9px; margin-top:10px; }
.edit-form button.danger { margin-top:6px; }
.empty { padding:42px 24px; border:1px dashed var(--line); border-radius:12px; text-align:center; color:var(--muted); }
.empty h2 { margin-bottom:6px; color:var(--ink); font-size:20px; }
.empty p { margin:4px 0; }
.notice-ok, .notice-error { margin-bottom:18px; padding:11px 14px; border-radius:9px; font-size:13px; }
.notice-ok { background:#eaf0e6; border:1px solid #cbdac2; color:#3f5a36; }
.notice-error { background:#f8e9e5; border:1px solid #e4c3ba; color:#85321f; }
.foot { padding-top:18px; padding-bottom:36px; border-top:1px solid var(--line); color:var(--muted); font-size:12px; }
.sr-only { position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0; }
@media (max-width: 900px) { .layout { grid-template-columns:1fr; gap:22px; padding-top:20px; } .sidebar { position:static; } .cards { grid-template-columns:1fr; } .add-grid { grid-template-columns:1fr; } .tagline { display:none; } .bar { min-height:64px; } }
</style>
</head>
<body>
<header class=topbar><div class='wrap bar'><a class=brand href='/'>拾光夹</a><p class=tagline>生活待购与灵感收藏夹 · 只在本机保存</p></div></header>
<main class='wrap layout'>
__SIDEBAR__
<div class=content>
__NOTICE__
__CONTENT__
</div>
</main>
<footer class='wrap foot'>所有记录保存在本机；关闭页面后再次打开仍可继续整理。</footer>
</body>
</html>'''

def now_text():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def clean(value, limit):
    value = (value or '').strip()
    return value[:limit]

def connect(path):
    con = sqlite3.connect(path, timeout=10)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA foreign_keys = ON')
    con.execute('PRAGMA busy_timeout = 10000')
    return con

def init_db(path):
    con = connect(path)
    try:
        con.executescript(SCHEMA)
        if con.execute('SELECT COUNT(*) FROM categories').fetchone()[0] == 0:
            for name in ('待购', '家居改造', '以后看看'):
                con.execute('INSERT INTO categories (name, created_at) VALUES (?, ?)', (name, now_text()))
        con.commit()
        default_category_id(con)
    finally:
        con.close()

def default_category_id(con):
    row = con.execute('SELECT value FROM settings WHERE key = ?', ('default_category_id',)).fetchone()
    if row is not None:
        try:
            cid = int(row['value'])
        except (TypeError, ValueError):
            cid = 0
        if con.execute('SELECT 1 FROM categories WHERE id = ?', (cid,)).fetchone() is not None:
            return cid
    first = con.execute('SELECT id FROM categories ORDER BY id LIMIT 1').fetchone()
    if first is None:
        cur = con.execute('INSERT INTO categories (name, created_at) VALUES (?, ?)', ('待购', now_text()))
        cid = cur.lastrowid
    else:
        cid = first['id']
    con.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', ('default_category_id', str(cid)))
    con.commit()
    return cid

def normalize_url(raw):
    raw = clean(raw, 2048)
    if not raw:
        return None, '请填写网页链接。'
    if any(ch.isspace() for ch in raw):
        return None, '链接中不能包含空格或换行。'
    if '://' not in raw:
        raw = 'https://' + raw
    try:
        parts = urlsplit(raw)
        host = parts.hostname
    except ValueError:
        return None, '链接格式无法识别。'
    if parts.scheme.lower() not in ('http', 'https'):
        return None, '只支持 http 或 https 网页链接。'
    if not host:
        return None, '链接缺少有效的网站地址。'
    return raw, None

def title_from_url(url):
    try:
        parts = urlsplit(url)
        host = parts.hostname or '未命名网页'
        path = parts.path.strip('/')
        name = host + ('/' + path if path else '')
    except ValueError:
        name = url
    return clean(name, 160)

def safe_return(value):
    value = clean(value, 1000)
    if not value.startswith('/'):
        return '/'
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or parts.path != '/':
        return '/'
    qs = parse_qs(parts.query, keep_blank_values=True)
    keep = {}
    if qs.get('category'):
        cat = clean(qs['category'][-1], 20)
        if cat:
            keep['category'] = cat
    if qs.get('q'):
        keyword = clean(qs['q'][-1], 80)
        if keyword:
            keep['q'] = keyword
    query = urlencode(keep)
    return '/' + ('?' + query if query else '')

def home_url(category='all', q=''):
    params = {}
    if category and category != 'all':
        params['category'] = category
    if q:
        params['q'] = q
    return '/' + ('?' + urlencode(params) if params else '')

def get_categories(con):
    return con.execute('''SELECT c.id, c.name, COUNT(b.id) AS total FROM categories c LEFT JOIN bookmarks b ON b.category_id = c.id GROUP BY c.id, c.name ORDER BY c.id''').fetchall()

def category_options(cats, selected):
    parts = []
    for c in cats:
        cid = c['id']
        name = c['name']
        mark = ' selected' if str(cid) == str(selected) else ''
        parts.append('<option value=%d%s>%s</option>' % (cid, mark, escape(name)))
    return ''.join(parts)

def parse_category(con, value):
    value = (value or '').strip()
    if not value or value == 'default':
        return default_category_id(con)
    try:
        cid = int(value)
    except ValueError:
        return None
    if con.execute('SELECT 1 FROM categories WHERE id = ?', (cid,)).fetchone() is None:
        return None
    return cid

def page(title, content, sidebar='<aside class=sidebar></aside>', notice='', kind='ok'):
    if notice:
        cls = 'notice-error' if kind == 'error' else 'notice-ok'
        notice_html = '<div class=%s role=status>%s</div>' % (cls, escape(notice))
    else:
        notice_html = ''
    return BASE.replace('__TITLE__', escape(title)).replace('__SIDEBAR__', sidebar).replace('__NOTICE__', notice_html).replace('__CONTENT__', content)

def error_page(message='请稍后重试。'):
    content = '<section class=empty><h1>暂时无法完成操作</h1><p>%s</p><p><a href=/>返回收藏夹</a></p></section>' % escape(message)
    return page('出错了', content)

def render_sidebar(cats, total, active, ret, default_id):
    parts = ['<aside class=sidebar>']
    parts.append('<div class=side-title><span>我的归类</span><span class=side-total>%d 条</span></div>' % total)
    parts.append('<nav class=cat-nav>')
    all_mark = ' data-active=1' if active == 'all' else ''
    parts.append(f'''<a class=cat{all_mark} href='/'><span>全部收藏</span><b>{total}</b></a>''')
    for c in cats:
        cid = c['id']
        name = c['name']
        count = c['total']
        mark = ' data-active=1' if str(cid) == active else ''
        tag = '<em class=default-tag>默认</em>' if cid == default_id else ''
        link = home_url(str(cid))
        parts.append(f'''<a class=cat{mark} href='{link}'><span>{escape(name)}{tag}</span><b>{count}</b></a>''')
    parts.append('</nav>')
    ret_attr = escape(ret)
    parts.append(f'''<form method=post action=/categories/add class=new-cat>
<input type=hidden name=return_to value='{ret_attr}'>
<label for=new-cat-name>新建归类</label>
<div class=inline><input id=new-cat-name name=name maxlength=24 required placeholder='例如：露营装备'><button class=small>添加</button></div>
</form>''')
    parts.append('<details class=manager><summary>管理归类</summary><div class=manager-body>')
    for c in cats:
        cid = c['id']
        name = c['name']
        name_attr = escape(name)
        parts.append(f'''<div class=manager-row>
<span class=manager-name>{escape(name)}</span>
<form method=post action='/categories/{cid}/rename' class=rename-form>
<input type=hidden name=return_to value='{ret_attr}'>
<input name=name value='{name_attr}' maxlength=24 required aria-label='归类新名称'>
<button class=mini>改名</button>
</form>
<form method=post action='/categories/{cid}/delete' onsubmit='return confirm(&quot;删除这个归类后，其中记录会移到其他归类。确定删除？&quot;)'>
<input type=hidden name=return_to value='{ret_attr}'>
<button class='mini danger'>删除</button>
</form>
</div>''')
    parts.append('<p class=manager-tip>删除归类不会删除收藏，其中的记录会迁移到默认归类；最后一个归类不能删除。</p>')
    parts.append('</div></details>')
    parts.append('<p class=side-note>默认归类用于接收没有指定归类的链接。</p>')
    parts.append('</aside>')
    return ''.join(parts)

def render_cards(rows, cats, ret):
    cards = []
    ret_attr = escape(ret)
    for b in rows:
        bid = b['id']
        url = b['url']
        title = b['title']
        note = b['note']
        cid = b['category_id']
        category_name = b['category_name']
        created = b['created_at']
        updated = b['updated_at']
        options = category_options(cats, cid)
        if note:
            note_html = '<p class=note>%s</p>' % escape(note)
        else:
            note_html = ''
        update_meta = '' if updated == created else ' · 更新于 ' + escape(updated)
        cards.append(f'''<article class=card>
<div class=card-meta><a class=chip href='{home_url(str(cid))}'>{escape(category_name)}</a><time>{escape(created)}{update_meta}</time></div>
<h2 class=card-title><a href='{escape(url)}' target=_blank rel='noopener noreferrer'>{escape(title)}</a></h2>
<p class=card-url>{escape(url)}</p>
{note_html}
<div class=card-actions>
<a class=open-btn href='{escape(url)}' target=_blank rel='noopener noreferrer'>打开原网页 ↗</a>
<form method=post action='/bookmarks/{bid}/move' class=move-form>
<input type=hidden name=return_to value='{ret_attr}'>
<select name=category_id aria-label='选择新的归类'>{options}</select>
<button class='mini move-btn'>移动</button>
</form>
</div>
<details class=edit-box>
<summary>编辑标题、备注或归类</summary>
<form method=post action='/bookmarks/{bid}/edit' class=edit-form>
<input type=hidden name=return_to value='{ret_attr}'>
<label>标题<input name=title maxlength=160 value='{escape(title)}'></label>
<label>备注<textarea name=note rows=3 maxlength=2000 placeholder='补充一点背景，方便以后看懂'>{escape(note)}</textarea></label>
<label>归类<select name=category_id>{options}</select></label>
<button class=primary>保存修改</button>
</form>
<form method=post action='/bookmarks/{bid}/delete' onsubmit='return confirm(&quot;确定永久删除这条收藏？此操作无法撤销。&quot;)'>
<input type=hidden name=return_to value='{ret_attr}'>
<button class='mini danger'>永久删除</button>
</form>
</details>
</article>''')
    return ''.join(cards)

def render_home(db_path, params):
    q = clean(params.get('q', [''])[0], 80)
    raw_cat = params.get('category', [''])[0]
    notice = clean(params.get('notice', [''])[0], 300)
    kind = 'error' if params.get('kind', [''])[0] == 'error' else 'ok'
    con = connect(db_path)
    try:
        cats = get_categories(con)
        total = con.execute('SELECT COUNT(*) FROM bookmarks').fetchone()[0]
        default_id = default_category_id(con)
        cat = 'all'
        current = '全部收藏'
        if raw_cat and raw_cat != 'all':
            try:
                wanted = int(raw_cat)
            except ValueError:
                wanted = 0
            found = con.execute('SELECT id, name FROM categories WHERE id = ?', (wanted,)).fetchone()
            if found is not None:
                cat = str(found['id'])
                current = found['name']
        clauses = []
        args = []
        if cat != 'all':
            clauses.append('b.category_id = ?')
            args.append(int(cat))
        if q:
            clauses.append('(b.title LIKE ? OR b.url LIKE ? OR b.note LIKE ?)')
            term = '%' + q + '%'
            args.extend([term, term, term])
        sql = '''SELECT b.id, b.url, b.title, b.note, b.category_id, b.created_at, b.updated_at, c.name AS category_name FROM bookmarks b JOIN categories c ON c.id = b.category_id'''
        if clauses:
            sql += ' WHERE ' + ' AND '.join(clauses)
        sql += ' ORDER BY b.updated_at DESC, b.id DESC'
        rows = con.execute(sql, args).fetchall()
    finally:
        con.close()
    ret = home_url(cat, q)
    sidebar = render_sidebar(cats, total, cat, ret, default_id)
    add_selected = cat if cat != 'all' else default_id
    add_options = category_options(cats, add_selected)
    cards_html = render_cards(rows, cats, ret)
    if rows:
        list_html = '<div class=cards>' + cards_html + '</div>'
    elif q:
        list_html = '<div class=empty><h2>没有找到匹配的记录</h2><p>试试更短的关键字，或清除搜索后再看看。</p></div>'
    elif cat != 'all':
        list_html = '<div class=empty><h2>这个归类还是空的</h2><p>可以从上方保存链接，或在已有记录里移动过来。</p></div>'
    else:
        list_html = '<div class=empty><h2>还没有收藏</h2><p>在上方粘贴一个链接，留下第一条记录。</p></div>'
    eyebrow = '搜索结果' if q else '我的收藏'
    result_note = (' · 关键字：' + escape(q)) if q else ''
    clear_link = f'''<a class=clear href='{home_url(cat)}'>清除搜索</a>''' if q else ''
    content = f'''<div class=page-head>
<div><p class=eyebrow>{eyebrow}</p><h1>{escape(current)}</h1><p class=result-line>{len(rows)} 条记录{result_note}</p></div>
</div>
<form method=get action=/ class=search-form role=search>
<input type=hidden name=category value='{cat}'>
<label class=sr-only for=search-q>关键字</label>
<input id=search-q type=search name=q value='{escape(q)}' maxlength=80 placeholder='搜索标题、网址或备注'>
<button class=primary>查找</button>
{clear_link}
</form>
<section class=add-panel>
<h2>收藏一条链接</h2>
<p class=hint>粘贴网址，选一个归类。标题留空时会自动使用网站地址；未特别处理的内容可以先放进默认归类。</p>
<form method=post action=/bookmarks/add class=add-form>
<input type=hidden name=return_to value='{escape(ret)}'>
<div class=add-grid>
<label class=wide>网页链接 *<input name=url maxlength=2048 required placeholder='https://example.com/article'></label>
<label>标题（可选）<input name=title maxlength=160 placeholder='留空则使用网址'></label>
<label>归类<select name=category_id>{add_options}</select></label>
<label class=wide>备注（可选）<textarea name=note rows=2 maxlength=2000 placeholder='价格、用途、稍后要看的重点……'></textarea></label>
</div>
<button class=primary>保存链接</button>
</form>
</section>
{list_html}
'''
    page_title = current + (' · ' + q if q else '')
    return page(page_title, content, sidebar, notice, kind)

class Handler(BaseHTTPRequestHandler):
    server_version = 'ShiguangClip/1.0'
    sys_version = ''

    def open_db(self):
        return connect(self.server.db_path)

    def send_html(self, status, body):
        data = body.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('Content-Security-Policy', CSP)
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def send_plain(self, status, text):
        data = text.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def see_other(self, location, notice=None, kind='ok'):
        if notice:
            sep = '&' if '?' in location else '?'
            location = location + sep + urlencode({'notice': clean(notice, 300), 'kind': kind})
        self.send_response(303)
        self.send_header('Location', location)
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', '0')
        self.end_headers()

    def read_form(self):
        try:
            length = int(self.headers.get('Content-Length') or '0')
        except ValueError:
            length = 0
        if length < 0 or length > MAX_BODY:
            raise ValueError('body too large')
        body = self.rfile.read(length).decode('utf-8', 'replace')
        parsed = parse_qs(body, keep_blank_values=True)
        return {key: values[-1] for key, values in parsed.items()}

    def do_GET(self):
        try:
            parsed = urlsplit(self.path)
            if parsed.path == '/':
                params = parse_qs(parsed.query, keep_blank_values=True)
                self.send_html(200, render_home(self.server.db_path, params))
            elif parsed.path == '/healthz':
                self.send_plain(200, 'ok')
            elif parsed.path == '/favicon.ico':
                self.send_response(204)
                self.end_headers()
            else:
                content = '<section class=empty><h1>页面不存在</h1><p><a href=/>返回收藏夹</a></p></section>'
                self.send_html(404, page('页面不存在', content))
        except sqlite3.Error:
            self.send_html(500, error_page('读取数据时出错，请稍后重试。'))
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_POST(self):
        origin = self.headers.get('Origin')
        host = self.headers.get('Host') or ''
        if origin and origin != 'http://' + host:
            self.send_html(403, error_page('请求来源无效，操作没有执行。'))
            return
        try:
            form = self.read_form()
        except ValueError:
            self.send_html(413, error_page('提交内容过大或格式不正确。'))
            return
        try:
            self.route_post(form)
        except sqlite3.Error:
            self.send_html(500, error_page('保存数据时出错，请稍后重试。'))
        except (BrokenPipeError, ConnectionResetError):
            pass

    def route_post(self, form):
        path = urlsplit(self.path).path
        ret = safe_return(form.get('return_to', ''))
        if path == '/bookmarks/add':
            self.post_add(form, ret)
            return
        if path == '/categories/add':
            self.post_category_add(form, ret)
            return
        parts = path.strip('/').split('/')
        if len(parts) == 3 and parts[0] == 'bookmarks' and parts[2] in ('edit', 'move', 'delete'):
            try:
                bid = int(parts[1])
            except ValueError:
                self.see_other(ret, '记录编号无效。', 'error')
                return
            if parts[2] == 'edit':
                self.post_edit(bid, form, ret)
            elif parts[2] == 'move':
                self.post_move(bid, form, ret)
            else:
                self.post_delete(bid, ret)
            return
        if len(parts) == 3 and parts[0] == 'categories' and parts[2] in ('rename', 'delete'):
            try:
                cid = int(parts[1])
            except ValueError:
                self.see_other(ret, '归类编号无效。', 'error')
                return
            if parts[2] == 'rename':
                self.post_category_rename(cid, form, ret)
            else:
                self.post_category_delete(cid, ret)
            return
        content = '<section class=empty><h1>页面不存在</h1><p><a href=/>返回收藏夹</a></p></section>'
        self.send_html(404, page('页面不存在', content))

    def post_add(self, form, ret):
        url, error = normalize_url(form.get('url', ''))
        if error:
            self.see_other(ret, error, 'error')
            return
        con = self.open_db()
        try:
            cid = parse_category(con, form.get('category_id', ''))
            if cid is None:
                self.see_other(ret, '选择的归类不存在，请重新选择。', 'error')
                return
            category = con.execute('SELECT name FROM categories WHERE id = ?', (cid,)).fetchone()
            if category is None:
                self.see_other(ret, '选择的归类不存在，请重新选择。', 'error')
                return
            title = clean(form.get('title', ''), 160) or title_from_url(url)
            note = clean(form.get('note', ''), 2000)
            duplicate = con.execute('SELECT id FROM bookmarks WHERE url = ? LIMIT 1', (url,)).fetchone()
            stamp = now_text()
            con.execute('INSERT INTO bookmarks (url, title, note, category_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)', (url, title, note, cid, stamp, stamp))
            con.commit()
            cat_name = category['name']
        finally:
            con.close()
        message = '已保存到「%s」。' % cat_name
        if duplicate is not None:
            message += ' 这个网址此前也收藏过。'
        self.see_other(ret, message)

    def post_edit(self, bid, form, ret):
        con = self.open_db()
        try:
            row = con.execute('SELECT id, url, title, category_id FROM bookmarks WHERE id = ?', (bid,)).fetchone()
            if row is None:
                self.see_other(ret, '这条收藏不存在，可能已经被删除。', 'error')
                return
            cid = parse_category(con, form.get('category_id', ''))
            if cid is None:
                self.see_other(ret, '选择的归类不存在，请重新选择。', 'error')
                return
            title = clean(form.get('title', ''), 160) or row['title'] or title_from_url(row['url'])
            note = clean(form.get('note', ''), 2000)
            con.execute('UPDATE bookmarks SET title = ?, note = ?, category_id = ?, updated_at = ? WHERE id = ?', (title, note, cid, now_text(), bid))
            con.commit()
        finally:
            con.close()
        self.see_other(ret, '修改已保存。')

    def post_move(self, bid, form, ret):
        con = self.open_db()
        try:
            row = con.execute('SELECT b.category_id, c.name AS category_name FROM bookmarks b JOIN categories c ON c.id = b.category_id WHERE b.id = ?', (bid,)).fetchone()
            if row is None:
                self.see_other(ret, '这条收藏不存在，可能已经被删除。', 'error')
                return
            cid = parse_category(con, form.get('category_id', ''))
            if cid is None:
                self.see_other(ret, '选择的归类不存在，请重新选择。', 'error')
                return
            target = con.execute('SELECT name FROM categories WHERE id = ?', (cid,)).fetchone()
            if target is None:
                self.see_other(ret, '选择的归类不存在，请重新选择。', 'error')
                return
            target_name = target['name']
            if cid == row['category_id']:
                message = '这条收藏已经在「%s」中。' % target_name
            else:
                con.execute('UPDATE bookmarks SET category_id = ?, updated_at = ? WHERE id = ?', (cid, now_text(), bid))
                con.commit()
                message = '已移动到「%s」。' % target_name
        finally:
            con.close()
        self.see_other(ret, message)

    def post_delete(self, bid, ret):
        con = self.open_db()
        try:
            row = con.execute('SELECT title FROM bookmarks WHERE id = ?', (bid,)).fetchone()
            if row is None:
                self.see_other(ret, '这条收藏不存在，可能已经被删除。', 'error')
                return
            title = clean(row['title'], 40)
            con.execute('DELETE FROM bookmarks WHERE id = ?', (bid,))
            con.commit()
        finally:
            con.close()
        self.see_other(ret, '已删除「%s」。' % title)

    def post_category_add(self, form, ret):
        name = clean(form.get('name', ''), 24)
        if not name:
            self.see_other(ret, '请填写归类名称。', 'error')
            return
        con = self.open_db()
        try:
            try:
                cur = con.execute('INSERT INTO categories (name, created_at) VALUES (?, ?)', (name, now_text()))
                con.commit()
                new_id = cur.lastrowid
            except sqlite3.IntegrityError:
                con.rollback()
                self.see_other(ret, '这个归类名称已经存在。', 'error')
                return
        finally:
            con.close()
        self.see_other(home_url(str(new_id)), '已新建归类「%s」。' % name)

    def post_category_rename(self, cid, form, ret):
        name = clean(form.get('name', ''), 24)
        if not name:
            self.see_other(ret, '请填写归类名称。', 'error')
            return
        con = self.open_db()
        try:
            row = con.execute('SELECT id FROM categories WHERE id = ?', (cid,)).fetchone()
            if row is None:
                self.see_other(ret, '这个归类不存在。', 'error')
                return
            try:
                con.execute('UPDATE categories SET name = ? WHERE id = ?', (name, cid))
                con.commit()
            except sqlite3.IntegrityError:
                con.rollback()
                self.see_other(ret, '这个归类名称已经存在。', 'error')
                return
        finally:
            con.close()
        self.see_other(ret, '归类已改名为「%s」。' % name)

    def post_category_delete(self, cid, ret):
        con = self.open_db()
        try:
            row = con.execute('SELECT id, name FROM categories WHERE id = ?', (cid,)).fetchone()
            if row is None:
                self.see_other(ret, '这个归类不存在。', 'error')
                return
            count = con.execute('SELECT COUNT(*) FROM categories').fetchone()[0]
            if count <= 1:
                self.see_other(ret, '至少需要保留一个归类，无法删除最后一个归类。', 'error')
                return
            removed_name = row['name']
            default_id = default_category_id(con)
            if cid == default_id:
                fallback_row = con.execute('SELECT id FROM categories WHERE id != ? ORDER BY id LIMIT 1', (cid,)).fetchone()
                if fallback_row is None:
                    self.see_other(ret, '找不到可用的目标归类。', 'error')
                    return
                fallback = fallback_row['id']
                con.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', ('default_category_id', str(fallback)))
            else:
                fallback = default_id
            cur = con.execute('UPDATE bookmarks SET category_id = ? WHERE category_id = ?', (fallback, cid))
            moved = cur.rowcount
            con.execute('DELETE FROM categories WHERE id = ?', (cid,))
            con.commit()
        finally:
            con.close()
        self.see_other(home_url(str(fallback)), '已删除归类「%s」，%d 条记录已移到其他归类。' % (removed_name, moved))

def main(argv=None):
    parser = argparse.ArgumentParser(description='本机中文生活待购与灵感收藏夹')
    parser.add_argument('--port', type=int, required=True, help='监听端口')
    parser.add_argument('--data-dir', required=True, help='保存 SQLite 数据的目录')
    args = parser.parse_args(argv)
    if args.port < 1 or args.port > 65535:
        parser.error('端口必须在 1 到 65535 之间')
    data_dir = os.path.abspath(os.path.expanduser(args.data_dir))
    try:
        os.makedirs(data_dir, exist_ok=True)
    except OSError as exc:
        print('无法创建数据目录：%s' % exc, file=sys.stderr)
        return 2
    if not os.path.isdir(data_dir):
        print('数据目录不可用：%s' % data_dir, file=sys.stderr)
        return 2
    db_path = os.path.join(data_dir, DB_NAME)
    try:
        init_db(db_path)
    except sqlite3.Error as exc:
        print('无法初始化数据库：%s' % exc, file=sys.stderr)
        return 2
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    except OSError as exc:
        print('无法监听 127.0.0.1:%d：%s' % (args.port, exc), file=sys.stderr)
        return 2
    server.db_path = db_path
    server.daemon_threads = True
    print('%s 已启动：http://127.0.0.1:%d' % (APP_NAME, args.port))
    print('数据目录：%s' % data_dir)
    print('按 Ctrl+C 停止。')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n已停止。')
    finally:
        server.server_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
