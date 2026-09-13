# Research Notes — Enterprise Risk Management (ERM)

Research date: 2026-09-06

## Research Goal

Understand what an Enterprise Risk Management application actually is as a software type: its central objects, the workflows around them, the roles involved, and the boundary against neighboring types (GRC Platform, Operational Risk Management, Third-Party Risk Management, Business Continuity, Financial Risk Management, Internal Audit).

## Initial Boundary (hypothesis before research)

- ERM software is expected to be an organization-wide system of record for identified risks: a risk register with owners, standardized likelihood/impact scoring, response/treatment tracking, and executive/board-level aggregated reporting.
- Likely sold in the current market mostly as a module/solution inside broader GRC / IRM / RMIS platforms.
- Nearest confusions: GRC Platform (suite vs application), Operational Risk Management (process/loss-level vs enterprise-level), Third-Party Risk (vendor-scoped), Business Continuity (disruption plans), Compliance Management (obligations).
- Unknowns: exact lifecycle of a risk record, role model, how assessment campaigns work, how deep control/loss-event linkage goes, whether "enterprise aggregation" is definitional or only a common feature.

## Research Questions

1. What is the central object, and what fields does a risk record carry?
2. How does standardized assessment work (scales, inherent/residual, re-assessment rhythm)?
3. How is accountability modeled (owners, review/approval, delegation to front line)?
4. How are responses/treatments recorded and tracked (mitigation plans, linked controls)?
5. How does enterprise roll-up work (org-entity scoping, heat maps, board reporting)?
6. What roles use the system (risk program owner, risk owner, assessor, executive)?
7. What adjacent objects do ERM systems link to (controls, incidents/losses, KRIs, policies, vendors)?
8. Where is the boundary vs GRC Platform / ORM / TPRM / BCM?
9. What varies by segment (suite vs standalone, SaaS vs on-prem, SMB vs Fortune 500)?
10. Historical check: would pre-2010 or regional register-style ERM still fit the definition?

## Representative Products

| Product | Positioning | Why selected |
|---|---|---|
| Archer (Archer IRM) | Enterprise GRC platform pioneer, large-enterprise / Fortune 500 tier | Defines the "one register, one taxonomy" enterprise pattern; explicit ERM use-case page |
| LogicGate Risk Cloud | Mid-market → enterprise, no-code workflow/agentic GRC platform | Different philosophy: ERM as configurable workflow application, AI-agent first-pass |
| Riskonnect | Integrated risk suite with RMIS/insurance heritage, mid-to-large | Different heritage: RMIS + claims + continuity; ERM product with explicit register/heat-map language |
| LogicManager | SMB / mid-market SaaS, taxonomy-driven ERM methodology | Different customer tier; partial evidence only (see Sources) |

Rejected/abandoned: ServiceNow IRM (two fetch timeouts), MetricStream (403), IBM OpenPages docs (403). Recorded as source-access limitations; no memory-based detail filled in.

## Sources

- Archer — https://www.archerirm.com/enterprise-operational-risk (Enterprise & Operational Risk use-case page), https://www.archerirm.com/ (root). Fetched 2026-09-06. Layer A.
- LogicGate — https://www.logicgate.ai/solutions/enterprise-risk-management/ , https://www.logicgate.ai/platform/applications/enterprise-risk-management-application/ , https://www.logicgate.com/ (root), https://help.logicgate.com/ (help-center category structure). Fetched 2026-09-06. Layer A (marketing/help-structure level; no deep KB articles fetched).
- Riskonnect — https://riskonnect.com/solutions/enterprise-risk-management/ (ERM software page incl. FAQ). Fetched 2026-09-06. Layer A (product page level).
- LogicManager — https://www.logicmanager.com/erm-software/ (resolved to a 2012 blog post + site navigation). Fetched 2026-09-06. Layer A- (positioning/nav only: platform pages named Risk Identification & Assessment, Risk Mitigation, Risk Monitoring, Risk Reporting, Risk Taxonomy, Task Management & Programs; methodology quote about assessing risk at the front line and aggregating to the board).

