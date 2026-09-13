# Research Notes — Background Check Platform

Research date: 2026-09-06

## Research Goal

Understand what a Background Check Platform actually is as an Application Type: its core objects, the order lifecycle, the consent/compliance machinery, the result and decision model, the actor surfaces (customer-side and candidate-side), and where its boundary sits against neighboring Types (ATS, Identity Verification, Tenant Screening, Employment Verification Platform, people-search services).

## Initial Boundary

Working hypothesis before research:

- A Background Check Platform is software + service that lets an organization order, track, and receive background investigations on individuals (criminal records, identity, employment/education verification, driving records, credit, drug testing) and act on the results.
- Primary users: recruiters / HR / talent acquisition, compliance managers; candidates as secondary actors (consent, data entry, status checking).
- Likely confusions:
  - vs **ATS** — the ATS owns the hiring pipeline; the background check is one regulated step executed inside (or beside) it via integration.
  - vs **Identity Verification** — proving identity claims vs investigating history; the former is typically *one component* of the latter.
  - vs **Tenant Screening Platform** — same mechanics, different industry actor (landlord) and data sources.
  - vs **Employment Verification Platform** — a single screen type (employment history), often continuous/income-oriented; the Background Check Platform composes many screen types.
  - vs **People-search / public-records sites** — no consent gate, no organizational permissible purpose, no adverse-action machinery.

## Research Questions

1. What are the core objects (candidate/subject, order, package, screen, report, result)?
2. What is the standard order lifecycle from initiation to decision?
3. What screen types exist and how are they bundled?
4. What role does candidate consent/disclosure play, and how is it captured?
5. How are results delivered and semantically graded (clear vs needs review)?
6. Who makes the hiring/eligibility decision — the platform or the customer?
7. What adverse-action / dispute machinery exists?
8. How does the platform integrate with ATS/HRIS systems?
9. What roles exist on the customer side and the candidate side?
10. How do product forms differ (API-first vs full-service enterprise vs SMB self-serve)?

## Representative Products

| Product | Philosophy | Customer tier | Rationale |
|---|---|---|---|
| Checkr | API-first platform, developer-oriented; dashboard + hosted candidate flow | mid-market/tech, volume | Richest public operational documentation (API docs describe objects + lifecycle explicitly) |
| Sterling (now First Advantage) | Full-service global enterprise screening, lifecycle-organized service catalog | enterprise, global | Market leader; broad service taxonomy; strong compliance positioning |
| HireRight | Global enterprise screening, high-volume workflows, ATS-integration-first | enterprise, global, staffing | Distinct integration posture (70+ ATS/HCM integrations); DOT/transportation strength |
| GoodHire | Self-serve SMB; pre-bundled packages; candidate-visible results | SMB → mid-market | Different customer tier and product philosophy; candidate-view parity is notable |

## Sources

Fetched 2026-09-06 (Tier 1/2, official):

- Checkr — https://checkr.com (root; product lines Workforce/Mortgage/Tenant/Trust/Personal; screening-type catalog in footer nav)
- Checkr — https://docs.checkr.com (API documentation: screening process, resources, packages, invitations, adverse actions, webhooks)
- Sterling / First Advantage — https://www.sterlingcheck.com (root; services by lifecycle: Identity-First / Pre-Hire / Post-Hire; industries; candidate hub; API docs at apidocs.sterlingcheck.app listed but not fetched)
- HireRight — https://www.hireright.com (root; services; integrations; candidate help center at support.hireright.com listed but not fetched)
- GoodHire — https://www.goodhire.com (root; screening services; packages; compliance features; personal checks)

Not fetched (recorded as limitation): Checkr Help Center dashboard guide articles, Sterling API docs, HireRight candidate help center, First Advantage help site (help.fadv.com). Assertion strength adjusted accordingly; no precise operational details inferred from memory.

## Product A — Checkr

### Key observations (Evidence Layer A unless noted)

