# Research Notes — Elevator Service Management

Research date: 2026-09-10
Leaf: Elevator Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services)
Slug: elevator-service-management

## Research Goal

Understand what "Elevator Service Management" software actually is in the real market: what objects it manages, how elevator/escalator service work flows through it, what is elevator-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings — especially fire protection as the other compliance-pole trade, CMMS/building maintenance, OEM IoT operator platforms, owner-side compliance management, construction project management).

This pass discharges the cross-reference left by the fire-protection-service-management pass ("Elevator Service Management | trade sibling (unprocessed) | expected same pattern — code-mandated periodic inspections with certificates and deficiencies; cross-reference when processed") and the family-structure expectation it recorded (fire protection and "likely elevator" carry defining trade structures, unlike the trade-tuned siblings).

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of an elevator/escalator (vertical transportation) service contractor: maintenance, repair, callbacks, periodic safety tests, modernization of elevators, escalators, moving walks, and related conveyances at customer buildings.
- Core objects likely: customer/building, the individual conveyance unit (car) as a regulated asset, maintenance service agreement (MSA/AMC), callback/breakdown ticket, periodic test record, certificate of operation, violation/deficiency, technician route, invoice.
- Elevator-specific candidates: per-unit code-mandated test cadence (ASME A17.1 Category 1/3/5 class regimes), certificates per unit, MSA scope tiers (full-maintenance vs T&I vs lubrication-only), callback economics (billable/non-billable split, callback rate), entrapment emergency response, modernization as second revenue engine, mechanic certification gating (CET/QEI/mechanic card), controller-brand-aware dispatch.
- Closest neighbors: Small Business Field Service Management (generic FSM spine), Fire Protection Service Management (compliance-pole sibling), CMMS/Building Maintenance Management (asset-ownership line — owner-side), OEM IoT operator platforms (KONE 24/7 Connected, Otis ONE, Schindler Ahead, TK MAX — complements), owner-side compliance/contract management (ATIS Alert, OxMaint class — different operator), Construction Project Management (modernization/installation projects).
- Key open question: does the elevator trade carry a *structurally distinct* trade object (the fire-protection pattern), or is it trade-tuned generic FSM (the electrical/HVAC pattern)?

## Research Questions

1. What objects make up the system (customer, building/bank, unit/car, MSA/contract, callback, test, certificate, violation, work order, invoice)?
2. How is the recurring maintenance program structured (contract types, scope tiers, visit cadence, per-unit clocks)?
3. How does callback/breakdown/emergency response work (entrapment, SLAs, dispatch, callback history per unit)?
4. How do periodic safety tests and certificates work (test categories, jurisdiction variation, expiry tracking, witness tests)?
5. What is the deficiency/violation lifecycle (discovery, tracking, cure deadlines, conversion to quotes/work)?
6. How does billing flow (recurring contract billing, callback billable/non-billable, repair quotes, modernization projects, accounting sync)?
7. How do the poles differ: elevator pure-play vs generic FSM with an elevator vertical vs inspection-company vs CMMS; US ASME regime vs UK/Germany/EU/India regimes?
8. Historical check: would a paper-era elevator service company still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| FieldCamp | vertical-specialist FSM pure-play; typed elevator data model (Property → Bank → Car), MSA-centered, AI dispatch; explicitly positions against generic FSM and OEM platforms | Tier 2 (industry page with operational FAQ + linked product docs) |
| ElevatorPlus | elevator pure-play (global, India-built, US/UK/EU/Gulf pages); 28-module business system; compliance-and-inspection-first framing ("built for ASME A17.1 compliance, not adapted for it") | Tier 2 (product + compliance pages with operational FAQs) |
| LiftGrid | elevator pure-play, EU/Türkiye regional pole; 12 modules; compliance & inspection hub with document-expiry machinery; TR e-Fatura invoicing | Tier 2 (features page, module-level detail) |
| Smart Service | generic FSM (QuickBooks add-on) with a dedicated elevator industry page — the "horizontal FSM serving the trade" pole; cert-driven cycle-based work framing | Tier 2 (industry page with operational FAQ + schema feature list) |

Named in the market but not directly researched (recorded as context, not evidence): LiftKeeper, FIELDBOSS (on Microsoft Dynamics 365), ElevatorApp, Essential (asset-based generic with elevator page), Guspora/KomplyOS/Maintoro (inspection/CMMS poles), AVIA (India pole), OxMaint (facility-side CMMS), ATIS (third-party inspection vendor + owner-side compliance software), OEM IoT platforms (KONE 24/7 Connected, Otis ONE, Schindler Ahead, TK MAX), enterprise OEM tools (Otis ALMA, KONE legacy, Lifeline).

## Sources

Fetched 2026-09-10:

- FieldCamp (Tier 2): https://fieldcamp.ai/elevator-maintenance/ — elevator industry page: data model, MSA scope card, Cat-1/Cat-5 cadence, entrapment workflow, callback ledger, deficiency→modernization, recurring billing, FAQ (explicitly documents what the product does NOT ship)
- ElevatorPlus (Tier 2): https://elevatorplus.app/compliance-and-inspection — compliance & inspection page: per-elevator scheduling, certificate storage, per-lift service history, QR access, checklists, audit trail, regulatory frameworks, FAQs; https://www.elevatorplus.app/ and https://www.elevatorplus.app/elevator-service-software-usa (from search capture) — module map, AMC/breakdown/PM framing, US regulatory table (US/UK/Germany/Canada), generic-FSM differentiation FAQ
- LiftGrid (Tier 2): https://getliftgrid.com/features — 12 modules: preventive maintenance operations, faults & work orders, compliance & inspection hub, technician mobile app, invoicing/e-Fatura, property manager portal, contracts & auto-renewal, proposals/e-signature, spare parts, reports, notifications, AI tools; positioning FAQ vs generic FSM
- Smart Service (Tier 2): https://www.smartservice.com/industry/elevator-service-software — elevator industry page: per-car equipment records, entrapment callback triage, PM agreement cycles, jurisdiction inspection cycles, multi-day repair shift handoffs, violation cure tracking, QuickBooks-native billing, six-stage workflow, portal, FAQ

## Product A — FieldCamp

### Key observations (evidence layer A unless noted)

