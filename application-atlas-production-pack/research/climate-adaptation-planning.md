# Research Notes — Climate Adaptation Planning

Research date: 2026-09-07

## Research Goal

Understand what "Climate Adaptation Planning" software actually is in the market: who builds and operates it, what core objects it manages, how the adaptation planning workflow runs inside it, and where its boundaries lie against physical climate risk analytics, scenario analysis, decarbonization planning, emergency/continuity management, and generic public-sector plan-execution software.

## Initial Boundary (hypothesis before research)

- What: software to produce and manage a climate adaptation plan — hazard/vulnerability assessment → adaptation options → prioritized roadmap → implementation tracking → monitoring & evaluation.
- Users: municipalities/regional governments, public agencies, utilities/infrastructure owners, land managers, corporate ESG/operations teams.
- Most likely confusions: Physical Climate Risk Platform (evidence production, no plan object), Climate Scenario Analysis (modeling), Decarbonization Planning Platform (mitigation twin with the same loop shape), generic strategic plan-execution platforms (machinery without climate content), Emergency Management (event response), knowledge portals (guidance without a managed plan).
- Unknowns: whether dedicated "adaptation planning" products exist at commercial scale, or whether the Type is carried by (a) integrated climate-action platforms, (b) generic plan-execution platforms, (c) free government tools, (d) risk-analytics platforms' adaptation features.

## Research Questions

1. What is the central managed object — the plan? What is its internal structure (themes/goals/measures/actions)?
2. How do hazard/risk/vulnerability inputs enter the system — embedded data, imported studies, external analytics?
3. What does an adaptation action/measure look like (attributes, sources, linkage to risks)?
4. How is prioritization done (cost-benefit, co-benefits, urgency, feasibility)?
5. What is the lifecycle of the plan (draft → adopt → implement → monitor → revise)? How do monitoring/evaluation close the loop?
6. What roles participate (planners, department owners, executives, citizens, higher government tiers, consultants)?
7. What interfaces exist (plan builder, libraries, maps, dashboards, public pages, reports)?
8. How does adaptation coexist with mitigation in one product?
9. Which surrounding Types feed or consume this Type?

## Representative Products (sample rationale)

| Product | Pole | Philosophy | Customer level |
|---|---|---|---|
| Futureproofed (part of Sweco) | integrated municipal climate-action planning SaaS | plan-first: build/manage/share climate plan incl. adaptation measures | cities & municipalities (EU), also business platform |
| XDI (Cross Dependency Initiative) | physical climate risk analytics with adaptation decision support | risk-first: quantify asset risk, explore adaptation pathways & cost-benefit | financial institutions, governments, corporates (global) |
| Envisio | generic public-sector strategy execution carrying climate plans | machinery-first: plan→goals→actions→measures→dashboards | local government, utilities, education, health (NA/AU) |
| Adaptation Workbook (NIACS / USDA Climate Hubs) | methodology-embedded online planning tool for land management | process-first: guided workbook producing a custom adaptation plan | land owners/managers, foresters, farmers (US, free) |
| Climate-ADAPT + Adaptation Support Tool (EEA/EU) | public knowledge/guidance portal structuring the planning cycle | knowledge-first: process guidance, no managed plan object | national/subnational policymakers, urban practitioners (EU, free) |

One Concern was initially sampled as an enterprise resilience-platform candidate; official pages show it now positions as climate-risk-to-financial-risk analytics (business interruption, digital twin) — recorded as Product Mismatch / boundary evidence, not as a representative of this Type. ClimateView/ClimateOS (municipal transition planning) was attempted but unreachable (transport error, not retried per network rules) — market context only, no claims.

## Sources

All fetched 2026-09-07:

