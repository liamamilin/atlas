# Research Notes — Food Traceability Platform

Research date: 2026-09-08
Section: §20 Agriculture, Food & Natural Resources
Slug: food-traceability-platform

---

## Research Goal

Understand "Food Traceability Platform" as an Application Type: what the unit of record is, what events are captured and by whom, how records cross trading-partner boundaries, what the retrieval/investigation loop looks like, who uses the product and in what posture, which rules matter, and where the boundary sits — especially against the processed siblings **food-recall-management** (2026-09-08, which pre-hung a JOINT REVIEW flag naming this leaf), **food-cold-chain-management** (2026-09-08), **food-manufacturing-erp** (2026-09-08), **food-safety-management** (2026-09-08), and machinery neighbors (Shipment Visibility Platform, EDI Platform / Data Exchange Platform, Produce Packing House Management).

## Initial Boundary

Working hypothesis before research: a food traceability platform is the standing, chain-wide ledger of lot-identified food and its movements across trading partners — "where did this lot come from / where did it go" — as opposed to:

- **Food Recall Management**: the episodic declared event (scope resolution + notification/response/verification loop + closure documentation)
- **Food Manufacturing ERP**: internal lot-controlled material flow within one company, tied to production, inventory and finance
- **Food Cold Chain Management**: condition integrity of temperature-controlled contexts
- **Food Safety Management / HACCP Management**: standing program machinery (hazards, control points, monitoring, CAPA, audits)
- **Shipment Visibility Platform**: per-shipment transport status, cargo-agnostic

