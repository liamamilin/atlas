# Trucking Management System

## Overview

A **Trucking Management System** (market vocabulary: *trucking TMS*, *carrier TMS*, *trucking software*) is the business system of record for a motor carrier — the software a trucking company runs its freight business on. It holds the loads the carrier has committed to haul, dispatches them to the carrier's **own** trucks and drivers, tracks the work from the truck, bills the customers (shippers and brokers), settles the drivers' pay, and ties the trucks' operating costs — fuel, fuel taxes, maintenance — to the business.

The defining core is small:

```text
Load (the unit of business record)
  ├── hauled by the carrier's OWN capacity (trucks + drivers)
  └── carrying the carrier's OWN money (customer billing + driver settlement)
```

Everything else commonly associated with modern trucking software — EDI connectivity, ELD/telematics tracking, driver mobile apps, load-board integration, customer portals, AI automation — is widespread in current products but is not what makes the system a trucking management system. A paper-era trucking office with a dispatch board, a load ledger, driver pay statements, fuel logs, and an invoice book satisfies the same core.

The boundary that matters most: a trucking management system is the **seller side** of freight. The shipper-side Transportation Management System buys carriage from carriers; the freight brokerage resells third-party capacity; the trucking TMS sells carriage that its own equipment and drivers perform.

## Users & Context

The system is operated by the carrier's office staff and consumed in the field by its drivers.

Primary users:

- **Dispatcher** — the operational core. Builds and assigns loads to trucks and drivers, communicates with drivers, monitors progress, and handles the day's exceptions (delays, breakdowns, cancellations).
- **Bookkeeper / accounting staff** — works the money: turns delivered loads into customer invoices, tracks unpaid and overdue invoices, computes and issues driver settlements, reconciles fuel and toll transactions.
- **Owner / operations manager** — oversees the business: utilization, revenue per load and per truck, margins, driver performance, and growth decisions.

Field side:

- **Driver** — receives dispatch details, updates load status from the road, scans and uploads documents (bills of lading, receipts), and views pay sheets. Depending on the product, this happens in a mobile app or simply by text/email replies.

