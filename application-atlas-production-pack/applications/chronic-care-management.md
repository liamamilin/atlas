# Chronic Care Management

## Overview

**Chronic Care Management** software operates ongoing care-management programs for people with chronic conditions. It identifies which patients in a practice's panel qualify for the program, enrolls them with documented consent, builds and maintains a care plan oriented to each patient's chronic conditions, and drives a recurring cycle of non-face-to-face care — outreach calls, medication work, referrals, scheduling, chart review — performed by care staff under clinician supervision. Each patient's service is documented per period (in the dominant form, a monthly service record including how much staff time was spent), and the program produces the documentation and billing outputs the payer regime requires.

The defining structure is small:

```text
Chronic-condition-defined patient population
  (eligible patients identified from the panel / EHR)
└── Consented program enrollment
    (patient bound to a defined ongoing program)
    └── Condition-oriented care plan maintained per enrolled patient
        └── Recurring documented care service cycle
            (care staff perform and record care activities
             per patient per service period)
```

Everything else commonly associated with the category — automated eligibility scanning, time tracking, billing reports, EHR integration, remote monitoring devices, patient apps, quality dashboards — is widespread in current products but is not what makes the software chronic care management. Programs funded without fee-for-service claims (payer disease-management programs, internally funded clinic programs, international chronic disease programs) realize the same core structure.

The Type sits inside a product family: it is the care-coordination machinery bound to a defined chronic-care program. What distinguishes it from a general care coordination platform is that the program's own rules — who is eligible, what consent is required, how service time is documented, what can be billed — are first-class objects the software must enforce, not just deployment context.

## Users & Context

The people who work in chronic care management software daily are mostly **care-delivery staff operating a program on behalf of a practice**:

- **care coordinators / care managers / registered or licensed nurses** — carry the enrolled caseload; make the recurring outreach calls, review charts, work medication refills, arrange referrals and appointments, and document every interaction
- **medical assistants** — support outreach and scheduling under delegation
- **supervising physicians and nurse practitioners** — direct the program, approve care plans, review escalations; the program operates under their supervision and billing identity
- **billing staff and practice administrators** — consume the monthly service documentation, review billing reports, and submit claims
- **compliance officers and program managers** — monitor consent records, documentation completeness, program growth, and payer-audit readiness

The patient is the program's subject and its most important participant: enrolled with documented consent, contacted on the program's recurring cycle, supported through care-line access, education, and help with transportation, mobility, and social needs; family members and caregivers are commonly included.

Typical operating contexts:

- **primary care and specialty practices** running the program for their own panels, with in-house staff or vendor support
- **community health centers and rural health clinics**, where the program extends scarce clinical capacity to dispersed populations
- **health systems and accountable care organizations** using the program to close care gaps and prevent acute utilization
- **outsourced care-management vendors** who deliver the program — enrollment calls, monthly outreach, documentation — on behalf of practices, under the practice physicians' supervision
- **health plans** sponsoring chronic-care programs for their members

## Core Model

### The Defining Core

**Chronic-condition eligibility.** The program's population is defined by chronic conditions, not by visits or episodes. The software holds the eligibility picture for each patient — which qualifying conditions they have and whether they meet the program's entry criteria — drawn from the practice's EHR panel. The specific rule varies by regime (the dominant US program requires two or more chronic conditions expected to last at least a year and pose significant risk); the software's job is to make the rule machine-enforceable against the panel. Without this anchor the product is generic outreach or coordination, not chronic care management.

**Consented program enrollment.** An eligible patient becomes a program member through a documented enrollment: the program is explained to the patient (including any cost-sharing and the right to opt out at any time), and the consent is recorded. Enrollment binds the patient to a defined, ongoing program with a service pattern and documentation obligations. It is the boundary of the program's accountable population — everything in the system happens to enrolled members.

**Condition-oriented care plan.** Each enrollee has a care plan built around their conditions: health goals, planned interventions, medication considerations, and barriers to address. In practice this is assembled from condition-specific, editable templates rather than written from scratch, kept current, and revised as the patient's situation changes. The plan is what turns monthly phone contact into managed care; it is also a program requirement that payers can audit, so its currency is tracked, not assumed.

**Recurring documented service cycle.** The program's heartbeat is a repeating service period — monthly in the dominant form — in which care staff perform and record non-face-to-face care for each enrollee: a check-in call, a clinical or chart review, a prescription refill arranged, a referral tracked, an appointment scheduled, a symptom followed up. Each interaction is logged to the patient's service record with what was done, by whom, and how long it took. This documented cycle is what separates chronic care management software from a care-plan authoring tool or a one-off outreach campaign: the service recurs, and the record of it accumulates.

