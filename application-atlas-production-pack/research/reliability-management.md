# Research Notes — Reliability Management

## Research Goal

Understand what a "Reliability Management" application (§16, Engineering/Manufacturing/Industrial, sibling of EAM, CMMS, Calibration Management) actually is as a software Type: what objects it manages, what its users do, how failure knowledge becomes maintenance strategy, and where it starts and ends relative to CMMS/EAM (work management), OEE Management (production effectiveness), Product Test Management (durability testing of products), and the enterprise asset family.

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the reliability-engineering discipline software used by asset-intensive operators — failure data/analysis (MTBF, Weibull, bad actors), FMEA/FMECA, Reliability Centered Maintenance (RCM), PM optimization, maintenance strategy management.
- Prior-pass constraints recorded in STATUS.md:
  - EAM pass: "vs reliability-management (strategy layer consuming EAM data)"
  - CMMS pass: "reliability-management consumes CMMS data for strategy (predictive triggers inside a CMMS are an extension, not the discipline)"
  - Product Test Management pass forwarded flag: "durability tests planned/recorded here; reliability engineering there"
- Adjacent confusion risks: SRE Management (§14 — name collision, IT-domain), Incident Management (§14), Manufacturing QMS/CAPA (quality corrective action), Business Continuity/Operational Risk (§11).

## Research Questions

1. What is the unit of record — the failure event, the failure mode, the strategy, the analysis study?
2. What analysis machinery is definitional vs common (MTBF/Weibull/criticality/simulation/RBI)?
3. Where do strategies go — do products deploy into EAM/CMMS, and how?
4. Is the strategy loop (build → deploy → sustain) a stable cross-product structure?
5. Does the Type include product-design reliability (design FMEA, reliability growth, test-data analysis) or only in-service equipment?
6. What standards shape the domain (SAE JA1011/JA1012, MSG-3, MIL-STD-2173, API 580/581) and are they definitional?
7. Boundary: vs CMMS/EAM, OEE, Product Test Management, SRE Management.

## Representative Products

Selected for market representation + different product philosophy + different customer tier:

| Product | Vendor | Philosophy / pole | Customer tier |
|---|---|---|---|
| ReliaSoft suite (Weibull++, XFMEA, RCM++, XFRACAS, MPC, BlockSim, Lambda Predict) | HBK (HBM Prenscia) | reliability-engineering analysis toolkit | engineering teams, product + asset orgs, aerospace/O&G references |
| Reliability Workbench + Availability Workbench (RCMCost, AvSim) | Isograph | modeling/analysis suite with RCM + availability simulation, EAM portals | safety/reliability professionals, process & aerospace |
| Cordant Asset Strategy (ex ARMS Reliability OnePM) | Baker Hughes | asset strategy management (ASM): build/deploy/sustain reliability strategies at scale, EAM master-data deployment | large O&G/mining/utility operators |
| Newton™ suite (RDMS, Intelligence) | Pinnacle | data-driven reliability: ITPM/inspection data system + quantitative risk & availability modeling | refining/midstream/petrochemical |

Bentley Asset Performance Management (Meridium lineage — the classic enterprise APM/reliability suite) was attempted ×2 and timed out; recorded as a sourcing limitation. AVEVA APM URL 404.

## Sources

Fetched 2026-09-09 (all Tier-1/2 vendor surfaces; no help-center-level operational docs reachable for any product):

