# Research Notes — Organization Design Platform

Research date: **2026-09-06**
Slug: `organization-design-platform` (DIRECTORY.md §09 HR, Workforce & Talent)

---

## Research Goal

Understand what an Organization Design Platform actually is as an Application Type: what objects exist inside it, what users do with them, how the design work flows from current state to implemented change, and where its boundary sits against Org Chart Management, Workforce Planning, HRIS, and People Analytics.

## Initial Boundary (hypothesis before research)

- Hypothesis: a platform for modeling, visualizing, analyzing, and redesigning organizational structure (reporting lines, positions, spans, layers, cost), with a scenario mechanism for future states.
- Likely confusions:
  - Org Chart Management (sibling leaf) — visualization/maintenance of the current chart
  - Workforce Planning Platform (sibling leaf) — headcount demand forecasting
  - HRIS — system of record for employee data
  - People Analytics Platform — analysis of workforce data
  - Diagramming Application — static org chart drawing

## Research Questions

1. What is the core object model? Is the structure held as data (positions, people, reporting lines) or as a drawing?
2. How is the person/position distinction handled (vacancies, open jobs, FTE)?
3. What exactly is a "scenario"? How is it created, isolated, compared, approved, and applied?
4. What data does the platform consume, and from where (HRIS/HCM/ERP integration vs upload)?
5. What analysis is standard (spans & layers, cost, vacancy, gaps)?
6. How do proposed changes reach implementation (merge, write-back, export)?
7. Who uses it (central OD/HR vs line managers vs finance)?
8. Where is the boundary against Org Chart Management and Workforce Planning?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Geography |
|---|---|---|---|
| ChartHop | People-ops platform; org chart as the hub; scenarios + headcount planning + HRIS modules | SMB / mid-market | US |
| Nakisa Org Design Suite | Enterprise org design; strategic + operational tiers; write-back into SAP/SuccessFactors/Workday/Oracle | Fortune-1000 enterprise | Canada |
| OrgVue | Consulting-adjacent workforce transformation platform; work-first modeling; analyze→design→plan→monitor | Global enterprise, transformation programs | UK |
| Functionly | Self-serve interactive org design for operational leaders; drag-and-drop scenarios and change plans | SMB / mid-market, consultants | Australia |

## Sources

Tier 1 (operational documentation) and Tier 2 (official product pages), fetched 2026-09-06:

- ChartHop Help Center (Archbee docs): https://docs.charthop.com/ , https://docs.charthop.com/getting-around-in-charthop , https://docs.charthop.com/planning , https://docs.charthop.com/scenarios , https://docs.charthop.com/org-chart
- ChartHop product site: https://www.charthop.com/
- Nakisa Org Design Suite: https://nakisa.com/products/org-design-software/ ; Nakisa root: https://nakisa.com/
- OrgVue: https://www.orgvue.com/ , https://www.orgvue.com/solutions/organization-modeling/
- Functionly: https://www.functionly.com/ , https://www.functionly.com/features/scenarios-forecasts-change-planning

Failed / not fetched: `help.charthop.com` (transport error, redirected usage to docs.charthop.com), `nakisa.com/org-design/` (404; replaced by /products/org-design-software/). Nakisa product documentation portal (docs.nakisa.com) was not fetched in depth; Nakisa observations rely on the official product page and are marked accordingly.

---

## Product Observations

### ChartHop (evidence layer A — official help-center docs, directly observed)

