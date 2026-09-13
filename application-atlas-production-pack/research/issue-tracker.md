# Research Notes — Issue Tracker

Research date: 2026-09-08

## Research Goal

Understand what an Issue Tracker actually is as an Application Type — from real products' official documentation:

- what the unit record ("issue") is and what it minimally carries;
- how issues move through a lifecycle and who controls transitions;
- how the issue space is organized (container, types, labels, components);
- which surfaces users work in (list, board, detail, triage inbox, planning layer);
- how code connects to issues — and whether that connection is definitional or layered;
- where the boundaries run vs Bug Tracking System (joint-review flag to discharge), Ticketing System, Task Management, Agile PM, Engineering PM, Incident Management, Help Desk, Requirements Management, Code Review, Error Tracking, Source Code Hosting;
- whether a general-tracker definition survives the historical record (the term "issue tracking" was near-synonymous with bug tracking in the 2000s).

## Initial Boundary

Initial hypothesis (pre-research):

- Core purpose: track discrete work items ("issues") arising in a team's work on its product/project — bugs, features, tasks, ideas — each as an individually addressable record driven through a lifecycle to a done/closed disposition.
- Users: software teams — filers, assignees/developers, triagers/leads, PMs; sometimes external contributors via public trackers.
- Nearest types: Bug Tracking System (defect-centric pole; joint-review flag pending from that pass), Ticketing System (demand-processing machinery), Task Management (personal/team to-dos), Agile PM (backlog + cadence philosophy on top), Engineering PM (adds dev-artifact binding + delivery containers), Incident Management (adds mobilization), Help Desk (requester-serving), Requirements Management (adds traceability/baselines).
- Key unknowns: is the record grammar really uniform across issue kinds (the seam vs bug tracking)? Is code linkage definitional? Is the container (project/repo/team) definitional? Does the definition survive Trac-era products?

## Research Questions

1. What is the issue record? What is minimally required on it (Linear's docs state a minimal definition — verify against others)?
2. What lifecycle do issues move through? Are statuses product-managed? Is reopen normal?
3. How is the issue space organized — container (project/repo/team), classification (type/tracker/label/component), hierarchy (subtasks/epics)?
4. What relationships exist between issues (blocks, duplicates, relates, parent/child)?
5. What are the working surfaces (list, board, detail, triage inbox, planning views)?
6. How does discussion happen on the record, and is the record also the coordination conversation?
7. How does code connect (commit/PR references, auto-close, dev panels) — definitional or common structure?
8. What planning machinery sits on top (backlog, milestones, sprints/cycles, roadmaps) — definitional or layered?
9. Who uses it; what roles/permissions matter; how does intake work (forms, email, API, integrations)?
10. Where are the boundaries vs the eleven neighboring Types listed above?
11. What varies: standalone vs embedded, SaaS vs self-hosted, opinionated vs configurable, public vs private, software vs non-software teams?

## Representative Products

| Product | Why chosen | Posture | Evidence quality |
|---|---|---|---|
| Jira (Atlassian) | market-defining configurable work-item tracker; enterprise tier; the word "issue" in the Type name is partly this product's heritage | SaaS + Data Center, suite-embedded | Tier-1 (official guide article body fetched — stronger than the bug pass's TOC-level capture) |
| GitHub Issues | platform-native tracker inside a code-hosting platform; individual/OSS tier; boundary anchor for embedding | embedded in code-hosting platform | Tier-1 (official docs fetched first-hand) |
| Linear | modern opinionated software-team issue tracker; startup/scale-up tier; states the minimal record definition explicitly | SaaS | Tier-1 (official docs: hub + issues + workflows + triage) |
| Redmine | long-lived open-source standalone general tracker (2006+); self-hosted tier; "issue tracking" as the product's own name for its core | self-hosted open-source | Tier-1 (official wiki: UserGuide + RedmineIssues + IssueTrackingSetup) |
| Trac | historical check anchor (2004-era); ticket+wiki+timeline hybrid; minimal machinery | self-hosted open-source | Tier-1 (official TracTickets page fetched) |

Selection covers: market leader (Jira), code-native pole (GitHub), modern opinionated pole (Linear), classic standalone open-source (Redmine), historical minimal (Trac). Different product philosophies (configurable enterprise machinery vs opinionated speed-first vs platform-native vs classic generic) and different customer tiers (enterprise, OSS/individual, startup, self-hosted).

## Sources

