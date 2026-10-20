#!/usr/bin/env python3
'''P0 行为验收组：A01、A02、A03、A11。

覆盖真实保存表单与会话/重启持久化、URL 正向边界与非法输入、
默认归类与自动创建归类、启动健康与首页外壳。仅使用 Python 3.12
标准库并复用 acceptance/common.py：以 --case 派发，未知用例显式失败；
每个用例对真实目标执行正向与硬负向行为断言，向 stdout 输出单个
atlas.acceptance-result.v1 JSON，失败时以非零码退出。
'''

from __future__ import annotations

import os
import re
import sys
import urllib.parse
import uuid
from html.parser import HTMLParser

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import common

_WHITESPACE_RE = re.compile(r'\s+')
_EMPTY_MARKERS = (
    '暂无',
    '没有记录',
    '还没有',
    '空状态',
    '无匹配',
    'no bookmarks',
    'nothing here',
    'empty',
)
_LIST_TAGS = frozenset({'ul', 'ol', 'table'})
_LIST_ATTR_TAGS = frozenset({'div', 'main', 'section', 'article', 'aside'})


class _Field:
    def __init__(self, attrs):
        self.attrs = attrs
        self.name = attrs.get('name')
        self.value = attrs.get('value', '')
        self.type = (attrs.get('type') or 'text').lower()
        self.checked = 'checked' in attrs


class _Option:
    def __init__(self, attrs):
        self.attrs = attrs
        self.value = attrs.get('value')
        self.text = ''
        self.selected = 'selected' in attrs

    def resolved_value(self):
        if self.value is not None:
            return self.value
        return self.text.strip()


class _Select:
    def __init__(self, attrs):
        self.attrs = attrs
        self.name = attrs.get('name')
        self.options = []

    def selected_value(self):
        for option in self.options:
            if option.selected:
                return option.resolved_value()
        if self.options:
            return self.options[0].resolved_value()
        return ''


class _Textarea:
    def __init__(self, attrs):
        self.attrs = attrs
        self.name = attrs.get('name')
        self.text = ''


class _Form:
    def __init__(self, attrs):
        self.attrs = attrs
        self.action = (attrs.get('action') or '').strip()
        self.method = (attrs.get('method') or 'get').strip().lower()
        self.testid = attrs.get('data-testid') or ''
        self.fields = []
        self.selects = []
        self.textareas = []

    def has_name(self, name):
        if any(field.name == name for field in self.fields):
            return True
        if any(select.name == name for select in self.selects):
            return True
        return any(textarea.name == name for textarea in self.textareas)

    def value(self, name):
        for field in reversed(self.fields):
            if field.name == name:
                return field.value
        for select in reversed(self.selects):
            if select.name == name:
                return select.selected_value()
        for textarea in reversed(self.textareas):
            if textarea.name == name:
                return textarea.text
        return None


class _Anchor:
    def __init__(self, attrs):
        self.attrs = attrs
        self.href = attrs.get('href') or ''
        self.testid = attrs.get('data-testid') or ''
        self.text = ''


class _Row:
    def __init__(self, attrs):
        self.attrs = attrs
        self.record_id = attrs.get('data-record-id') or ''
        self.anchors = []
        self.text = ''


def _action_path(action):
    text = (action or '').strip()
    if not text:
        return ''
    try:
        path = urllib.parse.urlsplit(text).path
    except ValueError:
        return text
    if not path:
        return ''
    if not path.startswith('/'):
        path = '/' + path
    return path.rstrip('/') or '/'


class _Document:
    def __init__(self):
        self.forms = []
        self.anchors = []
        self.rows = []
        self.testids = []
        self.start_tags = []
        self.text = ''

    def save_form(self):
        for form in self.forms:
            if form.method == 'post' and _action_path(form.action) == '/bookmarks/new':
                return form
        for form in self.forms:
            if form.method == 'post' and form.has_name('url'):
                return form
        return None


