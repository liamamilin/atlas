# Research Notes — Court Case Management System

Research date: 2026-09-07
Leaf: Court Case Management System (DIRECTORY §24 Government, Public Sector & Civic)
Slug: court-case-management-system

## Research Goal

Understand, from real court-operated software, what a Court Case Management System (Court CMS) actually is: its objects of record, its lifecycle, its roles, its rules, and its boundaries against neighboring justice-sector and legal-application Types. Produce a vendor-neutral Application Document that a non-user could read and correctly imagine how court case processing software works.

## Initial Boundary

Working hypothesis at start:

- Core: the court-side system of record for cases moving through a court — case registration, parties, the official docket/register of case events, hearing scheduling (calendars/listing), judgments/dispositions, and the financial follow-through (fines and fees).
- Primary operator: the clerk of court / court registry staff, with judicial officers as the decision-making users and justice partners as consumers.
- Nearest neighbors suspected at start: Court E-filing Platform, Jury Management System, Prosecutor Case Management, Public Defender Case Management, Legal Docket Management (law-firm meaning of "docket"), Probation & Parole Management, Public Sector Case Management, Police Records Management System, Corrections Management System, Law Practice Management / Legal Matter Management.
- Known unknowns: exact case model (how case types, parties, charges, hearings, and outcomes relate); whether e-filing and payments are inside the Type or separate; regional differences beyond the US; appellate handling.

## Research Questions

1. What is the core case record and what identifies a case?
2. What is the docket in a court system, and how does it relate to filings and documents?
3. How does a case enter the system (civil filing, criminal referral, citation)?
4. How do hearings get scheduled and what does "listing" involve?
5. What is recorded as the outcome, and what is generated from it (orders, judgments, notices)?
6. Who uses the system and what surfaces does each role get?
7. How are fines, fees, and payment plans handled?
8. How do justice partners (prosecutors, defenders, law enforcement, motor-vehicle agencies) interact?
9. What is public access, and how is it provided?
10. What varies across jurisdictions, court levels, and deployment models?

## Representative Products

| Product | Operator / origin | Why sampled | Evidence quality |
|---|---|---|---|
| Journal Technologies eCourt | US commercial vendor (subsidiary of Daily Journal Corp.); trial and appellate courts, US/Canada/Australia | Deep court CMS pole; court-specific feature vocabulary; public portal suite split (eFile-it / ePay-it) | Tier-1/Tier-2 product pages (marketing + capability descriptions) |
| Neumo Court / FullCourt Enterprise | US commercial vendor; statewide deployments (Montana 192 trial courts) | Statewide shared-platform pole; cloud migration; justice-partner access; judge view; payments | Tier-2 product page + Tier-2 case study (detailed operational claims) |
| CM/ECF + PACER (US federal judiciary) | Government-built; Administrative Office of the US Courts; district/bankruptcy/appellate courts | Federal/national pole; the canonical docket-sheet-centric model; public-access layer as a separate program | Tier-1 official FAQ + program pages (uscourts.gov) |
| HMCTS CJS Common Platform | UK government-built; HM Courts & Tribunals Service criminal courts | Non-US regional pole; explicit published domain language (case/defendant/charge/hearing/listing/results/NOWs) | Tier-1 official architecture/domain documentation (hmcts.github.io) |

Market context only (unreachable, no claims): Tyler Technologies (Odyssey) — commonly cited US market leader; tyler.com returned 404 on two attempted entry points and the source was abandoned per the network-restriction rule.

Terminology anchors (independent of vendors): Cornell LII Wex definitions of "docket" and "court docket"; US Courts' description of the case file ("a docket sheet and all documents filed in a case").

## Sources

Fetched 2026-09-07:

1. Journal Technologies — home page: https://www.journaltech.com/
2. Journal Technologies — eCourt product page: https://www.journaltech.com/ecourt
3. Journal Technologies — Public Access Solutions (eFile-it / ePay-it): https://www.journaltech.com/public-access-solutions
4. Neumo — Justice Solutions (Court/Jury/Probation): https://neumo.com/products/justice-solutions/ and Court page: https://neumo.com/products/justice-solutions/court/
5. Neumo — Montana Supreme Court case study: https://neumo.com/resources/montana-supreme-court-unifies-courts-on-shared-platform/
6. United States Courts — Court Records: https://www.uscourts.gov/court-records
7. United States Courts — FAQs: CM/ECF: https://www.uscourts.gov/court-records/file-a-case-cm-ecf/faqs-case-management-electronic-case-files-cm-ecf
8. HMCTS — The domain language (CJS Common Platform): https://hmcts.github.io/cjs-common-platform/architecture/domain-language.html
9. Cornell LII Wex — docket: https://www.law.cornell.edu/wex/docket ; court docket: https://www.law.cornell.edu/wex/court_docket

