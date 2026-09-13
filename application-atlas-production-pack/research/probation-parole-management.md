# Research Notes — Probation & Parole Management

Research date: 2026-09-09

## Research Goal

Understand what a Probation & Parole Management application actually is as an Application Type: what objects exist inside it, who operates it, how supervision work flows through it, which states and rules govern it, and where its boundaries sit against neighboring justice-sector Types (corrections management, court case management, law enforcement case management, social services case management) and against the monitoring/services layer sold around community supervision.

## Initial Boundary

Working hypothesis before research:

- Core use: agencies supervising convicted or released persons living in the community under court or paroling authority — recording the supervision relationship, tracking conditions, managing officer caseloads and contacts, documenting compliance and violations.
- Primary users: probation/parole officers, case managers, supervisors, administrators; secondarily the supervised person (portals/apps) and partner treatment providers.
- Nearest neighbors: Corrections Management System (custody side of the same agency family; a pre-hung §24 joint-review flag from that pass), Court Case Management System (orders in, revocations out), Social Services Case Management (casework without legal consequence machinery), Public Sector Case Management (generic parent).
- Known unknowns: whether assessment/case-planning machinery is definitional or common; whether monitoring/GPS/check-in apps are definitional; how the parole (board/paroling-authority) side differs from probation; international (non-US) realization; whether a DOC-enterprise span collapses this Type into corrections management.

## Research Questions

1. What is the unit of record — the person, the order, or the case?
2. How does a supervision case begin (court order? parole release?) and end (discharge, transfer, revocation)?
3. What are conditions of supervision, and how does the software track compliance with each?
4. What does the officer actually do in the system: caseload, contacts, field work, assessments, violation documentation?
5. How do violations escalate — graduated sanctions, revocation referral — and who decides?
6. Are risk-needs assessments and case plans definitional, or a modern common layer?
7. Where does electronic monitoring / drug testing / mobile check-in sit — core machinery or integration seam?
8. What participant-facing surfaces exist (portals, apps, check-ins)?
9. What roles and access boundaries exist (officer, supervisor, administrator, treatment provider, supervised person)?
10. What distinguishes this Type from corrections management (custody), court case management (adjudication), and social services case management (supportive casework)?
11. Would older, non-US, differently structured supervision systems still fit the definition? (§24 check)

## Representative Products

Selection rationale: market representation in community supervision software + different product philosophies + different centers of gravity (system-of-record casework vs monitoring-first vs participant-engagement-first). All three are US-market vendors; the international check is handled through sibling-pass evidence and structural reasoning (see Uncertainties).

| Product | Vendor | Pole | Why sampled |
|---|---|---|---|
| equivant Supervision (Northpointe Suite) | equivant | person-based case management of record for supervision agencies | deepest structural evidence: assessments, case planning, case management, violations matrix, workload management; names probation AND parole officers as users |
| SCRAM Systems | Alcohol Monitoring Systems Inc. | monitoring-first supervision programs (devices + compliance software + services) | the monitoring-centric realization; shows where the Type's boundary with the monitoring layer sits |
| Corrisoft (AIR Suite) | Corrisoft | participant-engagement smartphone monitoring + dashboard | the participant-facing pole; shows how check-ins, calendars, messaging, and education wrap around supervision |

Cross-checks against adjacent already-processed Types: corrections-management-system (custody sibling, joint-review flag), court-case-management-system (justice-partner and separate-supervision-product evidence).

## Sources

All fetched 2026-09-09. Evidence layers: A = direct observation on an official product page; B = cross-product commonality; C = canonical inference from comparison + boundary reasoning.

- equivant — corporate solutions page: https://www.equivant.com/ [A]
- equivant Supervision — product site root: https://www.equivant-supervision.com/ [A]
- equivant Supervision — Case Management: https://www.equivant-supervision.com/solutions/case-management/ [A]
- equivant Supervision — Case Planning: https://www.equivant-supervision.com/solutions/case-planning/ [A]
- SCRAM Systems — site root and agency-facing pages: https://www.scramsystems.com/ (incl. /solutions/probation-parole, /products/monitoring-software, TouchPoint blog pages) [A]
- Corrisoft — AIR Suite pages: https://corrisoft.com/ (root, /air-product-suite/, /solution-overview/) [A]

