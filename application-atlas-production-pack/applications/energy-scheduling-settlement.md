# Energy Scheduling & Settlement

## Overview

An **Energy Scheduling & Settlement** system is a wholesale power market participant's operational system of record for the market-facing half of its energy business. It does two connected jobs:

- **Scheduling** — it composes, validates, and submits time-structured energy quantities to the market or transmission authority the participant operates in: day-ahead and real-time bids and offers, self-schedules, virtual bids, and transmission tags that describe where energy will enter and leave the grid, hour by hour. Each submission is made under that market's rules and deadlines, and the awards, clearances, or acceptance statuses that come back are recorded.
- **Settlement** — it ingests the itemized settlement statements that the market operator, settlement agent, transmission provider, or bilateral counterparty issues — the authoritative claim of what the participant is charged and credited for the energy it scheduled, produced, consumed, or transported — and it checks those statements against the participant's own independent recomputation of what the settlement should be. Discrepancies become tracked records that are disputed, adjusted, and rebilled until the money is right and the books are closed.

The problem it exists to solve: in a wholesale power market, the participant's money is determined by quantities that were declared in advance (schedules and bids), measured after the fact (meters), and calculated by a counterparty (the market's settlement). The participant cannot simply trust that calculation — settlements are large, complex, charge-coded, and routinely wrong in the participant's disfavor. This system is the participant's disciplined answer: keep the market-facing record of what was submitted and what was awarded, recompute what settlement should be, compare it to what the market says it is, and drive every difference to a defensible financial closure.

Its boundary: it is not the trading system (which captures deals and manages risk before anything must be scheduled), not the forecasting platform (which produces the numbers bids are built from), not the grid control system (which physically balances the network in real time), not the metering infrastructure (which produces raw measurement), and not retail customer billing (which charges end consumers on tariffs). It sits in the middle of those systems: it consumes deals, forecasts, and meter data, and it produces settled, auditable money records.

## Users & Context

Primary users, and how each relates to the work:

- **Schedulers and market coordinators** — own the submission side. They build bids, schedules, and transmission tags from portfolio plans and forecasts, run them through validation, submit them before gate closures, respond to rejections, and monitor award and tag status through the operating day. Their work is deadline-driven and error-intolerant: a late or malformed submission is a missed market day or an untagged transaction.
- **Settlement analysts and back-office staff** — own the reconciliation side. They ingest settlement statements and meter data, run shadow settlements, compare expected versus actual charges, drill into discrepancies at interval and charge level, file and track disputes, and process rebills and prior-period adjustments.
- **Contract billing and accounting staff** — consume the validated settlement data to invoice bilateral and contract counterparties, allocate costs to internal and external entities, post to the general ledger, and record accruals ahead of final statements.
- **Traders and front-office staff** — consume award validation and settlement feedback: whether yesterday's awards matched the bids, what uplift, congestion, or deviations cost, and where settlement outcomes diverge from expectations.

Secondary users include middle-office managers (portfolio performance, dispute recovery, compliance posture) and — at smaller utilities, cooperatives, and public-power entities — a single team that covers scheduling, settlements, analytics, and billing in one platform.

The working context has two clocks. The **operating-day clock** is set by market deadlines: day-ahead gate closures, intraday and real-time intervals, tag cutoffs. The **financial clock** is set by settlement production: preliminary statements, revised and final versions, month-end close, accruals, and audit preparation. Layered over both is a third pressure — markets change their rules constantly, and the system must absorb those changes without the participant rebuilding its logic.

## Core Model

The defining core consists of three structures that only work together, all anchored to a position in a specific market:

```text
Position basis
  (the participant's resources, deals, contracts, and
   transmission entitlements in a named market)
        ↓ expressed to the market as
Market submissions of record
  (bids / offers / schedules / tags — validated against
   market rules, submitted under deadline, awards returned)
        ↓ settled by the market as
Settlement statement of record
  (itemized charges & credits by charge type, interval, subject)
        ↓ checked by
Participant-side reconciliation loop
  (shadow settlement → discrepancies → disputes,
   adjustments, rebills → financial closure)
```

### 1. The market submission of record

Everything begins with a **position basis**: the resources the participant owns or schedules at market locations, the bilateral deals and contracts it holds, and the transmission entitlements it can use. These give the participant its identity in the market and its standing to submit.

From that basis the system composes **submissions** — the time-structured declarations the market requires. Their exact form depends on the regime, but three families recur across markets:

- **Bids and offers** — price-and-quantity curves per resource and interval for day-ahead and real-time markets, plus virtual bids and spreads that are pure market positions at specific locations.
- **Schedules** — the participant's declared plan of production, consumption, or interchange per interval, including self-schedules of specific resources.
- **Transmission tags** — the declarations that tie a transaction to a physical path across transmission systems, specifying source, sink, and the hourly profile of the flow.

