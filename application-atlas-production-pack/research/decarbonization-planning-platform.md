# Research Notes — Decarbonization Planning Platform

Research date: 2026-09-07
Slug: decarbonization-planning-platform
Directory leaf: Decarbonization Planning Platform (§21 Environment, Sustainability & Climate)

## Research Goal

Understand what a "Decarbonization Planning Platform" actually is as a software Type: its core objects, how the planning loop really runs inside it, what is definitional vs merely common in the current market, and where its boundaries sit against neighboring Types — especially Carbon Accounting Platform (backward-looking measurement), Climate Adaptation Planning (recorded structural twin), Climate Risk Management / Climate Scenario Analysis (risk machinery), Energy & Carbon Management / Building Energy Management (energy-operations center), generic strategy-execution machinery, and Carbon Credit Management (beyond-value-chain instruments).

This pass must also discharge the structural-twin flag recorded in STATUS.md by the climate-adaptation-planning pass: "climate-adaptation-planning (processed) vs decarbonization-planning-platform (unprocessed): identical planning loop, different content domain; market commonly carries both in one integrated climate-plan product (Futureproofed); candidate outcomes: keep-both with content-domain seam, or consolidate."

## Initial Boundary (hypothesis before research)

- What: software to plan and govern an organization's emissions reduction — baseline/hotspots → targets → reduction levers/projects → prioritized roadmap (often with abatement-cost economics and scenarios) → implementation tracking → progress vs target.
- Users: corporate sustainability teams, finance (capital allocation), operations/facility managers, executives, municipal climate teams, consultants/advisors.
- Nearest neighbors: Carbon Accounting Platform (measurement of record — the anchor), Climate Adaptation Planning (structural twin), Climate Risk Management / Scenario Analysis (upstream machinery), Energy & Carbon Management (energy-first), Sustainability/ESG Management (broader), Carbon Credit Management (offsets), generic plan-execution platforms (machinery without climate content).
- Unknowns: whether standalone pure-play decarbonization planners exist without carbon accounting; how deeply the plan object is structured (targets/levers/scenarios as first-class objects?); whether MACC is definitional or a common implementation; how the municipal climate-plan pole relates.

## Research Questions

1. What is the central managed object — the plan/roadmap? Its internal structure (targets, levers/projects, scenarios, timelines)?
2. What anchors the plan — the emissions inventory? Where does it come from (in-product, imported, assessed)?
3. What does a reduction lever/project/initiative look like (attributes: abatement potential, cost, timing, owner, status)?
4. How is prioritization done (MACC, cost per tonne, NPV/IRR/payback, co-benefits)?
5. What role do targets play (SBTi, absolute/intensity, near-term/net-zero, roll-up)? Definitional or common?
6. How does scenario/pathway modeling work (multi-year simulation, carbon-price sensitivity, comparing lever mixes)?
7. How is implementation tracked (status/owners; planned vs realized; forecasts/alerts)?
8. What roles participate (sustainability, finance, operations, executives, advisors, municipal departments)?
9. What interfaces exist (portfolio views, MACC charts, scenario modelers, roadmaps, dashboards, public pages)?
10. How does planning coexist with carbon accounting in one product (module vs standalone)? Where exactly is the seam?
11. How does the municipal climate-plan pole (plan-first, measures databases, public pages) relate to the corporate pole?
12. Boundaries: what would you remove to turn this into each neighboring Type?

## Representative Products (sample rationale)

