# Research Notes — Bug Tracking System

Research date: 2026-09-06

## Research Goal

Understand what a Bug Tracking System actually is as an Application Type — from real products' official documentation:

- what the core record is (the "bug") and what it carries;
- how defects move through their lifecycle (triage → assignment → fix → verification → closure, reopening);
- who the actors are and how responsibility and permissions work;
- which surfaces users face (report form, list/query, defect detail, reports);
- how this Type differs from Issue Tracker, Error Tracking Platform, Help Desk/Ticketing, Test Management, and Engineering Project Management;
- whether a defect-centric definition survives the modern market, where most products are general issue/work-item trackers.

## Initial Boundary

Initial hypothesis (pre-research):

- Core purpose: record defects in a software product and drive each one to a verified fix.
- Users: QA/testers, developers, triagers/component owners, PMs; sometimes external reporters (open-source communities, customers).
- Nearest types: Issue Tracker (bug = one issue type among many), Error Tracking Platform (automatic runtime error capture), Help Desk/Ticketing (service requests), Software Test Management (planned test execution), Code Review Platform (code changes).
- Key unknown: is "Bug Tracking System" still a distinct Type, or has the market merged it into Issue Tracking? Both leaves exist separately in the directory.

## Research Questions

1. What is the defect record? Which fields does it carry (observed/expected, repro steps, version, severity/priority, environment)?
2. What is the defect lifecycle? Which states, transitions, resolutions, and reopen behavior do products implement?
3. How does triage work (severity/priority, confirmation, deduplication, routing)?
4. How is the defect space organized (product/component/version, project, labels)?
5. How is a fix connected back to the record (verification, fix version, commit/PR links)?
6. What query/report surfaces exist (search, saved searches, reports, charts, dashboards)?
7. What roles/permissions matter (reporter, assignee, QA, admin; private defects; public reporting)?
8. Where are the boundaries vs neighboring Types?
9. What varies: standalone vs embedded, self-hosted vs SaaS, defect-only vs mixed work items, public vs private defect reporting?

## Representative Products

| Product | Why chosen | Posture | Evidence quality |
|---|---|---|---|
| Bugzilla (Mozilla) | canonical pure bug tracker, long-lived, self-describes defect-centric model | self-hosted open-source; also used as a public community tracker (bugzilla.mozilla.org) | Tier-1 (BMO official docs, fetched) |
| MantisBT | lightweight pure bug tracker, self-described "web based bug tracking system" | self-hosted open-source, maintained since 2000 | Tier-1 (official Admin Guide, fetched in full) |
| Jira (Atlassian) | dominant commercial product; issue/work-item tracker where bug tracking is a first-class use | SaaS + DC, suite-embedded | Tier-1 support docs (hub + TOC structure); article bodies not fetched |
| GitHub Issues | platform-native issue tracker; bug tracking is one use among several; modern boundary anchor | embedded in code-hosting platform | Tier-1 (official docs, fetched) |
| YouTrack (JetBrains) | modern commercial tracker frequently used for bug tracking | SaaS + self-hosted | Positioning-only (product page thin; help paths unreachable) — no operational claims |

GitHub Issues and Jira double as boundary anchors for the Issue Tracker boundary.

## Sources

- MantisBT Admin Guide (official, full): https://mantisbt.org/docs/master/en-US/Admin_Guide/html-desktop/ — incl. §1.1 What is MantisBT, §3.9 Authorization and Access Levels, §4.1 Issue Creation, §4.2 Issue Statuses, §4.3 Workflow, §5.31 Custom Fields, §5.44 Issues visibility, §6.3 View Issues page, §6.4 View Issue Details page, §10 Project Management; plus documentation index https://mantisbt.org/documentation.php
- Bugzilla (BMO) official documentation: https://bmo.readthedocs.io/en/latest/using/understanding.html (2.3 Understanding a Bug — full field list + Flags), https://bmo.readthedocs.io/en/latest/using/editing.html (2.4 Editing a Bug — attachments, flags, time tracking, Life Cycle of a Bug), https://bmo.readthedocs.io/en/latest/using/index.html (User Guide TOC — finding bugs, reports and charts, saved searches)
- Jira Cloud support documentation: https://support.atlassian.com/jira-software-cloud/ and https://support.atlassian.com/jira-software-cloud/resources/ (nav/TOC evidence: "What is a work item?", "Transition work items through a workflow", "What are Jira workflows?", fix versions/components/versions pages, dev-tool integration pages, dashboards, public forms, AI Triage Agent)
- GitHub Issues docs: https://docs.github.com/en/issues and https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues (full text)
- YouTrack product page: https://www.jetbrains.com/youtrack/ (positioning only)

