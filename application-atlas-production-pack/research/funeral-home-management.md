# Research Notes — Funeral Home Management

Research date: 2026-09-08
Slug: funeral-home-management
Directory leaf: Funeral Home Management (§29 Home, Family, Personal & Local Services; siblings Cemetery Management — processed 2026-09-06, Crematory Management — processed 2026-09-07)

## Research Goal

Understand what funeral home management software actually is as an Application Type: what objects exist inside it, what funeral home staff do with them, how the core workflows (first call, custody and care of the deceased, arrangement with the family, service execution, disposition paperwork, financial settlement) actually flow, and where the boundary lies against the neighboring deathcare Types (Cemetery Management, Crematory Management — both processed) and against structurally similar Types (CRM, event management, case management).

This pass also carries a deferred obligation: both processed siblings recorded a joint-review flag anticipating this pass (cemetery-management and crematory-management Boundary Issues entries). The three-way seam must be adjudicated from the funeral side.

## Initial Boundary

Initial hypothesis (pre-research):

- Funeral Home Management is the operator-side business system of record for a funeral home: the decedent/funeral case as the organizing record, custody and care of the body, the arrangement conference output (services, merchandise, disposition), statutory paperwork (death certificate data, permits, releases), service scheduling, and case-linked financials.
- Closest neighbors: Crematory Management (the cremation operation), Cemetery Management (burial-space inventory), generic CRM (family relationships), event management (services), preneed platforms (pre-need contracts).
- Suspected variant axes: traditional full-service home vs cremation-society/disposition-only business; staff-led vs family-self-service arrangements; standalone product vs deathcare-suite module; US-centric regulatory shape (GPL, FTC disclosures, EDR) vs other jurisdictions.
- Known market context from sibling passes: deathcare vendors bundle funeral + cemetery + crematory as modules of one suite (PlotBox, OpusXenta); Passare documented as funeral-first case management with barcode chain-of-custody.

## Research Questions

1. What is the core object — is it a "case", what does it attach to, what case types exist?
2. How is custody of the deceased modeled — first call, removal/transfer, location, personal belongings, chain of custody?
3. How is care/preparation recorded (embalming, dressing, appearance) and is it definitional or depth?
4. What is the arrangement — how do family selections become a priced contract, and how does the price list work?
5. How is statutory paperwork handled — vital statistics, death certificate, permits, releases, electronic death registration?
6. How do services get scheduled and staff coordinated (calendar, vehicles, rooms, tasks, whiteboards)?
7. What financial machinery exists (payments, insurance assignments, accounting exports, inventory)?
8. What family-facing surfaces exist (online arrangements, portals, e-signature)?
9. Where is the boundary vs crematory (case-attached cremation record vs cremation register), vs cemetery (disposition as data vs space inventory), vs CRM/event tools?
10. Historical check: would a paper-era funeral home's record system still fit the definition?

## Representative Products

Selection rationale: market representation across the funeral-software market with different product philosophies and customer tiers; two products with reachable Tier-1 help centers anchor operational detail; the suite posture and the website-led posture are sampled to cover packaging variants.

| Product | Role in sample | Segment / philosophy | Evidence tier reached |
|---|---|---|---|
| Passare (Tribute Technology) | Case-first modern cloud system; deepest operational documentation | US funeral homes, mid-market, 2,600+ homes claimed | **Tier-1 help center** (support.passare.com: Getting Started, Managing Your Account, Accounting & Financials, plus 8 full articles) + Tier-2 homepage |
| Parting Pro | Arrangement-first / family-self-service pole; cremation-society segment | US cremation-focused homes and societies, 1,000+ directors claimed | **Tier-1 help center** (help.partingpro.com: Case Management collection, Care tab article) + Tier-2 homepage |
| PlotBox (funeral home module) | Deathcare-suite posture (funeral + cemetery + crematory on one record) | Combo operators, municipalities, enterprise; US/UK/AU | Tier-2 product page (funeral-home-software, US) with detailed feature copy and FAQs |
| Tribute Management Software (TMS) | Operations-first "command center" posture (staff, schedule, assets) | US funeral homes; released Oct 2022; talent from Ionic, SRS Computing, CRäKN | Tier-2 product page with FAQ |
| FrontRunner Professional (Pulse) | Website-led all-in-one posture | US/Canada funeral homes; now part of Tribute Technology | Tier-2 homepage |

Rejected / unavailable:
- CRäKN — transport error ×2; abandoned. (TMS FAQ confirms CRäKN's team/features were absorbed into Tribute Management Software — the lineage is documented from the acquirer's side.)
- SRS Computing — timeout ×2; abandoned. (Same TMS FAQ documents the absorption.)
- Gather — timeout ×2; abandoned.
- HMIS — transport error ×2; abandoned. (PlotBox markets an "HMIS Partnership" page — HMIS exists as a legacy vendor but was not reachable.)
- Facultatieve Technologies — fetched successfully but is a cremator/incinerator **hardware** manufacturer, not funeral home management software; product mismatch, excluded (useful as boundary evidence that equipment control is not this Type).
- Search engines unavailable (consistent with prior runs in this environment).

## Sources

