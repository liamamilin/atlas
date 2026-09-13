# Research Notes — Prior Authorization Platform

Research date: 2026-09-09

## Research Goal

Understand, from real products, what a Prior Authorization Platform is as an Application Type: who operates it on each side of the payer–provider divide, what objects exist inside it, how an authorization request actually moves from a planned service to a tracked approval, what rules govern the loop, and where the Type's boundaries lie against payer claims processing, health plan administration, utilization management, e-prescribing's ePA companion, and generic approval workflow tooling.

## Initial Boundary

Working hypothesis before research:

- Core use: obtaining a payer's advance approval ("prior authorization", PA) for health care services that the payer requires to be approved before delivery — and tracking that approval through to care delivery and claims.
- Likely users: provider-side patient-access / prior-auth staff and payer-side utilization-management (UM) clinical staff, with delegated review organizations as an intermediate actor.
- Nearest neighbors: Utilization Management (unprocessed sibling leaf), Payer Claims Processing (processed), Health Plan Administration System (processed), Electronic Prescribing (processed — ePA companion), Referral Management (unprocessed), generic Approval Workflow Platform.
- Unknowns: whether the Type is provider-side, payer-side, or both; whether "platform" implies network machinery or a single-organization workbench; how the X12 278 family maps onto the observed workflows; whether AI decisioning is definitional or variant.

Pre-hung flags from earlier passes (to discharge or confirm from this side):

- `health-plan-administration-system` (2026-09-08): "utilization-management + prior-authorization-platform (authorization status is an adjudication input; review machinery ships as separate suites)".
- `payer-claims-processing` (2026-09-08): "vs prior-authorization-platform / utilization-management — authorization status is an adjudication input and the review machinery (medical necessity, review determinations) is that side's center; X12's own corpus splits 837/835 claim machinery from 278 review machinery, joint review recommended".
- `electronic-prescribing` (2026-09-08): "vs Prior Authorization Platform: ePA is a frequent companion capability embedded at the point of prescribing … but the authorization record and payer decisioning are a separate Type."

## Research Questions

1. What is the unit of record — the request, the determination, or the authorization? How do they relate?
2. Who submits, who reviews, who decides, and where do delegated review organizations sit?
3. What does "is authorization required" detection look like, and is it core or common?
4. What channels carry the request (portal, EMR-embedded, EDI, API, fax/phone legacy), and how do attachments/clinical documentation move?
5. What does the payer side do with a request: criteria, review support, exceptions, determination, notification?
6. What happens after determination: status inquiry, validity windows, extensions, and the linkage to claims adjudication?
7. How do provider-side and payer-side product postures differ, and how do shared-network venues realize the same loop?
8. Is AI decision support definitional, common, or variant — and what control rules surround it?
9. Where exactly is the seam with payer claims processing, health plan administration, and utilization management?

## Representative Products

Selected for market position, documentation quality, different vantage points, and different customer layers:

| Product | Posture | Primary customers |
|---|---|---|
| Availity (Intelligent UM / AuthAI + Revenue Cycle Management) | dual-sided network: payer UM suite + provider pre-service tooling over a large payer–provider connectivity network | health plans; hospitals/physician groups |
| Waystar (Authorization Manager) | provider-side financial clearance suite component | health systems, specialty practices |
| Cohere Health (Utilization Management suite) | payer-side PA/UM automation, in-house + delegated operating models | health plans (mid-size/regional to national) |
| Infinx (Patient Access Plus) | provider-side tech-enabled services + AI agents, human-in-the-loop | specialty groups, laboratories, ASCs, hospitals |

Standard reference: X12 Health Care Services Review Information Transaction Set (278) — the official EDI machinery for the review request/response exchange.

## Sources

All fetched 2026-09-09.

- Waystar — Authorization product page: https://www.waystar.com/our-platform/financial-clearance/authorizations/ (plus platform root https://www.waystar.com/)
- Availity — Intelligent Utilization Management page: https://www.availity.com/intelligentum/ (title: "AI-Powered Prior Authorization")
- Availity — Revenue Cycle Management page: https://www.availity.com/revenue-cycle-management/
- Cohere Health — homepage/platform overview: https://coherehealth.com/ (UM suite, Policy Studio, Auth Match, provider surfaces)
- Infinx — homepage/platform overview: https://infinx.com/ (Patient Access Plus, payer connections, specialties)
- X12 — Transaction Sets reference: https://x12.org/products/transaction-sets (278 description and example families)

