# Research Notes — Capital Improvement Planning

Research date: **2026-09-06**
Slug: `capital-improvement-planning`
Directory location: §24 Government, Public Sector & Civic — "Capital Improvement Planning"

---

## Research Goal

Understand what a Capital Improvement Planning (CIP) application actually is as a software type: what objects exist inside it, what workflow it supports, which parts are defining versus merely common in current products, and where its boundaries lie against Public Budgeting Platform, Construction Project Management, Public Asset Management, Government Grants Management, and related public-sector types.

## Initial Boundary (working hypothesis before research)

- CIP software supports a government (or similar public entity) in assembling and governing a **multi-year plan of capital projects**: proposed long-lived physical improvements (roads, buildings, water/sewer systems, parks, facilities, fleets, equipment), each with cost estimates, scheduled fiscal years, and assigned funding sources.
- Capital funding is characteristically **constrained and lumpy** (bonds, grants, impact fees, rates, reserves), which makes prioritization the central activity.
- The plan is a **governed artifact**: adopted (and amended) by the jurisdiction's governing body, linked to the annual budget process.
- Likely confusions: operating-budget software (annual expense authority), construction project management (delivery of one approved project), asset management/EAM (condition and maintenance of existing assets), grants management (funding-source lifecycle).

## Research Questions

1. What are the core objects? (project request vs project vs plan vs funding source vs budget year vs allocation)
2. What is the defining workflow: intake → evaluation → selection → multi-year scheduling → funding match → adoption → year-1 funding → tracking/amendment?
3. What makes a project "capital" in these systems, and how is routine maintenance excluded?
4. How are funding sources modeled? (categories, per-year allocations, splits, gaps, debt/maintenance forecasts)
5. How is prioritization done? (criteria, weighted scoring, ranked lists, defensible recommendations)
6. What governance surfaces exist? (adoption, amendment, roll-forward, publication, transparency)
7. What happens after adoption? (execution/status/spending tracking — core or optional?)
8. What interfaces appear? (plan workspace, project detail, scoring matrix, funding table, map, dashboards, public portal)
9. What variants exist? (suite module vs standalone; municipal/county/district/school/utility; engagement-led public surfaces)
10. Where are the boundaries against adjacent types, and what "removal test" expresses each boundary?

## Representative Products (selection rationale)

Chosen for different product philosophies and different interaction surfaces:

| Product | Philosophy / position | Tier | Access outcome |
|---|---|---|---|
| **Euna Budget — Capital Budgeting** (formerly Questica; Euna Solutions) | CIP as a module of a public-sector budgeting suite; finance-led planning + funding + post-adoption oversight | mid-size to large municipalities, provinces, states | ✅ Official product pages fetched (budget suite page + capital-budgeting page) |
| **Balancing Act — Prioritize** (Engaged Public) | Public-engagement-first: residents/stakeholders select and rank budgeted projects; input into (not execution of) the capital plan | any-size local government | ✅ Official site + Prioritize solution page fetched |
| **OpenGov — Capital Projects / capital planning** | Market-leading suite; planning + execution tracking + resident portals | local government up to state | ❌ 403 on product page and help center; archive.org timeout ×2 |
| **ClearGov — Budgets (capital budgeting module)** | SMB local-government budget-cycle suite with capital module | small/mid local government | ❌ 403 on product page and help center |

OpenGov and ClearGov are retained only as **market anchors** (widely referenced in the local-government software market); no product claim about them is asserted anywhere in this research or the final document.

Munetrix (fetched) has pivoted its public site to K-12 analytics — dropped as a representative. VueWorks returned no content — dropped. Questica's own site now redirects to Euna Solutions (Questica was folded into Euna Budget) — noted as market consolidation, not usable as a separate sample.

## Sources

Successfully fetched (2026-09-06):

- Euna Solutions — Budget (suite page): https://eunasolutions.com/solutions/budget/ — Tier 2 (official product page)
- Euna Solutions — Capital Budgeting (module page + FAQ): https://eunasolutions.com/solutions/budget/capital-budgeting/ — Tier 2 (official product page)
- Balancing Act — homepage: https://www.abalancingact.com/ — Tier 2 (official product page)
- Balancing Act — Prioritize: https://abalancingact.com/solutions/prioritize — Tier 2 (official product page)
- MRSC (Municipal Research and Services Center of Washington) — Explore Topics: Finance & Budgeting; Budgeting TOC: https://mrsc.org/explore-topics/finance , https://mrsc.org/explore-topics/finance/budgets/budgeting-contents — official public-sector guidance; used only for type context (budget = legal authority to expend funds; annual/biennial adoption cadence)

