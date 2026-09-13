# Research Notes — Artwork Exhibition Logistics

Research date: 2026-09-06
Slug: `artwork-exhibition-logistics`
Directory leaf: "Artwork Exhibition Logistics" (§27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what software for the physical logistics of artwork exhibitions actually does — its central objects, workflows, states and rules — well enough to write a vendor-neutral Application Document, and to resolve the taxonomy question raised by the neighborhood: is "Artwork Exhibition Logistics" an independent product category, or a logistics structure that lives as a module inside museum collection systems and gallery suites, with specialized point tools at the edges?

## Initial Boundary

Working hypothesis before research:

- Artwork exhibition logistics = coordinating the physical movement and handling of specific artworks for display occasions: assembling the checklist of works to show, arranging packing and transport between locations (studio/storage → venue → return or onward), tracking each work's current location and movement history, documenting condition at each handover, and restoring works to their home locations afterwards.
- Primary operators: museum registrars and collections managers, gallery/exhibition managers and registrars, artist studio managers, and the art handlers/shippers they coordinate with.
- Nearest neighbors in the directory (all siblings under §27): Exhibition Planning Platform (upstream curatorial/production planning), Exhibition Installation Management (venue-side install work), Museum Object Movement Management (general internal location tracking), Museum Loan Management (the legal/agreement layer of borrowing and lending), Art Gallery Management / Artwork Consignment Management (commercial inventory custody basis). Adjacent outside §27: Convention / Exhibition Management (event industry — different object world), art shipping platforms (transport execution without a display occasion).
- Prior cross-references from the two adjacent passes already processed: artwork-consignment-management (commercial custody basis; artist side "send your artworks to exhibitions with professional consignments"), art-gallery-management (consignment as basis layer; movement history).

## Research Questions

1. What is the central object — the exhibition, the movement/shipment, the artwork's location state, or the handover document?
2. How is a work's journey modeled: checklist → prepare → out → venue → close → return/forward?
3. Which parties exist in the system: organizer/registrar, venue/lender, shipper/carrier, courier, insurer, conservator?
4. What documentation is generated and attached to moves (condition reports, dispatch/receipt, in/out protocols, packing requirements)?
5. Is the capability standalone, or packaged inside museum collection systems / gallery suites? Do specialized point tools exist for single parts?
6. How do commercial display contexts (art fairs, gallery shows) differ from institutional loans/touring exhibitions?
7. Historical check: would a pre-digital registrar's operation (paper checklists, condition forms, shipping logs, FileMaker-era gallery databases) satisfy the same core?

## Representative Products

Selected for market representability, documentation accessibility, different customer levels and different product philosophies:

| Product | Segment / tier | Philosophy | Evidence accessed |
|---|---|---|---|
| **Gallery Systems — TMS Collections** | Museum incumbent (40+ years; large institutions worldwide) | The collection database as the operational hub; Exhibitions / Loans / Shipping as sibling modules beside the object record | Tier 2 product/roles pages + vendor-authored workflow article (module-level evidence) |
| **Zetcom — MuseumPlus** | European museum incumbent (Bern; ~2,500 institutions) | Exhibition Management as a named module: coordination of participants, venues, lenders + in/out protocols; Contracts module for exhibition/loan agreements | Tier 2 product page (module descriptions) |
| **Artlogic** | Commercial gallery/artist suite (UK; cloud SaaS) | All-in-one gallery management; exhibitions/fairs as records + artwork Location/Shipping tab with movement history; transport execution via integration | Tier 1 public help center (location records, ARTA integration, art fair preparation guide, fair/exhibition records) |
| **ARTA** | Transport-execution platform (art/luxury/collectibles shipping: quoting, booking, insurance, tracking) | API-first logistics execution for unique high-value items; no display occasion — the boundary pole | Tier 1 public manual (shipment lifecycle, logistics guide structure) + Tier 2 site |
| **Articheck** | Condition-reporting / transit-visibility platform (galleries, museums, conservators, shippers) | Digital condition reports + "Transit Hub" visibility of art in situ, transit, storage; shared with loan/travelling-exhibition partners | Tier 2 official site (product pages, role pages, registrar testimonials) |

Considered and excluded (network-limitation rule):

- **Vernon Systems** (small-museum pole, NZ): www.vernonsystems.com returned an empty response on 2026-09-06 — dropped after one failure; no claims made.
- **Zetcom help center** (help.zetcom.com): transport error on first attempt — abandoned; MuseumPlus evidence stays at Tier-2 module-description level.
- **Collections Trust Spectrum pages** (the UK museum standard's "Transportation" procedure would have provided standards-level vocabulary): two different URL patterns returned 404 — abandoned; no Spectrum-procedure-specific claims are made.
- Gallery Systems and museum help centers generally sit behind client logins (community portal); TMS evidence is therefore module-level rather than screen-level.

## Sources

Tier 1 (official operational documentation):

- Artlogic Support — "Finding, creating and updating artwork location details" — https://support.artlogic.net/hc/en-gb/articles/360010220119 (Location/Shipping tab; Current location + location detail + date; "Add to location history" ordered movement history; location reports document current location; bulk "Update multiple" for a collection moving to an art fair booth; location records & value lists; "Last examined by" field)
- Artlogic Support — "Integrate with Arta" — https://support.artlogic.net/hc/en-gb/articles/360013420399 (request shipping quotes from ARTA through Artlogic; select artworks → Request ARTA shipping quote → shipment details → submit → finish in ARTA account)
- Artlogic Support — "How to prepare your systems ahead of an art fair" — https://support.artlogic.net/hc/en-gb/articles/16269347601820 (fair timeline; Art Fairs record + Exhibition Records; artwork lists for the fair; website/app/Private View publication side)
- Arta Manual — "Shipment lifecycle" — https://manual.arta.io/guides/getting-started/shipment-lifecycle (quote → book/pay → release, tracking, delivery; transit insurance; cross-border customs/duties; packing decisions: self-pack/crates vs specialized shipper)
- Arta Manual — "Logistics services" — https://manual.arta.io/guides/logistics (component vocabulary: Quote Requests, Quotes, Services, Shipments, Statuses; products: Self Ship, Parcel, Select, Premium; fulfillment: collection, exceptions, communications, tracking, destination services)

Tier 2 (official product pages / vendor-authored operational articles):

- Gallery Systems — "Software for Registrars" — https://www.gallerysystems.com/roles/software-for-registrars/ ("Efficiently manage exhibitions, with up-to-date data on object storage, insurance policies, and shipping status"; "Access shipping requirements in seconds to guarantee each collection object is fully transport-ready"; "Export the latest data as targeted reports and share them with partnering museums and art handlers"; condition reports as linked media)
- Gallery Systems — "Enhancing Museum Workflows with the TMS Suite" — https://www.gallerysystems.com/enhancing-museum-workflows-with-tms-suite/ (module inventory: Loans Module — "requests, approvals, agreements sent/received, and return schedules"; Exhibitions Module — "monitor object statuses, review approvals, and track deliverables"; Shipping Module — "shipment schedules, carrier details, and actual delivery dates"; Packages "ideal for exhibition checklists"; status flags such as "Condition Report Needed")
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/ ("Exhibition Management — Coordination of participants, venues and lenders, as well as input and output protocols"; "Contracts — Management of agreements and contracts relating to exhibitions, loans and collection objects")
- Arta — https://www.shiparta.com/ (solutions: marketplaces, merchants, auction sellers; products: Shipping, Insurance, Tracking, Integrations, Deliver Duty Paid)
- Articheck — https://articheck.com/ (condition reports; "Transit Hub" — "complete visibility of art in situ, transit, and storage"; solutions for Galleries / Museums / Conservators / Shippers; sharing with "partners on loans or travelling exhibitions"; audit trail; registrar testimonials incl. KODE Art Museums collection registrar on updates for "each move on one device")

Prior in-repo evidence (adjacent passes, 2026-09-06):

- research/artwork-consignment-management.md (Art Galleria artist side: "Send your artworks to exhibitions with professional consignments and keep tabs where your artworks are and when they're due back"; ArtCloud location semantics; Artlogic movement history)
- research/art-gallery-management.md (gallery inventory + movement/location tracking context)

## Product Observations

### Gallery Systems — TMS Collections (museum pole)

Evidence layer: B at module level (official product pages + vendor-authored operational article; no screen-level help docs reachable — client community is login-gated).

Key observations:

- The registrar is named as the core operating role: "juggling between tracking thousands of objects and working with a diverse team of colleagues, contractors, vendors, art handlers, and other registrars."
- Registrar value bullets center exhibition logistics: "Efficiently manage exhibitions, with up-to-date data on object storage, insurance policies, and shipping status"; "Access shipping requirements in seconds to guarantee each collection object is fully transport-ready"; "Export the latest data as targeted reports and share them with partnering museums and art handlers"; "Link unlimited media to your object records, such as condition reports and other integral documentation."
- Module structure (vendor-authored workflow article): **Loans Module** — "Track requests, approvals, agreements sent/received, and return schedules." **Exhibitions Module** — "Monitor object statuses, review approvals, and track deliverables." **Shipping Module** — "Maintain shipment schedules, carrier details, and actual delivery dates." **Projects Module** — customizable initiatives.
- Checklist support: "Packages: Compile custom lists of records for collaborative work — ideal for exhibition checklists."
- Readiness flags: "Status Flags: Apply prominent, customizable indicators to records that need attention — Needs Photography, Missing Required Data, **Condition Report Needed**. Flags can be cleared individually or in batches when work is complete."
- Workflow framing: an exhibition "might involve dozens of departments with tightly linked deliverables"; workflow tools (saved queries, flags, batch updates, flex fields) turn the CMS into "the central hub for your projects."
- Spectrum compliance is advertised (Collections Trust partner badge) — the system is aligned to museum documentation standards, though the standard's own pages could not be fetched.

### Zetcom — MuseumPlus (European museum pole)

Evidence layer: B at module level (official product page only).

Key observations:

- "Exhibition Management — Coordination of participants, venues and lenders, as well as input and output protocols." In/out protocols = the documented movement of works into and out of the exhibition context.
- "Contracts — Management of agreements and contracts relating to exhibitions, loans and collection objects" — the agreement layer is a sibling module, distinct from the exhibition module.
- Broader context: collection management core + customer service + digital assets + contracts + exhibition management + additional modules; SaaS option.

### Artlogic (commercial gallery/artist pole — Tier 1)

Evidence layer: A (public help center).

Key observations:

- **Location/Shipping tab** on every artwork record: "The current location of your artwork will be documented in the first three fields of the Location section" (current location, location detail, date). Supporting fields include notes and "Last examined by".
- **Movement history as first-class structure**: "Add to location history" appends the previous current location to an ordered history — "Each location added will appear in order of modification, with the most recent at the top." Moving a work = writing a new current location and pushing the old one into history. Dates are optional but recommended "to build a clearer timeline of your artworks' movements."
- **Location reports** document the current location (not history); locations can be standardized as location records/value lists to avoid name variants; QR-code stock updating ties physical inventory checks to location records.
- **Bulk movement for display occasions**: the Update multiple tool is illustrated with the exact exhibition scenario — "batch update artworks in one action, for example when a collection of artworks moves from the gallery to an art fair booth."
- **Exhibition/fair records**: the fair prep guide instructs creating "your art fair or exhibition record" (Art Fairs help note + Exhibition Records help note) and attaching the selected works; the guide's concern is presentation/publication (website, app, Private View links) — the logistics side of the fair appears as (a) location changes and (b) shipping quotes.
- **Transport execution via integration**: "Integrate with Arta — request a shipping quote from ARTA through Artlogic": select artworks → "Create... > Documents/Reports > Request ARTA shipping quote" → prepare shipment details → submit → "log in to your ARTA account to finish." Transport execution is delegated to a specialized platform, not built in.
- **Condition reporting via integration**: Articheck is a named integration; the artwork record carries "Last examined by" on the location entry.
- Context from the consignment pass (same vendor): consignments/loans tracked as basis layers with locations and movement history; artwork movement history is a core gallery-suite capability.

### ARTA (transport-execution pole — boundary product)

Evidence layer: A for mechanics (public manual), Tier 2 for positioning.

Key observations:

- Positioning: "Purpose built commerce technology for the art, luxury and collectibles market"; solutions are Marketplaces, Merchants, Auction Sellers — i.e., **post-sale/commerce shipping**, not exhibitions. No display occasion exists anywhere in its model.
- Shipment lifecycle (manual): 1) get shipping quotes from one or more vendors; 2) book and pay for the selected quote; 3) coordinate release and delivery of the packed items while providing tracking/status visibility. Insurance (transit insurance) and cross-border requirements (customs documentation, duties/taxes) are first-class considerations.
- Packing decision is explicit: self-pack (crates, protective cushioning) vs specialized shipper who manages packing and collection.
- Component vocabulary: Quote Requests, Quotes, Services, Shipments, Statuses; products Self Ship / Parcel / Select / Premium; fulfillment surfaces: collection, exceptions, communications, tracking, destination services.
- Boundary relevance: ARTA demonstrates what "art transport execution" looks like when the exhibition context is removed — quotes, booking, tracking, insurance. Exhibition-logistics software integrates with exactly this layer (Artlogic does).

