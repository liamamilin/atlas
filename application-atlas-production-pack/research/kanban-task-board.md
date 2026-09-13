# Research Notes — Kanban Task Board

## Research Goal

Understand the Kanban Task Board as an Application Type: what structure makes a product recognizable as one, what the typical working loop is, and where the boundary runs against the neighboring task-handling Types (To-do List Application, Task Management Application, Agile Project Management Application, Project Management Application), as well as look-alike Types (Digital Whiteboard, Issue Tracker, Sales Pipeline Management).

Evidence layers used below: **A** = directly observed on a fetched official page of a specific product; **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison + Type-boundary reasoning.

## Initial Boundary

Hypothesis before research:

- Core use: visualize and steer a flow of work — work is represented as cards on a board with ordered columns; moving a card across columns expresses its progress.
- Primary users: individuals (personal kanban) and teams (shared process boards); managers/stakeholders read the board.
- Nearest neighbors: To-do List Application (list + checkbox), Task Management Application (task records with status fields, list views), Agile Project Management Application (backlog + cadence + metrics — the board is one surface there), Project Management Application (schedule/plan-centric).
- Likely confusion traps: (1) "kanban view" inside task-management products vs a board-first product; (2) "kanban" as agile methodology vs the board as a software surface; (3) boards marketed as "project management".
- Unknowns: is progressive stage semantics definitional, or is the deeper invariant "position-as-state"? Are WIP limits/swimlanes definitional or method rituals? Where exactly does the Agile PM boundary sit (pre-flagged for joint review)?

## Research Questions

1. What objects exist in the product's world (board, column/list, card, swimlane, archive) and how do they relate?
2. What is the primary interaction loop (create → move → complete/archive)? What does dragging a card actually mean?
3. Which capabilities are definitional vs common vs optional: WIP limits, swimlanes, sub-columns, card attributes, automation, analytics, multiple views, templates?
4. Is the board the system of record for work state, or one view over a task list? (the discriminator vs task management)
5. Do personal/single-user boards and team boards share the same core?
6. Where are the boundaries to To-do List, Task Management, Agile PM, Project Management, Whiteboard, Issue Tracker?
7. Would older / non-modern realizations (physical card walls, open-source Trello-class tools) satisfy the same defining structure?

## Representative Products

| Product | Position in market | Philosophy / tier | Evidence level reached |
|---|---|---|---|
| Trello (Atlassian) | The market archetype; free personal tier → enterprise | General-purpose board-first; "any workflow" | Tier 1–2 (tour, guide chapters 1; official guide hub) |
| Kanban Tool | SMB/team pure-play; kanban-methodology flavored | Methodology-flavored board tool with time tracking & analytics | Tier 1–2 (product feature page; kanban-guide board article) |
| Businessmap (formerly Kanbanize) | Enterprise lean/PPM platform | Boards inside portfolio/OKR/value-stream suite | Tier 2 (root + kanban-boards feature page; KB not fetched) |
| Wekan | Open-source self-hosted Trello-class | Community, self-hosting pole | Tier 2 (official GitHub README; features wiki not fetched) |

Selection rationale: archetype + methodology-first pure-play + enterprise suite pole + open-source/self-host pole; spans personal (Trello free, Wekan, Kanban Tool personal example) to enterprise (Businessmap). Different product philosophies (general-purpose vs lean-methodology vs platform-module vs FLOSS).

## Sources

All fetched 2026-09-08 (Layer A unless noted):

- Trello — product tour: https://trello.com/tour
- Trello — guide hub: https://trello.com/guide
- Trello — "Learn Trello board basics" (guide ch. 1): https://trello.com/guide/trello-101
- Kanban Tool — homepage: https://kanbantool.com/
- Kanban Tool — product/functionality page: https://kanbantool.com/product
- Kanban Tool — "What is a Kanban Board?" (kanban guide): https://kanbantool.com/kanban-guide/kanban-board
- Businessmap — root: https://businessmap.io/
- Businessmap — "Kanban Boards" feature page incl. FAQ: https://businessmap.io/kanban-boards
- Wekan — official GitHub README ("Open Source kanban"): https://github.com/wekan/wekan (README-level; features wiki page not fetched)

Not reached this pass (recorded as limitations): Trello Atlassian support articles (support.atlassian.com not fetched — the trello.com guide chapters served as the operational layer), Businessmap knowledge base (knowledgebase.businessmap.io), Wekan features wiki. Assertion strength is calibrated accordingly.

## Product Observations

### Trello (Layer A)

