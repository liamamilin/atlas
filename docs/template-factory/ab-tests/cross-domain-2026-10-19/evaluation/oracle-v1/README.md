# Independent outcome oracle — frozen before template production

This toolchain was authored by an independent test engineer using only the three common REQUEST.md, request.json, CONTRACT.md files and protocol.json. The engineer did not read the condition mapping, any produced cognitive package or developer output. The API/CLI contracts are identical inputs to all developers. They deliberately state strong requirements, so these checks measure implementation of those stated requirements, not discovery of unstated mature-product needs.

Core IDs and traceability are in rubric.json. No account system for budget, bank integration, payment, email, recurring booking, desktop file manager, or other unrequested feature is scored. The browser probes exercise only the common testid controls and verify writes through the real read-only API; API success never stands in for usable UI.

Run only after manually reading **all** generated application source:

```sh
python3 evaluation/run.py --case budget --app /absolute/reviewed-app --evidence /absolute/new-round --source-reviewed --browser
python3 evaluation/run.py --case booking --app /absolute/reviewed-app --evidence /absolute/new-round --source-reviewed --browser
python3 evaluation/run.py --case rename --app /absolute/reviewed-app --evidence /absolute/new-round --source-reviewed
```

Use a genuinely new evidence directory for every app/round; the runner refuses existing directories. Never edit an application to fit tests. Source manifests before/after, tool hashes, real process epochs, complete HTTP or CLI event logs, and result.json are recorded. Booking uses only the explicitly synthetic common-contract accounts; all app subprocesses receive a minimal environment without inherited provider credentials. HTTP uses direct loopback http.client without automatic redirect following. The CLI operates on new owned fixture directories, never actual Downloads or source directories. The symlink/external-plan tests use only owned sibling sentinel files under the same evidence directory.

Browser probes use the installed local Playwright package and Node runtime, with a deny-default proxy that allows only the exact target origin and port. HTTPS CONNECT and WebSocket attempts are blocked. Chromium's default loopback bypass is explicitly disabled. Real UI clicks perform writes; `fetch` in the page is used only for readback. Captured screenshots are **not** a visual assessment unless an evaluator actually opens them. There is no dependency installation.

Real restart means the owned server process is stopped and replaced with a different PID, using the same data directory; `--init-demo` is repeated for booking and must not reset history. Genuine conflict testing releases two separate HTTP requests through a two-thread barrier; exactly one must succeed and the other return 409. This finite probe cannot prove atomicity under all workloads. Source review and outcome review must also consider race guarantees.

Expected integration ambiguities accepted neutrally: `/api/me` may return a direct user or `{user: ...}`; booking detail/cancel may return a direct record or `{booking: ...}`. JSON identifier types are retained without assigning a fixed integer/string type. Successful mutations accept any 2xx. Unauthorized ownership lookup may use 403 or privacy-preserving 404. An already-applied rename may return explicit success or nonzero refusal as long as no files change again. Changed-file undo may refuse unchanged or restore the filename while preserving the new content; silently restoring an old byte snapshot is forbidden.

Failure interpretation: `failed` means a concrete assertion failed under the declared interface; `setup_or_tool_error_unverified` means no product conclusion can be drawn from that check alone. Later checks may depend on earlier successful fixture creation; assess root causes, do not count cascaded setup errors as separate independent defects. Browser failures preserve their error; reviewers distinguish selector/engine infrastructure from real product behavior. Source review is an operator assertion, not an OS sandbox. Binding/storage guarantees and password hashing require supplementary source review; the harness never claims full security certification.

The checks are fixed before generation. Any later oracle correction must keep this original freeze and all original evidence, record the correction reason, and run every affected arm on the same corrected oracle. Initial and repaired applications must remain separate. No fake application was used to validate these business assertions; only syntax/help/selfchecks of test utilities were run at freeze. **No application outcome is claimed at this stage.**
