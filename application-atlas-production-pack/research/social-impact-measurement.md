# Research Notes — Social Impact Measurement

Research date: 2026-09-09

## Research Goal

Understand what "Social Impact Measurement" software actually is as an Application Type: what objects exist inside it, who uses it, how impact measurement work flows from defining what to measure to communicating impact, which structures are definitional vs merely common, and — critically — where its boundary runs against the already-processed sibling **Monitoring & Evaluation Platform** (§25), which left a JOINT REVIEW RECOMMENDED flag for this pass.

## Initial Boundary

Working hypothesis before research:

- Social Impact Measurement = software supporting the *practice* of measuring and demonstrating social impact: define what change you seek, gather evidence, analyze it, communicate impact to stakeholders.
- Nearest neighbors: Monitoring & Evaluation Platform (sibling leaf — the flagged seam), Survey Platform / Online Form Builder, BI / Dashboard Platform, Grantmaking Platform / Grants Management System, Nonprofit CRM, Nonprofit Case Management, Nonprofit Program Management, Government Performance Management, ESG Management.
- Risk identified by the M&E pass: M&E platforms market "impact measurement" as a use case (ActivityInfo has a dedicated page), so feature presence cannot separate the leaves — the seam must be center-of-gravity.
- Test handed to this pass: *remove the measurement-practice/methodology layer → the M&E machinery remains; remove the framework/actuals/reporting machinery of record → practice-tooling territory.* This pass must determine whether "practice tooling" is a real, coherent Type or merely lighter M&E.

## Research Questions

1. What do products that self-identify as "impact measurement" software actually contain? What is their unit of work?
2. Who buys and operates them — nonprofits, funders, investors, governments? Is the relationship one-sided or two-sided (funder ↔ grantee)?
3. Do these products hold a results framework of record with indicator actuals per reporting period and a submission/approval/lock quality workflow (the M&E machinery), or something structurally different?
4. What role does qualitative evidence (stories, open text, testimonials) play — peripheral or structural?
5. What is the terminal output — donor accountability reports, or stakeholder-facing impact communication (reports, dashboards, stories, public transparency)?
6. Where exactly does the seam with Monitoring & Evaluation Platform run, and can it be held at center-of-gravity strength with vendor-side corroboration in both directions?
7. Historical check: would pre-software impact measurement practice (paper frameworks, spreadsheets, annual impact reports) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy | Customer level / segment |
|---|---|---|
| **Sopact Sense** (Sopact) | data + AI "impact intelligence": surveys/interviews/documents → one record per person → analysis → action | nonprofits, workforce programs, foundations, universities, impact/ESG funds; small teams → enterprise |
| **ImpactMapper** | qualitative-first measurement: surveys + text tagging against outcome taxonomies + dashboards + designed impact reports; sold with consulting/training | donors, foundations, NGOs in human rights / gender / SDG space; small nonprofits → large foundations |
| **UpMetrics** | two-sided impact reporting platform: define metrics/framework, request & collect data from grantees/portfolio, analyze, tell the story | grantmakers, nonprofits, impact investors (US philanthropy + impact investing) |
| **Clear Impact Suite** (Scorecard + Compyle + Showcase) | methodology-embodied software built on Results-Based Accountability™: scorecards of results/indicators/measures + turn-the-curve improvement practice + public transparency | government agencies, health departments, nonprofits, funders, United Ways, collective-impact coalitions |

Boundary references (identified, not fully sampled):

