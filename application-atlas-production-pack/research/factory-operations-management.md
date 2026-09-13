# Research Notes — Factory Operations Management

## Research Goal

Determine what "Factory Operations Management" is as a distinct Application Type: what core objects and structures define it, who uses it, how operational work actually flows through it, and where its boundaries lie against the dense cluster of neighboring manufacturing leaves (MES, Shop Floor Management, OEE Management Platform, Production Planning / APS, SCADA, Industrial IoT Platform, CMMS/EAM, Manufacturing QMS, Manufacturing Traceability).

A key prior question: the directory leaf name maps onto the established market category "Manufacturing Operations Management (MOM)". The research must decide whether this leaf has an honest defining core of its own, or is merely an alias/umbrella over MES.

## Initial Boundary (working hypothesis, pre-research)

- Core use: managing the running of production on the factory floor in real time — between enterprise planning (ERP/APS) and machine control (SCADA/PLC).
- Likely users: operators, supervisors, plant/operations managers, plus maintenance/quality/materials responders.
- Likely nearest neighbors: MES (execution + traceability), Shop Floor Management (lean visual/issue management), OEE Management Platform (equipment effectiveness analytics), IIoT/SCADA (connectivity/control).
- Unknowns: does the market treat "factory operations management" as its own product category or just as MOM = MES umbrella? Does a core exist that covers both an enterprise MOM suite (Siemens-style) and a composable frontline operations platform (Tulip-style) without being vacuous?

## Research Questions

1. What objects does a factory operations product actually manage (machines/work centers, orders/jobs, operators/shifts, events, measures)?
2. Which functions are definitional vs bundled (execution, scheduling, quality, maintenance, inventory, work instructions, analytics)?
3. What is the operational loop (plan → execute → capture → respond → measure → improve)?
4. How does the product sit relative to ERP (plan owner) and SCADA/PLC (control layer)?
5. Where exactly is the seam with MES — and do the sampled products treat MES as inside, alongside, or outside this Type?
6. Would the definition survive the paper-era factory (boards, andon, shift logs) and non-Western / regional lean practice (§24 check)?

## Representative Products

Chosen for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| Siemens Opcenter | unified MOM suite (MES execution core + quality + planning + intelligence) | large enterprise, discrete + process + regulated | good (official product pages fetched) |
| Tulip | composable no-code frontline operations platform | mid-market → enterprise; lean/CI-driven manufacturers | excellent (full official knowledge base fetched) |
| L2L | connected manufacturing operations platform ("system of action", dispatch/abnormality-centric) | mid-size → global enterprise | good (official platform + solution pages fetched) |
| MachineMetrics | machine-data-centric "Intelligent MES" / production monitoring | discrete manufacturers, SME → mid | medium (official marketing site fetched; support docs not fetched) |

Rejected/failed samples: GE Vernova Proficy Plant Applications (enterprise MOM — URL 404 twice, abandoned), 42Q (cloud MES — fetch returned empty twice, abandoned). Rockwell FactoryTalk not attempted (time). This leaves the enterprise-suite pole with a single deep sample (Siemens) — noted under Uncertainties.

## Sources

All fetched 2026-09-08:

- Siemens — Opcenter MOM portfolio page: https://www.siemens.com/en-us/products/opcenter/ (fetched via plm.sw.siemens.com/en-US/opcenter/)
- Siemens — MES solution page: https://www.siemens.com/en-us/solutions/manufacturing-execution-system-mes/
- Siemens — Opcenter Execution (MES family): https://www.siemens.com/en-us/products/opcenter/execution/
- Tulip — Knowledge Base index: https://support.tulip.co/llms.txt
- Tulip — "What is Tulip?": https://support.tulip.co/docs/what-is-tulip
- Tulip — "Shop floor management": https://support.tulip.co/docs/shop-floor-management
- Tulip — "A Tour of the shop floor": https://support.tulip.co/docs/a-tour-of-the-shop-floor
- Tulip — "Machine attributes, downtime reasons, and states": https://support.tulip.co/docs/machine-attributes-downtime-reasons-and-states
- Tulip — "Plan an integration between Tulip and an MES or ERP": https://support.tulip.co/docs/plan-an-integration-between-tulip-and-an-mes-or-erp
- L2L — homepage: https://www.l2l.com/
- L2L — Platform: https://www.l2l.com/platform
- L2L — Shop Floor Execution: https://www.l2l.com/platform/shop-floor-execution
- L2L — Production Management: https://www.l2l.com/platform/production-management
- MachineMetrics — homepage: https://www.machinemetrics.com/

