# Research Notes — Government Performance Management

## Research Goal

Understand what software sold as "government performance management" actually does: what objects it manages, what loops it runs, who uses it, and how it differs from adjacent types (BI/dashboards, public budgeting, transparency/open-data portals, HR performance management, generic strategy-execution/OKR software).

## Initial Boundary (hypothesis before research)

- Core use hypothesis: public-sector organizations (cities, counties, agencies, districts) define goals/plans, decompose them into measurable indicators, collect actuals on a recurring cadence, assess status, hold management reviews, and report to leadership, governing bodies, and often the public.
- Nearest neighbors: generic strategy-execution/OKR software; BI/dashboard platforms; Public Budgeting Platform; Government Transparency Portal; Government Open Data Portal; Performance Management Platform (employee-level, HR); Monitoring & Evaluation Platform (nonprofit sector).
- Cross-reference obligation: two prior passes (climate-adaptation-planning, decarbonization-planning-platform) flagged that generic public-sector plan-execution machinery is carried by this market; the content-anchor test must be applied (climate/emissions anchor → climate planning type; absent → generic machinery).

## Research Questions

1. What is the object model: plans, goals/priorities, measures/KPIs, targets, actuals, initiatives/actions, departments?
2. How do actual values get into the system (manual entry, spreadsheet import, API/system feeds, email-in updates)?
3. How is status determined and maintained (computed evaluation rules vs manually set; RAG-style indicators)?
4. What does the review/reporting loop look like (staff meetings, stat-style reviews, council/board packets, scheduled reports, briefing books)?
5. What is government-specific here: departments as containers, fiscal-year alignment, council/legislature audiences, public transparency, measures libraries/benchmarks?
6. Where is the boundary against BI/dashboard tools, against project management, against budgeting platforms, against transparency portals, and against employee performance management?
7. Is the "government" framing definitional or an audience/market shaping of generic strategy-execution machinery?

## Representative Products

Selected for market presence in the public sector, documentation quality, and different product philosophies:

| Product | Philosophy / posture | Customer level |
|---|---|---|
| ClearPoint Strategy | Cross-industry strategy-execution scorecards (objectives/measures/initiatives); heavy local-government base; strong help center | Local gov, utilities, healthcare, finance, education |
| Envisio | Public-sector pure-play: strategic plans + performance analytics + community dashboards; measures library via Polco Track | Local gov (US + international), education, health, nonprofit |
| AchieveIt | Plan-execution management with automated update collection; government-heavy clientele incl. state/federal agencies | Local/state/federal gov, special districts, health departments |
| Neubrain | Government budgeting/analytics suite; performance measurement linked to budgets; transparency portal | Cities/counties, state agencies, federal/DoD |

Note: OpenGov and ClearGov were selected initially but their websites returned HTTP 403 to automated fetch on 2026-09-08; both were abandoned per the source-access rules. See Sources / Limitations.

## Sources

- ClearPoint Strategy homepage — https://www.clearpointstrategy.com/ (fetched 2026-09-08)
- ClearPoint Strategy Help Center — https://support.clearpointstrategy.com/en/ (fetched 2026-09-08)
- ClearPoint Help Center, "Organize Your Strategy" collection — https://support.clearpointstrategy.com/en/collections/6308146-organize-your-strategy (fetched 2026-09-08)
- Envisio homepage — https://www.envisio.com/ (fetched 2026-09-08)
- Envisio "Measure Performance" (Performance Analytics) — https://envisio.com/solutions/performance-analytics/ (fetched 2026-09-08)
- Envisio "Execute Strategy" — https://envisio.com/solutions/strategy-execution-software/ (fetched 2026-09-08)
- AchieveIt homepage — https://www.achieveit.com/ (fetched 2026-09-08)
- AchieveIt "Performance Management Software" — https://www.achieveit.com/solutions/performance-management-software/ (fetched 2026-09-08)
- Neubrain homepage — https://www.neubrain.com/ (fetched 2026-09-08)
- Neubrain "Performance Measurement" — https://www.neubrain.com/solutions/performance-measurement-software (fetched 2026-09-08)

### Source-access Limitations

