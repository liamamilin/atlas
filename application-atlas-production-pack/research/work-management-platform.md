# Research Notes — Work Management Platform

Directory leaf: "Work Management Platform" (§03.07 Project & Work Management)
Slug: work-management-platform
Research date: 2026-09-09
Methodology: v1.1

## Research Goal

Understand the Work Management Platform as an Application Type: what objects exist inside it (work items, boards/lists/projects/sheets, workflows, automations, forms, dashboards, portfolios), how a team's whole operational work is held and moved, which capabilities are definitional vs common vs variant, and where the boundary sits against the many neighboring Types that share its vocabulary (Project Management Application, Task Management Application, Project Portfolio Management, Workflow Management Platform, Collaborative Workspace, Team Workspace Platform, Collaborative Spreadsheet / Structured Table, Kanban Task Board, Business Management Suite, Professional Services Automation).

## Initial Boundary

- Hypothesis: "work management" is the market's own category label (Asana, monday.com, Smartsheet, Wrike, ClickUp all self-label variants of it; Gartner's Collaborative Work Management category). The Type is distinct from Project Management: it holds a team's whole ongoing operational work, where the project is one container among several.
- Counterparty flags to discharge at this pass (from processed siblings):
  - project-management-application (2026-09-08): "PM applications organize bounded scheduled undertakings; work management platforms organize a team's whole ongoing work (requests, processes, approvals, non-project recurring work) where the project is one container among several. The market blurs hard (Smartsheet and Asana are marketed in both vocabularies). Products above the seam should be attributed by center of gravity, not feature lists. Joint review recommended at that pass."
  - project-portfolio-management-application (2026-09-08): "Work-management centers a team's whole ongoing operational work (requests, processes, approvals) where projects are one container; PPM centers the governed investment collection above projects." Also carried flags to reconcile: task-management / to-do-list and professional-services-automation.
  - task-management-application (2026-09-09): "Work management centers a team's whole ongoing operational work (requests, processes, approvals); task management centers discrete completable tasks for people. Asana documents the overlap zone (one product family marketing both). Removal test: remove forms/requests/approval/process machinery → task management remains."
  - workflow-management-platform (§10, 2026-09-08): "work/project management centers on projects, plans, and schedules as objects; workflow management centers on instances of configured recurring patterns. Check this seam when work-management-platform is processed."
  - collaborative-spreadsheet / spreadsheet-application / structured-table passes: Smartsheet documented as the grid-as-work-management drift pole ("when rows become scheduled, dependent work items and the grid becomes the surface, the product has moved to Work Management").
  - collaborative-workspace / team-workspace-platform passes: work management's primary objects are tasks/projects/workflows with status machinery; in a workspace, tasks are one content type.
  - business-management-suite pass: work-centered products lack the customer+money spine.

## Research Questions

1. What is the container hierarchy (account/workspace → space/folder → board/list/project/sheet) and what lives at each level?
2. What is the work record (item/task/row) and what typed attributes does it carry?
3. How does work move: status workflows, automations/rules, approvals, intake forms?
4. What sits above the container: dashboards, reports, portfolios, goals, My Work, workload?
5. Which of these are definitional vs common vs variant?
6. Where exactly are the seams vs PM, Task Management, PPM, Workflow Management Platform, Workspace Types, Spreadsheet Types?
7. Historical check: would the early-web generation (2004–2010) and platform-native products still fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Self-labeling / philosophy | Customer tier | Evidence tier |
|---|---|---|---|
| Asana | "work management platform"; coined the category vocabulary; list-native | mid-market → enterprise | Tier 2 (features pages; help center JS-blocked ×2) |
| monday work management | "Work OS"; board-native, visual, automation-first | SMB → enterprise | Tier 1 (support center articles fetched) |
| Smartsheet | grid/spreadsheet-native work management; enterprise solutions | enterprise | Tier 1 (help center articles fetched) |
| Wrike | "collaborative work management" veteran; folder/project-native | mid-market → enterprise | Tier 1 (help center articles fetched) |
| ClickUp | "everything app for work" maximalist; hierarchy-native | SMB → enterprise | Tier 1 (help center articles fetched) |

