# Immigration Case Management

## Overview

An **Immigration Case Management** application is the government-side system of record for adjudicating applications for immigration permission and status. A national immigration authority uses it to receive applications filed from outside the government — for visas, residence or settlement, protection, citizenship, status documents, extensions and changes — verify who the applicants are, assess their evidence against the country's published immigration rules, and render recorded decisions that grant or refuse the requested permission. The case, its work, and its outcome live in this system; the decision it records is the authority's authoritative act on a person's right to enter, stay, work, or settle.

The defining core is small:

```text
Immigration case of record
  (externally filed request for a defined immigration process,
   anchored to the applicant and related parties)
└── Adjudication loop
    (screen → verify identity → assess evidence → decide → serve & issue)
└── Externally initiated, externally accountable
    (filed by the applicant / petitioner / representative;
     receipts, notices, decisions, and status served back)
```

Everything commonly associated with modern implementations — applicant online accounts, case-status trackers, biometric enrollment networks, digital status documents, third-party status verification, published processing times — is standard capability that mature systems add around this core, not what makes the system an immigration case manager. A paper-era immigration agency with numbered case files, examined documents, decision letters, and issued certificates satisfies the same core.

**A note on a naming collision.** The words "immigration case management" are also used by software sold to immigration law firms and corporate mobility teams. Those are practitioner-side tools: the practitioner prepares and tracks filings *on a client's behalf*, and the outcome is decided elsewhere and recorded. This Type is the other side of that seam: the *government agency* operates the system, and the decision is made *in* it. Operator and object state — not features — separate the two.

## Users & Context

The primary users are the staff of a national immigration authority:

- **Immigration officers / caseworkers / decision-makers** — work individual cases: review the file and evidence, verify identity, assess eligibility against the rules, conduct interviews where required, and render decisions.
- **Intake and screening staff** — receive and check filings for completeness, correct fees, signatures, and required documents before a case enters adjudication.
- **Biometric and identity-check staff** — capture fingerprints and photographs at application centers or through remote identity-check channels.
- **Appeals and review staff** — handle motions, administrative appeals, and hearings on decisions.
- **Supervisors and administrators** — assign and balance the caseload, maintain the decision-guidance corpus, monitor service standards, and run reporting.

Around the authority stand the **external participants**: applicants and petitioners, sponsors and employers, dependents, and authorized representatives (attorneys or accredited representatives) who file on an applicant's behalf, respond to requests, track progress, and — once a permission is granted — prove their status to third parties such as employers, landlords, and schools.

The work context is distinctive in three ways. First, the decisions are **high-stakes and law-bound**: eligibility is judged against published immigration law and policy, and outcomes change people's lives. Second, the caseload is **long-running and deadline-bearing**: applications sit in process for extended periods, carry response windows and status expiries, and are measured against published processing-time commitments. Third, the record is **accountability-bearing**: it is retained under records law, disclosable under freedom-of-information and subject-access regimes, and aggregated into published statistics.

## Core Model

### The defining core

**The immigration case of record.** One persistent, individually identified case per filed request. The case is an instance of a **defined immigration process** — a visa category, a residence or settlement route, a protection claim, a citizenship application, a status-document request — and the process defines what the case requires: the forms and evidence, the eligibility rules, the sequence of steps. The case is anchored to the **identified applicant**, and typically carries related parties in defined roles: petitioners or sponsors, dependents, and representatives of record. The case accumulates everything done to it — filings, identity records, evidence, requests, interviews, decisions — and its current state is always answerable.

**The adjudication loop.** What makes this case management *immigration* case management is that the authority works the case to a decision through a structured loop:

```text
Accept & screen
  → verify identity
  → assess evidence against eligibility rules
  → request further information where evidence is insufficient
  → interview where required
  → decide (grant / refuse, with reasons)
  → serve the decision and issue the outcome
```

