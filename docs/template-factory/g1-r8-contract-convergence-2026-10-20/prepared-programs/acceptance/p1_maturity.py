#!/usr/bin/env python3
'''P1 行为验收组：离线增强降级、导入导出、重复检测。

覆盖 A13、A14、A15。仅使用 Python 3.12 标准库并复用 acceptance/common.py：
以 --case 派发，未知用例显式失败；每个用例对真实目标执行正向与硬负向
行为断言，向 stdout 输出单个 atlas.acceptance-result.v1 JSON，失败时以
非零码退出。
'''

from __future__ import annotations

import html
import os
import sys
import uuid
from html.parser import HTMLParser
from urllib.parse import quote, urlsplit

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

import common

_NETSCAPE_HEADER = '<!DOCTYPE NETSCAPE-Bookmark-file-1>'

_RESOURCE_ATTRIBUTES = {
    'img': frozenset({'src', 'srcset'}),
    'script': frozenset({'src'}),
    'link': frozenset({'href'}),
    'iframe': frozenset({'src'}),
    'source': frozenset({'src', 'srcset'}),
    'video': frozenset({'src', 'poster'}),
    'audio': frozenset({'src'}),
    'object': frozenset({'data'}),
    'embed': frozenset({'src'}),
    'track': frozenset({'src'}),
}


def _unique_token(tag):
    return f'{tag}-{uuid.uuid4().hex[:12]}'


def _unique_url(tag):
    token = _unique_token(tag)
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


def _record_hostname(record):
    if isinstance(record, dict) and record.get('hostname') is not None:
        return str(record['hostname'])
    return None


def _record_title_value(record):
    if isinstance(record, dict):
        return record.get('title')
    return None


def _record_favicon(record):
    if isinstance(record, dict):
        return record.get('favicon_url')
    return None


def _record_ids(records):
    return {item_id for item_id in (_record_id(record) for record in records) if item_id}


def _has_error(payload):
    return isinstance(payload, dict) and payload.get('error') is not None


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


def _is_local_resource(value, base_url):
    if value is None:
        return True
    if not isinstance(value, str):
        return False
    text = value.strip()
    if not text:
        return True
    lowered = text.lower()
    if lowered.startswith('data:'):
        return True
    if text.startswith('/'):
        return True
    try:
        parts = urlsplit(text)
    except ValueError:
        return False
    if parts.scheme:
        if parts.scheme.lower() not in ('http', 'https'):
            return False
        base = urlsplit(base_url)
        return parts.netloc.lower() == base.netloc.lower()
    if parts.netloc:
        return False
    return True


class _ResourceCollector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls = []

    def handle_starttag(self, tag, attrs):
        names = _RESOURCE_ATTRIBUTES.get(tag.lower())
        if not names:
            return
        for name, value in attrs:
            if value is None or name.lower() not in names:
                continue
            if name.lower() == 'srcset':
                for part in value.split(','):
                    candidate = part.strip().split(' ')[0]
                    if candidate:
                        self.urls.append(candidate)
            else:
                candidate = value.strip()
                if candidate:
                    self.urls.append(candidate)

    handle_startendtag = handle_starttag


def _external_resources(body, base_url):
    collector = _ResourceCollector()
    try:
        collector.feed(body)
        collector.close()
    except Exception as exc:
        return [f'<parse-error:{type(exc).__name__}>']
    return [url for url in collector.urls if not _is_local_resource(url, base_url)]


def _import_counts(payload):
    if isinstance(payload, dict):
        if 'imported' in payload or 'skipped' in payload:
            return payload
        data = payload.get('data')
        if isinstance(data, dict):
            return data
    return {}


def _as_count(value):
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _find_value(payload, key):
    if isinstance(payload, dict):
        if key in payload:
            return True, payload[key]
        for value in payload.values():
            found, item = _find_value(value, key)
            if found:
                return found, item
    elif isinstance(payload, list):
        for value in payload:
            found, item = _find_value(value, key)
            if found:
                return found, item
    return False, None


class _A13TargetLinkParser(HTMLParser):
    """Capture anchors owned by the unique matching record row."""
    def __init__(self, record_id):
        super().__init__(convert_charrefs=True)
        self.record_id = str(record_id)
        self._table_depth = 0
        self._rows = []
        self.matching_rows = 0
        self.links = []

    def _close_rows_at_or_below(self, table_depth):
        while self._rows and self._rows[-1]['table_depth'] >= table_depth:
            self._rows.pop()

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs = {str(key).lower(): ('' if value is None else value) for key, value in attrs}
        if tag == 'table':
            self._table_depth += 1
        elif tag == 'tr':
            # HTML parsers may omit </tr>; a peer <tr> implicitly closes that row.
            # Prune stale peers and malformed descendants before opening the new row.
            self._close_rows_at_or_below(self._table_depth)
            is_target = (
                attrs.get('data-testid') == 'record-row'
                and attrs.get('data-record-id') == self.record_id
            )
            if is_target:
                self.matching_rows += 1
            self._rows.append({'table_depth': self._table_depth, 'target': is_target})
        elif (tag == 'a' and self._rows and self._rows[-1]['target']
              and self._rows[-1]['table_depth'] == self._table_depth
              and attrs.get('data-testid') == 'record-open-link'):
            self.links.append(attrs)

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == 'tr':
            self._close_rows_at_or_below(self._table_depth)
        elif tag == 'table':
            self._close_rows_at_or_below(self._table_depth)
            self._table_depth = max(0, self._table_depth - 1)


