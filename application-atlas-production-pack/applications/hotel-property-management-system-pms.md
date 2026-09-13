# Hotel Property Management System / PMS

## Overview

A **Hotel Property Management System (PMS)** is the lodging property's own staff-side system of record: it holds the property's bookable rooms — with their rates and availability — as the property's selling truth, holds the **reservations** that sell those rooms from whatever channel they arrive from, and operates each guest's **stay** on site from check-in through check-out, keeping the guest's **folio** as the stay's running account of charges and payments.

Everything the property runs day to day works on these same records: the front desk assigns rooms and settles folios, housekeeping publishes room readiness, rates and restrictions feed the property's distribution channels, charges flow in from the restaurant or spa, and the day is closed and reported at its end. A PMS is therefore wider than any single function — it is the property's central operating record, and the market's other hospitality systems (booking engines, channel managers, guest apps, POS, payment gateways, accounting) connect to it.

The boundary: it is the operator side, not the guest side; the property side, not the chain's selling layer; and it is defined by operating stays, not by the suite of marketing and revenue modules that current vendors commonly bundle around it.

## Users & Context

The PMS is worked by the property's staff, in a shift-based, interruption-driven environment where queue work (today's arrivals and departures) alternates with transactional work (one guest standing at the desk).

Primary users:

- **front desk agents / receptionists** — the largest user group: check-ins and check-outs, room assignment, payments and charges, walk-ins, stay changes.
- **reservations staff** (larger properties) — manage upcoming bookings, group blocks, and requests from travel agents and companies before arrival.
- **housekeeping staff and supervisors** — work from the PMS's room and task picture, updating room status as units are serviced.

Around them:

- **duty managers / supervisors** — handle exceptions: rate overrides, refunds, folio disputes, overbooking decisions.
- **night auditor** (in properties that staff the role) — performs the end-of-day close: balancing folios, posting room charges, rolling the business day.
- **general manager / owner** — reads occupancy, revenue and performance reports; in small properties also does the configuration.
- **accounting roles** (fuller products) — work the receivables, company invoices, and the property's financial reports.

One property — a hotel, hostel, resort, inn, apartment building — is the natural container for the system. Above it, groups and portfolios are a common extension, not the base shape.

## Core Model

The PMS's world is built on a small set of structures that all its modules share. Products name them differently (room, unit, space, area; bill, folio, guest account), but the structure recurs across the sampled products.

### The defining core

```text
Property
└── Bookable accommodation inventory
    │   (units: rooms / beds / spaces — grouped into categories,
    │    with rates, availability and selling restrictions over time)
    └── Reservation  (guest(s) × category × dates × price & terms;
        │             created in-house or received from any channel;
        │             modified or cancelled before arrival)
        └── Stay     (reservation becomes an in-house stay at check-in,
            │         assigned to a specific unit against live
            │         availability and room readiness)
            └── Folio (the stay's running account:
                       charges post during the stay,
                       payments settle against it,
                       balance closed at check-out)
```

- **The property's bookable inventory of record.** The property's own accommodation is held as individually identified units (a modern system models rooms, and generalizes to beds in dorms, apartments, function spaces or other sellable spaces), organized into categories — the level at which availability is counted and rates are attached. Availability — how many units of a category can be sold for which dates — is the property's own truth, and it is what the property's distribution reads. Selling controls such as minimum-stay requirements or closed-to-arrival dates qualify that availability.
- **The reservation of record.** A reservation is the property's recorded commitment to set aside a category of accommodation (or other service) for a guest for specified dates at a price, with terms such as a cancellation policy. It is the PMS's pre-arrival pipeline: reservations are created at the property or received from any channel — the property's own website, a central reservations office, a global distribution system, an online travel agency, a phone call — and can be modified or cancelled until the guest arrives. Reservations also carry their commercial context: the booker versus the staying guest, companions, the company or travel agency behind the booking, and the market segment it belongs to.
- **The operated stay with its folio.** At check-in the reservation becomes a stay: the guest is registered and a specific room is assigned from live inventory, respecting both availability and housekeeping readiness. During the stay the desk maintains it — room moves, extensions, companion changes — while charges accumulate on the folio: room charges post per night, and ancillary charges (restaurant, bar, spa, parking, phone) are posted manually or pushed automatically from the property's outlets. At check-out the folio is settled and closed; a closed folio is treated as settled and becomes a historical record. The desk's money view across all stays is the **guest ledger** — in-house guests and their balances, deposits held from future guests, and outstanding accounts.

### Money structures around the folio

Fuller PMS products extend the folio model with a small, stable set of accounts:

