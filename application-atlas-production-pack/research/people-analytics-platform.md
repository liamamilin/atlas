# Research Notes — People Analytics Platform

Research date: 2026-09-06
Leaf: People Analytics Platform (§09 HR, Workforce & Talent)
Slug: people-analytics-platform

## Research Goal

Understand what a People Analytics Platform actually is as an Application Type: its central objects, its data foundation, its analytical loop, its consumers, its rules (especially around people-data sensitivity), and its boundaries against HRIS/HCM reporting, Business Intelligence, Employee Engagement, Workforce Planning, and Organization Design.

## Initial Boundary

Working hypothesis before research:

- Core use: answer workforce questions (composition, movement, attrition, cost, diversity, outcomes) using integrated people data, with governed metric definitions and analytical surfaces (dashboards, guided insights).
- Primary users: people analytics teams / HR analysts (builders); CHRO, HRBPs, executives, managers (consumers).
- Nearest neighbors: HRIS/HCM (system of record + reporting), Employee Engagement Platform (survey measurement), Workforce Planning Platform (forward supply/demand), Organization Design Platform (structure scenarios), Business Intelligence Platform (generic analytics).
- Likely confusion: "People Analytics" is also the name of analytics modules inside HCM suites (e.g., SAP SuccessFactors People Analytics, Workday People Analytics) — the Type must be defined so that both standalone pure-plays and suite-embedded modules fit, without collapsing into "any HR reporting".

## Research Questions

1. What is the central object — a metric? a dashboard? a data model of the workforce?
2. Where does the data come from, and how is it integrated (HRIS, payroll, ATS, survey, performance, finance)?
3. What do users actually do: explore metrics, build dashboards, receive guided insights, drill into segments?
4. What time semantics matter (point-in-time workforce, trends, "as of" questions)?
5. What role structure exists (analyst/builder vs leader/consumer vs data ops)?
6. What rules govern behavior: access control on sensitive attributes, statistical safeguards on small groups, data-quality dependencies, refresh cadence?
7. Where is the boundary vs HRIS reporting, BI platforms, engagement analytics, workforce planning, org design?

## Representative Products

Selected for market representativeness + documentation quality + distinct product philosophies + distinct customer tiers:

| Product | Philosophy | Tier | Evidence level reached |
|---|---|---|---|
| Visier | Standalone pure-play people analytics; insight-first ("answers, not dashboards"); enterprise | Enterprise | Tier 1 (developer/analytic-model docs) + Tier 2 (platform, security, product pages) |
| One Model | Standalone data-first people analytics ("Data Mesh" governed HR data model + AI); enterprise | Enterprise | Tier 2 (homepage + Data Mesh product page); docs site not located |
| Culture Amp (People Analytics / Retention Insights) | Survey/engagement-first vendor extending into workforce analytics; mid-market | Mid-market | Tier 1 (support guide: Retention Insights article + collection) |
| ChartHop | Org-first "people ops platform" with analytics layer; mid-market | Mid-market | Tier 2 (homepage incl. FAQ) + Tier 1 help-center root (thin) |

Rejected/abandoned samples:

- SAP SuccessFactors People Analytics (suite-embedded archetype): SAP Help Portal returned empty JS shells twice (help.sap.com/docs/SAP_SUCCESSFACTORS_PEOPLE_ANALYTICS, /docs/successfactors); sap.com product path 404. Abandoned per network rules; retained only as a named example of the suite-embedded variant with degraded evidence (third-party integration pages describe it).
- Workday People Analytics: known JS-gated doc estate; not attempted after SAP failures (same suite-embedded archetype already covered by the SAP note).
- HiBob: help center gated behind customer login ("Customer login" shell). Abandoned.

## Sources

