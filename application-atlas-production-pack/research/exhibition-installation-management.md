# Research Notes — Exhibition Installation Management

Research date: 2026-09-07
Slug: `exhibition-installation-management`
Directory leaf: "Exhibition Installation Management" (§27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what software for managing exhibition installation actually does — its central objects, workflows, states and rules — well enough to write a vendor-neutral Application Document, and to resolve the taxonomy question raised by the neighborhood: is "Exhibition Installation Management" an independent product category, or the venue-side execution layer that lives inside museum collection suites' exhibition modules (and gallery suites' exhibition records), with the physical mounting work coordinated by generic tools outside the software?

## Initial Boundary

Working hypothesis before research:

- Exhibition installation management = the venue-side execution layer of a display occasion: planning and tracking the physical mounting of a defined set of works/elements into a venue space (placement, condition-on-install, display furniture/graphics/AV), and the mirror-image deinstall after close.
- Primary operators: museum registrars and collections managers, exhibition/production managers, curators (approving placement), preparators/art handlers (executing), AV technicians.
- Nearest neighbors in the directory (all siblings under §27): Exhibition Planning Platform (upstream curatorial/production planning), Artwork Exhibition Logistics (movement to/from the venue and custody continuity), Museum Object Movement Management (general internal location tracking), Museum Loan Management (the legal/agreement layer), Museum Collections Management (the object record system), Museum Condition Reporting (condition documentation). Adjacent outside §27: Convention / Exhibition Management (event industry — different object world: booths, services, exhibitors).
- Prior cross-references from adjacent passes already processed:
  - artwork-exhibition-logistics (2026-09-06): "vs Exhibition Installation Management (sibling) — venue-side execution (mounting, layout, condition-on-install, deinstall work). This Type covers the movement to/from the venue and custody continuity; installation is what happens inside the venue between the receipt leg and the return leg. They meet at the handover (arrival condition check ↔ install condition check)." The same pass flagged probable Module/Capability-of-suite packaging for the logistics structure and called for joint review of the §27 sibling leaves.
  - art-gallery-management (2026-09-06): exhibitions as records inside gallery suites; Veevart repositioned from gallery-side to museum operations.
  - artwork-consignment-management (2026-09-06): consignment as basis layer; no standalone consignment product in the reachable market.

## Research Questions

1. What is the central object — the exhibition record, the checklist of works, the venue/space, the per-object install state, or the install work items (tasks/crews)?
2. How is the install workflow modeled in software: checklist → space preparation → receive/condition → install → open → period → deinstall → condition-on-return?
3. What status/lifecycle does an object or element carry during install (not installed → installed → deinstalled)? How is "in the exhibition" recorded (statuses, in/out protocols, exhibition membership)?
4. Which roles exist and what can each do (registrar, curator, preparator, contractor)?
5. Is the capability standalone, a module inside museum collection systems / gallery suites, or handled by generic tools (spreadsheets, task boards, floor-plan drawings)?
6. How do variants differ: museum temporary exhibition vs permanent-gallery rotation vs traveling exhibition vs commercial gallery show vs art-fair booth?
7. Historical check: would a pre-digital museum install operation (paper install schedules, object lists, condition-on-receipt forms, gallery registers) satisfy the same core?

## Representative Products