- Futureproofed — https://www.futureproofed.com/ (root: products, services, cases)
- Futureproofed for Cities — https://www.futureproofed.com/products/cities (plan creation, measures/actions, prioritization, reporting, public page, group app)
- XDI — https://xdi.systems/ (solutions overview, sectors, use cases)
- XDI — https://xdi.systems/solutions/resilience ("Engage clients on a pathway to resilience", adaptation pathways, AdaptXDI)
- One Concern — https://www.oneconcern.com/ (boundary evidence: financial-risk positioning)
- Envisio — https://www.envisio.com/ (solutions, dashboards incl. City of Rockville Climate Action Plan dashboard, customers)
- Adaptation Workbook — https://adaptationworkbook.org/ (home: impacts explorer, menus, training)
- Adaptation Workbook — https://adaptationworkbook.org/how-to-use (full process, outputs, formats)
- Climate-ADAPT — https://climate-adapt.eea.europa.eu/ (Adaptation Support Tool, 6-step cycle, Urban AST, country profiles, sector policies)
- ClimateView — https://climateview.com/ (fetch failed; not used)

Sourcing limitation: all reachable pages are product/marketing surfaces plus one official guidance tool. Deep help-center / user-manual documentation was not reachable in this pass. Per evidence rules: no precise numeric claims (deadlines, counts, horizons, defaults) are made anywhere; cross-product findings are stated at commonality strength; single-product observations remain product-specific.

## Product Observations

### Futureproofed (Cities platform) — Evidence layer A (direct, official product pages)

- Positioning: "Calculate your carbon footprint and build, manage, and share your climate plan with ease and confidence." Two platforms: For Business (carbon management) and For Cities (climate plan for municipalities).
- Plan object: "Flexible climate plan creation — craft adaptable climate action strategies"; "Design individual plans or group them in line with your objectives. Time for change? Adapt and tailor your plans as you advance." → the plan is a persistent, editable, structured artifact.
- Measures/actions structure: "Choose from our list of measures, add custom measures to match your objectives, consider their impact and co-benefits and support them with actions." → curated measure library + custom measures; measures supported by implementation actions.
- Prioritization: "compare costs and (co-)benefits and prioritize actions"; "Understand the financial investment needs and return potential of individual measures or the climate plans as a whole to prioritise high impact, high return actions."
- Adaptation content: "Database of measures and actions — easy-to-use database of mitigation and adaptation measures." Adaptation is one content domain of the climate plan alongside mitigation (the product headline is net-zero/CO2-centric; a services page offers "Risk and vulnerability assessment"; blog titles cover city adaptation strategies and adaptation-measure financing).
- Tracking/reporting: "Report transparently on your progress"; audit log and verification features; dashboards tracking city initiatives; testimonial: "keeping a close eye on the progress of our municipality in the Climate Plan... actions and measures implemented, their impact."
- Public transparency: "Public page — automatically publish your climate plan and progress to the public... or embed it in your city's website."
- Collaboration & roles: invite colleagues and stakeholders into data collection/plan co-creation; "city climate coaches" (expert services) accompany the SaaS.
- Multi-entity: "Futureproofed group app — working with a group of cities or regional organizations? ... aggregation and visualization of your group's climate activities and progress" (case: 20 municipalities in Walloon Brabant; 50 cities via WWF One Planet City Challenge).
- Assessment input: emissions inventory upload/calculation (mitigation); risk & vulnerability assessment offered as an expert service feeding CSRD-type compliance — i.e., assessment evidence partially outside the SaaS core.

### XDI — Evidence layer A (direct, official product pages)

- Positioning: "The Physical Climate Risk Experts... XDI quantifies the cost of extreme weather and climate change impacts to physical assets." Products: screening, asset-level deep dive, reporting alignment (TCFD/ISSB/EU Taxonomy), stress testing (RCP/SSP/NGFS scenarios), delivery via "Climate Risk Hub" platform, API, off-the-shelf reports.
- Adaptation support exists, risk-shaped: solution "Engage clients on a pathway to resilience" — "Use XDI's data visualisation tools to explore multiple adaptation options to reduce risk to each asset and explore the cost-benefit of different adaptation pathways." Branded analysis "AdaptXDI".
- Use cases: FMCG company wanting "cost-benefit analyses of various adaptation pathways" at asset level; Greater Cities Commission regional risk analysis "and identification of adaptation measures... to inform GCC plans and inform investment pathways"; Sydney Water exploring "adaption options" for urban heat.
- Critically: no managed plan object, no action records with owners/status, no progress tracking — the output is analysis and decision support feeding external plans and investment pathways.
- Boundary reading: XDI-style platforms produce and quantify the evidence (and test option effectiveness in the model), then adaptation *planning* software consumes it into a managed program.

