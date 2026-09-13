# Media Buying Platform

## Overview

A **Media Buying Platform** is the buyer-side operating platform for the media buying operation: it holds the media plan of record, converts planned placements into authorized commitments to media vendors, and tracks the money and the delivery against those same records until the buys are reconciled and settled.

The defining structure is small:

```text
Media Plan (plan of record)
└── Placement (one ad space: vendor, program/channel, flight dates, rate/cost, quantity, goal)
    └── committed as → Buy commitment (insertion order with terms, or approved activation)
        └── Actual spend & delivery captured against the same records
            └── pacing / variance → in-flight reallocation
                └── (full form) vendor bill → reconciliation → payment handoff
```

Everything else commonly associated with these products — RFP workflows, vendor catalogs, flowcharts, platform integrations, dashboards, AI planning — is standard capability that makes the operation practical, not what makes the product a media buying platform.

The Type's center of gravity is the **buy**: the commitment that binds money to a vendor, and the accountability loop that follows it. Planning is integrated as the upstream stage of the same operation — modern products treat planning and buying as one continuous workflow rather than two separate jobs.

When the product's world shrinks to per-impression auction bidding on programmatic inventory, it is drifting toward a Demand-side Platform. When it centers on a single platform's campaign lifecycle, it is Advertising Campaign Management. When it centers on the marketing initiative the buys serve, it is Marketing Campaign Management.

## Users & Context

The primary user is a **media professional responsible for buying paid media on behalf of an advertiser**:

- **media buyer / trader** — commits buys with vendors, monitors delivery and pacing, handles changes and makegoods
- **media planner** — builds and revises the plan the buys execute; in digital-heavy teams the planner and buyer roles often merge
- **account / client lead** — owns the client relationship, authorizations, and reporting
- **media operations / ad ops** — trafficking, naming conventions, tracking, platform setup

Secondary users:

- **finance / accounting** — consumes reconciled bills and approved-for-payment data; in the agency form, the platform hands off to the agency's accounting system rather than replacing it
- **management** — oversees budgets, margins, and client portfolios across the operation

Two organizational postures exist. In the **agency posture**, the platform runs the buying operation for a portfolio of advertiser clients, with client hierarchies, authorizations, and client-facing reporting. In the **advertiser (in-house) posture**, the brand runs its own media investment in the platform, often using it to govern execution across multiple agency partners. Both postures work on the same core structures.

