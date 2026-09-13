# Freight Brokerage Platform

## Overview

A **Freight Brokerage Platform** is the business system of record a freight brokerage runs on: it holds each load of freight a shipper customer needs moved as a persistent record, prices that load on both sides of the transaction — what the shipper will pay and what the carrier will be paid — sources the trucking capacity from a vetted network of independent third-party carriers, commits a carrier to the load, follows the move from pickup to delivery, and then bills the shipper and pays the carrier.

The business it serves is an intermediary: a freight brokerage sells transportation it does not itself perform. It wins a shipper's load at one price, buys the capacity to haul it from a motor carrier at another price, and manages the spread between the two as its revenue. The platform is the software embodiment of that middle position. Its defining core is small:

```text
Load (the unit of business record)
  ├── sold side: customer charge
  ├── bought side: carrier pay        ← the spread = the brokerage's margin
  └── supply: independent third-party carriers (vetted, committed, settled)
```

Everything else the market associates with the category — load-board integrations, carrier compliance programs, driver apps, customer portals, quick-pay and factoring, AI document extraction — is standard equipment that mature products add to this spine, not what makes the product a brokerage platform. The category's pre-history is the paper brokerage office: a logbook of loads, a carrier file with authority and insurance copies, a phone, rate-confirmation sheets, and a checkbook. The software digitized that office; the two-sided intermediary business defines the Type.

Remove the resale economics and what remains is a shipper's Transportation Management System or a dispatch board. Remove the third-party carriers and what remains is a trucking company's system. Remove the load lifecycle and what remains is a rate calculator and a contact list.

## Users & Context

The platform is operated by the brokerage's own staff, whose roles shape how the system is used:

Primary users:

- **Dispatcher / load manager** — the operational core: covers loads by finding and committing carriers, dispatches them, chases status, works exceptions, and shepherds each load from coverage to delivery.
- **Carrier sales rep** — sources and recruits capacity: finds carriers for lanes, negotiates carrier rates, maintains the relationships that make future loads coverable.
- **Accounting / finance staff** — invoices customers, audits carrier bills against the agreed rate, resolves discrepancies, pays carriers, and manages credit and factoring.

Secondary users:

- **Brokerage administrator** — manages users, roles, offices, and the standing configuration (customers, carriers, rate terms, integrations).
- **Agents** — in brokerages organized around independent agents, the platform carries per-agent books of loads and split economics (a variant posture).
- **Counterparties as connected users** — shippers access customer-facing portals to quote, book, and track; carriers and their drivers receive assignments, send status, and upload documents through portals, driver apps, or messaging. In some platforms these counterparties are full users of a shared network; in others they are external parties reached through integrations.

The working context is fast-moving and margin-sensitive: loads are quoted and covered at speed, rates move with the market, carrier capacity is contested, and a load's profitability is decided at booking and protected again at settlement. Most sampled deployments are North American truckload and LTL brokerages; the intermediary pattern itself is not tied to one regulator or country.

## Core Model

### The Defining Core

**Load.** The central object: one freight movement for a shipper customer, held as a persistent, individually identified record. A load carries the commercial frame (customer, lane, equipment, dates) and the terms that make the business work — **both prices**: the rate the customer agreed to pay and the rate the brokerage agreed to pay the carrier. Everything else hangs from the load: the documents, the status events, the invoices, the carrier payment. Demand enters the platform in several ways — entered by hand, received as an electronic tender from a shipper's system, requested through a customer portal, or extracted from an email — and becomes a load record either way.

**Two-sided price and margin.** On each load the platform holds the sold side and the bought side, and the difference between them is the load's margin. This is not reporting decoration; it is the structure the whole system serves. Margin is locked at booking, watched during execution (accessorials and service failures can change it), and reconciled at settlement — where the customer's invoice and the carrier's bill are each checked against their agreed terms.

**Carrier network.** The supply side is a standing population of independent third-party motor carriers, held as records with their identity, operating credentials (operating authority, insurance), contacts, equipment, and history. Carriers are sourced, vetted, onboarded, committed to loads, scored after loads, and paid — all as managed records in the platform. The brokerage does not operate trucks; in the defining posture it owns none. (Products that also run a fleet alongside the brokerage exist and are treated as a hybrid variant below.)

### How the Objects Relate

```text
Shipper customer
   ↓  (tender / quote request / entry)
Load ── sold at: customer charge ──→ invoiced on delivery → cash in
   │
   │  sourced from
   ↓
Carrier network (vetted records)
   ↓  committed via tender / rate confirmation
Carrier pay ──→ carrier bill audited against the agreed rate → paid
   │
   └── execution: dispatch → tracking events → documents → delivery
```

