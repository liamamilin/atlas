# Corporate Governance Platform

## Overview

A **Corporate Governance Platform** is the system of record for an organization's governance function: the work of its board of directors and governing committees, plus the standing governance program that surrounds that work — the legal entities being governed, the people who govern them and their terms, and the recurring governance obligations (director & officer questionnaires, board evaluations, conflict-of-interest disclosures) that run on an annual rhythm alongside the meeting cycle.

In the market this is the same software category buyers most often call *board management software* or a *board portal*. The directory carries the category under two names — **Board / Corporate Governance Platform** (documented separately) and this leaf — and research confirms they name one Type: every product sold as a "corporate governance platform" centers on the governed-body meeting cycle described below, and the governance program is sold as the layer around it. What the "corporate governance platform" label emphasizes is that layer: at the enterprise pole, the meeting cycle ships together with entity governance, governance people data, questionnaires, evaluations, and disclosures as one integrated suite, and the widest packaging merges the whole thing into a governance-risk-compliance umbrella.

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

Around this core, the governance program adds the structures and obligations that make governance a year-round managed function rather than a sequence of meetings. Remove the meeting cycle entirely and what remains — entity records, officer registers, filing deadlines — is a different category (entity management); remove the governance program and what remains is the pure board portal.

## Users & Context

The software serves a small, named population with sharply asymmetric roles:

**Primary operator** — the *corporate secretary*, *governance manager*, or *board administrator* (in public-sector and nonprofit settings, the *board clerk*). This role runs both loops of the system: the recurring meeting cycle (scheduling, agendas, packs, minutes, actions) and the annual governance rhythm (questionnaire campaigns, evaluations, disclosure cycles, the governance calendar). In suite deployments the same role often also maintains the entity and officer records.

**Governance team / general counsel** — in enterprise deployments, the legal and governance team that owns the governance program: subsidiary structures, officer appointments, disclosure obligations, and the policies the board oversees. They are the main consumers of the entity register and the questionnaire/evaluation machinery.

**Primary consumers** — *directors, trustees and committee members*: senior, time-poor, often non-technical. They read the pack, annotate, vote, sign — and, distinct from the pure board portal, they are also the *respondents* of the governance program: each director completes a D&O questionnaire annually, participates in evaluations, and files conflict-of-interest disclosures through the same platform.

**Secondary participants** — the *chair* (signs minutes, controls proceedings), *executives* (present items, supply papers, and are themselves evaluated in some programs), and — in the corporate-service-provider variant — the provider's staff who run governance for many client boards on one platform.

The usage rhythm has two clocks. The **meeting cycle** recurs monthly or quarterly per body. The **annual governance rhythm** runs on the governance calendar: questionnaires collected ahead of disclosure season, evaluations run once a year, entity filings and renewals tracked against jurisdictional deadlines. Both clocks converge on the same records.

## Core Model

### The defining core

**Governed body.** The organizing container is the board or committee — a named governing body of the organization (main board, audit committee, remuneration committee; in larger deployments, subsidiary and affiliate boards). Each body has an identified member roster: directors or trustees with roles and terms. The body scopes everything else — who receives which pack, who may vote, whose record this is.

**Meeting.** The unit of governance work is the meeting: a dated, scheduled occasion of a specific body, with attendees, location or remote link, and a lifecycle from scheduling through materials and conduct to confirmed minutes. Meetings recur on a calendar; past meetings accumulate into the body's institutional memory.

**Agenda.** The agenda structures the meeting into sections and items, each with a presenter, an allocated time, and the papers attached to it. It is drafted, reviewed, and published as the official notice of business.

**Board pack.** The board pack (board book) is the curated set of meeting materials assembled against the agenda — the agenda plus the documents attached to each item, compiled into a single paginated volume and distributed to the body's members. Distribution is member-scoped and confidential: access is controlled per person and per document, and materials live inside the platform rather than as email attachments. This is the property the category was created to deliver.

**Governance record.** The meeting produces the record: minutes drafted against the agenda, with recorded decisions, resolutions, votes and action items. Minutes go through review, are confirmed — typically at the subsequent meeting — and the confirmed record is retained permanently as the body's official account. Past packs, minutes and policies accumulate into a searchable governance library.

