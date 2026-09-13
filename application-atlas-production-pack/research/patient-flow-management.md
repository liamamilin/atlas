# Research Notes — Patient Flow Management

## Research Goal

Determine what a Patient Flow Management application is as an Application Type: its defining core structure, its standard mature capabilities, its variant space, and its boundaries against adjacent types — most importantly Bed & Capacity Management (a pre-hung joint-review flag from the bed-capacity-management pass), plus Hospital Management System / EHR, EDIS, Patient Scheduling, Operating Room Management, and Care Coordination.

## Initial Boundary

- Hypothesis: hospital operations software managing the **patient's journey through the acute episode** (arrival/admission → unit stays → transfers → discharge) as a live, coordinated process — person-centric, in contrast to the bed-centric sibling Type.
- Likely users: patient flow / throughput coordinators, bed managers, capacity leaders, house supervisors, case managers, transfer center staff, operations/command-center teams.
- Likely confusions: Bed & Capacity Management (same market cluster, different center), EDIS (department-scoped tracking), Patient Scheduling (pre-booked slots), Care Coordination Platform (clinical/longitudinal vs operational/episodic), EHR-embedded modules.
- Known market hazard (pre-hung flag): vendors market one capability cluster under both names — Oracle Health sells a product literally named "Patient Flow" whose documented features are bed selection/EVS; TeleTracking markets "Throughput — Integrated Patient Flow"; LeanTaaS names its capacity product "Inpatient Flow". The joint review must decide: one Type or two.

## Research Questions

1. What is the unit of record — the patient journey? the bed? the task?
2. What states does a patient's journey carry (location, stage, expected discharge, barriers)?
3. How does discharge coordination actually work in these products?
4. How does the admission/placement side work, and can the Type exist without bed machinery?
5. What coordination rituals (huddles, rounds, escalations) does the software support?
6. What data flows in/out of the EHR/PAS?
7. Where is the line vs Bed & Capacity Management — and can both Types survive the removal tests?
8. Do older / regional (UK NHS) / non-AI products still fit the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different geographies/customer tiers, and coverage of the porous naming cluster:

1. **TeleTracking (Operations IQ Platform — Throughput module)** — US enterprise market leader; integrated operational platform that straddles the bed/flow cluster (needed for the joint review).
2. **LeanTaaS iQueue for Inpatient Flow** — analytics/insight-first pole; daily capacity plan, care progression, huddles, staffing.
3. **Qventus (Inpatient Capacity solution)** — AI-automation pole; EHR-embedded discharge planning; notably **no bed placement machinery** — independence evidence for a person-journey Type.
4. **Liaison Assist / Infinity Health (Patient Flow solution)** — UK NHS regional pole; task-based journey coordination replacing paper/whiteboards; non-AI, operational.

## Sources

- TeleTracking — https://www.teletracking.com/ ; https://www.teletracking.com/healthcare-operations-iq-platform/throughput/ ✅ (Tier-2 solution pages; Knowledge Bridge customer portal login-gated)
- LeanTaaS — https://leantaas.com/products/inpatient-flow/ ✅ (Tier-2 product page)
- Qventus — https://qventus.com/ ; https://qventus.com/solutions/discharge-planning/ ✅ (Tier-2 solution pages; KLAS Capacity Management category reference)
- Liaison Assist (Infinity Health) — https://infinityhealth.io/ ; https://infinityhealth.io/patient-flow/ ✅ (Tier-2 solution pages)

No sampled vendor publishes public Tier-1 operational documentation (help centers / user guides) for flow modules. Evidence rests at Tier-2 official solution-page level throughout. Vendor outcome metrics (percentages, hours, bed-days) are marketing claims and are recorded as claims only.

## Product A — TeleTracking (Operations IQ — Throughput) — Evidence layer A (page claims)

