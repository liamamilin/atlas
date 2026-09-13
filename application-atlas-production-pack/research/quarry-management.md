# Research Notes — Quarry Management

Research date: 2026-09-09
Leaf: Quarry Management (DIRECTORY.md §20 Agriculture, Food & Natural Resources)
Slug: quarry-management

## Research Goal

Understand what software marketed as quarry management actually does in the market: what its core objects are, who operates it, how the daily operational loop works, and where its boundary sits against generic bulk-materials weighbridge ticketing, mining operations software, and construction hauling platforms.

## Initial Boundary (hypothesis before research)

- Guess: Quarry Management = operations management for surface aggregate (crushed stone, sand & gravel) sites: production recording, stockpile inventory, sales/dispatch ticketing, site compliance.
- Neighbors to check: Mining Operations Management, Mine Planning Application, Mining Fleet Management, Inventory Management System, Grain Elevator Management, Dispatch Management (trucking).
- Unknowns: Is the weighbridge ticket the defining transaction? Is stockpile inventory definitional or just common? Do quarry products include reserves/planning (Mine Planning territory)? Role of royalties/compliance?

## Research Questions

1. What are the core objects (site, product, stockpile, ticket, order, load, hauler)?
2. What is the atomic transaction, and how does it flow to money (invoicing/AR) and material state (inventory)?
3. Which surfaces exist (scale house, dispatch board, loader, driver app, customer portal, back office)?
4. What rules matter (weighing sequence, ticket change history, tax/freight on invoices, permissions, disputes)?
5. What distinguishes quarry management from generic weighbridge ticketing platforms (cross-industry machinery) and from mining operations software?
6. What is common vs vendor-specific vs regional?

## Representative Products (final sample)

| Product | Vendor | Angle | Evidence |
|---|---|---|---|
| Apex + Command Cloud (Dispatch & Scale Ticketing, Material Supply) | Command Alkon | incumbent enterprise suite for aggregate producers: site automation, scale ticketing, dispatch, inventory, back office | A (multiple official product pages) |
| Trux (Ticketing, Materials, Drive) | Trux, Inc. | cloud dispatch/hauling + e-ticketing "purpose-built for quarries, pits, and HMA plants"; dump-truck logistics | A (official product pages) |
| Stockpile Reports | Stockpile Reports | specialized stockpile-measurement pole: phone/drone/camera imagery → verified tonnage per pile, by product & site | A (official product page) |

Rejected / unreachable (recorded, not used as evidence):
- Truckbase (truckbase.com) — generic trucking TMS for carriers; Product Mismatch, dropped.
- Wingfield (wingfield.io) — AI cameras for tennis/padel; researcher name confusion, dropped.
- PlantDemand (plantdemand.com) — quarry plant maintenance scheduling; site returned 503 twice, abandoned per network rule.
- Agg-Net directory, Capterra category — 403 blocked.
- help.truxnow.com — timed out (Tier-1 depth not reached for Trux).
- Metso digital-services page — 404.

## Sources

Fetched 2026-09-09:

- https://www.commandalkon.com/ — vendor home; Command Cloud positioning ("unifying dispatch, inventory, and reporting"); aggregate product family listing.
- https://www.commandalkon.com/aggregate/ — aggregate industry page; solution map (Apex, Material Supply "centralized view of on-site stockpiles and inventory", Sales & Quoting, Dispatch & Scale Ticketing, Customer Portal, TrackIt/Digital Fleet, Billing & Invoicing, AR, Payments).
- https://www.commandalkon.com/products/apex/ — "Automate Your Quarry or Plant Operations"; advanced scale ticketing; site automation (automatic truck recognition, driver kiosks and display, remote print enclosures, video verification of scale loading, antitheft modules, wireless loader systems); "connect sales, dispatch, and back office"; case-study quote (Great Lakes Aggregate) on throughput.
- https://www.commandalkon.com/products/dispatch-and-scale-ticketing/ — cloud dispatch & scale ticketing for bulk materials; quote→dispatch→delivery→invoice flow; weighmasters; FAQ: instant ticket data, per-user field visibility (freight rates, tax codes), weighing latency, Command Edge on-site gateway + internet outage guidance, printing, card payments, multi-product/freight/surcharge/environmental-fee invoices + automated tax, ERP integration, kiosks ("check-in, tare-in, weigh-out, ticket printing"), Scale Watcher camera verification, Load Manager (cloud replacement of Wireless Loader screen; loader operators see vehicles in-plant), Auto ID/RFID/OPC; explicit cross-industry statement ("works for any operation that weighs material in and out on a scale — including mining, waste and recycling, agriculture, and bulk liquids").
- https://www.commandalkon.com/products/material-supply/ — heavy building materials inventory; FAQ: inventory across "multiple pits, yards, terminals, and plants" in near real time rolled up to dashboards; "real-time inventory updates driven by connected ticket/receipt activity"; ticket as "the single source of truth that downstream processes reference"; OCR ticket capture with human verification; reorder/replenishment loop; invoice reconciliation; write-off reduction.
- https://www.truxnow.com/ — dump truck logistics; product set (Materials, Construction, Ticketing, Drive); "integrated with your sales order and scale/ticketing systems"; load planning ("how many loads, trucks, or tons will be required to fill an order"); GPS/cycle-time tracking; digital load slips; e-ticketing with integrated scale systems.
- https://www.truxnow.com/products-trux-ticketing — "Cloud-Based Ticketing Platform for Aggregates & HMA"; "purpose-built for quarries, pits, and HMA plants"; digital tickets at the scale with BOL data (carrier, vehicle, driver, scale weight, tax); scale system & ERP integration; timestamped tickets as single source of truth; traceable ticket edit history; end-of-day exports; hauler marketplace.
- https://www.stockpilereports.com/ — phone/drone/installed-camera imagery → verified volume/tonnage per pile with confidence score; piles managed by product & site; tonnage reports; use cases named: "Reducing inventory write-offs at year-end or month-end", "Delivery disputes (in or out)", "Production monitoring"; organizations with 200+ stockpiles across sites; integrations.

## Product A — Command Alkon (Apex; Command Cloud: Dispatch & Scale Ticketing, Material Supply)

Key observations (evidence layer A unless noted):

- Positions Apex as "Quarry and Plant Automation Software": scale ticketing + site automation + point-of-sale to back office connectivity.
- Site automation machinery (Apex): automatic truck recognition, driver kiosks and displays, remote print enclosures, video verification of scale loading, antitheft modules, wireless loader systems.
- Command Cloud Dispatch & Scale Ticketing: orders, tickets, pricing consistent from "quote to dispatch, delivery, and invoice"; dispatchers and weighmasters work from one real-time view; dynamic scheduling, live ETAs, constraint-aware dispatch; modern Edge device connects plant hardware (scales, printers) to cloud.
- FAQ confirms operational shape: ticket data instantly available system-wide on creation (no legacy "ticket out" replication step); scale weighing near real-time; kiosk steps named "check-in, tare-in, weigh-out, ticket printing"; manual ticketing supported; card payments in platform; invoices combine product types, freight charges, surcharges, environmental fees; automated location-based tax; field-level permissions (hide freight rates / tax codes); ERP/accounting integrations via APIs; Billing Prep, Invoicing, Accounts Receivable in-suite.
- Load Manager: browser screen for loader operators showing vehicles in-plant for load management (successor to Wireless Loader).
- Material Supply: inventory across multiple pits/yards/terminals/plants in near real time, rolled up to management dashboards; "real-time inventory updates driven by connected ticket/receipt activity"; ticket = "single source of truth"; OCR capture of inbound supplier tickets with human verification; automated replenishment ("signal → order → receipt" loop); invoice reconciliation ("only pay for materials you have received"); write-off reduction.
- Aggregate industry page: Material Supply described as "centralized view of on-site stockpiles and inventory"; fleet products (TrackIt, Digital Fleet) and AR/Payments as part of the aggregate solution map.
- Boundary evidence (B-layer inference from A): vendor states the dispatch/scale-ticketing machinery itself is cross-industry (mining, waste/recycling, agriculture, bulk liquids) — i.e., weighbridge ticketing per se is NOT quarry-defining; the quarry shape comes from the producing site, aggregate product set, and stockpile/production context around it.

