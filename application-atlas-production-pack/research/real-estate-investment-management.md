# Research Notes — Real Estate Investment Management

## Research Goal

Understand, from real products, what a Real Estate Investment Management application is: what the investment manager's system of record contains, how an investment moves from sourcing/underwriting through approval, acquisition, hold, and exit, what money structures live on the investment record (capitalization, value, income, returns, distributions), and how this Type separates from Real Estate Development Management, Property Management, Fund Administration / Investor Portal / Private Market Investment Platform (§08), securities-side Portfolio/Investment Management platforms, and Site Selection.

This pass also carries a **forward flag** from the real-estate-development-management pass (processed 2026-09-09): joint review of the shared surfaces (acquisition pipeline, underwriting, portfolio dashboards, investor reporting) with the proposed seam "unit of record = standing asset/portfolio with returns & valuations vs development project carried to built outcome with a cost/commitment spine". Discharged below.

## Initial Boundary

Working hypothesis at start:

- What: software used by real estate investors/investment managers (acquisitions teams, asset managers, fund managers, investor-relations and fund-operations teams) to run real estate as an investment business — the deal pipeline, the held portfolio, and the investor capital behind it.
- Who: acquisitions/analysts, asset managers, portfolio managers, IR, fund/finance operations, executives/investment committees.
- Confusable neighbors: Real Estate Development Management (creating assets), Property Management (operating assets), Fund Administration Platform / Investor Portal / Private Market Investment Platform / Deal Management for PE-VC / Portfolio Management System / Investment Management Platform (§08 financial-investment types), Site Selection, Real Estate Brokerage CRM, standalone valuation tools (Argus/Forbury pole).
- Unknowns going in: what the unit of record is at each market pole (deal? asset? fund? position?); whether investor-capital machinery (capital calls, distributions, waterfalls) is definitional or pole-specific; whether valuation is definitional; where the development seam actually cuts.

## Research Questions

1. What is the unit of record — deal, asset, fund, project, position? How do the poles differ?
2. What lifecycle does the record span (source → underwrite → approve → close → hold → exit)?
3. What money structures exist on the record: capitalization (ownership, equity/debt, classes), value (valuations, budgets), income, returns (projected vs realized), distributions?
4. Who uses the system and what do they do?
5. How do investors (LPs) participate — portals, statements, calls, distributions?
6. How do debt, exposure/risk, and portfolio analytics appear?
7. Where exactly is the seam with Development Management, and with the §08 fund/investment types?
8. Would older/regional/minimal products still satisfy the definition?

## Representative Products

Selected for market representativeness, different product philosophies, different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Dealpath | Deal-workflow pole: "operating system for real estate investing" — sourcing → pipeline → IC execution → fund allocation → owned-asset insights; dispositions and debt pipelines | Institutional investors/managers (CRE investment managers, REITs, homebuilders) | Tier-2 official product pages ×2 |
| MRI Investment Management (incl. Investment Central) | ERP-suite pole: portfolio/asset lifecycle + investment accounting + valuation + investor reporting inside a real-estate suite | Global real-estate investment managers, fund advisors, institutional investors, LIHTC syndicators | Tier-2 official solution + product pages ×2 |
| Juniper Square | Fund-operations pole: GP-side "fund operating system" — funds/entities, investors, positions, capital accounts, calls, distributions, reporting; real estate flagship vertical | Large GPs across private markets (real estate, PE, VC, credit) | Tier-2 official homepage (rich nav + platform copy) |
| InvestNext | Sponsor capital-side pole, real-estate-native, smaller/emerging sponsor tier: projects (property/fund), classes, positions, calls, distributions, portal | Small-to-mid real estate GPs/sponsors | **Tier-1 help center** (collections + article) + Tier-2 homepage |

Checked and dropped: Coyote (UK CRE asset-management regional pole) — transport errors on both root attempts, abandoned. Yardi Investment Suite — not attempted (vendor domain returned 403 in prior passes recorded in STATUS.md); full-suite pole rests on market structure only.

## Sources

All fetched 2026-09-09. WebFetch (text/markdown).

