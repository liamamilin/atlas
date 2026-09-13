# Research Notes — Operating Room Management

## Research Goal

Understand what an Operating Room Management system (also "operating theatre management" in UK/EU vocabulary) actually is as an Application Type: its defining structure, its scheduling and day-of-execution workflow, its interfaces, its rules, and its boundaries against neighboring Types — Anesthesia Information Management System (AIMS, flagged for joint review), Patient Scheduling, Hospital Management System (OT scheduling slice), Bed & Capacity Management / Patient Flow, EDIS, and the emerging OR analytics/optimization overlay category.

## Initial Boundary

Initial hypothesis (pre-research):

- OR management is the surgical/perioperative department's operational system: it schedules surgical cases into rooms and time slots, manages block time, tracks the day-of-case flow (patient phases, staff, delays), manages turnover, and reports utilization/throughput.
- Its differentiator vs the AIMS sibling: the OR (room + session time) as the managed resource vs the patient's anesthetic care record. The two are bundled in purchase (perioperative suites) but shipped as sibling products.
- Nearest neighbors: AIMS (flagged), Patient Scheduling, HMS OT-scheduling, Bed & Capacity Management (same operational pattern, different resource), OR analytics overlays (LeanTaaS/Qventus class).
- Main unknowns: whether day-of tracking is defining or a sibling module (Picis ships SmarTrack separately; SIS includes it as a pillar); whether block scheduling is defining or common; how deep supplies/preference cards go; how analytics overlays relate to the Type; whether a measurement leg belongs in L0.

## Research Questions

1. What is the unit of record — the surgical case, the room session, the block?
2. How does the scheduling workflow run: request → booking → room/time assignment → day-of adjustment?
3. How is OR capacity allocated (master surgery schedule, block time, release/recapture rules)?
4. What day-of-case operational state is tracked, and on what surface (the OR board)?
5. How are turnover and case timing measured and managed?
6. How do supplies/instruments/preference cards/implants attach to the case?
7. What analytics exist (utilization, block utilization, on-time starts, cancellations, deferrals, cost per case)?
8. What packaging variants exist (standalone / perioperative-suite module / EHR module / analytics overlay)?
9. Joint review: does the AIMS-pass boundary hold from this side?
10. Historical check: does the paper-era OR (booking book + block board + whiteboard + tally sheets) satisfy the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer tiers, and geographic spread:

| Product | Vendor | Philosophy | Evidence tier reached |
|---|---|---|---|
| OR Manager (+ Perioperative Suite) | Picis Clinical Solutions (US, part of Harris Computer) | perioperative-suite sibling product; scheduling + documentation + supply + revenue | Tier 2 (product page + FAQ + suite page + FAQ) |
| SIS Surgery (+ SIS Complete ASC pole) | Surgical Information Systems (US) | standalone surgical department system; scheduling/documentation/tracking as three named pillars; separate ASC product family | Tier 2 (product pages + homepage) |
| Qventus Surgical Growth | Qventus (US) | AI/automation overlay on OR capacity — no system-of-record claims; explicitly EHR-integrated | Tier 2 (solution page + vendor blog by clinician-author) |
| Epic OpTime / Oracle Health surgical modules | Epic / Oracle Health (US) | EHR-embedded perioperative modules | market anchor only — no public docs; no product claims made |
| (reference) University Hospital Augsburg OR management practice | — | real operating-theater management process, documented in a peer-reviewed study | Tier 3 (open-access BMC Health Services Research study) |

Rejected/abandoned samples (per network rule — failed once or twice, not retried):

- Getinge Tegris (device-vendor perioperative software) — direct URL guess 404; Bing search unusable (region-filtered, site: operator ignored); abandoned; no claims made.
- LeanTaaS iQueue for ORs — request timed out; the same domain 404'd once in a prior pass; abandoned; no claims made.
- GE Centricity Perioperative, MEDITECH Expanse Perioperative — not attempted (prior passes found MEDITECH pages generic; GE product line status unclear); no claims made.

## Sources