class _HtmlReader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.doc = _Document()
        self._form = None
        self._select = None
        self._option = None
        self._textarea = None
        self._anchor = None
        self._row = None
        self._testid_stack = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attributes = {
            str(key).lower(): ('' if value is None else value)
            for key, value in attrs
        }
        self.doc.start_tags.append((tag, attributes))
        testid = attributes.get('data-testid') or ''
        if testid:
            entry = {'tag': tag, 'attrs': attributes, 'text': ''}
            self.doc.testids.append(entry)
            self._testid_stack.append((tag, entry))
        if tag == 'form':
            self._finish_form()
            self._form = _Form(attributes)
        elif tag == 'input':
            if self._form is not None:
                self._form.fields.append(_Field(attributes))
        elif tag == 'select':
            self._finish_select()
            if self._form is not None:
                self._select = _Select(attributes)
        elif tag == 'option':
            self._finish_option()
            if self._select is not None:
                self._option = _Option(attributes)
        elif tag == 'textarea':
            self._finish_textarea()
            if self._form is not None:
                self._textarea = _Textarea(attributes)
        elif tag == 'a':
            self._finish_anchor()
            self._anchor = _Anchor(attributes)
        elif tag == 'tr' and testid == 'record-row':
            self._finish_row()
            self._row = _Row(attributes)

    def handle_data(self, data):
        if not data:
            return
        self.doc.text += data
        if self._row is not None:
            self._row.text += data
        if self._anchor is not None:
            self._anchor.text += data
        if self._option is not None:
            self._option.text += data
        if self._textarea is not None:
            self._textarea.text += data
        for _, entry in self._testid_stack:
            entry['text'] += data

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'a':
            self._finish_anchor()
        elif tag == 'option':
            self._finish_option()
        elif tag == 'select':
            self._finish_select()
        elif tag == 'textarea':
            self._finish_textarea()
        elif tag == 'form':
            self._finish_form()
        elif tag == 'tr':
            self._finish_row()
        if self._testid_stack and self._testid_stack[-1][0] == tag:
            self._testid_stack.pop()

    def _finish_option(self):
        if self._option is None:
            return
        option = self._option
        self._option = None
        if self._select is not None:
            self._select.options.append(option)

    def _finish_select(self):
        self._finish_option()
        if self._select is None:
            return
        select = self._select
        self._select = None
        if self._form is not None:
            self._form.selects.append(select)

    def _finish_textarea(self):
        if self._textarea is None:
            return
        textarea = self._textarea
        self._textarea = None
        if self._form is not None:
            self._form.textareas.append(textarea)

    def _finish_anchor(self):
        if self._anchor is None:
            return
        anchor = self._anchor
        self._anchor = None
        self.doc.anchors.append(anchor)
        if self._row is not None:
            self._row.anchors.append(anchor)

    def _finish_row(self):
        if self._row is None:
            return
        row = self._row
        self._row = None
        self.doc.rows.append(row)

    def _finish_form(self):
        self._finish_select()
        self._finish_textarea()
        if self._form is None:
            return
        form = self._form
        self._form = None
        self.doc.forms.append(form)

    def finalize(self):
        self._finish_anchor()
        self._finish_row()
        self._finish_form()


def _parse_html(text):
    reader = _HtmlReader()
    reader.feed(text or '')
    reader.close()
    reader.finalize()
    return reader.doc


def _unique_url(tag):
    token = f'{tag}-{uuid.uuid4().hex[:12]}'
    return f'https://{token}.atlas-acceptance.example/{token}'


def _safe_json(response):
    try:
        return response.json()
    except Exception:
        return None


def _extract_record(payload):
    if isinstance(payload, dict):
        for key in ('bookmark', 'record', 'data', 'item'):
            value = payload.get(key)
            if isinstance(value, dict):
                return value
        return payload
    return None


def _extract_list(payload, keys):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return None


def _record_id(record):
    if isinstance(record, dict) and record.get('id') is not None:
        return str(record['id'])
    return None


def _record_url(record):
    if isinstance(record, dict) and record.get('url') is not None:
        return str(record['url'])
    return None


def _record_title(record):
    if isinstance(record, dict) and record.get('title') is not None:
        return str(record['title'])
    return None


def _record_description(record):
    if isinstance(record, dict) and record.get('description') is not None:
        return str(record['description'])
    return None


def _bookmark_path(bookmark_id):
    return '/api/bookmarks/' + urllib.parse.quote(str(bookmark_id), safe='')


def _error_code(response):
    payload = _safe_json(response)
    if isinstance(payload, dict):
        error = payload.get('error')
        if isinstance(error, dict) and error.get('code') is not None:
            return str(error['code'])
        for key in ('code', 'error_code'):
            if payload.get(key) is not None:
                return str(payload[key])
    return None


def _fetch_bookmarks(client, recorder, aid, params=None):
    response = client.get('/api/bookmarks', params=params)
    recorder.expect_status(response, 200, aid=f'{aid}-list-status')
    payload = _safe_json(response)
    records = _extract_list(payload, ('bookmarks', 'items', 'data', 'records'))
    recorder.check(
        f'{aid}-list-shape',
        isinstance(records, list),
        f'GET /api/bookmarks 必须返回 JSON 数组，实际 {type(payload).__name__}',
    )
    return records if isinstance(records, list) else []


def _fetch_categories(client, recorder, aid):
    response = client.get('/api/categories')
    recorder.expect_status(response, 200, aid=f'{aid}-categories-status')
    payload = _safe_json(response)
    categories = _extract_list(payload, ('categories', 'items', 'data'))
    recorder.check(
        f'{aid}-categories-shape',
        isinstance(categories, list),
        f'GET /api/categories 必须返回 JSON 数组，实际 {type(payload).__name__}',
    )
    return categories if isinstance(categories, list) else []


def _category_names(categories):
    names = set()
    for item in categories:
        if isinstance(item, dict) and item.get('name') is not None:
            names.add(str(item['name']))
    return names


def _category_name(record, categories):
    if not isinstance(record, dict):
        return None
    names = _category_names(categories)
    by_id = {}
    for item in categories:
        if isinstance(item, dict) and item.get('id') is not None and item.get('name') is not None:
            by_id[str(item['id'])] = str(item['name'])
    for key in ('category', 'category_name', 'categoryName'):
        value = record.get(key)
        if isinstance(value, str):
            if value in names:
                return value
            if value in by_id:
                return by_id[value]
            return value
        if isinstance(value, dict) and value.get('name') is not None:
            return str(value['name'])
    for key in ('category_id', 'categoryId'):
        value = record.get(key)
        if value is not None and str(value) in by_id:
            return by_id[str(value)]
    return None


def _record_ids(records):
    return {_record_id(record) for record in records}


def _action_of(form):
    return form.action or '/'


