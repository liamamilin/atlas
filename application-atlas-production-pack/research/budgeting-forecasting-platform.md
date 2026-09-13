# Research Notes — Budgeting & Forecasting Platform

## Research Goal

Understand what a corporate Budgeting & Forecasting Platform actually is as an Application Type: the objects inside it, the planning cycle it manages, how budget and forecast versions work, how actuals enter the comparison loop, and where its boundaries lie against FP&A platforms, sales forecasting, financial consolidation, BI, accounting, and consumer budgeting.

## Initial Boundary

Working hypothesis at start:

- This is the organization-side planning system used by finance (FP&A) teams to run budget cycles and forecasts: a shared multi-dimensional financial planning model (accounts x time x organizational segments), multiple plan versions (budget / forecast / scenarios), contribution and approval workflow, and actuals-vs-plan variance.
- Nearest neighbors: Financial Planning & Analysis Platform (broader umbrella leaf in the same directory section — not yet processed, joint-review flag), Sales Forecasting Platform (unprocessed), Financial Consolidation Platform, General Ledger / Accounting Software, BI Platform, Public Budgeting Platform (government leaf), Budgeting Application (consumer — already documented sibling, budgeting-application.md), Spreadsheet Application (the substrate this Type replaced).
- Key question flagged up front: is "Budgeting & Forecasting Platform" genuinely distinct from "Financial Planning & Analysis Platform", or an emphasis-slice of the same product category?

## Research Questions

1. What are the core objects? (dimensions, accounts, entities, periods, versions, line items, plans)
2. What is a "budget" vs a "forecast" vs a "scenario" inside these systems?
3. How does the planning cycle flow (targets, contribution, review, approval, official plan)?
4. How do actuals enter, and how is variance computed and presented?
5. Who uses it (finance vs budget owners vs builders) and what does each do?
6. How do products differ: modeling-platform vs template/application-led vs suite-embedded vs Excel-flavored?
7. What role do drivers, allocations, and predictive/AI baselines play?
8. What must NOT be in the definition (era/vendor overfit: cloud, driver-based, ML, specific approval mechanics)?

## Representative Products

| Product | Segment / philosophy | Evidence level |
|---|---|---|
| Workday Adaptive Planning | enterprise; suite-adjacent, ERP-agnostic planning system; AI positioning | product pages (Tier 2) |
| Anaplan | enterprise; modeling-platform philosophy (build your own planning models) | Anapedia help docs (Tier 1) |
| Oracle EPM Planning (Planning & Budgeting Cloud lineage) | enterprise/mid; module-based applications (Financials, Workforce, Capital, Projects) on a dimensional engine | Oracle Help Center (Tier 1) |
| Planful | mid-market; financial performance platform (Plan / Close / Consolidate / Report) | product pages (Tier 2) |
| Prophix | mid-market; FP&A + close suite ("Autonomous Finance Platform") | product + use-case pages (Tier 2) |
| Board | enterprise; unified financial + operational planning platform, cloud or on-prem | product + PB&F pages (Tier 2) |

Market context only (no claims drawn): Vena (help center sign-in-gated), NetSuite Planning & Budgeting (docs not fetched; Oracle EPM Planning is the same lineage), historical predecessors (Hyperion Planning, Cognos/TM1, SAP BPC — used as historical check reasoning only, no fetched evidence).

## Sources

Fetched 2026-09-06:

- Workday — Adaptive Planning overview: https://www.workday.com/en-us/products/adaptive-planning.html
- Workday — Budgeting & Forecasting use case: https://www.workday.com/en-us/products/adaptive-planning/financial-planning/budgeting-forecasting.html
- Anapedia — Modeling index: https://help.anaplan.com/modeling-4fb7dde6-0385-4ee4-a8cd-dfe45803326a
- Anapedia — Dimensions: https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a
- Anapedia — Versions: https://help.anaplan.com/versions-19b4391f-5257-40ee-8dfb-36f0ab426c8f
- Oracle — Cloud EPM Planning "How Do I…": https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/
- Oracle — Use topic index: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/use-only-hdi.html
- Oracle — "Building a Plan with Approval Units" (Oracle Fusion Cloud EPM Working with Planning, E94218): reached via https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/saas/planning-budgeting-cloud&id=PFUSU-f_approvals_1
- Planful — home: https://www.planful.com/ ; Finance solution: https://www.planful.com/solutions/finance/
- Prophix — home: https://www.prophix.com/ ; Budgeting & Planning: https://www.prophix.com/use-case/budgeting-planning/
- Board — home: https://www.board.com/ ; Planning, Budgeting & Forecasting: https://www.board.com/finance/planning-budgeting-forecasting

