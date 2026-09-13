# Patent Prosecution Management

## Overview

A **Patent Prosecution Management** application manages the office-procedural life of pending patent applications: it keeps an identified record for every application a firm or IP department is prosecuting before a patent office, tracks the office events and response deadlines that the examination procedure generates, and drives the workflow of preparing, filing, and recording the responses that move each application toward its outcome — grant, abandonment, or appeal.

"Prosecution" is the patent-office term for this examination-phase conversation: after an application is filed, the patent office reviews it and communicates — through office actions, notices, and requirements — and the applicant must respond in writing within set windows, possibly across several rounds, an examiner interview, or an appeal, until the office allows the application or the application is abandoned. The patent office itself describes navigating this process as "patent prosecution." The application's job is to make that conversation manageable: nothing in it is more unforgiving than the response window, because a response filed late can forfeit the application.

The defining core is small:

```text
Prosecution case record
  (one identified record per application being prosecuted:
   bibliographic identity, parties, prosecution status)
└── Office-procedural timeline
    (recorded office events — filing, publication, office actions,
     notices, allowance — and the response deadlines they trigger)
└── Response workflow through to a recorded outcome
    (prepare, track, and record the filings the office procedure demands,
     advancing the case toward grant, abandonment, or appeal)
```

Everything else commonly associated with these products — automated docketing, jurisdictional rules engines, patent-office data feeds, IDS tooling, appeals task chains, client portals, billing — is a widespread and often expected extension, but not what makes the product a prosecution management application. Older, single-jurisdiction docketing systems — case records, office-action entries, response dates, a calendar — satisfy the core without any of those extensions.

The Type has a natural span: it begins when an application exists (filing) and ends when prosecution does (grant, abandonment, or appeal). Post-grant life — maintenance fees and renewals — belongs to patent portfolio management, not prosecution.

## Users & Context

The primary working context is the **law firm or IP practice** that prosecutes applications for clients; a corporate IP department runs the same structure from the owner's side, usually watching work it has delegated to outside counsel.

- **Patent attorneys / prosecutors** — own the cases; decide response strategy (argue, amend claims, interview the examiner, appeal); produce or approve the substantive responses.
- **Docketing specialists / paralegals** — the daily operators: enter office events, verify dates, work the deadline list, generate forms and client reports; in most practices this role lives in the system all day.
- **Billing / administrative staff** — turn prosecution activity into client invoices; administer users and templates.
- **Clients** — receive reports about their pending applications and, where offered, view portfolio status through read-only portals.

**External parties** shape the workflow more than in most application types: the patent office itself is the counterparty whose communications drive every deadline, and foreign associates act for the firm in other jurisdictions. A structural consequence: the system is only as good as its record of what the office has said, which is why office-data integration and reconciliation are so prominent in mature products.

## Core Model

### The Defining Core

**Prosecution case record.** The central object: one identified record per patent application being prosecuted. It carries a bibliographic identity — application number, jurisdiction, title, inventors, applicant/assignee, filing and publication dates — plus a **status** placing it on the procedural path (typically: filed → pending/published → allowed → granted, with abandonment as the exit). It names the responsible people: the attorney of record, supporting staff, and often a foreign associate for other jurisdictions. In firm-side products the case is also the billing unit.

**Office-procedural timeline.** Attached to the case is the running record of what the office has done and what the applicant must therefore do: each office event (an office action issued, a notice sent, a status change at the office) is recorded, and each event that demands a response carries a computed or recorded **deadline** — usually tracked as both an internal target date and the final legal due date. The timeline is cumulative: the sequence of events and responses on a case is its prosecution history.

**Response workflow.** Each demanded response becomes work: a task with an owner, the preparation of the response itself (arguments, claim amendments, forms, fee payments at allowance), the actual filing, and the recording of the filing — which in turn triggers the next stage's deadlines. The loop ends only at an outcome: allowance and grant, abandonment, or an appeal path.

Remove the case record and nothing remains. Remove the office-event/deadline timeline and what is left is a drafting workspace or a document folder. Remove the response workflow and what is left is a passive deadline calendar or a portfolio register — related, but not prosecution management.

### Standard Capabilities

Mature products commonly add the following. They make the core practical at practice scale, but a product can lack individual items and still be clearly a prosecution management application.

