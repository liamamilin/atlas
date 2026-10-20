#!/usr/bin/env python3
'''P0 行为验收组：关键字检索与打开原页。

覆盖 A07、A08。仅使用 Python 3.12 标准库并复用 acceptance/common.py：
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
        created = client.post_json('/api/bookmarks', {'url': target_url, 'title': 'A08 打开原页'})
        recorder.expect_status(created, 201, aid='a08-create-status')
        record_id = _record_id(_extract_record(_safe_json(created)))
        recorder.check('a08-create-id', bool(record_id), f'创建记录返回 id={record_id!r}')

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
