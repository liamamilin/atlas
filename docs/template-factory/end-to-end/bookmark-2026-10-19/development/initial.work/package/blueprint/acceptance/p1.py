'''acceptance/p1.py — P1 整理与维护用例（A11–A18）。

本脚本以 __file__ 定位套件根（sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))后导入 acceptance.common，并以其 main 直接驱动：
`python /suite/acceptance/p1.py --case A11..A18 --base-url <url> [--data-dir <dir>]
[--app-root <dir>]`。一个用例一次进程，stdout 恰一个 atlas.acceptance-result.v1 JSON，
诊断写 stderr，失败非零退出。

P1 沿用 P0 的 PRG／服务端渲染模式（全部经真实 HTTP 表单提交与真实 HTML 响应解析
验证，绝不使用 mock、不读取应用数据库、不重启进程）：
- 编辑记录 POST /bookmarks/<id>，字段 title、note（可选 tags，空白分隔）；成功 303，
  未知或已删除 id 返回 404；GET /bookmarks/<id> 返回 200 的真实编辑页并回显新值。
- 软删除 POST /bookmarks/<id>/delete 成功 303，记录进入 GET /trash 并与常规浏览和
  检索隔离；恢复 POST /bookmarks/<id>/restore 成功 303，未知或不在库 id 返回 404。
- 同 URL 再次保存收敛为同一记录（保持同一 data-bookmark-id），不新增第二条。
- GET /?collection=<id>、GET /?q=<kw>、GET /?tag=<name> 返回正确子集，默认按加入
  时间倒序（HTML 文档顺序即展示顺序）。
- POST /collections 可选 parent_id 建子归类，侧栏 li.collection 以 data-parent-id
  标注层级；POST /collections/<id>/rename 与 /collections/<id>/delete 成功 303；
  删除归类不级联删除记录，其记录回退默认收件箱（is_default=1，不可删除）。
- POST /bookmarks/<id> 的 tags 为记录标签集合；GET /tags 返回 200 标签索引。

导出 CASES = {case_id: fn(ctx) -> assertion 列表}；断言全部基于上述真实交互的响应，
不硬编码任何结论。
'''

import os
import sys
import time
import urllib.parse
import uuid

_SUITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _SUITE_ROOT not in sys.path:
    sys.path.insert(0, _SUITE_ROOT)

from acceptance.common import assertion, main, parse_list

__all__ = ['CASES']

# 明确不存在的记录 id，用于未知 id 的负例断言。
_UNKNOWN_ID = '999999999'


def _token():
    '''每次运行生成唯一后缀，避免共享目标上的用例互相污染。'''
    return uuid.uuid4().hex[:10]


def _quote(value):
    return urllib.parse.quote(str(value), safe='')


def _collection_path(collection_id):
    return '/?collection=' + _quote(collection_id)


def _search_path(query):
    return '/?q=' + _quote(query)


def _tag_path(tag):
    return '/?tag=' + _quote(tag)


def _bookmark_path(bookmark_id):
    return '/bookmarks/' + _quote(bookmark_id)


def _collection_endpoint(collection_id, action):
    return '/collections/' + _quote(collection_id) + '/' + action


def _create_collection(ctx, name, parent_id=None):
    '''新建归类；给定 parent_id 时创建子归类。'''
    fields = {'name': name}
    if parent_id is not None:
        fields['parent_id'] = str(parent_id)
    return ctx.target.post_form('/collections', fields)


def _save_bookmark(ctx, url, title, collection_id=None):
    fields = {'url': url, 'title': title}
    if collection_id is not None:
        fields['collection_id'] = str(collection_id)
    return ctx.target.post_form('/bookmarks', fields)


def _edit_bookmark(ctx, bookmark_id, **fields):
    '''POST /bookmarks/<id> 编辑 title、note 与 tags。'''
    return ctx.target.post_form(_bookmark_path(bookmark_id), fields)


def _delete_bookmark(ctx, bookmark_id):
    return ctx.target.post_form(_bookmark_path(bookmark_id) + '/delete', {})


