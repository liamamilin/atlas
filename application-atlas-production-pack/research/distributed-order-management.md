# Research Notes — Distributed Order Management

Slug: distributed-order-management
Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Distributed Order Management system actually is as an Application Type: its core objects, its defining workflow (sourcing orders across a fulfillment network), who uses it, which interfaces it presents, which rules and states matter, and where its boundary lies against neighboring Types (generic OMS, order orchestration, WMS, inventory management, TMS, sales order capture, returns, e-commerce fulfillment).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: a retailer/brand receives orders from multiple sales channels and must decide, per order/line, WHERE in a network of fulfillment locations (DCs, stores, vendors, 3PLs) each item is fulfilled from, then track execution to completion.
- Users: omnichannel/commerce operations, customer service, store/DC associates, supply-chain teams.
- Nearest neighbors: Order Management System / OMS (§05.07 sibling), Order Orchestration Platform (§05.07 sibling), Order Fulfillment Platform (§05.08), WMS (§10), Retail Inventory Management (§05.12), TMS (§18), Sales Order Capture (§07), Returns Management Platform (§05.09), Delivery Experience Platform (§05.08).
- Unknowns: how "distributed" differs from generic "order management" in market practice; whether splits/transfers are definitional; how deep into fulfillment execution DOM products go; historical (pre-omnichannel) fit.

Pre-hung seams inherited from STATUS.md:

1. sales-order-capture (§07, processed 2026-09-07): capture = create/confirm/amend the order record; OMS-side = route/split/source/fulfill across channels/locations after the record exists — joint review recommended when §05.07 leaves are processed. This pass operates on the OMS side of that seam.
2. returns-management-platform (§05.09, processed): seam "forward order lifecycle vs reverse operation"; joint review recommended when the §05.07 leaves are processed.
3. multi-marketplace-seller-platform (§05.23, processed): forward flag for order-management-system-oms — order-centric fulfillment orchestration across sources vs channel/listing-centric selling operation. This pass sits on the order-centric side.
4. transportation-management-system-tms (§18, processed): "demand commonly arriving as ERP/OMS orders consolidated into shipments" — to confirm/discharge from this side.

## Research Questions

1. What is the "order" in DOM — structure, states, and where it comes from?
2. What is a fulfillment location/node and what node types exist?
3. What exactly is the sourcing/routing/brokering decision and how is it configured (rules, conditions, criteria, strategies)?
4. What happens when no single node can fulfill an order (splits, transfers, consolidation, partial allocation, fallbacks)?
5. What omnichannel fulfillment methods does the Type carry (ship-from-store, BOPIS, curbside, ship-to-store, dropship)?
6. How does inventory visibility/ATP relate to the sourcing decision?
7. What execution surfaces exist at the node, and how much fulfillment execution belongs to the Type vs WMS/store ops?
8. What states and exception machinery exist (re-sourcing, blocking, substitution, cancellation cascades)?
9. Who are the users and what interfaces do they face?
10. Boundary: what distinguishes DOM from generic OMS, from order orchestration, and from WMS/fulfillment/inventory systems?

## Representative Products

Selection logic: market representation (two widely-cited enterprise anchors attempted), documentation completeness (public Tier-1 docs required), different product philosophy (composable suite / cloud-native standalone / platform-native orchestration hub / open-source-heritage mid-market), different customer tier.

| Product | Philosophy / segment | Docs access | Evidence depth |
|---|---|---|---|
| Kibo Commerce OMS | Composable commerce suite; OMS + storefront + B2B/B2C; mid-market→enterprise | docs.kibocommerce.com — full Tier-1 | Deep (conceptual guides: Order Routing, Fulfillment, OMS solution page) |
| Fluent Commerce | Cloud-native standalone OMS; retail omnichannel; enterprise | docs.fluentcommerce.com — full Tier-1 | Deep (Responsive Sourcing Framework, Order lifecycle, glossary) |
| Microsoft Dynamics 365 Intelligent Order Management | Platform-native orchestration hub on Dataverse; provider framework; B2C/DTC/B2B | learn.microsoft.com — full Tier-1 | Medium-deep (overview + component model) |
| HotWax Commerce | Apache OFBiz-heritage OMS; Shopify/NetSuite-centered mid-market retail; scheduled brokering | docs.hotwax.co — full Tier-1 | Medium (Order Routing app docs; doc index of fulfillment/store apps) |

