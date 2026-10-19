'''acceptance/p2.py — P2 互操作与可选增强用例（A19–A25）。

本脚本以 __file__ 定位套件根（sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))后导入 acceptance.common，并以其 main 直接驱动：
`python /suite/acceptance/p2.py --case A19..A25 --base-url <url> [--data-dir <dir>]
[--app-root <dir>]`。一个用例一次进程，stdout 恰一个 atlas.acceptance-result.v1 JSON，
诊断写 stderr，失败非零退出；全部断言基于对真实 HTTP 目标提交真实请求并解析真实
响应，绝不使用 mock，也不读取应用数据库、不重启进程。

本模块同时冻结 P2 的可驱动适配契约（P0/P1 沿用 acceptance/p1.py 声明的路由与表单字段）：

- 导出：`GET /export` 返回 200 的 Netscape 书签 HTML（含 `<!DOCTYPE
  NETSCAPE-Bookmark-file-1>` 标记），归类以 `<DT><H3>` 文件夹呈现，记录以
  `<DT><A HREF=".." ADD_DATE="..">标题</A>` 呈现，ADD_DATE 为 Unix 秒。
- 导入：`GET /import` 渲染带 `input[type=file]` 的真实表单；程序读取该表单的 action 与
  文件字段名（缺省 `/import`、字段 `file`），再以 multipart/form-data POST 上传
  Netscape HTML。文件夹名逐字映射为归类名，保留 URL、标题与 ADD_DATE。导入文件大小
  上限为 10 MiB（10485760 字节）。
- 元数据抓取：默认关闭。`POST /bookmarks` 仅在携带 `fetch=1` 时请求抓取；对私网、回环
  或链路本地目标一律以客户端安全错误（4xx）拒绝，绝不发起外发请求。
- 失效链接检查：`GET /links/check`。无外网环境下必须明确报告 unavailable/未验证
  （200 且正文含明确不可用标记，或 501/503），且不改动库内容。
- 网页存档：`GET /bookmarks/<id>/archive`。未配置存档时必须返回明确的未实现/不可用
  （404/501/503，或 200 且正文含明确不可用标记），不得伪造存档内容。
- 预填捕获：`GET /?add=1&url=<u>&title=<t>` 返回 200 的真实 `POST /bookmarks` 表单，
  url 与 title 字段预填为给定值；该 GET 只读，不产生记录。

导出 CASES = {case_id: fn(ctx) -> assertion 列表}；断言全部基于上述真实交互的响应，
不硬编码任何结论。
'''

import html
import os
import sys
import urllib.parse
import uuid
from html.parser import HTMLParser

_SUITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SUITE_ROOT not in sys.path:
    sys.path.insert(0, _SUITE_ROOT)

from acceptance.common import assertion, main, parse_forms, parse_list

__all__ = ['CASES']

_IMPORT_LIMIT_BYTES = 10 * 1024 * 1024
_LF = chr(10)
_CRLF = chr(13) + chr(10)

_UNVERIFIED_MARKERS = [
    'unavailable', 'unverified', 'not verified', 'not checked', 'offline',
    '未验证', '不可用', '无法验证', '未检查', '离线', '无法访问', '不可达', '无法连接',
]
_UNAVAILABLE_MARKERS = [
    'unavailable', 'not implemented', 'unimplemented', 'not configured',
    '未实现', '未配置', '不可用', '无法提供', '不支持',
]
_ARCHIVE_SUCCESS_MARKERS = [
    '存档成功', '副本已保存', 'archive saved', 'snapshot saved', 'copy saved', 'archive created',
]


def _token():
    '''每次运行生成唯一后缀，避免共享目标上的用例互相污染。'''
    return uuid.uuid4().hex[:10]


def _quote(value):
    return urllib.parse.quote(str(value), safe='')


def _collection_path(collection_id):
    return '/?collection=' + _quote(collection_id)


def _bookmark_path(bookmark_id):
    return '/bookmarks/' + _quote(bookmark_id)


def _escape_text(value):
    return html.escape(str(value), quote=False)


def _escape_attr(value):
    return html.escape(str(value), quote=True)


def _has_any(body, markers):
    lowered = str(body).lower()
    for marker in markers:
        if marker.lower() in lowered:
            return True
    return False


