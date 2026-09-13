# Research Notes — Life Sciences QMS

## Research Goal

Understand what a "Life Sciences QMS" (market name: **eQMS** — electronic quality management system) actually is as an Application Type: what records it holds, what workflows it enforces, what makes it specific to regulated life sciences (pharma, biotech, medical device) rather than generic quality software, and where its boundaries run against Manufacturing QMS, CAPA Management, GxP Training Management, Validation Management, and generic compliance/GRC tooling.

## Initial Boundary

Working hypothesis before research:

- **What**: the quality function's system of record in regulated life-sciences organizations — controlled documents (SOPs), quality events (deviations, nonconformances, complaints), CAPA, change control, audits, training, supplier quality, maintained as regulatory evidence under GxP-style regimes (FDA GMP / 21 CFR Part 11, EU GMP / Annex 11, ISO 13485).
- **Who**: quality assurance/quality control staff, document owners, auditors, management; inspectors/auditors consume the records.
- **Problem**: paper/spreadsheet quality systems fail traceability, approval control, and inspection readiness at scale.
- **Nearest types**: Manufacturing QMS (§16 sibling), CAPA Management (§16, processed), GxP Training Management (§22, processed), Validation Management (§22), Compliance Management Platform / GRC (§11), Document Management.
- **Unknowns**: which modules are definitional vs bundled; whether document control is definitional (Veeva reportedly splits it — unverified, source unreachable); the event→CAPA→effectiveness loop shape; packaging differences.

## Research Questions

1. What record classes does a life-science QMS manage, and which are universal across products?
2. What is the closed loop (event → investigation → CAPA → effectiveness)? What gates closure?
3. Is document control (SOP lifecycle) part of the defining core or a bundled module?
4. What regulatory machinery is built in (e-signatures, audit trails, validation posture, framework templates)?
5. How does change control work and how does it connect to documents/training/events?
6. What interfaces exist (queues, record detail, libraries, dashboards, admin)?
7. What distinguishes this Type from Manufacturing QMS and from generic compliance/GRC?
8. Which record classes are industry-pole-specific (device design controls vs pharma OOS/APQR)?

## Representative Products

| Product | Owner | Segment / philosophy | Evidence depth |
|---|---|---|---|
| MasterControl (Quality Excellence) | MasterControl | Enterprise suite; pharma + medtech; module suite with packaging tiers (Basic Document Management → Complete Digital QMS) | Product/solution pages (Tier 2) |
| TrackWise Digital | Honeywell (Sparta Systems) | Enterprise pharma pole; long heritage (25+ yrs), on-prem→cloud conversion; Salesforce-platform SaaS | Product/solution pages (Tier 2) |
| Greenlight Guru | Greenlight Guru | Medical-device-native eQMS; mid-market; templates + medtech-specific workflows; platform also spans product development & clinical | Product pages incl. long "what is it" definition + FAQ (Tier 2) |
| Qualio | Qualio | SMB/startup life-science eQMS; lightweight, vendor-validated, template-led; rebranding toward "compliance platform"/Compliance Intelligence | Product page + module pages (Tier 2) |

Selection rationale: market representation (all four are widely cited eQMS leaders), different customer tiers (enterprise pharma, enterprise suite, medtech mid-market, SMB), different product philosophies (suite packaging vs platform vs vertical-native vs lightweight), decent public documentation. Veeva Vault Quality — a major enterprise pharma eQMS — was **unreachable** (transport errors ×2 on veeva.com paths); the enterprise pharma pole is instead covered by TrackWise Digital.

## Sources

Research date: **2026-09-08**

- MasterControl — https://www.mastercontrol.com/quality-management-system/ , https://www.mastercontrol.com/quality/ (first URL 404'd; second fetched)
- Honeywell / Sparta Systems TrackWise Digital — https://www.spartasystems.com/trackwise-digital/
- Greenlight Guru — https://www.greenlight.guru/ , https://www.greenlight.guru/quality-management-software
- Qualio — https://www.qualio.com/ , https://www.qualio.com/product
- Veeva — https://www.veeva.com/products/vault-quality/ , https://www.veeva.com/products/quality/ — **both failed (transport errors ×2); source abandoned per network-limitation rule**

