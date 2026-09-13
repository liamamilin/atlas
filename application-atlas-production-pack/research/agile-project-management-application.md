# Research Notes — Agile Project Management Application

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an "Agile Project Management Application" is as an Application Type: what objects exist inside it (backlog, work item, board, iteration, epic, release…), how work flows from idea to done, what makes the planning model "agile" rather than plan-driven, which capabilities are common but not defining, and where the Type's boundary sits against Project Management Application, Kanban Task Board, Task Management, Issue Tracker, and the broader work/product management platforms.

## Initial Boundary (hypothesis before research)

- Hypothesis: a team-centric application that supports iterative, incremental delivery — an ordered backlog of work items, timeboxed iterations (sprints) and/or kanban flow on a visual board, lightweight estimation, and agile feedback metrics (velocity, burndown, cumulative flow).
- Likely confusions:
  - **Project Management Application** (sibling under 03.07) — suspected boundary: plan/schedule-centric (Gantt, dependencies, baselines) vs backlog/cadence-centric.
  - **Kanban Task Board** (sibling under 03.06) — board alone vs board + backlog + cadence + agile metrics.
  - **Issue Tracker / Bug Tracking System** (§12) — defect lifecycle as primary object vs planned delivery work.
  - **Work Management Platform / Product Management Platform** — generic organizational work / upstream product planning vs team delivery cadence.
  - **Engineering Project Management Platform** (§12) — suspected heavy overlap with this leaf; both used for software delivery tracking.

## Research Questions

1. What are the core objects (backlog, work item/story, board, iteration, epic, release) and how do they relate?
2. How does the iteration lifecycle work: plan → execute → complete → carry-over? What happens to unfinished work?
3. How does kanban-style continuous flow coexist with scrum-style timeboxes in the same products?
4. What estimation structures exist, and are they required?
5. What agile metrics are derived (velocity, burndown, CFD, lead/cycle time) and from what data?
6. What sits above the team backlog (epics, features, releases, roadmaps, multi-team plans)?
7. Which roles exist (product owner, scrum master, team member, admin, stakeholder) and what do they control?
8. Which rules govern board/workflow behavior (column mapping, WIP limits, definition of done, done-state mapping)?
9. Where is the boundary to general project management, task management, kanban boards, and issue trackers?
10. Do older (XP/Scrum-era) and kanban-only products fit the same defining structure?

## Representative Products

Selected for market coverage + documentation quality + different philosophies + different customer tiers:

| Product | Segment / philosophy | Core vocabulary | Evidence quality |
|---|---|---|---|
| Jira (Atlassian) | Market-standard; configurable issue/work tracker that became the agile default; SMB→enterprise | work item, backlog, sprint, epic, version, board | Tier 1 (support docs directly fetched) |
| Azure Boards (Microsoft) | Enterprise ALM suite; teams + process templates; plan/track at scale | work item, backlog, board, sprint (iteration path), delivery plan | Tier 1 (Microsoft Learn docs directly fetched) |
| Linear | Modern opinionated tool for software teams; speed/minimal-overhead philosophy | issue, cycle, project, initiative, triage | Tier 1 (docs directly fetched) |
| Zoho Sprints | SMB dedicated agile tool; scrum-first with kanban-adjacent features | backlog, epic, sprint, scrum board, release | Tier 2 (product site; help center JS-blocked) |
| Taiga | Open-source, self-hostable; scrum + kanban dual modules | backlog, sprint, kanban, epic, issue | Tier 2 (product site + community docs; self-hosting docs fetched) |

Rejected / unreachable sample:

- **Pivotal Tracker** — historically the archetypal opinionated iteration-based tool; pivotaltracker.com and its help docs transport-errored twice and were abandoned per network rules. No operational claims are made from memory; noted as an evidence gap.

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-06):

- Jira Software Cloud support (Atlassian):
  - What is a sprint? — https://support.atlassian.com/jira-software-cloud/docs/what-is-a-sprint/
  - View and understand the velocity chart — https://support.atlassian.com/jira-software-cloud/docs/view-and-understand-the-velocity-chart/
  - Documentation hub (full tree: scrum/kanban backlogs, epics, versions, sprints, reports incl. burndown/burnup/CFD/control/velocity/sprint/version, board configuration incl. columns/swimlanes/estimation, timeline/roadmap, team-managed agile feature toggles) — https://support.atlassian.com/jira-software-cloud/resources/
