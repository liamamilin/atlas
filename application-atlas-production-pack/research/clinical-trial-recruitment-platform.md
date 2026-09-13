# Research Notes — Clinical Trial Recruitment Platform

## Research Goal

Understand, from real products, what a Clinical Trial Recruitment Platform actually is and how it works: the core objects (study/criteria, candidate, screening/match, referral), the recruitment funnel workflow, the roles (sponsor/CRO, site, screener, candidate, clinician), the rules that govern the funnel, and the boundaries against CTMS, federated data/feasibility networks, trial-listing surfaces, patient-engagement platforms, and same-word HR recruitment software.

## Initial Boundary (hypothesis before research)

- Recruitment platform = the system that fills trials with eligible participants, distinct from:
  - CTMS (operational system of record for trial conduct — sites, milestones, visits, monitoring, budgets)
  - EDC / ePRO-eCOA / eTMF / IRT-RTSM (data capture, patient-reported outcomes, documents, randomization/supply)
  - Patient Engagement Platform / Patient Portal (post-enrollment participant experience)
  - Trial listing/discovery (ClinicalTrials.gov-style registries — unmanaged discovery)
  - Federated real-world-data networks (feasibility/site-selection cohorts, not a candidate funnel)
  - Recruitment Marketing Platform (HR domain — hiring employees; homonym, different domain)
  - Research Panel Platform (participants for market research, no clinical eligibility/ethics context)
- Suspected core objects: Study (with eligibility criteria), Candidate, Pre-screening questionnaire, Match, Referral, Site, Funnel status.

## Research Questions

1. What is the central object — the study, the candidate, or the referral that binds them?
2. How do candidates enter the system (ads, advocacy networks, physician referral, EHR mining, self-serve questionnaires)?
3. What does "matching" concretely mean — computable eligibility rule sets vs questionnaire pre-screening vs human screening calls?
4. What happens after a candidate qualifies — where does the platform end (site handoff? consent? enrollment)?
5. Who uses the system and what does each role see/do (sponsor dashboards, site queues, screener consoles, candidate surfaces, clinician alerts)?
6. Which funnel states are tracked and which analytics are computed (conversion, cost-per-patient, site scorecards)?
7. What rules matter — data quality (duplicates/spam), PHI/privacy posture, the pre-consent vs post-consent line?

## Representative Products

| Product | Vendor / heritage | Operational pole | Customer tier | Notes |
|---|---|---|---|---|
| Trialbee Honey | Trialbee | Sponsor/CRO-facing recruitment platform + site workspace; services + SaaS | Enterprise sponsor/CRO; sites | Self-named "Patient Recruitment Platform (PRP)" |
| Trialmed | Trialmed (Thermo Fisher; Acurian heritage — acurian.com now serves Trialmed) | Service-led recruitment network: central pre-screening/scheduling platform + patient database + owned site network | Sponsor/CRO (services); participants (public study finder) | Media/call-center heritage pole; useful for the historical check |
| GenomOncology | GenomOncology | EHR-integrated point-of-care trial matching (precision oncology) | Health systems / cancer centers; also CROs/sponsors | Data-led matching pole |
| Leal Health (TrialJectory) | Leal Health | Patient-initiated self-serve matching (oncology) + human support team | Patients/caregivers; oncologists; advocacy partners | Patient-facing pole |
| TriNetX | TriNetX | Federated real-world-data network — feasibility, site selection, cohort discovery | Pharma, health systems, academia | **Boundary sample**, not a core representative |

Attempted but unreachable (abandoned per network rules): Antidote (antidote.life is a parked domain; antidote.com empty ×2), Clara Health (empty ×2), TrialScout (transport error ×2), Deep 6 AI (transport error ×2), StudyKIK (JS-only shell). The patient-facing matching pole is therefore carried by Leal Health alone; the EHR-mining philosophy is evidenced through GenomOncology + TriNetX adjacency — see Source-access Limitation.

## Sources

All fetched 2026-09-07.

