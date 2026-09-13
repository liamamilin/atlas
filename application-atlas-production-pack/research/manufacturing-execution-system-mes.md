# Research Notes — Manufacturing Execution System / MES

## Research Goal

Determine what a Manufacturing Execution System (MES) is as a distinct Application Type: what core objects and structures define it, who uses it, how production work actually flows through it, and where its boundaries lie against the dense cluster of neighboring manufacturing leaves (Manufacturing ERP, Production Planning / APS, Factory Operations Management, Shop Floor Management, Manufacturing Traceability, Manufacturing QMS, OEE Management Platform, SCADA / HMI / Industrial Historian, Industrial IoT Platform).

This leaf carries a joint-review obligation recorded by the already-processed sibling leaf `factory-operations-management` (2026-09-08), which drew the seam from the MOM side: execution enforcement + as-built record = MES; live operations management (state + event-response + performance record) = Factory Operations Management. This pass must draw the same seam from the MES side and record agreement or disagreement.

## Initial Boundary (working hypothesis, pre-research)

- Core use: executing released production orders on the factory floor — taking the order from ERP/planning, running it operation by operation with the defined process, and producing the as-built record of what was actually made (traceability/genealogy).
- Likely users: floor operators, line supervisors, production/quality engineers, plant operations management.
- Likely nearest neighbors: Manufacturing ERP (owns orders/BOM/inventory at business grain), Production Planning/APS (owns the forward plan), Factory Operations Management (live operations management), SCADA/HMI (machine control), Manufacturing Traceability (genealogy without execution), Manufacturing QMS (quality system of record).
- Unknowns: is "process enforcement" definitional or a depth variant (market-label noise: some self-labeled MES are monitoring/job-tracking centered)? Does the definition survive the paper-traveler era? How much scheduling/dispatching belongs to MES vs APS?

## Research Questions

1. What objects does an MES actually hold (orders, operations/steps, routings/recipes, units/serials/lots, resources, quality results, as-built records)?
2. Which functions are definitional vs bundled (scheduling, quality, maintenance, inventory, OEE, work instructions, machine connectivity)?
3. What is the execution loop (release → dispatch → step execution → data collection → completion → reporting back)?
4. What exactly does "as-built record / traceability / genealogy" mean in product terms, and at what grain (unit/serial/lot vs shift/order aggregate)?
5. Where are the seams vs ERP (order ownership), vs SCADA/HMI (control), vs MOM/FOM (live operations), vs traceability/QMS (record-keeping)?
6. Would the definition survive the paper-traveler factory, the 1990s MES generation, and regional vendors (historical/market-sample check)?

## Representative Products

Chosen for market representativeness, documentation accessibility, different product philosophies, and different customer tiers. A first candidate list (iBase-t Solumina, 42Q, Plex, Körber PAS-X) was reduced by fetch failures — see Sources.

| Product | Pole | Tier / industries | Evidence quality |
|---|---|---|---|
| Siemens Opcenter Execution | enterprise MOM suite with MES execution engine; industry-packaged families (Discrete, Process, Electronics, Medical Device, Pharma, Semiconductor) | large enterprise; discrete + process + regulated | good (official product pages fetched fresh this pass + portfolio/MES solution pages from sibling pass 2026-09-08) |
| AVEVA Manufacturing Execution System | model-driven / composable MES over industrial-software estate (ex-Wonderware heritage); batch/repetitive consumer goods, food & bev, specialty chemicals | mid-market → enterprise | excellent (official product page + extensive official FAQ, fresh fetch) |
| Tulip | boundary witness, not an MES sample: composable no-code frontline operations platform that explicitly integrates with MES/ERP | mid-market → enterprise | excellent (official integration doc fetched fresh this pass; knowledge base from sibling pass) |
| L2L | boundary witness: connected operations platform whose FAQ addresses "replace our MES?" directly | mid-size → enterprise | good (official platform pages + FAQ from sibling pass) |
| MachineMetrics | boundary witness for market-label noise: self-labeled "Intelligent MES", monitoring/job-tracking-centered | SME discrete | medium (marketing-site only, sibling pass) |

Rejected / unreachable samples: iBase-t (403 ×2), 42Q (empty ×3 across two passes), Plex (transport error ×2), Körber PAS-X (timeout), DELMIA Apriso (thin content; deeper page 404), Epicor (404), Rockwell FactoryTalk ProductionCentre (404). Consequence: the regulated/aerospace specialist pole is under-sampled; the regulated leg is covered instead through Siemens' own pharma/medical-device families (eBR/eDHR productization).