- HBK/ReliaSoft — software catalog page (reliability product list) — https://www.hbkworld.com/en/products/software/reliability (via /products)
- ReliaSoft RCM++ product page — https://www.hbkworld.com/en/products/software/reliability/rcm-reliability-centered-maintenance-software
- ReliaSoft XFRACAS product page — https://www.hbkworld.com/en/products/software/reliability/xfracas-failure-reporting-analysis-corrective-action-system-fracas-software
- Isograph Reliability Workbench — https://www.isograph.com/software/reliability-workbench/
- Isograph RCMCost module — https://www.isograph.com/software/availability-workbench/rcmcost/
- Isograph "Reliability Centered Maintenance" method page — https://www.isograph.com/software/availability-workbench/rcmcost/reliability-centered-maintenance/
- ARMS Reliability (Baker Hughes Cordant) landing — https://www.armsreliability.com/
- Cordant Asset Strategy product page — https://www.bakerhughes.com/cordant/applications/asset-performance-management/asset-strategy
- Pinnacle (Newton) home — https://www.pinnaclereliability.com/
- Pinnacle Newton RDMS — https://pinnaclereliability.com/newton-rdms/

Unreachable: bentley.com APM (timeout ×2 — abandoned per network rule), avea.com APM (404). Consequence: enterprise-APM-pole claims rest on three reachable products; no numeric/precise operational claims asserted anywhere.

## Product A — ReliaSoft (HBK)

### Key observations (Evidence layer A unless noted)

- Catalog positions the whole line as "Reliability Analysis and Management"; techniques named: life data analysis, FMEA, reliability growth.
- **Weibull++** — life data analysis software (failure-time data → distributions, MTBF-class quantities).
- **XFMEA** — FMEA software.
- **RCM++** — "facilitates the reliability centered maintenance (RCM) analysis approach to improve reliability of the assets and optimize maintenance planning. Supports all the major RCM industry standards, such as ATA MSG-3, SAE JA1011 and SAE JA1012." Capabilities: "design processes based on criticality and consequences," "easily create maintenance tasks by configuring equipment and categorizing failure effects," FMEA within or independent of RCM analyses, "compare the costs of potential maintenance strategies and estimate the optimum maintenance interval for preventive repairs/replacements with simulation-based calculations," predefined analysis-workspace profiles for major RCM/FMEA reporting standards.
- **XFRACAS** — "web-based Failure Reporting, Analysis and Corrective Action System (FRACAS)… incident/failure reporting, failure analysis on returned parts, part tracking for serialized systems, root cause analysis, team-based problem resolution and tracking the completion of assigned actions." "Closed-loop process" bridging individual failures and underlying problems. Data reuse: "Use data from XFRACAS for life data analysis or repairable system/reliability growth analysis in Weibull++. Share system configuration and failure modes data between XFRACAS and XFMEA / RCM++." Explicitly offered "as a Base Solution for Asset Performance Management"; API S53 (O&G) compliance mention; GE Aviation flight-safety use.
- **MPC** — MSG-3 maintenance program creator for aircraft (aviation-industry wrapper on the same machinery).
- BlockSim (system reliability/availability/maintainability RAM), Lambda Predict (standards-based reliability prediction).
- Structure visible: failure events (XFRACAS) → life-data analysis (Weibull++) → failure-mode analyses (XFMEA/RCM++) → maintenance tasks/strategies. Same failure-mode data shared across analysis modules. This is the analysis→strategy chain as a product architecture.

## Product B — Isograph (Reliability Workbench / Availability Workbench)

### Key observations

