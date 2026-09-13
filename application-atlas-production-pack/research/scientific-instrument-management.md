# Research Notes — Scientific Instrument Management

## Research Goal

Understand, from real products, what the Application Type "Scientific Instrument Management" (§23 Education, Research & Knowledge Institutions) actually is: what objects exist inside it, whether its center is the instrument asset lifecycle, the scheduling of shared instrument time, or both; who uses it; how work flows; and where its boundaries hold against the dense neighboring cluster (Research Core Facility Management, Resource Calendar, LIMS/Research LIMS, Calibration Management, CMMS/EAM/Enterprise Asset Registry, Equipment Administration Platform).

This leaf inherits three forward flags from processed siblings:

1. **research-lims (§23, 2026-09-09)**: "equipment management is a module inside research LIMS, not identity" — module/neighbor boundary, to be discharged from this side.
2. **research-core-facility-management (§23, 2026-09-09)**: keep-both ratified with the seam "remove scheduling/billing/users and keep asset lifecycle → Scientific Instrument Management / CMMS territory" — that pass characterized this leaf as asset-lifecycle-centric.
3. **calibration-management (§16, 2026-09-07)**: "that Type is booking/scheduling of shared research instruments; calibration management is the fitness/traceability record" — that pass characterized this leaf as booking/scheduling-centric.

The two sibling characterizations differ (asset lifecycle vs booking/scheduling). A goal of this pass is to resolve the actual center from product evidence.

## Initial Boundary (hypothesis before research)

- Hypothesis: software that manages scientific instruments (microscopes, sequencers, spectrometers, cytometers, centrifuges) as shared resources in lab/facility contexts: an instrument register + booking/scheduling of instrument time + maintenance/calibration/fitness records + usage/qualification records; possibly utilization reporting and cost recovery.
- Likely nearest neighbors: Research Core Facility Management (recharge economics), Resource Calendar (generic booking), LIMS/Research LIMS (equipment as module), Calibration Management (metrology depth), CMMS/EAM (generic equipment maintenance), Enterprise Asset Registry / Equipment Administration Platform (generic asset administration).
- Known unknowns: is booking definitional or only common? Is usage capture definitional? Is billing in or out? Does the type hold outside universities (biotech, analytical/QC labs)?

## Research Questions

1. What record structure does an instrument carry (identity, units, location, status, responsible party, documents)?
2. Is shared-use scheduling/booking definitional, common, or optional? What booking mechanics exist (conflict detection, waitlists, approvals, calendar sync)?
3. What fitness/service semantics exist (maintenance, repair, calibration, down state) and how do they interact with availability/booking?
4. How are users identified, qualified, and gated (training, permissions, hardware access)?
5. Is actual-usage capture part of the core or a variant? What does it feed (utilization, billing)?
6. Where exactly is the seam with Research Core Facility Management (economics), LIMS (samples), Calibration Management (metrology), CMMS/EAM (generic maintenance), Resource Calendar (generic booking)?
7. What is variant rather than definitional (billing, external portals, loans, instrument data capture, IoT/telemetry, AI)?

## Representative Products

Selected for market representation, documentation completeness, product-philosophy difference, and customer-tier spread:

| Product | Posture | Why sampled |
|---|---|---|
| **BookitLab** (Prog4biz, since 2007) | Dedicated lab/instrument operations platform; sells "Lab Equipment Scheduling" and "Enterprise Asset Management" as distinct product lines | The purest dedicated instrument-management family; deep official product documentation; academic + pharma + analytical-lab customers |
| **Genemod** | Modern cloud research platform; "Equipment" is a first-class product pillar beside inventory/ELN | Startup-generation pole; equipment + core-facility management explicitly packaged; rich feature/FAQ documentation |
| **SciSure** (eLabNext + SciShield merger) | Scientific Management Platform (ELN + LIMS + EHS); equipment management is a capability inside the LIMS pillar | The suite-module pole; confirms the "equipment management as module" observation made by the research-lims pass |
| **Calpendo** (Exprodo Software, since 2008) | Calendar-first scheduling/facility management system heavily used by university imaging/MRI facilities | The scheduler-first pole and boundary zone toward Research Core Facility Management; calendar spine with booking rules, training automation, usage recorder add-on |