- Picis — OR Manager product page + FAQ: https://picis.com/solution/or-manager/ (fetched 2026-09-08; product now navigates from https://picis.com/solution/perioperative-suite/or-manager/)
- Picis — Perioperative Suite page + FAQ: https://picis.com/solution/perioperative-suite/ (fetched 2026-09-08)
- Surgical Information Systems — SIS Surgery product page: https://www.sisfirst.com/sis-surgery (fetched 2026-09-08)
- Surgical Information Systems — homepage: https://www.sisfirst.com/ (fetched 2026-09-08)
- Qventus — Surgical Growth (OR utilization) solution page: https://qventus.com/solutions/operating-room-utilization/ (fetched 2026-09-08)
- Qventus — "3 Ways Machine Learning can Optimize your Operating Room Utilization" (vendor blog, author David Atashroo, MD, 2023-11-28): https://qventus.com/resources/blog/3-ways-machine-learning-can-optimize-your-operating-room-utilization (fetched 2026-09-08)
- Schoenfelder J, Kohl S, Glaser M, McRae S, Brunner JO, Koperna T. "Simulation-based evaluation of operating room management policies." BMC Health Serv Res 2021;21:271. PMC7992985 (fetched 2026-09-08) — documents real OR management practice at University Hospital Augsburg: master surgery schedule, OR-coordinator role, disruption management, acuity categories, timestamped case process, KPIs.
- Search result pages: Bing (2 queries, region-degraded, no usable hits), NCBI/PMC search (used to locate the study).

### Source-access Limitations

- No Tier-1 help center / user manual / training documentation was reachable for any sampled product. Evidence base is Tier-2 official product/solution pages (operationally descriptive but marketing-adjacent), one vendor blog, and one peer-reviewed study.
- Epic and Oracle Health documentation gated/unreachable (consistent with prior passes); no product claims made about them.
- Consequence: no precise operational facts are asserted anywhere in the final document — no exact auto-release windows, no exact utilization formulas, no exact state names, no numeric thresholds. Vendor-claimed numbers (Qventus "reduce cancellations by up to 40%", "+3 strategic cases per OR per month", "CLAT improved case length estimation by 30%", Picis suite claims) are recorded here as vendor claims and excluded from the final document except where attributed.

## Product A — Picis OR Manager (+ Perioperative Suite)

### Key observations (Evidence layer A unless noted)

- OR Manager product page title: "Operating Room & Surgical Scheduling Software"; described as "a comprehensive operating room management software that automates each step of the perioperative process, including scheduling, intraoperative documentation, supply chain management, revenue management and quality reporting."
- Block machinery: "Maximize Block Utilization: We've improved block utilization through adaptive case averaging and block scheduling. With the addition of a single owner of a block, OR Manager enhances accountability and ensures operating room time is used more efficiently."
- Preference cards: "Leverage physician and procedure preference cards for greater efficiency"; "detailed and powerful preference cards that support global updating, case costing and implant/tissue documentation"; "The preference card is selected automatically when the surgeon and procedure are added to the surgery scheduling software."
- Tissue/implant documentation: "built-in tissue and implant documentation for regulatory compliance"; recall support — "a list of patients with the given tissue or implant can be easily obtained"; tracks receipt/preparation of tissues including solution and antibiotic administration and packaging integrity.
- Cost capture: "Comprehensive Patient Cost Capture: Append costs directly to the patient record in context"; customer quote: "real time supply costing by procedure/physician"; "perioperative leaders to view product waste in near real time."
- Scheduling tools: "Advanced tools for managing daily schedules, addressing conflicts, and ensuring optimal OR usage"; conflict handling — "a new dedicated 'issues' column that highlights the exact location of conflicts"; "Rearrange daily schedules with ease by adding bookings to a queue, sorting them by age and laterality, and efficiently reassigning them to rooms or blocks"; "Confidently Schedule Surgery and PAT Appointments."
- Analytics: "key performance indicators for the surgical encounter"; "data on block utilization, case costs and times, and the impact of surgeons, services, and procedures"; "Dynamic drill-downs and filtering enable OR leadership to gain insights."
- FAQ: integrates with Hospital Information Systems; customizable documentation screens.
- Suite context (suite page + FAQ): suite = Preop Manager, OR Manager, Anesthesia Manager, PACU Manager, SmarTrack Next, Envision Analytics, "unified into a single clinical documentation and workflow platform for the surgical patient journey, from pre-op to discharge"; "One Contiguous Patient Record."
- Suite FAQ on scheduling: "Within OR Manager, scheduling tools support multi-facility operations and physician-office direct reservations via 'Physician Office Link.' It uses historical procedure times to estimate duration, optimize scheduling, and improve OR utilization."
- Suite FAQ on OR Manager: "Automate surgical scheduling, resource management, intra-operative documentation, and supply costs in one unified operating-room system."
- SmarTrack Next (tracking sibling): "near real-time tracking of patients and staff"; "proactively notifies team members and families of patient status changes or delays, replacing manual calls and physical whiteboards with configurable digital displays and alerts."
- Envision Analytics: near real-time metrics; tracks "case volumes, delays, cancellations, operating room efficiency, cost per case, quality outcomes, and compliance metrics."
- Beneficiary framing (suite FAQ): "Schedulers and OR coordinators optimize room usage and case sequencing"; "Quality, finance, and leadership teams gain access to compliance, cost, and efficiency data."

