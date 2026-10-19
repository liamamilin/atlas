"""服务端渲染：中文 HTML 界面（Python 3 标准库，无第三方依赖、无外部资源）。"""

import html

# 备注上限：明确的较大上限，超限显式报错且不落库，绝不静默截断。
NOTE_MAX_LEN = 2000
NOTE_FIELD_LABEL = "备注（最多 %d 字）" % NOTE_MAX_LEN

UNSORTED_LABEL = "未分类"
UNSORTED_OPTION_LABEL = "未分类（以后看看）"

EMPTY_LIBRARY_TEXT = "你的收藏夹还是空的。把想记住的网页链接填进上面的表单并保存，记录就会出现在这里。"
NO_SEARCH_MATCH_TEXT = "没有找到匹配的记录。请更换关键词，或切换到其他分类后再试。"


def _e(value):
    return html.escape("" if value is None else str(value), quote=True)


def _friendly_time(value):
    text = str(value or "")
    if "T" in text:
        date, _, rest = text.partition("T")
        return "%s %s UTC" % (date, rest[:5])
    return text


def _category_options(categories, selected):
    selected = "" if selected is None else str(selected)
    parts = ['<option value="">%s</option>' % _e(UNSORTED_OPTION_LABEL)]
    for cat in categories:
        mark = " selected" if str(cat["id"]) == selected else ""
        parts.append(
            '<option value="%d"%s>%s</option>' % (cat["id"], mark, _e(cat["name"]))
        )
    return "".join(parts)


def _category_nav(categories, active):
    active = active or ""
    items = [
        '<li><a class="category-item category-all" href="/">全部</a></li>',
        '<li><a class="category-item%s" data-category-id="unsorted" href="/?category=unsorted">%s</a></li>'
        % (" is-active" if active == "unsorted" else "", _e(UNSORTED_LABEL)),
    ]
    for cat in categories:
        cid = str(cat["id"])
        mark = " is-active" if active == cid else ""
        items.append(
            '<li><a class="category-item%s" data-category-id="%s" href="/?category=%s">%s</a></li>'
            % (mark, cid, cid, _e(cat["name"]))
        )
    return "".join(items)


def _record_card(bookmark, categories):
    url = bookmark["url"]
    title = bookmark["title"] or url
    cat_label = bookmark["category_name"] or UNSORTED_LABEL
    note_html = ""
    if bookmark["note"]:
        note_html = '<p class="record-note">%s</p>' % _e(bookmark["note"])
    move_options = _category_options(categories, bookmark["category_id"])
    return (
        '<li class="record-card" data-testid="record-card" data-url="%s">'
        '<div class="record-head">'
        '<a class="record-open" data-testid="record-open" href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
        '<span class="record-category" data-testid="record-category">%s</span>'
        "</div>"
        "%s"
        '<p class="record-url">%s</p>'
        '<p class="record-time">保存于 %s</p>'
        '<form class="move-form" method="post" action="/move">'
        '<input type="hidden" name="bookmark_id" value="%d">'
        '<label class="move-label" for="move-select-%d">移动到分类</label>'
        '<select id="move-select-%d" name="category_id">%s</select>'
        '<button type="submit" class="move-submit" data-testid="record-move-submit" name="move">移动</button>'
        "</form>"
        "</li>"
    ) % (
        _e(url),
        _e(url),
        _e(title),
        _e(cat_label),
        note_html,
        _e(url),
        _e(_friendly_time(bookmark["created_at"])),
        bookmark["id"],
        bookmark["id"],
        bookmark["id"],
        move_options,
    )


