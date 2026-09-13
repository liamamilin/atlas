# Research Notes — Construction Cost Management

## Research Goal

Understand how real software manages **project cost during construction execution**: how the budget is set and changed, how committed cost (subcontracts, purchase orders) is tracked, how actual costs enter the system, how scope changes propagate into cost, and how cost-to-complete is forecast — and how this Type differs from Construction Estimating, Change Order Management, Progress Billing, Project Controls Platform, Construction Project Management, and job-cost accounting.

## Initial Boundary

Initial hypothesis: a Construction Cost Management application is the **project-level cost control system of record** for the delivery phase:

1. A **project budget baseline** organized by a cost breakdown structure.
2. **Commitments** (subcontracts, purchase orders) creating committed cost before invoices exist.
3. **Cost actuals** (vendor/subcontractor invoices, direct costs, labor) attributed to cost lines.
4. **Change management** that moves potential cost through approval into budget and commitment changes.
5. **Forecasting** (cost to complete / estimate at completion) and the recurring budget-vs-committed-vs-actual comparison report.

Nearest confusions:
- **Construction Estimating** — produces the pre-award price; cost management starts from the awarded budget.
- **Change Order Management** — the change workflow is one structure inside cost management.
- **Progress Billing** — the revenue side (billing the owner); cost management is the cost side.
- **Project Controls Platform** — cost + schedule + risk; this leaf is the cost pillar.
- **Accounting / job-cost software** — transaction/GL-centric; cost management is project-scoped and commitment-centric, connecting to the GL at a seam.

## Research Questions

1. What is the cost object model? (budget, cost codes, commitments, change objects, actuals, forecasts)
2. How does the budget work over time — original baseline, changes, revisions, locking, snapshots?
3. How are commitments represented (subcontracts, POs, schedules of values) and how does committed cost relate to budget and actuals?
4. How does the change chain work (event → quote → potential change → approved change → budget/commitment update)?
5. How do actual costs enter (vendor invoices, subcontractor invoices, direct costs, labor/payroll)?
6. How is cost-to-complete forecast and what metrics (variance, earned value) are exposed?
7. Who uses it (GC cost manager/PM, controller, owner rep, subcontractor collaborators) and what permissions matter?
8. Which capabilities are defining vs common vs optional vs vendor-specific?
9. Where are the boundaries vs Estimating, Change Order Management, Progress Billing, Project Controls, PM platforms, and accounting systems?

## Representative Products

| Product | Pole | Segment | Docs fetched |
|---|---|---|---|
| Procore | Construction-management platform heritage; cost tools inside a project platform; GC-centric, multi-party collaboration | mid-market to enterprise GCs and owners | Tier-1 support site: tool landing pages for Budget, Commitments, Change Events, Direct Costs + support root tool index (fetched 2026-09-07) |
| CMiC | Construction ERP heritage; single-database platform where job cost, subcontracts, change management, forecasting, billing share one system | enterprise GCs, heavy-civil | Tier-2: root page + Project Controls page (fetched 2026-09-07) |
| InEight | Project-controls heritage for capital projects; cost management (Control) as a modular app beside Contract, Change, Estimate, Billings | enterprise capital-project owners/contractors | Tier-2: InEight Control product page + platform nav + earned-value blog (fetched 2026-09-07) |
| Trimble Viewpoint Vista | Job-cost accounting / ERP heritage | mid-market contractors | Tier-2 product page only (fetched 2026-09-07); help docs unreachable |

Attempted, unreachable (2 failures each — abandoned per network rule): **Autodesk Construction Cloud** (help root 404, product page 403), **Sage Construction Management** (403), **Buildertrend** (403; also 403 in the sibling closeout run), **Buildxact** (403), **Trimble Vista help docs** (empty responses). Consequences: Autodesk's cost module is documented only structurally (from Procore-side integration references) with no claims; the residential/SMB pole is documented structurally only (Trimble's own "Trimble Financials — job costing accounting software for small contractors" naming); no precise numeric claims anywhere.

## Sources

