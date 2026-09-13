# Research Notes — Error Tracking Platform

## Research Goal

Understand, from real products, what an Error Tracking Platform is and how it works:

> What is captured, how raw error events become manageable issues, what the issue lifecycle is, what context surrounds an error, and where the Type's boundary sits against bug tracking, log management, APM, observability, and incident management.

## Initial Boundary

Working hypothesis before research:

- **Core use**: capture errors/exceptions/crashes occurring in running software automatically, aggregate the flood of duplicate events into distinct issues, and let a team triage those issues to resolution.
- **Primary users**: software developers / engineering teams; secondarily SREs and support-facing teams consuming error signal.
- **Nearest neighbors**: Bug Tracking System (§12, processed), Issue Tracker (§12, processed), Log Management (§14, processed), APM (§12, processed), Observability Platform (§14, processed), Metrics Monitoring (§14, processed), Distributed Tracing (§14, processed), Incident Management (§14, processed), On-call Management (§14, processed), Static Code Analysis (§12, processed), Debugger / Profiler (§12, processed), AIOps (§14, processed), IT Problem Management (§14, processed).
- **Counterparty flags to discharge**:
  - it-problem-management (§14, 2026-09-08): expected seam — software defect/error objects are signal or code-fix units vs the IT-operational cause record with workaround/change dispositions.
  - log-management (§14, 2026-09-08): expectation — error tracking centers exceptions grouped/deduplicated into issues with release context vs the raw ungrouped record stream.
  - debugger (§12, 2026-09-07): research notes list "error-tracking platform" as a remove-target (no execution control).
- **Unknowns going in**: whether release/version attribution is definitional or common; whether the triage lifecycle is definitional; how suite-embedded error tracking differs structurally from pure-play; whether mobile crash reporting is a variant or a separate Type.

## Research Questions

1. What exactly is captured (unhandled exceptions, handled errors, crashes, messages)? By what mechanism (SDK/notifier/API)?
2. How are raw events grouped into issues (fingerprint/hash)? How configurable? How are grouping errors corrected?
3. What is the issue lifecycle (states, transitions, assignment, resolution, recurrence)?
4. What context attaches to an error event (release/version, environment, user, request, breadcrumbs)?
5. How does release/deploy tracking interact with issue state (regressions, resolve-in-release, auto-resolution)?
6. What alerting/notification exists and where does it route?
7. What are the main interfaces (issue list, issue detail, event detail, release views, settings)?
8. Pure-play vs suite-embedded: same structure or different?
9. Mobile crash reporting: variant or separate Type?
10. What integrations exist (issue trackers, source control, chat/pager)?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **Sentry** | dominant pure-play, developer-workflow-centric, now broad suite | deepest docs; defines the modern category vocabulary (issues, fingerprints, releases) |
| **Rollbar** | pure-play, error-management-workflow-centric | explicit Item/Occurrence model; self-describes as "real-time error tracking platform" |
| **BugSnag** (SmartBear) | pure-play, stability/release-health-centric for product teams | stability scores + release-aware error workflow; mobile emphasis |
| **Datadog Error Tracking** | suite-embedded pole (over RUM/Logs/APM) | tests whether the Type's structure survives packaging inside an observability suite |
| **Airbrake** | heritage pure-play (2008-era exception reporter) | historical anchor; feature index confirms the old-generation shape |

Historical / market-sample check targets (no deep fetch): Errbit (open-source self-hosted Airbrake-style notifier, 2011-era), pre-SaaS server error logs, OS crash-dump reporting.

## Sources

Research date: **2026-09-10**. All Layer A observations below come from official vendor documentation fetched live on this date.