Failed sources (abandoned after 1–2 attempts, per network-restriction rule): tyler.com/courts/ (404), tyler.com/solutions/courts-justice/ (404), civica.com justice page (404), bsasoftware.com courts page (404), hmcts.github.io/ccd/ (404).

## Product A — Journal Technologies eCourt

### Key observations (Evidence layer A where noted)

- Self-describes as "a configured Case Management System (CMS)" for "appellate, superior, municipal, traffic, probate, and drug courts" [A].
- Scope statement: "case information management, document handling, hearings, outcomes, financials, and more" [A].
- Court-specific named features: "Judge View, Court Proceedings, Orders & Outcomes, Statutes/Act Management" [A].
- Configurability is emphasized as the central property: administrators tailor workflows and judicial needs; the architecture adapts "to evolving court processes and legislative changes" [A].
- Role-based access model: "judicial staff but also the public, litigants, attorneys, and other interested parties … based on their roles (authenticated in the system)" [A].
- Public portal: 24/7 access, electronic filing, online payments, and calendar reservations [A].
- Court types include trial and appellate courts, administrative law, and tribal governments [A].
- Vendor's own product split (boundary evidence): eCourt (courts) is sold separately from eProsecutor (prosecutors), eDefender (public defenders), eSupervision (probation, parole, court services, pretrial, diversion), eFile-it (e-filing), ePay-it (payments portal) [A].
- eFile-it details [A]: prepare/submit/route/review filings; a separate system for reviewing and accepting/rejecting filings; automatic fee assessment and work-queue routing; built-in case initiation forms; EFSP whitelisting; OASIS Electronic Court Filing (ECF) specification compliance; integration with the court's CMS.
- ePay-it details [A]: payments for traffic tickets, fines and fees, restitution, collections, payment-plan installments, garnishments; payments applied to the case immediately; DMV information relay; clerk-window credit-card readers as an omni-channel option.

## Product B — Neumo Court (FullCourt Enterprise)

### Key observations

- Product family: Justice = Court / Jury / Probation as separate product lines [A] (boundary evidence).
- Court product scope: "case, hearing, and collections management into a single, unified system"; features named as Integrated Case Management ("scheduling to judgment tracking"), Public Access Portal ("search cases, submit documents, make payments online"), Configurable Dashboards, Secure Information Sharing "built on NIEM standards" with law enforcement, probation, and other agencies [A].
- Montana Supreme Court case study [A, vendor-published operational claims]:
  - 192 trial courts on one shared cloud platform, replacing locally hosted legacy systems (an early DOS-based system, then a Windows-based system, 100+ servers).
  - Case search by docket number, date, or party name; real-time status tracking and version-controlled document management.
  - Judge view claim: "A judge can see if there are bonds or warrants outstanding, any dispositions, changes to the case — all within seconds."
  - Criminal dispositions delivered to the DMV "within a day or two" via API, replacing mailed handwritten reports; license suspensions/reinstatements reported near-real-time.
  - Access for county attorney and public defender offices into the shared platform (justice-partner access).
  - Built-in status tracking of filings through the review pipeline ("judges, clerks, and administrative staff can monitor where a filing stands").
  - Role-based permissions and logged actions (audit trail).
  - CitePay payment integration inside FullCourt Enterprise; online portals and in-court POS terminals; funds routed/deposited to county accounts with real-time reconciliation and deposit reporting.
  - Jury management planned as a separate Neumo Jury expansion.

## Product C — CM/ECF + PACER (US federal judiciary)

### Key observations (Tier-1)