## Sources

Fetched fresh this pass (2026-09-09):

- Siemens — Opcenter Execution (MES family page, incl. capability list and industry families): https://www.siemens.com/en-us/products/opcenter/execution/ (canonical: plm.sw.siemens.com/en-US/opcenter/execution/)
- AVEVA — Manufacturing Execution System product page with official FAQ (incl. MES vs ERP vs HMI/SCADA): https://www.aveva.com/en/products/manufacturing-execution-system/
- Tulip — "Plan an integration between Tulip and an MES or ERP" (system-of-record split): https://support.tulip.co/docs/plan-an-integration-between-tulip-and-an-mes-or-erp
- MESA — mesa.org now redirects to an ISA announcement that MESA International ceased operations 30 June 2026 and ISA assumed its content: https://www.mesa.org/

Carried from the sibling pass `factory-operations-management` (fetched 2026-09-08, documented in its research notes):

- Siemens — Opcenter portfolio page, MES solution page: siemens.com (MOM framing, "real-time software layer that links PLM to automation")
- Tulip — Knowledge Base (What is Tulip; Shop floor management; Machine attributes, downtime reasons, and states): support.tulip.co
- L2L — homepage, platform, Shop Floor Execution, Production Management pages incl. MES/ERP FAQ: l2l.com
- MachineMetrics — homepage ("Intelligent MES and machine monitoring"): machinemetrics.com

Not reachable: iBase-t, 42Q, Plex, Körber, DELMIA Apriso (operational docs), no ISA-95/MESA-11 standards text (MESA dissolved 2026-06; its content moved to ISA; no MES standards document was retrievable this pass). All layering claims below that would normally rest on ISA-95 are held on vendor statements only.

## Product Observations

### Siemens Opcenter Execution (suite pole, industry-packaged families)

Evidence layer A — official family page (fresh) + portfolio/MES pages (sibling pass):

- Family definition: "Opcenter Execution MES products optimize manufacturing operations, accurately reflecting design, engineering and process data in the production of actual finished products."
- Positioning: "Deliver the comprehensive digital twin to the factory floor... digitally linking enterprise systems with automated manufacturing equipment."
- Named MES capability clusters, verbatim highlights:
  - **Optimized sequencing** — "determining and implementing the most efficient production sequencing... synchronizes production processes across the supply chain to optimize production execution."
  - **Resource allocation and control** — "manage all relevant resources for manufacturing operations... manage and track the movement and storage of materials, in-process items and finished products, as well as the transfers between and within work centers."
  - **Production tracking** — "tracks and traces the status of production and disposition of work, including demonstration and documentation of regulatory and quality requirements... forward and backward traceability of components and their use within each end product."
  - **Equipment and personnel performance** — "track resource usage based on elapsed usage time and production quantities... ensure that production does not outpace maintenance requirements... track personnel training and certification requirements and orchestrate work assignments."
  - **Performance analysis** — "up-to-the-minute reporting of actual manufacturing operations and compare historical and expected results. Real-time feedback enables rapid identification and resolution of manufacturing issues."
- Industry-packaged products: Execution Discrete ("job shops and complex assembly"), Execution Process ("perfect quality required of process-manufactured products"), Execution Electronics ("printed circuit board, mechanical assembly and box-build"), Execution Medical Device and Diagnostics ("including electronic device history records (eDHR)"), Execution Pharma ("paperless manufacturing and electronic batch recording (eBR)"), Execution Semiconductor, Execution Foundation.
- From sibling pass (portfolio page): MES sits inside the Opcenter MOM portfolio beside quality, planning/scheduling (APS), intelligence, and logistics modules; MOM framed as "the real-time software layer that links product lifecycle management (PLM) to automation".

Interpretation: the suite pole realizes MES as the execution engine: order-anchored, resource-managed, traceability-producing, with regulated-industry packaging (eBR/eDHR) as first-class variants. Scheduling appears at execution grain (sequencing) while full APS remains a separate portfolio member.

### AVEVA Manufacturing Execution System (model-driven / industrial-software estate pole)

Evidence layer A — official product page + official FAQ (fresh):

