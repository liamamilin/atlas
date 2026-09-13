# Research Notes — Public Defender Case Management

Research date: 2026-09-09
Slug: public-defender-case-management
Directory leaf: Public Defender Case Management (§24 Government, Public Sector & Civic)

---

## Research Goal

Understand, from real products, what a Public Defender Case Management application is: the system of record a public defense agency uses to manage its representation of indigent clients across criminal (and related) court proceedings — who uses it, what objects exist inside it, how defense work flows, which states/rules matter, and how it differs from neighboring justice-sector Types (prosecutor case management, court case management, law practice management).

## Initial Boundary (hypothesis before research)

- What: case management for public defender offices/agencies (government-funded criminal defense for people who cannot afford counsel).
- Who: public defenders (attorneys), defense investigators, social workers (holistic defense), supervisors, office/agency administrators.
- Nearest Types: Prosecutor Case Management, Court Case Management System, Law Practice Management System, Legal Matter Management, Public Sector Case Management (generic), Social Services Case Management.
- Suspected boundary: the *defense-side party perspective* on the court process — the client relationship, defense work product, and attorney caseload — as opposed to the prosecution side, the court's neutral docket, or a billing-centric private firm.
- Unknowns: exact object model (client vs case vs charge vs event), conflict-checking mechanics, indigency/eligibility handling, court integration depth, reporting obligations to funders/oversight.

## Research Questions

1. What is the central unit of record — client, case, or matter? How do charges, court events, and people relate to it?
2. What is the case lifecycle (intake/appointment → assignment → court events → disposition → close)?
3. How are court events/hearings tracked, and how do they sync with court systems?
4. How does conflict-of-interest checking work (co-defendants, victims, witnesses)?
5. How is indigent eligibility handled at intake?
6. What do attorneys vs investigators vs administrators do?
7. How are documents (motions, discovery requests, pleadings) produced and filed?
8. What reporting exists (caseload/workload statistics, funding/grant reports)?
9. Where is the boundary with prosecutor case management and court case management?
10. What integrations exist (courts, jails/sheriff, e-filing, legal research)?

## Representative Products

Selected for market representativeness, documentation quality, and differing product philosophies:

| Product | Vendor | Philosophy / Position | Customer level (observed) |
|---|---|---|---|
| DEFENDERbyKarpel (DbK) | Karpel Solutions (St. Louis, MO) | Dedicated defender-side criminal case management; "same tools as prosecutors, geared to public defenders"; on-prem or Azure Government Cloud hosting | County public defender offices (Mifflin County PA, Bucks County PA, Williamson County IL) |
| LegalServer | Network Ninja, Inc. (Chicago) | Configurable web platform built exclusively for civil legal aid + public defense + government law offices; AWS-hosted; strong public help docs and APIs | Statewide agencies (Kentucky DPA, Colorado State PD, Nevada DIDS), county offices (Travis County TX, Harris County TX, Snohomish County WA, NYCDS), hybrid defender-nonprofits (Kalamazoo Defender) |
| eDefender | Journal Technologies (subsidiary of Daily Journal Corp.) | Defender product inside a justice suite (eCourt / eProsecutor / eDefender / eSupervision) sharing the eSeries framework | Justice-suite customers; public defender offices; Kentucky DPA previously a Journal Technologies customer |

Also known in the market but not researchable in this pass (source-access limitations below): Tyler Technologies' justice products (site returned 403), CSG justice products (transport errors), MTG "Defender Data" (domain parked/for sale), "CaseWorks" (no reachable official site found).

## Sources

Tier 1 (official operational documentation):

