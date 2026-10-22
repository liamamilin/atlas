# Core verification — Sideloaded Shelf template

This probe verifies A01–A05 over HTTP. It is a verifier, not an implementation requirement: the target may be the Node.js plus TypeScript service described in the architecture or any stack that honours the same contract.

## What the cases assert

- A01 — one scan creates 3 entries (embedded metadata, second embedded book without artwork, filename-derived title), reports the byte-identical duplicate and the broken EPUB, rejects the symlink that resolves outside the shelf, serves a cover for each entry, and a second scan creates nothing with stable ids.
- A02 — stale revision 409, unknown PATCH field 422, valid correction with manual provenance and revision increment, atomic collection assignment, restart durability, rescan does not revert.
- A03 — quoted author, case-insensitive title, collection field, unmatched values, unknown field 422, multi-term AND.
- A04 — exact download bytes, EPUB content type, attachment disposition, HEAD size, missing format 404, unknown entry 404, path-like format token rejected.
- A05 — explicit policy required, catalog-only delete 204, entry unsearchable, no shelf file changed, repeat and unknown delete 404, rescan re-creates a fresh entry, further scan idempotent.

## Prerequisites

- python3 with the standard library only; no pip installs and no network access.
- The target checkout with dependencies installed and built, startable by a command such as `npm start`.
- POSIX shell with process-group support (macOS or Linux) for the restart check; elsewhere restart timing is best effort.
- Ports are chosen dynamically; the probe sets PORT itself and binds only 127.0.0.1.

## Target contract used by the probe

Environment: ATLAS_DATA_DIR (writable, isolated), ATLAS_LIBRARY_ROOT (read-only shelf), HOST=127.0.0.1, PORT.

- GET /healthz returns 200.
- POST /api/scans with `{root}` returns 200 and counts `{created, unchanged, duplicates, failed, ignored}` plus items with path, status, reason, work_id.
- GET /api/books returns `{total, items}`; each item has id, title, author, cover_url (root-relative), cover_source, metadata_source, revision, manual_fields, collections, files (format, size, sha256).
- GET /api/books/:id returns one entry or 404 book_not_found.
- PATCH /api/books/:id takes revision plus title and author; stale revision is 409 revision_conflict; an unsupported key is 422 unknown_field; success increments revision by one and sets metadata_source manual.
- POST /api/collections `{name}` returns 201; a duplicate name is 409 collection_exists.
- PUT /api/books/:id/collections with `{names}` replaces the set atomically; an unknown name is 422 unknown_collection and changes nothing.
- GET /api/books?q= supports title:, author:, and collection: with quoted values; unsupported fields return 422 unknown_field.
- GET and HEAD /api/books/:id/file?format= stream the stored file as an attachment with its content type; missing format is 404 format_not_found; unknown entry is 404 book_not_found.
- DELETE /api/books/:id?file_policy=catalog_only returns 204 and removes only catalog rows; a missing or other policy is 422 invalid_file_policy; unknown or already-removed ids are 404.

## Run

```bash
cd acceptance
python3 probe.py --start npm start
python3 probe.py --start python3 -m my_service --keep
```

Everything after `--start` is the target command. Exit code 0 means all five cases passed, 1 means at least one check failed and the failures are listed, 2 means the probe or target setup failed. `--keep` leaves the disposable shelf, data directory and service log in the printed temp path for inspection.

## Fixtures and safety

The probe builds everything under a fresh `shelf-accept-*` temp directory: a shelf with three valid EPUBs (one with an embedded cover, one without artwork, one with no dc:title so the filename is used), a byte-identical duplicate, a file that is not a ZIP, and a symlink to an EPUB outside the shelf root. The catalog lives in a separate data directory. The probe never reads or writes a real library; A05 asserts every shelf file hash is unchanged after removal. Never point ATLAS_LIBRARY_ROOT at a library you care about while developing.

## Manual checks that remain human

Start the service and use the web UI to confirm: the shelf renders covers and titles; the detail form saves a corrected title and author and reloads them; collection assignment appears in the entry; search shows the corrected entry; the download opens in the reader; and the remove action asks for the catalog-only policy, states that the file is kept, and the file is still present afterwards. The probe does not inspect HTML, layout, accessibility, or an external reading application.

## Not verified

Real MOBI bytes (supply your own DRM-free fixture), DRM handling, fuzzy ranking, range or resumable downloads, concurrent scan races, crash recovery mid-scan, multi-format attachment, and an undo or trash path for removal. No certification or production readiness is implied by a passing run.