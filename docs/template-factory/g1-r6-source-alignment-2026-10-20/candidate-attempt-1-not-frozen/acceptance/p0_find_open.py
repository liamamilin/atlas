#!/usr/bin/env python3
'''P0 行为验收组：关键字检索与打开原页。

覆盖 A07、A08。A07 先保留 JSON 检索断言，再通过真实 category-search-form
在归类间提交同一关键字并验证空结果；A08 通过真实保存表单创建带查询串的
记录，检查打开链接属性、urljoin 解析目标与 /go 302。仅使用 Python 3.12
标准库并复用 acceptance/common.py：以 --case 派发，未知用例显式失败；
每个用例对真实目标执行正向与硬负向行为断言，向 stdout 输出单个
atlas.acceptance-result.v1 JSON，失败时以非零码退出。
'''

from __future__ import annotations

import os
import sys
import uuid
from html.parser import HTMLParser
from urllib.parse import quote, urljoin, urlsplit

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import common


_VOID_TAGS = frozenset({
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
    'link', 'meta', 'param', 'source', 'track', 'wbr',
})
_EMPTY_MARKERS = (
    '无匹配', '没有匹配', '没有找到', '未找到', '暂无', '没有记录',
    '空结果', 'no results', 'no matching', 'no bookmarks', 'nothing here', 'empty',
)


def _normalize_space(value):
    return ' '.join(str(value or '').split())


class _Field:
    def __init__(self, attrs):
        self.name = attrs.get('name')
        self.value = attrs.get('value', '')
        self.type = (attrs.get('type') or 'text').lower()
        self.checked = 'checked' in attrs


class _Option:
    def __init__(self, attrs):
        self.value = attrs.get('value')
        self.text = ''
        self.selected = 'selected' in attrs

    def resolved_value(self):
        if self.value is not None:
            return self.value
        return self.text.strip()


class _Select:
    def __init__(self, attrs):
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
        self.name = attrs.get('name')
        self.text = ''


class _Form:
    def __init__(self, attrs):
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
        self.href = attrs.get('href') or ''
        self.testid = attrs.get('data-testid') or ''
        self.target = attrs.get('target') or ''
        self.rel = attrs.get('rel') or ''
        self.text = ''


class _Row:
    def __init__(self, attrs):
        self.record_id = attrs.get('data-record-id') or ''
        self.anchors = []
        self.text = ''


class _Document:
    def __init__(self):
        self.forms = []
        self.anchors = []
        self.rows = []
        self.testids = []
        self.text = ''

    def save_form(self):
        for form in self.forms:
            if form.method == 'post' and _action_path(form.action) == '/bookmarks/new':
                return form
        for form in self.forms:
            if form.method == 'post' and form.has_name('url'):
                return form
        return None

    def search_form(self):
        for form in self.forms:
            if form.testid == 'category-search-form':
                return form
        for form in self.forms:
            if form.method == 'get' and form.has_name('category') and form.has_name('q'):
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
        testid = attributes.get('data-testid') or ''
        if testid:
            entry = {'attrs': attributes, 'text': ''}
            self.doc.testids.append(entry)
            if tag not in _VOID_TAGS:
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
        elif tag == 'tr' and (attributes.get('data-record-id') or testid == 'record-row'):
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
        if tag in _VOID_TAGS:
            return
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


def _action_path(action):
    text = (action or '').strip()
    if not text:
        return ''
    try:
        path = urlsplit(text).path
    except ValueError:
        return text
    if not path:
        return ''
    if not path.startswith('/'):
        path = '/' + path
    return path.rstrip('/') or '/'


def _form_path(form, default):
    return (form.action or '').strip() or default


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
    for key, value in (overrides or {}).items():
        fields[str(key)] = str(value)
    for name in omit:
        fields.pop(name, None)
    return fields


def _row_for_url(doc, url):
    for row in doc.rows:
        if any(anchor.testid == 'record-open-link' and anchor.href == url for anchor in row.anchors):
            return row
    for row in doc.rows:
        if any(anchor.href == url for anchor in row.anchors):
            return row
    return None


def _row_ids(doc):
    return {row.record_id for row in doc.rows if row.record_id}