Source-access limitation: deep help-center articles (Archer Community KB, LogicGate KB articles, LogicManager University, ServiceNow docs, MetricStream, IBM OpenPages docs) were not reachable from the research environment on 2026-09-06. All workflow claims below are calibrated to product-page/help-structure evidence; precise numeric limits, exact state names, and default settings are not asserted anywhere.

## Product Observations

### Archer — Enterprise & Operational Risk (archerirm.com)

Key observations (Layer A, product-page level):

- Positioning: "Answer the board's risk question the day they ask it"; the problem framed as each unit rating risk its own way vs "they all rate against one scale you can defend" → shared scale/taxonomy across units is the headline value.
- "One register ends the translation": enterprise risk register where "every risk, by owner and by unit"; benefits list includes "Enterprise risk register — every risk, by owner and by unit".
- Risk record fields named on the page: "Capture impact, likelihood, owner, and status for each risk, then link the controls that mitigate it. The register shows coverage instead of a list of worries."
- Taxonomy: "One taxonomy, defined once. Define enterprise risks and the intermediate risks beneath them." FAQ recommends a two-level risk taxonomy (enterprise risks + intermediate risks). Requirement to start: "a list of business units with owners."
- RCSA campaign workflow: "Scope by unit or process, generate an RCSA for each, and route it automatically… The plant manager confirms what still applies… Your team reviews and approves, and Archer snapshots the result."
- KRI/indicator management: "Set red and amber thresholds, numeric or qualitative, and Archer tasks the metric owner on the frequency you choose."
- Loss event intake: "anyone can log a loss event for root cause and impact analysis… link the event back to the risk and the control involved"; intake from employees outside the product via a shared form link ("Archer Engage form").
- Aggregation/reporting: "nightly snapshots and tracked thresholds"; "Snapshots show how a rating moved since last cycle"; "Risk and loss dashboards — prebuilt views for managers and the board"; customer quote: "Risk aggregation is a big point… to give greater visibility for boards and executives."
- Custom rating scales: "Can we keep our own impact and likelihood rating scales? Yes. Changing the rating factors is a primary feature."
- Framework alignment (FAQ): built on COSO for ERM, ISO 31000 for assessment method, NIST RMF, Basel II for operational risk.
- Suite context: ERM sits in a GRC platform alongside compliance, policy, audit, third-party, resilience, IT risk applications; customer quote stresses cross-application connections and audit trail ("Archer is the source of truth, and it creates a nice audit trail").

### LogicGate Risk Cloud (logicgate.ai)

Key observations (Layer A, product-page + help-center structure level):

- ERM is sold as a "solution" and as a preconfigured "ERM Application" on the Risk Cloud platform; the platform philosophy is no-code workflow applications over a connected graph database ("connects compliance controls, assets, and risks… multi-hop view of how everything relates").
- Centralized risk data: "A unified database stores all risks, assessments, and strategies, facilitating streamlined tracking, reporting."
- Risk-to-objective linkage: "connects risk to business objectives… Connect enterprise and operational risks to business objectives to measure and mitigate their impact."
- Assessment mechanics: "pre-configured risk scoring and guidance"; "Generate clear visual reports of residual risk and quickly initiate mitigation activities with just a few clicks" → residual risk and mitigation initiation are named surfaces.
- Owner-facing adoption: "Empower risk and control owners… with role-based dashboards, automatic notifications, and easy-to-complete forms"; humans are "the final approvers".
- KRI monitoring: "Continuously monitor SLAs and Key Risk Indicators (KRIs)"; "automatically assigning Key Risk Indicators (KRI) to be measured regularly."
- Reporting: "Generate board-ready reports"; executive dashboards; trend identification.
- AI agents (emerging, vendor-specific flavor): Intake Agent (pre-fills intake records, triages risks across domains, routes for assessment), Assessment Agent (evaluates against the defined risk framework, populates fields with rationales, identifies control gaps, creates linked mitigation records), Insights Agent (executive reports, chat experience, flags risks needing attention). All with "complete audit trail"; framed as first-pass automation with human judgment on top.
- Cross-application linkage (FAQ): link risk assessments in ERM with controls from the Controls Compliance application; suite spans cyber risk, TPRM, policy, audit, ESG, AI governance.
- Help-center structure (Layer A-): categories confirm object vocabulary — Applications (workflow containers), Key Concepts & Terms, Risk Cloud Content, Admin Resources (building/managing applications), End User Resources (completing work and viewing reports).

