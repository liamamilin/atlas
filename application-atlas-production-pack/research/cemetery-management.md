# Research Notes — Cemetery Management

Research date: 2026-09-06
Slug: cemetery-management
Directory leaf: Cemetery Management (§29 Home, Family, Personal & Local Services)

## Research Goal

Understand what cemetery management software actually is as an Application Type: what objects exist inside it, what cemetery staff do with them, how the core workflows (selling interment rights, scheduling and conducting burials, maintaining grounds and records) actually flow, and where the boundary lies against the neighboring deathcare Types (Funeral Home Management, Crematory Management) and against structurally similar Types (space booking, property management, genealogy platforms, GIS).

## Initial Boundary

Initial hypothesis (before research):

- Cemetery Management is the operator-side business system for running a cemetery: burial space inventory (graves/plots/lots/niches/crypts), interment records (who is buried where), plot/right sales and ownership, burial and service scheduling, grounds work orders, cemetery mapping, and public/genealogy search.
- Closest neighbors: Funeral Home Management (funeral service case), Crematory Management (cremation operation), Enterprise Resource Scheduling (space booking), Property Management, genealogy/records platforms, GIS.
- Expected seam: the cemetery manages the ground and the interment; the funeral home manages the funeral case; the crematory manages the cremation operation.

This hypothesis was used to guide research and was revised only in emphasis (see Final Synthesis).

## Research Questions

1. How is the burial space inventory structured (hierarchy: cemetery → section/block → lot → grave; niches; crypts)? What attributes does a space carry?
2. What exactly is an interment record, and what does it bind (deceased × space × date)? How are multiple interments in one grave handled?
3. How is ownership of burial rights modeled (deed, right of interment, ownership stakeholders, transfers)?
4. What is the space state model (available / reserved / sold / occupied), and how does sale and reservation change it?
5. How do burial/service scheduling and the resulting work orders (grave opening/closing, foundations, memorial installation) flow?
6. What role does the cemetery map play, and how is it linked to records?
7. What does the public-facing surface do (genealogy search, walk-to-grave, online memorials)?
8. How does data flow between funeral homes and cemeteries (at-need cases, funeral director portals, integrations)?
9. What financial machinery exists (contracts, pre-need/at-need, payments, trust/perpetual care funds)?
10. What roles use the system (office, sales/counselors, grounds crew, managers, external funeral directors, masons)?

## Representative Products

Selected for market representability, documentation quality, different product philosophies, and different customer tiers:

1. **PlotBox** — cloud deathcare management platform (cemetery + crematory + funeral home), enterprise posture, US/UK/AU/NZ. Philosophy: integrated multi-domain deathcare platform with mapping and financial suite.
2. **OpusXenta (Byond)** — cemetery and crematoria management software, tiered plans (Basic / Core / CorePLUS), AU/NZ/US/UK; serves councils, trusts, and operators of all sizes. Philosophy: tiered scalability from inactive cemeteries to complex enterprises.
3. **webCemeteries** — US cloud cemetery management with strong public-tools emphasis; the only sampled vendor whose Tier-1 knowledge base was reachable. Philosophy: fully-integrated management + public engagement.
4. **Chronicle** — cemetery-focused (not funeral), mapping-first, strong in AU/NZ/US/CA municipal, private, and religious cemeteries. Philosophy: map-anchored records with digitization services; offers a records-only "Lite" edition.
5. **CemeteryFind** — US records-and-mapping product (since 1992, powered by Docufree); records-centric posture without scheduling/sales depth. Used as the records-only / historical check sample.

Excluded during sampling (recorded, not researched further):

- **CemSites** — site unreachable (403 ×2), abandoned per network rules.
- **SRI Management** — fetches returned empty ×2, abandoned.
- **FrontRunner** — now positioned as funeral-home software under Tribute Technology; cemetery product not reachable as a distinct documented surface.
- **Everdays** — pivoted to life insurance; no longer a cemetery management product (drift).
- **Burgeon** — fetch returned empty ×1.
- **Capterra category page / DuckDuckGo** — 403 / timeout; market landscape instead confirmed via Chronicle's own comparison page, which names the category players: OpusXenta, PlotBox, CemSites, CIMS, Cemify, WebCemeteries.