- Azure Boards (Microsoft Learn):
  - What is Azure Boards — https://learn.microsoft.com/en-us/azure/devops/boards/get-started/what-is-azure-boards
  - Tutorial: Assign Backlog Items to a Sprint — https://learn.microsoft.com/en-us/azure/devops/boards/sprints/assign-work-sprint
  - About Kanban boards — https://learn.microsoft.com/en-us/azure/devops/boards/boards/kanban-overview
- Linear docs:
  - Docs hub — https://linear.app/docs
  - Start Guide — https://linear.app/docs/start-guide
  - How to use Linear: Small teams — https://linear.app/docs/how-to-use-linear-small-teams
  - Cycles — https://linear.app/docs/use-cycles
  - Projects — https://linear.app/docs/projects
  - Issue status (workflows) — https://linear.app/docs/configuring-workflows

Tier 2 (official product pages, directly fetched 2026-09-06):

- Zoho Sprints — https://www.zoho.com/sprints/ (module pages: backlog, scrum board, release, timesheet; agile guide)
- Taiga — https://taiga.io/ (feature pages for Scrum, Kanban, Issues, dashboards)

Source-access limitations:

- pivotaltracker.com and its help articles transport-errored twice; source abandoned. Historical-market checks therefore rely on the four verified products plus Taiga; no precise claims about Tracker are made.
- Zoho Sprints help center (help.zoho.com) returned an empty JS shell; Zoho evidence is limited to product-site descriptions of modules. Assertion strength reduced accordingly (no precise operational defaults claimed for Zoho).
- Taiga's docs.taiga.io is self-hosting/API documentation; user-facing behavior was confirmed from the product site's feature descriptions (community links) and kept at moderate strength.
- No third-party reviews were needed; official sources were sufficient for the structure.

## Product Observations

### Jira (evidence layer A — direct observation of official support docs)

Object structure:

- **Work item** (issue) is the unit of work; types include story, bug, task, epic, subtask; work items carry fields (story points, time estimates, sprint field, fix version), can be ranked, linked, transitioned through configurable **workflows** (statuses + transitions).
- **Backlog** (scrum backlog page; a kanban backlog variant exists) is where work is planned: rank, groom, estimate, assign to sprints.
- **Sprint** — "a short period in which the development team implements and delivers a discrete and potentially shippable application increment"; also called an iteration; planned from the Backlog tab; viewed on a board; issues are assigned to sprints (sprint is a queryable field); Scrum-only feature; docs recommend a fixed two-week duration for teams new to sprints. Parallel sprints exist as an option.
- **Board** — scrum board (sprint-scoped) or kanban board (continuous); columns map to workflow states; right-most column = "Done" for reporting; configuration includes columns, swimlanes, quick filters, card fields, estimation and tracking method (story points, original time estimate, work item count, or any numeric field), WIP constraints ("work item limits").
- **Epic** — large body of work above stories; epics exist in both scrum and kanban spaces.
- **Version (release)** — delivery container; work items associated with fix versions; release pages track progress.
- Reports (derived from board state + estimates): sprint report, burndown chart, burnup, velocity chart, control (cycle time) chart, cumulative flow diagram, epic report/burndown, version report, release burndown.
- **Velocity chart mechanics (directly documented)**: velocity = average of total completed estimates over the last several completed sprints; commitment bar frozen at sprint start; scope added after start counts toward completed; chart is board-specific and based on the board's column mapping; sub-task estimates excluded.
- **Timeline/roadmap** above epics with dependencies, roll-up dates, releases; **plans** (Advanced Roadmaps) for cross-project/multi-team planning with program boards.
- Agile features in team-managed spaces are individually toggleable (enable backlog, sprints, estimation, releases, reports) — evidence that backlog/board/sprint/estimation/reports are separable capabilities, not one monolith.
- Ceremony support exists (run a standup in Jira); capacity planning per individual; components group work by area.

Roles/permissions: space roles, company-managed vs team-managed governance split; dashboards shareable.

### Azure Boards (evidence layer A — direct observation of Microsoft Learn docs)

Object structure:

- **Work item** — unit of work; predefined types: Epic, Feature, User Story / Product Backlog Item / Requirement / Issue (varies by process template: Agile/Scrum/CMMI/Basic), Task, Bug; work item form captures discussion, history, attachments; links build hierarchies and traceability; leaf-node display rule on boards.
- **Backlogs** hub — product backlog is "an interactive list of work items that corresponds to a team's project plan or roadmap"; supports prioritizing, forecasting by sprints, linking to portfolio backlog items; **portfolio backlogs** (Features, Epics; additional levels customizable) group work above stories.
- **Boards hub** — Kanban boards per product/portfolio backlog; cards, columns mapped to workflow states, WIP limits, split columns (pull), swimlanes (service classes), definition of done per column, card checklists of tasks; CFD in context; lead time (proposed→completed) and cycle time (in-progress→completed) defined and widgetized.
- **Sprints hub** — sprints are **iteration paths** defined per team; Planning pane drag-and-drop from backlog to sprint; Planned Effort = sum of Story Points/Effort of assigned items; team capacity per member; sprint **Taskboard** is sprint-scoped and tracks tasks; sprint burndown and capacity charts monitor the sprint.
- **Teams as first-class structure**: each team defines its own area paths, iteration paths, backlogs, boards, sprints; "each team can manage its own backlog and boards"; team-level board configuration cannot be shared across teams.
- **Delivery Plans** — cross-team calendar view of deliverables/dependencies with rollup progress for features/epics.
- **Queries, dashboards, Analytics/Power BI** for triage, trend charts, reporting.
- State categories normalize workflow states into Proposed / In Progress / Resolved / Completed across types.
- Permissions/access: Basic vs Stakeholder access levels; Contributors group; work tracking permissions per node.

Kanban board vs Taskboard distinction (documented): kanban boards track requirements independent of any sprint with CFD; taskboards are sprint-scoped and track tasks, monitored via capacity and sprint burndown.

### Linear (evidence layer A — direct observation of official docs)

Object structure:

- **Issue** is the atomic unit: "a specific piece of work… that has a clear output and might take anywhere from a few minutes to a day"; zero-friction creation is a stated design goal; properties include status, priority, estimate, labels, due date, relations (blocking/blocked/related/duplicate), parent/sub-issues.
- **Workflow statuses** — team-specific; default set Backlog > Todo > In Progress > Done > Canceled; status categories in fixed order; reserved system Duplicate status; auto-close/auto-archive policies; Triage status category as an inbox for incoming/integration issues.
- **Cycles** — "time-boxed periods where a team works on completing a pre-defined set of work", explicitly "similar to commonly used agile-flavored sprints" but "unlike sprints, not tied to releases"; automatically created on a repeating schedule (1–8 weeks, chosen start day), optional cooldown period; **unfinished issues roll over automatically** into the next cycle; capacity dial estimated from the **velocity of the previous three completed cycles** (issues or estimate points completed); cycle graphs show effort and scope over time.
- **Projects** — larger units with a clear outcome and planned completion date; issues + documents + milestones; project status (On track/At risk/Off track), updates, progress graph with completion estimates; shared across teams.
- **Initiatives** — roadmap-level grouping above projects.
- **Teams** — workspace organized into teams (mimicking org structure; sub-teams inherit parent cycle schedules); each team has its own workflows, cycles, triage.
- Estimation is optional (t-shirt-style magnitudes or custom); some teams run without cycles (continuous flow + triage).
- Integrations (GitHub/GitLab/Slack) automate issue status from PRs; importers from Jira/GitHub/Asana/Shortcut/Trello.
- Philosophy (documented): "plan, track, and deliver work without a lot of overhead"; for small teams, start with issues immediately rather than over-planning.

### Zoho Sprints (evidence layer B — product site only; help center unreachable)

- Positioned as "agile project management software for dynamic teams"; module set explicitly named: **Backlog, Epics, Release, Board (Scrum Board), Reports, Timesheet, Meetings**.
- Backlog described as the place to "collect all your project ideas… refine work items that are sprint-worthy, and start your sprint".
- Scrum board described as "the central workspace" where teams "push a work item from its To-do status to Done across the board" during an ongoing sprint.
- Release module: short releases with customizable workflow stages; work items associated to releases, moved Plan → Released.
- Timesheet: log hours, billable/non-billable, approve/reject time logs.
- Content marketing confirms the standard conceptual vocabulary (product backlog, sprint planning, user stories, kanban vs scrum) — used only as confirmation of vocabulary, not of operational mechanics.