Fetch failures (recorded per source-access limitation rules):

- bugzilla.mozilla.org/page.cgi?id=lifecycle.html — internal error (template missing) ×1; pivoted to bmo.readthedocs.io (successful).
- bugzilla.org/docs/4.4/en/html/using/understanding.html — 404 ×1; pivoted to BMO readthedocs (successful).
- atlassian.com/software/jira/guides/bug-tracking/what-is-bug-tracking — 404 ×1; atlassian.com/agile/software-development/bug-tracking — fetched but body was navigation chrome only ×1; pivoted to support.atlassian.com (successful at hub/TOC level).
- jetbrains.com/help/youtrack/server/Issue.html and /issue.html — 404 ×2; YouTrack operational docs unreachable. YouTrack treated as positioning-level only; no operational claims.

## Product Observations

### Bugzilla (Mozilla) — evidence layer A

From "Understanding a Bug" and "Editing a Bug" (BMO official docs):

- The bug record ("the core of Bugzilla is the screen which displays a particular bug") carries:
  - Summary (one-sentence problem statement, shown next to the bug number)
  - Status and Resolution — "define exactly what state the bug is in — from not even being confirmed as a bug, through to being fixed and the fix confirmed by Quality Assurance"
  - Product and Component ("Bugs are divided up by Product and Component")
  - Version (affected released versions); Target Milestone (future version by which to fix)
  - Hardware (Platform and OS) — environment where the bug was found
  - Importance = Priority (P1–P5; set by assignee or someone with authority over their time such as a project manager) + Severity (blocker → trivial; also used to mark enhancement requests)
  - Assigned To ("the person responsible for fixing the bug"); optional QA Contact ("responsible for quality assurance on this bug")
  - Opened (reporter + timestamp); Updated; CC List (people who get mail when the bug changes)
  - Dependencies (Depends On / Blocks, with a dependency-tree view); See Also (related bugs in other Bugzillas or other bug trackers)
  - Keywords (admin-defined, e.g. crash, regression); Personal Tags (private to the author); Alias (short unique name); Whiteboard; URL
  - Flags — per-installation definable statuses on bugs or attachments with values ?/−/+/unset; requestable flags route a request to a named requestee (e.g. attachment `review` flag used to request code review; `blocking2.0` example for release decisions)
  - Time Tracking (group-gated: Orig. Est., Current Est., Hours Worked, Hours Left, %Complete, Gain, Deadline)
  - Attachments (patches, screenshots, test cases, logs; content-type; can attach by URL); Additional Comments
- Lifecycle: "The life cycle of a bug, also known as workflow, is customizable to match the needs of your organization." Default workflow is diagrammed; the docs confirm RESOLVED and VERIFIED are distinct statuses (time-left resets on RESOLVED and again on VERIFIED) and that status ranges from "not even being confirmed as a bug" through "fix confirmed by Quality Assurance".
- Search/report surfaces: Quicksearch, Simple Search, Advanced Search, Custom Search, Bug Lists; Reports and Charts; Saved Searches live in user preferences; email notification ("bugmail") preferences per user; API keys for programmatic access.
- User guide includes "Filing a Bug" (reporting a new bug; cloning an existing bug) — report intake is a first-class surface.
- Attachments used for code review requests → partial overlap surface with Code Review Platform, but the unit remains the bug.

### MantisBT — evidence layer A

From the official Admin Guide (self-description: "a web based bug tracking system… one of the most popular open source bug/issue tracking systems"):