def _empty_state_text(doc):
    for entry in doc.testids:
        testid = (entry['attrs'].get('data-testid') or '').lower()
        if 'empty' in testid:
            text = _normalize_space(entry['text'])
            if text:
                return text
    text = _normalize_space(doc.text)
    folded = text.casefold()
    for marker in _EMPTY_MARKERS:
        if marker.casefold() in folded:
            return marker
    return ''


def _html_search(client, recorder, aid, form, category, query):
    fields = _form_fields(form, {'category': category, 'q': query})
    response = client.get(_form_path(form, '/'), params=fields, accept='text/html')
    recorder.expect_status(response, 200, aid=f'{aid}-status')
    recorder.check(
        f'{aid}-content-type',
        'text/html' in response.content_type.lower(),
        f'GET 搜索页 Content-Type={response.content_type!r}',
    )
    doc = _parse_html(response.text)
    result_form = doc.search_form()
    recorder.check(f'{aid}-form', result_form is not None, '搜索页保留 category-search-form')
    retained_category = None
    retained_query = None
    if result_form is not None:
        retained_category = result_form.value('category')
        retained_query = result_form.value('q')
        recorder.check(
            f'{aid}-category-retained',
            retained_category == category,
            f'搜索表单 category={retained_category!r}（期望 {category!r}）',
        )
        recorder.check(
            f'{aid}-query-retained',
            retained_query == query,
            f'搜索表单 q={retained_query!r}（期望 {query!r}）',
        )
    text = _normalize_space(doc.text)
    recorder.check(
        f'{aid}-category-visible',
        category in text or retained_category == category,
        f'结果页显示所选归类 {category!r}（表单保留值 {retained_category!r}）',
    )
    recorder.check(
        f'{aid}-query-visible',
        query in text or retained_query == query,
        f'结果页显示查询 {query!r}（表单保留值 {retained_query!r}）',
    )
    return doc


def _unique_url(tag):
    token = f'{tag}-{uuid.uuid4().hex[:12]}'
    return f'https://{token}.atlas-acceptance.example/{token}'


def _unique_category(tag):
    return f'atlas-{tag}-{uuid.uuid4().hex[:10]}'


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


def _record_id(record):
    if isinstance(record, dict) and record.get('id') is not None:
        return str(record['id'])
    return None


def _record_url(record):
    if isinstance(record, dict) and record.get('url') is not None:
        return str(record['url'])
    return None


def _record_ids(records):
    return {item_id for item_id in (_record_id(record) for record in records) if item_id}


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


def _extract_list(payload, keys):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return None


def _bookmark_path(bookmark_id):
    return '/api/bookmarks/' + quote(str(bookmark_id), safe='')


def _go_path(bookmark_id):
    return '/go/' + quote(str(bookmark_id), safe='')


def _search(client, recorder, aid, params):
    response = client.get('/api/bookmarks', params=params)
    recorder.expect_status(response, 200, aid=f'{aid}-status')
    payload = _safe_json(response)
    records = _extract_list(payload, ('bookmarks', 'items', 'data', 'records'))
    recorder.check(
        f'{aid}-shape',
        isinstance(records, list),
        f'GET /api/bookmarks 必须返回 JSON 数组，实际 {type(payload).__name__}',
    )
    return records if isinstance(records, list) else []


