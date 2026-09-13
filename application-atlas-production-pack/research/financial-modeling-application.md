# Research Notes — Financial Modeling Application

## Research Goal

Understand what a Financial Modeling Application is as an Application Type: what the central artifact is, what objects exist inside it, how users build and use models, and where the Type's boundaries lie against spreadsheets, budgeting/forecasting platforms, actuarial modeling platforms, and FP&A platforms.

Context: this leaf carries a pre-existing joint-review flag from `actuarial-modeling-platform` (recorded in STATUS.md Boundary Issues) and a recorded seam from `budgeting-forecasting-platform` ("Financial Modeling (no org-wide cycle)"). Both must be answered from this side.

## Initial Boundary

Working hypothesis at start:

- The Type's center is the **financial model itself** — a persistent, user-built quantitative structure of a business's financial situation and prospects (assumptions → logic → projected statements/valuation).
- Nearest neighbors: Spreadsheet Application (general calculation grid), Budgeting & Forecasting Platform (governed planning cycle), FP&A Platform (umbrella), Actuarial Modeling Platform (insurance-liability semantics), Cash-flow Forecasting (slice), BI/Dashboard (reads actuals vs writes projections).
- Known recorded seams to respect:
  - budgeting-forecasting-platform (processed): "boundaries held vs ... Financial Modeling (no org-wide cycle)"
  - financial-close-management (processed): "FP&A (backward vs forward)"
  - actuarial-modeling-platform (processed): "financial modeling applications model corporate statements/valuation for finance teams"

## Research Questions

1. What is the central artifact, and what is it called in real products (model / plan / analysis / forecast)?
2. What are the core objects: assumptions, drivers, formulas, periods, actuals, scenarios, statements, entities?
3. What is the canonical build→use loop?
4. Where does data come from (manual entry, GL/accounting imports, live connections)?
5. How do scenarios work — copies, dimensions, or layered alternatives in one model?
6. What output surfaces exist (statements, dashboards, reports, exports, presentations)?
7. Is valuation machinery part of the Type?
8. What collaboration/governance exists (sharing, roles, audit)?
9. §24 check: would Excel-era modeling practice (no scenario machinery, no data connections, desktop) still fit the definition?
10. Boundary tests vs each neighbor: what to remove/add to cross the seam?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Customer tier | Evidence level reached |
|---|---|---|---|
| Quantrix Modeler | structural "beyond spreadsheet" modeling (desktop, matrix-based) | enterprise/analyst, 20+ years old | Tier-2 product page (rich) + Tier-1 help TOC; deep help articles 404 ×2 |
| Synario | scenario-centric, integrated-statements, institutional | higher-ed / utilities / transit / public sector / corporate | Tier-2 product pages (rich, incl. integrated-statements feature page) |
| Jirav | driver-based cloud modeling for SMB/VC-funded + accounting-firm channel | SMB / VC-funded / advisory firms | Tier-1 help center (Plan section + drivers article deep) + Tier-2 product page |
| PlanGuru | SMB budgeting-flavored 3-statement modeling (desktop + online) | small business / nonprofit / accountants | Tier-1 help center TOC + Tier-2 product page; overview article body empty |
| Lucanet xP&A (Causal lineage) | modern cloud modeling (Causal acquired by Lucanet) | mid-market finance teams | Tier-1 KB index/TOC only — sub-pages JS-rendered, same index returned for all paths |

Rejected/adjusted samples:

- **Finmark** — finmark.com now redirects to BILL's financial-operations platform (Finmark absorbed; standalone product documentation gone). Recorded as market drift; startup pole covered instead by Jirav's VC-funded positioning.
- **Pry** — acquired by Brex; not attempted (expected sunset).
- **Excel / Google Sheets** — boundary context only; they are Spreadsheet Application per directory (see collaborative-spreadsheet research notes). Not fetched; the seam is documented from the FMA side (products position against spreadsheets).

## Sources