def _form_fields(form, overrides=None, omit=()):
    fields = {}
    for field in form.fields:
        name = field.name
        if not name:
            continue
        if field.type in ('submit', 'button', 'reset', 'file', 'image'):
            continue
        if field.type in ('checkbox', 'radio') and not field.checked:
            continue
        fields[name] = field.value
    for select in form.selects:
        if select.name:
            fields[select.name] = select.selected_value()
    for textarea in form.textareas:
        if textarea.name:
            fields[textarea.name] = textarea.text
    if overrides:
        for key, value in overrides.items():
            fields[str(key)] = str(value)
    for name in omit:
        fields.pop(name, None)
    return fields


def _form_error_text(doc):
    parts = []
    for entry in doc.testids:
        testid = (entry['attrs'].get('data-testid') or '').lower()
        if testid == 'form-error' or 'form-error' in testid:
            text = _WHITESPACE_RE.sub(' ', entry['text']).strip()
            if text:
                parts.append(text)
    return ' '.join(parts)


def _row_for_url(doc, url):
    for row in doc.rows:
        for anchor in row.anchors:
            if anchor.testid == 'record-open-link' and anchor.href == url:
                return row
    for row in doc.rows:
        for anchor in row.anchors:
            if anchor.href == url:
                return row
    return None


def _row_by_id(doc, record_id):
    for row in doc.rows:
        if row.record_id == record_id:
            return row
    return None


def _row_open_link(row):
    for anchor in row.anchors:
        if anchor.testid == 'record-open-link':
            return anchor
    for anchor in row.anchors:
        if anchor.href.startswith('http://') or anchor.href.startswith('https://'):
            return anchor
    return None


def _category_values_in_html(doc):
    values = set()
    for form in doc.forms:
        for select in form.selects:
            if select.name != 'category':
                continue
            for option in select.options:
                value = option.resolved_value()
                if value:
                    values.add(value)
                text = option.text.strip()
                if text:
                    values.add(text)
    for anchor in doc.anchors:
        try:
            parts = urllib.parse.urlsplit(anchor.href)
        except ValueError:
            continue
        for key, value in urllib.parse.parse_qsl(parts.query, keep_blank_values=True):
            if key == 'category' and value:
                values.add(value)
    return values


def _has_list_container(doc):
    for tag, attrs in doc.start_tags:
        if tag in _LIST_TAGS:
            return True
        if tag not in _LIST_ATTR_TAGS:
            continue
        haystack = ' '.join((
            attrs.get('data-testid') or '',
            attrs.get('id') or '',
            attrs.get('class') or '',
        )).lower()
        if any(token in haystack for token in ('bookmark', 'record', 'list', 'item')):
            return True
    return False


def _empty_state_marker(doc):
    for entry in doc.testids:
        testid = (entry['attrs'].get('data-testid') or '').lower()
        if 'empty' in testid:
            text = _WHITESPACE_RE.sub(' ', entry['text']).strip()
            return text or testid
    text = _WHITESPACE_RE.sub(' ', doc.text).lower()
    for marker in _EMPTY_MARKERS:
        if marker in text:
            return marker
    return ''


def _save_form_from_home(client, recorder, aid):
    home = client.get('/', accept='text/html')
    recorder.expect_status(home, 200, aid=f'{aid}-home-status')
    doc = _parse_html(home.text)
    form = doc.save_form()
    if not recorder.check(
        f'{aid}-save-form',
        form is not None,
        '首页含 action=/bookmarks/new 且 method=post 的保存表单',
    ):
        return doc, None
    return doc, form


def _follow_303(client, recorder, response, aid):
    recorder.expect_status(response, 303, aid=f'{aid}-status')
    location = response.location
    if not recorder.check(
        f'{aid}-location',
        bool(location),
        f'303 响应必须带 Location，实际 {location!r}',
    ):
        return None
    page = client.get(location, accept='text/html')
    recorder.expect_status(page, 200, aid=f'{aid}-follow-status')
    return page


def _get_record(client, recorder, record_id, aid):
    if not record_id:
        recorder.check(f'{aid}-record-id', False, '缺少记录 id，无法读回 JSON')
        return None
    response = client.get(_bookmark_path(record_id))
    recorder.expect_status(response, 200, aid=f'{aid}-record-status')
    payload = _safe_json(response)
    record = _extract_record(payload)
    recorder.check(
        f'{aid}-record-shape',
        isinstance(record, dict),
        'GET /api/bookmarks/{id} 必须返回 JSON 对象，实际 ' + type(payload).__name__,
    )
    return record if isinstance(record, dict) else None