- Jira — Atlassian official guide, "Jira work items overview" (article body): https://www.atlassian.com/software/jira/guides/issues/overview — incl. work-item definition, work types (Epic/Task/Story/Bug/Sub-task), hierarchy, fields/layout, parent-child, linked work items (blocks/clones/duplicates/relates). Guide TOC also confirms products/boards/workflows/JQL/permissions/automation/timeline/reports/integrations/agentic-engineering sections.
- GitHub — official docs, "About issues": https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues — incl. uses (bug reports, features, ideas), creation paths, sub-issues, dependencies, metadata (types/labels/milestones), `fixes:` auto-close, Projects layer, notifications, templates/forms, issues-vs-discussions boundary.
- Linear — official docs: hub https://linear.app/docs ; "Create issues" https://linear.app/docs/creating-issues ; "Issue status" https://linear.app/docs/configuring-workflows ; "Triage" https://linear.app/docs/triage — incl. minimal record definition, default workflow, status categories, duplicate system status, triage inbox/actions/automation, email/API/URL intake, recurring issues, importers ("move issues from your existing issue tracker into Linear").
- Redmine — official wiki: "User guide" https://www.redmine.org/projects/redmine/wiki/UserGuide ; "Issue Tracking" https://www.redmine.org/projects/redmine/wiki/RedmineIssues ; "Issue tracking system" (admin) https://www.redmine.org/projects/redmine/wiki/RedmineIssueTrackingSetup — incl. "Issues are the heart of the Redmine business", trackers (bug/feature/support), statuses + closed flag, per-role×tracker workflow, field permissions, relations (duplicates/blocks/precedes), watchers, associated revisions, subtasks.
- Trac — official wiki, "TracTickets": https://trac.edgewall.org/wiki/TracTickets — incl. "tickets can be used for project tasks, feature requests, bug reports and software support issues", full field list, default statuses (new/assigned/accepted/closed/reopened), resolutions (fixed/invalid/wontfix/duplicate/worksforme), custom fields, notifications, queries/reports, commit-ticket updater reference.

Fetch failures (recorded per source-access limitation rules):

- https://linear.app/docs/issues — 404 ×1; pivoted to /docs/creating-issues (successful).
- https://docs.github.com/en/issues/planning-and-tracking-with-issues — 404 ×1; pivoted to the known-good "About issues" page (successful).
- https://docs.github.com/en/issues/planning-and-tracking-with-issues/learning-about-issues/about-issues-on-github — 404 ×1 (guessed new path); abandoned after the pivot above succeeded.

## Product Observations

### Jira (Atlassian) — evidence layer A

From the official guide article "Jira work items overview" (body fetched):

- "In Jira, teams use work items (formerly known as *issues*) to track bugs and individual pieces of work that must be completed. Depending on how your team uses Jira, a work item could represent a project task, a helpdesk ticket, a leave request form, etc." — the record is a generic work item; bugs are one use.
- Work types out-of-the-box: **Epic** ("larger body of work… collection of multiple work items"), **Task** ("'catch-alls'"), **Story** ("requirement expressed from the perspective of the user"), **Bug** ("a problem that needs to be fixed"), **Sub-task** ("granular decomposition… can be created for all work types"). Admins can create/customize work types "to match any method of project management".
- Hierarchy: Epic → work items (task/story/bug) → sub-tasks; additional levels above epic in Premium editions.
- Anatomy: work item fields (assignee, due date, status, description, attachments); custom fields; configurable layout (description region, field tabs, context fields, more fields).
- Parent/child: any work type can be parent or child (except subtasks, child-only).
- Linked work items out-of-the-box: **blocks/is blocked by, clones/is cloned by, duplicates/is duplicated by, relates to** — "All linked work items will appear on each work item… showcase dependencies."
- Guide TOC (section existence): projects, boards, workflows, agentic engineering (AI agents in Jira), integrations, reports/dashboards, insights, permissions, JQL, navigation, automation, timeline (roadmaps), advanced planning, mobile, editions/hosting.
- Observation: Jira's own docs define the unit as a generic work item whose kind is a type; planning machinery (boards/sprints/roadmaps) and dev-tool integration are separate guide sections — i.e., layers around the record, not the record itself.

### GitHub Issues — evidence layer A

From official docs "About issues" (fetched first-hand):

