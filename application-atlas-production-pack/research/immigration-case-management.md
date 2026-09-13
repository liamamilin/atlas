# Research Notes — Immigration Case Management (§24 Government, Public Sector & Civic)

Research date: 2026-09-08
Slug: immigration-case-management
Sibling context: `immigration-practice-management` (§11, processed 2026-09-07) — practitioner-side; its Boundary Issues entry requires this leaf to carry a disambiguation note (same market words, different operator).

---

## Research Goal

Understand what a **government-side immigration case management** application is: the system of record an immigration authority uses to receive, work, and decide applications for permission to enter, stay, work, settle, or obtain citizenship — and how it differs from (a) the practitioner-side immigration practice tools already documented under §11, (b) court case management, and (c) generic public-sector case management.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this leaf is the **agency-side adjudication** system (the government decides), whereas §11's leaf is the **practitioner-side preparation/tracking** system (the firm prepares filings; the government decides elsewhere).
- Likely confusion set: Public Sector Case Management (genus), Court Case Management System (immigration courts), Government Service Portal (applicant front door), Government Licensing Management (issuing instruments), Public Benefits Management (different benefit domain).
- Expected market reality: this Type is dominated by **government-built systems** (agencies build and operate their own), unlike the practitioner side which is a commercial software market. Commercial vendors appear as integrators, not as branded products with public help centers.

## Research Questions

1. What is the core object (case / benefit request / application) and what defines it?
2. What does the adjudication loop look like end-to-end (intake → screening → identity → evidence → decision → post-decision)?
3. How do identity verification and biometrics enter the loop?
4. How are decisions recorded, served, and contested (appeals/motions)?
5. What does the applicant (and their representative) see and do?
6. What role does the agency's policy/guidance machinery play in the product ecosystem?
7. How do outcomes become status/documents, and how are they proven to third parties?
8. Where are the boundaries: practitioner-side tools, courts, portals, licensing, benefits?

## Representative Products (sampled)

| Product | Operator | Shape | Evidence strength |
|---|---|---|---|
| USCIS (U.S. Citizenship and Immigration Services) | US benefits-adjudication agency | Policy Manual + online account + case status + forms + appeals | Strong (Tier 1, multiple pages) |
| UK Visas and Immigration (UKVI, Home Office) | UK national decision authority | Operational guidance collections + service standards + eVisa + processing times | Strong (Tier 1, multiple pages) |
| Department of Home Affairs — Immigration and citizenship (Australia) | National immigration/citizenship authority | ImmiAccount + VEVO verification | Thin (JS-shell pages; two surfaces named) |
| IRCC / GCMS (Canada) | National integrated case management | — | Context only (canada.ca unreachable) |
| EOIR ECAS (US immigration courts) | Immigration court | — | Context only (justice.gov unreachable) |
| UNHCR proGres | International mandate-holder (refugee RSD) | — | Context only (not verifiable from research environment) |

Selection rationale: USCIS and UKVI give two strong national samples with **different product philosophies** (USCIS: codified adjudication policy manual + applicant online account; UKVI: published operational guidance collections + service standards + digital status). Australia adds a third national regime with a distinct status-verification surface (VEVO). GCMS/ECAS/proGres were pursued for the integrated-national, court-side, and international poles respectively but could not be reached; they are recorded as market context with no claims.

## Sources (fetched 2026-09-08)