### Envisio — Evidence layer A (direct, official product pages)

- Positioning: "#1 Strategic Planning Software for Public Agencies" — generic public-sector strategy execution: "Create Plans" (create, track, link, and report across all organizational plans), "Execute Strategy", "Measure Performance" (centralize performance data), "Manage Projects", "Align Budget", "Share Progress" (community dashboards).
- Structure: plans → goals → actions → performance measures; projects with time/budget; automated reports and public dashboards; department-level accountability ("it isn't me hounding people for updates... updates are required").
- Climate presence: Inspiration Gallery shows "City of Rockville, MD — Climate Action Plan Dashboard — tracks progress on key sustainability goals such as emissions reduction and renewable energy adoption"; customer list includes Sonoma Water (a water utility). Climate plans are carried by the same generic machinery.
- No climate-specific content (no hazards, no measure libraries) — the machinery is domain-neutral; adaptation planning content arrives from the organization.
- Boundary reading: the same loop (plan→actions→measures→dashboards) without climate content is a different Type; this product demonstrates the Type can be *carried* by generic public-sector plan-execution software.

### Adaptation Workbook (NIACS / USDA Climate Hubs) — Evidence layer A (direct, official how-to)

- Positioning: "a climate change tool for land management and conservation"; online, interactive, self-guided; requires a user account.
- Process (from "How to Use"): input basic project-area information and detailed management goals/objectives → the Workbook generates potential climate-change impacts for the region → user uses own judgment to consider how broad impacts play out on their particular property → decide whether goals/objectives remain robust to climate change → brainstorm and evaluate a list of custom actions → finish by developing a monitoring plan to determine whether actions were effective.
- Action content: adaptation "menus" — curated lists of adaptation actions by topic; hierarchy Strategies → Approaches → Actions ("help you move from broad ideas to specific actions").
- Output: "a detailed, customized adaptation plan for your property... organized according to your management goals and objectives... can be combined with or added to your existing plans."
- Scope humility: "not intended to provide specific guidance or replace other forms of management planning... meant to complement existing management planning and decision-making systems."
- Formats: the plan structure also exists as Word/Excel worksheets, "Quick Guide" versions, a Spanish version, and print publications — evidence the methodology predates/carries independent of the online tool (historical check).
- Monitoring: a monitoring plan is a produced artifact of the process.

### Climate-ADAPT / Adaptation Support Tool (EEA, EU) — Evidence layer A (direct, official portal)

- Positioning: "Sharing adaptation knowledge for a Climate-Resilient Europe." The Adaptation Support Tool (AST) "assist[s] policy makers and coordinators on the national level in developing, implementing, monitoring and evaluating climate change adaptation strategies and plans"; a parallel Urban Adaptation Support Tool serves urban actors.
- Canonical 6-step cycle displayed on the portal: 1. Preparing the ground for adaptation → 2. Assessing climate change risks and vulnerabilities → 3. Identifying adaptation options → 4. Assessing and selecting adaptation options → 5. Implementing adaptation → 6. Monitoring and evaluating adaptation.
- Surrounding machinery: case studies structured to "cover all the key aspects in the implementation cycle of adaptation"; country profiles with status of national adaptation actions "as reported under the Governance Regulation" (EU Member States legally required to report biennially); sector policies (19 sectors); European Climate Data Explorer; resource catalogue; AI search assistant.
- It holds no managed plan object and no per-organization action tracking — it is process guidance + knowledge + policy reporting context.
- Boundary reading: knowledge portals structure and resource the planning process; they are not planning applications, but they define the workflow vocabulary the market uses.

### One Concern — boundary evidence only (Product Mismatch)

- Official pages position the company as "Planetary-Scale Resilience Software Platform" bridging "Climate Risk to Financial Risk in Capital Markets, Insurance, and Real Estate" — quantifying business-interruption risk from infrastructure dependency with AI/digital-twin modeling. No plan object, no action management. Belongs to the physical-risk analytics neighborhood, not this Type.

## Cross-product Comparison

