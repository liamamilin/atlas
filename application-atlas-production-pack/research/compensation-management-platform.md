# Research Notes — Compensation Management Platform

Research date: **2026-09-07**

## Research Goal

Understand, from real products, what a Compensation Management Platform is and how it works: its core objects, the compensation cycle workflow, the roles involved, the rules that govern pay decisions, and the boundary against Payroll, HRIS, Performance Management, and Sales Compensation Management.

## Initial Boundary

Working hypothesis at start:

- Core use: planning and administering employee pay — salary structures, merit/bonus cycles, budgets, market positioning, pay equity — as an HR-side decisioning layer.
- Users: compensation/HR teams, managers, finance; employees as recipients of statements.
- Nearest types: Payroll System (executes payment), HRIS (records), Performance Management Platform (feeds ratings in), Sales Compensation Management (directory §07; commission-driven), Benefits Administration (non-cash).
- Unknowns: exact object model of cycles/worksheets/plans; how deep budget machinery goes; whether pay structures (grades/bands) are verifiable; segment spread (SMB vs enterprise).

Note: the directory contains BOTH "Sales Compensation Management" (§07) and "Compensation Management Platform" (§09). This pass documents the §09 leaf (organization-wide pay planning/administration); the §07 leaf (sales-side commission/incentive calculation) must remain distinct — see Boundary Findings.

## Research Questions

1. What objects make up the system? (cycle, plan, worksheet, budget pool, award, statement)
2. What is a compensation cycle and how does it flow end-to-end?
3. What component types of pay are administered (base, bonus, stock/equity, incentives)?
4. How do budgets work (allocation to managers, top-down vs bottom-up, validation)?
5. What guidance constrains manager decisions (guidelines, matrices, models, guardrails)?
6. What roles exist (line manager, comp manager, comp administrator, HR, finance, employee)?
7. What happens after approval (write-back to HR records, payroll handoff, letters/statements)?
8. How do market benchmarking and pay-equity analysis enter the flow?
9. What off-cycle work exists (promotions, spot bonuses, case-by-case salary changes)?
10. Where are the boundaries vs payroll / performance / HRIS / sales comp / benefits?
11. What variants exist by vendor philosophy, customer tier, geography/regulation?

## Representative Products

Selected for market representation + documentation accessibility + different philosophies:

| Product | Pole | Why selected |
|---|---|---|
| Workday Compensation | Enterprise HCM suite module; "AI guardrails + wage intelligence" philosophy | Market-leading suite; dedicated product page reachable |
| Oracle Compensation (Fusion Cloud HCM) | Enterprise HCM suite module; task/plan configuration philosophy | Only sample with full Tier-1 operational documentation (Using Compensation user guide) |
| SAP SuccessFactors Compensation | Enterprise HCM suite module; global planning philosophy | Third major suite; dedicated product page reachable |
| beqom | Standalone global comp/incentive specialist (overlay on any HRIS) | Different packaging philosophy; strongest incentive-component depth; EU/regulation focus |

Dropped during research: Payscale (URLs 404 ×3), Paylocity (JS-walled SPA ×2), HiBob (404), Salary.com (404), Paycor (not attempted after pattern). Consequence: the sample skews enterprise; SMB/mid-market claims are NOT asserted in the final document.

## Sources

Fetched successfully (2026-09-07):

- Workday — Compensation Management Software product page: https://www.workday.com/en-us/products/human-capital-management/human-resource-management/compensation.html (Tier 2)
- Workday — Human Resource Management (Core HCM) product page (compensation module positioning, Pay Transparency, Total Rewards Agent): https://www.workday.com/en-us/products/human-capital-management/human-resource-management.html (Tier 2)
- Oracle — Using Compensation (user guide): Overview of Workforce Compensation Management; Overview of Workforce Compensation Plans; Overview of Base Pay Management. Reached via https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/saas/human-resources&id=FACMCoverview-of-workforce-compensation-management (and sibling IDs). Tier 1 — operational documentation.
- Oracle — Talent Management product page (Compensation module marketing + FAQ + datasheet link): https://www.oracle.com/human-capital-management/talent-management/ (Tier 2)
- Oracle — Human Resources documentation hub ("Use Compensation" task listing): https://docs.oracle.com/en/cloud/saas/human-resources/use.html (Tier 1 navigation)
- SAP — SAP SuccessFactors Compensation product page: https://www.sap.com/products/hcm/compensation-management.html (Tier 2)
- SAP — Talent Management page (Compensation capability cards): https://www.sap.com/products/hcm/talent-management.html (Tier 2)
- beqom — PaySuite root: https://www.beqom.com/ (Tier 2)
- beqom — Compensation Management product page incl. FAQ: https://www.beqom.com/products/compensation-management (Tier 2; FAQ prose is generic platform-level description)