def _case_a01(args, recorder):
    client = common.HttpClient(args.base_url)
    live_url = _unique_url('a01-live')
    live_title = f'A01 保存标题 {uuid.uuid4().hex[:8]}'
    live_description = f'A01 保存描述 {uuid.uuid4().hex[:8]}'
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a01-health-status')
        recorder.check(
            'a01-health-json',
            isinstance(_safe_json(health), dict),
            '/api/health 返回 JSON 对象',
        )
        _, form = _save_form_from_home(client, recorder, 'a01')
        if form is None:
            return
        fields = _form_fields(form, {
            'url': live_url,
            'title': live_title,
            'description': live_description,
        })
        response = client.post_form(
            _action_of(form), fields, follow_redirects=False, accept='text/html'
        )
        page = _follow_303(client, recorder, response, 'a01-save')
        if page is None:
            return
        doc = _parse_html(page.text)
        row = _row_for_url(doc, live_url)
        if not recorder.check(
            'a01-row-present',
            row is not None,
            f'保存后 HTML 列表出现原始 URL={live_url!r} 的记录行',
        ):
            return
        record_id = row.record_id
        recorder.check('a01-row-id', bool(record_id), f'记录行 data-record-id={record_id!r}')
        recorder.check(
            'a01-row-title',
            live_title in row.text,
            f'记录行文本包含标题 {live_title!r}',
        )
        recorder.check(
            'a01-row-description',
            live_description in row.text,
            f'记录行文本包含描述 {live_description!r}',
        )
        link = _row_open_link(row)
        href = link.href if link is not None else None
        recorder.check(
            'a01-row-href',
            href == live_url,
            f'行内打开链接 href={href!r}（期望 {live_url!r}）',
        )
        record = _get_record(client, recorder, record_id, 'a01')
        if record is not None:
            recorder.check(
                'a01-json-id',
                _record_id(record) == record_id,
                f'JSON id={_record_id(record)!r}（期望 {record_id!r}）',
            )
            recorder.check(
                'a01-json-url',
                _record_url(record) == live_url,
                f'JSON url={_record_url(record)!r}（期望 {live_url!r}）',
            )
            recorder.check(
                'a01-json-title',
                _record_title(record) == live_title,
                f'JSON title={_record_title(record)!r}（期望 {live_title!r}）',
            )
            recorder.check(
                'a01-json-description',
                _record_description(record) == live_description,
                f'JSON description={_record_description(record)!r}（期望 {live_description!r}）',
            )
    finally:
        client.close()

    first = None
    second = None
    instance_dir = None
    restart_id = None
    restart_url = _unique_url('a01-restart')
    restart_title = f'A01 重启标题 {uuid.uuid4().hex[:8]}'
    restart_description = f'A01 重启描述 {uuid.uuid4().hex[:8]}'
    try:
        try:
            first = common.launch_app(args.app_root, args.data_dir, 0)
            instance_dir = first.instance_dir
            first_client = None
            try:
                first_client = common.HttpClient(first.base_url)
                _, form = _save_form_from_home(first_client, recorder, 'a01-instance')
                if form is not None:
                    fields = _form_fields(form, {
                        'url': restart_url,
                        'title': restart_title,
                        'description': restart_description,
                    })
                    response = first_client.post_form(
                        _action_of(form), fields, follow_redirects=False, accept='text/html'
                    )
                    page = _follow_303(first_client, recorder, response, 'a01-instance')
                    if page is not None:
                        doc = _parse_html(page.text)
                        row = _row_for_url(doc, restart_url)
                        if recorder.check(
                            'a01-instance-row',
                            row is not None,
                            f'隔离实例保存后 HTML 列表出现 URL={restart_url!r} 的记录行',
                        ):
                            restart_id = row.record_id
                            recorder.check(
                                'a01-instance-row-id',
                                bool(restart_id),
                                f'隔离实例记录 data-record-id={restart_id!r}',
                            )
                            recorder.check(
                                'a01-instance-row-title',
                                restart_title in row.text,
                                f'隔离实例记录行包含标题 {restart_title!r}',
                            )
                            recorder.check(
                                'a01-instance-row-description',
                                restart_description in row.text,
                                f'隔离实例记录行包含描述 {restart_description!r}',
                            )
                            link = _row_open_link(row)
                            href = link.href if link is not None else None
                            recorder.check(
                                'a01-instance-row-href',
                                href == restart_url,
                                f'隔离实例行内 href={href!r}（期望 {restart_url!r}）',
                            )
                            record = _get_record(
                                first_client, recorder, restart_id, 'a01-instance'
                            )
                            if record is not None:
                                recorder.check(
                                    'a01-instance-json-url',
                                    _record_url(record) == restart_url,
                                    f'隔离实例 JSON url={_record_url(record)!r}（期望 {restart_url!r}）',
                                )
            finally:
                if first_client is not None:
                    first_client.close()
        finally:
            if first is not None:
                common.stop_app(first)
        if not restart_id or not instance_dir:
            recorder.check(
                'a01-restart-prerequisite',
                False,
                '隔离实例未提供可重启的记录 id 或实例目录',
            )
            return
        second = common.launch_app(
            args.app_root, args.data_dir, 0, instance_dir=instance_dir
        )
        second_client = None
        try:
            second_client = common.HttpClient(second.base_url)
            page = second_client.get('/', accept='text/html')
            recorder.expect_status(page, 200, aid='a01-restart-home-status')
            doc = _parse_html(page.text)
            row = _row_by_id(doc, restart_id)
            recorder.check(
                'a01-restart-row',
                row is not None,
                f'重启后 HTML 列表包含 id={restart_id!r} 的记录行',
            )
            if row is not None:
                link = _row_open_link(row)
                href = link.href if link is not None else None
                recorder.check(
                    'a01-restart-href',
                    href == restart_url,
                    f'重启后行内 href={href!r}（期望 {restart_url!r}）',
                )
                recorder.check(
                    'a01-restart-title',
                    restart_title in row.text,
                    f'重启后记录行包含标题 {restart_title!r}',
                )
                recorder.check(
                    'a01-restart-description',
                    restart_description in row.text,
                    f'重启后记录行包含描述 {restart_description!r}',
                )
            record = _get_record(second_client, recorder, restart_id, 'a01-restart')
            if record is not None:
                recorder.check(
                    'a01-restart-id',
                    _record_id(record) == restart_id,
                    f'重启后 JSON id={_record_id(record)!r}（期望 {restart_id!r}）',
                )
                recorder.check(
                    'a01-restart-url',
                    _record_url(record) == restart_url,
                    f'重启后 JSON url={_record_url(record)!r}（期望 {restart_url!r}）',
                )
                recorder.check(
                    'a01-restart-title-json',
                    _record_title(record) == restart_title,
                    f'重启后 JSON title={_record_title(record)!r}（期望 {restart_title!r}）',
                )
                recorder.check(
                    'a01-restart-description-json',
                    _record_description(record) == restart_description,
                    f'重启后 JSON description={_record_description(record)!r}（期望 {restart_description!r}）',
                )
        finally:
            if second_client is not None:
                second_client.close()
    finally:
        if second is not None:
            common.stop_app(second)