Attempted but **unreachable** (evidence limitation recorded per source-access rules):

- opengov.com/products/capital-projects/ — 403; support.opengov.com — 403; web.archive.org snapshots — timeout ×2
- cleargov.com/products/budgets — 403; help.cleargov.com — 403
- gfoa.org (capital budgeting best practice) — 403
- en.wikipedia.org / en.m.wikipedia.org "Capital improvement program" — timeout ×3
- help.eunasolutions.com (operational help portal) — 403
- mrsc.org dedicated CIP topic page — expected path 404 (CIP not exposed in fetched budgeting TOC)

**Consequence for assertion strength:** no Tier-1 operational help-center documentation was reachable for any sampled product. All product observations below rest on official marketing/product pages (Tier 2) and are marked evidence layer **A (directly observed, page-level)**. No precise numeric claims (horizon lengths, thresholds, defaults, state names) are asserted anywhere from memory; qualitative process claims are calibrated accordingly.

---

## Product A — Euna Budget, Capital Budgeting module

### Key observations (evidence layer A — official product pages, 2026-09-06)

Positioning: "Control capital spending with detailed project budgeting and multi-year funding oversight." The module is one of several budgeting modules (strategic, performance, personnel, operating, capital, transparency/OpenBook).

Workflow presented as three named stages — PLAN / BUILD / MANAGE:

1. **Evaluate & Allocate Capital Funding** ("Prioritize & Fund the Right Projects")
   - "Evaluate and rank projects across departments so limited funds are allocated responsibly."
   - "Score projects using weighted criteria"
   - "Split allocations across multiple sources, grants, or cost centers"
   - "Generate defensible, evidence-based recommendations for funding decisions"

2. **Build a Multi-Year Capital Plan**
   - "Organize projects across the timelines you need… align funding, scenario plan, and build a structured long-term plan."
   - "Set annual, quarterly, or monthly project timelines"
   - "Categorize by asset, fund, or status"
   - "Create and compare multiple planning scenarios"

3. **Oversee Projects & Spending**
   - "Oversee approved projects from funding through completion to maintain fiscal oversight and transparency."
   - "Monitor project status, timelines, and spending"
   - "Track expenditures and balances across years"
   - "Adjust funding or priorities as projects evolve"

Additional surfaces and claims:

- **Capital–operating linkage**: "Link capital and operating budgets to see how each project impacts long-term financial sustainability."
- **Scenario planning**: "compare funding strategies, phasing options, and long-term financial impacts before committing resources"; "model multi-year financial outcomes for capital projects"; "test alternative funding and scheduling scenarios"; FAQ adds "forecast maintenance costs, debt obligations, and future funding needs to build a sustainable plan."
- **Interactive mapping**: "Upload GIS files to map project locations and link to budget details"; "Share an interactive public map through OpenBook with project descriptions, funding data, and completion dates."
- **Publication**: "Publish a digital CIP using OpenBook's integrated publishing tool… interactive charts… publish online for transparent public access, or export for print."
- **FAQ-level workflow language**: "multi-year, multi-phase capital projects"; "prioritize requests, track project dependencies, and model funding scenarios over time"; "evaluate ROI, risk, and impact"; ERP/finance integration ("project data, funding streams, and budget updates flow automatically"); "audit trails and workflow guardrails"; dashboards for elected officials/auditors/community.

### Interpretation

The module evidences the full staff-side CIP lifecycle: request prioritization → weighted scoring → multi-year scheduling → funding-source allocation (split across sources/cost centers) → scenario comparison → adoption-stage publication → post-adoption expenditure tracking and re-prioritization. It also evidences the two most common extensions: capital–operating linkage and GIS/mapping-based public presentation. Whether post-adoption tracking is defining or optional cannot be decided from one product (see Rejected Findings).

---

## Product B — Balancing Act, Prioritize

### Key observations (evidence layer A — official product pages, 2026-09-06)

Positioning: "Simulation-based public engagement tools for government." Product family: Budget Simulation (operating-budget balancing by residents), Housing Simulation, **Prioritize**, Tax Receipt, Consulting.

Prioritize: "An engagement tool to get stakeholder preferences on **budgeted projects**."

