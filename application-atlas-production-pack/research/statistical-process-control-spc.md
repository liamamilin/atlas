# Research Notes — Statistical Process Control / SPC

Research date: 2026-09-09
Slug: statistical-process-control-spc
Leaf: Statistical Process Control / SPC (DIRECTORY.md §16 Engineering, Manufacturing & Industrial)

## Research Goal

Understand what a Statistical Process Control application actually is as a software Type: what objects organize its world, what its defining statistical content is, how the monitor→signal→respond loop works, which capabilities are definitional vs merely common, and where its boundaries run against the many neighboring quality/manufacturing Types in §16 (Manufacturing QMS, CAPA, Inspection & Metrology, MES, Industrial Historian, SCADA, HMI, OEE, Calibration Management, Shop Floor Management).

## Initial Boundary (hypothesis before research)

- SPC is the application that monitors process variation over time using control charts whose limits are computed from the process's own data, distinguishing common-cause from special-cause variation and signaling when a process becomes statistically unpredictable.
- Most likely confusions:
  - vs Inspection & Metrology Software — both consume measurements, but IM judges a part instance against nominal geometry; SPC judges process behavior over time.
  - vs Industrial Historian — both store time-ordered process data; historian archives raw telemetry, SPC applies statistics and reaches a state judgment.
  - vs MES / Manufacturing QMS — both sit in quality machinery; MES executes orders, QMS holds quality records; SPC is the statistical monitoring layer.
  - vs general statistics software — control charts are one procedure among many there; SPC products center the ongoing monitoring loop.
  - vs BI dashboards — generic metrics vs process-behavior statistics.
- Unknowns going in: whether capability analysis (Cp/Cpk) is definitional or common; how vendors structure the response-to-signal workflow; how spec limits are positioned relative to control limits; how automatic data collection is realized.

## Research Questions

1. What are the core objects (part, process, feature/characteristic, subgroup, chart, limits, rules, alarms, capability)?
2. How does data collection work — manual entry at a station, gauge/device integration, automatic machine data, timed collection?
3. What defines an out-of-control signal, and what happens after one (response workflow, assignable causes, corrective actions)?
4. How are control limits set and recomputed (initial study, "sufficient subgroups", staging, recalculation after process change)?
5. Where do specification limits sit — reference overlay? Are they definitional?
6. Where does capability analysis (Cp/Cpk/Pp/Ppk) sit — definitional or common?
7. What interfaces do operators vs engineers vs managers get?
8. What different philosophies exist across the market (specialist real-time products, analysis suites, cloud platforms, Excel add-ins, QMS-embedded modules)?
9. What is invariant across paper-era and modern implementations (historical/market-sample check)?
10. What are the exact seams with the neighboring §16 Types?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tier:

1. **Minitab (Minitab Statistical Software)** — analysis-suite heritage; SPC as a statistical procedure set inside a general quality/statistics package; world-class official help documentation. Mid/large quality organizations; also individual analysts.
2. **InfinityQS Enact** (cloud; vendor of the on-prem ProFicient line) — dedicated SPC/quality-intelligence specialist, cloud data-stream model, multi-site enterprise. Publicly reachable Enact help center (enacthelp.infinityqs.com).
3. **WinSPC (DataNet Quality Systems)** — real-time, operator-facing shop-floor SPC for Windows; deep device/gauge integration and configurable trigger/OCAP machinery; extensive public knowledgebase.
4. **QI Macros (KnowWare International)** — Excel add-in philosophy; template/wizard-driven SPC at the low end of the market (individual/small customers).
5. **Siemens Opcenter Quality / Opcenter X Quality** — SPC as a module embedded in an enterprise QMS/MOM suite; inspection-plan/order-driven acquisition; escalation into nonconformance management. Tier-2 evidence only (product pages/official blog; operational help behind support portal).

## Sources

Tier 1 (official operational documentation, directly fetched or officially indexed):

- Minitab Support (support.minitab.com):
  - Understanding control charts — https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/control-charts/supporting-topics/basics/understanding-control-charts/ (fetched 2026-09-09)
  - Variables control charts in Minitab — .../supporting-topics/understanding-variables-control-charts/variables-control-charts-in-minitab/
  - Types of data for control charts — .../supporting-topics/data/types-of-data-for-control-charts/
  - Using tests for special causes — .../supporting-topics/basics/using-tests-for-special-causes/
  - Set control limits and center lines — .../supporting-topics/options/set-control-limits-and-center-lines/
  - All statistics and graphs for Xbar Chart — .../how-to/variables-charts-for-subgroups/xbar-chart/interpret-the-results/all-statistics-and-graphs/
