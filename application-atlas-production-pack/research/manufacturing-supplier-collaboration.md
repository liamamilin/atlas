# Research Notes — Manufacturing Supplier Collaboration

Research date: 2026-09-09

## Research Goal

Understand the application Type the DIRECTORY calls **Manufacturing Supplier Collaboration** (§16 Engineering, Manufacturing & Industrial): what the software actually is, what objects the two companies (manufacturer/buyer and supplier) work on together, what the collaboration loop looks like end to end, which roles on both sides use it, which states and rules govern it, and where its boundaries run against the heavily adjacent processed siblings (Supplier Portal, Supplier Management Platform, Purchase Order Management, Procure-to-pay Platform, Supply Chain Planning/Demand Planning, MES, EDI Platform, Supplier Quality Management).

## Initial Boundary

Temporary hypothesis before research:

- **What it is**: the buyer-side (and supplier-facing) system through which a manufacturer and its production-material suppliers exchange a shared demand signal (orders / release schedules / forecasts / call-offs), the supplier's confirmations/commitments/exceptions, and the fulfillment trail (ship notices, goods receipts) — so both parties see the same picture from plan to arrival.
- **Users**: buyer-side buyer/planner, expeditor, inbound logistics; supplier-side customer service / order desk, production planner, shipping clerk.
- **Nearest neighbors**: Supplier Portal (§10, processed — pre-hung joint-review flag on this leaf), Supplier Management Platform, Purchase Order Management, P2P, EDI Platform, Supply Chain Planning/Demand Planning, MES, Supplier Quality Management.
- **Likely confusion**: this leaf is in §16 (manufacturing), but the market phrase "supplier collaboration" is also used by procurement suites (§10) for their supplier-facing surfaces. The center of gravity must decide the Type.
- **Unknowns**: is the shipment/receipt leg definitional or only common? Is the forecast/commit leg definitional or only common? How do ERP-embedded realizations (D365 "vendor collaboration") relate to dedicated network products (SupplyOn, e2open, SAP SNC class)?

## Research Questions

1. What is the central collaboration object (PO? release schedule? forecast? all three)? Who creates it and who responds?
2. What exactly does the supplier's response loop look like — acknowledge, confirm, commit, exception? At what grain (header, line, date, quantity)?
3. How does the loop close on the physical side (ASN/ship notice, goods receipt, delivery status)? Is invoice collaboration inside the Type?
4. Which ordering models appear (discrete PO, blanket, scheduling agreement, JIT/JIS, Kanban, VMI/consignment) and are any definitional?
5. What interfaces exist on each side (buyer workspace, supplier worklist, schedule views, shipment forms)?
6. Which rules matter: per-supplier activation, versioning of changed orders, who may change what (prices?), non-response handling?
7. How does the Type realize differently across poles: industry network vs multi-enterprise SaaS vs ERP-embedded module vs SMB portal?
8. Boundaries: vs supplier-portal (discharge the pre-hung flag), vs supplier-management, vs POM/P2P, vs EDI, vs planning, vs MES, vs supplier quality.
9. Historical check: would pre-EDI / paper-era release management (schedule + confirmation + packing slip + receiving reconciliation) still satisfy the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer tiers, and documentation reachability:

| Product | Pole | Philosophy | Customer tier | Evidence reached |
|---|---|---|---|---|
| SupplyOn (Supply Chain Collaboration; AirSupply) | industry/multi-buyer network (automotive, aerospace, electronics) | shared industry platform; standardized cross-company processes; suppliers log in to one network | large OEMs + their supplier base | Tier-2 solution pages + Tier-1 Help Center SCC category (article **index**; article bodies login-gated) |
| e2open (Supply application suite: PO Collaboration, Supply Forecast Collaboration, Supply Inventory Collaboration) | multi-enterprise SaaS network for direct materials | forecast/commit orchestration across all supply tiers attached to a large partner network | global manufacturers (EMS, automotive, high tech) | Tier-2 product pages (suite + 2 application pages) + brief case |
| Microsoft Dynamics 365 Supply Chain Management — Vendor collaboration | ERP-embedded, single-buyer realization | supplier-facing collaboration surface in front of the buyer's PO/consignment records; explicitly for vendors **without** EDI | enterprise ERP customers | Tier-1 official docs (Microsoft Learn, fetched 2026-09-09) |
| Aligni — Supplier Relations / vendor portal | SMB/manufacturing MRP with embedded vendor collaboration | lightweight portal replacing email; suppliers update quotes/promise dates in-system | small/mid manufacturers | Tier-2 feature page |

