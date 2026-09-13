# Board / Corporate Governance Platform

## Overview

A **Board / Corporate Governance Platform** — in the market most often called *board management software* or a *board portal* — is the system an organization uses to administer the work of its board of directors and its governing committees. It maintains the roster of governed bodies and their members, assembles and securely distributes agenda-structured meeting materials (the **board pack** or *board book*), supports the meeting itself, and preserves the outcome — confirmed minutes, recorded decisions, resolutions and follow-up actions — as the body's official governance record.

The defining core is small:

```text
Governed body (board / committee) with an identified member roster
└── Meeting as the unit of governance work
    ├── Agenda structuring the meeting
    ├── Board pack — materials assembled against the agenda and
    │   distributed to the body's members under member-scoped confidential access
    └── Governance record — minutes, decisions, resolutions and actions,
        confirmed and retained as the official record
```

Everything else commonly associated with the category — voting, e-signatures, director questionnaires, board evaluations, secure messaging, video integration, AI drafting — is standard or optional capability layered on this core, not what makes the product a board platform. The Type exists because board materials are confidential, the meeting cycle is recurring and formal, and the record must be authoritative; email, shared drives and generic meeting tools provide none of these guarantees.

## Users & Context

The software serves a small, named population with sharply asymmetric roles:

**Primary operator** — the *corporate secretary*, *board secretary*, *governance manager* or *executive assistant to the board*. This person runs the meeting cycle: schedules meetings, builds agendas, chases and attaches papers, compiles and distributes the pack, takes and finalizes minutes, and maintains the record. In public-sector and nonprofit settings the equivalent role is the *board clerk* or *administrator*.

**Primary consumers** — *directors, trustees and committee members*. They are senior, time-poor and often non-technical; they read the pack, annotate it, vote, sign, and expect the material to be current and self-evident. Director adoption is a first-order design constraint for the whole category, not an afterthought.

**Secondary participants** — the *chair* (signs minutes, controls proceedings), *executives* (present agenda items and supply papers), and in suite deployments the *general counsel* or governance team that also manages entities, questionnaires and compliance records.

The usage rhythm is a recurring meeting cycle (monthly or quarterly for most boards, with committee meetings interleaved) plus a slower annual layer: board evaluations, director questionnaires, interest/conflict disclosures, and planning of the year's meeting calendar. Access is needed between meetings as well — actions from the last meeting, policies, past minutes.

## Core Model

### The defining core

**Governed body.** The organizing container is the board or committee — a named governing body of the organization (main board, audit committee, remuneration committee, sub-committees; in multi-organization deployments, subsidiary boards). Each body has an identified member roster: directors or trustees with roles and terms. The body scopes everything else — who receives which pack, who may vote, whose record this is.

**Meeting.** The unit of governance work is the meeting: a dated, scheduled occasion of a specific body, with attendees, location or remote link, and a lifecycle that runs from scheduling through materials, conduct, and minutes to confirmation. Meetings recur on a calendar; the record of past meetings accumulates into the body's institutional memory.

**Agenda.** The agenda structures the meeting into sections and items, each with a presenter, an allocated time, and — crucially — the papers attached to it. The agenda is drafted, reviewed, and then published as the official notice of business.

**Board pack.** The board pack (board book) is the curated set of meeting materials assembled against the agenda: the agenda itself plus the documents attached to each item, compiled into a single paginated, numbered volume and distributed to the body's members. Distribution is member-scoped and confidential — the pack is addressed to the body's members, access is controlled per person and per document, and materials live inside the platform rather than as email attachments. This is the property the Type was created to deliver: the replacement for photocopied, couriered and emailed board papers.

**Governance record.** The meeting produces the record: minutes drafted against the agenda, with recorded decisions, resolutions, votes and action items (each action with an owner and follow-up). Minutes go through review and are confirmed — typically at the subsequent meeting — and the confirmed record is retained permanently as the body's official account. Past packs, minutes and policies accumulate into a searchable governance library.

### Standard capabilities of mature products

These are widespread across the researched market and expected by buyers, though they do not define the Type:

- **Agenda builder** — sections, items, presenters, time allocations; cloning of a previous meeting's agenda; draft circulation for review before publication.
- **Pack assembly machinery** — automatic compilation and page numbering; republishing when late papers arrive, producing a new version while retaining the original; a change log of what changed; replacing a document without destroying directors' annotations.
- **Director reading experience** — agenda-linked reading, personal annotations and notes, tablet/mobile apps, offline access, and read receipts showing who has opened the pack.
- **Minutes workflow** — minutes drafted within the agenda structure; review circulation; confirmation; e-signature by the chair or designated signatory.
- **Decision machinery** — formal voting on motions (in-meeting or out-of-cycle), decision/resolution registers, action items with owners, due dates and reminders.
- **Governance repository** — policies, standing documents and past packs in one searchable, permissioned library.
- **Meeting logistics** — official notices, reminders, calendar integration, remote-meeting links or embedded video conferencing.
- **Security baseline** — role-based permissions, encryption, multi-factor authentication, audit trails; materials kept inside the platform ("no inbox copies").
- **Multi-body support** — boards plus committees under one account; in larger deployments, multiple subsidiary or affiliated boards.
- **AI assistance** — an increasingly standard layer: drafting the book from uploaded papers, summarizing dense material for directors, generating minutes from transcripts, and answering questions across years of board history with cited sources.

