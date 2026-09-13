# Research Notes — Home Care Agency Management

Research date: 2026-09-08
Slug: home-care-agency-management
Directory leaf: Home Care Agency Management (§22 Healthcare & Life Sciences)

## Research Goal

Understand, from real products, what software for a home care agency actually is: its core objects, the operating loop that runs a non-medical (or private-duty) care agency out of an office and into clients' homes, and where it separates from neighboring types (home health EHR, hospice, generic employee scheduling, staffing agency systems, care coordination).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the agency-side operating system for delivering scheduled personal/support care at clients' homes: clients + caregivers + recurring home visits + point-of-care visit records (EVV in the US) + billing and payroll driven by those records.
- Nearest neighbors: Home Health EHR / Management (skilled clinical, Medicare-certified), Hospice Management, Employee Scheduling Platform, Staffing Agency Management System, Patient Scheduling, Care Coordination Platform.
- Main confusion risk: "home care" vs "home health" — market language mixes them; several vendors sell both as separate products/modules.

## Research Questions

1. What are the core objects? (client, caregiver, visit, care plan, authorization, invoice/claim, timesheet)
2. How does a visit flow from schedule to delivered service to money (bill + pay)?
3. What role does EVV / visit verification play — invariant or regulatory implementation?
4. How is scheduling different from generic employee scheduling? (client-need-driven, authorizations, matching, open-shift broadcast)
5. What does the caregiver's point-of-care surface do? (clock in/out, tasks/ADLs, notes, signatures)
6. What payor structures exist? (private pay, Medicaid, LTC insurance, VA; UK: local authority/private)
7. Where is the seam with Home Health EHR / Management?
8. What varies by region (US vs UK) and segment (SMB vs enterprise, personal care vs IDD vs skilled)?

## Representative Products

Selected for market representation, documentation access, different philosophies and customer tiers, and geographic spread:

1. **AxisCare** — US personal-care/private-duty home care, SMB-to-enterprise, scheduling-first all-in-one. (axiscare.com — fetched)
2. **HHAeXchange** — US payer/Medicaid/EVV-centric platform connecting providers, payers (MCOs, state Medicaid), and caregivers; HCBS framing. (hhaexchange.com — fetched)
3. **WellSky Personal Care** (ex-ClearCare) — large US incumbent for non-medical private duty; part of a suite that sells Home Health and Hospice as separate products. (wellsky.com — fetched)
4. **Birdie** — UK homecare platform (rostering/finance/quality-and-compliance; CQC context); regional check. (birdie.care — fetched)

Attempted but inaccessible (recorded per source-access limitation):
- **AlayaCare** — www.alayacare.com returned 403; help.alayacare.com transport error (2 failures → abandoned). Not used as evidence.
- **ShiftCare** — help.shiftcare.com and www.shiftcare.com both 403 (2 failures → abandoned). Not used as evidence.
- Note: birdie.ai is a different product (CX intelligence); the homecare Birdie is birdie.care.

## Sources

Tier 2 official product pages (operational feature pages with concrete workflow detail; vendor help centers largely unreachable this pass):

- AxisCare: / (root), /features/scheduling/, /features/electronic-visit-verification/, /features/billing/, /features/caregiver-app/, /features/care-plans/
- HHAeXchange: / (root), /solutions/providers/scheduling, /solutions/providers/billing-payroll
- WellSky: /personal-care-software/
- Birdie: / (root, birdie.care)

## Product A — AxisCare (US, personal care/private duty, scheduling-first)

### Key observations (evidence layer A unless noted)