Attempts that failed and were abandoned per network rules (2 failures each): Kinaxis supplier-collaboration paths (404 ×2), e2open /products/ and /solutions/ (404 ×2; root and /supply/ succeeded), SAP Ariba SCC path (404), Aligni guessed feature path (404; root worked). SAP help portal is a JS shell consistent with prior passes. SAP SNC/Ariba SCC and Kinaxis therefore serve as **market anchors only** (named in vendor-independent sources fetched here, e.g. e2open/SupplyOn pages referencing the collaboration category), with no operational claims drawn.

## Sources

- SupplyOn — Supply Chain Collaboration solution page: https://www.supplyon.com/en/solutions/supply-chain-collaboration/ (fetched 2026-09-09)
- SupplyOn — AirSupply solution page: https://www.supplyon.com/en/solutions/airsupply/ (fetched 2026-09-09)
- SupplyOn Help Center — Supply Chain Collaboration category (article index): https://supportcenter.supplyon.com/en/hc/category/supply-chain-collaboration (fetched 2026-09-09; article bodies login-gated)
- SupplyOn corporate site: https://www.supplyon.com/en/ (fetched 2026-09-09)
- e2open — Supply application suite: https://www.e2open.com/supply/ (fetched 2026-09-09)
- e2open — Purchase Order Collaboration: https://www.e2open.com/supply/purchase-order-collaboration/ (fetched 2026-09-09)
- e2open — Supply Forecast Collaboration: https://www.e2open.com/supply/supply-forecast-collaboration/ (fetched 2026-09-09)
- e2open — corporate home (Supply suite positioning, Jabil testimonial): https://e2open.com/ (fetched 2026-09-09)
- Microsoft Learn — Dynamics 365 SCM "Vendor collaboration with external vendors": https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors (fetched 2026-09-09)
- Aligni — Supplier Relationships: https://www.aligni.com/product/supplier-relationships/ ; Aligni home: https://www.aligni.com/ (fetched 2026-09-09)

Source-access limitations: SupplyOn help article **bodies** require login (index observed only — interface/artifact inventory usable, procedural detail not); SAP and Kinaxis unreachable (market anchors only, no claims); e2open/Aligni pages are Tier-2 marketing-product pages (operational mechanics described at process level only); no precise vendor figures, thresholds, or state vocabularies asserted in the final document beyond what Tier-1 text supports.

---

## Product A — SupplyOn (Supply Chain Collaboration / AirSupply)

### Key observations (Layer A unless noted)

- The vendor's own definition (solution page): "Supply Chain Collaboration is the digital coordination of planning, ordering, delivery, and logistics processes between customers and suppliers. It enables all parties to work from the same information."
- Ordering models on one platform: "classic purchase orders as well as JIT, JIS, VMI, and Kanban processes"; "Manage every ordering process."
- Collaborative supply planning: "Exchange demand, capacities, delivery quantities, and delivery dates with suppliers through a shared and transparent planning process"; order confirmations through shared planning processes.
- Monitoring: "Track purchase orders, confirmations, shipments, goods receipts, and delivery status across all parties in real time."
- Help Center SCC category (Tier-1 index) — the documented artifact inventory of the supplier-facing surface:
  - About: "What is Supply Chain Collaboration?", "Process overview"
  - Supplier how-tos: Dashboard, **Orders**, **Delivery Schedules**, **Kanban**, **JIT**, **JIS**, **Schedule Response**, **Forecast Collaboration**, **Vendor Managed Inventory (VMI)** + VMI supplier settings, packing material overview/details/instructions, material master data, **Goods receipt**, **Due deliveries overview**, **Demand reminder**, **Stock movements**, **FPA (Forwarder Pickup Advice) overview/details**, **ASN overview/details** with tabs (select positions, additional data, transport references, packing data, complete), create/delete/upload ASN, automatic FPA/ASN number assignment, pack-to-stock, XML/CSV/XLSX upload
  - Customer how-tos: site settings, material/packing master data, VMI, Forecast Collaboration, ASN profiles
  - Admin: email notifications & alerts, upload/download format, control points
  - Separate help categories exist for **Procurement** (orders approval/processing), **Capacity Management**, **Performance Management**, **Invoicing**, **M2M / EDI connection** — i.e., the vendor itself separates the collaboration loop from master data, capacity, performance, invoicing, and transport machinery.