- Definition [A]: "CM/ECF — the Case Management/Electronic Case Files program — is a joint program of the Administrative Office of the U.S. Courts and the federal courts to replace old case management systems" — it maintains electronic case files and offers electronic filing over the Internet.
- Record structure [A]: "The main type of record the federal courts create and maintain is a case file, which contains a docket sheet and all documents filed in a case."
- Simultaneous access [A]: "Parties, the judge, court staff, and the public can review the case file simultaneously."
- Auto-docketing [A]: "Attorneys filing over the Internet automatically create docket entries, and docket sheets are updated immediately when documents are filed."
- Notification [A]: a Notice of Electronic Filing is emailed to the filer and all registered participants immediately after each electronic filing, containing hyperlinks to the document and the docket sheet.
- Access control [A]: filing requires a court-issued login; each court decides to whom it issues filing credentials (principally attorneys, U.S. Trustees, bankruptcy trustees; some courts permit pro se litigants).
- Public access [A]: dockets and documents are publicly viewable via PACER, subject to court orders, policy, or court limitations; court opinions and court calendars are free to view.
- Document rules [A]: PDF-only; two utility programs verify document integrity (one at filing, one running on a preset schedule to verify documents have not changed since filing).
- Privacy rule [A]: rules require filers to redact personal identifiers (SSN/taxpayer-ID digits, birth month/day, minors' names, financial-account numbers, criminal home addresses); the filer is responsible; login requires acknowledgment.
- Court calendars are a separately viewable artifact [A] ("no charge to view court opinions and court calendars").
- Records governance [A]: national record disposition schedules govern most judiciary records including case files (retention).
- Scale context (vendor/system facts — research notes only): 41M+ cases, 500M+ documents, 700k+ attorneys filing electronically; bankruptcy rollout 2001, district 2002, appellate 2005.
- Coverage of court levels [A]: district (trial), bankruptcy, appellate — the same program family manages all three.

## Product D — HMCTS CJS Common Platform (UK)

### Key observations (Tier-1, published domain language)

- Domain-first design: "the words the courts use are the words the code uses" [A].
- Case model [A]:
  - A prosecution case "is what a prosecuting authority sends to the court. It is the container everything else hangs from."
  - A defendant is the person or organisation the case is brought against; a case can have several.
  - An offence is what is alleged; offence definitions are held centrally as reference data. A charge is the case-level concept that carries an offence — "the definition is shared and its use is not."
- Hearings and listing [A]:
  - A hearing is "an occasion on which the court considers a case."
  - Cases are listed into hearings: "matching cases to courtrooms, dates and the people required" — described as its own discipline.
- Results [A]:
  - Results are "what the court decided, recorded against a charge or a defendant"; structured rather than free text, "which is what makes them actionable"; they drive what happens next, including which documents are produced.
  - Result definitions form a centrally maintained catalogue of outcomes with per-outcome prompts; they change over time, so questions about results are date-sensitive.
- Court output documents [A]:
  - NOWs (notices, orders, warrants) are the documents a court produces after a hearing and "what a person outside the court actually receives"; a single hearing can generate several, addressed to different recipients.
  - Generation rule: "the document is generated from the decision rather than typed up afterwards."
- Reference data [A]: offence definitions, result definitions, prompts, court and prosecutor details — platform behavior lives in data, can change without a release, and "why did it do that" questions are answered by the reference data in force at the time.

## Cross-product Comparison

| Dimension | eCourt (Journal) | FullCourt Enterprise (Neumo) | CM/ECF + PACER (federal) | CJS Common Platform (HMCTS) |
|---|---|---|---|---|
| Operator side | Court (trial + appellate; US/CA/AU) | Court (statewide; 192 courts) | Federal courts (district/bankruptcy/appellate) | Criminal courts (England & Wales) |
| Case as container | case information management; configured per court | case management, docket number, party name search | case file = docket sheet + all filed documents | prosecution case = the container everything hangs from |
| Parties | litigants, attorneys, interested parties, role-authenticated | party-name search; partner access (county attorney, public defender) | parties, judge, court staff, public review simultaneously | defendant (person or organisation; multiple per case) |
| Docket / register | document handling; orders & outcomes | docket-number search; status tracking of filings | docket sheet; auto docket entries; updated immediately on filing | case events realized as hearings + recorded results (terminology differs) |
| Hearings / scheduling | hearings; public calendar reservations | scheduling; hearing management | court calendars (publicly viewable) | hearings; listing = matching cases to courtrooms/dates/people |
| Outcomes | outcomes; orders | judgment tracking; dispositions | decision date on docket; case closure | results recorded against charge/defendant; result-definition catalogue |
| Documents | document handling; MS Office integration | centralized document management, version control, real-time tracking | case file holds all filed documents; PDF; integrity verification | notices/orders/warrants generated from recorded results |
| Intake | e-filing (eFile-it separate product integrated with CMS); case initiation forms | filings with review pipeline tracking | CM/ECF filing with auto-docketing; court-issued logins | prosecution case received from the prosecuting authority |
| Financials | financials in product; ePay-it (fines, fees, restitution, payment plans, collections, garnishments) | collections; CitePay payments to county accounts; reconciliation | filing fees; PACER access fees | financial penalties appear as notices (evidence of penalty machinery, depth not documented in fetched source) |
| Public access | public portal (search, e-filing, payments, calendar reservations) | public access portal | PACER (fee-based; opinions and calendars free) | (not covered in fetched source) |
| Partner sharing | API integrations; eSeries inter-product integration | NIEM-based secure sharing; DMV API; prosecutor/defender access | notification to registered case participants | case received from prosecutor; reference data includes prosecutor details |
| Configurability | central selling point (workflows, case types, legislative change) | configurable dashboards; policy change adaptation | per-court local rules and credential decisions | reference-data-driven behavior; result definitions change over time |
| Deployment | hosted/cloud (SaaS pole via ePay-it; eSeries platform) | cloud shared platform (from on-prem legacy) | government-operated national system | government-built cloud platform |
| Governance/audit | auditing capability; role-based authenticated access | role-based permissions; logged actions (audit trail) | redaction rules; integrity verification; records disposition schedules | date-sensitive reference data as institutional memory |

### Evidence layer summary

- A (directly observed): all four products' scope statements and feature lists; CM/ECF FAQ operational rules; HMCTS domain language; Neumo case study claims (vendor-published); Journal product splits.
- B (cross-product commonality): case as container; parties; official register/docket; hearings + calendars; structured outcomes; documents attached to cases; role-separated access; public search; financial follow-through; partner integration; configurability/reference data; audit trails.
- C (canonical inference): the Type is "the court's own register of judicial work" — see Final Synthesis.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

A Court Case Management System is the court-operated system of record in which:

1. a case is registered as an identified, typed record (case/docket number under a case type) — the container to which everything attaches;
2. parties (the identified persons/organizations on each side) are bound to the case;
3. the court maintains an official, chronological register of case events — the docket / case register (filings, proceedings, orders, and their dates);
4. court proceedings (hearings) are scheduled: cases are matched to dates, courtrooms, and required participants on the court's calendars;
5. outcomes are recorded as structured dispositions/judgments/results, and case status advances or terminates on that record.

Plus the framing property: it is operated by the court (clerk/registry as day-to-day operator; judicial officers as the deciding users), and it is the authoritative record of the court's own process.

Remove any of these and the Type collapses: no case+parties → not court processing; no official event register → a document store or calendar tool, not case management; no proceedings scheduling → a records archive; no recorded outcomes → a tracker, not the record of adjudication; not court-operated → an agency case-management system (prosecutor, defender, probation).

### Historical / market-sample check

Pre-digital courts ran on the paper case file, the docket book (the chronological register of a case's proceedings — the Wex definitions describe exactly this, pre-software), and the printed court calendar. A clerk registering cases by number, binding parties, maintaining the docket, listing matters before a judge, and entering judgment satisfies the L0 core without e-filing, portals, payments integration, cloud, or statistics. The definition therefore does not depend on the modern implementation pattern. Non-US systems (HMCTS: prosecution case / defendant / charge / hearing / listing / results) and government-built systems (CM/ECF) also fit without US-specific vocabulary. Historical check: passed.

### L1 — Common Mature Structure (standard capabilities in mature products)

- Case types as the configurable backbone: civil, criminal, family, probate, traffic, appellate, and specialty case types, each with its own events, forms, fees, and flow.
- Document management bound to the case: registration of filings and generated documents, version control, integrity verification, the case file as "docket sheet + all documents".
- Electronic filing intake with a review gate: submission by attorneys/self-represented litigants, fee assessment, clerk accept/reject review, automatic docket entry on acceptance, notification to case participants.
- Financial machinery: fee schedules, fines, restitution, payment plans, collections, receipts, reconciliation, and reporting of dispositions to motor-vehicle and other agencies.
- Judicial officer (bench) view: a judge-facing case overview — parties, charges, outstanding bonds/warrants, prior dispositions, upcoming calendar.
- Calendars and listing support: judge/courtroom calendars, conflict avoidance, reservation surfaces (public calendar reservations observed in one product).
- Party/attorney records with service lists and notification machinery (notice of electronic filing; email to registered participants).
- Justice-partner access and inter-agency data exchange (prosecutor, public defender, law enforcement, probation, DMV), commonly standards-framed (NIEM, OASIS ECF observed).
- Public access portal: case search, calendars, documents (sometimes fee-based), online payments.
- Reporting/statistics: caseload, age of pending cases, disposition reporting to administrative offices; configurable dashboards.
- Role-based permissions, audit trails, records-retention schedules.

### L2 — Variant / Optional Structure

- Deployment: on-premises legacy → cloud; single-court instance vs statewide shared platform (one platform serving hundreds of courts).
- Court-level emphasis: unified trial courts vs appellate-specific case management vs limited-jurisdiction (municipal/traffic) courts.
- Public-access funding model: free public portals vs fee-per-page public access with free opinions/calendars.
- E-filing architecture: filing machinery inside the CMS vs a separate integrated filing product (EFSP model, OASIS ECF standard).
- Builder: commercial vendor vs government-built (federal/national judiciary programs).
- Regional process vocabulary: US (docket, disposition, judgment) vs UK criminal (listing, results, notices/orders/warrants); underlying structure holds while vocabulary and stage names differ.
- Courtroom-adjacent technology (recording, transcription, remote hearings) — adjacent surfaces, not observed as core in the fetched sources.
- Jury management, probation supervision, prosecutor/defender case handling — sold by the same vendors as separate products (they integrate with, but are not, the court CMS).

### L3 — Vendor-specific Detail (research notes only)

- Journal Technologies: eSeries framework; eCourt named modules (Judge View, Court Proceedings, Statutes/Act Management); ePay-it multilingual support claim (up to 25 languages), FedRAMP-compliant AWS hosting claim, WCAG 2.0 AA / ADA / CJIS / NIST compliance claims; velocity-script configuration.
- Neumo: FullCourt Enterprise product name; CitePay payments; Montana claims (192 courts, dispositions to DMV within 1–2 days vs weeks by mail, record search in under a minute vs hours, hundreds of field servers reduced to six); 50%/40% paperwork/admin-time reduction quote (jury program manager, NM AOC); NIEM-based sharing.
- CM/ECF (official system facts): PDF-only filings; PACER fee of ten cents per page with a per-document cap equivalent to 30 pages ($3.00; transcripts and docket sheets exempt; opinions and calendars free); 41M+ cases / 500M+ documents / 700k+ attorneys; appellate CM/ECF Java plug-in requirement (legacy-era detail); redaction reminder with mandatory login acknowledgment; two integrity-verification programs (at filing + scheduled re-verification); rollout timeline (bankruptcy 2001, district 2002, appellate 2005).
- HMCTS: prosecution-case-centric vocabulary; "NOWs" abbreviation for notices/orders/warrants; domain-first engineering ("the words the courts use are the words the code uses"); behavior change via reference data without releases; date-sensitivity of result definitions.

## Vendor-specific Findings

- The clearest vendor-side structural evidence is the product-split pattern: Journal Technologies ships Court / Prosecutor / Defender / Supervision / Filing / Payments as separate products on one framework; Neumo ships Court / Jury / Probation as separate lines. Neither vendor folds agency-side or jury software into the court CMS. This is strong evidence that the seams in Related Application Types are real market seams, not just taxonomy conveniences.
- Neumo's Montana study shows the statewide pole: the court CMS acts as shared inter-agency infrastructure (prosecutor/defender read access, DMV disposition feeds, county-level payment deposits), i.e., the CMS becomes the case-data hub of the justice system once deployed statewide.
- CM/ECF shows the record-centric pole: the program is named Case Management/Electronic Case Files — the case file (docket sheet + documents) is the object; e-filing and public access (PACER) are programs layered around it.

## Boundary Findings

1. **Court E-filing Platform.** The filing submission channel is separable: eFile-it is a distinct product that integrates with the court's CMS; CM/ECF bundles filing with case management in one program. Test: remove the case record/docket/calendars — a submission-routing system with accept/reject review remains an e-filing platform, not a court CMS. The CMS is the record of reference; e-filing is intake machinery. Flag: the market realizes the seam both as separate products and as one integrated system (CM/ECF) — joint review recommended when the e-filing leaf is processed.
2. **Jury Management System.** Separate products at both suite vendors (Neumo Jury; separate line at Journal's sibling products). Jury operations (summons, qualification, panels, juror pay) center on jurors, not cases; court CMS financials may carry juror-related fee categories, but the jury lifecycle is its own Type.
3. **Prosecutor Case Management / Public Defender Case Management.** Agency-side systems over the same real-world matters, different operator and objective (prosecution decisions / defense representation vs the court's adjudication record). Evidence: vendor product splits; HMCTS "a prosecution case is what a prosecuting authority sends to the court" (the case crosses into the court CMS from outside); Montana partner access goes INTO the court platform (the court record is the shared reference, agencies keep their own systems).
4. **Legal Docket Management (§11 sibling).** Same word, different object: in law-firm software "docketing" means tracking the firm's deadlines and filing obligations; in a court CMS the docket is the court's official public register of case events. Do not merge on the shared term.
5. **Probation & Parole Management.** Post-adjudication supervision of persons; separate products (eSupervision; Neumo Probation); the court CMS records the sentence and moves on; supervision caseloads are not court cases.
6. **Public Sector Case Management.** Generic container for tracked cases without the judicial structures (official docket, hearings/listing, dispositions as legal outcomes, case-type court procedure). Remove the judicial-processing semantics and the court CMS degrades into generic public-sector case management — that is the sharpest upward boundary.
7. **Corrections Management System.** Custody operations (already processed). A court CMS tracks court events but never manages custody; corrections systems track court dates but never adjudicate. Consistent with the corrections pass's recorded boundary ("vs Court CMS: tracks court events, never adjudicates").
8. **Police Records Management System / Law Enforcement Case Management.** Pre-charge records of incidents and arrests; criminal cases in the court CMS begin from charges (filed or referred), not from police incident records.
9. **Law Practice Management / Legal Matter Management.** Private-practice matters and client work vs the court's own register of judicial work; different operator, different object of record.
10. **Government Transparency Portal.** Publishes records; the court CMS manages them (public access portals are a capability of/layer over the CMS, not the Type).

## Uncertainties

- Tyler Technologies (commonly cited market leader) unreachable (404 ×2) — no claims made about its products; the market-leader anchor rests on Neumo's case study mentioning replacement of legacy systems and general market structure, which is weaker. Market-share statements deliberately avoided.
- Financial-module depth in criminal courts (assessments, ability-to-pay, trust accounts) was observed only at the payments-portal level (ePay-it/CitePay) — internal court financial configuration not directly documented in fetched sources; assertions kept at capability level.
- Civil-case lifecycle depth (service of process, case management conferences, discovery entries) not directly documented; the docket-register model from CM/ECF and the case-container model from HMCTS imply it, but stage vocabulary was not verified across civil cases — no stage lists asserted in the final document.
- HMCTS source covers the criminal platform only; civil/family/tribunal case management at HMCTS (separate services) not covered — UK non-criminal variation not asserted.
- Appellate-specific workflows (brief cycles, opinion publication) evidenced only via eCourt's appellate claim and CM/ECF's appellate program existence — depth not documented.
- Numeric limits, stage names, and default values are deliberately absent from the final document; the only numeric facts retained (federal PACER fees, Montana case-study figures) are research-notes-level, directly observed vendor/system facts.

## Final Synthesis

A Court Case Management System is the court's own system of record: the register in which the court opens identified cases under a case type, binds the parties, maintains the official chronological record of events (the docket), schedules cases into hearings on the court's calendars, records the structured outcomes of judicial decisions, and follows through financially and statistically — operated by clerks, used by judges, and exposed in controlled ways to attorneys, litigants, justice partners, and the public. Everything else commonly associated with modern products — e-filing machinery, payment portals, partner APIs, statewide shared platforms, cloud delivery — is standard capability or variant implementation, not the definition. The market realizes the surrounding machinery as either integrated programs (CM/ECF) or separate integrated products (eFile-it, ePay-it, Jury, Prosecutor, Defender, Supervision), which confirms the seams: this Type is the court-side record of adjudication, and neighboring Types are the intake channel, the jury pool, the agencies around the courtroom, and the generic case container.
