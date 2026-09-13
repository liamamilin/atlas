# Research Notes — Lean Construction Planning

## Research Goal

Understand what a Lean Construction Planning application actually is as an Application Type: the core objects it manages, the work its users perform, how the lean/Last Planner workflow maps onto software structures, which structures are defining vs merely common in today's market, and where the boundary lies against Construction Scheduling (the closest sibling, which left a joint-review flag for this pass), Construction Project Management, Project Controls, and generic task management.

## Initial Boundary

- Directory leaf: Lean Construction Planning (§17 Construction, Real Estate & Facilities).
- Hypothesis going in: software that operationalizes the Lean Construction / Last Planner System® methodology — pull planning, lookahead/make-ready planning, weekly work plans (commitments), constraint management, PPC-style reliability measurement — as distinct from CPM scheduling software.
- Closest neighbors: Construction Scheduling (§17, processed — joint-review flag pending against this leaf), Construction Project Management (§17, processed), Project Controls Platform (§17, unprocessed), Preconstruction Management (§17, unprocessed), Construction Field Management (§17, unprocessed), generic Task Management / Kanban (§03.06), Production Planning / APS (§16, manufacturing — same word "planning", different world).
- Prior-pass context: the construction-scheduling pass (2026-09-07) recorded in STATUS.md Boundary Issues: "joint review recommended vs Lean Construction Planning (§17, unprocessed): softest seam in the construction family — lean/Last Planner centers the collaborative commitment/lookahead workflow (pull plans, weekly work plans, constraint management, PPC-style variance) while Construction Scheduling centers the calculated activity network + baseline discipline; Touchplan documented as the overlap zone (lean workflow core + master-schedule synchronization as the consumption seam); discriminator = object of record (calculated master schedule vs commitment plan)". This pass must discharge that flag.
- The project-controls-platform pass (research notes) additionally observed "Last Planner System® alignment in Primavera Cloud task management" — evidence that enterprise scheduling suites embed lean machinery as a module.

## Research Questions

1. What is the unit of record — the calculated master schedule, or the near-term commitment plan?
2. How does the Last Planner workflow (pull → lookahead/make-ready → weekly commitment → daily huddle → measure/learn) map to software objects and surfaces?
3. Is there calculation machinery in lean products (pull calculations, constraint filtering), and how does it differ from CPM calculation?
4. How are commitments made, gated, and measured? What states do tasks/constraints carry?
5. Who collaborates, and on what surfaces (boards, huddles, mobile)?
6. How do lean products relate to the master schedule — own it, import it, synchronize with it?
7. Which structures are defining vs common vs variant vs vendor-specific?
8. Do combined products (CPM engine + lean layer in one platform) still fit this Type, or do they straddle two Types?
9. Historical check: does the pre-software (whiteboard/sticky-note + spreadsheet) form of LPS satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers/geographies:

| Product | Philosophy / pole | Tier & geography |
|---|---|---|
| Touchplan (MOCA Systems) | pure-play collaborative Last Planner overlay synchronized with the master schedule | US commercial GC market, large firms (DPR, Brasfield & Gorrie, Barton Malow, EllisDon) |
| vPlanner | pull-planning-first, "projects as networks of commitments", Enhanced LPS per P2SL 2020 Benchmark | consultant/heavy-user tier, US + international |
| lcmd | org-scale lean transformation platform (strategy → jobsite), takt emphasis, broad lean-method portfolio | European (German) GCs, infrastructure, pharma |
| Outbuild | combined master-schedule + lean field coordination, field-first (iPad), mid-market | US mid-market GCs (Skender, Redmond, Warfel) |
| VisiLean | combined full CPM engine + Last Planner + takt in one browser platform | European/UK enterprise contractors (Sisk, Mace, Galliford Try, Implenia) |

Also observed in the market (not core samples): Nialli Visual Planner (Nemetschek; LPS-designed visual planner importing the master schedule), Field Scribe Pull Planner (free/light pole), Space AI (AI lean platform, emerging), Oracle Primavera Cloud task management (suite-embedded LPS alignment — documented by the project-controls pass, not directly fetched this pass).

## Sources

Research date: 2026-09-10. All five sampled products fetched directly (evidence layer A):

