# Research Notes — Carrier Management

Research date: 2026-09-07
Leaf: "Carrier Management" (DIRECTORY.md §19 Energy, Utilities & Telecommunications, listed between Telecom Inventory Management and Telecom Expense Management)
Slug: carrier-management

---

## Research Goal

Determine what "Carrier Management" is as an Application Type in the telecom context: who operates it, what the core objects are, what workflows define it, how it differs from the adjacent leaves (Telecom Expense Management, Telecom Inventory Management, Supplier/Procurement Platforms, Telecom Provisioning Platform), and whether the leaf is a genuine Type or an alias/variant of TEM.

## Initial Boundary (working hypothesis before research)

- Hypothesis: in the telecom section of the directory, "carrier" means a telecommunications/network service provider (not a shipping carrier). Carrier Management = the enterprise buy-side practice/system of managing telecom carriers as vendors: selecting carriers, contracting, ordering services, tracking delivery, reconciling what carriers bill against contracts, disputing errors, holding carriers to SLAs.
- Nearest neighbors: Telecom Expense Management (invoice/expense machinery), Telecom Inventory Management (the service estate record), Supplier Management Platform (generic vendor management), Telecom Provisioning Platform (carrier-side activation machinery).
- Known ambiguity: "carrier management" could in principle also be read as carrier-to-carrier (wholesale/interconnect) partner management. Also a homonym risk with logistics "carrier management" (TMS world). Both to be resolved by market evidence.

## Research Questions

1. What is a "carrier" in this Type, and what is the managed object?
2. What objects compose the system's world model (carrier, contract, service, order, dispute, ticket)?
3. What are the defining workflows (source → contract → order → implement → reconcile → enforce)?
4. What rules and states matter (order validation, turn-up verification, dispute lifecycle, SLA accountability, renewal)?
5. How does Carrier Management relate to TEM and Telecom Inventory Management — Type, module, or seam?
6. Is this a standalone product category, a suite module, or a managed-service discipline?
7. Historical check: would older / regional / differently-positioned implementations fit the definition?
8. Resolve the wholesale/interconnect and logistics-homonym readings.

## Representative Products

Selection rationale: market representativeness (the four are prominent players in the enterprise telecom/technology management market), different product philosophies (software-led platform vs expert/managed-services-led vs hybrid; aggregator buying model), different customer tiers (mid-enterprise bundles through Fortune 100), and documented public product surfaces.

| Product | Posture | Sample pages fetched |
|---|---|---|
| Tangoe One Telecom | Large TEM/technology-lifecycle provider; software + services + advisory | tangoe.com/telecom-expense-management/ (+ root) |
| Calero (Telecom Management) | Platform + managed services; telecom/mobility/SaaS/market-data suite | calero.com/telecom-management, /telecom-auditing, /telecom-order-management (+ root) |
| Sakon (Telecom Cloud / Network360) | Platform-led system of record; ServiceNow-integrated; enterprise scale | sakon.com/, sakon.com/network-lifecycle |
| vCom (vManager) | Managed-services-led platform + wholesale Buyers' Club aggregation | vcomsolutions.com/, /products/it-procurement-and-strategic-sourcing, /products/it-operations-management |

Industry reference (not a product): AOTMP — professional body for technology/telecom expense management best practices (aotmp.com).

## Sources

All fetched 2026-09-07, all official vendor surfaces (Tier 1/Tier 2). WebFetch succeeded on first attempt for every URL; no retries needed.

