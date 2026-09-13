# Research Notes — Court E-filing Platform

Research date: 2026-09-07
Leaf: Court E-filing Platform (DIRECTORY §24 Government, Public Sector & Civic)
Slug: court-e-filing-platform

## Research Goal

Understand, from real products, what a Court E-filing Platform actually is: the objects it manages, the lifecycle of a filing, the roles on both sides (filer and court), the rules that govern submission and acceptance, and its boundaries against neighboring Types — above all the Court Case Management System, whose research pass (same date) flagged this leaf for joint boundary review. Produce a vendor-neutral Application Document that a non-user could read and correctly imagine how court e-filing works.

## Initial Boundary

Working hypothesis at start:

- Core: the intake channel through which court documents are submitted electronically — a packaged submission, routed to the court, passing a court-controlled review gate (accept/reject), with fees and notifications attached, and accepted filings handed into the court's case record.
- Primary users: two-sided — filers (attorneys, legal staff, self-represented litigants, agencies) on one side; court clerks/reviewers on the other.
- Nearest neighbors suspected at start: Court Case Management System (the flagged joint review), Legal Docket Management (law-firm meaning), Legal Document Automation, eDiscovery, Government Service Portal, court payment portals, public records access (PACER-like).
- Known unknowns: the exact architecture poles (EFSP marketplace vs court-run portal vs CMS-bundled); whether the review gate belongs to the e-filing platform or the CMS; how fees/refunds work; non-US coverage.

## Research Questions

1. What is the core object — what exactly is "a filing" as the system sees it?
2. What does a submission consist of (documents, case identification, parties, fees)?
3. Who reviews submissions and what are the accept/reject/return mechanics?
4. How do fees, refunds, and fee waivers work?
5. What is the relationship to the court's case management system (docketing handoff)?
6. What are the market architectures (EFSP/EFM marketplace, court-run portal, CMS-bundled)?
7. What value-added services cluster around filing (service of process, eService, courtesy copies)?
8. What rules constrain documents and filings (format, size, redaction, deadlines, mandatory vs voluntary)?
9. What varies by filer segment (attorney vs pro se vs agency) and by jurisdiction?
10. Where are the boundaries against neighboring Types?

## Representative Products

| Product | Operator / origin | Why sampled | Evidence quality |
|---|---|---|---|
| eFileTexas.gov (Texas OCA) | State-run official e-filing system with certified EFSP marketplace; state-provided EFSP hosted by Tyler | Tier-1 official portal: full three-party flow, EFSP model, reviewer side, fees, mandatory e-filing | Tier-1 official FAQ + program pages |
| CM/ECF (US federal judiciary) | Government-built; filing bundled with case management | The bundled pole; canonical docket-centric model; court-issued credentials | Tier-1 official FAQ (uscourts.gov) |
| Green Filing | Independent commercial EFSP, 9 US states | Independent EFSP pole; value-add services; fee structure; multi-state | Tier-2 product site + FAQ |
| One Legal (InfoTrack US) | Commercial EFSP + litigation support, CA/NV | EFSP-with-services pole; rejection/resubmission workflow; fee disbursement; support-center documentation | Tier-2 product pages + support center |
| TrueFiling (ImageSoft) | Court-developed vendor product; deployable as EFSP and/or EFM | The architecture pole that names both sides (EFSP/EFM, ECF 4.0); clerk review workflow | Tier-2 product pages |
| Tyler eFile & Serve Review Queue | Court-side review application (Tyler-hosted, used by Texas reviewers) | The court-side review surface: envelopes, review queue, accept/reject mechanics | Tier-2 official product documentation (version-updates/help) |

Market context: Tyler Technologies' Odyssey File & Serve is the state-provided EFSP in Texas (hosted at efiletx.tylertech.cloud; support at odysseyfileandserve.zendesk.com) — confirmed via the official eFileTexas State EFSP page. tyler.com itself was unreachable in the sibling CMS pass (404 ×2, abandoned per network rule); Tyler evidence here rests on the eFileTexas official pages and Tyler-hosted review-application docs.

