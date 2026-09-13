# Research Notes — Robotic Process Automation Platform

## Research Goal

Establish what a Robotic Process Automation (RPA) Platform is as an Application Type: the core objects (automation artifact, executor, execution instance, control plane), the canonical build→publish→deploy→trigger→execute→monitor lifecycle, the rules that govern execution, and the boundaries against the neighboring automation Types — especially Desktop Automation Application (§03.16, processed) and Agent Tool / Computer-use Platform (§13, processed), both of which carry open joint-review flags that this pass must discharge.

## Initial Boundary

Working hypothesis entering research:

- RPA Platform = enterprise automation platform where human-authored deterministic automations ("bots"/"robots") operate the organization's existing applications (canonically through their UIs), executed as centrally managed, triggered, monitored jobs across a fleet of machines, governed as organizational assets.
- Nearest neighbors: Desktop Automation Application (same mechanism, different ownership/scale), Agent/computer-use platforms (same target surface, different runtime decision-maker), BPM/Workflow platforms (orchestration vs execution), Test Automation (same GUI machinery, different job), low-code app platforms (build new software vs automate existing apps), ETL/integration platforms (data-level vs surface-level).
- Open flags to discharge: (1) agent-tool pass flagged RPA vs agent boundary for joint review; (2) desktop-automation pass recorded the ownership/scale discriminator and removal test, pending RPA-side confirmation.

## Research Questions

1. What is the automation artifact called and what is its structure (process/flow/bot; steps, decisions, targeting)?
2. How is it authored (visual designer, recorder, code)? Who authors it?
3. How does execution work: attended vs unattended; triggers (schedule/event/queue/human); what happens on the machine (sessions)?
4. What does the central control plane manage: deployment, machines/robots, monitoring, queues, credentials, audit, versions?
5. What is the execution-instance lifecycle and its states (job/session/run/transaction)?
6. How is work distributed at item level (work queues, statuses, retries, exceptions, reviewers)?
7. What rules/exceptions matter (determinism, UI-change fragility, session locking, stop semantics, exception taxonomy, concurrency/capacity)?
8. Who uses the product and in what operating model (developer, ops admin, CoE, citizen developer)?
9. Where do AI/agentic features sit relative to the deterministic core (authoring aid? callable step? separate agent layer?)
10. Where are the boundaries vs the neighboring Types listed above?

## Representative Products

Selected for market representation, documentation completeness, product philosophy, and customer tier:

1. **UiPath** — enterprise market leader; full-stack platform (Studio authoring family + Robot/Assistant + Orchestrator control plane); strong Tier-1 docs.
2. **SS&C Blue Prism (Blue Prism Enterprise)** — enterprise, centralized-operations heritage ("digital workforce" philosophy); Tier-1 docs reachable.
3. **Microsoft Power Automate (desktop flows / RPA side)** — suite-embedded, citizen-developer pole; the bridge product identified by the desktop-automation pass; strong Tier-1 docs (Microsoft Learn).
4. **Automation Anywhere** — enterprise, cloud-native; now self-branded "Agentic Process Automation Platform" with RPA as a product line; Tier-1 docs JS-gated, so Tier-2 official product/education pages only.

## Sources

Research date: 2026-09-07.

Tier-1 (official operational documentation, directly fetched):

- Power Automate — Introduction to desktop flows: https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction
- Power Automate — Manage machines: https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines
- UiPath — Documentation home (product map): https://docs.uipath.com/
- UiPath — Studio: Creating a basic process: https://docs.uipath.com/studio/standalone/latest/user-guide/creating-basic-process
- UiPath — Orchestrator: About queues and transactions: https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/about-queues-and-transactions
- UiPath — Elastic robot orchestration: https://docs.uipath.com/orchestrator/automation-cloud/latest/user-guide/elastic-robot-orchestration
- Blue Prism — Documentation home: https://docs.blueprism.com/ → https://documentation.blueprism.com/bp-7-5/en-us/home.htm
- Blue Prism — Studio: https://documentation.blueprism.com/bp-7-5/en-us/frmProcessStudio.htm
- Blue Prism — Control Room: https://documentation.blueprism.com/bp-7-5/en-us/frmControlRoom.htm

