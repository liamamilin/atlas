#!/usr/bin/env python3
'''P0 行为验收组：归类管理、记录移动、归类浏览与非法归类。

覆盖 A04、A05、A06、A12。仅使用 Python 3.12 标准库并复用
acceptance/common.py：以 --case 派发，未知用例显式失败；每个用例对真实
目标执行正向与硬负向行为断言，向 stdout 输出单个
atlas.acceptance-result.v1 JSON，失败时以非零码退出。
'''

from __future__ import annotations

import os
import sys
import uuid
from urllib.parse import quote

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import common

_SUCCESS_STATUSES = (200, 204)


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
        for key in ('category', 'bookmark', 'record', 'data', 'item'):
            value = payload.get(key)
            if isinstance(value, dict):
                return value
        return payload
    return None


def _record_id(record):
    if isinstance(record, dict) and record.get('id') is not None:
        return str(record['id'])
    return None


def _record_category_name(record):
    if isinstance(record, dict):
        for key in ('category', 'category_name'):
            value = record.get(key)
            if isinstance(value, str) and value:
                return value
            if isinstance(value, dict) and value.get('name'):
                return str(value['name'])
    return None


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


def _move_path(bookmark_id):
    return _bookmark_path(bookmark_id) + '/move'


def _category_path(category_id):
    return '/api/categories/' + quote(str(category_id), safe='')


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


def _category_ids(categories):
    ids = set()
    for item in categories:
        item_id = _record_id(item)
        if item_id:
            ids.add(item_id)
    return ids


def _find_category(categories, name):
    target = str(name).casefold()
    for item in categories:
        if isinstance(item, dict) and item.get('name') is not None:
            if str(item['name']).casefold() == target:
                return item
    return None


def _default_category(categories):
    for item in categories:
        if isinstance(item, dict) and item.get('is_default'):
            return item
    return _find_category(categories, common.DEFAULT_CATEGORY)


def _record_ids(records):
    return {item_id for item_id in (_record_id(record) for record in records) if item_id}


def _create_record(client, recorder, aid, category=None, title=None):
    url = _unique_url(aid)
    payload = {'url': url}
    if category is not None:
        payload['category'] = category
    if title is not None:
        payload['title'] = title
    response = client.post_json('/api/bookmarks', payload)
    recorder.expect_status(response, 201, aid=f'{aid}-save-status')
    record_id = _record_id(_extract_record(_safe_json(response)))
    recorder.check(f'{aid}-save-id', bool(record_id), f'保存 {url} 返回 id={record_id!r}')
    return record_id