## Sources

Fetched successfully (all official vendor surfaces):

- PlotBox — https://plotbox.com/ (home), https://plotbox.com/cemetery-management-software/, https://plotbox.com/cemetery-scheduling-software/ — product/marketing pages (Tier 2)
- Chronicle — https://chronicle.rip/ (home), https://chronicle.rip/cemetery-management/, https://chronicle.rip/cemetery-software-comparison/ — product/marketing pages (Tier 2)
- OpusXenta Byond — https://byond.cloud/ (home), https://byond.cloud/cemetery-management-software/ — product/marketing pages (Tier 2)
- webCemeteries — https://webcemeteries.com/ (home), https://webcemeteries.com/solutions/cemetery-management/ (Tier 2), plus **Tier-1 knowledge base**: https://support.webcemeteries.com/ (index) and https://support.webcemeteries.com/management (full module/article listing)
- CemeteryFind — http://cemeteryfind.com/ (home; https://www.cemeteryfind.com transport error ×1, http succeeded)

Source-access limitation: only webCemeteries' help center was reachable at Tier 1. PlotBox, Chronicle, OpusXenta, and CemeteryFind are documented from official product/marketing pages only. Accordingly, no numeric limits, default values, or precise operational parameters are asserted anywhere in this research or the final document; claims for those four products are kept at the feature/structure level visible on their official pages.

## Product Observations

### PlotBox (evidence layer A)

Official pages: home, cemetery-management-software, cemetery-scheduling-software.

- Positioning: "deathcare management platform" for cemeteries, crematories, and funeral homes; claims 2,000+ facilities; solutions pages for municipalities, pet cemeteries, natural/green burials, private organizations, archdiocese.
- **Mapping**: high-resolution drone imagery creates a digital map; "real-time inventory status"; plot information includes "locations, types, capacities, and dimensions"; color heat map displaying status; each point verified, coordinates checked, memorials photographed, discrepancies flagged (mapping is sold with a data-verification service).
- **Records management**: all cemetery records linked in one searchable database, "single source of truth"; Activity Log records "who did what, where, when, and how" per record.
- **Document management**: scanned images of "old books, interment cards, and paper contracts"; virtual filing cabinet; documents linked to plots.
- **Contract management / sales**: sell from anywhere on any device; online payments; electronic signatures; view available plots on digital maps; "place burial plots on hold".
- **Finance**: invoicing, payments, receipts, trust fund management; month-end close; reporting.
- **Scheduling**: real-time shared calendars (daily/weekly/monthly), color coding, linked events, "map burial view"; bookings for burials, cremations, and appointments across multiple sites; "avoid double-bookings"; scheduling "right from a contract with auto-generated burial orders, labels and other paperwork"; optional 24/7 funeral director portal for out-of-hours online booking.
- **Work orders**: assign, track, complete tasks; real-time work order management.
- **Memorial management**: requests to maintenance; memorial mason portal (external masons).
- **CRM**: customer lifecycle "from first contact to aftercare".
- **Public**: EverAfter Connect — public genealogy search, walk-to-grave directions, digital cemetery (flowers, memorials, sales contact).
- **Other**: risk assessments (H&S inspections), AI assistant (Eva), AI obituary assistant, PlotBox Pay, Vertica mapping (360° views of mausolea/columbaria with real-time inventory availability).
- Teams named: cemetery and crematory managers, funeral home directors, groundstaff, board members, sales and marketing, operations.

### OpusXenta — Byond (evidence layer A)

Official pages: home (byond.cloud), cemetery-management-software.