Open question entering research: is the **cross-partner** leg definitional, or can an internal-traceability-only product count as the same Type? (Suggested test: if the ledger never crosses an organization's walls, it is ERP/WMS/MES territory.)

## Research Questions

1. What is the unit of record — lot, batch, serial, case, pallet — and how is it identified?
2. What events are captured, at what points in the chain, by whom, carrying what data?
3. How do records cross organization boundaries (portals, feeds, message exchange, shared ledger)?
4. What does the retrieval function look like: one-up/one-back vs full chain view; investigation surfaces?
5. Who uses it, and in what posture (routine capture vs during an incident)?
6. What rules matter: data-sharing governance, completeness/gaps, validation, evidence retention?
7. How does recall integrate without the platform collapsing into recall management?
8. Which regulatory frames drive the market (FSMA 204 KDE/CTE, PTI, GS1, GDST), and which of those are regime-specific rather than definitional?
9. Historical check: would a paper-era one-up/one-back record-keeping chain satisfy the definition?

## Representative Products

Selected 2026-09-08 for market representation + documentation depth + different product philosophies + different customer layers:

| Product | Pole | Customer layer | Evidence tier |
|---|---|---|---|
| FoodLogiQ Traceability (Trustwell) | buyer-operated supply-chain traceability network with an investigations surface; traceability as one module of a wider compliance suite | restaurant/grocery brands + their suppliers | Tier-2 product page |
| ReposiTrak Traceability Network | retailer-driven KDE data-exchange network with validation-on-ingest; traceability as one product family of a retail network platform | retailers/wholesalers/foodservice + suppliers | Tier-2 product page + press releases |
| Wholechain | event-based, GS1/EPCIS-aligned blockchain traceability SaaS with labeling + consumer-transparency surfaces | small producers through global brands | Tier-1 helpdesk + product site |

Context evidence inherited from sibling passes (recorded in STATUS.md): Trustwell ships FoodLogiQ Traceability and FoodLogiQ Recall as **separate modules**, with Recall explicitly consuming Traceability output; ReposiTrak markets traceability as recall **readiness** while partnering with a recall-execution vendor; food-manufacturing-erp holds internal bi-directional lot traceability inside its own L0 (single-company scope).

Abandoned samples (network rules): FarmSoft (farmsoft.com returned 403 on first fetch), iFoodDS (empty responses ×2), FoodLogiQ support portal (transport error ×1), IBM Food Trust (not attempted — sample sufficient, stop conditions reached).

## Sources

Fetched 2026-09-08:

- Trustwell — FoodLogiQ Traceability product page: https://www.trustwell.com/products/foodlogiq/traceability/ (Tier-2)
- ReposiTrak — Traceability & FSMA 204 page: https://repositrak.com/fda-food-traceability/food-traceability/ (Tier-2)
- ReposiTrak — Traceability Network press release (produce suppliers joining the queue): https://www.repositrak.com/traceability/ → redirected to 2026-04-07 press release (Tier-2, corroborating)
- Wholechain — product site: https://wholechain.co/ (Tier-2)
- Wholechain Helpdesk (Tier-1):
  - https://support.wholechain.com/ (category map)
  - https://support.wholechain.com/category/318-traceability-events
  - https://support.wholechain.com/article/88-event-based-traceability
  - https://support.wholechain.com/article/225-event-data-sharing-overview

Unreachable / not used: farmsoft.com (403), ifoods.com (empty ×2), support.foodlogiq.com (transport error ×1). No primary regulatory source (FDA) was fetched; FSMA 204 content below is **as described by vendors** and is treated as vendor-reported.

---

## Product A — FoodLogiQ Traceability (Trustwell)

### Key observations (evidence layer A unless noted)

- Positioning: "capture and share Critical Tracking Event data, strengthen supply chain visibility, and respond faster when risk enters the picture"; explicitly sold for "FSMA 204 compliance by capturing and sharing CTE data across your organization and stakeholders" — the platform's unit of compliance work is the CTE (Critical Tracking Event).
- Unit of record: "Trace products at the batch-lot level both forward and backward across your supply chain" + "Visualize at the Traceability Lot Level" — lot/batch is the trace identity. Data captured includes "lots, expiration, and shipping dates".
- Cross-org: "view the movement of products and ingredients across your supply chain… where products came from, where they went, and which partners handled them along the way"; a supplier counter ("Suppliers In Platform") and industries spanning restaurants, grocers+retailers, manufacturers, distributors, growers/packers/shippers confirm the multi-party population. Sales framing: "Whether it's a trading partner traceability mandate, or compliance with the FSMA 204 traceability regulation".
- Retrieval/investigation: a named **Investigations** interface — "review product movement in timeline and map views, identify gaps in Critical Tracking Event (CTE) data", "uncover missing or incomplete traceability data", "identify potential root causes of food safety incidents". Gaps in event data are a first-class surfaced condition.
- Recall hand-off (not recall management): "create a withdrawal directly from an investigation when fast action is needed"; "Be alerted to impacted lots to launch withdrawals". Consistent with sibling-pass evidence that FoodLogiQ **Recall** is a separate module consuming Traceability output ("identify affected products at the batch-lot level").
- Evidence production: "Export investigation event data in FSMA 204 Electronic Sortable Spreadsheet format. Each export downloads as a zip file with relevant event, location, and product information to support FDA traceability record requests."
- Standards: "aligned with GS1 standards… capture and organize product, location, and event data so it can be shared across supply chain partners more consistently" — GS1 framed as alignment/implementation, not the essence.
- Capture surfaces: "mobile access to report, review, and act on supply chain data" ("from field to floor").
- Platform context: Traceability is one module of the FoodLogiQ suite (Compliance, Quality Management, Product Management, Risk Management, Recall alongside). Traceability module evidence stands on its own page.

## Product B — ReposiTrak Traceability Network

### Key observations

- Positioning: "the world's largest food traceability and regulatory compliance network" (vendor claim); connecting (vendor-claimed figures, recorded as claims only): 12,000 retail stores, 8,000 suppliers, 36 distribution centers. Research-notes-only figures — NOT promoted to the final document.
- The exchange frame: "efficiently exchanging FDA-required Key Data Elements (KDEs) for each Critical Tracking Event (CTE) in their supply chains — driven by the immediate traceability data sharing requirements of their retail, wholesale and foodservice customers." The product's center is **data sharing between partners**, not internal record-keeping.
- Regulatory frame as vendor-described: "Under FSMA 204, entities that manufacture, process, pack, or hold foods listed on the FTL must: capture and maintain KDEs for each CTE such as shipping, receiving, and transformation; exchange those KDEs with trading partners to ensure traceability continuity; provide complete traceability records to the FDA within 24 hours upon request, in a sortable electronic format." (Vendor description of the rule — not independently verified; used qualitatively only.)
- Ingest and validation machinery: "The platform accepts supplier data in any format—manual entry, automated feeds, or system uploads—and runs each submission through a 500-point validation process before transmitting it to trading partners"; "Data-agnostic ingestion that extracts and creates KDE records from shipping or receiving documents in *any* format"; a press release describes a "500+ point error detection process" and a US-based team correcting supplier data **before it reaches customers**. The numeric claim stays here.
- Electronic transmission beyond labels: "Electronic transmission of required KDEs, including data finalized post-labeling"; "Why labels alone are not sufficient… certain KDEs must be transmitted electronically with each shipment." — establishes that the platform's record is *more* than the physical label content: the ledger entry, not the label, is the shared object.
- Market posture: "Retailers, wholesalers and foodservice operators are actively requiring traceability data sharing from their produce suppliers today" — buyer-mandate-driven adoption; retailers demanding traceability "for all food items, not only those on the FDA's Food Traceability List", with timelines exceeding federal deadlines.
- Onboarding: suppliers join a "queue" and are onboarded over months (vendor statement) — network onboarding is a real operational phase.
- Recall relation: sibling navigation page "Prepare For Faster, More Precise Recalls" — traceability sold as recall *readiness*; the event workflow itself lives elsewhere (ReposiTrak partners with a recall-execution vendor per the sibling pass).
- Platform context: Traceability Network is one product family beside Compliance Management, Scan-based Trading, marketplace, and supply-chain modules.

## Product C — Wholechain

### Key observations (Tier-1 helpdesk unless noted)

- Event-based model (Tier-1): "Wholechain tackles traceability by breaking up complex supply chain webs into a series of steps — which we call *events*. Events capture the *who, what, when* and *where* of each activity a product undergoes in its journey." Events are aligned to GS1 EPCIS. Event types documented:
  - **Commission** — "a product coming into existence in its documented supply chain… typically the point of harvest, or the first time that a product is being documented as itself" (origin leg).
  - **Decommission** — product exits the traced chain (consumed, damaged, destroyed) with a required reason.
  - **Ship (Internal)** — movement between own locations while custody is retained.
  - **Ship (External)** — "moves product item(s) from a company's current inventory to its shipped inventory tab with the status 'pending', until the recipient company either receives or rejects the item(s) in their account" — the **cross-partner hand-off is a two-sided recorded transaction**.
  - **Receive** — confirms arrival at own location; can be logged for goods from a **non-user** (journey can start mid-chain); discrepancy → recipient may **reject** the ship record, "which sends a notification to the shipper that some information was off and the event needs to be revised".
  - **Aggregate / Disaggregate** — grouping into pallets/containers/SSCC logistical units and reversal; "All aggregations are *reversible*".
  - **Transform** — "an activity that *irreversibly* changes a product, transforming it into a new, traceable output product with a new Primary ID (i.e. a new serial number or lot number)" with inputs → outputs linkage ("an input lot of whole sockeye salmon is processed into three distinct production lots of packaged fillets"). This is the lot-identity-persists-through-transformation leg, documented explicitly.
- Custom data: per-event custom attributes via templates.
- Substrate: "all event data is written on a blockchain upon clicking 'Log Event'" — blockchain is the substrate, not the definition (the other two samples do fine without it).
- Capture surfaces: mobile/tablet/desktop "in the field, at sea, or in the warehouse".
- Sharing governance (Tier-1): privacy set **per product**; two preferences — **Open** (downstream companies can view event data; "upstream companies will not be able to view event details beyond their Ship event") and **Restricted** (downstream sees only Ship events). Invariant across settings: "Ship event record data will always be shared with downstream companies… you'll always be able to access the details of the Ship event record that an upstream company in your Network has sent to you." The hand-off event is always visible to both sides; deeper event visibility is governed.
- Labeling module: GS1-128, DataMatrix, SSCC barcodes; "PTI compliance made easy" (Produce Traceability Initiative); label editor; shared templates across plants.
- Transparency extension: QR codes unlocking product journeys for consumers ("Scan-to-see product journeys"); "Enable lot-level transparency… down to individual product batches or lots to meet buyer and regulatory demands" (product site, Tier-2).
- Integrations: ERP and WMS connections; API; Zapier (product site).
- Population: "global brands, manufacturers, wholesalers, exporters, importers, distributors, certifiers and small scale cooperatives" — the widest customer span in the sample.
- Analytics: site nav shows "Analytics COMING SOON" — analytics is not yet a shipped capability here (useful as existence proof that a functioning traceability product can lack analytics entirely).

---

## Cross-product Comparison

| Dimension | FoodLogiQ Traceability | ReposiTrak Traceability Network | Wholechain |
|---|---|---|---|
| Unit of record | batch-lot ("traceability lot level") | KDE records per CTE on shipped/received product (lot-level implied by FSMA frame) | lot / serial ("Primary ID") per item, aggregated into pallets/SSCC |
| Events captured | CTE data across partners; lots + expiration + shipping dates | shipping, receiving, transformation (FSMA frame); data finalized post-labeling | Commission, Decommission, Ship (int/ext), Receive, Aggregate, Disaggregate, Transform |
| Who records | teams across the supply chain, mobile "field to floor" | suppliers submit (any format); platform validates then transmits | each company logs its own events; recipient confirms/rejects |
| Cross-org mechanism | shared platform, supplier network | validated data files transmitted to trading partners | shared event ledger; ship→receive hand-off between accounts; per-product sharing settings |
| Retrieval | Investigations: timeline + map, forward & backward, gap detection | recall readiness (fast, precise scope from exchanged data) | chain view / product journeys; Sourceview storytelling |
| Recall relation | create withdrawal from an investigation; alert impacted lots | recall readiness; execution via partner | not positioned around recall (transparency + compliance center) |
| Standards alignment | GS1 | GS1-implied FSMA 204 KDE/CTE; retailer mandates | GS1 EPCIS, GS1 labels, PTI, GDST |
| Substrate | conventional SaaS | conventional SaaS network | blockchain |
| Driver named by vendor | trading-partner mandates + FSMA 204 | retailer/wholesale/foodservice mandates + FSMA 204 | buyer + regulatory demands, transparency |
| Analytics | (suite-level) | (suite-level reporting) | "COMING SOON" |

Stable across all three (cross-product commonality, layer B): lot/batch identity as the traceable unit; events recorded at the points food moves or changes (origin, transformation, ship, receive at minimum); records shared or linked across trading-partner boundaries; a forward-and-backward retrieval function; evidence production for regulators/auditors; regulatory-frame alignment as a selling point but described in vendor-specific frames.

Varying across all three (layer A per product, layer C inference for the abstraction): the event vocabulary (CTE/KDE frame vs EPCIS-derived type names), the ingest mechanism (portal + investigation vs validated file transmission vs account-to-account hand-off), the substrate, the retrieval surface, the segment emphasis.

## Abstraction (four levels)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The traceable lot as the unit of record** — food held at lot/batch identity granularity (traceability lot code or equivalent; serials as a refinement), each lot a persistent identified record. Remove → shipment/order tracker or product catalog.
2. **Tracking events recorded at the points the food moves or changes** — events at origin/commissioning, transformation, aggregation, shipping, receiving, exit — each capturing what/when/where/who and attributed to the performing party; the accumulating event history is the ledger. Remove → product/location master data.
3. **Cross-partner linkage with bi-directional retrieval** — one party's outbound record joins the next party's inbound record across the trading-partner boundary (each partner contributing its own events), so the platform can trace a lot upstream and downstream along the chain on demand. Remove → internal lot tracking (ERP/WMS/MES territory).

Jointly-held is load-bearing:

- 1 alone = lot-tagged product registry
- 2 without 1 = generic activity log / per-shipment tracker
- 3 without 1+2 = trading-partner network or EDI pipe with nothing traceable in it
- 1+3 without 2 = a chain directory of who-trades-with-whom, no movements
- 2+3 without 1 = consignment-level transport tracking (Shipment Visibility territory)

### L1 — Common Mature Structure

Standard capabilities in mature products, not definitional:

- Regulatory-frame alignment: FSMA 204-style KDE/CTE capture and sortable-electronic exports; PTI produce labeling; GS1 identifiers (GTIN/GLN/SSCC) and EPCIS-style event models; seafood data standards (GDST). All regime- and era-bound.
- Capture surfaces: supplier web portals, mobile field capture, scan-based entry, automated feeds/EDI/API, extraction from shipping/receiving documents.
- Submission validation and completeness/gap surfacing.
- Case/pallet label generation carrying lot identity.
- Chain visualization: timeline and map views, supply-chain mapping, consumer-facing journeys.
- Lot alerting and hand-off into recall/withdrawal machinery.
- Trading-partner onboarding (enrollment, locations, products) and data-sharing governance.
- Integrations with ERP/WMS; participation/completeness analytics.

### L2 — Variant / Optional Structure

- Posture: buyer-mandate network (retailer/QSR compels supplier data sharing) vs supplier-side compliance tooling vs producer/processor operational capture vs shared neutral network
- Depth: one-up/one-back only vs multi-step chain view
- Substrate: conventional database vs distributed ledger
- Scope: foods on a regulatory traceability list vs all items
- Segment specialization: produce, seafood, general food
- Consumer-facing transparency extension (QR product journeys)
- Depth of transformation modeling (input→output lot linkage explicit vs implied)

### L3 — Vendor-specific Structure (research notes only)

- Wholechain's branded event names (Commission/Decommission…), Sourceview storytelling, Help Scout knowledge structure, Zapier integrations.
- ReposiTrak's "500+ point error detection process", "queue" onboarding, vendor-claimed network size (12,000 stores / 8,000 suppliers / 36 DCs), scan-based-trading and compliance-management product families beside traceability.
- FoodLogiQ's "Investigations" interface naming, ESS export packaged as zip, Chipotle case study, suite module layout.
- IBM Food Trust (not fetched) — blockchain network pole known from market context only; no claims made.

## Rejected Findings

- **"FSMA 204 KDE/CTE compliance" as the definition** — rejected: the framework is a current US regulatory regime; the historical check (below) and the produce/seafood standards variety (PTI, GDST) show the Type predates and exceeds any one regime. Held as L1.
- **"GS1/EPCIS standards" as the definition** — rejected: dominant implementation vocabulary, not the essence; a paper chain satisfies the Type without them.
- **Blockchain as definitional** — rejected: one sampled product only; the other two operate conventional databases.
- **Label generation as definitional** — rejected: only Wholechain leads with a labeling module; the ledger entry, not the label, is the shared object (ReposiTrak explicitly transmits data "finalized post-labeling" that labels cannot carry).
- **Internal-only traceability as sufficient** — rejected as L0: all three sampled platforms center the cross-partner exchange; internal lot flow is the ERP/WMS/MES sibling's territory (consistent with food-manufacturing-erp's own L0, which holds internal bi-directional traceability inside one company).
- **"Platform" = consumer-facing transparency site** — rejected: consumer QR journeys are an optional extension (one product).
- **Analytics/dashboards as definitional** — rejected: one sampled product ships with analytics "coming soon".

