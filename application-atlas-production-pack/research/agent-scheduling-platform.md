# Research Notes — Agent Scheduling Platform

Research date: 2026-09-06
Directory leaf: "Agent Scheduling Platform" (Section 07 — Sales, Customer & Revenue; contact-center cluster)
Slug: agent-scheduling-platform

## Research Goal

Understand what an Agent Scheduling Platform for contact centers really is: its core objects, the workflow by which agent schedules are produced and maintained, the rules that govern assignment, the agent-facing side, and the boundary against neighboring Types (Workforce Management for Contact Centers, Employee Scheduling Platform, Time & Attendance, On-call Management, Contact Center Routing).

**Critical disambiguation:** in this part of the directory (contact-center cluster, next to Contact Center Platform / CCaaS / IVR / Contact Center Routing / Workforce Management for Contact Centers), "agent" means a **human customer-service agent**, not an AI agent. The leaf must not be confused with the AI-agent cluster leaves in Section 13 (Agent Development Platform, Agent Orchestration Platform, etc.).

## Initial Boundary (working hypothesis before research)

- Core use: produce and maintain work schedules for contact center agents so that staffing matches forecasted contact workload, under skill, availability, contract and labor constraints.
- Primary users: workforce planners / schedulers / WFM analysts (production side); agents and supervisors (consumption side).
- Nearest neighbors: Workforce Management for Contact Centers (broader discipline — scheduling is its central module), Employee Scheduling Platform (generic hourly-workforce shift scheduling), Time & Attendance (actuals, not plan), On-call Management (IT incident rotations), Contact Center Routing (consumes schedule outcome).
- Unknowns: does a standalone scheduling-only market exist (without forecasting/adherence)? How deep is agent self-service across the market? How do modern digital-support WFM tools differ from enterprise suites?

## Research Questions

1. What is the central object — schedule, shift, work plan, interval? How do they relate?
2. What inputs drive schedule construction (forecast, service goals, shrinkage, skills, availability, labor rules)?
3. What does the production workflow look like (auto-generation vs manual grid editing vs hybrid)? What lifecycle states does a schedule have?
4. How do agents interact with schedules (view, preferences, bidding, time-off, swaps)?
5. What happens intraday (reforecast, overtime/VTO, activity reassignment)?
6. Which rules/constraints materially shape behavior (labor law, seniority, fairness, rest, max hours)?
7. How does the platform connect to adjacent systems (ACD/routing, HR, payroll, time & attendance)?
8. Where is the boundary vs Workforce Management for Contact Centers and vs generic Employee Scheduling?
9. What variants exist (enterprise multi-site/BPO vs support-team SaaS; voice vs omnichannel; optimization-first vs manual-first)?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| NICE (CXone WFM + NICE WFM IEX) | Enterprise WFM leader; deep configurability + AI optimization; two product lines (cloud-native CXone WFM vs enterprise IEX) | Market leader; richest enterprise evidence |
| Verint Workforce Management (+ Calabrio One, now merged with Verint) | Enterprise WFM; governance/labor-law emphasis + agent-flexibility bots (TimeFlex) | Second major enterprise philosophy; Calabrio merger is a market fact |
| Genesys Cloud WFM | WFM embedded in a leading CCaaS platform; structured planner workflow | Only sampled product with fully public Tier-1 operational documentation |
| Zendesk WFM | Add-on WFM for support teams on a ticketing/helpdesk platform; lightweight auto-scheduling | Modern digital-support tier; different customer tier and philosophy |

Rejected/abandoned samples:
- **Assembled** (support-team WFM): www.assembledapp.com and help.assembledapp.com both failed with transport errors (2 attempts each) — abandoned per network rule.
- **Playvox**: playvox.com redirects to a tenant login page; help center is gated (only a handful of public articles; full help center requires login) — recorded as source-access limitation.

## Sources

Tier 1 (official operational documentation):
- Genesys Cloud Resource Center — "About workforce management" — https://help.mypurecloud.com/articles/about-workforce-management/ (fetched 2026-09-06)
- Genesys Cloud Resource Center — "Generate a schedule from a forecast" — https://help.mypurecloud.com/articles/75451/ (fetched 2026-09-06)
- Genesys Cloud Resource Center — "Schedule bids overview" — https://help.mypurecloud.com/articles/339969/ (fetched 2026-09-06)