The work environment is a web-based workspace organized around the media plan; the platform sits above the execution surfaces (ad platforms, DSPs, vendors' own systems) rather than replacing them.

## Core Model

### The Defining Core

```text
Media Plan (plan of record)
└── Placement
    └── Buy commitment
        └── Money & delivery accountability loop
```

Three structures, held together. If any one is removed, the product stops being a media buying platform:

- **The media plan of record** — the intended buys held as structured placements across multiple independent media vendors and channel types. A placement carries who it is bought through (the vendor), what the ad space is (a TV program, a print position, a billboard, a search campaign, a social campaign, a programmatic line), when it runs (flight dates), what it costs (rate and cost method), and what it should deliver (quantity and goal). The plan is the standing record the whole operation works from — not a one-off spreadsheet. Without it, there is nothing to buy against and nothing to be accountable to.
- **The committed buy** — plan lines converted into authorized, money-binding commitments to specific vendors. In the traditional form this is an **insertion order**: the placements for one vendor or deal, priced, scheduled, and carrying terms and conditions, approved internally and accepted by the vendor. In the digital-platform form this is an **approved activation**: line items that pass budget-authorization checks and are pushed to the ad platforms where they execute. Either way, the commitment is the transaction of record that turns intent into obligated spend. Without it, the product is planning advice.
- **The spend-and-delivery accountability loop** — actual spend and actual delivery captured against the same plan and commitment records, producing the planned-vs-committed-vs-actual picture that drives pacing decisions and in-flight reallocation. In the full agency form the loop closes financially: vendor bills are checked against what was ordered and what was delivered, and the approved result is handed to payment and accounting. Without it, the product is a document generator with no operational memory.

### The Container Hierarchy

The plan sits inside a client-and-budget container:

```text
Organization
└── Advertiser / Client (hierarchical; access-controlled)
    └── Campaign (a marketing initiative tied to a budget)
        └── Media Plan
            └── Placements → Commitments → Actuals → Bills
```

The campaign is the budget-bearing folder: it holds the plan, the budgets, the commitments, the performance data, and the payables together. Exact naming varies by product; the load-bearing idea is that one container binds a budget to the buys made against it.

### The Money States

The same placement moves through money states that the platform tracks:

```text
Planned → Committed → Actual (→ Billed → Paid, in the full form)
```

Budget structures (allocation buckets, caps, targets) are held against these states, so overspending or underspending is visible while there is still time to act.

### One Structure, Many Channels

A single plan holds placements across channel types side by side — a broadcast placement next to a search campaign next to a programmatic line next to an out-of-home panel. The channel determines how a placement executes and how its actuals arrive (platform APIs for digital, vendor-reported proof for traditional), not whether it belongs in the plan.

### Capabilities Beyond the Core

Standard capabilities in mature products:

- **RFP and proposal workflow** — request availability, pricing, and packaging from candidate vendors; track and evaluate responses; accept proposals into the plan
- **Vendor and program catalog** — a maintained database of media vendors, their programs, contacts, and rates, used at research and planning time
- **Generated outputs** — media flowcharts, client presentations, and authorization documents produced from the plan data
- **Trafficking handoff** — creative association, ad-spec handling, placement naming conventions, tracking URLs, and delivery of campaign data to ad servers and platforms
- **Performance-data integration** — delivery and cost actuals pulled from advertising platforms, DSPs, and vendors into the same data model, matched to placements
- **Pacing and budget reallocation** — monitoring delivery against plan and shifting budget while campaigns run
- **Vendor-bill reconciliation and payment handoff** — bills checked against orders and delivery; approved amounts passed to accounting systems
- **Approval and audit machinery** — authorization gates, change history, order amendments
- **Reporting and client-facing dashboards**
- **AI assistance** — plan drafting, recommendations, and optimization suggestions (era-current)

## How It Works

The buying operation runs as a loop from plan to payment:

### 1. Plan

The planner builds the media plan: placements are added from research and the vendor catalog, priced, scheduled into flights, and allocated against budget buckets. The plan is revised until it is authorized.

### 2. Authorize

The plan (or its placements) passes authorization gates — client sign-off in the agency form, budget-holder approval in the in-house form. Budget caps are enforced here: the platform prevents committing more than has been authorized.

### 3. Commit

The plan is burst into commitments — typically one per vendor or deal. Each commitment carries its placements, pricing, schedule, and terms and conditions; it is approved internally and, in the traditional form, sent to the vendor for acceptance (increasingly with electronic signatures). In the digital-platform form, approved line items are pushed directly to the ad platforms via API. Some products create commitment records even for programmatic buys that need no vendor signature, precisely to keep one governance record and a baseline for reconciliation.

### 4. Activate

Creative is delivered to spec, placements are named per convention, tracking is attached, and campaign data is trafficked to the platforms or vendors where the ads will run. The platform's identifiers are cross-referenced to the platforms' own identifiers so actuals can find their way home.

### 5. Track

While the buys run, actual spend and delivery flow back into the same records. Pacing — actual versus planned at the current point in the flight — is monitored continuously; shortfalls and overdelivery surface as alerts. Traditional channels contribute vendor-reported delivery proof; digital channels contribute platform-reported metrics.

### 6. Reconcile and settle

In the full form, vendors bill against their commitments on a recurring cycle while the buys run. Each bill is checked: did we order this, did they deliver what was promised, is it priced correctly, does it exceed what was committed? The reconciled result is marked approved for payment, payments are recorded, and the data is handed to the accounting system, which holds the ledger. The platform's own loop ends at the media-side money record.

### 7. Report

Throughout, the same data produces client reporting — flowcharts, dashboards, and plan-versus-actual reviews — without leaving the platform's records.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Media plan grid

The central surface. Placement rows with columns for vendor, program, channel, flight dates, rates, costs, quantities, and goals; batch editing, filtering, and color-coding; totals and budget roll-ups. Primary actions: add/edit/clone placements, allocate to budgets, exclude or lock lines, generate outputs.

### Placement detail

One ad space in full: vendor and contact, ad-space specifics, schedule (including daypart/weekpart granularity where the channel requires it), cost method and rate, KPI goals, associated creative, and the commitment(s) that carry it.

### Commitment / order workspace

Generate commitments from plan selections; attach terms; route for internal approval; send for vendor acceptance with electronic signature; handle amendments and changes; keep a terms library. In activation-form products, this surface is the approval-and-push console for line items.

### Budget / allocation view

Budget buckets or allocation trees with planned, committed, and remaining amounts; caps and validation that block over-commitment; top-down distribution across brands, regions, or campaigns.

### Flowchart / presentation output

Generated client-facing views of the plan across time — the traditional media flowchart, produced from the same plan data.

### Performance and pacing view

Actuals against plan per placement and in aggregate: spend, delivery, goal progress, pacing status, alerts on under/overdelivery.

### Bill reconciliation workspace

Vendor bills entered or ingested against commitments; ordered vs delivered vs billed comparison; approved-for-payment marking; payables and payment records; export or integration to accounting.

### Vendor catalog

Searchable vendors, programs, contacts, and historical rates — the research substrate for planning and RFPs.

### Client-facing surfaces

Dashboards or portals shared with clients or brand stakeholders, showing plan status, spend, and performance without exposing internal workflow.

## Important Rules / Behaviors

### Nothing commits without authorization

The commitment step is gated: client or budget-holder authorization must exist before placements become binding buys, and budget caps block commitments beyond what was authorized. This gate is the platform's core control point.

### The plan is the baseline for everything

Actuals, bills, and variance are all judged against the plan of record. A reporting or reconciliation capability that cannot compare against the plan cannot support the buying operation — this is why the plan lives as structured data rather than a document.

### Commitments bind terms

Each commitment carries its own terms and conditions (industry-standard or negotiated). Changes after commitment are recorded as amendments rather than silent edits, preserving the audit trail between what was agreed and what is billed.

### Money states are explicit

Planned, committed, and actual amounts are tracked as distinct states on the same records. In the full form, billed and paid follow. The distinction is what makes pacing, capping, and reconciliation possible.

### Gross and net are different numbers

In the agency posture, media cost is tracked gross (vendor-facing) and net (client-facing) with the agency's compensation visible as the difference. The platform holds both views on the same records.

### Delivery verification differs by channel

Digital actuals arrive continuously from platforms; traditional channels rely on vendor-reported proof of delivery (logs, affidavits, post-runs). The platform accommodates both, and shortfall against a commitment is actionable in either case.

### The platform is not the ledger

The platform holds the media-side money record — orders, bills, reconciliations — and hands approved results to the organization's accounting system. It deliberately does not replace the general ledger.

## Variants

- **Channel scope** — all-channel platforms spanning traditional and digital media in one plan vs digital-only platforms (programmatic, search, social, site-direct). Both realize the same core; scope is the market's most visible split.
- **Programmatic posture** — an embedded proprietary DSP inside the platform vs channel-agnostic integrations that pull actuals from external DSPs and platforms vs push-based activation through platform APIs and overlays.
- **Customer side** — agency-first (client portfolios, authorizations, client billing support) vs advertiser-first (in-house media teams governing their own investment and their agencies) vs products serving both.
- **Commitment form** — insertion-order-centric (signed documents, terms libraries) vs activation-push-centric (approved line items under budget caps). Many products blend both depending on channel.
- **Scale and geography** — local/traditional agency deployments vs global multi-market, multi-currency, multi-year investment structures.
- **Service wrapping** — self-service platforms vs platforms sold with managed media services operating inside the same environment.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Demand-side Platform / DSP | adjacent (may be contained) | DSP is per-impression programmatic trading infrastructure; a media buying platform holds the whole cross-channel buying operation and may embed a DSP as one module |
| Advertising Campaign Management | adjacent | campaign management runs the advertiser-defined campaign lifecycle on ad platforms; media buying runs the cross-vendor commercial operation (plan, commit, reconcile) those campaigns serve |
| Marketing Campaign Management Platform | adjacent | campaign management plans and coordinates the marketing initiative (brief, assets, calendar); media buying transacts the placements the initiative requires |
| Programmatic Advertising Platform | category sibling | the automated impression-trading layer; media buying is the wider buying operation that programmatic feeds into |
| Supply-side Platform / SSP | other side of the market | SSP serves media owners monetizing inventory; no overlap in customer or objects |
| Search Engine Marketing Management Platform | channel slice | SEM management operates search-engine ad accounts (keyword bids, budgets) via engine APIs; media buying spans channels including offline and holds the vendor money loop |
| Ad Server | downstream infrastructure | ad servers select and serve ads at request time; media buying decides and accounts for what was bought |
| Creative Management Platform / DCO | upstream supplier | creative production and versioning feeds the buys; media buying accounts for them |
| Marketing Analytics / Attribution Platform | measurement layer | attribution models outcomes; media buying's reporting is centered on plan-vs-actual for its own buys |

The sharpest boundary is the **DSP**: the two are layered, not competing — a buying platform can contain a DSP, and vendors themselves articulate the seam ("a DSP handles programmatic media buying; the buying platform is the operational foundation for the whole advertising organization"). The second sharpest is **advertising campaign management**: both touch platform campaign setup, but campaign management is the per-platform execution lifecycle while media buying is the multi-vendor money operation.

## Representative Products

- **Bionic for Agencies** (Bionic Advertising Systems) — agency media planning and buying across all channels; the clearest insertion-order-and-reconciliation-centric implementation
- **Basis** (Basis Global Technologies) — digital advertising operating system with an embedded DSP and a planning-to-payment financial loop
- **Camphouse (fka Mediatool)** — advertiser/agency media operations platform led by a planning system of record, budget allocation, and activation push
- **Strata** (FreeWheel) — cross-media agency platform with traditional-media heritage and financial-system integration
- **Mediaocean** — enterprise agency system of record (digital and traditional product lines); included as a further market anchor

## Sources

Research date: **2026-09-08**

- Bionic Advertising Systems — homepage; "The 11 Steps of the Media Buying Process Explained"; Knowledge Base (Bionic for Agencies user guide, data structure, vendor bill reconciliation) — https://www.bionic-ads.com/ , https://help.bionic-ads.com/knowledge
- Basis — homepage and platform page (incl. product FAQ) — https://basis.com/technology/platform
- Camphouse (fka Mediatool) — homepage; Planning System of Record; Budget Allocation; Media Activation — https://camphouse.io/
- Strata (FreeWheel) — product page — https://www.freewheel.com/strata
- Mediaocean — positioning-level only (named as a media buying system on Bionic's product pages); site not directly reachable

> Sourcing limitations: Basis's help center and Mediaocean's site could not be fetched from the research environment (repeated transport errors); Basis is documented at positioning/FAQ level and Mediaocean at category level only, with no operational claims. Strata's reachable documentation is a single product page, so no operational detail is asserted for it. Camphouse's vendor-bill reconciliation could not be verified in official documentation; the money loop is documented for it at the budget-authorization and pacing level. Precise numeric limits, pricing, and product-specific defaults are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