**USCIS (all fetched successfully):**
- https://www.uscis.gov/policy-manual (root: Policy Manual purpose; officer decision-making; discretion)
- https://www.uscis.gov/policy-manual/volume-1 (Volume 1 part structure; legal authorities incl. 8 CFR 103.2/103.3/103.8/103.16; forms list; complaints appendix)
- https://www.uscis.gov/policy-manual/volume-1-part-b (Submission of Benefit Requests: signatures, fees, fee waivers, interpreters/preparers, submitting requests; electronic payments transition)
- https://www.uscis.gov/policy-manual/volume-1-part-c (Biometrics Collection and Security Checks: ASC appointments, mobile biometrics, detained aliens, photograph reuse)
- https://www.uscis.gov/policy-manual/volume-1-part-e (Adjudications: chapter structure incl. Record of Proceeding, Burden and Standards of Proof, Verification of Identifying Information, Evidence, Discretionary Analysis, Rendering a Decision, Post-Decision Actions; RFE/NOID alerts; derogatory information; DNA testing)
- https://www.uscis.gov/policy-manual/volume-1-part-e-chapter-9 (Rendering a Decision: approvals/denials/abandonment/discretionary; service of decisions; appeal guidance)
- https://www.uscis.gov/file-online (online account; forms available online; track cases; pay fees; representatives)

**UKVI / gov.uk (all fetched successfully):**
- https://www.gov.uk/government/organisations/uk-visas-and-immigration (mandate: "decisions about who has the right to visit or stay"; services; SAR; FOI)
- https://www.gov.uk/government/organisations/uk-visas-and-immigration/about/about-our-services (service standards; biometrics at VAC/UKVCAS/SSC/ID Check app; further-information requests; processing times)
- https://www.gov.uk/topic/immigration-operational-guidance ("operational policy guidance used by UKVI staff to make decisions"; asylum/entry clearance/nationality/enforcement/ETA/appeals/identity checks/general grounds for refusal)
- https://www.gov.uk/evisa (eVisa = digital record of identity + status + conditions; UKVI account; share code; replaces physical documents)

**Australia (fetched; JS-shell pages, content partial):**
- https://immi.homeaffairs.gov.au/ (ImmiAccount; VEVO named)
- https://immi.homeaffairs.gov.au/visas/already-have-a-visa/check-visa-details-and-conditions/overview (VEVO: visa details/conditions for holders, employers, education providers; in-effect semantics; first-party and organisation-account checks)

**Unreachable (abandoned per network rules):**
- egov.uscis.gov (Case Status Online / processing times / E-Request) — 403
- canada.ca (IRCC) — timeout ×2
- justice.gov (EOIR/ECAS) — timeout ×2
- unhcr.org search endpoint — 403; content pages generic (no proGres documentation surfaced)
- DuckDuckGo HTML search — timeout ×2; Mojeek — 403; Bing — reachable but results localized/polluted for targeted queries

---

## Product A — USCIS (US)

### Key observations (evidence layer A = directly observed on official pages)

**The case object is the "benefit request".** The governing regulation cited throughout is 8 CFR 103.2 "Submission and adjudication of benefit requests". Cases are instances of defined benefit processes, organized in the Policy Manual by domain volumes: Nonimmigrants; Humanitarian Protection and Parole; Refugees and Asylees; Adoptions; Immigrants; Adjustment of Status; Admissibility; Waivers and Other Forms of Relief; Employment Authorization; Travel and Identity Documents; Citizenship and Naturalization. Each benefit has a named form (I-130 petition, I-485 adjustment, N-400 naturalization, I-589 asylum, I-765 employment authorization, I-821 TPS, …).

**The adjudication loop is codified.** Policy Manual Volume 1 Part E "Adjudications" chapters: Purpose and Background; **Record of Proceeding**; **Jurisdiction**; **Burden and Standards of Proof** (INA 291 burden of proof upon alien); **Verification of Identifying Information**; **Evidence**; Interviews [Reserved]; **Discretionary Analysis**; **Rendering a Decision**; **Post-Decision Actions**. The Policy Manual "contains the official policies of USCIS and assists immigration officers in rendering decisions… followed by all USCIS officers in the performance of their duties but it does not remove their discretion in making adjudicatory decisions."