Unreachable (recorded limitations): Planful support center (support.planful.com — transport error, abandoned after 1 attempt), docs.prophix.com (transport error, abandoned), Vena docs/help (sign-in-gated), board.com/en/platform/planning (404, substituted by the PB&F page). Oracle docs root paths 404'd twice before the correct path (planning-budgeting-cloud base) was found. No numeric limits, prices, cycle durations, or default settings are asserted from memory anywhere. Vendor performance statistics (Board's "75% reduction in planning time", Prophix customer-hour claims, customer counts) are marketing claims and are kept only here.

## Product A — Workday Adaptive Planning

### Key observations (evidence layer A, product pages)

- Positioning: "The planning system that integrates with any ERP/GL or data source." Sub-products: Financial Planning, Close & Consolidation, Workforce Planning, Operational Planning. The vendor itself treats budgeting/forecasting as one part of a planning suite.
- Budgeting & Forecasting use-case page — concrete capability set:
  - "Rolling forecasts … continuous picture of the business so you can respond to variances in real time"
  - "Top-down and bottom-up budgeting. Set top-down targets based on executive guidance or build bottom-up operational plans with cost center managers."
  - "Incremental and zero-based budgeting" (methodology choice lives inside the product)
  - "Driver-based expense planning … expense allocations using our built-in rules engine"
  - "Unlimited personal and shareable what-if scenarios"; "Compare what-if scenarios that incorporate real-time data"
  - "Plan across any time horizon. Build daily forecasts and monthly or quarterly budgets, as well as long-term plans … within your fiscal calendar."
  - "Boost collaboration and adoption. With one source for data and integrated workflows…"
  - "Connect all your systems … bring in ERP and cloud warehouse data, keep models up to date"
- Customer quote (VP Finance): "budget planners can see how regions are rolling up and what gaps are emerging in real time" — roll-up visibility during the cycle.

## Product B — Anaplan

### Key observations (evidence layer A, Anapedia Tier-1)

- **Dimensions**: "Dimensions are the lists that workspace administrators select to be a module's rows, columns, and pages. They provide the structure of a module and define the context for data in cells." Default lists in every model: **Time, Versions, Users, Organization** (Organization auto-populated with "Total Company" as top-level roll-up). Cell meaning = context from its dimension values. Example module: Products on rows, line items on columns, Time + Countries on pages.
- **Modules / line items**: a model is built from modules (grids) containing line items (measures) with summary methods (how child cells roll up into parents).
- **Versions** (the canonical budget/forecast/scenario object):
  - "You can use versions to compare different scenarios in a model."
  - Every new model includes default versions **Actual** and **Forecast**; "the version created with the name Actual is always selected as Actual"; "You cannot delete the Actual version."
  - **Switchover dates**: for non-Actual versions, data up to the switchover date equals Actual and is read-only; after it, the version is editable. "You can also select a new switchover date at the end of each period to create a rolling forecast." — the mechanism tying actuals to forecast versions.
  - Variance reports compare model versions; bulk copy between versions; restrict version edits.
- **Selective access**: restrict access to lists and list items per user — dimension-level security.
- **User experience**: Boards and Worksheets — "view and edit detailed data from Anaplan models on interactive grids and cards." Mobile app views/edits boards.
- **Data integration**: import/export line items, data, lists, users, versions; APIs and integration options at multiple levels; Data Orchestrator prepares data before import into models.
- **ALM**: model development → testing → deployment lifecycle (model governance is itself a product surface).
- Philosophy confirmed: Anaplan ships a modeling environment, not fixed budget applications; budgeting is a model you build. CoModeler / Forecaster (ML) exist as named extras.

## Product C — Oracle EPM Planning (PBCS lineage)

### Key observations (evidence layer A, Oracle Help Center Tier-1)