- Procore Support — Budget tool landing page: https://support.procore.com/products/online/user-guide/project-level/budget (fetched 2026-09-07)
- Procore Support — Commitments tool landing page: https://support.procore.com/products/online/user-guide/project-level/commitments (fetched 2026-09-07)
- Procore Support — Change Events tool landing page: https://support.procore.com/products/online/user-guide/project-level/change-events (fetched 2026-09-07)
- Procore Support — Direct Costs tool landing page: https://support.procore.com/products/online/user-guide/project-level/direct-costs (fetched 2026-09-07)
- Procore Support root (project/company tool index incl. Client Contracts, Funding, Invoicing, Prime Contracts, Progress Billings, ERP Integrations): https://support.procore.com/ (fetched 2026-09-07)
- CMiC — home page: https://www.cmicglobal.com/ (fetched 2026-09-07)
- CMiC — Project Management / Project Controls page: https://www.cmicglobal.com/products/project-management/project-controls (fetched 2026-09-07)
- InEight — Control product page ("Construction Cost Management Software"): https://ineight.com/products/ineight-control/ (fetched 2026-09-07)
- InEight — platform product index + Earned Value article (CPI = EV/AC; BAC from estimation stage): https://ineight.com/products/cost (redirect), https://ineight.com/blog/what-is-a-cost-performance-index-cpi/ (fetched 2026-09-07)
- Trimble — Viewpoint Vista product page ("construction ERP software… job costing, financial management…"): https://viewpoint.com/products/vista (fetched 2026-09-07)
- Structural cross-references: Procore ERP-integration FAQ set (budget forecast export to CMiC / Sage 300 CRE / Vista / Spectrum), Procore integrations list (Sage 100 Contractor, Sage 300 CRE, Sage Intacct, QuickBooks, Viewpoint Vista/Spectrum, CMiC connectors), Trimble product index ("Trimble Financials — job costing accounting software for small contractors")

## Product A — Procore

### Key observations (Layer A unless noted)

**Cost tool family** (Tier-1 support root, project tools index): Budget, Change Events, Change Orders, Client Contracts, Commitments, Direct Costs, Funding, Invoicing, Prime Contracts, Progress Billings — plus company-level ERP Integrations. Two mirror-axes exist: the **cost axis** (Commitments + Invoicing) and the **revenue axis** (Prime Contracts/Funding/Client Contracts + Progress Billings), with Budget and Change Events shared between them. (A multi-party fact: tutorials exist per role — General Contractor, Owner, Specialty Contractor — and "Specialty Contractor as a Client" variants, i.e., the same financial structures are used from both sides of each contract.)

**Budget tool** (Tier-1): "The Budget tool allows you to build and manage a comprehensive budget throughout a project's lifecycle. By eliminating the need for double-entry of contract modifications and change order values into complex spreadsheets, you'll have greater insight into how seen and unforeseen changes impact the bottom line… evaluating and forecasting your project's completion costs."
- Budget = line items; import from spreadsheet or build; export Excel/PDF; line items per cost code (default cost codes exist); **WBS** with **budget codes** (cost code + cost type structure; "What is a budget code in Procore's WBS?" FAQ; sub-jobs, divisions); GST budget handling (regional tax variant).
- **Budget changes** as discrete managed records: create / edit / delete / **void** / **approve** budget changes; "About Budget Changes"; budget change detail per line item; **budget modifications** (another change type; used to "unlock a budget"); change history view; **lock a budget / unlock a budget**.
- **Budget views**: configurable column sets ("What source columns are available in Procore's budget views?"), standard budget view, **buyout savings** view, labor-productivity views, ERP-standard views. Views are a core reporting mechanism.
- **Budget snapshots**: create/edit snapshots; "Analyze Line Item Variance Between Budget Snapshots"; project status snapshots (custom statuses).
- **Forecast to Complete** feature; **Forecasting tab** (per role); "About the Procore Standard Forecast View"; **advanced forecasting curves** distributing projected cost-to-complete amounts; "Budget Forecasts, Projections, and Reports"; Budget Forecast Report FAQ.
- **Change Order Analysis** report; **Budget ROM** column ("rough order of magnitude" cost surfaced from change events on the budget); RFQ values can be added to budget views; non-commitment costs tracked on change events.
- **Timesheet hours** column; production quantities (budgeted units; installed quantities import) — unit/quantity layer exists.
- **ERP integrations**: budget sync with ERP; export budget modifications; export **cost forecast data** to CMiC / Sage 300 CRE / Viewpoint Vista / Spectrum; "How can I tell if a project's budget is synced with an integrated ERP system?" — budget is the project-side record that exchanges with accounting.
- **Permissions**: granular permissions for the Budget tool; permission templates; "CONFIGURABLE RED TEXT ON BUDGET LINE ITEMS" (over-budget signals configurable — user-visible variance emphasis).