- opengov.com and cleargov.com: HTTP 403 on automated fetch (2026-09-08). No claims about these vendors are made from memory beyond noting they exist in this market; their suite-module posture is UNVERIFIED here.
- No Tier-1 operational help-center docs were reachable for AchieveIt or Neubrain in this pass (only official product/solution pages, which are Tier 2). Claims for those two products are calibrated accordingly.
- Evidence layers used below: A = directly observed on an official source of one product; B = observed across multiple products; C = canonical inference.

## Product Observations

### ClearPoint Strategy (evidence layer A unless noted)

- Object model: Scorecards are the containers. Inside a scorecard are "Elements": Objectives, Measures (KPIs), Initiatives (Projects) with Milestones, Risks, Action Items, and Series (data series attached to measures). Categories/Perspectives organize scorecards (balanced-scorecard-style grouping). Elements can be linked across scorecards; a "home scorecard" concept exists. OKR cascade to individuals is a separate collection ("Cascade to individuals with OKRs").
- Data in: manual updates, bulk spreadsheet import, a "Data Loader", scheduled "Updater Flow" automation, integrations (Power BI, Snowflake, SQL Server, plus CRM/marketing/PM tools).
- Status: "Calculations and Evaluations" automation produces status indicators; "Red Alert Measures" and key-metric-change alerts.
- Cadence: reminders for teams to submit updates on schedule; homepage pitches "monthly/quarterly objectives, measures, and initiatives".
- Reporting: scheduled report generation and distribution to stakeholders; "Briefing Books" exported for meetings; live dashboards; charts/visualizations; custom views filtered by team/department/individual.
- Users/access: user management collection with authentication and access controls; collaboration collection (34 articles) implies multi-role workflows.
- Market framing: "we analyzed 20,582 strategic plans"; publishes a KPI library for cities (140+ city KPIs); dedicated Local Government & State Agencies sector page; city case studies (e.g., a city manager making the city "data driven").

### Envisio (evidence layer A)

- Object model: multiple plan types coexist and link — organization-wide strategic plans, departmental work plans, standalone projects, KPI sets. Plan structure: goals/priorities → strategies → actions; projects/tasks with budget and spend; performance measures with targets, target lines, benchmark data, drill-down.
- Data in: manual updates; automated email reminders to chase staff updates ("Let Envisio chase down staff updates"); Open API and native integrations for automatic metric updates; scheduled data loading; embeds of third-party visualizations.
- Status: scorecards with traffic-light indicators; progress roll-ups of actions/projects/measures/narrative to show overall progress.
- Narrative: staff submit narrative updates alongside measures; dashboards combine data with narrative for context. Customer quotes confirm " Quarterly Operational Plan Review" generation for council and per-department report cards.
- Audiences: internal vs external publishing toggle; reports/dashboards/scorecards published to shareable URLs ("community dashboards" on performance.envisio.com); reporting for staff, elected officials, community.
- Government-specific structure: measures library via Polco Track integration (local-government KPIs, benchmarking data, livability domain scores); budget alignment solution ("Align Budget"); cross-departmental strategy teams; unlimited users pitched against per-seat silos; services team runs planning/performance workshops.
- Customers: cities, counties, libraries, public health, universities in US/Canada/Australia (e.g., Cloncurry Shire Council, QLD).

### AchieveIt (evidence layer A for product pages; no help-center docs reachable)

- Object model: plans as flexible hierarchies (tree view: areas of focus → goals → objectives/KPIs → initiatives/tasks); multiple plans created and connected across the organization; multi-plan executive view.
- Data in: automated update requests — items are assigned owners and update frequencies; the system emails update requests and accepts in-line updates in email; automated follow-ups ("no chasing"); update history retained per item.
- Status: on track / off track / at risk / thriving vocabulary; real-time dashboards; plan history and trends; drill into results for root-cause.
- Reporting: automated reports; meetings reframed from status collection to decision-making; public-facing dashboards via embed widgets (transparency use case).
- Government posture: industries pages for local/state/federal government, special districts, health departments; reporting pitched to "executives, legislatures, and citizens"; heavy agency/county customer logos; strategy-consultant services included.