Avoided: Jira (engineering-PM Type, processed separately), Trello (Kanban Task Board), Notion (Collaborative Workspace), Airtable (Structured Table), Basecamp (PM lightweight pole, used by the PM pass).

## Sources

Tier 1 (fetched 2026-09-09):

- monday.com Support Center — https://support.monday.com/hc/en-us — structural hierarchy article (workspaces/folders/boards/groups/items/columns/subitems/dashboards/workdocs), automations article (trigger/condition/action, cross-board), WorkForms article (submissions → items)
- Smartsheet Help Center — https://help.smartsheet.com/ — "Create and organize Smartsheet items" (item types: grid/Gantt/board/form/report/dashboard/timeline), sheets-and-rows category, automated-workflows category (trigger/condition/action blocks, approval requests, update requests, move/copy rows, document generation)
- Wrike Help Center — https://help.wrike.com/hc/en-us — "Projects in Wrike", "Level Up Your Work" category (Automation, Blueprints & Templates, Proofing & Approvals, Request Forms, Custom Statuses and Workflows, Custom Fields, Custom Item Types, Access Roles), "Request Forms in Wrike" (submit → create task/project/custom item → populate → locate → assign → start approval)
- ClickUp Help Center — https://help.clickup.com/hc/en-us — "Intro to the Hierarchy" (Workspace → Spaces → Folders → Subfolders → Lists → Tasks → Subtasks; Docs/Dashboards/Forms/Whiteboards as hierarchy items), Get-started category (views: List/Board/Table/Gantt/Calendar/Timeline/Workload/Mind Map/Form; task statuses; roles)

Tier 2 (fetched 2026-09-09):

- Asana — https://asana.com/features — feature families: Tasks/Projects/Project views/Custom fields/Status updates/My tasks/Inbox/Home; Goals/Portfolios/Reporting dashboards; Forms/Rules/Bundles/Templates; Capacity planning/Workload/Time tracking; Admin console/Permissions

Source-access limitation: Asana's help center (help.asana.com, asana.com/guide) is a JS application that returned a CSS error on two fetch attempts; per the network-restricted rule the source was abandoned after 2 failures and Asana evidence was downgraded to Tier-2 product-page strength. No precise Asana operational details (numeric limits, plan gating specifics) are claimed from memory.

## Product A — monday work management

### Key observations (Tier 1, evidence layer A)

- Structural hierarchy (help center, "Understanding monday.com's structural hierarchy"): Account → **Workspaces** ("every board, dashboard, or workdoc must be created within a workspace"; open or closed for privacy/transparency) → **Folders** → **Sub-folders** → **Boards / Dashboards / Workdocs**. Boards are "where the work happens, rather than where the work is housed."
- Board internals: **Groups** (color-coded sections categorizing items — a week, a month, a project step, a client) → **Items** ("an individual row in a group on your board… can represent anything from a list of projects, to weekly tasks, clients, locations or any other aspect of your workflow") → **Columns** ("dozens of columns" — typed: status, people, date, formula, connect-boards, dependency…) → **Subitems**.
- Dashboards: "aggregate data from multiple boards to create visual displays using widgets" (30+ widget types); single-board dashboards attach to a board as board views.
- Workdocs: multimedia docs with elements, embedded boards/items.
- Automations (help center): every automation = **trigger + condition + action(s)**; pre-made templates or "create from scratch"; multi-step actions; **cross-board automations** move/create items across boards; automation center per board with manage/pause/delete; importance labels (explicitly do not affect run order).
- WorkForms (help center): "custom forms to collect information, requests, or feedback, all connected directly to your boards… automatically capture responses as items"; shareable link/embed; "anyone with access to the shareable link… can submit a WorkForm, even without a monday.com account"; multiple forms per board routing submissions to different groups; results/analytics; conditional logic; drafts.
- Product family: monday work management / CRM / dev / service / WorkCanvas (whiteboard) / WorkForms — same engine, vertical packaging. Use-case pages: marketing, PMO, sales, developers, HR, IT, operations, construction.
- Roles & permissions section exists (board permissions, roles); admin console; enterprise tier.

