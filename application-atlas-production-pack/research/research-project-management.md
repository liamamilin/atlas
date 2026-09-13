# Research Notes — Research Project Management

Research date: 2026-09-09
Slug: research-project-management
Directory leaf: Research Project Management (§23 Education, Research & Knowledge Institutions)

## Research Goal

Determine what "Research Project Management" is as an Application Type: whether it is a distinct Type (coordination of research work as the primary job), a Variant of the generic Project Management Application, or merely a capability of Electronic Lab Notebooks / R&D platforms. Extract the smallest defining structure, the common mature structure, and the boundary seams against neighboring Types (ELN, generic PM, Research Grant Management/Administration, CRIS, Research Data Management, Research LIMS, CTMS).

## Initial Boundary (hypothesis before research)

- Core use hypothesis: coordinating the execution of research projects — planning work, assigning people, tracking experiments/studies against milestones and timelines.
- Users hypothesis: research teams — PI / lab head, postdocs / PhD students / research scientists, project/coordinator roles in R&D organizations.
- Neighbors: Project Management Application (generic), Electronic Lab Notebook, Research Administration Platform / Research Grant Management, Research Information Management / CRIS, Research Data Management, Research LIMS, Clinical Trial Management System.
- Main unknowns:
  1. Is there a distinct product population whose primary surface is coordination, or is RPM only a layer inside ELN/R&D platforms?
  2. What exactly makes the work items "research-shaped" — is that definitional or incidental?
  3. Does the academic (non-lab) pole realize RPM differently?

## Research Questions

1. What is the unit of record — what does a "research project" carry (aims, team, timeline, funding context)?
2. What work objects get coordinated (experiments, studies, tasks, deliverables)? What content do they carry (protocol steps, results, sample links)?
3. How does work flow: plan → assign → execute → record → review → report?
4. What coordination surfaces exist (dashboards, workload views, due-date tracking, bottleneck detection)?
5. What roles exist and how do they differ (PI, project lead, researcher, lab manager, QA)?
6. How do projects relate to research content systems (protocols, inventory/samples, data, reports)?
7. Where is the seam to generic PM (work-item content?), to ELN (coordination vs documentation?), to grant administration (team-side vs institution-side)?
8. Historical check: would paper-era research project management satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| SciNote | ELN-rooted platform with an explicit "Scientific Project Management" layer; academic + industry, freemium | Deep sample (site + knowledge base reachable) |
| Labguru | "Lab management software" platform (ELN + LIMS + inventory + automation); biotech/pharma mid-market | Deep-ish sample (site reachable; support center unreachable) |
| Benchling | Enterprise R&D cloud (notebook + registry + workflows + requests + insights); large biopharma | Deep sample (site + help center reachable; article pages 403) |
| LabArchives | Academic ELN (documentation-first), university-deployed | Boundary pole (ELN side) |
| RSpace (Research Space) | Open-source FAIR research data management / infrastructure orchestration | Boundary pole (RDM side) |

Rejected / unavailable during sampling:
- **Colabra** — previously marketed as "the research management platform for R&D teams"; live site on 2026-09-09 shows a pivoted product (AI workspace for M&A due diligence). Dropped; pivot recorded as market evidence that the standalone research-ops/PM startup niche is thin.
- **Riffyn (Riffyn Nexus, R&D process management)** — domain now serves unrelated content; product defunct/unreachable. Dropped.
- **eLabFTW** — main site and docs both unreachable (transport errors ×2 each). Dropped; limitation recorded.

## Sources

Layer A (directly observed, official):