- **ActivityInfo** — an M&E platform (sampled by the sibling pass) with a dedicated "Impact measurement" marketing page; used here as the M&E-side corroboration for the joint review.
- **eImpact** — an impact-reporting-first product; site unreachable twice (transport error / timeout), abandoned per the network rule. Recorded as a sourcing limitation; not used as evidence.
- **Salesforce Nonprofit Cloud / Bonterra "Impact Management"** — impact-measurement vocabulary used by CRM/case-management suites; packaging straddle, not sampled in depth.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Sopact — https://www.sopact.com/ (product homepage, use cases, pricing, FAQ); https://docs.sopact.com/ (user manual — only cover page reachable)
- ImpactMapper — https://www.impactmapper.com/ (homepage: software/consulting/training legs); https://www.impactmapper.com/features (full feature list, pricing, customer use cases)
- UpMetrics — https://upmetrics.com/ (homepage, FAQ); https://upmetrics.com/platform (platform capability pages, FAQs incl. GMS comparison, framework-agnostic statement)
- Clear Impact — https://clearimpact.com/ (homepage: suite + framework + services); https://clearimpact.com/scorecard/ (Scorecard capability detail, RBA scorecard anatomy)
- ActivityInfo (M&E-side corroboration) — https://www.activityinfo.org/about/impact-measurement.html (dedicated impact-measurement use-case page)

Sourcing limitations:

- No Tier-1 help-center article was individually fetched for any sampled product (help centers exist for UpMetrics and Sopact but were not reachable in useful depth in this environment; Sopact docs returned only a cover page). Evidence rests on official product pages, feature lists, FAQs, and customer-use descriptions — Tier 1/Tier 2 mix. Claims below are calibrated accordingly: structural claims (what objects exist, what the workflow is for) are strong; precise operational parameters (limits, plan features, exact role names) are not asserted.
- eImpact unreachable — the reporting-first pole of the market is described only from the sampled products' own reporting surfaces.

## Product Observations

### Sopact Sense (Sopact)

Evidence layer: A (direct observation of official product pages).

- Self-positioning: "Grant, Case & Impact Intelligence Software". Tagline: "Reliable answers from your impact data… an answer you can defend, source by source."
- The core loop is explicitly named: **"Collect. Extract. Analyze. Act. Repeat."** — "Most tools stop the moment the data is collected. Sopact keeps going. Every new response feeds the same record, so your answers stay current."
- **One record per person/program/organization** is the organizing structure: "Keep one record per person, pulled from all your sources" — surveys, interviews, documents, notes all attach to the same participant record over time (example: "482 notes tracked in one participant's record, over 14 months").
- Collection: build surveys (pre/mid/post assessments shown), assign to participant groups, multi-language collection, edit surveys live.
- Analysis: AI "Intelligent Cells / Intelligent Rows" interpret responses with context (the person, the program, the document); automated summaries; instant designer reports; claims traceability ("Every number traces back to where it came from").
- Use cases (solutions pages): Case Management ("track each person from intake through years of notes"), Applications & Grants (foundations follow funded people to outcomes), Training & Programs ("score every applicant… then measure what actually changed"), Impact & ESG Portfolio (impact funds/ESG teams track investments across the hold).
- Audience: "nonprofits, foundations, education and workforce programs, community networks and impact or ESG teams."
- Services wrap: Academy courses, technical advisory hours bundled into plans, paid pilots.
- Pricing: subscription tiers with usage allowances (AI analyses, survey responses); enterprise custom.

### ImpactMapper

Evidence layer: A (direct observation of homepage + full feature page).

- Self-positioning: "Reports, Consulting and Software for Social Impact Tracking" — three legs: **Impact Report** (consulting-produced reports/stories), **Impact Advisement** (workshops, M&E/impact-management training, metric refinement), **ImpactAnalytic Software** ("bring your diverse data streams together in one place to analyze impact trends and share the stories that matter most").
- Software features (feature page, 50+ features):
  - **Surveys**: design/send/analyze custom surveys; short/long text, choice, matrix, numerical, financial, rating fields; multilingual; public/private/anonymous; over-time series and pre-post surveys; QR/permalink sharing; participant self-tagging "according to your custom outcomes or any taxonomy"; saved quotes; PDF/CSV export.
  - **Tags as the measurement device**: "Track outcomes in qualitative and quantitative data using text, quantity, currency, location, and date Tag types"; tag taxonomies reviewed/managed; automatic tagging of incoming responses; "align your custom taxonomies and outcomes"; inductive and deductive coding through the text tagging tool.
  - **Text/report analysis**: upload Docx/PDF reports; search and tag text (content analysis); extract numbers/financials from text for charting; import interview transcripts via Trint API; import grant data from Airtable/Submittable/Fluxx (API) or CSV.
  - **Projects**: "Create grant or partner linked projects or a normal project"; multiple projects with different data sets, stakeholders, and tagging taxonomies.
  - **Charts & dashboards**: many chart types; custom dashboards "for fast and real-time communication to different audiences, such as your board, different donors, your communities, leadership, policymakers"; pages/sections; hero figures; maps; quotes placed under pictures; PDF export or live URL share.
