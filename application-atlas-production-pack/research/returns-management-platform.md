# Research Notes — Returns Management Platform

Research date: 2026-09-07

## Research Goal

Understand the **merchant-side** returns operation system: what objects exist, who works it, how a return moves from request to resolved outcome (money back / goods back / both), and where this Type sits against its sibling leaf (Returns & Exchange Portal, processed same day) and neighboring Types (OMS, WMS, fraud, store credit).

This leaf is the merchant-facing half of the 05.09 Returns family. The shopper-facing half is documented in `applications/returns-exchange-portal.md`; that pass explicitly deferred merchant-side detail to this pass. The two documents must hold a consistent seam.

## Initial Boundary

Temporary hypothesis before research:

- Core use: merchants receiving, deciding, processing, and financially resolving product returns/exchanges at scale.
- Users: returns/ops managers, CX agents, warehouse/3PL staff, finance.
- Nearest neighbors: Returns & Exchange Portal (sibling), Order Management System (forward lifecycle), WMS (receiving), Fraud Prevention (signals), Store Credit / Gift Card Management (ledger), Help Desk (agent cases), Retail POS (counter refunds).
- Unknowns: how far merchant-side goes (disposition/grading? liquidation? carrier claims?), whether "returns management" implies logistics orchestration or only decisioning, enterprise-vs-DTC structural differences.

## Research Questions

1. What is the unit of work on the merchant side? (RMA? return request? case?)
2. How are requests decided — who/what approves, rejects, or attaches conditions?
3. How do refunds, store credit, and exchanges actually execute from the merchant side?
4. What happens to returned goods — receiving, grading, restock, other disposition?
5. How is the physical journey orchestrated (labels, carriers, drop-off networks, consolidation)?
6. What integrations form the spine (commerce platform, payments, carriers, WMS/3PL, ERP, helpdesk)?
7. What exceptions and review queues exist in real products?
8. What analytics does the merchant side produce?
9. Where exactly is the seam with the shopper-facing portal, and with OMS/WMS?
10. Would an older / pre-automation / platform-native realization still fit the definition?

## Representative Products

Chosen for market representation, documentation quality, different product philosophy, different customer tier:

| Product | Philosophy / pole | Customer tier | Evidence quality |
|---|---|---|---|
| Loop Returns | exchange-first, workflow automation, DTC brand operations | mid-market DTC | Help Center (A) |
| AfterShip Returns | automation + API-first, post-purchase suite module | SMB → mid-market | API reference (A) |
| Happy Returns | reverse-logistics network pole (drop-off network, consolidation, verification) | mid-market → enterprise | product site (A) |
| ReturnGO | policy-automation / open-platform pole, sustainability framing | SMB → enterprise | product site (A) |
| ZigZag Global | global carrier-network + warehouse RMS pole (UK/international, 3PL-facing) | enterprise retail, 3PLs | product site incl. RMS page (A) |

Rejected/adjusted: **Optoro** (enterprise disposition/recovery pole) and **Narvar** (enterprise post-purchase suite) were selected initially but their sites returned 403/504 — dropped per the network-failure rule, recorded under Uncertainties. **ReturnGO** partially covers the sibling pass too (portal side); here it is used for merchant-side policy automation.

## Sources

All fetched 2026-09-07:

- Loop Returns — help.loopreturns.com: Help Center root (category map: Getting Started 29 articles; Loop Admin Settings 26 — subcategories General Settings 10 / Return Policy 7 / Shopper Return Portal 9; Loop Features 61; Labels and Shipping 26; Tracking 3; Point of Sale 7; Analytics 11; Accounting 8; Integrations 56; Third-Party Integrations 43); Loop Features category page (Workflows 6 articles; Shop Now 11; Exchanges 9; Bundles 1; Fraud & Abuse 4; Checkout+ 21; Loop Intelligence; Order Editing; Shopper Edit Return; Loop Assistant; Post-Purchase Offers; Slack Integration; Merchant Notifications; Background Agents); Workflows category page (Image & Video Upload; Workflows; Use Cases and Limitations; Common Workflow Templates; Warranties; Keep Item)
- AfterShip Returns — aftership.com/docs/returns: API root (operations: Create/Approve/Resolve/Reject Return, Receive items, Attach shipments, Remove return items, Record dropped-off return items, Update return items, Item tags, Returns Page deep link; webhooks); Return resource model (full schema, fetched in detail)
- Happy Returns — happyreturns.com root (solutions: Return & Exchange Portal; Return Bar® Network; Buy Online Return In-Store; Fraud Prevention; Non-consolidated Returns)
- ReturnGO — returngo.ai root (products: Returns, Warranty, Exchanges, Return Guard, Tracking, Shipping; integrations; workflows; insights/automation/API; white-label OEM)
- ZigZag Global — zigzag.global root (Returns Portal; Paid Returns; Live Exchanges; Refund to Store Credit; Return to Store; Reporting Hub; WhatsApp Returns; carriers network; Carrier Claims; German Returns Hub; white label) and /rms (Returns Management System for warehouses and 3PLs)

