'''acceptance/p0_find.py — P0 检索、打开、持久化与负例用例（A06–A10）。

本模块以 __file__ 定位套件根后导入 acceptance.common，确保以
`python /suite/acceptance/p0_find.py` 运行且 cwd 非 /suite 时导入仍可用。
导出 CASES = {case_id: fn(ctx) -> assertion 列表}；每条断言都基于对真实 HTTP
目标发起真实请求并解析真实 HTML 响应，绝不使用 mock，也不读取应用数据库，
不重启服务进程。spec 中 A06–A10 的 implementation 为 acceptance/p0.py，它合并
本模块与 acceptance/p0_core.py 的 CASES 后交给 common.main 逐例执行；
本模块也可直接以 `python acceptance/p0_find.py --case A06 ...` 运行。
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


def _search_path(query):
    return '/?q=' + urllib.parse.quote(str(query), safe='')


def _bookmarks_in(ctx, path, client=None):
    '''GET path 并解析书签列表；非 200 时返回空列表。'''
    client = client if client is not None else ctx.target
    response = client.get(path)
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


def _create_collection(ctx, name):
    return ctx.target.post_form('/collections', {'name': name})


def _save_bookmark(ctx, url, title, collection_id=None):
    fields = {'url': url, 'title': title}
    if collection_id is not None:
        fields['collection_id'] = str(collection_id)
    return ctx.target.post_form('/bookmarks', fields)


def _by_url(items, url):
    return [item for item in items if item['url'] == url]


def case_a06(ctx):
    '''A06：按归类浏览只返回该归类记录，不会串入其他归类的记录。'''
    checks = []
    token = _token()
    name_a = 'A06甲-' + token
    name_b = 'A06乙-' + token
    url_a = 'https://example.com/a06-a-' + token
    url_b = 'https://example.com/a06-b-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created_a = _create_collection(ctx, name_a)
    created_b = _create_collection(ctx, name_b)
    checks.append(assertion('create-collection-a-303', created_a.status == 303,
                            'POST /collections name=%r status=%s' % (name_a, created_a.status)))
    checks.append(assertion('create-collection-b-303', created_b.status == 303,
                            'POST /collections name=%r status=%s' % (name_b, created_b.status)))

    collection_a = _find_collection(ctx, name_a)
    collection_b = _find_collection(ctx, name_b)
    checks.append(assertion('collection-a-in-sidebar', bool(collection_a and collection_a['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    checks.append(assertion('collection-b-in-sidebar', bool(collection_b and collection_b['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection_a and collection_a['id'] and collection_b and collection_b['id']):
        return checks
    aid = collection_a['id']
    bid = collection_b['id']

    saved_a = _save_bookmark(ctx, url_a, 'A06标题甲-' + token, aid)
    saved_b = _save_bookmark(ctx, url_b, 'A06标题乙-' + token, bid)
    checks.append(assertion('save-in-a-303', saved_a.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url_a, aid, saved_a.status)))
    checks.append(assertion('save-in-b-303', saved_b.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url_b, bid, saved_b.status)))

    view_a, items_a = _bookmarks_in(ctx, _collection_path(aid))
    checks.append(assertion('view-a-200', view_a.status == 200,
                            'GET %s status=%s' % (_collection_path(aid), view_a.status)))
    urls_a = [item['url'] for item in items_a]
    checks.append(assertion('view-a-has-own-record', urls_a.count(url_a) == 1,
                            'collection A urls=%r' % urls_a))
    checks.append(assertion('view-a-excludes-other-collection', url_b not in urls_a,
                            'collection A urls=%r must not contain %r' % (urls_a, url_b)))
    own_a = _by_url(items_a, url_a)
    if own_a and own_a[0]['collection_id'] is not None:
        checks.append(assertion('view-a-record-collection',
                                str(own_a[0]['collection_id']) == str(aid),
                                'expected collection=%s actual=%r'
                                % (aid, own_a[0]['collection_id'])))

    view_b, items_b = _bookmarks_in(ctx, _collection_path(bid))
    checks.append(assertion('view-b-200', view_b.status == 200,
                            'GET %s status=%s' % (_collection_path(bid), view_b.status)))
    urls_b = [item['url'] for item in items_b]
    checks.append(assertion('view-b-has-own-record', urls_b.count(url_b) == 1,
                            'collection B urls=%r' % urls_b))
    checks.append(assertion('view-b-excludes-other-collection', url_a not in urls_b,
                            'collection B urls=%r must not contain %r' % (urls_b, url_a)))
    return checks


def case_a07(ctx):
    '''A07：关键字检索命中标题与 URL 中的词，并排除不匹配的记录。

    P0 捕获表单只提供 url/title/collection_id，没有可写备注字段，故备注不作为
    P0 可驱动的检索来源；本用例对真实可写入的标题与 URL 分别检索并验证排除。
    '''
    checks = []
    token = _token()
    name = 'A07归类-' + token
    keyword = 'A07键' + token
    url_marker = 'a07url' + token
    url = 'https://example.com/' + url_marker
    title = keyword + ' 标题'
    other_url = 'https://example.com/a07-other-' + token
    other_title = 'A07无关-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title, cid)
    saved_other = _save_bookmark(ctx, other_url, other_title, cid)
    checks.append(assertion('save-match-303', saved.status == 303,
                            'POST /bookmarks url=%r title=%r status=%s'
                            % (url, title, saved.status)))
    checks.append(assertion('save-other-303', saved_other.status == 303,
                            'POST /bookmarks url=%r title=%r status=%s'
                            % (other_url, other_title, saved_other.status)))

    by_title_resp, by_title = _bookmarks_in(ctx, _search_path(keyword))
    checks.append(assertion('search-title-200', by_title_resp.status == 200,
                            'GET %s status=%s' % (_search_path(keyword), by_title_resp.status)))
    checks.append(assertion('search-title-hits-title', len(_by_url(by_title, url)) == 1,
                            'search %r listed %r'
                            % (keyword, [item['url'] for item in by_title])))
    checks.append(assertion('search-title-excludes-nonmatch', not _by_url(by_title, other_url),
                            'search %r listed %r must not contain %r'
                            % (keyword, [item['url'] for item in by_title], other_url)))

    by_url_resp, by_url_items = _bookmarks_in(ctx, _search_path(url_marker))
    checks.append(assertion('search-url-200', by_url_resp.status == 200,
                            'GET %s status=%s' % (_search_path(url_marker), by_url_resp.status)))
    checks.append(assertion('search-url-hits-url', len(_by_url(by_url_items, url)) == 1,
                            'search %r listed %r'
                            % (url_marker, [item['url'] for item in by_url_items])))
    checks.append(assertion('search-url-excludes-nonmatch',
                            not _by_url(by_url_items, other_url),
                            'search %r listed %r must not contain %r'
                            % (url_marker, [item['url'] for item in by_url_items], other_url)))
    return checks


def case_a08(ctx):
    '''A08：GET /go/<id> 返回 302，Location 等于保存的 URL，不代理正文。

    保存的 URL 使用 .invalid 主机（RFC 2606 保留、任何环境都不可解析）：若应用
    真去抓取目标页并把正文代理回来，抓取必然失败，就不可能返回带该 Location 的
    302；因此 302+Location 与“未代理正文”共同成立。用例不跟随该外部跳转。
    '''
    checks = []
    token = _token()
    name = 'A08归类-' + token
    url = 'https://a08.invalid/open-' + token
    title = 'A08标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title, cid)
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url, saved.status)))

    view, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d in %s'
                            % (len(found), len(items), _collection_path(cid))))
    if not found or not found[0]['id']:
        checks.append(assertion('record-has-id', False,
                                'data-bookmark-id missing for %r' % url))
        return checks
    bookmark_id = found[0]['id']
    checks.append(assertion('record-has-id', True, 'data-bookmark-id=%s' % bookmark_id))

    go = ctx.target.get('/go/' + str(bookmark_id))
    checks.append(assertion('go-302', go.status == 302,
                            'GET /go/%s status=%s (redirect not followed)'
                            % (bookmark_id, go.status)))
    checks.append(assertion('go-location-is-saved-url', go.location == url,
                            'Location=%r expected saved url=%r' % (go.location, url)))
    body = go.body or ''
    checks.append(assertion('go-does-not-proxy-body', len(body.strip()) < 2048,
                            'redirect body length=%d; target host is unresolvable, no proxied page returned'
                            % len(body.strip())))

    missing = ctx.target.get('/go/999999999')
    checks.append(assertion('go-unknown-404', missing.status == 404,
                            'GET /go/999999999 status=%s' % missing.status))
    return checks


def case_a09(ctx):
    '''A09：保存后由全新无会话 HTTP 客户端读回该记录，证明服务端已持久保存。

    本用例不读取应用数据库、不重启应用进程，也不声称已完成进程重启：仅证明数据
    经服务端提交后，可由一个全新的无 Cookie 客户端读回。
    '''
    checks = []
    token = _token()
    name = 'A09归类-' + token
    url = 'https://example.com/a09-' + token
    title = 'A09标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title, cid)
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url, cid, saved.status)))

    fresh = ctx.new_session()
    checks.append(assertion('fresh-client-distinct', fresh is not ctx.target,
                            'new_session returned a distinct client instance'))
    fresh_cookies = getattr(fresh, '_cookiejar', None)
    checks.append(assertion('fresh-client-stateless',
                            fresh_cookies is None or len(fresh_cookies) == 0,
                            'fresh client cookie count=%s'
                            % (None if fresh_cookies is None else len(fresh_cookies))))

    read_path = _collection_path(cid)
    read_resp, read_items = _bookmarks_in(ctx, read_path, fresh)
    checks.append(assertion('fresh-read-200', read_resp.status == 200,
                            'stateless client GET %s status=%s' % (read_path, read_resp.status)))
    read_hits = _by_url(read_items, url)
    checks.append(assertion('fresh-read-finds-record', len(read_hits) == 1,
                            'stateless client listed %r'
                            % [item['url'] for item in read_items]))
    if read_hits:
        checks.append(assertion('fresh-read-title', read_hits[0]['title'] == title,
                                'expected title=%r actual=%r'
                                % (title, read_hits[0]['title'])))

    search_path = _search_path(title)
    search_resp, search_items = _bookmarks_in(ctx, search_path, fresh)
    checks.append(assertion('fresh-search-200', search_resp.status == 200,
                            'stateless client GET %s status=%s'
                            % (search_path, search_resp.status)))
    checks.append(assertion('fresh-search-finds-record',
                            len(_by_url(search_items, url)) == 1,
                            'stateless client search listed %r'
                            % [item['url'] for item in search_items]))
    return checks


def case_a10(ctx):
    '''A10：无匹配关键字返回空结果不误报；未暴露的公开/分享路由 404 且不泄露记录。'''
    checks = []
    token = _token()
    name = 'A10归类-' + token
    url = 'https://example.com/a10-' + token
    title = 'A10标题-' + token

    home = ctx.target.get('/')
    checks.append(assertion('home-200', home.status == 200, 'GET / status=%s' % home.status))

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title, cid)
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url, cid, saved.status)))

    view, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    bookmark_id = found[0]['id'] if found else None

    nonce = 'zzz-nomatch-' + token
    empty_path = _search_path(nonce)
    empty_resp, empty_items = _bookmarks_in(ctx, empty_path)
    checks.append(assertion('no-match-search-200', empty_resp.status == 200,
                            'GET %s status=%s' % (empty_path, empty_resp.status)))
    checks.append(assertion('no-match-search-empty', len(empty_items) == 0,
                            'search %r listed %d bookmarks' % (nonce, len(empty_items))))
    checks.append(assertion('no-match-search-no-false-hit',
                            not _by_url(empty_items, url),
                            'search %r listed %r'
                            % (nonce, [item['url'] for item in empty_items])))

    routes = ['/share', '/public']
    if bookmark_id:
        routes.append('/share/' + str(bookmark_id))
        routes.append('/public/' + str(bookmark_id))
    for path in routes:
        label = path.replace('/', '-')
        resp = ctx.target.get(path)
        checks.append(assertion('hidden-route-404%s' % label, resp.status == 404,
                                'GET %s status=%s' % (path, resp.status)))
        leaked = (url in resp.body) or (title in resp.body)
        checks.append(assertion('hidden-route-no-leak%s' % label, not leaked,
                                'GET %s body must not expose stored url/title' % path))
    return checks


CASES = {
    'A06': case_a06,
    'A07': case_a07,
    'A08': case_a08,
    'A09': case_a09,
    'A10': case_a10,
}


if __name__ == '__main__':
    from acceptance.common import main as _run
    _run(CASES, sys.argv[1:])