## Product B — Trux (Ticketing, Materials, Drive)

Key observations (evidence layer A):

- Ticketing product: "Cloud-Based Ticketing Platform for Aggregates & HMA… purpose-built for quarries, pits, and HMA plants… whether you're replacing paper, upgrading a legacy system, or starting fresh."
- Digital tickets generated at the scale with Bills of Lading data: carrier, vehicle, driver, scale weight, tax data; traceable change history on edited tickets; timestamped tickets as "single source of truth" for delivery verification and dispute reduction; structured end-of-day exports to billing; scale-system and ERP integration; customer sharing of digital tickets.
- Dispatch (Materials/Construction): digital dump-truck dispatching; load planning computes loads/trucks/tons required to fill an order; integrates with sales order and scale/ticketing systems; hauler communication; GPS and cycle-time tracking of every truck and load plant→jobsite; driver app (punch-in/complete loads/punch-out); third-party hauler marketplace; hauler payments.
- Named customer segment: "Material Producers" (aggregates & asphalt).

## Product C — Stockpile Reports (capability pole)

Key observations (evidence layer A):

- Turns phone/drone/installed-camera imagery into verified volume/tonnage per pile with confidence score; 3D model + contour image; report includes site and product.
- Piles managed by product & site; tonnage reports; organization-scale programs (200+ piles across states/countries) with role-based access and integrations.
- Named problem space matches quarry inventory practice: year-end/month-end inventory write-offs, delivery disputes, production monitoring.
- Interpretation: specialized measurement capability that feeds or replaces manual stockpile counts; not itself a quarry management system (no orders/dispatch/billing). Boundary-useful pole.

## Cross-product Comparison

| Structure | Command Alkon | Trux | Stockpile Reports |
|---|---|---|---|
| Producing site as operating unit | yes — pits/plants/yards/terminals, multi-site | yes — quarries, pits, HMA plants (site-side) | yes — sites hold piles |
| Saleable products with pricing | yes — products, pricing, quotes→orders | yes — orders, products, pricing central | piles labeled by product |
| Ticketed load as atomic record | yes — scale ticket, instant system-wide, permissioned fields | yes — digital ticket w/ BOL data, timestamped, editable w/ history | no (measures, doesn't transact) |
| Weighbridge/scale integration | yes — Edge gateway, kiosks, auto-ID, cameras | yes — integrated scale systems | no |
| Load-out / loader operation | yes — Load Manager for loader operators | implied via load completion at plant | no |
| Stockpile inventory | yes — Material Supply; ticket-driven updates | partial in fetched pages (ticketing-focused; Materials covers producer side) | yes — measured piles by product & site |
| Dispatch of trucks/haulers | yes — dispatch, ETAs, fleet modules | yes — core pole incl. marketplace | no |
| Billing path | yes — billing prep, invoicing, AR, payments, tax | yes — exports, ERP sync, hauler pay | no |
| Reconciliation/write-off control | yes — invoice reconciliation, write-off language | dispute reduction via timestamped tickets | yes — measurement vs book inventory |
| Driver/customer surfaces | kiosks, driver displays, customer portal | driver app, customer ticket sharing | consumer-ish measurement plans |
| Multi-site roll-up | yes — dashboards across locations | per-order/job views | yes — org-scale pile programs |

Reading: the *ticketed load + order/product spine* is common to both management-suite products; *stockpile/material state* appears as ticket-driven inventory in the suite and as measured piles in the measurement pole; *dispatch/hauling* is a strong secondary pole (Trux core); *back office* (invoicing/AR) present in the suite, integrated-by-export in the dispatch product.

## Abstraction (research-internal)

### L0 — Defining Invariant (minimal, jointly held)

1. **The producing site as the unit of record** — a persistent, identified quarry/pit operation (with its processing plant) carrying a defined set of saleable aggregate products; multi-site producers hold many of these in one system. Remove → generic inventory/dispatch tools with no site identity.
2. **The ticketed load as the atomic transaction** — each load of a specific product weighed on the site's scale and recorded as a ticket bound to product, weight, vehicle/driver, and customer/order; the ticket is the source of truth flowing to billing and inventory movement. Remove → no transactional spine; sales, inventory, and money cannot reconcile.
3. **The site's material ledger** — the stockpile state of each product at each site, increased by production and decreased by ticketed sales loads, reconciled against physical measurement. Remove → pure weighbridge-ticketing platform (cross-industry machinery per CA's own FAQ) or a hauling/dispatch app.