- "You can create issues in your repository to plan, discuss, and track work. Issues are quick to create, flexible, and can be used in many ways. Issues can track bug reports, new features and ideas, and anything else you need to write down or discuss with your team."
- Creation paths: from a repository, while adding sub-issues, converting a comment, from a specific line of code, via URL query; web UI, GitHub Desktop, CLI, GraphQL/REST APIs, Mobile.
- Sub-issues: "break down larger pieces of work into smaller issues… multiple levels… full hierarchy of work."
- Dependencies: "blocking relationships… blocked by, or blocking, other work."
- Metadata: issue types (organization-level), labels, milestones.
- Code integration: "Mentioning an issue in another issue or pull request will create references between them and using keywords, like `fixes:`, in your pull requests will automatically close the associated issues."
- Projects: "strongly integrated with issues to plan and track the work for your team. All your issue metadata is available in your projects" — a separate planning layer (tables/boards/views).
- Staying up to date: subscribe to issues for notifications; personal dashboard of recently updated subscribed issues; assign "to make it clear who is working on an issue".
- Community management: issue forms and templates "to help contributors open meaningful issues"; report abuse/spam.
- Efficient communication: @mention collaborators; `#`-link related issues; saved replies.
- Issues vs Discussions: "Some conversations are more suitable for GitHub Discussions" (Q&A, announcements); an issue can be **converted to a discussion** — the product itself marks the boundary between tracked work and untracked conversation.
- Observation: the container is the repository; the record is generic; planning is a separate layer (Projects); code linkage is native and automatable; the issue/discussion conversion is direct evidence of the "tracked work vs conversation" seam.

### Linear — evidence layer A

From official docs (hub, creating-issues, configuring-workflows, triage):