- Issue creation channels (§4.1): web interface (user logs in and reports), SOAP API ("the nightly build script can automatically report an issue if the build fails"), email (via patches/plugins), other injections.
- Statuses (§4.2): "MantisBT assumes that an issue can be in one of three stages: opened, resolved and closed" — customized status lists map onto these stages. Out-of-box statuses: new, feedback, acknowledged, confirmed, assigned, resolved, closed.
  - new → landing status; acknowledged (team agrees with report, not yet reproduced) → confirmed ("confirmed and reproduced") → assigned ("assigned to one of the team members and actively working") → resolved (with resolutions: fixed, duplicate, won't fix, no change required, etc.) → closed ("no further actions"; typically hidden from the View Issues page; some teams use closed for reporter sign-off, others for released-to-customers). Resolved can go back to feedback (reopen). feedback = "issue requires more information from reporter".
- Workflow (§4.3): administrators define valid next statuses per status, default next status, minimum access level required to trigger each transition, default status for new issues, and the status at which an issue counts as resolved. "By default, there is no workflow defined" (all transitions open) — workflow is a configurable overlay on the state machine.
- Access levels (§3.9): VIEWER, REPORTER, UPDATER, DEVELOPER, MANAGER, ADMINISTRATOR (numeric enum, customizable); per-action thresholds (report, update, note, close, delete…); project-specific overrides; private projects; public/private view status per issue; "limited view" configuration.
- Report form (config option $g_bug_report_page_fields): summary and description always; optional: additional_info, attachments, category_id, due_date, eta, handler, monitors, os, os_build, platform, priority, product_build, product_version, reproducibility, resolution, severity, status, steps_to_reproduce, tags, target_version, view_state. Severity scale: block, crash, major, minor, tweak, text, trivial, feature (feature = requesting new feature → MantisBT handles feature requests too, confirming mixed-record usage).
- View Issues page (§6.3): filterable/sortable list (priority, id, note count, category, severity, status, updated, summary); color-coded by status; simple keyword search across summary/description/steps/additional info/ids; sticky issues; CSV/Excel export; print reports (permission-gated).
- Issue detail page (§6.4) actions: Edit, Assign to, Change Status to, Monitor/End Monitoring (email notifications), Stick/Unstick, Clone (prefilled report, optional relationship), Reopen Issue ("re-open a resolved or closed issue… automatically put into Feedback status"), Close (config: may require resolve-first or not), Move Issue (to another project), Delete Issue (discouraged — "resolve the issue with an appropriate Resolution code" instead).
- Relationships: related to, parent/child (warned when resolving parent before children), duplicate of/has duplicate (generally resolved with duplicate resolution).
- Other: bugnotes (comments), bug history (audit), custom fields (per-project, incl. "required on report"), relationship graphs, sponsorship (funding an issue), reminders, changelog and roadmap generated per project (§10), summary page (aggregates), time tracking, sub-projects, email notifications with fine-grained notify flags, REST/SOAP APIs, user signup (for community/open-source installs, default access REPORTER), anonymous account mode.
- The MantisBT team's own bug tracker "is reserved for reporting issues with the software" — dogfooding pattern.

### Jira (Atlassian) — evidence layer A− (nav/TOC-level; article bodies not fetched)

From official support docs structure:

- Unit of work is the "work item" (recently renamed from "issue"); work items have types ("work types", renamed from issue types) — "How do work types differ based on space type?", "Change the work type for multiple work items".
- Workflows: "What are Jira workflows?", "Transition work items through a workflow", simplified workflow option — transitions are product-native concepts.
- Versioning fields: "Edit fix versions of a work item" (fix versions as a first-class field), "What is a version?", release pages; components ("What are Jira components?", "Link work items to Jira components"); epics, subtasks/child work items; sprints/boards (planning machinery).
- Dev integration: smart commits, "Reference work items in your development work", "View development information for a work item" (branches/commits/PRs/deploys), link repositories.
- Watch/notifications: "Watch, share and comment"; activity types page (history/audit); attachments; cloning; linking; flagging; archiving; security levels per work item; due dates; priority editing.
- Query/report: dashboards + gadgets, filters/quick filters, saved filters, list view, reports (burndown/control/velocity — project-management flavored), charts from work-item data.
- Intake: forms ("How secure are public forms?") — external/public intake is a supported pattern; CSV importer; "Automatically assign work items to people".
- AI: "Jira Triage Agent to categorize and route work items", AI coding agents opening work items — triage as a first-class concept.
- Observation: Jira's documentation treats bug tracking as one use of a general work-item system; there is no defect-exclusive record model in the docs structure. Bug-specific semantics (fix versions, verification workflow) exist as standard configurations of the generic machinery. (Layer B inference, Jira+GitHub.)

### GitHub Issues — evidence layer A (boundary anchor)

From official docs ("About issues"):

- "You can use GitHub Issues to track ideas, feedback, tasks, or bugs" — bugs are explicitly one use; the record type is generic.
- Metadata: issue types (org-level), labels, milestones; custom issue fields (org-level structured metadata); sub-issues (hierarchy); dependencies (blocked-by/blocking).
- Lifecycle: open/closed; "You can close an issue when bugs are fixed, feedback is acted on, or to show that work is not planned"; reopening implied (close/re-open of Projects mirrors it); duplicate marking ("Mark an issue or pull request as a duplicate to track similar issues… together").
- Code integration: mentioning an issue in another issue/PR creates references; "using keywords, like `fixes:`, in your pull requests will automatically close the associated issues" — fix linkage is native and automatable.
- Intake: issue forms and issue templates "to help contributors open meaningful issues"; creation from code line, URL query, CLI/API/mobile.
- Triage: "Triaging an issue with AI — determine whether the issue is actionable or needs more information."
- Projects: separate planning layer (tables/boards/roadmaps, custom fields) built on top of issues.
- Observation: no severity/verification semantics in the core record; bug-ness is a label/type. Confirms the modern "generic tracker" pole.

### YouTrack — positioning-level only

Product page fetched: title "Project management for all your teams", "Try free". Operational help unreachable (2× 404 on guessed paths; root help page returned title only). No operational claims made for YouTrack. Market context: JetBrains positions YouTrack as a tracker/agile tool; commonly used for bug tracking — recorded as unverified market context, not evidence.

## Cross-product Comparison

| Dimension | Bugzilla | MantisBT | Jira | GitHub Issues |
|---|---|---|---|---|
| Defect as primary record | Yes — bug is the record | Yes — issue (bug-centric; feature via severity) | No — work item with types; bug = one type | No — issue; bug = one use/label |
| Observed-vs-expected character | Status "from not confirmed… to fixed and confirmed by QA"; severity incl. enhancement | statuses include confirmed/reproduced; reproducibility + steps_to_reproduce fields | via bug workflow + fields (not doc-verified in detail) | via templates/forms (bug reports) |
| Lifecycle states | Status + Resolution; customizable workflow; UNCONFIRMED→…→RESOLVED→VERIFIED (distinct VERIFIED confirmed) | opened/resolved/closed stages; new/feedback/acknowledged/confirmed/assigned/resolved/closed; reopen → feedback | workflow per type; transitions configurable | open/closed (+ reopen via UI/API) |
| Resolutions | Resolution field (per docs context) | fixed, duplicate, won't fix, no change required, customizable | resolution field (not doc-verified here) | closed as completed/not planned; duplicate marking |
| Reporter / Assignee | Opened (reporter); Assigned To; QA Contact | reporter; handler/assignee; monitor list | assignee; reporter | author; assignees |
| Severity/Priority | Severity (blocker→trivial) + Priority (P1–P5) | severity (block/crash/…/feature) + priority | priority field (work-type dependent) | labels / custom fields (no native severity) |
| Version/Environment | Version affected; Target Milestone; Platform/OS | product_version, product_build, target_version, os/platform | affects/fix versions; environment (work-type dependent) | milestones (planning-ish); custom fields |
| Organization of defect space | Product → Component | Project (+ sub-projects) → Category | space/project → components | repository (+ org issue types) |
| Duplicate handling | resolution duplicate + See Also | duplicate of/has duplicate relationship + duplicate resolution | issue links (doc: "Link work items") | duplicate marking |
| Dependencies | Depends On / Blocks + dependency tree | related to / parent-child / duplicate | issue links, child items | dependencies (blocked/blocking), sub-issues |
| Comments / attachments | Additional Comments; attachments (patches/screenshots/logs) | bugnotes; attachments | comments; attachments | comments; attachments |
| Notifications | CC list + bugmail + per-user email prefs | monitor + notify flags; reminders | watchers; notifications | subscribe; notifications |
| Query/report | Quicksearch/Simple/Advanced/Custom; bug lists; saved searches; Reports and Charts | View Issues filters; saved filters; summary page; graphs; CSV/print | filters, quick filters, dashboards, reports | filtering/search; saved views (Projects); insights |
| Audit/history | bug change activity (email-based) | Bug History config | activity/history page | timeline/events |
| Code/fix linkage | attachments as patches + review flags; See Also | (via integrations/plugins) | smart commits, dev panel, PR references | `fixes:` auto-close, PR references, branch creation |
| Public/community intake | signup, public trackers (BMO pattern) | signup → REPORTER; anonymous mode | public forms | issue templates/forms; public repos |
| Time tracking | group-gated per-bug | config-gated per-issue | log time | not native (Projects custom fields) |
| AI assistance | — | — | Triage Agent | AI triage, Copilot |
| Deployment | self-hosted open-source | self-hosted open-source | SaaS/Data Center | SaaS (platform-native) |

## Abstraction Hierarchy

### Level 0 — Defining Invariant

Minimal structure; removing any part makes the product no longer recognizable as bug tracking:

1. **Defect record** — a persistent, individually addressable record (with its own identity/number) representing a defect in a software product: something observed to be wrong relative to expected behavior. The observed-vs-expected character is what makes the record a defect rather than a generic task.
2. **State-driven lifecycle toward resolution** — the record advances through states driven by work on it (received → worked → resolved → closed), with at least a notion of "resolved/closed" distinct from "open". Reopening a resolved record is standard behavior in every researched product but a minimal system could lack it — L1-leaning, kept adjacent to L0 as near-invariant.
3. **Responsibility** — the record carries who reported it and who is responsible for it (reporter / assignee). Without responsibility, it is a discussion board, not tracking.
4. **Queryable registry** — defects accumulate as a population that can be listed, filtered/searched, and reported on. Without this it is a queue of disconnected conversations.

Evidence: all four present in Bugzilla, MantisBT (A); present in Jira's bug workflow and GitHub Issues' bug usage (A for the generic machinery; B for bug-mode application). Canonical inference (C): the defect record with fix/verify-shaped lifecycle is the distinguishing center.

Historical check: GNATS-era and Bugzilla (1998), Trac, MantisBT (2000) fit without any modern machinery (boards, AI, integrations). GitHub Issues fits when used for bugs (defect-ness carried by labels/types — the definition must not require defect-exclusivity). Jira fits when configured with bug work types. Older/regional/platform-native samples all survive. ✓

### Level 1 — Common Mature Structure

Very common in mature products, not required for recognition:

- classification of defects: severity scale + priority (native fields in Bugzilla/MantisBT/Jira; label/field-based in GitHub)
- version and environment anchoring: affected version, fix/target version, platform/OS/build
- defect-space organization: product/component (Bugzilla), project/category (MantisBT), components (Jira), repository + labels (GitHub)
- comments (notes) and attachments (screenshots, logs, patches/test cases)
- watching/monitoring + email or in-product notifications; CC lists
- duplicate detection/handling (duplicate resolution/marking + linking)
- relationships: depends-on/blocks, parent/child, related
- saved searches/filters and reusable queries; list view as the primary surface
- reports/charts/aggregations over the defect population (open-by-severity, trend, summary)
- change history/audit trail per record
- configurable workflow (statuses/transitions/permissions per transition)
- intake aids: report templates/forms, prefilled cloning, public signup or forms for external reporters
- linkage between the fix and the record (commit/PR references; auto-close on merge in modern code-adjacent products)
- access levels/roles: at minimum reporter vs updater/developer vs manager/admin; private vs public defects

### Level 2 — Variant / Optional Structure

- time tracking per defect (group/permission-gated in Bugzilla/MantisBT; native in Jira; absent in GitHub)
- QA-specific roles/fields (QA Contact; verification status as separate state)
- code-review-style flags/request machinery on the defect (Bugzilla flags; Jira approvals)
- sponsorship/bounty of issues (MantisBT)
- changelog/roadmap generated from resolved issues (MantisBT §10)
- mixed-record usage: feature requests tracked alongside bugs (MantisBT severity "feature"; GitHub/Jira inherently)
- AI triage/routing agents (Jira Triage Agent; GitHub AI triage) — emerging
- email-driven operation (report by email, notifications as primary interaction — heritage pattern, still configured)
- public/community-facing tracker as a product surface (open-source ecosystems) vs purely internal
- standalone vs embedded: in code-hosting platform (GitHub) vs in work-management suite (Jira) vs standalone self-hosted (Bugzilla/MantisBT)

### Level 3 — Vendor-specific (Research Notes only)

- Bugzilla: flags (+/−/?/unset, requestable with requestee, "asking the wind"), attachment flags, dependency-tree view, alias, whiteboard, personal tags, group-gated time tracking fields (Gain, %Complete), See Also across installations, bugmail, quips.
- MantisBT: numeric access-level enum with per-action thresholds, sticky issues, ETA field, reminders, My View page, sponsorship machinery, custom functions/enums strings, anonymous account mode, relationship graphs.
- Jira: work-item/work-type terminology rename, JQL, company-managed vs team-managed spaces, smart commits, Development panel, Triage Agent/Coding Agent, dashboard gadgets, Atlassian ecosystem (Bitbucket/Confluence/JSW links).
- GitHub: `fixes:`-keyword auto-close, Projects as a separate planning layer, issue forms/templates, org-level issue types/fields, Copilot triage, slash commands.

## Boundary Findings

1. **Issue Tracker** (directory sibling, §12) — the most important boundary. Modern market: dominant products (Jira, YouTrack, GitHub Issues, GitLab) are general work-item trackers in which bug tracking is a configured use. Pure bug trackers (Bugzilla, MantisBT) keep the defect as the primary record with defect-specific semantics (severity scale, reproducibility, confirmation, verification-by-QA). Sharpest seam: **the record model and its lifecycle semantics** — defect records whose state machine is shaped by observed-vs-expected, fix, and verification (with reopen on failed verification) vs uniform work items whose state machine is shaped by planning/execution. Remove defect-specific semantics (verification, severity/repro) and the product becomes an Issue Tracker; restrict an Issue Tracker to defect records and it functions as a Bug Tracking System. The two Types share most surfaces; joint review with the Issue Tracker leaf is warranted (flagged in STATUS).
2. **Error Tracking Platform** (§12) — automatically captures runtime errors/exceptions/crashes from deployed software and aggregates them as events; a Bug Tracking System holds manually curated defect records driven through a human lifecycle. Detection vs adjudication: error tracking produces candidate signals; bug tracking owns the authoritative defect record and its fix/verify loop. Auto-creation of tracker records from error platforms is an integration, not a merge.
3. **Help Desk / Ticketing System / ITSM** (§07/§14) — tickets are user-reported service requests about the requester's situation, lifecycle shaped by SLA/fulfillment; bugs are reports about the product's incorrect behavior, lifecycle shaped by fix/verify. Incident→problem→known-error ITSM processes resemble bug triage but target service restoration, not code correction.
4. **Software Test Management** (§12) — test management executes planned verification (cases, runs, results); bug tracking manages the defects those results reveal. A failed test run feeds a defect record; verification of the fix returns to the test surface.
5. **Engineering/Agile Project Management** (§12) — boards, sprints, roadmaps, estimation organize planned work; defect tracking feeds fixes into that planning (via fix versions/milestones). In suite products the boundary blurs inside one tool, but planning machinery is not part of the defect model (pure trackers demonstrate: changelog/roadmap is a thin byproduct).
6. **Code Review Platform** (§12) — unit is a code change, not a defect. Overlap exists at the fix boundary (Bugzilla review flags on patch attachments; PR references), but the authoritative record remains the defect, not the patch.

## Uncertainties

- Jira article bodies were not fetched (nav/TOC-level evidence only). Jira-specific field/workflow details (default bug workflow statuses, default work types) are NOT asserted from memory; the document relies only on the documented existence of work types, workflows, fix versions, components.
- YouTrack operational documentation unreachable — YouTrack contributes positioning context only.
- GitHub Issues' severity/verification behavior inferred from its generic model (labels/custom fields) — asserted weakly.
- Exact default status names for Bugzilla's *default* workflow (UNCONFIRMED/CONFIRMED/IN_PROGRESS/RESOLVED/VERIFIED/CLOSED) are not asserted from the fetched docs; the docs confirm customization, distinct RESOLVED/VERIFIED, and an "unconfirmed" starting notion. Precise default state lists stay out of the final document.
- MantisBT evidence is the deepest (full admin guide); cross-product generalizations were calibrated to avoid over-weighting MantisBT's particular status vocabulary.

## Final Synthesis

A Bug Tracking System is the software team's system of record for defects. Its defining structure is small: defect records (observed-vs-expected character, individually addressable), a state-driven lifecycle that carries each defect to resolution and closure (with verification and reopening as standard), responsibility (reporter/assignee), and a queryable population registry. Around that core, mature products add classification (severity/priority), version/environment anchoring, defect-space organization, comments/attachments, watching/notifications, duplicate and dependency handling, saved searches, reports, configurable workflows, audit history, and controlled intake (including public reporting). The market's dominant posture today embeds this defect model inside general issue/work-item trackers; standalone pure trackers persist (especially in open-source ecosystems and self-hosted estates). The Type remains definable and distinct: its record model and lifecycle semantics are fix/verify-shaped, not plan/execute-shaped, and that is what separates it from Issue Tracking, Error Tracking, Help Desk, Test Management, and Project Management.