- SciNote — https://www.scinote.net/ (homepage), https://www.scinote.net/product/scientific-project-management/ (Project Insights page), https://knowledgebase.scinote.net/en/knowledge/what-are-project-insights-in-scinote, https://knowledgebase.scinote.net/en/knowledge/using-scinote (KB section index)
- Labguru — https://www.labguru.com/ (homepage), https://www.labguru.com/eln (ELN page); support.labguru.com unreachable (transport error)
- Benchling — https://www.benchling.com/ (homepage), https://www.benchling.com/bioresearch (product page + FAQ), https://help.benchling.com/hc/en-us (help center), help-center search results and section pages for "Benchling Task Management" / "Workflows" / "Requests" (article pages return 403 to fetch; structure inferred from titles, section taxonomy, and search snippets)
- LabArchives — https://www.labarchives.com/ (homepage)
- RSpace — https://www.researchspace.com/ (homepage)

Layer C (canonical inference) is built from the cross-product comparison below.

## Product Observations

### SciNote (evidence layer A)

Positioning: "Electronic Lab Notebook & Lab Inventory Management Software"; also ships a dedicated "Scientific Project Management" page whose product surface is the "Project Insights" dashboard.

Structure (homepage + KB):
- "SciNote adopts a projects / experiments / tasks structure that emulates how research happens."
- KB taxonomy: Protocols / Experiments / Tasks and workflows / Inventory — the coordination objects are first-class KB sections.
- Hierarchy: workspace (team) → projects (organized in project folders) → experiments → tasks.

Tasks (KB articles):
- assigned users ("How to Assign Users to Tasks"; multiple assignees counted per user in workload charts)
- status ("How to Update a Task Status on the App?"; statuses feed Status Overview; "the final status (depending on your Task workflow)" implies configurable task workflows; "How to Edit Workflows?")
- due dates (Tasks Due widget: Overdue / Today / Tomorrow / This Week / Next Week)
- protocol steps loaded from protocol templates, checkable off ("check off protocol steps"); locked protocols; protocol versions
- results (templates for results; link protocol steps to results)
- inventory items assigned to tasks with snapshots; stock consumption recorded per task ("Only consumption records of type 'Task' are counted")
- comments, tags, scheduled events, sharing with outside colleagues, archiving, moving between projects/experiments, favorites

Experiments: containers of tasks; sortable; movable between projects; archivable.

Projects: shareable with collaborators; project folders; customizable table views; access control ("available to all roles with project-level access"); active vs archived.

Project Insights dashboard (KB, detailed):
- widgets: Status Overview (tasks/experiments pie), Team Workload (stacked bars per assignee), Tasks Due (urgency tabs), Item Consumption (inventory usage per project, exportable), Bottlenecks (tasks with no updates in 7/14/30 days; Not-Started and final-status tasks excluded)
- filters: project (multi-select incl. folders), experiment, status, assignee; date range
- click-through from charts to filtered task lists; direct task editing with permission
- available on Professional/Platinum plans (plan gating = vendor detail)

Roles (marketing page): Lab Managers (monitor multiple workflows), Project Leads & Coordinators ("plan timelines, resources, and milestones"), QA/Compliance personnel, PIs ("oversee progress across collaborative projects").

Use cases (marketing page): pharma R&D (stability studies, "IND timeline tracking, GxP readiness"), diagnostic labs (workflow stages, technician capacity, reassignment), CROs ("task progression across sponsors or studies", "deliverables tied to specific milestones", sponsor updates).

Reporting: "auto-generated project reports"; "You will always know what was done, when, how, by whom and which results were generated."

### Labguru (evidence layer A; support center unreachable — thinner)

Positioning: "AI-Powered Lab Management Software"; platform = ELN + LIMS + inventory + automation + informatics.

ELN page:
- "Organize your information by projects and folders"
- "Create shared experiments and tasks to work together with teammates"
- "Manage your projects & set goals. Set goals, assign tasks to team member, and track research progress anytime and anywhere."
- comments/discussion on any item page; internal chat/video linked to projects and experiments; shared protocol/SOP database; sharing with internal and external collaborators

Requests module (ELN page):
- "submit, track, and manage requests" with unified templates
- "Real-time updates on request status and assignments"
- "Prioritize and schedule testing based on urgency and deadlines" (resource allocation)
- explicitly framed as helping "decision-making and project management"

