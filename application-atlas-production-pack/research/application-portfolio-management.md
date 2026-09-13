# Research Notes — Application Portfolio Management

Research date: 2026-09-06
Methodology: v1.1 (update-v1)

## Research Goal

Understand what an Application Portfolio Management (APM) application actually is as a Type: what its managed objects are, who uses it, how the portfolio is built, assessed, and changed over time, and where its boundary lies against CMDB, IT Asset Management, SaaS Management, Project Portfolio Management, and Enterprise Architecture management platforms.

Note: this leaf is the *portfolio* APM (Directory section 14, IT, Cloud & Infrastructure), not Application Performance Monitoring — the acronym collision is worth recording but the directory context is unambiguous.

## Initial Boundary

Working hypothesis before research:

- Core use: an organization-wide register of its own software applications, each carrying ownership, business/technical assessment, lifecycle position, and a disposition decision; reviewed on an ongoing cycle to decide what to keep, invest in, consolidate, or retire.
- Users: enterprise architects, application/portfolio managers, application owners, IT leadership.
- Nearest neighbors: CMDB (operational configuration), IT Asset Management (procure-to-retire assets), SaaS Management (SaaS discovery/spend), Project Portfolio Management (projects, not applications), EA management platforms (broader modeling).
- Main confusion risk: "APM" = Application Performance Monitoring (different Type entirely); and APM products are usually branded "Enterprise Architecture" tools, so the Type risks being defined by one vendor philosophy.

## Research Questions

1. What is an "application" record in these systems? What attributes does it carry?
2. What lifecycle model do applications follow? Who maintains it?
3. How does assessment work (criteria, scoring, classification models, data collection)?
4. What is the rationalization decision loop (steps, roles, outputs)?
5. What interfaces exist (inventory, matrix/bubble views, dashboards, roadmaps, surveys)?
6. What roles exist (portfolio manager, EA, application owner, technical expert, executive)?
7. What data flows in (discovery, CMDB, financial systems, vendor EOL data) and how is data quality governed?
8. Where is the boundary vs CMDB / ITAM / SaaS management / PPM / EA management?

## Representative Products

| Product | Philosophy | Customer tier | Evidence obtained |
|---|---|---|---|
| SAP LeanIX | Pure-play APM/EA SaaS built around "fact sheets"; APM is a named product inside LeanIX Enterprise Architecture | Mid-size to large enterprise | Deep: vendor wiki guides (APM guide, application rationalization guide), product/site pages |
| Ardoq | Data-driven, graph-metamodel EA platform; APM and Application Rationalization are packaged "Solutions" | Mid-size to large, consultancy-heavy | Deep: help-center use-case collection + full operational "Getting Started with Application Rationalization" article + solution pages |
| ServiceNow APM | Suite module: application portfolio as part of Strategic Portfolio Management, anchored on the CMDB | Large enterprise | Positioning only: product page timed out twice; docs portal is a JavaScript application that cannot be fetched. All ServiceNow-specific claims kept at positioning level |

Rejection notes: Bizzdesign and Orbus iServer were attempted as additional EA-suite samples; both candidate URLs returned 404 and were dropped rather than substituted with model-memory claims. Three samples with two deep + one positioning-level are sufficient to establish stable commonality (workflow stop conditions met).

## Sources

### LeanIX (SAP LeanIX)

- https://www.leanix.net/en/ — product home: positioning, product family (APM / Technology Risk and Compliance / Architecture and Road Map Planning), use-case list, pricing model (priced by number of applications, unlimited users). Fetched 2026-09-06.
- https://www.leanix.net/en/wiki/apm/application-portfolio-management — "Application Portfolio Management — The Definitive Guide": definition of APM practice, what APM involves, stakeholder questions, 8-step getting-started method. Fetched 2026-09-06.
- https://www.leanix.net/en/wiki/apm/application-rationalization — "Application Rationalization — The Definitive Guide": definition, 6-step rationalization process, assessment criteria, TIME/6Rs target-state outcomes, roadmap waves, continuity principle. Fetched 2026-09-06.
- docs-eam.leanix.net (product documentation) redirects to SAP Help Portal, which is a JavaScript application — not fetchable. 2 attempts, abandoned.

### Ardoq

