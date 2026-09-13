# Research Notes — Nonprofit Program Management

Research date: **2026-09-08**

## Research Goal

Understand what software sold or used as "nonprofit program management" actually is in the market: what a "program" is in these systems, what machinery surrounds it (planning, delivery, people, money, performance), and where this Application Type begins and ends relative to the already-processed §25 siblings (nonprofit case management, beneficiary management, monitoring & evaluation platform, nonprofit grant management, nonprofit management platform, nonprofit CRM).

## Initial Boundary

Working hypothesis at start:

- The leaf should be the **initiative/container side** of mission delivery: the organization's own programs as planned, structured offerings — distinct from the people/cases inside them (Nonprofit Case Management), the registry of served people (Beneficiary Management), and the results/indicator machinery (Monitoring & Evaluation Platform).
- The sibling nonprofit-case-management pass left an explicit flag: "programs as initiatives/containers (plans, budgets, milestones) vs the people and cases inside them; enrollment binding means each Type references the other's central object."
- The sibling monitoring-evaluation-platform pass left a note: "activities appear in M&E platforms as attribution context and reporting units, not schedulable work."
- Known risk: "program management" collides with two other senses — (a) the PMI/portfolio sense (a program = a group of projects), and (b) case-management products whose vendors use "program" loosely for service delivery. Also, most products in this space are sold under adjacent labels ("case management", "M&E software"), so a distinct product population answering exactly to "nonprofit program management" was not guaranteed.

## Research Questions

1. What is a "program" in these products — a service offering, a portfolio of projects, an enrollment container, or a results framework?
2. What is planned inside a program, and what machinery does the product provide for planning (schedules, sessions, workplans, milestones, budgets)?
3. How is delivery recorded (services delivered, sessions held, attendance, milestone sign-offs)?
4. Do identified people (participants/beneficiaries) live in the system, or only aggregate counts?
5. How does program performance get measured and reported (goals, indicators, dashboards, funder/board reports)?
6. Where does money sit (program budgets, funding sources, disbursements)?
7. What are the exact boundaries vs Nonprofit Case Management, Beneficiary Management, Monitoring & Evaluation Platform, Project Management Application (§03.07), and Nonprofit Grant Management?
8. Is this leaf a real Type, an alias, or only a module framing of neighbor Types?

## Representative Products

Selected for different philosophies, sectors, and tiers:

| Product | Sector / posture | Philosophy | Tier of evidence |
|---|---|---|---|
| DevResults | International development, specialist SaaS | Workplan/results-centric: program = portfolio of projects with workplans, budgets, indicators | Tier 1 (Knowledge Base + official tour) |
| Salesforce Nonprofit Cloud — Program and Outcome Management | Enterprise platform module | Suite module: programs + services + sessions + enrollment + outcomes/indicators, case management adjacent | Tier 2 (official product page; help center unreachable) |
| Bonterra Apricot (Social Solutions) | US human services, mid-market SaaS | Service-delivery-centric: programs organize participant service delivery (enrollments, rosters, attendance) | Tier 2 (official product page + FAQ; help center unreachable) |
| ActivityInfo | International development/humanitarian, M&E machinery | Boundary sample: data-collection + indicator-reporting machinery without program-offering planning/delivery loop | Tier 1 (official documentation index) |

## Sources

Accessed 2026-09-08:

- DevResults official site: https://www.devresults.com/ (positioning, "Manage" capability, dashboard description)
- DevResults official tour: https://www.devresults.com/tour (workplan, budget, checklists, program dashboard)
- DevResults Knowledge Base: https://help.devresults.com/ (index), https://help.devresults.com/help/projects-and-organizations (section index incl. "Define a Project" summary: "Preparing a project (formerly, 'activity') for reporting requires assigning reporting periods, indicators, and geographic places")
- Salesforce Nonprofit: https://www.salesforce.com/nonprofit/ (portfolio positioning, "Program and Outcome Management" solution link)
- Salesforce Program and Outcome Management page: https://www.salesforce.com/nonprofit/program-management-software/ (capability blocks and FAQ)
- Bonterra Apricot: https://www.bonterratech.com/product/apricot (positioning, feature list, FAQ, customer quote)
- Bonterra support: https://www.bonterratech.com/support (contact form only — no public KB)
- ActivityInfo documentation index: https://www.activityinfo.org/support/docs/index.html (docs structure), https://www.activityinfo.org/ (404 page exposing use-case list)