- The site separates "How-tos for suppliers" and "How-tos for customers" — **two-sided** documentation of the same process.
- AirSupply (aerospace flavor, from the BoostAeroSpace initiative of Airbus/Dassault/Safran/Thales): "shared transactional data foundation for collaborative aerospace supply chain processes across **forecast, purchase orders, despatch advice, goods receipt, inventory, quality collaboration, and invoicing**"; features: shared forecast collaboration, PO status tracking, "interactive adjustment of delivery quantity and date", ASN, incoming-goods optimization, VMI, on-time delivery processes, concession handling, complaint management, multi-tier data flow.
- **Portal boundary, vendor-documented**: AirSupply FAQ — "What makes AirSupply different from a basic supplier portal? … not just document exchange. It supports collaborative forecast handling, purchase order status, delivery coordination, incoming-goods optimization, inventory collaboration, quality processes, and invoicing on one shared platform."
- Positioning claims (marketing layer, treat as B/C): "Increase OTIF by up to 15% through proactive supplier collaboration"; 140,000+ connected suppliers; AI-based analytics for bottleneck early detection.

### Boundary-relevant notes

- EDI appears as a **connection method** (M2M/EDI help category), not as the collaboration itself.
- Quality collaboration exists as a connected extension ("Can SupplyOn integrate related supply chain processes? Yes. … quality documents, certificates, and parts quality processes") — separate Quality Management product family.

## Product B — e2open (Supply application suite)

### Key observations (Layer A at page level; product page = Tier-2)

- Suite frame: "Optimal supply through complete visibility and collaboration with all tiers of suppliers and outsourced production partners"; applications: Purchase Order Collaboration, Supply Forecast Collaboration, Supply Inventory Collaboration, Buy-Sell Management, Product Cost Management, Manufacturing Collaboration, Recall Management, Risk & Quality Management, PLM, Supply Network Discovery, Supply Risk Assessment.
- **Purchase Order Collaboration** page: "end-to-end, real-time visibility and management capabilities across POs, shipments, receipts, and invoices"; "manage discrete orders, blanket orders, blanket releases, scheduling agreements, shipments, receipts, and invoices"; "streamline your materials requirements planning and purchase order changes, including **expedites, de-expedites, and cancellations**"; "create and oversee governance for the entire PO process — including shipping instructions — for all suppliers"; "quickly identify critical gaps, such as **mismatches between order and shipment quantities**".
- **Supply Forecast Collaboration** page: "A time-series view displays component forecasts, upsides, and **commits** for suppliers and contract manufacturers"; "**Dynamic alerts for demand-supply mismatches between buyers and suppliers**"; "Automated issue identification … collaborative workflows across multiple stakeholders"; "A single source of truth for **forecasted demand and supplier commits**"; pain-point framing: "suppliers often hedge demand forecasts, incurring extra financial liability due to elevated stock".
- Brief case (automaker): "sharing accurate forecasts with suppliers and **gaining their commitment** to delivering on these forecasts. This commitment-based approach…".
- Jabil testimonial (EMS): "standardize and digitalize our **forecast communication process for all suppliers** … near real time visibility into **forecast status** with our suppliers".
- Multi-tier is a defining positioning element ("across all tiers", "multi-tier supply network"), realized through the e2net partner network and supplier onboarding ("If current partners are not already in the network, onboarding is fast and easy").

