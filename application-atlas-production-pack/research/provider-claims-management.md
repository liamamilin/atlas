# Research Notes — Provider Claims Management

Slug: provider-claims-management
Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand the provider-side claims software Type: what the claim is on the provider's side of the payer–provider relationship, how claims are produced, submitted, tracked, reworked and resolved, and where this Type separates from its dense neighborhood (Healthcare Revenue Cycle Management, Practice Management System, Medical Coding Platform, Payer Claims Processing, Prior Authorization Platform, EDI/Clearinghouse, Insurance Claims Management).

## Initial Boundary

Initial hypothesis (Step 1):

- Core use: get coded health services turned into payer claims, submitted, accepted, paid, and reworked when rejected or denied.
- Users: medical billers, billing managers, revenue-cycle staff, billing companies, hospital patient-financial-services teams.
- Nearest neighbors: Payer Claims Processing (opposite seat), Healthcare Revenue Cycle Management (broader flow), Practice Management System (system of record that often embeds claims machinery), Medical Coding Platform (upstream), Clearinghouse/EDI (transport), Prior Authorization Platform (upstream approvals), Insurance Claims Management (P&C — different object world).
- Known unknowns: how standalone claims tools differ from clearinghouse portals; how much of the claim lifecycle is the Type vs the RCM whole; whether denial management is core or common.

## Research Questions

1. What is the claim as an object on the provider side — what data does it bind, what lifecycle does it carry?
2. How are claims created (charge entry, coding output, file import, portal forms)?
3. What happens before submission (scrubbing/edits) and why does it exist as a distinct leg?
4. How does submission work — direct-to-payer vs clearinghouse; what feedback returns (acknowledgment, rejection)?
5. How is claim status tracked, and what vocabularies are shared with the payer side?
6. How do remittances (835/ERA/EOB) return and what does the provider do with them?
7. What is the rejection vs denial distinction, and what does the rework loop look like (correct/resubmit, appeal, write off)?
8. What reporting does the Type produce (clean-claim rate, acceptance rate, aging, denial patterns)?
9. Who operates it — practices, billing companies, hospitals — and how does multi-client operation work?
10. Where are the boundaries: RCM whole vs claims slice; PM system of record vs claims machinery; clearinghouse transport vs claim lifecycle?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer level:

| Product | Pole | Customer level |
|---|---|---|
| Waystar | enterprise RCM platform / clearinghouse (Claim Manager, Denial + Appeal Management) | hospitals, health systems, practices, billing services |
| Availity | dual-sided provider–payer network with provider RCM suite | hospitals + practices (network pole) |
| Tebra (ex-Kareo) | all-in-one EHR+ platform with embedded billing/claims | independent practices + billing companies |
| Claim.MD | minimal standalone clearinghouse portal | small practices, software vendors, payers |

Historical / market-sample anchors used for the abstraction check: the paper-era billing office (typed CMS-1500/UB-04 forms, batch mailing, paper EOBs, denial letters, claim logs) and the standalone-clearinghouse generation.

## Sources

Tier 1 (official product documentation, fetched 2026-09-09):

- Waystar — Claim Manager: https://www.waystar.com/our-platform/claim-management/claim-manager/
- Waystar — Denial + Appeal Management: https://www.waystar.com/our-platform/denial-prevention-recovery/denial-appeal-management/
- Waystar — platform map (Claim + Payer Payment Management, Payment Management, Denial Recovery, Analytics): https://www.waystar.com/our-platform/claim-management/ (nav structure)
- Availity — Revenue Cycle Management (Pre-Service / Post-Service Claim Management / Post-Adjudication): https://www.availity.com/revenue-cycle-management/
- Tebra — Electronic claim submissions: https://tebra.com/billing-payments/electronic-claim-submission
- Tebra — Billing & Payments (platform root): https://tebra.com/
- Claim.MD — homepage/services: https://www.claim.md/
- X12 — Transaction Sets and code lists (Claim Adjustment Reason Codes, Claim Status Category Codes, Remittance Advice Remark Codes, Provider Adjustment Reason Codes; 276/277 claim status examples): https://x12.org/products/transaction-sets