Failed / inaccessible (do not compensate from memory):

- SAP Help Portal (help.sap.com/docs/SAP_SUCCESSFACTORS_COMPENSATION) — JS shell only; no Tier-1 SuccessFactors docs.
- Workday Community/docs (community.workday.com) — login-gated; product-page guesses 404.
- Payscale, Paylocity, HiBob, Salary.com — unreachable (404 / JS wall).
- Bing / DuckDuckGo search — region-poisoned results / timeouts; effectively unusable.

## Product Observations

### Workday Compensation (evidence layer A unless noted)

From the Compensation product page (Tier 2):

- Named key capabilities: pay equity dashboards; compensation analysis tools; total rewards statements; compensation review; total compensation basis; executive compensation.
- "Compensation review" with in-flight cost modeling: "View the financial impact of changes before you commit to ensure your plans fit your budget."
- Market intelligence: "Embed real-time market benchmarks via Compa and Workday Wage Intelligence to accurately model promotion costs" (vendor-specific data integrations).
- Contextual skills surfaced "alongside performance" for manager decisions.
- "Automated mass actions … automating high-volume changes and eligibility rules, eliminating manual spreadsheet updates."
- "Proactive pay equity. Put equity at the heart of the merit cycle with 'pay vs. peers' insights that make it easy for managers to spot and fix gaps."
- "Intelligent guardrails. Equip managers with real-time guardrails and Workday AI to flag pay anomalies and prevent bias before awards are finalized."
- Dashboard described as "organization summary with overall budget and spend"; "pre-validated against live budgets".
- Language: "merit cycle", "Comp cycle chaos", "complex cycles"; Workday Agents "monitor minimum wage updates".
- From the Core HCM page: Compensation is a named product under Human Resource Management, grouped under "Total Rewards"; a separate "Pay Transparency" product exists; a "Total Rewards Agent" exists. (50% "increase in compensation planning speed" is a vendor marketing claim — not used.)

### Oracle Compensation (evidence layer A, Tier 1 for guide pages)

From "Using Compensation" — Overview of Workforce Compensation Management (Tier 1):

- "As a line manager, you can allocate compensation, such as merit increases or stock grants, to groups of people on a **focal, anniversary, or periodic basis**." → cycle-basis taxonomy directly documented.
- "You can also promote people, rate their performance, and communicate compensation changes."
- "You can use models to automatically calculate compensation, and even allocate it."
- "You can analyze proposed changes for equity among peer groups and by manager. You can also analyze how these proposals align with the market … and with organizational compensation strategies for performance."
- Roles: line manager (allocates), compensation manager (oversight, override, proxy), compensation administrator ("process and transfer approved workforce compensation to people's HR records").
- Surfaces: My Team > Workforce Compensation; My Client Groups > Compensation.

From "Overview of Workforce Compensation Plans" (Tier 1):

- "Use workforce compensation plans to **allocate budgets to managers and compensation to groups of people during a compensation cycle**. The plans are highly configurable, so the specific tasks and information you see depend on the plan setup and your role."
- Example plan configuration with budgeting: tasks include **Manage Budgets**, compensation tasks **Adjust Salary, Allocate Bonus, Allocate Stock**, communications task **Communications**, approvals task **Approve**. Another configuration without budgeting: **Allocate Award**, **Statement**, **Approvals**.
- Role-dependent UI: "Adjust Budgets button" appears for compensation administrators, not line managers.

From "Overview of Base Pay Management" (Tier 1):

- "Base pay is a person's fixed salary amount. You view and adjust this amount or any component amounts or percentages over the time the person works in your organization." → salary history over tenure.
- Salary adjusted "as part of HR actions, such as when you hire, transfer, or promote someone" → off-cycle adjustments via HR events.
- Line manager adjusts via "Change Salary quick action"; comp manager/HR specialist via My Client Groups > Compensation.
- **Salary basis** concept: currency, frequency, annualization factor; optional salary components (e.g., merit, location) itemize adjustments; "the salary amount you enter is held by the payroll element associated with the salary basis. The salary basis passes that amount to payroll for processing." → the comp→payroll handoff, documented.
- Currency: values appear in the employee's local currency; viewable in preferred currency via conversion rates.

