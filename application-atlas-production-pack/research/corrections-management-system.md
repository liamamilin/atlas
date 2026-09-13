# Research Notes — Corrections Management System

Research date: 2026-09-07
Slug: corrections-management-system
Directory leaf: Corrections Management System (§24 Government, Public Sector & Civic)

---

## Research Goal

Understand what a Corrections Management System actually is as an Application Type: what objects exist inside it, who operates it, how custody work flows through it, which states and rules govern it, and where its boundaries sit against neighboring justice-sector Types (police RMS, court case management, probation & parole, evidence management, generic public-sector case management).

## Initial Boundary (working hypothesis before research)

- Hypothesis: software used by correctional agencies (jails, prisons, detention centers, departments of corrections) to manage the full custody lifecycle of incarcerated persons: intake/booking, identification, classification, housing, movement, counts, programs, discipline, visits, property, medical linkage, release.
- Likely confusion points:
  - Police Records Management System (arrest records exist before booking)
  - Court Case Management System (court events are tracked, not adjudicated, inside corrections software)
  - Probation & Parole Management (community supervision vs institutional custody)
  - Evidence Management System (inmate property vs case evidence)
  - Inmate communications vendors (phones/tablets — adjacent services, not the management core)
- Naming hypothesis: the market uses "Jail Management System (JMS)", "Offender Management System (OMS)", "Inmate Tracking System", and "Corrections Management System" near-interchangeably; scope differs (county jail vs state DOC incl. community supervision).

## Research Questions

1. What is the central object — the incarcerated person record? What is it called?
2. What is a booking/custody episode and how does it relate to the person record (multiple bookings per person)?
3. How do charges, warrants, and court commitments attach to the custody episode?
4. How does classification work (risk/needs assessment → custody level → placement)?
5. How does the housing/bed model work (facility → unit → cell → bed)?
6. How do movements and counts work (scheduled/unscheduled movement, headcounts, cellchecks, reconciliation)?
7. Which subsystems exist: incidents, discipline, visits, property, programs/jobs/education, grievances, investigations, funds/commissary, medical, court events, sentence calculation, release?
8. What interfaces do officers and staff actually use (booking station, housing board, mobile/handheld, dashboards, kiosks)?
9. What rules matter (custody-level restrictions, count reconciliation, movement authorization, audit trails, CJIS security)?
10. What exceptions matter (escapes, deaths in custody, use of force, transfers, out-of-jurisdiction holds/detainers)?
11. Where is medical/mental health handled — inside the system or as an integration seam?
12. How does the Type relate to community supervision (probation/parole) in DOC-enterprise deployments?
13. Is "Jail Management System" a separate Type or a scope variant / synonym?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Vendor | Pole | Customer tier |
|---|---|---|---|
| JailTracker | Colossus, Incorporated (Global / Harris Computer family) | jail-focused corrections specialist (JMS/OMS) | county jails & regional facilities; 230+ facilities, 29 US states (vendor claim) |
| CentralSquare Jail | CentralSquare Technologies | module of a public-safety suite (CAD/RMS/Jail) | county sheriff offices / local government |
| CORIS OMS | Abilis Solutions | enterprise DOC-wide offender management (custody + probation + parole) | state/provincial/national corrections agencies; US, Canada, Australia; 400+ prisons & community offices (vendor claim) |
| ViaPath OMS (SAFESuite) | ViaPath Technologies (ex-GTL) | corrections-specialist with inmate-communications heritage; OMS is one pillar of a six-pillar suite | state DOCs and large facilities; 2,000+ facilities served (vendor claim) |

Rejected/abandoned samples (with reasons):
- Motorola Spillman Flex (jail module) — product URL 404 ×2, abandoned per network rules.
- Tyler Technologies (public-safety/corrections) — site returned 403, abandoned.
- Cybersoft Technologies (CorTrak) — transport error; cybersoft.com is an unrelated security vendor.
- Cody Systems, Corrections Software Solutions — timeout/transport errors, abandoned.
- Corrections Technology Association (industry functional standards referenced by Abilis) — transport error, abandoned.

## Sources

All fetched 2026-09-07. All successful sources are official vendor product pages (Tier 2). No Tier-1 help-center / user-guide / operational documentation was reachable for any sampled product — this market sells to government agencies and publishes almost no public operational documentation.