- https://www.ardoq.com/solutions/application-portfolio-management — APM solution page: benefits, related use-case family (Application Rationalization, Application Lifecycle Management, Application Hosting, Application Integration Management). Fetched 2026-09-06.
- https://help.ardoq.com/en/ — help center root: collection structure (Fundamentals, Use Case Solutions, Data Input/Visualization/Analysis, Integrations, Users and Access Management, etc.). Fetched 2026-09-06.
- https://help.ardoq.com/en/collections/6889-ardoq-use-case-solutions — use-case collection index: Application Rationalization, Application Hosting, Application Integration Management, IT Cost Management, IT Lifecycle Management, Capability Based Planning, Strategy to Execution, Technical Debt Management, Governance/Risk/Compliance. Fetched 2026-09-06.
- https://help.ardoq.com/en/articles/44015-getting-started-with-application-rationalization — full operational guide: prerequisites, 4-step workflow, roles (Owner/Expert), surveys, TIME bubble chart, Strategic Rating, executive/builder dashboards, risk triage, roadmap/timeline, viewpoints. Fetched 2026-09-06.

### ServiceNow

- https://www.servicenow.com/products/application-portfolio-management.html — timed out twice (2 attempts, abandoned).
- https://docs.servicenow.com/ — APM documentation is served by a JavaScript application; content not retrievable in this environment. Recorded as a source-access limitation; no ServiceNow-specific operational detail is asserted anywhere below or in the final document.

## Product Observations

### LeanIX (evidence layer A unless noted)

Positioning (site + wiki):

- APM defined as "the practice of governing and optimizing inventories of software applications to achieve precise business objectives … by creating transparent overviews of IT application landscapes to evaluate IT costs, standardize software throughout business units and promote agility and innovation."
- APM as practiced in large enterprises involves: documenting past, present, and future applications (deployed or planned); identifying/automating changes to application service lifecycles; organizing applications according to business capabilities; arranging IT components into technology stacks; grading the technical and functional value of applications.
- Product family around the APM product: Technology Risk and Compliance; Architecture and Road Map Planning; separate SaaS Management product; use cases: Application Portfolio Assessment, Application Rationalization, Application Modernization, Obsolescence Risk Management, Post-Merger IT Integration, AI Governance.
- Pricing is based on the number of applications in the landscape with unlimited users — the application record is the unit of value (A).
- Stakeholder questions APM answers: which apps deserve investment vs which to divest; which applications inadequately support business capabilities; gaps and overlaps (multiple apps per capability, per region); whether the portfolio develops in the right direction (lifecycle/EOL, successors, application roadmap).

Method (wiki "getting started", 8 steps):

1. Compile a list of applications (past, present, future; use SaaS management to identify SaaS).
2. Identify who owns the application (stakeholders/users; discover unused apps).
3. Identify the lifecycle of the application (value/risk profile changes across lifecycle; end-of-life risks).
4. Assess usage of applications.
5. Establish business value, quality, and costs per application (TCO; compare using business capabilities).
6. Create an application architecture framework (rationalization framework; target concepts).
7. Map the target concept onto the landscape; design an implementation roadmap (business leaders, IT heads, EAs review recommended actions per application).
8. Make rationalization a continuous process.

Assessment machinery:

- Simple pragmatic model used in LeanIX EAM core reports: per-application **functionality**, **technicality** (technical fit), **strategic value**, **costs**, and **data-related aspects**; collected collaboratively with all application owners using **custom surveys**.
- Advanced model mentioned: Beyer–Smertnig — criticality and support scored on a −2…+2 scale (A that this model is documented; the scale values are vendor-published guidance).
- For every application, TCO is recorded alongside criteria such as strategic value, available skills, user satisfaction, availability of alternatives.

Target state and roadmap:

- Methodologies: Gartner TIME model or 6Rs; four general outcomes regardless of method: **Keep** (invest further / tolerate), **Update** (modernize high-value apps on aging technology), **Migrate** (retire + migrate data/users to an existing app; standardize; merge; replace with COTS), **Eliminate** (retire without replacement).
- Rationalization executed "in waves" — immediate, mid-term, long-term (eliminations; migrations/consolidations; full rewrites/upgrades).
- Reports/views: application matrix (capabilities × applications, per user group/region), application landscape views colored by functional/technical fit, lifecycle reports, application roadmap.
- Scope guidance: rationalize per business capability or org unit, not all at once; involve business and IT leaders.
- Integrations named: SaaS management discovery, cloud vendors, Jira ("connecting EA planning to IT execution"), application TCO capabilities for cost capture/allocation.

### Ardoq (evidence layer A)

Positioning (solution page):