The **decision is the system's defining act**. It is recorded on the case with its reasons, served formally on the applicant, and — where the regime allows — contestable through motions and appeals. Approval and refusal both update the case record and the person's status; a refusal decision is itself a formal, reasoned, servable act, not silence.

**The externally-initiated, externally-accountable case.** The case is created by a filing from outside the authority — by the applicant, a petitioner or sponsor, or an authorized representative — and the case's state flows back out: receipts confirming the filing, notices and requests along the way, the decision, and the issued status. The applicant does not merely wait; they respond to requests by given dates, attend appointments, and can see where their case stands. This two-way external relationship is structural: without external filers there is nothing to adjudicate, and without served outcomes the adjudication is not accountable.

**The outcome is status.** A granted case does not end in a file note; it ends in a **status** — a permission to enter, stay, work, study, or settle, with conditions and an effect period, held as the authority's record and commonly evidenced by an issued document or digital status record. The status outlives the case: it is what third parties later verify and what future applications build on.

### Standard capabilities around the core

Mature systems commonly add:

- **Applicant online accounts** — file eligible applications electronically, upload evidence, respond to requests, pay fees, and track the case from one place; representatives can, where the regime allows, file and manage cases for clients through the same layer.
- **Case status and processing-time transparency** — status checkers keyed to the case, published processing times, and published service standards stating how quickly straightforward applications are decided.
- **Identity and biometric enrollment networks** — application centers and service points where fingerprints and photographs are captured, plus remote identity-check channels; appointment scheduling, rescheduling, and missed-appointment handling.
- **Evidence and document management on the case** — the case file (the record of proceeding) holding filings, evidence, correspondence, and officer records.
- **Further-information machinery** — standardized requests for evidence and notices of intent to refuse, with defined response windows.
- **Decision-guidance corpus** — the agency's published policy manual or operational guidance collections that officers follow when deciding; updated as law and policy change.
- **Decision and notice generation** — written decisions in plain language with reasons and guidance on appeal rights; formal service handling, including retention of undeliverable notices as evidence of service.
- **Outcome issuance** — secure identity documents or digital status records carrying the permission and its conditions; reissuance and replacement paths.
- **Third-party status verification** — ways for employers, landlords, and education providers to verify a person's status against the authority's record, via share codes or organization lookup accounts.
- **Appeals and motions machinery** — notice-of-appeal and motion channels, hearing requests, and the case's post-decision lifecycle.
- **Fee machinery** — published fee schedules and payment channels; some systems add waivers and exemptions.
- **Representation machinery** — formal recognition of authorized representatives (attorneys, accredited representatives) who file and act for applicants; some systems add rules for interpreters and paid preparers.
- **Expedite and priority paths** — expedite requests and paid faster-decision services.
- **Records access and accountability** — freedom-of-information and subject-access channels over the record; records-retention obligations; complaints channels for case-specific and general concerns.
- **Statistics and transparency publication** — immigration and citizenship data, processing-time collections, and transparency data sets derived from the caseload.

## How It Works

The operational loop runs:

```text
File → Accept & screen → Verify identity → Assess → (Request more / Interview) → Decide → Serve & issue → Post-decision
```

**File.** An applicant, petitioner, or representative files a request for a defined immigration process — through an online account, on paper, or (for some processes) through a pre-travel authorization channel. The filing names the process, identifies the applicant and related parties, carries the required forms and evidence, and pays the fee. Filing creates the case.

**Accept and screen.** The authority checks the filing for completeness: correct process and forms, fee, signatures, required documents. Problems at this stage stop the case before adjudication — a filing with no legal basis for the benefit sought can be refused without a further-information request first.

**Verify identity.** Identity verification is a distinct stage, commonly biometric: the applicant provides fingerprints and a photograph at an application center or service point, or through a remote identity-check channel assigned when the application is made. Some authorities start the processing clock only when the application is made *and* identity is proved. Missing a required biometric appointment or interview without rescheduling has consequences — the case can be denied as abandoned.

