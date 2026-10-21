# Personal Project Board - local single-user kanban board

## What this is
A dependency-free (Python 3 standard library only) local web app for one person: named
boards, user-named ordered columns, cards with a title and a short description, and card
movement between columns and inside a column. A card's column IS its status - there is no
separate status field. Everything is stored in one SQLite file inside a data directory you
choose, so boards, columns, card order and card positions survive a restart.

## Requirements
- Python 3.9 or newer, standard library only (http.server, sqlite3, json, urllib.parse)
- no third-party packages, no network access

## Layout
    app.py            entry point (argument parsing, server wiring)
    personal_board/   db.py, service.py, api.py, web.py, server.py
    probe.py          acceptance probe (stdlib only)
    README.md         this file
    data/             default data directory, created on first run

## Start the app
    python3 app.py --host 127.0.0.1 --port 8765 --data-dir ./data
    # the default data directory can also be set with PERSONAL_KANBAN_DATA_DIR=./data

Then open http://127.0.0.1:8765/ in a browser. The JSON API lives under
http://127.0.0.1:8765/api/ (health check: GET /api/health).

Stop the process with Ctrl-C. Start it again with the same --data-dir: the boards, the
column order, the card order and the per-column counts are read back unchanged from
<data-dir>/kanban.sqlite3.

## Run the acceptance probe
Start the app first, then:
    python3 probe.py --base-url http://127.0.0.1:8765 --case A01
    python3 probe.py --base-url http://127.0.0.1:8765 --case all

Cases (one per feature):
    A01  boards: create, list, read, rename, delete + 7 rejected writes
    A02  columns: seed, add, rename, reorder, delete guards
    A03  cards: create, read, edit + 12 rejected writes
    A04  movement: cross-column move, in-column reorder, rejected moves
    A05  read model: exact counts and sets, stable second read, date edges

Exit code 0 means every selected case passed, 1 means at least one case failed. Each case
creates its own disposable board and deletes only the records it created; no pre-existing
data is ever deleted, so run the probe against a scratch data directory.

## Manual restart check (operator step, not executed by the probe)
1. Start the app with a scratch data directory, create one board with three columns and
   two cards, and note GET /api/boards/{id}.
2. Stop the process (Ctrl-C) and start it again with the same --data-dir.
3. GET /api/boards and GET /api/boards/{id}: the board, the column order, the card order
   and the per-column card_count must be identical to step 1.

The probe cannot stop or start the server, so it does not and does not claim to verify
this step.

## Verification status
Runtime verification of this blueprint: not_run. No server was started, no request was
issued and no probe case was executed while this document was written; the acceptance
criteria describe what must hold, not what was observed. The upstream project (Kanboard)
was read as a pinned design reference only: it was neither installed nor run, and no
upstream source was copied into the target.

## Out of scope for P0
Accounts and login, roles and permissions, multi-user collaboration, a separate status
field, WIP limits, swimlanes, due/start dates and recurrence, notifications, time
tracking and reports, automation, templates, search and filtering, archive, secondary
views, external integrations.