**Standardized screening process (docs.checkr.com, "Understand the screening process")** — six steps:

1. Customer requests a background check.
2. Candidate is presented with and signs disclosures and authorizations, and submits PII (hosted apply flow: candidate enters own PII; custom flow: customer collects and passes PII via API).
3. Checkr conducts an SSN Trace and collects associated addresses (name/address history used to scope subsequent searches; out-of-place data triggers candidate outreach for confirmation).
4. Checkr runs searches/verifications based on the requested Packages (search scope may expand to counties from address history).
5. Checkr applies compliance filters based on customer settings and candidate's residence to determine which records are shown; returns a finalized report.
6. If there is a record, the customer Engages or Adverse-Actions the candidate "based on an individualized assessment". **Checkr explicitly does not make the determination on the customer's behalf.**

**Core objects (API resources)**: Candidate, Report, Package, Invitation, Geo, Program, Assessment, Subscription, Continuous Check, Adverse Action, Adverse Item, Verification, Document, Driver License, Professional License, School, Employer, Node/Hierarchy (multi-entity org structures), Form I-9, Webhook, Candidate Story, Report Tag, Report ETA.

**Report results**: `clear` and `consider` are the default results. Clear = no items requiring consideration; Consider = items require review. "With both Clear and Consider reports, customers must decide whether or not to engage a candidate."

**Screening-type catalog (API "Screenings" section)**: SSN Trace; National / County / State / Federal Criminal Search; Federal District Criminal; Federal Civil; Federal District Civil; Sex Offender Registry; Global Watchlist; Motor Vehicle Report; Drug & Alcohol Clearinghouse; FMCSA PSP; Education Verification; Employment Verification; Personal/Professional Reference Verification; Professional License Verification; International Criminal/Education/Employment/Watchlist/Identity Document Validation/MVR/Adverse Media; FACIS; Identity Data Evaluation; Social Media Screening.

**Workflows for order entry**: (1) Checkr Dashboard (invite candidates by email, or manual order where customer certifies offline consent); (2) Checkr-hosted candidate experience (API-triggered or dashboard-triggered email invitation → hosted apply flow → auto-created report); (3) self-hosted candidate experience (customer owns UX + compliance obligations).

**FCRA/compliance machinery**: credentialing with permissible purpose (business identity, EIN; credit checks additionally require onsite inspection per bureau requirements); required UI components for self-hosted flows — PII collection, FCRA consumer-rights summary acknowledgement, disclosure form on its own page with no extraneous information, state-specific disclosures (e.g., CA, WA DMV release), authorization form with ESIGN-compliant eSignature, upload of consent document; proof-of-consent storage requirements (PDF with date/time/IP).

**Adverse action**: Adverse Action resource (create/list/cancel, per-report), Adverse Item resource, adverse-action webhook events.

**Post-hire**: Subscriptions and Continuous Checks resources; continuous check webhook events.

**Roles**: Learning-center learning paths exist for Recruiters, Adjudicators, and Program Administrators.

**Candidate surface**: candidate.checkr.com portal; phone used for candidate authentication; `copy_requested` flag triggers an automatic copy of the report to the candidate's email.

**Multi-vertical reuse**: the same company operates Workforce, Mortgage (income/employment/asset verification — via a separate acquired product line), Tenant, Trust (platform-user criminal/ID/driver intelligence), and Personal (consumer-initiated verified profile) lines. The Workforce line is the Background Check Platform proper; Tenant/Trust/Personal are the same engine re-aimed at different audiences (see Boundary Findings).

**Misc (L3 precision — keep out of final doc)**: invitation validity window of 7 days with 24-hour reminder cadence; staging accounts with mocked candidate profiles; customer counts differ between docs ("over 10,000") and homepage ("140K+ businesses") — marketing numbers not relied upon.

## Product B — Sterling (now First Advantage)

### Key observations (Evidence Layer A unless noted)

