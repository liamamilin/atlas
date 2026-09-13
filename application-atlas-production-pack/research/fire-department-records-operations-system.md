# Research Notes — Fire Department Records / Operations System

Research date: 2026-09-07

## Research Goal

Understand what a Fire Department Records / Operations System (market label: **Fire RMS**) actually is: what objects it keeps as records, how the incident record is produced and reported, how the department's resources (personnel, apparatus, equipment) are maintained and connected to incidents, which operational modules are common vs. variant, and where its boundaries run against Computer-aided Dispatch (CAD), EMS Operations Platforms, and other public-safety record systems.

## Initial Boundary (hypothesis before research)

- Core use: fire departments keep official records of the incidents they respond to, their people, their apparatus/equipment, and related prevention/readiness work, and report standardized data to oversight bodies.
- Likely users: firefighters, company officers, chiefs, records/training administrators, fire-prevention staff.
- Nearest Types: Computer-aided Dispatch (real-time dispatch), EMS Operations Platform (clinical/ambulance side), Police Records Management System (law-enforcement records), Emergency Management Platform (multi-hazard EOC coordination).
- Unknowns: exact module structure; role of US NFIRS/NERIS standards; whether prevention (inspections/pre-plans) is core or variant; career vs volunteer differences; packaging (standalone vs suite vs state system).

## Research Questions

1. What is an incident record and how is it structured? What role do standardized reporting frameworks (NFIRS/NERIS, state variants) play?
2. What personnel records exist (roster, credentials, training) and how do they attach to incidents (staffing/attribution)?
3. What apparatus/equipment records exist and how do they connect to incidents and maintenance?
4. Which "operations" modules are common: scheduling, activities/duty logs, hydrants, property/occupancy, inspections/pre-plans, assets?
5. What integrations are typical (CAD, ePCR, billing, GIS/weather)?
6. How do the systems differ: standalone vs suite vs state-run; cloud vs local install; career vs volunteer vs industrial/military?
7. What are the boundary criteria vs CAD, EMS ePCR platforms, and Police RMS?
8. What is the minimal defining structure (L0) that survives the historical check (pre-NFIRS paper ledgers, non-US jurisdictions, industrial/military brigades)?

## Representative Products

Selection rationale: market representation + documentation quality + different product philosophies + different customer tiers + different generations of technology.

| Product | Vendor | Philosophy / tier |
|---|---|---|
| Firehouse Software / ESO Fire RMS | ESO | Desktop-heritage comprehensive RMS, large-department install base; now merged with ESO Fire cloud line |
| Emergency Reporting | ESO (acquired) | Cloud-first, incident-and-records reporting product for fire & EMS |
| ImageTrend Elite (Fire) | ImageTrend | Enterprise configurable platform; also runs state fire-marshal systems; AI-era features |
| First Due | First Due (Locality Media) | Cloud all-in-one suite ("your entire operation, one platform"), prevention-first, NERIS-transition leader |
| FirePrograms | FirePrograms (since 1981) | Privately owned heritage vendor; hosted or local PC/server; career, combination, volunteer, industrial, military departments |

Supplementary: ZOLL (EMS & Fire software suite page reviewed; docs too generic for product-structure claims — kept as market-context only).

## Sources

Official product pages (Tier 1/2):

- ESO — Fire Incidents: https://www.eso.com/fire/incidents-software/
- ESO — Records and Incident Reporting: https://www.eso.com/fire/records-incident-reporting/
- ESO — Scheduling and Personnel Management: https://www.eso.com/scheduling-personnel/
- ESO — Firehouse Software: https://www.firehousesoftware.com/
- ESO — Fire module index (nav): https://www.eso.com/fire/
- ImageTrend — Fire RMS Software: https://www.imagetrend.com/platform/fire-rms-software/
- ImageTrend — Platform (Pre-Incident/Incident/Post-Incident): https://www.imagetrend.com/platform/
- First Due — NERIS Fire Documentation Software: https://www.firstdue.com/products/neris
- First Due — product suite: https://www.firstdue.com/
- FirePrograms — home + modules: https://www.fireprograms.com/ , https://fireprograms.com/modules/incident-reporting/ (index on home page)
- ZOLL — EMS and Fire Software (context only): https://www.zoll.com/en-us/products/software-and-data/ems-and-fire-software