- **Reliability Workbench** modules: Prediction (MIL-217, 217Plus, SN29500, IEC 61709, FIDES, Telcordia, NSWC…), FMECA (MIL-STD-1629A, AIAG & VDA, SAE J1739, ARP5580…), RBD, Fault Tree, Event Tree, Weibull, Markov, Reliability Growth, Reliability Allocation, System Safety Assessment, Parts Libraries, Enterprise System (security-controlled project/library environment).
- **Availability Workbench** modules: RCMCost (RCM), AvSim (availability simulation), Weibull, Life Cycle Cost, Process Reliability, **SAP Portal**, **Maximo Portal**, Accelerated Life Testing.
- **RCMCost**: "implements the Reliability Centered Maintenance (RCM) procedure for determining maintenance strategies based on reliability techniques and encompasses… FMECA." Objectives: minimize costs, meet safety/environmental goals, meet operational goals.
- RCM process description (method page): "The RCM process begins with a failure mode and effects analysis (FMEA) that identifies the critical plant failure modes in a systematic and structured manner. The process then requires the examination of each critical failure mode to determine the optimum maintenance policy…" Strategy accounts for "cost, safety, environmental and operational consequences… redundancy, spares costs, maintenance crew costs, equipment aging and repair times." "Once optimal maintenance policies have been recorded the RCM process provides system performance predictions and costs, expected spares requirements and maintenance crew manning levels. **The RCM process may be used to develop a living strategy with the plant model being updated when new data is available or design changes take place.**"
- Standards: SAE JA1011, MSG-3, MIL-STD-2173(AS); RCM decision diagrams "provide a logical process for workgroups to determine what type of maintenance strategy to adopt for a given failure cause"; simulation of "preventive tasks, inspection tasks and condition monitoring."
- **EAM/CMMS seam (vendor-explicit)**: "Connect directly to your SAP or MAXIMO system and download your current maintenance plans and performance data for analysis and optimization." — the failure/performance data substrate and the deployment target both live in the EAM/CMMS.
- Cross-product commonality note: the "living strategy" (leg 3) appears verbatim here and structurally in Cordant's Sustain.

## Product C — Cordant Asset Strategy (ARMS Reliability / Baker Hughes; ex-OnePM)

### Key observations

- ARMS Reliability self-description: reliability consulting, software (OnePM), training in RCM, Maintenance Strategy Optimization, RAM Analysis, RCA. OnePM "establish[ed] a best-practice approach for developing, deploying, and sustaining justified maintenance strategies at scale." Now Cordant™ Asset Strategy — "asset strategy management, defect elimination, and asset performance management."
- Product page framing: "Improve asset performance and productivity with optimized maintenance strategies at scale." "Without a structured approach to managing industrial asset reliability strategies, even the most thorough, systematic monitoring of asset health is fundamentally tactical…"
- **ASM = Build / Deploy / Sustain**:
  - Build: "Build and structure reliability strategies that drive accurate modeling of performance, cost, and risk-optimized scenarios. Consolidate, structure and augment asset models to develop optimal strategies for each equipment type, for a given criticality."
  - Deploy: "Group maintenance tasks using your business rules for effective planning, scheduling, and execution. **Generate EAM system compliant master data ready for direct electronic implementation.**"
  - Sustain: "Reliability strategies keep pace with operational requirements while evolving over time to reduce risk and cost… quickly respond to changes with workflow engine for review and approval." — strategy governance (review/approval workflow).
- "Connects strategy with asset health and work execution" — the suite's own boundary statement: strategy (this product) sits between health monitoring (Cordant Asset Health) and work execution (the EAM/CMMS).
- Equipment knowledge base / strategy libraries: "A generic equipment knowledge base completes your Master Data; where there is far less complexity and disparity between like equipment type strategies."
- Governance leg: "close the gap between the forecasted and actual performance of agreed strategies" — forecast vs actual loop.
- Sibling applications in same suite: Asset Health, Asset Defect Elimination, Asset Integrity. Services menu: RAM Analysis, Maintenance Strategy Development/Optimization, Life Cycle Costing, Spare Parts Analysis, Availability and Capacity Analysis.
- Case-study numbers (marketing evidence only — do not promote): "5–10× more efficient… building maintenance strategies," "$135 MM saved… LNG," "700,000+ asset tactics developed in 14 weeks for water utility."

## Product D — Pinnacle (Newton™)

### Key observations