Attempted and excluded:

- IBM Sterling Order Management System — canonical enterprise market anchor; docs 403 on two URL patterns (ibm.com/docs). Abandoned per network rules; NO claims made about IBM product behavior.
- Manhattan Associates (Active Omni Order Management) — product page 403. Abandoned; no claims.
- Salesforce Order Management — developer docs 403. Abandoned; no claims.
- Radial — PRODUCT MISMATCH: the vendor's site now presents 3PL ecommerce fulfillment services ("Radial is becoming Paxon"), not a licensable distributed order management product; dropped from the sample. No product claims.

## Sources

All fetched 2026-09-08:

- Kibo: https://docs.kibocommerce.com/ (doc index), https://docs.kibocommerce.com/solutions/order-management , https://docs.kibocommerce.com/concept-guides/order-routing , https://docs.kibocommerce.com/concept-guides/fulfillment
- Fluent Commerce: https://docs.fluentcommerce.com/ (doc index), https://docs.fluentcommerce.com/by-type/glossary_term/sourcing , https://docs.fluentcommerce.com/essential-knowledge/responsive-sourcing-framework-overview , https://docs.fluentcommerce.com/by-type/glossary_term/sourcing-profile , https://docs.fluentcommerce.com/essential-knowledge/order-lifecycle
- Microsoft: https://learn.microsoft.com/en-us/dynamics365/intelligent-order-management/overview
- HotWax: https://docs.hotwax.co/documents , https://docs.hotwax.co/documents/retail-operations/orders/order-routing

Evidence layers: A = directly observed on a specific product's official docs; B = cross-product commonality across the sample; C = canonical inference from comparison + boundary reasoning.

## Product Observations

### Kibo Commerce OMS (Layer A)

- OMS solution page: "unified order orchestration across all sales channels", "intelligent fulfillment routing, real-time inventory visibility, and streamlined customer service operations"; capabilities: Real-Time Inventory, Order Routing, Fulfillment Operations, Returns Management.
- Order Routing (concept guide): "the dynamic decision-making logic that determines the optimal fulfillment location(s) for a customer order based on a configured set of business rules and real-time inventory and location data"; "central orchestration engine within the unified commerce platform".
- Hierarchy: Routes (strategies per order type) → Scenarios (a set of locations + filters + after actions, evaluated in sequence until assignment or route exhausted) → Locations: "physical or virtual entities (e.g., warehouse, store, dropshipper) that hold inventory and can fulfill orders".
- After Actions: fail over to the next Scenario, SPLIT the order to fulfill different items from different locations, or route items to customer care / cancellation.
- Filters in five categories: Item, Location, Order, Customer, Inventory; first-class + extensible custom attributes; e.g. hazardous-goods certification, insulated packaging, VIP tier routing, B2B-account-only locations, inventory reserved for kiosk sales.
- Capacity: daily order-assignment thresholds per location (documented example: store capacity limit excludes it from the pool until next day).
- Geographic proximity routing (lat/long distance as sort or radius filter); excess-inventory prioritization as a sorting rule.
- Fulfillment types in routing: Direct Ship; Delivery (local/last-mile); BOPIS "never uses Order Routing for initial assignment" (customer chose the store) but invokes Transfer Routes when the pickup store lacks stock; consolidation transfers move inventory to a receiving location so the order ships complete.
- Early invocation: routing check at cart/checkout to determine in real time whether a delivery/pickup method is viable ("maintaining high customer confidence in fulfillment promises").
- Upstream dependencies: real-time inventory visibility ("Outdated or inaccurate stock levels will lead to fulfillment failures"), location/facility management, catalog attributes. "Single view of inventory across the entire enterprise... treat store stock as sellable online inventory."
- Downstream: assignment "dictates the destination of the shipment, initiating the fulfillment workflow (e.g., picking, packing, shipping) at the assigned location"; origin determines carrier options/rates/EDD; CSR work needs the fulfilling location.
- Fulfillment guide: Fulfillment is "the execution layer"; BPM flows define shipment state transitions per fulfillment type (STH, BOPIS, Delivery); Fulfiller UI dashboard with Map/List views and SLA thresholds (Compliant / At Risk / Non Compliant).
- Exception machinery at the node: Rejection, Splitting (available portion processed, remainder into a child shipment for re-routing), Transfer (acquire missing items from another location; Wait for Transfer state; Receive Transfers page), Substitution (with required reason; also pre-fulfillment substitution by CSRs on pending orders), Cancellation, Location Blocking (temporary until inventory refresh or persistent "Keep location excluded"; Manage Blocked Locations page).
- Package consolidation: qualifying shipments (same location/type/customer/address/method) merge; single tracking number.
- Pick waves: group shipments by SLA, carrier, method, customer segments for wave/zone picking.
- Financial gate: "blocking shipments from entering the fulfillment workflow if the associated order has unpaid or completely errored payments."
- Remorse period: configurable delay between order submission and shipment creation (fraud check/edit window).
- Reverse logistics: Return routes (inbound movement of returns) and Disposition routes (restock/refurbish/liquidate/discard).
- EDD calculation leverages location capacity data ("Average Hours to Fulfill").
- Downstream integrations: SLA-miss event notifications to external systems (WMS, dashboards); shipment updates relayed to marketplaces via ChannelAdvisor-class connectors.