**Service taxonomy organized by screening lifecycle** (root nav):

- *Identity-First*: Digital Identity ("confirm identity before the screening process even begins").
- *Pre-Hire*: Criminal Record Checks; Civil Court Records; Global Checks; SSN Trace; Credit Checks; Credit + Liens + Judgments; Due Diligence; Executive Investigations; Drug & Occupational Health; Verification Checks (employment); Motor Vehicle Records; Fingerprinting; Reputational & Risk Compliance (sanctions); Social Media Screening.
- *Post-Hire*: Form I-9 / E-Verify; Criminal monitoring; Drug & Occupational Health monitoring; MVR monitoring; Medical License monitoring.
- *Solutions*: Global Screening (200+ countries & territories); Contingent Workforce screening.
- *Technology*: Candidate Experience (Candidate Hub); Client Experience; Reports & Analytics; Integrations; Sterling API; Compliance Tools.

**Positioning**: "Trust in a changing world"; combined First Advantage scale figures (80,000+ organizations, 200M+ screens annually, ~2/3 of Fortune 100) — marketing figures, not relied upon structurally.

**Candidate side**: "My Background Check" candidate portal entry; Candidate FAQs; candidate support for screening status.

**Industry breadth**: construction, education, energy, entertainment, financial, franchise, gig economy, government, healthcare, hospitality, manufacturing, media, nonprofit, retail, staffing, technology, transportation.

**Criminal description (Evidence A, marketing page)**: "searches of local and federal court records, sex offender registries, global sanctions, and international criminal records databases". Drug & health screening "supported by an in-house Medical Review Officer".

**Cross-product commonality note**: Sterling's Identity-First → Pre-Hire → Post-Hire organization is independent evidence that identity anchoring precedes screening and that post-hire monitoring is a mature extension (Evidence Layer B when combined with Checkr's Continuous Checks).

## Product C — HireRight

### Key observations (Evidence Layer A unless noted)

**Positioning**: "Background screening for fast, compliant hiring at scale"; "high-volume screening workflows"; "Stay compliant across regions and regulations".

**Service catalog (root page)**: County Criminal (felony/misdemeanor); U.S. Employment Eligibility Verification (Form I-9 and E-Verify); Global ID Check ("validates candidate's passport or national identity document to determine if it's authentic"); Global Criminal Search; Global Employment Verification; Healthcare Statewide Criminal Check; Drug & Alcohol Testing ("instant and lab-based testing options for pre-employment and ongoing screening needs"); Extended Workforce Screening (online solution for managing screening for extended/contingent workforce).

**Integration posture**: "70+ ATS & HCM integrations" named as a primary differentiator; partner logos (ATS/HCM/payroll vendors). "Only unified global platform in the industry" (vendor claim).

**Candidate side**: Candidate Help Center for "background check status" and "obtain a copy of your report" — candidate has visibility and report-copy rights.

**Regulated verticals**: DOT/FMCSA strength per customer review on the site ("standard for DOT/FMCSA backgrounds, motor vehicle records"); driver-risk partnership (SambaSafety) for post-hire monitoring.

**Scale claims**: 85M+ people screened annually; 200+ countries; ~50% of Fortune 100 — marketing figures, not relied upon structurally.

## Product D — GoodHire

### Key observations (Evidence Layer A unless noted)

**Self-serve posture**: "Need to run a few checks right away? Get up and running in minutes"; pre-bundled packages or custom packages "by job role or client"; central dashboard to "manage checks across many locations, departments, divisions, or clients".

**Dashboard**: "at-a-glance results and status updates"; candidates "can view their results in the same simple, mobile-optimized format available to you" — candidate result parity is explicit.

**Compliance**: "FCRA-certified, US-based support team"; in-house compliance experts; FCRA compliance features page; background checks organized by state (state laws map); employer forms library.

**Screening services**: criminal background checks, MVR, employment drug tests, education verification, employment verification; claims "100+ screening services" (marketing figure).

