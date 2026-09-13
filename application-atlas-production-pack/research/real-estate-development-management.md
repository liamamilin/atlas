# Research Notes — Real Estate Development Management

## Research Goal

Understand, from real products, what a Real Estate Development Management application is: what the developer-side system of record contains, how a development project moves from land/site acquisition through feasibility, design/entitlement, construction oversight, to lease-up/sale/stabilization or asset conversion, what money structures live on the project record, and how this Type separates from Construction Project Management, Preconstruction Management, Real Estate Investment Management, and Site Selection.

## Initial Boundary

Working hypothesis at start:

- What: software used by real estate developers / development managers to run development projects end-to-end (developer-side, not GC-side).
- Who: development managers, project managers, development accountants, acquisitions teams, executives at developer firms.
- Confusable neighbors: Construction Project Management (GC execution), Preconstruction Management (GC pursuit-to-award), Real Estate Investment Management (portfolio/investor view), Site Selection (location discovery), Property Management (operating stabilized assets), Construction Cost Management / Progress Billing (construction-phase money machinery), generic Project Management Application.
- Unknowns going in: whether underwriting/pro-forma modeling is definitional; whether draws/capital-partner funding machinery is definitional; whether the acquisition/deal pipeline belongs to this Type or to Investment Management; where entitlement/permit tracking sits.

## Research Questions

1. What is the unit of record — the "project"? What binds to it (site, budget, parties, documents)?
2. What lifecycle does the record span? Does it start before construction and end after it?
3. What money structures exist on the project (budget categories, commitments, actuals, forecasts, draws, capital calls)?
4. Who uses the system and what do they do (roles: executive, development leader, PM, accountant, acquisitions)?
5. How do external parties participate (capital partners/lenders/investors, vendors/consultants, brokers/agents)?
6. How does construction appear — executed in-system, or overseen from the developer side?
7. Where does feasibility/appraisal (pro forma, residual value) live — in this Type or adjacent?
8. What are the terminal events of the record (stabilization, sale, capitalization into operating assets)?
9. Would older/regional/minimal products still satisfy the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Northspyre | Developer-side development spend & project management pure-play ("Real Estate Development Management Software" — own labeling); deal + development + analytics products; draw/capital machinery prominent | Mid-to-large US developers (commercial, data center, affordable housing) | Tier-2 official product pages ×3 |
| Dealpath | Deal-management "operating system for real estate investing"; development is one solution (pipeline → delivery); institutional posture | Institutional investors/developers, homebuilders | Tier-2 official product/FAQ pages ×2 |
| MRI Project4000 (Capital Project Control) | ERP-module pole: capital-project cost control (commitments/expenditures vs budgets, WIP asset creation) inside a real-estate suite | Global real-estate owners/developers/operators | Tier-2 official solution page |
| LandTech LandInsight | UK front-end pole: land/site sourcing + planning data + development appraisal + site pipeline | Small-mid UK residential / care-home / power developers, land agents | Tier-2 official product page |

Checked and excluded as adjacent (not in-type): Forbury (Altus Group) — CRE valuation/appraisal of standing assets (valuations, investment analysis) — confirms the valuation-tool boundary, not a development-management sample.

## Sources

All fetched 2026-09-09. WebFetch (text/markdown).

- Northspyre — homepage https://www.northspyre.com/ (Tier-2)
- Northspyre — Development product page https://www.northspyre.com/real-estate-project-management-financial-planning-software (Tier-2)
- Northspyre — Construction Draw Management https://www.northspyre.com/construction-draw-management-software (Tier-2)
- Dealpath — homepage https://www.dealpath.com/ (Tier-2)
- Dealpath — Development solution page + FAQ https://www.dealpath.com/development/ (Tier-2)
- MRI Software — A-Z product index https://www.mrisoftware.com/products/development (404-redirected to index; nav evidence) (Tier-2)
- MRI Software — Capital Project Control https://www.mrisoftware.com/solutions/capital-project-control/ (Tier-2)
- LandTech LandInsight — https://www.landinsight.io/ (redirects to land.tech product page) (Tier-2)
- Forbury (boundary check only) — https://www.forbury.com/ (Tier-2)

