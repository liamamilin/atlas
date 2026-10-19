'''acceptance/p0_core.py — P0 捕获与归类用例（A01–A05）。

本模块以 __file__ 定位套件根后导入 acceptance.common，确保以
`python /suite/acceptance/p0_core.py` 运行且 cwd 非 /suite 时导入仍可用。
导出 CASES = {case_id: fn(ctx) -> assertion 列表}；所有断言都基于对真实 HTTP
目标提交真实表单并解析真实 HTML 响应，绝不使用 mock，也不读取应用数据库。
spec 中 A01–A10 的 implementation 为 acceptance/p0.py，它合并本模块与
p0_find.py 的 CASES 后交给 common.main 逐例执行；本模块也可直接运行。
'''

import os
import sys
import urllib.parse
import uuid

_SUITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SUITE_ROOT not in sys.path:
    sys.path.insert(0, _SUITE_ROOT)

from acceptance.common import assertion, parse_list

__all__ = ['CASES']


def _token():
    '''每次运行生成唯一后缀，避免共享目标上的用例互相污染。'''
    return uuid.uuid4().hex[:10]


def _collection_path(collection_id):
    return '/?collection=' + urllib.parse.quote(str(collection_id), safe='')


def _bookmarks_in(ctx, path):
    '''GET path 并解析书签列表；非 200 时返回空列表。'''
    response = ctx.target.get(path)
    if response.status == 200:
        items = parse_list(response.body)['bookmarks']
    else:
        items = []
    return response, items


def _collections(ctx):
    '''GET / 并解析侧栏归类项。'''
    ctx.target.get('/')
    return parse_list(ctx.target.body)['collections']


def _find_collection(ctx, name):
    for collection in _collections(ctx):
        if collection['name'] == name:
            return collection
    return None


def _default_collection(ctx):
    for collection in _collections(ctx):
        if collection['default']:
            return collection
    return None


def _bookmark_key(item):
    if item['id']:
        return 'id:' + str(item['id'])
    return 'url:' + str(item['url']) + '|' + str(item['title'])


def _library_keys(ctx):
    '''聚合首页与各归类视图中的记录标识，用于记录数不变性断言。'''
    keys = set()
    response = ctx.target.get('/')
    if response.status != 200:
        return keys
    parsed = parse_list(response.body)
    for item in parsed['bookmarks']:
        keys.add(_bookmark_key(item))
    for collection in parsed['collections']:
        if not collection['id']:
            continue
        view = ctx.target.get(_collection_path(collection['id']))
        if view.status == 200:
            for item in parse_list(view.body)['bookmarks']:
                keys.add(_bookmark_key(item))
    return keys


def case_a01(ctx):
    '''A01：合法 URL 保存到指定已有归类后，列表出现记录且标题/URL/归类正确。'''
    checks = []
    token = _token()
    name = 'A01归类-' + token
    url = 'https://example.com/a01-' + token
    title = 'A01标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = ctx.target.post_form('/collections', {'name': name})
    checks.append(assertion(
        'create-collection-303', created.status == 303,
        'POST /collections name=%r status=%s location=%s' % (name, created.status, created.location)))

    collection = _find_collection(ctx, name)
    checks.append(assertion(
        'collection-exists', bool(collection and collection['id']),
        'sidebar collections=%r' % [item['name'] for item in _collections(ctx)]))
    if not collection or not collection['id']:
        return checks
    cid = collection['id']

    saved = ctx.target.post_form('/bookmarks', {'url': url, 'title': title, 'collection_id': cid})
    checks.append(assertion(
        'save-303', saved.status == 303,
        'POST /bookmarks url=%r collection_id=%s status=%s location=%s'
        % (url, cid, saved.status, saved.location)))
    location = saved.location or ''
    checks.append(assertion(
        'redirect-to-collection', ('collection=' + str(cid)) in location,
        'location=%r expected collection=%s' % (location, cid)))

    path = _collection_path(cid)
    view, items = _bookmarks_in(ctx, path)
    checks.append(assertion(
        'collection-view-200', view.status == 200, 'GET %s status=%s' % (path, view.status)))
    found = [item for item in items if item['url'] == url]
    checks.append(assertion(
        'record-in-collection', len(found) == 1,
        'matching url count=%d of %d listed' % (len(found), len(items))))
    if found:
        item = found[0]
        checks.append(assertion(
            'record-title', item['title'] == title,
            'expected title=%r actual=%r' % (title, item['title'])))
        checks.append(assertion(
            'record-url', item['url'] == url,
            'expected url=%r actual=%r' % (url, item['url'])))
        if item['collection_id'] is not None:
            checks.append(assertion(
                'record-collection', str(item['collection_id']) == str(cid),
                'expected collection=%s actual=%r' % (cid, item['collection_id'])))
    return checks


