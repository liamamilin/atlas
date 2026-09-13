# Research Notes — Dangerous Goods Transportation Management

Research date: 2026-09-07
Slug: dangerous-goods-transportation-management
Directory leaf: Dangerous Goods Transportation Management (§18 Transportation, Mobility & Logistics)

---

## Research Goal

Explain what Dangerous Goods Transportation Management software is, who uses it, what core objects it manages, how a dangerous-goods consignment moves through it, what rules govern it, and where its boundary sits against neighboring Application Types (TMS, freight forwarding, air cargo, cold-chain monitoring, hazardous-materials management, global trade management).

---

## Initial Boundary (hypothesis before research)

- Core use: regulatory compliance for transporting hazardous materials — classification of products, determination of what is legal to ship under which mode/regulation, production of legally required transport documents, and the data handoff to carriers/acceptance.
- Users: shippers (chemical/product manufacturers), freight forwarders, carriers/airlines and ground handlers (acceptance side), DG specialists / safety advisors.
- Likely confusion with: Transportation Management System / TMS (carriage execution), Hazardous Materials Management (facility-side EHS), Global Trade Management (customs/sanctions), Cold Chain Transportation Monitoring (sibling special-cargo type), SDS/chemical compliance tools.
- Unknowns: exact core object model; how multiple regulations (air/sea/road/rail) are modeled; where checks happen (shipper vs carrier); document vs data flows.

---

## Research Questions

1. What is the "unit of record"? (per-product classification? per-shipment declaration? both?)
2. What does a classification record contain in regulation vocabulary?
3. How does a consignment get checked against a mode/region regulation, and what happens on failure?
4. What documents/data must be produced, and who receives them?
5. How are multiple regulations (ICAO/IATA air, IMDG sea, ADR road, national rules) handled in one system?
6. How do regulation updates (annual revisions, state/operator variations) propagate?
7. What is the acceptance-side (carrier) workflow vs the creation-side (shipper) workflow?
8. What role do SDSs play vs transport classification?
9. What falls OUT of this Type (facility hazmat management, condition monitoring, customs, carriage execution)?

---

## Representative Products (as actually studied)

Chosen to span the workflow poles with verifiable official documentation. Several well-known market anchors were unreachable (see Sources — access limitations), which degraded the sample; assertion strength was calibrated accordingly.

1. **IATA DG AutoCheck Solutions** (DG Digital + DG AutoCheck + Connect API) — the air-mode DG ecosystem product family: creation side (DG Digital, for shippers/forwarders), acceptance side (DG AutoCheck, for airlines/ground handlers), integration layer (Connect API). Official iata.org product pages. [Reachable]
2. **IATA Dangerous Goods Regulations (DGR)** — not a product but the industry-standard layer that defines the shared objects and flows every product encodes (classification, packing, documentation, handling). Official iata.org. [Reachable]
3. **3E** (Verisk) — classification-content and ERP-embedded pole: **3E Agent for Classification** (GHS + Dangerous Goods transport classification logic delivered into enterprise AI tools), **3E ERC+** (SDS authoring + "market and dangerous goods assessments" inside SAP Product Compliance), **3E Regulatory Intelligence API** (dangerous goods content as licensed data). Official 3eco.com product pages. [Reachable]
4. **Boundary probes** (reachable, used to hold boundaries, not as representatives): VelocityEHS (EHS chemical management — SDS/inventory, no transport product), Sphera (Hazardous Materials Management System for US Government + Performance-Oriented Packaging System — facility/government hazmat side), AEB (trade compliance/TMS/multi-carrier shipping — DG appears as data fields and a carrier-service flag, not as a managed object).
5. **In-repo cross-reference**: research/applications for air-cargo-management (DG/NOTOC as workflow gates inside air cargo systems) and cold-chain-transportation-monitoring (sibling special-cargo boundary), both processed earlier in this production run.