def _restore_bookmark(ctx, bookmark_id):
    return ctx.target.post_form(_bookmark_path(bookmark_id) + '/restore', {})


def _move_bookmark(ctx, bookmark_id, collection_id):
    return ctx.target.post_form(_bookmark_path(bookmark_id) + '/move',
                                {'collection_id': str(collection_id)})


def _collections(ctx, client=None):
    '''GET / 并解析侧栏归类项。'''
    client = client if client is not None else ctx.target
    client.get('/')
    return parse_list(client.body)['collections']


def _find_collection(ctx, name):
    for collection in _collections(ctx):
        if collection['name'] == name:
            return collection
    return None


def _find_collection_by_id(ctx, collection_id):
    for collection in _collections(ctx):
        if str(collection['id']) == str(collection_id):
            return collection
    return None


def _default_collection(ctx):
    for collection in _collections(ctx):
        if collection['default']:
            return collection
    return None


def _bookmarks_in(ctx, path, client=None):
    '''GET path 并解析书签列表；非 200 时返回空列表。'''
    client = client if client is not None else ctx.target
    response = client.get(path)
    items = parse_list(response.body)['bookmarks'] if response.status == 200 else []
    return response, items


def _by_url(items, url):
    return [item for item in items if item['url'] == url]


def _index_of_url(items, url):
    for index, item in enumerate(items):
        if item['url'] == url:
            return index
    return -1


def _bookmark_key(item):
    if item['id']:
        return 'id:' + str(item['id'])
    return 'url:' + str(item['url']) + '|' + str(item['title'])


def _unique_records(ctx):
    '''汇总首页、各归类视图与回收站中的记录，按 id 去重。'''
    records = {}
    home = ctx.target.get('/')
    if home.status == 200:
        parsed = parse_list(home.body)
        for item in parsed['bookmarks']:
            records[_bookmark_key(item)] = item
        for collection in parsed['collections']:
            cid = collection['id']
            if not cid:
                continue
            response = ctx.target.get(_collection_path(cid))
            if response.status == 200:
                for item in parse_list(response.body)['bookmarks']:
                    records[_bookmark_key(item)] = item
    trash = ctx.target.get('/trash')
    if trash.status == 200:
        for item in parse_list(trash.body)['bookmarks']:
            records[_bookmark_key(item)] = item
    return records


def _library_keys(ctx):
    return set(_unique_records(ctx).keys())


def case_a11(ctx):
    '''A11：编辑标题与备注后，列表与编辑页显示新值且更改持久保留。'''
    checks = []
    token = _token()
    name = 'A11归类-' + token
    url = 'https://example.com/a11-' + token
    title_old = 'A11旧标题-' + token
    title_new = 'A11新标题-' + token
    note_new = 'A11新备注-' + token

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s location=%s'
                            % (name, created.status, created.location)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title_old, cid)
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url, cid, saved.status)))

    view, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    if not found or not found[0]['id']:
        checks.append(assertion('record-has-id', False, 'data-bookmark-id missing for %r' % url))
        return checks
    bookmark_id = found[0]['id']
    checks.append(assertion('record-has-id', True, 'data-bookmark-id=%s' % bookmark_id))

    edited = _edit_bookmark(ctx, bookmark_id, title=title_new, note=note_new)
    checks.append(assertion('edit-303', edited.status == 303,
                            'POST /bookmarks/%s title=%r note=%r status=%s'
                            % (bookmark_id, title_new, note_new, edited.status)))

    edit_page = ctx.target.get(_bookmark_path(bookmark_id))
    checks.append(assertion('edit-page-200', edit_page.status == 200,
                            'GET /bookmarks/%s status=%s' % (bookmark_id, edit_page.status)))
    checks.append(assertion('edit-page-shows-new-title', title_new in edit_page.body,
                            'edit page must show title %r' % title_new))
    checks.append(assertion('edit-page-shows-new-note', note_new in edit_page.body,
                            'edit page must show note %r' % note_new))

    list_view, list_items = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('list-view-200', list_view.status == 200,
                            'GET %s status=%s' % (_collection_path(cid), list_view.status)))
    listed = _by_url(list_items, url)
    checks.append(assertion('record-still-listed', len(listed) == 1,
                            'matching url count=%d of %d' % (len(listed), len(list_items))))
    if listed:
        checks.append(assertion('list-shows-new-title', listed[0]['title'] == title_new,
                                'expected title=%r actual=%r' % (title_new, listed[0]['title'])))
        checks.append(assertion('list-no-longer-old-title', listed[0]['title'] != title_old,
                                'title must not remain %r' % title_old))
    checks.append(assertion('list-shows-new-note', note_new in list_view.body,
                            'list must render note %r' % note_new))

    fresh = ctx.new_session()
    fresh_view, fresh_items = _bookmarks_in(ctx, _collection_path(cid), fresh)
    fresh_listed = _by_url(fresh_items, url)
    checks.append(assertion('fresh-read-200', fresh_view.status == 200,
                            'stateless client GET %s status=%s'
                            % (_collection_path(cid), fresh_view.status)))
    checks.append(assertion('fresh-read-new-title',
                            bool(fresh_listed) and fresh_listed[0]['title'] == title_new,
                            'stateless client listed title=%r'
                            % (fresh_listed[0]['title'] if fresh_listed else None)))
    checks.append(assertion('fresh-read-new-note', note_new in fresh_view.body,
                            'stateless client must render note %r' % note_new))
    return checks