From the Talent Management page (Tier 2):

- "Support pay equity and compliance year-round with AI-powered compensation reviews"; "Manage global and local compensation requirements while aligning increases with priorities such as transparency, performance, and compliance."
- "AI Assist to generate customized compensation plan instructions"; "AI agents that access team pay, bonuses, equity, and history"; "Compensation Advisor agent" for total compensation data.
- FAQ: compensation uses "performance ratings, goals, and feedback … skills, potential, and succession data"; HR can "model different compensation scenarios, compare outcomes, and analyze compensation across teams and various demographics to identify pay gaps."

### SAP SuccessFactors Compensation (evidence layer A, Tier 2 only)

From the product page:

- Positioning: "Build and manage strategic employee compensation programs to optimize individual and business performance."
- Three pillars: "Make informed decisions about employee pay"; "Automate and simplify employee compensation planning"; "Centralize employee compensation management."
- Hero image caption: "Employee salary equity and incentive plan in SAP SuccessFactors Compensation."
- From the Talent Management page, Compensation capability cards: "Intelligent compensation modeling — Optimize your compensation programs by aligning workforce pay with HR and business objectives"; "Global compensation planning — Streamline compensation planning across your organization and tailor it to meet local market needs with a flexible solution"; "Timely rewards and recognition — Motivate your employees year round with real-time recognition."
- Performance module FAQ links reviews to "better development and compensation decisions."
- Limitation: no operational documentation accessible (help.sap.com is a JS shell). Do not state SuccessFactors-specific operational detail.

### beqom PaySuite — Compensation Management (evidence layer A, Tier 2; FAQ prose generic)

Component coverage ("One platform. Every compensation component."):

- Salary & Merit: "Run merit cycles, periodic reviews, and market adjustments with built-in guidelines and seamless approval workflows."
- Short Term Incentives: "complex, multi-KPI bonus structures and dynamic payout curves."
- Spot Bonus: "discretionary spot bonuses with collaborative workflows and real-time award notifications" (manager-initiated, immediate).
- Executive Comp Management: "configurable workflows, strict governance, and privacy controls."
- Sales Incentive Management: "Deploy sales bonuses faster … clear incentive statements" (sales-planning flavor — boundary-relevant).
- Long Term Incentives: "cash-based LTI grants and allocations"; FAQ: "tracking grants, vesting schedules, cliff dates, and performance conditions."

Cycle machinery:

- "Compensation Rounds — Streamline complex compensation cycles into a single, guided workspace—enabling teams to securely configure, validate, and repeat error-free rounds."
- "Top-down Budgeting — Model and cascade your comp capital from the top down before your cycles even begin … prevent costly budget overruns and policy deviations."
- "Configurable Workflows — dynamic, automated routing and approval tracking. Control who can view, edit, or sign off at every stage."
- "Audit & Governance Trails — instant, platform-wide history of every decision."
- Platform positioning: "System of Record: The ultimate single source of truth for all pay decisions"; integrates with HRIS/payroll/CRM/data-warehouse (Workday, Oracle, SAP, UKG, HiBob logos); partners with Mercer and WTW for market data; "Pay Intelligence" product.
- FAQ (generic platform-level claims, corroborating cross-product structure): "Compensation management software routes manager proposals through HR validation, budgeting controls, and final approvals — all in a streamlined, audit-ready workflow"; "A compensation platform manages on- and off-cycle reviews with local compliance, currency conversions, and budget controls"; "Total comp statements give employees a clear view of their total rewards — base salary, bonuses, equity, and benefits. A compensation platform generates and distributes personalized statements automatically"; "Spreadsheets break at scale."
- Global scale: "all global currencies, 30 languages, 100K+ concurrent users" (vendor claim); EU Pay Transparency Directive compliance is a major theme (PayAnalytics by beqom; PUMA case).

## Cross-product Comparison