Jointly-held analysis: 1 alone = site registry; 2 alone = generic bulk-materials ticketing platform (explicitly cross-industry); 3 alone = inventory/measurement tool; 1+2 without 3 = weighbridge ticketing at a quarry (machinery, not management); 1+3 without 2 = inventory system with no transaction spine; 2+3 without 1 = ticketing + inventory unbound to a producing operation.

Historical check (§24-style): a paper-era quarry — pit + price list of products + weighbridge ticket books + hand-tallied stockpiles + sales ledger — satisfies all three structures with no software machinery (no kiosks, cloud, RFID, drones, apps). Older/regional practices (manual tally, third-party haulers on paper load slips) fit. The core therefore does not encode current automation fashion.

### L1 — Common Mature Structure

- order/quote management with products and pricing flowing to dispatch
- dispatch board (orders/loads/trucks, ETAs, constraint-aware scheduling)
- scale automation: driver kiosks (check-in, tare-in, weigh-out, ticket printing), automatic vehicle ID, camera verification
- load-out support for loader operators (vehicles in-plant)
- e-ticketing shared with customers/haulers; timestamped, traceably editable tickets
- billing prep → invoicing (product lines + freight + surcharges + fees + tax) → AR → payments
- ERP/accounting integration; structured end-of-day exports
- fleet/driver tracking and driver mobile apps
- multi-site inventory roll-up and management dashboards
- inventory reconciliation and dispute reduction as explicit goals

### L2 — Variant / Optional

