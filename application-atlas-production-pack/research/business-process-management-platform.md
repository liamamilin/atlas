# Research Notes — Business Process Management Platform

Research date: 2026-09-07

## Research Goal

Understand what a Business Process Management (BPM) Platform actually is as a software category: what objects exist inside it, how a business process goes from definition to execution to supervision, who operates it, and where its boundary lies against neighboring Types (workflow management, approval workflow, low-code application platforms, case management, process mining, RPA, rules engines, integration platforms).

## Initial Boundary

Working hypothesis before research:

- Core: an explicitly modeled business process (usually BPMN) as a managed artifact; executable process instances driven by an engine; human tasks routed to workers; system steps invoked via connectors; monitoring of in-flight instances.
- Likely users: process analysts, developers, process owners/operations managers, end users (task workers), administrators.
- Likely confusions: Workflow Management Platform (closest sibling in the same directory section), Approval Workflow Platform, Low-code Application Platform, Process Mining Platform, RPA Platform, Business Rules Management System, Enterprise Service Management / request workflows, iPaaS.
- Known unknowns: how sharp the BPM-vs-workflow boundary really is in the market; whether "case management" is inside or adjacent; whether modeling-only tools (ARIS/Signavio-style) belong.

## Research Questions

1. What are the core objects? (process definition/model, instance, task, form, data, rules, events)
2. What is the full lifecycle? (model → automate → deploy/activate → run → supervise → improve)
3. How does human task allocation work? (assignment, claim, escalation, delegation)
4. How do system steps work? (connectors, service tasks, external workers)
5. How are models versioned and how do running instances survive model changes?
6. What does the runtime expose for supervision? (instance state, history, incidents, KPIs)
7. What roles/identity machinery does the platform carry?
8. Where is the boundary vs workflow tools, low-code platforms, case management, mining, RPA, rules, integration?
9. Historical check: would older workflow engines and modern lightweight workflow tools still fit the same definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, different customer tiers:

| Product | Philosophy / tier | Evidence tier |
|---|---|---|
| Camunda 7 | developer-centric, embeddable open-source engine + ops webapps | Tier 1 (full manual fetched) |
| Bizagi | model-first enterprise suite, PaaS cloud delivery | Tier 1 (docs portal + user guide pages fetched) |
| Bonita (Bonitasoft/Ofelia) | open-source application-building platform around a BPM engine; citizen + pro developer split | Tier 1 (full docs site fetched) |
| Oracle Process Automation (OIC) | cloud service module inside an integration suite | Tier 1 (Get Started + guide index fetched) |
| Flowable | open-source lineage (Activiti), enterprise low-code + engine, case/agentic positioning | Tier 1 (docs structure fetched) |

Market-context anchors (docs unreachable, no product claims made): Pega (docs.pega.com 403, pega.com 403), Appian (docs.appian.com 403 ×2, appian.com 406), IBM Business Automation Workflow (ibm.com/docs 403 ×2), Camunda 8 (docs.camunda.io 404 ×2). Boundary anchors referenced from general market knowledge only, no claims: ARIS / SAP Signavio (modeling/repository pole), Kissflow / Nintex (lightweight workflow pole).

## Sources

- Camunda 7 Manual (7.24) — https://docs.camunda.org/manual/7.24/ (fetched: manual root; TOC + intro observed)
- Bizagi Docs portal — https://docs.bizagi.com/ (fetched)
- Bizagi Platform User Guide — https://help.bizagi.com/platform/en/get_started.htm and https://help.bizagi.com/platform/en/bizagi-automation-getting-started.htm (fetched)
- Bonita Documentation 2026.2 — https://documentation.bonitasoft.com/ and https://documentation.bonitasoft.com/bonita/2026.2/bonita-overview/what-is-bonita-index (fetched)
- Oracle Cloud Infrastructure Process Automation — https://docs.oracle.com/en/cloud/paas/process-automation/index.html (fetched)
- Flowable Enterprise Documentation — https://docs.flowable.com/ (fetched)