- **deposits and preauthorizations** — money taken before or at arrival to secure the future folio;
- **company / city-ledger-style accounts** — charges of multiple guests compiled onto one company or travel-agency account for periodic invoicing instead of payment at check-out;
- **house accounts** — accounts for local, non-staying customers;
- **cashiers** — payment-handling roles with accountability for money taken during a shift;
- **outlets** — the property's retail points (bar, restaurant, spa) whose consumed charges either post to a guest's folio for later settlement or are recorded as paid at the outlet.

### What mature products add (standard capabilities)

These are widespread in current products and expected by the market, but a product does not stop being a PMS for lacking any of them:

- the **front-desk loop as a module** — arrivals and departures queues, walk-ins, stayovers, room moves, alarms and notes;
- **rate management** — rate plans, seasons, restrictions, closeouts and overrides;
- **distribution components** — a booking engine to capture direct bookings and a channel manager (native module or integration) that passes availability, rates and inventory out to sales channels and receives their reservations back;
- **housekeeping operations** — servicing assignments, checklists, inspections, feeding room readiness to the desk;
- **group machinery** — blocks of inventory held for groups, rooming lists, master folios for group billing;
- **guest and company profiles** — persistent records enabling repeat-guest recognition, preferences, and corporate or agency relationships;
- **night audit / end-of-day close** — the accounting roll-over that posts room charges, balances folios and closes the business day;
- **reporting** — occupancy, revenue and rate performance; production by channel and segment;
- **registration and fiscal documents** — registration cards, receipts, invoices, statutory guest reporting per jurisdiction;
- **roles, permissions and audit trails**; **integrations** — door locks and key cutters, payment terminals, POS, ID scanners, phone systems.

## How It Works

### Sell: maintain the property's selling truth

Staff configure the inventory (units, categories), the rates that price them over time, and the restrictions that shape what can be sold. This configuration is the source from which every channel's availability is derived. Where a channel manager or booking engine is connected, the PMS passes availability, rates and inventory out and receives reservations in — the property keeps one selling truth rather than per-channel stock.

### Book: hold the reservation until arrival

A reservation enters the system from any source and lives there as the property's record of the commitment: who, what category, which dates, at what price and terms. Reservations staff (or the desk in small properties) modify, cancel, add deposits, attach company accounts, and organize groups into blocks with rooming lists. Close to arrival the reservation appears on the arrivals list — the desk's work queue.

### Check in: reservation becomes stay

```text
Today's arrivals list (or a walk-in)
→ retrieve the reservation
→ register the guest (identity, documents, preferences)
→ assign a specific room — free for the dates AND ready (housekeeping status)
→ the stay goes in-house; the room becomes occupied; keys/access issued
→ registration documents produced where the jurisdiction requires them
```

A confirmed reservation does not by itself put a guest in a room — assignment is constrained by live availability and readiness, which is why the desk works against a shared room picture rather than a static list.

### Operate: the stay and its folio

While the guest is in-house, the folio grows: room charges post automatically per night; outlet charges arrive from the restaurant, bar or spa; the desk posts manual charges, corrections and splits. The desk also executes stay changes — room moves, extensions and shortenings — which immediately reshape future availability. Housekeeping works from the same records, servicing departing and staying rooms and publishing readiness back so the next assignment can be made.

### Check out: settle and close

```text
Today's departures list
→ open the stay's folio; review and correct charges
→ settle the balance (payment, or charges moved to a company account)
→ check out: the stay closes, the folio closes as settled
→ the room is released and flagged for servicing
```

### Close the day

At the property's business-day boundary — traditionally the night audit — the system posts the day's room charges, balances folios and cashiers, rolls availability forward, and produces the day's reports. Above-property deployments add consolidated reporting across many properties.

### Core, standard, optional

- **Defining core:** inventory of record with rates and availability; reservations of record from any channel; the operated stay with its folio and the guest-ledger money view.
- **Standard capabilities:** front-desk module, rate/restriction depth, booking engine and channel manager, housekeeping operations, groups, deposits/preauths/split folios, company and house accounts, cashiers, night audit, reporting, fiscal documents, roles and integrations.
- **Common variants:** multi-property management, native revenue management, guest messaging and AI assistance, self-service check-in, marketing/CRM and website modules, on-premise or open-source deployment.

## Interfaces

Exact layouts and names vary by product; the following surfaces are described conceptually.

### Property dashboard

The staff's home screen.

- typical information: today's arrivals and departures, occupancy, in-house counts, current room-status picture, alerts
- primary actions: jump into a check-in or check-out, search guests and reservations, add a walk-in

### Reservation / stay detail with folio

The record staff live in for any transaction with one guest.

- typical information: guests and companions, dates, room, rate, source, notes and flags; the folio — charges by type and date, payments, deposits, balance
- primary actions: modify the stay, assign or move the room, post or correct a charge, split the folio, take payment, check in, check out, cancel

### Availability / room picture

The live state of the property's inventory, commonly as a calendar grid or "tape chart" of units against dates.