**Decisions are the authoritative act, recorded and served.** Chapter 9: on approval "the officer updates all relevant electronic systems to reflect the approval"; on denial "the officer updates all relevant electronic systems and issues a written decision informing the requestor of the reason(s) for denial". Written decisions use plain language and include guidance on appeals/motions with form pointers. If a denial notice is returned undeliverable, the notice **and the original mailing envelope** are placed in the file as evidence of service. Denial types: lack of legal basis (deny without RFE first); **abandonment** (failure to appear for a required interview or biometrics appointment, or failure to provide an original document when requested); discretionary denial (separate analysis after threshold eligibility; may not be arbitrary). Asylum-specific: if the applicant appears removable, the asylum officer must grant or **refer to an immigration judge** — the referral path into the court system.

**Further-information machinery.** Requests for Evidence (RFE) and Notices of Intent to Deny (NOID) with defined response timeframes (including rules for timeframes ending on weekends/holidays); policy on disclosing derogatory information before adverse decisions; officers may suggest DNA testing when primary relationship evidence is insufficient.

**Identity and biometrics are a processing stage.** Part C "Biometrics Collection and Security Checks": biometrics collection at Application Support Centers (ASC) with appointment rescheduling and missed-appointment procedures; mobile biometrics for remote locations; biometrics for detained aliens; photographs as biometrics; photograph reuse for identity documents. 8 CFR 103.16 governs collection/use/storage of biometric information; 8 CFR 103.2(b)(13)(ii) covers failure to appear for biometrics capture, interview, or other required in-person process.

**Intake machinery.** Part B "Submission of Benefit Requests": signatures; fees (fee schedule G-1055; transition to electronic payments — ACH authorization form, paper-payment exemption); fee waivers (I-912); interpreters and preparers; submitting requests (filing periods). Representation: G-28 (attorney/accredited representative entry of appearance); Part D governs attorneys and representatives.

**Applicant-facing surfaces.** "File Online": create a free online account; file eligible forms online (N-400, I-90, I-130, I-589 named); "track your cases online"; pay fees online; two filing options; attorneys and accredited representatives can file online. Tools listed on uscis.gov: Check Case Processing Times; Case Status Online; Change of Address (AR-11); E-Request; Online Account and Technical Support.

**Contestation.** Part F "Motions and Appeals"; forms I-290B (Notice of Appeal or Motion) and N-336 (Request for a Hearing on a Decision in Naturalization Proceedings); 8 CFR 103.3 "Denials, appeals, and precedent decisions"; site-level "Administrative Appeals" section.

**Outcome issuance.** Volume 11 "Travel and Identity Documents" includes "USCIS-Issued Secure Identity Documents" and reissuance chapters — the decision produces secure documents.

**Accountability surfaces.** FOIA and Privacy Act links site-wide; Federal Records Act cited for records management; complaints taxonomy distinguishing case-specific complaints ("cases taking longer than expected", "case processing errors", "confusion regarding a notice") from non-case-specific; expedite requests (Part A Chapter 5); privacy and confidentiality chapter (incl. statutory confidentiality protections for certain humanitarian cases).

## Product B — UKVI / Home Office (UK)

### Key observations (layer A)

**Mandate framed as decisions.** "UK Visas and Immigration is responsible for decisions about who can come to the UK and who can stay here." Organisation page: "responsible for making millions of decisions every year about who has the right to visit or stay in the country, with a firm emphasis on national security".

**Service standards as published commitments.** "About our services": straightforward applications decided within customer service standards ("There is no need to ask us for progress on it"); processing time "will start when you make an application **and prove your identity**"; priority and super priority paid faster-decision services; if the application is incomplete or complex, "we will write to explain why it will not be decided within the normal standard. The letter will explain what will happen next."

**Biometric enrollment as an assigned step.** Applicants "provide your fingerprints and a photograph (biometric information) either at a visa application centre (VAC), a UK Visa and Citizenship Application Services service point (UKVCAS), a Service and Support Centre (SSC) or using the UK Immigration: ID Check app. You'll be told which option to use when you make your application." Also photo guidance for visa applications.

**Further-information requests with dates.** "you respond to any requests for further information by the dates we ask you."