### Boundary-relevant notes

- The suite splits the loop into named applications (PO collaboration vs forecast collaboration vs inventory collaboration) — strong evidence that the *loop* is the Type, with content types as modules.
- Invoices appear inside PO Collaboration, but invoicing is not a separate suite emphasis here — hold invoice collaboration as optional.

## Product C — Microsoft Dynamics 365 Supply Chain Management, Vendor collaboration

### Key observations (Layer A — Tier-1 official docs)

- Scope sentence: "The **Vendor collaboration** module is targeted at vendors who don't have electronic data interchange (EDI) integration … It lets vendors work with purchase orders (POs), invoices, consignment inventory information, and requests for quotation (RFQs), and also lets them access parts of their vendor master data." → EDI is the alternative channel, not a prerequisite; the module is the application layer for the non-EDI supplier.
- **Per-supplier activation**: "On the **Vendors** page … set the **Collaboration activation** field": *Active (PO is auto-confirmed)* or *Active (PO is not auto-confirmed)*; a batch job processes confirmations; price visibility is a separate per-vendor toggle ("Purchase order prices/amount").
- **PO response loop** (buyer sends approved PO → status *In external review* → vendor responds):
  - vendor responses: accept / reject / **accept with changes**;
  - line-level changes the vendor may make: change dates or quantities, **split lines for different receipt dates or quantities** (→ line status *Split into schedule*), **substitute an item** (text-entered), reject individual lines;
  - "The vendor **can't change price information and charges**. However, the vendor can suggest these changes by using notes.";
  - responses processed via "Process PO update"; some changes auto-consumable (dates, quantities), others manual (schedule splits);
  - **PO versioning**: "To change a PO that a vendor has already responded to, you must send the vendor a new version of the PO. … The **Purchase order vendor confirmation history** page lets you and your vendors track the history of each order. The previously confirmed version … remains in the list of confirmed POs until the new PO has been confirmed.";
  - cancellation is itself sent to the vendor for confirm/reject;
  - attachments classified *External* become visible to the vendor;
  - off-system fallback: "Vendors don't have to confirm a PO by using the vendor collaboration interface. They can also send an email … You can then manually confirm the order" (with a warning that there is no vendor response recorded).
- **Buyer-side worklists**: "Purchase order preparation" workspace with lists *In external review requires action* / *In external review awaiting vendor response*.
- **Consignment inventory** collaboration: vendor sees "Purchase orders consuming consignment inventory", "Products received from consignment inventory" (ownership transfer with product receipt posted — vendor uses it to invoice), "On-hand consignment inventory" at the customer's warehouse.
- RFQ collaboration (alternates, attachments, amendments, bid returns) documented in the same module.

### Boundary-relevant notes

- No forecast/schedule sharing and no ASN machinery in this module — at the ERP-suite pole the collaboration loop is **PO-confirmation-centric** (plus consignment). The schedule/forecast/ASN legs belong to dedicated collaboration products or EDI channels. This is the key structural contrast inside one market.
- The buyer's PO object and its internal approval workflow ("an internal process that the vendor isn't involved in") remain in the ERP; vendor collaboration is the shared surface in front of them. Consistent with the supplier-portal pass's surface-vs-record finding, but here the surface carries a genuine two-way response loop.

## Product D — Aligni (SMB pole)

### Key observations (Layer A at feature-page level; Tier-2 source)

- "Replace email threads with a dedicated **vendor portal** where suppliers can **view RFQs, update delivery dates, and confirm quotes** directly. Every update is tracked, visible, and tied to the right part or PO."
- "Share RFQs and POs through a **no-login-required** vendor portal"; "Suppliers can update pricing, lead times, and **promise dates**"; "Every update is tracked and visible."
- Performance: "Track every **promise date and delivery outcome** to spot trends, delays, and lead time shifts. See line-by-line delivery history."
- Document vaults: share specs/drawings/inspection criteria; role-based access and audit trails; "Get notified when vendors view or download attachments"; auto-notify on content changes.
- Positioning: "Integrated Vendor Collaboration — Manage quote and purchase conversations in one place and provide suppliers the ability to adjust information in the system."