Source-access limitation: no Tier-1 operational help-center articles were fetched for any product; all evidence is official product/solution-page depth (Tier 1–2 boundary). Consequently no exact workflow state names, numeric limits, defaults, or plan-level packaging details are asserted anywhere. Veeva unreachable → enterprise-pharma-pole breadth slightly under-sampled (TrackWise covers the pole).

## Product Observations

### MasterControl — Quality Excellence (evidence layer A)

- Positioning: "#1 QMS in life sciences", 1,100+ customers "from startups to global enterprises"; industries: pharma, blood/biologics/tissue, CMO/CDMO, medical device, food & beverage, government (FedRAMP), dietary supplements, cell & gene therapy.
- Explicit framing: "close the loop on quality — from quality event management to document management and training"; "digital closed-loop quality management system".
- Suite modules: Document Control, Change Control, Training Management, Audit Management, Risk Management, Quality Event Management, Quality Management; add-ons: Postmarket, Supplier, Regulatory, Clinical, Data & Analytics. Separate suites beside QMS: Manufacturing Excellence (eDHR, MES, EBR, logbooks), Asset Excellence, Validation (a separate product line), Insights.
- Quality Event Management: "build, modify and optimize your quality event forms and workflows" with a **no-code designer**; rules-based routing; "native integrations with document management, change controls, training and exams ensures you can close the loop on quality"; AI event summaries + deviation trend identification.
- Document management: "automate version control, eSignatures, and archiving"; teams "ensure ... documents are easily searchable, traceable, and 21 CFR Part 11 compliant".
- Training: "scheduling, routing and tracking to follow-up and escalation"; role-based exams; "automatically launch training and exams from document change control, CAPAs, and production records".
- Packaging tiers: "From Basic Document Management to a Complete Digital QMS" — Basic / Standard / Complete. **Document management is the entry tier; the full QMS is the complete tier.** This is direct evidence that document control is separable from the QMS core in at least one vendor's own packaging.
- Topic pages (nav): CAPA software, Deviations Management, Nonconformance, Out of Specification.

### TrackWise Digital (Honeywell / Sparta Systems) (evidence layer A)

- Positioning: "industry-leading, cloud-based quality management system (QMS) with integrated modules"; heritage "25+ years"; on-prem → cloud conversion (Eisai case); QuickTrack packaging "for startups, small, and medium-sized businesses".
- "Core Quality Processes" enumerated on the product page:
  - **Quality Events** — "Digitize and connect quality events to quickly act on issues."
  - **Nonconformance and Out of Specification** — "Manage and trend nonconforming product, investigations and approval of resulting actions and product dispositions."
  - **Deviations** — "centralized location, with associated investigations, approvals and resulting records."
  - **CAPA** — "Fully integrated CAPA system with automated routing, notification, delivery, escalation and approval capabilities."
  - **Audit Management** — "automates audit findings, responses, corrective actions, approval and reporting."
  - **Change Control** — "from request, through pre-approvals, change execution, follow-up approvals and implementation."
  - **Document and Training Management** — DMS + TMS "automate company-wide training policies and regulatory requirements".
  - **Complaint Handling** — "the entire complaint lifecycle, from investigation to resolution".
  - plus Quality Risk Management, Supplier Quality Management, OOS, Product Registration Tracking, Recall Management, APQR/Quality Management Review (separate pages).
- Own blog framing: "closed-loop corrective action and preventive action system (CAPA)" as "the most widely-used and effective process for ensuring safety and quality management".
- Industries: pharmaceutical & biotechnology, medical devices & diagnostics, food & beverage, discrete manufacturing, consumer products.
- SGS case study: modules = "quality, complaints, documents, training, supplier quality and CAPA"; audit management for "400 audits per year".

### Greenlight Guru (evidence layer A)