### Fluent Commerce (Layer A)

- Docs root self-labels the product class: "Order Management Systems (OMS) help you to optimize your fulfillment processes."
- Sourcing (glossary): "the process of where to fulfill an order from. This involves evaluating various factors such as inventory levels, shipping costs, delivery times, and customer location."
- Responsive Sourcing Framework: modular configuration for sourcing logic — Sourcing Profile (master plan per order type / brand / region) → Primary Sourcing Strategies (evaluated in priority order; order sourced by the first strategy that can fulfill the request IN ITS ENTIRETY) → Fallback Sourcing Strategy (backup when no primary strategy suffices) → Sourcing Conditions (boolean filters: order date, delivery country, customer tier, product category; AND-combined) → Sourcing Criteria (ranking functions scoring locations — distance to customer, available inventory, network priority; sequential tie-breaking). Profiles referenced by Order or Availability workflows.
- Split control: framework "attempts to minimize the number of fulfillment splits (limited to the maxSplit value)"; strategies aim to fulfill from a single location first.
- Sourcing auditability: "an immutable record of every sourcing decision... captures the sourcing profile and version applied, each strategy considered, the pass or fail result of every condition, and per-location criteria scores and positions."
- Order lifecycle (OMS UI): Order List (filterable by retailer, status, type, dates; role/permission-gated) → Order Details (Summary, Retailer Info, Customer, Collection/Delivery Info cards + Fulfillments table + Order Items table; tabs: Details, Fulfillments, Transactions, Attributes, Returns, Comments, Activity) → Order Item Details.
- Order structure: an Order holds multiple Fulfillments; each Fulfillment carries Status, Delivery Type, Fulfillment Location, Destination (store for Click-and-Collect or customer address for Home Delivery).
- Order types in reference module: CC (Click and Collect) and HD (Home Delivery); mixed baskets reference workflow.
- Status labels observed: Booked (submitted from the eCommerce site), Pick & Pack, Awaiting Courier Collection, Complete, Canceled (product-specific labels).
- Multi-tenant: "orders from all retailers associated with the logged-in user" — retailer as an org dimension with its own commission.
- Re-sourcing: "Partial Order Sourcing; Re-Sourcing after operational exceptions" listed as framework use cases.
- Fluent OMS web apps manage orders, product availability, inventory, and fulfilment; GraphQL/REST APIs, events, workflows, rules SDK — configuration-first platform.

### Microsoft Dynamics 365 Intelligent Order Management (Layer A)

