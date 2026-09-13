# Research Notes — HACCP Management

## Research Goal

Understand "HACCP Management" (§20 Agriculture, Food & Natural Resources) as an Application Type: what objects a HACCP-centric product holds, who operates it, what the daily loop looks like, what rules and states matter, and where the boundary sits — especially against the processed siblings **food-safety-management** (§20, 2026-09-08, JOINT REVIEW RECOMMENDED with this leaf), **food-cold-chain-management** (§20, 2026-09-08, JOINT REVIEW RECOMMENDED with this leaf), **food-recall-management** (§20, 2026-09-08), **food-traceability-platform** (§20, processed 2026-09-08), and neighboring machinery types (Manufacturing QMS / CAPA, Store Task Management, Food Manufacturing ERP).

Two sibling passes pre-hung seams for this leaf:

- **food-safety-management**: "both Types center the HACCP machinery (hazard analysis → CCPs → critical limits → monitoring → corrective action → verification → records); seam held this pass = the management-system layer — Food Safety Management additionally carries prerequisite programs beyond the HACCP plan, supplier management, document control, management review, and multi-framework certification machinery (the ISO 22000-style management system as a whole)." **Test handed to this pass:** "remove the management-system layer → HACCP plan machinery remains (haccp-management territory); remove the hazard-control plan while keeping PRP/audit/supplier/doc machinery → generic QMS." Its Uncertainty #1: "If that pass finds HACCP-only products that also carry PRP/doc/audit machinery, alias consolidation may be warranted; if thin HACCP-plan-only tools dominate, keep-both holds with the seam as stated."
- **food-cold-chain-management**: "temperature is the dominant CCP family and temperature-monitoring products market themselves as HACCP-compliance tools — seam held this pass = program machinery (hazard analysis, CCP determination across all hazards, verification, audits) vs the physical temperature-controlled estate + excursion response loop." **Test handed to this pass:** "remove the program machinery — if the estate/requirement/excursion/record loop remains, it was this Type [cold-chain]."

This pass's central job is the joint review: does a real market population of HACCP-centric products exist that is distinct from the full FSMS, or is haccp-management an alias/variant of food-safety-management?

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is software centered on the **HACCP machinery itself** — the Codex/NACMCF-class methodology: preliminary steps (team, product description, intended use, flow diagram) plus the seven principles (hazard analysis → determine CCPs → establish critical limits → establish monitoring → establish corrective actions → establish verification → record-keeping). The application holds the HACCP plan as a living record, drives CCP monitoring at the point of work, turns limit breaches into corrective actions, and keeps the plan verified and revised.
- Suspected nearest neighbors: Food Safety Management (alias risk — the joint review), Food Cold Chain Management (temperature CCPs), Food Recall Management, Food Traceability Platform, Food Manufacturing ERP, Manufacturing QMS / CAPA, Store Task Management / ops execution.
- Suspected boundary test: remove the management-system layer (PRPs-as-programs, supplier, doc control, mgmt review, certification) → HACCP machinery remains; remove the HACCP plan machinery → cold-chain estate / recall event / lot ledger each remain.

## Research Questions

1. What does a HACCP-centric product hold as objects? (study, flow diagram, hazards, CCPs, critical limits, monitoring schedules, corrective actions, verification, plan revisions…)
2. What is the plan-building workflow (the Codex-class study steps) as realized in software?
3. What is the daily monitoring loop at CCPs, and how does it differ from generic checklist execution?
4. Does a market population of HACCP-only tools exist without the FSMS management-system layer? (the joint-review question)
5. What is the seam vs Food Cold Chain Management (temperature CCPs vs the physical estate)?
6. What roles exist (HACCP team / food safety manager / site monitors / corporate / auditors)?
7. What is the analog ancestor, and would a paper-era HACCP program satisfy the invariants?
8. What is era machinery vs defining structure (AI plan generation, sensors, cloud, dashboards)?

## Representative Products