- Positioning (product site): "People analytics and workforce planning"; modules: HRIS, Headcount Planning, Compensation, Performance, Engagement, Goals, AI Pro. Integrates with ADP, Workday, SuccessFactors, Greenhouse, Gusto, BambooHR and "100+ HRIS, ATS, and FP&A tools"; described as "the intelligence layer on top of your existing systems, not another silo".
- Core surfaces (Getting around doc): Home page, **Org Chart**, Map (location view), Employee profiles, **Data Sheet**, Dashboards, **Planning** ("propose org changes with scenarios"), mobile app (company-wide directory).
- **Scenarios doc (key evidence)**:
  - "ChartHop *scenarios* help you visualize potential changes to your organization so that you can project and analyze the costs and impact of those changes before putting them into effect."
  - A scenario is a proposal; collaborators include "leadership team members or HR business partners".
  - Scenario contents: "changes to the hiring plan, backfills, promotions, organizational structure, or all of the above".
  - Isolation: "Any changes you propose in a scenario (including new jobs, reorganization, and terminations) are contained within the scenario and only you as a scenario owner have access… Your scenario and all changes within the scenario are not visible to the rest of your organization or put into effect until the scenario is **merged to Primary**."
  - Cost header: annualized run-rate (default), fiscal-year prorated, quarter prorated; "prorated run-rate, not a full forecast".
  - Approvals: "you may be required to send your scenario for review and approval before any changes can be made official. Once a scenario has been approved, scenario changes can be merged into your organization's primary **Org Chart**."
  - HRIS conflict rule: "if you merge the changes before you have updated your HRIS the data will be overwritten in the next days sync. We recommend that you merge your scenario and change the data in your HRIS on the same day."
  - Scenario statuses: Draft, Open, In review, Approved, Rejected, Merged, Archived.
  - Scenario list filters: created by, review status, keyword.
- **Org Chart doc**: navigate departments/teams/profiles; total people + open jobs counter ("Open jobs are included in the total regardless of their recruiting status"); zoom/orientation; expansion arrows with hover preview; search jobs/people/groups; **date slider** to "view the Org Chart as it was in the past, or as it will appear in the future when new hires join"; Visualize menu (color-coded fields, e.g. Department); export/screenshot mode; "The data you see depends on your permissions."
- Data model (FAQ): built-in fields for people and job data (compensation, levels/bands, equity) plus 16 custom-field types; open REST API with read/write endpoints.

### Nakisa Org Design Suite (evidence layer A for product page claims; docs portal not fetched)