## Product Observations

### Loop Returns (evidence A)

From help-center structure and article summaries:

- Merchant surfaces organized as: Admin Settings (General / Return Policy / Shopper Return Portal), Features, Labels and Shipping, Tracking, Point of Sale, Analytics, Accounting, Integrations (56 + 43 third-party articles).
- **Workflows** = rules built "on top of their general return policies" for scenarios outside typical policy; supports requiring **photo/video upload** before submission, **Keep Item** (customers keep low-value/damaged items instead of shipping back), automated **Warranties** policies self-served through the portal; ships with common workflow templates.
- **Merchant Notifications**: "real-time email alerts and Slack messages when returns hit your **Needs Review queue**" — direct evidence of a merchant-side review queue as a first-class surface.
- **Background Agents** (Beta): "AI-powered returns automation feature that proactively reviews your returns queue on a schedule and recommends — or takes" actions.
- Exchange machinery: Exchanges (9 articles), **Shop Now** (11 articles) — shopping-like incentive flows; Bundles; Fraud & Abuse (4 articles).
- **Loop Intelligence**: proprietary foundation model "built on real commerce data from millions of returns".
- In-store dimension: Point of Sale category (7 articles); Accounting category (8 articles) — financial reconciliation surface; Analytics (11 articles).
- Loop Assistant: AI assistant inside Loop Admin for returns/workflows/policy questions.

### AfterShip Returns (evidence A — API resource model)

The Return resource is a direct structural disclosure of the merchant-side model:

- Identity/anchor: `rma_number`; order with `external_id`/`order_number` on the e-commerce platform; store; customer.
- **filed_by: shopper / merchant / customer_support** — merchant and support staff can create returns, not only shoppers.
- Approval lifecycle: `approval_status` = submitted / approved / done / rejected / expired; timestamps `approved_at`, `rejected_at`, `resolved_at`, `refunded_at`, `expired_at`; per-stage automation flags: `auto_approved`, `auto_rejected`, `auto_resolved`, `auto_refunded`, `auto_received`; `reject_reason`.
- Item-level quantities ledger: `ordered_quantity`, `intended_return_quantity`, `return_quantity`, `refund_quantity`, **`received_quantity`, `restocked_quantity`, `removed_quantity`**.
- Merchant-side item operations: `item_tags` (merchant-applied), `merchant_uploaded_image_urls`, `remove return items` API.
- **Return methods** enum: `retailer_label`, `customer_courier`, `happy_returns`, `in_store`, `green_return`, `carrier_dropoff`, `retail_reworks`, `carrier_pickup`.
- **Receiving**: `receivings[]` (receive operations with `received_at`); `auto_received` flag; `restocks[]`; shipping_status at return level: no_label / pending / in_transit / delivered / partially_received / received / partially_dropped / dropped / void.
- **Refunds**: `refunds[]` with `destination` (original_payment / store_credit / refundid), `gateway` (payment gateway), `store_credit_reference` (e.g., gift card code), `total`, per-item details, `transactions` (platform refund transaction records, "Shopify only for now"); `refund_destination` original_payment/store_credit; `estimated_refund_total`, `return_total_including_tax`, `return_tax`.
- **Exchange**: `exchange` object with an `order` (created in the commerce platform), items, tax, `bonus_credits`, `instant_exchange` payment status (pending/charged/canceled/failed), `charge_by`.
- **Dropoffs**: `dropoffs[]` with `qr_code_url`, `dropoff_number` (e.g., "Express Code from Happy Returns"), `service_provider` (happy-returns, retail-reworks), status created/dropped/partially_dropped — the platform records third-party drop-off network events.
- **Shipments**: `shipments[]` with tracking number/status/courier, `label` with `source` (shopper_upload / merchant_upload / merchant_api / merchant_generate), packing slip, conditional shipping documents.
- **Exceptions**: `exceptions[]` = exchange_failed / restock_failed / generate_label_failed / refund_failed / charge_failed / **flagged** — exceptions requiring manual handling.
- **cost_of_return**: `charged`, `value` — return cost accounting.
- `is_gift_return` flag; `green_return` (no physical return required); `shop_now` flag; outcomes: exchange/refund/upsell/store_credit.
- Webhooks for lifecycle events; Platforms enum for source systems.