Failed / abandoned sources (per network rule, 1–2 attempts then abandon):

- https://tebra.com/medical-billing-software/ — 404 (root page used instead)
- https://www.availity.com/availity-essentials/ — 404 (RCM page used instead)

Not attempted after sampling saturation: Office Ally, CollaborateMD, Experian Health, AdvancedMD — the four-product sample had already produced stable cross-product commonality (stop condition 4).

Boundary-consistency context (processed sibling passes):

- applications/payer-claims-processing.md + research/payer-claims-processing.md (opposite seat; its Related Types table defines this Type as "provider-side claim production and submission management vs payer-side determination and settlement")
- applications/practice-management-system.md (claim/eligibility machinery held standard-NOT-definitional for PM — supports claims machinery being its own Type)
- applications/prior-authorization-platform.md (discharged payer-claims-processing's joint-review flag; X12 corpus splits 278 review machinery from 837/835 claim machinery + 276/277 status)
- applications/insurance-claims-management.md (P&C polysemy note: "claims" in §22 vs §08/§17 are different object worlds)

## Product A — Waystar (enterprise RCM platform / clearinghouse pole)

### Key observations (evidence layer A unless noted)

- Platform map: "Claim + Payer Payment Management" (Claim Manager, Claim Attachments, Claim Monitoring, Medicare Management), "Payment Management" (Payer Reimbursement, Remit + Deposit Management, EOB Conversion + Payer Lockbox, Patient Reimbursement/Payments, Agency Manager), "Denial Recovery" (Denial + Appeal Management, Recoupment Manager), "Analytics + Reporting". Upstream legs (Financial Clearance: eligibility, authorization; Clinical Integrity + Revenue Capture: charge integrity, prebill anomaly detection) are separate platform families — claims machinery is one slice of a wider RCM suite.
- Claim Manager page (title tag: "Claims Clearinghouse"): "Get your claim right, the first time" — precise claim edits per payer using configurable rules and crowdsourced insights; Rule Manager for custom rule creation (AI-assisted); automated eligibility verification + coverage detection integration "prior to claim submission" to prevent eligibility denials; flexible claim search; "simple rejection messaging removes the cumbersome task of interpreting payer responses"; eSignature and enrollment services for payer enrollments.
- Vendor-reported metrics (marketing data, not independently verified): 98.5%+ average clean claim rate; 2.5M continuously updated edits; 5K+ payer connections; 1M+ providers; integrates with 530+ HIS and PM systems; work "in your HIS or PM system or in the Waystar interface".
- Case-study metrics (vendor-reported): clean claim rate, payer acceptance rate, denial rate, "fewer claims touched manually".
- Denial + Appeal Management page: AI + predictive analytics prioritize "denials most likely to be overturned and paid" and route them to work groups; generative AI appeal letters; library of 1K+ prepopulated payer-specific forms (vendor-reported count); paperless process + batch appeal submission; appeal tracking + proof of delivery; exception-based workflows; root-cause reporting for denial prevention; auto coverage detection for eligibility-related denials; integrates into EHR, HIS or PM.
- Companion products confirm the leg structure: Claim Monitoring (status), Claim Attachments (documentation), Remit + Deposit Management / EOB Conversion (remittance capture incl. paper EOB conversion), Recoupment Manager (payer take-backs).

## Product B — Availity (network pole)

### Key observations

- Provider RCM organized in three phases — the cleanest lifecycle articulation in the sample: Pre-Service (patient access, eligibility, authorizations — "prevent claim denials before they happen"), Post-Service Claim Management, Post-Adjudication.
- Post-Service Claim Management capabilities (named): Claims Processing — "electronically submit many types of claims, including primary and secondary paper claims"; batch claims (837); interactive claims submission (DDE — Medicare direct data entry); worker's compensation claims; claim electronic attachments. Claims Management and Editing — "AI-driven predictive editing analyzes claims before they are sent to the payer, allowing providers to manage, correct and submit cleaner claims"; ACE claim edit and rule creation; real-time claims editing. Claim Status — "Providers spend too much time calling payers to find out whether a claim has been accepted, denied, or paid"; advanced claim status, real-time claim status, claim errors (276/277/CRD).
- Post-Adjudication capabilities (named): Remit Processing — electronic remittance delivery and claim matching, paper EOB to 835 remittance advice transformation, remittance auto-posting (835), lockbox, EFT reconciliation, remit replication. Denial Management and Appeals — denial prevention and management module, appeals form API. Patient Payments. Analytics and BI.
- Dual-sided network positioning: "reach the most nationwide payers directly, reducing transaction delays"; clearinghouse & trading-partner network as the transport layer beneath.
- The pain-point framing is itself evidence of the Type's job: manual claim management "slows down reimbursements, increases denial rates"; denied claims "create administrative backlogs, lost revenue".

## Product C — Tebra (small-practice embedded pole)

### Key observations

- Billing & Payments product: "Manage claims, eligibility, and denials with integrated medical billing"; components: practice management, real-time insurance eligibility, claims management, patient payments. Claims machinery is embedded in the practice's EHR+ platform (Kareo lineage), not a standalone claims product.
- Electronic claim submissions page — the clearest end-to-end workflow statement in the sample:
  - "After entering charges and checking claims against payer reimbursement rules, you can send primary and secondary electronic claims to the clearinghouse services directly."
  - "Quickly view your claims on one screen — get an immediate snapshot of all outstanding items, rebilling efforts, and accomplished tasks."
  - Attachments "for every claim type — Commercial, Workers' Compensation and Auto Accident".
  - "Track electronic claims from submission to adjudication. Internal validation from Tebra helps you ensure patient and policy information are correct. Clearinghouse partners provide daily reports. Payers may respond with reports on any denials prior to adjudication."
  - "Automatically track rejections and denials from insurance companies. Tebra's reports make it efficient to gather missing information, correct data entry errors, and resubmit electronic claims within payers' filing deadlines."
- Serves billing companies as a distinct audience (multi-client operation); RPA offered for billing-company automation (case studies with billing companies).
- Submission goes "through our clearinghouse partner" — the embedded pole still rides clearinghouse transport.

## Product D — Claim.MD (minimal standalone pole)

### Key observations

- Positioning: "Trusted Medical Claims Clearinghouse" — "Create claims through our medical clearinghouse portal, or upload files from any Medical Billing System. View electronic remittance, check real time benefits & eligibility."
- Claim creation: portal claim entry on "CMS-1500/UB04 style claims forms with realtime validation"; file upload in many formats (837P, 837I, 5010, 4010, CSV, XLS, XML, NSF, print image) — both hand-entered single claims and large batch files.
- Rejection handling: "one of Claim.MD's most valuable features is how we return rejected claims for corrections, speeding payment and eliminating the confusion of re-billing" — the correction-and-resubmit loop is the headline feature even at the minimal pole.
- Remittance: "Download, print or view electronic payment details" — standard 835, spreadsheet and XML remittance data, PDF of payment details.
- Reports "give easy accessibility to dive directly down to the claim level detail".
- Real-time eligibility through web portal and API; per-claim/subscription pricing tiers sized to single-doctor practices up to enterprises.
- Note: at this pole the product is a clearinghouse whose portal gives providers direct claim work surfaces — the transport/lifecycle seam (see Boundary Findings #5).

## Cross-product Comparison

| Aspect | Waystar | Availity | Tebra | Claim.MD |
|---|---|---|---|---|
| Claim creation | from 530+ HIS/PM systems or in Waystar interface | batch 837, interactive DDE, paper claims | charges entered in billing module → claims checked against payer rules | portal forms (1500/UB-04 style) or file upload (837P/I, CSV, XLS, XML, NSF, print image) |
| Pre-submission editing | configurable payer edits, custom rule creation, crowdsourced insights, eligibility integration | predictive editing, rule creation, real-time editing | internal validation of patient/policy info + payer reimbursement rules | realtime validation on claim forms |
| Submission path | clearinghouse, 5K+ payer connections (vendor-reported) | dual-sided network direct to payers | via clearinghouse partner | clearinghouse |
| Feedback loop | simple rejection messaging (translated payer responses) | claim status incl. 276/277-class errors; accepted/denied/paid visibility | daily clearinghouse reports; payer pre-adjudication denial reports; track submission→adjudication | rejected claims returned for correction |
| Remittance | Remit + Deposit Mgmt, EOB conversion, lockbox | 835 auto-posting, EOB→835 transformation, remit-claim matching, EFT reconciliation | (patient-payments side emphasized) | ERA view/download/print (835, spreadsheet, XML, PDF) |
| Denial rework | AI prioritization, appeal letters, payer-specific forms, appeal tracking, root-cause reporting | denial prevention & management module, appeals form API | auto-track rejections/denials; resubmit within filing deadlines | rejected claims returned for corrections |
| Reporting | analytics suite; clean-claim/acceptance/denial metrics (vendor-reported) | executive + user-level analytics | claims snapshot on one screen; reports | claim-level detail reports |
| Deployment posture | standalone platform attached to EHR/PM | network + RCM suite attached to EHR | embedded in EHR+ platform | standalone portal |
| Customer level | hospitals/health systems → practices → billing services | hospitals + practices | independent practices + billing companies | single-doctor → enterprise |

### Cross-product commonality (evidence layer B)

Present in all four sampled products:

1. the claim as a persistent, individually addressable record (patient + payer/coverage + provider + coded service lines + charges)
2. pre-submission validation/edits against payer requirements
3. transmission toward the adjudicating party (direct or via clearinghouse)
4. feedback returning to the provider (acknowledgment / rejection / status)
5. rejection and denial capture with reasons, and a rework loop (correct & resubmit, appeal)
6. remittance capture (835/ERA/EOB-class) matched back to claims
7. claim-level reporting (aging, acceptance, denial patterns)

Present in 3 of 4 or with varying depth: eligibility integration before submission (Waystar, Availity, Tebra; Claim.MD offers real-time eligibility as a portal feature), attachments (Waystar, Availity, Tebra), payer enrollment services (Waystar explicit; others implicit), secondary claims/COB (Waystar, Availity, Tebra), AI assistance (Waystar, Availity; era-current, not definitional).

## Canonical Model (Step 5–7 synthesis)

### L0 — Defining Invariant (three jointly-held structures)

1. **The claim as the unit of record** — a persistent, individually addressable request for payment assembled on the provider side: patient, payer/coverage reference, servicing provider, coded service lines with submitted charges. The provider's claims memory lives here; every edit, submission, response, and rework attaches to it.
   - remove → charge-entry/coding tooling with no payer-facing object
2. **The payer-directed submission path with front-end quality control** — claims are validated against payer requirements (edits/scrubbing) and transmitted toward the party that adjudicates them (payer directly or via a clearinghouse), with acceptance/rejection feedback returning to the provider.
   - remove → generic EDI transport, or a claim archive with no payer path
3. **The adjudication-outcome tracking & rework loop** — each claim is tracked to a recorded outcome (paid / denied / rejected / pending), payer responses (remittance/EOB, rejection and denial reasons) are captured against the claim, and unresolved claims re-enter work: correct and resubmit, appeal, or write off.
   - remove → one-way submission drop box; the "management" is gone

Jointly load-bearing: 1 alone = claim form store; 2 without 1 = transport conduit; 3 without 1+2 = payment-posting ledger; 1+2 without 3 = submission with no memory of outcome; 1+3 without 2 = claim log with no live payer path (the paper-era pole closes this by carrying mail as the submission path).

### L1 — Common Mature Structure

- claim worklists/queues organized by status and aging; claim search
- rejection vs denial distinction with reason capture (shared standardized vocabularies: claim adjustment reason codes, claim status category codes, remittance advice remark codes)
- denial management: prioritization, work routing, appeal generation on payer-specific forms, appeal tracking, root-cause analysis
- remittance processing: electronic remittance delivery, remit-to-claim matching, posting support; paper-EOB conversion where paper persists
- eligibility verification integrated before submission
- claim attachments (commercial documentation requests)
- primary + secondary claims / coordination of benefits
- payer enrollment/enrollment services (getting providers credentialed to submit to each payer)
- reporting: clean-claim rate, payer acceptance rate, denial rate, A/R aging
- integration with EHR/PM/HIS systems of record (claims machinery attaches to where charges originate)
- multi-client operation for billing companies

### L2 — Variant / Optional Structure

- claim creation mode: in-product forms vs file import (837/CSV/print-image) vs fully embedded in PM/EHR charge entry
- deployment posture: standalone claims platform vs network portal vs embedded module vs clearinghouse portal
- AI posture: predictive editing, AI appeal letters, denial prediction (era-current)
- Medicare-specific machinery (interactive DDE, enhanced claim status)
- specialty claim types (workers' compensation, auto accident)
- paper claim print (1500/UB-04) as legacy channel
- adjacent bundled lines: patient payments/statements, patient financial care, analytics depth
- pricing models (per-claim, volume tiers, subscription)

### L3 — Vendor-specific (research notes only)

- Waystar: Rule Manager, AltitudeAI, Automation Intelligence Center, Recoupment Manager, Agency Manager, EOB Conversion + Payer Lockbox; vendor-reported metrics (98.5% clean claim rate, 2.5M edits, 5K+ payers, 1M+ providers, 1K+ appeal forms)
- Availity: ACE claim edit, Essentials/Essentials Pro/Plus portal tiers, DDE interactive claims, CRD claim errors, CMS-0053-F attachments suite
- Tebra: RPA for billing companies, volume-based claim pricing, AI Smart Staff
- Claim.MD: GetHelp tickets, NSF/print-image file formats, per-claim pricing tiers

## Boundary Findings

1. **vs Payer Claims Processing (§22 sibling, processed)** — opposite seats on the same claim. The payer side holds the claim through rule-driven adjudication to a recorded determination and settlement; the provider side produces, submits, tracks, and reworks claims against those determinations. The X12 corpus splits the same way (837 submission / 835 remittance / 276/277 status are shared rails; each side reads them from its own seat). The payer pass already documents this Type in its Related Types table ("provider-side claim production and submission management vs payer-side determination and settlement"); this pass ratifies keep-both from the provider side. Failure test: remove adjudication/settlement from a payer system and it stops being payer claims processing; remove production/submission/rework from a provider system and it stops being provider claims management. Neither can perform the other's job.
2. **vs Healthcare Revenue Cycle Management (§22 sibling)** — slice vs whole. RCM spans pre-service financial clearance → charge capture/coding → claims → payment posting → patient collections → analytics. Claims management is the claims slice, independently purchasable and operable (Claim.MD; standalone clearinghouse portals; Waystar sells Claim Manager as a package). RCM platforms bundle the slice; the slice remains a distinct Type because its unit of record (the claim) and its loop (submit→track→rework) exist independently of the wider cycle. Consistent with the practice-management pass holding claims machinery standard-not-definitional for PM.
3. **vs Practice Management System (§22 sibling, processed)** — system of record vs attached machinery. The PM holds patients, appointments, charges; its billing loop produces claims. Claims machinery may be embedded in the PM (Tebra) or attached externally (Waystar integrates with 530+ HIS/PM systems; Claim.MD accepts uploads "from any Medical Billing System"). The seam: where does the charge originate and where does the practice's administrative record live (PM) vs where does the payer-facing claim work happen (this Type).
4. **vs Medical Coding Platform (§22 sibling)** — upstream producer. Coding produces the coded service lines; claims management consumes them into claims. Some vendors bundle both; the objects differ (code assignment vs claim lifecycle).
5. **vs EDI Platform / Clearinghouse (§13/§14 neighbors)** — transport vs claim lifecycle. A clearinghouse moves and validates transactions between trading partners; claims management centers the provider's work on claims. Claim.MD straddles: a clearinghouse whose portal gives providers direct claim entry, correction, and ERA viewing — the portal side is this Type's work; the transport side is the clearinghouse's. Seam test: does the product center the provider's claim worklist and lifecycle, or the transaction conduit between systems?
6. **vs Prior Authorization Platform (§22 sibling, processed)** — upstream approval machinery. Authorization status is an input to claims (and eligibility-related denials route back to coverage checks), but the review-to-determination loop is a different discipline (278-class machinery vs 837/835/276/277-class machinery).
7. **vs Insurance Claims Management (§08, processed) / Claims Adjuster Platform (§08, processed)** — different object worlds: loss events, adjusters, reserves vs coded health service lines and billing offices. Polysemy note already recorded by the claims-adjuster pass; no merge risk.
8. **vs Construction Claims Management (§17)** — contract disputes; entirely different world. Same word, no overlap.
9. **vs Patient Payments / Patient Financial Care** — downstream patient-side money; often bundled in the same RCM suites but a different counterparty (patient vs payer) and different object (patient balance vs payer claim).

## Historical / Market-Sample Check (§24)

- Paper-era billing office: typed CMS-1500/UB-04 claim forms (the claim record), batch mailed to payers (the submission path), paper EOBs and denial letters returned and filed (outcome capture), corrected claims resubmitted and appeals written (rework), claim logs and aging ledgers (reporting). All three L0 legs hold with no electronics. Electronic clearinghouses, 837/835 transactions, scrubbing engines, and AI are era machinery, not definitional.
- Standalone-clearinghouse generation (Claim.MD pole) and embedded-PM generation (Tebra/Kareo lineage) both satisfy the core despite very different packaging.
- Regional check: the researched sample is US-shaped (CMS-1500/UB-04, 837/835, clearinghouse economics). Non-US statutory/social-insurance billing regimes plausibly realize the same core (provider submits payment requests to an adjudicating authority and tracks outcomes), but this is an inferred abstraction, not observed — recorded as an uncertainty.

## Uncertainties

1. Help-center depth (step-by-step UI workflows, exact status vocabularies per product) was not reachable; all observations come from official product pages. Assertion strength kept at product-page level; no precise numeric limits, time windows, or default settings stated in the final document.
2. Vendor-reported metrics (clean-claim rates, edit counts, payer counts, form-library sizes) are marketing data — recorded here, excluded from the final document.
3. Non-US regimes unobserved; the Type is documented from a US-shaped sample.
4. The exact split of "claim status" machinery between clearinghouse, portal, and payer systems varies by product; documented conceptually (status is externally visible; 276/277-class exchanges exist) without claiming a specific realization.
5. Whether "claim monitoring" (proactive status polling) is universal or a Waystar/Availity-class capability — only 2 of 4 sampled products name it explicitly; held as common-mature, not definitional.

## Final Synthesis

Provider Claims Management is the provider-side claims system of work: it assembles coded services into claims, gets them through payer front-end validation and submission, tracks each claim to a recorded adjudication outcome, captures what payers pay and why they don't, and drives the rework loop (correct/resubmit, appeal, write off) until the claim resolves. Its defining core is the claim record + the payer-directed submission path with front-end quality control + the outcome-tracking and rework loop. Everything else — AI editing, appeal-letter generation, eligibility integration, attachments, Medicare machinery, patient payments — is mature structure or variant machinery. The Type sits between the practice's system of record (where charges originate) and the payer's adjudication machinery (where determinations happen), and is packaged in the market as embedded modules, standalone platforms, network portals, and clearinghouse portals.