Not reachable: GE Vernova Proficy Plant Applications (404 ×2: /software/products/plant-applications, /software/products/proficy-plant-applications), 42Q (empty response ×2). No independent analyst/standards text (MESA, ISA-95) fetched; the "layer between planning and control" framing is evidenced through vendor positioning only (Siemens and L2L both state it explicitly in their own words).

## Product Observations

### Siemens Opcenter (MOM suite pole)

Key observations (evidence layer A — official pages):

- Self-definition: "Opcenter is a unified manufacturing operations management (MOM) solutions portfolio, enabling digital software operations management."
- Layer positioning, verbatim: "MOM is the real-time software layer that links product lifecycle management (PLM) to automation, connecting the virtual world of product development with the real world of production." Also: "Digitally plan and orchestrate manufacturing and quality operations"; "Compare as-planned and as-is data" (closed loop).
- Named MOM capabilities: Manufacturing execution (MES), Quality management (QMS), Production planning and scheduling, Enterprise manufacturing intelligence.
- Products in portfolio: Opcenter APS; Opcenter Execution (MES families: Discrete, Process, Electronics, Medical Device with electronic device history records, Pharma with electronic batch recording, Semiconductor, Foundation); Opcenter X Quality; Opcenter RD&L (research/development/lab); Opcenter Intelligence (analytics); Opcenter Intra Plant Logistics (material flow warehouse→shop floor); Opcenter X (SaaS MOM for SMB).
- MES ("Opcenter Execution") key capabilities, verbatim highlights: optimized sequencing; "resource allocation and control — manage all relevant resources for manufacturing operations... manage and track the movement and storage of materials, in-process items and finished products"; "production tracking — tracks and traces the status of production and disposition of work... forward and backward traceability of components"; "equipment and personnel performance — track resource usage based on elapsed usage time and production quantities... ensure that production does not outpace maintenance requirements... track personnel training and certification requirements and orchestrate work assignments"; "performance analysis — up-to-the-minute reporting of actual manufacturing operations... Real-time feedback enables rapid identification and resolution of manufacturing issues."
- MES monitor/orchestrate/track-and-trace/optimize framing; "manage, monitor and control production processes across the shop floor"; "real-time information about production activities, resources and materials".

Interpretation: in the suite pole, MES execution is the engine inside the MOM portfolio; MOM adds quality, planning/scheduling, intelligence, and logistics around it. The order (work order) is the anchor object; as-built/traceability is the MES-grade differentiator.

### Tulip (composable frontline operations pole)

Key observations (evidence layer A — full official knowledge base):

