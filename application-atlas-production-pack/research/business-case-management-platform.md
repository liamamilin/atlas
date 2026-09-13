# Research Notes — Business Case Management Platform

Research date: 2026-09-07
Slug: business-case-management-platform
Directory location: §10 Enterprise Operations & Administration (between Procedure Management and Business Continuity Management Platform)

---

## Research Goal

Understand what a "Business Case Management Platform" actually is as an Application Type: what the core object (the business case) is, how proposals are authored, appraised, approved, and tracked, and how this Type relates to neighboring Types (PPM, capital planning, financial modeling, approval workflow, BPM case management, business continuity).

## Initial Boundary

Working hypothesis before research:

- A business case is a structured justification for a contemplated investment or change (need, options, costs, benefits, risks) used to support a funding/approval decision.
- The platform is the organization-side system of record for authoring, appraising, approving, and (often) tracking benefits of such proposals.
- Nearest neighbors: Project Portfolio Management (execution side), Capital Improvement Planning (public capital programs), Financial Modeling Application (spreadsheet NPV), Approval Workflow Platform (generic routing), Business Process Management (operational case instances), Business Continuity Management Platform (namesake trap — different domain), Idea/Innovation Management (front-end generation), OKR/Goal Management (strategy layer).

Naming ambiguity noted up front: "Business Case Management" could be misread as "case management for business operations" (enterprise case management). The directory position (Enterprise Operations & Administration, adjacent to governance/continuity leaves) and the established meaning of "business case" in investment governance both support the investment-proposal reading. Verified against real products during research (all sampled products implement the investment-proposal reading).

## Research Questions

1. What is the business case object in real products? What sections/fields does it carry?
2. What financial appraisal structure is standard (time-phased costs/benefits, computed metrics)?
3. What is the lifecycle: draft → review → approve → execute → benefits → close? Who decides?
4. How do cases relate to portfolios, projects, and strategy (scoring, alignment, conversion)?
5. What roles exist (author/sponsor, reviewer, approver, benefits owner, PMO, finance)?
6. What rules matter (approval gates funding, plan-of-record, versioning, audit, permissions)?
7. What variants exist (IT demand/ITBM, public-sector appraisal, innovation stage-gate, capital programs)?
8. What distinguishes a dedicated platform from a PPM module carrying the same object?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Definitive Pro (Definitive Business Solutions) | decision-centric PPM with a dedicated business case module | US federal/state/municipal + commercial | Tier-1 feature pages (public) |
| Planview Portfolios | enterprise PPM incumbent; business cases as first-class object | large enterprise (banking, manufacturing) | Tier-1 doc structure (article bodies sign-in gated) + Tier-2 product page |
| Clarity (Broadcom) | ITBM/PPM pole: Ideas workspace with financials + approval + conversion | large enterprise | Tier-1 docs (public) |
| Triskell Software | demand-management pole of the same market | mid/large enterprise (EU) | Tier-2 product pages |
| Wellspring Accolade (formerly Sopheon) | innovation stage-gate pole | global manufacturing/CPG enterprises | Tier-2 product pages |
| i-nexus | strategy-execution adjacent pole (boundary context) | global manufacturing/PE | Tier-2 product page |

Attempted and abandoned (network rules — 2 failures each, then stop):
- Amplify Now (amplifynow.com / www.amplifynow.com — empty responses ×2)
- ServiceNow SPM (servicenow.com — timeouts ×2)
- Wovex (wovex.com / www.wovex.com — 503 ×2)

## Sources

Fetched 2026-09-07:

- Definitive Pro homepage — https://definitiveinc.com/ (via definitivepro.com redirect)
- Definitive Pro — Business Cases feature page — https://definitiveinc.com/definitive-pro/business-cases/
- Planview Portfolios product page — https://www.planview.com/products-solutions/products/planview-portfolios/
- Planview Customer Success Center — Planview Portfolios → Outcomes → Business Cases (TOC + gated article) — https://success.planview.com/Planview_Portfolios/Outcomes/Business_Cases (+ Screen Basics sub-page, also gated)
- Broadcom TechDocs — Clarity 16.4.2 → Using Clarity → Capture, Develop, and Approve New Ideas — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/using/new-user-experience-capture-develop-and-approve-new-ideas.html
- Broadcom TechDocs — Clarity 16.4.2 → Manage Idea Financials — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/using/new-user-experience-capture-develop-and-approve-new-ideas/New-User-Experience--Manage-Financial-Module-in-Idea.html
- Triskell Software homepage — https://triskellsoftware.com/
- Triskell — Demand Management solution page — https://triskellsoftware.com/solutions/demand-management/
- Wellspring — Accolade product page — https://www.wellspring.com/en-us/accolade
- Wellspring homepage (Sopheon redirect) — https://www.sopheon.com/
- i-nexus homepage — https://www.i-nexus.com/

