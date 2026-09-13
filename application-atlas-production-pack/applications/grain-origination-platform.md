# Grain Origination Platform

## Overview

A **Grain Origination Platform** is a grain buyer's acquisition-side system: it publishes the buyer's purchase prices where growers decide to sell, turns grower offers and bid acceptances into purchase contracts, and manages the resulting book of open commitments — quantity filled versus remaining, pricing status, and current market value — until the contracted grain is delivered.

The defining structure is small:

```text
Buyer-published purchase prices (cash bids)
└── grower offers / bid acceptances
    └── purchase contract (typed, priced or pricable, terms-bearing)
        └── open commitment book (filled vs remaining, pricing status, market value)
            └── fulfillment by delivery — custody and settlement live in the receiving/custody system
```

Everything commonly bundled around modern products — grower mobile apps, relationship management for merchandisers, digital payments, e-signature, market-data feeds, farm-management pairing — is widespread in current products but is not part of the defining core. A paper-era country elevator ran the same acquisition process by hand: the posted daily bid sheet, phone-in offers concluded with a signed contract, and a contract ledger tracking filled bushels and unpriced commitments.

The boundary with the neighboring grain Types follows the trade's own division of labor: origination acquires the grain, the grain elevator system takes custody of it and settles the money owed, and grain-management systems protect it in storage. When a platform adds delivery tickets, storage inventory, and settlement of its own, it is extending into the elevator system of record — a posture some products take — not changing what origination itself is.

## Users & Context

Primary users, inside the grain-buying business:

- **grain buyer / merchandiser / originator** — sets and publishes the purchase prices, reviews and accepts or rejects grower offers, creates and prices contracts, and watches the book of open commitments
- **origination / office staff** — maintain contracts, discount schedules, customer records, and payment information; monitor offer queues and contract status
- **location or branch manager** — watches acquisition activity and commitments per delivery location and across the company

External participants:

- **growers (farmers)** — the sellers being acquired from. In current products they view posted prices, submit offers, accept bids, price unpriced contracts, sign documents, and follow their contracts and payments through a portal or app. Historically they did all of this by phone and paper.
- **brokers** — in some markets, intermediaries who originate grain on behalf of buyers and hold their own view of contracts and invoices.

The work context is market-driven rather than clock-driven: posted prices must track moving futures markets, growers respond at all hours, and acquisition volume peaks at harvest. This is why current products emphasize capturing offers the moment a grower decides to sell — after hours, from a phone — instead of the phone-tag-and-spreadsheet routine the products describe replacing.

## Core Model

### The Defining Core

Three structures, jointly held. If any one is removed, the product stops being recognizable as origination:

**1. Buyer-published acquisition pricing.** The buyer's standing offer to purchase grain — the *cash bid* in industry vocabulary — dimensioned by commodity, grade, delivery location, and period or season, revised as markets move, and made visible where growers decide to sell: the grower's app, the buyer's website, in-office displays, or a network board spanning many buyers' sites. The bid layer is the acquisition shop window; every downstream commitment begins with a price a grower could see and act on.

**2. The offer-to-contract formation loop.** Growers initiate — a firm offer to sell at specified terms, or acceptance of a posted bid. The buyer reviews and accepts or rejects; an accepted offer is a binding act that locks the price (with a timestamped record protecting both sides) and produces a **purchase contract**: a typed record carrying the counterparty, commodity, grade or grades, quantity, price or pricing basis, delivery location or locations, a delivery window, and payment terms. Where a contract covers several grades or alternative delivery sites, the price consequences may be carried as spreads or adjustments structured on the contract itself. The price may be fixed at signing or resolved later against a market reference; contracts that are not yet fully priced remain open to pricing actions from either side.

**3. The open commitment book.** Contracts are managed as live acquisition commitments rather than filed documents: how many bushels have been filled against each contract and how many remain, which contracts are unpriced and on what pricing basis, and what the open commitments are currently worth at market. The book is the buyer's acquisition position — what grain has been secured, at what exposure, toward which delivery windows.

These three are load-bearing together. A bid page with an offer inbox but no managed book is marketing tooling; posted prices with a hand-kept contract ledger are a website and a spreadsheet; a contract desk with fulfillment tracking but no market-facing pricing is the back office of an elevator system, not origination.

### Standard Capabilities

Mature products add a common operating layer on top of the defining core. These make the Type practical but do not define it:

