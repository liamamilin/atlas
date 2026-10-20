#!/usr/bin/env python3
'''P0 行为验收组：保存、校验、默认收件箱、启动外壳。

覆盖 A01、A02、A03、A11。仅使用 Python 3.12 标准库并复用
acceptance/common.py：以 --case 派发，未知用例显式失败；每个用例对真实
目标执行正向与硬负向行为断言，向 stdout 输出单个
atlas.acceptance-result.v1 JSON，失败时以非零码退出。
'''

from __future__ import annotations

import os
import re
import sys
import uuid
from urllib.parse import quote

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import common

_ENTRY_FORM_RE = re.compile(r'<form\b[^>]*\baction\s*=\s*[\x22\x27]?/bookmarks/new\b', re.IGNORECASE)
_URL_FIELD_RE = re.compile(r'<input\b[^>]*\bname\s*=\s*[\x22\x27]?url\b', re.IGNORECASE)
_LIST_CONTAINER_RE = re.compile(
    r'<ul\b|<ol\b'
    r'|<(?:div|main|section|article|aside)\b[^>]*\b(?:id|class)\s*=\s*[\x22\x27][^\x22\x27]*'
    r'(?:bookmarks?|lists?|records?)\b',
    re.IGNORECASE,
)


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


def _record_id(record):
    if isinstance(record, dict) and record.get('id') is not None:
        return str(record['id'])
    return None


def _record_url(record):
    if isinstance(record, dict) and record.get('url') is not None:
        return str(record['url'])
    return None


def _bookmark_path(bookmark_id):
    return '/api/bookmarks/' + quote(str(bookmark_id), safe='')


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


def _record_ids(records):
    return {_record_id(record) for record in records}


