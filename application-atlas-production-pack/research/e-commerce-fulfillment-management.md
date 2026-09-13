# Research Notes — E-commerce Fulfillment Management

## Research Goal

Understand what "E-commerce Fulfillment Management" (DIRECTORY §05.08 Fulfillment) really is by studying real products: what objects exist inside it, what workflow orders follow, who operates it, and where its boundary sits — with one pre-hung decision to discharge.

Pre-hung flags this pass must discharge:

1. **order-fulfillment-platform (§05.08 sibling, processed 2026-09-08)** — FORWARD FLAG: "market usage overlaps this Type heavily (ShipMonk 'Ecommerce Fulfillment' solution line, Red Stag 'D2C fulfillment' service) — that pass should apply the goods-identity + execution-loop + channel-loop test and decide keep-both vs alias, joint review recommended."
2. **distributed-order-management (§05.07)** — physical execution vs network sourcing seam (inherited).
3. **dropshipping-platform (§05.20)** — goods-identity test (inherited).
4. **warehouse-management-system-wms (§10)** — order-subject vs warehouse-subject seam (inherited; ShipHero self-labels "WMS").
5. **delivery-experience-platform (§05.08 sibling)** — phase seam: operation-to-carrier-handoff vs consumer-facing post-purchase surface (inherited).

## Initial Boundary

Working hypothesis before research:

- Core use: managing the fulfillment operation of an e-commerce seller — order intake from selling channels, stock at fulfillment locations, pick/pack execution, carrier dispatch, and completion reporting — across the self-fulfillment software pole and the fulfillment-service (3PL) pole.
- Users: e-commerce fulfillment/operations staff; in the service pole, the provider's warehouse staff execute and the merchant manages through a client-facing platform; in the software pole sold to fulfillment houses, a 3PL operator runs fulfillment for many client brands.
- Nearest neighbors: Order Fulfillment Platform (likely the same family — the forward flag), OMS/DOM §05.07, WMS §10, Dropshipping §05.20, Delivery Experience §05.08, Returns §05.09, Inventory Management §10, Multi-marketplace Seller Platform §05.23.
- Unknowns: does this leaf name a Type distinct from order-fulfillment-platform (e.g., a management/orchestration layer, or a 3PL-business-management system), or the same product family under a second market name? Is marketplace-operated fulfillment (FBA-class) in or out?

## Research Questions

1. What enters the system, and in what form does an order exist while being fulfilled?
2. Whose inventory is fulfilled and where is it stored? (goods-identity test)
3. What is the execution loop between "order received" and "shipment dispatched", and what state model governs it?
4. What flows back to the selling channel at completion? (channel-loop test)
5. Who executes the physical work in each product — the merchant's staff or a provider's?
6. What does the "management" in the leaf's name actually cover — is there a management layer with structures the sibling Type lacks?
7. In fulfillment-house/3PL variants, what extra structure exists (client accounts, per-activity billing, client portals) — and is it load-bearing for the Type?
8. Where do the seams sit vs OMS/DOM, WMS, dropshipping, delivery-experience, returns?
9. Would older / regional / paper-era fulfillment operations still fit the definition?

## Representative Products

| Product | Pole | Customer tier | Docs reached |
|---|---|---|---|
| Logiwa | warehouse-execution-grade fulfillment software ("AI-native WMS that optimizes warehouse fulfillment") for brands, 3PLs, fulfillment networks | high-volume brands, enterprise 3PLs | Tier-2 product site (multiple pages) |
| Mintsoft | cloud WMS / fulfilment management software for 3PLs (fulfilment houses) and e-commerce brands; UK pole | SMB → mid-market | Tier-1 help centre (collections + status article) + Tier-2 product site |
| J&J Global Fulfilment (ControlPort™) | fulfillment-service operator (12 global fulfilment centres) with a proprietary merchant-facing platform | mid-market → enterprise brands | Tier-2 product pages; client help desk login-gated |
| Flowspace | fulfillment-service operator (warehouse network) + platform (order/inventory/warehouse management, network optimization) | growing D2C brands | Tier-2 product site + platform pages |
| (reused from sibling pass) ShipStation, ShipHero, ShipMonk, Red Stag | self-fulfillment software ×2, fulfillment-service platforms ×2 | SMB → enterprise | Tier-1 help centres (ShipStation, ShipHero); Tier-2 (ShipMonk, Red Stag) — fetched 2026-09-08 by the order-fulfillment-platform pass |