def _case_a07(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a07-health-status')

        cat_a = _unique_category('a07a')
        cat_b = _unique_category('a07b')
        shared = f'shared{uuid.uuid4().hex[:12]}'
        host_token = f'host{uuid.uuid4().hex[:12]}'
        desc_token = f'descr{uuid.uuid4().hex[:12]}'
        unmatched = f'absent{uuid.uuid4().hex[:12]}'

        url_a = f'https://{host_token}.atlas-acceptance.example/notes/{uuid.uuid4().hex[:10]}'
        title_a = f'{shared} 收藏甲'
        desc_a = f'备注 {desc_token}'
        created_a = client.post_json(
            '/api/bookmarks',
            {'url': url_a, 'title': title_a, 'description': desc_a, 'category': cat_a},
        )
        recorder.expect_status(created_a, 201, aid='a07-create-a-status')
        id_a = _record_id(_extract_record(_safe_json(created_a)))
        recorder.check('a07-create-a-id', bool(id_a), f'创建记录甲返回 id={id_a!r}')

        url_b = _unique_url('a07b')
        title_b = f'{shared} 收藏乙'
        created_b = client.post_json('/api/bookmarks', {'url': url_b, 'title': title_b, 'category': cat_b})
        recorder.expect_status(created_b, 201, aid='a07-create-b-status')
        id_b = _record_id(_extract_record(_safe_json(created_b)))
        recorder.check('a07-create-b-id', bool(id_b), f'创建记录乙返回 id={id_b!r}')

        if not (id_a and id_b):
            return

        by_title = _search(client, recorder, 'a07-title', {'q': shared})
        title_ids = _record_ids(by_title)
        recorder.check('a07-title-hit-a', id_a in title_ids, f'标题片段 {shared!r} 命中记录甲：{sorted(title_ids)}')
        recorder.check('a07-title-hit-b', id_b in title_ids, f'标题片段 {shared!r} 命中记录乙：{sorted(title_ids)}')

        upper_title = shared.upper()
        by_title_upper = _search(client, recorder, 'a07-title-case', {'q': upper_title})
        recorder.check(
            'a07-title-case-insensitive',
            id_a in _record_ids(by_title_upper),
            f'大写标题片段 {upper_title!r} 命中记录甲（大小写不敏感）',
        )

        by_host = _search(client, recorder, 'a07-domain', {'q': host_token})
        host_ids = _record_ids(by_host)
        recorder.check('a07-domain-hit', id_a in host_ids, f'域名片段 {host_token!r} 命中记录甲：{sorted(host_ids)}')
        recorder.check('a07-domain-excludes-b', id_b not in host_ids, '域名检索不命中域名不同的记录乙')

        by_host_upper = _search(client, recorder, 'a07-domain-case', {'q': host_token.upper()})
        recorder.check(
            'a07-domain-case-insensitive',
            id_a in _record_ids(by_host_upper),
            f'大写域名片段 {host_token.upper()!r} 命中记录甲（大小写不敏感）',
        )

        by_desc = _search(client, recorder, 'a07-description', {'q': desc_token})
        desc_ids = _record_ids(by_desc)
        recorder.check('a07-description-hit', id_a in desc_ids, f'描述片段 {desc_token!r} 命中记录甲：{sorted(desc_ids)}')
        recorder.check('a07-description-excludes-b', id_b not in desc_ids, '描述检索不命中无该描述的记录乙')

        by_desc_upper = _search(client, recorder, 'a07-description-case', {'q': desc_token.upper()})
        recorder.check(
            'a07-description-case-insensitive',
            id_a in _record_ids(by_desc_upper),
            f'大写描述片段 {desc_token.upper()!r} 命中记录甲（大小写不敏感）',
        )

        combined_a = _search(client, recorder, 'a07-combined-a', {'category': cat_a, 'q': shared})
        combined_a_ids = _record_ids(combined_a)
        recorder.check('a07-combined-a-includes', id_a in combined_a_ids, f'category={cat_a!r} 与 q={shared!r} 叠加命中记录甲')
        recorder.check('a07-combined-a-excludes-b', id_b not in combined_a_ids, f'category={cat_a!r} 叠加过滤排除属于 {cat_b!r} 的记录乙')

        combined_b = _search(client, recorder, 'a07-combined-b', {'category': cat_b, 'q': shared})
        combined_b_ids = _record_ids(combined_b)
        recorder.check('a07-combined-b-includes', id_b in combined_b_ids, f'category={cat_b!r} 与 q={shared!r} 叠加命中记录乙')
        recorder.check('a07-combined-b-excludes-a', id_a not in combined_b_ids, f'category={cat_b!r} 叠加过滤排除属于 {cat_a!r} 的记录甲')

        empty = _search(client, recorder, 'a07-no-match', {'q': unmatched})
        recorder.check('a07-no-match-empty', empty == [], f'无匹配关键字 {unmatched!r} 返回 200 空数组，实际 {len(empty)} 条')

        home = client.get('/', accept='text/html')
        recorder.expect_status(home, 200, aid='a07-home-status')
        recorder.check(
            'a07-home-content-type',
            'text/html' in home.content_type.lower(),
            f'GET / Content-Type={home.content_type!r}',
        )
        home_doc = _parse_html(home.text)
        search_form = home_doc.search_form()
        if not recorder.check(
            'a07-search-form',
            search_form is not None,
            '首页含 form[data-testid=category-search-form]（category 与 q）',
        ):
            return
        if not recorder.check(
            'a07-search-fields',
            search_form.has_name('category') and search_form.has_name('q'),
            'category-search-form 同时含 category 与 q 字段',
        ):
            return
        recorder.check(
            'a07-search-method',
            search_form.method == 'get',
            f'category-search-form method={search_form.method!r}（期望 get）',
        )
        action = _form_path(search_form, '/')
        recorder.check(
            'a07-search-action',
            _action_path(action) == '/',
            f'category-search-form action={action!r}（期望 GET /）',
        )

        doc_a = _html_search(client, recorder, 'a07-html-a', search_form, cat_a, shared)
        ids_a = _row_ids(doc_a)
        recorder.check(
            'a07-html-a-hit',
            id_a in ids_a,
            f'归类 {cat_a!r} 中 q={shared!r} 命中记录甲：{sorted(ids_a)}',
        )
        recorder.check(
            'a07-html-a-excludes-b',
            id_b not in ids_a,
            f'归类 {cat_a!r} 的搜索结果排除记录乙：{sorted(ids_a)}',
        )

        doc_b = _html_search(client, recorder, 'a07-html-b', search_form, cat_b, shared)
        ids_b = _row_ids(doc_b)
        recorder.check(
            'a07-html-b-hit',
            id_b in ids_b,
            f'归类 {cat_b!r} 中 q={shared!r} 命中记录乙：{sorted(ids_b)}',
        )
        recorder.check(
            'a07-html-b-excludes-a',
            id_a not in ids_b,
            f'归类 {cat_b!r} 的搜索结果排除记录甲：{sorted(ids_b)}',
        )

        doc_empty = _html_search(client, recorder, 'a07-html-empty', search_form, cat_a, unmatched)
        empty_ids = _row_ids(doc_empty)
        recorder.check(
            'a07-html-empty-no-rows',
            not empty_ids,
            f'归类 {cat_a!r} 中 q={unmatched!r} 无记录行，实际 {sorted(empty_ids)}',
        )
        empty_text = _empty_state_text(doc_empty)
        recorder.check(
            'a07-html-empty-marker',
            bool(empty_text),
            f'无匹配时显示明确空结果，实际 {empty_text!r}',
        )
    finally:
        client.close()


def _case_a08(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a08-health-status')

        host_token = f'open{uuid.uuid4().hex[:12]}'
        path_token = uuid.uuid4().hex[:12]
        target_url = f'https://{host_token}.atlas-acceptance.example/page/{path_token}?src=atlas&n=7'
        home = client.get('/', accept='text/html')
        recorder.expect_status(home, 200, aid='a08-home-status')
        recorder.check(
            'a08-home-content-type',
            'text/html' in home.content_type.lower(),
            f'GET / Content-Type={home.content_type!r}',
        )
        home_doc = _parse_html(home.text)
        save_form = home_doc.save_form()
        if not recorder.check(
            'a08-save-form',
            save_form is not None,
            '首页含真实保存表单 form[action=/bookmarks/new]',
        ):
            return
        if not recorder.check(
            'a08-save-url-field',
            save_form.has_name('url'),
            '保存表单含 name=url',
        ):
            return
        save_action = _form_path(save_form, '/bookmarks/new')
        recorder.check(
            'a08-save-method',
            save_form.method == 'post',
            f'保存表单 method={save_form.method!r}（期望 post）',
        )
        recorder.check(
            'a08-save-action',
            _action_path(save_action) == '/bookmarks/new',
            f'保存表单 action={save_action!r}（期望 POST /bookmarks/new）',
        )
        saved = client.post_form(
            save_action,
            _form_fields(save_form, {'url': target_url, 'title': 'A08 打开原页'}),
            follow_redirects=False,
            accept='text/html',
        )
        recorder.expect_status(saved, 303, aid='a08-create-status')
        saved_location = saved.location
        if not recorder.check(
            'a08-create-location',
            bool(saved_location),
            f'保存成功 303 必须带 Location，实际 {saved_location!r}',
        ):
            return
        page = client.get(saved_location, accept='text/html')
        recorder.expect_status(page, 200, aid='a08-create-follow-status')
        page_doc = _parse_html(page.text)
        row = _row_for_url(page_doc, target_url)
        if not recorder.check(
            'a08-record-row',
            row is not None,
            f'保存后列表含 tr[data-record-id] 且打开链接 href={target_url!r}',
        ):
            return
        record_id = row.record_id
        if not recorder.check(
            'a08-create-id',
            bool(record_id),
            f'tr[data-record-id] 的 data-record-id={record_id!r}',
        ):
            return
        open_link = None
        for anchor in row.anchors:
            if anchor.testid == 'record-open-link':
                open_link = anchor
                break
        if not recorder.check(
            'a08-open-link',
            open_link is not None,
            '记录行内含 a[data-testid=record-open-link]',
        ):
            return
        recorder.check(
            'a08-link-href',
            open_link.href == target_url,
            f'打开链接 href={open_link.href!r}（期望原始 URL {target_url!r}）',
        )
        recorder.check(
            'a08-link-target',
            open_link.target == '_blank',
            f'打开链接 target={open_link.target!r}（期望 _blank）',
        )
        rel_tokens = {token.strip().lower() for token in open_link.rel.split() if token.strip()}
        recorder.check(
            'a08-link-rel',
            'noopener' in rel_tokens,
            f'打开链接 rel={open_link.rel!r} 含 noopener',
        )
        resolved_target = urljoin(client.base_url + '/', open_link.href)
        recorder.check(
            'a08-link-resolved-target',
            resolved_target == target_url,
            f'urljoin 解析 href 得到 {resolved_target!r}（期望 {target_url!r}）',
        )

        if record_id:
            opened = client.get(_go_path(record_id), follow_redirects=False)
            recorder.expect_status(opened, 302, aid='a08-open-status')
            location = opened.location
            recorder.check('a08-open-location-present', bool(location), f'302 响应携带 Location 头：{location!r}')
            recorder.check(
                'a08-open-location',
                location == target_url,
                f'GET /go/{{id}} Location={location!r}（期望保存时 URL {target_url!r}）',
            )

        unknown = f'no-such-{uuid.uuid4().hex[:12]}'
        missing = client.get(_go_path(unknown), follow_redirects=False)
        recorder.expect_status(missing, 404, aid='a08-unknown-status')
        code = _error_code(missing)
        recorder.check('a08-unknown-code', code == 'not_found', f'未知 id 打开错误码={code!r}（期望 not_found）')

        if record_id:
            fetched = client.get(_bookmark_path(record_id))
            recorder.expect_status(fetched, 200, aid='a08-readback-status')
            stored = _extract_record(_safe_json(fetched))
            recorder.check(
                'a08-url-unchanged',
                _record_url(stored) == target_url,
                f'打开动作后记录 url={_record_url(stored)!r}（未被改写，期望 {target_url!r}）',
            )
    finally:
        client.close()


_HANDLERS = {
    'A07': _case_a07,
    'A08': _case_a08,
}


def main(argv=None):
    args = common.parse_case_args(argv)
    recorder = common.Recorder(args.case)
    handler = _HANDLERS.get(args.case)
    if handler is None:
        recorder.check(
            'dispatch',
            False,
            f'acceptance/p0_find_open.py 不实现用例 {args.case}（应由其他程序派发）',
        )
    else:
        try:
            handler(args, recorder)
        except common.AcceptanceError as exc:
            recorder.check('infrastructure', False, f'验收基础设施错误：{exc}')
        except Exception as exc:
            recorder.check('unexpected-error', False, f'未预期错误：{type(exc).__name__}: {exc}')
    return recorder.finish(args.case)


if __name__ == '__main__':
    sys.exit(main())