Tier 2 (official product pages / FAQs):
- NICE — Workforce Management — https://www.nice.com/products/workforce-engagement/workforce-management (fetched 2026-09-06)
- NICE — Workforce Management (IEX) — https://www.nice.com/products/workforce-management/nice-iex-wfm (fetched 2026-09-06)
- Verint — Workforce Engagement — https://www.verint.com/workforce-engagement/ (fetched 2026-09-06; includes WEM/WFM FAQ and Calabrio merger statement)
- Zendesk — Workforce Management — https://www.zendesk.com/service/workforce-management/ (fetched 2026-09-06)

Unreachable / limited:
- calabrio.com now redirects to verint.com ("Calabrio is Now Verint") — Calabrio One product pages exist under verint.com; separate Calabrio documentation not fetched.
- Assembled — transport errors (abandoned).
- Playvox — login-gated; help center largely private.

## Product A — NICE (CXone WFM / NICE WFM IEX) — Tier 2

### Key observations (evidence layer A unless noted)

- Positioning: "helps contact centers forecast demand, build schedules, and adapt staffing as customer needs shift." WFM described as unifying "forecasting, scheduling, adherence tracking, and intraday reforecasting" in one platform.
- Two product lines: CXone WFM (cloud-native, digital-first, fast setup) vs NICE WFM (IEX) (enterprise-grade, highly configurable, for large complex operations). Same discipline, different depth/positioning — evidence that enterprise vs mid-market depth is a variant, not a Type boundary.
- IEX WFM FAQ (A):
  - "more than 45 AI-powered forecasting algorithms"; a "best pick" AI model selects the most accurate forecast per day.
  - Simulation tools "replicate real-world routing rules, agent skills, and multichannel behavior" so workforce plans reflect actual routing.
  - "Automated intraday reforecasting, queue-level net staffing analysis, and re-simulation" during the day.
  - "Schedule optimization … starts from the moment schedules are created. Then, throughout the day, the platform continually analyzes staffing and presents optimization suggestions … Managers can choose to apply the recommendations or adjust manually."
- Add-ons: Employee Engagement Manager ("automate intraday staffing tasks and give agents mobile self-service tools to manage schedules"); Enhanced Strategic Planner (long-term staffing plans, scenario modeling); Back Office WFM (non-customer-facing work).
- Main WFM page FAQ (A): "self-scheduling and shift bidding, agents get more flexibility—while managers keep service levels on track"; Copilot for Workforce Managers automates "shift change approvals and intraday adjustments".
- "True to Interval (TTI)" scheduling concept promoted in resources (vendor-specific naming).
- Case-study claims (adherence %, shrinkage %, cost savings) are marketing outcomes — not used as structural evidence.

## Product B — Verint Workforce Management (+ Calabrio One) — Tier 2

### Key observations

- Explicit WFM vs WEM definition (A): "Workforce Management (WFM) software provides forecasting, planning and scheduling capabilities. WEM software includes forecasting, planning and scheduling, but also provides performance management capabilities…" — direct vendor confirmation that scheduling is the defining core of WFM.
- Verint WFM positioning (A): "Accurately forecast, plan for and schedule resources for enterprises that need deeper structural, governance, regional labor laws, diverse operational needs, and advanced employee flexibility."
- AI forecasting (A): analyzes "historical volumes, work types and handle times – including asynchronous work across channels (chat, voice, email, SMS, etc.)" plus external events; "automatically compares the conditions with similar scenarios to select the forecasting model that best matches the parameters."
- AI scheduling (A): "automatically optimizes employee schedules to meet customer demand and employee scheduling preferences. The solution automatically ensures labor laws are adhered to for employee type, location and role."
- TimeFlex Bot (A): agents make "unlimited schedule changes" self-serve "without manager approvals"; "The TimeFlex Bot's proprietary model ensures that the overall schedule quality is maintained without the need for manual reviews"; claimed outcomes: attrition −30%, absenteeism −23% (marketing — not structural evidence).
- MyVerint mobile app (A): employees access schedules 24/7; "easily perform shift swaps and receive real-time notifications for voluntary time off or overtime."
- Workforce Intelligence (A): "intraday optimization, schedule change automation, predictive insights" embedded into existing Verint or Calabrio WFM.
- Calabrio Workforce Management (A): "robust, AI-powered WFM capabilities designed for the inbound contact centers looking for ease of use and the ability to balance the needs of the organization and the employee experience."
- Merger fact (A): "Verint and Calabrio have merged into one company… Calabrio Workforce Management and Calabrio Workforce Intelligence are now part of Verint's Workforce Engagement solution set."
- Case study titles confirm scheduling-time reduction as a core value metric (e.g., "Capitec Bank Reduces Manager Scheduling Time from Four Hours to 15 Minutes per Week"; Wix "cut time spent on agent scheduling by 40%").

