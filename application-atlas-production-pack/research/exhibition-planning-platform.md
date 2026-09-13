# Research Notes — Exhibition Planning Platform

## Research Goal

Understand what an "Exhibition Planning Platform" actually is in the real market: who plans exhibitions in software, what the planning-side object structure is, how planning relates to the already-processed sibling leaves (Exhibition Installation Management, Artwork Exhibition Logistics, Convention / Exhibition Management), and whether the Type stands as an independent Application Type or is a functional slice of museum/gallery suite modules.

## Initial Boundary

Leaf: Exhibition Planning Platform (§27 Media, Entertainment, Creator & Culture — museum/cultural-heritage cluster).

Initial hypothesis before research: the pre-execution, curator/registrar-side layer of displays — concept, selection of works, schedule, design, budget — upstream of installation (venue execution) and logistics (movement).

Immediately adjacent Types with already-processed passes (must be consistent with them):

- **Exhibition Installation Management** (applications/exhibition-installation-management.md): L0 = display occasion + install scope checklist + per-element install state (entering/leaving exhibition context). Its Related-Types table defers to this leaf: "concept, curation, design, budget and the production plan before anything is mounted; installation begins at the venue-space takeover."
- **Artwork Exhibition Logistics** (applications/artwork-exhibition-logistics.md): L0 = display occasion + checklist + per-work movement chain + custody continuity + handover documentation. Its Related-Types table defers to this leaf: "curatorial concept, design, budget, and production planning before anything moves."
- **Convention / Exhibition Management** (§26, processed): trade-show organizer operating system (booths, exhibitors, registration) — same word "exhibition", different object world.

Also adjacent: Museum Collections Management (substrate), Museum Loan Management (agreement layer), Digital Collection Portal (publishing), Event Management Platform (§26).

## Research Questions

1. What is the central planning object — is there a distinct "exhibition record" held before the show exists physically?
2. What does the checklist mean on the planning side: who builds it, from what, with what collaboration?
3. Is there a planning workflow (stages, approvals, deadlines)? What vocabulary do products use?
4. How do loans/participants/venues get coordinated during planning?
5. Does spatial/design planning (layout, casework, lighting) exist in software, and is it part of this Type?
6. How does the commercial gallery pole differ from the museum pole?
7. Is there any standalone dedicated exhibition-planning product, or does the structure ship only inside suites?
8. Where are the boundaries vs the two processed siblings — can the "remove X" tests be stated cleanly from this side?

## Representative Products

Selected for market position spread + documentation reachability + different product philosophies:

| Product | Vendor | Pole | Rationale |
|---|---|---|---|
| TMS Collections (Exhibitions module) | Gallery Systems | enterprise museum incumbent | deepest exhibition module; guide + curator role page reachable |
| MuseumPlus (+ Curator) | Zetcom | European museum incumbent | Exhibition Management module; also ships the only dedicated planning-adjacent product found (Curator, 3D planning) |
| Argus | Lucidea | small/mid museum | lighter exhibition treatment; reachable product pages |
| CatalogIt | It Unlimited | smallest institutions / private | exhibition documentation at the light end; help center reachable |
| Artlogic | Artlogic | commercial gallery / artist | gallery-suite pole: exhibitions as records + website publication; support center reachable |

Attempted and abandoned: Artwork Archive (features page returned 403 — domain blocked); Artlogic single help article (404 on direct URL; search snippets retained). Vernon Systems and Axiell were unreachable in prior sibling passes and were not retried (network rules).

## Sources

All fetched 2026-09-07:

- Gallery Systems — The Essential Guide to Managing Exhibitions in TMS Collections (guide outline) — https://www.gallerysystems.com/resources/the-essential-guide-to-managing-exhibitions-in-tms-collections/
- Gallery Systems — Software for Curators (role page) — https://www.gallerysystems.com/roles/software-for-curators/
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/
- Zetcom — Curator — https://www.zetcom.com/en/curator/
- Lucidea — Argus — https://lucidea.com/argus/
- CatalogIt — product site — https://www.catalogit.app/
- Artlogic — Gallery Management — https://www.artlogic.net/products/gallery/management
- Artlogic Support — search results for "exhibition" (86 results; snippets used) — https://support.artlogic.net/hc/en-gb/search?query=exhibition