### Boundary-relevant notes

- The SMB realization collapses the loop to quote/PO response + promise dates + delivery outcome tracking — still the same three structures (demand signal = RFQ/PO tied to part; response = confirm/quote/promise-date updates; closure = delivery outcome history), at minimal depth. Supports the abstraction (the invariant is the loop, not any specific document type or depth).

## Cross-product Comparison

| Dimension | SupplyOn SCC/AirSupply | e2open Supply suite | D365 Vendor collaboration | Aligni |
|---|---|---|---|---|
| Deployment shape | industry network, many buyers/suppliers, two-sided docs | multi-enterprise SaaS network | ERP-embedded module, one buyer | MRP-embedded portal, one buyer |
| Demand signal content | POs + JIT/JIS/Kanban + delivery schedules + forecasts; VMI | discrete/blanket orders, blanket releases, scheduling agreements; forecasts/upsides | POs (+ consignment consumption POs; RFQs) | RFQs and POs tied to parts |
| Supplier response | order confirmations; schedule response; interactive adjustment of delivery quantity/date; capacity exchange | commits against forecast; exception workflows; expedite/de-expedites | accept / reject / accept-with-changes (dates, quantities, splits, substitutions, line rejects) | confirm quotes; update pricing/lead times/promise dates |
| Fulfillment closure | ASN/FPA (packing data, transport refs), goods receipt, due deliveries, delivery status, stock movements (VMI) | shipments, receipts; order-vs-shipment mismatch detection; invoices | product receipts (incl. consignment); confirmed-PO receiving | promise-vs-delivery outcome history |
| Roles documented | supplier how-tos + customer how-tos (two-sided) | buyer-side applications + supplier network participation | buyer agents; vendor contacts with security roles | buyer + vendors |
| Channel breadth | web UI + M2M/EDI connection category | web UI + partner network onboarding | web UI; explicitly for non-EDI vendors; email fallback documented | web portal, login optional |
| Invoice collaboration | separate Invoicing product family | inside PO Collaboration app | invoices listed among module objects; separate AP invoicing workspace | not evidenced |
| Extras | capacity mgmt, performance, AI analytics, quality linkage (separate families) | inventory collaboration, buy-sell, cost mgmt, manufacturing collaboration, risk/quality (separate apps) | RFQ collaboration, vendor master data access | document vaults, branding, historical pricing |

**Stable across all four (candidates for the defining core):**

1. A buyer-issued demand/order signal held as a shared record (PO / blanket-release / schedule / forecast — content varies by pole).
2. A supplier response recorded back into the buyer's record (confirm/accept, promise/commit, exception at quantity/date/substitution/split grain).
3. A fulfillment leg reconciling signal → shipment → receipt/delivery outcome, visible to both parties.

**Common but variable:** ordering models (JIT/JIS/Kanban/VMI/consignment), capacity/feasibility exchange, packing/label data, master-data surfaces, per-supplier activation/onboarding, alerts & mismatch detection, performance scoring (OTIF), attachments/vaults, invoice collaboration, multi-tier extension, EDI/M2M channels, AI overlays.

**Pole-dependent:** network vs single-buyer; schedule-centric vs PO-centric vs forecast-commit-centric; invoice inside vs adjacent; quality/invoicing as separate product families.

## Canonical Model

### Level 0 — Defining Invariant (minimal)

Three jointly-held structures; remove any one and the product stops being this Type:

1. **The shared supply demand record** — a buyer-issued, supplier-addressed record of what the manufacturer needs, when, and in what quantity (orders, blanket releases/scheduling-agreement releases, release schedules/call-offs, or forecasts), held in the system as the record both parties work from. Remove → one-way demand publication (a document feed), not collaboration.
2. **The supplier response loop** — the supplier answers *into the shared record*: accept/confirm/commit, or exception (quantity, date, split, substitution), recorded so the buyer's side sees and can process the supplier's position. Remove → the supplier becomes a passive reader: portal-as-surface territory.
3. **The signal-to-arrival closure** — the same record advances through fulfillment: shipment/delivery notice, delivery status, goods receipt — promise vs actual reconcilable by both parties. Remove → a plan/commitment exchange with no delivery consequence (planning-communication tool) or a bare tracking feed.