**SMB→enterprise gradient**: same platform marketed to large organizations with "most modern API" and "pre-integrated with ATS/HRIS tools".

**Personal checks**: consumer-initiated "run a background check on yourself" exists as an adjacent offering under the same brand.

**Candidate flow (Evidence B with Checkr)**: candidate supplies own info and consent through a hosted flow; both parties get status updates ("we keep you both updated about the status of your employment background check").

## Cross-product Comparison

| Dimension | Checkr | Sterling/First Advantage | HireRight | GoodHire | Evidence |
|---|---|---|---|---|---|
| Initiator of screening | customer (API/dashboard/invite) | customer | customer | customer | A+A+A+A → B |
| Identified candidate/subject as central record | Candidate object | candidate record (implied by candidate hub) | candidate (implied) | candidate | A+A+B+B |
| Consent/disclosure gate before execution | explicit, per FCRA (disclosure own-page, authorization eSignature, consumer-rights summary) | compliance machinery central ("confirm identity before screening begins"; compliance tools) | "compliant hiring" central | FCRA-certified support; employer forms; state rules | A+A+A+A → B |
| Identity anchoring step | SSN Trace + identity data evaluation | Identity-First (Digital Identity) | Global ID Check | SSN trace (educational content) | A+A+A+B |
| Package of screens | Packages resource, per-package required PII | pre-hire services composed per program | services composed | pre-bundled packages + custom | A+A+B+A → B |
| Screen catalog: criminal (multi-jurisdiction), identity, verifications (employment/education/license), MVR, credit, drug/health, watchlist/sanctions, social media | yes | yes | yes | yes (subset claimed as 100+) | A+A+A+A → B |
| Results returned as report w/ status + outcome | report.status/result (clear/consider) | reports & analytics | report + status | results + status in dashboard | A+A+B+A → B |
| Customer makes engage decision; vendor does not decide | explicit ("Checkr does not make this determination") | implied by advisory positioning | implied | implied | A+B+B+B |
| Candidate participates: receives invite, enters PII, consents, tracks status, gets copy | yes (hosted apply flow, candidate portal, copy_requested) | yes (Candidate Hub, status) | yes (status, report copy) | yes (own info, sees results) | A+A+A+A → B |
| Adverse-action machinery | Adverse Action + Adverse Item resources | compliance tools (not itemized in fetched pages) | not directly observed | FCRA compliance features (not itemized) | A+B+B+B |
| ATS/HRIS integration | API + integrations; partner program | integrations + API | 70+ ATS/HCM integrations, core selling point | pre-integrated ATS/HRIS + API | A+A+A+A → B |
| Post-hire / continuous monitoring | Continuous Checks + Subscriptions | Post-Hire monitoring family | ongoing drug testing + driver monitoring | not observed | A+A+A+B |
| Multi-entity / client structures | Nodes/Hierarchy | contingent workforce solutions | Extended Workforce Screening | manage across locations/departments/clients | A+B+B+A |
| Product form | API-first platform | full-service enterprise | enterprise global, integration-first | self-serve SMB | L2 variance |

## Canonical Model (abstraction result)

### L0 — Defining Invariant (minimal)

A Background Check Platform exists where all of the following hold:

1. **Organization-initiated screening order on an identified individual** — a requesting organization (employer in the dominant case) orders an investigation about a specific, identified person.
2. **Subject-authorized execution** — the individual's disclosure/consent/authorization is captured before the investigation runs (legally mandated in the type's primary markets; without it the product degrades into people-search/data-broker territory, which is a different Type).
3. **Composed screens executed against records and data sources** — the order bundles specific screen types (criminal searches, verifications, registry/watchlist checks, driving records, etc.) executed against courts, registries, bureaus, employers, schools, licensing authorities.
4. **Returned findings report** — the outcome is a report of findings (per-screen results, filtered for jurisdictional reporting rules), not an identity assertion or a skill score.
5. **Customer-side eligibility decision** — the platform returns findings; the engage/no-engage (or equivalent eligibility) decision remains with the requesting organization, supported by the platform's compliance workflow.