- Positioning: "manage the orchestration of orders through to fulfillment... orchestrate order flows across different platforms and apps"; "designed to operate in complex environments where many internal and external systems and partners enable the supply chain processes"; B2C, DTC, B2B flows.
- Motivating scenario: customers implementing "buy-online ship and buy-online and collect" choose different e-commerce systems and fulfillment partners; IOM integrates them "into a single system".
- App: "an interface to view orders and the fulfillment state... a single place to view orders, regardless of the order source or how they were fulfilled." Orders originate in "different e-commerce systems, point of sales systems, electronic data interchange (EDI), and customer relationship management (CRM) apps."
- Providers: wrap API calls between systems and present them as actions; actions raise events that drive the orchestration; first-party (Dynamics 365 Supply Chain Management, Commerce, Finance) and third-party (e-commerce platforms, fulfillment and logistics systems); Power Automate connector ecosystem.
- Orchestration: business users configure flows that "manage the journey of an order"; embedded policy designer for rules; journey orchestration designer to "model and automate the response to fulfillment constraints"; ML mentioned as an optimization influence.
- Inventory Visibility Service: "real-time visibility of inventory in the supply network... single, global view of the inventory positions across all legal entities"; feeds fulfillment decisions.
- Fulfillment optimization: "a service that you can leverage through the orchestration flow... enables optimization decisions about where an order can be fulfilled, using concepts such as cost and closest in distance"; "define different fulfillment strategies... to determine the best location to fulfill an order from."
- Insights: Power BI dashboards of order and fulfillment metrics/KPIs.
- Built on Dataverse/common data model; no dependency on other Dynamics apps.

### HotWax Commerce (Layer A)

- Order Routing Rules app "to decide which orders the order routing engine attempts, which fulfillment locations it checks, and what happens when inventory is unavailable."
- Sourcing section: threshold, safety stock, store pickup, shipping, inventory channel, and inventory visibility settings; ATP ("available-to-promise inventory") documented.
- Routing structure, three levels: Routing group (when a set of routings runs — scheduled, e.g., "Run standard order routing every six hours") → Routing (which orders are selected and in what sequence — "Select standard shipping orders from the brokering queue, oldest first"; promise date can drive selection) → Routing rule (which facilities are eligible, how facilities are ranked, and what happens to unavailable items — "Try nearby warehouses first, then move remaining items to the next rule"; partial allocation; unavailable-item actions).
- Terminology: "brokering runs" (older name for routing groups) and "brokering queue"; facilities and facility groups; routing history and reports.
- Strategy testing tools (feature-gated): Simulation, Circuit, Test Drive.
- Store Operations apps: BOPIS Fulfillment App, Fulfillment App, Returns, Receiving, Cycle Count, Transfer Orders — fulfillment execution surfaces for store associates.
- Retail Operations apps: Orders, Inventory, Order Routing, Pre-Orders, Returns, Job Manager/Workflows (scheduled jobs).
- System admin: Company, Product Store, Users, Facilities, Fulfillment, Data Manager.
- Integration posture: Shopify (product/order/inventory sync), NetSuite (ERP), marketplace channels, RetailPro POS, Klaviyo/Iterable, EasyPost — the OMS sits between commerce channels and ERP.

## Cross-product Comparison

