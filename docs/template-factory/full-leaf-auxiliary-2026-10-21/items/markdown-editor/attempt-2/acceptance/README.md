# README Markup Editor - core verification

## Adapter and boundary
`probe.py` is a stdlib-only orchestrator. It requires Node.js >=18 on PATH, writes one temporary `.mjs` driver outside the target, imports `app/src/core.js` as an ES module, and asserts the four capability cases against the same pure functions that `src/app.js` wires to the DOM. It does not start a browser or server, install packages, use the network, or modify the target. Each run uses a disposable temporary directory that Python removes.

The target is a static Web app. The probe verifies its core contracts, not pixel layout, download placement, or the upstream repository.

## Files expected
`app/index.html`, `app/styles.css`, `app/package.json` with `type: module`, `app/src/core.js`, `app/src/app.js`.

## Run
```text
python3 acceptance_files/probe.py app
python3 acceptance_files/probe.py app --json
```
Exit codes: 0 all four cases passed; 1 a case failed or the adapter could not run; 2 not_run because Node.js >=18 is absent or unusable. `--json` prints status, per-case statuses and failure strings.

## Cases
- A01 selection-based markup insertion: Bold text and selection, H1 prefixes and idempotence, blank and empty no-ops, UTF-16 offsets, and coded errors for INVALID_SELECTION and UNKNOWN_ACTION.
- A02 derived preview: h1 and strong output, no literal markers, escaped HTML, inline code and emphasis, paragraph boundaries, CRLF equivalence, determinism, unmatched markers, and INVALID_CONTENT.
- A03 markup-only save and reopen: default README.md, text/markdown, body identity for LF, CRLF and BOM, reopen text and preview equality, custom and unsafe names, blank and oversized errors, non-string inputs, and the 1 MiB UTF-8 cap on open and save.
- A04 rendered counts: 4 words and 17 characters for the pinned example, bolding neutrality, 0/0 empty, marker exclusion, inline-code inclusion, UTF-16 units, key order, and INVALID_CONTENT.
A case passes only if every assertion in it passes. The probe makes no broader certification claim.

## Contract expected
`app/src/core.js` is an ES module exporting:
- `applyMarkup({text,start,end}, 'bold'|'h1')` returning `{text,start,end}`.
- `renderMarkdown(text)` returning an HTML string.
- `countText(text)` returning `{words,chars}` in that key order.
- `createSavePayload({text,start,end}, filename = 'README.md')` returning `{filename,mime,body}`.
- `openText(raw)` returning `{text,start:0,end:0}`.
Error codes are `INVALID_SELECTION`, `UNKNOWN_ACTION`, `EMPTY_DOCUMENT`, `INVALID_FILENAME`, `FILE_TOO_LARGE` and `INVALID_CONTENT`, attached as `err.code`.
An H1 on an empty or whitespace-only document is a no-op, not an insertion; the probe asserts that policy. Blank or whitespace-only saves raise EMPTY_DOCUMENT. The filename contract is a safe base name ending in `.md`, 4 to 120 characters, with no path separators, spaces or leading dot. Open and save both cap UTF-8 input at 1,048,576 bytes; the boundary is accepted and one byte more raises FILE_TOO_LARGE.

## Manual UI check (not automated)
1. Use a fresh empty download folder and run `python3 -m http.server 4173 --directory app`; open http://localhost:4173. Save is disabled and counts show 0/0.
2. Paste a plain draft such as `My Project` followed by a blank line and `A plain phrase in the draft.`.
3. Select `plain` and click B. The text becomes `**plain**`, the phrase remains selected, the preview shows strong text, and counts do not change.
4. Select the first line and click H1. It becomes `# My Project`; the preview shows a heading and counts still reflect the rendered words.
5. Click Save. The browser downloads README.md (the browser may rename on collision). Open the file in a text editor and confirm the literal `# ` and `**` characters with no HTML or style data.
6. Use Open to reopen that downloaded file. The textarea and preview are identical to before saving.
7. Negative checks: whitespace-only text leaves Save disabled; a safe but oversized temporary `.md` file produces FILE_TOO_LARGE. Do not test with or overwrite a user's existing project README; use a disposable folder and move files deliberately.

## Not_run limits
- No browser automation: layout, file chooser, download location and naming, and undo behavior are manual only.
- The probe does not install or run the upstream Marcdown app; source observations are static evidence at the pinned commit.
- If Node.js is missing or older than 18, exit code is 2 and no case is reported as passed.
- Non-UTF-8 input is decoded by the browser as UTF-8 with replacement characters; no encoding picker exists.
