# Research Notes — Healthcare Quality Management

## Research Goal

Understand what "Healthcare Quality Management" software actually is as an Application Type: what objects exist inside it, who uses it, how quality work flows through it, and where its boundaries lie against neighboring healthcare Types (Infection Prevention, Life Sciences QMS, Population Health, Value-based Care, Compliance Management).

## Initial Boundary

Working hypothesis before research:

- Core use: a hospital/health system's quality department measuring care quality, managing quality/safety events, running improvement work, and satisfying external quality reporting/accreditation obligations.
- Likely users: quality directors/coordinators, patient safety officers, risk managers, accreditation coordinators, clinical analysts, medical staff office (peer review).
- Nearest neighbors: Infection Prevention Platform (IPC-specific), Life Sciences QMS (GxP product quality — different object world), Population Health Management (patient-population outcomes), Value-based Care Platform (quality→payment), Compliance Management (broader), Manufacturing QMS (same word, different industry).
- Unknowns: Is the US "quality measure reporting" pole (Medisolv-style) the same Type as the "quality/safety operations QMS" pole (symplr/Verge/MedQPro-style)? Or two Types sharing a name?

## Research Questions

1. What is the unit of record — a measure? an event? an audit? a case abstraction?
2. How do external frameworks (CMS, TJC, JCI, NABH, CBAHI, ONA, ISO) shape the system's structure?
3. What is the improvement loop: how does a finding (gap, event, audit result) become a verified action?
4. How do the two apparent poles (measure reporting vs safety-event QMS) relate — one Type or two?
5. What data flows in (EHR, claims, manual abstraction) and out (submissions, surveys, boards)?
6. What roles and permissions matter (peer review confidentiality, event reporter anonymity)?
7. Where is the boundary with Infection Prevention, Life Sciences QMS, and Population Health?

## Representative Products

Selected for market representation + documentation reach + different product philosophies + different geographies/customer tiers:

| Product | Pole | Geography/Tier |
|---|---|---|
| Medisolv (ENCOR + QualityIQ) | quality-measure reporting & analytics | US hospitals/health systems/ACOs |
| symplr Quality & Safety (Midas, symplr Safety, Quality Review) | quality/safety operations + provider performance | US enterprise health systems |
| Verge Health (Converge, now RLDatix) | healthcare GRC — safety+compliance+provider | US, 900+ facilities |
| MedQPro | accreditation-driven hospital QMS | India (JCI/NABH) |
| iCenna QM | HIS-embedded quality management | Saudi Arabia (CBAHI), regional |

## Sources

- Medisolv: https://medisolv.com/ , https://medisolv.com/solutions , https://medisolv.com/hospital-quality-reporting-package , https://analytics.medisolvcloud.com/ (fetched 2026-09-10)
- symplr: https://www.symplr.com/solutions/quality-safety-management (fetched 2026-09-10), https://www.symplr.com/products/quality-review (search excerpt)
- Verge Health: http://vergehealth.com/ , press releases and coverage (search excerpts, fetched 2026-09-10)
- MedQPro: https://medqpro.com/ (search excerpt, fetched 2026-09-10)
- iCenna: https://icenna.com/qm (search excerpt, fetched 2026-09-10)
- CMS QAPI RCA guidance (context for RCA/PIP practice): https://www.cms.gov/Medicare/Provider-Enrollment-and-Certification/QAPI/Downloads/GuidanceforRCA.pdf

Source-access limitation: deep help-center/user-guide articles were not reachable for most vendors; evidence rests on official product/solution pages plus vendor self-descriptions. Precise operational details (exact measure counts, submission deadlines, module lists) are not asserted in the final document.

## Product Observations

### Medisolv (ENCOR / QualityIQ) — evidence layer A (official product pages)