- Customer use cases (named): qualitative coding/meta-analysis of 240+ reports for a UN initiative (lessons-learned compendium); a foundation using ImpactMapper "as an impact reporting tool" — grantee reports collected through surveys, "tagged with their outcomes from the Theory of Change", visualizations for annual board/donor/community reporting with baseline/mid-term over-time analysis; a participatory grantmaker analyzing "grantee stories of change" against its theory of change at portfolio level; corporate customer-feedback surveys; annual grantmaking-portfolio impact reporting for boards.
- Audience: "donors, philanthropists, investors, businesses, and nonprofits"; expertise in "human rights, gender equality and diversity, climate, SDG and social justice investments, grants, and projects."
- Pricing: monthly/annual licenses scaled to organization size (surveys-only tier → full suite for foundations); AI add-ons.

### UpMetrics

Evidence layer: A (direct observation of homepage + platform page + FAQs).

- Self-positioning: "Impact Reporting Software for Nonprofits, Foundations & Investors"; "Impact reporting built for learning and growth, not just compliance."
- Own methodology: **DeCAL** — "define, collect, analyze, and leverage… helps nonprofits build their own custom Impact Frameworks and gauge their progress towards mission-critical goals." A paid service (**Define+**) builds the custom Impact Framework with the vendor's team.
- Platform capabilities (platform page):
  - **Metrics & KPIs** ("Key Impact Indicators"): "Define the metrics that need to stay consistent across your portfolio for aggregate reporting and comparability, and the ones that should stay flexible for deeper program-level storytelling… adapt without losing consistency at the core."
  - **Two-sided data collection & reporting**: requesters build "customizable question sets and conditional logic… each recipient only sees what's relevant"; "submission tracking means you always know who's submitted and who needs follow-up." Submitters get "a dedicated portal… collaborate on responses, request clarifications, and track their status. Built-in approval flows mean both sides can refine answers together." Submitter accounts are free: "Instead of submitting into a black box, they get a central hub… collaboration tools… access to their own submission history."
  - **Data integration & management**: spreadsheets/CSV/Google Sheets/software integrations (Qualtrics, SurveyMonkey, some GMS tools; custom API/RPA integrations); in-platform tables to "organize, validate, and standardize data… so every dataset is accurate and analysis-ready."
  - **Qualitative data ("Stories")**: "Capture the stories, photos, interviews, and testimonials behind your numbers, and make them as analyzable as any quantitative metric. Structured coding, categories, and program associations… feeds straight into your dashboards."
  - **Analytics & dashboards**: real-time, filter by theme/geography/time, "benchmark across programs, and drill down or roll up"; custom queries; targets and performance-vs-target tracking.
  - **Reusable visualizations & sharing**: charts reused across dashboards; "share via public links or embedded charts without exposing underlying data"; "combine metrics with narratives to tell the complete impact story."
  - **Security/admin**: role/user permissions; SOC 2 Type 2.
- Framework posture: "framework-agnostic by design — bring your own indicators, map to established standards like IRIS+, SDGs, or Impact Performance Reporting Norms, or build a hybrid."
- Explicit boundary statements (vendor-drawn seams):
  - vs GMS: "Your grants management system is the administrative backbone… **UpMetrics is the impact data and reporting layer** that sits alongside it, covering everything your GMS doesn't do well: framework design, collaborative reporting, qualitative and quantitative data collection, portfolio-level analysis, and external storytelling. The two can coexist."
  - vs BI: publishes an "UpMetrics vs PowerBI" comparison one-pager.