Tier-2 (official product/marketing pages, directly fetched):

- Automation Anywhere — APA Platform product page: https://www.automationanywhere.com/products/automation-360
- Automation Anywhere — "What is RPA?": https://www.automationanywhere.com/rpa/robotic-process-automation

Source-access limitations:

- Automation Anywhere product documentation portal (docs.automationanywhere.com) is a JavaScript-only application; returned an empty shell twice. All Automation Anywhere structural claims are therefore limited to Tier-2 official pages; no Control Room terminology, bot lifecycle, roles, or queue mechanics were asserted from memory.
- UiPath "About Orchestrator" overview page returned 404 on three URL variants; Orchestrator claims rest on the queues/transactions page, the elastic-robot-orchestration page, and the product map — no Orchestrator UI specifics asserted.
- Blue Prism work-queue detail page not reachable (filename guess 404 ×1; not retried further); Power Automate work-queue page 404 ×2 (two paths). Item-level queue machinery is documented directly only by UiPath.
- Robot Framework / Robocorp (open-source developer-centric pole) not researched this pass.

---

## Product A — UiPath (Tier-1)

### Key observations (evidence layer A = direct)

- **Product family map (docs home):** Studio (professional designer), Studio Web (browser), StudioX (business-user designer), Robot, Assistant (attended surface), Orchestrator (control plane), Action Center (human-in-the-loop), Apps, Integration Service (connectors), Document Understanding, AI Computer Vision, Process Mining, Task Mining, Insights (analytics), Automation Ops (governance), Automation Hub (pipeline), Test Cloud / Test Manager (separate test product line), Marketplace, Data Fabric, Agents + Maestro (agentic orchestration layer: "Orchestrate AI agents, automations, and people"), Healing Agent ("self-healing" selectors), Automation Cloud Robots (Serverless and VM).
- **Authoring (Studio tutorial):** create a **project** (Process type, compatibility/language options) → drag **activities** from a palette into a **Sequence** on the Designer panel → **"Indicate application to automate"** targeting (point at a browser/Notepad window; screenshot + URL/path captured) → **Get Text / Type Into / Write Line** activities with **variables** (scoped) → **Run File** executes locally on the developer's machine. Targeting is UI-surface targeting by indication.
- **Queues & transactions (Orchestrator):** a **queue** is a container of items ("unlimited number of items"); queue items carry free-form or schema-validated (JSON schema) data; "As soon as queue items are processed, they become **transactions**". Transaction page shows statuses, processing dates, the Robot that processed them, exception type. **Queue triggers** "automatically start Maestro or RPA processes whenever new items are added". Processing order: deadline → priority → FIFO. Unique-reference enforcement; failed/abandoned items assignable to a **reviewer** with tracked review status; audit history. SLA predictions and Risk SLA (vendor-specific machinery). Failure classes: "application or business exception"; schema violations fail with a "Business Exception". Jobs can end "Faulted" (duplicate reference error).
- **Fleet orchestration (elastic robot orchestration):** "automatically scale your unattended robots… in the cloud"; machines provisioned manually (custom VMs) or automatically from a VM image template; UiPath installs/connects Robot to Orchestrator and runs jobs automatically; controls: maximum machine count, optimize for speed/cost, scheduled settings; cloud providers AWS/GCP/Azure.
- **Inference (structural):** the split between a design-time tool (Studio) that builds and tests automations locally, and a cloud/on-prem control plane (Orchestrator) that runs them on machines, is the platform's organizing architecture.

## Product B — SS&C Blue Prism / Blue Prism Enterprise 7.5 (Tier-1)

### Key observations (evidence layer A = direct)