## Product B — Smartsheet

### Key observations (Tier 1, evidence layer A)

- Item model (help center, "Create and organize Smartsheet items"): "In Smartsheet, most solutions begin with a sheet." Item types: **Grid** (clean slate), **Gantt** (standard project columns + Gantt enabled), **Board** (Kanban cards), **Form** ("a basic three-column sheet with a form attached"), **Report** ("real-time data from across multiple sheets in a single view"), **Dashboard** ("visual summary of sheet data or an information hub"), **Timeline**. Items live in **Workspaces**; visibility controlled by sharing; templates and import paths.
- Sheets track "tasks, project deadlines, punch lists, inventories, or customer information, whatever you need" — the row is the work record ("Rows represent individual items or tasks within a sheet").
- Row machinery: contact-list columns assign people; dependencies with predecessors auto-calculate dates; milestones; cell links consolidate/roll up across sheets; auto-number; conditional formatting; sheet summary formulas compute project metrics.
- Automated workflows (category): **trigger blocks** (when/frequency) + **condition blocks** (filter rows) + **action blocks**; four workflow types; actions include: assign people, change cell value, copy rows, move rows (to another sheet), alerts/notifications, **update requests** (collect edits from people not shared into the sheet), **approval requests** ("request multiple approvals and create an order for those"; approvals pause the workflow), reminders, document generation ("generate purchase orders, patient intake forms, contracts"); manual run; per-permission-level rights.
- Premium/enterprise layer: Control Center ("standardize, automate, and scale project and portfolio management"), Resource Management (projects, time/expense), Dynamic View (share info to the right people at the right time), WorkApps ("role-based views" packaging sheets/reports/dashboards), DataMesh/Data Shuttle/DataTable (cross-sheet/system data), Bridge (integration automation), Brandfolder/Content Automation (creative asset workflows), Proofing.
- Self-positioning: "Intelligent Work Management" (ENGAGE keynote framing).

## Product C — Wrike

### Key observations (Tier 1, evidence layer A)

- Structure: **Spaces** (team/department containers; types incl. personal, locked) → **Folders** → **Projects** ("projects help organize and manage related tasks under a larger goal… track the status and due dates separately from your tasks while adding information directly to the project itself: project owner, start date, end dates, custom fields, plus attachments or conversations") → **Tasks/Subtasks**. Projects are a special folder type; subprojects supported; Gantt; project status/progress.
- Navigation surfaces: My To-Do, Created by Me, Shared With Me, Starred; Wrike Views (list/board/table/gantt/calendar/workload-class); filters with AND/OR; workspace search.
- Process machinery ("Level Up Your Work" category):
  - **Custom Statuses and Workflows**: status groups; workflows per space or account-wide; default vs custom.
  - **Automation in Wrike**: rule constructor with triggers/actions; at space and account level.
  - **Request Forms**: "admins create custom intake forms for users or external submitters to send requests… When you submit a request, Wrike automatically: creates a task, a project, a custom item type or a blueprint; populates it with information from the form fields; adds it to a location; assigns the task / adds a project owner; starts an approval process (if specified)." Account-level and space-level forms; external public-link submissions; submission analytics (totals, per-month, last submitted).
  - **Proofing & Approvals**: approvals on tasks/folders/projects; file approvals with versioned review.
  - **Blueprints and Templates**: task/folder/project blueprints as reusable process scaffolds.
  - **Custom Fields** (many types, space/account management), **Custom Item Types** (task-like items with their own automation), **Access Roles** (graded permissions).
- Roles: Collaborators / Contributors / Viewers vs full users — external-participant tiering.
- Time tracking (timelog view, locking); BI export; integrations.

## Product D — ClickUp

### Key observations (Tier 1, evidence layer A)