- Audience: grantmakers, nonprofits, impact investors, for-profit organizations; cohort/capacity-building programs where funders buy licenses for nonprofit cohorts; customer quotes emphasize storytelling ("human testimony IS assessment… data with a soul"), fundraising outcomes, and portfolio reporting (e.g., "Collecting impact data from 37 active portfolio companies").

### Clear Impact Suite (Scorecard + Compyle + Showcase)

Evidence layer: A (direct observation of homepage + Scorecard page).

- Self-positioning: "Measure What Matters. Reach Your Peak." — "software to run on, experts to lean on, and a proven framework to align around." 25 years; "300+ health departments"; "468k social impact measures in use"; "1,000s of organizations."
- The software embodies a named measurement methodology: **Results-Based Accountability™ (RBA)** — three questions: "How much did we do? How well did we do it? Is anyone better off?" The vendor also sells the framework itself: training, professional certification, an AI mentor ("Ask Mark AI") trained on the framework, community/podcast/publications.
- **Scorecard** (the measure leg) anatomy, visible in product shots:
  - **Population Accountability**: a population-level **Result** ("All children succeed in school") with community **Indicators** ("% of students reading on grade level or above") shown as baseline trend lines with latest values and direction.
  - **Performance Accountability**: program **Performance Measures** typed by the RBA questions ("How Much: number of participants", "How Well: % of trainees completing job certification", "Better Off: % of patients managing chronic conditions").
  - Per-indicator panels: "Story Behind the Curve", "Partners", "What Works", "Strategy".
- Capabilities: interactive scorecards; **Turn the Curve Planning** ("a proven step-by-step process for improving measures — tell the story behind the data and build consensus on what to do next"); strategy maps ("line of sight between individual efforts and high-level goals"); action plans & Gantt charts; AI assist (trend analysis); **live website embeds** ("embed Scorecards, graphs, strategy maps, and reports on your public site — they update automatically"); fast builder & template library; **partner linking** ("connect with partner organizations to share data, coordinate efforts, report to funders, and create collective impact"); custom + ad-hoc reporting; **language editor** ("rename software objects — 'Results' to 'Goals,' 'Measures' to 'Metrics' — to match your methodology"); CSV imports & API; browser-based.
- **Compyle** (the collect leg): "Participant data collection & case management — custom intake forms, surveys, and analytics"; responses sync into Scorecard automatically.
- **Showcase** (the communicate leg): "Public-facing impact dashboards that update automatically and build trust through transparency."
- Suite flow: "One login, one source of truth. Data flows automatically from the field to the public — no exports, no re-entry, no silos." Collect → Measure → Communicate.
- Audience: government (federal/state/local), health departments (PHAB accreditation use), nonprofits ("proving impact to boards and funders"), funders/foundations ("measuring the collective impact of their whole portfolio"), United Ways, community schools, workforce development, collective-impact coalitions, defense (SBIR/DOD).

### ActivityInfo (M&E-side corroboration for the joint review)

Evidence layer: A (direct observation of the dedicated impact-measurement page).

- URL /about/impact-measurement.html: "Impact measurement software for nonprofits and NGOs — Turn field data into measurable impact in a secure environment."
- The page markets impact measurement **as a use case of the same M&E machinery**: "Eliminate data silos, **enhance your M&E workflows**"; "Monitor and report outcomes and long-term impact at all organization levels"; "Visualize progress and impact with Dashboards and tell impact stories with Notebooks"; "Share your impact reports internally or publish them."
- The machinery beneath is unchanged from the sibling pass's findings: no-code relational databases, forms, "lock changes once results have been reported", audit log, roles/permissions, multi-partner harmonization.
- Impact measurement sits in the use-case list beside M&E, humanitarian coordination, case management, grant management, CVA, conservation, disaster risk — i.e., one configuration of the same platform.