def _same_epoch(value, expected):
    if value is None:
        return False
    try:
        return int(str(value).strip()) == int(str(expected))
    except (TypeError, ValueError):
        return False


def _create_collection(ctx, name):
    return ctx.target.post_form('/collections', {'name': name})


def _save_bookmark(ctx, url, title, collection_id=None, fetch=None):
    fields = {'url': url, 'title': title}
    if collection_id is not None:
        fields['collection_id'] = str(collection_id)
    if fetch is not None:
        fields['fetch'] = str(fetch)
    return ctx.target.post_form('/bookmarks', fields)


def _collections(ctx):
    '''GET / 并解析侧栏归类项。'''
    ctx.target.get('/')
    return parse_list(ctx.target.body)['collections']


def _find_collection(ctx, name):
    for collection in _collections(ctx):
        if collection['name'] == name:
            return collection
    return None


def _bookmarks_in(ctx, path, client=None):
    '''GET path 并解析书签列表；非 200 时返回空列表。'''
    client = client if client is not None else ctx.target
    response = client.get(path)
    items = parse_list(response.body)['bookmarks'] if response.status == 200 else []
    return response, items


def _bookmark_key(item):
    if item['id']:
        return 'id:' + str(item['id'])
    return 'url:' + str(item['url']) + '|' + str(item['title'])


def _all_records(ctx):
    '''汇总首页、各归类视图与回收站中的记录，按 id 去重。'''
    records = {}
    home = ctx.target.get('/')
    if home.status == 200:
        parsed = parse_list(home.body)
        for item in parsed['bookmarks']:
            records[_bookmark_key(item)] = item
        for collection in parsed['collections']:
            cid = collection['id']
            if not cid:
                continue
            response = ctx.target.get(_collection_path(cid))
            if response.status == 200:
                for item in parse_list(response.body)['bookmarks']:
                    records[_bookmark_key(item)] = item
    trash = ctx.target.get('/trash')
    if trash.status == 200:
        for item in parse_list(trash.body)['bookmarks']:
            records[_bookmark_key(item)] = item
    return records


def _library_snapshot(ctx):
    return set(_all_records(ctx).keys())


def _find_record(ctx, url):
    for item in _all_records(ctx).values():
        if item['url'] == url:
            return item
    return None


class _NetscapeParser(HTMLParser):
    '''解析 Netscape 书签 HTML 中的文件夹（H3）与记录（A HREF）。'''

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.folders = []
        self._anchor = None
        self._heading = None

    def handle_starttag(self, tag, attrs):
        values = {key: ('' if value is None else value) for key, value in attrs}
        if tag == 'a':
            self._anchor = {'href': values.get('href'), 'add_date': values.get('add_date'),
                            'parts': [], 'text': ''}
        elif tag == 'h3':
            self._heading = {'add_date': values.get('add_date'), 'parts': [], 'text': ''}

    def handle_data(self, data):
        if self._anchor is not None:
            self._anchor['parts'].append(data)
        elif self._heading is not None:
            self._heading['parts'].append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self._anchor is not None:
            self._anchor['text'] = ' '.join(''.join(self._anchor['parts']).split())
            self.links.append(self._anchor)
            self._anchor = None
        elif tag == 'h3' and self._heading is not None:
            self._heading['text'] = ' '.join(''.join(self._heading['parts']).split())
            self.folders.append(self._heading)
            self._heading = None


def parse_netscape(body):
    '''解析 Netscape 书签 HTML，返回 {'links': [...], 'folders': [...]}。'''
    parser = _NetscapeParser()
    text = body if isinstance(body, str) else (body or b'').decode('utf-8', 'replace')
    parser.feed(text)
    parser.close()
    return {'links': parser.links, 'folders': parser.folders}


def _build_netscape(folder, entries):
    '''生成 Netscape 书签 HTML；entries 为 (url, title, add_date) 序列。'''
    lines = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        '<TITLE>Bookmarks</TITLE>',
        '<H1>Bookmarks</H1>',
        '<DL><p>',
    ]
    if folder:
        lines.append('    <DT><H3 ADD_DATE="1600000000">%s</H3>' % _escape_text(folder))
        lines.append('    <DL><p>')
    for url, title, add_date in entries:
        lines.append('        <DT><A HREF="%s" ADD_DATE="%s">%s</A>'
                     % (_escape_attr(url), _escape_text(add_date), _escape_text(title)))
    if folder:
        lines.append('    </DL><p>')
    lines.append('</DL><p>')
    return _LF.join(lines)