Historical check: paper/telex-era automotive release management (buyer mails/telecopies a release schedule; supplier confirms quantities/dates by return; shipments arrive with packing slips; receiving checks arrivals against the schedule) satisfies all three legs with no software. Conceptual lineage — moderate confidence, no fetched source (recorded in Uncertainties). §24-style check: platform-native SMB portals, ERP-embedded modules, and industry networks all fit; no era/region machinery in the core.

### Level 1 — Common Mature Structure

- Multiple ordering models over one collaboration model: discrete PO, blanket order/release, scheduling agreement, JIT/JIS, Kanban, VMI/consignment.
- Schedule/forecast collaboration views: time-phased demand vs supplier commits/confirmations; capacity/feasibility exchange.
- Demand reminders, expedites/de-expedites, cancellation flows, change handling as explicit collaboration events.
- Shipment notice machinery (ASN-class) with packing/transport data; goods receipt views; due-deliveries worklists.
- Mismatch/exception detection (order vs shipment quantities; demand vs commit), alerts, notifications.
- Two-sided interfaces: buyer workspace (responses requiring action) and supplier worklists (orders for review, due deliveries, ASN creation).
- Per-supplier activation / trading-relationship gating; supplier onboarding machinery.
- Document sharing (attachments/vaults) tied to orders/parts; audit trails.
- Delivery performance monitoring (promise vs actual; OTIF-class metrics).

### Level 2 — Variant / Optional

- Pole: industry/multi-buyer network vs single-buyer ERP/MRP-embedded vs standalone SaaS suite.
- Anchor object: schedule/release-centric (automotive/aerospace), PO-confirmation-centric (ERP suite), forecast-commit-centric (multi-tier orchestration).
- Invoice collaboration inside the loop vs separate invoicing products.
- Quality collaboration content (complaints, concessions, certificates) as connected extension.
- Multi-tier extension (tier-2 visibility, sub-tier networks).
- Channel: portal UI only vs EDI/M2M integration vs email fallback; login vs login-less supplier access.
- Capacity management, packaging/empties, AI analytics overlays — separate modules in-network products.
- Inventory collaboration modes (consignment, VMI) as distinct workflows over shared stock records.

### Level 3 — Vendor-specific (research notes only)

- SupplyOn: FPA (Forwarder Pickup Advice) as distinct ASN-sibling artifact; FPA/ASN tab structure (select positions → additional data → transport references → packing data → complete); automatic FPA/ASN number assignment; control points; packing-instruction master data; "control points" admin; AirSupply naming/heritage (BoostAeroSpace: Airbus, Dassault Aviation, Safran, Thales); store/academy/rollout-cockpit ecosystem; 140,000+ suppliers / 100 countries / 500B € spend stats; OTIF +15%, invoice-booking 95% stats.
- e2open: Harmony unified UX; e2net partner network; "Supply Network Discovery" (multi-tier mapping/due diligence); Long Tail PO-reduction case (overdue POs "from over a hundred to just two"); 50–75% / 60% / 20% / 35% / 10% stat blocks; Buy-Sell Management; Product Cost Management.
- D365: exact form names (Vendors page, Purchase order preparation workspace, Purchase order vendor confirmation history, consignment pages); *Collaboration activation* field values; auto-confirmation batch job and its scheduling guidance (recurrence reasoning vs lead times); "Is PO update processed?" flag; bolded changed fields; public-sector RFQ publication extensions; email templates with replacement tokens.
- Aligni: DiscussAnything™, TimeWarp™ (lead-time navigation), custom branding of POs/RFQs/portal, no-login portal access, vaults with vendor-view notifications.

## Vendor-specific Findings

