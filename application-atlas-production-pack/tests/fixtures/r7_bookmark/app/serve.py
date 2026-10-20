"""Controlled acceptance-program fixture, NEVER a G1 application delivery."""
import argparse
import html
import json
import os
import re
import sqlite3
import urllib.parse as url
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--host', default='127.0.0.1')
p.add_argument('--port', type=int, required=True)
p.add_argument('--data-dir', required=True)
args = p.parse_args()
Path(args.data_dir).mkdir(parents=True, exist_ok=True)
db = sqlite3.connect(Path(args.data_dir) / 'fixture.sqlite3', check_same_thread=False)
db.row_factory = sqlite3.Row
db.executescript('CREATE TABLE IF NOT EXISTS categories(id TEXT PRIMARY KEY,name TEXT UNIQUE); CREATE TABLE IF NOT EXISTS bookmarks(id TEXT PRIMARY KEY,url TEXT,title TEXT,description TEXT,hostname TEXT,category_id TEXT,trashed_at TEXT);')
mode = os.environ.get('ATLAS_R7_FIXTURE_MUTANT', '')
for name in ('未整理', '待购', '家居改造', '以后看看'):
    if mode == 'missing-preset' and name == '待购':
        continue
    db.execute('INSERT OR IGNORE INTO categories VALUES(?,?)', (uuid.uuid4().hex, name))
if mode == 'seeded-record':
    db.execute('INSERT OR IGNORE INTO bookmarks VALUES(?,?,?,?,?,?,NULL)', ('seed', 'https://seed.example', 'seed', '', 'seed.example', db.execute('SELECT id FROM categories LIMIT 1').fetchone()[0]))
db.commit()


def esc(value):
    return html.escape(str(value), quote=True)


def categories():
    return [dict(r) for r in db.execute('SELECT c.*, (SELECT COUNT(*) FROM bookmarks b WHERE b.category_id=c.id AND b.trashed_at IS NULL) count FROM categories c')]


def records(query):
    rows = [dict(r) for r in db.execute('SELECT b.*,c.name category FROM bookmarks b JOIN categories c ON c.id=b.category_id')]
    if query.get('include_trashed') != '1':
        rows = [r for r in rows if bool(r['trashed_at']) == (query.get('trash') == '1')]
    category = query.get('category')
    if category:
        rows = [r for r in rows if category in (r['category'], r['category_id'])]
    q = query.get('q', '').lower()
    if q:
        fields = ['title', 'hostname', 'description']
        if mode == 'category-name':
            fields.append('category')
        rows = [] if mode == 'always-empty' else [r for r in rows if any(q in r[f].lower() for f in fields)
            or (mode == 'url-path' and q in url.urlsplit(r['url']).path.lower())
            or (mode == 'url-query' and q in url.urlsplit(r['url']).query.lower())]
    return rows


def page(query, values=None, error=''):
    values = values or {}
    opts = ''.join(f'<option value="{esc(c["name"])}"' + (' selected' if c['name'] == query.get('category') else '') + f'>{esc(c["name"])}</option>' for c in categories())
    inputs = ''.join(f'<input name="{key}" value="{esc(values.get(key,""))}">' for key in ('url', 'title', 'description', 'category'))
    rows = records(query)
    row_html = ''.join(f'<tr data-testid="record-row" data-record-id="{r["id"]}"><td>{esc(r["title"])} {esc(r["description"])}<a data-testid="record-open-link" href="{esc(r["url"])}" target="_blank" rel="noopener noreferrer">打开</a></td></tr>' for r in rows)
    empty = '<p data-testid="empty-state">暂无记录</p>' if not rows and mode != 'missing-empty-ui' else ''
    return f'<html><body><p data-testid="form-error">{esc(error)}</p><form method="post" action="/bookmarks/new">{inputs}</form><a data-testid="category-manager" href="/categories">分类</a><form data-testid="category-search-form" method="get" action="/"><select name="category"><option value="">全部</option>{opts}</select><input name="q" value="{esc(query.get("q",""))}"></form><table data-testid="record-list">{row_html}</table>{empty}</body></html>'


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def respond(self, code, body, mime='application/json', headers=None):
        raw = (json.dumps(body, ensure_ascii=False) if mime == 'application/json' else str(body)).encode()
        self.send_response(code)
        self.send_header('Content-Type', mime + '; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        parsed = url.urlsplit(self.path)
        query = {k: v[-1] for k, v in url.parse_qs(parsed.query, keep_blank_values=True).items()}
        path = parsed.path
        if path == '/api/health':
            self.respond(200, {'ready': True})
        elif path == '/api/categories':
            self.respond(200, categories())
        elif path == '/api/bookmarks':
            self.respond(200, records(query))
        elif path.startswith('/api/bookmarks/'):
            found = [r for r in records({'include_trashed': '1'}) if r['id'] == path.rsplit('/', 1)[1]]
            self.respond(200 if found else 404, found[0] if found else {'error': {'code': 'not_found'}})
        elif path.startswith('/go/'):
            found = [r for r in records({}) if r['id'] == path.rsplit('/', 1)[1]]
            if found:
                self.respond(302, '', 'text/plain', {'Location': found[0]['url']})
            else:
                self.respond(404, {'error': {'code': 'not_found'}})
        elif path == '/':
            self.respond(200, page(query), 'text/html')
        else:
            self.respond(404, {'error': {'code': 'not_found'}})

    def do_POST(self):
        is_json = self.headers.get('Content-Type', '').startswith('application/json')
        raw = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        data = json.loads(raw) if is_json else {k: v[-1] for k, v in url.parse_qs(raw.decode(), keep_blank_values=True).items()}
        value = data.get('url', '')
        try:
            parsed = url.urlsplit(value)
            host = parsed.hostname or ''
            valid = parsed.scheme in ('http', 'https') and bool(host) and re.fullmatch(r'[a-zA-Z0-9.-]+', host)
            if is_json and mode == 'reject-json-single-label' and '.' not in host:
                valid = False
        except ValueError:
            valid = False
        if not valid:
            self.respond(400, {'error': {'code': 'invalid_url'}} if is_json else page({}, data, 'invalid_url'), 'application/json' if is_json else 'text/html')
            return
        category = data.get('category') or '未整理'
        db.execute('INSERT OR IGNORE INTO categories VALUES(?,?)', (uuid.uuid4().hex, category))
        cid = db.execute('SELECT id FROM categories WHERE name=?', (category,)).fetchone()[0]
        rid = uuid.uuid4().hex
        db.execute('INSERT INTO bookmarks VALUES(?,?,?,?,?,?,NULL)', (rid, value, data.get('title', ''), data.get('description', ''), host, cid))
        db.commit()
        if is_json:
            self.respond(201, next(r for r in records({}) if r['id'] == rid))
        else:
            self.respond(303, '', 'text/plain', {'Location': '/?' + url.urlencode({'category': category})})


ThreadingHTTPServer((args.host, args.port), Handler).serve_forever()