- **Docket/task machinery** — typed tasks that are either to-dos ("respond to the office action") or event records ("office action received"); each task has an owner, a reference date, an internal respond-by date, and the final legal due date; tasks are generated automatically when case data changes or an office communication arrives, and fire templated notifications and calendar entries.
- **Jurisdictional deadline rules** — a maintained body of rules computing response windows per jurisdiction and procedure (statutory periods, extension mechanisms), updated as laws change; where no rule exists, dates are entered by hand from the office communication.
- **Patent-office data integration** — import or automatic retrieval of bibliographic data, office documents, and status changes from office systems where feeds exist (for example the USPTO's filing systems and status services, EPO and WIPO sources); spreadsheet import or manual entry where they do not — which is still the norm for many non-US jurisdictions. Deeper integration enables automatic docketing of incoming office communications and reconciliation checks between the system's data and the office's data.
- **Prior-art and citation handling** (US practice) — references stored once and linked to every family member that cites them; generation of information disclosure statements and the corresponding office forms; counts showing what has been cited and what has not; automatic creation of supplemental-disclosure tasks when a related case cites something new.
- **Document repository and form generation** — per-case folders with revision history; office communications, responses, and executed filings attached to the case and its tasks; one-click generation of office forms and form letters populated from case data.
- **Family and continuation links** — connections between related applications (shared priority, continuations, divisionals), with transitive "related cases" views; family structure drives citation obligations and priority dates.
- **Appeals support** — task chains for the appeal procedure (notice of appeal, briefs, hearings, decision review) where the jurisdiction provides one.
- **Roles and audit** — role-typed users (attorney, paralegal/docketing clerk, administrator, client) governing visibility and edit rights; an activity log attributing each change, because the docket is legal evidence.
- **Client reporting and portals** — automatic notifications to the firm when office-driven deadlines arise (routed through internal users), scheduled client reports, and controlled client views of portfolio status.
- **Billing integration** (firm side) — fee events recorded against cases accumulate into client invoices in legal e-billing formats.
- **Reporting** — saved docket reports, aging and backlog views over pending cases, scheduled delivery.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Office-event ingestion
Forms:     automatic processing of office e-communications, scheduled data
           retrieval from office systems, spreadsheet import, manual entry

Concept:   Deadline computation
Forms:     vendor-maintained jurisdictional rules, firm-configured task
           types with reference dates and offsets, hand entry from the
           office communication

Concept:   Response production
Forms:     attorney-drafted responses and amendments, generated office
           forms and shells, fee payments at allowance
```

A reader who has only seen a modern cloud product with automatic office-feed docketing should still be able to recognize an older system — case cards, hand-entered office actions, a deadline calendar — as the same Type.

## How It Works

### Bring a case into the system

```text
New case:      application drafted and filed (or filing instructed)
               → case record created → filing date entered → status: pending
Existing caseload: bulk import from office data or spreadsheets
               → validation → family links established → statuses set
```

### The prosecution loop (the central interaction loop)

```text
An office event occurs (office action issued, notice sent, status changed)
→ the event is recorded on the case (automatically from office feeds
   or entered by hand)
→ rules compute the response deadline (internal target + final legal due date)
→ a response task appears on the docket with an owner
→ reminders and calendar entries fire as the date approaches
→ the attorney prepares the response (arguments, amendments, forms)
   with paralegal support
→ the response is filed → the filing is recorded → the task is closed
→ the closing triggers the next stage's deadlines
→ ... repeats through successive office actions
→ until an outcome: allowance → issue fee → grant,
   or abandonment, or an appeal path
```

This loop runs continuously across the whole caseload; the docket list sorted by due date is the daily working surface of the docketing specialist. Two properties matter structurally: tasks double as **history** (an event record of what the office said and what the firm did), and a closed task does not necessarily mean success — "missed" is a recorded outcome with legal weight.

### Extension sequences

Many response windows can be extended by filing a request and paying a fee. One common implementation models this as a sequence: when the current window's task is marked missed, the next extension window's deadline is generated, and the sequence continues until the final deadline, after which the application is lost. Extensions are typically not pre-created on the docket — to avoid flooding it with windows that will never be used — but the sequence is ready when needed. Some deadlines cannot be extended at all; under current US practice, for example, the fee payment due after a notice of allowance sits in a short non-extendable window, and missing it abandons the application.

### Citations and disclosures (US practice)

```text
A reference is cited (by the examiner, or by the applicant in a related case)
→ the reference is stored once and linked to every family member that must cite it
→ disclosure statements and office forms are generated
→ uncited-reference counts show what remains outstanding
→ related pending cases receive supplemental-disclosure tasks
```

### Client reporting

When an office communication with a deadline arrives, the system generates a notification; in some products these notifications are routed through internal users rather than sent directly to clients, who then relay structured reports. Scheduled reports and, where offered, client portals give the client a controlled view of its pending cases.

### End of prosecution

```text
Allowance → issue-fee payment (non-extendable window in US practice)
→ grant recorded → case status: granted
→ post-grant maintenance (renewals/annuities) passes to
   patent portfolio management — a different loop
Abandonment → recorded as the outcome → work generation stops
Appeal → the appeal task chain takes over until the tribunal decides
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Docket / task list

The deadline-safety surface and the specialist's daily view.

- tasks with type, reference date, respond-by and final-due dates, owner, status
- filterable and sortable; common views saved as reusable reports
- primary actions: close with outcome, reassign, add documents or comments, bulk edits

### Case detail

The register's front door for a single application.

- bibliographic data, parties, family links, published claims where available
- the case's task history — which is its prosecution history: every office event and response with dates and outcomes
- primary actions: edit record, add task, record an event, open documents, generate forms and letters

### Calendar / reminders

Time-oriented view of upcoming deadlines; reminder emails and calendar entries are generated from it.

### Prior-art / disclosure workspace

Reference lists per case and family, citation counts, disclosure-statement and office-form generation.

### Document repository

Per-case folders with revision history; office communications and filings attached to cases and tasks.

### Client portal

Where offered: a controlled, read-only view of the client's pending cases, governed by the firm.

### Reports

Docket reports, aging and backlog views, scheduled delivery, and the activity/audit log.

### Administration

Task types and their trigger rules, jurisdictional deadline rules (with test-before-production promotion in mature products), form-letter templates, user roles.

## Important Rules / Behaviors

### Deadline criticality is the system's constitution

A missed statutory response window can abandon the application, so the system treats deadlines differently from ordinary task software: due dates carry legal reference dates behind them, "missed" is a first-class recorded outcome rather than mere lateness, reminder sequences are deliberately staged, and extension sequences are modeled explicitly. This is the behavior every other design choice serves.

### Tasks are both to-dos and history

The docket records events that already happened as well as work that must be done. A case's task history is therefore its prosecution history — an evidentiary record of what the office said and who did what, when. Mature products discourage deleting tasks for exactly this reason.

### The office's record is the anchor

Case data originates from, and is checked against, the patent office's own records. Mature products generate reconciliation work when the two disagree (a "review differences" pattern) and alert users when an application's official status changes at the office. Where no office feed exists, the burden falls on manual entry — and the system's reliability drops accordingly.

### Representation matters

Patent offices communicate with the attorney or agent of record, not simultaneously with the applicant. The system is built around that representation: correspondence, forms, and deadlines attach to the case through the responsible practitioner.

### Inactive cases stop generating work

Cases that reach a terminal status (granted, abandoned, transferred) stop auto-generating tasks, so the docket reflects live obligations only.

### Family effects propagate

A citation or event on one family member can create obligations on related pending cases (for example, supplemental disclosure duties), because obligations frequently attach at family level, not per case.

### Financial records freeze (firm side)

Some products lock sent invoices against further changes, so the system's copy always matches what the client received; fee events, once invoiced, cannot be attached to another invoice.

## Variants

- **Law-firm edition (the default center)** — prosecution docketing, client billing, client portals, foreign-associate correspondence.
- **Corporate-side deployment** — the owner's IP department runs the same structure over its own pending applications, often to oversee outside counsel; disclosure intake and portfolio strategy sit upstream in patent management.
- **Regime emphasis** — US-weighted practice (office actions, extension sequences, information disclosure, appeals to the patent tribunal) vs European practice (examining communications, divisional filings, opposition windows) vs global PCT/national-phase coordination; office-feed availability varies sharply by jurisdiction.
- **AI-assisted prosecution** — automatic processing of office communications, extraction of examiner citations, generated response shells and forms; the newest common extension.
- **Work-product intelligence add-ons** — examiner statistics and art-unit analytics layered onto prosecution decisions; usually separate tools that attach to the workflow rather than manage it.
- **Suite module vs standalone** — prosecution management is frequently shipped as the firm-side emphasis of a broader IP management product rather than as a standalone category.

A variant remains a variant of this Type as long as the case record + office timeline + response workflow stays central. When the center of gravity moves to producing the application document itself (drafting), the product has become a drafting tool — a different Type, however it markets itself.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Patent Management | closest sibling; shared core | centers the **whole-life asset**: the portfolio register across granted and pending rights, renewal/annuity deadlines, renew-or-prune decisions, budgets. Prosecution Management centers the **pending case's office-procedural workflow** through grant. Structural test: remove post-grant renewals and a prosecution-centered system still stands; remove the office-response workflow and what remains is a portfolio register. In the current market both are sold as emphases of the same product family |
| Intellectual Property Management | broader superset | spans multiple IP classes (trademarks, designs, licenses) on one register; prosecution management is the patent-examination specialization |
| Legal Docket Management | adjacent, different object | tracks court cases and court-imposed deadlines in litigation; prosecution docketing tracks patent applications and statute/office-imposed deadlines — different records, different rules source |
| Legal Matter Management | broader container | manages legal matters of all kinds; patent prosecution matters are one matter type inside it, without patent-specific deadline rules and office integration |
| Legal E-filing Platform | counterparty surface | the patent office's own filing and case-management systems; prosecution management integrates with them (data feeds, e-communications) but is the firm-side system of record |
| AI Patent Drafting tools | upstream neighbor, often confused | center on producing the application document (claims, descriptions, drawings); no case register, no office-deadline timeline, no response workflow. The market phrase "prosecution software" is sometimes used for such tools; the phrase alone does not identify this Type |
| Patent Search / Analytics | different central object | operate on the global corpus of third-party patents and examiner data; prosecution management operates on the organization's own pending cases |
| Trademark Portfolio Management | sibling specialization | identical register+docket machinery applied to trademarks, whose lifecycle centers on renewals and use requirements rather than examination-driven response windows |

The most important boundary is with **Patent Management**: prosecution is one lifecycle stage of the patent asset, and in the researched products the prosecution workflow is implemented inside the same register-and-docket core that patent management uses. The two leaves are best understood as two centers of gravity on one structure — pending-case workflow vs whole-life portfolio — and deserve a joint review pass.

## Representative Products

- **AppColl Prosecution Manager** — cloud prosecution docketing and matter management for IP firms and small-to-mid corporate departments; the researched exemplar, with deep public documentation of its task, matter, prior-art, and office-communication machinery.
- **PATTSY WAVE (Anaqua)** — long-established patent and trademark docketing platform used by hundreds of law firms; known for automated docketing of US office activity and data validation against multiple office databases.
- **AQX Law Firm (Anaqua)** — enterprise IP management for law firms with an explicit prosecution emphasis (automated document processing, office-action responses, disclosure-statement generation).

The defining core was also checked against adjacent products that attach to prosecution without managing it — prosecution work-product tooling (Patent Bots) and a drafting-centered product marketed as "prosecution software" (PowerPatent) — to fix the boundary between managing prosecution and merely supporting it.

## Sources

Research date: **2026-09-06**

- USPTO — Patent Basics: https://www.uspto.gov/patents/basics
- USPTO — How to apply for a patent (process overview): https://www.uspto.gov/patents/basics/patent-process-overview
- AppColl Help Center — Prosecution Manager Overview Manual: https://support.appcoll.com/en_US/general-information/appcoll-overview-manual
- AppColl Help Center — Tasks category: https://support.appcoll.com/en_US/tasks
- AppColl Help Center — eOffice Actions category: https://support.appcoll.com/en_US/eoffice-actions
- Anaqua — PATTSY WAVE product page: https://www.anaqua.com/pattsy-wave/
- Anaqua — Achieve Docketing Excellence (PATTSY WAVE features): https://www.anaqua.com/pattsy-wave/achieve-docketing-excellence/
- Anaqua — AQX Law Firm product page: https://www.anaqua.com/aqx-law-firm/
- Patent Bots — product pages: https://www.patentbots.com/
- PowerPatent — product page: https://www.powerpatent.com/

> Sourcing limitation: several additional vendors in this category could not be reached from the research environment on 2026-09-06 (TurboPatent, Kluwer IP Wizard, CPI; Clarivate was also unreachable in the paired Patent Management research the same day). Cross-product claims therefore rest on the researched products, with Anaqua counted once despite two product lines. Precise operational figures observed in vendor documentation (task-offset values, refresh cadences, task-type counts) are kept in the Research Notes and deliberately not asserted here; the one office-sourced deadline behavior asserted (the non-extendable allowance-fee window in US practice) comes from the USPTO's own published process documentation. Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