- Hierarchy (help center, "Intro to the Hierarchy"): **Workspace** ("contains your entire organization and all of your work; one Workspace per organization") → **Spaces** ("arrange your different workflows or types of work… by departments, teams, high-level initiatives, clients"; own settings; shared or private) → **Folders** (optional; house Lists; auto-create a List) → **Subfolders** → **Lists** ("contain tasks that are part of the same project or goal") → **Tasks** ("the actionable parts of your projects… default sections and customizable options") → **Subtasks** (nested layers; used for epics).
- Hierarchy items beside locations: **Docs, Dashboards, Forms, Whiteboards**.
- Views over the same records: List, Board, Table, Gantt, Calendar, Timeline, Workload, Mind Map, Form, Chat, Embed, Map, Activity, Team — "You can create a List view on any level of your Hierarchy" (views are projections, not records).
- Task machinery: custom task statuses ("create custom task statuses to match your workflow… creative asset approvals…"), assignees, priorities, custom fields, dependencies, multiple lists (one task in several lists), templates with date remapping.
- Converged workspace (ClickUp 4.0): "a converged Workspace that connects your tasks, Docs, Chat, and AI tools in one place"; Hubs centralize Docs/Forms/Dashboards/Clips; Chat with channels/DMs; Brain AI; Agents.
- Roles/permissions: owner/admin/member/guest/limited-member ladders; per-location permissions; public sharing links; private items.
- Use-case pages: marketing campaigns, OKRs, content calendars, Gantt planning; explicit comparison vs Notion ("Notion is a document-first workspace… ClickUp…" — the vendor itself draws the workspace/work-management seam).

## Product E — Asana (Tier 2 only)

### Key observations (evidence layer A at feature-existence strength; no operational detail)

- Self-positioning: "the operating system for human-agent teams — the place where humans and agents run an organization's critical workflows together, on the same plan, toward the same goals."
- Feature families (features page): **Tasks** ("break work into bite-size pieces with clear owners and due dates"), **Projects** ("organize tasks and tackle work together in a shared hub"), **Project views** (list/calendar/timeline/Gantt/Kanban), **Custom fields**, **Status updates**, **My tasks**, **Inbox**, **Home**; **Goals** ("connect every team's work to company-wide objectives"), **Portfolios** ("mission control center to monitor connected projects"), **Reporting dashboards**; **Forms** ("standardize work requests so your team has the information they need from the start"), **Rules** ("automate routine tasks"), **Bundles** ("create, apply, and update processes across projects in one place"), **Templates**; **Capacity planning / Workload / Time tracking / Timesheets**; **Admin console / Permissions / Guest management**.
- FAQ confirms: projects hold tasks with assignees/dates/dependencies/custom fields; recurring tasks; personal use supported ("create an Asana project for anything").
- No help-center operational detail claimed (source blocked).

## Cross-product Comparison

