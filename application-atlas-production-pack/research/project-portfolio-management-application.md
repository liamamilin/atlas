# Research Notes — Project Portfolio Management Application

## Research Goal

Understand what a Project Portfolio Management (PPM) application actually is as an Application Type: what exists above the individual project, what objects and decisions define the portfolio layer, how selection/funding/capacity/monitoring work in real products, and where the Type's boundaries sit against project management, business-case management, work management, and the unrelated "portfolio management" of financial investments.

## Initial Boundary

- The core hypothesis: PPM manages **many projects (and related investments) as a governed collection** — deciding which work is taken on and funded, and watching the collection's aggregate money/capacity/progress — while a Project Management Application manages **one bounded undertaking**.
- Nearest neighbors: Project Management Application (below), Business Case Management Platform (decision slice, often a module inside PPM suites), Work Management Platform (ongoing team work), Agile Project Management (execution below/alongside), Financial Planning & Analysis (money planning in account structures), Portfolio Management System (financial investments — naming collision), Product Roadmap Application, Innovation/idea-management products, Professional Services Automation (commercial layer).
- Known pre-registered coordination obligations (from earlier passes):
  - project-management-application (processed 2026-09-08) defined this leaf as "adjacent (above)" and flagged joint review with unprocessed siblings incl. this one.
  - business-case-management-platform (processed) flagged that its Type is usually delivered as a module inside PPM/SPM suites (Planview, Clarity, Triskell) and recommended joint review.
  - portfolio-management-system (§08) flagged the "portfolio management" naming hazard and asked this pass to state the mirror-side distinction.

## Research Questions

1. What is the "portfolio" as a record? What is its unit of membership (projects only, or investments/programs/products/ideas)?
2. How does candidate work enter the portfolio (intake/demand/ideas) and how is it evaluated, selected, funded, rejected?
3. What is tracked at portfolio scope vs project scope (rollups, health, dashboards)?
4. How does cross-project resource/capacity planning work, and who does it?
5. What financial machinery exists (budgets, funding buckets, forecasts, actuals, capital/expense)?
6. Is project execution inside the product definitional, or can PPM sit above external execution tools?
7. What governance processes do the products encode (gates, reviews, scenarios, strategy linkage)?
8. Who are the users by role, and what does each do?
9. What is the minimal form of the Type (lightweight pole) and what does it omit?

## Representative Products

| Product | Pole / philosophy | Sources reached |
|---|---|---|
| Planview Portfolios (formerly Enterprise One) | enterprise classic; platform of five portfolio solutions; "sits above the tools where work happens" | official product page + solutions hub (Tier 2) |
| Clarity (Broadcom; "Project and Portfolio Management") | enterprise classic, IT heritage; two UIs (Clarity modern / Classic PPM); full docs reachable | official docs, Getting Started + doc tree (Tier 1) |
| Planisware (Orchestra/Horizon/Nova/Enterprise) | enterprise PPM incl. R&D/product development | official PPM page + root (Tier 2) |
| Meisterplan | lightweight, planning-first ("Lean PPM"); integrates to execution tools | official root + PPM feature page (Tier 2); help center timed out |
| Triskell Software | enterprise PPM suite (IT/R&D/strategic solutions) | official root (Tier 2) |

ServiceNow Strategic Portfolio Management was intended as a fifth/suite-pole sample but was not reachable (docs SPA returned a JS shell; product page timed out twice). Recorded as a sourcing limitation.

## Sources

Fetched 2026-09-08:

- Planview Portfolios product page — https://www.planview.com/products-solutions/products/planview-portfolios/ (fetched)
- Planview solutions hub — https://www.planview.com/products-solutions/ (fetched)
- Broadcom Clarity 16.4.2 — Getting Started — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/Getting-Started.html (fetched)
- Broadcom Clarity 16.4.2 — Using Classic PPM (doc tree; shows section families Demand Management / Financial Management / IT Service Management / Portfolio Management / Project Management / Resource Management / Requirements and Release Planning) — https://techdocs.broadcom.com/us/en/ca-enterprise-software/business-management/clarity-project-and-portfolio-management-ppm-on-premise/16-4-2/Using-Classic-Clarity-PPM.html (fetched)
- Planisware — Project and Portfolio Management (PPM) — https://planisware.com/project-and-portfolio-management-ppm (fetched)
- Planisware root — https://planisware.com/ (fetched)
- Meisterplan root — https://meisterplan.com/ (fetched)
- Meisterplan — Project Portfolio Management feature page — https://meisterplan.com/features/portfolio-management/ (fetched)
- Triskell root — https://triskellsoftware.com/ (fetched)