def render_page(ctx):
    categories = ctx["categories"]
    bookmarks = ctx["bookmarks"]
    form = ctx.get("form") or {}
    error = ctx.get("error")
    duplicate = ctx.get("duplicate")
    q = ctx.get("q") or ""
    active = ctx.get("active_category") or ""
    total = int(ctx.get("total_count") or 0)
    nonce = ctx.get("nonce") or ""
    confirm_nonce = ctx.get("confirm_nonce") or ""

    form_url = _e(form.get("url", ""))
    form_title = _e(form.get("title", ""))
    form_note = _e(form.get("note", ""))
    form_new = _e(form.get("new_category", ""))
    form_cat = _e(form.get("category_id", ""))

    error_html = ""
    if error:
        error_html = (
            '<p class="form-error" role="alert" data-testid="form-error">%s</p>' % _e(error)
        )

    duplicate_html = ""
    if duplicate:
        message = (
            "该链接可能已存在（%s）。如仍要保存为另一条记录，请点击“仍然保存”。"
            % _e(duplicate.get("title") or duplicate.get("url") or "")
        )
        duplicate_html = (
            '<div class="duplicate-box">'
            '<p class="form-error" role="alert" data-testid="form-error">%s</p>'
            '<form class="duplicate-form" method="post" action="/save">'
            '<input type="hidden" name="nonce" value="%s">'
            '<input type="hidden" name="force" value="1">'
            '<input type="hidden" name="url" value="%s">'
            '<input type="hidden" name="title" value="%s">'
            '<input type="hidden" name="note" value="%s">'
            '<input type="hidden" name="new_category" value="%s">'
            '<input type="hidden" name="category_id" value="%s">'
            '<button type="submit" class="duplicate-confirm" data-testid="duplicate-confirm" name="still-save">仍然保存</button>'
            "</form>"
            "</div>"
        ) % (
            message,
            _e(confirm_nonce),
            form_url,
            form_title,
            form_note,
            form_new,
            form_cat,
        )

    markers = ""
    if total == 0:
        markers += (
            '<div class="state-empty" id="empty-library" data-testid="empty-library">%s</div>'
            % _e(EMPTY_LIBRARY_TEXT)
        )
    if q and not bookmarks:
        markers += (
            '<div class="state-no-match" id="no-search-match" data-testid="no-search-match">%s</div>'
            % _e(NO_SEARCH_MATCH_TEXT)
        )

    cards = "".join(_record_card(item, categories) for item in bookmarks)
    list_html = (
        '<ol class="record-list" id="record-list" data-testid="record-list">%s</ol>' % cards
    )

    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>生活待购与灵感收藏夹</title>
<link rel="stylesheet" href="/static/app.css">
</head>
<body>
<header class="app-header">
  <h1>生活待购与灵感收藏夹</h1>
  <p class="app-sub">把偶然看到、暂时不处理的网页链接先存起来；需要时再按分类或关键词找回来，并回到原页面。</p>
</header>
<div class="layout">
  <aside class="sidebar">
    <h2 class="sidebar-title">分类</h2>
    <ul class="category-list" id="category-list" data-testid="category-list">%s</ul>
    <p class="sidebar-note">想新建分类？在右侧保存表单的“新建分类”里填写名称，保存记录时会一并创建。</p>
  </aside>
  <main class="content">
    <section class="panel save-panel">
      <h2>保存链接</h2>
      <form class="save-form" method="post" action="/save">
        <input type="hidden" name="nonce" value="%s">
        <div class="field">
          <label for="save-url">链接 URL（必填）</label>
          <input id="save-url" data-testid="save-url" name="url" type="text" autocomplete="off" spellcheck="false" placeholder="https://example.com/page" value="%s">
        </div>
        <div class="field">
          <label for="save-title">标题（可选）</label>
          <input id="save-title" data-testid="save-title" name="title" type="text" value="%s">
        </div>
        <div class="field">
          <label for="save-note">%s</label>
          <textarea id="save-note" data-testid="save-note" name="note" rows="3">%s</textarea>
        </div>
        <div class="field-grid">
          <div class="field">
            <label for="save-category-select">分类（可选，不选则进入未分类）</label>
            <select id="save-category-select" data-testid="save-category-select" name="category_id">%s</select>
          </div>
          <div class="field">
            <label for="save-category-new">新建分类（可选）</label>
            <input id="save-category-new" data-testid="save-category-new" name="new_category" type="text" value="%s">
          </div>
        </div>
        <button type="submit" class="primary" id="save-submit" data-testid="save-submit" name="save">保存到收藏夹</button>
      </form>
      %s
      %s
    </section>

    <section class="panel search-panel">
      <form class="search-form" method="get" action="/">
        <label for="search-input">搜索关键词</label>
        <input id="search-input" data-testid="search-input" type="search" name="q" value="%s" placeholder="标题 / 链接 / 备注 / 分类名">
        <button type="submit" id="search-submit" data-testid="search-submit">搜索</button>
      </form>
    </section>

    %s
    %s
  </main>
</div>
</body>
</html>
""" % (
        _category_nav(categories, active),
        _e(nonce),
        form_url,
        form_title,
        NOTE_FIELD_LABEL,
        form_note,
        _category_options(categories, form.get("category_id", "")),
        form_new,
        error_html,
        duplicate_html,
        _e(q),
        markers,
        list_html,
    )