- Positioning: "Data-Driven Reliability"; lens = **Data Collection → Data Organization → Intelligence → Strategic Decisions**. Newton answers "What happens if this compressor blows?" or "Can I push this inspection?"
- **Newton RDMS** — "transforms your ITPM data into a powerful tool"; "the only tool you need to manage all your inspection, test and preventative maintenance work processes"; "a better system of record for your ITPM data than Excel." Features: Inspection Management, Non-conformances, Data uploads; **Risk Based Inspection** ("Based on API 580 and 581… semi-quantitative risk models with an exceptional library of strategy rules"), Inspection Planning, **Strategies Library**; Thickness Locations/Inspections/Evaluations (corrosion rates, remaining life); **Asset Registry**, Equipment templates, Inspection/Event templates.
- Suite capability matrix (APM capability per Verdantix): Asset Register/Data (flexible asset hierarchy); Task Tracking and Inspection Data Management; API 580 RBI; **RCM and Maintenance Optimization** ("Use Reliability-Centered Maintenance (RCM) for improved asset performance"); CMMS Integration; Open Data Reporting with Power BI; Advanced Risk Modeling (quantitative PoF/CoF, "better Asset Failure Prediction") [Intelligence]; Throughput Modeling with Business Intelligence ("Live Facility Availability Modeling for performance forecasting") [Intelligence]; Full Stack Facility Optimization (what-if scenarios, CML/task optimization, spare parts, capital projects) [Intelligence]; Advanced Reliability Operating Windows ("connect operational data to predict asset reliability") [Intelligence].
- Newton Intelligence: "shows you the impact your decisions will have on the performance, availability, risk and cost of your facility."
- Industries: refining, midstream, petrochemical, mining, water — asset-intensive process industries.
- Note: this pole shows the **integrity/inspection (RBI) domain riding inside the same suite** — fixed-equipment integrity machinery (thickness, corrosion, RBI per API 580/581) alongside RCM/strategy machinery.

## Cross-product Comparison