### Neubrain (evidence layer A for product pages; no help-center docs reachable)

- Positioning: budgeting + business analytics suite for government; performance measurement is one solution among budgeting solutions (performance-based budgeting, operating/capital/payroll budget, forecasting, cost allocation).
- Object model: KPIs housed in a centralized platform connecting organizational strategy, budget, and performance measures; strategy records with objectives, initiatives, tasks; multiple parallel roll-up hierarchies (performance-oriented, organizational, departmental) documented on the operating-budget page.
- Data in: data readers/integrations from multiple source systems with transformation formulas and validation rules; manual monthly collection described as the incumbent pain.
- Output: scorecards, strategy maps, dashboards; self-service reporting; internal and External Transparency Portal (citizens, other agencies, regulatory and legislative authorities): strategy mapping, initiative/project tracking, scorecards, budget and performance analysis, fiscal health metrics.
- Budget linkage: performance-based budgeting "unifies cost-based budgeting with performance goals"; customer quotes describe linking budget decisions with strategic outcomes for city management, departments, and city council.

## Cross-product Comparison

| Structure | ClearPoint | Envisio | AchieveIt | Neubrain | Layer |
|---|---|---|---|---|---|
| Plan/goal hierarchy as system of record | Scorecards + objectives | Plans: goals/priorities/strategies | Plans: focus areas → goals → KPIs → items | Strategy records: objectives, initiatives, tasks | B |
| Performance measures with targets | Measures (elements) with series | Measures with targets, target lines, benchmarks | KPIs in plan trees | KPIs centralized, linked to strategy+budget | B |
| Periodic actuals/status cycle | Monthly/quarterly updates; status evaluations; alerts | Scheduled data loads; update reminders; scorecards | Owner-assigned update frequencies; email-in updates; status vocabulary | Monthly collection cycles; validation rules | B |
| Owner/accountability attribution | User management, custom views by team | Assigned ownership; update chasing | Every item has owner; follow-ups | Process roles/responsibilities | B |
| Narrative updates beside numbers | Analysis pods / AI analysis | Narrative updates combined with measures | Progress updates with reasons | Reporting incl. narrative (weaker evidence) | B |
| Roll-up / multi-plan aggregation | Linked elements, home scorecard | Multi-plan management, roll-up reporting | Connected plans, multi-plan view | Multiple roll-up hierarchies | B |
| Scorecards/dashboards | Yes | Yes | Yes | Yes | B |
| Scheduled/automated reports for audiences | Scheduled reports, briefing books | Auto-generated reports per audience | Automated reports | Self-service + scheduled (implied) | B |
| Public/transparency publishing | Not emphasized in fetched sources | Community dashboards, internal/external toggle | Public dashboard embeds | External transparency portal | B |
| Projects/initiatives linked to goals | Initiatives + milestones | Projects/tasks with budget+spend | Initiatives/tasks in trees | Initiatives/tasks | B |
| Data integration (API/BI/feeds) | Power BI/Snowflake/SQL Server, data loader | Open API, native integrations, embeds | (update automation; integrations not confirmed) | Data readers with validation | B |
| Measures library / benchmarks | City KPI library (marketing resource) | Polco Track measures + benchmarks | — | — | A, product-specific |
| Budget linkage | Not core | "Align Budget" module | — | Performance-based budgeting core | A, product-specific |
| OKR cascade to individuals | Yes | — | — | — | A, product-specific |
| AI assistance | AI assistants (strategy, analysis) | AI-assisted visuals, AI update drafting | — | Gen-AI budgeting messaging | A |