- InfinityQS Enact Help Center (enacthelp.infinityqs.com):
  - Control Limits — https://enacthelp.infinityqs.com/en-us/ControlLimits/IntroControlLimits.htm (fetched 2026-09-09)
  - Managing Control Charts — https://enacthelp.infinityqs.com/en-us/Tiles/ManagingCCTiles.htm
  - Managing Run Chart Dashboards — https://enacthelp.infinityqs.com/en-us/Dashboards/ManagingRunChartDashboards.htm
  - Managing Dashboards — http://enacthelp.infinityqs.com/en-us/Dashboards/ManagingDashboards.htm
  - Creating Processing Templates — https://enacthelp.infinityqs.com/en-us/ProcessingTemplates/CreatingProcessingTemplates.htm
  - Configuring Global Settings — https://enacthelp.infinityqs.com/en-us/GlobalConfiguration/ConfiguringGlobalSettings.htm
- WinSPC Knowledgebase (knowledgebase.winspc.com):
  - What Subgroup Level Control Tests come preconfigured with WinSPC? — https://knowledgebase.winspc.com/questions/315 (fetched 2026-09-09)
  - What is the difference between a Subgroup Level Control Test and a Sample Level Control Test? — https://knowledgebase.winspc.com/questions/86
  - Category pages: WinSPC Data Collection, WinSPC Collection Plans, WinSPC Control Tests Templates/Triggers, WinSPC Part/Process Setup, WinSPC Plant Monitor
  - What do the different colors in Control Charts and Plant Monitor mean? — https://knowledgebase.winspc.com/questions/319
- QI Macros (qimacros.com, official pages):
  - Control Chart Template — https://www.qimacros.com/control-chart/control-chart-template/
  - Which Template Should You Use? (wizard) — https://www.qimacros.com/control-chart/control-chart-template-wizard/
  - Fixed Limit Template — https://www.qimacros.com/control-chart/control-chart-template-fixed-limits/
  - How To Guide (PDF) — https://www.qimacros.com/pdf/qi-macros-how-to-guide.pdf

Tier 2 (official product positioning; used for scope/positioning only):

- Siemens Opcenter blog: Streamline statistical process control with Opcenter Quality — https://blogs.sw.siemens.com/opcenter/boost-statistical-process-control/
- Opcenter X Quality product pages — https://www.siemens.com/en-us/products/opcenter/quality-x-cloud-qms/ (and /essentials/), https://resources.sw.siemens.com/en-US/fact-sheet-opcenter-x-quality/

Neighbor passes consulted for seams (STATUS.md / prior research notes):

- inspection-metrology-software, manufacturing-execution-system-mes, industrial-historian, hmi, scada, oee-management-platform, capa-management, calibration-management, life-sciences-qms, shop-floor-management, manufacturing-traceability.

## Product Observations

### Minitab (Minitab Statistical Software) — evidence layer A (official help, fetched)

- Control chart defined as "graphs that plot your process data in time-ordered sequence" with center line (process mean), UCL/LCL representing process variation, limits "by default … at distances of 3σ above and below the center line".
- Purpose framing: "indicates when your process is out of control and helps you identify the presence of special-cause variation. When special-cause variation is present, your process is not stable and corrective action is necessary."
- In-control = points fall randomly within limits (common-cause only); out-of-control = points beyond limits or nonrandom patterns (special cause).
- Use cases listed: demonstrate stability over time; **verify stability before capability analysis — "A capability analysis is only valid when performed on a stable process"**; assess effectiveness of a process change; communicate performance over a period.
- Chart taxonomy: variables charts for subgroups (Xbar, R, S, Zone; combinations Xbar-R/Xbar-S/I-MR-R/S), variables charts for individuals (I, MR; I-MR), attribute charts (p/np/c/u — binomial and Poisson data), multivariate charts (correlated variables e.g. temperature+pressure), rare-event charts (time/opportunities between events), time-weighted charts (points not independent).
- Tests for special causes: tests 1–8 (point > 3σ; 9 points one side; 6 trending; 14 alternating; 2-of-3 > 2σ; 4-of-5 > 1σ; 15 within 1σ [stratification]; 8 > 1σ [mixture]); tests user-selectable with configurable parameters (e.g., limits at 2.5σ); only test 1 on time-weighted charts; tests 1–4 on attribute/R/S/MR charts.
- Limits: user can enter mean/σ per stage; stages support "historical control chart" showing process change over periods, limits recalculated per stage; option to assume equal subgroup sizes for straight limits.
- Capability analysis exists as a separate capability area (histogram, indices) predicated on stability.
- Observation: this is analysis-first SPC — data typically exist as worksheet columns; no shop-floor data collection station; no alarms/triggers; charts are produced on demand from data.

