# Research Notes — IT Change Management

## Research Goal

Understand, from real products, what an IT Change Management application is: its core objects, how the change governance loop actually runs, which structures are definitional versus common implementation, and where its boundaries sit against the neighboring IT-service types (ITSM suite, CMDB, Release Management, Deployment Management, Approval Workflow, Configuration Management, Incident/Problem Management).

## Initial Boundary

Hypothesis before research:

- IT Change Management = the IT organization's governance system for changes to its IT infrastructure and services: a managed record (change request / RFC) assessed for risk and impact, authorized by a designated authority, scheduled, implemented, and reviewed.
- Nearest types: ITSM (suite context), CMDB (the record changes act upon), Approval Workflow Platform (generic machinery), Application Deployment Management (executes changes), Configuration Management tooling (enforces state), Release Management (coordinates groups of changes), Incident/Problem Management (upstream/downstream loops).
- Easy confusions: the word "change" (change data capture, engineering change management, regulatory change management are different domains); "change management" also names organizational change management (a people-process discipline, not this software type).

## Research Questions

1. What is the central record, and what does it carry?
2. Which change classifications exist (standard/normal/emergency, minor/major) and how do they alter the flow?
3. How does risk/impact assessment work operationally?
4. Who authorizes, through which structures (change manager, CAB, ECAB, peer review, automation)?
5. How is scheduling handled (change calendar, maintenance windows, freeze periods, conflict detection, forward schedule of changes)?
6. How is implementation coordinated (tasks, rollout/backout plans, verification)?
7. What happens at closure (post-implementation review, outcome classification, feedback into the change model)?
8. What integrations matter (CMDB/assets, incidents, problems, requests, CI/CD pipelines)?
9. Which interfaces exist (queue, form, calendar, approval surface, dashboards, admin configuration)?
10. What rules constrain behavior (authorization tiers, emergency bypass, freeze windows, mandatory backout plans, unauthorized-change policy)?
11. How does the DevOps-oriented philosophy (decentralized authority, pipeline-linked changes, peer review) differ from the ITIL-classical philosophy?
12. Would older / paper-era / differently positioned products still fit the candidate definition?

## Representative Products

Selected for market representation, documentation quality, different philosophies and customer tiers:

| Product | Positioning | Tier of evidence captured |
|---|---|---|
| ManageEngine ServiceDesk Plus | ITIL-heavy unified ITSM suite, SMB→enterprise, on-prem + cloud | Rich (feature page, change-risk-assessment how-to guide, ITIL process whitepaper page) |
| Jira Service Management (Atlassian) | DevOps-oriented, mid-market, cloud-first; ITIL-adaptable | Rich (official ITSM practices page incl. product-specific flow guidance) |
| SolarWinds Service Desk (ex-Samanage) | Cloud ITSM suite, SMB/mid-market | Moderate (product page) |
| ServiceNow Change Management | Enterprise ITSM leader | NOT CAPTURED (see Sources) |

ServiceDesk Plus doubles as the ITIL-classical philosophy pole; Jira Service Management as the high-velocity / decentralized-authority pole.

## Sources

Captured (all official vendor surfaces):

1. ManageEngine — ServiceDesk Plus change management feature page — https://www.manageengine.com/products/service-desk/change-management.html — 2026-09-08
2. ManageEngine — ServiceDesk Plus change risk assessment guide ("How to set up change risk assessment") — https://www.manageengine.com/products/service-desk/it-change-management/change-risk-assessment.html — 2026-09-08
3. ManageEngine — ServiceDesk Plus ITIL change management hub ("6 steps to implement a successful ITIL change management process") — https://www.manageengine.com/products/service-desk/it-change-management/ — 2026-09-08
4. Atlassian — "What is IT change management" (ITSM topics) — https://www.atlassian.com/itsm/change-management — 2026-09-08
5. SolarWinds — Service Desk product page (change management section) — https://www.solarwinds.com/service-desk — 2026-09-08

Attempted and abandoned (1–2 failures each, per access rules):

