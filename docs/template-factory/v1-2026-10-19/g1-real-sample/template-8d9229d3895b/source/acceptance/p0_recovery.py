#!/usr/bin/env python3
'''P0 行为验收组：删除恢复与错误合同。

覆盖 A09、A10。仅使用 Python 3.12 标准库并复用 acceptance/common.py：
以 --case 派发，未知用例显式失败；每个用例对真实目标执行正向与硬负向
行为断言，向 stdout 输出单个 atlas.acceptance-result.v1 JSON，失败时以
非零码退出。
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


def _record_title(record):
    if isinstance(record, dict) and record.get('title') is not None:
        return str(record['title'])
    return None


def _record_description(record):
    if isinstance(record, dict):
        for key in ('description', 'desc'):
            if record.get(key) is not None:
                return str(record[key])
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


def _restore_path(bookmark_id):
    return _bookmark_path(bookmark_id) + '/restore'


def _move_path(bookmark_id):
    return _bookmark_path(bookmark_id) + '/move'


def _record_ids(records):
    return {item_id for item_id in (_record_id(record) for record in records) if item_id}


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


def _check_error(recorder, response, prefix, expected_status, expected_code, label):
    recorder.check(
        f'{prefix}-no-5xx',
        response.status < 500,
        f'{label} -> HTTP {response.status}（校验类错误不得产生 5xx）',
    )
    recorder.expect_status(
        response,
        expected_status,
        aid=f'{prefix}-status',
        detail=f'{label} -> HTTP {response.status}（期望 {expected_status}）',
    )
    code = _error_code(response)
    recorder.check(
        f'{prefix}-code',
        code == expected_code,
        f'{label} 错误码={code!r}（期望 {expected_code}）',
    )


def _create_record(client, recorder, aid, title=None, description=None):
    url = _unique_url(aid)
    payload = {'url': url}
    if title is not None:
        payload['title'] = title
    if description is not None:
        payload['description'] = description
    response = client.post_json('/api/bookmarks', payload)
    recorder.expect_status(response, 201, aid=f'{aid}-save-status')
    record_id = _record_id(_extract_record(_safe_json(response)))
    recorder.check(f'{aid}-save-id', bool(record_id), f'保存 {url} 返回 id={record_id!r}')
    return record_id


def _a09_on_base_url(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a09-live-health-status')

        category_name = _unique_category('a09live')
        url = _unique_url('a09live')
        title = f'A09 删除恢复 {uuid.uuid4().hex[:8]}'
        description = f'A09 描述 {uuid.uuid4().hex[:8]}'
        created = client.post_json(
            '/api/bookmarks',
            {'url': url, 'title': title, 'description': description, 'category': category_name},
        )
        recorder.expect_status(created, 201, aid='a09-live-create-status')
        record_id = _record_id(_extract_record(_safe_json(created)))
        recorder.check('a09-live-create-id', bool(record_id), f'创建记录返回 id={record_id!r}')
        if not record_id:
            return

        before = _fetch_bookmarks(client, recorder, 'a09-live-before', params={'category': category_name})
        recorder.check(
            'a09-live-visible-before',
            record_id in _record_ids(before),
            f'删除前记录 {record_id!r} 出现在归类 {category_name!r} 中',
        )

        deleted = client.request('DELETE', _bookmark_path(record_id))
        recorder.expect_status(deleted, _SUCCESS_STATUSES, aid='a09-live-delete-status')

        after_delete = _fetch_bookmarks(
            client, recorder, 'a09-live-after-delete', params={'category': category_name}
        )
        recorder.check(
            'a09-live-excluded-after-delete',
            record_id not in _record_ids(after_delete),
            f'删除后默认列表排除记录 {record_id!r}：{sorted(_record_ids(after_delete))}',
        )

        trashed = _fetch_bookmarks(
            client, recorder, 'a09-live-trashed',
            params={'category': category_name, 'include_trashed': 1},
        )
        recorder.check(
            'a09-live-soft-deleted',
            record_id in _record_ids(trashed),
            f'删除为软删除：include_trashed=1 仍可见记录 {record_id!r}',
        )

        restored = client.post_json(_restore_path(record_id), {})
        recorder.expect_status(restored, _SUCCESS_STATUSES, aid='a09-live-restore-status')

        after_restore = _fetch_bookmarks(
            client, recorder, 'a09-live-after-restore', params={'category': category_name}
        )
        recorder.check(
            'a09-live-visible-after-restore',
            record_id in _record_ids(after_restore),
            f'撤销恢复后默认列表重新可见记录 {record_id!r}',
        )

        fetched = client.get(_bookmark_path(record_id))
        recorder.expect_status(fetched, 200, aid='a09-live-after-fetch-status')
        restored_record = _extract_record(_safe_json(fetched))
        recorder.check(
            'a09-live-restored-url',
            _record_url(restored_record) == url,
            f'恢复后 url={_record_url(restored_record)!r}（期望 {url!r}）',
        )
        recorder.check(
            'a09-live-restored-title',
            _record_title(restored_record) == title,
            f'恢复后 title={_record_title(restored_record)!r}（期望 {title!r}）',
        )
        recorder.check(
            'a09-live-restored-description',
            _record_description(restored_record) == description,
            f'恢复后 description={_record_description(restored_record)!r}（期望 {description!r}）',
        )
        recorder.check(
            'a09-live-restored-category',
            _record_category_name(restored_record) == category_name,
            f'恢复后 category={_record_category_name(restored_record)!r}（期望 {category_name!r}）',
        )
    finally:
        client.close()


def _a09_across_restart(args, recorder):
    first = common.launch_app(args.app_root, args.data_dir, 0)
    instance_dir = first.instance_dir
    anchor_id = None
    deleted_id = None
    try:
        client = common.HttpClient(first.base_url)
        try:
            health = client.get('/api/health')
            recorder.expect_status(health, 200, aid='a09-restart-health-status')

            anchor_id = _create_record(client, recorder, 'a09-restart-anchor', title='A09 重启锚点')
            deleted_id = _create_record(client, recorder, 'a09-restart-deleted', title='A09 重启删除')
            if deleted_id:
                deleted = client.request('DELETE', _bookmark_path(deleted_id))
                recorder.expect_status(deleted, _SUCCESS_STATUSES, aid='a09-restart-delete-status')
                after_delete = _fetch_bookmarks(client, recorder, 'a09-restart-after-delete')
                recorder.check(
                    'a09-restart-excluded-before-restart',
                    deleted_id not in _record_ids(after_delete),
                    f'终止前已删除记录 {deleted_id!r} 被默认列表排除',
                )
        finally:
            client.close()
    finally:
        common.stop_app(first)

    if not (anchor_id and deleted_id):
        recorder.check('a09-restart-persist', False, '隔离实例未返回可用 id，无法验证删除跨重启')
        return

    second = common.launch_app(args.app_root, args.data_dir, 0, instance_dir=instance_dir)
    try:
        client = common.HttpClient(second.base_url)
        try:
            after = _fetch_bookmarks(client, recorder, 'a09-restart-after')
            ids = _record_ids(after)
            recorder.check(
                'a09-restart-anchor-persists',
                anchor_id in ids,
                f'重启后未删除记录 {anchor_id!r} 仍在默认列表（证明数据已持久化）',
            )
            recorder.check(
                'a09-restart-deletion-persists',
                deleted_id not in ids,
                f'重启后已删除记录 {deleted_id!r} 仍被默认列表排除',
            )
            trashed = _fetch_bookmarks(
                client, recorder, 'a09-restart-trashed', params={'include_trashed': 1}
            )
            recorder.check(
                'a09-restart-trash-retained',
                deleted_id in _record_ids(trashed),
                f'重启后已删除记录 {deleted_id!r} 仍以软删除状态存在，而非数据丢失',
            )
        finally:
            client.close()
    finally:
        common.stop_app(second)


def _case_a09(args, recorder):
    _a09_on_base_url(args, recorder)
    _a09_across_restart(args, recorder)


def _case_a10(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a10-health-status')

        anchor_url = _unique_url('a10-anchor')
        anchor_title = f'A10 锚点 {uuid.uuid4().hex[:8]}'
        anchor_description = f'A10 描述 {uuid.uuid4().hex[:8]}'
        created = client.post_json(
            '/api/bookmarks',
            {'url': anchor_url, 'title': anchor_title, 'description': anchor_description},
        )
        recorder.expect_status(created, 201, aid='a10-anchor-create-status')
        anchor_id = _record_id(_extract_record(_safe_json(created)))
        recorder.check('a10-anchor-create-id', bool(anchor_id), f'创建锚点记录返回 id={anchor_id!r}')
        if not anchor_id:
            return

        before_list = _fetch_bookmarks(client, recorder, 'a10-before-list')
        before_ids = _record_ids(before_list)

        before_fetch = client.get(_bookmark_path(anchor_id))
        recorder.expect_status(before_fetch, 200, aid='a10-anchor-before-status')
        before_record = _extract_record(_safe_json(before_fetch))

        unknown = f'unknown-{uuid.uuid4().hex[:12]}'

        unknown_get = client.get(_bookmark_path(unknown))
        _check_error(
            recorder, unknown_get, 'a10-unknown-get', 404, 'not_found',
            f'GET /api/bookmarks/{unknown}',
        )

        unknown_patch = client.patch_json(_bookmark_path(unknown), {'title': 'A10 未知 id'})
        _check_error(
            recorder, unknown_patch, 'a10-unknown-patch', 404, 'not_found',
            f'PATCH /api/bookmarks/{unknown}',
        )

        unknown_delete = client.request('DELETE', _bookmark_path(unknown))
        _check_error(
            recorder, unknown_delete, 'a10-unknown-delete', 404, 'not_found',
            f'DELETE /api/bookmarks/{unknown}',
        )

        unknown_move = client.post_json(_move_path(unknown), {'category': common.DEFAULT_CATEGORY})
        _check_error(
            recorder, unknown_move, 'a10-unknown-move', 404, 'not_found',
            f'POST /api/bookmarks/{unknown}/move',
        )

        malformed = (
            ('save', 'POST', '/api/bookmarks', '{"url": '),
            ('patch', 'PATCH', _bookmark_path(anchor_id), '{"title": '),
            ('move', 'POST', _move_path(anchor_id), '{"category": '),
        )
        for label, method, path, body in malformed:
            response = client.request(
                method, path, data=body, headers={'Content-Type': 'application/json'}
            )
            _check_error(
                recorder, response, f'a10-malformed-{label}', 400, 'bad_request',
                f'{method} {path} 畸形 JSON',
            )

        after_list = _fetch_bookmarks(client, recorder, 'a10-after-list')
        recorder.check(
            'a10-records-unchanged',
            _record_ids(after_list) == before_ids,
            f'错误请求未改变记录集合：{len(before_ids)} -> {len(_record_ids(after_list))}',
        )

        after_fetch = client.get(_bookmark_path(anchor_id))
        recorder.expect_status(after_fetch, 200, aid='a10-anchor-after-status')
        after_record = _extract_record(_safe_json(after_fetch))
        recorder.check(
            'a10-anchor-url-unchanged',
            _record_url(after_record) == _record_url(before_record),
            f'锚点 url={_record_url(after_record)!r}（未被修改）',
        )
        recorder.check(
            'a10-anchor-title-unchanged',
            _record_title(after_record) == _record_title(before_record),
            f'锚点 title={_record_title(after_record)!r}（未被修改）',
        )
        recorder.check(
            'a10-anchor-description-unchanged',
            _record_description(after_record) == _record_description(before_record),
            f'锚点 description={_record_description(after_record)!r}（未被修改）',
        )
        recorder.check(
            'a10-anchor-category-unchanged',
            _record_category_name(after_record) == _record_category_name(before_record),
            f'锚点 category={_record_category_name(after_record)!r}（未被修改）',
        )
    finally:
        client.close()


_HANDLERS = {
    'A09': _case_a09,
    'A10': _case_a10,
}


def main(argv=None):
    args = common.parse_case_args(argv)
    recorder = common.Recorder(args.case)
    handler = _HANDLERS.get(args.case)
    if handler is None:
        recorder.check(
            'dispatch',
            False,
            f'acceptance/p0_recovery.py 不实现用例 {args.case}（应由其他程序派发）',
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