Considered but not sampled: Agilent iLab Operations Software (institutional core-facility-weighted; already sampled by the sibling pass for that type), Stratocore PPMS (same posture), Quartzy (inventory-first, no booking spine), NEMO (previously unreachable for the sibling pass).

## Sources

Fetched 2026-09-09 (all Layer A unless noted):

- BookitLab — root: https://www.bookitlab.com/
- BookitLab — Lab Equipment Scheduling: https://www.bookitlab.com/solution/lab-equipment-scheduling
- BookitLab — Enterprise Asset Management: https://www.bookitlab.com/solution/enterprise-asset-management
- Genemod — Equipment: https://www.genemod.com/products/equipments
- SciSure — LIMS: https://www.scisure.com/lims (help center at https://support.elabnext.com/hc/en-us referenced but not fetched)
- Calpendo/Exprodo — root: https://www.exprodo.com/

Note: the eLabNext brand has merged into SciSure (Scientific Management Platform, 2025); observations for that posture come from the SciSure LIMS page (official vendor surface of the merged entity).

## Product Observations

### BookitLab (Layer A — directly observed)

**Positioning.** "The Flexible Platform for Research Labs... manage scheduling, equipment, services, and access in one configurable platform." Modular: Core Facility Management / Lab Equipment Scheduling / Request Management-LIMS / Enterprise Asset Management as separately named product lines. Serves universities, biopharma, analytical testing and manufacturing/quality labs since 2007; "100k+ instruments, services and assets are managed".

**Instrument/asset register.** "Centralized Asset Database — a single source of truth for every asset type with customizable metadata... Instruments & equipment, Rooms & facilities, Cleanrooms, Loanable assets, Consumables & kits." "Asset Lifecycle Tracking — monitor asset performance from acquisition to retirement." QR/barcode scanning supports "maintenance, loaning, repair, and service workflows."

**Scheduling.** "Dynamic Scheduling — schedule instruments, rooms, services, staff, and any other bookable resource in one system built for scientific core operations." Real-time availability on a visual calendar/timeline; "Automated conflict detection prevents double bookings"; customizable reservation forms; booking/billing rules; approval workflows; waitlists with auto-offer of next slot; bulk booking; two-way Google/Outlook calendar sync and iCal feeds; mobile booking and kiosk check-in; outside-organization public portal ("external users view a curated catalog, self-book permitted resources... Policies, quotas, and required training are enforced before access").

**Access & training gating.** "Usage & Access Control — enforce training requirements, monitor real-time usage, control equipment access via card readers or locks, and maintain complete compliance logs." "Tie access permissions to roles and training status... enforce access through software rules and hardware locks... support kiosk, assisted, and supervised usage models... track real-time usage for monitoring and billing." "Enforce training/qualification gates, kiosk check-ins and badge validation before equipment starts; capture telemetry and operator logs linked to asset records."

**Fitness & service.** "Full Asset Management Lifecycle — track each asset from purchase through retirement — schedule PMs, log repairs, attach calibration certificates and preserve an immutable activity trail." Work orders ("create and track work orders for equipment maintenance & scheduled checks"); maintenance scheduling; calibration records & certificates; SLA management; service requests "tied to asset records... auto-triage, reserve parts, create work orders." Linked assets & dependencies (instruments ↔ consumables, subcomponents, spares; dependency trees; cascading maintenance propagation).

**Asset-aware scheduling (the join).** "BookitLab connects scheduling with live asset status so maintenance events, repairs, and calibration windows directly shape resource availability. When a resource cannot be used, the platform can block the booking, guide users to equivalent assets, or suggest alternative times automatically."

**Usage & economics.** Billing module ("generate invoices based on equipment usage, service requests, and custom billing rules; chargebacks, rate structures"); reporting across "utilization, reservations, and availability... revenue, chargebacks, and billing activity... performance, downtime, and service demand." Add-ons: sample management, interactive floorplans, loan desk (custody tracking), publications ("link instruments, projects, and usage records to publications, with DOI capture").