- Self-description: "purpose-built platform for quality measurement and analytics"; "manage and submit all hospital measures across CMS and TJC programs."
- Unit of record is the **quality measure** and the **case being abstracted** against a measure: eCQMs (electronic clinical quality measures), abstracted measures (manual chart abstraction with "timely caseloads with pre-populated EHR data", "software that guides you through the measure algorithm and uses skip logic", "real-time displays of pass/fail status as your case is abstracted"), hybrid measures, PRO-PMs (patient-reported outcome performance measures).
- Submission machinery: "use one vendor to submit to multiple reporting entities including CMS, TJC, states and other payers like ACOs." Program packages: Hospital Quality Reporting, MIPS, MVPs, ACO APP.
- Benchmarking: "track your performance against all Medisolv clients nationwide", quarterly eCQM benchmarks, user-defined peer groups, quartile charts.
- Improvement side: QualityIQ analytics ("trends, gaps, and goals in near-real time"), Star Rating Analyzer, advisory/AQI services — improvement is analytics + consulting, not a structured CAPA workflow in the observed material.
- External frame is explicit and load-bearing: CMS, TJC, MIPS, state programs; "58% of quality leaders rank increasing regulatory requirements as the number one thing keeping them up at night" (vendor survey).

### symplr Quality & Safety (Midas, symplr Safety, Quality Review) — evidence layer A

- Self-description: "Simplify workflows for quality and safety event investigation, OPPE, FPPE, quality improvement monitoring and provider privileging."
- Event capture: "Easily document patient or non-patient-related occurrences such as safety events, medication errors, falls, equipment concerns, and near misses with customizable forms. Attribute events to individual physicians, employees, and hospital departments."
- Resolution workflows: "Automate complex quality resolution workflows… analyze undesirable outcomes during treatment, and assess results after intervention"; automated peer review workflows; OPPE/FPPE (ongoing/focused professional practice evaluation).
- Measurement: "Monitor, track, and trend performance measurements and indicators for providers or departments. Quickly identify outliers for further review and corrective action." Data integrated "from EHR, discharges, lab, surgery, Rx, claims, appeals, and privileging."
- External frame: "CMS accreditation measurements", "CMS Core Measure Indicators, OPPE, The Joint Commission Core Competencies"; TJC-driven peer-review cadence cited in marketing.
- symplr Safety: "digital event management system… capture incidents, provide analytics, manage workflows, and monitor safety improvements."

### Verge Health (Converge) — evidence layer A (site + press)

- Self-description: "Governance, Risk, and Compliance platform purpose-built for healthcare (GRC-H)"; "One Platform for Zero Harm."
- Module families: Patient & Employee Safety (Event Management, Patient Relations, Liability Claims, Peer Review MD/RN, Workers Comp), Organizational Compliance (Accreditation & Regulatory, Contract Compliance), Provider Management (credentialing, privileging, performance monitoring), plus Rounding, Mortality Review, Action Plans, BI & Analytics.
- Improvement loop: Action Plans as first-class module; "connecting risk, quality and safety issues"; rounding as proactive data collection ("250,000 audits of the process and environment of care annually" at a client).
- External frame: accreditation & regulatory compliance explicit; CIHQ partnership content; high-reliability-organization framing.

### MedQPro — evidence layer A (vendor site)

- Self-description: "India's first JCI and NABH Compliant healthcare QMS Software Solution… digitize your accreditation process"; "45 modules."
- Modules observed: Quality Assurance Audit Management, Quality Indicator Management, Medical Record Compliance Management, Incident Reporting Management, Mock Drill Management, Documentation Management, Safety and Risk Management ("risk identification → assessment/evaluation → mitigation and monitoring → incidents → follow-up").
- External frame is the product's spine: accreditation (JCI/NABH) readiness; quality champions; mock drills as accreditation-evidence events.

### iCenna QM — evidence layer A (vendor site)

