# Research Notes — Public Budgeting Platform

## Research Goal

Understand the public budgeting platform category: what software governments use to build, review, adopt, publish, and manage their budgets; who the participants are; what objects the system holds; how the annual budget cycle flows through it; and where it borders the neighboring Types (corporate Budgeting & Forecasting, Public Financial Management System, Capital Improvement Planning, Government Transparency Portal, Government Performance Management, Government Revenue/Grants/Procurement).

This pass also discharges (from this side) one boundary flag previously recorded against this unprocessed leaf:

1. capital-improvement-planning (2026-09-09): "packaging seam — multiple public budgeting suites ship capital-planning modules (verified in Euna Budget Capital; market anchors suggest the pattern is common), so the product-level boundary between 'CIP application' and 'budgeting suite with a capital module' is fuzzy; type-level boundary held by center of gravity (multi-year project register + funding-source allocation + governed multi-year adoption vs annual expense authority by fund/line item); no alias/duplicate declared — recommend joint review when Public Budgeting Platform is processed."

## Initial Boundary

Working hypothesis before research:

- A public budgeting platform is the software a government (municipality, county, state/province, national ministry, school district, public authority) uses to run its budget cycle: departmental budget requests → central budget office review/adjustment → proposed budget → adoption by the governing body → execution monitoring/amendments → budget book publication.
- The budget itself is not a private forecast: it is the government's formal spending plan, organized in the government's fiscal framework (funds, departments, account classifications), publicly scrutinized, and legally/governance-framed (appropriations, balanced-budget rules).
- Nearest neighbors: corporate Budgeting & Forecasting Platform (§08) — same verb "budgeting," different standing of the object; Public Financial Management System (§24) — the whole-of-government fiscal architecture of which budgeting is one cycle; Capital Improvement Planning (§24) — the multi-year capital project register that budgeting suites commonly embed as a module; Government Transparency Portal (§24, processed) — budget publication as an output surface; Government Performance Management (§24, processed) — performance budgeting linkage.
- Unknowns: whether execution controls (appropriation/commitment checking) are definitional or common; whether the adoption step is inside the platform's core or only supported; how the US local-government pole (GFOA/GASB/ACFR machinery) differs from the international PFM pole; whether the federal defense variant (PPBE) fits the same core.

## Research Questions

1. What is the unit of record — what exactly does the system hold as "the budget"?
2. What fiscal structure organizes it (funds, departments, cost centers, chart of accounts, fiscal periods)?
3. Who participates in building it, and what does each participant do (departments, budget office, finance, HR, executives, governing body, public)?
4. What are the phases of the cycle the platform supports, and which are inside vs outside the platform?
5. What budgeting content types exist (operating, personnel/position, capital, revenue, performance/program)?
6. How do scenarios, versions, and mid-year changes work?
7. How does the platform connect to budget execution (ERP/GL, appropriations, commitments) and to publication (budget books, open budget portals)?
8. What is public-sector-specific vs generic planning machinery?
9. Where are the boundaries vs corporate budgeting, PFM systems, CIP, transparency portals, and performance management?
10. Would older / non-US / differently-positioned realizations still fit the definition?

## Representative Products

Selected for market coverage, product-philosophy diversity, and documentation access:

1. **Euna Budget** (Euna Solutions; Questica lineage) — the purpose-built public-sector budgeting suite pole (US/Canada local governments, states, education, nonprofits); full-cycle module set (strategic / performance / personnel / operating / capital / transparency publishing). Reachable product pages; help center 403.
2. **FreeBalance Accountability Suite™** — the national-government PFM/GRP pole (25+ countries; Philippines Department of Budget Management, Bougainville, Micronesia, Brazil); budgeting as the center of a whole-of-government fiscal suite; budget formulation + execution controls vocabulary (appropriations, allotments, commitments, budget transfers).
3. **Neubrain** — the public-sector budgeting analytics pole (US federal/state/local; DoD PPBE and Congressional Budget Justification; counties, cities, housing authorities); performance-based budgeting + budget books/CAFR reporting.

Market anchors, unreachable and therefore used only for market structure (no product-specific claims drawn):