- Positioning: all-in-one home care platform; modules: Scheduling, Billing, Caregiver App, Admin App, Custom Forms, EVV, Reporting; separate Skilled Care module (plan of care, practitioner orders, vitals, wound care) and IDD vertical; AI suite ("AxisCare Intelligence").
- Scheduling: client–caregiver matchmaking using availability, driving distance, preferred weekly hours, skills, overtime, schedule history, preferences (e.g., pet allergies); drag-and-drop assign/reassign; color-coded calendars; open shifts sent to caregivers via text/email/mobile app; automated caregiver recommendations; multiple caregivers or multiple clients can share one shift; real-time alerts (caregiver running behind, no-show reminders, overtime approach); 12+ scheduling reports; historical visit/schedule-change summaries; rejected shifts logged.
- EVV: captures the six data elements (services performed, individual providing, patient receiving, date, location, start/end time); clock in/out via mobile device with GPS; telephony option; auto-verification with agency-defined rules/tolerances — staff review only exceptions; client authorizations set up in minutes; real-time authorization-utilization reporting ("avoid costly overages and maximize revenue"); works with EVV vendors/aggregators HHAeXchange, Sandata, AuthentiCare, CareBridge, Netsmart; open vs closed state models; EVV exemptions for non-in-home and 24-hour services.
- Caregiver app: visit location & GPS, client notes, ADLs, care plans; clock in/out with GPS verification and secure client signatures; submit timesheets; swap shifts; view/accept open shifts; medication reminders; preferred weekly hours; permission-based visibility of client details; HIPAA framing. Tagline: "Say Goodbye to Paper Timesheets" (historical anchor).
- Billing: multiple payer sources each with own rules; hundreds/thousands of invoices monthly; in-house billing for third-party billers (Medicaid, VA, LTC insurance); one-click invoice processing; client/family payment portal (view invoices, pay, store ACH/card); QuickBooks sync; pay and bill rate adjustments per client/service/authorization; Medicaid claims + remittance tracking; VA claim reconciliation; LTCi fax claims + care notes, split bills between multiple payers; mileage/expense tracking.
- Care plans: objectives, goals, interventions per client; real-time progress monitoring; mobile documentation (works offline); customizable care plan libraries.
- Roles: schedulers, office managers, billing, caregivers, clients+families, executives, sales+marketing. Agency sizes from "up to 15 clients" to 1,000+.

## Product B — HHAeXchange (US, payer/Medicaid/EVV-centric, HCBS)

### Key observations

- Positioning: one platform connecting providers, payers, and caregivers; mission framed around home and community-based services (HCBS). Provider verticals: Personal Care, I/DD, Self Direction. Payer side: MCOs and State Medicaid Programs (network management, program integrity, BI dashboards) — a two-sided market posture unique in the sample.
- Scale stats (vendor-claimed): 2.7M caregivers clocking in/out monthly; 485M visits confirmed annually; $38B annual payments managed; 32,000+ US providers; 180+ MCOs; 30 state Medicaid programs.
- Scheduling: recurring shifts aligned with client authorizations and plans of care; matching by location, skills, preferences; real-time availability updates; "case broadcasting" of open shifts to qualified caregiver pools via HIPAA-compliant text/mobile app; overtime reduction; EVV integration → billing accuracy, fewer claim rejections.
- Billing & claims: scheduled visits validated against payer requirements up front; EVV data appears automatically after visits; automated pre-billing scrub flags claim issues before generating and securely sending the 837 claim file to the payer; 835 remittance matched against 837, reconciling claims, working denials and AR; revenue/payment/adjustment reports. "The software requires EVV-validated data and performs pre-billing checks."
- Payroll: export of caregiver work hours, pay codes, overtime, holiday pay, adjustments to payroll providers (e.g., ADP) in pre-configured format; CarePay payroll product.
- Private pay: track/manage/process transactions alongside other revenue streams; HIPAA/PCI framing.
- Compliance & state programs: EVV & Compliance module; state-sponsored EVV portal; per-state info hubs.
- Caregiver mobile app (HHAeXchange+); clinical documentation and forms module; value-based care module.

## Product C — WellSky Personal Care (US, non-medical private duty incumbent)

### Key observations

- Positioning: "purpose-built to support the unique needs of non-medical home care organizations"; "the leading solution for documenting home-based visits"; 4,000+ agencies onboarded; HITRUST CSF certified.
- Platform areas: growth analytics; staff management (applicant tracking, screening, training, safety program); AI workflows (SkySense AI: summarization, ambient documentation); caregiver engagement; family communication ("Family Room" portal: care calendar, shift notes, pay or split a portion of the bill); mobile app (ClearCareGo lineage).
- Suite boundary evidence: WellSky sells Home Health, Hospice, Personal Care as separate products — personal care vs home health are distinct product categories inside one vendor.
- Extensions (vendor-specific): CareInsights (hospitalization-risk prediction), TeamEngage (caregiver rewards), Summarize (AI care summaries), Ambient Documentation (verbal conversation → structured care documentation), Connect API.

## Product D — Birdie (UK homecare, unified platform, CQC context)

### Key observations