- commodity mix: aggregate-only sites vs integrated producers (aggregate + asphalt/HMA; + ready-mix on the same platform family)
- scale of operation: single pit vs multi-site networks with central management
- attended vs unattended scale operations; degree of automation (RFID auto-ID, kiosks, cameras)
- owned fleet vs third-party haulers incl. marketplace dispatch
- regional weighbridge/legal-for-trade regimes and tax handling on tickets
- adjacent reusers of the same machinery: landfills/recycle yards, agriculture, bulk liquids (per vendor's own cross-industry statement)
- stockpile measurement modality: manual tally, phone/drone measurement, installed cameras (cross-checked against measurement-pole product)

### L3 — Vendor-specific (research notes only)

- Command Edge on-site gateway; Load Manager; Scale Watcher; wireless loader systems; PitTicketPro (Ticket Accounting); TrackIt / Digital Fleet; COMMANDbatch family (ready-mix batching — different Type); 99.8% OCR accuracy claim; Fractal payments partner; OPC interfaces; Great Lakes Aggregate throughput quote.
- Trux Drive punch-in/out; hauler marketplace; weekly hauler payments ("$1.3B" claim); fuel surcharge adjustments on hauler pay.
- Stockpile Reports confidence scores, MCP/AI-assistant integration, plan tiers.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Rejected Findings

- "Quarry management = trucking dispatch" (from Truckbase first impression): rejected — Truckbase is a generic carrier TMS, no quarry semantics; Product Mismatch recorded.
- "Quarry management includes plant maintenance scheduling" (PlantDemand hypothesis): unverified — site unreachable; not asserted anywhere in fetched evidence; left as uncertainty.
- "Quarry management includes reserves/pit design": no evidence in fetched sample; reserves/planning treated as Mine Planning territory; not asserted.
- "Royalty tracking is a standard quarry-software capability": NOT verified in any fetched source; recorded as uncertainty only.
- Stockpile Reports as a representative of the Type: rejected as representative; kept as boundary/capability pole.

## Boundary Findings

- **vs generic bulk-materials weighbridge ticketing**: the strongest boundary datum of this pass is the vendor's own statement that the ticketing/dispatch machinery "works for any operation that weighs material in and out on a scale — including mining, waste and recycling, agriculture, and bulk liquids." Therefore weighbridge ticketing alone is NOT the quarry Type; what makes it quarry management is the producing site + aggregate product set + material ledger around the tickets. Remove the producing-site/material context → the product family becomes cross-industry bulk ticketing, not quarry management.
- **vs Mining Operations Management** (sibling leaf): quarry management as evidenced is a *product-sales* loop (produce → stockpile → sell → ticket → invoice) over aggregate commodities; mining operations software centers on extraction/production reporting (faces, fleets, grades, processing toward downstream value). The seam from this side: if the site's revenue object is direct product sales off the weighbridge, it is quarry management; if it is mineral extraction feeding a processing/metals chain, it is mining operations. (This side's sample does not include mining-ops products; seam stated at center-of-gravity strength only.)
- **vs Mine Planning Application**: reserves/geology/pit design vs site operations & sales; no planning objects appeared in the quarry sample.
- **vs Mining Fleet Management**: equipment assignment/payload/grade telemetry vs the site's production-inventory-sales loop; fleet tracking appears in quarry products as a module (TrackIt/Digital Fleet; Trux GPS), reinforcing that fleet is a capability, not the Type.
- **vs Inventory Management System**: the material ledger is bound to weighbridge tickets and producing sites (tons of defined aggregate products), not generic SKU stock.
- **vs Dispatch Management (Trucking) / hauling platforms**: hauling dispatch coordinates trucks between locations; quarry management's dispatch leg is embedded in the site's own sales/production loop (order → loads → tickets → billing). Hauling data is consumed; the Type's center is the site and its product sales.
- **vs Grain Elevator Management**: same weigh-in/weigh-out ticket machinery family, but grain elevators handle third-party growers' grain (receipts, grades, storage, withdrawal) rather than producing and selling their own extracted product.
- **vs Natural Resource Rights Management**: land/rights/permits administration is a separate directory leaf; no rights objects in this sample.
- **"Remove what → becomes another Type" judgments**: remove ticketed loads → site inventory + production = generic inventory/production tooling; remove producing site + material ledger → cross-industry weighbridge ticketing; remove sales/commercial spine (orders/customers/billing) → mine/fleet production reporting territory; remove site identity → hauling dispatch platform.

## Uncertainties

- Production recording depth (per-plant/per-shift crusher output as a first-class record) was NOT directly evidenced in fetched pages; the sample shows inventory driven by ticket activity and production monitoring as a measurement use case. Calibrated wording used in the final document ("commonly… where tracked").
- Royalty tracking (per-ton payments to land/lease holders) — expected in industry practice but unverified in fetched sources; excluded from the final document.
- Regulatory/compliance machinery (e.g., MSHA training records, blasting records, environmental permits) — unverified; excluded from the final document.
- Help-center depth (Tier 1) unreachable for both primary products (Trux help timed out; Command Alkon help not attempted after repeated heavy pages); all claims rest on official product/FAQ pages (Tier 2) — assertion strength kept calibrated; no precise numeric limits asserted.
- Market breadth beyond the North American sample (European quarry software vendors) not reached; regional variant claims kept generic.

## Final Synthesis

A Quarry Management application is the site-and-sales system of record for an aggregate-producing operation. Its defining structure is three jointly-held things: the producing site (pit + plant + its saleable products) as the persistent unit of record; the ticketed load — every weighed load of a specific product bound to customer/order and vehicle — as the atomic transaction that drives both money (invoicing/AR) and material state (stockpile movement); and the site's material ledger (stockpiles per product, fed by production, drained by ticketed sales, reconciled by measurement). Around this core, mature products add the dispatch/hauling leg, scale automation, customer/driver surfaces, and the back-office billing path. The machinery is shared with other weighbridge industries; the quarry identity lives in the producing-site context and the product-sale loop.