### InfinityQS Enact — evidence layer A (official help center, fetched)

- Control chart: "graphical display of a feature that has been measured or computed from a sample versus the sample number or time"; center line = mean; UCL/LCL; "If nearly all of the sample points fall between the control limits, you can consider the process to be in-control."
- **Control Limits page (fetched, load-bearing):** "control limits are calculated from collected data, showing how the process is performing" ("Voice of the Process"). "After collecting a sufficient number of subgroups, you should set the control limits, which stores their values in Enact." Enact auto-updates control limits (every 10 minutes — vendor-specific mechanism detail, L3).
- **"Control limits have no relationship to the specification limits, and must never be calculated from specification limits."**
- In-control ≠ in-spec explicitly: a process can be "in-control but outside of specification limits, meaning the parts being manufactured are consistently bad"; and out-of-control while in spec ("parts might be acceptable, but there is no way of ensuring they will remain that way").
- Chart header context: Feature, Units, Part, Process, Shift, Lot — the data-stream identity model is Process → Part → Feature (+ organizational rollups, drift-down through Division→…→levels in bubble charts).
- Plot point states: Normal, Out of Specification (OOS), Out of Control (OOC), both, Inactive (disabled subgroups can be removed from control limit and Cp/Cpk calculations).
- Manufacturing limits vocabulary on variable charts: USL/Tar/LSL plus warning limits (UWL/LWL), within-piece limits, subgroup limits, reasonable limits — spec-family limits shown as reference lines, statistically derived limits computed separately.
- Statistics panel: Cp, Cpk (short-term), Pp, Ppk (long-term), yield; attribute charts: total defects/defectives, total pieces.
- Variable vs attribute charts: u chart plots defects-per-subgroup-size ratio; p chart plots defectives ratio.
- Data collection: "data collections (timed and manual)" opened from dashboards; raw vs aggregated dashboards; Stream Summary tile prioritizing data streams with OOS pieces and OOC subgroups; run chart dashboards per process-part-feature stream with spec limits and event counts (specification limit violations and statistical violations).
- Processing templates: standardized charts (plot in σ units, combine dissimilar data on one chart), Tabular/Shewhart CUSUM, Economic Control Limit (ECL) with Target Cp — advanced chart engines (L2/L3).
- Observation: this is the cloud quality-intelligence pole — persistent data streams, live events, dashboards, multi-site rollups. The monitoring loop is product-centered; analysis happens through tiles/reports, not statistical worksheet sessions.

### WinSPC (DataNet Quality Systems) — evidence layer A (official knowledgebase, fetched)