- Self-description: "policies, risks, audits, incidents, CAPA, KPIs, and accreditation evidence in one place"; CBAHI-aligned, HIMSS-ready, ISO 9001-compatible.
- Modules: Policies & SOPs Library, Incident & Event Reporting, Risk Register, Audits & Rounds, CAPA & Change Control, Training & Competency, KPIs/PREMs/Dashboards, Documented Evidence for Accreditation.
- PDCA cycle embedded as the improvement frame; "Export auditor-ready packs aligned with CBAHI/HIMSS/ISO 9001"; integrated with the vendor's own HIS/ERP.

## Cross-product Comparison

| Structure | Medisolv | symplr | Verge | MedQPro | iCenna | Layer |
|---|---|---|---|---|---|---|
| Defined quality measures/indicators tracked over time | ✓ (core) | ✓ | ✓ | ✓ | ✓ | B |
| External standards/accountability frame (regulator/accreditor/payer) | ✓ CMS/TJC/payers | ✓ CMS/TJC | ✓ accreditation/regulatory | ✓ JCI/NABH | ✓ CBAHI/ISO | B |
| Improvement loop: finding → action → effectiveness check | ✓ (analytics+advisory; loop present but lighter) | ✓ (workflows, corrective action) | ✓ (Action Plans) | ✓ | ✓ (CAPA, PDCA) | B |
| Adverse/safety event reporting & investigation | ✗ | ✓ | ✓ | ✓ | ✓ | B (pole-specific) |
| Audit / rounding / survey checklists | ✗ | partial | ✓ | ✓ | ✓ | B (pole-specific) |
| Document/policy control | ✗ | ✗ | partial | ✓ | ✓ | B (pole-specific) |
| Case-level measure abstraction & submission | ✓ (core) | partial (core measures via analytics) | ✗ | ✗ | ✗ | A (pole-specific) |
| Benchmarking vs peers | ✓ | ✓ | ✓ | ✗ | ✗ | B |
| Provider-level performance (peer review, OPPE/FPPE, privileging links) | partial (MIPS clinician) | ✓ | ✓ | ✗ | ✗ | B (US-shaped) |
| RCA / CAPA structured workflow | ✗ | ✓ | ✓ | ✓ | ✓ | B |
| Accreditation evidence packs / survey readiness | partial | partial | ✓ | ✓ (core) | ✓ (core) | B |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The quality measure/indicator of record** — a defined measure over the organization's care (process, outcome, or structure indicator), held persistently, tracked over time against targets/benchmarks. Remove → generic BI dashboard or KPI tracker.
2. **The external standards/accountability frame** — the measure set and quality processes are anchored to external bodies (regulators, accreditors, payers, standards programs) whose requirements define what "good quality" means and what must be reported/proven. Remove → internal-preference KPI tracking, not healthcare quality management.
3. **The improvement loop from finding to verified action** — findings (measure gaps, events, audit/rounding results, survey findings) drive corrective/improvement actions whose effectiveness is re-measured against the same measures. Remove → a reporting dashboard or an issue tracker with no quality feedback loop.

Jointly-held load-bearing: 1 alone = KPI dashboard; 2 without 1 = compliance checklist; 3 without 1+2 = generic issue/CAPA tracker; 1+2 without 3 = reporting shop with no improvement; 1+3 without 2 = generic quality analytics; 2+3 without 1 = accreditation paperwork with no measurement.

### L1 — Common Mature Structure

- Adverse/safety event reporting with customizable forms, attribution (department/provider), and investigation workflow
- RCA / CAPA management with root-cause analysis and effectiveness verification
- Audit / rounding programs (process and environment-of-care audits, mock drills)
- Benchmarking against peer groups / national comparators
- Dashboards and leadership reporting (trends, gaps, goals)
- Document/policy control in operations-pole products
- Integration with clinical data sources (EHR, ADT, lab, claims) to populate measures

### L2 — Variant / Optional