Not reachable (recorded limitations, do not fill from memory):

- ServiceNow docs (docs.servicenow.com) — JavaScript SPA shell only, two attempts; ServiceNow SPM product page timed out twice.
- helpcenter.meisterplan.com 404; help.meisterplan.com timed out — Meisterplan evidence is Tier-2 product pages only.
- Planview success.planview.com documentation portal — first URL guess 404; not pursued further (product pages served as the evidence base).

Evidence layers used below: **A** = directly observed on an official page of a named product; **B** = cross-product commonality across the sample; **C** = canonical inference.

## Product A — Planview Portfolios

### Key observations (Layer A)

- Positioning: one platform, "five solutions for every type of portfolio your enterprise runs. All five **sit above the tools where work happens** and bring **initiatives, investments, and resources** into a continuous, connected model of the business."
- Integration posture: "Planview sits above existing execution tools rather than replacing them. It connects to 60+ industry-standard tools — including Jira, Azure DevOps, ServiceNow… pulling credible execution signals without requiring teams to migrate."
- PPM solution framing (divisional/BU portfolios): "Prioritize the project portfolio with AI-scored ranking, **align resource capacity to what the organization can actually deliver**, and connect every program to the outcome it was **funded** to produce."
- Planview Portfolios feature tiers (product page):
  - Strategy: Strategic Alignment ("Translate high-level missions and objectives into specific investments"), OKRs, Roadmapping, **Investment Prioritization** ("Rank and analyze investments by business drivers and use what-if scenarios to compare options. Create an optimized portfolio"), **Financial Planning** ("Set financial targets for your portfolios. Manage to them with capabilities for budgeting, forecasting, and tracking costs and benefits").
  - Planning: **Product & Program Funding** ("incremental funding at multiple levels… Visualize impact of funding changes on desired business outcomes"), **Demand Management** ("Collect and evaluate demand across the enterprise from unstructured ideas to formal program and project requests"), **Capacity Planning** ("Make the right tradeoffs to optimize people and money"), **Scenario Planning** ("Create and compare scenarios to evaluate alternative prioritization, staffing, and timing options"), Program Management, Agile Team Planning, **Forecast and Actuals** ("Forecast costs and track actuals against the budget within and across portfolios. Balance your portfolio for capital and expense constraints").
  - Execution: Resource Management, Project Planning & Management, Hybrid Work Delivery, Workflows, Time Reporting, Costs and Actuals, Agile Costing.
  - Analytics & Reporting: portfolio reporting/dashboards ("portfolio, program, product, and project landscape"), embedded Power BI.
- Customer evidence (vendor case quotes on official pages): Corning — "combined them into one capital portfolio… visibility into the costs as well as the benefits… which projects are actively being worked on and how they are progressing in our **capital stage gate process**"; UPS — "consolidated funding decisions from 28 separate committees into a single platform"; NatWest — "35+ portfolios and 4,000+ projects to a ~$1B annual investment strategy."
- The vendor also sells adjacent single-purpose products (IdeaPlace innovation management, Roadmaps, PPM Pro, ProjectAdvantage/Sciforma, AdaptiveWork), showing the market packages demand-intake and roadmap functions both inside PPM and as standalone products.

## Product B — Clarity (Broadcom)

### Key observations (Layer A, Tier-1 operational docs)

