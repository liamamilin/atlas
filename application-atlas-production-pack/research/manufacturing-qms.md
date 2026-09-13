# Research Notes — Manufacturing QMS

## Research Goal

Understand what a Manufacturing QMS (quality management system software for manufacturers; market name "eQMS"/"EQMS") actually is as an Application Type: what records it holds, what machinery moves them, what compliance regime anchors it, how it relates to production systems (ERP/MES/PLM), and where its boundaries sit against the processed siblings (Life Sciences QMS, CAPA Management, MES, Inspection & Metrology, Calibration Management, Construction Quality Management) and the unprocessed neighbors (SPC, Supplier Quality Management, Manufacturing Traceability).

## Initial Boundary (working hypothesis, pre-research)

- Hypothesis: the quality function's system of record in manufacturing organizations — quality events arising in production (nonconformances, defects, holds), quality actions (CAPA, change), supplier quality, controlled documents — anchored in the quality-management-standards regime (ISO 9001 family, IATF 16949, AS9100, ISO 13485) rather than GxP drug regulation.
- Expected sharpest seams: vs Life Sciences QMS (same market name "eQMS", different center), vs CAPA Management (one record class vs the suite), vs MES (in-line quality execution vs quality system of record), vs SPC / Inspection & Metrology (execution vs record).
- Known prior evidence: the life-sciences-qms pass left a forward flag — "production-floor quality center (SPC/inspection/line NCR) vs regulated quality-system records center (events/CAPA/change/audits as compliance evidence)"; enterprise vendors sell manufacturing suites (eDHR/MES/EBR) beside the QMS and serve food & beverage/discrete manufacturing with the same QMS machinery.

## Research Questions

1. What record classes does a manufacturing QMS hold? Which are co-equal, which modular?
2. What is the characteristic manufacturing event class, and what is its lifecycle (nonconforming product control/disposition)?
3. What lifecycle machinery governs records (states, approvals, verification, closure)?
4. What is the compliance anchor — which regimes, which audits?
5. How do records bind to production context (parts, lots, work orders) and to ERP/MES/PLM?
6. Where do inspection execution and SPC sit — inside the QMS, beside it, or in a sibling product?
7. How does supplier quality work (SCAR, scorecards, PPAP, portals)?
8. What varies by industry (automotive core tools, medical device, food, pharma)?
9. What is packaging vs structure (module counts, no-code designers, AI, portals)?
10. Where are the boundaries: Life Sciences QMS, CAPA Management, MES, SPC, Inspection & Metrology, Supplier Quality Management, Manufacturing Traceability, Construction Quality Management, GRC, Document Management, EHS?

## Representative Products

| Product | Pole | Tier | Why sampled |
|---|---|---|---|
| Octave Reliance (formerly ETQ Reliance) | enterprise multi-industry eQMS suite (40+ applications) | enterprise, global multi-site | market-leading manufacturing-centered eQMS; automotive/electronics/HVAC/food customers |
| QT9 QMS | SMB/mid-market regulated-manufacturing QMS, natively unified with QT9 ERP | SMB/mid | different philosophy: all-modules-included, QMS+ERP one platform, pre-validated |
| Intellect | mid-market QMS + frontline operations platform | mid | different philosophy: quality records + connected frontline execution in one platform; no-code |
| ComplianceQuest (QualityQuest) | Salesforce-platform-native PLM+QMS+EHS+SRM+EBR suite | mid/enterprise | platform-native pole; medical device + pharma + automotive + packaging customers |
| Siemens (Teamcenter Quality + Opcenter X Quality) | PLM/MOM-embedded closed-loop quality (witness) | enterprise | quality-execution pole: inspection planning, SPC, APQP/FMEA/PPAP inside the PLM/MOM portfolio — boundary witness vs SPC/inspection execution and MES |

Rejected/abandoned samples: AssurX (HTTP 403, bot protection), Arena QMS (transport errors ×3, abandoned per network rules). Both would have added the discrete/electronics PLM-adjacent pole; the pole is partially covered by ComplianceQuest (PLM+QMS) and Siemens Teamcenter Quality.

## Sources

All fetched 2026-09-09 unless noted. Evidence layer A (direct, official) unless marked.