- Capabilities, verbatim highlights:
  - **Real-time production control** — "Manage plant schedules and job execution with up-to-date production and inventory information. Track and trace the transformation of materials into products."
  - **Traceability and genealogy** — "Track the transformation of materials into finished products across storage and production locations on the shop floor. Quickly run traceability investigations to reduce the costs and risks of quality and safety non-compliance."
  - **Plant inventory management** — "Eliminate delays and optimize production schedules with real time visibility into plant inventory levels. Enforce bill of material (BOM) and pre-weight recipes to reduce out-of-spec products."
  - **Product and process quality control** — "Automate quality sample plan execution. Apply Statistical Process Control (SPC) methods... Visualize sample data and quality KPIs in real time."
  - **Performance management** — "Measure and monitor OEE KPIs and schedule adherence in real time. Quickly respond to events to minimize downtime..."
  - **Paperless work management and execution** — "Manage plant schedules and synchronize human workflows with machine actions in real time to execute workorders, complete jobs..."
- The vendor's own boundary statement (official FAQ, verbatim): "A MES executes the business planning done in ERP by connecting people, processes and systems on the shop floor for managing, scheduling, controling, monitoring and tracking the execution of all operational activities in real time to ensure and enforce the effective and compliant production of specified products or product variations as planned, while HMI/SCADA is used to monitor and control automated production proceses, equipment and facilities for save and reliable opertaion." Also: MES "digitizes, governs and controls the production of quality products... by synchronizing the human and machine actions in real time as specified in a process model on plant premises and document[s] the transformation of raw materials into finished goods for regulatory compliance".
- Execution binding language: AVEVA Work Tasks "enforcing the compliant execution of standard operating procedures"; process model "as specified in a process model".
- ERP integration machinery: AVEVA Enterprise Integration "automates the exchange of production planning and results data between your manufacturing execution system and business applications", with continuity/reconciliation behavior when the business system is offline.
- Deployment philosophy: composable, model-driven, packaged business capabilities / use-case libraries, hybrid cloud (mission-critical workflow and quality control on plant premises; multi-site analytics on cloud platform); native integration to AVEVA System Platform (SCADA/MES/IIoT platform) and PI System (historian).
- Target production styles (FAQ): "flexible multi product make-to-order or make-to stock", "batch-oriented and flexible", food & beverages, consumer goods, specialty chemicals, repetitive volume manufacturing.

Interpretation: an independent vendor states the same triple — execute ERP's plan on the floor, bind execution to a process model (enforce SOPs/recipes/BOM), document the transformation for traceability/compliance. Its center of gravity is batch/repetitive consumer-goods production rather than regulated pharma/aerospace, which helps distinguish what is common vs industry-specific.

### Tulip (boundary witness — the explicit non-MES pole)

Evidence layer A — official integration doc (fresh) + knowledge base (sibling pass):

- Tulip self-defines as a no-code frontline operations platform; apps at stations guide operator work; machines/stations are digital objects with states (Running/Stopped/Idle) and downtime reasons.
- The integration doc fixes the system-of-record split, verbatim: work orders, BOM, inventory, planning and scheduling belong to ERP/MES ("A workorder's source of truth may be your ERP..."); Tulip keeps "Tulip-Centric Context" (e.g., "non-conformances logged in Tulip against a workorder"). Typical transactions: "Get information about a work order given a work order ID. Mark a work order as completed given a work order ID. Find all of the open work orders assigned to a station given a station ID."
- Do/Don't table: "Use Tulip for use cases that are best executed in your ERP (e.g. order planning & scheduling)" is a **Don't**. Common use case: "ERP Orders + Tulip Unit-Level Traceability: Rapidly identify the universe of potentially defective finished products."
- Interpretation: Tulip contributes the frontline execution experience and unit-level captures, while order/planning/process-of-record ownership stays with ERP/MES. This confirms from the outside what the MES pole claims for itself: the execution system of record and the as-built/process binding are MES's distinguishing content, not the operator-app surface alone.

### L2L (boundary witness — connected operations pole)

Evidence layer A — official pages + FAQ (sibling pass):