- APM = "manage low-value systems out of your IT portfolio"; benefits: application overview with costs; application owners visibility; investment control (where to increase investment, which applications to phase out); cost savings via capability-level candidates; risk management through rationalization.
- Use-case family split into separate packaged solutions: APM, Application Rationalization (distinct from APM), Application Lifecycle Management, Application Hosting, Application Integration Management, Business Capability Modeling, ERP Transformation, IT Lifecycle Management, Strategy to Execution.

Operational workflow ("Getting Started with Application Rationalization"):

- Definition: "the continuous process of assessing your organization's application portfolio and strategically deciding which applications can be kept, replaced, retired, or merged."
- Prerequisites: baseline data from Ardoq Foundation (Applications, People, Business Capabilities); Application Integration Management (captures how applications talk to each other → "determines how difficult to replace an application is"); IT Cost Management (CAPEX/OPEX → application *Total Direct Cost*).
- Step 1 — Review your application portfolio: validate baseline; every application must have both an **Owner** (provides business value sentiment) and an **Expert** (provides technical fit details); data can be loaded via Excel importer, ServiceNow integration, or Ardoq Surveys.
- Step 2 — Capture application details: surveys to owners/experts for interfaces, hosting, cost (CAPEX/OPEX rolls up to Total Direct Cost); a **Data Governance dashboard** verifies completeness and tracks discrepancies.
- Step 3 — Assess: applications visualized in the **TIME framework** (Tolerate/Invest/Migrate/Eliminate) on a **Bubble Chart**; **Strategic Rating** is an automated recommendation computed from assessment criteria; Executive Dashboard tracks Strategic Rating trend month-over-month, candidate operational cost over 1-year and 1–2-year runways, candidate tables; Builder dashboard for EAs computes a **Structural Complexity Score** (realized capabilities + integrations + connected infrastructure) and flags **Capabilities at Risk** (application is the single point of realization for a capability); **Rationalization Timelines** categorize upcoming workload by action track (Elimination / Investment / Migration) using end-of-life dates; risk triage distinguishes "urgent/high risk" (expiring within 1 year *with* capabilities at risk) from "quick wins" (expiring within 1 year, no capabilities at risk, low structural complexity).
- Step 4 — Plan and execute: impact assessment via Dependency Map, Block Diagram, and Timeline views before retiring a target; viewpoints such as "Connected Org Unit and Capabilities" and "Business Capabilities Realized by Applications"; rationalization roadmap built on the Timeline view with per-rating and lifecycle formatting.
- Roles implied: enterprise architects (run the exercise), application owners (business value), technical experts (technical fit), executives (dashboard consumers).
- ServiceNow appears here as an *integration/data source* into the portfolio (also confirming the CMDB-as-feeder pattern).

### ServiceNow APM (positioning-level only)