- Octave — Reliance overview: https://www.etq.com/reliance/ (redirects to Octave product page); Reliance Nonconformance Management: https://www.octave.com/products/asset-performance-management/reliance/non-conformance-management
- QT9 — root: https://www.qt9software.com/ ; QMS product page: https://qt9software.com/qms ; modules: https://qt9software.com/qms/modules ; nonconforming product module: https://qt9software.com/qms/nonconforming-product-software
- Intellect — root/platform: https://www.intellect.com/ (QMS modules: Audits, CAPA & NCRs, Document Control, Employee Training)
- ComplianceQuest — root: https://www.compliancequest.com/
- Siemens — Opcenter MOM: https://plm.sw.siemens.com/en-US/opcenter/ ; QMS solutions page (Teamcenter Quality + Opcenter X Quality): https://plm.sw.siemens.com/en-US/opcenter/quality-management-system-qms-capabilities/ (canonical: siemens.com/en-us/solutions/quality-management-qms/)
- Sibling research passes (internal): research/manufacturing-execution-system-mes.md, research/capa-management.md, research/life-sciences-qms.md, research/inspection-metrology-software.md, research/calibration-management.md, research/construction-quality-management.md

Sourcing limitations: no Tier-1 help-center articles were fetched for any sampled product (vendor help centers either unreachable or not attempted within budget); all observations are from official product/marketing pages and FAQs. Consequently no exact workflow state names, numeric limits, or default values are asserted anywhere. AssurX and Arena unreachable (see above).

## Product Observations

### Octave Reliance (formerly ETQ Reliance) — enterprise multi-industry eQMS — Evidence Layer A

- Self-label: "flexible, configurable quality management system built to scale"; FAQ names the category "Electronic Quality Management System (eQMS)".
- 40+ ready-to-use applications on one platform: Document Control, CAPA/Corrective Action, Audit Management, Training, Supplier Quality, **Nonconformance Management**, Supply Chain Quality Management, Change Management, Risk Register, New Product Introduction, Life Sciences Compliance, Lab Investigation (OOS), Health & Safety, Environmental Management, Advanced Analytics. "Quality Events" bundle = document control + CAPA + audit management + training, described as "the essential applications that form the foundation of effective quality management at any scale".
- Codeless application designer: drag-and-drop workflow/form/rule configuration without code; Script for advanced needs.
- Compliance framing: "ISO 9001, FDA 21 CFR Part 11, IATF 16949 and more"; Part 11/Annex 11 e-signatures; audit trails; validation support for life-sciences customers.
- Integration: ERP, PLM, CRM, MES, LIMS, HR via prebuilt connectors + REST APIs; "pull product data from your ERP… automatically trigger quality events based on manufacturing data".
- Mobile app with offline capture ("conduct audits from the factory floor. Capture nonconformances in real time").
- Multi-site/multi-language/role-based access; Reliance Go self-service packaging for smaller teams.
- Customers: Trane Technologies (HVAC), Celestica (electronics), Rheem, Kimberly-Clark, Owen Mumford, Lumileds, Manitoba Harvest. Case-study stat: "50% reduction in CAPA and SCAR resolution time" — SCAR (supplier corrective action request) named in a manufacturing customer context.
- Positioning: "Serving global manufacturers with hundreds of sites"; also mid-sized organizations.

### QT9 QMS — SMB/mid regulated manufacturing, QMS+ERP native — Evidence Layer A

- Self-label: "Quality Management Software Built for Regulated Manufacturers"; "all-in-one" QMS + ERP + BI on one platform, natively integrated ("developed together on a shared architecture… data flows seamlessly between systems in real time").
- 28+ modules, all included: Document Control, Audit Management, Risk Management, CAPA Management, **Nonconforming Products**, Quality Events Management, Supplier Evaluations, Supplier Surveys, Supplier Web Portal, Customer Feedback, Customer Surveys, Customer Web Portal, Employee Training, Preventive Maintenance, Change Control, Project Management, Safety Management, Management Review, Calibrations, Product Design Controls, Engineering Change Orders, Inspections, Deviation Management, FMEA, Audit Prep; plus EBR & DHR automation.
- Nonconforming Product module (Tier-1 detail): log NC → quarantine affected items ("stop bad parts fast… prevent nonconforming shipments") → approvals (approve/reject/verify) → optional root cause (5-Whys, Fishbone) → dispositions ("scrap, use as is, rework, etc.") → tasks → overdue alerts → credits (cost of poor quality) → supplier portal assignment → links to CAPA (bidirectional), deviations, customer feedback, inspections, risk. The module's own FAQ documents the ISO 9001 nonconforming-product process: identification → documentation → evaluation → segregation → investigation → disposition and approval → record keeping.
- Compliance list: ISO 9001, ISO 13485, ISO 14001, ISO 17025, AS9100, IATF 16949, HACCP, SQF, MoCRA, FDA 21 CFR Part 11 / 210 / 211 / 820 & QMSR, EU MDR, EU GMP, GxP.
- Pre-validated delivery (IQ/OQ/PQ executed by vendor); timeline-based traceability ("trace defective batches for targeted recalls"); e-signatures; audit trail.
- Portals: supplier, customer, employee (self-service access to documents/data).
- Deployment: cloud, on-premise, hybrid; US & EU hosting.
- Industries: medical devices, pharmaceuticals, aerospace, automotive, cannabis, chemicals, cosmetics, electronics, food & beverage, manufacturing, metals & mining, plastics.
- Customer quote: "We maintain an ISO9001:2015 certification, and this program will take the place of countless spreadsheets and emails."