### Taiga (evidence layer B — product site + community docs)

- Open-source agile PM platform, self-hostable; explicitly framed "for cross-functional agile teams".
- **Scrum module**: backlog & sprint planning, epics and sub-tasks, estimations, sprint task board with swimlanes per user story, burndown chart at project and sprint level; a Scrum project "can switch over to Kanban and vice versa" — direct evidence that scrum and kanban are two postures of the same object structure.
- **Kanban module**: customizable workflow, WIP limits, swimlanes, epics, archive.
- **Issues module**: separate bug/issue tracking with custom types/severities; "possibility to add issues to sprint"; "function to promote issue to user story" — in-product evidence of the issue-tracker → backlog boundary.
- Dashboards/reporting, wiki, roles & permissions, >20 languages; importers from GitHub/Jira/Trello.

## Cross-product Comparison

| Structure | Jira | Azure Boards | Linear | Zoho Sprints | Taiga | Verdict |
|---|---|---|---|---|---|---|
| Ordered, re-rankable backlog of work items | ✔ scrum/kanban backlog | ✔ product backlog (+ portfolio) | ✔ Backlog status + ranking | ✔ Backlog module | ✔ backlog | Universal → defining |
| Work item with status moving through workflow to Done | ✔ configurable workflow | ✔ states + state categories | ✔ status categories, fixed order | ✔ To-do→Done | ✔ stages + close definition | Universal → defining |
| Board as card/column tracking surface | ✔ scrum + kanban boards | ✔ kanban boards (+ taskboard) | ✔ board views | ✔ Scrum board | ✔ sprint task board + kanban | Universal → defining |
| Team as owning unit of backlog/board/cadence | ✔ space/board; team-managed spaces | ✔ first-class teams; per-team settings | ✔ teams; per-team workflows | ✔ project/sprint teams | ✔ project members/roles | Universal → defining |
| Bounded delivery cadence: timeboxed iteration OR continuous flow | ✔ sprints (scrum) + kanban | ✔ sprints (iteration paths) + kanban independent of sprints | ✔ cycles (optional) + continuous flow + triage | ✔ sprints | ✔ sprints ↔ kanban switch | Universal as a pair of alternatives → defining |
| Lightweight estimation (points/t-shirt/count) | ✔ points/time/count/numeric field | ✔ story points/effort | ✔ optional estimates | ✔ story points (implied by modules) | ✔ estimations | Common (kanban flow often estimate-free; Linear makes it optional) → L1 |
| Agile metrics: velocity, burndown, CFD, lead/cycle time | ✔ velocity chart (documented mechanics) | ✔ CFD, lead/cycle time, sprint burndown | ✔ velocity-based capacity, cycle graphs | ✔ reports module | ✔ burndown | Common → L1 |
| Epics / portfolio layers above stories | ✔ epics | ✔ features/epics/portfolio backlogs | ✔ projects/initiatives (different names) | ✔ epics | ✔ epics | Common → L1 |
| Releases/versions as delivery containers | ✔ versions | ✔ iterations + delivery plans | ✖ (documented: cycles not tied to releases; no version module) | ✔ release module | ✖ (not featured) | Common but not universal → L1 |
| Subtask/taskboard decomposition | ✔ subtasks | ✔ taskboard, task checklists | ✔ sub-issues | ✔ (in-sprint items) | ✔ sprint task board per story | Common → L1 |
| Cross-team planning surface | ✔ plans/program boards | ✔ Delivery Plans | ✔ initiatives | ✖ (observed) | ✖ | Common at scale → L1/L2 |
| WIP limits, swimlanes | ✔ | ✔ (documented kanban terms) | partial (board views; not prominent) | ✖ (observed) | ✔ | Common → L1 |
| Ceremony support (standup/retro tools) | ✔ standup | partial (dashboards) | ✖ | ✔ meetings module | ✖ (describes stand-ups conceptually) | Optional → L2 |
| Time tracking / timesheets | ✔ log time | partial (effort fields) | ✖ | ✔ timesheet module | ✖ (observed) | Optional → L2 |
| Dev-tool integration (git status automation) | ✔ | ✔ (GitHub linking, PRs, deployments) | ✔ | ✔ | ✔ | Common → L1 |
| Deep workflow configurability (custom states/transitions) | ✔ | ✔ (process customization) | constrained (fixed categories) | ✔ (release stages; board config) | ✔ (stages customization) | Common → L1; degree is L2/L3 |