- FAQ verbatim: "Does L2L replace our MES? In most plants, yes... For highly regulated environments needing full ISA-95 compliance, L2L is often deployed alongside an existing MES." And: "L2L pulls plans down from the ERP and pushes real-time results back up."
- Center of gravity: dispatch/abnormality routing, live production state, performance record — not enforcement of a defined process at unit grain.
- Interpretation: the market itself distinguishes "simple MES replacement" (job tracking + monitoring) from ISA-95-grade MES (regulated enforcement + as-built). Confirms the enforcement/record leg as the deep-MES differentiator, and confirms the label "MES" is used loosely at the shallow end.

### MachineMetrics (boundary witness — label noise)

Evidence layer A (marketing site only, sibling pass; assertions reduced):

- Self-labels "Intelligent MES and AI-powered machine monitoring"; actual center: universal machine connectivity, OEE/production monitoring, downtime tracking, work order tracking via ERP sync, automated scheduling.
- Interpretation: a machine-data platform with job tracking carries the MES label in the market. The label cannot be the boundary criterion; the structure (process-bound execution + unit-grain as-built record) must be.

## Cross-product Comparison

| Dimension | Siemens Opcenter Execution | AVEVA MES | Tulip (witness) | L2L (witness) | MachineMetrics (witness) |
|---|---|---|---|---|---|
| Self-label | MES family in MOM portfolio | MES | frontline operations platform | connected operations platform | "Intelligent MES" |
| Order/work-unit execution at operation grain | yes (production tracking, disposition, sequencing) | yes (job execution, workorders, schedules) | partial (app steps; order state stays in ERP/MES) | partial (order context from ERP sync) | partial (job tracking) |
| Execution bound to process definition | yes (design/engineering/process data reflected in production; eBR/eDHR families) | yes ("as specified in a process model"; enforce BOM/recipes; SOP enforcement) | partial (apps guide; no process-of-record claim) | no by default (coexists with ISA-95 MES when needed) | limited evidence |
| As-built record at unit/lot grain | yes (forward/backward traceability of components within each end product) | yes (traceability and genealogy; transformation of materials into products) | unit-level traceability positioned as *its* contribution against ERP orders | not claimed | partial (job-level machine data) |
| Regulated-industry record (eBR/eDHR class) | yes (product families) | partial (compliance documentation framing; no eBR/eDHR product claim observed) | GxP features (e-signature, record history) — variant | coexists with regulated MES | no |
| Resource management (equipment/personnel/material) | yes (explicit cluster) | yes (plant inventory; BOM enforcement) | stations/machines digital objects | maintenance/skills modules | machine fleet |
| In-line quality execution | yes (documentation of regulatory/quality requirements; QMS sibling in portfolio) | yes (sample plans, SPC) | non-conformance capture in apps | quality abnormalities/checks | limited |
| Performance/OEE analysis | yes (performance analysis cluster) | yes (OEE, schedule adherence) | analytics from states | OEE dashboards | core |
| Sequencing/scheduling depth | execution-grain sequencing; APS separate | plant schedule management | declined (ERP's job) | line-level adaptive scheduling | automated scheduling |
| ERP integration | yes (digitally linking enterprise systems) | yes (dedicated Enterprise Integration machinery) | yes (integration doc) | yes (ERP sync) | yes (connectors) |
| Machine connectivity | via automation layer / IT-OT integration | native via System Platform; agnostic connectivity claimed | yes (edge/OPC UA) | optional Machine Data Sync | core |
| Deployment | on-prem/cloud, suite packaging | hybrid cloud, composable/model-driven | SaaS, no-code | SaaS | SaaS |

Evidence layer B findings (cross-product commonality):

- **Order-anchored execution at operation grain with resource context** — present in both deep MES samples; partial in all three witnesses. This gradient is itself the boundary.
- **Execution bound to a held process definition** — explicit in both deep samples (Siemens: design/engineering/process data reflected in production; AVEVA: process model, BOM/recipe enforcement, SOP enforcement). Absent or shallow in all three witnesses. Strongest differentiating leg vs the operations-platform market.
- **As-built record at unit/lot grain producing traceability** — explicit in both deep samples; Tulip positions unit-level traceability as the value it adds *on top of* ERP orders, implying it is not the ERP's native grain. L2L/ISA-95 coexistence statement implies the same.
- **ERP as plan owner; MES exchanges orders/actuals** — 5/5 samples in some form (native in MES pole; integration-mediated in witnesses). AVEVA states the direction explicitly; Tulip's system-of-record split states the same from the other side.
- **In-line quality and regulated documentation** — deep in the regulated-packaged suite; present-but-lighter in batch/consumer-goods MES; variant elsewhere.
- **OEE/performance analysis and machine connectivity** — universal across the market but weighted differently (core in monitoring-first products; supporting in MES products) → standard capability, not definitional.

## Canonical Model

### L0 — Defining Invariant

A Manufacturing Execution System is the manufacturer's system for **executing released production orders on the shop floor against a defined process and producing the as-built record of what was actually made**. Three structures, jointly held:

1. **The released production order as the unit of executed work.** MES receives released orders (typically from ERP/planning) and manages their execution on the floor at operation/step grain: dispatching to lines, work centers, and machines; advancing steps; assigning and tracking equipment, personnel, and materials against the order; completing it and reporting results upward. Remove → planning/scheduling tools (orders exist, nothing executes them) or a dispatch board.
2. **Execution bound to the defined process.** The order executes against a held definition of how the product is made — routing operations or recipes/master recipes with parameters, work instructions, in-line quality checks — so the floor does what the definition says. Depth varies from advisory guidance (operator sees the step) to hard enforcement (out-of-sequence blocked, failed checks hold the unit, BOM/recipe enforced at issue, only approved versions run). Remove → generic production tracking; the system no longer executes *a defined method*.
3. **The as-built record at unit/lot grain.** The system accumulates what was actually produced, per serialized unit or lot: which materials/lots were consumed, on which equipment, by whom, when, with what measurement and inspection results — retained as the permanent production history from which forward/backward traceability and, in regulated industries, electronic batch/device records are produced. Remove → production monitoring/reporting tools; nothing of lasting evidentiary value accumulates.

Jointly-held is load-bearing:

- 1 alone = production order tracking / dispatch board
- 2 alone = work instruction / SOP / document control
- 3 alone = traceability/genealogy system (the Manufacturing Traceability leaf)
- 1+2 without 3 = guided execution tooling with no permanent record
- 1+3 without 2 = job tracking plus data collection without process binding — a shallow straddle the market still labels "MES" (see label-noise finding below)
- 2+3 without 1 = process/quality documentation not driven by order execution

Positioning (vendor-consistent, not standards-verified): between ERP/planning (which owns orders, BOMs, inventory, costing) and machine control (SCADA/PLC, which owns the equipment). Stated in vendors' own words by AVEVA ("executes the business planning done in ERP... while HMI/SCADA is used to monitor and control automated production processes"), Siemens ("digitally linking enterprise systems with automated manufacturing equipment"), L2L, and Tulip's system-of-record split.

### L1 — Common Mature Structure

- Machine/equipment connectivity and automatic data collection (PLC/SCADA integration, industrial protocols) feeding states, counts, and process values into the execution record.
- Resource management depth: equipment states/usage tracking, personnel training/certification gating of assignments, material movement/storage within and between work centers, plant-level inventory visibility.
- In-line quality execution: sample plans, SPC, holds and dispositions feeding the quality system of record.
- OEE / performance analysis over the execution record (up-to-the-minute reporting, historical comparison).
- Paperless operator surfaces: work instructions delivered at the point of work; in regulated packaging, the eBR/eDHR realizations of the as-built record.
- ERP integration machinery in both directions (order release inbound; results/actuals outbound), including offline-continuity and reconciliation behavior.
- Execution-grain sequencing/dispatch optimization (finer than APS planning).
- Multi-site standardization (model-driven or template-based rollouts) and analytics dashboards; AI insights as an era-current overlay.

### L2 — Variant / Optional Structure

- Industry packaging: discrete job shop / complex assembly vs process/batch vs regulated pharma (eBR) vs medical device (eDHR) vs electronics/PCB vs semiconductor. The packaging changes vocabulary (batch, lot, unit, op) and the enforcement depth more than the structure.
- Enforcement depth: advisory → guided → blocking. The deep-MES pole itself notes the shallow end is replaceable by simpler tools (L2L FAQ); regulated environments are where blocking depth is decisive.
- Deployment: on-prem vs cloud vs hybrid; monolithic suite vs composable/model-driven modular packaging.
- Relationship to the broader portfolio: standalone MES vs execution engine inside a MOM suite (with quality/planning/intelligence/logistics siblings).
- Scale/tier: global multi-site enterprises down to single-plant deployments; SaaS mid-market products.
- Scheduling depth: none → line-level sequencing → bundled APS (APS remains its own leaf).

### L3 — Vendor-specific (Research Notes only)

- Siemens: Opcenter Execution family naming (Discrete/Process/Electronics/Medical Device/Pharma/Semiconductor/Foundation); eBR/eDHR as productized families; Camstar/SIMATIC IT heritage; MOM portfolio framing; Mendix low-code personalization (sibling pass).
- AVEVA: Work Tasks (SOP-enforcing workflow), Enterprise Integration (offline-tolerant ERP exchange), native System Platform/PI System integration, CONNECT cloud analytics, model-driven packaged business capabilities/use-case libraries, hybrid-cloud split of mission-critical edge vs cloud multi-site.
- Tulip: Tables/Triggers/Apps model, citizen-developer methodology, unit-level traceability positioned against ERP orders, explicit Don't on order planning & scheduling.
- L2L: Dispatch model; explicit "replace the MES?" FAQ positioning; Stabilize/Standardize/Optimize method; Yokoten (sibling pass).
- MachineMetrics: "Intelligent MES" self-label over a monitoring/scheduling-centered product — market-label noise, not a structural datum.

## Vendor-specific Findings

See L3. Additionally: AVEVA is the only sampled vendor with a full sentence-level MES-vs-ERP-vs-SCADA boundary statement in an official FAQ; Tulip is the only sampled vendor with a written system-of-record table for work orders/BOM/inventory; L2L is the only sampled vendor that publicly prices the boundary ("replaces a simple MES in most plants; alongside an existing MES in regulated environments"). All three are treated as product-level statements that triangulate the seam, not as Type properties.

## Boundary Findings

- **vs Manufacturing ERP.** ERP owns the business-grain record: orders, BOMs/routings as masters, inventory, costing; its shop-floor recording is coarse confirmation (consumption/output/time against the order). MES owns execution grain and evidentiary grain: step-level enforcement and a per-unit/lot as-built record with genealogy. AVEVA states the seam verbatim ("executes the business planning done in ERP"); Tulip's system-of-record table states it from the other side. Remove the as-built unit-grain record and step-level process binding from MES and what remains is ERP shop-floor recording. Note: some manufacturing-ERP suites sell an MES module (bundling, not Type identity).
- **vs Production Planning / APS.** Planning decides what/when/which resources ahead of time at plant/schedule grain; MES executes released orders and optimizes within execution (sequencing, dispatching). Siemens keeps APS as a separate portfolio member; AVEVA manages "plant schedules and job execution" at execution grain; Tulip explicitly declines scheduling. Remove the planning horizon and you have MES; remove the execution/as-built and you have APS.
- **vs Factory Operations Management / MOM (joint review).** Same layer, different center. MES centers on enforcing order execution against a defined process and producing the as-built record; FOM centers on the live operational picture + event-and-response loop + performance record. Suite pole bundles MES as MOM's engine (Siemens portfolio); connected-operations poles either replace a shallow MES or coexist with an ISA-95-grade one (L2L FAQ) or integrate to it (Tulip). Remove live operations management → still MES; remove execution enforcement + as-built → still FOM. The seam drawn from this side agrees with the sibling's seam; joint review satisfied.
- **vs Shop Floor Management.** Event-and-response (andon/dispatch/issues) vs order-execution + as-built. A shop-floor management product needs no unit genealogy; an MES needs no abnormality-response loop as its center (though suites may include one).
- **vs SCADA / HMI / DCS / PLC.** Machine-level supervisory control and process visualization vs order-and-unit-level execution. AVEVA's FAQ draws exactly this line. Remove order/lot context → SCADA.
- **vs Industrial Historian.** Time-series process tags vs unit-bound production records; the historian is a data substrate MES may consume (AVEVA PI integration). Remove the process model and orders → historian.
- **vs Manufacturing Traceability.** Genealogy is MES's third leg; a standalone traceability system keeps and queries the record without executing production. In suites the record is produced by the execution engine (sibling's finding, consistent from both passes). Remove execution → traceability platform.
- **vs Manufacturing QMS / CAPA.** The quality system of record (documents, audits, CAPA, complaints) vs in-line quality execution (checks, SPC, holds) feeding it. Remove the quality-record center → MES retains quality execution only.
- **vs OEE Management Platform.** Effectiveness measurement/analytics vs execution. OEE appears in 5/5 sampled products but as a derived view; removing it leaves the MES intact.
- **Market-label noise finding.** "MES" is applied in the market both to the deep Type (Siemens, AVEVA) and to shallow job-tracking/monitoring products (MachineMetrics self-label; L2L's "simple MES" replacement claim). The Type boundary must therefore be structural (execution + process binding + as-built record), not label-based. Shallow straddles (L0 legs 1+3 without 2) are recorded as a gray zone.
- **"Remove what → becomes the neighbor" test:** remove the as-built record → production monitoring/dispatch; remove process binding → job tracking; remove order execution → traceability/documentation; remove unit/lot grain → ERP shop-floor recording; remove the floor entirely → ERP/APS.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit?

- **Paper-traveler era (pre-digital):** a job packet moving with the order — router sheet (process definition), operation sign-offs (step execution at order grain), lot/serial stamps and inspection sign-offs recorded on the traveler (as-built record at unit/lot grain) — satisfies all three legs with no software, no machine connectivity, no OEE. The MES digitizes precisely this packet; the vocabulary (routing, traveler, batch record) predates the software category.
- **1990s MES generation (MESA-era):** order dispatching, step tracking, labor/data collection, genealogy on the shop floor — fits without cloud, AI, or modern connectivity.
- **Regional vendors** (e.g., regional MES products in Asia/Europe serving electronics or pharma): same triple; industry packaging varies.
- Modern additions (machine connectivity, OEE arithmetic, e-signatures, hybrid cloud, AI insights) are era-current capabilities, not definitional.

Conclusion: the L0 passes the historical check; the definition does not depend on connectivity, cloud, OEE, or any specific protocol.

## Uncertainties

1. **Specialist poles under-sampled.** iBase-t (aerospace/defense), 42Q (cloud mid-market), Plex (cloud ERP-adjacent), Körber PAS-X (pharma), DELMIA Apriso were all unreachable this pass (403/empty/timeout/404). The regulated leg rests on Siemens' own eBR/eDHR family descriptions plus AVEVA's compliance documentation language; the aerospace/MRO flavor of the as-built record is not independently verified.
2. **No standards text.** No ISA-95/MESA-11 document was retrievable (MESA International dissolved 30 June 2026; content assumed by ISA; no MES standards document accessible this pass). The "between ERP and control" layering is held on four independent vendors' own statements (Siemens, AVEVA, L2L, Tulip), which agree with each other but are vendor evidence. ISA-95 compliance is mentioned only as a vendor-side phrase (L2L FAQ), not verified against the standard.
3. **Label noise.** The shallow straddle (order tracking + data collection without process binding) is labeled "MES" by part of the market. This pass holds the structural boundary; whether the taxonomy should split a "production tracking" Type off is a taxonomy-pass question, recorded in STATUS.md.
4. **Evidence quality asymmetry.** Two deep samples are both large European industrial-software vendors; mid-market cloud MES evidence is witness-grade only (marketing-site or FAQ). Assertions about mid-market MES behavior are calibrated to "common" strength, not "defining".
5. Numeric claims in vendor marketing (AVEVA's +15–20% OEE improvement etc.) were excluded from all canonical statements.

## Final Synthesis

A Manufacturing Execution System is the execution layer between the manufacturer's business systems and its machines: it takes released production orders and executes them on the floor at operation/step grain, binding what the floor does to the defined process (routing/recipe/work instructions/quality gates) and accumulating a permanent as-built record at unit/lot grain — what was made, from which materials, on which resources, by whom, with what results — from which forward/backward traceability and regulated-industry records (eBR/eDHR class) are produced. ERP owns the plan, orders, and business record; SCADA/PLC own the machines; the MES owns the execution of the plan on the floor and the evidentiary record of what was built. Enforcement depth (advisory → blocking), industry packaging (discrete/process/regulated/electronics/semiconductor), deployment shape, and portfolio context vary; OEE, machine connectivity, scheduling, quality modules, and AI are standard or optional capabilities, not the definition. The sharpest seams: with Manufacturing ERP (business record vs execution/evidence), with Factory Operations Management/MOM (live operations management vs execution enforcement + as-built; bundled in suites), and with Manufacturing Traceability/QMS (record-keeping centers vs execution-produced records). The market sometimes labels shallow job-tracking/monitoring products "MES"; the structural core above, not the label, is the Type.
