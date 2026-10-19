'''acceptance/common.py — 冻结验收套件的共享库。

导入本模块无任何副作用：不联网、不创建目录、不打开任何应用数据库。
模块只提供目标适配器、HTML 解析器、断言收集器与运行入口，不硬编码任何用例结论。
所有阶段文件（acceptance/p0.py、p1.py、p2.py）都基于本模块导出的接口，对真实 HTTP
目标执行正向与负向行为断言，标准输出恰为一行 atlas.acceptance-result.v1 JSON。

导出：
    HttpTarget(base_url)              标准库 http.client + http.cookiejar 目标适配器
    Headers                           大小写不敏感的响应头映射
    Form / parse_forms(html)          解析真实 HTML 表单的 action、method、字段与选项
    parse_list(html)                  解析书签列表项与归类列表项
    Assertions                        断言收集器（check/result/render）
    Ctx(base_url, data_dir, app_root) 运行上下文；data_dir 仅为 tester 可写草稿目录
    main(cases, argv)                 运行入口；stdout 恰一个结果 JSON，失败非零退出
    fail_explicit(msg[, case_id])     缺失/未知 flag 或基础设施缺失时显式非零退出
'''

import http.client
import http.cookiejar
import json
import os
import socket
import sys
import tempfile
import traceback
import urllib.parse
import urllib.request
from html.parser import HTMLParser

RESULT_SCHEMA = 'atlas.acceptance-result.v1'
RUNNER_SCHEMA = 'atlas.acceptance-runner.v1'
DEFAULT_TIMEOUT = 20.0

__all__ = [
    'RESULT_SCHEMA',
    'RUNNER_SCHEMA',
    'HttpTarget',
    'Headers',
    'Form',
    'parse_forms',
    'parse_list',
    'Assertions',
    'Ctx',
    'assertion',
    'redact',
    'fail_explicit',
    'main',
]


def redact(text):
    '''移除文本中 URL 授权段里的凭据，避免诊断信息泄露。'''
    value = str(text)
    marker = '://'
    pieces = []
    index = 0
    while True:
        position = value.find(marker, index)
        if position == -1:
            pieces.append(value[index:])
            break
        authority_start = position + len(marker)
        stop = len(value)
        for ch in ('/', '?', '#', chr(32), chr(9), chr(10)):
            found = value.find(ch, authority_start)
            if found != -1 and found < stop:
                stop = found
        at = value.find('@', authority_start)
        pieces.append(value[index:authority_start])
        if at != -1 and at < stop:
            index = at + 1
        else:
            index = authority_start
    return ''.join(pieces)


def assertion(aid, passed, detail=''):
    '''构造一条断言记录，供各阶段用例返回。'''
    return {'id': str(aid), 'passed': bool(passed), 'detail': str(detail)}


def _as_text(html):
    if isinstance(html, bytes):
        return html.decode('utf-8', 'replace')
    if html is None:
        return ''
    return str(html)


def _decode_body(raw, message):
    charset = 'utf-8'
    content_type = ''
    if message is not None:
        content_type = message.get('Content-Type') or ''
    for part in content_type.split(';'):
        piece = part.strip()
        if piece.lower().startswith('charset='):
            charset = piece.split('=', 1)[1].strip().replace(chr(34), '').replace(chr(39), '')
    try:
        return raw.decode(charset, 'replace')
    except LookupError:
        return raw.decode('utf-8', 'replace')


def _request_target(parts):
    target = parts.path or '/'
    if parts.query:
        target = target + '?' + parts.query
    return target


class Headers(dict):
    '''响应头映射；键查找大小写不敏感。'''

    def __init__(self, message=None):
        super().__init__()
        if message is not None:
            for key, value in message.items():
                self[key] = value

    def get(self, name, default=None):
        lowered = str(name).lower()
        for key, value in self.items():
            if key.lower() == lowered:
                return value
        return default

    def __contains__(self, name):
        lowered = str(name).lower()
        for key in self.keys():
            if key.lower() == lowered:
                return True
        return False