def _case_a02(args, recorder):
    client = common.HttpClient(args.base_url)
    token = uuid.uuid4().hex[:12]
    boundary = f'http://atlas-a02-{token}'
    boundary_title = f'A02 单标签主机 {token}'
    boundary_description = f'A02 原始字符串 {token}'
    invalid_values = [
        ('missing-scheme', f'{token}.example.com/no-scheme'),
        ('javascript-scheme', f'javascript:void({token})'),
        ('ftp-scheme', f'ftp://{token}.example.com/manual'),
        ('empty-host', 'http://'),
        ('space-in-hostname', f'http://{token}.exa mple.com/path'),
        ('illegal-hostname', f'http://{token}.example.com|invalid/'),
    ]
    try:
        _, form = _save_form_from_home(client, recorder, 'a02')
        if form is None:
            return
        fields = _form_fields(form, {
            'url': boundary,
            'title': boundary_title,
            'description': boundary_description,
        })
        response = client.post_form(
            _action_of(form), fields, follow_redirects=False, accept='text/html'
        )
        page = _follow_303(client, recorder, response, 'a02-boundary')
        if page is None:
            return
        doc = _parse_html(page.text)
        row = _row_for_url(doc, boundary)
        recorder.check(
            'a02-boundary-row',
            row is not None,
            f'单标签主机 URL={boundary!r} 出现在 HTML 列表',
        )
        record_id = row.record_id if row is not None else ''
        recorder.check(
            'a02-boundary-id',
            bool(record_id),
            f'单标签主机记录 data-record-id={record_id!r}',
        )
        if row is not None:
            link = _row_open_link(row)
            href = link.href if link is not None else None
            recorder.check(
                'a02-boundary-href',
                href == boundary,
                f'行内 href={href!r}（期望精确等于 {boundary!r}）',
            )
        if record_id:
            record = _get_record(client, recorder, record_id, 'a02-boundary')
            if record is not None:
                recorder.check(
                    'a02-boundary-json-url',
                    _record_url(record) == boundary,
                    f'JSON url={_record_url(record)!r}（期望原始字符串 {boundary!r}）',
                )
        # Independent JSON positive: not an HTML-created record read through JSON.
        before_json_ids = _record_ids(_fetch_bookmarks(client, recorder, 'a02-json-before-create'))
        json_boundary = f'https://atlas-a02-json-{token}/original?keep=1'
        positive = client.post_json('/api/bookmarks', {
            'url': json_boundary, 'title': f'A02 JSON {token}',
            'description': f'A02 JSON positive {token}',
        })
        recorder.expect_status(positive, 201, aid='a02-json-boundary-create-status')
        json_id = _record_id(_extract_record(_safe_json(positive)))
        recorder.check('a02-json-boundary-new-id', bool(json_id) and json_id not in before_json_ids,
                       f'独立 JSON POST 返回新的非空 id={json_id!r}')
        if json_id:
            saved = _get_record(client, recorder, json_id, 'a02-json-boundary')
            recorder.check('a02-json-boundary-readback',
                           _record_id(saved) == json_id and _record_url(saved) == json_boundary,
                           '独立 GET 读回同一 id 与精确原始 URL')
            listed_positive = _fetch_bookmarks(client, recorder, 'a02-json-positive')
            recorder.check('a02-json-boundary-listed', any(
                _record_id(item) == json_id and _record_url(item) == json_boundary
                for item in listed_positive), '列表包含同一 JSON 创建记录与原始 URL')
        before = _fetch_bookmarks(client, recorder, 'a02-before')
        before_total = len(before)
        before_token = sum(1 for item in before if token in (_record_url(item) or ''))
        for label, bad_url in invalid_values:
            bad_fields = _form_fields(form, {
                'url': bad_url,
                'title': f'A02 拒绝 {label}',
                'description': f'A02 保留输入 {label}',
            })
            html_response = client.post_form(
                _action_of(form), bad_fields, follow_redirects=False, accept='text/html'
            )
            recorder.expect_status(html_response, 400, aid=f'a02-html-{label}-status')
            error_doc = _parse_html(html_response.text)
            error_text = _form_error_text(error_doc)
            recorder.check(
                f'a02-html-{label}-form-error',
                bool(error_text),
                f'HTML 非法 URL 显示可读 form-error，实际 {error_text!r}',
            )
            error_form = error_doc.save_form()
            recorder.check(
                f'a02-html-{label}-form-present',
                error_form is not None,
                'HTML 错误页保留可重新提交的保存表单',
            )
            if error_form is not None:
                retained = error_form.value('url')
                recorder.check(
                    f'a02-html-{label}-retained',
                    retained == bad_url,
                    f'HTML 错误页保留 url={retained!r}（期望 {bad_url!r}）',
                )
            json_response = client.post_json('/api/bookmarks', {'url': bad_url})
            recorder.expect_status(json_response, 400, aid=f'a02-json-{label}-status')
            code = _error_code(json_response)
            recorder.check(
                f'a02-json-{label}-code',
                code == 'invalid_url',
                f'JSON 非法 URL 错误码={code!r}（期望 invalid_url）',
            )
        after = _fetch_bookmarks(client, recorder, 'a02-after')
        after_total = len(after)
        after_token = sum(1 for item in after if token in (_record_url(item) or ''))
        recorder.check(
            'a02-relative-count',
            after_total == before_total and after_token == before_token,
            f'非法提交前后记录数 {before_total}->{after_total}，标记记录数 {before_token}->{after_token}（不得新增）',
        )
        listed = {_record_url(item) for item in after}
        for label, bad_url in invalid_values:
            recorder.check(
                f'a02-{label}-absent',
                bad_url not in listed,
                f'被拒绝的 url={bad_url!r} 不出现在列表',
            )
    finally:
        client.close()


