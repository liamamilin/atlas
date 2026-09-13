# Research Notes — Task Mining Platform

Research date: **2026-09-08**

---

## Research Goal

Understand what a Task Mining Platform actually is as an Application Type: what it captures (which events, from which surface, by which mechanism), how the captured interaction stream becomes "tasks" (segmentation, grouping, merging), what analyses it produces, how insights turn into actions (automation handoff, process linkage), which roles and privacy machinery exist, and — most importantly — its boundaries against Process Mining Platforms, RPA Platforms, employee monitoring / digital-experience products, and time tracking.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: capture how employees actually interact with their work software (desktop/UI-level events), reconstruct the tasks they perform, and analyze them to find inefficiencies and automation/improvement opportunities.
- Users: process/automation analysts, RPA centers of excellence, operational excellence teams, business analysts; employees whose work is captured (data subjects, often also contributing recordings).
- Nearest neighbors likely confused with:
  - **Process Mining Platform** — mines business-transaction event logs from operational systems (case semantics); task mining mines user-level interaction from the work surface. Sibling, complementary.
  - **RPA Platform** — executes UI automation; task mining observes work and identifies automation candidates.
  - **Employee monitoring / Digital Employee Experience Management** — same capture substrate (desktop events), but the analytical object is person-level activity time / device experience, not reconstructed tasks; purpose is workforce oversight / IT experience, not work-structure analysis for improvement.
  - **Time Tracking Application** — declared/timer-based time per task/project for billing; task mining derives structure from observed interaction.
- Unknowns at start: capture mechanics (continuous background agent vs on-demand recorder), whether a predefined "known task" is definitional, how segmentation into tasks is productized (AI vs manual), privacy machinery, packaging (standalone vs suite module).

## Research Questions

1. What exactly is captured (mouse/keyboard events, screenshots, window titles, text entries), from which surface, and by which mechanism (recorder session vs background agent)?
2. Is the task defined before capture ("known task") or discovered from the stream?
3. How is the raw interaction stream turned into task structure — automatic clustering/merging, manual grouping, human curation?
4. What analyses are produced (time per step/activity, variants, application usage/switching, frequency)?
5. How do insights become actions (automation candidate handoff, RPA skeletons, connector recommendations, improvement tracking)?
6. How does task mining relate to process mining in-product (same portal, zoom-in pairing, separate product)?
7. What roles exist (recording employees, analysts/SMEs, admins, process owners)?
8. What privacy/consent machinery exists (PII masking, screenshot/text removal, anonymization, consent)?
9. What deployment/packaging forms exist, and what are the platform constraints (OS, remote desktop)?

## Representative Products

Selected for market representativity, philosophical diversity, and customer-tier diversity:

| Product | Position / philosophy | Customer tier | Docs status |
|---|---|---|---|
| **UiPath Task Mining** | Automation-suite module; AI merge of recorded traces of a known task; automation handoff (PDD/XAML → Automation Hub) is first-class | Enterprise automation estates | **Tier 1 docs fetched (5 pages)** — strongest operational evidence |
| **Microsoft Power Automate (task mining capability, ex-Process Advisor)** | Low-code automation platform module; citizen-developer recorder sessions; connector-based automation recommendations | Broad mid-market / Microsoft estates | **Tier 1 docs fetched (6 pages)** |
| **Apromore (Task Mining)** | Research-origin full-spectrum process-intelligence platform; task mining as the user-level layer complementing process mining; BPMN/simulation continuity | Mid-market/enterprise; free trial tier | Tier 2 product + educational pages fetched (2 pages); docs portal not attempted this pass (unreachable in prior sibling pass) |
| **Soroco Scout** | Pure-play "work graph" / work-discovery vendor; team-level work patterns tied to business outcomes; improvement tracking | Enterprise, consulting-led | Tier 2 product page fetched (1 page); capture mechanics not detailed on page |
| **Celonis (Task Mining)** | Pure-play process-intelligence suite shipping task mining as a module | Large enterprise | **Not researched** — /task-mining/ URL redirects to generic platform page, /platform/task-mining/ 404, docs auth-gated (per prior sibling pass). Abandoned after 2 attempts per network rules. Named only as a market anchor; **no operational claims drawn from it** |

Also used as definitional grounding (not a sampled product): Apromore's official educational page "What is Task Mining?" (Tier 2) — anchors the task-mining-vs-process-mining distinction from the vendor side. Wikipedia was attempted for Tier 3 grounding but timed out twice (abandoned).