**Source-access limitations (recorded per evidence rules):**

- help.salesforce.com is a JavaScript application; fetches failed (CSS error). Two search-engine attempts to locate mirrored help articles failed (search ignored site filters). Salesforce evidence is therefore **product-page (Tier 2) only**; object-level data-model claims are NOT made from memory.
- Bonterra/Apricot help center was not reachable (help.socialsolutions.com redirects to the product page; /support is a contact form; public GitHub docs 404). Apricot evidence is **product-page (Tier 2) only**, with reduced assertion strength.
- PlanStreet (candidate "program management software" self-label) — transport error; abandoned after one failure.
- WebFetch of global.bing.com did not honor site-restricted queries; abandoned.

Consequence: assertions about enrollment/attendance/scheduling machinery at Salesforce and Apricot rest on official marketing/FAQ pages, not operational help documentation. These are held at "product page evidence" strength and phrased cautiously in the final document. No precise numeric limits, default values, or object schemas are asserted anywhere.

## Product Observations

### DevResults (international development; Tier 1)

Evidence layer: **A (directly observed)** — official site, tour, and knowledge base.

- Self-positioning: "Cloud-based M&E software for development projects and data", but also "DevResults is a **web-based project management tool** specially designed for the international development community" (tour, Overview). The "Manage" capability: "Plan and implement your projects with easy-to-use tools."
- **Program** = the whole portfolio in its own vocabulary: the dashboard "gives you a snapshot of your program at a glance"; the org sets up "your program's results framework"; targets can be set "at the program level and/or at the project level".
- **Project** (formerly "activity") is the managed container. KB: "Preparing a project (formerly, 'activity') for reporting requires assigning reporting periods, indicators, and geographic places." KB section "Program Information → Projects and Organizations".
- Planning machinery per project: a **workplan** view "at a glance, including milestones, deliverables, reporting periods, and other calendar events"; **checklists** configurable to the organization's standard processes, milestones with due dates, overdue milestones flagged, "authorized staff can sign off on tasks as **complete & approved**".
- Money machinery per project: a **budget** with "any number of line items"; the project register "tracks **disbursements and expenses** against this budget"; burn rates and outstanding advances; **multiple funding sources** (awardee contributions, host government contributions, other donors); **multiple currencies** with automatic conversion to a primary currency.
- Performance machinery: **results framework** setup, **indicators** defined and assigned to projects ("For a project to report on an indicator in DevResults, the indicator must be assigned to that project"), granular progress logging, charts per project or program-wide, disaggregation, baselines and targets, reporting periods/cycles/fiscal years, **narrative questions**.
- Dashboard aggregates: all projects on an interactive map, "financial metrics for funds obligated, awarded and disbursed", results visualizations, "upcoming task notifications", "alerts for things like overdue milestones and over-budget projects", breakdowns "by sector, status and by mechanism".
- Collaboration surface per project: shared calendars, a "Facebook-style running log of **notes and comments**" (comments emailed to staff linked to the project), per-project **photo gallery** and **document library**.
- **Organizations** (partners): "Projects and organizations define who carries out a project, reports indicator data, or is associated with specific results." KB has "Entering Data: Partners", "Submission and Approval" (data submitted by partners goes through approval), and a recent article "Project-specific Permissions".
- Standard **forms** library "automatically populated with project information, including names, dates, contact information, and budget amounts".
- Geography machinery: places/facilities import, KML export, built-in administrative-boundary hierarchy, project locations auto-assigned to provinces/districts.
- No identified-participant registry observed: beneficiaries appear as aggregate counts inside indicator data (disaggregation), not as person records. No enrollment/roster/attendance machinery observed anywhere on the reachable surfaces.

### Salesforce Nonprofit Cloud — Program and Outcome Management (enterprise platform; Tier 2)

Evidence layer: **A for page content (official vendor page)**; strength capped at Tier 2 (help center unreachable).