### Happy Returns (evidence A — product site)

- Merchant-facing solutions: Return & Exchange Portal; **Return Bar® Network** ("10,000 Return Bar® locations", box-free label-free drop-off); **Buy Online, Return In-Store (BORIS)**; **Fraud Prevention**; **Non-consolidated Returns**.
- Merchant-side operating claims: "Returns arrive in as little as 5 days — pre-verified, labeled, and **consolidated** — driving **34% faster restocking** and 80% fewer CX contacts"; "Instant refunds triggered by **in-person verification**"; item-tag scanning at Return Bars; "**Flags risky returns and delays refunds until verified**"; "Audits flagged returns with AI-powered **Return Vision**".
- Positioning pillars: Fraud & Loss Defense / Operational Efficiency / Shopper Satisfaction. (Numeric claims are marketing figures — not carried into the final document.)

### ReturnGO (evidence A — product site)

- Self-positioning: "the world's leading **returns management platform**, helping companies turn a profit while tackling waste"; "The First Open Post-Purchase Platform".
- Modules: Returns, **Warranty**, Exchanges, **Return Guard** (return coverage sold to shoppers), Tracking, Shipping ("forward and return shipping labels from all the top carriers, including multi-carrier options").
- Merchant-side automation: "**automate post-purchase workflows and tailor your return policy to your needs, no matter how complex**" (Workflows); Insights; Automation; API pages.
- Integration spine: "integrates with any eCommerce stack, including **3PL, ERP, helpdesks, loyalty programs** and more"; "Any carrier / Any platform / Any country"; "growing network of warehouses and drop-off points"; ecosystem for Enterprises / Innovators / **Logistics Partners** (carriers, logistics and warehouse services via API).
- Merchant outcomes framing: retained revenue, revenue per return, logistics costs saved, reduced carbon footprint. Exchanges "directly in store" with Shop Now incentives. SOC 2. White-label OEM solution.
- Customer-side quote names the role: "Returns Manager, CurrentBody" — returns manager as the operator persona.

### ZigZag Global (evidence A — product site + RMS page)

- Composition: Returns Portal (shopper side) + global **carrier network** ("3,000 carrier lanes, 170 countries", customs clearance, routing) + **Carrier Claims** ("automated recovery of lost, delayed and damaged parcels") + **German Returns Hub** ("Validation, Grading, Consolidation and Routing for Returns"; defect items removed) + **RMS** + Reporting Hub + White Label (for "Parcel Carriers, Postal Operators, 3PL's").
- **RMS page — warehouse-side returns processing** (for "a retailer's warehouse as well as for any 3PL partner"):
  - "Warehouse teams receive comprehensive customer data, product information, and carrier details **before items even arrive**" (integration between RMS and Returns Portal; "Returned Merchandise Authorisation").
  - Benefits: know when/where returns will arrive; know what's inside each package and potential condition; "Identify potentially **fraudulent** returns before they impact your bottom line"; organize warehouse operations for faster processing.
  - Key features: **Search & Find** (by tracking number, order reference, return ID); **Identify & Confirm** (barcode scans, few-clicks processing); **Grade & Assign** ("visual product confirmation and **customisable grading levels**"); **Manage & Labels** ("manifests at any level — from individual boxes to entire pallets — with automatically generated labels in PDF or direct to Zebra printers").
  - "**Over-labelling and Unintended Returns Management**" — processing returns with over-labelling; managing orders that were not successfully delivered.
  - Scale/config: "Retailer data, **consolidation mapping, receiving warehouse settings, destination warehouse settings**, and Return Orders are all managed within the Returns Portal"; carrier labels via "External Carrier Service".
  - Case studies: Lands' End (international returns, wear-and-damage detection), DHL (RMS across its warehouse network — 3PL deployment).