| Product | Pole | Philosophy | Customer level |
|---|---|---|---|
| SINAI Technologies | pure-play decarbonization emphasis ("Reduce" module; deployable as connected platform or modules in existing ecosystem) | abatement-economics-first: finance-grade project modeling, MACC, carbon-price scenarios | global enterprise, heavy industry (Siemens Energy, ArcelorMittal, Harley-Davidson, Emirates, Natura) |
| Persefoni | carbon-accounting suite with a decarbonization module (Net-Zero Navigator) | ledger-first vendor extending forward from the Footprint Ledger; lever library via Bain partnership | enterprise + financial services |
| Sweep | enterprise carbon platform with a dedicated Decarbonization Strategy solution | data-platform-first: targets + initiatives + AI scenarios + budget modeling on one data spine | large enterprise (L'Oréal, Sanofi, Swisscom, SSE, Engie) |
| Normative | target-setting-led, advisor-coupled mid-market platform | SBTi-validation-first: named Climate Strategy Advisors + platform reduction scenario analysis | mid-market/European (Flying Tiger, Vodafone, Hitachi Rail, SEB) |
| Futureproofed (part of Sweco) | integrated climate action planning (Cities) + business carbon management | plan-first for cities (mitigation + adaptation measures in one climate plan); consultancy-coupled SaaS | cities/municipalities (EU) + mid-market business |
| IBM Envizi | enterprise ESG suite "Decarbonization" module family | energy-data-led: utility/interval analytics + Planning Analytics + Sustainability Program Tracking | large/complex organizations |

ClimateView/ClimateOS (municipal transition planning) attempted again this pass — transport error (second failure across passes; also failed in the climate-adaptation pass). Abandoned per network rules; recorded as a sourcing limitation. The municipal pole is therefore evidenced only through Futureproofed.

## Sources

All fetched 2026-09-07:

- SINAI — https://www.sinai.com/ (root: platform modules Measure/Engage/Report/Reduce; Verdantix capability circles; "1,534 decarbonization projects modeled")
- SINAI Reduce — https://www.sinai.com/platform/reduce (full feature set: project financial modeling, interactive MACC, roadmaps, target setting, tracking, carbon pricing, FAQ)
- Persefoni — https://www.persefoni.com/business/decarbonization-management (Net-Zero Navigator; Bain levers; scenarios; progress tracking)
- Sweep — https://www.sweep.net/ (root: solutions incl. Decarbonization Strategy)
- Sweep Decarbonization Strategy — https://www.sweep.net/decarbonization-strategy (targets, initiative templates, AI scenario modeling, MAC curve, budget view, FAQ; Climate Contribution Framework)
- Normative — https://normative.io/ (root: carbon accounting positioning, Climate Strategy Advisor)
- Normative SBTi — https://normative.io/platform/sbti/ (target development service; platform "reduction scenario analysis")
- Futureproofed — https://www.futureproofed.com/products/business (business platform: footprint, SBTi, hotspots, reporting; roadmap as service)
- Futureproofed Cities surfaces — https://www.futureproofed.com/products/cities (referenced on business page: flexible climate plan, measures database incl. mitigation + adaptation, public page; full observation recorded in research/climate-adaptation-planning.md, fetched same date)
- IBM Envizi Decarbonization — https://www.ibm.com/products/envizi/decarbonization (module family: Planning Analytics, Utility Bill Analytics, Interval Meter Analytics, Sustainability Program Tracking)

Sourcing limitations:

- No public help-center / user-manual documentation was reachable for any sampled product; all evidence is from official product/marketing surfaces (Tier 2) plus one prior-pass observation set (Futureproofed Cities, fetched 2026-09-07). Per evidence rules: no precise numeric claims are promoted to the final document; vendor stats (SINAI's 1,534 projects / 50-project MACC example / 2050 horizon; Normative's 349,000 factors / 100% SBTi approval; Sweep's Scope 3 share claims) stay in these notes as vendor claims.
- ClimateView unreachable ×2 across two passes — the dedicated municipal transition-planning pole is unsampled; no claims made about it.
- Prior-pass context used: research/carbon-accounting-platform.md and research/climate-adaptation-planning.md (both fetched 2026-09-07) for boundary alignment.

## Product Observations

### SINAI (Reduce module) — Evidence layer A (direct, official product pages)

- Positioning: "Enterprise carbon management from audit-grade measurement to profitable decarbonization, deployed as one connected platform or integrated into the systems you already use." Modules: Measure / Engage / Report / **Reduce** ("Decarbonization planning and reduction pathways").
- Reduce hero: "Prioritize reduction projects with financial confidence. Model projected costs, savings, emissions impact, and ROI assumptions to compare high-value decarbonization opportunities and align plans with targets, owners, forecasts, and actual performance."
- Feature set (named): Project Financial Modeling (CAPEX, OPEX, returns; NPV, IRR, payback, profitability index); Interactive Marginal Abatement Cost Curve (MACC) — "compare projects by $/tCO2 and ROI"; portfolio view "supports capital allocation and executive alignment"; Facility Level Planning ("define where decarbonization happens"); Decarbonization Implementation Plan ("translate analysis into execution steps"); Decarbonization Roadmaps — Scenario Modeling ("compare outcomes against targets and budgets"); Decarbonization Strategy ("align cross-functional decisions and sequencing"); Reduction Project Tracking ("monitor status, ownership, and realized impact"); Target Setting (Custom, SBTi); Carbon Pricing ("evaluate project economics under different assumptions"; "stress-test economics under policy and pricing scenarios").
- Workflow language: "Identify cost-effective abatement opportunities with finance-grade ROI metrics. Align sustainability, finance, and operations on what to fund next. Track execution and compare planned outcomes with realized emissions reductions and cost savings over time. Compare scenarios under different carbon-price futures. Connect facility-level execution to corporate roadmaps."
- FAQ: "Teams can plan projects by facility, assign owners, manage timelines, track status, and turn a climate transition action plan into measurable implementation." "SINAI Reduce models emissions and financial outcomes in the same planning environment."
- Data spine: "Every module runs on the same audit-ready emissions data, so your footprint, your disclosures, and your reduction plan never fall out of sync."
- Verdantix capability circles (vendor-published): Decarbonization Programme Management — MACC modelling (full), Abatement opportunity identification & implementation (full); Decarbonization Strategy Development — Transition risk analysis (full), Target management (full).
- Vendor stats (marketing claims, notes only): 1,534 decarbonization projects modeled; 50 projects in one MACC example; 2050 forecast horizon supported; 560M+ tonnes tracked; 100K+ emission factors.
- Services: in-house climate advisors for "GHG screening, target setting, climate transition planning, roadmap development, and implementation support."

### Persefoni (Decarbonization Management / Net-Zero Navigator) — Evidence layer A (direct, official product page)

- Positioning: "Create decarbonization strategies tailored to your business." "Persefoni's Net-Zero Navigator helps you find the highest impact actions to reach your reduction targets, customized to your business, industry, and priorities."
- Built "on top of Bain's industry-specific decarbonization levers and deep net-zero expertise" — a curated lever library underlies recommendations.
- Three-step narrative: (1) "Find the best reduction strategies… build an actionable decarbonization plan." (2) "Customize your decarbonization plan. Generate decarbonization scenarios and recommendations based on your industry, emissions data, and target goals. Then track your progress against science-based and other reduction targets." (3) "Meet your reduction targets. Having both your emissions data and decarbonization plan in Persefoni gives you immediate feedback on the impact of your reduction actions."
- Key structural facts: the plan is generated from emissions data + target goals + industry; scenarios and recommendations are product outputs; progress is tracked against targets; the emissions data and the plan live in the same product ("immediate feedback").
- A parallel Financial Services Decarbonization Management page exists (portfolio-side pole; not fetched this pass).
- From the carbon-accounting pass (same vendor, fetched 2026-09-07): Measure/Report/Decarbonize framing; net-zero target setting, reduction modeling, supplier engagement listed under Decarbonization.

### Sweep (Decarbonization Strategy solution) — Evidence layer A (direct, official product page)

- Positioning: "Plan, run, and track emissions reductions that hold up to financial scrutiny." "Sweep connects carbon accounting to target-setting, initiative planning, and financial modeling, so every decision is grounded in real emissions data rather than generic benchmarks."
- Four capability blocks: Hotspot identification ("highest-emission activities across Scope 1, 2, and 3… so your reduction plan targets the right levers"); Ready-made initiative templates ("built-in library of SBTi-aligned initiatives, then adapt to your operations and emissions profile"); AI-powered scenario modeling ("multi-year simulations… Test assumptions and initiatives, before you make changes"); Collaboration and progress tracking ("Assign initiatives, engage suppliers, and track progress together").
- "From target to delivered tonne, in one platform" — three pillars:
  - Set financial-grade targets: absolute and intensity targets (economic and physical), SBTi alignment, "top-down or bottom-up target consolidation across scopes, regions, and entities", "reductions aligned to your business forecast so every target is defendable".
  - Model with accuracy: "multi-year simulations on real forecasts and track delivery against the strategy you committed to"; AI-assisted forecasts/scenarios; "bottom-up and top-down execution with dependencies"; "real-time tracking of initiative progress".
  - Plan against your budget: "Set initiatives that combine carbon and budgets"; "Library of SBTi-aligned initiative templates"; "Year-by-year CapEx and OpEx modeling"; "Built-in MAC curve view to rank initiatives"; "Budget view across the full initiative portfolio".
- FAQ defines the category: "Decarbonization software enables businesses to measure their carbon footprint, plan emissions reductions, and track progress toward net zero targets." MAC analysis: "prioritize decarbonization initiatives using Marginal Abatement Cost (MAC) analysis… modeling the financial impact of actions such as switching to renewable energy, changing suppliers, or reducing energy use."
- Climate Contribution Framework (vendor-led, with Mirova Research Center, I Care by BearingPoint, Winrock): Reduce (value-chain decarbonization) / Scale (low-carbon solutions) / Finance (capital toward climate projects and credits beyond the value chain) — explicit separation of within-value-chain reduction from beyond-value-chain contribution.

### Normative — Evidence layer A (direct, official pages)

- Root positioning is carbon accounting ("Get carbon accounting right the first time… Numbers you can defend in any room and build your net zero plan around").
- The reduction-planning surface is target-led and advisor-coupled: SBTi Support service (fundamentals workshop → inventory alignment workshop → targets development workshops testing "ambition levels against SBTi pathways" → submission form completion → reviewer-query support). Platform FAQ: "The service is underpinned by the Normative platform, including GHG Protocol-compliant carbon calculations, **reduction scenario analysis**, and 349,000+ emission factors."
- Named Climate Strategy Advisor on every account (GHG Protocol-certified); vendor claims 100% SBTi approval rate.
- No self-serve MACC/project-portfolio machinery is presented on the fetched pages — the planning depth visible publicly is targets + scenario analysis + expert services. Kept product-specific.

### Futureproofed (part of Sweco) — Evidence layer A (direct, official pages; Cities detail from same-date prior pass)

- Business platform: "measure, reduce and report with ease" — carbon footprint calculation (foundation for the roadmap), streamlined data collection with audit trail, hotspot insights per business unit and site, SBTi target setting (with official validation support), reporting. Carbon reduction roadmap is offered as a **consulting service** ("Build a strategic plan outlining actionable steps to reduce carbon emissions") alongside SBTi target setting, SDG/co-benefit analysis, stakeholder engagement.
- Cities platform (from research/climate-adaptation-planning.md, fetched 2026-09-07): "Calculate your carbon footprint and build, manage, and share your climate plan"; flexible climate plan creation; database of measures and actions explicitly covering **mitigation and adaptation**; prioritization by costs and (co-)benefits; progress tracking with audit log; public transparency page; group app for multi-city aggregation.
- Structural significance: one vendor carries the corporate carbon-management pole and the municipal climate-action-plan pole; in the Cities product, mitigation (decarbonization) is one measures domain beside adaptation inside a single climate plan — direct evidence for the structural-twin seam.

### IBM Envizi (Decarbonization module family) — Evidence layer A (direct, official product page)

- Positioning: "Consolidate energy data and drive improved energy management across your organization… facilitates the ongoing monitoring, analysis, management and reporting of energy and emissions across large and complex organizations."
- "Planning and forecasting tools also enable users to conduct emissions planning and simulation, run optimization models, and carry out performance simulations."
- Key features: visualization/reporting, integrated regression tools, planning and forecasting tools, alerting and issue management, automated data capture and validation.
- Benefits: plan for performance ("forecast and model ESG performance with a range of planning tools from entry-level to advanced"); track ESG initiatives ("Track ESG and sustainability initiatives, compare projects across your portfolio"); inform decisions ("prioritizing activities and investments based on analysis of benchmarking and savings potential").
- Modules: Planning Analytics (ESG planning/forecasting "as part of a whole-of-business, integrated planning suite"); Utility Bill Analytics; Interval Meter Analytics; Sustainability Program Tracking ("Track and manage ESG and sustainability initiatives to ensure program outcomes are achieved on time and within budget").
- Structural significance: at the enterprise-suite pole, "decarbonization" is realized as energy-data-driven planning + program tracking rather than MACC-centric abatement economics — evidence for the energy-led variant and for the seam against energy management.

## Cross-product Comparison

| Dimension | SINAI Reduce | Persefoni NZ Navigator | Sweep Decarb Strategy | Normative | Futureproofed | Envizi Decarbonization |
|---|---|---|---|---|---|---|
| Emissions anchor | same-platform audit-ready data ("modules never fall out of sync") | "your emissions data" in-product | "real emissions data rather than generic benchmarks" | GHG inventory (platform) | carbon footprint as "foundation for your roadmap" | energy/emissions data (suite) |
| Target machinery | Target Setting (Custom, SBTi) | science-based + other targets | absolute + intensity, SBTi, top-down/bottom-up consolidation | SBTi target development (advisor-led) | SBTi alignment + validation support | target setting + tracking (prior pass) |
| Lever/project object | reduction projects (status, ownership, realized impact) | decarbonization levers (Bain library) | initiatives (SBTi-aligned templates; dependencies) | not directly observed as object | measures + actions (cities; mitigation + adaptation database) | initiatives/projects tracked across portfolio |
| Financial modeling | CAPEX/OPEX, NPV, IRR, payback, profitability index | not observed on page | year-by-year CapEx/OpEx; budget view across portfolio | not observed | investment needs/return (cities) | savings potential, benchmarking |
| Prioritization | interactive MACC ($/tCO2, ROI); AI-recommended | "highest impact actions" | built-in MAC curve view to rank initiatives | advisor judgment | cost + (co-)benefits comparison | benchmarking + savings potential |
| Scenario/pathway modeling | scenario modeling; carbon-price futures | decarbonization scenarios from industry + emissions + goals | multi-year AI simulations on real forecasts | "reduction scenario analysis" (platform) | not on business page | planning/forecasting, optimization models, performance simulations |
| Implementation tracking | Reduction Project Tracking; planned vs realized | progress vs targets | real-time initiative progress; delivery vs committed strategy | advisor-supported | progress tracking + audit log (cities) | Sustainability Program Tracking (on time, within budget) |
| Multi-level structure | facility-level planning → corporate roadmaps | — | scopes/regions/entities roll-up | — | per business unit and site (business); group app (cities) | portfolio → facility → sub-meter |
| Public transparency | — | — | — | — | public plan page (cities) | — |
| Adaptation content | no | no | no | no | yes (cities: mitigation + adaptation in one plan) | no |
| Carrier | connected platform or modules in existing ecosystem | carbon-accounting suite module | carbon platform solution | accounting platform + advisor services | standalone SaaS + consultancy | enterprise ESG suite module family |

### Stable commonalities (cross-product, layer B)

1. **Emissions evidence as the anchor** — the plan is built on the organization's own measured emissions and hotspots, explicitly contrasted with "generic benchmarks" (Sweep's wording; SINAI's shared-data-spine framing; Persefoni's "based on your… emissions data"; Futureproofed's "foundation for your roadmap"; Normative's inventory-alignment workshop; Envizi's energy/emissions data). The anchor may be computed in-product, imported from a carbon accounting system, or assessed with advisors — the anchor itself is invariant, its source is not.
2. **Reduction ambition as the plan's orientation** — every product frames the plan as the way from today's emissions to stated reduction goals (SBTi or custom; near-term/net-zero; absolute/intensity). The formal target machinery (validation, target types, consolidation) is common mature structure; the goal-orientation of the plan is constitutive.
3. **Discrete reduction levers/projects/initiatives as managed records** — identified, attributable units of reduction action, sourced from curated libraries/templates (Sweep SBTi-aligned templates, Persefoni/Bain levers, Futureproofed measures database) or authored custom, carrying abatement and cost attributes and (where tracked) owner/status/timeline. Five of six directly observed; Normative's public pages do not expose the object (gap noted).
4. **Recorded implementation progress over time** — status/ownership maintained between sessions and reporting cycles; planned outcomes compared with realized reductions (SINAI, Sweep, Persefoni, Futureproofed, Envizi). Every sampled product maintains state; none is a one-shot plan document.
5. **Prioritization support** — comparing levers by cost and impact (MACC at SINAI/Sweep; cost/co-benefit at Futureproofed; savings potential at Envizi; "highest impact" at Persefoni). Common; depth and formalism vary.
6. **Scenario/pathway modeling** — multi-year simulation of lever mixes against targets, with carbon-price sensitivity at the finance-grade pole (SINAI, Sweep, Persefoni, Envizi, Normative's scenario analysis). Common; absent from Futureproofed's fetched business page.
7. **Multi-level structure** — facility/site/entity-level planning rolling up to the corporate roadmap (SINAI, Sweep, Envizi, Futureproofed-cities group app).
8. **Cross-functional collaboration** — sustainability + finance + operations alignment is the stated purpose of the financial machinery (SINAI "align sustainability, finance, and operations on what to fund next"; Sweep "align sustainability and finance").

### Product-specific / weaker-evidence observations

- MACC as a named first-class view: directly observed at SINAI and Sweep only. Treat MACC as a common implementation of prioritization, not a definitional structure.
- Carbon-price sensitivity: directly observed at SINAI; implied in Sweep's budget/forecast framing. Common at the finance-grade pole; not universal.
- AI-shaped forecasting/scenarios: Sweep (AI-powered scenario modeling), SINAI (AI-recommended projects). Era-current; not definitional.
- Advisor/consultancy coupling: Normative (named advisors), Futureproofed (Sweco consultants; roadmap as a service), SINAI (climate advisors). A delivery-posture variant, not a structure.
- Public transparency page: municipal pole only (Futureproofed Cities).
- Beyond-value-chain contribution framing: Sweep's Climate Contribution Framework explicitly separates Reduce (value chain) from Finance (credits/capital beyond the value chain) — useful boundary evidence against Carbon Credit Management.
- Normative's in-platform planning machinery beyond "reduction scenario analysis" could not be verified from public pages.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A Decarbonization Planning Platform is recognizable only if all of the following hold:

```text
Emissions evidence (the organization's own measured emissions — baseline/hotspots;
  computed in-product, imported from carbon accounting, or assessed externally)
        ↓ anchors
A decarbonization plan — persistent, structured, organization-owned artifact
  organized over time toward a stated reduction ambition
        ↓ composed of
Discrete reduction levers / projects / initiatives
  (identified, attributable; sourced from libraries/templates or authored custom;
  carrying abatement and cost attributes)
        ↓ tracked through
Recorded implementation progress over time
  (status/owners maintained; planned vs realized against the plan's ambition)
```

Four properties. Removal test:

- Remove the emissions anchor → generic strategy-execution / project-portfolio software (a different Type; the machinery-first pole is known from the climate-adaptation pass and confirmed by the market's own "real emissions data, not generic benchmarks" framing).
- Remove the plan artifact (keep hotspot analytics only) → emissions analytics, not planning.
- Remove discrete managed levers (keep targets only) → target-setting/disclosure tooling.
- Remove progress tracking → a one-shot plan document/consulting deliverable; every observed commercial implementation maintains state over time.

Historical/regional check: the definition holds for pre-SBTi, pre-MACC practice — early corporate and municipal climate action plans built on emissions inventories with lists of measures, timelines, and progress reporting satisfy all four properties without science-based target machinery, abatement-cost curves, AI, or cloud delivery. SBTi validation, MACC economics, and scenario engines are modern-market commonalities, not invariants. The municipal climate-plan tradition (plan-first, measures databases, public reporting) also satisfies the core.

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- formal target machinery: SBTi alignment/validation support, absolute and intensity targets, near-term and net-zero horizons, top-down/bottom-up target consolidation across scopes/regions/entities
- financial modeling of levers: CAPEX/OPEX, NPV/IRR/payback-class investment metrics, cost per tonne abated
- abatement-cost prioritization (MACC-class views ranking levers by cost-effectiveness)
- scenario/pathway modeling: multi-year simulations of lever mixes against targets; carbon-price sensitivity at the finance-grade pole
- lever/initiative libraries and templates (SBTi-aligned initiative catalogs, industry lever libraries, measures databases)
- hotspot analysis guiding lever selection
- facility/site/entity-level planning with roll-up to the corporate roadmap
- progress dashboards: planned vs realized, forecasts, alerts
- cross-departmental collaboration and assignment (sustainability/finance/operations)
- transition-plan / climate-transition-plan reporting outputs feeding disclosure

### L2 — Variant / Optional Structure

- content-domain scope: mitigation-only vs integrated climate action plan carrying mitigation beside adaptation (municipal pole; observed at Futureproofed Cities)
- planning philosophy: abatement-economics-led (MACC/finance-grade) vs target-led (SBTi/advisor-coupled) vs energy-led (utility-bill/interval-data analytics + program tracking) vs plan-led (municipal climate plan with measures database and public page)
- customer segment: enterprise heavy industry vs mid-market vs cities/municipalities
- carrier: standalone module deployable into an existing ecosystem vs carbon-accounting suite member vs enterprise ESG suite module family vs consultancy-coupled SaaS
- supplier/value-chain decarbonization engagement programs
- beyond-value-chain contribution (credits, climate financing) as an adjacent extension
- public transparency surfaces (municipal)
- AI assistance (scenario shaping, project recommendation) — era-current
- regional/regulatory framing of targets and disclosure inputs

### L3 — Vendor-specific (kept out of the final document)

- SINAI: "Reduce" module naming; vendor stats (1,534 projects modeled, 50-project MACC example, 2050 horizon, 560M+ tonnes, 100K+ factors); Verdantix capability-circle claims; climate-advisor services packaging.
- Persefoni: Net-Zero Navigator branding; Bain & Company lever partnership; PersefoniAI; Financial Services decarbonization line.
- Sweep: Climate Contribution Framework (Reduce/Scale/Finance; developed with Mirova Research Center, I Care by BearingPoint, Winrock; shaped by Orange, Schneider Electric, EDF, Renault, Veolia); SBTi-aligned initiative template library; AI scenario modeling branding; analyst-report claims (IDC MarketScape, Verdantix).
- Normative: named GHGP-certified Climate Strategy Advisor model; 349,000+ emission factors; TÜV SÜD verification; 100% SBTi approval claim; Essential/Premium plan gating.
- Futureproofed: Sweco group ownership; city climate coaches; group app; Genvision sequestration integration; public page mechanics (detail in the adaptation pass notes).
- Envizi: module names (Planning Analytics, Utility Bill Analytics, Interval Meter Analytics, Sustainability Program Tracking); IBM integrated planning-suite linkage; IDC positioning claims.

## Rejected Findings (considered, not promoted)

- "A decarbonization platform must compute the emissions inventory itself" — rejected: the anchor can be imported or advisor-assessed; what is invariant is that the plan is anchored to the organization's own measured emissions, not the computation site.
- "MACC curves are the defining structure" — rejected: named MACC views observed at two of six products; prioritization is the invariant, MACC is one common implementation.
- "SBTi targets are definitional" — rejected: custom targets and pre-SBTi-era plans satisfy the core; SBTi machinery is common mature structure.
- "Decarbonization planning is only corporate" — rejected: the municipal climate-action-plan pole (Futureproofed Cities; ClimateView-class products) shares the same loop with a public-accountability surface.
- "Scenario modeling is definitional" — rejected: absent from Futureproofed's fetched business page and thin at Normative; common mature, not invariant.
- "Planning requires in-product carbon accounting" — rejected: SINAI explicitly markets module deployment into existing ecosystems; the data spine can live elsewhere.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| Carbon Accounting Platform | complementary halves, commonly one suite | accounting's defining loop ends at a measured, auditable inventory of record (backward-looking); this Type's defining loop starts from that inventory and governs the forward reduction program. Remove the plan/levers/tracking → carbon accounting; remove the inventory-of-record discipline → this Type. All sampled carbon platforms add planning as an extension; every sampled planning carrier anchors on emissions data — bidirectional adjacency, center-of-gravity seam. |
| Climate Adaptation Planning | structural twin (flag discharged this pass) | identical planning loop (evidence → plan artifact → discrete actions → tracked implementation → monitoring feeding revision); the content domain differs: emissions sources and reduction levers vs climate hazards and adaptive capacity. The market commonly carries both domains in one integrated climate-plan product (directly observed at Futureproofed Cities: mitigation and adaptation measures in one plan). Seam test: replace the emissions anchor with a hazard anchor → adaptation planning; vice versa → this Type. Keep-both ratified with the content-domain seam. |
| Climate Risk Management | adjacent (risk loop) | CRM keeps a risk process alive over an exposure population (assessments, prioritization, disclosure); this Type governs a reduction program over emission sources. Response-option evaluation appears in both; the managed plan/levers/progress structure belongs here. |
| Climate Scenario Analysis | upstream machinery | scenario projection machinery (futures compared, not forecasts); no managed plan or levers. This Type consumes scenario-class machinery (carbon-price futures, transition pathways) as one capability. |
| Energy & Carbon Management (§21, unprocessed) | adjacent — seam flagged for joint review | energy-first Types center consumption data and operational optimization; this Type centers the strategic reduction program. The Envizi pole (utility/interval analytics + program tracking inside one suite) shows the blend is real; the seam is the managed plan/program object vs operational energy management. Apply the program-object test when that leaf is processed. |
| Building Energy Management | adjacent | building-scoped operational energy (metering, control, HVAC); no organization-wide reduction program object. |
| Sustainability / ESG Management Platform | broader | center-of-gravity test: ESG suites manage wider environmental/social/governance data and disclosure; this Type's center is the emissions-reduction program. |
| Carbon Credit Management / Carbon Trading | adjacent (beyond value chain) | credits are beyond-value-chain instruments with registries and retirement; this Type governs within-value-chain abatement. Sweep's Climate Contribution Framework explicitly separates the two (Reduce vs Finance). |
| Strategic Plan Execution / Government Performance Management | carrier / generic machinery | identical plan→actions→measures→dashboard loop without emissions content (machinery-first pole established in the climate-adaptation pass). The emissions anchor is the Type boundary. |
| Energy Management System (§19) / Demand Response | adjacent | grid/asset-side operational optimization; not an organization's strategic abatement program. |
| Product Carbon Footprint / LCA | adjacent | unit of account is the product, not the organization's reduction program. |

Boundary judgments (removal test):

- Remove the emissions anchor → generic strategy-execution machinery.
- Replace the emissions anchor with a hazard anchor → Climate Adaptation Planning (twin).
- Remove the plan/levers/tracking, keep measurement → Carbon Accounting Platform.
- Remove the plan object, keep hotspot analytics → emissions analytics.
- Remove within-value-chain scope, keep instruments → Carbon Credit Management.

## Structural-Twin Flag Discharge (climate-adaptation-planning joint review)

The flag recorded by the adaptation pass is **discharged from this side**: keep-both ratified with the content-domain seam.

- Both passes independently arrived at the same four-property loop (evidence anchor → plan artifact → discrete actions → tracked implementation), differing only in the anchor's content domain.
- Direct market evidence for the seam: Futureproofed Cities carries mitigation and adaptation as measures domains of one climate plan; corporate carbon platforms (SINAI, Sweep, Persefoni, Envizi, Normative) carry mitigation only.
- Consolidation into one "climate action planning" Type was considered and rejected: the two domains have different evidence machinery (emissions inventories vs hazard/vulnerability analytics), different professional communities (carbon/sustainability vs risk/resilience planning), different market carriers (carbon-management suites vs risk analytics + public-sector planning tools), and the directory already treats them as separate leaves with distinct neighbors. The content-domain seam is the load-bearing distinction, exactly as the adaptation pass framed it.
- Secondary note stands: both Types are partially carryable by generic plan-execution machinery (Envisio pole); when strategic-plan-execution / government-performance-management leaves are processed, apply the content-anchor test (emissions or hazard anchor present → climate planning Type; absent → generic machinery).

## Uncertainties

1. Deep operational documentation (help centers, manuals) was not reachable for any sampled product; all evidence is from official product/marketing surfaces. Workflow internals (exact lever states, approval flows, revision mechanics, baseline-reconciliation behavior) are therefore stated at moderate strength only.
2. ClimateView/ClimateOS (dedicated municipal transition planning) unreachable in two passes; the municipal pole rests on Futureproofed alone. The plan-led municipal variant is claimed at common-pattern strength, not universal.
3. Normative's in-platform planning depth beyond "reduction scenario analysis" is not directly observed; its planning surface is advisor-led. Kept product-specific.
4. Persefoni's Net-Zero Navigator internals (plan object structure, scenario mechanics) are not directly observed beyond the page narrative.
5. Whether a standalone pure-play decarbonization planner exists with no carbon accounting at all is unverified; SINAI's "modules within your existing enterprise ecosystem" wording suggests module-only deployment is possible but does not document it.
6. Envizi's Planning Analytics depth (optimization models, performance simulations) is described only at marketing level; no operational detail claimed.
7. Vendor numeric claims (project counts, factor counts, approval rates, horizon support) are marketing figures recorded here only; none promoted to the final document.

## Final Synthesis

A Decarbonization Planning Platform is an organization's system for planning and governing emissions reduction. Its defining loop: anchor on the organization's own measured emissions (baseline and hotspots — computed in-product, imported from carbon accounting, or advisor-assessed) → organize a persistent plan/pathway toward stated reduction ambitions → compose the plan from discrete reduction levers/projects (library-sourced or custom, carrying abatement and cost attributes) → prioritize and stress-test them with abatement economics and scenarios → track implementation with recorded status and owners, comparing planned against realized reductions on the way to the target trajectory. The defining core is the emissions-anchored plan-levers-progress loop; target machinery (SBTi, absolute/intensity, consolidation), financial modeling, MACC-class prioritization, scenario engines, lever libraries, and dashboards are the common mature structure; integrated mitigation+adaptation climate plans, energy-led and advisor-led realizations, and municipal public-transparency surfaces are variants. The Type is bounded against carbon accounting (backward vs forward), climate adaptation planning (structural twin — same loop, hazard anchor), climate risk/scenario machinery (evidence and modeling without a managed program), energy management (operational optimization vs strategic program), generic plan-execution machinery (no emissions anchor), and carbon credits (beyond vs within the value chain).
