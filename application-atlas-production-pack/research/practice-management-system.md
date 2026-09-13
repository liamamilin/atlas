# Research Notes — Practice Management System (Healthcare)

Research date: 2026-09-09
Leaf: Practice Management System (DIRECTORY §22 Healthcare & Life Sciences)
Slug: practice-management-system

## Research Goal

Understand what a healthcare Practice Management System (PM) actually is as an Application Type: what objects it is built from, what its defining business loop is, how it relates to the EHR it is so often bundled with, and where its boundaries sit against Patient Scheduling, Healthcare Revenue Cycle Management, Hospital Management System, Patient Registration & Intake, and the cross-profession "practice management" family (law / massage / immigration) already documented in the Atlas.

## Initial Boundary

Working hypothesis before research:

- A healthcare PM is the **business/administrative-financial system of record for an ambulatory care practice** — the "PM" in the classic "EHR + PM" pairing.
- Core suspects: patient registration records, appointment scheduling, insurance eligibility, charge capture, claims, payment posting, patient statements, A/R, reporting.
- Nearest neighbors: EHR (clinical record), Patient Scheduling (booking machinery), Healthcare RCM (money cycle as discipline/service), Hospital Management System (institution scale), Patient Registration & Intake (encounter preparation), Medical Coding Platform (coding workbench).
- Known family pattern: the Atlas already holds Law Practice Management System (client + matter + file + money loop), Immigration Practice Management (practitioner caseload), Massage Practice Management (appointment-business core). Healthcare PM is presumably the same genus with a payer/claim-shaped money loop.
- Open question: is the appointment part of the defining core, or is PM essentially billing + registration with scheduling as an add-on? Is the claim machinery definitional or region/payer-model dependent?

## Research Questions

1. What is the unit of work a PM advances? (appointment? encounter? claim? invoice?)
2. What is the patient record in a PM — administrative identity, or clinical chart?
3. How does the money loop work: charges → claims → payments → balances? Which parts are US-payer-specific vs generic?
4. What does the front desk do day-to-day in a PM?
5. Where exactly is the seam vs EHR, and how do vendors themselves package the two?
6. Where is the seam vs standalone Patient Scheduling, vs RCM services, vs Hospital Management Systems?
7. Would a paper-era practice, a cash-only/direct-pay practice, and a non-US practice still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophy, and different customer tiers:

| Product | Tier / philosophy | Why sampled |
|---|---|---|
| AdvancedMD | PM-first ambulatory suite (independent + group practices; billing-company heritage since mid-90s) | The vendor's own taxonomy names "Practice Management" as a distinct pillar beside EHR and Patient Engagement |
| Tebra (formerly Kareo + PatientPop) | Independent-practice all-in-one platform; billing/PM heritage | Documents billing/PM decoupled from EHR via integration ("use billing without switching your EHR") |
| Jane App | Small-clinic / wellness / allied-health booking-first platform (CA/US/UK) | Base plan = schedule + patients + payments; insurance billing is an explicit add-on — proves claim machinery is not the base invariant |
| eClinicalWorks | Large ambulatory EHR+PM suite | Vendor explicitly contrasts "self-service Practice Management model" vs "RCM Service model" |

Attempted but excluded: **athenahealth** — www.athenahealth.com and /products/athenaone both returned HTTP 403 (two attempts). Recorded as a source-access limitation; no athena-specific operational claims are made anywhere in this research.

## Sources

Tier 1 (official operational documentation):

- Jane App — Jane's Guide (user guide): https://jane.app/guide
  - Front-Desk Training Chapter 1: Schedule — https://jane.app/guide/chapter-1-schedule
  - Front-Desk Training Chapter 3: Payments — https://jane.app/guide/chapter-3-payments
  - US Insurance Billing Training (category + 13 articles) — https://jane.app/guide/category/us-insurance-billing-training
- Tebra — Help Center index: https://helpme.tebra.com/ (linked from site; article-level pages not fetched)

Tier 2 (official product pages):

- AdvancedMD — homepage + Practice Management & Medical Billing pillar page: https://www.advancedmd.com/ , https://www.advancedmd.com/medical-billing/
- Tebra — homepage + Billing & Payments: https://www.tebra.com/ , https://www.tebra.com/billing-payments
- eClinicalWorks — Products & Services overview + RCM: https://www.eclinicalworks.com/products-services/ , https://www.eclinicalworks.com/products-services/revenue-cycle-management/