Selected for market representability, documentation accessibility, different customer levels and different product philosophies. All reachable products in this domain are museum collection management suites carrying exhibition modules — itself a finding (see Boundary Findings #8):

| Product | Segment / tier | Philosophy | Evidence accessed |
|---|---|---|---|
| **Gallery Systems — TMS Collections** | Museum incumbent (40+ years; large institutions worldwide) | The collection database as operational hub; Exhibitions Module beside the object record, with planning stages, checklists (Packages), venues, object statuses | Tier 2: product pages, vendor-authored exhibition-management guide outline, vendor workflow article (in-repo), registrar role page |
| **Zetcom — MuseumPlus** | European museum incumbent (Bern; ~900+ museums claimed) | Exhibition Management as a named module: coordination of participants, venues and lenders + input and output protocols; Contracts module separate | Tier 2: product page (module descriptions) |
| **Lucidea — Argus** | Small/mid museum pole (SaaS; Essentia program for small teams) | Web CMS with exhibits at object-history level; mobile on-site condition/location capture | Tier 2: product page (feature lists, testimonials) |
| **CatalogIt** | Smallest-institution pole (cloud SaaS; museum/personal/organization/conservator plans) | Exhibition/Loan/Shipment/Shipping Container profiles linked per exhibition; serves art installers/preparators as documentation users | Tier 1/2: public help center structure + vendor-authored traveling-exhibitions article by a named museum consultant |
| **Collector Systems** | Cloud CMS pole (museums + private collectors + advisors) | Exhibition and file management as tabs in a customizable cloud CMS; mobile location updates | Tier 2: product page |

Considered and excluded (network-limitation rule):

- **Vernon Systems** (small-museum pole, NZ): www.vernonsystems.com returned an empty response twice across two days (2026-09-06 prior pass; 2026-09-07 this pass, two URL patterns) — abandoned; no claims made.
- **Axiell** (museum incumbent): product URL 404; help.axiell.com timed out — abandoned after one attempt each; no claims made.
- **Zetcom brochure PDF**: fetch returned raw binary — not usable; MuseumPlus evidence stays at module-description level.
- **Veevart** (Salesforce-based museum operations): homepage shows repositioning to museum operations (fundraising/membership/ticketing/shop/front desk/accounting) with no exhibitions/collections module surfaced — used as market-structure context only, not a representative product.
- **ArtBelt** (candidate art-logistics operations tool from model memory): domain is parked for sale — memory-based candidate discarded; no claims made. (Lesson recorded: memory-sourced product names in this niche are unreliable.)
- Gallery Systems' detailed help sits behind a client login (community portal); TMS evidence is module/guide-outline level rather than screen-level.
- No search-engine discovery pass was possible (prior passes in this repo consistently found search engines unusable); the "no standalone product" conclusion is bounded to the reachable sample.

## Sources

Tier 1 (official operational documentation):

- CatalogIt — "Track Every Mile: Using CatalogIt for Traveling Exhibitions" (vendor blog, authored by Joy Tahan Ruddell, museum & collections consultant) — https://www.catalogit.app/post/track-every-mile-using-catalogit-for-traveling-exhibitions (Exhibition profile; Loan Out profiles; per-leg Shipment profiles capturing trucking/flight/courier/customs/condition checks/insurance/key dates; Shipping Container profiles for crates — materials, dimensions, contents; all linked to the Exhibition profile; multi-venue touring scenario San Francisco → Chicago → New York → Paris → return)
- CatalogIt Help Center — https://support.catalogit.app/ (category structure: Basic Features / Entries / Profiles / Museum Features [accession, acquisition, deaccession, forms] / Advanced Features; no installation-work category exists)

Tier 2 (official product pages / vendor-authored operational articles):

- Gallery Systems — "The Essential Guide to Managing Exhibitions in TMS Collections" (guide landing page with outline) — https://www.gallerysystems.com/resources/the-essential-guide-to-managing-exhibitions-in-tms-collections/ (catalog all exhibition types; object packages to build and refine checklists; complete customized Exhibition records; managing planning stages and user access; tracking venues, approvals, and object movements; linking objects to build accurate exhibition histories; enriching records with text entries and media; standardizing data entry and dashboards)
- Gallery Systems — "Enhancing Museum Workflows with the TMS Suite" (vendor workflow article; cited in prior in-repo pass) — Exhibitions Module "monitor object statuses, review approvals, and track deliverables"; Packages "ideal for exhibition checklists"; status flags incl. "Condition Report Needed"
- Gallery Systems — Collections Management product page — https://www.gallerysystems.com/solutions/collections-management/ (TMS Collections positioning; registrar testimonial on batch updating)
- Gallery Systems — site search results for "exhibition" — https://www.gallerysystems.com/?s=exhibition (EODEM article: Exhibition Object Data Exchange Model for loan/exhibition data exchange between institutions; webinar "Exhibition and Loan Management Best Practices: From Planning to Display")
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/ ("Exhibition Management — Coordination of participants, venues and lenders, as well as input and output protocols"; "Contracts — Management of agreements and contracts relating to exhibitions, loans and collection objects"; SaaS option; MuseumPlus Scan mobile app)
- Lucidea — Argus — https://lucidea.com/argus/ ("Manage accession, inventories, and locations"; "See the history of each object (including accessions, loans, and exhibits)"; mobile: "record data, check the condition of objects on site, or do inventories on the go"; "highlight specific exhibits or objects"; Essentia Program for smaller teams; Spectrum Partner)
- Collector Systems — https://www.collectorsystems.com/ ("From powerful search and reporting tools to exhibition and file management"; 1,000+ specialized data fields; built-in workflow; mobile app "update locations"; museums + private collections + advisors)

Prior in-repo evidence (adjacent passes, 2026-09-06):

- research/artwork-exhibition-logistics.md (TMS Loans/Exhibitions/Shipping modules; MuseumPlus in/out protocols; Artlogic exhibition/fair records + location/shipping; ARTA transport execution; Articheck condition/transit documentation)
- research/art-gallery-management.md (gallery suites: exhibitions as records; Veevart repositioning)
- research/artwork-consignment-management.md (consignment module packaging pattern)

## Product Observations

### Gallery Systems — TMS Collections (museum incumbent pole)

Evidence layer: B at module/guide-outline level (official product pages + vendor-authored guide outline and workflow article; no screen-level help docs reachable — client community is login-gated).

Key observations:

- The Exhibitions Module is described as record-and-status management: "Monitor object statuses, review approvals, and track deliverables" (workflow article); the guide outline adds "Managing planning stages and user access effectively" and "Tracking venues, approvals, and object movements."
- The checklist is a first-class structure: "Using object packages to build and refine checklists" (guide outline); Packages are "custom lists of records for collaborative work — ideal for exhibition checklists" (workflow article).
- Exhibition types are plural and cataloged: "How to catalog all exhibition types in TMS Collections" (guide outline) — in-house shows, travelling exhibitions, outgoing-loan responses, virtual exhibitions are named in the guide's framing text.
- Per-object exhibition history: "Linking objects to build accurate exhibition histories" (guide outline) — the object record accumulates its display history.
- Condition documentation attaches to the workflow: condition reports as linked media on object records; "Condition Report Needed" status flag (workflow article; registrar role page in prior pass).
- The guide's own scope statement names the coordination set: "careful coordination among curators, registrars, conservators, educators, and designers."
- Notably absent from every reachable description: wall construction, placement execution, crew scheduling, equipment/case installation as managed objects. The module tracks the exhibition record and its objects' statuses — not the physical work items.

### Zetcom — MuseumPlus (European incumbent pole)

Evidence layer: B at module level (official product page only; brochure PDF unusable, help center unreachable in prior pass).

Key observations:

- "Exhibition Management — Coordination of participants, venues and lenders, as well as input and output protocols." The in/out protocol is the documented movement of works into and out of the exhibition context — the record-level install/deinstall seam.
- "Contracts" is a separate module for exhibition/loan agreements — the legal layer is adjacent, not part of Exhibition Management.
- MuseumPlus Scan (mobile scanning) exists as a separate product — mobile capture of objects/locations.
- Same absence as TMS: no reachable description of physical install work items (crews, construction, placement tasks).

### Lucidea — Argus (small/mid museum pole)

Evidence layer: B (official product page).

Key observations:

- Exhibits live at the object-history level: "See the history of each object (including accessions, loans, and exhibits)" — the exhibition is something an object was in, recorded on the object's timeline.
- Location and condition capture is mobile-first: staff "record data, check the condition of objects on site, or do inventories on the go" — the on-site (in-gallery) documentation moment is supported.
- "Manage accession, inventories, and locations" — the location spine that install states ride on.
- Public-portal side: "highlight specific exhibits or objects" — the exhibition record doubles as curation for the online portal (adjacent capability).
- Essentia Program: enterprise features packaged for small teams — the small-museum tier is explicitly served.

### CatalogIt (smallest-institution pole — Tier 1)

Evidence layer: A for the traveling-exhibitions article (vendor-authored operational walkthrough by a named museum consultant); B for plan/feature positioning.

Key observations:

- The Exhibition profile is the organizing container: shipments and loans link to it; "you can view the entire journey in one place."
- Per-leg Shipment profiles capture "trucking arrangements, flight and cargo details, courier and customs information, condition checks, insurance coverage, key dates" — the movement layer is fully modeled (this is the logistics sibling's territory, evidenced here at Tier 1).
- Shipping Container profiles document "each crate's materials, dimensions, and contents" and generate "a comprehensive crate list for the entire exhibition, keeping registrars, shippers, and couriers on the same page."
- Loan Out profiles tie each lender's works to the exhibition — the agreement layer is a sibling profile type.
- The Museum plan advertises "Accession, exhibition, loan, and location documentation" — exhibition documentation is a standard CMS capability at the smallest tier too.
- Boundary-relevant positioning: CatalogIt's Consultants audience explicitly includes "Art Installers and Preparators" and "Display and Mounting Professionals" — but the product serves them as object-documentation users (condition, location, records), not as install-project management. Even the vendor closest to the install trade does not model install work.
- The help center's category tree (Basic Features / Entries / Profiles / Museum Features / Advanced Features) contains no installation-work category; Museum Features covers accession/acquisition/deaccession/forms.

### Collector Systems (cloud CMS pole)

Evidence layer: B (official product page).

Key observations:

- "Exhibition and file management" appears in the feature enumeration alongside search/reporting — exhibitions as a standard CMS tab.
- "Built-in workflow — streamline your collections management with built-in workflow for every process" — generic workflow machinery, not install-specific structures.
- Mobile app: "update locations, check financials, and collaborate" — location updates on the go.
- 1,000+ specialized data fields and 130+ user-defined fields — configurability rather than a dedicated install object model.

### Cross-product synthesis observations

- **The exhibition record is the organizing container everywhere**: TMS Exhibitions Module, MuseumPlus Exhibition Management, CatalogIt Exhibition profile, Argus/Collector Systems exhibit references on object records.
- **The checklist of works for the occasion is universal**: TMS Packages ("ideal for exhibition checklists"), CatalogIt (works linked via loans to the exhibition), Artlogic (prior pass: artwork lists on exhibition/fair records).
- **Per-object install/display state is recorded as entering and leaving the exhibition context**: TMS "monitor object statuses" + object movements; MuseumPlus "input and output protocols"; Argus object history including exhibits; CatalogIt loans/shipments linked per exhibition. The state vocabulary varies (statuses, protocols, history entries) but the structure is the same: the system can answer "is this work currently installed in this exhibition, and when did it go in/out."
- **Condition documentation attaches to the handover moments**: TMS condition reports as media + "Condition Report Needed" flag; CatalogIt condition checks per shipment leg; Argus on-site condition capture; Articheck as the dedicated point tool (prior pass).
- **Venues are tracked for touring**: TMS "tracking venues"; MuseumPlus "coordination of participants, venues and lenders"; CatalogIt multi-venue shipment chains.
- **The physical install work itself is not modeled in any reachable product**: no wall construction, no placement/position records, no crew/task scheduling, no equipment (cases, plinths, AV) installation tracking appears in any reachable documentation. The closest gestures are TMS's "planning stages" (record-level lifecycle stages) and CatalogIt serving installers as documentation users.
- **The agreement layer (loans/contracts) is a sibling module everywhere**: TMS Loans Module, MuseumPlus Contracts, CatalogIt Loan Out profiles.
- **The movement layer (shipments, crates, couriers) is modeled where the logistics sibling lives**: CatalogIt Shipment/Shipping Container profiles (Tier 1), TMS Shipping Module (prior pass).

## Cross-product Comparison

| Structure | TMS Collections | MuseumPlus | Argus | CatalogIt | Collector Systems | Assessment |
|---|---|---|---|---|---|---|
| Exhibition as organizing record (occasion with venue[s] and dates) | ✔ (Exhibitions Module; exhibition types cataloged) | ✔ (Exhibition Management module) | ✔ (exhibits on object history; portal exhibits) | ✔ (Exhibition profile; Tier 1) | ✔ (exhibition management tab) | Core (all) |
| Checklist of works/elements for the occasion | ✔ (Packages "ideal for exhibition checklists") | implied (exhibition module) | implied (exhibits reference objects) | ✔ (works linked via loans; Tier 1) | implied | Core (all organizer-side products) |
| Per-element install/display state (in the exhibition ↔ out) | ✔ ("monitor object statuses"; object movements) | ✔ ("input and output protocols") | ✔ (object history incl. exhibits) | ✔ (loans/shipments linked per exhibition; condition checks) | implied (workflow + locations) | Core (all; vocabulary varies) |
| Condition documentation at handover moments | ✔ (condition reports as media; "Condition Report Needed" flag) | not observed at module level | ✔ (on-site condition capture, mobile) | ✔ (condition checks per leg; Tier 1) | not observed | Common (institutional norm; strongest in museum tier) |
| Venues / multi-venue touring | ✔ ("tracking venues") | ✔ ("coordination of participants, venues and lenders") | not observed | ✔ (multi-venue shipment chain; Tier 1) | not observed | Common (touring contexts) |
| Exhibition history per object | ✔ ("linking objects to build accurate exhibition histories") | implied (in/out protocols accumulate) | ✔ (explicit: object history incl. exhibits) | implied (linked records) | implied | Common (all museum-tier products) |
| Linked movement/shipment records (crates, couriers, transport) | ✔ (Shipping Module; prior pass) | implied (in/out protocols) | not observed | ✔ (Shipment + Shipping Container profiles; Tier 1) | not observed | Common (the seam with the logistics sibling) |
| Readiness flags / statuses needing attention | ✔ (status flags incl. "Condition Report Needed") | not observed | not observed | not observed | not observed | Optional (single-product direct evidence; keep qualified) |
| Agreement layer (loans/contracts) as sibling | ✔ (Loans Module) | ✔ (Contracts module) | ✔ (loans in object history) | ✔ (Loan Out profiles) | not observed | Adjacent sibling (separate module/profile; not this Type's core) |
| Physical install work items (walls, placement tasks, crews, equipment install) | ✘ (not in any reachable description) | ✘ | ✘ | ✘ | ✘ | Absent from the reachable sample — the load-bearing negative finding |
| Design/layout artifacts (floor plans, mount designs) | not observed | not observed | not observed | not observed | not observed | Absent (design tools are a different Type; attachments possible but unevidenced) |
| Publication side (online exhibits) | ✔ (virtual exhibitions named in guide framing) | ✔ (eMuseumPlus sibling product) | ✔ (public portal exhibits) | ✔ (HUB web publishing) | ✔ (WordPress/Drupal integration) | Common adjacent capability (drift toward Digital Collection Portal) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software is not recognizable as exhibition installation management:

```text
Display occasion (the exhibition: venue space + date window,
                  install → open → close → deinstall)
└── Install scope: the defined set of works/elements
    gathered for the occasion (the checklist)
    └── Per-element installation state inside the venue
        (awaiting install → installed in place → deinstalled/removed),
        recorded as entering and leaving the exhibition context
```

Three invariants:

1. **A display occasion anchored to a venue space and a date window** — the exhibition is a bounded context (in-house show, touring stop, gallery show) whose lifecycle runs install → open → close → deinstall. Without it, object statuses and condition records exist but installation management does not — the software is generic collection or movement tracking.
2. **An install scope: the defined set of works/elements for the occasion** — the checklist that says what will be mounted. Without it there is no install to manage — only a calendar entry or a design idea.
3. **Per-element installation state recorded as entering and leaving the exhibition context** — each work/element carries a display state against the occasion (awaiting install, installed in place, deinstalled/removed), so the system can always answer "what is installed in this exhibition now, and when did each piece go in and come out." Without this state layer the software is exhibition planning (before) or logistics (around), not installation management.

Historical check (§24 applied): a pre-digital registrar's install operation tracks exactly this core — an exhibition file with a dated venue window, an object list (the checklist), and per-object in/out entries in the register with condition noted at receipt and release. Modern implementations (status flags, dashboards, mobile condition capture, linked shipment profiles, online-exhibit publishing) are not definitional. A commercial gallery hanging a show without formal condition reports still satisfies the core (checklist + placement window + in/out) — condition documentation is institutional common practice, not definitional.

### L1 — Common Mature Structure

Present in essentially all mature modern implementations; expected by the market but not definitional:

- condition documentation at the handover moments (arrival/install/deinstall), as linked media or structured reports; readiness flags such as "condition report needed" (flag vocabulary is product-specific)
- venues tracking for touring exhibitions (multiple venues, per-venue windows, participants/lenders coordination)
- exhibition history per object (the object record accumulates where it has been displayed)
- linked movement records at the seam with logistics (shipments, crates/containers, couriers, key dates)
- the agreement layer as a sibling (loans/contracts) that usually triggers the install
- collaborative checklists (packages/lists) with user access control; dashboards and reports over statuses
- roles: registrar/collections manager (records, statuses, condition), curator (selection/approval), preparator/art handler (execution), conservator (condition)
- publication adjacency: the exhibition record doubling as online-exhibit content

### L2 — Variant / Optional Structure

- segment variants: museum temporary exhibition vs permanent-gallery rotation (the museum's own spaces, no external venues) vs traveling exhibition (multi-venue chain) vs commercial gallery show (short window, sales overlay) vs art-fair booth (days-long window, booth as venue) vs historic-house reinstall
- depth of physical-work coordination: none in-system (the dominant reachable pattern — work coordinated with generic tools outside the software) vs task/checklist overlays configured in generic workflow fields
- design/layout artifacts: floor plans and mount designs produced in external design/CAD tools and attached (or not) to the exhibition record
- condition-report formality: full institutional protocols vs informal notes (commercial tier)
- time-based media / AV install specifics (equipment, power, playback checks) — depth varies
- publication depth: from a simple online exhibit page to a full public portal

### L3 — Vendor-specific (research notes only)

- TMS Collections: Exhibitions Module naming; Packages (checklists); status flags vocabulary ("Condition Report Needed"); planning stages; guide outline structure (exhibition types, venues/approvals/movements, exhibition histories, dashboards); EODEM (Exhibition Object Data Exchange Model) support for inter-institution loan/exhibition data exchange; Spectrum Partner positioning; login-gated client community.
- MuseumPlus: "input and output protocols" wording; Contracts module naming; MuseumPlus Scan mobile product; SaaS option; ~900 museums claim.
- Argus: object-history framing of exhibits; mobile on-site condition/inventory capture; Essentia Program packaging for small teams; public-portal exhibit highlighting.
- CatalogIt: Exhibition/Loan Out/Shipment/Shipping Container profile family and their linking; the traveling-exhibitions walkthrough scenario (San Francisco → Chicago → New York → Paris); Consultants audience naming ("Art Installers and Preparators", "Display and Mounting Professionals"); plan tiers with entry counts/storage.
- Collector Systems: 1,000+ specialized fields / 130+ user-defined fields; built-in workflow; WordPress/Drupal public integration; SOC 2/ISO 27001 claims.

## Vendor-specific Findings

All L3 above. None enter the canonical model. Notable structural observation: the two poles of the reachable market (largest incumbent suites and smallest-institution SaaS) implement the same record-level structure — exhibition record + checklist + in/out state — while neither models the physical install work. The market has not decomposed installation into a dedicated product the way it decomposed transport execution (ARTA) and condition documentation (Articheck); installation remains a layer inside the exhibition record.

## Boundary Findings

1. **vs Exhibition Planning Platform (sibling)** — upstream: concept, curation, design, budget, schedule, and the production plan before anything is mounted. Installation begins when the venue space is taken over for mounting. Structural test: remove the venue-space takeover and per-element install states → planning remains; remove the curatorial/design plan → installation tracking remains. Note: TMS's "planning stages" are the exhibition record's lifecycle stages, not the curatorial planning work — the record-level lifecycle belongs to this Type's occasion container.
2. **vs Artwork Exhibition Logistics (sibling, prior pass)** — the movement to/from the venue and custody continuity (checklist → out → venue → return/forward, with handover documentation). Installation is what happens inside the venue between the receipt leg and the return leg. They meet at the handover: the arrival condition check feeds the install condition check; the deinstall condition check feeds the return leg. Structural test: remove the movement chain → install tracking remains; remove the install/placement state → logistics remains. The prior pass's flag is confirmed and refined from this side.
3. **vs Museum Object Movement Management (sibling)** — general internal location tracking and movement control for any reason (storage↔gallery↔conservation). Installation is movement/state organized by a display occasion and ending in a display placement. Remove the occasion → object movement remains.
4. **vs Museum Condition Reporting (sibling)** — condition documentation as a standalone discipline (reports at any moment: transit, conservation, install). Installation consumes condition documentation at its handover moments but is not constituted by it. Remove condition reports → install state tracking remains (weakened but present); remove install states → condition reporting remains.
5. **vs Museum Loan Management (sibling)** — the legal/agreement layer (borrower/lender, requests, approvals, terms, return obligations). Every sampled system ships it as a sibling module/profile (TMS Loans; MuseumPlus Contracts; CatalogIt Loan Out). Remove the install states → loan management remains; remove the agreement terms → installation tracking remains.
6. **vs Museum Collections Management (sibling)** — the object record system is the substrate: install states, condition media, exhibition histories all hang off object records. Remove the exhibition occasion → collection management remains intact; remove the object records → installation management has nothing to install. Probable substrate/module relationship.
7. **vs Convention / Exhibition Management (§26, adjacent)** — the event-industry "exhibition" is a trade show: exhibitors, booths, service ordering, attendees. Its installation world (booth build/dismantle, "I&D") is a service-execution business around event infrastructure, not a collection-object lifecycle. Different object world, different rules; no shared core beyond the word "exhibition."
8. **Taxonomy / packaging reality** — in the reachable sample, **no standalone dedicated "exhibition installation management" product exists**: the install-state structure ships inside museum collection suites' exhibition modules (TMS Exhibitions; MuseumPlus Exhibition Management; Argus/Collector Systems exhibit references; CatalogIt Exhibition profile) and inside gallery suites' exhibition records (Artlogic, prior pass), while the physical mounting work (walls, placement, crews, equipment) is coordinated with generic tools outside the software. The leaf is therefore documented as the venue-side installation structure (occasion + install scope + per-element install state) while flagging the packaging reality as a probable Module/Capability-of-suite relationship — consistent with the flags raised by the artwork-exhibition-logistics and artwork-consignment passes. Requires joint review with the §27 sibling leaves (Exhibition Planning Platform, Museum Object Movement Management, Museum Loan Management, Museum Collections Management).

## Uncertainties

- Museum-side evidence is module/guide-outline level for the incumbents: Gallery Systems' detailed help is login-gated; Zetcom's brochure PDF was unusable and its help center was unreachable (prior pass). Screen-level workflows (exact status vocabularies, exact in/out protocol fields) are not asserted.
- Vernon Systems and Axiell (two additional museum CMS incumbents) could not be reached; the sample's breadth is bounded accordingly.
- The "physical install work is not modeled" finding is a negative finding over reachable documentation only: a product could model install tasks in a way not surfaced in marketing/product pages. The finding is stated at sample-bounded strength.
- Placement/position data (where exactly in the space a work hangs) is not evidenced in any reachable product; museums may track it in design files or free-text fields. No claim is made either way.
- Trade-show booth installation (I&D) software was not researched (different object world; no reachable product identified); the boundary with Convention / Exhibition Management is drawn structurally, not from product evidence.
- The permanent-gallery rotation variant (install states for ongoing collection displays rather than temporary exhibitions) is inferred from the object-history structure (Argus) and is written qualitatively.
- No search-engine discovery pass was possible; the "no standalone product" conclusion is bounded to the reachable sample and known-vendor enumeration.

## Final Synthesis

Exhibition Installation Management is the venue-side execution layer of display occasions. Its world is built from a display occasion — an exhibition anchored to a venue space and a date window running install → open → close → deinstall — an install scope (the defined checklist of works/elements gathered for the occasion), and a per-element installation state recorded as entering and leaving the exhibition context, so the system can always answer what is installed now and when each piece went in and came out. Around this spine the market has grown standard capabilities: condition documentation at the handover moments, venues tracking for touring, per-object exhibition histories, linked movement records at the seam with logistics, a sibling agreement layer (loans/contracts), collaborative checklists with access control, and publication of the exhibition record as online content. The load-bearing negative finding: in the reachable sample no product models the physical install work itself (wall construction, placement execution, crew scheduling, equipment installation) — that work is coordinated with generic tools outside the software, and no standalone dedicated installation-management product was identified. The structure ships as the exhibition layer inside museum collection suites and gallery suites. Boundaries: remove the venue-space takeover and install states → exhibition planning remains; remove the movement chain → installation remains (logistics is the around-the-venue sibling); remove the occasion → object movement remains; remove the object records → nothing is left to install. This packaging reality is recorded as a boundary issue for joint review with the sibling §27 leaves.