## Sources

| # | Source | Tier | Status |
|---|---|---|---|
| 1 | UiPath — Task Mining user guide: Introduction (docs.uipath.com) | 1 (official user guide) | fetched, 2026-09-08 |
| 2 | UiPath — Merge traces (docs.uipath.com) | 1 | fetched, 2026-09-08 |
| 3 | UiPath — Automation Hub integration (docs.uipath.com) | 1 | fetched, 2026-09-08 |
| 4 | UiPath — Task Mining FAQs (docs.uipath.com) | 1 | fetched, 2026-09-08 |
| 5 | UiPath — Task Mining docs root / navigation (docs.uipath.com) | 1 | fetched, 2026-09-08 |
| 6 | Microsoft Learn — Overview of process mining and task mining in Power Automate | 1 (official docs) | fetched, 2026-09-08 |
| 7 | Microsoft Learn — Overview of task mining | 1 | fetched, 2026-09-08 |
| 8 | Microsoft Learn — Prepare processes and recordings | 1 | fetched, 2026-09-08 |
| 9 | Microsoft Learn — Analyze tasks and processes | 1 | fetched, 2026-09-08 |
| 10 | Microsoft Learn — Visualize processes | 1 | fetched, 2026-09-08 |
| 11 | Microsoft Learn — Identify automation opportunities | 1 | fetched, 2026-09-08 |
| 12 | Microsoft Learn — Protect your data | 1 | fetched, 2026-09-08 |
| 13 | Apromore — Task Mining product page (apromore.com) | 2 (official product page) | fetched, 2026-09-08 |
| 14 | Apromore — "What is Task Mining?" educational page | 2 | fetched, 2026-09-08 |
| 15 | Soroco — Scout Business product page (soroco.com) | 2 | fetched, 2026-09-08 |
| 16 | Celonis — Platform page (celonis.com/platform, reached via /task-mining/ redirect) | 2 | fetched, 2026-09-08 — **contains no task-mining-specific content** |
| 17 | Celonis — /platform/task-mining/ | 2 | **404 — abandoned** |
| 18 | Nintex — process discovery product page + help center topic | 1/2 | **404 twice — abandoned** |
| 19 | Wikipedia — Process mining (Tier 3 grounding) | 3 | **timed out twice — abandoned** |

**Source-access limitation:** Celonis task-mining documentation and Nintex Process Discovery documentation were not reachable. Claims about those vendors are kept at market-anchor level only. Soroco's capture mechanics are not detailed on its fetched product page; claims about Soroco are kept at positioning level. No operational detail has been filled in from model memory.

---

## Product Observations

### UiPath Task Mining (evidence layer A — Tier 1 official docs)

**Positioning:** "AI-based desktop activity analysis that surfaces evidence of automation opportunities and captures task variations, with automation skeleton export as PDD and XAML files."

**Known-task orientation (explicit):** "Task Mining is built around a known task: one that a Business Analyst or Process Subject Matter Expert (SME) has already identified as worth investigating."

**What it does / does not do (as documented):**
- Does: record and compare variations (traces) of a known task; use AI to cluster screenshots and merge traces into a single task graph with decision points; surface task-level evidence (variants, step statistics, time-per-action data); export artifacts (PDD, Studio XAML skeleton).
- Does not: automatically discover unknown tasks across the organization; produce root-cause findings or a ranked list of automation recommendations; replace the review of a Business Analyst or SME; analyze end-to-end system event logs across business systems (that is Process Mining).

**Capture:** desktop recorder client (Windows only; web portal is cross-platform) capturing each action performed — mouse clicks, keystrokes, hotkeys — plus screenshots; recorder requires internet connection; Citrix applications can be captured (with degraded selector quality; installing the client inside the Citrix environment recommended). Audio capture exists (transcribed and summarized via LLM; merging traces with audio loses the audio capture). Mobile devices not supported.

**Collaboration:** recording users are invited to a project (no documented limit on invited users); each records traces of the same task; traces are collected in a web portal for project management, data storage, collaboration.

**AI reconstruction:** ML model clusters screenshots of the same application and screen across traces, merges matching steps, and creates decision points where actions differ. The AI does not rank findings or recommend which automation candidate to pursue — that remains a manual BA/SME step.