Remove any one of these four and the product stops being recognizable: without the eligibility anchor it is generic coordination; without enrollment the program has no population; without the care plan it is a call center; without the recurring documented service it is plan management or episodic outreach.

### Standard Capabilities Mature Products Add

A typical modern product carries most of the following. They make the program operable at scale; they are not the definition.

- **Panel-level eligibility identification** — automatic notifications and panel filters (by condition, payer, enrollment status) that surface patients who qualify but are not yet enrolled; practices are often unaware how large this group is.
- **Time tracking against program thresholds** — capturing clinical-staff time per patient per service period, in-platform where possible and by manual entry for phone work done elsewhere, with running totals toward whatever the regime requires (in the base US program, at least twenty minutes of clinical staff time per patient per month).
- **Billing and compliance outputs** — monthly billing reports that map documented time and activity to the correct billing codes, export in the biller's or clearinghouse's format, and the documentation set a payer audit would ask for: consent, an initiating visit, a current care plan, time logs, and evidence of the coordination work.
- **EHR integration** — pulling demographics, diagnoses, and medications in; writing care-plan documentation back to the chart; structured-import fallbacks where APIs are unavailable; or, in the EHR-embedded variant, living inside the EHR suite itself.
- **Multi-program stacking** — running sibling care-management programs (remote patient monitoring, principal care management, transitional care, behavioral health integration, annual wellness visits, advanced primary care management) on the same platform and objects, with per-program eligibility, documentation, and billing separation.
- **Care-team role model** — coordinators execute, supervising clinicians direct and approve, billing and compliance staff consume outputs; vendor-employed coordinators can substitute for in-house staff while the supervising physician keeps clinical direction.
- **Patient communication and support** — phone outreach as the default medium, plus secure messaging/texting, education content, care-line access between visits, and social-needs support.
- **Dashboards and analytics** — enrollment status, threshold proximity (who is about to miss the service minimum), care-gap closure, quality-program performance, and program revenue.
- **Compliance and security machinery** — timestamped, audit-ready records, role-based access, HIPAA-aligned infrastructure and certifications.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Chronic-condition eligibility
Forms:    rule-based panel filters over EHR diagnoses · eligibility notifications
          triggered by visits (e.g. an annual wellness visit) · vendor-run
          panel analysis during onboarding

Concept:  Consented enrollment
Forms:    practice staff obtaining consent at a visit · vendor enrollment
          call campaigns · digital consent via patient portal

Concept:  Care plan
Forms:    condition-specific editable templates · plans written back to the
          EHR chart · versioned plans with dated revisions

Concept:  Documented service cycle
Forms:    in-platform call logging with automatic time capture · manual time
          entry for off-platform work · a monthly billing report as the
          period's closing artifact

Concept:  Care staff
Forms:    in-house practice coordinators · vendor-employed nurses under the
          practice physician's supervision · pharmacists as delivery partners
```

A reader who has only seen one shape — say, an outsourced vendor running monthly calls for a primary-care practice — should still be able to recognize an in-house program operated in the EHR vendor's own module as the same Type.

## How It Works

### Launching a program

```text
Panel analysis (find eligible patients by diagnosis and payer mix)
→ platform configuration and EHR connection
→ staff training by role
→ patient consent and enrollment (the first wave of members)
→ initial care plans for the enrolled population
→ first monthly service cycle and first billing report
```

Vendors commonly front-load identification and enrollment because enrollment — not software setup — is where programs stall; time to a first billed service period is a marketed measure of onboarding quality.

### The monthly program loop

```text
For each enrolled patient, each service period:
→ identify who is due for contact (worklist of enrolled patients)
→ conduct non-face-to-face care: check-in calls, chart and clinical reviews,
   medication refills, referrals, appointment scheduling, follow-up on results
→ log each interaction to the patient's service record
   (what was done, by whom, how long it took)
→ update the care plan as circumstances change; flag escalations to the
   supervising clinician
→ close the period: time totals map to the service documentation;
   billing report generated, reviewed, and submitted
