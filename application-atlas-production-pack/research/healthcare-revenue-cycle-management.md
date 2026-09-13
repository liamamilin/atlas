# Research Notes — Healthcare Revenue Cycle Management

## Research Goal

Understand what a Healthcare Revenue Cycle Management (RCM) application is as an Application Type: what objects it holds, what the end-to-end workflow is, who operates it, and how it differs from adjacent provider-side and payer-side money Types (practice management, provider claims management, medical coding, prior authorization, value-based care, payer claims processing).

## Initial Boundary

- Hypothesis: RCM is the provider-side machinery that turns care delivered into money received — registration/eligibility → charge capture → coding → claim → remittance → denial/AR/patient billing.
- Nearest neighbors: Practice Management System (clinic-scale money loop), Provider Claims Management (claims slice), Medical Coding Platform (mid-cycle slice), Prior Authorization Platform (front-end slice), Value-based Care Platform (arrangement-level money), Payer Claims Processing (payer side of the same claim), Hospital Management System, Patient Registration & Intake (front-end slice), Accounts Receivable Management (generic AR).
- Known pre-hung seams from prior passes: practice-management-system (payer/claim-shaped money loop already in PM core — must articulate the RCM addition), value-based-care-platform (claim-level billing loop vs arrangement-level money), hospital-management-system (front-end charge capture vs claims back office), skilled-nursing-facility-management (generic RCM vs facility census), patient-registration-intake (front-end slice).

## Research Questions

1. What is the canonical stage decomposition of the revenue cycle across products? (front-end / mid-cycle / back-end?)
2. What is the unit of record — claim, account, or encounter?
3. How do charges become claims, and how do payer payments return to the provider's books?
4. What is the exception loop (denials, underpayment, AR follow-up, patient billing)?
5. How does the software-vs-service seam work (outsourced RCM services vs software)?
6. What distinguishes RCM from practice management's money loop?
7. Would older/paper-era billing operations satisfy the definition?

## Representative Products

Chosen for market representation, different product philosophy, different customer tier:

- **Waystar** — pure-play RCM technology platform (standalone layer over any EHR/PM); health systems + practices + billing companies
- **R1 RCM** — technology-enabled RCM *services* pole (operating partnerships, full outsourcing) + AI platform; hospitals/health systems/physician groups
- **athenahealth (athenaOne / athenaIDX / athenaCollector)** — software+services hybrid; small practices → enterprise health systems
- **Epic (Resolute HB/PB/SBO)** — EHR-embedded enterprise suite pole; large health systems

## Sources

- Waystar — https://www.waystar.com/ , https://www.waystar.com/our-platform/ (fetched 2026-09-10)
- R1 — https://www.r1rcm.com/ (root 403; content via search-indexed official pages r1rcm.com/solutions/physician-rcm, /solutions/denials-management, /the-revenue-operating-system-a-new-architecture-for-healthcare-revenue-cycle, /revenue-performance/revenue-recovery, /industry-insights/ai-revenue-cycle-management-from-point-solutions-to-full-cycle-orchestration; fetched 2026-09-10)
- athenahealth — https://www.athenahealth.com/solutions/revenue-cycle-services, /solutions/revenue-cycle-management, /solutions/athenaidx, /solutions/athenaone/practice-management (via search-indexed official pages; direct fetch 403; 2026-09-10)
- Epic — https://www.epic.com/software/access-and-revenue-cycle (via search-indexed official page; direct fetch 403); Epic Resolute structure corroborated by University of Iowa Epic education site (epicsupport.sites.uiowa.edu/epic-resources/resolute), UC Davis Resolute billing audit (ucop.edu audit report), UC auditor symposium deck (ucop.edu epicrevenuecycle.pdf) — Tier 3 corroboration for an enterprise pole with no accessible operational docs
- Prior-pass inherited evidence: value-based-care-platform, practice-management-system, payer-claims-processing, health-plan-administration-system, skilled-nursing-facility-management, hospital-management-system research notes

## Product Observations

### Waystar (Layer A — official platform pages)

