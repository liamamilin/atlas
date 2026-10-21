## workflow

### 0
"Start the local server against a disposable data directory; initialize the SQLite schema on first
start."

### 1
"Create the single home with POST /api/home, then add equipment records with POST /api/equipment
anchored by home_id."

### 2
"Create care plans with POST /api/plans using interval_days and an optional equipment anchor."

### 3
"Query GET /api/tasks/due with an explicit as_of and horizon_days to see the exact overdue, due, and
upcoming task sets."

### 4
"Record a completion and note with POST /api/plans/{id}/completions; one transaction appends the
actual completion and note, stores the true latest completion date, and sets due_on to max(old
due_on, latest + interval_days)."

### 5
"Read GET /api/plans/{id}/completions or GET /api/history filtered by home_id and equipment_id."

### 6
"Use GET / for the basic accessible single-page UI; all actions remain available through the
documented JSON API."

## acceptance

### 0
"A fresh database has no home; POST /api/home creates exactly one record with id home, and a second
POST returns 409 HOME_EXISTS without mutating the stored home."

### 1
"POST /api/equipment under the existing home returns 201 and round-trips through list and detail;
blank names, invalid categories with otherwise valid fields, and unknown homes return 422 or 404 and
add no equipment row."

### 2
"POST /api/plans enforces interval_days 1..3650 and mutual exclusion of last_completed_on and
first_due_on; GET /api/tasks/due returns exact overdue, due, and upcoming ID sets and counts at
as_of and horizon_days boundaries, so duplicate, extra, or missing tasks fail, while invalid
requests write nothing."

### 3
"A completion with note inserts one history row and atomically sets last_completed_on to
max(existing last_completed_on if present, completed_on) and due_on to max(old due_on, latest +
interval_days); leap-day, month-end, year-end, initial-backfill, no-anchor, future-date, oversize-
note, and unknown-plan failures leave both plan and completions unchanged."

### 4
"GET /api/history filters by home and equipment and returns documented fields in descending
completion order; invalid filters write nothing; GET / is dependency-free accessible HTML with html
lang=en, every input labelled by for/id, fieldset/legend groups, a due-table caption with th
scope=col, and a role=status aria-live=polite feedback shell; unknown routes or methods return
documented JSON errors."

## observations