### Riskonnect ERM (riskonnect.com)

Key observations (Layer A, product-page + FAQ level):

- Product highlights list (their own vocabulary): Dashboards ("status of risks and other key indicators – including customizable KRIs and KPIs"), Heat Maps ("meaningful visualization of your assessed risks to… prioritize actions"), Incident Management (capture at the source; separate module), Risk Assessments ("collect critical business threat information… automated tools"), Risk Hierarchy ("organize your risk data… by category, location, business unit, or custom configuration"), Risk Register ("build your organization's risk profile… easily share the information with stakeholders or auditors"), Risk Analytics and Insights.
- Connections: "See the connections between risks, controls, assessments, accountability, documentation, and other relevant factors."
- KRI thresholds: "Get automatic alerts when a risk indicator has crossed the threshold of acceptability"; "Monitor important KRIs and respond to oncoming risk events in real time."
- Accountability: "assign responsibility and accountability for identifying and managing risk in everyday work"; "Establish a common risk language throughout the organization."
- Executive framing: "Give leadership reliable, accurate data instantly"; "Empower the C-suite to make effective decisions about risk and opportunity"; front-lines-to-C-suite communication.
- FAQ definition of ERM: "a structured, organization-wide approach to identifying, assessing, and responding to the full spectrum of risks that could affect strategic objectives."
- ERM software vs spreadsheet boundary (FAQ): "A spreadsheet or static risk register can capture a list of risks, but it can't tell you when something has changed, who owns the response, or how one risk connects to others… ERM software automates data collection, flags changes to key risk indicators in real time, and surfaces the relationships between risks, controls, and accountability… a living risk profile rather than a periodic snapshot."
- GRC context (FAQ): "it sits within a broader GRC framework that connects risk management, compliance obligations, internal controls, and audit activities."
- Suite context: sibling modules — RMIS, claims, business continuity & resilience, compliance, TPRM, internal audit, internal controls, policy management, project risk ("Active Risk Manager"), AI governance; "start anywhere, expand everywhere" modular model.

### LogicManager (logicmanager.com) — partial evidence

Key observations (Layer A-: site navigation + one blog post; product pages not fetched):

- Platform navigation names the ERM loop explicitly: Risk Identification & Assessment → Risk Mitigation → Risk Monitoring → Risk Reporting; plus "Risk Taxonomy" and "Task Management & Programs" as platform pages.
- Methodology quote (2012 blog, founder): "The goal of every ERM program is to assess material risk down to where the risk activity takes place… front line management, and aggregate this information to an objective, accurate, and holistic picture applicable for each stakeholder, including the board." → the front-line-assess + enterprise-aggregate loop as the core promise.
- Solution taxonomy spans enterprise risk, security risk, third-party risk, audit, regulatory compliance, business continuity, model risk, EHS, operational loss → same GRC-suite pattern; ERM is one solution area.
- Board-facing resources ("Presenting ERM to the Board") consistent with executive-reporting orientation.
- No product-page detail on record fields/states fetched → all LogicManager-specific mechanics remain unverified; used only for cross-product loop confirmation.

## Cross-product Comparison