class HttpTarget:
    '''基于标准库的真实 HTTP 目标适配器；不接受带凭据的 URL。'''

    MAX_REDIRECTS = 5

    def __init__(self, base_url, timeout=DEFAULT_TIMEOUT):
        if not base_url:
            raise ValueError('base_url is required')
        parts = urllib.parse.urlsplit(base_url)
        if parts.scheme not in ('http', 'https') or not parts.hostname:
            raise ValueError('base_url must be an absolute http(s) URL')
        if parts.username or parts.password:
            raise ValueError('credential-bearing base URL is not supported')
        self.base_url = base_url
        self.scheme = parts.scheme
        self.host = parts.hostname
        self.port = parts.port
        self.timeout = timeout
        self._cookiejar = http.cookiejar.CookieJar()
        self.status = None
        self.reason = None
        self.headers = Headers()
        self.body = ''
        self.body_bytes = b''
        self.url = base_url

    @property
    def location(self):
        return self.headers.get('Location')

    def _connect(self, parts):
        if parts.scheme == 'https':
            return http.client.HTTPSConnection(parts.hostname, parts.port, timeout=self.timeout)
        return http.client.HTTPConnection(parts.hostname, parts.port, timeout=self.timeout)

    def request(self, method, path, body=None, content_type=None, headers=None,
                follow_redirects=False, _depth=0):
        url = urllib.parse.urljoin(self.base_url, path)
        parts = urllib.parse.urlsplit(url)
        if parts.scheme not in ('http', 'https') or not parts.hostname:
            raise ValueError('refusing to request non-http(s) URL')
        request = urllib.request.Request(url, data=body, method=method)
        request.add_header('Accept', 'text/html, */*')
        request.add_header('User-Agent', 'atlas-acceptance/1')
        if content_type:
            request.add_header('Content-Type', content_type)
        if headers:
            for key, value in headers.items():
                request.add_header(key, value)
        self._cookiejar.add_cookie_header(request)
        connection = self._connect(parts)
        try:
            connection.request(method, _request_target(parts), body=body,
                               headers=dict(request.header_items()))
            response = connection.getresponse()
            raw = response.read()
            self._cookiejar.extract_cookies(response, request)
            self.status = response.status
            self.reason = response.reason
            self.headers = Headers(response.headers)
            self.body_bytes = raw
            self.body = _decode_body(raw, response.headers)
            self.url = url
        finally:
            connection.close()
        if follow_redirects and self.status in (300, 301, 302, 303, 307, 308):
            target = self.headers.get('Location')
            if target:
                if _depth >= self.MAX_REDIRECTS:
                    raise http.client.HTTPException('too many redirects')
                next_url = urllib.parse.urljoin(url, target)
                return self.request('GET', next_url, None, None, None, True, _depth + 1)
        return self

    def get(self, path, follow_redirects=False, headers=None):
        return self.request('GET', path, None, None, headers, follow_redirects)

    def post_form(self, path, fields, follow_redirects=False, headers=None):
        encoded = urllib.parse.urlencode(fields, doseq=True).encode('utf-8')
        return self.request('POST', path, encoded,
                            'application/x-www-form-urlencoded', headers, follow_redirects)


class Form:
    '''一个解析后的 HTML 表单。'''

    def __init__(self, action='', method='get'):
        self.action = action
        self.method = method
        self.inputs = {}
        self.selects = {}
        self.textareas = {}

    def input(self, name):
        specs = self.inputs.get(name)
        return specs[0] if specs else None

    def select(self, name):
        return self.selects.get(name)

    def options(self, name):
        select = self.selects.get(name)
        return list(select['options']) if select else []

    def option_values(self, name):
        return [option['value'] for option in self.options(name)]

    def has_field(self, name):
        return name in self.inputs or name in self.selects or name in self.textareas

    def value_of(self, name):
        if name in self.inputs:
            return self.inputs[name][0]['value']
        if name in self.selects:
            for option in self.selects[name]['options']:
                if option['selected']:
                    return option['value']
            return None
        if name in self.textareas:
            return self.textareas[name]
        return None