- Positioning: "Integrated Patient Flow Across the Care Continuum." The Throughput module "coordinates every step of the acute care journey, from admission to discharge, so your hospital operates as a unified system rather than a collection of competing bottlenecks."
- Problem framing: "ED boarding, delayed discharges, idle beds, overwhelmed staff — these aren't isolated problems. They're symptoms of disconnected patient flow."
- Shared view: "unifies all of these workflows into a single operational view — so no step in the patient journey is managed in isolation, and no handoff falls through the cracks." "Every stakeholder [gets] a single, real-time source of truth across the enterprise."
- Automation targets: "discharge triggers, transport requests, EVS tasking" — "Phone calls to request transport. Manual EVS notifications. Discharge triggers that depend on someone remembering to act."
- Sub-capabilities:
  - Patient Placement: "Real-time care progression indicators keep admissions on pace with discharges, eliminating the lag between a bed becoming available and a patient reaching it."
  - EVS Management: automated cleaning requests at discharge ("the gap between discharge and room readiness").
  - Transport Management: built-in zoning, mobile interface.
  - Discharge Workflows: "Care teams stay coordinated through automated triggers and integrated workflows, so discharge doesn't stall waiting on a single point of action."
- Decision IQ (AI module): "ensures that every single discharge has an impact on patient flow… bottlenecks, like ED boarding and overstays are reduced, while hospital capacity expands."
- AutoDischarge: RTLS detects patient exit → automatic EVS notification ("reducing dirty bed times from hours to minutes").
- Metrics named: LOS, boarding, discharges, bed turnaround.
- Platform neighbors: Access module (arrival/front-door), Transfer & Command Centers (delivery model), Data & Analytics, Decision IQ. Cloud-hosted, EHR-integrated.

### Key observations
- Person-journey vocabulary present and central ("every step of the acute care journey", "care progression indicators", "no handoff falls through the cracks").
- Straddles both clusters: carries the full bed-operations machinery (EVS, transport, placement) AND journey/discharge coordination. Ideal straddle sample.
- The discharge event is the pivot that triggers the downstream loops; flow management here = keeping admissions pacing with discharges.

## Product B — LeanTaaS iQueue for Inpatient Flow — Evidence layer A (page claims + product screenshots)

- Tagline: "Make Every Inpatient Bed Count" — "a connected, insight-driven plan the whole system can execute, every day. Anticipate capacity constraints, surface barriers, and coordinate action."
- Scope claim: "connecting decisions across capacity, admissions, care progression, staffing, and discharge to improve patient flow across the system."
- Capability pillars:
  1. Capacity management: "Bring updates, escalations, and operational concerns together **before daily bed huddles**, automatically capture key decisions and actions, and **track follow-through** so teams can resolve emerging constraints and activate capacity protocols earlier."
  2. Admission planning / placement: "Give the ED, PACU, transfer center, and bed management a **shared view of incoming demand and placement progress**, helping teams prioritize patients, coordinate appropriate admission options (e.g., hospital at home), and reduce boarding and downstream delays."
  3. Care progression: "Bring care-progression signals and patient context into a unified view, **surface patients and barriers requiring intervention**, and focus **multidisciplinary rounds** on the actions needed to move patients forward."
  4. Staffing alignment: shift-level census and workload forecasts → staff-allocation and incentive-pay decisions.
  5. Discharge predictability: "Use multidisciplinary rounds to identify likely discharges and uncover **clinical, social, and logistical barriers** earlier, then coordinate follow-up across care management, ancillary teams, and discharge-lounge workflows to make beds available sooner."
- Product screenshot (direct UI observation): care-progression dashboard tiles "Likely DC Today 49", "Boarding >2 Hours 5", "Early DC Opportunity 6", "Needs EDD Review 9"; per-patient table of EDDs and predicted discharge dates, "linked to EHR".
- Vendor outcome claims: 6% admissions increase, 35% ED boarding reduction, 12hr LOS decrease, 40% LWBS reduction (marketing claims).

### Key observations
- Insight-first: no per-bed task execution machinery on the page; the product's substance is the daily coordination plan (huddle → decisions → tracked follow-through) and per-patient progression signals.
- Confirms the daily-rhythm operating model: bed huddles + multidisciplinary rounds are first-class software objects (agendas, captured decisions, follow-through tracking).
- Transfer center appears as one consumer of the shared admission view — a component of the flow picture, not the whole.
- "Hospital at home" appears as an alternate admission destination — journey endpoints beyond the physical bed.

## Product C — Qventus (Inpatient Capacity) — Evidence layer A (page claims)