- **Positioning (docs home + Enterprise home):** "Blue Prism® Enterprise is an intelligent automation (IA) solution that blends artificial intelligence (AI) and robotic process automation (RPA). With an SS&C Blue Prism **digital workforce**…" Surrounding products: Blue Prism Cloud, Hub/Interact (web frontends incl. web Control Room), Capture (process capture), Process Intelligence, Decipher IDP, Document Automation, **Blue Prism Desktop** (a lighter desktop-licensed product), WorkHQ ("next generation"), AI Gateway.
- **Studio (design area):** "where **processes and objects** are created, modified and undergo initial testing **before published to be used in Control Room**". Drag-and-drop flow construction "using the resources deployed on the current machine". Processes and objects organized into groups (tree + list); **version history per process/object**; clone; delete; **permission-locked groups** ("Setting permissions on a group requires the user to be assigned a role"); dual-license environments distinguish Desktop-published vs Enterprise-published processes by icon.
- **Control Room (operations area):** "the area of Blue Prism in which processes that have been designed, tested and **deployed** can be **controlled in a real world environment**." Displays **processes, resources and sessions**. Definitions given verbatim by the docs:
  - **Process** = "a business process previously designed and tested from Process Studio. It encapsulates a specific business process by taking pre-developed actions and making decisions based on their outcomes."
  - **Resource** = "a unit that performs all, or part of a process and can be either human, or more commonly, machine."
  - **Session** = "a process that is currently assigned to a resource. It maintains a state (for example, *Pending*, *Running*, *Completed*)".
- **Session operations:** create by dragging a process onto a resource (or resource onto process); cannot assign Enterprise processes to Desktop resources; bulk-run one process on several resources; **Stop** semantics: "Immediate Stop" vs "Request Stop" — a flag the running process can check via `IsStopRequested()` "allowing it to exit cleanly".
- **Inference (structural):** Blue Prism's core vocabulary — process (authored artifact) → publish → resource (executor: human or machine) → session (tracked execution with states) → control — is the cleanest articulation of the RPA platform model among the sampled products.

## Product C — Microsoft Power Automate (desktop flows) (Tier-1)

### Key observations (evidence layer A = direct)

- **Positioning (intro):** "Desktop flows **broaden the existing robotic process automation (RPA) capabilities** in Power Automate and enable you to automate all repetitive desktop processes." Designer with "prebuilt drag-and-drop actions or recording your own desktop flows to run later". Targets: "legacy applications, such as terminal emulators, modern web and desktop applications, Excel files, and folders". Interaction: "by using application **UI elements, images, or coordinates**." Users: home, small business, enterprise ("an employee of a large enterprise who automates data entry on an ERP system"). Same bridge-product framing the desktop-automation pass recorded.
- **Machine management (Manage machines):**
  - "**Machines** are the physical or virtual devices you use to automate desktop processes." Registering a machine to the cloud "allows you to harness the full power of robotic process automation (RPA)." Sign-in to the **machine-runtime app** auto-registers the machine into an **environment**; machine has name/description/environment.
  - Machine registration requires roles (**Environment Maker** or **Desktop Flow Machine Owner**); VM cloning caveat ("don't clone the virtual machine after installing machine runtime").
  - **Triggers:** "Power Automate enables you to trigger desktop flows from cloud flows using **events, schedules, and buttons**"; requires a **desktop flow connection**; attended RPA needs a premium per-user plan.
  - **Unattended:** "you need some **unattended bots** on the machine. Each unattended bot on a machine can carry **one** unattended desktop flow run at a time" — capacity ("process capacity or unattended RPA capacity") is allocated to machines.
  - **Connection = session machinery:** "When you create a desktop flow connection, you allow Power Automate to **create a Windows session on your machine** to run your desktop flows."
  - **Maintenance mode** per machine/machine-group stops new runs (running ones not canceled; new runs queue).
  - **Monitor > Machines:** name, version, group, status, "number of flows running", "number of flows queued", access type, owner. **Machine groups** (limit: 50 machines — precise number stays in notes).
  - **Sharing/permissions:** share machine with **Co-owner / User** permission levels; environment security roles (Desktop Flows Machine Owner / User / User-Can-Share) mapping to register/run/share/edit/delete actions.
  - Queued-run and run-duration limits exist (12 h queueing; unlimited run) — precise numbers stay in notes.