| Dimension | Kibo | Fluent | Microsoft IOM | HotWax |
|---|---|---|---|---|
| Self-label | "OMS" / "unified order orchestration" | "OMS" / "Order Management" | "Intelligent Order Management" / order orchestration | "OMS" |
| Order of record | Unified orders across channels, single lifecycle with statuses | Order list/detail with fulfilments + items, multi-retailer | Single order view "regardless of the order source" | Orders in brokering queue synced from Shopify/marketplaces |
| Node concept | Locations: warehouse, store, dropshipper ("physical or virtual") | Locations grouped in networks | External fulfillment systems reached via providers | Facilities + facility groups |
| Sourcing decision | Order Routing: routes → scenarios → filters → after actions | Sourcing: profiles → strategies → conditions → criteria | Fulfillment optimization service: strategies using cost/distance | Order routing: routing groups → routings → rules (facility eligibility/ranking/partial allocation) |
| Split behavior | After action: split order across locations | min-splits target with maxSplit cap; partial sourcing | (via orchestration flows; not detailed on overview) | Partial allocation; unavailable-item actions |
| Transfers | Transfer routes (incl. BOPIS transfers) | (re-sourcing after exceptions) | (via providers) | Transfer Orders app; Wait-for-Transfer machinery in Kibo; HotWax transfer orders app |
| Inventory dependency | Real-time visibility mandatory; "outdated stock → fulfillment failures" | ATS stock per location; availability workflows | Inventory Visibility Service, global view | ATP, safety stock, thresholds |
| Node execution surface | Fulfiller UI + BPM flows (pick/pack/ship) | Fulfillment records tracked; web apps | Delegates to providers/WMS | Fulfillment App / BOPIS App for stores |
| Exception machinery | Rejection, split, transfer, substitution, block, cancel | Re-sourcing after exceptions | Constraint response via orchestration designer | Unavailable-item actions; rejected-item re-selection |
| Returns extension | Return routes + disposition routes | Returns tab on order; return orders | (not detailed on overview page) | Returns app; RMA flows |
| Configuration actor | Business config of routing strategies | Both technical and business users; dedicated UX | "business user to directly change order flows" | Retail operations team via apps |
| Audit/explainability | Routing strategies + history | Immutable sourcing audit record | Policy designer (audit not stated on page) | Routing history/reports; simulation (gated) |
| Analytics | Fulfillment SLA dashboard | Embedded analytics | Power BI insights | Analytics apps (orders/fulfillment/inventory) |
| Integration spine | APIs, connectors, marketplace relay | GraphQL/REST/events-first | Provider framework (Power Automate) | Shopify/NetSuite/marketplace sync |

### B-layer findings (cross-product commonality, 4/4 unless noted)

- B1. A channel-neutral, persistent order of record that consolidates orders arriving from multiple external commerce channels/systems, independent of any single node. (All four.)
- B2. A modeled fulfillment network: multiple distinct fulfillment locations held as addressable, individually configured source nodes (DC, store, vendor/dropshipper, 3PL). (All four; vocabulary differs — locations/facilities/providers.)
- B3. A configurable sourcing/routing decision engine: per order/line, rules + rankings (distance, cost, inventory standing, capacity, capability, customer tier) select the fulfilling node(s). (All four; named "sourcing" or "routing" or "brokering" or "fulfillment optimization".)
- B4. The order's fulfillment is decomposed into per-node fulfillment sub-records (fulfillment/shipment/assignment) with their own lifecycle states, tracked back to the order. (Kibo shipments, Fluent fulfilments, HotWax per-facility allocation, IOM fulfillment state on the order view.)
- B5. Splitting across nodes and partial fulfillment are standard machinery for when no single node can satisfy; alongside transfers (move stock to the fulfilling node) and consolidation (fewer shipments). (Kibo + Fluent + HotWax direct; IOM via orchestration, weak evidence → B/qualified.)
- B6. Real-time network inventory visibility / ATP is a mandatory upstream dependency of the sourcing decision. (All four.)
- B7. Exception handling with re-sourcing: stockout at execution → re-route remainder, optionally block the failing node for future assignments. (Kibo + HotWax direct; Fluent re-sourcing after exceptions; → B.)
- B8. Omnichannel fulfillment methods as first-class order attributes: ship-to-home, in-store pickup (BOPIS/click-and-collect), local delivery, ship-from-store. (All four.)
- B9. Customer service view: one screen with the order's current fulfillment state and history. (All four.)
- B10. Business-user-facing configuration surfaces for sourcing logic. (All four.)
- B11. Analytics over order and fulfillment KPIs. (All four.)
- B12. Returns/reverse handling attached to the same order spine. (Kibo, Fluent, HotWax direct = 3/4; IOM not verified on fetched page → B/qualified.)
- B13. API/event-first integration surface; the DOM sits between commerce channels upstream and fulfillment/inventory/ERP systems downstream. (All four.)
- B14. Promise/EDD and early availability checks at shopping time. (Kibo explicit early invocation + EDD; HotWax promise-date-driven selection; Fluent availability workflows; IOM fulfillment strategies in flow → B, strength varies.)