**Customer voice.** Bar-Ilan Scientific Equipment Center director: "monitor and control booking, usage and billing of the many devices"; East Carolina: "schedule equipment and manage user fees"; Stanford: "various access control and training configurations."

### Genemod (Layer A — directly observed)

**Positioning.** "Equipment & core facility management — Track instruments and individual units, schedule across your facility, gate booking by training status, and stay ahead of maintenance — all in one workspace." Page title: "Lab Equipment Management & Scheduling Software".

**Instrument catalog.** "Register an instrument once and track every unit underneath it — location, model, and booking rules on the card. Instruments with multiple units, models, and locations. Domain tags — Immunology, PCR, Imaging, QC, GMP. Booking-required flags surfaced right on the card." FAQ: "Microcentrifuge 1 through 10 can live under one instrument and be scheduled independently."

**Scheduling.** "See every instrument and unit on one grid, drop in a reservation, and never double-book again. Day and week views, grouped by instrument and unit. Timezone-aware reservations across sites. Conflict detection before a booking is confirmed." Personal "My reservation" view; upcoming reservation reminders.

**Training-gated booking.** "Restrict reservations to trained, authorized users. Permissions follow each instrument's access policy." FAQ: "Flag an instrument as booking-required and assign it an access policy. Only members marked as trained and authorized can reserve it; everyone else sees the instrument but can't book until they're cleared."

**Maintenance & fitness.** "Log service dates, schedule preventive maintenance, and flag units as down before someone books them."

**Usage & data.** "Usage analytics — see utilization by instrument, room, and team — and right-size shared capacity with real numbers." "Instrument data integration — capture run outputs and link instrument data straight to the right sample and notebook entry."

**Audience.** Core facilities; shared instrumentation labs ("coordinate cytometers, microscopes, and analyzers across multiple research groups"); academic departments ("give students and postdocs self-service booking — gated by training and supervisor approval"); biotech R&D.

### SciSure / eLabNext (Layer A — directly observed, module depth)

**Positioning.** Scientific Management Platform (SMP) = ELN + LIMS + EHS. The LIMS page: "SciSure's LIMS gives lab teams a structured way to manage samples, inventory, equipment, and workflows in one system."

**Equipment capability.** Feature list: "Equipment management — track lab equipment, schedule calibrations, and manage bookings in one system." Section: "Track equipment and set up automations — ensure smooth lab operations with equipment tracking, maintenance scheduling, and compliance-ready logs."

**FAQ (operational detail).** "How are lab equipment and devices tracked? Equipment and devices are registered within the system and can be scheduled, booked, and tracked. Maintenance, calibration, and validation events can be planned in advance with automated notifications."

**Context.** Equipment sits in the same data model as samples, storage units, inventory, experiments; the platform's center is samples/workflows/compliance, not instruments. No utilization/billing or hardware access control observed on the fetched surface (Layer A silence; treated as not-observed, not absent).

### Calpendo (Layer A — directly observed, boundary pole)

**Positioning.** "Calpendo is an industry-leading facility management software for a wide range of industries. Since 2008... streamlining their booking and resource management of instruments, staff, 3d printers, meeting rooms and much more." Customer base dominated by university imaging/MRI/neuroimaging facilities (UC Berkeley MRI, Oxford, Cambridge, UCL, NIH, etc.).

**Calendar spine.** "Calpendo is built around an intuitive Calendar interface to view and manage your bookings across multiple resources" (day/week/month views, bookings by status including cancelled). "Powerful Rules — ensure your users book resources in the right way using simple-to-apply rules governing booking duration, frequency, timing and more."

**Workflow automations.** "Notify users of important changes to bookings. Automate training records and renewals. Calculate booking costs for your bookings based on the parameters specific to your context."

**Usage recorder.** Calpendo Activity Recorder (CAR): "track the actual usage of any instrument that is connected to a PC. Use CAR to understand who is using your instruments and for how long."