- Dealpath — homepage https://www.dealpath.com/ (Tier-2)
- Dealpath — Portfolio Insights https://www.dealpath.com/portfolio-insights/ (Tier-2)
- MRI Software — Real Estate Investment Management https://www.mrisoftware.com/products/real-estate-investment-software/ (reached as /solutions/investment-management/) (Tier-2)
- MRI Software — Investment Central https://www.mrisoftware.com/products/investment-central/ (Tier-2; timed out once, succeeded on retry)
- Juniper Square — homepage https://www.junipersquare.com/ (Tier-2)
- InvestNext — homepage https://www.investnext.com/ (Tier-2)
- InvestNext Help Center (Tier-1) — root https://support.investnext.com/en/ ; collection "Investment/Project Management" https://support.investnext.com/en/collections/2740018-investment-project-management ; collection "Distributions" https://support.investnext.com/en/collections/2553865-distributions ; article "How to Create a New Project" https://support.investnext.com/en/articles/4831744-how-to-create-a-new-project

Unreachable / dropped (per source-access rules):

- Coyote Software — transport error ×2 (www + bare domain) — dropped; UK regional asset-management pole not directly sampled.
- InvestNext — capital-calls product page https://www.investnext.com/platform/raising-capital/capital-calls/ — 403 (1 attempt); dropped (capital-call flow covered by homepage copy + help-center collection titles).
- MRI — investment-accounting sub-product page not fetched (module existence and scope documented on the solution page).
- No Tier-1 help center reached for Dealpath, MRI, or Juniper Square — their observations are Layer A but marketing-weight; assertions calibrated to structure level.

## Product A — Dealpath (key observations)

Evidence: homepage + Portfolio Insights page. [A]

- Self-labeling: "Real Estate's Leading Deal Management Software"; "The AI-Powered Operating System for Real Estate Investing"; audiences include "Real Estate Investment Managers" (resources section header).
- Platform surfaces: Market Tracking (proprietary comps database; capture every listing via AI extraction, bulk imports, broker feeds), Dealpath Connect (private listing exchange; broker distribution to buyers), Pipeline Management ("shared, real-time view of every active deal across regions and stages"), Deal Execution ("compare underwriting models to see which deals pencil, collaborate on execution tasks and documents, automate and memorialize due diligence and IC approval workflows, and allocate deals to funds"), Reporting & Analytics (dashboards: capital deployment, deals sourced, time to close, staffing capacity), CRM (JV partners, sponsors, brokers, consultants, investors with activity history), Portfolio Insights.
- Portfolio Insights (the owned-asset pole of this product): "Dealpath connects every deal, asset, and fund into one living view of your portfolio."
  - "All Your Owned Assets in One Place": track assets, capital deployment, staffing capacity, composition, industry exposure, pacing by fund.
  - Risk: "diversification across tenants, geography, property types, and other attributes."
  - Asset-management task coordination: "creating periodic budgets and valuations to forecasting revenue growth, tenant turnover, and capital expenditures" — budget cycles and reporting deadlines as coordinated tasks, some with external collaboration.
  - Market comparison: view owned assets alongside comps (own comps, MSCI/RCA comps, Connect listings) to "identify properties for acquisition and disposition."
  - Asset onboarding: "centralizing historical deal context, such as comps and underwriting assumptions, directly alongside asset records"; new-deal underwriting informed by "insights from existing owned assets, synced into Dealpath from external systems" — evidence that property performance data commonly originates in external systems and the investment platform consumes it.
  - Fund rotation audit trail: "a cleanly documented, memorialized audit trail of your entire fund rotation, including owned assets and which deals were considered vs. declined."
- Solutions: Acquisitions, Dispositions ("managing your disposition pipeline in a centralized source of truth"), Development ("manage ongoing projects through delivery"), Debt ("manage loan and origination pipelines... track your loan portfolios").
- Roles (nav): asset management teams and fund managers named on the portfolio page; property-type and role pages exist.

## Product B — MRI Investment Management / Investment Central (key observations)