**Assess.** The officer works the case file: reviews the evidence against the process's eligibility rules, checks identity information, and evaluates any grounds for refusal that apply across case types. Where evidence is insufficient, the authority issues a **further-information request** — a request for evidence or a notice of intent to refuse — with a response window; the applicant's response (or silence) becomes part of the record. Where the process requires it, an interview is conducted and recorded. Some decisions additionally require a separate discretionary analysis after threshold eligibility is met.

**Decide.** The officer renders the decision: grant or refuse, with reasons, recorded on the case and in the authority's systems. Written decisions use plain language the applicant can understand and include guidance on how to appeal or move to reopen. If a decision notice is returned undeliverable, the authority verifies the address and retains the notice in the file as evidence of service.

**Serve and issue.** The decision is served on the applicant and, where granted, the outcome is issued: a status with its conditions and effect period, evidenced by a secure document or a digital status record linked to the person's travel document. The person can then view their status, keep it current (updating details, linking documents), and prove it to third parties.

**Post-decision.** The case's lifecycle continues past the decision: motions and administrative appeals against refusals; hearings requested on certain decisions; reissuance of documents; and — in some regimes — referral paths out of the agency, such as a protection claim that must be referred to an immigration judge when the applicant appears removable. Approved outcomes seed future work: extensions, renewals, and status-document replacements become new cases for the same person.

Two supporting loops run alongside. The **guidance loop**: the agency maintains and publishes its decision-guidance corpus — the policy manual or operational guidance collections officers follow — updating it as law and policy change; the guidance binds officers' practice while preserving their decision-making discretion. The **accountability loop**: the record is retained under records law; applicants and the public can reach it through subject-access and freedom-of-information channels; complaints about specific cases are distinguished from general complaints; and the caseload is aggregated into published statistics and processing-time data.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by jurisdiction and system.

**Applicant online account.** The external participant's primary surface. Typical information: the person's applications and their states, pending requests and appointments, uploaded evidence, fees and payments, and issued status. Primary actions: start an application, upload documents, respond to a request, book or reschedule an appointment, update personal details, track case progress.

**Case status and processing times.** Public or account-scoped surfaces answering "where is my case" and "how long does this take": status lookup keyed to the case, published processing times by application type, and published service standards. Primary actions: check status, check processing times, request service (e.g., inquire about a case outside normal timeframes).

**Biometric appointment / identity check.** The identity-verification surface: appointment letters and bookings at application centers or service points, remote identity-check channels, rescheduling, and guidance on preparing for the appointment. Primary actions: attend, reschedule, complete the remote check.

**Status proof surface.** How a granted status meets the world: the holder views their status and conditions and generates proof for third parties — a share code to give an employer or landlord, or an organization lookup where employers and education providers verify entitlements directly against the authority's record. Primary actions: view status, generate proof, update linked documents.

**Officer case file and work surfaces.** The authority-side surfaces where the caseload lives: work queues and case assignment, the case's record of proceeding (filings, evidence, correspondence, officer records), evidence review, further-information request drafting, interview records, and decision drafting. These surfaces are largely internal; public documentation of them is thin, so their exact shape varies most across systems.

**Decision and notice documents.** The formal outputs: decision letters with reasons and appeal guidance, receipts, requests for evidence, notices of intent to refuse, and appointment notices — served in writing, with undeliverable items retained as proof of service.

**Guidance corpus.** The published body of decision guidance — organized by decision domain (for example asylum, entry clearance, nationality, appeals, identity checks, general grounds for refusal) — that officers follow and that applicants and representatives can read.

**Records-access channels.** Subject-access and freedom-of-information request channels over the record; complaints channels over cases and services.

## Important Rules / Behaviors

**The decision is the state's act.** It is recorded with reasons, served formally, and its service is evidenced in the file. It is not a draft or a recommendation: approval changes the person's status, and refusal is itself a formal, reasoned, contestable act.