Market anchors that could NOT be verified this pass (no operational claims made about them): Labelmaster DGIS (www 403, support host transport error), DGOffice / DG Software B.V. (root empty shell, /en 404, .net/.nl transport errors), SAP Dangerous Goods Management module (help portal JS shell), FedEx/UPS DG shipping pages (WAF/timeout), Exis Hazcheck (transport error), Camelot DGM (500).

---

## Sources

### Reachable (used)

- IATA — Dangerous Goods (HAZMAT) program page: https://www.iata.org/en/programs/cargo/dangerous-goods/ [fetched 2026-09-07]
- IATA — DG AutoCheck Solutions: https://www.iata.org/en/services/compliance/dg-autocheck/ [fetched 2026-09-07]
- IATA — Dangerous Goods Regulations (DGR) publication page: https://www.iata.org/en/publications/dgr/ [fetched 2026-09-07]
- 3E — 3E Agent for Classification: https://www.3eco.com/ai-solutions/3e-agent-classification/ [fetched 2026-09-07]
- 3E — 3E ERC+ (Integrated Regulatory Content for SAP): https://www.3eco.com/3e-solutions/product-stewardship/3e-erc/ [fetched 2026-09-07]
- 3E — corporate/products root: https://www.3eco.com/ [fetched 2026-09-07]
- VelocityEHS root: https://www.velocityehs.com/ [fetched 2026-09-07] (boundary probe)
- Sphera root + solution catalog: https://sphera.com/ [fetched 2026-09-07] (boundary probe)
- AEB root: https://www.aeb.com/ [fetched 2026-09-07] (boundary probe)
- AEB Help Center search "dangerous goods": https://service.aeb.com/hc/en/search?query=dangerous+goods [fetched 2026-09-07] (boundary probe; 193 hits, mostly customs/trade compliance; Carrier Connect carrier config mentions "Dangerous goods shipping required?"; SAP add-on release notes mention "UN dangerous goods number dangerousGoods... New fields for hazardous goods data")
- In-repo: research/air-cargo-management.md, applications/air-cargo-management.md (Hermes: "ensures your cargo meets Dangerous Goods Regulations according to IATA specifications"; NOTOC workflow gate) [2026-09-07]
- In-repo: research/applications cold-chain-transportation-monitoring.md (mutual boundary: DG = hazard-class compliance vs condition preservation) [2026-09-07]

### Unreachable / abandoned (per network rules, 1–2 attempts then abandon)

- Labelmaster (DGIS) — www 403; support host transport error
- DGOffice / DG Software — dgoffice.net root empty; /en 404; dgsoftware.net + dgsoftware.nl transport errors
- SAP Help Portal — search + viewer return JS shells ("SAP Help Portal | SAP Online Help")
- FedEx DG page — WAF block; UPS hazmat page — timeout; PHMSA (US DOT) — 403; ICAO — 403; IMO IMDG page — 500; UNECE dangerous goods — timeout; Exis Technologies — transport error; Camelot ITLab — 500
- Bing/DDG search — region-hijacked/timeout, unusable for source discovery

### Sourcing limitation statement

The shipper-side standalone software pole (DGIS-class, DGOffice-class) and the ERP-embedded DG module pole (SAP-class) could not be documented from official sources this pass. All shipper-side product mechanics below are therefore anchored on (a) the IATA standard-layer pages, (b) the 3E classification/ERP-embedded product evidence, and (c) canonical inference from the standard's own structure — NOT on the unreachable products. No precise numeric limits, exact field lists, default settings, or named document forms are asserted beyond what the reachable sources state.

---

## Product observations

### A. IATA DGR (standard layer) — evidence layer S (official standard documentation)

The DGR publication page enumerates what air-mode DG compliance consists of. This is the shared object vocabulary every product in the Type encodes:

- **Applicability** — "shipper and operator responsibilities, training, security, incident reporting"
- **Limitations** — "forbidden and hidden goods, storage and transport quantities, transport by post, transport by passengers/crew"
- **Classification** — "explosives, gases, flammable, toxic, oxidizing, radioactive and corrosive and multiple hazard material"
- **Packing Instructions** — per hazard family
- **Packaging Specifications** — "inner, UN, construction and testing, limited quantity"
- **Documentation** — "shipper's declaration, air waybill"
- **Handling** — "storage, loading, inspection, information provision, reporting, training, document retention"
- **Radioactive material** — separate full chapter (transport, limitations, classification, identification, packing, testing, labelling, documentation, handling)

Behavioral facts directly observed:

- Classification responsibility sits with the shipper ("The Regulations place the responsibility for correct classification of dangerous goods on the shipper"); classification may come from the manufacturer, an accredited lab, or the competent authority.
- The DGR is the "field manual" of the ICAO Technical Instructions; airlines can be stricter ("airlines are not obliged to transport a particular substance or product. They are free to impose requirements beyond and above the regulations").
- **State/Operator Variations** are published and updated (page lists live variation updates, e.g. FRG-07, JL-11, Q7-06, QY-06) — jurisdiction/carrier-specific deltas on top of the base regulation.
- The DGR is **published every year** with significant changes; addenda issued between editions. → regulation content is a continuously maintained dataset, not a static body of text.
- Packaging: UN specification packaging vs Limited Quantity provisions have distinct testing/specification regimes (drop/stack tests described in the FAQ).
- SDS relationship: "Material Safety Data Sheets are not required in transport and not required at all for articles"; "many SDS do not provide accurate classification for transport purposes" → transport classification is a distinct determination from workplace hazard communication, and software cannot simply copy it from the SDS.
- Special cargo programs exist as separate regulation products: Battery Shipping Regulations (BSR), Infectious Substances Shipping Regulations (ISSR) — category-specific tuning.
- DGR **Data eList** products and DGR for Electronic Flight Bags exist — the regulation itself ships as data and in-device formats, i.e., the standard is consumed by software as structured content.

### B. IATA DG AutoCheck Solutions (air-mode ecosystem) — evidence layer A (official product pages)

- Positioning: "From Dangerous Goods Declaration (DGD) creation to final acceptance, DG AutoCheck connects shippers, freight forwarders, ground handlers, and airlines through a single trusted validation layer."
- **DG Digital** (creation side): "enabling shippers and freight forwarders to create and submit Dangerous Goods Declarations (DGDs) electronically. By receiving e-DGD data directly into DG AutoCheck, airlines and ground handlers eliminate manual scanning, uploading, and verification of paper documents." Ships with a user manual (PDF, April 2026 version observed).
- **DG AutoCheck** (acceptance side): "Airlines and ground handlers to perform automated acceptance checks and complete digital checklists"; "All stakeholders to work from a single compliance engine aligned with the IATA Dangerous Goods Regulations (DGR)". Advertised speed claim: "Process dangerous goods acceptance checks 50% faster" (vendor marketing figure — L3).
- **Connect API** (integration layer): "seamlessly integrates with Cargo Management Systems and downstream applications, enabling the automated transfer of validated DG data for processes such as NOTOC preparation, ULD build-up, and accounting."
- Scale claims (L3 marketing): 1.3M checks processed; 15 airlines; 35 GHAs; 15 freight forwarders.
- Mobile apps exist (App Store / Google Play).
- Press release (2026-03): "IATA Launches DG Digital to Fully Digitalize Dangerous Goods Declarations."

Interpretation: the air-mode ecosystem makes the DGD a **data object** (e-DGD) rather than only paper, validated once at a shared compliance engine, then consumed downstream by carriage operations (NOTOC = crew notification document, ULD build-up = physical load). Creation → acceptance → downstream operations is one data lifecycle.

### C. 3E (classification content + ERP-embedded pole) — evidence layer A (official product pages)

