# Independent final acceptance report

**Verdict: PASS for the frozen P0 user flow.** The final repair bundle passed the independent browser workflow and survived a real Docker container restart with saved records and categories intact. Separate post-hoc HTTP probes rejected the CRLF URL without storing data or adding a response header, and all 20 concurrent same-name category rounds retained the successful response with no HTTP 500s.

## Frozen artifacts

- Scenario SHA-256: `835fd685630daeafbeb2602498f995ee6bdb5cf2382252bbcb66764086a434b1`
- Frozen PLAN SHA-256: `87698506065b6a66ad9b23897601345a24f48651fe8370d7abee49631ec09c89`
- SCOPE_NOTE SHA-256: `e792615d4f7eac7cddea72b26c3c7f16fe0d2c4029fa9841b0e27e81a31547e0`
- Freeze record SHA-256: `4fa15b363c7b190e8ae20d058f52fd4006b8b4326b00bead9b6dcd4f93ab778e`
- Repair application ZIP SHA-256: `406f755e0177a9a6337ec7daec67484b89db27a154f07c3476b9d5048f1f6389`
- Delivery SHA-256: `4accad35f8399183eb6a8426a971c8434611b69f0160d2b505e9dd29b86cb38e`
- Source package/context SHA-256: `93b5786c05e530252beef39644ba66614ddb0c93d4dd5c4facd23f237ad1fd73`
- Template: `tpl_934bc93157f948b982459a9affa72c79`, digest `3bbcbb2a2685f188756e5b47dd27ac606f11f72359910e09023084758bd972c1`.

The frozen repair scope lists only `app/server.py`, `app/storage.py`, and `app/validation.py`. Full hashes for all application files and delivery metadata are included in `FINAL_ACCEPTANCE_REPORT.json`; the UI runner's before/after source hash maps match exactly.

## Preregistered UI flow and restart

All nine UI observations passed: save to the default category, create a category, save in it, move and browse by category, keyword search, open the original page, HTML output safety, invalid-input rejection without dirty data, and the duplicate-save risk observation. The invalid-input cases (empty/malformed URL, `javascript:`/`data:` schemes, blank category, duplicate category) each returned HTTP 400 and left inventory unchanged. XSS sentinel execution and dialogs were not observed.

The duplicate URL test created a second record (`1 -> 2`) when submitted again. This was recorded as observation-only because the frozen contract does not promise URL uniqueness or idempotency. It is not counted as a failure.

The app container was actually restarted. Docker's `StartedAt` changed from `2026-10-19T03:51:10.100324637Z` to `2026-10-19T03:51:27.227151047Z`. After restart, the harness rechecked collections, saved/moved bookmarks, search, both exact original targets, duplicate-observation state, and HTML safety; all passed.

## Separate post-hoc probes

These probes are exploratory and are not part of the preregistered P0 verdict. A CRLF-bearing URL was rejected with HTTP 400. Bookmark and category inventories were unchanged, so there was no `/go/<id>` redirect to inspect; no injected response header appeared. The independent HTML parser cross-check found exactly one category with the expected name and ID.

Twenty rounds each submitted two concurrent requests for the same category name. Each round returned one 303 and one 400; all 20 acknowledged names were present in the subsequent HTML inventory, with zero HTTP 500 responses and zero client errors. Raw per-round snapshots and server logs are retained.

## Environment and cleanup

The app ran from the verified archive in Docker image `python:3.12-slim` (`sha256:ce9a404c2c0138e747a43e6ea022d2f7e670ed868df35d627a663ba7fb940ea9`) with the source mounted read-only and a dedicated writable state directory. The container dropped all capabilities, enabled `no-new-privileges`, and had memory/CPU/process limits. Its published port was bound only to `127.0.0.1`. The container used a dedicated Docker bridge; bridge egress was **not** enforced, so this is not claimed as a network-none test. Chromium was restricted to the application origin and local fixture origin, with other browser requests aborted.

Both runs verified container and network removal, temporary-state removal, and fixture shutdown. No app/source bytes were manually changed during acceptance.

Detailed evidence is retained in `evaluation/repair-1/` and `evaluation/posthoc-http-repair-1/`; the machine-readable record contains the full source hash map and test observations.