- Visier — Analytic Model overview (Tier 1): https://docs.visier.com/developer/Analytic%20Model/analytic-model-overview.htm
- Visier — Platform (Tier 2): https://www.visier.com/platform/
- Visier — Security & Governance (Tier 2): https://www.visier.com/platform/security-model/
- Visier — Visier People product page (Tier 2): https://www.visier.com/products/visier-people/
- One Model — Homepage (Tier 2): https://www.onemodel.co/
- One Model — Data Mesh (Tier 2): https://www.onemodel.co/products/data-mesh
- Culture Amp — People Analytics collection (Tier 1): https://support.cultureamp.com/en/collections/8949633-people-analytics
- Culture Amp — Retention Insights article (Tier 1): https://support.cultureamp.com/en/articles/7916907-retention-insights
- ChartHop — Homepage incl. FAQ (Tier 2): https://www.charthop.com/
- ChartHop — Help Center root (Tier 1, thin): https://docs.charthop.com/

## Product A — Visier

### Key observations (evidence layer A unless noted)

**Analytic model (Tier 1, docs.visier.com):**
- The product's world is an **analytic model**: data piped from multiple sources into a single repository, which "generates all the elements you need to do your work, whether that's constructing charts and dashboards in Visier or a third-party app".
- **Analytic objects** are table-like items: **subjects** (the foundation — e.g., Employee; "everything you can do … relies on the subjects"), **events** (something that happened to a record at an instant — Employment Start, Pay Change Event, employee exits), plus overlays and internal comparisons.
- **Properties** describe records (Employee ID, Full Name, Gender, Hourly Rate, Job Name, Tenure).
- **Dimensions** classify records for grouping (Location → members like North America, Canada, Vancouver).
- **Concepts** reclassify data into standardized subsets without new data (Gen X from Birth Date; Manager from Manager Status; Employee Movement = moved in/out/within; First Year = tenure < 1 year; Applicant Process stages).
- **Metrics** "calculate a business concern that can be quantified as a number"; formulas perform calculations on analytic objects/attributes and "always contain an aggregation function like SUM or AVERAGE".
- **Blueprint**: out-of-the-box content library; customizable without code for many parts; metrics can be built by reusing formulas or a formula language; changing Blueprint objects may affect receiving Blueprint updates (versioned content inheritance).
- Data in: File Upload, Data Connectors, Direct Data Intake API. Data out: aggregated data to third-party apps.

**Platform pillars (Tier 2, /platform/):**
- Unify: "a data layer that's built to manage and reconcile changes over time in both the schema and its records — enabling … accurate point-in-time insights".
- Enrich: benchmarks + AI-driven standardization.
- Model: "extensible data model includes thousands of well-documented, AI-ready metrics"; no-code config; built-in version control (Studio projects).
- Secure: "dynamic role-based access model … evolves with your organization".
- Distribute: Visier People app, Vee (AI agent), embedded analytics, APIs/connectors.

**Security model (Tier 2, /platform/security-model/):**
- Central security model defines permissions "across the entire analytics ecosystem — from data storage to analytic content to the way it's consumed".
- Dynamic role-based access "automatically updates as people move within the organization, reflecting changes in role, team, location, or any other attribute"; data access levels at **row and column level**.
- User permission management, access audit logs, configuration testing in Studio or via API.

**Visier People product surface (Tier 2):**
- Solution library keyed to workforce questions: headcount, retention, diversity, internal mobility, compensation, talent acquisition, employee experience, total rewards, skills, learning analytics, work time, OKRs, employee relations, hybrid work, workforce planning.
- "Hundreds of pre-built metrics, questions and analyses"; "explore your data on the fly … no data wrangling, querying or dashboard-building required".
- Vee AI assistant answers people questions; Vee Boards = AI-augmented executive insight boards (e.g., People Cost Board for CHRO & CFO).
- Proprietary benchmark dataset; open/extensible model (own objects, metrics, data; non-HR data like sales/operations).

## Product B — One Model

### Key observations (evidence layer A at product-page level; no Tier-1 docs located)