- Sentry: https://docs.sentry.io/product/ , /product/issues/ , /product/issues/states-triage/ , /product/issues/grouping-and-fingerprints/ , /product/issues/issue-details/error-issues/ , /product/releases/
- Rollbar: https://docs.rollbar.com/ (docs root + llms.txt index), https://docs.rollbar.com/docs/rollbar-terminology
- BugSnag: https://docs.bugsnag.com/ , /product/ , /product/error-grouping/ , /product/error-status-and-actions/ , /product/stability/
- Datadog: https://docs.datadoghq.com/logs/error_tracking/ , /error_tracking/explorer/ , /error_tracking/issue_states/
- Airbrake: https://docs.airbrake.io/docs/ (docs index only)

**Source-access limitations**:

- Firebase Crashlytics (firebase.google.com/docs/crashlytics) timed out twice on 2026-09-10 — abandoned per network rules. The mobile crash-reporting pole is therefore evidenced indirectly (BugSnag mobile session/stability docs, Sentry release-health crash-free metrics, Rollbar crash_report occurrence type) and Crashlytics is cited only as a positioning-level market anchor, not as an evidence source.
- Rollbar deep pages beyond the terminology page and the llms.txt index were not fetched; Rollbar observations are Layer A for the terminology page and index-level for feature existence.
- Airbrake evidence is index-level (feature existence confirmed from the official docs index; page bodies not fetched).
- No pricing/quota numbers asserted anywhere; quota mechanics asserted only where a vendor states them qualitatively.

---

## Product Observations

### Sentry (Layer A unless noted)

**Capture.** "Sentry automatically captures unhandled exceptions and groups similar errors into issues." Error issues capture "errors, uncaught exceptions, and unhandled rejections, as well as other types of errors, depending on the platform." An error issue is "a grouping of error events." Levels: error, info, warning, fatal, debug, sample.

**Grouping.** "We group similar events into issues based on a fingerprint." A fingerprint "uniquely identif[ies] an event"; default fingerprints are computed "using built-in grouping algorithms based on information such as a stack trace, exception type, and message." For error issues, "a fingerprint is primarily defined by the event stack trace." Customization: merging similar issues; fingerprint rules (project settings); stack trace rules (which frames count); SDK-side fingerprinting. Rules affect future events only. The Issue Details page exposes "Event Grouping Information" — which stack-trace parts contributed to the fingerprint.

**Issue as record.** Issue = "a single bug or problem with your app." Issues page shows: issue type and description, project, first/last seen, event counts, users affected, level. Quota note: "Your quota is consumed by *events*, not *issues*."

**Lifecycle.** Statuses: New (created within a recent window), Ongoing, Escalating (exceeded forecasted event volume), Regressed (resolved issue that came up again), Archived, Resolved. One status at a time. Manual: Archive (with options: forever / set period / until N occurrences / until N users affected; archived-forever issues still record events but never escalate), Resolve, Delete, Delete-and-Discard-Forever (error issues only; future events discarded and not counted toward quota). "For Review" list = new/regressed/unresolved issues not yet marked reviewed. Sorting: Recommended, Last Seen, First Seen, Trends, Events, Users. Saved searches. Ownership rules auto-assign issues. Reprocessing with new debug files. Seer Inbox (AI) groups assigned issues by closeness-to-fix (Layer A existence; AI posture treated as variant).

**Release context.** "A *release* is a version of your code deployed to an environment." Release health: user adoption, crash-free users, crash-free sessions, session data. Resolve-in-release: current release / next release / a chosen release / resolved-in-commit; recurrence in a newer release → automatic Regressed status and appearance in For Review. Suspect commits: "the code change that likely caused the problem." Releases auto-created on first event carrying the identifier if not notified.

**Alerting.** Alerts on issue state changes/filters, routed to Slack, PagerDuty, or the issue tracker; cron and uptime monitors create their own issue categories.

**Suite breadth (variant evidence).** Traces/spans, logs, session replay, profiling, application metrics, agents/LLM capture, dashboards, user feedback, snapshots, size analysis, build distribution, AI (Seer: root-cause explanation, Autofix, AI code review). The Issues page remains the documented center ("Sentry helps developers find and fix what's broken").