Source-access limitations:

- Pega, Appian, IBM BAW, Camunda 8 official documentation could not be fetched (403/404/406, 2 attempts each, then abandoned per network-restriction rule). These products are treated as market anchors only; no operational claims about them are made anywhere in this research or the final document.
- Bizagi help center is partially JS-framed; only pages that render as static .htm were used.
- Flowable evidence is at documentation-structure level (section map + positioning), not deep page level; Flowable-specific claims are kept minimal.

## Product Observations

### Camunda 7 (evidence layer A — direct observation)

Self-description: "a light-weight, open-source platform for Business Process Management."

- **Process engine** is the center: process definitions, process instances, process variables, process versioning, process instance migration, process instance modification/restart, external tasks, connectors, incidents, history (with cleanup), job executor, transactions in processes, multi-tenancy.
- **BPMN 2.0 reference**: task types (service, send, user, business-rule, script, receive, manual), gateways (exclusive XOR, parallel, inclusive, event-based), events (none/message/timer/error/escalation/signal/cancel-compensation/conditional/link/terminate start events), subprocesses (embedded, call activity, event subprocess, transaction subprocess).
- **DMN 1.3** decision engine: decision tables (input/output/rule/hit policy), decision requirements graphs; decisions invoked from BPMN (business-rule task).
- **CMMN 1.1** case management: plan items, stages, milestones, sentries, entry/exit criteria — a separate case model alongside BPMN.
- **Web applications**: Cockpit (operations: dashboards, process definition view, process instance view, history, instance modification/restart/migration, failed jobs, suspension, message correlation, reports, deployments, auditing), Tasklist (end-user task inbox: filters, user assignment, task lifecycle, forms), Admin (user/group/tenant/authorization management, system management).
- **Modeler**: BPMN, DMN, Forms, element templates.
- **Identity/authorization service**; REST API; deployment as embedded engine (Tomcat/WildFly/Spring Boot/Quarkus), Camunda Run, Docker.
- Interpretation: engine-first BPM — the process model is a deployable artifact; execution state, history and incidents are first-class engine data; supervision and task surfaces are separate webapps on top.

### Bizagi (evidence layer A — direct observation)

Self-description: "Digital Business Platform"; platform = Modeler + Studio + Automation (cloud PaaS).

- **Three-phase lifecycle** (from "Bizagi Cloud Platform" page):
  1. **Modeler Services** — "design the workflow or process flow… modeling, documenting, simulating, publishing and sharing business processes in industry-standard BPMN."
  2. **Studio Cloud Services** — "automating involves converting process activities into a technological application… wizard guides you through each step: defining the data model, the user interface, the business rules, work allocation and integration with other applications."
  3. **Automation Service** — "deployed to Automation Service in a Test or Production Environment… presented in a Work Portal (web-based application)… the Work Portal watches for the correctness of execution of the different tasks and activities… controls and verifies that the tasks are processed at the correct moment, using the correct person or resource, and that the process runs according to your company's guidelines."
- **PaaS posture**: subscription entitles ready-to-use cloud environments (Production, optional Test/Staging), Customer Portal for admins; customer responsibilities: develop/deploy applications, manage user accounts and access rights, business parameters and connectivity, VPN, monitor resource usage (BPUs).
- Interpretation: model-first BPM — free modeling layer (with simulation) feeds an automation layer that turns the model into a running application on vendor-operated cloud; the Work Portal is the runtime surface for both task workers and process supervision.

### Bonita (evidence layer A — direct observation)

Self-description: "an open-source and extensible platform for business process automation and optimization… integrates with existing information systems, orchestrates heterogeneous systems… provides deep visibility of process execution."