## Product C — Genesys Cloud WFM — Tier 1 (full operational documentation)

### Key observations

Organizational / configuration model (A):
- Hierarchy: **Business units** (forecasted/scheduled as one unit, share resources) → **Management units** (departments/sites/locations; share start-of-week, labor constraints, shift-trade rules, adherence rules, time-off allowances) → agents. **Planning groups** define a workload of one media type + route paths, grouped for forecasting/scheduling. **Staffing groups** = agents with similar skillsets sharing absence allowances.
- **Service goal templates**: reusable specs of service level, average speed to answer, abandonment rate — at business-unit level.
- **Media types**: voice, email, chat, callback, messaging, workitem (routed tasks without direct customer interaction); chat concurrency modeled.
- **Activity codes**: activity types placeable on the schedule; fixed length; classified as paid time / work time / shrinkage time; interruptible or not; selectable or not for time-off requests.
- **Work plans**: shift definitions (start/end, embedded activities like back-office work, breaks, meals) + weekly constraints (min/max paid hours, max consecutive working days, required non-working time between shifts) "to align with labor contracts"; permanent or temporary assignments; **rotations** (weekly sequences of work plans); **work plan bids**.

Forecasting (A):
- Methods: Automatic Best Method (selects most accurate model from historical data), Weighted Historical Index (user-weighted past periods), CSV import of external forecasts, continuous "Main Forecast" recalculated nightly.
- **Capacity planning**: identifies over/under-staffing and hiring needs.