def case_a12(ctx):
    '''A12：删除进入 /trash、从常规视图与检索排除；恢复后重新可见。'''
    checks = []
    token = _token()
    name = 'A12归类-' + token
    url = 'https://example.com/a12-' + token
    title = 'A12标题-' + token

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
    _, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    if not found or not found[0]['id']:
        checks.append(assertion('record-has-id', False, 'data-bookmark-id missing for %r' % url))
        return checks
    bookmark_id = found[0]['id']
    checks.append(assertion('record-has-id', True, 'data-bookmark-id=%s' % bookmark_id))

    deleted = _delete_bookmark(ctx, bookmark_id)
    checks.append(assertion('delete-303', deleted.status == 303,
                            'POST /bookmarks/%s/delete status=%s' % (bookmark_id, deleted.status)))

    _, items_after = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('excluded-from-collection', not _by_url(items_after, url),
                            'collection listed %r' % [item['url'] for item in items_after]))
    home_view, home_items = _bookmarks_in(ctx, '/')
    checks.append(assertion('excluded-from-home', not _by_url(home_items, url),
                            'home listed %r' % [item['url'] for item in home_items]))
    search_view, search_items = _bookmarks_in(ctx, _search_path(title))
    checks.append(assertion('excluded-from-search', not _by_url(search_items, url),
                            'search listed %r' % [item['url'] for item in search_items]))

    trash = ctx.target.get('/trash')
    checks.append(assertion('trash-200', trash.status == 200, 'GET /trash status=%s' % trash.status))
    checks.append(assertion('record-in-trash', url in trash.body,
                            'GET /trash body must show %r' % url))

    restored = _restore_bookmark(ctx, bookmark_id)
    checks.append(assertion('restore-303', restored.status == 303,
                            'POST /bookmarks/%s/restore status=%s' % (bookmark_id, restored.status)))

    view_restored, items_restored = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('visible-after-restore', len(_by_url(items_restored, url)) == 1,
                            'collection listed %r' % [item['url'] for item in items_restored]))
    trash_after = ctx.target.get('/trash')
    checks.append(assertion('removed-from-trash', url not in trash_after.body,
                            'GET /trash body must not show %r after restore' % url))
    return checks