- Vendor's own definitional sentence (high value): "Medical device quality management software is a cloud-based quality management system that brings **document control, training, supplier evaluation, internal audits, CAPA, complaints, risk files, design controls, and quality data into one connected system**. For medtech teams, it preserves traceability across product development, regulatory submissions, commercialization, and post-market activity... purpose-built to keep those records **audit-ready**."
- Module list: Document Control, Change Management, Training Management, Supplier Management, Quality Events (CAPAs, complaints, NCs), Parts & Inventory/BOM, Risk Management (ISO 14971, "dynamic Risk Management File"), CAPA & Nonconformance, Audit Management (internal/supplier/compliance), Design Controls & DDF.
- Quality events: "Start from best-practice templates or fully tailor event types, stages, questions, and required fields"; complaints evaluated via connected workflows to "determine whether it requires escalation, CAPA, or additional investigation"; "Every event ties directly to affected products, documents, and changes"; "sign digitally with 21 CFR Part 11-compliant approvals built into the flow".
- Change management: "evaluated for risk, training, and downstream impact"; connected records show affected SOPs/specs/training; version compare; approvals tracked.
- Training: "Tie training to document updates"; completions by person/team/document; overdue tracking.
- Audit: "Plan internal, supplier, and compliance audits; assign findings; track corrective actions; ... connect evidence"; "audit prep becomes a continuous process rather than a last-minute scramble".
- Regulatory alignment: ISO 13485:2016, FDA QSR/QMSR, EU MDR, ISO 14971:2019, 21 CFR Part 11; 80+ audit-tested SOP templates for implementation.
- FAQ posture: warns against "endless customizations" because of validation burden — a product philosophy pole (validated templates over configurability).

### Qualio (evidence layer A)

- Positioning drift visible: footer "© Qualio — QMS for Life Sciences"; hero now "The Agentic Compliance Platform for Life Sciences" with Compliance Intelligence (AI gap analysis, compliance score) — a marketing straddle toward compliance management, while the product module set remains classic eQMS.
- Module list (product page): Document management, Supplier management, Design controls, Risk management ("ISO 14971 and ICH Q9"), Training management, Change control, Audit management, CAPA & NCR ("Build automated response workflows for any quality event"), Compliance management, Analytics.
- Industries: medical devices, pharmaceutical, biotech, **cannabis**, SaMD, CROs (and cosmetics in solutions list) — adjacent regulated industries served by the same machinery.
- Compliance badges: FDA 21 CFR Part 11, EU Annex 11, ISO 27001.
- Validation approach: "We do the heavy lifting... built around the latest FDA and GAMP industry guidelines"; pre-built templates; "Only 1% of our customers choose to validate themselves" — vendor-validated posture as a selling point.
- Customer quotes evidence the lifecycle in practice: paper-to-eQMS migrations, ISO 13485 certification, MDSAP recertification audits, 510(k) preparation, "constant audit readiness".

## Cross-product Comparison