Prior in-repo passes used for boundary context (same production line): research/exhibition-installation-management.md, research/artwork-exhibition-logistics.md, applications/convention-exhibition-management.md, STATUS.md boundary flags (artwork-exhibition-logistics, exhibition-installation-management).

Evidence quality note: museum incumbents' detailed help centers are login-gated or were unreachable in sibling passes; this pass's evidence is guide-outline, role-page, product-page, and support-snippet level. No screen-level workflow claims are made below unless directly quoted.

## Product Observations

### TMS Collections (Gallery Systems) — museum incumbent

From the exhibitions guide outline (Layer A, official):

- "Strategies to Strengthen Your Exhibition **Planning** and Documentation"; exhibitions described as "one of the most complex and collaborative responsibilities within a museum, requiring careful coordination among curators, registrars, conservators, educators, and designers."
- Module scope: "plan, document, and preserve every aspect of an exhibition"; supports "developing an in-house show, organizing a travelling exhibition, responding to outgoing loan requests, or publishing virtual exhibitions."
- Guide contents (direct list): "How to catalog all exhibition types"; "Using **object packages to build and refine checklists**"; "Creating complete, customized Exhibition records"; "**Managing planning stages** and user access effectively"; "**Tracking venues, approvals, and object movements**"; "Linking objects to build accurate **exhibition histories**"; "Enriching records with text entries, and media"; "Standardizing data entry and leveraging **dashboards**."

From the Software for Curators role page (Layer A):

- "Create a smooth and efficient **planning process** by centralizing object and exhibition data."
- "Easily **create, edit, and share your exhibition checklists**, secured by custom authorization settings."
- "Before filing an inter-museum loan, **see if you have previously requested that object and its status**."
- "View detailed records for collection objects, featuring high-resolution images, **condition reports, and exhibition history**" — the selection-time view of candidate objects.
- Video description: a curator "quickly makes edits and controls access to his exhibition checklist ... while instantly viewing detailed information on the objects he is considering."
- eMuseum (sibling product) publishes exhibitions online.

Interpretation: the curator's planning loop is — select objects into a checklist → check their loan/display status → refine with access-controlled collaboration → advance planning stages. Planning stages, approvals, venues tracking are named module capabilities.

### MuseumPlus + Curator (Zetcom) — European museum incumbent

MuseumPlus product page (Layer A, module level):

- Core functions include "**Exhibition Management**: Coordination of participants, venues and lenders, as well as input and output protocols." and "**Contracts**: Management of agreements and contracts relating to exhibitions, loans and collection objects."
- Additional modules integrate seamlessly (event management, archiving, etc.); SaaS option available.

Curator product page (Layer A) — a distinct, dedicated exhibition-planning product:

- "zetcom Curator is the innovative and proven solution for **digital planning and exhibition design**... exhibition spaces can be precisely simulated and artworks can be optimally and playfully placed."
- Core functions: "3D exhibition planning — place artwork, panels, lights and pedestals"; "Virtual spatial representation — artwork, frames, walls, colors, lighting... Adjust the position and intensity of the light"; "integrated into MuseumPlus — import images, videos, audio files, and 3D artwork directly from MuseumPlus or manually"; "Testing the environment — ...test [if] sunlight falls on [the artwork] during the day"; "Collaboration & Assembly — share your ideas and collaborate with your team. **Export all floor plans and blueprints for every room and every wall**"; "Virtual gallery — create your space ... or let us make an exact copy of your rooms"; plus online/virtual exhibition publishing.
- Problem framing: "The traditional planning of exhibitions requires a lot of time, patience and resources. Employees are often unable to collaborate with each other effectively, and coordination with external service providers is also made more difficult. It is often only possible to validate the planning once the objects are in the room."

Interpretation: spatial/design planning is a real software sub-domain, but in the reachable sample it exists as a separate vendor product (Curator) tightly bound to a collection suite, not as the generic core of the Type.

### Argus (Lucidea) — small/mid museum

Product page (Layer A, product level; exhibitions appear at capability level):