- LegalServer Help — https://help.legalserver.org/
  - Case Status: https://help.legalserver.org/article/2725-case-status
  - Disposition and Case Status Compared: https://help.legalserver.org/article/1632-disposition-and-case-status-compared
  - Case Assignments: https://help.legalserver.org/article/1729-case-assignments
  - Case Profile Pages: https://help.legalserver.org/article/1717-case-profile-pages
  - Lead and Member Cases: https://help.legalserver.org/article/1629-lead-and-member-cases
  - Client Intake: https://help.legalserver.org/article/2558-client-intake
  - Closing a Case: https://help.legalserver.org/article/2435-closing-a-case
  - Cause Number: https://help.legalserver.org/article/1664-cause-number
  - Timekeeping category: https://help.legalserver.org/category/2589-timekeeping
  - Optional Modules category: https://help.legalserver.org/category/2585-other-modules
  - Cases & Matters category: https://help.legalserver.org/category/2587-casesmatters

Tier 2 (official product pages):

- DEFENDERbyKarpel — https://www.defenderbykarpel.com/ (+ /efficiency/ + /conflict-checking/ + /investigative-services/ + /evidence-tracking/ + /integrations/ + /information-management/ nav)
- Karpel Solutions corporate — https://www.karpel.com/
- Journal Technologies eDefender — https://www.journaltech.com/edefender (and https://www.journaltech.com/ suite overview)
- LegalServer marketing — https://www.legalserver.org/ and https://www.legalserver.org/public-defender/

Tier 3 (official vendor news / customer stories):

- Kentucky DPA selects LegalServer: https://www.legalserver.org/news/kentucky-department-of-public-advocacy-modernization/
- Travis County warrant alerts ("Cutting Days in Custody"): https://www.legalserver.org/news/cutting-days-in-custody/

Unreachable sources (recorded per source-access limitation rules):

- tylertech.com — HTTP 403 (2 attempts)
- csgjustice.com — transport error (2 attempts)
- mtgmc.com — domain parked ("for sale")
- caseworks.com / www.caseworks.com — transport errors
- Search engines (DuckDuckGo, Brave, Mojeek, SearXNG) — timeouts/403; Bing returned localized irrelevant results

Consequence: the sampled product set is 3 (within the 2–5 target). Claims about products outside the sample are not made. Karpel and Journal evidence is marketing-page level (Tier 2), so product-specific mechanics for those two are stated with lower confidence than LegalServer mechanics (Tier 1).

---

## Product A — DEFENDERbyKarpel (DbK)

Evidence layer: A (direct observation of official product pages; marketing register — mechanics inferred only where explicitly described).

### Key observations

- Positioning: "Powerful criminal case management tools designed specifically for public defenders"; "levels the playing field by providing the same capabilities afforded to prosecutors, but geared to the needs of public defenders and their clients." Explicitly a sibling of PROSECUTORbyKarpel.
- **Person Centric**: "comprehensive profiles and records of victims, witnesses, and defendants"; "Clearly display the roles associated with a person, such as defendant, witness, and co-defendant"; dedup ("remove duplicates and errors"), date stamping, "conduct comprehensive searches and efficiently organize data by individual."
- **Conflict Checking**: dedicated feature area; "systematically scanning case information and cross-referencing it with relevant data… proactively identify potential conflicts of interest"; "manage dozens of involved parties at once"; framed as ethically mandatory ("can't be ignored due to ethical considerations").
- **Electronic Docket / courts integration**: "built-in court interface… Electronic Docket control: automatically update the docket with upcoming events, eliminating the need to manually search for each individual case"; e-filing links; "Working with Justice Partners."
- **Document Management & Generation**: Word mail-merge generation; "automatically save all generated documents directly to their respective cases"; generate documents for multiple cases simultaneously; web-based scanning + OCR.
- **Workflow Management**: "task assignment, tracking, and deadline management."
- **Evidence Tracking**: case evidence "entered and tracked from virtually anywhere"; "fully integrated with Evidence.com" (digital evidence platform).
- **Investigative Services**: "Investigation Tracking Services… improve communications, generate accurate reports quickly, track time better… fostering better accountability for investigators" — defense investigators are a first-class staff role.
- **Information Management**: "Power Search" across case information; "Comprehensive Financial Tracking"; "statistical reports to analyze work spent on case type, tasks, and staff members."
- **Time tracking**: "track the amount of time spent on tasks" — for statistics, not client billing.
- **Hosting/security**: Microsoft Azure for Government Cloud; CJIS compliance; 99.5% uptime claim (vendor claim, not verified).
- **Calendar & email integration**; **External Agency Portal**; **Westlaw integration** (legal research).
- Customer news: county public defender offices going live (Mifflin County PA, Bucks County PA — "46-user", Williamson County IL — "manual" predecessor noted).