Source-access limitations:
- Planview Success Center Business Cases article bodies require sign-in. Only the documentation structure (object name, sub-pages: Screen Basics, Publishing Business Case Data, Screen Preferences, Using Business Case Scenarios, Formula Calculator; plus a "Project (and Portfolio) Business Case Report" in FastTrack Analytics; tags include "grants" and "permissions") is directly observable. Claims about Planview's business case internals are therefore kept at structure level only.
- ServiceNow SPM (a major ITBM pole) could not be reached; no ServiceNow-specific claims are made.
- Amplify Now and Wovex (dedicated benefits-realization vendors) could not be reached; benefits-realization findings rest on the sampled products that were reachable.

---

## Product Observations

### Definitive Pro (decision-centric PPM; dedicated business case module) — Evidence Layer A

From the Business Cases feature page (direct quotes/paraphrases):

- Definition given by the vendor: "A business case is used to: manage purposeful business change by organizing the financial impacts in relationship to time to support decision-making regarding potential investments." Methodology credibility is emphasized: "An effective business case will use a proven methodology… ensure that the underlying methodology is clear to the evaluators."
- The financial business case is a **tab-driven record** with configurable tabs:
  - **Business Need** — submitter enters data/text describing the need.
  - **Business Need Assessment** — scorecard(s) for an initial strategic-alignment assessment.
  - **Solution Approach** — delivery organization describes the solution approach.
  - **Resource Budgeting** — collect estimates from the resource teams required to deliver.
  - **Resource Planning** — time-phased (monthly) capacity and allocations; portfolio manager reviews conflicts/bottlenecks at portfolio and enterprise level.
  - **Forecast** — 5-year cost and benefit projection with discounting of out-year cash flows; auto-calculates total cost (pre-project, project, post-project) and total benefits (revenue, cost reduction, cost avoidance) by year; configurable cost pools (technology business management/TBM, capital projects, custom).
  - **Results** — auto-calculated financial metrics: Return $, ROI %, IRR %, payback period, NPV; pass/fail against established hurdle rates (optional); charts; one-click business case report in PDF; investment dashboard with pass/fail indicators vs hurdle rates.
  - **Location** — GIS plot of project locations.
  - **Contracts** — acquisition approach for contract actions; contract budget $.
  - **Governance** — key roles, key milestones, change requests, project health and status.
  - **Documents** — repository for reference documents.
  - **Lookbacks** — track and analyze changes to the business case over time.
- Process (from homepage): 1) develop a weighted decision model (AHP) from strategic objectives; 2) score projects by strategic benefit; 3) complete "lite business cases" for highly aligned projects (narrative fields for business need and solution approach + financial forecast); 4) value analysis (strategic benefit vs cost vs risk quadrants); 5) optimize the portfolio (funding/resource allocation via solver).
- Lifecycle: "supports the entire project lifecycle, from ideation to benefit realization, with structured phases for budget formulation, execution, and evaluation, and incorporates continuous feedback loops."
- Positioning: "progressively elaborate the business case as more and better information becomes available" (incremental investment risk reduction).
- Audience: federal agencies, state agencies, municipalities, commercial businesses. Marketing stats (35% greater portfolio benefit etc.) recorded as claims only.

### Planview Portfolios (enterprise PPM incumbent) — Evidence Layer A (structure) + B

From the product page (Tier-2):

- Strategy tab: Strategic Alignment ("translate high-level missions and objectives into specific investments"), OKRs, Roadmapping, **Investment Prioritization** ("rank and analyze investments by business drivers and use what-if scenarios"), **Financial Planning** ("set financial targets… budgeting, forecasting, and tracking costs and benefits").
- Planning tab: Product & Program Funding (incremental funding at multiple levels), **Demand Management** ("collect and evaluate demand across the enterprise from unstructured ideas to formal program and project requests"), Capacity Planning, Scenario Planning, Forecast and Actuals ("balance your portfolio for capital and expense constraints").
- Execution tab: project management, resource management, costs and actuals, agile costing.
- Customer quotes (recorded as claims): Corning — "combined them into one capital portfolio… visibility into the costs as well as the benefits… capital stage gate process"; NatWest — "track the main-level financial data, outcomes, and business cases, and ultimately the delivery of value."