### Intellect — QMS + frontline operations — Evidence Layer A

- Self-label: "AI QMS & Frontline Operations Platform for Manufacturing"; "One AI-powered platform for worker enablement and quality."
- QMS modules: Quality Management System, Audits, CAPA & NCRs, Document Control, Employee Training. Platform also: Frontline Operations (work instructions, inspections, task management, instant messaging, real-time expert/AI help), Asset & Data Management, Issue & Action Tracking, EHS, Skills & Training, Apps (no-code builder).
- Explicit market-structure statement: "Most manufacturers run quality management in one system and frontline execution in another. Intellect connects both, giving you visibility, compliance, and execution across every manufacturing site."
- CAPA & NCRs framing: "Every open nonconformance increases audit risk. Connect NCRs to CAPA resolution. Identify root causes faster, eliminate recurring nonconformances."
- Compliance: ISO, FDA, GMP, 21 CFR Part 11, OSHA, EPA, GxP; "closed-loop processes: SOPs, training, production events, and CAPA fully connected".
- No-code: "friendly enough to allow a non-IT person to build it the way we need it" (customer).
- Industries: discrete manufacturing (aerospace, automotive, cosmetics, electronics & semiconductors, plastics), process manufacturing (CPG, food & beverage), life sciences (biotech, labs, medical devices, nutraceuticals, pharma).
- Customers: Vornado, Cloyes (automotive), Asahi, Carlsberg, Fictiv, Microbac. Intellect IQ Platform (limited release Nov 2026) unifying QMS and frontline operations.

### ComplianceQuest (QualityQuest) — Salesforce-platform-native suite — Evidence Layer A

- Self-label: "AI-powered PLM, QMS, Supplier Management & EHS Platform" on Salesforce; "unifies quality processes in one AI-powered platform".
- Solutions: ProductQuest (PLM/design quality), QualityQuest (EQMS), BatchQuest (electronic batch records), PartnerQuest (SRM/SQM), SafetyQuest (EHS).
- Quality management scope: complaints management, quality management (NC/CAPA/audits/change), risk management, document & learning management, batch record management, supplier management, safety, environment.
- Manufacturing pole: BatchQuest — "Digitize batch records. Guide execution. Monitor in real time to deliver consistent batch quality" (EBR = MES-adjacent territory sold as a sibling product line).
- CQ.AI agents: NC Agent (5W2H structuring, duplicate detection, category recommendation), CAPA Agent (escalation of recurring NCs, root-cause assistance, effectiveness insights), Complaints Agent (triage, health-authority reporting determination), Audit Agent, Supplier Agent (recurring supplier issues → CAPA escalation).
- Customers: Dr. Reddy's (pharma), Stryker (medical device), Continental Contitech (automotive), Huhtamaki (packaging), YKK, Canon Medical, Flipkart. "Whether it is a small, medium or enterprise sized manufacturer."
- ERP/CRM integration (Salesforce-native).

### Siemens (Teamcenter Quality + Opcenter X Quality) — PLM/MOM-embedded closed-loop quality — Evidence Layer A (witness)

- Siemens' own QMS definition (FAQ): "QMS software is a digital solution that helps you to streamline quality management processes. It centralizes project planning, audits, supplier quality, issues and related problem solving, change management and reporting to ensure compliance, improve efficiency and drive continuous quality improvement."
- Core solution capabilities: Design for quality (FMEA, variation analysis, CAD/PMI reuse); Quality planning (APQP, control plans, quality project management); Quality control ("define, plan and perform inspections for incoming materials, parts, and finished products"; "SPC tools measure and control product and process quality"; "detect product and process deviations and create non-conformances"); Continuous improvement ("standardized problem-solving process (such as 8D, CAPA) by utilizing root cause analysis"; change requests); Supplier quality (PPAP, complaints, assessments, Supplier Quality Hub); Audit & compliance (certification, supplier, compliance, project, process audits; training/qualification).
- Two products: Teamcenter Quality (PLM-embedded, design-to-manufacturing closed loop, on-prem or cloud) and Opcenter X Quality (cloud QMS "for all quality-relevant processes on the shop floor, from production and inspection processes to corrective actions for deviations").
- "Closed-loop quality" framing: quality data from manufacturing feeds back to design; as-planned vs as-is comparison (Opcenter MOM page).
- Automotive core tools vocabulary throughout: APQP, FMEA, control plans, PPAP, SPC, 8D.
- Witness value: shows where the QMS meets quality execution (inspection planning/execution, SPC) — Siemens sells these as QMS *capabilities* inside the PLM/MOM portfolio, while the standalone eQMS vendors treat inspection/SPC as modules or integration points. Also shows the design-side extension (FMEA/design quality in PLM) that pure eQMS vendors cover with modules or leave to PLM.