Every submission carries identity (who is submitting, for which resource or path, at which location, for which intervals), is checked against the governing market's rules before it leaves the system, and is transmitted under a deadline. What returns is equally part of the record: **awards, clearances, acceptance or rejection statuses**, and the real-time state of each submission. A submission that was never validated, or an award that was never captured, breaks everything downstream.

### 2. The settlement statement of record

After the energy flows, the counterparty settles. The objects are statements — itemized, charge-coded lists of what the participant is charged and credited: energy at market prices, congestion, losses, ancillary and balancing services, uplift and deviation charges, transmission charges, imbalance charges. Each line attaches to a subject (a resource, a path, a portfolio), an interval, and a charge type.

Statements are not single events: they arrive in **preliminary form and are revised toward final versions**, and later corrections come as recalculations and rebills. The statement of record is the authoritative claim on money — the participant's baseline for everything it is owed and everything it owes. Bilateral and transmission counterparties produce the same kind of object in invoice form, and in bilateral regimes the counterparty's invoice plays the statement's role.

### 3. The participant-side reconciliation loop

The participant does not accept the statement blindly. The system maintains an **independent recomputation of what the settlement should be** — commonly called a shadow settlement or pre-settlement — built from the participant's own data: its position and contracts, the awards it received, the metered quantities validated at interval level, and the applicable prices and rules.

The loop then runs side-by-side comparison: expected settlement against the statement, charge by charge, interval by interval. Differences become **discrepancies** — first-class records, not spreadsheet footnotes — which are investigated with drill-down to the billing determinants, filed as **disputes** with the counterparty where justified, and tracked to resolution. When the participant's own data or contracts were wrong, the fix is a **versioned adjustment or rebill** that corrects the record without reopening already-closed months. The loop ends in **financial closure**: costs allocated to the entities and assets that caused them, own-side invoices issued from the validated data, accruals recorded against preliminary statements, and the results posted to the general ledger with an audit trail behind every charge.

### Why the three must be held together

- A product that only submits bids and tags is a submission tool — useful, but there is no settlement function.
- Statements ingested without recomputation are a data feed — the settlement office is gone, and errors simply flow into the books.
- Shadow settlements without statements to check against are accrual calculators with nothing to settle.

### One structure, many realizations

The core is written conceptually; markets realize it differently:

```text
Concept:      Market submission of record
Realizations: day-ahead bids/virtuals in organized markets; hourly
              schedules and bilateral trade reports in imbalance-settlement
              regimes; NERC-style transmission tags for physical paths

Concept:      Settlement statement of record
Realizations: ISO/RTO charge-coded statements; transmission provider
              invoices; bilateral counterparty invoices; settlement-agent
              invoices (e.g., imbalance settlement)

Concept:      Reconciliation loop
Realizations: shadow settlement vs ISO statement; verification of an
              agent's reported results with deviation notices; both-sides
              checkout before bilateral invoicing
```

A reader who knows only one regime should still recognize the others from this model.

## How It Works

The Type's work runs in two standing cycles, plus the financial rhythm that connects them.

### Cycle A — the submission cycle (deadline-driven)

```text
Start from the portfolio plan (deals, forecasts, resource availability)
→ compose bids / schedules / tags for the target intervals
→ validate against the market's rules (eligibility, pricing, volumes, paths)
→ correct and re-validate
→ submit before the deadline; withdraw or revise while the gate is open
→ receive and record awards / clearances / acceptance status
→ monitor tag and submission status through the operating day
→ feed awarded schedules to dispatch and settle-side expectations
```

The characteristic discipline is that validation happens **inside** the system before submission, not after rejection by the market — rejections cost market days. Tags follow their own sub-cycle: creation from templates or deals, approval routing to the tag authority, profile validation against transmission availability, and later checkout — the recorded extraction of tag data for billing analysis.

### Cycle B — the settlement cycle (statement-to-closure)

```text
Ingest settlement statements (and revised versions) from the market
→ ingest and validate meter data and prices as settlement inputs
→ compute the expected settlement (shadow / pre-settlement)
→ compare expected vs statement, charge by charge and interval by interval
→ investigate discrepancies; drill to billing determinants
→ file and track disputes with the counterparty where warranted
→ process accepted adjustments; rebill with versioned corrections
→ allocate costs to internal/external entities and cost-causing assets
→ invoice bilateral/contract counterparties from the validated data
→ record accruals against preliminary statements; post to the ledger
→ close the month on a clean, auditable record
```

### The financial rhythm

The two cycles repeat daily, but their outputs settle over weeks: preliminary statements arrive first, accruals are booked against the expectation, final versions replace preliminary ones, disputes conclude on the counterparty's timetable, and month-end close collects everything into financial records. Settlement work is therefore never "done" — it is versioned, reconciled, and closed in overlapping waves, which is why mature products treat corrections as versioned rebills rather than edits.