- Quantrix: https://quantrix.com/ , https://quantrix.com/products/quantrix-modeler/ , https://quantrix.com/modeler-help/ (help TOC at info.idbs.com), fetched 2026-09-06
- Synario: https://www.synario.com/ , https://www.synario.com/features/integrated-financial-statements/ , fetched 2026-09-06
- Jirav: https://www.jirav.com/ , https://help.jirav.com/ , https://help.jirav.com/plan , https://help.jirav.com/intro-to-opex , fetched 2026-09-06
- PlanGuru: https://planguru.com/ , https://help.planguru.com/knowledge , https://help.planguru.com/knowledge/planguru-app-online , fetched 2026-09-06
- Lucanet xP&A (Causal): https://docs.causal.app/ (index + TOC only; sub-pages JS-rendered), fetched 2026-09-06
- finmark.com (redirect to BILL — drift observation), fetched 2026-09-06

## Product Observations

### Quantrix Modeler (structural modeling pole)

Evidence layer: A (directly observed, product page + help TOC).

- Self-positioning: "business and financial modeling application" that "addresses the limitations and risks inherent in traditional spreadsheets"; "Think Outside the Cell"; "Beyond Excel financial modeling software for serious modelers".
- **Model** is the central artifact; help TOC chapters: "Planning and building a model", "Understanding the parts of a Quantrix model", "Working with structure", "Working with formulae", "Working with data", "Presenting a model", "Sharing a model", "Integrating data".
- **Structure/logic separation**: "Separate Structure from logic — Formulas will automatically update to reflect new structure."
- **Multi-dimensional matrices with categories** (dimensions): "Category linking — keep your lists of items in sync across a model — product, region, scenario or year is as easy as a single click."
- **Natural language formulas**: names ("Revenues", "Expenses") instead of cell addresses (B2); "one formula can calculate hundreds, thousands or even millions of cells."
- **Visual dependency inspector**: "interrogate the logic driving a particular value... visualize and navigate to the dependencies."
- **Interactive dashboards**: "users of your model only need to access certain parts of the model such as assumptions and results"; "Separating the presentation from the structure and logic of the model."
- **Data import/export**: "connect to the most current data and update it with a click of a button"; "Integrate with virtually any data source."
- **Optimization/solver**: built-in goal seek, multi-dimensional solver (Simplex, non-linear, genetic).
- **Groovy scripting** for automation.
- **Qloud** (cloud sharing/collaboration) and **Enterprise** (version control, security, user roles and permissions, cell-level audit trail, data-level role permissions).
- Use cases: forecasting, data analysis, scenario planning, budgeting, planning, data validation, M&A, CPQ. Industries: corporate finance, real estate & investment, energy, agriculture, financial services, PE/VC, commercial banking.
- Marketing stats (50,000 users, 1,200 companies, 95% fewer formulae, calculated-cells counts) — vendor claims, not asserted as facts.

### Synario (scenario/integrated-statements pole)

Evidence layer: A (directly observed, product + feature pages).