Rejected/considered: ShipBob (major service-operator pole — www 403 on 2026-09-08 pass, www 403 again this pass = 403 ×3; abandoned per network rules; no claims made); Amazon FBA (seller-central help login-gated; referenced only via sibling pass's evidence as a fulfillment-provider destination); Peoplevox / Linnworks / Extensiv (adjacent WMS / multi-marketplace-seller territory; not needed once stop conditions met).

## Sources

- Logiwa — https://www.logiwa.com/ (home; Solutions: Digital Warehouse, Smart Shipping, Connected Ecommerce; Industries: 3PLs, Online Sellers, Fulfillment Networks, Brands) — fetched 2026-09-10
- Mintsoft — https://www.mintsoft.co.uk/ (home; sectors 3PLs & Fulfilment Houses / Retail & multichannel; 3PL Client Portal; warehouse, order, shipping management) — fetched 2026-09-10
- Mintsoft Help Centre (Tier-1) — https://help-mintsoft.theaccessgroup.com/en/ (collections: Order Management ×75, Warehouse Management ×73, Shipping Management ×65, 3PL Accounting ×24, User/Admin Management "Warehouse/Client User Management" ×43); "Order status definitions and meanings" (23-status table); "Order Management" collection index; "3PL Accounting" collection index — fetched 2026-09-10
- J&J Global Fulfilment — https://www.ecommercefulfilment.com/ (home; /technology/controlport/ — ControlPort™ OMS pages: Order Management, Product Management, Live Order Tracking, Insights & Reporting) — fetched 2026-09-10
- Flowspace — https://flow.space/ (home; Platform: Order Management, Inventory Management, Warehouse Management, Network Optimization, FlowspaceAI, Reporting; fulfillment services pages) — fetched 2026-09-10
- ShipBob — https://www.shipbob.com/ — 403 (2026-09-10, this pass; previously 403 ×2 on 2026-09-08) — abandoned, source-access limitation
- J&J client help desk — https://jamesandjames.zendesk.com/hc/en-gb — login-gated (sign-in wall), not sampled
- Reused (fetched 2026-09-08 by order-fulfillment-platform pass): ShipStation https://help.shipstation.com/ ; ShipHero https://software-help.shiphero.com/hc/en-us ; ShipMonk https://www.shipmonk.com/ ; Red Stag https://redstagfulfillment.com/

## Product Observations

### Product A — Logiwa (evidence layer A, Tier-2 depth)

Self-labeling: "An AI-native WMS that optimizes warehouse fulfillment"; "fully integrated WMS and cloud order fulfillment software solution for B2C and DTC businesses"; "Logiwa IO (FMS/WMS)".

- **Connected ecommerce** — "Ecommerce fulfillment software pre-integrated with all your sales channels and order-management platforms" (solution page nav).
- **Smart shipping** — "Automated ecommerce shipping software pre-integrated with your carriers".
- **Digital warehouse** — "Modern digital warehouse management system powers a modern fulfillment experience"; warehouse automation/controls; analytics & reporting.
- **Audiences**: 3PLs ("Cloud 3PL software for high-volume fulfillment"), Online Sellers ("Ecommerce inventory management software"), Fulfillment Networks ("Cloud fulfillment network software"), Brands ("Warehouse execution system for omni-channel fulfillment"), Wholesalers ("hybrid wholesale distribution software for 3PL transitions"), Retail, B2B shippers ("B2B and B2C fulfillment").
- Customer references include 3PL/fulfillment operators (Radial "Fast Track powered by Logiwa", eShipper, Badger Fulfillment Group, Flexport "WMS fulfillment orchestration").
- Blog content covers multichannel inventory sync (stock across channels), inventory accuracy, per-order cost framing.

Reading: warehouse-execution-grade fulfillment management — the order loop (channels → orders → pick/pack → carrier shipping) wrapped in deeper warehouse machinery; sold to brands AND to 3PL/fulfillment-network operators.

### Product B — Mintsoft (evidence layer A, Tier-1 help centre)

Self-labeling: "Cloud-based WMS built for 3PLs and ecommerce brands"; "Automate your fulfilment with unrivalled control of your orders, inventory, warehouse operations and delivery partners"; sectors "3PLs & Fulfilment Houses" and "Retail, ecommerce & multichannel sellers".

- **Order intake**: integrations with marketplaces/carts ("Order retrieval and inventory sync"); "Create order channels"; manual orders; **"Set up mail orders"** (postal-order intake as a first-class channel type); bulk upload; failed-order fixing; duplicate order numbers.
- **State model (Tier-1, "Order status definitions and meanings")**: 23 statuses. Key facts observed directly:
  - NEW = "order has been created and all stock has been allocated… ready for picking and despatch" → allocation happens at order creation, not at ship time.
  - CANCELLED = "all stock allocations have been released" → allocation is real stock commitment.
  - DESPATCHED = "A despatch date and tracking number are recorded, and **integrated sales channels are updated automatically**" → channel sync-back is the loop-closing act.
  - Holding Order Policy governs insufficient stock: Manual (HOLDING until reprocessed), **Place on back order** (ONBACKORDER, auto-reprocess), or **Split order** (despatch available stock, back-order the rest).
  - Holds taxonomy: AWAITINGCONFIRMATION (order rules or manual; "Client users cannot edit orders while they are in this status"), AWAITINGDOCUMENTATION (e.g. commercial invoice), AWAITINGADDITIONALITEM (e.g. drop-ship order combined with warehouse order), AWAITINGPAYMENT, QUERYRAISED (previous status stored and restored on resolution), PACKANDHOLD (picked and packed but held until a release date — pre-orders), FRAUDRISK (flagged typically from an external integration; accepted or cancelled).
  - Execution state machine: NEW/PRINTED → AWAITINGPICKING → PICKINGSTARTED → PICKED → PACKED → DESPATCHED; PICKINGSKIPPED when items are skipped in picking (item not found at location); AWAITINGREPLEN when allocated from replenishment locations.
  - Per-activity billing inside the lifecycle: INVOICED = "After despatch, the system calculates the cost to pick, pack and despatch the order" (irreversible); INVOICEDFAILED = courier price could not be determined — "still treated as despatched for integration purposes" (external name stays DESPATCHED; internal/external status naming is a documented, configurable distinction).
- **Picking & packing**: batch configuration, barcode verification, rework, packing; picking methods per site: single-order picking, multi-tote batch picking, bulk batch picking, Rebin (zone) picking, open-pool/user-assigned; mobile app with barcode scanning, voice-assisted picking, stock moves, audit trails.
- **Warehouse management**: multiple locations, location management, pallet & carton IDs, stock counts, ASNs and POs, replenishment (KB collections).
- **Shipping management**: courier/multi-carrier integrations, label generation, tracking, shipping rules (65-article KB collection).
- **3PL client management**: "3PL client management at the core of our WMS" — client data, chargeable rates, inventory held, billing information; "raise your client invoices in Mintsoft based on costs such as storage, handling and shipping"; **3PL Client Portal** ("Give your customers their own login… connect their sales channels, import orders, create scheduled reports"); white labelling; User/Admin Management collection covers "Warehouse/ Client User Management" — two user populations (warehouse staff + client users).
- **3PL Accounting (Tier-1 collection, 24 articles)**: invoicing orders; picking costs (picking calculation types, channel tier pricing, order-volume tier pricing, warehouse pick pricing override); packaging/carton/pallet picking costs; storage charging (per unit, per pallet, volumetric, location-type, "highest point"); goods-in charging; recurring and additional invoice items; troubleshooting including "Cannot Invoice Order(s)".
- Returns & refunds processing inside Order Management.

### Product C — J&J Global Fulfilment / ControlPort™ (evidence layer A for product-page claims, Tier-2)

Self-labeling: "Global fulfilment, powered by our proprietary tech platform that gives eCommerce brands total visibility"; ControlPort™ = "our award winning order management system" / "Get total visibility and control with ControlPort™, our award winning fulfilment software". 12 global fulfilment centres (UK/EU/US/CA/AU), 400+ clients.

- **Service posture**: eCommerce fulfilment service ("expert handling, fast dispatch, and total visibility across all channels"), marketplace fulfilment, retail/B2B, returns; merchants' goods stored at J&J's fulfilment centres.
- **ControlPort™ (merchant-facing platform)**:
  - Order Management: "All your orders from every channel are organised in one platform"; "consolidates orders from your website, marketplaces, and retail partners into one platform… every order follows the same structured workflow"; "live updates from picking and packing through to despatch and carrier handover. You can see exactly where an order is, how long it has been in each stage, and any exceptions that require attention."
  - Product Management: SKUs, variants, bundles, attributes; goods-in with ASN tracking, discrepancy alerts.
  - Live Order Tracking: "real-time visibility from picking to delivery"; "Live carrier tracking with accurate timestamps; Early alerts for stalled or delayed shipments; Failed delivery notifications; Visibility of carrier performance trends"; reduces WISMO enquiries.
  - Insights & Reporting: "SLA tracking and fulfilment accuracy"; "Cost breakdowns and live price book access"; storage and pick fees transparency; stock ageing, BBE (best-before) expiry alerts, re-order automation, AI stock placement by popularity.
  - Returns management; custom API; client testimonial: cost transparency "picking, packing, storage and materials… broken down".
- Client quote framing the management relationship: "With J&J, I don't need to babysit or micromanage."

### Product D — Flowspace (evidence layer A for product-page claims, Tier-2)

Self-labeling: "Fulfillment Platform | Warehousing & Logistics for Ecommerce"; "Manage all fulfillment operations in one place"; services across "coast-to-coast warehousing".

- **Fulfillment services**: DTC ecommerce ("Fulfill any order from any sales channel"), B2B retail (pallets, BOL), managed freight; warehouse locations for inventory positioning.
- **Platform** (merchant-facing): Order Management ("Track and fulfill orders across all sales channels"), Inventory Management ("Monitor and control stock levels across locations"), Warehouse Management ("Manage operations from receiving to shipping"), Network Optimization ("Reduce costs and delivery times with warehouse placement"), FlowspaceAI, Reporting (financial, shipping, channel, inventory insights).
- **Execution loop visible in product UI claims**: status cards "Open order O-543656546 routed to warehouse → Picking SKU ABC123 with 2 items picked from PL-4532 → Packed shipping label purchased with tracking number"; tracking timeline (Packed → Awaiting carrier pickup → Shipped in transit → Delivered).
- Shipping service-level selection (Lowest Price / Ground / Three-Day / Two-Day / Next Day) with "high-cost orders flagged for review"; order changes allowed "up until packing"; custom rules to "reward repeat buyers"; lot tracking + expiration date tracking + ship-by-date rules in FDA-registered facilities; integrations with carts/marketplaces/retailers/EDI.

### Reused sibling-sample evidence (order-fulfillment-platform pass, 2026-09-08)

- **ShipStation** (Tier-1): "import your orders… set the carrier… print the labels… notifies the stores and your customers"; marketplace shipment notifications carry tracking/carrier/order id; default trigger label creation, delays possible; inventory with committed counts; Order Routing (plan-gated); fulfillment-provider destinations (FBA/Shipwire/dropshippers).
- **ShipHero** (Tier-1): order statuses drive pick queues; six hold types + locks; MIB/SIB/DirectPack picking; weight discrepancy detection; multi-warehouse allocation; 3PL Client Portal; used by brands AND 3PL operators.
- **ShipMonk** (Tier-2): provider-operated FCs; merchant-facing OMS/WMS/IMS; order status flow import→delivery; auto FC selection; SLA-at-risk dashboards; cost per order by pick/pack/ship/storage.
- **Red Stag** (Tier-2): provider-operated; merchant dashboard with inventory split across FCs; guarantees (zero shrink/mispick/late).

## Cross-product Comparison

| Structure | Logiwa | Mintsoft | J&J ControlPort | Flowspace | ShipStation* | ShipHero* | ShipMonk* | Red Stag* | Layer |
|---|---|---|---|---|---|---|---|---|---|
| Orders from connected selling channels (+ manual/CSV/mail/API) | ✓ "pre-integrated with all your sales channels" | ✓ channels + manual + **mail orders** (Tier-1) | ✓ "orders from your website, marketplaces, retail partners in one platform" | ✓ "any order from any sales channel" | ✓ | ✓ | ✓ | ✓ | B (8/8) |
| Merchant's OWN stored inventory at fulfillment location(s) | ✓ warehouse stock (brand or 3PL clients' goods) | ✓ warehouse stock, ASNs/POs, multi-location (Tier-1) | ✓ client stock at J&J FCs, ASN goods-in | ✓ brand inventory, lot/expiry, FDA-registered facilities | ✓ | ✓ | ✓ | ✓ | B (8/8) |
| Order→pick→pack→despatch execution loop | ✓ warehouse execution | ✓ batch/rebin picking, barcode verification (Tier-1) | ✓ "picking and packing through to despatch and carrier handover" | ✓ status cards routed→picking→packed+label+tracking | ✓ | ✓ | ✓ | ✓ | B (8/8) |
| State model governing the queue | ✓ (exec platform) | ✓ 23 statuses incl. holds policy (Tier-1) | ✓ "clear order status at every stage… exceptions flagged early" | ✓ status cards | ✓ statuses+holds | ✓ statuses+6 holds | ✓ status flow | ✓ dashboard | B (8/8) |
| Completion reported back to order's source | ✓ (shipping/channel sync; Tier-2) | ✓ "integrated sales channels are updated automatically" at despatch (Tier-1) | ✓ live tracking, status flow to client | ✓ tracking number purchased at pack; channel integrations | ✓ notifications | ✓ | ✓ | ✓ | B (8/8; Mintsoft Tier-1) |
| Holds / exception gating | ✓ (automation) | ✓ AWAITING*/QUERYRAISED/FRAUDRISK/PACKANDHOLD (Tier-1) | ✓ early exception alerts | ✓ high-cost flagged; order changes until packing | ✓ | ✓ 6 hold types | ✓ | (guarantee-driven) | B (7/8 A-evidenced) |
| Stock insufficiency policy (hold/back-order/split) | (inventory module) | ✓ Holding Order Policy, ONBACKORDER (Tier-1) | (inventory insights) | ✓ "Position your inventory closer to demand" (network) | — | — | — | — | A (1) + sibling partial |
| Carrier selection / labels / rates | ✓ smart shipping | ✓ shipping management, couriers | ✓ carrier handover; carrier performance | ✓ service-level selection incl. lowest-price | ✓ rate shop | ✓ | ✓ VCN | ✓ | B (8/8) |
| Inventory sync out to channels | ✓ (multichannel blog/positioning) | ✓ "Order retrieval and inventory sync" | (channels connected) | ✓ (channel integrations) | ✓ | ✓ | ✓ | ✓ | B (5/8 explicit; others implied — keep at common-mature, not definitional) |
| Returns processing | (via integrations) | ✓ returns & refunds collection | ✓ returns management | (returns via support) | ✓ portal | ✓ | ✓ | ✓ | B (6/8) |
| Multi-client (3PL) management: client records, client users, client portal | ✓ (3PL software) | ✓ client mgmt + Client Portal + warehouse/client user roles (Tier-1) | n/a (client IS the brand) | n/a (client IS the brand) | — | ✓ 3PL Client Portal | ✓ (3PL) | — | B (3/8 explicit; structure of the fulfillment-house variant) |
| Per-activity client billing (pick/pack/storage/goods-in costs) | (3PL pricing pages) | ✓ 3PL Accounting: picking costs, storage charging, goods-in charging (Tier-1) | ✓ cost breakdowns + live price book (client view) | ✓ (per-activity 3PL model) | — | — | ✓ cost per order | ✓ (service fees) | B (4/8; service/house pole) |
| SLA / performance reporting | ✓ analytics | ✓ SLA Dashboard (KB) | ✓ SLA tracking + fulfilment accuracy | ✓ reporting | (ship-on-time reporting) | ✓ | ✓ SLA-at-risk | ✓ guarantees | B (7/8) |
| Who executes physical work | merchant's or 3PL's staff | merchant's or fulfilment house's staff | provider's staff | provider's staff | merchant's staff | merchant's or 3PL's staff | provider's staff | provider's staff | B |
| Network placement / warehouse-location optimization | ✓ (fulfillment networks industry) | — | ✓ AI stock placement across FCs | ✓ Network Optimization (warehouse placement) | ✓ plan-gated Order Routing | ✓ MWA | ✓ auto FC selection | ✓ 2-FC split | B (6/8; optional layer, DOM-adjacent edge) |