- **Three components**: Bonita Studio (development), Bonita Runtime (BPM engine + applications), Bonita Continuous Delivery (environment-to-environment deployment).
- **Teamwork split**: "citizen developers input the business aspects (process, data model, main aspects of the user interfaces), professional developers… code extensions contributed as Maven dependencies. Both parts use BPMN as their common language."
- **Process modeling**: pools and lanes, tasks, iteration, gateways, expressions/scripts (Groovy), events, transitions, called processes, event subprocesses, operations, refactoring.
- **Actors + actor filters**: process actors mapped to organization (users/groups/roles); actor filters compute the assignee at runtime.
- **Connectors**: large official library — email, database, REST, SAP, Salesforce, ServiceNow, Workday, Dynamics, SharePoint, Kafka/RabbitMQ, e-signature (DocuSign/Adobe Sign/Yousign), UiPath (RPA), AI model connectors (OpenAI/Anthropic/Gemini/…), AI Agent Orchestrator.
- **Data**: Business Data Model (BDM, deployable business objects), process variables, contracts and contexts (input validation at task entry), documents attached to cases.
- **UI**: UI Designer (pages/forms, widgets, fragments), Living Applications (application descriptor, layouts, themes, multi-language), Adaptive Case Management as an example pattern.
- **Runtime applications**: Administrator application (process management, monitoring, process list, case list, task list, delegations administration), User Application (process list, case list, task list, delegations), Reporting App.
- **Identity**: organization (users/groups/roles), profiles, SSO (CAS/SAML/OIDC/Kerberos), LDAP/AD synchronizer, BDM access control.
- **Operations**: cluster, live update, backups, purge/archive, BDM retention.
- Terminology note: a process instance is called a **case** in Bonita.
- Interpretation: application-building BPM — the engine is wrapped in a full application stack (data model + UI + identity), so the deliverable is a "Living Application" whose behavior is governed by process models.

### Oracle Process Automation (evidence layer A — direct observation)

Self-description: "enables you to rapidly design, automate, and manage business processes in the cloud."

- **Two environments**: Design time (**Designer**: develop, test, activate process applications) and Runtime (**Workspace**: run, monitor, manage activated applications).
- **Design**: process applications; **structured processes** and **dynamic processes** (two process styles); basic/advanced controls; **human task activities**; email notifications/templates; **model decisions**; built-in functions; **activation** as the promotion step.
- **Work on tasks**: "find a task", "work on tasks" (end-user task surface).
- **Monitor and manage**: analytics, track processes, manage notifications.
- **Administer**: roles/access, provisioning, connectors, integrations (pairs with Oracle Integration 3).
- Interpretation: suite-module BPM — process automation as a service inside a broader integration cloud; same conceptual skeleton (model → activate → run → tasks → monitor) with cloud-service packaging.

### Flowable (evidence layer B — structure-level observation)

- Documentation sections: Getting Started, How-To, **Modeler** ("low-code modeling guides… building application models"), Developer, Administrator, User, **AI**, Cloud; plus **Flowable Forms**; open-source engine lineage (Activiti) with enterprise cloud.
- Positioning observed on the docs home: "Agentic Case Platform" — case-centric framing with AI/agentic capabilities.
- Interpretation: engine-lineage BPM converging on low-code modeling + case-centric + AI positioning. Because evidence is structure-level, no deeper Flowable-specific claims are made.

## Cross-product Comparison