| Product | Vendor | Pole | Why chosen | Depth reached |
|---|---|---|---|---|
| HACCP Builder | Costello (Red Wing, MN) | Dedicated HACCP-plan-first platform for small/mid food manufacturers, processors, co-packers, retail | The plan-first pole; a product *named* for HACCP where the HACCP plan is the spine (Plus + LogiSafe lines, HACCP Cloud daily compliance) | Root page (positioning, product lines, features, benefits, testimonials) |
| FoodDocs | FoodDocs | App-led "Digital HACCP Management System" for foodservice/retail/care (US/UK/EU) | The SMB app-led pole with an explicit HACCP product line and an unusually explicit enumeration of the HACCP system's components | Dedicated HACCP page (products, mechanics, FAQ block incl. HACCP components, review triggers, compliance disclaimers) |
| ComplianceMate (Ladle) | Ladle | Execution pole: automated HACCP workflow checklists + temperature sensors for foodservice/retail/c-store chains | The chain-ops execution pole; temperature-CCP machinery straddling the cold-chain seam (evidence for that boundary too) | Ladle root + ComplianceMate product block (via compliancemate.com redirect) |
| Ideagen Safefood 360° | Ideagen | Enterprise FSMS suite in which HACCP/PCP is a named module family | The suite pole; the joint-review evidence — shows what the HACCP *module* holds when the management-system layer ships beside it | HACCP, PCP & Food Safety Plans module page + full module catalog |

Selection rationale: market representation (dedicated HACCP tool / SMB app / chain execution / enterprise suite), different product philosophies (plan-first builder vs app-led loop vs execution-first vs suite-module), different customer tiers (small manufacturer → SMB multi-site → franchise/c-store chains → enterprise GFSI manufacturer). Two poles overlap deliberately with sibling passes' samples (Safefood 360° with food-safety-management; ComplianceMate with food-cold-chain-management) — re-sampled from this Type's angle for the joint review.

## Sources

Evidence layer A (official vendor pages, fetched 2026-09-08):

- HACCP Builder — https://haccpbuilder.com/ (root: positioning, product lines, services, features list, testimonials)
- FoodDocs — https://www.fooddocs.com/haccp (dedicated HACCP page: product split, mechanics, FAQ incl. HACCP components and review triggers; https://www.fooddocs.com/haccp-plan-software 404'd)
- Ladle / ComplianceMate — https://www.compliancemate.com/ (redirects to ladle.com root; ComplianceMate product block) 
- Ideagen Safefood 360° — https://safefood360.com/product/modules/haccp-pcp-food-safety-plans/ (HACCP module page); https://safefood360.com/product/modules/ (module catalog)

Not reachable: https://help.safefood360.com/ (transport error, abandoned after one failure); https://www.fda.gov/food/haccp and the HACCP principles URL (404 twice — bot-wall/restructure suspected; abandoned per network rule). PrimeroEdge (school-nutrition candidate) root page showed no HACCP-centric product — dropped rather than asserted from memory.