Evidence: Investment Management solution page + Investment Central product page. [A]

- Self-labeling: "Real Estate Investment Management Software — Maximize returns on your real estate investments"; "a real estate portfolio management platform that integrates financial management with real estate asset lifecycle processes."
- Module map (solution page): Asset management ("analyze investments, evaluate development plans, and forecast property and portfolio performance while enabling collaboration with leasing teams"), Investment accounting ("automate consolidations... Create accurate statements, capital calls, and distributions in just hours"), Investor reporting ("accurate, up-to-date visibility into investment portfolios"), Debt management ("View all portfolio debt in one place"), Fund modeling ("forecasting, transactional simulations, and scenario and sensitivity testing"), Valuation software ("value complex commercial assets; model scenarios, apply local standards, and track valuations"), Asset modeling ("model capital projects, test development returns, and run scenarios to hit target IRR").
- Investment Central product page: "Full lifecycle asset management" for "real estate investment managers, fund advisors and institutional investors"; "consolidates disparate investment data and documents"; features:
  - "Visibility into key metrics: ... key metrics and variances, such as NOI, DCR, cashflow, tenant exposure, valuations and more." — property-anchored investment metrics as first-class data.
  - "Centralized data and report repository: ... rely on MRI Investment Central as the source of record for your investment portfolio information"; "Eliminate Excel as the source of records for your investment portfolio." — system-of-record posture.
  - Risk management across portfolio "or drill down by investment or any attribute."
  - "Automated investment workflows and processes"; publish-quality batch investor reporting; secure investor portal ("10 largest banks access MRI Investment Portal").
- Accounting depth (testimonial quotes): "MRI Investment Accounting allows us to maintain records at each level from the underlying asset up to the client ledger"; consolidations mapped to one chart of accounts; investment accounting produces "statements, capital calls, and distributions."
- FAQ: "helps manage portfolios, track performance, model scenarios, and generate financial reports"; "suitable for both property and fund-level management... asset management at both levels."
- Vertical variant: LIHTC / affordable-housing syndication (syndicator customers, Stratford/Cinnaire/LIHC case studies) — equity-syndication configuration of the same record structure.

## Product C — Juniper Square (key observations)

Evidence: homepage (nav + platform copy). [A]

- Self-labeling: "The operations partner for private markets"; "The fund operating system built for the agentic era"; serving GPs "across every stage of the lifecycle, from first close to final distribution." Who we serve: Real Estate listed first, then PE, VC, Wealth Advisors, Private Credit, Fund of Funds; real-estate flagship clients (Tishman Speyer, Avanath, Greystar, Beacon, Stockbridge, BGO).
- Data model copy: "The data model, relationship graph, and workflow library that 2,300+ GPs rely on. **Every fund, asset, investor, and position—connected.** Every workflow—from fundraising and investor onboarding through fund accounting, treasury, compliance, and reporting—running on the same source of truth." — the four-object model (fund, asset, investor, position) in vendor's own words.
- Solutions: Fund Administration (fund accounting, treasury services, investor services, waterfall modeling, technology, client implementation, AML/KYC), Fundraising & Onboarding (managed close), Investor Management, Deal Services.
- Platform modules: Investor Onboarding, Portal, Investor Reporting, Distribution Payments, Data Rooms, DDQ, Insights, AI CRM for Investor Relations, Admin Oversight Agent.
- Outcomes copy: for IR teams ("LP context, fund data, and history connected—tear sheets, pipeline reports, personalized investor updates"); for CFOs/ops ("Period-close accelerated, PCAPs generated, GL variances analyzed, compliance checks run continuously").
- Scale claims: 2,300+ GPs, 750,000+ LPs, 45,000+ investment entities, $1T investor equity.

## Product D — InvestNext (key observations)

Evidence: homepage (Tier-2) + Help Center (Tier-1). [A]

