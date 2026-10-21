# Home Care Ledger: target architecture

## Scope and decisions to confirm
- Local single-user target: one homeowner, one home, loopback only.
- Python 3.11+ standard library only; SQLite; no third-party packages.
- This is a cognition template, not an application and not the upstream micasa codebase.
- Deliberately excluded: accounts and authentication, notifications, email, vendors, costs, quotes, projects, documents, manuals, photos, payments, LLM, multi-property, imports and exports, and deletion endpoints.
- Decision: exactly one home with fixed id `home`, because the pinned scenario is the user's own home and upstream exposes a single house profile.
- Decision: recurrence is every N calendar days, 1..3650, because the scenario says every N days. Upstream uses interval months; this target is not API-compatible with it.
- Decision: a plan created without an anchor is due on the server local creation date.
- Decision: next due after any completion is `max(old due_on, max(existing last_completed_on, completed_on) + interval_days)`; a backdated completion can never move `due_on` earlier, including a plan seeded only with `first_due_on` or no anchor.
- Decision: no natural-language dates and no timezone-bearing timestamps in domain dates.

## Runtime, data directory, start
- Source file `app.py`; database `$HOMECARE_DATA_DIR/homecare.sqlite3`.
- `HOMECARE_DATA_DIR` defaults to `./data`; the directory is created if absent.
- Start: `python3 app.py --data-dir ./data --host 127.0.0.1 --port 8765`.
- Equivalent environment variables: `HOMECARE_DATA_DIR`, `HOMECARE_HOST`, `HOMECARE_PORT`.
- Bind loopback by default. There is no authentication; do not expose the port.
- On first start create schema and indexes. Schema version 1 is created once; no migration beyond that.
- SQLite connection setup: `PRAGMA foreign_keys=ON`, `journal_mode=WAL`, `busy_timeout=5000`.
- Server: `ThreadingHTTPServer` is acceptable, but every write uses one explicit SQLite transaction.
- JSON is UTF-8. Maximum request body 1,048,576 bytes. POST and PATCH must send `application/json`; otherwise 415.
- Only GET, POST, and PATCH on documented routes. Other methods return 405 `METHOD_NOT_ALLOWED`.
- Health: `GET /health` returns `{status: ok, database: ready}`.

## Entities and exact persisted fields
`homes`
- `id` TEXT primary key, always the literal `home`.
- `name` TEXT NOT NULL, trimmed, 1..80 Unicode code points.
- `address` TEXT NOT NULL default empty string, trimmed, 0..200.
- `created_at`, `updated_at` TEXT UTC ISO-8601 with `Z`, for example `2026-10-21T08:30:00Z`.

`equipment`
- `id` TEXT primary key, `eq_` plus 32 lowercase hex characters.
- `home_id` TEXT NOT NULL REFERENCES `homes(id)` ON DELETE RESTRICT.
- `name` TEXT NOT NULL, trimmed, 1..80.
- `category` TEXT NOT NULL, one of `heating`, `cooling`, `plumbing`, `electrical`, `roof`, `exterior`, `appliance`, `safety`, `other`.
- `location` TEXT NOT NULL default empty, 0..80.
- `make` TEXT NOT NULL default empty, 0..80.
- `model` TEXT NOT NULL default empty, 0..80.
- `installed_on` TEXT NULL, strict calendar date 1900-01-01..2100-12-31.
- `created_at`, `updated_at` UTC ISO-8601.

`plans`
- `id` TEXT primary key, `pl_` plus 32 hex.
- `home_id` TEXT NOT NULL REFERENCES homes.
- `equipment_id` TEXT NULL REFERENCES equipment; when present it must belong to the same `home_id`.
- `name` TEXT NOT NULL, trimmed, 1..80.
- `interval_days` INTEGER NOT NULL, 1..3650 inclusive.
- `last_completed_on` TEXT NULL, strict date; latest known care date.
- `due_on` TEXT NOT NULL, strict date.
- `notes` TEXT NOT NULL default empty, 0..500.
- `created_at`, `updated_at` UTC ISO-8601.
- Index: `(home_id, equipment_id, due_on)`.

`completions`
- `id` TEXT primary key, `cm_` plus 32 hex.
- `plan_id` TEXT NOT NULL REFERENCES plans ON DELETE RESTRICT.
- `completed_on` TEXT NOT NULL, strict date.
- `note` TEXT NOT NULL default empty, trimmed, 0..500.
- `created_at` UTC ISO-8601.
- Index: `(plan_id, completed_on DESC, created_at DESC)`.
- There is no PATCH or DELETE for completions: the record is append-only.