\* = evidence inherited from the order-fulfillment-platform pass (fetched 2026-09-08); not re-fetched this pass.

## Canonical Abstraction

### L0 — Defining Invariant

**The same four jointly-held structures as the sibling Type** — the goods-identity + execution-loop + channel-loop test proposed by the forward flag passes on every sampled product, including all four sampled fresh this pass:

1. **Channel orders as the unit of fulfillment work.** Orders arrive from the seller's connected selling channels (plus manual, CSV, mail-order, API entry) and exist as persistent work records carrying items, quantities, recipient, service level, and a fulfillment state. Remove → nothing to fulfill (not a fulfillment management system).
2. **The seller's own stored inventory as the stock of record.** Goods are the seller's property held at fulfillment location(s) — its own warehouse(s), a fulfilment house's, or a provider's fulfillment centres operated on its behalf; allocation commits this stock to orders (Mintsoft Tier-1: NEW = "all stock has been allocated"; CANCELLED = "allocations released"). Remove → supplier-stock forwarding (dropshipping) or a bare label tool.
3. **The order-to-shipment execution loop.** Each order is allocated, physically picked and packed (scan-verified in mature products), and turned into a carrier shipment with label and tracking identity; the state model gates every step (Mintsoft Tier-1: NEW/PRINTED → AWAITINGPICKING → PICKINGSTARTED → PICKED → PACKED → DESPATCHED). Remove → order ledger without execution (OMS/DOM) or warehouse machinery without the order loop (WMS).
4. **Completion reported back to the order's source.** Despatch records tracking + date and updates the integrated sales channels automatically (Mintsoft Tier-1), closing the channel loop. Remove → internal warehouse tooling.

