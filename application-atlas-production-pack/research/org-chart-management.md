# Research Notes — Org Chart Management

## Research Goal

Understand what an Org Chart Management application really is, from real products: what its core objects are (people, positions, units, reporting lines), how the chart is built and kept current, how it is shared and consumed, and where its boundary sits against the Organization Design Platform (its closest sibling, which pre-hung a joint-review flag against this leaf), HRIS, diagramming tools, succession planning, and career pathing.

## Initial Boundary

Working hypothesis before research:

- Core use: the organization maintains "who reports to whom" as a living record and renders it as a navigable org chart.
- Primary users: HR/people-ops admins maintain it; everyone else consumes it; leaders use it to see the organization.
- Nearest neighbors: Organization Design Platform (scenarios/impact), HRIS (employee records; org chart often a feature view), Diagramming Application (org chart as shapes), Succession Planning Platform (org-chart navigation as capability), Career Pathing Application (role structures + requirements).
- Unknowns: is the chart data-driven or drawn? Is the chart the record or a rendering? Is company-wide publishing definitional? Is the time dimension (history/future) definitional? Is directory/profile content (photos, bios) definitional?

## Research Questions

1. What is the core object structure: person-under-manager, or person + position + unit + multiple relationship types?
2. How does people data enter the product: manual entry, CSV/Excel import, HRIS/ERP sync?
3. What does "management" mean operationally: which changes are made, how do they flow to the chart?
4. Is the chart generated from records (synchronized) or a hand-maintained drawing? What do vendors name as the pre-history?
5. What is shown on cards/boxes: name/title only, or photos, contact details, profiles, KPIs, open jobs?
6. How is the chart shared/published: interactive links, embeds, print, PDF/PPT export?
7. What time dimension exists: past states, future-dated views, history?
8. What rules matter: permissions, sensitive-data visibility, sync precedence?
9. Where is the boundary with Organization Design Platform (scenario/impact loop), HRIS, diagramming?

## Representative Products

Selected for market representation, documentation quality, different philosophies, different customer tiers:

| Product | Pole | Tier |
|---|---|---|
| Pingboard (by Workleap) | standalone cloud org chart + employee directory, self-serve | SMB / mid-market |
| ChartHop | org chart at the center of a people-operations platform | mid-market |
| Nakisa Org Chart Suite | enterprise org charting over HRIS/ERP data, part of a Workforce Planning portfolio | large enterprise |

Rejected/unreachable samples (see Sources): Organimi (403 ×2), OrgChart Now (transport error ×2), Apoint (transport error ×2), Lucidchart org-chart page (403), Microsoft Visio org-chart page (404 on the attempted URL). The diagramming-pole boundary is instead supported by vendor naming ("No more need for Excel, Visio, or PowerPoint" — Nakisa) and by the already-processed Diagramming Application research notes (org-chart connector/drop-on-manager mechanics documented there from official docs).

## Sources

Research date: 2026-09-08.

- Pingboard product page (Workleap) — https://www.pingboard.com/ — includes product FAQ (import methods, HRIS sync, planning org charts). Tier-2 official product page with FAQ.
- ChartHop Help Center — "Org Chart" — https://docs.charthop.com/org-chart — Tier-1 operational documentation.
- ChartHop Help Center index — https://docs.charthop.com/ — confirms platform scope (Org Chart, Headcount Planning, AI Scenario Planner, Dashboards, Performance Reviews, Engagement Surveys, ChartHop for Employees).
- Nakisa Org Chart Suite product page — https://nakisa.com/products/org-chart-software/ — Tier-2 official product page, feature-rich. Site navigation confirms Org Chart Suite / Org Design Suite / Strategic Workforce Planning Suite as three separate suites and a "Nakisa vs OrgPublisher by PeopleFluent" comparison page.
- Sibling passes (context, not fetched this pass): research/organization-design-platform.md (ChartHop scenarios/planning docs, Nakisa Org Design Suite page), research/diagramming-application.md (Visio org-chart mechanics from official docs), research/succession-planning-platform.md, research/career-pathing-application.md, research/workforce-planning-platform.md.

