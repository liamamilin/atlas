# Research Notes — Legal E-filing Platform

Research date: 2026-09-07
Leaf: Legal E-filing Platform (DIRECTORY §11 Legal, Risk, Compliance & Governance)
Slug: legal-e-filing-platform

## Research Goal

Understand what a "Legal E-filing Platform" actually is as an Application Type, from real products:

- what the core objects are (filing, case, document, party, fee, status)
- who uses it and in what roles
- how the filing workflow actually moves (prepare → submit → clerk review → accepted/rejected → returned copies)
- what rules and constraints govern the flow (court-maintained document types, security levels, fee schedules, file-stamp timing)
- where the boundary lies against court-side systems (EFM / Court Case Management), practice-management suites, and the sibling directory leaf "Court E-filing Platform" (§24 Government)

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the Type is the filer-side platform through which attorneys, staff, and self-represented litigants submit court filings electronically and track the court's accept/reject decision.
- Nearest neighbors suspected: Court Case Management System (court-side), Court E-filing Platform (§24 sibling — possibly the same Type), Law Practice Management System (e-filing as embedded capability), Legal Docket Management, Legal Document Automation (upstream document production).
- Unknowns: whether "legal e-filing" in the market covers only courts or also other authorities (patent office, SEC); whether the US "EFSP" market structure is definitional or incidental.

## Research Questions

1. What is the unit of submission? (envelope / filing / order)
2. What are the two fundamental flows? (initiate new case vs file on existing case)
3. What does the submission contain? (documents, document types, security, parties, filing party, service contacts, fees)
4. What is the status lifecycle, and who adjudicates? (clerk review; accepted / partially accepted / rejected / pending / processing)
5. How do fees work? (court fees, EFM/technology fees, provider fees, processor fees, waivers, pre-authorization, refunds)
6. How does the platform relate to the court's back-end (EFM) and to case data?
7. What is the service (eService / mail / process serving) relationship to filing?
8. What market structures exist? (competing certified EFSPs, state-run portal, court-vendor EFSP, PM-suite integration, concierge)
9. Where is the boundary against court-side systems and the §24 sibling leaf?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Green Filing | independent standalone EFSP, multi-state, price-led, support-led | richest public operational documentation found; documents the full filing workflow step by step |
| One Legal | EFSP + litigation-services bundle (InfoTrack company), California/Nevada | documents rejection handling (Re-File), fee layering, EFM relationship, physical-filing channel |
| FileTime | independent standalone EFSP, multi-state | documents the shared EFM identity layer, document conversion, retention variance, switching between providers |
| MyCase (+ InfoTrack integration) | practice-management suite with e-filing embedded via integration | the "capability inside a PM suite" packaging pole |
| Tyler Technologies (Odyssey File & Serve) | court-technology vendor operating both EFM and the largest EFSP | dominant market position; official docs unreachable — established indirectly (see Sources / Limitations) |

Market-structure context: eFileTexas.gov (official state portal) lists ~18 certified EFSPs for Texas and states that e-filing is mandatory for attorneys in civil, family, probate, and criminal cases; filers must file through an EFSP. This confirms the EFSP model as the dominant US market structure.

## Sources

### Green Filing (all fetched 2026-09-07)

- Homepage — https://www.greenfiling.com/ (features, pricing FAQ, envelope FAQ, file limits, testimonials)
- Texas state page — https://www.greenfiling.com/texas/ ($3 per filing submission; plan tiers Law Firm / Attorney / Individual Pro Se; envelope definition; TX file limits 35 MB per document / 100 MB total)
- Support center — https://help.greenfiling.com/texas (article map: Getting Started, per-state and per-court sections, Odyssey courts)
- "File on an Existing Case" — https://support.greenfiling.com/electronic-filing/file-on-an-existing-case/ (8-step workflow, fee breakdown, pre-authorization, file-stamp rule)
- "Initiate a New Case" — https://support.greenfiling.com/electronic-filing/initiate-a-new-case/ (same 8-step skeleton; court + case type selection; required party roles)
- "Filing Status Screen" — https://support.greenfiling.com/electronic-filing/viewing-filing-history-and-filed-documents/ (statuses, lead document, envelope open/closed service indicator, receipts)