| Structure | ReliaSoft | Isograph | Cordant ASM | Pinnacle Newton | Verdict |
|---|---|---|---|---|---|
| Equipment/failure-mode records bound to identified equipment | XFRACAS incidents + XFMEA/RCM++ failure-mode worksheets sharing "system configuration and failure mode data" | FMECA module; RCMCost FMECA data; fault trees/RBDs over system structure | asset models per equipment type; equipment knowledge base; asset registry lineage (OnePM) | Asset Registry with equipment hierarchy/templates; failure/inspection data as system of record | **Defining core** (realization differs: recorded failure events vs authored failure-mode analyses vs knowledge libraries) |
| Failure/consequence evaluation machinery | criticality + consequences; life data analysis; simulation of intervals; reliability growth | FMECA criticality; Weibull; AvSim simulation; importance analysis | "accurate modeling of performance, cost, and risk-optimized scenarios"; criticality-scoped strategies | semi-quantitative RBI models; quantitative PoF/CoF; availability forecasting | **Defining core** (analytical depth is a variant axis: judgment-criticality → statistical → simulation → quantitative risk) |
| Maintenance-strategy decisions as managed artifacts | RCM++ maintenance tasks, strategy cost comparison, optimum interval | RCMCost "optimal maintenance policies… recorded"; decision diagrams per standards; LCC | "justified maintenance strategies" as the central managed artifact; strategy libraries | Strategies Library; inspection plans; task optimization | **Defining core** |
| Strategy deployment to the maintenance program (EAM/CMMS) | XFRACAS "base solution for APM" (integration posture) | SAP Portal / Maximo Portal: download maintenance plans + performance data; upload optimized plans | "EAM system compliant master data ready for direct electronic implementation"; connects to "work execution" | "CMMS Integration" | **Common mature structure** (postures differ; all four show the seam) |
| Living-strategy governance loop (revise as data/operations change) | XFRACAS closed-loop corrective action; data feeding back into analyses | "living strategy with the plant model being updated when new data is available" | Sustain: workflow review/approval; forecast-vs-actual | Intelligence what-if; task optimization revisits; "strategic decisions" lens | **Defining core** at moderate abstraction (all four carry revision-in-light-of-data; governance workflow depth varies) |
| Failure-event capture workflows (FRACAS-style reporting) | XFRACAS (first-class) | relies on EAM data via portals | defect elimination sibling; failure history via EAM | inspection findings/non-conformances in RDMS; ITPM data | Common, NOT definitional (capture may live in CMMS/EAM/QMS) |
| Life-data statistics (Weibull/MTBF) | Weibull++ | Weibull modules | implicit in "financially optimized" strategies | "Advanced" tier (PoF models) | Common, NOT definitional (judgment-based RCM exists in-sample without it) |
| System modeling (RBD/fault tree/availability simulation) | BlockSim | AvSim, RBD, FaultTree | performance/cost/risk scenario modeling (abstract) | Throughput/availability modeling | Common-optional (engineering-depth pole) |
| Standards wrappers (SAE JA1011/1012, MSG-3, MIL-STD-2173) | RCM++ profiles; MPC (MSG-3) | RCMCost; Reliability Workbench safety modules | "justified" strategies (audit posture) | API 580/581 RBI | Common/variant (industry-dependent; standards shape reporting, not the record structure) |
| Inspection/integrity machinery (RBI, thickness, corrosion) | – | – | Asset Integrity sibling app | Newton RDMS center | Variant/adjacent (integrity pole; no separate directory leaf) |
| Condition/health telemetry ingestion | – (via HBK monitoring line, separate) | condition monitoring simulated in RCMCost | Cordant Asset Health sibling | Reliability Operating Windows (connect operational data) | Optional; substrate relationship |
| Defect elimination / RCA programs | XFRACAS root cause analysis; corrective actions | – | Asset Defect Elimination sibling | non-conformance workflows | Common-optional |

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The equipment failure knowledge of record** — persistent, failure-mode-structured records bound to identified equipment/functions (a hierarchy of equipment with functions and the ways each fails), fed by the plant's own failure events/inspection findings and/or authored engineering analysis (FMEA/FMECA/RCM worksheets) and/or equipment knowledge libraries. Remove → an asset registry (no failure semantics) or a plain work-order log.
2. **Failure evaluation** — the failure knowledge is analyzed and compared: criticality/consequence assessment, failure behavior over time, cost/risk of failure, ranking of what matters. Depth is a variant axis (expert-judgment criticality at one pole; life-data distributions, availability simulation, quantitative risk models at the other). Remove → an unanalyzed logbook / data store.
3. **The strategy loop** — evaluation resolves into maintenance-strategy decisions held as managed, revisable artifacts: which task on which failure mode, at what interval, at what cost/risk justification; deployed as the maintenance program (commonly as EAM/CMMS-consumable master data/plans); governed and revised as new failure data and operational context arrive. Remove → analysis that never changes how anything is maintained (a statistics toolkit), or maintenance planning with no failure basis (CMMS/EAM territory).