| Structure | MasterControl | TrackWise | Greenlight Guru | Qualio | Reading |
|---|---|---|---|---|---|
| Quality events (deviations/NC/OOS/complaints) | ✓ (QEM + topics) | ✓ (3 dedicated classes) | ✓ (Quality Events) | ✓ (CAPA & NCR module) | 4/4 — core |
| Investigation / root cause | ✓ (in event flows) | ✓ (investigations on deviations/NC) | ✓ (root cause analysis in CAPA) | ✓ | 4/4 — core |
| CAPA | ✓ | ✓ | ✓ | ✓ | 4/4 — core |
| Change control | ✓ (module) | ✓ (request→execution→implementation) | ✓ (risk/training/downstream impact) | ✓ | 4/4 — core |
| Audit management | ✓ | ✓ | ✓ | ✓ | 4/4 — core-adjacent (kept common) |
| Approval / e-signature control | ✓ (Part 11) | ✓ (approvals in all processes) | ✓ (Part 11 "built into the flow") | ✓ (Part 11/Annex 11 badges) | 4/4 — control layer |
| Traceability links between records | ✓ ("close the loop") | ✓ ("connect quality events") | ✓ (events tie to products/docs/changes) | ✓ ("smart links" cited by customer) | 4/4 — connective tissue |
| Controlled documents (SOPs) | ✓ (entry tier!) | ✓ (DMS module) | ✓ | ✓ | 4/4 but **separable** (MC packaging) → standard, not definitional |
| Training management | ✓ | ✓ (TMS module) | ✓ | ✓ | 4/4 but separable (module in all; standalone sibling Type exists) → standard |
| Risk management | ✓ | ✓ (QRM) | ✓ (ISO 14971) | ✓ (ISO 14971/ICH Q9) | 4/4 → standard |
| Supplier quality | ✓ (add-on) | ✓ | ✓ | ✓ | 4/4 (one as add-on) → standard |
| Complaint handling | ✓ (topic/postmarket add-on) | ✓ (dedicated lifecycle) | ✓ (dedicated) | ✓ (event class) | 4/4 → event-class standard |
| Audit trail / inspection readiness | ✓ | ✓ | ✓ ("audit-ready" repeated) | ✓ ("constant audit readiness") | 4/4 — regime anchor |
| Framework alignment (Part 11/ISO 13485/GMP) | ✓ | ✓ (GMP expertise) | ✓ (13485/QMSR/MDR) | ✓ (Part 11/Annex 11) | 4/4 — regime anchor |
| Design controls / DDF (device) | — (not on QMS page) | — | ✓ | ✓ | 2/4 → device-pole variant |
| Parts / BOM | — | — | ✓ | — | 1/4 → device variant |
| Recall management | (postmarket add-on) | ✓ (dedicated page) | — | — | enterprise extra |
| Product registration tracking | (regulatory add-on) | ✓ | — | — | 1/4 → vendor/enterprise extra |
| APQR / management review | — | ✓ (dedicated pages) | — | — | 1/4 → pharma-enterprise extra |
| Quality analytics / KPIs | ✓ (Insights) | ✓ (reporting/analytics) | ✓ (KPIs) | ✓ (Analytics module) | 4/4 → standard |
| AI assistance | ✓ | ✓ | ✓ | ✓ (agentic) | 4/4 era-current → era layer, not definitional |
| Cloud SaaS | ✓ | ✓ (Salesforce platform; on-prem heritage) | ✓ | ✓ | common-dominant; on-prem heritage exists → variant |
| Vendor-validated posture / validation support | ✓ (validation product line) | ✓ (GMP validation expertise) | ✓ (validation handled) | ✓ (vendor does validation) | 4/4 → standard capability |

Evidence layers: all observations above are directly observed (A) on official product pages; the cross-product rows generalize across the sample (B). No claim below 4/4 (except marked) is written as universal in the final document.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The quality record population of record** — the organization's quality events (deviations, nonconformances, out-of-specification results, complaints) and quality actions (investigations, corrective & preventive actions, change controls) held as individually identified, state-tracked, cross-linked records — the standing electronic record of the quality system itself. Remove → an SOP library or a static quality register; the QMS is gone.
2. **The closed-loop lifecycle machinery** — every record moves through a governed workflow enforced by the system: capture → triage/classification/risk evaluation → investigation & root cause → action → recorded approval → implementation → verification (effectiveness for actions; implementation for changes) → closure, with routing, notifications/escalation, and attributed approvals. Remove → a quality log with no process; the "management" is gone.
3. **The regulated-regime compliance anchor** — records exist as controlled regulatory evidence: every change logged, every approval attributed and signed, records linked and retained, retrievable on demand for external inspection/audit (FDA, EMA/notified bodies, ISO registrars). This is why the machinery is this formal. Remove → a generic ticketing/issue tracker with quality vocabulary.

Jointly-held is load-bearing:
- 1 alone = quality log/register (spreadsheet territory).
- 2 without 1 = generic workflow engine with nothing quality-shaped.
- 3 without 1+2 = a compliance checklist/attestation tool.
- 1+2 without 3 = generic ops issue tracking (CAPA-Management point tooling).
- 1+3 without 2 = a document store with no loop.

### L1 — Common Mature Structure (not definitional)