Typical context: for-hire trucking companies of every size — from a single-truck owner-operator to fleets with hundreds of power units — hauling truckload, LTL, specialized, or intermodal freight. The same machinery also serves **private fleets** (a shipper's own trucks hauling its own freight), where the money frame shifts toward internal cost-per-load.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a trucking management system:

**1. The load as the unit of business record.**
A load is one freight movement the carrier has committed to haul for a customer — with its customer, origin and destination (stops), equipment needs, pickup and delivery dates, and rate. It is a persistent, individually identified record that accumulates the whole operation: booking or tender acceptance, dispatch, status events from the road, delivery, documents, and finally billing. The load is the anchor to which everything else attaches — the truck and driver assigned to it, the documents generated on it, the money earned and paid on it.

**2. The carrier's own trucking capacity as the dispatchable supply.**
The carrier's trucks (tractors, trailers, other equipment) and its drivers are held as records — with schedules, availability, and compliance state — and loads are assigned against them. The system maintains who and what is available now; assignment consumes availability and completion restores it. This is the supply-identity boundary: the loads are hauled by the carrier's own capacity under its own operating identity, not procured from third-party carriers.

**3. The load's money on the carrier's own books.**
Each load carries both directions of the carrier's own money:

- **Revenue side** — the customer rate (per mile, flat, or percentage conventions vary by product and contract) that becomes an invoice, typically with accessorials and fuel surcharges itemized.
- **Pay side** — the driver settlement: the driver's or owner-operator's pay for the load, computed from dispatch data under the driver's pay arrangement, with deductions, bonuses, stop pay, and reimbursements itemized on a pay sheet.

Around the loads, the carrier's operating-cost machinery — fuel purchases, fuel-tax reporting, maintenance — is tied to the trucks that incur it. The carrier holds its own money in both directions; it does not hold a resale margin between a shipper's price and a third-party carrier's pay.

### Standard Capabilities of Mature Products

These are common across mature products and expected by the market, but they are layers on the core, not the definition:

- **Dispatch board / load planning surface** — the dispatcher's working screen: loads × trucks × drivers on a calendar, board, or list, showing what is unassigned, in progress, and complete.
- **Event-driven tracking from the truck** — location and status fed from ELD/telematics integrations or a driver app, replacing manual check calls; hours-of-service awareness so dispatch sees when a driver is near limits.
- **Document machinery** — rate confirmations in, bills of lading captured (commonly by mobile scanning), proof-of-delivery collected and reconciled for fast invoicing.
- **EDI connectivity with customers** — tenders received (often auto-creating loads from rate confirmations), status updates sent back, invoices exchanged — the standard connectivity with shippers and brokers.
- **Compliance machinery** — driver onboarding and credential records, hours-of-service monitoring, equipment compliance deadlines.
- **Cost machinery** — fuel-card transaction imports, fuel-tax reporting (IFTA-class), maintenance management (built in, or shipped as a sibling product).
- **Customer-facing surfaces** — tracking links, portals, automated status and ETA updates; live-tracking coverage is also how carriers keep their scorecards with brokers healthy.
- **Analytics** — revenue and margin per load, lane, driver, and truck; utilization; on-time performance.
- **Integration spine** — accounting systems (QuickBooks-class sync), factoring companies, load boards (posting and searching), fuel cards.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   Load intake
Realizations:  EDI tender auto-creating a load from the rate confirmation;
               PDF rate-confirmation import; manual entry; load-board booking

Concept:   Dispatch transmission to the driver
Realizations:  mobile app; text/email dispatch without any app; in-cab workflow tools

Concept:   Tracking feed
Realizations:  ELD/telematics integrations; native telematics;
               driver-app status updates

Concept:   Driver pay
Realizations:  native settlement engine; payroll-system integration; pay arrangements
               per driver (mile, load, percentage conventions vary)
```

## How It Works

The canonical loop runs from winning a load to closing its money. Exact step names vary by product; the sequence is the industry's own order-to-cash:

```text
Win or accept a load
  (rate confirmation from a broker/shipper, EDI tender, load-board booking,
   or a direct customer order)
→ the load is created with customer, stops, rate, and dates
→ Dispatch: assign the load to an available truck + driver
   (the dispatcher works the board; assignment transmitted to the driver
    by app, text, or email)
→ Haul: the truck moves; status flows back automatically
   (ELD/telematics location, driver-app updates, HOS-aware alerts)
→ Deliver: documents captured in the field
   (signed BOL/POD scanned or uploaded from the driver's phone)
→ Bill: the load's rate + accessorials become a customer invoice
   (often triggered by POD arrival; invoices tracked to payment,
    factoring exports where used)
→ Settle: the driver's pay for the load is computed and issued
   (settlement generated from dispatch data under the driver's pay
    arrangement; deductions, bonuses, reimbursements itemized)
→ Cost & report: fuel, toll, and maintenance costs accumulate against
   the trucks; fuel taxes reported; revenue/margin per load, driver,
   and truck reviewed
```

Two loops run continuously alongside this spine:

- **The dispatch loop** — throughout the day the dispatcher balances unassigned loads against available trucks and drivers, reassigns around breakdowns and delays, and keeps customer commitments informed.
- **The money loop** — invoices age toward payment; settlements cycle on the carrier's pay schedule; fuel and toll transactions import and flow into settlements and tax reporting.

## Interfaces

### Dispatch board / load calendar

The dispatcher's primary surface.

- Typical information: loads with customer, stops, dates, rate; assigned truck and driver; live status; unassigned loads awaiting capacity.
- Primary actions: create or import a load, assign truck + driver, transmit dispatch details, update status, attach notes and documents.

### Load detail

The record behind the board.

- Typical information: stops and times, rate and accessorials, assigned equipment and driver, status history, attached documents (rate confirmation, BOL, POD), notes visible to the team in real time.
- Primary actions: edit stops and rate, reassign, upload documents, trigger invoicing.

### Driver app / driver surface

The field side.

- Typical information: assigned loads and schedule, stop details, pay sheets.
- Primary actions: update status, scan and upload documents, communicate with dispatch, view pay.

### Invoicing and settlements screens

The bookkeeper's surfaces.

- Typical information: delivered loads awaiting invoice; unpaid and overdue invoices; settlement periods per driver; pay-sheet itemization (base pay, deductions, bonuses, reimbursements).
- Primary actions: generate and send invoices, record payments, generate settlements in bulk or individually, issue corrections and revisions.

### Customer-facing surfaces

Tracking links or portals where the carrier's customers see load status and documents; EDI status updates flow to customer systems without a human surface.

### Reports / dashboards

Revenue, margin per load/lane/driver/truck, utilization, on-time performance, fuel and cost summaries.

## Important Rules / Behaviors

- **The load is the anchor.** Notes, documents, status events, and money all attach to the load record; the load's history survives as the carrier's business record.
- **Driver actions drive load status.** In mature products the load's status advances automatically from the driver's field actions (accepted, en route, delivered), rather than by office data entry.
- **Settlements are computed from dispatch, not entered by hand.** The pay side is derived from the load record under each driver's pay arrangement; recurring bonuses and deductions are saved and applied, and revisions are tracked — because drivers check their pay sheets, settlement accuracy is a trust issue, not just an accounting one.
- **Document completeness gates invoicing.** Invoicing typically waits on the delivered load's paperwork (signed BOL/POD); missing documents delay cash, which is why field-side document capture is a first-class behavior.
- **Availability is consumed and restored.** Assigning a load takes a truck+driver out of available supply; completing it restores them. Hours-of-service state constrains what a driver can accept.
- **Accessorials must land on the invoice.** Extra charges (detention, lumper fees, extra stops) captured in the field flow onto the customer invoice — missed accessorials are lost revenue, so products automate their capture and itemization.
- **Exceptions are a designed concern.** Loads falling behind raise alerts; breakdowns and delays trigger reassignment and customer notification; the dispatcher's day is largely exception management.

## Variants

- **By scale** — from single-truck owner-operators (where the owner is dispatcher, driver, and bookkeeper at once) to enterprise carriers running multi-dispatcher operations; product families span the whole range.
- **By segment** — truckload, LTL (often terminal-centric operations with pickup-and-delivery loops), heavy haul and specialized, fuel delivery (with tank-inventory forecasting), intermodal (containers, chassis), cross-border.
- **Hybrid carriers (asset-based brokers)** — carriers that also broker loads they cannot cover, running fleet and brokerage sides in one platform with an explicit toggle between them. The defining posture remains own capacity; the brokerage machinery is imported per outsourced load.
- **Private fleets** — the same machinery applied to a shipper's own fleet: internal demand, cost-per-load focus, and empty-mile reduction instead of external billing.
- **Automation posture** — text-based dispatch that requires no driver app; driver-app-centric operations; AI-era layers (document extraction, automated order entry, tender evaluation) increasingly common but not definitional.
- **Regulatory regime** — the sampled market is North America-centric (FMCSA-style driver compliance, IFTA-style fuel taxes); other jurisdictions run equivalent regimes with different records and tax machinery. The core does not depend on any specific regulator.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Transportation Management System / TMS | same freight substrate, opposite seat | The TMS is the **buyer** side: a shipper/LSP procures carriage from carriers at rates and runs the tender-execute-track loop with carriers as supply. The trucking TMS is the **seller** side: it hauls with its own capacity and bills the customers. Vendors themselves ship separate carrier-TMS and shipper-TMS products. |
| Freight Brokerage Platform | same substrate, opposite supply identity | The brokerage resells **third-party** capacity, holding a two-sided price (customer charge vs carrier pay) with margin between. The carrier operates **its own** capacity and holds its own revenue and driver pay — no resale margin. Hybrid asset-based brokers run both in one product. |
| Load Board / Freight Marketplace | the market vs the operator | The board is where carriers find loads; the trucking TMS is where they run them. A carrier uses both; board integration is a standard capability, and the board holds no dispatch, fuel, maintenance, or settlement machinery. |
| Dispatch Management | the operational core vs the business system | Dispatch machinery (work queue × resources × assignment × live board) sits inside the trucking TMS as its operational core. Add the carrier's freight business frame — load money, settlement, compliance, customer EDI — and it becomes a trucking TMS; strip the frame and only dispatch remains. |
| Fleet Management System | vehicle estate vs load business | FMS centers on vehicles as assets (maintenance, fuel, telematics, compliance of the estate). The trucking TMS centers on the load business, with trucks as revenue-producing capacity; maintenance appears as a module or sibling product. |
| Driver Management | person records vs capacity and payees | Driver Management owns the person-centered credential and entitlement records. The trucking TMS consumes driver availability and compliance state and holds their pay arrangements. |
| Electronic Logging Device / HOS Platform | compliance record vs execution | The ELD produces the duty-status record of hours; the trucking TMS consumes it for dispatch awareness and tracking. ELDs integrate into the TMS as data suppliers. |
| Courier Management Platform | similar shape, different work | Both are own-workforce operators billing customers for completed work. The courier's work item is a parcel/delivery job with zone/route rating; the carrier's is a freight load with lane/equipment semantics, driver settlement, and fuel-tax machinery. |
| Freight Forwarding System | shared vocabulary, different center | Forwarder products are also marketed as "TMS", but the forwarder's center is international consignment, document, and charge machinery; the trucking TMS's center is domestic freight hauled by its own trucks. |
| Shipment Visibility Platform | watching vs executing | Visibility platforms watch freight other parties carry. The trucking TMS is the executing party; tracking flows from its own trucks into its own loads. |

## Representative Products

- **Truckbase** — dispatch-centric trucking TMS for small and mid-size asset-based carriers; text-first dispatch, instant invoicing, driver settlements.
- **Trimble TMW.Suite / Trimble TMS for Carriers** — enterprise order-to-cash platform for truckload carriers (also sold to brokers, 3PLs, and private fleets); dispatch, telematics, and billing unified.
- **Alvys** — all-in-one cloud TMS sold across carrier, broker, hybrid, enterprise, and private-fleet seats; native EDI, settlements, and IFTA reporting.

The defining core was checked against the paper-era trucking office and the single-truck owner-operator extreme to avoid over-fitting to the current SaaS market.

## Sources

Research date: **2026-09-10**

- Truckbase — homepage: https://truckbase.com/ ; Driver Settlement Software: https://truckbase.com/driver-settlement-software
- Trimble Transportation — Transportation Management: https://transportation.trimble.com/en/solutions/transportation-management ; TMW.Suite: https://transportation.trimble.com/en/solutions/transportation-management/tmw-suite-tms
- Alvys — homepage: https://www.alvys.com/ ; Carrier TMS: https://alvys.com/tms-for-carriers ; Help Center: https://help.alvys.com/en/
- Prior sibling research used as boundary context: research notes for Transportation Management System / TMS, Freight Brokerage Platform, Dispatch Management, Load Board / Freight Marketplace, Freight Forwarding System (all processed 2026-09-07/09).

> Sourcing limitation: several named carrier-TMS vendors were unreachable from the research environment on 2026-09-10 (McLeod, Rose Rocket, Tailwind, TruckLogics, Axon, ITS Dispatch, Dr Dispatch — blocked or timed out). Evidence therefore rests on three reachable products at product-page and help-center-index depth, plus the sibling passes' first-hand observations of overlapping products. Precise operational details (status vocabularies, settlement-cycle defaults, pay-period conventions, numeric limits) are intentionally not stated in this document; such details remain unverified rather than filled from memory.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
