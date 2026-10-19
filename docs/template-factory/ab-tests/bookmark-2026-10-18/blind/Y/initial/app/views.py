"""服务端渲染的中文 HTML 视图。所有写入表单 method=post，查询表单 method=get。"""

import html
from urllib.parse import urlencode


def esc(value):
    return html.escape("" if value is None else str(value), quote=True)


def _page_query(q, category_id, sort, limit, offset):
    params = []
    if q:
        params.append(("q", q))
    if category_id:
        params.append(("categoryId", category_id))
    params.append(("sort", sort))
    params.append(("limit", str(limit)))
    params.append(("offset", str(offset)))
    return urlencode(params)


def _layout(base, nav_html, flash, form_error, main_html, dialog_html=""):
    if flash:
        flash_html = '<div data-testid="flash" role="status" class="flash">%s</div>' % esc(flash)
    else:
        flash_html = ""
    if form_error:
        error_html = ('<div data-testid="form-error" role="alert" class="error">%s</div>'
                      % esc(form_error))
    else:
        error_html = '<div data-testid="form-error" role="alert" class="error"></div>'
    return (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>生活待购与灵感收藏夹</title>\n"
        '<link rel="stylesheet" href="%s/static/style.css">\n'
        "</head>\n<body>\n"
        '<header class="topbar"><a class="brand" href="%s/">生活待购与灵感收藏夹</a>%s</header>\n'
        "<main>\n%s\n%s\n%s\n</main>\n%s\n"
        '<script src="%s/static/app.js" defer></script>\n'
        "</body>\n</html>\n"
    ) % (esc(base), esc(base), nav_html, flash_html, error_html, main_html, dialog_html, esc(base))


def _nav(base, categories, show_delete=True):
    links = []
    for category in categories:
        cid = esc(category["id"])
        name = esc(category["name"])
        links.append(
            '<span class="nav-item"><a data-testid="category-link" data-category-id="%s"'
            ' href="%s/c/%s">%s</a>' % (cid, esc(base), cid, name)
        )
        if show_delete and not category["isDefault"]:
            links.append(
                '<button type="button" data-testid="category-delete" data-category-id="%s">删除</button>'
                % cid
            )
        links.append("</span>")
    links.append('<a data-testid="trash-link" href="%s/trash">回收站</a>' % esc(base))
    return '<nav class="nav">' + "".join(links) + "</nav>"


def _category_options(categories, selected_id, exclude_id=None, include_blank=False,
                      blank_label="（回到原归类）"):
    parts = []
    if include_blank:
        parts.append('<option value="">%s</option>' % esc(blank_label))
    for category in categories:
        if exclude_id is not None and str(category["id"]) == str(exclude_id):
            continue
        selected = " selected" if str(category["id"]) == str(selected_id) else ""
        parts.append('<option value="%s"%s>%s</option>'
                     % (esc(category["id"]), selected, esc(category["name"])))
    return "".join(parts)


def _dialog(base, categories, dialog):
    open_dialog = dialog is not None
    category_id = dialog.get("categoryId") if dialog else None
    error = dialog.get("error") if dialog else None
    target_id = dialog.get("targetId") if dialog else None
    action = "%s/categories/%s/delete" % (base, category_id if category_id is not None else "0")
    options = _category_options(categories, target_id, exclude_id=category_id)
    error_text = esc(error) if error else ""
    cls = "dialog open" if open_dialog else "dialog"
    hidden = "" if open_dialog else " hidden"
    return (
        '<div data-testid="category-delete-dialog" data-base-path="%s" class="%s"%s>\n'
        '<div class="dialog-box" role="dialog" aria-modal="true">\n'
        "<h2>删除归类</h2>\n"
        '<div data-testid="dialog-error" role="alert" class="error">%s</div>\n'
        '<form class="dialog-form" method="post" action="%s">\n'
        '<input type="hidden" name="mode" value="move">\n'
        '<label>把其中的记录移动到：<select name="targetCategoryId">%s</select></label>\n'
        '<button type="submit" data-testid="delete-move">移动并删除归类</button>\n'
        "</form>\n"
        '<form class="dialog-form" method="post" action="%s">\n'
        '<input type="hidden" name="mode" value="purge">\n'
        '<input type="hidden" name="confirm" value="true">\n'
        '<label><input type="checkbox" data-testid="confirm-purge"> 我确认把其中记录移入回收站</label>\n'
        '<button type="submit" data-testid="delete-purge">永久删除归类</button>\n'
        "</form>\n"
        '<button type="button" data-testid="delete-cancel">取消</button>\n'
        "</div>\n</div>\n"
    ) % (esc(base), cls, hidden, error_text, esc(action), options, esc(action))