**Commitments tool** (Tier-1): "The Commitments tool in Procore allows your teams to see the status and current value of all contracts and purchase orders… View and filter a detailed list of all the financial commitments (e.g., contracts, purchase order, etc.) on a project. Allow vendors to create and submit their invoices."
- Commitment = **subcontract** or **purchase order** (contract with a vendor); create/edit/delete; approve and sign (DocuSign integration); **inclusions/exclusions** on subcontracts.
- **Schedule of Values (SOV)** per commitment: add line items, import CSV; subcontractor SOV created by the subcontractor collaborator ("Invite a Subcontractor to Create a Subcontractor SOV"); link SOV items to change-event line items.
- **Commitment Change Orders (CCOs)**; configurable **1-tier or 2-tier** change order settings; PCO created from a change event then promoted to CCO; **financial markups** on CCOs.
- **Retainage**: enable retainage on a PO/subcontract; **sliding-scale retention rules** on subcontractor invoices; warning banner when retainage released.
- **Subcontractor invoicing**: Invoicing tool; invite to bill; invoice contacts submit invoices; bulk-edit invoice status; **payment schedules**; **Payments Issued tab** on a commitment (record payments out).
- **Privacy**: "Are commitments private by default?" FAQ; per-commitment privacy settings — financials are access-controlled between parties.
- **ERP sync**: export commitment/CCO to ERP for **accounting acceptance**; edit/delete constraints after sync ("request to reset a commitment synced with an integrated ERP system") — the commitment becomes a synchronized record with accounting-side custody.
- Custom numbering for financial objects; custom fields; approval **workflows** (custom workflow templates on contracts).

**Change Events tool** (Tier-1): "The Change Events tool allows you to track potential costs by better coordinating the entire change management process."
- "Create a change event based on a Request for Information (RFI) and add line items by cost code"; log all change events; clone; void; retrieve deleted.
- **RFQ loop**: "Create a Request for Quotes (RFQs) email based on a Change Event to your contractors and associate the RFQ with a commitment"; "Review RFQs responses from contractors and then Create a Prime Potential Change Order"; respond on behalf of collaborators; submit quotes as collaborator; "Latest Cost Setting for Change Order Requests".
- From one change event the system can generate: budget changes ("Create Budget Changes from a Change Event", beta), budget modification, **Commitment PCO → CCO**, **Prime Contract PCO → CO**, Funding CO, Client Contract CO, and even a new **purchase order or subcontract** ("Create a Purchase Order from a Change Event") — i.e., one change propagates to both cost and revenue structures and to commitments.
- **Field-initiated change orders** submitted by collaborators; multi-currency line items; Cost ROM and Revenue ROM columns (rough-order-of-magnitude estimates per line); financial markup lines with revenue ROM.

**Direct Costs tool** (Tier-1): "With the Direct Costs tool, avoid the price of being over budget and track the **non-contract costs** for a complete picture of the project expenses impacting your budget." Create/edit/delete direct costs; import CSV; per-role tutorials; permissions table (Read Only/Standard/Admin). Direct cost = cost with no commitment behind it (utility bills, owner-purchased items, etc.).

**Interpretation (Layer C)**: Procore's model is **budget-anchored, commitment-structured, change-event-driven**: everything financial ultimately lands on budget line items (cost code × cost type), commitments carry committed cost with SOVs and retainage, change events are the pre-approval cost funnel, and direct costs capture the residue. The ERP/accounting system remains the GL system of record; Procore exchanges commitments/CCOs/forecast with it.

## Product B — CMiC

### Key observations (Layer A for page content; positioning is Tier-2)

**ERP framing**: "Our construction ERP is built on a Single Database Platform"; suite = Financials (Construction Accounting, Project Controls, Equipment and Inventory, Opportunity Management, Payroll + HCM) + Project Management (Project Controls, Drawing and Construction Documents, Pre-qualification and Procurement, Quality and Safety). Subcontractor positioning: "Unify HCM, job costing and GL". Heavy-highway: "Accurately track units in place."