def _case_a04(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a04-health-status')

        name = _unique_category('a04')
        created = client.post_json('/api/categories', {'name': name})
        recorder.expect_status(created, 201, aid='a04-create-status')
        category_id = _record_id(_extract_record(_safe_json(created)))
        recorder.check('a04-create-id', bool(category_id), f'POST /api/categories 返回 id={category_id!r}')

        listed = _fetch_categories(client, recorder, 'a04-listed')
        recorder.check(
            'a04-created-visible',
            name in _category_names(listed),
            f'GET /api/categories 含新建归类 {name!r}',
        )

        duplicate = client.post_json('/api/categories', {'name': name})
        recorder.expect_status(duplicate, 409, aid='a04-duplicate-status')
        recorder.check(
            'a04-duplicate-code',
            _error_code(duplicate) == 'duplicate_category',
            f'同名再建错误码={_error_code(duplicate)!r}（期望 duplicate_category）',
        )

        variant = client.post_json('/api/categories', {'name': str(name).upper()})
        recorder.expect_status(variant, 409, aid='a04-duplicate-case-status')
        recorder.check(
            'a04-duplicate-case-code',
            _error_code(variant) == 'duplicate_category',
            f'大小写变体再建错误码={_error_code(variant)!r}（期望 duplicate_category）',
        )

        if not category_id:
            return

        record_id = _create_record(client, recorder, 'a04', category=name)
        if record_id:
            in_new = _fetch_bookmarks(client, recorder, 'a04-in-new', params={'category': name})
            recorder.check(
                'a04-record-in-new-category',
                record_id in _record_ids(in_new),
                f'记录 {record_id!r} 可在归类 {name!r} 中查到',
            )

        renamed_name = _unique_category('a04renamed')
        renamed = client.patch_json(_category_path(category_id), {'name': renamed_name})
        recorder.expect_status(renamed, _SUCCESS_STATUSES, aid='a04-rename-status')
        after_rename = _fetch_categories(client, recorder, 'a04-after-rename')
        names_after = _category_names(after_rename)
        recorder.check(
            'a04-rename-applied',
            renamed_name in names_after,
            f'重命名后新名 {renamed_name!r} 可见：{sorted(names_after)}',
        )
        recorder.check('a04-rename-old-absent', name not in names_after, f'重命名后旧名 {name!r} 不再出现')
        if record_id:
            by_renamed = _fetch_bookmarks(client, recorder, 'a04-by-renamed', params={'category': renamed_name})
            recorder.check(
                'a04-record-follows-rename',
                record_id in _record_ids(by_renamed),
                f'重命名后记录 {record_id!r} 仍属于该归类',
            )
            stale = _fetch_bookmarks(client, recorder, 'a04-stale-name', params={'category': name})
            recorder.check(
                'a04-unknown-category-empty',
                record_id not in _record_ids(stale),
                f'旧归类名 {name!r} 过滤不再返回该记录',
            )

        deleted = client.request('DELETE', _category_path(category_id))
        recorder.expect_status(deleted, _SUCCESS_STATUSES, aid='a04-delete-status')
        after_delete = _fetch_categories(client, recorder, 'a04-after-delete')
        remaining = _category_names(after_delete)
        recorder.check(
            'a04-delete-applied',
            renamed_name not in remaining,
            f'删除后 {renamed_name!r} 不再出现：{sorted(remaining)}',
        )
        if record_id:
            inbox = _fetch_bookmarks(client, recorder, 'a04-inbox', params={'category': common.DEFAULT_CATEGORY})
            recorder.check(
                'a04-record-back-to-default',
                record_id in _record_ids(inbox),
                f'删除归类后记录 {record_id!r} 回到「{common.DEFAULT_CATEGORY}」',
            )
            fetched = client.get(_bookmark_path(record_id))
            recorder.expect_status(fetched, 200, aid='a04-record-fetch-status')
            category_name = _record_category_name(_extract_record(_safe_json(fetched)))
            if category_name is not None:
                recorder.check(
                    'a04-record-category-default',
                    category_name == common.DEFAULT_CATEGORY,
                    f'记录 category={category_name!r}（期望 {common.DEFAULT_CATEGORY!r}）',
                )

        default_item = _default_category(after_delete)
        default_id = _record_id(default_item)
        if default_id:
            delete_default = client.request('DELETE', _category_path(default_id))
            recorder.expect_status(delete_default, 400, aid='a04-default-delete-status')
            recorder.check(
                'a04-default-delete-code',
                _error_code(delete_default) == 'protected_category',
                f'删除默认归类错误码={_error_code(delete_default)!r}（期望 protected_category）',
            )
            rename_default = client.patch_json(_category_path(default_id), {'name': _unique_category('a04default')})
            recorder.expect_status(rename_default, 400, aid='a04-default-rename-status')
            recorder.check(
                'a04-default-rename-code',
                _error_code(rename_default) == 'protected_category',
                f'重命名默认归类错误码={_error_code(rename_default)!r}（期望 protected_category）',
            )
    finally:
        client.close()


def _a05_on_base_url(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a05-health-status')

        category_name = _unique_category('a05live')
        record_id = _create_record(client, recorder, 'a05live')
        if not record_id:
            return

        moved = client.post_json(_move_path(record_id), {'category': category_name})
        recorder.expect_status(moved, _SUCCESS_STATUSES, aid='a05-live-move-status')
        in_category = _fetch_bookmarks(client, recorder, 'a05-live-in', params={'category': category_name})
        recorder.check(
            'a05-live-move-visible',
            record_id in _record_ids(in_category),
            f'移动后 {record_id!r} 可在 {category_name!r} 中查到',
        )
        inbox = _fetch_bookmarks(client, recorder, 'a05-live-inbox', params={'category': common.DEFAULT_CATEGORY})
        recorder.check(
            'a05-live-left-default',
            record_id not in _record_ids(inbox),
            f'移动后 {record_id!r} 不再属于「{common.DEFAULT_CATEGORY}」',
        )
        fetched = client.get(_bookmark_path(record_id))
        recorder.expect_status(fetched, 200, aid='a05-live-fetch-status')
        stored_category = _record_category_name(_extract_record(_safe_json(fetched)))
        if stored_category is not None:
            recorder.check(
                'a05-live-record-category',
                stored_category == category_name,
                f'记录 category={stored_category!r}（期望 {category_name!r}）',
            )
    finally:
        client.close()


def _a05_across_restart(args, recorder):
    first = common.launch_app(args.app_root, args.data_dir, 0)
    instance_dir = first.instance_dir
    category_name = _unique_category('a05restart')
    record_id = None
    try:
        client = common.HttpClient(first.base_url)
        try:
            health = client.get('/api/health')
            recorder.expect_status(health, 200, aid='a05-restart-health-status')
            record_id = _create_record(client, recorder, 'a05restart')
            if record_id:
                moved = client.post_json(_move_path(record_id), {'category': category_name})
                recorder.expect_status(moved, _SUCCESS_STATUSES, aid='a05-restart-move-status')
                in_category = _fetch_bookmarks(
                    client, recorder, 'a05-restart-in', params={'category': category_name}
                )
                recorder.check(
                    'a05-restart-move-visible',
                    record_id in _record_ids(in_category),
                    f'隔离实例移动后 {record_id!r} 可在 {category_name!r} 中查到',
                )
        finally:
            client.close()
    finally:
        common.stop_app(first)

    if not record_id:
        recorder.check('a05-restart-persist', False, '隔离实例未返回可用 id，无法验证归属跨重启')
        return

    second = common.launch_app(args.app_root, args.data_dir, 0, instance_dir=instance_dir)
    try:
        client = common.HttpClient(second.base_url)
        try:
            after = _fetch_bookmarks(client, recorder, 'a05-restart-after', params={'category': category_name})
            recorder.check(
                'a05-restart-persist-visible',
                record_id in _record_ids(after),
                f'重启后 {record_id!r} 仍可在 {category_name!r} 中查到',
            )
            inbox = _fetch_bookmarks(
                client, recorder, 'a05-restart-inbox', params={'category': common.DEFAULT_CATEGORY}
            )
            recorder.check(
                'a05-restart-persist-not-default',
                record_id not in _record_ids(inbox),
                f'重启后 {record_id!r} 不回到「{common.DEFAULT_CATEGORY}」',
            )
            fetched = client.get(_bookmark_path(record_id))
            recorder.expect_status(fetched, 200, aid='a05-restart-fetch-status')
            stored_category = _record_category_name(_extract_record(_safe_json(fetched)))
            if stored_category is not None:
                recorder.check(
                    'a05-restart-record-category',
                    stored_category == category_name,
                    f'重启后 category={stored_category!r}（期望 {category_name!r}）',
                )
        finally:
            client.close()
    finally:
        common.stop_app(second)


def _case_a05(args, recorder):
    _a05_on_base_url(args, recorder)
    _a05_across_restart(args, recorder)


def _case_a06(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a06-health-status')

        category_a = _unique_category('a06a')
        category_b = _unique_category('a06b')
        for label, category_name in (('a', category_a), ('b', category_b)):
            created = client.post_json('/api/categories', {'name': category_name})
            recorder.expect_status(created, 201, aid=f'a06-create-{label}-status')

        ids_a = [
            record_id
            for record_id in (
                _create_record(client, recorder, f'a06a-{index}', category=category_a) for index in range(1, 3)
            )
            if record_id
        ]
        ids_b = [
            record_id
            for record_id in (
                _create_record(client, recorder, f'a06b-{index}', category=category_b) for index in range(1, 3)
            )
            if record_id
        ]

        list_a = _fetch_bookmarks(client, recorder, 'a06-list-a', params={'category': category_a})
        set_a = _record_ids(list_a)
        list_b = _fetch_bookmarks(client, recorder, 'a06-list-b', params={'category': category_b})
        set_b = _record_ids(list_b)

        recorder.check(
            'a06-a-exact',
            bool(ids_a) and set_a == set(ids_a),
            f'按 {category_a!r} 过滤返回 {sorted(set_a)}（期望 {sorted(set(ids_a))}）',
        )
        recorder.check(
            'a06-b-exact',
            bool(ids_b) and set_b == set(ids_b),
            f'按 {category_b!r} 过滤返回 {sorted(set_b)}（期望 {sorted(set(ids_b))}）',
        )
        recorder.check('a06-disjoint', not (set_a & set_b), f'两类过滤结果不相交，交集={sorted(set_a & set_b)}')

        categories = _fetch_categories(client, recorder, 'a06-categories')
        item_a = _find_category(categories, category_a)
        item_b = _find_category(categories, category_b)
        count_a = item_a.get('count') if isinstance(item_a, dict) else None
        count_b = item_b.get('count') if isinstance(item_b, dict) else None
        recorder.check('a06-count-a', count_a == len(ids_a), f'归类 {category_a!r} 计数={count_a!r}（期望 {len(ids_a)}）')
        recorder.check('a06-count-b', count_b == len(ids_b), f'归类 {category_b!r} 计数={count_b!r}（期望 {len(ids_b)}）')
    finally:
        client.close()


def _case_a12(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a12-health-status')

        anchor_id = _create_record(client, recorder, 'a12-anchor')
        if not anchor_id:
            return

        before_categories = _fetch_categories(client, recorder, 'a12-before-categories')
        before_books = _fetch_bookmarks(client, recorder, 'a12-before-bookmarks')
        before_category_ids = _category_ids(before_categories)
        before_record_ids = _record_ids(before_books)

        too_long = 'x' * 121
        attempts = [
            ('save-empty', 'bookmark', ''),
            ('save-long', 'bookmark', too_long),
            ('move-empty', 'move', ''),
            ('move-long', 'move', too_long),
        ]
        for label, kind, category_value in attempts:
            if kind == 'bookmark':
                response = client.post_json(
                    '/api/bookmarks', {'url': _unique_url(f'a12-{label}'), 'category': category_value}
                )
            else:
                response = client.post_json(_move_path(anchor_id), {'category': category_value})
            recorder.expect_status(response, 400, aid=f'a12-{label}-status')
            code = _error_code(response)
            recorder.check(
                f'a12-{label}-code',
                code == 'invalid_category',
                f'{label} category={category_value[:24]!r} 错误码={code!r}（期望 invalid_category）',
            )

        after_categories = _fetch_categories(client, recorder, 'a12-after-categories')
        after_books = _fetch_bookmarks(client, recorder, 'a12-after-bookmarks')
        recorder.check(
            'a12-categories-unchanged',
            _category_ids(after_categories) == before_category_ids,
            f'归类集合不变：{sorted(_category_ids(after_categories))}（原 {sorted(before_category_ids)}）',
        )
        recorder.check(
            'a12-records-unchanged',
            _record_ids(after_books) == before_record_ids,
            f'记录集合不变：{len(before_record_ids)} -> {len(_record_ids(after_books))}',
        )
        names_after = _category_names(after_categories)
        recorder.check('a12-no-empty-category', '' not in names_after, '非法请求未创建空名归类')
        recorder.check('a12-no-long-category', too_long not in names_after, '非法请求未创建超长名归类')

        fetched = client.get(_bookmark_path(anchor_id))
        recorder.expect_status(fetched, 200, aid='a12-anchor-fetch-status')
        stored_category = _record_category_name(_extract_record(_safe_json(fetched)))
        if stored_category is not None:
            recorder.check(
                'a12-anchor-unchanged-category',
                stored_category == common.DEFAULT_CATEGORY,
                f'被移动尝试的目标记录 category={stored_category!r}（期望 {common.DEFAULT_CATEGORY!r}）',
            )
    finally:
        client.close()


_HANDLERS = {
    'A04': _case_a04,
    'A05': _case_a05,
    'A06': _case_a06,
    'A12': _case_a12,
}


def main(argv=None):
    args = common.parse_case_args(argv)
    recorder = common.Recorder(args.case)
    handler = _HANDLERS.get(args.case)
    if handler is None:
        recorder.check(
            'dispatch',
            False,
            f'acceptance/p0_organize.py 不实现用例 {args.case}（应由其他程序派发）',
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