- Self-labeling (page title): "Real Estate Investment Management Platform"; homepage: "Raise, nurture, and manage capital for real estate with people-centered investment management technology." Audiences: General Partners, Investor Relations Teams, Finance Leaders, Limited Partners.
- Platform map: Access (Raising Capital, Payments & Funding, Capital Calls, Co-Sponsors, Fund Structures), Nurture (Investor Portal, Investor CRM, Subscriptions, Deal Rooms), Management (Distributions, Cap Table Management, Transact Accounts, Document Management, Fund Administration), Compliance (Accreditation, KYC/AML, Security, K-1s & Global Tax Center).
- Tier-1 object model (help center):
  - "A **Project** is a primary concept on the InvestNext platform which is used as a blanket term for a specific investment, whether that be an individual property, investment fund, or any other structure." Creation fields: project name/type, optional legal name, **physical address**, **asset class(es)**, **relevant regulation(s)**, **structure**, currency, unit-calculation precision.
  - Projects carry **classes**: "Adding a New Class to a Project", "Setting Class Ownership Percentages", "Update Class Unit Price (Project)", "How to Delete a Class (Project)"; "How to Archive/Close a Project"; "Assets & Summary Page".
  - **Positions** (investing accounts): "Add a Position (Investing Account) to a Project", "Record an Additional Investment/Contribution for an Existing Investor", "Redeem Shares/Units", "Transfer Ownership (position-to-position and project-to-project)", "Equity Conversion", "Add Debt Positions (Promissory Notes)", "Move a Transaction from One Position (Account) to Another".
  - **Distributions** (Tier-1 collection): "Distribution Plan: Waterfall Hurdles Explained", "How to Create a Distribution Plan", "How to Run a Distribution", "Day Count Convention Explained", "Deductions (ex. Tax Withholding)", "Handling Failed Distribution Payments", "Reclassify/Split Paid Distributions", "Reinvest Dividends", checks FAQ.
- Homepage capability copy: waterfall builder ("complex distribution waterfalls with a point-and-click builder, automatically calculate distributions and send secure payments"), white-label investor portal, accreditation + KYC/AML integrated into onboarding, cap-table automation powering distributions and reporting, ACH payments, document management with K-1 support.
- Testimonials: distribution automation and "visually appealing investor dashboard" as the value center; one customer switched from Juniper Square — evidence both products occupy the same pole at different tiers.

## Cross-product Comparison

| Structure | Dealpath | MRI IM | Juniper Square | InvestNext |
|---|---|---|---|---|
| Investment as persistent record (deal/asset/fund/project) | Yes (deal → asset onboarded with underwriting context; "every deal, asset, and fund") | Yes ("source of record"; records "from the underlying asset up to the client ledger") | Yes ("Every fund, asset, investor, and position—connected") | Yes (Tier-1: Project = "a specific investment, whether property, fund, or any other structure") |
| Lifecycle span source → hold → exit | Yes (sourcing/pipeline → owned assets → dispositions pipeline) | Partial on observed surface (acquisition assessments + full lifecycle asset management claim) | Fund-cycle framing ("first close to final distribution") | Yes (raise → manage → distributions; archive/close project) |
| Capitalization structure (ownership: funds/vehicles/classes/positions, equity+debt) | Partial (fund allocation; deal-to-fund; debt pipelines) | Yes (investment accounting to client ledger; property + fund level) | Yes (fund/vehicle/entity + investor + position) | Yes (Tier-1: classes w/ ownership % + unit price; equity + debt positions) |
| Returns/value content (underwriting, valuations, income metrics) | Yes (underwriting models, comps, periodic budgets/valuations) | Yes (valuations, NOI/DCR/cashflow, fund modeling, target IRR) | Indirect (fund accounting/reporting surfaces value) | Indirect (unit price, cap table; distributions realize returns) |
| Investor capital operations (calls, distributions, waterfalls, statements) | Light (fund allocation only, observed) | Yes (investment accounting: capital calls, distributions, statements) | Yes (deep: calls, waterfall modeling, distribution payments, PCAPs) | Yes (deep, Tier-1: plans, hurdles, deductions, failed payments) |
| Investor-facing portal/reporting | Not observed | Yes (Investment Portal, batch investor reporting) | Yes (Portal, Investor Reporting, onboarding) | Yes (white-label portal, subscriptions) |
| Deal pipeline w/ stages, IC approvals, due diligence | Yes (deep, central) | Partial ("automated investment workflows") | Not on observed surface (deal services listed) | Light (deal rooms; subscriptions) |
| Valuation machinery | Task-level ("periodic budgets and valuations") | Yes (valuation software module) | Not observed | Not observed |
| Debt tracking | Yes (debt solution, loan portfolios) | Yes (debt management module) | Not observed as module | Yes (debt positions/promissory notes) |
| Portfolio analytics / exposure / risk | Yes (diversification, composition, pacing) | Yes (risk mgmt, drill down by attribute) | Partial (Insights) | Partial ("see the bigger picture... diversify") |
| Market/comps data layer | Yes (proprietary comps DB, Connect exchange, RCA) | No (observed surface) | No | No |
| Accounting engine (GL-grade) | No (observed surface) | Yes (investment accounting, consolidations) | Yes (fund accounting, PCAPs, GL variances) | Yes (fund administration module) |
| Document repository + audit trail | Yes (memorialized audit trail, considered-vs-declined) | Yes (centralized repository) | Yes (data rooms, audit trail) | Yes (document mgmt, e-signature) |
| Relationship CRM | Yes (brokers, JV partners, sponsors) | No (observed surface) | Yes (AI CRM for IR) | Yes (investor CRM) |
| Compliance (KYC/AML/accreditation) | No (observed surface) | No (observed surface) | Yes (AML/KYC) | Yes (accreditation, KYC/AML) |
| Regulatory/asset-class packs | Partial (property types, homebuilders) | Yes (LIHTC syndication) | Yes (asset-class verticals) | Yes (relevant-regulations field, Tier-1) |