- Product name itself: "Clarity — Project and Portfolio Management (PPM)".
- Framing: "Clarity helps you transform your organization **from managing projects to developing your initiatives as a true product or program portfolio**… Instead of running one-off projects, you can see your **money, people, and work** by product or service lines."
- **Investment types** (the unit of membership): four named types — **Projects** ("most large initiatives that have complex tasks… managed every day by a group of people"), **Ideas** ("captured in Clarity… a small group of people can work on them to create a viable prototype. Stakeholders can then decide if this idea has enough merit to be **converted into a fully-fledged project**"), **Custom Investments** ("align your investment nomenclature with your initiatives"), **Teams** ("fund the teams delivering value, not the work itself… persistent long-term funding").
- **Hierarchies**: "define parent-child relationships between investments… aggregation and calculation metrics to **roll up data automatically**. Then, you can view details, such as **total capital cost, operational cost, and return on investment**, for investments associated with each objective."
- **Objectives** (OKR workspace), **Roadmaps** ("highlight how your current investments are tied to organizational objectives… create new roadmap items… tied to new investments").
- **Staffing** workspace: "manage resource allocation for **all types of investments**… all key staffing metrics: **Availability, Allocation, Assignments, and Actuals**."
- **Timesheets** ("how much actual time a resource is spending on an investment. This helps determine both progress and cost").
- **Financials module**: "analyze your team's **planned, actual and forecasted budgets** in real-time… reconciling actual costs and **capitalization** associated with investments."
- Modules on investments: Tasks, **Status** ("create, manage, and publish status reports for various investment types"), **Risks, Issues, Changes**, Checklists, Agreements. Plus **Plans** (workforce analysis), Reporting, Administration (Blueprints, field-level security, SAML/API).
- Doc tree of Classic PPM confirms the classic module families: Demand Management, Financial Management, IT Service Management, **Portfolio Management**, Project Management, Resource Management, Requirements and Release Planning.
- Deployment: install/upgrade documentation exists — on-premise packaging is a real variant.

## Product C — Planisware

### Key observations (Layer A, official PPM page)

- The vendor's own "6 Key Project Portfolio Management Capabilities":
  1. **Demand management** — "the processing of all proposals that would impact current and future projects (project demands, ideas, and change requests)": collect and centralize demands in a single area; **assess the value and cost of each demand and identify the dependencies**; make decisions with transparency; ensure the connection between expressed needs and what is implemented. (Screenshots: "Idea intake dashboard", "Idea kanban".)
  2. **Portfolio management** — "Once project possibilities are identified, the **portfolio manager gets a set of projects that must be qualified, prioritized and validated**. They need to analyze the **overall coherence** of the organization's projects so that **duplicates are avoided, resources are focused on value-added projects and load is balanced** throughout the year." Actions: "Formalize strategy by structuring it in portfolio form"; "Consolidate projects for global strategic analysis"; "Define and present the organization's **financial and resource constraints**"; "**Arbitrate various scenarios** depending on priority and resource capacity." (Screenshot: "Portfolio Executive Summary".)
  3. **Project & product management** — Gantt, to-do lists, Kanban, templates, hybrid waterfall/agile/stage-gate.
  4. **Resource Management** — "role or named resources, assignment rules, timesheets… Anticipate team **capacity and availability**; Optimize workload… Get a single timesheet."
  5. **Budget & cost management** — "plan, track in real-time, and analyze the **financial performance of projects**… budgets globally or in detail (labor, expenses, materials and equipment)… centralized view on project costs (planned, actuals, payments)… reliability of forecasts and budgetary outcomes." (Screenshot: "Project cash flow".)
  6. **Collaboration & reporting** — "take decisions based on past findings, real-time monitoring, and forecasting."
- Product family split by portfolio domain: Orchestra ("Turnkey PPM Solution for PMOs"), Horizon ("IT Strategic Portfolio Management"), Nova ("SPM for Product Development"), Valoris ("CAPEX & Asset Investment Planning"), Enterprise. Root page framing: "picking better projects, managing them smarter" — "structured methods to **score, compare, and prioritize** initiatives"; "real-time visibility into **availability, skills, and workloads** across projects, programs, and portfolios."

## Product D — Meisterplan

### Key observations (Layer A, Tier-2 product pages; help center unreachable)