Unreachable / dropped (per source-access rules):

- Altus Group Argus Developer — 404 on /argus-developer/ and /products/argus-developer/ (2 attempts) — dropped; feasibility-tool pole not directly sampled.
- LandTech landtech.io root — timeout (1 attempt); landinsight.io succeeded instead.
- Yardi Development Suite — not attempted (vendor domain returned 403 in prior passes recorded in STATUS.md); full-suite development-suite pole rests on market structure only.
- No Tier-1 help center / operator manual was reached for any sampled product. All product observations below are Layer A (directly observed on official vendor pages) but marketing-weight; no operational manual detail available.

## Product A — Northspyre (key observations)

Evidence: official homepage + Development product page + Draw Management page. [A]

- Self-labeling: "Real Estate Development Management Software"; tagline "Powering your development strategy end-to-end"; "the only end-to-end development management platform". Products: Northspyre Deal (financial modeling & pipeline), Northspyre Development (project & financial management), Analytics (portfolio).
- Lifecycle explicitly named: **Acquisition → Early Planning → Pre-Development → Construction → Stabilization** ("Guide real estate projects to success from acquisition through stabilization").
- Acquisition stage: "Model deal scenarios, execute due diligence, manage your development pipeline"; use cases: Underwriting (pro forma), Pipeline Management.
- Pre-development: Project Planning ("use historical cost data and performance benchmarks to plan budget scenarios... sound assumptions on every line item"), Vendor Procurement ("organize bids... AI insights to identify scope gaps and cost-saving opportunities"; "safeguard against future change orders").
- Construction: Project Delivery & Schedule (tasks, real-time progress), Vendor Management ("track COIs, lien waivers, compliance; evaluate vendor performance; negotiate change orders"), Budget Management ("real-time visibility, predictive insights, proactive alerts... track, manage, execute budget transactions"), Forecasting ("automate cash flow reporting; predict cash shortages/surpluses; raise capital calls earlier").
- Draw machinery (dedicated page): draw packages ("audit-ready... linked documentation"), Draw Co-Pilot ("automatically analyze draw readiness... issues before it goes out to lenders and investors"), draw & invoice approvals ("custom approval workflows... PDF reports documenting who approved each invoice and when"), Funding Portal ("investors and lenders... 24/7 visibility into current and historical draw packages"), Complex Capital Management ("regulatory and compliance requirements across multiple sources"; capital-stack guide).
- Stabilization: "Monitor performance and simplify CapEx delivery" + Portfolio Analytics.
- Roles: Executive, Development Leader, Acquisition Leader, Project Manager, Accounting. Asset classes: commercial, data center, affordable housing. Mobile companion app ("review incoming project data... approve critical items from anywhere").
- Accounting integrations: sync cost data, invoices, payments between development and accounting systems; budget reconciliation (partners include Yardi, Sage Intacct, QuickBooks, etc.).

## Product B — Dealpath (key observations)

Evidence: official homepage + Development solution page incl. FAQ. [A]

- Self-labeling: "Real Estate's Leading Deal Management Software"; "AI-Powered Operating System for Real Estate Investing". Solutions: Acquisitions, Dispositions, **Development**, Debt.
- Development lifecycle named: **Sourcing & Site Selection → Underwriting & Due Diligence → Pre-Development & Construction → Occupancy & Stabilization**; "from breaking ground to lease-up".
- FAQ (direct quotes/paraphrase): "track projects from initial site evaluation through entitlements, construction, and stabilization"; "centralize and manage development budgets, including hard and soft costs"; workflows/stages/tasks/approvals configurable; centralized document repository (plans, budgets, reports).
- Pipeline Management: shared real-time deal flow across regions/stages. Deal Execution: underwriting model comparison, due diligence tasks/documents, IC approval workflows, fund allocation.
- Workflow automation: repeatable role-based workflows, auto-assigned tasks, task dependencies shifting milestone date projections. Milestones: "track milestones and compare projected dates against actuals"; "analyze spending and compare budgets against actuals".
- Collaboration: internal + external teams, selective access for third parties (legal, environmental), external task assignment. Map view. Mobile app (drop a pin during site visits, approve updates).
- CRM: JV partners, sponsors, brokers, consultants, investors tracked alongside deals. Market tracking (comps database) and Dealpath Connect (private listing exchange) — investment-side machinery.
- Homebuilders variant: "manage land acquisition and community development prep"; "track and manage horizontal development"; regional investment committee meetings.