- **OpenGov** (Budgeting & Planning) — opengov.com and support.opengov.com returned 403 in three separate prior passes (government-performance-management, government-transparency-portal) and was not retried this pass; the largest US local-government budgeting brand, market anchor only.
- **ClearGov** (Budget Cycle) — cleargov.com returned 403 in two prior passes; market anchor only.
- **Tyler Technologies** (Munis ERP budgeting) — tylertech.com returned 403 this pass (first attempt); the ERP-embedded budget module pole, market anchor only.

Domain authorities:

- **NASBO — Budget Processes in the States & Territories** (National Association of State Budget Officers): the canonical comparative reference on state budget cycles, participants, authorities, documents, monitoring, and performance.
- **FreeBalance's own PFM definition** (vendor, but a clean statement of the budget cycle: formulation → execution → accounting/reporting → audit).

## Sources

All fetched 2026-09-09:

- Euna Solutions — Budget (suite page): https://eunasolutions.com/solutions/budget/
- Euna Solutions — Operating Budgeting: https://eunasolutions.com/solutions/budget/operating-budgeting/
- Euna Solutions — Personnel Budgeting: https://eunasolutions.com/solutions/budget/personnel-budgeting/
- Euna Solutions — OpenBook Transparency Budgeting: https://eunasolutions.com/solutions/budget/transparency-budgeting/
- FreeBalance — home: https://www.freebalance.com/en/
- FreeBalance — Products (Accountability Suite): https://www.freebalance.com/en/products/
- FreeBalance — Public Financials Management: https://www.freebalance.com/en/products/public-financials-management/
- FreeBalance — PFM Modules: https://www.freebalance.com/en/products/public-financials-management/pfm-public-financials-management-modules/
- Neubrain — home: https://www.neubrain.com/
- Neubrain — Government Budgeting Software: https://www.neubrain.com/solutions/government-budgeting-software
- NASBO — Budget Processes in the States & Territories: https://www.nasbo.org/reports-data/budget-processes-in-the-states

Prior-pass observations reused (recorded 2026-09-09, capital-improvement-planning pass):

- Euna Budget — Capital Budgeting module page: https://eunasolutions.com/solutions/budget/capital-budgeting/ (project budgets, funding sources, multi-year plan, post-adoption tracking, capital–operating linkage, GIS map publication)

**Source-access limitation (load-bearing for assertion calibration):**

- The entire large US vendor pole (OpenGov, ClearGov, Tyler Technologies) is unreachable (403, consistent across passes). The US market-leader realization is therefore evidenced only at market-structure level; no feature sets, state names, or numeric limits are asserted for that pole.
- Euna's operational help center (help.eunasolutions.com) is 403; all Euna evidence is Tier-2 product pages (suite + module pages + FAQs printed on those pages). No Tier-1 operational docs for any sampled product were reachable.
- No precise operational facts (submission deadlines, approval-chain depths, amendment thresholds, fiscal-year defaults) are asserted anywhere; the sampled pages do not state them.

## Product Observations

### Euna Budget (Euna Solutions; Questica lineage) [Evidence layer A — Tier 2 product pages]