## Product B — LegalServer

Evidence layer: A (direct observation of official help documentation — strongest evidence in this sample).

### Key observations

- Positioning: "built exclusively for civil legal aid, public defense, and government law offices… not built for the profitability demands of for-profit law firms." Public defender page: "optimized to help public defenders leverage technology to protect fundamental rights… of those who are unable to afford an attorney."
- **Case/Matter model with a two-layer status system** (help doc, direct):
  - **Disposition** — system-controlled field tracking the application from prescreen/intake through open/closed or rejected. Six values: Prescreen → Incomplete Intake → Pending → Open → Closed; plus Rejected Matter. Users cannot directly set disposition; they must step through processes (e.g., a case cannot be flipped to Closed — the agency's "Close Case" process must be completed).
  - **Case Status** — agency-controlled lookup used as a workflow tool on pending/open cases (examples given: "Set for team meeting", "Needs supervisor review", "Pending conflict determination", "Awaiting pro bono placement", "Ready to close"). Every change recorded in Case Status History with date + user + note.
- **Case Assignments** (help doc, direct): every case must be assigned to a **Primary Advocate**, an **Assigned Office**, and an **Assigned Program**. Additional assignments carry an Assignment Type (examples: "Pro Bono", "Co-Counsel", "Intern"). Assignments have start/end dates; current vs past; primary assignment can only be transferred, not deleted. Assignment history list on case profiles. "Every pending and open case will appear on someone's home page" via the standard My Assignments list.
- **Case Profile Pages** (help doc, direct): tabbed layout; Actions menu (add case note, upload document, …); disposition gates editability — after closure, fields/actions are locked down "to prevent information on closed cases from being changed without re-opening the case."
- **Client–case structure** (help doc, direct): clients (persons) hold multiple associated cases; "Associating Multiple Cases with a Client"; **Lead and Member Cases** group cases involving *different clients* (example given: same defendant multiple cases; juvenile siblings) with one lead case — previously named "Master and Subordinate Cases"; **Related Cases**; **Case Contacts** (people in roles on a case).
- **Cause Number** (help doc, direct): a text field for the court's case number; can be surfaced as the primary case identifier throughout the UI (breadcrumbs, calendar, search, reports) and made a clickable link; search results default-filtered to the user's Office.
- **Intake** (help doc, direct — civil-oriented flow): Prescreen → Initial Information → Applicant Conflict Check → Family/Household → Adverse Party Conflict Check → Financial Information → Demographics → Eligibility Screen. Conflict checks appear as named intake steps (applicant + adverse party).
- **Timekeeping** (help docs, direct): "timeslips" per user per case; verify-time workflow; batch entry; posting/locking. Purpose in this market is workload/funding accounting, not client billing.
- **Reporting** (marketing + help): built-in reports with manager-specific views; "Track caseloads against benchmarks by case type, so workload and capacity are always visible"; Report Nuggets; any report can be exposed as a read-only Report API (JSON/XML); RESTful APIs for case creation/search/updates/notes/documents.
- **Justice-partner integration patterns** (customer story, Travis County TX — direct): daily automated search of the sheriff's warrant database matched against the agency's client records → email to the *assigned attorney*; same pattern powers "Court calendaring: daily searches of online court dockets automatically create attorney-specific calendar events", client monitoring, rearrest notification. The attorney assignment is the routing key.
- **Public defender scope statements** (marketing, direct quotes): appellate/post-conviction work; juvenile cases; "Manage holistic defense services when social work support, immigration advice, housing, or mental health advocacy is needed"; integrated interaction with outside counsel and experts.
- **Security posture**: AWS hosting with Government Cloud option; SOC 2 Type II, CJIS, NIST compliance claims; role-based access control with audit logging; encryption at rest/in transit.
- **Optional modules** (help category, direct): SSO, MFA, online intake, SMS to/from a case, external forms, workflows, case bundles, document automation integrations (Gavel/Documate, Docassemble), SharePoint/Google Drive/Dropbox, APIs.
- **Scale evidence** (Kentucky DPA story, direct): statewide agency — 36 trial offices across 120 counties, ~900 professionals + 200+ external contractors, 130,000+ trial and post-trial cases annually; specialized units: Conflict and Contract Services, Post-Conviction, Appeals, Juvenile Post-Disposition. Nevada DIDS quote: reports on "attorney workloads across the state."

## Product C — Journal Technologies eDefender

Evidence layer: A (official product page; marketing register).

### Key observations

- Positioning: "Case management for public defenders" inside a justice suite: eCourt (courts), eProsecutor (prosecutors), eDefender (public defenders), eSupervision (probation/parole/pretrial/diversion). Shared "eSeries Framework" (document management, business workflows, calendaring/scheduling, security, third-party integration).
- Feature claims: "managing intricate cases end-to-end, administering comprehensive discovery processes, tracking grants and funding, creating detailed court reports"; 24/7 access.
- **Conflict-of-Interest Checking**: "automatic Conflict of Interest Checking."
- **Discovery**: "Simplified Discovery… manage, track, and share case files. Auto-assign items for review, redaction, and disclosure."
- **Document management**: auto-populate document templates; file-cabinet folders; redaction, stamping, notations, highlighting, word search; "Search & Redact" one-click redaction.
- **Time and Expense**: "Track your work hours on each case… tie your time and expenses directly to grants or statutory requirements."
- **Subpoena management**: "Automate mass batch subpoenas… email delivery to personal service or mailing."
- **Dashboards**: "bird's eye view of your entire caseload."
- **Secure Public Portal**: "extend controlled access to clients, attorneys, justice partners, and witnesses."
- **Communication**: notifications; "Share Book" real-time document annotation with chat.
- **Integration**: "secure APIs… interfacing with court case management systems or integrating with evidence management platforms like Evidence.com."
- **Audit logs**: "recording every case detail."
- Configurability: "Create custom workflows, design screens, and manage site navigation your way."

---

## Cross-product Comparison

| Dimension | DEFENDERbyKarpel | LegalServer | eDefender | Reading |
|---|---|---|---|---|
| Client/person records | Person-centric: defendants, victims, witnesses, co-defendants with roles | Client (person) holds multiple cases; case contacts in roles | People in roles on cases (portals extend to clients/witnesses) | **Cross-product common (B)**: person records with case roles; the defended client is the anchor |
| Case as unit of work | Cases; documents auto-saved to cases; multi-case document generation | Case/Matter with disposition lifecycle; cause number as court identifier | Cases end-to-end; court reports | **Cross-product common (B)**: case is the hub |
| Court identity of case | Electronic docket pull from courts | Cause Number field (court case number) as first-class identifier | Interfaces with court case management systems | **Cross-product common (B)**: case carries the court's cause/docket number |
| Court events / calendar | Electronic Docket auto-updates upcoming events | Calendar events per case; docket searches auto-create attorney events | Calendaring and scheduling; court reports | **Cross-product common (B)**: hearings/events tracked per case, often synced from court systems |
| Assignment / ownership | Attorney assignment routes warrant alerts (Travis County is LegalServer; Karpel has staff/task accountability) | Primary Advocate + Office + Program mandatory; assignment types; history | Caseload dashboards | **Cross-product common (B)**: case owned by a responsible attorney; caseload visible per attorney |
| Conflict checking | Dedicated feature; scans and cross-references involved parties | Named intake steps (applicant + adverse party conflict check); "Pending conflict determination" status example | "Automatic Conflict of Interest Checking" | **Cross-product common (B)**; mechanics differ (depth not directly evidenced) |
| Documents | Word mail-merge generation; auto-file to case; OCR scanning | Documents/files on cases; document templates; automation integrations | Template auto-population; file cabinets; redaction/annotation | **Cross-product common (B)** |
| Discovery / evidence | Evidence Tracking + Evidence.com integration | Documents on cases (discovery handling not detailed in fetched docs) | eDiscovery: review/redaction/disclosure assignment | **Common (B)** — depth varies; strongest claims from Karpel/eDefender marketing |
| Investigation | Investigative Services tracking for defense investigators | Outside counsel/expert interaction mentioned | Subpoena management | **Common/Optional (B)** — investigator support present but unevenly evidenced |
| Timekeeping | Time spent tracked for statistics | Timeslips per case; verify workflow | Time & Expense tied to grants/statutes | **Cross-product common (B)** — time is workload/funding accounting, never client billing |
| Reporting | Statistical reports by case type, tasks, staff | Built-in reports; caseload vs benchmarks; manager views; Report APIs | Comprehensive reporting; grant monitoring | **Cross-product common (B)** — workload/caseload reporting to management & funders |
| Lifecycle control | Workflow management (tasks, deadlines) | Disposition (system-gated) + Case Status (agency-defined) with history; close-case process; closed-case lockdown | Custom workflows | **Cross-product common (B)**: gated lifecycle + workflow states; exact values agency/vendor-specific |
| Multi-office / programs | County offices (46-user deployments noted) | Office + Program structure; statewide agencies (36 offices) | Suite context | **Common (B)** — organizational structure of offices/programs/divisions |
| Security/compliance | Azure Gov Cloud; CJIS | AWS Gov option; SOC 2 / CJIS / NIST; RBAC + audit | Audit logs; secure portals | **Common (B)** — criminal-justice data regime |
| Client-facing surfaces | External Agency Portal | SMS from case; online intake; Simple Justice client portals | Secure Public Portal (clients, witnesses) | **Common/Optional (B)** |
| Billing clients | Absent (financial tracking exists; not client billing) | Absent (timekeeping ≠ billing; explicitly not for-profit firms) | Absent (time/expense for grants) | **Cross-product absence (B)** — defining negative: no client billing anywhere in sample |
| Eligibility / indigency | Not evidenced on fetched pages | Eligibility screen exists (civil-oriented); PD intake often court-initiated (not directly evidenced) | Not evidenced | **Uncertain** — recorded as variant/uncertainty |
| AI | Not evidenced | "Built-in AI" on PD page | Not evidenced | **Optional** |

## Canonical Abstraction

### Level 0 — Defining Invariant (minimal)

Four jointly-held structures. Remove any one and the system stops being recognizable as public defender case management:

1. **The represented client of record** — a persistent person record for an indigent person facing criminal charges (or other loss of liberty) to whom the agency owes representation; the anchor to which cases, communications, and history attach. (Remove → anonymous matter tracking.)
2. **The defense case as the unit of work** — the office's record of one court proceeding in which it defends a client, identified by the court's own cause/docket number, carrying the charges and the people-in-roles, advancing through a gated lifecycle (opened → worked → disposition → closed). The hub to which events, notes, documents, evidence, and time attach. (Remove → contact list / person registry.)
3. **The court-event-driven work rhythm** — hearings and court deadlines tracked per case (commonly synced from court systems) that pace the defense work performed between events. (Remove → a matter archive with no operational rhythm; a bare calendar without cases.)
4. **Assignment and caseload** — each case owned by a responsible attorney within the agency's office/program structure, making caseload per defender visible, assignable, transferable, and reportable. (Remove → a court-docket mirror with no defense-side management dimension.)

Jointly-held load-bearing checks:

- 1 alone = client/person CRM
- 2 without 1 = anonymous docket/case tracker
- 3 without 2 = bare court calendar
- 4 without 1–3 = staffing roster
- 1+2 without 3 = matter archive with no court rhythm
- 2+3 without 4 = a party-agnostic docket mirror (prosecutor/court territory)
- 1+3 without 2 = appointment scheduling around people

### Level 1 — Common Mature Structure

Present across the sampled products (or strongly in 2 of 3) but not definitional:

- Conflict-of-interest checking over involved parties (near-universal in sample; ethically driven; mechanics vary)
- Document management & generation from templates, auto-filed to the case
- Case notes with attribution/history
- Discovery / evidence tracking (review, redaction, disclosure; digital-evidence platform integration)
- Defense investigation support (investigator tasks, reports, subpoena management in one product)
- Timekeeping per case (timeslips) for workload and funding accounting — explicitly not client billing
- Caseload/workload reporting and dashboards (per attorney, per case type, vs benchmarks); funding/grant reports
- Calendar & email integration; court docket integration (electronic docket pull, docket-scrape event creation)
- Role-based access control, audit logging, criminal-justice security regime (CJIS-family compliance claims)
- Multi-office / multi-program / specialized-unit structure (trial, appeals, post-conviction, juvenile)
- Client communication surfaces (SMS from case, client portals) and external justice-partner portals
- APIs / integration toolkit for justice-partner data (warrants, dockets, arrests)

### Level 2 — Variant / Optional Structure

- Indigency/eligibility determination at intake (varies by jurisdiction; some offices screen eligibility, others receive court appointments — not directly evidenced in fetched PD-specific pages; recorded as uncertainty)
- Holistic defense (social work, immigration advice, housing, mental-health advocacy alongside legal representation)
- Appellate / post-conviction / juvenile case types as configured divisions
- Grant / funding tracking tied to time and expenses
- E-filing integration; legal-research integration
- AI assistance
- Deployment: on-prem vs government-cloud hosting; cloud-vs-"not the cloud" positioning is a vendor axis, not a Type property
- Client-facing portals vs staff-only systems

### Level 3 — Vendor-specific (Research Notes only)

- Karpel: "Power Search", "Electronic Docket" control naming, Westlaw integration, Evidence.com integration, "Why Not The Cloud" positioning page, 99.5% uptime claim
- LegalServer: six-value Disposition system; Prescreen; Lead/Member Cases (ex "Master and Subordinate"); Blocks architecture; Report API; Gavel/Documate & Docassemble integrations; Simple Justice portals; Cause Number Identification feature
- eDefender: eSeries Framework; Share Book live annotation; Search & Redact; eFile-it/ePay-it siblings; mass batch subpoenas

## Vendor-specific Findings

See Level 3. Additionally: Karpel explicitly markets itself as the defense sibling of its prosecutor product ("same powerful tools used by prosecutors"); Journal sells eDefender alongside eProsecutor/eCourt — both vendors confirm at the market-structure level that prosecutor and defender case management are sibling products from the same vendors, while remaining distinct Types.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove / add to cross the boundary) |
|---|---|---|
| Prosecutor Case Management | sibling / opposite party | Same court ecosystem, same object vocabulary (cases, events, evidence, people). The prosecutor initiates charges and represents the state; the defender represents the accused client. Remove the defense-client relationship and the defense-side work perspective → prosecutor CM. Vendors ship them as separate sibling products. |
| Court Case Management System | adjacent / neutral record | The court's system is the neutral docket of record for all parties; PDCM is one party's working system built around its clients and its defenders' caseload. Remove the party perspective (client of record + defense work product + attorney caseload) → court CMS. |
| Law Practice Management System | adjacent / different economics | Private firms acquire clients and bill them; timekeeping drives invoices. Public defense clients are indigent; the funder is the government; time drives workload/funding reports. Add client billing + client acquisition, remove the government/indigency context → LPM. The "no client billing" absence is cross-product in the sample. |
| Legal Matter Management | adjacent / different user | Matter management for corporate/in-house legal departments tracking outside counsel and legal spend; not defense-of-indigent-persons work. |
| Public Sector Case Management (generic) | genus | Generic government case management (permits, benefits, service requests) lacks the legal-proceeding structure: charges, court events, conflicts, discovery, cause numbers. PDCM is a legal-proceeding-shaped species of public-sector case management. |
| Social Services Case Management | adjacent / different object | Social-services cases are service needs (benefits, placement); PDCM cases are court proceedings. Holistic defense brings social-work support *inside* the defense agency, but the case core remains the legal proceeding. |
| Law Enforcement Case Management / Evidence Management System | adjacent / other side of investigation | Police-side records and evidence custody; the defender's evidence tracking is about receiving/reviewing/disclosing discovery, not collecting evidence as an investigative agency. |
| Legal Docket Management / Legal E-filing Platform | capability-adjacent | Docket tracking and e-filing appear as integrations/capabilities inside PDCM, not as its center. |