### Optional / variant capabilities

Depending on segment and vendor, products may add: director & officer questionnaires, interest/conflict-of-interest registers, board evaluations and skills tracking, annual work plans, out-of-cycle written resolutions ("flying minutes"), secure board messaging, live streaming, entity/subsidiary management, and — in the public-sector variant — a public transparency site. These are extensions, not the core.

## How It Works

The heart of the product is the **meeting cycle** — a loop that repeats for every meeting of every body:

```text
Plan the calendar
→ Build the agenda (draft → review → publish)
→ Assemble the board pack (attach papers → compile → number → distribute)
→ Directors prepare (read, annotate; late changes republished as a new version)
→ Hold the meeting (present, discuss, vote, assign actions)
→ Draft minutes against the agenda
→ Review → confirm → sign
→ Between meetings: track actions, maintain the repository
→ …next meeting
```

**Plan and schedule.** The administrator creates the meeting for a body — date, time, location or remote link — often well in advance so members can reserve the time. Many products maintain a full annual meeting schedule or work plan for the body.

**Build the agenda.** Agenda items are added under section headings, with presenters, time allocations and attached papers. A typical practice is to clone the previous meeting's agenda and adjust. While in draft, the agenda can be shared with the chair or executives for input. Publishing makes it official: members can see it, and the pack can be generated. A published agenda can still be edited and republished — the change is logged and a new pack version is issued.

**Assemble and distribute the pack.** Papers arrive from executives and are attached to agenda items as they come in. When the administrator publishes, the system compiles the pack — agenda plus attached documents, paginated and numbered — and distributes it securely to the body's members. If a paper arrives late, the administrator replaces or adds the document and republishes; the system renumbers, records the change, keeps the prior version, and preserves directors' annotations where possible. Members receive a notification rather than an attachment.

**Directors prepare.** Directors open the pack in the app or on the web, read documents linked to agenda items, and take personal annotations. Read receipts show the administrator who has opened the pack. AI features, where present, summarize dense papers and surface key questions before the meeting.

**Hold the meeting.** The meeting runs from the agenda: presenters speak to items, the system may display the pack in a presentation mode or link to the video conference, and the minute-taker records notes, decisions and actions against each item. Formal votes can be taken in the product and recorded per member.

**Draft, review, confirm the minutes.** Minutes are drafted within the agenda structure — each item carrying its notes, decisions, actions and vote outcomes. The draft is circulated for review, corrections are made, and the minutes are confirmed — in board practice, typically at the next meeting, where the previous minutes appear as an agenda item for confirmation. The confirmed minutes are signed (commonly with an e-signature by the chair) and locked as the official record. Actions assigned during the meeting flow into an action list that the administrator tracks between meetings, with reminders to owners.

**Between meetings.** The repository holds policies and past materials; out-of-cycle resolutions may be processed as written resolutions; the annual layer (evaluations, questionnaires, disclosures) runs on its own calendar.

## Interfaces

Two very different surfaces face the two populations — this asymmetry is characteristic of the Type.

### Administrator workspace (web)

The operator's console. Typical surfaces:

- **Meetings list / calendar** — all bodies' meetings with their current stage; create, schedule, cancel.
- **Agenda builder** — sections, items, presenters, times, attachments; draft/publish controls; change log.
- **Pack builder / review** — compile, preview, republish; version history; read receipts.
- **Minutes workspace** — take minutes per agenda item; notes, decisions, actions, votes; review circulation; confirmation and signing controls.
- **People & permissions** — members, roles, terms, per-document access.
- **Repository & registers** — governance library, decision register, action list, interest register.
- **Governance dashboard** — upcoming meetings, pending actions, overdue items, engagement.

### Director experience (app / tablet / web)

Deliberately simple. Typical surfaces:

- **Home / meetings** — upcoming meetings, current pack, outstanding actions and approvals.
- **Pack reader** — the paginated pack with agenda navigation, personal annotations, search.
- **Voting & approvals** — cast or record votes; sign documents and minutes.
- **Library** — policies, past packs, past minutes.

### Public transparency site (public-sector variant)

For school boards, councils and other public bodies, a separate outward-facing site publishes agendas, minutes, policies and recordings to the public, with accessibility compliance — while internal materials remain permissioned.

## Important Rules / Behaviors

**Meeting status gates the work.** A meeting moves through stages — agenda not yet prepared, agenda in draft, agenda published; then minutes in draft, minutes in review, minutes confirmed. Which actions are available depends on the stage: agenda items are editable in draft, the pack exists only after publication, minutes are drafted after the meeting and confirmed later. One researched product implements this as an explicit six-stage state machine (No Agenda → Draft Agenda → Published Agenda → Draft Minutes → Minutes in Review → Minutes Confirmed); other products implement the same pattern with their own stage names. The confirmed record is treated as final — the meeting is locked so the approved record cannot silently change.

