# Clinical Trial Recruitment Platform

## Overview

A **Clinical Trial Recruitment Platform** is a system that fills a clinical study with eligible participants: it maintains a pool of identified potential candidates, screens or matches them against the study's eligibility criteria, refers qualified candidates to the study's enrollment process, and tracks that journey as a measurable funnel from first contact to enrollment.

Its defining structure is small:

```text
Clinical Study (carrying its eligibility criteria)
└── Candidate pool (identified, contactable people)
    └── Screening / matching decision (candidate × study, against criteria)
        └── Qualified referral → handed to the site or study team
            └── Recruitment funnel (identified → screened → referred → enrolled)
```

Everything else commonly associated with this category — multichannel advertising, professional screener call centers, site scorecards, cost-per-enrolled-patient analytics, patient registries that re-match previously disqualified candidates, AI matching over health-record data — is widespread in current products but is not what makes a product a recruitment platform. What makes it one is the managed pipeline that connects real, contactable people to a specific study's criteria and hands them, pre-qualified, to the people who will consent and enroll them.

The platform's work ends at the consent seam. Final protocol eligibility, informed consent, and enrollment belong to the trial site or study team; the recruitment platform delivers candidates to that point and makes the path to it observable.

## Users & Context

The platform sits between a demand side (studies that need participants) and a supply side (people who might qualify):

**Demand-side operators:**

- **Sponsor / CRO study leads and recruitment managers** — operate or purchase recruitment for one or many studies; watch enrollment progress against targets, channel and vendor performance, and site-level conversion.
- **Recruitment service teams** — in service-led deployments, the vendor's campaign managers and screening staff work inside the platform on the sponsor's behalf.

**Supply-side operators:**

- **Site staff / study coordinators** — receive pre-qualified referrals, review candidate history and eligibility status, contact candidates, and move them toward screening appointments and consent.
- **Screening professionals** — nurses, medical professionals, or trained screeners who review questionnaire results and conduct screening calls or video evaluations before a referral is sent.
- **Clinicians at the point of care** — in data-led deployments, they receive match alerts for their own patients against trial eligibility.

**Candidates:**

- **Patients and healthy volunteers** — answer eligibility questionnaires, browse study listings, receive re-match notifications, and are contacted through the platform; in patient-initiated products they actively compare matches and apply.

The work context is the operational life of a clinical study: aggressive enrollment timelines, strict protocol criteria, competitive patient populations, and a hard regulatory boundary at consent — which is why the entire machinery of this Application Type exists to deliver *qualified* people to sites rather than raw interest.

## Core Model

### The Defining Core

```text
Clinical Study (with eligibility criteria)
└── Candidate pool (identified, contactable people)
    └── Screening / matching decision (candidate × study, against criteria)
        └── Qualified referral → site / study team
            └── Per-study recruitment funnel with observable conversion
```

Five properties. Remove any one and the product stops being a recruitment platform:

- **Clinical study with eligibility criteria** — the demand object. A study carries its inclusion and exclusion criteria (and, in some deployments, additional diversity or stratification constraints). The criteria are what candidates are assessed against; without a criteria-bearing study, the product degrades into generic lead generation.
- **Identified candidate pool** — the supply object. Candidates are actual, contactable persons with assessable health context — either self-reported through questionnaires or resident in health-record data. This distinguishes the Type from aggregate data networks, which count de-identified cohorts but manage no people.
- **Recorded qualification decision** — for every candidate-study pair, the platform records an assessment against the criteria: qualified, disqualified (with reasons), partial match, or pending. This record is the platform's unit of work and the basis of everything downstream.
- **Referral / handoff toward enrollment** — qualified candidates are handed to the study's enrollment process, typically the trial site or study team, who own final eligibility, consent, and enrollment. Without the handoff, the product is patient education or navigation, not recruitment.
- **Per-study recruitment funnel** — candidates are tracked across stages (identified → screened → referred → enrolled), making conversion, disqualification, and drop-off observable. The funnel is what makes recruitment *managed* rather than merely advertised.

### Standard Capabilities of Mature Products

These are common across mature products and expected by the market, but they are additions to the core rather than its definition:

- **Multichannel acquisition with centralized intake** — advertising, patient-advocacy and referral networks, TV/print, email campaigns, physician referrals, and community outreach all feed a single referral intake, so every candidate arrives in one queue regardless of origin.
- **Two-layer screening** — a digital, criteria-based pre-screening questionnaire followed by human professional review (screening calls or video evaluations by licensed or trained staff) before any referral reaches a site.
- **Recruitment analytics** — stage-by-stage conversion (for example, from questionnaire completion to referral to consent), disqualification reasons, form-abandonment points, channel and vendor performance including cost per enrolled participant, site scorecards, and enrollment progress against target.
- **In-platform candidate communication** — contacting candidates through SMS, messaging apps, VoIP/video calls, and email from within the platform, with activity logged against the candidate.
- **Candidate registries with re-matching** — persistent pools of past candidates; people disqualified from one study can be matched against later studies in their condition area.
- **Data-quality controls** — detection of duplicate submissions, spam, and language mismatches in candidate intake (present in some products).
- **Integration seams into the trial-execution stack** — connections to CTMS, EDC, IRT/RTSM, eConsent, and EHR systems, so referred participants and recruitment data flow into the systems that run the trial.

### One Structure, Many Implementations

The core model is conceptual; implementations differ sharply by product philosophy:

```text
Concept:            Eligibility criteria
Implementations:    protocol-based questionnaire items;
                    machine-readable eligibility rule sets;
                    biomarker-level criteria (variants, fusions, gene alterations)

Concept:            Qualification decision
Implementations:    self-report pre-screening questionnaire;
                    professional screening call / video evaluation;
                    matching engine over structured health-record or genomic data

Concept:            Candidate acquisition
Implementations:    outreach (ads, community, advocacy, physician referral);
                    patient self-initiation (questionnaire → instant matches → apply);
                    data-led discovery (continuous EHR monitoring with match alerts)

Concept:            Recipient of the referral
Implementations:    trial site coordinator (referral queue);
                    clinician at the point of care (match alert in clinical workflow);
                    the candidate themself ("apply" submission to the study)
```

A reader who has only seen one style — for example, an ad-driven call-center operation — should still be able to recognize an EHR-mining or patient-self-serve product as the same Application Type from the core model alone.

## How It Works

### 1. Study setup: encode the criteria

A study enters the platform with its protocol eligibility criteria. These are translated into whatever screening instruments the product uses: a pre-screening questionnaire keyed to the inclusion/exclusion criteria, or a machine-readable rule set the matching engine can evaluate against structured patient data. The study also gets its target enrollment, its participating sites or enrollment channels, and its acquisition plan.

### 2. Candidate acquisition: fill the pool

Candidates enter the pool through the product's acquisition philosophy:

- **Outreach-led** — the platform's operators run advertising, advocacy-group partnerships, physician referral, and community programs; every response (web form, call, referral) becomes a candidate record in the central intake.
- **Data-led** — the platform connects to a health system's patient data and continuously evaluates patients against study rule sets, surfacing candidates from within existing care populations.
- **Patient-initiated** — the candidate finds a study listing or matching service, answers a health questionnaire, and receives matched studies they can apply to.

### 3. Screening and matching: produce the qualification record

Each candidate is assessed against each study's criteria. The assessment may be a questionnaire score, a professional screener's call or video evaluation, a rule-engine match with confidence ranking, or a combination. The output is always the same kind of record: this candidate, against this study, is qualified / disqualified (with reason) / partially matching / pending review. Screening commonly happens in layers — digital first, human second — so that sites receive only pre-qualified referrals.

### 4. Referral and handoff: deliver to the study

Qualified candidates are referred to the enrolling site or study team — a referral queue with candidate history, eligibility status, and contact tools for the coordinator; a match alert in the clinician's workflow; or a candidate-submitted application. The site takes over: it confirms eligibility per protocol, schedules screening visits, obtains informed consent, and enrolls. Recruitment-platform integrations (CTMS, EDC, eConsent, IRT) reflect exactly this seam — the platform hands the person over and the trial-execution systems take the record forward.

### 5. Funnel management: measure and optimize

Throughout, the funnel is measured: how many candidates at each stage, where they drop off and why, which channels or vendors produce referrals that actually convert, how sites compare on cycle times and enrollment velocity, and how actual enrollment tracks against target. Disqualified or waitlisted candidates may be kept in a registry and re-matched when later studies fit their profile.