### Rollbar (Layer A for terminology page; index-level otherwise)

**Positioning.** Docs callout: "You're visiting the only real-time error tracking platform." Track "versions, deploys, customer impact, and more with an easy SDK install."

**Core model (terminology page, verbatim-faithful).**
- **Item** = "the fundamental unit of work in Rollbar. Each Item represents a group of Occurrences that represent the same underlying condition." "You don't add Items directly into Rollbar. Rather, you send Occurrences, and then Rollbar groups them into Items." For each Occurrence, Rollbar computes an identity hash (grouping engine + custom rules); same hash in the same project and environment → repeat Occurrence of the existing Item; unseen hash → new Item.
- **Occurrence** = "the raw events that you send to Rollbar" via SDK or API. Types: a single time an error/exception occurred ("trace"/"trace_chain"), a single time a native app crashed ("crash_report"), a single time an important event was logged ("message").
- **Counter** = unique sequential numeric identifier per project.
- The grouping engine "has knowledge about languages, frameworks, and common open source libraries"; manual merge of Items; custom fingerprinting rules; configurable file-path canonicalization.

**Lifecycle.** Item statuses: Active, Resolved, Muted, Merged. Transitions: New (→Active), Resolved, **Reactivated** (Resolved→Active due to a new Occurrence — "useful for getting notified about regressions"), Reopened (manual Resolved→Active), Muted/Unmuted, Merged/Unmerged. Resolve paths: UI, REST API, resolve via commit message + deploy notification, auto-resolve on deploy, auto-resolve old items (age-based). Item Owner, Item Levels (severity), Item Snooze (pause notifications for a period).

**Context & tracking.** Version tracking, deploy tracking (CI integrations: Bash/Capistrano/CircleCI/Jenkins/Heroku…), person tracking ("customer impact"), environments + hosts, projects, users/teams/accounts. Source maps; telemetry (events preceding the error); code context in tracebacks.

**Surfaces & integrations.** Items list (saved views), Item detail (Occurrences tab, Related Items, summarization), RQL (query language), Dashboard, Analyze/Improve modules (index-level), notifications (Slack/PagerDuty/OpsGenie/webhooks/Discord), issue-tracking integration (Jira/Trello/GitHub/Asana/Azure DevOps/Shortcut), Rollbar Resolve (AI-assisted root cause; index-level), MCP server setup (index-level), Terraform provider.

### BugSnag (Layer A)

**Grouping.** "BugSnag aims to group instances of the same event together to give you a clear view of which issues are having the biggest impact on your users whilst minimizing unnecessary noise." "Individual events are grouped into errors in your inbox and the reason for the grouping is shown at the top of the error view." Default algorithms chosen per language/SDK/data: top in-project stack frame (error class + file + line of the top in-project frame of the innermost exception); top in-project frame code; surrounding code (JS); method/file/line (JS); script tag / script tag line (JS); error class (eval); line number (web workers). Custom grouping: group by error class; group by error context; custom grouping hash (SDK-set); grouping discriminator (tie-breaker to split). Grouping-algorithm updates are opt-in and irreversible, applied to future events only.

**Lifecycle.** Statuses: Introduced today, Open, For review ("open errors awaiting triage"), Assigned to me/anyone, Issue created (linked third-party tracker issue), Fixed, Snoozed (temporarily ignored until a condition), Ignored (indefinite; manual reopen only). Actions: Assign; Create-or-view issue; Discard ("removed and future occurrences won't be stored or count towards your event limit"); Un-Discard; Delete; Ignore; **Mark as fixed** ("if the error occurs again in a version released after the most recent version it previously appeared in, it will be reopened and appear in your Inbox"); Reopen; Snooze; Fix with MCP (LLM investigation via SmartBear MCP server). "Events continue to be collected" for fixed/snoozed/ignored errors.

