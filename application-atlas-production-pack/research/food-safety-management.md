# Research Notes — Food Safety Management

## Research Goal

Understand "Food Safety Management" (§20 Agriculture, Food & Natural Resources) as an Application Type: what objects an FSMS-class product holds, who operates it, what the daily loop looks like, what rules and states matter, and where the boundary sits — especially against the processed siblings **food-recall-management** (§20, 2026-09-08), **food-cold-chain-management** (§20, 2026-09-08), **food-manufacturing-erp** (§20, 2026-09-08), the unprocessed sibling **haccp-management** (§20), **food-traceability-platform** (§20, unprocessed), and neighboring machinery types (Manufacturing QMS, CAPA Management, Compliance Management, Store Task Management).

Three sibling passes pre-hung seams for this leaf:
- **food-recall-management**: "FSMS/HACCP center the standing *program* machinery (hazard analysis, CCPs/PCPs, monitoring, verification, CAPA, audits); the recall is the *emergency-response event* the program prepares for." Test recorded: remove the event workflow → the FSMS remains; remove the program machinery → the recall event workflow remains.
- **food-cold-chain-management**: "temperature is the dominant CCP family and temperature-monitoring products market themselves as HACCP-compliance tools — seam held this pass = program machinery … vs the physical temperature-controlled estate + excursion response loop." JOINT REVIEW RECOMMENDED with haccp-management and food-safety-management.
- **food-manufacturing-erp**: boundary finding #6 — the ERP records lot movements and QC statuses as operations; dedicated Types center the traceability network or the food-safety program machinery.

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is the food business's **standing food-safety program of record** — the software machinery to build and operate a food-safety management system (FSMS): hazard analysis, control plans (HACCP/food-safety plans), prerequisite programs (PRPs), monitoring records, corrective actions/CAPA, verification, audits, document control, supplier approval, certification readiness.
- Suspected nearest neighbors: HACCP Management (§20 sibling — possibly overlapping/alias risk), Food Recall Management (§20, processed), Food Cold Chain Management (§20, processed), Food Traceability Platform (§20), Food Manufacturing ERP (§20, processed), Manufacturing QMS / CAPA Management (§16), Compliance Management (§11), EHS platforms (§21), Store Task Management / ops execution (§05/§26).
- Suspected boundary test: remove the standing program machinery → recall event workflow / cold-chain estate / traceability ledger each remain as separate Types; remove the hazard-control plan → generic QMS/audit tooling remains.

## Research Questions

1. What objects does an FSMS-class product hold? (plans, hazards, PRPs, forms, records, deviations, CAPA, documents, suppliers, audits…)
2. What is the daily loop vs the periodic (verification/audit) loop?
3. How do certification frameworks (HACCP, GFSI, BRCGS, SQF, FSSC 22000, IFS, FSMA, ISO 22000) feature — definitional or common?
4. What is the real seam vs HACCP Management (§20 sibling)?
5. What is the seam vs ops-execution/checklist products that market "food safety tasks"?
6. What roles exist (site staff vs food-safety manager vs corporate/above-site vs suppliers/auditors)?
7. What is the analog ancestor, and would a paper-era program satisfy the invariants?
8. Where do traceability/recall/temperature modules sit inside FSMS products — core or optional?

## Representative Products

| Product | Vendor | Pole | Why chosen | Depth reached |
|---|---|---|---|---|
| Ideagen Safefood 360° | Ideagen | Enterprise manufacturer, GFSI certification suite (35+ modules) | The certification-machinery FSMS pole; module taxonomy is the richest evidence of the Type's object world | Root + food-safety-management solution page + full module catalog (36 named modules, self-categorized) |
| SafetyChain Software | SafetyChain | US food & beverage plant FSQA execution | The plant-floor "close the loop" pole; explicitly frames programs → deviations → CAPA → verification → closure | Root + Food Safety Programs solution page |
| FoodDocs | FoodDocs | SMB foodservice/retail/care digital FSMS, AI-assisted | The SMB/app-led pole with HACCP plan builder; UK EHO-ratings-driven framing | Root page (product, features, FAQ, positioning) |
| Crunchtime Ops Execution (ex-Zenput) | Crunchtime | Multi-site restaurant/c-store ops execution with embedded food safety | Boundary pole: checklist/task-execution core where food safety is a compliance surface, not the center | Ops Execution page (via zenput.com redirect) |