class _FormParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.forms = []
        self._form = None
        self._selects = []
        self._option = None
        self._textarea = None

    @staticmethod
    def _attrs(attrs):
        return {key: ('' if value is None else value) for key, value in attrs}

    def handle_starttag(self, tag, attrs):
        values = self._attrs(attrs)
        if tag == 'form':
            self._form = Form(values.get('action', ''), (values.get('method') or 'get').lower())
            self.forms.append(self._form)
            return
        if self._form is None:
            return
        if tag == 'input':
            self._add_input(values)
        elif tag == 'select':
            name = values.get('name', '')
            select = {'name': name, 'multiple': 'multiple' in values,
                      'required': 'required' in values, 'options': []}
            self._form.selects[name] = select
            self._selects.append(select)
        elif tag == 'option' and self._selects:
            option = {'value': values.get('value', ''), 'has_value': 'value' in values,
                      'selected': 'selected' in values, 'label_parts': [], 'label': ''}
            self._selects[-1]['options'].append(option)
            self._option = option
        elif tag == 'textarea':
            name = values.get('name', '')
            self._form.textareas[name] = ''
            self._textarea = {'name': name, 'parts': []}

    def _add_input(self, values):
        name = values.get('name')
        if not name:
            return
        spec = {
            'name': name,
            'type': (values.get('type') or 'text').lower(),
            'value': values.get('value', ''),
            'required': 'required' in values,
            'checked': 'checked' in values,
            'placeholder': values.get('placeholder', ''),
        }
        self._form.inputs.setdefault(name, []).append(spec)

    def handle_endtag(self, tag):
        if tag == 'select' and self._selects:
            self._selects.pop()
        elif tag == 'option':
            self._option = None
        elif tag == 'textarea' and self._textarea is not None:
            self._form.textareas[self._textarea['name']] = ''.join(self._textarea['parts'])
            self._textarea = None
        elif tag == 'form':
            self._form = None

    def handle_data(self, data):
        if self._textarea is not None:
            self._textarea['parts'].append(data)
        elif self._option is not None:
            self._option['label_parts'].append(data)


def parse_forms(html):
    '''解析 HTML 中所有 form 的 action、method、输入字段、选项与文本域。'''
    parser = _FormParser()
    parser.feed(_as_text(html))
    parser.close()
    for form in parser.forms:
        for select in form.selects.values():
            for option in select['options']:
                label = ' '.join(''.join(option['label_parts']).split())
                option['label'] = label
                if not option['has_value']:
                    option['value'] = label
    return parser.forms


class _ListParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bookmarks = []
        self.collections = []
        self._stack = []
        self._items = []

    @staticmethod
    def _attrs(attrs):
        return {key: ('' if value is None else value) for key, value in attrs}

    def handle_starttag(self, tag, attrs):
        values = self._attrs(attrs)
        classes = set((values.get('class') or '').split())
        data = {key[5:]: values[key] for key in values if key.startswith('data-')}
        frame = {'tag': tag, 'classes': classes, 'data': data, 'item': None, 'role': None}
        if tag == 'li' and ('bookmark' in classes or 'collection' in classes):
            top = self._stack[-1] if self._stack else None
            if top is not None and top["item"] is not None and top["tag"] == 'li':
                closed = self._stack.pop()
                if self._items:
                    self._items.pop()
                self._finalize(closed["item"])
            kind = 'bookmark' if 'bookmark' in classes else 'collection'
            item = {
                'kind': kind,
                'data': data,
                'id': data.get(kind + '-id'),
                'text_parts': [],
                'title_parts': [],
                'note_parts': [],
                'fallback_title_parts': [],
                'url': None,
                'fallback_url': None,
            }
            frame['item'] = item
            frame['role'] = 'item'
            self._items.append(item)
        elif tag == 'a' and self._items:
            item = self._items[-1]
            if 'bookmark-title' in classes:
                item['url'] = values.get('href')
                frame['role'] = 'title'
            elif item['kind'] == 'bookmark' and item['fallback_url'] is None:
                item['fallback_url'] = values.get('href')
                frame['role'] = 'fallback-title'
        elif classes & set(['bookmark-note', 'note']):
            frame['role'] = 'note'
        self._stack.append(frame)

    def handle_data(self, data):
        if not self._items:
            return
        item = self._items[-1]
        role = None
        for frame in reversed(self._stack):
            if frame['role']:
                role = frame['role']
                break
        if role == 'title':
            item['title_parts'].append(data)
        elif role == 'fallback-title':
            item['fallback_title_parts'].append(data)
        elif role == 'note':
            item['note_parts'].append(data)
        else:
            item['text_parts'].append(data)

    def handle_endtag(self, tag):
        while self._stack:
            frame = self._stack.pop()
            if frame['item'] is not None:
                if self._items and self._items[-1] is frame['item']:
                    self._items.pop()
                self._finalize(frame['item'])
            if frame['tag'] == tag:
                break

    def _finalize(self, item):
        text = ' '.join(''.join(item['text_parts']).split())
        if item['kind'] == 'bookmark':
            title = ' '.join(''.join(item['title_parts']).split())
            if not title:
                title = ' '.join(''.join(item['fallback_title_parts']).split())
            note = ' '.join(''.join(item['note_parts']).split())
            self.bookmarks.append({
                'id': item['id'],
                'url': item['url'] or item['fallback_url'],
                'title': title,
                'note': note,
                'text': text,
                'collection_id': item['data'].get('collection-id'),
                'data': item['data'],
            })
        else:
            raw_default = item['data'].get('default')
            self.collections.append({
                'id': item['id'],
                'name': text,
                'default': raw_default in ('1', 'true', 'yes'),
                'default_raw': raw_default,
                'parent_id': item['data'].get('parent-id'),
                'data': item['data'],
            })