Tier 3: none needed; official material was sufficient.

Internal cross-references (Atlas): applications/electronic-health-record-ehr.md, applications/patient-scheduling.md, applications/patient-registration-intake.md, applications/hospital-management-system.md, applications/law-practice-management-system.md, applications/massage-practice-management.md, applications/immigration-practice-management.md, applications/medical-coding-platform.md (STATUS.md entries).

## Product A — AdvancedMD

### Key observations (evidence layer A unless noted)

- Vendor's own navigation taxonomy: three product pillars — **Practice Management** (under /medical-billing/), **EHR Software**, **Patient Engagement**; plus **Revenue Cycle Management** as an outsourced *service*. PM and EHR are separate pillars sold beside each other. (A)
- PM pillar sub-features (official nav + PM page): Scheduling Software, Billing Software, Reporting & Analytics, A/R Control Center, Central Billing Office, Electronic Remittance Advice, Claims Management, Credit Card Processing, Invoicing, eEligibility, Medical Billing Clearinghouse, Medical Coding, Period Close Automation, Patient Room Tracking. (A)
- PM page ("Modern front office features"): Scheduling; Insurance Verification ("automatically verifies insurance coverage for each patient prior to the appointment and updates patient files"); Copay Collection ("post payments to patient accounts during check-in"); **Charge Entry** ("use our online charge slips to post procedure, diagnosis or modifier codes"); Check-in Kiosk; Reporting. (A)
- Positioning: "unified, AI-enabled EHR, practice management, and patient engagement" platform for independent practices; 13,000 practices / 850 billing companies (marketing figures — recorded, not asserted as fact in final doc). (A, marketing)
- FAQ (official): "Our AdvancedMD billing software lets your practice manage claims, denials, and payments in-house using tools like eligibility, claims scrubbing, and dashboards, while our AdvancedMD RCM services let practices outsource the revenue cycle entirely, so an expert team manages claims, denials, posting, and collections on their behalf." — direct vendor statement of the software-vs-service seam. (A)
- Company history page: "Dating back to the mid 90s, our focus has been to offer best-in-class billing solutions for private practices." — billing-first heritage. (A)
- Billing-company pole: Central Billing Office — "manage each provider, practice and location within a single database, with a single login" — multi-client operation as a first-class mode. (A)

## Product B — Tebra

### Key observations

- Platform framing: "EHR+ platform connects care, billing, scheduling, and more." Pillars: EHR, Billing, Payments, Patient Experience, Practice Marketing. (A)
- Billing & Payments pillar bullet list includes **"Practice management"** alongside real-time insurance eligibility, claims management, patient payments — the vendor itself treats PM as the billing-side capability set. (A)
- Billing page feature set: automated insurance eligibility ("instantly check coverage, copays, and deductibles"); electronic claim submission ("automatically detect and correct common errors before submission; apply payer-specific rules"; batch claims); patient payments (payment links, card-on-file, reminders); automated patient statements ("clearly break down charges, insurance coverage, and balance"); RPA (auto-post ERAs, auto-post unapplied payments); A/R dashboard ("surface denial patterns and A/R trends"). (A)
- FAQ (official): "Medical billing software is RCM technology that helps healthcare practices and billing companies manage claims, verify insurance in real-time, post ERA/EOBs, track payments, and flag denials. Linked to your EHR, it tracks each claim, from patient eligibility checks to final reimbursement." (A)
- FAQ (official): "Can I use Tebra billing without switching my EHR? Yes. Tebra works with most major EHRs via HL7/FHIR or API bridges." — PM/billing decoupled from the chart is a supported deployment. (A)
- FAQ (official): eligibility mechanics — "sends an ANSI-X12 270 inquiry to 2,700+ payers and gets a 271 response in seconds — verifying active coverage, copay, deductible, and coinsurance." (A; precise figures are vendor marketing — kept out of final doc)
- Three billing postures sold side by side: in-house billers / outsourced billing partners / billing companies ("manage all clients in one dashboard, regardless of EHR"). (A)
- G2 category badges displayed: "Leader in Medical Practice Management and Billing", "Revenue Cycle Management High Performer" (third-party category naming — corroborates market naming). (A)