### Capability tiers

**Defining core** — without these, the product is not this Type:

- market-facing submissions of record (bids/schedules/tags) with validation, deadline handling, and returned awards/status
- settlement statement ingestion as the authoritative claim
- the reconciliation loop: expected-vs-actual settlement comparison, discrepancy tracking, dispute/adjustment/rebill, financial closure

**Standard capabilities** — widespread in mature products, not definitional:

- award validation and day-ahead versus real-time bid analysis
- pre-statement settlement estimates feeding accruals and P&L
- meter-data validation and correction as a settlement input
- versioned rebills and prior-period adjustments without reopening closed months
- contract billing (PPAs, bilateral contracts, member bills) from the same validated data
- cost allocation to internal/external entities and cost-causing assets; general-ledger mapping
- transmission-provider invoice validation
- audit trails with charge-level traceability
- vendor-maintained market-rule updates delivered as part of the service
- settlement analytics: awards vs dispatch vs meters vs settlements, uplift, congestion, deviation drivers

**Optional / variant** — depends on regime, seat, and customer:

- virtual bids and spreads (organized day-ahead markets)
- transmission-tag path machinery with approval chains and availability checks (tag-governed regimes)
- regulatory filing outputs for market transactions (region-specific)
- collateral and credit machinery (the market-agent seat)
- multi-commodity scope (power alongside gas and fuels)

## Interfaces

The main working surfaces, described conceptually; layouts and names vary by product:

### Bid / schedule workbench

The scheduler's primary surface for composing submissions.

- shows the target market day, intervals, and the resources or locations being bid
- provides validation messages against market rules before submission, deadline indicators, and submission status back from the market
- primary actions: create and edit bids/schedules, run validation, submit, withdraw, resubmit

### Tag management surface

The surface for transmission-tag declarations in tag-governed regimes.

- typical information: tag path (source to sink), hourly profile, approval state, transmission availability
- primary actions: create from templates or deals, send for approval, validate profiles, view status, check out tag data for billing analysis

### Settlement statement browser

The back office's view of the counterparty's claim.

- typical information: statement versions, charge types, subjects (resources/paths), intervals, amounts
- primary actions: ingest new statements, drill from summary to interval-level detail, flag lines for review

### Shadow-settlement comparison view

The heart of the reconciliation loop.

- typical information: expected vs actual settlement side by side, per charge and per interval, with variance highlighting
- primary actions: compare versions, accept/match lines, mark discrepancies, generate evidence for disputes

### Discrepancy / dispute queue

- typical information: open discrepancies with amounts, aging, assigned owner, counterparty, resolution state
- primary actions: investigate, file a dispute with evidence, track to resolution, record recoveries and adjustments

### Contract billing workspace

- typical information: contract terms as versioned logic, settlement data feeding each bill, invoice drafts
- primary actions: generate invoices, allocate costs, adjust and rebill, map to the general ledger

### Analytics dashboards

- typical information: portfolio settlement outcomes over time, award-vs-award-expected comparisons, drivers such as uplift, congestion, and deviations
- primary actions: drill down, build reports, share with trading and management

### Reporting and export surfaces

- standard financial outputs: general-ledger postings, accrual reports, audit extracts, and — where the regime requires — regulatory filing formats for market transactions

## Important Rules and Behaviors

### Deadlines are structural

Submissions only exist if they arrive before gate closure; the system's validation-and-submit mechanics exist to make deadline misses structurally unlikely. Edits are possible up to the deadline, after which the market — not the participant — decides what is changeable.

### Market rules live inside the system

Validation is only as current as the rulebook it encodes. Because markets revise tariffs and processes continuously, mature products treat rule maintenance as an ongoing service — the vendor absorbs rule changes and delivers them as tested updates, so the participant's validation does not silently rot.

### Statements are versioned; corrections never reopen closed months

Preliminary statements are superseded by revised and final versions, and errors discovered later are corrected through rebills and prior-period adjustments that keep closed accounting periods intact. The audit trail, not the raw number, is the durable object.

### Every charge must be traceable

Settlement amounts are challenged and audited routinely, so the system maintains traceability from a charge line back through its determinant — the awarded quantity, meter value, price, and rule that produced it. This traceability is what makes a dispute credible and a close defensible.

### Meter data is an input to be validated, not trusted

Settlements are computed from measured quantities, so meter data is centralized and validated at interval level before it feeds shadow settlements and billing; corrections are themselves recorded and versioned.

### Money flows both ways

Settlement includes credits as well as charges, and recovery of misapplied charges through disputes is a designed outcome, not an accident — the reconciliation loop exists precisely to find underpayments as well as overcharges.

### Bilateral alignment before invoicing