### The governance program around the core

Mature governance suites commonly carry the following structures alongside the meeting core. They are what the "corporate governance platform" packaging adds; a pure board portal may ship without several of them.

- **Entity & subsidiary governance.** A centralized corporate record for each legal entity the organization operates: registration and jurisdiction details, officers and directors, ownership relationships, structure charts, and the entity's own document set (constitutive documents, minute books, resolutions). Compliance deadlines and filing obligations attach to each entity and are tracked as tasks. In suite deployments this register is the bridge between the board's work and the legal reality it governs: the directors recorded on board rosters are the same people recorded as officers of entities.
- **Governance people data.** Directors and officers held as governed records — roles, classes, appointment and term dates, skills, and (in some products) diversity attributes — so that composition, tenure and succession questions are answerable from the system rather than from spreadsheets.
- **Governance questionnaires.** Recurring per-person collection campaigns, most prominently the **director & officer questionnaire**: each year every director and officer discloses interests, affiliations, independence and related matters through a form distributed and completed inside the platform, with responses aggregated for disclosure and regulatory use. Compliance questionnaires generalize the same machinery to other regulated data collection.
- **Board evaluations & assessments.** Structured evaluation cycles over the board, its committees, individual directors, and (in some suites) executive management: questionnaires distributed, responses collected, and results reported — normally in aggregate — as actionable insight for the following year.
- **Conflict-of-interest machinery.** Disclosure collection and review: interests declared by directors and officers, held in registers, reviewed, and where needed escalated — connected to the meeting record when a conflicted matter arises.
- **Governance calendar.** The annual plan that sequences the whole program: meeting schedule, questionnaire windows, evaluation cycles, disclosure deadlines, and entity filing dates in one view, so the governance function's obligations are visible and owned.
- **Governance intelligence & education** (suite pole). At the widest packaging, the platform adds curated external data — shareholder activity, compensation benchmarks, governance research — and structured board education, feeding the board's own oversight work.

### How the layers relate

```text
Governance calendar (the annual rhythm)
├── Meeting cycle  ← the defining core (bodies, meetings, packs, records)
├── Questionnaire campaigns (D&O, compliance) → aggregated disclosures
├── Evaluation cycles (board / committees / directors / management)
├── Conflict-of-interest disclosures → registers → review
└── Entity governance (records, officers, filings, deadlines)
        └── feeds the people data the meeting cycle and disclosures draw on
```

The same person appears in every layer — as a member of the roster, a respondent to the questionnaire, a subject of the evaluation, an officer of an entity. The platform's value is that these appearances are one governed record, not four disconnected lists.

## How It Works

### The meeting cycle

The core loop repeats for every meeting of every body:

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

The mechanics — pack compilation and versioning, annotation-preserving replacement, the minutes confirmation gate, action tracking — are the board portal's stock in trade and are described in depth in the paired research for the sibling leaf.

### The annual governance rhythm

Once a year (per program), the platform runs collection campaigns that follow a common shape:

```text
Configure the campaign (questionnaire or evaluation form, respondent list, window)
→ Distribute to each director / officer / participant
→ Respondents complete securely inside the platform
→ Administrator monitors completion, chases outstanding responses
→ Responses aggregate into reports (disclosure-ready or evaluation-ready)
→ Results inform the board's disclosures, composition and development decisions
→ Retained as part of the governance record
```

The D&O questionnaire campaign is the signature instance: an annual obligation for most governed organizations, per-person confidential, with aggregated output used for public disclosure and regulatory filings. Board evaluations follow the same machinery with a different instrument and an aggregate-only reporting posture.

### Entity governance loop

Between board cycles, the entity register is maintained:

```text
Entity created or acquired → corporate record opened
→ Officers/directors appointed (linked to governance people records)
→ Filings and renewals scheduled against jurisdictional deadlines
→ Changes recorded (appointments, resignations, ownership) with attribution
→ Structure charts and reports generated from the live record
→ Deadlines tracked to completion
```

When a board resolution affects an entity — an appointment, an approval, a structural change — the resolution recorded in the meeting cycle and the entity record updated in the register describe the same event from two sides; mature suites connect them.