From the Customer Success Center (Tier-1 structure; bodies gated):

- "Business Cases" is a first-class documented object under **Outcomes**, with sub-pages: Business Cases Screen Basics, Publishing Business Case Data, Setting Business Cases Screen Preferences, Using Business Case Scenarios, Using Formula Functions with the Formula Calculator.
- A FastTrack Analytics report exists: "WRK13 - Project (and Portfolio) Business Case Report."
- Article tags include "grants" and "permissions" (permission model exists; details not observable).

### Clarity / Broadcom (ITBM pole) — Evidence Layer A

From "Capture, Develop, and Approve New Ideas" (Tier-1 docs):

- "The Ideas workspace serves as a centralized hub for capturing, developing, and approving new business initiatives **before they evolve into full-scale projects or investments**… systematically evaluate and manage their innovation pipeline, allowing teams to screen multiple ideas efficiently and make informed decisions about which concepts deserve further investment and development."
- Ideas created from **customizable templates**; spreadsheet-like grid with configurable columns/fields; custom taxonomy ("products, value streams, or any custom investment type"); hierarchical organization.
- **Access rights** (prerequisites): Idea Management - Navigate; Ideas - Create; Idea - View - All; **Resource - Approve Ideas - All / Idea - Approve - All** — approval is a distinct permission from authoring.
- Idea blueprint: administrators/PMO content designers configure layouts per business need; business rules and channels supported.
- Sub-modules documented for ideas: Manage Idea Financials; Staff an Idea; Cross-Investment Links; To Dos; Checklists; Hierarchy; Agreements; **Risks, Issues, and Changes**; Status Reports; Conversations; Canvas dashboard; **Audit module**; Embedded reports.
- "You can execute a process from projects, custom investments, ideas, roadmap items… To learn more about **converting ideas to projects**…" — conversion is a first-class flow.

From "Manage Idea Financials" (Tier-1 docs):

