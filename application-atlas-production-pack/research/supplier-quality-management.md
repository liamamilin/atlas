# Research Notes — Supplier Quality Management

## Research Goal

Understand what "Supplier Quality Management" (SQM) software actually is as an Application Type: what objects exist inside it, who uses it, how supplier quality work flows, and where its boundaries sit against the already-processed neighbors (Manufacturing QMS, CAPA Management, Supplier Management Platform, Supplier Risk Management, Manufacturing Supplier Collaboration, Inspection & Metrology Software, SPC, Third-party Risk Management, Supplier Portal).

Pre-hung flags from prior passes that this pass must discharge:

- **manufacturing-supplier-collaboration (§16, 2026-09-09)**: "quality content (complaints/concessions/certificates) is connected-but-separate at the network pole (SupplyOn Quality Management family; e2open Risk & Quality app); the SQM pass should center the quality record/8D-class loop."
- **third-party-cyber-risk-platform (§15, 2026-09-09)**: flagged seam "quality record vs audits-as-mitigation" vs supplier-quality-management.
- **manufacturing-qms (§16, 2026-09-09)**: its Related-Types table already holds "Supplier Quality Management | component Type / module | supplier qualification, scorecards, SCARs, and PPAP as a standalone focus; inside the QMS it is one record class among several."

## Initial Boundary

Working hypothesis before research:

- Core purpose: the manufacturer's (buyer's) quality-side system over its supplier base — qualifying suppliers and their parts for quality, controlling the quality of incoming material, handling quality problems traced to suppliers, and evaluating supplier quality performance.
- Primary users: supplier quality engineers (SQEs), incoming-inspection staff, quality managers; suppliers as secondary participants.
- Nearest neighbors: Manufacturing QMS (internal quality), CAPA Management (the loop alone), Supplier Management Platform (commercial standing), Supplier Risk Management (risk lens), Manufacturing Supplier Collaboration (demand/fulfillment loop), Inspection & Metrology (geometric inspection execution).
- Unknowns: Is incoming inspection definitional? Is PPAP/FAI part qualification definitional or automotive/aerospace packaging? Is the supplier-facing response loop definitional? Is the scorecard definitional?

## Research Questions

1. What are the core objects: supplier quality record, part approval (PPAP/FAI/first-article), quality info record, complaint/SCAR/8D, deviation/concession, certificate, audit, scorecard?
2. How is incoming material quality controlled (receiving inspection, source inspection, skip-lot, usage decision)?
3. How does the supplier participate (portal, 8D response, certificate upload, scorecard visibility)?
4. What gates exist (approved-vendor list, part-level approval, release status, blocking)?
5. How do quality events and evidence feed supplier evaluation and sourcing/approval decisions?
6. What is the lifecycle of a supplier complaint/SCAR, and who does what at each step?
7. Which industry variants reshape the vocabulary (automotive PPAP/8D, aerospace FAI, life-sciences GMP supplier qualification)?
8. Where are the boundaries vs the nine neighbors listed above?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Customer tier |
|---|---|---|
| Octave Reliance Supply Chain Quality Management (formerly ETQ Reliance SCQM) | enterprise eQMS suite with a dedicated supplier-quality application set | enterprise multi-industry |
| SAP S/4HANA Quality Management (QM in Procurement) | ERP-embedded quality module | large enterprise |
| SupplyOn Quality Management | automotive supply-network collaboration platform | industry network (OEM ↔ tiered suppliers) |
| MasterControl Supplier (Supplier™ family) | regulated life-sciences eQMS supplier family | regulated enterprise |
| QT9 QMS supplier modules | SMB/mid-market QMS | SMB/mid-market |

## Sources

Fetched 2026-09-10:

- Octave — Reliance overview: https://www.etq.com/solutions/supplier-quality-management/ (redirects to Reliance overview); Reliance Supply Chain Quality Management product page: https://www.octave.com/products/asset-performance-management/reliance/supply-chain-quality-management
- SAP — official learning content (Tier 1): "Implementing Quality Control in Procurement" https://learning.sap.com/learning-journeys/configuring-sap-s-4hana-quality-management/implementing-quality-control-in-procurement ; "Using the Quality Info Record Procurement" https://learning.sap.com/courses/applying-sap-s-4hana-quality-management/using-the-quality-info-record-procurement_d53b2b7e-bd5b-43b0-8631-31d352ebe695 ; "Executing a Source Inspection" https://learning.sap.com/learning-journeys/applying-sap-s-4hana-quality-management/executing-a-source-inspection_f7b7e89d-b702-4e8c-a263-6acfcdfff40d ; "Performing Quality Inspection at Goods Receipt" https://learning.sap.com/learning-journeys/configuring-sap-s-4hana-quality-management/describing-quality-management-at-goods-receipt ; Quality Info Record OData API reference https://help.sap.com/docs/PRODUCT_ID/a08e12a754cf4891b41a01a285d065bb/472fa8f1fef64d47b07e2c96a2a57eb2.html
- SupplyOn — Quality Management solution page: https://www.supplyon.com/en/solutions/quality-management/ ; Complaint Management page: https://www.supplyon.com/en/solutions/quality-management/complaint-management/ ; automotive industry page: https://www.supplyon.com/en/industries/automotive_industry/ ; Problem Solver product page (SupplyOn Store): https://enable.supplyon.com/en/product/119 ; Problem Solver supplier onboarding guide: https://partners.supplyon.com/en/te/problem-solver ; ZF supplier-assessment case study: https://www.supplyon.com/en/customers/case-study-zf-supplier_assessment/ ; ZF supplier-board Problem Solver page: https://www.zf.com/site/supplierboard/en/ebusiness/digital_communication_types/problem_solver/problem_solver.html ; INNIO rollout notice (customer-published): https://supplier.innio.com/en/news-media/news/supplyon-quality-modules/
- MasterControl — Supplier Management: https://www.mastercontrol.com/supplier/supplier-management/ ; Supplier Quality Management Software for Life Sciences: https://www.mastercontrol.com/supplier/qms-software/ ; Supplier Audit: https://www.mastercontrol.com/supplier/supplier-audit-software/ ; Supplier Performance: https://www.mastercontrol.com/supplier/performance-software/ ; Supplier CAPA: https://www.mastercontrol.com/supplier/capa-corrective-action/ ; MasterControl Supplier Overview (help center): https://currentcloud.onlinehelp.mastercontrol.com/2024.1/en_us/Content/Supplier/MasterControl_Supplier_Overview.htm
- QT9 — QMS modules: https://qt9software.com/qms/modules ; Supplier Evaluations: https://qt9software.com/qms/supplier-evaluation-software ; Supplier Web Portal: https://qt9software.com/qms/supplier-web-portal-software ; Inspections: https://qt9software.com/qms/inspection-software

Failed fetches (1–2 attempts each, then abandoned per network rule):

- https://qt9software.com/qms/supplier-management-software → 404 (recovered via /qms/modules)
- https://www.mastercontrol.com/quality/supplier-quality-management-software/ → 404 (recovered via /supplier/* pages)

## Product Observations

### Octave Reliance Supply Chain Quality Management (formerly ETQ Reliance SCQM) — Evidence A

Official product page (octave.com). The vendor's own decomposition of the Type into **four integrated applications**:

1. **Production Part Approval Process (PPAP)** — "Evaluate components and subsystems from suppliers, establish clear design specifications for supply chain partners and monitor supplier compliance. Manage product and process change requests, submissions, approvals and waivers to build supplier confidence."
2. **Receiving and Inspection** — "Gain better control over supplier inputs by incorporating the process of receiving supplier components into your organization's internal processes. Set up inspection schedules and create sampling plans and skip lot profiles based on supplier performance."
3. **Supplier Corrective Action Request (SCAR)** — "Identify, fix and record quality issues traced back to suppliers using the same corrective action procedures used internally. Track investigation and resolution, assess nonconformance risk and monitor deviations from standard processes."
4. **Supplier Rating** — "Build comprehensive supplier scorecards based on quantitative and qualitative information on up to five dimensions of performance. Automatically update critical metrics, generate supplier reports and make informed future sourcing decisions."

Vendor FAQ definitions (same page):

- "Supply chain quality management is the act of upholding supplier quality. That means ensuring raw materials, components or subassemblies deliver at a level of quality that supports safe and effective performance in the finished product."
- SCAR: "a report that details a blemish, defect or nonconformance in delivered parts or raw materials from a supplier. This request also includes a step-by-step process for the supplier to remediate these blemishes in future deliveries." — supplier-facing remediation process, explicitly.
- PPAP: "PPAP software enables you to store, access and analyze documentation from the vendor and then set up an inspection schedule to ensure that the new parts are of the promised quality."
- Measurement: "Quality can be measured when shipments from suppliers pass inspection and sampling, when they arrive on time and when they're correctly labeled and packaged…"
- Improvement: "You can also perform PPAP audits to weed out suppliers who can't meet your criteria."
- Integration: "Integrate seamlessly with SAP, Oracle and other third-party systems to track supplier material and chemical information, collect supplier ratings…"
- Positioning: "Ensure finished product quality with automated control and visibility over all elements of your supply chain, from local manufacturers to global suppliers." "Include suppliers directly in product lifecycle."
- Customer quote (Cree): "One of the key requirements when we bought Reliance was that we could use it for supplier management. Our supplier quality engineering group is extremely happy with Reliance."
- Stat block: "50% reduction in CAPA and SCAR resolution time (Rheem)" — SCAR as a first-class record class.

Observations: the vendor's own four-app set maps exactly onto the hypothesized core — part qualification (PPAP), incoming control (receiving inspection), issue loop (SCAR), evaluation (rating). SCAR explicitly reuses internal corrective-action procedures pointed at a supplier, with a supplier-executed remediation process.

### SAP S/4HANA Quality Management — QM in Procurement — Evidence A (Tier 1: official learning/help content)

From "Implementing Quality Control in Procurement":