Reading of the matrix:

- **The investment record + its money content is the invariant.** All four products hold a persistent, identified record for each real-estate investment (deal, asset, fund/vehicle, or project) and carry the investment's money content on it — how it is capitalized and what it yields/returns (Layer B). InvestNext states the abstraction explicitly at Tier-1 ("a specific investment, whether that be an individual property, investment fund, or any other structure").
- **Poles differ in which money content is deep.** Dealpath deepens the front (sourcing, underwriting, approval, allocation) and lightens the investor-capital ledger; MRI deepens the asset/value/accounting center; Juniper Square and InvestNext deepen the investor-capital center (positions, calls, distributions, waterfalls, portals) and lighten the deal front (Layer B).
- **Investor-capital machinery is common-not-definitional** — deep at two poles, module-present at MRI, light at Dealpath (Layer A/B; single-pole strength for the deep machinery).
- **Valuation machinery is common-not-definitional** — explicit at MRI, task-level at Dealpath, not observed at the fund-ops poles (Layer A/B).
- **Deal pipeline + IC execution is common-not-definitional** — central at Dealpath, partial elsewhere (Layer A/B).
- Object vocabularies differ per product (deal/asset/fund vs fund/asset/investor/position vs project/class/position) — the conceptual structure is stable; labels vary.

## Canonical Model

Two jointly-held structures (the defining core):

1. **The investment of record.** A persistent, identified record for each of the firm's real-estate investments, spanning the investment lifecycle: prospective deals (sourced, screened, underwritten), held investments (the owned assets and the funds/vehicles that hold them), and exited investments. The record accumulates its investment context — underwriting and assumptions, decisions and approvals, documents, parties — across the whole arc, and the population of records is the firm's portfolio picture.
   - Remove → a market/listings database, a CRM of relationships, or an asset register with no investment content.

2. **The investment's capital-and-returns money structure.** The investment's own financial content held on the record and revised as the investment advances:
   - **capitalization** — who owns/funds it: the fund/vehicle structure, ownership positions (per-investor where held), equity and debt;
   - **value and returns** — what it is worth and yields: underwritten/projected returns at entry, value and income tracked while held (valuations, budgets, property-anchored metrics), realized proceeds/distributions at exit.
   Realizations vary by pole: underwriting models and fund allocation at the deal pole; valuations, investment accounting and asset→client-ledger records at the asset pole; capital accounts, waterfall distributions and statements at the fund-ops pole.
   - Remove → a property list or pipeline with no investment content, or a free-floating appraisal/waterfall worksheet.