## Canonical Model (Layer C)

Four jointly-held, minimal invariants:

1. **The channel-neutral order of record** — persistent, individually identified customer order (header + lines) held by the system itself, consolidating orders that arrive from multiple external commerce sources; the system is authoritative for the order's fulfillment state. Remove → per-channel order queues with no single order picture (that is channel/ERP territory).
2. **The fulfillment network of record** — a standing, modeled set of distinct fulfillment locations (DCs, stores, vendors/dropship suppliers, 3PLs) as individually addressable nodes carrying inventory standing and fulfillment capability. Remove → single-site order fulfillment = ERP/order-entry + warehouse territory, not "distributed".
3. **The per-order sourcing decision** — for each order (and its lines), the system decides which node(s) will fulfill which quantities, governed by configurable rules/rankings (inventory standing, distance, cost, capacity, capability, customer/order context). The node choice is the defining act of "distributed" order management. Remove → order tracking/visibility without management.
4. **The tracked fulfillment lifecycle across the network** — sourced work is released to the chosen nodes as fulfillment sub-records, execution events flow back into the order's state, and the lifecycle is driven to completion/cancellation with the order as the anchor of record. Remove → a recommendation/allocation calculator that never executes.

Jointly-held is load-bearing:

- 1 alone = channel order aggregator/ERP order entry.
- 2 alone = network/site inventory or facility registry.
- 3 alone = allocation/recommendation engine (no record, no execution).
- 4 alone = shipment/order visibility platform (decides nothing).
- 1+2 without 3+4 = an order warehouse with no intelligence — not management.
- 2+3 without 1 = an allocation optimizer without an order of record.
- 1+3 without 2 = sourcing against nothing.
- 1+2+3 without 4 = decides but never tracks — an ATP calculator.
- 1+4 without 2+3 = order tracking console — Shipment-visibility / generic OMS-lite territory.

## Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit?

- Pre-omnichannel era: a mail-order/catalog retailer's order-processing system choosing which of several DCs ships each order, splitting when no DC covers all lines, and tracking shipment back to the order — satisfies all four invariants with zero omnichannel retail (no stores as nodes, no BOPIS, no web channels: a phone/mail order is one "channel"). PASSED.
- ERP-embedded order management with multi-plant/shipping-point allocation satisfies the core (order of record + plants as nodes + allocation decision + tracked delivery). The ERP is a packaging variant, not the Type.
- Vendor dropship management (customer order → PO to supplier who ships) satisfies the core with a vendor node.
- Store-as-node, ship-from-store, BOPIS, curbside, endless aisle are the MODERN COMMON LAYER, not definitional — a DC-only network fits the Type. This keeps the definition from being over-fitted to 2015+ omnichannel retail.
- AI/ML optimization, real-time streaming inventory, GraphQL APIs, cloud multi-tenant SaaS — era-current machinery, not definitional. An OFBiz-heritage, scheduled-batch brokering product (HotWax pattern: routing groups run e.g. on a schedule) fits the core — batch cadence vs real-time is an implementation variant. PASSED.

## Vendor-specific Findings (Layer L3 — keep out of the final document)

- Kibo: Routes/Scenarios/Filters/After Actions vocabulary; remorse period (1–7200 minutes documented range); 10-shipment consolidation cap; ChannelAdvisor marketplace relay; Manage Blocked Locations page; Pick Waves; Map/List SLA dashboard; "Direct Ship" vs "Delivery" fulfillment-type naming.
- Fluent: "Responsive Sourcing Framework" branding; Sourcing Profile/Strategy/Condition/Criterion nomenclature; maxSplit parameter; immutable sourcing audit record; Mystique SDK; reference order statuses (Booked / Pick & Pack / Awaiting Courier Collection / Complete / Canceled); CC/HD order types; multi-retailer commission field; GraphQL-first configuration.
- Microsoft IOM: Dataverse/Power Platform substrate; Power Automate provider framework; first-party vs third-party provider split; Inventory Visibility Service and Fulfillment Optimization as named services; Power BI insights.
- HotWax: brokering-run scheduling (six-hour example); Routing group → Routing → Routing rule three-level structure; Shopify/NetSuite integration posture; OFBiz heritage; feature-gated Simulation/Test Drive/Circuit.