- The two-sided documentation split (supplier how-tos vs customer how-tos) is a SupplyOn help-center structure; D365 documents buyer-side setup plus a separate vendor-side article; e2open/Aligni publish buyer-side pages with supplier actions described. Two-sidedness is cross-product; the specific doc split is vendor-specific.
- AirSupply's "not just document exchange" portal contrast and D365's "targeted at vendors who don't have EDI integration" scoping are vendor-authored boundary statements — usable as evidence of the market's own discrimination lines, quoted in Research Notes and paraphrased vendor-neutrally in the final document.
- Consignment/VMI inventory visibility (D365 consignment pages; SupplyOn VMI + stock movements; e2open Supply Inventory Collaboration) recurs across poles → L1/L2, not definitional.

## Rejected Findings

- "Supplier collaboration = supplier portal" — rejected: the supplier-portal pass already held surface vs record; this pass finds the dedicated collaboration Type carries the *loop* (response + closure) as its center. SupplyOn ships separate Procurement/Capacity/Performance/Invoicing categories; D365 distinguishes the PO object from the collaboration surface. A pure publish-and-download portal with no recorded supplier response loop is a different Type.
- "EDI formats (830/862/DELFOR/DELJIT, VDA) define the Type" — rejected: EDI appears in-sample only as a transport/connection alternative (D365 scoping sentence; SupplyOn M2M/EDI category). Message-format machinery belongs to the EDI Platform Type.
- "Invoice processing is part of the core" — rejected: in-sample it is a separate product family (SupplyOn Invoicing), a separate suite app listed among many (e2open), or a separate AP workspace (D365). Optional.
- "Quality management (complaints/concessions/8D) is part of the core" — rejected: SupplyOn keeps Quality Management as a separate family; e2open as a separate application; AirSupply integrates it as extension. Flagged for the supplier-quality-management pass.
- "Multi-tier is definitional" — rejected as invariant: strongly positioned by network poles (e2open, AirSupply) but absent from D365/Aligni realizations, which are single-tier. Variant axis.
- "Capacity management is definitional" — rejected: SupplyOn ships it as a separate product; others embed feasibility exchange in responses. Common capability, not invariant.

## Boundary Findings

1. **vs Supplier Portal (§10, processed — pre-hung joint-review flag DISCHARGED from this side)**. The portal pass held "collaboration content vs document-exchange surface" at center-of-gravity, noting ASN/schedule collaboration was under-evidenced there. This pass finds ASN/ship-notice and schedule/forecast collaboration to be the **center** of dedicated collaboration products, and the market itself draws the line: SupplyOn FAQ ("not just document exchange… collaborative forecast handling, purchase order status, delivery coordination, incoming-goods optimization, inventory collaboration…"), D365 (collaboration module = response loop, distinct from mere document availability). Ratified discriminator: **a portal publishes buyer-side records for suppliers to access; collaboration Type owns a shared multi-step loop with a recorded supplier response and a fulfillment closure.** Overlap zone remains (portals can carry collaboration content; collaboration products include portal-like surfaces) — center of gravity decides; packaging gradient documented.
2. **vs Supplier Management Platform (§10, processed)**. Supplier of record/qualification/standing vs the demand-and-fulfillment loop. SupplyOn realizes them as separate solution families (Supplier Management vs Supply Chain Collaboration) with separate help categories; D365 grants "access to parts of their vendor master data" from within collaboration — master data is a companion surface, not the center. RATIFIED.
3. **vs Purchase Order Management (§10, processed)**. POM owns the PO as a buyer-side commitment object (create → approve → issue → fulfill → close). Collaboration makes the supplier an active participant in the same record (accept-with-changes, splits, promise dates) and extends the anchor beyond the PO (schedules, forecasts). D365 realizes both in one product (PO management internal; vendor collaboration shared surface); e2open's PO Collaboration adds release/agreement content and shipment/receipt legs the POM pass held buyer-side. Seam: buyer-side object lifecycle vs two-way shared loop.
4. **vs Procure-to-pay Platform (§10, processed)**. P2P chain ends in a payment-ready payable; the collaboration loop's spine ends in arrival/receipt. P2P's own pass listed "supplier collaboration surface" as an L1 capability — consistent: surface-as-capability inside P2P vs the loop as the Type. Invoice collaboration optional, not the head of the chain here.
5. **vs EDI Platform (§13 sibling, unprocessed)**. EDI = transport/format machinery; this Type = the application loop. D365 scoping sentence is the cleanest evidence ("targeted at vendors who don't have EDI integration"); SupplyOn separates M2M/EDI connection from SCC. Flag for the edi-platform pass; expect EDI pass to treat this Type as a consumer of its pipes.
6. **vs Supply Chain Planning / Demand Planning / APS (§10, SCP + demand-planning processed; APS/production-planning unprocessed)**. Planning types compute plans internally ("the platform plans, never executes" — SCP pass). This Type computes nothing about what to buy; it **exchanges** buyer demand signals with the counterparty and works exceptions. A forecast shared here is a record to be responded to, not a plan to be optimized. Seam: computation vs cross-party exchange. The demand-planning pass's "forecast of record" is the internal plan; the collaboration record is the supplier-addressed release/commit state.
7. **vs Manufacturing Execution System (§16, processed)**. MES executes internal shop-floor orders at operation grain and produces the as-built record. This Type is external: the loop crosses a company boundary; no operation execution, no as-built genealogy. Different worlds despite both touching production.
8. **vs Supplier Quality Management (§16 sibling, unprocessed)**. Quality content (complaints, concessions, audits, certificates) is adjacent and commonly connected (AirSupply quality collaboration; SupplyOn Quality family). Flag for the SQM pass: SQM should center the quality record/8D-class loop; this leaf keeps only demand/commitment/fulfillment collaboration in its core.
9. **vs Forecast/commitment tools without closure** — a product that only distributes forecasts and records commitments (no order/shipment/receipt leg) would sit at the Type's edge; in-sample such content always ships alongside order/fulfillment collaboration (e2open SFC inside the Supply suite). Held as a thin slice, not a separate Type.