Unreachable sources (abandoned after 1–2 attempts, per network rule): nycourts.gov/efile (403 — NYSCEF court-run portal pole not directly documented), content.tylerhost.net review-help-landing (404), support.onelegal.com Re-File article direct URL (404; category page fetched instead).

## Sources

Fetched 2026-09-07:

1. eFileTexas.gov — Home: https://efiletexas.gov/
2. eFileTexas.gov — FAQs: https://efiletexas.gov/faqs.htm
3. eFileTexas.gov — Service Providers: https://efiletexas.gov/service-providers.htm
4. eFileTexas.gov — Information for Reviewers: https://efiletexas.gov/reviewers/reviewers.htm
5. eFileTexas.gov — State Provided EFSP: https://efiletexas.gov/Service-Providers/StateEFSP.htm
6. United States Courts — FAQs: CM/ECF: https://www.uscourts.gov/court-records/file-a-case-cm-ecf/faqs-case-management-electronic-case-files-cm-ecf
7. Green Filing — Home: https://www.greenfiling.com/
8. One Legal — Home: https://www.onelegal.com/ ; Court Filing product page: https://www.onelegal.com/products/filing/
9. One Legal Support Center — Court Filing category: https://support.onelegal.com/en_US/court-filing
10. TrueFiling (ImageSoft) — Home: https://www.truefiling.com/
11. Tyler Technologies — eFile & Serve Review Queue version updates: https://content.tylerhost.net/docs/ReviewApp/Help/version-updates.html

Reused from the same-day sibling pass (research/court-case-management-system.md): Journal Technologies eFile-it observations (fetched 2026-09-07 from journaltech.com) — a vendor-side e-filing product integrated with a court CMS.

## Product A — eFileTexas.gov (Texas OCA)

### Key observations (Tier-1 official)

- Definition of the flow [A]: "Electronic filing (or eFiling) allows Filers and Courts to process documents and fees online. eFileTexas manages the flow of information among Filers and Clerks."
- Three-step canonical flow [A]:
  1. Filer submits documents — after selecting a certified EFSP, filers log on to the provider's site and file to any participating Texas court.
  2. EFSP delivers to the court — EFSPs "validate that the required data elements are completed at the time of submission as well as calculate filing fees and court costs" and electronically deliver to participating courts.
  3. Clerks accept or return — clerks review; on acceptance they "provide an electronic timestamped copy of the documents"; if something is wrong the clerk may "return your submission for correction. Any associated fees will be refunded."
- EFSP definition [A]: "applications run by independent companies that collect filings from Filers and transmit them to eFileTexas. Some EFSPs offer value added services beyond the state provided EFSP."
- EFSP marketplace [A]: ~25 certified providers listed in tiers (free e-filing / free trial / additional services with costs); state-provided EFSP is free. Shared credential model: "Once you register with a service provider, you do not need to re-register should you choose to use another provider. You may simply log in with your existing username and password."
- Mandatory e-filing [A]: mandatory for attorneys filing civil, family, probate, or criminal cases in the Supreme Court, Court of Criminal Appeals, Courts of Appeals, and all district and county courts; non-attorneys encouraged; some JP courts permit.
- Reviewer side [A]: dedicated Reviewer Portal (Tyler-hosted); official guides include "How to Return a Filing to the Filer for Correction and Work the Resubmitted Filing", "How to Initiate a Refund of the State Consolidated Fee", "Auto-Accept & Press Review Tool" (auto-accept vs manual review modes), court financial setup (merchant IDs, bank confirmation), infrastructure guidelines.
- eService [A]: "documents are electronically served to other parties in a case via e-mail. Using this option, you can track when each party received and opened the filing." Can be used without filing a document ("eFileTexas may be used to electronically serve documents between parties without filing the document through the courts").
- Fees [A]: state EFSP free but "all electronic submissions with associated court costs are subject to a convenience fee" (credit card processing fee 2.89%); commercial EFSPs may charge additional fees; filing fees set by the legislature; support is provided by each EFSP.
- Pro se support [A]: Guide-and-File self-help services to prepare and submit frequently filed documents; after eFiling into a case, filers may begin receiving email delivery of opposing parties' future filings and court notices (orders, hearings).
- Availability [A]: 24/7 submission; "Check your local court rules for the court review timelines and schedules."
- State EFSP value-adds [A]: free basic e-filing and e-service; access to file-stamped copies; online tracking and proof of delivery; 24/7 filing and access to electronically filed documents.