Historical / market-sample check: the defining structure above (backlog + work item + board + team + cadence with completion gate) does not depend on any modern implementation pattern. XP/Scrum-era tools of the early 2000s (story cards + iteration planning + velocity) and kanban-only tools (no sprints) both satisfy it; today's extras (roadmaps, AI assistance, cross-team program planning, SLAs, timesheets) are all absent from the older/regional sample and therefore stay out of the defining core. Estimation is deliberately kept out of the core because kanban-flow teams routinely track by count or not at all (Linear makes estimates optional; Jira offers count as a tracking method).

## L0 — Defining Invariant

A team-scoped, agile delivery work system with:

1. **Ordered backlog of work items** — a shared, continuously re-prioritized list of prospective work held by a team; planning means ordering and refining this list, not building a fixed schedule.
2. **Work item** — the unit of planned work (story/issue/task vocabulary varies) with an owner and a status; it moves through a defined workflow toward an explicit completion state ("done"), not a percent-complete of a plan.
3. **Board** — the visual surface where work items appear as cards in workflow columns and are advanced by the team; the board is a view over the backlog/work items, not a free-form task list.
4. **Bounded delivery cadence** — work is scheduled and completed in repeated bounded units: timeboxed iterations (sprints/cycles) with plan→execute→close→carry-over, or continuous pull flow; the team re-plans from the backlog at each boundary.
5. **Team ownership** — backlog, board, and cadence belong to a persistent team; progress (throughput/velocity) is attributed to the team, not to a resource schedule.

Remove the backlog → generic board/task tool. Remove the board/workflow → generic list tracker. Remove cadence-as-re-planning → generic issue tracker. Remove team scoping → personal task management. Remove all and the Type ceases to exist.

## L1 — Common Mature Structure

- Lightweight estimation (story points, t-shirt, count, hours) used for capacity and forecasting; method varies, optional in kanban posture.
- Agile feedback metrics derived from board state + estimates: velocity, sprint burndown/burnup, cumulative flow, lead/cycle time, control charts.
- Hierarchy above stories: epics/features (sometimes initiatives/portfolio backlogs) grouping backlog items.
- Release/version containers associating work items into deliveries.
- Story decomposition: subtasks and sprint taskboards/checklists.
- Cross-team planning views (delivery plans, program boards, initiatives) with rollups and dependency tracking.
- Kanban practices: WIP limits, swimlanes, split/pull columns, definition of done per column.
- Saved queries/filters/views, dashboards, notifications.
- Dev-tool integration: linking commits/PRs/branches to work items; status automation.
- Role model: admin/configurer, planner/product-owner-like role, team members, read-mostly stakeholders.
- Workflow customization (columns/states/transitions) per team.

## L2 — Variant / Optional Structure

- Ceremony support modules (standup summaries, retro boards, meeting modules).
- Time tracking/timesheets (including billable hours and approval).
- Roadmap/timeline surfaces above cadence (Gantt-like planning over epics/releases).
- Scaled-agile overlays (programs, SAFe-style rollups, dependency maps across many teams).
- Intake machinery (triage inboxes, SLAs, forms; support-tool integration).
- Deployment/hosting: multi-tenant SaaS vs self-hosted OSS; per-product AI assistance.
- Project/product-management containers with milestones and status updates (when the tool drifts toward product/work management).
- Process templates / vocabulary regimes (Agile vs Scrum vs CMMI style type sets).

## L3 — Vendor-specific Structure (Research Notes only)

- Jira: JQL query language; parallel sprints; company-managed vs team-managed spaces; space templates; components; Rovo/Coding Agents; smart commits; board-filter-driven boards.
- Azure Boards: area/iteration path model; process templates (Agile/Scrum/CMMI/Basic) and inheritance customization; state categories; stakeholder access level; Analytics/Power BI; MCP-server AI assistance; 60 MB/100-attachment work item limits.
- Linear: cycles cooldowns and automatic rollover; triage responsibility/on-call; SLAs; the Linear Method; initiative/project updates posting to Slack; sub-teams cycle inheritance.
- Zoho Sprints: meetings module; timesheet approval; Zoho ecosystem (Projects/Desk/Flow/Analytics) integration; OKR usage testimonials.
- Taiga: per-project Scrum↔Kanban switch; Taiga Seed estimation tool; "project doom-line"; team health "Iocane" function; themes; MPL-2 licensing.