**Decision guidance is a published corpus.** "Visas and immigration operational guidance — A collection of operational policy guidance used by UK Visas and Immigration staff to make decisions." Organized by decision domain: Asylum guidance (screening and routing; decision making; appeals; support; children; detention and reporting); Entry clearance guidance (basics; family members; maintenance and accommodation; medical issues; settlement; crew; exempt); Nationality guidance (British citizenship; Right of Abode; British overseas territories citizens; BNO; …); Enforcement guidance (criminality and detention; returns and removals); ETA caseworker guidance; Immigration staff guidance (Applications; Appeals; **Identity checks**; **General grounds for refusal**; Settlement; Visitors; Working; Studying; Immigration intelligence; …); the **Immigration Rules** (manual); Fees and forms; Windrush scheme caseworker guidance.

**The outcome is a digital status record.** eVisa page: "An eVisa is a digital record of: your identity and immigration status — for example the type of visa you have or if you have indefinite leave to remain (settlement) in the UK; the conditions of your status — for example if you're allowed to work or study in the UK." "You'll get an eVisa when you successfully apply for a visa or other type of permission to be in the UK." "eVisas have replaced physical immigration documents" (biometric residence cards and visa vignettes legacy). Access requires a **UKVI account**; the holder can "view your eVisa and get a **share code** to prove your immigration status, for example when you get a new job or rent a home"; travel requires linking the passport; details can be updated; errors can be reported.

**Status transparency and accountability.** "Visa processing times" collection published; subject access request service ("see the personal information that UKVI holds about you"); FOI; complaints procedure; Personal information charter; migration transparency data statistical sets.