- **Use surfaces**: Forms ("Entering Data", "Working with Data in Forms"), Ad Hoc grids (free-form data entry/analysis), Dashboards + Infolets, Reports and multi-report "Books", Smart View for Office (Excel add-in — enter/save data, ad hoc analysis, functions), Smart View for Google Workspace (forms in Google Sheets, flex forms), Private **Sandboxes** (personal what-if space).
- **Approval workflow** — "Building a Plan with Approval Units":
  - "Plans are tracked and managed through approval units. An approval unit is the basic unit for preparing, annotating, reviewing, and approving plan data."
  - Approval unit = **version + scenario + entity (or part of an entity)** — e.g. version "Worst Case" x scenario "Forecast" x entity "New York".
  - Administrator sets up approval units "typically based on the company's organization, geographical regions, or product lines"; designates reviewers/approvers as "the promotion path"; officially starts each unit to begin the planning cycle; state "Under Review"; owner enters data; then "Promote or Submit … After doing so, you can't change the data until you become the owner again."
  - "When all reviewers approve all approval units, the planning cycle is complete."
- **Modules** (pre-built planning applications on the same engine): Capital, Financials, Projects, Workforce — plus separate applications: Sales Planning (quota planning, advanced sales forecasting, key account planning), Strategic Workforce Planning, Strategic Modeling (long-range), Predictive Cash Forecasting.
- **Predictive assistance**: Predictive Planning ("Improving Forecasting Accuracy"), Advanced Predictions, IPM Insights (machine-learned insights with tagging and GenAI summarization).
- Implication: a dimension+member structure (Smart View "Working with Dimensions and Members") underlies everything; Oracle's approach = engine + optional pre-built modules, vs Anaplan's pure modeling.

## Product D — Planful

### Key observations (evidence layer A/B, product pages)

- Full platform scope: "planning, close, consolidation, and reporting in one financial performance management platform" (Plan / Close / Consolidate / Report).
- Finance page:
  - "budgeting, forecasting, reporting, and analysis in one place"; "Familiar Excel behaviour"; "Spotlight for Microsoft 365 … work in Excel, PowerPoint, or Word."
  - Templates: "Standardized templates ensure consistency across budgets, forecasts, and scenarios, so teams aren't rebuilding every cycle."
  - Rolling forecasts: "Update key drivers like revenue, headcount, or costs to immediately see the downstream impact. Then test scenarios…"
  - Annual operating plan: "Set targets across departments, roll up assumptions instantly, and keep approvals and revisions governed in one place. Each team contributes within a shared framework…"
  - Cash flow forecasting is driver-based (headcount, capex, payment terms).
  - AI agents (Analyst / Planner / Help) — forecasts from a baseline, what-if scenarios conversationally; MCP server with "dimension security and role-based access", "read-only by design".
- Customer-scale claim ("1,500+ companies") — marketing; not asserted in the final doc.

## Product E — Prophix

### Key observations (evidence layer A, product + use-case pages; unusually operational FAQ)

- Budgeting & Planning page:
  - **Collaborative budgeting**: "Give department heads a structured, guided input experience… Managers submit directly into [the platform], against a standard structure finance defines. Workflow routing handles review and approval automatically. Finance sees consolidation in real time as submissions come in."
  - **Driver-based planning**: "Connect your budget to the operational drivers that actually determine costs and revenue: headcount, hiring plans, utilization, volume, price, and pipeline. Change a driver and every dependent line updates automatically… benefit rates, and overhead allocations recalculate instantly."
  - **Scenario & version management**: "Build conservative, base, and stretch budgets within a single model without creating parallel files… compare versions side by side… Every version is tracked, labeled, and recoverable."
  - **AI-assisted baselines**: "analyzes historical actuals, trend patterns, and seasonality to generate planning baselines automatically. Finance reviews and adjusts… every final number with a full audit trail."
  - **Budget vs actual**: "Actuals flow into [the platform] automatically as periods close, mapped directly against the approved budget. Budget vs. actual variance is calculated instantly across every entity, department, cost center, and line item."
  - **ERP/GL integration**: Dynamics, Sage Intacct, NetSuite, SAP named.
  - **Methodology**: "Prophix One supports zero-based budgeting alongside traditional and driver-based approaches: finance chooses the methodology that fits the organization."
  - Process framing (the problem it sells against): annual budget cycle via emailed Excel templates; "department managers disengage"; "finance spends the rest of the year explaining variances."
- Suite scope: FP&A + Close & Consolidation + Reporting & Analytics; workflow page: "role-based approvals", budget collection automation; industries (construction, healthcare, higher-ed, senior living, manufacturing…).

## Product F — Board

### Key observations (evidence layer A, product + PB&F pages)