**Data foundation ("Data Mesh", Tier 2):**
- "Bring together HRIS, ATS, payroll, engagement, performance, finance, and other business data into a governed HR data model built for enterprise complexity."
- Pain framing: "Headcount data often lives in systems like Workday and SAP SuccessFactors. Labor costs come from finance systems. Recruiting metrics come from platforms like Greenhouse and iCIMS. Organizational changes touch all of these systems. Without a consistent foundation, reporting slows down, definitions become inconsistent, and teams lose confidence in the answers."
- Shared definitions: "HR and Finance can work from the same definition of headcount, reducing reporting discrepancies."
- Governance inside the data foundation: role-based access, shared workforce definitions, domain ownership by team, built-in controls and auditability; real-time delivery; adapt as systems/structures change.

**Analytics & consumption (Tier 2):**
- "Data Stories" — interactive data visualization and storytelling; customizable reports and **Storyboards**; "CHROs, HRBPs, and executives can quickly see what changed, why it matters, and what to do next"; standardized KPI reporting across teams/regions; board-ready views.
- **One AI Assistant**: "Ask workforce questions in plain language … explore workforce questions, summarize findings, and follow the thread to deeper analysis"; "expand access beyond the people analytics team".
- **Forecasting & Planning**: "transparent forecasts for hiring, attrition, capacity, and workforce cost so HR and finance can plan together".
- **Enterprise AI Connections (MCP)**: connect governed workforce data to Copilot/ChatGPT/Claude/Gemini with role-based access and governance; "answers aligned to your business definitions".
- Roles served: CFO, CHRO, HRBP, HRIS, People Analytics Leader, Talent Acquisition.
- Integrations: Workday, SuccessFactors, Qualtrics, Greenhouse, Databricks, Oracle/PeopleSoft.

## Product C — Culture Amp (People Analytics / Retention Insights)

### Key observations (evidence layer A, Tier 1 support guide)

**Scope of the "People Analytics" line:**
- The vendor's People Analytics support collection centers on **Retention Insights** ("Uncover the why behind employee turnover") — turnover analytics built from HRIS employee data + engagement survey data. A "Multi-signal Intelligence (MSI)" line (turnover risk) exists in early access.

**Retention Insights mechanics (Tier 1):**
- Motivation: "Most organizations track their actual turnover in their HRIS systems. This provides … insights into what employees are staying or leaving. It doesn't however provide you with a clear picture of: [why they leave / how turnover may change in the future / …]".
- Dashboard sections: **Overview** (engagement, retention, turnover over time; "Do you see a relationship between turnover and engagement?"); **Turnover by Group** (groups with highest turnover; "View More" shows "unique top motivators for that group (if it has 25 or more employees)"; "All Groups" comparison table sorted by highest turnover); **Significant Turnover** (highlights groups "where turnover across the last 12 months is higher than expected", statistically meaningful vs the parent population/filter); intent-to-stay question analysis; "actionable insights" shared with accountable leaders.
- Survey coupling: recommends including a two-year commitment question ("I see myself still working at [company] in two years' time") in engagement/pulse surveys so Retention Insights can predict future retention/turnover drivers.
- Data dependency: "This report relies on having accurate employee start and end dates. Without that information it's not possible for us to calculate the correct turnover or retention rate." HRIS sync or manual upload required; **Data Health tools** to keep employee data accurate.
- Calculation rules (Tier 1, precise): headcount and retention rate figures calculated to the end of the last calendar month; headcount for a month includes anyone in the group at any point during that month (mid-month department change → counted in both); retention and turnover calculated over a 12-month period; groups show retention/turnover only after a full year of data.
- Access: admin grants access to the Retention Insights dashboard (separate collection "Granting Access to Retention Insights").

## Product D — ChartHop

### Key observations (evidence layer A at product-page level; help-center root thin)