def _case_a03(args, recorder):
    if not recorder.check('a03-fresh-required-flags', bool(args.app_root and args.data_dir),
                          'A03 必须绑定同一应用源码 --app-root 与测试者 --data-dir'):
        return
    proc = None
    fresh_client = None
    try:
        try:
            proc = common.launch_app(args.app_root, args.data_dir, 0, fresh=True)
        except Exception as exc:
            recorder.check('a03-fresh-start', False,
                           f'无法启动独立 fresh 实例：{type(exc).__name__}: {exc}')
            return
        recorder.check('a03-fresh-owned-source',
                       os.path.realpath(proc.app_root) == os.path.realpath(args.app_root),
                       'fresh 实例来自与 base_url 相同的冻结应用源码根')
        fresh_client = common.HttpClient(proc.base_url)
        health = fresh_client.get('/api/health')
        recorder.expect_status(health, 200, aid='a03-fresh-health-status')
        categories = _fetch_categories(fresh_client, recorder, 'a03-fresh')
        names = _category_names(categories)
        for index, preset in enumerate(common.PRESET_CATEGORIES, 1):
            recorder.check(f'a03-fresh-api-preset-{index}', preset in names,
                           f'fresh 首次初始化 API 包含预置归类 {preset!r}；实际 {sorted(names)}')
        fresh_page = fresh_client.get('/', accept='text/html')
        recorder.expect_status(fresh_page, 200, aid='a03-fresh-home-status')
        fresh_doc = _parse_html(fresh_page.text)
        html_names = _category_values_in_html(fresh_doc)
        for index, preset in enumerate(common.PRESET_CATEGORIES, 1):
            recorder.check(f'a03-fresh-html-preset-{index}', preset in html_names,
                           f'fresh 首次初始化 HTML 包含预置归类 {preset!r}；实际 {sorted(html_names)}')
    finally:
        try:
            if fresh_client is not None:
                fresh_client.close()
        finally:
            if proc is not None:
                try:
                    common.stop_app(proc)
                except Exception as exc:
                    recorder.check('a03-fresh-cleanup', False, f'清理异常：{exc}')
                recorder.check('a03-fresh-process-stopped', proc.poll() is not None,
                               '本用例拥有的 fresh 子进程已结束')

    client = common.HttpClient(args.base_url)
    default_url = _unique_url('a03-default')
    default_title = f'A03 默认归类 {uuid.uuid4().hex[:8]}'
    new_name = f'自动归类-{uuid.uuid4().hex[:8]}'
    new_url = _unique_url('a03-newcat')
    new_title = f'A03 新归类 {uuid.uuid4().hex[:8]}'
    try:
        categories = _fetch_categories(client, recorder, 'a03')
        doc, form = _save_form_from_home(client, recorder, 'a03')
        if form is None:
            return
        omitted_fields = _form_fields(form, {
            'url': default_url,
            'title': default_title,
        }, omit=('category',))
        recorder.check(
            'a03-category-omitted',
            'category' not in omitted_fields,
            '真实保存表单省略 category 字段后提交',
        )
        response = client.post_form(
            _action_of(form), omitted_fields, follow_redirects=False, accept='text/html'
        )
        page = _follow_303(client, recorder, response, 'a03-default')
        if page is None:
            return
        default_doc = _parse_html(page.text)
        default_row = _row_for_url(default_doc, default_url)
        if not recorder.check(
            'a03-default-row',
            default_row is not None,
            f'省略归类保存后 HTML 列表出现 URL={default_url!r} 的记录行',
        ):
            return
        default_id = default_row.record_id
        recorder.check(
            'a03-default-id',
            bool(default_id),
            f'默认归类记录 id={default_id!r}',
        )
        record = _get_record(client, recorder, default_id, 'a03-default')
        if record is not None:
            actual_category = _category_name(record, categories)
            recorder.check(
                'a03-default-category',
                actual_category == common.DEFAULT_CATEGORY,
                f'省略 category 后 JSON 归类={actual_category!r}（期望 {common.DEFAULT_CATEGORY!r}）',
            )
        inbox = client.get(
            '/', params={'category': common.DEFAULT_CATEGORY}, accept='text/html'
        )
        recorder.expect_status(inbox, 200, aid='a03-inbox-status')
        inbox_doc = _parse_html(inbox.text)
        recorder.check(
            'a03-inbox-row',
            default_id is not None and default_id in {row.record_id for row in inbox_doc.rows},
            f'「{common.DEFAULT_CATEGORY}」过滤列表包含 id={default_id!r}',
        )
        new_fields = _form_fields(form, {
            'url': new_url,
            'title': new_title,
            'category': new_name,
        })
        response = client.post_form(
            _action_of(form), new_fields, follow_redirects=False, accept='text/html'
        )
        page = _follow_303(client, recorder, response, 'a03-newcat')
        if page is None:
            return
        new_doc = _parse_html(page.text)
        new_row = _row_for_url(new_doc, new_url)
        if not recorder.check(
            'a03-newcat-row',
            new_row is not None,
            f'新归类保存后 HTML 列表出现 URL={new_url!r} 的记录行',
        ):
            return
        new_id = new_row.record_id
        recorder.check('a03-newcat-id', bool(new_id), f'新归类记录 id={new_id!r}')
        refreshed = _fetch_categories(client, recorder, 'a03-refreshed')
        refreshed_names = _category_names(refreshed)
        recorder.check(
            'a03-newcat-created',
            new_name in refreshed_names,
            f'保存新归类名 {new_name!r} 后 /api/categories 自动创建；实际 {sorted(refreshed_names)}',
        )
        record = _get_record(client, recorder, new_id, 'a03-newcat')
        if record is not None:
            actual_category = _category_name(record, refreshed)
            recorder.check(
                'a03-newcat-json-category',
                actual_category == new_name,
                f'新归类记录 JSON 归类={actual_category!r}（期望 {new_name!r}）',
            )
        filtered = client.get('/', params={'category': new_name}, accept='text/html')
        recorder.expect_status(filtered, 200, aid='a03-newcat-filter-status')
        filtered_doc = _parse_html(filtered.text)
        recorder.check(
            'a03-newcat-filter',
            new_id is not None and new_id in {row.record_id for row in filtered_doc.rows},
            f'HTML 归类过滤 {new_name!r} 包含 id={new_id!r}',
        )
        api_filtered = _fetch_bookmarks(
            client, recorder, 'a03-newcat-api', params={'category': new_name}
        )
        recorder.check(
            'a03-newcat-api-filter',
            new_id is not None and new_id in _record_ids(api_filtered),
            f'API 归类过滤 {new_name!r} 包含 id={new_id!r}',
        )
    finally:
        client.close()