- JailTracker — https://jailtracker.com/ (home), https://jailtracker.com/solutions/ (solution detail), https://jailtracker.com/about/ (company)
- CentralSquare — https://www.centralsquare.com/solutions/public-safety-software/jail-information-management-system (Jail product page), https://www.centralsquare.com/solutions (suite index), https://www.centralsquare.com/public-safety/ (public safety index)
- Abilis Solutions — https://abilis-solutions.com/ (home), https://abilis-solutions.com/oms-solutions/ (CORIS functional framework)
- ViaPath — https://www.viapath.com/ (home), https://www.viapath.com/facilities/ (six pillars), https://www.viapath.com/facilities/facility-operations-management/ (OMS / SAFESuite)

Source-access limitation: because only marketing/product pages were reachable, precise operational details (exact count frequencies, exact classification instruments, exact permission models, exact state names) are NOT asserted anywhere. All claims below are calibrated to product-page-level evidence. Numeric figures quoted by vendors (e.g., "230+ facilities", "600 reports", "45→15 minutes booking") are vendor claims, recorded here as claims, not used as structural evidence in the final document.

---

## Product Observations

### JailTracker (Colossus / Global / Harris Computer)

Evidence layer: A (direct observation of official product pages).

- Self-describes with three near-synonymous terms on one site: "jail management system", "offender management system", "inmate tracking system" — direct evidence that the market treats these as one product category. [A]
- Positioning: "specialized information software solutions for the corrections community"; "Jail management is all we do"; roots in Kentucky 20+ years; staff come from corrections backgrounds. [A]
- Operational functions named on the solutions page:
  - "logging daily tasks like head counts, rounds, activities and incidents, and accounting" [A]
  - "scheduling, classifications and assessments, incident reports, and arrest charges" (automated tasks) [A]
  - "Greaseboard": "JailTracker makes your Greaseboard virtual… filter by category or block, move an inmate, directly access and update records" — the virtual housing board; "Greaseboard" is the pre-digital whiteboard artifact of jail operations. [A]
  - mobile app: "gets records started in real-time… complete tasks on-scene with no redundancy"; "mobile capabilities run within the software" [A]
  - configurable dashboards for "facility-wide awareness"; color coding; instantaneous updates [A]
  - 600 customizable reports out of the box + custom report/form builder (vendor figure) [A]
  - required fields and automatic alerts to force complete records ("crucial component of liability management") [A]
  - granular permissions "for groups or even individuals" [A]
  - automated notifications via email, SMS, or internal messaging; scheduled report delivery to printer [A]
  - medical queue example: "Should an inmate be added to a medical queue based on their response to a questionnaire?" — medical appears as a queue/alert target, not a core module. [A]
  - court services example: "Need to let Court Services know that an inmate's incarceration status has changed?" — status notification outward to courts. [A]
- Deployment: on-premise or hosted on Azure Gov "meeting the required CJIS standards". [A]
- Integrations: "over 100 existing integrations" (vendor figure), configurable per agency. [A]
- Incident reports have a supervisor approval flow ("newly created incident report pending approval"). [A]

### CentralSquare Jail (Public Safety Suite module)

Evidence layer: A (direct observation of official product pages).

- Product name: "Jail Management System" (JMS); part of the Public Safety Suite alongside CAD, Records (RMS), NG911 — the suite-module pole. [A]
- Headline value: "Drop your booking time from 45 minutes to 15 minutes per inmate… through an automated intake process" (vendor claim). [A]
- "Automate inmate intake and classification… Improve your processes for classifying and placing every inmate." [A]
- "Your facility staff make more efficient and safer decisions with access to arrests data, warrants and prior incidents" — reads from the RMS side of the suite at booking. [A]
- Explicit feature list ("Track Everything Inside Your JMS"):
  - **Inmate Movements** — "Logs all inmate transfers, housing changes, and movement within or outside the facility." [A]
  - **Headcounts & Cellchecks** — "Ensures inmate accountability and safety through scheduled checks and population counts." [A]
  - **Shift Notes & Incident Reports** — "Captures staff observations, daily activity logs, and documentation of any incidents." [A]
  - **Court Events & Sentence Calculations** — "Tracks inmate court appearances and manages sentence details, including time served and release dates." [A]
  - **Inmate Work & Transportation** — "Manages inmate job assignments and coordinates transportation for work or external appointments." [A]