Other: dashboards ("Data visualization & insights"), inventory integrated with experiments, equipment management, automation (triggers/rules/workflows), 21 CFR Part 11 signing/witnessing.

### Benchling (evidence layer A; article bodies 403 — structure from section taxonomy + snippets)

Positioning: "Cloud-based platform for biotech R&D"; Bioresearch = "a shared space to design and manage experiments, complex biomolecules, workflows, and results end-to-end."

FAQ (bioresearch page) — directly on point, quoting: "What are the best tools for collaborative biotech research project management? Bioresearch is purpose-built for multi-team R&D, with shared notebook entries, real-time co-editing, workflow task assignments, and registry access across the organization. The Requests feature makes it easy to initiate and track work across teams, with structured submission forms and real-time execution tracking built on top of those workflow tasks."

Workflow management (product page): "Drag-and-drop tasks in an easy-to-use flowchart to map activities from simple tasks like making a request, through complex process dependencies."

Task Management help-center section (taxonomy + snippets):
- subsections: Workflows, Requests
- concepts: Workflow (flowchart), Task Group ("a collection of related tasks generated from a single task schema"), Task ("an individual..." unit; has states incl. "terminal state", archived; outputs submitted from task details)
- Requests: "Tasks created via a request appear in the Workflows dashboard as standard tasks. Fulfillers can reference..." — requesters submit structured forms; fulfillers execute; configurable task-creation interface tied to task schemas
- failure/cancellation semantics exist ("Why are my workflow tasks failing?", downstream task dependencies, automatic cancellation of root tasks)

Projects (help center): top-level containers with project-level permissions; project folders hold notebook entries / registry entities / inventory; project ownership transfer; archiving (blocked by unarchived inventory items).

Insights: "Operational insights — build dashboards and share reports that track metrics"; "Unblock organizational bottlenecks with real-time dashboards."

Notebook: entries from templates, real-time co-editing, structured result schemas, linked to registered entities (samples, cell lines, plasmids) and inventory.

### LabArchives (evidence layer A — boundary pole)

Positioning: "The Modern Electronic Lab Notebook (ELN)" — "All Your Research in One ELN". Products: ELN for Research, Inventory, Scheduler, ELN for Education, Government (FedRAMP).
Primary jobs: record/organize/search/share scientific data; notebook pages with entries; real-time collaboration on pages; integrations (SnapGene, Prism, Microsoft).
No project/task coordination layer surfaced on the product surface: organization is notebook/page-centric; Scheduler covers equipment/room booking, not work coordination. → documentation-first pole; the coordination loop is absent or marginal.

### RSpace (evidence layer A — boundary pole)

Positioning: "open source research data management" / "Orchestrating research workflows into FAIR ecosystems and infrastructures". Products: Infrastructure Orchestration, ELN, Sample Management, Instrument Management, File Management.
Emphasis: FAIR metadata, PIDs (ORCID, IGSN, PIDINST, RAiD, ROR, DataCite), institutional storage integration, research integrity.
Coordination layer not primary; organization is document/sample/data-centric. → RDM pole.

## Cross-product Comparison