- Positioning: "Elevator maintenance software for the contractors who keep the cars running — and the MSAs renewing." Audience: independent elevator contractors / ISP (independent service provider) companies, "from a two-mechanic shop to a multi-state ISP."
- **Typed elevator data model**: Property → Bank → Car nested serviceable records, with controller brand, drive type, install year, Cat-1/Cat-5 due dates, MSA scope, and open deficiencies as first-class fields. "The horizontal FSMs flatten all of it into Customer → Asset." Inspection Certificate is a parent-child custom object with number, fees, expiration. Controller brand drives dispatch: "Otis 411, KONE LCE, Schindler Miconic, TK TCM — controller brand on every car so dispatch routes the mechanic with the right diagnostic tool on the truck."
- **MSA as the revenue backbone**: "Half of every contractor's revenue runs on the Maintenance Service Agreement." MSA modeled as a standing service agreement with full-maintenance, T&I (time and materials), OEM-parts, and lubrication-only templates. Contract terms attach once and ride every monthly invoice. One recurring job record per car generates monthly PM visits, annual Cat-1, and 5-year Cat-5 witness tests; recurring invoice closes the loop. Cat-5 (the AHJ-witnessed touchpoint) is the renewal-conversation lever, surfaced 90 days out.
- **Test cadence**: "ASME A17.1 sets the calendar — annual Cat-1, three-year Cat-3 hydraulic, five-year Cat-5 load test." Job templates auto-attach required skill (NAEC CET for Cat-1 sign-off; NAESA QEI-1 for Cat-5 witness), duration, checklist, products (test weights). "Hierarchical skills keep an IUEC apprentice off a Cat-1 sign-off." No A17.1 §8.6.1 MCP generator shipped — the rolling history of completed inspection forms per car is the audit trail handed to the AHJ.
- **Entrapment workflow**: "Entrapment is the only word the building owner cares about — the industry SLA is sixty minutes from call to on-site." Inbound (SMS from building super, after-hours VoIP with transcript, WhatsApp, OEM IoT webhook) lands in a unified inbox auto-linked to the Car record; AI Dispatcher proposes closest qualified mechanic gated on skill (mechanic-card holder, controller-brand diagnostic tool on truck); live-ETA link to the super; offline mobile forms in machine rooms. Entrapment is a high-priority job type; the 60-minute SLA is a buildable dashboard, not a built-in widget.
- **Callback ledger**: callback rate split — billable, non-bailble [sic: non-billable], repeat-within-thirty-days — "the three numbers that forecast an MSA cancellation." Per-visit job logs roll labor/miles/expense to the parent job so the repeat-callback car shows true profitability. "Three door-operator callbacks in sixty days is not a maintenance problem — it's a modernization quote waiting to be sent."
- **Deficiency → quote → modernization**: open deficiencies first-class; good/better/best modernization estimate from callback patterns; e-signature; 30% deposit on signature; multi-day jobs (many visits under one parent); no AIA G702/G703 progress billing (documented honestly).
- **Money**: monthly MSA invoice auto-drafted, card auto-charged (Stripe, retry logic), QuickBooks/Xero/Wave sync; pricebook bundles ("Annual Cat-1 + Inspection Cleaning" lump-sum); property-manager portal (invoices, cert PDFs, open deficiencies, schedule-next-visit).
- **Market map (vendor's own framing)**: Lane A — OEM IoT operator platforms (KONE 24/7 Connected, Otis ONE, Schindler Ahead, TK MAX) live inside the asset; fault alerts become callback tickets — "complements, not competition." Lane B — vertical-specialist FSMs (LiftKeeper, FIELDBOSS, Smart Service, ElevatorPlus, ElevatorApp). Lane C — horizontal FSMs with an elevator landing page (Joblogic, ServiceTitan, BuildOps) — "no Property → Bank → Car, no Cat-1/Cat-5 cadence, no MSA scope card."
- UK/EMEA shops run the same platform as lift maintenance software with WhatsApp inbound/outbound.

## Product B — ElevatorPlus

### Key observations

- Positioning: "Elevator service management software to automate your business"; "built for ASME A17.1 compliance, not adapted for it"; "built specifically for elevator maintenance contractors, not adapted from generic field service software." Global footprint claims (200+ elevator businesses, 20+ countries); India-built (Accucia Softwares, EECMAI member) with country-specific pages (US, UK, Gulf, Europe, ANZ, SE Asia, Canada, Africa).
- Module map (28+ modules): Sales & CRM (lead capture, quick quotation, approvals, digital signatures, change orders); Service Operations (mobile app, AMC management, breakdown management, customer portal, inspection management, field tracking); Installation & Projects (project management, BOM, work order & subcontractor); Material & Warehouse (inventory, multi-branch); Finance (payments, multi-currency); HR (HRMS, expense, asset management); Admin (access control 100+ roles, document automation, 17 languages); AI & integrations (WhatsApp automation 30+ triggers, AI assistant).
- **Compliance & inspection page** (the trade's signature): annual inspection scheduling per elevator with alerts and overdue escalation; digital certificate storage per elevator; complete timestamped service history per lift (PM visits, breakdowns, repairs, inspections, parts replaced — each entry with technician name, date, photos, completion report); QR code on any elevator → full service history, last inspection date, certificate status, outstanding issues ("field technicians and inspectors can verify on the spot"); customizable inspection checklists aligned to ASME A17.1, CSA B44, ISO 25745, or local regulatory bodies; immutable audit trail ("ready for legal, insurance, or regulatory audits"); portfolio compliance dashboard (inspection-due / overdue / upcoming across branches and clients).
- **US-page compliance specifics**: "Category 1 and Category 5 periodic tests are scheduled, recorded and stored against each unit, with QEI witness-test coordination and violations tracked from issue through to clearance with the AHJ. Maintenance Control Program documentation lives on the unit record, where an inspector expects to find it." Multi-state operation: mechanic licences and credentials tracked with expiry dates by state; "the code edition in force varies by jurisdiction, records are held per unit so you defer to the local AHJ."
- **Regulatory table** (US page): US — Cat 1/Cat 5 tests, ASME A17.1/CSA B44, per jurisdiction's adopted edition, AHJ + state elevator board; UK — thorough examination under LOLER 1998 reg 9, six-monthly (passenger lifts) / twelve-monthly (goods-only), HSE or local authority; Germany — Hauptprüfung/Zwischenprüfung under BetrSichV, at most every two years with midpoint interim, ZÜS; Canada — same ASME A17.1/CSA B44 code with per-unit MCP records.
- **Generic-FSM differentiation FAQ**: "Generic field service tools treat an elevator as a work order. ElevatorPlus treats it as a regulated asset with a code-mandated test schedule, a Maintenance Control Program, and an inspection history that has to survive an audit. Contractors switch at the point where the compliance side stops fitting inside a work-order tool."
- Parts inventory at warehouse and truck level; consumption logged against the job; reorder points "flag before a callback turns into a second visit."

## Product C — LiftGrid

### Key observations

- Positioning: "Elevator maintenance software built for elevator service companies — not adapted from a generic field service tool." "From fault report to paid invoice — in one workflow." EU/Türkiye regional pole (TR e-Fatura/GİB invoicing; LiftGrid Systems GmbH; Turkish-language version).
- Twelve modules on one panel, all sharing the same building/elevator/customer record: preventive maintenance operations (monthly maintenance plan, overdue jobs, per-elevator history with photo evidence, digital signature, service form); faults & work orders (fault logging/prioritization, technician assignment/routing, response-time tracking, closure report + customer notification); **compliance & inspection hub** (registration records, periodic inspection reports, certificates, applications, conformity documents — camera-scanned or PDF, auto-bound to the right building/elevator; 90/60/30/7-day expiry alert chain to technician, operations manager, and building contact; draft/awaiting-signature/approved/rejected status flow; 5-year compliance history per building and elevator); technician mobile app (daily job list, offline, photos, signatures, parts-used logging); invoicing/collections/receivables (TR e-Fatura, open balances, online payment links); property manager portal (fault reporting, history, documents, invoices); maintenance contracts & auto-renewal (tiered silver/gold/platinum pricing, per-elevator billing, SLA timers + breach notifications); proposals & e-signature (catalog-based, WhatsApp/email delivery, signed proposal → live contract in one click); spare parts & inventory (OEM parts catalogs for KONE, Otis, Schindler, ThyssenKrupp, Mitsubishi pre-loaded; van + warehouse stock); reports & analytics (technician/region performance, response times, SLA compliance, compliance rates); WhatsApp/SMS notifications; AI petition generator/document OCR/compliance assistant (coming soon).
- Positioning FAQ vs generic FSM: "Generic field service platforms don't understand buildings, elevators, periodic inspection, or TR e-Fatura logic. LiftGrid is designed for the sector — no customization required." "Buildings, elevators, shafts, certificates, and maintenance history are modeled natively. Not crammed into generic 'asset' or 'ticket' fields."
- Onboarding: CSV portfolio import ("every building, shaft, and elevator mapped in minutes"), 14-day to first live dispatch.

## Product D — Smart Service (generic FSM pole)

### Key observations

- Positioning: generic field-service platform (QuickBooks add-on, My Service Depot) with a dedicated elevator industry page: "Elevator service software built around how dispatch handles entrapment callbacks, multi-elevator-per-building inspection cycles, and shift-based repair handoffs." Also serves HVAC, appliance repair, electrician, fire protection, garage door, pest control, plumbing, etc. — the elevator page is a trade configuration of one platform.
- **Three rhythms framing**: "Elevator service businesses run on three different rhythms: entrapment and shutdown emergency callbacks that demand immediate response, PM-agreement inspection cycles that must be completed across every car in a building, and multi-day modernization or major-repair projects that span shifts."
- **Per-car equipment records** (not just per-building): "each car's controller, prior callback pattern, jurisdiction inspection cycle — already on the mobile work order." "The elevator is down" is useless when the building has six cars — dispatcher and mechanic both need to know which car. Per-car records persist across ownership changes, PM contract transitions, and modernization projects.
- **Entrapment/emergency dispatch**: triage against tech location and prior callback history per car; "the right mechanic with the right parts gets to the right car fast"; cert and capacity matching on the dispatch board.
- **PM agreements + jurisdiction cycles**: PM contracts list specific tasks per car per cycle; "annual inspections, fire service tests, and category tests vary by jurisdiction"; scheduling automates PM visits, queues the right test cycle on the right car, sends customer reminders, generates documentation for AHJ submission; renewal alerts 60 days before expiration.
- **Violation/deficiency follow-up**: "Inspector violations and mechanic findings turn into risk when nobody owns the quote, approval, or corrective work." Task Boards and follow-up tasks move violations "from finding to quote, approval, scheduling, completion, and invoice — jurisdiction cure deadlines are tracked, not lost."
- **Multi-day repair/modernization**: door operator replacement, board swap, cab modernization, hydraulic-to-traction conversion — multi-day projects spanning shifts; one work order holds shift notes, photos, parts POs, time punches, follow-up tasks so the relief mechanic isn't rebuilding context from text messages.
- **Billing**: per-callback billing, NET-30 commercial, multi-year PM contracts, multi-day repair progress billing — all through QuickBooks without double entry.
- Portal: property managers submit entrapment/shutdown/door-fault reports with the specific car identified; retrieve per-car history and AHJ documentation; track PM contract status and pay invoices.

## Cross-product Comparison

| Structure / capability | FieldCamp | ElevatorPlus | LiftGrid | Smart Service | Assessment |
|---|---|---|---|---|---|
| Customer/building with conveyance units; per-car (per-unit) records | ✓ (Property → Bank → Car; controller brand, drive type, install year as first-class fields) | ✓ (per-elevator records; certificates, tests, violations on the unit record) | ✓ (buildings, shafts, elevators modeled natively) | ✓ (per-car equipment records, not just per-building; controller, manufacturer, install date, capacity, jurisdiction) | Universal — core (the unit is the atomic record) |
| Contract-driven recurring maintenance program (MSA/AMC/PM agreement per unit) | ✓ (MSA standing agreement; full-maintenance / T&I / OEM-parts / lubrication-only templates; recurring job → monthly PM + tests + recurring invoice) | ✓ (AMC management; PM & job scheduling; AMC renewal alerts) | ✓ (maintenance contracts per elevator; tiered pricing; auto-renewal; SLA timers) | ✓ (PM agreements; covered tasks per car per cycle; each visit generates its own work order; renewal alerts) | Universal — core (the revenue backbone) |
| Callback/breakdown/emergency response logged against the unit | ✓ (unified inbox auto-linked to Car record; entrapment high-priority job type; 60-min SLA framing) | ✓ (breakdown management; complaint logging; structured checklists per callback; branded report auto-issued) | ✓ (faults & work orders; response-time tracking; closure report + customer notification) | ✓ (entrapment/shutdown/door-fault triage; per-car callback history surfaces patterns) | Universal — core (the trade's signature interrupt) |
| Code-mandated periodic tests per unit, jurisdiction-driven | ✓ (Cat-1 annual / Cat-3 three-year hydraulic / Cat-5 five-year load test from one recurring job per car; QEI witness) | ✓ (Cat 1/Cat 5 scheduled, recorded, stored per unit; QEI witness-test coordination; MCP documentation on the unit record) | ✓ (periodic inspection tracking; registration/certificate/application documents bound to building/elevator) | ✓ (jurisdiction inspection cycles — Category 1, fire service test, load test — scheduled by AHJ schedule, not generic calendar) | Universal — core (the compliance signature) |
| Certificates / compliance documents per unit with expiry tracking | ✓ (Inspection Certificate custom object: number, fees, expiration) | ✓ (digital certificate storage per elevator; certificate status via QR) | ✓ (compliance & inspection hub; 90/60/30/7-day alert chain; 5-year history) | ✓ (AHJ documentation generated; per-car inspection reports retrievable) | Universal — core |
| Deficiencies/violations tracked to resolution | ✓ (open deficiencies first-class; deficiency-close rate KPI) | ✓ (violations tracked from issue through to clearance with the AHJ) | ✓ (implied via compliance hub status flow; nonconformities named in sibling product LiftexPro) | ✓ (violation cure deadlines on Task Boards; finding → quote → approval → scheduling → completion → invoice) | Universal — core |
| Deficiency/finding → quote → corrective work | ✓ (deficiency → good/better/best estimate → job) | ✓ (quote a repair, track through approvals and parts, close to signed completion) | ✓ (signed proposal → live contract; fault workflows feed invoicing) | ✓ (violations move through quote/approval/scheduling/completion/invoice) | Universal — core |
| Technician coordination: dispatch, routes, mobile offline | ✓ (AI dispatcher; route optimization; offline forms in machine rooms) | ✓ (field tracking; mobile app) | ✓ (technician mobile app; offline in shafts/machine rooms) | ✓ (dispatch board; dynamic routing; mobile app) | Universal — core |
| Certification-gated work | ✓ (NAEC CET / NAESA QEI-1 / IUEC mechanic card; controller-brand diagnostic tool as skill; hierarchical skills) | ✓ (mechanic licences/credentials tracked with expiry by state) | ✓ (roles, skills, certifications configured) | ✓ (cert and capacity matching; "right-credentialed mechanic") | Universal — common (depth varies) |
| Billing of the whole operation | ✓ (recurring MSA invoice + auto-charge; callback/repair/modernization billing; QuickBooks/Xero/Wave) | ✓ (payment management; multi-currency; invoicing) | ✓ (invoicing from work orders and contracts; e-Fatura; collections) | ✓ (per-callback, NET-30, multi-year PM, progress billing; QuickBooks-native) | Universal — core |
| Callback-rate / per-unit reliability analytics | ✓ (billable/non-billable/repeat-within-30-days split; route revenue; first-time-fix) | ✓ (MIS reporting; service analytics) | ✓ (response-time and SLA compliance analysis; per-contract P&L) | ✓ (callback frequency per car; PM completion rates; contract renewal performance) | Universal — common (elevator-flavored KPIs) |
| Modernization as a distinct motion | ✓ (callback patterns → modernization estimates; multi-day jobs; deposits) | ✓ (modernization management module; project tracking) | partial (proposals → contracts; no dedicated mod module observed) | ✓ (multi-day modernization projects; shift handoffs; quote-to-work-order continuity) | Common — the second revenue engine |
| Customer/property-manager portal | ✓ (invoices, cert PDFs, deficiencies, schedule-next-visit) | ✓ (customer portal) | ✓ (property manager portal: fault reporting, documents, invoices) | ✓ (portal: callback reports, per-car history, contract status, payments) | Universal — standard |
| Offline mobile in machine rooms/shafts | ✓ (explicit) | ✓ (mobile app; offline implied) | ✓ (explicit — basements, shafts, machine rooms) | ✓ (mobile app; offline implied) | Common — standard (the trade works where signal is bad) |
| QR/barcode unit identification | — (not observed on fetched page) | ✓ (QR on elevator → full history) | ✓ (camera-scanned documents; QR implied) | ✓ (equipment scanning named by customer) | Common |
| SLA enforcement | partial (60-min entrapment SLA as buildable dashboard) | — (not observed) | ✓ (SLA timers + breach notifications) | ✓ (response-time commitments; SLA clauses named) | Common |
| OEM IoT integration posture | ✓ (webhook inbox; explicitly no direct API) | — | — | — (not observed) | Optional; OEM platforms are complements |
| AI assistance | ✓ (AI Dispatcher, AI Receptionist, Command Center) | ✓ (AI assistant, AI & MCP) | ✓ (AI petition generator/OCR/compliance assistant — coming soon) | ✓ (The Oracle AI reporting) | Optional; era-typical |
| Operator type | independent contractors / ISPs | elevator contractors (global) | elevator service companies (EU/TR) | elevator service companies among many trades | Variant axis |

### What is actually elevator-specific (across sample)

1. **The conveyance unit as a regulated asset with its own clock** — each car is an individually tracked record carrying controller brand/drive type/install date, its own maintenance cadence, its own test cadence, its own certificate, and its own callback history. "Generic field service tools treat an elevator as a work order" vs "a regulated asset with a code-mandated test schedule" is the trade's own self-description of the difference. [Layer A ×4]
2. **The MSA (maintenance service agreement) as the contract form** — scope tiers (full-maintenance, T&I, OEM-parts, lubrication-only) determine what is covered vs billable; the contract is a live record that generates the PM visits, the test cadence, and the recurring invoice. [Layer A ×3 + Layer B ×1]
3. **The callback economy** — breakdown/emergency calls (entrapment the signature case) logged against the unit, dispatched to certification- and controller-tool-matched mechanics, with per-car callback history as the diagnostic and commercial asset (callback rate forecasts MSA cancellation; repeat callbacks become modernization quotes). [Layer A ×4]
4. **The code-mandated compliance loop** — periodic tests/inspections per unit on jurisdiction-driven cycles (ASME A17.1 Cat 1/3/5 class in North America; LOLER thorough examination in the UK; BetrSichV in Germany; IS:14665/Lift Act in India; EN 81 in Europe), certificates of operation tracked to expiry, violations tracked to cure/clearance. [Layer A ×4]
5. **Modernization as the second revenue engine** — multi-day projects spanning shifts with handoff notes, deposits, and quote-to-job continuity. [Layer A ×3]

No sampled product showed a structurally distinct object beyond this loop (no MCP-generator engine — FieldCamp explicitly does not ship one; no OEM-controller interface). The elevator-specificity is the per-unit regulated-asset structure plus the MSA/callback economy — not a different data model from field service.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

Held jointly — the elevator service management system of record:

1. **Customer buildings with conveyance units** — work happens at the customer's buildings where elevators, escalators, and related conveyances operate; each unit is an individually tracked record (identity, controller/equipment attributes, per-unit service history) nested under the building. (Remove → generic CRM/task tracking.)
2. **The contract-driven recurring maintenance program** — each unit runs under a maintenance agreement with defined scope and visit cadence; the program generates the recurring PM visits and the recurring invoice, and is the backbone of the service business. (Remove → dispatch board with no recurring backbone.)
3. **The callback loop** — breakdown and emergency calls (entrapment the signature case) are logged against the unit, dispatched to qualified mechanics, and recorded as per-unit callback history that drives diagnosis and contract decisions. (Remove → pure PM scheduling.)
4. **The code-mandated compliance loop** — periodic tests/inspections per unit on jurisdiction-driven cycles, certificates of operation tracked to expiry, violations/deficiencies tracked to resolution, findings converting into corrective quotes and work. (Remove → generic field service management; the per-unit regulated-asset compliance structure is what makes the trade recognizable.)
5. **Billing of the whole operation** — recurring contract billing plus callback/repair/modernization billing, synced to accounting at the mature pole. (Remove → a logbook with no business operation.)

Remove the elevator content (conveyance units, code-mandated test cadence, certificates, MSA scope semantics) → the generic Small Business Field Service Management Type. Remove the per-unit compliance structure but keep one-off jobs → generic FSM with an elevator landing page.

Historical check: a paper-era elevator service company (a route of buildings on cards, a maintenance contract per building, a logbook in each machine room, a callback phone log, annual test certificates posted in the cabs, typed invoices for contract maintenance and repairs) satisfies all five properties at analog level. The check passes; none of the modern machinery (typed data models, offline apps, QR codes, SLA widgets, AI dispatch, e-invoicing) is definitional.

### Level 1 — Common Mature Structure

- Per-unit service history (every visit, test, callback, part logged against the unit, timestamped, with technician attribution)
- Deficiency → quote → corrective work conversion with approval tracking
- Modernization as multi-day jobs with shift-handoff notes, deposits, and change orders
- Certification/licensing tracking of mechanics (CET, QEI, state licences, mechanic cards) with expiry awareness and dispatch gating
- Controller-brand / OEM-aware dispatch (diagnostic tool matching)
- Offline-capable mobile execution (machine rooms, shafts, basements)
- QR/barcode unit identification; camera-scanned compliance documents
- SLA timers and response-time tracking with breach alerts
- Customer / property-manager portals (fault reporting, documents, certificates, invoices, payments)
- Route optimization across building portfolios; callback-to-nearest-mechanic matching
- Per-unit and portfolio compliance dashboards (due/overdue/expired across buildings)
- Callback-rate and reliability analytics (billable/non-billable/repeat splits, first-time-fix, per-contract P&L)
- Price books, proposals with e-signature, deposits; OEM parts catalogs; van/truck inventory
- Accounting/ERP sync (QuickBooks at SMB pole; larger ERPs at commercial pole)
- Automated customer notifications (visit reminders, report delivery, renewal alerts)

### Level 2 — Variant / Optional Structure

- Product packaging: elevator pure-play vs generic FSM with an elevator vertical vs inspection-company tools vs CMMS-for-elevator vs enterprise OEM tools
- Regulatory regime: US/Canada ASME A17.1/CSA B44 (Cat 1 annual / Cat 3 three-year / Cat 5 five-year, QEI witness, MCP documentation) vs UK LOLER thorough examination (six-monthly passenger / twelve-monthly goods) vs Germany BetrSichV (Hauptprüfung/Zwischenprüfung) vs India IS:14665 + state Lift Acts vs EU EN 81
- Regional invoicing rails (e.g., TR e-Fatura/GİB; EU e-invoicing formats)
- Sub-trade breadth: escalators, moving walks, dumbwaiters, platform/wheelchair lifts, chair lifts, parking lifts, freight vs passenger
- Operator type: independent contractor/ISP vs in-house elevator teams (hospitals, universities, portfolios) vs third-party inspection companies vs facility-side compliance management (owner-side — companion, not this Type)
- OEM IoT integration posture (webhook inbox vs no integration); predictive maintenance / controller-log ingestion
- AI assistance (dispatch, reception, compliance assistants); payment automation

### Level 3 — Vendor-specific (kept out of the canonical document)

- FieldCamp: "Property → Bank → Car" naming; AI Receptionist/AI Dispatcher with confidence scores; good/better/best estimates; 30% deposit automation; explicit non-features (no MCP generator, no AHJ filing, no AIA G702/G703, no Tap-to-Pay/ACH); Capterra rating
- ElevatorPlus: 28-module map; flat pricing/no per-seat; 17 languages; 100+ access roles; immutable audit trail; QR-on-elevator; US/UK/Germany regulatory table; 200+ companies / 20+ countries claims; EECMAI membership
- LiftGrid: 12-module panel; silver/gold/platinum tiers; TR e-Fatura/GİB built-in; pre-loaded OEM parts catalogs (KONE, Otis, Schindler, ThyssenKrupp, Mitsubishi); 90/60/30/7-day alert chain; 14-day onboarding; LiftGrid Systems GmbH
- Smart Service: QuickBooks add-on architecture; six-stage job workflow; Mission Control/The Oracle branding; 60-day renewal alerts; US/CA area served

## Vendor-specific Findings

See Level 3. Notable market-structure finding (FieldCamp's own framing, corroborated by the sample's diversity): the elevator software market splits into OEM IoT operator platforms (inside the asset — complements), vertical-specialist FSMs (this Type's pure-play pole), and horizontal FSMs with elevator landing pages (the generic pole). The researched sample spans all three lanes except the OEM platforms themselves, which are complements that feed callback tickets into this Type.

## Boundary Findings

1. **vs Small Business Field Service Management / trade siblings (HVAC, plumbing, electrical, garage door, handyman, locksmith)** — the field-service spine (customer+site → job lifecycle → technician coordination → billing) is shared and verified. The durable difference: elevator carries a *structurally distinct* trade object — the per-unit regulated-asset structure (code-mandated test cadence, certificates of operation, MSA scope tiers, per-unit callback history). Like fire protection and unlike electrical/HVAC/plumbing, the trade organizes the whole product around a compliance structure generic FSM lacks. This **confirms the two-pole family structure** the fire-protection pass proposed: elevator belongs to the compliance pole. **DISCHARGES the fire-protection pass's cross-reference from this side.**
2. **vs Fire Protection Service Management (§29 sibling, processed)** — compliance-pole sibling. Same family loop (recurring code-driven inspection program + persistent deficiencies + outward compliance reporting + technician coordination + billing). Trade content differs: fire's organizing object is the protected system inspected against NFPA-class question sets with AHJ report delivery; elevator's organizing objects are the conveyance unit with its own clock, the MSA with scope tiers, and the callback economy with entrapment response. Both face AHJs; elevator's outward deliverable is the certificate of operation and test records, fire's is the inspection report. Probable keep-both as separate trade Types within the compliance pole.
3. **vs CMMS / Building Maintenance Management / EAM** — asset-ownership line: CMMS manages assets the software operator owns; here the conveyances are customer-owned and the contractor holds maintenance/test history *about* them. The owner-side mirror (facility teams managing vendor contracts, SLAs, certificates — OxMaint/ATIS class) is a different operator with different objects; recorded as companion, not this Type.
4. **vs OEM IoT operator platforms (KONE 24/7 Connected, Otis ONE, Schindler Ahead, TK MAX)** — they live inside the asset, operated by OEMs; their fault alerts become callback tickets in this Type's systems. Complements, not this Type.
5. **vs Construction Project Management** — modernization and new installation are project work (multi-day jobs, progress billing); commercial-pole products bundle project machinery, but the maintenance/callback/compliance loop remains this Type's center.
6. **vs Property Maintenance Management** — property managers and REITs are customers/channels here, not operators; the subject of record is the contractor's book of conveyances, not the property portfolio.
7. **vs Appointment Scheduling Application** — scheduling is one fragment; this Type is the whole business operation.
8. **vs Third-party inspection vendors (ATIS class)** — inspection-only contractors are a variant operator of adjacent machinery; their owner-facing compliance software (ATIS Alert) is a companion, not this Type.

## Uncertainties

1. **Enterprise/OEM pole not directly researched** — Otis/KONE/Schindler/TK enterprise tools (ALMA class) and LiftKeeper/FIELDBOSS were not fetched; the vertical-specialist lane is represented only via FieldCamp's competitive framing. Assertions calibrated to the four researched products.
2. **No Tier-1 help-center docs fetched** — all four products evidenced via official product/industry pages with operational FAQs (rich but marketing-adjacent). FieldCamp links to product docs (docs.fieldcamp.ai) which were not separately fetched.
3. **Exact test frequencies** — products reference "annual Cat-1 / five-year Cat-5" and jurisdiction variation generically; ElevatorPlus's US page does tabulate US/UK/Germany regimes (recorded above as vendor-published reference), but no primary regulatory text was consulted; precise jurisdictional requirements are not asserted in the canonical document beyond the vendor-published pattern.
4. **MCP (Maintenance Control Program) software objects** — ElevatorPlus claims MCP documentation "lives on the unit record"; FieldCamp explicitly does *not* ship an MCP generator (the completed-form history is the audit trail). Whether any product generates A17.1 §8.6.1 MCP documents as structured objects was not verified; not claimed.
5. **Callback billing mechanics** (callback caps per contract, excess-billing thresholds, service credits) — named in the trade's contract vocabulary (and by owner-side sources) but not documented as software objects in the fetched sample; kept as standard capability without specifics.
6. **Escalator/sub-trade depth** — escalators appear in positioning (FieldCamp, ElevatorPlus segments) but no fetched source documents escalator-specific objects (step-chain, skirt clearance) as software structure; sub-trade handling held as variant, not claimed.
7. **Regional markets beyond US/EU/TR/IN** — Gulf/ANZ/SE Asia pages exist (ElevatorPlus) but were not fetched; canonical document avoids region-specific claims beyond the regimes observed.

## Final Synthesis

Elevator Service Management is the business-management system of an elevator/escalator service contractor. Its defining core is the field-service spine (customer buildings → jobs carried through a lifecycle by coordinated, certification-gated mechanics → billing) bound together with the trade's signature structure: the conveyance unit as a regulated asset with its own clock — a contract-driven recurring maintenance program (MSA with scope tiers) generating PM visits and recurring invoices per unit; a callback loop logging breakdown and entrapment emergencies against the unit with per-car callback history; and a code-mandated compliance loop of periodic tests on jurisdiction-driven cycles, certificates of operation tracked to expiry, and violations/deficiencies tracked to resolution and converted into corrective work. Modernization runs as the second revenue engine on multi-day jobs. Everything else commonly associated with these products (typed data models, offline mobile, QR identification, SLA timers, portals, route optimization, certification tracking, OEM parts catalogs, AI, IoT feeds) is standard or optional capability layered on this structure. The leaf confirms the §29 trade-family two-pole structure: elevator sits in the compliance pole beside fire protection — a genuinely structural trade object, not content tuning — and this pass discharges the fire-protection pass's cross-reference accordingly.