- Positioning: "Portfolio-Level Resource Management Software… Coordinate projects across multiple teams… **regardless of the tools or methods your teams use**."
- Three-step "How It Works": "**Establish Portfolio-Level Visibility** — Move up one level to get an overview of all projects, regardless of the tools your teams are using"; "**Plan Future Resource Needs at a High Level** — …a solid basis for planning decisions without getting lost in unnecessary details"; "**Simulate Scenarios in Real Time** — Find the best solution for planning conflicts across all projects, departments, and time horizons."
- PPM feature page: "Drive What Matters Most — Ensure all your **initiatives** contribute to your company's **goals**" (Goals view: "Assign all your investments to goals"); "Unblock Projects Before They Stall — The secret to good portfolio management? **Resource planning**!… ensure availability across projects and resolve bottlenecks"; "Track Progress with Confidence — Monitor overall **portfolio progress**… your **pipeline**, roadmap, and goals"; "**Establish the Right Projects, from Proposal to Execution** — a clean and lean **project intake** process with Meisterplan's dedicated **portfolio-level Kanban board**. Cultivate a **pipeline** of beneficial, strategically relevant and **qualified** initiatives"; Roadmap view ("milestones and dependencies"); **Portfolio Dashboard** ("automatically compiles a high-level summary of your KPIs to guide management through **performance monitoring, issue detection, and strategic steering**"); Team Planner ("full transparency on **allocations** and capacities").
- Glossary (vendor's own conceptual vocabulary): "Initiatives — Synonym for → **Project**"; "Allocation — the strategic process of identifying the correct resources for projects or individual tasks and assigning them accordingly"; "Resource — employees, budgets, materials and time".
- **Deliberately no task execution**: integrations (Jira, Asana, Smartsheet, ServiceNow, Microsoft Products, REST API) make Meisterplan "the central planning hub" while teams execute elsewhere. Feature list has no task management.
- Stakeholder list (vendor): PMO Director, Executive, **Resource Manager**, Project Manager, Team Member.
- Other feature families: Project Lifecycle Management, Demand and Project Prioritization, What-If Scenario Planning, Reporting Dashboards, Financial Management, Plans vs. Actuals, AI.

## Product E — Triskell Software

### Key observations (Layer A, official root)

- Positioning: "Enterprise Project Portfolio Management software… Manage **strategy, resources, budgets and plans** in a single solution to improve **visibility, decision-making and value delivery**."
- Solution set: Strategic Portfolio Management, Project Portfolio Management, Agile Portfolio Management, IT Portfolio Management, New Product Development, Transformation Program, **Resource Management, Demand Management, Financial Management**.
- "Capture, align, and link **objectives, initiatives, programs, and portfolios** across your organization."
- Specific capabilities named: OKRs and SMART goals cascade; Balanced Scorecards; "**Balance Capacity Planning with incoming demand**"; What-if Scenario feature; "Waterfall, Phase-Gate, Agile, Scaled Agile or any framework from a single PPM solution"; "Bring your **Lean budgeting** processes to the platform."
- Customer quote (Eramet, on official page): "Triskell fulfills the need for **macro-management at the portfolio level and micro-management at the project management level**… managing projects in a traditional (Waterfall) and Agile way."

## Cross-product Comparison

| Structure | Planview Portfolios | Clarity | Planisware | Meisterplan | Triskell | Layer |
|---|---|---|---|---|---|---|
| Collection-of-work record above projects ("portfolio") | portfolios of investments | hierarchies of investments; classic Portfolio Management | "structuring [strategy] in portfolio form; consolidate projects" | overview of all projects; single plan | "initiatives, programs, and portfolios" | A×5 |
| Unit of membership broader than "project" | initiatives, investments, programs, products, epics | four investment types: Projects, Ideas, Custom Investments, Teams | projects + demands/ideas/change requests | initiatives (= projects per glossary); investments assigned to goals | objectives, initiatives, programs, portfolios | A×5 |
| Candidate intake (demand/ideas) → decision | Demand Management ("unstructured ideas to formal requests") | Ideas ("decide if this idea has enough merit to be converted"); classic Demand Management | Demand management ("assess the value and cost of each demand") | project intake pipeline on a portfolio-level Kanban board | Demand Management solution | A×5 |
| Selection / prioritization / funding recorded at portfolio scope | Investment Prioritization ("rank… by business drivers"; "create an optimized portfolio"); Product & Program Funding ("incremental funding at multiple levels") | ideas approved into projects; teams "funded"; financial plans | "qualified, prioritized and validated"; "score, compare, and prioritize" | Demand and Project Prioritization; Goals | OKR/BSC cascade; PPM solution | A×5 |
| Cross-project money picture (budget/forecast/actuals) | Forecast and Actuals; "Balance your portfolio for capital and expense constraints" | Financials module (planned/actual/forecast; capitalization) | Budget & cost management; cash flow | Financial Management; Plans vs. Actuals | Financial Management | A×5 |
| Cross-project people picture (capacity/allocations) | Capacity Planning ("optimize people and money") | Staffing (Availability, Allocation, Assignments, Actuals) | Resource Management ("anticipate capacity and availability") | Resource Capacity Planning + Team Planner (core identity of the product) | Resource Management | A×5 |
| Portfolio-level monitoring / rollup | Dashboard Analytics; portfolio reporting | Hierarchies ("roll up data automatically… total capital cost, operational cost, ROI"); Status reports | Portfolio Executive Summary; KPI reporting | Portfolio Dashboard ("high-level summary of your KPIs") | "visibility… macro-management at the portfolio level" | A×5 |
| What-if / scenario comparison | Scenario Planning | (scenario semantics not fetched — not asserted) | "Arbitrate various scenarios" | What-If Scenario Planning (core) | What-if Scenario feature | A×4 |
| Strategy linkage objects (OKR/goals) | OKRs; Strategic Alignment | Objectives (OKR workspace); Roadmaps tied to objectives | "Formalize strategy… in portfolio form" | Goals view ("assign all your investments to goals") | OKRs + SMART + Balanced Scorecards | A×5 (depth varies) |
| Roadmaps | Roadmapping | Roadmaps | Product & Roadmapping capability | Roadmap view | (solutions imply; not explicitly named — not asserted) | A×4 |
| Execution inside the product | yes (Project Planning & Management, Hybrid Work Delivery, Agile Team Planning) | yes (Tasks, status, risks; classic Project Management) | yes (project & product management) | **no — integrates with Jira/Asana/etc.** | yes (project + program management; waterfall/agile) | A×5 (divides the sample) |
| Timesheets / actual effort | Time Reporting | Timesheets | single timesheet | plans vs. actuals (integration-mediated; not asserted in detail) | (not asserted) | A×3–4 |
| Programs as intermediate container | Program Management | (program portfolio in positioning) | "projects, programs, and portfolios" | (not named on fetched pages) | programs | A×3+ |
| Stage gates / lifecycle governance | (stage gates in customer quote) | ideas → prototype → project conversion | "waterfall, agile, stage-gate" planning modes | Project Lifecycle Management | Phase-Gate named | A×4 |

### Stable cross-product reading (Layer B)

Every sampled product, regardless of depth or philosophy, operates the same three-part structure:

1. a **persistent collection of work investments** (portfolio/hierarchy) whose members are broader than "projects" — programs, products, ideas/demands, funded teams;
2. an **intake → evaluate → select/fund decision loop** carried out against comparables (value, cost, strategy fit, capacity) with the decision recorded at portfolio scope;
3. a **reconciled aggregate picture across member investments** — money (budget/forecast/actuals) and people (capacity/allocations) and progress — which the governing roles read and act on by re-selecting, re-funding, re-allocating, or stopping work.

What divides the sample is packaging, not structure: execution can be inside the product (4 of 5) or deliberately external via integrations (Meisterplan); strategy linkage ranges from full OKR workspaces to a simple goals view; scenario tools range from spreadsheets-grade comparison to real-time simulation.

## Canonical Model (Layer C)

### L0 — Defining Invariant

A Project Portfolio Management Application is the system of record for governing a collection of work investments as a portfolio. Three jointly-held structures:

1. **The portfolio as a managed collection of record** — a persistent, named collection above individual projects; its members are work investments (projects, programs, products, ideas, funded teams). Remove → a project management tool (one undertaking) or a bare list/dashboard over projects.
2. **The select-and-fund decision loop at portfolio scope** — candidate work enters as demand/ideas/requests, is evaluated against comparables (value, cost, strategy fit, capacity), and is selected/rejected/defunded with recorded outcomes; new work is admitted and funded through this loop. Remove → passive reporting over existing projects (no governance), or an idea/business-case tool that stops at the approval gate.
3. **The cross-portfolio reconciling picture** — aggregate money (budget/forecast/actuals) and aggregate people (capacity/allocation) plus progress, computed across member investments and kept current as they execute, so the governing roles can rebalance (reprioritize, reallocate, fund, stop). Remove → a static approved-projects register or a decision log with no follow-through.

Jointly-held is load-bearing: (1) alone = a list of projects; (2) without (3) = business-case/idea management that ends at the gate; (3) without (2) = a portfolio dashboard; (1)+(2) without (3) = selection with no run-state reconciliation; (1)+(3) without (2) = monitoring without governance.

### L1 — Common Mature Structure

- A distinct **demand/idea intake object class** feeding the portfolio (named "demand management" by 3 of 5 vendors).
- **Prioritization frameworks** (scoring/ranking by business drivers; goal or OKR linkage at varying depth).
- **Scenario / what-if comparison** of portfolio compositions (4 of 5 sampled; strong market expectation, not definitional — a spreadsheet-era portfolio office could operate without it).
- **Funding machinery**: budgets on investments, funding levels/buckets, forecasts, actuals, capital vs expense treatment.
- **Capacity/allocation planning surfaces** (planner views, allocation records, availability).
- **Roadmaps** as portfolio-scope communication artifacts (4 of 5).
- **Portfolio dashboards / executive reporting / status reporting**.
- **Programs** as an intermediate container between portfolio and projects.
- **Timesheets/actual effort** feeding cost and progress.
- **Lifecycle governance forms**: stage gates, review cadences, status/risk modules.
- Multi-portfolio organization and rollup hierarchies.

### L2 — Variant / Optional Structure

- **Execution posture**: execution inside the same product (suite PPM) vs. planning-hub posture with execution delegated to external task/agile tools via integration (documented in both directions).
- **Domain flavor**: IT portfolio (Clarity heritage, IT PPM solutions), R&D / new product development (Planisware Nova, Planview NPD solution), capital/CAPEX portfolios (customer evidence; a vendor sells a dedicated CAPEX product), enterprise transformation.
- **Deployment**: on-premise enterprise packaging (Clarity install docs) through SaaS.
- **Strategy-object depth**: OKR workspaces vs simple goal tagging vs scorecards.
- **Agile machinery** above teams (agile costing/capitalization, scaled-agile support) — present in some, absent in others.
- **Innovation/idea management** as either built-in intake or separate products.
- **AI assistance** (era-current; all sampled vendors market some form) — not definitional.

### L3 — Vendor-specific (research notes only)

- Clarity's named investment types (Projects/Ideas/Custom Investments/Teams), Blueprints, Vaia (AI), MCP server, Jaspersoft reporting, Classic-vs-Clarity dual UI.
- Planview's five-solution platform packaging, Anvi conversational AI, Hub toolchain integration, Connected Work Graph, IdeaPlace/Roadmaps/PPM Pro/ProjectAdvantage product constellation.
- Planisware's Orchestra/Horizon/Nova/Valoris/Enterprise product split and Prisma AI layer.
- Meisterplan's Lean PPM framework branding, trial templates, MCP integration.
- Triskell's Balanced Scorecard emphasis, industry packaging, ISO/SOC certifications.
- Customer anecdotes (UPS 28 committees → one platform; NatWest 35+ portfolios/4,000+ projects; Corning capital stage-gate; RIMOWA IT portfolio manager quote) — illustrative only.

## Boundary Findings

- **vs Project Management Application (below; most important seam).** The managed record differs: PM = one bounded undertaking with its plan of owned/dated tasks tracked to that undertaking's end; PPM = the collection of undertakings plus the selection/funding/capacity decisions taken across them. The PM loop is plan→execute→complete within a project; the PPM loop is propose→evaluate→select/fund→balance→review across projects. Test in both directions: strip the portfolio layer (intake/selection/funding/cross-project capacity reconciliation) from a PPM product and a project management tool remains (Meisterplan proves the inverse is also a market shape: portfolio planning with execution delegated to external PM tools). Single products legitimately ship both layers as different capability tiers — the managed object, not the feature list, is the seam. Confirms and refines the PM pass's "adjacent (above)" note.
- **vs Business Case Management Platform (decision slice).** The business-case Type centers the investment proposal + appraisal + approval gate. In PPM those decision semantics are one leg of three and are followed by funded execution, run-state reconciliation, and rebalancing. Market packaging agrees: that pass recorded that business-case machinery ships as a module inside PPM/SPM suites (same suite names appear in both passes). Keep both Types; cross-reference.
- **vs Portfolio Management System (§08, financial investments).** Mirror-side naming hazard: "portfolio management" in finance = managing securities/investments (instrument/position/account objects); here = governing work investments (project/program/initiative objects). No shared objects, users, or workflows. The two Types must state the mirror-side distinction in their documents.
- **vs Work Management Platform (unprocessed sibling).** Work-management centers a team's whole ongoing operational work (requests, processes, approvals) where projects are one container; PPM centers the governed investment collection above projects. This pass re-affirms the PM pass's flag: joint review needed when work-management-platform is processed. Also to be reconciled then: task-management-application / to-do-list-application and professional-services-automation flags.
- **vs Financial Planning & Analysis Platform.** FP&A plans enterprise money in account × time × org structures; PPM's financial layer is project-anchored (budgets/funding/actuals on investments). They exchange data (forecasts, actuals) but the center of gravity differs.
- **vs Product Roadmap Application.** The roadmap in PPM products is a view/communication artifact over investment records, not the record itself. A standalone roadmap tool centers the timeline artifact.
- **vs Agile Project Management / Enterprise Agile Planning.** Agile PM = standing team backlog re-planned per cadence; PPM = selection and funding above/around team execution. Products may contain both; Meisterplan's integration posture and Planview's separate EAP solution show the market keeps the seams visible.
- **vs Innovation / idea management products.** Idea capture can be standalone; in PPM intake is the entry to the select-and-fund loop, and the loop continues past capture into funding and reconciliation.
- **vs Application Portfolio Management (§14).** Same word "portfolio", different object: APM governs installed applications/technology assets; PPM governs work investments. Worth one clarifying line in the final document.
- **vs decarbonization/strategy-execution platforms.** The decarbonization pass explicitly excludes "generic strategy-execution/project-portfolio machinery"; consistent — those products anchor on measured emissions, not on the governed work collection.

## Historical / Market-Sample Check (per §24 rule)

- Paper-era analog: a capital/IT investment office with project request forms, an annual approved-projects ledger carrying budgets, a master staff-allocation plan across projects, and quarterly review meetings that add, stop, or re-fund projects — satisfies all three L0 legs without software-era machinery (no AI, no OKR objects, no Gantt, no cloud).
- Classic 2000s enterprise PPM (the CA Clarity/Planview lineage the vendors themselves name) carries the same three legs; "PPM" as a product category name predates the modern strategy/agile/AI packaging.
- The definition deliberately names no AI, no OKRs, no agile, no stage gates, no roadmaps, no scenario simulators, no SaaS — all are characteristic of current market realizations, not the Type.

## Uncertainties

- ServiceNow SPM (a category-leading suite offering) was not directly observed; its inclusion as a representative product would likely have strengthened the suite pole but not changed the structure, given the convergence observed.
- Meisterplan's operational documentation (help center) was unreachable; its lifecycle states, scenario-comparison mechanics, and financial module depth are asserted only at product-page strength.
- Clarity's classic Portfolio Management sub-page (portfolio/scenario object semantics) was not fetched; Clarity observations come from the Getting Started page and the doc tree.
- Exact limits, state-label sets, and rollup formulas across products were not researched and are not asserted anywhere.
- Whether strategy-linkage (OKR-class objects) is trending toward definitional status in the market ("strategic portfolio management" naming) is possible but unproven; kept at L1 with the depth-variance note.

## Final Synthesis

The Type's center is a governance loop, not a bigger Gantt chart. A Project Portfolio Management Application holds a persistent collection of work investments, runs candidate work through a recorded select-and-fund decision loop against value/cost/strategy/capacity comparables, and maintains a reconciled aggregate picture of money, people, and progress across the collection that the governing roles use to keep rebalancing the portfolio as execution unfolds. Execution may live inside the product or in connected tools; strategy objects, scenarios, roadmaps, gates, and intake machinery are the mature-market layers on top; the defining core is the collection + the decision loop + the reconciling picture.