**Stability (release health pole).** "Stability is a measure of the proportion of user application sessions that are error free." Two scores: user stability (% of users error-free per day) and session stability (% of sessions error-free). Targets: Target stability and Critical stability, with a three-state indicator against the 30-day score and per-release lifetime score. "Any session in which a user experiences an 'unhandled' error is considered a crashing session"; a session with multiple unhandled errors counts once; snoozed/ignored unhandled errors still impact stability; rate-limited events do not (documented caveat). Session definitions per platform: mobile (app opened or returned after ≥30s background), browser (page load), server-side (request processed); overridable via `startSession()`.

**Other.** Releases & versions (configure version + release stage "to unlock powerful features"); feature flags & experiments (monitor errors during rollouts); automatic error assignment (rules-based to collaborator/team); pivot table; search & segmentation; sensitive-data redaction (PII); roles & permissions; SSO; on-premise offering; event-usage management (quota).

### Datadog Error Tracking (Layer A)

**Positioning (suite-embedded).** Error Tracking exists for Logs, and the Explorer "consolidates errors from multiple Datadog products (RUM, Logs, APM) into a unified view" (All / Browser / Mobile / Backend sources). "Error Tracking simplifies debugging by grouping thousands of similar errors into a single issue."

**Issue as record.** "An issue is a group of similar errors related to the same bug. Datadog creates issues by computing a fingerprint for each error using some of its attributes such as the error type, the error message, or the stack trace. Errors with the same fingerprint are grouped together in the same issue." Issue provides: users impacted, when first occurred, which commit probably caused it. Explorer list shows: error type/message, file path, first/last seen, occurrences-over-time graph, count in period. Tags: New (first seen recently + FOR REVIEW), Regression (RESOLVED and occurred again in a newer version), Crash, Suspected Cause. Facets: error.message, error.type, error.stack, error.handling (handled vs unhandled, with product-specific semantics). Sorting: Relevance / Count / Newest / Impacted Sessions (RUM).

**Lifecycle.** Five statuses: FOR REVIEW (new or regressed, needs attention), REVIEWED (triaged, to fix now or later), RESOLVED (fixed, no longer occurring), IGNORED (no action needed), EXCLUDED (stops collecting new errors and stops counting toward usage/billing). All issues start FOR REVIEW. Automatic review on assignment or work-item creation. Automatic resolution: issue inactive (no new errors for a stated window) or last reported in an old version while a newer version does not report it (version-tag dependent). Automatic re-opening via regression detection. Manual status changes; Activity Timeline records state history.

**Triage aids.** Assigned-to filter; Issue Team Ownership via Git CODEOWNERS and service owners; Suspected Cause; "Fix available" (AI-generated fix); Error Tracking Monitors (new issue / high impact; exportable from explorer queries); issue panel links to related traces/logs for APM-sourced errors.

### Airbrake (index-level, Layer A existence only)

Official docs index confirms the heritage pure-play shape: Error grouping; Deleting and muting errors; Deploy tracking; App versions; Breadcrumbs; Backtrace links; Public/private/custom source maps; Hotspots (error concentration views); Aggregations; Daily/weekly digest emails; Severity FAQ; Project environments; Teams; Integrations (JIRA, Trello, Pivotal Tracker, GitHub/GitLab/Bitbucket, Slack, Teams, webhooks, Zapier); Performance Monitoring (APM) as a separate product section; monthly error quota / usage caps / rejected errors FAQ (quota economics).

---

## Cross-product Comparison