Unreachable / abandoned (per source-access rules, 1–2 attempts each):

- Abilis Solutions (CORIS community corrections) — https://www.abilis.com/ — transport error ×2 (abandoned; partial evidence about its community-corrections span exists in the corrections-management-system pass, recorded there)
- ViaPath community-corrections line — /community-corrections/ 404; current site root shows facilities-focused pillars only [A — absence observation]
- UK Ministry of Justice nDelius (national probation case system) — github.com/ministryofjustice/ndelius 404, technical-documentation.data.justice.gov.uk transport error, delius-core 404 (international pole not directly sampled)
- Caseload Explorer — caseloadexplorer.com transport error ×1 (abandoned)
- SCRAM deep product doc path — /for-agencies/community-supervision-software/ 404 (root fetched instead)

Source-access limitation: no Tier-1 operational documentation (help centers, user guides, training material) was reachable for any sampled product. All structural claims below rest on Tier-2 official product pages. Assertion strength is calibrated accordingly; no precise operational parameters (numeric limits, time windows, default settings, state-name vocabularies) are asserted anywhere from memory.

## Product A — equivant Supervision (Northpointe Suite)

Official product pages (root, Case Management, Case Planning). Key observations:

- Positioning: "software solutions support Probation and Parole Officers, Administrators, Case Managers, and justice-involved individuals using software, data, people, practices, and experience." [A]
- Audience breadth: Case Management "delivers the core management features that probation, parole, community corrections agencies, institutions, and jails need to manage all the moving parts of their team's caseload." [A]
- Person-based record: "Our person-based case management system links client data together with individual assessment outcomes, case plans, programs, and notes." [A]
- Case processing events: "track and manage all of your case processing events, set reminders, handle scheduling, and easily oversee rewards, graduated sanctions, drug testing and electronic monitoring in one place." [A]
- Violations machinery: "Showcases evidence-based violations matrix." [A]
- Incentives: "Incentives and rewards tracking" alongside "graduated sanctions." [A]
- Officer workload: "a comprehensive Workload Manager to oversee supervision agency operations and caseload"; "Agency workload tracking at-a-glance"; "Managing your agency's workflow to support the supervision and case management of clients"; "Assessing thousands of clients appropriately and accurately across a staff of dozens or even hundreds of officers." [A]
- Assessments: dedicated Risk Needs Assessments solution with named validated instruments — COMPAS, COMPAS-R, LSI-R, LS/CMI, LSI-R: SV, ORAS, OYAS, WRNA-T. [A]
- Case planning: "Create individualized case plans that focus on assessed needs, establish goals, and give clear action steps"; "an evidence-based, participatory roadmap"; "assessments, goals, and actions are visible at a glance with case notes and status updates added in moments"; "Measures progress and allows the plan to be adjusted as needed"; automation flows from the supported assessments. [A]
- Court-facing duty: "critical functionality for Pre-Sentence Investigation (PSI)" — a court-facing report produced by probation. [A, single-product]
- Communication: "Automated client scheduling reminders using SMS capabilities." [A]
- Roles and access: impact lists "Probation/Parole Officers, Case Managers, Supervisors, Administrators, Justice-Involved Individuals, Treatment Providers"; "Limited access for third-partner treatment providers"; "Customizable dashboards for case managers, supervisors, and administrators." [A]
- History: "Review each justice-involved individual's complete history." [A]
- Surfaces: Solutions menu includes Portals (participant-facing portal line) and Custom Forms; Services include secure cloud hosting, data integration/migration. [A]
- Standards posture: partner/association logos include APPA (American Probation and Parole Association), CJIS, AWS. [A]
- Adjacent-family evidence: the same vendor sells Court, Corrections, Pretrial, Treatment Court, and Drug Testing LIS as separate product sites — supervision is a distinct line from the vendor's own court and corrections products. [A]

## Product B — SCRAM Systems

Official site root and agency-facing pages. Key observations:

- Positioning: "SCRAM Systems helps supervision programs close gaps with connected monitoring, drug testing, and services"; "For Agencies — Build or modernize your supervision program"; "Connected Supervision — Explore monitoring, testing, software, and services." [A]
- The coordination problem it addresses: "Supervision teams balance public safety, court requirements, testing, alerts, client communication, documentation, reporting, and the daily decisions that help people stay on track... teams can see what needs attention, manage follow up, and document the work behind positive change." [A]
- Software layer: "Monitoring & Compliance Software — Real-time visibility for smarter supervision"; "Dashboards, alerts, reports, and workflows that help teams manage activity across their caseload." [A]
- Participant-facing: "SCRAM TouchPoint® saves officers time by providing remote client check-in capability for community corrections departments"; mobile monitoring "keep clients connected between office visits with officer-managed communication, automated reminders, and mobile check-ins"; TouchPoint includes passive GPS location options for low-risk clients. [A]
- Monitoring technology around the case: GPS/location monitoring (incl. "Pattern of Life" travel-pattern mapping), continuous alcohol bracelet, remote breath, drug testing. [A]
- Managed services: "managed services that support daily operations, client touchpoints, and program outcomes" — a services layer on top of the software. [A]
- Programs served: Pretrial Supervision, Probation & Parole, Work Release Programs, Treatment & Specialty Courts; supervision-level framing by client risk (high-risk vs low-risk). [A]
- Observation: the site's center of gravity is devices + compliance software + services around supervision programs; no claims about case plans, assessments, or order management appear — the case-of-record layer is NOT this product's center. [A + comparative note]

## Product C — Corrisoft (AIR Suite)

Official AIR Suite pages. Key observations:

- Positioning: "Advanced Smartphone Monitoring for Streamlined, Accountable Supervision"; serves "probation, treatment courts, pretrial release, or residential reentry." [A]
- Agency dashboard: "AIR Dashboard — web-based management platform... connects all your AIR tools in the field... every AIR administrator accesses case management tools, real-time GPS tracking technology, and participant calendar management." [A]
- Officer-side mobile: "AIR Supervisor App — complete monitoring and reporting capabilities" on a smartphone. [A]
- Participant-facing: AIR Check-In app — "generates shared calendars with appointment reminders, video, AIR mail and SMS access to supervising staff... providing passive GPS monitoring and facial detection for scheduled or randomized check-ins"; participants "self-manage calendars, request travel exceptions, and immediately notify supervision officers if circumstances change in real time." [A]
- AIR Verify: "always on GPS, real-time alerts and seamless zone management." [A]
- Devices: AIR Mobile specialized smartphone; BLUtag one-piece ankle tracker; AIR Connect ankle tether (Bluetooth to the smartphone); Talitrix GPS wrist wearable. [A]
- Alcohol testing: AIR Thrive remote alcohol device paired with the apps — video-recorded tests with facial recognition. [A]
- Programming/education: MaxxLMS — "supervisors can appoint participants to various virtual courses... and track their progress" (behavioral-modification courses). [A]
- Support services: in-house call center (AIR Support) answering participant questions. [A]
- Observation: the center of gravity is participant engagement + monitoring with a dashboard case-management layer; deeper order/case-of-record machinery is not claimed. [A + comparative note]

## Cross-product Comparison

| Dimension | equivant Supervision | SCRAM Systems | Corrisoft AIR |
|---|---|---|---|
| Center of gravity | person-based case management of record for supervision agencies | monitoring devices + compliance software + managed services around supervision programs | participant smartphone engagement + monitoring, with a dashboard case layer |
| Supervised person record | "person-based case management," complete client history | clients as monitored caseload entries ("activity across their caseload") | participants with calendars, check-ins, messaging |
| Supervision case / order machinery | case processing events; PSI; configurable workflow | court requirements named as an input to balance; no order machinery claimed | program/compliance framing; no order machinery claimed |
| Conditions → compliance tracking | oversight of sanctions, rewards, drug testing, electronic monitoring per client | alerts, testing, monitoring status as the compliance picture | zones, scheduled/randomized check-ins, alcohol tests, education appointments |
| Contacts / check-ins | scheduling, reminders (SMS), case notes | remote check-ins via TouchPoint; officer-managed communication | scheduled/randomized check-ins with facial detection; shared calendars; messaging |
| Violations / sanctions | "evidence-based violations matrix," graduated sanctions, incentives | alerts and follow-up documentation ("manage follow up") | real-time alerts; notify officers of circumstance changes |
| Assessments / case plans | validated instruments (COMPAS/LSI-R/ORAS class) + automated case plans | absent from claims | goal-attainment framing only |
| Participant portal/app | Portals solution line | TouchPoint mobile app | AIR Mobile / Check-In / Verify apps + LMS |
| Treatment/education programming | programs and referrals; limited provider access | managed services as client touchpoints | MaxxLMS courses appointed by supervisors |
| Roles observed | probation/parole officers, case managers, supervisors, administrators, justice-involved individuals, treatment providers | agencies, supervising officers, service providers | administrators, supervising staff, participants |
| Populations served | probation, parole, community corrections agencies (also institutions/jails as clients) | pretrial, probation & parole, work release, treatment courts | probation, treatment courts, pretrial release, residential reentry |

