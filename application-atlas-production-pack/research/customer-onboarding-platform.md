# Research Notes — Customer Onboarding Platform

## Research Goal

Understand, from real products, what a **Customer Onboarding Platform** is: the vendor-side software used to run a specific new customer's transition from closed deal to first value — what its unit of record is, how the work is structured, who does the work, what the customer sees, and where its boundaries sit against Customer Success Platform, Project Management, PSA, Employee Onboarding, in-app onboarding/guidance tools, and Customer Training platforms.

## Initial Boundary (hypothesis before research)

- Hypothesis A (primary): the leaf is the vendor-side managed onboarding engagement for a new customer — per-customer plan of work, two-sided tasks, customer-facing portal/workspace, tracked to go-live/activation. Placed in §07 (Sales, Customer & Revenue) next to Customer Success Platform, Customer Health Monitoring, Product Usage/Adoption.
- Hypothesis B (competing): the leaf could mean in-app product onboarding (tours, checklists, tooltips — the "user onboarding" tools). Prior processed research (product-usage-adoption-platform) already flagged that guidance-first products have no directory leaf; if evidence showed this leaf is that category, a taxonomy problem would be recorded.
- Nearest neighbors to test: Customer Success Platform (§07), Project Management Application (§03.07), Professional Services Automation (§10), Employee Onboarding Platform (§09, processed), Customer Training / Academy Platform (§07), Customer Portal (§07), CRM (§07).

## Research Questions

1. What is the unit of record — is there a per-customer "engagement" object, and how is it bound to the customer?
2. How is the work structured — stages/phases/milestones/tasks? What does a task carry (owner, status, dates, dependencies, instructions)?
3. Who does the work — are tasks assigned to the customer (and third parties) as well as vendor staff? Is the customer a worker in the plan or only its subject?
4. What does the customer see — portal/workspace? What visibility control exists over internal vs shared items?
5. How does the engagement start (template? CRM handoff?) and end (go-live? handoff to CS?)?
6. What rules matter — dependencies, visibility, permissions, notifications?
7. What is common but not definitional — templates, resource management, time tracking, financials, AI?
8. Where are the boundaries vs the neighbors listed above?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies:

1. **GuideCX** — pure-play customer onboarding, portal-first philosophy (the customer-facing experience is the product).
2. **Rocketlane** — pure-play customer onboarding + implementation, project-management-grade philosophy (deep plan machinery, resource/financial management).
3. **Dock** — client-workspace-first philosophy (shared workspace spanning sales → onboarding → ongoing collaboration, with embedded mutual action plans).
4. **EverAfter** — customer-success-workspace philosophy (branded per-account hub covering onboarding → adoption → QBR → renewal). Tier-2 evidence only.
5. **Totango** — CS-suite boundary check (onboarding realized as a lifecycle stage/program inside a customer success platform).

Boundary check only (not part of the Type): **Userflow** (in-app onboarding/guidance category).

## Sources

Research date: **2026-09-08**

- Rocketlane Support / Help Center — https://help.rocketlane.com/ (home; Project Management articles: "How to Create a Rocketlane Project?", "Inviting your Team and Customers to a Project"; Customer Portal section) — Tier 1
- GuideCX Knowledge Base — https://help.guidecx.com/ (GUIDE 2.0 collection; "Tasks in 2.0") — Tier 1
- Dock Help Center — https://help.dock.us/ (Workspaces collection; "Using Dock for Project Management": "What are Project Plans?", "Tasks in Project Plans") — Tier 1
- EverAfter — https://www.everafter.ai/ (product/solutions pages) — Tier 2 (help center at help.everafter.ai unreachable; one transport error, abandoned per network rule)
- Totango Support — https://support.totango.com/hc/en-us (home; Terminology guide) — Tier 1 (boundary check)
- Userflow — https://userflow.com/ (product/solutions pages) — Tier 2 (boundary check)

## Product A — GuideCX (Tier 1)

### Key observations (evidence layer A unless noted)