Jointly-held check: 1 alone = failure log/registry; 2 without 1 = statistics on nothing; 3 without 1+2 = generic maintenance planning; 1+2 without 3 = reliability analytics toolkit (analysis that doesn't manage); 1+3 without 2 = arbitrary strategy (strategy without a basis ceases to be the discipline — in practice the analysis leg reappears at judgment depth); 2+3 without 1 = strategy machinery evaluating nothing anchored to equipment.

### L1 — Common Mature Structure

- EAM/CMMS integration in both directions (consume failure/work history; emit strategies/master data)
- Life-data analysis (Weibull-class distributions, MTBF/failure-rate metrics)
- RCM/FMEA analysis worksheets with standards profiles (SAE JA1011/JA1012, MSG-3, MIL-STD-2173-class decision logic)
- Criticality/risk ranking of equipment and failure modes
- Failure-event/corrective-action capture (FRACAS-style loops)
- Cost-of-failure / life-cycle-cost and PM-interval optimization (often simulation-based)
- Strategy libraries / equipment knowledge bases shared across sites
- Reporting/review outputs for engineering and management audiences

### L2 — Variant / Optional Structure

- Analytical depth: judgment-criticality → statistical life data → availability simulation → quantitative risk modeling (PoF/CoF)
- Subject scope: in-service plant equipment (center) vs product-design reliability work (design FMEA, reliability growth, test-data analysis) served by the same tool family
- Integrity pole: RBI/thickness/corrosion machinery (API 580/581) riding inside the suite
- Industry standards wrappers: MSG-3 (aviation), API S53 (O&G), AIAG & VDA (automotive FMEA) — reporting shapes, not structure
- Capture substrate: own FRACAS/incident modules vs CMMS/EAM-sourced history vs inspection data systems
- Governance depth: library versioning + review/approval workflows (large operators) vs desktop analysis files
- Cloud platform vs desktop workbench
- Condition/health telemetry ingestion, AI/predictive layers (era-current)

### L3 — Vendor-specific (research notes only)

- ReliaSoft: product names Weibull++/XFMEA/RCM++/XFRACAS/MPC/BlockSim/Lambda Predict; ReliaSoft Cloud; GE Aviation flight-safety usage claim; API S53 claim
- Isograph: RCMCost/AvSim naming; "1,900 companies, 12,000 sites, 75 countries" claim; software certifications with SAP, IBM partnership
- Cordant/OnePM: Build/Deploy/Sustain labels; "5–10× faster strategy builds," "$135 MM," "700,000+ tactics in 14 weeks" case claims; Cordant suite siblings (Asset Health/Defect Elimination/Integrity)
- Pinnacle: Newton/RDMS/Intelligence naming; "Reliability Operating Windows"; Power BI open-data reporting; Verdantix APM-capability framing; "$800K CML optimization," "94.22% availability" case claims
- Bentley (Meridium lineage) APM — unreachable this pass

## Vendor-specific Findings

- Only Cordant makes the strategy artifact itself the explicitly named center ("asset strategy management") — but Isograph's "optimal maintenance policies… recorded" + "living strategy," ReliaSoft's task/interval decisions, and Pinnacle's strategies libraries show the same structure unnamed. Treat "strategy as managed artifact" as canonical, the ASM branding as vendor framing.
- Only Pinnacle centers inspection/integrity (RBI) data — integrity pole is a variant, consistent with the directory having no separate RBI leaf.
- Only ReliaSoft productizes a dedicated FRACAS module; failure-event capture is commonly the CMMS's/EAM's job — supports keeping capture out of L0.

## Boundary Findings

- **vs CMMS / Maintenance Management & EAM** (prior passes' constraint honored from this side): CMMS/EAM = asset register + work orders + history (the execution system); Reliability Management = the failure/strategy discipline that consumes that history and emits strategies back (Isograph portals named SAP/Maximo explicitly; Cordant ships "EAM-compliant master data"; Pinnacle lists "CMMS Integration"). Removal tests: strip work-order execution from a reliability product and it survives (all four in-sample do not execute work); strip analysis/strategy from an EAM and it survives (recorded by the EAM/CMMS passes).
- **vs OEE Management Platform** (processed 2026-09-09, no reliability seam recorded there): OEE centers a production-effectiveness measure (A×P×Q + loss attribution + improvement loop on output); Reliability centers failure behavior and maintenance strategy (what fails, why, what to do about it). Downtime events may feed both. Removal tests: remove the OEE accounting model from reliability machinery → survives; remove failure-mode/strategy machinery from an OEE platform → survives.
- **vs Enterprise Asset Registry** (§10): registry = static identified-asset records; reliability = the discipline loop over failure knowledge; the registry/hierarchy is substrate inside reliability products (Pinnacle Asset Registry, Cordant asset models).
- **vs Product Test Management** (forward flag from that pass): Product Test Management plans/records/verifies tests of engineered products against requirements; Reliability Management analyzes failure and decides maintenance strategy for operating equipment. Bridge: durability test data and design-reliability analyses (life data analysis, design FMEA) are shared tool family — ReliaSoft explicitly serves both worlds. The §16 leaf's center is the in-service/maintenance loop; design-reliability usage is a variant context, not the defining center.
- **vs Aircraft Maintenance Management** (processed 2026-09-06; reliability analytics held L1 there): the aviation MSG-3 maintenance-program build (ReliaSoft MPC exists for exactly this) is the aviation-industry realization of the same strategy loop; aircraft type keeps its own airworthiness spine. Domain variant, never merged.
- **vs SRE Management (§14, processed 2026-09-09)**: pure name collision. SRE = reliability objectives/SLOs/error budgets for IT services; this Type = physical equipment failure and maintenance strategy. Never merge.
- **vs Manufacturing QMS / CAPA**: quality system of record for product conformity vs equipment reliability; XFRACAS itself notes the CAPA acronym family overlap (corrective-action mechanics shared), but the managed object differs (product defects vs equipment failure modes/strategies). Note for future QMS passes.
- **vs Incident Management (§14)** / **Cyber Incident Response (§15)**: response-workflow Types over service/security events; different objects, different loop.
- **vs Industrial Historian / IIoT / Digital Twin**: telemetry substrate; reliability products consume condition data (Pinnacle "Reliability Operating Windows," RCMCost simulates condition-monitoring tasks) but do not center device connectivity.
- **vs Business Continuity / Operational Risk (§10/§11)**: organization-level risk process vs engineering discipline on physical failure modes.

## Historical / Market-Sample Check (§24)

Paper-era reliability programs satisfy all three L0 legs with no modern machinery: airline/plant failure logbooks and FRACAS forms (leg 1), Weibull probability paper + MTBF/Pareto calculation + RCM decision worksheets (Nowlan & Heap, 1978; MSG-1/2/3 from the 1960s) (leg 2), and the resulting living maintenance program revised on new failure experience (leg 3). Platform-native/older products (desktop Weibull tools, spreadsheet strategy builds) also fit — cloud, portals, libraries, and AI are era-current, not definitional. Historical check: **passed**.

Market-structure note: the market's umbrella label for the broader suite space is "Asset Performance Management (APM)" (ReliaSoft markets XFRACAS "as a base solution for APM"; Pinnacle maps Newton to a "traditional APM" checklist; Cordant positions inside APM). The directory has no APM leaf; Reliability Management is the leaf, and the reliability core (failure knowledge + evaluation + strategy loop) is the stable structure across APM-branded suites. Recorded as a naming/market note, no directory change.

## Uncertainties

- Bentley/Meridium-lineage enterprise APM not directly evidenced (fetch failed ×2); its inclusion in "Common" rows rests on the three reachable poles' convergence plus Cordant/Pinnacle positioning statements. Assertion strength kept moderate accordingly.
- No Tier-1 help-center-level operational documentation was reachable for any sampled product (all evidence is product/method pages). Consequently: no numeric limits, defaults, or precise workflow rules asserted in the final document.
- Whether a "pure" strategy-management product can exist without any analysis module was not directly observed; in-sample, analysis always exists at some depth (at minimum criticality ranking). L0 phrased to absorb this (analysis at judgment depth).
- Depth of strategy-governance workflow (approval routing, versioning) varies; evidenced explicitly only at Cordant — held as common-at-enterprise-pole, not definitional.

## Final Synthesis

Reliability Management is the reliability engineer's discipline system for an equipment population: it holds what is known about how the operator's equipment fails (failure modes bound to equipment/functions, fed by failure events, inspections, and engineering analysis), makes that knowledge comparable and decision-ready (criticality, consequence, cost, failure behavior — at any analytical depth), and resolves it into maintained, justified maintenance strategies that are deployed to the maintenance program and revised as new experience arrives. The strategy loop is what makes it "management" rather than analysis; the failure-mode record is what makes it reliability rather than generic planning; the evaluation machinery is what connects them.