| Structure | SciNote | Labguru | Benchling | LabArchives | RSpace |
|---|---|---|---|---|---|
| Project as container with members/permissions/folders/archive | ✓ (project folders, sharing, roles, archive) | ✓ (projects and folders) | ✓ (project-level permissions, ownership, archive) | notebook-centric (no project container surfaced) | document/sample-centric |
| Research-shaped work items (experiments/tasks carrying procedure, results, sample links) | ✓ (experiments → tasks; protocol steps; results; inventory snapshots) | ✓ (experiments and tasks; goals; inventory linked) | ✓ (notebook entries + workflow tasks; schemas; registry/inventory links) | ✗ (pages/entries, documentation) | ✗ (documents/samples) |
| Assignment + status + due-date tracking | ✓ (assignees, statuses, task workflows, due dates) | ✓ ("assign tasks... track research progress") | ✓ (workflow task assignments, execution tracking, task states) | ✗ | ✗ |
| Progress visibility surface (dashboard) | ✓ (Project Insights: status, workload, due, bottlenecks, consumption) | ✓ (dashboards/insights) | ✓ (operational insights, real-time dashboards) | ✗ | ✗ |
| Cross-team/cross-org work requests | ✓ (share tasks with outside colleagues; comments/notifications) | ✓ (Requests module) | ✓ (Requests → tasks) | ✗ | ✗ |
| Protocol/procedure templates instantiated into work | ✓ (protocol templates → task protocols) | ✓ (shared protocol/SOP database; protocol converter) | ✓ (entry templates; workflow schemas) | ✓ (templates as content) | ✓ (template management) |
| Inventory/sample linkage with consumption | ✓ (per-task consumption records) | ✓ (inventory integrated) | ✓ (registry/inventory linked to entries) | separate Inventory product | ✓ (sample management) |
| Reporting | ✓ (auto-generated project reports) | ✓ (reports/datasets) | ✓ (dashboards/reports) | export | export/RO-Crate |
| Milestones/deliverables | ✓ (Project Leads "plan timelines, resources, and milestones"; CRO deliverables tied to milestones) | goals (weaker evidence) | marketing-level only ("reach milestones faster") | ✗ | ✗ |
| Compliance machinery (GxP / Part 11) | ✓ (optional module set) | ✓ | ✓ (Validated Cloud) | ✓ (Part 11, FedRAMP) | compliance page |

Reading:
- Structures 1–5 co-occur in all three coordination-capable samples and are absent in both documentation-first poles → candidate defining core (with the seam being the research-shaped work item + the coordination loop).
- Structures 6–9 are common mature structure (present in most coordination-capable products, but a documentation tool can satisfy 6–7 without being RPM).
- Compliance machinery varies by segment → variant, not definitional.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The research project as the unit of record** — a persistent, identified container organizing a body of research work: its aims/work content, its team (members with roles/permissions), and its progress over time. Remove → folder organization / loose task lists; no project memory.
2. **Research-shaped work items as the coordinated objects** — the units of work are research work (experiments, studies, analyses, tasks) carrying research content: procedure/protocol structure, recorded results, and links to research materials (samples, inventory, instruments, data). Remove → generic Project Management Application (projects + generic tasks).
3. **The coordination loop over those items** — work is planned and assigned, executed and recorded, tracked by status/dates/workload, reviewed for progress and blockers, and reported. The management layer answers "what's moving, what's stuck, who's loaded, what's next". Remove → an ELN / documentation space with project folders (records without management).

Jointly-held load-bearing tests:
- 1 alone = folder/organization structure (ELN organization, drive folders)
- 2 alone = ELN / experiment documentation
- 3 alone = generic project management
- 1+3 without 2 = generic PM with research-branded containers
- 2+3 without 1 = loose experiment/task tracker with no project memory
- 1+2 without 3 = documented research organized by project, but unmanaged

### L1 — Common Mature Structure