def case_a13(ctx):
    '''A13：已删除记录不出现在浏览与检索；未知或已删除 id 的编辑、移动、恢复返回 404 且库不变。'''
    checks = []
    token = _token()
    name = 'A13归类-' + token
    url = 'https://example.com/a13-' + token
    title = 'A13标题-' + token

    baseline = _library_keys(ctx)
    checks.append(assertion('baseline-snapshot', True, 'library keys before=%d' % len(baseline)))

    edit_unknown = _edit_bookmark(ctx, _UNKNOWN_ID, title='A13未知', note='A13未知')
    checks.append(assertion('unknown-edit-404', edit_unknown.status == 404,
                            'POST /bookmarks/%s status=%s' % (_UNKNOWN_ID, edit_unknown.status)))
    move_unknown = _move_bookmark(ctx, _UNKNOWN_ID, 1)
    checks.append(assertion('unknown-move-404', move_unknown.status == 404,
                            'POST /bookmarks/%s/move status=%s' % (_UNKNOWN_ID, move_unknown.status)))
    restore_unknown = _restore_bookmark(ctx, _UNKNOWN_ID)
    checks.append(assertion('unknown-restore-404', restore_unknown.status == 404,
                            'POST /bookmarks/%s/restore status=%s' % (_UNKNOWN_ID, restore_unknown.status)))

    after_unknown = _library_keys(ctx)
    checks.append(assertion('library-unchanged-after-unknown', baseline == after_unknown,
                            'before=%d after=%d added=%r removed=%r'
                            % (len(baseline), len(after_unknown),
                               sorted(after_unknown - baseline), sorted(baseline - after_unknown))))

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
    _, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    if not found or not found[0]['id']:
        checks.append(assertion('record-has-id', False, 'data-bookmark-id missing for %r' % url))
        return checks
    bookmark_id = found[0]['id']
    checks.append(assertion('record-has-id', True, 'data-bookmark-id=%s' % bookmark_id))

    deleted = _delete_bookmark(ctx, bookmark_id)
    checks.append(assertion('delete-303', deleted.status == 303,
                            'POST /bookmarks/%s/delete status=%s' % (bookmark_id, deleted.status)))

    view, items_after = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('deleted-excluded-from-collection', not _by_url(items_after, url),
                            'collection listed %r' % [item['url'] for item in items_after]))
    home_view, home_items = _bookmarks_in(ctx, '/')
    checks.append(assertion('deleted-excluded-from-home', not _by_url(home_items, url),
                            'home listed %r' % [item['url'] for item in home_items]))
    search_view, search_items = _bookmarks_in(ctx, _search_path(title))
    checks.append(assertion('deleted-excluded-from-search', not _by_url(search_items, url),
                            'search listed %r' % [item['url'] for item in search_items]))

    trash = ctx.target.get('/trash')
    checks.append(assertion('trash-200', trash.status == 200, 'GET /trash status=%s' % trash.status))
    checks.append(assertion('deleted-record-in-trash', url in trash.body,
                            'GET /trash body must show %r' % url))

    after_delete = _library_keys(ctx)

    edit_deleted = _edit_bookmark(ctx, bookmark_id, title='A13改')
    checks.append(assertion('deleted-edit-404', edit_deleted.status == 404,
                            'POST /bookmarks/%s status=%s' % (bookmark_id, edit_deleted.status)))
    move_deleted = _move_bookmark(ctx, bookmark_id, cid)
    checks.append(assertion('deleted-move-404', move_deleted.status == 404,
                            'POST /bookmarks/%s/move status=%s' % (bookmark_id, move_deleted.status)))

    after_failed = _library_keys(ctx)
    checks.append(assertion('library-unchanged-after-deleted-ops', after_delete == after_failed,
                            'before=%d after=%d added=%r removed=%r'
                            % (len(after_delete), len(after_failed),
                               sorted(after_failed - after_delete), sorted(after_delete - after_failed))))
    return checks