- Positioning: cemetery and crematoria software; "councils, trusts, and operators of all sizes"; AU/NZ/US/UK.
- **Burial management**: burial scheduling; plot management ("each is assigned and maintained accurately"); generate documentation — "burial orders, labels, and paperwork"; create work orders for burials with checklists; grounds staff access via mobile device.
- **Records management**: deceased records management; **ownership records** — "manage and maintain all records related to ownership and interment including details of interment and tenure"; document storage and retrieval.
- **Plot management**: cemetery mapping visualizing "available and sold plots"; plot inventory with "location, type, capacity, and dimensions" (customizable); real-time stock levels and availability.
- **Grounds and memorial management**: work order management; memorial management (installation of, and changes to, memorials); grounds task coordination; **mason permits** — online permit applications; edit, reject, issue, cancel, or complete permits.
- **Care and floral programs**: floral tributes; "annual and perpetual care programs".
- **Complaints management**: complaint tracking + reporting.
- **Plan tiers** (structure evidence): Basic = cemetery mapping (standard), deceased search, records management, public deceased search, public map search; Core = + sales management, **rights (deeds) management**, inventory management, standard scheduling, bookings management, **online funeral director bookings**, burial and cremation management, after care programs, grounds and task management, standard CRM, document management, standard reporting, integrated payments; CorePLUS = + advanced mapping integrations, advanced sales, advanced CRM, marketing automation, e-signatures, advanced scheduling, advanced grounds management, memorial management, permits and applications, risk register, advanced workflows, power reporting, API integrations.
- Dashboard surfaces named: "Persons & Records, Bookings, Programs & Services, Task Manager"; deceased records, invoices, care programs.

### webCemeteries (evidence layer A; Tier-1 for the knowledge base)

Official pages: home, cemetery-management solution page; knowledge base index + Management section (full module and article listing).

- Positioning: fully-integrated cloud solution; unlimited user accounts; permissions by role; navigation across "properties, owners, deceased".
- **Modules visible in the knowledge base** (Tier-1 structure evidence):
  - **Locations Module** — grave space details page; search by location; search available property; reserve a property; add a new location; edit location; edit grave property type; update "depth, price and other grave details"; edit grave layout / mapping / name; **add a new grave/burial right to a location**; **add an additional burial right to a grave**; delete an interment right; **relocate an interment right to a new grave**; update the status of a grave/burial right; view the history of a grave/burial right; add/update **ownership stakeholders** to a location (and to multiple graves); remove an owner; **disinter a deceased record from a location**.
  - **Deceased Module** — search by deceased record; search by dates; search by funeral homes; search veterans / veterans per section; add deceased record; explore deceased record page; add contact/next of kin; add obituary; profile photo; **transfer a deceased record to a new location**; **add a decedent to a location**; mark record as **confidential**; add service/event details; mark a person as **pre-deceased**; update **depth and grave details** from the deceased module; add military service record; delete deceased record.
  - **Ownership Module** — guide to stakeholder roles; search by owner; owner profiles; add/update ownership stakeholders; merge duplicate owner records; documents on owner profiles.
  - **Contracts Module** — "Understanding Need Status in Contracts (**Pre-Need, At-Need, and Combination**)"; quick start guide to building a contract; add locations to a contract; add deceased to contracts; add merchandise to a contract; ownership stakeholders on contracts; sales counselors on contracts; commissions in the price catalog; **perpetual care items**; taxes; payment terms; recurring statements/payments; contract statuses (In Progress, Signed, Price Lock, Cancelled); change ownership on a signed contract; copy a cancelled contract; apply credits; void a transaction; enter a transaction without payment processing; print contract/receipt.
  - **Reservations Module** — reservation types; create a reservation (Enterprise Sales); convert a reservation into a contract; search/manage reservations.
  - **Work Orders Module** — create work order; create from a deceased record / from a location / from Enterprise Sales / from an invoice; job types; recurring work orders + recurrence management; add location, deceased, or tree(s) to a work order; map area on a work order; comments + photos; watchers; templates; print; mark as done; view open/in-progress work orders from the cemetery map.
  - **Memorials Module** — search memorials; add memorial to a location / to a grave/burial right / to multiple graves; photos + primary photo; memorial vendors; customer on memorial.
  - **Maps** — inventory maps; wall maps search.
  - **Books Module** — create a book; add/replace book pages; page through a book; **link book pages to a deceased record / to a location** (scanned register books).
  - **Documents** — add documents to deceased records and locations; in-app document editing (text, shapes, drawing, rotation); rollback edits.
  - **Dynamic Forms** — e-signature; generate documents from location / owner profile / contract / deceased record / **interment right**; "Generating a Deed or **Right of Interment** Dynamic Form from a Location".
  - **CRM (Contacts & Customers)** — contacts, tags, interactions, upcoming interactions, do-not-contact, merge contacts, export owners and owner addresses, transfer credits between customer accounts.
  - **Payment Processing** — transactions, recurring auto payments, payment devices, statements, branding.
  - **Invoices** — generate invoice; apply payments; recurring invoices; create work order from an invoice.
  - **Reports** — accounting ledger report; merchandise and services reports; **daily interment report**; generate PDF.
  - **Arboretum Module** — tree records mapped and toured (tree search, map a tree, tree types, tour stops, export).
  - **Passare integration** — "Passare Integration Overview"; "Managing records linked with Passare" (Passare is funeral-home case management software).
