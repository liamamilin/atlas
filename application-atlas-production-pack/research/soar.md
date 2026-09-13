# Research Notes — SOAR (Security Orchestration, Automation and Response)

## Research Goal

Understand what a SOAR actually is as an Application Type: the objects inside it (playbooks/workflows, integrations/connectors, actions, triggers, runs, cases), who uses it, how automated response actually flows through it, which rules govern execution, and — critically — where it begins and ends relative to SIEM, Cyber Incident Response Platform, XDR, EDR, SOC Platform, ITSM incident tooling, and generic workflow automation.

Prior passes left two binding notes for this pass (recorded in STATUS.md Boundary Issues):

1. **cyber-incident-response-platform (processed 2026-09-07)** — joint-review flag: decide keep-both-with-seam vs variant presentation, with the adopted discriminator "automation/orchestration as center of gravity (SOAR) vs the incident case + response lifecycle + recorded response activity (CIRP)". This pass discharges the SOAR side.
2. **siem (processed 2026-09-09)** — forward note: the seam is analytics-over-event-data vs orchestration-across-external-tools; all five sampled SIEM products bundle SOAR-like automation at varying depth, so this pass should treat bundling as packaging, not identity, and expect the SIEM case/alert object as a trigger source.

## Initial Boundary (hypothesis before research)

Working hypothesis: a SOAR is a tool-agnostic security automation and orchestration platform. It connects to the security tools the customer already runs, executes automatable response playbooks triggered by security signals, orchestrates actions across those tools, and records execution. The most likely confusions:

- vs SIEM — both sit at the center of a modern SOC; both bundle "automation" today.
- vs Cyber Incident Response Platform — sampled SOAR products carry case layers.
- vs XDR — both "respond", but through different instrumentation.
- vs generic workflow automation (no directory leaf) — the deepest structural risk: if the SOAR core is just "workflow automation with connectors", the Type collapses into Workflow Management / no-code automation territory. The differentiator hypothesis: the security-operations substrate (security-tool connector library, security-signal triggers, response-action vocabulary).
- vs RPA — automation of UI-level arbitrary software vs API/tool-level orchestration.

## Research Questions

1. What are the core objects? Is there a stable vocabulary across products?
2. What exactly is a "playbook"/"workflow" — what building blocks does it have?
3. How do playbooks get triggered? What is the relationship to the SIEM alert/incident?
4. What does the integration/connectivity layer look like (apps, assets, connectors, credentials)?
5. What does "response" concretely mean (enrichment, containment, notification, ticketing)?
6. Where do humans sit in the loop (approvals, manual tasks, SLAs)?
7. How is execution recorded/audited?
8. Where does case management sit — core or embedded packaging?
9. Historical check: does the definition hold for the pre-cloud, pre-AI generation (Phantom/Demisto heritage)?
10. Boundary discriminators vs the neighboring Types above.

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different realization layers (standalone engine, suite pillar, SIEM-embedded module, open-source self-hosted, low-code AI-era platform):

| Product | Philosophy / position | Evidence depth |
|---|---|---|
| Splunk SOAR (Cloud) | SIEM-vendor-attached orchestration engine (Phantom heritage); on-prem + SaaS | Tier-1 docs ×2 pages + docs root (2026-09-09) |
| Cortex XSOAR (Palo Alto Networks) | automation-first with incident management + threat intel management; SaaS + on-prem | Tier-1 docs via official GitBook docs incl. query retrieval (2026-09-09) |
| Microsoft Sentinel (automation layer) | SIEM-embedded pole: playbooks/automation rules living inside a SIEM | Tier-1 Microsoft Learn (2026-09-09) |
| Shuffle | open-source "general purpose security automation platform", self-hosted or cloud, MSSP-minded | Tier-1 official GitHub repo README (2026-09-09) |
| Swimlane (Turbine) | low-code, AI-native security automation platform ("Hero AI", text-to-playbook) | docs root/quickstart only — deeper pages JS-gated (2026-09-09) |

Rejected for sampling: **Tines** (tines.com returned 403 on both fetch attempts — abandoned per network rule; no product claims made), **IBM QRadar SOAR** (unreachable 403 ×2 in the prior CIRP pass; not re-attempted), **Torq/Swimlane deep docs** (JS-gated; Swimlane kept at root-doc depth).