- Positioning: "Technology that helps homecare work smarter"; 1,000+ homecare businesses; UK social-care framing (carers, clients, CQC inspection readiness).
- Products: Care Management, Rostering, Finance (invoicing + payroll), Quality & Compliance, Workforce Experience; "three apps in one system": Agency Hub (web), Carer App (mobile, offline-capable), Family App.
- Unified records: care plans, visit notes, eMAR in a single client profile; "schedule visits that automatically connect to care plans and generate accurate timesheets"; "create invoices directly from completed visits without duplicate data entry."
- Alerts: medication alerts, late visits, client concerns; 50+ reports and dashboards (carer punctuality, visit completion rates, P&L).
- Quality & compliance: evidence gathering, issue tracking, inspection prep; predictive CQC benchmarking ("Q-Score") — regional (UK regulator) implementation of the compliance leg.
- AI: SmartPlans — records assessment conversation, drafts cited care plan for review.
- No US-style EVV observed on the fetched surface; visit times/notes/timesheets carry the service record instead. Regional confirmation that EVV is not the invariant.

## Cross-product Comparison

| Structure | AxisCare | HHAeXchange | WellSky PC | Birdie | Strength |
|---|---|---|---|---|---|
| Client roster (care recipients at home) | ✓ clients | ✓ patients/members | ✓ clients | ✓ clients | 4/4 |
| Caregiver roster (agency staff) | ✓ | ✓ | ✓ | ✓ carers | 4/4 |
| Scheduled home visit, recurring, assigned to caregiver | ✓ shifts/visits | ✓ recurring shifts | ✓ schedules/shifts | ✓ rostering visits | 4/4 |
| Client–caregiver matching (skills/location/preferences) | ✓ (AI) | ✓ criteria | implied | ✓ "better matches" | 3–4/4 |
| Open-shift broadcast / caregiver acceptance | ✓ text/email/app | ✓ case broadcasting | — | ✓ carer app | 3/4 |
| Point-of-care clock in/out (+GPS in US) | ✓ | ✓ | ✓ | ✓ | 4/4 |
| EVV six-element verification | ✓ | ✓ | ✓ (EVV mobile) | — (UK: timesheets/notes) | 3/4 US-only |
| Care plan driving visit tasks (ADLs etc.) | ✓ | ✓ plans of care | ✓ | ✓ (+eMAR) | 4/4 |
| Visit notes / care documentation | ✓ | ✓ clinical forms | ✓ | ✓ | 4/4 |
| Client signature on visit record | ✓ | implied | — | — | 1–2/4 (product-specific emphasis) |
| Authorization (authorized hours) tracking & utilization | ✓ | ✓ vs payer requirements | — | — | 2/4 (payer-context pole) |
| Billing from delivered visits (invoices and/or claims) | ✓ invoices + third-party | ✓ 837/835 claims | ✓ | ✓ invoices from visits | 4/4 |
| Payroll from verified visit hours | ✓ timesheets→pay | ✓ export/CarePay | ✓ caregiver mgmt | ✓ payroll | 4/4 |
| Family/client portal | ✓ | ✓ (mission) | ✓ Family Room | ✓ Family App | 4/4 |
| Alerts (late/missed visit, overtime, reminders) | ✓ | ✓ | ✓ | ✓ | 4/4 |
| Caregiver compliance (credentials/training/screening) | ✓ safeguards | ✓ | ✓ screening/training | ✓ Q&C | 4/4 |
| Payer-side products (MCO/state) | — | ✓ | — | — | 1/4 vendor-specific |
| Skilled/clinical extension (orders, vitals, wound care) | ✓ module | ✓ clinical module | separate product | — | 2/4 + suite split |
| IDD / self-direction vertical | ✓ | ✓ | — | — | 2/4 |
| AI assistance (summaries, drafting, matching) | ✓ | ✓ automation | ✓ | ✓ | 4/4 (era-current, B-layer commonality) |
| Recruitment/applicant tracking | ✓ (integrations) | — | ✓ | ✓ workforce | 3/4 |
| Managed RCM / billing service | ✓ | ✓ | ✓ (services) | — | 3/4 |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Four jointly-held structures:

1. **The two-sided care population of record** — the agency's clients (care recipients served in their own homes) and its caregivers (the staff who deliver that care), held as persistent identified records with care-relevant attributes on both sides.
   - Remove clients → generic HR/staff scheduling. Remove caregivers → consumer care marketplace, not agency management.