- Positioning: "Organizational intelligence for people analytics, headcount planning and HCM"; "connecting your people and business data into a living model of your organization, so you can see what's changing, model what's next, and act on it in the same place".
- FAQ explicitly frames the relationship: "People analytics tells you what's happening in your workforce. Organizational intelligence does that and more, covering the whole organization — people, cost and output together — and it doesn't stop at the answer. The analysis and the decision happen in the same place, on the same model."
- Modules: HRIS, Headcount Planning, Compensation, Performance, Engagement, Goals, AI Pro (agentic AI), Analytics ("Board-ready answers in a single click").
- Data: "connects ADP, Greenhouse, Workday, SAP, and 100+ HRIS, ATS, FP&A, and business tools into a living model of your organization"; designed as the "visual layer" on top of the existing stack; can also be the HRIS itself.
- AI: ask in plain English, answers "drawn from your whole org — people, cost and output — with links back to the source"; build dashboards/comp cycles/surveys/headcount plans from chat; **Access Guard**: "People, agents and outside assistants see only what the person they're acting for is allowed to see — so leaders get self-serve answers without exposing comp or performance."
- Built-in Nine Box (product update June 2026); time-based columns in the Data Sheet (Sept 2026) — the org model carries history.

## Cross-product Comparison

| Dimension | Visier | One Model | Culture Amp (Retention Insights) | ChartHop |
|---|---|---|---|---|
| Central structure | Analytic model: subjects (Employee) + events + properties + dimensions + concepts + metrics; Blueprint content library | Governed HR data model ("Data Mesh") over multi-source data; Storyboards/Data Stories | Turnover analytics over synced HRIS employee data + engagement survey data | "Living model" of the organization (people + cost + output) with analytics on top |
| Data sources | Multi-source: file upload, connectors, direct intake API; non-HR data extensible | HRIS, ATS, payroll, engagement, performance, finance; Workday/SF/Qualtrics/Greenhouse/Databricks | HRIS sync (Workday, BambooHR, Dayforce, …) or manual employee data file; survey data native | ADP, Greenhouse, Workday, SAP, 100+ HRIS/ATS/FP&A tools |
| Metric governance | Documented metric library; formula language; version control (Studio projects) | Shared definitions ("same definition of headcount" for HR & Finance); domain ownership | Vendor-defined turnover/retention calculations with stated rules | Org model carries definitions; time-based columns |
| Time semantics | Point-in-time insights; "manage and reconcile changes over time"; history/present/futures of a subject | Real-time delivery; refresh "from weeks to hours" (case-study claim) | Figures as of end of last calendar month; 12-month retention/turnover window; full-year group history required | "Current by default"; remembers how the organization changed (time-based columns) |
| Analytical loop | Explore prebuilt questions/analyses; on-the-fly exploration; Vee AI assistant; Vee Boards | Storyboards; One AI Assistant plain-language questions; forecasting | Overview → Turnover by Group → Significant Turnover → motivators → share with accountable leaders | Ask in plain English; dashboards; drill into the living model |
| Consumers | Self-serve for thousands of managers; C-suite boards | CHRO/HRBP/executives/CFO; "scale insights to every leader" | Admins grant dashboard access to leaders | People leaders, People Ops, Finance, managers, executives |
| Access control | Dynamic role-based access; row/column level; audit logs; central security model | Role-based access; governance, auditability; AI access curation | Admin-granted dashboard access; survey confidentiality machinery platform-wide | Access Guard (person-scoped visibility incl. agents); comp/performance protection |
| Statistical safeguards | Not observed in fetched pages | Not observed in fetched pages | Motivators require ≥25 employees; "significant turnover" statistical test vs parent population | Not observed in fetched pages |
| Benchmarks | Proprietary benchmark dataset | Not observed | Benchmark/comparison machinery in survey side (imported comparisons) | Not observed |
| Prediction/AI | Vee assistant; Vee Boards; predictive analytics positioning | One AI Assistant; forecasting (hiring/attrition/capacity/cost); MCP connections | Turnover-risk insights (early access); intent-to-stay prediction | Agentic AI; plain-language Q&A; build-by-chat |
| Adjacent modules | Workforce Planning product; Embedded Analytics for ISVs | Forecasting & Planning; Enterprise AI (MCP) | Engagement/Performance suites (the vendor's core) | HRIS, Headcount Planning, Compensation, Performance, Engagement, Goals |

## Canonical Model (synthesis)

### L0 — Defining Invariant (deliberately small)

1. **Integrated workforce data layer** — the organization's people records (identified employees with attributes, plus their dated events: hires, exits, moves, pay changes, and similar) unified from one or more source systems into a single analyzable model with preserved history.
2. **Governed workforce metrics** — quantified measures computed over that layer (headcount, turnover, movement, and similar) with consistent, managed definitions.
3. **Workforce question → analytical answer loop** — users interrogate the workforce by segment and over time (filter, trend, compare, drill) and receive analytical answers (visualizations, guided insights) rather than transactional record edits.

Remove the integrated multi-source analytical layer → HRIS operational reporting remains. Remove governed metrics → ad-hoc spreadsheet analysis remains. Remove the analytical loop → a data warehouse remains. In each case the Type is no longer recognizable.

Historical check: warehouse-era HR analytics (2000s HR data marts feeding BI reports) satisfies all three without any modern AI, benchmarks, or self-serve distribution; regional standalone products likewise. Suite-embedded analytics modules also satisfy all three (their source list is shorter). The definition therefore does not overfit the current pure-play market.

### L1 — Common Mature Structure

- Multi-source connectors (HRIS, ATS, payroll, engagement/survey, performance, finance)
- Prebuilt metric/content libraries (out-of-the-box questions, KPI packs, solution views)
- Dashboards / storyboards / stories as consumption surfaces
- Self-serve distribution to non-analyst roles (leaders, managers, executives), often role-scoped
- Data-quality / data-health tooling
- Access control calibrated to people-data sensitivity (role-based; row/column-level in the most mature)
- Benchmarks / external comparisons
- Predictive analytics (attrition/turnover risk)
- AI assistance (natural-language question answering; increasingly agents)
- Governance machinery (audit logs, definition catalogs, model version control)

### L2 — Variant / Optional Structure

- **Packaging posture**: standalone pure-play platform vs suite-embedded analytics module (HCM-native) vs engagement-suite extension vs org-platform layer vs embedded analytics sold to ISVs
- **Data architecture**: proprietary analytic model vs warehouse-native/data-mesh posture
- **Benchmark data**: proprietary vendor benchmarks vs customer-supplied comparisons vs none
- **Forward-looking extension**: forecasting and workforce-planning modules (overlaps Workforce Planning Platform)
- **AI posture**: assistant vs agentic vs connections to enterprise LLM tools (MCP-style)
- **Refresh cadence**: batch/scheduled vs real-time
- **Industry/regional compliance packs**, deployment region, tenant isolation requirements

### L3 — Vendor-specific (research notes only)

- Visier: Blueprint, Studio, Vee, Vee Boards, Sapient charts naming; "65k companies / 36M employee records" marketing figures.
- One Model: "Data Mesh", "One AI", "One AI Data Intelligence", MCP "Enterprise AI Connections" naming; JLL case-study claims (8x faster dashboards, refresh weeks→hours).
- Culture Amp: Retention Insights naming; motivator threshold of 25 employees; 12-month calculation window; end-of-last-calendar-month as-of rule; MSI early access.
- ChartHop: "Carrot" filters/queries, Access Guard, Nine Box module, PEPM pricing.

## Vendor-specific Findings

See L3 above. None of these enter the canonical document except as named examples in Variants/Representative Products.

## Boundary Findings

1. **vs HRIS / HCM (reporting)**: HRIS reporting reports on the HRIS's own transactional records for operating the HR function; People Analytics integrates multiple sources into an analytical model with governed definitions and answers cross-system workforce questions. Test: remove multi-source integration + the analytical model → HRIS reporting remains. **Complication**: HCM suites ship analytics modules named "People Analytics" (SAP SuccessFactors People Analytics; Workday People Analytics) — these satisfy the L0 with the suite as (often the only) source. The Type boundary is therefore data-scope posture (suite-internal vs cross-system), not feature presence. Flagged for joint review when HRIS/HCM leaves are processed.
2. **vs Business Intelligence Platform**: BI is domain-generic (any data, any semantics); People Analytics is domain-specific — workforce semantics (employee subjects, org hierarchy, tenure), HR metric definitions, people-data access rules, and HR benchmarks are built in. Test: swap the data domain → BI remains; People Analytics does not. One Model's own framing ("HR and Finance work from the same definition of headcount") shows the metric-governance layer is HR-specific.
3. **vs Employee Engagement Platform**: engagement centers the survey measurement loop (population, programs, confidentiality, action); People Analytics centers the integrated workforce data layer and metric governance. Engagement scores are one input to people analytics (Culture Amp couples them). Test: remove the survey engine → People Analytics remains; remove the data layer → engagement platform remains. Culture Amp spans both from the engagement side; Visier/One Model span it from the data side (survey data as a connector).
4. **vs Workforce Planning Platform**: planning is forward-looking (demand/supply, positions, scenarios over a horizon); People Analytics is descriptive/diagnostic (and predictive) over what is and has been. Vendors bundle them (Visier Workforce Planning; One Model forecasting; ChartHop headcount planning). Test: remove plan/position objects and the planning horizon → analytics remains. Consistent with the organization-design pass flag (org-design vs workforce-planning).
5. **vs Organization Design Platform**: org design centers structure authoring/scenarios (units, positions, reporting lines); People Analytics centers workforce measurement. ChartHop spans both on one "living model". Test: remove scenario/impact machinery → analytics remains. Consistent with the prior organization-design-platform pass.
6. **vs Employee Survey Platform**: survey platforms center questionnaire/collection mechanics for any audience; people analytics consumes survey results as one data source. Clean capability relationship.

## Uncertainties

- Suite-embedded people analytics (SAP SuccessFactors, Workday) could not be verified from official docs in this pass; their inclusion as a Variant rests on positioning-level evidence (vendor names + third-party integration pages). No precise claims made about their internals.
- One Model and ChartHop evidence is product-page level (Tier 2); no Tier-1 operational docs were reachable in the time budget. Interface-level mechanics for those two are asserted only conceptually.
- Whether "real-time" data delivery is now the market norm or a differentiator could not be established across the sample (Visier markets "real-time people data platform"; One Model markets real-time delivery; Culture Amp's figures are computed to end of last calendar month). Treated as a variant dimension, not a common structure.
- The prevalence of statistical safeguards (small-group suppression) beyond Culture Amp could not be verified; survey-side confidentiality machinery is well documented in the engagement pass, but analytics-side thresholds were observed in only one product.

## Final Synthesis

A People Analytics Platform is defined by a small core: an integrated, governed workforce data layer + workforce metrics with managed definitions + an analytical question→answer loop over the workforce (by segment, over time). Everything else commonly associated with the category — connectors, prebuilt content, dashboards, benchmarks, prediction, AI assistants, self-serve distribution, governance tooling — is mature-market structure, not definition. The Type's sharpest boundaries are against HRIS reporting (operational records vs analytical model), generic BI (domain-generic vs workforce-specific semantics and access rules), engagement platforms (survey measurement loop vs data layer), and planning/org-design Types (forward-looking structure vs descriptive measurement), with real bundling gradients in the market that should be handled as Variants, not separate structures.
