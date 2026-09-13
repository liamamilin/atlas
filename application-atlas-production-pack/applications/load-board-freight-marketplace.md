# Load Board / Freight Marketplace

## Overview

A **Load Board / Freight Marketplace** is the shared market venue of truckload freight: freight brokers and shippers publish their available loads as postings, motor carriers and owner-operators search those postings and respond to them, and the venue mediates the match between a specific load and a specific carrier.

The defining structure is small:

```text
Many independent capacity holders (brokers, shippers), one shared venue
└── Load posting (identified offer of one freight movement)
    └── Carrier-facing discovery over the whole pooled population
        └── Response path returning a carrier's interest to the poster
            └── The match: a specific load committed to a specific carrier
```

Three properties hold across every realization of the Type:

- **The load posting as the unit of market record.** A posting is an identified offer of one freight movement — where it goes, what equipment it needs, when it picks up, how heavy it is, and what it pays or is expected to pay — published by an identified capacity holder. The venue's content is a rolling population of these offers.
- **A pooled, searchable market.** Postings from many independent brokers and shippers are aggregated into one population that carriers can filter and compare across posters. The venue is operated by a party separate from the participants; it is not any single participant's system of record.
- **A response path back to the poster.** Each posting carries or mediates a way for a carrier's interest to reach the poster — a phone contact, a bid, or an in-platform booking. The response produces the match; the venue's own job is complete once the load is spoken for.

Everything else the market associates with load boards — structured search filters, lane rate data, carrier verification, broker credit scores, saved searches and alerts, in-app booking, mobile apps — is standard equipment that mature products add to this spine, not what makes the product a load board. The category's own histories describe its pre-history as a cork board and push pins: brokers' loads pinned where drivers could read them, matches made by phone. The software digitized that board; the pooled market with a response path defines the Type.

Remove the pooled multi-poster market and what remains is one broker's private posting feed — a coverage surface inside a freight brokerage's own system. Remove the response path and what remains is a read-only rate-data service. Remove the load postings and nothing freight-specific remains at all.

## Users & Context

**Carriers and owner-operators** are the demand side. They arrive with trucks to fill: searching by lane and equipment, comparing rates and deadhead miles, checking who is offering the load and whether that poster pays reliably, and responding to the loads they want. Their decisions are per-mile economics — a load's value depends on what it pays relative to the miles driven empty to reach it and after delivering it.

**Freight brokers and shippers** are the supply side. They post the loads they need covered — brokers moving their customers' freight, shippers moving their own — and manage the responses that come back: fielding calls, reviewing bids, booking the carrier they choose. Posting is increasingly automated from their own operating systems rather than typed by hand.

**The venue operator** runs the market: admission and verification of participants, the quality and reach of the posting pool, search and matching machinery, and (in some postures) the transaction itself.

The work context is fast and cyclical. Loads are posted and covered the same day; a truck looking for its next load is searching hours before it is empty; rates move with the market. Trust is structural: carriers commit equipment and time to counterparties they may never have met, and posters hand freight to carriers they must be able to hold accountable — so both sides lean on the venue's verification and credit information.

## Core Model

### The load posting — the unit of market record

A posting is a structured offer of one freight movement. Across the researched products it consistently carries:

- the lane: origin and destination (with distances, and deadhead miles from the carrier's likely position)
- the equipment type required (dry van, reefer, flatbed, step deck, power-only, hot shot, and similar truckload equipment categories)
- the schedule: pickup date or window, delivery expectation
- the freight facts: weight, sometimes commodity or reference number
- the commercial frame: the rate — as a dollar figure, a rate per mile, or (in marketplace postures) a bookable upfront price
- the poster's identity: which broker or shipper is offering the load

Postings are **time-bounded by the market itself**: a load that gets covered leaves the board, an uncovered load stays visible and ages. The board's content is therefore a rolling current population of freight seeking trucks — not a permanent registry.

### The pooled market — many posters, one venue

The population aggregates postings from many independent capacity holders under one operator. This is the property that separates a load board from a single brokerage's private posting feed, and it is what gives the board its value to carriers: one search reaches hundreds of posters' freight. It is also what gives the board its value to posters: the posting reaches a carrier population no single broker could address alone. In the neutral posture the venue holds no side of any transaction — it states plainly that prices and conditions are set by the posters, not by the venue.

### The carrier-side presence

A carrier's presence on the board consists of:

- **identity and equipment**: an account bound to the carrier's operating identity, with the equipment it can haul
- **verification credentials**: operating authority and insurance on file — in mature products a prerequisite for bidding or booking, not just a profile field
- **search state**: saved lanes and searches, alerts, saved loads — standing queries against the posting population

### The response path and the match

The response path is where the market actually clears, and its depth is the Type's main spectrum:

- **contact** — the posting exposes the poster's contact; the carrier calls, negotiates, and the match is made off-venue (the classic model; the industry's rate-confirmation document seals it)
- **bid** — the carrier submits a price or interest in-platform; the poster reviews responses and chooses
- **book** — the carrier commits in one step at a displayed price; the venue records the match directly

In all three, the outcome is the same structural event: a specific load becomes committed to a specific carrier. What happens next — dispatch, tracking, documents, payment — belongs to the participants' own systems, not the board's (with the partial exception of marketplace postures that keep more of the transaction in-platform).

### How the objects relate

```text
Broker / shipper (capacity holder)
   ↓  posts (manually, or automated from its own TMS/API)
Load posting ── lane · equipment · dates · weight · rate
   ↓  joins
Pooled posting population (rolling, many posters)
   ↓  searched & filtered by
Carrier / owner-operator (capacity seeker)
   ↓  responds: contact · bid · book
THE MATCH — load committed to carrier
   ↓  (off-venue in the classic model)
rate confirmation · dispatch · haul · documents · payment
   (participants' own systems)
```

### Standard capabilities

Mature products commonly add:

- **Search and discovery machinery** — structured filters over lane, equipment, dates, rate and rate-per-mile, weight, and deadhead distance; map views; saved lanes and searches; alerts by email, text, or push.
- **Rate and market data** — per-posting rates; lane rate tools computed from accumulated load records; market and fuel context for pricing decisions.
- **Two-sided trust machinery** — carrier-side verification (operating authority, insurance documents) required before a carrier can bid or book; poster-side credit information (credit scores, full credit reports, days-to-pay, authority and insurance status) exposed to carriers choosing whom to haul for.
- **Poster-side management** — dashboards for posted loads and incoming responses; posting automation from brokerage TMSs via API, file upload, email, or integration partners; private (restricted-visibility) loads; team posting management.
- **Document exchange** — storing and sending the paperwork that accompanies a match (rate confirmations, bills of lading, proof of delivery), with depth varying by product.
- **Backhaul tooling** — deadhead estimates, backhaul search before the current load is even delivered, multi-leg booking.
- **Mobile-first carrier surfaces** — driver-facing apps with the full search-and-book loop; web consoles for the poster side.

### One structure, many implementations

The core model is written in conceptual terms; products realize each piece differently:

```text
Concept:            the load posting
Implementations:    broker-typed posting, TMS-automated posting,
                    cross-posted feed, marketplace-held offer at a set price

Concept:            the response path
Implementations:    phone contact, in-app bid, instant book-now

Concept:            trust machinery
Implementations:    uploaded authority/insurance documents, linked broker
                    accounts, credit scores and days-to-pay reports

Concept:            rate information
Implementations:    rate on the posting, lane rate tools from load records,
                    upfront bookable prices
```

A reader who has only seen one implementation — say, an app where tapping "book" commits the load — should still be able to recognize the classic call-the-broker board, and the cork-board before it, from the core model.

## How It Works

The Type runs two mirrored loops — the poster's and the carrier's — that meet at the match.

### The poster's loop