Source-access limitations:

- USFA/FEMA pages (usfa.fema.gov NFIRS/NERIS) returned 404 on two URL attempts on 2026-09-07; the USFA link was reached only through vendor references (FirePrograms' NERIS seal links to usfa.fema.gov/nfirs/neris). NERIS/NFIRS facts below are therefore **vendor-documented** claims about the USFA-run national standard, not directly observed on the government site.
- Deep help-center articles (per-field forms, exact workflows) were not fetched; product structure claims rest on official product/module pages. Per-field details (exact NFIRS modules, exact state submission mechanics) are intentionally not stated with precision.
- ZOLL suite pages were generic; no fire-RMS structure claims drawn from ZOLL.
- Evidence layers: **A** = directly observed on the cited vendor page; **B** = cross-product commonality across the sample.

## Product Observations

### ESO — Fire Incidents / ESO Fire RMS / Firehouse Software

Key observations (A unless noted):

- Positioning: "Your Complete Records Management Software"; "We've taken the best of FIREHOUSE Software and ESO Fire technology … to create ESO Fire RMS" — the market calls this category Fire RMS.
- Module lineup (Firehouse nav): Incidents, Properties & Inspections, Permits, EHR, Analytics, Scheduling, Activities, Asset Management, Hydrants, Checklists, Personnel Management, FireRescue1 Academy. Newer grouping: Records and Incident Reporting / Community Risk and Prevention / Fleet and Field Readiness / Scheduling and Personnel Management / Performance, Analytics, and Insights.
- Fire Incidents: "Enter data once, and ESO automatically creates NERIS and EHR reports"; "progressive validation sequence helps you build a NERIS report step by step. If there's an error, simply click to open the field that needs correction"; "We automatically create and submit NERIS-compliant reports" to the state; "exposure recording and critical incident documentation"; end-of-shift backlog framing.
- Records and Incident Reporting page: NERIS / EHR / Incidents / Hydrants as the reporting surface; "manage hydrants and equipment"; connected ecosystem (incident reports, maintenance schedules, EHR).
- Scheduling: "Fill shifts faster with staffing visibility across your entire team"; readiness begins before dispatch. Personnel Management: "Track training, credentials, and staff records in one place." Activities: "Document the daily operations and community work that happens between calls."
- Scale claim: "Trusted by 10,000+ agencies" (scheduling page banner).

### Emergency Reporting (ESO)

- The standalone site now presents "Fire and EMS Records and Reporting" and redirects into the ESO ecosystem (support via ESO; Canada site emergencyreporting.ca). Direct product-structure evidence post-acquisition is thin from the fetch; treated as cloud Fire & EMS records product now consolidated under ESO. No structural claims drawn beyond this.

### ImageTrend Elite (Fire)

- Definition in vendor's own words: "ImageTrend Elite Fire reporting software is a robust records management system (RMS) built to streamline fire incident reporting, inspections, training, and preplans."
- Platform staged Pre-Incident (Scheduling, Visual Pre Plans, License Management, Permits and Inspections, Community Health) → Incident (ePCR Incident Reporting, Fire Incident Reporting [NERIS], Fire-Based EMS Incident Reporting, Critical Care) → Post-Incident (Unified Analytics, CQI, Billing, Investigations "capture evidence and analyze fire causes").
- NERIS: "Meet NERIS standards with configurable forms and centralized data management"; NERIS V1 "Data Exchange Compatible" badge; NEMSIS v3.5.1 collect badge; FedRAMP; SOC 2. Fire pole: "Simplify NERIS reporting, optimize resource planning, and enhance firefighter safety."
- Configurability: drag-and-drop form editing, field reordering, default answers, controlled value ranges and validation settings for import/export, "Plus-One codes" for reporting categories; shared form/workflow "Library" contributed by other fire departments.
- Field use: "Complete building inspections or preplans offline with Elite Field Inspections … syncs automatically once an internet connection is available."
- Integrations: "Pull Incident Data from CAD — Automatically transfer location, timestamps, and resource details from your CAD system"; scheduling (native or third-party) "Track personnel availability, assign shifts, and manage equipment"; billing/cost-recovery reports from incident data.
- Security: HIPAA-compliant encryption, role-based permissions, automated backups.
- Market: "Fire agencies (direct entry)" + "State Marshal's fire systems" (ImageTrend powers state fire-marshal reporting systems); accreditation dashboards; AI-era: Unified Analytics, Intelligent Image Capture, AI Check (CQI).

### First Due

- Positioning: "AI Powered Fire and EMS RMS Software — Your entire operation. One platform"; "Consolidate NERIS, ePCR, fire prevention, pre-incident planning, scheduling & personnel management, asset & inventory, hydrants, training, community engagement, mobile response, and more into a single application."
- Product list: NERIS; ePCR; Pre-Incident Planning (mapping, any device); Hydrants (services and test, response, data management); Scheduling & Personnel; Events & Activities; Training & Learning Management (LMS, evaluations, certifications, compliance); Health & Wellness; Assets & Inventory (enhanced asset management, next-gen vehicle checks, work-order management — "real-time insight … on apparatus and equipment health, usage, and compliance—seamlessly linked to … scheduling and incident reporting"); Fire Prevention (next-gen inspections, permitting, invoicing, occupancies); ITM (AHJ portal + service-provider submissions for inspection/testing/maintenance compliance); Community Connect (resident/business household life-safety profiles); Fire Investigations; Mobile Responder (iOS/Android, "Notify & Respond", "CAD Agnostic", full platform access); Incident Command; Data & Analytics; Advanced Data Insights.
- NERIS module: "As of January 1st 2026, NERIS has gone live nationwide"; "With NFIRS sunsetting soon, every department must act"; built-in NERIS and state data validation on submission; configurable incident workflow per agency; automated exports "directly from the … platform to all compliance-focused agencies"; "NERIS EMS+" (track vitals, signatures, medications, procedures without NEMSIS submission); NFPA Annual Survey support; "1710 Reports — Assess your ability to meet and exceed the NFPA 1710 turnout time"; heat-mapping of response area; ad-hoc reporting.
- Integrations: CAD ("incident data and apparatus response times are automatically available"); property/occupancy data from pre-plan/prevention; automated weather API; staffing ("attach personnel to apparatus in your NFIRS form automatically" via First Due scheduling or third-party); IRWIN (wildland interagency data); billing partners (fire cost recovery).
- Markets: US fire, EMS, Federal (FedRAMP), State EMS (repository), Law Enforcement (scheduling/personnel only), Industrial Fire & Safety; **Canada variant** ("Fire Documentation" NFIRS-based product; provincial fire agencies) — cross-border evidence that the same Type is realized under a different national standard.

### FirePrograms

- Since 1981 (44 years); "career, combination, volunteer, industrial, and military fire departments"; "Unlimited Stations · Unlimited Logins · Unlimited Users"; hosted **and** local PC/server versions ("Best of Both Worlds – Synchronized Web Browser and Desktop applications").
- Module suite: NERIS Incident Reporting ("Fastest incident report entry time … Smart Forms and Lookups — Never hunt for code again"); SceneConnect web portal ("Rapidly access and enter incidents over the web anywhere, anytime" — phone/tablet); Staffing and Scheduling ("manage Full-Time, Part-Time, On-Call, and Volunteer schedules with time tracking"; shift trades, vacation/sick requests with email/text confirmation; shift-based Status and Assignment Boards per station/apparatus/personnel group; personal work schedule online); Training; Personnel ("comprehensive Personnel Module automatically updates personnel records with critical information"); Assets + Asset Maintenance ("track and schedule department-wide cleaning, inspection, testing, repair and maintenance"); Hydrants ("Powerful hydrant analysis and integrated mapping"); CommandView Calendar ("hub for all agency activity"); Department Log ("Eliminate paper and effectively manage daily operations information"); Data Browsers ("rapidly analyze bulk records"); System Reporting (scheduled reports, on-the-fly filters); Interfaces and APIs; embedded operational videos.
- NERIS rollout: December 2025 "NERIS compliant reporting NATIONWIDE"; September 1, 2026: "Over 135,000 NERIS records uploaded from our customers"; NERIS "Data Exchange Compatible" seal linking to USFA.

### ZOLL (context only)

- Sells an EMS & fire software suite (via ZOLL Data Systems) covering "clinical, operational, and financial" needs; fetched pages too generic for structure claims. Confirms the market segment exists beyond the four main samples.

## Cross-product Comparison

| Structure / capability | ESO–Firehouse | ImageTrend | First Due | FirePrograms | Layer |
|---|---|---|---|---|---|
| Incident record as central object, entered by crews/officers | A (Incidents) | A (Fire RMS = "incident reporting…") | A (NERIS) | A (NERIS Incident Reporting) | Core |
| Standardized national reporting (NFIRS/NERIS) + validation | A (auto NERIS, progressive validation, auto submit) | A (NERIS forms, Data-Exchange badge) | A (NERIS validation, automated exports; NFIRS transition documented) | A (NERIS reporting, Data-Exchange seal) | Core→Common (US realization of "standardized reporting") |
| Response attribution: units + personnel on the incident | A (auto NERIS+personnel; FH staffing) | B (CAD transfers "resource details") | A (attach personnel to apparatus in the form) | A (staffing integrated with incident reporting) | Core |
| Personnel records (roster, credentials, training) | A (Personnel Management: training/credentials/records) | A (License Management; scheduling tracks certifications) | A (Training LMS, certifications) | A (Personnel module) | Core/Common |
| Scheduling / staffing / availability | A | A | A | A | Common |
| Apparatus & equipment assets + checks/maintenance | A (Asset Management, Fleet & Field Readiness, Checklists) | B (manage equipment via scheduling; pre/post modules) | A (Assets & Inventory, vehicle checks, work orders) | A (Assets, Asset Maintenance) | Common (near-core for "Operations") |
| Property / occupancy records + pre-incident plans | A (Properties & Inspections) | A (Visual Pre Plans) | A (Pre-Incident Planning, occupancies) | A (Protected Property Data) | Common |
| Inspections & permits (prevention) | A (Properties & Inspections, Permits) | A (Permits and Inspections) | A (Fire Prevention, ITM) | B (via Protected Property; not explicit) | Common |
| Hydrant records/testing | A (Hydrants) | B (ecosystem page) | A (Hydrants module) | A (Hydrants module) | Common |
| Training records / LMS | A (Personnel training; Academy) | A ("…training" in RMS scope) | A (Training & LMS) | A (Training module) | Common |
| Daily activity / duty log (between-call work) | A (Activities) | B | A (Events & Activities) | A (Department Log, CommandView Calendar) | Common |
| Reporting & analytics (response times, NFPA 1710/surveys, dashboards) | A (Analytics/Insights) | A (Unified Analytics, accreditation dashboards) | A (NFPA 1710 reports, NFPA survey, heat maps) | A (System Reporting, Data Browsers) | Common |
| CAD integration (import dispatch/incident data) | B (connected ecosystem; EMS dispatch product) | A ("Pull Incident Data from CAD") | A (CAD integration; CAD-agnostic mobile) | A (Interfaces and APIs) | Common |
| ePCR / EMS adjacency | A (EHR product; EMS line) | A (ePCR, Fire-Based EMS reporting) | A (ePCR, NERIS EMS+) | B (not listed) | Common (variant when dept runs EMS) |
| Mobile / field entry incl. offline | A (crew reporting framing) | A (Elite Field Inspections offline sync) | A (Mobile Responder, any device) | A (SceneConnect web/phone/tablet) | Common |
| Roles / permissions / security | B (enterprise SSO-era ecosystem) | A (role-based permissions, encryption, backups) | A (enterprise config) | B | Common |
| Deployment: cloud vs hosted vs local PC/server | A (FH desktop heritage → ESO cloud) | A (cloud; state systems) | A (cloud; FedRAMP federal) | A (hosted + local) | Variant |
| Department types served (career/volunteer/industrial/military) | B | B | A (fire/EMS/federal/industrial/Canada) | A (explicit) | Variant |
| Community engagement (resident profiles) | — | — | A (Community Connect) | — | Vendor-specific (L3) |
| State-level repository systems for fire marshals | — | A | (State EMS = EMS side) | — | Vendor-specific (L3) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

The smallest structure without which the product is no longer recognizable as this Type:

1. **The incident response record** — one durable, dated record per emergency response the department makes: what happened, where, when, classified by response type, written up by the department itself.
2. **Response attribution to the department's own resources** — the incident record names the apparatus (units) and personnel that responded, connecting it to standing records of those resources.
3. **The fire service organization as system of record** — all of this is kept as the official, durable record of one fire service organization (career, volunteer, combination, industrial, or military), not as ephemeral dispatch traffic.

Tests:

- Remove the incident record → asset/personnel tracking software, not a fire RMS.
- Remove unit/personnel attribution → an anonymous event log; the NFIRS/NERIS-era structure (apparatus/personnel on the report) and every sampled product contradict this.
- Remove the department-of-record role → a dispatch feed or analytics dashboard, not a records system.

Historical check (older / regional / platform-native): a pre-NFIRS fire department keeping a handwritten run log with unit and crew attribution, plus roster and apparatus binders, satisfies all three invariants without NERIS, cloud, scheduling software, or inspection modules. Industrial brigades and non-US departments satisfy it without the US standard. The L0 therefore does not include NERIS/NFIRS, scheduling, inspections, hydrants, or analytics.

### L1 — Common Mature Structure (common, not defining)

- Standardized incident reporting: jurisdiction-standard coding with field validation and automated export/submit to the oversight body (NERIS in the US, per-state variants, Canada's NFIRS-based variant in the sample).
- Personnel administration: roster, roles/rank, certifications/credentials with expiry awareness, training records.
- Scheduling / staffing: shifts, availability, trades/leave; volunteer on-call handling.
- Apparatus & equipment records: assets, daily/periodic checks, maintenance and testing schedules.
- Property / occupancy records and pre-incident plans; hydrant records and testing; inspection/permit (prevention) records.
- Daily activity/duty logging for between-call work.
- Reporting/analytics: response-time measures (e.g. NFPA 1710-style), annual surveys, dashboards, ad-hoc reports.
- Integrations: CAD import (location, timestamps, resources), ePCR linkage where the department runs EMS, billing/cost-recovery handoff, weather/GIS context.
- Mobile/field entry (including offline capture) and role-based access.

### L2 — Variant / Optional Structure

- Packaging: standalone incident-reporting tool → full RMS → all-in-one suite (records+prevention+community) → module of a state-run repository system.
- Deployment: cloud SaaS vs hosted vs local desktop/server (heritage vendors still ship local installs).
- Standard regime: US NERIS/NFIRS; Canada NFIRS-based; (other national regimes exist outside the sample).
- Department type: career vs volunteer vs combination vs industrial/military — changes the weight of scheduling/availability vs response analytics.
- Fire-only vs fire+EMS combined (determines ePCR/NEMSIS adjacency).
- Breadth add-ons: community engagement, responder health & wellness, incident command, investigations, quality programs, AI assistance.

### L3 — Vendor-specific (kept out of the final document)

- First Due: Community Connect (resident life-safety profiles), ITM (AHJ–service-provider compliance portal), Health & Wellness, Incident Command, "NERIS EMS+".
- ImageTrend: state fire-marshal repository systems, shared form Library, AI image capture / AI Check CQI, CQI/Billing modules, "Plus-One codes" form concept.
- FirePrograms: SceneConnect portal, CommandView Calendar, Data Browsers, local-install option, unlimited-station licensing.
- ESO: NarcBox, FireRescue1 Academy, D2i analytics acquisition; Firehouse desktop heritage.
- ZOLL: suite positioning only (no structure claims).

## Vendor-specific Findings

See L3 above. None of these were promoted into the canonical model.

## Boundary Findings

- **vs Computer-aided Dispatch / CAD**: CAD owns the real-time call-taking and dispatch event; its output is live operational traffic. The Fire RMS receives dispatch/incident data from CAD after the fact (ImageTrend: "Pull Incident Data from CAD — transfer location, timestamps, and resource details"; First Due: CAD integration with "incident data and apparatus response times"; First Due Mobile Responder "CAD Agnostic") and turns it into the permanent record. Remove the permanent-record side and you have CAD; remove real-time dispatching from this Type and it still stands. Several vendors ship both as separate products (ESO Dispatch is an EMS product line; ImageTrend lists ePCR/CAD-class tools separately) — supporting separation.
- **vs EMS Operations Platform / ePCR**: the EMS side documents the patient encounter under clinical standards (NEMSIS) and drives billing; the fire RMS documents the department's response. Fire-based EMS departments commonly run both; First Due's "NERIS EMS+" exists precisely to record medical data inside the fire report *without* NEMSIS submission — evidence the two records are distinct objects. Scheduling/personnel tools are often shared across both lines (ESO, First Due) — a shared-utility overlap, not Type identity.
- **vs Police Records Management System**: law-enforcement records (cases, arrests, evidence) follow different domain semantics and standards (NIBRS-class, not NERIS-class). Same "agency records" family, different Type.
- **vs Emergency Management Platform**: multi-hazard planning/EOC coordination for large-scale emergencies vs this Type's day-to-day single-department recordkeeping.
- **vs standalone Fire Prevention / inspection software**: inspections/permits/ITM are common modules here (ESO Properties & Inspections, ImageTrend Permits and Inspections, First Due Fire Prevention/ITM), and prevention-first suites exist; but removing prevention leaves the Type intact (FirePrograms sells the response record as the anchor), while removing the response record leaves only a prevention tool — a different (adjacent) Type.
- **vs Enterprise Asset Management**: apparatus/equipment records here are scoped to department readiness (checks, testing, maintenance) and integrated with incidents/scheduling; not the general-fleet depth of EAM.
- **Leaf-name note**: the directory leaf "Fire Department Records / Operations System" matches the market label "Fire RMS" (ImageTrend: "robust records management system (RMS) built to streamline fire incident reporting, inspections, training, and preplans"). The "Operations" half is realized as the personnel/scheduling/assets/activities modules. No taxonomy conflict found; CAD and EMS Operations Platform remain separate leaves and are shipped as separate products by the sampled vendors.

## Uncertainties

- Exact field-level structure of NERIS/NFIRS reports (module lists, required fields) not directly verified — USFA pages unreachable; vendor pages describe behavior (validation, auto-submit, apparatus/personnel attachment) but not field lists. No precise claims made in the final document.
- Per-product pricing, deployment quotas, exact integration catalogs (API lists) not researched.
- ImageTrend hydrant support inferred from the ecosystem page (B-level) rather than a dedicated module page.
- Non-North-American regimes (UK/EU/Asia national fire data standards) not researched; the final document keeps the standard regime as a variant ("jurisdiction-specific national standard") rather than naming NERIS as universal.
- Emergency Reporting's standalone product structure could not be observed post-acquisition; it contributes market-presence evidence only.
- Whether "inspections/permits" should eventually be split as its own Type (standalone prevention products exist) is a directory-level question; this pass records the flag without restructuring.

## Final Synthesis

A Fire Department Records / Operations System is the fire service organization's own system of record. Its center of gravity is the **incident response record** — a durable, dated, classified record of each response, attributed to the apparatus and personnel that responded — maintained alongside the **standing records of those resources** (personnel with credentials/training, apparatus/equipment with checks and maintenance) under the authority of **one fire service organization**, which reports standardized data upward where oversight regimes exist. Around this center, mature products add the operational apparatus of a department: scheduling/staffing, property and hydrant records, pre-incident plans, inspections/permits, duty/activity logs, analytics, and integrations to CAD and (for fire-based EMS) ePCR. The US market realization is strongly shaped by the NFIRS→NERIS national reporting standard, but the Type itself is older and wider than that standard — paper ledgers, Canadian NFIRS-based products, and industrial/military brigades all satisfy the defining structure.