## Product C — Jane App

### Key observations

- Base plan structure: Schedule, Charting, Payments, Reporting, Patient/Staff profiles; **Insurance billing is an add-on** ("the insurance add-on can be added to the Practice or Thrive plans"; removing it hides insurance features/data). — direct evidence that the claim machinery is optional packaging, not the base invariant. (A)
- Front-Desk Training Ch.1 (Schedule): practitioner **shifts** define bookable capacity ("Patients booking appointments online can only book appointments within the practitioner's shift"; staff may be allowed/disallowed to book outside shifts by setting); booking = click open time → New Appointment panel → search patient → choose treatment → adjust time → optionally select a claim; appointment statuses **Arrived / No Show** with color states; "Arrived" and "No Show" **automatically creates an invoice for the appointment**; appointment notes (administrative, internal-only); Tasks; Breaks (holidays, lunches, admin holds); group appointments/classes; rooms. (A)
- Front-Desk Training Ch.3 (Payments): "Arriving an appointment tells Jane the patient attended their session and is now ready to be billed"; "Jane's billing is built right into the main schedule"; Pay button → Receive Payment screen listing **all outstanding invoices on the patient's account**; payment methods incl. terminal, card-on-file; **partial payment** (collect part, leave balance); **adjustments/discounts**; **patient credits & owings** (account balances); refunds (unlink payment from invoice → refund); product returns. (A)
- US Insurance Billing Training (13 articles): setup sequence — add insurers → set clinic fees with **CPT codes** ("CPT codes are required to have an assigned fee for claim submission") → business/location/staff identifying info for **CMS-1500 (paper) and EDI** submissions → put insurance policy on patient profile → attach CPT + diagnosis codes → **"insure the visit"** → claims managed under the main **Billing tab** → **837p EDI generation** ("an electronic version of a CMS1500 form"; select a batch of claims and submit) → **posting insurer payments & EOBs** (two posting paths by remittance type) → **resubmissions & corrected claims** after clearinghouse/payer rejections. (A)
- Regional breadth: separate guide categories for Canadian insurance (incl. Teleplan), US insurance, UK insurance — same visit economy, different claim machinery per region. (A)
- Other clinic-management features in guide: packages & memberships, gift cards, payroll, intake forms, telehealth, waitlists, reminders, patient app. (A)

## Product D — eClinicalWorks

### Key observations

- Positioning: "comprehensive Electronic Health Record and Practice Management solutions... from scheduling and check-in through documentation, labs, prescribing, billing, and follow-up" for independent ambulatory practices. (A)
- RCM section (official): "eClinicalWorks is one of the few vendors... that offers clients a choice of RCM solutions — **a self-service Practice Management model in which you handle your own billing, or an RCM Service model** in which eClinicalWorks provides a complete end-to-end solution for your practice." — second independent vendor statement of the PM-software vs RCM-service seam. (A)
- RCM features: alerts dashboards, performance evaluation tools, KPI monitoring, "Reduce Days in A/R", robust reporting. (A)
- Suite breadth beside EHR/PM: Patient Engagement (portal, kiosk/check-in, telehealth, messenger campaigns, healow apps), Value-Based Care (ACO/CIN, CCM, HEDIS, PCMH, HCC coding, care planning), interoperability, hospital management solution. (A)
- "98% or higher first-pass acceptance rate" — vendor marketing claim; recorded here only. (A, marketing)

## Cross-product Comparison