- Platform organized into named stage families: **Financial Clearance** (eligibility verification, patient estimation, coverage detection, charity screening, authorization, referral status, registration QA, propensity to pay, price transparency) → **Clinical Integrity + Revenue Capture** (utilization management, clinical documentation integrity, prebill anomaly detection, charge integrity, DRG anomaly detection) → **Claim + Payer Payment Management** (claim manager, claim attachments, claim monitoring, Medicare management) → **Payment Management** (payer reimbursement, remit + deposit management, EOB conversion, patient reimbursement, patient payments, agency manager) → **Denial Recovery** (denial + appeal management, recoupment manager) → **Analytics + Reporting**.
- Positions as "complete revenue cycle management suite or to elevate your existing systems" — i.e., both full-cycle and modular attachment over existing EHR/PM systems ("RCM integration with proprietary systems").
- Serves the full provider spectrum: health systems/hospitals, physician/specialty practices, ASCs, billing services, labs, DME, FQHCs, SNFs.
- Patient-side surface exists (patient payments, video EOBs, estimates) but is one stage among many.

### R1 RCM (Layer A via indexed official pages)

- Self-definition (FAQ): "RCM includes the revenue cycle processes that help providers manage payment from patient registration and insurance verification through medical billing, claim submission, payment posting, denied claims and patient billing."
- Canonical decomposition (FAQ): "connected front-end, mid-cycle and back-end functions, from patient registration, demographic and insurance information, eligibility checks and charge capture to medical coding, clinical documentation, claim submission, payment posting, denial management, patient accounts and patient payments."
- Physician RCM solution list: patient access; denial management and prevention; financial clearance; patient-friendly billing (online bill pay, payment plans, omni-channel customer service); charge capture and underpayment recovery; coding management; HIM coding review (CPT/HCPCS/DRG); payment variance analysis; strategic pricing (chargemaster + payer contracts).
- Modular pole explicitly documented: "Not every physician group needs the full spectrum… modular RCM solutions… Front-end: eligibility verification; Mid-cycle: medical coding; Back-end: denial management, claim scrubbing, and AR follow-up."
- Services pole explicitly documented: "Operating partnerships — a longer term engagement where R1 manages revenue cycle operations and employees"; LifePoint press release: "technology-enabled RCM services… end-to-end and EHR-agnostic revenue cycle solution."
- Denial management detail: technical denials (authorization, eligibility, coding, COB, billing), clinical denials/appeals, DRG/ED downgrades, aged denials (extended business office), one-time placements; AR recovery; underpayment recovery; payment variance analysis.
- "Revenue operating system sits between the EHR and payment" — positions the EHR as not designed for financial transactions across payer relationships.

### athenahealth (Layer A via indexed official pages)

- Revenue Cycle Services stage list: registration verification & co-pay collection; insurance verification & coverage scan; authorization management; charge entry and coding; claim scrub, issue resolution & submission; posting and payments; claim denials resolution; zero pay & insurance credit resolution; patient refunds; performance reporting and insights.
- Two product poles: **athenaOne** (AI-native practice management + billing for practices, with EHR) and **athenaIDX** (enterprise RCM for large practices/health systems/billing services/hospitals, interoperable with third-party EMRs); **athenaCollector** (cloud RCM for independent practices); **athenaEDI** (integrated clearinghouse services).
- athenaIDX "pre-claim readiness" (census ingestion/reconciliation, scheduling, registration, insurance selection, eligibility verification, payment estimation, quality assessments) → "clean claim production" (intelligent charge capture, coding, rules engines) → "getting to balance zero" (A/R cycles, first-pass payment).
- Services framing: "technology and expertise"; work is done by automation + athena's own teams ("low-touch… routine A/R follow-up tasks independent of your team").
- Metrics vocabulary: clean claim rate, first-pass payment rate, A/R days, cost to collect, denial rate.

### Epic Resolute (Layer A root page + Tier 3 corroboration)

- Epic positions "Access & Revenue Cycle" as a suite area: eligibility confirmation, claims payment acceleration, self-pay arrangements, patient estimates, online payment, automated registration/charging.
- Resolute = Epic's revenue cycle application: **Hospital Billing (HB)** (facility fees, UB-04-class claims), **Professional Billing (PB)** (professional fees, CMS-1500-class claims), **Single Billing Office (SBO)** (blended self-pay). (Corroborated by University of Iowa Epic education pages.)
- Core objects observed in training/audit material: **HAR** (hospital account receivable — account housing facility charges), **guarantor account** (responsible party, houses professional charges), **CSN/encounter**, **coverage**, **charge** (with Charge Router evaluating/routing/modifying charges), **Charge Description Master (CDM)** (chargemaster: pricing, procedure codes, revenue codes), **workqueues** (patient WQs, charge review WQs, claim edit WQs, insurance follow-up WQs, account WQs — the exception-management mechanism), payment posting, credits, refunds, research billing.
- Charge capture performed by clinical staff at point of care; charge lag/timeliness metrics; clean claim rate; AR days tracked separately for HB and PB.
- Epic's own framing: revenue cycle was a "patchwork quilt" of many systems before integration — the EHR-embedded pole's pitch is one system from registration to payment.