Remove #1 → it becomes a consumer data-broker/people-search service. Remove #2 → it loses the legal structure that defines it (not operable in its primary markets). Remove #3 → it is a generic data-vendor lookup, not composed screening. Remove #4 → no deliverable exists. Remove #5 → it becomes an automated decisioning/credit-scoring type rather than a screening-report platform.

### L1 — Common Mature Structure

- **Screening packages** — pre-bundled or custom bundles of screen types, typically scoped by role/industry/jurisdiction; package determines both the screens run and the PII the candidate must supply.
- **Identity anchoring step** — SSN trace / ID document validation / identity data evaluation run first to confirm identity coherence and derive name/address history used to scope subsequent searches.
- **Screen-type catalog** — criminal (county/state/federal/national/international), civil, sex-offender registry, global watchlist/sanctions, MVR, employment verification, education verification, professional-license verification, reference checks, credit, drug & occupational health testing, social-media screening.
- **Candidate-facing flow** — invitation, own-PII entry, consent signing, document upload, status tracking, and (commonly) access to the report or a copy.
- **Order status tracking + turnaround estimates** — orders progress through pending/processing states visible to both customer and candidate; ETAs are surfaced.
- **Jurisdictional compliance filters** — records shown are filtered per the candidate's work location and customer settings (fair-hiring/ban-the-box style rules).
- **Adverse-action workflow support** — when findings may drive a negative decision: pre-adverse notice, waiting window, final notice, dispute/reinvestigation handling; compliance artifacts retained.
- **Adjudication support** — review/assessment tooling for deciding engage/no-engage on Consider-type results (explicitly a customer responsibility).
- **ATS/HRIS integration + API** — background checks are executed inside a hiring workflow; integrations and APIs are first-class.
- **Customer dashboards + reporting/analytics** — order queues, statuses, turnaround metrics, program-level views.
- **Multi-entity support** — hierarchies/locations/departments/clients (staffing, franchise, high-volume operations).

### L2 — Variant / Optional Structure

- **Post-hire continuous monitoring / rescreening** (criminal, MVR, drug, license monitoring).
- **Drug testing orchestration** (lab-based, instant, MRO review) — adjacent but commonly bundled.
- **Work-eligibility objects** (Form I-9 / E-Verify in US products).
- **Fingerprinting** coordination.
- **Executive due diligence / adverse media / executive investigations**.
- **Industry vertical re-aims of the same engine**: tenant screening (landlord-initiated), platform/marketplace trust screening (criminal+ID at booking time), mortgage/income-employment verification, personal (consumer-initiated) checks.
- **Regional regimes** (per-country criminal-record schemes, e.g., UK/EU/Canada variants; not directly researched in this pass — see Uncertainties).
- **Product-form packaging**: API-first developer platform vs full-service enterprise vs self-serve SMB.
- **Regulated-vertical depth** (DOT/FMCSA transportation, healthcare sanctions/FACIS).

### L3 — Vendor-specific Structure (Research Notes only)

- Checkr: `clear`/`consider` result vocabulary; Invitation object with expiry + reminder cadence; Geo/Program/Node objects; Candidate Stories; Assessments resource; MCP documentation; multi-vertical product lines under one brand; staging accounts with mocked candidates.
- Sterling/First Advantage: "Identity-First" lifecycle naming; Candidate Hub; Executive Investigations; Fingerprinting; Medical License Monitoring; in-house MRO.
- HireRight: Extended Workforce Screening; Healthcare Statewide Criminal Check; SambaSafety driver-risk partnership; "unified global platform" claim.
- GoodHire: state-laws map; personal self-check offering; candidate-view parity as differentiator; "100+ services" claim.

## Rejected Findings