| Structure / capability | AdvancedMD | Tebra | Jane | eCW | Layer |
|---|---|---|---|---|---|
| Persistent patient record anchoring appointments/invoices/claims | ✓ (patient files updated by eligibility) | ✓ (patient payments on accounts) | ✓ (patient profile: policies, invoices, credits/owings) | ✓ | B |
| Appointment book as daily operating surface (provider × visit type × time) | ✓ (Scheduling pillar) | ✓ (scheduling in platform) | ✓ (shifts + booking, Tier-1 depth) | ✓ ("scheduling and check-in") | B |
| Arrival/check-in state turning the visit into a billable object | ✓ (copay collection during check-in; charge entry) | ✓ (eligibility at front desk; claims from visits) | ✓ (Arrived → invoice auto-created; Pay in appointment panel) | ✓ (check-in → billing) | B |
| Charge capture with procedure/diagnosis coding | ✓ (charge slips: procedure/diagnosis/modifier codes) | ✓ (claims by CPT; adjust claims by CPT codes) | ✓ (CPT + diagnosis codes on insured visits; fees per CPT) | ✓ | B |
| Claim generation & submission (paper + EDI/clearinghouse) | ✓ (claims mgmt, clearinghouse, CMS-1500-class) | ✓ (electronic claim submission, scrubbing, payer rules) | ✓ (837p generation, CMS-1500, clearinghouse rejections) | ✓ | B |
| Insurance eligibility verification | ✓ (eEligibility, pre-appointment) | ✓ (real-time 270/271) | ✓ (US/CA/UK insurance add-on) | ✓ (implied in RCM) | B |
| Payment posting (insurer remittance + patient payments) | ✓ (ERA, credit card processing, invoicing) | ✓ (ERA/EOB posting, patient payments) | ✓ (posting insurer payments & EOBs; patient payments) | ✓ | B |
| Patient statements / balances / collections | ✓ (invoicing, A/R Control Center) | ✓ (statements, A/R dashboard) | ✓ (statements via Pay Balance email; credits & owings) | ✓ (A/R reduction) | B |
| Denials / rejections handling | ✓ (claims mgmt, denials) | ✓ (denial tracking, resubmission) | ✓ (resubmissions & corrected claims) | ✓ | B |
| Financial & productivity reporting | ✓ (BI/reporting) | ✓ (A/R dashboard) | ✓ (Reports) | ✓ (KPIs, dashboards) | B |
| Clinical charting (EHR) | separate pillar | separate pillar | separate module (Charting) | separate pillar | B — packaging, not PM identity |
| Patient self-scheduling / self check-in | ✓ (self-scheduling, kiosk) | ✓ (online scheduling, digital intake) | ✓ (online booking, self check-in) | ✓ (healow check-in) | B |
| Reminders / waitlists / no-show management | ✓ | ✓ (smart reminders) | ✓ (Tier-1) | ✓ | B |
| Multi-location / multi-provider configuration | ✓ (multi-site mgmt) | ✓ | ✓ (locations in schedule) | ✓ | B |
| Role separation (front desk / biller / provider / admin) | ✓ | ✓ | ✓ (front-desk vs practitioner training tracks; access levels) | ✓ | B |
| Insurance billing as *optional add-on* | — (core) | — (core) | **✓ explicit add-on** | — (core) | A — single-product, but structurally decisive |
| Billing-company multi-client mode | ✓ (Central Billing Office) | ✓ (billing companies) | — | — | B |
| RCM as outsourced service beside the software | ✓ (Managed Billing) | ✓ (outsourced partners) | — | ✓ (RCM Service model) | B |
| Packages/memberships, payroll, marketing, telehealth, portal | ✓ (PE pillar) | ✓ (marketing, AI) | ✓ (packages, payroll, websites) | ✓ (engagement, VBC) | B — suite extensions |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

The healthcare Practice Management System is the ambulatory practice's **administrative-financial system of record**. Three jointly-held structures; remove any one and the product stops being recognizable as a PM:

1. **The registered patient of record** — a persistent administrative patient record (identity/demographics, contacts, coverage and financial-responsibility information) that anchors appointments, invoices, claims, and balances. Not the clinical chart — the business identity. Remove → anonymous booking and billing tools with no patient memory.
2. **The scheduled visit as the unit of work** — the appointment book binding patient × provider × visit type × time, advancing through arrival/completion; arrival converts the booking into the practice's billable encounter. The book is the practice's daily operating rhythm, not just a calendar. Remove → standalone billing/claims tooling (RCM/billing territory) or a bare calendar.
3. **The visit-to-money loop** — services rendered on the visit are captured as charges (procedure/diagnosis-coded where payer billing applies), resolved into payer claims and/or patient payments, and balances are tracked on the patient account to resolution. Remove → scheduling/registration tooling with no business loop.