def _oversized_netscape(folder, token, limit):
    '''生成一个结构合法但超过大小上限的 Netscape 书签文件（字节）。'''
    lines = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<TITLE>Bookmarks</TITLE>',
        '<H1>Bookmarks</H1>',
        '<DL><p>',
        '    <DT><H3 ADD_DATE="1600000000">%s</H3>' % _escape_text(folder),
        '    <DL><p>',
    ]
    tail = ['    </DL><p>', '</DL><p>']
    size = len(_LF.join(lines + tail))
    index = 0
    while size <= limit:
        line = ('        <DT><A HREF="https://example.com/a21-%s-%d"'
                ' ADD_DATE="1600000000">A21-%d</A>' % (token, index, index))
        lines.append(line)
        size += len(line) + 1
        index += 1
    lines.extend(tail)
    return _LF.join(lines).encode('utf-8')


def _multipart_body(fields, file_field, filename, content):
    '''构造 multipart/form-data 请求体，返回 (content_type, body_bytes)。'''
    boundary = 'atlas' + uuid.uuid4().hex
    chunks = []
    for name, value in fields.items():
        chunks.append(('--' + boundary + _CRLF).encode('utf-8'))
        chunks.append(('Content-Disposition: form-data; name="%s"' % name
                       + _CRLF + _CRLF).encode('utf-8'))
        chunks.append(str(value).encode('utf-8'))
        chunks.append(_CRLF.encode('utf-8'))
    chunks.append(('--' + boundary + _CRLF).encode('utf-8'))
    chunks.append(('Content-Disposition: form-data; name="%s"; filename="%s"'
                   % (file_field, filename) + _CRLF + _CRLF).encode('utf-8'))
    chunks.append(('Content-Type: text/html' + _CRLF + _CRLF).encode('utf-8'))
    chunks.append(content if isinstance(content, (bytes, bytearray)) else content.encode('utf-8'))
    chunks.append(_CRLF.encode('utf-8'))
    chunks.append(('--' + boundary + '--' + _CRLF).encode('utf-8'))
    return 'multipart/form-data; boundary=' + boundary, b''.join(chunks)


def _import_target(ctx):
    '''从 GET /import 的真实表单读取 action 与文件字段名；未发现时显式标记。'''
    result = {'action': '/import', 'field': 'file', 'page': None, 'found': False}
    response = ctx.target.get('/import')
    result['page'] = response
    if response.status == 200:
        for form in parse_forms(response.body):
            for name, specs in form.inputs.items():
                if any(spec['type'] == 'file' for spec in specs):
                    result['action'] = form.action or '/import'
                    result['field'] = name
                    result['found'] = True
                    return result
    return result


def case_a19(ctx):
    '''A19：导出整个库为 Netscape 书签 HTML，解析出归类文件夹与记录。'''
    checks = []
    token = _token()
    name = 'A19导出-' + token
    url_1 = 'https://example.com/a19-1-' + token
    url_2 = 'https://example.com/a19-2-' + token
    title_1 = 'A19一号-' + token
    title_2 = 'A19二号-' + token
    decoy = 'https://example.com/a19-notsaved-' + token

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    for label, url, title in (('first', url_1, title_1), ('second', url_2, title_2)):
        saved = _save_bookmark(ctx, url, title, cid)
        checks.append(assertion('save-%s-303' % label, saved.status == 303,
                                'POST /bookmarks url=%r collection_id=%s status=%s'
                                % (url, cid, saved.status)))

    exported = ctx.target.get('/export')
    checks.append(assertion('export-200', exported.status == 200,
                            'GET /export status=%s' % exported.status))
    checks.append(assertion('export-netscape-marker',
                            'NETSCAPE-Bookmark-file-1' in exported.body,
                            'export body must be Netscape bookmark HTML; length=%d'
                            % len(exported.body)))
    parsed = parse_netscape(exported.body)
    links = {}
    for link in parsed['links']:
        links[link['href']] = link
    checks.append(assertion('export-contains-first',
                            url_1 in links and links[url_1]['text'] == title_1,
                            'export link for %r title=%r'
                            % (url_1, links[url_1]['text'] if url_1 in links else None)))
    checks.append(assertion('export-contains-second',
                            url_2 in links and links[url_2]['text'] == title_2,
                            'export link for %r title=%r'
                            % (url_2, links[url_2]['text'] if url_2 in links else None)))
    folder_names = [folder['text'] for folder in parsed['folders']]
    checks.append(assertion('export-folder-present', name in folder_names,
                            'export folders=%r expected %r' % (folder_names, name)))
    checks.append(assertion('export-excludes-unsaved', decoy not in exported.body,
                            'export must not contain unsaved %r' % decoy))
    return checks