## Boundary Findings

1. **vs Food Recall Management (§20 sibling — pre-hung JOINT REVIEW flag DISCHARGED this pass)**: seam = standing record vs episodic event. Traceability is the *continuous* lot-movement ledger across trading partners ("where did this lot go / where did it come from"); recall management is the *declared event* with scope resolution + notification/response/verification loop + closure documentation. Vendor corroboration: Trustwell ships the two as separate modules with Recall consuming Traceability output; FoodLogiQ Traceability's own page ends at "create a withdrawal directly from an investigation" and "be alerted to impacted lots" — the platform hands off an implicated lot, it does not run the event loop; ReposiTrak sells traceability as recall *readiness* and partners for execution. Tests: remove the event workflow → traceability platform remains; remove the standing ledger → recall event platform remains (fed by imports/notice data). Verdict: **keep-both ratified from this side.**
2. **vs Food Manufacturing ERP (§20 sibling, processed)**: ERP holds *internal* lot-controlled material flow (ingredients→batches→finished goods→shipments) tied to production and finance within one company; the traceability platform holds the *cross-organization* chain where each party records its own events and the links join at the trading boundary. Test: remove cross-partner linkage → ERP/WMS/MES territory; remove production/inventory/financial machinery → traceability platform remains.
3. **vs Food Cold Chain Management (§20 sibling, processed)**: lot identity & movement vs condition integrity of temperature-controlled contexts; some vendors bundle both (sibling-pass observation).
4. **vs Food Safety Management / HACCP Management (§20 siblings)**: standing program machinery (hazards, control points, monitoring, CAPA, audits) vs the lot ledger; traceability supplies "what moved where" evidence to the program but is not program machinery.
5. **vs Shipment Visibility Platform (§18)**: per-consignment transport status (cargo-agnostic; "where is my truck/container") vs the lot-identity chain including transformations ("which lots went into this product, and where did each come from"). Ship/receive events overlap at the boundary; transformation and lot identity do not exist in shipment visibility.
6. **vs EDI Platform / Data Exchange Platform (§13)**: generic document/message exchange vs the lot-ledger of record with event semantics. ReposiTrak's document-based ingestion is an implementation flavor — its output is KDE records on lots, not messages.
7. **vs Produce Packing House Management / Harvest Management (§20)**: internal packing-house/harvest operations vs the chain-wide ledger; a packing house is one event source among many in the chain.