Jointly-held is load-bearing (same decomposition as the sibling pass): 1 alone = order importer; 2 alone = inventory system; 3 without 1+2 = label tool; 4 without 1–3 = tracking feed; 1+2 without 3 = order+stock ledger; 1+3 without 2 = dropship-forwarding edge; 2+3 without 1+4 = WMS territory.

**The "management" in the leaf's name adds NO load-bearing fifth structure.** What the name foregrounds — governing the queue (statuses, holds, exception paths), keeping inventory truthful, overseeing execution, controlling despatch cost and service level, monitoring completion and SLA — is the management surface OVER the same four legs, present in every sampled product of both poles, not a structure absent from the sibling Type. The sibling pass already documents that surface (order console, holds, automation, dashboards).

### L1 — Common Mature Structure

- Order holds / exception gating taxonomy (payment, documentation, fraud, queries, release dates, confirmation) — Tier-1 evidenced in Mintsoft; ShipHero's six hold types
- Automation rules (tagging, status assignment, routing, packaging logic)
- Carrier connections + rate selection (lowest qualifying rate / service levels)
- Barcode scan validation at pick/pack touchpoints; batch picking methods (single/multi-tote/bulk/rebin/zone)
- Inventory sync out to channels (oversell prevention); stock insufficiency policies (manual hold / back-order / split)
- Returns processing feeding stock back into the loop
- SLA and performance/cost reporting (ship-on-time, fulfilment accuracy, cost per order/pick/pack/storage)
- Multi-location allocation / routing (closest vs fewest shipments; auto FC selection) — the DOM-adjacent edge
- 3PL client portal + per-activity client billing in the fulfillment-house variant
- Customer notifications (despatch confirmation, tracking pages)
- API/webhooks; user/permission model spanning warehouse staff and (in 3PL variants) client users