## Product C — MRI Project4000 / Capital Project Control (key observations)

Evidence: official A-Z index + Capital Project Control solution page. [A]

- Positioning: "Take the stress out of managing capital expenditure from projects... control of cash flow, budgets and projects and enable the creation of Work-in-Progress (WIP) assets."
- Money machinery: "commitments and expenditures are recorded at every stage against budgets for both capital and expense projects"; POs, invoices, credit notes, journals, accruals "automatically updated in real time to provide current position against budget"; transactions assignable to specific WIP assets or split.
- Approvals: "approvals process for authorizing, allocating, committing and spending... control of budgets, projects and schemes at each step."
- Terminal structure: WIP asset build-up — spend accumulates into auditable WIP assets that become the capitalized asset ("audit trail for asset creation") — i.e., the development record resolves into the operating asset, the ERP-side realization of project completion.
- Reporting: tailored reports for business decisions.
- Context from MRI's A-Z: no standalone "Development" product listed today; the development-adjacent machinery lives in Project4000 (capital project control), Job Cost, Investment Management, Debt Management — evidence that in full-suite vendors, development management decomposes into modules; the cost-control module is the skeleton reached this pass.

## Product D — LandTech LandInsight (key observations)

Evidence: official product page (land.tech). [A]

- Positioning: "Clear Land Intelligence for Professionals... consolidates ownership, planning, and property data into one platform, letting developers assess opportunities."
- Front-end development loop: "Find the Best Development Sites" (ownership/planning/site data), "Assess Sites Accurately" ("constraints, risks, and viability... faster site appraisals"), "Streamline Your Development Pipeline" ("manage your projects from sourcing to appraisal").
- Appraisal tool listed as a named feature (development appraisal); comparables and market intelligence "to validate viability early".
- Audiences: residential developers, agents (site sourcing for clients), care-home developers (demographics, catchment), power developers (grid capacity, multi-parcel assembly).
- Ecosystem add-ons: LandFund (debt advisory / rate comparisons), Give My View (community engagement). Support/tutorials portals exist but not fetched.
- No construction-phase or draw machinery visible on the fetched surface — the record's arc here is sourcing → appraisal → pipeline.

## Cross-product Comparison