## Uncertainties

- SupplyOn help **article bodies** login-gated: procedural states (exact ASN statuses, response states, deadline semantics) not verified — interface/artifact inventory verified from the index only.
- SAP SNC / SAP Ariba Supply Chain Collaboration / Kinaxis unreachable (404 ×2 or JS shell): the classic enterprise "supply network collaboration" generation is asserted only as market context (they are named in fetched vendor-independent content as the collaboration category), with **no operational claims**.
- Whether ASN submission is buyer-mandated per supplier in typical deployments (configuration-dependent) — not asserted.
- Historical check rests on conceptual lineage (paper/telex release accounting); no fetched source. Assertion strength in the final document kept at "conceptual" level.
- e2open/Aligni evidence is Tier-2 (product pages); workflow mechanics (e.g., how commits are versioned at e2open) not verified at Tier-1.
- Pricing/commercial-field behavior: D365 forbids vendor price changes on PO response (A); Aligni vendors update pricing in quote flow (A, different object). Generalization "commercial fields stay buyer-controlled in order confirmation" is moderate-confidence, supported by one Tier-1 + one Tier-2 in different object types.

## Final Synthesis

The Type is the **cross-company working loop between a manufacturer and its production suppliers**: the buyer issues a shared supply demand record (orders, releases/schedules, forecasts/call-offs for specific items over time); the supplier responds into that record (confirm/commit, or exception — quantity, date, split, substitute); and the record closes around physical fulfillment (shipment notice, delivery status, goods receipt — promise vs actual visible to both sides). Realizations span four poles — industry/multi-buyer networks (SupplyOn), multi-enterprise SaaS suites (e2open), ERP-embedded vendor-collaboration modules (Dynamics 365), and SMB MRP portals (Aligni) — but all four hold the same three structures. Everything else is packaging: ordering models (JIT/JIS/Kanban/VMI), capacity exchange, packing/label data, alerts, performance scoring, invoice and quality extensions, multi-tier breadth, and EDI/M2M channels. The Type's boundaries are held on two axes: **surface vs loop** (vs Supplier Portal) and **exchange vs computation** (vs planning), with EDI as the transport layer beneath and MES as the internal execution world beside it.