- ServiceNow: product page timed out; docs.servicenow.com served a JavaScript application shell (unusable). Two attempts.
- Freshservice: support article 404; alternative path 404. Two attempts.
- BMC change management page: 404. One attempt.
- InvGate: 490. One attempt.
- TOPdesk: 404. One attempt.
- SolarWinds change-management use-case deep page: 404 (product page captured instead).

Source-access limitation: no enterprise-suite pole (ServiceNow/BMC) and no second mid-market SaaS pole (Freshservice) with live documentation. Enterprise-only mechanics (e.g., ServiceNow change models/velocity features) are NOT asserted anywhere in this research. Claims are calibrated to the captured sample; broader-market claims use "mature products commonly" wording, and cross-product claims rest on 3 products, not 5.

## Product A — ManageEngine ServiceDesk Plus

### Key observations (evidence layer A unless noted)

Feature page:

- Framing: "Minimize risks and maximize the probability of success of your IT changes"; avoid "change-led outages, collisions and downtime."
- **Change logging with context**: "Log changes with all the contextual data needed, along with comprehensive rollout, backout and implementation plans."
- **Change calendar**: plan changes and releases; "change freeze and maintenance windows"; freeze windows for "holiday seasons, audits"; both window types can be scoped to sites, services, or all changes; **conflict detection** against these windows ("Configure your conflict windows, whether they're maintenance or freeze windows, to avoid change-based conflicts").
- **Change templates**: drag-and-drop fields, form rules, "stage specific sections", associate change roles and CABs to templates.
- **Change types / customization**: "Categorize changes according to your business needs under change types. Set up Closure Codes for changes as well as custom stages and statuses."
- **Stages**: FAQ lists stage examples "submission, planning, approval, implementation, user acceptance testing, release, review, and closure"; workflows "break down changes into eight stages, with customizable statuses within each stage" (stage count is product-specific configuration, not an industry constant).
- **Change roles**: predefined + custom roles "with fine-grained access permissions", associated to named users; granular access.
- **CABs**: "Configure CABs to help loop in the right stakeholders for approval, including requesters and technicians"; keep them updated as changes progress; "Pre-approve changes wherever needed."
- **Risk**: manual risk values, business rules auto-classification, or a **change risk questionnaire** that computes risk; Zia AI risk prediction trained on historic change data (AI is product-specific).
- **Visual workflow builder**: separate unique workflows for "standard, emergency, and critical changes"; automated notifications, approvals, timers, field updates; multi-path orchestration.
- **Associations**: "Associate changes with incidents, problems, and requests"; CMDB relationships give "an integrated view of the IT assets and services impacted by the change"; example scenario ties incident tickets → problem ticket → change ticket → service request/purchase order.
- **SLAs** attachable to change sites/templates.

Change risk assessment guide (operational depth):

- CRA = "a structured questionnaire that helps you identify and evaluate potential risks associated with any kind of addition or modification to your IT systems", weighting factors such as historical success rate, number of stakeholders, level of testing.
- Example questionnaire fields (vendor example, not defaults): number of teams involved, prior experience/success, level of testing, expected service outage, reversal time.
- Implementation machinery: additional fields → change template section → custom module as scoring reference table → triggers + custom function computing composite score → risk level written to the change record (vendor example bands: None/Minimal, Low, Medium, High, Critical with numeric thresholds — vendor-specific illustration).
- Risk drives "checks and balances": "additional layers of approvals, conditional checks, or CXO notifications."

ITIL process whitepaper page (vendor educational content — cross-checks the practice model):