| Structure | Asana (T2) | monday (T1) | Smartsheet (T1) | Wrike (T1) | ClickUp (T1) | Layer |
|---|---|---|---|---|---|---|
| Org container hierarchy (workspace → space/folder → work container) | projects in org | workspaces→folders→boards | workspaces→items | spaces→folders→projects | workspace→spaces→folders→lists | B (5/5) |
| Structured work record with typed attributes (status/people/dates/custom fields) | tasks+custom fields | items+columns | rows+columns | tasks+custom fields | tasks+custom fields | B (5/5) |
| Project as one container type among several | projects beside goals/portfolios | boards represent projects/clients/weeks | Gantt sheets beside grids/boards/forms | projects (folder subtype) beside folders | lists inside folders beside standalone lists | B (5/5) |
| Multiple views over the same records | list/board/timeline/Gantt/calendar | board views + widgets | grid/Gantt/board/card/calendar/timeline | list/board/table/Gantt/calendar | list/board/table/Gantt/calendar/timeline/workload | B (5/5) |
| Status workflows (defined states governing movement) | status updates/custom fields (T2) | status columns | dropdown/status columns + approval chains | custom statuses & workflows (named feature) | custom task statuses (named feature) | B (5/5) |
| Rules/automations acting on records | rules (T2) | trigger+condition+action automations, cross-board | trigger/condition/action blocks, move/copy rows | automation rule constructor, space/account level | automations (features; not fetched in detail) | B (5/5) |
| Intake forms creating records | forms (T2) | WorkForms → items, public link | forms → rows (form item type) | request forms → task/project/custom item/blueprint + approval | form view | B (5/5) |
| Approvals gating work | (not confirmed T2) | (via automations; not confirmed) | approval requests with ordered chain | approvals on tasks/folders/projects; file approvals | (approvals via statuses; not confirmed) | A (2/5 direct) — held common, not definitional |
| Cross-container reporting/dashboards | reporting dashboards, portfolios | dashboards aggregate multiple boards | reports + dashboards across sheets | reports, project rollups | dashboards | B (5/5) |
| Personal across-work view | My tasks, Inbox | My Work | left-panel recents/favorites | My To-Do, Created by Me, Shared With Me | My Tasks | B (5/5) |
| Templates/blueprints of recurring work | templates, bundles | templates, managed templates | templates | blueprints & templates | templates | B (5/5) |
| Resource/workload layer | workload, capacity (T2) | (workload widgets) | resource management (premium) | workload views, time tracking | workload view, time tracking | B — variant depth |
| Bundled content/communication surfaces | (docs via integrations) | workdocs | (attachments, proofing) | document editor | docs, chat, whiteboards | B — variant packaging |
| Vertical packaging on same engine | (goals/portfolios as packaging) | CRM/dev/service products | control center, workapps | custom item types, proofing | sprint folders, hubs | L3-leaning variant |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The team's shared work population as the system of record.** Persistent, structured, individually addressable work records (item / task / row) carrying typed attributes — status, assignee, dates, custom fields — held in an organizational container hierarchy (account/workspace → space/folder → board/list/project/sheet). The hierarchy holds the team's whole ongoing operational work; the project is one container type among several, not the unit of record.
   - Remove → a personal task manager (no org hierarchy, no population) or a PM application (project as the unit of record).
2. **Configured process governing how work moves.** The population's movement is held in the system as machinery: defined status workflows (named states with groups), rules/automations that act on record events, approvals that gate transitions, and intake forms that create records from requests — so the team's recurring work patterns run in-system rather than by hand.
   - Remove → a shared task list or collaborative spreadsheet with task rows and no process machinery (the task-management / spreadsheet pole).
3. **The cross-container coordination surface.** The population is worked and read above the single container: personal across-work views (My Work/My Tasks/My To-Do), cross-container dashboards and reports, and commonly portfolio/goal rollups and workload views — the layer that lets a team or organization see and steer all of its work.
   - Remove → a container-scoped tracker (single board/list/project tool).

Jointly-held load-bearing:
- 1 alone = shared task list / collaborative spreadsheet with task-shaped rows
- 2 without 1 = process engine over no work records (Workflow Management Platform territory)
- 3 without 1+2 = reporting shell over nothing
- 1+2 without 3 = container-scoped team tracker (issue-tracker-like)
- 1+3 without 2 = task manager with dashboards
- 2+3 without 1 = process tooling with no work population

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Multiple switchable views over the same records (list/board/table, Gantt/timeline, calendar, workload)
- Comments, mentions, attachments, activity history on records
- Sharing/permissions ladders (member/guest/viewer roles; per-container access; private vs open containers)
- Templates of recurring work (project/task templates, blueprints, bundles)
- Notifications/inbox and personal work queues
- Integrations (calendar, chat, file storage, dev tools) and APIs
- Mobile/desktop apps; search; admin console; SSO/enterprise security
- Sub-item decomposition (subtasks/subitems); dependencies with date effects
- AI assistance (era-current)

### L2 — Variant / Optional Structure

- Goals/OKR layer and portfolio rollups (present in mature products, plan-gated; not required to recognize the Type)
- Resource management depth: workload views → capacity planning → time tracking/timesheets (premium modules in-sample)
- Substrate philosophy: grid-native (Smartsheet), board-native (monday), list-native (Asana/ClickUp/Wrike) — one Type, different center surfaces
- Bundled content/communication surfaces: docs, whiteboards, chat (ClickUp converged workspace; monday workdocs; Wrike document editor) — packaging, not identity
- Vertical packaging on the same engine: CRM/dev/service variants (monday), proofing/creative (Wrike/Smartsheet Brandfolder), sprint folders (ClickUp)
- Intake depth: internal-only forms ↔ public external request forms with submission analytics
- Approval machinery depth: simple status gates ↔ ordered multi-step approval chains ↔ file proofing
- Automation metering (action-based pricing) — business-model variant
- Deployment: SaaS-dominant; platform-embedded realizations (Microsoft Planner/Lists inside M365) satisfy the core

