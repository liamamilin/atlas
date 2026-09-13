# Author Management Platform

## Overview

An **Author Management Platform** is publisher-side software for managing a publishing organization's ongoing relationship with the people who create the works it publishes. It keeps identified records for authors and contributors (and their representatives, such as agents and literary estates), attributes them to the publisher's works with credited roles, records the contractual terms under which each work is published — rights granted, remuneration, payees and payment shares, advances — and operates the recurring settlement loop: sales data comes in, amounts owed to each author are computed under the contract's terms, statements are issued, and payments are tracked.

The defining core is deliberately small:

```text
Creator registry (identified authors/contributors — persons or organisations — plus representatives)
└── Work attribution (creator ↔ the publisher's works, with attributed roles)
    └── Contract record (per work: rights granted, remuneration, payees and shares)
        └── Settlement loop (sales intake → amount-owed calculation → statements → tracked payments)
```

Everything else commonly associated with the category — royalty escalators, reserves against returns, supply-chain contributor feeds, author self-service portals, rights-income tracking — is a standard capability layered on this spine, not part of what makes the software "author management." Older publishing operations ran the same four-part structure with card files, contract folders, and periodic royalty ledgers; modern products digitize it.

When the software's center of gravity shifts — to the work's bibliographic data rather than the money relationship, to the production lifecycle of titles, or to royalty recipients who need not be authors at all — it is functioning as a different Application Type (Publishing Metadata Management, Publishing Editorial Workflow, Royalty Management Platform).

## Users & Context

The operator is the publisher; the managed population is **external** — authors are not employees, and the only surface most of them ever touch is a recipient portal, if one is offered.

Primary internal users:

- **contracts and royalty managers (finance)** — record contract terms, run the settlement cycle, issue statements, track payments and balances
- **editors / acquisition staff** — create and maintain author records, manage the working relationship, track manuscript delivery commitments
- **rights managers** — record rights granted per work, manage subsidiary/foreign-rights deals whose income flows to the same payees

Secondary users:

- **metadata/bibliographic staff** — maintain the public-facing contributor records (credited names, roles, biographical notes) that flow to the book supply chain
- **accounting** — receives settlement results and payment data into the wider finance systems

Typical organizational context: book publishers of all sizes — trade, academic and university presses, children's, religious, educational — as well as book packagers and hybrid publishers. The same software category also serves literary and rights agencies (in an agency-side configuration where authors are clients rather than counterparties), and royalty-specialist products generalize the same machinery to licensors in other industries.

## Core Model

### The Defining Core

Four structures. Each answers a question the publisher must be able to answer at any time: *who are our authors, what did they write for us, on what terms, and what do we owe them?*

- **Creator registry** — every author or contributor is an identified record: a person or an organisation, with contact details, notes, and relationships. Records are shared across the whole system: the same record appears as the credited contributor on a work, the recipient of a statement, and a contact in the address book. Representatives — literary agents, estates — are typically records too, because they can be payment recipients without being credited contributors.
- **Work attribution** — creators are linked to the publisher's works (titles) with an attributed role ("author," "editor," "illustrator," "translator") and, commonly, a display order for public presentation. One person accumulates many work links over time; this accumulation is the author's history with the publisher.
- **Contract record** — for each work, the commercial terms of its publication: which rights the creator grants the publisher (often by territory), how remuneration is calculated (the royalty basis and rates), who the payees are and how the payment is divided among them, and what advances have been promised. Some products generate contract documents from this data; others store signed copies alongside structured terms. Either way, the terms exist as data, because the settlement engine consumes them.
- **Settlement loop** — the recurring operating cycle of the Type. Sales (and returns) data is imported from distributors and sales channels; amounts owed are computed per contract terms for the period; statements are produced per payee; payments are made and recorded; balances, advances, and held-back reserves carry forward to the next period.

### Capabilities Shared by Mature Products

These are widespread in current products but are not what makes the software author management:

- **Remuneration mechanics** — tiered rates and escalators (rate changes triggered by units sold, sales value, elapsed time, or discount level), rates scoped per edition/format, sales channel, or territory; reserves against returns (a share of royalties held back and released over later statements); withholding/tax settings per payee.
- **Advances** — recorded as instalments with trigger events (for example, on signature, on delivery, on publication) and tracked from promised to paid.
- **Sales intake** — import of sales and returns from multiple distributors and formats, in multiple currencies.
- **Statement machinery** — calculation runs and statement batches with review before issue; statement history per recipient; balances and unearned advances as standing reports.
- **Non-credited payees and splits** — payment shares defined per payee, so an agent or estate can receive part of a work's royalty income without appearing as its credited author.
- **Rights income** — subsidiary/foreign-rights deals recorded against works, with license income feeding the same payees and statements.
- **Contributor metadata for the supply chain** — credited names, roles, ordering, and biographical notes maintained as public-facing data (in book publishing, delivered to retailers and data agencies via ONIX feeds).
- **Recipient portal** — a self-service surface where authors and agents view current and past statements, receive and store contracts and documents, receive messages, and update their own contact details. Common in current products, though not universal.
- **Housekeeping and audit** — record deduplication, activity notes, calculation auditability, and handoff of payment data toward accounting/ERP systems.