| Structure / capability | Workday | Oracle | SuccessFactors | beqom | Evidence | Tier |
|---|---|---|---|---|---|---|
| Employee pay records as managed population | ✓ (pay data united) | ✓ (salary records, HR records) | ✓ (centralize comp mgmt) | ✓ (HRIS sync) | B (4/4) | L1 |
| Compensation cycle/review event | ✓ "merit cycle", "comp review" | ✓ "compensation cycle"; focal/anniversary/periodic | ✓ "compensation planning" | ✓ "Compensation Rounds", "merit cycles" | B (4/4) | L1 |
| Component types: base salary | ✓ | ✓ (base pay mgmt) | ✓ | ✓ | B | L1 |
| Component types: bonus/variable | ✓ (bonuses in agent description) | ✓ (Allocate Bonus) | ✓ (incentive plan) | ✓ (STI, spot bonus) | B (4/4) | L1 |
| Component types: stock/equity awards | ✓ (exec comp, total rewards) | ✓ (stock grants, Allocate Stock) | (image only) | ✓ (LTI, vesting) | B (3/4 explicit) | L1 |
| Budget allocation to managers + validation | ✓ (live budgets, cost modeling) | ✓ (Manage Budgets, budget→managers) | (implied "budget needs") | ✓ (top-down cascade) | B (3–4/4) | L1 |
| Guidelines/models constraining awards | ✓ (guardrails, AI) | ✓ (models auto-calculate; strategy alignment) | ✓ (intelligent modeling) | ✓ (built-in guidelines, payout curves) | B (4/4) | L1 |
| Approval routing | ✓ ("before awards are finalized") | ✓ (Approve/Approvals tasks) | ✓ (implied) | ✓ (routing, sign-off, HR validation) | B (4/4) | L1 |
| Communication of decisions (letters/statements) | ✓ (Total Rewards statements) | ✓ (Communications, Statement tasks) | ✓ ("timely rewards and recognition") | ✓ (statements generated/distributed; pay-communication guide) | B (4/4) | L1 |
| Transfer finalized pay to HR records/payroll | ✓ (suite-native) | ✓✓ (admin "process and transfer … to people's HR records"; salary basis passes to payroll) | (suite-native, implied) | ✓ (HRIS/payroll integration) | B (4/4) | L1 |
| Market benchmarking/market reference data | ✓ (Compa, Wage Intelligence) | ✓ ("align with the market") | ✓ ("local market needs") | ✓ (Mercer/WTW, Pay Intelligence) | B (4/4) | L1 |
| Pay-equity analysis | ✓ (dashboards, pay-vs-peers) | ✓ (equity among peer groups; demographic gap analysis) | ✓ (salary equity) | ✓ (pay gaps, remediation, EU PTD) | B (4/4) | L1 |
| Scenario/cost modeling | ✓ (in-flight cost modeling) | ✓ (model workforce budgets; scenario modeling) | ✓ (intelligent comp modeling) | ✓ (dynamic payout curves, budget modeling) | B (4/4) | L1 |
| Off-cycle adjustments (hire/promotion/spot) | (mass actions/eligibility) | ✓ (HR actions: hire/transfer/promote) | (recognition) | ✓ (spot bonus, on/off-cycle) | B (2–3/4) | L1 |
| Salary history over tenure | ✓ (implied) | ✓✓ ("over the time the person works") | (implied) | ✓ (audit history) | B (2–3/4) | L1 |
| Total-rewards statements to employees | ✓✓ | ✓ (Statement task; TC statements) | ✓ | ✓✓ | B (4/4) | L1 |
| Executive comp with privacy governance | ✓ (executive compensation) | (not surfaced) | (not surfaced) | ✓ (exec comp mgmt, privacy) | 2/4 | L2 |
| Sales incentive planning module | – | – | – | ✓ | 1/4 product-specific | L2→drift seam |
| Equity/LTI administration (vesting, cliffs) | (total rewards view) | (stock grants) | (not surfaced) | ✓✓ (grants, vesting, cliff dates) | 1/4 detailed | L2 |
| AI assistance in the cycle | ✓✓ (agents, guardrails) | ✓✓ (AI Assist, Compensation Advisor) | ✓ (modeling cards) | ✓✓ (Intentional AI) | B (4/4) | L1 current-market, NOT definitional (historical check) |
| Multi-currency/localization | ✓ (suite claims) | ✓✓ (salary basis currency; local currency; conversion) | ✓ ("local market needs") | ✓✓ (all currencies, 30 languages) | B (4/4) | L1/L2 |
| Pay-range/grade/compa-ratio machinery | not verified | not verified (salary basis ≠ ranges) | not verified | not verified | 0/4 direct | NOT ASSERTED |
| Eligibility rules for cycle inclusion | ✓ ("eligibility rules") | ✓ (plan setup decides population) | implied | implied | B (2/4 explicit) | L1 (qualified wording) |
| Audit trail of decisions | implied | implied (processed records) | implied | ✓✓ (explicit feature) | 1/4 explicit | L1 (qualified wording) |

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Employee pay population** — identified employee records carrying current pay, drawn from the organization's HR system of record (the platform is a decisioning layer over people it does not register itself).
2. **Organization-defined compensation components** — the pay programs being administered (base salary, bonus, stock/equity, other incentive types), configurable as to what can be awarded and under what rules.
3. **The award proposal** — authorized users (normally line managers) propose specific pay awards for specific employees, either inside a governed compensation cycle or as case-by-case adjustments.
4. **Governed determination → pay of record** — proposals are constrained by budgets/guidelines, pass through approval, and finalized awards update the employee's pay of record, feeding HR/payroll.

