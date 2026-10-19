"""Server-side HTML rendering for the private P0 bookmark library.

The HTTP layer in ``app/server.py`` owns status codes, headers and routing; this
module only turns storage row dicts into complete HTML documents. There is no
template engine and no JavaScript: every page is a plain UTF-8 string built from
escaped fragments, so the interface works offline and with scripting disabled.

Public API (see ``__all__``):

``escape(value)``
    Return ``value`` as HTML-safe text; ``None`` becomes ``""``. Every dynamic
    value -- collection names, bookmark titles, URLs, the search keyword and the
    error message -- passes through this helper, so untrusted input can never
    change the structure of a page.

``render_index(collections, bookmarks, selected_collection_id, query,
form_state=None)``
    Render the library page returned for ``GET /`` (HTTP 200). ``collections``
    is the ordered list of collection row dicts, ``bookmarks`` the list of
    bookmark row dicts to display, ``selected_collection_id`` the collection
    currently browsed (a numeric id, the ``"inbox"``/``"default"`` alias, or
    ``None``/``""`` for the whole library) and ``query`` the current keyword (or
    ``None``). ``form_state`` may pre-fill the capture form after a redirect.

``render_error(status, message, form_state=None)``
    Render the frozen ``400``/``404`` pages. ``message`` is shown to the user;
    ``form_state`` may echo a rejected submission so the input can be corrected
    and resubmitted. Error pages never contain library content, so a ``404`` for
    an undefined public/share route cannot leak stored data.

``form_state`` contract
    A plain mapping (or ``None``) that may carry any of the submitted values
    ``"url"``, ``"title"``, ``"collection_id"`` and ``"name"``. ``render_index``
    uses them to pre-fill the capture form, and ``render_error`` uses them to
    re-render the rejected form. Storage row dicts are only read, never mutated.

The stable hooks the frozen acceptance suite relies on are always emitted:

* ``<li class="collection" data-collection-id data-default>`` in the sidebar,
* ``<li class="bookmark" data-bookmark-id data-collection-id>`` in the list,
* ``<a class="bookmark-title" href="<saved url>">`` on every record,
* the capture form ``POST /bookmarks`` (``url`` required, ``title``,
  ``collection_id``), the new-collection form ``POST /collections`` (``name``),
  the search form ``GET /`` (``q``) and the per-record move form
  ``POST /bookmarks/<id>/move`` (``collection_id``).
"""

import html
import urllib.parse

__all__ = ["render_index", "render_error", "escape"]

#: Inline stylesheet shared by every page. No script or external resource is
#: referenced, so the interface works with JavaScript disabled and offline.
_STYLES = """\
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif; line-height: 1.5; }
a { color: #0b5cad; }
header.topbar { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; padding: 0.75rem 1rem; border-bottom: 1px solid #d9d9d9; }
header.topbar h1 { font-size: 1.15rem; margin: 0; }
header.topbar h1 a { text-decoration: none; }
form.search { display: flex; align-items: center; gap: 0.5rem; margin-left: auto; }
.layout { display: flex; align-items: flex-start; gap: 1.5rem; padding: 1rem; }
nav.sidebar { flex: 0 0 16rem; }
nav.sidebar ul.collections { list-style: none; margin: 0 0 1rem; padding: 0; }
nav.sidebar li.collection { padding: 0.2rem 0.4rem; border-radius: 4px; }
nav.sidebar li.collection.active { background: #e8f0fb; font-weight: 600; }
nav.sidebar li.collection a { text-decoration: none; }
nav.sidebar form.new-collection { display: flex; flex-direction: column; gap: 0.3rem; }
main.library { flex: 1 1 auto; min-width: 0; }
section.capture form { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 0.75rem; margin-bottom: 1rem; }
section.capture label { display: flex; flex-direction: column; font-size: 0.85rem; gap: 0.2rem; }
section.capture input, section.capture select { padding: 0.35rem; }
ul.bookmarks { list-style: none; margin: 0; padding: 0; }
li.bookmark { display: flex; flex-wrap: wrap; align-items: center; gap: 0.6rem; padding: 0.6rem 0.4rem; border-bottom: 1px solid #ececec; }
a.bookmark-title { font-weight: 600; margin-right: auto; word-break: break-all; }
a.bookmark-open { white-space: nowrap; }
span.bookmark-note { color: #666; }
form.move { display: flex; align-items: center; gap: 0.4rem; }
label.visually-hidden { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
p.empty { color: #666; }
main.error { max-width: 40rem; margin: 3rem auto; padding: 0 1rem; }
main.error h1 { margin-bottom: 0.25rem; }
main.error p.status { color: #666; margin-top: 0; }
main.error p.message { font-weight: 600; }
section.recovery form { display: flex; flex-direction: column; gap: 0.4rem; max-width: 28rem; }
"""