Scheduling (A):
- **Generate load-based schedules** — "an automated scheduling method based on the forecasted workloads to meet service goals efficiently."
- **Manual schedules** without a forecast ("useful if the agents always work at the same time") and blank schedules — manual mode is a supported degenerate path.
- Schedule generation details (A, from "Generate a schedule from a forecast"):
  - Select business unit; schedule period type monthly or weekly; short-term schedules max six weeks; forecast period must cover the schedule period.
  - Agents must be marked "schedulable".
  - Options: Activity Smoothing (concurrent-activity distribution), Schedule Variability (randomization so the same agent doesn't always get the same shift combination).
  - Generation "may take 20 minutes or longer"; one business unit at a time; results listed under "Last Scheduling Attempts".
  - Schedule editor: assign/swap shifts between agents, replace shifts with activities, copy activities/shifts to agents or days, adjust times, add/remove agents; views by day/date range/week/vertical; metrics rows: scheduled vs required (with and without shrinkage), difference, performance; adherence columns for past schedules; multi-timezone display.
  - **Publish**: only one published schedule per date range; a new published schedule must fully encompass the one it replaces; no overlapping adjacent published schedules. Unpublished schedules can coexist for planning.
- **Activity plans**: schedule recurring or ad hoc activities (training, team meetings, compliance briefings) at times aligned with coverage.
- **Block scheduling** exists as a concept (overview article listed).

Agent-facing (A):
- Self-service via desktop and mobile: view schedule ("My Schedule"), submit time-off requests, shift trades.
- **Time-off**: limits (daily maximum hours per management unit), time-off plans linking activity codes to limits, requests auto-evaluated — "auto-approves the requests that meet all conditions and others require manual review"; HR system integration.
- **Shift trades**: agents exchange entire shifts; configurable rules/criteria (matching skills or queue assignments); auto or manual approval; "Alternative Shifts" = swap with the house.
- **Work plan bids / schedule bids**: agents bid on preferred work plans or schedule sets for future periods; system analyzes the bid configuration and "suggests the proper number of agents that should be assigned to each work plan"; agents submit ranked preferences (no queue mechanism); sorted "by hire date or performance ranking"; assigned based on preferences + available slots; future schedules automatically pick up allocations from the effective date. License-gated (CX 3/4 etc.) — vendor packaging detail.
- **Opportunities**: schedulers publish structured, time-bound work assignments (e.g., extra shifts) that agents request; approved requests auto-apply to schedules.

Intraday / feedback loop (A):
- **Intraday monitoring**: compares forecasted vs actual per planning group in 15/30/60-minute intervals; visual discrepancy indicators; configurable targets for answered/abandoned/completed.
- **Real-time adherence** + **historical adherence**; adherence explanations (agent-submitted; approved explanations excluded from calculations).
- **Historical shrinkage**: records scheduled and actual shrinkage "when agents were scheduled for interactions but were unable to fulfill them"; used to refine staffing models.
- Permissions (Add/Delete/Edit/Publish/View per WFM function), audit logging, APIs, CSV import/export.

## Product D — Zendesk WFM — Tier 2 (marketing page; support-team tier)

### Key observations

- Positioning (A): WFM as an add-on for service teams on the Zendesk platform: "Forecast, staff, and manage agent schedules with AI-powered precision."
- AI-powered staffing forecast (A): "analyzes your historical data to predict staffing needs in a given day, month, or season. Cut down on overtime costs and lower wait times."
- Automatic agent scheduling (A): "Create schedules down to the minute—including training, breaks, and ticket types. Agents get full visibility too."
- Real-time activity tracking (A): "View what agents are working on… how they spend their time in and out of Zendesk, and how well they adhere to schedules."
- Agent visibility (A): "Everyone can view their schedule… they'll know exactly when they're overachieving or need help."
- Customer quote (A, testimonial): scheduling time reduced "from 3 hours … to 30 minutes" — consistent with the cross-product value narrative (scheduler time reduction), though testimonial evidence is weak.
- Packaging (A): available to customers "on any Basic or Suite plan" as an add-on — vendor packaging detail.
- No evidence fetched on bidding, time-off workflows, or intraday reforecast for Zendesk — claims about those capabilities are NOT made for this product.

## Cross-product Comparison

| Dimension | NICE (CXone/IEX) | Verint (+Calabrio) | Genesys Cloud | Zendesk WFM |
|---|---|---|---|---|
| Central artifact | schedule (built from forecast; optimized at creation + intraday) | schedule ("forecast, plan for and schedule resources") | schedule (load-based generation from forecast; manual mode; publish lifecycle) | schedule ("automatic agent scheduling… down to the minute") |
| Demand input | AI forecast (45+ algorithms, best-pick), simulation of routing/skills | AI forecast incl. async channels + external events | Forecast module (Automatic Best Method / Weighted Historical Index / import; nightly continuous forecast) | AI staffing forecast from historical ticket data |
| Staffing target | service levels kept "up" while costs down | meet customer demand + preferences; labor-law compliant | service goal templates (SL/ASA/abandonment) → required staffing (with/without shrinkage) | staffing needs prediction (overtime/wait-time framing) |
| Schedule construction | automated optimization + manager apply-or-adjust | automatic optimization under labor laws | load-based generation + full manual grid editor + publish rules | automatic scheduling; manual detail not evidenced |
| Shift templates | implied (scheduling engine) | implied | explicit work plans: shifts + activities + weekly constraints + rotations | training/breaks/ticket types embedded in schedules |
| Agent self-service | self-scheduling, shift bidding; mobile self-service (EEM add-on) | TimeFlex unlimited self-serve changes; MyVerint app (swaps, VTO/OT notifications) | My Schedule, time-off requests (auto-evaluated), shift trades, work plan bids, opportunities | schedule visibility (deeper self-service not evidenced) |
| Intraday | automated reforecasting, net staffing analysis, re-simulation, suggestions | intraday optimization, schedule change automation (Workforce Intelligence) | intraday monitoring (forecast vs actual per interval), adherence | real-time activity tracking + adherence |
| Feedback loop | adherence tracking in suite | adherence (15% improvement case claim) | adherence + historical shrinkage feed staffing models | adherence reporting |
| Org structure | enterprise multi-site (implied) | enterprise governance, regional labor laws | business units → management units → planning/staffing groups | team-level (support teams) |
| Suite position | WFM inside WEM suite inside CX platform | WFM inside WEM suite; Calabrio merged in | WFM module inside CCaaS platform | add-on inside service/ticketing platform |

Cross-product commonalities (evidence layer B):
1. The **schedule** (agent × time assignments over a schedule period) is the central managed artifact in all four.
2. All four derive staffing needs from **predicted workload** (forecast) before or during scheduling.
3. All four treat **skills/queues/work types** as a scheduling dimension (routing-aware scheduling).
4. All four expose the schedule to **agents** (visibility at minimum).
5. All four operate on a **planning cadence** (schedule periods; forecasts refreshed; nightly/continuous recalculation evidenced in Genesys, "best pick per day" in NICE).
6. Three of four (NICE, Verint, Genesys) show **intraday adjustment** as a first-class activity; Zendesk evidences real-time tracking only.
7. Three of four (NICE, Verint, Genesys) show **agent self-service beyond viewing** (bidding, swaps, time-off); Zendesk evidences visibility only.
8. All four frame value as: meet service goals with fewer paid hours / less scheduler effort / better agent experience.

## Canonical Model (synthesis)

### L0 — Defining Invariant (minimal)

1. **Schedulable agent population** — identified employees with skills/qualifications, treated as the resource being scheduled.
2. **The schedule as central artifact** — a persistent plan binding specific agents to specific work times (shifts) across a schedule period, organized by operational unit.
3. **Demand-derived staffing targets** — required staffing per time interval computed from predicted interaction workload and service goals; schedule construction aims to meet these targets (manual construction exists as a supported degenerate mode, but the target structure remains the organizing principle).
4. **Rule-governed assignment** — assignments constrained by skills, availability, working-time rules (hours, rest, contracts/labor law).
5. **Distribution to agents** — the published schedule is visible to the agents it binds.

Remove #3 → generic Employee Scheduling Platform. Remove #1/#2 → no scheduling product. Remove #5 → a planner's private spreadsheet, not a platform.

### L1 — Common Mature Structure

- Forecasting module (multiple methods, model auto-selection, import) or forecast import as upstream input
- Shift/work-plan templates: start/end patterns, embedded activities (breaks, meals, training, meetings), weekly constraints (min/max hours, max consecutive days, min rest), rotations
- Schedule editor: agent × day timeline grid; assign/swap/copy/adjust shifts and activities; scheduled-vs-required comparison (with/without shrinkage)
- Publish lifecycle with uniqueness rules (one published schedule per period; replacement semantics)
- Agent self-service: view schedule, time-off requests (limits + auto-evaluation), shift trades/swaps (rule-checked, auto/manual approval), work-plan bidding (seniority/performance-ranked allocation)
- Intraday management: forecast-vs-actual monitoring per interval, reforecast, overtime / voluntary time off, activity reassignment
- Adherence tracking (real-time + historical) and shrinkage analytics feeding back into staffing models
- Activity codes classifying scheduled time (paid / work / shrinkage; interruptible or not)
- Multi-level org structure (business unit / site / team), multi-timezone, multi-skill & omnichannel workloads (incl. async work and concurrency)
- Roles & permissions (planner/admin, supervisor, agent), audit, APIs
- Integrations: ACD/routing (queues, skills, handle-time data), HR/payroll, time & attendance

### L2 — Variant / Optional Structure

- Suite position: standalone scheduling tool vs WFM-suite module vs CCaaS-embedded vs helpdesk add-on
- Channel scope: voice-centric legacy vs omnichannel (chat concurrency, messaging, email, back-office work items)
- Optimization posture: algorithm/AI-optimization-first vs manual-grid-first vs hybrid (apply-or-adjust)
- Agent-flexibility posture: fixed published schedules vs self-scheduling / bidding / unlimited self-serve changes
- Labor-law governance depth (regional rule engines, union/contract rules)
- Scale & segment: enterprise multi-site/BPO vs single support team
- Long-term/strategic capacity planning (hiring, scenarios) as an extension above short-term scheduling
- Deployment: cloud vs on-premises legacy
- Back-office / non-customer-facing workforce scheduling as an extension of the same machinery

### L3 — Vendor-specific (research notes only)

- NICE: IEX vs CXone WFM product split; "True to Interval (TTI)"; 45+ forecasting algorithms; Employee Engagement Manager; Enhanced Strategic Planner; Copilot for Workforce Managers; Back Office WFM.
- Verint: TimeFlex Bot; MyVerint mobile app; Workforce Intelligence bots; Da Vinci AI; WEM category framing; Calabrio merger packaging.
- Genesys: business unit / management unit / planning group / staffing group hierarchy; activity codes; service goal templates; opportunities; alternative shifts; schedule-bid license gating; 15/30/60-min intraday intervals; six-week short-term schedule cap; 20-minute generation time; nightly continuous forecast.
- Zendesk: ticket-type scheduling dimension; plan-gated add-on packaging.

## Rejected Findings

- "Agent scheduling = AI agent scheduling" — rejected: in this directory region "agent" is the human contact-center agent; the AI-agent cluster is a different section (13) with different Types.
- "Scheduling platforms always include quality management / gamification / voice-of-customer" — rejected: those are WEM-suite siblings (Verint explicitly separates Quality Automation from WFM); not part of this Type.
- "Self-scheduling/unlimited schedule changes are definitional" — rejected: only some products (Verint TimeFlex, NICE self-scheduling) position this as central; Genesys supports it as configurable features; older/enterprise deployments run fixed published schedules. L1/L2, not L0.
- "Forecasting is part of the scheduling platform" — partially rejected as a definitional claim: forecasting is inseparable in practice (all sampled products include or import forecasts), but Genesys explicitly supports schedule generation without a forecast and forecast import from external systems. So: demand-derived staffing targets are definitional; the forecasting engine itself is common-but-not-definitional.
- Marketing outcome numbers (44% attrition reduction, 94–95% adherence, $1M savings, 4h→15min scheduling) — rejected as structural evidence; vendor marketing.

## Boundary Findings

1. **vs Workforce Management for Contact Centers** — the closest and hardest boundary. Verint's own definition: WFM = "forecasting, planning and scheduling"; WEM adds performance management. In the market, agent scheduling is almost never bought standalone — it ships inside WFM suites (NICE, Verint/Calabrio, Genesys) or as WFM add-ons (Zendesk). The scheduling platform is best understood as the **scheduling core of contact-center WFM**: the schedule artifact, its generation/editing/publishing lifecycle, and the agent-facing schedule services. WFM adds forecasting as a first-class planner discipline, adherence, and (in WEM framing) performance/quality siblings. Test: if the product's center of gravity is producing/maintaining/publishing the schedule and handling agent schedule requests, it is this Type even when bundled in a WFM suite; if the center of gravity is the forecast→adherence→performance discipline as a whole, it is Workforce Management for Contact Centers. **Taxonomy note:** the two directory leaves are tightly coupled; scheduling is WFM's central module; a future consolidation pass may want to treat one as the parent.
2. **vs Employee Scheduling Platform** (Section 09) — generic shift scheduling for hourly workforces (retail, hospitality, healthcare). Distinction: contact-center agent scheduling is driven by **interval-level staffing requirements computed from interaction-volume forecasts and service goals** (queue/skill-aware, shrinkage-adjusted, routing-integrated), whereas generic employee scheduling works from simpler coverage rules and shifts without queue-level demand math. Remove the forecast/service-goal/routing machinery and only generic shift scheduling remains → different Type.
3. **vs Time & Attendance System** — T&A records actual worked time (clocks, timesheets, attendance); scheduling plans future work. They integrate (scheduled vs actual, adherence), but central objects differ (plan vs actuals).
4. **vs On-call Management** (Section 14, IT) — rotations of engineers for incident response; not demand-forecast-driven staffing of a service queue; different domain and objects.
5. **vs Contact Center Routing Platform** — routing consumes the schedule's outcome (which agents are on, with which skills, at which time); scheduling does not route interactions.
6. **vs Interview Scheduling / Meeting Scheduling / Appointment Scheduling** — calendar-appointment domain for events/meetings; not workforce shift planning. Name similarity only.
7. **vs AI-agent orchestration leaves** — "agent" disambiguation as noted above.

## Uncertainties

- Modern support-team SaaS tier (Assembled, Playvox) could not be verified from official docs (transport errors / login-gated). The support-team variant is evidenced only by Zendesk's marketing page (Tier 2). Claims about that tier are kept weak.
- Whether a meaningful market of standalone scheduling-only products (no forecasting, no adherence) exists — not verifiable from the sampled sources; the sampled market uniformly bundles scheduling with forecasting at minimum.
- Precise operational limits (schedule-period caps, generation durations, intraday interval sizes, license gating) were observed only in Genesys documentation — treated as product-specific facts, not generalized.
- Calabrio's product documentation was not independently fetched post-merger; Calabrio evidence comes from Verint's pages describing the merged lineup.
- The exact split of scheduling vs forecasting module ownership varies by product (some sell forecasting as a separate module/add-on); the canonical model treats forecasting as upstream input with variable packaging.

## Final Synthesis

An Agent Scheduling Platform (contact center) is the system of record for **who works when**: it maintains a population of schedulable agents with skills, converts predicted interaction workload into interval-level staffing requirements, produces a schedule that binds specific agents to specific shifts and activities under skill/availability/labor constraints, publishes it to agents, and then keeps the schedule alive intraday (reforecast, adjust, overtime/VTO) while recording how reality diverged (adherence, shrinkage) to improve the next cycle. Agents interact with the schedule as a first-class surface (view, time-off, trades, bids). Forecasting, adherence and performance are sibling disciplines that surround scheduling — usually in the same WFM suite — but the schedule and its lifecycle are this Type's defining center.