- **Grower portal / app** — the grower's window onto posted prices, their offers, contracts, balances, and payments; in current products also the channel for self-service offers and contract pricing.
- **Electronic signature and timestamped acceptance** — closing the offer-to-contract loop with a defensible record instead of a phone call.
- **Offer status synchronization** — the grower sees accept/reject decisions and contract status update immediately.
- **Relationship management for the origination desk** — each grower's activity, position, and history in one place, so merchandisers know who is ready to sell and where each contract stands.
- **Discount schedules and premium/discount tables** — managed configuration that will later govern settlement deductions for quality factors.
- **Market data and market-value tracking** — commodity and futures references feeding both the bid layer and the valuation of open contracts.
- **Multi-location pricing** — bids and delivery terms priced per location; some products price alternative delivery sites as adjustments structured on the contract.
- **Payment and settlement visibility** — payments to growers and settlement summaries; where the settlement of record is computed (inside this platform, or in the connected elevator/ERP system) varies by packaging posture.
- **Reporting and analytics** on origination activity and acquisition performance.

Some products go further — placing and tracking futures orders that back cash purchases, embedding bid widgets on third-party websites, licensing farm-management tools to their growers, or brokering intermediation with dedicated broker views. These are optional capabilities that depend on business model and posture.

### One Structure, Many Implementations

```text
Concept:   buyer's posted acquisition price   → posted daily bid sheet (paper heritage); digital bid boards, network price boards, embeddable widgets
Concept:   grower's offer                     → phone call and verbal yes (paper heritage); firm in-app offers with timestamped acceptance
Concept:   the purchase contract              → signed paper contract in the contract book; typed electronic contract, e-signed, often auto-created in a connected ERP
Concept:   the commitment book                → contract ledger; live position with filled-vs-remaining quantities, pricing status, and market value
Concept:   grower identity                    → local customer records; platform accounts linked to industry grower-registration services
```

A reader who has only seen one implementation — for example a mobile-app-first origination product — should still be able to recognize a paper-era origination desk, or a contract module buried in an elevator ERP, as machinery of the same Type.

## How It Works

### Publish and maintain acquisition prices

```text
Buyer sets bids by commodity, grade, location, and delivery window
→ prices are revised as the market moves
→ one update fans out to every channel at once
  (grower apps, the buyer's website, in-office displays, network boards)
→ growers compare prices and decide where to sell
```

Stale bids are a business risk the machinery is built to minimize: the cost of a missed price update is losing bushels to another buyer.

### Capture grower demand

```text
Grower views available prices (often filtered by commodity, grade, season, location, buyer)
→ submits a firm offer at chosen terms — any time, from anywhere
→ (or) accepts a posted bid outright
→ the offer enters the buyer's queue with its quantity and validity
```

### Form the contract

```text
Merchandiser reviews the offer
→ accepts (or rejects)
→ the price locks at acceptance, timestamped on the record
→ contract issued with quantity and terms; grower signs electronically
→ where the platform integrates an ERP, the accepted and filled offer
  creates the contract in the buyer's back-office system automatically
```

### Work the book

```text
Open contracts tracked: quantity filled vs remaining, delivery window, pricing status
→ unpriced contracts resolved by pricing actions
  (grower prices from the app, or buyer action against the market reference)
→ market value of open commitments monitored as prices move
→ deferred-delivery contracts may carry price escalators over time
```

### Fulfill by delivery

```text
Delivery window arrives
→ loads are delivered against the contract
→ deliveries are weighed and ticketed at the receiving point —
  the scale ticket and the storage record belong to the elevator/custody system,
  or to the platform's own fuller modules where it spans the chain
→ contract balances update as loads are applied; the remaining quantity shrinks
```

### Settle and pay

```text
Settlement applies the contract terms and quality adjustments
→ computed in the custody/back-office system, or in the platform's own
  settlement machinery on full-chain products
→ grower sees settlement and payment — check or digital transfer —
  against their contract in the portal
```

### Core vs Standard vs Optional

**Defining core** — without these, not origination:

- buyer-published acquisition pricing (cash bids)
- the offer → acceptance → contract formation loop
- the open commitment book (filled vs remaining, pricing status, market value)

**Standard capabilities** — present in most mature products:

- grower portal/app, e-signature, offer status sync
- relationship records for the origination desk
- discount schedules / premium-discount tables
- market data and market-value tracking
- multi-location bid and delivery pricing
- payment and settlement visibility, reporting