def case_a02(ctx):
    '''A02：空 URL、非 http(s) 协议与畸形 URL 被 400 拒绝且库记录数不变。'''
    checks = []
    token = _token()
    before = _library_keys(ctx)
    checks.append(assertion('baseline-snapshot', True, 'library record keys before=%d' % len(before)))

    invalid = [
        ('empty', ''),
        ('javascript-scheme', 'javascript:alert(1)'),
        ('data-scheme', 'data:text/html,<h1>A02</h1>'),
        ('malformed-text', 'not a url'),
        ('missing-host', 'http://'),
        ('non-http-scheme', 'ftp://example.com/A02-' + token),
    ]
    for label, bad in invalid:
        response = ctx.target.post_form('/bookmarks', {'url': bad, 'title': 'A02-' + token})
        checks.append(assertion(
            'reject-' + label, response.status == 400,
            'POST /bookmarks url=%r status=%s' % (bad, response.status)))
        checks.append(assertion(
            'error-page-' + label, len(response.body.strip()) > 0,
            'error response body length=%d' % len(response.body.strip())))

    after = _library_keys(ctx)
    checks.append(assertion(
        'library-unchanged', before == after,
        'before=%d after=%d added=%r removed=%r'
        % (len(before), len(after), sorted(after - before), sorted(before - after))))
    return checks


def case_a03(ctx):
    '''A03：不选归类保存进入默认收件箱，并可在 /?collection=inbox 浏览到。'''
    checks = []
    token = _token()
    url = 'https://example.com/a03-' + token
    title = 'A03标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    default = _default_collection(ctx)
    checks.append(assertion(
        'default-inbox-exists', bool(default and default['id']),
        'default collection=%r' % (default and default.get('name'))))

    saved = ctx.target.post_form('/bookmarks', {'url': url, 'title': title})
    checks.append(assertion(
        'save-without-collection-303', saved.status == 303,
        'POST /bookmarks url=%r status=%s location=%s' % (url, saved.status, saved.location)))

    accepted = {'inbox'}
    if default and default['id']:
        accepted.add(str(default['id']))
    location = saved.location or ''
    checks.append(assertion(
        'redirect-to-inbox',
        bool(location) and any(('collection=' + value) in location for value in accepted),
        'location=%r expected one of %r' % (location, sorted(accepted))))

    inbox_view, inbox_items = _bookmarks_in(ctx, '/?collection=inbox')
    checks.append(assertion(
        'inbox-view-200', inbox_view.status == 200,
        'GET /?collection=inbox status=%s' % inbox_view.status))
    found = [item for item in inbox_items if item['url'] == url]
    checks.append(assertion(
        'record-in-inbox', len(found) == 1,
        'matching url count=%d of %d listed in inbox' % (len(found), len(inbox_items))))
    if found:
        checks.append(assertion(
            'inbox-record-title', found[0]['title'] == title,
            'expected title=%r actual=%r' % (title, found[0]['title'])))
        checks.append(assertion(
            'inbox-record-url', found[0]['url'] == url,
            'expected url=%r actual=%r' % (url, found[0]['url'])))
    if default and default['id']:
        path = _collection_path(default['id'])
        by_id_view, by_id_items = _bookmarks_in(ctx, path)
        found_by_id = [item for item in by_id_items if item['url'] == url]
        checks.append(assertion(
            'record-in-default-collection', len(found_by_id) == 1,
            'matching url count=%d of %d in default collection view %s'
            % (len(found_by_id), len(by_id_items), path)))
    return checks