## Product B — SIS Surgery (Surgical Information Systems)

### Key observations

- SIS Surgery page title: "Operating Room Software"; "Comprehensive perioperative solutions from preop through postop help hospitals better manage the perioperative process."
- Three named benefit pillars:
  1. **Clinical Documentation** — "Intuitive OR documentation with charting by exception and configurable workflows that help ensure compliance."
  2. **Surgical Scheduling** — "Improved schedule management with advanced block time allocation, comprehensive resource management, and conflict checking."
  3. **Patient Tracking** — "Proactive coordination and communication with electronic patient tracking displays to reduce delays and cancellations."
- Enterprise EHR integration: "SIS fills the perioperative gap in your hospital systems. Using interoperability standards, SIS integrates surgery and anesthesia information with your hospital enterprise EHR"; "One care event and one, comprehensive, perioperative [record]"; "Medical device integration for documentation support"; "Up-to-date and accessible OR patient records."
- SIS Analytics add-on: "self-service analytics with drill down capabilities"; "Visual dashboards and access to Key Performance Indicators."
- Add-on products (named): SIS Web ("Web-based Surgeons' Office Schedule Request"), SIS PAT Scheduling ("Optimized Pre-Admission Testing"), SIS Surg eBoards ("Patient Tracking Boards"), SIS Reports, SIS Rules-Based Charging ("Accurate Charge Capture"), SIS Trax ("Tissue Management"), SAP 3 ("SIS Analytics Perioperative Performance Program").
- Homepage (hospital family): SIS Anesthesia ("documenting anesthetic events") and SIS Surgery ("comprehensive surgery information management") as separate hospital products — same-vendor sibling split as Picis.
- ASC pole (SIS Complete, homepage claims): "Connect directly to your surgeon's office and minimize scheduling gaps with real-time visibility into block utilization, case availability, and schedule changes across the ASC"; "Optimize inventory by aligning case scheduling, preference cards, and real-time usage data to reduce waste, stockouts, and excess spend"; "improving documentation and charge capture accuracy through integrated scheduling, real-time charting, and workflow-driven compliance checks"; "See the total cost of every case broken down by line item."

## Product C — Qventus Surgical Growth (analytics/automation overlay)

### Key observations

- Positioning: "So much more than just a scheduling tool, our Surgical Growth Solution harmonizes your growth strategy to your day-to-day operations, helping fill ORs with the cases that matter most"; "Grow strategic surgical volume: AI teammates fill your ORs with the cases that matter most."
- Capacity Assistant: "predicts with high confidence which partial or full blocks are unlikely to be used, up to a month in advance. Then, they deploy personalized nudges that engage surgeons and schedulers to release blocks weeks in advance"; "Shifts lower-acuity cases to your ASCs."
- Vendor blog (by a physician author) documents the block economy from the practitioner side:
  - "Surgeons must proactively release the allocated block time they know they will not be using or it will show as unavailable. Even if the hospital has an auto-release policy, it usually kicks in just a few days before the block that is being released. By the time the auto-release occurs, it's too late to fill the time."
  - Manual scheduling pain: "a lack of visibility into open time slots"; "back-and-forth between schedulers and the OR"; schedulers struggle to find time "outside of their surgeon's assigned block time."
  - Case-length estimation factors: "type of procedure, the hospital and specific OR in which the case is being performed, the clinician(s) involved, seasonality, time of day, trends in a surgeon's time performing the same operation."
  - Named mechanisms: "Available Time Outreach" (automatically offering available time to best-fit surgeons); "TimeFinder" ("an intuitive reservation interface used to view and request OR time in real time," filtered by predicted fit).