- Self-positioning: "Financial Modeling Software" / "purpose-built platform that makes it easy to build, modify, and maintain high-performance financial models"; "Customizable, built-to-scale FP&A solutions that bridge the gap between short-term budgeting and long-term forecasting."
- **Integrated financial statements out of the box**: "Built-in financial relationships... Unlike spreadsheets, there is no elaborate formula writing or complex relationship management. Synario's connected financial statements all live within a single financial model, eliminating your version control issues."
- **Pre-mapped accounting**: upload a .csv of historicals, "linking your labels into our connected architecture, and Synario will output a complete financial statement... sorted by your Income Statement, Balance Sheet, and Cash Flow."
- **Automated statement modeling**: "add in your formulas, your logic, and have it populated throughout the line items of your income statement, balance sheet, and cash flow statement. The outputs of your logic are based off of your historical data, new assumptions, projects, initiatives... All within a single model."
- **Multiverse Modeling** (patented, vendor-branded): "explore a multitude of financial outcomes in one financial model... layer different financial scenarios and compare them to each other in one central hub helping you to escape your spreadsheet version control issues."
- **Rolling cash flow modeling**: "projects your financial statements all the way down to cash over a 20+ year time-frame... enter your formulas into one central area and link the line items... any changes to the formulas will be populated throughout."
- **Formula-free pivoting**: statements pivot "along multiple axes... time, division, department, scenario."
- **Toggled sliders for initiatives**: "strategic and financial initiatives can be incorporated... through toggled sliders... isolate the impact a given initiative has across all three financial statements."
- **Click to Confidence** (explain feature): "access detailed explanations for each calculation within their models... breaking down the logic behind calculations"; AI insights add natural-language explanations; anomaly detection scans reports for outliers.
- **Cloud collaboration**: "real-time access to your models, stakeholders across departments can review, adjust, and analyze data together"; changes instantly update "presentations."
- **Import/export**: "easily import your audited financial data from your existing model or ERP system"; "export to multiple file formats."
- Users: "Modelers and Analysts" + "CX Leaders". Industries: higher education, water & utilities, transit, public sector, corporations, real estate, telecom, manufacturing, healthcare, accounting, government.
- Owned by PFM Solutions (public finance). Marketing stats (78% accuracy increase, $25m revenue, etc.) — vendor claims.

### Jirav (driver-based cloud pole)

Evidence layer: A (directly observed, Tier-1 help center + product page).

- Self-positioning: "all-in-one forecasting, budgeting, reporting, and dashboarding solution"; "Our powerful, integrated, and driver-based software forecasts the P&L, balance sheet, and cash flow."
- Help-center structure: Getting Started (Navigation & Terminology), Dashboards, Report, **Plan** ("Use your accounting, workforce, and operational data to create a driver-based financial model"), Settings (Your Company / Configuration / **Model** / Admin), Integrations ("Connect your Actuals").
- **Plan** is the model container: Plan Management, Plan Tables, Plan Drivers, Update Plan with Actuals, Plan of Record (POR), Active & Archived Plans, Sharing Plans, Task Management.
- **Driver mechanics** (from "Introduction to Planning with Drivers, Assumptions & Subitems"):
  - Drivers "utilize logical formulaic expressions to predict future planning periods" (e.g., 3-month trailing average of actuals plus 5% annual growth).
  - Standard driver library: Annual Target, Fixed Spread, Growth on Historicals, Periodic Growth, $ per Headcount, % of Another Account, Custom.
  - **Assumptions**: "key variables for your company that can be referenced throughout your plans via drivers" (e.g., $ per headcount); "an identifiable summary of all assumptions made in the model that can easily be reviewed and modified"; clicking an assumption highlights referencing accounts.
  - **Subitems**: month-specific detailed entries with text description (e.g., a particular vendor); department-scoped; cannot carry drivers.
  - "A combination of multiple drivers, subitems, and direct input can be used for the same account, everything in Jirav is additive in nature."
  - Drivers can be cloned across accounts/departments; start/end date, frequency, rounding editable.
- **Balance Sheet and Cash Planning** chapter: AR planning, Direct Cash Flow, Minimum Cash Balance, Inventory, Prepaids & CapEx, System Cash, Deferred Revenue, Loan Schedule, Line of Credit.
- **Workforce Planning** chapter: staff roster, driver-based hire architecture, payroll (bi-weekly, hourly).
- **KPIs**: SaaS metrics, cumulative formulas.
- **Actuals integration**: Accounting Actuals, Workforce Actuals, Custom Table Actuals, Budget Imports; "Update Plan with Actuals"; actuals imports from Excel/Google Sheets affect the forecast.
- **Plan administration**: Annual Budget Steps, Month-End Close Steps, Rolling Forecast Checklist, Rolling Forecasts (Budget vs Actual).
- **Auto-Forecast**; **Consolidations** under Custom Tables.
- Audiences: SMBs, VC-funded companies ("operating plans, investor packages, cash flow insights"), accounting & CFO advisory firms (FP&A advisory channel); industry blueprints/templates.