- "If your company purchases materials from external vendors, you can implement QM in Procurement to support your procurement processes for quality assurance purposes. You can implement QM in Procurement as 'stand-alone' or together with quality inspections. As a 'stand-alone' component, you can use all procurement functions except those for processing goods receipt inspections." — **incoming inspection is optional even inside the ERP pole**; the standing/control layer exists without it.
- **Quality Info Record for Procurement**: "defines details how you procure a material from a vendor. It is uniquely determined by the plant, vendor, and material." Controls:
  - **Release**: "The quality info record is released so that the material can be purchased from the vendor. It is also possible to restrict the release to a certain period of time or a certain quantity." (e.g., only 100 PC until end of year; the system forbids a PO exceeding it.)
  - **User status profile with release stages**: "to model a purchasing process with release stages (for example, first-article, preliminary series, regular procurement). Each stage can be assigned to an inspection type… so that you can perform different quality inspections depending on the current stage of your supply relationship. For example, during first-article inspection of a material, the Quality Technician performs a more detailed goods receipt inspection than for a material that you procure regularly."
  - **Blocking function**: "The selected function, for example, the creation of a purchase order or quotation, is blocked for quality reasons."
  - **Inspection control**: source inspection vs GR inspection setup.
  - **Quality assurance agreements**: "link documents (quality agreements) to this info record… you document that the supplier implements a quality system and is successfully audited so that you can skip goods receipt inspections in the future."
  - **Certified QM system skip**: "Goods receipt inspections can be skipped for certified suppliers… If there is a fit and the implemented QM system is marked as Certified QM System, the system does not create an inspection lot when goods are procured from this supplier and directly posts the goods to unrestricted-use stock."
- **Goods receipt inspection**: "The system can automatically create an inspection lot when a goods receipt for a purchase order is posted… it is stock-relevant and a transfer posting can be made for the stock exclusively using the inspection lot." Process: purchaser creates PO → warehouse posts GR → quality technician records inspection results and/or defects → "The Quality Engineer posts the usage decision."
- **Source inspection**: "the quality inspection must already be done at the supplier's premises before the goods transport to your warehouse… the system… subtracts an inspection lead time from the expected delivery date… Set the indicator *Source inspection instead of GR inspection* in the quality info record (procurement)."
- Roles named: Quality Planner (maintains info records), Quality Technician (records results/defects), Quality Engineer (usage decision), Purchaser, Warehouse Clerk.
- API reference confirms first-article machinery: "Maintain First Article Inspection", fields "ProductionPieceApprovalIsRequired", "ProductionPieceApprovalLevel".

Observations: the ERP pole realizes the supplier-part quality standing as a first-class object (quality info record: release + blocking + validity + stage model + inspection control + QA agreements + certification skip). The stage model (first-article → preliminary series → regular procurement) is a part-qualification lifecycle embedded in procurement. Incoming inspection is stock-gating (usage decision controls stock posting) — the strongest form of "quality standing gates use".

### SupplyOn Quality Management — Evidence A (official solution pages + partner onboarding center + customer-published pages)

From the Quality Management solution page:

- Positioning: "Quality Management that moves supplier quality upstream… Identify supplier risks earlier, resolve quality issues faster, and continuously improve supplier performance with connected quality processes and structured supplier collaboration."
- Module inventory: "Structure supplier readiness — Connect feasibility studies, technical reviews, APQP, PPAP, and virtual inspections in a structured readiness process." / "Resolve issues and track actions — Standardize complaints, 8D or 8S workflows, containment, root-cause analysis, corrective actions, and deadline control across plants and suppliers. → Complaint Management (8D | 8S), → Inspection | Audit Management" / "Manage changes and trace quality — Manage supplier-initiated changes and link quality issues to the relevant part, batch, serial context, site, supplier path, and process step. → Supplier Initiated CR (PCN | ECN), → Traceability (Parts | Quality)" / "Monitor and compare supplier performance."
- Complaint Management page: "Supplier Complaint Management is a structured workflow for managing supplier quality issues from complaint creation through containment, root-cause analysis, corrective actions, effectiveness checks, and closure… instead of fragmented email- and spreadsheet-based complaint handling."
  - "Structured complaint creation with part data, error description, and attachments"
  - "Complaint handling based on standardized problem-solving methods (8D | 9S)"
  - "Defined milestones and response times for supplier feedback and final report submission"
  - "Structured supplier response, task overview and complaint-specific action visibility through the full complaint workflow"
  - "Documentation of root-cause, corrective actions as well as corrected-part handling"
  - "Use of methods such as 5 Why and Ishikawa / Fishbone"
  - Containment: "documentation of effective containment actions and the clean date for corrected parts"
  - Deadlines: "planned response dates for each step, alerts for deadline monitoring… especially important where customer-specific maximum reaction times apply and overdue supplier responses must be escalated quickly"
  - "Give internal teams and suppliers one shared view of complaint status, deadlines, tasks, and process history."
  - "No internal process change necessary - you continue working with your internal system via backend integration" (Store page) — complaints can be pushed from the buyer's internal QM system.