→ the cycle repeats; patients who no longer participate exit the program
```

The loop is deliberately repetitive. Its purpose is continuity between visits: the program is the between-visit care relationship, made regular, documented, and accountable.

### Who does what

Coordinators live in the service worklist — working calls, documenting outcomes, watching which patients are approaching the period's threshold. Supervising physicians interact at defined points: approving plans, handling escalations, lending the program their supervision. Billing staff receive a period-ending report rather than raw activity, and compliance staff check that consent, plan currency, and documentation are complete before claims go out. Program managers watch growth and performance: enrollment rates, retention, care gaps closed, revenue.

### Stacking programs

Because the objects — eligibility, consent, plan, time log, billing report — recur across sibling care-management programs, mature platforms run several programs at once: a patient may receive remote patient monitoring whose readings feed the chronic-care plan, or graduate from a transitional episode into the ongoing chronic program. Each program keeps its own eligibility and documentation trail; time is attributed to the program it served.

## Interfaces

### Eligibility / patient registry

The program's front door.

- typical information: panel filtered by condition, payer, and enrollment status; flagged candidates who qualify but are unenrolled; current eligibility state per patient
- primary actions: review candidates, enroll a patient, start or resume consent, exclude with reason

### Enrollment and consent

- typical information: program explanation materials, consent status and timestamp, patient opt-out rights
- primary actions: capture consent (at a visit, by enrollment call, or via portal), record the consent artifact, track its audit readiness

### Care plan editor

- typical information: condition-specific plan content — goals, interventions, medications, barriers; revision dates and current version
- primary actions: assemble the plan from templates, update it as needs change, record reviews, write documentation back to the EHR

### Monthly service worklist / outreach tracking

The coordinator's primary working surface.

- typical information: enrolled patients due for contact, last-contact recency, interaction log, running time total toward the period's threshold, patients at risk of missing the minimum
- primary actions: log a call or message, document what was done and the time spent, escalate to the clinician, complete the period

### Time log and billing report console

- typical information: per-patient per-period time totals mapped to billing codes; the assembled billing report with required documentation elements attached
- primary actions: enter off-platform time, review the mapping, generate and export the report to the biller or clearinghouse

### Program dashboard

- typical information: enrollment and retention, threshold proximity, care-gap and quality measures, documentation completeness, program revenue
- primary actions: drill into cohorts, redistribute caseloads, export program reports

### Patient-facing surfaces

- typical information: the patient's plan, upcoming contact, education material, a way to reach the care team (secure messages; in some programs a phone care line available around the clock)
- primary actions: read and acknowledge, report status, contact the team

## Important Rules / Behaviors

### Consent comes before service

The formal program — and its documentation and billing obligations — begins at documented consent, which records the patient's understanding of the program, any cost-sharing, and the right to stop at any time. An undocumented consent is the most common audit failure; products therefore timestamp and store consent as a first-class record.

### Eligibility rules define the population

Who may enroll is set by the regime — the count and nature of qualifying conditions, their expected duration and risk, and sometimes a prior qualifying visit. The software encodes these rules so the panel is screened mechanically and enrollment of ineligible patients is prevented or flagged.

### Service is non-face-to-face, recurring, and supervised

The program's care happens between visits, by phone or messaging, on a repeating schedule. Clinical staff perform most of it; the supervising physician directs the program and approves plans — a supervision structure the software reflects through approval steps and attributed documentation.

### Time is the program's currency — and it is attributed

Where the regime pays for documented time, each patient's monthly total determines whether the service is billable and at what level, so time capture is a first-class mechanic rather than bookkeeping. Time is never counted toward a second program in the same period; attribution rules keep stacked programs separate.

### The documentation set is evidentiary

A claim must be able to show consent, an initiating visit, a current and revised care plan, time logs meeting the threshold, and evidence of the coordination work. Products capture these as the work happens — not reconstructed at billing time — because the program operates under audit.

### The care plan must stay current

A plan that no longer reflects the patient is a compliance problem and a clinical one. Plans carry revision history; currency is monitored; a stale plan surfaces as an exception in the worklist.

### The program record lives alongside the EHR, not instead of it

Clinical documentation remains in the EHR; the program holds what the EHR does not — eligibility, consent, service time, program billing — and exchanges context in both directions. Where integration is weak, staff fill the gap manually and the program gets harder to run, which is why interoperability is treated as mature structure rather than an accessory.

## Variants

- **Software-only platforms** — the practice's own staff run the program on guided workflows; the vendor supplies machinery and compliance expertise.
- **Platform plus managed coordinators** — vendor-employed care coordinators deliver the outreach and documentation under the practice's physician supervision, for practices without staffing capacity.
- **Tech-enabled services and full-service programs** — the vendor runs the program end to end (panel analysis, enrollment calls, monthly engagement, billing support) with proprietary software underneath.
- **EHR-embedded modules** — the program is delivered as a module of the practice's EHR suite, trading standalone depth for native data access and one login.
- **Regime variants** — the US fee-for-service program family dominates the market, with sibling programs (single high-risk condition management, transitional episodes, advanced primary care, wellness visits, behavioral health integration) stacked on the same machinery; payer-funded and international chronic-disease programs run the same core without claims machinery.
- **Customer-tier variants** — solo and small primary care; specialty practices (cardiology, endocrinology, nephrology); community health centers and rural clinics with distinct billing rules; health systems; ACOs; health plans; and pharmacy partners as delivery channels.
- **Condition and integration variants** — multi-condition general programs with condition-template libraries; device-fed programs where remote monitoring readings flow into the chronic-care record; phone-only programs without devices.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Care Coordination Platform | closest sibling | the same coordination machinery without a chronic-care program's rules as first-class objects; coordination spans transitions, discharge, and social care, while this Type is bound to a defined chronic-care program with eligibility, consent, per-period service documentation, and billing |
| Care Plan Management | adjacent | centers the care plan as an authored, controlled record; here the plan is one program object organizing a recurring service cycle |
| Remote Patient Monitoring | adjacent, often bundled | the device-data collection loop is RPM's defining core; monitoring readings can feed the chronic-care plan, but the program runs without devices |
| Population Health Management | upstream complement | panel-level analytics and registries identify who needs attention; this Type is the person-level program that acts on those patients |
| Payer Care Management | same machinery, other owner | health-plan-owned programs over members tied to cost and utilization oversight; here the program typically serves a provider's panel under provider supervision |
| Patient Engagement Platform | delivery slice | outreach, education, and content are the delivery medium here, documented against the service record; engagement platforms have no program record |
| Telehealth Platform | adjacent | delivers virtual visits; a visit is an event, not a recurring program relationship |
| Practice Management / Patient Scheduling | operational context | run the practice's visits and administration; this Type runs the between-visit program on top of them |

The family seam matters most: chronic care management, care coordination, and care plan management share objects (person, plan, activities) but keep different centers of gravity — the program with its rules, the team executing care, and the plan as a controlled document, respectively. Products frequently bundle all three; the leaves document the different centers, and the bundling is recorded as packaging rather than collapse.

## Representative Products

- **ChartSpan** — full-service chronic care management program delivered with proprietary software; enrollment, monthly engagement, documentation, and billing run as a managed service for practices, health centers, and health systems
- **Prevounce** — software-first platform for chronic care management alongside remote monitoring, advanced primary care management, and wellness programs, with optional managed services and connected devices
- **TimeDoc Health** — tech-enabled chronic care management services on an enterprise platform, strong in community health centers and rural deployments
- **ThoroughCare** — care-coordination platform carrying chronic care management as one program among siblings (principal care, transitional care, remote monitoring, wellness, behavioral health)
- **HealthArc** — chronic care management software and managed coordination services with documentation-grade program machinery, from panel analysis to billing export

The EHR-embedded pole is additionally represented by major EHR vendors' care-coordination suites that ship chronic care management as a module (observed in the sibling research on this category).

## Sources

Research date: **2026-09-06**

- ChartSpan — https://chartspan.com/ and https://www.chartspan.com/chronic-care-management/
- Prevounce — https://prevounce.com/ and https://www.prevounce.com/software/chronic-care-management
- TimeDoc Health — https://timedochealth.com/
- ThoroughCare — https://www.thoroughcare.net/chronic-care-management (plus care-coordination pages recorded in the sibling research on Care Coordination Platform)
- HealthArc — https://healtharc.io/chronic-care-management/

> Sourcing limitation: all sources are official vendor product, solution, and program-guide pages. The regulator's program documentation was not reachable from the research environment (access denied on the government program page, one attempt), and no vendor help centers were reachable in this pass. Program rules are therefore stated at the level the official vendor pages support and agree on — notably the recurring monthly service pattern, consent documentation, and the base program's twenty-minute clinical-staff time threshold, each documented across multiple sampled products. Billing-code names and dollar rates vary by year and geography and are deliberately not stated here. Detailed evidence, product-by-product observations, the cross-product comparison, and findings unique to individual products are recorded in the paired Research Notes.