All fetched 2026-09-08:

Passare (Tier-1 unless noted):
- https://support.passare.com/ (help center root)
- https://support.passare.com/getting-started (category: Create a Case, dashboards, internal comms, AI tools, glossary)
- https://support.passare.com/managing-your-account (category: checklists, case management, case types, care center, contract, documents, decedent tracking, payments)
- https://support.passare.com/accounting-financials (category: accounting, financials, reporting, inventory, batch, organization, calendar, price lists, rolodex)
- https://support.passare.com/case-types (article)
- https://support.passare.com/care-center (article)
- https://support.passare.com/goods-and-services (article)
- https://support.passare.com/vitals (article)
- https://support.passare.com/decedent-tracking-dashboard (article)
- https://support.passare.com/standard-forms (article)
- https://www.passare.com/ (homepage, Tier-2)

Parting Pro (Tier-1 unless noted):
- https://help.partingpro.com/en/ (help center root)
- https://help.partingpro.com/en/collections/483651-case-management (collection, 46 articles)
- https://help.partingpro.com/en/articles/14824026-using-the-care-tab-decedent-location-and-personal-belongings (article)
- https://www.partingpro.com/ (homepage, Tier-2)

PlotBox:
- https://plotbox.com/funeral-home-software (US funeral home software page)

Tribute Technology:
- https://www.tributetech.com/tribute-management-software (TMS product page with FAQ)
- https://www.frontrunnerpro.com/ (FrontRunner homepage; Pulse Business System)

Evidence layers used: A = directly observed on a specific product's official documentation; B = observed across multiple sampled products; C = canonical inference from cross-product comparison and boundary reasoning.

## Product A — Passare

### Key observations (evidence layer A unless noted)

**Positioning**: "Funeral home software built for the one who does it all — Case manager. Decedent tracker. Financial guru." All-in-one; 100+ features; 2,600+ funeral homes; 121K family collaborators (vendor-claimed). Users: admins, funeral directors, owners.