## Uncertainties

- No primary regulatory source was fetched; FSMA 204 specifics (KDE/CTE definitions, the 24-hour FDA-request window, the Electronic Sortable Spreadsheet requirement) are known here **only as vendors describe them** and were used qualitatively, never as precisely asserted facts.
- FarmSoft, iFoodDS and IBM Food Trust were not documented (403 / empty / not attempted) — the producer-operational pole rests on Wholechain's commission/transform/labeling surfaces plus FoodLogiQ's growers-packers-shippers industry page; the blockchain-network enterprise pole rests on market context only.
- FoodLogiQ help center unreachable — FoodLogiQ observations rest on its product page (Tier-2), which is unusually process-explicit for the category, but interface mechanics beyond the Investigations description are unverified.
- Whether "one-up/one-back" is the universal minimum linkage depth could not be confirmed across the sample directly (Wholechain documents per-product sharing that yields at least hand-off visibility to both sides; ReposiTrak transmits to direct trading partners; FoodLogiQ asserts chain-level tracing). Recorded as a nuance, not asserted as a rule.
- Serial-level vs lot-level tracking: Wholechain documents both; the other two are lot/frame-level in their surfaced language. Lot-level held as the L0 concept with serials as a refinement.

## Historical Check (per §24 of the workflow)