Remove #1 → generic budgeting/finance planning. Remove #2 → generic approval workflow. Remove #3 → payroll (execution without decisioning). Remove #4 → survey/statistics tool or a performance system. All four are required.

Historical check (§24): pre-digital practice fits — a salary roster (1), a salary schedule/bonus plan (2), a manager's merit recommendation form (3), department-head approval posted to the payroll ledger (4). Spreadsheet-era merit cycles ( emailed worksheets + consolidation spreadsheets) also fit. Modern add-ons (AI, dashboards, real-time market feeds, multi-currency, statements) are NOT in L0. ✓ passes.

### L1 — Common Mature Structure

- Compensation cycles (focal/anniversary/periodic bases; merit cycles) as the dominant working rhythm
- Budget machinery: pools allocated to managers/org units, usage tracking, top-down and bottom-up reconciliation, live validation of proposals against budget
- Guidance layer: guideline ranges/percentages, merit matrices keyed to performance ratings, models that pre-calculate or recommend awards, guardrails/anomaly flags
- Market reference data: survey/composite benchmarks positioned against employee pay (via native data or data-vendor integrations)
- Pay-equity analysis across the cycle (peer comparisons, demographic gap views, remediation tracking)
- Approval routing with role-dependent powers (override, proxy, adjust budgets)
- Communication artifacts: award letters/communications, total compensation/total rewards statements
- Scenario/cost modeling ("what does this plan cost")
- Off-cycle adjustments attached to HR events (hire, transfer, promotion) and discretionary spot awards
- Salary history over the employee's tenure; effective-dated changes
- Write-back/handoff to HRIS and payroll (native in suites; integration in standalone products)
- Multi-currency with local-currency display and conversion
- Performance-data linkage (ratings feed guidelines) — as input, not evaluation
- Cycle configuration: which components/budgets/tasks are included, and who is eligible (qualified)
- AI assistance (recommendations, drafting, anomaly detection) — strong current-market commonality, not definitional

### L2 — Variant / Optional

- Packaging: suite module (Workday/Oracle/SuccessFactors) vs standalone specialist overlaying any HRIS (beqom) vs data-led planning tools
- Component-scope poles: base-pay/merit-centric vs total-comp (STI+LTI+equity) vs incentive-heavy
- Equity/LTI administration depth (grants, vesting schedules, cliff dates)
- Executive compensation module with strict privacy/governance
- Sales incentive planning (drift seam toward Sales Compensation Management)
- Regulatory postures: EU Pay Transparency Directive; US pay-transparency tooling (some products ship dedicated pay-gap/transparency products)
- Regional/multi-entity scale (global enterprises: many countries, currencies, works agreements)
- Cycle cadence culture: annual focal vs anniversary vs always-on
- Analytics depth: dashboards, demographic analysis, reports for regulators/leadership

### L3 — Vendor-specific (research notes only)