- "Goes above and beyond a survey with a unique dual approach that allows users to **make selections and then rank order them**."
- "Resulting data provides deeper insight to support decision-making **within a fixed budget** or one-time expense such as stimulus funds" (ARPA/ESSER named as use cases).
- Key features: "highly informative results, including weighted and unweighted scores"; "allows users to decide what to include in a given budget, and then rank order their selections"; "unique consensus analysis shows how many stakeholders will have at least one of their choices included"; "provides context to possible selections with images and descriptions"; "highly graphic and interactive display."
- Simulation can reportedly be created "in an hour or less" (vendor claim, not independently verified).

### Interpretation

This is the **public-facing prioritization surface** of capital/budget planning: the same underlying problem (a list of candidate projects, a constrained budget, selection + ranking) is exposed to residents instead of staff. It contains none of the funding-source accounting, multi-year scheduling, or adoption machinery — confirming that those staff-side structures are what make the CIP type, while resident prioritization is an optional engagement variant. Evidence for this product covers only the engagement surface; nothing about it establishes staff-side structure.

---

## Type-level reference — MRSC (context)

MRSC (official Washington State local-government resource) frames the annual/biennial budget as "legal authority to expend funds," adopted by the legislative body on a statutory calendar. This grounds the CIP-to-budget relationship: the multi-year capital plan is a planning artifact whose first year is funded through the adopted budget. MRSC's finance topics also list Impact Fees, Debt Management Policies, and Asset Management Policies as standard local-government finance topics — consistent with the funding-source categories observed in products — but the dedicated CIP topic page was not reachable, so no further type-level claims are drawn from MRSC.

---

## Cross-product Comparison

| Dimension | Euna Budget (Capital) | Balancing Act (Prioritize) | Evidence layer |
|---|---|---|---|
| Capital project as identified record with description/context | ✅ projects across departments, categorized by asset/fund/status | ✅ project items with images/descriptions (engagement items) | A (both) |
| Estimated cost attached to project | ✅ (project budgets, funding data) | ✅ implied (selection "within a fixed budget") | A (Euna explicit; Balancing Act implied) |
| Weighted prioritization/scoring | ✅ weighted criteria scoring | ✅ weighted + unweighted preference scores | A (both; different evaluators — staff vs public) |
| Selection under funding constraint | ✅ allocate limited funds across sources | ✅ residents select within a fixed budget | A (both) |
| Multi-year scheduling across fiscal years | ✅ explicit ("multi-year capital plan", timelines) | ❌ absent | A (Euna only) |
| Funding sources & allocations (project × source × year, splits) | ✅ explicit (sources, grants, cost centers, balances across years) | ❌ absent | A (Euna only) |
| Governance/adoption machinery | ✅ publication + audit trails; adoption implied via budget linkage | ❌ absent (input to decision) | A/B |
| Post-adoption status & spending tracking | ✅ explicit ("oversee approved projects… expenditures and balances across years") | ❌ absent | A (Euna only — single source) |
| Scenario comparison / long-term financial impact | ✅ explicit (funding strategies, phasing, debt, maintenance forecasts) | ❌ absent | A (Euna only) |
| Capital–operating budget linkage | ✅ explicit | ❌ absent | A (Euna only) |
| GIS/map presentation of projects | ✅ explicit (upload GIS, public interactive map) | ❌ (not on fetched page) | A (Euna only) |
| Public transparency/engagement surface | ✅ (digital CIP book, public map via OpenBook) | ✅ (entire product) | A (both; different depth) |
| Role separation (departments / finance / governing body / public) | ✅ implied ("evaluate and rank projects across departments", "defensible recommendations", dashboards for officials) | ❌ (single public role) | A/B |

### Reading of the comparison

- The structures present in **both** products, despite radically different surfaces: project-as-record with descriptive context, cost, prioritization, selection under a funding constraint.
- The structures unique to the staff-side product: multi-year scheduling, funding-source accounting, adoption machinery, post-adoption tracking, scenarios, operating-budget linkage, mapping.
- The engagement product demonstrates the **minimal conceptual problem** of the type stripped to its core: candidate capital items + constrained budget + priority selection. This is strong evidence for a minimal defining structure and against inflating the core with accounting machinery.

---

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the software stops being a Capital Improvement Planning application:

```text
Register of proposed capital projects
(each an identified, long-lived physical improvement —
 explicitly not routine operating/maintenance spending)
  ├── estimated cost per project
  ├── identified funding sources under constraint
  │     (allocation of project × source, splittable across sources/years)
  ├── multi-year forward scheduling
  │     (projects placed in fiscal years beyond the current budget cycle)
  └── prioritization/selection to decide what enters the plan
        (the plan is assembled under constraint, then adopted/amended
         by the jurisdiction's governing authority)
```