| Dimension | Futureproofed | XDI | Envisio | Adaptation Workbook | Climate-ADAPT AST |
|---|---|---|---|---|---|
| Central object | climate plan (plans, measures, actions) | asset risk results + adaptation option analyses | strategic plan (goals, actions, measures) | custom adaptation plan per land project | none (guidance + knowledge) |
| Hazard/risk input | service-delivered assessment; measures database incl. adaptation | core: engineering-based hazard/loss analytics | none (content-neutral machinery) | generated regional impacts + expert judgment | guidance + data explorer links |
| Action content source | curated measure database + custom | analysis outputs (not managed actions) | user-defined actions | curated adaptation menus (strategy→approach→action) | curated options guidance |
| Prioritization support | cost + benefit + co-benefits comparison | risk-reduction + cost-benefit of pathways | none inherent | evaluation of custom actions | "assessing and selecting options" step |
| Implementation tracking | yes (progress, audit log) | no | yes (status, projects, budgets) | monitoring plan artifact (self-tracked) | no (policy-level reporting only) |
| Monitoring & evaluation | progress dashboards | n/a (re-run analysis) | performance measures | monitoring plan as output | step 6 of the cycle; country reporting |
| Public transparency | public page, embed | no | community dashboards | no (demos published) | portal itself public; country profiles |
| Multi-entity aggregation | group app (regional rollup) | portfolios of assets | org-wide plans | single project | national/subnational tiers |
| Climate-specific content | yes (integrated mitigation + adaptation) | yes (hazard analytics) | no | yes (adaptation-only) | yes (adaptation knowledge) |
| Commercial / free | commercial SaaS + services | commercial analytics | commercial SaaS | free public tool | free public portal |

### Stable commonalities (cross-product)

1. The **plan as a structured, persistent, organization-owned artifact** — organized into themes/goals/objectives, holding discrete adaptation actions/measures (Futureproofed, Envisio machinery, Workbook output; the AST defines the same structure for strategies/plans).
2. **Adaptation actions as discrete managed records** — sourced from curated libraries/menus of measures or authored custom; carrying attributes such as owner, timing, cost, expected benefit (Futureproofed measures→actions; Workbook strategies→approaches→actions; AST options).
3. **An evidence step that anchors the plan in climate impacts** — hazards/risks/vulnerabilities assessed via embedded data, generated regional projections, imported studies, or expert judgment (Workbook, XDI, AST step 2; Futureproofed via services). The anchor step may live outside the planning tool.
4. **Implementation tracking with recorded progress over time** — status updates against actions (Futureproofed, Envisio; Workbook via its monitoring plan; AST steps 5–6 as process requirement).
5. **A recurring cycle including monitoring/evaluation and revision** — the AST's 6 steps, the Workbook's monitoring plan, plan editability "as you advance" (Futureproofed), Envisio's annual planning/performance rhythm. Planning is explicitly iterative (adaptive management), not one-shot.
6. **Cross-departmental / multi-stakeholder collaboration** — invite colleagues/stakeholders, distributed ownership with central coordination (Futureproofed, Envisio; AST "preparing the ground").
7. **Public accountability surfaces** — published plans/progress (Futureproofed public page; Envisio community dashboards; portal-level public reporting at EU level).

### Product-specific / weaker-evidence observations

- Integrated mitigation+adaptation in one plan object: directly observed at Futureproofed (measures database explicitly covers both; product is CO2-first). Whether all integrated climate-plan platforms weight adaptation equally is not verified — keep as common pattern with variation, not universal rule.
- Curated measure/action libraries: observed at Futureproofed (database of measures) and Workbook (menus). Envisio has none. → Common but not definitional.
- Embedded hazard analytics: observed only in the risk-analytics pole (XDI). The planning carriers observed rely on external/imported/assessed evidence. → Treating embedded analytics as optional/variant, not core.
- Financial quantification (cost-benefit, investment needs): observed at Futureproofed and XDI; Workbook uses qualitative evaluation. → Common capability, variable depth.
- Multi-entity aggregation: observed at Futureproofed (group app) and implied at EU country-profile level; not present in Workbook/Envisio single-org framing. → Common at public-sector scale, not definitional.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Climate Adaptation Planning software exists to manage, for a specific organization, the loop from climate-impact evidence to a governed program of adaptation actions:

```text
Climate hazard / risk / vulnerability evidence
  (assessed, imported, or generated — the evidentiary anchor)
        ↓ anchors
An adaptation plan — persistent, structured, organization-owned artifact
  (organized into themes / goals / objectives)
        ↓ contains
Discrete adaptation actions / measures
  (identified, attributable; sourced from libraries or authored custom)
        ↓ tracked through
Recorded implementation progress over time
  (status/owners/timing maintained between sessions and reporting cycles)
```

Four properties. Removal test:
- Remove the hazard-driven content anchor → generic strategic plan-execution software (a different Type; observed directly via the machinery-first pole).
- Remove the managed plan/action structure (keep the analytics) → physical climate risk analytics / decision-support platform (a different Type; observed directly).
- Remove discrete managed actions → a knowledge/guidance portal (a different artifact class; observed directly).
- Remove progress tracking → a one-shot plan-drafting/document tool; every observed commercial implementation maintains state over time, and the process canon (prepare→assess→identify→select→implement→monitor/evaluate) makes implementation+monitoring constitutive of "planning" as practiced.

Historical/regional check: the definition holds for pre-SaaS carriers — the Workbook's print/Word/Excel ancestry produces the same four properties as methodology artifacts; free government tools; regional portals. It does not require cloud, embedded hazard data, GIS, financial quantification, or public dashboards (all modern-market commonalities, not invariants).

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- curated measure/action libraries ("menus" of adaptation options by topic)
- prioritization support: cost, benefit, co-benefits, feasibility comparisons
- monitoring & evaluation machinery: indicators/KPIs, effectiveness review feeding plan revision
- stakeholder collaboration & task assignment across departments
- progress dashboards and report generation/export
- public transparency page/dashboard
- multi-entity / regional aggregation and rollup
- assessment module or structured import of external risk/vulnerability studies

### L2 — Variant / Optional Structure

- plan scope: adaptation-only vs integrated mitigation+adaptation climate action plan
- carrier: climate-specific platform vs generic public-sector plan-execution machinery configured with climate content vs free government tool vs methodology workbook
- evidence depth: embedded hazard data & analytics vs imported studies vs expert-judgment workflows
- sector frames: municipal/urban, national/subnational strategy, land management & conservation (project-level), utilities/infrastructure assets, corporate operations
- geographic/regulatory framing: EU Governance Regulation reporting context, Global Covenant-style commitments, national guidance cycles (varies by region; not directly evidenced per-product beyond the EU portal)
- finance/budget linkage, GIS/mapping surfaces, scenario-explorer depth
- language localization (multi-language portals/tools observed at the public poles)

### L3 — Vendor-specific (kept out of the final document)

- Futureproofed: group app naming, Genvision carbon-sequestration integration, Sweco "city climate coaches", audit-log specifics, WWF OPCC cohort.
- XDI: "AdaptXDI" branded analysis, Climate Risk Hub platform, Climate Valuation home-buyer support tools, ISO27001 platform claim, scenario menu (RCP/SSP/NGFS).
- Envisio: Polco national livability benchmarks, Rockville dashboard specifics, GovTech 100 recognition.
- Adaptation Workbook: NIACS/USDA/American Forests partnership, forest/agriculture publication DOIs, demonstration-project gallery, online course format.
- Climate-ADAPT: AI search assistant, European Climate and Health Observatory, EUCRA assessment, Discomap preparedness portals, biennial Governance Regulation reporting mechanics.

## Rejected Findings (considered, not promoted)