- Official definitions (guide ch. 1): a **board** is "a place to keep track of information — often for large projects, teams, or workflows"; **lists** keep **cards** "organized in their various stages of progress"; lists "can be used to create a workflow where cards are moved across each step in the process from start to finish, **or simply act as a place to keep track of ideas and information**"; a **card** is "the smallest, but most detailed unit of a board", used to "represent tasks and ideas"; "drag and drop cards across lists to show progress".
- Board menu: manages members' board permissions, settings, card search, Power-Ups, automations, activity feed.
- Card features (tour): due dates with reminders, attachments (drag & drop), checklists with progress status, AI text assistance; "mark to-do's as 'Done'".
- Platform surfaces: Power-Ups (plugins), automation ("create a foolproof process for moving work forward... rules for almost any action"), templates gallery, different views activated in premium tiers, custom fields, integrations, MCP server for AI tools.
- Positioning: free plan "for individuals or small teams"; teams pages (marketing, product, engineering, design, startups, remote); use cases include task management, project management, resource hubs.
- Observation: Trello's own documentation treats the board as the primary object with no separate task-status field — list membership carries the organization/progress. Also notable: the same board grammar is explicitly offered for non-workflow uses (ideas/information tracking) — evidence that strict stage semantics is looser than "position-as-state".

### Kanban Tool (Layer A)

- Definition (kanban guide): "A Kanban Board is a visual signboard, showing the work to be done, the work in progress, and the work completed. It's a visual representation of a person's, team's, or department's value stream, that has been mapped out on a whiteboard, a wall, or in dedicated Kanban software."
- Origin framing: method from Toyota manufacturing; goals "visualize work, limit work in progress, optimize flow"; "the board belongs to the team: it is foremost not a project management tool, but a tool for the team and their stakeholders"; boards "typically divided into rows and columns with work items represented by colorful cards... as they move from start to finish through the process".
- Practice guidance: sequential steps; card priority top-to-bottom within a row; WIP limits per stage ("helps the team decide how many items to take on... ensures that the started items are finished before more work is pulled"); pull discipline ("pulling new items for themselves only after they've completed work"); middle steps "often divided into sub-columns" (in-progress/done split); single-user personal board worked through a worked example; physical vs digital boards both valid.
- Product functionality page: kanban boards "resembling a clean whiteboard"; customizable board templates (basic, time driven, event driven, product development, sales pipeline); flexible workflow editor with **swimlanes**; drag & drop; **WIP limits**; collapsible columns/swimlanes; task transfer/copy between boards; tasks archive + archive search; board search and filters; in-column card sorting.
- Card: description, external id/links, card type, task difficulty, assignment with email notifications, tags, estimated time; up to 15 custom fields; due dates, start dates, priorities; file attachments; comments; sortable to-do lists with sub-levels; full card history per card; 22 card colors; per-card direct links.
- Power-ups: card blocking, card aging, recurring tasks, postponed tasks, task dependencies, time in stage, cycle time, calendar widget, checklist templates, card covers, work timer, etc.
- Analytics: cumulative flow diagram, lead vs cycle time diagram, time reports, seamless time tracking (timer follows workflow start/pause), breakdown charts, export CSV/Excel.
- Roles: account owner, account administrator, project manager, regular user; board access full/custom/read-only.
- Deployment: cloud SaaS + On-Site self-hosting SKU; mobile apps; API; integrations (Zapier, calendars, Jira via extension); process automation; AI assistant that builds boards and suggests checklist items.

### Businessmap (Layer A, product-page level)

- Positioning: enterprise work/PPM platform ("Deliver outcomes, not just tasks"); **Kanban Boards** is one named module among Portfolio Workspaces, OKRs/Outcomes, Value Stream Manager, Collaboration Canvases, Form Builder, Project & Capacity Planning.
- Board features (feature page + FAQ): "A Kanban board puts every task in view as a simple card, so anyone on the team can see what's being worked on, what's done, and what's coming up next"; "Shape the board around your process... Split your boards into sections for different types of work, break stages down into more detail, or combine areas where the same people handle everything"; swimlanes "split a board horizontally to separate different types of work or classes of service"; **sub-columns** "break any workflow stage into multiple smaller steps"; board networks ("connect workflows across the organization... manage cross-team dependencies"); card templates with predefined fields/subtasks; AI agents executing work items on the board with full execution audit; automation policies (nav).
- Suite context: forecasting "use historical data and AI to forecast work delivery"; boards feed dashboards/outcomes at management level; industry solutions (engineering, pharma, banking).
- Observation: even at enterprise scale with portfolio layers above, the board remains a flow surface of cards in stages — the surrounding portfolio machinery is separate structure, not part of the board's model.

### Wekan (Layer A, README-level)