- **Pole packaging** (variant, not identity): measure-reporting/analytics pole (Medisolv) vs safety-event QMS pole (MedQPro/iCenna) vs GRC platform pole (Verge/symplr). Products bundle subsets; the L0 core holds across all.
- Regional accreditation frameworks (CMS/TJC US; JCI/NABH India; CBAHI Saudi; ONA/ANVISA Brazil; ISO international)
- Provider-level quality machinery (peer review, OPPE/FPPE, privileging linkage) — US-shaped, medical-staff-centric
- Submission tooling to specific programs (CMS eCQM submission, MIPS, state registries)
- Deployment: standalone vs embedded in a vendor's HIS/ERP suite (iCenna) vs enterprise operations platform module (symplr)

### L3 — Vendor-specific (Research Notes only)

- Medisolv ENCOR, QualityIQ, Quality365, Star Rating Analyzer, Equitable Care Module, abstraction skip-logic UX
- symplr Midas family names (DataVision, Statit), Quality Issue Manager (managed-care grievance tracking)
- Verge Converge module names, GRC-H Maturity Model, "Zero Harm" framing
- MedQPro "45 modules", mock-drill module
- iCenna PDCA embedding, integration hub

## Historical / Market-Sample Check

Would older/regional products fit the L0? Yes: the paper-era hospital quality department tracked defined indicators (e.g., infection rates, readmissions) on worksheets against Joint Commission/CMS requirements and ran corrective-action minutes — measure + external frame + improvement loop, no software. Regional products (MedQPro, iCenna, Qualiex-Brazil) satisfy the core under non-US frameworks, confirming the external frame is framework-agnostic. The US measure-submission machinery (eCQM, MIPS) is era/region-specific → L2, not L0. Check passed.

## Vendor-specific Findings

See L3 above. Also: Medisolv's improvement side is analytics+consulting rather than structured CAPA workflow — a philosophy difference within the Type, not a different Type.

## Boundary Findings

- **vs Infection Prevention Platform**: IPC is a single surveillance domain (infections, device-associated events, outbreak detection) with its own clinical data model; quality management is the organization-wide umbrella that may consume IPC indicators as measures. Remove the infection-specific surveillance object world → it becomes quality management; keep it → it is IPC.
- **vs Life Sciences QMS / CAPA Management**: same vocabulary (CAPA, audits, nonconformance) but the object world is products/batches/devices under GxP/ISO 13485, not care delivery under accreditation programs. Different Type.
- **vs Population Health Management**: PHM measures and intervenes on patient populations for clinical outcomes; quality management measures and improves the organization's care processes against external standards. Overlap on measures; different center of gravity.
- **vs Value-based Care Platform**: VBC is the payer-contract/money side (quality data feeding reimbursement); quality management is the operational measurement-and-improvement system. Medisolv straddles by selling reporting into VBC programs — packaging seam.
- **vs Compliance Management / GRC**: Verge explicitly brands itself healthcare GRC; the difference is emphasis — quality management centers on care-quality measures and improvement; enterprise compliance centers on the broader regulatory obligation estate. Convergent market; boundary recorded as a seam.
- **Decisive "remove" test**: remove the external accreditation/regulatory frame → generic quality analytics; remove the care-quality object world (measures over care) → generic GRC/compliance; remove the improvement loop → reporting dashboard.

## Uncertainties

- Exact workflow details inside event investigation and CAPA (state machines, escalation rules) not verified from help centers — kept generic in final doc.
- Whether the measure-reporting pole and operations pole are converging into one product category (symplr's "Quality Suite" suggests bundling) — recorded as a seam, not resolved.
- Degree to which quality management platforms own measure definitions vs consuming them from measure authors (CMS/NQF) — Medisolv clearly consumes external specifications; assumed common but not verified across all.

## Final Synthesis

Healthcare Quality Management is the healthcare organization's quality function's system of record: it holds the organization's defined quality measures over care, anchors them to external standards bodies whose requirements define and demand them, and runs the loop by which findings become verified improvement. Products range from measure-reporting engines to safety-event QMS to healthcare GRC platforms; the invariant core is measure + external frame + improvement loop.