def _save_form(base, categories, values, duplicate, default_id):
    selected = values.get("categoryId") or default_id
    parts = [
        '<form data-testid="bookmark-form" method="post" action="%s/bookmarks" novalidate>\n'
        % esc(base),
        '<input name="url" type="text" placeholder="粘贴网址" value="%s">\n' % esc(values.get("url", "")),
        '<input name="title" placeholder="标题（可留空）" value="%s">\n' % esc(values.get("title", "")),
        '<textarea name="note" placeholder="备注（可留空）">%s</textarea>\n' % esc(values.get("note", "")),
        '<select name="categoryId">%s</select>\n' % _category_options(categories, selected),
        '<button type="submit" data-testid="bookmark-submit">保存到收藏夹</button>\n',
        "</form>\n",
    ]
    if duplicate:
        existing_id = esc(duplicate["existingId"])
        duplicate_selected = duplicate.get("categoryId") or default_id
        parts.append(
            '<p class="duplicate">这个网址已经保存过了：'
            '<a data-testid="duplicate-existing-link" href="%s/b/%s">查看已有记录</a></p>\n'
            % (esc(base), existing_id)
        )
        parts.append(
            '<form data-testid="duplicate-save-form" method="post" action="%s/bookmarks">\n'
            % esc(base)
        )
        parts.append('<input type="hidden" name="allowDuplicate" value="true">\n')
        parts.append('<input name="url" type="text" value="%s">\n' % esc(duplicate.get("url", "")))
        parts.append('<input name="title" value="%s">\n' % esc(duplicate.get("title", "")))
        parts.append('<input name="note" value="%s">\n' % esc(duplicate.get("note", "")))
        parts.append('<input name="categoryId" value="%s">\n' % esc(duplicate_selected))
        parts.append(
            '<button type="submit" data-testid="duplicate-save-submit">仍然保存一份</button>\n'
        )
        parts.append("</form>\n")
    return "".join(parts)


def _row(base, bookmark, categories, prefill=None):
    bid = esc(bookmark["id"])
    cid = esc(bookmark["categoryId"])
    title = bookmark["title"]
    edit_title = prefill.get("title") if prefill and "title" in prefill else title
    edit_note = prefill.get("note") if prefill and "note" in prefill else bookmark["note"]
    move_selected = (prefill.get("categoryId") if prefill and "categoryId" in prefill
                     else bookmark["categoryId"])
    return (
        '<article class="bookmark" data-testid="bookmark-item" data-bookmark-id="%s"'
        ' data-category-id="%s">\n'
        '<h3><a data-testid="open-link" href="%s/b/%s">%s</a></h3>\n'
        '<p><span data-testid="bookmark-title">%s</span></p>\n'
        '<p class="url"><span data-testid="bookmark-url">%s</span></p>\n'
        '<p class="meta"><span data-testid="bookmark-category">%s</span> · '
        '<time data-testid="bookmark-created" datetime="%s">%s</time></p>\n'
        '<form data-testid="move-form" method="post" action="%s/bookmarks/%s/move">\n'
        '<select name="categoryId">%s</select>'
        '<button type="submit" data-testid="move-submit">移动</button>\n</form>\n'
        '<form data-testid="bookmark-edit-form" data-bookmark-id="%s" method="post"'
        ' action="%s/bookmarks/%s/edit">\n'
        '<input name="title" value="%s">\n'
        '<textarea name="note">%s</textarea>\n'
        '<button type="submit" data-testid="bookmark-edit-submit">保存编辑</button>\n</form>\n'
        '<form data-testid="bookmark-delete-form" method="post" action="%s/bookmarks/%s/delete">\n'
        '<button type="submit" data-testid="bookmark-delete-submit">删除</button>\n</form>\n'
        "</article>\n"
    ) % (
        bid, cid,
        esc(base), bid, esc(title),
        esc(title),
        esc(bookmark["url"]),
        esc(bookmark["categoryName"]), esc(bookmark["createdAt"]), esc(bookmark["createdAt"]),
        esc(base), bid, _category_options(categories, move_selected),
        bid, esc(base), bid, esc(edit_title), esc(edit_note),
        esc(base), bid,
    )