- https://www.tangoe.com/telecom-expense-management/ (Tangoe One Telecom service lifecycle)
- https://www.tangoe.com/ (root: ecosystem, consulting, partners incl. carriers)
- https://www.calero.com/telecom-management
- https://www.calero.com/telecom-auditing
- https://www.calero.com/telecom-order-management
- https://www.calero.com/ (root)
- https://sakon.com/ (Telecom Cloud)
- https://www.sakon.com/network-lifecycle (Network360)
- https://www.vcomsolutions.com/
- https://www.vcomsolutions.com/products/it-procurement-and-strategic-sourcing
- https://www.vcomsolutions.com/products/it-operations-management
- https://aotmp.com/ (industry context)
- Referenced but not fetched: vcomsolutions.com/wholesale-buyers-club (Buyers' Club — evidence taken from root-page summary of it), calero.com/telecom-inventory-management, tangoe.com/telecom-expense-management/inventory-management/ (evidence for inventory machinery taken from the TEM lifecycle page instead)

Evidence layers used below: **A** = directly observed on a specific product's official pages; **B** = cross-product commonality (multiple sampled products); **C** = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### Tangoe One Telecom (A-evidence unless noted)

- Market position: self-described pioneer of TEM ("Pioneered TEM 25+ Years Ago"); AI-powered platform + services; global carriers ecosystem ("largest ecosystem of global carriers", "400+ Global Providers" — vendor claims).
- **Telecom service lifecycle explicitly enumerated: Order → Inventory → Invoice → Expense → Audit & Optimization → Pay.** Each stage documented on the TEM page:
  - **Order**: "One platform for all telecom service orders of any size and complexity. Get quotes and submit service orders... Easily initiate, approve, and track all telecom moves, adds, changes, and disconnects (MACDs)... structured procedures govern service orders... clear view of all current and past telecom orders **by vendor** in a single database. Fulfillment services to simplify order management and maintain accurate inventory."
  - **Inventory**: "Catalog global telecom contracts and all related service information in a single, centralized platform... tracking assets, pull status updates... granular view into every billed line item and **normalize costs across vendors**."
  - **Invoice**: AI invoice capture "linking invoices to their associated contracts and service usage data"; compare charges against contracts; "collect credits when SLAs aren't met"; "manages disputes, and tracks credits across vendors"; "Data Requests" for invoice exceptions.
  - **Expense**: aggregate view by vendor and line of business; thresholds/alerts; AP/GL feeds; benchmarking against market pricing.
  - **Audit & Optimization**: "handling invoice corrections, managing vendor disputes, automating service modifications"; consultants "use market price indexes to analyze overspending, manage RFPs, and negotiate your contracts" — contract negotiation framed against **carrier contracts**.
  - **Pay**: "You pay Tangoe. We pay your vendors" (bill pay across carriers).
- POTS retirement framing: "Carriers are retiring copper on their schedule, not yours" — carrier dependency as the customer's problem.
- Root page: Services span telecom/mobile/cloud; consulting includes Contract Negotiations, Rates & Savings Analysis; partners include **Carriers** as an ecosystem category.
- Audience: "From global enterprises to mid-market companies"; mid-enterprise bundles.

### Calero Telecom Management (A-evidence)

- Telecom Management = platform + services; sub-offerings: Auditing & Dispute Management, Ordering & Procurement, Inventory Management.
- **Ordering & Procurement page** (wireline ordering):
  - Full lifecycle of fixed line service ordering — "from quoting to provisioning to invoice validation".
  - Quote & Order Management in 4 steps: **Request → Evaluate → Negotiate → Track** ("Submit vendor quote requests", "Compare your quote pricing and terms", "Use benchmarking tools to negotiate better pricing", "Track your order through delivery and installation").
  - "Automatically distribute telecom orders to your vendors"; internal approval workflows "to enforce business rules".
  - Order Initiation & Validation: "all orders align with contract terms, inventory needs, and business policies **before they're sent out**"; "vendor coordination from quote submittal to provisioning oversight".
  - Real-Time Order Tracking: "Status updates are automatically synced... Once services are turned up, we verify delivery and **update inventory and billing data** — so what you're paying for always matches what's live in the field."
  - MACD Management: "prevent disconnect errors... changes are tracked and validated".
  - Benchmarking Module: "evaluate vendor quotes against real market data... validate savings during RFPs and renewals."
  - Wireline e-Bonding (telecom page): "Automate the exchange of data between your telecom systems" — automated data exchange with carrier systems.
- **Auditing & Dispute Management page**:
  - "Telecom invoices are notoriously complex—stuffed with fees, taxes, and terms that are easy to misapply".
  - "automatically reconciles every invoice against your **inventory, MACDs, and contract terms**".
  - Variance workflow: variance detected → invoice analyst evaluates/resolves or escalates → telecom auditors "manage the dispute lifecycle" → "the credit or adjustment is posted to the correct account".
  - Dispute engine: "tracks issues from initial flag to final credit... across vendors, services, and projects"; granularity "down to the USOC if needed" (USOC = carrier service-ordering code — carrier-specific service codes as tracked entities); customizable dispute workflows; reporting on "open vs. closed claims, amounts recovered vs. denied, and dispute aging to keep vendors accountable".
  - "Eliminate 'zombie' services and align every telecom asset with a cost center and contract."
- Telecom page: "Visualize Your Global Network"; "Oversee the entire lifecycle of your telecom inventory from ordering and procurement to secure decommissioning"; invoice tracking/validation/bill pay.

### Sakon (Telecom Cloud / Network360) (A-evidence)

- Platform-led: "the governed system of record for your entire telecom network — keeping inventory accurate, orders in sync".
- "One accurate view of every service, **across every carrier**. Carrier, order, and ownership data unified."
- **Unified Telecom Record (UTR)** built by unifying three data sources:
  - "Carrier data. Monthly feeds from carriers — active services, components, and circuit identifiers — ingested in their native format without modification." ("Sakon connects to your carriers and ingests their feeds directly")
  - "Customer data. Order cost allocation, site ownership, and naming conventions mapped to your enterprise structure."
  - "Order data. Every quote, order, and change tracked with full provisioning detail and lifecycle history."
- Root page: "It's impossible to optimize telecom management with scattered data and **carrier portals**. Unify it all in one place with full network visibility, **standardized carrier data**..." Solutions: Wireless Lifecycle (device lifecycle, connectivity management), Network Lifecycle (UTR, service lifecycle management, MACD integration), AP Automation (invoice processing/payment), Telecom Connect (ServiceNow/Salesforce/Teams).
- **Order Management**: "All of your Network MACD activity in a single platform"; "Centralized MACD control"; "Real-time inventory updates. The record changes as orders progress"; "Validated before it is sent. Orders are checked against current inventory before submission — catching errors that would otherwise surface as provisioning failures."
- ServiceNow integration: certified scoped app; telecom CIs kept current in CMDB; incidents "worked against real service data".
- Outage/SLA framing: "Impacted circuits, the sites and teams that depend on them, and **the carrier accountable for the SLA** are all one click away"; "Know which carrier holds the SLA — and hold them to it, with the record to back it."
- Case-study evidence of scale: "1,500+ network services across 20+ carriers" (Fortune 100 financial institution); "1,000+ location network"; "100% Carrier contract visibility".
- Comparison table vs spreadsheets/"Generic TEM": Multi-carrier integration claim ("800+ All major carriers" — vendor claim), "Billing reconciliation vs Carrier — Built-in".
- Self-positioning against TEM: "We tried managing inventory through our TEM provider, but it didn't deliver the compliance we needed" (customer quote) — platform pole distinct from service-led TEM.

### vCom (vManager platform + managed services) (A-evidence)

- Positioning: IT/network/mobility lifecycle "from source to pay" — "Manage all technologies, carriers, and locations".
- **Planning and Procurement**:
  - Solution Design: "comprehensive audit and full RFP management".
  - Sourcing: "live marketplace, where organizations and partners can evaluate vendors, compare pricing, and initiate orders... approval workflows, custom pricing catalogs, and vendor availability finders"; "Compare and order services across multiple vendors through the platform's vendor-agnostic marketplace".
  - Contract Management: specialists negotiate; "All contract details — from service orders and exhibits to network diagrams — are securely stored and easily accessible within the platform."
  - Project types include "Wireless Migrations Between Carriers (500+ Lines)" and "Vendor Migrations" (carrier switching as a managed project).
- **Operations Management**:
  - Order Management: "Track and manage every order from any vendor, from start to finish... milestone updates, proactive notifications... We handle everything from escalations and disputes to MACDs, test and turn-up (TTU), and beyond." Tools: "MACD Order Portal", "MACD Project Management", "Order Reporting".
  - Asset Management: "Track **carrier services**, mobile devices and plans, cloud and SaaS licenses, hardware... auto reconciliation... we capture everything, from **circuit IDs and call paths** to warranties" — carrier services with circuit IDs as tracked assets; "Asset-to-Invoice Linking".
  - Service & Support: "Vendor Ticketing Portal, Vendor Escalation, Troubleshooting, and Resolution... Proactive Managed Network Services (MNS) and **Carrier Performance Management (CPM)**"; SLA FAQ: "We also ensure that **vendors are held accountable for their SLAs** during disruptions or outages."
- **Expense Management**: single portal for invoices across "technologies, vendors, and locations"; GL coding/cost centers; managed pay.
- **Buyers' Club** (wholesale aggregation; brand ancestry QuantumShift): "pre-negotiated discounts and enterprise-level pricing from a 100% vendor-agnostic provider"; "Track a single invoice while accessing dispute management, billing error protection, and provider redundancy"; "nomenclature normalization"; "detailed cost breakdowns by asset, **carrier**, service, and location."
- AOTMP TEM/MMS certifications listed for multiple specialists; one specialist's project type literally named "Vendor Management".

### AOTMP (industry context) (A-evidence, not a product)

- Professional body for "technology management best practices" (22+ years); TEM Performance Program; Efficiency First Framework; certifications that practitioners of this discipline hold (sampled products' staff carry AOTMP TEM/MMS certifications). Confirms that carrier/vendor management lives inside an established industry discipline (TEM / technology business management) with its own vocabulary and standards.

---

## Cross-product Comparison

| Structure / capability | Tangoe | Calero | Sakon | vCom | Layer |
|---|---|---|---|---|---|
| Carriers/providers as managed vendor records (orders "by vendor", vendor accountability, carrier data) | ✓ | ✓ | ✓ | ✓ | B — universal |
| Contract & rate terms recorded and used as enforcement baseline | ✓ (catalog contracts; charges vs contracts) | ✓ (orders aligned to contract terms; disputes enforce contract pricing) | ✓ (carrier contract visibility; SLA per carrier) | ✓ (contract details stored; negotiation) | B — universal |
| Purchased connectivity services bound to carrier + contract (service estate with carrier identifiers: circuits, lines, services) | ✓ | ✓ | ✓ (circuit identifiers from carrier feeds) | ✓ (carrier services, circuit IDs) | B — universal |
| Service orders & MACD (moves/adds/changes/disconnects) transacted with carriers, tracked to turn-up | ✓ | ✓ | ✓ | ✓ | B — universal |
| Order validation against contract/inventory/policy before submission | ✓ ("structured procedures govern") | ✓ (explicit) | ✓ (explicit) | ✓ (approval workflows) | B — universal |
| Quote/RFP-based sourcing & vendor selection (quote compare, benchmark, negotiate) | ✓ (RFP advisory; benchmark) | ✓ (Request→Evaluate→Negotiate→Track; benchmarking module) | partial (quotes in UTR; order data) | ✓ (RFP management, marketplace) | B — strong |
| Turn-up verification → inventory/billing records updated to match field reality | ✓ (fulfillment) | ✓ (explicit) | ✓ (record updates as orders close) | ✓ (TTU; asset-to-invoice linking) | B — universal |
| Multi-carrier data normalization (feeds/portal/e-bonding ingestion, naming normalization) | ✓ (ecosystem integrations; line-item normalization) | ✓ (wireline e-Bonding) | ✓ (monthly carrier feeds, native format) | ✓ (Buyers' Club nomenclature normalization) | B — universal |
| Invoice reconciliation vs contract+inventory+orders → variance → dispute → credit | ✓ (explicit stage) | ✓ (explicit, detailed) | ✓ ("Billing reconciliation vs Carrier") | ✓ (auto reconciliation; disputes) | B — universal (machinery shared with TEM) |
| Carrier/vendor SLA accountability (credits when SLAs missed; hold carrier to SLA; CPM) | ✓ | ✓ (vendor accountability) | ✓ (explicit) | ✓ (named CPM) | B — universal |
| Trouble tickets / escalations with vendors | — (not surfaced on fetched pages) | — (dispute tickets only) | ✓ (incidents in ServiceNow) | ✓ (vendor ticketing portal, escalations) | B — partial in sample; common |
| Market benchmarking of quotes/rates | ✓ | ✓ | — (not surfaced) | ✓ (marketplace pricing; wholesale rates) | B — common |
| Contract renewal/re-negotiation cycle | ✓ (advisory) | ✓ ("RFPs and renewals") | — (renewals not surfaced) | ✓ (contract management) | B — common |
| Spend reporting by carrier/vendor; GL/cost-center allocation | ✓ | ✓ | ✓ (cost allocation in customer data) | ✓ | B — universal (expense-side) |
| Bill pay / payment execution | ✓ (Tangoe Pay) | ✓ (bill payments) | ✓ (AP Automation) | ✓ (managed pay) | B — common (expense-side) |
| ITSM (ServiceNow) integration | ✓ (claimed) | ✓ (e-bonding & integrations) | ✓ (certified scoped app) | — (not surfaced on fetched pages) | B — common |
| Delivery posture | services+software hybrid | services+platform hybrid | platform/software-led | managed-services-led | L2 variant |
| Aggregated wholesale buying (single bill across carriers) | — | — | — | ✓ (Buyers' Club) | L2 variant (product-specific posture) |
| Wireless/device lifecycle bundled | ✓ (MMS) | ✓ (mobility) | ✓ (wireless lifecycle) | ✓ (mobile lifecycle) | L2 variant (adjacent Type machinery) |
| AI layer (invoice capture, assistants) | ✓ | ✓ (Calero Assistant) | ✓ (Telecom AI) | — (not surfaced) | L2 variant (era-common) |

Key reading: every sampled product implements the same vendor-facing spine — **carrier record + contract terms + service estate + order/MACD loop + reconciliation/enforcement loop** — while differing on posture (software vs services), buying model, and how far into expense/payment/ITSM machinery they reach.

## Canonical Model (abstraction results)

### L0 — Defining Invariant (minimal)

An enterprise-side system that manages **connectivity service providers ("carriers") as vendors** across the contracted service lifecycle. Four properties; remove any one and the Type stops being recognizable:

1. **Carrier as managed vendor record** — the counterparties from whom the organization buys connectivity services are held as governed records (the "who we buy from" register), with orders, contracts, tickets, and charges attributable to each.
2. **Contracted terms as the governing baseline** — the agreed services, pricing/rates, and service-level commitments with each carrier are recorded and serve as the baseline against which orders are made and carrier behavior is enforced.
3. **Purchased connectivity services bound to carrier and contract** — the recurring services bought from each carrier (circuits, lines, voice/data/internet services, wireless plans) are held as identified service records tied to the providing carrier, its contract, and (typically) location/cost allocation.
4. **Service-order transactions with the carrier** — new service requests, quotes, orders, and changes/disconnects (MACD) are initiated, validated, and tracked through the carrier's provisioning to delivery/turn-up, with the outcome recorded back into the service estate.

The conceptual formula: **select → contract → order → implement → enforce, with the carrier as counterparty.**

Not in L0 (deliberately): invoice processing/payment machinery, GL allocation, carrier-feed automation, e-bonding, benchmarking, ServiceNow integration, AI, wireless device lifecycle, wholesale aggregation. (See L1/L2.)

### L1 — Common Mature Structure (standard capabilities in mature products)

- Multi-carrier data normalization: ingestion of carrier billing/service data (feeds, portals, e-bonding) and normalization of carrier-specific naming/codes into one consistent estate view.
- Order validation and governance: orders checked against contract terms, inventory, and business policy before submission; approval workflows.
- Real-time order status tracking with milestone/provisioning detail; turn-up verification that updates inventory and billing records so "what you pay for matches what is live".
- Invoice-to-contract/inventory reconciliation: charges validated against contracts, orders/MACD history, and the service estate; variance detection → dispute lifecycle (flag → dispute ticket → resolution/escalation → credit or adjustment posted) with recovery reporting and dispute aging.
- Carrier SLA accountability: service-level commitments tracked; credits pursued when missed; carrier performance made visible (outage blast radius mapped to the accountable carrier).
- Sourcing support: quote requests, quote comparison, market benchmarking of rates, RFP/renewal support, contract negotiation (often expert-delivered).
- Vendor ticketing/escalation: trouble reports and escalations with carriers, tracked against the service record.
- Spend reporting by carrier/vendor; cost allocation hooks (GL/cost center).
- ITSM/ERP integration surfaces (ServiceNow/CMDB being the most cited).

### L2 — Variant / Optional Structure

- **Delivery posture**: software-led platform (self-serve system of record) ↔ expert/managed-services-led (the vendor's staff run orders, disputes, negotiations) ↔ hybrid; the same core structure is delivered by people, software, or both.
- **Buying model**: direct with each carrier vs aggregated/wholesale (one consolidated bill and pre-negotiated rates across carriers via the provider's buying power).
- **Estate scope**: wireline-only vs wireline + wireless vs full technology estate (adding SaaS/cloud) — broader scopes fold adjacent Types' machinery in.
- **Segment/scale**: mid-enterprise bundles vs global multi-carrier, multi-country estates.
- **Program variants**: carrier retirement/migration programs (e.g., copper/POTS replacement) as managed initiatives.
- **Integration-first posture** (deep ServiceNow/ITSM embedding) vs platform-portal posture.
- **Advisory/consulting layer** (market intelligence, negotiation services) bundled or not.
- **AI layer** (invoice capture, assistants) — era-common, not definitional.

### L3 — Vendor-specific (research notes only; not for the final document)

- Tangoe: "Tangoe One Telecom" naming; lifecycle stage labels Order/Inventory/Invoice/Expense/Audit & Optimization/Pay; "Data Requests" invoice-exception mechanism; Tangoe Pay; claims (400+ providers, 370K invoices/month, 70+ patents, $15B spend under management, 15–30% overspend claim).
- Calero: Auditing & Dispute Management / Ordering & Procurement / Inventory Management module naming; dispute granularity "down to the USOC"; Benchmarking Module; wireline e-Bonding naming; Calero Assistant; 4-step quote-and-order flow naming (Request/Evaluate/Negotiate/Track).
- Sakon: Network360 product name; Unified Telecom Record (UTR) branding; "800+" multi-carrier integration claim; 30-minute/30-day/90-day audit-readiness claims; 24× faster audit response, 85%/90%/75% result claims; certified ServiceNow scoped app; 30-Day Dual Improvement Guarantee.
- vCom: vManager platform name; Buyers' Club / QuantumShift wholesale aggregation; Carrier Performance Management (CPM) and Managed Network Services (MNS) names; MACD Order Portal; TTU (test and turn-up) abbreviation; in-house three-tier NOC; asset-to-invoice linking phrasing.
- AOTMP: Efficiency First® Framework, TEM Performance Program, certifications.

## Vendor-specific Findings

See L3. The only vendor-specific structure that flirts with Type-level significance is the **aggregated wholesale buying model** (vCom Buyers' Club): the platform provider becomes a reseller/aggregator between the enterprise and its carriers (single invoice, pre-negotiated rates). This changes the commercial relationship but preserves the L0 structure (carriers still recorded, contracted, ordered against, enforced). Classified as a business-model variant, not a defining structure.

## Boundary Findings

1. **vs Telecom Expense Management (sibling leaf)** — the most important seam. TEM centers on the invoice/expense/payment loop across technology spend (invoice capture, audit, GL allocation, payment) regardless of vendor; Carrier Management centers on the carrier relationship (contracts, orders, enforcement with the carrier as counterparty). Overlap: the reconciliation/dispute machinery is shared — in sampled products it lives at the junction (Calero puts disputes under Telecom Management; Tangoe puts disputes under the Invoice stage; Sakon calls it "billing reconciliation vs carrier"). Judged seam: remove the carrier/order/contract machinery and only invoice/expense machinery remains → TEM; remove the invoice/payment/GL machinery and only carrier/order/contract machinery remains → still recognizably Carrier Management. The dispute loop is therefore standard (L1) but not definitional. Because real products bundle both, the market often presents them as one "TEM/telecom lifecycle" suite; the directory split is analytic, and the two leaves should cross-reference.
2. **vs Telecom Inventory Management (sibling leaf)** — inventory centers on the estate record itself (what services/circuits exist, where, lifecycle, discovery). Carrier Management binds that estate to the providing carrier + contract and transacts changes with the carrier. In sampled products the two are one data spine (the "unified record" is simultaneously inventory and carrier relationship record). Seam: strip carrier/contract/order attribution → pure inventory; keep it → Carrier Management.
3. **vs Supplier Management Platform / Procurement & Sourcing** — generic vendor management lacks connectivity-specific semantics: circuit/service identifiers, MACD transactions, carrier service feeds, service-level enforcement, turn-up verification. Remove connectivity semantics → generic SRM/procurement.
4. **vs Telecom Provisioning Platform (carrier-side OSS)** — provisioning platforms are the carrier's own service-activation machinery (the seller's operations); Carrier Management is the buyer-side coordination of that provisioning. Different operator and different object of work.
5. **vs Managed Mobility Services** — MMS is device-centric wireless lifecycle (devices, UEM, help desk); Carrier Management is counterparty-centric (plans, services, contracts, orders with the mobile carrier). Wireless services appear in Carrier Management as purchased services; the device fleet is MMS territory. Overlap on wireless ordering/plan changes.
6. **Homonym: logistics "carrier management"** — in transportation/freight, "carrier" means motor/parcel carrier and carrier management is TMS/freight-brokerage machinery. Same word, different Type and different directory section. No evidence of overlap in sampled products.
7. **Second-referent risk: wholesale/interconnect partner management** — in the carrier-to-carrier (wholesale) world, managing counterpart carriers (interconnect agreements, routing, settlement) is a real practice, but it is normally called interconnect/partner management, none of the sampled enterprise-side products cover it, and the directory's neighboring leaves (Telecom Inventory Management, Telecom Expense Management) are enterprise-buy-side. Documented as an ambiguity for taxonomy reviewers; the enterprise buy-side reading is the one supported by market evidence.

## §24-style Historical / Market-Sample Check

Would older, regional, or differently-positioned implementations fit the L0?

- The discipline predates the cloud era: the sampled market leader claims 25+ years of TEM history and the industry body claims 22+ years of best-practice work; early TEM/telecom management was practiced by enterprise telecom departments and regional managed-service firms with spreadsheets, PDF/paper invoices, and circuit inventory lists. Their work was exactly the L0 loop: know the carriers, record the contracted terms, track the circuits/lines bought from each, order changes, and challenge bills that didn't match terms.
- Modern machinery (carrier feeds ingestion, e-bonding, marketplaces, ServiceNow apps, AI) is L1/L2 implementation, not definition. Removing all of it leaves the L0 loop intact.
- Platform-native/regional variants (agency/consultancy models that deliver the same functions manually) also satisfy L0 — the structure is about what is managed, not who executes it.

Conclusion: L0 does not over-fit the current SaaS/managed-services implementation.

## Uncertainties

1. No vendor publishes operational user guides (help-center depth) on public web; evidence is product/service marketing + solution pages (Tier 1–2). Precise operational facts (exact order status labels, dispute filing windows, workflow parameters, numeric carrier counts) are vendor claims or unstated — the final document deliberately avoids precise numbers.
2. Whether standalone pure-play "carrier management" products exist without the TEM/inventory machinery could not be verified; the sampled market presents carrier management as a spine inside broader telecom/technology lifecycle platforms and managed services. The final document therefore describes the Type analytically (the carrier-facing spine) while acknowledging that products usually bundle it with expense/inventory machinery.
3. Wholesale/interconnect reading of the leaf name remains a taxonomy-level ambiguity (see Boundary Findings #7).
4. Trouble-ticket/escalation machinery was only partially evidenced (2 of 4 products on fetched pages) — treated as common but with a note.
5. Wireless-side evidence is thinner than wireline (sampled pages are wireline-heavy); wireless services/plans as part of the estate is evidenced, but wireless-specific carrier mechanics were not deeply researched.

## Final Synthesis

Carrier Management is the enterprise buy-side Application Type whose defining core is the **governed relationship between an organization and the connectivity providers it buys services from**: carriers held as vendor records, contracted terms as the enforcement baseline, purchased services bound to carrier + contract as the managed estate, and service-order/MACD transactions tracked through carrier provisioning to turn-up. Around that core, mature products standardize carrier data across vendors, validate orders before submission, reconcile carrier billing against contracts and the estate through a dispute→credit loop, hold carriers to service levels, support sourcing/benchmarking/negotiation, and feed spend and inventory views downstream. Delivery ranges from software-led systems of record to expert-run managed services, and products commonly bundle the type with telecom expense and inventory machinery — but the carrier relationship (contract → order → enforce) is what makes the Type what it is: remove it and the remainder is expense management or inventory management; keep it and the product is recognizably Carrier Management regardless of era, region, or delivery model.