- **Project is the unit of record.** Help center organized around projects + tasks: Projects List Page, Project Details Page, Project Plan 2.0, Tasks in 2.0, Global Tasks Page, Program Management (multi-project), Project Team Tab.
- **Task model** ("Tasks in 2.0"): tasks are "the building blocks of every project"; each carries instructions, **assignee + role**, **dependencies** ("determine when the task becomes available to be worked on"), duration/due date; subtasks; attachments; checklists; custom fields (with "Internal Only" marking); estimated hours; tags.
- **Two-sided + third-party work distribution**: task **Responsibility** is explicitly typed **Customer / Internal / Third Party**. Assignee roles span Admins, Managers, Guides, Task Owners, Contributors, **Customers**, **Third Parties**. Customers and Third Parties cannot log time; they can complete checklist items when assigned.
- **Per-task customer visibility control**: for internal tasks, **Visibility** = Visible (customer sees full details) / **Task Name Only** (customer sees name, cannot expand) / **Hidden** (internal only). This is a first-class task attribute.
- **Customer participation via notifications**: when a task's dependency is met, GUIDEcx emails the assignee a **Task Assignment Email** with instructions, due date, attachments, and **action buttons to update task status directly from email**; customers can opt into **SMS notifications** "when it's their turn to complete a task"; reminders 1 day before / 1 day after due date.
- **Customer-facing surfaces**: "Customer Views in 2.0", **Embedded Onboarding Portal 2.0** (portal embeddable in the vendor's own product), Brands for projects (white-labeling).
- **Templates**: Template Library; "How to Templatize Project Plans"; template migration tooling.
- **Portfolio layer**: Program Management (GUIDE 2.0); GUIDEreports with standard reports **Customer Engagement**, Projects Overview, Task Management; Project Warnings ("Proactive Action Insights"); History Tab.
- **Vendor-side resourcing**: Resource Management collection — Dispatching, **PSA Assignment Engine**, workspace availability types, holidays/time off, People Timeline View, Task Planning View, estimated capacity.
- **Time tracking**: configurable ("Configure Time Tracking", "Require Time Tracking in 2.0") — vendor-side effort capture.
- **Integrations**: Jira, Salesforce via "Recipe Builder"; Open API; Analytics API; SSO.
- **AI**: "RAG Agentic Coach", "Tempo AI Project Performance" (era-current, L3).

## Product B — Rocketlane (Tier 1)

### Key observations

- **Project creation is customer-bound** ("How to Create a Rocketlane Project?"): the New Project dialog requires selecting a **Customer name**, project name, status, **template** (phases + tasks instantiated from it; multiple templates combinable), start date, due date (**auto-calculated from template duration**), then **Teammates**: Project Owner (default: creator), team members, a **Champion** role on the customer side, and **inviting members from the customer's team by email**; Team Visibility permissions; then Additional information.
- **Project structure**: Project Plan view with **phases and tasks**; phase dependencies; task dependencies; timeline view with date shifting; Project Overview; Project Settings; Projects Page (portfolio); bulk updates; saved views; global search.
- **Two-sided team**: "You can add team members from your Organisation and invite team members from your Customer's Organisation to your Projects" — Project Owner (crown icon) on vendor side, **Champion** on customer side; invites by email; join/leave project; RBAC article covers "permissions for team members and customers".
- **Customer Portal** (dedicated help section): "Collaborate with your customers on tasks, initiate chats and share files all in one place using Rocketlane customer portal"; portal is buildable ("How to build your customer portal"), customers invited to it, Slack integration, time tracking in portal.
- **Templates**: project, task, form, and document templates "reused dynamically in your project plans"; dynamic project templates.
- **Automations**: dedicated collection ("Automate the grunt work…").
- **Vendor-side operations (PSA-grade)**: Time Tracking (timesheets, approvals), Resource Management (allocations, skills matrix, Resource AI, utilization), **Financial Management** (budgets, rate cards, cost rates, billing methods, fixed-fee vs time-and-material, revenue recognition, invoices, expenses, posting periods), Reporting and Dashboards.
- **Integrations**: Salesforce, Jira, Slack; MCP tools (era-current, L3).

## Product C — Dock (Tier 1)

### Key observations

- **Workspace is the unit of record**: shared client workspaces with **pages, sections, embedded content, contact cards, real-time collaboration**; workspace owners; key dates; duplicating; connected workspaces; account mapping (to CRM accounts).
- **Sharing model**: Sharing/Publishing workspaces; **Workspace Roles**; **Control Access by Page**; **Hiding/Showing Sections from the Shared View**; workspace-to-PDF export.
- **Project Plans = mutual action plans** ("What are Project Plans?"): "Dock enables you to collaborate hands-on with customers and prospects through mutual action plans. You can customize Checklists, Timelines and Kanbans…". First listed use case: **"Onboarding a new customer or partner — align on timelines and key milestones, assign ownership and check off to-do's, send reminders on action items."** Also: sales-process next steps, and **"Internal alignment (i.e. Sales to Onboarding handoff)"**.
- **Task model** ("Tasks in Project Plans"): checklist tasks with **ownership assignment** — assign to **Teams**, **People** (workspace members), or **+Enter an email** ("assign any email the task" — customers without accounts); **Internal toggle** ("designates that task as internal only and hides it from the Shared view"); statuses (default To-Do / In-Progress / Completed, custom statuses); start/due dates incl. **relative dates**; automatic due-date reminder notifications; **action buttons** on tasks: external link, link to workspace page, **File Download**, **File Upload** ("makes it easy to request files that you need from customers"); rich-text descriptions with embedded content; subtasks; Project Widget; Global Task Management; Project Plan Templates.
- **Templates**: workspace, page, and section templates; **synced pages/sections** (central content updates); dynamic variables (personalization).
- **Communication**: comment threads, message threads inside the shared workspace.
- **Other collections**: Sales Order Forms (order/procurement side), Survey Forms, Content Management, Reporting, Security Profiles, Admin, Integrations (32 articles), Learning (Playbooks/Courses), Dock AI.

## Product D — EverAfter (Tier 2 — marketing site only)

### Key observations (assertion strength reduced accordingly)

- Positions as "AI-Powered Digital Customer Success Platform": "One branded hub for onboarding, adoption, QBRs and renewals, personalized per account and orchestrated by AI."
- **Programs** include **High-Touch Onboarding** ("speed up time-to-value"), **Digital-Touch Onboarding** ("personalized at scale"), POC (mutual action plan), Success Plan, QBR, Advocacy — onboarding is the first program of the account hub.
- **Capabilities**: AI-Powered Interface Builder, AI Studio, AI Agent for Journeys, AI Experts, **Task Management**, **Data Collection**, Integrations.
- Time-to-value solution page: "Provide complete transparency into the onboarding process for both your customer's team and your internal stakeholders. Embed strong goal-setting features, **status trackers and automated milestone updates**, to ensure alignment."
- Customer testimonials reference onboarding modules completed "in days versus weeks", digital/scaled onboarding at enterprise scale.
- Help center (help.everafter.ai) unreachable this pass — task-level mechanics not verified; structure-level claims only.

## Product E — Totango (Tier 1, boundary check only)

### Key observations

- CS platform object model (Terminology guide): **Account profile** (unit of record is the account, not the engagement); **Success plan** ("documentation tool within an account profile to track customer objectives… Optionally share plan objectives and assign tasks to customers via **Customer Portal**"); **Customer Portal** ("shared website where your customer contacts can view shared success plan objectives, track the progress in real-time, and **complete tasks assigned to them**"); **SuccessBLOC** = "ready-to-use toolkit to drive programs within the customer journey (e.g., **Onboarding**, Renewal, Expansion, Risk)"; **SuccessPlay** = pre-built workflow assigning internal tasks; **Lifecycle status attributes** = "classification system to group customers within pre-defined stages… such as in the **'Onboarding' stage** of the customer journey"; **account assignment team roles** include **Onboarding Manager**.
- Reading: in the CS-suite pole, onboarding is a **lifecycle stage + program toolkit** operated through the CS platform's journey machinery; the customer-portal + customer-assigned-tasks pattern is shared with the onboarding-platform Type, but the unit of record remains the account relationship, not a per-customer onboarding engagement.

## Product F — Userflow (Tier 2, boundary check only — NOT this Type)

- "AI-Powered Product Adoption & Onboarding Platform": in-app **tours, guides, checklists, resource centers, tooltips, banners, surveys** deployed **inside the vendor's own product UI**, targeted by user segments and product signals, built no-code by product/growth/CS teams; AI agent completes tasks for end users.
- Object model = flows/experiences + targeting rules + in-product deployment. No per-customer engagement, no plan of work with two-sided owners, no shared project surface. Confirms Hypothesis B is a **different territory** (guidance-first / digital adoption), consistent with the prior product-usage-adoption research note that this category has no directory leaf.

## Cross-product Comparison

| Structure | GuideCX | Rocketlane | Dock | EverAfter (T2) | Totango (boundary) |
|---|---|---|---|---|---|
| Per-customer engagement of record | Project (customer-bound) | Project (requires Customer name) | Workspace (per account) | Branded hub per account | Account + lifecycle stage (no engagement object) |
| Plan of work (stages/milestones + tasks) | Project Plan: tasks/subtasks, dependencies, durations | Project Plan: phases, tasks, dependencies, milestones | Project Plan section: checklist/timeline/kanban | Task management + journeys, milestones | SuccessBLOC program + SuccessPlays + tasks |
| Two-sided work (customer-assigned tasks) | Responsibility: Customer/Internal/Third Party; status-update from email; SMS | Customer team invited; Champion; portal tasks | Assign by email to anyone; file-upload requests | Tasks assigned to customers (T2) | Customer Portal: "complete tasks assigned to them" |
| Shared customer-facing surface | Customer Views; Embedded Onboarding Portal | Customer Portal (buildable; Slack) | Shared view; publish; per-page access | The hub itself | Customer Portal (shared success plan) |
| Per-item visibility control | Visible / Task Name Only / Hidden | Team visibility; RBAC incl. customers | Internal toggle; hide/show sections | not verified (T2) | share/unshare plan |
| Templates instantiated per customer | Template Library; templatized plans | Project/task/form/document templates; dynamic | Workspace/page/section templates; synced sections; dynamic variables | interface builder (T2) | SuccessBLOC toolkits |
| Progression tracking to completion | Project status; warnings; Customer Engagement report | Project status; dashboards; reporting | Project widget; dashboard views; trends | status trackers; automated milestone updates (T2) | lifecycle stage tracking |
| Notifications to both sides | assignment emails; reminders; SMS | portal notifications | due-date notifications; assignee notifications | automated updates (T2) | campaigns/emails |
| Customer data collection | attachments; custom fields | forms | file-upload action buttons; survey forms | Data Collection (T2) | — |
| Resources/content for customer | attachments; embedded portal | documents; portal files | embedded content; synced sections; file downloads | hub content (T2) | assets |
| Communication threads | task messages (internal/external); @mentions | portal chat | comment/message threads | discussion feeds (T2) | touchpoints |
| Portfolio / multi-engagement | Program Management; GUIDEreports | Projects page; bulk updates; dashboards | Connected workspaces; account mapping | — | portfolio segments |
| Vendor-side resource management | Dispatching; PSA Assignment Engine; availability | Allocations; skills matrix; Resource AI | — | — | team roles |
| Time tracking / financials | configurable time tracking | time tracking; budgets; rate cards; billing; revenue recognition | — | — | — |
| CRM handoff | Salesforce (Recipe Builder) | Salesforce integration | account mapping; HubSpot workflows; "Sales to Onboarding handoff" | Salesforce ISV (T2) | native CRM sync |
| AI (era-current) | RAG Agentic Coach; Tempo AI | Resource AI; MCP | Dock AI | AI agents for journeys (T2) | (Unison AI) |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a Customer Onboarding Platform:

1. **The per-customer onboarding engagement of record** — a persistent, individually identified engagement (project / plan / workspace) for ONE specific customer, existing to take that customer from closed deal to first value (go-live / activation / handoff to steady state). It is distinct from the account record itself. Remove → CRM/account management.
2. **The structured plan of work** — the engagement carries a plan organized as stages/phases/milestones and tasks, each with owner, status, and dates. Remove → account record with notes.
3. **Two-sided work distribution** — tasks in the plan are owned by vendor-side users AND by the customer (sometimes third parties); the customer is a tracked worker in the plan, not merely its subject. Remove → internal implementation project management (generic PM tool).
4. **Tracked progression toward a defined completion** — the engagement's progress is tracked (statuses, milestones) toward an explicit completion state. Remove → a to-do list with no journey.

Load-bearing combinations: 1+2 without 3+4 = generic project plan with a customer's name on it; 3+4 without 1 = a shared checklist with no engagement container; 1+3 without 2+4 = a customer contact with homework but no managed journey.

### L1 — Common Mature Structure

- Customer-facing shared surface (portal / shared workspace view) showing plan, progress, and resources
- Per-item visibility control (internal-only tasks, hidden sections, "name only" exposure)
- Reusable onboarding templates (project/plan/workspace templates) instantiated per customer, with dynamic personalization
- Task dependencies and scheduling (durations, relative/auto-calculated dates)
- Notifications and reminders to both sides (email, SMS, in-app)
- Customer data collection (forms, file-upload requests, attachments)
- Resources/content shared with the customer (documents, embedded content, synced sections)
- Communication threads (comments/messages, @mentions)
- Progress reporting and portfolio views across many onboardings (customer engagement reports, dashboards)
- CRM integration and sales→onboarding handoff
- Milestones / key dates

### L2 — Variant / Optional Structure

- Vendor-side resource management (dispatching, assignment engines, capacity, skills)
- Time tracking and financials (budgets, rate cards, billing, revenue recognition) — the PSA-grade pole
- Program management for multi-workstream enterprise implementations
- Digital-touch / scaled onboarding (automated low-touch journeys)
- Embedded portal (embedded in the vendor's own product); white-labeling/branding
- Third-party / implementation-partner participation as task owners
- Pre-sale use (POC/trial mutual action plans)
- Post-onboarding continuation (success plans, QBRs, renewals in the same workspace)
- AI assistance (AI coaches, AI agents, AI builders)

### L3 — Vendor-specific (research notes only)

GuideCX: Guides role, Recipe Builder, GUIDEreports, Tempo AI, GUIDE 1.0/2.0 split. Rocketlane: Nitro, Spotlighting, Sheets, MCP tools, plan tiers (Essential/Standard/Premium/Enterprise). Dock: Sales Order Forms, Playbooks/Courses, HubSpot workflow triggers. EverAfter: AI Studio, AI Experts, Interface Builder. Totango: SuccessBLOCs, SuccessPlays, Cadence, Unison.

## Rejected Findings

1. **"The customer portal defines the Type"** — rejected as L0. The portal is the modern surface for customer participation (L1). Spreadsheet-era onboarding (checklist with vendor/client owners, statuses, target dates, homework emailed to the customer, tracked to go-live) satisfies all four L0 legs without any portal. Historical check passed.
2. **"Templates define the Type"** — rejected. Template instantiation is common mature structure; a one-off plan written per customer still satisfies the core.
3. **"This is just project management with a customer name"** — rejected as a definition, retained as a boundary: generic PM lacks two-sided work distribution and the customer-facing shared surface; the discriminator is the customer as worker + participant.
4. **"This is in-app onboarding (tours/checklists in the product UI)"** — rejected. Userflow-class products deploy experiences inside the vendor's product UI for end users; no per-customer engagement, no two-sided plan. Different territory (no directory leaf; flagged).
5. **"Onboarding is a CS-platform feature, not a Type"** — rejected as a dissolution. The CS-suite pole (Totango) realizes onboarding as lifecycle stage + program toolkit, but a distinct product family (GuideCX, Rocketlane, Dock, EverAfter) exists whose unit of record is the per-customer engagement, not the account relationship. Module-convergence risk recorded.
6. **"Time tracking / financials define the Type"** — rejected. PSA-grade machinery is a variant pole (Rocketlane, GuideCX), absent in Dock/EverAfter.

## Boundary Findings

1. **vs Customer Success Platform (§07 sibling; sharpest seam)** — onboarding platform: unit of record = the per-customer transition engagement, ending at first value/handoff. CS platform: unit of record = the ongoing account relationship across the whole lifecycle (health, success plans, plays, renewals, QBRs). Evidence: Totango realizes onboarding as a lifecycle stage + SuccessBLOC inside the account-centric model; EverAfter/Dock extend the workspace beyond onboarding (adoption, QBRs, renewals). Test: remove ongoing-lifecycle machinery → the onboarding engagement still stands; remove the per-customer engagement plan → the CS platform still functions on portfolio signals. Overlap zone: customer portal, customer-assigned tasks, success plans.
2. **vs Project Management Application (§03.07)** — generic PM: projects/tasks/dependencies with internal teams only. This Type: customer-bound engagement + two-sided work + shared customer surface + sales-handoff semantics. Rocketlane/Dock contain generic-PM machinery as substrate; the discriminator is the customer side.
3. **vs Professional Services Automation (§10)** — PSA centers on billable service-delivery economics (resource utilization, time & billing, revenue recognition). Rocketlane and GuideCX carry PSA-grade machinery (both ship PSA assignment engines/time tracking; Rocketlane ships full financials) — a straddle documented at the variant level. The onboarding core is the customer transition, not the billable engagement economics.
4. **vs Employee Onboarding Platform (§09, processed)** — identical leaf-name pattern, different subject: customer-side orchestrates adoption of a product/service (accounts, usage, go-live); employee-side orchestrates entry into employment (compliance paperwork, pay, workplace, team). No shared structure beyond the generic journey/checklist pattern. (Already recorded in STATUS from the employee side; confirmed here from the customer side.)
5. **vs in-app onboarding / guidance products (no directory leaf)** — Userflow/Appcues-class products deploy tours/checklists/tooltips inside the vendor's product UI, targeted by segments/signals, built by product/growth teams. Different object model (flows + targeting vs engagement + plan), different builder, different surface. The two are complementary (a vendor may run both). Flag: guidance-first category still has no directory leaf (consistent with product-usage-adoption research).
6. **vs Customer Training / Academy Platform (§07)** — training platforms center on learning content, courses, certification; here, training content is one resource type shared inside the engagement plan.
7. **vs Customer Portal (§07 leaf)** — the portal is a surface; the onboarding platform is the managed engagement that *uses* a portal as one of its surfaces. A portal alone has no plan of work.
8. **vs CRM (§07)** — CRM stores the account/opportunity and the handoff; the onboarding platform instantiates and runs the engagement. Account mapping/integrations are the bridge (Dock "account mapping"; Rocketlane Salesforce integration; GuideCX Recipe Builder).

**"去掉什么就变成另一个 Type" 判据**：去掉客户侧参与（任务只归内部）→ 通用项目管理/实施跟踪；去掉 per-customer engagement（只看账户组合）→ Customer Success Platform；去掉计划与进度（只留共享内容页）→ Customer Portal / 客户资料页；去掉客户过渡语义（保留资源与财务）→ PSA；把对象换成"产品 UI 内的引导体验"→ in-app guidance（无目录叶）。

## Historical / Market-Sample Check

Spreadsheet-era customer onboarding: an implementation/onboarding manager keeps a per-customer checklist (task, owner = vendor or client, status, target date), emails the customer their homework, tracks progress to go-live, then hands the account to steady-state management. This satisfies all four L0 legs — engagement of record (the per-customer sheet), plan of work (rows with owner/status/date), two-sided work (client-owned rows), tracked progression (to go-live). No portal, no cloud, no template engine in the core. Managed-services implementation shops tracking customer deployments fit the same shape. The definition therefore does not over-fit to the modern portal-first SaaS packaging. ✓

## Uncertainties

1. **EverAfter depth**: help center unreachable; all EverAfter observations are Tier-2 (marketing). Task-level mechanics, visibility control, and portal behavior asserted at structure level only.
2. **Totango onboarding specifics**: the onboarding-playbooks article 404'd; onboarding-as-program evidence comes from the Terminology guide (SuccessBLOC example list, lifecycle stages, Onboarding Manager role) — sufficient for the boundary, not for program internals.
3. **Pure internal-only posture**: whether any marketed "customer onboarding platform" ships without any customer-facing surface — not verified; treated as thin-ancestor/edge posture, not a market pole.
4. **GuideCX 1.0 vs 2.0**: only 2.0 evidence fetched; legacy differences not examined.
5. **Numeric limits, plan-tier gating, exact cadences**: vendor facts (L3), deliberately excluded from the final document.
6. **Market naming drift**: "customer onboarding platform" is also used loosely by in-app guidance vendors for their "user onboarding" use case; the directory leaf is interpreted here as the §07 customer-lifecycle engagement Type, consistent with its placement.

## Final Synthesis

A Customer Onboarding Platform is vendor-side software whose unit of record is a per-customer onboarding engagement — a persistent, individually identified engagement for one specific customer, carrying a structured plan of work (stages/phases/milestones and tasks with owners, statuses, dates) in which work is deliberately distributed across both sides: vendor staff and the customer (sometimes third parties) each own and complete tasks, with per-item control over what the customer can see. The engagement is tracked through statuses and milestones toward a defined completion — go-live, activation, or handoff to steady-state management. Around this core, mature products add: a customer-facing portal or shared workspace; reusable templates instantiated per customer; dependencies and scheduling; notifications to both sides; customer data collection; shared resources and content; communication threads; portfolio reporting across many onboardings; and CRM handoff. Variant poles: project-management-grade (resource management, time tracking, financials — PSA-adjacent), portal-first, workspace-first (spanning sales → onboarding → ongoing collaboration), and CS-suite module (onboarding as a lifecycle stage inside a customer success platform). The Type's neighbors are separated by what they hold as the unit of record: the engagement (here), the account relationship (CS platform), the internal project (PM), the billable service engagement (PSA), the new hire (employee onboarding), the in-product flow (in-app guidance).