Key boundary judgment: **the defense-side party perspective** (represented indigent client + defense work product + defender caseload) is what separates PDCM from both the court's neutral system and the prosecutor's mirror-image system. The strongest structural tell observed: the *attorney assignment as routing key* (warrant alerts, docket-created events, caseload views all route to the assigned defender).

## Historical / Market-Sample Check

- Paper-era public defender office: manila case folders per client/case annotated with the court cause number, court-date calendars, attorney assignment boards, conflict card indexes, time-in-court logs, caseload reports to county funders — satisfies all four Level-0 structures with no software.
- 1990s–2000s dedicated systems (e.g., the Defender Data / JustWare generation, not directly reachable in this pass): client/case/event/conflict/report structures on-prem — consistent with the same core.
- Regional note: the sampled products are US-centric (cause numbers, CJIS, Gideon-era indigent defense). Other jurisdictions organize defense differently (duty-solicitor rosters, salaried public defender services); the four-leg core (client of record, defense case, court rhythm, assignment/caseload) still describes them, but this pass contains no non-US source — recorded as a limitation.

## Uncertainties

1. **Indigency/eligibility determination**: how prominently PD-specific products handle eligibility screening at intake (LegalServer's eligibility screen is documented in its civil-oriented intake; PD intake frequently begins from a court appointment). Not directly evidenced for Karpel/eDefender. Held as variant, not core.
2. **Charges as first-class objects**: whether charges/counts are modeled as discrete objects vs case attributes — not directly evidenced in any fetched page. Not claimed either way.
3. **Conflict-checking mechanics**: trigger points (at person entry vs on demand) and depth (co-defendant chains, witness/victim cross-reference) vary and are only marketing-described for Karpel/eDefender.
4. **Karpel "Comprehensive Financial Tracking"** scope (what financial objects a PD office tracks — expert costs, agency expenses) — not detailed in fetched pages.
5. **Non-US public defense systems** — no sources in this pass.
6. **Tyler / CSG / MTG / CaseWorks products** — unreachable; market-structure claims about them are not made.

## Final Synthesis

A Public Defender Case Management application is the defense agency's system of record for representing indigent clients: it anchors everything on the represented client, organizes work into defense cases identified by the court's cause number, paces the work by court events, and manages the work through assignment of each case to a responsible defender whose caseload is visible and reportable. Around that core, mature products add conflict checking, document generation, discovery/evidence handling, investigation support, per-case timekeeping for workload and funding accounting, justice-partner integrations (courts, sheriff, e-filing), and criminal-justice-grade security. It is defined against three neighbors by the same move: it is one *party's* working system on a court process — the defense party — not the court's neutral docket, not the prosecution's mirror, and not a billing private practice. The economics are structural: no client billing anywhere in the sample; time exists for workload and funding accountability, which is the management problem public defense exists to solve.