**Source-access limitation:** no primary regulatory text (Codex, NACMCF, FDA/FSIS) was fetched this pass. The HACCP methodology is described qualitatively from vendor-corroborated enumerations (FoodDocs' FAQ enumerates the seven HACCP components; Safefood 360° states "fully aligned with Codex principles" and USDA/Codex plan formats; HACCP Builder cites the "Process Approach" with "default USDA/FDA data"). No numeric regulatory claims are asserted. Vendor marketing pages (not help-center operational docs) carry most evidence — assertions are kept at the structural level; no precise defaults, plan-tier feature lists, or workflow state machines are claimed. One claim in the final document draws on the paired sibling pass: the "software supports but cannot guarantee compliance" disclaimer is evidenced directly here for FoodDocs and was recorded for Safefood 360° in research/food-safety-management.md — hence "multiple vendors state this."

## Product Observations

### HACCP Builder (Costello) — evidence layer A

Positioning: "The Food Operations Platform for Small & Mid-Sized Food Manufacturers"; "HACCP Builder brings your HACCP plan, real-time track & trace, inventory, and daily production logging into one system"; pitch to "a smaller operation just getting started with a HACCP plan."

Plan machinery (the strongest plan-first evidence in the sample):

- "HACCP Builder streamlines your HACCP process by **customizing flow charts, Hazard Analysis Tables, and HACCP Plan Tables**."
- "HACCP Builder's system **automatically assigns all CCP's, CP's, biological, chemical, and physical hazards**." (hazard classes: biological/chemical/physical; CCP and CP designations)
- Retail line: "Built on the **Process Approach**, offers **default USDA/FDA data**… supports **Menu/Recipe HACCP** for the restaurant and retail industry." (the FDA Food Code process approach to HACCP as built-in methodology dressing)
- "HACCP Cloud — Your HACCP plan, hazard analysis, and **daily records** in one system – always current, always audit-ready."

Daily loop:

- "HACCP Daily Compliance" cloud product; features list: "Add A Check List / Log", "Customizable Logs", "Customizable Processes", "Alerts & Notifications", "Tap, Talk and Log" (voice/mobile entry), "Multiple Access Points".
- "**corrective actions that log themselves** – less paperwork, more time on the floor."
- "HACCP Builder's corporate center allows for monitoring all units/facilities within an organization… enables the organization to take corrective actions in real time 24/7/365."

Verification/revision evidence: "Every **SOP change tracked automatically – who, when, and what changed**" (document-change audit trail); "always current, always audit-ready."

Adjacent modules riding the HACCP core: LogiSafe track & trace (FSMA 204, "cut recalls to minutes"), inventory, production logging, recipe/mix manager, facility plans. Product-line split: **Plus** (small retail/direct-to-consumer) vs **LogiSafe** (processors/warehouse/distribution needing track & trace).

Reading: a HACCP plan is the spine — flow charts, hazard-analysis tables, plan tables, auto-assigned CCPs/CPs — with daily compliance records and corrective actions wrapped around it, and traceability/inventory as adjacent modules. No supplier management, no audit-program machinery, no certification-framework mapping evidenced — the management-system layer is absent. This is the joint-review's decisive pole: a real product whose entire center is the HACCP plan machinery without the FSMS layer.

### FoodDocs — evidence layer A (dedicated HACCP page)

Positioning: "HACCP Food Safety Software & Digital HACCP Management System. Build, manage, and monitor your HACCP compliance in one smart platform. Create your HACCP plan, monitor critical control points, manage food safety records, and gain real-time visibility across all locations."

Product split (three named pillars):

- **HACCP Plan Software**: "Get your complete HACCP plan in under 1 hour" — automated hazard analysis, **CCP identification**, flow chart generation, SOP and PRP creation, fully downloadable HACCP documentation, editable anytime. AI-powered setup: "Answer a few questions and automatically get your essential HACCP documents (e.g., Hazard Analysis, CCPs, PRPs, flow chart, SOPs, and more)."
- **HACCP Monitoring System**: "**Turn your HACCP plan into action**" — monitor critical control points; temperatures, cleaning tasks, and other food safety checks; smart mobile notifications; real-time dashboard; **completed task verification**; sensor integrations.
- Traceability Software (ingredient tracking, batch traceability, recall-ready search) — adjacent module.

The vendor's own enumeration of the HACCP system (FAQ: "What is the monitoring system for HACCP?"): "a complete and comprehensive digital HACCP plan with the following components: **Hazard analysis, Critical control points, Critical limits, Monitoring procedures, Corrective action plan, Verification procedures, Record-keeping**" — plus PRP documents (waste management, pest control audit, laboratory tests, allergen and consumer information, cleaning and disinfection). This is the canonical seven-principle structure listed by a vendor as what the product's plan holds.

Relationship to FSMS (the joint-review question, answered by the vendor itself): "**HACCP is the core methodology used within a food safety management system.**" — the methodology layer is named as distinct from the management system around it.

Verification/revision evidence (FAQ: "Does HACCP expire?"): "A HACCP system is a continuously changing and improving system… **at least once a year, your HACCP team must schedule a HACCP internal audit and review**." Named revision triggers: after a major inspection or internal audit; after a recall or food-safety incident; when a new production process, layout, or product formulation is introduced; for compliance with new laws. The **HACCP team** is named as the owning body.

Execution surfaces: mobile app with smart notifications and "educative instructions"; sensor integrations (smart fridges, temperature sensors) auto-sync to temperature monitoring checks; "timestamped proof of compliance" for health inspections; real-time multi-location overview; AI reports. Paper-vs-digital framing: paper HACCP → "outdated documents, manual logs, no alerts, hard to audit, risk of damaged or lost records."

Compliance posture: "the software supports compliance, it cannot guarantee regulatory compliance… each business operates in a unique context"; "not a food safety consultancy" — the HACCP plan is generated from "data from states' regulations and data/feedback from companies similar to yours," machine-learning refined, but the operator owns adaptation. PDF download of the plan gated to paid annual plans (trial creates/edits but cannot export).

Reading: the full HACCP loop in miniature — plan (AI-assisted study artifacts) → monitoring of CCPs → verification of completed tasks → team review/revision on named triggers — with traceability and PRP documents adjacent. Same absence of supplier machinery/audit programs/certification mapping as HACCP Builder.

### ComplianceMate (Ladle) — evidence layer A (execution pole)

Context: compliancemate.com redirects to Ladle; ComplianceMate is one Ladle product beside MeazureUp/AuditApp (site audits) and Storewise (grocer pricing).

Positioning: "ComplianceMate offers advanced tools like **automated HACCP workflows** and real-time temperature monitoring." Feature checkmarks: "**Automated HACCP Workflow Checklists**", "**Temperature Sensor Monitoring with Real Time Alerting**", "Data Monitoring and Reporting".

Solutions lines: Operational Food Safety Checklists; Continuous Temperature Monitoring; Site Assessments. Industries: convenience stores, restaurants & food service, grocery, healthcare, hospitality, education, travel.

Reading: HACCP appears as *plan execution* — HACCP-derived workflow checklists on sensor- and probe-equipped sites, with alerting and reporting. Plan building is not evidenced on the fetched page. This pole shows the temperature-CCP execution half (straddling the cold-chain seam: its Continuous Temperature Monitoring line is the estate machinery; its HACCP workflow checklists are the program-execution half) and marks the boundary against generic checklist execution: the checklists are *HACCP workflows*, i.e., plan-derived, not free-form task lists.

### Ideagen Safefood 360° — evidence layer A (suite pole; the joint-review seam)

HACCP module page ("HACCP, PCP & Food Safety Plans"):

- "HACCP is often the corner stone of a food safety management system or program. Creating all your HACCP and PCP studies requires extensive resources, education and time, and **maintaining the plans takes a lot of time**." (maintenance burden is the pitch — the plan is a maintained object)
- "The module is **fully aligned with Codex principles**."
- Features: "HACCP study background details"; "**Draw HACCP flow diagrams**" (built-in flowcharting, "no need for external tools such as Microsoft Visio or CAD… automatically embedded in your ready HACCP plan"); "Process step descriptions"; "**Hazard analysis**"; "One-click HACCP / PCP plan printed in **USDA or Codex format**"; "Built-in fully customizable hazard database."
- Detailed workflow: "Driven by the built-in hazard database, conduct robust and specific **hazard identification** followed by **risk assessment** using the embedded risk model and calculator. **CCP determination** is then conducted on significant hazards using the **intelligent CCP decision tree**. Just complete the **CCP monitoring plan** and you're done."
- Living plan: "As you work your way through the hazard analysis for each step the system will automatically **compile your HACCP Summary Plan**. As you make changes and revisions to your HACCP study, **the plan will also update**."

Module catalog (36 modules, vendor's own tabs Documents / HACCP / Management / Monitoring / PRPs / Supplier Management / Utilities): the HACCP tab holds **HACCP, PCP & Food Safety Plans** and **Hazard Database**; the Management tab holds Corrective Action, Auditing, Management Review, Non conformance, Recall & Withdrawal, Quality Management; PRPs tab holds Cleaning, Maintenance, Pest Control, Glass & Plastic, Medical Screening, Training, etc.; plus Monitoring, Supplier Management/Portal, Document Control, Traceability.

Reading: the vendor's own architecture realizes the seam this pass was handed — the **HACCP module family** (plan study + hazard database) sits *beside* the **Management System family** (CAPA/nonconformance/audit/management review) and the **PRP family**. The HACCP study workflow (background → flow diagram → step descriptions → hazard analysis via hazard DB + risk model → CCP decision tree → monitoring plan → compiled plan that updates with revisions) is the richest plan-building evidence in the sample. The management-system layer is present but *separable* — it is a different module family. The plan-as-living-object ("maintaining the plans takes a lot of time"; plan updates with revisions) corroborates the revision loop.

## Cross-product Comparison

| Dimension | HACCP Builder | FoodDocs | ComplianceMate (Ladle) | Safefood 360° (HACCP module) |
|---|---|---|---|---|
| Center of gravity | HACCP plan + daily compliance records (plan-first) | digital HACCP system: plan → monitoring loop (app-led) | HACCP workflow *execution* (checklists + sensors) | HACCP/PCP study module inside a 36-module FSMS suite |
| Plan building | flow charts, Hazard Analysis Tables, HACCP Plan Tables; auto-assigned CCPs/CPs/hazards; process-approach defaults (USDA/FDA data); Menu/Recipe HACCP | AI-generated plan: hazard analysis, CCPs, critical limits, flow chart, SOPs, PRPs; editable, downloadable PDF | not evidenced | Codex-aligned study: background, flow-diagram drawing, step descriptions, hazard DB + risk model/calculator, CCP decision tree, monitoring plan; one-click compiled plan (USDA/Codex format) |
| Daily monitoring | "HACCP Daily Compliance"; checklists/logs; Tap-Talk-and-Log; alerts | CCP monitoring: temperatures, cleaning, other checks; mobile notifications; sensor sync; logbook | automated HACCP workflow checklists; temp sensors with real-time alerting; reporting | Monitoring module + IoT alerts (suite-level) |
| Deviation → corrective action | "corrective actions that log themselves"; real-time from corporate center | corrective action plan as named HACCP component; corrective actions on tasks | alerting on excursions (deep response loop not evidenced) | Corrective Action module (separate Management family) |
| Verification / review | SOP change tracking (who/when/what); audit-ready | "completed task verification" named feature; HACCP team internal audit & review at least yearly; named revision triggers | (hierarchy/oversight reporting) | Auditing + Management Review modules (separate family) |
| Plan currency | "always current"; automatic plan tables | "editable anytime"; does-not-expire revision FAQ | — | plan auto-updates with study revisions; "maintaining the plans takes a lot of time" |
| Output / audience | audit-ready; recalls in minutes; FSMA 204 line | downloadable HACCP plan (paid tier); health inspections; EHO ratings | chain reporting | GFSI/BRCGS/SQF/FSSC/IFS packaging (suite-level) |
| Management-system layer (supplier, doc control, audit programs, certification) | **absent** | **absent** (PRP documents only) | **absent** | **present** (separate module families) |
| Primary audience | small/mid manufacturers, processors, co-packers, retail | foodservice/retail/care SMBs, multi-site | c-store/restaurant/grocery chains | food manufacturers (GFSI) |

**Reading:** all four realize the HACCP machinery — a structured plan holding hazard analysis → CCPs → critical limits → monitoring requirements → corrective actions → verification — with daily monitoring execution wrapped around it. Three of four (HACCP Builder, FoodDocs, ComplianceMate) carry **no** management-system layer and are viable products on the HACCP machinery alone; the fourth ships that layer as separate module families. The joint-review test resolves: removing the management-system layer leaves a real product population — keep-both holds with the seam as pre-hung.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

A HACCP Management application is the food operation's **HACCP machinery system of record**. Four jointly-held structures; remove any one and the product stops being this Type:

1. **The HACCP plan as the unit of record** — the operation's hazard analysis and critical-control-point determination held as one structured, living plan: the process flow (flow diagram, process steps), the identified hazards (biological/chemical/physical, commonly allergen), the designated critical control points (with CP/oPRP-class control designations as common refinements), the **critical limits** set on those points, the monitoring requirements (what/how often/who), the corrective-action provisions, and the verification procedures — the Codex-class plan structure (PCP/food-safety-plan equivalents realized in the same object). Remove → a generic checklist/monitoring tool with no plan, or a document library.
2. **CCP monitoring at the point of work** — the recurring, attributed recording of control measurements against the plan's critical limits (temperature/time/check readings), turning the plan into daily executed work. Remove → a static plan document generator/binder (authoring-only tool).
3. **The deviation → corrective-action loop at the control points** — an out-of-limit result or a missed check triggers a documented, tracked response tied to the affected product/process. Remove → passive logging.
4. **Verification and revision of the plan** — review of monitoring records above the recording layer (verification of completed checks), and the plan kept current: revised and revalidated as the operation changes and after audits/incidents — the HACCP system is maintained, not filed. Remove → authoring tool + logbook with no management loop.

Jointly-held is load-bearing: 1 alone = a plan generator/binder; 2 without 1 = checklist execution / temperature logging (ops-execution or cold-chain territory); 3 without 1+2 = a generic corrective-action tool; 4 without 1–3 = an audit-reporting shell; 1+2 without 3 = a logbook; 1+3 without 2 = a plan never executed daily.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Plan-authoring aids: hazard databases (curated, customizable), CCP decision trees, embedded risk models/calculators, flow-diagram drawing tools, template/default content (USDA/FDA process-approach data; regulatory-data-derived AI generation)
- Mobile execution with instructions/notifications; probe and sensor integrations feeding monitoring records automatically
- Printable/exportable plan documents and record reports (the plan compiled to a PDF/document; records exportable for inspectors/auditors)
- Deviation alerts and escalation; dashboards; multi-site/corporate oversight ("corporate center", real-time multi-location views)
- Version/change tracking of the plan and associated SOP documents
- Adjacent modules riding the HACCP core: traceability/track & trace, recall readiness, inventory/production logging, recipe/menu management, training/instructions

### L2 — Variant / Optional Structure

- Methodology dressing: Codex-aligned HACCP (international/manufacturing), USDA/FDA **Process Approach** (retail/foodservice, menu/recipe HACCP), PCP/HARPC-class preventive-control plans (FSMA-era), regional hygiene-law equivalents
- Segment: manufacturers/processors (plan depth, hazard DBs) vs foodservice/retail/care (app-led simplicity, hygiene-rating framing) vs institutional settings
- Scale: single-site SMB vs multi-site chains with corporate oversight vs enterprise
- Suite posture: HACCP as the whole product (dedicated tools) vs one module family inside an FSMS suite
- Sensor/hardware coupling depth (continuous monitoring vs manual probe entry)
- PRP document coverage depth (some tools carry PRP *documents* without the FSMS program machinery)

### L3 — Vendor-specific (research notes only)

- HACCP Builder: Plus vs LogiSafe product-line split; FSMA 204 deadline positioning; "Tap, Talk and Log" voice entry; auto-assignment of CCPs/CPs/hazards; 24/7/365 corporate center; default USDA/FDA process-approach data
- FoodDocs: "15 minutes setup / 1 hour plan / 500x faster / €20,466 yearly" claims; ML refined from prior users' data; PDF export gated to paid annual plans; 30,000+ users claim; AWS Central-Europe deployment; 14-day trial mechanics
- ComplianceMate/Ladle: Ladle umbrella (MeazureUp, Storewise, TrackAssure); real-time alerting; product-line split between CTM and checklists
- Safefood 360°: "intelligent CCP decision tree"; embedded risk model/calculator; one-click USDA/Codex plan formats; 36-module catalog taxonomy; Ideagen branding

## Rejected Findings

- **"HACCP software = temperature monitoring"** — rejected as definitional. Temperature is one CCP family (the dominant one, per the cold-chain pass); the plan machinery spans all hazard classes (HACCP Builder auto-assigns biological/chemical/physical hazards; Safefood's hazard DB covers biological/physical/chemical/allergen). The cold-chain Type owns the physical estate.
- **"HACCP Management = Food Safety Management" (alias)** — rejected on current evidence. Three of four sampled products are HACCP-centric *without* the management-system layer and are viable market products; the suite vendor ships the two layers as distinct module families; and one vendor itself states HACCP is "the core methodology used within a food safety management system" — methodology layer ≠ management-system layer. Keep-both ratified with the pre-hung seam (consolidation candidate noted for taxonomy maintainers if the dedicated-tool population converges into suites).
- **"HACCP software = plan document generator"** — rejected. Authoring alone is not management: the daily monitoring, corrective-action, and verification/revision machinery is what makes the Type (authoring-only is a leg-1-only failure).
- **"HACCP requires GFSI/certification machinery"** — rejected. Foodservice/retail poles exist below certification (FoodDocs EHO framing; HACCP Builder small-operation framing; ComplianceMate chain ops).
- **"AI plan generation is definitional"** — rejected. Era machinery; the paper plan and spreadsheet-era tools satisfy the core.

## Boundary Findings

| Neighbor | Relationship | Distinction | Test |
|---|---|---|---|
| **Food Safety Management (§20, processed)** | broader sibling; JOINT REVIEW RESOLVED this pass | Both center the HACCP machinery. The seam is the **management-system layer**: FSMS additionally carries prerequisite programs as managed programs, supplier quality machinery, document control, management review/internal-audit programs, and multi-framework certification packaging. HACCP Management centers the HACCP plan machinery itself: study/plan of record → CCP monitoring → corrective action → verification & revision. Safefood 360° ships both as separate module families; HACCP Builder / FoodDocs / ComplianceMate are viable on the HACCP machinery alone. | Remove the management-system layer → HACCP machinery remains (this Type). Remove the HACCP plan machinery while keeping PRP/audit/supplier/doc machinery → generic QMS. |
| **Food Cold Chain Management (§20, processed)** | estate vs program (JOINT REVIEW RESOLVED this pass) | Temperature is the dominant CCP family and sensor products market HACCP compliance, but the cold-chain Type holds the physical temperature estate + excursion-response loop; this Type holds the plan machinery across all hazards (hazard analysis, CCP determination, verification, revision). ComplianceMate straddles: its continuous-temperature line is estate machinery; its HACCP workflow checklists are plan-execution machinery. | Remove the plan machinery → the estate/requirement/excursion/record loop remains (cold chain). Remove the estate/sensor machinery → the plan machinery remains (this Type). |
| Food Recall Management (§20, processed) | prepared-for vs event | The HACCP program prepares for incidents; the recall event workflow (scope, notification, response, closure) is the dedicated Type. HACCP Builder sells recall speed via its track & trace module — adjacent machinery. | Remove the standing plan machinery → the recall event workflow remains |
| Food Traceability Platform (§20, processed) | program vs ledger | The cross-partner lot-movement ledger is that Type's spine; HACCP products may bundle traceability modules (HACCP Builder LogiSafe, FoodDocs) but the plan machinery is independent. | Remove the plan machinery → the lot ledger remains |
| Food Manufacturing ERP (§20, processed) | program vs operations | ERP carries production/inventory/lot operations; HACCP Builder bundles inventory/production logging around its HACCP core, but the plan machinery defines this Type. | Remove the business back office → the HACCP machinery remains |
| Manufacturing QMS / CAPA Management (§16) | shared machinery, different subject | Deviations/CAPA/audits are generic quality machinery; the food-hazard object model (flow diagram, biological/chemical/physical/allergen hazards, CCPs, critical limits) defines this Type. | Replace the food-hazard model with generic industrial quality → QMS |
| Store Task Management / ops execution (§05.11/§26) | execution layer | Checklists without the plan of record are task execution; this Type's checklists are plan-derived (HACCP workflows with critical limits). A generic checklist tool carrying food-safety templates sits on this seam. | Remove the HACCP plan machinery/CCP semantics → generic task execution |
| Prerequisite programs / hygiene checklists | content vs machinery | PRP *documents* may live in HACCP tools (FoodDocs PRP documents; Safefood PRP family); the FSMS manages PRPs as programs. | Remove the HACCP plan → PRP hygiene checklists are FSMS/ops territory |

## Historical / Market-Sample Check

Paper-era analog HACCP program (1970s–2000s practice, pre-cloud): HACCP plan binder with flow diagram sheets, hazard analysis worksheets, CCP determination worksheets (decision trees on paper), critical-limit tables, monitoring log sheets filled at the CCPs (cook/cool/hold temperatures, sanitizer concentrations), corrective-action log, verification signatures and review notes, revision history when process or formulation changed. Satisfies all four L0 legs at analog level — the machinery predates software; the software digitizes scheduling, attribution, alerting, and the plan-revision loop.

Regime/regional variants across eras: Codex-aligned plans (international), USDA/FDA process-approach plans (US retail/foodservice — HACCP Builder's built-in defaults), FSMA-era preventive-control plans (PCP/HARPC descendants), UK hygiene-law HACCP-based procedures (FoodDocs' framing), FSMS-suite HACCP modules (Safefood). Early desktop HACCP plan builders (late-1990s–2000s, USDA process-approach era) satisfy legs 1/3/4 with paper monitoring; spreadsheet-era digitization (Excel logs + Word plans) partially satisfies leg 2. All fit the definition; the definition names no cloud, mobile, AI, sensor, or framework machinery.

Therefore: AI plan generation, cloud, mobile apps, sensor fleets, multi-site dashboards, document-control depth, and certification packaging are all standard-NOT-definitional.

## Uncertainties

1. **ComplianceMate plan-building depth** — the Ladle product page evidences HACCP workflow checklists + sensors but not plan authoring; help-center documentation was not fetched. Held as the execution-pole boundary evidence, not as support for the plan-building workflow.
2. **Help-center depth for all vendors** — research relied on product/marketing pages; workflow state machines (corrective-action statuses), permission models, and plan-tier gating beyond the one evidenced instance (FoodDocs PDF gating) were not verified. Assertions kept structural.
3. **Primary regulatory sources** — Codex/NACMCF/FDA text not fetched (fda.gov 404s); the seven-component HACCP structure is corroborated by vendor enumerations (FoodDocs FAQ; Safefood Codex-alignment claim) rather than primary text. No numeric regulatory claims made.
4. **Market convergence direction** — whether dedicated HACCP tools persist as a distinct population or are absorbed into FSMS suites; consolidation candidate recorded for taxonomy maintainers (keep-both ratified for now on current evidence).
5. **oPRP/CP designation vocabulary** — HACCP Builder evidences CP designations and Safefood evidences PCPs; the intermediate-control-point taxonomy (oPRP, CP, PCP) varies by regime and vendor; held as L2 methodology dressing, not normalized.

## Final Synthesis

A HACCP Management application is the food operation's HACCP-machinery system of record: it holds the HACCP plan — process flow, hazard analysis, designated critical control points, critical limits, monitoring requirements, corrective-action provisions, verification procedures — as one structured, living record; it drives the recurring monitoring of those control points at the point of work as attributed daily records; it turns every out-of-limit or missed result into a tracked corrective action tied to the affected product or process; and it keeps the plan verified and revised as the operation changes, so the HACCP system stays current and inspectable. Around that core, mature products add plan-authoring aids (hazard databases, decision trees, AI generation), mobile execution with notifications and sensor integrations, printable plan documents and record exports, dashboards and corporate oversight, and adjacent modules (traceability, recall readiness, inventory). The market realizes one Type in poles — dedicated plan-first tools for small manufacturers, app-led digital HACCP for foodservice/retail/care, plan-execution checklists with sensors for chains, and the HACCP module family inside enterprise FSMS suites. The joint review with Food Safety Management is discharged: keep-both holds, the seam being the management-system layer (PRPs as programs, supplier, document control, audit/management-review machinery, certification packaging), which the FSMS pass pre-hung and this pass corroborates from three independent HACCP-only products plus one suite's separate module families.