- Object model: Part/Process tree; Collection Plans (steps = variables/attributes to collect); Devices (serial gauges, ODBC/Excel devices, OPC, timed prompting of devices or operators); Stations and Users; Lists; Blueprints (pictorial operator aids for data collection).
- Data collection is the core mode: operator at a station enters/pulls readings; subgroup = one or more samples forming a plotted point (subgroup size configurable); sample = individual reading.
- Control tests ("rules") in two levels: Subgroup Level Tests (executed when a subgroup is added to the chart) and Sample Level Tests (executed per reading — out of engineering/spec limits; out of reasonable limits).
- Preconfigured subgroup tests organized in families — Shewhart, Western Electric (AT&T), Nelson — with zone definitions (Zone A/B/C), run/trend syntax: 1 point beyond limits/Zone A; 2-of-3 in Zone A+; 4-of-5 in Zone B+; 8–9 points one side; mixture (8 points both sides none in Zone C); stratification (15 in Zone C); trends (6 increasing/decreasing/steady); custom tests possible.
- Triggers on test violation: message box, email, log, file, reject reading, prompt for password, **prompt for Assignable Causes / Corrective Actions / Notes**, serial message, DDE/OPC write, start external program — the OCAP (out-of-control action plan) surface is configurable machinery.
- Color/severity semantics across Data Collection, Plant Monitor, Reports: red = out-of-control; purple = mixture/stratification; yellow = trend; green = no violation; grey = no data; "the cell or subgroup color will always indicate the highest severity level" but all violated rules are recorded in the database.
- Plant Monitor: station-level status grid of characteristics (colored cells) — a live shop-floor status surface.
- Reporting/analysis: Report Builder, Report Books, Datasets, Query Tool, Dashboards, QualTrend (separate analytics product), Variable Analyzer; capability report present.
- Timed data collection: prompt a device to send a reading or prompt the operator at intervals/specific times.
- Observation: this is the real-time shop-floor pole — SPC as a live production activity with operators, devices, prompts, and recorded responses.

### QI Macros (KnowWare International) — evidence layer A/B (official product + help pages)

- Philosophy: Excel add-in; SPC delivered as templates ("drop your data into the yellow shaded input area and the charts are drawn automatically") plus wizards.
- Control chart templates for attribute (c, np, p, u) and variable (XmR, XbarR, XbarS, Levey Jennings) charts and specialized charts; templates "perform stability analysis"; red points represent "unstable conditions that should be investigated".
- Control limit calculation options per template: Default (center line = average), Median, **Fixed (limits defined by user, e.g., evaluate a batch run against historical control limits)**, Short Run (DNOM), Real Time XbarR (parses gage data into subgroups), small-sample p.
- Control Chart Wizard/Template Wizard analyzes data shape (integers vs decimals, columns count, constant vs varying sample) and picks the chart (c/np/p/u/XmR/XbarR/XbarS); variable charts also produce histogram, capability plot, probability plot.
- Capability: histograms with Cp/Cpk, Capability Suite positioned as a core feature ("determine if your process meets your customer's requirements as defined by upper and lower specification limits"); includes "the same charts as Minitab's Capability Sixpack" (vendor claim).
- Gage R&R/MSA included (measurement-error analysis) — adjacent capability bundled.
- Observation: the minimal pole — no station, no devices, no live monitoring, no events; SPC as charting + stability + capability analysis over spreadsheet data. Customer tier: individual/small teams. Yet the statistical content is the same: time-ordered data, control limits, stability tests, capability.

### Siemens Opcenter Quality / Opcenter X Quality — evidence layer B/C (official blog + product pages; operational docs behind portal)

- SPC positioned as a module of the QMS: "The SPC module documents relevant inspections carried out within the product manufacturing process."
- Inspection-order workflow: inspection orders created from released inspection plans, allocated to acquisition stations; results collected via sampling, manually or with gauges for variable characteristics; batches/lot numbers acquired as context; values visualized in charts ("single value, control, and Pareto analysis").
- Deviation handling: "After identifying defects, tolerance issues, or process violations, causes, actions, and complaints can be acquired"; escalation to Opcenter Quality Concern and Complaint Management (CCM) or Teamcenter Quality for root-cause analysis — the QMS-embedded seam.
- Opcenter X Quality page: "Provide real-time quality feedback to operators, display SPC charts as data is collected"; "Automate violation-triggered actions"; "Continuously monitor process conditions, perform historical analysis"; AI-determined distribution + control limits compared to tolerance limits.
- Observation: SPC exists inside a quality suite, embedded in the inspection planning/acquisition workflow; the statistical machinery is not documented publicly at operational depth — assertions kept general for this product.

## Cross-product Comparison