- "Completely Open Source and Free software collaborative kanban board application with MIT license"; "real-time user interface".
- Use framing: "Whether you're maintaining a personal todo list, planning your holidays with some friends, or working in a team on your next revolutionary idea, Kanban boards are an unbeatable tool... They give you a **visual overview of the current state of your project**".
- Self-hosting: install on own computer/server; Docker/Snap packages; large deployments claimed (one 30k-user company claim — vendor claim, not verified).
- Trello-class board grammar (open-source Trello lineage); card-level feature detail not enumerated in the fetched README (recorded as evidence limitation).
- Observation: the open-source/self-hosted pole carries the same core structure — board as visual overview of current state, cards as work units — without cloud, AI, or analytics.

## Cross-product Comparison

| Structure / capability | Trello | Kanban Tool | Businessmap | Wekan | Strength |
|---|---|---|---|---|---|
| Board = ordered columns holding work as cards | ✔ lists | ✔ columns | ✔ | ✔ | B — universal in sample |
| Card = unit of work with own details | ✔ | ✔ | ✔ | ✔ (detail unenumerated) | B |
| Moving card between columns = progress/state change | ✔ "show progress" | ✔ drag & drop + stage mechanics | ✔ "what's being worked on, what's done" | ✔ | B — universal |
| Done/terminal handling (done column, mark complete, archive) | ✔ done list, "mark as done" | ✔ tasks archive + archive search | ✔ implied ("what's done") | ✔ implied | B |
| Board as the native model (position is the status record) | ✔ (no separate status field) | ✔ workflow editor defines stages | ✔ | ✔ | B |
| Column customization (rename/add/reorder; shape to process) | ✔ lists "arranged and titled however you'd like" | ✔ flexible workflow editor | ✔ explicit ("shape the board around your process") | ✔ | B |
| WIP limits | ✖ (not in fetched docs) | ✔ direct | (method-consistent; not directly observed) | ? | common, method-standard (Kanban Tool direct; guide says boards "should incorporate WIP limits") |
| Swimlanes (horizontal rows) | ✖ (not native) | ✔ | ✔ | ? | common |
| Sub-columns (stage splits) | ✖ | ✔ (method guidance) | ✔ direct | ? | common |
| Card attributes (assignee, due date, labels/colors, attachments, checklists, comments, history) | ✔ | ✔ (extensive) | ✔ (card templates, comments, subtasks) | ? (not enumerated) | B — common mature structure |
| Real-time multi-user collaboration | ✔ | ✔ | ✔ | ✔ | B |
| Board members / permissions / roles | ✔ menu permissions | ✔ roles + per-board access | ✔ (workspaces; enterprise tier) | ✔ (collaborative; detail not enumerated) | B |
| Automation of moves/actions | ✔ | ✔ | ✔ (automation policies) | ? | B — common |
| Search/filter across board + archive | ✔ | ✔ | ✔ | ✔ | B |
| Board templates & cloning | ✔ gallery | ✔ + cloning | ✔ card templates | ? | B — common |
| Flow analytics (CFD, cycle/lead time, forecasting) | ✖ (not in fetched docs) | ✔ | ✔ (AI forecasting) | ✖ | segment-dependent → variant |
| Time tracking | ✖ | ✔ signature | ✖ (not observed) | ✖ | product-specific |
| Multiple secondary views (calendar/timeline/table) | ✔ (premium views) | ~ (calendar widget) | ✔ (gantt/timeline surfaces) | ? | variant |
| Cross-board linking / board networks | ✖ (not observed) | ~ (task transfer between boards) | ✔ direct | ? | enterprise variant |
| AI assistance | ✔ (card text) | ✔ (board builder) | ✔ (agent orchestration) | ✖ | current-generation layer |
| Deployment flexibility (self-host/open-source) | ✖ (cloud) | ✔ On-Site SKU | ✖ (cloud) | ✔ FLOSS | variant |
| Personal/single-user board use | ✔ free personal plan | ✔ worked single-user example | ✖ (enterprise) | ✔ personal todo framing | B — variant axis, not structure |

Historical / market-sample check: the defining structure (board + card + position-as-state) does not depend on any modern implementation pattern. The Kanban Tool guide itself documents the physical antecedent — the value stream "mapped out on a whiteboard, a wall, or in dedicated Kanban software", originating in Toyota manufacturing's card signals — and a physical card wall satisfies all three structures. The open-source Wekan shows the same core without cloud/AI/analytics; Trello's earliest form and today's product differ only in added structure. Therefore nothing modern (WIP limits, swimlanes, analytics, automation, AI, cloud sync) belongs in the defining core. Check passed.