## Rejected Findings

- "Splits are definitional" — REJECTED as invariant. A DOM that always fills each order from exactly one chosen node is still recognizably DOM; splitting is the standard machinery when no single node can satisfy (3/4 direct evidence). The invariant is the node CHOICE, not the split.
- "Omnichannel store fulfillment (ship-from-store/BOPIS) is definitional" — REJECTED. Pre-omnichannel and DC-only networks satisfy the core; 4/4 evidence is a market-era pattern, not the definition (anti-overfitting: the "phone number" precedent).
- "Real-time inventory sync is definitional" — REJECTED. Batch/scheduled brokering against imported ATP (HotWax pattern) still fits; the invariant is that sourcing depends on a held view of node inventory standing, not on any sync cadence.
- "Every DOM includes a full fulfillment-execution engine (pick/pack/ship) at nodes" — REJECTED as definitional. 2/4 sampled products ship store/DC execution apps; IOM explicitly delegates execution to provider systems. Node execution surfaces = common, not defining.
- "Returns processing is definitional" — REJECTED. 3/4 direct evidence, but the Returns Management Platform seam (forward vs reverse) stands; returns in DOM are an extension of the same sourcing logic (return/disposition routing), common but not defining.
- "DOM = OMS" — HELD AS TAXONOMY QUESTION, not resolved here. All four sampled products self-label "OMS" (B-layer finding). See Boundary Findings.
- "Payment-state gating of fulfillment is universal" — NOT CLAIMED. Only Kibo documents it in fetched pages; kept product-specific.
- "The sourcing decision must consider cost" — REJECTED as invariant. Cost is one common criterion among several (distance, inventory age/excess, capacity, customer tier); no single criterion is universal.

## Boundary Findings