Jointly-held load-bearing:
- 1 alone = patient roster / CRM
- 2 without 1 = anonymous booking (generic appointment scheduling)
- 3 without 1+2 = standalone medical billing software
- 1+2 without 3 = front-desk diary with no revenue consequence
- 1+3 without 2 = billing operation with no daily operating rhythm
- 2+3 without 1 = anonymous billing

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Insurance eligibility verification before/at the visit (3/4 sampled as core; Jane ships it inside the insurance add-on)
- Claim scrubbing / payer-specific rules before submission
- Clearinghouse-mediated electronic submission (837P-class) alongside paper claim forms
- Electronic remittance posting (ERA/EOB) and insurer payment posting
- Patient statements, card-on-file / online patient payments, payment plans
- Denials/rejection worklists, resubmission/corrected-claim handling, A/R dashboards
- Financial and productivity reporting/analytics
- Appointment reminders, waitlists, no-show handling
- Multi-provider / multi-location configuration; provider schedules/shifts as capacity
- Role-based access across front desk, billers, providers, administrators
- Patient self-scheduling and self check-in surfaces
- Referral/authorization capture in payer-context deployments

### L2 — Variant / Optional Structure

- **Claim machinery depth itself** — region- and payer-model-dependent: US commercial/Medicare claims, Canadian provincial submission (e.g., Teleplan), UK insurance, cash/direct-pay/concierge practices running the loop with patient payment only. Jane's add-on packaging is the cleanest evidence.
- **Clinical charting** — bundled EHR is packaging, not PM identity (AdvancedMD and eCW sell EHR as a separate pillar; Tebra supports billing without switching EHRs).
- **Suite extensions** — patient portal/engagement, telehealth, marketing/reputation, payroll, inventory/products, population-health/value-based-care modules.
- **Operating posture** — in-house billing vs outsourced RCM service vs billing-company multi-client operation (Central-Billing-Office-style).
- **Deployment** — cloud SaaS vs legacy client-server/desktop lineage.
- **Specialty packaging** — mental health, PT, primary care, dental-adjacent wellness, etc.

### L3 — Vendor-specific (research notes only)

- AdvancedMD: A/R Control Center, Central Billing Office, Period Close Automation, Patient Room Tracking, AdvancedBiller partner program, ODBC/data-warehouse access.
- Tebra: RPA auto-posting (ERA, unapplied payments), AI Smart Staff, billing calculators, "2,700+ payers" claim.
- Jane: Jane Payments (terminal, AVS, card-on-file), packages & memberships, gift cards, Jane Payroll, Jane Sidekick, demo-clinic training model.
- eClinicalWorks: Sunoh.ai scribe, Eva virtual assistant, healow family (apps, check-in, Genie contact center), "98% first-pass acceptance" claim.
- athenahealth: not researched (403 ×2) — no claims made.

## Evidence → Assertion Calibration

- L0 legs rest on layer-B evidence (all four sampled products) plus layer-A Tier-1 workflow evidence from Jane (appointment→invoice→payment→balance chain documented step-by-step) and vendor-official PM feature enumerations from AdvancedMD/Tebra/eCW.
- The "claim machinery is not definitional" finding rests on single-product structural evidence (Jane's add-on packaging) corroborated by cross-product regional breadth (CA/UK guide categories) and the existence of cash/direct-pay postures; asserted as variant, not invariant.
- No precise numeric limits, rates, or payer counts from vendor marketing are promoted to the final document.
- athenahealth inaccessible: no athena-based assertions anywhere.

## Historical / Market-Sample Check

Paper-era solo practice (mid-20th century, no software): appointment book (provider columns × time slots), patient card/index (demographics, insurance card photocopy), charge ticket / superbill per visit, day sheet summarizing the day's charges and payments, paper claim forms mailed to payers, payment-posting log, patient statements. All three L0 legs are satisfied with no software, no EDI, no eligibility API. The 1990s Windows-era billing-first PM generation (the lineage AdvancedMD itself claims) fits with scheduling + billing + claims. Non-US regimes (Jane's CA/UK insurance categories; provincial submission) fit with different claim machinery. Cash-only/direct-pay practices fit with the loop reduced to charges → patient payment. Conclusion: the definition survives the historical and regional checks; claim/eligibility machinery stays out of L0.

## Vendor-specific Findings

See L3 above. Additionally: the market itself realizes "practice management" as (a) a standalone billing-first product family, (b) a pillar inside EHR suites, and (c) a booking-first clinic platform for wellness — three packaging poles of the same core.