| Structure / capability | Archer | LogicGate | Riskonnect | LogicManager | Evidence |
|---|---|---|---|---|---|
| Central risk register (org-wide system of record) | ✔ "one register… every risk, by owner and by unit" | ✔ "unified database stores all risks, assessments, strategies" | ✔ "Risk Register… your organization's risk profile" | ✔ implied by taxonomy/aggregate loop | B — all sampled |
| Shared taxonomy / common risk language across units | ✔ "one taxonomy, defined once" | ✔ "defined risk framework" | ✔ "common risk language"; risk hierarchy by category/location/BU | ✔ Risk Taxonomy platform page | B |
| Likelihood × impact (or equivalent) standardized scoring | ✔ "capture impact, likelihood, owner, status" | ✔ "pre-configured risk scoring and guidance" | ✔ heat map prioritization "by likelihood and impact" | implied (assessment) | B |
| Named owner / accountability per risk | ✔ "Accountability, by name" | ✔ "risk and control owners" | ✔ "assign responsibility and accountability" | ✔ "accountability chain" (nav) | B |
| Recorded response / mitigation with follow-through | ✔ controls linked; coverage view | ✔ "initiate mitigation activities"; linked mitigation records | ✔ "who owns the response" | ✔ Risk Mitigation (nav) | B |
| Assessment routed to front-line owners; review/approval | ✔ RCSA campaign: scope→route→review→approve | ✔ assessments routed to owners; agents first-pass, humans approve | ✔ "track the status of risk assessments" | ✔ "assess… down to front line" | B |
| Inherent vs residual distinction | partial (snapshots; not named on page) | ✔ "reports of residual risk" | implicit (assessed risks) | unverified | B-weak |
| KRI thresholds + alerts | ✔ red/amber thresholds, tasked owner | ✔ KRIs measured regularly; SLA monitoring | ✔ automatic alerts on threshold crossing | unverified | B |
| Heat maps / dashboards / board reports | ✔ prebuilt for managers and the board | ✔ board-ready reports, executive dashboards | ✔ heat maps, dashboards, C-suite | ✔ aggregate to board | B |
| Loss/incident events linked back to risks & controls | ✔ loss event intake + root cause | incident routing on platform page (ERM page not explicit) | ✔ incident management sibling module | operational loss solution area | B-weak |
| Org-entity hierarchy scoping (BU/location/process) | ✔ scope by unit or process | implied (enterprise spans "every business unit, function") | ✔ risk hierarchy by category/location/BU | implied | B |
| Assessment cycle history / trend over time | ✔ snapshots vs last cycle; nightly | ✔ trends identified (Insights) | ✔ "living risk profile rather than periodic snapshot" | unverified | B-weak |
| Framework alignment named (COSO ERM / ISO 31000) | ✔ explicitly | ✘ not on fetched pages | ✘ not on fetched pages | ✘ not on fetched pages | A — Archer only → Optional |
| Quantitative financial exposure modeling | ✔ separate Risk Quantification product | ✔ Risk Cloud Quantify | ✘ not on fetched page | ✘ | B-weak (2 products) → Optional |
| AI agents / first-pass automation | ✔ Evolv AI positioning | ✔ ERM Intake/Assessment/Insights agents | ✘ | ✔ AI page exists (not fetched) | B-weak, emerging → Optional |
| Sold inside broader GRC/IRM/RMIS suite | ✔ | ✔ | ✔ | ✔ | B — all sampled |

## Canonical Model — Four-Layer Abstraction

### L0 — Defining Invariant (minimal)

1. **Enterprise-scoped risk register.** The system manages a persistent, organization-wide population of risk records — each describing an identified uncertain event or condition with potential impact on organizational objectives, classified in the organization's risk taxonomy, and assigned to a named accountable owner.
2. **Standardized severity assessment.** Each risk is rated on the organization's shared assessment scales (canonical pair: likelihood × impact), so ratings are comparable across business units; the shared taxonomy/scale is what makes aggregation meaningful.
3. **Recorded management response.** Each risk carries a management decision on how it will be handled (treat / accept / avoid / transfer) that is recorded in the system and pursued through it.
4. **Enterprise aggregation & reporting.** The register rolls up across organizational units into comparative enterprise-level views (heat map, ranking, top risks) used for leadership/board reporting.

Removal test: remove the register → nothing left; remove shared standardized assessment → per-silo tools, no "E"; remove response → a reporting artifact, not risk *management*; remove enterprise roll-up → an operational/process risk tool, not enterprise.

Historical check (pre-cloud, regional, spreadsheet-era ERM): a register of risks with owners, likelihood/impact ratings, treatment notes, and quarterly board heat maps fits L0 fully. KRIs, campaigns, quantification, GRC suites, AI are not needed for recognizability → correctly excluded from L0.

### L1 — Common Mature Structure (cross-product common)