- Financial module on investments (including ideas): create/edit/analyze multiple **cost plans**; mark a **plan of record** and **submit for approval**; "When a cost plan is approved, it becomes the budget plan"; dynamic budget adjustments (new cost plans that merge with or replace the existing budget).
- **Benefit plans** (with benefit class/subclass attributes) and **actual transactions**; forecasts; time-phased data against fiscal time periods.
- Access rights include: Investment - Cost Plan - View/Edit All; Budget Plan - View/Edit/**Approve/Reject** All; Benefit Plan - View/Edit/Approve All — approval/rejection of financial plans is a distinct permission.
- Field-level security on financial plan attributes; relabeling; audit module.

### Triskell Software (demand-management pole) — Evidence Layer A (positioning)

From the Demand Management solution page:

- "centralized Demand Management hub to **capture, evaluate and prioritize project ideas**."
- Standardize scoring criteria and objective evaluation; prioritize by strategic value/alignment and "highest potential ROI."
- **Workflows**: "Automate request routing and approval processes for efficient demand intake."
- Requests repository; Kanban boards for demand workflow; capacity planning against demand; innovation management (capture ideas/R&D/NPD aligned to strategy).
- Customization FAQ: configurable workflows, approval processes, data model ("define your own demand attributes, metrics, and categorizations"), stages/milestones/approval rules.
- Use cases: PPM, resource management, IT portfolio, NPD, transformation programs, financial management ("integrate demand management with financial planning to ensure optimal investments").
- Customer quote (claim): Syngenta — CAPEX investment portfolio management with milestones, rolling forecast, KPIs.

### Wellspring Accolade (innovation stage-gate pole; formerly Sopheon) — Evidence Layer A (positioning)

- Accolade = "Enterprise Innovation Management System"; modular capabilities on a shared "Accolade Core" (unified data foundation, operating model).
- Strategic Innovation modules: Strategic Portfolio Management ("align initiatives to strategy, balance risk and return, and reallocate investments dynamically"), Revenue Stream Planning ("model multi-year growth targets as revenue streams and directly link innovation investments to business outcomes"), Sustainability Management, **Front End of Innovation (FEI)** ("Capture, contextualize, and advance high-potential innovation opportunities… Use structured workflows to develop, vet, and **graduate ideas into the execution pipeline**"), Technology Scouting.
- Process Execution modules: NPD ("Plan, execute, and govern… from concept through launch"), **Capex Management** ("Manage large-scale investments and capital projects with the same rigor and visibility you apply to your innovation portfolio"), Manufacturing Innovation, Technology Innovation.
- Enterprise Coordination modules: Integrated Roadmapping, Resource Planning.
- Positioning phrase: "manage your entire portfolio as a unified business case for enterprise growth."
- Customer quotes (claims): bringing "all of our actual data into Accolade… identify where you've got underperforming products versus what you planned."

### i-nexus (strategy-execution adjacent pole) — Evidence Layer A (positioning)

- "Workbench connects strategic goals, portfolios, initiatives, owners, milestones, KPIs and actions in one governed system."
- Use cases: transformation, operational excellence, M&A, PE value creation, finance, ESG.
- Customer quotes (claims): "document projects and visualize the associated savings"; "Operations and Finance have direct visibility into the alignment of improvement project activity and financial results."
- Treated as boundary context: strategy-execution systems carry initiative records with financial linkage but the center of gravity is goal cascade/KPI rhythm, not the investment appraisal record.

---

## Cross-product Comparison

| Aspect | Definitive Pro | Planview Portfolios | Clarity (Broadcom) | Triskell | Wellspring Accolade | i-nexus |
|---|---|---|---|---|---|---|
| Core object | Business case (tabbed record) | Business Cases (first-class object under "Outcomes") | Idea (investment type with financials) | Demand/request record | Idea/opportunity (FEI) → project | Initiative linked to goals |
| Justification narrative | Business Need + Solution Approach tabs | (structure only; bodies gated) | idea fields/templates | request fields | FEI capture/contextualize | initiative description |
| Strategic alignment scoring | Business Need Assessment scorecards (AHP) | Investment Prioritization by business drivers | screening in grid | scoring criteria, strategic alignment | align initiatives to strategy, balance risk/return | goals/KPIs linkage |
| Financial appraisal | 5-year cost & benefit forecast, discounting, ROI/IRR/NPV/payback, hurdle rates | financial planning: budgeting, forecasting, tracking costs and benefits | cost plans → plan of record → approval → budget plan; benefit plans; actuals | financial management module | revenue stream planning; capex management | savings tracking |
| Approval as recorded decision | governance tab (roles, milestones, change requests); hurdle pass/fail | permissions tag (details gated) | Idea - Approve - All; Budget Plan - Approve/Reject All | approval workflows/routing | vet/graduate gates | governed system |
| Portfolio/pipeline context | decision model → score → value analysis → optimize | portfolio prioritization, scenarios | ideas workspace pipeline | demand hub, kanban | portfolio management | portfolios |
| Resource estimates | resource budgeting + time-phased planning | capacity planning | staff an idea | capacity planning | resource planning module | resources |
| Risk | value analysis (benefit vs cost vs risk) | (not observed at case level) | risks/issues/changes for ideas | (not observed) | balance risk and return | (not observed) |
| Benefits realization | Lookbacks; "ideation to benefit realization" | costs and benefits tracking; customer quote | benefit plans + actual transactions | financial planning integration | actual data vs plan | savings visibility |
| Documents/attachments | Documents tab | Publishing Business Case Data | embedded reports, conversations | requests repository | (not observed) | (not observed) |
| Conversion to execution | phases: budget formulation → execution → evaluation | demand → formal program/project requests | convert ideas to projects | convert requests to projects | graduate ideas into execution pipeline | initiatives (execution tracked in-system) |
| Audit/versioning | Lookbacks (changes over time) | (not observed) | audit module | (not observed) | (not observed) | (not observed) |
| AI assistance | GenAI business case drafting (claim) | Anvi conversational AI | Vaia (AI) | (not observed) | Wellspring AI | AI-powered Strategy OS |
| Distinctive extras | GIS location, contracts tab, TBM cost pools, DQGI data quality, AI personas | OKR framework, agile costing | blueprints, field-level security, fiscal periods | configurable data model | sustainability module, tech scouting | Hoshin Kanri, X-matrix |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Business case record** — a persistent, identified proposal for a contemplated investment or change, owned by a named sponsor/author, carrying a justification narrative (the need/problem and the proposed solution or options).
2. **Structured financial appraisal** — time-phased costs and expected benefits attached to the record, from which comparative value metrics (ROI/NPV/payback/IRR-class) are computed by the system.
3. **Governed decision lifecycle** — the record moves through review/approval states with accountable decision-makers; approval or rejection is a recorded decision event that gates funding/execution.

Justification for minimality:
- Remove the record → nothing to manage (not a platform).
- Remove the financial appraisal → it collapses into a generic approval workflow / document management.
- Remove the governed decision lifecycle → it collapses into a financial modeling spreadsheet.
- Everything else observed (portfolio comparison, benefits tracking, templates, resources, risk, documents, AI) is absent in at least some real configurations and is therefore L1/L2.

§24 historical check: older and platform-native implementations (classic PPM "ideas/demand" modules, government investment-appraisal tools, pre-cloud PPM) all satisfy this L0 — a proposal record with costs/benefits and an approval gate. The L0 does not depend on cloud delivery, AI, OKRs, TBM taxonomies, or any specific financial methodology.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature modern offerings but not definitional:

- **Portfolio/pipeline context** — cases are held and compared as a population: scoring against strategic criteria, prioritization views, what-if scenarios, portfolio optimization (all six sampled products position cases inside a portfolio/pipeline).
- **Templates and standard methodology** — configurable case templates/blueprints; vendor-emphasized "proven methodology" so evaluators can trust comparisons.
- **Resource estimates** — early-stage resource/capacity estimates attached to the case (Definitive Pro resource tabs; Clarity staff-an-idea; Triskell capacity; Accolade resource planning; Planview capacity).
- **Benefits realization tracking** — post-approval tracking of promised benefits vs actuals (Definitive Pro lookbacks + benefit realization phase; Clarity benefit plans + actual transactions; Planview costs-and-benefits tracking; Accolade actual-vs-plan; i-nexus savings).
- **Risk and supporting records** — risks/issues attached to the case (Clarity explicitly; Definitive Pro via value analysis; Accolade risk/return balancing).
- **Documents, links, and reporting** — document repositories, cross-investment links, status reports, one-click case reports, portfolio dashboards.
- **Conversion to execution** — approved cases convert into projects/programs/investments (Clarity "converting ideas to projects"; Triskell request→project; Planview demand→formal requests; Accolade graduate into execution pipeline; Definitive Pro budget-formulation→execution phases).
- **Role separation** — author/sponsor vs reviewer/evaluator vs approver vs benefits owner vs PMO/finance; approval is a distinct permission (Clarity access rights; Planview permissions tag; Triskell approval workflows).
- **AI assistance** — drafting cases, summarizing, insights (Definitive Pro, Planview, Clarity; increasingly common).

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, or workflow variant:

- **IT investment flavor (ITBM)** — demand intake from IT, TBM-style cost pools, fiscal-period time-phasing, idea→project conversion machinery (Clarity; Planview demand management).
- **Public-sector / capital appraisal flavor** — hurdle rates with pass/fail indicators, GIS location of investments, contract/acquisition planning, grants (Definitive Pro; Planview "grants" tag).
- **Innovation stage-gate flavor** — front-end-of-innovation workflows, gates/vetting, graduation criteria, NPD process modules (Accolade; Triskell NPD).
- **Capital program flavor** — CAPEX portfolios, capital stage gates (Planview/Corning quote; Accolade Capex Management; Triskell/Syngenta CAPEX quote).
- **Strategy-execution flavor** — OKR/KPI linkage, Hoshin Kanri, scorecards (Planview OKRs; i-nexus).
- **Decision-science methods** — AHP weighting, consensus measurement, mathematical optimization of funding allocation (Definitive Pro).
- **Deployment posture** — SaaS vs on-premise (Clarity ships both), suite module vs standalone.
- **Financial depth** — discounting, IRR/NPV vs simpler ROI/payback; configurable cost pools; benefit classification taxonomies.

### L3 — Vendor-specific Structure (Research Notes only)

- Definitive Pro: named tab set (Business Need → … → Lookbacks), DQGI data-quality module, AI personas, T-shirt-size estimating, "3 weeks to get started" claim, marketing stats (35%/25%/50%).
- Clarity: blueprint system, SQL curve technology for time-phased data, named access rights ("Idea - Approve - All", "Investment - Budget Plan - Approve All"), field-level security with shield icons, Vaia AI, MCP server, Jaspersoft reporting, 250k-row CSV export.
- Planview: Anvi conversational AI, Connected Work Graph, OKR framework, FastTrack Analytics report WRK13, agile costing/capitalization.
- Triskell: configurable data model terminology, PPM maturity assessment, SAFe partner positioning.
- Accolade: Accolade Core/modules wheel, Revenue Stream Planning, Sustainability Management, Growth Innovation philosophy, Forrester stats.
- i-nexus: Strategy Cards, X-matrix/bowling-chart templates, Hoshin Kanri heritage.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical document except as neutral, de-branded examples where they illustrate a variant (e.g., hurdle rates as a public-sector appraisal practice, observed in one product — kept as "some products" with product-specific marking).

## Boundary Findings

- **vs Project Portfolio Management Application** — sharpest seam. PPM's center of gravity is executing a portfolio of projects (schedules, resources, delivery, status). Business case management's center of gravity is the *pre-execution* investment decision: justification, appraisal, approval, and the benefits promise. In the real market the two are usually sold in one suite (all sampled PPM products carry a business-case/idea object), but the objects and loops differ: remove execution management (tasks/schedules/timesheets) and business case management still stands; remove the case/appraisal/approval loop and what remains is PPM. The Type documented here is the decision-governance slice, whether sold standalone or as a suite module.
- **vs Capital Improvement Planning (§17)** — public capital programs aggregate many investments into multi-year capital plans/budgets with funding sources; the business case is the per-investment justification feeding that aggregation. CIP without per-investment appraisal is not this Type.
- **vs Financial Modeling Application (§08)** — financial modeling computes NPV/ROI in a spreadsheet-like surface without a governed record lifecycle, approval, or portfolio context. The appraisal math is shared; the governance is not.
- **vs Approval Workflow Platform (§10)** — generic request routing with forms and approvers. Without the investment-appraisal structure (time-phased costs/benefits, value metrics) it is not this Type.
- **vs Business Process Management Platform (§10)** — BPM "case management" handles operational case instances (requests, incidents, service cases). A business case is an investment proposal, not an operational instance. Naming overlap only.
- **vs Business Continuity Management Platform (§10)** — namesake trap ("business" + adjacent directory position). BCM manages impact analysis, continuity plans, exercises. No overlap in object or workflow.
- **vs Idea Management / Innovation Management (§12 Product Discovery)** — idea management generates and collects ideas; business case management appraises and approves investments. The front end overlaps (FEI modules); the seam is the financial appraisal + governed approval. A pure idea-collection tool is not this Type.
- **vs OKR / Goal Management Platform (§09)** — goals/KPIs cascade vs investment proposals. i-nexus sits between; its center is the goal/KPI rhythm, not the appraisal record.
- **vs Enterprise Request Management (§10)** — intake and fulfillment of requests; no appraisal or benefits semantics.

Naming-ambiguity note for joint review: "Business Case Management" is occasionally used in the market to mean operational case management for businesses. Product evidence (all sampled products) supports the investment-proposal reading for this directory leaf; recorded here so a future reviewer does not mistake the leaf for an alias of enterprise case management.

## Uncertainties

- Planview's business case internals (fields, scenarios mechanics, publishing semantics) could not be verified — article bodies are sign-in gated. Only the object's existence, sub-page structure, and a portfolio business case report are confirmed.
- ServiceNow SPM (major ITBM vendor) unreachable; its demand/investment model is unverified here. The ITBM pole rests on Clarity + Planview + Triskell.
- Dedicated benefits-realization vendors (Amplify Now, Wovex) unreachable; the benefits-tracking L1 finding rests on the reachable sample (still 4+ products).
- Exact state names for case lifecycles vary by product and were not systematically enumerated; the document uses conceptual states only.
- Hurdle-rate support is directly observed in one product (Definitive Pro); treated as optional/product-specific rather than common.
- Whether any product sells business case management fully standalone (without portfolio context) is unverified; all sampled products embed cases in a portfolio/pipeline. The L0 deliberately excludes portfolio context for this reason.

## Final Synthesis

A Business Case Management Platform is the organization-side system of record for investment proposals. Its defining core is small: a persistent business case record (justification narrative bound to a sponsor), a structured time-phased financial appraisal from which value metrics are computed, and a governed decision lifecycle in which accountable reviewers approve or reject the case, gating funding and execution. Around that core, mature products add the portfolio loop (score, compare, prioritize, optimize), template-driven authoring, resource estimates, risk records, benefits-realization tracking against the approved case, document/report machinery, and conversion of approved cases into projects or programs. The market implements the Type along several poles — decision-science-led (AHP/optimization), IT-demand-led (idea→project), innovation stage-gate-led, and strategy-execution-led — usually as a module of a broader PPM/SPM suite, occasionally as a dedicated decision platform for public-sector capital governance. The Type is bounded from PPM (execution), financial modeling (computation without governance), approval workflow (routing without appraisal), BPM case management (operational instances), business continuity (namesake only), and idea management (generation without appraisal).