### L3 — Vendor-specific (Research Notes only)

- monday: "Work OS" framing; WorkCanvas/WorkForms/Sidekick product names; automation importance labels; 30+ widget count
- Smartsheet: Control Center, Bridge, DataMesh, Data Shuttle, DataTable, Dynamic View, WorkApps, Brandfolder, "Intelligent Work Management" framing
- Wrike: Blueprints, Custom Item Types, Lightspeed, Access Roles naming, Collaborator/Contributor role ladder
- ClickUp: ClickApps, Hubs, Brain, Agents, ClickUp 4.0 converged workspace, "everything app for work"
- Asana: AI Studio/Teammates/Dash, Bundles, "operating system for human-agent teams"

## Vendor-specific Findings

- monday's automation "importance" labels explicitly do not affect execution order (product-specific UX).
- Smartsheet's approval workflows pause until approval completes and support ordered multi-approver chains (direct Tier-1; held common-mature, not definitional — Wrike documents approvals on tasks/folders/projects, others realize approvals via statuses/automations).
- Wrike request forms can create blueprints and custom item types, not only tasks/projects (product-specific depth).
- ClickUp's multiple-lists membership (one task in several lists) is a product-specific realization of cross-container work.
- Smartsheet's update requests collect edits from people not shared into the sheet (product-specific collaboration mechanism).

## Boundary Findings