| Dimension | Sentry | Rollbar | BugSnag | Datadog ET | Airbrake |
|---|---|---|---|---|---|
| Raw event unit | error event | Occurrence (trace / crash_report / message) | event | error event (from Logs/RUM/APM) | error notice |
| Aggregated unit | **issue** | **Item** | **error** (in inbox) | **issue** | error group |
| Grouping basis | fingerprint (stack trace primary; type/message) | identity hash (grouping engine + custom rules), scoped per project+environment | default algorithms (top in-project frame etc.) + custom (class/context/hash/discriminator) | fingerprint (type/message/stack trace) | error grouping settings |
| Grouping correction | merge issues; fingerprint/stack-trace rules; SDK-side | manual merge; custom fingerprints; path canonicalization | custom rules; algorithm updates opt-in, irreversible | (not fetched in depth) | grouping settings FAQ |
| Lifecycle states | New/Ongoing/Escalating/Regressed/Archived/Resolved | Active/Resolved/Muted/Merged | Open/For review/Fixed/Snoozed/Ignored/Issue created | FOR REVIEW/REVIEWED/RESOLVED/IGNORED/EXCLUDED | mute/delete |
| Recurrence after resolve | Regressed (auto) | Reactivated (auto) / Reopened (manual) | reopened if recurs in a version newer than last-seen version | Regression tag (auto re-open) | (not fetched) |
| Release/version context | releases + resolve-in-release + release health | version tracking + deploy tracking + resolve-in-version | releases & versions + release-aware reopen | version tags + version-aware auto-resolution + regression detection | app versions + deploy tracking |
| User impact | users affected (sort/filter) | person tracking | user stability score | users impacted; impacted sessions | user hotspots |
| Handled vs unhandled | unhandled capture emphasized | uncaught-error reporting docs | unhandled = crashing session (stability) | error.handling facet | severity FAQ |
| Alerting | issue alerts → Slack/PagerDuty/tracker | notifications → Slack/PagerDuty/OpsGenie/webhooks | email + Slack workflows | Error Tracking monitors | notifications + digests |
| Tracker integration | issue tracker alerts/routing | Jira/Trello/GitHub/Asana/Azure/Shortcut | create/view issue; two-way sync | work-item creation (auto-reviews issue) | JIRA/Trello/Pivotal |
| Source maps/symbolication | yes (reprocessing with debug files) | yes | build & deploy integrations (symbol files) | (via RUM/browser setup) | public/private source maps |
| AI posture | Seer (root cause, Autofix, code review) | Rollbar Resolve; MCP server | Fix with MCP | Suspected Cause; Fix available | — |
| Packaging | pure-play → broad suite | pure-play | pure-play (SmartBear suite adjacency) | observability-suite capability | pure-play + separate APM |
| Quota unit | events (not issues) | occurrences | events | error events (EXCLUDED stops billing) | monthly error quota |

**Reading of the comparison (Layer B):** every sampled product independently converges on the same four-part structure — machine-captured runtime error events; the error's own diagnostic identity (type/message/stack trace + context) as both record content and grouping basis; fingerprint/hash aggregation of recurring events into persistent issues; and a managed triage lifecycle with recurrence detection. Release/version context, user impact, alerting, tracker integration, and symbolication appear in all five but with different depth and vocabulary — common mature structure, not definition. The suite-embedded pole (Datadog) preserves the entire structure; packaging changes nothing structural.

---

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being an error tracking platform:

1. **Automatic runtime error capture from the running application.** Errors, exceptions, and crashes occurring while the software runs are captured and reported by an embedded notifier/SDK (or an equivalent intake API) without a human filing them. *Remove →* bug tracker (human-filed defects) or log management (records emitted for their own sake).
2. **The error's diagnostic identity as record content and grouping basis.** Each captured event carries the error's own diagnostic content — exception type/message, stack trace/backtrace, execution context (environment, release, request/user data) — and this content is what identifies and distinguishes errors. *Remove →* generic alerting or anonymous error counting.
3. **Aggregation of recurring raw events into distinct persistent issues.** Many occurrences of the same underlying error are grouped — by computed fingerprint/hash with configurable rules and manual merge — into one addressable issue carrying occurrence counts, first/last seen, and (commonly) affected users. *Remove →* raw event stream / log search.
4. **The issue's triage lifecycle to a recorded disposition.** The issue carries a managed state the team works through (open/unresolved → resolved / ignored / muted, with assignment), the system enforces the transitions, and recurrence after resolution is detected and surfaced (regression / reopen / reactivation). *Remove →* error analytics dashboard or alert feed.