Reading of the comparison:

- All three organize work around a supervised person and a caseload of such persons (B). All three connect the person's compliance state to officer attention — alerts, follow-up, documentation (B).
- Only the case-of-record pole claims order/case machinery, assessments, case plans, violations matrices, and graduated sanctions (A, single-product for those specifics).
- The monitoring-first and engagement-first poles are how the compliance-collection layer of the same supervision world is realized and sold; they integrate toward the case layer rather than replace it. This is the same layering the corrections pass recorded (management core vs communications/service layers around it).
- Electronic monitoring, drug testing, GPS, check-in apps are widely present but are instruments of condition compliance — era and program machinery, not the defining structure (C inference; supported by the historical check below).

## Canonical Model

### L0 — Defining Invariant

Minimal joint structure without which the product is not recognizable as Probation & Parole Management:

1. **The supervised person of record** — a persistent identified record for a person serving a community-based sentence or release (client/offender/participant vocabulary varies). The world is organized around people living in the community, not around facility structures. Remove → a person registry / contact database.
2. **The supervision case grounded in legal authority** — a bounded supervision relationship created by a court order (probation) or a paroling authority's release decision (parole), carrying the **ordered conditions** the person must meet (reporting, treatment, testing, fees, curfew, program participation — vocabulary varies), advancing toward an end state: successful completion/discharge, transfer, or revocation. The system records but does not create this authority. Remove → order documents with no supervision operation (court-side record).
3. **The officer-side supervision loop** — officers carry the person as a caseload assignment; contacts/reporting are recorded (office, field, phone, remote check-ins); condition compliance is tracked over time with monitoring/testing results feeding in; non-compliance is surfaced as recorded violations escalated through graduated sanctions toward revocation referral back to the court or paroling authority; positive progress is likewise recorded. Remove → compliance registry with no supervision operation; the "management" is gone.

Jointly-held load-bearing tests:

- 1 alone = supervised-person roster / registry
- 2 without 1 = order records on the court's side (docket output), not a supervision system
- 3 without 1+2 = generic casework/contact management (social-services territory)
- 1+2 without 3 = an order archive; nothing is supervised
- 1+3 without 2 = supportive casework with no legal authority or consequence machinery
- 2+3 without 1 = anonymous order enforcement with no person continuity across episodes

### L1 — Common Mature Structure

Very common in mature modern products, not required to recognize the Type:

- Risk/needs assessment instruments and assessment-driven **case plans** (goals, action steps, progress review) — the "evidence-based supervision" layer
- Caseload/workload management surfaces for officers; dashboards for supervisors/administrators
- Program and referral tracking (treatment, education, community service), often with limited partner-provider access
- Scheduling, reminders, and notifications (SMS/app)
- Custom forms and document management; court-facing report production (e.g., pre-sentence investigation reports in probation-heavy deployments)
- Statistical and stakeholder reporting (agency, state, federal)
- Participant-facing surfaces: portals, mobile check-in apps, shared calendars, messaging
- Integration spine: courts, monitoring vendors, treatment providers, drug-testing systems
- Role-based access with audit; cloud/government-hosted deployment posture

### L2 — Variant / Optional Structure

Depends on jurisdiction, population, program, era:

- Population mix: adult probation, parole, juvenile probation, pretrial supervision, treatment/specialty courts, work release, residential reentry/community-corrections facilities
- Electronic monitoring depth: GPS/ankle/continuous-alcohol/remote-breath/drug testing, zones, pattern-of-life — often delivered by specialist vendors and integrated
- Managed monitoring/participant support services (call centers, outsourced operations)
- Financial machinery: supervision fees, restitution handling (common in some jurisdictions; unverified in this sample — held uncertain)
- DOC-enterprise span: one system covering custody + probation + parole (packaging, recorded in the corrections pass)
- Court-facing duties: pre-sentence investigation reports, violation-report production
- Regional/organizational structure: US county probation departments vs state parole authorities vs DOC community-corrections divisions; national probation services elsewhere (not directly sampled)