**Variant / optional** — depends on business model, region, and posture:

- futures order placement inside the desk
- embeddable bid widgets, farm-management pairing
- brokered intermediation (broker notes, brokerage invoices)
- full custody/settlement extension (deliveries, inventory, settlements owned by the platform)
- regional payment instruments and deduction machinery

## Interfaces

### Bid / price publication surface

The buyer's public acquisition face.

- posted purchase prices by commodity, grade, delivery location, and window, kept current with the market
- primary actions: set and update bids, push updates to all channels, embed on external sites

### Offer management desk

The merchandiser's acquisition queue.

- incoming grower offers with quantities and terms; current posted bids; status of pending decisions
- primary actions: review, accept, reject; watch minimum-size and validity constraints where configured

### Contract records

The unit of commitment and the system's central record.

- contract number, type, counterparty, commodity, grade(s), quantity and quantity remaining, price or pricing basis, delivery location(s), delivery window, end date, status
- primary actions: create, price or reprice, sign, print/PDF/share, follow status

### Commitment / position view

The buyer's acquisition position at a glance.

- open commitments by commodity and location; filled versus remaining quantities; unpriced exposure and current market value
- primary actions: monitor exposure, initiate pricing actions, drill into a contract

### Customer (grower) view

The relationship record behind the commitments.

- each grower's activity, contracts, balances, payment history
- primary actions: follow up, log contact, review readiness to sell

### Grower portal / app

The grower's self-service surface.

- available prices across buyers and sites (on network products), own offers, contracts, balances, payments
- primary actions: submit or edit an offer, accept a bid, price an unpriced contract, sign documents, review settlements

### Settlement and payment visibility

The money view of fulfilled commitments.

- settlement summaries, payment records, direct-deposit enrollment where offered
- primary actions: review settlements, manage payment details

## Important Rules / Behaviors

### Acceptance is a binding, timestamped act

An accepted offer is not the end of a conversation; it is the moment the price locks, recorded with a timestamp that protects both sides. The contract follows from the acceptance rather than from later paperwork.

### Posted prices are living configuration

The bid layer is tied to market movement and fanned out to every channel at once. Consistency across channels is a behavior of the machinery, not a discipline imposed on staff — one update, everywhere.

### Contract terms govern what is owed

Delivery windows, quantity tolerances, and payment terms are held as structured data on the contract, and where a contract covers several grades or alternative delivery sites the price consequences are structured on the contract too (spreads and adjustments) rather than improvised. These terms will drive settlement downstream.

### Unpriced commitments live with the market

A contract whose price is not fixed remains open to pricing actions and is monitored at its current market value. The commitment book therefore moves with the market until every contract is priced and filled.

### Fulfillment is tracked contract-side; custody is tracked elsewhere

The origination record knows how many bushels remain against each contract. The scale ticket, the storage location, and the settlement computation belong to the receiving/custody system — the elevator's system of record — unless the platform deliberately spans the whole chain. The seam is explicit in how the products integrate: origination platforms read tickets, settlements, and bin levels from the back office, and write contracts and payments into it.

### Offers are firm and quantity-bounded

Grower offers commit a specific quantity at specific terms; products may enforce minimum offer sizes and validity rules. This is what makes an offer's acceptance contractible without renegotiation.

## Variants

- **Standalone origination layer over a grain ERP** — bids, offers, contracts, relationships, and payments operated on top of the buyer's existing back-office system, which keeps tickets, inventory, and the books (the integration-first posture)
- **Origination module inside a grain or ag-retail ERP** — the same offer, contract, and market-value machinery embedded beside inventory, accounting, and logistics in one suite serving elevators, feed mills, and ethanol plants
- **Full-chain platform** — origination machinery plus the chain's custody and money legs in one product: deliveries, inventory, settlements, and even inventory funding alongside contracts and prices
- **Single-buyer desk vs network platform** — one buyer operating its own acquisition surface vs a network where growers see many buyers' posted prices across sites on one board
- **Brokered intermediation** — brokers originate on buyers' behalf, with broker notes and brokerage invoicing as first-class records
- **Grower-engagement pairing** — buyers licensing farm-management tools to their growers so marketing decisions (and offers) arrive earlier and more confidently
- **Regional machinery** — different settlement instruments and deduction regimes (quality-discount schedules in North America; tax-invoice settlements with levy and royalty deductions, and pricing of warehoused grain, in Australia) around the same acquisition core
- **Marketplace-style listing posture** — dedicated online grain marketplaces exist in the market; they were not directly researchable for this document, so this posture is noted at the network-price-board level rather than asserted