- **3E Agent for Classification**: "Determine GHS hazard classes and Dangerous Goods transport requirements — packaging, labeling, and shipping — for products and formulations." Rule-grounded: "Every classification is grounded in 3E's curated regulatory intelligence"; explainable: "decision-tree logging and plain-language 'Why' explanations"; audit trail emphasized. Scenario simulation: "simulate how a formulation change, new ingredient, or target-market shift would affect classification and marketability." Comparison across products. Target roles: "product stewards, regulatory affairs specialists, EHS managers, hazard communication and Dangerous Goods specialists, and SDS authors."
  - Interpretation: classification is a **determination act** (rule engine over formulation + regulation), distinct from lookup; the output spans the transport-relevant triad (packaging, labeling, shipping); explainability/audit is a first-class requirement in this domain (a wrong answer "can trigger recalls, block launches, or fail audits").
- **3E ERC+**: "Author and publish SDS, conduct market and dangerous goods assessments, notify Poison Centres" inside SAP Product Compliance; "exclusive provider of embedded regulatory content for SAP S/4HANA for product compliance" (marketing positioning, L3).
- **3E Regulatory Intelligence API**: "regulatory content such as list substance data, multilingual phrases, and dangerous goods content from anywhere" — DG content licensed as data for embedding in other systems.
- Interpretation: the ERP/suite pole realizes DG management as (a) a dangerous-goods **assessment step** inside product-compliance workflows and (b) vendor-supplied, continuously updated **regulatory content** feeding ERP shipping flows — the same pattern the GTM pass found for customs content.

### D. Boundary probes

- **VelocityEHS** (full EHS platform): chemical management = SDS management, chemical inventory, GHS secondary labeling, emergency-response services. No dangerous-goods *transport* product on the site → facility-side hazmat management is a different Type; transport classification is not its center.
- **Sphera**: ships "Hazardous Materials Management" (Hazardous Material Management System for the US Government; Hazardous Material Information Resource System; Performance-Oriented Packaging System; Hazardous Waste Management) — storage/worker/packaging-certification side, government-flavored. Again facility-side; transport compliance not the spine.
- **AEB** (trade compliance + TMS + multi-carrier shipping): help center shows DG appearing as (1) a carrier/service configuration flag ("Dangerous goods shipping required?") in multi-carrier shipping, and (2) DG data fields in customs/SAP add-on flows ("UN dangerous goods number dangerousGoods. New fields for hazardous goods data"). → In carriage-execution and customs systems, DG is a **field/flag consumed**, not the managed object; the compliance determination machinery lives in dedicated DG products.
- **air-cargo-management (in-repo)**: airline/handler/forwarder systems embed DG as workflow gates ("Shipments declared as dangerous goods must satisfy the industry's Dangerous Goods Regulations before acceptance, and the flight crew must be notified of what is aboard (the NOTOC)") — carriage systems consume the DG determination; one sampled vendor documents DG-compliance checking per IATA specs.

### E. Negative-space observations (what the reachable evidence never shows)