- Change definition: "The addition, modification, or removal of anything that could have an effect on IT services."
- Change model with FIVE levels (product's educational version): Standard / Minor / Normal / Major / Emergency — explicitly "can be adapted to suit your organization"; standard changes "do not generate Request for Changes"; minor changes approved by change manager without CAB; normal changes convene CAB; major changes escalate to higher change authority; emergency changes handled by **ECAB** with streamlined process and post-hoc comprehensive testing.
- **Roles**: Change Manager (reviews RFCs, schedules CAB meetings, authorizes, updates records, coordinates build/test/implementation, reviews implemented changes, reports); **Change Authority** tiered by size/cost/risk (line manager → change manager → CAB+change manager → director/C-level/board); **CAB** (assesses from "business, technical, and financial viewpoint", flexible membership); **ECAB** (smaller core group, short notice, power to decide without escalation).
- **Process**: Record (RFC) → Review (change manager as gatekeeper: valid, specific, beneficial, feasible, necessary) → Assess (costs, resources, benefits, risks incl. service impact; plan execution incl. **back-out procedure**) → Authorize (escalate per type; authorized change added to the **Forward Schedule of Changes (FSC)**) → Coordinate implementation (build, testing, implementation "in the right manner and at the right time as agreed and published in the FSC") → Evaluate and close (**Post Implementation Review (PIR)**: objective achieved? side effects? costs/downtime overruns?; lessons fed back; potential demotion to standard change for next time).
- Rules stated: change management + configuration management interlock ("change management needs a view of the infrastructure to assess the impact... Configuration management needs changes to be recorded, so that the CMDB is kept up-to-date"); policy prohibiting unauthorized changes; "Don't implement any change without a back-out plan"; test changes/backout in a sandbox; unknown-risk changes mapped UP the model as precaution.
- **KPIs**: successful changes, failed changes rolled back, backlog, incidents caused by change, emergency/out-of-hours changes, unauthorized changes identified, resources/funds spent, FSC adherence percentage.

## Product B — Jira Service Management (Atlassian)

### Key observations (evidence layer A for the practices content; the page mixes general practice guidance with JSM-specific claims)

- Definition: "Change management—also known as change enablement—is an IT practice designed to minimize disruptions to IT services while making changes to critical systems and services." A change is "adding, modifying, or removing anything that could have a direct or indirect effect on services."
- "How Jira Service Management helps: Supports standard, normal, and emergency change workflows with automation, CAB collaboration, and integrations to CI/CD tools."
- **Three change types**: Standard (low-risk, commonly repeated, pre-approved, documented process; prime automation opportunity); Normal (non-emergency without pre-approved process; high-risk ones need risk assessment + CAB, low-risk ones quick approval); Emergency (must be handled on a much tighter timeline; risk of lengthy review outweighed by urgency; examples: security patch, server outage, major incident).
- **CAB**: traditional CAB "tasked with assessing the risks of and approving (or not approving) each change"; can become a bottleneck; many teams move away or restrict scope to riskiest changes; modern framing: CAB as "trusted advisors".
- **Philosophy pole**: ITIL 4 encourages decentralizing change authority "into the business stakeholder or peer level"; automation, virtual checklists, and **peer review** as nimbler alternatives; process "shifting—away from lengthy reviews and non-technical stakeholder approvals and toward automated, collaborative processes between IT and development teams."
- **Six-step process** (practice template): Change request (requester includes risks, implementation notes, affected systems) → Change request review (change manager or peer reviewer) → Change plan (expected outcomes, resources, timeline, testing requirements, **roll back** path) → Change approval (change manager / peer reviewer / CAB) → Change implementation (ship the change, document procedures and results) → Change closure (change manager reviews and closes; report covers success, timeliness, estimate accuracy, budget).
- Self-service portal for raising standard change requests; workflow automation routes "to the next authorized person based on your business rules"; knowledge-base templates for change plans; DevOps-driven release framing.

## Product C — SolarWinds Service Desk

### Key observations (evidence layer A, moderate depth)

- Change Management listed as a core service-management use case alongside Incident, Problem, Release — suite-module packaging.
- Value framing: "Structured change processes to minimize risk and maximize stability."
- Three product-specific capabilities: **Structure** ("Centralized documentation, approvals, and process for proper changes"); **Audits** ("Maintain a history of all changes in the event a rollback or audit is needed"); **Impact** ("Asset connections drives deep understanding of change request dependencies").
- CMDB section: "Impact analysis: Understand change impact based on asset dependencies" — cross-confirms change↔CMDB linkage as standard.
- Screenshot reference to a "Change Catalog Process" (pre-approved catalog concept; page text does not elaborate — treated as unverified beyond its existence).

## Cross-product Comparison

| Dimension | ServiceDesk Plus | Jira Service Management | SolarWinds Service Desk | Reading |
|---|---|---|---|---|
| Central record | Change ticket with template-driven contextual data, rollout/backout/implementation plans | Change request→record through 6-step flow; plan incl. rollback path | Change request with centralized documentation | B — universal |
| Change classification | 5 educational levels (standard/minor/normal/major/emergency); product workflows per type | 3 types (standard/normal/emergency) | not detailed | B at the standard/normal/emergency core; finer gradations are variant |
| Risk/impact assessment | Questionnaire-based scoring + rules + AI prediction; drives approval depth | Review step assesses likelihood/success; risk-aware approval | Via asset/CI dependency connections | B — form varies, function universal |
| Authorization structure | Tiered change authority; CAB; ECAB; pre-approval for standard | Change manager / peer reviewer / CAB; decentralization encouraged | Approvals as part of structured process | B — structure exists everywhere; composition varies by philosophy |
| Scheduling | Change calendar + freeze/maintenance windows + conflict detection; FSC concept in whitepaper | not detailed on captured page | not detailed | A (single-product rich); calendar treated as common but not definitional |
| Implementation tracking | 8 configurable stages incl. UAT/release; task coordination by change manager | implementation step with documented procedures/results | process for "proper changes" | B — lifecycle universal; stage count/names variant |
| Backout/rollback | Rollout + backout plans as first-class content | rollback path in change plan | history "in the event a rollback or audit is needed" | B |
| Closure & review | Closure codes; PIR in educational model; feedback loop (demote to standard) | closure report by change manager | audit history | B — review/closure universal; PIR formality varies |
| CMDB/asset linkage | CMDB relationships for impacted assets/services; explicit change↔config interlock | not on captured page (Assets elsewhere) | asset connections drive impact understanding | B (2 products + CMDB sibling pass) |
| Associations | incidents, problems, requests, releases, projects | dev-team collaboration, CI/CD tool integrations | incidents (asset-incident correlation) | B |
| KPIs | success rate, rolled-back failures, backlog, change-caused incidents, unauthorized changes, FSC adherence | change metrics/KPIs mentioned | not detailed | B |
| Philosophy | ITIL-classical, control-first, tiered authority | high-velocity, decentralized authority, peer review, CI/CD-linked | pragmatic mid-market suite | C — two recognizable philosophy poles |

## Canonical Model (working)

Three jointly-held structures:

1. **The change request as the managed record of record** — a persistent, individually identified record of a proposed addition/modification/removal affecting the organization's IT environment, carrying the change's content (what, why, scope), its assessed risk and impact, affected configuration items/services, and its implementation + backout plan.
2. **Pre-implementation authorization gated by assessed risk** — the record cannot proceed to implementation until a designated authority (person, board, or pre-approval policy keyed to change type) authorizes it; the depth of assessment and the level of authority scale with assessed risk.
3. **The governed lifecycle carried to a reviewed outcome** — the record moves through defined states (requested → assessed → authorized → implemented → reviewed → closed), implementation is coordinated and recorded, the outcome is classified (successful / failed / rolled back), and review results feed back into future change handling.

Remove test:
- 1 alone = a task/ticket tracker.
- 2 alone = generic approval machinery.
- 3 alone = a form plus a status column.
- 1+2 without 3 = approval workflow with no implementation/review loop.
- 2+3 without 1 = coordination with nothing governed.
- 1+3 without 2 = change *tracking* / activity log, not change *control*.

## Abstraction Hierarchy

### L0 — Defining Invariant

1. Change request as persistent managed record of a proposed IT modification (with its assessed risk/impact and implementation intent).
2. Risk-gated pre-implementation authorization by a designated change authority.
3. Governed lifecycle to a reviewed, closed outcome (implementation recorded, outcome classified, history retained).

Historical check (§24-style): paper-era change control — change request form → change board assessment → authorized entry on the schedule of changes → implementation sign-off → post-implementation review minutes — satisfies all three legs. ITIL v2/v3 era suites satisfy. So no modern machinery (calendar UIs, CMDB, AI, CAB software) is inside L0.

### L1 — Common Mature Structure

- Change type/model classification (standard / normal / emergency core; minor/major gradations vendor-dependent) routing process depth and authority level.
- Change Advisory Board (CAB) and emergency counterpart (ECAB); tiered change authority.
- Change calendar with maintenance windows and change-freeze periods; conflict detection; forward schedule of changes as a published plan of authorized changes.
- Implementation decomposition into tasks/stages; rollout and backout plans as first-class record content.
- CMDB / asset linkage for impact analysis; association with incidents, problems, requests, releases.
- Templates (change templates per type), workflow automation (approvals, notifications, routing).
- Audit history of every record action; KPI reporting (successful/failed changes, change-caused incidents, unauthorized changes, schedule adherence).
- Requester intake (portal/form) and requester visibility.
- Post-implementation review as a recognizable step; closure codes/outcome classification.

### L2 — Variant / Optional Structure

- Risk-scoring machinery depth: questionnaire builders, weighted scoring tables, rules-based auto-classification, AI risk prediction.
- Philosophy pole: decentralized authority — peer review, pipeline-linked changes, CI/CD evidence in place of board approval (DevOps posture).
- Pre-approved change catalogs (standard changes executed as catalog-like automated workflows).
- Suite-module vs dedicated-practice packaging; on-prem vs SaaS; SMB vs enterprise tuning.
- Segregation-of-duties specifics (who may not authorize what), CXO notifications for high risk.
- Stage vocabulary (5 vs 8 stages; UAT/release stages; stage/status customization).
- SLA attachments to changes; freeze-window scoping granularity (site/service/global).

### L3 — Vendor-specific (research notes only)

- ServiceDesk Plus: Zia AI risk prediction and Zia Workflow Assist (GenAI workflow builder); 8-stage default; change roles object; custom-module-based CRA scoring with example bands (None/Minimal→Critical at 8/16/24/31 in the guide's illustration); five-level educational change model; local-manageengine domain variants.
- Atlassian: six-step practice playbook; "CAB as trusted advisor" re-framing; kick-off playbook/knowledge-base-template integration; "70% of standard changes can be automated" attributed statistic (third-party claim relayed by vendor — not asserted as fact).
- SolarWinds: "Change Catalog Process" screenshot reference (unelaborated); ex-Samanage heritage; competitor-comparison pages.
- ServiceNow: none captured (source inaccessible) — deliberately no claims.

## Vendor-specific / Rejected Findings

- Rejected as definitional: change calendar, CAB, CMDB linkage, AI risk scoring, stage counts, freeze windows, PIR formality — all common or variant, none survives the "remove → stops being the Type" test (paper-era change control lacks the calendar UI, CMDB, and AI while remaining recognizably IT change management).
- Rejected: "change management = approval workflow with IT words." The authorization leg is necessary but not sufficient; without the change record and the governed lifecycle, the sample products stop being change management.
- Rejected: the five-level change model as a constant (Atlassian documents three levels; ServiceDesk Plus markets three workflows and teaches five; gradations are organizational configuration).
- Name-collision guard: this Type is unrelated to Change Data Capture, Engineering Change Management (different domain record), Regulatory Change Management, or organizational/people change management.

## Boundary Findings

- **vs ITSM (suite)**: change management is one practice/module inside ITSM suites (SolarWinds lists it beside incident/problem/release; ServiceDesk Plus markets a "Change module"). The suite's center is the service desk + incident/request estate; the change practice's center is the governed modification loop. A suite minus change governance is still ITSM; change governance without the service desk exists as a practice area inside the suite. Keep as separate Type; note suite-module packaging as variant. (ITSM leaf unprocessed — coordinate.)
- **vs CMDB** (processed 2026-09-07): CMDB = authoritative record of what exists (CIs + relationships). Change management = governed progression of modifications to that environment. The interlock is explicit in two sampled vendors: change needs the infrastructure view for impact; the CMDB needs change records to stay current. Change reads the CMDB; CMDB is updated through/because of changes. Remove the governance loop from a change product → CMDB + tickets; remove the CI record → change governance still runs (weaker impact analysis). Seam holds; direction of dependency recorded.
- **vs Approval Workflow Platform** (processed 2026-09-06): generic submitted-request → routed decisions → recorded outcomes, domain-agnostic. Change management embeds an authorization leg but binds it to a domain record (IT change), risk scaling, scheduling, implementation tracking, and outcome review. Approval machinery is a component, not the Type.
- **vs Application Deployment Management** (processed 2026-09-06): deploys packages to endpoint populations and tracks execution — it *executes* a class of changes. Change management *authorizes and records* changes regardless of executor (human tasks, deployment tools, pipelines). Its governance/approval layer there is L2; here governance is the core.
- **vs Configuration Management** (processed 2026-09-07): config-management tooling declares desired state and converges infrastructure automatically — it performs changes at machine level. Change management governs them at process level (assess/authorize/schedule/review). The configuration pass already flagged this name-collision seam; this pass aligns: enforcement-of-state vs governance-of-modification.
- **vs Release Management Platform** (unprocessed): releases bundle changes/deployments into coordinated delivery vehicles; change management governs each modification individually. Expected seam: aggregation-and-coordination vs per-change authorization/record. Flag for the release pass to treat research/it-change-management.md §Boundary Findings as counterparty.
- **vs Incident Management** (processed 2026-09-08): restore-response loop over declared service disruptions vs governance of planned modifications. Bridge: incidents trigger emergency changes; change-caused incidents are a shared KPI. Different records, different loops.
- **vs IT Problem Management** (unprocessed): root-cause elimination loop; changes are one remedy output of problem resolution (ServiceDesk Plus explicitly links problem → change). Flag for the problem pass.
- **vs Patch Management** (unprocessed): patch tooling executes a recurring change class at fleet scale; in change-governance terms patch deployments commonly ride the standard/pre-approved path. Expected module-vs-governance seam; flag for that pass.
- **vs Engineering Change Management** (§16 sibling, unprocessed): identical governance grammar (request → impact assessment → authority approval → implementation → review) over a different record base (product/BOM engineering data, ECO/ECN). The IT binding (infrastructure/services, ITSM context, service-impact language) is what makes this Type IT. Flag for that pass.
- **Taxonomy note**: "change management" is a heavily reused market label across ITSM, DevOps (change velocity/automation), and other domains; the software Type is defined here by its record+authorization+lifecycle core, not by the label.

## Uncertainties

- Enterprise-suite pole (ServiceNow, BMC) uncaptured: whether enterprise products carry structurally different machinery (e.g., formal change models as configurable objects, automated conflict/impact computation at depth) is unverified. Assertions deliberately avoid enterprise-specific mechanics.
- Freshservice / mid-market SaaS second pole uncaptured: the "3-type vs 5-type" distribution across the market is sampled at only 2 products on this dimension.
- Jira Service Management's in-product change calendar and conflict machinery were not verified on this pass (practices page only); calendar is held as "common" on single-product-rich evidence (ServiceDesk Plus) plus market expectation — wording kept at "mature products commonly".
- SolarWinds "Change Catalog Process" existence beyond the screenshot label is unverified.
- Whether the change calendar/freeze machinery is universal or suite-tier-dependent in lower-tier products is unverified.

## Final Synthesis

IT Change Management is the IT organization's governance system for modifications to its own IT environment. Its defining core is the joint presence of: (1) the change request as the persistent managed record of a proposed modification with its assessed risk/impact and implementation intent; (2) pre-implementation authorization gated by that assessment and granted by a designated change authority whose elevation scales with risk; (3) a governed lifecycle carried to a reviewed, closed outcome with implementation recorded and results classified. Everything else the market associates with the category — change types, CAB/ECAB, change calendars and freeze windows, CMDB-driven impact analysis, task decomposition, rollout/backout plans, templates, automation, audit trails, KPIs, AI risk prediction, pipeline-linked DevOps change flow — is common mature structure or variant, not definition. The Type realizes two philosophy poles in the sample: control-first ITIL-classical (tiered authority, CAB, calendar) and high-velocity decentralized (peer review, CI/CD-linked change records); both satisfy the same three-legged core, which is the strongest signal that the core is the Type.