## Sources

- Splunk: "About Splunk SOAR (Cloud)" (docs.splunk.com/Documentation/SOAR/current/User/Intro, mirrored at help.splunk.com); "Use playbooks to automate analyst workflows in Splunk SOAR (Cloud)" (…/Playbook/Overview); docs root /Documentation/SOAR. All fetched 2026-09-09. Layer A.
- Palo Alto Networks: cortex-docs.paloaltonetworks.com — Cortex XSOAR documentation home (readme.md) and two documentation-query retrievals returning excerpts sourced from "What Are Playbooks?", "Playbook Development", "Incident Lifecycle", "War Room Overview", "Concepts", "Content packs" pages. Fetched 2026-09-09. Layer A (official docs; retrieved via the docs platform's query mechanism).
- Microsoft: "Automate Threat Response with Playbooks in Microsoft Sentinel" (learn.microsoft.com/en-us/azure/sentinel/automate-responses-with-playbooks). Fetched 2026-09-09. Layer A.
- Shuffle: official GitHub repository README (github.com/Shuffle/Shuffle). Fetched 2026-09-09. Layer A. (shuffler.io site docs are cookie-walled.)
- Swimlane: docs.swimlane.com root / Turbine User Guide Quickstart. Fetched 2026-09-09. Layer A for positioning vocabulary only.

**Source-access Limitation**: Tines unreachable (403 ×2) — the "no-SIEM-heritage automation platform adopted by SOCs" pole is documented structurally via Shuffle's self-description ("general purpose security automation platform") instead; no Tines claims. Swimlane evidence limited to the docs root; deeper feature claims not made. IBM QRadar SOAR heritage pole unverified from primary sources (prior pass).

## Product Observations

### Splunk SOAR (Cloud) — evidence layer A

- Self-definition: "combines security infrastructure orchestration, playbook automation, and case management capabilities to integrate your team, processes, and tools to help you orchestrate security workflows, automate repetitive security tasks, and quickly respond to threats." Audience: SOC staff member, analyst, or manager.
- Official glossary (terminology table):
  - **App** — "A connection to third-party security technologies. The connection allows Splunk SOAR (Cloud) to access and run actions provided by the third-party technologies."
  - **Asset** — "A specific instance of an app… represents a physical or virtual device within your organization such as a server, endpoint, router, or firewall… configure an asset with the specific connection details for this firewall."
  - **Action** — "A high level primitive… such as get process dump, block ip, suspend vm, or terminate process. Actions are run in playbooks or manually from the… web interface. Actions are made available to Splunk SOAR (Cloud) by apps."
  - **Playbook** — "A series of automation tasks that act on new data entering Splunk SOAR (Cloud)… configure a playbook to run actions against all new containers with a specific label. Or configure running a playbook as part of the workflow in a workbook."
  - **Container** — "A security event that is ingested into Splunk SOAR (Cloud)… Labels are used to group related containers… run a playbook against all containers with the same label."
  - **Case** — "A special kind of container that can hold other containers… promote one of those containers to a case and then add the other related containers to the case."
  - **Artifact** — "A piece of information added to a container, such as a file hash, IP address, or email header."
  - **Indicator/IOC** — "populates the Common Event Format (CEF) fields in an artifact. Indicators are the smallest unit of data that can be acted upon."
  - **Workbook** — "A template providing a list of standard tasks that analysts can follow when evaluating containers or cases."
  - **Owner** — "The person responsible for managing assets… Owners receive approvals, which are requests to run a particular action on an asset. Approvals… contain a service level agreement (SLA) dictating the expected response time. SLAs can be set on events, phases, and tasks."
- Playbook authoring: visual playbook editor, "create playbooks without having to write code"; "link together a series of actions that are provided by apps"; examples: MaxMind `geolocate ip`, Okta `set password` / `enable user`; "The actions available for use in your playbooks are determined by the apps integrated."
- Run modes: triage/investigate cases manually; adding a case to Investigation; "Configuring playbooks to run automatically directly from the playbook editor." Run statistics viewable in the editor.
- Documented behavior rule: "If your system restarts while a playbook is running, the playbook run is canceled. Any changes made by the playbook before the restart remain, and are not rolled back."
- Python Playbook API + REST API exist (code surface alongside the visual editor).
- Ecosystem: "Develop Apps for Splunk SOAR" guide; Splunk App for SOAR Export "translates and forwards information from the Splunk platform to a Splunk SOAR instance"; Automation Broker "orchestrate and automate your notable responses for on-premises assets using apps, connectors and playbooks from Splunk SOAR."
- Heritage: legacy "Splunk Phantom" product listed; migration manual "Migrate from Splunk Phantom to Splunk SOAR (Cloud)" migrating "applications, playbooks, custom functions, and administration settings."

### Cortex XSOAR — evidence layer A

- Product card (official docs home): "Cortex XSOAR → Response playbooks → Tool orchestration → Incident management." Documentation scope: "Configure systems, orchestration, incidents, and playbooks."
- Core concepts (docs): **Integrations** "Connect Cortex XSOAR to third-party security/incident-management products. They fetch events (for example, alerts) and those events are then turned into incidents." **Incidents** — "the analyst-facing security items to investigate and remediate." **Playbooks** — "prescriptive automation that runs on an incident. Once an incident is created (or when you run manually), the relevant playbook enriches the incident using data from other products via integrations." **War Room** — "the incident's chronological workspace — an audit trail of actions, artifacts, and collaboration." **Context data** — "the structured 'working memory' that commands/scripts add to." Flow: Integrations → Incidents → Playbooks → War Room (context + audit trail).
- Playbook building blocks: tasks (run automations/sub-playbooks, communicate with users, set conditions, store data); conditional tasks deciding the path; loops ("check for specific information before continuing"); **manual tasks** "when an analyst must confirm information or escalate an incident"; manual conditional task "Only the assignee can complete the task" — blocks playbook progress until completed.
- **Content packs**: "organize Cortex XSOAR Marketplace content into packs of components — such as integrations, scripts, playbooks, and widgets — to address specific use cases… created by Palo Alto Networks and others."
- Deployment: 8 SaaS and 8 On-prem (and 6 heritage); Demisto SDK for content development (Demisto heritage visible in the SDK name); multi-tenant guide for MSP workflows; threat intel management guides ("unify threat intelligence aggregation, scoring, and sharing").

### Microsoft Sentinel (automation layer) — evidence layer A

- "Microsoft Sentinel playbooks are automated workflows that help you respond to threats quickly and consistently… run preconfigured sets of remediation actions and automate and orchestrate your threat response. Run playbooks automatically in response to specific alerts and incidents that trigger a configured automation rule, or run them manually for a particular entity or alert."
- Example: "if an account and machine are compromised, a playbook can automatically isolate the machine from the network and block the account before the SOC team gets notified of the incident."
- Use cases table: **Enrichment** ("collect data and attach it to an incident"), **Bi-directional sync** ("sync Microsoft Sentinel incidents with other ticketing systems… attach a playbook that opens a ticket in ServiceNow"), **Orchestration** ("send a message to your security operations channel in Microsoft Teams or Slack"), **Response** ("respond to threats right away with minimal human involvement… or manually trigger automated steps during an investigation or while hunting").
- Substrate: playbooks use Azure Logic Apps ("additional charges can apply"); playbook templates are ARM templates with Logic Apps workflows + API connections; templates from the Automation page, Content hub, and GitHub.
- Distinct **automation rules** object: automation rules trigger playbooks on new alerts/incidents (incident handling machinery separate from the playbook itself).
- Role model: Sentinel Responder "lets you access an incident in order to run a playbook manually, but doesn't allow you to run the playbook" (distinct Playbook Operator role runs it); Automation Contributor role exists so automation rules can run playbooks on Sentinel's behalf.
- Case/alert objects belong to the SIEM; the playbook/automation layer attaches to them. This is the SIEM-embedded realization pole.

### Shuffle — evidence layer A

- Self-description: "Shuffle is an open source automation platform, built for and by the security professionals… Built to work well with MSSP's and other service providers in mind." Repo about-line: "A general purpose security automation platform. Our focus is on collaboration and resource sharing." Blog series titles: "an open source SOAR platform."
- Features: "Simple, feature rich workflow editor"; "App creator using OpenAPI"; "Premade apps for your security tools"; "Organization and sub-organization control" (MSSP relevance); "Hybrid resource sharing with shuffler.io (optional)."
- Architecture: **Orborus** "distributes execution locations"; **Worker** "runs a workflow" (execution substrate separate from the UI); deployment self-hosted (docker-compose) or cloud.
- Integrations evidence: webhook integration example; blogpost walkthroughs integrating TheHive, Cortex, MISP, VirusTotal, Wazuh; separate "security-openapis" repository of OpenAPI app definitions.
- Workflow/app vocabulary (not "playbook"); licensing MIT/AGPLv3.

### Swimlane (Turbine) — evidence layer A (docs root only)

- Turbine User Guide quickstart: sections "Daily Operations… workspaces, dashboards, records, and reports"; "**Orchestration** — Build automation with playbooks, connectors, and components"; "**Hero AI** — Companion chat, Text to Playbook, component building, and native AI actions"; "Try a Solution — **AI SOC Solution** — a complete, ready-to-use security operations workflow."
- Vocabulary: playbooks + connectors + components on a records-based platform; AI-assisted authoring. (Deeper pages JS-gated; no operational claims beyond this.)

## Cross-product Comparison

| Dimension | Splunk SOAR | Cortex XSOAR | Sentinel (automation layer) | Shuffle | Swimlane/Turbine |
|---|---|---|---|---|---|
| Named connector object | App + Asset (instance w/ connection details) | Integration | Logic Apps API connections (via templates) | App (OpenAPI-created) | Connector |
| Named automation program | Playbook (visual editor + Python API) | Playbook (tasks/conditions/loops/manual) | Playbook (Logic Apps workflow) | Workflow | Playbook |
| Trigger sources | container ingestion (+label matching), workbook step, manual run, auto-run config | incident creation, manual run | automation rule on alert/incident creation, manual run | webhook, events (docs+blog), manual | signal/records-based (root docs only) |
| Worked object | Container → Case (promotable) + Artifact/CEF | Incident + indicators + context data | SIEM alert/incident (owned by SIEM) | event/webhook payload (no first-class case observed) | records |
| Human gate | Owner approvals with SLAs on events/phases/tasks | Manual tasks; assignee-only completion blocks | role-gated manual run | not directly observed in fetched pages | (root docs only) |
| Execution record | run statistics in editor | War Room audit trail + context | Logic Apps run history | Worker-executed workflow runs | dashboards/reports |
| Content economy | app store heritage (Phantom apps), App for SOAR | content packs / Marketplace (free) | playbook templates via Content hub + GitHub | premade apps + shared workflows repo | "AI SOC Solution" packaged workflow |
| Case layer | embedded (container→case, workbook tasks) | embedded (incident management core) | absent from the automation layer (SIEM owns it) | not observed as first-class | records-centric |
| AI-era machinery | Automation Builder Agent (build playbooks) | (docs home shows AgentiX sibling product) | — | — | Hero AI text-to-playbook |

**Cross-product commonalities (evidence layer B):**

1. Every sampled product has a named, first-class **connection object** to third-party security technologies, configured per-instance with connection details/credentials, whose instances expose **actions**. (A: Splunk app/asset + actions quote; XSOAR integrations; Sentinel API connections; Shuffle apps; Swimlane connectors.)
2. Every sampled product has a persistent, authored, re-editable **automation program** (playbook/workflow) — trigger + ordered/branching steps + actions, with conditions/loops and (where documented) human-gate steps. (A: all five.)
3. Every sampled product **executes programs automatically in response to security signals** and **manually on demand** during investigation. (A: Splunk triage/manual/auto; XSOAR incident-creation/manual; Sentinel automation-rule/manual; Shuffle webhooks/manual; Swimlane — implied by "orchestration", weaker.)
4. Every documented product **retains execution records** (run statistics, War Room audit trail, Logic Apps run history, Worker-run workflows). (A ×4; Swimlane not directly observed.)
5. **Action vocabulary is security-response-shaped**: enrich (geolocate, reputation), contain (block IP, suspend VM, isolate machine, disable account/set password), communicate (Teams/Slack, email), ticket (ServiceNow bi-directional sync). (A: Splunk examples; XSOAR enrichment; Sentinel use-case table.)
6. **Prebuilt content layer** — marketplaces/template libraries/packaged solutions of playbooks + integrations. (A: XSOAR content packs; Sentinel templates; Shuffle premade apps; Splunk app ecosystem; Swimlane AI SOC solution.)
7. **Human-in-the-loop machinery** is present wherever the product documents execution controls: approval requests with SLAs, assignee-only manual tasks that block, role separation between viewing an incident and running a playbook. (A ×3; not observed as absent anywhere.)

**Variable dimensions (variant axes):**

- Packaging: standalone engine (Splunk SOAR, XSOAR) vs SIEM-embedded module (Sentinel) vs open-source self-hosted/cloud (Shuffle) vs low-code platform with broader ops framing (Swimlane/Turbine).
- Case depth: promotable case object with workbook tasks (Splunk) → incident management as a named pillar (XSOAR) → no case object in the automation layer (Sentinel/Shuffle).
- Authoring philosophy: visual-first with code escape hatch (Splunk, XSOAR) vs external workflow substrate (Sentinel/Logic Apps) vs open-source code+GUI (Shuffle) vs AI-assisted text-to-playbook (Swimlane).
- Execution substrate: centralized engine vs distributed workers (Shuffle Orborus/Worker; Splunk Automation Broker for on-prem assets).
- Event intake: own ingestion pipeline (Splunk containers; XSOAR integrations fetching events) vs consuming an upstream SIEM's alerts/incidents (Sentinel) vs push-based webhooks (Shuffle).
- Audience extension: MSSP multi-tenancy (Shuffle sub-orgs; XSOAR multi-tenant guide), threat-intel management (XSOAR), broader ops automation beyond SOC (Shuffle "general purpose"; Swimlane platform framing).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The tool-agnostic security-tool connection layer.** Built-in, configurable connections to third-party security technologies the SOAR does not itself run — held as named connector objects (app/asset, integration, connector) carrying per-instance connection details and credentials, and exposing the actions the SOAR can perform on the connected tool's behalf. Remove this layer → single-product scripted response (EDR/XDR/ITSM automation territory), or a mere library of API documentation.
2. **The playbook/workflow as persistent re-editable response automation.** A stored automation program — trigger conditions, ordered/branching steps (conditions, loops, data/enrichment manipulation, optional human-approval steps) executing actions across the connected tools — authored through a visual editor and/or code, surviving between runs, editable as the organization's response practice changes. Remove → runbooks as documents, or ad-hoc one-off console actions.
3. **The triggered, recorded run.** Security signals (ingested events, upstream SIEM alerts/incidents, webhooks, schedules) or manual invocation fire executions; each run proceeds step-by-step through the program, passing data between steps, and leaves a retained, inspectable execution record (steps, inputs, outputs, errors) with results written back to the triggering object or the tools. Remove → a connector framework with no automation, or scripts executed by hand.

Jointly-held is load-bearing: (1) alone = an integration/connector catalog; (2) alone = a workflow-design tool / runbook authoring; (3) alone = scripting; (1)+(3) without (2) = point-to-point automation glue; (2)+(3) without (1) = generic workflow automation; (1)+(2) without (3) = an authored-but-not-executed playbook library.

**Security-operations orientation** is not a separate leg — it is carried inside the structures: connections target security tools, triggers are security signals, actions use the security response vocabulary (enrich / contain / notify / ticket). Strip the security orientation and the same three structures describe a generic workflow automation platform — the deepest boundary of this Type.

### L1 — Common Mature Structure

- Event/incident intake and normalization (own ingestion pipeline or upstream SIEM consumption), with the triggering security object (container/incident/alert) as the worked record.
- Artifact/indicator extraction and enrichment actions (reputation, geolocation, hashing).
- Case/incident management layer (promotion of related events into a case, task lists, notes) — embedded packaging, realized at different depths; some realizations leave the case object to the SIEM.
- Human-in-the-loop approval machinery: approval requests routed to owners with SLAs, manual tasks blocking program progress until a named assignee completes them.
- Prebuilt content economy: marketplaces/template libraries of playbooks, integrations, and packaged use-case solutions.
- Run monitoring: run statistics, execution history, dashboards, metrics.
- Role model separating authoring, running, and administration; audit trails.
- REST APIs and webhooks for programmatic control and integration.

### L2 — Variant / Optional Structure

- Deployment: SaaS, on-premises, hybrid, self-hosted open-source; distributed execution workers/brokers for on-prem assets.
- Case-management depth (none → embedded → full IR case management).
- Authoring philosophy: no-code visual ↔ low-code ↔ code-first; AI-assisted authoring (text-to-playbook, automation builder agents) as the era-current addition.
- Threat-intelligence management depth (feeds, scoring, sharing) — a named pillar in one sampled product, absent/light elsewhere.
- MSSP/multi-tenant operation.
- Scope drift beyond the SOC toward general ops automation ("general purpose security automation" self-descriptions) — a gradient, not a wall (see Boundary Findings 7).

### L3 — Vendor-specific (Research Notes only)

- Splunk: app/asset/container/label/CEF artifact/workbook/owner-approvals terminology; SLAs set on events/phases/tasks; restart-cancellation rule (changes before restart remain); App for SOAR Export; Automation Broker; Phantom heritage/migration; Automation Builder Agent; 1200px editor screen-width note.
- XSOAR: War Room; context data as JSON "working memory" (extend-context); Demisto SDK; playground; content packs free-of-charge framing; "only the assignee can complete the task" manual-task rule; multi-tenant/MSP guides; engines.
- Sentinel: automation rules vs playbooks split; Azure Logic Apps substrate with separate charges; playbook templates as ARM templates; role set (Responder vs Playbook Operator vs Automation Contributor service-account role); Azure portal retirement note (era-current).
- Shuffle: Orborus (execution distribution) / Worker (workflow execution); OpenAPI app creator; sub-organizations; singul.io; MIT/AGPL licensing split.
- Swimlane: Turbine platform naming; Hero AI companion chat / Text to Playbook / native AI actions; "AI SOC Solution".

## Historical / Market-Sample Check

- The definition does not require SaaS, AI, visual editors, marketplaces, or case management. The Phantom-heritage generation satisfies the three-leg core with apps (integrations), playbooks, containers/events, and audit — evidenced directly by Splunk's own migration manual (apps, playbooks, custom functions, administration settings migrate from Phantom to SOAR) and the legacy Phantom product listing; Demisto heritage visible in the still-named Demisto SDK.
- The open-source Shuffle pole satisfies the core with no first-class case object (workflow + app + webhook machinery only) — proving case management is not definitional.
- The Sentinel pole satisfies the trigger/automation legs while the case object belongs to the SIEM — proving the worked-object layer is not definitional either.
- Code-first authoring (Python Playbook API) and external-substrate authoring (Logic Apps) both satisfy leg 2 — visual no-code is not definitional.
- Check **passed**: older, on-prem, and differently positioned realizations all fit the three-leg core; nothing in L0 depends on the current cloud/AI/marketplace era.

## Boundary Findings

1. **vs SIEM** (§15, processed): SIEM = analytics/detection/investigation over the organization's own security event data; SOAR = orchestration/automation of response across external tools. The SIEM alert/incident is the classic trigger input; a SOAR commonly consumes it. Mature SIEMs bundle playbook automation (Sentinel playbooks/automation rules; Splunk ES+SOAR convergence) — **packaging, not identity**, confirmed from this side. Removal test both ways: remove the automation layer → the SIEM remains a SIEM; remove the analytics layer from a Splunk-class SOAR → it remains a working automation engine. **Discharges the siem pass's forward note.**
2. **vs Cyber Incident Response Platform** (§15, processed): CIRP's center = the incident case + response lifecycle + recorded response activity; SOAR's center = the automation/orchestration loop. Sampled SOAR products embed case layers (Splunk container→case + workbook; XSOAR incident management as named pillar) — the same embedded-realization pattern the CIRP pass observed. Removal test: remove playbooks/orchestration from a SOAR → it degrades into a case-management application (CIRP); remove the case layer → the SOAR remains a working automation engine (Shuffle-class runs without one; Sentinel's automation layer runs on the SIEM's case object). **Keep-both RATIFIED per the adopted discriminator — this pass discharges the CIRP joint-review flag from the SOAR side.** The flag's third party, soc-platform, remains unprocessed; its side of the review stays open.
3. **vs XDR** (§15, processed): XDR executes response through its own instrumentation across the domains it covers; SOAR orchestrates the customer's heterogeneous toolset, tool-agnostically — an XDR's containment action can be one integration among many driven by a SOAR. Seam: response-through-own-instrumentation vs orchestration-across-external-tools.
4. **vs EDR / NDR** (§15): single-domain detection+response Types; a SOAR action can call them, but the SOAR's unit of logic is the cross-tool workflow, not the domain signal.
5. **vs On-call Management / Incident Management (ITSM)**: ticketing/paging appear in SOARs as **integration targets** (Sentinel bi-directional ServiceNow sync; Teams/Slack orchestration; the CIRP pass observed a SOAR closing incidents in a ticketing system). ITSM incidents carry restore-service semantics; SOAR actions carry security-response semantics. The SOAR consumes these systems; it does not replace them.
6. **vs SOC Platform** (§15, unprocessed): per the CIRP/SIEM passes' framing, products centered on the whole-operations layer (process/workforce/metrics across the SOC) are a different Type; the SOAR is the automation machinery inside that layer. Left as a forward note for the soc-platform pass.
7. **vs generic workflow automation platforms** (no directory leaf — n8n/Zapier/Workato-class): the deepest structural seam. The SOAR's three legs without the security orientation describe exactly this product class. The observed differentiator is the security-operations substrate: purpose-built security-tool connector libraries, security-signal triggers, response-action vocabulary, and security use-case content economies (all evidenced above). Self-descriptions confirm the products police the seam themselves ("general purpose **security** automation platform" — Shuffle). The seam is a gradient, not a wall: some products deliberately generalize beyond the SOC. Recorded as a boundary note, not a taxonomy conflict, because the directory has no leaf for the generic class.
8. **vs Robotic Process Automation** (§10): RPA automates through application UIs across arbitrary business software; SOAR automates through APIs/tool actions of security software. Different substrate, overlapping marketing vocabulary ("orchestration/automation").
9. **vs Agent Orchestration Platform / §13 AI-agent machinery**: SOAR playbooks are deterministic authored programs over tool APIs; AI-agent orchestration centers on delegating work to autonomous agents. AI-assisted playbook authoring (text-to-playbook) is an authoring aid inside SOARs, not a Type change. Watch-item only.

## Uncertainties

1. Tines unreachable — the "automation-first, no-SIEM-heritage" pole is inferred structurally from Shuffle's general-purpose self-description; no Tines-specific claims made anywhere.
2. Swimlane evidence limited to the docs root; its deeper mechanics (trigger types, record model, connector credentials) unverified.
3. Shuffle's human-approval machinery not directly observed in fetched pages (likely present per category norms — not asserted).
4. Swimlane's run-record retention not directly observed (assumed common per category, not asserted for that product).
5. Whether the market is consolidating SOAR into "unified SecOps platforms" (Splunk ES+SOAR convergence; XSIAM sibling positioning) is era-current drift; the seams above held for all sampled products as packaged today. Re-review trigger if a "unified security operations platform" leaf is added.
6. Gartner's role in coining the category label was not verifiable from primary sources in this pass; the label's market reality is evidenced via vendor self-descriptions instead.

## Final Synthesis

A SOAR is the SOC's cross-tool response automation system. Its defining core is three jointly-held structures: the tool-agnostic connection layer to the organization's security technologies (named connector objects holding credentials and exposing actions); the playbook/workflow as a persistent re-editable automation program (trigger + branching steps + actions across those tools, optionally with human-approval gates); and the triggered, recorded run (security signals or manual invocation fire executions whose steps and results are retained and inspectable). Everything else commonly associated with the category — case management, event intake pipelines, marketplaces, SLA machinery, AI authoring — is embedded packaging or common mature structure, realizable at different depths or in neighboring systems (the SIEM's case object, the CIRP's case core) without changing the Type. The defining seams: SIEM = analytics over event data, SOAR = orchestration across tools; CIRP = the incident case under managed response, SOAR = the automation loop; XDR = response through own instrumentation, SOAR = response across the customer's toolset; generic workflow automation = the same machinery without the security-operations substrate.