### PlanGuru (SMB budgeting-flavored pole)

Evidence layer: A (directly observed, Tier-1 help TOC + product page).

- Self-positioning: "Business Budgeting Software, Business Planning Software"; "integrated 3-Way Forecasting software."
- **Container hierarchy**: Company → Project → Scenario ("Creating a Company, Project, and Scenario"; "Delete a Scenario, Project, or Company"; "Duplicate a Scenario"); desktop version's artifact is the "Analysis" ("Analysis Setup", "Build an Unlimited # of Analyses per Company").
- **Pre-built statement structure**: "Pre-built Integrated Financial Statement Structure"; "Automatically solved Cash Flow Statement"; "Forecast all 3 Financial Statements — integrated income statement, balance sheet, and cash flow."
- **Projection methods**: "over 20 powerful forecasting methods... intelligent, turn-key methods, plus the ability to build custom business drivers, including non-financial data" (vendor count claim); help TOC shows: Growth Rate, Percent of Other Accounts, Trend or Average, manual entry, "Building a Formula with Assumptions & KPIs."
- **Balance-sheet machinery** (help TOC): Cash and Cash Equivalents, Average Days to Collect, Days Cost of Sales, Prepaid Expenses, Fixed Assets/Depreciation/Accumulated Depreciation, Average Days to Pay, Accrued Expenses, Line of Credit, Note Payable, Retained Earnings, Taxes based on Net Income.
- **Actuals import**: QuickBooks / QuickBooks Online / Xero / Excel / other accounting systems; "Import up to 5 years of Actual Results" (vendor claim); "general ledger import utilities... import historical results in only a few minutes... view budget vs actual reports and build rolling forecasts."
- **Maintenance**: Monthly Roll Forward (Forecast), Annual Roll Forward, Archiving Your Budget.
- **Extras**: Financial Ratios, Business Valuation Tool, VAT/GST calculation, Smart Groups, Consolidations ("Consolidate Unlimited # of Projections"), Payroll Utility, Notes Payable and Line of Credit Tools.
- **Reporting**: PlanGuru Analytics (powered by Reach Reporting) — dashboards, reports, user roles; Standard Reports (financial statement reports, charts); Excel Add-in; export to PDF/Word/Excel.
- Audiences: small businesses, franchises, nonprofits, accountants/advisors (Advisor Plans); PlanGuru Launch implementation service.
- Deployment: Online App + Windows Desktop (legacy lineage).

### Lucanet xP&A (Causal lineage) — limited evidence

Evidence layer: A at TOC level only.

- docs.causal.app now serves the Lucanet Knowledge Base; the xP&A solution is documented with chapters: "Basic Concepts and Elements", "Creating a Model", "Integrating Data", "Modeling Your Data", "Viewing and Visualizing Data", "Working with Models", "Using Comments and Descriptions", "Comparison: xP&A vs. Excel Performance".
- Positioning: "Modeling, forecasting, planning... a 360° view of planning and analysis data from a single source of truth"; part of the Lucanet CFO Solution Platform (alongside Consolidation & Financial Planning, ESG Reporting, Disclosure Management, Lease Accounting, Banking & Cash Management, Tax Compliance).
- **Limitation**: all sub-page URLs return the same index content (JS-rendered KB); no operational detail reachable. Vocabulary confirms model-as-artifact + integration + modeling + views structure, consistent with the other samples, but no deeper claims drawn.

### Market drift observations

- **Finmark** (finmark.com) now redirects to BILL's financial-operations platform — the standalone startup-modeling product is no longer independently documented. The startup-modeling niche (Finmark, Pry) has been absorbed into broader platforms.
- **Causal** absorbed into Lucanet's xP&A suite — the modern cloud-modeling brand now lives inside a CFO-suite vendor.
- Both drifts suggest consolidation of the standalone modeling-tool market into suites; the Type persists as the modeling layer inside larger platforms.