- Positioning: "Enterprise Planning Platform" unifying **financial and operational planning** — "Continuous Planning, an always-on approach"; cloud **or on-premise** (explicit deployment variant).
- PB&F page:
  - "Integrated view of financial position … clear view of your P&L, balance sheet, and cashflow—and how defined drivers impact them."
  - "Accelerated planning cycles. Run your monthly forecast at speed with all parameters and workflows set up to ensure accuracy and control over your entire process."
  - "Driver-based planning: Use unlimited dimensions to create budgets, plans, and forecasts. Explore profitability by cost center, product, or any variable, with the ability to drill down."
  - Embedded ML predictions; industry-specific models.
- Suite scope: FP&A + FCCR (close/consolidation) + supply chain / merchandising / workforce planning.

## Cross-product Comparison

| Structure | Workday | Anaplan | Oracle | Planful | Prophix | Board | Evidence |
|---|---|---|---|---|---|---|---|
| Multi-dimensional model (accounts x time x org, plus more) | implied ("regions rolling up", modeling) | explicit (dimensions = rows/columns/pages; default Time/Versions/Users/Organization) | explicit (dimensions & members; entity dimension in approval units) | implied (single platform, dimension security) | explicit (entity/department/cost center/line item) | explicit ("unlimited dimensions") | B |
| Versions: budget / forecast / scenario as first-class data | yes (what-if scenarios; budgets vs forecasts) | yes (Actual + Forecast default, scenario versions, switchover) | yes (version x scenario in approval units; sandboxes) | yes (budgets, forecasts, scenarios; templates) | yes (conservative/base/stretch; tracked/labeled/recoverable) | yes (budgets, plans, forecasts) | B |
| Governed planning cycle (contribution + review/approval) | yes ("integrated workflows", top-down/bottom-up) | via model + access control (workflow is modeled, not a fixed module) | yes (approval units: prepare → review → approve → promotion path; cycle completes when all approved) | yes ("approvals and revisions governed in one place"; AOP) | yes ("workflow routing handles review and approval automatically") | yes ("parameters and workflows set up … control over your entire process") | B |
| Actuals integration + plan-vs-actual variance | yes (ERP/warehouse integration; "respond to variances") | yes (Actual version mandatory; variance reports) | yes (Actual vs plan comparison; GL integration) | yes (reporting on live data) | yes (actuals flow in at period close; instant variance) | yes (P&L/BS/CF view from source systems) | B |
| Rolling forecast / re-forecast as standing practice | yes (named) | yes (switchover-date rolling forecast mechanism) | yes (forecast scenario; monthly forecast patterns) | yes (named) | yes (AI baselines per cycle) | yes ("run your monthly forecast") | B |
| Driver-based planning + allocations | yes (named; expense allocations via rules engine) | buildable (modeling) | module-level (Financials/Workforce/Capital/Projects) | yes (named) | yes (named, driver cascade) | yes (named) | B |
| Predictive / AI baselines | yes (Predictive Forecaster, Planning Agent) | yes (Forecaster, CoModeler) | yes (Predictive Planning, Advanced Predictions, IPM Insights) | yes (Analyst/Planner agents) | yes (planning baselines, agents) | yes (ML predictions, FP&A Agent) | B — all 6; current-era common, not defining |
| Excel / spreadsheet-flavored input | not emphasized on fetched pages | Excel Add-in; Anaplan for Microsoft 365 | Smart View for Excel & Google Sheets | "Familiar Excel behaviour", Spotlight | "Keep Excel where it works" | not on fetched pages | B — common but uneven |
| Pre-built modules (workforce, capital, projects, sales) | Workforce/Ops Planning products | Applications (login-gated) + sales/workforce pages | Capital/Financials/Projects/Workforce modules; Sales Planning app | HR/Sales/Marketing/IT/Ops solutions | workforce planning use case | supply chain/HR/retail solutions | B |
| Long-range / strategic modeling | "long-term plans" | buildable | Strategic Modeling product | strategic planning framing | not on fetched pages | Strategic Long-term Planning page | B |
| Close/consolidation/reporting in same suite | Close & Consolidation product | separate positioning | EPM suite siblings | Plan/Close/Consolidate/Report | Close & Consolidation + Reporting | FCCR | B — suite expansion common |
| Deployment: cloud vs on-prem | cloud (fetched pages) | cloud (fetched pages) | cloud (Cloud EPM) | cloud | cloud | cloud or on-premise (explicit) | A (Board only); others not asserted |
| Methodology-agnostic (incremental / zero-based / driver-based as choices) | yes (incremental + zero-based named) | buildable | module choice | templates | yes (ZBB named) | not explicit on fetched pages | B |

## Canonical Model (synthesis)

