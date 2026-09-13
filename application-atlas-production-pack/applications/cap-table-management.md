# Cap Table Management

## Overview

A **Cap Table Management** application is a company-side system of record for corporate equity ownership — the software equivalent of the capitalization table. It records who owns the company (stakeholders), what ownership instruments the company has created (shares, option grants, convertible instruments), who holds how much of which instrument under what terms (holdings), and the ownership percentages derived from all of it. The record persists and is updated over time as ownership changes through recorded equity events.

Its reason to exist is that a growing company's ownership is too complex and too consequential to track in a spreadsheet: financings create new share classes, employee equity adds grants and vesting, convertible instruments convert into shares, people join and leave, and every one of these changes must be reflected accurately — because the same record informs fundraising dilution, board decisions, employee transparency, tax filings, and audit.

The boundary: this type maintains **one company's equity record** and serves the company that operates it. Distribution of information *to* investors is a surface built on the record (and has its own type, the Investor Portal); fund-level investor accounting is a different subject entirely (Fund Administration).

## Users & Context

**Primary operators (company side):**

- **Founder / CEO** — sets up the record at incorporation, watches ownership and dilution, models a raise before negotiating it.
- **CFO / finance lead** — maintains day-to-day accuracy, runs the equity expense and valuation reporting cycles, prepares audit and board materials.
- **In-house or external counsel** — structures share classes and grants, drives the document and signature flows, checks issuance compliance.

**Record subjects (portal side):**

- **Employees** — see their grants, vesting progress, and documents; request option exercises.
- **Investors** — see their holdings in the company; receive updates and documents the company chooses to share.

**Typical context:** from incorporation (founder shares) through first hires (option pool, first grants), seed financings (often convertible instruments), priced rounds (new preferred classes), growth (secondary sales, larger plans), to exit or IPO readiness. Venture-backed companies are the heartland, but the record type applies to any private company with more than a trivial ownership structure, including LLCs and family companies.

## Core Model

### The defining core

```text
Issuing company (the subject of the record)
├── Stakeholders — identified holders: individuals and entities
├── Securities — the ownership instruments the company has created
│     ├── Shares, organized into share classes (e.g., common vs preferred)
│     └── Contract-style instruments (option grants, convertible instruments)
├── Holdings — the binding of a stakeholder to a quantity of a security,
│     with terms (dates, prices, vesting conditions)
├── Computed ownership — percentages derived from holdings,
│     per class, outstanding, and fully diluted
└── Maintained over time — the record is updated through recorded
      equity events, each dated and attributable
```

Every part is load-bearing:

- **Issuing company** — the record exists for one company; the company is the operator of the system, not a record inside someone else's.
- **Stakeholders** — every holding belongs to an identified person or entity (founders, employees, investors, sometimes estates or trusts). Names differ by product ("stakeholders", "security holders", "shareholders"); the concept is the same.
- **Securities** — the instruments that create ownership or the right to ownership: shares organized in classes, awards such as options and restricted stock, and convertible instruments (SAFEs, convertible notes) that promise future shares.
- **Holdings with terms** — the unit of truth is not "X owns 10%" but "X holds N units of security S, issued/granted on date D at price P, vesting on schedule V". The terms are what make events computable later.
- **Computed ownership** — the table's purpose: percentages per holder and per class, both outstanding (issued shares) and fully diluted (as if everything outstanding-or-reserved had converted and vested).
- **Maintained over time** — the table reflects the company at any date because changes enter as recorded events, not silent overwrites.

### Standard capabilities mature products add

These are widespread across current products but a company with only founders and common shares can be fully served without most of them:

- **Share classes with rights** — voting vs non-voting, super-voting shares, preferred classes with their own terms; classes that can be excluded from fully-diluted math.
- **Typed equity-event machinery** — issuance, grant, transfer (optionally with recorded price), exercise, conversion of convertibles, cancellation/repurchase/forfeiture, class conversion, stock split (with history re-adjusted), dividends and payouts; bulk import; drafts reviewed before publication; an audit trail per transaction.
- **Equity plan / option pool** — reserved, unallocated capacity that grants draw down; pool sizing, amendment, and exclusion from fully-diluted figures.
- **Vesting** — time-based schedules and tranches, acceleration, performance conditions; post-termination exercise handling.
- **Financing rounds as composite events** — one event defining the round (name, share class, price) with multiple investments recorded under it, often alongside a pool top-up.
- **Convertible instruments** — SAFEs and notes held as pending instruments with their conversion terms (valuation cap, discount), converted into actual holdings through a recorded step.
- **Recorded valuations** — dated valuation events on the company's timeline that underpin award pricing (in the US, the 409A valuation; other jurisdictions have their own types).
- **Compliance and tax outputs** — share-based-payment expense reports (US GAAP / IFRS 2), issuance-exemption tracking, participant tax forms and elections, eligibility attestations.
- **Scenario modeling** — pro-forma fundraising rounds and dilution, including how outstanding convertibles would convert; waterfall views of who receives what on an exit.
- **Stakeholder portals** — employees and investors see their own holdings, vesting, and documents; administrators can preview what each stakeholder sees and revoke access.
- **Documents and e-signature** — grant letters, share certificates, exercise documents generated from templates and signed in-product or through an e-signature service; holding confirmations; a data room for fundraising.
- **Confidentiality and governance** — role-scoped administrative access; sharing of the table with outsiders, optionally anonymized; full auditability.
- **Migration** — importing an existing table from a spreadsheet or another provider as a first-class onboarding flow (sometimes a white-glove service).