## Interfaces

Three surface families face the three populations.

### Governance team console (web)

The operator's workspace, spanning both clocks:

- **Meetings & calendar** — all bodies' meetings with their stage; the annual governance calendar overlaying questionnaires, evaluations and filing deadlines.
- **Agenda & pack builders** — sections, items, presenters, attachments; compile, republish, version history, read receipts.
- **Minutes workspace** — per-item notes, decisions, actions, votes; review circulation; confirmation and signing.
- **Entity register** — entity profiles, officers and directors, structure charts, document sets, compliance tasks and deadlines.
- **Campaign consoles** — questionnaire and evaluation setup, distribution, completion tracking, aggregation and reporting.
- **Registers & library** — interest/conflict registers, decision register, action list, policies and past records.

### Director & officer surface (app / tablet / web)

Deliberately simple, and now the respondent surface too:

- **Home / meetings** — upcoming meetings, current pack, outstanding actions and approvals.
- **Pack reader** — paginated pack with agenda navigation, personal annotations, search.
- **Questionnaires & evaluations** — the respondent's forms for the annual campaigns, completed in the same place they read their packs.
- **Voting & signatures** — cast votes, sign minutes and documents.

### Entity & structure views

Read-mostly surfaces over the corporate record: entity profile pages, ownership and governance structure charts, officer listings, deadline dashboards — used by the governance team, and increasingly self-served by adjacent functions (finance, tax, legal operations) under permissioned access.

## Important Rules / Behaviors

**Confidentiality is member-scoped and revocable.** Permissions attach to the body and the person; a paper can be restricted to a subset of members; access can be revoked at any time. The category's standing promise is that board materials never travel as email attachments and never leave stray copies. Questionnaire responses inherit the same posture — a director's disclosure is visible to the governance function, not to the whole board.

**Published materials are versioned, never overwritten.** Republishing after a late change produces a new pack version; the original is retained and changes are logged. Directors must be able to rely on what they read, and auditors must be able to see what changed and when.

**The confirmed record is final.** Minutes move through draft and review to confirmation — typically at the subsequent meeting — after which the meeting is locked so the approved record cannot silently change. Votes, signatures and access events are logged and attributable.

**Campaign responses are per-person confidential, aggregated in reporting.** Questionnaire and evaluation machinery distributes one instrument per respondent and reports in aggregate (evaluations) or in controlled disclosure form (D&O data). Individual evaluation responses are not exposed as peer-readable records.

**The entity record is the source of truth.** Officer and director data in the entity register is maintained as the authoritative corporate record; changes are attributed and dated. Where the meeting cycle and the register describe the same event (a board appoints a director), mature suites link the resolution to the record change rather than maintaining two divergent accounts.

**Obligations are calendar-driven.** Questionnaire windows, evaluation cycles, disclosure deadlines and entity filings are scheduled objects with owners; the governance calendar makes an unowned obligation visible as a gap.

**Director adoption constrains design.** The consumer surface must be usable by senior, non-technical members without training — now extended to questionnaire and evaluation respondents. Complexity concentrates in the governance team console.

## Variants