def _case_a11_base(args, recorder):
    client = common.HttpClient(args.base_url)
    unknown = f'不存在归类-{uuid.uuid4().hex[:10]}'
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a11-base-health-status')
        health_payload = _safe_json(health)
        recorder.check(
            'a11-base-health-json',
            isinstance(health_payload, dict) and bool(health_payload),
            f'/api/health 返回非空 JSON 对象，实际 {type(health_payload).__name__}',
        )
        page = client.get('/', accept='text/html')
        recorder.expect_status(page, 200, aid='a11-base-home-status')
        recorder.check(
            'a11-base-home-content-type',
            'text/html' in page.content_type.lower(),
            f'首页 Content-Type={page.content_type!r}',
        )
        doc = _parse_html(page.text)
        form = doc.save_form()
        recorder.check(
            'a11-base-entry-form',
            form is not None,
            '首页含 action=/bookmarks/new 且 method=post 的录入表单',
        )
        if form is not None:
            recorder.check(
                'a11-base-entry-action',
                _action_path(form.action) == '/bookmarks/new',
                f'录入表单 action={form.action!r}',
            )
            recorder.check(
                'a11-base-url-field',
                form.has_name('url'),
                '录入表单含 name=url 输入字段',
            )
        manager = next(
            (anchor for anchor in doc.anchors if anchor.testid == 'category-manager'),
            None,
        )
        manager_href = manager.href if manager is not None else None
        manager_path = ''
        if manager_href:
            try:
                manager_path = urllib.parse.urlsplit(manager_href).path.rstrip('/')
            except ValueError:
                manager_path = ''
        recorder.check(
            'a11-base-category-manager',
            manager is not None and manager_path == '/categories',
            f'首页 category-manager 链接 href={manager_href!r}（期望指向 /categories）',
        )
        recorder.check(
            'a11-base-list-container',
            _has_list_container(doc),
            '首页含记录列表容器',
        )
        empty_page = client.get('/', params={'category': unknown}, accept='text/html')
        recorder.expect_status(empty_page, 200, aid='a11-base-unknown-status')
        empty_doc = _parse_html(empty_page.text)
        recorder.check(
            'a11-base-unknown-filter-empty',
            len(empty_doc.rows) == 0,
            f'不存在归类 {unknown!r} 过滤后记录行数={len(empty_doc.rows)}（期望 0）',
        )
        marker = _empty_state_marker(empty_doc)
        recorder.check(
            'a11-base-unknown-empty-state',
            bool(marker),
            f'不存在归类过滤显示明确空状态，标记={marker!r}',
        )
    finally:
        client.close()