- Product exists and is named "Application Portfolio Management" within the ServiceNow platform family; official docs unreachable in this environment.
- No operational specifics asserted. Its role in this research is to confirm that the suite-module-on-ITSM-platform form exists as a major market position (also independently confirmed by Ardoq's ServiceNow integration and the general market structure).

## Cross-product Comparison

| Dimension | LeanIX | Ardoq | Common? |
|---|---|---|---|
| Managed unit | Application "fact sheet" — one record per application, priced per application | Application component node in a graph metamodel | **Yes — application-as-record is the invariant** |
| Register scope | Past, present, and future (planned) applications | Baseline application portfolio validated before assessment | Yes (register covers current + planned; retired history kept) |
| Accountability | Identify owner per application (step 2) | Every application must have Owner (business value) + Expert (technical fit) | Yes — accountable ownership per application |
| Assessment basis | Functionality / technical fit / strategic value / costs / data aspects; collected from application owners via surveys | Business value from Owner, technical fit from Expert, cost from IT Cost Management; collected via surveys | Yes — value × technical fit × cost, collected from accountable people via surveys |
| Lifecycle | Application service lifecycles; EOL identification as a core step; obsolescence risk use case | End-of-life dates drive rationalization timelines; lifecycle data on records | Yes — per-application lifecycle/EOL tracking |
| Disposition model | TIME / 6Rs → Keep / Update / Migrate / Eliminate | TIME (Tolerate / Invest / Migrate / Eliminate), Strategic Rating auto-recommendation | Yes — value×fit quadrant classification into keep/invest/migrate/eliminate-family categories |
| Decision loop | 8-step method ending in "continuous process" | "Continuous process of assessing…"; roadmap built in Timeline; progress tracked month-over-month | Yes — recurring assess→decide→plan→execute loop |
| Roadmap | Implementation roadmap in waves (immediate / mid-term / long-term) | Rationalization roadmap on Timeline view | Yes |
| Risk checks before acting | Successor planning before EOL; security/compliance concerns for obsolete apps | Structural Complexity Score; Capabilities at Risk; dependency maps before retiring | Yes — dependency/capability risk gating retirement |
| Capability mapping | Organize applications according to business capabilities (core practice) | Business Capability Modeling is a Foundation prerequisite for rationalization | Yes across sample — but historically optional; L1 |
| Dependency/interface tracking | "Map data flows and application dependencies" as APM benefit | Application Integration Management is a packaged prerequisite solution | Yes — L1 |
| Cost capture | TCO per application; application TCO capabilities | CAPEX/OPEX → Total Direct Cost per application | Yes — L1 |
| Data sourcing | SaaS discovery, integrations (cloud, Jira) | Excel import, ServiceNow integration, surveys | Yes — L1 (sources vary) |
| Data quality governance | Continuous maintenance emphasized; survey-based refresh | Data Governance dashboard to verify completeness/track discrepancies | Yes — L1 |
| Product form | Pure-play SaaS; APM product inside EA suite; priced per application | Pure-play SaaS graph platform; APM/Rationalization as packaged "Solutions" | Variant |
| Executive reporting | Reports for CIO/CTO stakeholders; roadmap reports | Executive Dashboard (savings potential, rating trends) | Yes — L1 |
| Suite/CMDB anchoring | Standalone (integrates outward) | Standalone (imports from ServiceNow) | ServiceNow = suite module anchored on CMDB (positioning only) — Variant |

## Canonical Model (synthesis)

Defining core (L0):

1. **Organization-scoped application register** — the organization's own applications (bought, built, planned; past and present) as identified, individually managed records. The application — not a license, device, server, or project — is the portfolio unit.
2. **Accountable ownership per application** — each record has at least one accountable person/role providing the business perspective (and in practice a technical counterpart).
3. **Per-application portfolio assessment** — recorded business value/fit and technical fit/health judgments (plus cost where practiced), collected from the accountable people.
4. **Tracked lifecycle and disposition state** — each application carries a lifecycle position (including vendor end-of-life where known) and a disposition classification derived from assessment (keep/invest/tolerate vs modernize vs migrate/consolidate/replace vs retire).
5. **Recurring rationalization loop** — the portfolio is re-assessed on an ongoing cycle and portfolio-change decisions are recorded and planned (roadmap), rather than the register being a one-time inventory.

Remove the register → no APM. Remove ownership/assessment/lifecycle → a plain software inventory. Remove the decision loop → a static catalog (CMDB slice). Remove disposition → inventory, not portfolio management.

Common mature structure (L1): business capability mapping; application dependency/interface tracking; per-application cost capture (TCO/CAPEX/OPEX); technology-stack linkage and vendor-EOL/obsolescence data; survey machinery for collecting assessments; matrix/bubble classification views; executive dashboards (portfolio health, savings potential); rationalization roadmaps in waves; data-quality/completeness governance; integrations for register population (CMDB, discovery, ERP/financial, SaaS discovery); role separation between architects/managers, owners, technical experts, executives.

Variant / optional (L2): product form (pure-play APM/EA SaaS vs ITSM-suite module vs EA-suite module vs spreadsheet practice for small organizations); scope extensions sold as adjacent solutions (application risk & compliance, cloud migration, ERP transformation, post-merger integration, technical debt, strategy-to-execution); assessment-model depth (simple pragmatic criteria vs multi-criterion scoring scales); future-state/scenario modeling; SaaS vs on-prem delivery; licensing model (per-application vs per-user).

Vendor-specific (L3): LeanIX fact-sheet meta-model and per-application pricing; named integrations (Jira etc.); Beyer–Smertnig scoring model; Ardoq packaged Solutions (Foundation, AIM, ITCM, AR), Survey machinery, Structural Complexity Score, specific viewpoints/dashboards; ServiceNow CMDB-anchored module structure (unverified detail).

## Anti-overfitting Checks

- Shared implementation patterns that are NOT definitional: TIME quadrant as the *specific* taxonomy (both deep samples use TIME-family categories, but the older/neutral form is "a disposition classification derived from assessment"; TIME is one popular method); surveys as the specific collection mechanism; business-capability mapping as mandatory (both deep samples practice it, but spreadsheet-era and CMDB-anchored portfolios can run without capability maps).
- Historical / market-sample check: would spreadsheet-maintained portfolios (LeanIX itself recommends spreadsheets for small organizations), 2010s on-prem EA repositories, or CMDB-derived application lists still fit the L0? Yes — register + ownership + assessment + disposition + recurring review all predate modern SaaS packaging. L0 survives the check.

## Vendor-specific Findings

- LeanIX: pricing by number of applications with unlimited users (signals the application record as the value unit); product split APM / Technology Risk & Compliance / Architecture & Road Map Planning; use of Gartner TIME and 6Rs framing; Beyer–Smertnig model; "70% of organizations lack referenceable portfolio documentation" and other statistics are vendor marketing claims — not treated as facts.
- Ardoq: Solutions packaging (AR solution depends on Foundation, AIM, ITCM); Owner/Expert dual role; Strategic Rating as automated recommendation; Structural Complexity Score; Capabilities at Risk; 1-year expiration risk triage; "5 applications per capability" default threshold is explicitly customer-adjustable (do not generalize).
- ServiceNow: suite-module form factor; operational detail unverified.

## Boundary Findings

- **vs CMDB**: CMDB records configuration items to support operational processes (incident, change); the application portfolio records applications as *investment/decision* objects. Evidence: Ardoq consumes ServiceNow as a data source for the portfolio; the operational system and the decision layer are distinct products/integrations. Test: remove assessment/disposition/roadmap and you have a CMDB/software catalog; remove operational state tracking and you have APM.
- **vs IT Asset Management**: ITAM spans procure-to-retire across asset classes (hardware, licenses, contracts) with financial/legal focus; APM's unit is the application as a carrier of business capability and an investment decision. Overlap: the application inventory itself. Test: remove license/contract/asset-financial management and you have APM; remove value/fit assessment and disposition you have ITAM's software slice.
- **vs SaaS Management**: SaaS management discovers subscriptions/spend and manages the SaaS lifecycle; in these products it is explicitly an *input* to the portfolio register (LeanIX: "use the SaaS management process to identify SaaS applications"; LeanIX sells SMP separately). Test: a SaaS management product without portfolio disposition is not APM.
- **vs Project Portfolio Management**: PPM's objects are projects/investments/demands; APM's objects are applications in operation and the planned change of the estate. Roadmaps connect the two (retirement → replacement project). Test: if the managed record is a project with start/end rather than a long-lived application record, it is PPM.
- **vs Enterprise Architecture management platforms**: market reality — the leading APM vendors brand themselves as EA tools (LeanIX and Ardoq both cite Gartner EA Tools Magic Quadrant). APM is the core use case; capability/process/target-architecture modeling is breadth. The directory has no separate "Enterprise Architecture management platform" leaf, so this leaf effectively carries that market. Recorded as a taxonomy note, not silently restructured.
- **vs Application Performance Monitoring**: name collision only ("APM"); different Type entirely (runtime telemetry of running services). No overlap in objects or users.

## Uncertainties

- ServiceNow APM operational specifics (record model, lifecycle states, workflow) unverified — official docs unreachable; all ServiceNow claims kept positioning-level.
- Exact lifecycle phase vocabularies differ by product (planned/active/EOL/retired family; Ardoq leans on EOL dates, LeanIX documents "past, present, future"). Present as conceptual states with varying labels; do not universalize.
- Whether business-capability mapping is universal: standard across the deep sample and strongly expected in the market, but historically optional → kept out of the defining core.
- Bizzdesign/Orbus not examined (404s); EA-suite-module philosophy represented only indirectly. Low risk to the synthesis, since the deep samples already diverge on form factor.
- Numerical claims in vendor materials (average app counts, savings percentages) are marketing statistics and were deliberately not carried into the final document.

## Final Synthesis

An Application Portfolio Management application is an organization-facing management application whose world is the organization's own application estate turned into a governed portfolio: a register where every application is an individually owned, assessed record with a lifecycle position and a disposition, and a recurring rationalization loop that classifies the portfolio (value × technical fit), plans portfolio change in waves (keep / modernize / consolidate / replace / retire), and tracks execution against the register. Capability maps, dependency networks, cost capture, survey-driven data collection, executive dashboards, and integrations from CMDB/discovery/SaaS sources are the standard supporting machinery; the defining core is the register + ownership + assessment + lifecycle/disposition + recurring decision loop.