## Cross-product Comparison

| Dimension | Sopact Sense | ImpactMapper | UpMetrics | Clear Impact Suite |
|---|---|---|---|---|
| Named methodology wrapped around the software | "Collect–Extract–Analyze–Act–Repeat" loop; Academy | theory-of-change-aligned tagging; consulting/training legs | DeCAL (Define–Collect–Analyze–Leverage); Define+ service | Results-Based Accountability™; certification, AI mentor |
| Measurement basis | one record per person/program; outcome surveys (pre/mid/post) | tag taxonomies aligned to outcomes; survey fields incl. financial | metrics/KIIs; portfolio-consistent core + flexible program metrics | results → indicators → performance measures (How much / How well / Better off) |
| Framework of record with indicator actuals per reporting period + submit/approve/lock workflow | not the center (record-per-person + surveys) | absent (surveys + tags + dashboards) | partial (two-sided reporting with approval flows — collaboration-shaped, not audit-shaped) | partial (measures with baselines; no donor-audit lock machinery at the center) |
| Qualitative evidence | interviews, notes, documents on the person's record; AI interpretation | first-class: text tagging/coding of reports & open responses; saved quotes | first-class: "Stories" — coding, categories, program associations, fed into dashboards | present but lighter (story-behind-the-curve narrative panels) |
| Collection substrate | built-in surveys + document/interview ingestion | built-in surveys + report upload + imports (Fluxx/Airtable/Submittable/Trint) | integrations (Qualtrics, SurveyMonkey, Sheets, CSV, GMS) + built-in request/question sets | built-in intake forms/surveys (Compyle) syncing to Scorecard |
| Two-sided funder↔grantee flow | grant-side use case (follow funded people to outcomes) | grant/partner-linked projects; grantee reports via surveys | explicit two-sided design (request → submit → refine → approve; free submitter portal) | partner linking for collective impact; funder portfolio solutions |
| Terminal output | instant reports; "answers you can defend" | designed impact reports & dashboards for boards/donors/communities | dashboards, public links/embeds, impact narratives | scorecards, reports, public transparency dashboards (Showcase/embeds) |
| Population/community-level results | no (person/program level) | no (portfolio/project level) | no (program/portfolio level) | yes — population accountabilities beside program performance (RBA signature) |
| Services/capacity building bundled | Academy, advisory hours | consulting, workshops, trainings (a co-equal business leg) | professional/managed services, Define+, cohort programs | training, certification, consulting (a co-equal business leg) |
| Segment center | nonprofits/workforce/foundations/impact funds | human-rights/gender/SDG funders & NGOs | US philanthropy + impact investing | US government/health/nonprofit/collective impact |

Cross-product commonalities (evidence layer B):

1. All four organize the work around a **self-defined measurement basis** — the organization's or funder's own statement of intended change with measures attached (outcome taxonomies, KIIs, RBA results/indicators/measures, per-person outcome assessments).
2. All four **gather multi-source evidence** against that basis — built-in surveys/forms plus imports/integrations; the evidence explicitly includes qualitative material in three of four (Sopact, ImpactMapper, UpMetrics) and narrative panels in the fourth.
3. All four terminate in **stakeholder-facing impact communication** — dashboards, designed impact reports, public transparency surfaces — aimed at boards, donors/funders, communities, policymakers, the public; the vocabulary is "tell the story", "prove impact", "build trust", "attract funding".
4. All four wrap **methodology + capacity-building services** around the software (academies, certifications, cohorts, consulting) — the product is sold as a measurement practice, not just a tool.
5. None of the four centers the M&E machinery of record (donor-mandated framework + period actuals + submit/review/approve/lock + audit trail). Where submission/approval exists (UpMetrics), it is collaboration-shaped (refine answers together) rather than audit-shaped (lock after reporting).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **The impact framework as the measurement basis.** The organization's (or funder's) own defined statement of the change it seeks — outcomes, goals, population results — with measures attached (indicators, KPIs/KIIs, performance measures, outcome tags). Self-defined or mapped to shared standards; the framework is the organization's impact strategy made measurable, not a donor's mandated plan of record. Remove → a strategy document / logic-model editor, or generic survey/BI tooling.
2. **The evidence base gathered against that framework.** Multi-source impact data — quantitative measures and qualitative evidence (stories, interviews, testimonials, open text) — collected directly, imported, or requested from partners/grantees, organized so it can answer the framework's questions and trace back to its sources. Remove → a framework with nothing measured, or a collection tool with no measurement purpose.
3. **The impact communication loop.** The accumulated evidence turned into stakeholder-facing impact outputs — dashboards, impact reports, stories, public transparency surfaces — aimed at funders, boards, partners, communities, and the public, to demonstrate impact, mobilize resources, and feed learning and improvement. Remove → a private data store; the demonstration is what makes the practice "impact measurement" rather than mere record-keeping.