- Trialbee — homepage (https://trialbee.com/) and Honey Platform product page (https://trialbee.com/honey-platform/)
- Trialmed — homepage (https://trialmed.com/), pre-screening page (https://trialmed.com/finding-the-right-patients/pre-screening/), patient identification & engagement page (https://trialmed.com/finding-the-right-patients/patient-identification-and-engagement/)
- GenomOncology — homepage (https://www.genomoncology.com/) and Clinical Trial Optimization page (https://genomoncology.com/clinical-trial-optimization-solutions/)
- Leal Health — https://www.trialjectory.com/ (serves Leal Health patient-facing site)
- TriNetX — homepage (https://trinetx.com/)

Evidence layers: A = directly observed on the fetched page for that product; B = cross-product commonality across the sample; C = canonical inference from comparison + boundary reasoning.

## Product A — Trialbee (Honey Platform) — sponsor/CRO platform pole

Key observations (A-layer unless noted):

- Vendor self-frames the category: "Patient Recruitment Platform (PRP)"; "We Find Patients. You Find Cures." Serves sponsors, CROs, sites, patients. Delivery model is dual: **Full-Service Partnership** (recruitment managed service incl. campaign strategy, dual-stage screening, site enablement, Honey included) or **SaaS Access** (license Honey standalone, integrate into existing workflows).
- **Centralized intake across all channels**: "every referral arrives in one centralized dashboard" — advocacy groups and referral networks, online advertising, TV/brochures/print, email campaigns/newsletters, Trialbee and third-party vendors.
- **Built-in dual screening** before any candidate reaches sites:
  1. **Digital presecreener** — "Patients complete a protocol-specific questionnaire based on eligibility criteria."
  2. **Professional screening call** — "Qualified leads are reviewed by licensed medical professionals who confirm key details and assess fit — so your sites don't waste time on unqualified referrals." Vendor claims the process "filters out up to 75% of unqualified patients" before sites see them (marketing claim, treat as claim only).
- **Site workspace**: "Trialbee Honey presents only high-quality referrals to site staff via one secure, easy-to-use interface": review patient history; contact via SMS, WhatsApp, VoIP, or video (branded caller ID); "Track status, actions, and eligibility in real time."
- **Analytics**: four dashboard families — Study Status (actual vs target enrollment progress, trends, bottlenecks, regional differences); Recruitment Vendor Progress (which channels/vendors drive results; impressions, clicks, conversion rates, cost-per-patient in real time); Assessment & Screening Metrics ("conversion at every step from self-assessment to consent", disqualification reasons, form-abandonment points, contact hesitation); Site Metrics (candidates in process, cycle times, enrollment velocity, site scorecards for cross-site comparison).
- **Patient Registry**: "Turn disqualified patients into future enrollees. Keep waitlisted or disqualified candidates engaged and ready to re-match" — example patient message: "We've found a new study matching your profile!"
- **Data quality machinery**: "automatically detects potential duplicates, language mismatches, and spam — helping you maintain accurate data."
- **Integrations**: "Honey integrates seamlessly with IRT, CTMS, eConsent, and EDC systems" — explicit seam to the trial-execution stack (the recruitment platform is NOT those systems).
- Scale claims (vendor-published): 6,000+ research sites, 66 languages, 50 countries, 1.6M+ online pre-screeners completed since 2021, 30% referral-to-consent ratio ("double the industry average"), 78% disqualified through secondary screening.
- AI layer: "AI-powered intelligence built into Honey" (positioning; keep decisions grounded in "real-world recruitment data"); Scout AI chatbot demo exists.
- Regulatory/cultural framing (weak): "local regulatory and cultural understanding"; AI features help teams "stay compliant". No IRB-workflow features directly observed.

## Product B — Trialmed (Acurian heritage) — service-network pole

Key observations:

- Positioning: "Championing care in clinical research"; serves sponsors/CROs with recruitment services and owns 250+ research sites; claims 40+ years of clinical experience, 4,700+ recruited studies, **20M identified patient database**.
- **Central global pre-screening and scheduling platform**: "Our global pre-screening and scheduling platform confirms study eligibility and refers patients to research sites." Pre-screening evaluation "either online or by phone"; **secondary evaluation conducted by video** through a secure, browser-based platform (phone/tablet/computer). "Site appointments are reserved for patients with the greatest likelihood of enrolling in your study."
- **Evaluation stages ensure qualification**; "consistent pre-screening worldwide" via "centrally managed platform"; 40+ languages to evaluate patients.
- **Real-time data monitoring** at every stage: which recruiting efforts generate the most pre-screen evaluations, who does/doesn't complete the questionnaire, who is/isn't referred to sites — used to refine strategy and budget.
- **Candidate database logic**: "If a patient doesn't qualify for one study, we are able to identify quickly whether they may fit the criteria for another study in their disease area" — persistent pool reused across studies (same re-matching concept as Trialbee's registry).
- **Identification modeling**: "Advanced data modeling predicts patients most likely to enroll" — thousands of variables from first-party patient data plus consumer databases (demographic, psychographic, behavioral); "We know what conditions patients have, the medicines they're taking, their buying patterns…"
- **Acquisition channels**: targeted local recruiting campaigns, in-house marketing operations (100+ specialists claim), physician referrals, community outreach events, diversity emphasis — "finding well-qualified patients who meet the inclusion, exclusion and diversity criteria of your study."
- **Patient-facing acquisition surface**: public "Find a study" listing with per-study eligibility chips (condition, age range, sex, BMI, smoker status, compensation) — a recruitment funnel's front door, not a bare registry.
- Vendor-published stat with citation: "85% of clinical trials fail to recruit or retain a sufficient sample size" (cites a 2023 JCTS paper) — market-context claim.

## Product C — GenomOncology — point-of-care EHR-matching pole

Key observations:

- Positioning: precision-oncology platform; "Automate — customize patient treatment with unparalleled clinical trial matching"; audience includes oncologists, "Clinical Trial Professionals", coordinators, cancer-center research operations, CROs/pharma.
- **Matching engine ("Precision Decision")**: "evaluates eligibility rule sets, structured patient data, and biomedical ontologies to deliver ranked, curated trial matches in real time."
  - Real-time patient-trial matching: continuous monitoring of patient data; "instant alerts when eligibility criteria are met"; **full, wild-type, and partial match detection**; ranked results by match confidence.
  - Trial coverage: 15,000+ active oncology trials (claim); support for institution-specific trials; "Automated trial updates from ClinicalTrials.gov"; "Private institutional protocols encoded natively into the matching engine."
  - Matching logic: "Granular biomarker filtering (specific variants, fusions, CNVs)"; "Complex eligibility criteria support (demographics, prior treatments, comorbidities)"; "Exclusion criteria processing"; semantic understanding of clinical concepts.
- **Workflow integration**: embedded in GO Molecular Tumor Board; "EHR integration via GO Connect"; configurable notification preferences; **trial coordinator dashboards**.
- **Cohort analytics & feasibility** (adjacent layer): population-level trial eligibility analysis, enrollment forecasting, site feasibility assessments, recruitment planning tools.
- **API suite**: Trial Matching API, Variant Annotation API, Therapy Recommendation API, Patient Cohort Query API — the matching machinery is embeddable in institutional applications/EHR projects.
- Privacy posture: HIPAA-compliance badge displayed.
- Claims (customer reporting, treat as claims): 28× trial accrual rate lift, 75% less case review time, 20+ new patients identified per week, 3× faster enrollment speed.

## Product D — Leal Health (TrialJectory) — patient-initiated pole

Key observations (marketing-page level; lower confidence):

- Patient flow (as published): "01 Select your cancer type → 02 Complete our 2-minute questionnaire → 03 Instantly receive personalized list of treatments → 04 **Apply to the best treatment for you**." Matches include clinical trials alongside FDA-approved therapies (positioning: treatment decision support, "No Pharma Bias").
- **Human support layer**: dedicated patient support team "of PhDs, MDs, Nurses, & Social Workers" spending "on average 4 hours supporting and educating cancer patients" (claim) — human navigation wrapped around the match list.
- Scale claims: 3,000,000+ "treatment matches"; partnerships with advocacy/patient-support organizations (cancer foundations); press citations describe an oncologist-facing platform "to obtain personalized clinical trial matches for patients".
- Patient-directed language ("empower patients to own their cancer journey") — the candidate is the operator, not just the object.

## Boundary Sample — TriNetX (federated RWD network)

Key observations:

- Self-positioning: "The Global Truth Engine for Better Human Health" — trusted real-world data for research; data stays "within a secure, connected network of more than 13,000 clinical sites across 20+ countries", "properly governed connection back to our sites".
- For pharma: "Pinpoint the **right sites and real patients** from the start… trial design built for success" — feasibility/site-selection/protocol-optimization framing (customer quote: "real-time querying in support of our protocol optimization goals").
- No candidate funnel, no per-candidate screening/referral workflow, no enrollment conversion tracking observed on fetched pages — it is an aggregate-data query/feasibility environment, not an identified-candidate pipeline. Kept as the boundary pole separating recruitment platforms from data networks.

## Cross-product Comparison

| Structure / capability | Trialbee | Trialmed | GenomOncology | Leal Health | TriNetX (boundary) | Layer |
|---|---|---|---|---|---|---|
| Clinical study/trial carrying eligibility criteria (demand object) | A ("protocol-specific questionnaire based on eligibility criteria") | A ("inclusion, exclusion and diversity criteria") | A ("eligibility rule sets", exclusion processing) | A (cancer-type → matched trials) | (protocols via RWD query — aggregate) | L0 |
| Identified candidate pool (persons, not aggregates) | A (candidates w/ history, status) | A (20M patient database — claim) | A (patients in EHR, continuously monitored) | A (patients self-entering via questionnaire) | ✗ (de-identified cohorts) | L0 |
| Recorded screening/matching decision vs criteria | A (dual screening: digital presecreener + professional call) | A (online/phone pre-screen + video secondary evaluation) | A (ranked matches, full/partial, match confidence) | A (instant questionnaire matching) | ✗ | L0 |
| Referral/handoff of qualified candidate toward enrollment | A ("referrals are sent to sites") | A ("refers patients to research sites"; site appointments reserved) | A (alerts to clinicians/coordinators; "never miss a trial opportunity") | A ("Apply to the best treatment") | ✗ | L0 |
| Per-study recruitment funnel with conversion tracking | A (self-assessment → consent conversion; abandonment points) | A (pre-screen completion, referral rates monitored per stage) | B/C (accrual claims; enrollment forecasting) | C (not directly observed) | ✗ | L0 |
| Multi-channel acquisition with centralized intake | A (ads, advocacy networks, TV/print, email, vendors) | A (local campaigns, physician referral, community outreach) | ✗ (in-flow: patients already in care) | A (advocacy partnerships; patient search) | ✗ | L1 |
| Human professional screening/navigation layer | A (licensed medical professionals) | A (video secondary evaluation by professionals) | C (coordinator/tumor-board review downstream) | A (PhD/MD/nurse support team) | ✗ | L1 |
| Recruitment analytics (channel/vendor performance, site scorecards, cost-per-patient) | A (4 dashboard families) | A (stage-by-stage monitoring; budget optimization) | B (cohort analytics; forecasting) | C | ✗ | L1 |
| Persistent candidate registry / re-matching across studies | A (Patient Registry: "re-match") | A ("fit the criteria for another study") | ✗ (not observed) | C (not observed) | (cohorts, not funnel) | L1 (2/4 core products) |
| Data-quality controls (duplicates, spam, language mismatch) | A (auto-detection) | B (consistency/training emphasis) | ✗ | ✗ | ✗ | L1 (1/4 direct — product-specific-leaning) |
| Multi-channel candidate communication (SMS/WhatsApp/VoIP/video/email) | A | B (phone/video scheduling implied) | ✗ | C | ✗ | L1 |
| Integration seam to trial execution (CTMS, EDC, IRT/RTSM, eConsent, EHR) | A (IRT/CTMS/eConsent/EDC) | C (own site network absorbs handoff) | A (EHR via GO Connect; LIS/LIMS) | C | A (itself the data layer) | L1 |
| Feasibility/cohort analytics adjacency (population-level eligibility, forecasting) | ✗ (not observed) | B (study planning service exists) | A (enrollment forecasting, site feasibility) | ✗ | A (core purpose — but aggregate) | L2 |
| Matching basis: self-reported questionnaire data | A | A | ✗ | A | ✗ | L2 variant |
| Matching basis: structured EHR/genomic data (biomarkers, variants) | ✗ | ✗ | A | ✗ | A (aggregate) | L2 variant |
| Candidate-as-operator (patient self-serve "apply") | B (registry interaction) | B (public study finder) | ✗ | A | ✗ | L2 variant |

## Canonical Model — abstraction layers

### L0 — Defining Invariant

The smallest structure without which the product is no longer a recruitment platform for clinical trials:

1. **The clinical study as demand object, carrying its eligibility criteria** (inclusion/exclusion — plus any diversity/stratification constraints). The study is what the platform fills.
2. **An identified candidate pool as supply object** — actual persons with contactable identity and assessable health context (self-reported or system-resident), not de-identified aggregates.
3. **Recorded qualification decisions linking candidate ↔ study against its criteria** — screening/matching produces a per-candidate-per-study qualification record (qualified / disqualified / partial / pending), whatever the mechanism (questionnaire, screener call, rule engine).
4. **Referral/handoff of qualified candidates to the study's enrollment process** — typically the trial site/study team, who own final protocol eligibility, informed consent, and enrollment.
5. **A per-study recruitment funnel that tracks candidates across stages** (identified → screened → referred → enrolled), making conversion and disqualification observable to the operating roles.

Remove the eligibility-criteria-bearing study and it is generic lead generation. Remove the identified-candidate funnel (screening → referral → conversion) and it is a data/feasibility network or a trial listing. Remove the handoff and it is patient navigation/education. The funnel-with-handoff is what makes it a recruitment *platform* rather than an agency or a registry.

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- multi-channel candidate acquisition (advertising, advocacy/referral networks, TV/print, email, physician referral, community outreach) funneled into centralized intake
- dual-layer screening: digital/self-report pre-screening followed by human professional review (nurses/medical professionals)
- recruitment analytics: stage-by-stage conversion (e.g., self-assessment → referral → consent), disqualification reasons, channel/vendor performance incl. cost-per-enrolled-patient, site scorecards, actual-vs-target enrollment
- multi-channel candidate communication (SMS, WhatsApp, VoIP/video, email) from within the platform
- persistent candidate registries that re-match previously disqualified/waitlisted candidates to later studies
- data-quality controls (duplicate/spam/language-mismatch detection — observed directly at one product)
- integration seams into the eClinical stack: CTMS, EDC, IRT/RTSM, eConsent, EHR

### L2 — Variant / Optional Structure

- acquisition philosophy: outreach-led (media/community/physician referral) vs data-led (EHR/genomic mining, point-of-care alerts) vs patient-initiated (self-serve questionnaire → instant matches → apply)
- delivery model: full-service recruitment partnership vs licensed SaaS vs EHR-embedded platform vs CTMS-embedded recruitment module (site-side)
- therapeutic scope: general vs precision-oncology (biomarker-level matching: variants/fusions/CNVs; full/partial match detection; match-confidence ranking)
- matching basis: self-reported questionnaire data vs structured EHR/genomic data vs consumer-data modeling (psychographic/behavioral prediction)
- geography/language coverage; locally adapted materials (regulatory/cultural adaptation)
- patient-facing study finder/listing as the acquisition front door
- diversity-planning support (recruiting to diversity criteria — product-specific evidence)
- feasibility/cohort analytics adjacency (population-level eligibility estimates, enrollment forecasting, site feasibility scoring)
- decentralized-trial support (video-based secondary evaluation; home-trial services as adjacent service lines)

### L3 — Vendor-specific (research notes only; not canonical)

Trialbee: Honey™ naming, Scout AI chatbot, "filters out up to 75%" dual-screening claim, "referral-to-consent double the industry average" claim, 1.6M pre-screeners/6,000+ sites/66 languages/50 countries claims, branded caller ID, WhatsApp channel, auto duplicate/spam/language-mismatch detection, explicit IRT/CTMS/eConsent/EDC integration list, full-service vs SaaS split.
Trialmed: 20M identified-patient database claim, 40+ languages, video secondary evaluation, 4,700+ recruited studies claim, 100+ marketing specialists claim, psychographic/behavioral data modeling, owned 250+ site network, Thermo Fisher privacy-policy linkage, acurian.com→Trialmed migration, multilingual regional domains (CZ/UK/PL).
GenomOncology: "Precision Decision" engine, GO Connect / GO Molecular Tumor Board / BioMCP, 15,000+ oncology trials claim, ClinicalTrials.gov auto-updates, wild-type/partial match detection, match-confidence ranking, weekly/monthly knowledge-base updates, four-API suite (Trial Matching / Variant Annotation / Therapy Recommendation / Cohort Query), MEDITECH Expanse Genomics integration, accrual claims (28×, 75%, 20+/week, 3×), HIPAA badge.
Leal Health: 3.1M+ treatment-matches claim, 2-minute questionnaire, instant treatment+trial match list, "apply" action, ~4-hour human support claim, "No Pharma Bias" positioning, FDA-cleared decision-support press claim, advocacy partnership network, TrialJectory→Leal rebrand.
TriNetX: 309M+ lives / 14,200+ sites / 20+ countries / 4,000+ publications claims, LIVE/EVIDEX/XetaBase product names, EHDS-readiness positioning.

## Vendor-specific Findings

- The **dual-delivery model** (recruitment services bundled with platform vs platform-only SaaS) is explicit at Trialbee; Trialmed is service-led; GenomOncology and Leal are product-led. This is a packaging axis, not a structural difference of the Type.
- **Where the candidate is found** splits the market: the platform can (a) attract candidates from the open population (ads/community/physician referral), (b) discover candidates inside a health system's patient data (EHR/genomic mining, point-of-care alerts), or (c) receive candidates who initiate contact (patient self-serve). Mature players combine several.
- **Human-in-the-loop screening** is strongly present in the outreach-led poles (licensed screener calls, video secondary evaluations, patient support teams) and structurally weaker in the data-led pole (coordinator/tumor-board review happens downstream at the institution).
- **Re-matching pools** (disqualified/waitlisted candidates carried to future studies) appear in both the outreach-led products — the candidate database is a durable asset.

## Boundary Findings

1. **vs Clinical Trial Management System (CTMS)** — CTMS is the operational system of record for conducting the trial (sites, milestones, visit schedules, monitoring, budgets, deviations). The recruitment platform owns the *pre-enrollment candidate funnel* only. Direct seam evidence: Trialbee lists CTMS among its integrations. Reverse evidence: site-pole CTMS products (e.g., RealTime-CTMS, from the paired CTMS research) embed recruitment machinery (patient databases, landing pages, pre-screening, subject-profile sync) — recruitment capability can live inside a CTMS, but the dedicated Type's center of gravity is the funnel, not study operations. *Test: remove the candidate funnel and what remains is a CTMS; remove study operations and what remains is this Type.*
2. **vs Federated RWD / feasibility networks (TriNetX pole)** — these answer "how many eligible patients exist, where, and where should we site the trial" over de-identified aggregate cohorts, upstream of recruitment. No identified-candidate screening, referral, or conversion funnel. *Test: remove the identified-candidate funnel and you get a data network.*
3. **vs Trial listing / discovery surfaces (ClinicalTrials.gov-style registries; public study finders)** — a bare listing has no managed qualification pipeline. Product evidence: Trialmed's public "Find a study" is the acquisition front door *of* its funnel (eligibility chips → contact → pre-screen → referral); Leal's patient search wraps matching + apply. A discovery surface becomes part of this Type when it is coupled to managed screening and referral.
4. **vs Patient Engagement Platform / ePRO-eCOA / Patient Scheduling** — those operate post-consent participant experience (visits, diaries, reminders). The recruitment platform's work ends at the referral/consent seam: across products, the platform refers candidates *to* sites, and consent/enrollment is the site's act (Trialbee integrates eConsent downstream; Trialmed reserves "site appointments"). *Test: the consent line separates the Types.* (C-level inference, consistent across the sample.)
5. **vs Patient Registration & Intake / Patient Portal** — provider-patient administrative/care context; the managed object is a care relationship, not a study's candidate funnel.
6. **vs Research Panel Platform (marketing domain)** — recruits participants for market-research panels; no clinical eligibility criteria, no sites, no research-ethics context.
7. **vs Recruitment Marketing Platform (HR domain, §09)** — pure homonym: hiring employees vs enrolling trial participants. Demand object (job requisition vs clinical study), criteria, and rules differ entirely.
8. **vs eConsent** — consent execution is downstream machinery the funnel feeds into; not part of this Type.
9. **EHR-embedded matching capabilities** — matching logic embedded inside an EHR product is an EHR capability; the standalone Type integrates with EHRs (GenomOncology GO Connect) rather than being one.

## Uncertainties

- **Funnel-state vocabulary**: exact stage labels vary by product; no universal state machine was directly observed. Conceptual stages only (identified → pre-screened → screened → referred → site-screened → enrolled); do not present vendor stage names as standards.
- **Site selection/routing logic** (candidate picks site vs system assigns vs site claims) is not deeply evidenced anywhere in the sample — left light.
- **Human screening universality**: direct A-evidence at Trialbee/Trialmed/Leal; GenomOncology's human review happens downstream — classified L1, not L0.
- **Registry/re-matching**: A-evidence at two products (Trialbee, Trialmed); not observed at the data-led pole — L1 with 2/4 support.
- **Consent boundary** is canonical inference (C): strong and consistent, but not a directly documented feature statement on the fetched pages.
- **Regulatory/ethics context of recruitment materials** (IRB-approved materials, promotional review): only weak indirect signals ("local regulatory understanding", "stay compliant"); no IRB-workflow features observed — deliberately not claimed.
- **Leal Health evidence** is marketing-page level; the clinician-facing platform is known only through press citations on the page.
- **Source-access limitation**: Antidote, Clara Health, TrialScout, Deep 6 AI, StudyKIK unreachable (parked domains, transport errors, JS-only shells). The patient-initiated pole rests on one marketing-page sample; the EHR-mining philosophy rests on GenomOncology + TriNetX adjacency. No precise market-share, pricing, or numeric-limit claims are made in the final document; vendor scale numbers remain attributed claims in these notes only.

## Final Synthesis

A Clinical Trial Recruitment Platform is the system that fills a clinical study with eligible participants. Its defining core is small: a study carrying its inclusion/exclusion criteria; a pool of identified, contactable candidates; recorded screening/matching decisions that qualify candidates against those criteria; referral of qualified candidates to the study's enrollment process (the trial site/team); and a per-study funnel that makes conversion from first contact to enrollment observable. Everything else — multichannel advertising and advocacy outreach, professional screener calls, site scorecards and cost-per-patient analytics, patient registries that re-match disqualified candidates, EHR/genomic matching engines, eConsent/CTMS/EDC/IRT integrations — is mature but non-defining structure, varying by acquisition philosophy (outreach-led vs data-led vs patient-initiated), delivery model (services vs SaaS vs embedded), and therapeutic domain (general vs precision oncology). The platform operates strictly before informed consent: it produces pre-qualified referrals, and the site owns final protocol eligibility, consent, and enrollment.