### L3 — Vendor-specific Structure

(recorded here only; excluded from the final document)

- equivant: Northpointe Suite branding; named assessment instruments (COMPAS/COMPAS-R heritage from Northpointe; LSI-R/LS/CMI; ORAS/OYAS; WRNA-T); Workload Manager; violations matrix; PSI functionality; Portals solution line; CJIS/APPA association posture
- SCRAM: SCRAM CAM transdermal bracelet ("tests sweat for alcohol every 30 minutes" — vendor claim); TouchPoint mobile app; "Pattern of Life" GPS mapping; OnTarget partner portal; managed monitoring services framing
- Corrisoft: AIR brand family (AIR Mobile specialized smartphone, AIR Check-In, AIR Verify, AIR Thrive, AIR Connect, BLUtag, Talitrix); AIR Mail; MaxxLMS / Corrections Rehabilitation Institute courseware; AIR Support call center; "first smartphone-based supervision solution" claim

## Rejected Findings

- "Risk-needs assessments and case plans are part of the defining core" — rejected: only the case-of-record pole claims them; the monitoring-first and engagement-first poles run supervision programs without them, and the pre-digital practice (conditions + contact logs + violation reports) satisfies the Type without validated instruments. They are the strongest common-mature layer, not the invariant.
- "Electronic monitoring / GPS / mobile check-ins are definitional" — rejected: absent entirely from the pre-digital era and optional in program design (agencies choose which conditions to monitor); specialist vendors deliver them as a layer around supervision.
- "A full monitoring suite is required" — rejected: SCRAM/Corrisoft products are supervision-program realizations centered on the compliance-collection layer; the case-of-record pole sells oversight of third-party monitoring rather than the monitoring itself.
- "Parole-board hearing/decision machinery is part of this Type" — not established in this sample: the parole side observed here is the supervising-officer side (officers supervising released persons). Board-side machinery (hearings, decisions) was not directly evidenced; recorded as an uncertainty, not asserted either way.
- "Jails/institutions are outside the audience" — rejected by direct evidence: the case-of-record vendor names institutions and jails among the agencies it serves with the same person-based case machinery (case management for programs/conditions without custody structures). Community supervision machinery can be sold into facilities as a case layer — this does not move the defining core.
- Precise operational parameters (contact frequencies, caseload sizes, fees, deadlines, state vocabularies) — rejected for the final document: vendor pages do not establish them; no memory-filling.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (what to remove/keep) |
|---|---|---|
| Corrections Management System | sibling (§24 joint-review counterparty) | Corrections manages people held in facilities: custody episode, housing placement, movements/counts. This Type manages people living in the community under conditions: supervision case, condition compliance, officer contacts, violation escalation. Remove facility housing/counts/movement machinery and keep community-based case/contact/conditions machinery → this Type; add custody structures → corrections. DOC-enterprise products span both — packaging across the seam, not proof of one Type. Ratified keep-both (this pass discharges the corrections pass's flag). |
| Court Case Management System | upstream + downstream adjacent | The court creates the order and owns the docket, hearings, and adjudication; the supervision system receives the order/commitment as its legal authority and sends back violation reports, progress, revocation referrals. Court vendors sell supervision as a separate product line. Remove the supervision loop and keep docket/judicial workflow → court CMS. |
| Law Enforcement Case Management / Police RMS | adjacent | Those Types record events and investigations about people; no supervision relationship, no ordered conditions, no compliance loop. The supervised person may appear there as a subject; the records are different objects. |
| Social Services Case Management | closest generic sibling | Supportive casework shares the shape (assigned caseworker, contacts, notes, episodes) but lacks the legal authority, the ordered conditions, and the consequence machinery (sanctions → revocation). Remove the court/parole authority and consequence machinery → social services case management. Joint-review note left for the unprocessed §24 sibling. |
| Public Sector Case Management | generic parent | Generic intake→workflow→resolution lacks conditions-driven compliance, monitoring integration, and the sanction/revocation consequence path. |
| Electronic monitoring vendors (devices + compliance software + check-in apps) | service/technology layer | Monitoring collects condition-compliance evidence; the supervision system holds the case, the conditions, and the consequences. Products centered only on monitoring (devices, alerts, check-ins) sit in this layer even when sold into probation & parole programs; center of gravity decides. |
| Pretrial services software | adjacent machinery (no separate directory leaf) | The same supervision machinery applied to pre-trial release populations (court-appearance and compliance conditions before conviction); sampled products sell pretrial and probation/parole programs side by side. |
| Prosecutor / Public Defender case management | adjacent | Prosecution/defense case objects are criminal matters, not supervision relationships. |

"Remove what to become the other Type" tests:

- Remove housing/counts/movements, keep community case/contact/conditions machinery → Probation & Parole Management (corrections → here).
- Remove the supervision loop + conditions/consequence machinery, keep the docket/judicial workflow → Court Case Management.
- Remove the legal authority + sanction/revocation machinery, keep supportive casework → Social Services Case Management.
- Remove the person-based supervision case, keep device/alert/check-in machinery → monitoring layer, not this Type.

## §24 Historical / Market-Sample Check

- Pre-digital probation: a court order in the case folder, a conditions sheet, the officer's contact/report log (signed monthly reports), violation reports to the court, revocation hearings; parole: the paroling authority's release decision, conditions, the field officer's supervision record, revocation to the authority. All contain exactly the three L0 structures with no software-era machinery (assessments, GPS, portals, apps) — the definition is not an artifact of the current US vendor market. Historical check passed.
- Non-US structure: the definition names "court order or paroling authority" generically rather than US county/state machinery; national probation services fit the same three structures (not directly sampled — see Uncertainties).
- Era check: the assessment/case-plan layer (evidence-based supervision) and the monitoring/app layer are treated as common/variant, not defining, precisely because older and differently positioned systems satisfy the Type without them.

## Uncertainties

1. No Tier-1 operational documentation (help centers, user guides) was reachable for any sampled product; all structural claims rest on Tier-2 official product pages. Assertion strength is calibrated; no precise parameters asserted.
2. The parole (paroling-authority) side is evidenced only from the supervising-officer perspective; board/hearing/decision machinery, if packaged separately, was not observed. Possible sibling machinery; not resolved here.
3. International realization (UK nDelius-class national systems) could not be fetched; the international check is structural + sibling evidence (a court vendor's supervision product line sold internationally; the corrections pass's Canada/Australia DOC footprint).
4. Financial machinery (supervision fees, restitution) is common in the domain but unverified in this sample; held uncertain and excluded from the core.
5. Residential community corrections (halfway houses / residential reentry): one sampled product serves residential reentry; whether facility-shaped residential programs belong to this Type or to corrections is an open seam (population variant recorded, not resolved).
6. Sample is three US-market vendors, two of which are compliance-layer specialists; the case-of-record pole is documented from marketing/product pages only. Market breadth beyond this sample (statewide implementations, kiosk check-in vendors, registry/sexual-offender specialized systems) is unverified.

## Final Synthesis

A Probation & Parole Management application is the community-supervision agency's operational system of record for people serving sentences or releases in the community. Its defining core is three jointly-held structures: the supervised person of record; the supervision case grounded in legal authority (court order or paroling-authority release) carrying ordered conditions and advancing to completion, transfer, or revocation; and the officer-side supervision loop — caseload assignment, recorded contacts/reporting, condition-compliance tracking fed by monitoring and testing, violations escalated through graduated sanctions to revocation referral, and positive progress recorded. Around that core, mature products add assessment-driven case planning, program/referral tracking with partner access, scheduling and reminders, forms and court-facing reports, statistical reporting, participant portals and check-in apps, integrations to courts and monitoring vendors, and role-based access. The market realizes the Type at three poles — case-of-record suites, monitoring-first program stacks, and participant-engagement platforms — plus the DOC-enterprise packaging that spans custody and community in one system. The Type's boundary is structural, not lexical: custody structures make corrections management; dockets and adjudication make court case management; supportive casework without consequence machinery makes social services case management; devices and alerts without the case make a monitoring layer.