> Source-access limitation: Organimi and OrgChart Now — both dedicated org-chart vendors — could not be reached (403 / transport errors, 2 attempts each). Apoint and Lucidchart also unreachable. Claims are therefore calibrated to three products; no precise market-share or vendor-count claims are made. Details of Organimi/OrgChart Now were NOT filled in from model memory.

## Product A — Pingboard (Workleap)

### Key observations (evidence layer A unless noted)

Official product page (fetched 2026-09-08):

- Self-description: "Pingboard is a cloud-based org chart and employee directory solution, and one of Workleap's employee experience products." The Type name appears verbatim: "Org Chart and Employee Directory".
- Purpose framing: "When team structure, reporting lines, and roles are visible to everyone, collaboration becomes easy." — the chart as a company-wide visibility surface.
- Two named surfaces: **Org chart** ("Effortlessly illustrate reporting structures, departments, and cross-functional team compositions through an intuitive interface") and **Directory** ("Deep dive into who does what within your org").
- Visualize / Connect / Strategize framing: visualization of reporting lines; employee discovery of collaborators ("Who's Who" game, custom profiles with "unique interests and skills"); "Plan for the future of your organization with smarter resource planning."
- **Planning org charts**: "Create private org charts that show you how to allocate resources based on different scenarios. Invite others to comment and provide feedback on your private planning org charts." — a light, private scenario surface (comment-level, no documented impact measurement). Classified Optional / product-specific-leaning; the full scenario/impact loop is the Organization Design Type.
- Data ingestion (FAQ): "You can connect your HRIS using one of our automated integrations or you can upload an Excel file of the relevant employee data." And: "If you have an existing org chart in your current HRIS, you'll just need to sync to Pingboard to import the employee data. Once that's done, you can replicate your org chart in Pingboard."
- Integration posture: "Integrate directly into your HRIS to build simple, relevant, loved experiences."
- Audience: all employees ("Boost visibility of employees across the organization"), HR/people-ops as operators; part of a broader people-management suite (performance reviews, surveys, meetings).

## Product B — ChartHop

### Key observations (evidence layer A)

Official Help Center "Org Chart" article (fetched 2026-09-08):