```text
Encode criteria → acquire candidates → screen / match → refer to site
        ↑                                                      ↓
        └────────── re-match from registry ←── disqualified / waitlisted
                                                   (funnel measured end-to-end)
```

### Defining core vs common vs optional

**Defining core** — without these, not this Type:

- study with eligibility criteria
- identified candidate pool
- recorded qualification decision per candidate-study pair
- referral/handoff toward enrollment
- per-study funnel with observable conversion

**Common mature structure** — present in most modern products:

- centralized multichannel intake
- two-layer screening (digital + human)
- funnel analytics (conversion, disqualification reasons, cost-per-enrolled-participant, site scorecards, actual-vs-target)
- in-platform candidate communication
- candidate registries with re-matching
- integrations into the eClinical stack

**Variant / optional** — depends on philosophy, delivery model, and domain:

- acquisition basis: outreach campaigns vs health-record mining vs patient self-initiation
- delivery: full-service recruitment partnership vs licensed SaaS vs embedding inside an EHR or site-management product
- domain tuning: general trials vs precision-oncology biomarker matching
- patient-facing study finders and "apply" flows
- feasibility/cohort analytics (population-level eligibility estimates, enrollment forecasting)
- diversity-planning support; decentralized-trial accommodations (video-based secondary evaluation, remote participation)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Study recruitment dashboard (demand side)

- Purpose: run and optimize recruitment for one or many studies.
- Typical information: enrollment progress vs target, funnel conversion by stage, disqualification reasons, channel/vendor performance, regional breakdowns.
- Primary actions: monitor funnel, compare channels and vendors, reallocate budget, drill into bottleneck stages.

### Site referral workspace (site side)

- Purpose: process pre-qualified referrals into screened, consenting participants.
- Typical information: referral queue, candidate history and questionnaire results, eligibility status, contact details and communication log, site-level metrics.
- Primary actions: review candidate, contact via call/messaging, schedule visit, record status and eligibility decisions, advance or close the referral.

### Candidate-facing surfaces

- Purpose: let potential participants discover studies and self-assess.
- Typical information: study listings with plain-language eligibility attributes (condition, age, location), eligibility questionnaires, matched-study results, registry profile and re-match notifications.
- Primary actions: search studies, complete a questionnaire, submit contact details, view matches, apply or consent to be contacted.

### Screening console (professional screeners)

- Purpose: human review layer between digital pre-screening and site referral.
- Typical information: questionnaire results, criteria checklist, contact history.
- Primary actions: call or video-evaluate the candidate, confirm key details, record qualification decision and reasons.

### Point-of-care match surfaces (data-led variant)

- Purpose: surface trial opportunities for patients already in care.
- Typical information: ranked trial matches for a patient with match rationale and confidence, eligibility highlights.
- Primary actions: review matches, receive alerts when criteria are met, route to trial coordinators.

## Important Rules / Behaviors

### Pre-qualification is not eligibility

The platform qualifies candidates against the study's criteria, but final eligibility is determined at the site under the protocol. This division of labor is the structural reason referrals, not enrollments, are the platform's output. Candidates can still screen-fail at the site; the platform's role is to make that rare and measurable.

### The funnel filters before the site sees the candidate

Mature products deliberately push disqualification upstream — digital pre-screening followed by professional review — so that sites spend time only on candidates with a realistic chance of qualifying. Disqualification reasons are recorded, which is what makes funnel analytics possible.

### Disqualification is not the end of the candidate

Where registries exist, a disqualified or waitlisted candidate remains an asset: the platform can re-match them against later studies in their condition area. The candidate pool persists across studies even though the funnel is per-study.

### The platform stops at the consent seam

Informed consent and enrollment are the site's act. The recruitment platform hands over pre-qualified candidates; consent, randomization, and participation tracking belong to trial-execution systems (eConsent, EDC, CTMS, IRT). This boundary separates recruitment platforms from patient-engagement and trial-conduct products.

### Candidate records are sensitive health data

The platform holds identified, health-relevant information about people who have not yet consented to anything. Products emphasize secure handling of this data, controlled access for site and sponsor roles, and intake-quality controls (duplicates, spam, language mismatches) — the candidate pool is both a marketing asset and a compliance-sensitive record.

## Variants