def _a13_target_link(body, record_id, target_url):
    parser = _A13TargetLinkParser(record_id)
    parser.feed(body or '')
    parser.close()
    if parser.matching_rows != 1 or len(parser.links) != 1:
        return False, (f'top-level target row count={parser.matching_rows}, '
                       f'row open-link count={len(parser.links)} (expected exactly one each)')
    attrs = parser.links[0]
    rel = set((attrs.get('rel') or '').lower().split())
    valid = attrs.get('href') == target_url and attrs.get('target') == '_blank' and 'noopener' in rel
    return valid, (f'href={attrs.get("href")!r}, target={attrs.get("target")!r}, '
                   f'rel={attrs.get("rel")!r}; expected original URL, _blank, noopener')

def _case_a13(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a13-health-status')

        target_url = _unique_url('a13')
        hostname = urlsplit(target_url).hostname
        created = client.post_json('/api/bookmarks', {'url': target_url})
        recorder.expect_status(created, 201, aid='a13-create-status')
        payload = _safe_json(created)
        recorder.check(
            'a13-create-json',
            isinstance(payload, dict),
            f'仅凭 URL 保存返回 JSON 对象，实际 {type(payload).__name__}',
        )
        recorder.check(
            'a13-create-no-error',
            not _has_error(payload),
            '仅凭 URL 保存未返回 error 对象',
        )
        record = _extract_record(payload)
        recorder.check(
            'a13-create-record',
            isinstance(record, dict),
            f'保存响应含记录对象，实际 {type(record).__name__}',
        )
        record_id = _record_id(record)
        recorder.check('a13-create-id', bool(record_id), f'保存返回 id={record_id!r}')
        recorder.check(
            'a13-hostname-derived',
            _record_hostname(record) == hostname,
            f'保存返回 hostname={_record_hostname(record)!r}（期望由 URL 派生 {hostname!r}）',
        )
        recorder.check(
            'a13-url-unchanged',
            _record_url(record) == target_url,
            f'保存返回 url={_record_url(record)!r}（期望 {target_url!r}）',
        )
        title_value = _record_title_value(record)
        recorder.check(
            'a13-title-degraded',
            title_value is None or isinstance(title_value, str),
            f'未提供标题时 title={title_value!r}（允许缺失或派生字符串，不得为错误结构）',
        )
        favicon_value = _record_favicon(record)
        recorder.check(
            'a13-favicon-local',
            _is_local_resource(favicon_value, args.base_url),
            f'未提供图标时 favicon_url={favicon_value!r}（必须缺失、内联或同源，避免外部请求）',
        )

        if record_id:
            fetched = client.get(_bookmark_path(record_id))
            recorder.expect_status(fetched, 200, aid='a13-readback-status')
            stored = _extract_record(_safe_json(fetched))
            recorder.check(
                'a13-readback-record',
                isinstance(stored, dict),
                f'GET /api/bookmarks/{record_id} 返回记录对象',
            )
            recorder.check(
                'a13-readback-hostname',
                _record_hostname(stored) == hostname,
                f'读回 hostname={_record_hostname(stored)!r}（期望 {hostname!r}）',
            )
            recorder.check(
                'a13-readback-url',
                _record_url(stored) == target_url,
                f'读回 url={_record_url(stored)!r}（期望 {target_url!r}）',
            )
            stored_title = _record_title_value(stored)
            recorder.check(
                'a13-readback-title-degraded',
                stored_title is None or isinstance(stored_title, str),
                f'读回 title={stored_title!r}（允许缺失或派生字符串）',
            )
            stored_favicon = _record_favicon(stored)
            recorder.check(
                'a13-readback-favicon-local',
                _is_local_resource(stored_favicon, args.base_url),
                f'读回 favicon_url={stored_favicon!r}（必须缺失、内联或同源）',
            )

        page = client.get('/', accept='text/html')
        recorder.expect_status(page, 200, aid='a13-list-status')
        recorder.check(
            'a13-list-content-type',
            'text/html' in page.content_type.lower(),
            f'GET / Content-Type={page.content_type!r}（期望 text/html）',
        )
        body = page.text
        link_ok, link_detail = _a13_target_link(body, record_id, target_url) if record_id else (False, '缺少本次记录 id')
        recorder.check(
            'a13-target-row-open-link',
            link_ok,
            '本次记录行内的原始 URL 打开链接正确：' + link_detail,
        )
        external = _external_resources(body, args.base_url)
        recorder.check(
            'a13-list-no-external-resources',
            not external,
            f'列表页未引用外部资源：{external[:5] if external else "无"}',
        )
    finally:
        client.close()


def _case_a14(args, recorder):
    data_dir = args.data_dir
    if not data_dir:
        recorder.check('a14-data-dir', False, 'A14 需要 --data-dir 生成导入 HTML')
        return
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a14-health-status')

        exported_items = []
        for index in (1, 2):
            token = _unique_token(f'a14-export-{index}')
            url = f'https://{token}.atlas-acceptance.example/{token}'
            title = f'A14 导出 {index} {token}'
            created = client.post_json('/api/bookmarks', {'url': url, 'title': title})
            recorder.expect_status(created, 201, aid=f'a14-export-{index}-create-status')
            record_id = _record_id(_extract_record(_safe_json(created)))
            recorder.check(
                f'a14-export-{index}-create-id',
                bool(record_id),
                f'导出样本 {index} 保存返回 id={record_id!r}',
            )
            exported_items.append({'index': index, 'url': url, 'title': title, 'id': record_id})

        exported = client.get('/api/export', accept='text/html')
        recorder.expect_status(exported, 200, aid='a14-export-status')
        recorder.check(
            'a14-export-content-type',
            'text/html' in exported.content_type.lower(),
            f'GET /api/export Content-Type={exported.content_type!r}（期望 text/html）',
        )
        export_body = exported.text
        recorder.check(
            'a14-export-netscape-header',
            _NETSCAPE_HEADER.lower() in export_body.lower(),
            'GET /api/export 含 Netscape 书签文件头',
        )
        for item in exported_items:
            recorder.check(
                f'a14-export-{item["index"]}-url',
                item['url'] in export_body,
                f'导出内容含已存 URL {item["url"]}',
            )

        import_token = _unique_token('a14-import')
        import_items = []
        for index in (1, 2):
            token = f'{import_token}-{index}'
            url = f'https://{token}.atlas-acceptance.example/{token}'
            title = f'A14 导入 {index} {token}'
            import_items.append({'index': index, 'token': token, 'url': url, 'title': title})

        folder = f'导入验收 {import_token}'
        lines = [
            _NETSCAPE_HEADER,
            '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
            '<TITLE>Bookmarks</TITLE>',
            '<H1>Bookmarks</H1>',
            '<DL><p>',
            f'    <DT><H3>{html.escape(folder)}</H3>',
            '    <DL><p>',
        ]
        for item in import_items:
            lines.append(
                '        <DT><A HREF="{}" ADD_DATE="1700000000">{}</A>'.format(
                    html.escape(item['url'], quote=True),
                    html.escape(item['title']),
                )
            )
        lines.extend(['    </DL><p>', '</DL><p>', ''])
        import_html = chr(10).join(lines)
        import_filename = f'import-{import_token}.html'
        import_path = os.path.join(data_dir, import_filename)
        try:
            with open(import_path, 'w', encoding='utf-8') as handle:
                handle.write(import_html)
        except OSError as exc:
            recorder.check(
                'a14-import-fixture',
                False,
                f'无法在 --data-dir 内生成导入 HTML：{type(exc).__name__}',
            )
            return

        imported = client.request(
            'POST',
            '/api/import',
            data=import_html,
            headers={'Content-Type': 'text/html; charset=utf-8'},
            accept='application/json',
        )
        recorder.expect_status(imported, 200, aid='a14-import-status')
        counts = _import_counts(_safe_json(imported))
        imported_count = _as_count(counts.get('imported'))
        skipped_count = _as_count(counts.get('skipped'))
        recorder.check(
            'a14-import-count',
            imported_count == 2,
            f'导入计数 imported={imported_count!r}（期望 2）',
        )
        recorder.check(
            'a14-import-skipped',
            skipped_count == 0,
            f'导入计数 skipped={skipped_count!r}（期望 0）',
        )

        for item in import_items:
            found = _fetch_bookmarks(
                client,
                recorder,
                f'a14-import-{item["index"]}-search',
                params={'q': item['token']},
            )
            matches = [record for record in found if _record_url(record) == item['url']]
            recorder.check(
                f'a14-import-{item["index"]}-searchable',
                len(matches) == 1,
                f'导入 URL 可由关键字 {item["token"]!r} 检索到且唯一：{len(matches)} 条',
            )
    finally:
        client.close()


def _case_a15(args, recorder):
    client = common.HttpClient(args.base_url)
    try:
        health = client.get('/api/health')
        recorder.expect_status(health, 200, aid='a15-health-status')

        token = _unique_token('a15')
        url = f'https://{token}.atlas-acceptance.example/{token}'
        first = client.post_json('/api/bookmarks', {'url': url, 'title': f'A15 原始 {token}'})
        recorder.expect_status(first, 201, aid='a15-first-status')
        first_id = _record_id(_extract_record(_safe_json(first)))
        recorder.check('a15-first-id', bool(first_id), f'首次保存返回 id={first_id!r}')
        if not first_id:
            return

        before = _fetch_bookmarks(client, recorder, 'a15-before')
        before_ids = _record_ids(before)
        before_total = len(before)
        before_matches = sum(1 for record in before if _record_url(record) == url)
        recorder.check(
            'a15-before-single',
            before_matches == 1,
            f'首次保存后 URL 在列表中恰出现 {before_matches} 次（期望 1）',
        )
        recorder.check(
            'a15-before-contains-first',
            first_id in before_ids,
            f'首次保存的记录 {first_id!r} 出现在列表',
        )

        duplicate = client.post_json('/api/bookmarks', {'url': url, 'title': f'A15 重复 {token}'})
        recorder.expect_status(duplicate, 409, aid='a15-duplicate-status')
        duplicate_code = _error_code(duplicate)
        recorder.check(
            'a15-duplicate-code',
            duplicate_code == 'duplicate_url',
            f'重复 URL 错误码={duplicate_code!r}（期望 duplicate_url）',
        )
        found, existing_id = _find_value(_safe_json(duplicate), 'existing_id')
        recorder.check(
            'a15-duplicate-existing-id',
            found and str(existing_id) == first_id,
            f'409 附带 existing_id={existing_id!r}（期望 {first_id!r}）',
        )

        after_reject = _fetch_bookmarks(client, recorder, 'a15-after-reject')
        after_reject_ids = _record_ids(after_reject)
        after_reject_matches = sum(1 for record in after_reject if _record_url(record) == url)
        recorder.check(
            'a15-reject-total-unchanged',
            len(after_reject) == before_total,
            f'重复被拒后记录总数 {before_total} -> {len(after_reject)}（期望不变）',
        )
        recorder.check(
            'a15-reject-ids-unchanged',
            after_reject_ids == before_ids,
            f'重复被拒后记录集合不变：{len(before_ids)} -> {len(after_reject_ids)}',
        )
        recorder.check(
            'a15-reject-single',
            after_reject_matches == 1,
            f'重复被拒后 URL 仍只出现 {after_reject_matches} 次（期望 1）',
        )

        allowed = client.post_json(
            '/api/bookmarks',
            {'url': url, 'title': f'A15 允许重复 {token}', 'allow_duplicate': True},
        )
        recorder.expect_status(allowed, 201, aid='a15-allow-status')
        second_id = _record_id(_extract_record(_safe_json(allowed)))
        recorder.check('a15-allow-id', bool(second_id), f'允许重复保存返回 id={second_id!r}')
        recorder.check(
            'a15-allow-new-id',
            bool(second_id) and second_id != first_id,
            f'允许重复后新记录 id={second_id!r} 与首次 {first_id!r} 不同',
        )

        after_allow = _fetch_bookmarks(client, recorder, 'a15-after-allow')
        allow_matches = [record for record in after_allow if _record_url(record) == url]
        allow_ids = _record_ids(after_allow)
        recorder.check(
            'a15-allow-total-plus-one',
            len(after_allow) == before_total + 1,
            f'允许重复后记录总数 {before_total} -> {len(after_allow)}（期望 +1）',
        )
        recorder.check(
            'a15-allow-url-count',
            len(allow_matches) == 2,
            f'允许重复后同一 URL 出现 {len(allow_matches)} 次（期望 2）',
        )
        recorder.check(
            'a15-allow-original-retained',
            first_id in allow_ids,
            f'允许重复后原记录 {first_id!r} 仍存在',
        )
        if second_id:
            recorder.check(
                'a15-allow-second-present',
                second_id in allow_ids,
                f'允许重复后新记录 {second_id!r} 出现在列表',
            )
    finally:
        client.close()


_HANDLERS = {
    'A13': _case_a13,
    'A14': _case_a14,
    'A15': _case_a15,
}


def main(argv=None):
    args = common.parse_case_args(argv)
    recorder = common.Recorder(args.case)
    handler = _HANDLERS.get(args.case)
    if handler is None:
        recorder.check(
            'dispatch',
            False,
            f'acceptance/p1_maturity.py 不实现用例 {args.case}（应由其他程序派发）',
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