| Structure | Northspyre | Dealpath | MRI Project4000 | LandInsight |
|---|---|---|---|---|
| Development project as persistent record across multi-phase lifecycle | Yes (acquisition→stabilization) | Yes (site selection→stabilization) | Yes (capital/expense project, start-to-finish, WIP→asset) | Yes (sourcing→appraisal pipeline; early arc) |
| Site/land position bound to project | Yes (development projects) | Yes ("land purchase information", site selection) | Implied (projects) | Yes (parcels, ownership) |
| Staged lifecycle / pipeline views | Yes (named stages) | Yes (named stages, pipeline) | Partial (projects, schemes; no stage language observed) | Yes (sourcing→appraisal) |
| Project money spine: budget w/ projected vs actual | Yes (budget scenarios, budget transactions, actuals) | Yes (hard/soft cost budgets, budgets vs actuals) | Yes (commitments/expenditures vs budgets, real-time position) | Yes, appraisal form (viability/appraisal) |
| Land + soft costs alongside construction costs | Yes (implied by lifecycle) | Yes (explicit hard/soft) | Implied (capital projects) | Yes (appraisal includes land) |
| Commitment/contract control (POs, invoices, change orders) | Yes (budget transactions, change order negotiation) | Light (spending vs budgets) | Yes (PO/invoice/accrual engine) | No |
| Draw / capital-partner funding loop (draws, capital calls, lender/investor reporting) | Yes (deep: packages, compliance, approvals, portal, capital calls) | Partial (fund allocation, capital deployment dashboards) | No (observed surface) | No (LandFund = debt advisory add-on) |
| Milestones/tasks/dates, dependencies | Yes (delivery & schedule) | Yes (dependencies shifting milestone projections) | No (observed surface) | Light (site pipeline) |
| Vendor/consultant management (procurement, compliance docs) | Yes (bids, COIs, lien waivers, performance) | Partial (external collaborators, tasks) | No (observed surface) | No |
| Feasibility / underwriting / pro forma modeling | Yes (Deal product: model deal scenarios) | Yes (underwriting comparison, pro formas, comps) | No | Yes (appraisal tool, viability) |
| Site/market data layers (ownership, planning, constraints, maps) | No (observed surface) | Yes (market tracking, map view) | No | Yes (core) |
| Document repository | Yes (centralized doc mgmt) | Yes (FAQ) | No (observed surface) | Yes (site info, export/share) |
| Accounting integration / reconciliation / asset capitalization | Yes (sync invoices/payments, budget reconciliation) | No (observed surface) | Yes (GL-real-time, WIP→asset) | No |
| Approvals (internal gate before money moves) | Yes (draw/invoice approval workflows, mobile approvals) | Yes (IC approval workflows, configurable) | Yes (authorizing/allocating/committing/spending) | No (observed surface) |
| External-party access (selective) | Yes (funding portal for lenders/investors) | Yes (legal/environmental collaborators) | No (observed surface) | Yes (site sharing w/ team & clients) |
| Portfolio analytics / reporting | Yes | Yes (dashboards, reports) | Yes (tailored reports) | Light |
| Mobile app | Yes | Yes | No (observed) | No (observed) |
| AI assistance | Yes (budget line items, scope gaps, vendor recs, draw readiness) | Yes (data ingestion, screening) | No | Yes (planning summaries) |

Reading of the matrix:

- The development project record spanning a lifecycle that starts before construction and resolves after it: present in all four (Layer B).
- A money structure on the project (projected + actual costs, revised as it advances): present in all four — in appraisal form at the front pole (LandInsight), in commitment/expenditure-control form at the ERP pole (MRI), in execution-budget form in between (Northspyre, Dealpath) (Layer B).
- Draws/capital-partner funding machinery: strong at Northspyre only; partial at Dealpath; absent at two poles → common-at-the-capital-funded-pole, NOT definitional (Layer A + B; single-product-strength for the deep machinery).
- Feasibility/underwriting: present at two poles, absent at two → common/optional, NOT definitional.
- Vendor procurement/compliance machinery, deep commitment engines, site-data layers: pole-dependent → common/optional.
- Stage labels differ per product (Acquisition/Early Planning/Pre-Development/Construction/Stabilization vs Sourcing/Underwriting/Pre-Development & Construction/Occupancy & Stabilization) — conceptual lifecycle is stable; labels vary.

## Canonical Model

Two jointly-held structures (the defining core):

1. **The development project as the unit of record.** A persistent, identified undertaking that binds a land/site position to an intended built outcome, carried through a staged, multi-year lifecycle that begins before construction (siting/acquisition, feasibility, design/entitlement) and resolves only at completion events beyond construction (occupancy/stabilization, sale/disposition, or conversion into operating assets). The record persists and accumulates context (documents, milestones, decisions, parties) across the whole arc.
   - Remove → a generic project tracker / stage-labeled pipeline, or a construction-execution record that begins at contract award and ends at completion.

2. **The development money structure carried on that record.** The project's own financial content as a living structure: projected and actual costs (commonly spanning land acquisition and soft costs alongside construction costs), with commitments/spend tracked against the projection and the position revised as the project advances. Realizations: development appraisal/feasibility at the earliest pole; commitment-and-expenditure control against budget in ERP/cost-control products; execution budget with forecasting in between.
   - Remove → an opportunity pipeline with no cost content, or a bare schedule.

Jointly-held load-bearing:
- 1 without 2 = generic project tracker with development-branded stages.
- 2 without 1 = an appraisal worksheet / cost-control module with no development arc.
- Both legs together, with the lifecycle span, are what no neighbor Type holds: Construction PM holds contract-execution records; Investment Management holds asset/portfolio records; Site Selection holds location data; Property Management holds operating-asset records.