- "Background Check Platform = criminal records only" — rejected; verifications, registries, MVR, credit, drug/health are equally structural in the sample.
- "The platform decides if a candidate passes" — rejected; the sample explicitly keeps the decision with the customer. Adjudication assistance ≠ decisioning. (An automated-decision product would be drifting toward a different Type.)
- "API-first is the defining form" — rejected; full-service and self-serve forms predate and coexist with API-first packaging. Packaging is L2.
- "FCRA (US) mechanics are the Type" — rejected as *defining* detail; the *concept* (consent gate, disclosure, adverse action, dispute) is cross-jurisdictional, but specific US procedure names belong to one regulatory regime. Final doc keeps the concept, not the regime detail.
- Marketing scale claims (screens/year, customer counts, Fortune penetration, turnaround marketing stats) — rejected as evidence for structure.

## Boundary Findings

| Neighboring Type | Relationship | Distinction criterion ("remove/keep what?") |
|---|---|---|
| Applicant Tracking System / ATS | container vs step | ATS owns the requisition→candidate→pipeline workflow; the Background Check Platform owns the regulated order→consent→screens→report→adverse-action lifecycle executed inside one hiring step. Remove the consent/report/adverse-action machinery → it's just an ATS candidate record. The two are typically integrated. |
| Identity Verification (§15) | component vs whole | Identity verification asserts "this person is who they claim" (documents/biometrics/data checks). A background check platform *includes* an identity-anchoring step but its deliverable is a findings report about the person's history used for an eligibility decision. Remove history investigation → it's pure IDV. |
| Employment Verification Platform | one screen vs composition | Employment verification (and continuous income/employment data) is a single screen type; the Background Check Platform composes many. Same record-target (employers), different object scope. |
| Tenant Screening Platform (§17) | vertical re-aim | Same engine and lifecycle (order→consent→screens→report→decision), different initiating actor (landlord), different data emphasis, different regulatory framing. Remove the employment purpose/actors → tenant screening; the directory keeps them as separate leaves. |
| People-search / data-broker services | no consent, no purpose gate | Consumer-facing record lookup without subject authorization, organizational permissible purpose, or adverse-action machinery is a different Type (not in this directory branch). |
| Candidate Assessment Platform | records vs competence | Assessment measures skills/fit; background check investigates records/history. Different objects despite shared candidate-flow surfaces. |
| HR Compliance Management | policy vs investigation | HR compliance manages policies/training/cases; no per-individual records investigation or reporting agency role. |

## Uncertainties

1. **Adjudication tooling depth** is directly observed only at Checkr (Assessments resource; Adjudicator role). Its universality is inferred (B), not confirmed per-product.
2. **Adverse-action precision** (exact notice sequence, waiting windows, dispute timelines) was not fetched per-product in this pass; final doc describes the workflow shape without numeric windows.
3. **International/regional schemes** (e.g., country-specific criminal-record disclosure regimes) not directly researched; global coverage asserted by vendors but not verified operationally.
4. **Drug-testing orchestration depth** (in-house lab vs network) observed via marketing descriptions only.
5. Sterling's post-acquisition client experience is in transition (sites consolidating into First Advantage); observed pages may mix both brands.

## Final Synthesis

The Background Check Platform is best understood as a **regulated investigation-orchestration application**: an organization orders a composed screen on an identified individual; the individual's authorization gates execution; identity anchoring scopes the search; composed screens run against courts, registries, bureaus and verifiers; jurisdictional filters shape the returned report; and the customer — never the platform — makes the eligibility decision on the findings, supported by adverse-action and dispute machinery. Everything else (packages, candidate portals, integrations, monitoring, drug testing, verticals) is mature structure or variant layered on this spine. The Type's strongest negative boundary is against people-search services (no consent/purpose gate) and pure identity verification (no history investigation); its strongest structural coupling is to the ATS, inside whose hiring flow the background check is a step.