def _case_a11(args, recorder):
    # The base deployment may already contain records. Only fresh proves first init.
    if not recorder.check('a11-fresh-required-flags', bool(args.app_root and args.data_dir),
                          'A11 必须绑定实际冻结 app_root 与测试者 data_dir'):
        return
    _case_a11_base(args, recorder)
    proc = None
    client = None
    try:
        proc = common.launch_app(args.app_root, args.data_dir, 0, fresh=True)
        recorder.check('a11-fresh-owned-source',
                       os.path.realpath(proc.app_root) == os.path.realpath(args.app_root),
                       'fresh 实例来自同一冻结交付源码')
        client = common.HttpClient(proc.base_url)
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a11-fresh-health-status')
        recorder.check('a11-fresh-health-json', isinstance(_safe_json(health), dict),
                       'fresh 健康检查返回 JSON 对象')
        # No business write precedes these unfiltered observations.
        for name, params in (('active', None), ('including-trash', {'include_trashed': '1'})):
            records = _fetch_bookmarks(client, recorder, f'a11-fresh-{name}', params)
            recorder.check(f'a11-fresh-{name}-empty', records == [],
                           f'未过滤全库 {name} 记录数={len(records)}，首次初始化必须为0')
        categories = _fetch_categories(client, recorder, 'a11-fresh')
        ids = []
        for index, preset in enumerate(common.PRESET_CATEGORIES, 1):
            matches = [item for item in categories if isinstance(item, dict) and item.get('name') == preset]
            recorder.check(f'a11-fresh-preset-{index}', len(matches) == 1,
                           f'首次初始化准确存在预置分类 {preset!r}')
            if len(matches) == 1:
                item = matches[0]
                cid = item.get('id')
                legal = isinstance(cid, (str, int)) and not isinstance(cid, bool) and bool(str(cid).strip())
                recorder.check(f'a11-fresh-preset-{index}-id', legal, f'分类 ID={cid!r}')
                recorder.check(f'a11-fresh-preset-{index}-count', item.get('count') == 0,
                               f'预置分类活动记录 count={item.get("count")!r}')
                ids.append(str(cid))
        recorder.check('a11-fresh-preset-unique-ids', len(ids) == 4 and len(set(ids)) == 4,
                       '四个预置分类 ID 各自唯一')
        page = client.get('/', accept='text/html')
        recorder.expect_status(page, 200, aid='a11-fresh-home-status')
        recorder.check('a11-fresh-home-content-type', 'text/html' in page.content_type.lower(),
                       '未过滤首页是 HTML')
        doc = _parse_html(page.text)
        form = doc.save_form()
        recorder.check('a11-fresh-save-form', form is not None and
                       _action_path(form.action) == '/bookmarks/new' and form.has_name('url'),
                       '未过滤首页具备保存表单与 URL 字段')
        recorder.check('a11-fresh-category-entry', any(
            a.testid == 'category-manager' and _action_path(a.href) == '/categories'
            for a in doc.anchors), '未过滤首页有分类管理入口')
        recorder.check('a11-fresh-list-container', _has_list_container(doc), '未过滤首页有列表容器')
        recorder.check('a11-fresh-no-record-rows', not doc.rows, '首次初始化未过滤首页没有记录行')
        recorder.check('a11-fresh-explicit-empty-state', bool(_empty_state_marker(doc)),
                       '首次初始化未过滤首页有明确空状态')
    finally:
        try:
            if client is not None:
                client.close()
        finally:
            if proc is not None:
                try:
                    common.stop_app(proc)
                except Exception as exc:
                    recorder.check('a11-fresh-cleanup', False, f'清理异常：{exc}')
                recorder.check('a11-fresh-process-stopped', proc.poll() is not None,
                               '本用例拥有的 fresh 子进程已结束')

_HANDLERS = {
    'A01': _case_a01,
    'A02': _case_a02,
    'A03': _case_a03,
    'A11': _case_a11,
}


def main(argv=None):
    try:
        args = common.parse_case_args(argv)
    except SystemExit as exc:
        raw_args = list(sys.argv[1:] if argv is None else argv)
        requested_case = next((case for case in ('A03', 'A11') if f'--case={case}' in raw_args or any(
            value == '--case' and index + 1 < len(raw_args) and raw_args[index + 1] == case
            for index, value in enumerate(raw_args))), None)
        if not exc.code or requested_case is None:
            raise
        failed = common.Recorder(requested_case)
        failed.check(f'{requested_case.lower()}-fresh-arguments', False,
                     f'{requested_case} 参数无效；详见 stderr，不降级或跳过')
        return failed.finish(requested_case)
    recorder = common.Recorder(args.case)
    handler = _HANDLERS.get(args.case)
    if handler is None:
        recorder.check(
            'dispatch',
            False,
            f'acceptance/p0_library.py 不实现用例 {args.case}（应由其他程序派发）',
        )
    else:
        try:
            handler(args, recorder)
        except common.AcceptanceError as exc:
            recorder.check('infrastructure', False, f'验收基础设施错误：{exc}')
        except Exception as exc:
            recorder.check(
                'unexpected-error',
                False,
                f'未预期错误：{type(exc).__name__}: {exc}',
            )
    return recorder.finish(args.case)


if __name__ == '__main__':
    sys.exit(main())