### L2 — Variant / Optional Structure

- Operating posture: self-fulfillment software (merchant's staff execute) ↔ fulfillment-house/3PL software (the operator runs fulfillment for many client brands) ↔ provider-operated service with a proprietary merchant-facing platform ↔ hybrid vendors
- Buyer identity: brand operations teams vs fulfillment-house operators vs provider account managers
- Execution depth: shipping-centric (label/rate focus) ↔ warehouse-execution-grade (batch methods, location management, replenishment, pallet/carton handling, labor)
- Channel mix: D2C parcel ↔ B2B/retail (routing guides, EDI, pallets) ↔ marketplace programs (FBA prep/replenishment — Mintsoft PROCESSING status explicitly covers "Amazon FBA replenishment")
- Geography: UK "fulfilment house" market strongly present in-sample (Mintsoft, J&J); US D2C 3PL market (Flowspace, ShipMonk-class)
- Goods specialization: lot/expiry/BBE tracking, FDA-registered handling, big-and-heavy
- Billing: software subscription ↔ per-fulfillment-activity service fees
- AI-era additions: AI stock placement, AI agents, network optimization suggestions

### L3 — Vendor-specific (research notes only)

- Mintsoft: Holding Order Policy as a named configuration; internal/external status naming split (INVOICED displays as DESPATCHED externally); Rebin picking; "highest point" location-type storage charging; mail-orders channel type
- J&J: ControlPort™ brand; Navigator™ consultative services; Seymour AI assistant; live price book
- Flowspace: Pod3PL, FlowspaceAI, fulfillment-freedom-fund promotion, N4 naming
- Logiwa: Logiwa IO, App Store ecosystem, agentic-AI architecture marketing
- ShipMonk: Virtual Carrier Network, MonkProtect (sibling pass)

## Rejected Findings

- **"E-commerce fulfillment management is a distinct management/orchestration layer above fulfillment execution"** — rejected. Every management capability sampled (queue governance, holds, SLA/cost monitoring, network placement) exists inside products that also execute the loop, and inside the sibling Type's documented products. No sampled product manages fulfillment without the execution legs. The management surface is the L1 layer over the same core, not a separate Type.
- **"This leaf = 3PL business management (running a fulfillment house as a business)"** — rejected as the Type's identity. The multi-client structures (client records, client users, client portals, per-activity billing) are real and Tier-1-evidenced (Mintsoft), but they attach to the same order/inventory/execution objects and appear only in the fulfillment-house variant of the same product family; the sibling pass already absorbed the 3PL posture ("used by brands and 3PL operators"; "account managers who watch fulfillment on behalf of the brands they serve"). Held as the fulfillment-house variant's enrichment, not a definitional leg.
- **"Fulfillment management = WMS"** — rejected as identity (consistent with the sibling pass). Logiwa and Mintsoft self-label WMS, but their documented center of gravity is the channel order's journey ending in despatch and channel sync-back; warehouse machinery serves the order. The WMS seam (warehouse as subject) is adopted unchanged.
- **"Network placement (Flowspace Network Optimization, AI stock placement) is definitional"** — rejected to L2. It is the DOM-adjacent edge (same as ShipStation's plan-gated Order Routing in the sibling pass); optional, product-dependent.
- **"Mail-order intake is archaic"** — rejected: postal-order intake is a documented first-class channel type in a current product (Mintsoft "Set up mail orders"), supporting the historical check.

## Boundary Findings

- **vs Order Fulfillment Platform (§05.08 sibling — THE forward flag, DISCHARGED)** — the proposed goods-identity + execution-loop + channel-loop test was applied to four fresh products marketed under "e-commerce fulfillment (management)" (Logiwa, Mintsoft, J&J ControlPort, Flowspace): all four exhibit the sibling's four-leg core with no load-bearing unique leg; the sibling's four products equally market as "ecommerce fulfillment" (ShipMonk's "Ecommerce Fulfillment" line, Red Stag's "D2C fulfillment"). **Disposition: the two directory leaves name ONE product family — the merchant/fulfillment-house-side system that turns channel orders into dispatched, reported-back shipments. "E-commerce Fulfillment Management" is the market's management-discipline name; "Order Fulfillment Platform" is the platform-product name. Keep-both as market-name labels for one Type; taxonomy consolidation recommended for future directory maintenance; no directory change made unilaterally.** This document is written as the same Type viewed from the management-discipline name, with the fulfillment-house (multi-client) variant given its natural emphasis.
- **vs OMS / Distributed Order Management (§05.07)** — DOM centers the order × network × sourcing decision; here the order's physical fulfillment is the subject. Placement features (Flowspace Network Optimization, Mintsoft's split policy, ShipStation Order Routing) are the documented straddle edge, held as optional.
- **vs WMS (§10)** — warehouse-subject vs order-subject seam adopted unchanged: Logiwa/Mintsoft self-label WMS while operating order-driven fulfillment; fulfillment management commonly embeds WMS-grade machinery.
- **vs Dropshipping Platform (§05.20)** — goods-identity test confirmed again from this side: AWAITINGADDITIONALITEM explicitly covers a drop-ship order being combined with a warehouse order (Mintsoft Tier-1) — drop-ship combining is an edge mode inside an own-stock system.
- **vs Delivery Experience Platform (§05.08)** — phase seam held: operation to carrier handoff + channel sync; live tracking pages (J&J, Flowspace) are client/merchant-facing monitoring, not the consumer-facing branded post-purchase surface Type.
- **vs Returns Management Platform (§05.09)** — reverse operation seam held; returns are a module feeding stock back (Mintsoft returns collection, J&J returns management).
- **vs Inventory Management System (§10)** — inventory here exists to be allocated and shipped inside the loop; ASNs/POs/replenishment appear as supporting collections, not the center.
- **vs Multi-marketplace Seller Platform (§05.23)** — channel/listing sync vs physical execution; complementary layers.
- **vs TMS (§18)** — shipment as output of order execution vs bought transportation as unit of record; managed freight (Flowspace) is a service edge.

## Historical / Market-Sample Check

Paper-era mail-order fulfillment operation: orders arrive by post/phone (Mintsoft still ships a "mail orders" channel type — historical continuity in-product), the merchant's own goods on shelves, pick → pack → postage, dispatch log + notification back. All four legs satisfied at analog level. The 2000s cart + shipping-software generation satisfies without cloud/AI/3PL portals. The fulfillment-house model predates software (mail-order fulfilment houses) and fits the fulfillment-house variant with paper ledgers replacing the billing module. UK "fulfilment" spelling dominance in the service pole shows regional naming, not structural difference. Definition names no era-specific machinery. **Historical check passed.**

## Uncertainties

- ShipBob (major US service-operator pole) unreachable 403 ×3 across two passes — the service pole rests on J&J + Flowspace (fresh) + ShipMonk + Red Stag (inherited); no ShipBob claims made.
- J&J's client help desk (zendesk) is login-gated — ControlPort known at product-page depth only (Tier-2); no operational defaults claimed.
- Flowspace and Logiwa reached at Tier-2 (product pages); no Tier-1 KB sampled for either; precise features (e.g., Logiwa's channel sync-back mechanics) are position-level, not workflow-level.
- Amazon FBA not directly sampled (login-gated); FBA appears as a named status trigger (Mintsoft PROCESSING) and a provider destination (sibling evidence).
- Exact notification-timing defaults, plan gating, numeric limits deliberately excluded (evidence precision rule).
- Whether the market's directory should merge the two §05.08 execution-side leaves — recorded as a boundary issue for maintainers; not decided unilaterally.

## Final Synthesis

"E-commerce Fulfillment Management" and "Order Fulfillment Platform" are two market names for one Application Type: the merchant/fulfillment-house-side system that receives orders from connected selling channels, holds them as stateful work records, allocates them against the seller's own stored inventory at fulfillment location(s), drives the physical pick/pack work through a state-governed loop, turns each order into a carrier shipment with tracking, and reports completion back to the selling channel. The leaf's name foregrounds the management surface — queue governance (statuses, holds, stock-insufficiency policies), inventory truth, execution oversight (barcode-verified picking and packing), despatch control (rates, service levels), completion and SLA/cost monitoring — and the market realizes the Type across the same operating poles: self-fulfillment software, warehouse-execution-grade fulfillment software for brands and fulfilment houses (with client portals and per-activity client billing), and provider-operated fulfillment services with proprietary merchant-facing platforms. The forward flag from the order-fulfillment-platform pass is discharged: goods-identity, execution-loop and channel-loop tests pass 8/8 across the combined sample; keep-both recorded as labels of one Type; no unique definitional leg found for this leaf.
