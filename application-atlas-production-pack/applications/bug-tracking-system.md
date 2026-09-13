# Bug Tracking System

## Overview

A **Bug Tracking System** is a software team's system of record for defects. It stores individually addressable reports of things that are wrong in a software product — behavior that was observed but not expected — and carries each report through a lifecycle that ends in a resolution and closure. Around that core it keeps the accumulated defect population searchable, organized, prioritized, and reportable, so that a team can decide what to fix, who is fixing it, whether the fix actually worked, and what remains broken.

The defining core is small:

```text
Defect record (observed vs expected behavior in a software product)
└── Responsibility (who reported it, who is responsible for it)
    └── Lifecycle states (received → triaged/assigned → resolved → closed)
        └── Persistent, queryable registry of defects
```

Everything else commonly associated with these products — severity and priority scales, affected/fixed versions, environment fields, comments and attachments, watching and notifications, duplicate handling, saved searches, reports, configurable workflows — is standard machinery that makes the core practical, but older and minimal products have functioned without much of it.

The defining core is deliberately about **defects**, not about work in general. When the record model expands to tasks, features, epics, and roadmaps — with bugs as just one category — the product is drifting toward a different Application Type (Issue Tracker, Engineering Project Management). When defect reports are captured automatically from running software rather than curated by people, that is the Error Tracking boundary.

## Users & Context

The primary users are the members of a team that builds or maintains software:

- **Reporter / tester / QA** — observes wrong behavior while testing or using the product, files a defect report with enough context for someone else to observe the same thing, and later confirms that a fix actually works.
- **Developer / assignee** — picks up defects assigned to them, diagnoses the cause, fixes it, and moves the record to resolved with a note of what was done.
- **Triager / component owner** — a person (or role) who receives incoming reports, decides whether each is a real defect, rejects or merges duplicates, sets its importance and routing, and assigns it.
- **Product/project manager** — looks across the defect population: what is open, what is severe, what is scheduled into the next release, what is trending badly.

Secondary users include administrators (who configure projects/components, workflows, and permissions) and, in some deployments, **external reporters** — end users or community members who file defects through public sign-up, forms, or a community tracker.

The work context is software development and maintenance: defect records are created continuously from testing, internal use, customer reports, and automated checks, and they flow between these roles until each one is closed. The registry itself is also a management surface — leads and managers read it far more often than they write to it.

## Core Model

### The Defining Core

Four structures. Remove any one and the software is no longer recognizable as bug tracking:

- **Defect record.** A persistent, individually addressable unit — a bug with its own identity (typically a number or key) — describing a specific deficiency in the software: what was expected, what actually happened, and where it happened. This observed-versus-expected character is what distinguishes a defect record from a generic task: the record asserts that the software is wrong relative to intent, not merely that work remains.
- **Responsibility.** Every record carries who reported it and who is responsible for handling it. Assignment is the mechanism that turns a complaint into tracked work. Many products add a verification or QA responsibility on top of the fixer's.
- **Lifecycle states.** The record advances through a defined sequence of states driven by work on it: received, examined/triaged, assigned, worked on, resolved, closed. "Resolved" and "closed" are distinct from "open" in every mature product, and the transitions are product-managed state changes, not free-form edits. Reopening a resolved defect (because the fix didn't hold or verification failed) is a normal, supported operation in this family of software.
- **Queryable registry.** Defects are not ephemeral conversations: they accumulate as a population that can be listed, filtered, searched, counted, and reported on over time. The registry is what makes phrases like "the top open crashes for the next release" meaningful.

### Standard Capabilities

Mature products commonly add the following around the core. They make defect tracking practical at scale but do not define the Type:

- **Importance classification** — an ordered severity scale (typically from "blocks everything / crashes the product" down to "cosmetic") estimating damage, and a priority estimating urgency or scheduling rank. Severity and priority are deliberately separate in most products: a tiny cosmetic bug in a splash screen can be prioritized high for political reasons; a catastrophic bug in a rarely used path can sit unprioritized for months.
- **Version and environment anchoring** — which released version(s) exhibit the defect, which future version is expected to fix it, and the platform/OS/build where it was observed. This is what connects a defect to a release.
- **Defect-space organization** — a hierarchy or scheme that partitions the product so reports can be routed: product → component, project → category, repository → labels. Routing by area is how triage scales.
- **Conversation and evidence on the record** — comments/notes threaded on the defect (including the "steps to reproduce" detail many teams keep there), and attachments: screenshots, logs, test cases, and fix patches.
- **Watching and notifications** — people subscribe to a defect (or are on its recipient list) and are notified of every change; email remains a first-class channel in this family, historically even the primary one.
- **Duplicate handling** — because the same defect is reported many times, products provide an explicit way to mark a record as a duplicate of another and link them, preserving the reports without inflating the population.
- **Relationships** — links between records: depends-on/blocks, parent/child, and plain "related". A crash may be unfixable until another defect is fixed; tracking that dependency is native to the model.
- **Saved searches and lists** — the primary working surface is a filtered, sortable list of defects ("mine, open, by priority"; "all open crashes in version X"); saving and sharing those queries is standard.
- **Reports and aggregates** — charts and summaries over the population: open counts by severity or by component, incoming-vs-closed trends, backlog composition. This is the management face of the registry.
- **Change history** — every state change and field edit on a record is logged with author and time; the audit trail is both a workflow aid and an accountability record.
- **Configurable workflow** — the set of statuses, the allowed transitions between them, and who may trigger each transition are typically administrator-configurable, because teams differ on how formal the path from report to closure should be.
- **Controlled intake** — report templates/forms that steer reporters toward reproducible, complete reports; prefilled cloning of similar defects; and, in externally visible deployments, sign-up or forms that let outsiders file into the tracker under a restricted role.

### One Structure, Many Implementations

The model is conceptual; products realize each concept differently:

```text
Concept:                    Common implementations:
Defect identity             numeric bug number, per-project key + number
Organization scheme         product/component, project/category, repository/labels
Importance                  separate severity + priority fields, label schemes,
                            organization-level typed fields
Fix anchoring               target/fix version fields, milestones, releases
Fix linkage                 manual comment, commit references, automatic
                            closure when a linked code change merges
Intake                      web form, email, API, public sign-up, templates
Deployment                  self-hosted open source, SaaS, embedded in a
                            code-hosting platform or work-management suite
```

A reader who has only seen one shape (a modern SaaS tracker inside a development suite) should still recognize the others: a self-hosted open-source community tracker with numeric bug IDs and email-driven workflow is the same Type.

## How It Works

### The life of a defect

```text
Observe wrong behavior
→ file a defect record (what happened vs what was expected,
  where: version/platform/component)
→ triage: is it a real defect? duplicate? how severe? who owns the area?
→ assign a responsible person
→ diagnose and fix
→ move to resolved (record what was done)
→ verify: the reporter or QA confirms the fix in the affected context
→ close
(→ reopen if the problem reappears)
```

Three loops within this flow matter more than the rest:

**Triage.** Incoming reports arrive continuously and vary wildly in quality. Triage is the filtering pass that keeps the registry meaningful: rejecting non-defects, merging duplicates into the canonical record, completing under-reported records (asking the reporter for missing steps via the record's own conversation), classifying severity, and routing to the owning area and person. In products that expose roles, triage authority is distinct from fixing authority. Triage does not need to be a separate job title — in small teams developers triage their area — but the step itself is structural.

**Fix anchoring.** When a defect is fixed, the fix is anchored back to the record: the resolution notes what was done, and a future version is designated in which the fix should ship. Modern development-integrated products tighten this loop mechanically — referencing the defect in a commit or code-change request can show the linked work on the record and, in some platforms, automatically move the record toward closed when the change merges. The anchor matters because a defect is not "done" when the code is written; it is done when the corrected behavior ships and holds.

**Verification and reopening.** Resolution and closure are separate steps in many products, and the gap between them is reserved for verification: someone re-checks the corrected behavior against the original report. If verification fails, the record reopens and returns to active states — the population never silently loses unfixed defects. Some teams close on reporter sign-off; others close when the fix reaches customers; the products support either convention.

### The standing query loop

Alongside the per-record lifecycle runs a continuous population loop:

```text
save/share queries (my open defects, open crashes by severity)
→ review lists and dashboards in team rituals and planning
→ promote defects into scheduled work (fix version / milestone)
→ report on the population over time (trend, aging, composition)
```

This loop is why the registry is queryable rather than just persistent: the value of the accumulated records is that questions can be asked of the population, not only of one defect.

### How records enter the system

Entry paths vary by deployment. Internally, testers and developers file through the web form; automated processes (build or test failures) can file records through the API. Externally visible deployments add public sign-up, anonymous reporting, or structured forms, typically with the external reporter confined to a restricted role that can file and comment but not reclassify others' records. Email remains a supported intake channel in several products — a heritage of the family's origins that still functions.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Report/intake form

The entry surface for a new defect.

- fields steering the reporter toward completeness: summary, observed vs expected description, steps to reproduce, component/area, affected version, environment, optional attachments
- primary actions: submit the report; some products offer template selection, prefilled cloning of a similar defect, or field sets tailored per project

### Defect list / query view

The team's primary working surface.

- a filterable, sortable table of records — typically identity, summary, status, severity/priority, area, assignee, last updated — with color or status cues
- primary actions: search/filter, sort, save the current query, open a record, export or print, act on selections in bulk
- saved queries serve as shared team views ("today's new reports", "untriaged crashes")

### Defect detail view

The record itself — where the work happens.

- full field set (identity, status, importance, version/environment, people), the description, and the threaded conversation
- attachments and evidence; linked records (duplicates, dependencies); change history
- primary actions: edit fields, comment, attach, change status, reassign, watch, clone, reopen, close, delete (usually discouraged in favor of a resolution)

### Change-status flow

Because transitions carry meaning, moving a record typically asks for more than a click: a resolution choice (fixed, duplicate, won't fix, no change required, and similar), a required note, or a verification step — often with per-transition permission checks.

### Reports / summary surface

Aggregations over the population: counts by status, severity, or component; trends over time; per-release defect composition; printable or exportable summaries.

### Administration surface

Configure the defect space and the machinery: products/components or projects/categories, versions and milestones, custom fields, statuses/workflow and transition permissions, roles and access levels, notification rules, intake forms.

## Important Rules / Behaviors

### Status is product-managed, not free-form

A record's state changes only through defined transitions, and many transitions demand justification (a resolution, a note) or authority (per-transition permission). This is what makes the lifecycle trustworthy enough to plan against.

### Resolution and closure are distinct, with verification between

The typical sequence resolves a defect (fix believed done) and closes it later (fix confirmed or shipped). A resolved-but-unverified defect is not considered finished, and reopening is a normal, supported operation — not an exception path.

### Severity and priority are different questions

Severity describes damage if the defect occurs; priority describes scheduling urgency. Products keep them as separate fields precisely because they frequently disagree, and mixing them destroys the information.

### Duplicates are merged, not deleted

Repeat reports of the same defect are marked as duplicates of the canonical record rather than discarded, so reporter interest stays attached to the defect that will be fixed. Deletion of records is usually restricted or discouraged; closing with a resolution is the normal exit.

### The record outlives the conversation

Everything material happens on the record — decisions, requests for information, fixes, verification — and the history of those changes is retained. The registry is an organizational memory: a defect closed years ago remains findable when a regression pattern appears.

### Visibility is a first-class dimension

Defects routinely contain sensitive detail (security issues, customer data, internal URLs), so per-record or per-area visibility (private defects, restricted components, security levels) is a common structural feature rather than an afterthought.

## Variants

- **Standalone self-hosted tracker** — the classic shape: a dedicated server product (often open source) whose entire surface is defect tracking; common in open-source communities as a *public* tracker where anyone may sign up and file.
- **Suite-embedded tracker** — defect tracking as a configured use of a broader work-management platform; the defect model (bug type, fix-verify workflow, fix versions) sits inside generic machinery alongside tasks and features.
- **Platform-native tracking** — defect records as issues inside a code-hosting platform, where the fix linkage (branch, code change, merge) is immediate and defect classification leans on labels and templates rather than fixed severity fields.
- **Externally facing / community tracker** — the tracker itself is a public institution: volunteer reporters, duplicate storms, triage gatekeeping; intake templates and public role restrictions carry most of the load.
- **Internally regulated variant** — organizations that treat defect records as quality/compliance evidence: formal severity policies, mandatory verification, retention and audit expectations.
- **Email-heritage operation** — teams that run most of the workflow through notifications and email replies; several products still treat email as a full participant surface.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Issue Tracker | closest sibling; shared machinery | uniform work items (tasks/features/bugs as types or labels) optimized for planning and execution; a bug tracking system centers the defect record and its fix/verify-shaped lifecycle. Remove defect-specific semantics (severity/repro/verification) → issue tracker; restrict an issue tracker to defect records → functions as bug tracking |
| Error Tracking Platform | adjacent, upstream signal source | automatically captures runtime errors/exceptions from deployed software as events; the bug tracking system holds the curated defect record humans act on. Detection vs adjudication |
| Help Desk / Ticketing System | structurally similar record-and-lifecycle, different object | tickets are user-reported service requests with SLA/fulfillment-shaped lifecycle; defects are product-behavior reports with fix/verify-shaped lifecycle owned by the team that builds the product |
| Software Test Management | adjacent, feeder and verifier | test management executes planned verification (cases, runs, results); defects discovered there become bug tracking records, and fix verification returns to testing |
| Engineering / Agile Project Management | consumer of the registry | boards, sprints, roadmaps organize planned work; defect records feed fixes into planning via fix versions/milestones, but planning machinery is not the defect model |
| Code Review Platform | meets at the fix boundary | the unit is a code change, not a defect; review of the fix patch (or the linked change request) complements, but does not replace, the defect record |

The Issue Tracker boundary is the live one in the modern market: most commercial products are general trackers in which bug tracking is a configuration, while standalone defect-centric products persist in open-source and self-hosted ecosystems. The Types share most surfaces; the record model and lifecycle semantics are where they differ.

## Representative Products

- **Bugzilla** — the canonical standalone open-source bug tracker; long-lived, defect-centric, historically email-driven; still operates large public community trackers.
- **MantisBT** — lightweight open-source bug tracking system, self-described as such; representative of the minimal, defect-first shape.
- **Jira (Atlassian)** — dominant commercial work-item tracker; bug tracking as a first-class configured use (bug work type, fix versions, components, workflows).
- **GitHub Issues** — platform-native issue tracking inside a code-hosting platform; bug tracking as one use among several; representative of the modern embedded shape.

The defining core was checked against older and minimal products (classic standalone trackers), platform-native tracking, and suite-embedded tracking, so that the definition is not overfitted to any single era or packaging.

## Sources

Research date: **2026-09-06**

- MantisBT — official Admin Guide (full): https://mantisbt.org/docs/master/en-US/Admin_Guide/html-desktop/ (incl. issue lifecycle and workflow, statuses, access levels, report-form fields, list and detail pages); documentation index: https://mantisbt.org/documentation.php
- Bugzilla (bugzilla.mozilla.org) — official documentation: Understanding a Bug https://bmo.readthedocs.io/en/latest/using/understanding.html ; Editing a Bug / Life Cycle of a Bug https://bmo.readthedocs.io/en/latest/using/editing.html ; User Guide https://bmo.readthedocs.io/en/latest/using/index.html
- Jira Cloud — Atlassian support documentation (hub and section structure, incl. work items, workflows, fix versions, components, dev-tool integration): https://support.atlassian.com/jira-software-cloud/ and https://support.atlassian.com/jira-software-cloud/resources/
- GitHub — Issues documentation: https://docs.github.com/en/issues and "About issues": https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues
- YouTrack (JetBrains) — product page (positioning only): https://www.jetbrains.com/youtrack/

> Sourcing limitations: Jira documentation was captured at hub/table-of-contents level; article bodies were not fetched, so Jira-specific defaults (default bug workflow statuses, default work types) are not asserted anywhere in this document. YouTrack's operational help was unreachable from the research environment; YouTrack contributes positioning context only and no operational claims rest on it. Exact default state names, numeric limits, and field defaults are therefore not stated; lifecycle descriptions are given in conceptual states, and product-specific vocabularies (which do vary) are recorded only in the research notes.