def parse_list(html):
    '''解析书签列表项与归类项，返回 bookmarks 与 collections 两组结果。'''
    parser = _ListParser()
    parser.feed(_as_text(html))
    parser.close()
    return {'bookmarks': parser.bookmarks, 'collections': parser.collections}


class Assertions:
    '''断言收集器；不含任何默认通过结论。'''

    def __init__(self):
        self.items = []

    def check(self, aid, passed, detail=''):
        record = {'id': str(aid), 'passed': bool(passed), 'detail': str(detail)}
        self.items.append(record)
        return record['passed']

    def ok(self):
        return bool(self.items) and all(item['passed'] for item in self.items)

    def result(self, case_id, status=None, assertions=None):
        items = list(self.items if assertions is None else assertions)
        if status is None:
            if not items:
                status = 'unverified'
            elif all(item['passed'] for item in items):
                status = 'passed'
            else:
                status = 'failed'
        return {'schema': RESULT_SCHEMA, 'case_id': case_id, 'status': status, 'assertions': items}

    def render(self, case_id, status=None, assertions=None):
        return json.dumps(self.result(case_id, status, assertions), ensure_ascii=False)


class Ctx:
    '''运行上下文。

    data_dir 仅为 tester 在 /state 下的可写草稿目录，绝不作为应用数据库，
    也不用于打开应用 SQLite；app_root 为只读应用源码目录（可缺省）。
    '''

    def __init__(self, base_url, data_dir, app_root=None):
        if not base_url:
            raise ValueError('base_url is required')
        if not data_dir:
            raise ValueError('data_dir is required')
        self.base_url = base_url
        self.data_dir = os.path.abspath(data_dir)
        self.app_root = os.path.abspath(app_root) if app_root else None
        os.makedirs(self.data_dir, exist_ok=True)
        self.target = HttpTarget(base_url)

    def new_session(self):
        '''返回全新的无 Cookie 客户端，用于无状态读回断言。'''
        return HttpTarget(self.base_url)

    def scratch_path(self, name):
        return os.path.join(self.data_dir, name)

    def write_scratch(self, name, data):
        path = self.scratch_path(name)
        if isinstance(data, (bytes, bytearray)):
            with open(path, 'wb') as handle:
                handle.write(data)
        else:
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(data)
        return path

    def read_scratch(self, name):
        with open(self.scratch_path(name), 'r', encoding='utf-8') as handle:
            return handle.read()


_KNOWN_OPTIONS = {
    '--case': 'case',
    '--base-url': 'base_url',
    '--data-dir': 'data_dir',
    '--app-root': 'app_root',
}

_INFRASTRUCTURE_ERRORS = (
    ConnectionError,
    socket.timeout,
    socket.gaierror,
    TimeoutError,
    http.client.HTTPException,
)