- Positioning: "Transform your patient flow and discharge planning with our AI-powered Inpatient Capacity Solution." Solution nav label: "Inpatient Capacity — Automating the right actions to promote patient flow and create capacity."
- Architecture claim: "fully integrated into Epic, Cerner, and most other standard EHRs… care teams never have to switch between interfaces"; described as "a system of action on top of your EHR."
- Five named "AI assistants" (vendor names, recorded as L3):
  1. Discharge Planning Assistant — "auto-populate EDD and dispositions directly into the EHR on the first morning after admission. Models continue to pressure test the discharge plan throughout the patient's stay, identifying opportunities for earlier discharge, and discharges to lower levels of care." Locally trained ML.
  2. Flow Priority Assistant — "automatically sequences ancillary orders (therapy, imaging, lab) to best support patient flow and discharge success."
  3. Care Gap Assistant — "evaluates each patient care plan to identify and resolve gaps that could delay discharge, such as physical therapy, MRI, case management consults, foleys."
  4. Case Manager Assistant — "spot every opportunity for earlier, lower-acuity discharge… scoring patients based on likeliness for acceptance" (post-acute placement, SNF).
  5. Capacity Intelligence Assistant — "identify in real-time the most impactful actions leaders can take to boost throughput… easily identify and deploy the right staff."
- Analytics & Insights: real-time dashboards ("planned discharges, progress toward goals"), "strategic escalations — identify exactly where and how to intervene when care teams need support with at-risk discharge plans."
- MDR (multidisciplinary rounds) support: "40% fewer clicks during MDRs" (vendor claim).
- **No bed-state, placement, EVS or transport machinery anywhere on the product pages.** The entire product is per-patient journey/discharge orchestration inside the EHR.
- KLAS context: "Best in KLAS for Capacity Management 2025" (vendor-cited) — the market category treats this as capacity management, reinforcing the naming porousness.
- Vendor outcome claims: reduce excess days 15–30%, $3M cost savings, 5x ROI (marketing claims).

### Key observations
- **Independence evidence**: a recognized patient-flow/capacity product holding the journey + delay-removal core with NO bed layer. Remove the bed core → still clearly Patient Flow Management.
- Discharge planning starts at admission (EDD populated the first morning) — the journey is managed prospectively from day one, not just on the day of discharge.
- Barrier machinery is per-patient care-plan level (gaps, consults, orders), coordinated across ancillary teams.
- EHR-embedded surface model: the "shared view" can live inside the EHR rather than as a standalone board.

## Product D — Liaison Assist / Infinity Health (Patient Flow) — Evidence layer A (page claims)

- Positioning: "Improve patient flow and bed management. Hospital staff can increase the number of patients safely discharged each day and enable faster allocation of beds to those who need them the most."
- **Core sentence (direct quote)**: "Tasks are the bedrock of accurate and effective movement of patients through the healthcare system. Integrated task management underpins Liaison Assist allowing **patients to be tracked by location and throughout their patient journey, with the tasks that need to be completed**."
- Problem framing: "Hospital site teams often lack an up-to-date view of available beds and an accurate forward-view of discharges, with the tasks that need to be completed for patients."
- What the software shows: "live bed-state, task status, and visibility of discharges for the day… prioritise patients and allocate them to the most appropriate ward, while identifying and unblocking tasks that impede patient flow through the hospital."
- Benefits: bed allocation (all-locations view + "forward-view of confirmed AM and PM discharges"); discharge planning (ward teams view new admissions, patients waiting to be admitted, high-acuity patients, patients due for discharge; "proactively identify and unblock tasks that cause delays"); LOS reduction ("digital prompts to complete tasks and digital automations of high-volume tasks allow clinical best practice to be standardised and unnecessary delays removed from pathways"); staff-time savings.
- Integration: "can integrate with PAS and EPR systems… ensuring admissions, discharges and transfers are automatically recorded and surfaced on its dashboards." HL7 FHIR interoperable; DSP Toolkit; G-Cloud 13 (UK public-sector procurement).
- User testimonial: "Liaison Assist provides a fantastic flow of information, following the patient from admission to A&E to discharge" (A&E Team Leader, London North West University Healthcare NHS Trust).
- Lineage: "Replace paper processes, whiteboards, and physical checks… in six weeks."
- Vendor outcome claims: 20,000 bed days saved in one year at one trust; 91 minutes saved per user per shift (marketing/case-study claims).
- The same platform sells adjacent solution lines (Hospital at Home, Outpatients Transformation) — patient flow is one application of a task-orchestration platform.