## Boundary Findings

- **vs Project Management Application (sibling, 03.07)**: general PM centers on a pre-defined plan — task dependencies, milestones, Gantt schedules, baselines vs actual, resource leveling; progress is percent-complete against the plan. Agile PM centers on an ordered backlog re-planned at each cadence boundary; schedules appear only as optional overlays (timelines/roadmaps are L2 in every sampled agile product). Test: delete the backlog/cadence/flow machinery and keep the schedule → Project Management; add a WBS/baseline to an agile tool and it is drifting toward the other Type. Adjacent, distinct Types — but both are sometimes marketed under one banner, and some products (Jira, Azure Boards) span both with separate feature families.
- **vs Kanban Task Board (sibling, 03.06)**: a kanban task board is a visual flow surface for tasks; it lacks the ordered product backlog, team delivery cadence, estimation/velocity machinery, and release containers. The board is one surface of the agile PM application, never the whole. Test: a tool that is only the board is the other Type. Overlap risk: generic board tools marketed as "agile" — the presence of backlog + cadence + metrics is the discriminator.
- **vs Issue Tracker / Bug Tracking System (§12)**: issue trackers center the defect/request lifecycle (report → triage → fix → verify). In agile PM apps, bugs are one input class into the backlog. Taiga demonstrates the boundary inside one product by shipping a separate Issues module with an explicit "promote issue to user story" action; Linear's Triage exists to gate incoming reports into the backlog. Jira spans both markets, which blurs the line commercially but not structurally.
- **vs Task Management Application (03.06)**: task management is individual/small-team to-do oriented without delivery cadence, estimation, or velocity; agile PM is team delivery oriented. Personal-ish views in agile tools (my-items views) are secondary.
- **vs Work Management Platform / Product Management Platform (03.07 / §12)**: work management platforms target generic organizational work (no cadence/backlog semantics required); product management platforms center on upstream discovery/roadmap/customer problems. Linear's Projects/Initiatives and Jira's plans show agile tools growing in that direction — an adjacency to watch, not a merge.
- **vs Engineering Project Management Platform (§12 sibling)**: heavy overlap; the researched products are routinely used as both. This leaf is retained as the cadence/backlog-centric Type; Engineering Project Management should be reviewed with this boundary in mind (joint-review flag below).
- **Timebox vs flow is not a Type boundary**: scrum-posture and kanban-posture products implement the same L0 with different cadence mechanisms; Taiga exposes a per-project switch, Jira ships both board types, Azure documents kanban boards "independent of any sprint", Linear makes cycles optional. Cadence posture is a Variant, not a separate Type.

## Uncertainties

- Pivotal Tracker could not be verified (source unreachable); the opinionated-iteration lineage is inferred from the four verified products and is not load-bearing for the L0.
- Zoho Sprints' operational mechanics (sprint field defaults, board rules) rest on product-site descriptions only; no precise claims are made.
- Exact report definitions (e.g., how each product computes velocity) differ; only Jira's velocity mechanics were documented in detail, and they are kept in Research Notes rather than the canonical document.
- Whether the market treats "Agile Project Management Application" as separate from "Engineering Project Management Platform" is a taxonomy question the market itself answers inconsistently — flagged below.

## Final Synthesis

The Agile Project Management Application is defined by a small core: a **team-owned ordered backlog of work items**, a **board** that tracks each item through workflow states to an explicit **done**, and a **bounded delivery cadence** (timeboxed iteration or continuous pull) under whose boundaries the team re-plans from the backlog. Everything else the market expects — estimation, velocity/burndown/CFD metrics, epics, releases, subtasks, WIP limits, dev integrations, cross-team plans — is mature added structure, and ceremony support, time tracking, scaling overlays, and hosting choices are variants. The Type sits between general project management (plan/schedule-centric — a different planning philosophy) and issue/task tracking (no cadence/team delivery semantics), and it absorbs kanban and scrum as two postures of one structure rather than two Types.