**Buyer voice.** UCL UC San Diego: "We were in the market for an integrated software solution that provides web scheduling, project/user management and billing capabilities." Reports: "bespoke reports... custom and scheduled reports."

**Note.** Calpendo self-labels "facility management"; the sibling pass classified it as a core-facility management product. In this leaf it serves as evidence for the booking/rules/training/usage-recording spine at instrument facilities and as a boundary marker: its buyer checklist includes billing, pulling it toward the core-facility type.

## Cross-product Comparison

| Structure | BookitLab | Genemod | SciSure (eLabNext) | Calpendo | Layer |
|---|---|---|---|---|---|
| Instrument register (identity: model/units/serial, location, status) | ✓ (asset database, lifecycle, QR/barcode) | ✓ (instrument + per-unit catalog) | ✓ ("registered within the system") | ✓ (resources incl. instruments) | A×4 |
| Booking/reservations on instrument schedule | ✓ (calendar/timeline, waitlist, bulk) | ✓ (grid by instrument/unit) | ✓ ("scheduled, booked") | ✓ (calendar spine) | A×4 |
| Conflict prevention / double-booking prevention | ✓ (automated conflict detection) | ✓ (conflict detection before confirm) | not observed | ✓ (booking rules) | A×3 |
| Training/qualification gating of booking | ✓ (training status ↔ permissions; hardware enforcement) | ✓ (training-gated access policy) | not observed | ~ (training records/renewals automated; gating via rules) | A×2 + B |
| Maintenance/repair records & work orders | ✓ (PMs, work orders, incidents, SLA) | ✓ (service dates, PM) | ✓ (maintenance scheduling + notifications) | not observed | A×3 |
| Calibration records on instrument | ✓ (calibration certificates attached) | ~ (calibration via maintenance vocabulary, not explicit) | ✓ ("schedule calibrations") | not observed | A×2 + B |
| Fitness state gates availability | ✓ (asset-aware scheduling blocks booking when down) | ✓ ("flag units as down before someone books") | ~ (planned events + notifications) | not observed | A×2 |
| Actual usage capture (kiosk/recorder/telemetry) | ✓ (kiosk, badge, telemetry, operator logs) | ~ (usage analytics; data integration) | not observed | ✓ (CAR add-on) | A×2 + B |
| Utilization/utilization reporting | ✓ | ✓ (by instrument/room/team) | not observed | ✓ (bespoke reports) | B (4/4 at some reporting level) |
| Billing / cost recovery | ✓ (module) | not observed | not observed | ✓ (booking costs) | A×2 → variant |
| External/inter-organization portal | ✓ (public asset directory) | not observed | not observed | not observed | A×1 → optional |
| Instrument-data capture linked to samples/notebook | ~ (via LIMS syncs, marketplace) | ✓ (run outputs → sample + notebook entry) | ✓ (instruments linked to samples/experiments) | not observed | A×2 → adjacent/optional |
| Linked consumables/inventory | ✓ (inventory-related reservations, spares) | ✓ (same workspace as inventory) | ✓ (same system as inventory) | not observed | A×3 |
| Loans / custody | ✓ (loan desk module) | not observed | not observed | not observed | A×1 → optional |

Evidence layers: A = directly observed on that product's official surface; B = cross-product commonality. "not observed" = not on fetched surface; no absence claim is made.

## Abstraction Hierarchy

### L0 — Defining Invariant (the smallest stable structure)

Three jointly-held structures around the scientific instrument as a shared resource:

1. **The instrument register of record.** Persistent, individually identified records for the lab's/facility's scientific instruments — identity (name/type, make/model, serial-numbered physical units), location, operating status, responsible party. All four sampled products hold such a register (A×4). Remove it → an anonymous booking board or a generic calendar; the "scientific instrument" as a managed entity disappears.
2. **Shared-use time allocation on the instrument's schedule.** Instruments are shared by a population of users; the system allocates instrument time through reservations on a per-instrument calendar with conflict prevention (no double-booking). Observed in all four (A×4). Remove it → an asset register with maintenance records only; that is CMMS / Equipment Administration territory, and the "shared" dimension that motivates the software disappears.
3. **Fitness & service records on the instrument.** Maintenance, repair, and calibration events attached to the instrument record, maintaining an operating/fitness state (in service / down / under maintenance) that shapes availability. Directly observed in three (A×3; the fourth is a booking-first pole where service tracking is not on the fetched surface). Remove it → a bare booking site for possibly-broken instruments — Resource Calendar territory.