- progress dashboard (status, workload distribution, due/overdue tracking, bottleneck/stall detection)
- cross-team / external work requests (structured submission → tracked execution)
- protocol/procedure templates instantiated into work items
- inventory/sample linkage with usage/consumption recorded against work
- project reporting (auto-generated reports, exports)
- comments, notifications, tags, activity history on work items
- role differentiation: PI / lab head, project lead / coordinator, researcher, lab manager, QA/compliance (regulated segments)
- milestone / deliverable tracking (moderate evidence: explicit in SciNote's positioning and CRO use case; weaker elsewhere)

### L2 — Variant / Optional Structure

- compliance machinery: GxP/GLP, 21 CFR Part 11, e-signatures, audit trails (regulated pharma/CRO/diagnostics segments)
- automation (trigger/rules-based workflows, lab scripting)
- equipment/instrument scheduling and booking
- mobile app execution (check off steps, update status in the lab)
- AI assistance (protocol import, data query) — era-current
- deployment: cloud / on-prem / government-authorized environments; free academic tiers
- ELN integration depth: full notebook inside the same product vs links out to documentation systems
- domain flavor: wet-lab life sciences (dominant in sample) vs other research domains (observational, computational, social) — the invariant is domain-neutral; wet-lab vocabulary (protocols, reagents) is the dominant implementation, not the definition

### L3 — Vendor-specific (research notes only)

- SciNote: "Project Insights" widget set and its exact thresholds (7/14/30-day inactivity), plan gating (Professional/Platinum), "Quick Start" buttons, FLUICS/Zebra label printer integrations
- Benchling: "Task Group" concept, Workflows flowchart schemas, Requests configuration tied to task schemas, automatic cancellation semantics for root tasks, "Validated Cloud"
- Labguru: Requests module naming, "Lab Scripter", Protocol Converter, label system
- LabArchives: Course Manager, Scheduler product, FedRAMP/GovRAMP packaging
- RSpace: PID integrations (IGSN, RAiD, PIDINST), RO-Crate export, infrastructure orchestration framing

## Vendor-specific Findings

See L3. None of these entered the canonical model. The strongest candidate for accidental promotion was Benchling's Task Group / Workflows schema machinery — rejected because SciNote realizes the same need with simpler task workflows and Labguru with requests/automation; the invariant is "work items are schema/template-shaped and tracked", not any specific machinery.

## Rejected Findings

- "RPM = ELN feature" — rejected: the coordination loop (assignment, status/due tracking, workload/bottleneck views, requests) is absent in documentation-first ELN poles (LabArchives, RSpace) and is the primary surface in the coordination-capable samples. ELN integration is common but not definitional.
- "RPM = generic PM applied to research" — rejected: in all three coordination-capable samples the coordinated work items carry research content (protocol steps, results, sample/inventory links) and bind to research materials; this is the seam against generic PM.
- "Milestones are definitional" — rejected as L0: explicit milestone evidence is strong in only one sample (SciNote) and marketing-level in another; kept in L1 with moderate wording.
- "RPM is wet-lab-only" — rejected: the sampled products are life-science-heavy, but the defining structure (project container + research work items + coordination loop) is domain-neutral; wet-lab vocabulary is the dominant implementation.
- "Standalone research-PM products define the Type" — rejected by market evidence: the observed standalone niche is thin (Colabra pivot; Riffyn defunct; eLabFTW unreachable is an ELN anyway). The Type is realized predominantly as the coordination layer of research platforms. This is a market-structure finding, not a reason to deny the Type.

## Boundary Findings

| Neighboring Type | Seam | Remove-what test |
|---|---|---|
| Project Management Application (generic) | work-item content: research work items carry procedure/results/sample linkage vs generic to-dos | remove research-shaped work items → generic PM |
| Electronic Lab Notebook / ELN | primary job: coordination vs documentation of experiments | remove the coordination loop → ELN (LabArchives pole) |
| Research Grant Management / Research Administration Platform | actor + object: team-side work execution vs institution-side money administration (proposals, awards, sponsor compliance) | replace the team's work items with the institution's award records → grant management |
| Research Information Management / CRIS | purpose: working management of live projects vs the institution's record of research activity/outputs/people | replace live coordination with attributed institutional records → CRIS |
| Research Data Management | object: work coordination vs data stewardship/publication (FAIR, repositories, PIDs) | replace work items with datasets/data plans → RDM (RSpace pole) |
| Research LIMS | center of gravity: project/work coordination vs sample-centric lab operations | make samples the unit of record → LIMS territory |
| Clinical Trial Management System / CTMS | regulated clinical-trial machinery (subjects, visits, regulatory milestones) is its own Type | protocol-driven subject-facing trials → CTMS |
| Professional Services Automation | similar coordination skeleton, but billable client work and economics vs research work | billable client engagements → PSA |

Taxonomy observations (for STATUS.md Boundary Issues):
1. The market center of gravity for this Type is R&D organizations (biotech/pharma/industrial labs), while the directory places the leaf in §23 (Education, Research & Knowledge Institutions). The Type definition holds for both; the placement is acceptable but the population is broader than the section name suggests.
2. The Type is realized predominantly as the coordination layer inside research platforms (ELN/LIMS/R&D clouds) rather than as standalone products. It remains a distinct Type by the primary-job test, but a reader should expect product overlap with ELN leaves. The ELN↔RPM seam (coordination vs documentation) should be respected when the ELN leaves are processed.

## Uncertainties

- Labguru's support center was unreachable; its project/milestone internals (e.g., whether projects carry explicit milestone objects) could not be verified. Labguru evidence is limited to marketing/product pages; claims from Labguru are kept weaker.
- Benchling help-center article bodies return 403 to the fetcher; workflow/task semantics were assembled from section taxonomy, search snippets, and the product page FAQ. Precise task-state names are deliberately not claimed.
- eLabFTW (open-source academic ELN with projects/experiments/status) could not be reached; the open-source/academic pole is therefore under-sampled. The academic non-lab pole (research teams using generic PM tools) was not directly researched and is only used as a boundary inference, not as evidence.
- Milestone/deliverable tracking: common-plausible but only strongly evidenced in one sample; kept out of the defining core.
- Whether any product exists that is pure coordination (no documentation layer at all) could not be confirmed; all observed coordination-capable products bundle documentation. The definition does not require documentation, but the market may always bundle it.

## Historical / Market-Sample Check

Before freezing the defining core, ask whether older, regional, platform-native, or differently positioned products would still fit:

- **Paper-era research project management** (grant proposal with aims and timeline, paper lab notebook, team meetings, task assignment at the bench, progress reports to the PI/funder): all three defining structures hold — the funded project as container, research work items (experiments recorded in notebooks, tasks assigned to people), and the coordination loop (plans, meetings, reports). Modern machinery (dashboards, cloud, requests) is not required.
- **Non-wet-lab research** (observational campaigns, computational studies, social science fieldwork): the defining structure is domain-neutral; protocol/reagent vocabulary is the dominant market implementation, not the definition. The work items remain research-shaped (studies, analyses, campaigns with procedure and recorded outcomes).
- **Platform-native / open-source academic tools** (e.g., open-source ELNs with project/experiment/status structures): would satisfy the core via their project containers and status-tracked experiments, though their coordination loop is thinner — they sit near the ELN seam. (eLabFTW could not be fetched; this check is inferential and recorded as an uncertainty.)
- **Generic PM tools used by research teams**: satisfy the container and the loop but not the research-shaped work items — confirming that the work-item content seam, not the vocabulary, is what separates the Types.

The definition survives the check; no further abstraction was needed.

## Final Synthesis

Research Project Management is the team-side coordination system for research work. Its defining core is three jointly-held structures: the research project as the unit of record (persistent container for a body of research work, its team, and its progress); research-shaped work items as the coordinated objects (experiments/studies/tasks carrying procedure, results, and links to samples/materials/data); and the coordination loop (plan/assign → execute/record → track status/dates/workload → review → report). Remove the research-shaped work items and it collapses into generic project management; remove the coordination loop and it collapses into an ELN; remove the project container and it collapses into loose trackers. Mature products commonly add progress dashboards, cross-team requests, protocol templates, inventory/sample linkage, reporting, and (in regulated segments) compliance machinery. The market realizes the Type predominantly as the coordination layer of research platforms (ELN/LIMS/R&D clouds) spanning academic and industry R&D; standalone coordination-only products are rare.