- **Public tools** (product page + KB sections): Locate a Loved One (public burial search with location + online memorial page), Remember My Journey (public memorial timeline), virtual tours, mobile app, Forever Plot, flower store; walk-to-grave directions; publish burial records and maps to the cemetery's website.
- **Digitization service**: on-site scanning and US-based transcription; link scans to records; connect records to maps; migrate from legacy systems.
- Additional named tools: Arboretum Management, Books & Ledgers, Property Reservations, Memorial Management.

### Chronicle (evidence layer A)

Official pages: home, cemetery-management, cemetery-software-comparison.

- Positioning: cemetery management software (not funeral); "managing records, tracking plots, organizing interments"; cloud, multi-user, multi-device; serves municipal councils, private, religious/communal, historical/veterans, memorial park/green burial, multi-location cemeteries (AU/NZ/US/CA).
- **Record keeping**: database editing module; advanced record table; request listing table; activity log and general notes; **interactive map view**; multiple user access and roles; document attachment; advanced record search; "each data connected to your digital map".
- **Certificates and reports**: certificate generator with custom templates — Interment or Burial Certificate, Plot Certificate, **ROI (Right of Interment) or Ownership Certificate**, Work Order Certificate (.docx/.pdf); reports — Inventory, Activity Summary, Interments, Events, **Right of Interment**, Key Persons, Business, User Log (.csv/.xlsx/.pdf).
- **Event calendar & work order**: unlimited events; email notifications; list & calendar views; reminders; document attachment; resource allocation; public event view; Google Calendar integration; event-based certificates.
- **Sales**: sales module; online plot sales; deed certificate management.
- **Mapping services**: drone surveys, GIS mapping, headstone surveys; digitization service (digitize records, link to map, fix mistakes); 360 cemetery mapping; 3D 360 mausoleum & columbarium mapping; niche wall & columbarium display add-on.
- **Public**: Online Public Access — genealogy search; Life Chronicle online memorials (public tributes; revenue shared with cemetery); GPS walk-to-grave; featured stories.
- **Editions**: Lite (basic record management, track changes and notes, create certificate) vs Pro (advanced records, interactive digital map, unlimited users).
- Comparison page names the category: OpusXenta, PlotBox, CemSites, CIMS, Cemify, WebCemeteries; evaluation criteria listed: record management, GIS/digital mapping, public grave search, multi-site support, digitization/migration, sales/invoice/payment workflows, reporting, training/support.

### CemeteryFind (evidence layer A)

Official page: home (http).