**Identity gates processing.** Adjudication does not proceed on an unverified identity. Some authorities start the processing clock only when the application is made *and* identity is proved, and failure to attend a required biometric appointment or interview — without rescheduling — can end the case as abandoned.

**Eligibility is judged against published rules, not system logic.** The authority's guidance corpus binds officers' practice but does not remove their discretion; some benefits additionally require a separate discretionary analysis after eligibility is met. The system records and supports these judgments; it does not replace them.

**Further-information requests carry consequences.** Requests for evidence and notices of intent to refuse come with response windows; missing the window, or failing to provide an original document when requested, can end the case. Filing windows and response timeframes have defined rules (including how they shift when they end on non-business days).

**Status has conditions and effect periods.** A granted permission is not a blank check: it carries conditions (what the holder can and cannot do) and expiry. Verification surfaces draw on the authority's record — not the person's assertion — and report the permission's current state: what it allows, under what conditions, and until when; a permission that is no longer in effect cannot be verified as if it were.

**Visibility is asymmetric.** Applicants see their case's state, their own records, and their outcomes; the adjudication internals — officer analysis and notes — are visible to them only through formal access regimes (subject-access and freedom-of-information requests). Statutory confidentiality overlays can further restrict disclosure for certain case classes.

**The record is long-lived and accountability-bearing.** Cases are retained under records law, disclosable under access regimes, and aggregated into published statistics; complaints channels let applicants raise case-specific concerns (delays, processing errors, confusing notices) as well as general ones.

**Processing commitments are public.** Published processing times are common across mature systems; some authorities add formal service standards stating how quickly straightforward applications will be decided, and write to explain when a case cannot be decided within the standard — turning caseload management into a public commitment rather than an internal metric.

## Variants

- **Benefits-adjudication agency** — an authority dedicated to adjudicating immigration benefit requests (petitions, applications for residence, work authorization, naturalization), with a codified policy manual and named application forms.
- **Decision authority with an operational-guidance corpus** — an authority whose decision machinery is organized around published operational guidance collections and immigration rules, spanning entry clearance, settlement, nationality, asylum, and enforcement-adjacent caseloads.
- **Integrated national case management** — a single authority-wide system carrying the whole caseload across temporary and permanent residence and citizenship; widely described as the shape of large national systems, though not directly verified in this research pass.
- **Pre-travel authorization** — electronic travel authorizations adjudicated before travel, a lighter-weight process in the same case model.
- **Consular and visa-post processing** — entry-clearance decisions made abroad through visa application centers, with biometrics captured outside the territory.
- **Digital status vs physical documents** — the outcome as a digital status record with third-party proof (share codes, organization lookups) versus secure physical cards and vignettes; authorities range across this spectrum, with transitions under way.
- **Asylum and protection adjudication** — protection claims with screening and routing, decision-making guidance, and — in some regimes — referral paths into the court system when an applicant appears removable.
- **Enforcement-adjacent caseloads** — the same agency may carry detention, returns, and removals caseloads; these sit at the boundary toward enforcement and corrections Types rather than at this Type's center.
- **Build posture** — systems in this Type are predominantly built and operated by the agencies themselves, with commercial vendors acting as integrators; unlike the practitioner side, this is not primarily a packaged-software market.
- **Paid faster-decision services** — priority and super-priority processing as purchasable paths alongside standard service standards.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Immigration Practice Management | same market words, opposite side of the seam | a practitioner-side system prepares and tracks filings *on a client's behalf*; the outcome is decided elsewhere and recorded. Here the *agency* operates the system and the decision is made in it. Operator and object state — not features — separate the two |
| Court Case Management System | adjacent forum | immigration courts and tribunals adjudicate removal and appeal *proceedings* with dockets, hearings, and judges; here the agency adjudicates *applications* for permission and status. Referral and appeal paths connect the two |
| Public Sector Case Management | genus | generic government case containers without adjudication-of-status semantics, identity/biometric gates, or regime-defined eligibility — remove the immigration process semantics and this Type collapses into it |
| Government Service Portal | front door vs back office | the portal aggregates services and starts transactions; this system is the agency's system of record where filings become cases and decisions happen. The applicant-facing surfaces here are the case system's outward face, not the portal |
| Government Licensing Management | adjacent issuance | licensing registers entitlements to perform activities; immigration adjudicates permission to enter or stay, with admissibility screening and status conditions |
| Public Benefits Management | different benefit domain | welfare and service benefits versus immigration permissions; different eligibility law, different outcome semantics |
| Government Digital Identity | adjacent identity | an immigration account and status record are *status-bound* identity (permission plus conditions), not general-purpose digital identity |
| Social Services Case Management | adjacent government casework | service-needs casework versus status adjudication; different object, different decision |