## Cross-product Comparison

| Dimension | Octave Reliance | QT9 QMS | Intellect | ComplianceQuest | Siemens (witness) |
|---|---|---|---|---|---|
| Self-label | eQMS, 40+ applications | QMS for regulated manufacturers, 28+ modules | QMS + frontline operations platform | EQMS inside PLM/QMS/EHS/SRM suite | QMS inside PLM/MOM portfolio |
| Quality events (NC/deviation/complaint/audit finding) | ✓ (Nonconformance Mgmt; Lab Investigation OOS) | ✓ (Nonconforming Products, Deviation Mgmt, Quality Events, Customer Feedback) | ✓ (CAPA & NCRs) | ✓ (NC Agent, Complaints) | ✓ (nonconformances from deviations) |
| Nonconforming-product control (quarantine/disposition) | ✓ (NC application; disposition detail not on public page) | ✓✓ (quarantine, approve/reject/verify, scrap/use-as-is/rework) | partial (NCR capture; disposition detail not on public page) | ✓ (NC records; disposition detail not on public page) | ✓ (NC creation from deviations; inspection planning) |
| CAPA | ✓ | ✓ | ✓ | ✓ | ✓ (8D, CAPA) |
| Change control | ✓ (Change Management) | ✓ (Change Control, Engineering Change Orders) | (not on public QMS page) | ✓ | ✓ (change requests) |
| Audit management | ✓ | ✓ (+Audit Prep) | ✓ | ✓ | ✓ (certification/supplier/compliance/project/process) |
| Controlled documents | ✓ | ✓ | ✓ | ✓ | ✓ (centralized repository) |
| Training | ✓ | ✓ | ✓ | ✓ (learning mgmt) | ✓ (training/qualification) |
| Risk management | ✓ (Risk Register) | ✓ | (platform-level) | ✓ | ✓ (FMEA) |
| Supplier quality | ✓ (Supply Chain Quality Mgmt; SCAR in case study) | ✓ (Evaluations, Surveys, Web Portal) | partial (not on public QMS page) | ✓ (PartnerQuest SRM/SQM) | ✓ (PPAP, Supplier Quality Hub) |
| Inspection records | (via integrations) | ✓ (Inspections module) | ✓ (frontline inspections) | (via BatchQuest/quality) | ✓✓ (inspection planning + execution, incoming/in-process/finished) |
| SPC | (integration) | (not on module list) | (not on public page) | (not on public page) | ✓ (SPC tools in quality control) |
| FMEA / APQP / control plans / PPAP | (not on public page) | ✓ (FMEA module) | (not on public page) | (design quality in ProductQuest) | ✓✓ (APQP, FMEA, control plans, PPAP) |
| Closed-loop lifecycle (approval-gated workflow) | ✓ (workflow automation, e-signatures) | ✓ (approvals, e-signatures, audit trail) | ✓ (automated workflows) | ✓ (Salesforce workflow, e-signatures) | ✓ (closed-loop quality) |
| Compliance anchor named | ISO 9001, Part 11, IATF 16949, Annex 11 | ISO 9001/13485/14001/17025, AS9100, IATF 16949, HACCP, SQF, Part 11/210/211/820, EU MDR/GMP | ISO, FDA, GMP, Part 11 | (regulatory compliance framing; pharma/device customers) | standards, industry guidelines, customer qualifications, certification programs |
| Production-system integration | ERP/PLM/CRM/MES/LIMS/HR; event triggers from manufacturing data | native QT9 ERP; "links NCs, CAPAs, audits, training to ERP workflows" | frontline execution + quality in one platform | ERP/CRM (Salesforce) | PLM↔automation closed loop (Teamcenter + Opcenter) |
| EBR/DHR | (Life Sciences Compliance family) | ✓ (EBR & DHR module) | (not on public page) | ✓ (BatchQuest product line) | (MES families in Opcenter) |
| No-code configurability | ✓✓ (codeless designer) | (fixed best-practice modules) | ✓✓ (no-code builder) | ✓ (Salesforce platform) | (configuration, not no-code) |
| AI | ✓ (Insights, predictive) | (automation focus) | ✓ (AI platform, Search IQ) | ✓✓ (CQ.AI agents) | (not on public page) |
| Portals | (not on public page) | ✓ (supplier/customer/employee) | (frontline app) | (supplier collaboration) | (supplier collaboration) |
| Deployment | cloud SaaS (AWS) | cloud/on-prem/hybrid | cloud SaaS | Salesforce cloud | on-prem/cloud/SaaS |
| Scale/tier | enterprise global, mid-market via Go | SMB/mid | mid | SMB→enterprise | enterprise |