### One structure, many instruments

The core model is written in conceptual terms. The instrument vocabulary is the most visible implementation layer:

```text
Concept:            ownership instruments
Venture-backed US:  common + preferred classes, ISO/NSO options, RSUs,
                    SAFEs, convertible notes, warrants
UK/EU startups:     EMI and CSOP options, growth shares, BSPCE
LLCs / alt models:  units, profit interests, phantom stock
Digital assets:     tokens
```

A reader who only knows the venture-backed stack should still recognize a two-founder common-shares company — or a token cap table — as the same application type.

## How It Works

### Set up the record

```text
Create the company record
→ define share classes and totals
→ import or enter existing holdings
→ reconcile against actual documents (certificates, signed agreements)
```

Migration is a designed workflow in every product: spreadsheets and predecessor systems are imported in bulk, then validated document-by-document before the platform becomes the record.

### Record an ownership event

```text
Choose the event type (issue / grant / transfer / convert / cancel / split ...)
→ select stakeholder(s) and security
→ enter terms (dates, price, vesting)
→ generate the underlying document for signature
→ publish the transaction
→ the cap table, ownership math, and stakeholder portals update
```

Changes are typed, dated transactions rather than cell edits. Mature products keep drafts separate from published history and retain an audit trail per transaction, so the table can answer not just "who owns what today" but "what changed, when, on whose authority".

### Run a financing

```text
Record the round as one event (name, share class, price per share)
→ record each investment under it (investor, amount, resulting shares)
→ optionally create or top up the option pool
→ convert any outstanding SAFEs / notes under their terms
→ review the new ownership and dilution
```

### Administer employee equity

```text
Reserve pool capacity
→ grant an award from the pool (option/RSU/etc., with vesting schedule)
→ employee accepts and signs in their portal
→ vesting accrues on schedule
→ employee submits an exercise request; pays; administrator processes it
→ exercised shares appear as holdings; withholding and tax forms are generated
→ if the employee leaves, post-termination exercise rules apply
```

### Model before deciding

```text
Duplicate the current table into a scenario
→ add assumptions (round size, valuation, pool top-up, SAFE conversion)
→ read the pro-forma dilution per holder
→ optionally inspect the exit waterfall at assumed outcomes
```

### Close the loop with reporting

```text
Record a valuation on the timeline
→ generate expense reports for the accounting close
→ generate participant tax forms and elections when due
→ export/share the table (optionally anonymized) for board, audit, or diligence
```

## Interfaces

### Cap table view (admin)

The heart of the product.

- shows every stakeholder × security × holding, per class, with ownership percentages outstanding and fully diluted, often at any historical date
- primary actions: add an event, drill into a holding, export or share (with anonymization option)

### Transactions list (admin)

The event ledger behind the table.

- chronological, grouped by type, filterable; draft and published states
- primary actions: add a transaction, bulk import, edit where the product allows, inspect the audit trail

### Grants / securities management (admin)

- award-level detail: terms, vesting progress, holders, attached documents
- primary actions: grant from pool, modify, reprice, settle or cancel, process exercises

### Stakeholders (admin)

- the holder registry: individuals and entities, grouped (employees, investors), with custom fields, portal invitations and revocation
- primary actions: add/import, invite to portal, group, offboard

### Scenario / modeling tool

- sandbox over the current table for future rounds, convertibles, and exits
- primary actions: create scenario, set assumptions, compare dilution outcomes

### Stakeholder portal (employee / investor)

- my holdings, vesting timeline, documents, tax forms
- primary actions: accept a grant, sign, request an exercise, download documents; for investors, receive updates and reports the company shares

### Reports & documents (admin)

- valuation history, expense and compliance reports, certificates, grant letters, data room
- primary actions: generate from the live record, share with scoped access

## Important Rules / Behaviors

### The table is a ledger, not a spreadsheet

Ownership changes enter as recorded events with dates and actors. This is what makes the record trustworthy enough for board packs, audits, and diligence — and why products make historical reconstruction ("what did the table look like at date X?") a normal operation.

### Grants draw from finite capacity

Awards come out of a pool with a defined size; issuing beyond it is either blocked or flagged for amendment. The pool itself is a visible line in fully-diluted math, and products allow excluding unallocated pools or odd classes from that math.