- **vs Order Management System / OMS (§05.07 sibling, unprocessed)** — family problem. All sampled DOM products self-label "OMS"; the market uses OMS as the umbrella and "distributed order management" as the multi-node-sourcing capability inside it. Proposed seam for the sibling pass: DOM centers the multi-node fulfillment network + per-order sourcing decision; generic OMS (single-node or channel-centric order lifecycle management) lacks the network-choice invariant. JOINT REVIEW RECOMMENDED (discharges the sales-order-capture pass's request insofar as possible before the sibling is processed). ERP vendors label the entire span "sales order management", so packaging overlap is expected.
- **vs Order Orchestration Platform (§05.07 sibling, unprocessed)** — mechanism-vs-scope question. Orchestration (event-driven flows driving an order through steps) is one implementation spine of DOM (IOM's core), and Kibo calls routing its "central orchestration engine". Proposed seam: orchestration platform centers the flow/policy machinery; DOM centers the order×network×sourcing model. Likely keep-both with heavy overlap; JOINT REVIEW RECOMMENDED.
- **vs Sales Order Capture (§07, processed)** — seam adopted from that pass CONFIRMED from this side: orders arrive already captured/confirmed ("submitted from the eCommerce site" — Fluent; orders originating in e-commerce/POS/EDI/CRM — IOM; order sync from Shopify — HotWax). DOM takes the record after capture and manages fulfillment across the network. DISCHARGES that pass's joint-review request from this side.
- **vs Warehouse Management System / WMS (§10)** — decides-vs-executes. Kibo states assignment "initiat[es] the fulfillment workflow (picking, packing, shipping) at the assigned location" and that SLA-miss events can trigger external WMS workflows — i.e., the WMS executes inside the node; DOM may include lightweight node execution surfaces (store fulfiller apps) but deep warehouse execution is WMS. A DOM without any execution surface (IOM pattern) is still complete.
- **vs Retail Inventory Management / Inventory Management System (§05.12/§10)** — DOM consumes an inventory picture (ATP/safety stock/segmentation) and holds no perpetual inventory ledger of its own; Kibo names inventory accuracy as an upstream dependency; IOM ships a visibility service aggregating from source systems. Inventory data ownership lives in inventory systems; DOM holds the sourcing-relevant projection.
- **vs Transportation Management System / TMS (§18, processed)** — the TMS pass's flag CONFIRMED from this side: DOM's fulfillment assignments generate the demand that flows to transportation (origin, parcels, carrier options downstream of the node choice; Kibo: origin determines carrier options/rates). DOM decides from where; TMS decides how the goods move. DISCHARGES the TMS pass's inbound-order flag.
- **vs Returns Management Platform (§05.09, processed)** — seam adopted ("forward order lifecycle vs reverse operation") held: DOM's returns machinery (return routes, disposition routes) is an extension of the same sourcing logic; the standalone Returns Type centers the merchant-side reverse operation. Keep-both; joint-review flag noted for the sibling OMS passes.
- **vs Delivery Experience Platform (§05.08, processed)** — DOM produces the fulfillment/shipment events; the delivery-experience Type consumes them into a consumer-facing branded journey. Internal orchestration vs shopper-facing experience.
- **vs Order Fulfillment Platform (§05.08 sibling, unprocessed)** — expected seam (recorded for that pass): physical fulfillment operation management vs network-level order sourcing/orchestration. JOINT REVIEW RECOMMENDED.
- **vs E-commerce Fulfillment Management (§05.08 sibling, unprocessed)** — same expected seam as above; Radial's pivot to 3PL services illustrates that fulfillment-service offerings sit outside this software Type.
- **vs Multi-marketplace Seller Platform (§05.23, processed)** — CONFIRMED from this side: DOM is order/fulfillment-centric (channels are upstream sources of orders); the seller platform is channel/listing-centric (orders are one leg). Enterprise stacks run both integrated.
- **"Remove what to become another Type" test**: remove the network + sourcing decision → generic OMS/order tracking; remove the order of record → allocation/ATP calculator; remove cross-node choice → single-site order management (ERP); remove lifecycle tracking → promise/ATP recommendation tool; move the center to the reverse operation → Returns Management Platform; move the center to freight movement → TMS; move the center to node-internal execution → WMS/store ops.

## Uncertainties

- Enterprise anchors (IBM Sterling OMS, Manhattan Active Omni, Salesforce OM) unreachable (403 ×2 each pattern; abandoned). Their widely-claimed market presence could not be verified first-hand; no product claims made. If their docs were reachable, they would likely strengthen (not alter) the canonical model — but this remains unverified.
- Microsoft IOM evidence is overview-level; its split/transfer granularity and returns behavior were not verified on fetched pages (single-fetch depth, not access failure).
- Whether the market's "Order Orchestration Platform" leaf constitutes a distinct Type or a mechanism-layer view of the same population cannot be settled without the sibling's own product research.
- Pricing/packaging tiers and deployment ratios (SaaS vs self-hosted share) not researched — out of scope, no claims.
- Historical mail-order/ERP allocation claim rests on canonical inference from the model, not on fetched period documentation — held as Layer C inference, deliberately kept out of precise claims in the final document (phrased conceptually).

## Final Synthesis

Distributed Order Management is the order-management species whose defining core is the combination of a channel-neutral order of record + a modeled multi-node fulfillment network + the per-order sourcing decision across that network + the tracked fulfillment lifecycle anchored on the order. Everything else — splits/transfers/consolidation machinery, store-as-node omnichannel methods, inventory visibility services, fulfiller apps, promise/EDD, returns routing, analytics, ML optimization — is the common mature layer or variant structure. The market says "OMS" for all of it; the directory's three §05.07 siblings deserve a joint review to ratify keep-both/keep-family seams. Historical check passes at DC-allocation-era depth; the modern omnichannel retail layer is common, not defining.