```text
Load needs a truck
→ create the posting (typed, or automated from the brokerage TMS
   via API / file upload / email / integration partner)
→ publish into the pooled population
→ manage: adjust rate, restrict visibility, repost, expire
→ responses arrive: calls, bids, booking requests
→ choose and commit a carrier — the load is covered and leaves the board
```

For a broker, the board is one sourcing surface among several (its own carrier network, its broadcast lists); for a shipper without a carrier network, it may be the primary one. Postings compete against every other posting on the board for the same trucks, which is why rate accuracy and poster reputation are poster-side obsessions.

### The carrier's loop

```text
Truck needs a load (often before the current one is even delivered)
→ search the pool: lane, equipment, date, rate floor, max deadhead
→ evaluate postings: rate per mile, weight, pickup window,
   poster's credit and days-to-pay
→ respond: call the poster, submit a bid, or book instantly
→ match made — the board's job is done
→ haul, documents, and payment proceed in the participants' own systems
```

The search is economic, not just textual: carriers filter by rate-per-mile and deadhead because the truck's profitability is decided per mile. Saved lanes and alerts exist because the same truck works the same corridors repeatedly — the carrier is really running a standing query for profitable work.

### The reverse direction (two-direction boards)

Classic boards also run the mirror image: carriers post available trucks (equipment, origin, available date), and brokers and shippers search the truck population and its map. The structure is identical — posting, pooled population, response path — with the roles exchanged. Marketplace postures typically omit it: the carrier signs up, and freight is surfaced to the carrier rather than the carrier advertising capacity.

### Capability tiers

**Defining core** — without these, not a load board:

- the load posting as the identified unit of market record
- the pooled population of many independent posters, searchable as one market
- the response path returning carrier interest to the poster and producing the match

**Standard capabilities** — present in most mature products:

- structured search/filter, saved searches, alerts, maps
- rate and lane-rate data; market/fuel context
- carrier verification and poster-side credit information
- posting automation and poster dashboards
- document exchange; backhaul/deadhead tooling; mobile carrier apps

**Variant / optional** — depends on posture and segment:

- in-platform booking at displayed prices (marketplace postures)
- truck postings and the reverse search direction (classic boards)
- aggregation of postings from other boards and sources
- embedded finance (factoring, quick pay, fuel programs)
- AI dispatch and matching assistants

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Load search results (the board itself)

The carrier's primary surface: the current posting population, filtered.

- typical information: origin/destination, equipment, pickup date, rate and rate-per-mile, weight, deadhead estimate, poster identity, age of posting
- primary actions: filter and sort, save the search or lane, open a posting, set alerts

### Load detail

One posting in full, with its poster.

- typical information: complete lane and schedule, equipment requirements, weight, rate detail, poster's credit standing (scores, days-to-pay, authority/insurance status), contact or action controls
- primary actions: call/contact the poster, bid, book, save, share

### Posting management (poster dashboard)

The broker/shipper's console over its own postings.

- typical information: posted loads and their state, views/responses/bids per posting, posting sources and automation status
- primary actions: create/edit/repost postings, adjust rate or visibility, review responses, book a responding carrier, take loads down

### Truck postings (two-direction boards)

The reverse market: carriers' available equipment.

- typical information: equipment type, origin/available date, contact
- primary actions: post a truck, search trucks, view the truck map, contact a carrier

### Rate / market data view

The pricing context layer.

- typical information: lane rates derived from load records, rate-per-mile references, market and fuel context
- primary actions: look up a lane, compare periods, use as negotiation reference

### Carrier profile / verification

The carrier's standing identity on the venue.

- typical information: operating identity, authority and insurance documents, verification state, equipment, history on the venue
- primary actions: upload or update credentials, connect linked accounts, maintain the profile

### Mobile carrier app

The driver-facing surface, commonly where the whole carrier loop lives.

- typical information: filtered load feed, saved lanes, alerts, booking state
- primary actions: search, evaluate, bid/book, track saved loads

## Important Rules / Behaviors

### A posting is an offer, not a commitment