2. **The scheduled home visit as the unit of service delivery** — a dated, time-bounded appointment at a specific client's home, assigned to a specific caregiver, planned from care needs (and, where present, authorized hours); recurring patterns are the norm.
   - Remove → generic employee scheduling or appointment booking; the home as place of service disappears.
3. **The delivered-visit service record captured at the point of care** — a per-visit record of time on site and care actually delivered (tasks performed, notes; in current US implementations electronic check-in/out with location verification / EVV; historically paper timesheets signed by the client). This record is the agency's authoritative evidence that service occurred.
   - Remove → a calendar with no operating record; billing and pay lose their basis.
4. **The service-to-money translation in both directions** — revenue billed to payors/clients derived from delivered visits (client invoices, or payer claims with remittance/denial handling in payer contexts), and caregiver pay computed from the same verified visit records.
   - Remove → scheduling/documentation tool; the agency's business loop is gone.

Jointly-held is load-bearing:
- 1+2 without 3+4 = appointment calendar for care visits (thin pole)
- 3+4 without 1+2 = generic timesheet/billing system
- 1+3 without 2+4 = care documentation with no operations or money
- 2+3 without 1+4 = visit tracker with no population or business
- 1+4 without 2+3 = billing system with no care operations

### Historical / market-sample check (§24)

- Pre-digital practice: paper visit logs/timesheets signed by clients, wall schedules, invoice books, payroll from timesheets — satisfies all four legs. The sampled vendors themselves name this ancestor ("Say Goodbye to Paper Timesheets" — AxisCare; "eliminate the struggle of paper logs" — WellSky). No cloud, mobile app, GPS, or EVV in the core.
- EVV is a current regulatory implementation (US Medicaid personal-care services) of the older "proof the visit happened" — not the invariant. Birdie (UK) realizes the same leg with timesheets/notes and no EVV.
- Regional check passed: UK homecare (Birdie) fits the four legs with different vocabulary (carers, rostering, CQC) and no EVV/Medicaid.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Care plans with per-visit tasks (ADLs, meal prep, medication reminders), goal tracking, libraries/templates
- Client–caregiver matching on skills, certifications, location/driving distance, preferences, continuity
- Open-shift broadcasting to caregiver pools; caregiver shift acceptance/swaps; availability management
- Alerts: late/missed visits, no-show reminders, clock-in/out reminders, overtime warnings, medication reminders
- Family/client portal (schedules, shift notes, invoices/payments)
- Caregiver compliance: credentials/certifications with expiry, training, screening, supervision
- Authorization management: authorized hours/services vs scheduled vs delivered, utilization reporting
- Intake/assessment workflows; custom forms
- Reporting/dashboards (operations, punctuality, visit completion, revenue)
- Mileage/expense capture; QuickBooks/accounting and payroll-system integrations; CRM integrations
- Multi-branch/franchise support; role-based access

### L2 — Variant / Optional Structure

- EVV posture: built-in EVV vs integration with state aggregators (Sandata, CareBridge, AuthentiCare, HHAeXchange, Netsmart); open vs closed state models; telephony check-in as alternative to mobile app (US regulatory implementations)
- Payer mix: private-pay-first vs Medicaid/MCO-centric vs LTCi/VA-heavy; claims (837/835) machinery in payer contexts
- Verticals: IDD / self-direction programs; skilled/private-duty nursing extension (drift toward Home Health EHR)
- Payer-side platform (provider+payer two-sided network) — one vendor in sample
- AI-era capabilities: AI matching, care summaries, ambient documentation, AI care-plan drafting, care-note analytics
- Recruitment/applicant tracking, caregiver engagement/rewards, e-learning
- Managed RCM/billing services (service wrapper, not product structure)
- Regional compliance packaging: CQC quality benchmarking (UK)
- Offline mobile capability; eMAR

### L3 — Vendor-specific (research notes only)

- AxisCare: Axi AI chat assistant, AxisCare Intelligence, EVV state map, RCM service line, "12+ scheduling reports"
- HHAeXchange: CarePay, "case broadcasting" (branded), State Info Centers, program-integrity tools, payer BI dashboards, 99.9% first-pass acceptance claim, scale stats
- WellSky: SkySense AI, Family Room, CareInsights, TeamEngage, Summarize, Ambient Documentation, ClearCareGo app, HITRUST certification
- Birdie: Q-Score (CQC prediction), SmartPlans, Flock community, Birdie Academy, three-apps packaging, 0.6MB-per-report claim

