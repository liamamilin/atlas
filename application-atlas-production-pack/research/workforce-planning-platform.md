# Research Notes — Workforce Planning Platform

Research date: **2026-09-08**
Slug: `workforce-planning-platform` (DIRECTORY.md §09 HR, Workforce & Talent)

Pre-hung flags to discharge (from sibling passes):
- workforce-management-platform (§09, 2026-09-08): "workforce-planning-platform seam left for that pass (strategic long-horizon headcount vs operational shift/day loop)"
- organization-design-platform (§09, 2026-09-06): joint-review flag — shared headcount/cost metrics, different center of gravity
- people-analytics-platform (§09, 2026-09-07): forward-looking planning vs descriptive/diagnostic analytics; vendors bundle
- competency-management-platform (§09, 2026-09-07): workforce planning named an "unprocessed consumer of readiness/gap data"

---

## Research Goal

Understand what a Workforce Planning Platform actually is as an Application Type: what the plan object is, how demand and supply are built, what the planning loop looks like, who uses it, and where its boundary sits against People Analytics, Organization Design, Workforce Management, FP&A/Budgeting, Succession Planning, and HRIS.

## Initial Boundary (hypothesis before research)

- Hypothesis: a platform for long-horizon, organization-level planning of workforce demand and supply — how many people of what kinds (roles/skills), where, at what cost, over future periods — built on a baseline of the current workforce, projecting supply (attrition, movement), expressing demand from business strategy, computing gaps, and modeling scenarios/actions (hire, upskill, restructure) to close them.
- Likely confusions:
  - People Analytics Platform (sibling, processed) — descriptive measurement of the current/past workforce
  - Organization Design Platform (sibling, processed) — structure scenarios (reporting lines, spans, positions)
  - Workforce Management Platform (sibling, processed) — operational shift/day labor deployment
  - Budgeting & Forecasting Platform (§08) — money-centric planning where headcount is a cost line
  - Succession Planning Platform (sibling) — individual readiness for key roles
  - HRIS (sibling) — employment/position records of record (current state)

## Research Questions

1. What is the core object of record? Is there a persistent "plan" held as structured data over a time horizon?
2. How is the supply side / baseline established (HRIS/payroll/ERP actuals; positions vs people vs skills)?
3. How is demand expressed (business goals, driver assumptions, finance targets)?
4. What does the planning loop look like end to end (baseline → demand → supply projection → gap → scenario/action → selection → tracking)?
5. What time horizons and granularities exist (multi-year strategic vs annual headcount plan; position vs role-cluster vs skill)?
6. What are the outputs and handoffs (hiring plans to HCM/recruiting, cost plans to finance, structure changes to org design)?
7. Who uses it and how do collaboration/approval work?
8. Where do the boundaries sit against the six neighbor Types above?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Visier Workforce Planning | People-analytics-native companion solution | Enterprise |
| Nakisa Strategic Workforce Planning Suite | Enterprise SWP suite with formal methodology + headcount planning module | Fortune-1000 enterprise |
| OrgVue | Consulting-led workforce-transformation platform; SWP + org modeling on one data model | Global enterprise / transformation programs |
| Workday Adaptive Planning (Workforce Planning) | FP&A-suite pole: workforce planning inside an enterprise planning platform | Enterprise |
| ChartHop (Planning: scenarios + headcount planning) | Org-chart-native mid-market platform | SMB / mid-market |

## Sources

Fetched 2026-09-08 (Tier 2 official product pages unless noted):

- Visier: https://www.visier.com/solutions/workforce-planning/ (Tier 2). docs.visier.com returned empty — not retried.
- Nakisa: https://nakisa.com/products/strategic-workforce-planning-software/ (Tier 2; detailed 6-step workflow documented on the page)
- OrgVue: https://www.orgvue.com/solutions/workforce-planning/ (redirects to /solutions/strategic-workforce-planning/) (Tier 2; 5-step workflow + FAQ on page)
- Workday: https://www.workday.com/en-us/products/adaptive-planning/workforce-planning/overview.html (Tier 2; use-case taxonomy at .../headcount-cost-planning.html, .../strategic-workforce-planning.html, .../talent-planning.html, .../workforce-capacity-planning.html observed at nav level)
- ChartHop: https://docs.charthop.com/planning (Tier 1 doc index: Scenarios / Headcount planning / Compensation bands); https://docs.charthop.com/headcount-planning returned an empty client-rendered body — headcount-planning mechanics rest on the doc index + the scenarios doc already captured first-hand by the organization-design pass (research/organization-design-platform.md), cited as internal cross-pass evidence.