| Aspect | Minitab | Enact | WinSPC | QI Macros | Opcenter Quality |
|---|---|---|---|---|---|
| SPC posture | analysis suite chapter | cloud quality-intelligence platform | real-time shop-floor application | Excel add-in templates | QMS/MOM suite module |
| Data organization | worksheet columns → charts on demand | process→part→feature data streams | part/process tree + collection plans | spreadsheet templates | inspection plans → orders → stations |
| Subgrouping | explicit (incl. individuals, subgroup size 1) | subgroups of pieces per feature | subgroup = samples per plotted point | template-defined | sampling in inspection orders |
| Limits from process data | yes (default 3σ; user-settable; staged) | yes ("calculated from collected data"; stored; auto-updated) | yes (per chart; zones) | yes (average/median/fixed-options) | yes (AI-assisted distribution → limits) |
| Spec limits | capability context; separate from control limits | reference lines; "must never be calculated from" for control limits | sample-level test "out of engineering limits" separate from OOC | histogram/capability context | compared against tolerance limits |
| Special-cause rules | tests 1–8, configurable | statistical violations flagged on points/events | Shewhart/Western Electric/Nelson families + custom | stability analysis red points | "process violations" (detail n/a) |
| Signal response | none (analysis output) | events; stream prioritization | triggers: prompts for assignable causes/corrective actions/notes, email, reject, OPC/DDE | none | causes/actions/complaints acquired; escalation to CCM |
| Capability | dedicated area; stability prerequisite | Cp/Cpk/Pp/Ppk per stream; also in stats panel | capability report | histograms + Cp/Cpk suites | process capability monitoring |
| Automatic data collection | no (file/worksheet based) | timed and manual data collections | devices: serial/OPC/ODBC/Excel; timed prompting | gage parse option in templates | gauges; manual; acquisition stations |
| Live status surfaces | no | dashboards, stream summary | Plant Monitor, colored charts/ribbon | no | dashboards; operator feedback |
| Multi-site | n/a | division→…→site rollups | plant-level | n/a | enterprise suite |

### What is invariant (A/B evidence across sample)

1. Time-ordered observations of a defined process characteristic, accumulated as a persistent record and organized into plotted points (subgroups of one or more readings).
2. Control limits computed from the process's own collected variation — center line + limits — explicitly distinct from specification/tolerance limits (Minitab default 3σ; Enact "calculated from collected data … must never be calculated from specification limits"; WinSPC zones; QI Macros average/median center lines; Opcenter limits from determined distribution).
3. Statistical rules evaluated against those limits to signal out-of-control / special-cause behavior — point beyond limits and non-random patterns (trends, runs, mixtures, stratification) — with the meaning that the process has become unpredictable and investigation/action is warranted.
4. The in-control ≠ within-spec distinction (Enact explicit; Minitab implicit via stability/capability separation; all sampled products show both kinds of limits).
5. Capability/performance analysis against spec limits as the companion analysis (present in all five sampled; but see below — held common, not definitional).
6. Charts as the primary surface; everything else radiates from the control chart.

### Evidence calibration notes

- WinSPC trigger machinery, Enact auto-update cadence, Opcenter inspection-order flow: product-level observations (A for WinSPC/Enact via help centers; B/C for Opcenter).
- "Stability before capability" — A at Minitab (stated verbatim); consistent with Enact treating Cp/Cpk on streams and disabling subgroups from capability math; held as a common mature rule, not a definitional invariant.
- Attribute charts operating without spec limits — supported structurally (Enact attribute chart statistics show only defects/defectives/pieces; Minitab attribute chart section defines no spec usage); supports keeping spec limits OUT of the defining core.
- No sampled product is a pure "monitoring without capability" product, so capability is documented as standard/common, not optional; but it is analysis about the process against specs, not the act of statistical monitoring itself — hence not definitional.

## Canonical Model (abstraction result)

### L0 — Defining Invariant (deliberately minimal)

```text
Defined process characteristic
  └── time-ordered observations accumulated as a persistent record,
      organized into plotted points (subgroups of one or more readings)
      └── control limits computed from the process's own variation
          (center line + limits; never derived from specifications)
          └── rule-based statistical evaluation against those limits
              → out-of-control signals when behavior is non-random/beyond limits
```

Remove tests:
- Remove limits-from-own-data (plot against spec/tolerance limits only) → tolerance charting/inspection territory, not SPC.
- Remove statistical rule evaluation → run chart/strip chart, no out-of-control determination.
- Remove the process-behavior subject (monitor machine up/down, output counts) → SCADA/HMI/OEE/historian territory.
- Remove time-ordered accumulation → one-shot statistical test or report, not process control.

### L1 — Common Mature Structure