def case_a20(ctx):
    '''A20：从 Netscape 书签 HTML 导入，文件夹映射为归类并保留 URL/标题/添加日期。'''
    checks = []
    token = _token()
    folder = 'A20文件夹-' + token
    url_1 = 'https://example.com/a20-1-' + token
    url_2 = 'https://example.com/a20-2-' + token
    title_1 = 'A20一号-' + token
    title_2 = 'A20二号-' + token
    add_date_1 = '1600000123'
    add_date_2 = '1600000456'

    payload = _build_netscape(folder, [
        (url_1, title_1, add_date_1),
        (url_2, title_2, add_date_2),
    ]).encode('utf-8')

    baseline = _library_snapshot(ctx)
    checks.append(assertion('baseline-snapshot', True, 'library keys before=%d' % len(baseline)))

    target = _import_target(ctx)
    checks.append(assertion('import-endpoint-ready', target['found'],
                            'GET /import status=%s file input discovered=%s'
                            % (target['page'].status if target['page'] else None, target['found'])))
    if not target['found']:
        return checks

    content_type, body = _multipart_body({}, target['field'], 'bookmarks.html', payload)
    imported = ctx.target.request('POST', target['action'], body, content_type)
    checks.append(assertion('import-accepted', imported.status in (200, 303),
                            'POST %s multipart status=%s' % (target['action'], imported.status)))

    collection = _find_collection(ctx, folder)
    checks.append(assertion('import-creates-folder-collection', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    _, items = _bookmarks_in(ctx, _collection_path(cid))
    found = {item['url']: item for item in items}
    checks.append(assertion('imported-first-url', url_1 in found,
                            'collection listed %r' % list(found)))
    checks.append(assertion('imported-first-title',
                            url_1 in found and found[url_1]['title'] == title_1,
                            'title=%r expected %r'
                            % (found[url_1]['title'] if url_1 in found else None, title_1)))
    checks.append(assertion('imported-second-url', url_2 in found,
                            'collection listed %r' % list(found)))
    checks.append(assertion('imported-second-title',
                            url_2 in found and found[url_2]['title'] == title_2,
                            'title=%r expected %r'
                            % (found[url_2]['title'] if url_2 in found else None, title_2)))

    exported = ctx.target.get('/export')
    checks.append(assertion('export-after-import-200', exported.status == 200,
                            'GET /export status=%s' % exported.status))
    by_href = {link['href']: link for link in parse_netscape(exported.body)['links']}
    checks.append(assertion('import-preserves-add-date-first',
                            url_1 in by_href and _same_epoch(by_href[url_1]['add_date'], add_date_1),
                            'ADD_DATE for %r=%r expected %s'
                            % (url_1, by_href[url_1]['add_date'] if url_1 in by_href else None,
                               add_date_1)))
    checks.append(assertion('import-preserves-add-date-second',
                            url_2 in by_href and _same_epoch(by_href[url_2]['add_date'], add_date_2),
                            'ADD_DATE for %r=%r expected %s'
                            % (url_2, by_href[url_2]['add_date'] if url_2 in by_href else None,
                               add_date_2)))

    after = _library_snapshot(ctx)
    checks.append(assertion('import-added-records', baseline <= after,
                            'before=%d after=%d' % (len(baseline), len(after))))
    return checks


def case_a21(ctx):
    '''A21：畸形、空或超限导入被明确拒绝且库内容与归类集合保持不变。'''
    checks = []
    token = _token()
    target = _import_target(ctx)
    checks.append(assertion('import-endpoint-ready', target['found'],
                            'GET /import status=%s file input discovered=%s'
                            % (target['page'].status if target['page'] else None, target['found'])))
    if not target['found']:
        return checks
    action = target['action']
    field = target['field']

    baseline = _library_snapshot(ctx)
    baseline_names = sorted(collection['name'] for collection in _collections(ctx))
    checks.append(assertion('baseline-snapshot', True,
                            'library keys=%d collections=%d'
                            % (len(baseline), len(baseline_names))))

    bad_inputs = [
        ('malformed', 'bad.html', b'<<< this is not a netscape bookmark file >>>'),
        ('empty', 'empty.html', b''),
    ]
    for label, filename, payload in bad_inputs:
        content_type, body = _multipart_body({}, field, filename, payload)
        response = ctx.target.request('POST', action, body, content_type)
        checks.append(assertion('reject-%s' % label, 400 <= response.status < 500,
                                'POST %s %s status=%s' % (action, label, response.status)))
        checks.append(assertion('error-body-%s' % label, bool(response.body.strip()),
                                'error response body length=%d' % len(response.body.strip())))

    oversized = _oversized_netscape('A21超限-' + token, token, _IMPORT_LIMIT_BYTES)
    checks.append(assertion('oversized-payload-exceeds-limit', len(oversized) > _IMPORT_LIMIT_BYTES,
                            'payload bytes=%d limit=%d' % (len(oversized), _IMPORT_LIMIT_BYTES)))
    content_type, body = _multipart_body({}, field, 'oversized.html', oversized)
    response = ctx.target.request('POST', action, body, content_type)
    checks.append(assertion('reject-oversized', 400 <= response.status < 500,
                            'POST %s oversized status=%s' % (action, response.status)))

    after = _library_snapshot(ctx)
    checks.append(assertion('library-unchanged', baseline == after,
                            'before=%d after=%d added=%r removed=%r'
                            % (len(baseline), len(after),
                               sorted(after - baseline), sorted(baseline - after))))
    after_names = sorted(collection['name'] for collection in _collections(ctx))
    checks.append(assertion('no-collection-created', baseline_names == after_names,
                            'collections before=%r after=%r' % (baseline_names, after_names)))
    return checks


def case_a22(ctx):
    '''A22：元数据抓取默认关闭（保存不外发）；携带 fetch=1 时私网/回环被安全拒绝。'''
    checks = []
    token = _token()
    loopback_ok = 'http://127.0.0.1:9/a22-default-' + token
    default_title = 'A22默认标题-' + token

    saved = _save_bookmark(ctx, loopback_ok, default_title)
    checks.append(assertion('default-save-accepted', saved.status in (200, 303),
                            'POST /bookmarks default url=%r status=%s'
                            % (loopback_ok, saved.status)))
    record = _find_record(ctx, loopback_ok)
    checks.append(assertion('default-save-recorded', bool(record),
                            'library record for %r present=%s' % (loopback_ok, bool(record))))
    if record:
        checks.append(assertion('default-no-metadata-fetch', record['title'] == default_title,
                                'stored title=%r expected user value %r (no fetch rewrite)'
                                % (record['title'], default_title)))

    blocked = [
        ('loopback', 'http://127.0.0.1:9/a22-fetch-' + token),
        ('localhost', 'http://localhost:9/a22-fetch-' + token),
        ('private', 'http://10.255.255.1/a22-fetch-' + token),
        ('link-local', 'http://169.254.169.254/a22-fetch-' + token),
    ]
    for label, url in blocked:
        response = _save_bookmark(ctx, url, 'A22拒绝-' + label, fetch='1')
        checks.append(assertion('fetch-rejected-' + label, 400 <= response.status < 500,
                                'POST /bookmarks fetch=1 url=%r status=%s'
                                % (url, response.status)))

    attempts = {url for _, url in blocked}
    leaked = [item['url'] for item in _all_records(ctx).values() if item['url'] in attempts]
    checks.append(assertion('rejected-fetch-no-record', not leaked,
                            'blocked fetch URLs must not be stored: %r' % leaked))
    return checks


def case_a23(ctx):
    '''A23：无外网下失效链接检查明确报告 unavailable/未验证，且不改动记录。'''
    checks = []
    token = _token()
    url = 'https://example.com/a23-' + token
    title = 'A23标题-' + token
    saved = _save_bookmark(ctx, url, title)
    checks.append(assertion('setup-save-303', saved.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url, saved.status)))

    before = _library_snapshot(ctx)
    checks.append(assertion('baseline-snapshot', True, 'library keys before=%d' % len(before)))

    response = ctx.target.get('/links/check')
    checks.append(assertion('check-responds', response.status in (200, 501, 503),
                            'GET /links/check status=%s' % response.status))
    if response.status == 200:
        checks.append(assertion('check-reports-unverified',
                                _has_any(response.body, _UNVERIFIED_MARKERS),
                                'offline check must report unavailable/unverified; body length=%d'
                                % len(response.body)))
    else:
        checks.append(assertion('check-explicit-unavailable', response.status in (501, 503),
                                'GET /links/check status=%s must be explicit unavailable'
                                % response.status))

    after = _library_snapshot(ctx)
    checks.append(assertion('check-does-not-modify-library', before == after,
                            'before=%d after=%d added=%r removed=%r'
                            % (len(before), len(after),
                               sorted(after - before), sorted(before - after))))
    return checks


def case_a24(ctx):
    '''A24：未配置存档时请求网页副本返回明确的未实现/不可用，不伪造存档。'''
    checks = []
    token = _token()
    name = 'A24归类-' + token
    url = 'https://example.com/a24-' + token
    title = 'A24标题-' + token

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    saved = _save_bookmark(ctx, url, title, collection['id'])
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url, saved.status)))
    record = _find_record(ctx, url)
    checks.append(assertion('record-present', bool(record and record['id']),
                            'library record for %r present=%s' % (url, bool(record))))
    if not (record and record['id']):
        return checks

    before = _library_snapshot(ctx)
    response = ctx.target.get(_bookmark_path(record['id']) + '/archive')
    explicit = response.status in (404, 501, 503) or (
        response.status == 200 and _has_any(response.body, _UNAVAILABLE_MARKERS))
    checks.append(assertion('archive-unconfigured-explicit', explicit,
                            'GET /bookmarks/%s/archive status=%s must be explicit '
                            'unimplemented/unavailable' % (record['id'], response.status)))
    checks.append(assertion('archive-not-fabricated',
                            not _has_any(response.body, _ARCHIVE_SUCCESS_MARKERS),
                            'response must not fabricate a saved archive copy'))
    after = _library_snapshot(ctx)
    checks.append(assertion('archive-request-does-not-change-library', before == after,
                            'before=%d after=%d added=%r removed=%r'
                            % (len(before), len(after),
                               sorted(after - before), sorted(before - after))))
    return checks