Jointly-held load-bearing:

- 1 alone = asset register / asset spreadsheet (Enterprise Asset Registry pole)
- 2 without 1 = generic room/vehicle booking (Resource Calendar)
- 3 without 1+2 = maintenance logbook (CMMS)
- 1+2 without 3 = booking site that cannot see broken instruments
- 1+3 without 2 = instrument CMMS/EAM (BookitLab's own "Enterprise Asset Management" module is exactly this ring — as a module, not the type's identity)
- 2+3 without 1 = anonymous calendar + logbook

§24 historical check: paper-era lab — an equipment register card (identity), a sign-up sheet on the instrument (booking), and a maintenance logbook (service records) satisfy all three legs with no software. Early 2000s homegrown university schedulers = register + booking, still in-type. A single lab sharing three PCR machines among its members still fits (shared = across users, not necessarily across labs). Non-research contexts (BookitLab serves analytical/QC labs) still fit — the invariant is the instrument-as-shared-resource, not the university. ✓ The L0 survives.

### L1 — Common Mature Structure (very common, not definitional)

- Training/qualification gating: restrict reservations (and often physical access) to trained, authorized users (BookitLab, Genemod direct; Calpendo automates training records; SciSure not observed). The gate is the common implementation of access policy over the L0 reservation.
- Actual-usage capture: kiosk check-in, workstation recorder, badge/interlock, telemetry; reconciles reservation vs real use (BookitLab, Calpendo CAR, Genemod usage analytics + data capture).
- Utilization & operational reporting (by instrument, room, team; downtime; demand).
- Service requests from users triaged into work orders tied to asset records.
- Linked consumables/inventory (booking can auto-reserve reagents/kits; spares linked to work orders).
- Calendar interoperability (two-way sync, iCal feeds).
- Waitlists, cancellation policies, booking rules (duration, frequency, timing).
- Multi-device surfaces: web, mobile, kiosk.

### L2 — Variant / Optional Structure (segment, scale, economics, posture)

- Billing/cost recovery (chargebacks, rate structures, funding-source attribution) — present in the dedicated platform and the imaging-facility scheduler, absent/optional elsewhere; this is the Research Core Facility Management seam, not part of this type's identity.
- External/inter-organization portals (curated public catalogs, external self-booking with quotas/policies).
- Hardware access enforcement (card readers, interlocks, kiosks) vs software-only.
- Loans/custody (loanable equipment desks).
- Instrument-data capture: run outputs linked to samples/notebook entries (adjacent to LIMS/ELN/SDMS territory).
- Publications linkage, facility floorplans, multi-language UI.
- Suite packaging: dedicated product vs equipment module inside ELN/LIMS/EHS platforms.
- Multi-site/multi-facility roll-ups; AI assistants (era-current).

### L3 — Vendor-specific Structure (Research Notes only)

- BookitLab: module packaging names ("Lab Equipment Scheduling", "Enterprise Asset Management", "Request Management/LIMS"); "assemblies" and "modes" in reservation configuration; Lite edition; Lite ELN; animal-facility module; Prog4biz company; 2007 lineage.
- Genemod: instrument+unit catalog model ("Microcentrifuge 1 through 10 under one instrument"); domain tags (Immunology, PCR, Imaging, QC, GMP); "booking-required" flag; "Agentic Lab OS" AI positioning; "Equipment & core facility management" tagline.
- SciSure: SMP framing (ELN+LIMS+EHS merger of eLabNext and SciShield); storage-unit management (freezers/LN2) as inventory-side sibling; Supplies module; marketplace add-ons.
- Calpendo: CAR (Activity Recorder) product; Starter/Premium/Enterprise licence tiers; low-code workflow engine; "facility management" self-label; imaging-facility customer concentration.