- Positioning: "enables executives, HR, finance, and line managers to align, approve, and implement org changes".
- Two tiers: **Strategic Org Design** ("plan and structure your workforce to realize your strategic vision") and **Operational Org Design** ("empowers all managers to build high-performing teams… request timely adjustments in their team structure").
- Strategic flow (product page): "Determine your organization's goals and objectives. Understand your current workforce. Analyze talent gaps and strengths. Explore and compare infinite scenarios with real-time impact analysis. Plan your optimal future workforce. Implement. Monitor. Iterate."
- Scenarios: "Create scenarios to model your organizational changes aligned with business rules to respect financial targets, respond to HR KPIs… measurable through organizational health indicators."
- Operational flow (from page imagery/labels): create proposal → share/review/collaborate → approve proposal → validate/deploy proposal.
- Metrics named: "span of control, layers, and headcount"; alignment with Finance.
- Write-back: "Write back new scenarios to your core ERP, HCM, and HRIS in a few clicks thanks to seamless integrations with SAP HCM, SuccessFactors (SFSF), Workday, Oracle, and others."
- Customer quote (OPG, Manager Org Design & Job Evaluation): org change process "could take up to 38 days… With the write-back, the end-to-end org change process now takes under 5 days."
- Portfolio structure (vendor's own split): **Org Chart Suite** (visualization) vs **Org Design Suite** (scenario modeling and design) vs **Strategic Workforce Planning Suite** (analytics and headcount planning) — three separate products under one "Workforce Planning Portfolio".

### OrgVue (evidence layer A for product/capability pages)

- Positioning: "The software platform for AI-led organizational change"; "Orgvue connects organizational design and workforce transformation".
- Platform loop: **Analyze** ("where capability gaps, cost inefficiencies, and transformation risks sit") → **Design** ("Compare multiple organizational design scenarios. Assess impact on costs, capabilities, and delivery before you commit resources") → **Plan** (skills/talent/readiness) → **Monitor** ("continuous workforce intelligence").
- Organization modeling page:
  - **Position-level modeling**: "every reporting line, role and cost is captured… Uncover hidden layers, spans and inefficiencies; Test scenarios down to individual positions; See the real cost and impact of every decision."
  - **High Level Modeling (HLM)**: "grouping people into functions, job families or grades… design and compare multiple scenarios… without needing full position data."
  - Data sheet summary: "Visualize your current state and identify areas that need attention; Model different scenarios and instantly see the financial impact; Compare the impact of design decisions and engage stakeholders."
  - "Most tools look back. Orgvue looks forward… bringing together people, cost and structure data in one platform."
- Capability list (site navigation): activity analysis, annual position planning, data harmonization, job architecture, monitoring & tracking, organization analysis, benchmarking, organization modeling, skills gap analysis, succession planning, talent intelligence, talent selection & planning.
- Roles addressed: executives, transformation team, HR, finance, IT leadership.
- Case-study metrics: "50% faster modeling across 120 countries"; "8,000 positions into 83 clusters"; 150+ upskilled OD practitioners; 170 countries impacted by a new operating model.
- Partner-delivered: "Always-on org design with Deloitte and Orgvue" (consulting-led delivery model).

### Functionly (evidence layer A for feature pages)

- Positioning: "interactive org design software for operational leaders. Plan org charts, run future scenarios, and action change plans."
- Feature groups: Data/Integrations/AI/Templates ("Visualize your org instantly and keep it updated automatically"); Groups, Dotted-lines, Accountabilities ("Map your unique organizational structures with dynamic design"); **Scenarios, Forecasts, Change Planning**; Collaboration/Sharing/Security.
- Scenarios: "Your org sandbox for bold ideas"; scenario comparison (current vs future state); per-scenario data security; scenario duplication for leaders working on separate team scenarios; change plan view ("view and export changes between your current and future scenarios"); live collaboration with version history; dynamic insights: "headcount, costs, vacancies, **span, depth**, and FTE gaps".
- Forecasts: compensation per position; compensation is "sensitive" by default ("never accessible from shared links or exports"); headcount forecast sheet; cost variance between two scenarios; budget status (actual / committed / uncommitted).
- Change planning: play-by-play change plan (variances between current and future org); **vacancy status** tracking "through the entire lifecycle of hiring from draft to occupied"; new-hire request export; position change request export; position description export.
- Insights: group calculations in the chart; group goals (headcount, FTE, total compensation); scenario summary (total positions, vacancies, unassigned people); "role cracks & gaps" (unassigned roles, positions with multiple roles); accountability gaps/overlaps.
- Use cases: restructures, workforce expansion, RIF, M&A, annual strategic planning, new executives, executive accountability, new strategic direction, preparing for org change.
- Customer quote: "invaluable to visualize hires, functions, and span of control."

---

## Cross-product Comparison

| Dimension | ChartHop | Nakisa Org Design | OrgVue | Functionly |
|---|---|---|---|---|
| Org structure as data | yes (people/jobs fields, REST API) | yes (HRIS/ERP-sourced) | yes (people/cost/structure data unified) | yes (positions, people, groups) |
| Current-state chart | Org Chart surface, time slider | Org Chart Suite (separate product) | current-state visualization | org visualization |
| Scenario mechanism | Scenarios (sandbox, merge to Primary) | scenarios, strategic + operational tiers | scenarios, position-level or high-level | scenarios (sandbox, comparison) |
| Impact metrics | cost (annualized/FY/quarter), headcount | span of control, layers, headcount, health indicators | cost, capability, delivery impact | headcount, cost, vacancies, span, depth, FTE |
| Approval flow | review/approve statuses → merge | proposal → review → approve → deploy | stakeholder engagement (consulting-led) | delegation/change plan (lighter) |
| Implementation handoff | merge to Primary + HRIS same-day sync | write-back to SAP/SFSF/Workday/Oracle | transformation program support | change plan export, new-hire/position-change requests |
| Data source | HRIS/ATS/payroll integrations | ERP/HCM/HRIS integrations | multi-source data harmonization | integrations + upload |
| Person/position distinction | people + open jobs | positions in HCM | positions central ("8,000 positions") | positions vs people, vacancy lifecycle |
| Audience | people ops + managers + finance | executives/HR/finance + line managers | transformation teams/HR/finance | operational leaders + consultants |
| AI | AI Scenario Planner, Ask ChartHop | AI platform (portfolio-level) | Henshaw companion, role clustering | OrgPilot (agent/advisor modes) |

### Cross-product commonalities (evidence layer B)

Present in all four sampled products:

1. The organization is held as **structured, queryable data** (units, positions, people, reporting relationships), not as a static drawing.
2. A **current-state baseline** of the structure is maintained and visualized.
3. A **scenario mechanism**: alternative future-state structures derived from the current state, isolated from the live baseline until applied.
4. **Impact evaluation** of scenarios — headcount/positions in all; cost/compensation in all four as well.
5. **Workforce data ingestion** from HR systems (integration or import).
6. **Spans & layers / organizational-health metrics** (span of control and layers named explicitly by Nakisa and OrgVue; span/depth/vacancy by Functionly; org analytics by ChartHop).
7. **Collaboration with controlled access** (scenario sharing, permissions, sensitive-data handling).
8. A **handoff toward implementation** (merge, write-back, or change-plan export) — form varies, presence does not.

### What varies (candidate L2)

- Modeling granularity: position-level vs aggregate (function/job-family/grade) modeling.
- Audience split: central strategic OD vs line-manager operational design.
- Implementation coupling: deep write-back into HCM/ERP vs merge-to-primary vs export-based handoff.
- Whether headcount planning / workforce planning is bundled or separate.
- Breadth: pure org design vs broader workforce-transformation platform (job architecture, skills, activity analysis).
- Delivery model: self-serve SaaS vs consulting-led enterprise program.
- AI assistance depth.

---

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

An Organization Design Platform exists only if all three hold:

1. **Organization structure as structured data** — units, positions, people, and reporting relationships held as a queryable model (not a static diagram).
2. **Current state + alternative future states** — the model can be instantiated as the as-is organization and as one or more proposed future structures (scenarios) derived from it.
3. **Impact comparison between states** — proposed structures can be compared through measurable impact (at minimum headcount/positions; cost is the standard currency).

Remove #1 → diagramming tool. Remove #2 → org chart management (record/publishing of the current chart). Remove #3 → a drawing editor with copies; the "design" claim collapses. All three are required for the Type to be recognizable.

### L1 — Common Mature Structure

- HRIS/HCM/ERP data integration or structured import (people, job, compensation data)
- Interactive org chart of the current state (zoom, search, filter, color-coded attributes; time dimension in some products)
- Position records distinct from people (vacancies/open jobs, FTE)
- Organizational-health metrics: span of control, layers, vacancy, gaps/overlaps
- Cost modeling against budgets (run-rate, prorated views, budget status)
- Review/approval workflow over scenarios
- Change plan / transition tracking toward implementation
- Collaboration, sharing, permission levels, sensitive-data (compensation) controls
- Export/reporting surfaces

### L2 — Variant / Optional Structure

- Granularity: position-level vs high-level (function/job-family/grade) modeling
- Audience posture: strategic (central OD/HR/finance) vs operational (line managers)
- Implementation coupling: HCM/ERP write-back vs merge-to-primary vs export handoff
- Bundled headcount/workforce planning vs separate product
- Adjacent capability bundles: job architecture, skills gap analysis, activity analysis, succession, benchmarking
- Delivery model: self-serve SaaS vs consulting-led enterprise program
- AI assistance (scenario generation, role clustering, Q&A)
- Deployment/industry/regulatory contexts (e.g., public-sector authorizations)

### L3 — Vendor-specific (research notes only)

- ChartHop: Carrot (CQL) query language; Data Sheet; scenario status names (Draft/Open/In review/Approved/Rejected/Merged/Archived); fiscal-year proration semantics and custom-cost-formula caveat; Map view; mobile directory app; package tiers (Basic / Headcount Planning / Compensation Reviews / Performance / Engagement); "merge to Primary" terminology; same-day HRIS sync recommendation.
- Nakisa: three-suite portfolio split (Org Chart / Org Design / Strategic Workforce Planning); Strategic vs Operational Org Design tier naming; OPG case-study figures (38 days → under 5 days); CCCS Protected B authorization; product-sheet PDF.
- OrgVue: Henshaw AI companion; role clustering (8,000 positions → 83 clusters); Deloitte partnership ("always-on org design"); professional services / success packages; Everest Group "Luminary" recognition; case metrics (120 countries, 170 countries, 150+ practitioners).
- Functionly: OrgPilot AI (agent/advisor modes); labs.functionly.com demo/templates; budget status (actual/committed/uncommitted); 22-day trial; consultant partner program; "role cracks & gaps" terminology; Org Design Podcast.

---

## Vendor-specific Findings

See L3 above. None of these entered the canonical model. Notably, Nakisa's own portfolio split (Org Chart Suite vs Org Design Suite) is vendor evidence *for* the directory's split between Org Chart Management and Organization Design Platform, and is treated as boundary evidence rather than a canonical structure.

## Boundary Findings

1. **vs Org Chart Management (sibling leaf)** — The tested difference: org chart management maintains and publishes the *current* structure as a record; organization design models and evaluates *alternative* structures. Nakisa ships these as two separate suites (vendor-confirmed split). ChartHop bundles both (org chart surface + scenarios). Test: remove scenarios/future-state modeling → what remains is org chart management; remove record-keeping/publication of the current state → what remains is not a functioning org design platform either (it loses its baseline). The two Types share the structural model; the design platform adds the scenario/impact loop. Flag for joint review when Org Chart Management is processed.
2. **vs Workforce Planning Platform (sibling leaf)** — Overlap: headcount and cost forecasting. Difference in center of gravity: workforce planning asks "how many people of what kind will we need over time" (demand/supply over a horizon); org design asks "how should the organization be structured and how do proposed structures compare". Vendors bundle both (ChartHop Headcount Planning module; Nakisa Strategic Workforce Planning Suite; OrgVue workforce-planning solution). Flag for joint review.
3. **vs HRIS** — HRIS is the system of record for employee data; the org design platform consumes it and (in some products) writes approved structures back. ChartHop also sells an HRIS module — bundling, not identity. The design platform's defining loop (scenarios + impact) is absent from an HRIS.
4. **vs People Analytics Platform** — Analytics answers questions about the workforce; org design changes the structure. Metrics overlap (spans/layers reports exist in both), but the scenario/apply loop is unique to org design.
5. **vs Diagramming Application** — Diagramming holds shapes; an org design platform holds structured records with metrics, permissions, and lifecycle. A diagramming tool can draw an org chart but cannot answer "what does this structure cost".
6. **Historical / market-sample check** — Older and regional org-charting products (e.g., the org-chart tools Nakisa compares itself against: Ingentis, OrgPublisher, OrgPlus) largely sit on the *org chart management* side; where they added scenario modeling they crossed into this Type. The L0 (structured model + scenarios + impact) does not depend on SaaS delivery, HRIS integration, or AI, so older/consulting-era org design work fits the definition. No over-fitting detected.

## Uncertainties

- Nakisa's operational documentation portal (docs.nakisa.com) was not fetched in depth; Nakisa workflow details (proposal → approve → deploy) come from the official product page and its imagery labels, not from a step-by-step user guide. Assertion strength reduced accordingly.
- OrgVue's implementation handoff (write-back specifics) is not documented on public pages; its loop is described as analyze→design→plan→monitor with consulting-led delivery. Whether OrgVue supports direct HCM write-back is unverified.
- Exact permission models, numeric limits, and pricing-tier gating vary and were not systematically researched; no precise numbers are asserted in the final document beyond vendor-published case-study figures (kept in Research Notes only).
- The exact market share/ordering of vendors in this category was not researched; the four products were chosen for structural diversity, not as a market-size ranking.

## Final Synthesis

An Organization Design Platform is defined by a small loop: hold the organization as structured data → derive isolated future-state scenarios from the current structure → compare them through measurable impact → hand the chosen structure toward implementation. Everything else commonly seen (HRIS integration, spans-and-layers analytics, approval workflows, cost forecasting, AI assistance, position-level vs aggregate modeling) is mature market structure or variant posture, not the definition. The closest sibling Type, Org Chart Management, shares the structural model but lacks the scenario/impact loop; Workforce Planning shares the metrics but centers on demand/supply over time rather than structure.