Jointly-held load-bearing:
- 1 without 2 = a deal/property/asset registry (listings-database or CRM territory).
- 2 without 1 = an appraisal or waterfall calculator with no record of the firm's investments.
- Together they are what no neighbor holds: Development Management holds a project with a cost/commitment spine carried to a built outcome; Property Management holds the operating asset (tenants, rent, maintenance); Fund Administration holds the fund's official books and the investor register as the record; securities platforms hold instrument positions against a security master.

## Abstraction Hierarchy (internal)

### L0 — Defining Invariant
- (1) the investment of record (persistent identified real-estate investment records spanning source → hold → exit, accumulating investment context)
- (2) the investment's capital-and-returns money structure on the record (capitalization: ownership/equity/debt; value & returns: projected → tracked → realized, revised over the hold)

### L1 — Common mature structure
- Staged pipeline with approval gates (IC) and due-diligence/task execution; memorialized decision trails
- Underwriting/modeling: scenario & sensitivity testing, fund modeling, target-return framing
- Valuation tracking and recurring budget/valuation cycles on held assets
- Investor capital operations: commitments, capital calls, distribution plans with waterfall calculation, statements, tax documents; investor portal/reporting surfaces
- Debt tracking (portfolio debt; loan pipelines; debt positions)
- Portfolio analytics: composition, exposure (geography/property type/tenant), risk, pacing by fund
- Disposition management and exit tracking with realized returns
- Document repository and audit trail
- Accounting integration/consolidation (investment accounting, fund accounting, GL adjacency)
- Relationship CRM (brokers, JV partners, investors); market/comps data layers (at the deal pole)
- Fund/vehicle structuring (entities, SPVs, master-feeder chains at the fund-ops pole)

### L2 — Variant / optional
- Asset-class and regulatory packs (affordable-housing/LIHTC syndication; regulation fields on the record)
- Compliance machinery (KYC/AML, accreditation) at the sponsor/fund-ops pole
- Co-sponsorship/JV configurations; wealth/advisor distribution channels
- Development projects as investment content (development pipelines; development-return modeling) — the Development Management seam
- Debt-origination pipelines (lending-side configuration)
- Treasury/payments rails (distribution payments, ACH); data rooms/DDQ; treasury services
- Map views, mobile, AI assistance (era-current)
- Third-party (administrator) vs in-house (manager) operating posture of the same record structure

### L3 — Vendor-specific (research notes only)
- Dealpath: Dealpath Connect private listing exchange; Dealpath AI; MSCI/RCA comps integration; "$10T+ transactions" and "300+ firms" claims; homebuilder configuration
- MRI: Investment Central / Investment Portal / Data Management Services module names; Agora platform; LIHTC/syndicator customer stats; "NOI, DCR, cashflow, tenant exposure" metric list
- Juniper Square: GPX platform, JunieAI, Headless GPX (MCP exposure), Admin Oversight Agent "Fay", Managed Close, DDQ/Data Rooms packaging; 2,300+ GPs / 750k+ LPs / 45,000+ entities / $1T equity claims
- InvestNext: Transact Accounts; MCP early access; 96% retention / "2x faster go-live" claims; unit-calculation-precision field; Intercom-based help center

## Vendor-specific Findings

See L3. Additional structural notes: Dealpath is the sampled evidence that the deal pole deliberately straddles into Development Management (its development solution was sampled by that pass) and into Debt (origination/loan portfolios — a separate §17/§08 territory at most). MRI is the sampled evidence that suite vendors decompose this Type into named modules (asset management, investment accounting, valuation, fund modeling, debt management) — the decomposition confirms the internal structure rather than changing it. Juniper Square and InvestNext are the sampled evidence that the fund-ops pole straddles into Fund Administration Platform / Investor Portal territory while self-labeling as real-estate investment management.

## Boundary Findings