**Merge modes:** Auto merge (up to 10 traces at once; traces with manually added steps excluded), Guided merge (two traces, step-by-step human decisions: append element, append all elements, merge actions, skip), Compare (read-only side-by-side). Merged result is editable: rename steps/decisions, add details, remove actions.

**Limits (product-specific):** maximum 500 actions per trace; guidance to create distinct traces per task and capture in under an hour; recording languages English and Japanese (merging traces in different languages may produce inaccurate results).

**Privacy:** PII masking enabled by default (provided via Microsoft Cognitive Services on collected images); customers can anonymize who the data was collected from; "Privacy & GDPR consent compliant" positioning; tenant data isolation asserted.

**Action loop:** from a trace, a BA/SME exports an automation candidate to **Automation Hub** — a form captures automation name, description, business area, "number of ways to complete the process", "% of Digital Input", "% of Structured Digital Data Input" (metrics feeding automation-potential assessment), optional process owner. Documentation attached to the idea: XAML skeleton + PDD (.docx). One idea per trace; subsequent exports add documentation to the same idea. Bidirectional links (Show in Task Mining / View in AH).

**Expected workflow (as documented):** define the known task → collect comparable traces from one or more recording users → merge/compare traces into one task graph → review as BA/SME → quantify the finding (time savings, frequency, complexity) → submit candidate to Automation Hub.

**Lineage (documented in FAQ):** formerly known as "Assisted Task Mining"; positioned as "an evolution of Task Capture" — Task Capture is the human-driven sibling product that captures one expert's ideal step-by-step workflow ("taking selfies" of expertise) into a PDD, one task graph at a time, without AI merging. Task Mining = web portal + desktop recorder; Task Capture = full desktop application.

### Microsoft Power Automate — task mining capability (evidence layer A — Tier 1 official docs)

**Positioning:** "Task mining is a technology that enables organizations to capture detailed steps for tasks performed on users' desktops, either independently or collaboratively with colleagues." Analyzing recorded user actions → insights into how tasks are performed, common mistakes, tasks that can be automated. Positioned as the desktop-level zoom-in complement to the process mining capability in the same product ("You can zoom in to specific desktop tasks you might have discovered during your process mining analysis").

**Capture:** on-demand recording sessions via the **Power Automate desktop recorder** (part of Power Automate for desktop). User creates a named **process** in the portal, opens the recorder, clicks Record, performs the actions, selects Finish. Recorder features: action list with descriptions, delete individual actions, pause/resume, reset. Multiple people contribute recordings to the same process ("invite others to contribute recordings to the process for richer insights").

**Preparation / reconstruction:** recorded actions are grouped into **activities** — auto-grouping is available ("The process mining capability is now able to automatically group similar actions into activities") and fully editable: drag activity headers, rename from recommended or custom names; process owner can publish **recommended activity names** for consistency across recordings; minimum two activities required for a meaningful map. Sensitive information must be removed before analysis: delete screenshots per step; edit text entries to remove confidential content.

**Analysis:** process map (activities as nodes, transitions as edges; each sequence a **variant**; metrics: frequency of activities, throughput time per variant). KPIs: number of recordings, number of variants, average time. Visualizations: variants by frequency, variants by time, activity by average time, recordings by time, start-date filter. Variant/recording selectors for drill-down.

**Application analytics (dedicated report):** top apps used; access patterns (apps used together); app-switching frequency pairs; time spent by application; actions by application; KPIs: apps used, times accessed (app comes back into focus), time spent (focused time only), actions count. Scatter plot of time spent × times accessed per app (circle size = usage across recordings) to identify essential apps and back-and-forth switching.

**Automation recommendations:** blue recommendation icons on process map activities; "+Automate activities" opens the Power Automate form designer with **connector recommendations** per activity; user assembles a flow from recommended connectors.

**Recording lifecycle:** statuses In progress / Failed / Not analyzed / Ready to analyze / Analyzed (+ not-ready and modified icons); analysis runs at process level over recordings marked ready; re-analysis syncs modified recordings.

**Licensing/packaging:** task mining included in Power Automate Premium (and trial); process mining capacity metered separately; task mining processes analyzed/visualized in the web interface only (not the Process Mining desktop app). Prerequisite: Power Platform environment with Dataverse; Environment Maker role to create/share/contribute.

### Apromore Task Mining (evidence layer A for module existence/positioning — Tier 2)