### Not everything outstanding is owned the same way

An option is a right, not a share; unvested portions may not exist economically at all; convertibles are promises. The fully-diluted view deliberately counts things that do not yet exist — the two numbers (outstanding vs fully diluted) answer different questions and mature products keep both in view.

### Valuation drives award pricing

Option strike prices derive from recorded valuation events. Recording a valuation is therefore part of the equity workflow, not an external fact — and in the US it connects to the 409A regime.

### Conversion has semantics

Converting a SAFE or note is a recorded step that transforms a pending instrument into holdings under the instrument's terms (cap/discount, pre- vs post-money mechanics). Products keep the conversion linked to the original instrument and, in several, reversible while correcting errors.

### Confidentiality is structural

Cap table data is among a company's most sensitive information. Access is role-scoped; stakeholder portals expose only each person's own position; sharing with outsiders is deliberate and can be anonymized. Auditability of who changed what is part of the same posture.

### Events can be undone — carefully

Products provide reversal or correction paths (undo a conversion, void an exercise, delete or amend a draft) precisely because real-world messiness — terminations, repricing, mis-dated documents — must be represented without corrupting the history.

## Variants

- **Stage** — formation (founder shares, free tiers) → early hiring (pool, first grants) → venture rounds (classes, convertibles) → late stage (secondaries, complex scenarios) → IPO readiness.
- **Geography** — US-centric stack (409A, 83(b), Rule 701, Form 3921, QSBS) vs UK/EU schemes (EMI, CSOP, BSPCE, growth shares) vs multi-jurisdiction operations with country-specific compliance reports; multi-currency records.
- **Corporate form** — C-corporations vs LLCs (units, profit interests) vs trusts/foundations as holding structures.
- **Public-company extension** — the same record plus share plan administration at scale, trading restriction windows, release elections, and settlement/broker integration; several products span private and public.
- **Ecosystem packaging** — focused startup tooling vs a broader private-capital suite that also runs fund administration and SPVs vs a valuation-services-led product vs an equity-compensation platform extending into executive and deferred compensation.
- **Instrument breadth** — token/crypto cap tables as a distinct sub-world in some products.
- **Service depth** — self-serve software vs vendor-managed cap table ("we run it for you") vs white-glove migration.
- **Era-common additions** — AI assistants answering questions over live equity data and automating administrative tasks.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Investor Portal | adjacent, often bundled | distribution surface *to* investors (statements, updates, documents); cap table management maintains the ownership record the portal reports from |
| Fund Administration Platform | adjacent, same market | subject is a fund's LP/GP structure, capital calls, and fund accounting — not one operating company's equity |
| Deal Management for PE/VC | adjacent | investor-side pipeline and deal work; the record operator is the investor, not the issuing company |
| Private Market Investment Platform | adjacent | investor-side investing into private assets; ownership ledger of the investee company is not its subject |
| Public-company share plan administration | adjacent (extension of this type toward public markets) | centers on administering listed-share plans with trading and settlement; private-round financing mechanics recede |
| Accounting Software / General Ledger | downstream consumer | records the company's money; cap table expense reports feed it as inputs |
| Board / Corporate Governance Platform | neighbor | board and committee operations across all matters; equity consents here are bound to the ownership record only |
| Legal Entity Management | neighbor | statutory entity data, officers, and filings across an organization; not equity instruments and holdings |
| Compensation Management Platform | different domain | cash compensation design and budgeting; equity grants live in the ownership record, with HR-system integration as the seam |

## Representative Products

- **Carta** — dominant US incumbent; cap table as the core of a broad private-capital suite (equity, fund administration, valuations, transfer agent).
- **Pulley** — startup-focused challenger with a product-led philosophy and an extensive public help center.
- **Ledgy** — European leader; strong multi-jurisdiction compliance; spans private companies into public-company share plans and executive compensation.
- **Eqvista** — value-segment, valuation-led product (409A services in front of a free cap table tier); SEC-registered transfer agent.

## Sources

Research date: **2026-09-07**

- Carta — https://carta.com/ , https://carta.com/cap-table/ (product pages)
- Pulley — https://help.pulley.com/en/ (help center: Recording Securities, Cap Table Flows, Fundraising & Modeling collections)
- Ledgy — https://www.ledgy.com/ , https://help.ledgy.com/en/ (help center: Admin Guide; "What transaction types can I add on Ledgy?")
- Eqvista — https://eqvista.com/ (services and cap table pages)

> Sourcing limitation: Morgan Stanley Shareworks (the enterprise/public-company pole) could not be reached during research and is used only as unnamed market context. Carta and Eqvista evidence rests on official product/service pages rather than operational help centers; those products' feature-level details are asserted only coarsely. The strongest structural claims are anchored on Pulley's and Ledgy's operational documentation. Precise numeric limits, prices, and default windows are intentionally not stated.