def case_a14(ctx):
    '''A14：同 URL 再次保存不产生第二条记录，原记录被更新而非复制。'''
    checks = []
    token = _token()
    name = 'A14归类-' + token
    url = 'https://example.com/a14-' + token
    title_first = 'A14首次-' + token
    title_second = 'A14再次-' + token

    created = _create_collection(ctx, name)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name, created.status)))
    collection = _find_collection(ctx, name)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved_first = _save_bookmark(ctx, url, title_first, cid)
    checks.append(assertion('first-save-303', saved_first.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url, saved_first.status)))
    _, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('first-record-present', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    if not found or not found[0]['id']:
        checks.append(assertion('first-record-has-id', False, 'data-bookmark-id missing for %r' % url))
        return checks
    first_id = found[0]['id']

    saved_second = _save_bookmark(ctx, url, title_second, cid)
    checks.append(assertion('second-save-303', saved_second.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url, saved_second.status)))

    _, items_after = _bookmarks_in(ctx, _collection_path(cid))
    matching = _by_url(items_after, url)
    checks.append(assertion('collection-single-record', len(matching) == 1,
                            'matching url count=%d of %d' % (len(matching), len(items_after))))
    if matching:
        checks.append(assertion('record-updated-title', matching[0]['title'] == title_second,
                                'expected title=%r actual=%r' % (title_second, matching[0]['title'])))
        checks.append(assertion('record-not-copied-title', matching[0]['title'] != title_first,
                                'stale title %r must be replaced' % title_first))

    records = _unique_records(ctx)
    library_matches = [item for item in records.values() if item['url'] == url]
    checks.append(assertion('library-single-record', len(library_matches) == 1,
                            'unique library records for url=%d' % len(library_matches)))
    if library_matches:
        checks.append(assertion('record-kept-id', str(library_matches[0]['id']) == str(first_id),
                                'expected id=%s actual=%r' % (first_id, library_matches[0]['id'])))
    return checks


def case_a15(ctx):
    '''A15：默认按加入时间倒序，按归类与关键字筛选返回正确子集与顺序。'''
    checks = []
    token = _token()
    name_c = 'A15丙-' + token
    name_d = 'A15丁-' + token
    keyword = 'A15键' + token
    keyword_other = 'A15另' + token
    url_1 = 'https://example.com/a15-1-' + token
    url_2 = 'https://example.com/a15-2-' + token
    url_3 = 'https://example.com/a15-3-' + token

    created_c = _create_collection(ctx, name_c)
    created_d = _create_collection(ctx, name_d)
    checks.append(assertion('create-collection-c-303', created_c.status == 303,
                            'POST /collections name=%r status=%s' % (name_c, created_c.status)))
    checks.append(assertion('create-collection-d-303', created_d.status == 303,
                            'POST /collections name=%r status=%s' % (name_d, created_d.status)))
    collection_c = _find_collection(ctx, name_c)
    collection_d = _find_collection(ctx, name_d)
    checks.append(assertion('collection-c-in-sidebar', bool(collection_c and collection_c['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    checks.append(assertion('collection-d-in-sidebar', bool(collection_d and collection_d['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection_c and collection_c['id'] and collection_d and collection_d['id']):
        return checks
    cid = collection_c['id']
    did = collection_d['id']

    saved_1 = _save_bookmark(ctx, url_1, keyword + ' 第一', cid)
    checks.append(assertion('save-first-303', saved_1.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url_1, saved_1.status)))
    time.sleep(1.1)
    saved_2 = _save_bookmark(ctx, url_2, keyword + ' 第二', cid)
    checks.append(assertion('save-second-303', saved_2.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url_2, saved_2.status)))
    saved_3 = _save_bookmark(ctx, url_3, keyword_other + ' 第三', did)
    checks.append(assertion('save-other-303', saved_3.status == 303,
                            'POST /bookmarks url=%r status=%s' % (url_3, saved_3.status)))

    view_c, items_c = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('collection-view-200', view_c.status == 200,
                            'GET %s status=%s' % (_collection_path(cid), view_c.status)))
    urls_c = [item['url'] for item in items_c]
    checks.append(assertion('collection-has-newest', url_2 in urls_c, 'collection C urls=%r' % urls_c))
    checks.append(assertion('collection-has-older', url_1 in urls_c, 'collection C urls=%r' % urls_c))
    checks.append(assertion('collection-excludes-other', url_3 not in urls_c,
                            'collection C urls=%r must not contain %r' % (urls_c, url_3)))
    index_2 = _index_of_url(items_c, url_2)
    index_1 = _index_of_url(items_c, url_1)
    checks.append(assertion('collection-newest-first',
                            index_2 != -1 and index_1 != -1 and index_2 < index_1,
                            'newest index=%d older index=%d' % (index_2, index_1)))

    search_view, search_items = _bookmarks_in(ctx, _search_path(keyword))
    checks.append(assertion('search-view-200', search_view.status == 200,
                            'GET %s status=%s' % (_search_path(keyword), search_view.status)))
    search_urls = [item['url'] for item in search_items]
    checks.append(assertion('search-hits-both', url_1 in search_urls and url_2 in search_urls,
                            'search %r listed %r' % (keyword, search_urls)))
    checks.append(assertion('search-excludes-other', url_3 not in search_urls,
                            'search %r listed %r must not contain %r' % (keyword, search_urls, url_3)))
    s_index_2 = _index_of_url(search_items, url_2)
    s_index_1 = _index_of_url(search_items, url_1)
    checks.append(assertion('search-newest-first',
                            s_index_2 != -1 and s_index_1 != -1 and s_index_2 < s_index_1,
                            'newest index=%d older index=%d' % (s_index_2, s_index_1)))

    other_view, other_items = _bookmarks_in(ctx, _search_path(keyword_other))
    other_urls = [item['url'] for item in other_items]
    checks.append(assertion('other-search-view-200', other_view.status == 200,
                            'GET %s status=%s' % (_search_path(keyword_other), other_view.status)))
    checks.append(assertion('other-search-hits-own', url_3 in other_urls,
                            'search %r listed %r' % (keyword_other, other_urls)))
    checks.append(assertion('other-search-excludes-unrelated',
                            url_1 not in other_urls and url_2 not in other_urls,
                            'search %r listed %r' % (keyword_other, other_urls)))
    return checks