## Cross-product Comparison

| Dimension | Waystar | R1 | athenahealth | Epic Resolute |
|---|---|---|---|---|
| Packaging | standalone tech layer over any EHR/PM | services + AI platform (operating partnerships) | software+services hybrid (athenaOne/IDX/Collector) | EHR-embedded suite module |
| Stage decomposition | financial clearance → revenue capture → claims → payments → denials → analytics | front-end / mid-cycle / back-end | registration→verification→auth→charge/coding→claim→posting→denials→refunds→reporting | access → charge capture → coding → claims → posting → follow-up/denials |
| Unit of record | claim/account flows through platform | patient accounts, claims | encounters → claims → balances | HAR + guarantor account + encounter + charge |
| Exception machinery | denial + appeal management, recoupment | denials management, AR recovery, underpayment recovery | denial resolution, zero-pay/credit resolution, claim alarms | workqueues (claim edit, follow-up, denial) |
| Patient money | patient payments, estimates, EOB | patient-friendly billing, payment plans | copay/prepay/payment plans, refunds | self-pay, SBO, estimates |
| Analytics | executive dashboards, payer analytics | denial patterns, payment variance | performance reporting, payer dashboards | AR days, clean claim rate, charge lag dashboards |

Stable across all four: (1) the cycle is decomposed into front-end (pre-service clearance), mid-cycle (charge/coding), back-end (claim, remittance, denial, AR, patient billing); (2) the patient account is the persistent accumulator; (3) the charge→claim→remittance→balance chain; (4) an exception/recovery loop; (5) payer-contract-aware money (payment variance, underpayment); (6) revenue-integrity concern (missing charges, coding accuracy, chargemaster).

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The provider-side revenue cycle as a managed end-to-end money pipeline, held by four jointly-held structures:

1. **The patient account as the unit of record** — a persistent account per patient/guarantor (per care organization) onto which charges accumulate, payments and adjustments post, and balances (payer vs patient responsibility) are held across the whole cycle; the account survives from pre-service through final resolution. Remove → a claim processor or AR report with no account memory.
2. **The charge-to-claim translation chain** — billable care is captured as charges (against a chargemaster/fee schedule), coded, edited/scrubbed against billing rules, and formed into payer-directed claims. Remove → generic AR ledger, or coding tool with no money path.
3. **Remittance and balance reconciliation** — payer responses (payments, denials, adjustments) post back onto the account, splitting payer-paid vs patient-responsibility balances; the account's money state is continuously reconciled. Remove → one-way claim submission tool.
4. **The exception and recovery loop** — denials, rejections, underpayments, aged balances and patient balances are worked as managed exceptions (appeal, correct-resubmit, follow up, collect, refund) until the account reaches a resolved state. Remove → clean-claim factory with no memory of failure.

Jointly-held load-bearing: (1 alone = patient accounting ledger; 2 without 1 = claim scrubber; 3 without 1+2 = payment posting utility; 4 without 1–3 = denial analytics; 1+2 without 3+4 = charge master with no follow-up; 2+3 without 1 = anonymous transaction stream; 1+4 without 2+3 = AR tracker with no claim semantics).

Binding: provider-side healthcare money under payer contracts (remove binding → generic AR/collections; move to payer side → payer-claims-processing).

### L1 — Common Mature Structure

- Front-end financial clearance (eligibility verification, prior authorization support, patient estimation, coverage detection)
- Revenue integrity / charge capture tooling (missing-charge detection, chargemaster management, coding review)
- Denial management with root-cause analytics and appeals
- Patient financial experience (estimates, online bill pay, payment plans, financial assistance screening)
- Revenue cycle analytics (clean claim rate, A/R days, cost to collect, denial rate, first-pass payment rate)
- Clearinghouse connectivity / standardized electronic claim and remittance transactions
- Workqueue-style exception management UI

### L2 — Variant / Optional

- Packaging: standalone layer (Waystar) vs EHR-embedded suite (Epic) vs software+services hybrid (athenahealth) vs full operating partnership/outsourcing (R1)
- Hospital billing vs professional billing as separate ledgers (facility vs professional fees) or blended single billing office
- AI/agentic automation posture (R1 Phare, athena AI-native, Waystar AltitudeAI) — era-specific current-market common, not definitional
- Utilization management, clinical documentation integrity, DRG anomaly detection (mid-cycle integrity depth varies)
- Regulatory-program-specific machinery (Medicare management, price transparency, charity screening)