- "Enhanced Curation... handle annotations, accessioning, circulation, loans, and other curation tasks—all from a unified, flexible platform."
- Statistics section: "See the **history of each object (including accessions, loans, and exhibits)**."
- "Create Enriching Multimedia Exhibits... image galleries, links to related objects, and in-depth, multimedia documentation."
- Public portal highlights "specific exhibits"; object records support condition checking on mobile.

Interpretation: at this pole, "exhibits" surface mainly as object-history entries and multimedia exhibit building — the planning machinery is thinner than TMS's; module-level rather than workflow-level evidence.

### CatalogIt (It Unlimited) — smallest institutions / private collections

Product site (Layer A):

- Museum plan: "**Accession, exhibition, loan, and location documentation**"; "Workflow and multi-user capabilities."
- "Use It: ...managing and maintaining your objects, **coordinating exhibitions**, and sharing your stories with the world" via HUB/web publishing.
- Sibling pass verified Exhibition profile linked to Loan, Shipment and Shipping Container profiles; blog "Track Every Mile: Using CatalogIt for Traveling Exhibitions" (2025-07-10) exists for the touring case.

Interpretation: exhibition = a profile type alongside loans/locations; planning is documentation-shaped at this pole.

### Artlogic — commercial gallery / artist pole

Gallery Management page (Layer A):

- "Stay on top of **exhibitions, proposals, and inventory lists** with tools designed to simplify every step."
- Website integration: "Easily build exhibitions, online stores and viewing rooms in minutes."
- Inventory features list: "Consignments and loans... Provenance and condition reports."

Support center search "exhibition" (86 results; Layer A at snippet level):

- "Exhibition records — create an exhibition record and add artworks to it. How to make an Exhibition record... All website Exhibition records" (categorized under Websites > Records & Categories > Other records).
- "How to sort Exhibitions records — reorder how different Exhibition sections appear in your website's Exhibitions page and to sort Exhibition records."
- "Artwork lists & Reports overview — creating **lists and documents for exhibitions and loans**, as well as the Activity Timeline."
- "Add a virtual exhibition to your website — 3-D walk-through exhibitions."
- Art fair records exist as a sibling record type ("Art Fairs" under Other records).

Interpretation: at the gallery pole the exhibition record is artworks + dates + publication: it drives the public website's Exhibitions page, and artwork lists/documents for the show are generated from inventory. Planning machinery (stages, approvals) is not headlined; the record's center of gravity is presentation and sales context.

## Cross-product Comparison

| Aspect | TMS Collections | MuseumPlus (+Curator) | Argus | CatalogIt | Artlogic |
|---|---|---|---|---|---|
| Exhibition as record before the show | Exhibition records; "all exhibition types" cataloged | Exhibition Management module coordinating participants/venues/lenders | exhibits at object-history level | Exhibition profile beside loan/location | Exhibition record with artworks + dates |
| Checklist of works on planning side | object packages "to build and refine checklists"; curator creates/edits/shares checklist | via module + Curator drag-and-drop of artworks | implied by curation tasks | profile-linked works | "add artworks to it"; artwork lists/documents for exhibitions |
| Planning workflow / stages | "Managing planning stages... effectively"; approvals tracking | coordination role (stages not headlined on public page) | not surfaced | "workflow and multi-user capabilities" | not surfaced |
| Availability/loan status consulted at selection | "see if you have previously requested that object and its status" | Contracts module for exhibition/loan agreements | loans handled; linkage present | loan profiles linked | loans + lists/documents |
| Venues / touring | "tracking venues" | venues + lenders coordination | not surfaced | traveling-exhibitions use case | art-fair records sibling type |
| Spatial / design planning | not in reachable docs | Curator: 3D placement, lighting, floor-plan/blueprint export | not surfaced | not surfaced | not in core; virtual exhibition (3D walkthrough) as website output |
| Collaboration / access control | checklist "secured by custom authorization settings" | collaboration framing (Curator) | user permissions, audit trails | multi-user workflow | user roles and permissions |
| Object exhibition history | "build accurate exhibition histories" | implied by module | "history of each object (including... exhibits)" | documentation over time | exhibitions tied to artwork records |
| Publication adjacency | eMuseum online exhibitions; virtual exhibitions | Curator virtual gallery publishing | public portal exhibits | HUB web publishing | website Exhibitions page; virtual exhibitions |