The boundary with **Immigration Practice Management** is the most important one, because the market uses the same words for both. The structural test is the operator and the object state: if the system's user prepares filings for a client and the decision happens elsewhere, it is the practitioner-side Type; if the system's user is the authority and the decision happens in the system, it is this Type.

## Representative Products

- **USCIS (U.S. Citizenship and Immigration Services)** — benefits-adjudication agency with a codified policy manual, named application forms, applicant online accounts, case status and processing-time tools, and motions-and-appeals machinery
- **UK Visas and Immigration (Home Office, United Kingdom)** — national decision authority with published operational guidance collections, service standards, biometric enrollment networks, digital status (eVisa) with share-code proof, and published processing times
- **Department of Home Affairs — Immigration and citizenship (Australia)** — national authority with an online application account (ImmiAccount) and third-party status verification (VEVO)

The definition was checked against the paper-era agency model and against non-US regimes to avoid over-fitting to any single country's forms, identifiers, or channels. Canada's integrated national case management system, the US immigration courts' case system, and UNHCR's refugee registration and case management system were pursued as additional poles (integrated-national, court-side, international) but could not be verified from the research environment; they are treated as market context only and no claims about them are made here.

## Sources

Research date: **2026-09-08**

USCIS (United States):

- USCIS Policy Manual (root): https://www.uscis.gov/policy-manual
- Policy Manual Volume 1 — General Policies and Procedures: https://www.uscis.gov/policy-manual/volume-1
- Volume 1 Part B — Submission of Benefit Requests: https://www.uscis.gov/policy-manual/volume-1-part-b
- Volume 1 Part C — Biometrics Collection and Security Checks: https://www.uscis.gov/policy-manual/volume-1-part-c
- Volume 1 Part E — Adjudications: https://www.uscis.gov/policy-manual/volume-1-part-e
- Volume 1 Part E Chapter 9 — Rendering a Decision: https://www.uscis.gov/policy-manual/volume-1-part-e-chapter-9
- File Online: https://www.uscis.gov/file-online

UK Visas and Immigration (United Kingdom):

- UKVI organisation page: https://www.gov.uk/government/organisations/uk-visas-and-immigration
- About our services: https://www.gov.uk/government/organisations/uk-visas-and-immigration/about/about-our-services
- Visas and immigration operational guidance: https://www.gov.uk/topic/immigration-operational-guidance
- eVisas: access and use your online immigration status: https://www.gov.uk/evisa

Department of Home Affairs (Australia):

- Immigration and citizenship: https://immi.homeaffairs.gov.au/
- Check visa details and conditions (VEVO): https://immi.homeaffairs.gov.au/visas/already-have-a-visa/check-visa-details-and-conditions/overview

> Sourcing limitations: official applicant-facing status services (US), the Canadian immigration authority's site, the US immigration courts' site, and UNHCR's documentation could not be reached from the research environment (access denied or repeated timeouts), and general web search results were unreliable for targeted queries. Officer-side work surfaces are therefore described at low precision, inferred from the agencies' own adjudication-procedure documentation rather than from screenshots or system manuals. Claims about Canada's integrated system, the immigration-court pole, and refugee-case systems are deliberately absent. Vendor-published figures are not asserted as facts.