- Touchplan — https://touchplan.io/ (homepage) and https://touchplan.io/digitize-lean-construction-planning/ (LPS phase walkthrough, via search capture of the official page)
- vPlanner — https://vplannerapp.io/products (vPlanner.Pull / vPlanner.Manage / vPlanner.Mobile)
- lcmd — https://www.lcmd.io/en/lean-construction (LPS, takt, pull planning, visual management, lean-method portfolio)
- Outbuild — https://www.outbuild.com/ (module map: Master Schedule, Lookahead, Weekly Work Plan, Roadblocks & Constraints, Pull Planning, Analytics) and https://www.outbuild.com/pull-planning-software (via search capture of the official page)
- VisiLean — https://visilean.com/planner (Planner: full CPM engine) and https://visilean.com/construction-management-solutions (five pillars: Plan/Collaborate/Communicate/Visualise/Control; via search capture of the official page)
- Methodology context: P2SL LPS 2020 Benchmark (Ballard & Tommelein, UC Berkeley) — https://p2sl.berkeley.edu/wp-content/uploads/2021/03/Ballard_Tommelein-2021-LPS-Benchmark-2020-2.pdf (linked from vPlanner's own site; not fetched directly)

No help-center depth was fetched for any product (marketing/product pages only); operational details below are kept at the strength of these pages. No numeric limits, default windows, or pricing asserted in the final document.

## Product A — Touchplan (evidence layer A)

- Self-positioning: "cloud-based, real-time platform for general contractor and specialty contractor collaboration"; "construction planning and scheduling software"; "Touchplan for Lean — Implement the Last Planner System®, Pull Plans, and Lookahead Plans Instantly".
- LPS phase support documented on the official Lean page: Phase Planning (team takes high-level tasks from the Master Schedule and conducts a Pull Plan for a specific phase); Look Ahead Planning ("the 'Can' phase" — activate the sequence into a look-ahead schedule, discuss what trade partners "can" do based on existing constraints); Make-Ready Planning (visualize/manage work based on current constraints; patented "Active Line" facilitates transition from long-range planning to detailed look-ahead; constraint log recorded early); Weekly Work Planning ("the 'Will' phase" — each trade partner commits to what they "will" do in the next seven days; weekly meeting reviews what happened since the last meeting); Daily Huddle ("the 'Did' phase" — review previous day's completed activities, discuss current day's tasks; Touchplan Mobile updates task statuses from the field).
- Measurement: "Basic Variance Report and Percent Plan Complete (PPC) metrics"; variance report highlights pinned tasks that didn't go according to plan (late, early, or in progress without status update); insights into "PPC, ticket statuses, milestones, constraints, team activity, crew planning".
- Collaboration posture: "Invites all team members into the planning environment by offering access to unlimited users"; "From trades to the Owner, gain buy-in"; "Pins represent real commitments"; "complete the full pull planning process without manually putting sticky notes on a wall"; "convert their pull plan into the look ahead schedule"; "all steps in the planning process beyond the master schedule, all within a single platform".
- Master schedule relationship: "Master Schedule Synchronization" is a named product pillar; "Sync Plans to the Master Schedule and transition from long-range pull plans to short-term lookaheads".
- Other named machinery: BoardScan (whiteboard digitization), Analytics, Reporting, API, crew management/staffing plans, Precision Time Planning page, patented planning software (US Pat. 10,410,178 B2).
- Users: General Contractors, Specialty Contractors, Owners, Architects and Engineers; industries incl. data centers, healthcare, infrastructure, life sciences.

## Product B — vPlanner (evidence layer A)