**Project Controls** (Tier-2): "CMiC's Project Controls solution allows users to effectively **monitor project budgets**, including time, expenses, suppliers, and costs… identify issues early in the process and course correct in a timely manner."
- **Financial Forecasting (GC Monitor)**: "Forecasting pulls **live data from Job Cost, Payroll, Subcontract and Change Management**, delivering real-time cost visibility without manual updates." "Posted change orders, subcontract costs, and labor expenses flow directly into projections." "PMs spot cost trends and take corrective action before problems surface in WIP or billing."
- **WIP (Work in Progress)**: "draws data directly from **Job Cost (actuals), Forecasting (projected costs and revenue), and Billing (Over/Under)**"; "WIP values update automatically when costs, billings, or changes are posted"; "visibility into margin and profit trends in real-time"; "Executives can review WIP knowing the numbers align perfectly with the GL and project forecasts."
- **Billing**: "pulls contract and cost data directly from Subcontract Management, Change Management, and Job Costing, capturing changes the moment they are posted"; "Approved change orders flow automatically into billing periods"; "WIP Over/Under ties directly to invoiced amounts."
- **Change Management**: "Change events feed directly into Forecasting, Subcontracts, Billing, and WIP, **instantly adjusting commitments, costs, and revenue projections** across the system"; "complete financial control over scope changes. Teams can view the cost and margin impact when changes are approved"; "strengthens audit trails."
- **Subcontract Management**: "Subcontract values, **commitments**, and payments stay aligned with project financials"; "Committed costs and forecasts update immediately when subcontracts are executed or revised."
- **Actuals**: "Helps Track Actual Costs Accurately: This includes all labor costs (including subcontractors), materials, and equipment expenses"; payroll "can track full burden costs (overhead and benefits) **against budget allocations**."

**Interpretation (Layer C)**: the ERP pole realizes the same canonical structures with **job cost as the actuals engine** and the GL native: budget/commitments/changes/forecast/billing are modules of one system rather than tools of a platform, and the commitment ("committed costs") is again the explicit middle layer between budget and actuals. Because accounting is native, this pole's boundary with accounting software is internal, not an integration seam.

## Product C — InEight

### Key observations (Layer A for page content; positioning is Tier-2)

**Product naming**: "InEight Control — Real-Time Cost Management for Capital Construction." "Built for detailed construction cost management, the software **creates construction budgets directly from estimates and forecasts remaining work** with real-world precision, using **actuals received from the field and your financial system**."

**Key features** (Tier-2):
- **Construction forecasting**: "accurate construction forecasts for remaining work based on industry-proven forecasting techniques. **Compare multiple forecast versions, evaluate 'what-if' scenarios**, and proactively adjust budgets."
- **Budgeting and control**: "Maintain **multiple versions of your construction budget** as it evolves based on trends and change status. **Automatically update budget baselines as change orders are approved**, ensuring accurate cost forecasts." FAQ: "current values can be easily compared against **original budget values**, making it easier to pinpoint where variances occur."
- **Earned value management**: "live earned value metrics to monitor progress and performance across all your projects"; blog (Layer A for content): CPI = EV/AC, EV = % complete × BAC, "the project's total Budget at Completion determined during the estimation stage."
- **Workflow and routing**: "acting on notifications and reviewing detailed audit logs. **Track all changes made, who made them and when they were made**."
- **Best-practices FAQ** (vendor-stated): "clearly identifying out-of-scope items, using an **approval process to route and approve changes**, and automatically incorporating those changes into the project's current budget."
- **Integration**: "designed to integrate with leading **ERP, financial, and other data systems**… eliminates manual entry, reduces errors, and creates one location for cost management across teams"; "integrating with your ERP" (Control one-liner).

**Platform context** (Tier-2 nav): Control (budget/forecast) sits beside **Contract** ("Centralize all contracts and stay on top of payments"), **Change** ("Consistently track issues and manage change orders"), **Estimate** ("Build accurate estimates"), **Billings**, **Plan & Progress** ("capturing real-time productivity information"), Schedule, Document/Model, Report & Explore. Solution pages include **Earned Value Management** and **Risk Management**. Company self-description: "a leader in **project controls software for capital construction**."

**Interpretation (Layer C)**: the project-controls pole treats cost management as the **budget/forecast discipline over earned progress**: the estimate seeds the budget; field actuals and financial actuals merge; change orders re-baseline the budget; versioned forecasts and EV metrics quantify the trajectory. Commitments/contracts and billings are sibling modules, confirming that this Type spans (or coordinates) them rather than being defined by any one.

## Product D — Trimble Viewpoint Vista

### Key observations (Layer A for page content; thin — help docs unreachable)