- **Pure-play board portal** — the meeting cycle alone; the entry pole of the category and the form most mid-market and SMB buyers purchase.
- **Governance suite** — the meeting cycle plus the governance program (entities, questionnaires, evaluations, disclosures, calendar) as one platform; the form the "corporate governance platform" label usually denotes.
- **GRC umbrella** — the governance suite merged with risk, compliance and audit applications under one vendor platform; the widest packaging, in which governance is one category among several.
- **Lifecycle packaging** — programs tuned to pre-IPO, private-company and public-company stages, where disclosure obligations scale with the stage.
- **Industry editions** — banking, insurance, healthcare, higher education, private equity, law firms, fund administration, nonprofits: the same core with industry-tuned security, residency and questionnaire content.
- **Public sector** — school boards, councils and public bodies: the meeting cycle plus a public transparency site, livestreaming and accessibility compliance.
- **Association / nonprofit audience** — the same core applied to association boards and committees (documented as the sibling audience variant).
- **Entity-management-led packaging** — the corporate-secretarial family that centers entity records and obligations without the meeting cycle; adjacent category, sometimes branded with governance vocabulary.
- **Corporate service provider model** — one platform administering governance for many client organizations.
- **Regional deployments** — data-residency commitments and national digital-identity integrations for signing and authentication.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Board / Corporate Governance Platform | **same Type — alias leaf** | research confirms both directory names resolve to one category; the sibling leaf documents the meeting-cycle core in depth, this leaf adds the governance-program layer; merge or explicit split recommended at joint review |
| Committee / Board Management | audience variant | identical core applied to association boards and committees; vocabulary changes, structure does not |
| Legal Entity Management | adjacent, frequently bundled | centers the legal entity record (registrations, officers, equity, filings) with no governed-body meeting cycle; appears inside governance suites as the entity-governance module; remove the meeting cycle from this Type and the remainder is this category |
| Entity Compliance Management | adjacent | centers entity-level obligation tracking (filings, renewals); one slice of the entity-governance module here |
| Governance Risk & Compliance Platform | adjacent umbrella | centers enterprise risk, compliance and audit programs; the widest governance packaging absorbs it, but the governed-body governance work and the GRC program remain distinct centers |
| Legislative Management System / Government Meeting & Agenda Management | adjacent, overlapping in public sector | organized around the public legislative/clerk workflow (readings, ordinances, public comment) rather than a governed body's confidential meeting cycle; public-sector board portals sit between the two |
| Virtual Data Room | adjacent | document sharing with external parties for a transaction; no governed body, no recurring cycle, no official record |
| Enterprise Content Management | broader | organization-wide content lifecycle; the governance library here is a bounded repository for one function |

The two most important boundaries. Against **board management software**: same Type — the label difference marks the governance program, not a different category. Against **entity management**: the governed body is the seam — entity registers without bodies and meetings are a different category, however much governance vocabulary they borrow.

## Representative Products

- **Diligent One Platform** (Diligent) — the enterprise governance umbrella: board management (Diligent Boards, BoardEffect, Diligent Community) plus entity management, market intelligence, and governance-program modules (conflict-of-interest, policy), extendable into full GRC.
- **Nasdaq Boardvantage / Nasdaq Governance Solutions** (Nasdaq) — the governance suite with the cleanest taxonomy: board management + board evaluations & assessments + D&O and compliance questionnaires + governance community, packaged by lifecycle and industry.
- **OnBoard** (Passageways) — mid-market board platform whose "governance system of record" pillar carries the program layer (D&O questionnaires, assessments, roles & terms, skills tracking) inside a meeting-centric product.
- **BoardEffect** (Diligent) — nonprofit and higher-education tier of the same category; shows the program layer scaled to mission-driven boards.

The paired research notes also sampled entity-management software (branded around "governance operations") as the boundary pole establishing that a governance-branded product without a meeting cycle belongs to Legal Entity Management, not this Type.

## Sources

Research date: **2026-09-07** (OnBoard observations carried from the sibling pass of 2026-09-06)

- Diligent — Diligent One Platform page: https://www.diligent.com/platform/
- Diligent — Diligent Entities product page: https://www.diligent.com/products/entities/
- Nasdaq — Governance Solutions category page: https://www.nasdaq.com/products/governance
- Nasdaq — Boardvantage product page: https://www.nasdaq.com/solutions/boardvantage
- OnBoard — product/platform pages: https://www.onboardmeetings.com/ (fetched 2026-09-06)
- Athennian — product page (boundary-pole evidence): https://www.athennian.com/
- Sibling leaf research: research/board-corporate-governance-platform.md and applications/board-corporate-governance-platform.md (2026-09-06)

> Sourcing limitation: no operational help-center documentation was reachable/fetched for the governance-program modules in this pass; all observations rest on official product and platform pages (positioning level), and OnBoard detail is carried from the earlier pass's homepage navigation. Claims about module mechanics are therefore written at capability level, not workflow level; no numeric limits, retention periods or security specifications are asserted, and vendor marketing statistics were excluded from evidence.

Detailed product-by-product observations, the cross-product comparison matrix, the alias analysis against the sibling leaf, and the boundary tests are recorded in the paired Research Notes.