### L3 — Vendor-specific

- Epic Resolute HB/PB/SBO naming, HAR/guarantor/CSN/CDM terminology, Charge Router, workqueue taxonomy
- Waystar AltitudeAI™, R1 Phare/Phare Access/Claim/Flow, athenaIDX/athenaCollector/athenaEDI product names, KLAS rankings, vendor-published performance metrics

## Historical / Market-Sample Check

Paper-era provider billing office: patient ledger cards/accounts, charge tickets captured from care areas, coding against ICD/CPT volumes, claim forms (UB/CMS-1500 predecessors) mailed to payers, remittance advice posted to ledgers, denial letters appealed, patient statements and collections — satisfies all four L0 legs. Mainframe-era patient accounting systems (the "patient accounting/AR" systems that preceded the RCM name) satisfy the same core. The definition names no EDI transaction, no AI, no cloud, no specific claim form. Historical check **passed**.

## Vendor-specific Findings

- R1 explicitly documents the software-vs-service seam: operating partnerships (R1 manages revenue cycle operations and employees) vs agentic solutions; "only 10 to 15% of the provider market engages in full transitional outsourcing" — both poles in-type.
- athenahealth documents tiered packaging by customer size (athenaCollector for independents, athenaIDX for enterprise).
- Epic's pitch is consolidation ("patchwork quilt" of 20 systems → one).
- Waystar explicitly supports both "complete suite" and "elevate your existing systems" attachment.

## Boundary Findings

- **vs Practice Management System**: PM's defining money loop (eligibility → coded charges → claims → remittance posting → patient responsibility) is the same claim-shaped chain at clinic scale, embedded in practice operations alongside scheduling/charting. RCM is the dedicated revenue-cycle machinery as its own center of gravity — full front/mid/back cycle, revenue integrity, denial/AR recovery as first-class disciplines, typically at hospital/health-system/billing-company scale. Keep-both; bundling is packaging (athenaOne bundles both; Epic bundles both).
- **vs Provider Claims Management**: claims slice (submission→adjudication-tracking→remittance) vs the whole cycle including front-end clearance, charge capture, coding, patient billing. Keep-both.
- **vs Medical Coding Platform**: coding is one mid-cycle step; RCM consumes coding, does not center on it. Keep-both.
- **vs Prior Authorization Platform**: front-end slice. Keep-both.
- **vs Value-based Care Platform** (discharges pre-hung flag): RCM = claim-level fee-for-service billing loop (encounter→claim→payment); VBC = arrangement-level money (savings/losses/incentives, capitation, bundles). Keep-both RATIFIED from this side.
- **vs Payer Claims Processing**: same claim object, opposite side of the payer–provider transaction; provider submits and follows up, payer adjudicates. Keep-both.
- **vs Hospital Management System**: HMS = hospital operations of record; RCM = the money pipeline. Keep-both.
- **vs Skilled Nursing Facility Management**: SNF = census-driven facility operations with its own payer money path; generic RCM lacks the facility census. Keep-both.
- **vs Patient Registration & Intake**: front-end slice (registration/clearance), no claim/AR machinery at center. Keep-both.
- **vs Accounts Receivable Management / Collections Automation**: generic commercial AR lacks payer-contract, coding, and claim semantics. Keep-both.
- **Software-vs-service seam**: the Type includes technology-enabled services (R1 operating partnerships, athena services) — the service pole operates the same cycle with the same objects; the software core is the boundary counterparty the practice-management pass flagged. Both poles in-type; recorded as variant axis.

## Uncertainties

- Epic operational documentation not directly accessible (root page via search index; structure corroborated by Tier 3 training/audit documents) — Epic-specific object names kept out of the final document's core; used only as corroboration.
- Exact stage names vary by vendor; final document uses conceptual stage names.
- Non-US markets: sampled products are US-centric (payer/claim machinery is US-shaped). International hospital billing exists but was not directly sampled; definition kept at payer-contract abstraction level rather than US program specifics.

## Final Synthesis

Healthcare Revenue Cycle Management is the provider-side money pipeline: the application whose defining core is the patient account of record + the charge-to-claim translation chain + remittance/balance reconciliation + the exception-and-recovery loop, spanning front-end clearance, mid-cycle charge/coding, and back-end claim/denial/AR/patient-billing work, under payer contracts. Everything else — packaging, AI, specific stage products, program machinery — is common, variant, or vendor-specific.