- Positioning: "Cloud Records and Mapping for Cemeteries"; since 1992; powered by Docufree; US.
- **Records management**: database "customized to your specific needs, with a wide variety of data fields"; view scanned paper records and computer files in one system; "easily add new lot sales and burials".
- **Mapping**: paper cemetery maps "easily linked to burials and lot owners"; edit and update maps; works on smartphones, tablets, PCs; "cemetery management and the public can quickly locate burials".
- **Document scanning service**: on-site scanning of burial cards, lot cards, ledger books, deeds, maps; scanned records merged with the search database.
- **Public search**: free public burial search across cemeteries that opt in; cemetery accounts are private unless the cemetery allows public viewing.
- Notably absent from the public surface: scheduling, work orders, contracts/payments, CRM. (Lot sales are mentioned as records entries, not as a sales workflow.)

## Cross-product Comparison

| Structure / capability | PlotBox | OpusXenta Byond | webCemeteries | Chronicle | CemeteryFind |
|---|---|---|---|---|---|
| Burial space inventory (identified spaces w/ location, type, capacity, dimensions) | ✓ (plots, types, capacities, dimensions) | ✓ (plot inventory: location, type, capacity, dimensions) | ✓ (locations / grave spaces, depth, property types) | ✓ (plots tracked, map-linked) | ✓ (lots, burial/lot cards) |
| Interment / deceased records (who is buried where) | ✓ (records mgmt, single source of truth) | ✓ (deceased records mgmt) | ✓ (Deceased Module; add decedent to location; disinter; transfer) | ✓ (interments; interment certificates/reports) | ✓ (burial records; public burial search) |
| Ownership / interment rights (deeds, stakeholders, transfers) | ✓ (contracts; plots on hold) | ✓ (rights (deeds) management; ownership + tenure records) | ✓ (interment/burial rights; ownership stakeholders; deed/right-of-interment forms; relocate right) | ✓ (ROI/ownership certificates; deed certificate mgmt) | ✓ (lot owners; deeds scanned) |
| Space state / availability | ✓ (real-time inventory status; heat map) | ✓ (available and sold plots; stock levels) | ✓ (status of grave/burial right; search available property; reserve) | ✓ (map-linked plot status) | ✓ (implied by lot/burial records) |
| Digital cemetery map linked to records | ✓ (drone imagery, verification service) | ✓ (standard → advanced mapping integrations) | ✓ (inventory maps; wall maps; edit grave mapping) | ✓ (interactive map; drone/GIS services) | ✓ (scanned paper maps linked to burials/owners) |
| Burial/service scheduling | ✓ (real-time calendars; burial orders auto-generated; FD portal) | ✓ (burial scheduling; bookings mgmt; online FD bookings) | ✓ (service/event details on deceased; daily interment report; — no dedicated calendar module visible in KB index) | ✓ (event calendar; public event view) | ✗ (not on public surface) |
| Work orders (grounds/interment/memorial) | ✓ | ✓ (burial work orders w/ checklists; grounds tasks; mobile) | ✓ (full Work Orders Module; job types; recurring; map areas; photos) | ✓ (event and work order manager) | ✗ |
| Sales & contracts (pre-need/at-need, payments) | ✓ (contracts & sales; e-sign; payments; finance suite; trust funds) | ✓ (sales mgmt; integrated payments; e-signatures in CorePLUS) | ✓ (Contracts Module w/ pre-need/at-need/combination; price catalog; commissions; payment processing; invoices) | ✓ (sales module; online plot sales) | △ (lot sales recorded as records; no sales workflow) |
| Public / genealogy search | ✓ (EverAfter Connect) | ✓ (public deceased search; public map search — even in Basic tier) | ✓ (Locate a Loved One; Remember My Journey; mobile app) | ✓ (Online Public Access; Life Chronicle) | ✓ (free public burial search) |
| Document management / digitization | ✓ (scanned books/cards/contracts linked to plots) | ✓ (document storage; — digitization service not explicit on fetched pages) | ✓ (Documents; Books module; on-site scanning service) | ✓ (document attachment; digitization service) | ✓ (on-site scanning; merged with database) |
| Memorial / monument management | ✓ (+ mason portal) | ✓ (+ mason permits) | ✓ (Memorials Module; memorial vendors) | △ (niche wall/columbarium display add-on) | ✗ |
| Multi-user roles/permissions | ✓ (permissions per role) | ✓ (multi-user; roles) | ✓ (unlimited users; permissions by role) | ✓ (multiple user access and roles) | △ (account-based; not detailed) |
| Multi-site | ✓ (multiple sites in scheduling) | ✓ (network of locations) | ✓ (enterprise; multiple cemeteries) | ✓ (multi-location cemeteries segment) | ✗ (single cemetery accounts) |
| Care programs (perpetual/annual) | △ (trust fund management in finance) | ✓ (annual and perpetual care programs) | ✓ (perpetual care items in contracts) | ✗ (not on public surface) | ✗ |
| Funeral-director-facing surface | ✓ (FD portal, 24/7 booking) | ✓ (online funeral director bookings) | △ (Passare integration instead) | ✗ | ✗ |
| Crematory module (sibling Type bundled) | ✓ (crematory software) | ✓ (crematory management) | ✗ | ✗ | ✗ |
| Records-only edition | ✗ | △ (Basic tier is close) | ✗ | ✓ (Lite) | ✓ (whole product is records-centric) |