Question: would older, regional, platform-native record-keeping satisfy the L0?

**Paper-era one-up/one-back chain (conceptual):** a packing house keeps a lot register (harvest/pack dates, lot numbers on case tags), a shipping ledger recording which lots went to which customers, and buyers keep receiving ledgers recording which lots arrived from which suppliers; the chain joins by looking up the prior handler on an invoice. All three legs hold at analog level: lot identity (tags), event records at points of work (ledger entries), cross-partner linkage (the sold-to/received-from joins enabling retrieval). **Passes.** Therefore the definition must not require GS1 identifiers, EPCIS event classes, portals, blockchain, or even digital transmission — those are the current era's realizations of the three legs.

**Spreadsheet era:** shared spreadsheets + EDI case-level ASN data in produce chains — passes without cloud/blockchain.

Conclusion: the historical form is the *maintained chain of lot-identity records with recorded movements and partner joins*; the modern platform digitizes capture, join and retrieval. The market name ("platform") names the digitization posture, not a feature set.

## Final Synthesis

A Food Traceability Platform is the food supply chain's standing lot-level movement ledger: it holds food at traceable lot/batch identity, records the tracking events that happen to it as it moves between and transforms at trading partners, and links those records across partner boundaries so any lot can be traced backward and forward along the chain on demand. Its defining core is the joint holding of three structures — traceable lot identity, recorded tracking events, cross-partner linkage with bi-directional retrieval. Everything else regulators and buyers currently demand (KDE/CTE frameworks, GS1/EPCIS vocabularies, validation machinery, labels, portals, blockchain, consumer transparency) is the current market's way of realizing that core, not the core itself. The Type is the standing record the episodic recall event runs on; the two are separable and are sold separately by the same vendors.

Market realization: one Type in three poles — buyer-operated supply-chain network with investigation tooling (FoodLogiQ), retailer-driven validated data-exchange network (ReposiTrak), event-based standards-aligned SaaS with labeling and transparency (Wholechain).