| Structure | Camunda 7 | Bizagi | Bonita | Oracle PA | Flowable |
|---|---|---|---|---|---|
| Explicit process model as managed artifact | BPMN 2.0 definitions, Modeler | BPMN in Modeler Services | BPMN diagrams in Studio | Processes in Designer | Models in Modeler |
| Executable instances from the model | Process instances (engine) | Processes run in Work Portal | Cases (instances) on Runtime engine | Activated apps run in Workspace | Engine runtime |
| Human task allocation | User task + Tasklist (assignment, lifecycle) | Work allocation (Studio) + Work Portal tasks | Actors + actor filters + task list | Human task activities + find/work on tasks | User application |
| System steps | Service tasks, external tasks, connectors | Integration with other applications | Connectors (large library) | Connectors + integrations | Developer APIs |
| Decisions / rules | DMN decision tables | Business rules (Studio step) | Expressions/scripts; rules via connectors | "Model decisions" | (not observed in detail) |
| Forms / task UI | Camunda Forms, task forms | UI definition (Studio step) | UI Designer, forms, Living Applications | (in Designer) | Flowable Forms |
| Process data | Process variables | Data model (Studio step) | BDM + process variables + contracts | (in Designer) | (not observed in detail) |
| Flow logic | Gateways, events, subprocesses, call activities | Modeled in BPMN | Gateways, events, called processes, event subprocesses | Structured + dynamic processes | (modeled) |
| Versioning / environments | Process versioning, instance migration, deployments | Test/Production environments | Environments, deploy, Continuous Delivery | Activation; Test/Production | Cloud/deploy |
| Supervision of in-flight work | Cockpit (definition/instance views, history, incidents, failed jobs) | Work Portal "watches correctness of execution" | Administrator app (monitoring, case list) | Workspace (track processes, analytics) | Administrator |
| Identity / roles | Identity + authorization service, tenants | User accounts + access rights | Organization, profiles, SSO/LDAP | Roles | Administrator |
| Audit / history | History (configurable, cleanup), auditing | (implied by Work Portal control) | Archives, queriable logging | (not observed) | (not observed) |
| Case management | CMMN (separate model) | — | ACM example pattern | Dynamic processes | Case/agentic positioning |
| Simulation | — (not in core) | Modeler simulation | — | — | — |
| Analytics / KPI | Cockpit reports | (Work Portal control) | Reporting App | Analytics | (not observed) |
| AI | — (not in C7 core) | — | AI connectors, AI Agent Orchestrator | — | AI section |
| Deployment posture | Embedded engine / Run / Docker | Vendor PaaS | OSS bundle / cluster / Cloud | Cloud service in OIC | OSS + Enterprise Cloud |

Reading of the table:

- The first five rows are present in **all five products** — this is the candidate defining core.
- Rows 6–13 are present in nearly all — standard mature capabilities.
- Simulation, AI, case management, analytics vary — variant/optional layer.
- Deployment posture is the biggest philosophical axis (embedded library ↔ vendor PaaS).

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

A BPM Platform is recognizable by exactly this structure:

1. **Explicit process model as a persistent managed artifact** — the end-to-end business process is defined as a first-class, versioned object (a graph of steps, flow logic and events), not as scattered code or ad-hoc task lists.
2. **Executable process instances** — each real-world run of the process is an individual instance whose state the platform's engine advances step-by-step according to the model, carrying its own data.
3. **Orchestration of human and system work** — model steps allocate work to identified people (task assignment against an organizational identity) and invoke system actions (connectors/services), so one model governs both.
4. **Observable execution state and history** — the platform maintains, per instance, where it is, what happened, and what failed, so in-flight processes can be inspected and supervised.

Remove #1 → the product is an application builder or integration tool. Remove #2 → a pure modeling/repository tool (ARIS/Signavio-modeler pole). Remove #3 → an iPaaS (system-to-system only) or a plain task tracker (human-only). Remove #4 → an unobservable library with no operational grip; the category's reason to exist disappears.

### L1 — Common Mature Structure

- Visual modeling studio; BPMN as the dominant notation (all five sampled products use or accept BPMN).
- Task inbox / work portal for task workers (list, open, complete via forms; claim/assignment; delegation observed in Bonita, assignment in Camunda).
- Forms builder / task UI definition.
- Process data model: process variables and/or a deployable business data model; documents attached to instances.
- Connectors / integration to external systems; service/system steps.
- Decisions/rules layer (DMN-style decision tables or rules invoked from the model).
- Flow logic vocabulary: gateways (exclusive/parallel/inclusive), events (timer, message, error, escalation), subprocesses/called processes.
- Versioning + multi-environment deployment (dev/test/production; "activation" in Oracle terms).
- Operations console: instance views, history, incident/failed-job handling, retries, instance migration.
- Organizational identity: users/groups/roles, SSO/LDAP/AD integration, authorization over models and instances.
- Audit trail / execution history.
- KPI dashboards / process analytics (Cockpit reports, Reporting App, Workspace analytics).