Unreachable / abandoned (one attempt each, per network rules):

- Experian Health prior-authorization page — HTTP 403
- AMA prior-authorization hub — HTTP 403
- UnitedHealthcare provider portal auth page — 404 (moved)
- DuckDuckGo search fallback — timeout (search engines abandoned; direct URLs used)

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality; **C** = canonical inference from comparison + boundary reasoning.

## Product A — Availity (network / both sides)

### Key observations (evidence layer A unless noted)

- Payer-side product is named "Intelligent Utilization Management"; its stated subject is "transforming the prior authorization process". The AuthAI engine is positioned as "transparent, responsible AI" grounded in "a health plan's existing medical policy", not predictive models. (product page)
- **Control rule, verbatim**: "Availity AuthAI does not auto-deny, deny or approve prior authorizations. … recommendation engine, not a decisioning engine." Health plan remains in control; every recommendation traceable and overridable; policy logic codified in Clinical Quality Language (CQL), an HL7 standard. (product page FAQ)
- End-to-end decomposition from the vendor's own FAQ: **Intake & Submission** (providers submit from EMR workflow or the multi-payer portal); **Attestation** (FHIR APIs CRD/DTR/PAS support "is auth required" queries, answering "no auth required" or returning the attestation protocol to gather the right clinical data from the provider's EHR); **UM Decision support** (codified medical policy recommends approvals in near real time for routine cases); **UM Exception handling** (complex cases organized for UM clinicians); **UM Feedback loop** (outcomes update medical policy logic); **Determination** (returned via FHIR API to provider via EMR workflow or portal). (product page FAQ)
- CMS-0057 framing (vendor-stated): three FHIR APIs — Coverage Requirements Discovery (CRD, "tells providers if prior authorization is needed"), Documentation Templates and Rules (DTR, "automates gathering the right clinical data"), Prior Authorization Support (PAS, "enables electronic submission and response") — with a vendor-stated January 1, 2027 start for plans. (product page FAQ)
- Integration posture: platform-agnostic, integrates via FHIR API "to UM systems and any EHR"; requests "route to or from delegated vendors supporting insourced, outsourced, or hybrid UM operating models". (product page FAQ)
- Network scale claims (vendor-reported): 170+ health plans, 3.4M+ providers; customer quote: "98% of our prior auth requests electronically". Stat claims: 75% of PA requests receive near-real-time approval recommendation; 99% submitted with clinical data or informed questions answered; 100% of providers notified of unnecessary PA requests; 95% reduction in appeals/grievances; near-real-time recommendation "less than 90 seconds" on average.
- Provider-side RCM page: pre-service "Authorizations" capabilities listed as "Provider Authorizations, 278 Notice of Submission, EDI Enrollment"; pain narrative = "calling a payer to find out if an authorization is required, submitting the authorization via fax, or calling the payer to check the status"; value = "connects directly to payers … to get care decisions faster". (RCM page)

## Product B — Waystar (provider-side suite)

### Key observations (A)

- Positioning: "Prior authorization delays are the #1 cause of claim denials" (vendor claim); "Waystar automates the entire prior authorization process. No phone calls, no faxes — just approvals." (product page)
- Module set (all vendor-branded, provider-facing): **Auth Initiate** ("initiate authorizations for scheduled services"); **Auth Notify + Submit** ("authorization requests for inpatient direct admissions"); **Auth Accelerate** ("real-time approvals, automatic updates, and full transparency … fully automating end-to-end prior authorization workflows"; with **Auth Attachments** — "attach supporting materials directly to the authorization request and confirms payers have received them"); **Auth Status** ("automate status update retrievals to track authorizations"); **Medical Necessity** ("real-time checks against payer policies and coverage guidelines … before or during patient registration"). (product page)
- Requirement detection: "authorization verification tools instantly analyze EHR, HIS, and PM orders to determine if an authorization is required and ensure accurate submissions in real time — including attached clinical documentation when required by the payer", via a "robust authorization rules engine". (product page)
- Vendor-reported outcomes: 50%+ reduction in average authorization initiate time; <2% cancellation rate due to denied/delayed authorizations; 8-day increase in average lead time; 97% DAR clearance rate; 70M authorization transactions annually; 35+ service lines covered. (product page, footnoted to a named health-system case study)
- Placement inside the suite: Authorization sits under "Financial Clearance" beside Eligibility Verification and Coverage Detection; a separate "Referral Status" module handles referrals; provider-side "Utilization Management" is a different pillar ("Clinical Integrity + Revenue Capture"). (platform navigation)