- typical information: each unit's occupancy state (occupied, arriving, departing, vacant) and readiness state; rate and restriction overlays by date
- primary actions: assign or move guests between specific units, read readiness before assigning, adjust rates and restrictions

### Rate calendar / rate management

The property's pricing surface.

- typical information: rates by category and date, restrictions, closeouts, yields by channel
- primary actions: update rates, set restrictions, open or close sales, review channel parity

### Housekeeping / room status

The servicing picture shared between desk and housekeeping.

- typical information: per-room service status and occupancy, zones or assignments, current work
- primary actions: assign and complete servicing, update readiness, report out-of-service rooms

### Groups and blocks

- typical information: block inventory and pickup, rooming lists, group master folio versus individual folios
- primary actions: create blocks, pick up rooms, check groups in or out, post to the master account

### Cashiering / guest ledger

The money view.

- typical information: in-house balances, deposits held, company and house accounts, cashier sessions
- primary actions: take or refund payments, transfer charges, close the day's cashiers

### Reports

- typical information: occupancy, ADR-class rate and revenue metrics, production by channel and segment, audit and tax reports
- primary actions: run, schedule, export

### Configuration

Units and categories, rates, taxes and charges, document templates, users and roles, integrations.

## Important Rules / Behaviors

- **A confirmed reservation is not an occupied room.** Check-in requires a specific unit that is both available for the dates and ready (housekeeping status). The readiness state is maintained on the servicing side and consumed by the desk.
- **The folio is the stay's account, open while the stay is open.** Charges post throughout the stay; at check-out the balance is settled and the folio closes as assumed-settled. After closure the record freezes into history (some products allow corrections for a configurable window).
- **Room assignment is a tracked move, not an overwrite.** Moving a guest updates the occupancy state of both units and preserves the stay's history.
- **Money taken before arrival secures the stay.** Deposits and preauthorizations are recorded against the reservation/folio and settle against the balance at departure.
- **Not everything the property sells belongs to a stay.** Non-resident and paid-at-outlet revenue is recorded separately from guest folios, keeping the guest ledger's in-house picture clean; company billing compiles selected guests' charges onto accounts invoiced later.
- **One selling truth feeds many channels.** Availability and rates configured in the PMS are what distribution passes outward; incoming reservations write back into the same record — the property avoids holding per-channel stock.
- **The business day is an accounting boundary.** The end-of-day close posts charges, balances money, and separates the business days; much of the system's money discipline hangs off this roll-over.
- **Staff power is permission-gated.** Rate overrides, refunds, folio corrections and configuration are restricted by role; cashier accountability tracks who took which money.
- **Exact labels vary.** State vocabularies (occupied/vacant/clean/inspected…), folio and audit names, and unit terminology differ by product; the structures above are conceptual, not a standard.

## Variants