Evidence layers: all cells above are directly observed (A) on official pages; the row-level readings generalize across the sample (B). Rows with gaps are marked partial/not-on-public-page rather than inferred.

### Stable commonalities (cross-product, layer B)

1. **Quality record population**: events (nonconformances, deviations, complaints, audit findings) + actions (CAPA, change) + governance classes (documents, training, audits, risk, suppliers) — 5/5.
2. **Nonconformance as the characteristic event class** — 5/5; with quarantine/disposition machinery documented in Tier-1 detail at QT9 and present in NC framing at all others.
3. **Approval-gated closed-loop lifecycle with attribution** — 5/5 (workflow automation, e-signatures, audit trails, "closed-loop" language).
4. **Compliance anchor in quality-system regimes** — 5/5 (ISO 9001 universal; sector standards per industry; FDA where regulated).
5. **Production-system integration** — 5/5 in some form (native ERP at QT9; connector/API at Octave/CQ; platform-unified at Intellect; PLM/MOM-native at Siemens).
6. **Cross-record linkage** (NC↔CAPA↔change↔audit↔complaint↔supplier) — 5/5 in framing ("connect NCRs to CAPA resolution", "link modules", "connect quality events").
7. **Analytics/trending over the record population** — 5/5.

### Pole-specific differences

- Module-count packaging (40+ vs 28+ vs fewer) is vendor packaging, not structure.
- Floor machinery: Siemens embeds inspection planning/execution + SPC as QMS capabilities; QT9 ships an Inspections module; Octave/CQ integrate; Intellect unifies frontline execution. Depth varies; presence of *records* is universal, presence of *execution engines* is not.
- Design-side quality (FMEA/design controls): deep at Siemens (PLM) and CQ (ProductQuest); module at QT9; not prominent at Octave/Intellect public pages.
- EBR/DHR: product line at CQ, module at QT9, family at Octave — MES-adjacent territory bundled variably.
- Configurability philosophy: no-code (Octave, Intellect, CQ) vs pre-validated fixed best practice (QT9) — a real philosophical axis.
- AI: era-current everywhere it appears; depth varies.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

A Manufacturing QMS is the quality function's system of record in a manufacturing organization. Three structures, jointly held:

1. **The production-anchored quality record population of record.** Quality events arising from making and supplying product — nonconforming product/material (the characteristic class, with its control loop: identify → segregate/quarantine → evaluate → disposition [scrap / rework / use-as-is / return] → recorded approval), deviations, inspection failures, customer complaints, audit findings — and quality actions (investigations, corrective & preventive actions, change controls), held as individually identified, state-tracked, cross-linked records that reference the product context (parts, lots/batches, work orders, suppliers) drawn from the manufacturer's business systems. Remove → SPC/inspection execution tooling or a defect log; the system of record is gone.
2. **The closed-loop lifecycle machinery.** Every record moves through a governed workflow enforced by the system: capture → triage/classification/risk evaluation → investigation & root cause → disposition/action → recorded approval → implementation → verification (effectiveness for actions; implementation for changes) → closure, with routing, notifications/escalation, and attributed approvals. Closure is earned, not declared. Remove → a quality log/register with no process.
3. **The quality-system compliance anchor.** Records exist as controlled evidence that the organization's quality system meets its regime — standards certification (ISO 9001 family and sector standards such as IATF 16949, AS9100, ISO 13485), customer requirements, and applicable regulation — every change logged, every approval attributed and signed, records linked and retained, retrievable on demand for internal, customer, and registrar audits. This is why the machinery is this formal. Remove → a generic ticketing/issue tracker with quality vocabulary.

Jointly-held is load-bearing:

- 1 alone = defect/NC log plus inspection tooling
- 2 without 1 = generic workflow engine with nothing quality-shaped
- 3 without 1+2 = a compliance checklist/attestation tool
- 1+2 without 3 = ops issue tracking (CAPA-point tooling territory)
- 1+3 without 2 = a document store with no loop
- Remove the production anchor from 1 (events no longer bound to product/parts/lots/suppliers) → the generic regulated-records eQMS center (the Life Sciences QMS pole)

