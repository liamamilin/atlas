"""Synthetic HTTP/application-launch fixtures; they never implement a P0 app."""
from urllib.parse import parse_qsl, quote, urlsplit


class FakeResponse:
    def __init__(self, status=200, payload=None, text="", location=None, content_type="text/html"):
        self.status_code = status
        self._payload = payload
        self.text = text
        self.location = location
        self.content_type = content_type

    def json(self):
        return self._payload


class FakeProc:
    def __init__(self, root):
        self.app_root = root
        self.base_url = "http://fresh"
        self.stopped = False

    def poll(self):
        return 0 if self.stopped else None


class FakeA03Client:
    def __init__(self, p0, *, fresh=False, missing_fresh=None, missing_html=None, bad_default=False, reject_new=False):
        self.p0 = p0
        self.fresh = fresh
        self.missing_fresh = missing_fresh
        self.missing_html = missing_html
        self.bad_default = bad_default
        self.reject_new = reject_new
        self.records = {}
        self.next_id = 0
        self.closed = False

    def _categories(self):
        names = list(self.p0.common.PRESET_CATEGORIES) if self.fresh else [self.p0.common.DEFAULT_CATEGORY]
        if self.fresh and self.missing_fresh:
            names.remove(self.missing_fresh)
        if not self.fresh and len(self.records) > 1:
            names.append(next((r['category'] for r in self.records.values()
                               if r['category'] != self.p0.common.DEFAULT_CATEGORY), ''))
        return [{'id': f'c-{i}', 'name': name} for i, name in enumerate(filter(None, names))]

    def _home(self, category=None):
        names = [item['name'] for item in self._categories()]
        if self.fresh and self.missing_html:
            names = [name for name in names if name != self.missing_html]
        options = ''.join(f'<option value="{name}">{name}</option>' for name in names)
        form = '<form method="post" action="/bookmarks/new"><input name="url"><input name="title"><select name="category">' + options + '</select></form>'
        rows = []
        for rid, rec in self.records.items():
            if category and category != rec['category']:
                continue
            rows.append(f'<tr data-testid="record-row" data-record-id="{rid}"><td>{rec["title"]}</td><td><a data-testid="record-open-link" href="{rec["url"]}">{rec["url"]}</a></td></tr>')
        return form + '<table>' + ''.join(rows) + '</table>'

    def get(self, path, params=None, accept=None):
        if path == '/api/health':
            return FakeResponse(payload={'ok': True}, content_type='application/json')
        if path == '/api/categories':
            return FakeResponse(payload=self._categories(), content_type='application/json')
        if path.startswith('/api/bookmarks/'):
            rid = path.rsplit('/', 1)[-1]
            return FakeResponse(payload={'bookmark': self.records[rid]}, content_type='application/json')
        if path == '/api/bookmarks':
            chosen = (params or {}).get('category')
            rows = [r for r in self.records.values() if not chosen or r['category'] == chosen]
            return FakeResponse(payload=rows, content_type='application/json')
        if path == '/' or path.startswith('/?'):
            if path.startswith('/?'):
                params = dict(parse_qsl(urlsplit(path).query))
            return FakeResponse(text=self._home((params or {}).get('category')))
        raise AssertionError(f'unexpected fake GET {path!r}')

    def post_form(self, path, fields, follow_redirects=False, accept=None):
        self.next_id += 1
        rid = f'r{self.next_id}'
        category = fields.get('category') or self.p0.common.DEFAULT_CATEGORY
        if not fields.get('category') and self.bad_default:
            category = '错误默认分类'
        if self.reject_new and fields.get('category'):
            return FakeResponse(status=303, location='/?category=' + quote(category))
        self.records[rid] = {'id': rid, 'url': fields['url'], 'title': fields.get('title'), 'description': '', 'category': category}
        return FakeResponse(status=303, location='/?category=' + quote(category))

    def close(self):
        self.closed = True