- No reachable source shows DG software doing carriage planning, tendering, freight-cost settlement (TMS jobs).
- No reachable source shows in-transit condition monitoring (cold-chain's job).
- No reachable source shows customs declaration production (GTM/customs job) — DG and customs outputs coexist on the same shipment but are different documents/objects.
- No reachable source shows facility storage segregation or SDS authoring as the center (facility-side tools' job).

---

## Cross-product Comparison

| Structure | IATA DGR (standard) | DG AutoCheck/DG Digital | 3E classification/ERP | Boundary probes |
|---|---|---|---|---|
| Classification in regulation vocabulary (UN no., proper shipping name, class, packing group) | yes (Classification chapter) | yes (compliance engine aligned to DGR) | yes ("GHS hazard and Dangerous Goods transport classification logic") | consumed as fields (AEB) |
| Classification as rule-driven determination, not lookup | implied by DGR structure | yes (validation engine) | yes (decision-tree, explainable) | — |
| Per-consignment compliance determination (mode/qty/packaging) | implied (Limitations, Packing) | yes (acceptance check vs DGR) | yes ("packaging, labeling, and shipping" requirements determination) | flag consumed by carriers |
| Transport document production (shipper's declaration / DGD) | Documentation chapter | yes (e-DGD creation) | assessment inside suite; content via API | fields only |
| Carrier/acceptance handoff | Handling (inspection, information provision) | yes (acceptance checklists, digital checklists) | — | gates in air-cargo systems |
| Multi-regulation coverage | air (ICAO TI/DGR); State/Operator variations | DGR-aligned | "across global markets" (claim, L2) | — |
| Regulation content as maintained data service | DGR annual editions; Data eList | engine updated to DGR | curated regulatory intelligence + API | — |
| Downstream operational data flows (NOTOC, ULD, accounting) | Handling (information provision) | Connect API explicit | — | NOTOC gates in air cargo |
| Explainability / audit trail | document retention duty | validation history implied | explicit (decision-tree logging, audit trail) | — |
| Scenario simulation ("what if") | — | — | explicit (formulation-change simulation) | — |
| SDS authoring / facility inventory | explicitly NOT required in transport | — | adjacent (separate products) | the centers of VelocityEHS/Sphera |

Stable cross-product commonality (with the caveat that the directly-verified product sample is small): the classification record + the determination act + the document/data handoff appear in every reachable witness, including the standard itself and the boundary probes' consumed fields.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three structures, jointly necessary:

1. **The dangerous goods classification record** — a maintained, per-product (or per-material/formulation) record expressing the product's hazard identity in the vocabulary of transport regulation: UN number, proper shipping name, hazard class/division, packing group (plus the regulation's per-regime special data). It is master data: it exists before and after any shipment and is maintained as regulations change.
   - Remove → generic shipping/logistics software with a "hazmat" checkbox.
2. **The regulation-scoped compliance determination of a specific consignment** — applying the rules of the applicable regulation(s) for the intended mode/region/quantity to the actual consignment data: whether it may be carried, under which quantity provisions, in which packaging, with which marking/labeling, and what variations apply. The output is a recorded determination attached to the shipment (validated/accepted state), not a static lookup answer.
   - Remove → a classification reference database (an ERG-class lookup), not transport management.
3. **The compliant transport documentation and carrier handoff** — production of the legally required shipping paper (the shipper's DG declaration in air terms; mode-equivalent documents elsewhere) from classification + consignment data, and delivery of the required data/paperwork to the carrier/operator side that must accept and carry the goods.
   - Remove → a hazmat knowledge base; the Type stops being *transportation management*.

The unit of work is the **consignment (shipment)**; the unit of record that persists across shipments is the **classification**. Both are needed.

Historical/market-sample check: the paper era (printed DGR/49 CFR books, typed/handwritten shipper's declarations, pre-printed labels, manual acceptance inspection) satisfies structures 1–3 without any digital machinery — classification data kept by the shipper, determination done by a trained person against the book, document produced on paper and handed to the airline. This pass could not research the PC-era DG software generation directly (unreachable), so the minimal-software pole is stated as canonical inference (layer C): a maintained classification dataset + document production is the smallest recognizable software realization. L0 deliberately excludes: label printers, placards, emergency phone services, training records, cloud delivery, any specific mode.

### L1 — Common Mature Structure

- **Multi-regulation, multi-mode coverage** — one system holding classification/determination content keyed by mode and region (air/sea/road/rail; national rules). (Direct for air + "global markets" claim at 3E; cross-product commonality asserted at moderate strength only.)
- **Regulation content as a maintained service** — vendor-curated, regularly updated regulatory datasets (annual DGR editions + addenda on the standard side; curated content/API on the product side); content change → re-determination impact on products.
- **Quantity-limit machinery** — limited/excepted-quantity regimes, packaging specification tiers (UN spec vs limited quantity), forbidden/hidden-goods determinations.
- **Marking/labeling output support** — labels/marks as regulated outputs of the determination (documented as "labeling" requirements at 3E and as a DGR/label-product ecosystem on the standard side).
- **Acceptance checking** — automated or assisted validation of documents/data against the regulation before carriage (airline/GHA digital checklists; shipper-side pre-checks in creation tools).
- **Downstream operational data flow** — validated DG data feeding carriage operations (NOTOC preparation, ULD build-up, accounting via Connect API; DG gates inside air-cargo systems; carrier service flags in multi-carrier shipping).
- **State/operator/carrier variation handling** — jurisdiction- and carrier-specific deltas applied on top of base regulation.
- **Emergency-response information accompanying shipments** — documented at standard-layer as information-provision duties; specific phone-number mandates NOT directly verified this pass (kept general).
- **Audit trail and record retention** — regulation imposes document-retention duties (DGR Handling chapter); products emphasize audit trails/explainability.
- **Training/competency records** — training is an applicability duty in the DGR; competency-based training guidance exists; DG software commonly tracks DG training (kept at L1, product-side tracking not directly observed in the reachable sample).
- **Integration spine** — ERP/order systems (classification master data feeding shipping), TMS/multi-carrier (DG fields/flags), e-DGD exchange, content APIs.

### L2 — Variant / Optional Structure

- Mode-specific depth (air-acceptance ecosystem vs sea/road/rail tooling; separate special-cargo regulation products: batteries, infectious substances, radioactive).
- Packaging-side tooling (packaging specification/testing management — partially facility-side, boundary with hazmat management).
- AI classification assistance with explainable rule trees; conversational classification; scenario simulation (current-era; 3E Agent direct).
- SDS-authoring adjacency (same vendors, different product line — the SDS↔transport-classification gap is documented, so the two remain distinct determinations).
- Facility-side extensions: storage segregation, hazmat inventory (belong to Hazardous Materials Management).
- Emergency-response service integration (third-party response providers) — not directly observed; plausible, unverified.
- Incident reporting support (DGR duty; product realization not observed).
- Paper-to-digital migration posture (scan-and-verify vs native e-DGD — directly documented at IATA as the before/after).

### L3 — Vendor-specific (research notes only)

- DG AutoCheck "50% faster" claim; 1.3M checks / 15 airlines / 35 GHAs / 15 forwarders counts.
- DG Digital user manual as separate product artifact; Connect API name; mobile app distribution.
- 3E "exclusive provider of embedded regulatory content for SAP S/4HANA for product compliance"; Supplier SDS Loader "reduces manual effort by up to 70%" (marketing); 3E Agent product naming; 3E ERC+ naming.
- Hermes (air-cargo vendor) DG-compliance checking wording.
- AEB-specific field names (dangerousGoods code lists) in SAP add-on release notes.

---

## Vendor-specific Findings

- IATA's products are also the *standard owner's* products — a unique market position (regulator-adjacent vendor). Its compliance engine is by construction DGR-aligned; independent shipper-side tools implement the same regulation from the publication/data-eList.
- 3E's pole monetizes classification *content and logic* (AI-agent delivery, API supply, ERP embedding) rather than shipping execution — classification-as-a-service.
- The air ecosystem is the only mode with a verified shared digital acceptance layer; whether sea/road equivalents exist as products was not verifiable this pass.

---

## Boundary Findings

- **vs Transportation Management System / TMS**: TMS plans, tenders, executes and settles carriage. DG management determines whether/how hazmat may be carried and produces the required papers/data. Removal test: strip the regulatory determination+documents → TMS remains; strip route/rate/execution → DG management remains. In reachable evidence TMS/multi-carrier products *consume* DG as fields/flags ("Dangerous goods shipping required?"), confirming complementarity. Complementary handoff: classification+consignment data flow into booking; carrier acceptance feeds status back.
- **vs Freight Forwarding System / Air Cargo Management**: forwarder/airline systems move the consignment (booking, AWB, carriage lifecycle). DG management is the compliance spine *inside* that flow — a gate and a document (air-cargo research: DG acceptance gate + NOTOC; DG Digital/AutoCheck sits exactly at that gate). Removal test: remove carriage execution/booking/AWB lifecycle → DG management stands; remove DG determination → air cargo still runs (until refused at acceptance).
- **vs Cold Chain Transportation Monitoring**: sibling special-cargo type. DG = hazard-class compliance (classification, documentation, packaging/labeling); cold chain = condition preservation (measured environment vs requirement). Mutually held boundary, recorded on both sides in this production run.
- **vs Hazardous Materials Management (§21)**: facility-side chemical inventory/SDS/storage/worker safety. The bridge object is the classification, but the determinations differ: workplace hazard communication (GHS) vs transport classification (mode regulations) — the standard explicitly warns SDSs often do not carry accurate transport classification. Removal test: remove movement/consignment → hazmat management; remove facility/inventory/SDS → DG transport management.
- **vs Global Trade Management (§10, processed)**: structurally similar three-part pattern (product master classification → transaction-level determination → regulatory output), but the regulatory object differs: trade/customs (tariff codes, origin, sanctions, licenses; output = customs declarations) vs transport safety (hazard class, packing group, quantity limits; output = DG transport documents). Both may touch the same shipment; AEB evidence shows DG data fields flowing inside customs/SAP add-on contexts without DG management being the product. Removal test: change the regulatory vocabulary and authority — trade compliance tools cannot produce a DG declaration and vice versa.
- **vs SDS authoring / chemical compliance tools**: adjacent capability, not the Type (see above).
- **Prohibited-goods overlap**: "forbidden and hidden goods" determination is DG-specific; generic embargoes belong to GTM.

No taxonomy problem found: the leaf is a genuine, distinct Type (not an alias/variant/capability). One packaging note: the leaf name says "Transportation Management", and the market also sells the acceptance-side pole under "DG compliance/acceptance" names — same Type, opposite side of the consignment.

---

## Uncertainties

1. **Standalone shipper-side pole unverifiable** (DGIS/DGOffice unreachable). All claims about creation-side products are anchored on DG Digital (which is creation-side and verified) + canonical inference. No screen-level workflow claims for standalone shippers' tools.
2. **ERP-embedded DG module specifics unverified** (SAP DG module unreachable); the ERP pole is evidenced indirectly (3E ERC+ dangerous-goods assessments inside SAP Product Compliance; DG data fields in SAP add-on flows).
3. **Non-air modes** (IMDG sea, ADR road, RID rail) not directly documented (regulator sites unreachable); multi-mode coverage stated at moderate strength, grounded in the 3E "global markets" claim and market structure.
4. **Emergency-response information specifics** (e.g., mandated emergency phone on documents) not directly verified; kept general ("information provision" duty documented at standard layer).
5. **Exact DGD field lists / document templates** not asserted (would require product manuals).
6. **Historical software generation** (1980s–2000s PC-era DG tools) not directly researched; historical check performed conceptually against the paper era.
7. Whether road/sea modes have shared digital acceptance ecosystems analogous to DG AutoCheck — unknown.

---

## Final Synthesis

A Dangerous Goods Transportation Management application is the regulatory-compliance system of record for moving hazardous goods: it holds each product's dangerous-goods classification as maintained master data in the vocabulary of the transport regulations; it determines, per consignment, what the applicable regulation(s) permit and require (mode/region/quantity → packaging, marking/labeling, limitations, variations, forbidden determinations) as a recorded decision; and it produces the legally required transport documentation and data handoff through which the carrier accepts and carries the goods. Mature products add multi-mode regulation libraries under continuous content update, acceptance automation, downstream operational data flows, variation handling, emergency-response information, audit/retention, training records, and deep integration into ERP/TMS/e-commerce shipping flows. The Type's center of gravity is the hazard-compliance spine of the consignment — not carriage execution (TMS/forwarding), not condition preservation (cold chain), not facility chemical management, not customs/trade compliance — though it shares the *pattern* (master classification → transaction determination → regulatory output) with trade compliance while differing entirely in regulatory object.

L0 one-liner (for STATUS.md): per-product DG classification records (regulation vocabulary, maintained) + regulation-scoped per-consignment compliance determination (limits/packaging/labels/forbidden, recorded) + production of the legally required transport documents and carrier-acceptance data handoff.