- Positioning: "Unify your nonprofit program management, delivery, and evaluation… Make strategic decisions on what is and isn't working." FAQ: "Program and outcome management software helps program managers, service providers, case workers, and others **set up programs and services** so data is connected." FAQ also frames the alternative: "Managing programs with spreadsheets or multiple systems."
- Capability block "Programs and Services": "Reduce program complexity… **Know when you're not on track toward meeting program goals**. Save time by streamlining **attendance, service, and participant tracking**."
- Capability block "Service Delivery": "Gain a holistic view of interactions to understand which participants have urgent needs… Deliver wraparound care by making it easier to share information with external partners."
- Capability block "Service Schedules and Sessions": "Schedule individual service sessions and **enroll participants in bulk**, saving hundreds of staff hours in preparation for service delivery."
- Capability block "Program Participant Self-Service": a secure self-service portal where participants "directly **enroll in programs and services**".
- Capability block "Case Management" (adjacent, same solution): "guided intake process, manage inbound and outbound referrals, assign an entire case team…"; "Intake and Referrals": "guided flow from **referral to intake to program enrollment**."
- Capability block "Outcomes Management": "Track desired outcomes… Use **Outcome Activities** to connect programs or benefits that contribute to the desired end goal."
- Capability block "Indicators": "building your library of indicators. Connect them to **multiple outcomes or programs**… Use **time-bound performance periods** to track a program's starting point and end goal."
- Capability block "Outcomes Home Page": "understand if your indicators are on target, see recent results, manage assessments."
- Screens referenced: "action plan dashboard for youth training program planning", "holistic program management dashboard containing alerts, participation, and overview", "attendance summary portal", "internal staff view into how you setup a program participant's program enrollments".
- Cross-links on the same page: Data 360, Service Cloud, Tableau, MuleSoft, Slack, Omnistudio, Einstein AI ("generate a program performance summary").

### Bonterra Apricot (US human services; Tier 2)

Evidence layer: **A for page content (official vendor page)**; strength capped at Tier 2 (help center unreachable).

- Vendor positioning is **"Case management software for nonprofits"** — the vendor sells program management under the case-management banner. The vendor's own copy nevertheless centers programs: "Our case management solution **unifies participant and program data** into one platform… From intake to reporting"; "Whether you're managing **a few programs or operating across multiple sites**… ensure your programs run efficiently as you grow"; "Solve the challenges of **managing programs and delivering impact**."
- Feature list (vendor FAQ): "Case management: including tools for managing **caseloads, exits and enrollments, schedules, and network and internal referrals**"; forms and records (form designer, secure document folder, templates); reporting tools (**compliance reporting, aggregate reports**, inventory dashboard); workflow management (email triggers, automated rules, alerts); security/administration (role-based permissions, MFA, SSO); participant engagement (secure online forms, direct messaging, streamlined intake); "**attendance tracking**, and inventory management"; batch record creation; imports/API.
- AI add-on (Bonterra Que) copy exposes program semantics: "Highlight disengagement patterns or **missed milestones based on your program criteria**"; "Data integrity review… Identify missing fields, duplicates… before reporting deadlines"; "funder reporting and compliance reviews".
- Reporting pole: "Deliver clear, **funder-ready impact reports**"; "Measure program impact… measuring impact an integrated part of delivering services."
- Customer quote on the same page: "Having flexibility with our **program management software** and being able to adjust how we're collecting data to continually reflect programming has been key." (case-study customer)
- Tier names: Apricot Essentials / Pro / Enterprise (Essentials: "data capture, industry-leading case management, reporting and analytics"; Enterprise: "best-in-class reporting and dashboards, single sign-on, inventory management, API access").

### ActivityInfo (boundary sample, M&E machinery; Tier 1)

Evidence layer: **A (official documentation index)**.

- Documentation structure: "Information system design" (Database design, Form design, Permission design, Report design, Automations), "Using a database" (Data management, Mobile data collection, Formulas), integrations (ArcGIS, Power BI, R, Tableau, QGIS, MCP/AI, API).
- Site-wide use-case list: Monitoring & Evaluation, Humanitarian coordination, Case Management, Grant management, Impact measurement, Cash Voucher Assistance, Conservation, Disaster and Climate Risk Management.
- Observed machinery = structured data collection (forms, validation, mobile/offline), database organization, role-based permissions, reports/dashboards. **No program-offering planning/delivery loop observed** (no workplans, milestones, service schedules, session/attendance machinery, or program budgets on the reachable surfaces). This matches the M&E sibling pass's characterization of the sector: collection + indicator/reporting machinery.

## Cross-product Comparison