- "Keep Compliant With Built-in Reporting… Spend less time compiling data for government mandated reports." [A]
- Customer story framing: "Track Inmates From Booking to Release" — booking, classifications, repeat offenders, reports, audits, inmate movements. [A]
- The suite sells RMS and Jail as separate products — direct evidence of the RMS/JMS seam being policed by the vendor itself. [A]

### Abilis CORIS OMS

Evidence layer: A (direct observation of official product pages).

- Positioning: "purpose-built, commercial-off-the-shelf (COTS) solution for managing offender information… enterprise-wide use… officers, administrators, and staff across all operational divisions." [A]
- Scope: "more than 40 modules to address the full breadth of operational requirements across custody, probation, and parole business processes" — the DOC-enterprise pole covering institutional AND community supervision. [A]
- Standards basis: modules "based on defined standards from the Corrections Technology Association" (industry association; CTA site itself unreachable). [A]
- Functional domains (directly listed):
  - **Offender Management**: Offender Profile, Case Management, Classification, Jobs, Programs, Education — "accuracy and integrity of all offender-specific information, including identity, risks, and rehabilitative criteria and plans." [A]
  - **Facility Management**: Population Counts, Housing, Property, Discipline, Incidents, Investigations, Grievances, Visitation — "safe, secure and efficient management of offenders in secure environments." [A]
  - **Sentence Management**: Pre-sentencing Investigation, Sentencing & Calculation, Parole Board, Release Authorization — "rules-driven management of offender sentence and parole processes, custom-designed to satisfy individual jurisdictional requirements." [A]
  - **Financials**: Commissary Fund, Community Fees, Payroll, Restitution, Trust — "GAAP-compliant… banking and trust requirements for prison-based and community-based offenders." [A]
  - **Public Safety**: Fugitive, Victims, Most Wanted — "secure integration and data-sharing with key stakeholders across the justice and public safety spectrum." [A]
  - **Reporting & BI**: pre-built operational reports, ad-hoc reporting, analytics, dashboards; secure data warehouse; 250+ preformatted reports (vendor figure); example dashboards for Visitation, Incident, Grievance analytics. [A]
  - **Application Management**: Administration, User Rights & Provisioning, Configuration, Documents, Auditing, Workflow, Notifications. [A]
- Notably ABSENT from the 40-module framework: medical/mental health as a domain — health is not listed among the functional domains. [A]
- Implementation reality: go-live within 27–36 months (vendor claim) — evidence that DOC OMS replacement is a multi-year modernization program. [A]
- International footprint: agencies in US, Canada, Australia; "400+ Prisons & Community Offices"; case studies for Virginia DOC, Idaho DOC, Australian Capital Territory. [A]
- Cloud: optimized for Microsoft Azure; thousands of concurrent users; 99.95% uptime target (vendor claim). [A]

### ViaPath OMS (SAFESuite)

Evidence layer: A (direct observation of official product pages).

- Positioning: corrections-specialist suite with six pillars: Intelligence & Facility Security, Connected Communications, Enhanced Telehealth, Facility Operations & Management, Financial Services, Education/Reentry. [A]
- The OMS lives under "Facility Operations & Management": "Our ViaPath Offender Management System (OMS) eliminates manual processes and data fragmentation. By automating reporting, centralizing records, and aligning workflows with facility policies…" [A]
- "30+ years providing OMS solutions, 2,000+ facilities served, 1M+ global users" (vendor claims; heritage as GTL, the inmate-communications vendor). [A]
- The OMS is one pillar among six; communications (phones, tablets, video visitation, digital mail), telehealth, and financial services are sold as separate pillars — evidence that communications/health/money are adjacent service layers around the management core. [A]
- Compliance posture: SOC 2, CJIS, ADA, HIPAA, PCI-DSS; NIST 800-53, ISO 27001 (vendor claims). [A]
- Customer quote: "35 percent drop in disciplinary actions" — discipline exists as a managed domain in the market. [A-quote]

---

## Cross-product Comparison