Positioning (vendor-consistent): the QMS sits beside the business/production systems — ERP owns orders/inventory, MES owns execution and the as-built record, PLM owns design — and exchanges context with them (product data in, quality events triggered by manufacturing data out). Siemens states the closed loop explicitly (quality data from manufacturing feeds design); QT9 states the ERP linkage explicitly; Octave states event-triggering from manufacturing data.

### L1 — Common Mature Structure (not definitional)

- Controlled document management (SOP/work-instruction lifecycle with version control and approval) — 5/5 but separable (modular in all; the life-sciences pass proved separability via packaging).
- Training management bound to documents — 5/5, separable (standalone sibling Type exists).
- Audit management as a record class (internal/supplier/customer/registrar audits → findings → actions) — 5/5.
- Risk management (risk registers, FMEA, risk-based evaluation inside events/changes) — 4/5 explicit.
- Supplier quality (qualification/evaluation, scorecards, SCARs, PPAP where automotive, supplier portals) — 4/5 explicit; standalone sibling leaf exists.
- Complaint handling as an event class feeding investigation — 4/5 explicit.
- Inspection records (incoming/in-process/final) as event sources — 4/5 explicit at record level.
- Change control / engineering change linkage — 4/5 explicit.
- Quality analytics: KPIs, trending, cost-of-quality, dashboards — 5/5.
- Compliance machinery: e-signatures/audit trails (Part 11/Annex 11 where regulated), validation posture, framework templates — 5/5.
- Cross-record linkage and traceability exports for audits/recalls — 5/5.
- Mobile/offline capture from the floor — 3/5 explicit.
- Portals (supplier/customer/employee) — 2/5 explicit.
- AI assistance (summaries, trend detection, agents) — era-current, 4/5.

### L2 — Variant / Optional Structure