### One Legal (all fetched 2026-09-07)

- Homepage — https://www.onelegal.com/ (services: court filing, process serving, court delivery, locator, file-serve-file, eService, sheriff delivery, concierge; court fees paid upfront; case-centric organization)
- Court Filing product page — https://www.onelegal.com/products/filing/ (court-approved EFSP in enabled CA superior courts + select NV courts; Matters tab; Re-File)
- Support center — https://support.onelegal.com/ (Court Filing category: 61 articles)
- "How to Use Re-File to Resubmit Rejected Filings" — https://support.onelegal.com/en_US/court-filing/how-to-use-re-file-to-resubmit-rejected-filings (full/partial rejection; case initiation vs subsequent; duplicate-resubmission prevention)
- "Why did the court reject my filing?" — https://support.onelegal.com/en_US/court-filing/why-did-the-court-reject-my-filing (clerk rejection messages, one-way communication, partial rejection semantics, Returned list)
- "What fees should I expect to pay when eFiling?" — https://support.onelegal.com/en_US/court-filing/what-fees-should-i-expect-to-pay-when-efiling (statutory court fees, EFM/technology fee, cost recovery fee, convenience fees, eCheck fees, disbursement-on-behalf)
- "What is eFileCA?" — https://support.onelegal.com/en_US/court-filing/what-is-efileca (EFM = court's back-end system; account connection; counties choose their own technology vendor)

### FileTime (fetched 2026-09-07)

- Homepage — https://www.filetime.com/ (EFM shared identity; firm vs single-filer accounts; document converter; monthly invoicing; retention: EFM keeps file-stamped copies 35 days (eFilings) / 7 days (eServices), FileTime 3 years; switching providers without re-registration)

### eFileTexas.gov (state portal, fetched 2026-09-07)

- https://efiletexas.gov/ (mandatory e-filing for attorneys; EFSP requirement; certified EFSP list incl. State Provided EFSP at efiletx.tylertech.cloud, Green Filing, FileTime, InfoTrack, LegalConnect, Rapid Legal, et al.)

### MyCase (fetched 2026-09-07)

- Homepage — https://www.mycase.com/ (practice-management suite positioning)
- "Integrating InfoTrack with MyCase" — https://supportcenter.mycase.com/en/articles/9370184-integrating-infotrack-with-mycase (eFiling + process serving via InfoTrack; orders and expenses synced to the case; returned document syncing; InfoTrack eFiling states listed)

### Tyler Technologies — INDIRECT ONLY (see Limitations)

- tylertech.com product pages: HTTP 403 (2 attempts)
- efile.texas.tylertech.cloud / efsp.tylertech.cloud: transport errors (2 attempts)
- Indirect evidence: eFileTexas.gov lists the State Provided EFSP at efiletx.tylertech.cloud/OfsEfsp; Green Filing's support center maintains dedicated "Odyssey courts" sections (eFileCA, eFileGA, eFileVA, eFileTX) and an "Odyssey Court Submission Failures" article; One Legal's eFileCA article is tagged "tyler"; multiple Green Filing testimonials compare against "Odyssey".

## Product Observations

### Green Filing (evidence layer A unless noted)

**Positioning**: "e-Filing Service Provider" (EFSP) for state courts; operates in CA, GA, IL, IN, MD, NV, TX, UT, VA. Counters on homepage: 23,334,218 documents filed by 176,134 filers (as of fetch date).

**Unit of submission**: "A filing submission, commonly referred to by the court as a filing envelope, is a single submission of documents to the court for a case. A filing submission may contain multiple documents or pleadings as long as they are intended for the same case." (FAQ, homepage + Texas page). File limits are per state (Texas: 35 MB per document, 100 MB total; no page/document-count limit; all documents must pertain to a single case).