def case_a16(ctx):
    '''A16：在父归类下新建子归类，可在父与子层级浏览并把记录移动到子归类。'''
    checks = []
    token = _token()
    parent_name = 'A16父-' + token
    child_name = 'A16子-' + token
    url_child = 'https://example.com/a16-child-' + token
    url_moved = 'https://example.com/a16-moved-' + token

    created_parent = _create_collection(ctx, parent_name)
    checks.append(assertion('create-parent-303', created_parent.status == 303,
                            'POST /collections name=%r status=%s' % (parent_name, created_parent.status)))
    parent = _find_collection(ctx, parent_name)
    checks.append(assertion('parent-in-sidebar', bool(parent and parent['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (parent and parent['id']):
        return checks
    pid = parent['id']

    created_child = _create_collection(ctx, child_name, parent_id=pid)
    checks.append(assertion('create-child-303', created_child.status == 303,
                            'POST /collections name=%r parent_id=%s status=%s'
                            % (child_name, pid, created_child.status)))
    child = _find_collection(ctx, child_name)
    checks.append(assertion('child-in-sidebar', bool(child and child['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (child and child['id']):
        return checks
    cid = child['id']
    checks.append(assertion('child-distinct-from-parent', str(cid) != str(pid),
                            'child id=%s parent id=%s' % (cid, pid)))
    checks.append(assertion('child-parent-id', str(child['parent_id']) == str(pid),
                            'child data-parent-id=%r expected %s' % (child['parent_id'], pid)))

    parent_view, _parent_items = _bookmarks_in(ctx, _collection_path(pid))
    checks.append(assertion('parent-view-200', parent_view.status == 200,
                            'GET %s status=%s' % (_collection_path(pid), parent_view.status)))
    child_view, _child_items = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('child-view-200', child_view.status == 200,
                            'GET %s status=%s' % (_collection_path(cid), child_view.status)))

    saved_child = _save_bookmark(ctx, url_child, 'A16子标题-' + token, cid)
    checks.append(assertion('save-to-child-303', saved_child.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url_child, cid, saved_child.status)))
    _, child_items = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('record-in-child', len(_by_url(child_items, url_child)) == 1,
                            'child view listed %r' % [item['url'] for item in child_items]))

    saved_parent = _save_bookmark(ctx, url_moved, 'A16移动标题-' + token, pid)
    checks.append(assertion('save-to-parent-303', saved_parent.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url_moved, pid, saved_parent.status)))
    _, parent_items = _bookmarks_in(ctx, _collection_path(pid))
    found = _by_url(parent_items, url_moved)
    checks.append(assertion('record-in-parent', len(found) == 1,
                            'parent view listed %r' % [item['url'] for item in parent_items]))
    if not (found and found[0]['id']):
        checks.append(assertion('moved-record-has-id', False, 'data-bookmark-id missing for %r' % url_moved))
        return checks
    moved = _move_bookmark(ctx, found[0]['id'], cid)
    checks.append(assertion('move-to-child-303', moved.status == 303,
                            'POST /bookmarks/%s/move collection_id=%s status=%s'
                            % (found[0]['id'], cid, moved.status)))
    _, child_after = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('moved-record-in-child', len(_by_url(child_after, url_moved)) == 1,
                            'child view listed %r' % [item['url'] for item in child_after]))
    _, parent_after = _bookmarks_in(ctx, _collection_path(pid))
    checks.append(assertion('moved-record-not-in-parent', not _by_url(parent_after, url_moved),
                            'parent view listed %r' % [item['url'] for item in parent_after]))
    return checks


def case_a17(ctx):
    '''A17：归类重命名生效；删除归类时记录回退默认收件箱而不被级联删除。'''
    checks = []
    token = _token()
    name_old = 'A17旧名-' + token
    name_new = 'A17新名-' + token
    url = 'https://example.com/a17-' + token
    title = 'A17标题-' + token

    created = _create_collection(ctx, name_old)
    checks.append(assertion('create-collection-303', created.status == 303,
                            'POST /collections name=%r status=%s' % (name_old, created.status)))
    collection = _find_collection(ctx, name_old)
    checks.append(assertion('collection-in-sidebar', bool(collection and collection['id']),
                            'sidebar collections=%r' % [c['name'] for c in _collections(ctx)]))
    if not (collection and collection['id']):
        return checks
    cid = collection['id']

    saved = _save_bookmark(ctx, url, title, cid)
    checks.append(assertion('save-303', saved.status == 303,
                            'POST /bookmarks url=%r collection_id=%s status=%s'
                            % (url, cid, saved.status)))

    renamed = ctx.target.post_form(_collection_endpoint(cid, 'rename'), {'name': name_new})
    checks.append(assertion('rename-303', renamed.status == 303,
                            'POST /collections/%s/rename name=%r status=%s'
                            % (cid, name_new, renamed.status)))
    renamed_collection = _find_collection_by_id(ctx, cid)
    checks.append(assertion('renamed-collection-present', bool(renamed_collection),
                            'collection id %s present=%s' % (cid, bool(renamed_collection))))
    if renamed_collection:
        checks.append(assertion('rename-applied', renamed_collection['name'] == name_new,
                                'expected name=%r actual=%r'
                                % (name_new, renamed_collection['name'])))
    checks.append(assertion('old-name-gone', _find_collection(ctx, name_old) is None,
                            'sidebar must not contain %r' % name_old))

    view, items = _bookmarks_in(ctx, _collection_path(cid))
    checks.append(assertion('record-in-renamed-collection', len(_by_url(items, url)) == 1,
                            'matching url count=%d of %d' % (len(_by_url(items, url)), len(items))))

    default_before = _default_collection(ctx)
    checks.append(assertion('default-inbox-present', bool(default_before and default_before['id']),
                            'default collection=%r' % (default_before and default_before.get('name'))))

    before = _library_keys(ctx)
    deleted = ctx.target.post_form(_collection_endpoint(cid, 'delete'), {})
    checks.append(assertion('delete-collection-303', deleted.status == 303,
                            'POST /collections/%s/delete status=%s' % (cid, deleted.status)))
    checks.append(assertion('collection-gone', _find_collection_by_id(ctx, cid) is None,
                            'collection id %s must be removed from sidebar' % cid))
    default_after = _default_collection(ctx)
    checks.append(assertion('default-inbox-survives', bool(default_after and default_after['id']),
                            'default collection=%r' % (default_after and default_after.get('name'))))

    after = _library_keys(ctx)
    checks.append(assertion('records-not-cascade-deleted', before == after,
                            'library keys before=%d after=%d removed=%r'
                            % (len(before), len(after), sorted(before - after))))

    inbox_view, inbox_items = _bookmarks_in(ctx, '/?collection=inbox')
    checks.append(assertion('record-falls-back-to-inbox', len(_by_url(inbox_items, url)) == 1,
                            'inbox listed %r' % [item['url'] for item in inbox_items]))
    if default_before and default_before['id']:
        default_view, default_items = _bookmarks_in(ctx, _collection_path(default_before['id']))
        checks.append(assertion('record-in-default-collection',
                                len(_by_url(default_items, url)) == 1,
                                'default collection listed %r'
                                % [item['url'] for item in default_items]))
    return checks


def case_a18(ctx):
    '''A18：为记录添加与移除标签，并按标签浏览出对应记录。'''
    checks = []
    token = _token()
    name = 'A18归类-' + token
    url = 'https://example.com/a18-' + token
    title = 'A18标题-' + token
    tag_a = 'a18tagA' + token
    tag_b = 'a18tagB' + token

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
    _, items = _bookmarks_in(ctx, _collection_path(cid))
    found = _by_url(items, url)
    checks.append(assertion('record-located', len(found) == 1,
                            'matching url count=%d of %d' % (len(found), len(items))))
    if not found or not found[0]['id']:
        checks.append(assertion('record-has-id', False, 'data-bookmark-id missing for %r' % url))
        return checks
    bookmark_id = found[0]['id']
    checks.append(assertion('record-has-id', True, 'data-bookmark-id=%s' % bookmark_id))

    added = _edit_bookmark(ctx, bookmark_id, title=title, tags=tag_a + ' ' + tag_b)
    checks.append(assertion('add-tags-303', added.status == 303,
                            'POST /bookmarks/%s tags=%r status=%s'
                            % (bookmark_id, tag_a + ' ' + tag_b, added.status)))

    tags_index = ctx.target.get('/tags')
    checks.append(assertion('tags-index-200', tags_index.status == 200,
                            'GET /tags status=%s' % tags_index.status))
    checks.append(assertion('tags-index-lists-tag', tag_a in tags_index.body,
                            'GET /tags body must show %r' % tag_a))

    view_a, items_a = _bookmarks_in(ctx, _tag_path(tag_a))
    checks.append(assertion('browse-tag-a-200', view_a.status == 200,
                            'GET %s status=%s' % (_tag_path(tag_a), view_a.status)))
    checks.append(assertion('browse-tag-a-finds-record', len(_by_url(items_a, url)) == 1,
                            'tag %r listed %r' % (tag_a, [item['url'] for item in items_a])))
    view_b, items_b = _bookmarks_in(ctx, _tag_path(tag_b))
    checks.append(assertion('browse-tag-b-finds-record', len(_by_url(items_b, url)) == 1,
                            'tag %r listed %r' % (tag_b, [item['url'] for item in items_b])))

    removed = _edit_bookmark(ctx, bookmark_id, title=title, tags=tag_a)
    checks.append(assertion('remove-tag-303', removed.status == 303,
                            'POST /bookmarks/%s tags=%r status=%s'
                            % (bookmark_id, tag_a, removed.status)))

    view_b_after, items_b_after = _bookmarks_in(ctx, _tag_path(tag_b))
    checks.append(assertion('removed-tag-excludes-record', not _by_url(items_b_after, url),
                            'tag %r listed %r' % (tag_b, [item['url'] for item in items_b_after])))
    view_a_after, items_a_after = _bookmarks_in(ctx, _tag_path(tag_a))
    checks.append(assertion('kept-tag-still-finds-record', len(_by_url(items_a_after, url)) == 1,
                            'tag %r listed %r' % (tag_a, [item['url'] for item in items_a_after])))
    return checks


CASES = {
    'A11': case_a11,
    'A12': case_a12,
    'A13': case_a13,
    'A14': case_a14,
    'A15': case_a15,
    'A16': case_a16,
    'A17': case_a17,
    'A18': case_a18,
}


if __name__ == '__main__':
    main(CASES, sys.argv[1:])