### One Structure, Many Implementations

The core model is written conceptually; concrete products realize each piece differently:

```text
Concept:            Creator registry
Implementations:    shared address book of person/organisation contacts;
                    "royalty recipient" files; imported author lists

Concept:            Contract record
Implementations:    structured contract editor generating PDF documents;
                    stored signed copies plus rule configuration

Concept:            Settlement engine
Implementations:    batch runs with analysis and approval steps;
                    one-button calculate-and-issue cycles

Concept:            Author-facing surface
Implementations:    emailed PDF statements; secure online portals
```

A reader who has only seen one implementation — say, a suite where author management is one module among many — should still be able to recognize a royalty-only product paying authors under the same model.

## How It Works

### Bring an author into the system

```text
Create (or import) a person or organisation record
→ link the record to the work with a credited role
→ record the contract: rights, rates, payees and shares, advance instalments
→ track contractual milestones (e.g., manuscript delivery) alongside the work's production
```

Vendors describe onboarding for migrating publishers in exactly this triad: authors, titles, contracts — then sales data.

### Attribute and maintain the public identity

The credited name, role, order, and biographical note attached to each work feed the publisher's public metadata. Where credited identity and payee identity differ — a pseudonym, or an agent collecting on behalf of an author — some products keep separate records: the credited one for public surfaces, the payee one for money.

### Operate the settlement cycle

```text
Import sales and returns for the period
→ run the royalty calculation over the affected works
→ review the results
→ generate statements per payee
→ deliver statements (email and/or portal)
→ record payments made
→ carry balances, unearned advances, and reserves forward to the next period
```

This cycle repeats for the life of each contract — commonly for years after publication — which is why the loop, not any single statement, is the Type's operating heart.

### Maintain the relationship between cycles

The system doubles as the publisher's memory of the relationship: correspondence, notes, documents (signed contracts, addenda), contact details, and — where a portal exists — a channel for announcements and document delivery that reduces ad-hoc inquiries from authors.

## Interfaces

Described conceptually; names and layouts vary by product.

### People / address book

The registry surface.

- person and organisation records with contact details, notes, categories/tags
- derived views such as "contributors," "payees," or agency "clients"
- primary actions: create/import records, deduplicate, link to works, add notes

### Work page — contributions section

Where attribution happens.

- the work's credited creators with roles, order, and public metadata
- primary actions: add/attach a contributor with a role, edit biographical notes, reorder credits

### Contract editor

The commercial-terms surface, usually the densest screen in the product.

- terms, rights granted, royalty rate rules, payees, payment shares, advances, reserves
- contract documents (generated PDFs or stored signed copies)
- primary actions: enter/edit terms, record advance instalments and paid dates, attach documents

### Settlement consoles

- calculation runs (per period, over selected works) and statement batches (per payee)
- review screens before approval; statement previews
- primary actions: create run/batch, review, approve, generate, deliver

### Statement output and recipient portal

- the statement itself: earnings by work and rate rule, advances and reserves applied, balance carried
- portal (where offered): current/past statements, contracts and documents, messages, self-service contact updates — accessible to authors and agents without staff involvement

### Reports

- balances and accruals, payment history, per-author and per-title earnings; export toward accounting systems

## Important Rules / Behaviors

### The credited author and the payee are not necessarily the same record

Agents and literary estates commonly receive part or all of a work's royalty income. The system must therefore track, per work, *who is paid* separately from *who is credited* — the structural reason both concepts exist in every researched product.

### Rate rules are conditional and scoped

A work's royalty rate is rarely a single number: rates vary by edition/format, channel, territory, and by escalator conditions (units, value, time, discount). More specific rules override general ones. This is the machinery the contract record encodes and the settlement engine consumes.

### The settlement engine carries state forward

Advances paid, prior payments, and held reserves are not per-period events but running balances. A payment made outside a statement still needs to be recorded in the system, or the next period's balances will be wrong; reserves released in later statements supplement newly earned royalties. Statements are consequently cumulative documents, and mature products emphasize their auditability.

### Statements are per-payee, and their issue is a controlled event

Calculation results are reviewed before statements are finalized; the statement date fixes the period. Once issued, a statement is a financial document toward the author — products treat issue, delivery, and archiving as deliberate steps, not side effects.

### Public metadata is a contract-adjacent obligation

Credited roles and their order flow to the supply chain and shape how the world sees the author's contribution; some products carry the credited order into retail-facing feeds, because errors there are publicly visible and contractual-adjacent.