## Product C — Cohere Health (payer-side UM)

### Key observations (A)

- Sells to health plans ("Built for plans. Trusted by clinicians. Proven at scale."); UM suite is described as "AI-powered prior authorization automation — touchless prior authorizations and faster medical necessity reviews". (homepage)
- Offerings: **In-House** ("Run UM with your own clinical team", with named stages Intake → Decision → Review Assist → Review Resolve → Align); **Delegated** ("Specialty-specific care management" — musculoskeletal, cardiovascular, GI, sleep, diagnostic imaging); **API-Based** ("Embed UM into existing systems"); **Policy Studio** ("Manage clinical policy at scale"). (homepage navigation)
- Determination posture (vendor-reported): "85% real-time approvals" with "the remaining prior authorization submissions are reviewed by a clinician before final determination". (homepage)
- Provider-facing surfaces: portal login, registration/onboarding, a public "Check Auth Status" page, provider help center publishing "Review Criteria" collections. (homepage header/footer links)
- Cross-loop linkage: Payment Integrity offering includes "Auth Match — Reconcile claims against authorizations"; separate Appeals and Care Management products on the same platform ("Cohere Unify") connecting UM, payment integrity, appeals, care management, quality, claims operations. (homepage)
- Scale claims (vendor-reported): 17 clients, 25M covered lives, 47M plan/provider interactions, 94% provider satisfaction; ROI figures (18x UM for a regional plan). Named health-plan CMO testimonials (Humana, Geisinger).

## Product D — Infinx (provider-side tech-enabled services + agents)

### Key observations (A)

- Patient Access Plus agent suite includes: "Prior auth determination agent", "Prior auth initiation agent", "Prior auth follow-up agent", "Patient access experts", "Payer/clearinghouse connections", "Provider HL7/API/FHIR integration", "Workforce human-in-the-loop orchestration", "Workflow execution", "Analytics and insight". (homepage)
- The three named agents line up with the loop's phases: determination (is auth required / what does the payer require), initiation (submit), follow-up (track to outcome). (homepage)
- Payer connections (vendor-reported): "2800+ payer connections … spanning eligibility, authorizations, claims, denials, posting, and A/R, with coverage varying by workflow and plan configuration." (homepage navigation)
- Named connections include the delegated-review intermediaries: EviCore, AIM, Optum, NIA Magellan, HealthHelp — evidence that provider-side workflows must route around payer-delegated UM entities as distinct destinations. (homepage navigation)
- Scope breadth: "Prior Authorization Support For Referring Physicians" module; specialty programs for radiology, laboratory, specialty pharmacy, LTC pharmacy, DME — service lines where prior auth volume concentrates. (homepage navigation)
- Engagement model blends platform and services (managed prior-auth operations, human-in-the-loop exception handling), pricing structured around volume/outcomes (vendor-reported). Prior-authorization ROI calculator offered as a free tool. (homepage)

## Standard reference — X12 278 (A)

- Official description (X12 transaction sets page): "Health Care Services Review Information Transaction Set (278) … can be used to transmit health care service information, such as subscriber, patient, demographic, diagnosis or treatment data for the purpose of request for review, certification, notification or reporting the outcome of a health care services review." And: "Expected users of this transaction set are payors, plan sponsors, providers, utilization management and other entities involved in health care services review."
- Example families published by X12: **278 — Request for Review and Response**; **278 — Inquiry and Response**; **278 — Notification and Acknowledgment** (multiple versions).
- Read: the standards body itself models the Type's exchange as (a) request for review, (b) certification/outcome notification, (c) inquiry (status) — between payor, provider, and UM entities. The claim machinery is a different corpus (837 claim submission, 835 remittance, 276/277 claim status), corroborating the payer-claims-processing pass's flag.

## Cross-product Comparison