- "Adaptation planning software always includes hazard maps/GIS" — rejected: only implied in analytics and portals; none of the planning-carrier pages directly evidence GIS as structural.
- "Adaptation plans are 10-year/2050-horizon documents" — rejected: plausible market convention but not directly evidenced in fetched sources; no horizon numbers stated.
- "Corporate adaptation planning is a distinct enterprise Type" — rejected for now: only the analytics pole directly evidences corporate use; corporate adaptation planning appears as a use case feeding risk/disclosure workflows, not as a distinct observed product family.
- "Monitoring is optional" — rejected: monitoring/evaluation appears in every process description (including the free tools); treated as part of the common mature structure rather than the strict invariant because software realizations vary widely (indicator engines vs produced monitoring-plan documents).

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| Physical Climate Risk Platform | upstream / adjacent | quantifies hazard exposure and asset loss, supports option cost-benefit testing; has no managed plan, actions, owners, or progress. Remove the plan/actions/tracking from this Type → risk analytics. |
| Climate Risk Management | adjacent (governance loop) | enterprise risk-process framing (risk register, controls, treatment, audit) applied to climate; adaptation planning's central artifact is the public-facing, goal-structured adaptation plan rather than a risk register. Overlap is real; boundary rests on the artifact and audience. |
| Climate Scenario Analysis | input machinery | models futures under emission/socioeconomic scenarios; supplies projections; no plan or action management. |
| Decarbonization Planning Platform | structural sibling | identical planning loop; the content domain is emissions sources and reduction levers instead of climate hazards and adaptive capacity. In the market one platform often carries both domains in one climate plan (observed at Futureproofed) — the two leaves are content-domain twins, structure-wise. |
| Business Continuity Management Platform | adjacent | keeps an organization operating through disruption (procedures, recovery, continuity plans); shorter horizon, internal operations focus; adaptation planning is long-horizon adjustment of assets/policies/land to changing climate conditions. |
| Emergency Management Platform | adjacent | preparedness/response operations for hazard events (dispatch, resources, alerts); this Type plans multi-year structural adaptation before/ between events. |
| Strategic Plan Execution / Government Performance Management | carrier / generic machinery | identical plan→actions→measures→dashboard loop without climate content (observed directly). This Type = that machinery + climate-adaptation content anchor. The content anchor is the Type boundary. |
| Capital Improvement Planning (public sector) | downstream consumer | funding/budget machinery into which adaptation actions are often fed; its core object is the capital program, not the adaptation strategy. |
| Knowledge portals (e.g., adaptation knowledge platforms) | guidance, not application | structure the process and curate knowledge/case studies; hold no per-organization plan or action records. |
| Environmental Management System | broader domain | organization-wide environmental aspects/compliance management; adaptation is one possible topic, not the organizing principle. |

Boundary judgments (removal test):
- Remove the climate-hazard content anchor → strategic plan-execution / performance-management Type.
- Replace the hazard anchor with emissions anchor → decarbonization planning (structural twin).
- Remove the plan/actions/tracking, keep the analytics → physical climate risk platform.
- Remove the plan object but keep curated process knowledge → knowledge/guidance portal.

## Uncertainties

1. Deep operational documentation (help centers, manuals) was not reachable in this pass; all planning-carrier evidence comes from product/marketing surfaces. Workflow internals (e.g., exact action states, approval flows, revision mechanics) are therefore stated at moderate strength only.
2. Futureproofed's adaptation-specific depth inside the Cities platform (beyond the adaptation-measures database and services) could not be verified; the product's headline is mitigation/net-zero. Adaptation coexistence is therefore claimed as a pattern, with variation acknowledged.
3. Envisio's official marketing of climate planning was not directly verified (observed via a named customer dashboard and customer list); climate-content claims for the machinery pole are kept product-specific.
4. ClimateView/ClimateOS unreachable; no claims made about the transition-planning pole.
5. Regional/national adaptation plan platforms outside the EU/US (e.g., national NAP portals) were not sampled; the national-strategy variant rests on the EU portal evidence.
6. The corporate segment's preferred carriers (ESG suites' physical-risk modules vs dedicated tools) are not directly evidenced; kept qualitative.

## Final Synthesis

Climate Adaptation Planning is the plan-side counterpart of physical climate risk analytics: risk platforms quantify the threat; adaptation planning software governs the response. Its canonical object structure is: climate hazard/risk/vulnerability evidence anchoring an organization-owned, structured adaptation plan composed of discrete actions/measures, tracked through implementation and closed by monitoring/evaluation that feeds the next revision. The canonical workflow is the 6-step adaptive cycle (prepare → assess risks → identify options → assess/select → implement → monitor/evaluate). In the market the Type is carried by three vehicle classes — integrated climate-action platforms (often mitigation+adaptation in one plan), generic public-sector plan-execution machinery configured with climate content, and free methodology-embedded government tools — while risk-analytics platforms and knowledge portals supply the evidence and process scaffolding at the edges. The defining boundary: keep the hazard anchor, plan artifact, discrete actions, and tracked implementation; lose any one of the four and the product becomes a neighboring Type.