| Dimension | JailTracker | CentralSquare Jail | Abilis CORIS | ViaPath OMS | Evidence |
|---|---|---|---|---|---|
| Person record (inmate/offender) | yes ("inmate") | yes ("inmate") | yes ("offender") | yes ("incarcerated individuals") | B |
| Booking / intake | intake, arrest charges | automated intake/booking | (implied in offender profile/case mgmt) | (centralizing records) | B |
| Classification & assessment | classifications and assessments | intake + classification | Classification module | — | B |
| Housing placement | Greaseboard (virtual housing board), move inmate, filter by block | housing changes logged | Housing module | — | B |
| Movements | move inmate; mobile on-scene | Inmate Movements (transfers, housing changes, in/out of facility) | (implied) | — | B |
| Counts / accountability | head counts, rounds | Headcounts & Cellchecks | Population Counts | — | B |
| Incidents | incident reports w/ supervisor approval | Shift Notes & Incident Reports | Incidents + Investigations | — | B |
| Discipline | (not explicit) | (not explicit) | Discipline module | customer quote references disciplinary actions | B- (one direct anchor) |
| Court events / sentence calc | incarceration-status change to Court Services | Court Events & Sentence Calculations (time served, release dates) | Sentence Management domain (sentencing & calculation, parole board, release authorization) | — | B |
| Programs / jobs / education | activities | Inmate Work & Transportation | Jobs, Programs, Education | Education/Reentry pillar | B |
| Visitation | (not explicit) | (not explicit) | Visitation module | video visitation as separate comms pillar | B- |
| Property | (not explicit) | (not explicit) | Property module | — | B- (single anchor) |
| Grievances | (not explicit) | (not explicit) | Grievances module + analytics dashboard | — | B- (single anchor) |
| Funds / commissary / trust | accounting (daily tasks) | (not explicit) | Financials domain (commissary, trust, payroll, restitution) | Financial Services pillar | B |
| Medical / health | medical queue via alert | (not explicit) | ABSENT from framework | separate Telehealth pillar | B- (absence pattern: integration seam) |
| Reporting / BI | 600 reports + builder + dashboards | mandated government reports | BI platform, 250+ reports, dashboards | automated reporting | B |
| Alerts / workflow automation | automated alerts, notifications (email/SMS/internal) | (implied) | Workflow, Notifications modules | automated business workflows | B |
| Permissions / audit | granular per-user permissions | audits (customer story) | User Rights & Provisioning, Auditing | audit controls | B |
| Mobile | mobile app, same interface | (not explicit) | (not explicit) | (not explicit) | B- (single anchor) |
| CJIS posture | CJIS standards (Azure Gov) | CJIS Security Policy published | (not explicit) | CJIS listed | B |
| Deployment | on-prem or Azure Gov hosted | cloud suite (AWS) | Azure cloud, on-prem heritage | secure platform | B |
| Scope | jail-focused | jail-focused | custody + probation + parole (DOC-wide) | facility-focused suite | B |
| Packaging | standalone JMS/OMS | suite module | enterprise COTS OMS | suite pillar | B |

## Canonical Model (working abstraction)

```text
Person in custody (identified individual under the agency's legal authority)
└── Custody episode (booking/admission → release/transfer/discharge; grounded in
    charges/court commitment/sentence; one person, many episodes over time)
    ├── Legal basis (charges, warrants, holds, court commitments, sentence)
    ├── Classification (risk/needs assessment → custody level → restrictions)
    ├── Housing placement (facility → unit → cell/bed; changes over the episode)
    ├── Movement record (every location change, in or out of the facility)
    └── Accountability loop (scheduled counts/cellchecks reconciling persons to places)
```

## Abstraction Hierarchy

### L0 — Defining Invariant

Smallest structure without which the software stops being a corrections management system:

1. **Person-in-custody record** — an identified individual held by a correctional agency (inmate / offender / resident / detainee — the label varies; the record does not).
2. **Custody episode** — a bounded period of lawful custody for that person (booking/admission → release, transfer, or discharge), carrying the legal basis (charges, court commitment, sentence, hold).
3. **Housing placement** — the person is located in the facility's physical structure (unit/cell/bed) at any moment.
4. **Movement & accountability record** — location changes are recorded, and periodic counts/cellchecks reconcile the person population against housing locations.

Test: remove the person record → not a custody system. Remove the custody episode → a police contact database (RMS). Remove housing placement → a registry, not facility operations. Remove movement/count accountability → a census database, not custody management. All four are needed.

Historical check (§24): the pre-digital baseline — booking ledgers, the greaseboard (housing whiteboard), count sheets, movement logs — contains exactly these four structures. JailTracker's own copy ("makes your Greaseboard virtual") documents the continuity directly. Older, regional, and non-US systems (paper-era county jails, UK/Canadian/Australian prison systems) satisfy the same four invariants without any modern module (BI, mobile, kiosks, integrations). The definition therefore does not over-fit to the current US market.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature implementations but not definitional:

- classification & assessment (risk/needs → custody level → placement rules)
- incident reporting (with supervisor review/approval in some products) and investigations
- discipline/infractions machinery
- court-event tracking and sentence/release calculation (time served, release dates)
- programs, jobs/work assignments, education
- visitation management
- inmate property tracking
- grievances
- inmate funds: commissary, trust accounts, payroll for work assignments, restitution
- mandated/statistical reporting + operational reports + dashboards/BI
- alerts, notifications, workflow automation
- role-based permissions, audit trails, document management
- mobile/handheld officer use
- integrations: CAD/RMS (arrest data at booking), courts, medical, communications vendors, state/federal systems
- CJIS-aligned security posture

### L2 — Variant / Optional Structure

Depends on segment, jurisdiction, scale, deployment:

- scope: county jail (pretrial-heavy, high turnover) vs prison (sentenced, long-stay) vs DOC-enterprise (custody + probation + parole in one system)
- sentence management depth: parole board, pre-sentence investigation, release authorization (sentenced populations; DOC pole)
- public-safety extensions: fugitive, victims, most-wanted (one product)
- financial depth: GAAP-compliant trust/banking vs simple commissary
- medical posture: external correctional EHR integration vs telehealth service pillar vs simple medical queues/alerts
- communications posture: integrated inmate communications (phones/tablets/video) as suite pillars vs pure management core
- deployment: on-premise vs government-cloud (Azure Gov / AWS); CJIS hosting requirements
- packaging: standalone JMS vs public-safety-suite module vs enterprise OMS platform
- terminology: inmate / offender / resident / detainee / incarcerated individual
- regional: US county/state structure vs Canadian provincial vs Australian territory systems

### L3 — Vendor-specific Structure

(kept out of the final document; recorded here as examples)

- JailTracker: "Greaseboard" as the virtual housing board; 600 out-of-box reports; 100+ integrations; Azure Gov hosting; corrections-background support team; Harris Computer family membership.
- CentralSquare: "Jail" product within Public Safety Suite; 45→15-minute booking claim; Jail Pro overview sheet; Morgan County AL customer story; suite siblings (CAD, RMS, NG911, Unify).
- Abilis: CORIS® brand; 40+ modules; CTA-standards basis; Agilis delivery framework; 3 releases/year on 4-month cadence; 250+ preformatted reports; 27–36-month go-live; 99.95% uptime; CORIS Community user conference; CORIS Academy certifications; Virginia/Idaho/ACT case studies.
- ViaPath: SAFESuite™; six-pillar architecture; Call IQ / Data IQ / Voice IQ analytics; ex-GTL heritage; 2,000+ facilities / 1M+ users claims; 51M free learning hours claim.

## Vendor-specific Findings

See L3 above. Additionally:

- Only Abilis documents an industry-standards basis (Corrections Technology Association); the association's own site was unreachable, so the standards' content could not be verified.
- Only JailTracker documents the pre-digital artifact continuity ("Greaseboard").
- Only CentralSquare documents the RMS→Jail data flow at booking ("access to arrests data, warrants and prior incidents") — the suite-module advantage.
- Only ViaPath frames the OMS as one pillar of a communications-led suite.

## Rejected Findings