## Cross-product Comparison

| Dimension | Loop | AfterShip | Happy Returns | ReturnGO | ZigZag | Evidence |
|---|---|---|---|---|---|---|
| Identified, order-anchored return records (RMA) | yes (returns admin) | yes (rma_number, external order id) | yes (portal requests processed) | yes | yes (RMA/RMS) | B |
| Merchant-side queue with review of exceptions | Needs Review queue | auto_* flags + exceptions[] + flagged | flagged risky returns | workflows route scenarios | fraud identification pre-refund | B |
| Policy/rules engine above base policy | Workflows | rule/zone objects on methods | risk rules gate refunds | Workflows ("no matter how complex") | policy config in portal | B |
| Automated approval/processing at scale | Background Agents, notifications | auto_approved/auto_refunded/auto_received | auto for verified items | workflow automation | automated workflows (RMS) | B |
| Refund execution with destination & gateway detail | Accounting category; refunds via platform | refunds[]: destination, gateway, store_credit_reference, transactions | refunds gated on verification | refund to store credit, original payment | refund to store credit | A (AfterShip) + B |
| Exchange order creation in commerce platform | Exchanges, Shop Now | exchange.order created | exchanges with verification | exchanges incl. in-store | Live Exchanges | B |
| Return-method orchestration (labels/carriers/drop-off/in-store) | Labels and Shipping (26), POS | return_method enum (8 values) | Return Bars, BORIS | multi-carrier labels, drop-off points | carrier network, Return to Store | B |
| Receiving recording + restock quantities | (implied by Accounting/Analytics) | received_quantity/restocked_quantity/removed_quantity; receivings[]; restocks[] | restocking speed, consolidated arrivals | warehouse network | RMS identify/confirm, manifests | A (AfterShip, ZigZag) + B |
| Disposition/grading beyond restock | Keep Item (no return) | removed_quantity; green_return | defect handling at network | exchange-for-other / sustainable alternatives | grading levels, defect removal, routing | B (depth varies) |
| Fraud/abuse controls | Fraud & Abuse category | flagged exception | Return Vision, risk scoring, delayed refunds | Return Guard (coverage), workflows | pre-refund fraud identification | B |
| Analytics/reporting | Analytics (11) | (reporting via API data) | efficiency metrics | Insights, outcome metrics | Reporting Hub | B |
| Integration spine (commerce, payments, carriers, 3PL/WMS, ERP, helpdesk) | 56+43 integration articles | Platforms enum, webhooks, gateway refs | partners | 3PL/ERP/helpdesk/loyalty explicit | 3PLs, carriers, postal operators | B |
| In-store/omnichannel returns | POS category | in_store method | BORIS | exchange in store | Return to Store | B |
| Returnless / keep-item postures | Keep Item | green_return | (consolidation economics imply) | sustainable alternatives | (n.o.) | B |
| Carrier claims / cost recovery | (n.o.) | cost_of_return | (n.o.) | logistics costs saved | Carrier Claims | A (ZigZag) + B (cost_of_return) |
| Multi-warehouse / consolidation settings | (n.o.) | shipping_status, dropoffs | consolidation network | warehouse network | consolidation mapping, receiving/destination warehouse settings | A (ZigZag) + B |

n.o. = not observed in fetched sources (absence is not evidence of absence).

## Canonical Abstraction

### L0 — Defining Invariant (kept deliberately small)

A Returns Management Platform is the **merchant-side system of record for the returns operation**, and its irreducible structure is:

1. **Return requests as managed records** — identified requests (RMA) anchored to a specific prior order and its line items with quantities; persisted, revisitable, worked as a queue by merchant staff.
2. **Policy-based decisioning** — each request is approved, rejected, or conditionally shaped (fees, methods, required evidence) according to the merchant's return policy and rules; decisioning may be manual or automated but is always the merchant's policy expressed as system behavior.
3. **Financial resolution execution** — the platform records and executes the money outcome: refund to the original payment method or to store credit, and (where offered) exchange/replacement creating a new order in the commerce system.
4. **Physical-return handling where required** — where the policy requires goods back, the platform records the goods' arrival (receipt) and their routing (restock into inventory or removal into another disposition).