- **Outreach-led recruitment** (media/call-center heritage) — advertising, community outreach, and physician referral feed centralized intake; large screener teams and patient databases are the operational core; often delivered as a managed service.
- **Data-led / point-of-care matching** — the platform mines structured health-record (and, in precision oncology, genomic) data and pushes match alerts into clinical workflows; candidates are discovered rather than advertised to.
- **Patient-initiated matching** — self-serve questionnaires produce instant matched-study lists; the candidate compares options and applies; human support teams provide navigation.
- **Delivery-model variants** — full-service partnership (platform bundled with campaign and screening services) vs licensed SaaS the sponsor operates itself.
- **Embedded variants** — recruitment modules inside EHR platforms or site-side trial-management systems; the same funnel machinery, sold as a capability of a larger product.
- **Domain variants** — general therapeutic-area recruitment vs precision-oncology matching (biomarker-level criteria, partial-match handling, match-confidence ranking).
- **Geographic variants** — multilingual, multi-country operations with locally adapted materials and regionally distributed site networks.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Clinical Trial Management System / CTMS | the operational system of record for conducting the trial (sites, milestones, visits, monitoring, budgets); the recruitment platform owns only the pre-enrollment candidate funnel and hands off at the referral seam — recruitment machinery can be embedded in a CTMS, but the funnel owner is this Type |
| Federated real-world-data / feasibility networks | answer "how many eligible patients exist and where" over de-identified aggregate cohorts, upstream of recruitment; no identified-candidate screening, referral, or conversion funnel |
| Trial listing / discovery (registry-style) | unmanaged discovery without a qualification pipeline; a listing surface becomes part of this Type when coupled to managed screening and referral |
| Patient Engagement Platform | operates the post-consent participant experience (visits, reminders, programs); recruitment operates pre-consent acquisition |
| ePRO / eCOA Platform | captures participant-reported and clinical-outcome data during the trial, after enrollment |
| Patient Registration & Intake / Patient Portal | provider-patient administrative context for care, not a study's candidate funnel |
| Patient Scheduling | appointment logistics as a capability; in recruitment products scheduling exists only as part of moving candidates to site screening |
| eConsent | executes informed consent downstream; a system the recruitment funnel feeds into |
| Research Panel Platform | recruits participants for market-research panels; no clinical eligibility criteria, trial sites, or research-ethics context |
| Recruitment Marketing Platform (HR) | homonym from talent acquisition: fills job requisitions with candidates, not studies with participants; different demand object and rules |

The most important boundary is with the CTMS: the two meet at the referral/enrollment seam, and recruitment capabilities sometimes appear inside site-side CTMS products — but the defining question is which object the system manages. A system whose center of gravity is the study's operational conduct is a CTMS; one whose center of gravity is the candidate funnel against study criteria is a recruitment platform.

## Representative Products

- Trialbee (Honey Platform) — sponsor/CRO recruitment platform with site workspace and dual screening
- Trialmed (Acurian heritage) — service-led recruitment network with central pre-screening and a large candidate database
- GenomOncology — EHR-integrated point-of-care trial matching for precision oncology
- Leal Health (TrialJectory) — patient-initiated matching with human support

A federated health-data network (TriNetX) was examined as a boundary sample to sharpen the distinction from feasibility/data-network products; it is representative of that neighboring category, not of this Type.

## Sources

Research date: **2026-09-07**

- Trialbee — homepage (https://trialbee.com/) and Honey Platform product page (https://trialbee.com/honey-platform/)
- Trialmed — homepage (https://trialmed.com/), pre-screening page (https://trialmed.com/finding-the-right-patients/pre-screening/), patient identification & engagement page (https://trialmed.com/finding-the-right-patients/patient-identification-and-engagement/)
- GenomOncology — homepage (https://www.genomoncology.com/) and Clinical Trial Optimization page (https://genomoncology.com/clinical-trial-optimization-solutions/)
- Leal Health — https://www.trialjectory.com/
- TriNetX — homepage (https://trinetx.com/), used as boundary sample

> Sourcing limitation: this category is documented mainly through vendor product and marketing pages rather than public help centers; several prominent products (Antidote, Clara Health, TrialScout, Deep 6 AI, StudyKIK) could not be reached from the research environment. Vendor-published scale figures (database sizes, conversion rates, platform counts) are treated as claims and intentionally not restated as facts in this document. Funnel-stage names are conceptual; exact state labels vary by product. Evidence details and product-by-product observations are recorded in the paired Research Notes.