**Jointly-held load-bearing:**
- 1 alone = raw error feed / log stream
- 2 alone = crash-artifact analyzer / debugger territory
- 3 without 4 = error analytics dashboard
- 4 without 1–3 = generic ticket queue
- 1+2 without 3 = log management applied to errors
- 2+3 without 1 = manually-filed, deduplicated defect reports (bug tracker)
- 1+3 without 2 = anonymous error counting
- 3+4 without 1 = issue tracker with error-shaped records

### L1 — Common Mature Structure

Present across the sample; expected in the market; not definitional:

- release/version attribution (errors tagged with the producing release; resolve-in-release; regression = recurrence in a newer release) and deploy tracking
- affected-user / person tracking (user-impact counts, user stability)
- handled vs unhandled distinction; severity/level classification
- breadcrumbs / telemetry (events preceding the error)
- issue alerting and routing (new issue, regression, volume spike → chat / pager / email)
- assignment automation (ownership rules, CODEOWNERS)
- issue-tracker integration (linked tickets, two-way sync, resolve-via-commit)
- source-code integration (suspect commits)
- source map / symbol upload and stack-trace symbolication
- environments and projects as scoping containers
- search / filters / saved views over the issue population
- trends and dashboards (error rates over time, release health, stability scores)
- discard / delete-and-discard semantics (stop collecting a specific error)
- auto-resolution on inactivity or newer-version-absence
- quota economics where events (not issues) are the billing unit

### L2 — Variant / Optional Structure

- **mobile crash-reporting pole** — native crash capture, symbolication files, ANR handling, crash-free sessions as the headline KPI (Crashlytics-class products; BugSnag/Sentry mobile surfaces)
- **client-side/browser pole** — source maps, script-error quirks, third-party/bot filtering
- **packaging**: standalone pure-play vs capability embedded in an observability suite vs self-hosted/open-source deployment
- **AI assistance**: root-cause explanation, suggested fixes, AI triage/inbox ordering
- **suite drift**: performance/profiling/session-replay/logs/metrics extensions alongside the error core
- **feature-flag/experiment correlation**; **user feedback capture linked to errors**
- **quota/rate-limit postures** and what happens at the limit

### L3 — Vendor-specific (research notes only)

- Sentry: fingerprint property `{{ default }}`; Escalating forecast algorithm; archive-forever semantics; discard-forever (error issues only); reprocessing with new debug files; Seer/Autofix; Inbox ordering; Relay; issue priority model
- Rollbar: Item/Occurrence/Counter vocabulary; Active/Resolved/Muted/Merged transition names; RQL; Analyze/Improve modules; Terraform provider; path canonicalization rules
- BugSnag: Target/Critical stability targets; per-platform session definitions; grouping discriminator; grouping-algorithm update irreversibility; Fix with MCP; SmartBear Insight Hub positioning
- Datadog: FOR REVIEW/REVIEWED/RESOLVED/IGNORED/EXCLUDED state names; stated auto-resolution window; error.handling facet semantics; multi-source (RUM/Logs/APM) consolidation; Suspected Cause; EXCLUDED billing stop
- Airbrake: hotspots; aggregations; digest emails; rejected-errors quota behavior

## Rejected Findings