- Part/process/characteristic organizing hierarchy (Enact process-part-feature; WinSPC part/process + collection plans; Opcenter inspection plans; Minitab/QI Macros implicit in data layout).
- Chart families: variables (Xbar-R/S, I-MR, zone), attributes (p, np, c, u), time-weighted (EWMA/CUSUM — Enact CUSUM templates, Minitab time-weighted), standardized/short-run (Enact standardized charts; QI Macros DNOM), rare-event (Minitab).
- Special-cause rule families beyond the basic point rule: Nelson / Western Electric / Shewhart (WinSPC preconfigured families; Minitab tests 1–8; QI Macros stability analysis).
- Specification limits and targets as reference overlay (USL/LSL/Target on charts).
- Capability and performance analysis (Cp/Cpk/Pp/Ppk, histograms), with stability-before-capability practice.
- Operator-facing data collection: station entry, gauge/device/PLC integration (WinSPC devices; Opcenter gauges; Enact data collections; QI Macros gage parse).
- Out-of-control events and response recording: prompts for assignable causes/corrective actions/notes, email/message triggers, severity colors (WinSPC), events (Enact), causes/actions acquisition (Opcenter).
- Limit lifecycle management: set after sufficient subgroups, freeze/fix, stage, recalculate on process change (Minitab stages; Enact stored limits; QI Macros fixed-limit templates).
- Reporting and status surfaces: dashboards, plant/floor monitors, reports, historical analysis.

### L2 — Variant / Optional

- Product philosophy/substrate: specialist real-time client (WinSPC), cloud platform (Enact), analysis suite (Minitab), Excel add-in (QI Macros), QMS-embedded module (Opcenter Quality).
- Industry/regulatory regime: automotive AIAG-style SPC, pharma/med-device validation contexts, food/packaging (Enact net-content statistics — LSC/MAV), semiconductors.
- Data collection posture: fully manual entry → gauge-connected → machine-connected/timed → streamed IIoT.
- Multivariate SPC (Minitab multivariate charts); economic control limits (Enact ECL).
- Alarms beyond the station: email, plant monitor cells, dashboards; write-back to OPC/DDE (WinSPC — machine-adjacent edge).
- Suite adjacency: gauge R&R/MSA bundled (QI Macros, calibration-management seam), CAPA/NCR escalation (Opcenter → CCM), traceability context fields (lot/shift/operator on every subgroup).

### L3 — Vendor-specific (research notes only)

- Enact: 10-minute auto refresh of control limits; Composite Quality Score; Stream Summary prioritization order (OOS then OOC); disabled-subgroup slider; standardized-chart engine.
- WinSPC: Collection Plan steps; Blueprints; trigger types incl. DDE poke, OPC item write, reject, password prompt; control-test template linking vs applying; QualTrend companion; color severity table.
- Minitab: tests 1–8 numbering; per-chart option dialogs; Real-Time SPC engine as separate product line; staging mechanics; worksheet storage of limits.
- QI Macros: wizard data-shape heuristics (columns/type → chart choice); template workbooks with yellow input areas; "same charts as Minitab Capability Sixpack" claim.
- Opcenter: inspection orders from released plans; acquisition stations; AI distribution selection; Copilot; CCM/Teamcenter Quality escalation paths.

## Vendor-specific Findings

See L3 above. Notable: WinSPC's trigger list is the deepest documented OCAP machinery in-sample; Enact's in-control≠in-spec teaching text is the clearest single articulation of the type's central conceptual discipline; QI Macros' fixed-limit templates document the "freeze limits and judge future batches" practice; Minitab documents the staged historical chart.

## Boundary Findings