## Rejected Findings

- **"Billing is definitional" — rejected.** Billing appears strongly in 2/4 sampled products and is the load-bearing center of the sibling type (Research Core Facility Management: rate-bearing catalog + usage-to-recharge loop). Its presence here marks the boundary zone, not the invariant. A single lab managing shared instruments with no charging still fully fits this type.
- **"Training gating is definitional" — rejected as invariant, kept as L1.** Strongly observed (BookitLab, Genemod), but the paper-era and lightweight lab satisfy the type without a formal qualification system; the invariant is that reservations are made by identified users against the instrument's schedule.
- **"Usage capture is definitional" — rejected as invariant, kept as L1.** Booking-based management without actual-usage capture still fits (Calpendo base without CAR; Genemod analytics is a feature, not the spine).
- **"This is just CMMS for labs" — rejected.** The shared-use allocation semantics (booking by identified users, qualification, utilization) are absent from generic CMMS/EAM and are what the market's own naming puts first ("Lab Equipment Scheduling", "instrument scheduling", "equipment management & scheduling").
- **"Instrument data acquisition/control is part of the type" — rejected.** Instrument control and run-data belong to instrument firmware / CDS / LIMS/SDMS territory; here the instrument is an allocation and fitness object. Data-capture linkage appears as an optional adjacent capability only.

## Boundary Findings

**vs Research Core Facility Management (§23, processed).** The sibling's center is the facility's service operation to a researcher population: a rate-bearing instrument/service catalog, per-user/per-group attribution with funding sources, and a usage-to-recharge economic loop. This type's center is the instrument itself as a managed shared asset: register + time allocation + fitness. Booking exists in both; the load-bearing seam is the economics (and the facility-user funding machinery). Test: keep the instrument register/booking/fitness and remove rates/funds/recharge → this type; add the rate-bearing storefront and recharge loop → core facility. Direct market evidence for the split: BookitLab itself sells "Core Facility Management" and "Lab Equipment Scheduling" as separate product lines (vendor's own taxonomy separates the two). Calpendo is the boundary zone: calendar-spined like this type, but its buyers' checklist includes billing/users/projects, which is why the sibling pass classified it as core-facility software. **Flag from research-core-facility-management discharged from this side:** their "keep asset lifecycle → Scientific Instrument Management / CMMS" characterization holds, with the refinement that the lifecycle ring alone is the CMMS pole — the distinctive joint structure of this type is shared-time allocation + fitness records on an identified instrument register.

**vs Research LIMS (§23, processed) / LIMS (§22, processed).** LIMS is sample-centric (samples, assays, runs, chain of custody). This type is instrument-centric. Equipment management appears as a module inside LIMS platforms (SciSure: equipment registered, booked, maintained inside the LIMS pillar) — module, not identity. **Flag from research-lims discharged from this side:** confirmed — an equipment module inside a research LIMS lacks the type's center (scheduling as the operating spine, fitness-gated availability, utilization as a first-class concern); when a platform ships equipment management deep enough (booking + maintenance + utilization + access), it is crossing into this type, and the market sells dedicated products for exactly that.

**vs Calibration Management (§16, processed).** Calibration management's center is measurement fitness: procedures with tolerances, as-found/as-left results, uncertainty, reference standards with their own due states, traceability, certificates as the deliverable. Here calibration is one service/record among maintenance events attached to the instrument, feeding availability (BookitLab attaches calibration certificates; SciSure schedules calibration events with notifications; neither documents metrology machinery). Test: remove booking/shared-use and deepen metrology semantics → calibration management; the same physical instrument can live in both systems with different semantics. **Flag from calibration-management discharged from this side:** their characterization ("booking/scheduling of shared research instruments") names the scheduling leg; this pass adds that the register + fitness legs are equally load-bearing — the type is not a bare scheduler.