Selection rationale: market representation (certification suite / plant FSQA / SMB app / chain ops), different product philosophies (document-first management system vs execution-first quality vs app-first SMB vs task-first ops), different customer tiers (enterprise manufacturer → mid-market plant → SMB sites → franchise chains). Unreachable: Icicle Technologies (transport error — SMB manufacturer FSMS/ERP pole unsampled); iFoodDS (produce supply-chain quality-data pole) not attempted after saturation.

## Sources

Evidence layer A (official product pages, fetched 2026-09-08):

- Ideagen Safefood 360° — https://safefood360.com/ (root); https://safefood360.com/food-safety-management-software/ ; https://safefood360.com/product/modules/ (module catalog)
- SafetyChain — https://safetychain.com/ (root); https://safetychain.com/platform/food-safety-programs
- FoodDocs — https://www.fooddocs.com/ (root incl. FAQ block)
- Crunchtime Ops Execution — https://www.zenput.com/ (redirects to Crunchtime Ops Execution page); https://www.crunchtime.com/operations-platform (404)

Not reachable: help-center / KB articles for all four vendors (not attempted beyond roots/solution pages after saturation; module/plan-tier specifics therefore unverified). Icicle Technologies — https://www.iciclehq.com/ — transport error, abandoned after one failure.

## Product Observations

### Ideagen Safefood 360° (evidence layer A — root, solution page, module catalog)

Positioning: "combines power, scalability, speed and efficiency… Integrating food safety, supplier quality, and compliance management into one cloud-based platform to manage all major global and retailer technical standards." "Designed to manage your audits, HACCP and PCP plans, present information in intuitive dashboards and reports." "Over 35 modules – creating an audit-ready working environment for any GFSI-recognized standard." Built "from the requirements of SQFI, BRCGS, ISO, FSSC, FSMA, the Safe Food for Canadians Act and other global standards."

Homepage feature blocks (six named):
- **HACCP / PCP**: "Create HACCP, PCP and Food Safety Plans, integrating risk assessment models, decision trees and a custom hazard database for full GFSI and retailer compliance."
- **Management System**: "Take control of your key management processes, including CAPA and deviation management, auditing, management review, recalls and more."
- **Prerequisite Programs**: "Manage all PRPs in one place. Modules include cleaning, maintenance, pest control, employee training, glass & plastic control, and more."
- **Monitoring**: "Start monitoring your production process, product batches, material deliveries or other areas of business. Integrate with IOT devices and be alerted in real-time when results are out of specification."
- **Supplier Management**: "Manage approved suppliers directly or enable self-assessments. Conduct audits, risk assessments and appraisal scorecards while scheduling document reviews and tasks to prevent oversights." (separate solution page; supplier portal)
- **Document Control**: "Integrate your key documents and plans into Ideagen Safefood 360°… Approve documents, notify users of changes, and maintain version control."

Signature features (solution page): paperless FSMS; automated scheduled reports; "one central hub for all records, programs, and processes"; "Automate Schedules — clear overview of upcoming and overdue tasks to ensure all work is done as planned and nothing falls between the cracks"; "automatic alerts to the latest nonconformances or events"; "Major global standards and legislation are automatically updated in the system."