## Date, validation and recurrence rules
- Domain dates are `YYYY-MM-DD` only. Reject timestamps, natural language, invalid ordinal dates, and years outside 1900..2100 with 422 `VALIDATION_ERROR`.
- `server_today` is `datetime.date.today()` in the host local timezone. Domain dates are not converted between zones.
- Creation response timestamps are UTC; domain decisions use `server_today` or an explicit `as_of`.
- Plan anchor when created:
  - `first_due_on` supplied: `due_on = first_due_on`.
  - else `last_completed_on` supplied: `due_on = last_completed_on + interval_days`.
  - else: `due_on = server_today`.
- `last_completed_on` and `first_due_on` are mutually exclusive; supplying both is 422.
- `last_completed_on` may not be after `server_today`; `first_due_on` may not be before 1900-01-01 or after 2100-12-31.
- Completion accepts `completed_on <= server_today`.
- Next due after a completion is always `max(old due_on, max(previous last_completed_on, completed_on) + interval_days)`, using proleptic Gregorian ordinal addition. `last_completed_on` is set to the true latest of its previous value and `completed_on`. This makes backdated entries safe, including a plan seeded only with `first_due_on` or no anchor, and never regresses the schedule.
- If a plan was seeded with `last_completed_on`, that seed is not a completion record; only completion rows appear in history.
- Due status at `as_of`: `overdue` when `due_on < as_of`; `due` when equal; `upcoming` when greater.
- Due query includes tasks with `due_on <= as_of + horizon_days`. Default `horizon_days=0`, so default shows overdue and due only. Horizon range 0..365.
- Sort order: due tasks by `due_on ASC, created_at ASC, id ASC`; plans by `created_at ASC, id ASC`; completions and history by `completed_on DESC, created_at DESC, id DESC`.
- Date edge examples: 2024-02-28 + 1 = 2024-02-29; 2024-02-29 + 1 = 2024-03-01; 2024-12-31 + 30 = 2025-01-30; 2026-01-31 + 31 = 2026-03-03.
- Initial backfill examples: `due_on=2026-03-01` with interval 30 and `completed_on=2025-01-01` keeps `last_completed_on=2025-01-01` and `due_on=2026-03-01`; a plan with no anchor is due on its creation day and a backdated completion keeps that due date.
- Integer fields reject booleans, floats, and numeric strings; JSON boolean true is not an integer. Query integers use decimal digits only.

## HTTP API
Base URL in examples: `http://127.0.0.1:8765`.

Common response rules:
- All API responses are JSON objects with `Content-Type: application/json; charset=utf-8`.
- Error shape: `error` object with `code` string, `message` string, and `field` string or null.
- Codes and statuses:
  - `INVALID_JSON` 400
  - `UNSUPPORTED_MEDIA_TYPE` 415
  - `METHOD_NOT_ALLOWED` 405
  - `NOT_FOUND` 404 for an unknown route
  - `HOME_NOT_FOUND` 404
  - `EQUIPMENT_NOT_FOUND` 404
  - `PLAN_NOT_FOUND` 404
  - `HOME_EXISTS` 409
  - `VALIDATION_ERROR` 422
  - `INTERNAL_ERROR` 500 with no leaked internals
- Unknown request fields are rejected with 422 `VALIDATION_ERROR` and `field` naming the first unknown field.
- Canonical plan object: `id`, `home_id`, `equipment_id`, `name`, `interval_days`, `last_completed_on`, `due_on`, `notes`, `created_at`, `updated_at`, `completion_count`, and `status`. `status` is computed against `server_today`.
- Canonical completion object: `id`, `plan_id`, `completed_on`, `note`, and `created_at`.

### Home
`POST /api/home`
Body: `name` required, `address` optional. Returns 201 `{home: HOME}`. If a home already exists returns 409 `HOME_EXISTS` and writes nothing.
`GET /api/home` returns 200 `{home: HOME}` or 404 `HOME_NOT_FOUND`.
`PATCH /api/home` Body: at least one of `name`, `address`; validates bounds. Returns 200 `{home: HOME}`. Empty patch 422. There is no DELETE.

### Equipment
`POST /api/equipment`
Body: `home_id` required, `name` required, `category` required, optional `location`, `make`, `model`, and `installed_on`.
Returns 201 `{equipment: EQUIPMENT}`. Unknown home 404 `HOME_NOT_FOUND`.
`GET /api/equipment?home_id=home` returns 200 `{equipment: [EQUIPMENT...]}` sorted by `created_at ASC, id ASC`. Missing `home_id` 422; unknown home 404.
`GET /api/equipment/{id}` returns 200 `{equipment: EQUIPMENT}` or 404 `EQUIPMENT_NOT_FOUND`.
No delete.