Jointly-held load-bearing:

- 1 alone = logic-model / theory-of-change documentation tool
- 2 without 1 = survey / data-collection tool or a spreadsheet
- 3 without 1+2 = empty report/story builder
- 1+2 without 3 = monitored spreadsheet / private evidence store (machinery without demonstration)
- 1+3 without 2 = storytelling without evidence
- 2+3 without 1 = BI dashboards with no measurement basis

Domain binding: mission-driven social impact — nonprofits, philanthropy, impact investing, community collaboratives. Remove → corporate BI, ESG compliance management, or government internal performance regimes.

### L1 — Common Mature Structure

- Survey/form-based collection instruments, including pre/post (pre/mid/post) assessment designs
- Qualitative evidence handling as a first-class citizen: open-text analysis, coding/tagging against outcome taxonomies, stories of change, saved quotes, testimonials
- Chart builders and dashboards; reusable visualizations shared by link or embed
- Baselines and targets with progress-vs-goal views
- Portfolio/program-level aggregation and cross-program benchmarking (funder side)
- Two-sided reporting workflows (funder requests ↔ grantee/portfolio submissions, with collaboration and approval)
- Framework-agnostic standards mapping (IRIS+, SDGs, sector norms)
- Public-facing transparency surfaces (public dashboards, auto-updating embeds)
- Role-based access and security certification (SOC 2 class)
- Methodology guidance and capacity-building services wrapped around the software (market characteristic of the Type)

### L2 — Variant / Optional Structure