Five properties, deliberately small:

1. **Capital project register** — proposed improvements as identified records. The capital/operating boundary is part of the definition: if the register holds routine operating activities, the artifact is not a CIP.
2. **Estimated cost per project** — planning-level costs that make comparison and funding analysis possible.
3. **Funding-source association under constraint** — capital money is categorized (bond, grant, fee, rate, reserve-type sources) and finite; without tied funding sources the artifact is a wish list, not an improvement plan.
4. **Multi-year forward scheduling** — the plan spans multiple fiscal years beyond the adopted budget year. Horizon length varies by jurisdiction; no fixed length is asserted.
5. **Governed selection & adoption** — the plan exists as an adopted, amendable governing artifact; a scratch list of projects without a governing adoption step is not a CIP.

Historical/§24 check: a small city doing CIP in a spreadsheet and a large county using a suite both satisfy all five properties — the spreadsheet has the register, costs, years, funding columns, priority order, and a council resolution adopting it. A resident-engagement simulator alone does **not** satisfy properties 3 (accounting-grade funding sources), 4 (multi-year schedule), and 5 (adoption) — which is consistent with it being a variant surface rather than the type.

### L1 — Common Mature Structure

Very common in current mature products but not required to recognize the type:

- Departmental **project request intake** (submit → review → recommend) feeding the register
- **Weighted scoring / ranking criteria** and defensible funding recommendations
- **Funding splits** (project funded from multiple sources/cost centers; balances tracked across years); gap/unfunded status
- **Scenario planning**: alternative funding strategies and phasing; long-term financial impact (debt obligations, future maintenance/O&M)
- **Capital–operating linkage** (year-1 slice into the annual capital budget; operating impact of capital projects)
- **Post-adoption tracking**: project status, timelines, expenditures vs allocation; re-prioritization and amendments
- **Categorization** by department, asset, fund, category, status; phasing and dependencies
- **Plan publication**: CIP book/report generation; charts; public transparency access
- **Reporting/dashboards** for executives, elected bodies, auditors
- **ERP/finance-system integration** (project data, funding streams, budget updates)
- **Role-based collaboration**: departments propose; finance/budget office consolidates; executive recommends; governing body adopts

### L2 — Variant / Optional Structure

Depends on jurisdiction type, scale, region, deployment, or workflow:

- **GIS/interactive mapping** of project locations (including public interactive maps)
- **Resident engagement / participatory prioritization** (public selects and ranks projects within a budget; consensus analysis; used for one-time funding pools as well)
- **Asset-condition-driven planning** depth (needs derived from asset condition/assessment data)
- **Grant-seeking depth** (grants as funding sources with application lifecycle)
- **Jurisdiction overlays**: municipal, county, special district/utility (rate-funded), school-district facilities, state agencies
- **Packaging**: standalone CIP planner vs module inside a public budgeting suite vs planning+delivery tracking span
- **Delivery-form**: cloud SaaS vs on-premises; single-jurisdiction vs multi-entity
- **Regional vocabulary**: "capital improvement plan/program" (US), capital programme (elsewhere); annual vs biennial budget cadence downstream

### L3 — Vendor-specific (Research Notes only)

- Euna Budget: OpenBook (transparency publishing), Budget Book Studio, Euna AI, module split (strategic/performance/personnel/operating/capital/transparency); Questica lineage (questica.com now redirects to Euna Solutions); ROI/risk/impact evaluation framing; "1,000+ organizations" vendor claim.
- Balancing Act: "Prioritize" dual select-then-rank mechanic; "consensus analysis"; ARPA/ESSER stimulus-fund framing; Polco-affiliated whitepaper; "created in an hour" setup claim; Government Technology Top 100 / ELGL awards.
- OpenGov / ClearGov: market presence assumed from market knowledge; **no claims recorded** because their sites were unreachable.

---

## Vendor-specific Findings

See L3. None of the above module names, mechanics, or claims leak into the canonical model.

## Rejected Findings

Considered and rejected from the defining core:

- **Post-adoption project/spending tracking** — observed in only one sampled product (Euna). Some CIP processes end at the adopted plan and funded budget. Kept as common/optional; single-source rule applied.
- **Scenario planning / debt & maintenance forecasting** — single product. Common-mature at best; not defining.
- **GIS mapping** — single product (and optional even there). Presentation layer, not structure.
- **Public engagement as defining** — only the engagement product centers it; staff-side product treats publication as an add-on. Rejected as defining; retained as variant.
- **Fixed plan horizon (e.g., a specific number of years)** — no accessible source states a universal horizon; horizons vary by jurisdiction. Written as "multi-year, length varies."
- **Bond/debt modeling** — mentioned by one vendor; funding-source machinery is generic; debt planning is a specialization.
- **Grant application lifecycle** — grants appear as funding sources; full grant management is a different type (adjacent leaf).

## Boundary Findings

Each boundary includes the "remove what and it becomes the other type" test.

| Adjacent type | Relationship | Distinction & removal test |
|---|---|---|
| **Public Budgeting Platform** | closest sibling; CIP often ships as its module | Operating budgeting centers on the **annual expense authority** (funds, departments, line items, legally adopted each cycle). CIP centers on **multi-year projects and their capital funding**. Remove the multi-year project/funding-source structure and only annual fund/line-item budgeting remains → operating budgeting platform. Remove annual appropriation mechanics and keep projects/funding across years → CIP. |
| **Construction Project Management / Project Controls** (§17) | downstream of the CIP seam | Those types manage **delivery of an individual approved project** (schedule, bids/procurement, change orders, field operations). CIP selects, prioritizes, funds, and monitors the **portfolio**; its execution depth typically stops at status/spend vs allocation. Remove portfolio selection/funding and keep one project's delivery → construction PM. |
| **Public Asset Management / EAM (and Enterprise Asset Registry)** | upstream data provider | Asset systems hold condition/maintenance of **existing** assets; CIP decides **new/renewal investment**. Asset-condition data feeds project requests, but maintenance operations are not capital planning. |
| **Government Grants Management** | funding-source adjacency | Grants appear inside CIP as funding sources; grant lifecycle (discovery, application, compliance, reporting) is its own type. |
| **Public Works Management** | operations vs investment | Work orders/routine maintenance are operating activity — explicitly outside "capital." |
| **Government GIS** | data/presentation layer | Mapping presents CIP projects; GIS is spatial infrastructure, not the plan machinery. |
| **Government Performance Management** | different instrument | Measures/results of services vs selection/funding of capital investments; scoring criteria overlap in form only. |
| **Parks & Recreation Administration / school facilities planning** | domain variant | Same CIP machinery applied to one domain's facilities; variant, not separate type, unless domain workflows replace the core (e.g., purely instructional facilities programming). |

Also recorded: **packaging seam** — because CIP commonly ships as a module of budgeting suites, the market boundary between "Capital Improvement Planning application" and "budgeting suite with a capital module" is fuzzy at the product level. The type-level distinction (documented by center of gravity) holds, but this is flagged for awareness in STATUS.md.

## Uncertainties

1. **Operational depth of intake and approval workflows** — help-center docs were unreachable; the request → review → recommend flow is evidenced only at marketing-page granularity.
2. **Whether adoption is modeled as a system state** (draft/recommended/adopted/amended versions inside the product) or happens outside the system (documents/resolutions) — not directly observable from any fetched page. The canonical model treats the plan as a governed artifact without asserting in-product version states.
3. **Post-adoption tracking depth** (e.g., encumbrance-level accounting) — unknown; kept qualitative.
4. **Horizon norms** (how many years, roll-forward mechanics) — not asserted; varies by jurisdiction and no reachable source states a norm.
5. **Public-engagement surface prevalence** — evidenced by one product; prevalence across the market unknown.
6. **Suite-leader structure (OpenGov planning + execution + portals)** — could not be verified; the "planning→execution span" L2 variant may be more common than the single-sample evidence shows.

## Final Synthesis

A Capital Improvement Planning application is the public-sector system of record for **deciding which long-lived physical improvements to build, in which years, funded from which capital sources** — before construction and before annual appropriation. Its defining structure is small: a register of proposed capital projects with cost estimates, funding-source allocations under constraint, multi-year scheduling, prioritized selection, and governing adoption/amendment. Around that core, mature products add request intake, weighted scoring, scenario planning, capital–operating linkage, post-adoption tracking, publication, mapping, and ERP integration; engagement-led public prioritization is a distinct variant surface. The type's sharpest boundaries are against the operating budget (annual expense authority vs multi-year capital investment) and construction delivery (portfolio funding vs single-project execution).