## Abstraction Hierarchy (internal)

### L0 — Defining Invariant
- (1) development project of record binding site position + intended built outcome, lifecycle pre-construction → post-construction resolution
- (2) development money structure on the record (projected/actual costs, commitments, revised position)

### L1 — Common mature structure
- Stage-gated pipeline across the firm's development projects (roll-ups, dashboards)
- Milestones/critical dates and tasks with roles/assignments; projected vs actual tracking
- Capital funding loop at the capital-funded pole: draw/requsition packages, readiness/compliance checks, approval workflows, lender/investor reporting, capital calls
- Commitment/contract control (POs, invoices, change orders) with real-time budget position
- Vendor/consultant management (procurement/bids, compliance documents, performance)
- Document repository on the project
- Forecasting (cost to complete, cash flow, capital call timing)
- Accounting integration/reconciliation (invoices/payments sync, GL; WIP→asset capitalization at ERP pole)
- Internal approval gates before money moves; selective external-party access

### L2 — Variant / optional
- Feasibility depth: pro-forma/underwriting modeling, comps databases, residual-value appraisal
- Site/land data layers (ownership, planning, constraints, maps, topography, grid capacity)
- Capital-stack structuring views (equity/debt complexity, regulatory compliance for funding sources)
- Community engagement / planning consultation; debt advisory add-ons
- Asset-class packs (affordable housing compliance, data centers); homebuilder horizontal-development configuration
- Map views; mobile apps; AI assistance (era-current)
- Investor/broker relationship CRM (straddling toward Investment Management)

### L3 — Vendor-specific (research notes only)
- Northspyre: Draw Co-Pilot, Funding Portal, marketing stats (75% faster draw packages, 80% less manual work, 66% fewer overruns), named accounting partners, mobile launch specifics
- Dealpath: Dealpath Connect private listing exchange, Dealpath AI, homebuilder positioning, $10T transactions claim
- LandInsight: UK dataset coverage (grey belt, topography, grid capacity), 80%-faster claim, LandFund/Give My View packaging
- MRI: Project4000 WIP/audit-trail specifics, A-Z portfolio decomposition

## Vendor-specific Findings

See L3 above. Also: no vendor in the sample markets a product that executes GC-side construction field operations (RFIs, submittals, punch lists) as the center — construction appears as oversight/budget/milestone surfaces, corroborating the Construction PM seam. Dealpath and Northspyre both market acquisition/underwriting machinery alongside development — evidence that the acquisition pipeline straddles this Type and Real Estate Investment Management.

## Boundary Findings

1. **vs Construction Project Management (§17, processed).** Construction PM's wall (recorded that pass): the multi-org contractual community executing construction. Here the operator is the developer/owner creating an asset; construction is one phase, typically delegated and overseen (budget/commitments/vendor oversight, milestones), not executed (no RFIs/submittals/punch-list machinery as center). Remove test: strip pre-construction (siting/feasibility/entitlement) and post-construction resolution, and the contract-execution community → Construction PM; strip construction-execution depth → this Type stands. Keep both. Consistent with the preconstruction pass's forward note.

2. **vs Preconstruction Management (§17, processed).** Precon = a GC's pursuit-to-award pipeline (unit: pursuit of work to be won). Here = the developer's project creating an asset (unit: the undertaking itself). Different operator, different unit of record, different money (bid leveling vs development budget). Keep both.

3. **vs Real Estate Investment Management (§17, unprocessed) — FORWARD FLAG for joint review.** Shared: acquisition pipeline, underwriting, portfolio dashboards, investor reporting. Proposed seam: unit of record — a standing asset/portfolio with returns/valuations vs the development project carried to built outcome with a cost/commitment spine; Dealpath and Northspyre both straddle deliberately (investment OS with a development solution; dev platform with underwriting). Removal tests: strip the development arc + cost spine → investment/deal management; strip pipeline/valuation/investor-returns machinery → development management remains. Ratify at the investment-management pass.

4. **vs Site Selection Platform (§17, unprocessed) — forward note.** LandInsight straddles: pooled land/planning/ownership data discovery + appraisal + site pipeline. Proposed seam: location discovery as the center (pooled market/site data, comparable search) vs the development project of record with money spine. Ratify at that pass.