## Boundary Findings

- **vs Electronic Health Record** — sharpest seam. EHR = the clinical chart of record (problems/medications/notes, encounter-based clinical documentation). PM = the business record (registration, schedule, charges, claims, payments). The two are frequently bundled ("EHR + PM"), but vendors sell them as separate pillars (AdvancedMD, eCW) and support decoupled deployment (Tebra: billing without switching EHRs, via HL7/FHIR bridges). The EHR pass itself held scheduling/billing as non-definitional for EHR. Test: remove the money loop and the business schedule-of-record, keep the chart → EHR; remove the chart, keep the business loop → PM.
- **vs Patient Scheduling** — the scheduling pass already held: native scheduling module = embedded realization inside PM/EHR; standalone Type justified where booking/access machinery is the center. PM's center is the whole business loop; scheduling is one leg of it. Test: strip charges/claims/payments from a PM → Patient Scheduling territory.
- **vs Healthcare Revenue Cycle Management** — two independent vendors document the seam explicitly (AdvancedMD FAQ: in-house software vs outsourced RCM services; eCW: "self-service Practice Management model" vs "RCM Service model"). PM is the practice-operated software loop; RCM (as a Type) is the revenue cycle as a managed discipline/service with back-office depth (denials strategy, analytics, outsourced operations). Test: outsource the loop's operation to a service → RCM territory; run it in-product → PM.
- **vs Hospital Management System** — the HMS pass held "2+3 without 1 = clinic/practice-management scale" and named Practice Management as the practice-scale sibling. HMS = institution of record (departments, wards+beds, multi-department operations); PM = ambulatory practice scale without ward/bed machinery. Test: add wards/beds/multi-department institutional operations → HMS.
- **vs Patient Registration & Intake** — intake owns encounter-preparation record creation (who the patient is, coverage capture before the visit); PM owns the whole business loop that intake feeds. Intake is one upstream step realized inside PMs and as standalone products.
- **vs Medical Coding Platform** — coding is one step in the PM's charge pipeline (charge entry → codes → claim). The coding pass defined the coding function's own workbench; PM merely consumes codes.
- **vs cross-profession practice-management family** — Law LPM (client + matter + file + money loop), Immigration PM (caseload), Massage PM (appointment-business core) share the genus: client/patient records + appointments + service delivery + money. Healthcare PM's distinctive legs: the clinical visit economy and the payer/claim-shaped money loop. The massage pass already recorded the seam ("clinical packaging pole sits on the seam with §22 Practice Management but keeps the visit economy central"). Keep-both across professions; the genus is real but the payer/claim machinery and clinical anchoring justify separate Types.
- **vs Professional Services Automation** — project/engagement-billable work vs visit-based care delivery; different unit of work and different money loop.

## Uncertainties

- athenahealth — a major PM/EHR/RCM vendor — could not be reached (403 ×2). The sample therefore lacks the largest cloud-suite pole; mitigated by eCW covering the large-suite pole and by the consistency of the other four.
- Enterprise/hospital-employed practice PM (hospital-owned clinics billing through the hospital's system) was not directly sampled; the hospital-side seam is held via the HMS pass's own boundary statement.
- Exact claim-format/regional machinery details (e.g., provincial submission specifics beyond Jane's Teleplan category existing) were not verified at article depth; asserted only at "regional claim machinery varies" strength.
- Whether patient self-scheduling has become universal was not measured; held as common, not universal.

## Final Synthesis

The healthcare Practice Management System is the ambulatory practice's administrative-financial system of record. Its defining core is the conjunction of three structures: the registered patient of record, the scheduled visit as the unit of work (arrival converting booking into billable encounter), and the visit-to-money loop (charges → payer claims and/or patient payments → balances tracked to resolution). Everything else the market associates with PM — eligibility, scrubbing, clearinghouse EDI, ERA posting, statements, denials worklists, reporting, reminders, self-scheduling — is standard mature capability; the claim machinery itself is region/payer-model variant (Jane's add-on packaging is the decisive evidence); the clinical chart belongs to the EHR and its bundling is packaging; RCM-as-service, hospital scale, intake, and coding are neighboring Types with documented seams. The paper-era practice and the cash-only practice both satisfy the core, which passes the historical and regional checks.
