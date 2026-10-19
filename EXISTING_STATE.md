# EXISTING STATE

## Directory Structure
- `application-atlas-production-pack/`: local API, Atlas corpus, project store, execution/recovery/backup services.
- `atlas-web/`: Vite/React frontend, generated public data, Playwright E2E.
- `docs/`: U17 decisions, release checklist, security and page audit notes.

## Entry Files
- Frontend: `atlas-web/src/main.tsx`, `atlas-web/src/app.tsx`
- API: `application-atlas-production-pack/drafts_api.py`
- Project state: `application-atlas-production-pack/project_store.py`
- Execution: `application-atlas-production-pack/execution_service.py`
- Backup/restore: `application-atlas-production-pack/project_backup.py`

## Core Modules
- Content pages: home, browse, leaf, search, apps, tutorial.
- Draft workflow: draft creation, generation, dedupe, promotion, dirty-state editing.
- Project workflow: references, requirements, decisions, document review, iterations, tasks, execution, apply, acceptance, backup/recovery.
- Safety: local API boundary, fixed verification, OpenCode V1/V2 permissions, apply/restore journals.

## Current Capabilities
- 10 user routes plus a catch-all route and global shell.
- Route-level lazy loading; generated data validation.
- Local project state, evidence, recovery and scoped backup.
- 180 backend tests, 6 frontend unit tests, 3 repeatable Playwright scenarios.

## Known Missing Features
See `docs/U17_PAGE_AUDIT.md` and `docs/U17_PAGE_POLISH_PLAN.md`.

## Existing Behavior
- Atlas is local single-user software; no automatic dangerous replay.
- User source workspaces are not included in project backups.
- OpenCode provider execution requires explicit environment configuration.

## Existing Tests
- Backend: `python3 -m unittest discover -s application-atlas-production-pack/tests -q`
- Frontend: `npm run typecheck && npm test`
- Browser: `npx playwright test --repeat-each=3`
- Data/build: `npm run build && npm run verify-data`

## High Risk Areas
- Draft polling and stale data.
- Project/iteration identity in nested panels.
- Source manifest mapping and long-content responsive behavior.
- Unknown route/error recovery semantics.

## Change Constraints
- Do not expose credentials or raw provider output.
- Do not auto-replay or auto-delete dangerous work.
- Keep source workspace outside the Atlas project database.
- Do not commit or push without explicit user instruction.