### Articheck (condition-documentation pole — boundary/adjacent product)

Evidence layer: B (official site: product/role pages, customer testimonials from named registrars).

Key observations:

- Dedicated product for the handover documentation layer: "Easy to use condition reports and complete visibility of art in situ, transit and storage — help our customers avoid disputes, reduce liability, and protect artwork."
- **Transit Hub**: updates on "each move on one device compiled in one channel" (collection registrar, KODE Art Museums); "Transit Hub also saved us time from not travelling" — i.e., the courier-accompaniment need partially replaced by shared transit visibility.
- Roles served: Galleries, Museums, Conservators, **Shippers** — the same documentation object is shared across the chain.
- Sharing model: "Other people will only see your reports if you purposefully choose to share them, for example when collaborating with partners on loans or travelling exhibitions. You control exactly who has access, to what extent, and for how long." Cross-party collaboration around a specific movement is the product's core sharing scenario.
- "Proof of due care & diligence — establish a legally verifiable audit trail for your objects."
- Marketing numbers on the site (e.g., "up to 75% faster") are vendor claims — not used as facts.

### Cross-product synthesis observations

- The **artwork record with current location + movement history** is the substrate everywhere: Artlogic explicitly (Tier 1), TMS as "object storage / shipping status" data on object records, Articheck as per-move updates per object, ARTA as per-shipment item tracking.
- The **display occasion** (exhibition record / fair record) is the organizing container on the organizer side: Artlogic (Art Fairs + Exhibition Records), TMS (Exhibitions Module), Zetcom (Exhibition Management).
- The **checklist** (which works are in the occasion) exists as Packages in TMS (explicitly "ideal for exhibition checklists") and as artwork lists attached to fair/exhibition records in Artlogic.
- **Readiness and handover documentation** is a shared discipline: condition reports as linked media (TMS), a "Condition Report Needed" flag (TMS), "Last examined by" (Artlogic), the entire Articheck product, and museum in/out protocols (Zetcom).
- **Transport execution** is either tracked at summary level inside the operator's system (TMS Shipping Module: schedules, carriers, actual delivery dates) or delegated to a specialized platform (Artlogic→ARTA; ARTA's own quote→book→track loop).
- **The agreement layer is adjacent, not central**: TMS Loans Module and Zetcom Contracts handle the legal structure (requests, approvals, agreements, return schedules) as a sibling module; logistics picks up where the agreement ends.
- **Insurance** appears in all poles (TMS registrar page: insurance policies; ARTA: transit insurance; Articheck: risk/liability framing) — always as a consideration attached to the movement, never as the organizing structure.
- **Two-sided custody**: lender and borrower sides exist as separate operator worlds (TMS "share reports with partnering museums"; Articheck shared reports "with partners on loans or travelling exhibitions"); each side records custody from its own perspective — consistent with the two-sided divergence pattern documented in the consignment pass for ArtCloud.

