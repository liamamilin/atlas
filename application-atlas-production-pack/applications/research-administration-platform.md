# Research Administration Platform

## Overview

A **Research Administration Platform** is a research institution's administrative system of record for sponsored research. It carries each funding undertaking as a persistent record — from proposal development and institutional approval, through submission to the sponsor, into award setup and post-award administration of funds, personnel commitments, subawards, and changes — until the project is closed out.

Its purpose is to let the institution — not the individual researcher — act as the administering party of sponsored research: gating what goes to sponsors, holding what sponsors committed, and administering the money and obligations that follow. The defining core is small:

```text
Sponsored project (the institution's record of one funding undertaking)
├── Proposal phase   — what the institution requests from the sponsor
└── Award phase      — what the sponsor committed, administered to closeout
    ├── institutional pre-award loop:  assemble → budget → route → submit → follow up
    └── post-award loop:  set up → track funds/effort/subawards → record changes → close out
```

Everything else commonly associated with these products — system-to-system sponsor submission, effort certification, compliance modules, funding-opportunity search, agreement libraries — is widespread but not what makes the product this Type. Older paper-era research offices, legacy on-prem systems, and non-US regional regimes all fit the same core without any of those specifics.

## Users & Context

The primary users are **research administrators** — staff in departmental research offices and central sponsored-programs / research-services offices. They move proposals through routing, set up awards, track funds, manage subawards, and produce reports. The platform is their daily work surface and the institution's memory of its research portfolio.

**Principal investigators (PIs) and their research teams** are the second primary audience: they author proposals, build budgets, respond to routing requests, and monitor their own awards and spending.

Around them:

- **Approvers in the institutional hierarchy** (department chairs, deans, central research officials) act on proposals routed to them — the institutional sign-off before anything reaches a sponsor.
- **Contract and negotiation staff** track agreements and award terms.
- **Finance offices** are integration counterparts: the institutional general ledger and payroll systems hold the transactions; the platform presents them in research language.
- **Compliance offices** connect through disclosure and protocol records linked to projects.

Typical context: higher education is the dominant market, but teaching hospitals, academic medical centers, research institutes, and nonprofits run the same administration. The common thread is an institution that receives external sponsorship for research and must account for it to sponsors and auditors.

## Core Model

### The Defining Core

**The sponsored project** is the central object: one persistent, identified record of one research funding undertaking, binding the institution's research to an external sponsor and to money terms. It spans two phases held on one record:

- **The proposal** — what the institution requests: the research plan, the budget, the personnel commitments, the institutional assurances. Authored by the researcher in structured forms, but owned and submitted by the institution.
- **The award** — what the sponsor committed: the funded record holding the sponsor's terms and conditions, required deliverables, anticipated and obligated amounts, and the account distributions through which the money becomes spendable. The award links back to the proposal it resulted from.

Two loops move this record through its life:

**The institutional pre-award loop.** The researcher assembles the proposal; the budget is computed under the institution's rate and cost rules; the proposal routes through the institution's review and approval hierarchy; the institution submits it to the sponsor; and post-submission activity (sponsor requests for more information, revised budgets) is tracked on the same record. The routing gate is the point: the proposal is not the researcher's to send — it becomes the institution's submission only after institutional approval.

**The post-award administration loop.** When the sponsor commits, the award is set up as the institution's funded record. From then on the platform administers the award's life: spending tracked against budget, personnel commitments and effort administered, subawards issued and invoiced under the prime award, agreements negotiated, and every change over the award's life — amendments, extensions, rebudgeting — recorded on the award itself, through to closeout.

Remove the sponsored-project record and the loops have nothing to carry. Remove the institutional routing gate and the product becomes the sponsor's application portal or a document editor. Remove the post-award loop and the product is a proposal pipeline with no award memory — or, on the other side, pure grants accounting inside an ERP.

### Standard Capabilities

Mature products commonly add, around this core:

- **Rate-governed budget development** — budget tools that compute from personnel salary data, placeholder positions, direct-cost categories, and the institution's own rates (indirect/F&A, fringe benefits, inflation), for both requested funds and cost share.
- **Configurable routing workflows** — approval chains that mirror the institution's organizational hierarchy, with conditional logic, role-triggered tasks, and notifications.
- **A personal action list** — each user's queue of documents awaiting their action (approve, acknowledge, complete a task), plus a personal view of documents they initiated or submitted.
- **Post-award financial views in research language** — spend versus budget, projections and what-if forecasting, spend-down management, and stakeholder summaries; the institutional ERP/GL/payroll systems remain the transaction substrate, integrated rather than replaced.
- **Subaward administration** — outgoing subaward records linked to the prime award, with subaward invoicing tracked against them.
- **Agreement and negotiation tracking** — contracts, material transfer and non-disclosure agreements, and other award-adjacent agreements held in the same system.
- **Compliance touchpoints** — conflict-of-interest and financial-interest disclosures, export-control reviews, and research-ethics protocol links attached to the project record, usually realized as sibling modules integrated with pre- and post-award data.
- **Role-scoped dashboards and analytics** — administrators see their units' portfolios; PIs see their own projects; leadership sees aggregate trends.
- **Shared master data** — person, sponsor, and subawardee records reused across all modules.
- **Audit-ready record-keeping** — linked attachments, approval histories, and retained records behind every action.