- Philosophy: "It is often said that projects should be managed as networks of commitments. Yet most teams implementing the Last Planner System® (LPS) are coached to represent their plans as disconnected activities without clear handoffs… We know that you cannot build a network without connections!" — handoffs are first-class.
- vPlanner.Pull: "collaborate on sequencing the work from any location in real-time while performing analytics to check if the work can be done when it is needed"; touch-friendly interface on large displays in the same space or remote participation; "Analyze the plan while being developed through automatic pull calculations to ensure the work sequence meets its targets"; identify late paths, organize late tasks, replan; print/distribute pull plans; publish pull plans to vPlanner.Manage; annotate with background graphics and labels.
- vPlanner.Manage: "comprehensive support for all the phases of the Enhanced Last Planner System®, takt planning, advanced metrics, analytics, and best-in-class integration with legacy CPM tools". Features: manage projects as production systems with visibility to work and constraints; takt planning incl. supply-chain workflows and constraints; automatic pull calculations identifying longest/late paths; "Automatically identify required tasks and backlog tasks"; integrated constraint logs prioritizing all known constraints; advanced metrics "Commitment Level (CL), Percent Required Complete or Ontrack (PRCO), and Milestone Variance (MV)"; "Automatically extract lookahead views and separate what CAN be done and SHOULD be done to stay on track. Isolate required work and backlog work"; LPS metrics "Percent Planned Complete (PPC) and Reasons for Variance and Root Causes"; roll-up to Gantt views; daily huddles and commitment status tracking; resource/hours forecasting; CPM import/export (activities, logic, codes, durations); scale to "thousands of activities with hundreds of users".
- vPlanner.Mobile: "access and status commitments from any location and using any device".
- Methodology positioning: supports the Enhanced LPS per the P2SL 2020 LPS Benchmark (near-term + long-term horizons, advanced metrics aligning near-term priorities with long-term milestones); claims to be the first commercial system supporting the expanded definition; LCI vendor partner and sustaining sponsor.

## Product C — lcmd (evidence layer A)

- Self-positioning: "the only fully integrated solution on the market for Lean Construction planning and execution… from strategic planning to day-to-day control on the jobsite. Everything in one tool."
- Digital LPS: "The LPS® is the core of the Lean approach" — weekly work planning; dependencies and commitments; daily stand-ups and planning boards.
- Takt planning: "structures construction projects into recurring time and process intervals. Clear Takts create consistent workflows… across all trades" — takt zones, sequences, dependencies; 1-click takt creation; automatic conflict and dependency checks.
- Pull planning: "consistently aligns the project schedule with the target completion date… dependencies and handoffs digitally visible, verifiable, and adjustable at any time — enabling realistic commitments, clear interfaces, and a reliable, jointly owned plan"; digital pull planning in real time; automatic transparency of dependencies and milestones.
- Visual management: dashboards & analytics for continuous improvement; visual boards for status; real-time KPIs "(e.g., Plan Percent Complete)".
- Lean-method portfolio beyond LPS (organization layer): Value Stream Mapping, Value Design / Target Value Delivery, A3 Thinking, 5S, Standard Work, IPD, Last Responsible Moment, Colocation Space, Continuous Improvement — each mapped to an lcmd capability.
- Execution layer: LPS, TAKT, Lookahead Planning ("Proactively detail upcoming weeks to identify constraints early… Automatically detect risks, blockers, and interfaces"), Daily Huddles/Stand-Ups, Visual Management.
- Platform: software + mobile app; BIM and Power BI integrations; help center on Zendesk; role-based solutions (project management, construction management, lean management, executive management, clients & project owners); company solutions (GCs, lead designers, developers & owners); European client base (Drees & Sommer, Implenia, PORR, DB InfraGO, Roche, Sanofi…).

## Product D — Outbuild (evidence layer A)

- Self-positioning: "the first fully integrated, AI-powered, collaborative scheduling and field coordination platform built specifically for construction"; footer taxonomy splits "Scheduling" (Master Schedule, Schedule Impact Request, Submittals, RFIs, CPM Schedule) from "Field Coordination" (Lookahead, Field Tracking, Weekly Work Plan, Roadblocks & Constraints, Pull Planning) and "Portfolio Management" (Projects Timeline, Executive Dashboard, Analytics).
- Master Schedule: "Build and update your contract schedule fast"; import from MS Project or P6.
- Lookahead: "Create Lookaheads directly from your master schedule. Your team can easily break down schedule activities into a sequence of field-focused tasks to plan their work. Progress updates on the lookahead automatically push to the master schedule."
- Weekly Work Plan: "field teams and trades to assign tasks and commit to them directly from the Lookahead. They can plan their upcoming week, track commitments, and ensure work is completed as planned."
- Roadblocks & Constraints: "Flag issues early so teams can fix them before they delay work"; roadblocks tied to one or multiple tasks, ownership visible; "Teams should load the plan with roadblocks, not hide them"; superintendents run the session and remove constraints; trade partners plan their own work by adding tasks directly.
- Pull Planning: "shared pull plan tied to your Lookahead and Master Schedule. Trade partners add their own tasks, then the team sequences the work together on screen… drag and drop tasks to build flow, validate handoffs, then commit the week"; iPad app for field; "No sticky notes."
- Analytics: "Percent Planned Complete, Percent Roadblock Removed, Reason for Variance, S-Curve, and more".
- Integrations: Procore, Trimble ProjectSight, Autodesk — "RFIs pulled into the Roadblock Log", submittals tied to schedule activities, drawings attached to lookahead tasks, real-time two-way schedule sync.
- Users: Owners, GCs, Trade Partners, Architects & Designers; mid-market and enterprise tiers; pricing starts at $12,000 annually (marketing fact — research notes only).