- Assessment campaigns / self-assessments routed to risk and control owners (RCSA is the common instrument), with review and approval by the risk function.
- Inherent vs residual (sometimes target) scoring on the same risk record.
- Risk appetite / tolerance thresholds; flagging or escalation when a rating or indicator exceeds them.
- Mitigation/treatment plans with tasks, owners, due dates; treatment progress tracked.
- Control library linked to risks ("register shows coverage", "connections between risks, controls, assessments").
- KRI monitoring: indicators assigned per risk, measured on a cadence, with alerting thresholds.
- Loss/incident event intake linked back to risks and controls (root-cause analysis).
- Organizational-entity scoping: risks attached to business units / locations / processes; risk hierarchy.
- Lifecycle & history: assessment statuses, approval workflow, period snapshots/trend of how ratings move.
- Role model: risk program owners/administrators (define taxonomy, scales, campaigns), risk/control owners & assessors (respond, rate, mitigate), executives/board (consume reports); user-attributed audit trail.
- Dashboards/heat maps/top-risk and board reporting; document/evidence attachments; intake forms reaching people outside the core user base.
- Deliberate framework alignment surfaces (taxonomy template, assessment method) — e.g., COSO ERM / ISO 31000 named by one product; common as program scaffolding, not as software structure.

### L2 — Variant / Optional Structure

- Quantitative financial-exposure modeling (scenario/Monte-Carlo-style quantification) as a separate capability or product line.
- Depth of GRC-suite embedding: policy, compliance, audit, TPRM, BCM, ESG as sibling applications vs standalone ERM tool.
- Industry/regulatory overlays: financial services (regulatory operational-risk programs), healthcare, energy/utilities.
- Delivery & licensing: SaaS vs on-prem; concurrent vs named licensing; modular "start anywhere" packaging.
- AI assistance (agentic intake triage, first-pass assessment, report drafting) — emerging across leaders.
- Integration ecosystems (BI tools, ticketing, security platforms, HR).

### L3 — Vendor-specific (research notes only)

- Archer: Evolv Foundation/Risk packaging; two-level taxonomy recommendation; nightly snapshots; "Risk and Control Matrix" report; Engage forms; Basel II anchoring; Archer Community/Academy.
- LogicGate: Risk Cloud Applications/Workflows semantics; no-code graph database; Spark AI; ERM Intake/Assessment/Insights Agents; Config Newton; Risk Cloud Quantify; Skilljar-based learning.
- Riskonnect: RMIS/claims heritage; GoLive! implementation model; Active Risk Manager (project risk); modular "start anywhere, expand everywhere" pricing.
- LogicManager: Risk Ripple Analytics; Accountability Chain; Completeness Checker; LMX assistant; Risk Maturity Model assessment; concurrent-seat SaaS philosophy.

## Vendor-specific Findings

(See L3 above; none promoted to the canonical model.)

## Rejected Findings

- "ERM software = GRC suite": rejected as a definition. All sampled vendors sell ERM *inside* broader suites, but the ERM application itself is identifiable by the register/assessment/response/aggregation core; suite breadth is packaging, not the type.
- "ERM = operational risk management": rejected. Archer combines them in one use case; LogicGate and Riskonnect sell them separately. They share record types (risks, controls, losses, RCSA) but differ in scope/audience — see Boundary Findings.
- "Quantification (Monte Carlo / financial exposure) is core": rejected — present in two of four products as optional add-on; qualitative taxonomy-driven programs are fully viable.
- "AI agents are structural": rejected — emerging differentiator, not part of the type's stable structure.
- Precise claims (number of scale levels, default frequencies, exact status names): rejected — no deep official help-center documentation was reachable; asserting them would exceed evidence.

## Boundary Findings