- Self-definition: "Tulip is a no-code frontline operations platform" — apps built by "citizen developers" (manufacturing engineers), explicitly contrasted with "traditional MES" monolithic architecture ("composable vs. monolithic architectures" doc).
- Shop floor model: "Shop floor management" doc — Stations ("digital representations of physical workspaces where tasks are executed"), Interfaces (display devices running the Player; exactly one per station), Machines ("a digital representation of a physical datasource"), Edge devices, Vision (cameras/detectors).
- Machine state model (Machine attributes, downtime reasons, and states doc): default States "Running, Stopped, Idle"; default Downtime Reasons list "Changeover, Maintenance, Material, No Operator, On Break, On Lunch, Other, Set up, Team Meeting, Tooling"; Attributes are machine properties (setpoints/actuals, e.g. cycle time, spindle speed); Machine Types group per-model definitions; states feed OEE calculations and analytics.
- App model: operator-facing apps with steps, triggers, timers, forms, widgets; data in Tables (records, aggregations, queries, record links); Analytics editor (first pass yield, defect pareto, cycle time by user, control charts, machine data analysis); dashboards ("create your first shop floor dashboard"); Automations; HTTP/SQL/MQTT connectors; e-signature and record-history for GxP use.
- MES/ERP boundary, verbatim from "Plan an integration between Tulip and an MES or ERP": ERP/MES is "system of record" for work orders, BOM, inventory, planning and scheduling ("Use Tulip for use cases that are best executed in your ERP (e.g. order planning & scheduling)" listed under Don'ts). Typical transactions: "Get information about a work order given a work order ID. Mark a work order as completed given a work order ID. Find all of the open work orders assigned to a station given a station ID." "Store Tulip-Centric Context in Tulip. A workorder's source of truth may be your ERP, but certain data is relevant mainly to Tulip (e.g. non-conformances logged in Tulip against a workorder)." Common use cases include "Improved dispatching in ERP based on real-time manufacturing workcenter statuses" and "ERP Orders + Tulip Unit-Level Traceability".
- Lean/CI framing: "Stay Lean... Go to Gemba... Find & unload from the bottleneck"; continuous improvement through incremental app deployment.

Interpretation: Tulip deliberately does NOT own planning or full MES enforcement; it owns the frontline execution experience (operator apps at stations), live machine/resource state, captured operational data, and the improvement loop. This is the pole furthest from classic MES — useful for finding the minimal core.

### L2L (connected operations / "system of action" pole)

Key observations (evidence layer A — official platform/solution pages):

- Self-definition: "The Connected Manufacturing Operations Platform"; its own FAQ heading: "L2L Manufacturing Operations Management (MOM) software". Tagline: "The Heartbeat of the Modern Factory"; positioning as "the single system of action" versus "rigid legacy suites" (system-of-action vs system-of-record framing is their stated philosophy).
- Shop Floor Execution module: real-time dispatch ("Automatically assign and track tasks based on machine alerts, ensuring the right person is moving to the right problem the second it happens"); abnormality management ("Give operators a seamless way to report machine, quality, or safety hiccups. These alerts are instantly routed and tracked through to resolution"); visual work instructions & SOPs at the point of work; digital document management; best-practice sharing (Yokoten) across shifts/plants; digital checklists; root cause analysis + "permanent corrective actions"; dashboards for downtime and OEE; real-time notifications; AI ("L2L Execution AI... When a line slows or stops, L2L Execution AI suggests a fix and routes it to the right person automatically").
- Production management module ("Go from planned to performed"): production planning & scheduling, real-time production monitoring (output/performance/status live across lines and sites), line-level rescheduling & adjustments ("Instantly reschedule at the line level and adjust production orders and planned operator counts as conditions shift"), capture actuals ("tied to the anticipated output of a build sequence or order - synced with your ERP"), quality checks & anomaly capture at source, audits & checks (5S, PFMEA, IPQC, start-up…), safety & incident management, continuous improvement tools.
- Maintenance module (CMMS) and Skills module ("automated skill-checks that prevent unauthorized work").
- Integration packages: Application Sync (ERP: "inventory, production orders, and financial data stay perfectly in sync with operational reality"); Machine Data Sync ("Connect L2L to your PLCs, SCADA systems, and IIoT devices to automate OEE calculations and downtime tracking. Use real-time machine health data to trigger condition-based maintenance"); UI Extension.
- Method: Stabilize (capture every disruption and resolution in real time; quantify response times, failure modes, costs) → Standardize (operationalize standard work; digital audits; data-led RCA) → Optimize (analytics-driven CI, OEE).
- MES/ERP boundary, verbatim from FAQs: "Does L2L replace our MES? In most plants, yes... For highly regulated environments needing full ISA-95 compliance, L2L is often deployed alongside an existing MES." "Does L2L replace our ERP? No. L2L complements ERP by handling the 'last mile' of execution on the floor that ERPs were never designed to manage. L2L pulls plans down from the ERP and pushes real-time results back up." "What is shop floor execution software? ... You could see it as a combination of MES + connected worker + CMMS." "How does shop floor execution connect to maintenance and quality? It's one platform, not three. An abnormality raised during execution can auto-trigger a maintenance work order. A quality fail can pause a line and escalate to a supervisor."
- Works without machine connectivity: "Whether your lines feed data through PLCs and SCADA, or your team captures output and status through operator entry..."

Interpretation: L2L centers the response loop (abnormality → dispatch → standardized resolution → RCA) and wraps it with live production state, ERP order sync, and performance measurement. Shift language is pervasive ("every shift, every line", shift priorities, shift progress).

### MachineMetrics (machine-data-centric pole)

Key observations (evidence layer A for the marketing site; support docs not fetched — assertion strength reduced accordingly):

- Self-definition: "Intelligent MES and AI-powered machine monitoring for discrete manufacturers - connecting machines, ERP, and tribal knowledge while automating everything in between." "Stop monitoring machines, start monitoring production."
- Core model visible from navigation: universal machine connectivity (any make/model; MTConnect, OPC UA, etc.); machine monitoring; production monitoring (OEE & production analytics); downtime tracking ("instant visibility into every machine, every shift, every job"); work order tracking ("MachineMetrics unifies machine data, ERP, and workflows"); automated scheduling (Production Schedule Intelligence); condition monitoring / predictive maintenance; ERP connectors.
- Roles addressed: production, operations, maintenance, scheduling, frontline, executives.

Interpretation: this pole starts from machine data and reaches toward orders (ERP sync) and scheduling — the mirror image of Tulip (starts from operator work, reaches toward machines). The two poles meet in the middle: live production operations with order context. MachineMetrics labeling itself "MES" while delivering monitoring+scheduling confirms that "MES" as a label is used loosely in this market and cannot be taken as a boundary criterion by itself.

## Cross-product Comparison

| Dimension | Siemens Opcenter | Tulip | L2L | MachineMetrics |
|---|---|---|---|---|
| Self-label | "unified MOM portfolio" | "frontline operations platform" | "Connected Manufacturing Operations Platform" / "MOM software" | "Intelligent MES and machine monitoring" |
| Anchor object | work order (production + quality operations) | station + app + machine + table records | machine/asset + dispatch + shift | machine + job (ERP work order) |
| Live resource state | yes (production status, resource usage) | yes (machine states: Running/Stopped/Idle; interface/station status) | yes (live run rates, status changes, machine alerts) | yes (machine states, downtime, run rates) |
| Downtime reason coding | yes (production tracking/disposition) | yes (named default reason list) | yes (downtime tracking, failure modes) | yes (downtime analysis) |
| Production order/job context | native (execution core) | via ERP/MES integration (work order pull; mark completed) | via ERP sync ("capture actuals... synced with your ERP") | via ERP connectors (work order tracking) |
| Event → response loop | yes ("real-time feedback and resolution of manufacturing issues") | via apps/triggers/automations (operator reporting, escalation) | explicit center (dispatch, abnormality routing, RCA) | partial (alerts/workflows, less dispatch-centric) |
| Standardized work / instructions | yes (work instructions, 3D instructions) | yes (apps as instructions; checklists) | yes (visual work instructions, SOPs, checklists) | limited (frontline surface) |
| Quality events | yes (QMS capability) | yes (non-conformances logged in apps) | yes (quality abnormalities, quality checks) | limited |
| Maintenance response | yes (production must not outpace maintenance) | optional (integrations) | yes (CMMS module; auto work orders) | yes (condition monitoring → maintenance) |
| OEE / performance measurement | yes (performance analysis, OEE via IT/OT) | yes (states feed OEE; analytics) | yes (automated OEE calc, dashboards) | yes (OEE & production analytics — core) |
| Execution enforcement (routing, eBR/eDHR, genealogy) | yes (MES families: eBR, eDHR, forward/backward traceability) | no (explicitly integrates to MES; unit-level traceability via ERP orders) | no by default (coexists with MES when ISA-95-grade needed) | partial (job tracking; no e-record enforcement evidence) |
| Scheduling | yes (Opcenter APS in portfolio) | no (explicitly ERP's job) | yes (line-level adaptive scheduling) | yes (Production Schedule Intelligence) |
| Machine connectivity | via automation layer / IT-OT integration | yes (OPC UA, MQTT, edge devices) | yes (PLC/SCADA/IIoT sync package; optional) | yes (universal connectivity — core) |
| AI layer | AI integration mentioned (low specificity) | yes (AI agents, copilot) | yes (Execution AI — prescriptive) | yes (Max AI) |

Evidence layer B findings (cross-product commonality, 4/4 unless noted):

- Live operational state of machines/work centers with coded downtime reasons — 4/4 (Tulip and L2L documented in detail; MM strongly; Siemens via production tracking).
- Production order / job context anchored to resources — 4/4, but *ownership varies*: native in the suite pole; consumed-from-ERP in the other poles. This asymmetry is itself a finding: the Type consumes the production plan; it does not own it.
- Event-and-response loop (capture at source → route → track to resolution) — strong in L2L, explicit in Siemens ("real-time feedback and resolution"), present in Tulip (apps/automations), weaker/partial in MachineMetrics.
- OEE / performance measurement per machine/line/shift — 4/4, but weight varies from core (MM) to supporting (Siemens, Tulip).
- Dual capture paths (machine signals + operator entry) — documented explicitly by Tulip (machine triggers + app input) and L2L ("PLCs and SCADA... or... operator entry"); implied by MM (tribal knowledge + machine data).
- Shifts/lines/sites as the organizing operational grid — L2L pervasive; Tulip (stations, shifts and schedules feature); Siemens (lines, plants, multi-site); MM ("every machine, every shift, every job").
- Standard work / instructions delivery at the point of work — 3/4 (Siemens, Tulip, L2L), limited evidence for MM.
- ERP integration as plan/result exchange — 4/4.

## Canonical Model (Layer C)

### L0 — Defining Invariant

Factory Operations Management is the manufacturer's system for running production on the factory floor in real time. Three structures, jointly held:

1. **The live operational picture of production.** The factory's production resources — machines, lines, work centers, stations — and the work running on them (production orders / runs / jobs, organized by line and shift) are held as managed objects whose current operational state is continuously maintained: running / stopped / idle, changeover, downtime with coded reasons, progress against plan. Remove this leg → a planning system or asset registry with nothing live (ERP/APS owns the plan, not the live state); the Type collapses into adjacent record systems.

2. **The event-and-response loop at the point of production.** Operational events — downtime, quality problems, material shortages, safety incidents, deviations from plan — are captured at the source (operator report and/or machine signal) and driven through a routed, typically standardized response by the responsible function (maintenance, quality, materials, supervision), tracked to resolution. Remove this leg → passive production monitoring / OEE dashboards; the "management" in operations management disappears.

3. **The operational performance record.** The accumulated state, events, and counts are computed into operational performance measures per machine / line / shift / site (OEE, downtime, throughput, yield in current products) that management uses to steer operations and close the loop back into improvement. Remove this leg → an andon/alerting app with no operations record to manage by.

Jointly-held is load-bearing:

- 1 alone = production/machine monitoring (seam with the OEE Management Platform / production monitoring market)
- 2 alone = andon/alerting tool
- 3 alone = BI/analytics
- 1+3 without 2 = OEE analytics without a management loop
- 2+3 without 1 = generic issue tracking with no production context
- 1+2 without 3 = dispatch without an operational record

Positioning (evidence-calibrated): the Type occupies the layer between enterprise planning (ERP/APS) and machine control (SCADA/PLC). This is stated by vendors themselves — Siemens: "MOM is the real-time software layer that links PLM to automation"; L2L: "pulls plans down from the ERP and pushes real-time results back up" and "connect to your PLCs, SCADA systems, and IIoT devices". No independent standards text was fetched, so this framing is held as vendor-consistent rather than standards-verified.

### L1 — Common Mature Structure

- Machine data connectivity (OPC UA / MQTT / edge gateways) producing automatic states and OEE — dominant but not required (L2L explicitly supports operator-entry-only deployments; paper-era ancestor obviously lacks it).
- Work instructions / SOPs / digital checklists delivered at the point of work.
- Quality events captured at the source (non-conformances, checks) feeding response.
- Notifications, escalation, and routing rules (including auto-triggered maintenance work orders).
- Dashboards / live boards (andon-style visual management).
- Root cause analysis and corrective-action follow-through; continuous-improvement tooling.
- ERP integration for order pull and actuals push.
- Shift and schedule management; multi-line, multi-site rollup.
- User/role governance; skills/qualification checks (L2L explicit; Siemens personnel certification tracking).
- E-signature / electronic records for regulated deployments (Siemens eBR/eDHR; Tulip GxP).

### L2 — Variant / Optional Structure

- Execution depth: full MES-grade enforcement (routing enforcement, eBR/eDHR, forward/backward genealogy) present in the suite pole; absent by design in the composable/connected poles. This is the primary segmentation axis of the Type.
- Scheduling depth: from none (Tulip) through line-level adaptive scheduling (L2L, MM) to full APS (Opcenter APS — but APS is its own leaf).
- Maintenance depth: from simple response routing to a full CMMS module (separate leaf).
- Material logistics (warehouse→line), laboratory/R&D, warehousing-grade inventory — suite-pole extras.
- Computer vision inspection; AI copilots/prescriptive recommendations; predictive/condition monitoring.
- Deployment: cloud SaaS vs on-premise; industry packaging (discrete/process/electronics/pharma/semiconductor).

### L3 — Vendor-specific (Research Notes only)

- Tulip: Tables/Triggers/Automations/App Editor as build blocks; citizen-developer methodology; Edge IO/Edge MC hardware; Vision detectors (jig/change/color/OCR); specific default downtime-reason list; "interfaces" naming (r283 rename).
- L2L: Dispatch concept and "Dispatch Summary"; L2L Method (Stabilize/Standardize/Optimize); Yokoten sharing; Execution AI; IWS/TPM/Lean support claims; marketing ROI percentages (excluded from canonical doc).
- Siemens: Opcenter module family names (Execution Discrete/Process/Electronics/Pharma/Semiconductor/Medical, X Quality, RD&L, Intelligence, Intra Plant Logistics, APS); Mendix low-code personalization; Insights Hub pairing.
- MachineMetrics: Max AI; Connectivity Hub; Production Schedule Intelligence; machine-connector logo ecosystem.
- MachineMetrics' self-labeling as "MES" despite a monitoring-centered reality — treated as market-label noise, not a boundary datum.

## Vendor-specific Findings

See L3 above. Additionally: Tulip's documentation is the only sample with a fully explicit statement of the system-of-record split against ERP/MES (planning/BOM/inventory = ERP; frontline execution context = Tulip). L2L is the only sample whose FAQ explicitly addresses both "replace the MES?" and "replace the ERP?" questions. These are documented as product-specific statements, not Type properties.

## Boundary Findings

- **vs Manufacturing Execution System / MES (the critical seam).** Both live at the same layer and are frequently bundled (Siemens MOM portfolio contains MES as its engine; MM labels itself MES). The seam drawn from evidence: MES centers on *enforcing the execution of production orders against a process/routing definition and producing the as-built record* (eDHR/eBR, forward/backward traceability, work disposition) — that is what distinguishes Opcenter Execution's description. Factory Operations Management centers on *managing the running operation*: live state, events, cross-function response, and performance. In the suite pole FOM contains MES; in the connected-operations poles FOM either replaces a simple MES (L2L FAQ), coexists with an ISA-95-grade MES (L2L FAQ), or explicitly integrates with MES/ERP (Tulip). If you remove execution enforcement + as-built record, you still have factory operations management; if you remove live operations management, you still have an MES. Distinct Types, heavy market overlap. JOINT REVIEW recommended (the MES leaf is unprocessed at time of writing).
- **vs Shop Floor Management.** The event-and-response loop (L0 leg 2) is also Shop Floor Management's heart (dispatch, andon, visual management). The distinguishing increment for this Type: legs 1+3 — the production-operations record and live production state at machine/line/order grain, plus the positioning against ERP/control layers. A product can be Shop Floor Management without order/performance anchoring. JOINT REVIEW recommended (leaf unprocessed).
- **vs OEE Management Platform.** OEE measurement is common to 4/4 samples but is held as a standard capability here, not definitional; the OEE leaf keeps the measurement/effectiveness-analytics center (equipment effectiveness as the subject). 1+3 without 2 degenerates exactly into that neighbor.
- **vs Production Planning / APS.** Planning owns the forward plan; this Type consumes it and adapts execution to it (L2L "reschedule at the line level... as conditions shift" is the operations-side seam; Tulip explicitly declines planning). Suite poles bundle APS — bundling noted as packaging.
- **vs SCADA / HMI / DCS / PLC / Industrial Historian.** Those supervise and control machines and collect tag data; this Type manages operations (people + work + response + performance) above them, consuming machine signals via connectivity. Tulip's own docs (edge devices, OPC UA) and L2L's Machine Data Sync package show the consumption relationship.
- **vs Industrial IoT Platform.** IIoT is the connectivity/data substrate; the same integration packages appear here as consumers. MachineMetrics straddles the two markets, which is a product-level straddle, not evidence of Type identity.
- **vs CMMS / EAM.** Maintenance work management is one response class inside the operations loop; CMMS keeps the asset-care center. L2L bundles a CMMS module; Siemens ties maintenance to production ("production does not outpace maintenance requirements").
- **vs Manufacturing QMS / CAPA / Traceability.** Quality records, CAPA loops, and traceability systems are separate record types; here quality appears as events/checks feeding the response loop, with deep record-keeping delegated to the quality leaves.
- **"Remove what → becomes the neighbor" test:** remove the response loop → production monitoring / OEE platform; remove the production context and performance record → shop-floor issue/andon tool; remove live state → ERP/planning; remove the operations management entirely (keep enforcement + as-built) → pure MES; keep only machine data → IIoT/historian.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- Paper-era factory (mid-20th century): shift production boards showing output vs target, andon cords/lights (Toyota heritage; widely copied), downtime boards with coded reasons, tally sheets and shift logs, quality alert flags, tiered morning meetings with a performance board, supervisor dispatching maintenance/quality to the line. This satisfies all three legs: a live operational picture (boards per line/shift), an event-and-response loop (andon → responder → resolution), and an operational performance record (tally/downtime ledgers reviewed in meetings). The definition therefore does not depend on cloud, machine connectivity, or OEE arithmetic.
- Regional lean variants (andon-based systems in Japanese-heritage plants; visual-management-heavy European plants) fit the same core.
- The modern era adds machine-data automation of the same legs (automatic states, automatic OEE) — era-current capability, not definitional.

Conclusion: L0 passes the historical check; machine connectivity, OEE math, AI, and cloud delivery are held outside the defining core.

## Uncertainties

1. The enterprise-suite pole rests on one deep sample (Siemens). GE Vernova Proficy Plant Applications (the natural second sample) was unreachable (404 ×2); 42Q (mid-market cloud MES) returned empty responses ×2. Assertions about suite-pole structure are calibrated to Siemens evidence plus cross-pole consistency.
2. No independent standards text (MESA model, ISA-95) was fetched; the "between planning and control" layering is held on vendor statements (Siemens, L2L), which agree with each other but are vendor evidence.
3. MachineMetrics evidence is marketing-site-only; role/workflow depth for that pole is inferred from navigation and homepage copy, not operational docs. Its claims are used only for boundary triangulation.
4. Precise numeric claims in vendor marketing (e.g., L2L's "80% reduction in decision-making time", case-study percentages) were excluded from all canonical statements per evidence rules.
5. The exact market boundary between this leaf and Shop Floor Management will remain partly judgment-based until that leaf is researched; flagged for joint review rather than resolved unilaterally.
6. The leaf name ("Factory Operations Management") vs market label ("Manufacturing Operations Management / MOM"): treated here as one Type. No sampled vendor uses the exact phrase "factory operations management"; L2L and Siemens use "manufacturing operations management". This near-alias situation is recorded in STATUS.md rather than silently rewriting the directory.

## Final Synthesis

Factory Operations Management is the real-time operations layer of the factory: it holds the live operational picture of production (resources + running work + machine/operator-captured state), runs the event-and-response loop that turns disruptions into routed, standardized, tracked resolutions across maintenance/quality/materials/supervision, and maintains the operational performance record (OEE, downtime, throughput, yield per machine/line/shift/site) that closes the loop into improvement. It sits between ERP/APS (which own the plan) and SCADA/PLC (which own the machines), consuming the plan and machine signals, pushing actuals and statuses back up. The market realizes it in two dominant shapes — enterprise MOM suites whose engine is an MES (execution enforcement + as-built traceability), and connected/frontline operations platforms that manage the operation without MES-grade enforcement — which share the same defining core and differ chiefly in how much of execution they enforce. OEE analytics, machine connectivity, work instructions, scheduling, maintenance, quality modules, and AI are standard or optional capabilities of the Type, not its definition.