## Vendor-specific Findings

- HHAeXchange is the only sampled product operating a two-sided provider+payer platform (MCO/state Medicaid products, network management, program integrity). Held as vendor-specific/variant; not promoted to core.
- AxisCare and HHAeXchange both expose skilled-care/clinical modules — evidence that the Type's edge with Home Health EHR is a real drift zone, packaged as optional modules rather than the core.
- Client signature capture on the visit record is explicit in AxisCare, implied elsewhere — held below the line.

## Boundary Findings

- **vs Home Health EHR / Management**: home health = Medicare-certified skilled clinical care (nursing/therapy), physician-ordered plans of care with certification periods, OASIS-style assessments, episode/period-of-care billing under CoPs. Home care agency management = non-medical/personal care delivered on hourly visit schedules, agency-authored care plans, no physician order required, visit/hour-based billing. Suite evidence: WellSky sells them as separate products; AxisCare/HHAeXchange package skilled care as add-on modules. Remove the caregiver-visit operating loop and center clinical assessment + physician orders → Home Health EHR.
- **vs Hospice Management**: terminal-illness interdisciplinary care under the hospice benefit, volunteer/bereavement machinery — different core objects and rules.
- **vs Employee Scheduling Platform / Workforce Management**: generic scheduling has no care recipients, no care plans, no EVV/service verification, no payor billing; home care scheduling is client-need-driven with authorizations and matching.
- **vs Staffing Agency Management System**: staffing places workers into client organizations' shifts (recruitment/placement-centric); home care delivers recurring personal-care services to individuals at home with care plans and payors.
- **vs Patient Scheduling**: books patient appointments with providers at facilities; home care schedules staff into clients' homes.
- **vs Care Coordination Platform**: cross-provider orchestration of a patient's journey (payer/provider view); not the agency's own operating system of record.
- **vs facility care (SNF/assisted living)**: place of service is the client's home, not a facility — the visit, not the bed/unit, is the operating unit.
- **"去掉什么就变成另一个 Type" 判据**: remove the home as place of service → facility/clinic scheduling; remove the care plan/service semantics → staffing; remove the two-sided population → generic scheduling; remove the money legs → care documentation tool; center physician orders + clinical assessment → Home Health EHR.

## Taxonomy note

- DIRECTORY.md keeps "Home Health EHR / Management" and "Home Care Agency Management" as separate leaves. Research supports this: different regulatory regimes, different core objects, different billing shapes; vendors themselves split them. No boundary issue to escalate; seam documented.
- Market naming variance: "home care software", "private duty home care software", "personal care software" (WellSky), "homecare" (UK) — all one Type.

## Uncertainties

- AlayaCare and ShiftCare unreachable this pass; their structures inferred only from market familiarity, not used as evidence.
- Vendor help centers (operational Tier-1 docs) largely unreachable; evidence is Tier-2 product/feature pages. Precise operational parameters (exact EVV tolerances, specific state rules, exact claim formats beyond 837/835 naming, payroll export field lists) intentionally not asserted.
- WellSky's scheduling/billing internals observed only at page level (positioning + module names), not workflow level.
- Client-signature-on-visit prevalence unconfirmed beyond AxisCare.
- UK local-authority billing specifics (council invoicing) not researched this pass.

## Final Synthesis

A Home Care Agency Management application is the agency-side operating system for delivering scheduled personal/support care in clients' homes. Its defining core is four jointly-held structures: the two-sided care population (clients + caregivers), the scheduled home visit as the unit of service delivery, the delivered-visit service record captured at the point of care (EVV being the current US regulatory implementation of an older proof-of-service practice), and the two-directional service-to-money translation (bill the payor/client from delivered visits; pay the caregiver from the same verified records). Around that core, mature products add care plans, matching, open-shift broadcasting, alerts, family portals, compliance tracking, authorization management, and reporting; variants span payer mix (private pay → Medicaid/MCO), verticals (personal care, IDD, skilled extension), regions (US EVV vs UK CQC), and AI-era assistance. The sharpest boundary is with Home Health EHR / Management (skilled clinical care under physician orders) — vendors themselves keep the two apart as separate products or add-on modules.