A variant remains a **Variant** unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies. A product that only manages trading positions without grower-facing acquisition is a different Type; a product that only weighs and settles delivered grain without publishing prices or forming commitments is the elevator system beneath this one.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Grain Elevator Management | downstream sibling (most important seam) | the facility's full commerce system of record: ticketed movements, settlement money loop, storage-located inventory. Origination ends where the ticket, the bin, and the settlement begin; the two share offers and contracts, and full products straddle the seam |
| Grain Management | adjacent (physical layer) | manages the physical condition of grain in storage (temperature, moisture, aeration); no acquisition machinery, no commercial records — disjoint cores |
| Agribusiness ERP | packaging parent | runs the whole grain or ag-retail business; origination machinery appears inside it as a module rather than as the product's center |
| Farm Management Platform | other side of the transaction | grower-side production, finance, and marketing-decision records; origination is the buyer-side mirror of the same grain, and the two are often paired products |
| Commodity Trading & Risk Management | adjacent (paper side) | trading positions and hedging without grower-facing acquisition semantics (delivery locations, grade machinery, grower counterparties) |
| Customer Relationship Management (generic) | contained capability | the origination desk's relationship records serve acquisition toward bushel commitments; generic CRM has no bid, contract-as-commitment, or pricing-basis semantics |
| Online Marketplace | adjacent (network posture) | multi-buyer price boards let growers compare offers on one platform; marketplaces centered on listing and matching grain between many parties are a related but distinct business, not directly researched here |

The most important boundary is with **Grain Elevator Management**: the two Types share the contract and the grower relationship, and modern products straddle the seam in both directions. The structural line is custody and settlement — the elevator system owns the scale ticket, the bin, and the money owed for delivered grain; origination owns how the commitment to deliver was priced, formed, and tracked.

## Representative Products

- **Bushel** — digital origination and payments layer operated by grain traders and processors over their existing ERPs; grower-app-first offer capture, cash-bid management, contract automation, and CRM
- **AgriDigital Platform** — Australian agri-commodity supply chain platform spanning contracts, posted prices, deliveries, inventory, settlements, and finance; network posture with many buyers' prices visible to growers
- **Agvance Grain (Grower360)** — grain module of a cooperative ag-retail ERP, with the offer platform, e-signed contracts, and contract market-value tracking operated through the grower portal
- **Ever.Ag CMS** — commodity merchandising ERP for elevators, feed mills, and ethanol plants; origination machinery (CRM, contract lifecycle, position) embedded beside inventory and grain accounting

The defining core was checked across these four packaging postures — standalone layer, network platform, ERP module, and embedded merchandising suite — and across two regions (North America, Australia). A dedicated online grain marketplace (Grain Discovery) could not be directly examined; see Sources.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Bushel — https://www.bushelpowered.com/agribusiness/grain , https://www.bushelpowered.com/challenges-we-solve/drive-origination , https://www.bushelpowered.com/agribusiness/solutions/trade , https://www.bushelpowered.com/release-notes
- AgriDigital — https://www.agridigital.io/ , https://www.agridigital.io/agridigital-platform ; Help Centre: https://knowledgebase.agridigital.io/en — notably "Contracts for Buyers", "Prices for Growers", "Definitions of common terms"
- Agvance (Software Solutions Integrated) — https://agvance.net/products/grain , https://agvance.net/products/grower360
- Ever.Ag — https://ever.ag/agribusiness/cms/

> Sourcing limitations: Grain Discovery's site is an application that could not be read without JavaScript, so marketplace-posture products were not directly examined; the Bushel knowledge base timed out (it was also unreachable during the neighboring grain-elevator research), and Bushel's evidence rests on official product pages and public release notes; Ever.Ag and Agvance surfaces are product pages rather than operational help centers. Vendor performance figures encountered during research (offer durations, bushel volumes, fill-rate percentages, hours saved) are vendor claims and are intentionally not asserted in this document. Contract-type vocabularies beyond the documented mechanics (price now or price later, pricing basis, grade and location spreads, delivery windows) are not asserted. Detailed observations, cross-product comparisons, and per-product evidence are recorded in the paired Research Notes.