### One Structure, Many Realizations

The core model is conceptual; products realize it differently:

```text
Sponsor submission:   system-to-system submission into sponsor portals (where the
                      regime provides one), or preparation and out-of-system submission
Post-award money:     a fund view computed over the institutional ledger, or a
                      lighter award-financial view fed by finance-system integration
Compliance:           sibling modules in the same suite, or integrations to
                      separate institutional systems
Internal funding:     internal competitions routed like proposals, or institutional
                      funds administered inside the fund view
```

A reader who has only seen one realization (for example, US federal system-to-system submission) should still recognize products built for other regimes from the core model.

## How It Works

### Develop and route a proposal

```text
Researcher creates a proposal in structured forms
→ builds the budget (personnel, costs, institutional rates applied automatically)
→ attaches documents and compliance touchpoints
→ submits for institutional routing
→ approvers act in turn (approve / acknowledge / request changes)
→ institution submits to the sponsor
→ post-submission requests and revised budgets tracked on the same record
```

The routing step is the institutional gate: the platform enforces that the proposal passes the institution's hierarchy before the sponsor ever sees it.

### Set up and administer the award

```text
Sponsor commits → award record created, linked to its proposal
→ terms, deliverables, amounts, and account distributions captured
→ spending tracked against the award's budget (transactions from the institutional finance systems)
→ personnel commitments and effort administered
→ subawards issued under the award and invoiced against it
→ changes over the award's life recorded as modifications
→ closeout
```

The award is a living record, not a filed letter: anticipated and obligated amounts change, accounts are distributed, documents accumulate, and every modification is recorded on the award it modifies.

### Capability tiers

**Defining core** — without these, not this Type:

- the sponsored-project record spanning proposal and award
- the institutional pre-award loop (assemble → budget → route → submit)
- the post-award administration loop (funds, personnel, subawards, modifications, closeout)

**Standard capabilities** — present in most mature products:

- rate-governed budget tools, configurable routing, action lists
- award terms/deliverables/amounts as system of record
- research-language fund views over integrated finance systems
- subaward and agreement administration
- compliance touchpoints, role-scoped dashboards, audit-ready records

**Optional / variant** — depends on regime, segment, and packaging:

- system-to-system sponsor submission machinery (regional)
- effort reporting and certification (regime-dependent)
- funding-opportunity search
- internal funding competitions and institutional funds
- clinical/industry-funded billing flows
- non-research scholarly activity administration

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Administrator worklist / dashboard

The research administrator's primary entry surface.

- lists proposals in routing, awards, funds, subawards, and outstanding tasks for their scope
- surfaces status, deadlines, and next steps per project
- primary actions: open a record, act on a routed item, run reports

### Proposal workspace

The pre-award authoring surface for the researcher and their administrators.

- structured proposal forms with guided navigation and embedded help
- budget editor with the feel of a spreadsheet and the institution's rates applied as computation
- attachments, compliance links, and routing status
- primary actions: edit sections, build/copy budgets, submit for routing, respond to reviewer requests

### Routing / approval queue

The approver's surface — the personal action list of documents awaiting a decision.

- the document's summary, its history, and its attachments
- primary actions: approve, acknowledge, return with comments, complete a task

### Award record

The post-award system of record for one award.

- sponsor terms and conditions, deliverables, anticipated/obligated amounts, account distributions, award documents
- modification history over the award's life
- primary actions: record changes, distribute accounts, attach documents, link subawards

### Fund / spend view

The post-award financial surface, presented in grants-and-contracts language rather than accounting jargon.

- budget versus actual spend, projections, what-if scenarios, transaction review
- primary actions: review transactions, forecast, generate financial summaries

### Subaward and agreement surfaces

- outgoing subaward records linked to their prime award, with invoicing status
- agreement records (contracts, MTAs, NDAs) with negotiation activity and review routing

### Effort / certification surface (where the regime requires it)

- personnel commitments against projects, payroll-derived effort data, certification routing

### Reports / analytics

- role-scoped dashboards over the portfolio: submission volumes, award pipeline, spend status, compliance posture

## Important Rules / Behaviors

### The institution is the applicant

Proposals do not go to sponsors from the researcher's desk. The platform enforces institutional routing and approval before submission — this is the structural reason the platform exists, and the step that makes the record the institution's rather than the individual's.

### Budgets are computed, not typed

Proposal budgets are derived from personnel salary data and institutional rate tables (indirect-cost, fringe-benefit, and similar rates), for both requested funds and cost share. Changing a rate or a salary ripples through the budget — the budget is an output of configured rules as much as an input to the sponsor.

### The award is a living record

Awards change over their life: amounts are adjusted, accounts redistributed, terms amended, extensions granted. These are recorded as modifications on the award, preserving the history — the award record, not a document folder, is what the institution audits against.

### The ledger stays in the finance systems

The platform presents money in research language — funds, awards, spend-down, projections — while the institutional ERP/GL/payroll systems remain the source of transactions. Integration, not replacement, is the normal relationship; a platform that tried to be the general ledger would be drifting into ERP territory.