- Controlled document management (SOP lifecycle: authoring → review → approval → effective current version → periodic review → retirement; version control, e-signatures) — 4/4 but **separable** (MasterControl sells it as the entry tier; all vendors modularize it).
- Training management bound to documents (auto-launch from doc changes/CAPAs; completions per person; overdue/escalation) — 4/4, separable, standalone sibling Type exists (GxP Training Management).
- Audit management as a record class (plan/schedule internal & supplier audits → findings → corrective actions → evidence) — 4/4.
- Risk management (ISO 14971 / ICH Q9 framings; risk files, matrices, risk-based evaluations inside events/changes) — 4/4.
- Supplier quality management (qualification by risk, monitoring, linkage to events) — 4/4 (one positions it as add-on).
- Complaint handling as a dedicated event class with its own lifecycle — 4/4.
- Quality analytics/KPIs/trending — 4/4.
- Compliance machinery: Part 11/Annex 11 e-signature + audit-trail posture, validation support (vendor-validated delivery or validation tooling), framework-aligned templates (ISO 13485, QSR/QMSR, GMP) — 4/4.
- Design-note: audit management could arguably be raised into the core, but the sampled evidence shows it as one co-equal record class among several rather than the organizing center; keeping it common is the safer abstraction.

### L2 — Variant / Optional Structure