## Cross-product Comparison

| Structure | TMS Collections | MuseumPlus | Artlogic | ARTA | Articheck | Assessment |
|---|---|---|---|---|---|---|
| Unique artwork record as the tracked unit (one per physical piece) | ✔ (object records) | ✔ (object cataloging) | ✔ (artwork records, Tier 1) | ✔ (items within shipments) | ✔ (artwork entities) | Core (all) |
| Current location + movement history per work | ✔ ("object storage / shipping status" on records; module-level) | implied (in/out protocols) | ✔ explicit (Current location + Add to location history; Tier 1) | per-shipment only (no home-location model) | ✔ ("in situ, transit, storage"; per-move updates) | Core for exhibition-logistics operators (organizer-side products); execution platforms carry only per-shipment state |
| Display occasion as organizing container (exhibition/fair record with works list) | ✔ (Exhibitions Module; Packages as checklists) | ✔ (Exhibition Management module) | ✔ (Art Fairs + Exhibition Records; artwork lists) | ✘ (no exhibition concept) | partial (travelling exhibitions as sharing scenario) | Core for this Type; its absence defines the execution-platform boundary |
| Checklist of works for the occasion | ✔ (Packages "ideal for exhibition checklists") | implied (exhibition module) | ✔ (fair/exhibition records carry artworks) | ✘ | ✘ | Core (all organizer-side products) |
| Movement/transport coordination (schedules, carriers, booking) | ✔ (Shipping Module: schedules, carrier details, actual delivery dates) | implied (in/out protocols) | via integration (ARTA quote request; Tier 1) | ✔ (quote → book → track; Tier 1) | visibility only | Core (form varies: built-in module vs delegated execution) |
| Handover documentation (condition at moves, dispatch/receipt, in/out protocols) | ✔ (condition reports as media; "Condition Report Needed" flag) | ✔ ("input and output protocols") | ✔ ("Last examined by"; Articheck integration) | ✘ (no condition layer) | ✔ (the whole product) | Core (distributed across organizer system + specialized tools) |
| Readiness state on the work ("transport-ready", flags) | ✔ (status flags; "fully transport-ready") | not observed | not observed (readiness implied by prep guides) | ✘ | ✘ | Common (museum-side; keep qualitative) |
| Insurance as an attached consideration | ✔ (insurance policies data; policy management) | not observed | not observed | ✔ (transit insurance product) | ✔ (risk/liability framing) | Common (attachment, not organizer) |
| Agreements/loans layer (approvals, terms, return schedules) | ✔ (Loans Module) | ✔ (Contracts module) | ✔ (consignments/loans as basis layers) | ✘ | ✘ | Adjacent sibling (separate modules; not this Type's core) |
| Cross-party sharing of logistics records (partner museums, shippers) | ✔ ("share reports with partnering museums and art handlers") | ✔ (participants/lenders coordination) | ✔ (integrations; quote submission to ARTA) | ✔ (buyer/buyer-side notifications) | ✔ (shared reports with loan/travelling-exhibition partners) | Common (all) |
| Packing/crating requirements | ✔ ("shipping requirements... fully transport-ready") | not observed | not observed | ✔ (self-pack vs specialized shipper; packing standards) | ✘ | Common |
| Courier accompaniment / transit visibility | not observed | not observed | not observed | ✔ (tracking) | ✔ (Transit Hub; "saved us from not travelling") | Common (modern implementations; form varies) |
| Commercial display context (fairs/booths) as first-class variant | ✘ (museum focus) | ✘ | ✔ (fairs as records + location moves) | ✔ (gallery/marketplace commerce) | ✔ (galleries as a role) | Variant (segment-dependent) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software is not recognizable as artwork exhibition logistics:

```text
Display occasion (exhibition/fair context: venue(s) + dates)
└── Checklist of specific works gathered for the occasion
    └── Per-work movement chain organized by the occasion
        (origin → venue → return or onward to the next occasion)
        └── Custody continuity: the work's current location is
            always known and each change is recorded into history
        └── Handover documentation attached to each leg
            (condition at release/receipt, dispatch/receipt record)
```

Four invariants:

1. **A display occasion that gathers works** — the exhibition (or fair) is a bounded context with venue(s) and dates that pulls specific works into a checklist. Without it, movement tracking exists but exhibition logistics does not — the software is generic object movement or shipping.
2. **A per-work movement chain organized by the occasion** — works travel out to the venue and back or onward; the chain is composed of legs (release, transport, receipt) attributed to the occasion. Without the movement chain, the software is exhibition planning or installation only.
3. **Custody continuity (current location + history)** — at any moment the system can answer "where is this work and how did it get there." Without continuity of custody, handover documentation and dispute resolution collapse, and the registrar function the software serves cannot be operated.
4. **Handover documentation attached to movements** — condition statements and dispatch/receipt records are tied to the specific leg, not floating. Without documented handover, the operator cannot prove due care or allocate liability — the reason this documentation is inseparable from the movement itself.

Historical check (§24 applied): a 1990s registrar or gallery operating on paper or FileMaker (the ArtBase lineage documented in prior passes) tracks exactly this core — an exhibition checklist, a current-location column per work, a movement log, condition forms signed at each handover, shipping records with carriers and dates. Integrations, quote APIs, QR codes, tracking pages, transit dashboards and insurance products are modern implementations, not definitional.

### L1 — Common Mature Structure

Present in essentially all mature modern implementations; expected by the market but not definitional:

- transport coordination at summary level: shipment schedules, carrier details, actual delivery dates (built-in module) or delegated execution via integration
- readiness management: per-work shipping requirements, transport-ready states, flags such as "condition report needed"
- generated logistics documents: location reports, condition report templates, packing/shipping requirement sheets, in/out protocols
- location standardization (location records, value lists) and bulk location updates for batch movements to an occasion
- insurance considerations attached to legs (policy values on records; transit insurance for shipments)
- cross-party distribution of logistics records (reports to partner museums, lenders, art handlers; shared condition/transit records)
- packing/crating as a modeled step (requirements recorded; specialized shippers handle execution)
- agreements layer adjacency: loans/consignments as the commercial/legal basis that usually triggers the movement
- reporting: movement history timelines, location reports, exhibition deliverable tracking

### L2 — Variant / Optional Structure

- segment variants: institutional (loans, couriers, condition protocols, touring rotation) vs commercial (fairs, booth moves, quote-driven shipping, sales overlays) vs artist studio (outbound shipments to shows, "when they're due back")
- transit visibility form: none / carrier tracking pages / shared transit hub per move (courier accompaniment as the pre-digital baseline)
- execution locus: transport execution handled inside the operator system (summary tracking) vs delegated to specialized platforms via integration/API
- cross-border logistics (customs documentation, duties) — depth varies by market reach
- publication adjacency: exhibition/fair records doubling as website/app content (commercial suites)
- packing and storage as included capabilities (some operators run their own storage/QR stock management)

### L3 — Vendor-specific (research notes only)

- TMS Collections: Packages (exhibition checklists), status flags vocabulary, Flex Fields for institutional workflows, TMS Suite module split (Loans/Exhibitions/Shipping/Projects), Spectrum partner positioning, "Anne the registrar" video narrative.
- MuseumPlus: "input and output protocols" wording for exhibition movements; Contracts module naming; SaaS option; GIS add-on (unrelated).
- Artlogic: Location/Shipping tab field layout (current location, location detail, date, last examined by); "Add to location history" mechanics; Update multiple tool; ARTA quote-request document type; Articheck integration; Private Views/art fair prep timeline (publication side); Artlogic App.
- ARTA: product tiers (Self Ship/Parcel/Select/Premium), Quote Request → Quote → Shipment component model, fulfillment statuses/exceptions/destination services, DDP product, commerce-solutions positioning (marketplaces/merchants/auction sellers).
- Articheck: Transit Hub naming, template language count, sharing granularity (access/extent/duration), audit-trail claims, numeric marketing claims (excluded from canonical doc).

## Vendor-specific Findings

All L3 above. None enter the canonical model. Notable structural observation: the specialized poles (ARTA, Articheck) each contain exactly one of this Type's invariant structures (movement execution without the display occasion; handover documentation without the occasion or the chain) — they are the market's own decomposition of the logistics problem into point tools, which the organizer systems integrate with.

## Boundary Findings

1. **vs Exhibition Planning Platform (sibling)** — upstream: concept, curation, design, budget, schedule, and the production plan before anything moves. Logistics begins at the physical chain: what is checked, packed, shipped, received, returned. Structural test: remove venue logistics and custody continuity → planning remains; remove planning/design → logistics remains.
2. **vs Exhibition Installation Management (sibling)** — venue-side execution (mounting, layout, condition-on-install, deinstall work). This Type covers the movement to/from the venue and custody continuity; installation is what happens inside the venue between the receipt leg and the return leg. They meet at the handover (arrival condition check ↔ install condition check).
3. **vs Museum Object Movement Management (sibling)** — general internal location tracking and movement control for any reason (storage↔gallery↔conservation). This Type is movement organized by a display occasion, typically including external venues, transport execution, and cross-party handover. Remove the occasion → object movement remains.
4. **vs Museum Loan Management (sibling)** — the legal/agreement layer (borrower/lender, requests, approvals, terms, return obligations) vs the physical layer. Every sampled organizer system ships them as sibling modules (TMS Loans vs Shipping/Exhibitions; Zetcom Contracts vs Exhibition Management). Remove the movement/custody chain → loan management remains; remove the agreement terms → logistics remains.
5. **vs Artwork Consignment Management (adjacent sibling, prior pass)** — consignment is the retained-ownership commercial basis; exhibitions are a display occasion. In the commercial world the same physical move may be documented as a consignment (Art Galleria artist side: "Send your artworks to exhibitions with professional consignments... when they're due back"), so the documents overlap in practice — but the structures differ: settlement vs custody chain.
6. **vs art shipping/fulfillment platforms (ARTA; no dedicated directory leaf)** — quote→book→track transport execution for unique items without a display occasion. The exhibition-logistics system consumes this layer (Artlogic→ARTA) or reimplements it at summary level (TMS Shipping Module). Structural test: remove the display occasion and checklist → an art shipping platform remains.
7. **vs condition-reporting tools (Articheck)** — the handover-documentation invariant alone, as a cross-party point tool. Adjacent capability; organizer systems either link condition media on the object record or integrate such tools.
8. **Taxonomy / packaging reality** — in the reachable sample, **no standalone dedicated "artwork exhibition logistics" product exists**: the structure ships as modules inside museum collection systems (TMS: Loans/Exhibitions/Shipping beside the object record; MuseumPlus: Exhibition Management beside Contracts) and inside gallery suites (Artlogic: location/shipping + exhibition/fair records), with specialized point tools at the edges (transport execution, condition reporting). The leaf is therefore documented as the logistics-centered structure (checklist + movement chain + custody continuity + handover documentation) while flagging the packaging reality as a probable Module/Capability-of-suite relationship — consistent with the flag raised by the artwork-consignment pass. Requires joint review with the §27 sibling leaves.

## Uncertainties

- Museum-side evidence is module-level (Tier 2) for both museum incumbents: Gallery Systems' detailed help sits behind a client login; zetcom's help center was unreachable (transport error). Screen-level workflows (exact states of a shipment record, exact in/out protocol fields) are not asserted.
- The UK museum standard's transportation procedure pages (Collections Trust) returned 404 twice; standards-level vocabulary could not be verified and no Spectrum-specific claims are made.
- Vernon Systems (a potential small-museum data point) returned an empty response and was dropped after one failure.
- Touring-exhibition rotation (multi-venue schedules) was not directly evidenced in the sample beyond Articheck's "travelling exhibitions" sharing scenario; the touring variant is written qualitatively.
- Insurance mechanics (policy types, valuation flows) appear in all poles only as attached considerations; no formula-level or state-level claims are made.
- Packing/crating evidence is strong on the execution side (ARTA) and readiness side (TMS) but weak on the organizer-side modeling; kept qualitative.
- No search-engine discovery pass was made (prior passes showed poor results for this domain); the "no standalone product" conclusion is bounded to the reachable sample.

## Final Synthesis

Artwork Exhibition Logistics is the software structure that operates the physical journey of artworks to, between, and from display occasions. Its world is built from unique work records whose location is always current and historically documented; a display occasion (exhibition or fair) that gathers specific works into a checklist; a movement chain per work — out to the venue, through the display period, and back home or onward to the next occasion — with condition statements and dispatch/receipt records attached to each handover. Around this spine the market has grown standard capabilities: transport coordination at summary level or via integrated execution platforms, readiness and shipping-requirement management, insurance attachments, packing requirements, cross-party sharing of logistics records with partner institutions and art handlers, and reporting. The defining boundary: remove the display occasion and only object movement or art shipping remains; remove the movement chain and only exhibition planning/installation remains; remove the handover documentation and the operator cannot prove due care — the reason registrars exist. In the reachable market the structure is not sold standalone: museum collection systems and gallery suites carry it as modules, flanked by point tools for transport execution (quote→book→track) and for condition/transit documentation. This packaging reality is recorded as a boundary issue for joint review with the sibling §27 leaves.