Layer coding: TMS planning stages/checklist/approvals = A (official guide/role page). MuseumPlus exhibition module scope = A (product page). Curator 3D planning = A. Argus/CatalogIt/Artlogic planning depth = A at product/snippet level but thinner; not promoted to cross-product claims where only one product documents a feature.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three structures:

1. **The exhibition record as a planned display occasion** — a named, dated, venue-scoped occasion (in-house show, traveling exhibition, gallery show, collection rotation) held in the system as a record *before and through* its physical realization.
2. **The curated checklist** — the checklist of specific works/elements selected for the occasion, drawn from the collection and prospective loans, built and refined collaboratively during planning, with each entry staying linked to its object record.
3. **The planning progression toward realization** — the occasion is advanced through planning (refinement, approvals, coordination of participants such as lenders and venues) toward its execution window and closure.

Tests: remove the occasion → object-level notes with no show; remove the checklist → a calendar/website page of shows; remove the progression → a static list, not a planning application.

Historical check (older/regional/pre-digital practice): paper exhibition checklists, curator's object lists, printed exhibition schedules, and gallery show files all carry occasion + checklist + progression without any modern implementation (no object packages, no 3D, no cloud, no website sync). The L0 survives; nothing era- or region-specific enters the core.

### L1 — Common Mature Structure

- Checklist/object selection machinery with collaboration and access control (TMS authorization settings; multi-user in CatalogIt/Artlogic/Argus)
- Loan/participant coordination during planning (TMS loan-status check before requesting; MuseumPlus contracts-for-exhibitions; CatalogIt loan profiles; Artlogic lists/documents for exhibitions and loans)
- Venues/touring tracking on the occasion (TMS; MuseumPlus; CatalogIt touring case)
- Linkage building per-object exhibition history (TMS explicit; Argus explicit)
- Approvals tracking (TMS guide names approvals)
- Text/media enrichment of the exhibition record (TMS)
- Reports/dashboards over exhibitions (TMS)
- Publication adjacency: exhibitions feed online exhibits/websites (eMuseum, Curator virtual gallery, CatalogIt HUB, Artlogic website Exhibitions page, Argus portal)

### L2 — Variant / Optional Structure

- Spatial/design planning as a software layer: 3D room models, artwork/panel/lighting placement, environment testing, floor-plan export (single-vendor product: zetcom Curator; also virtual 3D walkthroughs at Artlogic as a website feature). Not observed in the other sampled products' reachable docs.
- Virtual-only exhibitions as a record type (TMS "publishing virtual exhibitions"; Artlogic virtual exhibitions; Curator online exhibition)
- Art-fair presentations as a sibling record type (Artlogic)
- Budget tracking: NOT directly observed in any reachable sample documentation — recorded as plausible museum practice but unverified; excluded from claims
- Task/deadline management detail: not directly observed as named machinery; the TMS guide's workflow framing implies deadline work but no task module was documented — unverified
- Commercial gallery overlay: sales context, proposals, consignments around shows (Artlogic)

### L3 — Vendor-specific (kept out of the final document)

- TMS: "object packages" as the checklist implementation; "planning stages" vocabulary; eMuseum as the publishing sibling
- Zetcom: Curator's drag-and-drop MuseumPlus integration, room-copying service, sunlight simulation
- Artlogic: Exhibition records implemented as website record types; website-sorting of exhibitions; PrivateViews presentation app
- CatalogIt: Exhibition/Loan/Shipment/Shipping Container profile family; HUB publishing
- Argus: exhibits as object-history entries with multimedia exhibit building

## Rejected Findings

- "Exhibition planning = project management with tasks/budgets" — rejected as core: no sampled product's reachable documentation defines the Type through task/budget machinery; museum planning documentation centers on records, checklists, and coordination. Budget/task work is real museum practice but unverified in software specifics here (kept as uncertainty).
- "Spatial design belongs in the core" — rejected: only one sampled vendor ships it, as a separate product; the other products plan exhibitions without 3D tools. It is a strong optional layer.
- "The exhibition program calendar (multi-year scheduling) is definitional" — rejected: no sampled product directly documents a program-level scheduler in reachable docs; statuses/dates over records are what is observable. Program-calendar capability left as uncertainty.
- "Publishing is definitional" — rejected: publishing is an adjacency present in all five products but as a downstream surface (sibling Digital Collection Portal / website products).