- **"Error tracking = release tracking"** — rejected as definitional. Release context is universal in the current sample but absent from the heritage generation (Airbrake's early form, Errbit) and from minimal deployments that never report releases. The Type is recognizable without it; it is L1.
- **"Error tracking requires source maps / symbolication"** — rejected; client-side and mobile implementation concerns (L2).
- **"Error tracking is a subset of APM"** — rejected. APM's processed entry holds error grouping as an L1 capability inside APM; the sampled pure-plays have no request-performance telemetry at all and remain squarely in-type. The Datadog case shows error tracking operating as a layer over multiple telemetry sources, not inside one.
- **"Grouping must be stack-trace-based"** — rejected as definitional. Grouping basis varies (in-project frame, error class, context, custom hash); the invariant is identity-based aggregation, not a specific algorithm.
- **"Issues are incidents"** — rejected. None of the sampled products declares issues as incidents or owns paging; alert routing hands off to downstream incident/on-call machinery.
- **"AI root-cause is part of the Type"** — rejected; L2 variant appearing across 2025–2026 products but structurally additive.

## Boundary Findings

1. **vs Bug Tracking System (§12, processed 2026-09-06)** — CONFIRMED keep-both. The bug record is born from a human's observed-vs-expected defect report and carries a fix/verify-shaped lifecycle; the error-tracking issue is born from a machine-captured runtime event and carries a triage-shaped lifecycle (resolve/ignore/mute + regression detection). The bridge is documented in both directions: error-tracking issues create linked tracker tickets (Rollbar/BugSnag/Airbrake integrations; Datadog work-item creation), and tracker tickets can resolve error issues via commit messages (Sentry/Rollbar). A dev-centric org may produce either object from one investigation — the objects remain distinct.
2. **vs Log Management (§14, processed 2026-09-08)** — CONFIRMED from this side, exactly as that pass predicted: error tracking centers exceptions **grouped/deduplicated into issues** with per-issue state and release context; log management centers the **raw ungrouped record stream** with time-anchored search as the primary interaction. Datadog Error Tracking for Logs is the sharpest natural experiment: the same log-error substrate, reorganized from a searchable record corpus into fingerprinted issues with a lifecycle. Keep-both; the seam is the unit of interaction (issue vs record), not the substrate.
3. **vs APM (§12, processed 2026-09-06)** — keep-both. APM centers request/operation performance telemetry (latency/error/throughput per operation) with per-service health views; its error grouping is one facet of service health. Error tracking centers the exception itself as the unit of record with an issue lifecycle; service health is a derived view. Datadog's Error Tracking sits above APM/RUM/Logs as a consolidating layer — consistent with both processed entries.
4. **vs Observability Platform (§14, processed 2026-09-09)** — keep-both. The observability platform's defining core is multi-signal ingestion + shared context + cross-signal investigation; error tracking is a single-signal specialist whose depth is the issue lifecycle. Suite-embedded error tracking (Datadog; Sentry's own suite breadth) is packaging, not identity.
5. **vs Incident Management (§14, processed 2026-09-08) / On-call Management (§14, processed 2026-09-09)** — consistent with both passes: error tracking is an **upstream alert source** (both passes list error-tracking tools as alert inputs). The error-tracking issue is not the incident record: most issues are worked asynchronously and never declared; the incident record, severity-driven mobilization, and paging live downstream.
6. **vs Metrics Monitoring (§14, processed 2026-09-08)** — keep-both. Numeric time series vs discrete exception events grouped into issues. Error-rate metrics are the documented bridge (error tracking → metrics), not an identity claim.
7. **vs Distributed Tracing (§14, processed 2026-09-08)** — keep-both. Spans vs exceptions; trace IDs attached to error events (Datadog issue panel links to traces) are the bridge.
8. **vs Static Code Analysis Platform (§12, processed 2026-09-09) / Code Quality Platform (§12, processed 2026-09-07)** — keep-both. Static examination of code that has not run vs runtime capture of errors that did occur. Code-quality state is platform-side quality over code; error-tracking state is runtime error issues over running software.
9. **vs Debugger (§12, processed 2026-09-07) / Profiler (§12, processed 2026-09-09)** — RATIFIES the debugger pass's remove-target: error tracking has no execution control (no launch/attach/pause) and no cost attribution; it is passive capture plus aggregation. The stack trace in an error event is a diagnostic artifact, not a stopped-state inspection.
10. **vs AIOps Platform (§14, processed 2026-09-06)** — keep-both. AIOps = automated machine analysis over operational signal streams producing correlated actionable output; error tracking's grouping is deterministic identity computation (fingerprint/hash) and its output is the issue itself. ML-assisted grouping exists (Rollbar "automation-grade grouping") as an implementation of the same identity function, not as AIOps-style cross-signal correlation.
11. **vs IT Problem Management (§14, processed 2026-09-08)** — DISCHARGES that pass's flag from this side: the software error object here is a **signal / code-fix unit** (an exception occurrence aggregated into a triaged issue, disposed by fixing code); the IT problem record is the **operational cause record** (suspected/confirmed underlying cause of incidents, disposed by workaround + change). The expected seam holds: dev-centric orgs may produce either object from one investigation, and the objects interlink (error issue → ticket → change), but the records, lifecycles, and dispositions differ. Keep-both.
12. **Mobile crash reporting** — held as a **variant pole within this Type**, not a separate directory leaf: the aggregation model (crash events → grouped issues → triage → release health) is identical; only the capture substrate (native crashes, symbolication) and the headline KPI (crash-free sessions) differ. No directory change.
13. **Historical / market-sample check (§24)** — passed. Errbit-class open-source self-hosted notifiers (capture exceptions via notifiers → group by backtrace → resolve/ignore states, no releases, no source maps, no AI) satisfy all four L0 legs. Pre-SaaS server error logs satisfy only capture (no grouping, no issue lifecycle) → log-management territory, confirming the seam. OS crash-dump reporting satisfies capture + diagnostic identity but has no aggregation service or lifecycle → crash-artifact analysis (debugger-adjacent), not this Type. Therefore L0 names no SaaS, release machinery, source maps, or AI.