**Published materials are versioned, never overwritten.** Republishing after a late change produces a new pack version; the original is retained and changes are logged. Directors must be able to rely on what they read, and auditors must be able to see what changed and when.

**Access is member-scoped and revocable.** Permissions attach to the body and the person; a paper can be restricted to a subset of members; access can be revoked at any time. The platform's standing promise to buyers is that board materials never travel as email attachments and never leave stray copies.

**The record is attributable and auditable.** Votes, decisions, signatures and access events are logged. Minutes carry the actual attendance, and the confirmed minutes are the authoritative account against which later questions ("what did the board decide and why?") are answered.

**Draft materials are visible to members, but marked as draft.** Draft agendas and draft minutes are typically labeled as such (one product titles the PDF "Draft Agenda" until publication); whether draft minutes are hidden from members is a product policy, not an industry constant.

**Director adoption constrains design.** The consumer surface must be usable by senior, non-technical members without training; complexity is concentrated in the administrator workspace. Products compete heavily on this.

## Variants

- **Enterprise corporate** — security-grade posture, governance-suite integration (entities, risk, compliance), corporate service providers running many client boards on one platform.
- **Mid-market SaaS** — the volume center of the market; director-experience-led, fast to adopt.
- **SMB / nonprofit / schools** — simpler, lower-cost editions; the same core loop with lighter machinery.
- **Public sector** — school boards, municipal councils, special districts: the same meeting cycle plus a public transparency site, livestreaming, accessibility compliance, and public goal tracking.
- **Regulated industries** — banks, credit unions, healthcare, universities: the core loop with stricter security, residency and audit expectations.
- **Regional deployments** — data-residency commitments (e.g., in-country storage), national digital-identity integrations for signing and authentication.
- **Governance suite vs pure-play** — the same core sold alone, or as the board layer of a broader corporate-governance suite.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Corporate Governance Platform | near-duplicate leaf in the directory | market products conflate board management with broader governance suites; the board meeting cycle is the core here, suite modules (entities, risk, compliance) are extensions |
| Committee / Board Management (association context) | audience variant | identical core model applied to association boards and committees; vocabulary changes, structure does not |
| Legislative Management System / Government Meeting & Agenda Management | adjacent, overlapping in public sector | organized around the public legislative/clerk workflow (readings, ordinances, public comment) rather than a governed body's confidential meeting cycle; public-sector board portals sit between the two |
| Virtual Data Room | adjacent | document sharing with external parties for a transaction; no governed body, no recurring meeting cycle, no minutes or official record |
| Meeting Scheduling Application | adjacent | finds times for any meeting; no bodies, packs, or governance record |
| AI Meeting Assistant / Meeting Recording & Transcription | capability donor | captures and summarizes any meeting; supplies the minutes-from-transcript capability but has no governance body, member-scoped pack, or confirmed record |
| Enterprise Content Management | broader | organization-wide content lifecycle; the governance repository here is a bounded library for one function |
| Legal Entity Management | suite neighbor | core object is the legal entity/corporate record, not the board meeting cycle; often bundled in governance suites |

The most important boundary: remove the governed body and its member-scoped pack, and the product becomes generic meeting software or file sharing; remove the confirmed record, and it becomes a document portal; add a public legislative workflow, and it becomes agenda management for government.

## Representative Products

- **Diligent Boards** (Diligent) — enterprise flagship; board management inside the broader Diligent One governance suite; sibling variants BoardEffect (nonprofits/higher education) and Diligent Community (school boards and local government).
- **OnBoard** (Passageways) — mid-market SaaS; meeting lifecycle, governance system of record, director engagement, board continuity.
- **Azeus Convene** (Azeus Systems) — international board portal; separate AGM and board-evaluation product lines.
- **BoardPro** — ANZ SMB/nonprofit/school segment; workflow-first with a fully documented meeting lifecycle.

## Sources

Research date: **2026-09-06**

- Diligent — Diligent Boards product page: https://www.diligent.com/products/boards/
- Diligent — Diligent Community product page: https://www.diligent.com/products/community/
- OnBoard — product/platform pages: https://www.onboardmeetings.com/
- Azeus Convene — product page: https://www.azeusconvene.com/
- BoardPro — product page: https://boardpro.com/
- BoardPro Help Centre — Meeting Workflow collection: https://help.boardpro.io/en/collections/3796866-meeting-workflow-from-building-the-agenda-to-confirming-the-minutes
- BoardPro Help Centre — "Meeting Stages and Flow": https://help.boardpro.io/en/articles/376886-meeting-stages-and-flow

> Sourcing limitation: operational help-center documentation was reachable only for BoardPro in this research pass; OnBoard's support site was unreachable and Diligent/Convene observations rest on official product pages (positioning level). Workflow mechanics confirmed in only one product are therefore described as an implementation pattern rather than an industry standard, and no numeric limits, retention periods or security specifications are asserted. Vendor marketing statistics were excluded from evidence.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