- Industry/regime flavor: general manufacturing (ISO 9001), automotive (IATF 16949 + core tools APQP/PPAP/FMEA/8D), aerospace/defense (AS9100), medical device (ISO 13485 / FDA Part 820 / QMSR), pharma/GMP (Part 210/211, EU GMP), food & beverage (HACCP, SQF, FSSC-style), cosmetics (MoCRA), electronics, cannabis. The regime changes vocabulary and templates more than structure.
- Portfolio posture: standalone eQMS suite (Octave) vs QMS+ERP native (QT9) vs QMS+frontline operations (Intellect) vs platform-native suite (ComplianceQuest on Salesforce) vs PLM/MOM-embedded (Siemens Teamcenter Quality + Opcenter X Quality).
- Floor machinery depth: integration-mediated event triggers vs built-in inspection modules vs full inspection/SPC execution engines (Siemens pole; the SPC and Inspection & Metrology leaves' territory).
- Design-side depth: FMEA/design controls as modules vs PLM-native design quality.
- EBR/DHR bundling (regulated batch/device records) — MES-adjacent, bundled variably.
- Adjacent-class bundling: calibration management, preventive maintenance, safety/EHS, environmental management — bundled modules at several vendors, each with its own standalone Type.
- Scale packaging: enterprise multi-site vs SMB template-led/self-service (Reliance Go, QT9 pricing model).
- Configurability philosophy: no-code designers vs pre-validated fixed best practice.
- Deployment: cloud SaaS dominant; on-prem and hybrid persist (QT9 explicitly all three).

### L3 — Vendor-specific (Research Notes only)

- Octave: 40+ application packaging; "Quality Events" foundation bundle naming; Reliance Go self-service tier; codeless designer + Script; Hobart/LNS analyst framing; ETQ→Octave rebrand (Hexagon spin-off); case-study stats (650% ROI, 32% scrap/rework reduction, Rheem 50% CAPA/SCAR time).
- QT9: concurrent-license pricing model ("no per-user fees"); pre-validated IQ/OQ/PQ delivery; native QT9 ERP shared architecture; timeline traceability; 150MB/file storage limit; Q-Cast podcast; cost-of-poor-quality calculator.
- Intellect: Intellect IQ Platform (Nov 2026 limited release) unifying QMS + frontline operations; Zaptic CFW heritage (connected frontline worker); Search IQ / Data IQ; Gartner Software Advice "Best Ease of Use" award framing.
- ComplianceQuest: ProductQuest/QualityQuest/BatchQuest/PartnerQuest/SafetyQuest suite naming; CQ.AI agents on Salesforce Agentforce; 5W2H NC structuring; Frost & Sullivan/Gartner MQ positioning.
- Siemens: Teamcenter Quality vs Opcenter X Quality split (PLM-side vs shop-floor-side); variation analysis (Tecnomatix); Supplier Quality Hub; CIMdata report framing; Mach Medical case study.

## Vendor-specific Findings

See L3. Additionally: QT9 is the only sampled vendor with Tier-1 detail on the nonconforming-product control loop (quarantine, approve/reject/verify, disposition types, supplier-portal assignment); Siemens is the only sampled vendor whose QMS framing spans design (PLM) and shop floor (MOM) as one closed loop with inspection/SPC execution inside; Intellect is the only sampled vendor with an explicit statement about the market's own structure ("most manufacturers run quality management in one system and frontline execution in another"). All treated as product-level statements that triangulate seams, not Type properties.

## Boundary Findings

- **vs Life Sciences QMS (§22, processed 2026-09-08)** — the sharpest seam, jointly reviewed. Both Types share the same three-part core shape (record population + closed-loop lifecycle + compliance anchor). The differences are centers of gravity, not disjoint structure: Manufacturing QMS centers production-floor and product quality (nonconforming product with disposition, inspection failures, supplier lots, complaints about shipped product; records bound to parts/lots/work orders), with its regime center in the quality-management-standards certification world (ISO 9001 family, IATF, AS9100, customer/registrar audits); Life Sciences QMS centers the regulated quality-system records (deviations/OOS/change/audits as GxP-style regulatory evidence). The overlap zone is real and commercially important: QT9, Octave, and ComplianceQuest all serve medical device/pharma customers alongside general manufacturing, and the life-sciences pass found its vendors serving food & beverage and discrete manufacturers. Evidence that the seam is center-of-gravity rather than regime-exclusive: the same vendor (QT9) lists ISO 9001 and IATF 16949 and GMP on one compliance page. Removal tests: remove the production anchor → the life-sciences-style records center; remove the regime formality → generic quality tooling. Both leaves stand; taxonomy observation recorded in STATUS.md.
- **vs CAPA Management (§16, processed 2026-09-07)** — confirmed from this side: CAPA is one record class inside the QMS; all five sampled products embed CAPA among co-equal classes (NC, change, audits, documents, suppliers). Remove the record population → CAPA point tool. Consistent with the capa pass's own seam.
- **vs MES (§16, processed 2026-09-09)** — MES owns in-line quality execution (checks, SPC, holds) as part of executing released orders and producing the as-built record; the QMS owns the quality system of record (events, actions, dispositions, audits) and consumes execution-originated events. Octave: "automatically trigger quality events based on manufacturing data"; the MES pass: "in-line quality execution… feeding the quality system of record". Remove the quality-record center → MES retains quality execution only; remove order execution → QMS.
- **vs SPC (§16, unprocessed)** — SPC is statistical monitoring/control of process variation (Siemens: "SPC tools measure and control product and process quality" inside quality control). The QMS holds records about quality events; SPC engines hold control charts and process data. SPC data is an event source. Forward flag for the SPC pass.
- **vs Inspection & Metrology Software (§16, processed 2026-09-08)** — that Type is the part-grain geometric conformance loop (nominal reference + measured geometry + evaluation + part-level record). The QMS holds quality-system-grain records; inspection results enter as event sources. QT9's Inspections module ("capture inspection details online") is record-level, not metrology execution. Remove the record population → inspection/metrology.
- **vs Supplier Quality Management (§16, unprocessed)** — supplier quality (qualification, SCARs, scorecards, PPAP, supplier portals) is a standard record class/module inside the QMS (4/5 explicit). Standalone supplier-quality products exist — the leaf's territory. Forward flag.
- **vs Manufacturing Traceability (§16, unprocessed)** — traceability owns the lot/serial genealogy chain; the QMS links quality records to lots/parts but does not own genealogy. Consistent with the MES pass's seam.
- **vs Construction Quality Management (§17, processed 2026-09-07)** — different domain: construction conformance (specs/ITPs/punch lists, project-grain) vs manufacturing production quality (parts/lots, production-grain). Different event sources and objects; shared loop shape only.
- **vs GRC / Compliance Management (§11)** — obligations/policies/controls centered vs quality records centered. Qualio's straddle noted in the life-sciences pass; same reading here.
- **vs Document Management / Enterprise Records (§10)** — controlled documents are one separable record class; the QMS's center is the event/action loop.
- **vs EHS (§21)** — safety/environmental events vs quality events; several vendors bundle both (QT9 Safety Management, CQ SafetyQuest, Octave Health & Safety) — bundling, not identity.
- **vs Healthcare Quality Management (§22, unprocessed)** — healthcare-delivery quality (patient-safety events, accreditation) vs manufacturing production quality. Different domain, different users.
- **"Remove what → becomes the neighbor" tests:** remove the record population → SPC/inspection execution + CAPA point tool; remove the loop → quality log; remove the compliance anchor → generic ticketing; remove the production anchor → generic regulated eQMS (life-sciences pole); remove CAPA/change/audit classes keeping NC only → nonconformance point tooling.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit?

- **Paper-era manufacturing quality system:** NCR forms with disposition sign-offs (MRB — material review board), quarantine tags, CAPA logbooks, controlled document binders with revision registers, supplier scorecards and SCAR letters, audit files, inspection records — satisfies all three L0 legs with no software. The vocabulary (MRB, SCAR, 8D, NCR) predates the software category.
- **The automotive 8D discipline** (team → problem description → containment → root cause → corrective actions → prevention → closure) maps onto the closed loop without any modern feature; Siemens sells 8D as a QMS problem-solving process today.
- **Pre-cloud on-prem QMS products** (ETQ's own heritage; TrackWise heritage noted in the life-sciences pass) satisfy; cloud is a variant.
- **Regional products** (Japanese TQM tooling, European automotive QMS products, regional food-safety systems): same triple; regime flavor varies.
- Modern additions (cloud, no-code designers, AI agents, portals, pre-validated delivery, mobile capture) are era-current capabilities, not definitional.

Conclusion: the L0 passes the historical check; the definition does not depend on cloud, no-code, AI, e-signature machinery (held as the modern implementation of attributed recorded approvals), or any specific standard.

## Uncertainties

1. **No Tier-1 help-center evidence** for any sampled product: exact workflow stage names, default states, and numeric limits were not verified. The lifecycle description is conceptual (capture → … → closure) and matches vendor-described stages only at that grain. Final document deliberately avoids precise stage labels and numbers.
2. **AssurX and Arena unreachable** (403 / transport ×3). The discrete/electronics PLM-adjacent pole is covered indirectly (ComplianceQuest ProductQuest, Siemens Teamcenter Quality) but not by a dedicated eQMS vendor of that pole.
3. **Disposition machinery depth** is Tier-1-verified only at QT9; the other products' public pages confirm NC records but not disposition detail. The L0's disposition language is calibrated to "characteristic class with its control loop" rather than claiming uniform MRB machinery.
4. **SPC/inspection execution depth** inside QMS products varies and is under-documented on public pages (only Siemens documents SPC explicitly). The seam vs the SPC leaf is drawn structurally, not from exhaustive product evidence.
5. **Market-name noise:** "eQMS"/"EQMS" is used by both manufacturing and life-sciences vendors; "QMS software" is also used generically. The Type boundary must be structural (production anchor + regime center), not label-based.
6. **Intellect's supplier-quality depth** not verified (not on public QMS page); supplier quality held at 4/5.

## Final Synthesis

A Manufacturing QMS is the quality function's system of record in a manufacturing organization. Its defining core is exactly three jointly-held structures: (1) the production-anchored quality record population — quality events arising from making and supplying product (nonconforming product/material with its identify→quarantine→disposition→approve control loop as the characteristic class, plus deviations, inspection failures, complaints, audit findings) and quality actions (investigations, CAPA, change controls), held as identified, state-tracked, cross-linked records bound to product context (parts, lots, work orders, suppliers); (2) the closed-loop lifecycle machinery that moves every record from capture through investigation, recorded approval, implementation, and verification to earned closure; (3) the quality-system compliance anchor — records maintained as attributed, traceable, retained evidence that the quality system meets its regime (ISO 9001-family certification, sector standards, customer requirements, applicable regulation), inspection-ready for internal, customer, and registrar audits. Controlled documents, training, audits-as-class, risk, supplier quality, complaints, inspection records, analytics, compliance machinery, portals, mobile capture, and AI are the standard capability layer — common and nearly universal, but modular and separable. Industry regimes (automotive core tools, medical device, pharma, food), portfolio posture (standalone suite / QMS+ERP / QMS+frontline / platform-native / PLM-MOM-embedded), configurability philosophy, floor-machinery depth, and deployment are variants. The sharpest seams: with Life Sciences QMS (same core shape, different center of gravity — production-floor quality vs regulated quality records; overlap zone in regulated manufacturing), with CAPA Management (one record class standalone), with MES (in-line quality execution feeding the record system), and with SPC/Inspection & Metrology (execution engines vs system of record). The market label "eQMS" spans both QMS Types; the structural core above, not the label, is the Type.