- Problem Solver supplier onboarding guide (supplier-side view, Tier 1 for the two-sided structure):
  - Task overview: "Task type… Task name… Task status: Closed, waiting, Open… Due date… Responsible."
  - Complaint details: "complaint date and appearance dates, part information and quantities… attach files to clarify the problem."
  - "All 8D steps can be implemented here. It consists of 10 sub-sections… D1 | Team… D2 | Problem Description… D3 | (Interim) Containment Actions… D4 | Root Cause Analysis and Escape Points… D5 | Permanent Corrective Actions… D6 | Implement Corrective Actions… D7 | Prevention of Reoccurrence… D8 | Closure and Report Evaluation. The 8D report rating shows the quality of the content of an 8D report."
  - "Supplier-Internal Data is only visible to the supplier" — asymmetric visibility inside one shared record.
  - "Status and timeline Tab displays the current status and timeline of each 8D-step… maintenance… if the complaint is active (not closed, cancelled, or waiting for review)."
- ZF supplier-board page (customer-published): "The ZF Group solution for this activity is the SupplyOn Problem Solver module (sometimes referred to as e-8D)… The 8D method is a standardized problem solution process… supports methods such as 5-Why, Ishikawa and Drill-deep-and-wide."
- ZF supplier-assessment case study (Performance Monitor): "ZF uses as its measurable key figure for quality the PPM (parts per million) value, which is calculated on the basis of the number of faulty components delivered in relation to the overall number of components delivered… The assessment data from incoming goods at ZF locations is entered into the central SAP Business Warehouse and automatically transferred to SupplyOn and made available to the suppliers… updated on a monthly basis… traffic light function on every data plane… historical comparison… suppliers… self-administration of access rights to the assessment data."
- INNIO rollout notice (customer-published): SupplyOn quality modules = "Supplier deviation requests – Technical Review / Non-conformance management including 8D report – Problem Solver / Parts qualification process – Project Management / Audits – Audit Management."
- Automotive industry page: "Structured collaboration in supplier quality – APQP, supplier evaluation, complaint management, and standardized 8D-based problem solving – speeds up issue closure and long-term improvement."