Reading of the table:

- Present in **all five** products: burial space inventory; interment/deceased records; ownership/rights records; space state/availability; map linked to records; public search. These are the Type's stable core (evidence layer B).
- Present in **four of five** (all except the records-centric CemeteryFind): scheduling, work orders, sales/contracts depth, memorial management. These are common mature structure, not defining (evidence layer B).
- Present in **some**: care programs, FD portals, crematory bundling, multi-site, records-only editions — variant/optional (evidence layer B, weaker).
- Product-specific surfaces (evidence layer A only): Arboretum module (webCemeteries), Books module (webCemeteries), mason permits workflow shape (OpusXenta), EverAfter/Life Chronicle public memorials (PlotBox/Chronicle), drone-verification mapping service (PlotBox/Chronicle/webCemeteries as services).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as cemetery management:

```text
Burial Location Inventory
  (the cemetery's grounds decomposed into individually identified,
   state-tracked burial spaces — graves/plots/lots, niches, crypts —
   each addressable within the cemetery's layout)
    └── Interment Record
        (an identified deceased person bound to a specific location at a date;
         the register of who lies where)
```

Two invariants:

1. **Individually identified, state-tracked burial locations.** The cemetery exists in the system as a decomposed inventory of addressable spaces, each with a location identity (e.g., section/row/lot/grave), physical attributes (type, capacity, dimensions), and an operational state (available / reserved / sold / occupied vocabulary varies by product). Remove this → the product is a generic records database or document archive, not cemetery management.
2. **Interment records binding identified deceased persons to specific locations at dates.** The burial register is the heart of the system: who is interred where, and when. Interment occupies the location's capacity and is reflected in its state. Remove this → the product is a property/space inventory without its defining content.

Supporting observations:

- All five sampled products carry both structures (evidence layer B).
- The §24 historical check passes: a parish churchyard register (graves + burial register, no family ownership, no digital map) satisfies both invariants; CemeteryFind (1992, records-centric, no scheduling/work orders/sales workflow) satisfies both; municipal "exclusive right of burial" tenure models satisfy both. Veterans/national cemeteries (interment assigned by eligibility, no plot sales) would also satisfy both — this last case is conceptual inference, not directly researched.
- Deliberately **not** in L0: ownership/sales (a cemetery can operate without selling — churchyards, veterans grounds), scheduling, work orders, maps (location identity can be textual), public search, finance.

### L1 — Common Mature Structure

Present in most modern products; not required to recognize the Type:

- **Interment rights / ownership records** — the legal layer over the inventory: deeds, rights of interment, ownership stakeholders, transfers of ownership, owner profiles. (All five sampled products; vocabulary varies: "rights (deeds)", "right of interment", "lot owner".)
- **Digital cemetery map linked to records** — inventory maps with status coloring; modern implementations use drone/GIS surveys; older implementations link scanned paper maps. Location identity is the invariant; the map is its dominant modern implementation.
- **Burial/service scheduling** — shared calendars for burials/cremations/services; auto-generated burial orders and paperwork; double-booking avoidance; funeral director self-service booking in some products.
- **Work orders** — grave opening/closing, grounds maintenance, memorial installation; job types; mobile field updates with photos; recurring work.
- **Sales & contracts** — available-property search, reservations/holds, contracts with need status (pre-need / at-need / combination), price catalogs, payments, invoices.
- **Public/genealogy search** — public burial search, grave location/walk-to-grave, online memorial pages.
- **Document management & digitization** — scanned deeds, burial/lot cards, ledger books linked to records; migration from paper and legacy systems (often sold as a vendor service).
- **Deceased record enrichment** — obituary, photos, next of kin, veteran/military records, confidential flags.
- **Multi-user roles/permissions**; **reporting** (inventory, interments, activity); **audit/history per record**.

### L2 — Variant / Optional Structure

Depends on segment, geography, regulation, scale, business model:

- **Perpetual/annual care programs** and trust-fund accounting depth (US regional posture; OpusXenta care programs, webCemeteries perpetual care items, PlotBox trust funds).
- **Memorial/monument management** with mason permits and external mason portals.
- **Funeral-director-facing surfaces**: FD portals with online booking; integrations with funeral case-management software (webCemeteries ↔ Passare).
- **Bundled sibling Types**: crematory management (PlotBox, OpusXenta), funeral home management (PlotBox) — combo deathcare operations.
- **Multi-site/enterprise governance** for cemetery networks and archdioceses.
- **CRM, marketing automation, aftercare programs, complaints management, risk assessments/H&S.**
- **Online plot sales** (public e-commerce for pre-need property) and **online memorials / digital cemetery engagement** (public tributes, flower stores).
- **Segment variants**: municipal/council, private/memorial park, religious/archdiocese, veterans, green/natural burial, pet cemeteries, columbarium/mausoleum-heavy (vertical memorialization with 360°/3D mapping).
- **Deployment/edition posture**: cloud multi-user vs desktop heritage; records-only "Lite" editions; records-centric products (CemeteryFind) as a persistent low-end pole.
- **AI assistance** (assistants, obituary generation).

### L3 — Vendor-specific Structure

Stays in Research Notes:

- PlotBox: Eva AI assistant; PlotBox Pay; EverAfter Connect; Vertica Mapping (360° mausolea/columbaria); AI Obituary Assistant; drone mapping with per-point verification service.
- Chronicle: ChroBot assistant; Life Chronicle revenue-sharing memorials; Lite/Pro editions; 3D 360 mausoleum mapping; named certificate set (Interment/Burial, Plot, ROI/Ownership, Work Order); named report set.
- OpusXenta Byond: Basic/Core/CorePLUS tier definitions; mason permit lifecycle (edit/reject/issue/cancel/complete); floral program management; complaints module; risk register.
- webCemeteries: Remember My Journey; Forever Plot; Arboretum Module (tree records/tours); Books Module (scanned register books linked to records); virtual tours; website design service; Passare integration.
- CemeteryFind: Docufree on-site scanning service; Bosscan; free public search network across opted-in cemeteries.

## Vendor-specific Findings

See L3 above. Additional notes:

- The only Tier-1 help center in the sample (webCemeteries) confirms the object model at article granularity: Locations (grave spaces) hold one or more **interment/burial rights**; rights have owners (stakeholders); deceased records attach to locations; contracts carry need status and can include perpetual care items; work orders can be created from deceased records, locations, or invoices; disinterment and right-relocation are supported, exceptional, recorded operations.
- Chronicle's comparison page (vendor-authored) is used only to confirm the category's player set and evaluation criteria, not as feature evidence for competitors.

## Boundary Findings