1. **vs Project Management Application (§03.07 sibling — joint-review flag DISCHARGED, keep-both RATIFIED).** PM's unit of record is the bounded undertaking (project as persistent container with a plan of record tracked to that undertaking's end, project-scope progress loop). WM's unit of record is the team's whole ongoing work population; the project is one container type among several; there is no plan-of-record requirement; the coordination surface reads across containers. The market blurs hard — the same products (Asana, monday, Smartsheet) are marketed in both vocabularies, and both passes' samples overlap — so attribution is by center of gravity, not feature lists. Removal tests both directions: strip WM to one bounded undertaking + its plan + progress → PM remains; add requests/process machinery/approvals/cross-container reporting to PM → WM. The PM pass's scheduling-intensive machinery (Gantt/dependencies/baselines/critical path) is lineage differentiation inside PM, not the WM wall — WM products also ship Gantt/timeline views without becoming PM.
2. **vs Task Management Application (§03.06 sibling — flag DISCHARGED, keep-both RATIFIED).** Task management centers discrete completable task records for people (two-state open→done grammar, personal-first organization, execution views). WM centers the team's operational work population with process machinery and a coordination surface. The task pass's removal test is adopted and confirmed: remove forms/requests/approval/process machinery → task management remains. Asana straddles both vocabularies (one product family marketing both) — packaging overlap documented, not a Type merge.
3. **vs Project Portfolio Management Application (§03.07 sibling — flag DISCHARGED, keep-both RATIFIED).** PPM centers the governed investment collection above projects (selection, funding, benefits, rebalancing — investment objects serving PMO/executive governance). WM centers operational work where a portfolio is one optional rollup container. PPM's record is the investment; WM's record is the work item. WM products ship portfolio *views*; PPM owns the investment decision loop.
4. **vs Workflow Management Platform (§10 — adjacency DISCHARGED, keep-both).** The workflow platform's unit of record is the configured recurring process pattern and its executed instances (process-first). WM's unit of record is the work item; process machinery is attached to the population (work-first). The "workflow" term collision is real — WM vendors call their automations/status machinery "workflows" (Wrike "Custom Statuses and Workflows", Asana "workflow automation", monday "building workflows") — but in WM the process layer serves the work records; in the workflow platform the process definition IS the record. Test: delete the work records and keep the patterns → workflow platform; delete the patterns and keep the records → task manager.
5. **vs Collaborative Spreadsheet / Structured Table (§03.03 — confirms sibling drift pole).** Smartsheet is the documented drift pole: rows-as-cells in a calculation grid = spreadsheet; rows become scheduled, dependent, approvable work items with status workflows and the grid becomes the surface = WM. The structured-table pass recorded the same wall (user-defined tables vs managed work objects).
6. **vs Collaborative Workspace / Team Workspace Platform (§03.12).** Workspace Types center persistent shared content (pages/docs) with membership; tasks are one content type inside. WM centers work records with status machinery; docs are one bundled surface. ClickUp's own comparison page draws this seam from the vendor side ("Notion is a document-first workspace").
7. **vs Kanban Task Board (§03.06).** The board is one view/container inside WM; standalone board tools remain their own Type (kanban pass: "packaging embedding does not change the board's Type").
8. **vs Business Management Suite (§10).** WM lacks the customer+money transaction spine; it manages work for teams, not business transactions for a company (business-management-suite pass seam, confirmed).
9. **vs Professional Services Automation (§10 — PPM pass's carried flag, seam recorded).** PSA adds the billable-commercial layer over work-management-like machinery (client projects, time→billing, utilization economics). WM's work has no commercial settlement semantics. Flag left for the PSA pass; not resolved here.
10. **"Workflow"-term collision note for the directory:** WM products' "workflow" vocabulary (automations, status workflows, request workflows) is process machinery over work records — it must not be conflated with the Workflow Management Platform Type (§10) whose record is the process instance. Recorded as a naming hazard, no directory change.

## Historical / Market-Sample Check (§24)

- The Type is software-native; no paper-era ancestor is claimed. The relevant historical population is the early-web generation (2004–2010: Basecamp-class PM tools, early Smartsheet/Wrike) and platform-native realizations (Microsoft Planner/Lists inside M365).
- Early-web generation check: shared structured work records in containers (sheets/folders/projects with owners, dates, status columns) satisfy leg 1; status columns with defined states and manual routing satisfy leg 2 in its minimal realization; early reports/personal views satisfy leg 3 minimally. The full modern machinery (trigger-action automations, public intake forms, ordered approval chains) is the category's maturation — held as the modern realization of the governed-movement invariant, NOT as separate invariants. The L0 phrasing ("work's movement governed by states and rules held in the system") is deliberately abstract enough that a status-column-plus-manual-routing generation fits.
- Platform-native check: Planner/Lists-class products (structured records in lists, views, Power-Automate-class rules) satisfy all three legs without any vendor-specific machinery.
- Anti-overfit guards: grid substrate NOT definitional (board-native and list-native poles in-sample); automations/forms/approvals as named features NOT definitional individually (the governed-movement invariant is; the machinery generation is era-current); goals/portfolios NOT definitional (rollup containers, plan-gated); AI NOT definitional; SaaS-only NOT definitional (platform-embedded pole).

## Uncertainties

- Asana operational detail (help center) unverified — all Asana claims held at feature-existence strength; no Asana-specific rule/limit appears in the final document.
- ClickUp automations detail not fetched (features known from category structure only); held at category strength.
- Approval machinery: directly evidenced at 2/5 (Smartsheet, Wrike); held common-mature, not definitional. Whether monday/ClickUp ship dedicated approval objects was not confirmed.
- The exact plan-gating of goals/portfolios per product was not researched (pricing-tier detail — L3 territory, excluded).
- Professional Services Automation seam left to the PSA pass (flag carried, not resolved).

## Final Synthesis

The Work Management Platform is the team's operational work system: a shared, structured population of work records held in an organizational container hierarchy where projects are one container among several; a configured process layer (status workflows, automations, approvals, intake forms) that moves the work; and a cross-container coordination surface (personal work views, dashboards/reports, portfolio/goal rollups) that lets the team and organization see and steer all of it. Everything else — views, templates, integrations, workload, docs, chat, AI, vertical packaging — is mature added structure or variant packaging. The Type sits between Project Management (bounded undertaking as unit of record), Task Management (discrete completable records for people), Project Portfolio Management (governed investment collection above projects), and Workflow Management Platform (process instances as the record), and it is the drift destination of grid products whose rows become managed work items.