- Clinic Scheduler Assistant: "digitizes faxes and makes it easier for schedulers to book strategic cases"; metrics vendor-claimed (96% acceptance, 22-minute median turnaround).
- Robotics Assistant: real-time dashboards "for everything from day-of activities to quarterly business reviews."
- Analytics suite: "OR Leader Dashboard — block allocation optimization opportunities with volume, throughput, utilization, and engagement data"; "Surgeon Dashboard — case volume, market rankings, referral network integrity, and personal OR metrics"; "Executive Dashboard — trends in case volume, primetime utilization, and block utilization."
- EHR integration: "Qventus integrates seamlessly with your EHR" — explicitly an overlay, not the record holder.
- Strategic Control Panel: "deploy our AI teammates to operationalize your growth objectives" — robotic optimization, service line growth, ASC optimization.
- Vendor-claimed outcomes (root page): "Reduce surgery cancellations by up to 40%", "Add three strategic cases per OR per month" — excluded from final document as claims.

## Product D — Peer-reviewed reference: OR management practice (University Hospital Augsburg)

### Key observations (layer A for the study; layer B when generalized)

- Framing: "operating rooms are a major bottleneck resource and an important revenue driver in hospitals"; "between 60 and 70% of hospital admissions are due to surgeries"; "around 40% of hospital expenses, as well as revenues, are generated in the operating theaters"; "staffing cannot be changed daily to respond to changing demands"; "the resulting high complexity in operating room management necessitates perpetual process evaluation and the use of decision support tools."
- Master surgery schedule (MSS): "The master surgery schedule (MSS) predetermines the daily assignments of each operating room to medical departments. An MSS holds for every week until the next revision takes place."
- Department preliminary schedules: "The departments set up preliminary schedules for their respective patients independently of each other, based on the current allocation of the MSS… These schedules, in general, follow the logic to fill regular hours with semi-urgent and elective patients. These schedules are available no later than the day before surgery."
- OR-coordinator role: "An OR-coordinator is responsible for coordinating the individual schedules of the departments and for disruption management."
- Disruption management options: "the reallocation of operating rooms, the extension of opening times, and postponing surgeries are available to manage short-term disruptions"; emergency patients "are assigned to the emergency operating room or the next available operating room. If the emergency patient is assigned to any room other than the emergency operating room, the remaining patients on the room's schedule are postponed accordingly. Should this cause elective patients to be moved outside of the operating hours, they are deferred to the next day."
- Patient acuity grouping: elective / semi-urgent (surgery within 24 h) / very-urgent (within 6 h) / emergency (ASAP); dedicated emergency OR ("staffed and on stand-by"); two rooms run overnight for very-urgent cases.
- Case process flow with system-collected timestamps: patients wait in the holding area → anesthesia induction → moved to OR → procedure ("the time from the first cut to suture is widely used in productivity benchmarks") → surgical follow-up → moved to PACU or ICU with handover; anesthesia-team presence vs OR-occupation durations distinguished.
- KPIs in use: utilization (reported separately for regular vs extended hours; system utilization incl. anesthesia/cleaning vs room utilization), overtime/undertime vs planned opening hours per the MSS, patient waiting time per acuity type, number of treated patients, number of deferred surgeries, anesthesia turnover time; sequencing policies (FIFO / shortest-first / longest-first) as managed policy options; parallel induction of anesthesia as a capacity policy.
- The study's purpose itself: "allows operating theater managers to test a multitude of potential changes in operating room management without disrupting the ongoing workflow"; insights "served to calibrate the newly implemented planning software."

## Product E — Epic OpTime / Oracle Health (market anchors)

### Key observations

- No public operational documentation reachable (consistent with prior passes; Oracle docs index has no public surgical-module operational docs; Epic closed). Included only as market anchors demonstrating that the EHR-embedded perioperative module is a dominant deployment pattern in large US health systems. No product-specific claims made anywhere.

## Cross-product Comparison