### L2 — Variant / Optional Structure

- **Deployment posture**: embedded engine library inside the customer's application (Camunda 7) ↔ self-managed server/cluster (Bonita, Camunda Run) ↔ vendor-operated PaaS/cloud (Bizagi Automation Service, Oracle PA, Bonita Cloud, Flowable Cloud).
- **Audience posture**: developer-first (Camunda, Flowable, Bonita pro-dev side) ↔ analyst/model-first (Bizagi Modeler) ↔ low-code citizen+pro mix (Oracle, Flowable Modeler, Bonita citizen developers).
- **Notation posture**: standard BPMN/DMN/CMMN vs proprietary notations (older generation); DMN for decisions; CMMN/dynamic processes/ACM for case-style work.
- **Case-centric extension**: CMMN (Camunda), dynamic processes (Oracle), ACM pattern (Bonita), case/agentic positioning (Flowable) — common but not defining.
- **Suite membership**: standalone platform vs module of an integration cloud (Oracle PA inside OIC) vs member of a broader automation suite (Bizagi).
- **Ecosystem integrations**: RPA invocation (Bonita↔UiPath connector), process mining pairing, AI model/agent connectors (Bonita, Flowable).
- **Simulation** of models before deployment (observed in Bizagi Modeler; product-dependent).
- **Multi-tenancy** (Camunda tenants), industry templates/content packs.

### L3 — Vendor-specific (research notes only)

- Camunda: Cockpit/Tasklist/Admin/Cawemo product names; external-task pattern; job executor; incidents; history time-to-live; element templates; Camunda 8/Zeebe architecture (unfetched — no claims).
- Bizagi: Modeler Services / Studio Cloud Services / Automation Service split; Work Portal; Customer Portal; BPUs (capacity units); PFX integrated authentication; VPN shared responsibility.
- Bonita: Business Data Model; contracts and contexts; actor filters; Living Applications; UI Designer; Bonita Continuous Delivery; Ofelia rebrand; Community vs Enterprise editions.
- Oracle: Designer/Workspace environment split; structured vs dynamic processes; activation; BreakGlass; pairing with Oracle Integration 3.
- Flowable: "Agentic Case Platform" positioning; Flowable Forms; Work/Modeler/Administrator/User application set.

## Vendor-specific Findings

See L3 above. None of these were promoted into the final document beyond neutral, vendor-attributed mention in Representative Products.

## Boundary Findings

