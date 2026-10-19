# Local CI verification — 2026-10-19

This report records local verification of the CI gates on macOS 26.6.2, Node v22.21.1, npm 10.9.4, and Python 3.10.13. The checkout was at `d0a206dd749e866619379e152b26a880d1d3c104` when checks began; multiple implementation agents edited the shared working tree during the run, so this is evidence for the tested working-tree state, not an immutable commit. The backend full suite and final strict Docker gate were not repeated here while the parent was coordinating concurrent backend edits.

| Command/check | Result |
|---|---|
| `npm ci --registry=https://registry.npmjs.org --replace-registry-host=always` | Pass; 196 packages installed. The lockfile's previous `registry.npmmirror.com` tarball endpoints returned `ECONNRESET`, so the registry host was replaced for this run. |
| `python application-atlas-production-pack/export_atlas.py` | Pass; parsed 1,805 leaf documents, wrote Atlas SQLite/JSON exports. |
| `npm run gen` | Pass; generated 1,805 leaves, 270 sections, 33 apps. |
| `npm run verify-data` | Pass; no missing or stale generated files. |
| `npm run typecheck` | Pass (`tsc --noEmit`). |
| `npm test` | Pass; 9 tests, 0 failures/skips. |
| `npm run build` | Pass; Vite production build completed. |
| `npm run test:e2e` | Pass; 17 tests, 0 failures. Ran on local ports 5188/5199 after confirming the ports were free. |
| `npm run test:e2e:factory -- --reporter=line` | Pass after concurrent UI fixes; 25 tests, 0 failures. Ran sequentially on local ports 5208/5209. The first run before fixes had five responsive overflow failures; the clean run after the nav-wrap fix had 22/25, with three stale fixture expectations; a later clean run after those were corrected passed 25/25. |
| `npm audit --registry=https://registry.npmjs.org --audit-level=high` | Pass, exit 0 after lockfile update to `source-map-js` 1.2.2. Two moderate `postcss-selector-parser` advisories remain; npm reports its suggested fix requires `npm audit fix --force`, which would downgrade `@tailwindcss/typography` to 0.5.4. No forced downgrade was applied. |
| `python -m pip_audit -r requirements.txt` using `pip-audit==2.10.1` | Pass; no known vulnerabilities. |
| Ruff CI path list from `.github/workflows/checks.yml` | Pass at check time: “All checks passed!”. This is a lint result only; it does not substitute for the parent-run full backend test suite. |

The npm audit gate is configured at `--audit-level=high`, so the two moderate advisories are visible in audit output but do not fail that configured threshold. The lockfile update changes only the resolved `source-map-js` package from 1.2.1 to 1.2.2 and its registry URL/integrity hash.

The earlier strict Docker run recorded in [ci-baseline.md](../ci-baseline.md) had 18 repository tests and zero skips. Of those, eight execute actual Docker integration paths (seven verifier tests plus one API-queued frozen-source test); the remaining ten use fixtures/mocks. The 18-test count must not be described as 18 containerized app runs. Because runtime code continued changing in the shared tree after that run, the final required Docker gate remains to be repeated on the stable final tree before claiming current Docker verification.

The two Playwright suites and the build use the local repository and synthetic route fixtures where specified. Passing them does not establish independent acceptance of a real generated application.