### Plans
`POST /api/plans`
Body: `home_id` required; `name` required; `interval_days` required; optional `equipment_id`, `last_completed_on`, `first_due_on`, and `notes`.
Returns 201 `{plan: PLAN}`. Unknown home 404. Unknown equipment 404 `EQUIPMENT_NOT_FOUND`; equipment belonging to another home 422 `VALIDATION_ERROR` with field `equipment_id` (defensive, unreachable while only one home exists).
`GET /api/plans?home_id=home&equipment_id=eq_...` returns 200 `{plans: [PLAN...]}`. `equipment_id` is an optional filter. Missing home 422; unknown home 404; unknown equipment 404.
`GET /api/plans/{id}` returns 200 `{plan: PLAN}` or 404 `PLAN_NOT_FOUND`.
No interval or schedule edit endpoint in this version; create a new plan instead. This is a deliberate scope cut.

### Due work
`GET /api/tasks/due?home_id=home&as_of=YYYY-MM-DD&horizon_days=0&equipment_id=eq_...`
- `home_id` required; `as_of` optional, default `server_today`; `horizon_days` optional integer 0..365; `equipment_id` optional.
- Returns 200 `{as_of, horizon_days, tasks: [TASK...]}`.
- TASK fields: `id` (plan id), `home_id`, `home_name`, `equipment_id`, `equipment_name` or null, `name`, `interval_days`, `last_completed_on`, `due_on`, `status`, `days_until_due`, and `notes`.
- `days_until_due = due_on - as_of` in days; negative means overdue.
- Invalid `as_of`, out-of-range horizon, missing home, or unknown home or equipment: 422 or 404 as applicable. No writes.

### Completions and history
`POST /api/plans/{id}/completions`
Body: `completed_on` required, `note` optional default empty.
Returns 201 `{completion: COMPLETION, plan: PLAN}`. Unknown plan 404 `PLAN_NOT_FOUND`. Future date, bad date, or note over 500: 422. The insert and plan update happen in one transaction; on any failure neither changes.
`GET /api/plans/{id}/completions` returns 200 `{completions: [COMPLETION...]}` or 404 `PLAN_NOT_FOUND`.
`GET /api/history?home_id=home&equipment_id=eq_...&limit=100`
- `home_id` required; `equipment_id` optional; `limit` 1..500 default 100.
- Returns 200 `{history: [HISTORY...]}` sorted as defined above.
- HISTORY fields: `id`, `plan_id`, `plan_name`, `home_id`, `home_name`, `equipment_id`, `equipment_name` or null, `completed_on`, `note`, and `created_at`.
- Missing home 422; unknown home or equipment 404. No writes.

## Atomic failure semantics
- Validate method, content type, JSON, field presence, types, bounds, enums, dates, and referential checks before opening a write transaction.
- For `POST /api/home`, insert with fixed id `home`; a concurrent duplicate loses with 409 and leaves exactly one row.
- For `POST /api/equipment` and `POST /api/plans`, one INSERT each; foreign-key failure maps to 404 or 422, not 500.
- For completion, `BEGIN IMMEDIATE`; select plan; compute `latest = max(previous last_completed_on, completed_on)` (or `completed_on` when absent); INSERT completion with the actual `completed_on` and note; UPDATE plan `last_completed_on=latest`, `due_on=max(old due_on, latest + interval_days)`, and `updated_at`; COMMIT. Any error triggers ROLLBACK, leaving zero new completions and an unchanged plan.
- Reads never create rows. A failed request must produce no completion, no plan, no equipment, and no home mutation.
- SQLite constraint errors are mapped to a deterministic 422 or 409; unexpected errors return 500 `INTERNAL_ERROR` without partial commits.

## Basic accessible UI
`GET /` returns one HTML document with `lang=en`, UTF-8, no external assets, and a small inline script that calls the JSON API.
- Sections, in order: Home; Equipment; Care plans; Due work; Completion history.
- Every `input` has an `id` and a visible `label for` that references it; groups use `fieldset` and `legend`.
- Buttons are native `button` elements with descriptive text: Create home, Add equipment, Add plan, Record completion, Refresh.
- Due table has a `caption`, every `th` uses `scope=col`, and text status plus a non-color-only overdue label.
- Success and validation messages render in a container with `role=status` and `aria-live=polite`; errors also include the field name.
- Forms are keyboard operable, visible focus is retained, default browser font sizing is not disabled, and no timeout or auto-submit is used.
- Completing a task opens a small form for `completed_on` and `note`; the API response updates the due list and history without a full page reload.
- History has home and equipment filters populated from the API.
- The UI is a convenience surface; all behavior is available through the documented API.
- These structural checks are a smoke test, not a certification of full accessibility conformance.

## Probe contract
`probe.py` is a standard-library HTTP client supplied in `acceptance_files`. It accepts `--base-url` and exactly one `--case A01..A05`, creates only disposable records with a unique suffix, never deletes, and asserts exact statuses, shapes, dates, ordering, exact due ID sets and counts, zero-write outcomes, and HTML structure through `html.parser.HTMLParser`. It does not start the server and makes no claim about an upstream run.