### Subawards hang off the prime award

Outgoing subawards are records linked to the award that funds them, and their invoicing flows back through that award. The prime-award/subaward relationship is structural, not incidental.

### Visibility is role-scoped

PIs see their own projects; department administrators see their units; central offices see the institution's portfolio. The same role-scoping governs who can act — approve, modify, submit — at each stage.

### Audit-readiness is a standing property

Records, attachments, approvals, and histories are retained and organized for audit and sponsor reporting. This is not a reporting feature bolted on at the end; it is the reason the workflow keeps everything on the record.

## Variants

- **Packaging** — full connected suites (research administration plus compliance and adjacent lines), single products chosen à la carte, or institutions extending the platform with their own forms and workflows for local processes (gift routing, facility use, eligibility, closeout checklists).
- **Regional regime** — US federal-heavy machinery (system-to-system submission, federal forms, effort certification) versus other national regimes with their own sponsor portals and costing rules; the core loop is regime-independent, the submission and certification machinery is not.
- **Institution scale and office structure** — large research universities with high proposal volume and centralized offices, versus institutions with emerging research programs and small teams; decentralized institutions route through semi-autonomous units.
- **Funding-type breadth** — grants and contracts only, versus portfolios that also include institutional funds, philanthropic funds, clinical income, and industry-funded clinical trials administered in the same fund view.
- **Scope of "research"** — some institutions also administer training, public-service, and other scholarly activities in the same system.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Research Grant Management | near-sibling (likely overlapping population) | the market uses "research administration" and "grant management" for the same systems; this leaf is defined as the institution-wide platform spanning the full sponsored-research lifecycle — the boundary deserves a joint review |
| Research Information Management / CRIS | adjacent | CRIS holds the institution's research information (publications, activities, expertise); this Type holds its funding undertakings; awards feed CRIS, not the reverse |
| Research Funding Discovery Platform | capability-adjacent | opportunity search is commonly bundled here but is not the defining structure; discovery products hold opportunity databases without proposal/award records |
| IRB / Research Ethics Management; Animal Research Ethics / IACUC; Research Compliance Management | sibling modules | committee review over protocols versus administration of funding; suites ship both and integrate them (disclosures, protocol links, congruency checks) |
| Government Grants Management | counterpart side | the sponsor/funder's own intake, review, and award machinery; the proposal crosses between the two systems |
| Grantmaking Platform | counterpart side | foundations administering money they give out, versus the institution administering money it receives for research |
| Nonprofit Grant Management | adjacent grantee-side | grants funding program delivery, versus grants funding research; research-specific machinery (effort, subawards, sponsor terms, research compliance) marks this Type |
| ERP / Financial Management | integration substrate | the ledger and chart of accounts live there; this Type holds the award/fund view in research language over that substrate |
| Research Project Management | different object | managing the research work itself (tasks, milestones, scientific progress) versus administering the funding wrapper around it |
| Clinical Trial Management System | different object | trial conduct versus the funding and administration wrapper (clinical trials appear here as a funding type) |

The most important boundary is the sponsor-side one: the same transaction — a proposal in, an award out — is administered by two different systems on two sides. This Type is the institution's side.

## Representative Products

- Cayuse (Award Management: Sponsored Projects, Proposals (S2S), Fund Manager, Project Effort, Agreements, Insights)
- Kuali Research (Sponsored Programs and its sibling compliance products)

The core model was checked against the market's own category language ("research administration", "pre-award to post-award grant management", "research lifecycle management") as used by both sampled vendors. Other known vendors in this market (legacy enterprise suites, UK/EU regional platforms, ERP-embedded grants modules) could not be verified during research and are not characterized here.

## Sources

Research date: **2026-09-09**

- Cayuse — Sponsored Projects: https://www.cayuse.com/sponsored-projects/
- Cayuse — Award Management: https://www.cayuse.com/award-management/
- Cayuse — Proposals (S2S): https://www.cayuse.com/award-management/proposals-s2s/
- Cayuse — Fund Manager: https://www.cayuse.com/award-management/fund-manager/
- Cayuse — The Cayuse Suite: https://www.cayuse.com/the-cayuse-suite/
- Kuali — Research Administration: https://www.kuali.co/products/research
- Kuali — Sponsored Programs: https://www.kuali.co/products/sponsored-programs
- Kuali Help Center — "What is Kuali Research?": https://kuali.zendesk.com/hc/en-us/articles/27090467314075-What-is-Kuali-Research
- Kuali Help Center — "Navigating Kuali": https://kuali.zendesk.com/hc/en-us/articles/40899745658651-Navigating-Kuali

> Sourcing limitation: several other vendors in this market (Huron Research Suite, InfoEd, Worktribe, Aurora, ResearchMaster) and the US sponsor-side portal Grants.gov were not reachable from the research environment on 2026-09-09. The verified sample is two US-origin commercial suites; claims about the broader market are calibrated accordingly, and precise operational details (routing step taxonomies, rate tables, validation catalogs, closeout checklists) are intentionally not stated. Such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