### L0 — Defining Invariant (deliberately small)

1. **Multi-dimensional financial planning model** — the organization's plan is structured numeric data positioned along at least: financial accounts (chart-of-accounts structure), time periods, and organizational segments (entities/departments/cost centers). Remove the dimensional anchoring and it is not an organizational budgeting platform.
2. **Versioned plan data** — the same model holds multiple versions of the plan (budget, forecast, scenario variants) as first-class, switchable, comparable datasets, distinct from actual results. (Anaplan's mandatory, undeletable Actual version plus switchover mechanics is the sharpest single piece of evidence that the plan/actual separation is structural, not incidental.)
3. **A governed planning cycle** — the plan is produced and revised through a managed organizational process: contributions are made against a finance-defined structure, consolidated, reviewed, and approved toward an official plan state. (Present in all sampled products; Oracle documents the full mechanics.)

Nothing else is required: cloud delivery, driver-based planning, ML baselines, Excel add-ins, pre-built modules, approval-state names, rolling-forecast cadence — all removable and the product is still recognizably this Type.

Historical / market-sample check: the pre-platform baseline this category replaced (Excel + email budget packets) already had the L0 objects in degenerate form — a workbook is a 3-axis grid, copied sheets are versions, the email chain is the cycle — which supports the L0 as era-independent. On-prem/older CPM generations (Hyperion-era planning, BPC-style systems) share the same conceptual objects (dimensions, versions/scenarios, input schedules, submission workflow). The L0 does not require any current-market implementation pattern.

### L1 — Common Mature Structure

- actuals integration from GL/ERP at period close, and budget-vs-actual variance analysis (the payoff loop; near-universal — arguably core-adjacent, but a budget-setting tool without actuals import would still be this Type)
- rolling forecasts / recurring re-forecast cycles (forecast versions updated as actuals accrue)
- top-down targets vs bottom-up submissions (target setting, then department-level contribution)
- driver-based planning: operational drivers (headcount, volume, price, hiring) computing financial lines; allocations
- scenario/what-if management (shareable scenarios, personal sandboxes)
- planning workflow machinery: approval units / planning units, submission states, promotion paths, locked/released data
- dimension management + security (dimension-level / selective access, role-based access)
- input surfaces: web grids/forms for budget owners; Excel add-ins (Smart View, Spotlight, MS365 add-ins)
- dashboards, financial reports, board-ready reporting; drill-down
- predictive/statistical forecast baselines and AI assistants (all 6 sampled products ship some form — common but era-bound)
- pre-built planning modules: workforce/headcount, capital, projects, cash flow, sales/quota planning
- long-range / strategic modeling; integrated business planning reach into operational planning

### L2 — Variant / Optional Structure

- product philosophy poles: pure modeling platform (build the budgeting app yourself) vs module/application-led (pre-built budgeting content) vs finance-suite member (planning alongside close/consolidation/reporting)
- segment tuning: mid-market (guided, template-led, faster time-to-value) vs enterprise (modeling freedom, scale, governance)
- deployment: cloud vs on-premise (only Board asserted on fetched pages; not claimed for others)
- Excel posture: add-in writeback vs "familiar Excel behaviour" vs replace-Excel rhetoric
- industry editions/packs (construction, healthcare, higher-ed, retail merchandising…)
- scope expansion into financial close, consolidation, disclosure, reporting suites
- ERP-agnostic integration vs suite-native planning
- public-sector / appropriations shape → treated as a different directory Type (Public Budgeting Platform), not a variant here

### L3 — Vendor-specific (research notes only)

- Anaplan: switchover dates; Polaris calculation engine; CoModeler; Anaplan XL Reporting; Data Orchestrator; ALM revision tags; "Total Company" default top-level item
- Oracle: approval-unit state names (Under Review, Promote, Submit); Private Sandboxes as named feature; IPM Insights; Predictive Cash Forecasting; Infolets; Books; Smart View for Google Workspace flex forms
- Workday: Planning Agent, Predictive Forecaster, "AI-native modeling", AI explainability/confidence metrics
- Planful: Analyst / Planner / Help agents, Signals, Projections, MCP server, Spotlight for Microsoft 365
- Prophix: Budgeting Agent, "Autonomous Finance Platform", customer-efficiency statistics (marketing claims)
- Board: FP&A/Controller/Merchandiser/Supply Chain/Architect Agents, Board Foresight, Board Signals, on-prem option, analyst-recognized positioning

## Vendor-specific Findings

(Consolidated from L3 above; none promoted to the final document's core model.)

- The planning-workflow mechanism differs structurally: Oracle exposes fixed approval units with states; Anaplan has no fixed approval module — workflow is itself modeled in the platform; SaaS mid-market products embed guided workflow routing. The invariant is "the cycle is managed and attributable", not any specific workflow topology.
- Excel posture is a real market axis: Oracle/Planful/Prophix/Anaplan all provide Excel-adjacent entry, with different philosophies about whether Excel is the interface, a companion, or the problem being replaced.
- AI/predictive positioning is near-universal in the current generation but shallow-evidence (marketing-heavy); treated as L1-era flavor, not structure.

## Boundary Findings

- **Financial Planning & Analysis Platform** (sibling leaf, unprocessed): the sampled products market themselves under both names; "FP&A platform" is the broader umbrella (adds analysis/reporting emphasis, strategic planning), while "budgeting & forecasting" names the planning-cycle-centered slice. Products could not be cleanly partitioned by name. Joint-review flag recorded in STATUS.md. For this leaf, the defining center is held to be the governed budget/forecast cycle over the financial planning model.
- **Sales Forecasting Platform** (sibling leaf, unprocessed): inside these platforms, sales forecasting appears as a finance-side projection of revenue within the financial plan (and as quota/account planning modules, e.g. Oracle Sales Planning). The separate sales-side Type centers on CRM pipeline data owned by sales organizations. Boundary held: data source (pipeline vs financial model) and owning function (sales vs finance).
- **Financial Consolidation Platform**: consolidates *actual* results across entities for statutory close; budgeting plans *future* values. They meet at actuals (variance needs them) and at suite bundling (vendors sell both). Held.
- **General Ledger / Accounting Software**: books of record for actual transactions; may hold a simple account-by-period budget figure, but without versions, cycle machinery, or contribution workflow. Held — mirrors the consumer budgeting-application boundary ("no ledger semantics").
- **Business Intelligence Platform**: analyzes actuals history read-only; budgeting platforms write future versions under governance. Suite bundling blurs edges (Board explicitly fuses both). Held on write-direction + governance.
- **Financial Modeling Application**: analyst ad-hoc modeling tool; not an org-wide governed cycle over the chart of accounts. Held.
- **Public Budgeting Platform** (§24 government leaf): appropriations/funds domain objects and civic process; excluded as different domain, not a variant.
- **Budgeting Application (consumer sibling, already documented)**: personal plan vs organizational cycle; the sibling's recorded boundary ("corporate: departments, forecast versions, rollups, variance over business performance — different actors and objects entirely") is confirmed by this research. Consistent.
- **Spreadsheet Application**: the degenerate baseline. The distinguishing test: governance (who may change which cells, submission states) + shared single model + cycle. A spreadsheet lacks all three by construction.

## Uncertainties

- Vena, Datarails, Cube, Jedox, NetSuite PB, OneStream, CCH Tagetik not directly researched (gated or out of budget); conclusions rest on 6 products. The Excel-native pole (Vena-style) is described only generically ("Excel-flavored input" from fetched Oracle/Planful/Prophix/Anaplan evidence), not via Vena's own documentation.
- Help-center-level operational detail (exact workflow states, numeric limits, default cadences) unavailable for 4 of 6 products; all precise mechanics in the final doc are anchored to Oracle/Anaplan Tier-1 docs and phrased as "commonly" elsewhere.
- Workday help center was not attempted (JS-gated historically); Workday evidence is product-page level only.
- On-premise deployment asserted only for Board; not generalized.
- The precise historical evolution (Hyperion → PBCS etc.) was reasoned, not fetched; no dated claims made.

## Final Synthesis

A Budgeting & Forecasting Platform is the organization's system for producing and maintaining its financial plan as governed, multi-dimensional, versioned data. Its world is: a planning model whose cells mean (account, period, organizational segment); versions of that model — budget, forecast, scenarios — kept separate from actuals; and a recurring cycle in which targets are set, budget owners contribute, finance consolidates and reviews, and an official plan is approved and then measured against actuals. Everything else — drivers, rolling forecasts, AI baselines, Excel add-ins, modules, suites — is market-standard furniture around that core. The Type's edges are held by three tests: financial-account anchoring (vs generic planning), future-facing governed plan data (vs BI/consolidation/GL), and organizational cycle (vs personal budgeting and financial modeling). The FP&A Platform sibling remains a joint-review item because the market uses the two names for overlapping product categories.