**Positioning:** "captures real user interactions across systems to reveal friction, reduce manual effort, and unlock powerful automation and optimization opportunities, giving you a complete view of how work really gets done." Framed as "the missing layer of process intelligence" bridging "the execution gap" between mapped processes and actual work.

**Problems addressed (as documented):** hidden manual work (task execution outside core systems — emails, spreadsheets, toggled screens); rework & redundancy (copy-pasting, screen-switching, multi-system workflows); fragmented data (no view of user-system interaction to prioritize automation); operational controls (difficulty standardizing best practices).

**How it works (as documented on the educational page):**
1. **Collect data** — user interaction data collected and ingested.
2. **Gain a basic overview** — visual overview as a **process map of the routines** followed within a given process task: steps performed, their duration, resource productivity and utilization.
3. **Identify bottlenecks** — bottlenecks, ping-pong behavior, rework loops from the task's routines; KPIs.
4. **Optimize** — discover a **BPMN model** out of the routines; simulate what-if scenarios to assess improvement interventions.

**Task vs process distinction (vendor's own table):** task mining = individual tasks and how they are done; source = user interaction data from desktop applications (e.g. Outlook, Excel); focus = optimization of individual tasks. Process mining = full end-to-end processes; source = event logs from enterprise systems (SAP, Salesforce, ServiceNow); focus = overall process optimization. "Task mining and process mining should be seen and used as complementary techniques."

**Use cases (as documented):** improve process and task efficiency; increase customer and employee satisfaction; discover automation potential (RPA opportunities — "manual, repetitive and error-prone tasks are identified with ease"); unify process variants (identify the most productive users).

**Privacy posture:** "collects and analyzes the user interaction data of your employees in a secure and privacy-aware way" (claim level only).

**Platform context:** task mining is one module of the full-spectrum platform (process mining, compliance center, simulation, copilot); now part of Salesforce. Marketing percentages (90% visibility, 45% faster, 30% efficiency, 40% manual-effort reduction) not treated as operational evidence.

### Soroco Scout (evidence layer A for positioning — Tier 2)

**Positioning:** "Discover teams' work patterns and bottlenecks. Understand how your teams' work patterns affect your business outcomes." Product of a pure-play "work graph" company (work-graph framing on site nav).

**Flow (as documented):**
- **Visibility** — work patterns "from a birds' eye to worms' eye" for everybody "from a CXO to an associate"; 20+ bottlenecks; connect to business objectives (optimization opportunities mapped to teams' KPIs).
- **Change** — map AI/automation capabilities to business needs; recommendations for deploying automation/AI; "simulate success" — curate and forecast a change journey.
- **Impact** — track benefits of interventions; opportunity tracking.
- **Improve** — generate data-backed business documents and summaries; process modelling ("choose from up to 5 different actions to model your work").

**Orientation:** team/organization-level work patterns tied to business outcomes — broader than single-task analysis; improvement tracking is first-class (unlike the automation-handoff pole).

**Analyst positioning:** Everest Group PEAK Matrix leader "Digital Interaction Intelligence" (2025); NelsonHall NEAT leader "Process Understanding"; Forrester Wave "Process Intelligence Software" (2023). Marketing numbers (30% opportunities, 10+ recommendations) not treated as operational evidence.

**Capture mechanics:** not detailed on the fetched page (recorded as a source limitation).

### Celonis — not observed

Task-mining-specific pages unreachable (redirect to generic platform page; /platform/task-mining/ 404; docs auth-gated per the sibling process-mining pass). Retained as a market anchor only: the leading pure-play process-intelligence suite ships task mining as a module. No operational claims drawn from it.

---

## Cross-product Comparison

| Capability / structure | UiPath (A, T1) | Microsoft (A, T1) | Apromore (A, T2) | Soroco (A, T2) | Evidence layer |
|---|---|---|---|---|---|
| Capture of user interactions with work software at the point of work | ✔ recorder client: clicks, keystrokes, hotkeys, screenshots | ✔ desktop recorder: actions, screenshots, text entries | ✔ "real user interactions across systems/screens" | implied (work patterns from team digital interactions; mechanism not detailed) | **B** |
| Reconstruction of work structure from the interaction stream (steps/actions → tasks/activities/patterns) | ✔ task graph with steps + decision points | ✔ actions grouped into activities → process map | ✔ process map of routines within a task | ✔ team work patterns | **B** |
| Variations of the work captured and compared | ✔ explicit (traces, variants, merge/compare) | ✔ explicit (variants KPI, variant selector) | ✔ (variation in how users complete tasks; unify variants) | ✔ (work patterns) | **B** |
| Time measures (per step/activity/task) | ✔ time-per-action, step statistics | ✔ average time, activity time, throughput time | ✔ duration, resource utilization | ✔ (bottlenecks) | **B** |
| Application usage / switching analytics | partial (screenshot clustering by app; no named report on fetched pages) | ✔ dedicated application analytics report | ✔ app-switching named as the problem class | implied | **B** (dedicated report explicit in 1 of 4; concept present in others) |
| Multiple people contributing captures of the same work | ✔ (invite recording users, merge traces) | ✔ (invite contributors to a process) | implied (routines across users; "most productive users") | ✔ (team-level) | **B** |
| AI/automated clustering or grouping of raw actions | ✔ explicit (screenshot clustering, auto-merge ML) | ✔ auto-grouping into activities (optional; manual fully supported) | not evidenced on fetched pages | not evidenced | **B** (2 of 4; manual path exists in both) |
| Human curation/edit of the reconstructed structure | ✔ explicit (guided merge, rename, edit) | ✔ explicit (grouping, renaming, recommended names) | not evidenced | not evidenced | **B** (2 of 4) |
| Known-task orientation (work defined before capture) | ✔ explicit ("built around a known task") | ✔ (named process created before recording) | partial ("a given process task") | ✖ (team-level pattern discovery, no predefined task) | **variance axis**, not invariant |
| Automation candidate identification / handoff | ✔ explicit (Automation Hub export, PDD + XAML skeleton) | ✔ explicit (connector recommendations → flow designer) | ✔ (automation-ready task discovery, RPA opportunities) | ✔ (AI/automation recommendations) | **B** |
| Privacy machinery (PII masking, screenshot/text removal, anonymization) | ✔ explicit (default PII masking, contributor anonymization, GDPR) | ✔ explicit (delete screenshots, remove text) | ✔ claim ("secure and privacy-aware") | ✔ (privacy page linked; lock icon) | **B** |
| Pairing with process mining (task-in-process context) | ✔ (FAQ: complementary; separate products) | ✔ (same portal; "zoom in to desktop tasks discovered during process mining") | ✔ (same platform; connect task-level to process KPIs) | ✖ (work-graph framing; no process-mining pairing on page) | **B** (3 of 4) |
| Capture mode: on-demand guided recording | ✔ (recorder client, current docs) | ✔ (recorder sessions) | not evidenced | not evidenced | **B** (2 of 4 documented) |
| Capture mode: continuous background capture | not in current docs (product formerly "Assisted Task Mining"; earlier continuous-capture form not evidenced in fetched pages) | ✖ | implied ("captures real user interactions", "real-time visibility") | implied | **variant** — moderate confidence |
| Team/org-level pattern discovery (beyond single task) | ✖ explicit ("does not automatically discover unknown tasks") | ✖ (process-scoped) | partial | ✔ core | **variance axis** |
| Automation artifacts export (PDD/XAML skeletons) | ✔ | ✔ (flow assembly, not PDD) | ✖ not evidenced | ✖ (business documents/summaries instead) | product-apportioned |
| Improvement/opportunity tracking layer | ✖ (delegated to Automation Hub) | ✖ | ✖ | ✔ (opportunity + impact tracking) | product-apportioned |
| Simulation / BPMN continuity from task data | ✖ | ✖ | ✔ (BPMN discovery from routines, what-if) | ✔ (process modelling actions; change simulation) | Optional |
| Desktop/workstation as capture surface; mobile excluded | ✔ explicit (Windows only, no mobile) | ✔ (Windows desktop recorder) | ✔ (desktop applications) | not stated | **B** (desktop universal in sample; mobile exclusion explicit in 1) |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being a Task Mining Platform:

```text
User-interaction capture at the point of work
  (recorded events of how people actually operate their work software
   — applications, screens, UI actions — on their work computers)
└── Reconstruction of tasks from the interaction stream
    (the captured stream is structured into meaningful units of work —
     steps/actions grouped into tasks/activities — and their variations,
     derived from the data rather than self-reported)
    └── Task-level work analysis for improvement
        (measures of how the work is performed — time, frequency,
         variation, application usage — oriented to exposing
         inefficiencies and identifying improvement/automation opportunities)
```

Three invariants:

1. **User-interaction capture at the point of work** — the substrate is what people do inside their software (which application, which screen, which action), not the business-transaction records the systems themselves generate. Remove it and there is nothing to mine; the product degenerates into interviews/surveys or system-log analytics (the process-mining sibling).
2. **Reconstruction of tasks from the interaction stream** — raw interaction events are structured into named, comparable units of work and their variations. Remove it and the product is activity logging / employee monitoring (person-level app-time aggregates) or a plain screen recorder.
3. **Task-level work analysis oriented to improvement** — the reconstructed tasks are measured (where time goes, how the work varies, which applications are involved) to expose inefficiencies and improvement/automation opportunities. Remove the improvement orientation and analytical object, and the product is surveillance/recording tooling.

Deliberately NOT in L0: a predefined "known task" (Soroco discovers team-level patterns without one), AI clustering/merging (manual grouping is a fully supported path in sampled products), screenshots (UiPath/Microsoft use them; the invariant is the interaction event, not the image), continuous background capture (on-demand recorder sessions are an equally valid realization), desktop-vs-other surface specifics (desktop/workstation is the universal current substrate; phrased abstractly), privacy machinery, automation handoff, process-mining linkage, cloud delivery, any specific export format.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature products; not definitional:

- split architecture: a capture client on the work computer + a web portal for analysis/collaboration
- multiple people contributing captures of the same work; collaborative review
- automated (AI/ML) clustering or grouping of raw actions into named activities — with a manual grouping/curation path alongside
- task graph / process map as the central visualization: steps as nodes, transitions as edges, decision points, variants
- time measures per step/activity/task and frequency counts; variant comparison
- application usage analytics: which apps, how often accessed, time spent, switching patterns
- human curation layer: rename, regroup, delete steps; recommended activity naming for consistency
- privacy machinery: PII masking, screenshot/text removal, contributor anonymization, consent posture
- automation handoff: candidates exported to automation tooling (RPA skeletons / process definition documents / connector-based flow recommendations)
- packaging as a module of a broader automation or process-intelligence platform; complementary pairing with process mining

### L2 — Variant / Optional Structure

Depends on segment, packaging, strategy:

- capture mode: on-demand guided recording sessions vs continuous background capture
- analytical scope: single known task (task-scoped) vs team/organization-level work-pattern discovery (discovery-scoped)
- output artifacts: process definition documents, automation skeletons, connector-based flows, business documents/summaries, BPMN models for simulation
- linkage to process mining (task-in-process context) vs standalone deployment
- improvement/opportunity tracking layer (intervention tracking)
- simulation / what-if continuity from task data
- audio capture/narration; remote-desktop/Citrix capture
- deployment: cloud SaaS vs on-prem components; OS constraints (Windows-dominant capture clients)
- AI summaries/copilots over captured work

### L3 — Vendor-specific (research notes only)

- **UiPath**: PDD (.docx) + XAML skeleton export; Automation Hub export form (number of ways to complete the process, % digital input, % structured digital data input, process owner); one idea per trace with documentation accumulation; auto-merge up to 10 traces; max 500 actions per trace; capture-in-under-an-hour guidance; English/Japanese recording languages; PII masking via Microsoft Cognitive Services (default-on); contributor anonymization option; Citrix capture with degraded selectors; recorder Windows-only, web portal cross-platform; audio capture with LLM summarization (lost on merge); Task Capture sibling product (human-driven, single graph, no AI merge); "formerly Assisted Task Mining" naming history; no platform-unit consumption.
- **Microsoft**: Power Automate desktop recorder (pause/resume/delete/reset); process container with contributor invitations; auto-grouping + manual activity grouping with recommended activity names published by process owner; minimum two activities; recording status lifecycle (In progress/Failed/Not analyzed/Ready to analyze/Analyzed + not-ready/modified icons); application analytics report (apps used, times accessed, focused time spent, actions; scatter plot, switching pairs, pie charts); connector recommendations via form designer; web-only visualization for task mining (desktop Process Mining app excluded); Dataverse/Power Platform prerequisites; Environment Maker role; licensing tiers (Premium/trial; process-mining capacity metering).
- **Apromore**: routines → BPMN model discovery; what-if simulation on task-derived models; "execution gap" framing; full-spectrum platform packaging (compliance center, copilot); Salesforce acquisition; marketing percentage claims.
- **Soroco**: "work graph" framing; 20+ bottlenecks; up to 5 process-modelling actions; opportunity + impact tracking; change-journey simulation; analyst-category positioning (Everest "Digital Interaction Intelligence", NelsonHall "Process Understanding", Forrester "Process Intelligence Software").

## Vendor-specific Findings

- **The "known task" premise is a packaging choice, not the Type's invariant.** UiPath states it explicitly ("built around a known task") and Microsoft operationalizes it (named process created before recording), but Soroco's core promise is discovering team-level work patterns without a predefined task, and Apromore straddles both. Defining the Type as "mining variations of a known task" would overfit to the automation-suite pole and exclude the discovery-scoped pole.
- **Recorder-based vs continuous capture is a real market split.** The two Tier-1-documented products both use on-demand recorder sessions (UiPath's current product is the former "Assisted Task Mining"; Microsoft's is recorder-native). Continuous background capture is implied by Apromore/Soroco positioning but not operationally evidenced in fetched pages. Held as a variant axis with moderate confidence.
- **AI merging is differentiating, not definitional.** UiPath's screenshot-clustering auto-merge is the most productized; Microsoft offers auto-grouping with a fully supported manual path; the others don't evidence it on fetched pages. Manual grouping satisfies the core (Microsoft documents it as a first-class path).
- **The action loop has two shapes:** automation-handoff (UiPath → Automation Hub with PDD/XAML; Microsoft → connector recommendations/flow designer) vs improvement-tracking (Soroco opportunity/impact tracking). Both are implementations of "insights become actions"; neither is definitional.
- **Privacy machinery is near-universal and prominent** (default PII masking, screenshot/text removal, anonymization) — a signature operational concern of the Type, but held as common mature structure, not invariant.

## Boundary Findings

- **vs Process Mining Platform** (sharpest seam, confirmed from both sides — the sibling pass documented the same boundary from the process-mining side): the substrate differs. Process mining ingests **event logs from operational systems** — business-transaction records carrying case identity (one order, one claim, one ticket). Task mining ingests **user-interaction events from the work surface** — what a person clicked, typed, and switched between, with no case semantics by default. The unit of analysis differs accordingly: case/variant vs task/person/session. Both sampled vendor families document the complementarity in their own words (UiPath FAQ: task mining = desktop-level activity for a known task, process mining = end-to-end system event logs; Apromore table: user interaction data from desktop applications vs event logs from enterprise systems; Microsoft: "zoom in to specific desktop tasks discovered during your process mining analysis"). Remove the user-interaction substrate → process mining; add case/transaction semantics to the captured stream → it becomes process mining.
- **vs RPA Platform**: task mining observes work and identifies automation candidates; RPA executes automation. The handoff artifacts (PDD/XAML skeletons, connector recommendations) are the bridge, not the core. UiPath explicitly lists "producing root-cause findings or a ranked list of automation recommendations" as something Task Mining does *not* do — the human decides; the robot later executes.
- **vs Employee monitoring / workforce-analytics products and Digital Employee Experience Management**: same capture substrate (desktop events), different analytical object and purpose. Employee monitoring aggregates person-level activity (app/URL time, productivity scoring, policy violations); DEX products aggregate device/application experience quality for IT. Task mining reconstructs the *structure of work* (tasks, steps, variations) and orients to work improvement/automation. Remove task reconstruction → activity monitoring; remove the improvement orientation → surveillance tooling. (Boundary phrased on the analytical object; whether monitoring vendors now ship task-mining-like features was not researched.)
- **vs Time Tracking Application**: time tracking records declared/timer-based time per task/project, typically for billing/payroll, with the task as a user-selected label. Task mining derives the task structure itself from observed interaction and analyzes how the work is performed. Declared vs derived is the seam.
- **vs Desktop Automation Application / personal UI automation**: those products *actuate* the UI (play back scripts); task mining *observes* the UI. Same surface, opposite direction.
- **vs Task-capture / process-documentation tools** (intra-family, e.g. UiPath's own Task Capture sibling): human-driven capture of one expert's ideal workflow into a step document vs AI-driven mining of multiple people's actual variations. Documentation of intended work vs mining of performed work. The directory has no separate leaf for the documentation form; recorded here as a thin sibling, not a taxonomy conflict.
- **"Remove what → becomes another Type" test**: remove user-interaction capture → Process Mining Platform (system event logs) or a survey/interview practice; remove task reconstruction → employee monitoring / activity logging / screen recording; remove the improvement orientation → surveillance/recording tooling; remove analysis entirely → capture utility.

## Historical / Market-Sample Check

- Would older, regional, platform-native, or differently positioned products still fit L0?
  - **Paper-era ancestor: the time-and-motion / task-observation study.** An analyst observing a worker, reconstructing the task's steps on an observation sheet, timing each step, comparing variations across workers, and proposing improvements — satisfies the conceptual core (observe work at task level → reconstruct → analyze for improvement) with no software at all. The modern product digitizes the observer.
  - **Documented product lineage (UiPath FAQ):** Task Capture (human-driven capture of a known task into a step document, one graph at a time, no AI) → Assisted Task Mining → Task Mining (AI clustering/merging of multi-person traces). The earlier, simpler form satisfies the core without AI merging, screenshots-as-data, or cloud collaboration — confirming those are era-current additions, not invariants.
  - **Manual-grouping path (Microsoft):** auto-grouping is optional; a fully manual grouping/editing workflow is documented as a first-class path — the core does not require AI.
  - **Recorder-based capture (current UiPath/Microsoft) and continuous capture (implied by other poles) both satisfy the core** — capture trigger mode is not an invariant.
- Therefore L0 must not include: AI clustering, screenshots, continuous agents, cloud delivery, GDPR-specific machinery, automation-marketplace handoffs, process-mining integration, team-level dashboards, or any specific export format. All are current-market features.
- Naming check: "task mining" is the established category term used by all sampled vendors (product names, educational pages, analyst categories such as "Process Understanding" / "Process Intelligence"). The directory leaf name matches market usage. No taxonomy conflict.

## Uncertainties

1. **Celonis task mining unverified** (source unreachable). Its inclusion rests on market notoriety and the sibling pass's category evidence; no operational claim in the final document depends on it.
2. **Soroco capture mechanics undocumented** on the fetched page (agent? which events? continuous?). Claims kept at positioning level; the work-pattern reconstruction and improvement orientation are documented, the capture substrate is inferred from category membership.
3. **Continuous vs on-demand capture**: current UiPath and Microsoft docs describe recorder-based capture only; continuous background capture is implied by Apromore/Soroco positioning but not operationally evidenced. Held as a variant axis with moderate confidence.
4. **Employee-monitoring convergence**: whether workforce-monitoring/DEX vendors now ship task-reconstruction features was not researched; the boundary is phrased on the analytical object and purpose, which is robust either way.
5. **Mobile/other-surface capture**: UiPath explicitly excludes mobile; the sample is desktop-uniform. The final document phrases the surface as "the employee's workstation/desktop (today's universal substrate)" without claiming exclusivity forever.
6. **Scale limits** (traces per study, actions per trace, retention) documented only for UiPath; treated as product-specific and excluded from the final document.
7. **Wikipedia Tier 3 grounding unavailable** (timeouts); the task-vs-process distinction is instead anchored by two independent vendor educational/docs sources (UiPath FAQ, Apromore educational page), which agree.

## Final Synthesis

A Task Mining Platform is an analysis platform whose substrate is **user-interaction data captured at the point of work** — the events of people actually operating their work software (applications, screens, clicks, keystrokes, switches) — from which it **reconstructs the tasks people perform and the variations in how they perform them**, and on which it **runs task-level work analysis** (time per step, frequency, variant comparison, application usage) **oriented to exposing inefficiencies and identifying improvement and automation opportunities**. Around this core, mature products add: a capture-client + portal architecture with multi-person contribution, AI-assisted clustering/grouping of raw actions into named activities (with manual curation alongside), task graphs/maps with variants and decision points, application usage/switching analytics, privacy machinery (PII masking, screenshot/text removal, anonymization, consent), and an action loop that hands automation candidates to RPA/automation tooling or tracks improvement opportunities. The Type is defined by observation of work at the human-interaction layer; remove that substrate and it becomes process mining (system event logs), employee monitoring (person-level activity aggregates), or a screen recorder (unstructured capture). Its two deepest variant axes are capture mode (guided recording sessions vs continuous background capture) and analytical scope (a predefined known task vs team-level work-pattern discovery).