5. **vs Property Management (§17).** Handover/stabilization seam: this Type's arc ends at stabilization/sale/capitalization ("monitor performance and simplify CapEx delivery" is the observed boundary surface); the operating asset's tenants, rent, and maintenance are Property Management's record. MRI's WIP→asset capitalization is the structural form of the handover.

6. **vs Lease Administration (§17).** Lease-up appears here as milestones/dates toward stabilization; the lease records themselves (terms, obligations, rent schedules) belong to Lease Administration / downstream PM.

7. **vs Construction Cost Management / Progress Billing (§17).** Cost machinery inside construction execution (GC-side contract cost registers; GC bills the owner via progress billing) vs the developer's whole-project budget incl. land/soft costs. The draw/requisition loop here moves funds FROM capital partners TO the developer — a different party and direction from progress billing. Keep separate; machinery interlocks.

8. **vs generic Project Management Application (§03.07, processed).** Per that pass's family note, domain instantiations remain separate Types when the domain adds a defining structure; here the development money spine + development lifecycle stages + capital-partner loop are the domain structures. Keep both.

9. **vs valuation/feasibility tools (Argus/Forbury — checked adjacent).** Standalone CRE valuation/appraisal products value standing assets (Forbury's own positioning: "valuations, appraisals and strategic analysis... throughout the CRE lifecycle"). Appraisal appears inside this Type as a capability (LandInsight appraisal tool; Dealpath underwriting), but a valuation tool without a project record is not development management. Keep separate.

## Historical / Market-Sample Check (§24)

Paper-era developer: land purchase contract file, feasibility/appraisal calculations (residual land value), a development budget ledger (land, professional fees, construction), architect's certificates and draw requests to the lender, milestone and site-meeting notes — satisfies both L0 legs with no software machinery. Regional check: UK small-developer pole (LandInsight) and US institutional pole both fit; ERP-module realization (MRI) fits; self-funded merchant developer without capital-partner machinery fits (LandInsight pole proves capital machinery non-definitional). The definition names no pro-forma mechanics, no draw percentages, no stage labels, no geography. Pass.

## Uncertainties

1. **No Tier-1 operational documentation reached for any sampled product** — all evidence is official product/FAQ pages (marketing-weight). Exact workflow states, status vocabularies, numeric limits, and default behaviors are withheld from the final document; assertions are calibrated to structure-level.
2. **Entitlement/permit tracking**: Dealpath documents permits/surveys/environmental reports as tracked work and "design through permitting" processes; whether systems hold entitlements as first-class objects vs milestones/tasks is unconfirmed — held as a standard capability with milestone realization, not promoted.
3. **Feasibility-tool pole (Argus Developer) and full-suite development-suite pole (Yardi) not directly sampled** — their existence and shape rest on market structure; no product-specific claims made.
4. **Terminal events**: stabilization (Northspyre, Dealpath), sale/disposition (Dealpath), WIP→asset capitalization (MRI) all observed; whether lease-up detail (per-unit absorption, pre-leasing) is tracked as first-class data at any pole is unconfirmed — kept generic.
5. **MRI's development decomposition**: MRI markets no standalone "Development" product today (A-Z evidence); the historical development-heritage module structure is inferred from the current portfolio — treated as ERP-packaging evidence, not product history.

## Final Synthesis

Real Estate Development Management = the developer-side system of record for creating real estate assets: a development project of record (site position + intended built outcome) carried through a staged lifecycle that starts before construction and resolves after it, carrying the project's own money structure (projected costs, commitments, actuals, revised position) — with pipeline views across the firm's projects, milestone/workflow machinery, and, at the capital-funded pole, the funding loop with capital partners (draws, capital calls, lender/investor reporting). The defining core is the project-of-record + money-spine pair; everything else is common mature structure or variant. Construction is overseen, not executed; the asset is created, not operated; the location is an input, not the product; the deal is the funding context, not the record.

Status: leaf validated as a coherent, independent Application Type. No taxonomy change. Forward flags recorded for real-estate-investment-management and site-selection-platform passes.