| Dimension | DevResults (development) | Salesforce NP Cloud (enterprise suite) | Apricot (human services) | ActivityInfo (boundary) |
|---|---|---|---|---|
| "Program" means | the whole portfolio of projects | set-up container for services & sessions | organizing unit for participant services | (database = attribution container; M&E machinery) |
| Central managed unit | project (formerly "activity") | program + services | program (vendor sells it as case management) | database / forms |
| Planning machinery | workplan: milestones, deliverables, reporting periods | service schedules and sessions | schedules; program criteria | — |
| Delivery tracking | checklists with sign-off, milestone due dates/overdue flags, budget vs disbursements/expenses | attendance, service delivery, participant tracking | attendance tracking, exits and enrollments, caseloads | — (form submissions only) |
| Identified people | not tracked (aggregate counts in indicators) | participants enrolled (bulk, self-service portal) | participants unified with program data | — |
| Money | per-project budget, line items, multiple funding sources, multi-currency, burn rates | not observed on the page | not observed on the page (inventory only) | — |
| Performance | results framework, indicators assigned to projects, baselines/targets, dashboards, alerts (overdue/over-budget) | program goals, outcomes + indicator library, time-bound performance periods, Outcomes Home | funder-ready dashboards, compliance/aggregate reports, missed-milestone signals | reports/dashboards over collected data |
| Oversight direction | donors, governance (funds obligated/awarded/disbursed) | program managers → leadership (what is/isn't working) | funders (compliance reporting) | donors/M&E officers |
| Partner/sub-grantee mechanics | organizations carry out projects, report data, submission/approval, project-specific permissions | external partners via Service Delivery sharing | network referrals | — |
| Adjacent suites on same page | IATI, Enterprise publishing | case management, Data 360, Tableau | case management is the banner; Impact Hub analytics | M&E use-case pages |

## Canonical Model

### Level 0 — Defining Invariant

Three jointly-held structures. If any one is removed, what remains is a neighboring Type or a non-Type:

1. **The program as the organization's managed offering of record.** A persistent, identified record for a defined program through which the organization delivers part of its mission — carrying at minimum identity (name), intent (goals/aims), and span (period/status). All program machinery attaches to this record. Remove it → generic project/task tools or a CRM wearing program labels; there is no offering to manage.

2. **Planned delivery organized under the program.** The offering's delivery is structured inside the system as planned elements over time — service schedules and sessions (service-delivery implementations) or activity workplans with milestones/deliverables and reporting periods (workplan implementations). Remove it → a program catalog/brochure with nothing planned; no "management" to do.

3. **Recorded delivery tracked against the plan and rolled up as program performance.** Execution records (services delivered, sessions held, attendance taken; milestones completed/sign-offs; indicator actuals) are attributed to the program and surfaced as program-level progress views, dashboards, and reports directed at management and oversight parties (funders, boards, donors). Remove it → a static plan archive; nothing is tracked.

Domain binding: the programs are the **mission-delivery offerings of a mission-driven organization**, planned and evaluated under funder/board oversight rather than commercial deliverables under a P&L. Remove this → generic Project Management Application (§03.07) or Professional Services Automation.

Jointly-held is load-bearing:

- 1+2 without 3 = program plans/catalog documents with no managed execution.
- 1+3 without 2 = tracked to-do items with no planned delivery structure (generic tracker with program labels).
- 2+3 without 1 = generic work management (workplans and tracking without mission-program semantics).

**Deliberately NOT in Level 0** (tested and rejected):

- Identified-participant enrollment/rosters/attendance — rejected: DevResults manages programs without tracking identified people (beneficiaries exist only as aggregate counts in indicator data). Enrollment is the service-delivery implementation's answer to "who receives the offering"; the workplan implementation answers with "which organization/project delivers and reports". The invariant is that delivery is organized and tracked, not that people are registered.
- Program budgets/funding sources — rejected: observed as first-class only at DevResults; absent from the Salesforce and Apricot pages (money may sit in fund-accounting/grant systems).
- Results frameworks/logframes as structured records — rejected: that is the Monitoring & Evaluation Platform's defining machinery; program products carry goals/indicators commonly but not as the framework-of-record center.
- Case episodes/case notes — rejected: Nonprofit Case Management's center; straddled by suite products but not required here.
- Cloud/mobile/AI/dashboards-as-product — era machinery.

### Level 1 — Common Mature Structure

Very common across the sample (and the sector) but not definitional:

- participant enrollment with an entry→active→exit lifecycle, rosters, attendance (service-delivery variants)
- program goals/outcomes with attached indicators, targets, time-bound performance periods
- program calendars / shared schedules
- documents, notes, photos, and activity feeds attached to the program/project
- referral management (inbound/outbound, internal and network)
- roles and permissions, including partner/sub-grantee visibility and submission/approval flows
- dashboards and alerts (overdue milestones, off-track goals, over-budget, disengagement signals)
- assessments (intake and progress measures)
- compliance/funder report generation from recorded data
- process templates and checklists with sign-off
- data-quality tooling (dedupe, missing-field review) feeding funder reporting

### Level 2 — Variant / Optional Structure

- per-program budget vs actuals with line items, multiple funding sources, multi-currency (development/humanitarian variant; DevResults)
- sub-grantee/partner reporting networks (organizations carry out projects and report data)
- participant self-service portal (direct enrollment; Salesforce)
- program portfolios aggregated by sector, geography, status, mechanism; GIS mapping of program locations
- geography intelligence (administrative boundaries, KML import/export)
- inventory/kit management (Apricot)
- case-management machinery co-sold in the same product (suite straddle)
- narrative (qualitative) reporting questions alongside indicators
- AI assistants (summaries, data-integrity review, disengagement signals)
- mobile/offline data collection feeding program reporting
- deployment variants: multi-tenant SaaS vs self-managed server (ActivityInfo pole, M&E side)

### Level 3 — Vendor-specific

- DevResults: "project (formerly 'activity')" terminology; IATI export; FedRAMP authorization; Enterprise publishing; standard-forms auto-population with project data; burn-rate infographics; "discussions" feed; program targets vs project targets duality.
- Salesforce: Outcome Activities; Experience Cloud participant portal; Power of Us licensing (10 free licenses); Einstein program-performance summaries; Data 360/Tableau/MuleSoft packaging.
- Apricot: Bonterra Que AI; Impact Hub analytics (built on Amazon Quick Suite); Data Standards library; Essentials/Pro/Enterprise tiering; vendor sells the Type under the "case management" banner.
- ActivityInfo: MCP/AI-assistant integration; R package; self-managed server distribution.

## Vendor-specific Findings

- The strongest single-product finding in-sample is DevResults' money machinery (budget line items vs disbursements/expenses, multiple funding sources, multi-currency) — **product-specific in this sample**, held at Level 2.
- Salesforce's "Outcome Activities" (linking programs/benefits to desired end goals) — vendor-specific construct, Level 3.
- Apricot's Data Standards (aligning metrics across programs/partner organizations) — vendor-specific, Level 3.
- DevResults' administrative-boundary geography intelligence — vendor-specific, Level 3.

## Rejected Findings

1. "Nonprofit program management = case management renamed." Rejected: the DevResults pole manages programs with workplans/budgets/indicators and no case episodes; the case-management reading only covers the human-services pole. The two are real neighbors with different centers.
2. "Enrollment of identified people is definitional." Rejected via DevResults (aggregate-count beneficiary model).
3. "Program budget is definitional." Rejected: one-pole evidence only.
4. "This leaf is an alias of Monitoring & Evaluation Platform." Rejected: removal tests pass both directions (M&E machinery lacks the offering's planning/delivery loop; program management does not require the results-framework machinery of record). Confirms the M&E sibling's note that in M&E products, activities/projects are attribution containers and reporting units, not schedulable delivery work.
5. "This leaf is an alias of Project Management Application (§03.07)." Rejected: generic PM lacks program-offering semantics (services/sessions to participants, beneficiary counts, funder oversight, enrollment/attendance). A program office *can* run on generic PM tools, but the defining structures are not native there.
6. "This leaf is a slice of Nonprofit Management Platform." Rejected: the platform pass defines the whole-operations umbrella whose function domains (including programs) are purchasable/absent slices; this leaf is the single-domain depth the platform treats as a slice. Keep-both, consistent with that pass's own packaging analysis.

## Boundary Findings

1. **vs Nonprofit Case Management (§25, processed):** case = a person's bounded service episode (intake→service→exit under a program, with caseworker and caseload); program = the organization's planned offering. Enrollment binding means each references the other's central object (a case is opened *under* a program; a program counts *participants* who may be case clients). Suite products straddle: Salesforce sells case management on the same page as program management ("referral to intake to program enrollment"); Apricot is banner-labeled "case management" while a customer on the same page calls it "our program management software". Removal tests: strip case-episode machinery (caseloads, case plans, case notes) → program planning/delivery coordination remains (this Type); strip the program container/planning machinery → case management remains. **Boundary HELD, keep-both. Discharges the case-management pass's flag.**
2. **vs Beneficiary Management (§25, processed):** registry of served people with participation/assistance events vs the offering side. A program-management product need not hold a person registry (DevResults). **Keep-both.**
3. **vs Monitoring & Evaluation Platform (§25, processed):** M&E = results framework of record + indicator actuals per reporting period + accountability reporting loop; program management = the offering's plan→deliver→track→report loop. Indicator machinery is common in both (overlapping vocabulary confirmed vendor-side: DevResults markets both "M&E software" and "project management tool"). Removal tests pass both directions. **Keep-both; ratifies the M&E pass's flag.**
4. **vs Project Management Application (§03.07):** generic work management vs mission-program semantics. The workplan implementation (DevResults) is the closest straddle — its workplan/milestone/checklist machinery is PM-shaped, but it exists only inside program semantics (program targets, funder funds-flow, partner reporting, indicator assignment). **Keep separate; light flag for the §03.07 pass (unprocessed).**
5. **vs Nonprofit Grant Management (§25, processed):** funding relationships vs delivery offerings; a program is typically funded by grants but the central objects differ (grant = funder×amount×terms; program = offering×delivery×participants). **Keep-both.**
6. **vs Nonprofit Management Platform (§25, processed):** whole-operations umbrella vs single-domain depth. **Keep-both** (consistent with the platform pass's "domains as slices" framing).
7. **Label diffusion (new finding):** no sampled product's primary vendor banner is exactly "nonprofit program management": the vendor banners are "M&E software" (DevResults), "case management" (Apricot), "Program and Outcome Management" (Salesforce). The Type is real but sold under adjacent labels; "program management" additionally collides with the PMI portfolio sense (DevResults' "program" = portfolio). Worth recording for the taxonomy pass.

## Historical / Market-Sample Check (§24 procedure)

- Paper-era program office: a program folder/binder containing the program plan (goals, planned activities, schedule), session logs and attendance sheets, a participant register, staff assignments, a budget worksheet, and a quarterly report typed for the funder/board — satisfies all three Level-0 legs at analog level.
- Spreadsheet era: a program workbook (activity schedule + enrollment tab + budget columns + planned-vs-actual report tab) satisfies.
- Older/regional products: community-based organizations running programs on paper rosters, and 1990s–2000sAccess/Excel-based program trackers, satisfy without cloud, AI, dashboards-as-product, or portal machinery.
- The definition does not name service sessions, attendance, enrollment, budgets, or indicators — every modern implementation in the sample realizes the three legs differently, so no era/sector pattern is frozen into the core.

## Uncertainties

1. Whether a "pure" program-management-only product population exists (all three sampled products bundle adjacent machinery: M&E, case management, or platform services). The Type may characteristically ship as a domain inside broader systems rather than as a standalone category. Not resolvable from the reachable evidence.
2. Salesforce object-level structure (the exact data objects behind "programs and services", enrollment, sessions) — help center unreachable; not asserted.
3. Commonality of program budgets beyond the development pole — unverified (two of three samples silent on the reachable pages).
4. Exact enrollment lifecycle states and statuses — not verified; no exact status names are asserted.
5. Apricot's program-level machinery depth (vs its case-level machinery) — product-page evidence only; the vendor's banner is "case management", so the balance between program and case machinery inside Apricot is not fully verifiable from reachable sources.
6. Volunteers' and events' linkage to programs — plausible and implied by suite positioning (Bonterra sells volunteer/event products alongside) but not directly observed as program-attached machinery; held unverified.

## Final Synthesis

Nonprofit Program Management is the mission-driven organization's **program-delivery management system**: the defining core is exactly three jointly-held structures — the program as the organization's managed offering of record (identity + intent + span, everything attaches to it), planned delivery organized under the program (service schedules/sessions in service-delivery implementations; activity workplans with milestones/deliverables and reporting periods in workplan implementations), and recorded delivery tracked against the plan and rolled up as program performance for management and oversight parties (funders/boards/donors). Identified-participant enrollment, budgets, results frameworks, and case episodes are common or variant capabilities, not definitional — the DevResults pole proves the Type stands without people registries or budgets, and the M&E/case boundaries hold by removal tests in both directions. The market realizes one Type across two poles (service-delivery-centric human services; workplan/results-centric international development) plus a suite-module posture, sold under diffuse vendor labels. Historical check passes at the paper program-folder level.
