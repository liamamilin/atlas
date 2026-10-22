# Aurora Resource Calendar acceptance probe

Portable standard-library HTTP verifier for the web target. It does not install, start, or modify the application.

## Target expected

- Node.js 22 TypeScript/Fastify service with SQLite as the authoritative schedule.
- Room id `aurora`, name `Aurora Conference Room`, timezone `Asia/Shanghai`, capacity 12, location `HQ 3F`.
- Acceptance week Monday 2026-10-19 through Sunday 2026-10-25; Thursday is 2026-10-22; room offset +08:00.
- JSON endpoints `GET /api/rooms/aurora/week`, `GET /api/rooms/aurora/reservations`, `POST /api/rooms/aurora/reservations`, and `DELETE /api/rooms/aurora/reservations/:id`, as specified in the architecture.
- `X-Actor` identifies the caller; `X-Role: admin` is optional; a non-owner cannot cancel another staff member claim.
- The week page `GET /rooms/aurora/week?weekStart=2026-10-19` is the manual UI surface.

## Isolated setup

1. `npm ci`
2. `export DATABASE_PATH=/tmp/atlas-aurora-$RANDOM.sqlite`
3. `npm run build`
4. `npm run migrate`
5. `npm run seed`
6. `DATABASE_PATH=$DATABASE_PATH PORT=8080 npm start`
7. `ATLAS_BASE_URL=http://127.0.0.1:8080 python3 probe.py`

The database must be disposable and dedicated to this run. Do not point `DATABASE_PATH` at a shared or production file. The seed must be non-destructive; it only ensures the `aurora` room exists and never truncates reservations.

Optional overrides: `ATLAS_ROOM_ID`, `ATLAS_WEEK_START` (must be a Monday), `ATLAS_UTC_OFFSET` (for example `+08:00`). The defaults are the fixed scenario above.

## Safety and exit codes

- Preflight reads the week and checks Thursday 09:00-10:00, 14:00-16:00, 14:30-15:30, and 16:00-17:00 before any write.
- Unreachable view, missing busy array, or any occupied baseline window: `status: not_run`, exit 2, and no POST or DELETE. The 09:00 setup claim is never written first.
- Case failure: `status: fail`, exit 1, with `failures` naming the case and assertion.
- Full pass: `status: pass`, exit 0, with per-case check counts.
- Writes use generated `probe-*` actor ids. Best-effort cleanup soft-cancels only reservations the probe created; cancelled audit rows remain. The probe never hard-deletes and never cancels a row it did not create.
- A pass means the JSON contract and journey passed on this database run. It is not a security, UI, or production certification.

## Cases

- A01: week view identifies Aurora and seven days, rejects a non-Monday weekStart with 400 `INVALID_WEEK_START`, accepts a 09:00-10:00 setup claim, shows it once to its owner with purpose, and hides the purpose from another staff member while 14:00-16:00 stays free.
- A02: a zero-length 14:00-14:00 request returns 400 with `INVALID_INTERVAL` or `INVALID_DURATION` and changes neither the caller list nor the busy set; a blank purpose returns 400 `INVALID_PURPOSE` with no row; the 14:00-16:00 Training session claim returns 201 and appears exactly once.
- A03: a 14:30-15:30 overlap returns 409 `SLOT_CONFLICT` with the original id, its 14:00 and 16:00 values, and a message naming both windows; busy state and stored rows do not change; 16:00-17:00 is accepted.
- A04: a non-owner cancel returns 403 and leaves the block; the owner cancel returns 204, keeps the row as cancelled, and frees the window; a fresh claim returns 201; a repeat cancel returns 404 `NOT_FOUND`.

## Meaningful negatives

- Non-Monday `weekStart` -> 400 `INVALID_WEEK_START`.
- Zero-length 14:00-14:00 -> 400 with an accepted interval or duration code; caller row set and week busy set unchanged, so a server that returns 400 but inserts a ghost row fails.
- Blank purpose -> 400 `INVALID_PURPOSE`; no row.
- Overlapping 14:30-15:30 -> 409 with the existing id and both intervals; no row.
- Non-owner cancel -> 403; block remains.
- Repeat cancel -> 404.

## Manual UI check

With the service running behind the trusted ingress, open `http://127.0.0.1:8080/rooms/aurora/week?weekStart=2026-10-19` with an `X-Actor` identity. For local demo only, start with `NODE_ENV=development DEV_ACTOR=alex`. Expect seven days, the accepted blocks, a claim form, and Cancel controls for your own blocks. The probe does not render the page and cannot verify layout.

## Not proven

No install, start, UI rendering, accessibility, performance, multi-instance, SSO, CSRF, rate-limit, calendar-sync, retention, or disaster-recovery check. The probe cannot prove that the database is disposable; the operator must enforce isolation. No result is a production certification.