The load is the center; the two prices are its commercial identity; the carrier network is the substrate that makes the bought side real.

### Standard Capabilities

Mature products commonly add:

- **Carrier lifecycle management** — sourcing and recruiting, credential verification (operating authority, insurance), onboarding packets and registration, compliance monitoring as credentials expire, and performance scorecards built from completed loads.
- **Capacity-sourcing surfaces** — search and posting on external load boards, broadcast/offer-out to the carrier network and contact lists, routing guides and bid boards that automate how a load is offered to candidate carriers.
- **Dispatch and tracking** — carrier selection and assignment, dispatch communication, event-driven status from the truck (driver apps, telematics/ELD connections, tracking services, or driver check-ins), exception alerts, and proof-of-delivery capture.
- **The document trio and its paper trail** — rate confirmation to the carrier, bill of lading traveling with the freight, signed proof of delivery closing the loop; document imaging and extraction feeding the record.
- **Settlement in both directions** — customer invoicing (commonly triggered at delivery), carrier-bill audit against the rate confirmation (reweighs, reclassifications, accessorials), discrepancy handling, carrier payment including expedited "quick pay" options, and connections to factoring and payment providers.
- **Customer self-service** — white-label portals where each shipper quotes, books, tracks its own loads, and retrieves documents, isolated from other customers' data.
- **Margin and performance analytics** — revenue and margin by load, lane, customer, and carrier; carrier scorecards; sales commissions.
- **Integration spine** — electronic tenders and status updates with shipper systems (EDI/API), load boards, tracking and visibility providers, carrier onboarding/identity services, accounting systems, and payments/factoring services.

## How It Works

The canonical loop runs from demand to settled cash, and it runs on a clock — coverage is competitive and minutes matter.

### 1. Demand becomes a load

```text
Tender arrives (shipper EDI/API, portal request, email, phone)
→ load created with customer, lane, equipment, dates
→ customer charge quoted or pulled from contract terms
```

### 2. The load is covered

```text
Search capacity: carrier network, load boards, routing guide
→ broadcast/offer the load to candidate carriers
→ negotiate or accept a carrier rate
→ commit: send the rate confirmation / dispatch the carrier
```

Coverage is the platform's first act of margin-making: the dispatcher chooses between a known carrier, a broadcast response, and a board option, with the carrier pay against the customer charge visible at the moment of choice. The rate confirmation — the document stating what the carrier will be paid and what it agreed to haul — is the commitment artifact of the Type; a load with a rate confirmation out is spoken for, and an uncovered load is the brokerage's burning problem.

### 3. The move is executed and tracked

```text
Dispatch instructions to the carrier/driver
→ status events flow in (driver app, telematics, tracking service, check-ins)
→ exceptions surface: late pickup, delay, no capacity at the dock
→ documents accumulate: BOL out, signed POD in
```

Status is event-driven from the executing carrier, not self-declared by the brokerage. Mature products replace manual check calls with automated feeds and alerts; the dispatcher's job shifts from asking "where is it" to working the loads that need attention.

### 4. Both directions settle

```text
Delivery confirmed (POD)
→ customer invoice issued → cash collected (credit terms, or factored)
→ carrier bill arrives → audited against the rate confirmation
   ├── matches → paid (standard terms or quick pay)
   └── differs (reweigh, reclass, accessorial) → discrepancy worked
→ margin recorded on the load
```

The carrier-bill audit is the bought-side mirror of the sold-side invoice: every charge is checked against what was agreed, because the spread is the revenue. Payment machinery connects to the financial system — carrier payments, expedited pay, and factoring relationships in which carriers sell the receivable to get paid sooner.

### Capability Tiers

**Defining core** — without these, not a freight brokerage platform:

- load as the persistent unit of business record
- two-sided price (customer charge and carrier pay) held and settled on the same load
- independent third-party carrier network as the supply side, held as managed records
- the quote → cover → haul → deliver → bill → pay lifecycle

**Standard capabilities** — present in most mature products:

- carrier vetting/onboarding/scorecards; load-board and broadcast sourcing; routing guides
- dispatch, event-driven tracking, exception management
- rate confirmation / BOL / POD documents
- both-direction settlement with bill audit, quick pay, factoring connections
- customer self-service portals, margin analytics, commissions
- EDI/API integration with shippers, accounting sync

**Variant / optional** — depends on posture, mode mix, and era:

- hybrid asset-based operations (own fleet alongside the brokerage)
- multi-seat network posture (shippers/carriers as platform users)
- LTL rating depth via direct carrier connections; drayage, refrigerated, intermodal scope
- embedded finance depth; agent books; AI agents for quoting, tracking calls, document extraction

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Load board / load workbench