- **vs Inspection & Metrology Software** (neighbor pass pre-declared "3+4 without 1 = SPC/data-collection"): IM judges a physical part instance against nominal geometry (CAD/drawing + tolerances) and produces per-part verdicts. SPC has no nominal geometry reference and no part verdict — it judges the process over time. A chart with only spec limits drawn is IM-style conformance view; the SPC content is the control limits. Seam: part-instance conformance vs process-behavior statistics.
- **vs Industrial Historian**: historian archives raw high-rate telemetry (never primarily manual entry) and exists to replay it. SPC consumes lower-rate samples, transforms them through subgroup statistics into plotted points with computed limits, and reaches a state judgment (in/out of control). Common upstream: historian/PLC data feeding SPC. Seam: archival + replay vs statistical state determination.
- **vs HMI / SCADA**: both show live process behavior, but HMI/SCADA supervise and write back to the process (commands, setpoints); SPC never commands the process — its "action" loop terminates in human response and recorded causes/actions. WinSPC's OPC write-back trigger is a machine-adjacent edge case (an integration out, not process control).
- **vs OEE Management**: OEE measures equipment time/output effectiveness with a loss-accounting model; SPC measures characteristic variation stability with statistical limits. Both have measure→review→act loops; the statistic and the subject differ completely.
- **vs Manufacturing Execution System**: MES executes released orders and binds quality gates to execution; MES's own pass recorded SPC as a standard-not-definitional capability. In-suite SPC (Opcenter) confirms the seam: SPC module serves inspection execution, but the SPC core (limits, rules, signals) is independent of order execution.
- **vs Manufacturing QMS / Life-sciences QMS / CAPA**: QMS holds the quality record population and closed-loop quality processes; CAPA manages investigation/action records. SPC signals can initiate those records (Opcenter escalates violations to CCM; WinSPC records assignable causes/corrective actions) — the seam is statistical monitoring machinery vs quality-record system of record.
- **vs Calibration Management**: calibration maintains measurement fitness (instrument register, due states); SPC assumes measured data and monitors the process. MSA/Gage R&R sits between them (bundled at QI Macros) but remains a measurement-fitness discipline.
- **vs general statistics / data-science workbenches**: general tools include control charts as one procedure; SPC applications center the persistent monitor loop (continuous data collection, live signals, response). Minitab straddles the boundary — its SPC chapter is the Type's content delivered inside an analysis suite.
- **vs BI dashboards / stream analytics (IT)**: generic thresholds and metrics vs process-behavior statistics (rational subgrouping, within/between variation, capability). A threshold alarm on a metric is not SPC; the computed-from-own-variation limit is.

### Historical / market-sample check (§24-style)

- Paper-era SPC: Shewhart charts hand-drawn on pre-printed forms; limits computed by hand from prior data; Western Electric handbook rules applied by eye; response recorded in logbooks. Satisfies the L0 chain with zero modern machinery — historical check passed.
- 1980s–90s DOS/Windows SPC packages (e.g., early SQCpack, WinSPC's predecessors) satisfy with station data entry and chart printing; regional products likewise.
- Spec-limit-only "quality charts" (in/out of tolerance plots) are excluded — they are inspection, not SPC. Run charts without limits excluded — no out-of-control determination.
- Therefore the canonical definition must not name: σ multiplier defaults (Minitab default 3σ is an implementation convention), specific rule families (Nelson/WE are dominant realizations), specific chart taxonomy, gauges/PLCs, cloud, AI.

## Uncertainties

- Siemens Opcenter Quality operational depth not verified (help behind support portal); its workflow description rests on official blog/product pages — assertions for this product kept at Tier-2 strength.
- Enact's event/notification internals (alarm console semantics, event lifecycle) not deeply fetched; only event existence and stream prioritization verified.
- QI Macros evidence is from official product/help pages (marketing-adjacent); feature existence verified, workflow depth not.
- Whether any shipped SPC product lacks capability analysis entirely is unverified; capability therefore held "common mature" rather than "optional", while remaining OUT of the defining core.
- WinSPC knowledgebase documents version 7.2–8.3 era; current-version behavior may differ (noted, low impact on canonical findings).

## Final Synthesis

SPC is the application Type whose subject is the statistical behavior of a manufacturing process over time. Its world is organized around a defined process characteristic whose observations accumulate as a persistent, time-ordered record; the record is transformed into plotted points; limits computed from the process's own variation (center line + control limits) are drawn; and statistical rules evaluate the points against those limits to signal when the process has become unpredictable (out of control / special cause). The signal's meaning — investigate and act — drives the type's second half: response recording (assignable causes, corrective actions), and companion analysis (capability against specification limits, with stability as the prerequisite). Specification limits are reference, never the source of control limits; in-control is not the same as in-spec.

Everything else — organizing hierarchies, chart families, rule families, devices, dashboards, suites, regimes — is common mature structure or variant. The market spreads across five philosophies (analysis suite, cloud platform, real-time station client, Excel add-in, QMS module), all of which preserve the same defining chain. The historical check passes at the paper-chart generation.