Publishing a load creates no obligation on either side. The market clears only when a poster accepts a response (or an instant booking occurs); until then the posting competes in the pool and may age, be repriced, or be withdrawn. Covered loads leave the board — the population is always the freight still seeking trucks.

### The neutral venue holds no side of the deal

In the classic posture the venue holds no side of any deal: prices and conditions are set by the posters, not by the venue, and the venue takes no margin on the match. Its product is the market itself — reach, search quality, and trust information. (The marketplace posture, where the operator holds the transaction, is a variant — see below.)

### Verification gates participation

Mature products commonly gate bidding and booking on verified carrier credentials — operating authority and insurance on file. The gate exists because the venue's matches put strangers in commercial contact: an unverified participant is the raw material of freight fraud (loads resold by unauthorized intermediaries), a structural risk this market actively polices. Poster-side trust runs the other direction: carriers can see posters' credit standing and payment behavior before committing their trucks.

### Rate information is context, not (usually) a price

Lane rates and market data derived from load records inform negotiation; they do not commit anyone to a price. The exception is the marketplace posture, where the displayed price is the operator's own bookable offer.

### The board's job ends at the match

Dispatch, tracking, document flow, and payment belong to the participants' own systems (brokerage platforms, TMSs, trucking systems). The venue mediates discovery and trust; it is not the system of record for the haul. Products that keep more of the transaction in-platform are deepening into adjacent Types, not redefining this one.

### Per-mile economics shape the interface

Deadhead miles, rate-per-mile, and backhaul positioning are first-class posting fields and filter dimensions — because the carrier's decision is an economic one per mile, and the board's search machinery is the tool that decision runs on.

## Variants

- **Classic subscription board** — the long-dominant form: neutral venue, paid access tiers, postings from brokers and shippers, response by contact (call the poster), commonly two-direction with truck postings, plus rate tools and credit information as paid features.
- **Free venue / aggregator** — free access for both sides, funded by adjacent services (factoring, banking, fuel); often aggregates postings from other boards and sources into one surface, with linked-account access where posters restrict their loads; mobile-first, driver-centric.
- **Principal-operated digital marketplace** — the operator is itself a licensed freight broker: freight on the surface is the operator's own book, prices are upfront and bookable, and the transaction is held in-platform. This pole straddles toward the Freight Brokerage Platform Type — its marketplace surface is the venue leg; its held economics are the brokerage legs.
- **Two-direction boards** — boards that run the reverse market (truck postings, truck maps, brokers searching trucks) alongside load postings.
- **Mode and segment scope** — truckload-dominant (van, reefer, flatbed, step deck, power-only, hot shot); some marketplace postures extend to LTL and intermodal/drayage on the shipper side.
- **Regional regimes** — the researched sample is North American; other markets run equivalent exchange-style venues under their own regulatory regimes. The Type's definition is regime-neutral: credentials are "operating authority and insurance," not any one country's paperwork.
- **Embedded-finance depth** — factoring, quick-pay, fuel programs, and banking attached to the venue as adjacent products, especially in free postures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Freight Brokerage Platform | adjacent, venue vs system of record | The load board is the shared market where many brokers and carriers meet; the brokerage platform is one intermediary's business system of record (load as business record, two-sided price and margin, carrier network as procured supply). Integration with boards is standard capability in brokerage platforms; membership in the venue is not part of that Type. A brokerage's internal coverage board is a surface, not the marketplace. |
| Transportation Management System / TMS | adjacent, market vs execution | A TMS is one company's operational system for executing its freight moves; the board is the market for finding capacity to cover them. TMSs post to and source from boards; the board holds no execution record. |
| Trucking Management System | adjacent, whose operation | The carrier's own operations system (drivers, fleet, maintenance, settlements). A carrier uses both: the board to find loads, its own system to run them. |
| Job Board | same venue shape, different domain | Both are third-party venues where many independent posters advertise time-bounded postings to searching responders. The unit differs: a freight movement (lane, equipment, weight, rate, pickup window) vs a job opening; the participants differ: companies trading capacity vs employers hiring people; the response differs: a bid or booking on commercial terms vs a job application. Freight boards also carry market-rate data and credit/verification machinery job boards do not. |
| Classifieds Platform / Listing Marketplace | generic vs domain-structured | A generic listing venue lacks the load posting's structured freight semantics (equipment taxonomy, lane, weight, pickup window, rate per mile), the two-sided verification/credit machinery, and the booking/bid response path. |
| Dispatch Management | adjacent, market vs assignment | Dispatch is the assignment act inside one company's live operation; the board is the open market before and around that act. |
| Shipment Visibility Platform | adjacent, matching vs tracking | Visibility tracks moves already in flight; the board matches moves that do not exist yet. The board's job ends where visibility's begins. |
| Freight Forwarding System | adjacent, different document world | The forwarder's center is international consignment machinery (multi-leg carriage, forwarder documents and charges); the board's center is the domestic spot market for truckload capacity. |