1. **vs Funeral Home Management** (§29 sibling, unprocessed). The funeral home manages the funeral case: removal and care of the deceased, visitation/viewing, ceremony, disposition paperwork, funeral merchandise. The cemetery manages the ground and the interment: spaces, rights, opening/closing, permanent records. The seam is the case vs the space+interment. Market evidence: webCemeteries integrates with Passare (funeral case management) rather than absorbing it — the seam documented from inside the market; PlotBox bundles both for "combo" operations, but ships them as distinct modules. Removal test: remove the burial space inventory and interment records → funeral home software.
2. **vs Crematory Management** (§29 sibling, unprocessed). The crematory manages the cremation operation: authorizations, chamber scheduling, remains tracking. The cemetery manages burial spaces and interments. PlotBox and OpusXenta bundle both; the modules remain distinct. Removal test: remove the ground/space inventory → crematory software.
3. **vs Enterprise Resource Scheduling Platform / amenity booking** (§10/§17/§26). Cemetery spaces are not time-slot rentals: an interment is permanent, and a "reservation" in cemetery software is a hold on saleable inventory pending contract, not a booking of occupancy over time. Removal test: remove permanence and interment rights, make occupancy time-based → booking system.
4. **vs Property Management** (§17). Property management leases space for money over time to living tenants with leases, rent, and maintenance obligations. Cemetery software sells perpetual interment rights; the "occupant" is deceased; there is no lease cycle. Structural analog only.
5. **vs Genealogy platforms / public records sites**. Public search is an outward-facing feature of cemetery software. Genealogy platforms aggregate records across institutions for family-history research and neither operate ground nor sell rights. The public portal does not make a genealogy product.
6. **vs GIS / mapping products**. The map is a representation layer over the register. GIS products do not hold interment records, rights, or contracts. Several vendors sell mapping as a service (drone survey → digital map) feeding the register.
7. **vs generic records/document management**. CemeteryFind shows that a records-centric product (no scheduling, no sales workflow, no work orders) still belongs to this Type because it holds the space inventory + interment register. But a pure document archive without space/interment structure is records management, not cemetery management.
8. **Taxonomy note (for joint review)**: deathcare vendors increasingly bundle cemetery + crematory + funeral home management in one platform (PlotBox explicitly; OpusXenta cemetery+crematoria). The three directory leaves are distinct operator domains with distinct core objects, but they are often sold as one suite. Flagged for joint review when funeral-home-management and crematory-management are processed.

## Uncertainties

- Exact space-state vocabularies (available/vacant/sold/occupied/reserved/owned) vary by product; no canonical state list is asserted.
- Scheduling depth in webCemeteries is inferred from service/event details on deceased records and the daily interment report; no dedicated scheduling module appeared in the fetched KB index — treated as "scheduling present in most products, form varies".
- Pre-need/at-need vocabulary is directly evidenced only in webCemeteries' help center; treated as industry-common with that anchor, not asserted as universal.
- Perpetual care legal regimes (e.g., US state trust-fund requirements) were not researched; perpetual care is recorded only as a product capability.
- Veterans/national cemetery products were not directly sampled; their fit to L0 is conceptual inference.
- No numeric limits, default values, or precise operational parameters are asserted anywhere — no Tier-1 documentation was reachable for four of five products, and none was needed for the claims made.

## Final Synthesis

Cemetery Management is the operator-side system of record for running a cemetery. Its defining core is small: the cemetery's grounds decomposed into individually identified, state-tracked burial locations, and interment records binding identified deceased persons to specific locations at dates. Everything else the market ships — interment rights and deeds, digital maps, burial scheduling, work orders, sales and contracts, public genealogy search, document digitization, care programs, memorial management, FD portals, multi-site governance — is common mature structure or variant posture layered on that core, and the records-only pole (CemeteryFind, Chronicle Lite) proves the core stands without them.

The Type's center of gravity is the permanent register: cemeteries operate on decade-to-century time horizons, records outlive staff and even the cemetery's sellable inventory, and the system's job is to keep the answer to "who lies where, and what may still be done with this ground" accurate and findable — for the office, the grounds crew, the funeral director, and the public.