**The case is the spine.** Everything hangs off a case:
- Case types (article "Case types"): **At-need** (decedents in your care: biographical/vitals/veteran info, family members & their role in planning, service and disposition scheduling, obituary, contract & payments), **Pre-need** (pre-need contract holders: contact/veteran info, family, obituary/service/disposition wishes, policy info via FDLIC integration, contract; "do not sign Goods & Services" on pre-need; convert to at-need when the time comes), **Imminent-need** (hospice/near passing; same as at-need excluding death details; convert to at-need), **Trade case** (trade work for other funeral homes: embalming, removals, cremations; record the business you do trade work for; invoice another funeral home), **Pet case** (pet death/cremation; owner + veterinarian clinic; contract & invoice), **Cash sale** (ancillary sales: additional death certificates, merchandise; associated to a decedent's case; receipt).
- Case management machinery: copy cases between locations, delete/restore, edit case dates, export, case numbering sequence, case merging (how information transfers), multiple pre-need contracts, self-started cases, transferred cases (data transfer from other systems, adjust goods and services for transferred cases).
- Editable case statuses, case tags, custom fields, client service types (organization settings).

**Vitals = first call + vital statistics on one page** (article "Getting started with Vitals"): configurable per branch (admin permission), field search, collapsible sections; available on At-need, Imminent-need, Trade cases; custom fields and notes cannot be removed; integration-required fields must stay (documented for integrations — EDR integrations need specific fields). "Education & Race Options" are editable organization settings — death-certificate demographic fields.

**Care Center = custody and care of the body** (article "Getting started with the Care Center"): "Use the Care Center to track the care and preparation of a body before services."
- Decedent information: basics (weight, height, who remains were delivered to), identification photos (staff-only, never visible to family).
- Preparation status: dropdown (default Not started / In progress / Complete; customizable), preparation due dates (type, branch, date, time, owner) with notifications.
- **Transfer**: first call information + transfer details; personal items collected at pickup with action needed (e.g., disposed of, stayed with the decedent); print a Personal Items Record; staff sign for personal items.
- **Embalming**: embalming authorization received (when, who gave permission); pre-embalming observations; body markings chart (tattoos/scars annotated on a chart); embalming procedure log (closures, injections with fluid lists, treatments); embalming record (embalmer name, when).
- **Dressing**: outfit description; personal items signed for.
- **Appearance**: hair/cosmetic photos; hair, makeup, manicure, shaving, special care details.
- **Cremation**: cremation container (from Goods & Services); ID tag; pacemaker/jewelry removed; family witnesses selected; cremation tracking events (e.g., "Cremation" event with cremator name and when it occurred).
- **Merchandise**: contract merchandise appears (which urn/casket); ordering details.
- **Tracking**: Location Events History = the chain of custody (locations, user, date/time, notes; voided locations; GPS tool); Tracking ID history (all QR codes assigned to the body); personal items with photos; printable activity reports.
- Notes (@mentions), Care Center checklists (icon turns green when complete).

**Decedent tracking via mobile + QR/barcode** (homepage + barcodetracking page + decedent-tracking-dashboard article): "Assign scannable barcodes to decedents, items, and locations to create a reliable chain of custody… tie those barcodes to a case"; mobile shows current location of items and decedents with a digital record of every handoff and movement; replaces "clipboards, sticky notes, or notebooks". Dashboard: multi-pane case listing with mobile-information columns, auto-refresh.

**Arrangement → contract** (article "Goods and services page"): the contract is built by adding items from the **price list** to the case's **Goods & Services page** (categories, search, Quick-Add for frequent items, discretionary amount/name overrides); disclosures checked and editable; contract printed/emailed via standard forms; **signing** (Yes → lock symbol appears; "very important to sign every case so the goods and services will appear on your accounting and revenue reports"); **re-sign** after modifications — changes show as refund/adjustment (e.g., casket change = old casket refunded, new added); contract changes visibility toggles (on the printed statement — SFG — and on the G&S page).

**Price lists** (category): add/edit items, configure discounts, quick-add, effective dates, packages, schedule future pricing/cost changes. **Inventory**: add/transfer/remove inventory; add inventory to the Goods & Services page.

**Payments & financials** (categories): payments & adjustments page; insurance assignments (enter and track); receipts (create/print, numbering); interest on balances; card & ACH via Deluxe Merchant Services; multiple contracts for at-need (beta); pet & trade invoicing (beta); FEMA invoice; checks (write/manage, approvals, reporting); ledger; batch deposits/payments/forms; accounting exports (QuickBooks Desktop/Online, Sage 50; chart of accounts; accounting lock date); reporting (system reports with descriptions, user reports, survey reports, mail-merge address labels).

**Documents** (category + article): standard forms on the case sidebar (download/print); templates with tags for customization; custom documents; template categories; eSignatures (including on print-&-sign contracts); memorial content; obituary page + obituary templates + AI Obituary Writer.

**Scheduling & coordination**: global schedule; calendar (event types, color-coding, connect your calendar); tasks (getting started, task widget); checklists (create, run reports, use within a case); whiteboards (organize cases with colors/icons/labels); dashboards (case listing, filter tabs, unsigned cases, search, share).

**Family-facing**: Planning Center (category — "everything you need to stay connected with families"); family and friends page on the case; online arrangements; eSignatures; AI Obituary Writer.

**Integrations** (category): print, **answering service** (first-call intake), aftercare, payment, **preneed**, website, **electronic death record (EDR)**, memorial, live streaming, Parting Pro, **cemetery management**.

**Roles & security**: roles & permissions, invite users, SSO, two-factor authentication, user groups, organization messages, notifications.

## Product B — Parting Pro

### Key observations (evidence layer A unless noted)

**Positioning**: "The #1 cremation arrangement software for funeral homes"; all-in-one business solution; 1,000+ funeral directors, 300k families served (vendor-claimed); customer base skews to cremation societies and disposition-only businesses (testimonials: ATX Cremation, Arkansas Cremation, Simple Cremation, etc.). Products: **Case management** + **Online arranger**; services: online marketing, websites, drop-shipped urns.

**Case lifecycle** (Case Management collection, 46 articles):
- Case stages as record classes: **Price shoppers** (inquiry-stage records: "What do I do with a price shopper?", send price-shopper email, notes, reminders, "when a price shopper becomes an active case") → **Pre-need case** (track pre-planners; families submit prearrangement information) → **Imminent case** (deaths that have not occurred; families prearrange for imminent deaths) → **At-need case** (move to at-need once a death has occurred; families choose services and pay).
- Active case operations: assign/update case IDs, add logistics information, mark case complete, archive cases, delete cases.
- **Death certificate working copy verification** (article) — the case carries death-certificate verification workflow.
- Photo sent to family for ID verification.
- Events management; custom outbound emails; task management (task templates); notifications.

**Care tab = decedent location and personal belongings** (article, detailed):
- "Record decedent location, transfers, and personal belongings on every case. Entries are timestamped, attributed to the staff member who made them, and printable as PDFs for compliance or family hand-off."
- Location entries: tracking ID (cremation tag number, internal code, or facility reference), from/to location (from configurable tracking locations: facilities, coolers, prep rooms, partner sites — with addresses), transfer reason (Initial Removal, Preparation, Refrigeration, Viewing/Visitation, Crematory, Cemetery…), date/time, note; newest-first cards; prefilled from previous entry.
- Personal belongings: item name, action (Remain with decedent, Return to family, Dispose, Donate, custom), storage location, item ID, note, photos.
- Generated PDFs: **Decedent Location Report** (chronological chain with staff attribution) and **Personal Belongings Directive** (with Authorizing Agent + Funeral home representative signature blocks — paper sign-off in this release).
- Settings: body tracking (locations + transfer reasons), belonging records (actions + storage locations); deleted values preserved as labels on historical entries.
- FAQ: staff-facing only (families never see the Care tab); no granular Care permissions yet (roadmap); no mobile app yet (roadmap); no QR/barcode scanning yet (roadmap); digital signature on directive on roadmap.

**Contracts & money** (Contract Management + Payments & Accounting collections): create contract, send for signature (remote or e-signed in person), revise a signed contract, invoice↔contract generation, contract template customization, purchaser-address requirement setting; invoices (create/send, split between multiple payers, refunds); online store (families choose services and pay online); reviews after case completion (Google/Yelp/Facebook).

**Family self-service**: online arranger ("families arrange anytime, anywhere without any sales pressure"); families submit prearrangement information; families choose services and pay when a death has occurred.

**Integrations** (13 articles); aftercare texting hub; websites; marketing.

## Product C — PlotBox (funeral home module)

### Key observations (evidence layer A)

- Positioning: "From the first call to the final memorial, PlotBox runs your front office — cases, custody, payments and your website — on one record." Deathcare platform (cemetery + crematory + funeral home lines); 2,000+ facilities / "4,000 deathcare operators" (vendor-claimed); 20+ yrs; ISO 27001/9001.
- Case journey stages named on the page: **First call → Arrangement conference → Obituary & documents → Decedent tracking → Service coordination → Memorialization**.
- **Arrangement management**: "Every case captured in one place, from the first call through to the final arrangement. Your whole team works from the same up-to-date record."
- **At-need & pre-need**: both case types in the same system (FAQ: "one consistent way of working regardless of case type").
- **Chain of custody & QR decedent tracking**: "A transparent, auditable record of where every decedent and their belongings are at every stage — scanned and timestamped from any mobile device." Full body tracking using QR codes and scanners; mobile-ready transfers (case files, route assignments, transfer protocols in the field); eSignatures and document uploads at the point of transfer ("capture critical signatures on glass"); works "even when internet connectivity is low".
- **Digital schedule & locations**: services, arrangement rooms, chapels, visitation rooms and vehicles on one shared real-time schedule "with safeguards against double-booking".
- **Transfer management**: "Log and assign removals to team members and track them through to completion, with case files and routes available in the field."
- **In-house cremation**: "Authorizations, permits and custody checkpoints built into the workflow, so no required step gets missed" (combo-operator posture).
- **Customizable first-calls**: "Tailor your intake forms to capture specific state requirements, permissions, and details instantly."
- **Automated workflows**: trigger custom work orders and task assignments when a case is created; real-time handoffs between transfer staff, arrangers, and directors with mobile notifications; custom statuses for cases and workflow setup with case reassignment.
- **Document management**: "Key documents—from Release Forms to Death Certificates—are organized, accessible, and printable directly from PlotBox."
- **Money**: PlotBox Pay (in person, by link, family portal), reconciliation to the GL, contracts & e-signatures (DocuSign), family portal (upload documents, pre-arrangement questionnaires, balances, pay online), e-commerce & sympathy from the memorial page.
- **AI obituary assistant** (drafts from case record; "nothing is published automatically").
- **Combo operations**: one family record across funeral/cemetery/crematory ("data entered once… no re-keying"); shared scheduling, unified payments; digital mapping; walk-to-grave.
- **Multi-site**: one system across locations, consolidated reporting, role-based permissions (arrangers, crematory staff, grounds teams, head office).
- **Migration**: full historical record migration from legacy MIS (free migration offer for "MIS Pro" customers; contract forgiveness) — evidence that the market it displaces is legacy funeral management systems (HMIS partnership page exists).

## Product D — Tribute Management Software (TMS)

### Key observations (evidence layer A)

- Positioning: "the operational backbone of your funeral home. It brings together case management, scheduling, team coordination, and service planning into one unified system — replacing spreadsheets, whiteboards, and disconnected tools." "Command center."
- **More than case management** (FAQ): "Most management software in the funeral industry is limited to managing cases, whereas TMS takes it a step further by giving you the capability to manage your entire funeral home" — assets (cars, rooms), staff activity, non-case tasks (e.g., mowing the lawn). This FAQ is direct market evidence that **case management is the recognized baseline** of the category and "management" extends around it.
- **Manage your cases**: enter case information once; "all of your paperwork is done online in seconds"; connects to QuickBooks Online, Federated and more; "saving up to 5 hours on every case" (vendor claim).
- **Manage your operations**: track what cars are booked for what services, who is cutting the grass and when.
- **Manage your staff**: invite staff to tasks/services/meetings; see acceptances; reminders; built-in SMS messaging; RSVP to tasks (initials turn yellow until confirmed).
- **Digital whiteboard**: daily schedule cast to any TV in the facility; shows weather.
- **Calendar planning**: staff, rooms, and cars booked; mini calendar while planning an arrangement to confirm availability on the spot.
- **Single entry system**: contacts (e.g., ministers) and case information entered once populate forms and events ("digital rolodex").
- **Online paperwork**: send forms to families electronically to fill out and eSign remotely.
- Cloud-based, any device; website integration (enter once, flows everywhere); Tribute Pay; one ecosystem with Tribute Websites/Store/Pay.
- Lineage (FAQ): released October 2022; "acquisitions were made and talent came from Ionic, SRS Computing and CRäKN."
- Data transfer from current management software offered.

## Product E — FrontRunner Professional (Pulse)

### Key observations (evidence layer A)

- Positioning: "Funeral software made simple… run your entire funeral home from one place." Now part of Tribute Technology.
- **Pulse Business System**: "manage your entire business in one convenient place… From advanced reporting and streamlined accounting to online memorials and important documents."
- Product family: funeral home websites (lead generation, "built-in revenue generators"), marketing services (SEO/social), Pulse business system (management), online memorials (RSVP feature), notifications, EasyID (virtual identification).
- All-in-one framing: "one completely integrated business solution, with one fee, from one company"; founded by a licensed funeral director; 20+ years.

## Cross-product Comparison

| Capability | Passare | Parting Pro | PlotBox (FH module) | TMS | FrontRunner Pulse | Strength |
|---|---|---|---|---|---|---|
| Case per decedent as the organizing record | ✓ (case types; case sidebar; case listing) | ✓ (case IDs; active case; archive/complete) | ✓ ("every case… in one connected record") | ✓ (case management baseline) | ✓ (implied: "run your entire funeral home from one place"; reporting/documents) | B |
| Case types incl. at-need / pre-need (+ imminent, trade, cash sale, pet in some) | ✓ (all six named) | ✓ (price shopper, pre-need, imminent, at-need) | ✓ (at-need & pre-need named) | — (not itemized on page) | — | B (at-need/pre-need), A-single (trade/pet/cash-sale named in Passare) |
| Custody tracking of the deceased (location/transfer events) | ✓ (Care Center Tracking; QR/barcode chain of custody; GPS) | ✓ (Care tab location entries; timestamped, attributed; PDF report) | ✓ (QR decedent tracking; custody checkpoints; auditable record) | — (not surfaced on page) | — | B |
| Personal belongings recorded with disposition actions | ✓ (items with actions, signatures, photos) | ✓ (belongings with actions, storage, photos, directive PDF) | ✓ ("decedent and their belongings") | — | — | B |
| Care/preparation recording (embalming/dressing/appearance) | ✓ (full embalming log, dressing, appearance) | — (not in Care tab; roadmap for more) | partial (custody checkpoints; in-house cremation authorizations) | — | — | A-single (Passare deep; treat as depth, not invariant) |
| Arrangement recorded on the case (services/merchandise/disposition) | ✓ (Funeral options page; Goods & Services) | ✓ (families choose services; online arranger) | ✓ (arrangement management; arrangement conference stage) | ✓ (service planning) | ✓ (implied) | B |
| Priced from a maintained price list → contract | ✓ (price lists; G&S; sign/lock; re-sign refunds) | ✓ (contracts, invoices, online store) | ✓ (contracts & e-signatures; payments) | ✓ (paperwork populates; QuickBooks) | ✓ (accounting) | B |
| Statutory data & documents (vitals/death certificate/permits/releases) | ✓ (Vitals page; standard forms; EDR integrations; education/race options) | ✓ (death certificate working copy verification; ID verification photo) | ✓ (Release Forms to Death Certificates; state-requirement first-call forms; in-house cremation authorizations/permits) | ✓ ("all the documents right there" testimonial; forms populate) | ✓ (important documents) | B |
| Service & resource scheduling (calendar; rooms/vehicles/staff) | ✓ (global schedule; calendar; event types) | ✓ (events management) | ✓ (digital schedule: services, rooms, chapels, vehicles; double-booking safeguards) | ✓ (calendar planning: staff/rooms/cars; whiteboard) | — | B |
| Tasks/checklists/staff coordination | ✓ (tasks, checklists, whiteboards, notes) | ✓ (task templates; notifications) | ✓ (work orders, task assignments, handoffs) | ✓ (RSVP tasks, SMS) | — | B |
| Family-facing collaboration (online arrangements/portal/e-sign) | ✓ (Planning Center; online arrangements; eSignatures) | ✓ (online arranger; families pay online) | ✓ (family portal; online arranger; DocuSign) | ✓ (online paperwork e-sign) | ✓ (online memorials; RSVP) | B |
| Payments & case-linked financials | ✓ (payments, insurance assignments, receipts, interest, batch, checks, ledger) | ✓ (invoices, split payers, refunds, store) | ✓ (PlotBox Pay, GL reconciliation) | ✓ (QuickBooks Online, Tribute Pay) | ✓ (streamlined accounting) | B |
| Accounting exports / bookkeeping integration | ✓ (QuickBooks Desktop/Online, Sage 50, lock date) | ✓ (payments & accounting collection) | ✓ (reconciled to GL) | ✓ (QuickBooks Online, Federated) | ✓ (accounting) | B |
| Merchandise inventory | ✓ (inventory module; add to G&S) | ✓ (drop-shipped urns; online store) | — (not surfaced on FH page) | — | — | B (thinner) |
| Obituary authoring/publishing | ✓ (obituary page, templates, AI writer) | — (websites service) | ✓ (AI obituary assistant; website sync) | ✓ (website integration) | ✓ (online memorials) | B |
| Mobile field app | ✓ (Passare Mobile; scan; GPS) | — (roadmap) | ✓ (mobile-first transfers; low-connectivity tolerance) | — (cloud any-device) | — | B |
| Multi-location / branches | ✓ (copy cases between locations; branch-scoped configs) | — (not surfaced) | ✓ (multi-site one system; role-based permissions) | ✓ (locations on whiteboard) | — | B |
| Answering-service / first-call intake integration | ✓ (answering service integrations; AI scanner for first call) | — (price shoppers captured as records) | ✓ (customizable first-calls) | — | — | B (thinner) |
| Preneed machinery | ✓ (pre-need cases; preneed integrations; FDLIC policy view) | ✓ (pre-need cases; family-submitted prearrangements) | ✓ (at-need & pre-need in one system) | — | — | B |
| Reviews / aftercare / marketing | — (aftercare integrations; surveys) | ✓ (reviews; aftercare texting hub; marketing) | ✓ (sympathy/e-commerce) | — | ✓ (marketing services) | B (variant territory) |
| Price shoppers (inquiry-stage records) | — | ✓ (named concept with lifecycle) | — | — | — | product-specific |

Stop-condition check: the core model is explainable; the main workflows (first call → custody → arrangement → service → disposition → settlement) are documented at operational granularity from two Tier-1 KBs; stable cross-product commonalities have emerged; further products would mostly repeat this evidence. Research stops here.

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as funeral home management:

```text
Funeral case of record
(one persistent, identified case per deceased person,
 from first call through final disposition — the container)
├── Custody & care of the deceased
│   (the body is in the home's care: removal/transfer and location events,
│    personal belongings with dispositions — the chain of custody)
├── The arrangement
│   (the family-composed plan — disposition method, services, merchandise —
│    recorded and priced on the case as its contract)
└── Statutory identity & authorization data
    (vital statistics / death-certificate data, disposition authorizations
     and permits, release forms — carried on the case and produced from it)
```

Removal tests:

- Remove the **case of record** → scattered tools (a spreadsheet, a wall calendar, a paper file); there is no system.
- Remove **custody & care** → an event planner with a forms clerk: nothing tracks the body the home is responsible for.
- Remove the **arrangement** → a custody log plus paperwork: no funeral is being planned or sold; the family's plan has no record.
- Remove **statutory data & authorization** → a CRM with a calendar: the legal spine of funeral service (who died, may we care for and dispose of this person, may we release them) disappears.

Jointness is load-bearing: case + custody without arrangement = decedent custody tracker; arrangement + paperwork without case/custody = event planning with forms; case + arrangement without custody/paperwork = CRM + calendar.

Evidence support: case-per-decedent (all five products); custody/location events with belongings (Passare Care Center + QR tracking; Parting Pro Care tab; PlotBox QR decedent tracking); arrangement → priced contract (Passare G&S/signing; Parting Pro contracts/store; PlotBox contracts; TMS paperwork; Pulse accounting); vitals/statutory data and documents (Passare Vitals + standard forms + EDR; Parting Pro death-certificate verification; PlotBox release forms/death certificates/state-requirement first calls; TMS "all the documents right there").

### L1 — Common Mature Structure

Very common across the sampled mature products, not definitional:

- **Case types and conversion paths** — at-need / pre-need / imminent-need as the common trio; trade cases, cash sales, pet cases in some products; pre-need/imminent convert to at-need.
- **Service & resource scheduling** — shared calendar for services/visitation; rooms, chapels, vehicles, staff as bookable resources; double-booking safeguards; color coding.
- **Task/checklist/whiteboard coordination** — per-case tasks and checklists, staff assignment with acceptance/reminders, daily whiteboards (digital or cast to displays), internal notes/@mentions/SMS.
- **Price list → goods & services → contract** — maintained price list (items, categories, packages, discounts, effective dates), per-case selection, disclosures, contract generation, signing (e-signature or print-&-sign), re-sign producing refunds/adjustments.
- **Payments & case-linked financials** — payments/adjustments, receipts, insurance assignments, card/ACH, batch deposits, invoicing (incl. trade/pet), accounting export to bookkeeping systems (QuickBooks/Sage-class), checks/ledger at the deepest pole.
- **Merchandise inventory** — caskets/urns as inventory items linked to the price list and the case.
- **Document/template machinery** — standard forms on the case, custom templates with merge tags, obituary authoring/publishing.
- **Family-facing collaboration** — online arrangements, family portals (documents, balances, payments), e-signature, planning pages.
- **Dashboards & reporting** — case listing with filters/statuses/tags, configurable dashboards, system/user reports, survey/review capture.
- **Roles, permissions, multi-location** — role-based access, branches/locations, consolidated multi-site reporting.
- **Mobile field apps & scanning hardware** — QR/barcode chain-of-custody scanning, GPS location events, signatures on glass (where present).
- **Integration spine** — answering services (first-call intake), print providers, electronic death registration, preneed providers, payment processors, websites, live streaming, aftercare, cemetery management systems.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- **Operator posture**: traditional full-service home vs cremation-society / disposition-only business (the Parting Pro pole — online-arranger-led, price-shopper funnel, drop-shipped merchandise) vs combo operator (funeral + cemetery + crematory on one family record — the PlotBox pole) vs trade-services provider (trade cases serving other homes).
- **Family-facing depth**: staff-led arrangements with family e-signature vs family self-service arrangements completed online before/without staff sessions.
- **Custody mechanism**: manual timestamped location entries (Parting Pro's current release) vs QR/barcode scanning with GPS and mobile apps (Passare, PlotBox) — mechanism varies, custody tracking itself is invariant.
- **Care-recording depth**: full embalming/dressing/appearance logs (Passare) vs custody-only (Parting Pro) — depth, not membership test.
- **Preneed handling**: native preneed cases + conversion vs integration with preneed insurance/trust providers.
- **Regional shape**: the sampled products are US-centric (GPL-style price lists with disclosures, death-certificate demographics, EDR integrations, insurance assignments); UK/EU/regional shapes were not directly sampled — the L0 reads jurisdiction-neutral (vital statistics, authorizations, permits exist everywhere; vocabulary varies).
- **Packaging**: standalone funeral-first product vs deathcare-suite module vs website-led all-in-one (FrontRunner/Tribute family) — the same core sold three ways.
- **Adjacent services bundled**: websites, marketing, aftercare, reviews/reputation, sympathy e-commerce, live streaming — commerce/growth extensions, not the Type.

### L3 — Vendor-specific Structure (Research Notes only)

- Passare: Care Center section structure (preparation statuses/due dates, embalming authorization + injections/fluid lists + body-markings chart, dressing, appearance, cremation section with cremator name/witnesses/ID tag/pacemaker-jewelry removal); SFG (statement of funeral goods) contract-changes visibility toggles; case numbering sequence; accounting lock date; batch deposits/forms; rolodex; branch-scoped Vitals configurations; FEMA invoice; Graystone survey reports; FDLIC preneed policy integration; Deluxe Merchant Services; AI Scanner (first-call/vitals intake); AI Obituary Writer; whiteboards; unsigned-cases finder; 2,600+ homes / 121K family collaborators / 96% approval claims.
- Parting Pro: price shoppers as a first-class record class with email reminders and conversion; online arranger with money-back guarantee framing; drop-ship urn service; aftercare texting hub; reviews (Google/Yelp/Facebook) sent after completion; Care-tab release boundaries (no granular permissions, no mobile app, no QR scanning, paper-signature directive — all roadmap items); 1,000+ directors / 300k families / ROI claims ($60–80 contract lift, 2 hours saved).
- PlotBox: Eva AI assistant; EverAfter Connect website (family online arranger, portal, sympathy e-commerce); PlotBox Pay; DocuSign integration; QR body codes with low-connectivity tolerance; HMIS partnership + free MIS migration + contract forgiveness; combo one-family-record framing; 2,000+/4,000 facilities / 99% retention claims.
- TMS: digital whiteboard cast to TV with weather; RSVP tasks with yellow-initials confirmation; built-in SMS; mini-calendar during arrangement planning; single-entry rolodex; released Oct 2022; talent from Ionic/SRS Computing/CRäKN; QuickBooks Online + Federated integrations; ROI calculator; "up to 5 hours per case" claim.
- FrontRunner Pulse: EasyID virtual identification; online memorials with RSVP; website "built-in revenue generators"; one-fee all-in-one framing.

## Vendor-specific Findings

See L3. Additional observations:

- The market has consolidated: Tribute Technology now spans Passare, TMS, FrontRunner, Parting Pro (integration partner), Tribute Websites/Store/Pay; TMS's own FAQ documents absorbing Ionic, SRS Computing, and CRäKN. PlotBox partners with (and migrates from) HMIS. Consequence: several legacy vendor domains are dead or absorbed; the sampled set is dominated by the consolidated groups — recorded as a sampling caveat.
- Two sampled products (Passare, PlotBox) explicitly support **trade/pet/cremation-adjacent** work inside the funeral case (trade cases; in-house cremation with authorizations/permits/custody checkpoints; pet cases) — the funeral case system stretches over adjacent deathcare work without becoming those Types.
- No sampled product surfaces cremator/retort equipment control; the one cremator-hardware vendor encountered (Facultatieve Technologies) sells machines, not management software — boundary evidence.

## Boundary Findings

1. **vs Crematory Management** (§29 sibling, processed). The funeral home holds the **case**: family, arrangement, custody of the deceased, disposition paperwork. The crematory holds the **operation**: booking, authorization paperwork, the cremation register, remains custody and release. Evidence from the funeral side: Passare's Care Center has a *Cremation section on the case* (cremator name, when it occurred, witnesses, ID tag) — a case-attached record of the event, not a register with remains-release workflow; Parting Pro models "Crematory" as a *transfer location* (a place the decedent moves to); PlotBox ships "in-house cremation" as authorizations/permits/custody checkpoints *built into the funeral workflow* for combo operators, while its separate crematory line holds the register. Removal test: remove the case/family/arrangement and keep booking + register + remains custody → crematory management; keep the case and hand the deceased to the crematory → funeral home management. **Joint review discharged from this side — see Taxonomy note below.**
2. **vs Cemetery Management** (§29 sibling, processed). The cemetery holds the **ground**: identified burial locations, interment register, interment rights. The funeral home records disposition *as data on the case* (cemetery/crematory name, date) — no space inventory, no deeds. Passare ships a "Cemetery Management Integration" (integration seam, not absorption); PlotBox's combo framing ("one family record" across funeral and cemetery) keeps the modules distinct. Removal test: add identified burial locations and interment rights → cemetery management.
3. **vs CRM** (§07). The family relationship is recorded (family members with planning roles, pre-need prospects, price shoppers in one product), but the organizing object is the decedent case with custody and statutory obligations, not a sales pipeline over living customers. Parting Pro's price shoppers are the CRM-ish pole — inquiry records that convert to cases — and even there the case is the destination. Remove custody + paperwork + arrangement → CRM.
4. **vs Event Management / scheduling platforms** (§26, §03). Services (visitation, ceremony) are scheduled, but a funeral service is bound to a decedent case with custody obligations and statutory paperwork; rooms/vehicles are resources of the home, not rentable inventory. Remove the case/custody/paperwork → event planning or resource scheduling.
5. **vs Preneed platforms**. Pre-need appears as a case type (wishes, contracts, conversion to at-need) and via integrations with preneed insurance/trust providers; the regulated preneed sales/trust machinery itself is adjacent territory. The funeral system records and converts; it does not administer the trust.
6. **vs Aftercare / memorial / grief-support platforms**. Obituaries, online memorials, aftercare messaging, sympathy commerce are outward-facing extensions bundled by several vendors; the Type's center is the operator's case loop.
7. **vs generic case management** (§10/§24). The funeral case is a domain case: decedent identity, custody chain, arrangement-as-contract, statutory data. Generic case management lacks all four domain semantics.

**Taxonomy note (joint review discharge).** Both processed siblings deferred a three-way joint review to this pass. Adjudicated from the funeral side: **keep-both (three domain Types) RATIFIED.** The three cores are distinct and independently deployable: cemetery = space inventory + interment register + rights; crematory = operation register + authorization paperwork + remains custody; funeral home = case + custody + arrangement + statutory data. Market structure confirms "three domain Types sold as one suite": PlotBox ships funeral/cemetery/crematory as distinct modules sharing one family record; Passare integrates *to* cemetery management systems rather than absorbing them; Parting Pro treats the crematory as a transfer location. The consolidated-deathcare-platform alternative view is recorded but not adopted; no directory change recommended.

## Sampling Limitation

- Two Tier-1 help centers were reachable (Passare, Parting Pro) and anchor the operational claims; the other three products are evidenced at product-page granularity (capability existence asserted; precise states/limits/defaults not).
- Search engines were unavailable; several legacy vendors (SRS Computing, CRäKN, Gather, HMIS) were unreachable — two of them documented as absorbed into Tribute Technology from the acquirer's side. The sample therefore skews toward the consolidated groups and toward US products; a UK/EU funeral-management product was not directly sampled (the one EU vendor encountered sells cremation equipment).
- Claims derived from vendor marketing pages (customer counts, time savings, retention) are labeled vendor-claimed and treated as Tier-3 corroboration.

## Uncertainties

- Exact case-status vocabularies and workflow gate logic (e.g., whether a case can be signed before paperwork completes) were observed only at the granularity the KBs disclose; conceptual states are asserted, exact labels vary by product.
- Whether any product enforces a hard block between custody steps (e.g., cremation section requiring authorization first) is not evidenced; PlotBox's "custody checkpoints built into the workflow" suggests enforcement exists in at least one product, but the mechanism was not observed at rule granularity.
- UK/EU/regional funeral software shapes (direct-cremation providers, funeral directors under UK regulation) were not sampled; the jurisdiction-neutral reading of the L0 is inference (C-layer), not direct observation.
- Preneed depth (trust accounting, regulated preneed sales administration) was not researched; only the funeral system's preneed case/integration surface is asserted.
- The "management vs case management" scope question (does the Type include facility/asset/fleet management?) is resolved as: case spine definitional, whole-operations extension common-mature (TMS's own FAQ frames it as "more than case management") — but the boundary of "the whole business" (payroll? marketing?) is vendor-dependent and not canonical.
- Pet-case and trade-case fit to L0 is direct for Passare (named case types with contracts) but single-product; treated as variant coverage of the same core.

## Final Synthesis

Funeral Home Management is the operator-side business system of record for a funeral home, and its world is organized around the **funeral case**: one persistent, identified case per deceased person, opened at the first call and closed at final disposition. Four structures are held jointly on that case: the custody and care of the deceased (where the body is, every transfer, the belongings that came in with them); the arrangement (the family-composed plan of disposition, services, and merchandise, priced from the home's price list and confirmed as the case's contract); the statutory identity and authorization data (vital statistics for the death certificate, authorizations and permits, release forms); and the case itself as the container every workflow hangs from. Everything else the market ships — case types and conversions, scheduling of rooms/vehicles/staff, tasks and whiteboards, payments and accounting exports, inventory, document templates, family portals and online arrangements, dashboards, mobile scanning, integrations to answering services/EDR/preneed/websites/cemetery systems — is common mature structure or variant posture layered on that spine.

The Type's center of gravity is the case plus the chain of custody: a funeral home's defining obligations are that the deceased in its care is always accounted for, that the family's plan is recorded and paid for as a contract, and that the legal paperwork for death, disposition, and release travels with the case. Cemetery software holds the ground; crematory software holds the operation; funeral home software holds the case and the family.