def escape(value):
    """Return ``value`` as HTML-safe text, with ``None`` rendered as ``""``."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def _state_has(state, key):
    """Return ``True`` when ``state`` is a mapping that contains ``key``."""
    if not state:
        return False
    try:
        return key in state
    except TypeError:
        return False


def _field(state, key, default=""):
    """Return ``state[key]`` as text, tolerating ``None`` and missing keys."""
    if not state:
        return default
    try:
        value = state.get(key, default)
    except AttributeError:
        return default
    return default if value is None else str(value)


def _row_value(row, key, default=None):
    """Read ``key`` from a storage row dict (or object), or ``default``."""
    if row is None:
        return default
    if isinstance(row, dict) or hasattr(row, "get"):
        value = row.get(key, default)
    else:
        value = getattr(row, key, default)
    return default if value is None else value


def _is_truthy(value):
    """Return ``True`` for SQLite-style truthy flags (``1``/``"1"``/``"true"``)."""
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes")
    return bool(value)


def _is_inbox_value(value):
    """Return ``True`` when ``value`` names the default inbox (or is empty)."""
    if value is None:
        return True
    return str(value).strip().lower() in ("", "inbox", "default")


def _collection_url(collection_id):
    """Return the read-only URL that browses a single collection."""
    token = "" if collection_id is None else str(collection_id)
    return "/?collection=" + urllib.parse.quote(token, safe="")


def _resolve_active_id(collections, selected_collection_id):
    """Resolve the browsed collection to an id string, or ``None`` for all."""
    if selected_collection_id is None:
        return None
    token = str(selected_collection_id).strip()
    if token == "":
        return None
    if token.lower() in ("inbox", "default"):
        for collection in collections or []:
            if _is_truthy(_row_value(collection, "is_default", 0)):
                return str(_row_value(collection, "id"))
        return None
    return token


def _collection_options(collections, selected_id, skip_default=False):
    """Render the ``<option>`` elements for a collection ``<select>``."""
    if _is_inbox_value(selected_id):
        selected = None
    else:
        selected = str(selected_id).strip()
    options = []
    for collection in collections or []:
        if skip_default and _is_truthy(_row_value(collection, "is_default", 0)):
            continue
        collection_id = _row_value(collection, "id")
        marker = ""
        if selected is not None and str(collection_id) == selected:
            marker = " selected"
        options.append(
            '<option value="{0}"{1}>{2}</option>'.format(
                escape(collection_id), marker,
                escape(_row_value(collection, "name", "")),
            )
        )
    return "".join(options)


def _collection_item(collection, active_id):
    """Render one sidebar ``<li class="collection">`` row."""
    collection_id = _row_value(collection, "id")
    classes = "collection"
    if active_id is not None and str(collection_id) == active_id:
        classes = "collection active"
    return (
        '<li class="{0}" data-collection-id="{1}" data-default="{2}">'
        '<a href="{3}">{4}</a>'
        "</li>"
    ).format(
        classes,
        escape(collection_id),
        "1" if _is_truthy(_row_value(collection, "is_default", 0)) else "0",
        escape(_collection_url(collection_id)),
        escape(_row_value(collection, "name", "")),
    )


def _bookmark_item(bookmark, collections):
    """Render one record: title link, open link, optional note and move form."""
    bookmark_id = _row_value(bookmark, "id")
    url = _row_value(bookmark, "url", "")
    note = _row_value(bookmark, "note", "")
    title = str(_row_value(bookmark, "title", "")).strip()
    display_title = title or str(url)
    note_html = ""
    if str(note).strip():
        note_html = '<span class="bookmark-note">{0}</span>'.format(escape(note))
    options = _collection_options(collections, _row_value(bookmark, "collection_id"))
    return (
        '<li class="bookmark" data-bookmark-id="{0}" data-collection-id="{1}">'
        '<a class="bookmark-title" href="{2}">{3}</a>'
        '<a class="bookmark-open" href="/go/{0}">打开原页</a>'
        "{4}"
        '<form class="move" method="post" action="/bookmarks/{0}/move">'
        '<label class="visually-hidden" for="move-{0}">移动到归类</label>'
        '<select id="move-{0}" name="collection_id">{5}</select>'
        '<button type="submit">移动</button>'
        "</form>"
        "</li>"
    ).format(
        escape(bookmark_id),
        escape(_row_value(bookmark, "collection_id")),
        escape(url),
        escape(display_title),
        note_html,
        options,
    )


def _result_heading(collections, query_text, active_id):
    """Return the heading shown above the record list."""
    if query_text:
        return "检索：" + query_text
    if active_id is not None:
        for collection in collections or []:
            if str(_row_value(collection, "id")) == active_id:
                return "归类：" + str(_row_value(collection, "name", ""))
        return "归类"
    return "全部收藏"


def _empty_message(query_text):
    """Return the message shown when the record list is empty."""
    if query_text:
        return "没有匹配的记录；请更换关键字，或清空检索。"
    return "这里还没有记录；可用上方表单保存一个链接。"


def _page_head(title):
    """Return the shared ``<head>`` of a document."""
    return "".join([
        "<!DOCTYPE html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>",
        escape(title),
        "</title>",
        "<style>",
        _STYLES,
        "</style>",
        "</head>",
    ])


def _recovery_form(state):
    """Render the rejected form again so the user can correct and resubmit."""
    if not state:
        return ""
    if _state_has(state, "name") and not _state_has(state, "url"):
        return (
            '<form method="post" action="/collections">'
            '<label for="recovery-name">归类名称</label>'
            '<input id="recovery-name" type="text" name="name" required value="{0}">'
            '<button type="submit">重试新建</button>'
            "</form>"
        ).format(escape(_field(state, "name")))
    if (
        _state_has(state, "url")
        or _state_has(state, "title")
        or _state_has(state, "collection_id")
    ):
        hidden = ""
        if _state_has(state, "collection_id"):
            hidden = (
                '<input type="hidden" name="collection_id" value="{0}">'.format(
                    escape(_field(state, "collection_id"))
                )
            )
        return (
            '<form method="post" action="/bookmarks">'
            '<label for="recovery-url">网址</label>'
            '<input id="recovery-url" type="url" name="url" required value="{0}">'
            '<label for="recovery-title">标题</label>'
            '<input id="recovery-title" type="text" name="title" value="{1}">'
            "{2}"
            '<button type="submit">重试保存</button>'
            "</form>"
        ).format(
            escape(_field(state, "url")),
            escape(_field(state, "title")),
            hidden,
        )
    return ""


def render_index(collections, bookmarks, selected_collection_id, query, form_state=None):
    """Return the library page (HTTP 200) as one HTML document."""
    collections = list(collections or [])
    bookmarks = list(bookmarks or [])
    state = form_state or {}

    active_id = _resolve_active_id(collections, selected_collection_id)
    query_text = "" if query is None else str(query).strip()

    sidebar_items = "".join(
        _collection_item(collection, active_id) for collection in collections
    )

    if _state_has(state, "collection_id"):
        capture_selected = _field(state, "collection_id")
    else:
        capture_selected = active_id or ""
    inbox_marker = " selected" if _is_inbox_value(capture_selected) else ""
    capture_options = _collection_options(
        collections, capture_selected, skip_default=True
    )

    bookmark_items = "".join(
        _bookmark_item(bookmark, collections) for bookmark in bookmarks
    )
    if bookmark_items:
        results_body = '<ul class="bookmarks">' + bookmark_items + "</ul>"
    else:
        results_body = (
            '<ul class="bookmarks"></ul>'
            '<p class="empty">{0}</p>'.format(escape(_empty_message(query_text)))
        )

    parts = [
        _page_head("私人收藏夹"),
        "<body>",
        '<header class="topbar">',
        '<h1><a href="/">私人收藏夹</a></h1>',
        '<form class="search" method="get" action="/">',
        '<label for="search-q">检索</label>',
        '<input id="search-q" type="search" name="q" value="{0}" placeholder="标题、网址或备注关键字">'.format(escape(query_text)),
        '<button type="submit">搜索</button>',
        "</form>",
        "</header>",
        '<div class="layout">',
        '<nav class="sidebar" aria-label="归类">',
        "<h2>归类</h2>",
        '<p><a class="all-link" href="/">全部收藏</a></p>',
        '<ul class="collections">',
        sidebar_items,
        "</ul>",
        '<form class="new-collection" method="post" action="/collections">',
        '<label for="new-collection-name">新建归类</label>',
        '<input id="new-collection-name" type="text" name="name" value="{0}" required>'.format(escape(_field(state, "name"))),
        '<button type="submit">新建</button>',
        "</form>",
        "</nav>",
        '<main class="library">',
        '<section class="capture">',
        "<h2>保存链接</h2>",
        '<form method="post" action="/bookmarks">',
        '<label for="capture-url">网址</label>',
        '<input id="capture-url" type="url" name="url" value="{0}" required placeholder="https://...">'.format(escape(_field(state, "url"))),
        '<label for="capture-title">标题</label>',
        '<input id="capture-title" type="text" name="title" value="{0}" placeholder="留空则显示网址">'.format(escape(_field(state, "title"))),
        '<label for="capture-collection">归类</label>',
        '<select id="capture-collection" name="collection_id">',
        '<option value=""{0}>未整理（默认收件箱）</option>'.format(inbox_marker),
        capture_options,
        "</select>",
        '<button type="submit">保存</button>',
        "</form>",
        "</section>",
        '<section class="results">',
        "<h2>{0}</h2>".format(escape(_result_heading(collections, query_text, active_id))),
        results_body,
        "</section>",
        "</main>",
        "</div>",
        "</body>",
        "</html>",
    ]
    return "".join(parts)


def render_error(status, message, form_state=None):
    """Return the frozen ``400``/``404`` error page as one HTML document."""
    state = form_state or {}
    parts = [
        _page_head("出错了"),
        "<body>",
        '<main class="error">',
        "<h1>出错了</h1>",
        '<p class="status">HTTP {0}</p>'.format(escape(status)),
        '<p class="message">{0}</p>'.format(escape(message)),
    ]
    recovery = _recovery_form(state)
    if recovery:
        parts.extend([
            '<section class="recovery">',
            "<h2>修正后重试</h2>",
            recovery,
            "</section>",
        ])
    parts.extend([
        '<p class="back"><a href="/">返回收藏夹</a></p>',
        "</main>",
        "</body>",
        "</html>",
    ])
    return "".join(parts)