## Product E — VisiLean (evidence layer A)

- Self-positioning: "Award-winning cloud-based construction management software built on the Last Planner® System"; footer: "built on Lean principles with advanced BIM and analytics… real-time, integrated production management".
- VisiLean Planner (new product): "Full CPM engine. Real-time collaboration. Browser-native." — task scheduling (durations, dates, milestones, task types, calendars, constraint management), dependency logic (FS/SS/FF/SF with lag/lead), constraint engine (SNET, FNLT, Must Start/Finish, ASAP/ALAP), calendar management, CPM calculation (critical path, forward/backward pass, float analysis, dynamic auto-scheduling), WBS hierarchy, Gantt interaction, import/export (MPP, XER, XML, CSV, XLSX), handles 30K tasks (marketing figure — notes only).
- Comparison table self-declared: "Full CPM engine: Full support; Lean / Last Planner integration: Full support; Bidirectional execution sync: Full support" vs P6/MS Project/Asta (Lean "~" partial).
- Platform pillars (from solutions page): "Plan (CPM scheduling, Last Planner, Takt, P6/MSP/Asta import), Collaborate (commitments, lookahead, constraint mapping), Communicate (LiveSite mobile app, notes, photos), Visualise (live 4D BIM integration), and Control (PPC, DPR, variance analysis). Site updates flow to the office in real time without exports or spreadsheets."
- Customer evidence (testimonials): "Our Last Planner sessions used to take all day. With VisiLean, we finish in two hours and everyone leaves with clear commitments" (Lean Construction Manager, John Sisk & Son); "The constraint management alone paid for the platform. We catch blockers two weeks earlier than before" (SMP Alliance); "Importing from P6 and running collaborative sessions in the same tool" (Mercury Engineering).
- Also ships Reality Capture and Quality modules (adjacent capabilities — suite drift).

## Cross-product Comparison

| Structure | Touchplan | vPlanner | lcmd | Outbuild | VisiLean | Layer |
|---|---|---|---|---|---|---|
| Shared near-term commitment plan (lookahead + weekly work plan) | ✔ | ✔ | ✔ | ✔ | ✔ | universal in sample |
| Commitments made by performing parties (trades commit their own work) | ✔ ("each trade partner… commit") | ✔ (commitment management, huddles) | ✔ ("team commitments") | ✔ ("trades assign tasks and commit") | ✔ ("clear commitments" in LPS sessions) | universal in sample |
| Constraint/roadblock objects gating readiness | ✔ (constraint log, make-ready) | ✔ (integrated constraint logs, prioritized) | ✔ (constraint tracking; risks/blockers auto-detected) | ✔ (roadblock log, tied to tasks, ownership) | ✔ (constraint mapping; "catch blockers two weeks earlier") | universal in sample |
| Reliability measurement (PPC-class) + variance reasons | ✔ (PPC, Basic Variance Report) | ✔ (PPC + reasons + root causes; CL/PRCO/MV) | ✔ (Plan Percent Complete KPI) | ✔ (PPC, Reason for Variance, % Roadblock Removed) | ✔ (PPC, variance analysis) | universal in sample |
| Pull planning (collaborative reverse sequencing with handoffs) | ✔ (patented; BoardScan digitizes whiteboard) | ✔ (vPlanner.Pull; automatic pull calculations) | ✔ (digital, real-time) | ✔ (drag-and-drop, iPad) | ✔ (collaborative sessions; LPS) | universal in sample |
| Daily huddle / stand-up support | ✔ | ✔ | ✔ | (field tracking; huddle implied) | (LiveSite field updates) | common |
| Takt planning | ✖ (supports "LPS, Takt, IPD" methods per marketing list) | ✔ | ✔ (1-click takt, conflict checks) | ✖ | ✔ | variant |
| Master schedule: import/sync | ✔ (named pillar) | ✔ (CPM import/export) | (integrations; BIM/Power BI) | ✔ (own master module + two-way sync) | ✔ (own full CPM engine + import) | common |
| Owns a CPM calculation engine | ✖ | ✖ (imports/exports CPM) | ✖ | partial (master schedule module; CPM schedule page) | ✔ (full engine) | variant (packaging) |
| Mobile field app | ✔ | ✔ (vPlanner.Mobile) | ✔ | ✔ (iPad) | ✔ (LiveSite) | common |
| Portfolio/enterprise dashboards | (analytics/reporting) | (scale claims) | ✔ (executive/role solutions) | ✔ (executive dashboard) | (Power BI) | variant |
| AI assistance | ✖ observed | ✖ observed | ✖ observed | ✔ (Outbuild AI, agents) | ✖ observed | emerging variant |
| Broad stakeholder access posture | ✔ (unlimited users) | (hundreds of users) | (role-based) | ✔ (stakeholders at no extra cost) | (whole-team) | common (business-model expression) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures; remove any one and the product stops being recognizable as Lean Construction Planning:

1. **The shared near-term commitment plan of record** — a persistent, shared plan of upcoming site work held at two horizons (a lookahead of approaching work and a weekly work plan of promises), built with and held by the performing parties themselves. Remove → the calculated master schedule of Construction Scheduling, or a generic work plan.
2. **Make-ready constraint gating** — planned work carries its prerequisites as first-class constraint/roadblock objects (with ownership and status) that must be identified and cleared before work is promotable to a commitment ("can" before "will"). Remove → a task board with no readiness discipline.
3. **The promise-keeping reliability loop** — commitments are evaluated as done/not-done against the plan, completion measured (PPC-class), and reasons for variance recorded and fed back into re-planning. Remove → a lookahead planner with no accountability loop.

Binding: construction production semantics — the object world is site work broken into field-executable tasks by trade/crew, coordinated across trade partners. Remove the binding → generic kanban/task management.

Jointly-held load-bearing tests:
- 1 alone = shared work plan / collaborative schedule (no readiness discipline, no reliability loop)
- 2 alone = constraint/risk log
- 3 alone = completion tracker
- 1+2 without 3 = make-ready board with no accountability
- 1+3 without 2 = commitment tracking without quality gating
- 2+3 without 1 = constraint tracker + metrics with no shared plan

### L1 — Common Mature Structure (very common, not defining)

- Pull planning as the signature method for building phase plans (collaborative reverse sequencing, handoffs as first-class connections; digital sticky-note boards; automatic pull calculations at the vPlanner/VisiLean-class pole)
- Master schedule linkage (import or synchronization; progress flowing back)
- Daily huddle / stand-up support
- Mobile field surfaces for status updates
- Analytics dashboards (PPC trends, variance reports, S-curves)
- Broad stakeholder participation (trades, owners, designers invited; often free/unlimited seats as business-model expression)
- Meeting-routine support (weekly work plan meeting, daily huddle)

### L2 — Variant / Optional Structure

- Takt planning (takt zones, cadences, one-click takt) — lcmd, vPlanner, VisiLean; not universal
- Owning a CPM engine in-product (Outbuild master schedule module; VisiLean full engine) vs consuming an external master schedule (Touchplan sync; vPlanner import/export; Nialli import)
- Portfolio/enterprise dashboards and org-scale roll-up (Outbuild executive dashboard; lcmd role-based org solutions)
- Integrations with construction-management platforms (Procore, Trimble, Autodesk; RFIs/submittals feeding the constraint log)
- BIM/4D linkage (lcmd BIM, VisiLean 4D)
- AI-assisted planning (emerging: Outbuild AI/agents; Space AI)
- Regional/method breadth: lean-method portfolios beyond planning (lcmd: 5S, VSM, A3, TVD, IPD, Last Responsible Moment)
- Business model: unlimited/free stakeholder access vs seat-based

### L3 — Vendor-specific (research notes only)