def _case_a01(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a01-health-status')

        live_url = _unique_url('a01-live')
        created = client.post_json('/api/bookmarks', {'url': live_url, 'title': 'A01 存活往返'})
        recorder.expect_status(created, 201, aid='a01-base-save-status')
        base_id = _record_id(_extract_record(_safe_json(created)))
        recorder.check('a01-base-save-id', bool(base_id), f'保存返回 id={base_id!r}')
        if base_id:
            fetched = client.get(_bookmark_path(base_id))
            recorder.expect_status(fetched, 200, aid='a01-base-readback-status')
            stored = _extract_record(_safe_json(fetched))
            recorder.check(
                'a01-base-readback-url',
                _record_url(stored) == live_url,
                f'读回 url={_record_url(stored)!r}（期望 {live_url!r}）',
            )
    finally:
        client.close()

    first = common.launch_app(args.app_root, args.data_dir, 0)
    instance_dir = first.instance_dir
    persisted_id = None
    persisted_url = None
    try:
        instance = common.HttpClient(first.base_url)
        try:
            persisted_url = _unique_url('a01-restart')
            response = instance.post_json(
                '/api/bookmarks', {'url': persisted_url, 'title': 'A01 重启持久化'}
            )
            recorder.expect_status(response, 201, aid='a01-instance-save-status')
            persisted_id = _record_id(_extract_record(_safe_json(response)))
            recorder.check(
                'a01-instance-save-id',
                bool(persisted_id),
                f'隔离实例保存返回 id={persisted_id!r}',
            )
        finally:
            instance.close()
    finally:
        common.stop_app(first)

    if not persisted_id:
        recorder.check('a01-restart-readback', False, '隔离实例未返回可用 id，无法验证重启持久化')
        return

    second = common.launch_app(args.app_root, args.data_dir, 0, instance_dir=instance_dir)
    try:
        reopened = common.HttpClient(second.base_url)
        try:
            again = reopened.get(_bookmark_path(persisted_id))
            recorder.expect_status(again, 200, aid='a01-restart-readback-status')
            restored = _extract_record(_safe_json(again))
            recorder.check(
                'a01-restart-id',
                _record_id(restored) == persisted_id,
                f'重启后 id={_record_id(restored)!r}（期望 {persisted_id!r}）',
            )
            recorder.check(
                'a01-restart-url',
                _record_url(restored) == persisted_url,
                f'重启后 url={_record_url(restored)!r}（期望 {persisted_url!r}）',
            )
        finally:
            reopened.close()
    finally:
        common.stop_app(second)


def _case_a02(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        token = f'atlas-a02-{uuid.uuid4().hex[:12]}'
        candidates = [
            ('missing-scheme', f'example.com/{token}'),
            ('javascript-scheme', f'javascript:void("{token}")'),
            ('ftp-scheme', f'ftp://{token}.example.com/manual'),
            ('dotless-host', f'http://{token}'),
        ]
        before = _fetch_bookmarks(client, recorder, 'a02-before')
        token_before = sum(1 for record in before if token in (_record_url(record) or ''))
        for label, bad_url in candidates:
            response = client.post_json('/api/bookmarks', {'url': bad_url})
            recorder.expect_status(response, 400, aid=f'a02-{label}-status')
            code = _error_code(response)
            recorder.check(
                f'a02-{label}-code',
                code == 'invalid_url',
                f'POST url={bad_url!r} 错误码={code!r}（期望 invalid_url）',
            )
        after = _fetch_bookmarks(client, recorder, 'a02-after')
        token_after = sum(1 for record in after if token in (_record_url(record) or ''))
        recorder.check(
            'a02-relative-count',
            token_after == token_before,
            f'含唯一标记 {token} 的记录数 {token_before} -> {token_after}（不得新增）',
        )
        listed = {_record_url(record) for record in after}
        for label, bad_url in candidates:
            recorder.check(
                f'a02-{label}-absent',
                bad_url not in listed,
                f'被拒绝的 url={bad_url!r} 未出现在列表中',
            )
    finally:
        client.close()


def _case_a03(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        categories = _fetch_categories(client, recorder, 'a03')
        preset_names = _category_names(categories)
        for preset in common.PRESET_CATEGORIES:
            recorder.check(
                f'a03-preset-{preset}',
                preset in preset_names,
                f'预置归类 {preset!r} 可见：{sorted(preset_names)}',
            )

        default_url = _unique_url('a03-default')
        default_response = client.post_json('/api/bookmarks', {'url': default_url})
        recorder.expect_status(default_response, 201, aid='a03-default-save-status')
        default_id = _record_id(_extract_record(_safe_json(default_response)))
        recorder.check('a03-default-save-id', bool(default_id), f'缺省归类保存返回 id={default_id!r}')
        if default_id:
            inbox = _fetch_bookmarks(
                client, recorder, 'a03-inbox', params={'category': common.DEFAULT_CATEGORY}
            )
            recorder.check(
                'a03-default-inbox',
                default_id in _record_ids(inbox),
                f'记录 {default_id!r} 出现在「{common.DEFAULT_CATEGORY}」归类中',
            )

        new_name = f'自动归类-{uuid.uuid4().hex[:8]}'
        new_url = _unique_url('a03-newcat')
        new_response = client.post_json('/api/bookmarks', {'url': new_url, 'category': new_name})
        recorder.expect_status(new_response, 201, aid='a03-newcat-save-status')
        new_id = _record_id(_extract_record(_safe_json(new_response)))
        recorder.check('a03-newcat-save-id', bool(new_id), f'新归类保存返回 id={new_id!r}')

        refreshed = _fetch_categories(client, recorder, 'a03-refreshed')
        recorder.check(
            'a03-newcat-created',
            new_name in _category_names(refreshed),
            f'保存 {new_name!r} 后归类被自动创建：{sorted(_category_names(refreshed))}',
        )
        if new_id:
            filtered = _fetch_bookmarks(
                client, recorder, 'a03-newcat-filter', params={'category': new_name}
            )
            recorder.check(
                'a03-newcat-filter',
                new_id in _record_ids(filtered),
                f'记录 {new_id!r} 可按归类 {new_name!r} 检索到',
            )
    finally:
        client.close()


def _case_a11(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a11-health-status')
        payload = _safe_json(health)
        recorder.check(
            'a11-health-json',
            isinstance(payload, dict),
            f'/api/health 返回 JSON 对象，实际 {type(payload).__name__}',
        )

        page = client.get('/', accept='text/html')
        recorder.expect_status(page, 200, aid='a11-home-status')
        recorder.check(
            'a11-home-content-type',
            'text/html' in page.content_type.lower(),
            f'首页 Content-Type={page.content_type!r}',
        )
        body = page.text
        recorder.check(
            'a11-entry-form',
            bool(_ENTRY_FORM_RE.search(body)),
            '首页含 action=/bookmarks/new 的录入表单',
        )
        recorder.check(
            'a11-url-field',
            bool(_URL_FIELD_RE.search(body)),
            '录入表单含 name=url 输入字段',
        )
        recorder.check(
            'a11-list-container',
            bool(_LIST_CONTAINER_RE.search(body)),
            '首页含记录列表容器',
        )
    finally:
        client.close()


_HANDLERS = {
    'A01': _case_a01,
    'A02': _case_a02,
    'A03': _case_a03,
    'A11': _case_a11,
}


def main(argv=None):
    args = common.parse_case_args(argv)
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
            recorder.check('unexpected-error', False, f'未预期错误：{type(exc).__name__}: {exc}')
    return recorder.finish(args.case)


if __name__ == '__main__':
    sys.exit(main())