**Adjacent machinery in the same agency.** Electronic travel authorisation (ETA) — pre-travel permission; Sponsor Management System (SMS) manuals — employers/sponsors create and assign certificates of sponsorship and report worker activity (sponsor-side obligations feeding the case system's employment routes).

## Product C — Department of Home Affairs, Immigration and citizenship (Australia)

### Key observations (layer A, thin — JS-shell pages)

- **ImmiAccount** — the online application account (online.immi.gov.au), listed as the primary self-service entry.
- **VEVO (Visa Entitlement Verification Online)** — "allows visa holders, employers, education providers and other organisations to check visa details and conditions." VEVO reports: which visa; expiry date; must-not-arrive-after date; period of stay; conditions (what you can and can't do). "VEVO is not able to provide any details relating to visas that are not 'in-effect'." First-party check plus **organisation accounts** for third parties (employers register). Pre-1990 migrants without an electronic record can request an electronic record of their permanent visa ("Proof of permanent residence") and then use VEVO — the authority's record is the source of truth; verification reads it.

## Context-only samples (no claims)

- **IRCC GCMS (Canada)** — canada.ca unreachable from the research environment (timeout ×2). Bing snippets surfaced IRCC's secure account / portal / "Your IRCC application" surfaces but no GCMS operational documentation. Treated as market context: Canada is known to operate an integrated national case management system, but **no operational claims** are made in this pass.
- **EOIR ECAS (US immigration courts)** — justice.gov unreachable (timeout ×2). The immigration-court pole is reasoned structurally (see Boundary Findings) without product-specific claims.
- **UNHCR proGres** — UNHCR's registration/case management system for refugee operations could not be verified from the research environment (search endpoints blocked; content pages generic). No claims made.

---

## Cross-product Comparison

| Dimension | USCIS (US) | UKVI (UK) | Home Affairs (AU) | Commonality |
|---|---|---|---|---|
| Core object | benefit request (application/petition per named form) | application for permission (visit/work/study/settle/nationality) | visa application (ImmiAccount) | **All three: an externally filed request for an immigration permission/benefit, case-tracked** |
| Process definition | Policy Manual volumes by benefit domain + named forms | operational guidance collections by decision domain + Immigration Rules | visa classes with conditions | **All three: the case is an instance of a defined, regime-published process** |
| Identity gate | Verification of Identifying Information chapter; biometrics (ASC appointments; failure to appear → abandonment denial) | processing time starts when application made **and identity proved**; biometrics at VAC/UKVCAS/SSC/ID Check app | (not directly observed) | **Identity verification is a distinct processing stage, commonly biometric** |
| Further information | RFE / NOID with response timeframes | "requests for further information by the dates we ask you" | (not directly observed) | **Cross-product: evidence requests with response windows** |
| Decision | approval/denial recorded in "all relevant electronic systems"; written decision with reasons + appeal guidance; service of decisions (undeliverable → envelope in file) | decision within service standards; letter if not decidable within standard; refusal grounds codified ("general grounds for refusal" guidance) | (not directly observed) | **Decision as recorded authoritative act, served in writing** |
| Outcome | secure identity documents (Volume 11); status effects | eVisa digital status record + conditions; share code proof | visa record with conditions; VEVO verification | **Outcome = status with conditions, held as the authority's record** |
| Third-party proof | (not directly observed as a named surface) | share code to employers/landlords | VEVO for employers/education providers | **Common: status provable to third parties from the authority's record** |
| Applicant account | online account (file, track, pay) | UKVI account (eVisa access, update details) | ImmiAccount | **Common mature: applicant online account** |
| Status exposure | Case Status Online; processing times published | visa processing times published; service standards | VEVO details | **Common: status/processing-time transparency** |
| Contestation | motions and appeals (I-290B, N-336); administrative appeals | appeals guidance; asylum appeals; (new Independent Appeals Body consultation) | (not directly observed) | **Common: formal appeal/motion paths** |
| Guidance machinery | Policy Manual (binds officers, preserves discretion) | operational guidance collections + Immigration Rules | (not directly observed) | **Common: published decision-guidance corpus as part of the operating model** |
| Records access | FOIA/Privacy Act; Federal Records Act | subject access requests; FOI | FOI / Information publication scheme | **Common: formal access regimes over the record** |
| Fees | fee schedule, waivers, electronic payments | visa fees published; priority paid services | (not directly observed) | **Common: fee machinery on intake** |
| Representation | G-28 attorneys/accredited representatives; interpreters/preparers | representatives implied in services (not directly observed this pass) | (not directly observed) | Common (US strongest) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The immigration case of record** — a persistent, individually identified case per externally filed request for an immigration permission or benefit (entry/stay permission, residence or settlement, protection, citizenship, status document, extension/change), anchored to the identified applicant and related parties (petitioners, sponsors, dependents), bound to a defined immigration process whose requirements and stages it carries.
   - Remove → a generic government case tracker with nothing immigration-specific.

2. **The adjudication loop** — the authority works the case to a decision: acceptance/completeness screening → identity verification (commonly biometric) → evidence assessment against the process's eligibility rules, with further-information requests where evidence is insufficient → interview where required → a **recorded decision (grant/refuse, with reasons)** that is the authority's authoritative act on the person's permission/status → post-decision actions (service of the decision, issuance of the status outcome, appeal/motion paths).
   - Remove → an application registry or correspondence log; the "adjudication" — the reason this Type exists — is gone.

3. **The externally-initiated, externally-accountable case** — the case is created by a filing from outside the authority (by the applicant, a petitioner/sponsor, or an authorized representative), and the case's state and outcome are served back to that party: receipts, notices, requests, decisions, status, and the issued status record.
   - Remove → an internal government workflow tool with no external party.

Jointly-held is load-bearing:
- 1+2 without 3 = an internal adjudication simulator with nobody filing in.
- 3 without 1+2 = an application form site + status page.
- 1+3 without 2 = an application registry with status but no decisions (portal territory).
- 2+3 without 1 = decision machinery with no case container.

**Historical / market-sample check (§24):** a paper-era immigration agency — applications received by mail, numbered case files, identity documents examined, eligibility assessed against published rules, interviews, decision letters served, visas/certificates issued, files retained, motions heard — satisfies all three legs with no software, online accounts, biometric databases, or AI. Non-US/non-UK regimes fit without any specific form, identifier, or agency name in the core. The definition is not overfit to the current cloud-era, online-account pattern.

### L1 — Common Mature Structure

- Applicant online account: file, upload evidence, respond to requests, pay fees, track status (USCIS online account; UKVI account; ImmiAccount)
- Case status exposure + published processing times (Case Status Online; visa processing times collections; service standards)
- Person-level identity layer: agency identifiers, biometric enrollment networks (ASC / VAC / UKVCAS / SSC / ID-check app class), identity verification as a processing gate
- Evidence/document management on the case (record of proceeding; uploaded evidence; RFE/NOID-class requests)
- Decision-guidance corpus as part of the operating model (Policy Manual; operational guidance collections; Immigration Rules)
- Decision & notice generation with reasons and appeal/motion guidance; formal service of decisions (incl. undeliverable handling)
- Outcome issuance: secure identity documents / digital status records with conditions
- Third-party status verification (share code; VEVO)
- Appeals/motions machinery (notice-of-appeal forms; hearings; administrative appeals)
- Fee machinery (schedules, waivers, electronic payment)
- Representation machinery (attorneys/accredited representatives; interpreters/preparers)
- Expedite/priority processing paths (expedite requests; paid priority services)
- Records-access regimes (FOIA/Privacy Act; subject access; FOI) and records-management obligations
- Statistics/transparency publication (immigration data; processing times; transparency data sets)
- Complaints handling distinguishing case-specific from general complaints

### L2 — Variant / Optional Structure

- Regime packaging: which benefit domains exist and how they're grouped (nonimmigrant/immigrant/asylum/nationality volumes; entry clearance/settlement/nationality guidance; visa classes)
- Pre-travel authorization (ETA-class) vs in-country applications vs consular/visa-post processing abroad
- Digital status records vs physical documents (eVisa transition; legacy cards/vignettes)
- Third-party verification mechanics (share code vs organisation-account lookup)
- Sponsor-side machinery feeding the case system (sponsor management; employment-verification adjacency)
- Enforcement-adjacent caseloads carried by the same agency (returns/removals, detention guidance) — boundary toward enforcement Types
- Court referral paths (asylum officer → immigration judge; appeals to tribunals)
- Build posture: government-built and -operated systems dominate; vendors act as integrators (unlike the practitioner-side commercial market)
- Paid faster-decision services (priority/super priority)
- Humanitarian confidentiality overlays (statutory protections on disclosure for certain case classes)

### L3 — Vendor-specific (research notes only)

- USCIS: named forms (I-130/I-485/N-400/I-589/I-765/I-821/I-290B/N-336/G-28/I-797C/AR-11/I-912/G-1055/G-1650/G-1651), ASC network, E-Request, priority dates, DNA-testing policy, photograph-reuse policy, 8 CFR citations, AFM→Policy Manual transition
- UKVI: eVisa share code, UKVCAS/SSC/VAC network, UK Immigration: ID Check app, SMS manuals (sponsor side), Windrush schemes, ETA Irish resident exemption, "general grounds for refusal" guidance collection, Independent Appeals Body consultation
- Australia: ImmiAccount, VEVO first-party/third-party split, "must not arrive after" date semantics, pre-1990 electronic-record backfill

## Vendor-specific Findings

See L3 above. None of these entered the canonical core. Notably, the **guidance corpus** (Policy Manual / operational guidance) is common across sampled agencies but is a *publication* of the agency rather than a software module; it is held in L1 as part of the operating model, not in L0.

## Rejected Findings

- "Immigration case management = a form-filling system" — rejected: forms are the intake instrument of one leg; the Type is defined by adjudication, not form automation (that's the practitioner-side flagship).
- "Online applicant accounts are definitional" — rejected by the historical check (paper-era agencies satisfy the core without them).
- "Biometrics are definitional" — rejected: identity verification is the invariant stage; biometrics is its dominant modern implementation, not the definition (paper-era identity-document examination satisfies).
- "Case status websites are definitional" — rejected: status exposure is the accountability half of leg 3, realizable by letters/notices; the online tracker is the modern implementation.
- "This Type is a commercial software category" — rejected: the sampled reality is agency-built systems; commercial products appear as integrators. The Type is defined by the operator's function, not by a vendor market.

## Boundary Findings

| Neighbouring Type | Relationship | Distinction | "Remove what → becomes the other Type" |
|---|---|---|---|
| **Immigration Practice Management (§11)** | same market words, different operator | practitioner prepares/tracks filings **on a client's behalf**; the outcome is decided elsewhere and recorded; commercial software market. Here: the **agency adjudicates**; the decision is the system's own authoritative act; systems are agency-built | flip the operator from agency to practitioner → Immigration Practice Management |
| Court Case Management System | adjacent forum | immigration courts/tribunals adjudicate removal/appeal **proceedings** with dockets, hearings, judges; here the agency adjudicates **applications** for permission/status. Referral paths connect them (asylum referral; appeals) | flip the object from application-for-permission to court proceeding/docket → Court Case Management |
| Public Sector Case Management | genus | generic case containers for government services; no adjudication-of-status semantics, no identity/biometrics gate, no regime-defined eligibility | remove the immigration process semantics → Public Sector Case Management |
| Government Service Portal | front door vs back office | the portal aggregates services and starts transactions; the case system is the agency's system of record where filings become cases and decisions happen. Applicant-facing surfaces here are the case system's outward face | remove the case of record and adjudication, keep service aggregation → Government Service Portal |
| Government Licensing Management | adjacent issuance | licensing registers entitlements to perform activities; immigration adjudicates permission to enter/stay with status conditions and admissibility screening | remove status/admissibility semantics, keep instrument issuance → licensing territory |
| Public Benefits Management | different benefit domain | welfare/service benefits vs immigration permissions; different eligibility law | swap the benefit domain → Public Benefits Management |
| Government Digital Identity | adjacent identity | UKVI account/eVisa is **status-bound** identity (permission + conditions), not general-purpose digital identity | remove the status/permission semantics → digital identity |
| Social Services Case Management | adjacent government casework | service-needs casework vs status adjudication | remove adjudication, keep service casework → Social Services Case Management |

## Uncertainties

1. **Integrated-national pole unverified**: GCMS (Canada) could not be reached; the claim that some authorities run a single integrated case system across temporary residence, permanent residence, and citizenship is plausible market context but rests on no fetched evidence this pass. No claims made in the final document.
2. **Court-side pole unverified**: EOIR ECAS unreachable; the immigration-court boundary is reasoned structurally (directory structure + USCIS's referral path), not from court-system documentation.
3. **International/refugee pole unverified**: proGres not verifiable; the Type's abstraction is therefore grounded in national agencies only.
4. **Officer-side UI surfaces** (work queues, case-file screens) were not directly observed anywhere; they are inferred from the adjudication procedure documentation (officers "update all relevant electronic systems", work the record of proceeding). The final document describes officer-facing surfaces at correspondingly low precision.
5. **Australia sample is thin** (JS-shell pages): ImmiAccount and VEVO are directly evidenced; the rest of the Australian loop is not.
6. **Commercial-vendor presence** for this Type (integrators building agency systems) could not be documented from public product documentation; no vendor claims made.

## Final Synthesis

The Type is the **government immigration authority's adjudication system of record**: cases are externally filed requests for immigration permissions/benefits, bound to defined regime processes; the authority works each case through an adjudication loop (screening → identity → evidence → decision) whose decision is the authoritative act on the person's status; and the case's state and outcome are served back to the external parties who filed. Everything else — online accounts, status trackers, biometric networks, digital status documents, third-party verification, appeals portals, guidance corpora, statistics — is mature structure around that core, and the paper-era agency satisfies the core without any of it.

The sharpest boundary is the **operator seam** with §11's Immigration Practice Management: same market words ("immigration case management" is literally used as a product name on the practitioner side), opposite sides of the adjudication. The §11 pass flagged this collision for joint review; this pass carries the disambiguation in the final document.