Observations: the network pole centers the two-sided quality issue loop (8D executed by the supplier inside the buyer's record, with asymmetric visibility, deadlines, escalation) plus part qualification (APQP/PPAP readiness), deviation requests, audits, traceability linkage (part/batch/serial), and supplier performance monitoring (PPM from incoming-goods data, supplier-visible). Quality is a separate solution family from SupplyOn's supply-chain collaboration (consistent with the manufacturing-supplier-collaboration pass's finding).

### MasterControl Supplier (Supplier™ family) — Evidence A (product pages + one help-center overview)

- Help center overview (Tier 1): "Use MasterControl Supplier to store and access supplier ratings, audit records, AVL, and other documentation related to your suppliers and the parts and components they provide." Tasks: Create/Edit a Supplier InfoCard, "Add materials, parts, and services information", view virtual folders and reports.
- Supplier Management page: "maintains all supplier quality data and documentation in one place… A supplier management system simplifies supplier qualification and supplier corrective action request (SCAR) processes."
- Supplier Quality Management page: "automatic tracking of supplier information stemming from audits, nonconformance reports, and CAPAs - information which is critical in generating supplier rating… approved-vendor reports that include lists of the materials or services a supplier is approved to provide, the supplier's rating, and the supplier's contact information."
- Supplier Audit page: "Maintenance of all supplier status data and essential quality information in a central, secure repository… supplier approval status, contact information, audits, non-conforming material reports, CAPA reports, contracts, approved goods and services, supplier ratings…"; "The capability to manage approvals at the individual part or services level"; "Organization-wide access to AVLs as they are updated in real time"; "Access to supplier-focused quality event solutions, such as MasterControl Supplier Corrective Action (SCAR)™, MasterControl Supplier Deviation™, and MasterControl Supplier Scorecard™"; "It also supports the successful fulfillment of a number of qualifications, such as supplier surveys, supplier audits, and process validation."
- Supplier Deviation (from Supplier Management page): "creates a formal process where vendors can request an exception to written specifications. Materials are shipped only after the appropriate individuals have reviewed and approved the request and provided proper justification." — the concession loop with buyer approval gating shipment.
- Supplier CAPA page: "suppliers are added, replaced, or dropped and the statuses of existing suppliers constantly fluctuate. During the course of such events, CAPA activities involving these suppliers frequently arise…"; "bi-directional goods and services links let users automatically check approval statuses"; "Supplier View… displays a Supplier Status field for each supplier, indicating if a particular vendor is approved or not."
- Integration: "Seamless integration with complementary quality solutions such as MasterControl Audit™, MasterControl CAPA™, and MasterControl Risk™."

Observations: the regulated pole centers the **AVL with part-level approvals** (approval status per supplier AND per part/service), fed by qualification evidence (surveys, audits, process validation), with a supplier quality-event family (SCAR, Supplier Deviation, Supplier Scorecard) integrated with the wider QMS (Audit, CAPA, Risk). The deviation artifact is buyer-approved exception-to-spec with shipment gating.

### QT9 QMS supplier modules — Evidence A (product pages)

- Modules page: supplier family = Supplier Evaluations, Supplier Surveys, Supplier Web Portal; adjacent: Inspections, Deviation Management, CAPA, Nonconforming Products, Audit Management.
- Supplier Evaluations: "streamlines how organizations qualify, assess and re-evaluate suppliers. With built-in tools for tracking supplier performance, managing risk and documenting corrective actions…"; "Create reusable supplier evaluations online"; "Send your suppliers their scorecard using QT9 QMS"; "Suppliers can access full evaluation history in the QT9 QMS Supplier Portal"; FAQ: "Supplier evaluation within a QMS is a structured process used to assess suppliers based on criteria such as quality performance, delivery reliability, compliance history, and risk… to support informed sourcing decisions."
- Supplier Web Portal: "Track and respond to nonconforming product and corrective actions tasks" (suppliers work NCPs/CAPAs in the portal); "Use supplier surveys to manage supplier approval processes"; "You define and set your supplier's login credentials"; "Allow suppliers direct access to evaluation history"; "View and track documents assigned to suppliers."
- Inspections: "Whether you're monitoring incoming materials, in-process production or final product quality…"; FAQ names "Receiving Inspection – An examination of received goods to ensure they are as specified and undamaged" and "First Article Inspection"; "Track lot number, PO number and even job number per inspection"; "Track certificates of analysis or compliance with unlimited file attachments"; "Link failed inspection records or criteria to nonconforming products or corrective actions"; "Easily create unlimited inspection plans per part or product category" (revision-controlled).
- FAQ: "Is supplier management required by regulators? Both the FDA and ISO have established standards that support comprehensive supplier management… Regulatory bodies stress that product owners are the final responsible party for ensuring the quality of all inputs, including those from external parties."

Observations: the SMB pole realizes the same structures lighter: supplier records + evaluations/surveys (approval via surveys), a supplier portal where suppliers work NCP/CAPA tasks, receiving inspection at lot/PO grain with CoA attachments, and linkage into NC/CAPA. Regulatory framing (product owner responsible for inputs) is explicit.

## Cross-product Comparison

| Structure | Octave SCQM | SAP S/4HANA QM | SupplyOn QM | MasterControl Supplier | QT9 QMS |
|---|---|---|---|---|---|
| Supplier(-part) quality record with buyer-maintained approval standing | supplier tracking + PPAP approvals/waivers | quality info record (vendor×material×plant): release, blocking, validity period/quantity, stage model | supplier records in network; parts qualification process | Supplier InfoCard + AVL, approval per supplier AND per part/service | supplier records; approval managed via surveys/evaluations |
| Part/material qualification evidence | PPAP app (submissions, approvals, waivers, change requests) | first-article / release stages; production piece approval; QA agreements | APQP/PPAP readiness process; parts qualification (Project Management) | supplier surveys, audits, process validation as qualification | supplier surveys; inspection plans per part |
| Incoming/source inspection | Receiving & Inspection app (schedules, sampling plans, skip-lot by supplier performance) | GR inspection lots (stock-relevant, usage decision); source inspection at supplier site; certified-supplier skip | Inspection \| Audit Management; incoming-goods data feeds assessment | (not centered on fetched pages; NC material reports referenced) | Inspections module (receiving inspection; lot/PO/job tracking; CoA attachments) |
| Supplier quality issue loop | SCAR app ("same corrective action procedures used internally"; supplier remediation steps) | (complaint machinery not fetched — not asserted) | Complaint Management 8D/9S Problem Solver (D1–D8, containment + clean date, deadlines, escalation, asymmetric visibility) | SCAR app; Supplier Deviation (buyer-approved exception, shipment gating) | NCPs + CAPA tasks worked by suppliers in portal; Deviation module |
| Supplier evaluation / rating | Supplier Rating app (scorecards, "up to five dimensions", sourcing decisions) | (vendor evaluation not fetched — not asserted) | Performance Monitor (PPM + delivery, traffic lights, monthly, supplier-visible, historical) | Supplier Scorecard app; ratings from audits/NCs/CAPAs | Supplier Evaluations (scorecards sent to suppliers) |
| Supplier participation | "include suppliers directly in product lifecycle" | (supplier-side not centered in fetched content) | full two-sided: supplier executes 8D steps in-system; supplier-internal data private; self-administered access rights | (portal implied; not fetched) | Supplier Web Portal (credentials buyer-set; NCP/CAPA response; surveys; evaluation history) |
| Audits | PPAP audits (FAQ); audit mgmt separate app | (audit mgmt separate) | Audit Management module | Supplier Audit app (qualification fulfillment) | Audit Management module (separate) |
| Certificates | chemical/material info via integration | certificate type in material master; QM-system certification skip | (certificate mgmt in family per prior pass) | documentation incl. certifications | CoA/CoC attachments on inspections |
| Deviation/concession | PPAP waivers | (release restrictions) | Supplier deviation requests (Technical Review) | Supplier Deviation (exception to spec, approval before shipment) | Deviation Management module |
| Traceability linkage | supplier material/chemical info via ERP | lot/stock-relevant inspection lots | part/batch/serial context linkage | part/service links | lot/PO/job tracking per inspection |

Cross-product commonalities (Evidence B):

1. Every sampled product maintains a **supplier(-part) quality record with buyer-controlled approval standing** (AVL/quality info record/release status/approval per part).
2. Every sampled product has a **supplier quality issue loop** in which quality problems attributed to supplier material are recorded, responded to by the supplier (or processed with supplier participation), and closed (SCAR / 8D complaint / NCP+CAPA / deviation).
3. Every sampled product accumulates **quality evidence on the supplier/part record** (inspection results, audit findings, certificates, complaint history) and uses it to maintain/adjust the standing and to evaluate suppliers.
4. Part-level qualification before/at sourcing is common (PPAP, first-article, part-level AVL approvals, qualification processes).
5. Supplier-facing participation surfaces are common (portals, shared 8D workflows, scorecard visibility).
6. Evaluation/scorecards feeding sourcing decisions are common.

Divergences (variant axes):

- Where the standing lives: standalone eQMS record vs ERP quality info record vs network platform record.
- Whether incoming inspection is centered (Octave, SAP, QT9) or peripheral (MasterControl pages; SupplyOn delegates to buyer's internal QM/backend integration).
- Methodology packaging: 8D/9S (SupplyOn, automotive), PPAP (Octave, SupplyOn, SAP first-article), SCAR naming (Octave, MasterControl), generic CAPA/NCP (QT9).
- Deployment: eQMS suite module (Octave, MasterControl, QT9), ERP-embedded (SAP), industry network (SupplyOn).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The buying manufacturer's quality-side system of record over its supplier base. Three jointly-held structures:

1. **The supplier(-part) quality standing of record.** Suppliers — and, at the finer grain, the parts/materials/services they supply — are held as quality-managed records whose approval/qualification status is established and changed by the buying organization: approved-for-quality standing that gates use of the supplier's material. Realizations: approved-vendor list with part-level approvals; quality info record with release status/blocking/validity; PPAP/first-article-class part approvals. Remove → supplier directory (Supplier Management Platform territory) or a part catalog.
2. **The two-sided supplier quality issue loop.** Quality problems attributed to supplier-provided material are recorded as events (complaint / SCAR / supplier NC), routed to the supplier for structured response (containment → root cause → corrective action → effectiveness verification), with the affected material dispositioned (deviation/concession with buyer approval, return, sort/clean), and the loop closed only on earned verification. Remove → internal CAPA machinery, or a complaint log with no supplier loop.
3. **The quality evidence base feeding the standing.** Quality evidence about the supplier and its material — incoming/source inspection results, audit findings, certificates, complaint history, accumulated performance data — is held against the supplier/part record and drives evaluation (scorecards/ratings) and approval adjustments (approve / restrict / tighten-or-skip inspection / exit). Remove → an unmoored approved list nobody verifies, or bare inspection data with no supplier standing.

Jointly-held load-bearing:

- 1 alone = approved vendor list (Supplier Management Platform)
- 2 alone = CAPA/complaint machinery with a supplier field (CAPA Management)
- 3 alone = inspection records / certificate repository (Inspection & Metrology / document storage)
- 1+2 without 3 = approvals and complaints with no evidence base
- 1+3 without 2 = qualification program with no issue handling
- 2+3 without 1 = quality events and data with no supplier standing (scattered quality records)

### L1 — Common Mature Structure

- Part-level qualification before/at sourcing (PPAP / first-article / part-level AVL approvals / qualification processes) — present in all five sampled products in some form.
- Incoming/receiving inspection of supplier material with lot/PO linkage, feeding usage/acceptance decisions (centered in 3 of 5; present as NC material reports elsewhere).
- Supplier evaluation scorecards/ratings (quality metrics such as defect/PPM figures plus delivery and responsiveness) feeding sourcing decisions.
- Supplier audits (on-site or desk) as qualification and standing-maintenance evidence.
- Certificates (CoA/CoC, QM-system certification) as attached evidence; certification-based inspection relief.
- Supplier-facing participation surfaces (portals, shared issue workflows, scorecard visibility).
- Deviation/concession handling as a disposition family inside the issue loop.
- Integration with ERP/procurement (supplier master, POs, receipts) and with the wider QMS (CAPA, audit, NC, risk).

### L2 — Variant / Optional

- Methodology packaging: 8D/9S problem solving (automotive-dominant), PPAP (automotive), AS9102-class FAI (aerospace), GMP supplier qualification (life sciences), generic CAPA/SCAR.
- Whether incoming inspection is centered or delegated (backend integration with the buyer's internal QM at the network pole; stand-alone QM-in-procurement without inspections at the ERP pole).
- Stage models of the supply relationship (first-article → preliminary series → regular procurement).
- Skip-lot / sampling-plan relief driven by supplier performance; certified-supplier inspection skip.
- Multi-site/plant structures, supplier-initiated change requests (PCN/ECN), traceability linkage depth (part/batch/serial).
- Deployment: eQMS suite module, ERP-embedded, industry network platform, SMB suite.
- Regulatory regime packaging (FDA/ISO 13485/IATF 16949/VDA) — shapes vocabulary and approval depth, not structure.

### L3 — Vendor-specific (research notes only)

- Octave: the four-app naming (PPAP / Receiving and Inspection / SCAR / Supplier Rating); "up to five dimensions of performance"; stat blocks (35% cost-of-quality reduction etc.); Cree/Rheem quotes.
- SAP: transaction-level machinery (QI01/QI07/QA51-class reports, inspection lot origin 01, movement type 101, usage decision, "Source inspection instead of GR inspection" indicator, inspection lead time subtraction, OData API field names like ProductionPieceApprovalIsRequired).
- SupplyOn: Problem Solver naming ("e-8D" at ZF), 8D report rating, task status vocabulary (Closed/waiting/Open), "clean date for corrected parts", Performance Monitor monthly cadence ("by the tenth working day"), traffic-light function, supplier self-administration of access rights, 9S variant.
- MasterControl: Supplier™ family naming (SCAR™, Supplier Deviation™, Supplier Scorecard™), InfoCard/virtual-folder model, "Supplier View" status field, bi-directional goods/services links.
- QT9: three-module supplier family naming, portal included without extra licensing, buyer-set supplier credentials.

## Vendor-specific Findings

- The two-sided documentation/visibility split recurs (SupplyOn: supplier-internal data private to supplier; QT9: buyer-set supplier credentials; ZF: supplier self-administration of access rights) — two-sidedness is cross-product; the specific visibility mechanics are vendor-specific.
- Vendor-authored boundary statements usable as market discrimination evidence: Octave SCAR FAQ ("using the same corrective action procedures used internally" — the seam vs internal CAPA); SupplyOn ("instead of fragmented email- and spreadsheet-based complaint handling"; "No internal process change necessary — you continue working with your internal system via backend integration" — the seam vs internal QMS); SAP ("QM in Procurement as 'stand-alone'… except those for processing goods receipt inspections" — inspection is a separable layer).
- PPM as the quality key figure is documented at ZF/SupplyOn (customer case) — automotive-dominant realization, not definitional.

## Rejected Findings

- "SQM = PPAP + 8D" — rejected as definition: PPAP and 8D are sector methodology packaging (automotive); MasterControl/QT9 realize the same structures with AVL + SCAR + surveys and generic CAPA/NCP. The invariants are part-qualification evidence and the supplier response loop, not the named methods.
- "Incoming inspection is definitional" — rejected: SAP documents QM-in-Procurement stand-alone without GR inspections; SupplyOn delegates inspection to the buyer's internal QM via backend integration; MasterControl's fetched pages center AVL/SCAR/deviation/scorecard rather than inspection. Incoming inspection is the dominant realization of the evidence base, not the invariant.
- "Scorecards are definitional" — rejected as invariant: universal in the sample but the standing can be maintained without a computed score (approval status + evidence). Held L1.
- "SQM is just a QMS module" — rejected as identity claim: every sampled product ships supplier quality as a first-class center (dedicated app set at Octave, dedicated family at MasterControl, dedicated solution family at SupplyOn, dedicated modules at QT9, first-class QM-in-Procurement at SAP); the manufacturing-qms pass itself classified SQM as a component Type with standalone focus.
- "Supplier portal is the Type" — rejected: the portal is the participation surface; the record + loop is the Type (consistent with the supplier-portal pass's surface-vs-record line).
- "Supplier quality = supplier risk" — rejected: different evaluative lenses (conformance evidence vs risk signals); see Boundary Findings.

## Boundary Findings

1. **vs Manufacturing QMS (§16, processed)**. QMS = the quality function's whole system of record (record population + closed loop + compliance anchor, production-anchored); SQM = the supplier-facing slice centered as its own system. The manufacturing-qms pass pre-ratified this: "component Type / module… as a standalone focus; inside the QMS it is one record class among several." Seam: center of gravity. SQM lacks the QMS's document-control/training spine as core; QMS lacks the supplier standing/evaluation center. RATIFIED — keep both.
2. **vs CAPA Management (§16, processed)**. CAPA = the corrective-action loop as such from any source; SQM = the supplier relationship centered, of which the SCAR is one loop instance addressed to an external party with supplier participation and material disposition. Octave's own wording ("using the same corrective action procedures used internally") is vendor evidence of the seam. RATIFIED — keep both.
3. **vs Supplier Management Platform (§10, processed)**. SMP = supplier of record + buyer-controlled commercial standing + maintained information base (identity, banking, contracts, onboarding); SQM = quality standing + quality issue loop + quality evidence. Both maintain "approval status" — SMP's gates procurement eligibility, SQM's gates quality fitness of material/parts. SMP's own doc lists Supplier Quality as a domain slice. Overlap zone: qualification questionnaires and certificate collection exist in both; the discriminator is what the standing is *for* and what events maintain it. RATIFIED — keep both.
4. **vs Supplier Risk Management (§10, processed)**. SRM = risk standing from external signals + due diligence + criticality, with a risk action loop feeding procurement decisions; SQM = quality standing from conformance evidence (inspection/audit/certificate/complaint history), with a quality issue loop. Audits appear in both (SRM: mitigation; SQM: qualification/evidence) — the third-party-cyber-risk pass's flag. Seam: risk lens vs conformance lens; event substrate (external signals vs material quality events). RATIFIED — keep both.
5. **vs Manufacturing Supplier Collaboration (§16, processed)**. Collaboration = the demand/commitment/fulfillment loop (orders, releases, ASN, receipt); SQM = the quality loop (qualification, complaints/SCARs, deviations, evaluation). The collaboration pass's flag DISCHARGED: SupplyOn ships Quality Management as a separate solution family from Supply Chain Collaboration; e2open ships quality as a separate application; the SQM core is the quality record/8D-class loop. RATIFIED — keep both.
6. **vs Inspection & Metrology Software (§16, processed)**. I&M = the part-grain geometric conformance loop (nominal vs measured geometry, CMM-class execution); SQM's incoming inspection is the supplier-facing acceptance/usage decision at lot grain (checklists, sampling, usage decision), not metrology depth. QT9's inspection module (checklists, lot/PO tracking) vs I&M's CAD-nominal machinery makes the seam visible. RATIFIED — keep both.
7. **vs Statistical Process Control (§16, processed)**. SPC monitors internal process variation against control limits; SQM aggregates supplier quality performance and events. Different subject, different machinery. RATIFIED.
8. **vs Third-party Risk Management (§15, processed)**. TPRM = risk assessment of any third party (vendors, partners, contractors) with no supplier lifecycle or quality-record center; SQM = suppliers, quality lens, quality record center. Audits-as-mitigation (TPRM/SRM) vs quality record (SQM). RATIFIED.
9. **vs Supplier Portal (§10, processed)**. Portal = the supplier-facing interaction surface; SQM = the buyer-side quality record + loop the portal feeds. Consistent with the supplier-portal pass's surface-vs-record line and the collaboration pass's ratification. RATIFIED.

## Uncertainties

- SAP QM complaint/notification machinery (vendor complaints/QM notifications) was not fetched; no claims made about SAP's complaint loop. SAP evidence covers the standing/inspection/qualification legs only.
- SupplyOn help-center article bodies remain login-gated (per the manufacturing-supplier-collaboration pass); procedural states (exact complaint statuses beyond the supplier-guide's Closed/waiting/Open) not verified. Solution pages + partner onboarding center + customer-published pages used instead.
- MasterControl workflow details (SCAR stages, deviation approval routing) not verified beyond product-page descriptions; one help-center overview page fetched.
- Whether supplier scorecards are always supplier-visible: documented at SupplyOn (Performance Monitor), QT9 (scorecards sent to suppliers), ZF case study; not asserted for Octave/MasterControl.
- Historical check rests on conceptual lineage (paper-era approved vendor lists, receiving inspection logs, supplier corrective-action letters, paper PPAP submissions, certificate files) plus vendor-authored contrasts (ZF case study: "The conventional paper-based assessment process, which is characterized by media disruption…"; SupplyOn: "instead of fragmented email- and spreadsheet-based complaint handling"). No fetched pre-digital source; assertion strength kept at conceptual level.
- e2open's Risk & Quality app not fetched (named by the collaboration pass); treated as corroborating market-structure context only.

## Final Synthesis

Supplier Quality Management is the **buying manufacturer's quality-side system of record over its supplier base**. Its world has three jointly-held structures: (1) the supplier(-part) quality standing of record — suppliers and the parts/materials they supply held as quality-managed records carrying buyer-maintained approval/qualification status that gates use of the material; (2) the two-sided supplier quality issue loop — quality problems attributed to supplier material recorded as events, routed to the supplier for structured response (containment → root cause → corrective action → effectiveness), with affected material dispositioned under buyer approval and closure earned; (3) the quality evidence base — inspection results, audit findings, certificates, complaint history, and accumulated performance data held against the record, driving evaluation and approval adjustments. The five sampled poles (enterprise eQMS suite, ERP-embedded, automotive network, regulated life sciences, SMB QMS) realize the same three structures with different packaging: PPAP/8D/FAI are sector methodology, incoming inspection is the dominant-but-optional evidence channel, scorecards are the dominant evaluation realization, and the supplier portal is the participation surface. The Type's boundaries hold on five seams: internal quality (QMS), the loop alone (CAPA), commercial standing (Supplier Management Platform), risk lens (Supplier Risk Management / TPRM), and the demand/fulfillment loop (Manufacturing Supplier Collaboration).