The boundary that matters most is against the **Freight Brokerage Platform**: the two are commercially intertwined (brokers are the board's posters; boards are the brokerage's sourcing surfaces) without being the same Type. The structural test: strip the pooled multi-poster market from a board and a private coverage feed remains; give a venue its own two-sided books on each load and it has become a brokerage.

## Representative Products

- **Uber Freight** — principal-operated digital freight marketplace: the operator is a licensed freight broker (not a motor carrier), freight is bookable in-app at upfront prices, and the marketplace surface sits inside a wider logistics technology company.
- **TruckSmarter** — neutral free venue and aggregator: postings pulled from many brokers and sources into one searchable pool, in-app bid and book, carrier verification and broker credit checks, AI dispatch assistance; monetized through adjacent fintech rather than the board.
- **Direct Freight** — classic subscription board: two-direction (load postings and truck postings), lane rate tool computed from load records, poster-side credit and authority information, document storage, TMS integration partners.

The market's largest incumbents (DAT, Truckstop, 123Loadboard) could not be reached directly during research (access blocked); they are documented indirectly through the integration lists of brokerage platforms, which name them as the canonical boards brokers connect to. The core model was checked against the neutral-venue pole, the principal-operated pole, and the classic two-direction pole, and against the cork-board/phone-matching pre-history the category's own descriptions cite, to avoid defining the Type by any single era, vendor, or interface.

## Sources

Research date: **2026-09-09**

- Uber Freight — homepage: https://www.uberfreight.com/
- Uber Freight — Carriers ("Haul with us"): https://www.uberfreight.com/en-US/carriers
- Uber Freight — Uber Freight Shipping (shipper platform): https://www.uberfreight.com/en-US/technology/freight-shipping
- TruckSmarter — homepage: https://www.trucksmarter.com/
- TruckSmarter — Free load board page and FAQs: https://www.trucksmarter.com/free-load-boards
- TruckSmarter — Brokers page and Broker FAQs: https://www.trucksmarter.com/brokers
- TruckSmarter — Glossary: https://www.trucksmarter.com/glossary
- TruckSmarter — Help Center: https://help.trucksmarter.com/
- Direct Freight — homepage and feature list: https://www.directfreight.com/
- Context from prior sibling passes: Freight Brokerage Platform research and document (2026-09-08), Transportation Management System document, Job Board document.

> Sourcing limitation: DAT, Truckstop, and 123Loadboard (the market's largest classic boards) and the European freight-exchange pole were unreachable from the research environment (HTTP 403 / timeouts after repeated attempts). Claims in this document rest on the three reachable products above, which cover the neutral-venue, principal-operated, and classic two-direction postures; the incumbents are named only as market context, with no mechanism claims made about them. Precise operational parameters (posting fees, subscription prices, load-volume figures, verification rule details) are intentionally not asserted — figures found in competitor comparisons were treated as unverified and excluded. Detailed evidence, the cross-product comparison matrix, and the boundary joint-review notes are recorded in the paired Research Notes.