Failed / not fetched: docs.visier.com (empty), docs.charthop.com/headcount-planning (client-rendered empty), charthop.com/solutions/headcount-planning (404). No precise numeric claims are asserted anywhere; where a product's evidence is page-level only, this is noted.

---

## Product Observations

### Visier Workforce Planning (evidence layer A — official product page)

- Positioning: "Visier Workforce Planning helps you shape your workforce according to your business goals while managing costs. It's a collaborative tool that helps HR, Finance, and business leaders align on data-driven strategic people plans."
- Headline promise: "Forecast and track your required future workforce."
- Collaborative planning: "get aligned on the current state of the workforce, and the desired future state. Delegate portions of a plan to various stakeholders so they can have input and stay accountable."
- Continuous planning: "Headcount and business conditions are constantly changing, which is why a once-annual planning process can fall short. Visier Workforce Planning lets you track actuals and make adjustments on the fly so that your plans and forecasts are always up to date."
- Finance bridge: "This solution bridges the gap between headcount plans and financial budgets. It goes beyond the capability of financial planning systems by enabling you to plan within shared goals for finance and workforce requirements."
- Data posture: "As a companion solution to Visier People, Visier Workforce Planning automatically brings in the data that matters from your core HR systems. It can also pull in data from financial planning systems."
- Capability claims: "answer strategic questions about your current workforce, model detailed future scenarios, and forecast your future workforce using predictive models."
- Representative questions the product answers: "What changes to hiring and internal movement will be necessary to hit our headcount goals?" / "How should we shape our workforce in order to hit specific financial targets?" / "What will my workforce look like a year from now, and how should we modify that?" / "How does turnover affect my hiring strategies and workforce costs?" / "How can we fill current talent gaps in a cost-effective way?"

### Nakisa Strategic Workforce Planning Suite (evidence layer A — official product page)

- Positioning: "streamlines the entire workforce planning process—from current state assessment to upcoming needs forecasting, gap analysis, future scenario modeling, headcount planning, and real-time impact monitoring and adjustments."
- Documented 6-step SWP workflow:
  1. **Strategic initiative creation, timeline, and cluster selection** — initiatives with name/goals/stakeholders; **time horizon** chosen (long-term 3–5 years, medium 2–3, short-term); **dimensions/clusters** (legal entity, business unit, function, job family, location).
  2. **Current state assessment** — analyzes both talent ("supply pool") and positions ("position pool") via a **5C framework**: Capacity (headcount, FTE, position trends), Cost (salaries, compensation, position budgets incl. vacancies), Capabilities (skills/competencies at employee and position level), Composition (roles, functions, seniority, demographics, employment types), Configuration (org structure incl. spans and layers).
  3. **Future state driver configuration** — three driver classes: **Supply drivers** (attrition rates, retirements), **Market drivers** (unemployment, inflation), **Demand drivers** (revenue growth targets, geographical expansion, operational efficiency goals).
  4. **Gap analysis of current vs. future state** — same 5C dimensions compared over time.
  5. **Scenario creation, comparison, and selection** — scenarios to close the supply/demand gap using the **6B model**: Buy (recruit), Borrow (contractors), Bot (automate), Build (upskill), Bounce (reduce/transition), Bind (retain).
  6. **Selected scenario continued tracking** — monthly/quarterly evaluation, recalibration; "at this stage, based on your internal processes, you can begin operational or strategic organizational design and operational workforce planning."