| Structure | Waystar (provider) | Availity (payer+network) | Cohere (payer) | Infinx (provider services) | X12 278 |
|---|---|---|---|---|---|
| Authorization request: member/patient + provider + coded planned service + clinical justification | ✔ orders pulled from EHR/HIS/PM; attachments when required | ✔ attestation protocol gathers clinical data from EHR | ✔ touchless intake, evidence surfaced for review | ✔ determination/initiation agents + experts | ✔ subscriber/patient/diagnosis/treatment data |
| Requirement detection ("is auth required") | ✔ rules engine over orders | ✔ CRD "is auth required" queries; notifies of unnecessary requests | — (payer side presupposes the request; owns policy instead) | ✔ determination agent | — |
| Multi-channel intake | ✔ replaces phone/fax/portals | ✔ EMR-embedded + multi-payer portal; "98% electronic" | ✔ portal + API-based offering | ✔ payer portals/connections (incl. delegated entities) | ✔ EDI exchange |
| Review support grounded in payer policy | n/a (provider side) | ✔ CQL-codified policy recommendations; clinician exception handling | ✔ Policy Studio; Review Assist/Resolve | n/a | n/a |
| Determination returned with reasons | ✔ receives decisions/updates | ✔ determination returned via FHIR/portal | ✔ 85% real-time; remainder clinician-determined | ✔ follow-up to outcome | ✔ certification / response |
| Authorization of record + status inquiry | ✔ Auth Status retrievals | ✔ tracking; 278 inquiry machinery named on provider page | ✔ public Check Auth Status page | ✔ follow-up agent | ✔ 278 Inquiry and Response |
| Validity window / service scope of an authorization | implicit (tracking) | implicit | implicit | implicit | implied by "certification" (inference, not quoted) |
| Delegation routing (UM intermediaries) | n/a observed | ✔ route to/from delegated vendors | ✔ delegated offering is a product line | ✔ named connections (EviCore, AIM, Optum, NIA Magellan, HealthHelp) | ✔ "utilization management … entities" among expected users |
| Linkage to claims | ✔ denial-avoidance framing (#1 cause) | ✔ payment-accuracy adjacency | ✔ Auth Match reconciles claims vs authorizations | ✔ denial prevention | ✔ deliberately separate transactions (837/835/276/277) |
| Policy/criteria management as payer-side object | n/a | ✔ codified policy + feedback loop updates policy logic | ✔ Policy Studio at scale | n/a | n/a |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures; removing any one destroys the Type:

1. **The authorization request as the unit of record.** A persistent, identified request binding a specific patient/member, a requesting/servicing provider, planned coded service(s), and clinical justification, submitted to the payer side in advance of care delivery. Remove → generic document exchange or workflow tooling with nothing to authorize.
2. **The review-to-determination loop.** The payer side (the plan's UM unit or its delegated review organization) evaluates the request against its coverage and medical-necessity rules and produces a recorded determination — approve, deny, partial, or pend-for-more-information — returned to the requester with reasons. The deciding act belongs to the payer party; platforms assist. Remove → one-way submission with no decision, not authorization.
3. **The authorization of record.** The durable outcome: an identified, trackable authorization covering defined services (commonly within a validity period) that both parties reference — status-checkable by the requester while arranging care, and consumable downstream by claims adjudication. Remove → ephemeral request/response messages; status tracking and claims reconciliation collapse.

Jointly-held is load-bearing: 1 alone = a submission inbox; 2 without 1+3 = an advice engine; 3 without 1+2 = an empty authorization registry; 1+2 without 3 = one-shot messaging with no memory.

### L1 — Common Mature Structure

Very common in current products, not required for the definition:

- requirement detection against payer rules ("is auth required" / "which documentation"), evaluated on orders/scheduled services (Waystar rules engine; Availity CRD; Infinx determination agent)
- multi-channel electronic intake: EHR/PM-embedded, payer/provider portals, standardized electronic transactions (278-class), FHIR APIs, with legacy phone/fax channels as the baseline being replaced
- clinical-documentation assembly and attachments, with delivery confirmation to the payer
- status inquiry and tracking worklists on both sides
- policy-grounded decision support with human exception review (recommendation engines that do not decide; clinician-reviewed remainder)
- delegation routing to payer-delegated UM organizations
- payer-side policy/criteria management (codified criteria, feedback of outcomes into policy)
- EHR/PM integration and payer/clearinghouse connectivity as the plumbing layer
- provider-side denial-avoidance analytics (auth failures as a leading denial cause)

### L2 — Variant / Optional Structure

Depends on segment, geography, operating model, automation posture:

- vantage point: provider-side suite component vs payer-side suite vs shared network venue serving both
- UM operating model: in-house review team vs delegated review organization vs hybrid; insourcing/outsourcing configurations
- automation posture: real-time automated approval for routine cases vs asynchronous clinician review vs human-in-the-loop services
- service-line scope: imaging/advanced diagnostics, musculoskeletal/surgery, oncology and specialty drugs (pharmacy benefit), laboratory, DME, inpatient admissions; urgent and admission-initiated requests as timing variants of the same loop
- regulatory machinery: US X12 278 heritage; CMS interoperability rules and the FHIR CRD/DTR/PAS triple (vendor-stated dates); other jurisdictions' prior-approval regimes (not directly researched — see Uncertainties)
- adjacent bundling: referral status, medical-necessity checking, appeals handling, auth-vs-claims reconciliation (payment integrity), care management, provider scheduling contexts

### L3 — Vendor-specific (research notes only)

- Waystar: Auth Initiate / Auth Notify + Submit / Auth Accelerate / Auth Attachments / Auth Status / Medical Necessity module names; AltitudeAI branding; stat claims (50% initiate-time reduction, <2% cancellation, 8-day lead-time increase, 70M transactions annually, 97% DAR clearance).
- Availity: AuthAI branding and its CQL implementation; Essentials/Multi-Payer Portal product naming; stat claims (75% near-real-time recommendations, 99% submitted with clinical data, <90-second average, 95% appeal reduction, 98% electronic intake quote, 170+ plans, 3.4M providers); vendor-stated CMS-0057 API descriptions and January 1, 2027 date.
- Cohere: Unify platform name; In-House stage names (Intake, Decision, Review Assist, Review Resolve, Align); Policy Studio; Auth Match; delegated specialty lines (MSK/cardiovascular/GI/sleep/imaging); stat claims (85% real-time approvals, 18x ROI, 25M covered lives, 47M interactions).
- Infinx: Healthcare Revenue OS / Revenue Cycle Agent Platform framing; agent names (determination/initiation/follow-up); 2800+ payer connections; named intermediary connections; services-led pricing posture; ROI calculator.

## Vendor-specific Findings

- The explicit "recommendation engine, not decisioning engine" control rule is directly documented at one sampled vendor (Availity) but represents a governance posture likely shared market-wide under regulatory scrutiny; held as strongly-evidenced common behavior, not L0.
- Cohere's public "Check Auth Status" page shows payer-side products expose status lookups to providers outside any portal login — one-product observation (A), treated as a common-pattern instance.
- Waystar's "Medical Necessity" module (real-time medical-necessity checking at registration, provider side) is one-product observation at module granularity; the underlying behavior (checking planned services against payer necessity rules pre-service) appears across vendors but as differently-scoped capabilities.

## Rejected Findings

- **"AI is definitional"** — rejected. The paper-era workflow satisfies the L0 legs; automation posture (rules, analytical AI, manual review) is a variant axis. Two vendors explicitly frame AI as assisting, not deciding.
- **"Real-time determination is definitional"** — rejected. Asynchronous clinician review remains standard for complex cases in every payer-side sample; real-time is a common modern capability with vendor-reported rates.
- **"Prior authorization is US-only"** — rejected as definitional. The sample is US-centric (limitation noted), but the request→review→authorization structure is jurisdiction-agnostic; US transaction machinery (278, CMS rules) is L2.
- **"Delegated review organizations are part of the Type's core"** — rejected. They are participants in the loop (routed-to destinations), documented at two vendors; the invariant is that the request routes to whoever the payer charges with deciding.
- **"Pharmacy-benefit PA is a separate Type"** — rejected. Same request→determination→authorization loop; pharmacy/specialty-drug scope is a service-scope variant (evidence: Infinx specialty/LTC pharmacy lines; e-prescribing pass already records ePA as a companion capability at the point of prescribing).
- **"Auth-vs-claims reconciliation is core"** — rejected. Payer-side common capability (one sampled product sells it as a named offering); the adjudication machinery it serves is the payer-claims-processing Type's center.

## Boundary Findings

- **vs Payer Claims Processing** (processed leaf): the seam is request-review-record vs claim-adjudication-payment. Authorization status is an *input* to adjudication rule layers (as that pass recorded); the review machinery is this Type's center. X12's own corpus corroborates: 278 review transactions are separate from 837/835 claim transactions and 276/277 claim status. **Discharges that pass's joint-review flag from this side — keep-both ratified.** The boundary test: remove the claim/payment machinery and the prior-auth loop still stands; remove the request→determination loop and claims processing still stands (auth status then simply never arrives).
- **vs Health Plan Administration System** (processed leaf): benefit plan configuration *holds* authorization rules (which services require auth — recorded in that pass as part of the benefit rulebook); this Type *operates* the request machinery against those rules. Discharged on the same system-of-record vs machinery reasoning.
- **vs Utilization Management** (unprocessed sibling — NEW FLAG): the heaviest remaining seam. Payer-side market packaging overlaps: two sampled products sell payer prior auth *inside* "Utilization Management" offerings (Cohere's UM suite; Availity's Intelligent UM), while a provider-side suite (Waystar) groups PA under financial clearance and UM under a separate clinical-integrity pillar — packaging splits observed in both directions. Proposed seam for that pass: **utilization management = the payer's clinical review program** (medical-necessity criteria, review types including prospective/concurrent/retrospective, reviewer staffing and delegation governance, program-level operation), **prior authorization platform = the multi-party request machinery** (intake → review support → determination → notification → authorization of record → status) whichever side hosts it. PA is UM's prospective, transactional face. Joint review recommended when that leaf is processed.
- **vs Electronic Prescribing** (processed leaf): confirmed from the other side already — electronic prior auth (ePA) embedded at the point of prescribing is a companion capability; the authorization record and payer decisioning remain this Type. No change needed here.
- **vs Referral Management** (unprocessed): referrals are provider-to-provider authorizations of care relationships; no payer determination on coverage is the center. Adjacent; separate Type.
- **vs generic Approval Workflow Platform**: identical abstract loop (request → review → decision → record), but without health care semantics — member/patient binding, coded planned services, clinical justification, coverage/medical-necessity rules, claims linkage. Remove the health care semantics and this Type dissolves into it.
- **"Remove what → becomes another Type" tests**: remove the payer-side determination act → document/submission tooling, not authorization; remove the durable authorization of record → messaging; remove "in advance of care delivery" and add concurrent/retrospective program machinery → utilization management territory; remove coded services/clinical justification → generic approval workflow.

## Uncertainties

- Precise turnaround-time rules, auto-approval thresholds, and authorization expiry/units conventions are not stated canonically in the accessed sources; all such figures in this file are vendor-reported and product-specific. The final document deliberately avoids precise numbers.
- Non-US prior-approval regimes were not directly researched (sample is US-centric; Experian/AMA/UHC attempts failed). The definition names no US machinery; regional realization is asserted only as L2 variant with low confidence on specifics.
- The vendor-stated CMS-0057 compliance date and API responsibilities were taken from one vendor's FAQ; not verified against the regulation itself.
- Large legacy payer-side suites (the dominant historical engines) were not directly documented in this pass (consistent with the shared limitation recorded by the payer-claims-processing pass); the payer pole rests on two well-documented current-generation vendors.
- Whether concurrent-review (inpatient stay) requests are fully in-scope for this Type or belong to the UM sibling is left to the utilization-management joint review; the researched loop structure would accommodate them as the same machinery with different timing, but no sampled product page directly evidenced a concurrent-review workflow in this pass.

## Final Synthesis

A Prior Authorization Platform is the multi-party machinery through which advance payer approval for planned health care services is requested, decided, recorded, and tracked. Its world has exactly three load-bearing structures: the authorization request (member + provider + coded planned service + clinical justification, filed in advance of care), the review-to-determination loop (payer-side evaluation against coverage/medical-necessity rules to a recorded, reasoned determination — recommenders assist, the payer party decides), and the authorization of record (a durable, trackable approval whose status both parties consult and which downstream claims adjudication consumes as an input). Everything else commonly seen — requirement detection, electronic multi-channel intake, attachments, decision support, delegation routing, policy management, real-time approval, auth-vs-claims reconciliation — is mature add-on structure or variant scope. The Type is realized from provider-side suites, payer-side suites, and shared network venues alike, and packaging overlaps heavily with utilization management; the seam proposed for the sibling leaf is program (UM) vs request machinery (this Type), with the claims-input and benefit-rulebook seams to the processed payer leaves ratified here.