Module catalog (36 modules, vendor's own category tabs Documents / HACCP / Management / Monitoring / PRPs / Supplier Management / Utilities): HACCP, PCP & Food Safety Plans; Hazard Database; Complaints; Corrective Action; Auditing; Management Review; Non conformance; Business Process; Recall & Withdrawal; Quality Management; Calibration; Cleaning; Maintenance; Code of Practice; Contamination Control; Microbiological Control; Glass & Plastic Control; Pest Control; Medical Screening; Traceability; Training; Supplier Management; Supplier Portal; Monitoring; Receiving; Batching; Document Control; Employee Database; Products & Materials; Categories; Contacts; Items; Tests; Alerts; Reports; Discussions.

Modules framed as "Designed by food safety experts… Compliant with industry standards… Ready to use right out of the box."

Reading: the vendor's own taxonomy is the FSMS structure — HACCP plan family + PRP family + management-system family (CAPA/nonconformance/audit/management review) + monitoring + supplier + documents. Recall & Withdrawal and Traceability appear as modules *inside* the management system — corroborating the recall pass's "one process among many" finding.

### SafetyChain (evidence layer A — root, Food Safety Programs page)

Positioning: "#1 Digital Plant Management Platform for Food & Beverage", "trusted in 2,500+ manufacturing facilities to digitize quality, streamline compliance". One of six suite pillars is "Food Safety Programs"; others: Regulatory & Customer Compliance, In-Process Quality, Production Monitoring, Process & Data Controls, Supplier Compliance.

Headline thesis: "Food Safety Programs That Close the Loop. Food safety only works when issues are corrected, verified, and prevented from happening again."

Food Safety Programs feature set:
- Digital Forms: "No-code forms for inspections, quality checks, and audits"
- Document Access: "Access SOPs and compliance materials directly in mobile workflows"
- CAPA Workflows: "Automate corrective actions and issue resolutions"
- Supports: "Pre-Op Hygiene; Master Sanitation; GMP; Facility Audits; Receiving Inspections; HACCP Monitoring; Corrective and Preventive Actions (CAPA)"

Program families (three named):
- **Facility and Hygiene Programs**: "Standardize and enforce Pre-Op inspections, GMPs, sanitation checks, and facility audits so deviations trigger corrective actions, verification steps, and documented closure—ensuring problems are resolved, not repeated."
- **Material and Incoming Programs**: "Confirm receiving inspections are performed and documented at the point of receipt, automatically escalating material issues…"
- **Process Safety Programs**: "Execute HACCP monitoring and required verification workflows with built-in accountability, so missed critical limits drive immediate corrective action, verification, and traceable documentation—supporting defensible HACCP programs."

Grade-A Food Safety, Every Day block: "One System for All Programs — Manage GMPs, Pre-Ops, HACCP, sanitation, and receiving checks in a single platform that connects execution, corrective action, and oversight"; "Digital Forms at the Point of Work — Capture food safety data in real time using configurable forms that enforce requirements as work is performed"; "Built-In Scheduling, Verification, and CAPA — Ensure required checks, corrective actions, and supervisor reviews happen on time, every time, without manual follow-up"; "Exception-Based Oversight — Automatically surface out-of-spec results and incomplete records so teams focus on what needs attention"; "Centralized, Defensible Records — Maintain secure digital records with timestamps, signoffs, corrective actions, and full audit history"; "Real-Time, Plant-Wide Visibility". "No Binders. No Blind Spots. No Unresolved Issues." Customer quotes name users: FSQA Coordinator, Food Safety Coordinator, QA & Food Safety Manager.

Reading: the same four-part structure as Safefood but execution-first: programs → scheduled digital forms → deviations (including *incomplete records* surfaced as exceptions) → CAPA → verification → documented closure → audit-ready records.

### FoodDocs (evidence layer A — root page incl. FAQ)

Positioning: "Top-Rated FSMS Software. Comply Easily with the Best Food Safety Software. Try the intuitive digital Food Safety Management System…" FAQ: "FoodDocs is a HACCP-based food safety management software platform that helps hospitality groups, care homes, and food-to-go businesses manage food safety digitally. The software includes daily monitoring, food safety inspections, audits, HACCP plans, traceability, corrective actions, reporting, and compliance management."

Mechanics:
- Setup: "The AI-powered FSMS software creates personalized pre-set tasks for you… Customize tasks according to your food safety operations and assign them to team members. Adjust the monitoring system and tasks any time you need." ("Implement your Food Safety Management System in 15 minutes" — vendor claim.)
- Execution: mobile app "Receive smart notifications and food safety alerts"; "App checklists for food safety include detailed visual instructions"; "add corrective actions if the task is not filled as required by food safety protocols"; sensor integrations (smart fridges, temperature sensors) auto-sync to temperature monitoring checks.
- Oversight: "Monitoring Logbook — Get a detailed overview of your completed tasks and protect your brand by staying compliant"; "timestamped proof of compliance"; "Real-Time Overview — Monitor your company's food safety compliance remotely with a look… across all locations"; AI reports (task completion, heatmaps, trends).
- Plan machinery: "Get a ready-to-use HACCP Plan in 1 hour or less — Automatically generated Hazard Analysis, Critical Control Points, Standard Operating Procedures, and Flow Chart… Keep your food safety compliance docs for food inspectors and customers in one place."
- Audits: "Conducting internal food safety audits to meet higher standards" (trial feature list).
- Trace & recall: "Trace and recall your production with ease… in case of product recalls or potential hazards."
- FAQ "What is a digital Food Safety Management System?": "A food safety management system (FSMS) is the framework that ensures your business controls food safety hazards, maintains compliance, and protects customers." Manages: "Digital food safety checklists, Automated monitoring logs, Temperature records, Corrective actions, Supplier and traceability documentation."
- Compliance disclaimer: "While the software supports compliance, it cannot guarantee regulatory compliance… FoodDocs is fully customizable, allowing you to adapt checklists, procedures, and documentation based on inspector feedback and your specific operational requirements."
- Users named: Food Safety Managers, Operations Managers, Executive Chefs, Culinary Managers. Industries: hospitality, food-to-go/retail, healthcare. UK EHO "5-star ratings / scores on the doors" framing; US + UK presence; 30,000+ users claimed (vendor).

Reading: the same program structure in miniature: plan (HACCP builder) + PRP-ish daily tasks + monitoring records + corrective actions + audits + docs + trace/recall module — app-led, checklist-fronted, SMB-weighted. The vendor's own FSMS definition matches the canonical frame.

### Crunchtime Ops Execution / Zenput (evidence layer A — ops-execution page)

Positioning: "Zenput is now Crunchtime Ops Execution"; "Drive consistent restaurant operations execution at every location." Part of a restaurant ops suite (inventory, labor & scheduling, ops execution, kitchen, guest, L&D).

Food-safety-relevant mechanics: "Crunchtime Ops Execution automates daily operational tasks, from line checks and opening checklists to audits and food safety processes. And it highlights incomplete work so your stores can deliver the best guest experience every day." "Stay on top of critical food safety tasks through integration with Bluetooth temperature probes, automatic temperature monitoring, and food labeling." Above-store oversight: "Track which tasks were done on time (or not) and identify whether tasks weren't completed correctly." AI photo validation flags blurry/wrong photos. Regulator evidence: "your operational leaders can easily select relevant dates in Ops Execution and pull up a comprehensive report of the work that's been done in that location as well as the audits that have been completed."

Reading (boundary pole): task-execution machinery — scheduled checklists, temperature capture, labeling, escalation of incomplete work, audit reports. What is *not* evidenced on the page: hazard analysis/plan building, PRP program structure, CAPA/nonconformance workflows, document control, supplier management, management review. Food safety rides a generic ops/task core. This is the seam against Store Task Management / ops-execution territory: a product can carry food-safety checklists without being an FSMS.

## Cross-product Comparison

| Dimension | Safefood 360° | SafetyChain | FoodDocs | Crunchtime OpsX |
|---|---|---|---|---|
| Center of gravity | management system (35+ modules) | program execution "close the loop" | digital FSMS app | task/ops execution |
| Plan machinery | HACCP/PCP & FS Plans + Hazard Database (module family) | HACCP monitoring programs (execution-level) | AI HACCP plan builder (hazard analysis, CCPs, SOPs, flow chart) | not evidenced |
| PRPs | dedicated PRP module family (cleaning, pest, glass & plastic, training…) | Pre-Op/GMP/sanitation program family | hygiene/daily tasks with instructions | line checks |
| Monitoring records | Monitoring module + IoT alerts | digital forms at point of work | mobile checklists + sensors + logbook | checklists + probes + labels |
| Deviation → corrective action | CAPA + Non conformance modules; alerts on nonconformances | deviations trigger CAPA, verification, documented closure | corrective actions attached to tasks | incomplete-work surfacing (no CAPA workflow evidenced) |
| Verification / review | Auditing + Management Review modules | verification steps; supervisor reviews; exception-based oversight | internal audits; real-time remote oversight | above-store review of task completion |
| Documents | Document Control (approve/version/notify) | SOPs accessible in workflows | compliance docs in one place | not evidenced |
| Suppliers | Supplier Management + Portal (separate solution line) | Supplier Compliance pillar | supplier documentation (FAQ mention) | not evidenced |
| Traceability / recall | Traceability + Recall & Withdrawal modules | FSMA 204 blog content (adjacent) | trace & recall features | not evidenced |
| Framework posture | GFSI/BRCGS/SQF/FSSC/IFS/FSMA/SFCA; standards auto-updated | audit-ready, defensible HACCP programs | HACCP-based; EHO ratings | health-department reporting |
| Primary audience | food manufacturers/processors (GFSI) | F&B manufacturers (plants) | foodservice/retail/care SMBs | restaurant/c-store chains |

Reading: three of four (Safefood, SafetyChain, FoodDocs) independently realize the same structure — **plan + PRP program of record → scheduled monitoring records → deviation/corrective action → verification/audit → audit-ready evidence** — with suite depth varying by segment. The fourth realizes only the record/execution leg and is the boundary pole. Framework machinery, supplier management, document control, traceability/recall modules are common in mature products but scale with the customer tier (manufacturer-class heavy, foodservice-class light or absent).

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

A Food Safety Management application is the food operation's **standing program system of record**. Four jointly-held structures; remove any one and the product stops being this Type:

1. **The hazard-control program of record** — the operation's food-safety program held as structured, living records: identified hazards and the controls applied against them, organized as control plans (HACCP/PCP/food-safety-plan class: steps, critical limits, monitoring requirements) plus prerequisite programs (cleaning/sanitation, pest control, maintenance, personal hygiene/health, glass & brittle plastic, training, and similar standing programs). Remove → a generic checklist/audit tool or document library.
2. **Scheduled operational record-keeping against the program** — the recurring checks, readings, inspections and forms the operation performs and records at the point of work as evidence that controls are working, timestamped and attributed. Remove → a static document library / plan archive.
3. **The deviation → corrective-action → verified-closure loop** — out-of-spec, missed, or nonconforming results (the system detects *incomplete records* too, not just failed values) become tracked issues requiring documented response, follow-up and closure, with prevention framing (CAPA-class machinery). Remove → passive data logging / a logger.
4. **The verification and evidence function** — review sits structurally above monitoring (supervisor/manager verification, internal audits, management review), and the accumulated record is maintained in an audit-ready, defensible form for inspectors, certification auditors and customers. Remove → shop-floor logging with no management system.

Jointly-held is load-bearing: 1 alone = QMS document store; 2 without 1 = checklist/ops-execution tool (the Crunchtime pole); 3 without 1–2 = generic CAPA tool; 4 without 1–3 = audit-reporting shell. 1+2 without 3+4 = a monitoring logbook, not a management system.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Digital forms/form designer as the record surface; mobile execution with instructions, photos, signatures
- Automated scheduling with overdue/missed-task visibility; alerts/notifications
- Document control (approve, version, notify, distribute SOPs)
- Supplier quality machinery (approval, self-assessments, scorecards, portals) — suite-class products
- Framework/standard content and "audit-ready" packaging (GFSI-type schemes, FSMA, national inspection regimes)
- Traceability and recall/withdrawal modules (consuming/contributing to the program)
- Complaints handling; training records; calibration; microbiological/test results
- Multi-site dashboards; exception-based review; reporting/BI

### L2 — Variant / Optional Structure

- Certification-framework depth: multi-scheme mapping and standards auto-updates (manufacturer-class) vs hygiene-rating-driven simplicity (foodservice-class)
- Sensor/IoT fleets feeding monitoring records automatically (temperature, humidity) vs manual probe/entry
- AI-assisted setup and plan generation (SMB-class pole)
- Enterprise/corporate governance layer (multi-site program standardization, remote oversight)
- Segment module sets: pet food, seafood, bakery, beverage industry editions (Safefood industry pages)
- Lab/test-result integration depth; batching/receiving QC records

### L3 — Vendor-specific (research notes only)

- Safefood 360°: 35+-module architecture, StatusBI self-service BI, "automatic updates" of standards/legislation/outbreak news, free-demo SQF industry pages, Ideagen compliance-division branding
- SafetyChain: "Digital Plant Management" umbrella with six pillars, plant-impact ROI claims ($900k/5x-10x), customer-count claims (2,500+ facilities), industry awards
- FoodDocs: "15 minutes setup / 1 hour HACCP plan" claims, 20% time savings / €20,466/year claims, 5-star EHO ratings framing, 30,000+ users claim, AWS EU deployment detail, plan-tier PDF-export gating
- Crunchtime: AI photo validation, 100,000+ locations claim, franchise hierarchy machinery, Squadle/Teamworx product-line split

## Rejected Findings

- **"FSMS = recall management + traceability"** — rejected. Recall/traceability appear as modules inside FSMS suites (Safefood module catalog; FoodDocs features) but the dedicated Types own those structures (corroborates the recall pass's vendor-structure evidence: Trustwell separate modules; Safefood 360° lists Recall & Withdrawal inside the Management System block).
- **"FSMS = temperature monitoring + checklists"** — rejected as definitional. Sensor/checklist execution is the common record surface; the cold-chain pass holds the physical-estate Type, and the Crunchtime pole shows checklist execution without program machinery is a different product class.
- **"FSMS requires GFSI certification machinery"** — rejected as definitional. Framework machinery is heavy in the manufacturer pole and absent/thin in foodservice/retail poles (FoodDocs names only HACCP-based framing and EHO ratings; Crunchtime names health-department reporting). The Type exists below and beside certification.
- **"Supplier management is core"** — rejected. It is a suite-class capability (Safefood, SafetyChain) absent or thin elsewhere (FoodDocs FAQ mention; Crunchtime none).
- **"FSMS is a manufacturing-only Type"** — rejected. Foodservice/retail/care poles (FoodDocs, Crunchtime) and the historical record show the program machinery across the whole food economy; depth varies.

## Boundary Findings

| Neighbor | Relationship | Distinction | Test |
|---|---|---|---|
| **HACCP Management (§20, unprocessed)** | narrower sibling; JOINT REVIEW RECOMMENDED | The HACCP machinery (hazard analysis → CCPs → critical limits → monitoring → corrective action → verification → records) sits at the center of BOTH. This pass holds the seam at the **management-system layer**: FSMS additionally carries PRPs beyond the HACCP plan, supplier management, document control, management review, and multi-framework certification machinery (the ISO 22000-style management system as a whole). Safefood 360° evidences both in one suite with HACCP/PCP as a named module family beside Management System and PRP families. | Remove the management-system layer → HACCP plan machinery remains (that pass's territory). Remove the hazard-control plan and keep PRP/audit/supplier/doc machinery → generic QMS. |
| Food Recall Management (§20, processed) | embedded workflow class | Recall is one process inside the standing program (Safefood module; FoodDocs feature); the dedicated Type owns the event + notification/response loop | Remove the standing program machinery → the recall event workflow remains |
| Food Cold Chain Management (§20, processed) | estate vs program | Temperature monitoring appears in all FSMS-class products as program records (sensor integrations; HACCP monitoring); the physical estate + excursion-response loop is that Type | Remove the program machinery → the estate/requirement/excursion/record loop remains |
| Food Traceability Platform (§20, unprocessed) | module vs ledger | Traceability appears as an FSMS module (Safefood, FoodDocs); the cross-partner lot-movement ledger is that Type's spine | Remove the program machinery → the lot ledger remains |
| Food Manufacturing ERP (§20, processed) | operations vs program | ERP records lot movements/QC statuses as part of operations; the FSMS centers the program machinery (consistent with that pass's boundary finding #6) | Remove the business back office → the program machinery remains |
| Manufacturing QMS / CAPA Management (§16) | shared machinery, different subject | Deviations, CAPA, audits, document control are generic quality machinery; the food-safety hazard object model (HACCP/PCP plans, food PRPs, food-law frameworks) defines this Type | Replace food-safety subject matter with generic industrial quality → QMS |
| Store Task Management / ops execution (§05.11/§26) | execution layer without program | The Crunchtime pole carries food-safety checklists/audits/temperature on a task-execution core without plan building, CAPA workflow, document control or management review | Remove the task/ops core and keep the program machinery → FSMS; remove the program machinery → ops execution |
| EHS platforms (§21) | person/environment safety vs product safety | EHS protects workers/environment; FSMS protects the food; hygiene programs (sanitation) can touch both but the record frames differ | Change the subject from food hazards to workplace hazards → EHS |

Boundary verdict: the leaf is a legitimate distinct Type — the standing program machinery with the hazard-control plan at its center. The one genuinely unresolved seam is vs the unprocessed haccp-management sibling; recorded for joint review rather than resolved unilaterally.

## Historical / Market-Sample Check

Paper-era analog program (1980s–2000s HACCP practice; pre-software): HACCP plan binder (hazard analysis worksheets, CCP determination, critical limits), monitoring log sheets (cooking/cooling temperatures, sanitizer concentrations, receiving checks), corrective action log, verification signatures and review notes, supplier approval files, SOP manual, internal audit checklists, inspection-ready binder. Satisfies all four L0 legs at analog level. Regional/regime variants: UK Safer Food Better Business-style packs (simplified "safe methods" + diary + opening/closing checks), US Food Code HACCP plans, EU food-law hygiene packages — same machinery, different framework dressing. Spreadsheet-era digitization (Excel logs + Word SOPs + shared drives) satisfies legs 1–2 partially and 3–4 weakly — the market itself pitches "replace paper binders/spreadsheets" (SafetyChain "No Binders"; FoodDocs paper-vs-digital section), confirming the analog core and the digitization of records/scheduling/escalation as the modern mass.

Therefore: cloud, mobile apps, AI setup, IoT sensors, multi-site dashboards, GFSI framework catalogs, supplier portals, and BI are all standard-NOT-definitional. Older, regional, platform-native implementations fit the definition; the definition does not name any specific standard, scheme, or inspection regime.

## Uncertainties

1. **haccp-management seam** — the most consequential unresolved boundary (see Boundary Findings). If that pass finds HACCP-only products that also carry PRP/doc/audit machinery, alias consolidation may be warranted; if thin HACCP-plan-only tools dominate, keep-both holds with the seam as stated.
2. **Help-center depth** — research relied on vendor marketing/product pages; module-by-plan-tier lists, workflow states (e.g., CAPA statuses), and permission models were not verified from operational documentation. Assertion strength kept at structure level; no precise counts, defaults, or state machines asserted.
3. **Supplier-quality boundary** — Safefood markets supplier management as a near-separate solution line; the relationship to Supplier Management Platform (§10) / Supplier Risk Management (§11) types was noted but not resolved here.
4. **Enterprise "food safety" governance layer** — corporate multi-site program standardization (Safefood Enterprise page, not fetched; Crunchtime above-store oversight) may be a variant or a thin separate Type; held as variant this pass.
5. **Supply-chain quality-data pole** (produce/fresh quality inspection platforms, e.g. iFoodDS-class) unsampled — potentially a variant where supplier/customer quality data dominates; left for any future pass.

## Final Synthesis

A Food Safety Management application is the food business's standing program system of record: it holds the operation's hazard-control program — food-safety/HACCP-class control plans plus prerequisite programs — as structured living records; it drives the recurring monitoring that produces timestamped, attributed evidence that the controls work; it converts every out-of-spec, missed or nonconforming result into a corrective action that must be completed, verified and closed; and it keeps the whole record chain reviewable and audit-ready for inspectors, certification auditors and customers, with verification (reviews, internal audits, management review) sitting structurally above daily monitoring. Around that core, mature products add document control, supplier quality machinery, framework/certification packaging, traceability and recall modules, sensor integrations, multi-site dashboards and mobile execution. The Type is one market realized in poles — certification-suite FSMS for manufacturers, plant-floor FSQA execution, app-led SMB digital FSMS, and ops-execution platforms where food safety rides a task core (the boundary pole). Its program machinery is what the processed siblings pre-hung: the recall pass owns the episodic event, the cold-chain pass owns the physical estate, the ERP owns the operational record; the FSMS owns the standing program. The seam vs the unprocessed haccp-management sibling — HACCP plan machinery vs the broader management-system layer — is recorded for joint review.