The dispatcher's home: loads in flight with their state, and the coverage queue.

- typical information: load ID, customer, lane, pickup/delivery dates, equipment, customer charge and carrier pay, margin, status, coverage state, exception flags
- primary actions: create load, search/post capacity, offer or broadcast to carriers, commit a carrier, dispatch, filter by status or customer

### Load detail

The record view of one load's whole life.

- typical information: parties, stops, contents/equipment, both agreed rates, assigned carrier, status timeline and events, documents (rate confirmation, BOL, POD), charges, notes
- primary actions: edit, re-cover/cancel, send documents, record events, attach files, invoice, pay carrier

### Capacity sourcing view

Where the dispatcher hunts trucks.

- typical information: matching carriers with history and scorecards, load-board results, broadcast responses, rate references for the lane
- primary actions: compare options, contact carrier, negotiate rate, send rate confirmation

### Carrier profile

The standing record of one carrier in the network.

- typical information: identity and credentials (authority, insurance with expiry), onboarding/packet state, equipment, contacts, loads hauled, performance
- primary actions: verify credentials, approve/onboard, view loads, score, deactivate

### Customer portal (counterparty-facing)

The shipper's window into the brokerage, usually white-labeled.

- typical information: the customer's own quotes, loads, statuses, documents
- primary actions: request quote, book, track, download documents

### Settlement / accounting screens

The money side, both directions.

- typical information: invoices issued and their aging, carrier bills pending audit, discrepancies, payables, quick-pay eligibility
- primary actions: invoice, match/audit bill, dispute, approve, pay, sync to accounting

### Analytics / dashboards

- typical information: revenue, margin per load/lane/customer/carrier, coverage speed, carrier performance
- primary actions: drill down, export, build reports

### Administration

- typical information: users, roles, offices/divisions, customers, carrier terms, integrations
- primary actions: manage users and permissions, configure customers and carriers, connect integrations

## Important Rules / Behaviors

### The load carries two prices, and both bind

The customer charge and the carrier pay are each commitments. The customer invoice is generated from the agreed sold rate; the carrier bill is checked against the agreed bought rate. Margin lost after booking — through accessorials, reweighs, or service-failure concessions — is a visible event, not a rounding error.

### A covered load is not a hauled load

Sending a rate confirmation commits a carrier, but execution depends on the carrier actually showing up with a truck. No-shows and late coverage are structural exceptions of this business; the platform's sourcing surfaces exist so a load can be re-covered quickly, and its tracking feeds exist so the failure is seen early.

### Status comes from the carrier, not the brokerage

The platform is the system of record for the transaction, but the executing carrier generates the truth: driver-app actions, telematics, tracking services, or human check-ins. A brokerage's visibility is only as good as its connectivity to its carriers — which is why carrier communication channels are structural, not optional.

### Credentials gate the network

Loads are committed only to carriers whose credentials are on file and current. Operating authority and insurance verification are the entry ticket to the bought side; expired insurance or unverified identity takes a carrier out of the coverable pool. Fraud in this market (loads resold by unverified intermediaries) makes the vetted-network property commercially central, though the depth of tooling varies by product.

### Settlement is asymmetric by design

The customer is billed after performance; the carrier may be paid on terms, paid early through quick-pay arrangements, or paid promptly through a factoring relationship in which the carrier sells the receivable. The platform must manage these different cash rhythms against the same load record — and the discrepancy workflow when the carrier bills differently than the rate confirmation says.

### Counterparty data is isolated

Each shipper sees its own loads and documents; carrier commercial terms are not customer-visible. The platform enforces visibility boundaries between the two sides it stands between.

## Variants