- **vs Governance Risk & Compliance Platform:** GRC Platform is the broader suite (policies, compliance obligations, controls, audit, ethics). ERM is the risk-centered application within it. Test: remove compliance/policy/audit machinery → still ERM; remove the risk register + standardized assessment + enterprise roll-up → not ERM. In the current market ERM is most often a module/solution of such a platform; a standalone ERM tool is the reduced case, not a different type.
- **vs Operational Risk Management:** same building blocks (risk records, controls, RCSA, loss events) but different center of gravity: ORM is anchored on operational processes, control failures, loss events, and front-line operations; ERM is anchored on the enterprise-wide register aggregated to leadership, spanning strategic/financial/compliance/operational categories. Evidence: Archer markets them as one combined use case with RCSA as the operational mechanism inside the enterprise register; LogicGate/Riskonnect sell them as separate solutions. If the primary object is process-level losses/control testing → ORM; if it is the enterprise roll-up of top risks to objectives → ERM. Boundary is real but porous — recorded for joint review with the ORM leaf.
- **vs Third-party Risk Management:** TPRM scopes the same risk machinery to vendor/counterparty relationships and their lifecycle (due diligence, monitoring). ERM's population is organization-internal risks across all categories.
- **vs Financial Risk Management Platform:** market/credit/liquidity risk with quantitative models, specific to financial institutions; ERM is cross-category, organization-wide, mostly qualitative.
- **vs Business Continuity Management:** BCM manages disruption preparedness (BIA, recovery plans, exercises); risk feeds into it (Archer: BIA results roll into process-based RCSA) but the primary objects/plans differ.
- **vs Internal Audit Management:** audit plans and engagements provide assurance *over* risks/controls; audit consumes the register for risk-based planning but does not own it.
- **vs Compliance Management:** obligations/regulatory mapping with control linkage; risk register may link to obligations, but compliance is anchored on requirements, not risks.
- **vs spreadsheet risk register:** not an Application Type, but the software-type boundary is explicit in vendor evidence: change tracking, ownership, inter-risk linkage, automation, living profile vs static snapshot (Riskonnect FAQ; Archer's "two weeks of email" problem statement).
- **Insurance-industry "ERM":** in insurance/actuarial contexts "ERM" can denote capital/actuarial risk modeling — that belongs to Actuarial Modeling Platform / Financial Risk Management, not this type (Riskonnect's RMIS/claims lineage is likewise adjacent, not the core).

## Taxonomy note

DIRECTORY places Enterprise Risk Management under "Legal, Risk, Compliance & Governance" alongside GRC Platform, ORM, TPRM, etc. Research supports ERM as a valid standalone Type (distinct register-centric core model), with the caveat that in the live market it is nearly always delivered as a module of a GRC/IRM/RMIS platform — the Type boundary should be documented against GRC Platform and ORM (see Boundary Findings).

## Uncertainties

1. Exact risk-record lifecycle states (draft/active/closed etc.) not verified from deep official docs — stated only as "statuses and approval workflow exist".
2. Whether inherent/residual/target triads are universal — residual is directly evidenced for LogicGate, implied elsewhere; treated as common, not definitional.
3. LogicManager product mechanics unverified (nav-level evidence only) — used solely to confirm the assess→mitigate→monitor→report loop.
4. ServiceNow IRM (a market leader) could not be fetched; its inclusion could shift emphasis (e.g., workflow-platform embedding, CMDB linkage) but not the L0 core.
5. Degree of KRI universality: evidenced in three of four products at page level; treated as common mature structure, not core.
6. Approval/delegation depth (review queues, escalation matrices) varies by product; not asserted precisely.

## Final Synthesis

An Enterprise Risk Management application is the organization-wide system of record for the risks an organization manages as a whole. Its world has one center — the risk register: structured risk records, each describing an uncertain event with potential impact on objectives, classified in a shared taxonomy, owned by a named person, and rated on the organization's common likelihood-and-impact scales. Around the register run four loops: (1) identification and intake (front-line submission, campaign-based self-assessment); (2) assessment (standardized scoring, inherent/residual, review and approval by the risk function); (3) response (recorded treat/accept/avoid/transfer decision, mitigation plans, linked controls, KRI thresholds and alerts); (4) enterprise reporting (roll-up across units into heat maps, rankings, and board-ready views, refreshed through periodic re-assessment). The defining property of the type is the enterprise character: one shared taxonomy and one register across business units, so that exposure is comparable and aggregable — exactly what per-silo tools and spreadsheets cannot provide. Mature products add campaign machinery, appetite thresholds, loss-event linkage, snapshots/trends, and role-based work distribution; quantification, AI assistance, and deep GRC-suite integration are optional variants. The type's nearest neighbor is the GRC Platform, whose broader scope (policy, compliance, audit) surrounds ERM as its risk-centered core; Operational Risk Management shares its building blocks but centers on process-level losses and controls rather than the enterprise roll-up.