- Workday: Compa + Workday Wage Intelligence real-time benchmarks; Pay Transparency Analyzer; Total Rewards Agent; "50% faster compensation planning" claim.
- Oracle: workforce compensation plan task model (Manage Budgets / Adjust Salary / Allocate Bonus / Allocate Stock / Communications / Approve); salary basis → payroll element plumbing; Compensation Advisor agent; focal/anniversary/periodic terminology; proxy/override powers of comp managers.
- SAP SuccessFactors: Joule assistants; "Intelligent compensation modeling" card labels; no operational docs accessible.
- beqom: Intentional AI (explainable/collaborative/controllable); Calculation Workspace (no-code comp logic); Business Matrices; PayAnalytics (equity); 100K+ concurrent users, 30 languages; Mercer/WTW partnership.

## Vendor-specific Findings

See L3. The most consequential: Oracle's plan-configuration model shows tasks are **assembled per plan** (a plan may have budgeting or not; different compensation tasks; communications on/off) — this is a strong structural insight (cycle contents are configurable) but the specific task names are Oracle's. Workday's market-data integrations and beqom's calculation workspace are implementation choices, not type structure.

## Boundary Findings

| Neighbor | Distinction | "Remove X" criterion |
|---|---|---|
| Payroll System | Payroll computes and delivers payments from pay records; comp platform *decides and records* the pay. Oracle Tier-1: salary basis "passes that amount to payroll for processing" — the seam is the handoff. | Remove determination/approval and keep computation/delivery → Payroll. Remove payment execution and keep award determination → comp platform. |
| HRIS / Core HR | HRIS is the system of record for job/pay data; comp platform runs the *decision cycle* over that data and writes results back. Suites blur the seam because the comp module is inside the HRIS. | Remove the cycle/decisioning loop (keep records only) → HRIS feature. |
| Performance Management Platform | Evaluates people (goals, feedback, ratings); comp consumes ratings as guideline input (Oracle: "analyze how proposals align with … compensation strategies for performance"). Oracle's comp module can also *rate* performance — suite overlap, not type identity. | Remove pay awarding (keep evaluation) → Performance Management. |
| Sales Compensation Management (§07 leaf) | Sales comp = transaction/quota-driven commission and incentive *calculation* for sales populations. Comp platform = manager-proposed, budget-governed awards organization-wide. beqom ships both under one suite — real adjacency. | Remove commission/calculation-from-transactions (keep proposal/approval of pay) → comp platform; vice versa → sales comp. Flag for joint review when §07 leaf is processed. |
| Benefits Administration Platform | Administers non-cash programs via enrollment/eligibility events; no pay-award determination. | Replace pay awards with plan enrollments → Benefits. |
| Employee Recognition Platform | Discretionary, often non-monetary recognition moments; no budgets-of-record, no pay-of-record write-back. | Remove governed determination → recognition. |
| Budgeting & Forecasting Platform (finance) | Plans workforce *cost* in aggregate; comp platform anchors money to *specific employees and awards*. | Detach awards from employees → FP&A. |

## Uncertainties

1. **Pay structures (grades/bands/ranges/compa-ratio)** — widely associated with the domain, but NOT verified in any fetched source. Deliberately excluded from the final document beyond the evidenced "market reference points" concept.
2. **SMB/mid-market segment** — sample is enterprise-skewed (Payscale/Paylocity/HiBob unreachable). No claims made about lighter-weight products.
3. **Exact cycle mechanics** — snapshot timing, proration rules, effective dates, rounding: not evidenced; final document speaks only of effective-dated changes and eligibility being configured.
4. **SuccessFactors operational detail** — marketing page only; no Tier-1 docs reachable.
5. **Worksheet form factor** — Oracle documents a task-based model, Workday shows a review summary screen; the classic "spreadsheet-like manager worksheet" is strongly implied (and beqom FAQ references manager proposals en route) but no single source documents it verbatim as a grid. Final document describes the review surface conceptually.
6. **Employee self-service depth** — statements evidenced; whether employees view proposed (pre-approval) figures is NOT evidenced; final document stays silent on pre-approval visibility.

## Final Synthesis

A Compensation Management Platform is the organization's pay-decisioning layer: it manages the cycle and case-by-case acts by which the organization changes what its people are paid — base salary, bonuses, equity — under budgets, guidelines, market reference, and equity constraints, and it delivers the finalized awards back into the employee's record of pay from which payroll and total-rewards communication draw. The defining core is the four-part loop (pay population → components/programs → governed award proposal → approved update to pay of record). Everything else — cycles themselves, budget cascades, guidelines, benchmarks, statements, dashboards, AI — is mature market structure around that loop, and component mix, packaging, regulatory posture, and incentive depth vary by segment and vendor.