## Uncertainties

- Datadog's grouping-correction surface (merge/split rules) was not fetched in depth; asserted only that fingerprinting is automatic and issues are managed — grouping-customization breadth is confirmed for Sentry/Rollbar/BugSnag only.
- Airbrake evidence is index-level; its lifecycle state names were not verified.
- Firebase Crashlytics unreachable; the mobile pole's KPI vocabulary (crash-free rates) is evidenced via Sentry/BugSnag/Rollbar instead. Crashlytics-specific behavior unverified.
- Exact auto-resolution windows, escalation algorithms, and archive conditions are vendor-specific parameters (documented above as L3); no universal values are claimed.
- The relative market weight of pure-play vs suite-embedded error tracking is not asserted — no market-size evidence was gathered.

## Final Synthesis

An **Error Tracking Platform** is the software team's runtime-error system of record. Its defining core is four jointly-held structures: **automatic capture of runtime errors from the running application** (machine-reported via embedded notifier/SDK, not human-filed); **the error's diagnostic identity** (type/message/stack trace + execution context) as both the record's content and its grouping basis; **aggregation of recurring raw events into distinct persistent issues** (fingerprint/hash-based, configurable, manually correctable); and **the issue's triage lifecycle to a recorded disposition** (open → resolved/ignored/muted with assignment, with recurrence after resolution surfaced as regression/reopen).

Around that core, mature products add a consistent layer: release/version attribution with resolve-in-release and regression detection, user-impact tracking, alerting and routing, issue-tracker and source-code integration, symbolication, environments/projects scoping, and health/stability views. Variants divide by surface (server / browser / mobile-crash), packaging (pure-play / suite-embedded / self-hosted), and AI posture. The Type's boundary is sharpest against bug tracking (human-filed defect vs machine-captured error), log management (issue vs raw record), and APM (exception-centric vs request-performance-centric); it is the upstream alert source for incident and on-call machinery.