In contract-driven settlement, both sides of a trade are checked to align before an invoice issues — the direct descendant of interchange-checkout practice — with configurable validations and comparison views standing in for the old manual reconciliation.

## Variants

Common forms of the Type; a variant stays a variant unless it changes the users, core objects, or workflow so much that the model above no longer applies:

- **By market regime** — organized ISO/RTO markets (charge-coded statements, virtual bidding, transmission tags); bilateral markets (contract-driven invoices, checkout-style alignment); imbalance-settlement regimes (hourly plans plus metered balance, verification of an agent's results, reconciliation of preliminary against final quantities). Other regional settlement models exist and are presumed to fit the same structure, but were not directly sampled in this pass.
- **By participant class** — generators and IPPs (generation-heavy submissions, market revenue settlement); load-serving utilities, public power, and community-choice aggregators (load settlement, member or jurisdictional billing); marketers and traders (portfolio-heavy, virtual and spread activity); cooperatives (member billing from validated settlement data).
- **By packaging** — submission-only point tools (the thin scheduling pole); settlement-only back-office products; integrated bid-to-bill platforms; and full trading-and-risk suites where this Type's functions sit beside deal capture and risk. Packaging overlap with trading suites is common in the market but does not change the object of record.
- **By seat** — the commercial default is the participant seat described throughout this document. The same settlement function also exists as a market-wide duty: a settlement agent owned by or acting for system operators runs the settlement, invoicing, and collateral management for an entire market's participants. That seat adds market-level machinery (collateral requirements, market-behavior monitoring, published settlement data) and is recorded here as the Type's operator-side relative rather than a separate commercial category.
- **By scope and delivery** — power-only versus power-plus-fuels back offices; hourly versus sub-hourly settlement granularity; single-market versus multi-market participants (including participants running two market regimes in parallel during a market migration); fully managed cloud service versus deployable enterprise software.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Energy Trading Platform | holds deals, positions, and risk — the front and middle office; this Type holds the market-facing submissions and settlement statements those deals must become. Suites bundle both; the object of record differs, and one sampled product family explicitly positions itself as not being a trading-and-risk system |
| Energy Forecasting Platform | produces and verifies the forecast quantities (generation, load, price) that bids are built from; it is an input producer with no settlement accountability, while this Type submits and settles their consequences |
| Grid Operations Platform | physical, real-time operation of the network — telemetry, switching, reliability; this Type is the market-financial aftermath of the operating day, used by different staff with different objects |
| Energy Management System / EMS | control-center real-time balancing loop (supervision, control, generation-to-load balancing); market settlement is financial record-keeping after the fact, not control |
| Meter Data Management System | the enterprise metering record and its quality machinery; this Type embeds meter-data *validation as a settlement input*, but the enterprise metering system remains a separate Type |
| Utility Billing Platform | bills end consumers on retail tariffs; this Type settles wholesale market money with market operators, agents, transmission providers, and counterparties — the two meet at load-serving entities, where both consume the same meter data |
| Demand Response Platform | manages flexibility programs and dispatch; when that flexibility settles into wholesale markets, the resulting submissions and settlement flows land in this Type |

The boundary with the Energy Trading Platform is the most important one, because the market packages them together. The structural test: if the system's center of gravity is deal capture, valuation, and risk, it is trading; if it is submissions under deadline and settlement statements reconciled to closure, it is this Type.

## Representative Products

- **PCI Energy Solutions** (GenManager bid-to-bill suite; e-Tag+; ETRM back office) — participant-side full-suite pole, US ISO/RTO and bilateral markets
- **Yes Energy** (PowerCore bid-to-bill platform; Submission Services) — participant-side platform pole from a market-data company
- **eSett Oy** (Nordic Imbalance Settlement agent) — the market-wide settlement-agent pole, included deliberately to show the same settlement function from the operator side

## Sources

Research date: **2026-09-08**

- PCI Energy Solutions — https://www.pcienergysolutions.com/ — root and solution pages: Bid-to-Bill, Settlements and Billing, Wholesale Market Participation, e-Tagging, ETRM Back Office (accessed 2026-09-08)
- Yes Energy — https://www.yesenergy.com/ — root, PowerCore, and Submission Services product pages (accessed 2026-09-08)
- eSett Oy — https://www.esett.com/ — root and NBS Handbook (v5.4 web version) (accessed 2026-09-08)

> Sourcing limitations: two further participant-side vendors commonly present in this market (Adapt2 and OATI) could not be reached from the research environment (connection errors and timeouts), so the participant-side commercial sample is two products, both North American. Product pages are vendor marketing surfaces rather than end-user manuals; precise operational facts (statement cadences, dispute timetables, numeric limits, vendor-claimed performance figures) are therefore not asserted in this document and remain, where recorded at all, in the paired Research Notes. Agent-side settlement mechanics are evidenced from one product only and are kept generic above.