### 0
["documentation", "README.md", 17, 17, "Document claim: micasa describes itself as home maintenance
from the terminal, a local tool rather than a hosted multi-tenant service."]

### 1
["documentation", "README.md", 25, 25, "Document claim: the upstream advertises schedules, due
dates, and full history."]

### 2
["code_observation", "internal/data/models.go", 104, 135, "Code observation: HouseProfile stores
address, year built, systems, and other attributes; no explicit multi-home ownership table is
observed in the selected files."]

### 3
["code_observation", "internal/data/models.go", 201, 216, "Code observation: Appliance stores make,
model, serial, warranty, and location, with no home_id field observed."]

### 4
["code_observation", "internal/data/models.go", 218, 237, "Code observation: MaintenanceItem has an
optional ApplianceID, category, season, interval months, last serviced date, and due date."]

### 5
["code_observation", "internal/data/models.go", 261, 274, "Code observation: ServiceLogEntry belongs
to a maintenance item and stores serviced_at, optional vendor and cost, notes, and timestamps."]

### 6
["code_observation", "internal/data/store_house.go", 22, 31, "Code observation: CreateHouseProfile
counts existing profiles and rejects a second row, implementing one house profile."]

### 7
["code_observation", "internal/data/store_maintenance.go", 24, 33, "Code observation:
ListMaintenanceByAppliance filters maintenance items by appliance id, showing an equipment-anchored
query path."]

### 8
["code_observation", "internal/data/store_servicelog.go", 16, 30, "Code observation:
syncLastServiced sets LastServicedAt to the most recent non-deleted serviced_at."]

### 9
["code_observation", "internal/data/store_servicelog.go", 59, 73, "Code observation:
CreateServiceLog runs in a transaction, creates the service log, then syncs the parent maintenance
item."]

### 10
["code_observation", "internal/data/validation.go", 168, 177, "Code observation: ComputeNextDue
returns an explicit due date when set, otherwise adds interval months to the last service date."]

### 11
["code_observation", "internal/data/validation.go", 182, 192, "Code observation: AddMonths clamps
the day to the target month end, avoiding the Jan 31 plus one month overflow."]

### 12
["code_observation", "internal/data/validation.go", 98, 153, "Code observation: interval parsing
accepts years and months, not days."]

### 13
["code_observation", "internal/data/dashboard.go", 12, 25, "Code observation: scheduled maintenance
is defined as interval months greater than zero or an explicit due date."]

### 14
["documentation", "README.md", 58, 58, "Document claim: the upstream is pure Go using SQLite and a
terminal UI; this target does not copy or run that implementation."]

## features

### 0
"Home and equipment anchor"

### 1
"Every-N-day plan and due queue"

### 2
"Completion and next-due rollover"

### 3
"Anchored care history"

### 4
"Accessible localhost UI"

## goals

### 0
"In a dedicated data directory, create the single home, add an equipment record under it, and prove
duplicate-home and invalid-name, invalid-category, and unknown-home requests return 409, 422, or 404
without changing stored records."

### 1
"Create plans with interval_days in 1..3650 and verify GET /api/tasks/due returns exact overdue,
due, and upcoming ID sets and counts at the as_of and horizon_days boundaries, using fresh equipment
scopes, while invalid plans write nothing."

### 2
"Record a completion and note in one atomic call and verify last_completed_on is the true latest
date and due_on is max(old due_on, latest + interval_days) across leap-day, month-end, year-end,
initial-backfill, and no-anchor creation-day examples, with invalid completions leaving no trace."

### 3
"Retrieve completions filtered by home and equipment in documented descending order with plan and
equipment names and notes, and reject invalid filters without writes."

### 4
"Load GET / and assert a dependency-free HTML shell exposes home, equipment, plan, due, completion,
and history workflows with structural accessibility relationships (label for/id, fieldset/legend,
due caption and th scope=col, role=status, aria-live=polite, lang=en), while unknown routes and
methods return documented JSON errors."

## gaps

### 0
"Upstream status: not_run. The repository was read as evidence only; no build, test, server, TUI, or
database was executed, so no upstream behavior is runtime-verified."

### 1
"Runtime verification is not_run for the target too. The probe and architecture are authored
artifacts; no server was started and no acceptance case was executed in this task."

### 2
"Single-home and single-user by design; no multi-property, accounts, authentication, sharing, or
remote access."

### 3
"No notifications, email, SMS, push, calendar sync, or background scheduler; due work is pull-based
through the API and UI."

### 4
"No costs, vendors, receipts, photos, manuals, warranties, projects, quotes, incidents, documents,
or LLM features; those upstream surfaces are intentionally out of scope."

### 5
"Every-N-days recurrence differs from upstream interval months; no compatibility with upstream
databases, APIs, or schema is claimed."

### 6
"No delete, undo, archive, or restore endpoints; completion history is append-only and test records
remain until the disposable data directory is discarded."

### 7
"Validation is strict and date-only; natural-language dates and timezone conversion are unsupported.
Server local date can differ by one day from a client in another timezone."

### 8
"The UI is a minimal single-page client, not a polished product; no internationalization, offline
cache, or mobile-native behavior. Accessibility assertions are structural and do not certify full
conformance."

### 9
"Schema v1 has no migration path. Changing entities later needs an explicit migration or a new
disposable database."

### 10
"Concurrency is sized for one user; SQLite WAL and busy_timeout reduce but do not eliminate lock
contention."

### 11
"User decision points: confirm one-home scope, creation-day due for plans without an anchor,
`max(old due_on, latest completion + interval_days)` rollover that never regresses, strict date-only
input, and the absence of delete and defect-tracking features."

### 12
"Restart durability may be described as an operator stop and start step in README; it was not run
and is not claimed as verified."