1. **vs Real Estate Development Management (§17, processed) — FORWARD FLAG DISCHARGED, JOINT REVIEW, keep-both RATIFIED.** Shared surfaces confirmed from this side: acquisition pipeline, underwriting, portfolio dashboards, investor/capital reporting; Dealpath appears in both passes' samples deliberately (the investing OS markets a development solution; the dev pass sampled it as the deal-OS pole). The seam holds at the **unit of record + money spine**: here the record is a standing investment (deal/asset/fund) with a **capital-and-returns** spine whose lifecycle resolves at exit/distribution; there the record is a development project with a **cost/commitment** spine carried to a built outcome, resolving at stabilization/sale/capitalization. Direction of money differs structurally: returns/distributions flow back to capital here; draws/funding flow in to pay costs there. Removal tests ratified both ways: strip the development arc + cost spine from a development product → acquisition/investment management remains (Dealpath's acquisitions solution is exactly this); strip sourcing/valuation/returns/investor machinery → development management remains. Corroboration: suite vendors keep the two as separate named modules (MRI Project4000/Capital Project Control vs MRI Investment Management). Deliberate straddling does not merge the Types; the record's center of gravity decides.

2. **vs Commercial / Residential Property Management (§17).** The operating asset (tenants, leases in operation, rent collection, maintenance) vs the investment record (value, returns, ownership, capital events). This Type consumes property-level performance as investment content (asset metrics "such as NOI, DCR, cashflow, tenant exposure"; "forecasting revenue growth, tenant turnover, and capital expenditures" as asset-management tasks; "collaboration with leasing teams") but does not run operations. Remove test: strip tenancy/operations → this Type stands; strip value/returns/ownership → property management.

3. **vs Lease Administration (§17).** Lease records, terms, and obligations belong to Lease Administration; here leases appear as income/exposure context and abstractions (tenant exposure, revenue-growth forecasting).

4. **vs Fund Administration Platform (§08, processed 2026-09-07) — consistency note, seam ratified from this side.** That pass's core: the administered fund as organizing record + official books/records (investment-grade GL) + investor register with per-investor capital accounts. The fund-ops pole of this Type (Juniper Square, InvestNext — which even ships fund-administration modules) carries all of that machinery, but this Type's record center is the **real-estate investment itself** (property-anchored value/returns content, deal front, asset lifecycle), with investor capital machinery as how the investment is capitalized and settled. Fund Administration's center is the fund's **official books** (asset-class-agnostic, audit/authority posture). Straddle is deliberate and double-sided in-sample (both sampled fund-ops products self-label as real-estate investment management AND sell fund administration). Keep-both; the overlap region is real-estate fund administration.

5. **vs Investor Portal (§08, processed 2026-09-07).** The portal is the LP-facing delivery surface (authenticated external investors, scoped views, published documents); this Type holds the underlying investment record and capital operations that feed such surfaces (every fund-ops-pole product ships a portal). Surface vs system of record. Keep-both.

6. **vs Private Market Investment Platform (§08, processed 2026-09-06).** That Type is the **investor-side** platform (listed offerings, eligibility gate, commitment-to-execution, investor-side portfolio). This Type is the **manager-side** system of record. Sides differ; subscription-capture machinery appears in both but from opposite sides (InvestNext captures investor intent for the sponsor). Keep-both.

7. **vs Deal Management for Private Equity / VC (§08, unprocessed) — forward note.** Deal objects are company equity vs real property; the downstream record differs structurally: this Type's closed deal matures into an owned-asset record carried through a multi-year hold (valuations, income, capital events), which a company-deal tracker does not hold. Dealpath is the CRE instantiation of deal management and demonstrates the property-specific extension. Ratify at that pass if needed.

8. **vs Portfolio Management System / Investment Management Platform (§08, processed 2026-09-06/07).** Those centers are securities books of record (positions/transactions/cash against a security master; forward-management loop with order execution). Here the center is physical property assets with leases, capex, valuations, and property-anchored metrics, held for years without order execution machinery. Different object substrate, different lifecycle, different data. Keep-both.