| Dimension | Picis OR Manager | SIS Surgery | Qventus Surgical Growth | Augsburg practice (study) | EHR modules (Epic/OH) |
|---|---|---|---|---|---|
| Managed object | OR time: rooms, blocks, cases, supplies, revenue | OR time: scheduling, docs, tracking pillars | OR capacity: blocks, open time, case placement, demand | OR theater: 18 rooms, MSS, schedules, disruptions | (anchor only) |
| Unit of work | surgical case (scheduling + documentation + costing) | surgical case | case requests/booked time (no day-of record) | surgical case with timestamped sub-processes | — |
| Capacity allocation | block scheduling; single block owner; adaptive case averaging | "advanced block time allocation, comprehensive resource management" | block prediction + release nudges; open-time marketing | MSS: room ↔ department per week; departmental preliminary schedules | — |
| Conflict handling | dedicated "issues" column; rebooking queue (age, laterality); reassign to rooms/blocks | conflict checking at scheduling | — (avoids conflicts upstream by predicting unused time) | OR-coordinator disruption management; postponement/deferral rules | — |
| Duration estimation | "uses historical procedure times to estimate duration" (suite FAQ) | (not stated) | ML case-length prediction (procedure, room, clinician, seasonality…) | historical duration distributions per specialty/acuity | — |
| Day-of execution | SmarTrack Next (sibling): near-real-time tracking, notifications, whiteboard replacement | Patient Tracking pillar + Surg eBoards add-on | none (upstream only) | whiteboard-era coordination documented as timestamps + coordinator role | — |
| Turnover | suite analytics: turnaround time (Envision) | (not stated) | (not stated) | turnover time KPI; cleaning time in room utilization | — |
| Supplies/preference cards | preference cards auto-selected at booking; global updates; case costing; implant/tissue docs; recalls | preference cards + real-time usage data aligned to scheduling (ASC pole); SIS Trax tissue management | — | — | — |
| Revenue/charging | revenue management; costs appended to patient record | rules-based charging add-on; charge capture | — | (revenue-driver framing in literature) | — |
| Analytics | block utilization, case costs/times, surgeon/service/procedure impact, drill-downs | dashboards + KPIs; SAP 3 program | OR leader / surgeon / executive dashboards: volume, throughput, utilization, primetime, block utilization | utilization, overtime/undertime, waiting time, deferrals | — |
| Patient-facing/booking intake | PAT appointments; physician-office reservations (Physician Office Link) | SIS Web (surgeons' office schedule request); PAT scheduling | clinic EMR-integrated booking; fax digitization | departmental preliminary schedules by day before | — |
| Integration | HIS integration | enterprise EHR + device integration | EHR integration (overlay) | IT system collects timestamps | are the EHR |
| Packaging | perioperative-suite sibling product | standalone department system + add-ons; separate ASC product | analytics/automation overlay | paper+IT practice | EHR module |

### Cross-product commonalities (Evidence layer B)

All three evidence-bearing products, plus the practice study, converge on:

1. **Identified operating rooms as the managed capacity** — rooms/suites with staffed session time being allocated, filled, and measured.
2. **The scheduled surgical case as the unit of work** — patient + procedure(s) + surgeon + room + date/time + duration estimate, carrying resource requirements.
3. **A schedule-of-record machinery** — booking under constraints, conflict checking, and adjustment (reassignment, postponement, deferral) up to and during the day of surgery.
4. **Allocation of scarce OR time to owners** — recurring room/service allocations (MSS, block time) with release/recapture dynamics; block utilization as a first-class metric in every sample.
5. **Duration estimation from history** — historical procedure times as the basis of scheduling (explicit in Picis, the study, and Qventus).
6. **Measurement of OR time usage** — utilization (with distinctions such as regular vs extended hours), on-time/delays, overtime/undertime, deferrals, turnover; OR economics (cost per case) in the US-pole products.
7. **Surgeon/service accountability framing** — per-surgeon and per-service views of time and cases; block ownership as accountability.
8. **Multi-party coordination** — schedulers, OR coordinators, departments, surgeon offices, anesthesia, leadership all as interacting roles.
9. **Integration posture** — the OR system consumes/feeds HIS/EHR (patient identity, posting, billing) in every sample; standalone-vs-embedded is packaging, not function.
10. **Patient-throughput orientation** — PAT (pre-admission testing) linkage, cancellations/delays reduction, PACU/ICU destinations in scope of the operational picture.

### Divergences (candidate L2/L3)

- Packaging: perioperative-suite sibling (Picis) vs standalone department system + add-ons (SIS) vs EHR module (Epic/OH anchors) vs analytics overlay (Qventus) (L2).
- Day-of tracking: in-family sibling product (Picis SmarTrack Next) vs named pillar + add-on boards (SIS) vs absent (Qventus) (L2).
- Documentation depth: intraoperative charting inside OR Manager (Picis) vs pillar with charting-by-exception (SIS) vs none (Qventus) — charting is a common capability, not the center (L2).
- Supply chain depth: preference cards + tissue/implant registry + recalls (Picis, SIS) vs absent (Qventus) (L1/L2 boundary case).
- Revenue machinery: rules-based charging, cost-per-case (US-pole products) (L2).
- Segment: hospital OR vs ASC (SIS Complete pole: revenue-cycle-heavy, block visibility for surgeons' offices) (L2).
- AI/automation: prediction + nudge + automated outreach (Qventus; era machinery) (L2).
- Geography: US block/relative-value economics vs globally-budgeted systems (the study's German university hospital manages cancellations/deferrals under different financing; financing regime not part of the structure) (L2).
- Regional vocabulary: "operating room management" (US) vs "operating theatre management" (UK/EU, incl. the study's "operating theater") (L2).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **Identified operating rooms held as schedulable capacity** — the OR (and its staffed session time) exists in the system as an individually identified, bookable, scarce resource. Remove → patient/clinic scheduling or generic room booking; there is no OR to manage.
2. **The scheduled surgical case as the unit of record** — each planned procedure held as a record binding patient × procedure(s) × surgeon × room × time, with a duration estimate and the resources the case requires. Remove → a staffing roster or a room calendar with no surgery in it.
3. **The managed schedule and its day-of execution loop** — cases are placed into rooms/sessions under the department's allocation arrangements and kept current as reality diverges (add-ons, urgent insertions, cancellations, delays, reassignment between rooms/blocks, postponement/deferral), with case progress through the day visible enough to coordinate the department — the digital successor of the OR whiteboard. Remove → a static booking list; nothing is being managed.

Justification for minimality:

- **Intraoperative clinical documentation is NOT L0**: it is a common module (Picis includes it; SIS names documentation a pillar; the AIMS sibling exists precisely for the anesthesia record), but an OR-management product is still recognizable as such with charting handled by sibling/host products. The AIMS pass already established that the anesthesia record is the AIMS center, not the OR's.
- **Formal block-time objects are NOT L0**: allocation of OR time to owners IS part of leg 3's "allocation arrangements," but the specific block/release/auto-release/recapture implementation is the dominant modern mechanism, not the invariant — the MSS-style room↔department template (study) achieves the same allocation without per-surgeon blocks.
- **Preference cards / supply chain are NOT L0**: universal in hospital-pole products but absent in the overlay pole; a capability layer on the case.
- **Measurement/performance reporting is NOT L0 but sits just above it**: OR-time measurement (utilization, delays, turnover) appears in every evidence-bearing source and motivates the whole Type ("bottleneck resource, revenue driver"), but a product that manages schedule + day-of without analytics is still this Type; conversely a product that only measures (Qventus/LeanTaaS class) does NOT hold the schedule of record and is held as an overlay, not the Type.
- **Day-of execution loop IS L0**: the Type's name and every source's framing is "management" of the OR as it runs — the study's OR-coordinator disruption management, SIS's Patient Tracking pillar, Picis's whiteboard-replacement sibling all point at the same structure. A booking-only tool is scheduling software, not OR management.

Jointly-held load-bearing: (1 alone = room booking; 2 alone = surgical appointment book; 3 alone = whiteboard; 1+2 without 3 = booking calendar; 2+3 without 1 = generic case tracker).

### L1 — Common Mature Structure

- Block-time management: recurring time allocations to surgeons/services, ownership, release/auto-release/recapture, block-utilization accounting.
- Case duration estimation from historical procedure times (per procedure, surgeon, room; increasingly ML-assisted).
- Conflict checking at booking; waitlist/rebooking queues; laterality and case-attribute checks surfaced in sample documentation.
- Day-of boards: patient phase tracking (pre-op/holding → in OR → to PACU/ICU), staff tracking, delay flags, configurable displays, notifications to staff/families (whiteboard replacement).
- Turnover (turnaround) management and measurement between cases; first-case on-time starts.
- Staff/team assignment for cases (anesthesia, scrub/circulating teams) at least at the assignment level; deeper rosters vary.
- Preference cards (surgeon + procedure supply/instrument lists), auto-selection at booking, global updates, usage capture, case costing.
- Supply/implant/tissue documentation attached to the case, including recall lookup.
- Intraoperative documentation/charting modules (often charting-by-exception) — capability, sibling-overlap with AIMS territory.
- Charge capture / revenue management from the case record; cost-per-case views.
- PAT (pre-admission testing) scheduling and readiness linkage; surgeon-office request portals.
- Urgent/emergency case insertion (add-on cases, dedicated emergency rooms, deferral rules).
- Analytics/reporting: utilization (regular vs extended hours), block utilization, case volumes/delays/cancellations, surgeon/service/procedure impact, cost; role-based dashboards.
- Multi-facility support; HIS/EHR integration (identity, posting, results).

### L2 — Variant / Optional Structure

- Packaging: standalone department system / perioperative-suite sibling / EHR-embedded module / analytics-automation overlay on the schedule.
- Segment: hospital OR (multi-department, trauma mix) vs hospital-outpatient department vs ASC (smaller, revenue-cycle-heavy, surgeon-office-facing block visibility).
- Acuity mix and emergency infrastructure: elective-heavy vs trauma/emergency-heavy programs (dedicated emergency ORs, night rooms, insertion policies).
- Financing regime: US fee-for-service economics (block accountability, charge capture) vs globally-budgeted systems (cancellation/deferral management) — regime shapes emphasis, not structure.
- AI/automation layer: unused-block prediction, nudge workflows, case-length ML, automated time marketing (era machinery, current-pole products).
- Regional vocabulary: "operating room management" vs "operating theatre management."
- Family portals / patient-status notifications to families (single-product evidence).

### L3 — Vendor-specific (Research Notes only)

- Picis: Physician Office Link (physician-office direct reservations), adaptive case averaging, SmarTrack Next (family portals, mobile alerts), Envision Analytics (Power BI dashboards, nightly HIS refresh), Device Hub, SmartRequest, PicisPrima.
- SIS: SIS Web, SIS PAT Scheduling, SIS Surg eBoards, SIS Rules-Based Charging, SIS Trax (tissue management), SAP 3, SIS Scribe (operative notes), Amkai/SourceMed ASC lineage, SN Chart.
- Qventus: Capacity/Market Research/Strategic Marketing/Clinic Scheduler/Robotics Assistants, TimeFinder, Available Time Outreach, CLAT (Case Length Adjustment Tool), Strategic Control Panel; vendor-claimed metrics (40% cancellation reduction, +3 cases/OR/month, 30% duration-estimation improvement, 96% request acceptance, 22-minute turnaround, 100 scheduler-hours/month saved).
- Vendor driver/feature counts and ROI claims generally — marketing claims, excluded from the final document.

## Historical / Market-Sample Check

- Paper-era analog: the OR booking book (cases with patient/procedure/surgeon/room/time), the block/master-schedule board (weekly room↔service template), the day-of whiteboard (patient location/phase per room), and tally sheets for times/turnover/utilization — all four defining elements satisfiable on paper; the whiteboard and booking book are explicitly named as what current products replace ("replacing manual calls and physical whiteboards"). No software surface, no block objects by name, no AI in the core.
- Regional check: US products (Picis, SIS, Qventus), German university-hospital practice (study), UK/EU "theatre" vocabulary; globally-budgeted financing changes emphasis (deferrals/cancellations) but not the structure.
- Era check: pre-ML OR scheduling systems (MSS + booking + board + timestamps) satisfy all legs; the AI/automation layer is current-era machinery held at L2.
- Segment check: the ASC pole runs the same three legs (rooms, cases, schedule+visibility) with revenue-cycle emphasis — segment variant, not separate Type.

## Boundary Findings

- **vs Anesthesia Information Management System (JOINT REVIEW — discharges the AIMS pass flag)**: held, both directions confirmed. Picis ships OR Manager and Anesthesia Manager as separate suite products; SIS ships SIS Surgery and SIS Anesthesia as separate hospital products — vendor-confirmed structural separation in two independent vendors. The center of gravity differs: OR management centers the operating room as scheduled, measured capacity (rooms, sessions, blocks, case placement, turnover); AIMS centers the anesthetic care of the patient with device-integrated physiologic capture. Structural test from this side: remove the anesthesia record → OR management remains intact; remove the schedule/room/capacity machinery → AIMS remains. The surgical case is the meeting point (both attach to it), and suites bundle both for purchase — tightly coupled siblings, not one Type.
- **vs Patient Scheduling**: patient scheduling centers the patient's appointment (visits, reminders, provider availability); OR management centers the OR as capacity and the surgical case as unit of work, where the patient is one attribute. PAT scheduling appears inside OR products as a linked capability, not the Type.
- **vs Hospital Management System (OT scheduling slice)**: HMS carries a thin "OT/OR scheduling" module inside the hospital's registration/billing spine; OR management is the surgical department's system of record for rooms, blocks, and day-of operations. Capability slice vs centered Type.
- **vs Bed & Capacity Management / Patient Flow**: the same operational-coordination pattern (live state, placement decisions, throughput metrics) over a different resource — inpatient beds vs operating rooms. Adjacent; post-op destination planning is where they meet.
- **vs Emergency Department Information System**: EDIS runs unscheduled emergency care of its own department; the OR receives emergency cases as insertions into managed OR capacity (dedicated emergency OR, add-on rules) — a policy inside OR management, not EDIS.
- **vs Clinical Documentation / operative notes**: procedure/operative note charting is documentation tooling; OR management may carry charting modules but the case record's operational (not clinical-narrative) content is the center.
- **vs OR analytics/optimization overlays (Qventus, LeanTaaS-class)**: overlays operate on the same object — OR time, blocks, case placement — but hold no schedule-of-record and no day-of execution loop; they read/predict/nudge on top of the EHR/OR system. Held adjacent as an overlay variant, not the Type (consistent with the Qventus vendor's own "more than just a scheduling tool… integrates with your EHR" framing).
- **vs Sterile processing / instrument tracking**: preference cards reference instruments/supplies; the sterile-processing department's reprocessing and instrument-inventory systems are separate operational domains; the seam is the case's supply requirements.
- **vs Enterprise Resource Scheduling / Resource Calendar**: generic resource scheduling has no surgical-case semantics (procedure types, laterality, acuity insertion, turnover); the OR system's schedule machinery is surgery-specific.

## Uncertainties

- Exact case-phase state names and the depth of day-of state (per-patient phase, per-room state, staff presence) could not be verified at field level from public sources; the final document describes phases conceptually (pre-op/holding → in OR → post-op destination) without asserting product-specific state vocabularies.
- Block auto-release windows: the vendor blog says auto-release "usually kicks in just a few days before the block" — kept as weak/qualified wording ("commonly set shortly before the block date"); no exact day counts asserted.
- Staff-rostering depth (whether full labor scheduling lives inside OR management or in adjacent workforce products) unverified; held at "assignment level common, depth varies."
- EHR-embedded modules (Epic OpTime, Oracle Health): market anchors only; their functional depth vs standalone products unverified; no claims made.
- The relative market share of standalone vs suite vs EHR-embedded vs overlay is unknown; described as common deployment patterns without ranking.
- Whether every product's analytics includes first-case on-time starts specifically: not directly evidenced in-sample (the concept is standard in OR management literature but not fetched verbatim); kept out of the final document's metric list or phrased at concept level.

## Final Synthesis

An Operating Room Management system is the surgical department's operational system of record for its most scarce and expensive capacity: it holds identified operating rooms as schedulable resources, holds each scheduled surgical case as a record binding patient, procedure(s), surgeon, room, time and duration estimate with its resource requirements, and manages the schedule-of-record — booking under the department's allocation arrangements (block time or room/service templates), conflict checking, and continuous adjustment as urgent cases, cancellations, and delays force reassignment, postponement, or deferral — with the day-of execution loop that makes case progress visible across the department, the digital successor of the OR whiteboard. Around this core, mature products add block release/recapture machinery, duration estimation from historical case times, turnover measurement, preference cards and supply/implant documentation, intraoperative charting, charge capture, PAT linkage, surgeon-office request portals, and role-based analytics (utilization, block utilization, delays, cost per case). The Type is packaging-agnostic: standalone department system, perioperative-suite sibling, EHR-embedded module, or — on top of any of these — the emerging AI/analytics overlay that predicts unused blocks and automates time filling. Its sharpest boundaries: AIMS (anesthetic-care record vs OR-as-resource; joint-review flag discharged), Patient Scheduling (patient appointment vs OR capacity), Bed & Capacity Management (beds vs rooms), and the analytics overlays (no record held).