- Methodology substrate: RBA scorecard vs theory-of-change tag taxonomies vs KII frameworks vs per-person outcome records — different vocabularies for the same three-leg core (one product even ships a language editor to rename objects to the customer's methodology)
- Population/community-level results beside program-level performance (collective impact; RBA's population accountabilities) vs program/portfolio-only
- Segment packaging: nonprofit-self-serve vs funder-portfolio vs impact-investor vs government/health vs corporate CSR/ESG adjacency
- Two-sided depth: single-org self-measurement vs funder-run multi-grantee measurement networks
- AI analysis layers (era-current: auto-tagging, AI insights, AI report assistants, AI mentors)
- Adjacent modules on the same substrate: case management, application/grant intake (Sopact, Compyle) — packaging variants, not the core
- Public transparency depth (private dashboards → public embeds → dedicated public portals)

### L3 — Vendor-specific Structure (Research Notes only)

- Sopact: "Intelligent Cells / Intelligent Rows", MCP (Claude/ChatGPT) integration, usage-metered AI analyses, 2-month paid pilots
- ImpactMapper: Fluxx and Trint APIs, ambassador program/fellowship, Global South free-license fund, surveys-only tier
- UpMetrics: DeCAL branding, Define+ service, Stories 2.0 (Aug 2026 release), cohort programs in 10+ US communities, "vs PowerBI" one-pager
- Clear Impact: Ask Mark AI, Virtual RBA Facilitator videos, PHAB accreditation support, Showcase product, RBA licensing terms, GSA contract holder status

## Vendor-specific Findings

- The **services wrap** (training/certification/consulting/cohorts) is co-equal to software in two of four sampled vendors (ImpactMapper, Clear Impact) and a major revenue line in the other two — a market characteristic worth noting, but a service layer, not a software structure; it does not enter the definition.
- **Population-level results** (community indicators beyond any single program) are an RBA/Clear Impact signature; the other three sample at program/portfolio level. Held as a variant axis, not definitional.
- **Two-sided reporting** is explicit product architecture in UpMetrics, present as grant-linked projects in ImpactMapper and grant-side use case in Sopact, and partner-linking in Clear Impact — common-mature, not definitional (single-org self-measurement deployments exist).

## Boundary Findings

### vs Monitoring & Evaluation Platform (the flagged joint review — DISCHARGED from this side)

The seam holds at **center of gravity**, confirmed from this side with vendor-side corroboration in both directions:

- **M&E Platform** (sibling pass): machinery-first **system of record** for funded program implementation — the program's results framework of record + indicator actuals accumulated per reporting period + the quality workflow (submit → review → approve → lock, audit trail) + accountability reporting to oversight parties. The framework is the funded program's mandated plan; the record exists to be audited.
- **Social Impact Measurement** (this pass): practice-first **measurement and demonstration layer** — the organization's/funder's self-defined impact framework + a multi-source evidence base in which qualitative evidence is first-class + stakeholder-facing impact communication for learning, fundraising, and credibility. The practice exists to demonstrate and improve impact, not to satisfy a donor's audit.
- Corroboration, M&E side: ActivityInfo markets "impact measurement" as a use-case page on unchanged machinery ("enhance your M&E workflows"; "lock changes once results have been reported") — feature presence cannot separate the leaves, exactly as the sibling pass predicted.
- Corroboration, SIM side: UpMetrics explicitly positions itself as "the impact data and reporting layer" alongside the grants system and against compliance ("Impact reporting built for learning and growth, not just compliance"); UpMetrics even publishes a comparison against PowerBI.
- The handed test resolves positively for keep-both: remove the practice/communication orientation from an M&E platform → the machinery remains (ActivityInfo's impact page changes nothing structural). Remove the framework/actuals/reporting machinery of record from the SIM side → **practice tooling remains, and it is a real market**: ImpactMapper runs a substantial, named-customer business on surveys + outcome tags + dashboards + designed reports with no period-actuals record and no audit-lock workflow at all.
- Straddle zone (packaging, not Type collapse): TolaData ("impact management suite", sampled by the sibling pass), SoPact (case management + impact intelligence), Clear Impact (government performance + nonprofit impact), Bonterra "Impact Management", ActivityInfo's impact page. These vendors sell both vocabularies from one substrate; the center of gravity still separates them.
- **Keep-both RATIFIED from this side.** The two Types share machinery vocabulary (framework, indicators, reporting) but differ in whose framework it is, what the record is for, and what the terminal output is.

### vs Survey Platform / Online Form Builder

Collection-only tools center the form and lack both the measurement basis and the communication loop. Vendor-drawn: UpMetrics integrates Qualtrics/SurveyMonkey rather than replacing them; ImpactMapper's surveys are one leg of a measurement practice (participant self-tagging "according to your custom outcomes"); Sopact's FAQ explicitly answers "What makes Sopact different from a survey tool?" — connection to the person/program and interpretation with evidence.

### vs BI / Dashboard Platform

BI is domain-agnostic analysis of arbitrary data; SIM carries impact semantics (frameworks, outcomes, stories, funder-facing impact reports, public trust surfaces). Vendor-drawn: UpMetrics' "vs PowerBI" comparison.

### vs Grantmaking Platform / Grants Management System

Money and relationship records vs impact evidence. Vendor-drawn: UpMetrics' FAQ ("Your grants management system is the administrative backbone… UpMetrics is the impact data and reporting layer that sits alongside it"); ImpactMapper imports from Fluxx rather than managing grants.

### vs Nonprofit Case Management

Case management centers person-level service episodes; SIM centers aggregate impact evidence against a framework. Straddle: Sopact and Compyle bundle case management beside impact measurement — packaging on one substrate.

### vs Government Performance Management

Shares indicator/reporting machinery; differs in institutional context (government bodies' own performance regimes vs mission-driven impact demonstration to funders/communities). Clear Impact literally serves both audiences from one product — the clearest straddle; consistent with the M&E pass's note. Center-of-gravity call.

### vs ESG Management / Sustainability Reporting

ESG centers regulatory/disclosure compliance for companies; SIM centers mission impact for social-purpose organizations. Straddle: Sopact's "Impact & ESG Portfolio" and impact-investor segment (impact funds measuring portfolio companies) — the impact-investing pole sits between the two Types; recorded as a boundary note, not resolved here.

### vs Nonprofit Program / Project Management

Activities, schedules, and workplans vs measured change. Activities appear in SIM products only as attribution context (programs associated with stories/metrics), never as schedulable work.

## Uncertainties

- **eImpact unreachable** — the reporting-first pole (impact-report builders) could not be verified; the communication leg's thinnest form is therefore described from the sampled products' reporting surfaces, not from a dedicated reporting tool. If eImpact-class products lack frameworks AND collection entirely, they might sit below the Type floor (report-builder territory) — flagged, unresolved.
- **Help-center depth**: no Tier-1 operational article was fetched for any sampled product; internal workflow details (exact roles, status names, limits) are unknown and deliberately not asserted. The two-sided approval flow in UpMetrics is known only at product-page depth.
- **Segment edges**: the impact-investing pole (IRIS+, portfolio KIIs) and the corporate ESG pole were observed only through Sopact/UpMetrics positioning; a dedicated impact-investor measurement product was not sampled.
- **Market-size claims** on vendor pages (e.g., "468k social impact measures in use", "1,300+ active users") are vendor marketing figures, recorded but not endorsed.

## Historical / Market-Sample Check (§24)

Would older, regional, or differently-positioned practice still fit the definition?

- **Paper-era practice**: a nonprofit that writes its theory of change / outcome framework (leg 1), tracks indicator values and collects beneficiary stories in a spreadsheet and a folder of interviews (leg 2), and produces an annual printed impact report for funders and the community (leg 3) — satisfies all three legs with no software at all. The definition names no surveys, AI, cloud dashboards, or standards libraries.
- **RBA itself predates the sampled software**: Results-Based Accountability originates in Mark Friedman's framework work (the vendor's own materials present the framework as a 25-year method the software embodies); a paper scorecard with baseline + "story behind the curve" satisfies the core.
- **Regional/international practice**: ImpactMapper's human-rights/gender/SDG segment and UN-initiative meta-analyses show the Type is not US-philanthropy-specific; community foundations and United Ways show it is not development-sector-specific either.
- Conclusion: the definition survives the historical check; nothing era-current (AI, SOC 2, public embeds, IRIS+ mapping) is load-bearing.

## Final Synthesis

A **Social Impact Measurement** application is the mission-driven organization's (or funder's) impact measurement and communication practice made software: it holds the organization's self-defined impact framework — the change it seeks with measures attached — as the measurement basis; gathers a multi-source evidence base against that framework, in which quantitative measures and qualitative evidence (stories, interviews, open text) stand side by side; and turns the accumulated evidence into stakeholder-facing impact communication — dashboards, impact reports, stories, public transparency surfaces — that demonstrates impact to funders, boards, partners, and communities and feeds learning and improvement.

Its center of gravity is the **practice** (define → gather → interpret → communicate → improve), typically wrapped in methodology guidance and capacity-building services; its machinery is lighter than an M&E platform's, its framework is self-defined rather than donor-mandated, qualitative evidence is first-class rather than narrative attachment, and its terminal output is demonstration and mobilization rather than audited accountability. That is the seam against the Monitoring & Evaluation Platform, and it holds at center-of-gravity strength with vendor corroboration on both sides — the two Types are siblings sharing vocabulary, not aliases.