- "Corrections management = inmate communications" — rejected: communications pillars exist (ViaPath) but the management core (person/episode/housing/movement/count) is present in every product regardless of communications offering.
- "Medical is a core OMS module" — rejected on evidence: Abilis's 40-module framework omits medical; ViaPath sells telehealth as a separate pillar; JailTracker surfaces medical only as an alert/queue target. Medical is an integration seam (correctional EHR is its own market).
- "Jail Management System is a separate Type from Corrections Management System" — rejected: JailTracker alone self-describes as JMS, OMS, and inmate tracking system; the difference is scope (jail vs DOC-wide), not structure.
- "Community supervision (probation/parole) is part of the defining core" — rejected: only the DOC-enterprise pole (Abilis) includes it; jail-focused products do not. It is a scope variant.
- Precise operational numbers (count frequencies, booking minutes, report counts, uptime percentages) — rejected for the final document: vendor claims only, no operational documentation to verify.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (what to remove/keep) |
|---|---|---|
| Police Records Management System | upstream adjacent | RMS records police events (arrests, reports, cases) about people who may never be booked; the corrections system starts at lawful custody (booking) and manages the person while held. CentralSquare sells RMS and Jail as separate products — the vendor polices the seam. Remove the custody episode/housing/count machinery and add field-based report/case workflows → you get an RMS. |
| Court Case Management System | adjacent (downstream + upstream) | The corrections system tracks court events (appearances, commitments) and receives commitments; it does not manage dockets, filings, or judicial workflow. Remove custody operations and keep case/docket processing → court CMS. |
| Probation & Parole Management | sibling (community supervision) | Community supervision manages people living in the community under conditions; corrections management manages people held in facilities. They share the offender/person record concept and case machinery but differ in the custody/housing/count core. DOC-enterprise OMS (Abilis) spans both — a scope variant, not proof of one Type. |
| Evidence Management System | adjacent | Inmate property is personal property held during custody (wallet, clothing, medication) and returned at release; evidence management is chain-of-custody for case evidence. Different object, different rules. |
| Public Sector Case Management | generic parent | Generic case management lacks the physical custody structures (housing, counts, movements) and the 24/7 operational accountability loop. |
| Inmate Communications platforms (phones/tablets/video) | service-layer adjacent | Communications vendors sell services to facilities; the OMS is the management system of record. ViaPath sells both — as separate pillars. |
| Correctional EHR / medical | integration seam | Health records for incarcerated persons are typically a separate system integrated with the OMS (scheduling, queues, alerts). |
| Jail kiosk / inmate self-service tablets | device layer | Kiosks/tablets are surfaces onto the OMS (or communications platforms), not the Type itself. |

"Remove what to become the other Type" tests:
- Remove housing + counts + movements, keep arrest/report/case workflows → Police RMS.
- Remove custody operations, keep docket/filing/judicial workflow → Court Case Management.
- Remove facility housing/counts, keep community-based case/contact/conditions machinery → Probation & Parole Management.
- Remove the person-in-custody anchor, keep generic intake→workflow→resolution → Public Sector Case Management.

## Uncertainties

1. No Tier-1 operational documentation (help centers, user guides) was reachable for any sampled product. All structural claims rest on official product pages (Tier 2). Assertion strength in the final document is calibrated accordingly; no precise operational parameters are stated.
2. The exact relationship between "Corrections Management System" (directory name) and the market's "JMS/OMS" labels is resolved here as synonym-with-scope-variants, but the directory has no separate "Jail Management System" leaf to reconcile against; no conflict found in DIRECTORY.md.
3. Medical/mental-health handling is inferred as an integration seam from an absence pattern (three products) plus one explicit separate-pillar observation; a product with a fully integrated medical module may exist in the market.
4. The Corrections Technology Association functional standards (referenced by Abilis as the basis of its 40 modules) could not be fetched; their content is unverified.
5. Non-US systems (UK P-NOMIS, Canadian CSC OMS, Australian state systems) were not directly sampled; the international check rests on Abilis's documented US/Canada/Australia footprint plus structural reasoning.
6. Vendor numeric claims (facility counts, report counts, booking-time reductions, uptime) are recorded as claims only.

## Final Synthesis

A Corrections Management System is the operational system of record for a correctional agency's custody population. Its defining core is small: an identified person-in-custody record; a bounded custody episode grounded in legal authority (booking → release/transfer); a housing placement in the facility's physical structure; and a movement-and-accountability loop (recorded movements reconciled by scheduled counts/cellchecks). Around that core, mature products add classification, incidents, discipline, court-event tracking with sentence/release calculation, programs/jobs/education, visitation, property, grievances, inmate funds, mandated reporting/BI, alerts/workflow, permissions/audit, mobile officer use, and integrations to RMS, courts, medical, and communications systems.

The market realizes the Type in three packaging poles — standalone jail-focused systems (JMS), modules of public-safety suites, and enterprise DOC-wide OMS platforms that extend into probation and parole — and in adjacent service layers (communications, telehealth, financial services) sold around the management core. The Type's names (Jail Management System, Offender Management System, Inmate Tracking System, Corrections Management System) are synonyms with scope differences, not different structures.

Boundary posture: upstream of booking is the police RMS; courtroom processing belongs to court case management; community supervision is the probation/parole sibling (spanned only by DOC-enterprise deployments); inmate property is not case evidence; medical is an integration seam. The historical check passes: the pre-digital jail (booking ledger, greaseboard, count sheets, movement log) contains exactly the four defining structures, so the definition is not an artifact of the current US vendor market.