def _pagination(base, q, category_id, sort, limit, offset, total):
    prev_html = ""
    next_html = ""
    if offset > 0:
        prev_offset = max(0, offset - limit)
        href = "%s/?%s" % (base, _page_query(q, category_id, sort, limit, prev_offset))
        prev_html = '<a data-testid="page-prev" href="%s">上一页</a>' % esc(href)
    else:
        prev_html = '<a data-testid="page-prev" aria-disabled="true">上一页</a>'
    if offset + limit < total:
        next_offset = offset + limit
        href = "%s/?%s" % (base, _page_query(q, category_id, sort, limit, next_offset))
        next_html = '<a data-testid="page-next" href="%s">下一页</a>' % esc(href)
    else:
        next_html = '<a data-testid="page-next" aria-disabled="true">下一页</a>'
    return '<nav class="pager">%s%s</nav>' % (prev_html, next_html)


def _search_and_sort(base, q, category_id, sort, limit):
    hidden = []
    if category_id:
        hidden.append('<input type="hidden" name="categoryId" value="%s">' % esc(category_id))
    hidden.append('<input type="hidden" name="sort" value="%s">' % esc(sort))
    hidden.append('<input type="hidden" name="limit" value="%s">' % esc(limit))
    hidden_html = "".join(hidden)

    sort_hidden = []
    if q:
        sort_hidden.append('<input type="hidden" name="q" value="%s">' % esc(q))
    if category_id:
        sort_hidden.append('<input type="hidden" name="categoryId" value="%s">' % esc(category_id))
    sort_hidden.append('<input type="hidden" name="limit" value="%s">' % esc(limit))
    desc_sel = " selected" if sort == "created_desc" else ""
    asc_sel = " selected" if sort == "created_asc" else ""

    return (
        '<form data-testid="search-form" method="get" action="%s/">\n'
        '<input name="q" value="%s" placeholder="按关键字查找">%s'
        '<button type="submit" data-testid="search-submit">搜索</button>\n</form>\n'
        '<form data-testid="sort-form" method="get" action="%s/">\n'
        '<select data-testid="sort-select" name="sort">'
        '<option value="created_desc"%s>最新添加</option>'
        '<option value="created_asc"%s>最早添加</option></select>%s'
        '<button type="submit" data-testid="sort-submit">排序</button>\n</form>\n'
    ) % (esc(base), esc(q), hidden_html, esc(base), desc_sel, asc_sel, "".join(sort_hidden))


def render_home(state):
    base = state["base"]
    categories = state["categories"]
    default_id = state["defaultId"]
    q = state.get("q") or ""
    category_id = state.get("categoryId") or ""
    sort = state.get("sort") or "created_desc"
    limit = state.get("limit") or 50
    offset = state.get("offset") or 0
    total = state.get("total") or 0
    bookmarks = state.get("bookmarks") or []
    prefill = state.get("prefill") or {}

    body = [
        '<section class="panel"><h2>保存新链接</h2>\n',
        _save_form(base, categories, state.get("save") or {}, state.get("duplicate"),
                   default_id),
        "</section>\n",
        '<section class="panel"><h2>查找与排序</h2>\n',
        _search_and_sort(base, q, category_id, sort, limit),
        "</section>\n",
        '<section class="panel"><h2>新建归类</h2>\n',
        '<form data-testid="category-form" method="post" action="%s/categories">\n' % esc(base),
        '<input name="name" placeholder="归类名称"><button type="submit"',
        ' data-testid="category-submit">新建归类</button>\n</form>\n',
        "</section>\n",
    ]
    if bookmarks:
        body.append('<section class="library">\n')
        for bookmark in bookmarks:
            body.append(_row(base, bookmark, categories, prefill.get(str(bookmark["id"]))))
        body.append(_pagination(base, q, category_id, sort, limit, offset, total))
        body.append("</section>\n")
    else:
        if q:
            kind = "search"
        elif category_id:
            kind = "category"
        else:
            kind = "library"
        body.append(
            '<section><p data-testid="empty-state" data-empty-kind="%s" class="empty">'
            "这里还没有记录。</p></section>\n" % kind
        )
    nav = _nav(base, categories)
    return _layout(base, nav, state.get("flash"), state.get("formError"), "".join(body),
                   _dialog(base, categories, state.get("dialog")))