**Two fundamental flows**, documented as parallel guides with an identical 8-step skeleton:
1. Initiate a New Case — step 1 = Select Court & Case Type
2. File on an Existing Case — step 1 = Select Case (case already linked to the account, or "Add a Case" to retrieve it from the court's system by case number)

Steps 2–9 shared: Add Documents → Security & Additional Services → (New Case) Parties → Filing Party → Service Contacts → Filing Fees → Review & Submit → Pre-authorization of Fees.

**Document handling**: Document Types are "determined and maintained by the court"; if no exact match, filer selects the closest generic type. Document Description = exact and complete title. Upload auto-converts most native formats (Word, WordPerfect, JPG, PNG, GIF, TIF) to text-searchable PDF; direct Word upload only for document types courts require in Word (e.g., certain proposed orders). The vendor explicitly states it is "prohibited from providing legal advice" on which document type to choose.

**Security**: per-document security level (Public / Confidential; options vary by court and document type). Critical documented warning: electronic service transmits ALL documents in the filing to ALL selected parties regardless of per-document security settings.

**Parties**: court-required party roles (tip box or auto-populated); representing attorneys; "Address Unknown" checkbox; Add Party.

**Filing party**: the party the filer files on behalf of; selected from case parties.

**Service contacts**: eServe recipients (electronic service, complimentary, with tracking); Mail Service (Certified / First Class, additional fees); return address; filers can only edit/delete service contacts they added themselves.

**Fees** (documented breakdown): Court Document Fees (triggered by document type) + EFM Convenience Fee (charged by some courts' E-Filing Managers, covers the EFM software the court uses to receive/review/process e-filings from any integrated provider) + Court Transaction Fee + Provider Service Fee (the EFSP's own per-accepted-filing fee) + Payment Service Fee (~3% credit card or flat up to $1 ACH, charged by the payment processor) + Sales Tax (some states tax the e-filing service). "Confirm Fee Calculation" shows estimated fees computed from case type + document types + additional services. Waiver payment accounts for court-approved fee waivers (not available in all courts). Provider service fees billed monthly separately (Texas page: $3 per filing submission; some counties add a $2 e-filing service fee; ~3% court credit-card convenience fee).

**Additional services** attached to a filing: mandatory fees (court reporter fee, first paper fee) and optional services (certified copies), with quantity; vary by court.

**Review & Submit**: Filing for an Attorney (select/add); Created By (logged-in user); Client Matter/Reference No. (internal); Courtesy Email Notice (unofficial — recipients are NOT served and do not receive conformed copies); Note to Clerk (up to 500 characters where offered); verification checkbox.

**Submission semantics**: "Click the 'Submit Filing' button to send your filing directly to the Court Clerk for review. After all documents are successfully sent, the Court will provide an envelope number and the exact date and time they received your complete submission. This receipt timestamp will be the official file stamp for your accepted documents. For filings submitted after 11:59 PM on weekdays, or anytime on weekends or Court Holidays, the official file stamp will be the next Court business day."

**Status lifecycle**: after submit, status shows "Pending" on the Filing Status Screen; "Court review times vary, typically ranging from a minute to a full business day. Extended pending times might suggest a court backlog. For status inquiries, contacting the Court directly with your filing's Envelope Number is the best approach."

**Filing Status Screen**: displays all filings in the account with status "accepted, partially accepted, rejected, pending, processing, and more"; columns Filing Id / Status / Last Changed / Case Number / Envelope Number; list shows the Lead Document only (click Filing Id for all documents); filter by Filing Id, Client Matter Number, Envelope Number, Filing Batch; My Filings vs All Filings; service envelope icon open/closed (whether service contacts opened the served documents); Case Summary screen via case number (all filings on the case); Print receipts for accepted filings.

**Pre-authorization**: on submission the court initiates a pre-authorization on the payment card for estimated fees; "This pre-authorization is only finalized when your filing is accepted. If the court rejects your submission, the pre-authorization will not be settled and should automatically be removed from your account within 3 to 10 business days following the rejection date" (bank-dependent).

**Rejection handling** (testimonial + support structure): "we can simply edit and re-file rejected documents rather than starting over" (customer testimonial); support center includes court-specific rejection/fix articles and "Odyssey Court Submission Failures and How To Fix Them".

**Court-specific rule encoding**: the support center maintains per-court sections (Alameda, Los Angeles, Riverside, San Diego, Santa Clara; Cook County; statewide guides) covering fee waivers, refunds, document finders, eFiling vs eSubmit, motion spindling (hearing dates), courtesy copies, proposed orders, auto-accepted document types, summons service fees, appeals guides, payment processors, cell-number requirements for unlawful detainer defendants.

**Accounts**: firm accounts with unlimited users (Law Firm plan), attorney plans, Individual (Pro Se) plan (1 user, limited support); secured support-staff accounts; attorney service firm accounts; party address book; default court/case type; require client matter numbers; filter filings by case/attorney/client.

**eFile by Email / Auto-File** (homepage, available in some states): email documents to an assigned address to create drafts; Auto-File "automatically fills in the required fields using information from your legal documents, like your Complaint, Petition, Answer, or Motion" (testimonial: "probably 90 to 95% correct").

### One Legal (evidence layer A)

**Positioning**: "court-approved eFiling service provider in all enabled California superior courts, as well as select Nevada courts"; part of InfoTrack. Services: Court Filing, Service of Process, Court Delivery, Locator, File + Serve + File, eService, Sheriff Delivery, Concierge. "Court fees paid upfront on your behalf." Case-centric organization: "groups every order, document, and invoice tied to a specific case." Audience: "solo practices to AmLaw 200 firms to freelance paralegals."

**Order model**: filings are placed as orders; Orders list with status; Order Details page; order number vs court transaction number as distinct tracking references (article titles). Matters tab: "View all case information, documents, order statuses, and invoices by matter."

**Re-File (rejected filings)**: documented for full and partial rejections, for case initiation and subsequent filings:
- Full rejection of case initiation → Re-File button on Order Details → case initiation workflow with all data pre-populated → correct (party names, documents) → resubmit.
- Partial rejection where a case number was generated → enters the Subsequent Filing Workflow; "Previously accepted documents will remain associated with the case. Only rejected documents need to be corrected and re-uploaded." "Do not re-upload accepted documents, as they are already part of the case record and will be rejected if resubmitted."
- Full rejection of subsequent filing → pre-populated parties, document types, hearing dates, fees → correct → resubmit.
- Duplicate-resubmission prevention: after successful resubmission the Re-File button is disabled and the resubmission timestamp is displayed.
- Bundled process-serving orders associated with rejected filings are updated and resubmitted automatically.
- Physical-filing rejections: handled by the One Legal team directly with the filer (human-mediated channel).
- "Standard filing fees apply. If your filing results in court fees, One Legal will disburse those fees on your behalf and will invoice you once the order is complete."

**Rejection semantics**: "When the court rejects a filing, the clerk may provide a reason for the rejection at the time of processing... attached to the filing or the rejected document via a one-way communication from the court's system. This electronic communication is received and displayed by the One Legal system." Display locations: filing-level "MESSAGE FROM THE COURT CLERK" below the filing status; per-document yellow rows in the Your Files list; email notifications. Partial rejection status label: "Rejected by Court - partial rejection"; accepted documents appear in a "Returned" list. "If no rejection reason is shown... there was no information provided by the court clerk who processed the rejection."

**Fees** (documented breakdown): Statutory court fees — initial filing fee (first paper / case initiation), other filing fees (subsequent filings), other court fees (court reporter, copying official records); "In many cases, the document types you select during the eFiling process will trigger the correct fees... Other types, it will be up to you, the filer, to know which fees are required and add them as necessary." Other court-imposed fees — Court Technology / Court Transaction / EFM Fee ("charged by the court's technology vendor, meaning the company that provides the court's back-end eFiling system with which One Legal connects (i.e. eFile CA)"), Cost Recovery Fee, court/EFM credit-card convenience fee, eCheck fees ($0.25–$1.00 depending on court). "One Legal will pay court fees on your behalf via whichever method carries the lowest fee, usually eCheck."

**EFM relationship**: "In some courts, filers are asked to connect their One Legal accounts to the court's back-end system (also known as the electronic filing manager or EFM) before placing an electronic filing transaction. This creates another extra layer of security and identity verification between the filer and the court." California allows each county to select its own technology vendor; eFileCA (Tyler) is the EFM in a listed set of counties.

**Court Filing knowledge base** (61 articles) covers: required formatting for eFiled documents in CA superior courts; file-size limits; electronic bookmarks for exhibits; text-searchable/OCR requirements; PDF failure troubleshooting; document under seal; exempt-from-eFiling documents and paper submission channel; deadlines ("Documents eFiled by 11:59 p.m. are considered filed that day"); conformed copies and filed-endorsed caption pages; e-signing approaches; eService list management; case portfolio; court reservation numbers (Riverside/LA motion scheduling); Orange County order splitting; JTI courts fee disbursement; character limits; Client Billing Code; lead documents in LASC; filing-party limitations in LASC; judicial officer assignment; appeals fees; fee waiver with complaint; jury fees; "Case Participants" in the filing workflow.

### FileTime (evidence layer A)

**Positioning**: independent EFSP for TX, CA, IN, IL, MD, GA, VA (Themis Solutions).

**Shared EFM identity layer**: "The beauty of the eFiling Manager system is once you register you can then login to any of the service providers and try out their systems." Switching: "You don't have to re-register... Login with your email address and password you used to login with your current efile provider... FileTime will download all your data from eFiling Manager."

**Account model**: firm account with firm administrator; or single-filer account "if you are not a practicing attorney and you are a single filer such as a pro se filer, contract paralegal, court reporter, process server."

**Document converter**: converts uploads to system-required PDF; warns if document security features will cause the filing to fail; orients non-standard dimensions; removes fill-in-the-blank coding on county download forms that cause failures by eFiling Manager; produces text-searchable PDFs.

**Retention variance**: "eFiling Manager, and several other service providers save your file stamped documents only 35 days for eFilings and 7 days for eServices. FileTime saves file stamped copies of both your eFiled and eServed documents for 3 years." (product-specific numbers, kept as example)

**Billing**: monthly invoicing of eFiling and eService submissions (Platinum plan) with detailed report "against which you bill the cases."

**Other**: customizable reporting with Excel export; free fax service; easy-to-print proofs of service; eService-gap workarounds ("There are many shortcomings in the eService side of the eFiling Manager... we've created ways to work around most of them").

### MyCase + InfoTrack (evidence layer A for the integration pattern)

MyCase is a practice-management suite (intake, case management, documents, calendaring, billing, payments via LawPay, client portal, AI). E-filing is not a MyCase-native module; it is delivered through the InfoTrack integration: "InfoTrack integrates with MyCase to connect case and client data you already have with the courts... InfoTrack automates key court filing tasks such as eFiling and process serving and automates tracking these expenses in MyCase... Filing and serving orders in InfoTrack and any associated expenses are automatically synced to the case in MyCase... Improve case organization with returned document syncing." InfoTrack eFiling states: CA, FL, GA, IL, IN, MD, NY, NV, TX, UT; process serving in all 50 states. Activation: create an InfoTrack account and specify MyCase as the firm's CMS.

### eFileTexas.gov (evidence layer A for market structure)

Official state portal: "e-Filing is now mandatory for all attorneys filing civil, family, probate, or criminal cases in the Supreme Court, Court of Criminal Appeals, Courts of Appeals, and all district and county courts. While not required, non-attorney filers are encouraged to file as well." Filers choose an EFSP from a certified list (~18 providers, including the State Provided EFSP operated on Tyler infrastructure at efiletx.tylertech.cloud, plus Green Filing, FileTime, InfoTrack, LegalConnect, Rapid Legal, and others). The portal also lists active courts and a "Reviewers" section (clerk-side review).

### Tyler Technologies (evidence layer B — indirect)

Official surfaces unreachable (403 / transport errors). Established indirectly:
- eFileTexas.gov lists the State Provided EFSP at efiletx.tylertech.cloud/OfsEfsp (Tyler infrastructure hosting a state EFSP).
- Green Filing's support center organizes court documentation around "Odyssey" systems (eFileCA, eFileGA, eFileVA, eFileTX) and maintains an "Odyssey Court Submission Failures" article — i.e., competitors build around Tyler's EFM.
- One Legal's eFileCA article (EFM explanation) is tagged "tyler".
- Customer testimonials on Green Filing/One Legal pages compare their UX against "Odyssey".
Conclusion (qualified): Tyler operates both the EFM layer (Odyssey EFM, e.g., eFileCA) and a filer-facing EFSP (Odyssey File & Serve), and is the dominant court-technology vendor in the US e-filing market. Product-level operational claims about Odyssey File & Serve are NOT directly verified and are not asserted in the final document.

## Cross-product Comparison

| Aspect | Green Filing | One Legal | FileTime | MyCase (+InfoTrack) | Tyler (indirect) |
|---|---|---|---|---|---|
| Market pole | standalone EFSP | EFSP + litigation services | standalone EFSP | PM suite w/ e-filing integration | court vendor: EFM + EFSP |
| Geography | 9 states | CA + NV (e-filing) | 7 states | via InfoTrack: 10 states | many states (indirect) |
| Unit of submission | filing submission / envelope | order (eFiling) | submission | order via InfoTrack | envelope (per competitor docs) |
| Case binding | add case from court system / initiate new case | case portfolio / Matters | cases from EFM | case data from MyCase | Odyssey cases |
| Clerk adjudication | pending → accepted / partially accepted / rejected / processing | order status incl. "Rejected by Court - partial rejection" | via EFM statuses | via InfoTrack | via Odyssey EFM |
| Rejection loop | edit & re-file rejected documents | Re-File with pre-population, duplicate prevention | knowledge-base guidance | via InfoTrack | — |
| Fee machinery | court + EFM + transaction + provider + processor + tax; waivers; pre-auth | statutory + technology/EFM + cost recovery + convenience; disbursement on behalf | monthly invoicing | expense sync to case | — |
| Service | eService (free) + certified/first-class mail | eService + process serving + sheriff + courtesy copies | eService + proofs of service | process serving (all 50 states) | — |
| Document prep | PDF conversion incl. Word/WP/images | format guides, OCR, bookmarks, PDF fixes | converter with failure warnings | documents from MyCase | — |
| User tiers | firm / attorney / pro se | solo → AmLaw 200 | firm / single filer | firms | — |
| Support | live chat/phone/email, per-court articles | support center + concierge | phone/email/chat, training | PM-suite support | — |

**Cross-product commonalities (evidence layer B)**:
1. The filing submission bound to exactly one court case (existing or new) — all sampled products.
2. Clerk adjudication loop with accept/reject (incl. partial rejection) and reasons conveyed back — Green Filing, One Legal, FileTime (via EFM), eFileTexas reviewer model.
3. Court-maintained document types with filer-selected closest match — Green Filing, One Legal.
4. Layered fee structure (court fees + technology/EFM fees + provider fees + processor fees) — Green Filing, One Legal, FileTime (billing), eFileTexas ecosystem.
5. File-stamped / conformed copies returned on acceptance — Green Filing, One Legal, FileTime.
6. Document conversion to court-required PDF — Green Filing, One Legal, FileTime.
7. Electronic service with open-tracking + mail service — Green Filing, One Legal, FileTime.
8. Case-centric organization of filings, documents, invoices — Green Filing (case summary), One Legal (Matters), MyCase (case sync).
9. Firm/organization accounts with roles + pro se single-filer tier — Green Filing, FileTime, One Legal (audience span).
10. Human support as a first-class layer — Green Filing (live chat), One Legal (support team/concierge), FileTime (support-led positioning).

## Canonical Model

### L0 — Defining Invariant (three jointly-held properties)

1. **The filing submission of record** — a prepared unit of one or more documents plus case/party context, submitted electronically to a court through the platform; one submission pertains to one case. (Remove → document delivery/messaging tool.)
2. **Case binding** — every submission is bound to a court case: either an existing case retrieved from the court's records (by case number) or a new case initiated through the platform with the court's required party roles. (Remove → generic government form submission.)
3. **The clerk adjudication loop** — the submission crosses into the court's system and comes back with the clerk's decision: accepted, partially accepted, or rejected (with the clerk's reasons conveyed back through the platform). Acceptance is what constitutes filing (file stamp / conformed copies); rejections are correctable and resubmittable without losing accepted content. (Remove → one-way upload portal; the filing semantics disappear.)

Jointly-held is load-bearing: submission + case binding without adjudication = a document drop; adjudication without case binding = generic e-forms; case binding without submission = a case-inventory tool.

### L1 — Common Mature Structure (standard capabilities)

- Fee machinery: computed fee set (court fees triggered by case/document types; EFM/technology fees; transaction fees; provider fees; payment-processor fees; sales tax), payment accounts, pre-authorization settled on acceptance and released on rejection, fee waivers as a payment type, refunds, receipts, itemized invoicing (monthly billing at some poles).
- Filing status tracking: status screen across all filings (pending / processing / accepted / partially accepted / rejected), envelope/submission numbers, receipts, email notifications.
- Returned artifacts: file-stamped documents and conformed copies delivered back on acceptance.
- Document preparation aids: conversion to court-required text-searchable PDF, format/OCR guidance, failure warnings.
- Case-centric organization: case summary (parties, judge assignment, register of filings), case portfolios/matters, filing history per case.
- Electronic service: service contacts, eServe with open-tracking; mail service (certified/first class) as paid complement.
- Organization accounts: firm accounts with attorneys/staff/support-staff roles; client matter numbers; party address books; pro se single-filer tier.
- Court-specific rule encoding: per-court document types, formatting rules, file-size limits, character limits, fee schedules, court-specific workflow quirks — maintained as configuration/content by the provider.
- Human support layer: live chat/phone/email positioned as a differentiator.

### L2 — Variant / Optional Structure

- Market structure: competing certified EFSPs (US dominant) vs state-run single portal vs court-vendor-operated EFSP; shared EFM identity across providers in some states.
- Packaging: standalone EFSP vs PM-suite embedded (integration) vs concierge/full-service (human-mediated filing incl. physical channel for exempt documents).
- Adjacent services bundled: process serving, courtesy copy delivery, court delivery, sheriff delivery, locator, research.
- Automation: auto-fill of filing fields from document content; filing-by-email; AI assistance (emerging).
- Physical filing channel for eFiling-exempt documents.
- Retention terms for file-stamped copies (varies by provider).
- User-tier tuning (pro se guides, attorney-service-firm accounts).

### L3 — Vendor-specific (research notes only)

- Green Filing: $3-per-submission flat pricing (TX); Auto-File; eFile by Email; single-screen filing; 23.3M documents / 176K filers counters.
- One Legal: Re-File button with disabled-after-resubmission semantics; File + Serve + File bundle; Concierge; Matters tab; order number vs court transaction number; disbursement via lowest-fee method (usually eCheck).
- FileTime: 3-year retention vs EFM's 35-day/7-day; Platinum monthly invoicing; converter specifics (security-feature warnings, dimension orientation, county-form coding removal).
- Tyler: Odyssey EFM/EFSP family; "envelope" terminology origin; state EFSP operation (efiletx.tylertech.cloud).
- MyCase/InfoTrack: expense sync to case; returned-document syncing to case; CMS-specified activation.

## Rejected Findings (considered, not promoted)

- **Fee payment as definitional** — rejected: fee machinery is universal in the sample and deeply integrated into the submission flow, but fee-waived and zero-fee filings pass through the same platform; the Type is recognizable without payment mechanics. Kept as L1.
- **US EFSP multi-provider market structure as definitional** — rejected: a state-run single portal or a court-operated system realizes the same Type; the EFSP layer is market structure, not identity. Kept as L2.
- **"Envelope" terminology as definitional** — rejected: vendor/court vocabulary for the submission concept.
- **Electronic service as definitional** — rejected: service is a legal act adjacent to filing; some filings require no service; mail service is an alternative. Kept as L1.
- **Document conversion as definitional** — rejected: convenience capability. L1.
- **Per-state operation as definitional** — rejected: artifact of US federalism; the canonical model is jurisdiction-agnostic. L2.
- **"Legal e-filing = any authority filing" (patent, SEC, tax)** — rejected for this leaf: the market category "legal e-filing" in the researched sample is court filing; other authorities are separate directory Types (Tax Filing Platform, Regulatory Reporting). Recorded as a boundary note.

## Boundary Findings

- **vs Court Case Management System / EFM (court-side)**: the EFM is the court's back-end receiving/reviewing system; the CMS is the court's case system of record. The e-filing platform is the filer-facing layer that submits into the EFM and conveys results back. Same transaction, opposite sides. One Legal documents the seam explicitly (account connection to the EFM as identity verification). If a court operates its own single portal, the two layers merge in one system — the Type boundary then follows the filer-facing surface, not the operator.
- **vs Court E-filing Platform (DIRECTORY §24 sibling)**: the researched market has ONE category here — filer-side e-filing services. The §24 leaf is most plausibly the same Type framed from the government/court side. Recorded in STATUS.md Boundary Issues for joint review; this document treats the filer-side platform as the Type.
- **vs Law Practice Management System**: PM suites embed e-filing via integration (MyCase+InfoTrack pattern); the embedded capability retains the same core (submission, adjudication loop, fees) while the PM's core (clients, matters, billing, calendar) is different. E-filing remains its own Type.
- **vs Legal Document Automation**: upstream — produces the documents; no submission or adjudication loop.
- **vs Legal Docket Management**: the docket is the court's register of case events; filer-side docket monitoring is adjacent. The e-filing platform's center of gravity is the submission transaction, not the docket record.
- **vs Government Service Portal**: general citizen-facing service delivery; e-filing is a specialized filing transaction with clerk adjudication and fee machinery.
- **vs e-signature**: signing is upstream document preparation; e-filing platforms document acceptable signing approaches but signing is not the platform's core.
- **"Remove what to become another Type" tests**: remove the adjudication loop → document delivery/managed file transfer; remove case binding → government e-forms; remove the court context (keep adjudication) → generic regulatory submission; remove the filer side (keep the court side) → Court Case Management / EFM.

## Historical / Market-Sample Check

- Paper-era: the clerk's counter performed intake, fee collection, and accept/reject. The e-filing platform digitizes exactly this interaction; the canonical model (submission → clerk decision → file stamp) does not depend on any modern feature.
- Non-US / government-operated systems (e.g., national court e-filing portals): the model holds — submission bound to a case, clerk adjudication, returned filed copies. The US EFSP layer is not required by the definition. (Non-US systems were not directly fetched; this fit is inference from the model's construction, recorded as an uncertainty.)
- Early US e-filing (federal CM/ECF lineage, 1990s–2000s): filer accounts, electronic submission, clerk docketing, fee payment — consistent with the model without any modern automation (auto-file, AI) or service tooling.
- Conclusion: the three-property L0 survives the historical check; all modern conveniences stay in L1/L2.

## Uncertainties

1. Tyler's official product documentation was unreachable (403 / transport errors). Tyler's role is established indirectly (state portal listing + competitor documentation). No product-level operational claims about Odyssey File & Serve are made in the final document.
2. Clio's e-filing offering was not directly verified (clio.com 403; support center requires login). The PM-integration pole is evidenced by MyCase+InfoTrack instead.
3. Exact numeric limits (file sizes, fee percentages, retention days, review times) are court/state/product-specific and time-varying; recorded as examples only, excluded from the final document.
4. Whether any EFSP performs clerk-review functions itself — no evidence found; all sampled documentation places review with the court (clerk), with the platform conveying results.
5. Non-US e-filing systems were not directly researched; the canonical model was deliberately built jurisdiction-agnostic, but non-US fit is inference.
6. Scope question: whether the directory's "Legal E-filing Platform" was intended to cover non-court authority filings (patent/SEC). The researched market says no; recorded as a boundary note rather than a silent scoping decision.

## Final Synthesis

A Legal E-filing Platform is the filer-side platform through which legal filings reach a court electronically. Its defining core is three structures held together: (1) the filing submission — documents plus case/party context assembled into one unit bound to exactly one court case (an existing case pulled from the court's records, or a new case initiated with the court's required roles); (2) the clerk adjudication loop — the submission crosses into the court's system and returns as accepted, partially accepted, or rejected, with the clerk's reasons conveyed back, acceptance constituting filing (file stamp, conformed copies) and rejection feeding a correct-and-resubmit loop that never discards accepted content; and (3) the filer-side case-organized record of these transactions. Around this core, mature products add fee machinery (layered court/technology/provider/processor fees, pre-authorization, waivers, receipts), filing-status tracking, returned file-stamped copies, document preparation aids, electronic and mail service, firm accounts with roles, court-specific rule encoding, and human support. Market realizations vary — standalone EFSPs, court-vendor EFSPs, state-run portals, PM-suite integrations, concierge services — but all realize the same core. The court-side receiving system (EFM/CMS) is the opposite side of the same transaction and a different Type; the §24 sibling leaf "Court E-filing Platform" is most plausibly the same Type from the government side (joint review recommended).