**vs CMMS / EAM / Enterprise Asset Registry / Equipment Administration Platform (§10/§16).** Those types center on the asset lifecycle of equipment in general (holdings, maintenance, work orders, depreciation). This type holds the same ring (all dedicated products have it) but its distinguishing joint structure is shared-use allocation by a user population (reservations, qualification, utilization) on scientific instruments. Test: remove the shared-use/booking semantics → CMMS/EAM/Equipment Administration. BookitLab naming its asset ring "Enterprise Asset Management" (as one module of a lab platform) is consistent: the ring is a component here, not the identity.

**vs Resource Calendar (§3.08).** A resource calendar books rooms/equipment on calendars but carries no instrument semantics: no units/serial identity model, no fitness state gating availability, no qualification gating, no utilization-of-instrument reporting. Test: remove instrument identity + fitness + qualification semantics → resource calendar.

**vs Instrument control / data systems (Chromatography Data System, instrument firmware, SDMS).** There the instrument is an operating/data surface (runs, acquisitions, result files). Here the instrument is an allocation/fitness object. Overlap is at data-capture integration (optional capability, e.g., linking run outputs to samples), not identity.

**"Remove what to become another type" summary:**

- remove the register and instrument semantics → Resource Calendar
- remove shared-use scheduling/booking → CMMS / EAM / Equipment Administration territory
- remove the fitness/service ring → bare booking site (Resource Calendar pole)
- add the rate-bearing catalog + funding-source recharge loop → Research Core Facility Management
- center on samples/assays and demote equipment to a module → LIMS / Research LIMS
- deepen calibration into metrology semantics (tolerances, standards, traceability, certificates) → Calibration Management
- center on the instrument's run data/control → CDS / instrument software / SDMS territory

## Uncertainties

1. **SciSure equipment depth.** Only the LIMS marketing/FAQ page was fetched; the help center (deeper operational documentation of booking rules, qualifications, utilization) was not. Claims about SciSure are limited to what that page shows (register, booking, maintenance/calibration scheduling with notifications); no claim is made about access control or billing there.
2. **Calpendo service-tracking depth.** No maintenance/calibration records were observed on Calpendo's fetched surfaces; it may exist in Premium configurations. Calpendo is therefore used as the scheduling-leg pole and boundary marker, not as evidence about the fitness leg.
3. **Genemod billing.** Not observed on the equipment page; no claim is made. (The platform serves core-facility-posture labs, so economics may exist elsewhere.)
4. **Agilent iLab / PPMS not re-sampled.** The institutional core-facility posture is already covered by the sibling pass; no claim in this document depends on them.
5. **Market-share / ubiquity claims** are not made; customer-logo walls and counts (e.g., "100k+ instruments") are vendor statements, recorded as such, not verified.
6. **Exact limits** (booking rule counts, notice windows, licence-tier feature counts) are vendor-specific and stay in these notes only.

## Final Synthesis

Scientific Instrument Management is the shared-instrument management system of research and laboratory operations. Its defining core is three jointly-held structures:

1. the **instrument register of record** — identified scientific instruments (make/model, serial-numbered units, location, status, responsible party) held as persistent records;
2. **shared-use time allocation** — reservations by identified users on each instrument's schedule, with conflict prevention; access commonly gated by training/qualification;
3. **fitness & service records on the instrument** — maintenance, repair, and calibration events that maintain an operating state which shapes availability and booking.

Around this core, mature products add a standard ring: qualification management, actual-usage capture, utilization and downtime reporting, service-request workflows, linked inventory/consumables, calendar interoperability, and multi-device surfaces. Billing/recharge, external portals, hardware interlocks, loans, publications linkage, and instrument-data capture are variant or optional — billing in particular is the seam with Research Core Facility Management, and sample linkage is the seam with LIMS.

The market realizes the type in three postures: dedicated instrument-operations platforms (scheduling + asset ring + access), equipment modules inside research platforms (ELN/LIMS/EHS suites), and calendar-first facility schedulers used by instrument facilities. The type is not university-specific (analytical/QC and biotech labs fit), not software-era-specific (paper-era labs satisfy the core), and not economics-dependent (charging is configuration, not structure).