- **vs Workflow Management Platform (directory sibling, sharpest seam).** Both model multi-step work with human tasks. The gradient observed: BPM platforms treat the process model as the governed system-of-record for an end-to-end business process, execute it on a process engine with instance state/history/versioning/migration, and wrap it in full lifecycle tooling (modeling discipline, simulation, decisions, operations consoles). Lightweight workflow tools center on configuring recurring internal workflows (form → routing → approvals) with lighter lifecycle machinery. The boundary is **gradient, not crisp** — modern low-code workflow products increasingly carry engine-grade features. Recorded as a boundary issue for joint review; this leaf's side of the test: if the artifact is a governed, versioned, engine-executed end-to-end process model with instance lifecycle, it is BPM; if it is a configured routing recipe for a recurring work pattern, it is workflow management.
- **vs Approval Workflow Platform.** Approval platforms specialize in request→approve→outcome chains. BPM generalizes: approvals are just human-task steps inside a larger orchestrated process. Remove the multi-step orchestration and keep only the approval chain → approval platform.
- **vs Low-code Application Platform.** Low-code platforms' primary artifact is the application (data + UI + logic); BPM's primary artifact is the process model. Straddle observed: Bonita builds applications around processes; Bizagi markets "Low-Code Apps"; Appian/Pega (market anchors) are commonly described as both. The honest seam: what the platform manages as its central versioned artifact — the process model (BPM) vs the application (low-code).
- **vs Process Mining Platform.** Mining discovers process reality from event logs (as-is); BPM prescribes and executes the normative model (to-be) and produces the very event history mining consumes. Complementary; suites increasingly bundle both.
- **vs Robotic Process Automation Platform.** RPA automates UI-level actions inside a step; BPM orchestrates the steps. Observed integration: Bonita ships a UiPath connector — RPA as a called system step.
- **vs Business Rules / Decision Management.** Rules decide; processes sequence. DMN decision tables are invoked from process models (Camunda business-rule task; Oracle "model decisions"). Separate Type for the rules engine itself.
- **vs Integration Platform / iPaaS.** iPaaS centers on system-to-system data/application pipelines; BPM centers on business process instances that mix human and system steps. Oracle PA's pairing with Oracle Integration documents the seam from inside one vendor.
- **vs Case Management.** Predetermined flow (process) vs outcome-driven flexible work (case). Sampled products carry case-style extensions (CMMN, dynamic processes, ACM) — adjacent capability, not the defining core.
- **Modeling-only tools fail L0 #2–#4**: ARIS/Signavio-style modelers (and Bizagi Modeler standalone) document and share processes but do not execute instances — they are a different Type (process modeling/repository), even though they are bundled with BPM suites.
- **"去掉什么就变成另一个 Type" 判据**: remove instance execution → process modeling tool; remove the governed model → workflow/approval tooling; remove human tasks → iPaaS; remove system steps → task tracker; remove supervision/history → bare scheduler.

## Historical / Market-Sample Check (§24)

- Older workflow engines (Staffware, IBM MQ Workflow, FileNet, TIBCO InConcert era) already had: explicit process definitions, engine-executed instances, human task routing, system invocations, monitoring. They satisfy the L0 — the definition does not overfit the modern low-code/cloud era.
- Modern lightweight workflow tools (Kissflow/Nintex class) also satisfy L0 at its minimum — which confirms that L0 alone does **not** separate BPM from workflow management; the separation is depth/governance of the model lifecycle (see Boundary Findings). This is recorded as a taxonomy gradient rather than resolved unilaterally.
- Modeling-only tools (ARIS, Signavio modeler, standalone Bizagi Modeler) fail the instance-execution invariant — correctly excluded from the Type.

## Uncertainties

- Pega, Appian, IBM BAW, Camunda 8 documentation unreachable — the enterprise-suite pole (Pega/Appian/IBM) is argued from market position only; their case-centric and AI-heavy postures are NOT reflected as claims in the final document.
- Flowable evidence is structure-level; its decision/rules and data-model specifics were not observed.
- Simulation prevalence: observed in Bizagi only within the sample; likely common in modeling-side tools but not verified across the sample.
- Exact KPI/analytics depth varies and was not uniformly documented; kept qualitative.
- The BPM-vs-workflow gradient (see Boundary Findings) is a genuine market ambiguity, not a research failure; flagged for joint review with the Workflow Management Platform leaf.

## Final Synthesis

A Business Process Management Platform is organization-facing infrastructure whose defining core is: an explicit, governed, versioned process model as the central artifact; engine-executed process instances advanced according to that model; orchestration that drives both human tasks (assigned against organizational identity) and system steps (connectors/services) from the same model; and observable per-instance state and history that makes in-flight processes supervisable.

Around that core, mature products add: visual BPMN modeling studios, task inboxes with forms, process/business data models, connector libraries, decision/rules layers, event/gateway flow logic, multi-environment versioning and deployment, operations consoles with incident handling and instance migration, organizational identity integration, audit trails, and process analytics. Variants concentrate in deployment posture (embedded engine ↔ self-managed ↔ vendor cloud), audience posture (developer-first ↔ analyst-first ↔ low-code mix), case-centric extensions, and suite membership.

The category's center of gravity is the **process model as the managed contract between business design and runtime execution** — everything else in the product serves defining, executing, supervising, or improving that model's instances.