- **Pure brokerage platform** — the dominant form: no trucks anywhere in the business; the platform is purely the intermediary's system (vendors in this pole explicitly exclude asset-based companies from their target market).
- **Hybrid / asset-based brokerage** — the brokerage also runs trucks; one product toggles between carrier-side operations (drivers, fleet, driver settlement) and brokerage-side operations (loads tendered out) on a shared substrate. The load record may be hauled either by the fleet or by a third-party carrier.
- **3PL use** — logistics providers running broker-like operations across multiple clients; multi-client structure added to the same operational frame.
- **Multi-seat network platform** — one platform where shippers, carriers, and brokers are all participants sharing the same shipment record; the brokerage is one seat of a network rather than the sole owner of the system.
- **Mode-scope variants** — truckload-centric, LTL-centric (with direct carrier rating connections), partials, drayage; refrigerated and other niches.
- **Digital-first brokerage operations** — brokerages whose platforms are operated as customer-facing services (instant quoting, app-based booking) rather than behind-the-scenes tools; the system of record underneath is the same Type.
- **Agent-model brokerages** — the platform carries per-agent books, split commissions, and subsidiary/offices structure.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System / TMS | sibling, other side of the transaction | A TMS is the shipper's (or 3PL's) operational system for its own freight: it buys carriage but holds only the procurement side, with no resale. The brokerage platform holds both sides of a transaction it is a principal to. Products may serve both seats from one family; the seat and the held economics separate the Types. |
| Trucking Management System | sibling, opposite supply identity | The carrier's system runs trucks under its own authority — drivers, fleet, maintenance, driver settlement. The brokerage never operates the trucks it sells. Hybrid asset-based brokers run both in one product. |
| Load Board / Freight Marketplace | adjacent, venue vs system of record | The load board is the external market where many brokers and carriers meet; the brokerage platform is one brokerage's business record. Integration with boards is standard; membership in the venue is not part of this Type. |
| Dispatch Management | adjacent, different center | Dispatch centers the assignment act over a live board, domain-generic. A brokerage contains dispatch-like machinery, but its center is the two-sided commercial record across the full quote-to-settle lifecycle. |
| Freight Forwarding System | adjacent, different document world | Both are asset-free intermediaries; the forwarder's center is international consignment machinery (multi-leg carriage, forwarder documents and charges, ocean/air bookings). The brokerage's center is domestic truckload/LTL buy-sell on rate confirmations. |
| Freight Audit & Payment Platform | adjacent, whose payables | FAP runs the shipper's freight-payables control over invoices from carriers it does not transact with. The brokerage's settlement is internal to its own transaction — it audits its own suppliers against its own rate confirmations. |
| Shipment Visibility Platform | adjacent, watching vs transacting | Visibility tracks moves without committing, pricing, or settling. Tracking feeds flow into the brokerage platform; the visibility product holds no two-sided price. |
| Courier / Last-mile Delivery Platforms | different capacity model | Courier platforms run or orchestrate an operator's own fulfillment workforce; the brokerage procures licensed third-party motor carriers for full loads. |
| Customer Relationship Management | capability inside | Shipper prospecting and carrier recruiting live inside brokerage platforms as CRM-like modules; the CRM is not the system of record for the load. |

The two boundaries that matter most: against the **shipper-side TMS** (the brokerage resells and holds the margin; the TMS executes moves it owns operationally), and against the **trucking seat** (whose trucks and whose authority). The load board seam is a standing joint-review point, since brokerage platforms and load boards are commercially intertwined without being the same Type.

## Representative Products

- **Tai TMS** — brokerage-native pure-play platform (now part of Descartes); explicitly positioned for freight brokers and 3PLs and not for asset-based companies; quote-to-invoice automation across truckload and LTL.
- **Alvys** — all-in-one platform sold to carriers, brokers, and hybrid asset-based brokerages; shows the shared substrate and the hybrid posture.
- **Turvo** — multi-seat collaborative network platform sold to brokers, 3PLs, shippers, and carriers; the straddling posture across the TMS seam.

The model was checked against the pure-brokerage pole, the hybrid pole, and the multi-seat network pole, and against the historical paper-era brokerage office (load logbook, carrier file, phone quotes, rate-confirmation sheets, checkbook) to avoid defining the Type by any single era, vendor, or interface.

## Sources

Research date: **2026-09-08**

- Tai Software — homepage: https://tai-software.com/
- Tai Software — Freight Broker TMS FAQ (22 answers, incl. capability blocks, integrations taxonomy, target-seat exclusions): https://tai-software.com/freight-broker-tms-faq/
- Alvys — homepage: https://www.alvys.com/
- Alvys — Freight Broker TMS page: https://alvys.com/freight-broker-tms
- Alvys — Help Center (loads & trips, accounting & settlements, safety & compliance, integrations index): https://help.alvys.com/en/
- Turvo — homepage: https://turvo.com/
- Turvo — Freight Brokers page (roles, routing guides, driver app, integration categories): https://turvo.com/freight-brokers/

> Sourcing limitation: the traditional enterprise brokerage-suite pole (McLeod Software; MercuryGate; legacy Descartes brokerage products) could not be reached from the research environment (HTTP 403 / unreachable), and one widely used SMB product renders as a JavaScript application (unreachable after repeated attempts). Claims in this document rest on the three reachable products above, which cover the pure-brokerage, hybrid, and multi-seat postures. Precise operational parameters (payment-term defaults, audit tolerances, specific document formats' field lists, carrier-verification rule details) are intentionally not asserted. Detailed evidence, the cross-product comparison matrix, and the boundary joint-review notes are recorded in the paired Research Notes.