- Positioning: "A full-cycle budgeting solution built for how the public sector actually works. It connects planning, forecasting, management, and reporting." "Supporting you through every stage of the budget cycle from planning and forecasting to publishing and sharing results."
- Who it serves: "public sector organizations of all sizes, including towns, cities, counties, states, educational institutions, and non-profits"; Professional tier for small/mid organizations, Enterprise tier "for the largest and most complex agencies such as major cities, states, state agencies, and federal governments."
- Module set (the suite's own articulation of budget content types):
  - **Strategic Budgeting** — "Align every dollar to strategic priorities."
  - **Performance Management** — "tracking and measurement of KPIs… throughout the budget cycle."
  - **Personnel Budgeting** — "Accurately forecast salaries, benefits, and staffing costs… your largest expense."
  - **Operating Budgeting** — "Manage day-to-day expenses."
  - **Capital Budgeting** — "detailed project budgeting and multi-year funding oversight."
  - **OpenBook: Public Transparency** — "Publish digital budget books and ACFRs, then share them with your community through an interactive public portal."
- Operating budgeting workflow (module page): three-step framing **Forecast → Formulate → Analyze**:
  - Forecast: "Project future budgets… Use scenario planning to test alternative allocations and outcomes; Update projections quickly as assumptions or funding shift." "Model 'what-if' scenarios… Compare multiple budget scenarios… Duplicate organizations to explore alternative plans quickly."
  - Formulate: "Draft operating budgets by department with intuitive workflows, categorized cost centers, and accessible entry tools. Use a user-friendly interface designed for non-finance staff; Structure spending by department or fund, simplifying oversight and edits; Handle approval workflows effortlessly across your organization." "Configure workflows to match your agency's setup; Integrate with your ERP or financial system to eliminate duplicate entry; Sync budget calendars with tools like Google or Outlook."
  - Analyze: "Compare planned vs. actuals across funds, departments, and cost centers; Monitor variances throughout the year to stay on budget; Generate reports that meet public sector standards."
- Collaboration model: "Unite departments into a centralized and secure workspace with clear roles, permissions, and approvals." FAQ: "The platform centralizes department and fund-level budgets into a single hub… Department heads can easily manage their cost centers, submit requests, and track adjustments without the headaches of juggling spreadsheets." "Stakeholders can submit, review, and approve budget requests. Notifications, role-based access, and centralized dashboards."
- Mid-year changes: "You can process change requests and updates, even after budgets are published, while maintaining an auditable history of every adjustment."
- Role-based access: "Assign roles to distribute workload efficiently; Limit access to prevent errors, non-compliance, and unauthorized changes."
- Personnel budgeting (module page): "Model and manage salaries, benefits, and positions… Connect finance and HR data to keep positions, costs, and priorities in sync." "Track by position or individual and roll up to department or organization level; Handle mid-year hires, reclassifications, and benefits updates; Maintain accuracy with built-in version control." Compensation machinery: "grid-based compensation… benefits, allowances, and employer taxes, with support for separate pay scales for union and contract roles… base wages as fixed salary amounts or percentiles within a configured grade range… benefits-on-benefits calculations." **Position control**: "Manage position funding across cost centers, accounts, or grants… Support complex funding splits across multiple sources." What-if: "simulate budget impacts from changes like added roles or salary step increases."
- Capital budgeting (prior-pass observations, same vendor): project budgets with funding sources (grants, cost centers), multi-year capital plan and timelines, post-adoption oversight of expenditures and balances across years, funding strategies/phasing/debt/maintenance forecasts, capital–operating linkage, GIS/map publication of projects.
- Publication/transparency (OpenBook page): "Financial Publisher — Build and publish dynamic publications, including Budget Books, ACFRs, and more with direct integration to your budget data… interactive digital versions or export to PDF… Align publications with GFOA award standards." "Public Portal — Host and present financial information in a centralized, easy-to-navigate website where stakeholders can explore budgets, projects, and reports. Display Budget Books, ACFRs, and CIPs in one place." "Statement Builder — Create technical financial statements and disclosures." "GFOA Award Checklist — Built-in checklists help teams track GFOA award requirements." "Dynamic Charts & Tables — Click through charts to uncover data by fund, department, or project." "Content Automation — automatically generating department pages, fund summaries, capital project sheets." "Interactive CIP Mapping." Sync: "When your budgets update in the Euna system, those changes sync to OpenBook channels automatically."
- Compliance frame: "Meet GFOA, GASB, and accessibility standards"; "FOIA-Ready Audit Trails"; "Public Transparency Tools Built-in"; ERP integrations "crucial for key financial information."
- Customer-voice evidence of the division of labor: "a powerful budgeting tool that enables all users to properly track and manage their own budgets, allowing the Finance Team to spend more time on analysis and planning" (Finance Director, city); "Having the budget and actual details together in one spot" (university program director).

### FreeBalance Accountability Suite™ [Evidence layer A — Tier 2 product pages]

- Positioning: "a commercial off-the-shelf, Government Resource Planning (GRP) solution that covers the entire budget cycle and manages all critical government fiscal systems." Customers: national governments across 25+ countries ("trusted to manage $425 billion in budget dollars" — vendor claim, not asserted).
- Canonical cycle statement (vendor's own definition of PFM software): "an integrated financial management system used by governments to manage the entire budget cycle. This includes **budget formulation, budget execution, accounting and reporting, and audit**. Typically, all ministries, departments and spending agencies of a government are connected to a single, unified system."
- Public-sector specificity claim: "Commitment accounting and budget management are unique to the public sector, enabling budgetary and commitment controls."
- PFM pillar modules (budget machinery inside the suite):
  - **(PFPF) Core Public Financials** — "budget controls, appropriations management, commitment accounting, and a robust Chart of Accounts… double-entry bookkeeping, real-time ledger updates."
  - **(PFBC) Budget Controls** — "multiple aggregate budget controls… equal and unequal allotments… soft and hard commitments/obligations… de-commitment and de-obligation functions. Providing real-time 'free balance' status… the ability to predict budget deficits and surpluses."
  - **(PFBR) Budget Transfer Requests** — "request, action and manage budget transfers… workflow approval process… manage transfers within line items."
  - **(PFBM) Budget Management** — "budget appropriations, streamline budget transfers, swiftly action budget amendments and quickly apply budget control update vouchers… mid-term reviews can be undertaken effortlessly."
- Control model (benefits list): "Budgetary Control — Budgetary funds are mapped to the Chart of Accounts at a predetermined hierarchy level for aggregate fiscal control." "Multi-Level Allotment Controls — Supports appropriations, warrants or allocations, mapped to summarized or detailed reports within the Chart of Accounts and to fiscal periods." "Commitment and Obligation Control — Supports a soft commitment to spend or hard commitments to contractual obligations." "Real-Time Ledger — Balances ledgers in real-time to ensure budgets are not overspent."
- Chart-of-accounts framing (vendor blog teaser): "The Chart of Accounts (COA) or 'budget classification' is arguably the most critical part of effective PFM reform and IFMIS design. The COA for government is more complicated than in the private sector."
- Suite context: six pillars (Government Performance Management — "Tying performance directly to budgeting"; Public Financials Management; Public Expenditure Management; Government Treasury Management; Government Receipts Management; Civil Service Management). Budgeting machinery is one pillar of the whole fiscal architecture.
- Standards frame: UN, IMF, World Bank, IFRS, MCC; PEFA results published; progressive activation "in line with a sequenced PFM reform program."

### Neubrain [Evidence layer A — Tier 2 product pages]

- Positioning: "Budgeting, Business Analytics, and Performance Management" for "Federal, state, and local government agencies… from small municipalities to large Federal government agencies."
- Solution set: Performance-based Budgeting ("unifies cost-based budgeting with performance goals"), Pay and Personnel Budget ("Salaries make up the greatest portion of your expenditure budget"), Operating Budget, Capital Budget, Forecasting, Performance Measurement, Cost Allocation, "CAFR, Financial Reporting, and Budget Books."
- Operating budget: "automates the creation of the **base budget** and any **supplemental requests or service level changes**. It is capable of housing multiple parallel organizational hierarchies and roll-up levels (performance-oriented, organizational, departmental, and others)."
- Capital budget: "automates the creation, budgeting, analysis, and reporting of the capital project budgeting tasks. It can interface with any Financial system as well as Project and Grants Management software."
- Federal/defense variant: DoD solutions for "Programming, Budgeting and Execution (PPBE), and Congressional Budget Justification (J-Book)"; customer quote: "prepare complex Congressional Budget submissions in support of our $35B annual appropriation" (Air National Guard) — appropriation vocabulary at the federal pole.
- Monitoring framing: "Budgets are often established and then quickly forgotten. But monitoring performance and measuring adherence to performance goals is key."
- Customers: Placer County CA, City of Salem OR, Park City UT, Housing Authority of Baltimore City, US Air Force, US Navy, Air National Guard, PA Turnpike Commission.

### NASBO — Budget Processes in the States & Territories [Domain authority]

- The report's own section structure is a domain map of the budget cycle and its machinery (published since 1975; compiled from state budget offices):
  1. **Budget Timeline and Participants** — "the budget cycle calendar followed by states… functions and staffing of budget offices… states' revenue estimating processes."
  2. **Requirements, Authorities and Limitations** — "the budgetary powers of the executive branch, as well as the state laws and regulations that govern and restrict state budgets, including **balanced budget requirements, debt limits and tax and expenditure limits**."
  3. **Budgeting Practices, Procedures and Tools** — "which **funds are subject to appropriation**… state rainy day funds… how states treat unanticipated general fund surpluses and unspent appropriations, and the use of **integrated financial management systems** by states."
  4. **Budget Documents** — "the different budget methodologies used by states… how the **executive budget proposal** and other key documents in the budget process are presented and structured."
  5. **Monitoring the Budget** — "how state budget offices and other participants **monitor and control expenditures, transfer appropriated funds**, and forecast future operating expenditures."
  6. **Measuring Performance and Using Data and Evidence** — performance data collection/reporting, spending transparency websites, evidence-based policymaking.
- Confirms the executive-proposal → appropriation structure, the legal frame (balanced budget requirements), the fund/appropriation vocabulary, and monitoring/transfers as standing budget-office work.

## Cross-product Comparison

| Dimension | Euna Budget | FreeBalance | Neubrain | NASBO (domain) |
|---|---|---|---|---|
| Center | full-cycle budgeting suite for public sector | budget machinery inside whole-of-government PFM/GRP suite | budgeting + performance analytics for public sector | domain map of the budget cycle |
| Unit of record | the budget by department/fund/cost center, across operating/personnel/capital | appropriations/allotments/commitments on the Chart of Accounts | base budget + supplemental requests by hierarchy levels | the executive budget proposal / appropriations |
| Fiscal framework | funds, departments, cost centers | funds mapped to Chart of Accounts hierarchy, fiscal periods | parallel organizational hierarchies and roll-up levels | funds subject to appropriation |
| Participants | department heads (submit/manage own budgets), finance/budget office (review, consolidate), HR (personnel), executives, public (portal) | ministries, departments, spending agencies connected to one unified system; budget office controls | departments, budget offices, city councils, federal agencies | budget offices, executive branch, legislature |
| Cycle phases | planning/forecasting → building → review/approval → publishing/sharing | formulation → execution → accounting/reporting → audit | base budget → supplemental requests → monitoring | timeline → authorities → documents → monitoring → performance |
| Personnel | dedicated module: position control, pay grids, union scales, benefits layering | civil service management pillar (separate) | pay & personnel budget module | (staffing of budget offices) |
| Capital | capital budgeting module (projects, funding sources, multi-year) | projects & job costing (estimates/forecasts) | capital budget module (project budgeting tasks) | Capital Budgeting in the States (separate report) |
| Execution control | ERP integration; change requests after publication with auditable history | appropriations, allotments, soft/hard commitments, transfers, amendments, real-time ledger "so budgets are not overspent" | interface with financial systems | monitor and control expenditures, transfer appropriated funds |
| Publication | budget books, ACFRs, public portal, GFOA award checklists | transparency portals (separate solution) | CAFR/financial reports/budget books | budget documents; transparency websites |
| Performance | performance management module (KPIs through the cycle) | government performance management pillar ("tying performance directly to budgeting") | performance-based budgeting (link budgets with outcomes) | measuring performance section |
| Regional machinery | GFOA/GASB/ACFR/ADA (US/Canada local) | UN/IMF/World Bank/PEFA/COA reform (international national) | GSA schedule, PPBE/J-Book (US federal) | US state laws: balanced budgets, debt limits, TELs |

Cross-product commonalities (evidence layer B):

1. **The budget is held in the government's own fiscal framework** — funds, organizational units (departments/agencies), cost centers, and account classifications, scoped to fiscal periods. Every sampled product organizes the budget this way; NASBO confirms funds/appropriations as the domain frame. The chart of accounts / budget classification is named by FreeBalance as the critical structure.
2. **The build is multi-participant with a central consolidator** — contributing units draft/submit their own budgets (department heads "manage their own budgets," "submit requests"); the budget/finance office reviews, adjusts, consolidates, and controls versions/approvals. Present in all three products.
3. **The cycle is annual-recurring with named phases** — formulation/preparation → review/approval → (adoption) → execution/monitoring → reporting/publication. FreeBalance states it as formulation/execution/accounting-reporting/audit; Euna as planning→building→publishing; NASBO's sections map the same arc.
4. **Personnel costs are a first-class budgeting content type** — dedicated personnel/pay budgeting with position-level tracking in two of three products (Euna, Neubrain; FreeBalance holds it in the Civil Service pillar), with "salaries are the largest expense" framing in both.
5. **Capital budgeting appears as a module** — Euna and Neubrain both ship capital budget modules; FreeBalance links budgeting to project costing. Consistent with the CIP pass's finding that budgeting suites embed capital planning.
6. **Mid-year change machinery** — amendments/transfers/change requests after adoption, with auditable history (Euna FAQ; FreeBalance PFBR/PFBM; NASBO "transfer appropriated funds").
7. **Publication of the budget as a formal document** — budget books (and ACFRs at the US local pole) generated from the budget data, plus public-facing portals (Euna OpenBook; FreeBalance transparency portals solution; Neubrain budget books; NASBO budget documents section).
8. **Performance linkage is a module, not the core** — every vendor sells performance/strategic linkage as a separate module or pillar beside the budget modules.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Removing any one changes the Type:

1. **The government's budget as the unit of record.** A persistent, structured allocation of public money for a fiscal period, organized in the government's own fiscal framework — its funds, organizational units, and account classifications — spanning the spending sides (operating, personnel, capital) and the revenue side it must fit. The budget is the government's spending plan of record, not a private forecast. Remove → corporate budgeting/FP&A over a private chart of accounts, or a spreadsheet.
2. **The multi-participant build–review–consolidate cycle.** Contributing units (departments, agencies, ministries) draft and submit budget requests with justifications; the central budget/finance office reviews, adjusts, consolidates, and versions the whole; scenarios and what-ifs are tested before a proposed budget emerges. Remove → a static ledger, a reporting tool, or a form collection with no consolidation machinery.
3. **The public-authority posture.** The budget is the government's formal, publicly-scrutinized spending plan: it is proposed for adoption by the government's governing body/legislature, published as the budget document (budget book), and carries forward as the frame that governs spending during the year (amendments and transfers are tracked against it). Remove → corporate FP&A (private plan, no adoption/publication) or a transparency portal (publication without the budget machinery).

Joint-hold test: (1)+(2) without (3) = corporate-style planning with departmental submissions; (2)+(3) without (1) = a document/workflow tool with no fiscal structure; (1)+(3) without (2) = a budget ledger/publication with no build cycle.

Deliberately NOT in L0 (checked against the historical sample and cross-product variance): fund accounting and appropriation/commitment controls (the strongest realization of the fiscal framework and of leg 3's execution frame — but the conceptual invariant is "the government's fiscal framework" and "the budget governs the year," and preparation-focused products satisfy the Type without in-platform execution checking); balanced-budget requirements (variant — national deficit regimes exist); GFOA/GASB/ACFR machinery (regional); performance/program budgeting (module); capital project registers (module); specific approval-chain depths or deadlines (not evidenced).

### L1 — Common Mature Structure

- Departmental/agency submission workspaces with roles, permissions, and approval workflows ("designed for non-finance staff").
- Personnel/position budgeting: position control, funding splits, pay grids/union scales, benefits layering, mid-year hires/reclassifications, version control.
- Capital budgeting module: project budgets, funding sources, multi-year plans, capital–operating linkage.
- Revenue estimation/forecasting feeding the balance.
- Scenario planning / what-if modeling / version control ("duplicate organizations to explore alternative plans").
- Budget-vs-actual monitoring, variance analysis across funds/departments/cost centers.
- Mid-year amendments/transfers with auditable history.
- Budget book / financial report publication (budget books, ACFRs) generated from budget data; GFOA-class award alignment at the US local pole.
- ERP/GL integration (budget data synchronized with the financial system of record).
- Performance/strategic linkage (align dollars to goals/KPIs) as a module.
- Public transparency portal as an output surface.

### L2 — Variant / Optional Structure

- **Level of government**: municipal/county (US local pole), state/provincial, national/ministries (international PFM pole), federal agencies and defense (PPBE, Congressional Budget Justification/J-Books), school districts, housing/transportation authorities.
- **Regime**: balanced-budget regimes (US states: balanced budget requirements, debt limits, tax/expenditure limits) vs national budgets that may run deficits; executive-proposal + legislative appropriation vs parliamentary patterns.
- **Budgeting methodology**: line-item vs program/performance/outcome budgeting (NASBO: "different budget methodologies used by states").
- **Product form**: standalone budgeting suite (Euna) vs budget pillar inside a PFM/GRP suite (FreeBalance) vs analytics vendor overlay (Neubrain) vs ERP-embedded module (Tyler-class, unreachable).
- **Execution-control depth**: in-platform appropriation/commitment/allotment controls (FreeBalance pole) vs preparation-and-publication focus with ERP-side execution (Euna/Neubrain pole).
- **Regional machinery**: GFOA/GASB/ACFR/ADA (US/Canada local) vs UN/IMF/World Bank/PEFA/COA-reform (international national).
- **Publication form**: static PDF budget book vs interactive public portal vs both.

### L3 — Vendor-specific Structure (Research Notes only)

- Euna: OpenBook, Budget Book Studio, Euna AI, Professional vs Enterprise tiers, Questica lineage (questica.com redirects to Euna), module names, marketing percentages (50% fewer FOIA requests, 25% time saved — not asserted), "1,000+ organizations" claim.
- FreeBalance: module codes (PFPF/PFBC/PFBR/PFBM/PFCB/PFFA/PFFM/PFSI/PFSL/PFAA), Accountability Suite/Platform naming, GRP term, progressive activation, six base configurations, PEFA results page, "$425 billion" claim.
- Neubrain: PPBE/J-Book solutions, MAJIC dashboards, GSA MAS schedule, cost allocation plans, D&B past-performance rating.
- NASBO: six-section report structure, 1975 origin, territories companion report.

## Vendor-specific Findings

- The US market-leader pole (OpenGov, ClearGov) and the ERP-embedded pole (Tyler Munis) could not be directly researched (403 across passes). Their existence and market role are treated as market-structure anchors only. The final document describes the ERP-embedded and market-leader realizations generically without product-specific features.
- Euna's module split (strategic/performance/personnel/operating/capital/transparency) is one vendor's articulation of budget content types; Neubrain's split (performance-based/personnel/operating/capital/forecasting/reporting) partially matches; FreeBalance's pillar split differs (execution-centric). The content-type *classes* (operating, personnel, capital, revenue, performance) recur; the module names do not.

## Boundary Findings

- **vs Capital Improvement Planning (§24, processed) — flag DISCHARGED, keep-both ratified.** The CIP pass held the seam by center of gravity; this pass confirms it from the budgeting side. Budgeting suites ship capital-budgeting modules (Euna Budget Capital verified; Neubrain Capital Budget; OpenBook displays CIPs), so the product-level boundary is fuzzy — but the type-level boundary holds: CIP's unit of work is the **multi-year capital project** (register, funding-source allocation, governed multi-year adoption); Public Budgeting's unit of record is the **government's fiscal-period budget as a whole** (operating + personnel + capital + revenue allocations by fund/department/account). A budgeting suite without a capital module is still fully in-type (FreeBalance's budget machinery has no CIP register; its project linkage is job costing). A CIP application without the operating/personnel/revenue budget is still CIP. Module-vs-whole-product seam; no alias/duplicate.
- **vs Budgeting & Forecasting Platform (§08, corporate).** Same verb, different object standing. Corporate budgets are internal management plans over a private chart of accounts; nothing is adopted by a governing body, published as a public document, or carries appropriation standing. Public budgets are the government's formal spending plan: publicly scrutinized, adopted, published, and framing execution (amendments tracked). Fund-based fiscal structure and public-authority posture are the discriminators; FreeBalance states the public-sector specificity directly ("commitment accounting and budget management are unique to the public sector"). Keep-both.
- **vs Public Financial Management System (§24, unprocessed sibling).** FreeBalance demonstrates the relationship: budgeting machinery (formulation + execution controls) is one pillar of a PFM/GRP suite that also holds treasury, receipts, expenditure, civil service. The budgeting platform is centered on the budget cycle; the PFM system is the whole-of-government fiscal architecture (typically "all ministries, departments and spending agencies connected to a single, unified system"). Overlap zone: budget execution controls. Keep-both; seam = budget-cycle center vs whole-fiscal-operations center. Joint review recommended when Public Financial Management System is processed.
- **vs Government Transparency Portal (§24, processed).** Budget publication (budget books, open budget portals) is an output module of budgeting (Euna OpenBook; FreeBalance transparency-portals solution). The transparency portal is the standalone publication surface — consistent with that pass's finding that transparency publishing recurs as a module inside neighboring Types. Interlock, not overlap.
- **vs Government Performance Management (§24, processed).** Performance budgeting links dollars to goals/KPIs; the performance Type maintains the goal→measure→actuals loop. Every sampled vendor sells performance as a separate module/pillar beside budget modules — packaging evidence that they are distinct machineries. Consistent with that pass.
- **vs Government Revenue Management / Tax Administration (§24).** Revenue estimation feeds budget formulation (NASBO: revenue estimating processes); revenue collection is a different Type. Budget platforms forecast revenue as an input to the balance; they do not collect it.
- **vs Government Grants Management (§24, processed).** Grants appear as revenue sources and as funding sources for positions/projects (Euna personnel funding "across cost centers, accounts, or grants"); the grant lifecycle machinery is a separate product (Euna sells Grants as a separate product). Interlock.
- **vs Government Procurement Platform (§24, processed).** Procurement executes budgeted spending; commitment control links budgets to obligations (FreeBalance soft/hard commitments). The procurement cycle is that Type's center.
- **vs Spreadsheet Application (§03.03).** The documented "before" state: Euna's FAQ explicitly frames the product against "juggling spreadsheets" with "version control issues and manual errors." The platform adds the shared fiscal framework, workflow, consolidation, and audit history.
- **vs Government Meeting / Agenda Management (§24).** Budget hearings and adoption votes happen in legislative settings; platforms may publish hearing materials, but the meeting machinery is that Type.

## Uncertainties

- US market-leader and ERP-embedded poles unverified (403); their feature realizations are inferred only at market-structure level. The final document avoids product-specific claims for them.
- No Tier-1 operational documentation was reachable for any sampled product (Euna help center 403; FreeBalance/Neubrain publish product pages, not operational manuals). Workflow details (submission windows, approval-chain depths, amendment rules, fiscal-year defaults) are therefore described conceptually; no precise operational facts are asserted.
- Whether preparation-focused products (ClearGov-class) include any execution monitoring is unknown; execution control is held as common-mature, not definitional, partly for this reason.
- The adoption act itself (the vote) happens in the legislature, outside the platform; platforms support the proposal/book and versioning for the governing body. How different products support the adoption step specifically (e.g., elected-official workspaces) was not directly observed.
- Non-US regimes beyond FreeBalance's international pole (e.g., EU municipal budgeting products) were not sampled; the international realization is evidenced by one vendor.
- School-district and special-district variants are evidenced only through Euna's stated audience (K-12, education) and customer types; no district-specific product was directly researched.

## Final Synthesis

The Public Budgeting Platform is the government's budget-cycle system of record. Its defining structure is threefold and jointly-held: (1) the government's budget as the unit of record — a structured allocation of public money for a fiscal period, organized in the government's own fiscal framework of funds, organizational units, and account classifications, spanning operating, personnel, capital, and revenue sides; (2) the multi-participant build–review–consolidate cycle — departments submit requests and justifications, the budget office reviews, adjusts, consolidates, and versions, scenarios are tested, and a proposed budget emerges; (3) the public-authority posture — the budget is the government's formal, publicly-scrutinized spending plan, proposed for adoption by its governing body, published as the budget document, and carried forward as the frame that governs the year's spending through tracked amendments and transfers. Around this core, mature products add position/personnel budgeting, capital project modules, revenue forecasting, scenario machinery, budget-vs-actual monitoring, ERP integration with appropriation/commitment controls, performance linkage, and public transparency publishing. The Type is distinct from corporate budgeting by the standing of its object (public, adopted, published, authority-bearing), from CIP by its unit of record (the whole fiscal-period budget vs the multi-year capital project), from PFM systems by its center (the budget cycle vs the whole fiscal architecture), and from transparency portals by its direction (building and governing the budget vs publishing records about government conduct). The paper-era lineage — departmental request forms, budget office worksheets, the executive budget proposal, hearings, the adopted appropriations document, the budget book — satisfies all three legs with no software, confirming the definition is not overfit to the current SaaS generation.