## Boundary Findings

**vs Exhibition Installation Management (processed sibling).** Shared: the occasion and the checklist. Discriminator: installation owns the per-element in/out state at the venue (install → installed → deinstalled); planning owns selection, refinement, approvals, and coordination before that state machine starts. From this side: TMS's planning stages/approvals and checklist refinement are curator work; the install state layer (documented in the sibling's pass inside the same TMS module) is registrar work at the venue. Tests: remove install states → planning remains; remove planning progression/checklist refinement → install-state tracking remains.

**vs Artwork Exhibition Logistics (processed sibling).** Logistics owns the movement chain (origin → venue → return) and custody continuity. Planning decides *what* moves and coordinates *why* (selection, loans); logistics executes *how*. Test: remove the movement chain → planning remains; remove the selection/checklist → logistics has nothing to move.

**vs Museum Loan Management.** The loan agreement layer (requests, approvals, terms, returns) is a sibling record type in the same systems (MuseumPlus Contracts; CatalogIt Loan profiles; TMS loan module). Planning *consumes* loan status during selection ("see if you have previously requested that object") but does not constitute the agreement machinery.

**vs Museum Collections Management.** The object record is the substrate; exhibitions link to it and accumulate histories on it. Remove exhibitions → collections management continues unchanged.

**vs Convention / Exhibition Management (§26).** Namesake only: trade-show exhibitions are produced events with exhibitors, booth inventory, registration; collection-object exhibitions are displays of works. Different users, objects, flows, rules.

**vs Digital Collection Portal / website products.** Publishing the exhibition record to the public is downstream adjacency; the record feeds it, but publishing machinery is not the planning Type.

**vs Event Management Platform (§26) / Museum Visitor Experience Platform.** The museum exhibition as planned here has no attendee/registration/visitor-operations machinery in its core; those are separate Types.

**Module-of-suite finding (joint review).** In the reachable sample, no standalone dedicated exhibition-planning product exists. The planning structure ships as the exhibition layer inside museum collection suites (TMS Collections, MuseumPlus, Argus, CatalogIt) and gallery suites (Artlogic). The single dedicated planning-adjacent product found (zetcom Curator — 3D spatial planning) is a suite-bound add-on, not an independent platform. This confirms the pattern the two sibling passes flagged: the §27 exhibition family (Planning / Installation / Logistics) are three functional workflows over one occasion+checklist spine, typically inside one suite module. Directory question for joint review: keep all three as separate Types with containment (each documenting its defining workflow slice) vs fold; this pass does not restructure the directory.

## Uncertainties

- Budget tracking and task/deadline machinery inside planning modules: plausible but not directly documented in the reachable sample — unverified, excluded from the final document.
- Multi-year exhibition-program calendar/scheduler views: not directly observed; only record-level dates/statuses are evidenced.
- Exact planning-stage vocabularies (stage names, transition rules): behind login walls; not asserted.
- Vernon Systems / Axiell exhibition handling: unreachable in sibling passes, not retried here; the sample's coverage of the museum-incumbent pole rests on TMS + MuseumPlus.
- Whether any standalone exhibition-planning SaaS exists outside the museum-suite orbit (e.g., in the design-studio world): not found in reachable official sources; the negative finding is bounded to the reachable sample.

## Final Synthesis

The Exhibition Planning Platform is the curator/registrar-side planning layer over displays. Its defining structure: the exhibition record as a planned display occasion + the curated checklist of works selected for it + the planning progression that advances the occasion toward realization. Around that core, mature systems add checklist collaboration with access control, loan/participant/venue coordination, approvals, object-history linkage, enrichment, reporting, and a publication adjacency. Spatial/design planning is a real but optional software layer (one dedicated suite-bound product in the sample). The commercial gallery pole realizes the same spine with a sales/publication center of gravity. The Type is real as a *workflow* but not as a standalone product category: it ships as the exhibition layer of museum and gallery suites, which is the joint-review finding to record.