- Touchplan: patented Active Line (long-range → look-ahead transition), BoardScan whiteboard digitization, US Pat. 10,410,178 B2, "Precision Time Planning" page, ROI marketing figures (50% delay reduction, 20% rework reduction, 50% meeting-time reduction)
- vPlanner: Enhanced LPS metrics CL/PRCO/MV; P2SL 2020 Benchmark positioning; "CAN vs SHOULD" separation; required vs backlog work isolation; vPlanner.Pull/Manage/Mobile module split
- lcmd: one-click takt creation, automatic clock-plan suggestion (testimonial claim), lean-method portfolio breadth, Power BI/BIM integrations, Zendesk help center
- Outbuild: Schedule Impact Request, submittals/RFI modules tied to schedule, $12,000 annual pricing floor, "450+ customers / $50B+ active projects" claims
- VisiLean: 30K-task capacity claim, ISO 27001/Cyber Essentials badges, Reality Capture and Quality modules, LiveSite branding
- Nialli: Nemetschek branding, PCL/PC Construction testimonials

## Rejected Findings (anti-overfitting)

- **Pull planning is NOT definitional.** It is the signature method and universal in-sample, but products can populate the lookahead directly from a master schedule import (Outbuild: "Create Lookaheads directly from your master schedule"; Nialli: "Imports data from your master schedule"; VisiLean: P6/MSP import). The commitment plan is the record; pull planning is one way to build it.
- **Master-schedule synchronization is NOT definitional** — it is the consumption seam with Construction Scheduling, present in most products but not required by the definition (a standalone phase-planning deployment satisfies the core).
- **The exact PPC formula name is not definitional** — the reliability-measurement leg is conceptual (done/not-done evaluation + reasons recorded); lcmd names it "Plan Percent Complete", vPlanner adds CL/PRCO/MV. No numeric targets or thresholds asserted.
- **The six-week lookahead window is NOT asserted** — Touchplan's marketing page says "six-week look ahead schedule" for its own process description; other products do not state a window. Held as a common convention, not a rule.
- **Daily huddle is NOT definitional** — common routine support, absent/implicit at some poles.
- **Takt is NOT definitional** — variant method supported by some products.
- **Digital pull-planning canvas with connecting arrows is NOT definitional** — the whiteboard is the predecessor artifact (BoardScan exists precisely to digitize it; Outbuild's own FAQ frames "no sticky notes" as the differentiator).
- **AI is NOT definitional** — emerging layer.

## Historical / Market-Sample Check (§24 discipline)

Would older, regional, platform-native products still fit? The Last Planner System itself predates its software: LPS was developed in the 1990s (Ballard; the P2SL 2020 Benchmark document vPlanner links describes the system's evolution), and its pre-software form was whiteboard/sticky-note pull planning sessions, spreadsheet lookaheads and weekly work plans, and manually computed PPC with variance reason tallies. That paper form satisfies all three L0 legs: a shared commitment plan held by the performing parties, constraint/make-ready tracking, and PPC measurement with recorded reasons. Touchplan's BoardScan and Outbuild's "no sticky notes" framing explicitly name the whiteboard/spreadsheet as the predecessor artifact. Regional check: US (Touchplan, vPlanner, Outbuild), German/European (lcmd, VisiLean — Finland/UK/India company), UK enterprise contractors (VisiLean testimonials) all fit. The definition does not depend on any single vendor's module names, patented mechanics, or metric vocabulary.

## Boundary Findings

### vs Construction Scheduling (§17, processed) — JOINT REVIEW DISCHARGED

The scheduling pass's flag is **RATIFIED keep-both** with its proposed discriminator confirmed from this side:

- **Object of record is the discriminator.** Construction Scheduling owns the calculated master schedule (activity network, durations + dependencies + calendars, critical path/float, baseline discipline). Lean Construction Planning owns the near-term commitment plan (lookahead + weekly work plan) built with the performing parties; the master schedule is consumed (imported/synchronized) as the upstream target, not calculated here.
- **Calculation machinery differs.** Scheduling derives dates from network logic (CPM). Lean products derive *readiness and sequence quality* (automatic pull calculations, late-path identification, constraint filtering, CAN-vs-SHOULD separation) — vPlanner and VisiLean document this explicitly. VisiLean ships a full CPM engine *and* the lean layer; Outbuild ships a master-schedule module *and* the lean layer — both are documented straddle poles where one product spans both Types; center of gravity (which record the product is sold to own) decides, and both vendors sell the lean layer as the differentiator.
- **Touchplan confirmed as the overlap zone** (lean workflow core + master-schedule synchronization as the consumption seam) — consistent with the scheduling pass's observation.
- The seam is soft (shared vocabulary: lookahead, activities, Gantt roll-ups) but the object worlds are distinct. Keep both Types.

### vs Construction Project Management (§17, processed)

PM manages the whole project record (RFIs, submittals, drawings, cost, documents, community of organizations). Lean planning centers the production commitment loop. Overlap exists at the integration edge (Outbuild pulls RFIs into the roadblock log; submittals tied to schedule activities) — that is integration, not PM core. Boundary held.

### vs Project Controls Platform (§17, unprocessed)

Controls = cost + schedule + risk + change governance at program level; lean planning = production reliability at the workface. Lean analytics (PPC, variance) are production metrics, not controls metrics. No conflict expected; joint review recommended when that leaf is processed.

### vs Construction Field Management (§17, unprocessed)

Field management records site execution events (daily logs, punch, safety, quality). Lean planning orchestrates near-term production commitments. Progress updates flow from field surfaces into both. VisiLean's LiveSite (field progress + quality checks) shows the adjacency; the commitment/make-ready machinery is the lean side's differentiator.

### vs generic Task Management / Kanban (§03.06)

A lean planning board looks kanban-like (cards, columns, statuses), but the construction production binding (trade partners, crews, handoffs, master-schedule lineage, make-ready constraint machinery, PPC) is absent in generic task tools. Remove the binding → generic task management.

### vs Production Planning / APS (§16, manufacturing)

Same word "planning", same "lean" ancestry (lean construction adapts lean manufacturing), different world: factory orders on work centers vs site commitments by trade partners. Different Type.

### vs Preconstruction Management (§17, unprocessed)

Preconstruction = estimating, bidding, constructability before field work. Lean planning = in-flight production planning once work is in execution. Forward note for that pass.

## Uncertainties

1. No help-center depth fetched for any sampled product (marketing/product pages only). Task/constraint state vocabularies, exact lifecycle transitions, and permission models are described generically; no precise state names asserted in the final document.
2. Oracle Primavera Cloud's LPS-aligned task management is taken from the project-controls pass's research notes, not fetched this pass — suite-embedded pole marked accordingly.
3. Nialli Visual Planner observed via search capture of its official homepage only; not counted as a core sample.
4. Whether pure-play lean products can run fully standalone (no master schedule at all) is not directly evidenced — Touchplan/vPlanner/Outbuild/VisiLean all document master-schedule linkage as standard. The definition does not require it, but market practice appears to assume it.
5. Exact PPC computation rules (which tasks count, on-time definition) vary and were not researched to precision — deliberately not asserted.
6. lcmd's "automatically creating clock plans" claim appears only in a customer testimonial — vendor-claimed capability, not independently verified.

## Final Synthesis

A Lean Construction Planning application is the site production team's collaborative commitment-planning system: it holds the near-term plan of construction work as a shared commitment plan (a lookahead of approaching work plus a weekly work plan of promises) built with and held by the performing trade parties; it gates the promotion of planned work into commitments through make-ready constraint management (prerequisites tracked as first-class constraint/roadblock objects with owners and status, cleared before "will"); and it closes the loop with promise-keeping measurement (PPC-class completion against the week's commitments, reasons for variance recorded, root causes identified) that feeds re-planning. Pull planning — collaborative reverse sequencing of a phase's work with handoffs as first-class connections — is the signature method for building the plan, and master-schedule linkage (import or synchronization, with progress flowing back) is the standard integration. Product philosophies diverge by pole: pure-play collaborative lean overlays synchronized with an external master schedule (Touchplan, vPlanner), org-scale lean transformation platforms with takt emphasis (lcmd), and combined platforms that own both a CPM engine and the lean layer (Outbuild, VisiLean). The commitment-plan-vs-calculated-master-schedule seam separates this Type from Construction Scheduling; the production-commitment loop separates it from Construction Project Management, Project Controls, Field Management, and generic task management.