- **Inference (structural):** even the suite-embedded, citizen-developer product converges on the same RPA machinery — registered machines, unattended bots as capacity units, cloud-triggered attended/unattended runs, group management, monitoring — confirming the Type boundary drawn from the desktop side.

## Product D — Automation Anywhere (Tier-2 only)

### Key observations (evidence layer B/T2 = official marketing/education pages; structural claims reduced accordingly)

- **Positioning:** flagship self-brand is now "**Agentic Process Automation Platform**" ("orchestrates goal-based AI agents, RPA, APIs, and human expertise in one unified platform"). RPA remains a listed product line: RPA Software, Automation Workspace (low-code bot building), CoE Manager, Cloud Service, Citizen Developers; Mozart Orchestrator (platform feature).
- **Definition & character:** "RPA is software that automates digital tasks quickly and reliably… rules-based… generating a complete **audit trail** of actions". Origins attributed to "keystroke macros developed for business applications in the **1990s**" (vendor history claim, Tier-2).
- **Categories:** **Unattended** ("pre-programmed triggers, data inputs, and schedules to run independently… back-office processes like data entry, IT operations"); **Attended** ("initiated with triggers or inputs to help human workers with routine tasks on demand… customer service and IT helpdesk… human-in-the-loop oversight"); **Hybrid**.
- **Enterprise scale:** "run thousands of automations simultaneously"; RBAC, encryption, audit trails (security FAQ section).
- **Operating model:** non-technical workers configure automations without coding; **Center of Excellence (CoE)** for standards/governance "across the automation life cycle"; CoE Manager product for oversight and ROI.
- **Known limitations (vendor-acknowledged):** "RPA can only operate effectively with **structured data**" (unstructured handled by AI add-ons); "business applications advance and evolve in ways that **disrupt rigid, rules-based RPA**"; maintenance is a named challenge; vendor sells "self-repairing, reusable automations that **adapt to application UI changes**" (Automator AI).
- **Agent boundary (vendor's own words):** "What differentiates RPA from AI agents? RPA quickly and reliably automates rules-based digital tasks… AI agents… work autonomously to achieve defined goals… **AI agents rely on RPA to provide the execution layer** that performs tasks quickly and accurately at scale."
- NOT evidenced (docs portal unreachable): Control Room terminology, Bot Creator/Bot Runner roles, work-queue mechanics, credential vault, bot lifecycle states. None of these are asserted anywhere in this pass.

---

## Cross-product Comparison

| Dimension | UiPath (A) | Blue Prism (A) | Power Automate (A) | Automation Anywhere (T2) |
|---|---|---|---|---|
| Automation artifact | Process / project in Studio (activities, sequences) | **Process** + **Object** (two artifact classes) | Desktop flow (+ cloud flow as trigger wrapper) | bot / automation in Automation Workspace |
| Authoring | drag-drop activities; indicate-on-target UI selection; variables; local run/debug | drag-drop flow; publish; version history; permission groups | drag-drop actions + **recorder** | low-code; non-technical users; citizen developers |
| Target surface | applications via UI (indicate app/browser; text/type/scrape) | applications (via process/object design) | UI elements, **images, coordinates**; terminal emulators, web, desktop, Excel | digital tasks across enterprise apps incl. legacy |
| Central control plane | Orchestrator (+ Automation Ops governance) | **Control Room** | Power Automate portal (Monitor > Machines) + cloud flows | Mozart Orchestrator (named only) |
| Executor | Robot (attended/unattended); serverless/VM cloud robots | **Resource** = "human, or more commonly, machine" | registered **Machine** + unattended bots | (not evidenced) |
| Execution instance | Job; queue item → **transaction** | **Session** (Pending / Running / Completed) | desktop-flow run (queued/running counts) | (not evidenced) |
| Triggers | schedules, queue triggers, (events) | manual session creation in Control Room (scheduling not fetched) | cloud-flow **events, schedules, buttons** | "pre-programmed triggers, data inputs, and schedules" |
| Attended/unattended | both (Assistant + serverless/VM unattended robots) | both (human-or-machine resource framing) | both, explicitly licensed/plan-gated | both, explicit categories |
| Item-level work distribution | **Queues**/transactions: statuses, deadlines, priority, reviewers, retries, SLA machinery | Work queues (known feature; page not reachable — NOT asserted here) | runs queue on machines; work-queue page unreachable | (not evidenced) |
| Exception handling | application vs **business exception**; reviewer assignment; retry of failed/abandoned | stop semantics (immediate vs requested clean stop) | maintenance mode; queued-run handling; locked-session recommendations | "Where RPA flags an exception… AI steps in" (generic) |
| Governance | roles/permissions; audit history; Automation Ops | role-gated permissions; audit (groups) | security roles; sharing permissions; environments | RBAC, audit trail, CoE model |
| Scale machinery | elastic robot orchestration (auto-scale unattended fleets on AWS/GCP/Azure) | enterprise deployment; dual-license Desktop vs Enterprise tiers | machine groups; capacity-based unattended bots | "thousands of automations simultaneously" |
| AI posture | Healing Agent (self-healing targeting), Document Understanding, Agents + Maestro orchestration | AI Gateway, Document Automation, Decipher IDP, Process Intelligence | (desktop-flow docs: deterministic core) | agents call RPA as "execution layer"; self-repairing automations |

**Reading:** all four products implement the same skeleton — an authored deterministic automation operating the organization's applications at user-facing surfaces, published into a central control plane that runs it on managed machines as monitored executions under organizational governance. Differences are of packaging (standalone suite vs platform-embedded), authoring audience (professional vs citizen), deployment (cloud vs self-hosted), and how much item-level distribution and exception machinery is exposed.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately minimal)

1. **The robot: an authored, deterministic, reusable automation program.** A human-designed sequence of steps with condition-based branches ("taking pre-developed actions and making decisions based on their outcomes" — BP), fixed at authoring time; the runtime executes what was authored, it does not decide. Shared with desktop automation; this is the mechanism-family invariant.
2. **Surface-level operation of existing applications.** The automation operates the organization's existing business applications through the same surfaces a human operator uses — canonically application UIs (windows, controls, screens, browser pages; terminal screens; interaction by UI elements, images, or coordinates — PA), not by modifying or rebuilding those applications. This is what makes RPA "robotic process" automation of business systems rather than integration engineering.
3. **Managed as an organizational machine workforce.** The platform (not the end user) owns the operating layer: automations are published/versioned from the design environment into a central control plane; machines/robot identities are registered to the platform; executions are triggered (schedules, events, queue items, human start), assigned to machines, tracked as stateful runs, and governed by organizational roles/permissions/audit. The removal test: strip this layer and the product is a Desktop Automation Application; make this layer the product's center and it is an RPA Platform.

All three required. Remove (1) → not an automation product; remove (2) → BPM/integration/build tooling; remove (3) → desktop automation; let a model decide actions at runtime → agent / computer-use platform.

### L1 — Common Mature Structure

- Design studio (visual flow construction dominant; recorder as a common authoring aid; targeting machinery: selectors/indication, images, coordinates).
- Central control plane with machine/fleet views, run/session monitoring with states, dashboards, audit.
- Machine registration and grouping; environment/workspace scoping.
- Attended and unattended execution modes (with capacity/licensing models around unattended robots).
- Trigger set: schedules, events, human-initiated runs (attended), queue-driven starts.
- Item-level work queues with statuses, retries, deadline/priority ordering, and exception review (documented directly by UiPath; the machinery's presence across mature platforms is market-typical but only one sampled product's docs were reachable on this).
- Exception taxonomy distinguishing data/business failures from automation-environment failures (formally documented by UiPath; AA acknowledges exception handling generically).
- Roles: automation developer, operations/admin, business analyst, plus governance (CoE) and citizen-developer enablement.
- Versioning of automations; publishing from design to control environment.

### L2 — Variant / Optional Structure

- Packaging: standalone enterprise platform vs embedded in a broader platform (Power Automate in Power Platform; ecosystem RPA in ServiceNow/Salesforce/SAP per AA's market page); light desktop-licensed tier (Blue Prism Desktop).
- Deployment: SaaS cloud vs self-hosted/on-prem vs hybrid (UiPath Automation Cloud vs Automation Suite; BP Enterprise vs BP Cloud; AA Cloud Service / VPC execution).
- Authoring audience: professional developer (Studio/Process Studio) vs business-user designer (StudioX, citizen-developer programs).
- AI extensions: document understanding/IDP, AI-assisted authoring, self-healing selectors, AI agents and agentic orchestration layers that call RPA as execution machinery (Maestro, Mozart, AI Agent Studio) — variant layer that does not change the deterministic core.
- Process discovery / task mining companions (adjacent Types; bundled by vendors).
- Scale machinery: elastic cloud robot provisioning, SLA prediction tooling, high-availability deployment.
- Industry operating models: CoE governance, automation pipelines (idea → assessment → build → run).

### L3 — Vendor-specific (research notes only)

- UiPath: Orchestrator queue SLA predictions & Risk SLA (30-minute alert cadence; High-priority side effects), JSON-schema validation of queue items, 256,000-character Specific-Data limit, `IsStopRequested()`-style flags (UiPath wording differs), serverless vs VM cloud robots, Automation Ops, Action Center, Maestro Case/Flow, Healing Agent, Studio compatibility/language options (Windows/VB), project name limits.
- Blue Prism: dual-license Desktop-vs-Enterprise resource typing and iconography, backward-compatibility warnings when editing across runtime versions, Hub/Interact web frontends, WorkHQ next-gen platform, Capture/Process Intelligence/Decipher IDP companion products.
- Power Automate: machine-runtime app, direct-connectivity version floor (2.8.73.21119), Windows-Home exclusion, 50-machine group limit, 12-hour queueing limit, Environment-Maker / Desktop-Flows-Machine-Owner/User roles, maintenance-mode red pictogram, Automation Center recommendations (10-minute window), gateway deprecation.
- Automation Anywhere: Mozart Orchestrator, Process Reasoning Engine, AI Agent Studio, Automation Co-Pilot, CoE Manager, Community Edition, Gartner/IDC positioning claims, customer ROI figures.

## Vendor-specific Findings

See L3. Two structural observations worth keeping:

- PAD/Power Automate's own intro sentence ("desktop flows broaden the existing RPA capabilities") plus Blue Prism shipping a separate light "Desktop" product confirm the market itself frames personal desktop automation and enterprise RPA as two layers of one stack — supporting the L0 boundary rather than eroding it.
- Blue Prism's definition of a resource as "human, or more commonly, machine" shows the RPA platform vocabulary admits human executors; in practice the machine executor is the defining case and human routing belongs to orchestration/BPM layers.

## Rejected Findings

- "RPA is defined by record-and-replay" — rejected: recording is one authoring aid; Blue Prism and UiPath's core authoring is constructive (drag-drop flows with targeting), and AA markets non-technical low-code building without recorder-first claims.
- "RPA is defined by screen scraping" — rejected: targeting mechanisms span UI elements/selectors, images, coordinates, and terminal sessions; scraping is a legacy mechanism among several.
- "RPA requires unattended execution" — rejected: attended-only deployments remain fully RPA; attended/unattended is a posture dimension (AA's own category taxonomy), and the desktop-automation pass showed the unattended/fleet layer is what turns the *local* tool into the *platform* Type.
- "RPA is defined by a visual low-code designer" — rejected: the invariant is the authored deterministic automation, not the authoring surface; designer form varies (professional vs citizen vs recorded).
- "Modern RPA decides actions with AI at runtime" — rejected: sampled products keep the bot deterministic; AI appears as authoring aid, callable processing step, or a separate agent layer that *calls* RPA. Model-decided runtime action is the neighboring agent/computer-use Type.
- "Work queues are definitional" — held as L1 not L0: directly evidenced only by UiPath this pass; an RPA platform conceptually runs triggered automations without item-level queues (early/historical RPA did), so queues are common mature machinery, not the defining structure.

## Boundary Findings

1. **vs Desktop Automation Application (§03.16) — FLAG DISCHARGED (joint review completed from the RPA side).** Same mechanism family (human-designed deterministic automations). The discriminator recorded from the desktop side — ownership and scale — is confirmed: RPA's L0 centers the *managed estate* (publish → central control plane → registered machines/robot identities → triggered, monitored, governed executions), while desktop automation keeps authoring and execution local and user-owned. Power Automate reconfirms the bridge-product analysis from this side: its desktop-flow authoring layer is desktop-automation machinery; machine registration, machine groups, unattended bots, capacity, monitoring and security roles are the RPA layer, and Microsoft's own docs frame desktop flows as "broadening the existing RPA capabilities". Removal tests hold both ways (strip fleet management → desktop automation; make the fleet the product's center → RPA). No merge; boundary is structural, not vendor-level.
2. **vs Agent Tool / Computer-use Platform (§13) — FLAG DISCHARGED (RPA half of the open flag).** The runtime decision-maker discriminates: RPA executes human-designed deterministic sequences fixed at authoring time; the agent Type has a model deciding each action from live observations. Confirmed in-sample: UiPath ships Agents/Maestro as a *separate* agentic layer whose docs describe orchestrating "AI agents, automations, and people" — automations remain a distinct orchestrated instrument; Automation Anywhere's own FAQ draws the same line ("AI agents rely on RPA to provide the execution layer"); AI features inside RPA products (Healing Agent, Automator AI) act on authoring/resilience, not on runtime task decisions. Both vendors police the boundary in their own docs. The agentic-orchestration drift (platform suites bundling both mechanisms) mirrors the Copilot Studio observation from the agent pass: mechanism-level boundary, not vendor-level.
3. **vs Business Process Management Platform / Workflow Management Platform (§10 siblings).** BPM orchestrates end-to-end process flows across human tasks and system steps; RPA executes the machine-performed steps at application surfaces. Evidence: Blue Prism's resource concept ("human, or more commonly, machine") shows the RPA platform managing the *machine* performer; AA positions agents/BPM as orchestrators that call RPA. They compose (BPM/RPA interlocks are standard); the boundary is what executes the step vs what sequences the process. Distinct Types.
4. **vs Test Automation Platform (§12).** Same GUI-driving machinery (record, target, replay); different job — doing the organization's production work vs asserting expected behavior of software under test. UiPath itself ships Test Cloud/Test Manager as a separate product line — vendor-policed boundary. Distinct Types; boundary is the job.
5. **vs ETL / Data Integration Platforms / Managed File Transfer (§13).** Data-centric movement between systems vs surface-level operation of applications. AA lists "transferring data between applications" among RPA tasks — the *outcome* can overlap, the *mechanism* (operating the application surface as a user would) does not. Distinct Types; watch RPA products' API-step extensions as a gray zone (marked L2).
6. **vs Low-code Application Platform / No-code Application Builder (§12).** Building new applications vs automating the operation of existing ones. Distinct Types despite adjacent low-code authoring machinery.
7. **vs Process Mining / Task Mining (§10/§13 siblings).** Discovery/analysis of processes vs execution of automations. Vendors bundle them (UiPath Process Mining/Task Mining, BP Capture/Process Intelligence, AA Process Discovery) — packaging, not identity. Distinct Types.
8. **vs Personal Workflow Automation Platform / No-code Personal Automation Application (§03.16 siblings, unprocessed).** Consistent with the desktop pass's surface test: those Types orchestrate cloud-service-to-cloud-service events for personal use; RPA operates organizational application estates with fleet machinery. Joint review remains with the sibling passes; no conflict expected.

## Historical / Market-Sample Check (per §24)

- Would older products fit? The vendor-attributed origin lineage (1990s keystroke macros → modern RPA) passes through two generations: (a) local macro/screen-scraping automation — which fails L0-3 and is therefore *desktop-automation*-class, correctly excluded; (b) the RPA generation proper (Blue Prism early-2000s onward, enterprise "digital workforce" framing) — authored UI-level automations + central control/management, satisfying all three L0 elements. The definition excludes RPA's precursors by the same element that distinguishes the Type from desktop automation today — a sign the cut is at the right joint.
- Regional / platform skew: all sampled desktop-execution surfaces are Windows-centric (a market reality of enterprise desktop estates), but the definition nowhere requires Windows; cloud/serverless robot hosting (UiPath elastic) and cross-platform web authoring (Studio Web) already stretch it. No platform element entered the definition.
- Modern skew check: nothing in L0 requires cloud delivery, elastic scaling, AI, queues, SLA tooling, recorders, or citizen-developer programs — all are L1/L2. The definition does not overfit the 2020s AI-era positioning (AA markets "APA" as the successor category; the RPA product line beneath it still satisfies the L0 exactly as before).
- Check conclusion: definition survives the historical and market-sample check.

## Uncertainties

1. Automation Anywhere operational documentation unreachable (JS-only portal, 2 attempts). All AA-specific mechanics (control-room terms, bot roles, work queues, vaults) unverified; AA contributes Tier-2-level corroboration only (attended/unattended taxonomy, CoE model, rules-based character, agent-boundary statements).
2. UiPath Orchestrator overview page unreachable (404 ×3 URL variants); Orchestrator UI specifics (deployment pages, job views) not asserted; control-plane claims rest on the queues page, elastic-orchestration page, and product map.
3. Work-queue machinery beyond UiPath (BP guide page 404; PA page 404 ×2): queues are written as "common mature machinery" with moderate strength, UiPath as the directly documented instance.
4. Credential/vault machinery: universally expected in this market but not directly evidenced in any fetched page this pass; deliberately omitted from standard-capability claims and noted here.
5. Open-source / developer-centric pole (Robot Framework, Robocorp) not researched; packaging-variant claims exclude it.
6. Blue Prism scheduling machinery (schedules/triggers in Enterprise) not fetched; trigger claims rely on PA/UiPath/AA evidence.
7. Licensing shapes (per-bot, per-capacity, per-user) are only qualitatively evidenced (PA capacity allocation; UiPath elastic controls); no numeric or pricing claims made in the final document.

## Final Synthesis

A Robotic Process Automation Platform is the organizational layer above automation authoring: it lets people build deterministic software robots that operate the company's existing applications the way a human operator would (through their user-facing surfaces), and it runs those robots as a centrally governed machine workforce — published into a control plane, deployed onto registered machines, triggered by schedules/events/queues/human requests, executed as stateful monitored runs, and maintained under organizational roles, permissions and audit. The defining core is exactly three elements: authored deterministic automation; surface-level operation of existing applications; management as an organizational machine workforce. Attended/unattended postures, queues, elastic fleets, AI assistance and agentic orchestration layers are common or variant structures, not definitions. The Type sits between Desktop Automation (same mechanism, personal scale), agent/computer-use platforms (same surface, model-decided runtime), BPM (process orchestration vs step execution), test automation (same machinery, different job), and integration platforms (data-level vs surface-level) — with all four sampled products, and their own documentation, policing these seams in the same places.