Remove (1) → a policy document or refund tool, not returns management. Remove (2) → a payments/refund processor. Remove (3) → reverse-logistics tracking, not returns management. Remove (4) → nothing manages the "returns" (the goods) at all. Historical check: a mail-order returns desk with a paper RMA ledger, a manager approving against catalog policy, credit memos issued, and restocking of received parcels satisfies all four without any modern machinery — the definition holds for older/regional realizations (passes the historical-sample check).

### L1 — Common Mature Structure

Present in most mature sampled products; expected by the market but not definitional:

- rules/workflow automation layered above base policy (auto-approval, conditional requirements, templated scenarios)
- review/exception queues (flagged, failed-refund, failed-restock, failed-label, failed-charge) with notifications
- return-method orchestration: prepaid labels, QR/drop-off networks, in-store, pickup, customer-arranged courier
- item-level processing detail: item tags, merchant-uploaded photos, received/restocked/removed quantities
- exchange machinery: variant swap, instant exchange with payment authorization, bonus credit, shop-now incentives
- refund timing configuration (refund on approval / carrier scan / receipt / inspection) and cost-of-return accounting
- analytics: return rate, reasons, method adoption, cost, revenue retained
- integration spine: commerce platform, payment gateways, carriers/aggregators, WMS/3PL, ERP, helpdesk; APIs/webhooks
- shopper-facing status surface (the sibling portal) operated as part of the same product
- gift returns, multi-store/multi-warehouse settings

### L2 — Variant / Optional Structure

- **Reverse-logistics network pole**: branded drop-off network with in-person verification, consolidation into fewer/labeled shipments, refunds triggered at verification (Happy Returns; ZigZag hub).
- **Warehouse-RMS pole**: heavy receiving-side processing — pre-arrival visibility, barcode confirmation, customizable grading levels, box/pallet manifests, printer integration, over-labelling, undelivered-returns handling (ZigZag RMS; used by 3PLs).
- **Carrier-network pole**: international lanes, customs, carrier claims recovery (ZigZag).
- **Exchange-first pole**: engineered to convert refunds into exchanges/credit (Loop Shop Now; ReturnGO; ZigZag Live Exchanges).
- **Sustainability posture**: green/returnless returns, keep-item, return coverage sold to shoppers, carbon metrics (Loop Keep Item, AfterShip green_return, ReturnGO).
- **Warranty claims handled in the same platform** (Loop Warranties, ReturnGO Warranty).
- **Omnichannel**: BORIS / return-to-store executed via POS; in-store exchange (Loop POS, Happy Returns BORIS, ZigZag Return to Store, ReturnGO in-store).
- **White-label/OEM for carriers, postal operators, 3PLs** (ZigZag; ReturnGO).
- **AI layer**: returns-trained foundation models, queue-reviewing agents, AI fraud audits (Loop, Happy Returns) — era-typical, not definitional.
- **Adjacent suite modules**: forward shipping, tracking, order editing, post-purchase offers (suite drift).

### L3 — Vendor-specific (Research Notes only)

- Loop: Checkout+ bundle; Post-Purchase Offers funnels; Order Editing; Shopper Edit Return; Slack integration; Loop Intelligence/Assistant/Background Agents branding; Ordway billing portal.
- AfterShip: `retail_reworks` method value; Protection/Warranty/Parser sibling suite; Post-purchase MCP; "Shopify only for now" refund-transaction note; deep-link API for the returns page.
- Happy Returns: Return Bar® trademark; Return Vision; fixed integration into one drop-off network (also exposed as a method value inside AfterShip).
- ReturnGO: Return Guard; Edge portal UX; ReturnGO 2.0; SOC 2 positioning.
- ZigZag: German Returns Hub; External Carrier Service; Zebra printer output; RMS/Portal split as two sellable surfaces.

## Vendor-specific Findings