## Product B — CM/ECF (US federal judiciary)

### Key observations (Tier-1 official)

- Definition [A]: CM/ECF is the Case Management/Electronic Case Files program — it maintains electronic case files and offers electronic filing of court documents over the Internet. Filing and case management are one program (the bundled pole).
- Record structure [A]: case file = docket sheet + all documents filed in the case; parties, judge, court staff, and public can review simultaneously.
- Auto-docketing [A]: "Attorneys filing over the Internet automatically create docket entries, and docket sheets are updated immediately when documents are filed."
- Notification [A]: Notice of Electronic Filing emailed to the filer and all registered participants immediately after each electronic filing, with hyperlinks to the document and the docket sheet; litigants receive one free copy of each electronically filed document through the notice link.
- Access control [A]: filing requires a court-issued login and password; each court decides to whom it issues filing credentials (principally attorneys, U.S. Trustees, bankruptcy trustees; some courts permit pro se litigants and bankruptcy claimants).
- Document rules [A]: PDF-only (chosen to retain pagination/formatting/fonts); two utility programs verify document integrity (one at filing, one running on a preset schedule to verify documents have not changed since filing).
- Redaction rule [A]: rules require filers to redact personal identifiers (all but last four digits of SSN/taxpayer ID, birth month/day, minors' names, financial-account numbers, home addresses in criminal cases); the filer is responsible; login requires an acknowledgment that cannot be skipped.
- Fees [A]: no added fees for filing electronically (existing court filing fees apply); public access via PACER is fee-based (10 cents/page, capped at the equivalent of 30 pages; transcripts and docket sheets exempt; opinions and calendars free).
- Legal basis [A]: federal rules authorize courts by local rule to permit or require electronic filing; most courts have issued authorizing local rules plus procedures.
- Availability [A]: at the court's option, registered attorneys can file 24/7 "right up to the filing deadline"; training per court; an attorney trained in one court may be authorized to file in another at that court's discretion.
- Coverage [A]: district, bankruptcy, and appellate courts; 41M+ cases, 500M+ documents, 700k+ attorneys filing electronically (system facts).

## Product C — Green Filing

### Key observations (Tier-2)

- Positioning [A]: independent e-filing service provider across nine states (CA, GA, IL, IN, MD, NV, TX, UT, VA); "single-screen e-filing" with live chat/phone/email support.
- Filing features [A]:
  - PDF conversion — upload word-processing documents, converted to text-searchable PDFs.
  - File-stamped documents — "Once accepted, your file stamped documents will be attached to your confirmation email."
  - Case summary views — "View basic case and party information, judge assignment, and a register of e-filing activity on your case."
  - Electronic service — complimentary e-service and tracking with a filing; identify service contacts.
  - Mail service (certified/first-class, extra fees); detailed reporting (filing activity + fees + client matter numbers); email notifications; filing summary emails; detailed filing receipts.
- Efficiency features [A]: party address book, default court/case type, default plaintiff, client matter number enforcement, custom case names, filtering by case/attorney/client, attorney service firm accounts, secured support staff accounts.
- eFile by Email [A]: send documents as email attachments to an assigned address linked to the account; filings enter drafts.
- Auto-File [A]: "automatically fills in the required fields using information from your legal documents, like your Complaint, Petition, Answer, or Motion" (user verifies before submission).
- Fees [A]: standard court filing fees per state schedule; courts may add payment-processor fees, "e-filing manager (EFM) fees", court technology fees, other county-mandated fees; Green Filing charges a provider fee on accepted submissions, waived when a court-approved fee waiver applies; optional services (process serving, courtesy copy delivery, certified mail) cost extra.
- Document constraints [A]: PDF required; per-document size limits vary by state (7–35MB); total submission size varies (15–100MB); no limit on document/page count within size limits; all documents in a submission must pertain to a single case.
- Competitive context (testimonials, weaker evidence) [B]: filers compare against the court-appointed/state provider; "edit and re-file rejected documents rather than starting over"; filing a whole package vs one document at a time.

## Product D — One Legal (InfoTrack US)

### Key observations (Tier-2)

- Positioning [A]: court-approved EFSP in all enabled California superior courts and select Nevada courts; bundles eFiling with service of process, court delivery, eService, courtesy copies, sheriff delivery, locator, concierge.
- Filing workflow [A]: online ordering and status tracking; matter-centric organization ("Matters tab" — case information, documents, order statuses, invoices by matter); court fees paid upfront on the filer's behalf with itemized invoicing for client billing.
- Rejection handling [A]: "Re-File" feature "streamlines the resubmission of rejected court filings without repetitive data entry. Available in all eFiling courts" (full and partial resubmission per support center).
- Physical filing [A]: print, assemble, and deliver to the court any eFiling-exempt documents; concierge service (experts handle filing/service/delivery).
- Bundles [A]: "Case Initiating Filing + Serve + File" (eFiling, service of process, and eFiling the proof of service in one transaction); "Subsequent Filing + eService"; "Court Filing + Courtesy Copy Delivery".
- Support-center topic map (Tier-2, article titles — evidence of the operational surface) [A]:
  - Rejection/resubmission: "Why did the court reject my filing?", "How to Use Re-File to Resubmit Rejected Filings".
  - Court returns: "How do I retrieve conformed copies and filed-endorsed caption pages?", "When can I expect my conformed copies?".
  - Architecture: "How do I connect to my state's electronic filing manager (EFM)?", "What is eFileCA?" (court technology vendor connection), "How do I add an attorney to the EFM for eFileCA?".
  - Fees: statutory court fees, convenience fees, court-mandated technology fees, fee waivers with complaints/petitions, fee disbursement, jury fees, appeals fees.
  - Deadlines: "Documents eFiled by 11:59 p.m. are considered filed that day" (California courts).
  - Document requirements: PDF conversion from many formats, text-searchable OCR, electronic bookmarks, character limits, file size limits, e-signature options, sealing confidential documents, amended documents.
  - Tracking: order number vs court transaction number (two identifiers); order status; cancellation where permitted.
  - Case participants in the filing workflow; eService list management; exemptions from mandatory eFiling; per-court information pages (deadlines, service levels, reservation numbers).

## Product E — TrueFiling (ImageSoft)

### Key observations (Tier-2)

- Positioning [A]: "court-developed solution" — web-based electronic filing system for attorneys, paralegals, court reporters, and self-represented filers; 24/7 from any device; case initiation or filings into existing cases.
- Architecture (the key structural evidence) [A]: "TrueFiling can be deployed as an electronic filing service provider (EFSP) that provides a fresh interface for integrating with any existing ECF 4.0-conformant electronic filing managers (EFM). TrueFiling is also available as an EFM that supports connection with multiple EFSPs so that filing processes are centralized. All our customers have chosen to deploy it for both an EFSP and EFM."
- CMS handoff [A]: "Once filings are approved, that data is electronically sent to your case management system for docketing, so you don't have to worry about re-keying the same information." Integrative with any case or document management system.
- Clerk review workflow [A]: "the TrueFiling system enables the court to electronically accept, route, and take action, such as filing signed proposed orders, summons or case initiation requests"; clerks move through filing review; "when a file is processed, the filers will receive an automatic notification"; multiple clerks can simultaneously view the same document; bottlenecks visible in operations.
- Filer surfaces [A]: initiate cases or submit filings; case search (view case information, add a party as case contact, file to the case); review history (payment receipts, copies of submitted filings, status of filings being processed).
- Multi-jurisdictional [A]: one login grants access to various courts; the platform tracks each court's individual CMS, fees, and case types.
- Modules [A]: Electronic Commerce module (view/purchase court-approved filings list, receive certified copies); TrueSign and TrueCertify; Law Enforcement Agency Portal (LEAP) for criminal eFilings integrated with a paperless prosecutor solution; TrueFiling Review for fee reports.

## Product F — Tyler eFile & Serve Review Queue (court-side review application)

### Key observations (Tier-2, official Tyler product documentation)

- The court-side review application is named "eFile & Serve Review Queue" / "Review Application"; its users are "reviewers" (court staff) [A].
- Core objects [A]: the **Envelope** (Envelope Lookup page, Envelope Details page) containing **filings** (filings list, Filing Details panel); within a filing, a **Lead Document** plus **Auxiliary Documents** in submission order; proposed-order drafts; charge information (criminal offense date/time ranges); document viewer; comments panel; "Image Auto stamp".
- Review queue mechanics [A]: the queue auto-refreshes on a configurable interval (backend-configured per client, 1–5 minutes range; set to 3 minutes in the observed release) so incoming envelopes display promptly; reviewers page through filings lists and return to the correct page after viewing details.
- This confirms the envelope/filing/lead-document data model on the court side, mirroring what EFSPs collect on the filer side.

## Cross-product Comparison

| Dimension | eFileTexas (state portal) | CM/ECF (federal) | Green Filing (EFSP) | One Legal (EFSP) | TrueFiling (EFSP+EFM) | Tyler Review Queue (court side) |
|---|---|---|---|---|---|---|
| Architecture | state system + certified EFSP marketplace; state EFSP free | filing bundled with case management | independent EFSP across 9 states | EFSP + litigation-support services | deployable as EFSP and/or EFM; ECF 4.0 conformance | court-side review application over the EFM |
| Core submission unit | filing via EFSP; data elements validated at submission | document filed into case file (docket sheet + documents) | submission of documents for one case (single-case rule) | order (filing transaction) with documents | filing/envelope; case initiation or subsequent | envelope → filings → lead + auxiliary documents |
| Case identification | case category/type + filing type dropdowns; existing-case filing type | case number under court-issued login | county + case number lookup; case type defaults | matter-centric; case participants; reservation numbers | case search; add party as case contact | charge information; case context panels |
| Review gate | clerks accept or return for correction; fees refunded on return | (filing auto-docketed; court controls credentials and local rules) | court reviews; provider fee only on acceptance | court rejects; Re-File resubmission | court "electronically accept, route, and take action" | review queue; accept/reject/return; auto-accept mode |
| Proof of filing | electronic timestamped copy; file-stamped copies | Notice of Electronic Filing with document link; free copy | file-stamped documents attached to confirmation email | conformed copies / filed-endorsed caption pages | payment receipts, copies, status in review history | image auto-stamp |
| Fees | court fees + 2.89% convenience fee; EFSP fees vary | no added e-filing fees; court filing fees apply; PACER for access | court fees + EFM fees + technology fees + provider fee (waived on fee waiver) | court fees disbursed upfront; itemized invoicing; convenience/technology fees | payment receipts; fee reports (Review) | refund initiation (state consolidated fee) |
| Notifications | email delivery of opposing filings + court notices after eFiling | NOE emailed to filer + registered participants immediately | filing summary emails; email notifications | status tracking; eService open tracking | automatic notification when file processed | queue auto-refresh (court side) |
| Service on parties | eService with received/opened tracking; usable without filing | service by electronic means if parties consent (rules) | complimentary e-service + tracking; mail service | eService; service of process; File+Serve+File bundles | (not observed) | (not observed) |
| Pro se support | Guide-and-File self-help; pro se encouraged | some courts permit pro se | (self-help positioning) | self-representation resources section | self-represented filers named | (n/a) |
| Multi-court | any participating Texas court from one EFSP login | per-court registration (training portable at court's discretion) | 9 states, one provider | CA + NV courts | one login, various courts | per-client deployment |
| Mandatory e-filing | mandatory for attorneys (civil/family/probate/criminal); exemptions | per local rule (most courts) | (state-dependent) | mandatory vs voluntary courts documented; exemptions | (court-dependent) | (n/a) |

### Evidence layer summary

- A (directly observed): all product scope statements, the eFileTexas three-step flow and reviewer guides, CM/ECF FAQ operational rules, Green Filing feature/fee FAQ, One Legal product + support-center topics, TrueFiling EFSP/EFM architecture statement, Tyler Review Queue object model.
- B (cross-product commonality): packaged submission with lead + supporting documents; case identification (new vs existing case); submission-time validation and fee calculation; court-controlled accept/reject gate; returned-for-correction loop with fee refunds; file-stamped/conformed copies as proof of filing; status tracking and notifications; eService; multi-court single-account access; CMS docketing handoff on acceptance.
- C (canonical inference): the Type is the intake machinery of the court record — see Final Synthesis.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

A Court E-filing Platform is the intake channel into a court's case record, in which:

1. an identified filer assembles a packaged electronic filing — document(s) plus case identification (a new case or an existing case) — and submits it to a specific court through the platform;
2. the submission is routed to the court and passes through a court-controlled review gate;
3. the court accepts or rejects the submission, and the outcome is returned to the filer;
4. accepted filings enter the court's case record (handed off for docketing).

Framing property: it is intake machinery — not the court's system of record, not a drafting tool. The platform exists to move documents across the filing gate; the record of what happens afterward belongs to the Court CMS.

Remove any of these and the Type collapses: no packaged submission bound to a case → a generic document upload portal; no court-controlled review gate → a file-transfer service; no accept/reject outcome returned to the filer → a drop box, not filing; no entry into the court's case record → a messaging system, not court filing.

### Historical / market-sample check

Pre-digital courts ran filing through the clerk's counter: the filer presented documents, the clerk reviewed conformity, stamped "filed", collected fees, and the documents entered the case file. The e-filing platform is the digital analog of that window — submission, review, stamp, fee, record. A minimal court-run upload portal with manual clerk review satisfies the L0 core without EFSP marketplaces, eService, auto-accept modes, multi-court accounts, or value-added service bundles. CM/ECF (early 2000s) also fits without any marketplace layer. The definition therefore does not depend on the modern US EFSP-marketplace implementation. Historical check: passed.

### L1 — Common Mature Structure (standard capabilities in mature products)

- Structured submission data: court, case category/type, filing/document codes (dropdown vocabularies), party information, service contacts; validation of required data elements at submission time.
- Fee machinery: filing-fee calculation at submission, payment collection, convenience/processing/technology fees, EFSP service fees, refunds when a submission is returned, fee-waiver handling.
- Proof of filing: electronic timestamp / file-stamped copies / conformed copies / Notice of Electronic Filing returned to the filer.
- Status tracking and notifications: submission received, accepted/rejected with reasons, e-service receipts; email delivery of subsequent case activity in some products.
- Rejection handling: rejection reasons, return-for-correction, resubmission without re-entering data (re-file features).
- eService: electronic service of filed documents on other parties with delivery/open tracking; sometimes usable standalone.
- Case context for filers: case search, case summary (parties, judge assignment, register of e-filing activity), filing history and receipts.
- New-case initiation and subsequent filings into existing cases as distinct flows.
- Document preparation aids: conversion to text-searchable PDF, bookmarks, e-signature support, format/size validation.
- Court-side review application: review queue with incoming submissions, envelope/filing detail views, accept/reject/return actions, auto-accept modes, refund initiation, fee reports.
- CMS integration: on acceptance, filing data and documents transmitted to the court's case management system for docketing (auto-docketing in the bundled model).
- Multi-court access under one filer account (multi-jurisdictional filing).

### L2 — Variant / Optional Structure

- Architecture: EFSP marketplace (many certified providers against a state/court EFM) vs single court-run portal vs filing bundled into the CMS (CM/ECF) vs one vendor deploying both EFSP and EFM.
- Mandatory vs voluntary e-filing regimes (attorney-mandatory with pro se encouraged is a common pattern); exemptions for specific documents/case types; paper filing retained for exempt documents.
- Court coverage: single court, county, statewide, or national systems; civil/family/probate/criminal/traffic mixes; appellate e-filing.
- Filer segments: attorneys and firm staff; self-represented litigants (guided document preparation); agencies (law-enforcement filing portals); process-serving firms.
- Value-added bundling: service of process, courtesy-copy delivery, physical filing of exempt documents, concierge (human-mediated) filing, certified-copy purchase, document download/docket monitoring.
- Payment models: free state provider + transaction convenience fees; commercial provider fees; court fees disbursed upfront by the provider with itemized invoicing.
- Regional: the researched sample is US-centric (state EFSP model, federal direct model); other jurisdictions run their own national/court portals — structure assumed similar but not directly verified.

### L3 — Vendor-specific Detail (research notes only)

- Tyler Technologies: Odyssey File & Serve as Texas's state-provided EFSP (efiletx.tylertech.cloud, OfsEfsp UI; support at odysseyfileandserve.zendesk.com); eFile & Serve Review Queue with Envelope Lookup/Details pages, Filing Details panel, Lead/Auxiliary document ordering, configurable queue auto-refresh (1–5 min; 3 min in observed release), Image Auto stamp, proposed-order drafts, charge/offense-time panels; texas-review.fileandserve.tylertech.cloud reviewer portal.
- eFileTexas: 2.89% credit-card convenience fee; Guide-and-File self-help for pro se; reviewer guides for return-for-correction and state-consolidated-fee refunds; Auto-Accept vs Press Review Tool; shared EFSP credential model (register once, reuse across providers); ~25 certified EFSPs in three pricing tiers.
- CM/ECF: PDF-only; court-issued logins; mandatory redaction acknowledgment at login; two integrity-verification programs (at filing + scheduled re-verification); PACER 10-cents/page with $3 per-document cap (transcripts/docket sheets exempt; opinions/calendars free); rollout timeline (bankruptcy 2001, district 2002, appellate 2005); 41M+ cases / 500M+ documents / 700k+ attorneys; appellate Java plug-in (legacy-era detail).
- Green Filing: eFile by Email; Auto-File (auto-population from document content, user-verified); single-screen filing; 9 states; provider fee waived on court-approved fee waivers; per-document size 7–35MB and total 15–100MB varying by state; party address book; client-matter-number enforcement; attorney service firm accounts; monthly billing/auto-pay of provider fees.
- One Legal: Re-File (full/partial resubmission of rejected filings); Matters tab; court fees paid upfront and disbursed; concierge; File+Serve+File bundles; eFileCA/EFM account connection; order number vs court transaction number; California 11:59 p.m. same-day filing cutoff; "By Fax" stamp for non-originals; per-court info pages.
- TrueFiling: EFSP+EFM dual deployment (all customers deploy both); ECF 4.0 conformance; LEAP law-enforcement portal for criminal e-filings; TrueSign/TrueCertify; Electronic Commerce module (certified copies); TrueFiling Review fee reports.
- Journal Technologies (from sibling pass): eFile-it as a separate product — prepare/submit/route/review filings; separate review system for accept/reject; automatic fee assessment and work-queue routing; built-in case initiation forms; EFSP whitelisting; OASIS ECF specification compliance; integration with the court's CMS.

## Vendor-specific Findings

- The market's dominant structural pattern is the **two-sided intake architecture**: a filer-side submission service (EFSP) and a court-side filing manager/review gate (EFM + review queue), integrated by a standard (OASIS ECF 4.0 observed at TrueFiling and eFile-it). The same vendor may sell either side or both (TrueFiling; Tyler).
- The **bundled pole** (CM/ECF) collapses both sides into one program: filing, docketing, and public access in one system. This does not merge the Types — it confirms that the intake function is separable in principle and only sometimes co-deployed.
- The **marketplace pattern** (eFileTexas) adds a governance layer: the state certifies multiple competing EFSPs, provides a free baseline provider, and shares credentials across providers — competition happens on the filer side, while the court side (review) remains single.
- Value-added services (service of process, courtesy copies, physical filing, concierge) cluster on the commercial EFSP side and are explicitly "beyond the scope of e-filing documents into court cases" (Green Filing's own fee framing) — evidence that they are adjuncts, not the core.

## Boundary Findings

1. **Court Case Management System (joint review — resolved).** The CMS is the court's record of reference (case, parties, docket, hearings, outcomes); the e-filing platform is the intake machinery (submission, review gate, accept/reject). The market realizes the seam both as separate integrated products (EFSP/EFM model; Journal eFile-it) and as one bundled program (CM/ECF). Tests both ways: remove the case record/docket/calendars from an e-filing platform and a functioning e-filing platform remains (submission → review → accept/reject); remove intake from a CMS and a functioning CMS remains (register cases, maintain dockets, schedule hearings, record outcomes). The CMS research's flagged question — "is e-filing inside the Type or separate?" — resolves as: separate Type, mandatory integration seam at acceptance (auto-docketing). Both documents record the seam.
2. **Legal Docket Management (§11 sibling).** Same word, different object: law-firm docketing tracks the firm's deadlines and filing obligations; court e-filing moves documents across the court's filing gate. A firm's docketing system may *trigger* a filing, but it does not submit it.
3. **Legal Document Automation / Drafting.** Drafting produces the document; e-filing submits it. Auto-population features (Green Filing Auto-File) blur the edge but remain submission-time assistance, not document production.
4. **Process Serving / eService.** Service on other parties is a distinct legal act with its own rules; e-filing platforms commonly bundle it, and it can be used standalone (eFileTexas FAQ: eService without filing). Bundled ≠ definitional.
5. **Government Service Portal.** Generic citizen-to-government submission lacks the case binding, the court-controlled review gate, the fee schedules, and the case-record handoff. Remove those and e-filing degrades into a generic portal — the sharpest upward boundary.
6. **Court payment portals (fines/fees).** Payments for existing obligations (tickets, fines, installments) vs filing fees attached to a submission. Adjacent; different object (payment vs filing).
7. **Public records access (PACER-like).** Retrieval vs submission — two sides of court infrastructure, different users and flows. CM/ECF itself separates them into two programs (CM/ECF files; PACER reads).
8. **eDiscovery.** Party-to-party litigation data exchange and review vs submission into the official record.

## Uncertainties

- Tyler's main site unreachable (404 in the sibling pass; not retried here) — Tyler evidence rests on the official eFileTexas state-EFSP page and Tyler-hosted review-application documentation; no claims about Tyler's full product portfolio.
- NYSCEF (New York court-run portal) returned 403 — the court-run portal pole is covered by eFileTexas instead; NY-specific mechanics not asserted.
- Non-US e-filing (UK CE-file, Canada, Australia, etc.) not directly researched; regional generalization kept at "other jurisdictions run their own portals" without structural claims.
- Exact review timelines (how fast clerks must act) are jurisdiction-specific and were not asserted; eFileTexas explicitly defers to local court rules.
- Fee amounts observed (2.89% convenience fee; PACER pricing; Green Filing size ranges) are directly observed single-source facts kept at research-notes level.
- Appellate e-filing depth (brief cycles, specific appellate rules) not documented beyond CM/ECF's appellate program existence.
- Auto-accept policies (which filing types qualify) observed as a mode name only; qualification rules not documented.

## Final Synthesis

A Court E-filing Platform is the intake machinery of the court record: the channel through which an identified filer packages documents with case identification, submits them to a specific court, passes a court-controlled review gate, and receives the outcome — acceptance (with a file-stamped/conformed copy and entry into the court's case record) or rejection (with reasons and, commonly, a fee refund and a correction loop). The platform is two-sided by nature: filers prepare, validate, pay, submit, track, and serve; clerks queue, inspect, accept, return, and refund; and on acceptance the filing is handed to the court's case management system for docketing. The market deploys this machinery as certified EFSP marketplaces over a court filing manager, as single court-run portals, or bundled into the case management system itself — but in every deployment the defining structure is the same: submission → review gate → accept/reject → into the record. Everything else — eService, service of process, courtesy copies, multi-court accounts, auto-accept, guided pro se preparation, value-added litigation services — is standard capability or variant, not the definition.