- Precondition: "After you have uploaded your employee roster and historical data to ChartHop, you can use the Org Chart to navigate parts of your organization that include its departments, teams, and employee profiles." — the chart is a rendering of roster records; departments/teams/profiles are part of the model.
- The chart counts "the total number of people and open jobs in your org. Open jobs are included in the total regardless of their recruiting status." — open jobs are first-class chart objects alongside people.
- Navigation mechanics: zoom in/out, vertical/horizontal orientation, "expansion arrows" to open reporting lines, hover preview of the employees and jobs underneath.
- "Searching the Org Chart: … search for jobs, people, or groups. To view an open role or a person's profile, enter the job title… To locate a person, enter their name and click it to load their profile."
- Permissions surface into the chart: "Double-click any card in the Org Chart to view the employee profile information for that employee. The data you see depends on your permissions."
- **Time dimension**: "You can use the date slider at the top of the page to view the Org Chart as it was in the past, or as it will appear in the future when new hires join your organization… Bookmark this view to save an always-current snapshot of your ChartHop org."
- Visualize menu: "highlight specific fields within your Org Chart… employee cards display color-coded labels. For example, if you select Department, each employee's department is displayed."
- Export/screenshot: "You can Export the org chart by clicking the Download/Export button… Screenshot Mode… will turn the background of the Org Chart white and remove any PTO information from the People cards." — export-aware sensitive-data behavior.
- Platform context (docs index): Org Chart sits beside Headcount Planning, AI Scenario Planner, Dashboards, Performance Reviews, Engagement Surveys, "ChartHop for Employees" — the org chart is the center of a bundled people platform. (The scenario/planning side was documented in the sibling Organization Design pass; from this leaf's perspective ChartHop demonstrates bundling, not Type identity.)

## Product C — Nakisa Org Chart Suite

### Key observations (evidence layer A; product-page depth, no help-center access)

Official product page (fetched 2026-09-08):

- Positioning: "The Nakisa Org Chart Suite enables you to automatically create org charts to visualize and analyze complex organizational structures. With native ERP integrations, unparalleled scalability, and powerful HR analytics… best org chart software for large enterprises."
- Data-driven chart generation: "Automatically create and update org charts in real time… You'll accurately represent team structures and get automated updates of the employee data right from your ERPs."
- Complex structures: "simplify the visualization of complex reporting structures such as matrix and dotted lines so that you can better understand org relationships."
- Summary charts: "Nakisa's summary charts simplify and present large amounts of HR data… view as much or as little detail as necessary for making tactical and strategic HR staffing decisions."
- Saved views: "Configure and save org chart views."
- KPI overlay: "Visualize key HR KPIs right in your org chart… Proactively achieve optimal span of control, layers, and headcounts. Gain insight into how your organization's staffing has improved (or not) over time."
- ERP integrations named: "Use Nakisa's native ERP integrations with SAP HCM, SAP SuccessFactors (SFSF), Workday, Oracle and more. Quickly create intuitive organizational charts that easily import your HR data and automatically self-update. **No more need for Excel, Visio, or PowerPoint.**" — the vendor names the pre-history tools of this Type (spreadsheet + drawing + presentation).
- History: "Check historical org charts and track your organization evolution… pull org charts from previous years. See what you need to see, including changing titles, responsibilities, team structures, chains of command… Easily compare years of change."
- Relationship to org design: "Once you've designed your future organization with Nakisa OrgDesign to align with upcoming changes (reorganizations, mergers and acquisitions, reduction in force, succession planning, and more), you can use Org Chart to create organizational charts, visualize, and share them with your team." — the scenario/design work lives in the Org Design Suite; the Org Chart Suite visualizes and shares.
- Sharing/export: "Share your organization charts with ease. Give interactive links to your team so that they can explore org changes on their own time. Export your organizational charts in PDF, PowerPoint, or PNG… Keep everyone in your company informed of the current structure and metrics as well as future plans."
- Portfolio framing (vendor's own words): "The broader Nakisa Workforce Planning Portfolio is made up of three software suites: The Org Chart Suite, offering powerful, intuitive organization visualization; the Org Design Suite, offering top-to-bottom org scenario modeling and organizational design; and the Strategic Workforce Planning Suite, offering cutting edge analytics and headcount planning." — first-hand confirmation that the market treats org-charting and org-design as separate products.
- Compliance/audit: "Export data to demonstrate compliance or facilitate audits with a couple of clicks."
- A "Nakisa vs OrgPublisher by PeopleFluent" comparison page exists in site navigation — the vendor positions against a legacy dedicated org-charting product (legacy product's details not fetched; not asserted).

## Cross-product Comparison

| Dimension | Pingboard | ChartHop | Nakisa Org Chart Suite | Layer |
|---|---|---|---|---|
| Self-description | "org chart and employee directory solution" | org chart as core navigation surface of a people platform | "automatically create org charts to visualize and analyze complex organizational structures" | A×3 |
| Core object | people in reporting structure + profiles/directory | roster records (people, jobs, departments, teams, profiles) rendered as chart | employee/HR data from ERPs organized into reporting structures incl. matrix/dotted lines | A×3 |
| Data ingestion | HRIS integration or Excel upload | employee roster + historical data upload (+ platform syncs) | native ERP integrations (SAP HCM, SuccessFactors, Workday, Oracle), auto-update | A×3 |
| Chart ↔ data synchronization | chart replicated from imported data; maintained in product | chart renders uploaded/synced roster; open jobs counted live | chart "automatically self-updates" from ERPs in real time | A×3 |
| Maintenance operations | implied in-product editing + re-sync | in-product records; future states via planned hires | charts reflect ERP changes; history retained | A (B on editing detail) |
| Directory/profiles | first-class (directory, custom profiles, photos implied, Who's Who) | profiles per person; "data you see depends on your permissions" | HR data on cards; summary charts | A (directory depth product-specific) |
| Search | implied (directory product) | documented (people/jobs/groups) | implied by "visualize and analyze" framing | B |
| Views/filtering/coloring | not documented this pass | Visualize menu, color-coded labels | configure & save views; summary charts | A×3 (forms vary) |
| Sharing/publishing | company-wide visibility framing | Download/Export; Screenshot Mode | interactive links; PDF/PPT/PNG export; "keep everyone informed" | A×3 |
| Time dimension | not documented | date slider: past and future states | historical org charts, compare years | A×2 (B for the third) |
| Open jobs / vacancies | not documented | open jobs counted in chart | vacant positions referenced in a customer quote (weak) | A (1 strong) |
| KPI/analytics overlay | not documented | not documented on this page | span of control, layers, headcount KPIs in chart | A (1 product) |
| Matrix / dotted lines | not documented | not documented on this page | documented | A (1 product) |
| Private scenario/planning charts | "Planning org charts" (private, comments) | full scenarios in the platform (AI Scenario Planner; documented in sibling pass) | future org designed in Org Design Suite, then visualized | A — different depths; full loop = Org Design Type |
| Permissions | not documented this pass | profile data permission-scoped | compliance/audit export posture | A (1 strong, 1 partial) |
| Export formats | not documented | Download/Export; screenshot | PDF, PowerPoint, PNG | A×2 |
| Sensitive-data handling | not documented | Screenshot Mode strips PTO | audit/compliance export framing | A (1 product) |

## Canonical Model — L0 / L1 / L2 / L3

### L0 — Defining Invariant (deliberately minimal)

1. **The reporting structure of record.** The organization's people — and commonly positions and units — held as the product's maintained records of who reports to whom (manager/subordinate relationships giving the structure its shape). Remove → a flat employee directory / HRIS roster with no reporting semantics.
2. **The chart as the structure's synchronized rendering.** The org chart the product shows is the authoritative view of that record: editing the chart changes the record, and record/sync changes update the chart — the chart and the structure are one maintained thing, not a detached drawing. Remove → a diagramming application (shapes with no records behind them) or a data table with no chart.
3. **Standing maintenance against organizational change.** The product's ongoing job is keeping that record current as people join, move, and leave and as branches are reorganized — not producing one-off drawings. Remove → a one-off chart generator; the "management" is gone.

Jointly-held load-bearing: 1 alone = directory/roster; 2 alone = drawing tool; 1+3 without 2 = HRIS territory (records maintained, no chart center); 2+3 without 1 = a hand-maintained drawing — the pre-history the vendors themselves name (Excel/Visio/PowerPoint). In the analog ancestor (the wall chart maintained by HR), legs 1 and 2 are fused: the wall chart IS both the record and the rendering.

### L1 — Common Mature Structure (very common, not defining)

- Employee directory and profiles (photos, titles, contact details, bios/interests) — the people-facing layer around the chart (Pingboard makes the directory a named co-surface; ChartHop profiles; Nakisa HR-data cards).
- Search across people/jobs/groups (ChartHop documented; directory-class products imply it).
- Data sourcing implementations: automated HRIS/ERP integration, CSV/Excel import, manual entry (all three products; forms differ).
- Visualization controls: filter/color-code by attribute, saved views, zoom/orientation (ChartHop Visualize menu; Nakisa saved views; universal chart interactions).
- Sharing/publishing: interactive links for the company, export to PDF/PPT/PNG/print (Nakisa explicit; ChartHop export; Pingboard company-visibility framing).
- Time dimension: viewing the chart at past dates or future-dated states (ChartHop date slider; Nakisa historical charts). Signature in digital products but absent from the analog wall chart — hence not definitional.
- Open jobs/vacancies visible in the structure (ChartHop counts them).
- Permission-scoped visibility of what each viewer sees (ChartHop).

### L2 — Variant / Optional Structure

- Matrix / dotted-line secondary reporting visualization (Nakisa; structure-heavy enterprises).
- Summary/aggregate chart views over large orgs (Nakisa).
- KPI overlays on the chart (span of control, layers, headcount) (Nakisa) — drifts toward org-design/people-analytics territory.
- Private planning charts (scenario-light: private copies for resource planning, with comments) (Pingboard) — the deep scenario/impact loop belongs to Organization Design Platform.
- Position modeling (positions vs people, vacancy states) — enterprise pole; person-under-manager suffices at the light pole.
- Company-wide social/engagement features around the directory (interest profiles, "who's who" games) (Pingboard).
- Sensitive-data export controls (e.g., stripping sensitive fields from shared images) (ChartHop).
- Audit/compliance export of structure data (Nakisa).
- AI assistance over the structure (ChartHop platform; era-current, optional).

### L3 — Vendor-specific (stays here, not in the final document)

- Workleap suite packaging: Pingboard as one product in a talent-management portfolio (performance reviews, surveys, meetings) with "AI in HR University" content marketing; "Who's Who game" as a named engagement feature.
- ChartHop CQL/Carrot query language, Carrot reference, AI Agent Memory, "ChartHop for All (Org-Rollouts)" academy framing; expansion-arrow hover previews; title abbreviation ("Senior Vice President" → "SVP"); bookmarkable always-current chart views.
- Nakisa suite naming and split (Org Chart Suite / Org Design Suite / Strategic Workforce Planning Suite), "Value Acceleration Workshop" services, Decision Intelligence cross-sell, buyer's guides/RFP content, named ERP connectors, "Nakisa vs OrgPublisher" competitive page, customer quotes (COTY VP HRIS; Sinarmas HRIS Planning Manager).

### Rejected Findings (considered and NOT promoted)

- **"Employee directory is the Type"** — rejected: the directory is the people layer around the chart; a directory without reporting structure is not org chart management (Pingboard itself names both surfaces separately).
- **"HRIS/ERP sync is definitional"** — rejected: manual entry and file import are first-class paths at the light pole (Pingboard FAQ); sync is the dominant enterprise implementation, not the invariant.
- **"Time travel (past/future views) is definitional"** — rejected: the analog wall chart and the file-based era satisfy the Type without it; held as L1 despite being signature in digital products.
- **"Photos/profiles are definitional"** — rejected: enterprise record-centric charts show HR data fields, not social profiles.
- **"Company-wide social discovery features are definitional"** — rejected: single-product leaning (Pingboard), engagement-oriented, not structural.
- **"Planning charts make this an org-design Type"** — rejected: Pingboard's planning charts are private copies with comments (no documented impact measurement); the full scenario→measure→apply loop is the Organization Design Type's differentiator, confirmed vendor-side by Nakisa's suite split.

## Boundary Findings

1. **vs Organization Design Platform (closest sibling — JOINT REVIEW DISCHARGED).** The org-design pass flagged: "both hold the same structural model; the tested difference is the scenario/impact loop; Nakisa ships Org Chart Suite and Org Design Suite as two separate products while ChartHop bundles both; probable adjacent-Types-with-shared-core relationship." This pass confirms and ratifies keep-both: the scenario/impact loop (propose in an isolated copy → measure impact → apply) is the org-design differentiator, and this Type's core (structure of record + synchronized chart + standing maintenance) contains none of it. First-hand vendor evidence for the split: Nakisa's own portfolio page separates "The Org Chart Suite, offering powerful, intuitive organization visualization" from "The Org Design Suite, offering top-to-bottom org scenario modeling and organizational design," and its workflow text says future organizations are *designed* in OrgDesign and then *visualized and shared* with Org Chart. ChartHop bundles both (docs index lists Org Chart, AI Scenario Planner, Headcount Planning). Remove-test: remove the scenario/impact loop → Org Chart Management remains; remove the maintained current-structure chart of record → Organization Design Platform remains.
2. **vs HRIS / HCM / Employee Record System.** The HRIS is the system of record for employee data and HR processes; its org chart (where present) is a feature view over records. This Type's center of gravity is the reporting structure and its chart. Evidence: standalone org-chart products exist without HRIS process machinery (Pingboard: people arrive by HRIS sync *or* Excel upload — no HR processes claimed); conversely the enterprise pole exists precisely to visualize what HRISs hold (Nakisa: "import your HR data… from your ERPs"). The relationship is upstream-feeder, not identity. An HRIS's embedded chart is a module of that Type, not this Type standing alone.
3. **vs Diagramming Application.** Diagramming tools draw org charts as shapes (the diagramming pass documents org-chart connector/drop-on-manager mechanics); there are no person records, no synchronization between chart and roster, no standing maintenance semantics. Vendors of this Type name the drawing tool as the replaced pre-history (Nakisa: "No more need for Excel, Visio, or PowerPoint"). Remove-test: remove the record layer (chart edits writing to maintained records) → Diagramming Application territory.
4. **vs Succession Planning Platform.** Succession centers key roles, candidate slates, and readiness standing; org-chart navigation is one of its standard capabilities (recorded in that pass). This Type holds no key-role/candidate/readiness semantics. The org chart is the structural substrate succession tools commonly sit on or beside.
5. **vs Career Pathing Application.** Career pathing owns the organization's career structure (roles/levels/progression links + requirements) and employee-facing exploration; this Type owns people in reporting lines. A role/level library is not a reporting structure (seam recorded by that pass, confirmed from this side).
6. **vs Workforce Planning Platform.** Workforce planning centers demand/supply of headcount over a time horizon; this Type centers the current reporting structure as a record. Structure changes *flow* toward org-design/org-chart surfaces (recorded in that pass's handoff description); the chart of record is downstream of planning, not the planner.
7. **Directory-adjacent surfaces.** Intranets/employee portals and people-search tools commonly embed an org chart or people directory. Where that view is a feature over someone else's records, it is not this Type standing alone; the Type requires the structure and its maintenance as the product's own center.

## Historical / Market-Sample Check

- **Analog ancestor**: the wall-mounted (or printed) org chart maintained by HR — the chart is both the record of who reports to whom and the authoritative rendering, updated by hand as people join/move/leave. Satisfies all three L0 legs with legs 1+2 fused. Definition holds.
- **Spreadsheet + drawing era**: a maintained manager-column spreadsheet plus a Visio/PowerPoint org chart redrawn after each change — the era the vendors themselves name (Nakisa: "No more need for Excel, Visio, or PowerPoint"; Pingboard FAQ's "Excel file" ingestion). Where the chart is kept current as the structure changes, the Type's job is satisfied; where a chart is drawn once and never maintained, the third leg fails — correctly a drawing, not chart management.
- **Older dedicated org-charting products** (1990s–2000s desktop charters; the legacy competitor Nakisa compares against): per the sibling org-design pass's boundary note, these sit on the org-chart side of the seam; this pass adds first-hand evidence that a current enterprise vendor still positions against one. Their details were not fetched; no specific claims made.
- The L0 names no SaaS delivery, HRIS integration, AI, photos, time sliders, or publishing tiers — none are required to recognize the Type in older or differently positioned products. No over-fitting detected.

## Uncertainties

- Editing mechanics at the enterprise pole: Nakisa's page emphasizes automatic ERP-driven updates; direct in-chart editing (drag re-parenting) is not documented from reachable sources. Stated with reduced precision in the final document ("in many products the chart is also the editing surface" — evidenced at the light/mid poles, held as common at enterprise).
- Whether company-wide publishing is universal: all three sampled products frame the chart as something consumed beyond its maintainers, but Organimi/OrgChart Now (likely export/print-centric) were unreachable. Held as strong-common (L1), not definitional.
- Directory depth varies (social profiles vs HR fields); sample of three cannot establish the distribution.
- Group/department objects vs pure reporting tree: ChartHop models departments/teams/groups explicitly; Nakisa visualizes "complex reporting structures"; Pingboard mentions departments and cross-functional compositions. Held: units/groupings common; exact modeling varies.
- Multi-manager (matrix) handling: only Nakisa documents matrix/dotted-line rendering; held as variant.

## Final Synthesis

An Org Chart Management application is the organization's reporting-structure system of record: people (and commonly positions and units) organized under managers as maintained records, whose authoritative rendering is the org chart the product shows, shares, and exports — kept current as the organization changes. Everything commonly bundled around it — the employee directory and profiles, search, HRIS/ERP synchronization, visual filters and saved views, interactive publishing and PDF/PPT export, past/future time views, open-job visibility, KPI overlays, permission scoping — is standard mature structure or optional, not defining. The closest sibling, the Organization Design Platform, shares the structural model but adds the scenario/impact loop; vendors themselves ship the two as separate products while some platforms bundle both. The Type stands alone without any HR process machinery: its center is the structure of record and its chart.