**Positioning** (Tier-2): "Vista™ construction ERP software. Collaborate in real time and scale your business with a **fully integrated ERP solution for job costing, financial management, HR, service management and jobsite tracking**." Trimble product index lists Vista as "**Job cost accounting software & ERP**" under Financial Management, alongside Spectrum ("Job cost accounting software & ERP") and **Trimble Financials ("Job costing accounting software for small contractors")**.

**Structural cross-evidence (Layer A, from Procore's integration docs)**: Procore maintains dedicated connectors and FAQ flows for exporting budget, cost forecast, commitments and CCOs to **Vista** and **Spectrum** — i.e., the ERP side receives commitments/forecast/actuals that the cost-management side originates, and job cost is the ERP-side realization of the cost ledger.

**Interpretation (Layer C)**: the accounting-heritage pole realizes cost management as **job cost accounting**: budget-per-job, committed cost, and actual cost posting by cost code inside the accounting system, with the platform pole connecting outward to it. Evidence is thinner here; claims about Vista's internal objects are NOT made.

## Cross-product Comparison

| Dimension | Procore | CMiC | InEight | Trimble Vista |
|---|---|---|---|---|
| Budget | Budget tool; line items by cost code × cost type (WBS budget codes); import/build; lock; snapshots; views | "monitor project budgets" incl. time/expenses/suppliers/costs; payroll burden "against budget allocations" | budgets "directly from estimates"; multiple versions; baselines auto-updated on CO approval; current vs original | job costing within ERP (no object detail documented) |
| Cost breakdown structure | cost codes + cost types + sub-jobs (WBS) | job cost structure (native accounting) | structure from estimate | cost codes (inferred structurally, not claimed) |
| Commitments | Commitments tool: subcontracts + POs, SOV, CCOs, retainage, payments issued | Subcontract Management: "committed costs… update immediately when subcontracts are executed or revised" | sibling module Contract ("centralize all contracts and stay on top of payments") | ERP-native (structural evidence via connector) |
| Change machinery | Change Events → RFQ → PCO → CO, propagating to budget + commitments + funding/prime (both axes) | Change Management: "change events feed directly into Forecasting, Subcontracts, Billing, and WIP" | Change module; "automatically update budget baselines as change orders are approved"; approval routing | not documented |
| Actuals | vendor/subcontractor invoices (Invoicing), Direct Costs for non-contract costs, timesheet hours | Job Cost = actuals; payroll burden, materials, equipment | "actuals received from the field and your financial system" | job cost postings |
| Forecast | Forecast to Complete; forecasting views; advanced forecasting curves; forecast export to ERP | GC Monitor forecasting pulling live from Job Cost/Subcontract/Change Management | versioned forecasts, what-if scenarios | not documented |
| Control report | budget views + Budget Forecast Report + Change Order Analysis | WIP (job cost + forecasting + billing over/under), GL-aligned | dashboards; EV metrics (CPI) | WIP/job reports (not documented) |
| Accounting seam | ERP integrations; commitment export "for accounting acceptance"; forecast export | GL is native (single database) | ERP integration; "one location for cost management" | ERP itself |
| Multi-party | GC / Owner / Specialty Contractor role variants; subcontractor billing portal; commitment privacy | GC, subcontractor, heavy-highway poles | owners and contractors on capital projects | contractor-internal |
| Evidence strength | Tier-1 (support docs) | Tier-2 (vendor pages, but specific and structural) | Tier-2 (vendor pages) | Tier-2 thin |

**Cross-product commonality (Layer B):**

1. **Budget baseline vs recorded cost** — every product centers on a per-project cost plan compared against what has been committed and incurred, at cost-line granularity (Procore budget line items; CMiC budget monitoring via job cost; InEight current-vs-original budget; Vista job costing).
2. **Committed cost as an explicit layer** — all sampled products with reachable documentation treat contracts/POs ("commitments") as a first-class cost state between budget and actuals (Procore Commitments; CMiC "committed costs"; InEight Contract; Vista job cost committed columns exist per heritage — only structurally evidenced, so kept Layer B with qualification).
3. **Change propagation** — a scope change is captured before it is priced/approved (change event/issue), moved through pricing (RFQ/quotes) and approval, and then **updates budget and commitments (and billing)** mechanically (all three deep-documented products).
4. **Forecast to complete** — all three deep-documented products maintain a forward-looking projected cost (Procore Forecast to Complete; CMiC Forecasting; InEight forecast versions/what-if); EV indices appear at the capital-projects pole (InEight).
5. **Accounting boundary** — cost management keeps project-side cost control distinct from the GL, either by integration (Procore, InEight) or by being one system with accounting (CMiC, Vista). The project-side record always remains cost-organized, not journal-organized.
6. **Multi-role, multi-party access** — financials are shared across GC, owner, and subcontractor roles with privacy controls (Procore explicit; CMiC/InEight poles imply; qualified Layer B).
7. **Approval governance** — changes, budgets, contracts and invoices route through approval workflows with audit trails (Procore workflows/audit; CMiC "strengthens audit trails"; InEight workflow/routing + audit logs).

## Canonical Model (Layer C synthesis)

```text
Project (construction delivery engagement)
└── Cost budget (baseline plan, organized by cost lines of the work)
    ├── recorded as: original budget → discrete budget changes → current/revised budget
    └── each cost line compares against:
        ├── Committed cost (contracts / purchase orders with vendors, via schedules of values)
        │   └── adjusted by commitment change orders; carry retainage; drive vendor invoices
        ├── Incurred cost (vendor/subcontractor invoices, direct costs, labor/materials/equipment)
        └── Forecast (projected cost to complete → estimate at completion)
Change chain: change event/issue → pricing (RFQ/quotes) → potential change → approved change
              → updates budget lines + commitment lines (+ revenue structures on the funding side)
Control surface: budget vs committed vs actual vs forecast per cost line (cost report / dashboard)
```

## L0 — Defining Invariant (minimal)

1. **A project cost budget as the managed baseline** — planned cost organized into cost lines for the project's work. Without it there is no "management", only expense recording.
2. **Recorded cost entries attributed to those cost lines** — committed and/or incurred costs, however captured.
3. **The budget-vs-recorded-cost comparison (variance) as the recurring control view** — the cost report. Without comparison there is no control loop.

Historical check: a spreadsheet-era or ledger-era cost report (estimated vs committed vs actual per cost code) satisfies all three; pre-software cost-engineering practice satisfies it. Modern-only machinery (cloud collaboration, approval workflows, EV indices, budget views, portals) is deliberately excluded.

## L1 — Common Mature Structure

- **Cost breakdown structure management** — cost codes/dimensions (division/area/type) with libraries and defaults (Procore cost codes/cost types; CMiC job cost structure; InEight estimate-derived structure).
- **Commitments** — subcontracts and purchase orders with schedules of values; commitment change orders; committed-cost tracking as the middle layer; retainage on payments (3/3 deep products + structural for Vista).
- **Change machinery** — event/issue capture → quote/pricing → potential change → approved change → automatic budget + commitment (± revenue) update; approval routing; audit trail.
- **Forecast to complete** — cost-to-complete / EAC maintenance; version/scenario comparison at mature implementations; periodic re-forecast.
- **Actuals capture** — subcontractor/vendor invoicing, direct (non-contract) costs, labor/time costs; import from other systems.
- **Payment machinery on the cost side** — payments issued/recorded against commitments; retention rules.
- **Budget governance** — lockable budgets, discrete change records (approve/void), snapshots/versions, original-vs-current comparison.
- **Accounting integration seam** — commitments/CCOs/forecast/actuals exchanged with the GL/ERP (or the GL is native in the ERP pole).
- **Reporting** — cost reports/dashboards (WIP, change order analysis, variance), exportable.
- **Multi-role permissions & privacy** — role-based access; financial privacy between contracting parties; collaborator (subcontractor) participation in billing and quotes.

## L2 — Variant / Optional Structure

- **Revenue-side mirrors** — funding/prime/client contracts and progress billings toward the owner (present in GC-side suites; separate Type in this directory).
- **Earned-value metrics** (CPI/SPI), productivity and production-quantity tracking, man-hour views (capital-projects and heavy-civil emphasis).
- **Unit/quantity layer** — budgeted vs installed quantities (heavy-civil "units in place").
- **Regional tax** on budgets (GST); multi-currency line items.
- **Residential/SMB simplified realization** — estimate-to-actual job tracking without heavy commitment machinery (structurally evidenced via small-contractor job-cost positioning; not directly documented).
- **Field-initiated changes** from mobile; single-database ERP realization vs platform+integration realization.
- **Portfolio/program roll-up** across projects (InEight portfolio EV; Procore portfolio financials as separate product family).

## L3 — Vendor-specific Structure (research notes only)

- Procore: budget views engine (configurable source columns), Budget ROM / RFQ / non-commitment-cost source columns, buyout savings view, 1- vs 2-tier change order settings, "specialty contractor as client" role variants, advanced forecasting curves, labor productivity budget views, ERP "accounting acceptance" states, granular-permission matrix, red-text over-budget signaling, project status snapshots.
- CMiC: GC Monitor, WIP Over/Under framing, single-database marketing, "units in place" heavy-highway framing.
- InEight: Control data library, forecast version compare, InEight NOW per-user buying, knowledge library/U training.
- Trimble: Vista/Spectrum/Trimble Financials product ladder by contractor size.

## Boundary Findings

- **vs Construction Estimating**: estimating produces the pre-award price prediction; cost management takes over at award/baseline. Handoff is explicit at InEight ("budgets directly from estimates", BAC "determined during the estimation stage") and Procore (separate Estimating tool; budget imported). **Remove the budget-vs-actual control loop and keep only pricing before award → you have Construction Estimating.**
- **vs Change Order Management**: the change workflow is one mechanism inside cost management. Cost management owns the whole budget/commitment/actual/forecast loop; change objects are inputs to it. A product that only manages the change document/approval workflow (without the cost baseline) is Change Order Management. (Directory has separate leaves — valid split; joint-review note recorded.)
- **vs Progress Billing**: billing the owner is the revenue mirror (Procore Progress Billings / Funding; CMiC Billing; InEight Billings). Cost management's payment machinery runs the opposite direction (vendor/subcontractor payables). Same SOV/retainage vocabulary, opposite flow. **Keep only the owner-billing flow → Progress Billing.**
- **vs Project Controls Platform**: project controls = cost + schedule (+ risk + documents) (CMiC "cost, schedule, and risk management"; InEight platform). This leaf is the cost pillar alone.
- **vs Construction Project Management**: PM platforms span schedule, RFIs, submittals, field tools; cost tools are one tool family inside them (Procore's structure shows exactly this). Cost management is distinguishable by its object set (budget/commitments/forecast), not by UI.
- **vs Accounting Software / General Ledger / job-cost accounting**: accounting is journal/GL-centric and enterprise-scoped; cost management is project-scoped, commitment-centric, forecast-bearing. The job-cost ledger is the accounting-side realization of the actuals layer; modern cost management adds commitments+changes+forecast+multi-party collaboration and connects to the GL at a seam (or embeds it, ERP pole).
- **"去掉什么就变成另一个 Type" 判据**: remove the budget baseline → cost reporting/accounting view; remove commitments+forecast and keep only time-card/invoice capture → expense tracking; remove change control → static budget vs actual (job cost); remove the project scope → generic budgeting software.

## Uncertainties

- **Autodesk Construction Cloud Cost Management** could not be reached (404/403); its presence in this market is known structurally (Procore↔Autodesk integration references) but **no product-specific claims** are made.
- **SMB/residential pole** (Buildertrend/Buildxact class) unreachable; its characterization (lighter commitment machinery, estimate-to-actual focus) rests on Trimble's own small-contractor positioning plus general market structure — kept qualified.
- **Trimble Vista internals** undocumented (help unreachable); the ERP pole is evidenced through its product page and the Procore connector flows only.
- Whether **owner-side funding/billing** belongs inside this Type or is fully covered by Progress Billing / Construction Contract Administration leaves: sampled suites include the revenue mirror, but the canonical document treats it as an adjacent revenue axis, consistent with the directory's separate leaves. Joint review with change-order-management and progress-billing passes may refine this.
- Retainage law/regional terms (retention vs retainage) vary by jurisdiction; no legal claims made.

## Final Synthesis

Construction Cost Management is the **project-scoped cost control system of record for construction delivery**: it holds the project's cost budget as a managed baseline (original → changed → current, per cost line of a cost breakdown structure), tracks **committed cost** (subcontracts/purchase orders with schedules of values) between the plan and the invoices, records **incurred cost** (vendor/subcontractor invoices, direct costs, labor), pushes every scope change through an event→pricing→approval chain that mechanically updates budget and commitments, and maintains a **forecast of the cost to complete**, all surfaced through the recurring budget-vs-committed-vs-actual-vs-forecast cost report under role-based, party-privacy-controlled access, exchanging (or embedding) the accounting/GL side at a defined seam.