- **Cloud suite-centered PMS** (the current dominant shape) — the PMS as the operational core of a vendor's wider platform: payments, distribution, guest messaging, marketing and revenue tools natively connected, or an open marketplace of integrations instead.
- **Best-of-breed PMS + integrations** — the property system focused on its core, with distribution, revenue, POS and guest-experience tools connected through interfaces and marketplaces.
- **Desk-first small-property products** — independents, inns, B&Bs, vacation rentals; the desk loop plus basic configuration is most of the product, with distribution added as modules. (The market's "front desk software" naming points at this shape; the front-desk application is documented as its own operational-slice Type.)
- **Enterprise / chain deployments** — heavy group and company handling, compliance-grade registration and fiscal reporting, above-property management of portfolios, and integration frameworks for POS, locks, loyalty and distribution at scale.
- **Open-source / self-hosted PMS** — the same spine installable without a vendor cloud; selling components (booking engine, channel manager) arrive as separate add-on modules.
- **Property-type tuning** — hostel bed-level inventory and per-person rates; vacation-rental units; campground sites; hourly/day-use rooms; function-space and activity booking alongside rooms.
- **Regional compliance shapes** — statutory registration, police/guest reporting, and fiscal document platforms realized as document and reporting layers on the same core.
- **Deployment heritage** — the market's on-premise front-office generation (several still maintained and migrated to cloud) demonstrates the same core without cloud delivery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Hotel Front Desk Application | contained operational slice | The desk loop (live room inventory + stay operated arrival-to-departure + folio) is the PMS's operational core; the PMS adds the pre-arrival reservation pipeline, rate/selling controls, housekeeping operations, the end-of-day close, reporting and above-property management. Desk-first small-property products sit between the two shapes. |
| Hotel Central Reservation System / CRS | adjacent, selling | A chain-level or central selling layer that holds inventory and reservations for selling across properties; it has no operated on-site stay. The PMS receives its reservations. |
| Hotel Booking Engine | adjacent, selling | The customer-facing capture surface for direct bookings; it sells availability the PMS holds and writes reservations back into it. |
| Hotel Channel Manager | adjacent, distribution | The hub that distributes the PMS's availability, rates and inventory to many channels and returns their reservations; a common pattern is PMS ⇄ channel manager ⇄ channels. Remove the PMS's on-site operation and you are left with this side. |
| Hotel Revenue Management System | upstream decision layer | Decides what rates and availability controls should be; the PMS holds and applies them. Current suites sometimes bundle a native pricing layer, and standalone revenue systems integrate with the PMS. |
| Hotel Housekeeping Management | adjacent, operations | Owns the room-servicing operations loop (assignments, checklists, inspections); the PMS consumes its readiness output and feeds it stay demand. Often shipped as a PMS module. |
| Hotel Guest Experience Platform / Digital Concierge | guest-facing counterpart | Guest-operated surfaces (online check-in, chat, portals) write into the stay the PMS operates; the PMS is staff-side. |
| Hotel CRM / Loyalty Platform | adjacent, relationship layer | Owns the standing cross-property guest relationship and the loyalty program of record; the PMS's guest profile is the stay-anchored operational slice used at the desk. |
| Hostel Management System | segment sibling | The same operator-side spine with bed-as-unit inventory and per-person rate semantics; one market largely serves hostels and hotels from the same products. |
| Campground / RV Park Management | segment sibling | Same skeleton with site-typed inventory (hookups, rig fit), up-front payment skew and long-stay machinery instead of daily room turnover. |
| Short-term Rental Management | overlapping sibling (unresolved seam) | Sampled PMS products serve vacation rentals directly; the dedicated STR leaf centers distributed unit portfolios with owner-side machinery. Boundary to be ruled by that leaf's pass. |
| Commercial Property Management | different tenure model | Multi-year lease tenancies with rent schedules and recoveries versus transient nightly guest stays settled by folio. |

The closest boundary is the one running through the PMS itself: the selling slices (CRS, booking engine, channel manager) end where the guest arrives; the operational slices (front desk, housekeeping) are contained inside it; and the relationship, revenue-decision and guest-experience layers surround it. The PMS is the property-side record they all hang from.

## Representative Products

- **Mews** — cloud PMS (mid-market and groups) with publicly documented API glossary and concepts; unusually transparent object model (spaces, reservations, bills/folios, paymasters, cashiers, channel-manager flow, multi-property).
- **WebRezPro** — long-established cloud PMS for independents and multi-segment operators; articulates the classic department structure (front desk / back office / accounting) on its product pages.
- **Yanolja Cloud Solution (eZee lineage)** — cloud platform spanning small independents to multi-property groups; names the PMS scope directly (reservations, check-ins, folios, housekeeping, night audit) inside a one-platform suite.
- **Cloudbeds** — "hospitality management system" for hostels through enterprise portfolios; PMS-centered unified-platform packaging with distribution and guest-experience modules.
- **HotelDruid** — free, open-source (AGPL) property management from B&Bs to large hotels; shows the minimal core with booking engine and channel manager as separate add-on modules.

The core model was also checked against the enterprise documentation family of a leading hospitality suite (Oracle OPERA Cloud, index level) and an APAC vendor's help-center structure (RMS Cloud) to avoid over-fitting to the current cloud-suite shape, and against the classic front-office vocabulary (folio, guest ledger, city ledger, cashier) that modern products' own glossaries still carry.

## Sources

Research date: **2026-09-08**

- Mews — Glossary for Open API users: https://docs.mews.com/getting-started/glossary.md
- WebRezPro — PMS product site: https://www.webrezpro.com/
- Yanolja Cloud Solution — platform site and FAQ: https://yanoljacloudsolution.com/
- Cloudbeds — platform site and FAQ: https://www.cloudbeds.com/ ; PMS product page: https://www.cloudbeds.com/product/pms/
- HotelDruid — product site: https://www.hoteldruid.com/en/
- Oracle Hospitality — OPERA Cloud Services 26.3 Get Started and Hospitality documentation indexes: https://docs.oracle.com/en/industries/hospitality/opera-cloud/26.3/
- RMS Cloud — Help Center: https://help.rmscloud.com/hc/en-us

> Sourcing limitation: deep operational documentation was not retrievable for the enterprise vendor (OPERA Cloud user-guide chapters are JavaScript-rendered; the PDF exceeds fetch limits) and for Cloudbeds' and RMS Cloud's help-center articles (transport error; JS-gated search). Findings rest on the accessible sources above — a Tier-1 API glossary plus product-page and FAQ evidence — and claims are kept at the level these sources support: precise operational limits, default settings and enterprise-only workflows are not asserted, and vendor performance statistics encountered in marketing pages were deliberately excluded.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary review against the processed sibling leaves are recorded in the paired Research Notes.