Key inference: the recurring joint structure is **plan-decomposed measures + target/actual/status over time + owner-attributed periodic updates + roll-up reporting to leadership/governing audiences**. Public publishing is common but not universal (ClearPoint's fetched sources emphasize internal reporting). Budget linkage and measures libraries are differentiators, not common structure.

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The goal-to-measure structure of record** — the organization's plan/goals decomposed into defined performance measures (KPIs) with targets, held persistently in the system. Remove → BI/dashboard tool or project tracker (no goal-derived measurement), or a static plan document.
2. **The recurring actuals/status cycle** — actual values (and often narrative updates) captured per measure on a recurring period by accountable owners — entered manually, imported, or fed from other systems — producing maintained status against target and a history over time. Remove → static plan or one-off report; nothing is being "managed".
3. **Review-and-report presentation of status** — the maintained status is assembled into scorecards/dashboards/reports whose purpose is organizational review and reporting to leadership/governing audiences. Remove → a metrics data store without a management loop.

Jointly-held is load-bearing: (1)+(3) without (2) = a published plan or open-data dashboard; (2)+(3) without (1) = generic BI; (1)+(2) without (3) = a data-collection register.

### L1 — Common Mature Structure

- Initiatives/projects/actions linked to goals (with milestones, budgets/spend) alongside measures
- RAG-style status (traffic lights / on-track-off-track-at-risk), computed by evaluation rules or set manually
- Automated update collection: scheduled reminders, email-in updates, follow-up escalation
- Roll-up reporting and multi-plan views; reports tailored per audience (department, priority, status)
- Briefing books / scheduled report distribution for recurring meetings
- User/role model with department-scoped visibility; unlimited-user pricing common in the segment
- Data import/integration: spreadsheet loaders, APIs, BI-tool connections, scheduled feeds
- Narrative/context updates attached to measures
- Public/community dashboards as an optional publishing surface
- Vendor-delivered strategy/performance consulting services as a companion

### L2 — Variant / Optional Structure

- Budget linkage (performance-based budgeting; measures joined to budget accounts/fiscal data)
- Measures libraries and cross-jurisdiction benchmark data (livability domains etc.)
- OKR cascade to individuals
- Strategy maps (strategy-map visualization)
- Fiscal-year/period alignment specific to government budget cycles (implicitly present; explicit machinery observed only in the budget-linked sample)
- Stat-style operational review formats (CitiStat/CompStat heritage) — plausible historical carrier but not directly documented in this sample (uncertainty)
- Transparency-portal packaging (citizen-facing portals with fiscal-health indicators, open-checkbook-adjacent content — observed in one sample; the fiscal content belongs to transparency types)

### L3 — Vendor-specific Detail

- ClearPoint: scorecard/perspectives terminology, Series element type, Red Alert measures, Data Loader, briefing books, AI assistants
- Envisio: Polco Track measures/benchmark integration, community-dashboard URLs (performance.envisio.com), MS Teams integration, unlimited-users policy
- AchieveIt: on track/off track/at risk/thriving vocabulary, in-email update submission, tree-view plan editor
- Neubrain: PPBE/J-Book (DoD) solutions, cost allocation, external portal content list (tax/debt analysis, open checkbook)

## Vendor-specific Findings

- Budget linkage is a suite-posture differentiator (Neubrain core; Envisio optional module; ClearPoint not documented as core).
- Measures libraries/benchmarks (Polco Track) observed once — product-specific.
- OKR individual cascade observed once — product-specific.
- AchieveIt's email-native update submission (in-line updates by replying to email) observed once.

## Boundary Findings

- **vs BI Platform / Dashboard Platform**: BI visualizes arbitrary source data; here the center of gravity is a goal-derived measure structure with targets, owners, and a managed update cycle. Remove the plan/target/owner loop from this Type and you get BI; add arbitrary-source exploration to BI and it doesn't acquire accountability loops. Evidence: all four products pitch against spreadsheets/BI as "strategy context", not raw exploration.
- **vs Public Budgeting Platform**: budget construction (accounts, funds, scenarios, adoption) is the other type's core; here measures are core. Overlap is real but partial: performance-based budgeting sits in the overlap zone (observed in the budget-linked sample and as an optional module elsewhere). Products from either pole converge without dissolving the boundary.
- **vs Government Transparency Portal / Government Open Data Portal**: transparency/open-data types publish data of record; this type *produces and maintains* goal-linked performance status through a managed loop, then may publish it. Publishing without the plan/measure/update loop = transparency portal. Public publishing is therefore common-not-defining.
- **vs Project Management Application**: project tracking exists here, but projects are one plan element beside measures with targets; there is no resource/dependency-centered project core. Remove measures+targets and this collapses into project management.
- **vs Performance Management Platform (employee/HR)**: individual appraisal/goal software targets persons; this type targets organizational units and services. Ownership here is accountability for data updates, not performance appraisal of the owner.
- **vs OKR / Goal Management Platform (§09 neighbor)**: structurally the nearest generic relative. Differences observed: measure/KPI-centricity with targets and quantitative series rather than key results only; institutional reporting audiences (councils, boards, legislatures); public-transparency duty; fiscal alignment; measures libraries. The market also carries the same machinery cross-industry (ClearPoint serves hospitals/banks; AchieveIt serves healthcare/education) — see Taxonomy Note.
- **vs Monitoring & Evaluation Platform / Social Impact Measurement (nonprofit section)**: M&E centers on program evaluation against theory-of-change/indicators for funders; this type centers on organization-wide service performance and management review. Adjacent; convergent vocabulary (indicators, targets, outcomes).
- **Climate-planning cross-reference (discharge of prior passes' flag)**: content-anchor test applied. A climate action plan tracked in this machinery (observed: a city climate dashboard with emissions-reduction and renewable-energy measures carried in the public-sector pure-play's public dashboards) keeps the emissions/hazard anchor → belongs to the climate/decarbonization planning types as content, while the generic machinery belongs here. Generic goal→measure→actuals→status plans without a climate/emissions anchor → this type. Both prior passes' flags discharged.

## Taxonomy Note (potential issue, not silently resolved)

The defining machinery of this leaf (plan→measures→actuals→status→reporting) is materially identical to generic corporate strategy-execution/OKR software; the sampled products themselves are cross-industry or carry cross-industry siblings. What makes this leaf a distinct directory entry is the audience/market shaping: public-sector entities, institutional audiences (council/board/legislature), transparency duty, fiscal alignment, and a distinct vendor ecosystem (public-sector pure-plays + gov suite vendors). This is recorded as a boundary observation — "audience-governed Type" — rather than silently merged or split. Joint review with the OKR / Goal Management Platform and Performance Management Platform leaves may be worthwhile.

## Historical / Market-Sample Check

- Before dedicated software, governments ran this loop with paper and meetings: strategic plans and budget documents carrying performance measures, periodic printed reports to council, and stat-style review sessions (CitiStat/CompStat heritage). That paper-era practice satisfies all three L0 structures (plan-decomposed measures, periodic actuals with owners, assembled review/reporting) — no modern addition is definitional.
- Regional check: the sample includes a Canadian-headquartered vendor with Australian local-government customers (quarterly operational plan reviews for council) and US federal/DoD-adjacent budget-linked performance — the core holds across Westminster-style council reporting and US-style budget-linked performance.
- Modern additions (public dashboards, benchmark libraries, AI drafting, BI integrations, unlimited-user SaaS pricing) fail the removal test in neither direction — they are conveniences, not definers. L0 survives their removal.

## Uncertainties

- OpenGov and ClearGov (the most prominent suite/benchmarking players in this market) could not be fetched (403); their module structure is unverified here. The "gov-suite module" variant posture is therefore inferred from market structure, not from product evidence.
- AchieveIt and Neubrain claims rest on official product pages only (Tier 2); detailed operational mechanics (update cadence defaults, permission depth, status-rule configuration) were not verified against help-center docs.
- Whether stat-style operational performance products (CitiStat-lineage tools) form a distinct sub-type or a variant was not resolved by direct documentation.
- Public publishing is documented as common but may be more prevalent than the sample shows (ClearPoint's fetched pages simply did not emphasize it).
- Precise status vocabularies, update frequencies, and evaluation-rule mechanics vary by product and were deliberately not generalized.

## Final Synthesis

Government Performance Management is the public-sector organization's system of record for managing institutional performance: it holds the organization's goals decomposed into measures with targets, runs a recurring owner-attributed cycle that collects actuals and narrative updates and maintains status against target, and assembles that status into scorecards, dashboards, and reports for management review and reporting to governing bodies — with public dashboards, benchmark libraries, and budget linkage as common extensions, and with the machinery itself being shared with (and shaped differently by) the broader strategy-execution market.
