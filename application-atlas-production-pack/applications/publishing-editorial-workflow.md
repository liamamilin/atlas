# Publishing Editorial Workflow

## Overview

A **Publishing Editorial Workflow** application manages the editorial process of a publishing work: the work enters the system as a submission, proposal, or early draft — before any publication decision has been made — and is carried as a persistent editorial record through an ordered set of editorial stages (entry, evaluation, editing, release toward production), advancing through explicit decision gates, with each stage's work assigned to named editorial roles under deadlines.

The defining core is small:

```text
Work-in-editorial (the unit of record)
└── staged editorial process with recorded gates
    └── role-assigned stage work with deadlines
```

Everything else commonly associated with publishing software — contracts, royalties, title P&L, bibliographic metadata feeds, sales — is business machinery that mature products often carry alongside the workflow, but it is not what makes the workflow. Strip the money and metadata away and the editorial process remains; strip the process and what is left is a title database with a task list.

The Type is bounded on one side by Book Publishing Management (which centers the title as a commercial product rather than the content process) and on the other by generic workflow and project tools (which lack publishing's stages, gates, and unit of work).

## Users & Context

The primary users are the editorial staff of a book publisher — trade, academic, children's, religious, educational, or a scholarly university press:

- **acquiring / commissioning editor** — brings works in: records the proposal, makes the editorial case, shepherds the work through the acquisition decision
- **managing editor / editorial director** — assigns editors to works, monitors each editor's assignments, watches the whole list's progress
- **editorial assistant** — enters and maintains work data, sets up task schedules, chases dates
- **reviewers / readers** — external or internal people who evaluate a manuscript and return reports by a due date
- **copyeditors and proofreaders** — in-house or freelance, assigned to specific works for defined editing passes
- **production editor / production staff** — receive the work at the transmittal gate and carry the printer-facing tasks (files to printer, proofs checked, delivery confirmed)

The work environment is a publisher's list: many works in flight at once, each at a different editorial stage, all converging on publication dates. The system is the place where the editorial team sees who has what, what is late, and what decisions are pending. Secondary users include freelance editors and reviewers (reaching the system through assignments) and, in suite products, the surrounding departments — contracts, royalties, marketing, sales — who consume the workflow's outputs.

## Core Model

### The Defining Core

**The work-in-editorial as the unit of record.** The system's world is organized around a persistent record for one publishing work during its editorial life. The record exists *before* the publication decision — as a submission from an author or agent, a proposal drafted by a commissioning editor, or a first draft of a title idea — and it accumulates the editorial process's history: decisions taken, files attached, notes exchanged, steps completed. Works that are rejected or never published keep their record; the acquisition history survives the decision. Without this unit, there is no editorial workflow — only a title database or a pile of tasks.

**The staged editorial process with recorded gates.** What the system manages is the *process* the work moves through, not merely a list of tasks. The work advances through an ordered set of stages — entry, evaluation, editing, release toward production — and the transitions that matter are explicit decision points whose outcomes are recorded against the work: proposed or declined, review passed or revisions requested, approved for production. The stage set is configurable in mature products; the gate structure is what stays. Without gates, the system is a status board; without stages, a task list.

**Role-assigned stage work with deadlines.** Editorial work is delegated. Each stage's work is assigned to identified participants — the acquiring editor who owns the proposal, the reviewers who evaluate the manuscript, the copyeditor who edits it, the proofreader who checks it, the production editor who takes it forward — with due dates, reminders, and visible completion and overdue state. A managing role assigns work and monitors assignments across the list. Without assignment, the process is a diagram nobody works.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Submission and proposal intake** — a configured entry path that collects what is needed to evaluate a new work: details, files, the proposing editor's case for publication.
- **Evaluation machinery** — reviewer/reader assignment with due dates and automated reminders, overdue visibility, and — at the trade pole — the acquisition or editorial meeting organized in-system as a recorded decision gate.
- **Task and to-do machinery anchored on key dates** — per-work tasks with assignees; due dates fixed or relative to base dates such as the publication date or a manuscript delivery date, so that schedules shift automatically when those dates move; task templates, dependencies, reminders, and — in some products — calendar integration with external calendar systems.
- **Schedule visualization and company-wide visibility** — Gantt or visual schedules, dashboards surfacing active works, overdue tasks, and approval deadlines, and notification surfaces so everyone in the company knows what has to be done by when.
- **Manuscript and production file handling** — files attached to the work's record: submission files (chapters, figures), and production files archived as the record of what was sent to print. Depth varies; versioning of large working files may be left to external tools, with the system holding the archive of record.
- **Issue tracking** — in some products, problems arising during the process captured as tracked records rather than lost in email.
- **Configurable workflows and roles** — stage sets, role systems, and workflow steps adapted to each publisher's own process.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  work-in-editorial as unit of record
Realizations:  submission record (scholarly workflow systems),
               work + proposal brief (cloud suites),
               idea/submission/proposal in pre-production (modular suites),
               early title draft (enterprise suites)

Concept:  staged process with gates
Realizations:  named stage sequence submission → review → copyediting →
               production (scholarly systems),
               proposal → plan → acquisition meeting → publication process
               (suites), configurable stage boards and workflow-driven apps

Concept:  role-assigned stage work
Realizations:  reviewer assignment with due dates and reminders,
               to-dos assigned to system users,
               schedule templates auto-assigning tasks by role
```

A reader who has only seen one realization should still recognize the others from the core model.

## How It Works

### Capture the work early

```text
A work becomes a publishing possibility
→ it is recorded in the system immediately — not in a document or email first
→ the originator enters what is known (details, contributor, files, the
  editorial case in a proposal brief)
→ the work sits in the system as an early record, without cluttering the
  list of real titles
```

The record exists from this moment on, whatever the decision turns out to be.

### Evaluate and decide

```text
Evaluation begins
→ reviewers/readers are assigned with due dates; reminders go out;
  overdue responses are visible
→ reports come back; revisions may be requested and re-reviewed
→ at the trade pole, the proposal is put to the acquisition or editorial
  meeting: the editorial argument (brief) and the financial argument
  (plan/P&L) are on screen, and the meeting works through the pipeline
→ the decision is recorded against the work: approved, declined, revisited
```

The gate is the point of the stage: an explicit, recorded outcome — not a silent drift to the next phase.

### Edit

```text
Approved work enters editing
→ editing passes are planned as assigned, dated work: copyedit,
  proofread — each pass owned by a named person, in-house or freelance
→ the manuscript and its files live on the work's record
→ problems found along the way are raised as tracked issues
→ completed steps are checked off; the editorial record accumulates
```

### Release to production and track to publication

```text
The work is approved for production
→ transmittal: the approved files and the remaining tasks move to
  production editors
→ printer-facing tasks run on the same machinery: send files to printer,
  check proofs, confirm the job, check shipment — each assigned and dated
→ task dates hang off key dates (publication date, manuscript delivery
  date); when a date moves, dependent dates move with it
→ the workflow's output joins the publisher's wider machinery: metadata
  to the trade, marketing materials, the published book
```

### The standing loop

Across all stages, the managing view is the same: the list of works in flight, each with its stage, its pending decisions, its assigned and overdue work. Editors work from their assignments; managers watch the list; everyone sees what has to be done by when.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Work list / pipeline board

The primary entry surface over the work population.

- works grouped by editorial stage; filters such as drafts, forthcoming, published
- primary actions: open a work, advance a stage, record a decision, add a work

### Work editorial page

The work's record — the hub of its editorial life.

- editorial state and stage history; proposal brief; attached files; decisions taken
- tasks and to-dos with assignees and dates; notes and discussions; issues
- primary actions: enter/edit data, upload files, assign work, set or shift dates, check off completion

### Review / evaluation workspace

The evaluation stage's working surface.

- submissions awaiting evaluation; assigned reviewers and due dates; returned reports; overdue flags
- primary actions: assign a reviewer, set a due date, send a reminder, record the review outcome

### Task and schedule views

The deadline machinery.

- per-work task lists; schedule views (Gantt-style or visual boards) with dependencies; calendars exportable to external calendar systems; dashboards of active works, overdue tasks, and approval deadlines
- primary actions: create/assign tasks, set fixed or date-relative deadlines, reschedule when key dates move

### Role and workflow configuration

Administrative surfaces.

- stage and workflow definitions; user roles and permissions; task templates

## Important Rules / Behaviors

### Gates are recorded decisions

Stage advancement at the points that matter is an explicit act with a recorded outcome — approved, declined, revisions requested. The acquisition record persists even for works that are never published; early drafts of rejected ideas remain retrievable without cluttering the live list.

### Assignment requires identified people

Tasks and reviews are assigned to users of the system; the assignee is the person who completes the work or confirms that a third party has done it. Work cannot float unassigned if the process is to be visible.

### Dates hang off key dates and shift with them

Task deadlines are commonly expressed relative to base dates — the publication date, a manuscript delivery date. When a base date moves (a manuscript arrives late, a publication date slips), dependent task dates move automatically. This is what keeps a list of dozens of works schedulable at all.

### Overdue state is visible by design

The system surfaces falling-behind work — overdue reviews, late tasks, approaching approval deadlines — to the assignee and to managing roles. The editorial process is managed partly through this visibility.

### The workflow tracks the process; it does not do the editing

Writing, revising, and layout happen in editors and layout tools outside the workflow system. The system routes the work, records its state, and archives the files of record; it is deliberately not the place where prose is edited or pages are designed.

### Workflows are configurable, stage names are not universal

Every sampled product lets the publisher adapt stages, roles, and task templates to its own process. No canonical stage vocabulary exists across products; the gate structure, not the labels, is the stable thing.

## Variants

- **Standalone editorial-workflow system** — the workflow is the whole product: submission wizard, review rounds, editing stages, publication. Strongest at scholarly presses and library-based publishers, where peer review is a standard stage and the press publishes to its own website.
- **Editorial core inside a publishing management suite** — the workflow is the process spine of a wider title-management system, surrounded by contracts, royalties, rights, metadata, and sales machinery. The dominant packaging for trade publishers.
- **Modular workflow bolt-on** — the production/pre-production workflow sold as a separately licensed module over a shared title database.
- **Scholarly calibration** — peer-review rounds (internal and external, anonymous or open) as a first-class stage; scholarly infrastructure (DOIs, ORCID, OAI-PMH, ONIX for books and chapters); multilingual metadata; in-system catalog publication.
- **Trade calibration** — the acquisition/editorial meeting as the evaluation gate; reader reports; production handoff and metadata delivery to the trade.
- **Scale tiers** — lighter editions for small publishers (acquisition, contracts, schedules, catalogs) with upgrade paths to full workflow machinery.
- **Deployment** — open-source self-hosted, SaaS, hosted service, on-prem plus cloud.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Book Publishing Management | centers the title as a commercial product — money (P&L, contracts, royalties), metadata to the trade, sales, backlist; the editorial process appears there as schedule tasks and decision gates, not as the managed thing. Suite products bundle both faces; the acquisition stage genuinely overlaps |
| Academic Journal Management | the same workflow shape (container + submissions + staged workflow + evaluation + publication) realized over journal/article objects with issues and scholarly-serial semantics; the scholarly monograph press sits on the seam and is claimed here as book publishing |
| Peer Review Platform | the review exchange itself — reviewer–submission pairing, review records as the primary objects — container-agnostic; here review is one stage inside the work's process |
| Newsroom Management System / News Publishing Platform | the newsroom's continuous produce-and-publish loop over a story stream with public channels and post-publication corrections; here a per-title, project-like process with a publication horizon and a production handoff |
| Magazine & Periodical Management | the periodical business system — publication, issue cycle, advertising, circulation; editorial tracking there is a capability, not the center |
| Workflow / Approval Workflow Platform | generic process machinery over arbitrary records; here the stages, gates, roles, and unit of work are publishing-specific |
| Project Management Application | production schedules resemble project plans, but the unit is the publishing work with editorial stage semantics; strip the publishing semantics and a generic PM tool remains |
| Document / Collaborative Editor | the editing work itself happens there; the workflow system routes and tracks the process and archives the files of record |
| Desktop Publishing / Page Layout | layout is executed there; the workflow tracks the tasks and pushes data into layout tools, but does not perform typesetting |

The boundary with Book Publishing Management is the most important one, because market products genuinely bundle both. The structural test: remove the content-process depth (evaluation machinery, editing stages, editorial gates, the editorial record) and the business lifecycle remains — that is publishing management; remove the money, metadata, and sales machinery and the content process remains — that is this Type.

## Representative Products

- **Open Monograph Press (PKP)** — open-source editorial-workflow-first system for scholarly monograph presses; the standalone pole
- **Consonance** — modern cloud publishing suite whose editorial process (proposal briefs, acquisition pipelines, to-dos anchored on publication and manuscript-delivery dates) is documented in unusually deep official user guides
- **Stison** — modular SMB cloud suite; Production Manager covers pre-production through production scheduling
- **Firebrand Title Management Enterprise** — US title-lifecycle workflow platform since 1994; the vendor's own category name for the territory is "Publishing Workflow and Project Management"
- **Klopotek (Title Management, Editorial & Production)** — enterprise publishing suite; editorial drafts through Editorial Meeting approval with workflow-driven apps and company-wide schedule notification

## Sources

Research date: **2026-09-09**

- Open Monograph Press — https://pkp.sfu.ca/software/omp/ ; https://github.com/pkp/omp (README)
- Consonance — https://consonance.app/docs/ , incl. /docs/best-practice-publishing-process/ , /docs/create-and-use-a-pipeline/ , /docs/pipelines-ten-uses/ , /docs/to-dos/ , /docs/production-files/
- Stison — https://www.stison.com/production-manager
- Firebrand Technologies — https://firebrandtech.com/title-management-enterprise
- Klopotek — https://www.klopotek.com/title-management-editorial-and-production
- Sibling research consulted for boundary work: research/book-publishing-management.md, research/academic-journal-management.md, research/news-publishing-platform.md, research/magazine-periodical-management.md, research/peer-review-platform.md

> Sourcing limitations: PKP's user documentation site was unreachable (anti-bot challenge) — OMP evidence is at official product-page level, and no production-stage internals are asserted. General web search was unusable this pass (engine timeouts/regional redirects), so no new vendors were discovered beyond the sibling-known set; the sample inherits the sibling passes' reachable population. Stison, Firebrand, and Klopotek evidence is at official product-page level. Precise operational details (numeric limits, default settings, exact stage vocabularies, permission granularity) are intentionally not stated in this document; such detail remains in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