def case_a04(ctx):
    '''A04：新建归类后出现在侧栏，并可把记录保存到该新归类。'''
    checks = []
    token = _token()
    name = 'A04归类-' + token
    url = 'https://example.com/a04-' + token
    title = 'A04标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = ctx.target.post_form('/collections', {'name': name})
    checks.append(assertion(
        'create-collection-303', created.status == 303,
        'POST /collections name=%r status=%s location=%s' % (name, created.status, created.location)))

    collection = _find_collection(ctx, name)
    checks.append(assertion(
        'collection-in-sidebar', bool(collection and collection['id']),
        'sidebar collections=%r' % [item['name'] for item in _collections(ctx)]))
    if not collection or not collection['id']:
        return checks
    cid = collection['id']

    saved = ctx.target.post_form('/bookmarks', {'url': url, 'title': title, 'collection_id': cid})
    checks.append(assertion(
        'save-to-new-collection-303', saved.status == 303,
        'POST /bookmarks url=%r collection_id=%s status=%s location=%s'
        % (url, cid, saved.status, saved.location)))
    location = saved.location or ''
    checks.append(assertion(
        'redirect-to-new-collection', ('collection=' + str(cid)) in location,
        'location=%r expected collection=%s' % (location, cid)))

    path = _collection_path(cid)
    view, items = _bookmarks_in(ctx, path)
    checks.append(assertion(
        'new-collection-view-200', view.status == 200, 'GET %s status=%s' % (path, view.status)))
    found = [item for item in items if item['url'] == url]
    checks.append(assertion(
        'record-in-new-collection', len(found) == 1,
        'matching url count=%d of %d listed' % (len(found), len(items))))
    if found:
        checks.append(assertion(
            'record-title', found[0]['title'] == title,
            'expected title=%r actual=%r' % (title, found[0]['title'])))
    return checks


def case_a05(ctx):
    '''A05：记录从归类 A 移动到 B 后仅出现在 B。'''
    checks = []
    token = _token()
    name_a = 'A05源-' + token
    name_b = 'A05目标-' + token
    url = 'https://example.com/a05-' + token
    title = 'A05标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created_a = ctx.target.post_form('/collections', {'name': name_a})
    created_b = ctx.target.post_form('/collections', {'name': name_b})
    checks.append(assertion('create-source-303', created_a.status == 303,
                            'POST /collections name=%r status=%s' % (name_a, created_a.status)))
    checks.append(assertion('create-target-303', created_b.status == 303,
                            'POST /collections name=%r status=%s' % (name_b, created_b.status)))

    collection_a = _find_collection(ctx, name_a)
    collection_b = _find_collection(ctx, name_b)
    checks.append(assertion('source-collection-present', bool(collection_a and collection_a['id']),
                            'source collection id=%r' % (collection_a and collection_a['id'])))
    checks.append(assertion('target-collection-present', bool(collection_b and collection_b['id']),
                            'target collection id=%r' % (collection_b and collection_b['id'])))
    if not (collection_a and collection_a['id'] and collection_b and collection_b['id']):
        return checks
    aid = collection_a['id']
    bid = collection_b['id']

    saved = ctx.target.post_form('/bookmarks', {'url': url, 'title': title, 'collection_id': aid})
    checks.append(assertion('save-to-source-303', saved.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s' % (url, aid, saved.status)))

    src_view, src_items = _bookmarks_in(ctx, _collection_path(aid))
    found_source = [item for item in src_items if item['url'] == url]
    checks.append(assertion('record-in-source', len(found_source) == 1,
                            'matching url count=%d of %d in source view' % (len(found_source), len(src_items))))
    if not found_source:
        return checks
    bookmark_id = found_source[0]['id']
    checks.append(assertion('record-has-id', bool(bookmark_id), 'data-bookmark-id=%r' % bookmark_id))
    if not bookmark_id:
        return checks

    moved = ctx.target.post_form('/bookmarks/%s/move' % bookmark_id, {'collection_id': bid})
    checks.append(assertion('move-303', moved.status == 303,
                            'POST /bookmarks/%s/move collection_id=%s status=%s location=%s'
                            % (bookmark_id, bid, moved.status, moved.location)))
    location = moved.location or ''
    checks.append(assertion('redirect-to-target', ('collection=' + str(bid)) in location,
                            'location=%r expected collection=%s' % (location, bid)))

    tgt_view, tgt_items = _bookmarks_in(ctx, _collection_path(bid))
    in_target = [item for item in tgt_items if item['url'] == url]
    checks.append(assertion('record-in-target', len(in_target) == 1,
                            'matching url count=%d of %d in target view' % (len(in_target), len(tgt_items))))
    src_after_view, src_after_items = _bookmarks_in(ctx, _collection_path(aid))
    still_source = [item for item in src_after_items if item['url'] == url]
    checks.append(assertion('record-not-in-source', len(still_source) == 0,
                            'matching url count=%d of %d remaining in source view'
                            % (len(still_source), len(src_after_items))))
    return checks


CASES = {
    'A01': case_a01,
    'A02': case_a02,
    'A03': case_a03,
    'A04': case_a04,
    'A05': case_a05,
}


if __name__ == '__main__':
    from acceptance.common import main as _run
    _run(CASES, sys.argv[1:])