- Headcount planning module (same suite): "Create detailed plans with specific headcount and budget targets. Monitor progress, adjust as needed"; centralize headcount planning "to visualize team structures, hiring gaps, create and approve headcount plans, and monitor hiring progress"; AI agent to "instantly apply changes like reallocating headcount or updating budgets"; "Leverage real-time data from integrated ERPs"; "Allocate headcount to distinct budgets"; RBAC; "Assign parts of the headcount plan to dedicated teams, collaborate, and chat directly in the app"; approvals.
- Portfolio split (vendor's own taxonomy): **Org Chart Suite** (visualization) / **Org Design Suite** (org scenario modeling and design) / **Strategic Workforce Planning Suite** (analytics and headcount planning) under one "Workforce Planning Portfolio".

### OrgVue (evidence layer A — official solution page)

- Positioning: "Intentionally align your workforce capacity, skills and costs to your business strategy."
- Vendor's own definition of effective workforce planning: "A process that aligns the deployment of your workforce to deliver strategic business goals; A Planning baseline that segments the workforce data into clearly defined roles, job families and levels with visibility on current cost and headcount; The ability to instantly identify gaps between workforce supply and demand over time; The ability to model and assign the right people with the right skills to appropriate work; Continuous monitoring of progress against both the workforce and business plan."
- Documented 5-step workflow:
  1. **Build a strong planning baseline** — "Bring in data from your HRIS system, cost information, budget from Finance, payrolls or other planning systems"; segment the workforce; role architecture via AI; "How do open positions impact the current structure and workforce?"
  2. **Strategic workforce planning** — "Translate assumptions and simulate future demand and supply forecasts across multiple scenarios"; screenshot captions: "Setting up the demand planning… determine what your demand is going to look like over time"; "Viewing current plan (blue bars) and comparing it to strategic demand plan (orange)"; "Where do I face the biggest talent risk due to AI, attrition or retirement?"
  3. **Organization modeling** — "Simulate changes using drag-and-drop simplicity, and instantly see the impact on your plan"; "What if I closed five positions in a specific region, in two years?"; screenshot: "Seeing the supply versus demand gap for different role clusters, per quarter."
  4. **Operational workforce planning** — "Compare 'as is' and 'to be' costs, and forecast net full-time equivalent cost demand over time, highlight critical gaps, finalize budget and cost plan and delegate planning tasks across business units."
  5. **Tracking and monitoring** — "Monitor actuals down to position level and review your plan accordingly. Am I actually meeting my planned headcount and cost? Which departments are off-plan?"
- FAQ: workforce planning "typically involves five key steps": setting strategic direction → analyzing the workforce → developing an action plan (hiring, training, restructuring) → implementing strategies → monitoring and evaluating.
- Same platform also sells organization design, skills gap analysis, succession planning, job architecture (bundling evidence).

### Workday Adaptive Planning — Workforce Planning (evidence layer A for product page; Tier 2)

- Positioning: "bring HR, finance, and operations together in one powerful platform to create workforce plans."
- "Model your workforce dynamics. Model hiring, transfers, and retention plans with driver-based assumptions, and see the cost impact instantly."
- Use cases (own taxonomy): **Headcount and cost** ("Easily link workforce plans to financial models with up-to-date headcount plans and related costs, staying on budget"); **Workforce capacity planning** ("allocating the right people at the right time"); **Talent planning** ("Model skills capacity by location, time, cost of workforce… test different scenarios"); **Strategic workforce planning** ("Build the right team to better meet your strategic goals and business initiatives").
- FAQ: "Identify your organization's talent needs and talent gaps, and plan scenarios for how best to fill them. Then, publish your approved hiring plans for automated rendering in HCM by your recruiting teams to kick off the hiring process—no more errors, unaccounted-for requisitions, or having to chase down associated budgets."
- Stated key principles: "Powerful modeling and scenario planning" (multidimensional modeling engine, compare scenarios); "Companywide collaboration" (shared views, planning process workflows); "Continuous planning" (plan-execute-analyze cycle).
- Nav-level taxonomy: Workforce Planning sits inside the Adaptive Planning (FP&A) product family alongside Financial Planning; "Easy integration with any HR system".

### ChartHop Planning (evidence layer A for docs index; scenarios detail via sibling pass)

- Planning doc index (Tier 1, directly observed): three entry docs — **Scenarios** ("Understand how to propose org changes with scenarios"), **Headcount planning** ("Learn about creating headcount plans"), **Compensation bands**.
- docs.charthop.com/headcount-planning body was empty at fetch time; headcount-planning mechanics below the doc-title level could not be directly observed this pass.
- From the organization-design pass's first-hand capture (research/organization-design-platform.md): scenarios are sandboxed proposals ("changes to the hiring plan, backfills, promotions, organizational structure"), isolated until "merged to Primary", with annualized/FY/quarter cost views, review/approval statuses, and an HRIS-sync caveat ("if you merge the changes before you have updated your HRIS the data will be overwritten in the next days sync").
- Product site (sibling pass): positioned "People analytics and workforce planning"; HRIS/ATS/FP&A integrations; Headcount Planning is a named module/package.

---

## Cross-product Comparison

| Dimension | Visier | Nakisa SWP | OrgVue | Workday Adaptive | ChartHop |
|---|---|---|---|---|---|
| Plan as object over horizon | yes — plans/forecasts adjusted "on the fly" | yes — initiatives with explicit horizon (short/2–3y/3–5y) | yes — plan vs strategic demand over time, per quarter | yes — plans linked to financial models over periods | yes — headcount plans; scenario proposals |
| Supply/baseline from HR actuals | yes — data "from your core HR systems" | yes — supply pool + position pool, ERPs | yes — HRIS, cost, budget, payroll data in | yes — integrates with any HR system | yes — HRIS sync |
| Demand from business goals/drivers | yes — "shape workforce according to business goals… hit specific financial targets" | yes — demand drivers: revenue growth, expansion, efficiency | yes — "translate assumptions… strategic demand plan" | yes — driver-based assumptions | yes — hiring plan within scenarios |
| Supply dynamics modeled | yes — turnover → hiring strategies and costs | yes — attrition/retirement supply drivers | yes — talent risk from "AI, attrition or retirement" | yes — "hiring, transfers, and retention plans" | partial — backfills/hiring in scenarios |
| Gap analysis | yes — "fill current talent gaps cost-effectively" | yes — 5C gap analysis current vs future | yes — "supply versus demand gap by role cluster, per quarter" | yes — "talent needs and talent gaps" | yes — hiring gaps visualization |
| Scenarios / actions to close gaps | yes — "model detailed future scenarios" | yes — 6B action strategies per scenario | yes — multi-scenario simulation incl. position closures/outsourcing | yes — "plan scenarios for how best to fill them" | yes — sandboxed scenarios, merge-to-Primary |
| Workforce economics (headcount + cost/comp) | yes — cost-driven people planning | yes — Cost is one of the 5C; headcount+budget targets | yes — "capacity, skills and costs"; FTE cost demand | yes — headcount and related costs vs budget | yes — cost header on scenarios |
| Plan-vs-actual tracking | yes — track actuals, adjust on the fly | yes — monthly/quarterly tracking of selected scenario | yes — actuals down to position level | yes — monitor costs/open positions, course-correct | yes — HRIS-synced org chart vs scenario |
| Collaboration/delegation | yes — delegate portions of a plan | yes — assign parts of plan, approvals, RBAC | yes — delegate planning tasks across BUs | yes — companywide collaboration, workflows | yes — scenario collaborators, approvals |
| Handoff to execution | companion to HCM-data platform | explicit: → operational workforce planning / org design; headcount plan approvals | → operational workforce planning: finalize budget/cost plan | explicit: approved hiring plans → HCM rendering for recruiting | scenario merge → HRIS same-day sync |
| Skills dimension | yes — talent gaps | yes — Capabilities in 5C | yes — "capacity, skills and costs"; skills gap analysis | yes — talent planning "skills capacity" | not observed at doc level |
| Where it lives in the vendor's portfolio | companion module of an analytics platform | one of three suites in a Workforce Planning Portfolio | one solution on a transformation platform | product inside an FP&A suite | planning module of a people-ops platform |

### Cross-product commonalities (evidence layer B)

Present across the sampled products:

1. **The plan as the managed object** — a persistent, structured, editable plan of the future workforce across defined future periods, distinct from reports/dashboards about the current workforce.
2. **A current-workforce baseline (supply anchor)** — headcount/positions/roles/cost drawn from HR/payroll/ERP systems (integration or import), continuously reconciled with actuals.
3. **Demand expressed from business strategy** — revenue/growth/expansion/efficiency goals or driver assumptions translated into required workforce by segment.
4. **Supply projection through workforce dynamics** — attrition, retirements, transfers, retention modeled between now and the horizon.
5. **Gap computation** — demand vs supply per segment per period, made visible (role clusters × quarters in the observed examples).
6. **Scenario modeling and action selection** — alternative futures and action sets (hire/borrow/automate/build/reduce/retain vocabulary) compared to close gaps; a selected plan emerges.
7. **Workforce economics** — headcount/FTE plus cost/compensation as the plan's shared currency bridging HR and Finance.
8. **Continuous plan-vs-actual tracking and re-planning** — actuals fed back against the plan; plans adjusted intra-cycle.
9. **Collaboration with delegation and approval** — plan portions delegated to stakeholders; approval gates before a plan becomes official.
10. **Handoff toward execution** — approved plans pushed toward recruiting/HCM, finance budgets, or operational workforce/org-design processes.

### What varies (candidate L2)

- Time horizon: multi-year strategic (3–5y) ↔ medium (2–3y) ↔ short-term annual/quarterly headcount planning ↔ continuous re-forecast.
- Granularity: position-level ↔ role/job-family clusters ↔ skills/competencies.
- Packaging: standalone-ish module of an analytics platform / one suite in a planning portfolio / one solution of a transformation platform / module of an FP&A suite / module of a people-ops platform.
- Modeling depth: driver-based deterministic modeling vs predictive/AI forecasting vs drag-and-drop org modeling.
- Structure dimension: pure quantity planning vs planning coupled to org-structure authoring (OrgVue, ChartHop scenarios carry structure changes).
- Delivery model: self-serve SaaS vs consulting-led transformation programs.
- Audience weighting: HR-led vs Finance-led vs executive/transformation-led.

---

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Workforce Planning Platform exists only if all three hold:

1. **The workforce plan as object of record** — a persistent, structured, editable plan of the organization's future workforce (people — by roles/skills/org segments — and their levels), organized across a defined future time horizon. Remove → an analytics report or dashboard about the current workforce; nothing is being "planned".
2. **A current-workforce baseline anchoring the plan** — the plan is built on the organization's actual present workforce (headcount/positions/roles, typically with cost) taken from HR/payroll/ERP records (integrated or loaded), and is reconciled against actuals as they accumulate. Remove → generic strategic or financial planning where the workforce is not the subject.
3. **The demand → supply → gap → action loop over the horizon** — future workforce demand is expressed from business goals/driver assumptions; supply is projected through workforce dynamics (attrition, movement, retirement); the gap between them is computed per segment and period; and scenarios/actions to close the gap are modeled, compared, and selected. Remove the loop → a headcount budget sheet or a forecast report.

Jointly-held is load-bearing: 1 alone = a planning spreadsheet with no anchor or loop; 2+3 without 1 = analytics with projections but no plan of record; 1+3 without 2 = free-floating scenario theater disconnected from the real workforce; 1+2 without 3 = a budget table with no planning semantics.

Evidence calibration: each leg is directly observed in all five sampled products (layer A), and the loop shape is independently articulated in vendor-documented workflows (Nakisa 6 steps; OrgVue 5 steps; Workday's three stated principles).

### L1 — Common Mature Structure

- HRIS/payroll/ERP/finance-system integrations feeding the baseline
- Workforce economics: headcount/FTE AND cost/compensation as twin currencies (present in all five samples, but a headcount-only plan remains recognizable — cost is standard, not defining)
- Skills/competency dimension on the supply and demand sides (skills-gap analysis; capabilities in current-state assessment)
- Predictive/AI-assisted forecasting of attrition or future workforce state
- Approval workflows over plans/scenarios; role-based access
- Dashboards and reports (gap views by segment × period; plan-vs-actual views)
- Templates/multi-cycle plan management (annual cycle, re-forecast rounds)
- Export/reporting toward finance and executive audiences

### L2 — Variant / Optional Structure

- Horizon posture: strategic multi-year SWP vs annual/quarterly headcount planning vs continuous planning (the leaf's own market names "strategic workforce planning" and "headcount planning" as poles of the same Type — Workday sells both as use cases of one product; Nakisa's SWP Suite contains a headcount planning module)
- Granularity posture: position-level vs role-cluster vs skills-based planning
- Packaging: analytics-suite companion vs FP&A-suite module vs transformation platform vs people-ops platform module vs standalone
- Coupling to org-structure authoring (scenarios that move positions/reporting lines) — the org-design overlap zone
- Consulting-led delivery vs self-serve
- Industry/regulatory contexts (e.g., public-sector workforce planning)

### L3 — Vendor-specific (research notes only)

- Nakisa: 5C framework (Capacity/Cost/Capabilities/Composition/Configuration); 6B model (Buy/Borrow/Bot/Build/Bounce/Bind); initiative→driver→gap→scenario→tracking step naming; Nakisa AI Agent for headcount reallocation; long list of security certifications; product-sheet PDF.
- OrgVue: Henshaw Roles AI; role grids and role clusters; "blue bars vs orange" plan/demand visuals; Forrester-conducted survey assets (209 decision makers); TVH/UK-public-sector case studies; self-assessment tool.
- Visier: companion-solution framing to Visier People; "beyond the capability of financial planning systems" claim; predictive-model forecasting language.
- Workday: Elastic Hypercube Technology; "publish approved hiring plans for automated rendering in HCM"; customer-average marketing figures (70% shorter planning cycles); use-case nav taxonomy (Headcount & Cost / Capacity / Talent / Strategic).
- ChartHop: scenario status names and merge-to-Primary semantics (captured by the sibling pass); PEPM pricing; Carrot query language; compensation bands doc adjacency.

---

## Vendor-specific Findings

See L3. None enter the canonical document. Nakisa's and Workday's own product taxonomies are treated as **boundary evidence** (where vendors draw the seams), not canonical structure.

## Boundary Findings

1. **vs People Analytics Platform (§09, processed) — FLAG DISCHARGED; keep-both.** Analytics is descriptive/diagnostic over what is and has been (integrated data layer + governed metrics + question→answer loop); workforce planning is normative and forward-looking — it holds plan objects across a future horizon and runs the demand→supply→gap→action loop. Vendors bundle them (Visier Workforce Planning is explicitly "a companion solution to Visier People"; Workday pairs Adaptive Planning with Analytics & Reporting; ChartHop markets both). Test: remove plan objects + the horizon loop → analytics remains; remove the analytical question→answer layer → planning remains (it keeps the plan, baseline, and gap loop). Consistent with the people-analytics pass's own seam formulation.
2. **vs Organization Design Platform (§09, processed) — FLAG DISCHARGED; keep-both.** Org design centers the structure question (how should the organization be structured; structure scenarios compared by impact); workforce planning centers the quantity-over-time question (how many people of what kind will be needed, when, at what cost — demand/supply per period). Vendors bundle and hand off between them: OrgVue runs both on one platform (its workforce-planning flow includes an org-modeling step); Nakisa ships them as **two separate suites** and its SWP workflow's final step explicitly hands off to "operational or strategic organizational design" — vendor-confirmed packaging evidence for the seam; Workday lists "Org Design & Scenario Modeling" as a use case adjacent to (not constituting) Workforce Planning. Test: remove time-phased demand/supply/gap machinery → org design remains; remove structure authoring/scenario-of-structure → workforce planning remains. Cross-reference written both directions consistent with the org-design pass's flag.
3. **vs Workforce Management Platform (§09, processed) — FLAG DISCHARGED; keep-both; disambiguation cross-reference written.** WFM is the operational labor-deployment system (shift/day loop: demand → schedules → worked time → labor governance). Workforce planning is the strategic/tactical planning layer above it (multi-period workforce demand/supply/gap/action; no shifts, no time capture). Vendor evidence for the layering: Nakisa's SWP step 6 explicitly hands off *down* to "operational workforce planning"; the WFM pass recorded UKG's "Strategic Workforce Planning" as a feature-level layer inside a WFM suite. Test: remove the shift/day operational loop → workforce planning remains; remove the multi-period plan loop → WFM remains.
4. **vs Budgeting & Forecasting Platform (§08) / FP&A** — FP&A is money-centric: revenue/expense/cash lines, with headcount appearing as a cost line. Workforce planning is people-centric: the subject is people (roles/positions/skills/capacity) with cost as the shared currency layer. Workday's own framing shows the seam from the FP&A side: "Easily **link** workforce plans to financial models" — link, not identical; Visier explicitly claims to "go beyond the capability of financial planning systems by enabling you to plan within shared goals for finance and workforce requirements". Workday Adaptive Planning realizes this Type as a module inside an FP&A suite — packaging, not identity. Test: swap the subject from people to money lines → FP&A remains; keep people as subject with cost as attribute → workforce planning remains.
5. **vs Succession Planning Platform (§09)** — succession centers identified individuals and their readiness for specific key roles (pipelines of named people); workforce planning centers aggregate workforce quantities by segment over time (pools, not names). The competency-management pass flagged workforce planning as a consumer of readiness/gap data — confirmed here conceptually: gap-closure actions (Build/Bind/transition) and talent-risk views consume capability/readiness signals, but the plan object remains aggregate. Test: named-individual pipelines are succession; aggregate segment plans are workforce planning.
6. **vs HRIS (§09)** — HRIS is the employment/position record master for the current state and HR operations; workforce planning consumes its data as the baseline and holds the *plan* of record for the future. Requisition/headcount approval inside HCM suites is the execution-side machinery the plan hands off to (Workday's publish-into-HCM flow shows the seam).
7. **vs Demand Planning (§10 supply chain)** — demand planning forecasts goods/services demand; workforce planning forecasts the workforce needed to serve whatever the business demands. They may consume the same business drivers from opposite sides.
8. **Historical / market-sample check** — paper-era **manpower planning** satisfies the L0 at analog level: an HR planner's working file held the current establishment by department/grade (baseline from personnel records), forecast requirements by year from business plans (demand), attrition/retirement estimates (supply dynamics), the resulting gap, alternative staffing scenarios (hire/train/redeploy), and periodic reconciliation — all without software, skills ontologies, AI, or approvals workflows. The 1990s–2000s spreadsheet era satisfies identically. Therefore the definition does not overfit the current SaaS market: predictive forecasting, skills ontologies, ERP write-back, and AI agents are all standard capabilities, not definitional. "Workforce planning" and the older "manpower planning"/"human resource planning" name the same job; "strategic workforce planning" vs "headcount planning" is a horizon gradient inside the Type, not two Types.

## Uncertainties

- No Tier-1 operational help-center docs were reachable for Visier, Nakisa, OrgVue, or Workday this pass (docs.visier.com empty; enterprise HCM/planning help portals historically login-gated per prior passes). All four products are evidenced at official product-page level (Tier 2); workflow claims for Nakisa/OrgVue rest on vendor-documented methodology published on those pages, which is more detailed than typical marketing prose but is still vendor self-description. Assertion strength kept moderate for interface-level mechanics.
- ChartHop's headcount-planning doc body was empty at fetch time; its headcount-planning mechanics below doc-title level were not directly observed. ChartHop evidence = doc index + the sibling pass's first-hand scenarios-doc capture.
- Whether approvals/write-back into HCM or ERP are universal could not be verified across the whole market; observed in Workday, Nakisa, ChartHop (merge-to-Primary), but held as common-mature machinery, not invariant.
- Market-share ordering of FP&A-suite modules vs HR-analytics companions vs standalone SWP vendors was not researched; the Type does not depend on it.
- The exact default horizons, cadence defaults, and numeric limits of any product were not researched; no precise numbers asserted (Nakisa's 3–5y / 2–3y horizon *options* are quoted as vendor-documented options, not defaults).

## Final Synthesis

A Workforce Planning Platform is defined by a small loop: hold the current workforce as the baseline → express future demand from business goals and drivers → project supply through workforce dynamics → compute gaps by segment and period → model and compare scenarios/actions to close the gaps → track the selected plan against actuals and re-plan. The plan itself — a persistent, time-phased, editable object anchored in HR actuals — is what makes this a planning system of record rather than an analytics tool; the loop is what makes it planning rather than budgeting; the aggregate, multi-period subject is what separates it from org design (structure), succession (individuals), and workforce management (shift/day operations). Everything else commonly associated with the category — cost/comp modeling, skills dimensions, predictive forecasting, approvals, AI, dashboards, HCM/ERP write-back — is mature market structure or variant packaging, not the definition.