def case_a25(ctx):
    '''A25：预填捕获入口 GET /?add=1&url=&title= 返回带预填值的真实保存表单。'''
    checks = []
    token = _token()
    url = 'https://example.com/a25-' + token + '?a=1&b=2'
    title = 'A25标题-' + token + ' & 灵感'

    before = _library_snapshot(ctx)
    path = '/?add=1&url=' + _quote(url) + '&title=' + _quote(title)
    response = ctx.target.get(path)
    checks.append(assertion('prefill-200', response.status == 200,
                            'GET prefill entry status=%s' % response.status))

    forms = parse_forms(response.body)
    form = None
    for candidate in forms:
        action = candidate.action or ''
        if candidate.method == 'post' and 'bookmarks' in action and candidate.has_field('url'):
            form = candidate
            break
    checks.append(assertion('prefill-real-capture-form', form is not None,
                            'forms=%r' % [candidate.action for candidate in forms]))
    if form is not None:
        checks.append(assertion('prefill-url-value',
                                form.input('url') is not None and form.value_of('url') == url,
                                'url field value=%r expected %r'
                                % (form.value_of('url'), url)))
        checks.append(assertion('prefill-title-value',
                                form.input('title') is not None and form.value_of('title') == title,
                                'title field value=%r expected %r'
                                % (form.value_of('title'), title)))
        checks.append(assertion('prefill-has-collection-field', form.has_field('collection_id'),
                                'capture form must expose collection_id selection'))

    after = _library_snapshot(ctx)
    checks.append(assertion('prefill-get-is-read-only', before == after,
                            'before=%d after=%d added=%r'
                            % (len(before), len(after), sorted(after - before))))
    return checks


CASES = {
    'A19': case_a19,
    'A20': case_a20,
    'A21': case_a21,
    'A22': case_a22,
    'A23': case_a23,
    'A24': case_a24,
    'A25': case_a25,
}


if __name__ == '__main__':
    main(CASES, sys.argv[1:])