9. **vs Wealth Management Platform (§08, processed 2026-09-08).** Client-relationship-centered advisory record vs investment-centered manager record. Distinct.

10. **vs Site Selection Platform (§17, unprocessed) — forward note.** Dealpath's Market Tracking/Connect straddle the seam from this side: pooled market/comps data and listing exchange serve discovery, but the record here is the firm's investment, not the location data product. Consistent with the development pass's proposed seam.

11. **vs Real Estate Brokerage CRM / CRM (§07).** Relationship tracking (brokers, JV partners, sponsors) is a surface here; the record is the investment, not the relationship.

12. **vs standalone valuation/feasibility tools (Argus/Forbury pole — checked adjacent).** Valuation appears inside this Type as a capability (MRI valuation software; Dealpath periodic valuations); a valuation engine without the investment population and its lifecycle is not this Type. Keep separate.

## Historical / Market-Sample Check (§24)

Paper-era investment office: property acquisition files with underwriting memos/appraisals, a capital ledger recording partners' shares and contributions/distributions, income and periodic valuation records, disposition files — satisfies both L0 legs with no software machinery. Single-owner investor ledger (ownership structure trivial, capitalization = price + debt) still fits: L0-2 does not require per-investor positions, only the capital-and-returns content. Regional check: UK/European institutional property asset management (asset records + valuations + fund structures) fits; pre-cloud ERP-era investment accounting (records from underlying asset up to client ledger) fits; regional fund-ops products fit. The definition names no portals, no AI, no waterfall-hurdle specifics, no stage labels, no geography, no asset class. Pass.

## Uncertainties

1. **Tier-1 operational documentation reached only at InvestNext** (help-center collections + one article; object model confirmed at title level). Dealpath/MRI/Juniper Square evidence is official but marketing-weight (Tier-2). Structure-level assertions only; no status vocabularies, numeric limits, or default behaviors stated in the final document.
2. **Returns-metric vocabularies** (IRR named only at MRI: "hit target IRR"; equity-multiple/cash-on-cash not directly observed in-sample) — kept generic in the final document.
3. **MRI investment-accounting module internals** (whether per-investor capital accounts are native to the module or suite-adjacent) not directly verified — the module's public copy names capital calls, distributions, statements, and asset→client-ledger records; per-investor register depth assumed from the fund-ops pole, not from MRI.
4. **Dealpath asset-record depth**: owned-asset performance is "synced into Dealpath from external systems" — the deal pole's asset record appears context/analytics-weight rather than an operating-data store; not confirmed further.
5. **Coyote (UK regional pole) and Yardi (full-suite pole) unsampled** — regional and full-suite-ERP realizations rest on market structure; no product-specific claims made.
6. **Whether "Deal Services" at Juniper Square includes a deal pipeline** is unconfirmed from the observed surface — kept out of the fund-ops pole's characterization.

## Final Synthesis

Real Estate Investment Management = the investment-side system of record for real estate: a persistent population of identified investment records (prospective deals, held assets and the funds/vehicles that hold them, exited investments) each carrying the investment's capital-and-returns money structure — how it is capitalized (ownership, equity/debt) and what it yields (underwritten returns at entry, value and income while held, realized proceeds at exit) — revised as the investment advances through the investment lifecycle from sourcing to exit. Around this core, mature products add the staged pipeline with approval gates, underwriting and scenario modeling, valuation and budget cycles, investor capital operations (calls, waterfall distributions, statements, portals), debt tracking, portfolio analytics, and accounting consolidation. The market realizes the Type at three poles (deal-workflow, asset/accounting, fund-operations) that deliberately straddle Development Management (project + cost spine), Property Management (operating asset), and the §08 fund/investment types (official books, investor-facing surfaces, securities books) — the record's center of gravity (investment with capital-and-returns spine) decides the Type.

Status: leaf validated as a coherent, independent Application Type. No taxonomy change. Development-management forward flag discharged (keep-both ratified). Consistency notes recorded vs fund-administration-platform; forward notes left for deal-management-for-private-equity-vc and site-selection-platform passes.
