# 生活待购与灵感收藏夹 — Bookmark Manager (P0)

A private, single-user, offline bookmark library. Save external web links, classify them into simple collections (with a default inbox for unsorted links), browse by collection, search by keyword, and open a record back to its original page. Data persists across sessions in a local SQLite file.

## Frozen offline contract

- **Python 3 standard library only.** The server uses `http.server.ThreadingHTTPServer` + `http.server.BaseHTTPRequestHandler`, `sqlite3`, and server-rendered HTML. No third-party dependencies (there is no `requirements.txt` on purpose), no JavaScript, no build step, no bundler, no package manager.
- **No outbound network access at runtime.** The only request that leaves the app is the user-initiated `GET /go/<id>` `302` redirect to a saved URL; the app never fetches, proxies, or archives the target page and never follows that redirect itself.
- **No authentication.** P0 is a private, single-user local library: no login, no accounts, no permissions, and **no public/share route**. `/share`, `/public`, `/share/<id>`, `/public/<id>` and every other undefined route return `404` without leaking stored data.
- **Source stays read-only.** Only the directory passed to `--data-dir` is written to; the application never writes beside its own source.
- **Pointers, not copies.** Records anchor to URLs; web content stays on the Web.

## Requirements

- Python 3 with its standard library. There is no install step and nothing to build.

## Launch locally

```bash
python3 -m app --host 127.0.0.1 --port 8000 --data-dir ./state
```

Then open `http://127.0.0.1:8000/` in a browser.

Arguments:

- `--host` — interface to bind. **Defaults to `127.0.0.1` (loopback)** for normal local use.
- `--port` — TCP port. **Defaults to `8000`**; must be an integer in `1024`–`65535`.
- `--data-dir` — directory holding all mutable state. **Defaults to `./state`**; created if absent.

### Managed container delivery

`delivery.json` starts the app inside the managed container with a literal argv:

```json
["python3", "-m", "app", "--host", "0.0.0.0", "--port", "8000", "--data-dir", "/state/data"]
```

Binding `0.0.0.0` is used **only inside the managed container**, where the container port `8000` is published on the host as `127.0.0.1` only. The app itself still defaults to loopback when `--host` is omitted, so local runs stay private. Use `--host 0.0.0.0` only when an outer layer restricts access.

## Data and persistence

- All mutable state lives in one SQLite database file, **`library.sqlite3`**, directly under the `--data-dir`.
  - Local default: `./state/library.sqlite3`.
  - Managed delivery: `/state/data/library.sqlite3`, beneath the persistent `/state` mount — that mount is the volume to back up.
- Data survives process restart; every write commits a SQLite transaction.
- The whole `--data-dir` can be copied for backup and restore. The read-only source tree is never the data store.
- P0 schema:
  - `collections(id INTEGER PK, name TEXT NOT NULL UNIQUE, is_default INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)` — a default inbox named `未整理` (`is_default = 1`) is created on first start and cannot be deleted.
  - `bookmarks(id INTEGER PK, url TEXT NOT NULL, title TEXT NOT NULL DEFAULT '', note TEXT NOT NULL DEFAULT '', collection_id INTEGER NOT NULL REFERENCES collections(id), created_at TEXT NOT NULL, updated_at TEXT NOT NULL)`.
- Timestamps are stored as UTC ISO-8601 text. Each bookmark has exactly one owning collection (single-ownership; no tags in P0).

## HTTP routes, forms and error contract (P0)

All pages are server-rendered HTML. GET is read-only; every POST mutates state and then redirects with `303` (POST/Redirect/GET) so a refresh never re-submits.

| Method | Path | Form / query fields | Success | Error |
| --- | --- | --- | --- | --- |
| GET | `/` (query `?collection=<id>` or `?collection=inbox`, and/or `?q=<keyword>`) | `collection`, `q` | `200` library page with the collection sidebar and bookmark list | unknown `collection` id → `404` |
| POST | `/bookmarks` | `url` (**required**), `title` (optional), `collection_id` (optional) | `303` to `/?collection=<chosen id>` or `/?collection=inbox` | empty, malformed, host-less, or non-`http(s)` URL → `400` error page echoing the submitted input |
| POST | `/collections` | `name` (**required**) | `303` to `/` | empty or duplicate name → `400` |
| POST | `/bookmarks/<id>/move` | `collection_id` (**required**) | `303` to `/?collection=<target id>` | unknown bookmark id or unknown collection → `404` |
| GET | `/go/<id>` | none | `302` with `Location: <saved URL>` | unknown id → `404` |
| GET | `/?q=<keyword>` | `q` | `200` result list (possibly empty) | — |
| any | other paths, including `/share`, `/share/<id>`, `/public`, `/public/<id>` | — | — | `404`, no library content leaked |

`404` uses one uniform shape for all unknown entities. A `400` page keeps the submitted input so the user can correct it.

### Stable UI contract the server renders

- Capture form: `<form method="post" action="/bookmarks">` with fields `url` (required), `title`, and an optional `collection_id` select.
- New-collection form: `<form method="post" action="/collections">` with field `name`.
- Move form (per record): `<form method="post" action="/bookmarks/<id>/move">` with field `collection_id`.
- Search form: `<form method="get" action="/">` with field `q`.
- Collection sidebar item: `<li class="collection" data-collection-id="<id>" data-default="0">` (the inbox uses `data-default="1"`).
- Bookmark list item: `<li class="bookmark" data-bookmark-id="<id>" data-collection-id="<id>">` containing `<a class="bookmark-title" href="<saved URL>">`.
- Open-original entry point: `GET /go/<id>` (`302`).

The `<id>` values are emitted in the `data-bookmark-id` and `data-collection-id` attributes so every P0 flow is usable and verifiable without JavaScript.

## Search semantics (P0)

- Case-insensitive `LIKE` match over `title`, `url`, and `note` (not page bodies).
- Scoped to the selected collection when `collection` is supplied; otherwise across the whole library.
- No match returns `200` with an empty list, never a false hit.

## Validation and safety

- Only absolute `http://` / `https://` URLs are accepted; empty, malformed, host-less, and non-`http(s)` schemes (`javascript:`, `data:`, `ftp:`, …) are rejected with `400`.
- A blank `title` falls back to displaying the URL.
- All dynamic text is HTML-escaped on output.
- Server-side fetching of target pages is off, so there is no SSRF surface.

## Source layout

```
README.md            this file
app/__init__.py      package marker (`python -m app` target)
app/__main__.py      module entry point
app/config.py        --host / --port / --data-dir parsing
app/storage.py       SQLite schema and data access
app/validation.py    URL, title and collection-name validation
app/views.py         server-rendered HTML
delivery.json        offline runtime descriptor (managed-container start argv)
```

## Out of scope (P0)

No login or auth, no sharing or public collections, no multi-user or sync, no page archiving or metadata fetching, no broken-link checking, no full-text search, no tags or nested collections, and no import/export. These are later-phase decisions; P0 delivers save → classify → find → open on a persistent local library.