## Canonical Model

### Level 0 — Defining Invariant (deliberately small)

Three jointly-held structures. Removing any one stops the product from being recognizable as a Kanban Task Board:

1. **The board** — the organizing surface: a work area divided into ordered vertical columns, each a named container (stage/list) of work. The board is the primary working model of the product, not a rendering over some other record. (Remove → a task list / note collection.)
2. **The card** — the unit of work: a self-contained, movable work item carrying its own details (title at minimum; typically description, owner, dates, labels, attachments, discussion). (Remove → a whiteboard of sticky scribbles with no work objects, or a calendar of slots.)
3. **Position-as-state** — a card's column membership is how the product records and communicates where that work stands; movement between columns is the primary state-changing operation, and the column sequence expresses progression from not-started toward done, with order within a column expressing sequence/priority. The product needs no separate status field for this; the position is the status. (Remove → a task record with a status dropdown — a different Type's grammar.)

Note on the fourth candidate "progressive workflow semantics": rejected for L0. Trello's own documentation explicitly allows lists to be used "to create a workflow... or simply act as a place to keep track of ideas and information" — the market accepts category-columns and information-hub boards as legitimate uses of the same product. The load-bearing invariant is that *position carries the state*, not that every board models a strict multi-stage process. The done/terminal end is part of the progression meaning but boards in the wild may lack an explicit done column; products still expose completion/archive machinery. Kept inside structure 3 as "progression toward done is the organizing meaning", not as a mandatory column.

Note on the fifth candidate "shared/collaborative": rejected for L0 — personal single-user boards are a documented, marketed use of every sampled general-purpose product (personal kanban). Sharing is the common deployment, not the definition.

### Level 1 — Common Mature Structure

Present across the sample (or in most of it) without defining the Type:

- card attributes: description, assignee/member, due date, labels/colors, attachments, checklists/subtasks, comments, per-card history
- real-time multi-user updates on a shared board
- board member/permission model (who can see/edit a board; roles)
- column & workflow customization (rename/add/reorder columns; sub-columns; collapse)
- swimlanes (horizontal rows for work types / classes of service)
- WIP limits per column (method-standard; strong in methodology-first products, absent natively in the archetype's fetched docs)
- card search, filters, labels
- board templates and cloning
- automation of repetitive moves/actions
- archive of completed cards with archive search
- notifications (assignments, comments — typically via email)
- API, integrations, mobile clients
- boards home / switcher (many boards per user/team)

### Level 2 — Variant / Optional Structure

- flow analytics: cumulative flow diagram, cycle/lead time, forecasting (methodology-first and enterprise segment)
- time tracking (one sampled product's differentiator)
- secondary views: calendar, timeline/Gantt, table, dashboard
- card dependencies, blocking, aging, classes of service, card templates, recurring tasks
- custom fields
- cross-board linking / board networks; portfolio layers above boards (PPM posture)
- personal kanban vs team deployment (audience axis)
- deployment: cloud SaaS vs on-premises/self-hosted vs open source
- AI assistance (current-generation layer: text help, board builders, agent execution)
- non-workflow board uses (idea boards, information/resource hubs) — same surface, degenerate flow

### Level 3 — Vendor-specific Structure

- Trello: Power-Ups extension ecosystem; Butler automation branding; Inbox/Planner surfaces; MCP server; "card back" terminology; free/standard/premium/enterprise plan gating of views and features
- Kanban Tool: On-Site self-hosting SKU; developer-tools power-up scripts (Swimlane Auto-Assign, Cycle time, etc.); Kanbanira Jira extension; "22 card colors" specifics; uptime claims
- Businessmap: Portfolio Workspaces / OKR-Outcomes / Value Stream Manager / Collaboration Canvas / Form Builder modules; AI-agent orchestration arena; Flight Levels whitepaper positioning; industry solution packs
- Wekan: Meteor-based implementation; Sandstorm/Snap/Docker packaging; 234-language translation program; Standard for Public Code assessment; 30k-user deployment claim

## Vendor-specific Findings

- Trello's guide explicitly generalizes the board beyond workflow (ideas/information lists) — supports keeping strict stage semantics out of the definition.
- Kanban Tool's guide is the sample's clearest statement of method practice (WIP limits, pull, top-to-bottom priority, sub-columns) and of the "board belongs to the team, not a project management tool" positioning.
- Businessmap demonstrates the enterprise packaging: the board as one module inside a strategy-execution suite, with board networks and AI-agent execution — evidence that scale layers are optional, not structural.
- Wekan shows the minimal FLOSS form: the core with none of the commercial accretions.

## Boundary Findings

- **vs To-do List Application**: a to-do app's world is a list with checkable items (completion is a boolean act, reminders first-class); no board grammar. Remove board + position-as-state from a Kanban Task Board and keep the flat checklist → to-do app. Conversely, a to-do app that *adds* board columns is drifting toward this Type only if the board becomes the primary model.
- **vs Task Management Application**: sharpest seam. Task management centers on the task *record* (status field, priority, assignee, lists/calendars as primary views; the kanban board, when present, is a projection view over records). Here the board is the native model — the card's position is the state of record. Center-of-gravity test: if the board is one view among many over a task table, it's task management; if the board is where the work state lives, it's this Type. Trello markets "task management" as a use case — commercial overlap is real, structural identity is not.
- **vs Agile Project Management Application** (pre-flagged sibling; discharged from this side — see STATUS): the agile PM Type's defining core is a team-owned ordered backlog of work items + a bounded delivery cadence (timeboxed iteration or continuous pull) as the re-planning boundary + feedback metrics. The board is one surface of that Type, never the whole. A Kanban Task Board has no ordered product backlog, no iteration/cadence machinery, no velocity/burndown as defining structure. Test: a tool that is *only* the board is this Type; add backlog+sprints+metrics machinery and it becomes the other Type. Businessmap straddles commercially by shipping boards inside a PPM/agile suite, but its boards remain flow surfaces while the portfolio/planning machinery lives in separate modules — packaging overlap, not Type merger. Joint-review flag DISCHARGED with keep-both ratified.
- **vs Project Management Application**: plan/schedule-centric (tasks with dates, dependencies, resources, Gantt; percent-complete planning philosophy). A board may be one view of a PM tool; schedule machinery is not part of this Type's core.
- **vs Digital Whiteboard**: freeform spatial canvas; no card-state model (stickies have no stage membership or movement semantics). Kanban templates/widget boards on whiteboards are optional task machinery (that pass's L2), not this Type. Remove position-as-state and allow free arrangement → whiteboard.
- **vs Issue Tracker / Bug Tracking System**: issue record + workflow schema + reporting primary; boards are a common view. The workflow there is usually admin-defined per issue type with required transitions; here the board geometry is user-shaped and the state lives in position.
- **vs Sales Pipeline Management** (cross-domain): identical board grammar (cards in stage columns, drag to advance) over a different world model (deals, buyers, values, win/loss). Board-grammar sharing is implementation, not Type identity — consistent with that pass's "remove → personal kanban of cards" formulation.
- **vs Work Management Platform / Team Workspace / PPM suites**: broad containers that include boards as one module. Packaging embedding does not change the board's Type.

"Remove what → becomes another Type" summary: remove board/position-as-state → task list or task management; add backlog+cadence+feedback metrics → agile PM; add schedule/dependency planning → project management; freeform spatial arrangement without state → whiteboard; keep grammar, swap the world model to deals → sales pipeline.

## Uncertainties

- Wekan card-level feature detail rests on README-level evidence (features wiki not fetched); its core structure is confirmed, its exact card field set is not asserted.
- Businessmap operational mechanics were observed at product-page level; its knowledge base (Zendesk-hosted) was not fetched, so board-configuration specifics (WIP limit mechanics, card template scope) are asserted at capability level only.
- Trello support articles were not fetched; operational specifics (power-up limits, plan gating details) are deliberately not stated.
- Whether "order within column = priority" is honored as data in all products is only directly documented by Kanban Tool's guide; treated as common practice guidance, not a structural rule.
- WIP limits: directly observed in one product; the method literature (as republished by the same vendor) frames them as standard practice; classified common-method, not definitional — a sampled-product gap remains possible for some regional products.

## Final Synthesis

A Kanban Task Board is defined by a small core: a **board** (the primary working surface, divided into ordered columns), **cards** (self-contained units of work), and **position-as-state** (a card's column membership is the record of where the work stands; moving the card is the state change; column order expresses progression toward done, card order expresses sequence). The board is the model of record, not a view over task records. Everything the market associates with the category — card attributes, real-time collaboration, permissions, WIP limits, swimlanes, sub-columns, templates, automation, archives, search, mobile/API — is mature added structure; flow analytics, time tracking, secondary views, board networks, AI, and deployment choices are variant or optional; personal vs team is an audience axis, not a structural one. The Type sits between list-centric task handling (different record grammar), agile delivery management (adds backlog + cadence + metrics around the board), and freeform visual surfaces (no state-in-position). A physical whiteboard with sticky notes satisfies the defining core — the software is the persistence, sharing and scaling of that grammar, not the grammar itself.