- **Minimal record definition** (creating-issues): "Issues are always linked to a single team. They have an issue ID (team's issue identifier and unique number) and are required to have a title and a status—all other properties and relations are optional." — the cleanest vendor statement of the minimal issue: identity + title + status + container.
- Creation: keyboard-first (`C`), full-screen (`V`), templates, `linear.new` URLs with query-parameter pre-fill (title, description, status, team, priority, assignee, estimate, cycle, label, project, milestone, links, template), GraphQL API, email intake (team intake address, template addresses, **Linear Asks** for requester-facing workflows with synced replies), drafts (local + saved; 6-month expiry).
- Recurring issues: convert any issue to recurring with cadence; future issues created when due date passes.
- **Workflow** (configuring-workflows): "Issue statuses define the type and order of states that issues can move through from start to completion." Default set and order: **Backlog > Todo > In Progress > Done > Canceled**. Statuses are team-specific and customizable within fixed **status categories** (Backlog / Unstarted / Started / Completed / Canceled / Duplicate + optional Triage). Default status for new issues configurable. **Duplicate is a system-managed status** applied automatically when an issue is marked as a duplicate. Auto-close (close stale issues after a set period) and auto-archive (archived issues still searchable and restorable; creator notified).
- **Triage** (triage page): "a special inbox for your team. When an issue is created by integration or by a workspace member not belonging to your specific Linear team, it will appear here. Triage offers an opportunity to review, update, and prioritize issues before they are added to your team's workflow." Actions: **accept** (→ team's default status, optional comment), **mark as duplicate** (choose canonical issue; attachments and customer requests move to it; new issue → Canceled type), **decline** (→ Canceled, optional explanation), **snooze** (hidden until chosen time or new activity). Triage excluded from views by default ("outside the normal workflow"). Triage responsibility: rotating ownership of the inbox, optionally synced to PagerDuty/OpsGenie/Rootly/Incident.io schedules. Triage rules (condition→action: update team/status/assignee/label/project/priority). Triage Intelligence (LLM suggests assignee/label, surfaces likely related issues or duplicates). Support integrations: Intercom, Front, Zendesk, Slack; Asks for non-Linear requesters.
- Hub structure: Issues, Issue properties, Projects, Initiatives, Cycles, Views, Find and filter, Linear Asks, Integrations, Analytics, Administration, Importers. Importers page: "Quickly move issues from your existing issue tracker into Linear" — the market category "issue tracker" is the product's own vocabulary.
- Issue relations (hub): "Indicate blocked, blocking, related, and duplicate issues." Parent and sub-issues: "Break down larger tasks into smaller pieces of work."
- Observation: Linear is the opinionated pole — fixed status categories, triage as a first-class inbox, keyboard-first, minimal required fields. The record grammar is uniform; bug-ness is a label.

### Redmine — evidence layer A

From official wiki (UserGuide, RedmineIssues, RedmineIssueTrackingSetup):

- "Issues are the heart of the Redmine business. An issue is bound to a project, owned by a user, can be related to a version, etc." — container + ownership + version anchoring in one sentence.
- **Trackers**: "Trackers are how you split your issues into different types - common ones are Bug, Feature, Defect or etc." Defaults: **bug, feature, support**. Per tracker: name, default status, roadmap display flag, its own workflow, standard/custom field sets. — the type system on a uniform record.
- **Issue statuses**: "can be added and deleted freely. Each status has… **Issue closed**: indicates that the issue is considered as closed (more than one status can be declared as closed)." % Done per status (optional setting).
- **Workflow**: "status transitions that the various project members are allowed to make on the issues according to their type" — a role × tracker matrix of authorized transitions; status change requires 'Edit issues' permission; **field permissions per state** (read-only / required per role).
- Issue page: chronological messages (comments, quotable, editable), related issues, watchers (notified on update; admin-manageable), **associated revisions** (commit-message keywords configured by admin display the commit on the issue; manual association from the changeset view, reversible).
- Adding issues: gated by role permission (Issue tracking > Add issues); tracker field "defines the nature of the issue".
- **Relations**: related to; **duplicates/duplicated by** ("closing A will automatically close B"); **blocks/blocked by** ("A can't be closed unless B is"); **precedes/follows** (order with day offsets, rescheduling); copied from/to.
- **Subtasks**: parent/child; "Because it's just a normal task a subtask can also have subtasks. There is no limit in the depth"; cross-project subtasks configurable; parent properties computed from subtasks (done % weighted average, earliest start, latest due, summed spent/estimated time, highest priority).
- Project container (UserGuide TOC): project overview, activity, issue tracking (list, summary), roadmap (version overview), time tracking, Gantt, calendar, news, documents, files, forums, wikis, repository, project settings. — issues are the core; wiki/forums/gantt are bundled modules.
- Observation: Redmine is the classic standalone general tracker — the same uniform record (issue) with a type field (tracker), role-gated configurable workflow, rich relations, and repository linkage as a configured integration.

### Trac — evidence layer A (historical anchor)

From official wiki TracTickets (1.6 docs):

- "As the central project management element of Trac, tickets can be used for **project tasks**, **feature requests**, **bug reports** and **software support issues**, among others." — direct period evidence that the record is type-open and uniform.
- "Tickets can be edited, annotated, assigned, prioritized and discussed."
- Fields: Summary; Description (wiki-formatted); **Reporter**; **Type** (defaults: defect, enhancement, task); **Component** ("the project module or subsystem"); Version; Keywords; Priority (trivial→blocker); Severity (optional, hidden by default); **Milestone**; **Assigned to/Owner** ("Principal person responsible for handling the issue"); Cc; **Resolution** (fixed, invalid, wontfix, duplicate, worksforme); **Status** (default workflow: new, assigned, accepted, closed, reopened).
- Comments + change history below properties; comment editing policy; all edits update "last changed".
- TracLinks: "refer to other issues, changesets and files" — cross-object linking native.
- Custom fields; hidden fields; default values; assign-to restricted to authenticated users with TICKET_MODIFY; preset-value new-ticket URLs; cloning; deletion via optional component (TICKET_ADMIN); batch modify; ticket queries (TracQuery) and reports (TracReports); email notifications (TracNotification); workflow customization (TracWorkflow); roadmap/milestones (TracRoadmap); commit-ticket updater (TracRepositoryAdmin) — changesets referencing tickets.
- Environment bundles wiki + timeline + repository browser + tickets — the heritage hybrid shape.
- Observation: Trac satisfies the modern definition with zero current-era machinery — no boards, no AI, no auto-close keywords (commit updater is an optional component), numeric ticket IDs, one project per environment. The lifecycle (new → assigned/accepted → closed, reopened) and resolutions vocabulary are fully recognizable today.

## Cross-product Comparison

| Dimension | Jira | GitHub Issues | Linear | Redmine | Trac |
|---|---|---|---|---|---|
| Unit record | work item (formerly "issue") | issue | issue | issue | ticket |
| Record grammar | uniform; kind = work type (Epic/Task/Story/Bug/Sub-task, customizable) | uniform; kind = org issue type / label / use | uniform; kind = label; minimal required fields (title+status) | uniform; kind = tracker (bug/feature/support defaults) | uniform; kind = type (defect/enhancement/task defaults) |
| Container | project | repository | team | project | environment (= one project) |
| Identity | key + number | number (#N) | team prefix + number | id (+ per-project display) | ticket number |
| Lifecycle | workflow per type; transitions product-native | open/closed (+ reopen); duplicate marking | status categories Backlog/Unstarted/Started/Completed/Canceled/Duplicate (+Triage); default Backlog>Todo>In Progress>Done>Canceled | statuses freely definable; "issue closed" flag (multiple closed statuses allowed); per-role×tracker transitions | new/assigned/accepted/closed/reopened; workflow customizable |
| Dispositions/resolutions | resolution field (bug pass TOC evidence) | closed as completed/not planned; duplicate marking | Done / Canceled types; Duplicate system status; decline→Canceled | resolution on resolve; duplicates auto-close | fixed/invalid/wontfix/duplicate/worksforme |
| Ownership | assignee field | assignees | assignee property | "owned by a user" | Reporter + Assigned to/Owner |
| Triage | Triage Agent (AI) named in docs TOC; forms intake | templates/forms; AI triage named in bug pass | dedicated Triage inbox with accept/duplicate/decline/snooze + rules + Intelligence + responsibility rotation | role-gated status flow (new→confirmed→assigned…) | anonymous posting restricted by default |
| Hierarchy | epic → item → subtask (+ Premium levels above) | sub-issues (multi-level) | parent/sub-issues | subtasks (unlimited depth, cross-project configurable) | — (flat; relations instead) |
| Relations | blocks/blocked-by, clones, duplicates/duplicated-by, relates-to | dependencies (blocked-by/blocking), references, duplicate marking | blocked/blocking/related/duplicate | related, duplicates (auto-close), blocks, precedes/follows (rescheduling), copied from/to | TracLinks to issues/changesets/files; See Also-class refs |
| Conversation on record | comments; watch/share | comments, @mentions, saved replies, subscribe | comments + activity log | chronological notes, quotable | comments + change history |
| Code linkage | dev-tool integration section (smart commits, dev panel — bug pass TOC) | references; `fixes:` auto-close | GitHub automations (integrations) | associated revisions via configured commit keywords; manual association | commit-ticket updater (optional component) |
| Planning layer | boards, sprints, timeline/roadmaps, advanced planning | Projects (tables/boards/views) | projects, cycles, initiatives, milestones | roadmap, versions, Gantt, calendar | roadmap, milestones |
| Query/search | JQL, filters, dashboards | filtering/search; Projects views | views, find and filter | filters, issue list, summary | TracQuery, TracReports, search |
| Notifications | watchers | subscribe + notifications | notifications | watchers + notify flags | Cc + TracNotification |
| Intake | forms (public), CSV import, API | web, Desktop, CLI, APIs, Mobile, URL query, code line, comment conversion | keyboard, templates, email (incl. Asks), API, linear.new URLs, importers | web form (role-gated), email (via patches/plugins), API | web form (preset URLs), email |
| Time tracking | log time (bug pass TOC) | not native (Projects fields) | estimates (points/t-shirt) | time tracking module + per-issue spent time | — (plugin heritage) |
| Permissions | permissions guide section; security levels (bug pass) | repo access; org issue types | workspace/team roles; triage responsibility | role system gating per action; field permissions per state | TICKET_* permission system |
| Deployment | SaaS + Data Center | platform-native SaaS | SaaS | self-hosted open source | self-hosted open source |
| Bundled extras | full suite (JSW/JSWM, JSM sibling) | Projects, Discussions, Copilot | projects/initiatives, Asks, analytics | wiki, forums, files, documents, news, gantt, calendar | wiki, timeline, repository browser, roadmap |

## Abstraction Hierarchy

### Level 0 — Defining Invariant

Four jointly-held structures; removing any one makes the product no longer recognizable as an issue tracker:

1. **The issue of record** — a persistent, individually addressable record (own identity: number or key) of one discrete item of work or problem in the team's work on its product/project. The record grammar is **uniform**: the same fields, states, and lifecycle apply regardless of what kind of work the issue represents (bug, feature, task, improvement, idea); the kind is a classification on the record (type / tracker / label), not a different record model. Evidence: Trac ("tickets can be used for project tasks, feature requests, bug reports and software support issues"), Jira ("a work item could represent a project task, a helpdesk ticket, a leave request form"), GitHub ("track ideas, feedback, tasks, or bugs"), Redmine (trackers on one issue model), Linear (title+status required, all else optional). Remove → a pile of notes / a discussion thread.
2. **Work-shaped lifecycle to a recorded disposition** — states from open through worked to done/closed; transitions are product-managed state changes, not free-form edits; reopen is a normal supported operation. Evidence: all five products (Linear's fixed status categories; Trac's new/assigned/accepted/closed/reopened; Redmine's closed flag + transition matrix; Jira workflows; GitHub open/closed + reopen). Remove → discussion board / idea list.
3. **Ownership** — the record carries who raised it and who is responsible for it (reporter/author + assignee/owner); assignment is the mechanism that turns a raised item into tracked work. Evidence: Trac (Reporter + Assigned to/Owner), Redmine ("owned by a user"), Jira (assignee), GitHub (assignees), Linear (assignee). Remove → forum / anonymous suggestion box.
4. **Organized, queryable population** — issues accumulate as a population held in an organizing scheme — a container for the body of work (project / repository / team space) partitioned by classification (types, labels, components) — that can be listed, filtered, searched, and reported on. Evidence: Redmine ("bound to a project"), Linear ("always linked to a single team"), GitHub ("in your repository"), Jira (projects), Trac (components + queries/reports). Remove → disconnected records; a tracker you cannot ask "what's open, by area, by priority" of is not tracking.

Jointly-held is load-bearing: 1 alone = note list; 2 without 1 = stateless chat; 3 without 1/2 = people directory; 4 without 1/2/3 = empty container. The uniform-grammar property inside leg 1 is the seam vs Bug Tracking System; the work-item (not incoming-demand) character is the seam vs Ticketing System; the shared-container team-processing character is the seam vs personal task management.

Historical check (older / regional / platform-native): Trac (2004) satisfies all four legs with zero current-era machinery — no boards, no AI, no auto-close, no SaaS; Redmine (2006) likewise. The definition therefore must not require boards/sprints/cycles, AI, code linkage, estimates, or SaaS delivery. ✓ (See §24 check below.)

### Level 1 — Common Mature Structure

Very common in mature products, not required for recognition:

- **Classification layer**: types/trackers (bug/feature/task/story defaults, customizable), labels, components/areas; priority (and severity in bug-mode usage)
- **The record as conversation**: comments, @mentions, activity/change history, attachments
- **Watching/subscriptions + notifications** (email remains a first-class channel in the family's heritage)
- **Relationships**: parent/subtask hierarchy, blocks/blocked-by, relates-to, duplicates (with merge/auto-close semantics)
- **Saved filters/views**; the list view as primary working surface; board view; detail view
- **Planning layer on top of the record**: backlog, milestones/versions, sprints/cycles, roadmaps (packaging varies: Jira boards/sprints, GitHub Projects, Linear cycles/projects, Redmine roadmap/versions, Trac milestones/roadmap)
- **Code linkage**: commit/PR references, auto-close keywords, development panels (native in GitHub; integration-mediated in Jira/Linear; configured keywords in Redmine; optional component in Trac)
- **Configurable workflow**: statuses/transitions, per-role transition rights, field permissions per state
- **Intake variety**: web form, templates/forms, email, API, URL pre-fill, integrations (chat, support tools), importers
- **Search/query** over the population (query languages are L3)
- **Reports/dashboards/aggregates** over the population
- **Roles/permissions**; per-record visibility (private issues); public/community trackers
- **Automation rules** (condition→action)
- **AI assistance** (triage/routing/duplicate detection/drafting) — era-common in current products

### Level 2 — Variant / Optional Structure

- opinionated vs configurable philosophy (Linear's fixed categories + minimal fields vs Jira's fully customizable types/workflows/fields)
- standalone vs embedded packaging (standalone server; inside a code-hosting platform; inside a work-management suite)
- SaaS vs self-hosted
- public/community-facing tracker (open-source ecosystems: sign-up, templates, abuse reporting) vs purely internal
- requester-facing intake modes (Linear Asks with synced replies; Jira public forms; GitHub issue templates) — shades toward help-desk when requester-serving becomes the primary job
- time tracking, estimates/story points, % done
- wiki/forums/docs bundling (Trac/Redmine heritage hybrids)
- recurring issues; auto-close/auto-archive policies
- cross-team/cross-project issues and moves
- non-software teams running their work on issue-tracker machinery (Jira business teams; leave-request example in Jira's own docs)
- AI agents acting on issues (Jira agentic engineering; Linear Triage Intelligence; GitHub Copilot)

### Level 3 — Vendor-specific (Research Notes only)

- **Jira**: "work item" terminology rename (formerly issue); JQL; company-managed vs team-managed projects; default work types Epic/Task/Story/Bug/Sub-task; Premium hierarchy levels above epic; work-item layout regions; dev panel/smart commits; Triage Agent; agentic-engineering guide section; JSM as the service-desk sibling product.
- **Linear**: team as container with per-team issue ID prefix; fixed status categories with customizable statuses inside; Duplicate as system-managed status; Triage inbox + triage responsibility + rules + Triage Intelligence; Asks (requester-facing email intake with synced replies); auto-close/auto-archive; drafts with 6-month expiry; linear.new pre-fill URLs; recurring issues; estimates as t-shirt/points; importers; keyboard-first operation.
- **GitHub**: repository as container; organization-level issue types and custom fields; sub-issues; dependencies; Projects as a separate planning layer; `fixes:`-keyword auto-close; issue forms/templates; conversion of issues to Discussions; Copilot assistance; creation from code lines.
- **Redmine**: trackers with per-tracker workflow/fields/default-status/roadmap-flag; role × tracker transition matrix; per-state field permissions (read-only/required); % done (status-driven or manual); relations incl. precedes/follows with day-offset rescheduling; cross-project subtasks with computed parent properties; associated revisions via configured commit keywords; bundled wiki/forums/gantt/calendar/news/documents/files.
- **Trac**: trac.ini-configured workflow; components/versions/milestones as admin-managed enums; timeline view; wiki + repository browser bundling; TracLinks; commit-ticket updater as optional component; batch modify; preset-value new-ticket URLs; restrict_owner dropdown; ticket deletion as optional admin component.

## §24 Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the definition?

- **Trac (2004)**: fits all four L0 legs — tickets (uniform, type-open), lifecycle (new→closed, reopened), ownership (reporter/owner), organized queryable population (components, queries, reports) — with none of the modern machinery. ✓
- **Redmine (2006)**: fits; its own docs name the core "Issue tracking". ✓
- **Jira (2002, originally an issue tracker for software teams)**: fits; today's docs describe the same record with a renamed vocabulary ("work items"). ✓
- **Email-era trackers (GNATS lineage)**: those fit the *bug*-centric pole (sibling Type); the general-tracker sense is documented at least since the Trac/Jira/Redmine generation. The definition does not depend on any pre-2000 artifact. ✓
- **Platform-native (GitHub Issues)** and **suite-embedded (Jira)** and **opinionated SaaS (Linear)** and **self-hosted OSS (Redmine/Trac)** all fit without packaging-specific assumptions. ✓

Conclusion: the L0 is era-robust. Boards/sprints/cycles, AI, code auto-close, estimates, and SaaS delivery are all excluded from the defining core.

## Boundary Findings

1. **Bug Tracking System** (§12 sibling, processed 2026-09-06) — **JOINT REVIEW DISCHARGED from this side; verdict: keep-both as sibling Types.** The seam held by the bug pass (defect record with observed-vs-expected character + fix/verify-shaped lifecycle vs uniform work item + work-to-done lifecycle) is **confirmed from the general-tracker side with direct evidence**: in every sampled general tracker the bug is a *classification on a uniform record*, never the record itself — Jira: bug is one work type among Task/Story/Epic; GitHub: "issues can track bug reports, new features and ideas"; Redmine: bug is one tracker (with feature and support); Trac: defect is one ticket type (with enhancement and task); Linear: bug is a label. None of the five exposes defect-specific record semantics (reproducibility, verification-by-QA states) as the record model. Removal tests both directions: remove defect-specific semantics from a bug tracking system → it becomes an issue tracker; restrict an issue tracker to defect records with fix/verify semantics → it functions as a bug tracking system. Consolidation view (bug tracking as mere variant of issue tracking) **rejected**: the two record models differ in what the record asserts (a defect vs a unit of work) and in lifecycle shape (fix/verify vs work-to-done), and each pole has dedicated products that lack the other's semantics (Bugzilla/MantisBT vs the sampled general trackers). The market hosts both: suites configure bug tracking inside general trackers; standalone defect-centric products persist in OSS/self-hosted ecosystems.
2. **Ticketing System** (§07, processed 2026-09-08) — keep-both, consistent with that pass's own seam: ticketing systems process *incoming demands* (request/report/problem/alert) to a recorded disposition, requester identity optional; issue trackers hold the *team's own work items* (plan/execute + fix/verify-shaped work) anchored in a product/project container with code linkage as common structure. Naming overlap noted: Trac calls its issues "tickets" and Request Tracker (a ticketing system) calls its tickets "tickets" — the record name is not the discriminator; the subject and record shape are.
3. **Task Management Application** (§03.06, unprocessed) — seam held on: the issue is a team-processed work item in a shared product/project container whose population is managed (triage, backlog, assignment, lifecycle, reporting), canonically about development/product work; the task is a personal/team to-do organized for execution without the issue-population management character. Market blur acknowledged (Jira markets task management; task tools market issue tracking). **Flag recorded for joint review when task-management-application is processed.**
4. **Agile Project Management Application** (§03.07, processed 2026-09-06) — keep-both, consistent with that pass: agile PM's defining core is the planning philosophy (team-owned ordered backlog + board + bounded cadence with re-planning); the issue tracker is the record machinery underneath. Removal test: remove backlog/cadence machinery → still an issue tracker (Redmine without sprints, GitHub Issues without Projects, Trac). Remove the issue machinery → nothing remains.
5. **Engineering Project Management Platform** (§12, processed 2026-09-08) — keep-both, seam confirmed from this side: EPM's L0 adds the development-artifact binding (work items ↔ branches/commits/PRs) and the delivery container (releases/milestones/iterations) on top of work-item tracking; its own removal test reads "remove → generic issue tracker/task tool". This pass's L0 deliberately excludes code linkage (L1) and delivery containers (L1/L2), so the seam holds in both directions.
6. **Incident Management** (§14, processed 2026-09-08) — keep-both, consistent with that pass's removal test ("issue tracker with incident states"): incident management adds the standing mobilization structure (severity-driven routing, on-call schedules, escalation/paging) that issue trackers lack; an issue tracker holding incident-shaped issues is still an issue tracker.
7. **Help Desk** (§07, processed 2026-09-07) — keep-both: help desk is requester-serving (the record exists to deliver help back to the person who asked); the issue tracker's record exists to carry the team's work to done. Requester-facing intake modes in issue trackers (Asks, public forms) are L2 variants, not the primary job.
8. **Engineering Requirements Management** (§12, processed 2026-09-08) — keep-both, consistent with that pass's removal test ("flat ticket list, issue-tracker shape"): requirements management adds structured specification, typed traceability links with coverage, and baselines/managed change; the issue tracker holds a flat (hierarchy-bearing but not specification-structured) work-item population.
9. **Code Review Platform** (§12, processed 2026-09-07) — keep-both: the unit is a proposed code change with line-anchored review and a reviewer verdict; the issue tracker's unit is a work item. They meet at the fix boundary (PR references issues; auto-close on merge).
10. **Error Tracking Platform** (§12, unprocessed) — keep-both, consistent with the bug pass: error tracking auto-captures runtime errors as events; the issue tracker holds curated records humans act on. Auto-creation of issues from error platforms is an integration (Linear's Sentry integration is documented in its triage page), not a merge.
11. **Source Code Hosting Platform** (§12, unprocessed) — keep-both: GitHub Issues is embedded in a hosting platform whose core is repositories/version control; issues are one surface. Embedding is a packaging variant of the issue tracker, not evidence that hosting and tracking are one Type.

## Uncertainties

- Jira: the guide article body was fetched (stronger than the bug pass's TOC-level capture), but support.atlassian.com article bodies were still not fetched; no default workflow status names or default resolutions are asserted anywhere.
- Linear: docs captured at hub + three pages; numeric details stated by the docs themselves (draft expiry, email attachment limits) are recorded as L3 only and do not appear in the final document.
- GitHub: "About issues" fetched first-hand; labels/milestones/Projects pages not fetched individually — asserted only at the level the About page states.
- Redmine: wiki pages fetched; the role/permission system is asserted at wiki level (per-action permissions, field permissions) without enumerating every permission name.
- Trac: TracTickets fetched; TracWorkflow page not fetched — workflow customization is asserted from TracTickets' own reference and default status list.
- YouTrack and GitLab were not sampled this pass (the bug pass had YouTrack at positioning-only level); market context only, no claims rest on them.
- The exact historical boundary between "bug tracking" and "issue tracking" vocabulary in the early 2000s (when the general sense stabilized) is not precisely dated from fetched sources; the claim is limited to "documented at least since the Trac/Jira/Redmine generation".

## Final Synthesis

An Issue Tracker is the software team's system of record for its work items. Its defining structure is small: the issue (a persistent, individually addressable record of one discrete item of work or problem, with a uniform record grammar under which bug/feature/task/idea are classifications, not different record models), a work-shaped lifecycle carrying each issue from open through worked to a recorded done/closed disposition with reopen as a normal operation, ownership (who raised it, who is responsible), and an organized queryable population held in a container for the body of work (project/repository/team) and partitioned by classification. Around that core, mature products add the classification layer, the record-as-conversation, watching/notifications, relationships (hierarchy, blocks, duplicates), saved views and boards, a planning layer (backlog/milestones/cycles/roadmaps), code linkage, configurable workflows with role-gated transitions, varied intake (forms/email/API/integrations), search, reports, permissions, automation, and AI assistance. The market realizes one Type in several poles — configurable suite machinery (Jira), platform-native embedding (GitHub Issues), opinionated modern SaaS (Linear), classic standalone open-source (Redmine), and the minimal heritage hybrid (Trac) — and the definition survives all of them plus the historical record. The sharpest boundary is with the Bug Tracking System (discharged joint review: keep-both, seam = uniform record grammar + work-shaped lifecycle vs defect record + fix/verify lifecycle), with the Ticketing System (incoming demands vs the team's own work items), and with the planning-oriented siblings (Agile PM, Engineering PM) whose defining machinery sits on top of, not inside, the issue record.