### Key observations
- The UK regional pole: "patient flow" here = tracking patients through their journey with attached tasks + discharge forward-view + bed allocation support. Person-journey core intact; explicitly the digital successor of paper lists and whiteboards — valuable historical/lineage evidence.
- Non-AI: coordination happens through task triage, prompts, and shared real-time state. Shows AI depth is variant, not definitional.
- Bed-state appears as one consumed surface among several — the journey+tasks are the product's center ("tasks are the bedrock").
- NHS vocabulary: "site teams", "wards", "PAS" (patient administration system), A&E. Confirms the bed-capacity pass's regional-vocabulary observation from this side.

## Cross-product Comparison

| Dimension | TeleTracking Throughput | LeanTaaS iQueue | Qventus Inpatient Capacity | Liaison Assist |
|---|---|---|---|---|
| Unit of record | "every step of the acute care journey" + handoffs | per-patient progression signals + daily plan | per-patient EDD/disposition/care plan | per-patient journey + attached tasks |
| Shared live view | "single operational view… no handoff falls through the cracks" | shared view for ED/PACU/transfer center/bed mgmt | EHR-embedded surfaces + dashboards | real-time site picture (bed-state, tasks, discharges) |
| Discharge machinery | discharge workflows w/ automated triggers; AutoDischarge (RTLS) | likely-discharge ID; clinical/social/logistical barriers; discharge lounge | EDD auto-populated day 1; pressure-tested all stay; lower-acuity moves | forward-view of confirmed AM/PM discharges; unblocking tasks |
| Barrier/delay surfacing | "discharge doesn't stall waiting on a single point of action" | "surface patients and barriers requiring intervention" | care gaps predicted per patient; strategic escalations | "identify and unblock tasks that impede patient flow" |
| Admission/placement side | patient placement w/ care-progression indicators | shared incoming-demand view; prioritization; hospital-at-home | (not present on pages) | prioritise patients, allocate to appropriate ward; live bed-state |
| Coordination rituals | (implied; bottleneck/boarding reduction) | bed huddles w/ captured decisions + follow-through; MDRs | MDRs; strategic escalations | (not on page) |
| Automation depth | triggers, RTLS, EVS/transport tasking | insight + follow-through tracking | AI assistants act on below-license tasks | task triage, digital prompts, high-volume automations |
| AI/ML depth | Decision IQ module | predictive EDDs/discharge dates (linked to EHR) | locally-trained ML throughout | none on pages |
| Staffing linkage | (not on page) | shift-level census/workload forecasts | "deploy the right staff" | (not on page) |
| EHR/PAS substrate | "seamlessly integrated with the EHR" | EDDs "linked to EHR" | embedded in Epic/Cerner | PAS/EPR integration; ADT auto-recorded |
| Metrics emphasized | LOS, boarding, discharges, bed turnaround | boarding, LOS, admissions, LWBS | excess days, LOS, planned discharges | daily safe discharges, LOS, bed days |
| Bed layer present? | yes (full) | indirect (admission planning view) | **no** | partial (bed-state as consumed surface) |

### Cross-product conclusions

- **B-layer commonality (all four)**: per-patient journey tracking with timing; discharge as the pivotal coordination event; delay/barrier surfacing and unblocking; a shared real-time operational picture; EHR/PAS ADT substrate; throughput metrics.
- **B-layer commonality (3 of 4)**: coordination rituals (huddles/MDRs/escalations); automation of flow handoffs.
- **Variant axes**: AI/ML depth (none → full AI); bed-layer bundling (none → full); staffing linkage; transfer-center/command-center delivery; care-setting breadth (inpatient core, extensions to hospital-at-home/outpatients).
- The market's naming porousness is real and confirmed from this side: the KLAS category is "Capacity Management" while product names say "Patient Flow"/"Inpatient Flow"; conversely Oracle Health's "Patient Flow" product (sibling research) is bed-centric.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures; none naming software surfaces, AI, beds, or specific rituals:

1. **The live tracked patient journey** — each patient in the facility's acute episode is held in the system as a progression subject: where the patient is in the journey (location/stage) and where they are heading (anticipated moves and discharge), with timing visible. Remove → no flow subject; what remains is disconnected departmental records or a bare bed board.
2. **Delay-surfacing and progression coordination** — the system identifies patients whose progression is stalled or at risk (barriers, overdue discharges, boarding) and coordinates the corrective actions across the teams and units involved. Remove → a passive tracking board / census report; the "management" in the type name is gone.
3. **The shared house-wide operational picture** — one live view of the journeys that the coordinating roles (flow/capacity staff, unit teams, intake) jointly act from, whether standalone or EHR-embedded. Remove → per-department silos, the failure mode the Type exists to fix.

### L1 — Common Mature Structure

- Discharge coordination machinery: expected/estimated discharge dates, likely-discharge identification, barrier lists (clinical/social/logistical), discharge worklists, forward-view of the day's discharges
- Admission/intake coordination: shared incoming-demand view (ED, PACU, transfer center), prioritization, admissions paced against discharges, boarding visibility
- Coordination rituals supported in software: daily bed huddles, multidisciplinary rounds, escalation paths — with captured decisions and follow-through
- Throughput metrics and dashboards: LOS, excess days, boarding time, discharge counts, turnaround
- EHR/PAS integration: ADT events in; actions/plan data back (EDD, dispositions)
- Automation of flow handoffs: discharge triggers, transport/EVS task notification, ancillary-order sequencing, task triage/prompts
- Task layer: flow-relevant tasks attached to the patient journey, triaged and tracked

### L2 — Variant / Optional Structure