def render_category(state):
    base = state["base"]
    categories = state["categories"]
    category = state["category"]
    bookmarks = state.get("bookmarks") or []
    prefill = state.get("prefill") or {}
    body = [
        '<h1 data-testid="category-title">%s</h1>\n' % esc(category["name"]),
        '<form data-testid="category-rename-form" data-category-id="%s" method="post"'
        ' action="%s/categories/%s/rename">\n'
        % (esc(category["id"]), esc(base), esc(category["id"])),
        '<input name="name" value="%s">\n' % esc(state.get("renameValue", category["name"])),
        '<button type="submit" data-testid="category-rename-submit">重命名</button>\n</form>\n',
        '<form data-testid="category-form" method="post" action="%s/categories">\n' % esc(base),
        '<input name="name" placeholder="归类名称"><button type="submit"',
        ' data-testid="category-submit">新建归类</button>\n</form>\n',
    ]
    if bookmarks:
        body.append('<section class="library">\n')
        for bookmark in bookmarks:
            body.append(_row(base, bookmark, categories, prefill.get(str(bookmark["id"]))))
        body.append("</section>\n")
    else:
        body.append(
            '<section><p data-testid="empty-state" data-empty-kind="category" class="empty">'
            "这个归类还没有记录。</p></section>\n"
        )
    nav = _nav(base, categories)
    return _layout(base, nav, state.get("flash"), state.get("formError"), "".join(body), "")


def render_trash(state):
    base = state["base"]
    categories = state["categories"]
    items = state.get("items") or []
    body = [
        '<p><a data-testid="home-link" href="%s/">返回首页</a></p>\n' % esc(base),
        '<form data-testid="trash-clear-form" method="post" action="%s/trash/clear">\n'
        % esc(base),
        '<label><input type="checkbox" data-testid="trash-clear-confirm" name="confirm"'
        ' value="true"> 确认清空回收站</label>\n',
        '<button type="submit" data-testid="trash-clear-submit">清空回收站</button>\n</form>\n',
    ]
    if items:
        for item in items:
            bid = esc(item["id"])
            body.append(
                '<article class="trash-item" data-testid="trash-item" data-bookmark-id="%s">\n'
                % bid
            )
            body.append('<p><span data-testid="trash-title">%s</span></p>\n'
                        % esc(item["title"]))
            body.append('<p class="url"><span data-testid="bookmark-url">%s</span></p>\n'
                        % esc(item["url"]))
            body.append('<p class="meta">原归类：%s%s</p>\n'
                        % (esc(item["categoryName"]),
                           "（已删除）" if item["categoryDeleted"] else ""))
            body.append(
                '<form method="post" action="%s/trash/%s/restore">\n'
                '<select data-testid="restore-target" name="categoryId">%s</select>'
                '<button type="submit" data-testid="restore-submit">恢复</button>\n</form>\n'
                % (esc(base), bid, _category_options(categories, "", include_blank=True))
            )
            body.append(
                '<form data-testid="trash-delete-form" data-bookmark-id="%s" method="post"'
                ' action="%s/trash/%s/delete">\n'
                '<label><input type="checkbox" data-testid="trash-delete-confirm" name="confirm"'
                ' value="true"> 确认永久删除</label>\n'
                '<button type="submit" data-testid="trash-delete-submit">永久删除</button>\n'
                "</form>\n" % (bid, esc(base), bid)
            )
            body.append("</article>\n")
    else:
        body.append(
            '<section><p data-testid="empty-state" data-empty-kind="trash" class="empty">'
            "回收站是空的。</p></section>\n"
        )
    nav = _nav(base, categories, show_delete=False)
    return _layout(base, nav, state.get("flash"), state.get("formError"), "".join(body), "")


def render_error_page(base, status, message):
    body = '<h1>%s</h1><p>%s</p>' % (esc(status), esc(message))
    return _layout(base, "", None, None, body, "")