- Industry poles: medical-device pole (design controls/DHF/DDF, parts/BOM, post-market surveillance, EU MDR/510(k) pathways) vs pharma pole (OOS depth, batch/product dispositions, APQR, GMP focus) vs adjacent-regulated service (food & beverage, supplements, cannabis, cosmetics, CROs — all four vendors serve some).
- Deployment: cloud SaaS dominant; on-premises heritage conversion (TrackWise/Eisai case) — not definitional.
- Scale packaging: SMB template-led (Qualio, TrackWise QuickTrack, MasterControl entry tiers) vs enterprise configurable multi-site.
- Configurability philosophy: no-code form/workflow designers (MasterControl, Greenlight Guru configurable event types) vs validated best-practice templates (Greenlight Guru's own anti-customization FAQ; Qualio) — a real philosophical axis, held as variant.
- Enterprise extras: recall management, product registration tracking, APQR/management review, postmarket surveillance.
- AI assistance (summaries, trend identification, gap analysis) — era-current.

### L3 — Vendor-specific (research notes only)

- MasterControl: no-code event form designer; AI deviation summaries; separate Manufacturing (eDHR/MES/EBR), Asset, and Validation product lines; FedRAMP government packaging.
- TrackWise Digital: Salesforce-platform SaaS; Quality Process Accelerators (QPAs); Product Registration Tracking; APQR (HPQR) and HQMR pages; Recall Management; QuickTrack SMB packaging; "first AI-enabled QMS" claim.
- Greenlight Guru: living DDF with AI traceability-gap checks; design-controls + clinical EDC platform around the QMS; 80+ audit-tested SOP templates; AI training quizzes; medtech-expert support positioning; QMSR resource hub.
- Qualio: Compliance Intelligence agent (gap analysis across 30 frameworks, compliance score, cross-mapped evidence); "agentic compliance platform" rebranding; vendor-side validation ("1% validate themselves").

## §24 Historical / Market-Sample Check

Paper-era pharma/medtech quality unit: controlled-form deviation reports, CAPA logbooks, change-control forms with wet-ink signatures, investigation files, complaint files, audit files, SOP binders with revision control, inspection binders — satisfies all three L0 legs (records, lifecycle with recorded approvals, regulatory-evidence retention). No cloud, no Part 11 machinery, no risk matrices in the core. Early on-premises TrackWise (pre-cloud) satisfies. Regional EU/Asia pharma QMS products satisfy (the regime anchor is "regulated-regime evidence", not US-specific regulation). Therefore: e-signature/Part 11 machinery is held as the modern **implementation** of "attributed recorded approvals + traceability", not as the invariant; cloud is a variant; AI is era-current.

Anti-overfitting check: all four sampled products bundle document control + training; but MasterControl's own packaging (Basic Document Management → Complete QMS) proves bundling is packaging, not definition. Document control and training stay out of the core.

## Boundary Findings

- **vs Manufacturing QMS (§16 sibling)**: Manufacturing QMS centers production-floor quality (SPC, inspection, line NCRs, shop-floor metrics); Life Sciences QMS centers the regulated quality system of records (events/CAPA/change/audits as compliance evidence). Evidence of the seam: the enterprise vendors themselves sell manufacturing suites (eDHR/MES/EBR) **beside** the QMS, and both serve food & beverage/discrete manufacturing with the same QMS machinery — the regime anchor (GxP-style regulated evidence) plus record formality is what carries, not the industry label per se. Remove the regime anchor and record formality → generic manufacturing/quality tooling.
- **vs CAPA Management (§16, processed 2026-09-07)**: that pass defined CAPA as the quality-process system of record for the CAPA record itself, with "co-equal documents/training/audits = QMS" as the object-scope test. Confirmed from this side: CAPA is one record class inside this Type; standalone CAPA tooling lacks the record population (change control, audits, documents as co-equal classes).
- **vs GxP Training Management (§22, processed 2026-09-08)**: that pass set the seam "personnel loop vs quality-event loop; module-vs-Type". Confirmed from this side: training is a standard bundled module here, triggered by document changes and CAPAs, not the center.
- **vs Validation Management (§22 sibling, unprocessed)**: validating computerized systems/processes is a distinct function; the QMS supports it (document/training on validation protocols) and vendors sell validation tooling beside the QMS (MasterControl), or vendor-validate the QMS itself (Qualio). Adjacent, not overlapping centers.
- **vs Document Management / Enterprise Records (§10)**: generic controlled documents without the quality-event closed loop and without the regulatory-evidence anchor.
- **vs Compliance Management Platform / GRC (§11)**: obligations/policies/controls centered vs quality records centered; Qualio's marketing straddle (Compliance Intelligence) noted but its product module set remains quality-record centered.
- **vs Regulatory Information Management (§22 sibling)**: submissions/dossier centered vs quality records centered; TrackWise's Product Registration Tracking is an enterprise extra, not the center.
- **vs Internal Audit Management / Audit & Assurance (§11)**: audit program alone vs audits as one class among linked quality records.
- **Removal tests**: remove the event/action record population → document management + training; remove the closed-loop machinery → static registers; remove the regime anchor → generic ticketing; shift center to production-floor quality → Manufacturing QMS; shift center to design controls & product lifecycle → medical-device product development platform (Greenlight Guru's own second product is exactly that, sold separately).

## Uncertainties

- **Veeva Vault Quality unreachable** (transport errors ×2). It is a major enterprise pharma eQMS; its architecture reportedly separates document control (QualityDocs) from QMS — which would further support the "documents separable" reading — but this was **not verified** and is not relied on anywhere. Enterprise-pharma pole covered by TrackWise + MasterControl instead.
- No Tier-1 help-center articles fetched → no exact workflow state names, numeric limits, or defaults asserted anywhere; the workflow description is conceptual (capture → ... → closure) and matches vendor-described stages only at that grain.
- Packaging/pricing tiers not researched beyond MasterControl's three-tier mention.
- Audit management's exact position (core vs common) is a judgment call: 4/4 presence, but organized as one record class; kept common with reasoning recorded.
- The "Life Sciences" leaf label vs market reality: all four vendors serve adjacent regulated industries (food, supplements, cannabis, cosmetics, CROs, discrete manufacturing). The regime anchor (GxP-style regulated evidence) is the deeper invariant; "life sciences" is the center of gravity. Recorded as a mild taxonomy nuance, no directory change.

## Final Synthesis

A Life Sciences QMS is the quality function's system of record in regulated life-sciences organizations. Its defining core is exactly three jointly-held structures: (1) the quality record population — quality events (deviations, nonconformances, OOS, complaints) and quality actions (investigations, CAPAs, change controls) as individually identified, state-tracked, cross-linked records; (2) the closed-loop lifecycle machinery that moves every record from capture through investigation, recorded approval, implementation, and verification to closure; (3) the regulated-regime compliance anchor — records maintained as attributed, traceable, retained regulatory evidence, inspection-ready at all times. Controlled documents, training, risk, supplier quality, complaints-as-events, analytics, and compliance machinery (Part 11 e-signatures, validation posture, framework templates) are the standard capability layer — common and nearly universal, but modular and separable. Industry poles (device design controls; pharma OOS/APQR), deployment (SaaS/on-prem), scale packaging, configurability philosophy, and era-current AI are variants. The seams to Manufacturing QMS (production-floor center), CAPA Management (one record class standalone), GxP Training Management (personnel loop), and GRC (obligations center) are all confirmed from this side against processed neighbors.