- AfterShip's API is the clearest public structural disclosure: per-stage automation flags and an item-level quantities ledger (ordered → return → refund → received → restocked → removed) are implemented as first-class fields — strong support for L0.3/L0.4, but the specific field set is product-specific.
- ZigZag uniquely (in sample) sells the warehouse-processing surface (RMS) as a distinct product aimed at 3PLs, and uniquely documents carrier-claims recovery and over-labelling/undelivered-returns handling.
- Loop uniquely documents a merchant-filed return path? — no: AfterShip's `filed_by: shopper|merchant|customer_support` is the direct evidence for agent-filed returns; Loop documents agent-side work via the queue and admin. Both support the "merchant-side creation/editing of requests" capability (B).
- Happy Returns and ZigZag both monetize physical infrastructure (drop-off network; hub), which shapes their merchant-side feature emphasis (verification, consolidation, restock speed).

## Boundary Findings

- **vs Returns & Exchange Portal (sibling, same family)**: the portal is the shopper-facing initiation/tracking surface bound to one order's return; the platform is the merchant-side operation (queue, decisioning, execution, disposition). In today's market they are usually one product with two surfaces; the seam is *who acts*: the shopper self-serves on the portal; staff/systems work the platform. Strip the shopper surface → this platform; strip the merchant operation → the portal.
- **vs Order Management System / Fulfillment**: OMS owns the forward order lifecycle (capture → fulfillment → post-purchase state). Returns platforms consume order data and create reverse movements (exchange orders, restocks) — they coordinate but do not own the forward order ledger. When an ERP/OMS suite embeds RMA machinery, the functional core is the same; the standalone Type is the specialized platform. Flagged for joint review when OMS-related leaves are processed.
- **vs WMS**: WMS executes general warehouse operations; the returns platform is returns-specific (policy, refund resolution, recovery) and may hand receiving/restock execution to the WMS/3PL. ZigZag's RMS shows the seam explicitly: it is a returns-specific processing layer, not a general WMS.
- **vs Retail POS**: counter refunds happen on the POS; the returns platform's in-store role ends at directing/handling the omnichannel return and reconciling the outcome.
- **vs Fraud Prevention Platform**: detection engines are cross-cutting; the returns platform embeds the decision (delay refund, flag, require evidence) rather than owning detection.
- **vs Store Credit / Gift Card Management**: the ledger lives downstream; the platform issues credit as a resolution destination and records a reference.
- **vs Help Desk**: agent case handling is where returns *exceptions* may spill; the platform's purpose is to resolve without a ticket.
- **"Remove what to become another Type" criteria**: remove merchant-side operation → portal; remove returns-specific policy/resolution machinery → generic customer portal or delivery-experience platform; reverse the flow direction (forward orders) → OMS/fulfillment; move the act to the counter → Retail POS.

## Uncertainties

- **Optoro and Narvar could not be fetched** (403/504 on 2026-09-07, two attempts each per rule). The enterprise disposition/recovery pole (liquidation channels, return-to-vendor, refurbishment marketplaces) is therefore **under-evidenced** in this pass. Disposition beyond restock is asserted only where directly observed (ZigZag grading/routing/defect removal; AfterShip removed_quantity; Loop Keep Item). Claims about enterprise-grade disposition breadth are kept weak/qualified.
- ReturnGO and Happy Returns evidence is product-page level rather than step-by-step help articles; their merchant flows are described generically.
- Loop's exact refund-execution mechanics (e.g., which events trigger refunds) were not fetched in detail; refund-timing flexibility is asserted from cross-product structure (AfterShip refund events) and must stay calibrated in the final document.
- Numeric marketing figures (e.g., network sizes, restock-speed percentages) are recorded here as vendor claims only and excluded from the final document.

## Final Synthesis

The Returns Management Platform is the merchant-side operating system of the reverse-commerce process. Its center is the **return request (RMA)** — an identified, order-anchored, item-level record — worked as a queue: decided under merchant policy (increasingly automatically, with humans on exceptions), resolved financially (refund / store credit / exchange order) through the commerce and payment stack, and — where goods come back — tracked inbound and routed back into inventory or another disposition. Around this core mature products add: method orchestration (labels, carriers, drop-off networks, in-store), exchange-revenue machinery, exception queues, fraud gates, analytics, and a broad integration spine. The market sells this together with the shopper-facing portal as one family; this document defines the merchant half, with the sibling document defining the shopper half.