## Cross-product Comparison

| Structure | Quantrix | Synario | Jirav | PlanGuru | Lucanet xP&A (Causal) | Evidence |
|---|---|---|---|---|---|---|
| Model as named persistent artifact | Model | Model ("single financial model") | Plan (+ Plan of Record) | Company→Project (+ desktop "Analysis") | Model | B |
| Explicit assumptions/inputs | Assumptions (dashboard-accessible) | Assumptions, initiatives | Assumptions + Drivers + Subitems | Assumptions & KPIs, custom drivers | (TOC only) | B |
| User-defined logic w/ propagation | Natural-language formulas, structure-aware | Formulas populated across line items | Drivers (formulaic expressions) | Projection methods + formulas | Modeling Your Data | B |
| Time-period projection | Categories (year/month typical) | Months→20+ years rolling | Monthly planning periods | Monthly, multi-year | Planning periods | B |
| Integrated 3-statement structure | Free-form (matrices; statements possible, not forced) | Out-of-the-box, pre-connected | Forecasts P&L + BS + CF | Pre-built, auto-solved CF | (TOC only) | B (A for 3 products; free-form pole documented) |
| Actuals import/integration | Data import, any source | CSV/ERP audited financials | Accounting/workforce actuals integrations | QuickBooks/Xero/Excel GL import | Integrating Data | B |
| Scenario analysis | Scenario as category/dimension | Multiverse: layered scenarios in one model | Multiple scenario plans | Scenario object under project | (TOC only) | B |
| Driver/method library | Formula language + functions | Built-in financial relationships | Standard driver library | 20+ methods (vendor claim) | (TOC only) | B |
| Reporting/dashboards | Interactive dashboards, charts | Real-time visualizations, presentations | Dashboards + reports | Analytics dashboards + standard reports | Viewing and Visualizing Data | B |
| Explain/traceability | Dependency inspector | Click to Confidence | Assumption→account highlighting | (not observed) | (TOC only) | B (3 products) |
| Collaboration/sharing | Qloud, roles, audit trail | Cloud collaboration | Sharing Plans, task mgmt | Users, Analytics roles | Working with Models | B |
| Roll-forward / maintenance | (not observed at depth) | Rolling cash flow | Rolling forecast checklist, month-end steps | Monthly/annual roll forward | (TOC only) | B (3 products) |
| Valuation machinery | (not observed) | (not observed) | (not observed) | Business Valuation Tool | (TOC only) | product-specific (PlanGuru) |
| Optimization/solver | Goal seek + solver | (not observed) | (not observed) | (not observed) | (TOC only) | product-specific (Quantrix) |
| Scripting | Groovy | (not observed) | (not observed) | (not observed) | (TOC only) | product-specific (Quantrix) |
| Workforce/headcount depth | (not observed) | (not observed) | Staffing chapter | Payroll utility, workforce planning | (TOC only) | B (2 products) |
| Consolidations | (not observed) | (not observed) | Consolidations | Consolidations | (TOC only) | B (2 products) |
| Templates/blueprints | Example models | (not observed) | Industry blueprints | (not observed) | (TOC only) | B (2 products) |
| AI assistance | (not observed) | Anomaly detection, AI insights | (not observed) | (not observed) | (TOC only) | product-specific (Synario) |

## Canonical Model

### L0 — Defining Invariant (minimal)

```text
Financial Model (persistent, user-built artifact representing
                 an organization's/project's financial situation & prospects)
├── Explicit assumptions / inputs (user-set, distinct from calculated results)
├── User-defined calculation logic linking inputs → outputs
│   └── propagation: changing inputs recalculates outputs
└── Time-period projection of financial results (the output layer)
```

Four properties. Remove any one and the product stops being recognizable as a financial modeling application:

1. **The model as persistent artifact** — a named, storable, user-built structure (not a one-off calculation). Without it, the product is a calculator or a report.
2. **Explicit assumptions/inputs** — values and drivers the user sets, conceptually separated from computed results. Without the separation, there is no model to interrogate — only a fixed document.
3. **User-defined logic with propagation** — formulas/methods the user defines connect inputs to outputs; editing an input flows through to every dependent result. Without propagation, it is a static projection, not a model.
4. **Time-period projection** — outputs are financial results laid out over periods (months/years), typically mixing historical actuals with future projections. Without the time dimension, it is a snapshot, not a financial model.

§24 historical check: Excel/Lotus-era modeling practice (inputs block → calculation rows → projected statements; no scenario machinery, no data connections, no cloud) satisfies all four properties. Quantrix (founded to move "beyond spreadsheets") and PlanGuru's legacy Windows desktop product also fit. The definition does not overfit to modern cloud patterns (live connections, AI, cloud collaboration are all non-definitional).

Deliberately NOT in L0 (despite being near-universal in the dedicated-tool sample):

- **Integrated three-statement structure** — pre-built in statement-anchored products (Synario, PlanGuru, Jirav) but free-form in the structural pole (Quantrix models need not be statement-shaped; use cases include CPQ, energy-market forecasting). The three-statement model is the canonical common form, not the invariant.
- **Scenario analysis** — present in all sampled dedicated products, but the historical dominant implementation (spreadsheet modeling) does it without first-class machinery. Same anti-overfitting pattern as phone-number identity in IM.
- **Actuals integration** — modern products treat it as standard, but a purely forward-looking model (e.g., a startup pre-revenue model with no actuals) is still a financial model.

### L1 — Common Mature Structure

- Integrated financial statements (income statement, balance sheet, cash flow) as the canonical output structure — pre-built and auto-linked in statement-anchored products; constructible in structural products.
- Actuals integration — GL/accounting-system imports (QuickBooks/Xero/Excel/CSV class) or live connections; actuals vs projection separation inside the model.
- Scenario analysis — multiple assumption sets / initiatives compared within one model (layered scenarios, scenario dimensions, or scenario objects).
- Driver/projection-method libraries — standard reusable logic (growth, % of another account, $ per headcount, trend/average, periodic change).
- Balance-sheet & cash machinery — working-capital days, debt/LOC schedules, depreciation, prepaid/accrual handling, cash-flow solving.
- Reporting & dashboards — charts, statement reports, presentation canvases; export (PDF/Excel/Word).
- Explain/traceability — dependency inspection, calculation explanations, assumption→affected-account highlighting.
- Collaboration/sharing — cloud model sharing, roles, comments; enterprise audit trails at the high end.
- Templates/blueprints — industry or use-case starting points.
- Roll-forward maintenance — advancing periods, refreshing actuals, rolling forecasts.

### L2 — Variant / Optional Structure

- Modeling-substrate philosophy: **structural/free-form** (user defines dimensions and logic from scratch; statements optional) vs **statement-anchored** (pre-built IS/BS/CF skeleton; user fills logic).
- Deployment: desktop (legacy lineage, e.g., Windows modeling apps) vs cloud SaaS vs desktop+cloud hybrid.
- Customer tier: SMB/self-service vs institutional (higher-ed, utilities, transit, public sector) vs enterprise (roles, audit, version control).
- Budget-cycle machinery depth: lightweight (budget archiving, annual budget steps, month-end close steps) — the straddle zone toward budgeting/forecasting platforms.
- Valuation machinery (product-specific in sample: PlanGuru Business Valuation Tool).
- Optimization/solver, scripting/automation (Quantrix).
- Workforce/headcount planning depth; consolidations across entities/projections.
- KPI frameworks (e.g., SaaS metrics); non-financial drivers (units, ridership, enrollment).
- AI assistance (anomaly detection, natural-language explanations).
- Advisory-firm channel (white-labeled client modeling as a service).

### L3 — Vendor-specific (research notes only)