- AI/ML depth: locally trained EDD prediction, care-gap prediction, order sequencing, post-acute acceptance scoring, prescriptive leader actions (none in the UK sample → clearly optional)
- Staffing-demand alignment (shift-level census/workload forecasts)
- Transfer-center / command-center delivery model (centralized, optionally multi-facility)
- RTLS/sensor-triggered automation (patient exit detection)
- Bed-state/placement bundling (the sibling Type's core, frequently sold inside the same suite)
- Care-setting breadth: hospital-at-home, post-acute placement, outpatient/ambulatory flow extensions
- Regional vocabulary: "patient flow" vs "throughput" vs "patient journey"; UK PAS/site-team framing vs US capacity framing

### L3 — Vendor-specific (Research Notes only)

- TeleTracking: Operations IQ platform naming; Throughput/Access/Decision IQ module names; AutoDischarge; Adopt IQ services; "dirty bed times" phrasing
- LeanTaaS: iQueue brand; pillar names; UI labels ("Likely DC Today", "Boarding >2 Hours", "Needs EDD Review")
- Qventus: assistant names (Discharge Planning Assistant, Flow Priority Assistant, Care Gap Assistant, Case Manager Assistant, Capacity Intelligence Assistant); "system of action"; KLAS 92.5 rating citation
- Liaison Assist: task-platform framing ("tasks are the bedrock"); CIP (Cost Improvement Programme) positioning
- Vendor outcome claims: 15–30% excess-day reduction, 35% boarding reduction, 12hr LOS, 20,000 bed days, 91 min/shift — all marketing claims, none operational facts

## Rejected Findings

- "Patient Flow Management = bed management under another name" — rejected: Qventus holds the full flow core with no bed machinery; the bed layer is a bundle, not the definition.
- "AI/ML prediction is definitional" — rejected: Liaison Assist is a recognized NHS flow platform with no AI claims; prediction is the depth pole of L2.
- "Transfer center = the Type" — rejected: transfer coordination appears across samples as one intake component of the journey picture, not the center.
- "The Type requires task management" — rejected as definitional (LeanTaaS's insight-first pole manages flow through huddles/rounds without a task system on its pages); tasks are L1.

## Boundary Findings

1. **vs Bed & Capacity Management (JOINT REVIEW — pre-hung flag DISCHARGED from this side)**: keep-both RATIFIED on the object test, now corroborated from both sides. (a) Qventus: journey+discharge core with no bed layer → removal test passes toward flow; (b) Oracle Health "Patient Flow" (sibling evidence): bed-utilization/EVS features despite the name → removal test passes toward bed & capacity; (c) Liaison Assist: journey+tasks as the product's center with bed-state as one consumed surface; (d) TeleTracking straddles with both layers inside one suite. The market genuinely bundles both, and names products across the seam; the structural centers nevertheless differ (person-journey progression vs per-bed state/placement/capacity). Both documents record the seam; market-naming porousness documented, not silently resolved.
2. **vs Emergency Department Information System**: EDIS is the ED's own visit-scoped clinical/operational system of record (per that pass's research); flow is house-wide and episode-scoped. Meeting point: ED boarding appears in flow as an intake queue/metric; the admission decision + bed handoff is the handoff line (corroborated by EDIS research's "widen the geography → Patient Flow Management" test).
3. **vs Patient Scheduling**: scheduling pre-books future time slots; flow manages live, care-event-driven progression. No appointment book in any sampled product.
4. **vs Operating Room Management**: same live-coordination pattern over a different managed resource (ORs vs patients). Meeting point per ORM research: post-op destination planning; urgent surgical cases enter flow as demand.
5. **vs Hospital Management System / EHR**: the EHR documents care and produces ADT events; flow adds the operational progression layer on top ("system of action on top of your EHR" — Qventus; PAS/EPR integration — Liaison). HMS pass pre-hung this seam ("surface vs centered object"); ratified: in an HMS the bed board/queues are one surface; here the journey/progression is the centered object.
6. **vs Care Coordination Platform**: care coordination spans settings and the longitudinal care plan (clinical/social); flow is the operational progression of the acute episode inside the facility. Conceptual distinction; care-coordination leaf unprocessed — hedged accordingly.
7. **vs Clinical Communication Platform**: that pass's research records flow systems as an *event source* that communication platforms forward from; the centers differ (message exchange vs progression coordination).

## Uncertainties

- No Tier-1 operational documentation exists publicly for any sampled product; all evidence is Tier-2 solution-page level. No state vocabularies, thresholds, timers, or defaults are asserted anywhere.
- ED-specific and ambulatory flow products exist in the market but were not sampled; the EDIS boundary relies on that pass's research plus page-level evidence.
- Standalone transfer-center products (e.g., Central Logic) were not fetched; transfer coordination is treated as a bundled capability based on its appearance in three of four samples' materials.
- Vendor outcome metrics are unverified marketing claims and are never relied on in the final document.
- Qventus's absence of placement machinery is absence-on-page evidence, not a certified product boundary (suites evolve); assertion strength kept moderate.

## Historical / Market-Sample Check (§24)

- Paper-era lineage: the ward whiteboard + bed board carrying each patient's location, expected discharge date, and the daily discharge/huddle meeting where barriers are surfaced and actions assigned — satisfies all three L0 legs with no software, no AI, no EDD algorithms. Liaison Assist explicitly documents this lineage ("replace paper processes, whiteboards, and physical checks").
- UK NHS regional products (PAS-centric, site-team vocabulary) satisfy the definition; US "throughput" vocabulary satisfies it; the definition names neither.
- Non-AI flow management (Liaison) and insight-only flow management (iQueue pages) satisfy it; AI is held out of the core.
- The definition does not name beds, RTLS, transfer centers, staffing, or specific rituals — all variant/bundled machinery.

## Final Synthesis

A Patient Flow Management application is hospital operations software whose defining core is: the live tracked journey of each patient through the facility's acute episode (current position plus anticipated moves and discharge, with timing), the surfacing of stalled or at-risk progression (delays, barriers, boarding, overdue discharges) together with coordination of the corrective actions across the teams involved, and one shared house-wide operational picture the coordinating roles act from. Mature products extend this core with discharge-coordination machinery, admission/intake coordination, huddle/round/escalation support, throughput metrics, EHR/PAS integration, task layers, and handoff automation; variants add AI prediction depth, staffing alignment, transfer-center/command-center delivery, sensor automation, and — very commonly — the bed-state/placement layer of the sibling Bed & Capacity Management type, which is why the market's naming drifts across the seam. The type is person-journey-centric; the bed-centric sibling is resource-centric; both survive the removal tests in both directions.