### Authors touch the system rarely — and on their own terms

Unlike employee-facing systems, the managed population is external. Self-service portals exist precisely because the relationship is intermittent: an author may interact only a few times a year, and the portal must make those interactions (statement lookup, contact update) staff-free.

## Variants

- **Author management inside a publishing-management suite** — the dominant packaging: author/contract/royalty functionality alongside bibliographic metadata, production, rights, and sales in one system.
- **Royalty-specialist configuration** — settlement-first products, sometimes generalized to non-author royalty recipients (inventors, licensors, franchisees) across industries; when scoped to publishing they act as the settlement engine of this Type.
- **Title-management-centric configuration** — contributor records managed primarily as supply-chain metadata, with settlement as an attached module.
- **Agency-side configuration** — literary/rights agencies operate the same machinery with authors as *clients*: submission tracking, incoming royalty capture, client reporting and client portals.
- **Deployment variants** — cloud SaaS versus self-hosted/local installation; the latter is marketed on data-custody grounds (sensitive contract and sales data stays in-house, only finished statements are published to the portal).
- **Segment calibrations** — trade versus academic publishing (open-access works change the money model), children's and illustrated (many small rights and contributors), religious and educational; scale from single-imprint independents to multinational feed operations.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Royalty Management Platform | closest sibling; gradient | the settlement engine generalized to any royalty recipients; author management adds the author registry, work attribution, and relationship surface around it |
| Book Publishing Management | containing suite | bundles author management with bibliographic, production, rights, and sales operations; author management is its people-and-money layer |
| Publishing Metadata Management | adjacent | manages titles and contributor records for the supply chain, without the contract/settlement relationship |
| Publishing Editorial Workflow | adjacent, upstream | acquisition, submissions, and production lifecycle of works; authors appear as counterparts before contracts exist |
| Creator CRM | different population | manages social creators and sponsorships/audiences, not contracted authors under rights-and-royalty terms |
| Talent Agency Management | different operator | agency suites manage talent clients and bookings; the agency-side configuration of this Type instead tracks authors' published works and incoming royalties |
| Academic Journal Management | different habitat | manages scholarly author accounts for manuscript submission and peer review, without author contracts or royalties |
| Accounting / Payroll systems | downstream | record payments owed to internal or external parties generically; they do not model rights grants, contract-driven royalty calculation, or contributor attribution |

The most consequential boundary is with **Royalty Management Platform**: every royalty system researched here pays authors under author contracts, and every author-management implementation researched here is settlement-centric. The working distinction — author registry and relationship surface versus generalized recipient population — deserves joint review when that sibling leaf is processed.

## Representative Products

- **Consonance** — all-features publishing enterprise management SaaS (UK); contracts, royalties, rights, contacts, and metadata in one system
- **Stison** — modular publishing management suite (UK): Title Manager, Royalties Manager, Rights Manager, Production Manager
- **MetaComet Systems** — royalty-first specialist suite (US): Royalty Tracker, Sales Aggregator, Rights, and the author-facing Royalty Portal; also serves non-publishing royalty industries
- **EasyRoyaltiesPlus / RIGHTS 20|20 (Book Matters)** — royalty accounting with rights modules and the ROL author/agent portal (US); self-hostable deployment; agency-side configurations under the same ecosystem

The defining core was checked against the historical practice of publishing operations (pre-digital contract files and royalty ledgers) and against non-publishing royalty systems, to avoid defining the Type by any single era or packaging style. Enterprise on-premise publishing systems could not be verified in this research pass (see Sources) and are deliberately not characterized.

## Sources

Research date: **2026-09-06**

- Consonance — https://consonance.app/ (product overview); user documentation: https://consonance.app/docs/ incl. "About royalties," "Add contributors to a work," "Edit a contract," "Add a contact" (fetched 2026-09-06)
- Stison — https://www.stison.com/ incl. Title Manager and Royalties Manager product pages (fetched 2026-09-06)
- MetaComet Systems — https://metacomet.com/ incl. Royalty Tracker and Royalty Portal product pages (fetched 2026-09-06)
- Book Matters LLC — https://www.easyroyalties.com/ (EasyRoyaltiesPlus / That's Rights! / ROL Royalty Portal product pages, fetched 2026-09-06)

> Sourcing limitation: Ingenta BiblioSuite (enterprise publishing-system tier) returned HTTP 403 on two attempts and was abandoned; the Stison knowledge base was unreachable (transport error). Evidence for three of the four products is therefore official product pages rather than operational help centers; Consonance supplies the operational-documentation depth. Precise operational facts (default statement frequencies, exact rate syntaxes, plan mechanics, vendor-published customer counts) are not asserted in this document; detailed observations and uncertainties are recorded in the paired Research Notes.