def fail_explicit(message, case_id=None):
    '''显式失败：缺失/未知 flag 或基础设施缺失时打印诊断并非零退出。

    已知 case_id 时，仍向 stdout 输出恰一个 status=failed 的结果 JSON。
    '''
    text = redact(message)
    if case_id:
        payload = Assertions().result(
            case_id,
            status='failed',
            assertions=[assertion('infrastructure', False, text)],
        )
        sys.stdout.write(json.dumps(payload, ensure_ascii=False) + '\n')
        sys.stdout.flush()
    sys.stderr.write('acceptance: FATAL: ' + text + '\n')
    sys.stderr.flush()
    raise SystemExit(2)


def _parse_cli(argv):
    options = {'case': None, 'base_url': None, 'data_dir': None, 'app_root': None}
    index = 0
    while index < len(argv):
        token = argv[index]
        if token in ('-h', '--help'):
            fail_explicit('--help is not a valid acceptance invocation; pass --case with a known case id')
        if token.startswith('--') and '=' in token:
            name, value = token.split('=', 1)
        elif token in _KNOWN_OPTIONS:
            name = token
            if index + 1 >= len(argv):
                fail_explicit('missing value for ' + token)
            value = argv[index + 1]
            index += 1
        else:
            fail_explicit('unrecognised argument ' + repr(token))
        if name not in _KNOWN_OPTIONS:
            fail_explicit('unrecognised argument ' + repr(name))
        options[_KNOWN_OPTIONS[name]] = value
        index += 1
    return options


def _normalise_assertions(produced):
    if produced is None:
        return []
    if isinstance(produced, Assertions):
        return list(produced.items)
    items = []
    for entry in produced:
        if isinstance(entry, dict):
            items.append({
                'id': str(entry.get('id', '')),
                'passed': bool(entry.get('passed', False)),
                'detail': str(entry.get('detail', '')),
            })
        elif isinstance(entry, (tuple, list)) and len(entry) >= 2:
            detail = entry[2] if len(entry) > 2 else ''
            items.append({'id': str(entry[0]), 'passed': bool(entry[1]), 'detail': str(detail)})
        else:
            items.append({'id': 'invalid-assertion', 'passed': False,
                          'detail': 'unrecognised assertion ' + repr(entry)})
    return items


def main(cases, argv=None):
    '''运行单个用例；stdout 恰一个 atlas.acceptance-result.v1 JSON，失败非零退出。'''
    if argv is None:
        argv = sys.argv[1:]
    options = _parse_cli(argv)
    case_id = options['case']
    if not case_id:
        fail_explicit('missing required flag --case')
    if case_id not in cases:
        fail_explicit('unknown --case ' + repr(case_id) + '; known cases: ' + ', '.join(sorted(cases)))
    if not options['base_url']:
        fail_explicit('missing required flag --base-url')
    data_dir = options['data_dir'] or tempfile.mkdtemp(prefix='atlas-acceptance-')
    try:
        context = Ctx(options['base_url'], data_dir, options['app_root'])
    except Exception as exc:
        fail_explicit('cannot initialise acceptance context: ' + redact(exc), case_id=case_id)
    try:
        items = _normalise_assertions(cases[case_id](context))
    except SystemExit:
        raise
    except _INFRASTRUCTURE_ERRORS as exc:
        fail_explicit('cannot reach target: ' + redact(exc), case_id=case_id)
    except BaseException as exc:
        traceback.print_exc(file=sys.stderr)
        items = [assertion('case-execution', False,
                           'case raised ' + type(exc).__name__ + ': ' + redact(exc))]
    if not items:
        items = [assertion('behavior', False, 'case produced no assertions')]
    status = 'passed' if all(item['passed'] for item in items) else 'failed'
    result = {'schema': RESULT_SCHEMA, 'case_id': case_id, 'status': status, 'assertions': items}
    sys.stdout.write(json.dumps(result, ensure_ascii=False) + '\n')
    sys.stdout.flush()
    raise SystemExit(0 if status == 'passed' else 1)


if __name__ == '__main__':
    fail_explicit('acceptance/common.py is a shared library; run a phase entry such as acceptance/p0.py')