- Quantrix: matrices/categories/category-linking, always-on pivot, Qloud, Groovy, "Think Outside the Cell" framing, 95%-fewer-formulae claim.
- Synario: Multiverse Modeling (patented), Click to Confidence, toggled initiative sliders, formula-free pivoting, PFM Solutions ownership.
- Jirav: Plan of Record (POR), UA Picker, Auto-Forecast, subitems, "everything is additive" composition rule, driver library names (Annual Target, Fixed Spread, Trended Actuals).
- PlanGuru: Company→Project→Scenario hierarchy, "Analysis" artifact naming, 20+ methods / 10-year / 5-years-actuals claims, Analytics powered by Reach Reporting, PlanGuru Launch service.
- Lucanet: xP&A naming, CFO Solution Platform bundling, "Comparison: xP&A vs. Excel Performance" chapter.

## Vendor-specific Findings

See L3 above. None promoted to the canonical document except as neutral examples where they illustrate a common capability (e.g., "a driver library" is common; "Annual Target driver" is Jirav's).

## Boundary Findings

### vs Spreadsheet Application (§03.03) — sharpest seam

- FMA products define themselves against spreadsheets: Quantrix "addresses the limitations and risks inherent in traditional spreadsheets"; Synario "Unlike spreadsheets, there is no elaborate formula writing"; Jirav "ditching your outdated V50 Excel model"; Lucanet ships a "Comparison: xP&A vs. Excel Performance" chapter.
- Structural distinction: a spreadsheet is a general-purpose addressed-cell grid with arbitrary layout and no financial semantics; an FMA imposes financial-model semantics — named assumptions/drivers, period structure, statement/line-item organization, scenario machinery, actuals linkage.
- Test: remove the financial semantics (assumptions/periods/statements) → you have a spreadsheet. Add them as product structure → you have an FMA.
- Interchange exists (Excel import/export, Excel add-ins — PlanGuru) and spreadsheets remain the incumbent modeling substrate in practice; that makes the spreadsheet the Type's principal "previous way of working", not a member of the Type.

### vs Budgeting & Forecasting Platform (§08, processed) — seam confirmed from both sides

- Their recorded seam: "Financial Modeling (no org-wide cycle)". Confirmed here: none of the sampled products carries the governed planning cycle that defines that Type (budget-owner contribution against a finance-defined structure → consolidation → approval/promotion path → locked official plan; versioned plan data as first-class switchable datasets).
- FMA products do carry lightweight budget machinery (Jirav Annual Budget Steps / Month-End Close Steps; PlanGuru budget archiving/roll-forward) — this is the straddle zone, and both vendors market into budgeting/forecasting categories. The center of gravity remains the model artifact (build/maintain/explore), not the governed cycle.
- Test: remove the model-artifact centrality and add the governed multi-contributor approval cycle → budgeting-forecasting platform. Remove the governed cycle → FMA.

### vs Actuarial Modeling Platform (§08, processed) — joint-review answer

- The shared abstract pattern (assumptions → calculation logic → projected outputs over time) is generic modeling machinery, not evidence of sameness.
- The seam is the **modeled object's semantics + professional community**: actuarial platforms model insurance products/liabilities with actuarial assumption machinery (mortality/lapse/curves as versioned first-class inputs) over policy/experience data; FMA models corporate/project financial statements and valuation for finance teams.
- Sample check: none of the five sampled FMA products carries insurance-liability semantics, actuarial assumption types, or policy/experience data structures. Quantrix's industry list includes financial services/insurance-adjacent verticals, but as deployment targets for the same generic modeling engine, not as actuarial object structures.
- Conclusion: boundary holds; the two Types are siblings under "build quantitative financial models" with different modeled objects. Gradient acknowledged (both project future financial outcomes), but no wall-crossing product observed.

### vs Financial Planning & Analysis Platform (§08, unprocessed sibling) — new flag

- Market vocabulary straddles: Synario markets itself as "FP&A solutions"; Jirav as an FP&A solution; the budgeting-forecasting research already flagged the FP&A umbrella problem ("same products sold under both names").
- Proposed seam for joint review when financial-planning-analysis-platform is processed: FMA holds the **model-artifact-centered** core (build/maintain/explore a financial model); "FP&A platform" is likely the umbrella category framing (planning process + analysis + reporting) that overlaps budgeting-forecasting-platform. FMA products market into FP&A vocabulary but their defining structure is the model, not the planning process.

### vs other neighbors

- **Cash-flow forecasting tools** (unprocessed leaves): short-term, bank-data-driven cash visibility is a slice of model output; FMA's center is the full statement model over strategic horizons. Not deeply sampled; held as adjacent.
- **BI / Dashboard Platform**: reads governed actuals and presents; FMA writes future projections through user-defined logic. FMA dashboards present the model, not the business's data warehouse.
- **Financial Consolidation Platform**: statutory consolidation of actuals vs FMA's combining of projections/entities inside a model (PlanGuru/Jirav "consolidations" are model-level, not statutory-close machinery).
- **Financial Close Management** (processed): backward-looking close execution vs forward-looking modeling — consistent with that leaf's recorded "FP&A (backward vs forward)" seam.
- **Financial Advisor Platform** (processed): advisor-side client-household planning vs corporate/project financial modeling; different user and object.
- **Treasury/Cash Management**: operational cash positioning vs modeled cash projection as part of statements.

## Uncertainties

- Lucanet xP&A (Causal) operational detail unreachable (JS-rendered KB; sub-pages return the index). Only TOC-level structure confirmed. No claims drawn beyond vocabulary.
- Quantrix deep help articles 404'd (two URL patterns tried); Quantrix evidence rests on the product page + help TOC. Scenario mechanics in Quantrix (scenario-as-category) is inferred from the category-linking description ("product, region, scenario or year") — plausible but not article-verified.
- PlanGuru "Budgeting & Forecasting Overview" article body was empty; PlanGuru structure taken from help TOC + product page.
- Finmark/Pry (startup-modeling pole) no longer independently documented; the startup tier is covered via Jirav's VC-funded positioning only.
- The investment-banking valuation-modeling practice (DCF/comps/LBO) was not sampled through a dedicated product; in practice it lives largely in spreadsheets plus market-data platforms. Valuation machinery appears in the sample only as PlanGuru's Business Valuation Tool (product-specific). The Type definition therefore does not claim valuation tooling as common.
- No numeric limits, durations, or defaults asserted anywhere in the final document; vendor counts (20+ methods, 10-year horizon, 5 years actuals, 50,000 users) kept as attributed claims in these notes only.

## Final Synthesis

A Financial Modeling Application is an application whose center is the **financial model**: a persistent, user-built structure that holds explicit assumptions, user-defined calculation logic, and time-period projections of an organization's financial results. The canonical build→use loop is: create the model (often from a template or pre-built statement structure) → bring in historical actuals → define assumptions and attach drivers/formulas to line items → let the engine propagate logic into projected statements/results → explore alternatives as scenarios within the same model → present via dashboards/reports → maintain by rolling periods forward and refreshing actuals.

The Type splits into two stable philosophies — **structural/free-form modeling** (user defines dimensions and logic; Quantrix pole) and **statement-anchored modeling** (pre-built integrated IS/BS/CF; Synario/PlanGuru/Jirav pole) — plus a deployment/tier spectrum from legacy desktop to cloud SaaS, SMB to institutional. Market consolidation is absorbing standalone modeling tools into suites (Causal→Lucanet, Finmark→BILL), but the modeling layer itself persists as the Type's substance.

Boundaries: against spreadsheets the seam is financial semantics; against budgeting/forecasting platforms the seam is the governed org-wide planning cycle (confirmed from both sides); against actuarial platforms the seam is the modeled object's semantics (corporate statements/valuation vs insurance liabilities — joint-review flag answered); vs the unprocessed FP&A-platform sibling, a new umbrella flag is raised.
